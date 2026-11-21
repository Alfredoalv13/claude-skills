# Open Source Claude Skills

A small, curated set of battle-tested [Claude Code](https://claude.com/claude-code) skills, scrubbed of any personal or business information.

## Skills

| Skill | Category | What it does |
|---|---|---|
| [worktree-pr-flow](open-source-skills/dev-workflow/worktree-pr-flow) | dev-workflow | Ship every bug fix or feature through an isolated git worktree, a CI-gated pull request and an automated AI review, then merge and clean up. |
| [agent-diamond](open-source-skills/planning/agent-diamond) | planning | Design multi-agent workflows with the diamond pattern: parallel researchers, independent skeptics, then a human approval gate. |
| [project-kickstart](open-source-skills/planning/project-kickstart) | planning | A 7-phase, gated planning pipeline from raw idea to launch: offer and market, PRD, foundation docs, roadmap, epics, sprints, PR workflow, launch. |
| [app-idea-to-prd](open-source-skills/planning/app-idea-to-prd) | planning | Turn a rough idea (even a voice-note transcript) into a PRD with quick, honestly-sourced market research and a build/park/skip verdict. |
| [app-store-assets](open-source-skills/publishing/app-store-assets) | publishing | Create, review and validate Apple App Store assets (icon, screenshots, previews, copy) against Apple's rules to avoid rejection. |
| [hormozi-content-framework](open-source-skills/marketing/hormozi-content-framework) | marketing | A value-first content checklist and rules inspired by Alex Hormozi's $100M Offers and $100M Leads, paraphrased, not a substitute for the books. |
| [seo-geo-blog-engine](open-source-skills/marketing/seo-geo-blog-engine) | marketing | Research keywords, write answer-first articles with FAQ and schema, publish only after approval. Built for Google and AI-citation traffic. |
| [content-autoresearch](open-source-skills/marketing/content-autoresearch) | marketing | A measured experiment loop for social content: change one variable, measure lift, keep only what clearly works. |
| [community-listening-engagement](open-source-skills/marketing/community-listening-engagement) | marketing | Find audience pain points on Reddit, LinkedIn and X and draft value-first replies for you to post. |
| [lead-research-outreach](open-source-skills/sales/lead-research-outreach) | sales | Prospect dossiers and a value-first email sequence, drafted for your review. |

## Categories
`dev-workflow` · `planning` · `publishing` · `marketing` · `sales`

## Install
Copy a skill folder into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/` (one project):

```bash
cp -R open-source-skills/planning/project-kickstart ~/.claude/skills/
```

## Contributing
PRs welcome. Keep skills generic: no secrets, no personal or company names, placeholders like `{brand}` for anything user-specific.

## License
MIT, see [LICENSE](LICENSE). Chosen because it is short, permissive and the norm for skill and tooling repos. Apache-2.0 would add an explicit patent grant; unnecessary here.
