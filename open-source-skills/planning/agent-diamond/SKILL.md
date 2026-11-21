---
name: agent-diamond
description: Design and run diamond-pattern multi-agent workflows (parallel researchers + independent skeptics + human gate). Use when building agent graphs, parallel research desks, SEO content machines, go-to-market kits, Claude Code or Codex workflows, or optimizing AI systems by removing fake sequential edges. Triggers on agent graph, diamond pattern, multi-agent research, workflow graph, parallel agents, skeptic pass, human-in-the-loop approval for irreversible actions, verifier gate, node contracts, model tiering, graph-max, code mode script.
---

# Agent Diamond

## Overview

Apply the diamond pattern for multi-agent systems: fan-out independent jobs in parallel, run dedicated checkers/skeptics that never grade their own homework, merge survivors, and place a human gate only where mistakes are expensive to undo. Includes ready-to-paste Claude Code prompts for three high-ROI business graphs plus the core design rules.

## Core Concepts

### What a graph is
- A graph is a plan of jobs (nodes) and real dependencies (edges).
- An edge exists only when data actually moves across it. "And then" is not enough.
- Running notes travel with the work (findings, decisions, open items).
- Most "graphs" people draw are still single unbranching chains with fake edges. Cutting those is the first unlock.

### Node contracts
Every node needs a clear contract so it can be parallelized and wired safely:
- Bounded input (passed explicitly, never assumed from a shared context window)
- Bounded output (defined shape, preferably schema-validated)
- Exactly one job
Force structured returns and validate at the tool-call layer so mismatches retry instead of handing free text downstream.

### The diamond — the one topology you need
1. Split the question into independent angles / jobs.
2. Run workers side-by-side (parallel).
3. Hand every finding to a separate checker whose only job is to try to kill it.
4. Merge only the survivors into one ranked result.
5. Human sees the final merged output (or intermediate positioning) and gives the last yes.

Never let the same agent grade its own homework. Top models catch ≤21% of their own errors of the same kind.

### Verifiers on the edge (three useful patterns)
- **Adversarial**: independent skeptics prompted to refute each finding; keep only if majority survive.
- **Perspective-diverse**: give each verifier a distinct lens (correctness, currency, source realness, security, reproducibility).
- **Judge panel**: generate several attempts, score with parallel judges, synthesize from the winner while grafting the best of the runners-up.

### The stop rule
- Graphs buy breadth, not better judgment.
- Use multi-agent diamond only when work truly splits into pieces that never need each other's results.
- If every step needs the full picture, stay with one agent. Parallel teams win on independent work and lose on sequential work (same-budget tests show +80% vs –30–70%).

### Barriers vs pipelines
A barrier makes everything wait for the slowest node. Use only when a true cross-item dependency exists (e.g. global dedupe). Otherwise prefer pipelines so fast items finish early instead of idling.

### Failure containment
- A failing node should resolve to null (or drop out), not crash the whole batch.
- Design every fan-in to tolerate missing inputs.
- When nodes write in parallel, isolate them (own worktree / sandbox) then merge cleanly. Only add this seatbelt when parallel writes actually happen.

### Model tiering
Route repetitive or bounded fan-out nodes to cheaper/faster models. Keep the expensive model for judgment, synthesis, and final merge. By default subagents inherit the session model — change that on purpose or the invoice will surprise you.

### Cycles (unknown-size discovery)
Use a controlled cycle only when the job size is unknown until you are inside it (bug sweeps, open-ended discovery). Pattern: loop-until-dry. Keep spawning until consecutive rounds surface nothing new. Dedupe against *everything seen*, not just confirmed results, or rejected findings will reappear forever.

### The human gate + anchors
- Place approval exactly where a mistake is expensive to undo (send, publish, refund, invoice, launch).
- Not on every step and not on none.
- Some measurements must be unarguable anchors that touch reality: money that landed, tests that actually ran, customers who stayed.
- Some rules must be frozen (optimizers are never allowed to weaken them).
- The deepest judgment of what is worth controlling comes from outside the graph.

### Four safety rules
- Every loop gets a maximum number of rounds.
- Only one job writes to any one file.
- The routing lives in written steps; the AI fills the jobs.
- Always a hard cap on how many agents can spawn.

## When to trigger a diamond
Ask first: "Where does my work split?"
- Independent research angles, competitor + customer + channel profiling, top-pages + questions + gaps → diamond.
- Pure sequential reasoning, single long chain of dependent edits → one agent.

## Ready-to-use Claude Code prompts

