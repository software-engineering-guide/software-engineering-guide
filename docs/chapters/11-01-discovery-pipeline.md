# 11.1 The discovery pipeline

## Overview and motivation

The discovery pipeline is the flow of work that decides **what to build and why**, and defines **what success will look like**, before and alongside delivery. Where the delivery pipeline (chapter 11.2) turns validated ideas into running software, the discovery pipeline turns problems, evidence, and strategy into a prioritized, testable set of intended outcomes. In modern practice the two run continuously and in parallel, often called *dual-track* development, rather than as sequential phases. Discovery keeps feeding a ready supply of de-risked, well-framed work to delivery, and delivery keeps feeding real-world outcome data back into discovery.

For large teams, a weak discovery pipeline is the most expensive failure mode in software. A team with excellent delivery and poor discovery builds the wrong thing efficiently: it ships fast, hits its velocity targets, and still moves no business metric. The cost is invisible on engineering dashboards and enormous on the balance sheet. The discovery pipeline is how you make that cost visible: it forces goals to be explicit, measurable, and falsifiable before you commit large investments.

Enterprise and government contexts raise the stakes. Enterprises coordinate dozens of teams against a shared strategy, so misaligned local goals compound into wasted portfolios. Government programmes commit multi-year public funding against legislated mandates, where "we built what the contract said" is no defence if the outcome (citizens served, wait times reduced, fraud prevented) never materializes. A disciplined discovery pipeline, expressed through objectives, measures, and explicit quality requirements, is how both keep their intent auditable.

## Key principles

- **Outcomes over outputs.** Measure the change you create for users and the business, not the features you ship.
- **Make intent explicit and measurable.** A goal you cannot measure is an opinion you cannot manage.
- **De-risk before you build.** The cheapest experiment beats the most confident opinion.
- **Discovery and delivery run continuously in parallel**, not as sequential gates.
- **Quality attributes are requirements, not afterthoughts.** Reliability, security, and accessibility are discovered and specified, not hoped for.
- **Alignment beats local optimization.** Nested goals connect team work to strategy.
- **Close the loop.** Delivered outcomes are evidence that re-enters discovery.

## Recommendations

### Frame direction with OKRs

