import { NextResponse } from 'next/server'
import Stripe from 'stripe'

export async function POST(req: Request) {
  if (!process.env.STRIPE_SECRET_KEY || !process.env.STRIPE_WEBHOOK_SECRET) {
    return NextResponse.json({ error: 'Stripe not configured' }, { status: 501 })
  }

  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
    apiVersion: '2025-05-28.basil',
  })

  const body = await req.text()
  const sig = req.headers.get('stripe-signature')

  if (!sig) {
    return NextResponse.json({ error: 'Missing stripe-signature header' }, { status: 400 })
  }

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET)
  } catch (err) {
    const message = err instanceof Error ? err.message : 'Webhook signature verification failed'
    console.error('[webhook] Signature error:', message)
    return NextResponse.json({ error: message }, { status: 400 })
  }

  try {
    switch (event.type) {
      case 'checkout.session.completed': {
        const session = event.data.object as Stripe.Checkout.Session
        const listingId = session.metadata?.listingId
        const listingTitle = session.metadata?.listingTitle
        const customerId = session.customer
        const paymentIntent = session.payment_intent

        console.log('[webhook] Payment complete:', {
          listingId,
          listingTitle,
          customerId,
          paymentIntent,
          amount: session.amount_total,
        })

        // TODO: After Supabase is connected —
        // 1. Create order record in DB
        // 2. Generate signed download URL (24h TTL) via Supabase Storage
        // 3. Send confirmation email with download link
        break
      }

      case 'payment_intent.payment_failed': {
        const pi = event.data.object as Stripe.PaymentIntent
        console.error('[webhook] Payment failed:', pi.id, pi.last_payment_error?.message)
        break
      }

      case 'charge.refunded': {
        const charge = event.data.object as Stripe.Charge
        console.log('[webhook] Refund processed:', charge.id)
        // TODO: Revoke download access in DB
        break
      }

      default:
        // Unhandled event type — safe to ignore
        break
    }
  } catch (err) {
    console.error('[webhook] Handler error:', err)
    return NextResponse.json({ error: 'Webhook handler failed' }, { status: 500 })
  }

  return NextResponse.json({ received: true })
}

// Required: disable body parsing so we get raw body for signature verification
export const config = {
  api: { bodyParser: false },
}
