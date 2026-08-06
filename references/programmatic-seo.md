# Programmatic SEO and Scaled-Content Gate

Use this reference for directories, marketplaces, location/service combinations, integration libraries, template galleries, comparison matrices, data pages or any system that can generate many indexable URLs.

## Contents

1. Core rule and admission contract
2. Page-worthiness and template contracts
3. Pilot, QA and lifecycle
4. Evidence labels

## Core Rule

Scale useful data or functionality, not prose. The ability to substitute entities into a template does not make each result a distinct page.

Do not use universal word counts, percentages of unique text or inventory thresholds. Define project-specific thresholds before generation and make the system fail closed.

## Admission Contract

Record:

```markdown
- Repeated user job:
- Evidence of demand:
- Why one canonical page cannot serve the variants:
- Dataset and source of truth:
- Data owner and update process:
- Unique entity fields:
- Derived value, calculation or comparison:
- Product or user utility:
- Minimum data completeness:
- Minimum inventory/result threshold:
- Maximum acceptable staleness:
- Deduplication/entity-resolution method:
- index_if:
- noindex_if:
- Do-not-generate condition:
- Canonical rule:
- Empty/low-data state:
- 404/redirect/consolidation behavior:
- Internal-link generation rule:
- Pilot cohort:
- Sampling and edge-case QA:
- Monitoring window:
- Scale, stop and rollback criteria:
```

Fail admission if:

- variants share the same user job and result;
- the page differs mainly through tokens or location names;
- data cannot be kept accurate;
- the page has no useful outcome without search traffic;
- there is no stable canonical/entity model;
- low inventory or missing data produces misleading pages;
- the project cannot review representative templates and instances;
- the goal is primarily to cover query fan-out or manipulate rankings/AI responses.

## Page-Worthiness Predicate

Every generated URL must satisfy a documented predicate such as:

```text
index_if = entity_is_valid
  AND required_fields_complete
  AND inventory_or_evidence_above_project_threshold
  AND content_or_utility_is_distinct
  AND canonical_is_unique
  AND freshness_within_limit
  AND page_passes_template_rules
```

The exact fields and thresholds must come from real user value, inventory/data distributions and risk. Do not invent them from an SEO checklist.

## Template Contract

Each page family needs:

- a clear job and intent;
- reliable entity/data facts;
- meaningful derived value, comparison or workflow;
- a useful primary component, not merely templated text;
- honest low-data and empty states;
- visible freshness/source information when material;
- a natural conversion or next step;
- crawlable incoming and outgoing links;
- consistent canonical, pagination and facet behavior;
- metadata and schema generated only from real visible values;
- localization beyond machine translation when market context changes;
- privacy, consent and moderation rules for user data/UGC.

Do not generate fake introductions, FAQs, reviews, city proof, experts, statistics or testimonials to make templates look unique.

## Pilot and QA

Before scaling:

1. Build a small representative cohort across high, medium, low and missing-data cases.
2. Review every template variant and edge state in rendered desktop and mobile views.
3. Crawl the cohort and inspect status, indexability, canonical, internal links, pagination/facets, schema and rendering.
4. Test real user utility and conversion/activation behavior.
5. Confirm data refresh, invalidation, deletion and redirect paths.
6. Monitor indexation, qualified acquisition, engagement/task completion, conversion and support/quality guardrails.
7. Scale only if the cohort passes its predeclared success conditions.

During scale, sample by template and risk rather than checking only the most complete pages. Maintain distribution monitoring for completeness, duplication, freshness, indexation and business quality.

Stop or roll back when:

- page quality falls below the predicate;
- duplication/canonical conflicts grow;
- low-value URLs dominate crawling or indexation;
- data becomes stale or misleading;
- qualified engagement/conversion is absent despite sufficient observation;
- spam, moderation, privacy or brand risk appears;
- the template creates doorway-like routes or a worse experience than consolidation.

## Lifecycle

Define behaviors for:

- newly valid entities;
- materially updated records;
- temporarily empty inventory;
- permanently removed records;
- merged/renamed entities;
- duplicate inputs;
- translated/localized variants;
- stale or unverified records;
- user-generated content under review.

Use sitemaps and IndexNow where supported as discovery/change notifications. A successful submission does not prove crawl, indexation or ranking.

## Evidence Labels

- Google scaled-content, doorway and site-reputation policies are `Confirmed` policy constraints.
- Product-relevant data and working utility are professional and empirical success patterns, not guaranteed ranking factors.
- Page thresholds and scale criteria are project decisions that must be validated with the pilot.
- GEO effects of programmatic pages are `Experimental` unless first-party longitudinal evidence supports them.
