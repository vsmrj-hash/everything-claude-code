# Marketplace Workflow Skill

## When to Use

Activate this skill when:
- A user runs `/marketplace <brief>`
- A user asks to "build a marketplace", "launch a marketplace", or "deploy a marketplace to Vercel"
- You are acting as any of the four marketplace pipeline agents
- You need to understand how the four-agent pipeline fits together

## How It Works

The marketplace workflow is a **sequential four-agent pipeline** controlled by the `marketplace-orchestrator`. Each agent produces a file-based artifact that the next agent reads as input — creating a reliable, restartable pipeline.

### Pipeline Map

```
User: /marketplace <brief>
              │
              ▼
┌─────────────────────────────────────┐
│  Agent 1: marketplace-orchestrator  │  model: opus
│  Input:   user brief                │
│  Output:  .claude/marketplace-      │
│           build-spec.yaml           │
└─────────────────┬───────────────────┘
                  │ delegates to ↓
┌─────────────────────────────────────┐
│  Agent 2: marketplace-designer      │  model: sonnet
│  Input:   build-spec.yaml           │
│  Output:  .claude/marketplace-      │
│           design-manifest.md        │
└─────────────────┬───────────────────┘
                  │ delegates to ↓
┌─────────────────────────────────────┐
│  Agent 3: marketplace-deployer      │  model: sonnet
│  Input:   build-spec.yaml           │
│           design-manifest.md        │
│  Output:  .claude/marketplace-      │
│           deployment-receipt.md     │
└─────────────────┬───────────────────┘
                  │ delegates to ↓
┌─────────────────────────────────────┐
│  Agent 4: marketplace-publisher     │  model: sonnet
│  Input:   build-spec.yaml           │
│           design-manifest.md        │
│           deployment-receipt.md     │
│  Output:  .claude/marketplace-      │
│           publication-report.md     │
└─────────────────┬───────────────────┘
                  │
                  ▼
         🚀 Live marketplace URL
```

### Artifacts (file-based message passing)

| File | Produced by | Consumed by |
|------|-------------|-------------|
| `.claude/marketplace-build-spec.yaml` | orchestrator | designer, deployer, publisher |
| `.claude/marketplace-design-manifest.md` | designer | deployer, publisher |
| `.claude/marketplace-deployment-receipt.md` | deployer | publisher |
| `.claude/marketplace-publication-report.md` | publisher | orchestrator (final summary) |

All artifacts live in `.claude/` (gitignored by convention) so they don't pollute the repo.

## Agent Responsibilities

### Agent 1 — Orchestrator (`marketplace-orchestrator`)
- Parse the user's natural-language brief
- Extract: name, category, audience, features, design tone, tech stack, Vercel scope
- Ask clarifying questions if required fields are missing
- Produce structured YAML Build Spec
- Invoke Designer → wait → invoke Deployer → wait → invoke Publisher → wait
- Handle errors by re-tasking the failing agent (max 3 retries)
- Deliver final summary with live URL to user

### Agent 2 — Designer (`marketplace-designer`)
- Translate Build Spec into a complete visual language
- Define all design tokens (colors, typography, spacing, shadows)
- Write component specs for every required component
- Define page layouts and mobile breakpoints
- Produce a Tailwind config extension block
- Output must be implementation-ready (deployer should never need to guess)

### Agent 3 — Deployer (`marketplace-deployer`)
- Scaffold Next.js 14 App Router project with all dependencies
- Implement every component per the Design Manifest
- Build all API routes (listings CRUD, Stripe checkout, webhook handler)
- Set up Drizzle schema and push migrations to Supabase
- Configure Vercel project, set env vars, and deploy to production
- Run quality gates before writing the receipt (build must pass)

### Agent 4 — Publisher (`marketplace-publisher`)
- Verify all pages return 200
- Audit feature completeness against the spec
- Run security checklist (auth on mutations, webhook verification, no secrets in code)
- Check performance thresholds (Lighthouse ≥ 70 performance, ≥ 90 accessibility)
- Classify all issues: 🔴 Blocking / 🟡 Advisory / 🟢 Polish
- Return GO (approved) or NO-GO (with precise fix list) to orchestrator

