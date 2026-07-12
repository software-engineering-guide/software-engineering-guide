# 3.5 Scalability, performance, and resilience

## Overview and motivation

[Scalability](https://en.wikipedia.org/wiki/Scalability), performance, and resilience are three distinct qualities, and people often blur them together. **Performance** is how fast the system responds and how much work it does per unit of resource. **Scalability** is how well it maintains performance as load grows. **Resilience** is how well it keeps working, or degrades gracefully, when things fail. A system can be fast but unscalable (great at low load, collapses at high load), scalable but fragile (handles volume but falls over when one component fails), or resilient but slow. A large organization needs all three, designed in from the start, because retrofitting any of them after launch is expensive and disruptive.

For enterprise and government systems, the consequences of getting these wrong are public and severe. Think of a benefits portal that buckles on the first day of a new scheme, a tax filing system that times out at the deadline, or a payments platform that goes down during peak shopping. These are the failures that make headlines, trigger inquiries, and erode public trust. These systems also face highly peaked, often legally-timed load (filing deadlines, enrolment windows, paydays) and stringent availability and recovery obligations. You have to plan capacity for predictable surges, degrade gracefully under the unpredictable ones, and recover within defined time and data-loss limits after a disaster. This is engineering with a public accountability dimension.

This chapter covers horizontal versus vertical scaling, statelessness and [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) as enablers of scale, [load balancing](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [autoscaling](https://en.wikipedia.org/wiki/Autoscaling) and capacity planning, performance engineering with explicit budgets, resilience patterns and [chaos engineering](https://en.wikipedia.org/wiki/Chaos_engineering), and multi-region [disaster recovery](https://en.wikipedia.org/wiki/Disaster_recovery) framed by RTO, RPO, and business continuity. The unifying message is that these qualities are the product of deliberate design and continuous testing, not of hope.

*See also:* chapter 3.3 (distributed systems), chapter 9.1 (site reliability engineering), and chapter 9.2 (observability and monitoring).

## Key principles

- **Design for scale-out, not scale-up.** Vertical scaling has a ceiling and a [single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure); horizontal scaling is how you reach large, resilient scale.
- **Statelessness is the enabler of horizontal scale.** If any request can go to any instance, you can add and remove capacity freely.
- **You cannot improve what you do not measure.** Performance work is driven by profiling and load testing against explicit budgets, never by guesswork.
- **Everything fails; design for it.** Assume components will fail and build so the system survives their failure.
- **Graceful degradation beats hard failure.** A partially working system that sheds non-essential features is better than a total outage.
- **Capacity is planned, surges are absorbed.** Forecast predictable load; use autoscaling and headroom for the rest.
- **Recovery objectives are business decisions.** RTO and RPO are chosen by the business against cost, then engineered to.
- **Test resilience deliberately.** You do not know a system is resilient until you have made it fail on purpose.

## Recommendations

### Prefer horizontal scaling and design stateless services

Vertical scaling (bigger machines) is simple and sometimes the right first step, but it hits a hard ceiling, gets disproportionately expensive at the top end, and leaves a single point of failure. **Horizontal scaling** (more machines behind a load balancer) scales far further and improves availability, because losing one instance is survivable. The prerequisite is **statelessness**. Keep no client session or request state on the instance; push it to a shared store (database, cache, token). Stateless services can be added, removed, replaced, and load-balanced freely, which is what makes both autoscaling and rolling deployment possible. Where state must be partitioned, **shard** by a key that distributes load evenly and keeps related data on the same shard.

### Load-balance, autoscale, and plan capacity

Put a **load balancer** in front of every scaled tier to distribute traffic and route around unhealthy instances via health checks. Configure **autoscaling** to add capacity when a leading indicator (CPU, request queue depth, latency) crosses a threshold and remove it when load falls. Tune scaling speed and cooldowns so you neither lag behind a spike nor thrash. Autoscaling is not a substitute for **capacity planning**. For predictable, business-critical surges (tax deadlines, enrolment periods, sales events), forecast the load, pre-provision or pre-warm capacity, and load-test to that target in advance. Autoscaling alone cannot react instantly to a step-change, and cold starts add latency exactly when you can least afford it. Always keep headroom. Running at 100% leaves no room to absorb spikes or failures.

### Engineer performance against explicit budgets

Set **performance budgets** (concrete targets such as p95 API latency under 200 ms, page interactive under 2 seconds, or cost per transaction under a threshold) and enforce them in testing and monitoring so regressions fail the pipeline rather than reaching users. Drive optimization with **measurement**. Profile to find the actual bottleneck, which is rarely where you guess, and load-test to find where the system breaks and how it behaves near that limit. Focus on the critical path and the tail (p95/p99), because at scale the tail latencies dominate user experience. Optimize the biggest bottleneck first, re-measure, and stop when you meet the budget. Over-optimizing already-adequate code is wasted effort.

### Build in resilience patterns and validate with chaos engineering

Apply the resilience patterns from distributed systems: timeouts, bounded retries with backoff, [circuit breakers](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (which fail fast when a dependency is unhealthy), and bulkheads (which isolate resource pools so one failure cannot exhaust the rest), plus **graceful degradation** (shed or simplify non-essential features under stress: disable recommendations, serve cached content, queue non-urgent work) and **load shedding** (reject or throttle excess requests to protect the core rather than collapsing entirely). Eliminate single points of failure through redundancy at every tier. Then **validate** resilience with chaos engineering. Deliberately inject failures (kill instances, add latency, sever a dependency, fail a zone) in controlled experiments, starting in test and maturing to production game days, to prove the system behaves as designed. Resilience that has never been tested is only a hypothesis.

### Plan multi-region, disaster recovery, and business continuity

Decide the recovery objectives explicitly: **RTO** (Recovery Time Objective, how long you can be down) and **RPO** (Recovery Point Objective, how much data you can afford to lose). These are business decisions with direct cost implications, and they drive the architecture. Options range in cost and speed: backup-and-restore (cheapest, slowest), pilot light, warm standby, and active-active multi-region (most expensive, near-zero RTO/RPO). Choose the tier each system's criticality justifies. Not everything needs active-active. Replicate data across regions consistent with the chosen RPO, automate failover, and, above all, **test the failover regularly**. Untested disaster recovery reliably fails when it is finally needed. Wrap all of this in a **business continuity plan** covering people, communications, and manual fallbacks, not just technology.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| Vertical scaling | Simple, no code change, low initial effort | Hard ceiling, costly at top, single point of failure |
| Horizontal scaling | Near-unlimited scale, improves availability | Requires statelessness, load balancing, more ops |
| Autoscaling | Matches cost to demand, handles variable load | Reacts with lag; cold starts; can thrash if mistuned |
| Active-active multi-region | Near-zero RTO/RPO, survives regional loss | Highest cost and complexity, hard data consistency |
| Backup-and-restore DR | Cheapest, simplest | Long RTO, larger data loss window |

The central trade-off is cost versus assurance. Every increment of scalability headroom, performance, and recovery capability costs money and complexity, and the returns are non-linear. Going from 99.9% to 99.99% availability, or from an hour's RTO to seconds, can multiply cost. The discipline is to size each investment to the system's actual criticality and the business's tolerance for downtime and data loss, rather than reflexively engineering everything to the highest tier. A citizen-facing payments system earns active-active redundancy; an internal reporting tool does not.

## Questions to discuss with your team

1. **When your last serious incident happened, which of the three (performance, scalability, resilience) actually failed, and did you fix the right one?** The chapter separates them deliberately: a system can be fast yet collapse under load, scale yet fall over when one component dies, or survive failures while being slow. Teams often misdiagnose, adding capacity to a resilience problem or hardening a system that was simply under-provisioned for a surge. Walk through the last two serious incidents and name which quality broke and what the response actually improved. The distinction changes the fix: statelessness and sharding for scale, redundancy and circuit breakers for resilience, profiling and budgets for performance. Getting the category right is the difference between spending on the cure and spending on a symptom.

2. **Do performance regressions fail your pipeline, or do they reach users before anyone notices?** A performance budget (p95 latency, page-interactive time, cost per transaction) only protects users if it is enforced automatically, so a change that blows it fails the build rather than shipping. On a large team with many contributors, latency creeps in through a thousand small commits, and without a gate the tail slowly rots until a launch exposes it. Bring your current budgets and check whether they are wired into CI and monitoring, and whether they target p95 and p99 rather than averages, because the tail is what users feel at scale. Where no budget exists, setting one is the first move. Enforcement is what turns a good intention into a property that survives team growth.

3. **Under stress, what sheds first, and did you design that order or will you discover it in the outage?** Graceful degradation and load shedding mean the system gives up non-essential work to protect the core, but only if you have decided in advance what is essential. For a citizen-facing service that ranking is often a policy decision: submitting a tax return must survive even if status dashboards and historical lookups go dark. If no one has chosen, the system sheds whatever fails first, which may be the exact thing users need most. List your features in priority order and confirm the architecture can drop the low-priority ones (cached responses, disabled recommendations, queued non-urgent work) without taking the critical path with them. Then test it under real load, because untested degradation is only a hope.

4. **For your most critical system, what are the RTO and RPO, who actually chose those numbers, and when did you last prove you can meet them?** Recovery Time Objective (how long you can be down) and Recovery Point Objective (how much data you can afford to lose) are business decisions with direct cost implications, yet on a large team they are often invented by whoever wrote the runbook rather than owned by the people accountable for the service. The competing pull is cost against assurance: shrinking RTO from an hour to seconds or RPO from minutes to zero can multiply the infrastructure bill, so the right number is the one the business will actually pay for, not the most impressive one. Bring the documented objectives, the date of the last real failover test, and the measured time and data loss that test produced, because an untested objective is a wish. In enterprise and government settings these numbers may be set by statute, contract, or SLA, so name who signs off on them and whether the last rehearsal met the obligation or quietly missed it.

5. **For your biggest predictable surge, are you trusting autoscaling to react in the moment, or have you forecast the load, pre-provisioned, and load-tested to that target?** Autoscaling reacts with lag and cold starts add latency exactly when you can least afford it, so a known step-change (a filing deadline, an enrolment window, a sales event) is precisely the case where reactive scaling fails and deliberate capacity planning wins. The tension is cost: pre-warming capacity for a peak means paying for headroom that sits idle most of the year, and the temptation is to hope autoscaling covers it for free. Bring last year's peak numbers, this year's forecast with growth, and the results of a load test run to a multiple of that forecast rather than to today's average traffic. For a government or enterprise service facing a legally-timed surge, add the consequence of getting it wrong, since a benefits portal or tax system that buckles on day one becomes a public inquiry, not just a slow afternoon.

6. **Have you ever deliberately failed a component in production, and does each system's redundancy tier actually match its criticality and its cost?** Resilience that has never been tested is a hypothesis, and the tiers you can buy range from cheap backup-and-restore through warm standby to expensive active-active multi-region, so the discipline is spending assurance where it is justified rather than gilding everything or protecting nothing. The competing considerations are blast radius and budget: chaos experiments must have guardrails and an abort switch, and active-active for an internal reporting tool is waste while backup-only for a payments platform is negligence. Bring an inventory of your single points of failure, the redundancy tier of each critical system, and evidence of the last controlled failure injection and what it revealed. In enterprise and government portfolios, map each tier to a documented criticality rating so an auditor can see that the money follows the risk, and so nobody has to defend the spend for the first time during the outage.

## Sector lens

**Startup.** You cannot predict whether a launch brings fifty signups or fifty thousand, so buy scale rather than build it: run stateless services behind a managed load balancer and let the platform autoscale on request rate. Set one modest performance budget and pick managed data stores so a spike does not force a 2 a.m. re-architecture. Skip multi-region disaster recovery and chaos programmes for now; keep tested backups and spend your scarce engineering attention on the product, not on redundancy your traffic does not yet justify.

**Small business.** With no reliability specialist and a tight budget, the buy-versus-build choice tilts hard toward buy: a managed platform or serverless stack makes scaling and failover the provider's job, and a single well-run region is usually enough. Frame resilience as a small number of concrete promises you can keep, such as a nightly backup you have actually restored from once and a realistic recovery window you have communicated to customers. Avoid paying for active-active or continuous load testing you have neither the traffic nor the staff to warrant.

**Enterprise.** The problem is consistency across many teams: standardize performance budgets enforced in CI, a shared library of resilience patterns (timeouts, circuit breakers, bulkheads), and a documented redundancy tier for each system tied to its criticality. Reserve active-active multi-region for tier-one services, run a chaos engineering programme with guardrails and production game days, and treat capacity planning for known surges as a scheduled discipline rather than an afterthought. Govern RTO and RPO centrally so every critical system has owned, tested objectives an auditor can verify.

**Government.** Load is often legally timed and availability obligations are statutory, so capacity planning cannot rely on autoscaling reacting in the moment: forecast the deadline surge, pre-provision, and load-test well above forecast. Procurement should specify RTO, RPO, and a schedule of rehearsed failovers as contractual requirements, not vendor promises, and should avoid single-region lock-in for critical services. Decide in advance which path is legally essential (submitting a return, claiming a benefit) so degradation sheds status dashboards and lookups first, and be transparent with the public about outages and recovery rather than hoping no one notices.

## Examples

**Startup.** A small startup launching on Product Hunt cannot predict whether it will get fifty signups or fifty thousand, so it keeps its services stateless behind a managed load balancer and lets the platform autoscale on request rate. It sets one modest performance budget (pages respond under 300ms at the 95th percentile) and picks a managed database so a traffic spike does not force a 2 a.m. re-architecture. When the launch-day surge does arrive, the site slows a little rather than falling over, and the team spends the day talking to new users instead of fighting an outage.

**Enterprise.** A streaming media company runs stateless services across multiple regions behind global load balancing, autoscaling on request rate to follow the daily prime-time wave. Performance budgets gate every release on p99 startup latency. Under a regional failure, traffic shifts automatically to healthy regions, and non-essential features (personalized artwork, recommendation refresh) degrade first to protect playback. The company runs continuous chaos experiments in production, routinely terminating instances and injecting latency, so that real failures are indistinguishable from drills and cause no customer-visible outage.

**Government.** A tax agency knows its filing system faces a massive, legally fixed deadline surge each year. Rather than relying on autoscaling to react in the moment, it forecasts peak load from prior years, pre-provisions capacity weeks ahead, and load-tests to 150% of forecast. The architecture is stateless behind load balancers with a warm-standby second region. RTO and RPO are set by policy (no more than 15 minutes downtime and near-zero data loss for submitted returns), and failover is rehearsed quarterly. Under extreme load, non-critical features (status dashboards, historical lookups) shed first so that return submission, the legally essential path, stays available.

## Business case: motivations, ROI, and TCO

Scalability, performance, and resilience are classic cases where the cost of failure vastly exceeds the cost of prevention. But the prevention is visible on the budget and the failure is only potential, which is why they are chronically underfunded until the first disaster. The adoption cost is real: redundant infrastructure, multi-region capacity, load-testing and chaos tooling, and the engineering time to build statelessness and resilience patterns. The cost of *not* investing is a high-profile outage during peak demand: lost revenue by the minute for commerce, missed statutory obligations and public inquiry for government, [service-level agreement](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) penalties, and lasting reputational damage.

Frame the case to leadership with numbers the business already understands. Estimate the cost of one hour of downtime during peak (lost transactions, penalties, remediation, reputation), then compare it to the annual cost of the redundancy and testing that prevents it. For critical systems the prevention is almost always a fraction of a single major incident. Tie RTO and RPO to explicit money: how much revenue or how many transactions per hour of downtime, and how much data loss is legally or commercially tolerable. Present performance as a revenue and satisfaction lever, since faster systems convert better and cost less per transaction, and present resilience as insurance whose premium is small relative to the covered loss. The strongest argument is that these qualities are cheap to design in and ruinous to retrofit after the outage that forces the issue.

## Anti-patterns and pitfalls

- **Sticky sessions and in-instance state.** Storing session state on the server, preventing free horizontal scaling and safe instance replacement.
- **Autoscaling as capacity planning.** Assuming autoscaling will absorb a known step-change surge it is too slow to react to.
- **Running hot with no headroom.** Operating at near-100% utilization, leaving nothing to absorb spikes or failures.
- **Optimizing without profiling.** Tuning code that is not the bottleneck while the real one goes untouched.
- **Ignoring the tail.** Reporting average latency while p99 users suffer; averages hide the pain at scale.
- **Untested disaster recovery.** A DR plan and backups that have never been exercised and will fail when needed.
- **Single points of failure.** One load balancer, one database primary, one region: an unredundant component that takes everything down.
- **Chaos engineering without guardrails.** Injecting failures with no blast-radius control or abort switch, causing the very outage you meant to prevent.

## Maturity model

- **Level 1: Initiate.** Ad hoc and reactive. Single-instance or vertically scaled, with state held on the server. No load testing, no performance budgets, and no disaster recovery beyond occasional backups nobody has restored from. Any component failure causes a full outage, and scale problems are discovered in production.
- **Level 2: Develop.** Basic practices appear but vary team to team. Some services are horizontally scaled and stateless behind a load balancer, with basic autoscaling on a few of them. Load testing happens before big launches but not routinely, and backups exist while disaster recovery is documented but rarely exercised. What one team does well another has not started.
- **Level 3: Standardize.** Practices are documented and enforced org-wide. Capacity is planned for known surges with headroom, performance budgets are enforced in CI so regressions fail the build, and resilience patterns (timeouts, bounded retries, circuit breakers, bulkheads) plus graceful degradation are the default. RTO and RPO are defined per system, redundancy tiers are assigned by criticality, and disaster-recovery failover is tested on a regular schedule across teams.
- **Level 4: Manage.** The qualities are measured and controlled against baselines. Teams track p95 and p99 latency, error budgets, and utilization and headroom against forecast, and alert on breaches rather than discovering them at launch. Tested failover times are compared to the target RTO and RPO, degradation and load-shedding thresholds are validated with metrics, and go or no-go decisions on releases and capacity are driven by data. Where numbers drift from the baseline, the gap is visible and owned rather than hidden behind averages.
- **Level 5: Orchestrate.** Scalability, performance, and resilience are continuously improved and integrated across the organization. Active-active multi-region is used wherever criticality justifies it, chaos engineering runs continuously including production game days, and capacity forecasting feeds directly into planning and procurement. Resilience is validated on an ongoing basis, recovery objectives are consistently met and proven, and the architecture adapts as load patterns and the risk picture shift, tied into business continuity and risk planning.

## Ideas for discussion

1. Which of your services still hold state on the instance, and what prevents you from making them stateless?
2. For your most critical system, what are the RTO and RPO, who set them, and when did you last prove you can meet them?
3. Does autoscaling actually protect you against your biggest known surge, or are you relying on it to do something it cannot?
4. Where is your remaining single point of failure, and what is the plan to remove it?
5. Are you measuring and budgeting p99 latency, or hiding behind averages?
6. Have you ever deliberately failed a component in production? If not, how do you know your resilience works?

## Key takeaways

- Distinguish performance, scalability, and resilience; a large system needs all three, designed in from the start.
- Horizontal scaling and stateless services are the foundation of scale, availability, and safe deployment.
- Combine autoscaling with real capacity planning and headroom for predictable, business-critical surges.
- Drive performance with profiling and load testing against explicit budgets, focusing on the critical path and the tail.
- Build resilience with timeouts, circuit breakers, bulkheads, graceful degradation, and redundancy, then validate it with chaos engineering.
- Set RTO and RPO as business decisions, engineer DR to match each system's criticality, and test failover regularly.

## References and further reading

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
