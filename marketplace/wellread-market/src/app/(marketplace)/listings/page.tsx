import ListingCard from '@/components/ListingCard'
import { BookOpen } from 'lucide-react'
import Link from 'next/link'
import { CATEGORIES } from '@/types'

const ALL_LISTINGS = [
  { id: '1', title: 'Life After Ozempic', authorName: 'Dr. Sarah Chen', price: '19.99', category: 'weight-loss', coverUrl: null, status: 'active' as const, featured: true, description: 'A scientific guide to post-GLP-1 endocrine reset and hormone-stabilizing nutrition.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 52, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.8, reviewCount: 124 },
  { id: '2', title: 'The Muscle-Asset Protocol', authorName: 'Coach Tyler Rhodes', price: '22.99', category: 'weight-loss', coverUrl: null, status: 'active' as const, featured: false, description: 'Resistance training and metabolic preservation for GLP-1 users.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 61, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.7, reviewCount: 67 },
  { id: '3', title: 'The Perimenopause Career Survival Guide', authorName: 'Lisa Hartmann', price: '24.99', category: 'perimenopause', coverUrl: null, status: 'active' as const, featured: true, description: 'Managing brain fog, sleep disruption, and professional presence.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 87, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.9, reviewCount: 89 },
  { id: '4', title: 'The Sandwich Generation Toolkit', authorName: 'Maria Rodriguez', price: '17.99', category: 'caregiver-support', coverUrl: null, status: 'active' as const, featured: true, description: 'Systems and checklists for working women balancing career and elder care.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 64, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.7, reviewCount: 56 },
  { id: '5', title: 'The 30-Day Elder Care Crisis Manual', authorName: 'Patricia Nolan', price: '29.99', category: 'caregiver-support', coverUrl: null, status: 'active' as const, featured: false, description: 'Fast-track assessment systems for urgent senior placement.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 93, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.8, reviewCount: 41 },
  { id: '6', title: 'The AI-Safe Family', authorName: 'James Park', price: '14.99', category: 'family-safety', coverUrl: null, status: 'active' as const, featured: false, description: 'How to create a family cyber-defense protocol against voice cloning scams.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 43, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.6, reviewCount: 34 },
  { id: '7', title: 'The Value-First Budget', authorName: 'Derek Osei', price: '12.99', category: 'budget-wellness', coverUrl: null, status: 'active' as const, featured: false, description: 'Optimize household spending and build financial resilience against inflation.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 78, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.5, reviewCount: 112 },
  { id: '8', title: 'The Microplastics Detox', authorName: 'Dr. Ana Souza', price: '16.99', category: 'clean-living', coverUrl: null, status: 'active' as const, featured: false, description: 'A scientific blueprint for reducing synthetic toxins in your food and home.', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 55, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.7, reviewCount: 78 },
]

export default function ListingsPage({ searchParams }: { searchParams: Promise<{ category?: string; q?: string }> | { category?: string; q?: string } }) {
  // Handle both promise and direct searchParams (Next.js 15 vs 14)
  const params = searchParams as { category?: string; q?: string }
  const category = params.category
  const query = params.q?.toLowerCase()

  let filtered = ALL_LISTINGS
  if (category) filtered = filtered.filter(l => l.category === category)
  if (query) filtered = filtered.filter(l => l.title.toLowerCase().includes(query) || l.description.toLowerCase().includes(query))

  const activeCategory = CATEGORIES.find(c => c.slug === category)

  return (
    <div className="bg-[#FAFAF8] min-h-screen">
      {/* Category strip */}
      <div className="border-b border-[#E5E5E0] bg-white sticky top-16 z-30">
        <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex gap-2 overflow-x-auto py-3" style={{ scrollbarWidth: 'none' }}>
            <Link
              href="/listings"
              className={`whitespace-nowrap px-4 py-1.5 rounded-full text-sm transition-colors ${!category ? 'bg-[#2D6A4F] text-white font-medium' : 'border border-[#E5E5E0] text-[#8A8A8A] hover:border-[#2D6A4F] hover:text-[#2D6A4F]'}`}
            >
              All
            </Link>
            {CATEGORIES.map(cat => (
              <Link
                key={cat.slug}
                href={`/listings?category=${cat.slug}`}
                className={`whitespace-nowrap px-4 py-1.5 rounded-full text-sm transition-colors ${category === cat.slug ? 'bg-[#2D6A4F] text-white font-medium' : 'border border-[#E5E5E0] text-[#8A8A8A] hover:border-[#2D6A4F] hover:text-[#2D6A4F]'}`}
              >
                {cat.label}
              </Link>
            ))}
          </div>
        </div>
      </div>

      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            {activeCategory && (
              <h1 className="font-[family-name:var(--font-heading)] text-2xl font-semibold text-[#1A1A1A] mb-1">{activeCategory.label}</h1>
            )}
            <p className="text-sm text-[#8A8A8A]">{filtered.length} ebook{filtered.length !== 1 ? 's' : ''}</p>
          </div>
        </div>
        {filtered.length === 0 ? (
          <div className="text-center py-20">
            <BookOpen className="w-12 h-12 text-[#E5E5E0] mx-auto mb-4" />
            <h3 className="font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1A1A1A] mb-2">No ebooks found</h3>
            <p className="text-[#8A8A8A]">Try a different category or search term.</p>
          </div>
        ) : (
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 md:gap-6">
            {filtered.map(listing => <ListingCard key={listing.id} listing={listing} />)}
          </div>
        )}
      </div>
    </div>
  )
}
