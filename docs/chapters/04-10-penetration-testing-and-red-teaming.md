# 4.10 Penetration testing and red teaming

## Overview and motivation

You can build every control your threat model calls for and still not know whether they work. Documentation says the firewall blocks that port, the code review says input is validated, the policy says least privilege is enforced. Offensive security is how you find out if any of that is true when a motivated attacker pushes on it. This chapter is about deliberately attacking your own systems, under authorization, to find the weaknesses before a real adversary does.

The discipline runs along a spectrum. At the light end sits [vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner): automated tools that probe for known flaws and misconfigurations. In the middle sits [penetration testing](https://en.wikipedia.org/wiki/Penetration_test): a skilled human who chains weaknesses to prove exploitability against a defined target. At the far end sits [red teaming](https://en.wikipedia.org/wiki/Red_team): a goal-driven campaign that emulates a real adversary across people, process, and technology, and that tests your ability to detect and respond, not just your ability to prevent. Each answers a different question, and confusing them is the most common way organizations waste money and comfort themselves with false assurance.

This chapter sits deliberately apart from its neighbors. Chapter 4.4 covers security operations: the defensive, monitoring side that watches for threats and responds to them. This chapter is the offensive counterpart that tests whether that defense actually works. Chapter 4.9 covers the secure software development lifecycle, where security is built into how code is designed and shipped; offensive testing validates the product of that lifecycle from the outside. It also builds on the foundations and culture of chapter 4.1 and the application security practices of chapter 4.2.

For large enterprises, offensive testing is both a risk-reduction tool and a regulatory obligation. Payment processors, banks, and healthcare providers face explicit requirements to test. For government, the stakes reach national security and public trust: adversaries here are well-resourced nation-states, and the systems they target run elections, benefits, and critical infrastructure. In both settings, the value comes not from the report but from what you fix and how much faster you learn to detect the next intrusion.

## Key principles

- Match the engagement to the question: scanning, pen testing, and red teaming answer different things.
- Get written authorization and clear rules of engagement before anyone touches a system.
- Findings are worthless until they are remediated and retested; track them like any other work.
- A red team exists to make the blue team better, not to win.
- Emulate real adversaries and their techniques, not generic checklists.
- Measure detection and response, not just the count of vulnerabilities found.
- Beware theater: an engagement scoped to pass looks impressive and proves nothing.

## Recommendations

### Understand the offensive security spectrum

Start by naming what you are buying. Vulnerability scanning is broad, automated, and cheap; run it continuously against your estate to catch known [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVEs) and misconfigurations. It produces volume and false positives, and it cannot tell you whether a flaw is truly exploitable in context. Penetration testing puts a skilled tester against a defined target for a fixed window, chaining weaknesses to demonstrate real impact: this scanner finding, combined with that weak permission, yields domain administrator. It answers "can this specific thing be broken, and how badly."

Red teaming answers a larger question: "if a determined adversary targeted us, would we notice, and could we stop them." It is goal-oriented (exfiltrate this data set, reach this control system), covers the full attack surface including people and physical access, and is usually run without warning the defenders. [Purple teaming](https://en.wikipedia.org/wiki/Red_team#Purple_team) collapses the wall: red and blue work together in the same room, the attacker runs a technique and the defender watches whether their tooling catches it, tuning detections in real time. Purple teaming often delivers more defensive improvement per dollar than a covert red team, because every action becomes a teaching moment.

### Choose black, grey, or white-box deliberately

How much you tell the tester shapes what you learn. Black-box testing gives them nothing but a target, simulating an external attacker with no inside knowledge; it is realistic but slow, and testers may spend the whole budget on reconnaissance that a real adversary would take months over. White-box testing hands over source code, architecture diagrams, and credentials, letting the tester go deep and cover more ground in the time available. Grey-box sits between: some knowledge, some credentials, mimicking an attacker who has done homework or a malicious insider.

For most application testing, grey or white-box gives better return, because you are paying for depth of analysis, not for the tester to rediscover your subnet layout. Reserve black-box for when the realism of the discovery phase is itself the thing you want to test, such as measuring how much an outsider can learn from your public footprint. Be explicit about which you are commissioning, since a black-box report that finds little may mean you are secure or may mean the tester ran out of time at the perimeter.

### Scope carefully and write the rules of engagement

Scope is where engagements succeed or fail. A [rules of engagement](https://en.wikipedia.org/wiki/Rules_of_engagement) document defines what is in bounds and what is not, which techniques are permitted, the testing window, the systems and networks covered, data handling requirements, and emergency contacts on both sides. It names the production systems that are off-limits or require care, sets a rule for stopping if the tester finds something actively dangerous, and defines what happens if they stumble onto real attacker activity or genuinely sensitive data.

Write down escalation paths and a "get out of jail" letter: authorization the tester can produce if security staff or law enforcement challenge them mid-engagement. Agree in advance on how findings are stored and transmitted, since a pen test report is a map of how to breach you and must be protected accordingly. Narrow scope produces deep findings on a small surface; broad scope produces shallow coverage of a large one. Pick on purpose, and never let scope quietly expand mid-engagement without re-authorization.

### Treat authorization as the line between testing and crime

The single act that separates a penetration tester from a criminal is authorization. Accessing systems you are not authorized to access is a crime under laws such as the [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) in the United States and equivalents elsewhere, and good intentions are no defense. Authorization must come in writing from someone with the actual authority to grant it, cover exactly the systems and techniques in scope, and be signed before work begins.

Third-party systems complicate this. Your cloud provider, your software-as-a-service vendors, and any shared infrastructure may have their own testing policies, and you cannot authorize an attack on assets you do not own. Check provider rules, request permission where required, and keep testing inside your own tenancy. Social engineering that targets employees raises ethical and legal questions about consent and psychological harm that you must think through in advance. When in doubt, involve legal counsel; the cost of a conversation is trivial against the cost of an unauthorized-access incident.

### Weigh internal teams against third-party testers

An internal red team knows your environment, builds relationships with defenders, and can test continuously rather than in annual bursts. That familiarity is also a limitation: they share your blind spots and organizational assumptions, and their independence can be questioned when they report to the same leadership as the systems they test. Third-party firms bring fresh eyes, specialized skills, and the independence that auditors and regulators often demand, but they ramp slowly, cost more per engagement, and leave when the report is delivered.

Most mature programs use both. Internal teams handle continuous adversary emulation, detection tuning, and the deep environmental knowledge that makes purple teaming productive. External firms provide periodic independent validation, meet the independence requirements of standards like PCI DSS, and probe the areas your own people have stopped seeing. Whichever you use, insist that the testers are qualified: certifications such as OSCP (Offensive Security Certified Professional) and demonstrated experience matter more than a polished sales deck.

### Run bug bounties and coordinated disclosure

A [bug bounty](https://en.wikipedia.org/wiki/Bug_bounty_program) program invites external researchers to find and report vulnerabilities in exchange for recognition and payment. It gives you continuous, crowd-sourced testing across a range of skills you could never hire all at once, and you pay only for real findings. It is not a substitute for structured pen testing, since researchers chase what pays and may ignore whole categories, but it is a powerful complement that surfaces creative attacks.

Before you run a paid bounty, you need a [coordinated vulnerability disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) policy: a published, easy-to-find way for anyone to report a security issue safely, a commitment not to pursue good-faith researchers legally, defined response timelines, and an internal process to triage and fix what comes in. A security.txt file and a clear reporting address are the minimum. Government agencies increasingly mandate vulnerability disclosure policies for public-facing systems, and having no channel does not stop researchers from finding bugs; it only stops them from telling you safely.

### Use assumed-breach and adversary emulation

Perimeter-only testing assumes the attacker starts outside, but real breaches often begin with a phished credential or a compromised laptop already inside. An [assumed breach](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) exercise starts the tester with a foothold, such as access as a standard employee, and asks how far they can go from there. This tests your internal segmentation, detection, and blast-radius controls directly, rather than betting everything on a perimeter that will eventually be crossed. It is usually a better use of a red team's time than watching them grind against a hardened edge.

Ground the campaign in real adversary behavior using [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), a public knowledge base of the tactics and techniques attackers actually use, organized from initial access through exfiltration. Adversary emulation picks a threat actor known to target your sector, reproduces their documented techniques, and tests whether you detect and stop each step. This is far more useful than a generic attack, because it maps your defenses against the specific adversaries you face and produces findings your threat intelligence can prioritize.

### Feed findings to the blue team and detection engineering

The point of offense is better defense. Every red team action is a chance to ask: did our tooling generate a signal, did anyone see it, and did they respond correctly. Run engagements so that each technique maps to a detection you either have, need to build, or need to tune. This is detection engineering: turning attacker behavior into reliable alerts, and it is where red team value compounds. A finding that "we were not detected during lateral movement" should become a new detection rule, tested by re-running the technique.

Tabletop exercises extend this to decision-making. Gather the people who would respond to a real incident and walk through a realistic scenario on paper: who declares the incident, who talks to legal, who decides to pull a system offline. Tabletops are cheap, expose gaps in roles and communication that technical tests miss, and prepare the humans who matter most when chapter 9.3 incident management goes live. Pair technical red teaming with regular tabletops so both your tooling and your people are exercised.

### Track remediation and retest

A vulnerability report that no one acts on is a liability, since you now knowingly run a flaw an auditor can cite. Feed every finding into your normal work-tracking system with an owner, a severity, and a due date tied to risk. Critical findings get emergency treatment; lower ones join the backlog with honest priority. The metric that matters is time to remediate, not time to report.

Retesting closes the loop. After a fix ships, the tester (or an automated check) confirms the vulnerability is actually gone and that the fix did not open a new hole. Without retesting, "remediated" is a hope, not a fact, and many findings recur because a fix was incomplete or a regression reintroduced them. Standards like PCI DSS require this loop explicitly. Build retesting into the engagement contract so it is not a forgotten afterthought.

## Trade-offs: pros and cons

| Approach | Best for | Pros | Cons |
|---|---|---|---|
| Vulnerability scanning | Continuous coverage of known flaws | Cheap, broad, automated, frequent | Noisy; cannot prove exploitability |
| Penetration testing | Proving impact on a defined target | Deep, human insight; real exploit chains | Point-in-time; scoped narrowly; costly |
| Red teaming | Testing detection and response | Realistic; exercises people and process | Expensive; slow; needs mature blue team |
| Purple teaming | Improving detections fast | High learning per dollar; collaborative | Less realistic; needs both teams available |
| Bug bounty | Ongoing crowd-sourced discovery | Pay per finding; diverse skills | Uneven coverage; triage burden; needs process |

The core tension is between realism and learning speed. A covert red team is the most realistic test you can run, but its lessons arrive slowly and only after a full campaign, and an immature blue team learns little from being quietly defeated. Purple teaming sacrifices surprise to maximize how fast defenders improve. A second tension is breadth versus depth: scanning covers everything shallowly, while a pen test covers a sliver deeply. Mature programs layer these rather than choosing one, running continuous scanning underneath periodic deep testing and occasional full-scope red team campaigns. The wrong move is to buy a single annual pen test, file the report, and call the problem solved.

## Questions to discuss with your team

1. **When we commission offensive testing, are we clear on which question we are actually asking, and does the engagement match it?** Many organizations buy a "penetration test" and receive a vulnerability scan with a human-written summary, then believe they have tested their defenses when they have only checked for known flaws. Others commission a red team when their detection capability is so immature that the exercise only proves what everyone already knew. Bring your last three engagement scopes and the resulting reports, and ask whether each one answered the question you needed answered: coverage of known vulnerabilities, exploitability of a specific target, or ability to detect and respond to an intrusion. The answer should shape a deliberate mix of scanning, pen testing, and red or purple teaming matched to your maturity.

2. **What happens to a finding after the report lands, and how would we prove it was fixed?** The value of offensive security is entirely in remediation, yet many programs measure success by the size of the report rather than the shrinkage of risk. Trace a real finding from your last engagement: who owned it, how it was prioritized against feature work, when it was fixed, and whether anyone confirmed the fix actually worked. If you cannot produce that trail, your testing is generating knowledge you are not acting on, which is worse than not knowing, because now you are knowingly exposed. The output of this discussion should be a tracked remediation workflow with owners, risk-based deadlines, and mandatory retesting built into every contract.

3. **Is our red team making our blue team better, or is it just keeping score?** A red team that celebrates undetected wins and hoards its techniques is entertaining and useless. The relationship should be collaborative underneath the adversarial surface: every technique that goes undetected should become a new detection rule, every successful path should inform segmentation, and the two teams should debrief together. Ask your defenders what they learned from the last red team engagement and whether any concrete detection or control changed as a result. If the honest answer is nothing, you are paying for theater, and you should shift toward purple teaming and adversary emulation explicitly tied to detection engineering.

## Examples

**Startup.** A twenty-person fintech startup cannot afford an internal red team, so it layers what it can. Automated vulnerability scanning runs on every deploy through its pipeline, catching known dependency flaws early. It publishes a security.txt file and a simple coordinated disclosure policy, then opens a modest bug bounty on a public platform once the product stabilizes, paying real researchers for real bugs. Before signing its first enterprise customer, it commissions a grey-box penetration test of the application from a reputable firm, tracks every finding to closure in its normal issue tracker, and pays for a retest to confirm the fixes. This layered approach gives credible security coverage at a cost the startup can sustain, and the pen test report becomes evidence it can share during customer due diligence.

**Enterprise.** A multinational retailer that processes card payments must meet PCI DSS, which requires both internal and external penetration testing at least annually and after significant changes, plus segmentation testing to prove the cardholder environment is isolated. It runs continuous scanning across thousands of assets, commissions independent external pen tests to satisfy the standard, and maintains an internal red team that runs assumed-breach exercises grounded in MITRE ATT&CK against threat actors known to target retail. The red team works closely with the security operations function of chapter 4.4: every undetected technique becomes a detection engineering ticket, and quarterly purple team sessions tune the alerting. Remediation is tracked with risk-based deadlines, and the whole program produces the audit evidence that chapter 4.6 compliance requires.

**Government.** A national agency running citizen benefits systems faces nation-state adversaries and a public mandate to protect sensitive personal data. It maintains a vulnerability disclosure policy on all public-facing systems, as government directives increasingly require, giving researchers a safe channel to report flaws. Independent third-party assessors conduct penetration tests as part of the authorization process before any system goes live, and continuous monitoring includes ongoing scanning. The agency runs adversary emulation modeled on the specific threat groups its intelligence partners flag, and regular tabletop exercises rehearse the incident response and legal coordination that a real breach would demand. Findings feed a formal remediation program with mandated timelines, and retesting is a precondition for keeping a system's authorization to operate.

## Business case: motivations, ROI, and TCO

The return on offensive security is the breach you did not suffer. A serious data breach costs millions in direct response, regulatory fines, legal liability, customer churn, and reputational damage, and the single most expensive factor is how long an intrusion goes undetected. Red teaming and purple teaming attack that number directly by shrinking the gap between compromise and detection. A penetration test that finds an exploitable path to your customer database, fixed before an attacker finds it, pays for the entire program many times over in a single avoided incident.

There are hard drivers too. PCI DSS mandates penetration testing for anyone handling card data. Frameworks and government authorization regimes require independent assessment before and during operation. Enterprise customers demand recent pen test reports as a condition of contracts. In these cases the testing is not optional, and the question is only whether you extract real security value from money you must spend anyway.

The total cost of ownership includes more than the engagement fee. Budget for the tooling and staff of an internal team if you build one, the triage burden of a bug bounty, and above all the remediation work that findings generate, which is where the real spend lands. A program that commissions tests but underfunds fixing is the worst of both worlds: it pays for the bad news and then pays again when the ignored finding is exploited. To make the case to leadership, connect testing to metrics they track: mean time to detect, mean time to remediate, audit findings closed, and the risk reduction on your most critical assets.

## Anti-patterns and pitfalls

- **Scan-and-rename:** selling a vulnerability scan as a penetration test, delivering a tool's output with no human validation or exploit chaining.
- **Report and forget:** treating the deliverable as the goal, filing the findings, and never tracking remediation or retesting.
- **Scope to pass:** narrowing the engagement so the systems most likely to fail are conveniently out of bounds, producing a clean report that means nothing.
- **Red team as scoreboard:** an adversarial team that hoards techniques and celebrates wins instead of making defenders better.
- **Testing an immature blue team covertly:** running a stealth red team before you have any detection capability, so the exercise proves only what you already knew.
- **No authorization or vague scope:** starting work without written permission, or letting scope creep into systems you do not own, courting legal disaster.
- **Perimeter obsession:** testing only the external edge while ignoring the assumed-breach reality that attackers start inside.
- **Ignoring the disclosure channel:** having no safe way for external researchers to report bugs, so they publish publicly or sell instead.
- **Theater metrics:** counting vulnerabilities found rather than risk reduced, detection improved, and time-to-remediate shortened.

## Maturity model

- **Level 1, Initial:** Testing is occasional and reactive, often a single annual pen test done to check a box. Reports are filed with little follow-through, remediation is untracked, there is no disclosure channel, and detection of a real intrusion is untested and likely absent.
- **Level 2, Managed:** Vulnerability scanning runs regularly and penetration tests are commissioned on a schedule and after major changes. Findings are tracked to closure with owners and deadlines, a coordinated disclosure policy exists, and retesting confirms fixes. Testing is still mostly external and prevention-focused.
- **Level 3, Defined:** Offensive testing is a program, not an event. Assumed-breach exercises and adversary emulation grounded in MITRE ATT&CK are routine, an internal or contracted red team operates continuously, findings feed detection engineering, and tabletop exercises rehearse response. A bug bounty supplements structured testing.
- **Level 4, Optimizing:** Red and purple teaming are tightly coupled to security operations, every technique maps to a tested detection, and the organization measures and improves mean time to detect and respond. Adversary emulation tracks the specific threat actors targeting the sector, and the program continuously refines its scope, techniques, and metrics as it learns.

## Ideas for discussion

1. If a real attacker gained a foothold as a standard employee today, how far could they reach before anyone noticed, and how do you know?
2. Which of your last engagements were genuinely realistic, and which were scoped so the likely failures were conveniently out of bounds?
3. How many findings from your previous test are still open, and what does that say about whether testing or remediation is your real bottleneck?
4. Do external researchers have a safe, obvious way to report a vulnerability to you, and what happens when a report arrives?
5. When did your incident responders last rehearse a breach on paper, and did the tabletop expose gaps your technical tests missed?
6. Are you measuring vulnerabilities found, or are you measuring detection improved and risk reduced?

## Key takeaways

- Offensive security is a spectrum: scanning finds known flaws, pen testing proves exploitability, and red teaming tests detection and response. Match the engagement to the question.
- Authorization in writing and clear rules of engagement are the line between security testing and crime; never skip them, especially on systems you do not fully own.
- The value is in remediation and retesting, not the report. Track every finding with an owner, a risk-based deadline, and a confirmed fix.
- A red team exists to make the blue team better. Feed findings into detection engineering, favor purple teaming and assumed-breach exercises, and ground campaigns in real adversary techniques via MITRE ATT&CK.
- Measure detection and response, not just vulnerability counts, and beware engagements scoped to pass, which produce comfort without security.

## References and further reading

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
