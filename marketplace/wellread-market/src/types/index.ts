export interface Listing {
  id: string
  sellerId: string
  title: string
  description: string
  price: string
  category: string
  coverUrl: string | null
  fileUrl: string | null
  previewUrl: string | null
  pageCount: number | null
  authorName: string
  status: 'draft' | 'active' | 'archived'
  featured: boolean
  createdAt: Date
  updatedAt: Date
}

export interface Order {
  id: string
  buyerId: string
  listingId: string
  stripeSessionId: string | null
  amount: string
  status: 'pending' | 'paid' | 'fulfilled' | 'refunded'
  downloadUrl: string | null
  downloadExpiresAt: Date | null
  createdAt: Date
}

export interface Review {
  id: string
  listingId: string
  reviewerId: string
  reviewerName: string
  rating: number
  comment: string | null
  createdAt: Date
}

export const CATEGORIES = [
  { label: 'Weight Loss & GLP-1', slug: 'weight-loss' },
  { label: 'Perimenopause', slug: 'perimenopause' },
  { label: 'Caregiver Support', slug: 'caregiver-support' },
  { label: 'Family Safety', slug: 'family-safety' },
  { label: 'Budget Wellness', slug: 'budget-wellness' },
  { label: 'Detox & Clean Living', slug: 'clean-living' },
  { label: 'Parenting', slug: 'parenting' },
  { label: 'Mental Wellness', slug: 'mental-wellness' },
]