Use **[Objectives and Key Results](https://en.wikipedia.org/wiki/OKR) (OKRs)** to connect strategy to team execution. An *Objective* is a qualitative, inspirational statement of a desired end state ("Make first-time onboarding effortless"). *Key Results* are the small number (typically 2–4) of measurable outcomes that prove the objective is being met ("Increase 7-day activation from 40% to 60%"; "Reduce onboarding support tickets by 30%"). Key results express **outcomes**, not tasks: "ship the new wizard" is a task masquerading as a result.

Cascade OKRs by *alignment*, not dictation: leadership sets a small number of company objectives; teams propose key results and their own objectives that ladder up to them. Set them on a regular cadence (commonly quarterly with an annual frame), review them mid-cycle, and grade them honestly at the end. Keep them separate from performance reviews: OKRs graded for compensation quickly become sandbagged. See chapter 10.1 for how OKRs connect to portfolio and programme management.

### Monitor health with KPIs

Distinguish **[Key Performance Indicators](https://en.wikipedia.org/wiki/Performance_indicator) (KPIs)** from OKRs. OKRs describe the *change* you want this period; KPIs describe the *ongoing health* you must sustain regardless of what you are changing (uptime, conversion rate, cost per transaction, customer satisfaction). A metric can be both (a KPI you are actively trying to move becomes a key result), but most KPIs are guardrails you monitor, not targets you sprint toward.

Classify every important metric as **leading** (predictive and actionable now, such as trial sign-ups) or **lagging** (confirmatory and slow, such as annual revenue). Discovery relies on leading indicators to steer before lagging indicators confirm. Beware vanity metrics that rise reliably but predict nothing (raw page views, total registered users); prefer ratio and cohort metrics that resist gaming. See chapters 7.3 and 7.4 for the analytics and experimentation machinery behind these measures.

### Specify system quality attributes explicitly

Functional requirements say what the system does. **System quality attributes** (the "-ilities": reliability, performance, scalability, security, accessibility, maintainability, operability) say how well it must do it. These are routinely under-discovered: everyone assumes them, no one specifies them, and they surface as production incidents. Treat them as first-class discovery output. Identify the **architecturally significant requirements** (the quality demands that materially shape the architecture) for each initiative. Quantify them ("p99 latency under 200 ms at 10× current load"; "WCAG (Web Content Accessibility Guidelines) 2.2 AA"; "recovery time objective of 15 minutes"). And where you can, encode them as automated **fitness functions** (executable checks that continuously verify a quality attribute) that the delivery pipeline can check. This is the discovery-side complement to chapter 3.1 (architecture fundamentals) and chapter 3.5 (scalability, performance, resilience).

### Make every goal SMART

Whether writing a key result, an acceptance criterion, or a quality target, apply the **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)** test:

- **Specific:** names one clear, unambiguous outcome.
- **Measurable:** has a metric and a source of truth.
- **Achievable:** is realistic given constraints and evidence.
- **Relevant:** ladders up to a higher objective and to user value.
- **Time-bound:** has a deadline or review date.

"Improve performance" fails every letter. "Reduce median checkout time from 8s to 3s for mobile users by end of Q3, measured by real-user monitoring" passes all five. SMART criteria convert vague ambition into a falsifiable claim that discovery can test and delivery can verify.

### Run continuous, evidence-driven discovery

Structure discovery as a repeatable pipeline, not a one-off phase:

1. **Sense.** Gather signals: user research, support data, analytics, market and compliance inputs.
2. **Frame.** Map opportunities (an *opportunity-solution tree* connects a desired outcome to the user needs and candidate solutions that could move it).
3. **Hypothesize.** State assumptions as falsifiable claims: "We believe [change] will cause [outcome] for [segment], and we'll know if [measure] moves."
4. **Experiment.** Validate the riskiest assumptions with the cheapest test: interviews, prototypes, fake-door tests (advertising a not-yet-built feature to measure real demand), [A/B experiments](https://en.wikipedia.org/wiki/A/B_testing) (randomized comparisons of two variants, chapter 7.4).
5. **Decide.** Persevere, pivot, or drop, and feed the survivors into the delivery backlog with their SMART success criteria attached.

The output of the discovery pipeline is not a feature list; it is a stream of *validated, measurable bets* ready for delivery.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Outcome-based goals (OKRs)** | Aligns teams to impact; empowers autonomy in *how* | Hard to write well; tempting to backfill with tasks; noisy attribution |
| **Output/feature roadmaps** | Predictable, easy to communicate and contract | Rewards shipping over impact; hides wrong-thing risk |
| **Heavy up-front discovery** | Reduces build waste; strong requirements | Slows start; risks analysis paralysis; assumptions still untested |
| **Continuous dual-track discovery** | De-risks continuously; fast feedback | Requires research capacity and discipline; harder to schedule |
| **Explicit quality attributes as SMART targets** | Prevents "-ility" surprises; auditable | Effort to quantify; can over-constrain early exploration |

The central tension is **commitment vs. learning**. Enterprises, and especially governments, often need firm commitments for budgeting and contracts, which pulls toward output roadmaps. Good outcomes need room to learn, which pulls toward OKRs and experiments. Resolve it this way: commit to *problems and outcomes* firmly, and hold *solutions* loosely.

## Questions to discuss with your team

1. **Who on your team actually owns discovery, and do they have the capacity to run it continuously rather than in a one-off sprint?** Dual-track development works only when someone holds the discovery track open every week rather than only at the start of a quarter. In a large org, discovery often has no dedicated owner, so it collapses into whoever has spare time, which is no one, and the team defaults to building. Bring evidence: count how many of your last ten features went through a documented hypothesis and a cheap test before build, versus straight into the backlog. In enterprise and government settings, where one misaligned initiative can waste multiple team-quarters, name a product owner or a trio (product, design, engineering) accountable for the sense-frame-hypothesize-experiment-decide loop. If no one owns it, staff it before you argue about anything else.

2. **Which of your current initiatives have architecturally significant requirements that you have never quantified, and could you encode any as fitness functions?** The "-ilities" (reliability, performance, security, accessibility) get assumed and then surface as production incidents. Walk through each active initiative, ask which quality attributes materially shape the architecture, and check whether each has a number and a source of truth: "p99 under 200 ms at 10x load," "WCAG 2.2 AA," "recovery time objective of 15 minutes." For enterprise and government, unquantified accessibility or security requirements create direct legal and audit exposure. The signal to bring is your last three incidents: how many traced back to a quality attribute nobody specified? Where you can turn a target into an automated fitness function the delivery pipeline checks, do it, because a specified but unenforced target drifts.

3. **When you last committed to a solution, did you test the riskiest assumption first, or the easiest one?** Teams reliably validate the assumption they are most comfortable with and skip the one that would actually kill the idea. For each initiative, list its assumptions (desirability, viability, feasibility) and rank them by "how dead is this idea if we are wrong here," then aim the cheapest test at the top of that list. This matters at scale because a confident, senior team can commit a quarter of engineering to an untested belief, and the cost stays invisible until launch. Bring the artifact: your last hypothesis stated as "We believe [change] causes [outcome] for [segment], measured by [metric]," and ask whether you tested it or just built it. If you cannot name the riskiest assumption, you are not ready to commit build capacity.

4. **How many of your key results are genuine outcomes, and how many are tasks or ship dates wearing outcome clothing?** The single most common failure in outcome-based planning is backfilling key results with the work you already planned to do ("launch the new wizard") instead of the change that work is supposed to cause ("raise 7-day activation from 40% to 60%"). At scale this quietly defeats the whole point: dozens of teams report green while no business metric moves, because everyone graded themselves on shipping. The competing pull is real, output roadmaps are easier to communicate, contract, and forecast, which is exactly why they creep back in. Bring your current OKR set and mark each key result as outcome or output, then check whether OKR grading is entangled with compensation, since results tied to pay get sandbagged fast. For enterprise and government portfolios, where funding is committed against stated goals, a roadmap of outputs with no outcome measure is an audit finding waiting to happen; insist that each initiative commit to a problem and a measurable outcome firmly while holding the solution loosely.

5. **Which of your KPIs would keep climbing even if the product were getting worse, and what guardrails protect the metrics you are actively trying to move?** Every metric you elevate to a target invites [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law): once a measure becomes the goal, people optimize the measure rather than the thing it was meant to represent. Vanity metrics (raw page views, cumulative registered users) rise reliably and predict nothing, while a single key result chased without guardrails can be met by degrading something you never named. The tension is that leading indicators let you steer early but are noisy and gameable, whereas lagging indicators are trustworthy but confirm too late to act. Bring your metric inventory classified as leading or lagging and as target or guardrail, and stress-test each target by asking "how could a clever team hit this number while making the product worse." In regulated and public settings, publish the guardrails alongside the targets, because an oversight body that sees only the headline metric cannot tell genuine public value from a gamed number.

6. **When delivery ships something, how does the real-world outcome actually re-enter discovery, or does the loop stay open?** Dual-track development only compounds if delivered outcomes flow back as evidence for the next round; when the loop stays open, teams ship, celebrate, and never learn whether the bet paid off, so the same untested assumptions recur. In a large organization the feedback path is where responsibility is most likely to fall through a gap: delivery owns the release, analytics owns the dashboard, and no one owns comparing the promised key result to the observed one. Bring your last ten shipped initiatives and ask, for each, whether anyone checked the outcome metric against the original SMART target and whether that check changed a subsequent decision. For enterprise and government programmes committing multi-year funding, name the cadence and the owner for retiring or re-scoping features that failed to move their metric, because a shipped feature nobody revisits becomes permanent cost with no accountable review.

## Sector lens

**Startup.** With a tiny team and little runway, your discovery pipeline is deliberately lightweight but never skipped: a day of customer interviews and a fake-door test cost almost nothing against the weeks a wrong build burns. Pick one leading indicator that stands in for your core value, state each bet as a single falsifiable hypothesis, and kill ideas before you write code rather than after. Formal OKRs are overkill at five people; one honest measurable outcome per cycle is enough to keep speed from becoming motion without progress.

**Small business.** You likely have no dedicated researcher or product analyst, so treat discovery as a habit, not a role: a few structured conversations with real customers and a simple metric you already collect. The build-versus-buy question dominates, because most quality attributes (reliability, security, accessibility) are cheaper to get from a reputable vendor than to specify and enforce yourself. Write one or two SMART targets so you can tell whether a purchased tool or a small build actually moved the outcome, and avoid committing scarce budget to features no one validated wants.

**Enterprise.** Scale turns discovery into a coordination problem across dozens of teams: without a shared OKR cadence and a common definition of "outcome," local goals drift and duplicate, and misaligned bets compound into wasted portfolios. Standardize how architecturally significant requirements are quantified and encode them as fitness functions so quality attributes are governed, not assumed. Manage discovery as a portfolio with explicit kill criteria and a loop that feeds delivered outcome metrics back to the next cycle, so leadership steers on impact rather than on a backlog of features.

**Government.** Procurement and multi-year funding demand firm commitments, which pull hard toward output contracts, yet public value lives in outcomes: citizens served, wait times cut, burden reduced. Frame programmes around measurable public outcomes and non-negotiable quality attributes (WCAG accessibility, plain language, security), and make discovery evidence, including usability testing with assistive-technology users, part of the record oversight bodies can audit. Define success as taxpayer or citizen outcomes rather than delivered modules, so "we built what the contract said" can never substitute for a result that never materialized.

## Examples

**Startup.** A four-person seed-stage team building a scheduling app for hair salons is tempted to build an online-booking widget because a few loud users asked for it. Instead they run a week of discovery: five owner interviews, a fake-door "Book online" button on the marketing site, and a single leading indicator (percentage of appointments that end in a no-show). The interviews and click data reveal that no-shows, not booking, are the real pain, so they write one SMART key result (cut no-shows from 22% to under 10% for pilot salons this quarter) and ship a small deposit-and-reminder feature first, killing the booking widget before writing a line of it.

**Enterprise.** A retail bank's payments group replaces a feature-count roadmap with three quarterly OKRs, one being "Make everyday payments feel instant" with key results for p95 transfer confirmation time, first-attempt success rate, and payment-related support contacts. System quality attributes are specified up front (99.99% availability, sub-second confirmation, PCI-DSS (Payment Card Industry Data Security Standard) scope minimized) and wired into delivery as fitness functions. Discovery runs weekly customer interviews and fake-door tests before committing engineering. Two candidate features are killed in discovery for failing to move the leading indicators (saving an estimated two quarters of build effort), while a smaller, unglamorous latency fix moves the key result most.

**Government.** A national tax agency modernizing online filing sets a programme objective of "Reduce the burden of filing for ordinary taxpayers," with SMART key results: cut median time-to-file from 45 to 20 minutes, raise successful self-service completion from 60% to 85%, and meet WCAG 2.2 AA and plain-language standards as non-negotiable quality attributes. KPIs (uptime during filing season, call-centre volume) are monitored as guardrails. Discovery uses moderated usability testing with real taxpayers, including assistive-technology users, before each release. Because success is defined as taxpayer outcomes rather than delivered modules, the programme can show oversight bodies measurable public value, not just spend.

## Business case: motivations, ROI, and TCO

The return on a discovery pipeline is dominated by **avoided waste**. Industry experience, echoed in controlled-experiment programmes at large tech firms, repeatedly finds that a large share of built features, often cited around half or more, produce no measurable improvement or actively harm the target metric. Suppose even a quarter of a team's build capacity goes to ideas that discovery would have killed cheaply. The pipeline then pays for itself many times over: a week of user research and a fake-door test costs almost nothing against a quarter of engineering, plus the ongoing maintenance burden of an unused feature.

The **[total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO) framing matters because unvalidated features are not free after launch. Every shipped feature carries perpetual costs: maintenance, testing, security surface, support, and cognitive load (chapter 10.4). Killing a bad idea in discovery avoids not just the build cost but the entire tail of ownership. Explicit quality attributes follow the same logic: specifying reliability and accessibility as SMART targets up front is far cheaper than retrofitting them after an outage, breach, or lawsuit.

To make the case to leadership, shift the conversation from "how much are we shipping" to "how much are we moving the metrics that matter," and show a few concrete examples of expensive features that moved nothing. The adoption cost is modest (research capacity, an OKR cadence, and the discipline to write SMART criteria), and the primary risk of *not* adopting is silent, uncounted, and compounding.

## Anti-patterns and pitfalls

- **Roadmaps of features masquerading as strategy:** output lists with no stated outcome or measure.
- **Key results that are tasks:** "launch X" instead of "improve Y by Z."
- **OKR theatre:** goals written, filed, and never reviewed or graded.
- **Sandbagged or heroic OKRs:** targets set to guarantee 100% (nothing learned) or fantasy stretch with no plan.
- **Unspecified quality attributes:** reliability, security, and accessibility assumed rather than quantified, then discovered in production.
- **Vanity metrics:** measures that always go up and predict nothing.
- **Discovery as a one-time phase:** a "discovery sprint" up front, then no continued validation.
- **Building the solution before testing the assumption:** skipping the cheapest experiment because the team is confident.
- **Metric fixation and [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law):** once a measure becomes the target, it stops being a good measure; balance with guardrail KPIs.

## Maturity model

- **Level 1, Initiate:** Work is defined as features on a roadmap and success is "we shipped it." There are no explicit outcome measures or quality targets; discovery happens by accident, if at all, and decisions are driven by the loudest opinion.
- **Level 2, Develop:** OKRs and KPIs exist for some teams but not others; goals are stated yet often output-shaped; quality attributes are named but not quantified. A team may run a one-off "discovery sprint," then stop validating once build begins, so practice is real but inconsistent across the organization.
- **Level 3, Standardize:** A consistent OKR cadence aligned to strategy, SMART key results, and specified, testable quality attributes are documented and expected org-wide. Discovery is a recognized, staffed activity with hypotheses and experiments, and architecturally significant requirements are identified for each initiative rather than assumed.
- **Level 4, Manage:** The portfolio is measured against baselines. Leading and lagging indicators, discovery hit-rate, and the outcome each shipped bet actually moved are tracked against its SMART target; hypotheses are graded on evidence and kill criteria are enforced; fitness functions report quality-attribute conformance continuously, so drift from a specified reliability, performance, or accessibility target is caught with data rather than in an incident.
- **Level 5, Orchestrate:** Continuous dual-track discovery is integrated with portfolio, risk, and budgeting; validated bets flow steadily to delivery and outcome metrics loop back automatically to steer the next round. Leading indicators steer investment, and the organization routinely retires, re-scopes, and rebalances initiatives on evidence, adapting the pipeline itself as the market and the metrics shift.

## Ideas for discussion

1. Look at your current roadmap: how many items state a measurable outcome versus just a feature to ship?
2. Which of your team's key results are actually disguised tasks, and how would you rewrite them?
3. What system quality attributes does your product depend on that have never been explicitly quantified?
4. What is the cheapest experiment that could have killed your last failed feature before you built it?
5. How do you resolve the tension between the firm commitments budgeting/procurement demands and the learning good outcomes require?
6. Which of your KPIs would keep rising even if the product were getting worse?

## Key takeaways

- The discovery pipeline decides *what* and *why*, and defines success **before** delivery commits resources.
- Use **OKRs** for the change you want, **KPIs** for the health you sustain, and classify metrics as leading or lagging.
- Treat **system quality attributes** as explicit, quantified, testable requirements, not assumptions.
- Make every goal, key result, and acceptance criterion **SMART**.
- Run discovery **continuously and in parallel** with delivery; validate the riskiest assumptions cheaply.
- The dominant ROI is **avoided waste**: both build cost and the perpetual TCO of unused features.
- Close the loop: delivered **outcome metrics** (chapter 11.2) are the primary evidence for the next round of discovery.

## References and further reading

- *Measure What Matters*, by John Doerr (on OKRs).
- *Radical Focus*, by Christina Wodtke (on OKRs in practice).
- *Continuous Discovery Habits*, by Teresa Torres (opportunity-solution trees, dual-track discovery).
- *Inspired* and *Empowered*, by Marty Cagan (product discovery and outcome teams).
- *Lean Analytics*, by Alistair Croll and Benjamin Yoskovitz (leading indicators, vanity metrics).
- *The Lean Startup*, by Eric Ries (build-measure-learn, validated learning).
- *Escaping the Build Trap*, by Melissa Perri (outcomes over outputs).
- *Outcomes Over Output*, by Joshua Seiden.
- *Software Architecture in Practice*, by Bass, Clements, Kazman (quality attributes).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): origin of SMART criteria.
