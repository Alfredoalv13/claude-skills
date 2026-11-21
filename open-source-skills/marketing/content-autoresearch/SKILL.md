---
name: content-autoresearch
description: "Use this skill to run a disciplined experiment loop on social content (X, LinkedIn, newsletters): measure a baseline, change ONE variable at a time, publish variants, measure, and keep only changes that clear a hard lift threshold, then record what you learned. Trigger on 'autoresearch', 'content experiment', 'A/B test my posts', 'what content works', 'baseline my account', 'propose the next variant', 'close the experiment', or 'content learning log'."
---

# Content Autoresearch Loop

Inspired by the autoresearch idea of automated, measured iteration. Instead of guessing what works, run short experiments that change one thing at a time and keep only what is clearly better.

## Files (create in `autoresearch/`)
- `baseline.md`: current performance per platform
- `experiments.csv`: id, platform, variable, control, variant, start, end, n_control, n_variant, metric, lift, decision
- `learnings.md`: the running wiki of what worked and what did not

## Phase 1: Baseline
Export the last 30 days of posts for one platform (the user pastes or provides analytics). Compute the median and mean of the chosen **primary metric** (pick one: engagement rate, replies, saves, clicks). Record the top and bottom quartile and what they have in common. Write to `baseline.md`.

## Phase 2: Propose one variant
Pick **one variable** only: hook style, length, format (text/image/carousel), posting time, call to action, topic angle. Write a hypothesis: "Changing X from A to B will raise <metric> because <reason>." Draft the variant posts and tag each with the experiment id. Everything else stays the same.

## Phase 3: Run
Publish control and variant posts across a fixed window (default 14 days) with comparable topics and times. Do not edit the plan mid-run. Publishing is done by the user or their scheduler. This skill never posts by itself.

## Phase 4: Measure
At window end, collect metrics per post. Compute lift = variant median ÷ control median.

## Phase 5: Close with a hard rule
Accept the variant only if **lift ≥ 1.30× AND each arm has at least 15 posts** (adjust the numbers once, in writing, before you start). Otherwise reject or extend once. Record the decision in `experiments.csv` and write one paragraph to `learnings.md`: what changed, the number, the likely reason, and the next question.

## Honesty gate
- Never cherry-pick posts or move the window after seeing results.
- Small samples are noise. Say "inconclusive" when it is.
- Do not fabricate metrics. If data is missing, mark it missing.
- Lift on one account is evidence, not proof. Say so in the learnings.

## Output of a run
Updated baseline, one experiment proposal or closeout, and a learnings entry.
