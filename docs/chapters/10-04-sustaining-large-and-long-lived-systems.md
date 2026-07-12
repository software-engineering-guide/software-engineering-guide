# 10.4 Sustaining large and long-lived systems

## Overview and motivation

Most writing about software engineering is about building new things. But most of the world's important software is old, large, and still running: tax systems, benefit payments, air-traffic control, core banking, industrial control, and the infrastructure of daily life. These systems routinely run for ten, twenty, or thirty years. That is far longer than the tenure of anyone who built them, and often longer than the companies and languages that produced them. Sustaining such systems means keeping them reliable, secure, understood, and able to change, across decades and across generations of staff. It is one of the hardest and least glamorous disciplines in the field, and one where large enterprises and governments carry the heaviest burden.

Why does this matter more for large organizations? Continuity of obligation. A startup can rewrite or abandon its software. A national government cannot stop paying pensions while it refactors. Enterprises and agencies own systems whose failure has consequences measured in livelihoods, safety, or public trust. And they own many of them at once, staffed by people who join and leave over decades. The central threats are not exotic. They are the slow erosion of the people who understand the system ([bus factor](https://en.wikipedia.org/wiki/Bus_factor), how few people would have to leave before knowledge of a system is lost), the piling up of undocumented knowledge in a few heads, the decay of the technology stack toward [end of life](https://en.wikipedia.org/wiki/End-of-life_(product)), and the paralysis that sets in when a system becomes too critical to touch and too poorly understood to change safely.

This chapter is about stewardship: the deliberate, unglamorous work of helping a system outlive its authors gracefully. It covers ownership continuity and bus-factor mitigation, planned [deprecation](https://en.wikipedia.org/wiki/Deprecation) and sunsetting, knowledge transfer, the peculiar challenges of decades-long systems, and the constant balancing act between innovating and preserving the stability that citizens and customers depend on.

## Key principles

- **Every critical system needs an owner, always.** Ownership is a continuous assignment, not a memory of who wrote it.
- **Knowledge that lives in one head is a risk, not an asset.** Institutionalize understanding before the person leaves.
- **Boring is a feature.** For long-lived critical systems, stability and predictability often outrank novelty.
- **Plan the ending at the beginning.** Every system will be retired or replaced; design and document for that day.
- **Change is how you stay safe.** A system too frightening to touch is already failing; the ability to change is a survival trait.
- **Continuity outlives individuals.** Design teams, documentation, and processes so that no single departure is a crisis.
- **Trust is the real product.** For citizen- and customer-facing systems, reliability and fairness sustained over time are the mission.

## Recommendations

### Establish stewardship and ownership continuity

Assign explicit, current ownership for every system that matters. Own at the team level, not the individual level, so ownership survives departures. Maintain a [service catalogue](https://en.wikipedia.org/wiki/Service_catalog) that records, for each system, who owns it, what it does, what it depends on, and how critical it is. Review ownership regularly, and never let a system become orphaned. An unowned critical system is an emergency waiting to happen. When teams reorganize, transfer ownership deliberately, with a handover, not by assumption. For the most critical long-lived systems, make sure ownership includes not just operation but the ability to understand and change the system, so stewardship does not decay into mere babysitting.

### Mitigate bus factor and key-person risk

Actively measure and reduce concentration of knowledge. If only one person can deploy, debug, or change a system, that is a [single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure) as real as any hardware. Reduce it through pairing and rotation, mandatory code review, shared on-call, and a deliberate rule that no critical task has exactly one capable person. Cross-train so at least two (preferably three) people can perform each essential function. Treat the departure of a key person as a foreseeable event you prepare for continuously, not a shock you absorb. Documentation helps. But working knowledge spread across a team through actual practice is far more durable than documents no one has exercised.

### Institutionalize knowledge transfer

Capture the knowledge that would otherwise leave with people. Focus first on the knowledge that is hard to reconstruct: why decisions were made, what alternatives were rejected and why, where the sharp edges and the critical hacks the rest of the system quietly relies on are, and how the system behaves under stress. Use architecture decision records to preserve the reasoning behind choices, not just the choices. Keep [runbooks](https://en.wikipedia.org/wiki/Runbook) and operational documentation close to the system, and exercise them regularly so they stay true. Build onboarding paths that get new stewards to genuine competence. Treat departures as knowledge-transfer events with real handover time. Remember that [tacit knowledge](https://en.wikipedia.org/wiki/Tacit_knowledge), the feel for a system, transfers mainly through doing alongside someone who has it, so overlap departing and arriving stewards where you can.

### Manage deprecation, sunsetting, and end-of-life

Plan endings deliberately. When you decide to retire or replace a system, treat the sunset as a project in its own right: identify every consumer and dependency, provide a migration path and a realistic timeline, communicate clearly and repeatedly, and support consumers through the transition. Avoid the trap of running the old and new systems in parallel forever because no one will do the hard work of turning the old one off. Assign explicit accountability for completing the decommission. Preserve data, records, and the ability to answer questions about the retired system long after it stops running, especially where legal retention rules apply. A sunset done badly leaves zombie systems that are unmaintained but still relied upon: the worst of all worlds.

### Sustain systems across decades

For systems that must run for twenty or thirty years, plan to outlive everything: the original team, the vendors, the language ecosystem, and the hardware. Prefer [open standards](https://en.wikipedia.org/wiki/Open_standard) and documented interfaces over proprietary black boxes, so future maintainers have a chance. Modularize, so parts can be replaced one at a time rather than through an all-or-nothing [rewrite](https://en.wikipedia.org/wiki/Rewrite_(programming)) that is too risky to ever attempt. Keep the system continuously maintained. A system kept current in small steps stays sustainable. A system frozen "because it works" silently becomes unmaintainable as its stack ages out of support. Keep the skills to operate it, too: for genuinely old technology, deliberately train successors rather than hoping the last expert never retires.

### Balance innovation with stability and trust

Tell apart the parts of your estate where novelty creates value from the parts where stability is the value. Core systems that citizens and customers depend on daily usually reward reliability, backward compatibility, and cautious change over exciting rewrites. Invest innovation at the edges (new channels, new features, new interfaces) while keeping the durable core stable and well-understood. Change the core, yes, but in small, reversible, well-tested increments rather than heroic leaps. The goal is a system that is both dependable and able to evolve: never so frozen that it [rots](https://en.wikipedia.org/wiki/Software_rot), never so churned that it becomes unreliable.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Keep and maintain the old system | Preserves institutional knowledge; low disruption; proven reliability | Aging stack; scarce skills; mounting risk if unmaintained |
| Big-bang rewrite | Fresh stack; sheds accumulated cruft | Very high failure rate; loses hard-won edge-case knowledge |
| Incremental modernization | Continuous risk reduction; keeps running | Slow; requires sustained funding and discipline |
| Documentation-heavy transfer | Explicit, searchable record | Decays if unmaintained; misses tacit knowledge |
| People-based transfer (pairing/rotation) | Durable working knowledge; resilient teams | Costs current productivity; needs deliberate scheduling |
| Freeze critical core | Maximum stability short-term | Stack ages into unmaintainability; grows too scary to touch |

The defining trade-off is stability versus evolution, and the naive resolutions both fail. Freeze a critical system to protect it, and you guarantee it eventually becomes unmaintainable and unsafe. Rewrite it wholesale to modernize, and you invite the high failure rate that big-bang replacements are notorious for, and you discard decades of encoded edge-case knowledge that nobody remembers is there. The durable path is continuous, incremental change: keep the system alive and moving in small steps, so it never ages out of support and never needs a terrifying leap. Knowledge transfer is a similar trade-off, between the ease of documents and the durability of lived experience. The answer is both: lived, team-held knowledge as the backbone, and documents as the reference.

## Questions to discuss with your team

1. **Which of your critical systems have no current, named team owner right now?** Ownership is a continuous assignment, not a memory of who wrote the code, and an unowned critical system is an emergency waiting to happen, noticed only when it breaks. Walk your service catalogue (or build one) and check that every system records who owns it, what it depends on, and how critical it is. Bring evidence: pick three important systems and try to name the accountable team and the last time ownership was reviewed. Where a system is orphaned, or where a reorganization silently dropped it, assign ownership deliberately with a real handover rather than by assumption. Make sure ownership includes the ability to understand and change the system, so stewardship does not decay into mere babysitting.

2. **When you replace a system, who is accountable for actually turning the old one off?** The eternal parallel run is a common and costly failure: old and new systems run side by side indefinitely because no one owns the shutdown, leaving you maintaining two systems and getting the safety of neither. Treat every sunset as a managed project with named accountability for completing the decommission, a mapped list of consumers, a migration path, and a realistic timeline. Bring evidence: how many "temporary" parallel runs or half-retired systems are still drawing maintenance in your estate today? Preserve data and records to meet legal retention rules long after the system stops running, but do not let retention become an excuse to never finish. A sunset done badly leaves zombie systems that are unmaintained yet still relied upon, the worst of all worlds.

3. **Which skills for your long-lived systems will the labour market stop supplying, and what is your succession plan?** Systems that run for twenty or thirty years outlive their language ecosystems, their vendors, and the careers of the people who understand the old stack, and the market will not reliably hand you replacements. Reduce bus factor deliberately so no critical function has exactly one capable person, and cross-train so at least two, preferably three, people can perform each essential task. Bring evidence: for each aging critical system, count how many people can safely change it and how close the most knowledgeable are to retirement. The answer should drive deliberate training of successors and real overlap between departing and arriving stewards, because tacit knowledge (the feel for a system) transfers mainly by doing alongside someone who has it. Documents are the reference; lived, team-held knowledge is the backbone.

4. **When did you last change your most critical long-lived system, and does anyone still dare to?** A system that no one has touched in a year is not stable, it is drifting toward the "too scary to touch" trap, where every change is feared and so the stack quietly ages out of support. For a large organization this matters because paralysis compounds: the longer the freeze, the more knowledge fades and the riskier the eventual unavoidable change becomes. Bring evidence: for each critical system, the date of the last deliberate change, the size of the smallest change anyone would attempt today, and whether a routine dependency or security patch could be shipped this week without heroics. The competing consideration is real, because change also introduces risk, so the goal is not churn but a steady cadence of small, reversible, well-tested steps. In enterprise and government estates, where a frozen core can sit under a citizen service for a decade, treat "we never change it" as a red flag rather than a reassurance, and fund the continuous maintenance that keeps the option to change alive.

5. **How much of your estate is running on a technology that is at or near end of life, and who is tracking that clock?** Aging runtimes, unsupported databases, and out-of-maintenance frameworks are the slow failure mode that turns into a sudden crisis the day a security patch stops arriving. For a large team the danger is that no one owns the horizon: individual teams patch what breaks, but nobody maintains a portfolio view of which stacks lose vendor support and when. Bring evidence: an inventory of each critical system's core technologies, their published end-of-life or end-of-support dates, and the current gap between what you run and what is still supported. The tension is between the cost of continuous upgrading and the risk of deferral, and deferral usually wins until it catastrophically loses. In enterprise and government settings, where procurement and accreditation cycles can take a year or more, an end-of-life date that looks distant is often already inside your lead time, so the succession and upgrade work has to start well before the clock runs out.

6. **Where in your estate is stability the value and novelty a liability, and how do you keep that boundary honest?** Not every system rewards the same treatment: core systems that citizens and customers depend on daily usually reward reliability and cautious change, while the edges reward experimentation, and confusing the two wastes money or invites outages. For a large organization the risk is that ambition and career incentives push exciting rewrites into exactly the durable core that should stay boring. Bring evidence: a map of your estate marking where reliability is the mission and where novelty creates value, plus recent changes that crossed that line in either direction and what they cost. The competing consideration is that even a stable core must still evolve, so "stable" cannot become an excuse to freeze. In enterprise and government contexts, tie this boundary to explicit criticality tiers and a named authority who can veto a risky rewrite of a system the public cannot afford to see fail, so the judgement does not drift with whoever is loudest this quarter.

## Sector lens

**Startup.** With a handful of engineers and little runway, your sustainment risk is concentrated in one or two people who wrote the systems you cannot afford to lose, such as billing or auth. Spend almost nothing on process, but do the cheap, high-value things now: pair a second person through each critical system, write a one-page architecture decision record for the surprising parts, and keep a runbook you actually use. Resist the urge to rewrite something just because it is old, because at your size a failed rewrite of a core system can end the company.

**Small business.** You have no dedicated maintenance team and a tight budget, so favour buying and hosting over building anything you would have to sustain yourself. Prefer vendors and open standards that let you leave, and keep a plain record of which outside system runs which critical function and who to call when it breaks. Where you do own custom code, make sure at least two people (or a trusted contractor plus one employee) understand it, so a single departure or a lapsed support contract does not strand you.

**Enterprise.** Your challenge is portfolio scale: many long-lived systems, many teams, and staff who rotate over decades. Standardize team-level ownership in a service catalogue, measure bus factor across the estate, and fund continuous incremental modernization rather than betting on big-bang rewrites. Govern end-of-life horizons centrally so no critical stack silently ages out of support, and run every sunset as an audited project with named accountability for completing the decommission.

**Government.** Continuity of obligation is absolute: you cannot stop paying benefits or running air-traffic control while you refactor, and failures are public and consequential. Procurement rules push you toward open standards, data portability, and documented interfaces so future maintainers and future vendors have a chance. Fund deliberate succession training for the older technologies the labour market no longer supplies, preserve records of retired systems to meet statutory retention, and treat sustained reliability of citizen services as the accountable mission rather than overhead.

## Examples

**Startup.** A five-person startup already has a system it cannot afford to lose: the billing service one founder wrote in the first month and that now runs every customer charge. Only that founder understands it, so the team treats the bus factor as a real risk rather than a compliment. They pair a second engineer through a full billing cycle, write a short architecture decision record explaining why the odd retry logic exists, and keep a runbook next to the code that they actually exercise during an incident. They resist rewriting it just because it is old and unglamorous, and instead improve it in small reversible steps, so the service that keeps the company alive is understood by more than one head.

**Enterprise.** A large insurer runs a policy-administration system first written decades ago and still central to its business. Rather than attempt a risky wholesale rewrite, it modularized the system behind well-defined interfaces and now replaces one component at a time, each change small and reversible. Every critical function has at least three people who can perform it. On-call is shared. Architecture decision records capture why the system works the way it does. A curated internal course brings new engineers to competence on the [legacy](https://en.wikipedia.org/wiki/Legacy_system) stack, and departing experts overlap with successors so tacit knowledge transfers by doing.

**Government.** A national social-security agency operates benefit-payment systems that have run for over thirty years and cannot stop. It records explicit team ownership in a service catalogue. It funds continuous maintenance rather than freezing the systems. It trains successors in the older technologies deliberately, because the labour market will not supply them. When it retires an obsolete subsystem, it runs the sunset as a managed project: mapping every consumer, providing migration support, preserving records to meet legal retention rules, and assigning accountability for actually completing the decommission, so no zombie system lingers.

## Business case: motivations, ROI, and TCO

The return on sustaining long-lived systems comes from avoiding the two catastrophic failure modes that dominate their [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership). The first is the sudden crisis: a key person leaves, an unsupported component is breached, or an orphaned system fails with no one who understands it. The second is the failed mega-project: a rushed wholesale rewrite that overruns, underdelivers, or collapses. Both are enormously expensive, and both are largely preventable by steady stewardship. The cost of a single avoided rewrite failure, or a single avoided extended outage of a critical citizen service, usually exceeds years of sustained maintenance investment.

The adoption cost is ongoing and unglamorous: funding maintenance that produces no new features, paying for cross-training and documentation time that reduces short-term output, and investing in incremental modernization that never makes headlines. The cost of *not* adopting is deferred and larger: rising risk as the stack ages, ballooning key-person exposure, and eventually a forced, high-risk, high-cost replacement under emergency conditions. When you make the case to leadership, reframe maintenance from "cost centre" to "risk management for systems the organization cannot afford to lose." Present total cost of ownership across the full multi-decade life (including the sustainment and eventual decommission) rather than only the build. And emphasize this: for citizen- and customer-facing systems, sustained reliability is not overhead. It is the trust that is the actual product.

## Anti-patterns and pitfalls

- **The hero maintainer.** One irreplaceable person who understands the system; their departure is an existential event.
- **Freeze and forget.** Declaring a critical system "done," stopping maintenance, and watching its stack age into unmaintainability.
- **The doomed rewrite.** Betting the organization on a wholesale replacement that discards encoded knowledge and usually overruns or fails.
- **Orphaned systems.** Critical software with no current owner, noticed only when it breaks.
- **Documentation theater.** Volumes of docs that are outdated, unexercised, and trusted by no one.
- **The eternal parallel run.** Old and new systems running side by side indefinitely because no one is accountable for the shutdown.
- **Tacit-knowledge loss.** Letting experts leave with no overlap, so the feel for the system evaporates.
- **Too scary to touch.** A system so poorly understood that any change is feared, which guarantees it decays.

## Maturity model

**Level 1: Initiate.** Sustainment is ad hoc and reactive. Systems depend on individual heroes, ownership is remembered rather than assigned, and knowledge lives undocumented in a few heads. Old systems are frozen until they break, aging stacks drift toward end of life unnoticed, and retirements are announced but never completed.

**Level 2: Develop.** Basic practices appear but vary team by team. Ownership is written down for the most obvious major systems, some runbooks and documentation exist, and a few critical functions have a second capable person. Maintenance is funded but reactive, cross-training happens when someone remembers, and there is no shared way of doing any of it across the organization.

**Level 3: Standardize.** Stewardship practices are documented and enforced org-wide. Team-level ownership is recorded in a service catalogue and survives reorganizations. Bus-factor mitigation through rotation and cross-training is a standing rule, architecture decision records and exercised runbooks are expected, modernization is incremental by policy, and every sunset runs as a managed project with named accountability for completing the decommission.

**Level 4: Manage.** Sustainment is measured and controlled with data against baselines. You track bus factor per critical system, the count of people who can safely change each one, the age of every core technology against its end-of-life date, the share of the estate under continuous versus deferred maintenance, and the number of stalled parallel runs and half-finished decommissions. These metrics carry thresholds that trigger action: a system that falls below the bus-factor floor or crosses an end-of-support horizon gets funded remediation, and stewardship health is reported to leadership alongside delivery.

**Level 5: Orchestrate.** Stewardship is continuously improved and integrated across the organization. No critical system is a single point of human failure, knowledge transfer including tacit knowledge through overlap is routine, and systems evolve in small reversible steps so none ages out of support. Ownership, end-of-life tracking, succession, and sunset planning are woven into portfolio and risk planning, the estate is rebalanced as technologies and obligations shift, and multi-decade systems are sustained while preserving the trust of the people who depend on them.

## Ideas for discussion

- How do you measure bus factor meaningfully, and what target is right for different criticality levels?
- When is an incremental modernization genuinely infeasible, making a rewrite the lesser risk?
- How do you fund and reward maintenance work so that stewardship is a respected career path, not a dead end?
- What is the right way to preserve tacit knowledge when the last expert is about to retire and no overlap is possible?
- How long should you retain the ability to answer questions about a retired system, and who pays for that?
- Where in your estate is stability the value and novelty a liability, and how do you keep that judgement honest over time?

## Key takeaways

- Most important software is old and long-lived; sustaining it across decades and staff generations is a first-class discipline.
- Every critical system needs current, team-level ownership; orphaned critical systems are latent emergencies.
- Reduce bus factor deliberately (no critical task should have exactly one capable person) and transfer tacit knowledge through overlap, not just documents.
- Keep long-lived systems continuously and incrementally maintained; freezing them and betting on wholesale rewrites are both failure modes.
- Plan endings as managed projects with accountable completion, preserving data and records to meet obligations.
- For citizen- and customer-facing systems, sustained reliability and fairness are the mission, and maintenance is risk management for what you cannot afford to lose.

## References and further reading

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce and Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* and writings on the Strangler Fig pattern
- Betsy Beyer et al., *Site Reliability Engineering* and *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, reports on federal legacy IT modernization
