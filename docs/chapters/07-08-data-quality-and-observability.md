# 7.8 Data quality and observability

## Overview and motivation

[Data quality](https://en.wikipedia.org/wiki/Data_quality) is fitness for use: the degree to which data serves the decisions, products, and reports that depend on it. A dataset is not good or bad in the abstract. It is good enough for a purpose, or it is not. A customer address that is fine for a marketing count may be unfit for a legal notice. That framing matters, because it moves the conversation from "is our data perfect" (never) to "is our data fit for what we are about to do with it" (answerable, and testable). The classic dimensions are accuracy, completeness, consistency, timeliness, validity, and uniqueness, and most real problems reduce to one of them.

Here is the uncomfortable truth for large teams: bad data is worse than no data. When you have no data, you know it, and you proceed with appropriate caution. When you have wrong data that looks right, you act on it with false confidence. Bad data corrupts silently. It flows into a dashboard that an executive trusts, into a [machine learning](https://en.wikipedia.org/wiki/Machine_learning) model that trains on it and encodes its errors, and into decisions that no one thinks to question because the number was right there on the screen. The damage is diffuse and delayed, which is exactly why it is expensive. By the time someone notices, the wrong number has been quoted in a board deck, a regulatory filing, or a public statistic.

Data observability is the discipline that catches this before your consumers do. It is the direct parallel to software observability and telemetry (chapter 9.2): the same instinct that tells you to monitor request latency and error rates tells you to monitor data freshness, volume, schema, and distribution. This chapter builds on data strategy and governance (chapter 7.1) and data engineering (chapter 7.2), and it feeds data modeling and the semantic layer (chapter 7.7) and responsible and trustworthy AI (chapter 6.5). For enterprises reconciling many source systems and for governments publishing statutory statistics, treating data reliability as an engineering problem with owners and service levels is the difference between trust and a very public correction.

## Key principles

- Data quality is fitness for use, not perfection; define it against the purpose.
- Bad data is worse than no data, because it corrupts decisions silently.
- Test data like you test code: assertions, expectations, and schema checks in the pipeline.
- Contracts between producers and consumers make expectations explicit and enforceable.
- Observe freshness, volume, schema, and distribution, the same way you observe services.
- Lineage turns "something is wrong" into "here is what broke and what it affects."
- Treat data incidents like production incidents, with ownership, severity, and service levels.
- Detect problems where they enter, not three layers downstream in a dashboard.

## Recommendations

### Define quality by dimension, and measure it

Vague quality goals produce vague results. Break quality into measurable dimensions and attach concrete checks to each. Accuracy asks whether values reflect reality (does this recorded revenue match the source ledger). Completeness asks whether expected records and fields are present (are any days missing, are required columns null). Consistency asks whether the same fact agrees across systems (does the customer count in finance match the count in the warehouse). Timeliness asks whether data arrives in time to be useful (is yesterday's data ready before the morning report). Validity asks whether values conform to rules and formats (are all currency codes real, are dates in range). Uniqueness asks whether entities appear once (are there duplicate orders inflating the total). Pick the dimensions that matter for each dataset, set thresholds, and track them over time. Quality you do not measure is quality you are guessing at.

### Test pipelines with assertions and expectations

Data deserves the same testing rigor as application code. Use [data validation](https://en.wikipedia.org/wiki/Data_validation) at every stage: assertion-based tests that fail the pipeline when an invariant is violated, and expectation-based tests that declare what "normal" looks like for a table and flag deviations. Assert that primary keys are unique and non-null, that foreign keys resolve, that categorical columns contain only accepted values, that numeric columns fall within plausible ranges, and that row counts land in an expected band. Add schema checks that fail loudly when a column is added, dropped, renamed, or retyped upstream. Run these checks in continuous integration so a bad transformation is caught before merge, and run them again in production against live data so a bad source is caught before it reaches consumers. The goal is to fail early and loudly, because a broken pipeline is safer than a silently wrong one.

### Establish data contracts between producers and consumers

Most data quality incidents start upstream, when a producing team changes a schema, a semantic meaning, or a value convention without knowing who depends on it. A [data contract](https://en.wikipedia.org/wiki/Data_contract) fixes this by making the interface explicit: the schema, the semantics of each field, allowed values, freshness guarantees, and the process for making a change. The producer commits to the contract, the consumer builds against it, and a breaking change requires versioning and notice rather than a silent surprise on Monday. Enforce contracts mechanically where you can, by validating incoming data against the contract at the boundary and rejecting or quarantining violations. Contracts turn an implicit, fragile dependency into an explicit, negotiated one. They also make ownership visible, which is half the battle at scale.

### Monitor the four signals of data observability

Data observability watches four signals, in direct parallel to how you watch a running service (chapter 9.2). Freshness: is the data as recent as it should be, or has the pipeline stalled. Volume: is the row count in the expected range, or did a table arrive half-empty or double-loaded. Schema: has the structure changed unexpectedly. Distribution: have the values themselves drifted, so that a column that was 2 percent null is suddenly 40 percent null, or an average has shifted in a way that signals an upstream bug. Instrument these signals on your important tables, learn their normal patterns, and alert on breaches. This is how you replace "an executive noticed the dashboard looked wrong" with "the owning team got paged at the point of failure." The worst possible detector of a data problem is a downstream human who trusts the number.

### Add anomaly detection, but tune it against alert fatigue

Static thresholds catch the obvious failures. For subtler drift, layer in [anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection) that learns each metric's normal seasonal pattern and flags statistically unusual deviations, so you catch a slow leak before it becomes a flood. Be disciplined about this. Noisy anomaly alerts train people to ignore alerts, which is worse than no alerts. Start with your highest-value tables, alert only on things a human should act on, route each alert to a named owner, and tune ruthlessly. An alert that no one acts on is a bug in your monitoring, not a feature.

### Track lineage for impact analysis and root cause

When something breaks, two questions matter immediately: what caused it, and what does it affect. [Data lineage](https://en.wikipedia.org/wiki/Data_lineage) answers both by mapping how data flows from source through every transformation to every downstream table, dashboard, and model. For root cause, you trace a bad figure back upstream to the transformation or source that introduced it. For impact analysis, you trace forward to see every consumer touched by a bad load, so you can notify them and quarantine the damage before it spreads. Capture lineage automatically from your transformation and orchestration tools rather than maintaining a diagram by hand, because a hand-drawn diagram is wrong the day after you draw it. In enterprises with many sources, publish lineage into a data catalog so any consumer can see where a field came from and trust it accordingly.

### Treat data incidents like production incidents

The practices that keep services reliable apply directly to data. Give every important dataset an owner. Define severity levels for "data downtime," the periods when data is missing, wrong, or late. Set service levels: freshness targets, an acceptable error budget, and a target time to detect and resolve. Put data on-call rotations behind the most critical pipelines, write runbooks, and run blameless postmortems after incidents so the same failure does not recur. When a payment table is late or a public metric is wrong, that is an incident, and it deserves the same seriousness as an outage. This is the cultural shift that makes all the tooling pay off.

### Profile and reconcile continuously

Profiling means routinely examining the shape of your data: value distributions, null rates, cardinality, min and max, and format patterns. It surfaces problems you did not think to assert, and it tells you what "normal" looks like so you can set good expectations. Reconciliation means checking that independent sources agree: does the warehouse total match the source system of record, does the sum of the parts equal the whole. Automate reconciliation between critical systems and alert on divergence, because a reconciliation break is often the earliest and clearest signal that something upstream went wrong.

## Trade-offs: pros and cons

| Approach | Pros | Cons | Best fit |
|---|---|---|---|
| Assertion tests (hard fail) | Stops bad data cold, clear invariants | Can block pipelines on minor issues | Critical keys, referential integrity |
| Expectation tests (soft flag) | Catches drift, less brittle | Needs tuning, can be ignored | Distributions, volume bands |
| Data contracts | Prevents upstream surprises, clear ownership | Coordination and governance overhead | Cross-team producer or consumer boundaries |
| Anomaly detection | Catches subtle, unforeseen drift | Alert fatigue, false positives | High-value tables, seasonal metrics |
| Manual spot checks | Cheap to start, no tooling | Does not scale, misses silent errors | Very early stage only |
| Full observability platform | Broad coverage, lineage, alerting | Cost, setup, another system to run | Many sources, regulated reporting |

The central tension is coverage versus noise. Instrument nothing and problems reach your consumers first, which destroys trust. Instrument everything with hair-trigger alerts and you drown your team in false positives until they mute the channel, which also lets problems reach consumers. Resolve this by ranking your data by blast radius. The tables that feed board metrics, customer-facing products, regulatory reports, and machine learning models get the full treatment: contracts, hard assertions, observability, and on-call ownership. The long tail of exploratory tables gets light-touch profiling. Spend your reliability budget where wrong data would hurt most, and be deliberately sparing everywhere else.

## Questions to discuss with your team

1. **When bad data reaches production, who finds out first, and how?** This is the single most revealing question about your data reliability, because the honest answer is usually "a consumer, by accident." If an analyst, an executive, or a customer is your detection system, your mean time to detect is measured in days and your credibility takes the hit every time. The alternative is instrumentation that pages the owning team at the point of failure, before the bad number propagates. Bring real numbers: how many of your last ten data incidents were caught by monitoring versus reported by a downstream human, and how long did each sit undetected. The answer tells you whether you have observability or just hope, and it should directly drive where you invest in freshness, volume, schema, and distribution checks first.

2. **Which datasets have an owner, a contract, and a service level, and which are orphans?** At scale, most data quality failures trace back to an unowned interface: a producing team changed something with no idea who depended on it, because no contract said so. Ownership is the foundation that makes contracts, alerting routes, and incident response possible, and orphaned datasets are where silent corruption lives. Walk through your most important tables and ask, for each, who is accountable, what the producer has committed to, and what freshness and accuracy the consumers are promised. Bring your lineage: the tables with the largest downstream blast radius are the ones that most need this and are often the ones missing it. The gap between "important" and "owned" is your priority list for the next quarter.

3. **What is the actual cost of a data quality incident to us, and do we treat it accordingly?** Teams underinvest in data quality because the cost of bad data is diffuse and delayed, so it never shows up as a line item, while the cost of building quality tooling is concrete and immediate. Reframe it by pricing a real incident end to end: the wrong decision, the rework, the engineer hours spent tracing root cause without lineage, the eroded trust that makes people quietly rebuild their own shadow datasets, and, in regulated or public-facing settings, the correction notice and its reputational damage. Bring a specific example from the last year and total it up honestly. If a single silent failure in a payment or public-statistics pipeline could cost more than a year of observability tooling, the business case makes itself, and the conversation shifts from whether to invest to where.

## Examples

**Startup.** A twenty-person company runs its go-to-market on a warehouse fed by product events and a payments provider. Early on, a mislabeled currency field quietly inflated reported revenue for two weeks before anyone noticed, which shook the team's trust in every dashboard. They responded with a lightweight set of tests in their transformation tool: uniqueness and non-null on keys, accepted-value checks on currency and status columns, and a row-count band per source. They added basic freshness and volume monitoring on the handful of tables that feed the company metrics, routed to a single Slack channel one engineer owns. It is modest, but it catches the failures that matter, and the founders trust the numbers again.

**Enterprise.** A multinational bank reconciles customer and transaction data across dozens of source systems into a governed warehouse feeding regulatory reports, risk models, and executive dashboards. It runs data contracts at every producer boundary, so an upstream schema change is versioned and negotiated rather than sprung on consumers. An observability platform monitors freshness, volume, schema, and distribution across thousands of tables, with anomaly detection on the high-value ones and lineage published into a data catalog for impact analysis. Data incidents follow the same severity and on-call process as service outages, with service levels on the pipelines feeding regulatory submissions. When a source system drifts, the owning team is paged and the affected downstream reports are known within minutes, not discovered by a regulator.

**Government.** A national statistics agency publishes economic indicators that markets, policymakers, and the public treat as authoritative, so accuracy is a statutory obligation and every published figure must be auditable. Its pipelines land immutable raw survey and administrative records, then transform them in layered, tested stages with reconciliation against source totals at each step. Full lineage lets analysts trace any published number back to source records, which is both a quality tool and a legal requirement. Before release, figures pass validation gates for validity, completeness, and consistency against prior periods, and any anomaly is investigated and documented rather than published. A wrong public statistic is a serious incident, so the agency treats data downtime with the gravity that public trust demands.

## Business case: motivations, ROI, and TCO

The return on data quality and observability comes from trust preserved, incidents shortened, and bad decisions avoided. Trustworthy data is the foundation that makes every downstream investment in analytics, business intelligence, and AI actually pay off, because a model or dashboard is only as good as the data beneath it. When quality checks catch a bad load at the boundary, you avoid the far larger cost of a wrong number reaching a decision, a customer, or a filing. Lineage collapses root-cause investigation from days of manual tracing to minutes, which is pure recovered engineering time. Observability shrinks mean time to detect from "when a consumer complains" to "when the pipeline fails," which is where most of the trust damage is avoided.

The total cost of ownership includes tooling for testing, observability, and cataloging, plus the engineering time to instrument pipelines and the organizational work of assigning owners and writing contracts. This is real, but weigh it against the cost of not doing it: silent corruption discovered by executives, machine learning models trained on bad features that encode errors at scale, analysts quietly rebuilding shadow datasets because they no longer trust the official ones, and, in regulated or public settings, correction notices that damage credibility for years. To leadership, frame data quality as insurance on every data-driven decision the organization makes. The premium is modest and predictable. The uninsured loss, a single high-profile wrong number, is neither.

## Anti-patterns and pitfalls

- Treating data quality as a one-time cleanup project instead of an ongoing engineering practice.
- Discovering failures from downstream consumers rather than from monitoring at the point of failure.
- No dataset ownership, so no one is accountable when something breaks and no one gets paged.
- Producers changing schemas or semantics with no contract, silently breaking every consumer.
- Anomaly alerts so noisy that the team mutes the channel and misses the real incident.
- Feeding unvalidated data straight into machine learning models, encoding errors at scale (chapter 6.5).
- Maintaining lineage as a hand-drawn diagram that is wrong the day after you draw it.
- Chasing perfect data everywhere instead of fit-for-use quality on the tables that matter.
- Deleting raw data, so you cannot reprocess or reconcile when a quality bug surfaces later.

## Maturity model

- **Level 1, Initial:** Quality is nobody's job. Problems are found by consumers, usually after a wrong number reaches a report. No tests, no monitoring, no ownership. Fixes are manual firefighting, and the same failures recur.
- **Level 2, Managed:** Basic tests on critical tables (keys, nulls, accepted values) run in the pipeline. Some freshness and volume monitoring exists on the most important datasets. Incidents are handled reactively, but at least someone usually notices before the executive does.
- **Level 3, Defined:** Quality dimensions are measured with thresholds. Data contracts govern key producer boundaries. Observability covers freshness, volume, schema, and distribution on important tables, with lineage for impact analysis. Datasets have owners, and data incidents follow a defined severity and response process.
- **Level 4, Optimizing:** Quality and observability are pervasive and largely automated. Anomaly detection catches subtle drift, contracts are enforced mechanically, and lineage is captured automatically and published in a catalog. Data has service levels and on-call ownership like production services, reconciliation runs continuously, and blameless postmortems drive steady reduction in data downtime.

## Ideas for discussion

1. Which of your tables would cause the most damage if they were silently wrong for a week, and are those the ones you monitor most?
2. Where would a data contract have prevented your last upstream-caused incident, and why was there not one?
3. How much engineering time does a typical root-cause investigation take today, and how much would automated lineage save?
4. Are any of your machine learning models training on data you do not validate, and what errors might they be encoding?
5. Is your alerting tuned well enough that people act on every alert, or has anyone muted the channel?
6. What freshness and accuracy service levels would your most important consumers actually sign up to, and could you meet them today?

## Key takeaways

- Data quality is fitness for use across accuracy, completeness, consistency, timeliness, validity, and uniqueness.
- Bad data is worse than no data, because it corrupts decisions and models silently.
- Test data like code: assertion and expectation tests plus schema checks, in CI and in production.
- Use data contracts to make producer and consumer expectations explicit and enforceable.
- Observe freshness, volume, schema, and distribution, in parallel to software observability (chapter 9.2).
- Capture lineage for fast root cause and impact analysis, and publish it for consumers.
- Treat data incidents like production incidents, with ownership, severity, and service levels.
- Instrument where wrong data hurts most; aim for fit-for-use quality, not perfection everywhere.

## References and further reading

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
