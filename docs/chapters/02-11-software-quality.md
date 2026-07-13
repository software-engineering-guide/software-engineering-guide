# 2.11 Software quality

## Overview and motivation

[Software quality](https://en.wikipedia.org/wiki/Software_quality) is how well a system meets stated needs and reasonable expectations. That means more than whether it works: it means whether the system is reliable, secure, maintainable, usable, performant, and fit for its purpose over time. Quality is broader than testing. Testing (chapter 2.4) is one activity that reveals defects. Quality is the whole discipline of building the right thing well, and of knowing, with evidence, that you've done so. A system can pass every test and still be low quality if it's unmaintainable, inaccessible, or poorly suited to what users actually need.

On a large team, quality can't live in one person's head or one team's habits. Hundreds of engineers, multiple products, and long-lived systems need a shared definition of quality, explicit processes for assuring it, and measurements that tell you whether it's getting better or worse. Without that, "quality" becomes a vague aspiration that loses every argument against a deadline, and defects pile up until change becomes slow and risky.

In enterprise and government settings the stakes climb higher. Regulated, safety-critical, and citizen-facing systems have to demonstrate quality, not just assert it: documented processes, traceable evidence, and independent verification are often mandatory. Poor quality carries direct financial, legal, and reputational cost, and in some domains it puts people in danger. A deliberate quality discipline, built from models, processes, measurement, and culture, is what turns quality from an accident into a managed outcome.

## Key principles

- Quality is fitness for purpose plus conformance to requirements; define both explicitly.
- Quality is built in, not tested in; verification finds defects, but prevention avoids them.
- Distinguish [quality assurance](https://en.wikipedia.org/wiki/Quality_assurance) (are our processes sound?) from [quality control](https://en.wikipedia.org/wiki/Quality_control) (is this product good?).
- Verification asks "did we build it right?"; validation asks "did we build the right thing?"
- Measure quality with a small set of meaningful metrics; treat metrics as signals, not targets.
- The cost of a defect rises the later it is found, so shift quality activities earlier.
- Quality is a property of the whole organization and its culture, not a gate at the end.

## Recommendations

### Adopt a shared quality model such as ISO/IEC 25010

Give your organization a common vocabulary for quality by adopting a recognized product-quality model. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) defines characteristics including functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability. Use it to make quality concrete: for each system, decide which characteristics matter most and what "good enough" means for each. These product-quality characteristics are the same **quality attributes** that drive architecture (chapter 3.1). Quality and architecture are two views of one concern, so let them share one list of priorities rather than two competing ones.

### Separate quality assurance from quality control

Treat quality assurance (QA) and quality control (QC) as distinct but complementary activities. QA is process-oriented and preventive: it improves the way work gets done, through standards, reviews, definitions of done, and training, so defects are less likely to appear in the first place. QC is product-oriented and detective: it inspects actual work products, such as testing, [code review](https://en.wikipedia.org/wiki/Code_review), and audits, to catch defects that did get in. A mature organization invests in both, but leans toward QA, because preventing defects is cheaper than finding and fixing them.

### Run explicit software quality management processes

Make quality a managed process, not a quiet hope. For significant work, write a quality plan that states the target quality characteristics, the assurance and control activities, the acceptance criteria, and who's accountable. Weave it into practices you already have: code review (chapter 2.5) as both a control and a way to share knowledge, testing strategy (chapter 2.4) as the automated safety net, and [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) as continuous inspection. Review the quality data regularly and act on trends, instead of only reacting to incidents.

### Practise verification and validation as distinct disciplines

Verification confirms that work products meet their specifications, so that the right inputs to each stage produce the right outputs, through reviews, static analysis, and testing against requirements. Validation confirms that the finished system actually meets user needs and its intended use, through user testing, acceptance testing, pilots, and field feedback. You need both. A system can be correct against a flawed specification (verified but not valid), or it can address a real need while still containing defects (valid but not verified). In regulated environments, independent [verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) by a party separate from the developers may be required.

### Measure quality with meaningful metrics

Pick a small set of metrics that reflect quality outcomes and their drivers, and watch them over time. Useful measures include defect density, defect escape rate (defects found in production versus before release), mean time to detect and to repair, change-failure rate, code-health signals such as complexity and duplication, and validation signals such as user-reported issues and accessibility conformance. Steer clear of vanity and gameable metrics: a metric that becomes a target stops measuring reality. Pair the numbers with qualitative signals from reviews and user feedback.

### Characterize and manage defects systematically

Treat defects as data, not just fires to put out. Classify them by severity, type, and root cause. Track them from discovery to resolution. Look for patterns so you can prevent recurrence. Use techniques such as [root-cause analysis](https://en.wikipedia.org/wiki/Root_cause_analysis) and defect categorization to tell one-off mistakes apart from systemic weaknesses. Feed what you learn back into QA, through updated standards, added tests, and improved reviews, so the same class of defect doesn't return. A defect fixed without understanding its cause is a defect you've invited back.

### Manage the cost of quality deliberately

Understand quality economics through the classic categories: prevention costs (training, standards, good design, tooling), appraisal costs (reviews, testing, audits), and failure costs (internal rework before release, plus external failures found by users, which cost far more). Shift your investment toward prevention and early appraisal, because every dollar there avoids many dollars of failure cost later. Make these costs visible, so "we have no time for quality" is seen for what it is: a choice to spend more on failure instead.

### Build a quality culture

Make quality everyone's responsibility, owned by the teams that build the software, rather than handed off to a downstream QA department that inspects it at the end. Leaders should reward quality outcomes, make it safe to report defects and near-misses, and treat quality data as a learning tool rather than a stick. A blameless approach to defects brings problems into the open early. A blaming one hides them until they're expensive.

## Trade-offs: pros and cons

| Practice / choice | Pros | Cons |
|---|---|---|
| Formal quality model (ISO 25010) | Shared vocabulary; explicit priorities | Overhead if applied dogmatically |
| Heavy quality assurance (prevention) | Fewer defects; lower total cost | Upfront investment; slower to show payoff |
| Heavy quality control (inspection) | Catches defects that slip through | Expensive; finds defects late |
| Independent V&V | High assurance; objective | Costly; slower; can feel adversarial |
| Rich quality metrics | Visibility; early warning | Gaming risk; measurement overhead |
| Dedicated QA team | Focus and expertise | Can offload responsibility from developers |
| Quality-owned-by-teams | Ownership; fast feedback | Requires discipline and skill throughout |

The central trade-off is investment versus assurance, shaped by timing. Prevention costs money now to avoid larger failure costs later. So the economically right level of quality isn't the maximum; it is the point where the marginal cost of more assurance equals the failure cost it avoids. That point sits high for safety-critical systems and lower for low-stakes internal tools. The other recurring tension is ownership. Central QA groups build expertise but can let developers offload responsibility. Team-owned quality builds ownership but demands skill and discipline everywhere.

## Questions to discuss with your team

1. **When the same class of defect shows up twice, do we run root-cause analysis, or do we just fix it again?** A defect fixed without understanding its cause is a defect you have invited back, and on a large team the same root cause can surface across many services before anyone connects the dots. Treating defects as data (classified by severity, type, and cause, then mined for patterns) is what separates a team that gets steadily more reliable from one that stays busy re-fixing the same mistake. Bring your defect tracker to the meeting and look for recurring signatures: how many recent incidents share a cause you never addressed systemically? The answer should feed prevention, so a recurring cause drives an updated standard, a new shared helper, an added test, or a better review checklist, because that is how a fix in one place stops the whole class from returning.

2. **Is it safe on our team to report a defect or a near-miss, and what happens to the person who raises one?** Quality is a property of culture, and a blameless approach brings problems into the open early while a blaming one hides them until they are expensive, which in a regulated or citizen-facing system can mean a public failure or a penalty. This matters most at scale, where the engineer closest to a risk is often junior and the incentive to stay quiet is strong. Bring honest signals: do near-misses get logged and discussed, or do they vanish? Do postmortems name causes or name people? The action is to make quality data a learning tool rather than a stick, reward the people who surface problems, and run blameless postmortems, because you cannot prevent what your team is afraid to report.

3. **Can validation actually stop a release, and who holds that authority when a deadline is looming?** Verification (did we build it right?) and validation (did we build the right thing?) are distinct disciplines, and validation only has teeth if a failed accessibility check, a failed acceptance test, or damning user research can genuinely block shipping. In enterprise and government settings this is often mandatory, sometimes through independent verification and validation by a party separate from the developers, and "we shipped it anyway" is not an answer an oversight body accepts. Bring your last few releases: did any quality signal ever actually stop one, or does the gate always yield to the date? If validation has never blocked a release, it is decoration, and the fix is to write acceptance criteria into the quality plan up front, name who owns the go/no-go decision, and give that decision real authority independent of the delivery pressure.

4. **Do we actually know our cost of poor quality, and are we deliberately shifting spend from failure toward prevention?** Cost of poor quality (COPQ) is the money lost to internal rework, production incidents, emergency fixes, support load, lost users, and penalties, and it is almost always larger than the visible spend on reviews and testing. On a large team the failure costs are scattered across incident channels, support queues, and rework nobody logs as rework, so they stay invisible until someone adds them up. The tension is that prevention costs money now, in a budget cycle, to avoid failure costs that land later and land on someone else's budget, which makes the trade easy to defer forever. Bring real figures: incident count and cost, rework hours, escaped-defect rate, and the current split of spend across prevention, appraisal, and failure, then decide whether the mix should move earlier. For enterprise and government systems, where most of the lifetime cost lands after first release, put COPQ in front of the people who hold the budget, because a number an oversight body can see is far harder to trade away than a vague appeal to "quality".

5. **Which of our quality metrics have quietly become targets, and what behaviour are they now driving?** A metric that becomes a target stops measuring reality: chase a coverage percentage and you get tests written to move the number, not tests that catch defects. At scale this is dangerous, because a headline dashboard shared across dozens of teams sets the incentives for all of them, and a gameable metric spreads the gaming everywhere at once. The competing consideration is that you still need measurement, so the answer is rarely "drop the metric" but "pair it with a counter-signal and read it alongside qualitative evidence from reviews and users". Bring your current metric set and, for each one, ask what someone under pressure could do to move it without improving quality, and whether you have seen that happen. In regulated and citizen-facing settings, be especially wary of conformance metrics that look green while the underlying validation (accessibility, real user outcomes) was never genuinely exercised, since an auditor will eventually test the reality behind the number.

6. **Who owns quality here: the teams that write the code, or a separate group at the end, and which are we actually resourcing?** Ownership shapes everything downstream, because a downstream QA silo lets developers offload responsibility for the code they write, while team-owned quality builds ownership at the cost of demanding skill and discipline in every team. On a large team this is not either/or: the sustainable pattern is usually teams owning quality through code review and automated tests, supported by a small central group that maintains standards, runs quality assurance as process improvement, and coaches, rather than inspecting quality in at the end. Bring an honest map of where quality work currently happens, who is accountable when a defect escapes, and where budget and headcount actually sit versus where the rhetoric says quality lives. For enterprise and government organizations, add the independent verification and validation requirement: some assurance regimes mandate a separate party, so decide deliberately which controls belong to the delivery teams and which must stay independent to satisfy audit.

## Sector lens

**Startup.** Speed matters more than ceremony, so name the two or three quality characteristics that actually protect your product, usually reliability and maintainability, and let polish wait. Own quality across the whole team with code review and a modest automated test suite rather than standing up a separate QA group you cannot staff. When the same class of bug appears twice, spend twenty minutes on root cause and add one shared helper plus a test, so prevention stays cheap and your change-failure rate stays low while you move fast.

**Small business.** With no dedicated quality specialist and a tight budget, lean on quality that is built into the tools and platforms you buy rather than a process you have to run. When you choose software, treat the vendor's quality evidence as part of the purchase: security posture, accessibility, support responsiveness, and how often their releases break. Track a handful of cheap, honest signals (production incidents, customer-reported issues, time to fix) instead of an elaborate metrics programme you have no one to maintain.

**Enterprise.** The work is consistency across many teams: adopt a shared quality model such as ISO/IEC 25010, separate quality assurance (process) from quality control (product), and run cost-of-quality reviews that shift spend toward prevention. Keep quality owned by the delivery teams, supported by a small central group that maintains standards and dashboards for defect escape rate, change-failure rate, and code-health trends. Standardize the vocabulary and the gates so groups stop reinventing quality practice, while leaving teams room to meet those bars in their own way.

**Government.** Procurement, transparency, and public accountability set the frame, so write quality requirements into contracts and require documented, traceable quality evidence rather than assertions. Expect independent verification and validation by a party separate from the developers, mandatory accessibility conformance, and defect records with severity and root cause kept as part of the audit trail. Report cost-of-poor-quality figures (rework, appeals, service failures) to oversight bodies, and give validation real authority to block a release that would fail the citizens who depend on it.

## Examples

**Startup.** A five-person startup decides that for its early product, reliability and maintainability are the quality characteristics that matter, and lets pixel-perfect polish wait. Quality is owned by the whole team: code review and a modest automated test suite are the controls, and there is no separate QA group to hand defects to. When the same class of bug shows up twice, they spend twenty minutes on a quick root-cause look and add one shared helper plus a test, so it stops recurring instead of being re-fixed by hand each time. That small habit of prevention keeps their change-failure rate low while they are still moving fast.

**Enterprise.** A large financial-services firm adopts ISO/IEC 25010 as its quality vocabulary and, for each product, records target levels for reliability, security, and maintainability. Teams own quality: code review and automated tests are controls in the pipeline, while a small central group runs QA by maintaining standards and coaching. A quality dashboard tracks defect escape rate, change-failure rate, and code-health trends. Defects are classified and root-caused, and recurring causes drive updates to shared libraries and checklists. Leadership reviews cost-of-quality data quarterly and has shifted spend toward prevention, cutting both production incidents and the cost of fixing them.

**Government.** A national agency delivering a citizen-facing benefits platform works under an assurance regime that requires documented quality evidence. It runs a formal quality management process with a quality plan per release, plus independent verification and validation by a team separate from the developers. Verification checks each work product against requirements traced to policy. Validation includes accessibility conformance testing and user research with real citizens, and either can block a release. Defects are tracked with severity and root cause as part of the audit trail, and cost-of-poor-quality figures (rework, appeals, and service failures) go to oversight bodies to justify continued investment in prevention.

## Business case: motivations, ROI, and TCO

The return on quality is lower total cost of ownership and steady delivery speed. The cost of quality has two sides. The good spend, prevention and appraisal, is visible and controllable: design, standards, reviews, testing, and tooling. The cost of poor quality (COPQ) is larger but often hidden: internal rework, production incidents, emergency fixes, customer support, lost users, regulatory penalties, and reputational damage. Studies going back to Crosby's "Quality Is Free" have consistently found that the total cost of poor quality dwarfs the cost of preventing it, and that defects grow far more expensive the later you catch them: an issue found in design costs a fraction of the same issue found in production.

For leadership, the argument isn't "spend more on quality." It's "spend earlier to spend less overall." Quantify COPQ from your own data (incident count and cost, rework hours, escaped-defect rate) and show how prevention and early appraisal bring it down. Connect quality to business outcomes: reliability retains customers, maintainability keeps future change cheap, and security and accessibility keep you out of legal trouble. In long-lived enterprise and government systems, where most of the cost lands after first release, the maintainability and reliability dimensions of quality dominate lifetime cost. That makes early quality investment one of the highest-leverage decisions you can make.

## Anti-patterns and pitfalls

- **Quality as a final gate:** inspecting quality in at the end instead of building it in, so defects are found when they are most expensive.
- **Confusing testing with quality:** assuming that passing tests means high quality, ignoring maintainability, usability, and fitness for purpose.
- **QA as a separate silo:** a downstream team that "owns quality," letting developers offload responsibility for the code they write.
- **Metrics theatre:** chasing coverage percentages or defect counts as targets, which invites gaming and hides real quality.
- **Verification without validation:** building the specification correctly while never checking that the specification meets real needs.
- **No root-cause analysis:** fixing defects individually without addressing the systemic cause, so the same class recurs.
- **Ignoring cost of poor quality:** treating quality as pure cost because failure costs are hidden and unmeasured.

## Maturity model

**Level 1 (Initiate).** Quality is undefined and ad hoc. It rides on individual diligence, gets checked mainly by manual testing at the end, and defects are handled reactively as they surface. There's no shared model, no metrics, and no line between assurance and control.

**Level 2 (Develop).** Basic practices appear: code review, automated tests, and a defect tracker. Some quality data gets collected, but unevenly, and each team does it its own way. Quality is still mostly seen as testing, prevention is minimal, verification happens, and validation is informal.

**Level 3 (Standardize).** The organization adopts a shared quality model (such as ISO/IEC 25010), separates QA from QC, and runs quality management processes with quality plans and acceptance criteria, documented and applied consistently across teams. Verification and validation are distinct and deliberate, and defects are classified and root-caused to an agreed scheme.

**Level 4 (Manage).** Quality is measured and controlled against baselines. A small set of meaningful metrics is tracked over time (defect density, defect escape rate, mean time to detect and repair, change-failure rate, and code-health signals such as complexity and duplication), and cost-of-quality is quantified across prevention, appraisal, and failure. Acceptance and quality gates are enforced on evidence rather than opinion, trends are reviewed on a fixed cadence, and validation can genuinely block a release.

**Level 5 (Orchestrate).** Quality is a continuously improved, culturally owned discipline integrated with business and risk planning. Prevention is the emphasis, cost-of-quality data guides where investment goes, and root-cause findings systematically prevent recurrence. Teams own quality end to end, metrics feed continuous improvement, and the organization adapts its quality practice as products, risks, and regulation shift. This aligns with the higher levels of the maturity models in chapter 10.8.

## Ideas for discussion

- Which ISO/IEC 25010 quality characteristics matter most for your systems, and what is "good enough" for each?
- Where does your organization sit on the prevention-appraisal-failure spending mix, and should it shift?
- Do you distinguish verification from validation in practice, or collapse both into "testing"?
- Is quality owned by the teams that build software, or delegated to a separate group, and what would change if you moved it?
- What is your true cost of poor quality, and could you measure it well enough to make the business case?
- Which of your quality metrics are genuine signals, and which have become gameable targets?

## Key takeaways

- Quality is broader than testing: it is fitness for purpose plus conformance, across characteristics like reliability, security, and maintainability.
- Use a shared quality model (ISO/IEC 25010) so quality attributes are explicit and align with architecture (chapter 3.1).
- Separate quality assurance (prevent, process) from quality control (detect, product), and lean toward prevention.
- Practise verification (built it right) and validation (built the right thing) as distinct disciplines.
- Measure quality with a few meaningful metrics, and characterize defects by severity and root cause to prevent recurrence.
- Manage the cost of quality: prevention and early appraisal are far cheaper than failure, especially in long-lived systems.
- Build a blameless quality culture where teams own quality, supported by code review (chapter 2.5) and testing strategy (chapter 2.4).

## References and further reading

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
