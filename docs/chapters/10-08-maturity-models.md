# 10.8 Maturity models

## Overview and motivation

A [maturity model](https://en.wikipedia.org/wiki/Maturity_model) is a structured way to assess how capable and consistent your practice is in some domain, and to describe a path for improving it. It defines a small ladder of levels. At the bottom, work is ad hoc and reactive. At the top, it is measured, managed, and continuously optimizing. Each rung has observable characteristics you can check against.

Maturity models turn a vague question ("are we good at this?") into a repeatable answer ("we are at level 2 here, level 4 there, and this is what level 3 would require"). This book uses a five-level model in every chapter and consolidates them in chapter 12.4. This chapter is about the discipline itself: how the models work, when they help, and how they mislead.

The reason they matter is simple. Large organizations cannot improve what they cannot see. Across dozens of teams, capability varies enormously and invisibly. Some teams have excellent testing and weak security; others have the reverse. A maturity model gives you a shared vocabulary and a common yardstick, so gaps become comparable, investment can be prioritized, and progress can be tracked over time rather than merely asserted. Well-known examples include CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), for process), the DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) model (software delivery performance), OWASP SAMM (Software Assurance Maturity Model) and BSIMM (Building Security In Maturity Model) for software security, TMMi (Test Maturity Model integration, for testing), the Agile Fluency model, and data-management maturity models, plus countless internal scorecards.

For enterprise and especially government, maturity models carry particular weight. Government contracting has long used CMMI appraisal levels as a supplier qualification, and frameworks like the U.S. CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) tie cybersecurity maturity directly to eligibility for defence work. That gives maturity models real teeth. It also creates the central risk of this chapter: when a level becomes a gate or a target, people optimize for the appraisal rather than the underlying capability. Used well, maturity models are a mirror. Used badly, they are theatre.

## Key principles

