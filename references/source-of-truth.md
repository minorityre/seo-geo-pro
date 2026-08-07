# Source of Truth for SEO/GEO

Last live verification of the listed current-platform guidance: 2026-08-03.

Use this reference when a task depends on current policies, crawlers, AI Search, snippets, structured data, Core Web Vitals, YMYL, AI-generated content or claims about ranking, citations or platform controls. Re-open the decisive source at execution time; this registry can become stale.

## Contents

1. Evidence hierarchy and claim rules
2. Primary-source registry
3. Confirmed current principles
4. Platform controls and measurement
5. Structured data and page experience
6. Empirical GEO evidence
7. Claims to reject

## 1. Evidence Hierarchy and Claim Rules

Prefer:

1. The user's real site, data, product truth, code, rendered output and first-party tools.
2. Current official platform documentation, standards and policies.
3. Independent research with a visible method, comparable context and stated limitations.
4. Professional experience labeled as judgment.
5. Community and forum reports for symptoms, language and edge cases only.

Classify claims:

- `Confirmed`: official documentation or direct first-party evidence supports the exact statement.
- `Best practice`: a recommendation consistent with official guidance and user value, not a guaranteed factor.
- `Probable`: evidence is strong but incomplete or contextual.
- `Hypothesis`: plausible and needs validation.
- `Experimental`: a controlled tactic with uncertain or platform-specific effects.
- `Not verifiable`: do not use as a decision basis.

Do not say “Google rewards X” when the source says only that X helps users or eligibility. Do not turn quality-rater guidance, patents, correlations or third-party scores into confirmed ranking factors.

## 2. Primary-Source Registry

### Google Search

- Search Essentials: https://developers.google.com/search/docs/essentials
- Technical requirements: https://developers.google.com/search/docs/essentials/technical
- Spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Generative AI content guidance: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- 2026 generative AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- AI features and the website: https://developers.google.com/search/docs/appearance/ai-features
- Third-party SEO advice: https://developers.google.com/search/docs/fundamentals/third-party-seo
- Crawling/indexing and JavaScript SEO: https://developers.google.com/search/docs/crawling-indexing
- Structured-data policies and supported features: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Ecommerce SEO: https://developers.google.com/search/docs/specialty/ecommerce
- Review system and review guidance: https://developers.google.com/search/docs/appearance/reviews-system
- Search Quality Rater Guidelines: https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- Search Generative AI report announcement: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- Generative AI performance report: https://support.google.com/webmasters/answer/16984139
- Search generative AI control: https://support.google.com/webmasters/answer/16908024

### Bing and Microsoft

- Bing Webmaster Guidelines/help: https://www.bing.com/webmasters/help/
- AI Performance: https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
- AI Performance announcement: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- Microsoft AI-answer content guidance: https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- Bing `data-nosnippet`: https://blogs.bing.com/webmaster/October-2025/Bing-Introduces-Support-for-the-data-nosnippet-HTML-Attribute
- IndexNow documentation: https://www.indexnow.org/documentation

### OpenAI and ChatGPT Search

- OpenAI crawler/user-agent documentation: https://developers.openai.com/api/docs/bots
- Publisher/developer FAQ: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- ChatGPT Search: https://help.openai.com/en/articles/9237897-chatgpt-search

### Web standards and experience

- Schema.org: https://schema.org/docs/full.html
- Core Web Vitals: https://web.dev/articles/vitals
- Google page experience: https://developers.google.com/search/docs/appearance/page-experience
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI page structure: https://www.w3.org/WAI/tutorials/page-structure/
- WAI images: https://www.w3.org/WAI/tutorials/images/
- Agent-friendly websites: https://web.dev/articles/ai-agent-site-ux

## 3. Confirmed Current Principles

### Length and content quality

- Google has no preferred word count and says there is no ideal page length.
- Quality depends on purpose, usefulness, originality, effort, accuracy, experience and satisfaction, not length alone.
- Main content can be prose, images, video, product functionality, a calculator, a shopping flow or another working experience.
- Google warns against summary-only, search-engine-first and scaled low-value content regardless of whether humans or AI produced it.
- AI assistance is allowed; accuracy, relevance, provenance and editorial review remain required.

Implication: use a semantic coverage and page-experience contract. Never use a global word minimum as the publication gate.

### Google generative Search

- Google's generative Search features rely on core Search ranking/quality systems and indexed Search content.
- A page must be indexed and eligible for a snippet to be eligible; eligibility does not guarantee appearance.
- Google recommends unique, expert-led, non-commodity content, useful organization and high-quality images/video.
- Query fan-out is a research mechanism, not permission to create a page for every variant.
- Google says `llms.txt`, AI-only markup, artificial micro-chunking, AI-specific rewrites and inauthentic mentions are not required for Google Search.
- There is no special schema required for generative Search.
- Agent-friendly design is emerging: browser agents may rely on screenshots, DOM and accessibility trees. Semantic controls and stable, explicit states help humans and agents.

### AI-generated content

- Large-scale unoriginal or low-value output can violate scaled-content policy regardless of production method.
- Accuracy, quality and relevance also apply to title, description, alt text and structured data.
- Explain automation/AI use when readers would reasonably expect to know how content was created.
- Ecommerce AI images/product data may have additional Merchant Center metadata/disclosure requirements; verify them live.

### Reviews and recommendations

- High-quality reviews require insightful analysis, original research and accountable expertise or enthusiasm.
- First-hand reviews should show how the test was performed and evidence of the work.
- A documentary comparison is valid when labeled honestly; do not present it as hands-on testing.
- Rankings need a homogeneous method, fit/no-fit reasoning, limits and verifiable data.

## 4. Platform Controls and Measurement

### Google

