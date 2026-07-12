# 9.8 On-call and operational readiness

## Overview and motivation

Someone is awake right now because your system might page them. On-call is the human arrangement that puts a qualified person within reach of a production problem at any hour, and operational readiness is the work you do beforehand so that person has a fighting chance. This chapter is about that readiness and that human system: how you design a rotation people can sustain for years, how you decide what is worth waking someone for, and how you make sure a service is genuinely ready to be operated before you let it carry real traffic.

Keep this distinct from two neighbors. Chapter 9.3 covers incident management, the response process once something is actively broken: command roles, severity levels, coordination, and postmortems. Chapter 9.1 covers [site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE), the broader discipline of engineering reliability with service level objectives and error budgets. This chapter sits upstream of the incident and alongside the discipline. It asks a narrower, more personal question: is the service ready to run, and is the person carrying the pager set up to succeed rather than to suffer? An organization can have an excellent incident process and still burn out its engineers, because the pain of on-call is decided long before any incident, by the quality of the alerts, the state of the runbooks, and the humaneness of the schedule.

For large teams, on-call stops being an informal favor and becomes infrastructure. A platform with hundreds of services and dozens of teams cannot rely on the one person who happens to know how everything works. It needs rotations, escalation paths, and readiness standards that hold up when the original authors have moved on. In enterprise and government settings the stakes rise further. Regulated services carry availability commitments and duty-of-care obligations to the staff who operate them. A citizen-facing benefits or health system cannot go dark overnight because the only person who understood it was on holiday. Operational readiness is how an institution keeps its promises after the launch party ends, and humane on-call is how it keeps the people who keep those promises.

## Key principles

- Page a human only for problems that are urgent, actionable, and real.
- Design the rotation for a person who has a life, not for an always-available machine.
- Prove a service is ready to operate before it carries production traffic.
- Alert on user-visible symptoms and SLOs, not on every internal cause.
- Treat runbooks and readiness reviews as living documents that get used, not filed.
- Whoever builds a service should help run it, within humane and supported limits.
- Measure on-call health and cut toil so the load trends down, not up.

## Recommendations

### Design a humane, sustainable rotation

Start with the shape of the schedule, because it decides more about sustainability than any tool. A common pattern is a weekly rotation with a primary responder who takes pages first and a secondary who acts as backup when the primary does not acknowledge or needs help. Keep the pool large enough that any one engineer is on-call no more than one week in four, and ideally one in six or beyond. A rotation of four or fewer people is a warning sign: illness, holidays, and attrition will collapse it into the same two exhausted heroes.

