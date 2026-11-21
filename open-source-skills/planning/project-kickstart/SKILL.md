---
name: project-kickstart
description: Master orchestrator for kickstarting any new app, website, or software project Use this skill whenever the user wants to start a new project, brainstorm an app idea, create a PRD or foundation documents, plan epics/sprints/tasks, set up a development workflow (PRs, features, bug fixes), design an offer or pricing model, or plan a launch. Trigger it even if the user just says "I have an app idea", "let's plan a new project", "kickstart", "new build",. It walks the project through 7 gated phases from idea to post-launch growth.
---

# Project Kickstart — Master Planning & Delivery Skill

This skill turns a raw idea into a fully planned, launch-ready project. Instead of
copy-pasting prompts into a chat and downloading zip files, you (Claude) execute the whole
pipeline directly — creating real files in the project folder, gating each phase
on user approval.

**Core philosophy (why the phases are ordered this way):**
1. **Offer before product.** Per Alex Hormozi ($100M Offers), the offer is the #1
   lever in any business. A mediocre product attached to a Grand Slam Offer beats
   a great product nobody wants to pay for. So we validate the offer BEFORE
   writing 40 planning documents.
2. **Documents before code.** LLMs are probabilistic; business logic must be
   deterministic. Architecture, auth, data, and permissions get locked in writing
   before any UI or code exists.
3. **Small verifiable tasks.** Work ships as epics → sprints → tasks small enough
   to implement, test, and verify in a single focused session (addyosmani
   planning-and-task-breakdown principle).
4. **Launch is a repeatable muscle, not an event.** The best companies launch
   again and again (coreyhaines launch principle). Launch planning starts during
   development, not after.

## Operating rules

- **Gates:** At the end of every phase, summarize what was produced and ask the
  user to approve before advancing. Never skip a gate. The user may say "fast
  mode" to collapse gates for small projects — then confirm only after Phase 2
  and Phase 4.
- **Files, not chat dumps:** Every artifact is written to disk in the project
  folder (see Directory layout below). Never ask the user to copy-paste content
  into files — write the files yourself.
- **Ask, don't assume, for Section-0 inputs:** working name, theme/visual
  reference, purpose, initial modules, constraints, target users, monetization
  intent. Everything else you may draft and let the user correct.
- **Scale to the project:** a weekend tool doesn't need all 43 documents. Ask at
  Phase 0 whether this is **Full** (SaaS / revenue product → all docs), **Lean**
  (MVP validation → ~12 core docs), or **Micro** (internal tool → PRD + data
  model + delivery plan only). Mark skipped docs as "N/A — Micro/Lean scope" in
  the PRD so the gap is a decision, not an accident.

## Directory layout (create at Phase 0)

```
<project-name>/
├── docs/
│   ├── 00-PRD.md                  # master doc, references all others
│   ├── foundation/                # the 42 foundation docs (NN-kebab-name.md)
│   ├── decisions/                 # ADRs: one file per irreversible decision
│   └── directives/                # SOPs for agentic workflows (if any)
├── planning/
│   ├── roadmap.md                 # now / next / later, outcome-based
│   ├── epics/                     # one file per epic
│   └── sprints/                   # sprint-NN.md with task tables
├── launch/
│   ├── offer.md                   # Grand Slam Offer + money model
│   ├── launch-plan.md             # channel plan, Product Hunt playbook
│   └── assets/                    # copy, video briefs, screenshots
└── (code goes here after Phase 5 approval)
```

## Default tech stack (override if the user says otherwise)

Frontend: React, Next.js (App Router, SSR/SSG), Tailwind CSS, daisyUI.
Backend/Data: Supabase (Postgres, Auth, RLS, Storage), Next.js server functions.
Auth: Google OAuth + email, custom domain auth (no Supabase URLs visible),
password reset/change, account deletion & export, session persistence.
Hosting: Vercel. Analytics: Plausible (cookie-gated). Payments: Stripe.
AI/Dev: GitHub, Claude Code, OpenAI (latest) where the product needs LLM features.

**Core reliability rule:** any repeatable, automated, scheduled, multi-step,
API-driven, or ingestion workflow must follow the 3-layer architecture —
(1) Directives (markdown SOPs) → (2) Orchestration (decision logic) →
(3) Execution (deterministic code/scripts). The AI plans and routes; execution
is deterministic. Never leave business logic living only inside an LLM prompt.

