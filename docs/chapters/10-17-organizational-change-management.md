# 10.17 Organizational change management

## Overview and motivation

[Change management](https://en.wikipedia.org/wiki/Change_management) is the discipline of helping people adopt new ways of working. Note the emphasis: people. It is not the technical change itself, the new platform, the reorganization, the migration to trunk-based development. It is the human half of that work, the part that decides whether the shiny new thing you shipped actually gets used, or quietly rots while everyone keeps doing what they did before. You can deploy a tool in an afternoon. Getting a thousand engineers to change a habit takes months, and it does not happen by accident.

This matters for large teams because scale multiplies the human cost of change. A five-person startup can change direction over lunch. A five-thousand-person enterprise cannot, and yet it changes constantly: new architectures, new compliance regimes, new operating models, new leaders with new priorities. Most of these efforts underdeliver, and the reason is rarely the technology. It is resistance that was never surfaced, communication that never landed, sponsorship that evaporated, and reinforcement that never came, so people drifted back to the old way the moment attention moved on. If you lead technical change and ignore the human side, you are gambling your budget on hope.

Enterprise and government settings raise the stakes further. A large enterprise may run dozens of transformation programs at once, saturating its people with change until they stop responding to any of it. Government adds constraints that private firms rarely face: leadership turns over with political cycles, procurement rules limit how fast you can buy or build, unionized workforces have negotiated protections around how work changes, and every misstep is subject to public accountability. In all these settings, treating change management as a real discipline, with its own plan, owners, and metrics, separates a transformation that sticks from an expensive announcement that fades.

## Key principles

- **Change the people, not just the system.** Deployment is not adoption. The work is done when behavior changes.
- **Lead change and manage it.** Vision and energy get people moving; plans and reinforcement get them to stay.
- **Sponsorship is oxygen.** A change without a committed, senior sponsor dies quietly, every time.
- **Explain the why before the what.** People adopt changes they understand and resist changes imposed on them.
- **Roll out incrementally, measure adoption.** Pilot, learn, expand. Track use, not just release.
- **Reinforce or revert.** Without follow-through, people return to the old way. Sustaining is the hard part.
- **Culture is the deepest layer.** Structure and process change faster than beliefs; plan for that.

## Recommendations

### Treat adoption, not deployment, as the finish line

The single most common failure in technical change is declaring victory at go-live. The tool is installed, the announcement is sent, the program is marked green, and everyone moves on. Six months later, half the teams are still on the old workflow and the promised benefits never materialized. The problem is that deployment is an event and adoption is a process. Define your success in terms of behavior: what will people actually do differently, how many of them, and by when. If you are rolling out a new deployment pipeline, the goal is not "the pipeline exists," it is "eighty percent of services deploy through it, and mean lead time has dropped." Write that down before you start.

This reframing connects directly to how you measure. Deployment metrics (installed, rolled out, licensed) are easy and misleading. Adoption metrics (active users, workflows migrated, old paths retired) tell you the truth. Relate change outcomes to the discovery-to-delivery flow in chapter 11.1 so you can see whether the change actually moved the results it promised, rather than merely happening.

### Build a guiding coalition and secure real sponsorship

No meaningful change survives on the enthusiasm of one champion. You need a coalition: a group with enough authority, credibility, and cross-functional reach to carry the change through the parts of the organization that will resist it. This idea sits at the center of the change model popularized by [John Kotter](https://en.wikipedia.org/wiki/John_Kotter), whose eight-step framework opens with establishing urgency and building a guiding coalition precisely because lone reformers get isolated and overruled.

Sponsorship is the part people underinvest in most. A sponsor is a senior leader who visibly wants the change, spends their own political capital on it, removes obstacles, and keeps showing up after the launch. A sponsor who lends their name to a kickoff email and then disappears is worse than no sponsor, because their silence signals that the change does not really matter. Before you start, name your sponsor, get a concrete commitment about what they will do and for how long, and have a plan for what happens if they leave, which in high-turnover settings you should assume will happen.

### Communicate a compelling "why," repeatedly

People do not resist change so much as they resist being changed without explanation. The most reliable way to lower resistance is to make the reason for the change genuinely understood, not just announced. This is the "A" and "D" of the ADKAR model, which frames individual change as a sequence: Awareness of why, Desire to participate, Knowledge of how, Ability to do it, and Reinforcement to sustain it. The order matters. If you jump to training people (Knowledge) before they understand why the change helps them (Awareness and Desire), the training does not stick.

Communicate the why more times than feels necessary. People need to hear a message many times, through several channels, before they believe it is real and permanent. Say it in all-hands meetings, in standups, in writing, and, above all, through the visible behavior of leaders. Address "what does this mean for me" directly and honestly, including the parts people will not like. A change communication that only lists benefits and hides costs teaches people not to trust the next one.

### Roll out incrementally, and pilot before you scale

Big-bang rollouts, everyone switches on the same day, are seductive and dangerous. They concentrate all the risk into a single moment, give you no chance to learn, and leave no fallback when something breaks. Prefer incremental rollout: pilot with a few willing teams, learn what goes wrong, fix it, and expand in waves. Each wave gives you evidence, reference customers inside your own walls, and a growing base of people who can help the next group. This is the practical backbone of an adoption roadmap, covered in chapter 12.6, and it pairs naturally with the maturity-model thinking in chapter 10.8: you are moving groups up a ladder deliberately, not flipping a switch.

Piloting also protects your credibility. The first wave will surface problems you did not anticipate, and it is far better to hit them with fifty friendly users than five thousand skeptical ones. Choose early pilots for their willingness and influence, so their success becomes a story the next wave believes.

### Reinforce and sustain, or watch it revert

The hardest and most neglected phase of change is the one after launch, when attention naturally drifts to the next initiative. Without reinforcement, people revert. The old workflow is still in muscle memory, the new one is still effortful, and the path of least resistance pulls them back. The classic model associated with social psychologist [Kurt Lewin](https://en.wikipedia.org/wiki/Kurt_Lewin) captures this as three phases: unfreeze the current way, change to the new way, and refreeze so the new way becomes the default. Most organizations do the first two and skip the third.

Refreezing is concrete work. Retire the old path so it is no longer an option (this is often the most effective single lever). Bake the new behavior into onboarding, defaults, checklists, and tooling so newcomers never learn the old way. Celebrate and make visible the teams that have adopted well. Keep measuring adoption for months after launch, and treat a decline as a live problem to fix, not a settled matter. Change that is not reinforced is change you will pay for twice.

### Align structure and culture to the change

Two deeper layers determine whether a change can hold. The first is structure. If you ask teams to work in a new way but leave the reporting lines, incentives, and team boundaries that produced the old way, the structure will win. The idea captured by [Conway's law](https://en.wikipedia.org/wiki/Conway%27s_law), that systems mirror the communication structures of the organizations that build them, cuts both ways: to change how software is built, you often have to change how teams are drawn, a topic developed in chapter 1.2. The second and deepest layer is [organizational culture](https://en.wikipedia.org/wiki/Organizational_culture), the shared assumptions and values that chapter 1.1 addresses. Culture changes slowest of all, because it lives in what people believe rather than what they are told. You cannot mandate it; you shift it by changing what leaders reward, tolerate, and model, and then waiting. Plan your timeline accordingly: process in weeks, structure in months, culture in years.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Big-bang rollout** | Fast; single cutover; no dual-running cost | Concentrated risk; no learning loop; hard to reverse |
| **Incremental rollout** | Learns as it goes; contains risk; builds internal advocates | Slower; dual-running overhead; change can stall mid-way |
| **Following a named model (Kotter, ADKAR, Lewin) closely** | Shared vocabulary; nothing forgotten; credible to stakeholders | Ritual over substance; false confidence; poor fit if applied rigidly |
| **Pragmatic, model-informed approach** | Fits your context; focuses energy where it matters | Requires judgment; easy to skip inconvenient steps |
| **Dedicated change-management function** | Consistency; capacity; guards against change saturation | Overhead; can become a box-ticking gate; distance from the work |

The central tension is between speed and stickiness. Big-bang rollouts and skipped reinforcement feel fast because they compress the visible work, but they push cost into the future as failed adoption and rework. Incremental rollout with real reinforcement feels slow because you pay the cost up front, in pilots, communication, and follow-through, and it is the only reliable way to make change hold. Resolve the tension by front-loading the human work deliberately: budget for it, staff it, and measure adoption long after the launch you were tempted to call the end. Use named models as a checklist against forgetting, not as a script to perform.

## Questions to discuss with your team

1. **How will we know this change was adopted, not just deployed, and who is watching that metric six months from now?** Most teams can tell you the launch date and almost none can tell you the adoption curve a quarter later. Before you start, agree on the specific behavior that counts as success, the metric that captures it, and the person responsible for tracking it well past go-live. Bring your last three significant changes to the discussion and ask honestly what fraction of the intended audience actually changed their behavior and still does. If you cannot answer that for past changes, you have been measuring deployment and calling it adoption. The answer should reshape how you define "done" for the current effort and who stays accountable after the celebration.

2. **Who is the committed sponsor for this change, what exactly have they agreed to do, and what happens if they leave?** Sponsorship is the strongest single predictor of whether change sticks, and it is the thing teams most often assume rather than secure. Get specific: a sponsor is not a name on a slide, it is a senior leader spending political capital, clearing obstacles, and showing up repeatedly after launch. In organizations with frequent leadership turnover, especially government across political cycles, you must plan for the sponsor to change mid-flight and build a coalition broad enough to survive it. Bring the actual commitment to the meeting, in writing if you can, and stress-test it: what happens to this change if that person is reassigned next quarter? If the honest answer is that it collapses, you have a single point of failure to fix now.

3. **How many changes are we asking these same people to absorb at once, and are we past the point of change saturation?** Every initiative competes for the same finite attention and goodwill, and large organizations routinely run so many at once that people stop responding to any of them. This is change fatigue, and it is the reason a perfectly good change can fail for reasons that have nothing to do with its merits. Inventory every significant change currently landing on the teams in question, not just yours, and count them from the receiving end. Bring evidence of how the last few changes were received, whether people are engaged or quietly waiting for the latest thing to pass. If the teams are saturated, the right move may be to sequence, pause, or consolidate rather than to communicate harder.

## Examples

**Startup.** A forty-person startup decides to move from ad hoc deploys to a standardized continuous delivery pipeline. Rather than mandating it, the two most respected engineers pilot it on their own services for two weeks, fix the rough edges, and demo the halved deploy time at the all-hands. The founder (the sponsor) publicly commits that all new services will use the pipeline and that the old scripts will be deleted in ninety days. Adoption spreads by envy and deadline rather than decree, and because the old path is genuinely retired, nobody drifts back. The whole "change management" effort is lightweight and mostly informal, which is exactly right at that size.

**Enterprise.** A financial-services firm with three thousand engineers launches a platform migration alongside four other transformation programs. A small central change-management function notices the teams are saturated and sequences the programs instead of running them in parallel, giving each a clear window. For the migration itself, they name an executive sponsor, build a coalition of engineering directors, communicate the "why" (regulatory risk and cost) repeatedly, and roll out in waves of ten teams. They track workflows migrated and old systems decommissioned, not licenses purchased, and they keep reporting the adoption curve for a year. The programs that were sequenced land; an earlier one that was run big-bang and never reinforced had quietly reverted.

**Government.** A national agency modernizes a decades-old case-management system used by a unionized workforce. Change here is bounded by realities a startup never sees: procurement rules dictate the pace of buying, union agreements govern how job roles can change and require genuine consultation, and the whole program is accountable to the public and to auditors. The team engages the union early as part of the coalition rather than presenting a finished plan, phases the rollout region by region to respect training and staffing constraints, and documents adoption for public accountability. Crucially, they design the change to survive a leadership transition, embedding it in standard operating procedures and civil-service roles rather than resting it on one appointed official who may leave after the next election.

## Business case: motivations, ROI, and TCO

The business case for change management is uncomfortable because its return shows up as an avoided loss rather than a visible gain. Consider the denominator most leaders never compute: the money already spent on tools, platforms, and reorganizations that were deployed and never adopted. That is pure waste, and it is enormous in large organizations. Change management converts that spend into realized value. The return on investment is straightforward: a modest, deliberate investment in sponsorship, communication, piloting, and reinforcement dramatically raises the probability that the far larger technical investment pays off. Spending ten percent more to make the other ninety percent land is obviously worthwhile, yet it is routinely cut first.

On total cost of ownership, the honest accounting includes the human costs that rarely appear in a budget: the productivity dip during transition, the dual-running period when both old and new systems operate, the training, and the ongoing reinforcement. These are real and should be planned, but they are dwarfed by the cost of failed adoption: the wasted capital investment, the rework, and the corrosive effect on trust, because every failed change makes the next one harder to sell. To make the case to leadership, reframe the choice: the question is not whether to spend on change management, it is whether to protect the value of a much larger investment or to gamble it on hope. Show them the graveyard of past deployments that were never adopted, and the case makes itself.

## Anti-patterns and pitfalls

- **Declaring victory at go-live:** treating deployment as the finish line, so adoption is never driven or measured, and the change quietly fails.
- **Sponsor in name only:** a senior leader who lends their name to the kickoff and then disappears, signaling that the change does not really matter.
- **Big-bang everything:** switching everyone at once, concentrating all risk into one moment with no learning loop and no fallback.
- **All benefits, no costs:** communication that only sells the upside, which teaches people not to trust the next announcement.
- **Change saturation:** stacking so many initiatives on the same people that they stop responding to any of them, then blaming resistance.
- **Skipping the refreeze:** launching and moving on without retiring the old path or embedding the new one, so people revert.
- **Model as ritual:** performing the eight steps or the five ADKAR letters as a ceremony while missing the substance underneath.
- **Ignoring structure and culture:** asking for new behavior while leaving the incentives, team boundaries, and beliefs that produced the old behavior intact.

## Maturity model

- **Level 1, Initial:** Change is technical only. New tools and reorganizations are announced and deployed; adoption is assumed and unmeasured; failed changes are blamed on resistant people. There is no sponsor role, no communication plan, and no reinforcement.
- **Level 2, Managed:** Some changes get a sponsor and a communication plan. Rollouts are occasionally piloted rather than big-bang. Adoption is tracked informally for high-profile efforts, but reinforcement is weak and reversion is common. Change saturation is not managed.
- **Level 3, Defined:** A consistent approach exists, informed by established models but applied pragmatically. Significant changes require a named sponsor and coalition, a clear "why," incremental rollout, and adoption metrics. Reinforcement is planned. The portfolio of concurrent changes is visible and sequenced.
- **Level 4, Optimizing:** Change capability is an organizational strength. Adoption is measured and reinforced long after launch; change saturation is actively managed across the portfolio; structure and culture are treated as part of the change; sponsorship survives leadership turnover; and lessons from each change improve the next.

## Ideas for discussion

1. Look at your last five significant changes. How many were genuinely adopted, and how would you even know? What does the honest number tell you about your default definition of "done"?
2. Where in your organization is change fatigue highest right now, and what would it take to pause or consolidate rather than add another initiative?
3. Which named model, if any, fits your culture best, and are you using it as a checklist against forgetting or performing it as a ritual?
4. When a sponsor leaves mid-change, what happens? Is any current change resting on a single point of failure you should broaden now?
5. What old paths are you still leaving open that let people revert, and what would it cost to retire them for good?
6. How long after a launch do you keep measuring adoption, and what would change if you doubled that window?

## Key takeaways

- Change management is about people adopting new ways of working, distinct from the technical change itself; deployment is not adoption.
- Change efforts fail from predictable human causes: absent sponsorship, unexplained "why," big-bang risk, change saturation, and missing reinforcement, rarely from the technology.
- Use established models (Kotter, ADKAR, Lewin) pragmatically, as a checklist against forgetting, not a ritual to perform.
- Build a coalition, secure a committed sponsor, communicate the why repeatedly, roll out incrementally (chapter 12.6), and measure adoption, not just deployment (chapter 11.1).
- Reinforce relentlessly or watch teams revert; retire the old path and embed the new one in defaults.
- Align structure (chapter 1.2) and culture (chapter 1.1) to the change; culture is the slowest layer and cannot be mandated.
- In enterprise, manage the whole portfolio to avoid change saturation; in government, design change to survive political cycles, procurement limits, and union consultation.

## References and further reading

- John P. Kotter, *Leading Change*.
- John P. Kotter, "Leading Change: Why Transformation Efforts Fail," *Harvard Business Review*.
- Jeff Hiatt, *ADKAR: A Model for Change in Business, Government and Our Community* (Prosci).
- Kurt Lewin, *Field Theory in Social Science*.
- Chip Heath and Dan Heath, *Switch: How to Change Things When Change Is Hard*.
- William Bridges, *Managing Transitions: Making the Most of Change*.
- Everett M. Rogers, *Diffusion of Innovations*.
- Edgar H. Schein, *Organizational Culture and Leadership*.
- Todd Jick and Maury Peiperl, *Managing Change: Cases and Concepts*.
