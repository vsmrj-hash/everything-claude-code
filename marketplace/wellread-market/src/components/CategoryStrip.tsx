'use client'
import { cn } from '@/lib/utils'
import { CATEGORIES } from '@/types'

interface CategoryStripProps {
  activeSlug?: string
  onChange?: (slug: string) => void
}

export default function CategoryStrip({ activeSlug, onChange }: CategoryStripProps) {
  return (
    <div className="border-b border-[#E5E5E0] bg-white sticky top-16 z-30">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex gap-2 overflow-x-auto py-3" style={{ scrollbarWidth: 'none' }}>
          <button
            onClick={() => onChange?.('')}
            className={cn(
              "whitespace-nowrap px-4 py-1.5 rounded-full text-sm transition-colors",
              !activeSlug
                ? "bg-[#2D6A4F] text-white font-medium"
                : "border border-[#E5E5E0] text-[#8A8A8A] hover:border-[#2D6A4F] hover:text-[#2D6A4F]"
            )}
          >
            All
          </button>
          {CATEGORIES.map(cat => (
            <button
              key={cat.slug}
              onClick={() => onChange?.(cat.slug)}
              className={cn(
                "whitespace-nowrap px-4 py-1.5 rounded-full text-sm transition-colors",
                activeSlug === cat.slug
                  ? "bg-[#2D6A4F] text-white font-medium"
                  : "border border-[#E5E5E0] text-[#8A8A8A] hover:border-[#2D6A4F] hover:text-[#2D6A4F]"
              )}
            >
              {cat.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
