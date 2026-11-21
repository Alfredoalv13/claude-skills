---
name: seo-geo-blog-engine
description: "Use this skill to research keywords, write, optimize, and publish blog articles that rank on Google AND get cited by AI assistants (GEO, generative engine optimization). Covers keyword tiering by intent, a keyword brief, article structure with answer-first sections, FAQ and schema markup, a human approval gate, and a publish checklist. Trigger on 'SEO blog', 'keyword research', 'keyword brief', 'GEO', 'get cited by ChatGPT/Perplexity', 'write a blog article', 'refresh an old post', or 'optimize this draft'."
---

# SEO + GEO Blog Engine

A three-stage pipeline: **Research → Write → Publish**. Each stage hands a small, checkable artifact to the next. A human approves before anything goes live.

## Setup (once)
Create `blog-engine/brand.md` with: brand name, audience, product, tone, three topics you can speak about with real authority, and words to avoid. Read it before every run. If missing, ask for these five things and save them.

## Stage 1: Keyword research
1. Seed from real language: customer questions, support tickets, community threads, sales calls. People search with their pain, not your product category.
2. Expand each seed into 15-30 variants (questions, comparisons, "how to", "vs", "alternatives", "for <role>").
3. Classify each keyword:
   - **Intent:** informational, commercial, transactional, navigational
   - **Persona:** who is typing it
   - **Tier 1:** high-intent and winnable. **Tier 2:** useful supporting topics. **Tier 3:** long-tail or awareness.
4. Score priority = relevance to your product × intent strength × competition ease (1-5 each). Drop anything under a threshold you set.
5. Save to `blog-engine/keywords.csv` (keyword, intent, persona, tier, score, status).
6. For a chosen keyword, write a **keyword brief**: target keyword, secondary keywords, search intent in one sentence, the question to answer in the first 40 words, competitor gaps (what top results miss), and 5 FAQs.

## Stage 2: Write
Structure every article for readers first, then machines:
- **Answer-first opening:** a 40-60 word direct answer under the H1.
- Clear H2/H3 headings phrased as the questions people ask.
- Short paragraphs, concrete examples, real numbers. Cite sources you actually checked and name them in the text.
- A comparison table or step list where it fits. Models and snippets quote structured content.
- An FAQ section from the brief, each answer 40-80 words.
- One honest limitations or "when this is not for you" paragraph. It builds trust and reads as expertise.
- Meta title (under 60 chars), meta description (under 155), slug, and JSON-LD (`Article` plus `FAQPage`) in a code block.
- Internal links to 2-3 related posts, and one clear next step for the reader.

**Honesty gate (do not skip):** no invented statistics, quotes, case studies or customer names. Anything you cannot source gets removed or marked `[NEEDS SOURCE]`.

For other languages, write natively rather than translating word for word, and keep one canonical URL per language.

## Stage 3: Approve and publish
1. Save the draft as `blog-engine/drafts/<slug>.md` with status `Review`.
2. Show the user a checklist: keyword in title/H1/first paragraph, answer-first block, FAQ, schema valid, sources verified, links work, no placeholder text.
3. Only after explicit approval, publish through your own CMS or API and record the live URL and date in `keywords.csv`.
Never publish automatically. Keep API keys in environment variables, never in files.

## Refreshing old posts
Every quarter, check posts that dropped in rankings: update stale facts, add new FAQs from search queries, tighten the answer block, bump the modified date.

## Output of a run
Keyword brief, one reviewed draft, schema block, and a publish checklist the user can tick off.
