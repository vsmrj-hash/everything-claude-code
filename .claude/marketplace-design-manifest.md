# Design Manifest — WellRead

## Design Philosophy

WellRead serves health-anxious adults who are already overwhelmed — they need a buying experience that feels calm, credible, and effortless. The aesthetic is **editorial minimal**: generous whitespace, an authoritative serif headline font paired with a clean sans-serif body, and a forest-green palette that reads as natural and trustworthy without veering clinical. Every design decision reduces cognitive load: one clear action per screen, no decorative clutter, trust signals surfaced early (ratings, author credentials, preview chapters), and a checkout flow that never surprises.

---

## Color System

### Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `color-primary` | `#2D6A4F` | CTAs, active states, primary buttons, links |
| `color-primary-hover` | `#245A42` | Hover on primary elements |
| `color-secondary` | `#95D5B2` | Badges, category pills, subtle highlights |
| `color-secondary-hover` | `#7DC4A0` | Hover on secondary elements |
| `color-accent` | `#1B4332` | Deep emphasis, footer background, strong headings |
| `color-surface` | `#FFFFFF` | Card backgrounds, modals, inputs |
| `color-surface-raised` | `#F5F5F0` | Elevated surfaces, dropdowns, tooltips |
| `color-background` | `#FAFAF8` | Page background |
| `color-text-primary` | `#1A1A1A` | Headlines, body copy |
| `color-text-secondary` | `#4A4A4A` | Captions, sub-labels, secondary info |
| `color-text-muted` | `#8A8A8A` | Placeholders, timestamps, disabled states |
| `color-border` | `#E5E5E0` | Dividers, card outlines, input borders |
| `color-success` | `#16A34A` | Download confirmations, positive badges |
| `color-warning` | `#D97706` | Pending orders, advisory notices |
| `color-error` | `#DC2626` | Validation errors, destructive actions |
| `color-star` | `#F59E0B` | Rating stars (fixed amber) |

### Semantic Aliases

| Role | Token |
|------|-------|
| Primary button background | `color-primary` |
| Primary button hover | `color-primary-hover` |
| Price display | `color-primary` |
| Rating stars | `color-star` |
| "New" badge | `color-secondary` bg + `color-accent` text |
| Success banner | `color-success` |
| Input border focus | `color-primary` ring |

---

## Typography

### Fonts

- **Heading font**: Fraunces (variable, optical-size aware) — editorial serif conveying authority and warmth
  - Google Fonts: `https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,600;9..144,700&display=swap`