- **Maturity is a means, not an end.** The goal is capability and outcomes, not a level number.
- **Assess to learn, not to score.** Honest self-assessment beats a flattering appraisal.
- **Higher is not always better.** The right target depends on risk, context, and cost.
- **Measure per domain, not one global grade.** Capability is uneven; a single number hides it.
- **Prioritize the lowest-maturity, highest-risk gaps first.**
- **Beware [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Once a level is a target, it stops measuring capability.
- **Re-assess periodically.** Maturity drifts as people, systems, and threats change.

## Recommendations

### Choose the right model for the domain

Match the model to the capability you want to improve, and prefer established, evidence-based models over invented ones where they exist:

- **Process and delivery:** CMMI (broad process maturity), the DORA capability model (delivery performance, grounded in research, chapter 11.2).
- **Security:** OWASP SAMM and BSIMM (software security practices), CMMC (defence cybersecurity).
- **Testing and quality:** TMMi.
- **Agile and ways of working:** the Agile Fluency model (chapter 10.7).
- **Data:** data-management maturity models (DMM, DCAM).

For internal use, a simple four- or five-level scale applied per capability (as this book does) is often more actionable than a heavyweight external framework. Reserve formal, appraised models for where they are contractually required.

### Assess honestly and per capability

Run assessments that produce truth, not comfort. Involve the people doing the work. Gather evidence rather than opinions. Score each capability separately, so the picture reflects reality: strong here, weak there. A self-assessment used to guide improvement is worth more than an external appraisal used to earn a badge, because the first rewards candour and the second rewards presentation. Chapter 12.4 provides a consolidated self-assessment across every domain in this book; use it as a starting instrument.

### Use maturity to prioritize, not to punish

The output of an assessment is a prioritized improvement backlog, not a report card for blame. Combine maturity with risk. A level-1 capability in a low-risk area may be fine. A level-2 capability in a safety- or compliance-critical area is urgent. Direct investment to the gaps where low maturity meets high risk, and connect the work to outcomes (chapter 11.1) so improvement is measured by results, not by climbing the ladder for its own sake.

### Set target levels deliberately: higher is not free

Each level up costs effort and often adds process weight. The right target is rarely "level 5 everywhere." It is the level where the extra capability still justifies the extra cost for that domain's risk. Regulated and safety-critical capabilities may genuinely need the top rungs, and audit often requires at least a "defined" level 3. Many others are well served at level 3 and would only accumulate bureaucracy by pushing further. Decide targets per capability, and stop climbing when the risk-adjusted return does.

### Guard against maturity theatre

The one failure mode that destroys the value of maturity models is optimizing for the score. Watch for assessments that grade generously, evidence assembled only for the appraisal, or "level 5" claims that production incidents contradict. Keep the assessment tied to observable behaviour and real outcomes. Rotate or externally sanity-check your assessors. Treat a suspiciously high self-score as a smell. The moment the level becomes the goal, the model stops telling you the truth.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Formal appraised models (CMMI, CMMC)** | Comparable, contractually recognized, rigorous | Costly; invites gaming; can ossify process |
| **Lightweight internal scorecards** | Fast, actionable, low overhead | Less comparable externally; easy to bias |
| **Evidence-based capability models (DORA)** | Tied to real outcomes; research-backed | Narrower scope; needs real metrics |
| **Single overall maturity grade** | Simple to communicate | Hides uneven capability; misleads |
| **Per-capability assessment** | Accurate, actionable prioritization | More effort; no single headline number |

The central tension is **assessment as mirror vs. assessment as target**. The same model that helps a team see itself clearly turns counterproductive the instant a level is tied to reward, eligibility, or status. The more a level matters, the more energy flows into the appearance of maturity rather than the substance.

## Questions to discuss with your team

1. **Should we keep a candid internal self-assessment separate from any contractually appraised level, and who owns each?** When a CMMC or CMMI level gates revenue, the appraisal and the truth drift apart, because energy flows toward passing rather than improving. For a large enterprise or a government supplier, that gap is where risk hides: you pass the audit and stay exposed. Run two books on purpose. Keep the formal appraisal for eligibility, and keep a blunt internal scorecard that no one is rewarded for inflating. Name an owner for each, and treat any distance between them as a signal to investigate, not to paper over. Bring recent incidents, near misses, and post-appraisal decay to the meeting as evidence of which book is telling the truth.

2. **For each domain, are we adopting an established evidence-based model or inventing our own scorecard, and is that the right call?** Established models (DORA for delivery, SAMM or BSIMM for security, TMMi for testing) carry research and external comparability that a homegrown grid cannot match. A lightweight internal four-level scale is faster and more actionable, and it is often the better choice for internal steering. The trap is inventing a heavyweight bespoke framework that has all the ceremony of a formal model and none of the evidence base. Decide per domain: reserve formal appraised models for where a contract requires them, use evidence-based models where they exist and fit, and keep a simple per-capability scale for everything else. Bring the list of domains, mark which model each one uses today, and challenge every invented scorecard.

3. **Who runs our assessments, how would we catch generous grading, and how often do we re-assess?** An assessment that grades itself flatters itself, and maturity drifts as people, systems, and threats change, so a two-year-old appraisal is often fiction. Rotate assessors or bring in an external sanity check, and treat a suspiciously high self-score as a smell to chase, not a win to celebrate. Set a re-assessment cadence tied to how fast each domain changes: security more often than, say, documentation. Gather evidence and involve the people doing the work rather than collecting opinions from managers. If your answer is that one team scores itself once a year with no cross-check, you are measuring comfort, not capability.

4. **What target maturity level does each capability actually need, and where would pushing higher only buy us process weight?** Higher is not free: every level up costs effort and usually adds ceremony, so a blanket goal of level 5 everywhere drains a finite improvement budget into bureaucracy that some domains will never repay. For a large organization the right target varies by capability, because a low-risk area sitting at level 2 may be perfectly safe while a safety- or compliance-critical area at the same level is an emergency. Bring a per-capability risk rating, an honest estimate of what the next rung costs in effort and process, and any audit or contractual floor, since many audits require at least a defined level 3. In enterprise and government settings, some regulated capabilities genuinely need the top rungs while most are well served at level 3, so decide targets deliberately, capability by capability, and stop climbing once the risk-adjusted return does.

5. **The last time we raised a maturity level, did the outcome it was meant to protect actually improve, or did only the score move?** A level that climbs while incidents, lead time, or defect rates stay flat is Goodhart's Law in action: once the number becomes the target, it stops measuring capability. For a large team this slips by easily, because a successful appraisal feels like progress even when production tells a different story. Tie each capability's level to a real outcome metric before you invest, then bring the before-and-after evidence to the discussion: incidents per quarter, change-failure rate, time to recover, whatever the capability exists to improve. In enterprise and government portfolios where an appraised level gates eligibility, the gap is dangerous, because the level can rise on assembled evidence while the underlying practice quietly decays, and the first proof of that is a breach, outage, or failed audit.

6. **Do we communicate one headline maturity grade or a per-capability picture, and are levels ever tied to reward, ranking, or team standing?** A single overall number is easy to present to leadership and hides exactly the unevenness that matters, because strong delivery can mask a level-1 security capability; a per-capability heat map is more work yet shows where low maturity meets high risk. The harder question is how the scores get used, because the moment a level is tied to a team's reward or ranking, honest reporting dies and effort flows into the appearance of maturity rather than the substance. Bring the heat map, and a frank account of every place a level currently feeds a performance review, a budget decision, or a vendor scorecard. For enterprises and government suppliers, where appraised levels can gate revenue and eligibility, be explicit about which grades carry consequences and which exist only to steer, because a maturity picture people are rewarded for inflating stops describing reality.

## Sector lens

**Startup.** A heavyweight appraised model is overhead you cannot afford on a short runway. Run a one-hour self-assessment on a simple scale across a handful of capabilities, fix only the lowest-maturity gap that blocks something concrete (say, the security questionnaire from your first enterprise customer), and leave the rest alone. The assessment should cost an afternoon, not a consultant, and its output is a single next action rather than a uniform high score you neither need nor can fund.

**Small business.** With no dedicated assessor and a tight budget, borrow a lightweight public model rather than commission a bespoke framework: a short delivery or security checklist you can self-score. Treat it as a yearly conversation about where a weak spot would cost you a customer, not a standing programme. Keep it cheap and blunt, because a flattering score you paid a vendor to produce is worth less than a candid one you did yourself in an afternoon.

**Enterprise.** The value is a shared per-capability scorecard applied consistently across many teams, so gaps become comparable and improvement budget flows to where low maturity meets high risk. Guard hard against maturity theatre once levels feed budget or status: rotate or externally sanity-check assessors, and manage the results as a heat map that directs paved-road investment (chapter 4.2) rather than a league table that ranks teams and kills honest reporting.

**Government.** A maturity level is often a literal gate here: CMMC for defence work, a CMMI appraisal as a supplier qualification. Meet the required level with genuine capability, and keep a candid internal self-assessment separate from the formal appraisal so the audit floor never quietly becomes the ceiling. Document evidence transparently for appraisers, and treat any distance between the certified level and real practice as accountable risk to close, not paperwork to file.

## Examples

**Startup.** A ten-person SaaS startup runs a one-hour self-assessment against a simple four-level scale covering delivery, testing, security, and on-call. It finds delivery and testing at level 3 but security stuck at level 1, which matters because it is about to sign its first enterprise customer with a security questionnaire. So the founders spend the next month raising just security to a defensible level 2 and leave the rest alone, rather than chasing a uniform high score they neither need nor can afford yet.

**Enterprise.** A financial-services firm assesses its 40 teams with a lightweight per-capability scorecard (delivery, testing, security, observability, on-call). The heat map reveals that security maturity lags most where regulatory exposure is highest, so the platform team funds paved-road security tooling (chapter 4.2) for those teams first. Because the assessment is used to prioritize investment rather than rank teams, managers report honestly. Re-assessment a year later shows real movement, and, crucially, fewer security incidents, not just higher scores.

**Government.** A defence contractor must reach a required CMMC level to bid on work, and a systems integrator holds a CMMI appraisal as a contract qualification. Here the maturity level is a literal gate to revenue. The well-run version treats the required level as a floor for genuine capability and keeps a candid internal self-assessment separate from the formal appraisal. The poorly-run version assembles evidence for the appraisal and lets real practice decay the day after, passing the audit while remaining exposed.

## Business case: motivations, ROI, and TCO

The return on maturity assessment comes from **directed investment**. Improvement budgets are finite. Spent blindly, they fund whatever is loudest. A maturity assessment shows you where capability is weakest against risk, so the same spend buys more risk reduction and more outcome improvement. The assessment itself is cheap, only days of structured, evidence-based review, set against the cost of misallocated improvement programmes or, worse, an undetected capability gap that surfaces as a breach, outage, or failed audit.

On **total cost of ownership**, the discipline is low-cost when you keep it lightweight and high-cost when it hardens into appraisal bureaucracy. The dominant hidden cost is *maturity theatre*: effort spent producing the appearance of maturity returns nothing and can mask real risk, which is negative ROI. To make the case to leadership, present maturity as a risk-and-investment lens, a heat map that turns "improve everything" into "improve these three things first," and explicitly budget against the temptation to chase levels for their own sake. Where a level is contractually required (CMMC, CMMI), the ROI is direct: it is the price of eligibility, and the goal is to meet it with real capability rather than costly pretence.

## Anti-patterns and pitfalls

- **Level as the goal:** chasing a number instead of the capability it is meant to represent.
- **Maturity theatre:** assembling evidence for an appraisal while real practice decays.
- **One global grade:** a single maturity score that hides dangerous unevenness.
- **Higher-is-always-better:** pushing every capability to level 5 regardless of risk or cost.
- **Assess once, never again:** a one-time appraisal treated as permanent truth.
- **Ranking teams to blame:** using maturity for punishment, which kills honest reporting.
- **Model worship:** following a heavyweight framework's ceremony past the point of usefulness.
- **Ignoring outcomes:** climbing the ladder while delivery, reliability, or security do not improve.

## Maturity model

- **Level 1, Initiate.** No shared notion of maturity; capability is assumed, uneven, and unmeasured; any assessment is reactive, triggered by an incident or an audit demand rather than planned.
- **Level 2, Develop.** A few teams run ad hoc assessments against some scale, but the model, cadence, and rigour vary team to team; results are used inconsistently and evidence is thin, so scoring for appearance is an ever-present risk.
- **Level 3, Standardize.** A single per-capability model and assessment cadence are documented and applied org-wide; assessments are evidence-based, involve the people doing the work, and feed a prioritized improvement backlog rather than a report card.
- **Level 4, Manage.** Maturity is measured and controlled with data: each capability's level is tracked against a baseline, tied to an outcome metric (incidents, lead time, change-failure rate), and re-assessed on a set cadence, so drift and generous grading show up as numbers rather than opinions, and targets are set deliberately per domain against risk and cost.
- **Level 5, Orchestrate.** Assessment is integrated across the organization and continuously improved: maturity, risk, and outcomes inform investment as one adaptive picture, targets are rebalanced as threats and context shift, assessors are rotated or externally checked as a matter of course, and the practice actively retires ceremony that no longer earns its cost.

## Ideas for discussion

1. Which of your capabilities are you assuming are mature without evidence?
2. Where does your lowest maturity coincide with your highest risk, and is that where your improvement budget is going?
3. Is any maturity level in your organization a target or a gate? What behaviour has that produced?
4. What is the right target level for each capability, and where would climbing further just add bureaucracy?
5. Would your teams report their maturity honestly, or does the way you use scores punish candour?
6. When you last "improved maturity," did outcomes actually change?

## Key takeaways

- A maturity model assesses capability against a ladder of levels and describes a path to improve: a mirror, not a trophy.
- Pick established, evidence-based models per domain (CMMI, DORA, SAMM/BSIMM, CMMC); a lightweight per-capability scale is often most actionable.
- **Assess honestly, per capability**, and use results to **prioritize by risk**, not to rank or blame.
- **Higher is not always better:** set target levels deliberately against risk and cost.
- Beware **maturity theatre** and **Goodhart's Law**: a level that becomes a target stops measuring capability.
- See chapter 12.4 for this book's consolidated maturity self-assessment, and every chapter's own maturity section.

## References and further reading

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defense, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
