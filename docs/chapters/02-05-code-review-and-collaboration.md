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

Keep each change focused on a single logical concern and small enough to review carefully. Large PRs get shallow reviews. Give a clear description of what changed, why, and how you verified it, so the reviewer has context. Split mechanical refactors and behavior changes into separate PRs, so each one is easy to reason about. A good description is the author's single most important contribution to review quality.

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

1. **What counts as too big for one pull request, and do you split mechanical refactors from behavior changes?** This chapter states plainly that large PRs get shallow reviews and that the author owns reviewability, and it asks you to separate refactors from behavior changes so each is easy to reason about. On a large team a giant PR guarantees a rubber stamp, which gives false assurance while letting real defects through. Bring the evidence: your distribution of PR sizes and how review depth drops as diffs grow. Agree a practical size norm and a habit of landing pure refactors separately from logic changes, so a reviewer can actually hold each change in their head. That single discipline lifts the quality of every review that follows.

2. **How do you distinguish a blocking objection from an optional suggestion, and is that convention actually used?** The chapter asks you to separate blocking issues from preferences and be explicit about which is which, and it flags blocking on preference as a corrosive anti-pattern. Without a shared convention, a reviewer's style opinion reads as a required change, which breeds resentment and slows delivery across the whole team. Bring examples from recent reviews where a preference stalled a merge as the concrete signal. Adopt a lightweight marker, for example a prefix that tags non-blocking notes, so authors know instantly what must change versus what is a suggestion. That keeps review focused on correctness and design rather than taste.

3. **Who must approve changes to security-sensitive or compliance-relevant code, and how is that routing enforced?** This chapter describes role-based approvals, code-ownership rules, and segregation of duties where no one person controls an entire sensitive change, with the approval recorded as audit evidence. In enterprise and government settings these are required controls, and the risk is that they either get skipped or turn into a bottleneck that freezes delivery. Bring the signal: which modules are sensitive, and whether ownership rules currently route those changes to the right approvers automatically. Encode the routing in code-ownership configuration and pair it with automated checks and small changes, so the control is satisfied without a human gatekeeping queue. Decide this deliberately rather than discovering the gap during an audit.

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

- **Level 1, Initial:** Review is inconsistent or skipped; mechanical issues dominate; feedback norms are unset.
- **Level 2, Repeatable:** Review is required but slow and variable; automation is partial; PR size and quality vary widely.
- **Level 3, Defined:** Small PRs, automated mechanical checks, clear standards and feedback norms, and monitored latency.
- **Level 4, Optimizing:** Review depth is matched to risk, latency is low and tracked, pairing and AI assistance are used deliberately, and review measurably improves quality and knowledge spread.

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
