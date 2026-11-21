---
name: community-listening-engagement
description: "Use this skill to find real conversations on Reddit, LinkedIn, X and forums where you can genuinely help, understand audience sentiment and pain points, and draft value-first replies for a human to review and post. Trigger on 'community research', 'Reddit research', 'what are people saying about', 'pain points from', 'find posts I can answer', 'draft helpful replies', 'engagement queue', or 'social listening'."
---

# Community Listening + Value-First Engagement

Two jobs: **listen** (learn what people struggle with and how they say it) and **engage** (help in public, without pitching). Every reply is drafted for a human to review. Nothing is posted automatically.

## Setup (once)
Create `community/config.md`: your topic areas, 10-25 communities per platform, 20-40 pain-first search phrases written the way a frustrated person would write them ("drowning in client emails"), and the topics you are qualified to answer.

## Job 1: Listening sweep
1. For each community and phrase, collect recent posts the user provides or that public search surfaces (follow each site's terms; use official APIs where they exist, and never scrape behind a login).
2. Classify each post:
   - **Sentiment:** frustrated, curious, excited, skeptical
   - **Awareness:** unaware, problem-aware, solution-aware, product-aware
   - **Pain point** in one sentence and the **exact phrases** used
   - **Fit:** can we add real value here? (high/medium/low)
3. Write a digest: top pain points ranked by frequency, language patterns worth reusing, objections, and questions nobody answered well. Keep a link to every source thread.
4. Append insights to `community/insights.md` so findings accumulate over time.

## Job 2: Engagement queue
For posts with high fit and recent activity, draft a reply following these rules:
- Answer the actual question first with specific, usable advice.
- Write like a peer. No marketing language, no links, no pitch, no pretending to be a customer.
- Disclose affiliation if you mention anything you make.
- Match platform norms (Reddit: conversational and longer; LinkedIn: short and thoughtful; X: under 280 characters).
- One idea per reply. If you cannot add value, skip the post.

Write to `community/queue.csv`: platform, link, author handle, summary, awareness, draft, status (`Draft` → `Approved` → `Posted`), notes.

## Human gate
The user reads each draft, edits freely, and posts it themselves. Respect community rules, rate limits and anti-spam norms. Do not automate posting from accounts, run fake accounts, or coordinate upvotes.

## Output of a run
A sentiment digest, an updated insights file, and a queue of 5-15 reviewable drafts.
