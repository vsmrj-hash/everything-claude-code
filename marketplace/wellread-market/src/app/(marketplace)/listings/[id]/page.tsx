import { notFound } from 'next/navigation'
import Link from 'next/link'
import { Star, FileText, Check, Lock, ChevronRight } from 'lucide-react'
import { formatPriceDollars } from '@/lib/utils'
import type { Metadata } from 'next'

const LISTINGS_MAP: Record<string, {
  id: string; title: string; authorName: string; price: string; category: string;
  coverUrl: null; description: string; pageCount: number; avgRating: number; reviewCount: number
}> = {
  '1': { id: '1', title: 'Life After Ozempic', authorName: 'Dr. Sarah Chen', price: '19.99', category: 'weight-loss', coverUrl: null, description: 'A comprehensive scientific guide based on clinical weight-maintenance frameworks. Features gradual tapering schedules, a protein- and fiber-rich dietary blueprint targeting 1.0–1.2 grams of protein per kilogram of body weight, and appetite-management tools to prevent the ghrelin rebound that causes rapid weight regain after stopping GLP-1 medications.\n\nIncludes:\n• 7-week tapering schedule\n• Daily protein tracking worksheets\n• 30 high-protein, high-fiber recipes\n• Appetite hormone regulation strategies\n• When to re-start: evidence-based criteria', pageCount: 52, avgRating: 4.8, reviewCount: 124 },
  '2': { id: '2', title: 'The Muscle-Asset Protocol', authorName: 'Coach Tyler Rhodes', price: '22.99', category: 'weight-loss', coverUrl: null, description: 'Short, repeatable strength-training routines for GLP-1 users that require no gym setup. Outlines home-based progressive resistance training and tracking frameworks to ensure rapid fat loss does not destroy metabolic health.', pageCount: 61, avgRating: 4.7, reviewCount: 67 },
  '3': { id: '3', title: 'The Perimenopause Career Survival Guide', authorName: 'Lisa Hartmann', price: '24.99', category: 'perimenopause', coverUrl: null, description: 'Managing brain fog, sleep disruption, and professional presence during the perimenopausal transition. Evidence-based strategies for cognitive clarity, sleep optimization, and workplace performance.', pageCount: 87, avgRating: 4.9, reviewCount: 89 },
  '4': { id: '4', title: 'The Sandwich Generation Toolkit', authorName: 'Maria Rodriguez', price: '17.99', category: 'caregiver-support', coverUrl: null, description: 'Systems and checklists for working women balancing career, children, and aging parents simultaneously. Practical frameworks for managing caregiver burnout and creating sustainable support systems.', pageCount: 64, avgRating: 4.7, reviewCount: 56 },
  '5': { id: '5', title: 'The 30-Day Elder Care Crisis Manual', authorName: 'Patricia Nolan', price: '29.99', category: 'caregiver-support', coverUrl: null, description: 'Fast-track assessment systems for urgent senior placement. Step-by-step decision guides for families navigating sudden care transitions, memory care, and assisted living evaluations.', pageCount: 93, avgRating: 4.8, reviewCount: 41 },
  '6': { id: '6', title: 'The AI-Safe Family', authorName: 'James Park', price: '14.99', category: 'family-safety', coverUrl: null, description: 'How to create a family cyber-defense protocol against voice cloning scams, deepfakes, and AI-powered fraud. Practical playbooks for parents and caregivers.', pageCount: 43, avgRating: 4.6, reviewCount: 34 },
  '7': { id: '7', title: 'The Value-First Budget', authorName: 'Derek Osei', price: '12.99', category: 'budget-wellness', coverUrl: null, description: 'Optimize household spending and build financial resilience against inflation. Evidence-based frameworks for spending that maximizes wellbeing per dollar.', pageCount: 78, avgRating: 4.5, reviewCount: 112 },
  '8': { id: '8', title: 'The Microplastics Detox', authorName: 'Dr. Ana Souza', price: '16.99', category: 'clean-living', coverUrl: null, description: 'A scientific blueprint for reducing synthetic toxins in your food and home. Evidence-based guidance on filtration, cookware, and sourcing for cleaner everyday living.', pageCount: 55, avgRating: 4.7, reviewCount: 78 },
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params
  const listing = LISTINGS_MAP[id]
  if (!listing) return { title: 'Not Found' }
  return { title: listing.title, description: listing.description.slice(0, 160) }
}

