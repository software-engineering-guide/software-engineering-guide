# 2.10 Software configuration management

## Overview and motivation

[Software configuration management](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) is the discipline of identifying the components of a software system, controlling how they change, recording the state of every change, and verifying that what you built and delivered matches what you intended. It answers a question that sounds simple but gets hard at scale: what exactly is in this release, how did it get there, and who approved it? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) treats SCM as a foundational knowledge area for a clear reason: every other engineering activity needs a stable, known configuration to work against.

On a large team, SCM is the connective tissue that keeps thousands of moving parts coherent. Source code, libraries, container images, infrastructure definitions, configuration data, documentation, and test artefacts all change on their own clocks, and a delivered system is one specific combination of specific versions of all of them. Without deliberate configuration management, that combination is unknown and can't be reproduced. You can't recreate a past release, trace a defect to the change that caused it, or say with confidence what's running in production.

Enterprise and government settings raise the stakes. Regulated and public-sector programmes have to show that changes were authorized, reviewed, and recorded; that a delivered build traces back to approved requirements and source; and that nothing entered the system uncontrolled. Here SCM is as much an evidence system as an engineering one. [Version control](https://en.wikipedia.org/wiki/Version_control) (chapter 2.6) manages source history; SCM governs the whole configuration and the controlled process by which it changes. It's closely tied to [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (chapter 8.2), delivery pipelines (chapter 8.1), and audit and assurance (chapter 10.2).

## Key principles

- Everything that determines system behaviour is a [configuration item](https://en.wikipedia.org/wiki/Configuration_item) under control, not just source code.
- A [baseline](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) is a known, agreed reference point; changes are made against baselines deliberately, not casually.
- Change is controlled and recorded, not prevented; the goal is authorized, traceable change.
- Status accounting means you can always answer what is in a configuration and what its change history is.
- Audits verify that the built and delivered system matches the recorded configuration and approved requirements.
- Reproducibility is non-negotiable: any released version must be rebuildable from controlled inputs.
- Automate identification, recording, and verification; manual bookkeeping does not scale and does not survive audit.

## Recommendations

### Define the SCM process and assign ownership

Write down an SCM plan that says what's under configuration control, how items are identified, how changes are proposed and approved, and how status is recorded and audited. Assign clear ownership, such as a configuration manager or an accountable team, so SCM isn't everyone's job and therefore no one's. Scale the process to the risk: a small internal tool needs light-touch control, while a safety-critical or regulated system needs formal boards and records. Anchor the plan in a recognized standard such as IEEE 828 so auditors and partners can follow it.

### Identify configuration items and establish baselines

List the configuration items that determine how the system behaves: source, dependencies, build scripts, container images, infrastructure definitions, configuration data, schemas, and key documents. Give each one a stable identifier and a versioning scheme. Set baselines at meaningful points (a released version, an approved requirements set, a certified build) so you have an agreed reference to change against and to return to. A baseline is immutable: once you declare it, you don't edit it. You only supersede it with a new baseline created through the change process.

### Control change through a defined process and appropriate boards

Route changes to controlled items through a defined path: proposal, impact assessment, approval, implementation, and verification. For higher-risk items, use a [change control board](https://en.wikipedia.org/wiki/Change_control_board) (CCB) that weighs cost, risk, and schedule before it authorizes a change. Right-size the board: a lightweight automated gate for routine code changes, and a formal cross-functional CCB for changes that touch baselines, interfaces, or regulated behaviour. Record each decision and the reasoning behind it, and connect significant configuration decisions to decision records (chapter 1.6) so the reasoning survives.

### Maintain configuration status accounting

Keep an accurate, queryable record of every configuration item: its current version, which baseline it belongs to, and the change requests applied to it. This status accounting is what lets you answer, at any moment, what a release contains and how it got there. Generate the record automatically from your tools of record (version control, pipeline, artefact registry) instead of maintaining a parallel spreadsheet that drifts from reality. This record is the backbone of traceability from requirement to change to build to deployment.

### Conduct configuration audits

Verify two things on a regular schedule. A functional configuration audit confirms that the configuration performs the way its requirements specify. A physical configuration audit confirms that the delivered artefacts match the recorded configuration: that the build came from the recorded source and dependencies and contains nothing unaccounted for. Automate as much of this as you can: [reproducible builds](https://en.wikipedia.org/wiki/Reproducible_builds), artefact checksums, software bills of materials (SBOMs), and provenance attestations turn auditing from a manual inspection into a continuous check.

### Manage releases and delivery as controlled events

Treat a release as a specific, identified baseline delivered through a repeatable process. Version your releases explicitly, produce a manifest or bill of materials that describes exactly what's included, and record the mapping from release to source revision to deployed artefact. Sign and checksum released artefacts so anyone downstream can verify their integrity. Tie release management into the delivery pipeline (chapter 8.1) so promotion through environments is itself controlled, recorded, and reversible.

### Choose and integrate SCM tooling

Lean on tools that automate identification, control, accounting, and audit rather than relying on discipline alone: version control for source, artefact and image registries for binaries, an immutable pipeline for builds, infrastructure as code for environments, and dependency and SBOM tooling for provenance. Connect them so a single change flows traceably from commit to deployed release. What you're after is a toolchain where the configuration record is a byproduct of doing the work, not a separate clerical chore.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| Formal change control boards | Strong authorization and audit trail; risk weighed before change | Slower throughput; overhead if applied to routine changes |
| Lightweight automated gates | Fast flow; low overhead; scales to many changes | Weaker for high-risk baselines; less deliberation |
| Strict immutable baselines | Reproducible, auditable reference points | Discipline and tooling required; friction if overused |
| Automated status accounting | Accurate, always-current record; audit-ready | Upfront tooling and integration investment |
| Manual configuration records | Simple to start; no tooling needed | Drifts from reality; fails at scale and under audit |

The central trade-off is control versus flow. Heavy change control gives strong assurance but slows delivery. Light control flows fast but weakens traceability. The answer isn't to pick one globally; it is to tier control by risk: automate routine changes through fast gates, and reserve formal boards and immutable baselines for the items where authorization and auditability genuinely matter. The second trade-off is upfront tooling investment versus ongoing clerical cost and audit risk. Automated accounting costs more to set up and far less to live with.

## Questions to discuss with your team

1. **What exactly belongs on our configuration-item list, and who owns the decision when something new appears?** SCM only works if the list of controlled items matches the set of things that actually determine behaviour, and on a large system that set is larger than most teams think: source, dependencies, build scripts, container images, infrastructure definitions, schemas, feature flags, and the configuration data that quietly changes what the software does. If nobody owns the list, it goes stale, and the item that took you down in production turns out to be the one thing no one thought to control. Bring your current inventory to the meeting and hunt for behaviour-determining items that are missing from it. Assign an accountable owner (a configuration manager or a named team) so adding a new item is a deliberate decision, not an accident, because SCM that is everyone's job is no one's job.

2. **Can we prove a deployed artefact came from the source and pipeline we think it did, and would that proof survive tampering?** Reproducibility and traceability are the whole point of SCM, and the sharp version of the question is whether you can link the running binary back to a specific commit and build run with evidence, not assertion. In a regulated or high-value system this is also your supply-chain defence: signed provenance attestations, artefact checksums, and a software bill of materials turn "we are pretty sure" into something an auditor or an incident responder can verify. Bring your last release and try to walk it backward from the deployed artefact to the approved change. If any hop is a manual claim rather than a recorded, verifiable link, that is where an attacker or an honest mistake can slip something in unnoticed, and closing it means wiring signing and provenance into the pipeline so the record is a byproduct of delivery.

3. **Is anyone able to edit a release in place today, and what would that do to our ability to trust it?** A baseline is only useful if it is immutable: the moment "the release" can be edited after the fact, you can no longer reproduce it or rely on it as a reference, and every downstream audit becomes archaeology. The classic failure is config edited directly in production or a tag quietly moved, which is exactly the shortcut that feels harmless and makes a release impossible to reconstruct later. Bring the honest answer to the meeting: who has the access to change a deployed baseline without going through the change process, and has it happened? The fix is to make baselines genuinely immutable and to route every change through proposal, impact assessment, approval, and verification, tiering the rigour so routine changes flow through fast automated gates while baseline and regulated changes go to a board.

4. **Is our configuration status accounting generated automatically from our tools of record, or maintained by hand, and how far has it drifted from what is actually deployed?** Status accounting is the record that lets you answer, at any moment, what a release contains and how it got there, and on a large system that record is only trustworthy if it falls out of the work rather than being typed into a parallel spreadsheet. The competing pull is that a hand-kept register feels cheap to start and flexible, while automating it means integrating version control, the pipeline, and the artefact registry so the record becomes a byproduct of delivery. Bring the register you rely on today, pick three recent releases at random, and check whether the recorded versions, baselines, and applied change requests match what the tooling says shipped. For an enterprise or government programme, a status record that diverges from reality is not a tidiness problem, it is an audit finding waiting to happen, because an auditor who catches one gap stops trusting the whole account and asks you to reconstruct it by hand.

5. **Is our change control tiered by risk, or does the same level of ceremony govern every change regardless of what it touches?** Control and flow pull against each other: a formal change control board weighs cost, risk, and schedule before it authorizes a change, but applying that ceremony to a routine code tweak just adds delay, while pushing a shared baseline or a regulated payment flow through a fast automated gate removes deliberation exactly where you need it. The failure modes are symmetric, uniform heaviness that people learn to route around, or uniform laxity that lets a high-risk change slip through unexamined. Bring a sample of last quarter's changes sorted by what each one touched, and check whether the rigour it received actually matched its risk. In a regulated or public-sector setting, name which item classes must reach a cross-functional board and which may flow through automated gates, and record that tiering explicitly, because "we use judgement" is not a control an auditor or an oversight body can verify.

6. **When did we last run a functional and a physical configuration audit, and how much of the evidence would be a live record rather than a reconstruction?** A functional configuration audit confirms the system performs the way its requirements specify, and a physical configuration audit confirms the delivered artefacts match the recorded configuration and contain nothing unaccounted for; skip them and you are trusting that your baselines and status accounting are honest without ever checking. The tension is cost: manual audits are slow and painful, which is exactly why teams defer them, and the way out is to automate the checks with reproducible builds, artefact checksums, software bills of materials, and provenance attestations so verification becomes continuous. Bring your most recent release and try to produce, on the spot, the requirement-to-change-to-build-to-deployment trace and the artefact-to-source proof. For enterprise and government programmes, this evidence trail is what certification and oversight demand, so the honest question is whether tomorrow's audit would be answered from records you already hold or from an archaeology exercise you cannot afford.

## Sector lens

**Startup.** Keep SCM light but real. Put source, infrastructure definitions, and config data in version control, and make every release a tagged build produced by one pipeline rather than a hand-assembled artefact. Skip change control boards and formal baselines, which are overkill at your size, but never let anyone edit config directly in production, because that single shortcut is what makes a release impossible to reproduce when a customer hits a bug next Tuesday.

**Small business.** With no configuration manager and a tight budget, lean on tools that give you SCM almost for free: a hosted version-control platform, its built-in pipeline, and an artefact registry, so the configuration record is a byproduct rather than a job you have to staff. Buy this capability embedded in tools you already pay for instead of building a bespoke process. Spend your scarce attention on the two habits that matter most, reproducible tagged releases and keeping behaviour-changing config out of manual production edits.

**Enterprise.** The problem is consistency across many teams: a shared SCM plan, a common configuration-item taxonomy, tiered change control, and status accounting generated automatically from version control, the artefact registry, and the pipeline. Reserve formal change control boards and immutable baselines for shared platform and regulated flows, let routine changes flow through automated gates, and standardize signed provenance and SBOMs so any team's release can be traced and any auditor can query a live record instead of commissioning a reconstruction.

**Government.** Procurement rules, transparency, and public accountability shape the process. Follow a formal SCM plan aligned to a recognized standard such as IEEE 828, baseline configuration items at contractual milestones, and route every change to a controlled baseline through a board that records impact, decision, and rationale. Require that delivered artefacts be reproducible from controlled inputs, checksummed, and traceable end to end from approved requirement to delivered build, because that documented evidence trail is exactly what certification, audit, and public oversight demand.

## Examples

**Startup.** A six-person startup keeps its SCM light but real: source, infrastructure definitions, and config data all live in version control, and every release is a tagged, versioned build produced by the same pipeline rather than assembled by hand. When a customer reports a bug that appeared last Tuesday, they trace the deployed artefact back to the exact commit in minutes instead of guessing. They skip change control boards and formal baselines, which would be overkill at their size, but they refuse to let anyone edit config directly in production, because that one shortcut is what makes a release impossible to reproduce later.

**Enterprise.** A large financial-services company places all deployable artefacts, infrastructure definitions, and configuration data under configuration control. Every release is an immutable, versioned baseline with a generated software bill of materials, and each deployed artefact carries a signed provenance attestation linking it to a specific source revision and pipeline run. Routine application changes flow through automated pipeline gates, while changes to shared platform baselines or regulated payment flows go to a change control board. Status accounting is generated automatically from version control, the artefact registry, and the pipeline, so auditors query a live record instead of asking for a reconstruction.

**Government.** A defence programme follows a formal SCM plan aligned to IEEE 828. Configuration items are listed and baselined at contractual milestones, and a change control board authorizes every change to a controlled baseline, recording impact, decision, and rationale. Functional configuration audits confirm the delivered system meets specified requirements, and physical configuration audits confirm delivered artefacts match the recorded configuration exactly. Releases are reproducible from controlled inputs, checksummed, and traceable end to end, from approved requirement through change request to delivered build, which is exactly the evidence trail that certification and oversight demand.

## Business case: motivations, ROI, and TCO

SCM exists to control risk and cost across a system's life. The return comes from reproducibility and traceability: you can recreate any release, trace defects to the changes that caused them, and answer audit questions from records instead of archaeology. That shrinks incident diagnosis time, reduces the cost and length of audits, and prevents the expensive class of failure where no one can say what's running or how to rebuild it.

Total cost of ownership favours automation. Manual configuration records are cheap to start and steadily expensive to maintain, and they fail exactly when you need them most, during an incident or an audit, because they've drifted from reality. Automated identification, accounting, and audit cost more upfront but turn the configuration record into a near-free byproduct of the delivery pipeline. To make the case to leadership, frame SCM as the control that makes releases reproducible and changes auditable, and weigh it against the cost of unreproducible releases, prolonged audits, and the compliance risk of uncontrolled change.

## Anti-patterns and pitfalls

- **Configuration by tribal knowledge:** the true contents of a release live only in an engineer's head, not in any record.
- **Mutable baselines:** "the release" is edited in place, so it can no longer be reproduced or trusted as a reference.
- **Uncontrolled configuration data:** code is version-controlled but the config that changes its behaviour is edited ad hoc in production.
- **Change control theater:** a board that rubber-stamps everything, adding delay without adding real scrutiny.
- **Manual status accounting:** a spreadsheet of versions that silently diverges from what is actually deployed.
- **Unreproducible builds:** releases that cannot be rebuilt from controlled inputs, so audits and rebuilds become guesswork.
- **Untraceable releases:** no mapping from deployed artefact back to source revision, change request, and approval.

## Maturity model

- **Level 1 (Initiate):** SCM is ad hoc and reactive. Only source is controlled; releases are assembled by hand; there are no baselines, no reliable record of what is deployed, and no way to reproduce a past build.
- **Level 2 (Develop):** Basic practices exist but vary from team to team. Some systems define configuration items and a change process and version their releases, baselines exist here and there, but records are partly manual and the rigour of control is inconsistent across the organization.
- **Level 3 (Standardize):** Practices are documented and enforced organization-wide. A common configuration-item taxonomy, immutable baselines, tiered change control, and status accounting are established and largely automated; releases are reproducible and traceable, and audits are supported by tooling rather than by memory.
- **Level 4 (Manage):** SCM is measured and controlled with data. Reproducibility rate, traceability coverage from requirement to deployed artefact, change lead time through each control tier, configuration-drift incidents, and audit findings are tracked against baselines and targets. Deviations trigger correction, and each go or no-go decision rests on this evidence rather than on assertion.
- **Level 5 (Orchestrate):** SCM is continuously improved and integrated across the organization. Fully automated and continuously verified with reproducible builds, SBOMs, provenance attestations, and live status accounting, the process is woven into delivery, security, and audit, and it adapts as risk and delivery outcomes shift, retiring and re-scoping controls on evidence.

## Ideas for discussion

- Can you reproduce your last release exactly from controlled inputs today, and how long would it take?
- Which configuration items determine behaviour but are not actually under control, especially configuration data and infrastructure?
- Is your change control tiered by risk, or does it add uniform overhead or uniform laxity everywhere?
- Where does your configuration record live, and how far has it drifted from what is actually deployed?
- What evidence could you produce in an audit tomorrow, and how much of it would be reconstruction rather than record?
- How do reproducible builds, SBOMs, and provenance change what your audits can verify automatically?

## Key takeaways

- SCM controls the whole configuration (code, dependencies, infrastructure, and config data), not just source.
- Baselines are immutable reference points; change is authorized and recorded against them, not prevented.
- Status accounting must let you answer, at any moment, what a release contains and how it got there.
- Audits verify that what was built and delivered matches the recorded configuration and approved requirements.
- Tier control by risk and automate identification, accounting, and audit so the record is a byproduct of delivery.

## References and further reading

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
