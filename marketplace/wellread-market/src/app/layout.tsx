import type { Metadata } from 'next'
import { ClerkProvider } from '@clerk/nextjs'
import './globals.css'

export const metadata: Metadata = {
  title: { default: 'WellRead — Health & Wellness Ebooks', template: '%s | WellRead' },
  description: 'Science-backed guidance for your body, your life. Ebooks on GLP-1 transitions, perimenopause, caregiver support, and more.',
  metadataBase: new URL(process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:3000'),
  openGraph: {
    siteName: 'WellRead',
    type: 'website',
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <html lang="en" suppressHydrationWarning>
        <body>
          <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 z-50 bg-primary text-white px-4 py-2 rounded-md">
            Skip to content
          </a>
          {children}
        </body>
      </html>
    </ClerkProvider>
  )
}
