# Delivery Workflow: Roadmap → Epics → Sprints → Tasks → PRs

Used in Phases 4–5. Combines the roadmap-planning methodology (deanpeters) with
planning-and-task-breakdown (addyosmani) and general engineering best practices.
Working files live in `planning/`; summary in foundation doc 42.

## 1. Roadmap (`planning/roadmap.md`)

A roadmap is a strategic communication tool — what we're building, why it
matters, how it ladders to business outcomes — not a Gantt chart.

Structure it as **Now / Next / Later**:
- **Now** — current sprint-level certainty, tied to a measurable outcome
- **Next** — committed direction, sequence may shift
- **Later** — believed direction, explicitly not committed

Each roadmap item states: the outcome (metric from doc 29 it moves), the Value
Equation lever it serves (from doc 40), and the epic(s) that deliver it.
Prioritize with a lightweight score: (impact on outcome × confidence) / effort.
Kill or defer anything that serves no stated outcome — that's how
feature-factory roadmaps happen.

## 2. Epics (`planning/epics/epic-NN-<name>.md`)

An epic is a coherent unit of user value, typically 1–3 sprints. Template:

```markdown
# Epic NN — <Name>
**Outcome:** <metric / user capability this unlocks>
**Roadmap item:** <link>  **Foundation docs:** <e.g. 14, 15, 17>
**In scope:** ...
**Out of scope:** ...   ← as important as in-scope
**Definition of done:** <observable, testable statements>
**Risks / unknowns:** ...
**Task list:** (filled at sprint planning)
```

Epic sequencing rules:
- Walking skeleton first: the thinnest end-to-end slice (auth → core action →
  persisted result) before widening any layer.
- Dependencies flow from the data layer up. Schema/RLS epics precede the UI
  epics that consume them.
- The MVP epic set = the shortest path to the dream outcome (doc 40). Anything
  not on that path is Next/Later.

## 3. Sprints (`planning/sprints/sprint-NN.md`)

1–2 week timeboxes with a named goal ("a user can sign up and create their
first project"), not a bag of tasks. Template: goal, epic(s) served, task
table, carry-over section, and an end-of-sprint review (what shipped, what
moved on metrics, what enters the backlog).

## 4. Task breakdown

Good task breakdown is the difference between an agent that completes work
reliably and one that produces a tangled mess. Every task must be:

- **Small**: implementable + testable + verifiable in one focused session
- **Explicit**: has acceptance criteria written BEFORE implementation
- **Independent-ish**: minimal cross-task coupling; dependencies declared
- **Verifiable**: states HOW to verify (test to run, flow to exercise)

Task table format (in the sprint file):

| ID | Task | Epic | Acceptance criteria | Depends on | Status |
|---|---|---|---|---|---|
| S02-T01 | Create `projects` table + RLS policies | E01 | Migration applies cleanly; owner can CRUD own rows; member read-only; anon blocked (tested via SQL) | — | todo |

Breakdown procedure for an epic:
1. Re-read the epic's foundation docs (data model, API contract, flows).
2. List the vertical slice steps end-to-end.
3. Split any step estimated over one session; merge trivial ones.
4. Write acceptance criteria per task; unclear criteria = the task isn't
   understood yet — resolve before the sprint starts, not during.
5. Order by dependency; flag tasks that can run in parallel (worktrees/agents).

Don't over-plan: only the current sprint gets task-level detail. Epics further
out stay at epic granularity — plans decay.

## 5. Git, branches & PRs

- Default branch is protected in practice: no direct commits to `main` — all
  changes through PRs, even solo. Use the worktree-pr-flow skill when
  available.
- Branch names: `feat/S02-T01-projects-table`, `fix/<issue>-<slug>`,
  `chore/<slug>`.
- Conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`, `docs:`,
  `test:`.
- One task (or one bug) per PR. If a PR grows past ~400 changed lines,
  split it.

PR template (`.github/pull_request_template.md`):

```markdown
## What & why
<link task ID / bug ID>
## How verified
<commands run, flows exercised, screenshots>
## Checklist
- [ ] Acceptance criteria met (quote them)
- [ ] No secrets/keys in diff
- [ ] RLS/authz unchanged, or doc 15 updated + ADR written
- [ ] Migrations are backward-compatible or gated
- [ ] Docs updated if behavior changed
```

Review gate (self-review or agent review before merge): correctness against
acceptance criteria, security (authz, injection, secrets), and simplification.
CI must pass: typecheck, lint, tests, build.

## 6. Bug workflow

Intake → triage → fix. No drive-by fixes: a bug found mid-task gets logged,
not silently fixed in an unrelated PR.

1. **Intake**: log in the tracker (GitHub Issues by default) with: observed vs
   expected behavior, reproduction steps, environment, severity.
   Severity: S1 data loss/security/down · S2 core flow broken · S3 degraded ·
   S4 cosmetic.
2. **Triage**: S1 interrupts the sprint immediately; S2 enters the current
   sprint if capacity allows; S3/S4 go to backlog and get batched.
3. **Fix loop**: reproduce first (a failing test where feasible) → fix →
   verify the repro passes → PR referencing the issue → merge closes it.
4. **Regression rule**: every S1/S2 fix leaves behind an automated test.

## 7. Feature-request workflow

New ideas mid-build never jump straight to code. They enter `planning/`
backlog → scored against the roadmap outcome + Value Equation → become an epic
or task at the next sprint boundary. If the user insists something is urgent,
it swaps against current sprint scope explicitly (name what gets bumped).

## 8. Definition of Done (project-wide)

A task is done when: acceptance criteria verified · tests pass · merged to
main via PR · deployed to preview/staging without errors · docs/foundation
updated when behavior or schema changed. A sprint is done when its goal is
demonstrable end-to-end, not when its tasks are merely merged.
