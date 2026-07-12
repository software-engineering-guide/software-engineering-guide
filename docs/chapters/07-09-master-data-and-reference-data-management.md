# 7.9 Master data and reference data management

## Overview and motivation

Ask five systems how many customers the organization has, and you get five different numbers. One counts email addresses, one counts contracts, one counts logins, and two disagree about whether "Acme Corp" and "ACME Corporation" are the same company. [Master data management](https://en.wikipedia.org/wiki/Master_data_management) (MDM) is the discipline of reconciling the core entities your business shares, customer, product, supplier, employee, location, into one authoritative version every system can trust.

Start by sorting your data into three kinds, because they need different treatment. Master data describes the nouns of your business: the people, places, and things that many processes refer to. Reference data is the controlled vocabulary those processes use: currency codes, country codes, unit-of-measure lists, product categories. Transactional data records the verbs: an order placed, a payment made, a shipment sent. Master and reference data are lower-volume than transactions but referenced everywhere, so an error in them contaminates everything downstream.

The cost of getting this wrong is concrete. When the same customer exists as four slightly different records, you mail four catalogs, you cannot see one relationship worth keeping, and your revenue-per-customer number is quietly wrong. A [golden record](https://en.wikipedia.org/wiki/Single_source_of_truth), the single trusted version of an entity assembled from many sources, is what replaces those conflicting copies, so that every integration stops re-solving the same matching problem.

For enterprises reconciling systems accumulated through decades of growth and acquisition, MDM is the difference between a coherent customer view and a permanent reconciliation tax. For government, the stakes rise: a citizen who appears as three different people in three agencies may be denied a benefit, taxed twice, or lost between departments. This chapter complements data strategy and governance (chapter 7.1), which sets ownership and policy; data modeling and the semantic layer (chapter 7.7), which defines what entities mean; and data quality and observability (chapter 7.8), which keeps records clean over time.

## Key principles

- Sort your data into master, reference, and transactional; each needs different handling.
- One golden record per real-world entity, assembled deliberately, not discovered by accident.
- Choose an MDM architecture style to fit your control and latency needs, not fashion.
- Matching and survivorship are business rules, so write them down and let stewards tune them.
- Reference data is shared vocabulary; version it and publish it like an API.
- Governance and stewardship are the engine of MDM; the software is only the tooling.
- Propagate golden records as events so downstream systems stay in sync, not stale.
- Measure MDM by decisions improved and duplicates removed, not by records loaded.

## Recommendations

### Classify master, reference, and transactional data first

You cannot manage what you have not sorted, so begin by classifying your data domains. A useful test for master data is whether a wrong value propagates: if one bad address ripples into billing, shipping, and legal notices, you are looking at master data. This drives your investment: you build a matching engine for the customer entity, not order line items. Name the domains explicitly, rank them by how much pain their duplication causes, and start with the one or two that hurt most, usually customer and product because they touch revenue directly.

### Pick an MDM architecture style deliberately

There are four common architecture styles, and the right one depends on how much authority you can centralize and how quickly changes must propagate. The registry style leaves data in the source systems and builds only an index of matched identifiers, so it can answer "these five records are the same customer" without moving any data; it is cheap and low-risk, but read-only, so it cannot fix the sources. The consolidation style pulls copies into a central hub and merges them into golden records for reporting, but does not push corrections back, so the sources stay messy. The coexistence style goes further: it synchronizes cleaned values back to the source systems, so the sources improve over time while still operating independently. The centralized or transactional hub style makes the MDM hub the system of record itself, where entities are created and edited directly and every other system consumes from it; this gives the strongest consistency and control, and it is the hardest to adopt because it changes where work happens. Many organizations progress from a registry that proves value toward coexistence as trust grows, and run more than one style across different domains.

### Match, merge, and set survivorship rules explicitly

The heart of MDM is deciding when two records describe the same real-world thing. This is [record linkage](https://en.wikipedia.org/wiki/Record_linkage), rarely as simple as an exact key match because real data is full of typos, abbreviations, and missing fields. Deterministic matching uses exact rules on chosen fields (same tax ID, or same email plus postal code). Probabilistic matching scores similarity across many fields using [approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching) and weights, so "Bob Smith, 12 Main St" and "Robert Smith, 12 Main Street" can be judged a likely match above a threshold. Deciding which records refer to the same entity is called identity resolution, and it powers everything from customer views to fraud detection.

Once records match, you must decide which values survive into the golden record. These survivorship rules are business logic, so make them explicit: prefer the most recent value for a phone number, the most complete value for an address, the most trusted source for a legal name. Set a threshold band where matches are auto-merged, a lower band where they are auto-rejected, and a middle band where a human decides, which is where stewardship lives. Keep every merge reversible and logged, because a wrong merge that fuses two real customers is worse than a missed one.

### Treat reference data as versioned shared vocabulary

Reference data is the shared vocabulary your systems speak, and vocabulary that drifts causes silent misalignment: when one system uses ISO country code "GB" and another uses "UK," joins fail and counts diverge. Maintain each reference list in one governed place, publish it for every consumer, and, crucially, version it. Codes are added, retired, split, and merged over time, and if you overwrite the list in place, you break historical reports that were correct under the old codes.

Treat a reference dataset like an API with a contract. Publish it with effective dates so a consumer can ask "what were the valid region codes on this date," keep retired codes rather than deleting them, and record the mapping when a code changes meaning. Prefer recognized external standards where they exist, such as ISO country and currency codes, because standards give you interoperability for free and connect to the open-standards discipline in chapter 3.8.

### Model hierarchies and relationships, not just flat records

Master data is not a pile of independent rows; it is a web of relationships. A customer belongs to a household and to a corporate parent. A product rolls up into a category and a brand. These hierarchies carry real business meaning: roll up sales by corporate parent and the picture changes entirely from rolling up by individual account. Model these relationships explicitly so consumers traverse them consistently instead of each team inventing its own rollup.

Watch for the case where one entity needs several hierarchies at once. A product may roll up one way for finance and another for merchandising, and both are legitimate, so support multiple named hierarchies rather than forcing one true tree. Relationships between domains matter too, such as which supplier provides which product.

### Wire golden records into the semantic layer and data quality

The golden records MDM produces are the trustworthy entities that the semantic layer of chapter 7.7 references when it defines metrics: "active customers" means something only when "customer" is unambiguous. Feed your golden records into the semantic layer so every metric counts the same deduplicated, resolved entities.

MDM and data quality (chapter 7.8) are two sides of one coin: quality checks detect the duplicates, nulls, and format violations that MDM then resolves, and MDM's matching surfaces quality problems the checks missed. Run continuous quality monitoring on your master data specifically: duplicate rates, match confidence distributions, completeness of key fields, and the size of the review queue, so drift surfaces before consumers see it.

### Propagate golden records through events

A golden record that no downstream system sees helps no one. The strongest pattern is event-driven propagation: when an entity is created, merged, or corrected, the MDM hub publishes a change event, and subscribing systems update their local copy. This builds on [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture) and the streaming patterns of chapter 7.2, keeping dozens of systems consistent without brittle nightly batch syncs that leave everyone a day stale.

Publish the events with enough context to be useful: the entity identifier, what changed, the new surviving values, and a version so consumers can order updates and detect ones they missed. Make consumers idempotent so replaying an event does no harm, and offer an API for systems that cannot subscribe. The principle from data architecture and storage (chapter 3.4) applies: design for the golden record to flow, because one no one consumes is just an expensive spreadsheet.

### Assign stewardship and governance before tooling

MDM fails as a technology project and succeeds as a governance one. The critical role is the [data steward](https://en.wikipedia.org/wiki/Data_steward), a person accountable for the quality and rules of a specific domain, who resolves ambiguous matches, tunes survivorship rules, and arbitrates when two departments disagree about what "supplier" means. Stewards are usually business people with deep domain knowledge, not engineers, and they need real authority and time allocated, because part-time stewardship with no mandate produces exactly the drift MDM was meant to stop.

Wrap the stewards in the governance structures from chapter 7.1: a data owner accountable for each domain, a council to settle cross-domain disputes, and clear policies for who may create or merge master records. Document the decisions, because the rules for matching a customer are institutional knowledge that must survive staff turnover. Tooling serves the governance; buying an MDM platform before you name your stewards is buying an engine with no driver.

## Trade-offs: pros and cons

| MDM style | Pros | Cons |
|---|---|---|
| Registry (index only) | Cheap, low-risk, sources untouched | Read-only; cannot fix source data |
| Consolidation (central copies) | Clean records for analytics quickly | Sources stay messy; no writeback |
| Coexistence (sync back to sources) | Sources improve; balanced control | More integration; sync conflicts to manage |
| Centralized / transactional hub | Strongest consistency and control | Highest cost; changes where work happens |
| Deterministic matching | Predictable, explainable, auditable | Misses typos, variants, and messy data |
| Probabilistic matching | Catches real-world variation | Needs tuning; false merges if careless |

The central tension in MDM is control versus disruption. The styles that give you the cleanest, most consistent data (coexistence and centralized hubs) are exactly the ones that intrude most on how source systems and their owners work, and that intrusion is where MDM programs stall. The pragmatic path is to earn trust with a low-risk style and move toward stronger control only where the business case is clear. The matching trade-off runs parallel: deterministic rules are auditable but brittle, probabilistic scoring is powerful but demands stewardship and a tolerance for the occasional wrong merge. Most mature programs blend both.

## Questions to discuss with your team

1. **Which master data domains actually cause us pain, and have we ranked them by cost rather than treating them all at once?** Many MDM programs collapse under their own ambition, trying to master every entity in the enterprise at once and delivering nothing for two years. The productive move is to find the one or two domains where duplication and conflict cost you real money or trust, usually customer or product, and to quantify that cost: the wasted mailings, the reconciliation hours, the wrong revenue numbers, the audit findings. Bring concrete examples of the same entity appearing multiple ways across your systems, and let that ranking tell you where to start, because a narrow, measurable win builds the credibility you need to expand.

2. **Who owns each master data domain, and do our stewards have the authority and time to actually do the job?** MDM tooling without empowered stewardship is a car with no driver, and the most common failure mode is naming a steward on a slide while giving them no real mandate and no allocated hours. The people who resolve ambiguous matches and settle "what counts as a customer" disputes need domain expertise, decision authority, and protected time. Bring your org chart and ask, for your top domain, exactly who decides when two records are the same person and who arbitrates when sales and finance disagree. If you cannot name that person and point to their allocated time, you have found the gap that will sink the program.

3. **When we merge two records into a golden record, can we explain and reverse the decision, and where do the surviving values come from?** Survivorship rules are business logic that most teams have never written down, which means merges happen by accident of load order or tooling defaults, and a wrong merge that fuses two real customers is painful to unwind. Bring a real merged record and trace each surviving field back to its source and rule: why this address, why this name, why this phone number. Confirm that every merge is logged and reversible, and that a middle band of uncertain matches goes to a human rather than being auto-merged. If you cannot explain a specific golden record, your stewards cannot defend it to an auditor or a wronged customer.

## Examples

**Startup.** A fast-growing software company sells through both self-serve signup and a sales team, and the two channels create the same customer twice under slightly different company names. Revenue-per-account looks wrong and the sales team keeps cold-calling existing users. Rather than buy a heavy platform, they start with a lightweight registry: a matching job in their data warehouse that links records by email domain and normalized company name, with one part-time steward reviewing the uncertain matches weekly. It costs little, fixes the reporting error, and proves the value that justifies more investment as they grow.

**Enterprise.** A global manufacturer has grown through acquisition and runs a dozen ERP and CRM systems, each with its own supplier records, so the same supplier appears fifteen ways and the company cannot negotiate as one buyer or see its true spend. It stands up a coexistence-style MDM hub for the supplier and product domains, using deterministic matching on tax and registration identifiers plus probabilistic scoring on names and addresses. Named stewards in procurement tune the survivorship rules and work the review queue, and golden records are published as change events that flow back into every ERP so cleaned data improves the sources. Consolidated spend visibility unlocks better contract terms, and the reconciliation tax that consumed finance every quarter falls sharply.

**Government.** A national government wants agencies to treat a citizen as one person rather than a stranger at every counter, while respecting strict legal limits on data sharing. It builds a centralized master data hub for the person entity, keyed on a governed national identifier, with reference data versioned by effective date so historical records stay correct. Identity resolution is deliberately conservative: uncertain matches go to trained stewards rather than automated merges, because a wrong merge could deny someone a benefit or expose their data, and every match is logged for audit and appeal. The payoff is fewer duplicated records, less fraud from split identities, and a citizen who does not have to prove who they are at every door, within the interoperability standards of chapter 3.8.

## Business case: motivations, ROI, and TCO

The return on MDM comes from removing a tax that most organizations pay without naming it. Duplicate and conflicting records cost money in obvious ways (wasted marketing to the same person five times, shipping errors from stale addresses, missed volume discounts) and in less obvious ways (analysts reconciling counts, executives deciding on numbers that are quietly wrong, auditors billing hours to untangle which record is real). A consolidated supplier view frequently pays for the whole program through better contract terms alone.

The total cost of ownership has three parts: the platform or build, the integration to sources and consumers, and, largest over time, the ongoing stewardship. The integration cost is easy to underestimate, because connecting a dozen aging source systems is where MDM programs bleed schedule and budget, and the stewardship cost is easy to forget, because it is a permanent operating expense, not a one-time build. To make the case to leadership, tie MDM to numbers they already track: revenue accuracy, marketing efficiency, procurement savings, audit cost, and regulatory risk, then start narrow and let a measured win on one high-pain domain fund the expansion.

## Anti-patterns and pitfalls

- **Boil-the-ocean scope:** mastering every domain at once, delivering nothing for years, and losing sponsorship before the first win.
- **Tooling before governance:** buying an MDM platform before naming stewards and owners, so the engine has no driver.
- **Part-time stewards with no authority:** assigning stewardship on a slide while giving no real mandate or protected time.
- **Silent survivorship:** merging records by tooling default or load order, with no written rules and no way to explain a golden record.
- **Irreversible merges:** auto-merging uncertain matches with no undo, so a wrong fusion of two real entities becomes permanent damage.
- **Reference data overwritten in place:** editing code lists without versioning, breaking every historical report that was correct under the old codes.
- **Golden records no one consumes:** building a pristine hub that no downstream system subscribes to, so the clean data never reaches decisions.
- **Reinventing standard codes:** minting your own country or currency lists when ISO standards exist, and losing interoperability for no reason.

## Maturity model

- **Level 1, Initial:** Master and reference data are unmanaged. The same entity exists many times with no authoritative version, code lists diverge, matching is manual and ad hoc, and no one owns the problem, so counts of core entities disagree and no one can say which is right.
- **Level 2, Managed:** Key domains are recognized and someone deduplicates them, often in the warehouse for reporting. Basic matching exists, reference lists are collected, and a few people act as informal stewards, but the sources stay messy and rules are undocumented.
- **Level 3, Defined:** MDM is a governed program. Master domains have named owners and empowered stewards, matching and survivorship rules are written down, golden records are produced and propagated to consumers, and reference data is versioned and published.
- **Level 4, Optimizing:** Golden records flow as events in near real time, feed the semantic layer, and are trusted enterprise-wide. Matching is continuously tuned against measured outcomes, MDM value is quantified and reported, and the organization extends mastery to new domains as a repeatable capability.

## Ideas for discussion

1. If two of your systems disagree about how many customers you have, which one is right, and how would you prove it?
2. Which master data domain would deliver the biggest measurable win if you mastered it first, and what is that win worth?
3. Where would probabilistic matching help you today, and are you comfortable with the occasional wrong merge it implies?
4. How do you version your reference data, and what breaks in your historical reports when a code changes meaning?
5. Who is the named steward for your most important entity, and do they have the authority and time to actually do the job?
6. When a golden record changes, how do your downstream systems find out, and how stale can they be before it hurts?

## Key takeaways

- Sort your data into master, reference, and transactional; invest matching and governance where duplication costs most.
- Produce one golden record per real-world entity, assembled by explicit, reversible, logged survivorship rules.
- Choose an MDM architecture style (registry, consolidation, coexistence, or centralized hub) to fit your appetite for control and disruption.
- Treat reference data as versioned shared vocabulary, prefer recognized standards, and never overwrite code lists in place.
- MDM succeeds on governance and stewardship, not tooling; propagate golden records as events and measure the program by decisions improved.

## References and further reading

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
