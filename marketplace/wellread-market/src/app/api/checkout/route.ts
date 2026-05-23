import { NextResponse } from 'next/server'
import { auth } from '@clerk/nextjs/server'

export async function POST() {
  const { userId } = await auth()
  if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })

  // Stripe checkout session creation goes here after env vars are configured
  return NextResponse.json({ error: 'Configure STRIPE_SECRET_KEY in Vercel environment variables' }, { status: 501 })
}
