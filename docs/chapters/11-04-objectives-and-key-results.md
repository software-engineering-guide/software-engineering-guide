# 11.4 Objectives and key results (OKRs)

## Overview and motivation

Every large organization faces the same quiet failure: teams working hard, on time, on things that do not advance the strategy. [Objectives and Key Results](https://en.wikipedia.org/wiki/OKR) (OKRs) is the goal-setting framework built to prevent exactly that. It connects the strategy at the top of the house to the concrete, measurable outcomes each team commits to achieve in a defined period. It was developed at Intel by [Andrew Grove](https://en.wikipedia.org/wiki/Andrew_Grove) and popularized after John Doerr introduced it at Google. An OKR describes the change you are driving right now.

An OKR has two parts. An **objective** is a qualitative, inspirational statement of a desired end state, short and free of numbers, that a team can rally around. **Key results** are the few measurable outcomes that together prove the objective was reached. Direction plus proof: the objective says where you are going, and the key results say how you will know you arrived.

For large teams, the discipline the framework imposes is worth as much as the framework itself. In enterprises, dozens of teams pursue local goals that quietly diverge from strategy, and one shared set of company objectives can align hundreds of people on the same few bets. In government, multi-year programmes commit public funds against legislated mandates, and "we delivered the modules in the statement of work" is no defence if wait times or fraud never improved. OKRs force intent to be stated as outcomes the public can audit. This chapter is about writing them, running their cadence, grading them honestly, and protecting them from the distortions that turn a good idea into ceremony. Its companion, chapter 11.5, covers key performance indicators (KPIs), the metrics you track to sustain ongoing health, and the two chapters are meant to be read together.

## Key principles

- **Objectives inspire; key results measure.** Direction plus proof.
- **Key results are outcomes, not tasks.** Measure the change you cause, not the work you do.
- **OKRs for the change; KPIs for the health.** Set the boundary deliberately (chapter 11.5).
- **Fewer is better.** A few objectives, a few key results each. Focus is the mechanism.
- **Align, don't dictate.** Leadership sets direction; teams propose how they contribute.
- **Cadence over ceremony.** Set, review mid-cycle, grade honestly, repeat.
- **Grade for learning.** A low grade on a stretch goal is information, not a verdict on a person.
- **Keep OKRs out of pay and ratings.** Tie them to compensation and they get sandbagged and gamed ([Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)).

## Recommendations

### Write objectives that are qualitative and directional

An objective is a qualitative, inspirational statement of a desired end state in plain language, short and free of numbers. "Delight new customers in their first week" is an objective; "Increase activation by 20%" is a key result in disguise. Aim for three to five objectives per level. More than that is a to-do list wearing the costume of a strategy, and the whole point of the framework is to make you choose.

### Make every key result a measurable outcome, not an output

This is the most violated rule in the entire framework. Key results are the few measurable outcomes that together prove the objective was achieved. An **output** is what the team produces, such as a shipped feature; an **outcome** is the change it causes, such as higher retention. An output can be 100% done while the outcome stays flat. Write two to four key results per objective, each with a metric, a baseline (the current value, so change is meaningful), a target (the value you intend to reach), and a named source of truth (the authoritative system that computes it, drawn from your product analytics in chapter 7.4). A key result you can complete by working hard rather than by moving a number is a task, not a key result.

### Align by cascading down and proposing up

Alignment runs both ways. In **cascading (top-down)** alignment, leadership publishes a few company objectives and each layer derives objectives that ladder up to them. In **bottom-up proposal**, the teams closest to the work draft their own objectives and negotiate them upward. Do both, and aim for roughly half of your OKRs to originate bottom-up. The goal is alignment, not dictation: handing teams their numbers destroys the ownership that makes OKRs motivating in the first place. Done well, OKRs become the language a portfolio uses to express intended outcomes (chapter 10.1) and the discovery pipeline uses to frame what to build next (chapter 11.1).

### Run a disciplined cadence: set, review, grade

Run OKRs on a rhythm, most commonly **quarterly** for teams inside an **annual** company frame. **Setting** drafts, negotiates, and publishes, so every team can see every other team's OKRs. **Mid-cycle review** combines lightweight weekly check-ins with a formal mid-point, tracking each team's confidence and surfacing blockers while there is still time to act. A key result trending red mid-cycle should trigger a governance decision (chapter 1.5), not an end-of-quarter surprise. **Grading** scores each key result honestly on a 0.0 to 1.0 scale, where the score is roughly the fraction of the target achieved. A short retrospective then decides whether the objective continues, changes, or retires.

### Distinguish aspirational from committed OKRs

Separate two kinds, because they grade differently and mixing them causes real damage. A **committed OKR** is a promise: the team expects 1.0, and missing it signals a genuine problem. Use these for must-hit obligations like a compliance or contractual deadline. An **aspirational (or stretch) OKR** is a deliberately ambitious target where reaching 0.6 to 0.7 is success. Graded at a consistent 1.0, it was set too low; graded at 0.2, it was fantasy with no plan behind it. Label each OKR by type so nobody mistakes an ambitious 0.6 for a failed one, and so a team pushing hard on a stretch goal is celebrated rather than punished.

### Keep OKRs out of performance reviews and compensation

OKRs are for direction and learning, not a bonus formula. The moment a key result determines someone's rating or pay, two things happen. People **sandbag**, setting targets they know they can beat, which kills ambition outright. And people **game** the metric, optimizing the number while the underlying goal quietly decays. This is Goodhart's law: when a measure becomes a target, it stops being a good measure. Grade OKRs for learning, and evaluate people through the separate mechanisms of roles, ladders, and growth in chapter 1.3. The two conversations can inform each other, but they must never be the same conversation.

### Set the boundary with KPIs deliberately

A KPI measures ongoing health you sustain regardless of what you are changing this quarter: availability, conversion rate, cost per transaction. A key result expresses a target movement in a metric over a bounded time. The useful test: keep tracking the metric after the objective is met and it is a KPI; retire it with the objective and it was a key result. A metric can play both roles, becoming a key result the quarter you push it and settling back into a guardrail once you do. In short, OKRs are the change you want; KPIs are the health you sustain. For north-star metrics, KPI trees, guardrails against gaming, SLIs and SLOs, DORA metrics, vanity metrics, and public performance reporting, see chapter 11.5, which treats all of them in depth.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| **Outcome key results** | Align effort to real impact; hard to game | Hard to write; slow, noisy; attribution is difficult |
| **Task or output key results** | Easy to write and track; clear ownership | Reward activity over impact; weak link to value |
| **Cascading (top-down) alignment** | Fast, coherent, unambiguous | Kills ownership; teams disengage |
| **Bottom-up proposal** | High ownership; surfaces frontline insight | Risks drift from strategy without a strong top frame |
| **Aspirational/stretch OKRs** | Drive ambition and breakthrough thinking | Demotivating if mistaken for commitments or tied to pay |
| **Committed OKRs** | Reliable for must-hit obligations | Encourage sandbagging if overused |

Two tensions govern this chapter. The first is **ambition versus safety**: stretch goals create breakthroughs, but only in a culture where a 0.6 is celebrated rather than punished, which is precisely why coupling OKRs to compensation is corrosive. The second is **alignment versus ownership**: numbers handed straight down are coherent but dead on arrival, while pure bottom-up drifts from strategy. Resolve both the same way. Label every OKR by type, grade for learning, keep performance ratings in a separate mechanism entirely, and run alignment in both directions so leadership sets the frame and teams fill it with goals they actually believe in.

## Questions to discuss with your team

1. **Are your key results outcomes, or are they tasks in disguise?** Walk your current list and ask, for each one, whether you could hit it by simply working hard rather than by moving a number. If "launch the new onboarding flow" is a key result, you have written a task, because you can ship it in full while retention stays flat. The outcome version is "raise 7-day activation from 25% to 45%," which no amount of effort guarantees. This matters most for large teams, where output-shaped goals let everyone report green while the strategy stalls. Bring the list, mark each key result as outcome or task, and rewrite the tasks as the change you actually want to cause.

2. **When a key result trends red at mid-cycle, does anyone have the authority to reallocate, or do you wait for the quarter to end?** The mid-cycle review exists so a failing bet triggers a decision while there is still time to act, not a post-mortem. In many organizations the check-in is theatre: confidence gets logged, nothing moves, and the miss surfaces only at grading. Bring the record of your last few mid-cycle reviews and ask what concretely changed as a result, whether people moved, scope was cut, or a target was renegotiated. For enterprise and government portfolios, where OKRs are the language leadership uses to steer spend (chapter 10.1), a red key result should be able to pull teams onto the problem. If your review cannot move resources, you are running OKR theatre with extra steps.

3. **Do your OKRs ever surface in performance or pay conversations, and what has that done to how ambitiously people set targets?** The instant a key result feeds a rating or a bonus, the framework inverts: people set targets low enough to guarantee a 1.0 and optimize the number rather than the goal. Ask honestly whether managers reference OKR grades when writing reviews, because even an informal habit teaches teams to sandbag. Compare the ambition of goals set by teams who believe grading is safe with those who suspect it is not. Bring examples of targets that look suspiciously beatable, and trace whether the caution comes from the work or from the incentive. Keeping grading separate from the evaluation mechanisms in chapter 1.3 is what lets people reach.

4. **How many objectives and key results does each team actually carry, and is that a focus or a backlog?** Focus is the mechanism that makes OKRs work, so count what you have: if a team holds a dozen objectives, it has a to-do list wearing the costume of a strategy, and everything is priority number one, which means nothing is. The competing pull is real, because every stakeholder wants their initiative named as a company goal, and saying no to a powerful sponsor is harder than adding one more line. Bring the raw counts per team, the list of what got explicitly dropped this cycle to make room, and an honest read on whether anyone can recite the objectives from memory. For a large enterprise or agency, the discipline scales badly by accident: a modest per-team count multiplied across hundreds of teams becomes an unreadable portfolio, so the constraint has to be set and enforced at the top, not left to each team to police alone.

5. **Is every OKR labelled committed or aspirational, and would your culture celebrate a 0.6 on a stretch goal or quietly punish it?** These two types grade on opposite scales, so mixing them unlabelled means a healthy 0.6 on an ambitious goal reads as a failure while a sandbagged 1.0 reads as a triumph, which is exactly backwards. The tension is between ambition and safety: stretch goals produce breakthroughs only where a miss is treated as information, yet the same low grade can be weaponized in a blame culture. Bring last cycle's grades sorted by type, and look at what happened to the people who landed a 0.5 on a real stretch: were they debriefed or sidelined. For enterprise and government portfolios, committed key results often carry statutory or contractual weight where 1.0 is the only acceptable outcome, so the label is not cosmetic; it tells leadership which misses are learning and which are genuine breaches of a promise the organization made.

6. **Which of the things you call OKRs are really KPIs, and are you tracking ongoing health as if it were a quarterly change?** The boundary matters because a metric you will keep watching long after this objective is met is a guardrail, not a key result, and dressing standing health up as a quarterly goal both crowds out real change and lets a team claim progress for simply keeping the lights on. The judgement call is genuine, since a metric can be a key result the quarter you push it and settle back into a KPI once you do (chapter 11.5). Bring your current list and apply the retire test to each line: if you would still track it next year regardless of strategy, move it to the health dashboard. In a large or public organization this cleanup is what keeps the OKR set honestly about the change you are driving, so oversight bodies can see intended outcomes rather than a restatement of the metrics you report every period anyway.

## Sector lens

**Startup.** With a handful of people and short runway, run one objective with two or three outcome key results and nothing more; the framework's job here is to stop a small team from chasing every shiny idea at once. Skip the heavy cadence and tooling, hold a five-minute weekly confidence check, and grade honestly at quarter end. Keep the whole thing away from equity and pay, and lean on an aspirational goal, because a founder-led team is exactly where a celebrated 0.6 pays off.

**Small business.** You have no dedicated OKR owner and no appetite for a consultant-driven rollout, so keep it to a shared page anyone can read, not a purchased platform. Write outcomes in customer terms, such as repeat-purchase rate or complaint volume, using numbers you already have rather than instrumenting new analytics you cannot staff. The main risk is drift, so tie the quarter's one or two objectives directly to the owner's plan and revisit them in the same meeting you already hold.

**Enterprise.** The hard part is coherence across many teams: a shared quarterly-within-annual cadence, published OKRs everyone can see, and a capped count per team so the portfolio stays readable. Run alignment both ways so leadership sets a few company objectives while teams propose bottom-up, wire mid-cycle reviews into governance (chapter 1.5) so a red key result can actually move resources, and keep grading firmly separate from the rating and pay mechanisms in chapter 1.3. Audit periodically for output-shaped key results and creeping OKR counts, the two failures that scale fastest.

**Government.** Public accountability reshapes the framework: objectives should name citizen outcomes, not delivered modules, so a legislature can audit whether wait times or error rates actually improved. Split committed key results that carry statutory or contractual weight, where 1.0 is required, from aspirational ones that push service quality further, and label them plainly for oversight bodies. Procurement and multi-year programme structures make bottom-up ownership harder to sustain, so invest deliberately in letting frontline teams propose targets, and publish the measures so the public can hold the agency to the outcomes it promised.

## Examples

**Startup.** A six-person productivity-app startup is celebrating a rising "total registered users" chart until a board member asks whether anyone actually keeps using the product. They replace the vanity chart with one aspirational quarterly OKR: the objective "New users feel the magic in week one," with key results for 7-day activation (from 25% to 45%) and week-4 cohort retention, each carrying a baseline, a target, and a source of truth in their analytics. They grade the OKR at 0.6 as an honest success for a stretch goal, run a short retrospective to decide what carries into next quarter, and keep the whole thing well away from anyone's equity or pay. They lean on a KPI guardrail (support tickets per active user) so they cannot juice activation with a pushy flow, and they leave the details of that guardrail to their KPI practice in chapter 11.5.

**Enterprise.** A global logistics company runs OKRs quarterly under annual company objectives. One company objective is "Become the carrier customers trust for time-critical shipments." A regional operations team proposes, bottom-up, "Make same-day delivery dependable in our metros," with aspirational key results: raise on-time same-day delivery from 82% to 95%, halve complaints per thousand shipments, and hold cost per parcel flat. Each key result has a named owner, a baseline, and a target. At mid-quarter the on-time key result trends to 0.4, triggering a governance decision (chapter 1.5) to reallocate two teams onto the failing hub. At quarter end the objective grades 0.6, a success for a stretch goal, and the learning reshapes next quarter's portfolio (chapter 10.1). No one's bonus moved because of the 0.6. The ongoing health metrics that sit beside these OKRs, such as delivery-network SLOs and flow metrics, live on the KPI dashboards described in chapter 11.5.

**Government.** A state unemployment-insurance agency modernizing its claims system sets an annual objective: "Help eligible residents receive benefits quickly and correctly." Committed key results carry statutory weight: pay 90% of valid first claims within 21 days, up from 63%, and hold the improper-payment rate below the federal threshold. Aspirational key results push further: raise self-service filing from 55% to 80% and cut the median call-centre wait from 40 to 10 minutes. Because success is defined as claimant outcomes rather than delivered modules, the agency can show its legislature measurable public value. OKRs are graded quarterly for learning, entirely separate from civil-service ratings, so frontline managers set honest targets. The published performance measures the agency reports to oversight bodies, and the definitional rigour those measures demand, are covered in chapter 11.5.

## Business case: motivations, ROI, and TCO

The return on OKRs comes from focus and alignment, which together avoid the single largest hidden cost in a large organization: many capable teams working hard, on time, on things that do not advance the strategy. When intended outcomes are explicit and visible across teams, duplicated effort surfaces, contradictory goals get reconciled before they collide, and low-value work loses its cover. A large organization's most expensive resource is the aligned attention of its people, and the dominant return here is redirected capacity.

The [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) is modest but real. The cadence consumes management time, and writing good outcome-based key results takes a few cycles to learn, because teams reflexively reach for output-shaped goals they know how to hit. Budget for that learning curve rather than abandoning the framework when the first quarter feels awkward. Two failure modes destroy the return outright. The first is **OKR theatre**: goals written at quarter start, filed, and never reviewed or graded, which pays the full ceremony cost for none of the benefit. The second is coupling OKRs to compensation, whose sandbagged and gamed metrics erode the very outcomes the framework was meant to improve. Keep the cadence light, the counts low, and the grading honest, and OKRs repay their overhead many times over.

## Anti-patterns and pitfalls

- **Key results that are tasks:** "launch the app" instead of "raise mobile retention to X%." The most common failure by far.
- **Too many OKRs:** a dozen objectives per team is a backlog, not a focus, and it defeats the whole purpose.
- **OKR theatre:** set once at quarter start, never reviewed at mid-cycle, never graded at the end.
- **Cascade-only alignment:** numbers handed down with no bottom-up proposal, which kills the ownership that makes goals motivating.
- **Sandbagging:** targets set deliberately low to guarantee a 1.0, hiding a lack of ambition behind a perfect score.
- **Stretch goals mistaken for commitments:** a healthy 0.6 on an aspirational goal treated as a failure, until teams stop reaching.
- **OKRs tied to pay or ratings:** the direct cause of sandbagging and gaming, and a textbook trigger for Goodhart's law.
- **Grading dishonestly:** inflating scores throws away the framework's only real output, which is the truth about what worked.

## Maturity model

- **Level 1, Initiate:** Goals are ad hoc or feature lists, and success means "we shipped it." Targets are round numbers chosen because they sounded ambitious. There is no cadence, no grading, and no shared visibility across teams, and any goal-setting is reactive to whatever is loudest this week.
- **Level 2, Develop:** Some teams run OKRs and a basic practice is taking shape, but key results are often disguised tasks, the cadence is inconsistent from team to team, and OKRs leak into performance reviews. Grading, where it happens at all, is optimistic. Sandbagging and gaming appear but go unrecognized, and each team improvises its own format.
- **Level 3, Standardize:** A quarterly-within-annual cadence is documented and enforced across the organization. Key results are outcome-based with baselines and targets, OKRs align both top-down and bottom-up, committed and aspirational OKRs are labelled, per-team counts are capped, and grading is honest and kept separate from compensation. Everyone writes to the same standard and can read every other team's OKRs.
- **Level 4, Manage:** The OKR practice is measured against baselines rather than run on faith. You track the share of key results that are true outcomes versus tasks, the fraction of OKRs originating bottom-up, average committed and aspirational grades, mid-cycle confidence trends, and how often a red key result actually moved resources. These measures are reviewed each cycle against prior quarters, so drift towards output-shaped goals, grade inflation, or sandbagging is caught with data and corrected, not just felt.
- **Level 5, Orchestrate:** OKRs are the portfolio's shared language (chapter 10.1), mid-cycle reviews drive real reallocation (chapter 1.5), and outcome data from delivery and analytics (chapter 7.4) loops continuously into the next cycle. The cadence, counts, and grading norms adapt as the organization learns, the culture rewards stretch goals and treats low grades as learning, and the boundary with KPIs (chapter 11.5) is held cleanly across every level of the org.

## Ideas for discussion

1. Of your current key results, how many describe an outcome, and how many are tasks you could complete by simply working hard?
2. What fraction of your OKRs originated bottom-up versus handed down, and what does that imply for how much ownership teams feel?
3. Are your OKRs ever consulted in performance or pay conversations, and what has that done to how ambitiously people set targets?
4. Which of your objectives are genuine stretch goals, and would your culture celebrate or punish a 0.6 on them?
5. When a key result went red mid-cycle last quarter, what actually changed, and who had the authority to change it?
6. Which metrics you currently call OKRs are really KPIs that belong in your ongoing health tracking (chapter 11.5)?

## Key takeaways

- An **objective** is a qualitative, inspirational end state; **key results** are the few measurable outcomes that prove it was reached, and they must be **outcomes, not tasks**.
- Give every key result a **metric, baseline, target, and source of truth**, and keep the counts small: a few objectives, a few key results each.
- Align **both ways**: leadership sets direction top-down, teams propose bottom-up. Alignment, not dictation.
- Run a **cadence** (quarterly within an annual frame) with mid-cycle review and **honest grading** on a 0.0 to 1.0 scale; label **committed** OKRs (aim for 1.0) versus **aspirational** OKRs (0.6 to 0.7 is success).
- Keep OKRs **out of performance reviews and compensation** to prevent sandbagging and gaming (Goodhart's law); evaluate people through the mechanisms of chapter 1.3.
- **OKRs are the change you want; KPIs are the health you sustain.** For KPIs, north-star metrics, guardrails, SLIs and SLOs, and public performance reporting, see chapter 11.5.

## References and further reading

- *Measure What Matters*, by John Doerr (the canonical modern account of OKRs, from Intel to Google).
- *High Output Management*, by Andrew Grove (the origin of the objectives-and-key-results approach).
- *Radical Focus*, by Christina Wodtke (OKRs in practice for smaller teams, with a focus on cadence discipline).
- *Objectives and Key Results*, by Paul Niven and Ben Lamorte (implementation guidance for larger organizations).
- Google re:Work, "Set goals with OKRs" (Google's published guidance on OKR practice).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): the SMART criteria for writing measurable key results.
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law, on why an OKR tied to pay stops measuring what you meant.
