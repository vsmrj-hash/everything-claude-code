'use client'

import { useState, Suspense } from 'react'
import Link from 'next/link'
import { Lock, BookOpen, Loader2 } from 'lucide-react'
import { useSearchParams } from 'next/navigation'
import { formatPriceDollars } from '@/lib/utils'

const LISTING_DATA: Record<string, { title: string; price: number; author: string }> = {
  '1': { title: 'Life After Ozempic', price: 19.99, author: 'Dr. Sarah Chen' },
  '2': { title: 'The Muscle-Asset Protocol', price: 22.99, author: 'Coach Tyler Rhodes' },
  '3': { title: 'The Perimenopause Career Survival Guide', price: 24.99, author: 'Lisa Hartmann' },
  '4': { title: 'The Sandwich Generation Toolkit', price: 17.99, author: 'Maria Rodriguez' },
  '5': { title: 'The 30-Day Elder Care Crisis Manual', price: 29.99, author: 'Patricia Nolan' },
  '6': { title: 'The AI-Safe Family', price: 14.99, author: 'James Park' },
  '7': { title: 'The Value-First Budget', price: 12.99, author: 'Derek Osei' },
  '8': { title: 'The Microplastics Detox', price: 16.99, author: 'Dr. Ana Souza' },
}

function CheckoutForm() {
  const searchParams = useSearchParams()
  const listingId = searchParams.get('listing') || '1'
  const item = LISTING_DATA[listingId] || LISTING_DATA['1']

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function handleCheckout() {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch('/api/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ listingId }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || 'Checkout failed')
      if (data.url) window.location.href = data.url
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Something went wrong')
      setLoading(false)
    }
  }

  return (
    <div className="w-full max-w-md">
      <h1 className="font-[family-name:var(--font-heading)] text-2xl font-semibold text-[#1A1A1A] mb-6">Complete your purchase</h1>

      <div className="bg-white rounded-xl border border-[#E5E5E0] p-5 mb-6 flex gap-4 items-start">
        <div className="w-12 h-16 rounded-lg bg-gradient-to-br from-emerald-100 to-teal-200 flex items-center justify-center flex-shrink-0">
          <BookOpen className="w-6 h-6 text-[#2D6A4F]" />
        </div>
        <div className="flex-1 min-w-0">
          <p className="font-medium text-[#1A1A1A] text-sm line-clamp-2">{item.title}</p>
          <p className="text-xs text-[#8A8A8A] mt-0.5">by {item.author}</p>
          <p className="text-xs text-[#8A8A8A] mt-1">PDF · Instant download after payment</p>
        </div>
        <p className="font-[family-name:var(--font-mono)] font-bold text-[#2D6A4F]">{formatPriceDollars(item.price)}</p>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 text-sm rounded-lg px-4 py-3 mb-4">
          {error}
        </div>
      )}

      <button
        onClick={handleCheckout}
        disabled={loading}
        className="w-full bg-[#2D6A4F] hover:bg-[#245A42] disabled:opacity-60 disabled:cursor-not-allowed text-white font-semibold py-4 rounded-xl transition-colors flex items-center justify-center gap-2 text-lg"
      >
        {loading ? (
          <><Loader2 className="w-5 h-5 animate-spin" /> Redirecting to Stripe…</>
        ) : (
          <>Pay {formatPriceDollars(item.price)} — Instant Download</>
        )}
      </button>

      <p className="flex items-center justify-center gap-1.5 text-xs text-[#8A8A8A] mt-3">
        <Lock className="w-3 h-3" /> Secured by Stripe · 256-bit encryption · Instant PDF delivery
      </p>
      <p className="text-center text-xs text-[#8A8A8A] mt-4">
        <Link href={`/listings/${listingId}`} className="hover:text-[#2D6A4F] underline">← Back to listing</Link>
      </p>
    </div>
  )
}

export default function CheckoutPage() {
  return (
    <div className="min-h-screen bg-[#FAFAF8] flex flex-col">
      <header className="border-b border-[#E5E5E0] bg-white py-4">
        <div className="max-w-[1200px] mx-auto px-4 flex items-center justify-between">
          <Link href="/" className="font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1B4332] flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-[#2D6A4F]" /> WellRead
          </Link>
          <span className="flex items-center gap-1.5 text-sm text-[#8A8A8A]">
            <Lock className="w-4 h-4" /> Secure Checkout
          </span>
        </div>
      </header>
      <main className="flex-1 flex items-start justify-center py-12 px-4">
        <Suspense fallback={<div className="w-full max-w-md animate-pulse"><div className="h-8 bg-gray-100 rounded mb-4" /><div className="h-24 bg-gray-100 rounded mb-4" /><div className="h-14 bg-gray-100 rounded" /></div>}>
          <CheckoutForm />
        </Suspense>
      </main>
    </div>
  )
}