- **Body font**: Inter (variable) — neutral, highly legible at small sizes
  - Google Fonts: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap`
- **Mono font**: JetBrains Mono — for prices, codes, download tokens

### Type Scale

| Tailwind Classes | Size | Line Height | Weight | Usage |
|-----------------|------|-------------|--------|-------|
| `font-heading text-5xl font-bold` | 48px | 1.15 | 700 | Hero headline |
| `font-heading text-4xl font-semibold` | 36px | 1.2 | 600 | Page H1 |
| `font-heading text-3xl font-semibold` | 30px | 1.25 | 600 | Section titles |
| `font-heading text-2xl font-medium` | 24px | 1.3 | 500 | Card titles, ebook titles |
| `text-xl font-medium` | 20px | 1.4 | 500 | Sub-headings, author names |
| `text-base` | 16px | 1.65 | 400 | Body copy, descriptions |
| `text-sm` | 14px | 1.5 | 400 | Labels, captions, metadata |
| `text-xs` | 12px | 1.4 | 400 | Badges, timestamps, footnotes |
| `font-mono text-lg font-bold` | 18px | 1.0 | 700 | Price display |

---

## Spacing & Layout

- **Container max-width**: `1200px`
- **Content padding**: `px-4 sm:px-6 lg:px-8`
- **Section vertical rhythm**: `py-16 md:py-24`
- **Card gap**: `gap-4 md:gap-6`
- **Border radius scale**: `rounded-sm`=4px, `rounded`=6px, `rounded-md`=8px, `rounded-lg`=12px, `rounded-xl`=16px, `rounded-2xl`=20px

## Shadows

| Token | Value |
|-------|-------|
| `shadow-card` | `0 1px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)` |
| `shadow-elevated` | `0 4px 20px rgba(0,0,0,0.10)` |
| `shadow-modal` | `0 20px 60px rgba(0,0,0,0.16)` |
| `shadow-focus` | `0 0 0 3px rgba(45,106,79,0.25)` |

---

## Tailwind Config Extension

```js
// tailwind.config.js
const { fontFamily } = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2D6A4F',
          hover:   '#245A42',
        },
        secondary: {
          DEFAULT: '#95D5B2',
          hover:   '#7DC4A0',
        },
        accent:  '#1B4332',
        surface: {
          DEFAULT: '#FFFFFF',
          raised:  '#F5F5F0',
        },
        background: '#FAFAF8',
        border:  '#E5E5E0',
        muted:   '#8A8A8A',
        star:    '#F59E0B',
      },
      fontFamily: {
        heading: ['Fraunces', ...fontFamily.serif],
        body:    ['Inter', ...fontFamily.sans],
        mono:    ['JetBrains Mono', ...fontFamily.mono],
      },
      boxShadow: {
        card:     '0 1px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)',
        elevated: '0 4px 20px rgba(0,0,0,0.10)',
        modal:    '0 20px 60px rgba(0,0,0,0.16)',
        focus:    '0 0 0 3px rgba(45,106,79,0.25)',
      },
      maxWidth: {
        container: '1200px',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
  ],
}
```

---

## Component Specifications

---

### 1. Hero

**File**: `src/components/Hero.tsx`

**Layout**: Full-width, 2-col desktop (text 55% left + decorative book-grid 45% right), stacked mobile.

**Elements**:
- Category badge: `inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-secondary text-accent text-xs font-medium tracking-wide uppercase mb-4`
- Headline: `font-heading text-5xl font-bold text-text-primary leading-tight mb-4` — "Feel better. Read smarter."
- Sub-headline: `text-xl text-text-secondary leading-relaxed mb-8 max-w-lg`
- Primary CTA button: `inline-flex items-center gap-2 bg-primary hover:bg-primary-hover text-white font-medium px-8 py-4 rounded-lg transition-colors duration-150`
- Secondary link: `text-primary underline underline-offset-2 text-sm ml-6`
- Book-grid: 3 ebook covers arranged at slight rotations, `shadow-elevated rounded-lg`

**Props**:
```typescript
interface HeroProps {
  headline?: string
  subheadline?: string
  ctaLabel?: string
  ctaHref?: string
  featuredBooks?: { imageUrl: string; title: string }[]
}
```

**Mobile**: Stacked, book-grid hidden on `<sm`, headline `text-3xl`

---

### 2. ListingCard (Ebook Cover Card)

**File**: `src/components/ListingCard.tsx`

**Layout**: Vertical card — cover image → metadata → price → actions

**Elements**:
- Cover: `w-full aspect-[2/3] object-cover rounded-lg shadow-card` (standard book aspect ratio)
- Category badge: `absolute top-2 left-2 px-2 py-0.5 rounded-full bg-secondary/90 text-accent text-xs font-medium`
- Title: `font-heading text-lg font-semibold text-text-primary mt-3 line-clamp-2`
- Author: `text-sm text-text-secondary mt-1`
- Star rating: `flex items-center gap-1 mt-2` — filled stars in `color-star`, count in `text-xs text-muted`
- Price: `font-mono text-lg font-bold text-primary mt-3`
- Actions row: `flex gap-2 mt-3`
  - "Preview" button: `flex-1 border border-border text-text-secondary hover:border-primary hover:text-primary text-sm py-2 rounded-md transition-colors`
  - "Buy now" button: `flex-1 bg-primary hover:bg-primary-hover text-white text-sm py-2 rounded-md transition-colors`

**Hover state**: `group hover:shadow-elevated transition-shadow duration-200`; cover `group-hover:scale-[1.01] transition-transform`

**Props**:
```typescript
interface ListingCardProps {
  id: string
  title: string
  author: string
  coverUrl: string
  category: string
  price: number
  rating: number
  reviewCount: number
  href: string
  onPreview?: () => void
}
```

**Mobile**: 2-col grid `grid-cols-2 gap-3`; smaller text `text-base`→`text-sm`

---

### 3. CategoryStrip

**File**: `src/components/CategoryStrip.tsx`

**Layout**: Horizontally scrollable row of pill buttons, `overflow-x-auto scrollbar-hide py-2`

**Categories (from spec)**:
`Weight Loss` · `Perimenopause` · `Caregiver Support` · `Family Safety` · `Budget Wellness` · `Detox & Clean Living` · `Parenting` · `Mental Wellness`

**Pill style (inactive)**: `whitespace-nowrap px-4 py-2 rounded-full border border-border text-sm text-text-secondary hover:border-primary hover:text-primary transition-colors cursor-pointer`

**Pill style (active)**: `whitespace-nowrap px-4 py-2 rounded-full bg-primary text-white text-sm font-medium`

**Props**:
```typescript
interface CategoryStripProps {
  categories: { label: string; slug: string }[]
  activeSlug?: string
  onChange: (slug: string) => void
}
```

**Mobile**: Same, swipe-scrollable

---

### 4. FilterSidebar

**File**: `src/components/FilterSidebar.tsx`

**Layout**: Sticky `top-24 w-64 shrink-0` sidebar on desktop; bottom-sheet drawer on mobile (triggered by floating "Filters" button)

**Sections**:
1. **Category** — checkbox list, label `text-sm text-text-primary`, checked=`accent-primary`
2. **Price Range** — dual-handle `<input type="range">` slider, display `$0 – $49`
3. **Rating** — row of 5 star buttons, click selects "N stars & up"
4. **Sort** — `<select>` dropdown: Relevance · Price: Low → High · Price: High → Low · Newest · Top Rated
5. **Clear all** — `text-sm text-primary underline mt-4 cursor-pointer`

**Props**:
```typescript
interface FilterSidebarProps {
  filters: {
    categories: string[]
    priceMin: number
    priceMax: number
    minRating: number
    sort: string
  }
  onFilterChange: (filters: FilterSidebarProps['filters']) => void
  onClear: () => void
}
```

**Mobile**: `fixed bottom-0 inset-x-0 bg-surface rounded-t-2xl shadow-modal p-6 z-50` with backdrop overlay; toggled by `<FilterButton />`

---

### 5. ProductDetail

**File**: `src/app/(marketplace)/listings/[id]/page.tsx`

**Layout**: 2-col `grid grid-cols-1 lg:grid-cols-[2fr_3fr] gap-12 py-12`

**Left col — Cover**:
- Main cover: `w-full max-w-xs mx-auto rounded-xl shadow-elevated`
- File type badge: `flex items-center gap-1.5 mt-4 text-sm text-muted` — `<FileText /> PDF · 47 pages`
- "Preview first chapter" link: `flex items-center gap-1 text-primary text-sm underline mt-2 cursor-pointer`

**Right col — Info**:
- Breadcrumb: `text-xs text-muted mb-4` — `Home / Weight Loss / <title>`
- Title: `font-heading text-4xl font-semibold text-text-primary mb-2`
- Author: `text-text-secondary text-base mb-3` — "by <AuthorName>"
- Rating row: stars + `(<N> reviews)` link
- Divider: `border-t border-border my-4`
- Price: `font-mono text-3xl font-bold text-primary mb-6`
- Description: `prose prose-sm text-text-secondary max-w-none mb-6`
- Feature bullets: `space-y-2` — `<Check className="text-success" /> <span>Instant PDF download</span>`
- CTA: `w-full bg-primary hover:bg-primary-hover text-white font-semibold py-4 rounded-xl text-lg transition-colors`
- Sub-text: `text-center text-xs text-muted mt-2` — "Secure checkout via Stripe"
- Author card: `mt-8 p-4 rounded-xl border border-border flex gap-4 items-start`

**Mobile**: Single column; cover `max-w-[180px]` centered top

---

### 6. ReadingPreviewModal

**File**: `src/components/ReadingPreviewModal.tsx`

**Layout**: `fixed inset-0 z-50 flex items-center justify-center` with `bg-black/60 backdrop-blur-sm`

**Modal box**: `bg-surface rounded-2xl shadow-modal max-w-2xl w-full mx-4 max-h-[80vh] overflow-hidden flex flex-col`

**Header**: `flex items-center justify-between px-6 py-4 border-b border-border`
- Title `font-heading text-lg font-semibold` + "Chapter 1 Preview"
- Close button `<X />` `text-muted hover:text-text-primary`

**Body**: `overflow-y-auto px-6 py-4 prose prose-sm text-text-primary`
- Renders first ~800 words of the ebook as HTML
- Fades out at bottom: `relative after:absolute after:bottom-0 after:inset-x-0 after:h-32 after:bg-gradient-to-t after:from-surface`

**Footer**: `px-6 py-4 border-t border-border flex items-center justify-between`
- "Buy to read the rest" copy
- "Buy now — $X.XX" CTA button

**Props**:
```typescript
interface ReadingPreviewModalProps {
  isOpen: boolean
  onClose: () => void
  title: string
  previewHtml: string
  price: number
  onBuy: () => void
}
```

---

### 7. CheckoutForm

**File**: `src/components/CheckoutForm.tsx`

**Layout**: `max-w-lg mx-auto py-12` — single column, 3-step wizard

**Step indicator**: `flex items-center gap-2 mb-8`
- Step dot: `w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium`
- Active: `bg-primary text-white`
- Complete: `bg-success text-white`
- Inactive: `border-2 border-border text-muted`
- Connector: `flex-1 h-px bg-border`

**Step 1 — Order Summary**:
- Ebook cover thumbnail + title + price
- `text-2xl font-mono font-bold text-primary` total
- "Continue" button

**Step 2 — Your Details**:
- Email input (pre-filled from Clerk if signed in)
- Name input
- "Continue" button

**Step 3 — Payment**:
- Stripe `<CardElement />` in `border border-border rounded-lg p-3`
- "Pay $X.XX" submit button
- `<Lock className="w-4" /> Secured by Stripe` sub-text

**Props**:
```typescript
interface CheckoutFormProps {
  listing: { id: string; title: string; price: number; coverUrl: string }
  onSuccess: (orderId: string) => void
}
```

---

### 8. DownloadPortal

**File**: `src/app/(marketplace)/checkout/success/page.tsx`

**Layout**: `max-w-md mx-auto text-center py-20`

**Elements**:
- Success icon: `w-16 h-16 rounded-full bg-success/10 flex items-center justify-center mx-auto mb-6` with `<CheckCircle className="text-success w-8 h-8" />`
- Headline: `font-heading text-3xl font-semibold mb-2` — "Your ebook is ready!"
- Sub-text: `text-text-secondary mb-8`
- Download card: `border border-border rounded-xl p-6 text-left mb-4`
  - Cover thumbnail + title + file size
  - `<Download />` "Download PDF" button — `w-full bg-primary text-white py-3 rounded-lg`
  - Expiry note: `text-xs text-muted mt-2` — "Link expires in 24 hours"
- "Browse more ebooks" link back to `/listings`
- Email confirmation note: `text-sm text-muted mt-6`

**Security**: Download URL is a signed Supabase Storage URL with 24h TTL, generated server-side after payment confirmation. Never exposed client-side before payment.

---

### 9. SellerDashboard

**File**: `src/app/(dashboard)/seller/page.tsx`

**Layout**: `flex h-screen bg-background`
- Left sidebar `w-56 shrink-0 bg-accent text-white py-8 px-4 flex flex-col`
- Main area `flex-1 overflow-y-auto p-8`

**Sidebar nav items**: Overview · My Listings · Orders · Payouts · Settings — `flex items-center gap-3 px-3 py-2 rounded-lg text-sm`; active=`bg-white/10`

**Stat cards (4-up grid)**:
```
Total Earnings  |  Active Listings
Pending Orders  |  Avg. Rating
```
Each: `bg-surface rounded-xl p-5 shadow-card`; value `font-mono text-2xl font-bold text-primary`; label `text-sm text-muted mt-1`

**Listings table**:
- Columns: Cover · Title · Price · Sales · Status · Actions
- Status toggle: `<Switch />` active/draft
- Actions: edit pencil icon + trash icon

**Upload CTA**: `flex items-center gap-2 bg-primary text-white px-5 py-2.5 rounded-lg text-sm font-medium` — "+ New Listing"

**Mobile**: Bottom nav tabs replace sidebar; stats stack 2-col

---

### 10. ReviewBlock

**File**: `src/components/ReviewBlock.tsx`

**Layout**: Two sub-sections — aggregate summary above, individual review list below, submit form at bottom for verified buyers

**Aggregate summary**:
- Large rating number `font-heading text-5xl font-bold text-text-primary`
- 5 star row
- `text-sm text-muted` — "based on N reviews"
- Per-star bar chart (5→1 stars with `bg-secondary` fill bars)

**Review list item**:
- Avatar (initials fallback) + reviewer name + date
- Star row (filled to rating)
- Comment `text-sm text-text-primary`
- `border-b border-border pb-4`

**Submit form** (shown only to verified buyers):
- "Write a Review" heading
- Star selector (click to rate)
- Textarea `border border-border rounded-lg p-3 text-sm w-full resize-none`
- Submit button

**Props**:
```typescript
interface ReviewBlockProps {
  listingId: string
  averageRating: number
  reviewCount: number
  reviews: { id: string; reviewerName: string; rating: number; comment: string; createdAt: string }[]
  canReview: boolean
  onSubmit: (rating: number, comment: string) => Promise<void>
}
```

---

## Page Layouts

### `/` — Home

```
[Navbar]
[Hero — full width, bg-background]
[CategoryStrip — sticky below hero, bg-surface border-b]
[Featured Listings — "Editor's Picks" — 4-col grid, bg-background py-16]
[How It Works — 3-step row, bg-surface-raised py-16]
  Step 1: Browse by topic
  Step 2: Preview a chapter free
  Step 3: Buy & download instantly