export default async function ListingDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const listing = LISTINGS_MAP[id]
  if (!listing) notFound()

  return (
    <div className="bg-[#FAFAF8] min-h-screen py-12">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-1.5 text-xs text-[#8A8A8A] mb-8">
          <Link href="/" className="hover:text-[#2D6A4F] transition-colors">Home</Link>
          <ChevronRight className="w-3 h-3" />
          <Link href="/listings" className="hover:text-[#2D6A4F] transition-colors">Browse</Link>
          <ChevronRight className="w-3 h-3" />
          <span className="text-[#1A1A1A]">{listing.title}</span>
        </nav>

        <div className="grid grid-cols-1 lg:grid-cols-[2fr_3fr] gap-12">
          {/* Cover */}
          <div>
            <div className="w-full max-w-xs mx-auto rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.10)] overflow-hidden aspect-[2/3] bg-gradient-to-br from-emerald-100 to-teal-200 flex flex-col items-center justify-center p-8">
              <span className="font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1B4332] text-center">{listing.title}</span>
              <span className="text-sm text-[#4A4A4A] mt-2">by {listing.authorName}</span>
            </div>
            <div className="flex items-center justify-center gap-4 mt-4">
              <span className="flex items-center gap-1.5 text-sm text-[#8A8A8A]">
                <FileText className="w-4 h-4" /> PDF · {listing.pageCount} pages
              </span>
            </div>
          </div>

          {/* Info */}
          <div>
            <h1 className="font-[family-name:var(--font-heading)] text-4xl font-semibold text-[#1A1A1A] mb-2">{listing.title}</h1>
            <p className="text-[#4A4A4A] text-lg mb-4">by {listing.authorName}</p>
            <div className="flex items-center gap-2 mb-4">
              {[1,2,3,4,5].map(n => (
                <Star key={n} className={`w-5 h-5 ${n <= Math.round(listing.avgRating) ? 'fill-[#F59E0B] text-[#F59E0B]' : 'text-[#E5E5E0]'}`} />
              ))}
              <span className="text-sm text-[#8A8A8A]">({listing.reviewCount} reviews)</span>
            </div>
            <div className="border-t border-[#E5E5E0] my-5" />
            <p className="font-[family-name:var(--font-mono)] text-4xl font-bold text-[#2D6A4F] mb-6">{formatPriceDollars(parseFloat(listing.price))}</p>
            <div className="prose prose-sm text-[#4A4A4A] max-w-none mb-6 whitespace-pre-line">{listing.description}</div>
            <ul className="space-y-2 mb-8">
              {['Instant PDF download', 'Readable on any device', '30-day money-back guarantee', 'Secure payment via Stripe'].map(feature => (
                <li key={feature} className="flex items-center gap-2 text-sm text-[#1A1A1A]">
                  <Check className="w-4 h-4 text-green-600 flex-shrink-0" /> {feature}
                </li>
              ))}
            </ul>
            <Link
              href={`/checkout?listing=${listing.id}`}
              className="w-full block text-center bg-[#2D6A4F] hover:bg-[#245A42] text-white font-semibold py-4 rounded-xl text-lg transition-colors"
            >
              Buy for {formatPriceDollars(parseFloat(listing.price))}
            </Link>
            <p className="flex items-center justify-center gap-1.5 text-xs text-[#8A8A8A] mt-3">
              <Lock className="w-3 h-3" /> Secure checkout · Instant download
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
