# 7.7 Data modelling and the semantic layer

## Overview and motivation

A [data model](https://en.wikipedia.org/wiki/Data_model) is a decision about what your data means, made before you decide where the data lives. It names the things your business cares about, the attributes that describe them, and the relationships between them. Storage, indexes, file formats, and query engines all come later. This ordering matters because the meaning of your data outlives every technology you use to hold it. Warehouses get replaced, table formats change, and query engines come and go, but "customer," "order," and "active user" have to mean the same thing across all of them, for years.

For a small team, modelling is often implicit. One engineer holds the whole schema in their head, and a shared understanding of "revenue" survives because there are only three people to disagree. At the scale of large developer organizations, enterprises, and government agencies, that informality collapses in exactly the way described in chapter 7.1 (data strategy and governance). Dozens of teams build hundreds of tables, each with its own idea of what a "session" is or when a user counts as "active." Two dashboards show two different numbers for the same week, and a leadership meeting turns into an argument about whose query is right instead of what to do next. Bad modelling does not announce itself. It shows up months later as reconciliation work, failed audits, and decisions made on figures nobody can defend.

This chapter is about doing that work deliberately. It covers conceptual, logical, and physical models; entity-relationship modelling; when to normalize and when to denormalize; how modelling differs for transactional versus analytical workloads; dimensional modelling with facts and dimensions; and the semantic layer that holds the one governed definition of every business metric. The payoff is not elegance for its own sake. It is that "active user" and "revenue" mean one thing everywhere, so your teams can trust the numbers and move faster because of it.

*See also:* chapter 3.4 (data architecture and storage), chapter 7.3 (analytics and business intelligence), and chapter 11.5 (key performance indicators).

## Key principles

- Decide what data means before you decide where it lives.
- Model at three levels: conceptual (business), logical (structure), physical (implementation).
- Normalize to protect correctness in transactional systems; denormalize deliberately for analytical speed.
- Match the model to the workload: transactions and analytics have opposite needs.
- Every business metric has exactly one governed definition, and it lives in the semantic layer.
- Conformed dimensions let independent teams join and compare data safely.
- Grain is a design decision you make on purpose, not an accident of a query.
- Models are living assets: name them well, document them, and keep them evolvable.

## Recommendations

### Model at three levels, in order

Work from meaning outward. Start with a conceptual model: the entities your business cares about and how they relate, written in plain language a domain expert can check. "A customer places many orders; an order contains many line items; each line item refers to one product." No keys, no types, no tables yet. Then build a logical model that adds structure: attributes, primary and foreign keys, cardinalities, and constraints, still independent of any specific database. [Entity-relationship modelling](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) is the standard notation here, and an entity-relationship diagram is the artefact you review with both engineers and business stakeholders. Only then produce the physical model: the actual tables, columns, data types, indexes, partitions, and storage layout for your chosen engine. Skipping to physical design is the most common modelling mistake, because it bakes today's technology choices into decisions that should outlast them.

### Normalize transactional systems, denormalize analytical ones on purpose

For systems that record transactions, favour [database normalization](https://en.wikipedia.org/wiki/Database_normalization). Normal forms remove redundancy so that each fact is stored once, which prevents update anomalies and keeps writes correct when many users change data concurrently. This is the right default for [online transaction processing](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), where correctness under concurrent writes matters more than the speed of any single analytical query. Analytical systems have the opposite priorities. They are read-heavy, they scan and aggregate huge ranges, and joining dozens of normalized tables at query time is slow and hard to reason about. There you denormalize on purpose, collapsing related attributes together so queries are simpler and faster. The discipline is to denormalize deliberately, with a documented reason, rather than letting redundancy creep in by accident. Chapter 3.4 (data architecture and storage) covers the engines that make each pattern perform.

### Use dimensional modelling for analytics

For analytical workloads, adopt [dimensional modelling](https://en.wikipedia.org/wiki/Dimensional_modeling), the approach popularized by Ralph Kimball. You split the world into facts and dimensions. A fact table holds the measurements of a business process: the amount of a sale, the duration of a call, the quantity shipped. Dimension tables hold the descriptive context you filter and group by: the customer, the product, the store, the date. Arrange one fact table surrounded by its dimensions and you have a [star schema](https://en.wikipedia.org/wiki/Star_schema), which is easy for analysts to understand and fast for engines to query. Normalize those dimensions into sub-tables and you get a snowflake schema, which saves some storage at the cost of more joins and more complexity; prefer the star unless you have a concrete reason. For very large, highly regulated environments where auditability and source tracking dominate, a data vault approach models hubs, links, and satellites to capture history and lineage aggressively, at the cost of more tables and a steeper learning curve. Most teams should start with Kimball-style stars and reach for data vault only when the audit requirements justify it.

### Fix the grain and handle changing dimensions explicitly

Before you add a single column to a fact table, state its grain: exactly what one row represents. "One row per order line item." "One row per user per day." Grain is the foundation of a correct model, because every measure and every dimension either fits that grain or does not belong in the table. Mixing grains is how you get double-counted revenue. Then decide how dimensions change over time. A customer moves to a new city; do you overwrite the old value, keep a full history, or track only the current and prior value? These are the standard [slowly changing dimension](https://en.wikipedia.org/wiki/Slowly_changing_dimension) patterns, and choosing wrong means your historical reports quietly rewrite the past. Decide the grain and the change strategy up front, write them into the model's documentation, and hold the line in review.

### Build one semantic layer as the single definition of every metric

This is the recommendation that pays for the whole chapter. A [semantic layer](https://en.wikipedia.org/wiki/Semantic_layer) sits between your physical tables and every tool that consumes them, and it holds the one governed definition of each business metric. "Active user" is defined once, as code, with its exact logic: which events count, over what window, excluding which internal accounts. "Revenue" is defined once, including how refunds, discounts, and currency conversion are handled. Every dashboard, notebook, report, and reverse-ETL job reads that definition instead of re-implementing it in a bespoke query. When the definition changes, it changes in one place and every consumer updates together. This is the mechanism that makes governed metric definitions real rather than aspirational, and it is the direct implementation of what chapter 11.5 (key performance indicators) asks for. Treat metric definitions as versioned code with owners, review, and tests, exactly as chapter 7.1 asks you to treat data as a product.

### Establish conventions, naming, and documentation

Consistency is a feature. Adopt naming conventions and enforce them: a convention for table names, a convention for keys, a standard for date columns, a rule for how you mark a fact versus a dimension. Decide once whether you use singular or plural entity names and never mix them. Document each model where the people who use it will look: the meaning of every table, the grain of every fact, the definition of every metric, and the owner of each. Good naming and documentation are what let a new analyst self-serve instead of interrupting the team, and they are what let an auditor trace a number from a board deck back to its source without a guided tour.

### Keep models evolvable

Your model will change, so design for change. Add columns rather than repurposing existing ones. Use surrogate keys so that a change in a source system's natural key does not ripple through your warehouse. Version metric definitions and deprecate them with notice instead of silently altering them under running dashboards. Keep transformations in version control, tested, and reviewed, so a change to what "active user" means is a pull request with a diff and an approver, not a quiet edit in a BI tool. A model you cannot safely evolve becomes a model people route around, and shadow definitions are how the single source of truth dies.

## Trade-offs: pros and cons

| Approach | Pros | Cons | Best fit |
|---|---|---|---|
| Normalized (3NF) | Correct writes, no redundancy, flexible | Slow analytical joins, complex queries | OLTP and operational systems |
| Star schema (Kimball) | Fast, intuitive, analyst-friendly | Some redundancy, ETL to maintain | Most analytics and BI |
| Snowflake schema | Less storage, cleaner dimensions | More joins, more complexity | Large, tightly governed dimensions |
| Data vault | Full history, auditable, agile loads | Many tables, steep learning curve | Highly regulated, audit-heavy |
| Semantic layer over models | One definition everywhere, tool-agnostic | Upfront build, needs ownership | Multi-team, multi-tool orgs |

The central tension is speed of a single query against correctness and flexibility across the whole estate. Normalization protects correctness and pays for it in query complexity; dimensional models buy query speed and clarity and pay for it with ETL and some managed redundancy. There is no universal winner, which is why you match the model to the workload rather than picking a favourite. The semantic layer resolves the second tension, between many teams and many tools, by making the metric definition independent of any one of them. The mistake is treating these as ideological camps. A healthy organization runs normalized OLTP systems, dimensional analytical models fed from them, and one semantic layer on top, each doing the job it is good at.

## Questions to discuss with your team

1. **When two dashboards show different numbers for the same metric, whose definition wins, and where does that definition physically live?** This question exposes whether you actually have a single source of truth or just believe you do. In most large teams the honest answer is that "active user" is redefined in a dozen different queries, and the winner is whoever argues loudest in the meeting. Bring real evidence: pick one metric, find every place it is computed, and compare the logic line by line. You will almost certainly find silent disagreements about windows, exclusions, and edge cases. The answer should drive a decision to build a semantic layer where each metric is defined once, as reviewed code, so the question stops being about people and starts being about a versioned artefact. Until that definition has a single physical home, every reconciliation is temporary.

2. **What is the grain of your most important fact table, and can everyone in the room state it the same way?** Grain is the quiet foundation that most modelling failures trace back to. If half the team says "one row per order" and the other half says "one row per line item," you have a double-counting bug waiting to surface in a revenue report. Bring the actual table and ask each person to describe one row in a single sentence. Disagreement here is not a communication problem to smooth over; it is a design defect to fix before more measures pile on top of it. The answer should be written into the model's documentation and enforced in review, because once analysts build queries on an ambiguous grain, the ambiguity spreads faster than you can correct it.

3. **How will this model absorb change, and what happens to last year's reports when a definition shifts?** Every model faces changing source systems, changing business rules, and changing metric definitions, so the real question is whether change is a controlled pull request or a silent edit that rewrites history. Bring a recent example: a metric whose definition changed, or a source key that got renamed, and trace what happened to existing dashboards. If a slowly changing dimension was handled by overwriting, your historical reports may have quietly changed their past values, which is a serious problem for anyone doing trend analysis or regulated reporting. The answer should push you toward surrogate keys, versioned metric definitions, explicit change strategies, and transformations kept in version control with review. A model nobody can safely change becomes a model people abandon.

4. **Which dimensions must mean the same thing across every team, and who is accountable for owning each one?** Conformed dimensions are what let marketing, finance, and operations join their data and get comparable answers, but only when "customer," "product," "region," and "date" carry one agreed definition instead of a private copy per team. The competing pull is autonomy: each team wants to model its own world at its own pace, and forcing a shared dimension slows them down in the short term while paying off across the estate. Bring the two or three dimensions that show up in the most cross-team reports, list every version of each that exists today, and see how far their keys and attributes actually diverge. Name an owner for each conformed dimension, because a shared dimension with no owner drifts back into private copies within a quarter. In enterprise and government settings, where a figure from one department gets compared with another in public, an unconformed dimension is the difference between an honest comparison and an accidental falsehood, so decide early which dimensions are governed centrally and which stay local.

5. **Where does the boundary sit between your normalized transactional systems and your denormalized analytical models, and is every denormalization a deliberate decision?** Matching the model to the workload is the core discipline, yet the boundary is exactly where it blurs: an analyst denormalizes a warehouse table for speed, an engineer normalizes a reporting table out of habit, and nobody wrote down which side each choice belongs to. The tension is speed of a single query against correctness and flexibility across everything, and reasonable people land differently depending on whether they own writes or reads. Bring your slowest analytical query and your most contended transactional table, and ask for each redundant column whether its redundancy was chosen with a documented reason or crept in by accident. The goal is a written rule for when denormalization is allowed and who signs off, not a purity contest. For large or regulated organizations, this boundary also decides where personal data is duplicated, so an undocumented denormalization is both a performance question and a data-governance exposure that someone will eventually have to explain to an auditor.

6. **Should you build or buy the semantic layer, and who is accountable for keeping every metric definition current once it exists?** A semantic layer only delivers a single source of truth when it is owned and maintained, so the choice of tool matters less than the answer to who reviews a change to what "revenue" means and who is on the hook when a definition goes stale. The competing considerations are real: a build gives you control and fits your stack but adds an engineering burden, while buying a metrics tool is faster yet risks lock-in and a definition language you do not fully control. Bring your handful of highest-stakes metrics, the tools that consume them today, and an honest read on whether anyone currently owns those definitions or they simply exist. Decide up front whether definitions live as versioned code with named owners and tests, because a semantic layer nobody maintains rots into the same scattered definitions it was meant to replace. In enterprise and government reporting, where a metric on a public dashboard must be traceable to a documented, reviewed definition, that ownership and the ability to prove the lineage of a number is what turns the semantic layer from a convenience into an auditable control.

## Sector lens

**Startup.** Modelling can wait, but definitions cannot. With two engineers and no runway to build a warehouse, put one small semantic layer in your transformation tool and define the two or three metrics your board actually watches, "active user" and "revenue," once as tested code. Skip data vault and elaborate dimensional schemas; a thin star and a handful of governed definitions buy you consistent numbers without slowing delivery. The payoff is that board prep stops being an argument about whose query is right.

**Small business.** You have no data modeller and no budget for a metrics platform, so lean on the definitions built into the tools you already run and write down the few that matter in one shared document everyone reads. Favour buying analytics embedded in your existing software over standing up a warehouse you cannot staff. Where you do model, keep it simple and name things consistently, because the person maintaining it next year may be the one who cannot remember why "customer" meant two things. Consistency is cheaper than reconciliation.

**Enterprise.** The problem is many teams and many tools drifting into private definitions, so invest in conformed dimensions, one governed semantic layer, and metric definitions kept as versioned code with owners and review. Standardize naming, grain declarations, and slowly changing dimension strategies across the estate so a number in one tool matches the same number in another. Treat the semantic layer as a product with a roadmap and an owning team, and measure how much reconciliation time it removes. The return is trusted numbers across the business and audits that trace cleanly from a board deck back to source.

**Government.** Transparency and cross-agency comparability shape the work: canonical reference data for geography and demographics, governed definitions of core indicators, and published methodology with versioned releases so the public can trace any figure back to a documented definition. Procurement rules may require that your models and definitions stay portable and vendor-neutral, so avoid a semantic layer locked to one proprietary tool. Keep individual agencies free to model their operational data while conforming to shared dimensions for anything reported nationally. A published indicator that cannot be traced to a versioned definition is an accountability failure as much as a data one.

## Examples

**Startup.** A Series A company had three definitions of "active user" living in three places: the product analytics tool, the finance spreadsheet, and the investor deck. The numbers never matched, and every board prep turned into a scramble. Two engineers introduced a small semantic layer in their transformation tool, defining "active user" and "monthly recurring revenue" once as tested code, with the exact windows and exclusions written down. Every dashboard now reads those definitions. The board-prep argument disappeared, and onboarding a new analyst went from a week of tribal knowledge to reading one documented model. This connects directly to the discipline described in chapter 7.4 (product analytics and experimentation), where a stable definition of "active" is what makes experiment results comparable.

**Enterprise.** A global retailer ran five business-intelligence tools across marketing, finance, supply chain, merchandising, and stores, and each had reinvented "gross margin" slightly differently. They built one semantic layer on top of a Kimball-style warehouse with conformed dimensions, so that "product," "store," and "date" meant the same thing across every fact table and every tool. Each metric was defined once and consumed everywhere. Reconciliation meetings that used to eat days per quarter mostly vanished, and when finance changed how returns affected margin, the change propagated to all five tools at once. The conformed dimensions were what let independent teams join their data with confidence instead of suspicion.

**Government.** A national government needed comparable reporting across health, labour, and education agencies, each of which historically defined "household," "region," and "employment" its own way. A cross-agency body established shared reference data and standard definitions: canonical dimension tables for geography and demographics, and governed definitions of core indicators, published with methodology and versioned releases. Individual agencies model their own operational data but conform to the shared dimensions and definitions for anything reported nationally. The result is that a figure from one agency can be compared with another honestly, and the public can trace any published indicator back to a documented definition, supporting the transparency obligations covered in chapter 7.1.

## Business case: motivations, ROI, and TCO

The return on good modelling and a semantic layer is mostly recovered time and avoided error. In many organizations, analysts spend the majority of their time finding data, reconciling conflicting numbers, and rebuilding definitions other people already wrote. A single governed definition of each metric turns that repeated work into a one-time investment. It also removes an entire category of expensive failure: the wrong number in a board deck, the misreported figure that triggers an audit finding, the quarter-long reconciliation project that exists only because two teams defined "revenue" differently. When the definition lives in one reviewed place, those failures largely stop happening.

The cost is real and worth naming. You invest upfront in conceptual and logical modelling, in building and populating the semantic layer, and in the ongoing ownership that keeps definitions current. Total cost of ownership (TCO) includes the tooling, the modelling and analytics-engineering time, and the governance to keep the model from drifting. Weigh that against the cost of not doing it, which is larger but hidden: it shows up as duplicated pipelines, analysts as human reconciliation engines, and executives making confident decisions on figures no one can defend. Make the case to leadership in their terms. One trusted definition of every metric is what lets them compare across the business, trust the dashboards, and answer regulators without a fire drill. Start where the reconciliation pain is worst, define those few metrics once, and let the recovered time fund the rest.

## Anti-patterns and pitfalls

- Jumping straight to physical tables, baking today's technology into decisions that should outlast it.
- Defining the same metric independently in every dashboard, so no two numbers agree.
- Leaving grain unstated, then discovering double-counted measures in a revenue report.
- Denormalizing analytical tables by accident instead of by documented decision.
- Normalizing an analytical warehouse until every query is a twelve-table join nobody understands.
- Handling slowly changing dimensions by overwriting, so historical reports silently rewrite the past.
- Using natural keys everywhere, so a source-system key change ripples through the whole warehouse.
- Building a semantic layer with no owner, so definitions drift and trust erodes.
- Treating the model as done at launch instead of a living asset that must stay evolvable.

## Maturity model

- **Level 1, Initiate:** Modelling is implicit and reactive. Tables are designed physical-first by whoever needs them. Metrics are redefined in every report, and numbers routinely conflict. Grain is undocumented, and nobody owns the definitions.
- **Level 2, Develop:** Some analytical tables follow a dimensional pattern, and a few key metrics have written definitions, but they live in a wiki and are not enforced. Naming conventions exist on paper. Practice varies team by team, and reconciliation is still frequent and manual.
- **Level 3, Standardize:** Conceptual, logical, and physical models are distinct and reviewed. A semantic layer defines core metrics once, as versioned code with owners. Conformed dimensions let teams join safely. Grain and slowly changing dimension strategies are documented and enforced in review across the organization.
- **Level 4, Manage:** The model estate is measured against baselines. You track metric-definition coverage (the share of reported metrics served by the semantic layer), the count of duplicate or shadow definitions still in use, reconciliation hours spent per quarter, and the rate of grain and lineage defects caught in review versus in production. Definition changes flow through reviewed pull requests with tests, and freshness, test-pass rates, and drift are watched on dashboards. When a metric diverges or a dimension stops conforming, the measurement surfaces it before a board meeting does.
- **Level 5, Orchestrate:** Every important metric has one governed definition consumed by all tools and teams, and the semantic layer is integrated with analytics, experimentation, and regulated reporting. Models are evolvable by design and continuously refined; definitions are trusted organization-wide; reconciliation work has largely disappeared. The organization routinely deprecates, re-scopes, and conforms new dimensions as the business changes, rebalancing the model estate as an adaptive asset.

## Ideas for discussion

1. Pick your three most important metrics. How many distinct definitions of each exist across your tools today, and what would it take to collapse them to one?
2. Where has an unstated grain caused a real reporting error, and how long did it take to notice?
3. Which of your dimensions should be conformed across teams first, and who owns them?
4. Are your metric definitions in version control with review, or editable silently inside a BI tool?
5. When did a slowly changing dimension last rewrite your history without anyone noticing, and how would you catch it next time?
6. If you replaced your warehouse engine tomorrow, how much of your model's meaning would survive the move?

## Key takeaways

- Data modelling is deciding what data means, and that meaning outlives every storage technology you choose.
- Model at three levels in order: conceptual, then logical, then physical.
- Normalize transactional systems for correctness; denormalize analytical ones deliberately for speed.
- Use dimensional modelling with facts, dimensions, and a stated grain for analytics.
- Build one semantic layer so every business metric has a single governed definition everywhere.
- Conformed dimensions let independent teams join and compare their data with confidence.
- Name well, document, use surrogate keys, and version definitions so the model stays evolvable.

## References and further reading

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modeling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
