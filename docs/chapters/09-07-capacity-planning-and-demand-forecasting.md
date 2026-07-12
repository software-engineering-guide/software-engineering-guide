# 9.7 Capacity planning and demand forecasting

## Overview and motivation

Every system has a ceiling. Compute cores run out, disks fill, connection pools exhaust, and a queue that was empty at breakfast overflows at lunch. Capacity planning is the discipline of matching the supply of compute, storage, and network to the demand you expect, with enough headroom that a normal day never comes close to the ceiling and a bad day fails gracefully rather than catastrophically. Demand forecasting is the other half: predicting how much load is coming, when, and why, so that supply arrives before the demand does rather than after the outage.

This chapter sits between two neighbors and stays complementary to both. Chapter 3.5 covers scalability as an architectural property: how a system is built so it can grow at all, through statelessness, sharding, and horizontal scaling. Chapter 9.1 covers site reliability engineering (SRE), which sets the reliability targets that capacity must defend. Here you take the architecture as given and the targets as fixed, then answer a quantitative question: how much of everything do you need to buy, reserve, and hold in reserve so the system meets its service level objectives (SLOs, the reliability targets from chapter 9.1) through forecast demand and the spikes you did not forecast. Autoscaling and performance engineering (chapter 2.16) are tools you use here, but they are not substitutes for planning, and confusing them for planning is a common and expensive mistake.

For large teams, capacity stops being a spreadsheet an engineer keeps and becomes a shared model that many services depend on. A platform of hundreds of services shares finite pools: database connections, message-broker throughput, cloud account quotas, network egress. One team's growth can starve another's if nobody holds the whole picture. In enterprise settings, capacity errors show up as either wasted millions in idle infrastructure or embarrassing outages during the exact moments that matter most. In government, the stakes sharpen further. A tax deadline, a benefits enrollment window, or a public health registration drive concentrates a nation's demand into a few hours, the load is legally mandated rather than optional, and the public remembers a site that buckled under a deadline it set itself. Capacity planning is how you keep those promises.

## Key principles

- Plan capacity for forecast demand plus deliberate headroom; do not run near saturation.
- Separate capacity planning, autoscaling, and performance engineering; each solves a different problem.
- Forecast from trend, seasonality, known events, and business growth, not from last week alone.
- Find your real limits by load testing and benchmarking, not by guessing or by waiting for production to find them.
- Treat latency near saturation as a cliff, not a slope; utilization targets exist because of queueing theory.
- Know your hard bottlenecks: connection pools, quotas, and single points do not autoscale.
- Balance cost against reliability on purpose, and review capacity on a regular cadence rather than after an incident.

## Recommendations

### Separate capacity planning, autoscaling, and performance engineering