## Technology Stack

| Concern | Choice | Why |
|---------|--------|-----|
| Framework | Next.js 14 App Router | Server components, edge-ready, Vercel-native |
| Styling | Tailwind + shadcn/ui | Utility-first, accessible components |
| Auth | Clerk | Fastest setup, embeddable UI, webhooks |
| Database | Supabase + Drizzle ORM | Postgres, type-safe ORM, free tier |
| Payments | Stripe Checkout | Industry standard, test mode, webhooks |
| Deployment | Vercel | MCP-integrated, instant previews |
| Icons | Lucide React | MIT, tree-shakeable, consistent |

## Error Handling Patterns

### Agent Failure Recovery
```
orchestrator detects agent failure
  → read error output
  → triage: missing data? wrong config? API error?
  → re-task with corrected input
  → max 3 retries
  → if still failing: surface to user with diagnosis
```

### NO-GO Recovery Loop
```
publisher returns NO-GO with blocking issue list
  → orchestrator reads blocking issues
  → re-tasks deployer with specific fix instructions
  → deployer applies fixes and redeploys
  → publisher re-reviews
  → repeat until GO or user escalation
```

### Missing Secrets
```
deployer needs API key (Stripe, Supabase, Clerk)
  → orchestrator asks user directly
  → user provides keys
  → orchestrator passes to deployer
  → deployer adds to Vercel env vars
  → NEVER store secrets in files
```

## Design Tone Reference

| Tone | Best for | Color strategy |
|------|----------|----------------|
| `minimal` | B2B, digital tools | Monochrome + 1 accent |
| `vibrant` | Consumer, creative | High-sat 3-color palette |
| `enterprise` | Professional services | Navy/gray + trusted blue |
| `playful` | Kids, community, hobbies | Pastels + bold accent |

## Examples

### Example 1 — Digital Goods Marketplace

**Brief**: `/marketplace Marketplace for selling AI-generated art prints. Buyers are collectors, sellers are AI artists. Clean, gallery-style design.`

**Build Spec excerpt**:
```yaml
marketplace:
  name: "ArtDrop"
  slug: "artdrop"
  category: digital-goods
  design:
    tone: minimal
    primary_color: "#1A1A2E"
  features: [search, auth, listings-crud, cart, checkout, instant-download, ratings]
```

**Result**: Gallery-style Next.js marketplace with instant download after Stripe payment, deployed at `artdrop.vercel.app`.

---

### Example 2 — Service Marketplace

**Brief**: `/marketplace A platform where local personal trainers offer 1:1 session bookings to fitness enthusiasts in their city.`

**Build Spec excerpt**:
```yaml
marketplace:
  name: "FitLocal"
  slug: "fitlocal"
  category: services
  design:
    tone: vibrant
    primary_color: "#FF6B35"
  features: [search, auth, listings-crud, booking-calendar, ratings, location-filter]
```

**Result**: Vibrant service marketplace with calendar-based booking, location filter, deployed at `fitlocal.vercel.app`.

---

### Example 3 — Physical Goods Marketplace

**Brief**: `/marketplace Vintage vinyl marketplace for collectors. Sellers list albums with condition grades, buyers filter by genre and decade.`

**Build Spec excerpt**:
```yaml
marketplace:
  name: "VinylVault"
  slug: "vinylvault"
  category: physical
  design:
    tone: playful
    primary_color: "#2D1B69"
  features: [search, auth, listings-crud, cart, checkout, condition-grading, genre-filter]
```

**Result**: Record marketplace with condition grading system, genre/decade filters, deployed at `vinylvault.vercel.app`.

## Integration with Other Skills

- Use `feature-development` skill when adding new features post-launch
- Use `database-migration` skill when evolving the Supabase schema
- Use `security-review` skill before switching to production Stripe keys
- Use `tdd-workflow` skill when adding test coverage to deployed components

## Related Commands

- `/marketplace` — Launch the full pipeline
- `/plan` — Plan a specific feature before adding it
- `/code-review` — Review marketplace code quality
- `/verify` — Verify a deployed change
- `/e2e` — Generate E2E tests for marketplace flows