As of 2026-08-03, Search Console is rolling out dedicated Generative AI performance reports to a subset of properties.

- The dedicated view reports impressions and dimensions such as pages, countries, devices and dates as available.
- The same activity remains included in overall Search performance; do not double-count it.
- Availability is limited/rolling out; do not assume every property has the report or control.
- Verify the separate Search generative AI inclusion control, inheritance and business implications when available.
- A generative impression is visibility, not a citation-quality, traffic or conversion metric.

### Bing/Copilot

Bing AI Performance can report citation activity, cited pages and grouped grounding-query information across supported Microsoft/partner experiences.

- Citation counts do not indicate ranking, authority, importance or the page's role in an answer.
- Grounding queries are grouped/aggregated, not exact user prompts.
- Data is sampled/aggregated and observational; changes do not prove the effect of a content update.
- Treat preview intent, topic and citation-share dimensions as versioned and verify availability.

IndexNow notifies engines of URL changes. A successful request means receipt, not crawl, indexation or ranking.

### OpenAI

Verify current docs and IP ranges; do not hard-code user-agent versions.

- `OAI-SearchBot`: Search discovery/appearance. Allowing it does not guarantee placement.
- `GPTBot`: potential training use. Its decision is independent of Search.
- `ChatGPT-User`: user-initiated visits; robots rules may not apply and it does not control Search eligibility.
- `OAI-AdsBot`: ad landing-page validation, relevant only when ads are in scope.

Blocking Search crawling may not remove every navigational reference obtained through other providers. Stronger removal can require `noindex` while allowing the relevant crawler to read it; verify the current platform instructions and consequences first.

### Cross-platform GEO measurement

Keep separate:

`indexation → retrieval → citation → prominence → claim absorption/fidelity → referral → branded demand → assisted conversion → revenue`

For manual panels, record engine/surface, market, account or mode, device, date, exact prompt/query, repetitions/paraphrases, cited URLs and response. Do not combine heterogeneous engines into one unexplained score or declare a trend from one capture.

## 5. Structured Data and Page Experience

### Structured data

Use a live resolver, not a timeless static list:

1. Identify the consumer and current Search feature.
2. Verify current support, policies and required/recommended properties.
3. Confirm every value represents visible, real, current content.
4. Validate syntax and rendered output.
5. State only eligibility; valid markup does not guarantee display, ranking or citation.

Feature support changes. For example, Google retired Sitelinks Search Box/SearchAction as a Search feature, and FAQ rich-result visibility is highly restricted. Re-check before recommending either.

### Core Web Vitals

Current good thresholds:

- LCP: 2.5 seconds or less.
- INP: 200 milliseconds or less.
- CLS: 0.1 or less.

Use the 75th percentile of real users and segment device/origin/page as available. Lighthouse is laboratory diagnostic evidence, not proof of field performance, accessibility compliance or ranking improvement.

### Accessibility and agents

Use WCAG 2.2 AA as the default product baseline unless stronger requirements apply. Automated tools cannot establish complete conformance. Add manual keyboard, focus, zoom/reflow, headings/landmarks, contrast, media and assistive-technology checks.

Semantic HTML, accessible names and stable state changes help people, search processing and browser agents. Do not claim direct ranking benefit.

## 6. Empirical GEO Evidence

Treat this section as research context, not policy.

| Evidence | Direct observation | Limitation | Allowed implication |
|---|---|---|---|
| GEO, KDD 2024: https://arxiv.org/abs/2311.09735 | Some citation/statistic/style interventions improved a visibility metric within fixed retrieved contexts | Does not prove organic retrieval, traffic, durability or cross-platform effects | Use evidence-rich writing for readers; test citation effects as `Experimental` |
| C-SEO Bench, NeurIPS 2025: https://papers.neurips.cc/paper_files/paper/2025/file/27aa3aeff0f8460a7b43d30fa6c5c032-Paper-Datasets_and_Benchmarks_Track.pdf | Many rewrite heuristics were ineffective or harmful; context position/retrieval mattered more | Experimental models/tasks do not reproduce every commercial engine | Reject universal recipes such as “add statistics/FAQs to rank in AI” |
| AI Overviews measurement, 2026 preprint: https://arxiv.org/abs/2605.14021 | In 55,393 queries, cited domains and co-displayed first-page results diverged; some answer claims were unsupported by cited pages | Forty-day, trending-query, observational window | Separate organic rank, retrieval, citation and claim fidelity; verify claims at source |
| Wikipedia traffic study, 2026 preprint: https://arxiv.org/abs/2602.18455 | AI-summary exposure was associated with heterogeneous traffic declines and stronger substitution for some intents | Wikipedia/language setting does not generalize to every business | Measure business outcomes by intent; do not assume visibility produces clicks |

Research findings can conflict because engines, retrieval sets, prompts, metrics and periods differ. Explain those differences rather than averaging conclusions.

## 7. Claims to Reject

- “Google prefers 2,000 words” or any universal length target.
- “A 700-word page is thin” without showing what useful work is missing.
- “E-E-A-T, quality-rater criteria or information gain is a direct ranking factor.”
- “`llms.txt`, special GEO schema, artificial chunking or FAQ volume is required for Google AI.”
- “Valid schema guarantees a rich result, ranking or citation.”
- “Lighthouse green proves good real-user CWV or accessibility compliance.”
- “IndexNow `200` means indexed.”
- “More Bing citations means higher AI rank or authority.”
- “Blocking GPTBot blocks ChatGPT Search.”
- “All search/answer engines obey the same controls.”
- “One prompt or screenshot proves AI visibility.”
- “A third-party AI visibility score is an internal platform metric.”
- “A known GEO rewrite formula guarantees discovery, citations or revenue.”
