# 4.4 Security operations

## Overview and motivation

Prevention is necessary, but it is never enough. Determined adversaries, novel vulnerabilities, and plain human error mean some threats will slip past your defences. Security operations is the discipline of finding them fast, responding well, and feeding what you learn back into stronger defences. It is the difference between an incident contained in minutes and one that festers for months before anyone notices.

In a large organization, security operations has to work at scale and speed. Thousands of services generate oceans of logs. Hundreds of new vulnerabilities are disclosed every week. Deployment never stops. Manual, artisanal operations simply cannot keep up. The answer is to embed security into the delivery pipeline ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), automate detection and response, and build the muscle to handle incidents calmly when they hit. For government, security operations also carries statutory obligations: mandated incident reporting timelines, coordinated vulnerability disclosure, and forensic rigour that can withstand legal scrutiny.

This chapter covers integrating security into the pipeline, managing vulnerabilities and patching, responding to incidents and conducting forensics, running detection through [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) and SOAR, and validating defences through red and purple teaming and [penetration testing](https://en.wikipedia.org/wiki/Penetration_test).

## Key principles

- **Automate the routine.** Machines handle scanning, correlation, and repetitive response so humans focus on judgement.
- **Shift security into the pipeline.** Testing and gates live in [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (continuous integration and continuous delivery), giving fast feedback where engineers already work.
- **Assume breach and prepare.** Rehearse incident response before you need it; the incident is not the time to improvise.
- **Measure and reduce time.** Mean time to detect and mean time to respond are the metrics that matter most.
- **Blameless learning.** Every incident and near-miss becomes a lesson that hardens the system, not a search for someone to punish.
- **Validate defences adversarially.** Test your security the way real attackers would, then fix what they find.
- **Detection engineering is a product.** Treat detections as code: version-controlled, tested, and continuously improved.

## Recommendations

### Build DevSecOps into the pipeline

Integrate automated security testing directly into continuous integration and delivery so feedback reaches engineers within minutes:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Static Application Security Testing) analyses source code for vulnerable patterns as it is committed.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dynamic Application Security Testing) probes the running application for exploitable flaws.
- **SCA** (Software Composition Analysis) flags known-vulnerable dependencies.
- **IaC scanning** checks infrastructure-as-code for insecure configurations before they deploy.
- **Secret scanning** blocks credentials from entering the repository.

Tune these tools ruthlessly to control false positives. A scanner that cries wolf gets ignored. Set risk-based gates: block on high-severity, high-confidence findings, and track the rest without halting delivery. You want a fast, trusted signal, not a wall of noise.

### Manage vulnerabilities and patch systematically

A steady stream of vulnerabilities calls for a systematic, prioritized process, not a fresh panic with every headline.

