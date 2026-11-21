# Foundation Document Catalog (42 docs + PRD)

The canonical document set for Phase 2. A 40-doc set, renumbered cleanly, plus three additions from the master-skill
cross-reference: Offer & Monetization (40), Launch & Growth (41), and Delivery
Plan (42). The PRD is `docs/00-PRD.md`; everything else lives in
`docs/foundation/` as `NN-kebab-name.md`.

Every doc must: assume Supabase + RLS and GitHub workflows (unless stack was
overridden), be deterministic and auditable, and be directly usable by an AI
developer without further clarification. Write real content — no placeholder
sections. If a section genuinely can't be decided yet, write the open question
and who decides it.

## Contents
1. [Catalog by layer](#catalog-by-layer)
2. [Scope-tier matrix](#scope-tier-matrix)
3. [Generation order & batching](#generation-order--batching)
4. [Per-doc content notes](#per-doc-content-notes)

---

## Catalog by layer

### Layer A — Strategy & Foundation
| # | File | Doc |
|---|---|---|
| 01 | 01-product-objectives.md | Product & Website Objectives |
| 02 | 02-audience-personas.md | Audience, Personas & Intent States |
| 03 | 03-information-architecture.md | Information Architecture & Routing |
| 04 | 04-public-vs-authenticated.md | Public Pages vs Authenticated Surfaces |
| 05 | 05-feature-framework.md | Feature & Capability Framework |
| 06 | 06-lifecycle-methodology.md | Product Lifecycle & Methodology |
| 07 | 07-brand-positioning.md | Brand & Positioning |
| 08 | 08-seo-llmseo.md | SEO + LLMSEO Strategy |

### Layer B — UX, UI & Structure
| # | File | Doc |
|---|---|---|
| 09 | 09-page-types-app-shell.md | Page Types & App Shell Definitions |
| 10 | 10-navigation-permissions.md | Navigation, Permissions & Route Protection |
| 11 | 11-design-system.md | Design System (Web + App) |
| 12 | 12-onboarding-activation.md | Onboarding, Activation & Conversion Strategy |
| 13 | 13-user-flows.md | User Flows & Journey Maps |

### Layer C — Users, Auth & Data
| # | File | Doc |
|---|---|---|
| 14 | 14-accounts-authentication.md | User Accounts & Authentication (Supabase Auth, email/OAuth/magic links, custom-domain auth, sessions, logout) |
| 15 | 15-authorization-rls.md | Authorization, Roles & RLS Matrix (Owner/Admin/Member/Viewer, RLS rules, ownership models) |
| 16 | 16-user-lifecycle.md | User Lifecycle Management (creation, verification, password recovery, deletion, GDPR export/delete) |

### Layer D — Data & Systems
| # | File | Doc |
|---|---|---|
| 17 | 17-data-model-erd.md | Data Model & ERD |
| 18 | 18-data-dictionary.md | Data Dictionary |
| 19 | 19-state-event-model.md | State & Event Model |
| 20 | 20-api-contract.md | API Contract Specification |
| 21 | 21-ai-integration.md | AI Integration & Prompt Architecture |

### Layer E — Policies, Compliance & Trust
| # | File | Doc |
|---|---|---|
| 22 | 22-cookies-consent.md | Cookies, Consent & Tracking (categories, consent storage, analytics gating, region-aware) |
| 23 | 23-privacy-policy.md | Privacy Policy |
| 24 | 24-terms-of-service.md | Terms of Use / Service |
| 25 | 25-acceptable-use.md | Acceptable Use Policy |
| 26 | 26-compliance-notes.md | Compliance & Regulatory Notes (GDPR/CCPA, residency, auditability) |

### Layer F — Operations & Monetization
| # | File | Doc |
|---|---|---|
| 27 | 27-notifications-messaging.md | Notifications & Messaging |
| 28 | 28-billing-entitlements.md | Billing, Plans & Entitlements *(conditional — paid products)* |
| 29 | 29-analytics-kpis.md | Analytics & KPI Spec |
| 30 | 30-performance-reliability.md | Performance & Reliability Targets |
| 31 | 31-testing-seed-data.md | Testing Strategy & Seed Data |
| 32 | 32-security-threat-model.md | Security, Threat Modeling & Monitoring |
| 33 | 33-operational-playbook.md | Operational Playbook |
| 34 | 34-feedback-intake.md | Feedback, Bug Reporting & Feature Intake |

### Layer G — AI & Change Control
| # | File | Doc |
|---|---|---|
| 35 | 35-ai-builder-instructions.md | AI Builder Instructions |
| 36 | 36-ai-content-prompt-rules.md | AI Content & Prompt Rules |
| 37 | 37-agentic-workflows.md | Agentic Workflows & Directives *(conditional — see below)* |
| 38 | 38-change-management.md | Change Management & Versioning |
| 39 | 39-code-quality.md | Code Quality & Continuous Evaluation |

### Layer H — Growth (new in this skill)
| # | File | Doc |
|---|---|---|
| 40 | 40-offer-monetization.md | Offer & Monetization Strategy (from Phase 1 / `references/offer-and-monetization.md`) |
| 41 | 41-launch-growth.md | Launch & Growth Plan (from Phase 6 / `references/launch-playbook.md`; summary lives here, working files in `launch/`) |
| 42 | 42-delivery-plan.md | Delivery Plan: Epics, Sprints & Task Breakdown (from Phase 4; summary here, working files in `planning/`) |

### PRD — `docs/00-PRD.md`
Written LAST (Phase 3). References all other docs by number, defines MVP
in/out scope, staged development path, and the manual-work appendix
(Supabase setup, API keys, env vars, domains, Stripe, OAuth screens) as
plain-English step-by-step instructions.

---

## Scope-tier matrix

- **Full** (revenue SaaS): all 42 + PRD. Doc 28 only if paid; doc 37 only if
  the product has automation/pipelines/agents/scraping/scheduled jobs.
- **Lean** (MVP validation): 01, 02, 05, 12, 13, 14, 15, 17, 20, 29, 40, 42
  \+ PRD. Legal docs (23–25) use short standard templates. Everything else
  gets a one-line "N/A — Lean scope" entry in the PRD.
- **Micro** (internal tool): PRD + 17 (data model) + 42 (delivery plan);
  add 14/15 if it has users beyond the owner.

## Generation order & batching

Generate in dependency order, gating every batch with the user:

1. **Batch 1 — Strategy:** 01, 02, 07, 40 (40 comes in from Phase 1)
2. **Batch 2 — Structure:** 05, 03, 04, 08
3. **Batch 3 — Data core:** 17, 18, 15, 14, 16 ← the lock-in batch; review hardest here
4. **Batch 4 — Systems:** 19, 20, 21, 37 (if applicable)
5. **Batch 5 — UX:** 09, 10, 11, 12, 13
6. **Batch 6 — Ops:** 27, 28, 29, 30, 31, 32, 33, 34
7. **Batch 7 — Policy & control:** 22, 23, 24, 25, 26, 35, 36, 38, 39, 06
8. **Batch 8 — PRD:** 00 (+ 41, 42 stubs to be filled in Phases 4 & 6)

Rationale: data/auth (batch 3) constrains everything downstream, so it's
reviewed before UX and ops are written against it.

## Per-doc content notes

Notes for the docs that most often come out shallow:

- **05 Feature framework:** every feature tagged MVP / v1.x / later, and mapped
  to the Value Equation lever it serves (dream outcome, likelihood, time,
  effort). A feature that maps to no lever is a cut candidate.
- **08 SEO + LLMSEO:** include how the product's public surface serves the lead
  magnet and primary channel chosen in doc 40. LLMSEO = structured, quotable,
  entity-rich public pages that LLM crawlers can cite.
- **15 RLS matrix:** an actual table — every table × every role × SELECT/
  INSERT/UPDATE/DELETE, with the Postgres policy expression sketched. This doc
  prevents the single most expensive class of vibe-coding security bugs.
- **17 ERD:** Mermaid `erDiagram` + per-table ownership column conventions
  (`user_id`/`org_id`), soft-delete policy, timestamp conventions.
- **20 API contract:** route table (path, method, auth, role, request/response
  shapes, error codes). Server actions count as API surface.
- **21 AI integration:** which features call an LLM, model choice per call,
  the 3-layer rule (directive/orchestration/execution) applied to each
  pipeline, cost ceilings, fallback behavior when the LLM fails.
- **37 Agentic workflows** (only if applicable): max 5 MVP workflows. Per
  workflow: name, trigger (manual/cron/webhook), inputs, outputs, failure
  modes, stored artifacts; a `docs/directives/<name>.md` SOP (goal, inputs,
  tools, outputs, edge cases); deterministic execution scripts; observability
  (what's logged, where, replay procedure); guardrails (rate limits, retries,
  cost controls, human-approval points).
- **38 Change management:** semver, migration policy, and the rule that
  post-PRD changes to auth/data/permissions require an ADR in
  `docs/decisions/` + explicit user approval.
- **35 AI builder instructions:** becomes the project's `CLAUDE.md` seed —
  stack conventions, forbidden patterns, doc-consultation rules.
