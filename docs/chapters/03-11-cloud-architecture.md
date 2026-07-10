# 3.11 Cloud architecture

## Overview and motivation

[Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) is renting someone else's infrastructure on demand, over a network, billed for what you use, and released when you are done. Cloud architecture is the discipline of designing systems that treat those rented resources as their native home rather than as a rented copy of your old data center. That distinction is the whole point of this chapter. You can move a legacy application to a cloud provider and change nothing about its design, and you will get a bigger bill and roughly the same fragility. Or you can design for the cloud and get elasticity, managed services that erase whole categories of undifferentiated work, and the ability to survive the failure of an entire building without paging anyone. This builds directly on the fundamentals in chapter 3.1: cloud architecture is architecture, with the same trade-offs and quality attributes, applied to a substrate you do not own.

For large teams the stakes are higher because the cloud rewires who does what. When a team can provision a database, a queue, and a global load balancer in minutes, the bottleneck stops being procurement and becomes governance: cost, security, and consistency across dozens of teams doing this at once. The cloud gives every engineer a corporate credit card and a warehouse of power tools, which is wonderful and dangerous in equal measure. Getting the architecture right means capturing the upside (speed, elasticity, resilience) while installing the guardrails that keep spend, security posture, and data residency under control.

Enterprises and governments feel both edges sharply. Enterprises arrive with decades of existing systems, so their cloud story is usually a migration story, full of hybrid connectivity and difficult buy-versus-build calls. Governments carry the added weight of sovereignty, authorization regimes, and citizens' data that legally cannot leave certain borders. The decisions here (which service model, how many providers, where the failure domains sit, what runs as managed service versus your own code) shape cost and risk for a decade.

## Key principles

- **Design for the cloud, do not photograph your data center.** Elasticity, managed services, and failure-domain awareness are the reasons to be here; a lift-and-shift throws them away.
- **Everything is provisioned as code.** If a human clicks it into existence, it is undocumented, unrepeatable, and unauditable.
- **Design across failure domains on purpose.** Regions, availability zones, and services fail; your architecture decides whether that is a shrug or an outage.
- **The shared responsibility model is a contract, not a slogan.** Know exactly which line the provider secures and which line you secure.
- **Buy the undifferentiated, build the differentiating.** Managed services are worth real money for the plumbing; keep your competitive advantage in your own hands.
- **Lock-in is a cost to price, not a sin to avoid.** Portability has a price and leverage has a value; decide deliberately rather than by reflex.
- **Cost is a first-class quality attribute.** In the cloud, architecture and the invoice are the same decision.

## Recommendations

### Choose the service model deliberately, and default to managed