- Maintain an accurate asset inventory so you know what could be affected by any given vulnerability.
- Prioritize remediation by real risk: combine severity, exploitability (is it being exploited in the wild?), exposure, and asset criticality rather than patching by raw score alone.
- Define and enforce **remediation SLAs** (service-level agreements) by severity tier, and measure adherence.
- Automate patching where you safely can, especially for infrastructure and dependencies.
- Run a **coordinated vulnerability disclosure** programme with a clear intake channel and, where appropriate, a [bug bounty](https://en.wikipedia.org/wiki/Bug_bounty_program), so external researchers can report flaws responsibly instead of dumping them publicly.

### Prepare for and run incident response

When an incident hits, a rehearsed process is worth more than any tool.

- Maintain an **incident response plan** with defined roles (incident commander, communications lead, investigators), severity classifications, and escalation paths.
- Establish clear phases: **preparation, detection and analysis, containment, eradication, recovery, and post-incident review.**
- Preserve evidence properly for **[forensics](https://en.wikipedia.org/wiki/Digital_forensics)**: capture logs, memory, and disk images with a documented chain of custody so findings hold up legally and analysis is sound.
- Plan **breach communications** in advance: who notifies customers, regulators, and the public, on what timeline, with legal and PR involvement. Regulatory clocks (often 72 hours or less) start ticking at discovery.
- Run **tabletop exercises** regularly so the team knows the plan before a real crisis, and conduct blameless post-incident reviews that produce concrete improvements.

### Operate detection with SIEM and SOAR, and engineer detections

Bring your security signals together and act on them at scale.

- Use a **SIEM** (Security Information and Event Management) to aggregate and correlate logs and events from across the estate, surfacing suspicious patterns.
- Use **SOAR** (Security Orchestration, Automation, and Response) to automate triage and response playbooks: enriching alerts, isolating hosts, disabling credentials, and opening cases without waiting on a human for routine steps.
- Practise **detection engineering**: treat detection rules as versioned, tested code aligned to a framework like [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), measure their true and false positive rates, and continuously improve coverage of real adversary techniques.
- Ensure comprehensive, tamper-resistant logging across applications and infrastructure; you cannot detect what you do not log.

### Validate defences with red and purple teaming and pentesting

Testing your defences the way an attacker would is the only way to know they actually work.

- **Penetration testing** provides focused, point-in-time assessment of specific systems, often for compliance.
- **[Red teaming](https://en.wikipedia.org/wiki/Red_team)** simulates a realistic adversary pursuing objectives across your environment, testing detection and response as well as prevention.
- **Purple teaming** brings attackers (red) and defenders (blue) together collaboratively so that every simulated attack immediately improves detections and controls, turning an exercise into lasting capability.
- Feed all findings back into detection engineering, remediation, and training.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Blocking pipeline gates | Stops known issues from shipping | Friction, false positives frustrate teams |
| Non-blocking scanning | Low friction, fast delivery | Issues may ship; requires discipline to fix |
| In-house SOC | Deep context, full control | Expensive, hard to staff 24/7 |
| Managed detection/response | 24/7 coverage, expertise on tap | Less context, vendor dependency |
| Automated patching | Fast, closes windows quickly | Risk of breaking changes |
| Frequent red teaming | Realistic validation, finds real gaps | Costly, resource-intensive |
| Bug bounty programme | Crowdsourced discovery, good coverage | Triage burden, payout costs, noise |

The core tension is speed versus assurance, and coverage versus cost. Blocking gates and automated patching maximize assurance but add friction and risk. Non-blocking approaches move faster but depend on follow-through. Round-the-clock detection is essential at scale yet expensive to build in-house, which pushes many organizations toward hybrid models. The sustainable path automates the high-confidence routine, saves human attention for genuine judgement, and keeps tuning the balance using measured outcomes rather than fear.

## Questions to discuss with your team

1. **What are your remediation SLAs by severity, and what actually enforces them?** A steady stream of vulnerabilities needs a systematic, prioritized process, not a fresh panic with every headline, and SLAs by severity tier are how you keep pace. Decide your clocks (for example, critical in days, high in weeks) and, just as important, how you measure adherence and who is accountable when a deadline slips. Prioritize by real risk, combining severity with exploitability in the wild, exposure, and asset criticality, rather than patching by raw CVSS score alone. Bring your current backlog of open findings sorted by age and severity, because unpatched criticals sitting past their window are the evidence that matters. If the SLA has no enforcement and no owner, it is a wish, and scanning without remediation just builds audit debt and a false sense of safety.

2. **When an incident hits at 2am, who is the incident commander and how fast does the regulatory clock start?** A rehearsed process is worth more than any tool, so you need named roles (incident commander, communications lead, investigators), defined severity levels, and escalation paths written down before the crisis. Regulatory clocks often run 72 hours or less and start at discovery, so decide in advance who notifies customers, regulators, and the public, and confirm legal and PR are in the loop. Preserving forensic evidence with a documented chain of custody has to happen before anyone rebuilds a compromised host, or you lose the ability to understand or prove what occurred. Bring the date of your last tabletop exercise, because if it was long ago or never, your plan is untested. For government teams, statutory reporting deadlines make this non-optional, so rehearse the notification path, not just the technical response.

3. **Which routine response actions will you let SOAR take without a human in the loop?** Automation is force multiplication that lets a lean team cover a large estate, and the metric that matters is mean time to respond, which automated playbooks can cut from hours to minutes. Decide which high-confidence actions (isolating a host, revoking a credential, opening a case) you trust to run automatically, and which need human judgement first. The risk is a false positive triggering a disruptive action, so tie automation to detection quality and tune ruthlessly, because a system that cries wolf gets switched off. Bring your current alert volume and false-positive rate, because those numbers tell you which playbooks are safe to automate today. If every response step waits on a human, you will not keep up at scale, and dwell time, which drives breach cost, will stay high.

4. **Which pipeline findings block a release, which are only tracked, and who keeps the false-positive rate low enough that engineers still trust the gate?** A scanner that cries wolf gets ignored, and once engineers lose faith in a gate they lobby to remove it, so the value of DevSecOps rests on signal quality rather than raw coverage. The tension is real: block on too little and vulnerable code ships; block on too much and you add friction, slow delivery, and burn goodwill. Bring the true and false positive rates for each scanner (SAST, DAST, SCA, IaC, and secret scanning), how often teams override or suppress a gate, and the age of the findings you merely track without fixing. For an enterprise or government body running hundreds of pipelines, set the block-versus-track policy centrally and tune it with data, because gates that differ arbitrarily from team to team create both audit gaps and the sense that security is capricious.

5. **How confident are you that your detections still cover the techniques a real attacker would use, and who owns them as tested, versioned code?** Detections decay quietly as your environment and your adversaries evolve, so a rule set that looked comprehensive last year can lose coverage long before an incident finally reveals the gap. Treating detections as code, version-controlled, tested, and mapped to a framework such as MITRE ATT&CK, is what separates an engineering practice from a pile of stale alerts, yet it competes for the same scarce analyst time as live triage. Bring your current ATT&CK coverage map, the measured true and false positive rate of your top detections, and the results of your last purple-team exercise, since collaborative red-and-blue testing is the fastest way to prove which detections actually fire. In enterprise and government settings where a framework may be mandated, tie each detection to a named owner and a review cadence, because coverage nobody maintains is coverage you discover you lost only after the breach.

6. **Do you build detection and response in-house, buy managed detection and response, or blend the two, and have you priced what genuine round-the-clock coverage costs?** Dwell time drives breach cost, so the uncovered hours (nights, weekends, holidays) are exactly when an undetected intruder does the most damage, and yet staffing a 24/7 security operations centre in-house is expensive and hard to sustain. The trade is context and control versus cost and speed to coverage: an in-house team knows your estate deeply but is slow and costly to build, while a managed provider gives instant expertise around the clock at the price of thinner context and a vendor dependency. Bring your current coverage hours, your mean time to detect and respond during off-hours, your alert volume, and an honest read on whether you can recruit and retain the analysts a self-run centre needs. For government and regulated enterprises, weigh data residency, personnel clearance, and statutory reporting obligations the provider must be able to meet, and confirm the contract preserves the forensic rigour and chain of custody that legal proceedings demand.

## Sector lens

**Startup.** Speed and survival come first, so buy security as a byproduct of tools you already run rather than staffing operations. Wire free scanners into CI to block secret leaks and known-vulnerable dependencies at commit time, forward logs to a low-cost managed service with a handful of high-value alerts, and write a one-page incident plan (who to call, how to rotate credentials, snapshot before you rebuild) before you ever need it. Your scarcest resource is engineering attention, so automate the routine and resist standing up a security operations centre you cannot keep running.

**Small business.** With no dedicated security specialist and a tight budget, lean on managed detection and response and on the security features already built into your platforms. Treat patching and asset inventory as the highest-leverage habits: know what you run, keep it current, and enforce a simple remediation deadline by severity. Prefer vendors who handle round-the-clock monitoring, coordinated disclosure intake, and forensic capture for you, and rehearse the one thing you cannot outsource, which is deciding who declares an incident and who talks to customers.

**Enterprise.** The challenge is consistency across many teams and hundreds of pipelines: a shared block-versus-track gate policy, remediation SLAs enforced org-wide, a SIEM and SOAR platform with measured detections, and purple teaming that turns every exercise into new coverage. Manage security operations as a portfolio with dashboards for mean time to detect and respond, SLA adherence, and detection precision, and decide deliberately where in-house depth beats managed scale. Budget the human-oversight cost of triage and tuning explicitly, because automation shifts effort rather than removing it.

**Government.** Procurement rules, transparency, and public accountability shape every choice. Statutory incident-reporting deadlines and coordinated vulnerability disclosure are obligations rather than options, so rehearse the notification path to the national authority as carefully as the technical response, and preserve forensic evidence under a chain of custody that withstands legal scrutiny. Favour contracts that keep detection logic and data portable, demand that any managed provider meet residency and clearance requirements, and expect red-team assessments and continuous scanning to feed an authorization process the public can trust.

## Examples

**Startup.** A startup with no security operations centre wires free scanners into its CI pipeline so secret leaks and known-vulnerable dependencies get caught at commit time, blocking only on high-confidence findings so the two engineers are not drowned in noise. They write a one-page incident plan before they need it: who to call, how to rotate credentials, and to snapshot a compromised host before rebuilding it so they can learn what happened. They forward logs to a low-cost managed service and set a few alerts on the events that would actually signal a breach, so a problem shows up in hours rather than the months it takes to notice by accident.

**Enterprise.** A software-as-a-service company runs SAST, SCA, IaC, and secret scanning in every pipeline, blocking only on high-severity, high-confidence findings and tracking the rest on a dashboard with remediation SLAs. A SIEM feeds a SOAR platform that auto-isolates hosts and revokes credentials on high-confidence alerts, cutting mean time to respond from hours to minutes. Quarterly purple-team exercises against MITRE ATT&CK techniques directly generate new detection rules, steadily closing coverage gaps.

**Government.** A federal agency operates a security operations centre (SOC) with mandated incident reporting to a national cyber authority within statutory deadlines. It runs a coordinated vulnerability disclosure programme with a public intake channel as required by policy, and preserves forensic evidence under strict chain-of-custody procedures suitable for legal proceedings. Annual red-team assessments and continuous vulnerability scanning feed the agency's ongoing authorization and its risk-based remediation SLAs.

## Business case: motivations, ROI, and TCO

Almost everything about the case for security operations comes down to dwell time: the longer an attacker goes undetected, the more the breach costs. Studies consistently show that incidents contained quickly cost dramatically less than those that linger for months. The total cost of ownership includes tooling (SIEM, SOAR, scanners), staffing or managed services for detection and response, and the time to build and rehearse incident processes. Against that stands the cost of not investing: a breach discovered late, spreading across systems, drawing regulatory fines, mandatory notifications, litigation, and reputational harm, all made worse by the chaos of an unrehearsed response.

The ROI comes from faster detection and response, automation that lets a lean team cover a large estate, and prevention improvements fed back from every incident and exercise. DevSecOps in particular pays off by catching issues in the pipeline where they are cheap, rather than in production where they are expensive and public. When you make the case to leadership, put numbers on your current mean time to detect and respond, show how those tie to dwell time and cost, and frame automation as force multiplication that avoids growing headcount in lockstep with the estate. For government, stress that statutory reporting and disclosure obligations make mature operations non-optional.

## Anti-patterns and pitfalls

- **Alert fatigue.** So many alerts that analysts tune out and miss the real one.
- **Scanning without remediation.** Generating findings no one fixes, creating a false sense of security and audit debt.
- **No incident plan.** Improvising during a crisis, wasting critical minutes and mishandling evidence.
- **Destroying evidence.** Rebuilding a compromised host before capturing forensics, losing the ability to understand or prove what happened.
- **Blame culture in reviews.** Punishing responders so the next incident is hidden or handled defensively.
- **Compliance-only pentesting.** A single annual test to satisfy an auditor, with findings ignored until next year.
- **Blocking gates with high false positives.** Eroding trust until engineers demand the gates be removed entirely.
- **Set-and-forget detections.** Rules that decay as the environment and adversaries evolve, silently losing coverage.

## Maturity model

**Level 1: Initiate.** Security operations are ad hoc and reactive. Security testing is manual and rare, and there is no central logging or SIEM. No incident plan exists, so response is improvised in the moment. Patching happens only when a headline forces it, and defences are never adversarially tested.

**Level 2: Develop.** Basic practices appear but are inconsistent across teams. Some pipelines run scanners while others run none, and central logging exists in patches. A basic incident plan is documented but rarely rehearsed, patching follows loose timelines, and an annual pentest satisfies compliance without changing much. Coverage and rigour depend on which team you ask.

**Level 3: Standardize.** Practices are documented and enforced org-wide. Full DevSecOps scanning with risk-based gates is applied consistently, a SIEM correlates events, and initial SOAR playbooks run. Incident response is rehearsed with tabletops and blameless reviews, remediation SLAs by severity are enforced with named owners, and coordinated vulnerability disclosure and regular red teaming are the norm rather than the exception.

**Level 4: Manage.** Operations are measured and controlled against baselines. Mean time to detect and respond, SLA adherence by severity tier, scan coverage, detection true and false positive rates, and dwell time are tracked on dashboards and reviewed on a cadence. Detections carry measured precision and recall mapped to MITRE ATT&CK, automation decisions are gated on false-positive data rather than hope, and a metric that drifts past its baseline triggers a defined response instead of going unnoticed.

**Level 5: Orchestrate.** Security operations are continuously improved, integrated across the organization, and adaptive. Detection engineering, purple teaming, remediation, and incident review feed one loop that adapts to new adversary techniques as they emerge. Automated playbooks handle the routine across the whole estate so humans concentrate on judgement, security is planned alongside delivery and risk, and every incident and exercise measurably hardens the system while the core metrics keep trending down.

## Ideas for discussion

1. Which pipeline findings should block a release, and which should merely be tracked?
2. Build an in-house SOC, use managed detection and response, or blend the two, and why?
3. How do you keep detection rules from decaying as your environment evolves?
4. How aggressively should patching be automated given the risk of breaking changes?
5. What does a genuinely blameless post-incident review look like in your culture?
6. How do you measure whether red and purple teaming are actually improving your defences?

## Key takeaways

- Prevention fails eventually; operations exist to detect and respond fast.
- Embed SAST, DAST, SCA, IaC, and secret scanning in the pipeline with risk-based gates.
- Prioritize patching by real exploitability and asset criticality, under enforced SLAs.
- Rehearse incident response, preserve forensic evidence, and plan breach communications in advance.
- Use SIEM and SOAR to correlate and automate; treat detections as engineered, tested code.
- Validate defences with pentesting, red teaming, and collaborative purple teaming.
- Dwell time drives breach cost, so mean time to detect and respond are the metrics that matter.

## References and further reading

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / SIEM literature
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, *Coordinated Vulnerability Disclosure* guidance and *CVSS* specification