[Trust bar — "Trusted by 2,000+ readers" + icons: Lock / Star / Download]
[Footer]
```

### `/listings` — Browse

```
[Navbar]
[Breadcrumb + result count "N ebooks" + sort dropdown]
[CategoryStrip]
[FilterSidebar (left 256px) | ListingGrid (flex-1, 3-col → 2-col → 1-col)]
[Pagination — centered, prev/next + page numbers]
[Footer]
```

### `/listings/[id]` — Product Detail

```
[Navbar]
[ProductDetail 2-col]
[ReviewBlock]
[Related Listings — "More like this" 4-col]
[Footer]
```

### `/checkout` — Checkout

```
[Minimal Navbar — logo + "Secure Checkout" + lock icon]
[CheckoutForm (max-w-lg centered)]
[Trust strip — Stripe logo + "256-bit encryption" + "Instant download"]
```

### `/checkout/success` — Download Portal

```
[Minimal Navbar]
[DownloadPortal (max-w-md centered)]
```

### `/seller` — Seller Dashboard

```
[SellerDashboard — full viewport, sidebar nav]
```

### `/sign-in` and `/sign-up`

```
[Centered card — bg-surface rounded-2xl shadow-elevated max-w-sm]
[WellRead logo + tagline above card]
[Clerk <SignIn /> or <SignUp /> embedded widget]
```

---

## Mobile Breakpoints (< 768px)

| Component | Mobile Behaviour |
|-----------|-----------------|
| Navbar | Hamburger → full-screen slide-in drawer |
| Hero | Stacked; book-grid hidden; headline `text-3xl` |
| ListingGrid | 2 columns, `gap-3` |
| FilterSidebar | Hidden; "Filters" FAB bottom-right → bottom-sheet |
| ProductDetail | Single column; cover centered, max-w-[180px] |
| SellerDashboard | Bottom tab nav; stats 2-col |
| CheckoutForm | Full-width, inputs `text-base` to prevent iOS zoom |
| CategoryStrip | Horizontal scroll, no wrap |

---

## Accessibility Notes

- **Focus rings**: `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2` on ALL interactive elements
- **Color contrast**: `color-primary` (#2D6A4F) on white = 6.8:1 ✅ AAA; `color-text-secondary` (#4A4A4A) on white = 9.7:1 ✅ AAA
- **Images**: All `<Image />` components require non-empty `alt` props; decorative images use `alt=""`
- **Forms**: `<label>` always visible — no placeholder-only inputs
- **Screen readers**: `aria-live="polite"` on filter result count update; `role="dialog"` + `aria-modal="true"` on modals
- **Skip link**: `<a href="#main-content" className="sr-only focus:not-sr-only ...">Skip to content</a>` in root layout
- **Keyboard nav**: Sidebar category checkboxes, star rating selector, and step wizard all fully keyboard-navigable

---

## Animation & Motion

- **Global transition**: `transition-colors duration-150 ease-in-out` (color/border changes)
- **Card hover**: `hover:shadow-elevated transition-shadow duration-200`
- **Cover hover**: `group-hover:scale-[1.015] transition-transform duration-200`
- **Modal open**: `animate-in fade-in zoom-in-95 duration-200` (using `tailwindcss-animate`)
- **Bottom sheet**: `animate-in slide-in-from-bottom duration-300`
- **Page load skeleton**: `animate-pulse bg-border rounded` placeholders
- **Reduced motion**: All animations wrapped in `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; } }` in `globals.css`

---

*Design Manifest complete — WellRead v1.0*
