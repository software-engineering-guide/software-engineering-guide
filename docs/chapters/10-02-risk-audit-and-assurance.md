# 10.2 Risk, audit, and assurance

## Overview and motivation

Risk, audit, and assurance is the practice of understanding what could go wrong: with your software and with the organization that builds and runs it. You decide what to do about it. Then you prove that the controls you claim to have actually work. You prove it to executives, regulators, auditors, and the public. On a small team, [risk management](https://en.wikipedia.org/wiki/Risk_management) is mostly implicit. A few people hold the whole picture in their heads. In a large enterprise or government agency, you have to make risk explicit and systematic. No one person can see the whole surface. The consequences of failure are large and often regulated. Trust has to be shown, not assumed.

This matters more for large organizations, for three reasons. First, scale multiplies exposure. More systems, suppliers, data, people, and connections mean more ways to fail and a bigger blast radius when failure comes. Second, large organizations answer to outsiders (regulators, auditors, boards, courts, and citizens) who want evidence, not assurances. Third, concentration creeps in quietly. Shared platforms, common suppliers, and reused components create [single points of failure](https://en.wikipedia.org/wiki/Single_point_of_failure) that no single team notices, yet that can take down the whole enterprise at once.

This chapter aims to bring enterprise risk-management discipline to software without smothering delivery in bureaucracy. Done well, risk and assurance are not a tax on engineering. They are how a large organization earns the right to operate at scale. They turn "trust us" into "here is the evidence."

## Key principles

- **Risk is managed, not eliminated.** The job is to identify, assess, treat, and monitor risk to an accepted level, not to pretend it can be reduced to zero.
- **Own risk where it is created.** The team that builds and runs a system owns its risk; central functions set standards and check, they do not absorb accountability.
- **Evidence over assertion.** A control you cannot demonstrate is a control you do not have.
- **Continuous over point-in-time.** Annual [audits](https://en.wikipedia.org/wiki/Audit) catch drift too late; controls should be monitored continuously and automatically where possible.
- **Third parties inherit your risk.** Your suppliers' weaknesses become your weaknesses; supply-chain risk is your risk.
- **Concentration is a first-class risk.** Efficiency through consolidation quietly creates single points of failure that must be named and managed.
- **Proportionality.** Match the depth of control to the consequence; treating every system as maximum-criticality wastes effort and breeds evasion.

## Recommendations

### Apply enterprise risk management to software

Adopt a common risk framework and vocabulary across the organization, so you can compare and add up risks. Keep a [risk register](https://en.wikipedia.org/wiki/Risk_register) for each significant system, and roll the individual registers up to a portfolio view. For each risk, record likelihood, impact, owner, current controls, and treatment decision (accept, mitigate, transfer, or avoid). Use the ["three lines"](https://en.wikipedia.org/wiki/Three_lines_of_defence) model to separate duties: teams own and manage their risks (first line), risk and compliance functions set policy and challenge (second line), and internal audit independently assures (third line). Set an explicit [risk appetite](https://en.wikipedia.org/wiki/Risk_appetite) at the top, so teams know how much risk the organization is willing to carry instead of each team guessing.

### Assure third-party and supply-chain risk

Inventory your suppliers and, just as important, your software dependencies, including transitive open-source components. Assess each supplier in proportion to the access and criticality it carries. Lean on recognized attestations (such as SOC 2, an independent audit report on a provider's security controls, or [ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) reports) rather than reinventing questionnaires where good evidence already exists. Require a software bill of materials (SBOM) for the components you consume, so you can answer "are we affected?" the moment a vulnerability breaks. Build supply-chain integrity into your pipeline: verify provenance, pin and sign artifacts, and control what enters your build. Write security, breach-notification, audit-rights, and exit terms into contracts. Reassess suppliers on a regular cadence, rather than only at onboarding.

### Build audit trails, evidence, and continuous controls monitoring

Design systems to produce evidence as a by-product of running. Capture immutable, time-stamped, tamper-evident audit logs of significant actions: who did what, to what, when, and with what authorization. Protect those logs from being changed by the very people they record. Favour controls that are automated and continuously monitored: policy-as-code that blocks non-compliant changes, pipeline gates that enforce required reviews, and dashboards that show control status in real time. Continuous controls monitoring turns audit from a periodic scramble to reconstruct evidence into a steady stream of assurance. It catches drift within hours instead of at the next annual review.

### Govern business continuity and disaster recovery

Know what your organization must keep doing, and how fast, if systems fail. Run a business-impact analysis to set recovery-time and recovery-point objectives (RTO/RPO) per service based on business need, not engineering convenience. Then maintain the [business-continuity](https://en.wikipedia.org/wiki/Business_continuity_planning) and [disaster-recovery](https://en.wikipedia.org/wiki/Disaster_recovery) (DR) plans and (this is the part organizations skip) actually test them. Run regular exercises that include full failover and restore-from-backup drills. Untested backups and untested failover are assumptions, not capabilities. Govern this at the enterprise level, so you understand cross-system dependencies before a real disaster, not during it.

### Manage concentration risk and single points of failure

Go looking, on purpose, for the places where many services depend on one thing: a single cloud region, one authentication provider, one key supplier, one database, one person. Map these concentrations at the portfolio level, because individual teams cannot see them. For the most critical, reduce concentration through redundancy, multi-region or multi-supplier strategies, and graceful degradation, while weighing the added cost and complexity honestly. Where you accept concentration for efficiency, make it a conscious, documented, owned decision with a tested backup plan. Do not let it be an accident nobody noticed until it failed.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Heavy formal controls | Strong assurance; audit- and regulator-ready | Slows delivery; invites checkbox compliance and evasion |
| Lightweight risk-based controls | Fast; effort focused on real exposure | Requires mature judgment; gaps if risk assessed poorly |
| Point-in-time audit | Familiar; clear pass/fail moment | Catches drift late; incentive to prepare only for audit day |
| Continuous controls monitoring | Early drift detection; less audit scramble | Upfront automation investment; tooling and instrumentation cost |
| Consolidation / single supplier | Lower cost; simpler; volume leverage | Concentration risk; single point of failure; lock-in |
| Redundancy / multi-supplier | Resilience; no single point of failure | Higher cost and complexity; more to maintain and secure |

The recurring trade-off is assurance versus velocity. The resolution is proportionality plus automation. Blanket heavy controls slow everyone down and, worse, teach teams to treat compliance as theatre to be gamed. Purely lightweight controls depend on judgment that not every team has. The way through: match control depth to consequence, and automate controls into the delivery pipeline so that assurance comes from the act of building rather than bolted on afterward. The concentration trade-off (efficiency versus resilience) has no universal answer. Decide it consciously for each critical dependency, with the accepted risk documented and a backup plan tested.

## Questions to discuss with your team

1. **How will you classify systems by criticality so control depth matches consequence?** Proportionality is the resolution to the assurance-versus-velocity tension: treat every system as maximum-criticality and you waste effort and teach teams to game compliance, treat nothing as critical and you get caught exposed. You need an explicit tiering that ties each system to a risk appetite set at the top, so a low-stakes internal tool and a citizen-facing benefits system do not carry the same controls. Bring evidence to the discussion: list your systems, the data and blast radius each carries, and the controls currently applied, then look for the mismatches in both directions. The answer should change what you automate into the pipeline versus what you leave to human judgment, and it should give teams a clear basis for daily trade-offs instead of guessing. Without agreed tiers, proportionality is just a word.

2. **Can you answer "are we affected?" within minutes the next time a critical dependency discloses a vulnerability?** When a widely used component breaks, the organizations that respond fast already have an SBOM inventory that maps every place a component is used, including transitive open-source dependencies. If your honest answer is days, or "we would have to go look," that gap is the difference between a contained response and a scramble. Bring the evidence: pick a real library you depend on and time how long it takes to list every service that ships it. The answer should drive investment in generating SBOMs in the pipeline, pinning and signing artifacts, and verifying provenance, so exposure is a query rather than an investigation. This is supply-chain risk, and your suppliers' weaknesses are already your weaknesses.

3. **Which services get full failover and restore-from-backup drills, how often, and who signs off that they passed?** Untested backups and untested failover are assumptions, not capabilities, and organizations discover this during a real disaster rather than before one. Run a business-impact analysis to set recovery-time and recovery-point objectives per service from business need, then tie drill frequency to those tiers. Bring evidence: for your most critical service, when was the last full restore actually exercised end to end, and did it meet the stated RTO? The answer should produce a schedule of routine, cross-system DR exercises whose results are reported to leadership, because governance at the enterprise level is what surfaces the cross-system dependencies a single team cannot see. Where you accept a single-region or single-supplier concentration for efficiency, make it a conscious, documented, owned decision with a tested backup plan.

4. **Which of your controls produce evidence automatically as a by-product of running, and which still depend on someone assembling proof at audit time?** A control you cannot demonstrate is a control you do not have, and the organizations that survive audits calmly are the ones whose pipelines emit immutable, time-stamped records of significant actions without anyone remembering to collect them. The competing pull is real: automating controls into policy-as-code and continuous monitoring costs upfront engineering effort, whereas point-in-time evidence gathering feels cheaper until the annual scramble arrives and drift has already accumulated for months. Bring evidence to the discussion: for your top handful of controls, ask whether the proof exists in a tamper-evident store right now, whether the people the logs record can alter them, and how many hours it would take to reconstruct a quarter of activity. The answer should steer investment toward continuous controls monitoring and pipeline gates over manual attestation. In enterprise and government settings, the strongest position is giving auditors read access to live control dashboards, turning audit from a periodic reconstruction into ongoing sampling of a steady evidence stream.

5. **Do the three lines of defence actually operate as separated duties, or has ownership blurred so that the people who build a system also assure it?** Independence is the whole point of the model: teams own and manage their risks in the first line, risk and compliance set policy and challenge in the second, and internal audit assures independently in the third, and when those roles collapse into one another the assurance becomes self-marking homework. The tension is that pushing risk ownership out to delivery teams can feel slower and more contentious than letting a central function absorb it, yet central absorption quietly removes accountability from where the risk is actually created. Bring evidence: map a recent significant risk decision and name who owned it, who challenged it, and who independently assured it, then check whether any single group played two of those parts. The discussion should also surface whether a risk appetite is set explicitly at the top, because without one each team guesses how much risk to carry. For a regulated enterprise or a government agency, an accountable official who formally accepts residual risk, distinct from the team that built the system, is often a hard requirement rather than a nicety.

6. **Where do many of your services quietly depend on one thing, and who at the portfolio level owns that concentration?** Consolidation onto a single cloud region, one authentication provider, one key supplier, one database, or one person delivers real efficiency and volume leverage, and it just as reliably manufactures single points of failure that no individual team can see because each team sees only its own slice. The honest trade-off is efficiency versus resilience, and it has no universal answer: redundancy and multi-region or multi-supplier strategies buy resilience at the cost of money, complexity, and more surface to secure. Bring evidence: attempt a portfolio-level map of shared dependencies and look for the choke points where a single outage cascades across many services, then check which of those concentrations anyone actually owns. The answer should convert accidental concentration into conscious, documented, contingency-tested decisions for the most critical dependencies. In enterprise and government portfolios, a regional outage that exposes a single-region citizen-facing service is exactly the failure that regulators and the public will scrutinize afterward, so map it before the disaster rather than during it.

## Sector lens

**Startup.** With a handful of people and no runway for a risk department, make assurance a by-product of building rather than a separate function. Keep one short risk register with an owner and a treatment decision per entry, lean on your cloud provider's SOC 2 report instead of writing controls from scratch, and generate an SBOM in the pipeline so "are we exposed?" is a query on the day a dependency flaw lands. Name your single glaring concentration out loud, usually the one person who can deploy, and pair someone with them so the knowledge is not trapped in one head.

**Small business.** You have no dedicated risk or audit specialist and a tight budget, so buy assurance rather than build it: prefer suppliers whose SOC 2 or ISO 27001 attestations already carry the evidence you would otherwise have to produce. Spend your limited effort where consequence is highest, a single risk register and a monthly restore-from-backup drill beat an elaborate framework nobody maintains. Treat contracts as a control, writing breach-notification and exit terms into supplier agreements so you inherit less of their risk blind.

**Enterprise.** The defining problem is scale across many teams: run the three-lines model, keep per-service risk registers that roll up to a board-level portfolio view, and set an explicit risk appetite at the top so teams stop guessing. Encode key controls as policy-as-code enforced in the pipeline, give auditors read access to live control dashboards instead of preparing for annual audits, and map concentration risk at the portfolio level because no single team can see the shared choke points. Match control depth to consequence through explicit criticality tiers so proportionality is real rather than a slogan.

**Government.** Procurement rules, transparency, and public accountability shape every choice. Follow a formal authorization process in which an accountable official accepts residual risk, maintain continuous monitoring so authorization is an ongoing state rather than a one-time certificate, and write audit-rights and data-portability terms into vendor contracts. Because a regional outage that exposes a single-region citizen-facing service becomes a public matter, mandate multi-region failover and tested restores for the most critical services, and report disaster-recovery exercise results to leadership on a fixed cadence.

## Examples

**Startup.** A six-person health-tech startup handling patient data cannot afford a risk department, so it makes assurance a by-product of building. It keeps one short risk register in a shared doc, with an owner and a treatment decision for each entry, and reviews it at the Friday standup. It leans on its cloud provider's SOC 2 report rather than writing its own controls from scratch, generates an SBOM in the pipeline so it can answer "are we exposed?" the day a dependency flaw lands, and runs a restore-from-backup drill every month because an untested backup is only a hope. It also names its one glaring concentration risk out loud: the single founder who can deploy, and pairs a second engineer with him so that knowledge is not trapped in one head.

**Enterprise.** A payments company operates under continuous regulatory scrutiny. It runs the three-lines model. It maintains per-service risk registers rolled up to a board-level dashboard. It encodes its key controls as policy-as-code, enforced in the deployment pipeline. Change approvals, access grants, and configuration changes emit immutable audit events into a tamper-evident store. Rather than preparing for annual audits, the company gives auditors read access to live control dashboards, turning audit into sampling of continuous evidence. When a widely used open-source library discloses a critical flaw, the company's SBOM inventory answers "where are we exposed?" in minutes.

**Government.** A national government agency follows a formal authorization process before any system may operate. It requires documented controls, an independent assessment, and an accountable official who accepts residual risk. It maintains continuous monitoring, so authorization is an ongoing state rather than a one-time certificate. A regional cloud outage once exposed a single-region dependency in a citizen-facing benefits system. In response, the agency mapped [concentration risk](https://en.wikipedia.org/wiki/Concentration_risk) across its portfolio, mandated multi-region failover and tested restores for its most critical services, and now runs periodic disaster-recovery exercises whose results are reported to leadership.

## Business case: motivations, ROI, and TCO

The return on risk and assurance is dominated by avoided catastrophic loss: a major breach, a regulatory penalty, a prolonged outage of a critical service, or a supply-chain compromise. These events are individually rare but individually enormous. A single avoided incident can exceed the multi-year cost of the entire assurance programme. Beyond loss avoidance, mature assurance lowers the ongoing cost of compliance, because evidence is produced automatically rather than assembled in a panic. It makes it easier to win regulated business and pass customer due-diligence. And it speeds incident response, because you already know your exposure.

The adoption cost includes risk and audit staff, tooling for monitoring and evidence, and the engineering effort to automate controls into pipelines. The cost of *not* adopting is the expected value of the catastrophes you did not prevent, plus the slow tax of manual audit preparation and the reputational damage that compounds after any public failure. When you make the case to leadership, quantify a small number of plausible worst cases and their likelihood. Frame continuous controls monitoring as trading a large, unpredictable, occasional loss for a small, steady, predictable cost. Emphasize total cost of ownership: a control automated once pays down audit cost every year thereafter.

## Anti-patterns and pitfalls

- **Checkbox compliance.** Producing documents that satisfy an auditor while the real control does not function.
- **Audit-day theatre.** Systems that are compliant only in the weeks before the annual audit and drift the rest of the year.
- **Risk register as a graveyard.** A register that is filled once and never revisited, disconnected from actual decisions.
- **Untested DR.** Backup and failover plans that have never been exercised and therefore do not work when needed.
- **Supplier trust by logo.** Assuming a well-known vendor is secure without evidence, and ignoring transitive dependencies entirely.
- **Invisible concentration.** Consolidating onto one region, supplier, or person for efficiency without anyone owning the resulting single point of failure.
- **Assurance as a delivery blocker.** Heavy central controls with no proportionality, which teams route around, creating shadow systems with no assurance at all.
- **Logs the actor can edit.** Audit trails that the people being audited can alter, which prove nothing.

## Maturity model

**Level 1: Initiate.** Risk is handled reactively after incidents. No shared framework or register exists. Controls are undocumented and unverified, and audits are painful, manual scrambles. Concentration and supplier risk are unexamined, and single points of failure surface only when they fail.

**Level 2: Develop.** Basic practices appear but vary by team. Some risk registers exist for major systems, and a control framework is adopted so audits pass, but preparation is manual and point-in-time. Key suppliers are assessed at onboarding and not after. Backups exist but are rarely tested, and only some single points of failure are known.

**Level 3: Standardize.** The three-lines model and a common framework are documented and enforced org-wide, giving one risk vocabulary that lets you compare and roll up exposure. Many controls are automated into pipelines, and continuous monitoring covers key controls. Supplier and dependency inventories, including SBOMs, are maintained; DR is tested on a schedule; and concentration risk is mapped at the portfolio level rather than left to individual teams.

**Level 4: Manage.** Assurance is measured and controlled against baselines rather than merely documented. Control coverage, drift-detection time, DR-drill pass rates against stated RTO and RPO, mean time to answer "are we affected?" after a disclosure, and residual risk versus the stated risk appetite are all tracked as metrics and reported to leadership. Deviations from baseline trigger action, kill criteria and remediation deadlines are enforced on evidence, and each significant go or no-go decision is made against the numbers rather than by assertion.

**Level 5: Orchestrate.** Assurance is continuously improved and integrated across the organization. Auditors sample live evidence, risk appetite drives proportional controls that adapt as the risk profile shifts, and supply-chain integrity is verified in the pipeline. DR exercises are routine and cross-system, concentration decisions are conscious, owned, and contingency-tested, and risk and assurance are woven into portfolio and strategic planning so the organization rebalances controls as its exposure changes.

## Ideas for discussion

- How do you set a meaningful risk appetite that teams can actually use to make daily trade-offs?
- What is the right boundary between controls automated in the pipeline and controls that require human judgment?
- When is accepting concentration risk for efficiency the right call, and how do you keep that decision honest over time?
- How much supply-chain assurance is proportionate for a small transitive dependency versus a critical vendor with deep access?
- Can continuous controls monitoring ever fully replace independent audit, or does independence require a human outsider?
- How do you prevent risk and assurance functions from becoming a delivery bottleneck that teams route around?

## Key takeaways

- Risk is managed to an accepted level, owned where it is created, and proven with evidence rather than assertion.
- Prefer continuous, automated controls monitoring over point-in-time audits so drift is caught early and evidence is produced as a by-product of operation.
- Third-party and supply-chain risk (including transitive open-source dependencies) is your risk; inventory it, demand SBOMs, and verify provenance.
- Business continuity and DR are capabilities only if tested; untested backups and failover are assumptions.
- Concentration risk and single points of failure are portfolio-level concerns invisible to individual teams; map them and make consolidation a conscious, contingency-tested decision.
- The business case is dominated by avoided catastrophe; trade a large unpredictable occasional loss for a small steady predictable cost.

## References and further reading

- ISO 31000, *Risk Management: Guidelines*
- ISO/IEC 27001 and 27005, *Information Security Management* and *Information Security Risk Management*
- NIST, *Risk Management Framework (SP 800-37)* and *Security and Privacy Controls (SP 800-53)*
- NIST, *Secure Software Development Framework (SP 800-218)* and *Cybersecurity Framework*
- Committee of Sponsoring Organizations of the Treadway Commission (COSO), *Enterprise Risk Management: Integrating with Strategy and Performance*
- AICPA, *SOC 2 Trust Services Criteria*
- The Open Group, *FAIR (Factor Analysis of Information Risk)*
- Betsy Beyer et al., *Site Reliability Engineering* (Google)
- Institute of Internal Auditors, *The Three Lines Model*
