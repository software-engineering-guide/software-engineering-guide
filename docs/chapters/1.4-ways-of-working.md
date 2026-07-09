# 1.4 Ways of working

## Overview and motivation

"Ways of working" describes how your team actually coordinates, plans, communicates, and delivers day to day. How is work broken down? Who talks to whom, and when? How is progress tracked, and how do decisions and knowledge flow?

Most organizations adopt a named methodology, [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), some scaling framework, and assume the ceremonies are the same as the value underneath. They are not. The methodologies that transformed software delivery were reactions against heavyweight, hand-off-driven processes. Their goal was fast feedback, small batches, and empowered teams. Adopt only the rituals, standups, sprints, story points, without the principles, and you get the costs of process without the benefits: [cargo-cult](https://en.wikipedia.org/wiki/Cargo_cult) agile.

For large teams, this is where good intentions succeed or fail. A thousand engineers cannot all be in the same room, attend the same meeting, or share the same tacit context. The larger you get, the more you must lean on written communication, asynchronous collaboration, and lightweight coordination rather than meetings and hallway chats. Scale changes the physics. Practices that work beautifully for eight co-located people can collapse for eighty distributed people. And scaling frameworks that promise to fix this often reintroduce the very hand-offs and centralization that [agile](https://en.wikipedia.org/wiki/Agile_software_development) was meant to remove.

Enterprises and government feel every one of these pressures at full force. They span many time zones, blend permanent staff with contractors and vendors, and often carry mandated stage gates and reporting. Here, a docs-first, asynchronous, outcome-focused way of working is not a nicety. It is the only thing that scales. The recommendations below favor adapting principles to context over importing frameworks wholesale, and favor written, asynchronous, transparent practices that let large, distributed, mixed workforces truly collaborate.

## Key principles

- Adopt principles, not rituals; understand why a practice exists before you copy it.
- Small batches and fast feedback beat large plans and long cycles.
- Prefer flow (limiting work in progress) over rigid time-boxing where it fits.
- Estimate to enable conversation and planning, not to manufacture false precision.
- Default to asynchronous, written communication; reserve synchronous time for what truly needs it.
- Make work and decisions visible and documented so anyone can catch up without a meeting.
- Optimize for outcomes delivered, not activity performed or capacity utilized.

## Recommendations

### Adapt Agile, Scrum, Kanban, and Lean to context

Treat these as a toolkit, not a religion. Scrum's time-boxed sprints suit teams with discovery work that benefits from a regular planning and review cadence. Kanban's continuous flow and explicit work-in-progress limits suit teams with unpredictable, interrupt-driven work such as platform and operations. [Lean](https://en.wikipedia.org/wiki/Lean_software_development)'s focus on eliminating waste and shortening lead time underpins both. Choose deliberately. Mix where it helps; many teams run "[Scrumban](https://en.wikipedia.org/wiki/Scrumban)." Keep the practices that create value, and drop the ceremonies that have become empty ritual. The test for any practice is simple. Does it shorten feedback, reduce batch size, or increase clarity? If not, question it.

### Scale with caution, not cargo cult

Scaling frameworks, [SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), LeSS (Large-Scale Scrum), the popularized "Spotify model," promise to coordinate many teams. Approach them with a skeptical eye. SAFe brings structure and is often chosen by large enterprises and government for its comprehensiveness and training ecosystem, but it can reintroduce heavy planning, hierarchy, and hand-offs that undercut agility. LeSS stays closer to lean principles, but demands real organizational change. The Spotify "model" was a snapshot of one company's evolving culture, never a template, and even Spotify did not run it the way people imagine. Prefer to scale by reducing the need for coordination, through the team topologies of the previous chapter, rather than by bolting a coordination framework onto a fragmented structure.

### Estimate honestly and lightly

Story points and velocity help your team plan its own near-term work and talk about relative complexity. They are not a productivity metric, a cross-team currency, or a promise. Never turn velocity into a target: it will be gamed through point inflation. For longer-range forecasting, prefer counting throughput and using historical cycle-time data, which is often more accurate than summing estimates. Many mature teams cut estimation overhead by slicing work into similarly small pieces and simply counting them. Whatever the method, remember that estimates are forecasts under uncertainty, not commitments. Communicate them as ranges.

### Default to asynchronous, docs-first communication

In large, distributed organizations, synchronous meetings do not scale, and they shut out people in other time zones. Make writing the default: design docs, [decision records](https://en.wikipedia.org/wiki/Architectural_decision), written status updates, and thorough tickets that carry enough context to act on without a live conversation. Record and summarize the meetings you cannot avoid. A docs-first culture lets someone in another time zone contribute fully, lets new joiners and contractors onboard by reading, and leaves a durable record. Save synchronous time for genuine collaboration, relationship-building, and quickly clearing up ambiguity. Protect big blocks of focus time from meeting fragmentation.

### Work well across time zones, contractors, and vendors

Distributed and mixed workforces are the norm at scale. Design for "[follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun)," where handoffs are written and complete, not verbal. Set a few overlapping core hours for the synchronous contact you need, and share the pain of inconvenient meeting times fairly rather than always burdening the same region. For contractors and vendors, invest extra in written context, clear interfaces, and shared tooling, because they lack the tacit knowledge your permanent staff accumulate. Bring vendors into the same visible boards and documentation instead of managing them through a separate, opaque channel. Where you can, structure contracts around outcomes rather than hours.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
| --- | --- | --- |
| Agile (stakeholder interactions) | High collaboration and fastest value | Requires trust and flexibility |
| Scrum (time-boxed sprints) | Regular cadence, predictable rhythm, built-in reflection | Ceremony overhead; poor fit for interrupt-driven work |
| Kanban (continuous flow, WIP limits) | Flexible, exposes bottlenecks, good for ops | Less rhythm; needs discipline to limit WIP |
| SAFe / heavy scaling framework | Structure, training, familiar to large orgs and government | Reintroduces hierarchy and hand-offs; can smother agility |
| LeSS / lightweight scaling | Stays close to lean principles | Demands deep organizational change |
| Async / docs-first | Scales across time zones; durable; inclusive | Slower for ambiguous topics; requires writing discipline |

The overarching trade-off is coordination versus autonomy, and structure versus adaptability. More framework and more synchronous coordination buy predictability and alignment, at the cost of speed, overhead, and team empowerment. Less framework buys speed and ownership, at the cost of possible misalignment across many teams. For most large organizations, the best answer is a minimal shared cadence plus strong written practices. That reduces the coordination burden at its source rather than managing it with heavier process.

## Questions to discuss with your team

1. **If leadership wants the predictability a scaling framework promises, how will you give them that without reintroducing the hand-offs agile was meant to remove?** Large enterprises and government programs often mandate SAFe-style big-room planning and stage-gate reporting because oversight bodies demand forecasts and coordination they can see. The competing considerations are genuine: leadership needs predictability and alignment across many teams, and heavy frameworks buy that at the cost of speed, overhead, and the very hand-offs that slow delivery. Bring evidence to the discussion, such as how much of the workweek disappears into planning events and cross-team dependency coordination, and whether those events remove dependencies or merely surface them. The stronger move is to scale by reducing the need to coordinate through team topology, then satisfy reporting from live boards and written interfaces rather than from planning marathons. Decide which coordination is real and which is ceremony, and give leadership the forecast they need from throughput and cycle-time data instead of from a framework's overhead.

2. **What will you actually do to stop velocity from being turned into a cross-team productivity metric?** Story points help a single team plan its own near-term work, and they become worthless the moment they are compared across teams or set as a target, because point inflation is the rational response. In a large organization, the pull to roll velocity up into a dashboard executives compare runs strong, and it quietly corrupts the estimates the teams depend on. Bring the evidence of drift: are points inflating over time, are teams padding estimates, is anyone being ranked by velocity? Prefer counting throughput and using historical cycle-time data for any forecast that leaves the team, and communicate estimates as ranges under uncertainty rather than promises. The answer should produce an explicit agreement that velocity never leaves the team, and that cross-team forecasting uses flow metrics instead.

3. **What is your concrete bar for "written down," and which decisions genuinely still need a synchronous conversation?** A docs-first default is the thing that scales across time zones, contractors, and vendors, and it costs real writing discipline that not everyone has yet. Get specific about the bar: does a ticket carry enough context to act on without a live call, do decisions land in a durable record, are the meetings you cannot avoid recorded and summarized? For enterprises and government programs blending permanent staff with contractors who lack tacit knowledge, the written context is what lets a mixed, distributed workforce contribute fully. The trade-off is that ambiguous or contentious topics are often faster to resolve synchronously, so name those explicitly and reserve scarce synchronous time for them. Decide who bears the cost of building the writing habit and of inconvenient meeting times, and share that cost fairly rather than always burdening the same region.

## Examples

**Startup.** A distributed eight-person startup skips the full Scrum ceremony catalog and runs on a shared Kanban board plus a short written daily update in Slack. Because the two founders sit in different time zones, they make writing the default from day one: every decision lands in a doc, so no one is blocked waiting for the other to wake up. When they later hire in a third time zone, onboarding is mostly just reading, and the async habit scales without change. The practice they never adopted, the synchronous status meeting, is the one they never miss.

**Enterprise.** A multinational bank rolled out a scaling framework across hundreds of teams, complete with quarterly big-room planning. Alignment improved on paper, but delivery slowed. Teams spent days in planning events and coordinating cross-team dependencies that the framework surfaced but did not remove. The bank course-corrected. It kept only the lightweight cross-team alignment it genuinely needed, restructured teams to own their value streams end to end, and shifted most coordination to written interfaces and async updates. Delivery lead time fell, and the exhausting planning marathons shrank to focused, occasional syncs.

**Government.** A government agency delivering citizen services worked across permanent staff in one region and contractor teams in two others, spanning many time zones, under mandated progress reporting. It adopted a docs-first, Kanban-based way of working. Every piece of work carried full written context on a shared board visible to staff and vendors alike. Handoffs between regions were written and complete. Required status reports came straight from the board rather than from separate meetings. This let a distributed, mixed workforce collaborate continuously, satisfied oversight reporting as a byproduct, and cut the agency's dependence on hard-to-schedule cross-timezone meetings.

## Business case: motivations, ROI, and TCO

The economic argument rests on flow efficiency. In most knowledge work, the time a unit of work spends actively worked is a small fraction of its total lead time. The rest is waiting: in queues, in meetings, in hand-offs, in time-zone gaps. Ways of working that shrink batch size, limit work in progress, and replace synchronous bottlenecks with written asynchronous flow attack that waiting directly. The payoff is shorter lead times and higher throughput without adding people, plus fewer defects, because feedback arrives sooner while context is fresh.

Weigh the cost of adopting against the cost of the status quo. Docs-first, async, and lean flow cost mainly a change in habits and some up-front investment in writing and tooling. They need no expensive licenses. Heavy scaling frameworks, by contrast, carry real cost: training, certification, dedicated roles, and the ongoing overhead of large planning events. Only genuine coordination needs justify that. The cost of doing nothing shows up as meeting-saturated calendars, excluded remote contributors, cargo-cult ceremonies that consume time without improving outcomes, and slow delivery. To make the case to leadership, measure delivery lead time, deployment frequency, and the fraction of the workweek lost to low-value meetings. Small improvements in flow across a large workforce add up to large capacity gains.

## Anti-patterns and pitfalls

- Cargo-cult agile: performing ceremonies without the underlying principles.
- Velocity as a target: invites point inflation and destroys the metric's usefulness.
- Framework worship: imposing SAFe or a "Spotify model" template regardless of fit.
- Estimates as commitments: treating forecasts under uncertainty as binding promises.
- Meeting-driven culture: defaulting to synchronous calls that exclude other time zones.
- Undocumented decisions: knowledge trapped in people's heads and past conversations.
- Vendor black boxes: managing contractors through opaque side channels instead of shared visibility.
- Utilization obsession: maximizing everyone's busyness rather than the flow of finished work.

## Maturity model

- Level 1 (Initial): Process is ad hoc or cargo-cult; communication is meeting-driven and undocumented; estimates are treated as promises.
- Level 2 (Managed): A methodology is followed consistently, but ceremonies are rote and coordination across teams is heavy.
- Level 3 (Defined): Practices are chosen to fit context; async, docs-first communication is the norm; estimation is used for conversation, not control.
- Level 4 (Optimizing): The team continuously tunes its way of working from flow metrics; coordination need is minimized at the source; distributed and mixed teams collaborate smoothly.

## Ideas for discussion

- Which of our ceremonies would we keep if we judged them purely on the value they create?
- Are we scaling by adding a framework or by reducing the need to coordinate?
- Is our velocity a planning aid or a target we are quietly gaming?
- What decisions and status live only in meetings and people's memories, and should be written?
- Whose time zone bears the cost of our synchronous meetings, and is that fair?
- Are our contractors and vendors working in the same visible flow as our staff?

## Key takeaways

- Adopt the principles behind methodologies, not just their rituals.
- Choose Agile, Kanban, or a blend to fit the work; favor small batches and fast feedback.
- Approach scaling frameworks skeptically; scale by reducing coordination, not adding process.
- Use estimates for conversation and forecasting, never as productivity targets or promises.
- Default to asynchronous, docs-first communication so large, distributed, mixed teams can collaborate.
- Optimize for outcomes and flow, not activity or utilization.

## References and further reading

- David J. Anderson, "Kanban: Successful Evolutionary Change for Your Technology Business"
- Donald Reinertsen, "The Principles of Product Development Flow"
- Mary and Tom Poppendieck, "Lean Software Development: An Agile Toolkit"
- Craig Larman and Bas Vodde, "Large-Scale Scrum (LeSS)"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (delivery metrics)
- The Agile Manifesto and its twelve principles
- Henrik Kniberg, "Scaling Agile @ Spotify" (with the caution that it is a snapshot, not a model)
- GitLab's public Handbook on asynchronous, remote-first working
