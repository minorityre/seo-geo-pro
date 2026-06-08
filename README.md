# SEO/GEO Pro

[![CI](https://github.com/minorityre/seo-geo-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/minorityre/seo-geo-pro/actions/workflows/ci.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-0099ff)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![tests](https://img.shields.io/badge/tests-15%20passing-brightgreen)](tests/)
[![SEO/GEO](https://img.shields.io/badge/SEO%2FGEO-Pro-14B8A6)](references/task-playbooks.md)
[![AI Search](https://img.shields.io/badge/AI%20Search-ready-7C3AED)](references/source-of-truth.md)

Senior SEO and GEO skill for Codex.

SEO/GEO Pro is an evidence-first operating system for technical SEO, content strategy, on-page optimization, structured data, E-E-A-T, migrations, local SEO, ecommerce SEO, SaaS SEO and AI search visibility.

It is designed for agents that need senior SEO judgment without turning every task into a generic checklist. It separates internal SEO reasoning from public copy, labels evidence clearly, avoids unverified GEO hacks and includes small helper scripts for safer audits.

## What It Helps With

- Technical SEO audits.
- Rendered SEO checks for JavaScript-heavy pages.
- Indexation and crawlability diagnostics.
- SEO/GEO content briefs.
- On-page optimization.
- AI Overviews, AI Mode, Copilot and ChatGPT Search visibility.
- Entity and citability improvements.
- Structured data recommendations.
- Ecommerce category and product SEO.
- SaaS comparison, alternative, use-case and integration pages.
- Local SEO and service-area pages.
- Migration planning and QA.
- Traffic drop diagnosis.
- Public copy QA before publishing.

## What Makes It Different

SEO/GEO Pro is intentionally conservative:

- It does not promise rankings, traffic or AI citations.
- It treats GEO as an additional layer on top of SEO fundamentals.
- It distinguishes confirmed evidence, probable findings, hypotheses and missing data.
- It does not recommend special AI-only tricks unless current official evidence supports them.
- It blocks internal SEO language from leaking into public landing pages.
- It includes safe URL handling for helper scripts to reduce SSRF risk during audits.

## Installation

### Codex Skill Install

Clone the repository and copy the skill into your Codex skills directory.

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

## Repository Structure

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

## Basic Usage in Codex

Ask Codex naturally. The skill should activate when the task is about SEO, GEO, AEO, indexing, organic search, schema, AI search visibility or public SEO copy.

Examples:

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

## Helper Script Examples

### Safe URL Validation

```bash
python scripts/seo_url_safety.py https://example.com --strict --json
```

### Fetch HTML Safely

```bash
python scripts/seo_fetch.py https://example.com --json
python scripts/seo_fetch.py https://example.com --output page.html
```

### Parse SEO Elements From HTML

```bash
python scripts/seo_parse_html.py page.html --base-url https://example.com --json
```

The parser extracts:

- title
- meta description
- meta robots
- canonical
- H1/H2/H3
- hreflang
- Open Graph and Twitter metadata
- JSON-LD schema blocks
- images and alt text
- internal and external links
- word count

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

The guard flags terms such as:

- SEO ownership
- cannibalization
- generic landing
- SEO hypothesis
- quick win
- thin content
- money page
- SERP ownership
- crawl budget

These terms are fine in private SEO plans. They should not appear in public commercial copy unless the page is explicitly teaching SEO.

## Evidence Labels

Use these labels in audits and recommendations:

| Label | Meaning |
|---|---|
| Confirmed | Proved by inspected source, crawl, rendered page, log, official documentation or first-party tool output. |
| Probable | Strongly supported, but not fully proven. |
| Hypothesis | Plausible and worth testing, but needs validation. |
| Experimental | Useful only as a controlled test, not a guaranteed result. |
| Missing data | Required data was not available. |

## Recommended Audit Output

```markdown
## Technical Diagnosis
| Priority | Area | Evidence | Evidence Label | Affected URLs | Action | Impact | Effort | Risk | Validation |
|---|---|---|---|---|---|---|---|---|---|

## GEO / AI Search
| Priority | Area | Evidence | Evidence Label | Action | Metric |
|---|---|---|---|---|---|

## Roadmap
| Priority | Action | Owner | Dependencies | Time | Leading Indicator | Business Metric |
|---|---|---|---|---|---|---|
```

## GEO Position

This skill follows a conservative interpretation of current official guidance:

- GEO/AEO is not a replacement for SEO.
- Google generative AI features are rooted in Search ranking and quality systems.
- There is no special schema required only for Google generative AI features.
- `llms.txt` can be useful for developer documentation and future optionality, but should not be sold as a guaranteed citation lever.
- AI-specific keyword rewrites and artificial content chunking should not replace useful, original, human-first content.
- Search crawlers, training crawlers and user-initiated agents must be handled separately.

## Testing

Run the local tests:

```bash
python -m pytest -q
```

The tests avoid live external network calls.

## Notes on Safety

The helper scripts validate user-supplied URLs before network access and block common SSRF targets, including:

- loopback addresses
- private IP ranges
- cloud metadata hosts
- non-HTTP schemes
- obfuscated IPv4 forms

This does not make the scripts a replacement for a hardened crawler or a production sandbox. Use them as local audit helpers.

## License

MIT. See [LICENSE](LICENSE).