Cloud providers sell along a spectrum captured by the [as-a-service](https://en.wikipedia.org/wiki/As_a_service) models: Infrastructure as a Service (IaaS) rents raw compute, storage, and networking; Platform as a Service (PaaS) rents a managed runtime so you deploy code without tending servers; Software as a Service (SaaS) rents finished applications. [Serverless computing](https://en.wikipedia.org/wiki/Serverless_computing), including functions and managed event-driven services, pushes this further: you supply code or configuration and the provider handles all provisioning, scaling to zero when idle. Each step up the spectrum trades control for leverage, from IaaS with the most control and the most operational burden to serverless with the least of both.

The default should be to climb as high up that spectrum as your requirements allow. A managed database that handles patching, backups, failover, and scaling is almost always a better use of your engineers than a self-run one. Reserve lower-level IaaS for cases that genuinely need it: specialized hardware, unusual compliance boundaries, licensing constraints, or performance the managed offering cannot meet. Write the reason down as an architecture decision record (chapter 3.1), because "we run our own message broker" is a claim that should be re-justified every year.

### Design across regions and availability zones as explicit failure domains

A cloud region is a geographic area; within it, [availability zones](https://en.wikipedia.org/wiki/Availability_zone) are physically separate data centers with independent power, cooling, and networking, close enough for low-latency replication but far enough that one failing does not take the others. These are the seams along which the cloud breaks, so your architecture must treat them as first-class. The baseline for any serious workload is multi-zone: spread compute and data across at least two, ideally three, zones so that losing one degrades capacity rather than causing an outage. This is cheap insurance with rarely a good excuse to skip it.

Multi-region is a heavier decision, tied to your resilience and recovery targets (chapter 3.5) and your disaster-recovery plan (chapter 9.5). Spreading across regions buys survival of a whole-region failure and can put data closer to users, but it introduces real cost, latency, and consistency problems, because cross-region synchronous replication is slow and asynchronous replication means accepting data loss on failover. Decide based on explicit recovery time and recovery point objectives, not a vague wish to be "highly available." Most systems need robust multi-zone and a tested multi-region recovery path; few genuinely need active-active across regions, and those that build it without needing it pay for the complexity every day.

### Treat the shared responsibility model as an architectural boundary

Cloud security runs on a [shared responsibility model](https://en.wikipedia.org/wiki/Cloud_computing_security): the provider secures the cloud (physical facilities, the hypervisor, the managed-service internals) and you secure what you put in the cloud (your data, access controls, network configuration, and code). The exact line moves as you climb the service spectrum. With IaaS you patch the operating system; with a managed database you do not, but you still own who can connect and whether the data is encrypted. The most expensive incidents come from misreading this line, most famously the open storage bucket that leaks millions of records because someone assumed the provider made it private by default.

Make the boundary explicit in your designs and hand the details to chapter 4.3, which covers infrastructure and cloud security in depth. Architecturally, the imperatives are constant: encrypt data at rest and in transit by default, grant least privilege through identity rather than network position, keep the blast radius of any single credential small, and assume any internet-reachable resource will be probed within minutes. Bake these into your landing zone so teams inherit them.

### Provision everything as code, inside a governed landing zone

In a mature cloud practice, no production resource exists because a person clicked a console. Everything is declared in [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (chapter 8.2), version-controlled, reviewed, and applied through a pipeline, so your infrastructure is reproducible, auditable, and diffable. This is what makes multi-zone, multi-region, and disaster recovery real instead of aspirational: you can stand up an identical environment in a new region because the environment is a program, not a memory.

Wrap that code in a landing zone: a pre-built, governed foundation of accounts (or subscriptions or projects), networking, identity, logging, and guardrails that every team builds on. Use separate accounts as blast-radius and billing boundaries, so one team's mistake cannot reach another's data and every dollar traces to an owner. Enforce guardrails as policy-as-code that prevents forbidden configurations (a public database, an unencrypted volume, a resource in a disallowed region) rather than relying on after-the-fact review. A central platform team usually owns the landing zone, connecting this chapter to platform engineering (chapter 8.4) and to containers and cloud-native runtimes (chapter 8.3).

### Price lock-in honestly, and be skeptical of multi-cloud

[Vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in) is the cost of switching providers, and it is a spectrum, not a binary. Using a provider's managed queue creates some lock-in; using its proprietary machine-learning platform creates a lot. The reflexive fear of it drives teams to sacrifice real leverage (the managed services that make the cloud worth using) to preserve a portability they will never exercise. The honest move is to price it: for each significant dependency, estimate what leaving would actually cost and weigh it against what the service saves you now. Abstracting away a managed service to stay portable often costs more, permanently, than the migration you are insuring against ever would.

This is why genuine multi-cloud (running the same workload across two providers) is usually a cargo cult rather than a strategy. It forces you down to the lowest common denominator, doubles your operational surface, and multiplies the expertise your teams must hold, all to hedge a risk that rarely materializes. There are legitimate reasons to touch more than one provider: a best-of-breed SaaS from a second vendor, a regulator's resilience mandate, or a deliberate sovereignty requirement (chapter 10.11). Hybrid cloud, keeping some systems on-premises connected to the cloud, is often unavoidable during enterprise migration and for data that legally cannot move. Choose these with clear eyes and a written justification, not because a slide deck said "multi-cloud."

### Architect for cost, and adopt well-architected thinking

In the cloud, an architectural decision is a spending decision: over-provisioning "just in case" shows up on next month's invoice. Treat cost as a quality attribute you design for, and adopt FinOps practices, the discipline of shared financial accountability for cloud spend (chapter 9.4), so engineering, finance, and product own the bill together. Tag every resource with an owner, make cost visible per team and per service, right-size continuously, use autoscaling so you pay for load rather than for peak, and exploit the pricing levers (committed-use discounts, spot capacity for interruptible work) that the cloud offers.

Beyond cost, use a well-architected framework as a review checklist. The major providers each publish one, and they converge on the same pillars: reliability, security, cost optimization, performance efficiency, operational excellence, and sustainability. Run a lightweight review at design time and periodically thereafter, scoring the system against each pillar and recording the gaps as tracked work. It is a cheap way to catch the trade-off you did not notice.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
| --- | --- | --- |
| Lift-and-shift (rehost) | Fast, low initial effort, exits the data center quickly | Keeps old fragility, misses elasticity and managed services, often costs more |
| Cloud-native redesign | Full elasticity, resilience, managed-service leverage | Higher up-front effort and skills; larger change to absorb |
| Single cloud, deep integration | Simplicity, maximum leverage, lower operational surface | Concentrated lock-in and provider risk |
| Multi-cloud (same workload, two providers) | Provider-failure hedge, negotiating leverage | Lowest-common-denominator design, doubled ops and expertise |
| Hybrid (cloud plus on-premises) | Meets data-residency and legacy constraints, staged migration | Network complexity, two operating models to run at once |
| Serverless / high managed | Minimal toil, scales to zero, fast delivery | Less control, provider-specific, cold-start and quota limits |

The central tension is control versus leverage, and it runs through every row. The more you hand to the provider, the faster you move and the less you operate, at the cost of deeper coupling. The resolution is not to pick one pole but to place each workload deliberately: climb high up the managed spectrum for the commodity plumbing, stay lower where control genuinely earns its keep, and price the lock-in in both directions rather than treating portability as free and dependence as sin. Large organizations get into trouble when they let fear (of lock-in, of the cloud, of cost) make this choice by reflex instead of by analysis.

## Questions to discuss with your team

1. **Which of our workloads are lifted-and-shifted, and are we paying cloud prices for data-center architecture?** It is common to migrate under a deadline, rehost everything as-is, and declare victory, then discover the bill is higher than the data center and none of the resilience or elasticity benefits materialized. The honest audit is to list your major workloads and mark each as rehosted, re-platformed, or genuinely redesigned, then look at which still run on fixed-size, always-on, single-zone footprints. Some lift-and-shift is a legitimate first step, so the question is not whether you did it but whether you have a plan and a timeline to go further. Bring the cost per workload and the incident history, because the workloads that are both expensive and fragile are where redesign pays back fastest. If everything is still shaped like the old data center a year after migration, you bought a more expensive data center.

2. **When an availability zone or a whole region fails, what actually happens, and have we tested it?** Many teams believe they are resilient because they deployed to a cloud, without having designed their failure domains or ever having pulled the plug to check. The concrete version: for each critical system, how many zones does it span, what is the documented recovery time and recovery point objective, and when did we last run a game day that failed a zone or rehearsed a region recovery? Multi-zone should be the unremarkable baseline, so any critical single-zone workload is a finding; multi-region is a heavier, costlier decision tied to explicit recovery targets, not adopted by default. Bring your dependency map, because the failure that hurts is usually a shared service (a database, an identity provider) whose failure domain nobody charted. Resilience you have never tested is a hypothesis, not a property.

3. **For our biggest provider dependencies, what would leaving actually cost, and is that a price worth paying to avoid?** Lock-in debates tend to run on ideology rather than numbers, with one camp abstracting away every managed service to stay portable and another ignoring concentration risk entirely. Ground it: pick your three deepest dependencies, estimate the real engineering cost and elapsed time to replace each, and weigh that against what the service saves you today and how likely you are to ever switch. Layer in the risks that portability does not fix, such as a regulator demanding a second source or a sovereignty rule about where data may live, since those can justify multi-cloud or hybrid even when pure economics would not. The goal is a deliberate, written position per dependency, not a blanket policy. Once you price it, most feared lock-in turns out cheaper to accept than the abstraction layer built to avoid it.

## Examples

**Startup.** A twelve-person startup builds cloud-native from day one on a single provider and feels no guilt about it. The API runs on serverless functions that scale to zero overnight, the data lives in a managed Postgres with automated backups and multi-zone failover, and background jobs run on a managed queue. All of it is defined in infrastructure-as-code, and two engineers own the whole platform because the provider operates the hard parts. When a viral moment sends traffic up fiftyfold in an hour, autoscaling absorbs it and the bill rises in proportion to real usage, then falls again. The founders deliberately accept lock-in as the price of moving fast with a tiny team, and they wrote that decision down to revisit at scale.

**Enterprise.** A multinational insurer with three hundred legacy applications runs a multi-year migration governed by the "6 Rs" (rehost, re-platform, repurchase, refactor, retire, retain). Low-value commodity apps are rehosted quickly to exit two data centers on a deadline; the core policy platform is refactored to be cloud-native; homegrown tools are repurchased as SaaS; and obsolete systems are retired. A central platform team owns a landing zone with per-business-unit accounts, encrypted-by-default guardrails, and policy-as-code that blocks public data stores, while hybrid connectivity links the cloud to the mainframe systems of record that will not move for years. Cost is governed through a FinOps practice with per-unit showback, and a well-architected review gates each application's production launch.

**Government.** A national agency delivering a citizen benefits service is legally required to keep resident data within national borders and to run on authorized infrastructure. It deploys into the provider's government cloud region and pursues an authorization under a regime such as [FedRAMP](https://en.wikipedia.org/wiki/FedRAMP) in the United States (with the compliance work in chapter 4.6), documenting the shared responsibility boundary line by line for auditors. Data residency and broader sovereignty concerns (chapter 10.11) drive an architecture that pins storage and processing to in-country zones and blocks, through policy-as-code, any resource in a disallowed region. The system spans three availability zones with a tested cross-zone recovery plan and provisions everything as code, so audit evidence is a git history rather than a scramble.

## Business case: motivations, ROI, and TCO

The cloud's headline promise is turning capital expenditure into operating expenditure: instead of buying servers years ahead of demand and running them at low utilization, you pay for what you use and scale with the business. That is real, but the deeper return is speed and focus. A managed service that erases patching, backups, and failover hands those engineer-hours back to product work, and provisioning in minutes rather than months compresses the time from idea to production. Elasticity means you stop paying for peak capacity you use twice a year. When the architecture is right, these compound into a total cost of ownership that beats the data center on both cost and capability.

The cost of getting it wrong is equally real, so the business case must be honest. Lift-and-shift without redesign often raises costs while delivering none of the benefits, and ungoverned spend can balloon quietly across dozens of teams until finance sounds the alarm. Frame the case to leadership around three levers: speed (faster delivery and shorter provisioning), resilience (fewer and shorter major incidents), and optionality (entering a new market or region without a data-center project). Put numbers on the avoided data-center refresh, the reduced headcount for commodity infrastructure, and the outage minutes prevented, and set them against the migration cost and the ongoing FinOps and platform investment. The strongest argument is rarely raw cost savings; it is the option value of moving faster than competitors still waiting on hardware.

## Anti-patterns and pitfalls

- **Lift-and-shift and call it "cloud."** Rehosting a data-center design onto rented infrastructure captures the costs and none of the benefits.
- **Console-clicked infrastructure.** Resources created by hand are unrepeatable, undocumented, and impossible to recover or audit; treat any manual production change as a defect.
- **Cargo-cult multi-cloud.** Running the same workload across two providers to hedge a rare risk, paying in complexity and lowest-common-denominator design every day.
- **Single-zone "high availability."** Believing the cloud is resilient by default while running critical workloads in one zone with no tested failover.
- **Misreading shared responsibility.** Assuming the provider secures what you actually own, the classic path to a public bucket leaking millions of records.
- **Cost as an afterthought.** Designing without regard to spend, then discovering the invoice made your architectural decisions for you.

## Maturity model

- **Level 1, Initial:** Cloud use is ad hoc. Teams click resources into existence in shared accounts, workloads are lifted-and-shifted, and there is no landing zone, no cost visibility, and resilience is assumed rather than designed. The first serious outage or bill shock is a surprise.
- **Level 2, Managed:** Core infrastructure is provisioned as code and workloads run multi-zone. Accounts are separated and basic guardrails exist, but service-model and lock-in choices are made by habit, cost is watched after the fact, and multi-region recovery is untested.
- **Level 3, Defined:** A governed landing zone with policy-as-code guardrails is standard, a platform team owns the foundation, well-architected reviews gate significant designs, FinOps gives per-team cost accountability, and buy-versus-build and failure-domain decisions are deliberate.
- **Level 4, Optimizing:** Architecture, cost, security, and resilience are continuously measured and tuned with data. Failure domains are exercised through routine game days, right-sizing and pricing are automated, sovereignty and residency are enforced by policy, and service-model and lock-in positions are re-priced on a regular cadence.

## Ideas for discussion

1. Where on the IaaS-to-serverless spectrum does each of your major workloads sit, and could any climb higher to shed operational toil without losing control you actually need?
2. If your primary provider raised prices sharply or suffered a multi-day regional outage, what is your real plan, and does it justify any multi-cloud or hybrid complexity you carry?
3. Who owns your landing zone and its guardrails, and can a team ship a non-compliant resource (public data store, unencrypted volume, disallowed region) today?
4. For a regulated or sovereign workload, can you produce the shared-responsibility boundary and the authorized configuration as evidence without a fire drill?

## Key takeaways

- Design for the cloud rather than photographing your data center; elasticity, managed services, and failure-domain awareness are the reasons to be here.
- Climb the service-model spectrum toward managed and serverless for commodity work, and keep control lower only where it genuinely earns its cost.
- Make regions and availability zones explicit failure domains: multi-zone as the baseline, multi-region tied to tested recovery targets.
- Provision everything as code inside a governed landing zone with policy-as-code guardrails, separate accounts, and a platform team that owns the foundation.
- Price vendor lock-in honestly in both directions, and be skeptical of multi-cloud unless a concrete regulatory, sovereignty, or best-of-breed reason demands it.
- Treat cost as a first-class quality attribute through FinOps, and run well-architected reviews to catch the trade-offs you missed.

## References and further reading

- Peter Mell and Timothy Grance, *The NIST Definition of Cloud Computing* (NIST Special Publication 800-145)
- Amazon Web Services, *AWS Well-Architected Framework*
- Microsoft, *Azure Well-Architected Framework* and *Cloud Adoption Framework*
- Google Cloud, *Google Cloud Architecture Framework*
- Stephen Orban, *Ahead in the Cloud: Best Practices for Navigating the Future of Enterprise IT* (and the "6 Rs" migration strategies)
- J.R. Storment and Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- Gregor Hohpe, *Cloud Strategy: A Decision-Based Approach to Successful Cloud Migration*
- U.S. General Services Administration, *FedRAMP* program documentation and security baselines
- Cloud Security Alliance, *Security Guidance for Critical Areas of Focus in Cloud Computing*
