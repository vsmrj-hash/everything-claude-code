---
description: Launch the 4-agent marketplace pipeline. Understands your product brief, designs the UI, deploys to your Vercel, and publishes the live marketplace — end to end.
---

# /marketplace — Build & Deploy a Marketplace

This command activates the **marketplace-orchestrator** agent, which drives a four-agent pipeline to turn your product idea into a live Vercel marketplace.

## What Happens

```
/marketplace <your product description>
         │
         ▼
[Agent 1] marketplace-orchestrator
  → Parses your brief, produces a Build Spec
         │
         ▼
[Agent 2] marketplace-designer
  → Designs color tokens, typography, every component
         │
         ▼
[Agent 3] marketplace-deployer
  → Scaffolds Next.js, wires Supabase + Stripe + Clerk, deploys to Vercel
         │
         ▼
[Agent 4] marketplace-publisher
  → QA audit, security review, go/no-go decision
         │
         ▼
🚀 Live marketplace URL delivered to you
```

## Usage

```
/marketplace I want to sell digital illustration packs to indie game developers

/marketplace A service marketplace where freelance chefs offer meal-prep services
              in local neighborhoods

/marketplace Platform for vintage vinyl record collectors to buy and sell albums
```

## What to Include in Your Brief

The more you give, the faster the pipeline runs without asking questions:

| Element | Example |
|---------|---------|
| **What's being sold** | Digital assets, services, physical goods |
| **Who buys** | Indie devs, local families, collectors |
| **Who sells** | Designers, chefs, individual collectors |
| **Key features** | Search, ratings, instant download, subscriptions |
| **Visual vibe** | Minimal, vibrant, enterprise, playful |
| **Vercel scope** | Your Vercel team name or "personal" |

## Minimal Brief (orchestrator will ask for missing info)

```
/marketplace A marketplace for handmade ceramic goods
```

## What Gets Built

A full-stack Next.js 14 marketplace including:

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 14 App Router |
| Styling | Tailwind CSS + shadcn/ui |
| Auth | Clerk |
| Database | Supabase (PostgreSQL + Drizzle ORM) |
| Payments | Stripe Checkout |
| Deployment | Vercel |
| Icons | Lucide React |

### Pages
- `/` — Home with hero and featured listings
- `/listings` — Browse with filter sidebar and search
- `/listings/[id]` — Product detail with reviews
- `/checkout` — Stripe-powered checkout
- `/sign-in` / `/sign-up` — Auth
- `/seller` — Seller dashboard (listings, orders, payouts)

## Artifacts Produced

| File | Contents |
|------|---------|
| `.claude/marketplace-build-spec.yaml` | Structured requirements parsed from your brief |
| `.claude/marketplace-design-manifest.md` | Full design system and component specs |
| `.claude/marketplace-deployment-receipt.md` | Vercel URLs, deployment ID, env var checklist |
| `.claude/marketplace-publication-report.md` | QA results, issue list, go/no-go decision |

## After the Pipeline Completes

You'll receive:

```markdown
🚀 Marketplace Live — <your marketplace name>

Live URL: https://<slug>.vercel.app
Dashboard: https://vercel.com/…

Next Steps:
1. Add your Stripe keys in Vercel → Settings → Environment Variables
2. Seed initial listings via /admin/seed
3. Configure custom domain
4. Enable Stripe webhooks
```

## Secrets You'll Need

Have these ready — the deployer will prompt you to paste them:

1. **Clerk** — Get from [clerk.com](https://clerk.com) → Create Application
2. **Supabase** — Get from [supabase.com](https://supabase.com) → New Project → Settings → API
3. **Stripe** — Get from [stripe.com](https://stripe.com) → Developers → API Keys
4. **Vercel** — Already connected if you're running in Claude Code on the web

## Related Agents

| Agent | File | Role |
|-------|------|------|
| marketplace-orchestrator | `agents/marketplace-orchestrator.md` | Pipeline brain |
| marketplace-designer | `agents/marketplace-designer.md` | UI/UX design |
| marketplace-deployer | `agents/marketplace-deployer.md` | Code + Vercel |
| marketplace-publisher | `agents/marketplace-publisher.md` | QA + go-live |

## Related Commands

- `/plan` — Plan a feature before building
- `/code-review` — Review code after changes
- `/verify` — Verify a deployed change works
