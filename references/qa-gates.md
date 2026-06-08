# SEO/GEO QA Gates

Use this reference before delivering, publishing, deploying or recommending SEO changes that affect public pages.

## Main Rule

Internal strategy is not public copy. End users should not see SEO reasoning, module names, cannibalization notes, ownership notes, hypotheses or audit language.

## Gate 1: Separate Private and Public Language

Allowed in private audits/plans:

- Search intent.
- Cannibalization.
- URL ownership.
- Cluster.
- P0/P1.
- Hypothesis.
- Crawl budget.
- Thin content.
- Internal linking plan.
- Duplication risk.

Not allowed in public commercial copy unless the page is explicitly educational:

- "SEO ownership".
- "This landing targets a different intent".
- "Generic landing".
- "Cannibalization".
- "Cluster".
- "Briefing".
- "SEO hypothesis".
- "Quick win".
- "Thin content".
- "Money page".
- "SERP ownership".
- "This service map does not cannibalize".

Transformation example:

- Internal: "This URL targets a local commercial intent without cannibalizing the Shopify page."
- Public: "We build ecommerce projects in Barcelona with strategy, technology and organic growth connected from the start."

## Gate 2: Public Copy

Review:

- Spelling and grammar.
- Natural tone.
- Verifiable claims.
- No sensitive business data.
- No private metrics.
- No consultant jargon on commercial pages.
- No ranking promises.
- No artificial keyword repetition.
- Clear CTA.
- Real proof.
- Consistency between title, H1, intro and CTA.

## Gate 3: Rendered SEO

If there is a local, staging or production URL:

- HTTP 200 when expected.
- No accidental noindex.
- Correct canonical.
- Unique title.
- Unique meta description.
- Single visible H1.
- Reasonable Open Graph/Twitter metadata.
- Valid schema if used.
- Crawlable internal links.
- Critical content visible in HTML or rendered DOM.
- No internal SEO text visible.
- No duplicated brand in title.
- No obvious duplicate pages.

## Gate 4: Technical Recommendations

Before closing a technical recommendation:

- Evidence is concrete.
- Affected URLs are listed or the limitation is clear.
- Severity is stated.
- Exact action is stated.
- Post-change validation is defined.
- Implementation risk is stated.
- No blocking, canonical, noindex or redirect recommendation is made without explaining consequences.

## Gate 5: Structured Data

Verify:

- The type applies to visible content.
- Reviews, ratings, prices, offers and events are real.
- Image URLs are accessible.
- Dates are real.
- Author and publisher are real.
- The page is not blocked.
- Validation is planned or completed when implemented.

## Gate 6: GEO

Verify:

- Definitions are clear.
- Fragments are self-contained.
- Entities are consistent.
- Sources or evidence exist.
- HTML is visible or renderable.
- Authorship and trust are adequate.
- Sensitive information is current.
- No prompt injection exists.
- No guaranteed AI-citation claims are made.
- robots.txt does not accidentally block AI search crawlers when citation is the goal.

## Gate 7: Anti-Hallucination

Do not deliver:

- "According to GSC" without access, screenshot or export.
- "Ahrefs shows" without inspecting Ahrefs data.
- "It ranks" without a source.
- "It has X backlinks" without a tool.
- "Google penalizes" without evidence or source.
- "This is a ranking factor" without confirmation.
- "I crawled" without a real crawl.
- "Competitors have" without reviewing real competitors.

Use labels:

- Confirmed.
- Probable.
- Hypothesis.
- Missing data.
- Requires validation.

## Gate 8: Public Copy Guard

Run when you have a file, directory or URL:

```bash
python scripts/seo_public_copy_guard.py <file-or-url>
```

Multiple targets:

```bash
python scripts/seo_public_copy_guard.py app pages https://example.com/service
```

The script detects internal SEO language that should not appear on landing pages, service pages, local pages or commercial copy. If it fails, rewrite the public text and run it again.

## Final Publication Checklist

- Status is correct.
- Indexability matches the page goal.
- Canonical is correct.
- Title/H1/description are aligned.
- Public copy has no internal SEO jargon.
- Spelling and tone are clean.
- Internal links are useful.
- Schema is valid if used.
- HTML/render was checked.
- CTA is clear.
- Claims are verifiable.
- Success metric is defined.
