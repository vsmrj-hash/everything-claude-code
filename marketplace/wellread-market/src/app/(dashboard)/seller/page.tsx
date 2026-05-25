import { auth } from '@clerk/nextjs/server'
import { redirect } from 'next/navigation'
import Link from 'next/link'
import { BookOpen, DollarSign, ShoppingBag, Star, Plus } from 'lucide-react'

export default async function SellerPage() {
  const { userId } = await auth()
  if (!userId) redirect('/sign-in')

  const stats = [
    { label: 'Total Earnings', value: '$0.00', icon: <DollarSign className="w-5 h-5" /> },
    { label: 'Active Listings', value: '0', icon: <BookOpen className="w-5 h-5" /> },
    { label: 'Pending Orders', value: '0', icon: <ShoppingBag className="w-5 h-5" /> },
    { label: 'Avg. Rating', value: '—', icon: <Star className="w-5 h-5" /> },
  ]

  return (
    <div className="flex h-screen bg-[#FAFAF8] overflow-hidden">
      {/* Sidebar */}
      <aside className="w-56 shrink-0 bg-[#1B4332] text-white/80 py-8 px-4 hidden md:flex flex-col">
        <div className="font-[family-name:var(--font-heading)] text-lg font-semibold text-white mb-8 flex items-center gap-2">
          <BookOpen className="w-5 h-5" /> WellRead
        </div>
        {[
          ['Overview', '/seller', true],
          ['My Listings', '/seller/listings', false],
          ['Orders', '/seller/orders', false],
          ['Settings', '/seller/settings', false],
        ].map(([label, href, active]) => (
          <Link
            key={label as string}
            href={href as string}
            className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm mb-1 transition-colors ${active ? 'bg-white/10 text-white font-medium' : 'hover:bg-white/5'}`}
          >
            {label}
          </Link>
        ))}
        <div className="mt-auto">
          <Link href="/listings" className="flex items-center gap-2 text-sm text-white/50 hover:text-white/80 transition-colors">
            ← Back to store
          </Link>
        </div>
      </aside>

      {/* Main */}
      <div className="flex-1 overflow-y-auto">
        <div className="p-8">
          <div className="flex items-center justify-between mb-8">
            <h1 className="font-[family-name:var(--font-heading)] text-2xl font-semibold text-[#1A1A1A]">Seller Dashboard</h1>
            <Link
              href="/seller/listings/new"
              className="flex items-center gap-2 bg-[#2D6A4F] hover:bg-[#245A42] text-white px-5 py-2.5 rounded-lg text-sm font-medium transition-colors"
            >
              <Plus className="w-4 h-4" /> New Listing
            </Link>
          </div>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-10">
            {stats.map(stat => (
              <div key={stat.label} className="bg-white rounded-xl p-5 shadow-[0_1px_4px_rgba(0,0,0,0.06),0_1px_2px_rgba(0,0,0,0.04)]">
                <div className="flex items-center gap-2 text-[#8A8A8A] mb-3">{stat.icon}<span className="text-sm">{stat.label}</span></div>
                <p className="font-[family-name:var(--font-mono)] text-2xl font-bold text-[#2D6A4F]">{stat.value}</p>
              </div>
            ))}
          </div>

          <div className="bg-white rounded-xl shadow-[0_1px_4px_rgba(0,0,0,0.06),0_1px_2px_rgba(0,0,0,0.04)] p-6">
            <h2 className="font-[family-name:var(--font-heading)] text-lg font-semibold text-[#1A1A1A] mb-4">Your Listings</h2>
            <div className="text-center py-12 text-[#8A8A8A]">
              <BookOpen className="w-10 h-10 mx-auto mb-3 opacity-30" />
              <p className="text-sm">No listings yet.</p>
              <Link href="/seller/listings/new" className="text-[#2D6A4F] text-sm font-medium hover:underline mt-2 block">
                Create your first listing →
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
