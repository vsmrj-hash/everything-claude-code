import Hero from '@/components/Hero'
import ListingCard from '@/components/ListingCard'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { BookOpen, Download, Star, Lock } from 'lucide-react'

// Static seed data for first deployment
const FEATURED_LISTINGS = [
  { id: '1', title: 'Life After Ozempic', authorName: 'Dr. Sarah Chen', price: '19.99', category: 'weight-loss', coverUrl: null, status: 'active' as const, featured: true, description: '', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 52, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.8, reviewCount: 124 },
  { id: '2', title: 'The Perimenopause Career Survival Guide', authorName: 'Lisa Hartmann', price: '24.99', category: 'perimenopause', coverUrl: null, status: 'active' as const, featured: true, description: '', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 87, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.9, reviewCount: 89 },
  { id: '3', title: 'The Sandwich Generation Toolkit', authorName: 'Maria Rodriguez', price: '17.99', category: 'caregiver-support', coverUrl: null, status: 'active' as const, featured: true, description: '', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 64, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.7, reviewCount: 56 },
  { id: '4', title: 'The AI-Safe Family', authorName: 'James Park', price: '14.99', category: 'family-safety', coverUrl: null, status: 'active' as const, featured: false, description: '', sellerId: '', fileUrl: null, previewUrl: null, pageCount: 43, createdAt: new Date(), updatedAt: new Date(), avgRating: 4.6, reviewCount: 34 },
]

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#FAFAF8]">
      <Navbar />
      <main id="main-content" className="flex-1">
        <Hero />

        {/* Featured ebooks */}
        <section className="py-16 lg:py-20 bg-[#FAFAF8]">
          <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-end justify-between mb-8">
              <div>
                <h2 className="font-[family-name:var(--font-heading)] text-3xl font-semibold text-[#1A1A1A]">Editor&apos;s Picks</h2>
                <p className="text-[#8A8A8A] mt-1">Curated guides solving today&apos;s most urgent health challenges</p>
              </div>
              <a href="/listings" className="text-sm text-[#2D6A4F] font-medium hover:underline hidden sm:block">View all →</a>
            </div>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
              {FEATURED_LISTINGS.map(listing => (
                <ListingCard key={listing.id} listing={listing} />
              ))}
            </div>
          </div>
        </section>

        {/* How it works */}
        <section className="py-16 bg-[#F5F5F0]">
          <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 className="font-[family-name:var(--font-heading)] text-3xl font-semibold text-[#1A1A1A] mb-12">How WellRead Works</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {[
                { icon: <BookOpen className="w-7 h-7" />, title: 'Browse by topic', desc: 'Filter by health concern, price, or rating. Every ebook is reviewed by our editorial team.' },
                { icon: <Star className="w-7 h-7" />, title: 'Preview free', desc: 'Read the first chapter of any ebook before buying. No surprises.' },
                { icon: <Download className="w-7 h-7" />, title: 'Buy & download', desc: 'Secure Stripe checkout. Your PDF downloads instantly — no waiting, no account required.' },
              ].map((step, i) => (
                <div key={i} className="flex flex-col items-center p-6">
                  <div className="w-14 h-14 rounded-2xl bg-[#95D5B2]/30 flex items-center justify-center text-[#2D6A4F] mb-4">
                    {step.icon}
                  </div>
                  <h3 className="font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1A1A1A] mb-2">{step.title}</h3>
                  <p className="text-[#8A8A8A] text-sm leading-relaxed">{step.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Trust bar */}
        <section className="py-8 bg-white border-t border-[#E5E5E0]">
          <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap items-center justify-center gap-8 text-sm text-[#8A8A8A]">
            <span className="flex items-center gap-2"><Lock className="w-4 h-4 text-[#2D6A4F]" /> Secured by Stripe</span>
            <span className="flex items-center gap-2"><Download className="w-4 h-4 text-[#2D6A4F]" /> Instant PDF delivery</span>
            <span className="flex items-center gap-2"><Star className="w-4 h-4 text-[#F59E0B] fill-[#F59E0B]" /> 4.8 average rating</span>
            <span className="flex items-center gap-2"><BookOpen className="w-4 h-4 text-[#2D6A4F]" /> 200+ ebooks</span>
          </div>
        </section>
      </main>
      <Footer />
    </div>
  )
}
