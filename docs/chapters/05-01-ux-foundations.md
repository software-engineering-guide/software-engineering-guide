# 5.1 UX foundations

## Overview and motivation

[User experience](https://en.wikipedia.org/wiki/User_experience) (UX) is about understanding people (their goals, their contexts, their constraints) and then shaping software so it helps them succeed with the least friction. It is not decoration you apply at the end. It is a way of working that begins before the first line of code and continues well after release. This chapter covers the research, modelling, and [design-thinking](https://en.wikipedia.org/wiki/Design_thinking) practices that let a large organization make product decisions from evidence rather than from guesses.

For large teams, UX is a coordination problem as much as a craft. When dozens of squads ship into one shared product, mismatched mental models, duplicated flows, and contradictory terminology pile up into a confusing whole that no single team owns. A shared UX foundation, built from common personas, agreed journey maps, and a documented [information architecture](https://en.wikipedia.org/wiki/Information_architecture), gives every team the same map of the user, so their separate decisions add up to a coherent experience. Without it, each team optimizes locally and the product as a whole makes no sense.

Enterprise and government raise the stakes. Enterprise software often has captive users who cannot walk away, so bad UX gets paid for in training, support tickets, errors, and lost productivity rather than in people leaving. Government services often reach the entire public, including people in crisis, on old devices, with low digital confidence, or with no alternative provider. Here UX quality is a matter of equity and civic trust: a poorly designed benefits application can deny someone food or housing, not because they are ineligible, but because they could not finish the form.

## Key principles

- Design for real people doing real tasks in real conditions, not for an idealized user on a fast connection with full attention.
- Research reduces risk. The cheapest time to discover a wrong assumption is before you have built on top of it.
- Users cannot reliably tell you what they will do; observe behaviour, not just stated preference.
- Focus on the job the user is trying to get done, not the feature you want to ship.
- Consistency is a feature: a coherent mental model across the product lowers cognitive load.
- [Accessibility](https://en.wikipedia.org/wiki/Accessibility) and inclusion are part of good UX from the start, not a later compliance pass.
- Qualitative and quantitative methods answer different questions; use both.
- Small, frequent research beats rare, heavyweight studies.

## Recommendations

### Establish continuous, mixed-method research

Aim for a lightweight but continuous research practice rather than occasional big studies. Interviews reveal motivations and mental models. [Usability testing](https://en.wikipedia.org/wiki/Usability_testing) reveals where designs break down; five to eight participants per round surfaces most of the severe issues. Surveys measure attitudes at scale but cannot explain the "why." Analytics and instrumentation show what people actually do across the whole population. Pair a qualitative method (why) with a quantitative one (how many), so findings are both explained and sized. And keep a research repository, so insights stay searchable and reusable across teams instead of getting lost in one squad's slides.

### Model users with personas, journey maps, and jobs-to-be-done

Build a small set of evidence-based personas that capture goals, contexts, and constraints, not demographic caricatures. Frame needs as jobs-to-be-done, the underlying outcome a user is trying to achieve rather than a feature ("when I lose my job, I want to quickly understand what support I qualify for, so I can keep paying rent"). This keeps the focus on outcomes rather than features. Journey maps chart the whole experience across channels and over time, exposing gaps and handoffs that no single screen reveals. For services with heavy back-stage operations (call centres, caseworkers, fulfilment), use [service blueprints](https://en.wikipedia.org/wiki/Service_blueprint) to connect the front-stage experience to the systems and staff behind it.

### Design the information architecture deliberately

Information architecture (IA) is how content, features, and navigation are structured and labelled. Use [card sorting](https://en.wikipedia.org/wiki/Card_sorting) and tree testing to derive that structure from users' mental models rather than from your org chart. A common failure in large organizations is exposing internal departmental boundaries as top-level navigation. Establish a controlled vocabulary so the same concept has the same name everywhere. [Interaction design](https://en.wikipedia.org/wiki/Interaction_design) then defines the moment-to-moment behaviour: states, feedback, error recovery, and the flow between steps.

### Apply design thinking pragmatically

The double-diamond model (diverge then converge to define the right problem, then diverge and converge to design the right solution) is a useful frame. Treat it as a mindset, though, not a rigid gated process. In practice, run tight loops: frame a hypothesis, sketch, test with a handful of users, and learn within days. Save the heavier discovery for genuinely novel or high-risk problems. And watch out for "innovation theatre," where workshops produce sticky notes but no shipped change.

### Integrate UX into delivery

Embed designers and researchers in delivery teams rather than running a separate "UX department" that hands off specs over a wall. Make research findings a standing input to prioritization. Put UX quality gates, such as usability benchmarks and accessibility checks, in the definition of done. And track outcome metrics (task success, time on task, error rate, satisfaction) right alongside your delivery metrics.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Continuous discovery research | Catches problems early, builds shared understanding | Ongoing cost, needs recruiting pipeline and skilled staff |
| Heavyweight upfront research | Deep insight before major investment | Slow, can delay learning that only shipping reveals |
| Analytics-only decisions | Scales, objective, cheap once instrumented | Explains what but not why; blind to non-users and edge cases |
| Personas and journey maps | Align many teams on one model of the user | Go stale, can become fiction if not refreshed with data |
| Embedded designers | Fast feedback, shared ownership | Harder to keep craft consistent across many teams |

Every organization balances research investment against delivery speed. The mistake is treating this as either-or. The productive stance is proportional: spend more discovery on decisions that are expensive to reverse (core IA, primary flows, platform choices), and less on details you can easily change later. The cost of research is almost always small next to the cost of building the wrong thing well.

## Questions to discuss with your team

1. **Who owns the shared information architecture and controlled vocabulary, and what happens when a team wants to deviate?** At scale the most common failure is letting each squad expose its own org-chart structure and its own names for the same concept, so the product ends up with three words for one thing and navigation that mirrors departments instead of user tasks. Decide now whether IA and vocabulary are owned centrally, derived from card sorting and tree testing rather than internal politics, and how a team requests a change. This matters more in enterprise and government because captive users cannot walk away, so incoherence gets paid for in training, support tickets, and errors rather than churn. Bring the current list of duplicate terms and conflicting flows as evidence. If you cannot name an owner, that is your first action item.

2. **What is our recruiting pipeline for research participants, and does it reach assisted-digital, low-confidence, and non-digital users?** Continuous discovery only works if you can get in front of real users every week, and the hardest people to recruit are often the ones who most need the service: people in crisis, on old devices, or who normally rely on help. Testing only confident, connected volunteers gives you a flattering but false read, especially for public services where equity of access is the whole point. Agree on who runs recruiting, what incentives you offer, and how you observe assisted-digital sessions without adding to a vulnerable person's burden. Bring the participant demographics from your last three studies and check them against your actual user base. If they skew toward easy-to-reach users, fix the pipeline before you trust the findings.

3. **Which UX quality gates belong in our definition of done, and how do we stop them becoming theatre?** Embedding designers and researchers only pays off if research is a standing input to prioritization and if usability and accessibility checks actually block a story from shipping, not a slide deck everyone nods at and ignores. Pick concrete outcome metrics you will track alongside delivery metrics: task success, time on task, error rate, and satisfaction. The risk is research run to justify decisions already made, so agree who can veto a launch on a UX gate and what evidence overrides an executive's opinion. Bring one recent feature and ask whether its research changed the decision or merely decorated it. If findings never move a roadmap, your gates are cosmetic.

4. **How do we keep our personas, journey maps, and IA from decaying into fiction once the research that produced them is a year old?** Shared models are what let dozens of teams design toward one coherent experience, but they only work while they still describe real users, and the moment a persona becomes an artefact people cite to win arguments rather than a summary of evidence, it does active harm. Decide who owns refreshing each model, on what cadence, and against what data (fresh interviews, analytics, support themes), and agree a visible "last validated" date so stale models are obvious. The competing consideration is cost: refreshing everything continuously is wasteful, so tie refresh frequency to how fast that part of the user base or journey actually changes. Bring the provenance of your current top personas and ask when each was last checked against a real user. In enterprise and government, where a captive or public user base shifts slowly but consequentially (an ageing population, a new benefit, a device transition), a model that quietly drifts out of date can steer years of investment toward users who no longer exist.

5. **Where does accessibility live in our process, and can we prove a release meets it before it ships rather than after a complaint?** Treating accessibility as a late compliance pass is both the most common failure and the most expensive, because retrofitting semantics, focus order, and contrast into a built interface costs far more than designing them in. Decide which standard you hold yourselves to (for example WCAG, the Web Content Accessibility Guidelines), whether conformance is a blocking gate in the definition of done, and who is accountable when an inaccessible feature reaches production. The tension is speed versus inclusion, and teams under deadline pressure will quietly drop the checks that are not enforced. Bring your last audit, the automated and manual coverage behind it, and the number of accessibility issues found after release rather than before. For government especially this is not optional politeness: it is often a legal duty and a matter of equity, since a public service that excludes disabled or assisted-digital users has failed at its core purpose, not a secondary one.

6. **When our analytics and our qualitative research disagree, how do we decide which to believe, and who arbitrates?** Large organizations accumulate both dashboards that show what thousands of users do and interviews that explain why a handful behave as they do, and the two will routinely point in opposite directions: a flow with high completion that quietly humiliates people, or a feature users praise in sessions but never touch at scale. Agree in advance how you triangulate, which question each method is trusted to answer (analytics for magnitude and reach, research for cause and meaning), and who has authority to call the decision when they conflict. The risk is cherry-picking whichever source flatters the plan already chosen. Bring a concrete recent disagreement and walk through how it was actually resolved. In enterprise and public settings the stakes are sharpened because analytics systematically undercount the very people who matter most: non-users, abandoners, and those on assistive technology rarely show up in the funnel, so trusting numbers alone can render the excluded invisible.

## Sector lens

**Startup.** You have no researcher and no time for a repository, so make research a founder habit: sit beside five real users for an afternoon before building the next thing. Skip formal personas and journey maps; a shared understanding of the one job you are solving, refreshed by watching people weekly, beats documentation nobody maintains. Your advantage is that the whole team can absorb an insight the same day it appears, so protect that speed and resist ceremony.

**Small business.** With no UX specialist and a tight budget, lean on the conventions your users already know rather than inventing your own, and buy tools with sensible defaults instead of designing flows from scratch. Do the cheap, high-value research yourself: a handful of usability sessions over a video call and a read of your support tickets will surface most of the severe problems. Treat accessibility basics (contrast, labels, keyboard access) as table stakes you get from a good component library rather than a project you staff.

**Enterprise.** The core problem is coherence across many teams, so invest in the shared foundations: owned personas, maintained journey maps, a controlled vocabulary, and a documented information architecture that squads design toward rather than around. Embed designers and researchers in delivery teams, but govern craft centrally so the product does not fracture into inconsistent dialects. Fund a research repository and quality gates in the definition of done, and track UX outcome metrics as a portfolio so no single team's local optimization degrades the whole.

**Government.** Accessibility and equity of access are duties, not preferences, so hold releases to a published standard and research with the full range of the public, including assisted-digital, low-confidence, and non-digital users. Procurement and transparency shape delivery: publish your design principles and research methods, structure services around citizens' life events rather than internal departments, and keep evidence of testing for audit. Because users often have no alternative provider, a flow they cannot finish denies a service, so treat completion by the hardest-to-reach user as the real measure of success.

## Examples

**Startup.** A four-person startup building a scheduling tool for small clinics had strong opinions about what receptionists needed, but no evidence. Before writing more features, the founders sat beside five receptionists for an afternoon each and watched them work. They learned that the real pain was not booking speed but double-bookings caused by a confusing calendar view, something no one had thought to mention in earlier sales calls. Reframing the product around that one job, and sketching and testing fixes with the same five people over a week, turned a stalling trial into their first paying customers.

**Enterprise.** A multinational bank consolidated seven regional internal loan-origination tools into one platform. Rather than merging feature sets, the team ran journey mapping and service blueprinting with underwriters across regions. They found that the "regional differences" everyone assumed were mostly inconsistent terminology and screen order, not genuine process differences. A unified IA and shared vocabulary cut underwriter training time substantially and reduced processing errors, because staff now shared one mental model.

**Government.** A national tax authority redesigning its online filing service ran moderated usability testing with taxpayers spanning ages, devices, and digital-confidence levels, plus assisted-digital observation of people who normally rely on help. Testing revealed that jargon-laden section headings caused people to abandon or misfile. Reframing content around taxpayers' jobs-to-be-done, and restructuring the IA around life events rather than internal tax codes, increased successful self-service completion and reduced call-centre volume, directly lowering cost to serve while improving equity of access.

## Business case: motivations, ROI, and TCO

The return on UX comes from three levers: more success (more users complete valuable tasks), lower cost to serve (fewer support contacts, less training, fewer errors), and less rework (catching wrong directions before they are built). In enterprise settings where users are captive, the payoff shows up as productivity and fewer errors rather than conversion; a few seconds saved per transaction, across thousands of employees, compounds into large annual savings.

Total cost of ownership has to weigh the cost of adopting against the cost of not adopting. The adoption costs are easy to see: researchers and designers, recruiting and incentives for participants, tooling, and time in the schedule. The cost of not adopting is larger but harder to spot: abandoned transactions, support and training overhead, expensive late redesigns, failed launches, and reputational or legal exposure when public services exclude people. Because these costs are spread across support, training, and operations budgets rather than the product line, leadership often underestimates them.

To make the case to leadership, tie UX to metrics executives already track: completion and conversion rates, cost per transaction, support ticket volume, training days, and error and rework rates. Run a small, instrumented pilot that shows a measurable before-and-after, then extrapolate across the portfolio. Framing research as risk reduction on irreversible decisions tends to resonate with finance and governance stakeholders.

## Anti-patterns and pitfalls

- **HiPPO-driven design**: decisions made by the highest-paid person's opinion instead of evidence.
- **Research theatre**: studies run to justify decisions already made, findings ignored.
- **Personas as fiction**: invented profiles never validated against real users, used to win arguments.
- **Org chart as IA**: navigation that mirrors internal departments rather than user tasks.
- **Big-bang research**: rare, expensive studies that arrive too late to change anything.
- **Testing only the happy path**: ignoring error states, edge cases, and users under stress.
- **Design as a final coat of paint**: bringing UX in only to make a finished build "look nice."
- **Ignoring assisted and non-digital users**: designing only for confident, connected users.

## Maturity model

**Level 1: Initiate.** No dedicated UX practice. Decisions are made by opinion and the highest-paid person's instinct. Research, if it happens at all, is ad hoc and reactive, triggered by a launch that went badly. Flows and terminology are inconsistent across teams, and nobody owns the overall experience.

**Level 2: Develop.** Some teams have designers and run occasional usability tests, and a few personas or journey maps exist, but practice varies widely between squads and is not maintained. UX is treated as a phase rather than a continuous discipline, and it is often bypassed under schedule pressure. Good work happens in pockets but does not add up across the product.

**Level 3: Standardize.** Continuous mixed-method research feeds prioritization, and shared personas, journey maps, and a controlled-vocabulary IA are documented and used across teams. UX quality gates, including usability benchmarks and accessibility checks, sit in the definition of done and are enforced org-wide. A searchable research repository keeps insights reusable rather than trapped in one squad's slides.

**Level 4: Manage.** The practice is measured against baselines rather than merely performed. You track task success, time on task, error rate, satisfaction, and accessibility conformance as agreed metrics, set targets, and watch them over releases. Research participant samples are checked against the real user base so findings are representative, quality gates report pass rates rather than opinions, and the cost of research is weighed against measured reductions in support contacts, training, and rework. Decisions to ship or hold rest on evidence against those baselines.

**Level 5: Orchestrate.** Research is continuous, outcome-linked, and integrated with product, business, and risk planning across the organization. Teams run controlled experiments, close the loop from insight to shipped change to measured effect, and retire or re-scope models of users as the population and its journeys shift. The UX foundation adapts continuously: personas, journeys, IA, and standards are refreshed on evidence, and the organization rebalances where it invests discovery as reversibility and risk change.

## Ideas for discussion

- How much discovery is "enough" before committing to a direction, and who decides?
- How do you keep personas and journey maps alive rather than letting them become stale artifacts?
- When quantitative analytics and qualitative research disagree, which do you trust and why?
- How should a large organization balance a central UX standard with each team's autonomy?
- What is the right way to research services used by people in crisis without adding to their burden?
- How do you measure the ROI of research that prevents a mistake you therefore never made?

## Key takeaways

- UX is a way of working from the start, not decoration at the end.
- Combine qualitative methods (why) with quantitative methods (how many).
- Model users with evidence-based personas, journey maps, jobs-to-be-done, and service blueprints.
- Structure information around users' mental models, not the org chart.
- Treat design thinking as a pragmatic mindset with tight learning loops, not a rigid process.
- The cost of research is small compared with the cost of building the wrong thing.
- In enterprise and government, UX quality translates directly into productivity, cost to serve, and equity of access.

## References and further reading

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, and Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* and *Design Principles*
- U.S. General Services Administration, *18F Methods* and the *U.S. Web Design System* research guidance
- Nielsen Norman Group, research method articles and reports