Always start Claude Code in an empty (or dedicated) folder. Replace the bracketed placeholders. The keyword "workflow" tells Claude to coordinate a team instead of a single line.

### Graph 1 — Deep Research Desk
For any high-stakes decision (pricing, market entry, offer choice).

```
i need decision-grade research on: [your question]. use a workflow: split the question into 5 distinct angles, run one researcher per angle in parallel, every finding needs a source link and a date, then run a skeptic against each finding that tries to disprove it, drop what fails, merge the survivors into one report ranked by confidence, save it as research-report.md and show me the top findings
```

### Graph 2 — SEO Content Machine
Produces one ranking-ready draft that never publishes without you.

```
i want an article that can rank for: [topic]. use a workflow: run three research jobs in parallel, one lists what the current top-ranking pages cover, one collects the real questions people ask about this topic, one finds what the top pages skip, merge all three into an outline, write a full draft from the outline, then run a fact-checker that flags every claim without a source, save the draft to drafts/ with the flagged claims listed at the top, never publish anything
```

### Graph 3 — Go-to-Market Kit
Full launch kit with positioning as the shared foundation and human pause.

```
i'm launching [product] for [audience]. use a workflow: run three research jobs in parallel, one profiles the buyer and collects the exact words they use, one maps where these buyers spend time online, one collects how competitors pitch them, merge into a one-page positioning doc and pause to show it to me, then run three writers in parallel from that doc: landing page copy, a week of launch posts, a set of outreach messages, then run a checker that compares every asset against the positioning doc and flags anything off, save everything to launch-kit/ and change nothing after that without asking me
```

### Additional high-ROI shapes (adapt as needed)
- **Cited research report**: decompose → parallel searches → dedupe sources → adversarial verify every claim → write.
- **Security / code sweep**: one subagent per file or route hunting specific issues → verifier pass confirming findings.
- **Unknown-size discovery**: parallel finders → dedupe against everything seen → verify survivors → loop until dry.
- **Adversarial diff review**: route by size; small change = quick pass; large = parallel audits on distinct lenses + judge panel.

## Implementation path (once the graph is designed)
The hard part is the design. Wiring is now cheap.

1. Draw the graph (paper, Excalidraw, Mermaid, whiteboard — anything).
2. Hand the diagram + a short description to a strong coding agent (Claude Code, Codex, etc.).
3. Prompt it roughly: “Write a code-mode / workflow script that implements this graph. Run it with <inputs>.”
4. There is often no step 4 — modern coding agents can turn a clear diagram into a runnable orchestration script.

Prefer this over hand-coding the orchestration once the nodes, edges, and contracts are solid. More advanced shapes (planner + multi-reviewer + pass/fail feedback loops + plan reviewer) are valid after the basic diamond and real-edge discipline are in place.

## Design process (use every time)
1. Draw the current system as jobs + arrows.
2. Delete every fake edge (no real data dependency).
3. Identify natural split points → insert one diamond.
4. Give every node a contract (bounded in/out + one job).
5. Add dedicated checkers with distinct kill criteria (or one of the three verifier patterns).
6. Place the human gate + reality anchors only at irreversible points.
7. Route cheap models to fan-out, expensive to judgment.
8. Draw the final graph cleanly, then use the Implementation path above (or paste one of the ready prompts).
9. After first run, ask the coding agent to save the workflow so it becomes a one-command repeat.

## Playbook reminders
- Fake edges first — nothing new until the wasted waits are gone.
- Split only what never reads back.
- No finding travels unchecked; no two checkers ask the same question.
- Prefer pipelines over barriers unless there is a true cross-item dependency.
- One writer per file; plan in written steps.
- Contain failure at the node; tolerate missing inputs at fan-in.
- The last yes sits where a mistake would be expensive to undo.
- One tool is enough until you can name the reason it isn't.
- Keep the graph grounded: some numbers and rules must stay outside the optimizing loops.

## References
- See `references/one-pager.md` for the compact visual summary of the nine principles.
- Core practical prompts and cards originate from @EXM7777.
- Additional engineering depth (contracts, verifier patterns, barriers, model tiering, anchors, failure containment) drawn from the graph-engineering essay by @humzaakhalid.
- Implementation shortcut (draw the graph → hand to coding agent) from @alex_frantic (OpenAI Harness Engineering).

When the user asks to design a new graph, adapt the diamond shape, keep the skeptic/verifier separate, enforce the stop rule and node contracts, and always end with an explicit human gate + reality anchors for anything that ships. Once the design is solid, use the Implementation path to turn the diagram into a runnable script.
