import Link from 'next/link'
import Image from 'next/image'
import { Star, BookOpen } from 'lucide-react'
import { cn, formatPriceDollars } from '@/lib/utils'
import type { Listing } from '@/types'

interface ListingCardProps {
  listing: Listing & { avgRating?: number; reviewCount?: number }
  onPreview?: () => void
}

export default function ListingCard({ listing, onPreview }: ListingCardProps) {
  const price = parseFloat(listing.price)
  return (
    <div className="group flex flex-col bg-white rounded-xl shadow-[0_1px_4px_rgba(0,0,0,0.06),0_1px_2px_rgba(0,0,0,0.04)] hover:shadow-[0_4px_20px_rgba(0,0,0,0.10)] transition-shadow duration-200 overflow-hidden">
      <div className="relative aspect-[2/3] w-full overflow-hidden bg-[#F5F5F0]">
        {listing.coverUrl ? (
          <Image
            src={listing.coverUrl}
            alt={listing.title}
            fill
            className="object-cover group-hover:scale-[1.01] transition-transform duration-200"
            sizes="(max-width: 768px) 50vw, 25vw"
          />
        ) : (
          <div className="w-full h-full flex flex-col items-center justify-center bg-gradient-to-br from-emerald-50 to-teal-100 p-4">
            <BookOpen className="w-10 h-10 text-[#2D6A4F] mb-3 opacity-60" />
            <span className="font-[family-name:var(--font-heading)] text-sm font-semibold text-[#1B4332] text-center line-clamp-3">{listing.title}</span>
          </div>
        )}
        <span className="absolute top-2 left-2 px-2 py-0.5 rounded-full bg-[#95D5B2]/90 text-[#1B4332] text-xs font-medium capitalize">
          {listing.category.replace(/-/g, ' ')}
        </span>
      </div>
      <div className="flex flex-col flex-1 p-4">
        <h3 className="font-[family-name:var(--font-heading)] text-base font-semibold text-[#1A1A1A] line-clamp-2 mb-1">
          {listing.title}
        </h3>
        <p className="text-sm text-[#8A8A8A] mb-2">by {listing.authorName}</p>
        {listing.avgRating !== undefined && (
          <div className="flex items-center gap-1 mb-3">
            {[1,2,3,4,5].map(n => (
              <Star key={n} className={cn("w-3 h-3", n <= Math.round(listing.avgRating!) ? "fill-[#F59E0B] text-[#F59E0B]" : "text-[#E5E5E0]")} />
            ))}
            <span className="text-xs text-[#8A8A8A] ml-1">({listing.reviewCount})</span>
          </div>
        )}
        <div className="mt-auto">
          <p className="font-[family-name:var(--font-mono)] text-lg font-bold text-[#2D6A4F] mb-3">{formatPriceDollars(price)}</p>
          <div className="flex gap-2">
            {listing.previewUrl && (
              <button
                onClick={onPreview}
                className="flex-1 border border-[#E5E5E0] text-[#8A8A8A] hover:border-[#2D6A4F] hover:text-[#2D6A4F] text-sm py-2 rounded-md transition-colors"
              >
                Preview
              </button>
            )}
            <Link
              href={`/listings/${listing.id}`}
              className="flex-1 bg-[#2D6A4F] hover:bg-[#245A42] text-white text-sm py-2 rounded-md transition-colors text-center font-medium"
            >
              Buy now
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
