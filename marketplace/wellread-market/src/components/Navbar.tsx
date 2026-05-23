import Link from 'next/link'
import { auth } from '@clerk/nextjs/server'
import { SignInButton, UserButton } from '@clerk/nextjs'
import { BookOpen, Search } from 'lucide-react'

export default async function Navbar() {
  const { userId } = await auth()

  return (
    <header className="sticky top-0 z-40 w-full border-b border-[#E5E5E0] bg-white/95 backdrop-blur">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-[family-name:var(--font-heading)] text-xl font-semibold text-[#1B4332]">
          <BookOpen className="w-6 h-6 text-[#2D6A4F]" />
          WellRead
        </Link>
        <nav className="hidden md:flex items-center gap-8">
          <Link href="/listings" className="text-sm text-[#4A4A4A] hover:text-[#2D6A4F] transition-colors">Browse</Link>
          <Link href="/listings?category=weight-loss" className="text-sm text-[#4A4A4A] hover:text-[#2D6A4F] transition-colors">GLP-1</Link>
          <Link href="/listings?category=perimenopause" className="text-sm text-[#4A4A4A] hover:text-[#2D6A4F] transition-colors">Perimenopause</Link>
          <Link href="/seller" className="text-sm text-[#4A4A4A] hover:text-[#2D6A4F] transition-colors">Sell</Link>
        </nav>
        <div className="flex items-center gap-3">
          <Link href="/listings" aria-label="Search" className="text-[#8A8A8A] hover:text-[#2D6A4F] transition-colors">
            <Search className="w-5 h-5" />
          </Link>
          {userId ? (
            <UserButton />
          ) : (
            <SignInButton mode="modal">
              <button className="text-sm font-medium px-4 py-2 bg-[#2D6A4F] hover:bg-[#245A42] text-white rounded-lg transition-colors">
                Sign in
              </button>
            </SignInButton>
          )}
        </div>
      </div>
    </header>
  )
}
