import { NextResponse } from 'next/server'
import Stripe from 'stripe'
import { STRIPE_PRICE_IDS } from '@/lib/stripe-products'

const LISTING_TITLES: Record<string, string> = {
  '1': 'Life After Ozempic',
  '2': 'The Muscle-Asset Protocol',
  '3': 'The Perimenopause Career Survival Guide',
  '4': 'The Sandwich Generation Toolkit',
  '5': 'The 30-Day Elder Care Crisis Manual',
  '6': 'The AI-Safe Family',
  '7': 'The Value-First Budget',
  '8': 'The Microplastics Detox',
}

export async function POST(req: Request) {
  if (!process.env.STRIPE_SECRET_KEY) {
    return NextResponse.json(
      { error: 'Stripe not configured. Add STRIPE_SECRET_KEY to Vercel environment variables.' },
      { status: 501 }
    )
  }

  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
    apiVersion: '2026-04-22.dahlia',
  })

  let listingId: string
  try {
    const body = await req.json()
    listingId = body.listingId
  } catch {
    return NextResponse.json({ error: 'Invalid request body' }, { status: 400 })
  }

  if (!listingId) {
    return NextResponse.json({ error: 'listingId is required' }, { status: 400 })
  }

  const priceId = STRIPE_PRICE_IDS[listingId]
  if (!priceId) {
    return NextResponse.json({ error: 'Listing not found' }, { status: 404 })
  }

  const baseUrl = process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:3000'

  try {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [{ price: priceId, quantity: 1 }],
      mode: 'payment',
      success_url: `${baseUrl}/checkout/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${baseUrl}/listings/${listingId}`,
      metadata: { listingId, listingTitle: LISTING_TITLES[listingId] || '' },
      invoice_creation: { enabled: true },
    })

    return NextResponse.json({ url: session.url })
  } catch (err) {
    const message = err instanceof Error ? err.message : 'Stripe session creation failed'
    console.error('[checkout] Stripe error:', message)
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
