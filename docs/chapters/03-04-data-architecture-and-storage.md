# 3.4 Data architecture and storage

## Overview and motivation

Data outlives code. Applications are rewritten every few years, but the data they manage (customer records, financial ledgers, benefit histories, health records) persists for decades. It is often the organization's most valuable and most regulated asset. Data architecture is the discipline of deciding how that data is modelled, where it is stored, how it is kept consistent, how it evolves, and how it is served fast enough at scale. For a large organization these decisions are foundational. Your choice of storage engines and data models constrains what the business can do, how fast it can move, and how much it costs, for the entire life of the system.

The stakes are highest in enterprise and government because of scale, longevity, and regulation. A bank's transaction store must never lose or double-count a cent. A government registry must retain records for statutory periods and prove their integrity to auditors. A health system must enforce fine-grained access and residency rules. At the same time, these organizations serve enormous read and write volumes and cannot afford to have every query hit a single [relational database](https://en.wikipedia.org/wiki/Relational_database). So data architecture has to reconcile correctness and durability with performance and scale, and do so while the schema keeps changing to meet new mandates.

This chapter covers the major storage paradigms and when to use each, the discipline of [polyglot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence), data modelling and the frequently underestimated problem of schema evolution and migration, [caching](https://en.wikipedia.org/wiki/Cache_(computing)) and [CDNs](https://en.wikipedia.org/wiki/Content_delivery_network) (content delivery networks) with the notoriously hard problem of invalidation, and how transactions, locking, and concurrency behave when you push them to scale. The through-line is simple: there is no universal database. There are trade-offs, and good data architecture means choosing them consciously, one workload at a time.

## Key principles

- **Model the data to fit the access patterns, not the other way around.** Design storage around how data will be read and written, not around an abstract "correct" model.
- **There is no one database to rule them all.** Different workloads want different engines; polyglot persistence is normal at scale.
- **Correctness first for systems of record.** For authoritative data, durability and consistency are non-negotiable; optimize performance around them, not through them.
- **Schema will change, so plan for it.** Migrations are a first-class, continuous engineering activity, not a one-off.
- **Own your data behind a service boundary.** Each bounded context (a self-contained domain model with its own explicit boundary) owns its data; sharing a database couples teams and destroys autonomy.
- **Caching is a correctness problem disguised as a performance win.** Every cache introduces staleness and invalidation risk; treat it deliberately.
- **Denormalization is a trade, not a sin.** Duplicating data for read performance is legitimate if you own the consistency consequences.
- **Consistency and scale trade off.** The stronger the transactional guarantee, the harder it is to distribute; buy only what the workload needs.

## Recommendations

### Choose the storage paradigm from the workload

Match each workload to the model that fits it. **Relational** databases give strong consistency, joins, and mature transactions; they are the default for systems of record and anything with complex integrity rules. **[Document](https://en.wikipedia.org/wiki/Document-oriented_database)** stores fit hierarchical, schema-flexible data read as a unit (a whole order, a whole profile). **[Key-value](https://en.wikipedia.org/wiki/Key-value_database)** stores give extreme speed for simple lookups (sessions, feature flags, caches). **[Graph](https://en.wikipedia.org/wiki/Graph_database)** databases excel where relationships are the query (fraud rings, org charts, entitlements, supply chains). **[Columnar](https://en.wikipedia.org/wiki/Column-oriented_DBMS)** stores power analytical queries scanning few columns over billions of rows (data warehouses, reporting). **[Time-series](https://en.wikipedia.org/wiki/Time_series_database)** databases optimize for append-heavy, timestamped data (metrics, telemetry, [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) sensors, market data). Resist forcing one engine to do every job. Using a relational database as a queue, or a document store as a ledger, invites pain.

### Adopt polyglot persistence deliberately

Large systems legitimately use several stores: a relational system of record, a search index, a cache, an analytics warehouse, and perhaps a graph or time-series engine. This is **polyglot persistence**, and it is the right pattern when workloads genuinely differ. The cost is operational, because you now have more engines to run, secure, back up, and staff. Manage that cost by treating each store as owned by a service, standardizing operational tooling, and keeping the number of technologies to those that earn their place. Be wary of adopting a new database for every minor need. Each one is a permanent operational commitment.

### Model data and treat schema evolution as continuous

Invest in data modelling up front for systems of record. Normalize to protect integrity, then denormalize selectively for proven read hot spots. Whatever the model, **schema evolves forever**, so make migrations safe and routine. Use versioned, automated, forward-only migration scripts checked into source control and applied through the deployment pipeline. For zero-downtime changes on large tables, use the **expand-contract (parallel change)** pattern: add the new column or table, backfill and dual-write, migrate readers, then remove the old shape. Never a single breaking alter. Make schema changes backward-compatible across deploys so old and new code run at the same time. In event-sourced or message-based systems, version your event and message schemas explicitly and support upcasting old events (transforming them to the current schema on read).

### Design caching and invalidation with eyes open

Caching and CDNs are the highest-leverage performance tools. A CDN serves static and cacheable content from the edge near users, and application caches spare the database from repeated reads. But the hard part is invalidation: knowing when cached data is stale. Choose a strategy per case. Use time-based expiry (TTL) where slight staleness is acceptable and simplest. Use explicit invalidation or write-through where freshness matters. Use cache-aside where the application manages population. Set TTLs consciously, guard against **cache stampedes** (many clients rebuilding the same expired entry at once) with locking or request coalescing, and prevent **thundering herds** on cold caches. Never cache data whose staleness could cause a correctness or compliance failure (entitlements, balances, consent) without an explicit, tested invalidation path. Treat cache keys, TTLs, and invalidation as designed artifacts, not incidental configuration.

### Manage transactions, locking, and concurrency for scale

Understand isolation levels and pick the weakest that is still correct for each transaction, because higher isolation costs concurrency. Prefer **[optimistic concurrency](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)** (version checks on write) for low-contention, read-heavy workloads, and reach for **pessimistic locking** only under genuine hot contention, keeping locks short and consistently ordered to avoid deadlocks. As you scale, a single writable database becomes the bottleneck. Introduce read replicas for read scaling (accepting replication lag), and **[shard](https://en.wikipedia.org/wiki/Shard_(database_architecture))/partition** by a key that spreads load evenly and keeps related data together to avoid cross-shard transactions. Remember that sharding trades away easy cross-shard joins and multi-shard [ACID](https://en.wikipedia.org/wiki/ACID) (Atomicity, Consistency, Isolation, Durability) transactions, which is often why sagas and denormalization appear. Push these techniques in only as the workload demands. Premature sharding adds permanent complexity.

## Trade-offs: pros and cons

| Store type | Best for | Strengths | Weaknesses |
|---|---|---|---|
| Relational | Systems of record, complex integrity | ACID, joins, mature tooling | Harder to scale writes horizontally |
| Document | Aggregate reads, flexible schema | Fast whole-object read/write, flexible | Weak cross-document joins/transactions |
| Key-value | Sessions, caches, simple lookups | Extreme speed and scale | No querying beyond the key |
| Graph | Relationship-heavy queries | Fast traversals, expressive | Niche ops skills, scaling limits |
| Columnar | Analytics, reporting | Fast aggregate scans, compression | Poor for row-level transactional writes |
| Time-series | Metrics, telemetry, IoT | Efficient append and time queries | Narrow purpose |

The dominant trade-off is consistency and rich querying versus horizontal scalability and speed. Relational systems give the strongest guarantees and the most flexible queries, but they are the hardest to scale writes across many machines. [NoSQL](https://en.wikipedia.org/wiki/NoSQL) (non-relational) families relax joins, transactions, or schema to gain scale and speed. Caching trades freshness for latency. Sharding trades cross-partition transactions for write throughput. None of these is universally right. The art is to place each workload on the point of the curve its correctness and performance needs actually require.

## Questions to discuss with your team

1. **For each critical dataset, can everyone name the one system of record, or do caches and projections quietly get treated as truth?** Data outlives code, and the most damaging data incidents come from drift: a cache, search index, or read projection is mistaken for authoritative and silently diverges from the real source. On a large team this happens when ownership is fuzzy and several services write overlapping copies, so no one can say which value is correct during an incident. Bring a map of your important data and, for each item, the single store that is authoritative plus the derived copies that must be rebuildable from it. In finance and government, being able to prove which record is the legal source and reconstruct the rest is often a regulatory requirement, not a convenience. Anything you cannot rebuild from the system of record is itself a system of record, whether you meant it to be or not.

2. **What does each database engine in your estate actually cost to run, secure, and back up, and does every one still earn its place?** Polyglot persistence is right when workloads genuinely differ, but each engine is a permanent operational commitment: patching, backups, monitoring, security review, and staff who know it at 3 a.m. A large organization can drift into a zoo of stores adopted for one feature each, and the marginal one adds cost forever while serving a workload a store you already run could handle. List every engine, the workload that justifies it, and who is on call for it, then flag any adopted for a need a primary store could now meet. New database adoption should clear a high bar, because removing one later means another migration. Standardizing operational tooling across the stores you keep is how you hold the cost down without forcing one engine to do every job.

3. **Where can a user read a stale value from a replica right after their own write, and does that break a promise you made them?** Read replicas scale reads but lag the primary, so a user who updates a profile and immediately reloads can see the old value, which reads as a bug or, for a balance or consent flag, a compliance failure. Decide per flow whether read-your-writes matters, and route those reads to the primary or use a session-consistency mechanism. Bring the list of flows served from replicas and mark which ones a user acts on immediately after writing. For balances, entitlements, and consent, treat stale reads as correctness failures, not cosmetic ones. The point is to buy the consistency each workload actually needs, and to make the staleness you do accept explicit rather than accidental.

4. **Can you change the schema of your largest, busiest table today without downtime, and who has actually rehearsed the expand-contract steps?** Schema evolves forever, and the failure that hurts most is a big-bang alter that locks a huge table, freezes the service, and cannot be rolled back cleanly. On a large team the risk multiplies because several services read the same shape, so a breaking change needs old and new code to run side by side across a staged deploy. The competing pull is speed: a single alter is quick to write, while expand-contract (add the new shape, backfill, dual-write, migrate readers, drop the old shape) is more steps and more patience. Bring your biggest table, an honest estimate of how long a naive alter would lock it, and a specific migration someone has run end to end in a rehearsal rather than in theory. In enterprise and government systems that run continuously and carry statutory availability targets, downtime for a migration is a breach, so the expand-contract discipline is the price of being allowed to change the schema at all.

5. **Which cached or replicated values, if served stale, would cause a compliance or safety failure rather than a cosmetic one, and is every one of those invalidation paths tested?** Caching is a correctness problem wearing a performance costume: the danger is not slowness but serving an entitlement, balance, consent flag, or access decision after it changed. For a large organization the hazard is diffuse, because caches and edge layers accumulate across teams and no single person can list what is cached where or when it clears. The tension is real: aggressive caching and long TTLs buy latency and protect the database, while strict freshness costs both. Bring an inventory of cached and CDN-served data, marked for which entries carry a compliance or safety consequence, plus evidence that the invalidation path for each of those has been exercised in practice rather than merely configured. In regulated and public settings, a stale consent or eligibility value is an auditable failure, so those items need an explicit, tested invalidation path or they should not be cached at all.

6. **What is your retention, archival, and data-residency strategy for each authoritative store, and can you prove it to an auditor?** Data outlives code and often outlives the team that wrote it, so unbounded growth and vague residency rules quietly become the problem no one owns until a table is unmanageable or a record sits in the wrong jurisdiction. A large organization spans many stores and regions, and the competing considerations are cost (hot storage is expensive, so archive and tier), performance (bloated tables slow everything), and legal duty (statutory retention floors and residency ceilings that can conflict). Bring, per authoritative dataset, the retention period, where the data physically lives, the archival and deletion mechanism, and the name of the person accountable for it. For enterprise and especially government systems, retention and residency are usually legal mandates with audit and sovereignty requirements, so being able to prove where each record lives, how long it is kept, and when it is destroyed is a licence to operate, not a nicety.

## Sector lens

**Startup.** Run one database and resist the zoo. A single managed relational store gives you transactions, one thing to back up, and one place to reason about consistency, which is exactly what a three-person team can afford to hold in its head. Add a cache, a read replica, or a search index only when a specific slow query or real read volume forces it, so complexity arrives with a paying reason. Keep migrations versioned from day one, because retrofitting migration discipline onto a live product is far harder than starting with it.

**Small business.** You have no database specialist and no time to operate several engines, so favour a managed store and let your platform provider handle backups, patching, and replication. Treat store selection as a buy decision: pick the boring, well-supported engine your tools already integrate with rather than the fastest one on a benchmark. Set a simple retention and backup policy you can actually verify, and never cache anything tied to money or permissions without a clear way to clear it, because a stale price or entitlement costs you a customer.

**Enterprise.** The core challenge is polyglot persistence across many teams: a relational system of record plus search, cache, warehouse, and perhaps graph or time-series engines, each owned by a service rather than shared. Standardize operational tooling, backup, and monitoring across the stores you keep, hold new-engine adoption to a high bar, and make expand-contract migrations and explicit cache invalidation the default. Manage the estate as a portfolio with clear data ownership, so no engine survives past the workload that justified it and no team is coupled through a shared database.

**Government.** Data residency, statutory retention, and provable integrity shape every choice. Provision every store in sovereign regions, configure CDNs to cache only non-personal data, and keep an immutable audit history for records that must be reconstructable for regulators. Migrations mandated by new legislation have to be applied backward-compatibly through the pipeline so the service stays available through legislative deadlines, and the system of record must be identifiable so you can prove which value is the legal source and rebuild every derived copy from it.

## Examples

**Startup.** A seed-stage startup runs everything on a single managed PostgreSQL instance and resists the urge to add a separate search engine, cache, and warehouse before it needs them. One database means one thing to back up, one place to reason about consistency, and transactions that just work, which matters when the whole team is three engineers. They add a Redis cache and a read replica only when a specific slow query and real read volume justify it, so complexity arrives with a paying reason rather than ahead of one.

**Enterprise.** A retail bank keeps its authoritative ledger in a strongly consistent relational database: every posting is a proper ACID transaction, sharded by account range for write scale. Around it sits a polyglot estate: a search index for customer lookup, a Redis cache (write-through, short TTL) for account summaries on the mobile app, a columnar warehouse for regulatory and analytical reporting, and a graph database for transaction-network fraud detection. Schema changes to the ledger use expand-contract with dual-writes so the 24/7 system never takes downtime for a migration.

**Government.** A national vehicle registry stores authoritative records in a relational system of record with statutory retention and full audit history. Public-facing "check a vehicle" lookups are served from a read replica and an edge cache with a short TTL, because slightly stale public data is acceptable and the read volume dwarfs writes. Data residency law requires all records to remain in-country, so every store is provisioned in sovereign regions and the CDN is configured to cache only non-personal data. Migrations to add new fields mandated by transport policy are applied backward-compatibly through the pipeline so the service stays available during legislative deadlines.

## Business case: motivations, ROI, and TCO

Data architecture decisions have among the longest and largest cost tails in software, because data and its schema are the hardest things to change once systems and integrations depend on them. The adoption cost of good practice (deliberate store selection, disciplined migrations, designed caching, and appropriate sharding) is mostly senior engineering time and some additional operational tooling. The cost of *not* adopting it shows up as a single overloaded database throttling the whole business, emergency re-platforming when the wrong store is discovered too late, extended outages from a botched migration, and, most damaging, data corruption or a compliance breach from a mis-invalidated cache or a lost transaction.

Make the case to leadership in terms of scalability headroom, incident risk, and regulatory exposure. The right storage choices are what let the business grow read and write volume without a rewrite. Disciplined migrations are what let the schema keep pace with new mandates without downtime. Correct caching is what delivers fast user experiences without silent staleness bugs. Quantify the TCO over the system's life. A single well-chosen data architecture avoids the recurring cost of working around a poor one, and one prevented data-corruption incident typically dwarfs the entire cost of doing it well. In regulated sectors, the ability to prove data integrity and residency is not a cost centre but a licence to operate.

## Anti-patterns and pitfalls

- **Shared database across services.** Multiple services reading and writing one schema, coupling teams and making every change a coordination crisis.
- **One database for everything.** Forcing analytics, queues, search, and transactions onto a single relational engine until it collapses.
- **Big-bang migrations.** Single breaking schema changes that require downtime and cannot be rolled back safely.
- **Caching without invalidation strategy.** Stale data served indefinitely, or correctness bugs because no one owns when the cache clears.
- **Premature sharding.** Distributing data before the load requires it, permanently losing joins and transactions for no benefit.
- **Ignoring replication lag.** Reading your own write from a lagging replica and getting stale data, breaking user expectations.
- **Unbounded data growth.** No archival or retention strategy, so tables grow until performance and cost become untenable.
- **Storing derived data as truth.** Treating a cache, index, or projection as the system of record, then discovering it drifted.

## Maturity model

- **Level 1: Initiate.** One database is used for every purpose. Schema changes are manual and ad hoc, with no migration discipline. Caching is incidental and invalidation is an afterthought. Performance problems are solved reactively by buying a bigger machine, and no one can reliably name the system of record for a given dataset.
- **Level 2: Develop.** Some storage choices are deliberate and a cache or warehouse has appeared, but practice varies by team. Migrations are versioned yet sometimes require downtime, and expand-contract is used by whoever happens to know it. Several services still share a database, and caching strategies differ from one team to the next.
- **Level 3: Standardize.** Polyglot persistence is matched to workloads, each store owned by a service and never shared. Automated, backward-compatible, zero-downtime expand-contract migrations are the documented, enforced standard org-wide. Caching strategies, TTLs, and invalidation paths are explicit design artefacts, and the single system of record for each dataset is documented, with derived copies rebuildable from it.
- **Level 4: Manage.** The data estate is measured and controlled against baselines. You track migration duration and rollback rate, replication lag against read-your-writes requirements, cache hit ratio and staleness incidents, per-store operational cost, and query latency at target percentiles, then act on the numbers. Retention and residency are audited against statutory requirements, correctness of derived data is verified continuously, and every engine must justify its cost against the workload it serves.
- **Level 5: Orchestrate.** Data architecture is continuously improved and integrated with capacity, cost, and risk planning across the organization. Sharding, caching, and consistency choices are rebalanced per workload as access patterns and cost shift, and stores that no longer earn their place are retired through planned migrations. Schema evolution, archival, and residency are fully automated and adaptive, so the estate reshapes itself to new mandates and load without emergency re-platforming.

## Ideas for discussion

1. Which of your current stores are doing a job they were not designed for, and what would the right engine be?
2. Can you perform a schema change on your largest table today with zero downtime? If not, why not?
3. Where does your system cache data whose staleness could cause a compliance or correctness failure?
4. Which services share a database, and what would it take to give each its own?
5. Where is a single writable database your scaling ceiling, and is read-replication or sharding the right next step?
6. What is your retention and archival strategy, and who is accountable for it?

## Key takeaways

- Data outlives code; storage and modelling decisions constrain the business for the system's entire life.
- Match each workload to the storage paradigm that fits its access pattern; expect polyglot persistence at scale.
- Give each service ownership of its data; never couple teams through a shared database.
- Treat schema evolution as continuous and use backward-compatible, zero-downtime expand-contract migrations.
- Caching is a correctness problem: design TTLs, invalidation, and stampede protection deliberately, and never cache compliance-critical data without a tested invalidation path.
- Buy only the consistency and transactional guarantees each workload needs; sharding and replication trade cross-partition transactions for scale.

## References and further reading

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Pramod Sadalage and Martin Fowler, *NoSQL Distilled*
- Pramod Sadalage and Scott Ambler, *Refactoring Databases: Evolutionary Database Design*
- C. J. Date, *An Introduction to Database Systems*
- Joe Celko, *SQL for Smarties*
- Vlad Mihalcea, *High-Performance Java Persistence* (transactions, isolation, concurrency)
- Eric Evans, *Domain-Driven Design* (bounded contexts and data ownership)
- Werner Vogels, "Eventually Consistent"
