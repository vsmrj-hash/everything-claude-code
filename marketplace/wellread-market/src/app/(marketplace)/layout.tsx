import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'

export default function MarketplaceLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex flex-col min-h-screen bg-[#FAFAF8]">
      <Navbar />
      <main id="main-content" className="flex-1">
        {children}
      </main>
      <Footer />
    </div>
  )
}
