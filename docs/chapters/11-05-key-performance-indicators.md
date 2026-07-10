# 11.5 Key performance indicators (KPIs)

## Overview and motivation

A **[key performance indicator](https://en.wikipedia.org/wiki/Performance_indicator) (KPI)** is a metric your organization deliberately chooses to track because it reflects the ongoing health of something that matters. The word *key* carries the weight here: a KPI is not any number you can collect, but the small set you have decided are worth steering by. Where an objective and key result (OKR) describes a change you are driving right now, a KPI describes the steady state you are protecting. This is the cleanest way to hold the two apart: OKRs are the change you want; KPIs are the health you sustain. Chapter 11.4 is the companion chapter on OKRs, their cadence, and their grading; this chapter is about choosing KPIs, defining them, and protecting them from distortion.

For large teams, the discipline a good KPI imposes is worth as much as the metric itself. In enterprises, dozens of teams pursue local numbers that quietly diverge from strategy, and one well-chosen KPI can align hundreds of people on the value customers actually receive. In government, multi-year programs commit public funds against legislated mandates, and "we delivered the modules in the statement of work" is no defense if wait times or fraud never improved. A badly chosen KPI corrupts quietly: a call center measured on *calls closed per hour* will close calls, not solve problems.

This chapter is about getting those choices, and the guardrails around them, right. Chapter 11.1 introduces KPIs briefly as part of the discovery pipeline; here you get the depth. The stakes are high because a KPI is an instruction disguised as a measurement. People optimize what you count, so what you count had better be what you want.

## Key principles

- **Key, not many.** A KPI is one of the few metrics you have chosen to steer by, not everything you can collect.
- **Measurable, actionable, and owned.** Every KPI has one precise definition, a source of truth, an owner, and a lever that moves it.
- **Health, not change.** KPIs track the steady state you protect; OKRs (chapter 11.4) drive the change you want.
- **Lead where you can, confirm where you must.** Prefer leading indicators; use lagging ones to verify.
- **Weight toward outcomes.** Inputs and outputs are easy to count; the value lives in outcomes.
- **Assume every metric will be gamed.** Design against [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) with ratios, cohorts, and paired guardrails.
- **Reject vanity.** If no reading would change a decision, the metric is decoration.
- **Visualize honestly.** A dashboard should inform in seconds without misleading.

## Recommendations

### Define what makes a KPI "good"

A good KPI passes four tests. It is **aligned**: it traces to a stated goal, so moving it means something. It is **measurable**: one precise definition, a named **source of truth** (the authoritative system of record), a unit, and a collection method, so two people computing it separately arrive at the same number. It is **actionable**: the owning team has levers that actually move it. It is **owned**: one accountable person or team owns its trend, its definition, and its data quality. A metric that fails any of the four tests is a candidate for deletion, not a candidate for a dashboard. Most metric clutter in large organizations is numbers that fail at least two of these and were never retired.

### Classify metrics by timing and by chain of value

Two lenses keep a KPI set balanced. The first is timing. A **leading indicator** is predictive and movable now (trial sign-ups, onboarding completion); a **lagging indicator** is confirmatory and slow (annual revenue, churn). Leading indicators let you steer before the lagging ones deliver a verdict you can no longer change. The second lens is the chain of value. An **input metric** measures effort spent (hours worked, dollars deployed); an **output metric** measures what the system produced (features shipped, tickets closed); an **outcome metric** measures the change you actually wanted (revenue retained, wait time reduced). Teams gravitate to inputs and outputs because they are easy to count and fully within their control, but the value lives in outcomes. Weight your set toward outcomes, and treat a dashboard that is all outputs as a warning sign.

### Design metrics that resist gaming

Assume Goodhart's law: when a measure becomes a target, it stops being a good measure. Design against it from the start rather than reacting after the distortion appears.

- **Prefer ratios and rates over raw counts.** "Tickets closed" rewards volume; "percentage resolved on first contact" rewards resolution. A raw count is gameable by doing more of something worthless.
- **Use cohorts.** A **cohort** is a group defined by a shared starting point (all users who signed up in March). Reporting by cohort stops a declining trend from hiding inside a flattering aggregate that a strong recent month props up.
- **Pair every incentivized KPI with a guardrail.** A **guardrail metric** is a paired counter-metric that must not degrade while you push the primary one: call handle time paired with customer satisfaction, activation paired with support load. The guardrail makes cheating visibly expensive.

### Reject vanity metrics; require actionability

A **vanity metric** reliably rises, looks impressive, and changes no decision: cumulative registered users, page views, lines of code. The tells are consistent. It only ever goes up. It is an absolute count rather than a rate. And it has no answer to the question "what would we do differently if this number doubled?" An **actionable metric**, by contrast, ties to a specific behavior you can influence and to a decision it would change. Before you adopt any KPI, ask what action a good reading and a bad reading would each trigger. If both readings lead to the same behavior, discard the metric. This test alone will shrink most proposed dashboards by half.

### Build a KPI tree under a single north-star metric

Do not track KPIs as a flat list. Arrange them as a **KPI tree** (or metric tree): a top metric broken into the metrics that mathematically or causally drive it, level by level, down to the operational measures that individual teams own. The tree tells you which lower metric to investigate when a top one moves, which turns "the number is down" into "this hub's dwell time is the cause." At the very top, name a single **north-star metric**: the measure that best captures the core value delivered to customers. For a marketplace it might be completed transactions; for a product, weekly active usage of the core feature. A north-star aligns effort and stops departments optimizing conflicting local numbers, but only if it measures value rather than vanity, and only if guardrails balance it. If your top metric could keep rising while customers got less value, it is vanity dressed as strategy.

### Set baselines, targets, and thresholds

A KPI without a reference point is just a number on a screen. Give every one three references. A **baseline** is the current or historical value, so that a change is meaningful rather than mysterious. A **target** is the value you intend to reach, with a date. **Thresholds** trigger action before a target is won or lost: a **warning threshold** prompts attention, and a **critical threshold** prompts intervention. Ground targets in evidence (a past trend, an external benchmark, or a capacity model) rather than round-number optimism, and write down the reasoning. Recorded reasoning is what lets a miss teach you something instead of merely disappointing you, because you can compare what happened against the assumption that set the target.

### Visualize honestly on dashboards

A KPI dashboard should let a reader grasp status and trend in seconds without being misled. Show trend over time, not a lone snapshot. Start value axes at zero unless you have a stated reason not to, because truncated axes exaggerate small changes into dramatic ones. Show variation and uncertainty rather than false precision. Annotate context so a reader can tell a real shift from noise: deploys, incidents, seasonality, policy changes. Avoid the chart tricks that flatter a number: dual axes that imply a correlation, cherry-picked date ranges, and 3-D effects that distort proportions. These practices connect directly to analytics and business intelligence (chapter 7.3) and to product analytics and experimentation (chapter 7.4), where the same honesty standards govern how you read what a metric is telling you.

### Adopt the operational KPI vocabularies

Operational health has well-established KPI vocabularies you should reuse rather than reinvent. From site reliability engineering (chapter 9.1): a **service level indicator (SLI)** is a measured signal of service health (latency, success rate); a **service level objective (SLO)** is the target range for an SLI (99.9% of requests succeed); and the **error budget** is the allowed shortfall (the 0.1% you may spend on risk before you stop shipping and stabilize). From the delivery pipeline (chapter 11.2): **flow metrics** track work through the system (flow time, [throughput](https://en.wikipedia.org/wiki/Throughput), [work in process](https://en.wikipedia.org/wiki/Work_in_process), flow efficiency), and the four metrics from the [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA) program pair speed with stability: deployment frequency, lead time for changes, change failure rate, and time to restore service. Both vocabularies set speed beside stability by design, so no team can post a great velocity number by quietly sacrificing reliability. These same operational KPIs feed engineering effectiveness and developer productivity work (chapter 1.10).

### Meet public-sector performance-reporting duties

Government adds a distinct requirement: KPIs are often **published performance measures** reported to legislatures, oversight bodies, and the public, sometimes under statute. Treat these with extra rigor. Hold the definition stable across reporting periods, so that a trend is genuinely comparable year to year. Document the methodology and the data source. Be honest about limitations. Because a published measure creates strong incentives, it is especially prone to Goodhart distortion: a target to reduce a waiting list gets met by redefining who counts as waiting. Pair each published measure with guardrails, and audit the definition itself, not just the number. The most important question about a public KPI is often not "did it improve?" but "does it still measure what it claimed to measure?"

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| **Outcome metrics** | Align effort to real impact; hard to game | Hard to define; slow, noisy; attribution is difficult |
| **Input/output metrics** | Easy to measure; clear ownership; fast feedback | Reward activity over impact; weak link to value |
| **Leading indicators** | Let you steer early | Predictive, so noisier and less certain |
| **Lagging indicators** | Authoritative confirmation | Arrive too late to change the result |
| **Few KPIs** | Focus, clarity, easy to communicate | May miss dimensions; blind spots |
| **Many KPIs** | Broad coverage; fewer surprises | Diluted attention; dashboard fatigue; conflicting signals |
| **Public performance reporting** | Accountability, transparency, trust | Strong gaming pressure; definitions become political |

The central tension is **focus versus coverage**, sharpened by **motivation versus distortion**. You want enough measures to see the whole picture, few enough that a team can actually act on them, and each one guarded so that the act of incentivizing it does not corrupt it. Resolve the tension by holding a small set of owned, outcome-weighted KPIs arranged in a tree under one north-star metric, and by pairing every incentivized measure with a guardrail. Coverage then comes from the tree's structure rather than from the sheer number of metrics on the screen.

## Questions to discuss with your team

1. **Do you have a single north-star metric, and does it measure delivered value or just activity?** A flat list of KPIs lets departments optimize conflicting local numbers, while a north-star aligns everyone on the value customers actually receive: completed transactions for a marketplace, activation for a product. Ask whether your top metric would keep rising if customers were getting *less* value, because if it can, it is vanity dressed as strategy. In a large organization the north-star is what stops one team's win from being another team's loss, so it has to sit atop a KPI tree of the operational measures teams control. Bring your current top-line metric and try to trace it down to what each team owns. If the tree does not connect, the north-star is decoration rather than a steering mechanism.

2. **For each incentivized KPI, what is the cheapest way to game it, and what guardrail would expose that cheating?** Every metric you attach a reward or a reputation to invites optimization of the number rather than the outcome, and the cheapest path is rarely the one you intended. Sit down and, for each KPI, deliberately design the exploit: how would a rational team make this number look good while doing less of what you actually want? Then name the counter-metric that would catch it (handle time paired with satisfaction, activation paired with support tickets, speed paired with error rate). This exercise matters most for the metrics you report upward or publish, because those carry the strongest incentives and therefore the strongest distortion pressure. If you cannot name a guardrail for a KPI, you are not ready to incentivize it yet.

3. **Are your targets grounded in evidence, and did you write down the reasoning behind each one?** A KPI without a baseline is just a number, and a target set to a round figure because it sounded ambitious cannot be interpreted when you miss it. For each KPI, check that it carries a baseline, a target with a date, warning and critical thresholds, and a recorded rationale drawn from a past trend, a benchmark, or a capacity model. This matters most for measures carrying statutory or contractual weight, where "pay 90% of valid claims within 21 days" needs to be defensible rather than aspirational guesswork. Bring your current targets and ask, for each one, "why this number and not one higher or lower?" If the answer is silence, the target was optimism, and a miss will teach you nothing.

## Examples

**Startup.** A six-person productivity-app startup is celebrating a rising "total registered users" chart until a board member asks whether anyone actually keeps using the product. They retire that vanity count and adopt 7-day activation as their north-star metric, cohorted by signup week so a strong launch cannot hide the churn underneath. They give it a baseline (25%), a target (45%), and warning and critical thresholds, and they pair it with a guardrail (support tickets per active user) so they cannot juice activation with a pushy onboarding flow. The whole company dashboard fits on one screen: the north-star, its two drivers, and the guardrail. When the KPI trends toward the warning threshold, they know from the tree which driver to investigate first.

**Enterprise.** A global logistics company adopts *on-time delivery rate* as its north-star metric and builds a KPI tree beneath it: pickup punctuality, hub dwell time, and last-mile success, each owned by a named regional lead with a baseline, a target, and warning and critical thresholds. Each speed KPI is paired with a guardrail, so on-time rate travels with damage rate and no region can hit its number by rushing parcels into breakage. Platform SLOs (99.95% tracking-API availability, chapter 9.1) and DORA metrics (chapter 11.2) sit on the engineering dashboard beside the business KPIs. When on-time rate dips toward its warning threshold in one region, the tree pinpoints that hub's dwell time as the cause, and the fix is targeted rather than a company-wide scramble. The metrics that the team decides to *move* this quarter become key results in that team's OKRs (chapter 11.4); the rest stay as standing guardrails.

**Government.** A state unemployment-insurance agency reports *median days from claim to first payment* as its published performance measure, cohorted by claim month so a good quarter cannot mask a worsening backlog, rather than the vanity count of "claims processed." It pairs that measure with guardrails (payment accuracy and appeal-overturn rate) so speed cannot be bought with errors. The definition of "median days" is frozen across years and documented publicly, and an independent audit checks the definition itself, confirming that claimants who are still waiting are not quietly reclassified out of the count. Frontline SLIs (portal uptime, call-answer rate) feed the operational dashboard beneath the published measures. Because success is defined as *claimant outcomes* rather than *delivered modules*, the agency can show its legislature measurable public value that survives scrutiny.

## Business case: motivations, ROI, and TCO

The return on a good KPI comes from **focus and alignment**, which avoid the largest hidden cost in large organizations: many teams working hard, on time, on things that do not advance strategy. When the small set of measures that matter is explicit and visible, duplicated effort surfaces, contradictory local goals get reconciled before they collide, and low-value work loses its cover. A large organization's most expensive resource is the aligned attention of its people, and the dominant return on KPIs is redirected capacity.

The cost of the *wrong* KPI is not the dashboard. It is quarters of effort optimizing a number while the real outcome erodes, plus the cost of unwinding the gamed behavior afterward. A call center that spent a year minimizing handle time while maximizing repeat contacts produced a negative return entirely through a single well-intentioned metric, and then had to rebuild both the process and the staff's trust.

The **[total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO)** of a KPI is modest but real and recurring. Each metric carries an ongoing cost: instrumentation and pipelines to collect it, dashboards to display it, review meetings to discuss it, and the mental load of one more thing to watch. That recurring cost is the strongest argument for a *small* set where every KPI earns its keep, because an unused metric still costs money to maintain. Keep the set small, the definitions precise, and the guardrails in place, and your KPIs repay their overhead many times over in avoided misdirection.

## Anti-patterns and pitfalls

- **Vanity metrics:** cumulative counts that only rise and change no decision.
- **Metric fixation:** behavior optimizes the number, not the outcome, because no guardrail exposes the gap.
- **Unowned or ill-defined KPIs:** no accountable person, or two teams computing "active user" differently and arguing instead of managing.
- **Output-only dashboards:** everything measured is what the team produced; nothing measures the change it caused.
- **A flat list with no tree:** dozens of gauges and no north-star, so a moving number gives no clue where to look.
- **Round-number targets with no rationale:** a goal chosen because it sounded bold, impossible to interpret when missed.
- **Dishonest charts:** truncated or dual axes, cherry-picked windows, and 3-D effects that manufacture a story.
- **Published measures gamed by redefinition:** a waiting-list target met by changing who counts as waiting.
- **Confusing KPIs with OKRs:** treating a standing health metric as a quarterly change goal, or vice versa (chapter 11.4).

## Maturity model

- **Level 1, Initial:** Metrics are mostly vanity counts with no baselines, targets, owners, or shared definitions. Dashboards show snapshots without trend, and no one can say which number matters most.
- **Level 2, Managed:** KPIs exist for some teams with baselines and targets, but they are mostly outputs, definitions vary between teams, and guardrails are absent. Gaming appears and goes unrecognized as gaming.
- **Level 3, Defined:** A coherent, owned KPI set has precise definitions and a named source of truth. Metrics are classified as leading or lagging and input, output, or outcome; incentivized measures are paired with guardrails; and charts follow honest-visualization standards.
- **Level 4, Optimizing:** A KPI tree ties frontline measures to a single north-star metric; outcome metrics dominate the set; operational SLIs, SLOs, and DORA and flow metrics integrate with business KPIs; definitions are audited and Goodhart effects actively monitored. The metrics that a team chooses to move feed cleanly into its OKRs (chapter 11.4).

## Ideas for discussion

1. Which of your KPIs would keep rising even if the product or service were getting worse?
2. For each incentivized KPI, what is the cheapest way to game it, and what guardrail would expose that cheating?
3. How many of your dashboard metrics are outcomes, and how many are inputs or outputs you count because they are easy?
4. Which of your metrics lack an owner or a single agreed definition, and what has that ambiguity cost you in arguments?
5. For a measure you report or publish, could the target be met by redefining the measure rather than improving the outcome?
6. If you had to cut your dashboard to five metrics, which would survive, and does a north-star sit at the top of that five?

## Key takeaways

- A **KPI** is a metric chosen because it reflects a goal you want to protect; a good one is **aligned, measurable, actionable, and owned**.
- **OKRs are the change you want; KPIs are the health you sustain.** For OKRs, cadence, and grading, see chapter 11.4.
- Classify metrics as **leading or lagging** and **input, output, or outcome**, and weight your set toward **outcomes**.
- Assume **Goodhart's law**: pair every incentivized KPI with a **guardrail**, and prefer **ratios and cohorts** over raw counts.
- Reject **vanity metrics**; organize KPIs into a **tree** under a single **north-star metric**; give each a **baseline, target, and thresholds**.
- Visualize **honestly** (chapters 7.3 and 7.4), and reuse operational vocabularies: **SLIs, SLOs, and error budgets** (chapter 9.1) and **DORA and flow metrics** (chapter 11.2).
- In government, treat **published measures** with extra definitional rigor and audit the definition, not just the number.

## References and further reading

- *Key Performance Indicators: Developing, Implementing, and Using Winning KPIs*, by David Parmenter (a practical framework for selecting and structuring KPIs).
- *Lean Analytics*, by Alistair Croll and Benjamin Yoskovitz (vanity versus actionable metrics, and the One Metric That Matters).
- *The Lean Startup*, by Eric Ries (actionable versus vanity metrics, and cohort analysis).
- *How to Measure Anything*, by Douglas W. Hubbard (defining and quantifying the seemingly unmeasurable).
- *The Visual Display of Quantitative Information*, by Edward R. Tufte (honest, high-integrity data graphics).
- *Site Reliability Engineering*, by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds. (SLIs, SLOs, and error budgets).
- *Accelerate*, by Nicole Forsgren, Jez Humble, and Gene Kim (the DORA delivery and stability metrics).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law; see also Marilyn Strathern's widely quoted formulation.
- U.S. Government Accountability Office (GAO) guidance on performance measurement and the GPRA Modernization Act: public-sector performance-reporting practice.
