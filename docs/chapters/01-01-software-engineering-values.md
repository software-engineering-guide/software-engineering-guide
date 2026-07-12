# 1.1 Software engineering values

## Overview and motivation

[Software engineering](https://en.wikipedia.org/wiki/Software_engineering) values are the shared beliefs, norms, and everyday behaviours that shape how people build software together. They are not the posters on the wall or the words in the employee handbook. They are what actually happens when an incident wakes someone at 3 a.m., or when a junior engineer disagrees with a principal engineer, or when a deadline collides with quality. Values are the invisible system beneath every technical decision.

In a small team, values spread by osmosis: people sit together, absorb the norms, and self-correct. In a larger team, osmosis fails. Now you have to make values explicit, write them down, have leaders model them, and reinforce them through your systems. Skip that, and the culture fragments into dozens of incompatible micro-cultures that quietly tax every collaboration.

For a larger team, the stakes are structural. Weak values show up as attrition, slow decisions, hoarded knowledge, and repeated incidents whose root causes are never fully fixed. Strong values show up as fast, safe, reliable changes: engineers surface problems early, learn from failure, and take ownership. The gap between these two states is often wider than any technology choice.

Enterprises and government organizations feel this acutely, because they work at scale, under scrutiny, and over long timelines. Systems built today may run for a decade or more, staffed by people who never met the original authors. In these settings, culture is what carries intent across time and turnover.

Regulated enterprises face one more pressure: the temptation to substitute process for trust. When accountability is high and mistakes are visible, the reflex is to pile on controls, sign-offs, and blame. It is understandable, but it backfires. The most reliable, secure, and compliant organizations are usually the ones with the strongest learning cultures, not the most punitive ones. Values and compliance are allies, not opposites.

## Key principles

- [Psychological safety](https://en.wikipedia.org/wiki/Psychological_safety) is the foundation; without it, every other practice degrades.
- Failure is data. Blameless learning turns incidents into durable improvement.
- Ownership means accountability for outcomes, not just outputs: "you build it, you run it."
- Writing is thinking. A culture that writes decisions down scales its judgment.
- Sustainable pace beats heroics; [burnout](https://en.wikipedia.org/wiki/Occupational_burnout) is a systems failure, not a personal one.
- [Diversity, equity, and inclusion](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) are engineering strengths that improve decision quality.
- Values are modelled top-down and reinforced bottom-up; leaders' actions outweigh their words.

## Recommendations

### Build psychological safety deliberately

Psychological safety is the shared belief that you can speak up, ask questions, admit mistakes, and challenge decisions without fear of humiliation or punishment. It is the single strongest predictor of team effectiveness in large-scale studies. Build it deliberately. Have leaders own their own mistakes out loud ("here is a mistake I made and what I learned"). Meet bad news with curiosity rather than punishment. Invite dissent openly in meetings. Rotate who speaks first, so senior voices do not anchor the discussion. And make it normal to say "I don't know" and "I need help."

### Practice blameless learning

When something breaks, look at the conditions that allowed the failure, not the person who triggered it. Adopt blameless [postmortems](https://en.wikipedia.org/wiki/Postmortem_documentation): a written record of what happened, the timeline, the contributing factors, and concrete action items with owners and dates. Start from the assumption that everyone acted reasonably given what they knew at the time. Ask "what made this easy to get wrong?" instead of "who messed up?" And track action items to completion. A postmortem culture that never closes its follow-ups is just theatre.

### Establish clear ownership models

"You build it, you run it" makes the team that writes a service responsible for operating it, on-call included. This tightens the feedback loop between design decisions and operational pain, and that improves quality. Pair it with a service catalogue that records, for every system, who owns it, how to reach them, its dependencies, and its runbooks. Keep ownership explicit and non-overlapping. Ambiguous ownership is how systems rot and incidents linger. When a team genuinely cannot operate a system on its own, give it platform support rather than diffusing accountability.

### Cultivate a writing culture

Writing sharpens your thinking, and it creates artifacts that carry across time zones and years. Make design docs and decision records routine for significant changes: a short document that states the problem, the options considered, the proposed approach, and the trade-offs, circulated for comment before you build. This surfaces disagreement early, while it is still cheap, and it leaves a durable record of why you decided what you did. Keep templates lightweight and expectations in proportion to the decision's weight. And reward good writing in public.

### Protect sustainable pace

Hero culture, where a few people repeatedly rescue the organization through unsustainable effort, is a symptom of weakness, not a virtue. It burns people out, concentrates knowledge dangerously, and hides the underlying problems you should be fixing. So measure and manage on-call load. If one person is paged constantly, treat that as a defect to engineer away. Make time off normal, protect focus time, and judge output over a quarter rather than a week.

### Treat DEI as an engineering strength

Diverse teams make better decisions. They weigh more perspectives and fall for [groupthink](https://en.wikipedia.org/wiki/Groupthink) and blind spots less often, and that matters enormously for accessibility, security, and serving broad populations. Build inclusion into your everyday engineering: accessible documentation, inclusive language in code and interfaces, meeting practices that let quieter voices contribute, and a fair split of both the glamour work and the glue work.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
| --- | --- | --- |
| Blameless postmortems | Surfaces real root causes; builds trust; drives systemic fixes | Can feel like "no accountability" to outsiders; requires discipline to close actions |
| "You build it, you run it" | Tight quality feedback loop; clear ownership | On-call burden; needs strong platform support to avoid burnout |
| Docs-first / RFC culture | Durable decisions; scales across turnover; async-friendly | Slower for trivial changes; risks bureaucracy if over-applied |
| Sustainable pace | Retention, reliability, long-term velocity | Feels slower during crunch; requires leadership to hold the line |

The central tension is short-term speed versus long-term health. Heroics and blame buy a burst of apparent control, then a slow collapse in morale and reliability. Blameless learning, ownership, and sustainable pace feel slower in any single week, but they compound into far higher velocity over quarters and years. Leaders have to be willing to absorb the short-term discomfort to protect long-term capacity.

## Questions to discuss with your team

1. **How do you keep "blameless" from reading as "no accountability" to auditors, executives, and the public?** In a regulated enterprise or a government agency under oversight, a postmortem that names no culprit can look like a cover-up to people outside engineering. The competing considerations are real: you need the honesty that only blamelessness produces, and you also need decision-makers to trust that failures get addressed. Bring concrete evidence to the discussion, such as your incident recurrence rate and the completion rate of postmortem action items, because a system that reliably closes its follow-ups is visibly accountable even without a scapegoat. Separate two questions that blame culture fuses together: what made this easy to get wrong, and did anyone act with genuine negligence or bad faith. If your answer is that accountability lives in fixing the conditions and closing the actions, then publish that mechanism so outsiders can see the accountability they are looking for.

2. **Which teams are carrying on-call systems they cannot realistically operate, and who pays for that gap?** "You build it, you run it" tightens the feedback loop, and it assumes a team has the platform support to run what it built. At enterprise and government scale, some teams inherit legacy systems, vendor black boxes, or cross-cutting infrastructure that no small team can genuinely own alone. The trade-off sits between diffusing accountability (bad) and setting a team up to fail on a pager it cannot answer (also bad). Bring the paging data: if one person or one team is paged constantly, treat that as a defect to engineer away, not a badge of honour. The answer should tell you where to invest in platform teams, staged rollouts, and current runbooks, so ownership stays clear while the operational burden stays humane.

3. **Do the behaviours you actually promote for match the values you publish?** Values decay into cynicism the moment leaders reward what the posters condemn, and at scale this gap stays invisible until attrition and quiet knowledge-hoarding reveal it. Look hard at your last promotion cycle: did it reward firefighting and heroics, or fire prevention and the glue work that keeps a large team healthy? Enterprises and government bodies compound the risk, because rigid grade systems and long tenures let a mismatched incentive run for years before anyone corrects it. Bring real evidence, such as who got promoted, who was praised in public, and what those people actually did. If heroics get the rewards, you are training your organization to manufacture the crises it then celebrates solving, and the fix is to change the incentives, not the wall art.

4. **How would you actually know whether psychological safety is high or low on a given team, rather than assuming it from the org chart?** Safety is the foundation every other practice rests on, and it is also the easiest thing to fool yourself about, because the teams with the least of it are the ones least likely to tell you. At scale the average across a thousand people hides the variance that matters: one manager can quietly run a fear-based team inside an otherwise healthy organization. The competing considerations are candor versus comfort, since the survey questions that reveal real problems are the ones people are most reluctant to answer honestly, and gathering the signal can itself feel unsafe. Bring concrete evidence rather than vibes: team-level results from a validated safety instrument, the rate at which people admit mistakes in writing, near-miss reports that surfaced before they became incidents, and exit-interview themes. For an enterprise or government body, insist the data stays team-level and is never used to punish a low-scoring team, because the moment a safety score becomes a stick, it stops measuring safety and starts measuring fear of the measurement.

5. **What is your real on-call and heroics load, and are you rewarding the people who prevent fires or the ones who fight them?** Sustainable pace is where good intentions quietly collapse under delivery pressure, and a large organization can run on the invisible overtime of a few exhausted people for years before it notices. The tension is honest: heroics genuinely rescue you in the moment, and depending on them concentrates knowledge, hides systemic defects, and burns out your most committed engineers. Bring the operational data to the discussion: pages per person per week, after-hours deploys, the distribution of on-call load across the team, and how much of it lands on the same few names month after month. Look, too, at who your last promotion cycle rewarded. In enterprises and government agencies with rigid grade ladders and long tenures, a culture that pays for firefighting can persist unchallenged for a decade, so the answer should tell you where to engineer the pager down and how to make fire prevention a visibly promotable act.

6. **Which significant decisions from the past two years have no written record of their reasoning, and what will that cost when the authors are gone?** A writing culture is what carries intent across turnover, and its absence is invisible right up until the moment someone needs to change a system nobody understands anymore. The competing pull is speed: writing a design doc or decision record feels like friction in the moment, and over-applied it curdles into bureaucracy that slows trivial changes. Bring evidence to calibrate it: the share of consequential changes that have a design doc or decision record, how often people can actually find and cite the reasoning behind an existing architecture, and how long a new engineer takes to become productive on an undocumented service. For enterprises and government organizations whose systems outlive the tenure of everyone who built them, and which may face audit or freedom-of-information scrutiny, the written record is both institutional memory and evidence of due diligence, so the answer should draw the line where the decision's weight justifies the writing and no lower.

## Sector lens

**Startup.** Values still spread by osmosis, so do not import heavy process, but do name the one or two behaviours that matter most, usually blameless honesty about mistakes and a bias to surface bad news early. The founders set the tone by owning their own errors out loud, because in a tiny team a single sharp reaction in Slack can teach everyone to hide problems for months. Your scarce runway is a reason to protect safety, not skip it: a team that hides bugs is far more expensive than a five-minute retro.

**Small business.** With no dedicated engineering-culture specialist and a tight budget, lean on lightweight rituals rather than tooling you have to buy or staff. A shared incident channel, a one-page decision log, and a habit of "what made this easy to get wrong?" cost nothing and carry most of the value. Be deliberate about the buy-versus-build line for practices too: adopt an off-the-shelf postmortem template and a simple on-call rota instead of building a bespoke system you cannot maintain.

**Enterprise.** At scale the job is consistency without uniformity: blameless learning, clear non-overlapping ownership, and a writing culture become org-wide norms with tooling, expectations, and a service catalogue behind them. Governance and audit push you toward controls, so make the case that a strong learning culture is the most reliable and compliant option, and show it with incident-recurrence and action-item-closure metrics. Watch the variance between teams, because averages hide the fear-based pockets that quietly leak talent and knowledge.

**Government.** Procurement rules, transparency obligations, and public accountability shape how values are expressed, especially around blame. A postmortem that names no culprit can read as a cover-up to outside oversight, so publish the mechanism, showing that accountability lives in fixing conditions and closing actions, and let citizens and auditors see it. Because systems outlive administrations and staff turnover is measured in years, treat written decision records as both institutional memory and evidence of due diligence under freedom-of-information scrutiny.

## Examples

**Startup.** A six-person startup runs on trust and hallway conversation, so no one writes the team's values down. When a founder-engineer pushes a bad migration and the CTO snaps at them in Slack, the room goes quiet, and the next two bugs get quietly hidden rather than surfaced. The team recovers by adopting one lightweight habit: a five-minute blameless "what made this easy to get wrong?" chat after each incident, no template required. That small ritual keeps the osmotic culture healthy without the process overhead a larger organization would need.

**Enterprise.** A large financial-services firm suffered a major outage when a routine configuration change cascaded across services. In a blame culture, the engineer who pushed the change would have been reprimanded, and that would be the end of it. Instead, a blameless postmortem showed that the deployment tooling made the dangerous change look identical to a safe one, that no staged rollout existed, and that the runbook was outdated. The firm invested in progressive rollouts and configuration validation, and similar changes now fail safely. Choosing to look at the system rather than the person produced a durable engineering improvement.

**Government.** A government digital service agency adopted "you build it, you run it" alongside a strict docs-first [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments) process. Because its systems have to survive changes in political administration and staff turnover measured in years, every significant decision is recorded in a design doc that explains the context and trade-offs. New engineers, and incoming contractors, can read the reasoning behind a decade-old architecture instead of reverse-engineering it. That written [institutional memory](https://en.wikipedia.org/wiki/Institutional_memory) is what lets the agency keep public services reliable despite high turnover and strict accountability requirements.

## Business case: motivations, ROI, and TCO

The return on culture is real but indirect, which is why it is chronically underfunded. Over a system's lifetime, the dominant cost is not building it. It is maintenance, incident response, rework, and the cost of losing and re-hiring skilled people. A strong learning culture improves every one of these. Blameless postmortems reduce repeat incidents. Clear ownership reduces mean time to recovery. A writing culture lowers the cost of [onboarding](https://en.wikipedia.org/wiki/Onboarding) and the cost of decisions made in ignorance of the reasoning that came before.

Take attrition alone. Replacing a mid-level engineer typically costs somewhere between half and two times their annual salary once you count recruiting, ramp-up, and the institutional knowledge that walks out the door. If a healthier culture trims regretted attrition by even a few percentage points across a thousand-person organization, the savings dwarf the modest cost of running postmortems and writing docs. The adoption cost is mostly leadership attention and a little process overhead. The cost of not adopting is paid continuously and invisibly: slower delivery, recurring incidents, and quiet talent flight.

To make the case to leadership, connect culture to metrics executives already track: delivery lead time, change failure rate, mean time to recovery, incident recurrence, and regretted attrition. Frame psychological safety not as a soft benefit but as the mechanism that makes every other engineering investment pay off, because unsafe teams hide the very problems those investments are meant to fix.

## Anti-patterns and pitfalls

- Blame-and-shame incident reviews: they drive problems underground and people stop reporting.
- Hero worship: rewarding firefighting over fire prevention perpetuates the fires.
- "Values" that leaders violate: stated values contradicted by behaviour breed cynicism.
- Ownership without support: assigning on-call for systems teams cannot realistically operate.
- Process as trust substitute: piling on sign-offs instead of building genuine safety.
- Docs theatre: writing documents no one reads or that never influence decisions.
- Inclusion as a checkbox: hiring for diversity while excluding those same voices from decisions.

## Maturity model

- Level 1, Initiate: Values are accidental and personality-driven. Incidents mean blame, knowledge lives in a few heads, and heroics are how things get done. Nobody has written down what the team believes or how it behaves under pressure.
- Level 2, Develop: A few teams start blameless postmortems, write the occasional design doc, and talk about ownership, but the practices are inconsistent, unevenly applied, and not yet reinforced by leadership. Whether you land on a healthy team is mostly luck.
- Level 3, Standardize: Blameless learning, clear non-overlapping ownership, and a writing culture are documented org-wide norms with templates, a service catalogue, and defined on-call expectations. Leaders model the values and the same behaviours are expected everywhere, not just where a good manager happens to sit.
- Level 4, Manage: The culture is measured against baselines and controlled with data. You track team-level psychological-safety scores, incident recurrence, postmortem action-item closure rate, on-call load distribution, mean time to recovery, and regretted attrition, and you act on the numbers when a team drifts. Kill firefighting incentives on evidence, and reward fire prevention because you can now see it.
- Level 5, Orchestrate: Culture is continuously improved and integrated with how the whole organization plans, hires, and promotes. Safety is high, learning is fast, and practices adapt as evidence and context change. The organization rebalances on-call load, refreshes decision records, and evolves its norms deliberately rather than waiting for a crisis to force the issue.

## Ideas for discussion

- Where in our organization do people not feel safe to say "I don't know" or "I disagree," and why?
- Do our incident reviews change the system, or just assign fault and move on?
- Are we rewarding heroics that we should be engineering away?
- Which important decisions from the past two years have no written record of their reasoning?
- How evenly is glue work and on-call load distributed across the team?
- Do our stated values match what actually gets people promoted here?

## Key takeaways

- Values are the invisible operating system behind every technical decision; at scale, values must be explicit.
- Psychological safety is foundational; without it, other practices decay.
- Blameless learning converts failure into durable systemic improvement.
- Clear ownership ("you build it, you run it") tightens the quality feedback loop.
- Writing culture scales judgment across time zones and turnover.
- Sustainable pace and inclusion are long-term velocity multipliers, not costs.

## References and further reading

- Amy C. Edmondson, "The Fearless Organization" and "Teaming"
- Google re:Work / Project Aristotle research on team effectiveness
- Sidney Dekker, "The Field Guide to Understanding 'Human Error'"
- John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate: The Science of Lean Software and DevOps"
- Gene Kim et al., "The Phoenix Project" and "The DevOps Handbook"
- Camille Fournier, "The Manager's Path"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Tom DeMarco and Timothy Lister, "Peopleware: Productive Projects and Teams"
