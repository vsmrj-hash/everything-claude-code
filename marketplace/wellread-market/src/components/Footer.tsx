import Link from 'next/link'
import { BookOpen } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="bg-[#1B4332] text-white/80 py-12 mt-auto">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div>
            <div className="flex items-center gap-2 font-[family-name:var(--font-heading)] text-xl font-semibold text-white mb-3">
              <BookOpen className="w-5 h-5" /> WellRead
            </div>
            <p className="text-sm text-white/60">Science-backed guidance for your body, your life.</p>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-white mb-3">Shop</h4>
            <ul className="space-y-2 text-sm">
              {[['Browse All', '/listings'], ['GLP-1 & Weight Loss', '/listings?category=weight-loss'], ['Perimenopause', '/listings?category=perimenopause'], ['Caregiver Support', '/listings?category=caregiver-support']].map(([label, href]) => (
                <li key={href}><Link href={href} className="hover:text-white transition-colors">{label}</Link></li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-white mb-3">Sell</h4>
            <ul className="space-y-2 text-sm">
              {[['Become a Seller', '/seller'], ['Dashboard', '/seller'], ['Pricing', '/seller#pricing']].map(([label, href]) => (
                <li key={label}><Link href={href} className="hover:text-white transition-colors">{label}</Link></li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-white mb-3">Company</h4>
            <ul className="space-y-2 text-sm">
              {[['About', '/about'], ['Privacy', '/privacy'], ['Terms', '/terms']].map(([label, href]) => (
                <li key={href}><Link href={href} className="hover:text-white transition-colors">{label}</Link></li>
              ))}
            </ul>
          </div>
        </div>
        <div className="border-t border-white/10 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-white/40">
          <p>© {new Date().getFullYear()} WellRead. All rights reserved.</p>
          <p>Secure payments by Stripe · Instant PDF delivery</p>
        </div>
      </div>
    </footer>
  )
}
