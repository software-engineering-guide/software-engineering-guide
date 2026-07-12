# 2.5 Code review and collaboration

## Overview and motivation

[Code review](https://en.wikipedia.org/wiki/Code_review) is the practice of having someone other than the author examine a change before it merges. It is one of the highest-leverage quality and knowledge-sharing activities a software organization has, and for large teams it is also a primary mechanism of coordination and culture. Review catches defects, spreads knowledge of the codebase, enforces standards, and mentors engineers, but only when you do it well. Done badly, it becomes a bottleneck, a source of friction, or a rubber stamp that gives false assurance.

For large teams, review is where individual work meets collective ownership. It is often the main touchpoint between engineers who otherwise work on their own, so its norms shape how the whole organization collaborates. Review spreads knowledge so that no part of the system is understood by only one person, which reduces the [bus-factor](https://en.wikipedia.org/wiki/Bus_factor) risk, the danger when knowledge sits with too few people, that plagues large, long-lived systems. It also creates an audit trail of who changed what and who approved it.

In enterprise and government contexts, review often carries a compliance dimension. [Segregation of duties](https://en.wikipedia.org/wiki/Separation_of_duties) (no one person controls an entire sensitive change), mandatory approvals, and traceability are frequently required controls. A change that touches sensitive systems may need review by specific roles, and the review record becomes audit evidence. Your challenge is to satisfy these controls while keeping review fast and constructive, instead of turning it into ceremony.

## Key principles

- Review to improve the change and share knowledge, not to show off.
- Small changes get better reviews, so keep pull requests (PRs) focused and reasonably sized.
- Review latency is a team-wide cost. Fast turnaround keeps everyone moving.
- Automate the mechanical stuff (style, tests, security scans) so humans review design and correctness.
- Separate blocking issues from suggestions and preferences, and be explicit about which is which.
- Critique the code, not the person. Feedback norms shape whether review builds trust or corrodes it.
- The author is responsible for making a change easy to review.

## Recommendations

### Make pull requests small and well-described

Keep each change focused on a single logical concern and small enough to review carefully. Large PRs get shallow reviews. Give a clear description of what changed, why, and how you verified it, so the reviewer has context. Split mechanical refactors and behaviour changes into separate PRs, so each one is easy to reason about. A good description is the author's single most important contribution to review quality.

### Establish review standards and checklists

Spell out what reviewers should look for: correctness, design fit, test adequacy, security implications, readability, and adherence to standards. A lightweight checklist keeps reviews consistent and stops important dimensions from slipping through, without turning review into box-ticking. Define what requires review, who can approve, and any role-based approvals needed for sensitive areas.

### Set and monitor review latency norms

Agree on a target turnaround, for example responding within a working day, and make review a first-class part of the day rather than something squeezed in last. Long review queues stall delivery and tempt engineers into oversized, batched changes. Monitor time-to-first-review and time-to-merge, and treat sustained latency as a process problem to fix, not a personal failing.

### Automate everything mechanical

Run formatting, [linting](https://en.wikipedia.org/wiki/Lint_(software)), tests, and security and dependency scanning in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), so reviewers never spend attention on them. Save human review for the things machines cannot judge: whether the design is right, whether the approach fits the system, whether the tests are meaningful, and whether the code will still make sense later.

### Use pair and mob programming where they fit

Use [pair programming](https://en.wikipedia.org/wiki/Pair_programming), where two engineers write code together at one workstation, for complex or high-risk work, onboarding, and knowledge transfer. It is continuous review, and it often removes the need for a separate review step. Use [mob programming](https://en.wikipedia.org/wiki/Mob_programming), where the whole team works on one task at once, for critical design decisions or for spreading knowledge of a thorny area across the team. Think of these as complements to asynchronous review, chosen by context, not replacements to mandate everywhere.

### Adopt automated and AI-assisted review carefully

Use automated review tools and AI assistants to catch common issues, suggest improvements, and lighten the reviewer's load, but treat their output as input, not authority. AI review is good at surface issues and consistency, and poor at deep design judgment and system context. Keep a human accountable for every approval, especially for security-sensitive and compliance-relevant changes.

### Set constructive feedback norms

Set norms that keep feedback specific, kind, and focused on the code. Encourage reviewers to ask questions rather than issue commands, to explain the reasoning behind a request, and to praise good work. Mark blocking concerns and optional suggestions clearly (for example, by prefixing non-blocking notes). These norms decide whether review strengthens the team or breeds resentment.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Asynchronous PR review | Flexible; documented; scales across time zones | Latency; loses nuance; can feel adversarial |
| Pair programming | Continuous review; fast knowledge transfer; high quality | Two people on one task; tiring; harder to schedule |
| Mob programming | Whole-team alignment; spreads deep knowledge | Expensive in aggregate; not for routine work |
| Mandatory multi-reviewer | Strong assurance; compliance-friendly | Slower; diffuses responsibility; queue pressure |
| AI-assisted review | Fast, tireless on common issues; reduces load | Misses system context; false confidence if over-trusted |

The core tension is thoroughness versus speed. Deeper review catches more, but it slows delivery and can frustrate authors. Faster review keeps flow, but it risks being superficial. The way through is to match review depth to change risk, so trivial changes get a light review and risky changes get a deep one, and to automate away the mechanical work so human effort concentrates where it matters.

## Questions to discuss with your team

1. **What counts as too big for one pull request, and do you split mechanical refactors from behaviour changes?** This chapter states plainly that large PRs get shallow reviews and that the author owns reviewability, and it asks you to separate refactors from behaviour changes so each is easy to reason about. On a large team a giant PR guarantees a rubber stamp, which gives false assurance while letting real defects through. Bring the evidence: your distribution of PR sizes and how review depth drops as diffs grow. Agree a practical size norm and a habit of landing pure refactors separately from logic changes, so a reviewer can actually hold each change in their head. That single discipline lifts the quality of every review that follows.

2. **How do you distinguish a blocking objection from an optional suggestion, and is that convention actually used?** The chapter asks you to separate blocking issues from preferences and be explicit about which is which, and it flags blocking on preference as a corrosive anti-pattern. Without a shared convention, a reviewer's style opinion reads as a required change, which breeds resentment and slows delivery across the whole team. Bring examples from recent reviews where a preference stalled a merge as the concrete signal. Adopt a lightweight marker, for example a prefix that tags non-blocking notes, so authors know instantly what must change versus what is a suggestion. That keeps review focused on correctness and design rather than taste.

3. **Who must approve changes to security-sensitive or compliance-relevant code, and how is that routing enforced?** This chapter describes role-based approvals, code-ownership rules, and segregation of duties where no one person controls an entire sensitive change, with the approval recorded as audit evidence. In enterprise and government settings these are required controls, and the risk is that they either get skipped or turn into a bottleneck that freezes delivery. Bring the signal: which modules are sensitive, and whether ownership rules currently route those changes to the right approvers automatically. Encode the routing in code-ownership configuration and pair it with automated checks and small changes, so the control is satisfied without a human gatekeeping queue. Decide this deliberately rather than discovering the gap during an audit.

4. **What review-latency target have you actually agreed, and do you measure and enforce it, or is it only an aspiration?** The chapter treats review latency as a team-wide cost and asks you to monitor time-to-first-review and time-to-merge, treating sustained delay as a process problem rather than a personal failing. On a large team an unowned review queue quietly taxes everyone: authors batch bigger changes to avoid the wait, those changes then get shallower reviews, and delivery lead time drifts upward with no single culprit. The competing consideration is that a hard latency target can push reviewers to skim, so speed and depth have to be balanced rather than traded blindly. Bring the evidence: your current distribution of time-to-first-review, how it varies by team and by change size, and where reviews sit longest. In enterprise and government settings, tie the target to the flow metrics leadership already tracks, because a mandatory multi-reviewer control with no latency norm becomes the bottleneck that freezes delivery and tempts people to route around the control entirely.

5. **For which kinds of change do you trust automated and AI-assisted review, and where must a human stay accountable?** The chapter says to treat AI review output as input, not authority: strong on surface issues and consistency, weak on deep design judgement and system context, with a human accountable for every approval. Without an explicit boundary, a large team drifts into over-trust, where a green bot comment reads as a passed review and real design and security risks slide through under false confidence. The competing pull is that AI review genuinely lightens load and catches common defects tirelessly, so banning it wastes leverage. Bring the evidence: where automated suggestions have caught real issues, where they have produced noise, and which change types (security-sensitive, compliance-relevant, architectural) you would never let a machine sign off alone. For enterprise and government work, name who holds accountability for an approval when an AI assistant was in the loop, because an audit will ask who reviewed a change, and "the tool did" is not an answer a regulator accepts.

6. **Where should pairing or mobbing replace asynchronous review, and how do you use review to reduce bus-factor risk deliberately?** The chapter frames pair and mob programming as continuous review chosen by context, and it names review as the mechanism that spreads knowledge so no part of the system is understood by only one person. Left implicit, knowledge concentrates: the same expert reviews every change to a subsystem, review turns into a rubber stamp because nobody else can challenge them, and bus-factor risk grows precisely where the system is most critical. The competing consideration is cost, since mobbing spends the whole team's time and pairing ties up two engineers, so you cannot mandate it everywhere. Bring the evidence: which modules have only one credible reviewer, where onboarding stalls, and where a thorny area would benefit from a live session over comment threads. In a large or public organization, treat deliberate knowledge spread as risk management, because a long-lived system whose critical parts depend on one person is an operational and continuity liability, not merely a staffing inconvenience.

## Sector lens

**Startup.** With three or four engineers, keep review lightweight: one teammate's approval on a small pull request, mechanical checks in CI, and no mandatory second reviewer that would stall a merge. The real goal is less compliance than making sure more than one person understands each part of the system, so pair on the risky pieces and treat that as onboarding. Do not build heavy code-ownership routing you will soon outgrow; a shared norm of small, well-described changes buys most of the benefit at almost no cost.

**Small business.** You are unlikely to have a review-tooling specialist, so lean on what your hosting platform (for example a managed Git service) gives you out of the box rather than building custom automation. Buy the linting, test, and security-scanning integrations instead of maintaining them, so your few engineers spend their scarce review minutes on design and correctness. Keep one simple rule, every change gets one other set of eyes, and resist adding process you have nobody to maintain.

**Enterprise.** The challenge is consistency across many teams: shared standards, code-ownership rules that route sensitive changes to the right approvers, and role-based approvals recorded as audit evidence. Automate the mechanical checks organization-wide so human review concentrates on design, and track review latency as a flow metric so mandatory multi-reviewer controls do not silently become bottlenecks. Match review depth to change risk with a documented policy, so trivial changes stay fast while high-risk ones get segregation of duties and deeper scrutiny.

**Government.** Change control is often mandatory: every production change reviewed and approved by someone other than the author, with the record kept as audit evidence to satisfy segregation-of-duties requirements. Favour a transparent, traceable trail of who authored, who approved, and which checks passed, and invest in automation and small, frequent changes so the control does not freeze delivery. Where review tooling is procured, demand exportable audit logs and avoid lock-in, since the evidence must outlive any single vendor and stand up to public scrutiny.

## Examples

**Startup.** A four-engineer startup keeps every pull request small and asks for one teammate's approval before merge, less for compliance than to make sure no single person is the only one who understands a part of the system. CI runs the formatter and tests, so the humans spend their few review minutes on design and correctness rather than spacing. When the team hits a thorny piece of the payments flow, two of them pair on it instead of trading asynchronous comments, which doubles as onboarding for the newest hire.

**Enterprise.** A large software company requires at least one approving review on every change, plus a second approval for changes to security-sensitive modules identified by code ownership rules. CI handles all style and test checks, so reviewers focus on design and correctness. The team tracks time-to-first-review and treats a rising median as a signal to rebalance workload. New engineers are onboarded through pairing, which shortens their path to contributing independently.

**Government.** A national agency operating under strict change-control requirements mandates that every production change be reviewed and approved by someone other than the author, with the approval recorded for audit. To keep this control from becoming a bottleneck, the agency invests in automated checks and small, frequent changes, and sets a same-day review-response norm. The review trail, covering who authored, who approved, and what checks passed, becomes part of the compliance evidence for each release, satisfying segregation-of-duties requirements without freezing delivery.

## Business case: motivations, ROI, and TCO

Code review pays you back in three currencies: defects caught before production, knowledge spread across the team, and standards upheld automatically over time. Catching a defect in review is far cheaper than catching it in production, and the knowledge-sharing benefit reduces key-person risk that can otherwise cost an organization dearly when someone leaves. Review is also the cultural transmission mechanism that keeps a growing team coherent.

The cost of review is engineer time and some latency, both of which are manageable with good practices. The cost of *not* reviewing, or of reviewing badly, includes production defects, siloed knowledge, inconsistent code, and, in regulated settings, failed audits and compliance findings. Over-heavy review has its own real cost too: long queues, oversized batches, demoralized engineers. To make the case to leadership, connect review practices to change-failure rate, delivery lead time, and onboarding speed, and track review latency as an explicit flow metric.

## Anti-patterns and pitfalls

- **The rubber stamp:** approvals with no real examination, providing false assurance and satisfying only the letter of a control.
- **The giant PR:** thousands of lines that can only be skimmed, guaranteeing shallow review.
- **Nitpick-only review:** focusing on trivia while missing design and correctness, often because mechanical checks are not automated.
- **Review as gatekeeping:** using review to assert dominance or block others, poisoning collaboration.
- **The slow queue:** reviews that sit for days, stalling delivery and encouraging batching.
- **Over-trusting AI review:** treating automated suggestions as authoritative and dropping human judgment on risky changes.
- **Blocking on preference:** presenting personal style opinions as required changes without distinguishing them from real defects.

## Maturity model

- **Level 1, Initiate:** Review is ad hoc and reactive. It is often skipped or done inconsistently, mechanical issues dominate the comments, feedback norms are unset, and any approval trail is incidental rather than deliberate.
- **Level 2, Develop:** Basic review practices exist but vary from team to team. Review is required in some places and slow or optional in others, automation is partial, and pull-request size and quality swing widely with no shared expectation.
- **Level 3, Standardize:** Standards are documented and enforced organization-wide. Small focused PRs, automated formatting, linting, tests and security scanning in CI, clear checklists, an explicit blocking-versus-suggestion convention, and code-ownership rules that route sensitive changes to the right approvers.
- **Level 4, Manage:** Review is measured and controlled against baselines. Time-to-first-review, time-to-merge, review depth versus change risk, defect-escape rate, and change-failure rate are tracked; sustained latency is treated as a process problem; and the data drives where to rebalance reviewer load and where controls are slowing delivery without adding assurance.
- **Level 5, Orchestrate:** Review is continuously improved and integrated across the organization. Depth adapts to change risk, pairing, mobbing and AI assistance are used deliberately with a human accountable, knowledge spread and bus-factor risk are managed intentionally, and review measurably improves quality, delivery flow, and onboarding.

## Ideas for discussion

- What is the right review-latency target for your team, and what prevents you from hitting it?
- How do you match review depth to change risk without adding bureaucracy?
- Where do pairing or mobbing outperform asynchronous review in your context?
- How much should AI-assisted review be trusted, and for which kinds of changes?
- How do you keep review feedback constructive as the team grows and diversifies?
- How do you satisfy compliance approval requirements without creating bottlenecks?

## Key takeaways

- Keep pull requests small and well-described; the author owns reviewability.
- Automate the mechanical so humans review design, correctness, and tests.
- Track and manage review latency as a team-wide flow cost.
- Match review depth to change risk, and distinguish blocking issues from preferences.
- Use pairing, mobbing, and AI assistance as context-fit complements, keeping a human accountable.

## References and further reading

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