Where you operate across time zones, prefer a [follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun) model, in which teams in different regions each cover their own daylight hours so nobody is routinely paged at 3 a.m. This respects the [circadian rhythm](https://en.wikipedia.org/wiki/Circadian_rhythm), the body's internal sleep-wake cycle, whose disruption is a direct health cost, not a minor inconvenience. When follow-the-sun is not possible, compress the pain: shorter night-shift blocks, guaranteed recovery time after a bad night, and an explicit rule that an engineer paged heavily overnight does not owe a full day of feature work the next morning.

Escalation is the safety net beneath the rotation. Define, in writing, what happens when the primary does not acknowledge a page within a set window: it rolls to the secondary, then to a team lead or manager, then to a broader group. An [escalation policy](https://en.wikipedia.org/wiki/Escalation) that is automatic and well understood means no page ever falls silently on the floor, and no single tired person is the only line of defense.

### Make paging policy about actionable, urgent, real problems

The fastest way to destroy an on-call rotation is to page people for things they cannot or need not act on. Adopt one rule and defend it fiercely: a page is a claim that a human must do something now. If an alert does not meet all three tests, urgent, actionable, and describing a real user-visible problem, it does not deserve a page. Route it to a ticket, a dashboard, or a daily digest instead.

The enemy here is [alarm fatigue](https://en.wikipedia.org/wiki/Alarm_fatigue), the well-documented phenomenon in which people exposed to frequent alarms become desensitized and start to ignore them, including the ones that matter. It is a patient-safety concept from hospitals, and it transfers exactly to software. When every shift brings twenty pages and nineteen are noise, responders learn to swipe them away half-asleep, and the twentieth, the one that was real, gets the same reflexive dismissal. Every noisy alert you tolerate is a small tax on the credibility of every other alert.

Treat alert quality as a first-class engineering deliverable. Track the acknowledge-to-action ratio: of the pages that fired, how many led to a human doing something that mattered? An alert that never once required action in a quarter is a candidate for deletion or downgrade. Review your alerts on a regular cadence, and give any engineer standing to challenge a noisy one. The goal is a rotation where a page is rare enough that it still means something.

### Alert on symptoms and SLOs, not on causes

The most effective way to cut noise is to change what you alert on. Alerting on causes, such as high CPU, a full disk, or a single restarted process, generates a flood of pages for conditions that may never affect a user and that the system often self-heals. Alert instead on symptoms: is the service doing what users need it to do? Bind your paging alerts to your [service-level objectives](https://en.wikipedia.org/wiki/Service-level_objective) (SLOs), the numeric reliability targets defined in chapter 9.1, and page when you are burning through the error budget fast enough to miss the target, or when a user-facing indicator such as latency or success rate crosses a line that people actually feel.

This symptom-based, SLO-driven approach depends on the observability and telemetry of chapter 9.2, since burn-rate alerting only works when your metrics, logs, and traces are structured and trustworthy. The payoff is dramatic: a handful of meaningful symptom alerts replace hundreds of cause alerts, and a page once again correlates with a problem worth waking for. Causes still matter, but they belong on the diagnostic dashboards the responder consults after a symptom alert fires, not in the paging path.

### Require operational readiness before launch

A service should earn its way into production. Before it carries real traffic, run it through a production readiness review: a structured check, ideally by someone outside the building team, that the service can actually be operated. Codify the review as a checklist that becomes a shared standard across teams. A strong list covers monitoring and SLOs, alerting that meets the paging policy, dashboards, runbooks for the likely failures, defined ownership and an on-call rotation, capacity and load expectations, dependency and failure-mode analysis, backup and recovery, security and access controls, and a rollback plan.

The review is a conversation, not a gate to be gamed. Its value is that it forces the building team to confront operability while they still have context, rather than discovering at 2 a.m. six months later that nobody wrote a runbook or set an alert. Tie readiness to the resilience testing of chapter 9.6: a service that has never had a dependency failure injected before launch is making an untested promise about how it fails. For high-stakes enterprise and government launches, make the readiness review a required, documented step, because the cost of an unready citizen-facing service failing in public is measured in trust as much as in money.

### Write runbooks and playbooks that actually get used

A runbook is a step-by-step operational document: how to restart this service, rotate this credential, drain this queue, interpret this alert. A playbook is the broader response guide for a class of situation. Both are worthless if nobody reads them, and most runbooks go unread because they are stale, vague, or impossible to find at 3 a.m. Fix the failure modes directly. Link the runbook from the alert itself, so a responder reaches it in one click from the page. Keep runbooks in version control next to the code, as the documentation practices of chapter 2.7 recommend, so they are reviewed and updated like any other artifact. Write them for a stressed, sleepy stranger, with concrete commands and expected outputs, not prose that assumes the author's context.

The test of a runbook is whether someone other than its author can follow it successfully under pressure. Validate that during onboarding and game days, and update the runbook the moment an incident reveals it was wrong. A runbook that lies is worse than none, because it sends a tired responder confidently in the wrong direction.

### Own what you build, within humane limits

The [DevOps](https://en.wikipedia.org/wiki/DevOps) movement popularized "you build it, you run it": the team that writes a service also carries its pager. The benefit is real and worth defending. When builders feel their own pages, they invest in reliability, fix noisy alerts, and design for operability, because the feedback loop reaches them personally rather than landing on a separate operations team that cannot fix the root cause.

The model has limits you must respect. It requires that teams be genuinely equipped to run their services: given the tooling, the platform, the training, and the time to do operations well, as the engineering effectiveness of chapter 1.10 and the ways of working of chapter 1.4 both demand. Full ownership is cruel when imposed on a team too small to staff a rotation, or without the platform support that makes on-call bearable. Some organizations run a hybrid, where a central SRE or platform team co-owns the hardest tiers or provides after-hours coverage for services that meet a high reliability bar, freeing product teams from routine night pages. The principle to keep is the feedback loop; the shape can flex to fit the team's size, maturity, and the humaneness of the load.

### Onboard on-call engineers deliberately and run game days

Nobody should take the pager for the first time alone and unprepared. Build an onboarding path: shadowing an experienced responder for a rotation, reverse-shadowing where the newcomer leads with a mentor watching, a walk through the dashboards and runbooks, and a clear map of who to escalate to. Make readiness to go on-call an explicit milestone, not an assumption.

Game days are the rehearsal that makes on-call real. In a game day you deliberately exercise a failure, ideally in a realistic environment, and let the on-call engineer respond using only the tools and runbooks they would have in a real incident. This is where you discover that the runbook is out of date, the dashboard is missing a signal, or the alert never fires. Game days build the muscle memory and the confidence that turn a first real page from panic into procedure, and they connect naturally to the chaos engineering of chapter 9.6.

### Run clean handoffs and measure on-call health

The handoff between shifts is where context leaks. Institute a short, structured handoff: what is currently degraded, what alerts fired and were suppressed, what changes are in flight, what to watch. Pair it with basic on-call hygiene, including a policy that the outgoing responder does not leave a mess for the incoming one, and that anything left half-fixed is written down.

Above all, measure. You cannot manage a load you do not see. Track pages per shift, the share of pages that land off-hours (evenings, nights, weekends), time to acknowledge, and how often the secondary and escalation tiers are triggered. Watch the trend, not just the number: a rotation whose off-hours pages climb quarter over quarter is heading for burnout regardless of the current absolute count. Feed these metrics into a regular operational review where the team decides what toil to automate away, which alerts to kill, and where readiness fell short. Reducing toil, the repetitive manual operational work that scales with traffic rather than being fixed once, is how you keep the on-call load flat while the system grows.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| You build it, you run it | Tight reliability feedback loop; owners fix root causes | Cruel to under-resourced or tiny teams; uneven night load |
| Central SRE or platform on-call | Protects product teams from routine night pages; deep operational skill | Weakens the builder feedback loop; can become a dumping ground |
| Follow-the-sun rotation | Nobody paged overnight; humane and healthy | Needs staff in multiple regions; heavier handoff overhead |
| Small local rotation | Simple; everyone knows the system | Collapses under illness or attrition; fast burnout |
| Symptom and SLO alerting | Few, meaningful pages; low fatigue | Needs mature telemetry; may miss slow-building causes |
| Cause-based alerting | Catches issues early and specifically | Floods responders; drives alarm fatigue |
| Strict readiness reviews | Fewer nasty surprises in production | Slows launches; can feel bureaucratic if gamed |

The central tension is between coverage and humanity. Push for maximum coverage and you get large rotations, aggressive alerting, and full ownership everywhere, which protects the system while grinding down the people. Optimize purely for the responder's comfort and you risk gaps where a real problem waits unattended. Resolve it not by splitting the difference but by raising quality: excellent alerts, working runbooks, and ready services let a smaller, calmer rotation cover more ground safely. The organizations that operate best are usually the ones whose responders are paged least, because they invested in readiness rather than in stamina. Every hour spent removing a noisy alert or fixing a runbook buys back multiple hours of human attention and protects the credibility of the whole system.

## Questions to discuss with your team

1. **Would you personally be willing to carry this rotation for a year, and what would you change if the answer is no?** This question cuts through abstraction because it makes the load personal. Bring the real numbers to the conversation: how many pages fired last month, how many landed after midnight or on a weekend, and how long the average acknowledgment took. Ask each person on the rotation whether the current shape is one they can sustain without dreading their on-call week, and listen for the quiet answers as much as the loud ones. If the honest answer is that the rotation is only survivable because a couple of heroes absorb the worst of it, you have found a fragility that will break the first time one of them leaves. The output you want is a concrete list of changes, whether a larger pool, a follow-the-sun split, a night-page reduction, or an alerting cleanup, with an owner and a date attached to each.

2. **For every alert that can page a human, can you name the action the responder is expected to take?** Most rotations have never audited this, and the exercise is revealing. Pull the full list of paging alerts and, for each one, ask what a responder is supposed to do when it fires and how often it fired without leading to any real action last quarter. Alerts that fail the test, the ones nobody can attach an action to, or that consistently resolve themselves before anyone touches them, are the noise that erodes trust in every other alert. Bring the acknowledge-to-action data if you have it, and be ready to delete or downgrade aggressively. The goal is a paging path where every alert is a genuine request for human help, and the meeting should end with a shorter, sharper alert list than it started with.

3. **When a new engineer joins this rotation, what exactly prepares them, and have you tested that it works?** Onboarding to on-call is often assumed rather than designed, and the gap shows the first time a newcomer is paged alone into a failure they have never seen. Walk through the actual path a new responder takes: what they shadow, which runbooks they read, whether anyone has followed those runbooks recently to confirm they still work, and who they escalate to when they are stuck. Try picking a real recent incident and asking whether a new hire, armed only with the current runbooks and dashboards, could have resolved it. The honest answer usually exposes stale documentation and missing signals, which is exactly what game days are meant to surface before a real incident does. Leave with a defined readiness milestone for on-call and a schedule for the game days that will keep it honest.

## Examples

**Startup.** A twelve-person startup launches its first paid product and puts all six engineers on a weekly rotation with a primary and secondary. In the first month the pager fires nightly, mostly for CPU and disk alerts that self-resolve, and two engineers quietly start job-hunting. The team stops and rebuilds: they delete every cause-based alert, define two SLOs for checkout and search, and page only on error-budget burn. Pages drop from roughly forty a week to three. They add a one-page readiness checklist that every new service must pass and link each runbook directly from its alert. On-call goes from the reason people leave to a manageable part of the job, and they did it with a spreadsheet and discipline rather than an expensive tool.

**Enterprise.** A global payments company runs hundreds of services under a "you build it, you run it" model, backed by a central platform team that provides the paging system, the readiness review process, and a shared runbook repository in version control. Every service passes a documented production readiness review before launch, covering SLOs, alerting, runbooks, capacity, and rollback. On-call health is a tracked metric: teams whose off-hours pages exceed a threshold trigger an automatic review, and the platform team offers to co-own the reliability work until the load comes down. Game days run quarterly against realistic failure injection. Because the standard is uniform and the tooling is shared, an engineer can move between teams and understand the on-call system immediately, and leadership can see, per team, whether the human load is sustainable.

**Government.** A national tax agency operates a filing system with hard seasonal peaks and a legal obligation to remain available to citizens. Because the workforce is concentrated in one time zone and overnight staffing is limited, the agency contracts a follow-the-sun arrangement with an operations partner so that no civil servant is routinely paged in the middle of the night, and it treats the health and duty-of-care of on-call staff as a formal requirement. Every service change passes an operational readiness review before deployment, with the checklist retained for audit. Runbooks are written to be executed by a responder who did not build the system, because the people running it in five years will not be the people who wrote it. During filing season the agency runs game days against the peak-load scenario, so the responders meet the surge in rehearsal before they meet it for real.

## Business case: motivations, ROI, and TCO

The return on operational readiness and humane on-call shows up in two ledgers: the system's reliability and the team's retention. On the reliability side, services that pass a readiness review and carry symptom-based alerts fail less often and recover faster, because the runbook exists, the alert is meaningful, and the responder was rehearsed. Mean time to acknowledge and mean time to recover both drop when a page reaches a prepared person with a linked runbook rather than a confused one hunting for context. On the human side, on-call is a leading cause of engineer attrition, and replacing a senior engineer costs a large multiple of the investment it would have taken to fix the rotation. [Occupational burnout](https://en.wikipedia.org/wiki/Occupational_burnout), the state of chronic workplace exhaustion the World Health Organization recognizes as an occupational phenomenon, is expensive precisely because it takes your most experienced people, the ones who understand the system, and drives them out.

The cost to adopt is mostly one-time and modest. You write a readiness checklist, migrate alerts from causes to symptoms, put runbooks in version control, and set up on-call health metrics. The recurring cost is the discipline of reviewing alerts, running game days, and honoring humane scheduling. The cost of neglect compounds quietly: noisy alerts breed fatigue, fatigue breeds missed real incidents and departures, and every departure takes operational knowledge with it, which raises the load on those who remain. To make the case to leadership, connect on-call health to metrics they already watch: incident frequency and duration, time to acknowledge, unplanned attrition, and the off-hours page trend. A rotation whose off-hours pages are falling while the system grows is direct evidence that your reliability investment is working and that your engineers will still be here next year.

## Anti-patterns and pitfalls

- **The hero rotation:** two or three people quietly absorb every hard page, so the schedule looks fine on paper and collapses the moment one of them leaves.
- **Paging on causes:** alerting on CPU, memory, and disk rather than user-visible symptoms, flooding responders with pages that never needed a human.
- **Alert fatigue tolerated:** known-noisy alerts left in the paging path for months because deleting them feels risky, until responders ignore everything.
- **Runbook rot:** documents written once at launch, never updated, and confidently wrong when a tired responder follows them at 3 a.m.
- **Ownership without support:** imposing "you build it, you run it" on a team too small to staff a rotation or lacking the platform and tooling to run it humanely.
- **Readiness theater:** a review checklist filled in to pass the gate rather than to genuinely confront how the service fails.
- **Launch and abandon:** shipping a service with no rotation, no alerts, and no runbooks, then discovering the gap during the first outage.
- **Unmeasured load:** no data on pages per shift or off-hours pages, so burnout is invisible until people quit.
- **First page, no rehearsal:** putting a new engineer on-call with no shadowing and no game day, then acting surprised when they freeze.

## Maturity model

- **Level 1, Initial:** On-call is informal and ad hoc. A few people are called when things break, alerts fire on causes and are mostly noise, runbooks are missing or stale, services launch with no readiness check, and nobody measures the human load until someone burns out or quits.
- **Level 2, Managed:** A defined rotation with primary, secondary, and escalation exists. Some alerts are tuned and some runbooks are written, a basic readiness checklist is used inconsistently, and pages per shift are counted, but night pages are common and onboarding to on-call is improvised.
- **Level 3, Defined:** Readiness reviews are a standard, documented step before launch. Paging is symptom and SLO based, runbooks live in version control and link from alerts, onboarding includes shadowing and game days, handoffs are structured, and on-call health metrics including off-hours pages are reviewed regularly.
- **Level 4, Optimizing:** On-call health is a managed outcome with falling page and off-hours trends. Alert quality is continuously curated, toil is systematically automated away, follow-the-sun or equivalent protects sleep, game days and failure injection are routine, and the organization tunes ownership and staffing deliberately as it learns from every shift.

## Ideas for discussion

1. What is your current ratio of pages that led to real action versus pages that resolved themselves, and what would it take to measure it?
2. If your most knowledgeable responder left tomorrow, which services would become unsafe to operate, and why?
3. Where does "you build it, you run it" serve you well, and where is it quietly cruel to an under-resourced team?
4. When did you last watch a new engineer follow one of your runbooks under realistic conditions, and what broke?
5. Are your off-hours pages trending up or down over the last four quarters, and does anyone own that number?
6. Which readiness-review item, if you enforced it strictly, would have prevented your most recent bad launch?

## Key takeaways

- On-call readiness is decided before any incident, by the quality of your alerts, runbooks, and rotation, not by heroics during the outage.
- Page a human only for problems that are urgent, actionable, and user-visible; alert on symptoms and SLOs, and route everything else to tickets and dashboards.
- Design rotations for people with lives: large enough pools, follow-the-sun where possible, automatic escalation, and honored recovery time.
- Prove services ready before launch with a production readiness review, keep runbooks in version control and linked from alerts, and rehearse with game days.
- Measure on-call health, especially off-hours pages and time to acknowledge, and drive the load down by cutting toil and noise rather than by asking people to endure more.

## References and further reading

- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, and Stephen Thorne (eds.), *The Site Reliability Workbook: Practical Ways to Implement SRE*
- Rob Ewaschuk, "My Philosophy on Alerting," in *Site Reliability Engineering* appendix
- John Allspaw and Jesse Robbins (eds.), *Web Operations: Keeping the Data on Time*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
- World Health Organization, *ICD-11*, entry on burn-out as an occupational phenomenon
