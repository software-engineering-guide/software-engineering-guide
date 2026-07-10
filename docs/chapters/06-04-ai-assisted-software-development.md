# 6.4 AI-assisted software development

## Overview and motivation

AI coding assistants can now generate code, complete functions, write tests, explain unfamiliar systems, and help you [refactor](https://en.wikipedia.org/wiki/Code_refactoring). Used well, they speed up routine work. They lower the barrier to unfamiliar languages and frameworks. They take the drudgery out of boilerplate.

Used poorly, they cause real harm. They can flood a codebase with plausible-looking but subtly wrong code. They can introduce security holes, create licensing exposure, and erode the skills of the engineers who lean on them. AI-assisted development is a genuine productivity tool and a genuine risk at the same time. The difference lies almost entirely in the engineering discipline around it.

For large teams, the challenge is consistency and safety at scale. When hundreds of developers use AI assistants, small individual habits add up to organizational outcomes. If everyone accepts suggestions uncritically, review load and defect rates rise. If you provide clear norms, good defaults, and strong verification, the same tools raise throughput without lowering quality. The productivity story is also more nuanced than vendor claims suggest. Real gains vary widely by task, and naive measurement, like counting accepted suggestions, will mislead you.

Enterprise and government settings add sharper constraints. Code that touches regulated systems, handles sensitive data, or runs critical infrastructure cannot be trusted just because an AI produced it. Licensing provenance matters when generated code may echo training data under restrictive licenses. Some organizations must keep source code on-premises and cannot send it to external services at all. Setting clear, enforceable norms for AI assistance is now part of responsible engineering leadership. Among available assistants, tools built on Anthropic's Claude models are one leading option alongside others; the practices below apply whichever you adopt.

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

Point assistants at tasks where they shine and mistakes are cheap to catch: boilerplate, test scaffolding, format conversions, explaining unfamiliar code, and exploring approaches. Treat their output as a first draft. Stay in the driver's seat. Read, understand, and edit every suggestion rather than accepting on autopilot. In unfamiliar domains, use the assistant to learn, but check its claims against authoritative documentation. Assistants can invent APIs and misstate behavior with total confidence.

### Review, test, and verify AI-generated code as untrusted input

Give AI-generated code the same scrutiny you would give code from a new team member, or more. A human reviewer should understand it well enough to explain and maintain it. "The AI wrote it" is never an acceptable answer to "why does this work?" Insist on tests, and watch out for AI-generated tests that merely assert current behavior rather than intended behavior. Run [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis), security scanning, and dependency checks. For high-risk code (authentication, [cryptography](https://en.wikipedia.org/wiki/Cryptography), financial logic, safety systems), treat AI output as a starting point that demands expert human verification, never as authoritative.

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
| Licensing | Faster reuse of common patterns | Provenance and license exposure |

The central trade-off is speed versus verification. AI shifts effort from writing to reviewing. The net gain depends on whether your review and verification practices are strong enough to catch what the assistant gets wrong. Weak review leads to quality decline. Strong review and clear norms capture the upside.

## Questions to discuss with your team

1. **Which parts of our codebase are off-limits to AI assistance entirely, and how do we enforce that boundary?** Uniform trust is a trap: applying the same light scrutiny to authentication, cryptography, financial logic, and safety systems as to boilerplate is how subtle, confident errors reach critical paths. For a large team, an explicit list of excluded or expert-review-only modules turns individual judgment into an organizational safeguard. Bring your risk map of the codebase, your current policy (if any), and how you would actually stop generated code from landing in a restricted module: pipeline checks, ownership rules, or review gates. In defense, regulated, and safety-critical settings, some modules should exclude AI assistance completely. The answer should scale verification effort to the risk of the code, never to how confident the output looks.

2. **What are our real change-failure and defect-escape trends since we adopted assistants, and are we measuring them or guessing?** Vendor productivity claims and acceptance-rate counts are vanity metrics that mislead, because time saved writing code can be lost again reviewing and debugging it. For leadership to invest on evidence rather than hype, you need delivery and quality signals over time: cycle time, change-failure rate, defect-escape rate, and developer-reported effectiveness. Bring whatever real numbers you have, and be honest where you have none. The risk to watch is teams pressured to accept unsafe suggestions just to hit a metric. The answer should replace suggestion counts with outcome measures, and set expectations that gains are real but uneven, large for some tasks and negative for others.

3. **If generated code echoes restrictively licensed training data or pulls in a risky dependency, who catches it and when?** Generated code can resemble licensed material or recommend abandoned or malicious packages, and that exposure lands in your product whether or not anyone noticed. For enterprises and government, licensing provenance and supply-chain risk carry legal weight that a "the AI wrote it" shrug does not survive. Bring your current secret scanning, license checks, and dependency provenance tracking, and identify where in the pipeline each runs. Discuss what routes questionable code to legal review and who owns that call. If secrets can be pasted into external tools or unvetted packages can merge unchallenged, close those gaps before scaling assistant use across the team.

## Examples

**Startup.** A six-engineer SaaS startup adopted AI coding assistants to move faster on routine work. It leaned on them for boilerplate, tests, and unfamiliar framework code, but kept a firm rule that a human who understood the change had to review every pull request, and it added a secret scanner and a license check to the pipeline. For the billing and authentication code, engineers treated AI output as a rough draft to verify line by line rather than trust. They watched cycle time and escaped defects rather than counting accepted suggestions, and kept the gains without letting quality slip.

**Enterprise.** A large e-commerce company rolled out AI coding assistants with guardrails. It forbade secrets in prompts. It required human review, with the reviewer expected to understand the code. It added security scanning in the pipeline and chose a private deployment so proprietary code never left its environment. It measured impact through cycle time and change-failure rate rather than acceptance counts. It found solid gains on boilerplate and tests, but insisted on expert review for payment code, where it treated AI output as untrusted.

**Government.** A defense software organization permitted AI assistance only through an on-premises tool that kept classified and sensitive code inside its boundary. It prohibited sending source to any external service. It required disclosure of AI-assisted contributions in code review and mandated security and licensing scans on all generated code. It excluded AI assistance entirely from certain safety-critical modules. Junior engineers followed a training path that ensured they learned fundamentals directly, so the workforce would not lose the ability to build and verify systems without assistance.

## Business case: motivations, ROI, and TCO

The motivation is faster delivery and less drudgery, so your scarce engineering talent can focus on design, judgment, and hard problems. ROI shows up as reduced cycle time for suitable tasks and improved developer experience, but only where verification keeps quality high. Naive ROI claims based on suggestion counts are misleading, and you should reject them.

TCO includes tool licensing, secure or on-premises deployment, security and licensing scanning, and the often-underestimated cost of reviewing and correcting AI output. The cost of *not* adopting is competitive: peers may deliver faster and attract talent who expect modern tools. The cost of adopting carelessly is quality erosion, security incidents, and legal exposure. Make the case to leadership with a pilot that measures real delivery and quality outcomes, paired with a concrete plan for norms, verification, and data protection.

## Anti-patterns and pitfalls

- **Autopilot acceptance.** Committing suggestions without reading or understanding them.
- **Vanity metrics.** Judging success by acceptance rate or lines generated.
- **Secrets in prompts.** Pasting credentials or sensitive data into external tools.
- **Trusting AI tests.** Accepting generated tests that lock in current behavior, not intended behavior.
- **Ignoring provenance.** Overlooking license and dependency risks in generated code.
- **Skill atrophy.** Letting juniors outsource understanding and never learn fundamentals.
- **Uniform trust.** Applying the same low scrutiny to safety-critical code as to boilerplate.

## Maturity model

1. **Initial.** Individuals use assistants ad hoc; no policy; no measurement; secrets and IP at risk.
2. **Developing.** Basic usage guidance and data rules; some security scanning; anecdotal productivity claims.
3. **Defined.** Clear norms by risk level, mandatory review and scanning, honest outcome metrics, secure deployment, and disclosure practices.
4. **Optimizing.** Continuous measurement of delivery and quality impact; strong verification integrated into the pipeline; deliberate skill development; policy adapts as tools evolve.

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
