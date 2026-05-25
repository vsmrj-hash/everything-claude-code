import { NextResponse } from 'next/server'

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url)
  const category = searchParams.get('category')
  const q = searchParams.get('q')

  // Placeholder — replace with db query after connecting DATABASE_URL
  const listings = [
    { id: '1', title: 'Life After Ozempic', authorName: 'Dr. Sarah Chen', price: '19.99', category: 'weight-loss', status: 'active' },
    { id: '2', title: 'The Perimenopause Career Survival Guide', authorName: 'Lisa Hartmann', price: '24.99', category: 'perimenopause', status: 'active' },
    { id: '3', title: 'The Sandwich Generation Toolkit', authorName: 'Maria Rodriguez', price: '17.99', category: 'caregiver-support', status: 'active' },
    { id: '4', title: 'The AI-Safe Family', authorName: 'James Park', price: '14.99', category: 'family-safety', status: 'active' },
    { id: '5', title: 'The Value-First Budget', authorName: 'Derek Osei', price: '12.99', category: 'budget-wellness', status: 'active' },
    { id: '6', title: 'The Microplastics Detox', authorName: 'Dr. Ana Souza', price: '16.99', category: 'clean-living', status: 'active' },
  ].filter(l => {
    if (category && l.category !== category) return false
    if (q && !l.title.toLowerCase().includes(q.toLowerCase())) return false
    return true
  })

  return NextResponse.json(listings)
}
