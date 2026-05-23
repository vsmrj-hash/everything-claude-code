import { NextResponse } from 'next/server'

export async function POST(req: Request) {
  const sig = req.headers.get('stripe-signature')
  if (!sig) return NextResponse.json({ error: 'No signature' }, { status: 400 })
  // Webhook processing goes here after Stripe keys are configured
  return NextResponse.json({ received: true })
}
