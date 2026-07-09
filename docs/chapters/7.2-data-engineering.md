# 7.2 Data engineering

## Overview and motivation

[Data engineering](https://en.wikipedia.org/wiki/Data_engineering) is the discipline of building and operating the pipelines and platforms that move data from where it is produced to where it creates value. It covers ingestion from source systems, transformation into clean and modeled forms, storage in cost-effective formats, orchestration of the whole flow, and the reliability practices that keep it all trustworthy. If data strategy decides what data should exist and who owns it, data engineering is the plumbing and machinery that makes it flow.

For large teams, this discipline is foundational. Analytics, [business intelligence](https://en.wikipedia.org/wiki/Business_intelligence), product experimentation, [machine learning](https://en.wikipedia.org/wiki/Machine_learning), and regulatory reporting all sit downstream of data pipelines. When those pipelines are fragile, slow, or opaque, every dependent function suffers. Dashboards show stale numbers. Models train on corrupt features. Auditors cannot reconstruct how a figure was produced. At enterprise and government scale, pipelines process billions of records across many source systems, and a single silent failure can push wrong data into decisions, payments, or public statistics.

The field has grown up from bespoke scripts and monolithic [ETL (extract, transform, load)](https://en.wikipedia.org/wiki/Extract,_transform,_load) tools into the modern data stack: modular, largely SQL-driven components for ingestion, transformation, orchestration, and storage, connected by open formats. This modularity is both a gift and a trap. It lets you assemble best-of-breed tools, but without engineering discipline it produces a sprawl of undocumented, untested jobs. This chapter covers the practices that keep pipelines idempotent, testable, observable, and affordable at scale.

## Key principles

- Pipelines are software and deserve version control, testing, review, and CI/CD.
- Prefer idempotent, reproducible transformations that can safely re-run.
- Make data flows observable: freshness, volume, schema, and quality are monitored.
- Model data deliberately for its consumers rather than dumping raw tables.
- Choose batch or streaming based on real latency needs, not novelty.
- Optimize storage format, partitioning, and compute cost as first-class concerns.
- Separate ingestion, transformation, and serving so each can evolve independently.
- Fail loudly and early; a broken pipeline is safer than silently wrong data.

## Recommendations

### Choose ETL or ELT deliberately

ETL transforms data before loading it into the destination. [ELT (extract, load, transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) loads raw data first and transforms it inside a powerful warehouse or lakehouse. Modern cloud platforms have made ELT the default, because storage is cheap and compute is elastic, and keeping raw data lets you reprocess when logic changes or bugs turn up. Prefer ELT for analytics workloads: land raw immutable data, then build layered transformations on top. Save pre-load transformation for cases where privacy, cost, or contractual constraints require cleaning or filtering before the data lands.

### Design batch and streaming pipelines for their latency needs

Most analytics needs are well served by scheduled batch pipelines, which are simpler to reason about, test, and backfill. Reach for streaming only when the business genuinely needs low-latency data: fraud detection, operational alerting, real-time personalization. Streaming adds real complexity around ordering, exactly-once semantics, late-arriving data, and state management. Where you need both, consider architectures that unify batch and streaming logic rather than maintaining two divergent codebases. Be honest about your latency requirements. "Real-time" is often an unexamined wish that doubles your cost.

### Orchestrate with explicit dependencies

Use an orchestrator to express pipelines as [directed acyclic graphs (DAGs)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of tasks with explicit dependencies, retries, and scheduling. This gives you visibility into what ran, what failed, and what is blocked, plus the ability to backfill and rerun deterministically. Base dependencies on data availability, not just clock time, so downstream jobs wait for upstream data rather than firing on a guess. Keep orchestration logic in version control, and treat DAG changes like code changes.

### Model data for consumption

Raw tables are rarely fit for analysts. Apply [dimensional modeling](https://en.wikipedia.org/wiki/Dimensional_modeling), which arranges facts and conforming dimensions in [star schemas](https://en.wikipedia.org/wiki/Star_schema), where you need governed, reusable, self-service analytics. Wide denormalized tables ("one big table") can outperform for specific query patterns and are simpler for some consumers, at the cost of duplication and flexibility. Layer your transformations: a raw staging layer, a cleaned and conformed core layer, and consumer-facing marts. This separation lets you fix logic in one place, and it lets consumers depend on stable interfaces.

### Make pipelines idempotent and testable

Design transformations so that re-running them produces the same result, rather than duplicating or corrupting data, for example by using deterministic upserts keyed on business identifiers and partition-overwrite patterns. Write tests at multiple levels: unit tests for transformation logic, schema tests, and data tests that assert expectations such as uniqueness, non-null keys, referential integrity, and accepted value ranges. Run these in CI, so a bad change is caught before it reaches production data.

### Instrument observability and reliability

Monitor the four core signals of data health: freshness (is it up to date), volume (is the row count in the expected range), schema (has the structure changed unexpectedly), and distribution (have values drifted anomalously). Alert on breaches, and route them to the owning team. Keep runbooks, on-call rotations, and blameless postmortems for data incidents, just as you would for services. Track lineage, so that when something breaks, you can see the downstream impact right away.

### Optimize storage and cost

Use columnar open formats such as Parquet, or open table formats that support schema evolution, time travel, and efficient updates. Partition data by the columns you filter on most, typically date, and avoid a proliferation of tiny files by compacting. Separate hot and cold data with tiered storage and lifecycle policies. Monitor compute spend per pipeline and per query. Runaway costs usually come from full scans, missing partitions, and unbounded reprocessing. Treat cost as a metric with owners, not a surprise on the monthly bill.

## Trade-offs: pros and cons

| Choice | Pros | Cons | Best fit |
|---|---|---|---|
| ELT (transform in place) | Keeps raw data, cheap storage, reprocessable | Large storage footprint, governance needed | Cloud analytics |
| ETL (transform before load) | Controls cost, filters sensitive data early | Loses raw, harder to reprocess | Regulated or constrained loads |
| Batch | Simple, testable, easy backfill | Higher latency | Most analytics |
| Streaming | Low latency, real-time reaction | Complex, costly, hard to test | Fraud, ops alerting |
| Star schema | Governed, reusable, self-service friendly | Modeling effort upfront | Shared BI |
| Wide table | Fast for known queries, simple | Duplication, less flexible | Narrow high-performance use |

The dominant trade-off is simplicity versus latency and flexibility. Batch and ELT with layered star schemas give you a testable, backfillable, well-understood system that serves most needs affordably. Streaming, real-time, and highly denormalized designs buy speed and specific performance, but at a steep cost in operational complexity and testing difficulty. Adopt complexity only where a concrete business requirement pays for it, and keep the simple path as your default.

## Questions to discuss with your team

1. **Have you deliberately chosen ELT over ETL, and are you keeping raw immutable data so you can reprocess when logic changes or bugs surface?** The chapter's default is ELT: land raw data cheaply, then build layered transformations, because keeping raw lets you rerun everything when a rule changes or a bug appears weeks later. Deleting raw data forecloses that option and is a common, painful pitfall. The competing case for ETL is real in regulated or constrained loads, where privacy, cost, or contract terms require filtering or masking before data lands. Bring evidence: how often have you needed to reprocess history, and what did it cost when you could not? For a government or enterprise pipeline that must trace any figure to source, immutable raw records are also an auditability requirement, so the answer shapes both your storage policy and your legal defensibility.

2. **Which of the four data-health signals do you actually monitor, and who gets paged when one breaks?** The chapter names four signals worth watching: freshness, volume, schema, and distribution. Many teams monitor none of them and learn about failures from an executive staring at a stale dashboard, which is the worst possible detector. At enterprise and government scale, a single silent failure can push wrong data into payments, reports, or public statistics, so the cost of late detection is measured in trust and money, not just rework. Bring your real mean time to detect and the name of whoever currently finds incidents first. If the answer is "a consumer," you need alerting routed to the owning team plus runbooks and blameless postmortems, treating data incidents exactly like service outages.

3. **Do your analysts consume modeled, tested marts, or are you dumping raw tables on them and calling it self-service?** The chapter is direct: raw tables are rarely fit for analysts, and layering transformations into a raw staging layer, a conformed core, and consumer-facing marts lets you fix logic once and give consumers stable interfaces. The competing pull is speed, since modeling with star schemas or deliberate wide tables costs upfront effort and it is tempting to skip it. But dumping raw data pushes the modeling cost onto every analyst repeatedly, producing divergent numbers and wasted hours. Bring a signal: what share of analyst time goes to reshaping raw data, and how many teams have rebuilt the same joins. If the number is high, invest in a conformed core layer so consumers depend on tested, reusable interfaces instead of reinventing them.

## Examples

**Startup.** A ten-person analytics startup had grown a tangle of cron jobs that broke silently overnight and sometimes double-counted rows when an engineer reran one by hand. The team moved to a managed connector for ingestion, a transformation framework for version-controlled models, and a lightweight orchestrator that retries and backfills on its own. They made every model idempotent and added a handful of tests for null keys and row counts, so a bad source change now fails in CI instead of surfacing in the founder's Monday dashboard.

**Enterprise.** A global retailer replaced hundreds of hand-written extract scripts with an ELT stack. Managed connectors land raw source data, a transformation framework builds tested, version-controlled models in a lakehouse, and an orchestrator manages dependencies with retries and backfills. Data tests catch schema drift from source systems before it reaches dashboards. Partitioned columnar storage cut query costs substantially, while improving freshness from daily to hourly.

**Government.** A tax authority ingests filings and third-party data through a governed pipeline that lands immutable raw records for auditability, then transforms them in layered, tested stages. Idempotent processing lets them safely reprocess a filing period when a rule changes. Full lineage lets auditors trace any computed figure back to source documents, a legal requirement for public accountability.

## Business case: motivations, ROI, and TCO

The ROI of disciplined data engineering comes from reliability, speed, and cost control. Reliable pipelines mean decisions and reports rest on trustworthy data, so you avoid the expensive rework and reputational damage of wrong numbers. Modular, tested pipelines let teams ship new data products faster, compounding the value of every downstream analytics and ML investment. Optimizing storage and compute directly reduces the cloud bill, often by large margins once partitioning and query patterns are fixed.

The adoption cost includes platform tooling, engineering time to build tested modular pipelines, and the discipline of treating data as software. Weigh this against the cost of not adopting: fragile bespoke jobs that only their author understands, silent data corruption discovered by executives, ballooning cloud spend from full-table scans, and analysts blocked waiting on data. To leadership, frame data engineering as the foundation that makes analytics, BI, and AI trustworthy and affordable. Under-invest here, and you cap the return on every data initiative above it.

## Anti-patterns and pitfalls

- Pipelines built as one-off scripts with no version control, tests, or review.
- Non-idempotent jobs that duplicate or corrupt data when re-run after failure.
- Adopting streaming for prestige when batch would meet the latency requirement.
- Dumping raw tables on analysts and calling it self-service.
- No observability, so failures are discovered by downstream consumers.
- Ignoring partitioning and file sizing until the cloud bill explodes.
- Coupling ingestion, transformation, and serving so nothing can change safely.
- Deleting raw data, making it impossible to reprocess when logic changes.

## Maturity model

1. Initial: Ad hoc scripts, manual runs, no tests or monitoring. Failures found by consumers. Costs unmanaged.
2. Developing: Some orchestration and scheduling. Basic transformations in version control. Occasional tests. Reactive firefighting when pipelines break.
3. Managed: ELT with layered, tested, version-controlled models. Orchestrated dependencies with retries and backfills. Observability on freshness, volume, and schema. Costs tracked and partitioning optimized.
4. Optimizing: Pipelines treated fully as software with CI/CD, data contracts, and comprehensive testing. Proactive observability and automated anomaly detection. Cost and reliability owned with SLAs. Batch and streaming unified where needed, and new data products ship rapidly on a stable platform.

## Ideas for discussion

- Where in your stack does "real-time" actually earn its cost, and where is it wishful?
- Which pipelines could not be safely re-run today, and what would it take to fix that?
- How much of your cloud data bill comes from full scans and missing partitions?
- Do your analysts consume modeled marts or raw tables, and what does that cost them?
- What is your mean time to detect a data incident, and who finds it first?
- Would unifying batch and streaming logic reduce your maintenance burden or add risk?

## Key takeaways

- Treat pipelines as software: version control, tests, review, CI/CD, and observability.
- Prefer ELT with layered, tested models; keep raw data for reprocessing.
- Choose batch by default and streaming only where latency genuinely pays.
- Make transformations idempotent so re-runs are safe.
- Model data for consumers with star schemas or deliberate wide tables.
- Monitor freshness, volume, schema, and distribution, and treat data incidents like outages.
- Optimize storage formats, partitioning, and compute cost as first-class concerns.

## References and further reading

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
