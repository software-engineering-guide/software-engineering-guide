# 9.5 Disaster recovery and business continuity

## Overview and motivation

Sooner or later, something you did not plan for will take a system down: a region-wide cloud outage, a fat-fingered `DROP TABLE`, a flood in a data centre, a ransomware detonation, or a supplier that vanishes overnight. The question is never whether disruption arrives, but how fast you recover and how much you lose in the process. This chapter is about being ready for the bad day before it comes.

Two disciplines answer that readiness, and they are not the same thing. [Business continuity planning](https://en.wikipedia.org/wiki/Business_continuity_planning) (BCP) keeps the whole organization functioning through a disruption: people, offices, communications, payroll, and the critical business processes customers depend on. [Disaster recovery](https://en.wikipedia.org/wiki/Disaster_recovery) (DR) is the narrower, technical job of restoring IT systems and data after they fail. Continuity is the goal; recovery is one of the means. You can restore every server and still fail your customers if nobody knew who was allowed to declare a disaster or how to reach them. This chapter treats DR as an engineering practice and BCP as the business frame it serves.

For large teams the stakes scale with you. An enterprise carries regulatory recovery obligations, multi-region footprints, and concentration risk in a handful of suppliers. Government carries a legal duty to sustain essential functions for citizens, codified as continuity of operations. Both operate under scrutiny where an untested plan is a liability you will discover at the worst possible moment. Recovery is where reliability (chapter 9.1) and incident response (chapter 9.3) meet the harder question of surviving the failures you cannot design away.

## Key principles

- **Continuity is broader than recovery.** Restoring servers is not the same as keeping the business running.
- **Two numbers drive everything.** Recovery time objective (RTO) and recovery point objective (RPO), set from business impact, size every decision.
- **An untested backup is not a backup.** A restore you have never performed is a hope, not a capability.
- **Assume the backup is a target.** Ransomware hunts your backups first, so keep copies immutable and offline.
- **Rebuild from code, not from memory.** If you cannot recreate infrastructure from source, you cannot recover it reliably.
- **Map what you depend on.** You recover only as fast as your slowest upstream dependency.
- **Measure recovery like any other system.** Actual RTO and RPO from real drills, not the numbers you wrote on a slide.

## Recommendations

### Set RTO and RPO from a business impact analysis

Every recovery decision descends from two numbers, so get them right first. The **recovery time objective (RTO)** is how long a system can be down before the harm is unacceptable. The **recovery point objective (RPO)** is how much data you can afford to lose, measured as the age of the last good copy you can restore to. A payments ledger might demand an RTO of minutes and an RPO near zero; an internal analytics dashboard might tolerate a day of each. You cannot set these in engineering. Derive them from a [business impact analysis](https://en.wikipedia.org/wiki/Business_impact_analysis) (BIA) that ranks business processes by the cost of their disruption and traces each back to the systems and data it needs. Tighter objectives cost more, so the BIA is what stops you from gold-plating a trivial service and under-protecting a critical one.

### Do backups right: the 3-2-1 rule, immutability, and testing

Backups are the floor beneath every recovery strategy, and most organizations do them worse than they think. Follow the [backup](https://en.wikipedia.org/wiki/Backup) discipline known as the **3-2-1 rule**: keep at least three copies of your data, on two different media or systems, with one copy off-site. Modern threats add two more requirements. Keep at least one copy **immutable** (write-once, un-deletable for a retention window) and ideally **offline or air-gapped**, because ransomware now deliberately encrypts or deletes reachable backups before it announces itself. Above all, test restores on a schedule. An untested backup is not a backup, it is an untested assumption, and the failures you find in a drill (corrupt archives, missing encryption keys, backups of the wrong volume) are exactly the ones that would have ended you in a real event.

### Choose a DR strategy along the cost-versus-speed spectrum

DR strategies trade money for recovery speed, and you should pick per system based on its RTO and RPO rather than buying one tier for everything. Four patterns anchor the spectrum. **Backup and restore** is cheapest and slowest: you rebuild from backups when disaster strikes, with an RTO of hours to days. **Pilot light** keeps a minimal core (databases replicating, core config in place) warm but scaled down, ready to expand. **Warm standby** runs a smaller always-on copy of the full stack that you scale up on failover, cutting RTO to minutes. **Multi-site active-active** runs full capacity in two or more locations serving live traffic, giving near-zero RTO at the highest cost and complexity. Match the tier to the number the business signed off on, and do not pay active-active prices for a system that tolerates a pilot light.

### Replicate data with the consistency trade-off in mind

Speed of recovery depends on how current your standby data is, and here you inherit the hard problems of [distributed systems](https://en.wikipedia.org/wiki/Distributed_computing) (chapter 3.3). **Synchronous replication** confirms every write in a second location before acknowledging it, giving an RPO near zero at the cost of added write latency and a hard limit on distance. **Asynchronous replication** acknowledges locally and ships changes after, so it is fast and geographically flexible but leaves a replication lag window you will lose on failover. There is no free choice: stronger consistency costs latency, weaker consistency costs data. Decide per data store from its RPO, and know your typical replication lag, because that lag is your real RPO on a bad day, not the number in the design doc.

### Rebuild from code with infrastructure as code

You cannot reliably recover an environment you provisioned by hand, because nobody remembers every click. Define your environments as [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (chapter 8.2) so a whole stack can be recreated from version-controlled source in a known-good state. This turns recovery from an archaeology project into a repeatable pipeline run, keeps your standby region honest (it drifts less when both are built from the same code), and gives you a clean way to stand up recovery infrastructure in a fresh account or region after a compromise. Store the code, secrets references, and runbooks somewhere that survives the loss of your primary environment.

### Map dependencies before you need them

Systems fail in webs, not in isolation, and recovery stalls on the dependency you forgot. Map what each critical system needs to function: upstream services, DNS, identity and authentication, certificate authorities, message queues, and third-party APIs and SaaS providers. Note the recovery order, because bringing an application up before its database or its identity provider just produces a second outage. Pay special attention to external suppliers, since your recovery is capped by theirs and you may have no visibility into it. This mapping ties directly to resilience and graceful degradation (chapter 3.5): the fewer hard dependencies a system has, the faster it comes back.

### Test recovery as a practice, not an event

A DR plan you have not exercised is fiction. Build a ladder of tests. A **tabletop exercise** walks the team through a scenario on paper to find gaps in roles, decisions, and communication. A **game day** injects a real controlled failure into a live-like environment. A **full failover drill** actually cuts over to the recovery site and runs on it. Run these on a cadence, rotate the scenarios (including the loss of a key person or supplier), and measure the outcome: capture the **actual RTO and RPO** you achieved and compare them to target. The gap between measured and promised recovery is the most honest reliability metric you own, and closing it is the whole point of the drill.

### Plan cyber-recovery as its own scenario

Ransomware and destructive cyberattacks break the assumptions of ordinary DR, so treat them separately. In a natural disaster your data is intact elsewhere; in a [ransomware](https://en.wikipedia.org/wiki/Ransomware) event your data and often your backups are the weapon, and your recovery environment may itself be compromised. Plan a **clean-room recovery**: an isolated, trusted environment where you restore from immutable copies, scan for the intrusion, and rebuild identity and credentials before reconnecting anything. Know which backup is your last known-clean point, and expect that finding it takes forensic time your ordinary RTO never budgeted for. This is where immutable, offline copies earn their cost, and it connects tightly to incident management (chapter 9.3) and to compliance and governance obligations for breach handling (chapter 4.6).

## Trade-offs: pros and cons

| DR strategy | Pros | Cons |
|---|---|---|
| Backup and restore | Cheapest; simple; low ongoing cost | Slow RTO (hours to days); larger RPO |
| Pilot light | Low cost; core data warm and ready | Manual scale-up; recovery still takes real time |
| Warm standby | Fast RTO (minutes); full stack proven | Ongoing cost of a running second environment |
| Multi-site active-active | Near-zero RTO; no single-site failure | Highest cost and complexity; consistency is hard |
| Synchronous replication | RPO near zero | Write latency; distance-limited; tighter coupling |
| Asynchronous replication | Fast, flexible, geographically free | Data loss window equal to replication lag |

The central tension is that recovery speed and data freshness both cost money and complexity, and neither is free at any tier. Resolve it per system rather than per organization: let the business impact analysis assign each critical system an RTO and RPO, then buy exactly the strategy that meets it. Spending active-active money on a reporting tool starves the ledger that needed it, and the reverse is negligence. The discipline is matching the spend to the number the business owns, and revisiting that match as systems change in importance.

## Questions to discuss with your team

1. **What are the RTO and RPO for each of your critical systems, and who in the business signed off on them?** If engineering invented these numbers alone, they are guesses, and guesses get funded either too generously or not at all. The recovery time and recovery point objectives should fall out of a business impact analysis that ranks processes by the cost of their disruption, so the ledger gets minutes and the internal wiki gets a day. Bring your current tiering and ask whether the person accountable for each business process would actually accept the data loss and downtime you have designed for. In a large organization this conversation is what prevents the expensive mistake of protecting everything equally, which protects nothing well. If nobody outside engineering can name the numbers, you do not yet have objectives, you have hopes.

2. **When did you last perform a real restore, and did you measure the actual RTO and RPO you achieved?** A backup you have never restored is an untested assumption, and the failure modes that kill you (corrupt archives, lost encryption keys, a snapshot of the wrong volume, a dependency that will not come up) surface only when you try. Bring the date and result of your last full failover drill, not your last tabletop, and the gap between the recovery you achieved and the recovery you promised. For a large team, one successful restore of one system does not prove the others, so ask what fraction of critical systems have been recovered end to end in the past year. The measured gap is your most honest reliability number, and if you cannot state it, your plan is fiction until proven otherwise.

3. **If ransomware encrypted your production and reached your backups tonight, what is your last known-clean copy and where would you rebuild?** Ordinary disaster recovery assumes your data is safe somewhere else, and a destructive cyberattack breaks exactly that assumption by making your data and your backups the weapon. Ask whether at least one backup copy is immutable and offline, how you would identify the last clean restore point, and where a trusted clean-room environment would come from when production itself is compromised. This scenario needs forensic time that your normal RTO never budgeted, so bring an honest estimate of how long finding a clean point actually takes. For enterprise and government teams this is also a compliance event (chapter 4.6) with breach-notification clocks running in parallel. If the answer is "we would restore the latest backup," you have not planned for this at all.

4. **Which of your systems is paying for a recovery tier its business impact analysis does not justify, and which is dangerously under-protected?** Recovery speed and data freshness both cost money at every tier, so a blanket policy either wastes active-active budget on a reporting tool or starves the ledger that genuinely needed it. The competing pull is real: one standard tier is far simpler for many teams to operate, while tiering per system matches spend to value but demands ongoing curation as a system's importance shifts. Bring the current DR strategy for each critical system, the RTO and RPO it targets, the monthly cost of its standby and replication, and the date the tiering was last revisited against a fresh impact analysis. In an enterprise or government setting a mismatched tier multiplies across regions and audit will ask you to justify both the money you spend and the exposure you accept, so an unexplained active-active bill and an unprotected critical service are equally hard to defend.

5. **Do you actually know the recovery order of your critical systems, and how far your recovery depends on suppliers you cannot test?** Systems fail in webs, not in isolation, and a recovery stalls on the dependency nobody mapped: bring an application up before its database, identity provider, or DNS and you simply produce a second outage. Mapping dependencies is tedious and the map goes stale, but the alternative is discovering the recovery order live during a failover, and concentration risk in a handful of SaaS providers stays invisible until they fail together and cap your recovery at theirs. Bring a current dependency map, the documented recovery sequence, and a list of external suppliers with their stated recovery commitments and whether you have ever validated any of them. For a large or public organization, supplier continuity and concentration risk are increasingly a procurement and regulatory concern, so those recovery obligations belong in the contract in a form you can audit rather than in a vendor's marketing.

6. **If you restored every server tonight, would the business actually keep running, and who is authorized to declare a disaster?** Disaster recovery restores IT, but business continuity keeps the organization functioning: people, communications, payroll, and the decisions that depend on someone having the authority to make them. You can recover every system and still fail your customers if nobody knew who could declare a disaster or how to reach staff when the normal channels are also down. Engineering owns recovery, yet continuity spans facilities, HR, communications, and leadership succession, and those seams between departments are exactly where a plan quietly rots. Bring the declaration authority and escalation chain, the fallback communication plan, the named successors and alternate facilities, and the date the business side (not just IT) last exercised the plan. Government carries a legal continuity-of-operations duty with named successors and essential functions, and enterprises face regulatory continuity obligations, so both are judged on whether the business survives the bad day, not merely the servers.

## Sector lens

**Startup.** With a tiny team and little runway, you cannot afford a hot second region, so be deliberate about the cheap parts that still save you. Set one honest recovery tier, follow the 3-2-1 rule with automated snapshots and at least one immutable copy your own admins cannot delete, and keep the whole environment as infrastructure as code so you can rebuild from source. Skip the elaborate plan and instead run one real restore into a scratch environment each quarter, because a single timed drill teaches you more than a binder nobody reads.

**Small business.** With no dedicated continuity specialist and a tight budget, treat recovery as something you buy rather than build. Lean on your cloud provider's managed backup, snapshot, and cross-region replication rather than standing up bespoke DR infrastructure, and choose vendors whose backups are immutable and whose restore process you can actually run yourself. Frame the whole exercise around two questions you can answer without a specialist: how much data can we lose, and how long can we be down, and prove one restore works before you trust it.

**Enterprise.** At scale the problem is portfolio governance across many teams: a business impact analysis that assigns every service an RTO and RPO, recovery strategies tiered from backup-and-restore up to active-active, and a central view of upstream and supplier dependencies including concentration risk. Budget the standby, replication, and immutable-copy costs explicitly, run regulator-witnessed full failovers on a cadence, and measure actual recovery against target as a tracked reliability metric. Maintain cyber-recovery as its own programme with immutable vault copies and a clean-room runbook, tested independently of the natural-disaster drills.

**Government.** Procurement rules, transparency, and public accountability shape every choice, and continuity is often a legal duty rather than a preference. Build a continuity-of-operations programme that identifies essential functions, orders their recovery, and names successors and alternate facilities so decisions never stall for want of an authorized person, and align it to recognized guidance such as NIST SP 800-34 in support of FISMA obligations. Keep air-gapped backup copies, define infrastructure as code for rebuild in an alternate region, and run an annual full exercise plus ransomware tabletop drills whose measured results you report to oversight bodies as evidence that essential services survive.

## Examples

**Startup.** A twelve-person SaaS company cannot afford a hot second region, so it is deliberate about the cheap parts. It sets one honest tier: RTO of four hours, RPO of fifteen minutes for the customer database. It follows the 3-2-1 rule with automated snapshots, one copy replicated to a second cloud region and one immutable copy with a locked retention window that its own admins cannot delete. Its entire environment is infrastructure as code (chapter 8.2), so it can stand up a fresh stack from source. Once a quarter it runs a real restore into a scratch environment on a Friday afternoon, times it, and files a short note. The first drill took nine hours and found a missing migration step; the fix is why the next one took three.

**Enterprise.** A multinational bank operates under regulatory recovery requirements that mandate tested continuity for critical services. It runs warm standby in a second region for its core banking platform, with synchronous replication inside a metro pair for near-zero RPO and asynchronous replication to a distant region for regional-disaster survival. A business impact analysis assigns every service an RTO and RPO, and a central team maps upstream dependencies including two SaaS providers flagged as concentration risk. Twice a year it performs a full regulator-witnessed failover, measures actual against target, and feeds the gaps into the next cycle. A separate cyber-recovery programme maintains immutable vault copies and a clean-room runbook, tested independently of the natural-disaster drills.

**Government.** A national agency delivering benefits maintains a continuity of operations (COOP) programme built to sustain its essential functions during any disruption. Following [continuity of operations](https://en.wikipedia.org/wiki/Continuity_of_Operations) practice and the NIST SP 800-34 contingency-planning guidance that supports its FISMA obligations, it identifies essential functions, orders their recovery, and names successors and alternate facilities so decisions never stall for lack of an authorized person. Citizen-facing systems carry documented RTO and RPO, backups follow the 3-2-1 rule with air-gapped copies, and infrastructure is defined as code for rebuild in an alternate region. An annual full exercise, plus tabletop drills for a ransomware scenario, tests the plan against measured recovery, and the results are reported to oversight bodies as evidence that essential services survive the bad day.

## Business case: motivations, ROI, and TCO

The return on DR and continuity is avoided catastrophe, which is genuinely hard to value until you need it and painfully concrete when you do. Frame it as risk management: the expected cost of a disruption is its likelihood times its impact, and impact for a large organization runs from lost revenue per hour of downtime through regulatory penalties, breach-notification costs, and the reputational damage that outlives the outage. A single unrecoverable ransomware event has ended companies and, in the public sector, has taken essential citizen services offline for weeks. Against that, the cost of a tested recovery capability is modest and knowable.

The total cost of ownership (TCO) is real and ongoing: standby infrastructure, replication bandwidth, backup storage (multiplied by immutable and offline copies), and the engineering time to build automation and run drills. This is exactly why you tier by RTO and RPO instead of buying active-active everywhere, so spend tracks the value of each system rather than a blanket policy. To make the case to leadership, translate the plan into their language: here is the downtime and data loss we can survive today, here is the gap to our targets, here is what closing it costs, and here is the exposure if we do not. The most persuasive artefact is a measured drill, because a recovery you have demonstrated is a number leadership can trust, and an untested plan is a liability disguised as an asset.

## Anti-patterns and pitfalls

- **Untested backups.** A restore you have never performed is a hope; the drill is where you find the corruption, the missing key, and the wrong volume.
- **Backups reachable from production.** If ransomware can encrypt or delete your backups, you have one copy, not three. Keep one immutable and offline.
- **One RTO and RPO for everything.** Blanket tiers over-protect the trivial and under-protect the critical; tier from a business impact analysis.
- **Confusing DR with BCP.** Restoring every server while nobody knows who declares a disaster or how to reach staff is a recovered system and a failed business.
- **Hand-built recovery environments.** Infrastructure you cannot rebuild from code drifts, and drift is discovered mid-failover.
- **Ignored dependencies.** Recovering an app before its database, identity provider, or DNS just produces a second outage.
- **Plan rot.** A binder written once and never exercised describes a system that no longer exists.
- **Supplier blind spots.** Your recovery is capped by your critical suppliers' recovery, and concentration risk is invisible until they fail together.

## Maturity model

- **Level 1, Initiate:** Recovery is ad hoc and reactive. Backups may run but restores are untested. There are no agreed RTO or RPO, no business impact analysis, and recovery is improvised during the incident. A serious data loss or ransomware event would likely be unrecoverable.
- **Level 2, Develop:** Basic practices exist but they are inconsistent across teams. Some critical systems have backups following the 3-2-1 rule and documented RTO and RPO for the most important services, and a basic DR plan exists with restores tested occasionally. Coverage is partial, dependencies are not mapped, drills are ad hoc, and one team's discipline does not imply the next one's.
- **Level 3, Standardize:** Recovery practice is documented and enforced organization-wide. A business impact analysis drives tiered RTO and RPO across systems, recovery strategies are matched to those tiers, environments are infrastructure as code, dependencies and recovery order are mapped, and scheduled drills (tabletop, game day, and failover) run to a defined cadence. A cyber-recovery plan with immutable, offline copies is documented and applied consistently rather than left to individual teams.
- **Level 4, Manage:** Recovery is measured and controlled against baselines. Every drill captures the actual RTO and RPO achieved and tracks the gap to target, and metrics such as restore success rate, the fraction of critical systems recovered end to end within the past year, backup coverage and immutability, and monitored replication lag as the real RPO are reported on dashboards. Deviations trigger action, tiering is re-derived from data on how systems are actually used, and go or no-go decisions rest on evidence rather than on the numbers written on a slide.
- **Level 5, Orchestrate:** Recovery is continuously improved, integrated across the organization, and adaptive. Failover and cyber-recovery clean-room restores are rehearsed as routine, supplier and concentration risk is actively managed, and continuity is integrated with reliability (chapter 9.1) and incident response (chapter 9.3) so the organization recovers predictably from failures it has never seen and re-scopes its recovery posture as the system landscape and threat picture shift.

## Ideas for discussion

1. Which of your critical systems has never been restored end to end, and what would it take to prove it can be?
2. If you lost your primary cloud region for a full day, which business processes stop, and in what order would you bring systems back?
3. How much of your recovery depends on suppliers whose own recovery you cannot see or test?
4. Where are you paying for a recovery tier the business impact analysis does not justify, and where are you under-protecting?
5. If your backups were reachable and encrypted tonight, what is your genuine last known-clean restore point?
6. What is the honest gap between your promised RTO and RPO and the ones your last drill actually achieved?

## Key takeaways

- **Continuity is the goal; recovery is a means.** Business continuity planning keeps the organization running; disaster recovery restores the IT systems it depends on.
- **RTO and RPO drive everything**, and both come from a business impact analysis, not from engineering guesswork. Tier systems rather than protecting all equally.
- **An untested backup is not a backup.** Follow the 3-2-1 rule, keep at least one immutable and offline copy against ransomware, and test restores on a schedule.
- **Match the DR strategy to the number:** backup-and-restore, pilot light, warm standby, or active-active, chosen by each system's RTO and RPO.
- **Replication trades consistency for freshness** (chapter 3.3); your real RPO is your replication lag, not your design doc.
- **Rebuild from code** with infrastructure as code (chapter 8.2), and map your dependencies before you need them.
- **Test with tabletop exercises, game days, and full failover drills**, and measure actual versus target RTO and RPO.
- **Plan cyber-recovery separately** with clean-room restore, and connect the whole practice to reliability (chapter 9.1), incident response (chapter 9.3), and compliance (chapter 4.6).

## References and further reading

- ISO 22301, *Security and resilience: Business continuity management systems: Requirements* (the international standard for BCP).
- National Institute of Standards and Technology, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems* (RTO, RPO, and recovery strategies for government systems).
- National Institute of Standards and Technology, *SP 800-61 Rev. 2: Computer Security Incident Handling Guide* (incident and cyber-recovery handling).
- U.S. Federal Emergency Management Agency, *Continuity Guidance Circular* and federal COOP guidance (essential functions and continuity of operations).
- Federal Financial Institutions Examination Council (FFIEC), *Business Continuity Management* booklet (regulatory recovery expectations for financial institutions).
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, eds., *Site Reliability Engineering: How Google Runs Production Systems* (reliability and disaster testing).
- Kelly Shortridge and Aaron Rinehart, *Security Chaos Engineering* (deliberately exercising failure and recovery).
- Cybersecurity and Infrastructure Security Agency (CISA), *#StopRansomware Guide* (ransomware prevention and recovery practice).
