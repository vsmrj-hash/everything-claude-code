import { SignIn } from '@clerk/nextjs'
import { BookOpen } from 'lucide-react'
import Link from 'next/link'

export default function SignInPage() {
  return (
    <div className="min-h-screen bg-[#FAFAF8] flex flex-col items-center justify-center py-12 px-4">
      <Link href="/" className="font-[family-name:var(--font-heading)] text-2xl font-semibold text-[#1B4332] flex items-center gap-2 mb-2">
        <BookOpen className="w-6 h-6 text-[#2D6A4F]" /> WellRead
      </Link>
      <p className="text-[#8A8A8A] text-sm mb-8">Science-backed guidance for your body, your life.</p>
      <SignIn />
    </div>
  )
}
