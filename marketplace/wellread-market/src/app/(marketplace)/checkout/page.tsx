import Link from 'next/link'
import { Lock, BookOpen } from 'lucide-react'
import { formatPriceDollars } from '@/lib/utils'

const LISTING_PRICES: Record<string, { title: string; price: number; author: string }> = {
  '1': { title: 'Life After Ozempic', price: 19.99, author: 'Dr. Sarah Chen' },
  '2': { title: 'The Muscle-Asset Protocol', price: 22.99, author: 'Coach Tyler Rhodes' },
  '3': { title: 'The Perimenopause Career Survival Guide', price: 24.99, author: 'Lisa Hartmann' },
  '4': { title: 'The Sandwich Generation Toolkit', price: 17.99, author: 'Maria Rodriguez' },
  '5': { title: 'The 30-Day Elder Care Crisis Manual', price: 29.99, author: 'Patricia Nolan' },
  '6': { title: 'The AI-Safe Family', price: 14.99, author: 'James Park' },
  '7': { title: 'The Value-First Budget', price: 12.99, author: 'Derek Osei' },
  '8': { title: 'The Microplastics Detox', price: 16.99, author: 'Dr. Ana Souza' },
}

export default async function CheckoutPage({ searchParams }: { searchParams: Promise<{ listing?: string }> | { listing?: string } }) {
  const params = searchParams as { listing?: string }
  const listingId = params.listing || '1'
  const item = LISTING_PRICES[listingId] || LISTING_PRICES['1']

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
        <div className="w-full max-w-md">
          <h1 className="font-[family-name:var(--font-heading)] text-2xl font-semibold text-[#1A1A1A] mb-6">Complete your purchase</h1>
          <div className="bg-white rounded-xl border border-[#E5E5E0] p-5 mb-6 flex gap-4 items-start">
            <div className="w-12 h-16 rounded-lg bg-gradient-to-br from-emerald-100 to-teal-200 flex items-center justify-center flex-shrink-0">
              <BookOpen className="w-6 h-6 text-[#2D6A4F]" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="font-medium text-[#1A1A1A] text-sm line-clamp-2">{item.title}</p>
              <p className="text-xs text-[#8A8A8A] mt-0.5">by {item.author}</p>
            </div>
            <p className="font-[family-name:var(--font-mono)] font-bold text-[#2D6A4F]">{formatPriceDollars(item.price)}</p>
          </div>
          <div className="bg-white rounded-xl border border-[#E5E5E0] p-6">
            <p className="text-sm text-[#8A8A8A] mb-4">Payment is processed securely by Stripe. Add your Stripe keys in Vercel environment variables to enable live checkout.</p>
            <div className="space-y-3">
              <input type="email" placeholder="Email address" className="w-full border border-[#E5E5E0] rounded-lg px-3 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2D6A4F]/30 focus:border-[#2D6A4F]" />
              <input type="text" placeholder="Name on card" className="w-full border border-[#E5E5E0] rounded-lg px-3 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2D6A4F]/30 focus:border-[#2D6A4F]" />
              <div className="border border-[#E5E5E0] rounded-lg px-3 py-3 bg-[#F5F5F0] text-sm text-[#8A8A8A]">
                Card details (Stripe Elements loads here after keys are configured)
              </div>
            </div>
            <button className="w-full mt-4 bg-[#2D6A4F] hover:bg-[#245A42] text-white font-semibold py-4 rounded-xl transition-colors">
              Pay {formatPriceDollars(item.price)}
            </button>
            <p className="flex items-center justify-center gap-1.5 text-xs text-[#8A8A8A] mt-3">
              <Lock className="w-3 h-3" /> Secured by Stripe · 256-bit encryption
            </p>
          </div>
        </div>
      </main>
    </div>
  )
}
