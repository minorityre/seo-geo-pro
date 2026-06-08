# SEO/GEO Pro: Codex Skill for Search and AI Visibility

[![CI](https://github.com/minorityre/seo-geo-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/minorityre/seo-geo-pro/actions/workflows/ci.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-0099ff)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![tests](https://img.shields.io/badge/tests-15%20passing-brightgreen)](tests/)
[![SEO/GEO](https://img.shields.io/badge/SEO%2FGEO-Pro-14B8A6)](references/task-playbooks.md)
[![AI Search](https://img.shields.io/badge/AI%20Search-ready-7C3AED)](references/source-of-truth.md)

```text
  ███████╗███████╗ ██████╗      ██████╗ ███████╗ ██████╗      ██████╗ ██████╗  ██████╗
  ██╔════╝██╔════╝██╔═══██╗    ██╔════╝ ██╔════╝██╔═══██╗    ██╔══██╗██╔══██╗██╔═══██╗
  ███████╗█████╗  ██║   ██║    ██║  ███╗█████╗  ██║   ██║    ██████╔╝██████╔╝██║   ██║
  ╚════██║██╔══╝  ██║   ██║    ██║   ██║██╔══╝  ██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║
  ███████║███████╗╚██████╔╝    ╚██████╔╝███████╗╚██████╔╝    ██║     ██║  ██║╚██████╔╝
  ╚══════╝╚══════╝ ╚═════╝      ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝

              The evidence-first SEO/GEO layer for Codex agents
```

**SEO/GEO Pro is a senior, evidence-first SEO and generative search visibility skill for [OpenAI Codex](https://openai.com/codex/).** It helps Codex audit websites, plan content, diagnose technical SEO issues, improve AI-search citability, build structured data recommendations, and keep public copy clean before publishing.

It is built for operators who want the judgment of a senior SEO strategist inside an agent workflow: official-source discipline, clear evidence labels, business prioritization, migration awareness, public-copy QA, and small executable helpers for safer URL inspection.

## Table of Contents

- [Who This Is For](#who-this-is-for)
- [Why SEO/GEO Pro](#why-seogeo-pro)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Prompt Commands](#prompt-commands)
- [Features](#features)
- [Compared to Manual / Agency / Commercial Tools](#compared-to-manual--agency--commercial-tools)
- [Use Cases](#use-cases)
- [Sample Output](#sample-output)
- [Architecture](#architecture)
- [Methodology](#methodology)
- [Requirements](#requirements)
- [Helper Scripts](#helper-scripts)
- [Limitations](#limitations)
- [Documentation](#documentation)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Who This Is For

**SEO consultants and agencies.** Use Codex as a senior second brain for audits, briefs, migration QA, content plans and client-ready prioritization without shipping generic checklists.

**Founders and builders.** If you are shipping SaaS, ecommerce, marketplaces, directories or local-service sites, SEO/GEO Pro helps turn product context into organic growth work that engineers and writers can actually implement.

**In-house SEO and growth teams.** Use it before releases, migrations, content refreshes and reporting cycles to catch indexation risk, weak evidence, schema mismatch, AI-search gaps and public-copy leakage.

**Technical operators.** The skill is useful when SEO decisions touch rendered HTML, canonicals, robots, structured data, crawl paths, JavaScript rendering, Core Web Vitals, URL mapping or production QA.

## Why SEO/GEO Pro

- **Built for Codex.** This is not a Claude Code port with changed wording. It is packaged as a Codex skill with a direct `SKILL.md`, references, agent metadata and local helper scripts.
- **Evidence-first recommendations.** Findings are labeled as `Confirmed`, `Probable`, `Hypothesis`, `Experimental` or `Missing data`, so the reader knows what is proven and what still needs validation.
- **SEO and GEO together.** AI Overviews, AI Mode, Copilot and ChatGPT Search are treated as search surfaces built on discoverability, clarity, trust, citations, entities and technical accessibility, not as a magic replacement for SEO.
- **Falsifiable, not promotional.** Important recommendations should include the observation, dependency, failure check, leading indicator and business metric.
- **Public-copy safety.** Internal SEO language such as "ownership", "cannibalization", "quick win", "thin content" and "money page" should stay in private plans, not leak into landing pages.
- **Operator-friendly outputs.** The templates are written for action: affected URLs, evidence, priority, owner, dependencies, implementation risk and validation.
- **Lightweight execution.** The helper scripts cover safe URL checks, HTML fetches, SEO parsing, optional rendering and public-copy scanning without turning the skill into a heavy crawler.

## Installation

### Recommended: Skills CLI

The `npx skills add` CLI scans this repository and installs the `seo-geo-pro` skill directly.

```bash
npx skills add https://github.com/minorityre/seo-geo-pro --skill seo-geo-pro
```

To install it globally for your user-level Codex skills:

```bash
npx skills add https://github.com/minorityre/seo-geo-pro --skill seo-geo-pro --global
```

To list the available skills in the repo before installing:

```bash
npx skills add https://github.com/minorityre/seo-geo-pro --list
```

### Manual Install

Use this only if you prefer not to use the skills CLI. Clone the repository and copy it into your Codex skills directory.

Windows PowerShell:

```powershell
git clone https://github.com/minorityre/seo-geo-pro.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\seo-geo-pro" | Out-Null
Copy-Item -Recurse -Force .\seo-geo-pro\* "$env:USERPROFILE\.codex\skills\seo-geo-pro\"
```

macOS / Linux:

```bash
git clone https://github.com/minorityre/seo-geo-pro.git
mkdir -p ~/.codex/skills/seo-geo-pro
cp -R seo-geo-pro/* ~/.codex/skills/seo-geo-pro/
```

Restart Codex after installing or updating the skill.

### Optional Script Dependencies

The skill works as instructions without dependencies. The helper scripts need Python 3.10+.

```bash
pip install -r requirements.txt
```

For JavaScript rendering:

```bash
playwright install chromium
```

## Quick Start

Use natural language in Codex:

```text
Audit https://example.com for technical SEO and GEO. Prioritize only issues with evidence.
```

```text
Create an SEO/GEO brief for a SaaS comparison page targeting "best CRM for agencies".
```

```text
Optimize this landing page title, H1, intro, internal links and AI-search answer blocks.
```

```text
Diagnose why organic traffic dropped after the migration. Separate confirmed evidence from hypotheses.
```

```text
Review this public copy before publishing and remove internal SEO language.
```

## Prompt Commands

SEO/GEO Pro does not require slash commands. These prompt patterns work well:

| Prompt | What It Produces |
|---|---|
| `Run a complete SEO/GEO audit for <domain>` | Executive summary, source limitations, technical/content/authority/GEO findings and roadmap. |
| `Create an SEO brief for <topic>` | Intent, SERP angle, structure, entities, links, schema, media and QA. |
| `Optimize <URL> for search and AI answers` | Before/after title, description, H1, intro, FAQs, links, schema and citable blocks. |
| `Plan a migration from <old site> to <new site>` | Baseline, URL mapping, pre-launch, launch, post-launch and rollback checks. |
| `Diagnose this traffic drop` | Segmentation, confirmed causes, probable causes, hypotheses and validation. |
| `Check this page before publishing` | Rendered SEO QA and public-copy leakage checks. |

## Features

### Technical SEO

- Crawlability and indexability reasoning.
- robots.txt, meta robots and X-Robots-Tag checks.
- Canonicals, redirects, soft 404s and status-code diagnosis.
- Sitemap and URL inventory guidance.
- JavaScript rendering and initial HTML vs rendered DOM review.
- Hreflang, international SEO and migration QA.
- Core Web Vitals framing: LCP, INP and CLS.

### Content Strategy

- Keyword and entity research from business value and intent, not volume alone.
- SEO/GEO briefs for editorial, SaaS, ecommerce, local, comparison and support pages.
- Topical maps, hubs, clusters and internal linking plans.
- Content refresh, consolidation and cannibalization workflows.
- Differentiation requirements: proof, examples, data, cases, expert judgment and limitations.

### GEO / AI Search Visibility

- AI-search readiness grounded in SEO fundamentals.
- Citable answer blocks, definitions, structured headings and entity consistency.
- Guidance for AI Overviews, AI Mode, Copilot and ChatGPT Search.
- Clear crawler-control distinctions: search bots, training bots and user-initiated agents.
- Measurement ideas: AI referrals, cited pages, grounding queries, logs, brand mentions and assisted conversions.

### Structured Data

- Organization, LocalBusiness, Person, Article, Product, Offer, Review, BreadcrumbList, WebSite, Event, Course, JobPosting, SoftwareApplication, VideoObject and ImageObject guidance.
- Visible-content alignment.
- Risk warnings for fake authors, fake ratings, fake prices, expired jobs, non-visible FAQs and unsupported claims.

### Public Copy QA

- Private SEO reasoning stays private.
- Public pages should sound like commercial/editorial copy, not a consultant audit.
- The copy guard catches internal terms before they ship.

## Compared to Manual / Agency / Commercial Tools

| | Manual Audit | Agency Engagement | Commercial SEO Tool | SEO/GEO Pro |
|---|---|---|---|---|
| Speed | Slow but nuanced | Slowest | Fast crawl/report | Fast agent-assisted reasoning |
| Judgment | Depends on analyst | Depends on team | Rule-based | Senior protocol + evidence labels |
| Data ownership | Local | Often external | Vendor platform | Local by default |
| GEO awareness | Varies | Varies | Often lagging | Built into workflow |
| Falsifiability | Rare | Rare | Usually absent | Expected for key recommendations |
| Public-copy QA | Manual | Manual | Usually absent | Built in |
| Best use | Deep expert review | Full service | Large-scale crawling/data | Agent-led strategy, QA and implementation planning |

SEO/GEO Pro does **not** replace Screaming Frog, Ahrefs, Semrush, Sistrix, Search Console or Bing Webmaster Tools. It helps Codex interpret evidence, prioritize action and produce implementation-ready outputs.

## Use Cases

**SaaS launch.** Build use-case, alternative, comparison and integration pages without inventing competitor claims or publishing generic copy.

**Shopify/ecommerce growth.** Plan category pages, product schema, internal links, faceted navigation rules, product copy improvements and Merchant Center-aware content.

**Local-service SEO.** Review service-area pages, NAP, local proof, Google Business Profile alignment, LocalBusiness schema and doorway-page risk.

**Migration QA.** Build URL inventories, redirect maps, pre-launch checks, launch smoke tests, post-launch monitoring and rollback criteria.

**AI-search visibility.** Improve entity clarity, self-contained answers, citations, sources, author trust and technical accessibility without selling unverified GEO hacks.

**Publishing workflow.** Scan public content before release so internal strategy terms do not leak into landing pages.

## Sample Output

```markdown
## Technical Diagnosis

| Priority | Area | Evidence | Evidence Label | Affected URLs | Action | Impact | Effort | Risk | Validation |
|---|---|---|---|---|---|---|---|---|---|
| P0 | Indexability | Rendered page includes noindex | Confirmed | /pricing | Remove accidental noindex before launch | High | Low | Medium | Re-fetch rendered HTML and inspect robots directives |

## GEO / AI Search

| Priority | Area | Evidence | Evidence Label | Action | Metric |
|---|---|---|---|---|---|
| P1 | Citability | Key service page has no direct definition or source-backed answer block | Confirmed | Add concise definition, proof and FAQ block | AI referrals, cited page tracking, branded search |

## Roadmap

| Priority | Action | Owner | Dependencies | Time | Leading Indicator | Business Metric |
|---|---|---|---|---|---|---|
| P0 | Fix noindex and validate canonical | Developer | Deploy access | Same day | URL appears as indexable in inspection | Organic landing-page eligibility |
```

## Architecture

```text
seo-geo-pro/
  SKILL.md
  references/
    source-of-truth.md
    task-playbooks.md
    output-templates.md
    qa-gates.md
  scripts/
    seo_url_safety.py
    seo_fetch.py
    seo_parse_html.py
    seo_render_page.py
    seo_public_copy_guard.py
  tests/
  agents/
    openai.yaml
```

The main skill stays compact enough for Codex to load quickly. Deep guidance lives in references and is loaded only when the task needs it.

## Methodology

SEO/GEO Pro follows seven phases:

1. **Understand** the business, audience, page type and goal.
2. **Classify** the task and website type.
3. **Gather evidence** from URLs, rendered HTML, SERPs, tools, analytics or provided exports.
4. **Diagnose** confirmed issues, probable issues, hypotheses, opportunities and risks.
5. **Prioritize** by impact, effort, risk, dependencies and owner.
6. **Deliver** actions with evidence, implementation details, validation and metric.
7. **QA** public copy, schema, rendered SEO and anti-hallucination risks before closing.

Evidence labels:

| Label | Meaning |
|---|---|
| Confirmed | Proved by inspected source, crawl, rendered page, log, official documentation or first-party tool output. |
| Probable | Strongly supported, but not fully proven. |
| Hypothesis | Plausible and worth testing, but needs validation. |
| Experimental | Useful only as a controlled test, not a guaranteed result. |
| Missing data | Required data was not available. |

## Requirements

- Codex with local skill support.
- Python 3.10+ for helper scripts.
- Optional Playwright Chromium for rendered checks.

## Helper Scripts

### Safe URL Validation

```bash
python scripts/seo_url_safety.py https://example.com --strict --json
```

### Fetch HTML Safely

```bash
python scripts/seo_fetch.py https://example.com --json
python scripts/seo_fetch.py https://example.com --output page.html
```

### Parse SEO Elements

```bash
python scripts/seo_parse_html.py page.html --base-url https://example.com --json
```

Extracts title, description, robots, canonical, H1/H2/H3, hreflang, Open Graph, Twitter metadata, JSON-LD, images, links and word count.

### Render JavaScript Pages

```bash
python scripts/seo_render_page.py https://example.com --mode auto --json
python scripts/seo_render_page.py https://example.com --mode always --output rendered.html
```

Modes:

- `auto`: fetch raw HTML first and render only if it looks like an SPA shell.
- `always`: force Playwright rendering.
- `never`: raw HTML only.

### Public Copy Guard

```bash
python scripts/seo_public_copy_guard.py ./src ./content
```

The guard flags internal SEO language such as `SEO ownership`, `cannibalization`, `generic landing`, `SEO hypothesis`, `quick win`, `thin content`, `money page`, `SERP ownership` and `crawl budget`.

## Limitations

- SEO/GEO Pro is not a crawler replacement. Use dedicated crawlers for large URL inventories.
- It does not include proprietary keyword, backlink or traffic data. Bring your own exports from GSC, Bing, Ahrefs, Semrush, Sistrix or analytics.
- It does not guarantee rankings, traffic or AI citations.
- Script output is scoped. A single URL parse does not prove site-wide indexation or performance.
- The skill avoids unverified GEO claims. If official guidance changes, update `references/source-of-truth.md`.

## Documentation

- [Main skill](SKILL.md)
- [Source of truth](references/source-of-truth.md)
- [Task playbooks](references/task-playbooks.md)
- [Output templates](references/output-templates.md)
- [QA gates](references/qa-gates.md)
- [Tests](tests/)

## FAQ

### Is SEO/GEO Pro only for Codex?

It is written for Codex first. The Markdown instructions can be adapted elsewhere, but the packaging and examples assume Codex skills.

### Does this optimize for AI Overviews and ChatGPT Search?

Yes, but through evidence-first SEO fundamentals: discoverability, indexability, clear entities, visible HTML, useful structure, trust, sources and citable passages.

### Does it recommend `llms.txt`?

It can mention `llms.txt` as low-cost optionality, especially for developer documentation, but it should not be sold as a guaranteed citation lever.

### Can it run a complete site crawl?

Not by itself. It includes small helpers for safe URL fetches, parsing and rendering. For full crawling, use a dedicated crawler and give Codex the export.

### Is it safe to use on private projects?

The scripts include SSRF-oriented URL validation, but you still control what data you pass to Codex and what you commit. Do not publish private exports, credentials or customer data.

## Contributing

Contributions are welcome. Keep the project practical:

- Prefer official sources and direct evidence.
- Avoid SEO myths and unverified GEO hacks.
- Keep public-copy QA strict.
- Add tests for scripts when behavior changes.
- Do not commit credentials, private exports or customer data.

Run before opening a PR:

```bash
python -m pytest -q
```

## Author

Built by **[Armand Mainou](https://github.com/minorityre)**, founder/operator behind **[PIXELWOLF](https://pixelwolf.es/)** and **[Beetter](https://www.beetter.co/)**.

Armand builds and scales ecommerce systems, automation workflows, SaaS products and organic-growth infrastructure from Barcelona. This skill packages the kind of practical SEO/GEO operating system used when technical execution, content quality, search visibility and business outcomes need to live in the same workflow.

Links:

- [GitHub: minorityre](https://github.com/minorityre)
- [PIXELWOLF](https://pixelwolf.es/)
- [Beetter](https://www.beetter.co/)
- [LinkedIn](https://es.linkedin.com/in/armand-mainou-gobierno)

## License

MIT License. See [LICENSE](LICENSE) for details.
