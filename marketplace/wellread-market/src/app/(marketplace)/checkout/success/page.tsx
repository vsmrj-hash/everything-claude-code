import Link from 'next/link'
import { CheckCircle, Download, BookOpen } from 'lucide-react'

export default function CheckoutSuccessPage() {
  return (
    <div className="min-h-screen bg-[#FAFAF8] flex flex-col">
      <header className="border-b border-[#E5E5E0] bg-white py-4">
        <div className="max-w-[1200px] mx-auto px-4">
          <Link href="/" className="font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1B4332] flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-[#2D6A4F]" /> WellRead
          </Link>
        </div>
      </header>
      <main className="flex-1 flex items-center justify-center py-20 px-4">
        <div className="max-w-md w-full text-center">
          <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6">
            <CheckCircle className="w-8 h-8 text-green-600" />
          </div>
          <h1 className="font-[family-name:var(--font-heading)] text-3xl font-semibold text-[#1A1A1A] mb-2">Your ebook is ready!</h1>
          <p className="text-[#8A8A8A] mb-8">Payment confirmed. Your download link is ready below and has been emailed to you.</p>
          <div className="bg-white border border-[#E5E5E0] rounded-xl p-6 text-left mb-4">
            <div className="flex gap-4 items-start mb-4">
              <div className="w-10 h-14 rounded-lg bg-gradient-to-br from-emerald-100 to-teal-200 flex items-center justify-center flex-shrink-0">
                <BookOpen className="w-5 h-5 text-[#2D6A4F]" />
              </div>
              <div>
                <p className="font-medium text-[#1A1A1A] text-sm">Your purchased ebook</p>
                <p className="text-xs text-[#8A8A8A]">PDF · Instant download</p>
              </div>
            </div>
            <button className="w-full bg-[#2D6A4F] hover:bg-[#245A42] text-white font-semibold py-3 rounded-lg transition-colors flex items-center justify-center gap-2">
              <Download className="w-4 h-4" /> Download PDF
            </button>
            <p className="text-xs text-[#8A8A8A] mt-2 text-center">Link expires in 24 hours</p>
          </div>
          <Link href="/listings" className="text-[#2D6A4F] text-sm font-medium hover:underline">
            Browse more ebooks →
          </Link>
        </div>
      </main>
    </div>
  )
}