---

## The 7 phases

### Phase 0 — Intake & Brainstorm
Collect the Section-0 inputs (see Operating rules). Explore the idea with the
user: use case, target users, modules, constraints, competitive landscape,
riskiest assumption. Decide scope tier (Full / Lean / Micro). Create the
directory layout. Output: `docs/foundation/01-product-objectives.md` draft +
scope decision recorded in `docs/decisions/`.

### Phase 1 — Offer, Market & Money Model (Hormozi)
Before any architecture: who pays, for what, and why it's irresistible.
**Read `references/offer-and-monetization.md`** and work through: market
selection scorecard, Value Equation, offer stack, guarantee, pricing, and the
money model (attraction → upsell → downsell → continuity; target 30-day cash >
CAC). Score the offer 0–10 and iterate with the user until ≥ 8, or record an
explicit decision to proceed anyway (e.g. free/internal tools skip pricing but
still do the Value Equation for adoption). Output: `launch/offer.md` +
foundation docs 40 & (draft) 07-brand-positioning.

### Phase 2 — Foundation Documents
**Read `references/foundation-docs.md`** for the full 42-doc catalog, per-doc
outlines, generation order, and the scope-tier matrix (which docs Lean/Micro
skip). Generate docs in dependency order, batching 3–5 per gate so the user
can review without fatigue. Every doc assumes the tech stack above (Supabase +
RLS, GitHub workflows) and must be deterministic, auditable, and ready for
AI-assisted code generation. Output: `docs/foundation/` populated.

### Phase 3 — PRD & Development Path
Write `docs/00-PRD.md`: references every foundation doc, states what the MVP
includes/excludes, and lays out the development path in stages. Include a
plain-English step-by-step appendix for all manual work the user must do
(Supabase project creation, API keys, env vars, custom domain, Stripe setup,
OAuth consent screens). Gate: user approves the PRD. Architecture, auth, data
model, and permissions are now **locked** — changes after this point go through
the change-management process (doc 38), not casual edits.

### Phase 4 — Delivery Plan: Roadmap, Epics, Sprints, Tasks
**Read `references/delivery-workflow.md`.** Build the outcome-based roadmap
(now/next/later), decompose into epics, sequence sprints, and break the first
sprint into tasks with explicit acceptance criteria — each small enough for one
focused session. Also set up the engineering workflow: branch strategy, PR
template + review checklist, bug intake → triage → fix loop, definition of
done. Output: `planning/` populated + `.github/` templates when a repo exists.

### Phase 5 — Build Loop
Development starts only after Phase 3–4 approval. For each task: branch →
implement → verify against acceptance criteria → PR → review → merge. Follow
the worktree-pr-flow skill if available. New feature requests and bugs found
mid-build enter through the intake process in `references/delivery-workflow.md`
— they never bypass the backlog. Re-read the relevant foundation doc before
touching auth, data model, RLS, or billing code.

### Phase 6 — Launch
**Read `references/launch-playbook.md`.** Start this phase while Phase 5 is
still running (launch prep is 2–4 weeks of lead time). Covers: lead magnets and
the Core Four channels ($100M Leads), the repeated-launch calendar, the Product
Hunt playbook, and the launch video brief (use the product-launch-video skill
if installed). Output: `launch/launch-plan.md` + assets.

### Phase 7 — Post-Launch: Feedback & Iteration
Wire the loop back to Phase 4: analytics review vs the KPI spec (doc 28),
feedback/bug intake (doc 33), and a monthly "re-launch" cadence — every
meaningful improvement is a new announcement. Offer and pricing get re-scored
quarterly against the Value Equation.

---

## Reference files — when to read what

| File | Read when |
|---|---|
| `references/offer-and-monetization.md` | Phase 1, and any pricing/monetization/positioning question |
| `references/foundation-docs.md` | Phase 2, and whenever generating or updating a foundation doc |
| `references/delivery-workflow.md` | Phase 4–5, and any epic/sprint/task/PR/bug-workflow question |
| `references/launch-playbook.md` | Phase 6–7, and any launch/marketing/lead-gen question |

If the user enters mid-process ("I already have a PRD, plan my sprints"), jump
to the matching phase — but skim the earlier phases' outputs first and flag any
missing prerequisite (e.g. no offer doc, no locked data model) instead of
silently proceeding.