These three disciplines are often confused, and confusing them leads to buying the wrong fix. Capacity planning is the medium-to-long-term question of how much total resource you must provision, reserve, and budget for over weeks, quarters, and years. [Autoscaling](https://en.wikipedia.org/wiki/Autoscaling) is the short-term, automated adjustment of resources to track load minute by minute: it moves you within the envelope that planning provisioned, but it cannot conjure quota you never reserved, warm a cold database, or scale a component that only runs as a single instance. Performance engineering (chapter 2.16) changes the shape of the problem by making each unit of work cheaper, so the same hardware serves more demand.

The distinction is practical. When a system is slow under load, autoscaling adds instances, performance engineering makes each instance faster, and capacity planning decides whether you can afford the instances and whether the downstream database can accept the connections they will open. A team that reaches only for autoscaling will hit a hard limit it never planned for; a team that reaches only for performance engineering will optimize code while the account quota caps them regardless. You need all three, and you need to know which one a given problem calls for.

### Forecast demand from trend, seasonality, events, and business growth

A forecast built on last week's average will miss every interesting moment. Build yours from four distinct components. The trend is the underlying direction: is demand growing, flat, or shrinking, and how fast? [Seasonality](https://en.wikipedia.org/wiki/Seasonality) is the repeating pattern: the daily peak at 9 a.m., the weekly lull on weekends, the annual surge before the holidays. Event-driven spikes are the one-off concentrations: a product launch, a marketing campaign, a television mention, a government filing deadline. Business-driven growth is the demand your own roadmap creates: a new market, a large customer onboarding, a feature that triples requests per session.

Use the right technique for each. A [time series](https://en.wikipedia.org/wiki/Time_series) of historical load, decomposed into trend and seasonality, gives you a defensible baseline for steady demand. Events cannot be extrapolated from history because they have no history; they come from talking to the business, reading the roadmap, and asking marketing and product what they are about to launch. The most damaging capacity failures are almost always events that engineering never heard about. The cure is organizational, not statistical: a standing channel where product, marketing, and operations declare upcoming spikes far enough ahead to provision for them.

### Set utilization targets and respect the queueing-theory cliff

The instinct to run infrastructure "hot" at 90% utilization to save money is a trap, and the reason is [queueing theory](https://en.wikipedia.org/wiki/Queueing_theory), covered in depth in chapter 11.3. As a resource approaches full utilization, waiting time does not rise gently and linearly; it explodes. A server at 50% utilization has comfortable headroom; the same server at 90% can see latency several times worse, and at 95% the queue can run away entirely. Latency near saturation is a cliff, not a slope, and your users feel the cliff as timeouts, retries, and errors long before the resource is technically "full."

This is why capacity planners set utilization targets well below 100%, commonly in the 50% to 70% range for latency-sensitive services, higher for throughput-oriented batch work that tolerates queueing. The target is not waste; it is the price of predictable latency. Pick the target from the SLO: if your latency objective is strict, your utilization ceiling is lower, because the tail latency that queueing produces is exactly what blows an SLO. Headroom and safety margin are the same idea from two directions. Headroom is the gap between normal load and capacity; safety margin is that gap expressed as insurance against a forecast that runs high, a failover that concentrates load, or a spike you did not see coming.

### Find real limits through load testing and benchmarking

You cannot plan around a limit you have not measured. [Load testing](https://en.wikipedia.org/wiki/Load_testing) drives synthetic or replayed traffic at a system to observe how latency, throughput, and error rate behave as load rises, and where they break. Benchmarking measures a component in isolation to establish its ceiling: requests per second per instance, writes per second per database node, messages per second per broker partition. Together they tell you the two numbers planning needs: how much a unit of capacity delivers, and where the whole system falls over.

Run several distinct tests. A load test ramps to expected peak and confirms the SLO holds with headroom. A stress test pushes past the breaking point to see how the system fails, because a system that degrades gracefully is very different from one that collapses. A soak test holds moderate load for hours or days to expose memory leaks, connection exhaustion, and disk-fill problems that only appear over time. A spike test slams load on suddenly to check whether autoscaling and buffers absorb it before users notice. Test against production-like data and topology, because a limit measured on a toy dataset lies. Rerun these tests when the system changes, so your numbers describe the system you have rather than the one you had a year ago.

### Choose provisioning strategies deliberately

Cloud providers let you buy the same capacity in ways that trade price against flexibility, and mixing them well is where real money is saved. On-demand capacity is flexible and expensive: you pay full rate for the ability to start and stop anytime, which suits unpredictable and short-lived load. Reserved capacity (commitments of one or three years, or savings plans) is cheaper per unit in exchange for a promise to keep using it, which suits your stable baseline. [Spot instances](https://en.wikipedia.org/wiki/Spot_instance) sell spare capacity at a deep discount but can be reclaimed with little warning, which suits fault-tolerant, interruptible work such as batch processing and stateless workers.

The pattern that works is layered. Cover your steady baseline with reserved capacity for the lowest unit cost, absorb daily and weekly variation with on-demand autoscaling, and push interruptible batch work onto spot to harvest the discount. Keep a warm buffer pool of pre-provisioned capacity for services that cannot tolerate the cold-start delay of scaling from zero, so a sudden spike meets ready capacity rather than a queue while new instances boot. The right blend is a portfolio decision, and it shifts as your demand shape and the provider's pricing change, so revisit it.

### Map hard bottlenecks that will not autoscale

Autoscaling breeds a dangerous confidence, because plenty of limits sit downstream of the thing that scales and do not move when it does. Database [connection pools](https://en.wikipedia.org/wiki/Connection_pool) are the classic example: scale your stateless tier from 10 to 100 instances and each opens connections to the same database, which has a hard cap on concurrent connections and will start refusing new ones. Cloud accounts carry quotas on almost everything: instances per region, IP addresses, API calls per second, function concurrency. Any single point of the architecture, a primary database, a leader node, a shared cache, a licensed appliance, is a ceiling that horizontal scaling elsewhere cannot raise.

Make these explicit. Keep a written inventory of every hard limit between a request and its response: pool sizes, quota values, single-instance components, third-party rate limits, license seat counts. For each, record the current value, current usage, and the load at which it binds. This inventory is the difference between a capacity plan that describes the whole system and one that describes only the easy, elastic parts while a connection pool quietly waits to end your launch. Raise quotas ahead of need, because provider quota increases can take days to approve.

### Provision for peak events, not just the average

Averages hide the moments that matter. A system sized for mean load will fail at the peak, and for many organizations the peak is the entire point: the retail surge on the biggest shopping day, the streaming spike at a live final, the tax portal on the filing deadline, the benefits site when enrollment opens. Plan these named events individually. Estimate the peak from the business (expected concurrent users, requests per session, the multiple over a normal day), provision to that peak with headroom, load test at that level, and stage the capacity before the event rather than scrambling during it.

Treat a launch or deadline as an operational event with a runbook. Pre-warm caches and buffer pools, raise quotas in advance, freeze risky deployments during the window, and put humans on call who can act if the forecast proves low. After the event, capture the actual peak and how close you came to your limits, because that number is the best input to next year's plan. Government deadlines deserve special care: they are self-imposed, publicly known, and immovable, so there is no excuse for being surprised and no way to hide when you are.

### Instrument capacity and review it on a cadence

Capacity planning runs on data, and the data comes from the observability of chapter 9.2. Track utilization of every constrained resource (CPU, memory, disk, network, connection pools, queue depth) against its limit, so you can see headroom shrinking before it disappears. Watch saturation signals directly: queue lengths, wait times, and rejection rates reveal the queueing cliff approaching. Trend these over weeks to project when a resource will hit its ceiling at the current growth rate, and alert on the projection rather than the current value alone, so you provision before the wall rather than at it.

Hold capacity reviews on a regular cadence, monthly or quarterly, rather than only after an incident. In each review, compare forecast to actual demand and correct the model, walk the hard-limit inventory and check headroom against each, look at upcoming events and business plans, and decide what to reserve, raise, or retire. Keep a living capacity model: a simple document or spreadsheet that maps demand drivers to resource needs, so anyone can ask "what happens to the database if traffic doubles" and get an answer from the model instead of an outage. The model is never perfect, but a written, regularly corrected model beats intuition every time.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| High utilization target | Lower cost per unit; less idle capacity | Latency explodes near saturation; no room for spikes or failover |
| Generous headroom | Predictable latency; absorbs spikes and failover | Higher steady cost; can hide inefficiency |
| Reserved capacity | Lowest unit price for stable baseline | Commitment risk if demand falls or shifts |
| On-demand capacity | Flexible; matches variable load minute to minute | Highest unit price; can surprise the budget |
| Spot instances | Deep discount for interruptible work | Reclaimed without notice; unsuitable for stateful or latency-critical work |
| Autoscaling | Tracks load automatically within the envelope | Cannot exceed reserved quota; cold starts; masks downstream limits |
| Buffer pool (warm capacity) | Absorbs sudden spikes instantly | Pays for idle capacity between spikes |

The central tension is cost against reliability, and there is no setting that optimizes both. Run lean and you save money until the day a spike meets a saturated resource and latency falls off the queueing cliff. Run generous and you sleep well while paying for headroom that sits idle most of the time. Resolve the tension with the SLO rather than with fear or thrift. Provision enough headroom to meet the reliability target through forecast peaks plus a margin, and no more, then let [FinOps](https://en.wikipedia.org/wiki/FinOps) (financial operations for cloud spend, chapter 9.4) hunt the waste that does not defend an SLO. The goal is deliberate balance: every dollar of headroom bought on purpose to buy a known amount of reliability, and every dollar of waste removed on purpose because it buys none.

## Questions to discuss with your team

1. **Do we actually know the load at which each of our hard bottlenecks binds, or are we assuming autoscaling will save us?** Most teams can tell you their instances autoscale, and most cannot tell you the concurrent-connection limit on their primary database, the API rate limit of their most important third party, or the account quota that caps their function concurrency. Those are the limits that end launches, and they do not move when the stateless tier scales. Bring the written inventory of hard limits if you have one, and if you do not, that absence is the finding. For each limit, you want three numbers: the ceiling, today's usage, and the demand level at which they meet. Anywhere you cannot produce all three, you have a bottleneck you are managing by hope.

2. **When did we last load test to the level of our worst upcoming peak, on production-like data, and did the SLO hold with headroom?** A capacity plan is a set of claims about how the system behaves under load, and an untested claim is a guess wearing a suit. The peak that matters is not last month's average but the next launch, holiday, or deadline, and the test only means something if the data and topology resemble production, because a limit measured on a toy dataset lies. Bring the results of your most recent stress and soak tests, including where the system broke and how it failed when it did. If the honest answer is that you have never driven the system to its breaking point on purpose, then you will discover that point in production, at the worst possible time, with users watching.

3. **How do product, marketing, and operations tell engineering about a spike before it happens, and how far ahead?** The most expensive capacity failures are not modeling errors; they are events that engineering never heard about until traffic arrived. A forecast can extrapolate trend and seasonality from history, but an event has no history, so it can only come from the people planning it. Bring the last three demand spikes and ask, for each, how many days of warning engineering got and whether that was enough to reserve capacity and load test. The evidence you want is a standing channel with a lead time long enough to provision against, because cloud quota increases alone can take days. If the channel does not exist, your capacity plan is blind to exactly the moments it exists to protect.

## Examples

**Startup.** A ten-person startup runs a consumer app on autoscaling cloud infrastructure and feels safe because the instance count grows with load. Their first television feature triples traffic in an hour, the stateless tier scales beautifully, and the app falls over anyway: every new instance opened database connections until the database hit its connection cap and began refusing them. The lesson reshapes their practice. They add a connection pooler in front of the database, write down every hard limit between a request and a response, and load test to several times their normal peak on a production-sized dataset. They cover their steady baseline with a reserved-capacity commitment for the discount and keep a small warm buffer pool so the next spike meets ready capacity. The changes cost a week and convert their fragile confidence into a plan they can defend.

**Enterprise.** A global retailer treats its biggest sales day as the capacity event of the year. Months ahead, a cross-functional team builds a demand forecast from prior years' trend and seasonality plus the merchandising plan, translates the forecast into resource needs through a capacity model, and provisions to the projected peak with generous headroom. They load, stress, soak, and spike test the full path on production-like data, raise every relevant cloud quota weeks in advance, pre-warm caches and buffer pools, and freeze risky deployments for the surrounding window. Reserved capacity covers the stable baseline for cost, on-demand autoscaling absorbs the daily curve, and interruptible batch work runs on spot. Observability tracks every constrained resource against its limit in real time during the event, with alerts on projected saturation rather than current value. The day passes without drama, which is exactly the outcome the planning bought.

**Government.** A national tax agency runs a filing portal whose demand is legally concentrated into the days before an immovable deadline, when a whole country files at once. The agency plans for that peak specifically rather than for an annual average that would be meaningless. It estimates concurrent filers from prior years and population data, provisions to that peak with a wide safety margin because there is no option to shed load or ask citizens to come back later, and load tests to the projected concurrency on realistic data. The team keeps a written inventory of every quota and single point of failure, raises limits with providers well ahead of the window, and sets utilization targets low enough that the queueing cliff stays far from the deadline surge. After each filing season they record the true peak and how much headroom remained, feeding next year's model. The public sees a portal that stays up on the day it is designed for, which is the whole point of the institution's promise.

## Business case: motivations, ROI, and TCO

The return on capacity planning appears as two costs avoided that pull in opposite directions, which is what makes the discipline valuable. Under-provisioning costs outages, and outages during peak events cost the most: lost revenue, lost transactions, and reputational damage precisely when the audience is largest. A retail site down on its biggest day or a government portal collapsing on its filing deadline pays for years of planning in a single bad hour. Over-provisioning costs the opposite way, in cloud bills for capacity that sits idle, and at enterprise scale a few points of chronic over-provisioning across a fleet runs to millions of dollars a year. Capacity planning is the practice that finds the deliberate middle: enough to defend the SLO through peaks, no more than that.

The cost to adopt is mostly discipline rather than tooling. You build a demand forecast, write down your hard limits, run load tests on a cadence, blend your provisioning strategies, and hold regular capacity reviews. The total cost of ownership (TCO) improves from both sides at once: fewer capacity-driven incidents lower the cost of downtime and emergency response, and continuous rightsizing plus a sensible reserved-and-spot blend lower the steady infrastructure bill. To make the case to leadership, connect capacity to the numbers they already watch. Tie under-provisioning to revenue lost per hour of peak downtime and to SLO breaches with contractual penalties, and tie over-provisioning to the FinOps waste report from chapter 9.4. The argument is not abstract prudence; it is money on both sides of a dial you can set on purpose.

## Anti-patterns and pitfalls

- **Autoscaling as a plan:** trusting elastic instances while a database connection pool, account quota, or single point silently caps the whole system.
- **Running hot to save money:** targeting 90%-plus utilization and meeting the queueing cliff, where latency explodes and the SLO breaks.
- **Averages instead of peaks:** sizing for mean load so the system fails at exactly the peak event that justified building it.
- **Forecasting from history alone:** extrapolating trend and seasonality while missing the launch or campaign that engineering was never told about.
- **Untested limits:** planning around a breaking point nobody has measured, then discovering it in production at the worst moment.
- **Toy-data load tests:** measuring capacity on unrealistic data and topology, producing numbers that lie about the real system.
- **No hard-limit inventory:** managing quotas, pools, and single points by memory and hope rather than a written, maintained list.
- **Reserve-everything or reserve-nothing:** over-committing to reserved capacity that demand outgrows or shrinks below, or paying full on-demand rates for a stable baseline.
- **Capacity review only after incidents:** treating planning as reactive firefighting instead of a regular cadence that provisions ahead of need.

## Maturity model

- **Level 1, Initial:** Capacity is reactive. Teams add resources after they run out, trust autoscaling to handle everything, and have no forecast, no hard-limit inventory, and no load testing. Peak events are met with hope, and outages during launches and deadlines are treated as bad luck.
- **Level 2, Managed:** Basic monitoring shows utilization, and teams provision headroom by rule of thumb. Some load testing happens before big events, major quotas are known, and a simple forecast exists, but practices vary by team, the model is not maintained, and downstream bottlenecks are often missed.
- **Level 3, Defined:** Capacity planning is a documented discipline. A demand forecast combines trend, seasonality, events, and business growth; a written hard-limit inventory is maintained; utilization targets derive from SLOs; load, stress, and soak tests run on a cadence; and provisioning blends reserved, on-demand, and spot deliberately. Regular capacity reviews correct the model.
- **Level 4, Optimizing:** Capacity is modeled continuously and provisioned ahead of need. Forecasts are validated against actuals and refined, saturation is projected and alerted on before it arrives, provisioning blends are optimized against live pricing, peak events run from rehearsed runbooks, and cost and reliability are balanced deliberately against the SLO across the whole platform.

## Ideas for discussion

1. What is your current utilization target for latency-sensitive services, and can you justify it from your SLO and the queueing behavior rather than from a wish to save money?
2. Which of your components cannot autoscale at all, and what happens to the rest of the system when one of them saturates?
3. If your traffic doubled next quarter, which resource hits its ceiling first, and how many days of lead time would you need to raise it?
4. How do you decide the blend of reserved, on-demand, and spot capacity, and when did you last revisit it against your actual demand shape?
5. When a peak event is coming, who owns pre-warming, quota raises, and the go/no-go decision, and is that written down as a runbook?
6. Are your capacity alerts firing on projected saturation weeks ahead, or only on current utilization once the wall is already close?

## Key takeaways

- Capacity planning matches supply to forecast demand with deliberate headroom; it is distinct from autoscaling (short-term, within the envelope) and performance engineering (cheaper units of work).
- Forecast from trend, seasonality, known events, and business growth, and get event warnings from product and marketing, because events have no history to extrapolate.
- Respect the queueing-theory cliff (chapter 11.3): latency explodes near saturation, so set utilization targets from your SLO and hold real headroom.
- Find limits by load, stress, soak, and spike testing on production-like data, and keep a written inventory of hard bottlenecks that will not autoscale.
- Blend reserved, on-demand, and spot capacity with warm buffer pools, plan named peak events individually, and review capacity on a cadence rather than after outages.

## References and further reading

- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, and Stephen Thorne (eds.), *The Site Reliability Workbook: Practical Ways to Implement SRE*
- John Allspaw, *The Art of Capacity Planning: Scaling Web Resources in the Cloud*
- Neil J. Gunther, *Guerrilla Capacity Planning: A Tactical Approach to Planning for Highly Scalable Applications and Services*
- Martin L. Abbott and Michael T. Fisher, *The Art of Scalability: Scalable Web Architecture, Processes, and Organizations for the Modern Enterprise*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- Leonard Kleinrock, *Queueing Systems, Volume 1: Theory*
- J. R. Storment and Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
