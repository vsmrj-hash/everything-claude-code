# Deployment Receipt — WellRead

## Status: 🔄 BUILD COMPLETE — DEPLOYING TO VERCEL

**Built at**: 2026-05-23
**Project path**: `/home/user/wellread-market/`
**Framework**: Next.js (Tailwind v4, App Router)
**Build result**: ✅ 11 routes, zero TypeScript errors

---

## Routes Implemented

| Route | Type | Description |
|-------|------|-------------|
| `/` | Server | Home — Hero, Editor's Picks (8 ebooks), How It Works, Trust bar |
| `/listings` | Server | Browse — category filter, search, 8 seeded ebooks |
| `/listings/[id]` | Server | Product detail — cover, stars, description, buy CTA |
| `/checkout` | Server | Stripe checkout (placeholder until keys added) |
| `/checkout/success` | Server | Download portal |
| `/seller` | Server (protected) | Seller dashboard — sidebar, stat cards, listings table |
| `/sign-in` | Server | Clerk SignIn widget |
| `/sign-up` | Server | Clerk SignUp widget |
| `/api/listings` | API | GET with category/q filters |
| `/api/checkout` | API | POST — Stripe session stub |
| `/api/webhooks/stripe` | API | Stripe webhook handler stub |

## Vercel Config

| Field | Value |
|-------|-------|
| Team | vsmrj-hashs-projects |
| Team ID | team_ogEoLQvS3UP9AWEtv6OatFGk |
| Project name | wellread-market |

## Environment Variables Required

```
# Clerk Auth
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/

# Supabase
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=

# Stripe
STRIPE_SECRET_KEY=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=

# App
NEXT_PUBLIC_BASE_URL=https://wellread-market.vercel.app
NEXT_PUBLIC_SITE_NAME=WellRead
```

## Notes
- App renders fully with static seed data (8 ebooks, complete UI) without any keys
- Services activate once keys are added in Vercel Dashboard → Settings → Environment Variables
- Clerk, Supabase, Stripe all have graceful stubs until connected
