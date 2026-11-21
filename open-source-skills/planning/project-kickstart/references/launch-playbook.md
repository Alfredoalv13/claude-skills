# Launch & Growth Playbook

Used in Phases 6–7. Combines the coreyhaines launch methodology, the ognjengt
Product Hunt playbook, $100M Leads channel strategy, and launch-asset
production. Output: `launch/launch-plan.md`, assets in `launch/assets/`,
summary in foundation doc 41.

Start launch prep while the build is still running — realistic lead time is
2–4 weeks. The offer doc (`launch/offer.md`) is the source of truth for
messaging; never write launch copy that contradicts it.

## 1. Launch mindset: launch repeatedly

The best companies don't launch once — they launch again and again. Plan a
**launch calendar**, not a launch day:
- **Tier 1** (2–4/yr): new product, major feature — full channel push, PH
  launch, video, email sequence
- **Tier 2** (monthly-ish): meaningful features — changelog post, social
  thread, email to users
- **Tier 3** (continuous): improvements — in-app changelog, build-in-public

Before writing any launch plan, check for existing marketing context
(`.agents/product-marketing.md`, `.claude/product-marketing.md`, or the
`launch/` folder) and reuse it rather than re-asking the user.

## 2. Channel plan ($100M Leads — the Core Four)

Advertising = letting the market know your stuff exists. Four ways, two axes
(people who know you vs strangers × 1-to-1 vs 1-to-many):

| Channel | What it looks like for a SaaS launch |
|---|---|
| Warm outreach (1:1, known) | Personal messages to network, waitlist, past clients — highest conversion, do FIRST; aim for the first 10 users by hand |
| Content (1:many, known→strangers) | Build-in-public posts, SEO/LLMSEO articles, the lead magnet, demo videos. Hook → Retain → Reward structure |
| Cold outreach (1:1, strangers) | Personalized DMs/emails to the named avatar (doc 40); lead with the lead magnet, not the pitch |
| Paid ads (1:many, strangers) | Only after organic proves the offer converts; ads amplify a working funnel, they don't fix a broken one |

Rules: pick ONE primary channel and saturate it before adding another ("rule
of 100": 100 reps/day of the primary action — outreach msgs, minutes of
content, ad spend units). The **lead magnet** defined in Phase 1 is the tip of
every channel: give away something an ideal customer would happily pay for,
that naturally reveals the paid product ("give until they ask").

## 3. Launch sequence (any Tier 1 launch)

**T-4 to T-2 weeks — Momentum build**
- Ship the lead magnet + public pages (pricing, docs 04/08 surfaces)
- Waitlist or early-access list; warm outreach begins
- Build-in-public teasers; line up testimonials/proof from beta users
  (proof feeds the Value Equation's "likelihood" lever)
- Produce launch assets (§5)

**T-1 week — Arm everything**
- Final QA on the golden path: signup → first value in <10 min
- Analytics events for the funnel (doc 29) verified end-to-end
- Draft all copy: announcement post, email sequence, social threads, PH
  listing. Every asset states dream outcome + risk reversal, not features
- Founding-member pricing window defined (ethical urgency)

**T-0 — Launch day** (see §4 if Product Hunt)
- Publish announcement; email the list; warm-outreach the superfans to
  engage early; respond to every comment/question same-day

**T+1 week — Convert & compound**
- Follow-up email to non-converters (address objections, restate guarantee)
- Publish "what we learned" / metrics post (content from the launch itself)
- Log every objection heard — feed doc 34 intake and next offer iteration

## 4. Product Hunt playbook (Tier 1, optional but recommended for consumer/prosumer SaaS)

Goal: #1 Product of the Day is a byproduct of preparation, not luck.
- **2+ weeks out**: polish PH-specific assets — tagline (≤60 chars, outcome
  not category), gallery (first image = the dream outcome), a 30–60s demo
  video; warm up your PH account and (optionally) recruit a hunter with
  relevant followers; build a supporter list — people who genuinely use PH
  (PH penalizes vote rings and fresh accounts).
- **Launch at 12:01 AM PT** to get the full 24 hours.
- **Maker comment** posted immediately: the story, who it's for, the founding
  offer for the PH community (a real exclusive — this is an attraction offer).
- **All day**: reply to every comment fast; push supporters in waves (morning /
  midday / evening), never all at once; share progress in communities where
  the avatar lives (no vote-begging language — PH penalizes it).
- **After**: thank-you update, convert PH signups with the follow-up sequence,
  add the badge to the site.

## 5. Launch assets checklist (`launch/assets/`)

- Announcement post (blog) — offer-led narrative, proof, guarantee, CTA
- Email sequence: tease → launch → social proof → objections → last-call
  (urgency window closes)
- Social threads per platform the avatar uses
- Demo/launch video — brief first: hook (dream outcome in 3s), problem,
  product in action, proof, offer + CTA. If the `product-launch-video` /
  `hyperframes` skills are installed, use them to produce it; otherwise
  write the brief + script for external production
- Screenshots/GIFs of the golden path
- PH kit (if applicable): tagline, description, gallery, maker comment,
  founding offer

## 6. Post-launch loop (Phase 7)

- **Weekly**: funnel metrics vs doc 29 KPIs; where's the biggest drop-off?
  Fix the funnel stage, not everything at once
- **Monthly**: Tier 2 launch of the best shipped improvement; re-run rule-of-100
  on the primary channel; review CAC vs 30-day gross profit (money model —
  if 30-day cash < CAC, fix the attraction offer/upsell before scaling spend)
- **Quarterly**: re-score the offer (0–10 scorecard); revisit market/channel
  choices; graduate a secondary channel only if the primary is saturated and
  systematized
- Every insight loops back into Phase 4 planning as backlog items — launch
  learnings are roadmap input, not trivia
