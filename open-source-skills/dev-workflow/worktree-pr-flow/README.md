# worktree-pr-flow

Ship every bug fix or feature through an isolated git worktree, a CI-gated pull request and an automated AI review, then merge and clean up.

**Use it when:** Any time you ask Claude to change code in a git repo.

**Notes:** Bootstraps a CI workflow (`assets/ci.yml`) into repos that lack one.

## Install

```bash
cp -R worktree-pr-flow ~/.claude/skills/
```

Restart Claude Code; the skill triggers from its `description`. License: MIT (see repo root).
