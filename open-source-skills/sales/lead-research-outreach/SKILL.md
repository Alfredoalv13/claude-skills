---
name: lead-research-outreach
description: "Use this skill to turn a list of prospects into researched, personalized, value-first outreach: define your ideal customer, build a short business dossier for each lead from public information, map likely pain points, and draft a short email sequence for human review. Trigger on 'lead research', 'prospect dossier', 'personalized cold email', 'email sequence', 'outreach drafts', 'ICP', or 'research these leads'."
---

# Lead Research + Outreach Drafts

Goal: every recipient thinks "this person actually looked at my business and tried to help." Quality over volume. A human approves everything before it is sent.

## Setup (once)
Create `outreach/icp.md`: who you help (industry, size, role), the problem you solve, proof you can legitimately cite, your offer in one sentence, and the sender name and signature. If any is missing, ask.

## Step 1: Lead list
Work from a list the user provides (CSV or pasted), with at least name, role, company, website, and a work email that the user obtained lawfully. Remove duplicates and anyone already contacted. Do not guess or generate email addresses, and do not collect personal data beyond business context.

## Step 2: Dossier (per lead)
From the company website and public pages, capture in `outreach/dossiers/<company>.md`:
- What they do, who they serve, how they make money
- Recent changes (new product, hiring, announcement), with source link
- 1-3 likely pain points mapped from the ICP, each labelled **observed** (seen on their site) or **inferred**
- One specific, true observation worth mentioning
Mark anything unverified. Never invent facts.

## Step 3: Sequence draft (default 3-4 emails)
- **Email 1 (value first):** one specific observation, one useful idea or resource they can use without replying, a soft question. Under 100 words.
- **Email 2 (day 3):** a short additional insight tied to their situation.
- **Email 3 (day 6):** a brief, low-pressure close with an easy way to say no.
- Optional **Email 4:** a final useful note, no guilt.
Rules: subject lines under 7 words and honest, plain text, no fake "Re:" threads, no false urgency, no claims you cannot back up, and a working unsubscribe or opt-out line.

## Step 4: Human gate
Show the dossier and drafts side by side. The user edits and approves. Sending happens through the user's own email tool, in small daily batches (start with 20-30), with replies handled personally.

## Compliance reminders
Follow CAN-SPAM, GDPR, CASL and similar rules for your audience: honest sender identity, physical address where required, a working opt-out honored promptly, and a lawful basis for contacting people. Keep API keys in environment variables, never in files. This skill gives drafting help, not legal advice.

## Output of a run
Dossiers, sequence drafts, and a tracking sheet (lead, status, last touch, reply, next step).
