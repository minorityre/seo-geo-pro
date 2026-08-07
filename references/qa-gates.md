# SEO/GEO QA Gates

Use this reference before delivering, publishing, deploying or recommending SEO changes that affect public pages.

## Contents

- Gate 0: admission and content contract
- Gates 1–2: private/public language and copy
- Gates 3–5: rendered SEO, technical recommendations and structured data
- Gates 6–8: GEO, anti-hallucination and copy guard
- Gates 9–12: semantic depth, page experience, programmatic scale and measurement/lifecycle
- Final publication checklist

## Main Rule

Internal strategy is not public copy. End users should not see SEO reasoning, module names, cannibalization notes, ownership notes, hypotheses or audit language.

## Gate 0: Admission and Content Contract

Before creating or approving public content, verify:

- A real user job, need and acceptance criteria exist.
- The create/update/consolidate/redirect/noindex decision was made.
- The page/format is appropriate to the job.
- Primary and secondary intents belong on the same canonical URL.
- Required questions, decisions, proof, original contribution, media/functionality and next action are defined.
- Existing pages and cannibalization were reviewed.
- Missing facts, experience, rights or expert approval are explicit and block publication when material.

Fail if the page exists only because of a keyword, fan-out query or generated template variant.

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

## Gate 9: Semantic Depth and Editorial Quality

Do not use word count as the acceptance test. Verify:

- Every required user question and decision maps to final content or a working component.
- The reader can complete the defined job without a predictable second search.
- Material claims have support, scope, date and limitations.
- Material figures, ranges, thresholds and safety recommendations have a primary source, reproducible calculation or accountable professional method.
- Original value is visible: experience, data, case, expert view, comparison, original media, tool, template or decision-making synthesis.
- Examples, objections, errors, exceptions and limits exist where they change the decision.
- Each section adds a distinct answer, proof, decision, example, exception or action.
- Reverse-outline, specificity, second-search and deletion tests were run.
- Repetition, generic filler and keyword-only sections were removed.
- A broad/definitive task was not closed with a skeletal draft merely because headings were filled.

Keep the artifact in draft/review if decisive evidence or differentiation is missing. Do not fabricate “depth.”

Assign a readiness state: `brief-ready`, `copy-complete`, `implementation-pending`, `evidence-blocked`, `review-approved` or `publish-ready`. Fail any “ready to publish/as is” claim if author/reviewer, URL, factual inputs, rights, CTA destination, links, metadata/schema values, implementation or rendered QA remains unresolved. Do not use a draft-generation date as `datePublished`, `dateModified` or “last reviewed.”

## Gate 10: Page Experience, Media, Accessibility and Agents

Review the rendered page, not only text:

- Main answer/value and primary action are clear.
- Information order follows the user job.
- Proof is close to the relevant claim or CTA.
- CTA matches the destination and what happens next.
- Critical price, limitations, evidence or instructions are not hidden unnecessarily.
- Media has a real job, provenance/rights, contextual alt treatment and performance dimensions.
- Interactive states cover loading, empty, error, success, disabled and permissions as relevant.
- Desktop/mobile, content extremes, zoom/reflow and reduced motion are usable.
- Title, landmarks, headings, reading/focus order, link purpose, keyboard, focus visibility, contrast, labels, errors and media alternatives meet applicable WCAG 2.2 AA requirements.
- An automated accessibility scan is supplemented by manual checks; do not claim conformance from a clean scanner.
- When agent journeys matter, semantic controls, accessible names, DOM/a11y-tree relationships and explicit state changes were inspected.

## Gate 11: Programmatic and Scaled Content

Before a pilot or scale decision, verify:

- The dataset/source of truth, owner and freshness process exist.
- Every URL passes a project-specific page-worthiness predicate.
- `index_if`, `noindex_if`, do-not-generate, canonical, empty-state and redirect/consolidation rules are explicit.
- Pages provide unique data, inventory, calculation, comparison or product utility beyond token substitution.
- Query variants that share one user job are consolidated.
- The pilot covers high, medium, low and missing-data cases.
- Every template/edge state and a risk-based instance sample were crawled, rendered and reviewed.
- Scale, stop and rollback criteria include technical, task-success, business, spam, privacy and brand guardrails.

Fail closed: weak pages must remain ungenerated, noindex, consolidated or redirected as the contract specifies.

## Gate 12: Measurement and Lifecycle

Verify:

- Baseline, source, segment and observation window are clear.
- Eligibility, visibility, acquisition, task success, activation, conversion and retention are not conflated.
- Google/Bing/AI metrics are interpreted within their published limits.
- AI surfaces are measured separately with repetitions and context; one screenshot is not a trend.
- Correlation is not presented as causation.
- Owner, review date, update triggers and merge/redirect/delete criteria exist.
- Failure and rollback checks are defined for risky changes.

## Final Publication Checklist

- Page admission and URL decision passed.
- Content contract and coverage matrix reconciled.
- Status is correct.
- Indexability matches the page goal.
- Canonical is correct.
- Title/H1/description are aligned.
- Public copy has no internal SEO jargon.
- Spelling and tone are clean.
- Content has material value without omission or filler.
- Claims, original contribution and evidence are verifiable.
- Product/page utility and critical states work.
- Internal links are useful.
- Schema is valid if used.
- HTML/render was checked.
- CTA is clear.
- Mobile, media and applicable accessibility checks passed.
- Distribution, success metric, owner and lifecycle are defined.
- Readiness is explicitly `publish-ready`; no declared pending dependency contradicts that state.
