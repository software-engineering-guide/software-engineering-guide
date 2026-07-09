# 10.7 Agile

## Overview and motivation

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) is a mindset for delivering software (and value) iteratively, incrementally, and in close collaboration with the people who will use it. Codified in the 2001 *Manifesto for Agile Software Development*, it is best understood not as a process but as a set of **values and principles**: prioritize individuals and interactions, working software, customer collaboration, and responding to change, over the plan-heavy, contract-heavy, documentation-heavy defaults that came before. Frameworks like [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), and [Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming) (XP) are *implementations* of that mindset. They are useful starting points, but not the mindset itself. This chapter complements chapter 1.4 (ways of working, which surveys methods broadly) by going deep on Agile specifically.

Agile is driven by the same force that animates the discovery and delivery pipelines (chapters 11.1–11.2): requirements for software are *discovered*, not fully known up front, and the world changes faster than a long plan can absorb. Big-bang, plan-everything-first delivery repeatedly produces systems that are late, over budget, and, worst of all, wrong, because all the learning arrives at the end, when it is most expensive to act on. Agile's core bet is simple: short cycles of building real, working software and getting real feedback beat long cycles of speculation. Done well, it reduces risk continuously rather than deferring it.

For large teams, enterprise, and government, Agile is both powerful and frequently mangled. Enterprises adopt it across hundreds of teams and often reduce it to ritual ("we do stand-ups now") without changing how decisions are made or how value is measured. Government has embraced Agile deliberately, because iterative, user-centered delivery demonstrably reduces the risk of large public programs: the U.S. Digital Service and its *Digital Services Playbook*, the UK's Government Digital Service and Service Standard, and agile procurement reforms all arose partly in response to high-profile [waterfall](https://en.wikipedia.org/wiki/Waterfall_model) failures. The prize is real. So is the failure mode of "agile in name only."

## Key principles

- **Value the Manifesto's four values** (people, working software, collaboration, and responsiveness) over process artifacts.
- **Deliver working software frequently** in small increments; working software is the primary measure of progress.
- **Welcome change**, even late; adaptability is a feature, not a failure.
- **Build around motivated, empowered, self-organizing teams.**
- **Collaborate continuously with users and stakeholders.**
- **Reflect and improve** at a regular cadence.
- **Sustain a humane pace** and technical excellence: speed without craft collapses.

## Recommendations

### Anchor on values and principles, not ceremonies

The single most important Agile recommendation is to lead with the *why*. A team that holds a daily stand-up, a sprint review, and a retrospective, but still commits to fixed scope on a fixed date, hides bad news, and never changes the plan, is not agile. It is waterfall with meetings. Use the twelve principles as a checklist for genuine agility. Are you delivering working software often? Can you welcome a change next iteration? Does the team decide *how* to do the work? Is the customer actually in the loop? If the ceremonies aren't producing those outcomes, fix the outcomes, not the ceremonies.

### Choose a framework as a starting point, not a religion

Pick a framework that fits the work and adapt it:

- **Scrum:** timeboxed sprints, a prioritized backlog, and defined roles (product owner, scrum master, developers). Good for feature delivery with a clear product owner; weak when work is highly interrupt-driven.
- **Kanban:** continuous flow with explicit work-in-progress limits and a pull system. Good for support, operations, and unpredictable arrival (and directly grounded in flow and queueing theory, see chapters 11.2, 11.3). Limiting WIP shortens lead time ([Little's Law](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** engineering practices including [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development), [pair programming](https://en.wikipedia.org/wiki/Pair_programming), [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), refactoring, small releases. The technical backbone that makes any framework sustainable.
- **Scrumban** and blends: pragmatic combinations many mature teams converge on.

Frameworks are scaffolding. Keep what helps, drop what doesn't, and never let "the framework says so" override "the principles say why."


### Insist on technical excellence

Agile without engineering discipline degrades quickly into fast production of unmaintainable code, "dark scrum," where teams sprint themselves into a tar pit of defects and [technical debt](https://en.wikipedia.org/wiki/Technical_debt). The XP practices are not optional extras. Continuous integration (chapter 8.1), automated testing (chapter 2.4), refactoring, trunk-based development (chapter 2.6), and clean design (chapter 2.2) are what let a team keep changing software cheaply, which is the entire premise of agility. Sustainable pace matters for the same reason: burned-out teams cannot sustain quality or responsiveness.

### Scale with care, and prefer descaling

Scaling frameworks, such as SAFe (the Scaled Agile Framework), LeSS, Nexus, and Scrum@Scale, coordinate many teams toward shared goals. They can help, but they carry a warning (echoing chapter 1.4): heavy scaling frameworks often reintroduce the very command-and-control, plan-heavy overhead Agile was meant to remove. Before you adopt a big framework, try *descaling*. Organize around independent, stream-aligned teams with clear ownership and minimal cross-team dependencies (chapter 1.2), so you need less coordination machinery in the first place. Where coordination is genuinely required, add the lightest structure that works, and connect it to outcomes (OKRs, objectives and key results, chapter 11.1), not output.

### Make agility real in enterprise and government

Adaptive delivery and institutional constraints can coexist, but it takes deliberate design:

- **Hybrid governance:** an adaptive delivery core inside a predictive funding/compliance shell (chapter 10.6), so iteration satisfies rather than fights oversight.
- **Agile procurement:** modular, outcome-based contracts and shorter increments instead of one fixed-scope megacontract; this is where public-sector Agile most often succeeds or fails.
- **Compliance as you go:** build audit, accessibility (chapter 5.3), and security (chapter 4.1) into the increment via automation and fitness functions (automated checks that continuously verify architectural and quality properties; chapters 8.5, 1.6), not a late gate.
- **Real user access:** the hardest and most important. Teams need genuine contact with citizens or customers, which procurement and security rules often obstruct.

### Improve continuously, and mean it

The retrospective is Agile's engine of improvement, and it is worthless if it produces no change. Run retrospectives that generate a small number of concrete, owned actions, and actually complete them before the next one. Measure outcomes (did the change move a key result? see chapter 11.1) and flow (are lead times shrinking? see chapters 11.2, 11.3). Don't measure velocity: it is a capacity signal that becomes a lie the moment you use it as a productivity target.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| **Agile (adaptive)** | Fast feedback; absorbs change; early, continuous value | Harder to fix scope/cost up front; demands engaged customer & discipline |
| **Waterfall (predictive)** | Predictable scope; contract/audit-friendly | Late feedback; big-bang risk; poor fit for uncertain requirements |
| **Scrum** | Cadence, roles, focus; widely understood | Ceremony overhead; struggles with interrupt-driven work |
| **Kanban** | Flow, WIP limits, flexible; great for ops | Less structure; needs discipline to hold limits |
| **Heavy scaling (SAFe)** | Coordinates many teams; familiar to large orgs | Can reintroduce command-and-control; ceremony-heavy |
| **Descaling / team autonomy** | Less coordination overhead; faster teams | Requires low coupling and strong platform/ownership |

The defining tension is **adaptability versus predictability**, and the classic misread is that Agile means "no plan." It does not. It means planning continuously and committing to *outcomes and cadence* while letting *scope* flex. The other recurring trap is treating Agile as *only* process (ceremonies) or *only* engineering (XP). It needs both.

## Questions to discuss with your team

1. **In your enterprise or government context, are your contracts modular and outcome-based, or is delivery locked inside one fixed-scope megacontract?** Agile procurement is where public-sector agility most often succeeds or fails, because a single fixed-price, fixed-scope contract forces waterfall no matter what the delivery teams call their meetings. Modular, outcome-based contracts with shorter increments let scope flex to a valuable core within fixed funding, which is exactly the pattern behind modern public-sector successes and the antidote to past big-bang failures. Bring evidence: look at your current contracts and ask whether a vendor is paid for demonstrated working software or for a fixed scope signed off years ago. The answer should shape how you structure the next procurement far more than which framework your teams adopt internally. You cannot be adaptive in delivery while your contract mandates a distant, all-or-nothing go-live.

2. **Are audit, accessibility, and security built into each increment through automation, or bolted on as a late gate?** Compliance-as-you-go is what lets adaptive delivery coexist with institutional constraints: build the checks into the increment via automation and fitness functions rather than saving them for a pre-release scramble. A late compliance gate reintroduces the big-bang risk Agile exists to remove, because the expensive problems surface at the end when they are hardest to fix. Bring evidence: for your last increment, check whether accessibility, security, and audit evidence were verified automatically in the pipeline or deferred to a manual review before launch. The answer should push these properties into continuous automated checks, so oversight is satisfied by the act of building rather than by a separate phase. This is also what keeps a regulated program honest between audits instead of only in the weeks before one.

3. **How would you know if your teams are sprinting into technical debt, and what protects sustainable pace under launch pressure?** Agile without engineering discipline degrades into dark scrum, where teams sprint fast into a tar pit of defects and unmaintainable code, and burned-out teams cannot sustain quality or responsiveness. The XP practices (continuous integration, automated testing, refactoring, trunk-based development) are what let a team keep changing software cheaply, which is the entire premise of agility, so they are not optional extras to trade away when a date looms. Bring evidence: track whether lead times are shrinking or growing, whether defect rates are climbing, and whether the team is quietly working longer hours to hit each sprint. The answer should make technical excellence and humane pace non-negotiable, because speed bought by sacrificing craft collapses within a few iterations. Measure flow and outcomes, never velocity as a target, because the moment you make a capacity signal a productivity goal it becomes a lie.

## Examples

**Startup.** A five-person startup skips the ceremony debate and lives the Agile values directly. It ships a working slice to real users every week, sits close enough to founders and early customers that feedback arrives daily, and welcomes a change of direction next week when the evidence says the current bet is wrong. The team refuses to trade away technical excellence for speed, so continuous integration, automated tests, and trunk-based development are non-negotiable even under launch pressure, and each Friday retrospective produces one concrete change the team actually finishes before the next. It never tracks velocity as a target, measuring instead whether shipped work moved activation and whether lead times are shrinking.

**Enterprise.** A telecom's 60-team transformation initially "does Scrum" but sees no improvement. Teams still receive fixed annual scope and report on velocity. A reset refocuses on principles: quarterly OKRs replace feature mandates, teams are re-organized to reduce cross-team dependencies (descaling), and XP practices (CI, TDD, trunk-based development) are made non-negotiable. Lead times fall, defects drop, and, crucially, the business starts measuring outcomes rather than story points, connecting Agile delivery to the discovery pipeline (chapter 11.1).

**Government.** A digital-service team rebuilds a citizen-facing benefits application using Agile inside a hybrid governance shell: two-week increments delivering working, user-tested software; accessibility and security built into every increment; and modular procurement replacing a single fixed-price contract. Real usability testing with citizens (including assistive-technology users) each iteration catches problems the old waterfall process would have shipped. The program delivers a usable service early and shows measurable public value to oversight bodies. This is the pattern behind modern public-sector successes, and the antidote to past big-bang failures.

## Business case: motivations, ROI, and TCO

Agile's return comes from **risk reduction and faster value realization**. By delivering working software early and often, teams turn uncertainty into evidence continuously, catching wrong-thing and won't-work failures while they are cheap, instead of at a distant, expensive go-live. The research behind modern delivery (the DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), findings in chapter 11.2) shows that the practices Agile promotes (small batches, frequent releases, fast feedback, technical excellence) correlate with better delivery *and* stability *and* organizational performance. Early increments also start returning value sooner, improving the timing and total size of ROI versus a big-bang release that returns nothing until the end.

On **[total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, Agile lowers the cost of change over a system's life, provided the engineering discipline is real. Its dominant risk is *fake agile*: ceremony without principle or craft, which adds meeting overhead while delivering none of the benefit, and can be worse than an honest waterfall. So the business case is conditional. The ROI is high when you adopt Agile as mindset-plus-engineering, and roughly zero (or negative) when you adopt it as ritual. Make the case to leadership by framing Agile as continuous risk reduction and outcome measurement, not as "going faster," and by insisting the investment includes technical practices, not just new meetings.

## Anti-patterns and pitfalls

- **Fake / cargo-cult agile:** ceremonies performed while decisions, funding, and mindset stay waterfall.
- **Velocity as productivity:** turning a capacity estimate into a target, which corrupts it ([Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** sprinting without technical excellence into unmaintainable, defect-ridden code.
- **Retrospectives without change:** reflection that produces no completed actions.
- **Fixed scope *and* date *and* cost:** calling it agile while quality silently absorbs the pressure.
- **Absent customer:** no real user feedback, so iterations optimize the wrong thing.
- **Framework worship:** "SAFe/Scrum says so" overriding the principles and the team's judgment.
- **Scaling before descaling:** adding heavy coordination frameworks instead of reducing dependencies.

## Maturity model

- **Level 1 (Initial):** Waterfall or ad hoc delivery; big-bang releases; no iterative feedback.
- **Level 2 (Managed):** Agile ceremonies adopted (stand-ups, sprints) but mindset and engineering practices lag; velocity treated as output; scope still fixed up front.
- **Level 3 (Defined):** Values and principles genuinely guide work; XP-style technical excellence in place; teams self-organize; customers engaged; retrospectives drive real change.
- **Level 4 (Optimizing):** Adaptive delivery tied to outcomes (OKRs) and flow metrics; low-dependency team design (descaled); hybrid governance satisfies oversight without slowing delivery; continuous improvement is cultural, not ceremonial.

## Ideas for discussion

1. Score your team against the twelve Agile principles: where are you agile in ceremony but not in substance?
2. Is velocity used on your team as a forecast or as a target, and what has that done to behavior?
3. Which XP technical practices are missing, and how is their absence showing up as defects or slow change?
4. Before adopting a scaling framework, could you reduce cross-team dependencies instead?
5. In your context, what specifically blocks real user access each iteration, and how could you remove it?
6. What was the last concrete change a retrospective actually produced?

## Key takeaways

- Agile is a **mindset of values and principles**, not a set of ceremonies; frameworks are starting points, not the goal.
- Deliver **working software frequently**, welcome change, and empower **self-organizing teams**.
- **Technical excellence (XP practices) is non-negotiable.** Agility without it becomes fast decay.
- **Scale with care; prefer descaling.** Reduce dependencies before adding coordination frameworks.
- In enterprise/government, combine **adaptive delivery with hybrid governance and agile procurement**, and fight for real user access.
- The ROI is **continuous risk reduction and earlier value**, but only when Agile is real, not ritual. See chapters 1.4, 11.1, 11.2, 10.6, and 11.3.

## References and further reading

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
