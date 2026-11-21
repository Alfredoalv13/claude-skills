---
name: app-idea-to-prd
description: Fast idea capture. Use whenever the user says they have a new app idea ("I have a new idea for an app", "app idea:", "new idea:", "what if there was an app that...", or dumps a rough concept, voice-note transcript, or one-liner). Turns it into a PRD with quick market research (competitors, pricing, gaps, verdict) and saves it as a markdown note in your ideas folder (Obsidian-friendly, works with any notes folder). NO code, no scaffolding. Built to work from a phone. For deeper planning of an idea the user has decided to build, hand off to project-kickstart.
---

# App Idea → PRD (+ quick market research) → Notes folder

Goal: the user drops a raw idea (often from their phone, often messy). You return a
researched, well-structured PRD saved in their notes folder, in a few minutes, with almost no
back-and-forth. **Never write code, scaffold a project, or create project folders.**

> **Setup:** set `IDEAS_DIR` below to the folder where your idea notes live
> (an Obsidian vault subfolder, a docs folder in a repo, anything). Optionally set
> `MOC_FILE` to an index note that should get a one-line link to each new idea.
> If you don't set them, ask the user once where to save, then remember the answer.

## Rules

1. **Don't interrogate.** The user is on a phone. Make reasonable assumptions, list them
   under "Assumptions & open questions" in the note, and proceed. Ask at most ONE
   question, and only if the idea is truly unintelligible.
2. **Keep their ideas.** Every feature or concept the user mentioned must appear in the
   PRD, tagged `(user)`. Features you add are tagged `(suggested)`. Never silently drop
   or rewrite their intent.
3. **Research is fast and honest.** Budget ~5-8 web searches (WebSearch, standard mode).
   Cite sources with URLs. If you couldn't verify something (pricing, download counts,
   market size), say "unverified" instead of inventing numbers. Never fabricate
   competitors.
4. **Honest verdict.** End with Build / Build-narrow / Park / Skip and a one-line why.
   A crowded market is a finding, not a failure; say what the wedge would be.
5. **Notes etiquette** (see below): flat folder, frontmatter, no topic subfolders.
6. **Don't touch other notes' bodies** except appending one line to the index note (`MOC_FILE`), if configured.

## Steps

1. **Parse the idea** into: one-sentence pitch, target user, problem, the user's own
   feature ideas (verbatim intent), platform guess (default: web or mobile, whichever fits the idea best).
2. **Check for duplicates:** search `IDEAS_DIR` (grep titles and bodies) for the
   same or a related idea. If one exists, tell the user and ask (once) whether to
   extend the existing note or create a new one. Default: create new and link with
   `[[wikilinks]]` under "Related ideas".
3. **Quick research** (parallel searches in one turn):
   - Direct competitors / alternatives (App Store, Product Hunt, web). Aim for 4-8.
   - For each: what it does, pricing, platform, one weakness or review complaint.
   - Demand signals: Reddit/forum complaints, search interest, category size if easy
     to find.
   - Monetization norms in the category (subscription / one-time / freemium, price
     points).
   - Mac App Store / iOS specifics if relevant (review/policy risks, e.g. needs a
     backend, user accounts, sandboxing).
4. **Write the note** using the template below. Filename: `NN Title.md` where NN is the
   next number after the highest in `IDEAS_DIR` (always check with
   `ls | sort -n | tail`; start at 01 if empty). Title is Title Case, descriptive, no
   punctuation that breaks filenames (no `: / \ ?`).
5. **Link it into the index (optional):** if `MOC_FILE` is set, append one line
   `- 💡 [[NN Title]]` under the matching domain heading (closest heading if none fits).
6. **Reply short** (phone-friendly, under ~120 words): pitch, verdict, top 3 competitors,
   the wedge, the note path, and the 1-3 biggest open questions. No walls of text.

## Notes location and conventions

- Save to `IDEAS_DIR` flat. Don't create subfolders there.
- If something is explicitly NOT an idea (e.g. an active multi-note build), ask or
  place it in your inbox folder.
- Prefer Obsidian-flavored markdown if the folder is a vault: YAML frontmatter,
  `[[wikilinks]]`, `> [!note]` callouts. Plain markdown is fine otherwise.
- Only edit inside the notes folder.

### Frontmatter (exact keys; keep keys stable so Obsidian Bases / Dataview can query them)

```yaml
---
type: app-idea
status: prd-draft          # idea | prd-draft | spec-drafted | building | shipped | parked
domain: <one of the existing domains>
created: YYYY-MM-DD
tags: [app-idea]
verdict: build | build-narrow | park | skip
platforms: [ios, macos, web]
---
```

`domain` examples (reuse existing values in your folder; invent a new kebab-case one only
if none fit): `personal-productivity`, `content-social-media`, `ai-agent-tools`,
`ecommerce`, `local-services`, `finance-ops`, `real-estate`, `games`, `design-assets`.

## PRD template (body of the note)

```markdown
# <Title>

> [!summary] One-liner
> <Pitch in one sentence.> **Verdict: <verdict>**, <one-line reason>.

## 1. Problem & opportunity
- Who has the problem, how painful, how they cope today.

## 2. Target users
- Primary persona (+ secondary if any). Who it is NOT for.

## 3. Core idea & value proposition
- What it does differently; the "wedge".

## 4. Features
| Feature | Source | Priority | Notes |
|---|---|---|---|
| ... | (user) / (suggested) | MVP / v2 / later | ... |

## 5. User flow (happy path)
1. ...

## 6. Quick market research
**Date researched:** YYYY-MM-DD · **Depth:** quick scan (not a full study)

| Competitor | What it does | Pricing | Platform | Gap / weakness | Source |
|---|---|---|---|---|---|

- **Demand signals:** ...
- **Monetization norms:** ...
- **Market notes / risks:** ...
- **Differentiation / wedge:** ...

## 7. Monetization hypothesis
- Model, price point guess, why.

## 8. MVP scope & success metric
- What ships first (max ~5 features). One metric that says it's working.

## 9. Technical notes (light, no code)
- Platform, likely stack, backend needed?, AI/API dependencies, App Store gotchas.

## 10. Risks
- Top 3, each with a mitigation.

## 11. Assumptions & open questions
- Things I assumed because the idea didn't say. Questions for the user.

## 12. Verdict & next step
- Build / Build-narrow / Park / Skip, why, and the single smallest next action.
  If Build: "Run project-kickstart on this note to plan it for real."

## Related ideas
- [[existing notes]]

## Sources
- [title](url)
```

## Handoff

If the user says "let's build it", invoke `project-kickstart` if installed (it plans epics, docs, and
offer design) and set the note's `status: building` plus a `related_build:` property
once a project folder exists. This skill itself never starts a build.
