---
name: worktree-pr-flow
description: >-
  Standard workflow for ALL bug fixes and new features in a git repository: do the
  work in an isolated git worktree on a dedicated feature branch, ship it through a
  pull request gated by CI and an automated Claude bug-hunter review, and merge it
  correctly — never edit the default branch (main/master) directly. Use this
  proactively at the START of any code change — whenever the user asks to fix a bug,
  add or implement a feature, refactor, or make any non-trivial edit to a repo — even
  if they don't mention worktrees, branches, or PRs. The bug-hunter review is run by an
  internal Claude subagent in-session (no external API key). Also use it to bootstrap the
  build/test CI into a repo that doesn't have it yet.
---

# Worktree → PR workflow

This is the default way to make any code change. Two ideas drive it:

1. **Isolation via git worktrees.** A worktree is a second working directory backed by
   the same repo, checked out to its own branch. Each fix/feature gets its own worktree,
   so the main checkout stays untouched, multiple changes can proceed in parallel without
   stashing, and an experiment that goes wrong is thrown away by deleting a directory.
2. **Every change lands through a reviewed PR.** Humans and an automated bug-hunter get a
   chance to catch problems before they reach the default branch, and CI proves the build
   and tests pass. The default branch is never edited directly.

Follow the steps in order. They're cheap and they compound: the discipline is what keeps
the default branch always-green and every change traceable.

## Step 0 — Preflight

Before touching code:

- Confirm you're in a git repo and identify the **default branch**:
  `gh repo view --json defaultBranchRef -q .defaultBranchRef.name` (fallback: the branch
  `origin/HEAD` points to, usually `main` or `master`).
- Make sure `gh` is authenticated (`gh auth status`) and the remote exists (`git remote -v`).
  If there's no GitHub remote, ask the user how they want to host/review (you can still use
  worktrees + branches locally and open the PR once a remote exists).
- **Never commit to the default branch.** If `git branch --show-current` is the default
  branch and there are uncommitted changes meant for a feature, move them to a feature
  branch (see Step 1) before committing.

## Step 1 — Create the worktree + branch

Pick a branch name by intent: `fix/<short-slug>` for bug fixes, `feat/<short-slug>` for
features, `chore/<short-slug>` / `ci/<short-slug>` / `docs/<short-slug>` otherwise.

Create the worktree as a **sibling directory** of the repo (so it doesn't nest inside the
working copy), branched from the up-to-date default branch:

```bash
git fetch origin
git worktree add -b fix/<slug> "../<repo-name>--fix-<slug>" origin/<default-branch>
cd "../<repo-name>--fix-<slug>"
```

If the agent harness supports it, prefer spawning the task in a worktree directly (e.g. an
agent `isolation: "worktree"` option) — same effect, less manual bookkeeping.

Do all subsequent work from inside the worktree directory.

## Step 2 — Do the work and verify it

Make the change. Then **build and run the tests before pushing** — a red PR wastes a CI
cycle and a reviewer's attention. Detect the project's commands rather than guessing:

- Look for the obvious signals: `Package.swift` / `*.xcodeproj` (Swift/Xcode),
  `package.json` (Node — check the `scripts`), `Cargo.toml` (Rust), `pyproject.toml` /
  `tox.ini` (Python), `Makefile`, `go.mod`, etc.
- Re-use whatever the repo's own CI runs (read `.github/workflows/`) so local and CI agree.
- If you genuinely can't find a test command, say so rather than claiming it passed.

Keep the change focused — one logical fix/feature per worktree/PR. If you discover an
unrelated issue, note it for a separate branch instead of widening the PR.

## Step 3 — Commit, push, open the PR

- Commit with a clear, scoped message (see Conventions). Commit only the files for this
  change; don't sweep in unrelated edits or local/machine files.
- Push the branch: `git push -u origin <branch>`.
- Open the PR against the default branch with a description that explains the *what* and
  *why*, how it was tested, and anything a reviewer should watch for:

```bash
gh pr create --base <default-branch> --head <branch> --title "<type>: <summary>" --body "<...>"
```

## Step 4 — Run CI, then review with an internal subagent; iterate

