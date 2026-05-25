import Link from 'next/link'
import { ArrowRight, BookOpen } from 'lucide-react'

export default function Hero() {
  return (
    <section className="bg-[#FAFAF8] py-20 lg:py-28">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#95D5B2] text-[#1B4332] text-xs font-medium tracking-wide uppercase mb-5">
              New releases this week
            </span>
            <h1 className="font-[family-name:var(--font-heading)] text-5xl lg:text-6xl font-bold text-[#1A1A1A] leading-tight mb-5">
              Feel better.<br />Read smarter.
            </h1>
            <p className="text-xl text-[#4A4A4A] leading-relaxed mb-8 max-w-lg">
              Evidence-based ebooks on GLP-1 transitions, perimenopause, caregiver burnout, and more — written by experts, delivered instantly.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <Link
                href="/listings"
                className="inline-flex items-center gap-2 bg-[#2D6A4F] hover:bg-[#245A42] text-white font-medium px-8 py-4 rounded-lg transition-colors duration-150"
              >
                Browse ebooks <ArrowRight className="w-4 h-4" />
              </Link>
              <Link href="/seller" className="text-[#2D6A4F] underline underline-offset-2 text-sm font-medium">
                Start selling →
              </Link>
            </div>
            <div className="flex items-center gap-6 mt-10 text-sm text-[#8A8A8A]">
              <span className="flex items-center gap-1.5"><BookOpen className="w-4 h-4 text-[#2D6A4F]" /> 200+ ebooks</span>
              <span>⭐ 4.8 avg rating</span>
              <span>⚡ Instant download</span>
            </div>
          </div>
          <div className="hidden lg:flex items-center justify-center gap-4 relative">
            {[
              { color: 'bg-emerald-100', rotate: '-rotate-6', title: 'Life After Ozempic' },
              { color: 'bg-teal-50', rotate: 'rotate-2', title: 'Perimenopause Guide' },
              { color: 'bg-green-100', rotate: 'rotate-8', title: 'Sandwich Generation' },
            ].map((book) => (
              <div key={book.title} className={`${book.rotate} ${book.color} w-32 h-48 rounded-lg shadow-[0_4px_20px_rgba(0,0,0,0.10)] flex items-end p-3 transition-transform hover:scale-105`}>
                <span className="font-[family-name:var(--font-heading)] text-xs font-semibold text-[#1B4332] leading-tight">{book.title}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
