# Source of Truth for SEO/GEO

Use this reference when a task depends on current guidance, crawlers, robots, AI Search, snippets, structured data, YMYL, AI-generated content or claims about ranking factors.

## Evidence Hierarchy

1. Current official documentation.
2. Direct evidence from SERPs, GSC, Bing Webmaster Tools, logs, crawls, Ahrefs, Semrush, Sistrix and analytics.
3. Studies with clear and reproducible methodology.
4. Practical experience clearly labeled as professional judgment.
5. Third-party opinions only as hypotheses.

If community SEO advice conflicts with official documentation, prioritize official documentation. If official documentation does not cover the case, state uncertainty and propose validation.

## Required Sources by Topic

Google:

- Search Essentials: https://developers.google.com/search/docs/essentials
- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Guidance on AI-generated content: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Optimizing for generative AI features on Google Search: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Crawling and indexing docs: https://developers.google.com/search/docs/crawling-indexing
- Structured data policies: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Ecommerce SEO: https://developers.google.com/search/docs/specialty/ecommerce
- Search Quality Rater Guidelines: https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf

Bing and Microsoft:

- Bing Webmaster Guidelines: https://www.bing.com/webmaster/help/Webmaster-Guidelines-30fba23a
- Bing Webmaster Tools Help: https://www.bing.com/webmasters/help/
- Bing AI Performance: https://www.bing.com/webmasters/help/9f8e7d6c
- Microsoft guidance for AI search answers: https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- IndexNow: https://www.indexnow.org/

OpenAI and ChatGPT Search:

- OpenAI crawlers and user agents: https://developers.openai.com/api/docs/bots

Standards:

- Schema.org: https://schema.org/docs/full.html
- Web.dev Core Web Vitals: https://web.dev/articles/vitals

## Claim Rules

- `Confirmed`: only when official documentation or direct first-party evidence supports the statement.
- `Best practice`: widely accepted recommendation consistent with official documentation.
- `Hypothesis`: plausible, but validation is needed.
- `Experimental`: useful for a controlled test, not for promised results.
- `Not verifiable`: do not use it as a decision basis.

Do not say "Google rewards X" if the source says only that X helps users or eligibility. Do not say "ranking factor" if the source does not confirm it.

## Official Principles

Google Search Essentials prioritize minimum technical requirements, spam policies and helpful, reliable, people-first content. Meeting requirements does not guarantee crawling, indexing or ranking.

Google recommends using words people would use to search for the content in prominent places such as title, main heading, alt text and anchor text, without keyword stuffing.

Google's generative AI guidance states that AI search features are rooted in core Search ranking and quality systems. For Google Search, GEO/AEO is still SEO.

Google says you do not need special schema, AI-only markup, `llms.txt`, artificial chunking or AI-specific keyword rewrites for generative AI features. Unique, useful, non-commodity content and technical accessibility matter more.

Google's AI-content policy does not prohibit AI assistance. The problem is scaled, low-value, inaccurate, irrelevant or unsupervised content.

Bing treats SEO and GEO as connected: SEO improves discovery, indexation and clarity; GEO improves eligibility for grounding and reference in AI answers. Neither SEO nor GEO guarantees rankings, traffic, grounding or citations.

Microsoft recommends fresh, authoritative, structured, semantically clear content with clear headings, tables, FAQs, data, examples, sources and consistency across text, images and video.

OpenAI distinguishes:

- `OAI-SearchBot`: search and appearance in OpenAI search features.
- `GPTBot`: crawling that may be used for model training.
- `ChatGPT-User`: user-initiated actions; robots.txt may not apply and it is not used to determine Search appearance.

## Robots, Crawlers and AI

Before recommending robots rules:

1. Identify the goal: search appearance, citation, training permission, training block, sensitive content protection or crawl-load reduction.
2. Distinguish search crawlers, training crawlers and user-initiated agents.
3. Verify current official user agents.
4. Document implications:
   - Blocking search bots can reduce appearance and citation opportunities.
   - Blocking training bots does not equal blocking search bots.
   - robots.txt does not remove already indexed content.
   - Meta directives and headers can affect snippets, cache and answer use.
5. Do not copy bot lists from blog posts without verification.

## Structured Data

Schema must represent visible, real content. Do not use schema to invent reviews, ratings, offers, prices, stock, authors, FAQs or events. Validate with Rich Results Test or Schema Markup Validator when implemented.

## E-E-A-T and YMYL

E-E-A-T is not a meta tag or schema property. It is a trust evaluation framework. In YMYL, raise standards for accuracy, consensus, authorship, expert review, primary sources, freshness and limits.

## Core Web Vitals

Use field data when possible. Current good thresholds:

- LCP: 2.5 seconds or less.
- INP: 200 milliseconds or less.
- CLS: 0.1 or less.

Use the 75th percentile of real users when field data exists. Lighthouse is useful lab evidence, but it does not replace field data.
