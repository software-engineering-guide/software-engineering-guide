# 6.4 AI-assisted software development

## Overview and motivation

AI coding assistants can now generate code, complete functions, write tests, explain unfamiliar systems, and help you [refactor](https://en.wikipedia.org/wiki/Code_refactoring). Used well, they speed up routine work. They lower the barrier to unfamiliar languages and frameworks. They take the drudgery out of boilerplate.

Used poorly, they cause real harm. They can flood a codebase with plausible-looking but subtly wrong code. They can introduce security holes, create licensing exposure, and erode the skills of the engineers who lean on them. AI-assisted development is a genuine productivity tool and a genuine risk at the same time. The difference lies almost entirely in the engineering discipline around it.

For large teams, the challenge is consistency and safety at scale. When hundreds of developers use AI assistants, small individual habits add up to organizational outcomes. If everyone accepts suggestions uncritically, review load and defect rates rise. If you provide clear norms, good defaults, and strong verification, the same tools raise throughput without lowering quality. The productivity story is also more nuanced than vendor claims suggest. Real gains vary widely by task, and naive measurement, like counting accepted suggestions, will mislead you.

Enterprise and government settings add sharper constraints. Code that touches regulated systems, handles sensitive data, or runs critical infrastructure cannot be trusted just because an AI produced it. Licensing provenance matters when generated code may echo training data under restrictive licences. Some organizations must keep source code on-premises and cannot send it to external services at all. Setting clear, enforceable norms for AI assistance is now part of responsible engineering leadership. Among available assistants, tools built on Anthropic's Claude models are one leading option alongside others; the practices below apply whichever you adopt.

*See also:* chapter 2.5 (code review and collaboration), chapter 2.4 (testing strategy), and chapter 6.5 (responsible and trustworthy AI).

## Key principles

- The engineer, not the assistant, is accountable for every line committed.
- AI-generated code is a draft to be reviewed and verified, never a finished product to be trusted.
- Verification effort should scale with the risk of the code, not with how confident the output looks.
- Measure productivity by outcomes that matter (delivered value, quality, cycle time), not by suggestion counts.
- Protect against security and licensing risks introduced through generated code.
- Preserve and grow human engineering skill; do not let assistants hollow it out.
- Be transparent about where and how AI assistance is used.

## Recommendations

### Use AI pair programming as a drafting and exploration tool

Point assistants at tasks where they shine and mistakes are cheap to catch: boilerplate, test scaffolding, format conversions, explaining unfamiliar code, and exploring approaches. Treat their output as a first draft. Stay in the driver's seat. Read, understand, and edit every suggestion rather than accepting on autopilot. In unfamiliar domains, use the assistant to learn, but check its claims against authoritative documentation. Assistants can invent APIs and misstate behaviour with total confidence.

### Review, test, and verify AI-generated code as untrusted input

Give AI-generated code the same scrutiny you would give code from a new team member, or more. A human reviewer should understand it well enough to explain and maintain it. "The AI wrote it" is never an acceptable answer to "why does this work?" Insist on tests, and watch out for AI-generated tests that merely assert current behaviour rather than intended behaviour. Run [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis), security scanning, and dependency checks. For high-risk code (authentication, [cryptography](https://en.wikipedia.org/wiki/Cryptography), financial logic, safety systems), treat AI output as a starting point that demands expert human verification, never as authoritative.

### Measure productivity honestly and set realistic expectations

Skip vanity metrics like acceptance rate or lines generated. Look instead at delivery and quality signals over time: cycle time, change failure rate, defect escape rate, and developer-reported effectiveness. Gains are real but uneven: large for some tasks, negligible or negative for others. Time saved writing code can be lost again in reviewing and debugging it. Set expectations with leadership accordingly, so investment rests on evidence rather than hype, and so teams are never pressured to accept unsafe suggestions just to hit a metric.

### Manage security and licensing risks

Scan generated code for vulnerabilities and insecure patterns. Assistants can reproduce insecure idioms from their training data. Never paste secrets, credentials, or sensitive data into prompts sent to external services. Prefer tools that meet your data-handling requirements, including on-premises or private deployment where source code cannot leave the environment. Address licensing too. Generated code can resemble licensed training data, so use tools and policies that reduce this risk, keep provenance where you can, and route anything questionable through legal review. Track the provenance of dependencies the assistant suggests, since it may recommend abandoned or malicious packages.

### Set team norms, disclosure, and skill maintenance

Publish clear guidance on when and how AI assistance may be used, what data may never be shared, and what verification each risk level requires. Encourage transparency about AI-assisted contributions where it matters for review and accountability. Keep human skills sharp on purpose. Make sure engineers, especially juniors, still learn the fundamentals rather than outsource their understanding. Rotate people through work that builds deep expertise, and treat over-reliance as a real long-term risk to the team's capability.

## Trade-offs: pros and cons

| Dimension | Benefit of AI assistance | Risk of AI assistance |
|---|---|---|
| Speed | Faster boilerplate and drafting | Time lost reviewing wrong code |
| Onboarding | Easier entry to new languages/frameworks | Shallow understanding, invented APIs |
| Quality | More tests, quicker refactors | Plausible but subtly wrong code |
| Security | Can suggest fixes and scanning | Can introduce vulnerabilities |
| Skills | Frees time for higher-value work | Erodes fundamentals if overused |
| Licensing | Faster reuse of common patterns | Provenance and licence exposure |

The central trade-off is speed versus verification. AI shifts effort from writing to reviewing. The net gain depends on whether your review and verification practices are strong enough to catch what the assistant gets wrong. Weak review leads to quality decline. Strong review and clear norms capture the upside.

## Questions to discuss with your team

1. **Which parts of our codebase are off-limits to AI assistance entirely, and how do we enforce that boundary?** Uniform trust is a trap: applying the same light scrutiny to authentication, cryptography, financial logic, and safety systems as to boilerplate is how subtle, confident errors reach critical paths. For a large team, an explicit list of excluded or expert-review-only modules turns individual judgment into an organizational safeguard. Bring your risk map of the codebase, your current policy (if any), and how you would actually stop generated code from landing in a restricted module: pipeline checks, ownership rules, or review gates. In defence, regulated, and safety-critical settings, some modules should exclude AI assistance completely. The answer should scale verification effort to the risk of the code, never to how confident the output looks.

2. **What are our real change-failure and defect-escape trends since we adopted assistants, and are we measuring them or guessing?** Vendor productivity claims and acceptance-rate counts are vanity metrics that mislead, because time saved writing code can be lost again reviewing and debugging it. For leadership to invest on evidence rather than hype, you need delivery and quality signals over time: cycle time, change-failure rate, defect-escape rate, and developer-reported effectiveness. Bring whatever real numbers you have, and be honest where you have none. The risk to watch is teams pressured to accept unsafe suggestions just to hit a metric. The answer should replace suggestion counts with outcome measures, and set expectations that gains are real but uneven, large for some tasks and negative for others.

3. **If generated code echoes restrictively licensed training data or pulls in a risky dependency, who catches it and when?** Generated code can resemble licensed material or recommend abandoned or malicious packages, and that exposure lands in your product whether or not anyone noticed. For enterprises and government, licensing provenance and supply-chain risk carry legal weight that a "the AI wrote it" shrug does not survive. Bring your current secret scanning, licence checks, and dependency provenance tracking, and identify where in the pipeline each runs. Discuss what routes questionable code to legal review and who owns that call. If secrets can be pasted into external tools or unvetted packages can merge unchallenged, close those gaps before scaling assistant use across the team.

4. **How do we keep engineers, especially juniors, learning the fundamentals rather than outsourcing their understanding to the assistant?** Skill atrophy is a slow risk that never shows up in this quarter's velocity, then shows up years later as a team that cannot debug, design, or review without a prompt. For a large organization, the competing pull is real: assistants let junior engineers ship faster today, and the pressure to hit delivery targets fights against the slower work of building deep expertise. Bring evidence on how your people actually grow: what fraction of juniors can explain the code they merged, how much unassisted problem-solving your onboarding still requires, and whether reviews catch shallow understanding or just rubber-stamp working output. Deliberately rotate people through work that builds mastery, and treat over-reliance as a capability risk, not a personal failing. In government and long-lived critical systems, the workforce may need to build and verify systems for decades without vendor tools, so a training path that guarantees direct fundamentals is a continuity requirement, not a nicety.

5. **Which assistants are we actually permitted to use given where our source code and data must stay, and how do we stop a secret ever reaching a prompt?** Data-handling constraints decide the tool before productivity does: an assistant that streams your source to an external service may be disqualified outright, whatever its capabilities. For a large team the tension is between the convenience of the best hosted tool and the requirement that proprietary code, credentials, and sensitive data never leave your boundary. Bring your data-classification map, the deployment options each candidate tool offers (hosted, private, on-premises), and the concrete controls that keep secrets out of prompts: pre-commit scanning, prompt filtering, and engineer training. Decide which tools are allowed for which classes of code, and make the boundary enforceable rather than advisory. In regulated, defence, and classified settings, an on-premises or air-gapped deployment may be the only lawful option, and sending source to any external service must be prohibited and technically blocked, not merely discouraged.

6. **How do we turn scattered individual habits into consistent org-wide norms, and who owns the policy as tools evolve?** When hundreds of developers each improvise their own approach, small habits compound into organizational outcomes, and inconsistent verification is where defects and exposure slip through. The competing consideration is autonomy: teams resent heavy central mandates, yet a free-for-all produces uneven quality and no shared safeguard. Bring your current guidance (if any), evidence of how uniformly it is followed, and a proposal for good defaults baked into the pipeline so the safe path is the easy path. Name an owner who keeps the policy current as assistants change every few months, and a disclosure norm so reviewers know when AI assistance shaped a contribution. For an enterprise or public body, tie the norms to audit and accountability: a documented, enforced standard that an auditor can inspect beats a folk practice that varies by team and disappears when a key person leaves.

## Sector lens

**Startup.** With a handful of engineers and no runway to waste, lean on hosted assistants for boilerplate, tests, and unfamiliar frameworks, and let them accelerate routine work. Keep one non-negotiable rule: a human who understands the change reviews every merge, because a subtle wrong line in a five-person codebase has nowhere to hide and no one else to catch it. Add a secret scanner and a licence check early; they are cheap and they prevent expensive mistakes you cannot afford to clean up later.

**Small business.** You probably have no security specialist and a tight budget, so prefer assistants embedded in tools you already trust over a bespoke setup you must maintain. Frame the risk in plain terms: never paste customer data or credentials into an external prompt, and treat generated code touching billing or authentication as a draft to verify, not a finished answer. Choose vendors whose data-handling terms you can actually read and whose AI features you can turn off if they misbehave.

**Enterprise.** The problem is consistency and safety across many teams: shared norms by risk level, mandatory review and scanning in the pipeline, and honest delivery-and-quality metrics rather than acceptance counts. Standardize the tool choices and deployment model so proprietary code stays inside your boundary, budget the review and correction cost that assistants shift onto reviewers, and exclude or gate high-risk modules explicitly. Manage AI assistance as a governed capability with an owner, not a scatter of individual habits.

**Government.** Procurement rules, transparency, and public accountability shape every choice. Favour on-premises or private deployment where source code and sensitive data cannot leave the environment, prohibit sending code to external services, and require disclosure of AI-assisted contributions so decisions stay auditable. Mandate security and licensing scans on all generated code, exclude AI assistance from safety-critical and classified modules, and keep a training path that ensures the public workforce can build and verify systems without vendor tools over the long life of the systems it owns.

## Examples

**Startup.** A six-engineer SaaS startup adopted AI coding assistants to move faster on routine work. It leaned on them for boilerplate, tests, and unfamiliar framework code, but kept a firm rule that a human who understood the change had to review every pull request, and it added a secret scanner and a licence check to the pipeline. For the billing and authentication code, engineers treated AI output as a rough draft to verify line by line rather than trust. They watched cycle time and escaped defects rather than counting accepted suggestions, and kept the gains without letting quality slip.

**Enterprise.** A large e-commerce company rolled out AI coding assistants with guardrails. It forbade secrets in prompts. It required human review, with the reviewer expected to understand the code. It added security scanning in the pipeline and chose a private deployment so proprietary code never left its environment. It measured impact through cycle time and change-failure rate rather than acceptance counts. It found solid gains on boilerplate and tests, but insisted on expert review for payment code, where it treated AI output as untrusted.

**Government.** A defence software organization permitted AI assistance only through an on-premises tool that kept classified and sensitive code inside its boundary. It prohibited sending source to any external service. It required disclosure of AI-assisted contributions in code review and mandated security and licensing scans on all generated code. It excluded AI assistance entirely from certain safety-critical modules. Junior engineers followed a training path that ensured they learned fundamentals directly, so the workforce would not lose the ability to build and verify systems without assistance.

## Business case: motivations, ROI, and TCO

The motivation is faster delivery and less drudgery, so your scarce engineering talent can focus on design, judgment, and hard problems. ROI shows up as reduced cycle time for suitable tasks and improved developer experience, but only where verification keeps quality high. Naive ROI claims based on suggestion counts are misleading, and you should reject them.

TCO includes tool licensing, secure or on-premises deployment, security and licensing scanning, and the often-underestimated cost of reviewing and correcting AI output. The cost of *not* adopting is competitive: peers may deliver faster and attract talent who expect modern tools. The cost of adopting carelessly is quality erosion, security incidents, and legal exposure. Make the case to leadership with a pilot that measures real delivery and quality outcomes, paired with a concrete plan for norms, verification, and data protection.

## Anti-patterns and pitfalls

- **Autopilot acceptance.** Committing suggestions without reading or understanding them.
- **Vanity metrics.** Judging success by acceptance rate or lines generated.
- **Secrets in prompts.** Pasting credentials or sensitive data into external tools.
- **Trusting AI tests.** Accepting generated tests that lock in current behaviour, not intended behaviour.
- **Ignoring provenance.** Overlooking licence and dependency risks in generated code.
- **Skill atrophy.** Letting juniors outsource understanding and never learn fundamentals.
- **Uniform trust.** Applying the same low scrutiny to safety-critical code as to boilerplate.

## Maturity model

1. **Initiate.** Individuals use assistants ad hoc and reactively; no policy, no measurement; secrets and intellectual property are at risk, and generated code merges with whatever scrutiny each person happens to apply.
2. **Develop.** Basic usage guidance and data rules exist, and some security scanning runs, but practice is inconsistent across teams: verification depth varies by person, productivity claims are anecdotal, and high-risk code is not reliably gated.
3. **Standardize.** Norms by risk level are documented and enforced org-wide: mandatory human review, security and licensing scans in the pipeline, secure or on-premises deployment where required, disclosure practices, and an explicit list of excluded or expert-review-only modules.
4. **Manage.** The practice is measured and controlled against baselines: cycle time, change-failure rate, and defect-escape rate are tracked before and after adoption, review and correction cost is quantified, secret-leak and licence-exposure incidents are counted, and go or no-go decisions on tools and expansion rest on that evidence rather than on vendor claims.
5. **Orchestrate.** AI assistance is continuously improved and integrated across the organization: verification is built into the pipeline as the default path, skill development is deliberate and tracked, policy adapts as tools change every few months, and the organization routinely re-evaluates, replaces, and re-scopes assistants as the evidence and the risk picture shift.

## Ideas for discussion

- How should verification requirements differ between boilerplate and safety-critical code?
- What productivity metrics actually reflect value from AI assistance in your context?
- When, if ever, should AI-assisted contributions be disclosed?
- How do you prevent skill erosion, especially for junior engineers?
- What data-handling constraints govern which tools you can use?
- How do you manage licensing and provenance risk from generated code?

## Key takeaways

- The engineer remains accountable; AI output is an untrusted draft to be verified.
- Scale verification to risk, and never trust safety-critical AI code without expert review.
- Measure real delivery and quality outcomes, not suggestion counts.
- Protect against security, data-leakage, and licensing risks with policy and tooling.
- Set clear norms and deliberately preserve human engineering skill.

## References and further reading

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