- CI (build + tests) runs automatically on the PR. Watch it:
  `gh pr checks <number> --watch` (or `gh run watch <run-id> --exit-status`).
- If CI fails, read the failing job log (`gh run view <run-id> --log-failed`), fix in the
  worktree, and push again — CI re-runs.
- **Review the PR with an internal bug-hunter subagent** — done inside your Claude Code
  session, so it needs no external Anthropic API key. Spawn a code-reviewer subagent (the
  Agent tool with a bug-hunter prompt, or the `/code-review` skill) scoped to the PR's diff
  (`gh pr diff <number>`), have it hunt for bugs the change introduces (crashes, threading,
  leaks, logic, coordinate/units, persistence/data-loss, regressions), and post its findings
  as a PR comment: `gh pr comment <number> --body "<report>"` (or inline review comments via
  `gh api repos/{owner}/{repo}/pulls/<number>/reviews`).
  - **Read the PR-branch version of files for context**, not the default branch. The main
    checkout is usually on the default branch, so point the reviewer at a worktree checked
    out to the PR branch, or use `git show <branch>:<path>`.
  - Address real findings with follow-up commits; briefly note anything you're intentionally
    leaving. Don't merge over unresolved high-severity findings.

If the repo has **no CI yet**, bootstrap it first (see "Bootstrapping CI").

## Step 5 — Merge correctly

- Merge only when **CI is green** and review is resolved. Prefer **squash merge** for a
  clean, linear history (one commit per PR on the default branch):
  `gh pr merge <number> --squash --delete-branch`.
- For substantive code changes, get the user's go-ahead before merging — don't self-merge
  feature/fix PRs unless they've said to. Infra/baseline PRs (CI config, dependency bumps)
  are fine to merge once green if the user asked you to set them up.
- Recommend (don't silently enable) **branch protection** requiring the build check, so the
  default branch can't be merged into while red. Offer the command; let the user apply it.

## Step 6 — Clean up the worktree

After the PR merges (or is abandoned):

```bash
cd <main-checkout>
git worktree remove "../<repo-name>--fix-<slug>"   # add --force if it has throwaway changes
git fetch --prune                                   # drop the deleted remote branch ref
```

`git worktree list` shows what's still around if you lose track.

## Bootstrapping CI (repos without it)

When a repo has no `.github/workflows`, add a build/test gate as its own `ci/...` PR before
feature work. `assets/ci.yml` is a template with per-stack examples (Swift/Xcode, Node,
Python, Rust) — fill in the repo's actual build+test commands and delete the rest.

Watch out for gotchas the first run exposes — e.g. an Xcode scheme must be **shared** (checked
into `xcshareddata/xcschemes/`) for CI to resolve `-scheme`, and deployment targets / toolchain
versions must be compatible with the runner image. Let the PR's own CI run validate the setup,
then fix what it surfaces.

The bug-hunter **review is run by an internal subagent** in your Claude Code session (Step 4),
not a hosted GitHub Action — so it needs no API-key secret and works in any repo immediately.
(If you ever want a fully-hosted review that runs without a session open, the opt-in option is
`anthropics/claude-code-action@v1` gated on an `ANTHROPIC_API_KEY` secret — but that's not the
default here.)

## Conventions

**Branch names:** `fix/`, `feat/`, `chore/`, `ci/`, `docs/`, `refactor/` + a short kebab slug.

**Commit / PR titles** — `<type>: <imperative summary>`, e.g. `fix: stop overlay drifting on drag`.

**Example — starting a bug fix:**
Input: "the dropdown closes when you click inside it"
Action: `git worktree add -b fix/dropdown-inside-click ../app--fix-dropdown origin/main`, fix
it there, run the tests, push, `gh pr create`, watch CI + review, then squash-merge on green.

## Guardrails

- Never edit, commit to, or push the default branch directly. All changes flow through a PR.
- One focused change per worktree/PR. Spin up a separate worktree for unrelated work.
- Verify build/tests locally before pushing; report failures honestly.
- Don't commit machine-local or secret files (e.g. `.claude/settings.local.json`, `.env`,
  signing material) — gitignore them.
- Clean up merged/abandoned worktrees so they don't accumulate.
