# 1.2 Team topologies and organizational design

## Overview and motivation

How you divide people into teams determines what software you can build and how fast you can build it. This is not a metaphor. It is a near-mechanical consequence known as [Conway's Law](https://en.wikipedia.org/wiki/Conway%27s_law): organizations design systems that mirror their own communication structures. If three teams build a [compiler](https://en.wikipedia.org/wiki/Compiler), you get a three-pass compiler. If your payments logic is split across a frontend team, a backend team, and a database team, every payment change needs three-way coordination. For a small organization, that is manageable. For a large one, the shape of the org chart becomes the dominant constraint on your engineering, your architecture, your delivery speed, and your quality. So designing team structure is a first-class engineering activity, not an HR afterthought.

Team topologies give you a deliberate vocabulary for this design. Instead of letting structure accrete by accident through reorgs and headcount, mature organizations choose team types and interaction modes on purpose, and they revisit those choices as the system and business evolve. The goal is to keep each team's [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) low, the total amount a team has to hold in its head to be effective, so teams can own their domain end to end and deliver a steady flow of value without constantly waiting on others.

For enterprises and government, this discipline is decisive. Large organizations naturally sprawl into deep hierarchies, shared services with long queues, and hand-off chains that turn a two-day change into a two-month project. Government adds procurement boundaries, contractor teams, and mandated [separations of duty](https://en.wikipedia.org/wiki/Separation_of_duties) that fragment ownership further. Explicit topology design is how these organizations reclaim flow: align teams to streams of value, build platforms that reduce cognitive load, and choose interaction patterns that make dependencies visible and intentional rather than hidden and constant.

## Key principles

- Conway's Law is inescapable; design teams to match the software engineering you want (the "inverse manoeuvre").
- Optimize for team cognitive load, not for maximum utilization of individuals.
- Prefer stream-aligned teams that own a slice of value end to end.
- Platforms exist to reduce the cognitive load of stream-aligned teams, not to gatekeep.
- Make team interactions explicit and few: collaboration, X-as-a-service, or facilitating.
- Minimize dependencies; every cross-team hand-off is a queue and a risk.
- Team structure is a living design that must evolve as the system and business change.

## Recommendations

### Use the four fundamental team types

Team topologies define four team types that cover most needs. Stream-aligned teams are the default: each owns a continuous flow of work for a specific product, service, or user journey, end to end. Platform teams provide internal products (compute, deployment, data pipelines, identity) that stream-aligned teams consume self-service, which lowers their cognitive load. Enabling teams are specialists (testing, security, observability) who coach stream-aligned teams to build a capability, then step back. Complicated-subsystem teams own components that need deep specialist expertise (a pricing engine, a [video codec](https://en.wikipedia.org/wiki/Video_codec), a cryptographic module), where it makes no sense for every team to hold that knowledge. Most of your teams should be stream-aligned; the other three types exist to support them.

### Apply the inverse Conway manoeuvre

Since software mirrors your organization's structure, shape your teams to produce the software you want. Want loosely coupled services with clear boundaries? Create loosely coupled teams with clear ownership boundaries. Want a payments capability that ships on its own schedule? Form a payments team that owns it front to back. Do not fight Conway's Law with heroic coordination. Redraw the team boundaries so the architecture you want becomes the path of least resistance.

### Manage cognitive load explicitly

A team can only master so much. Cognitive load includes the domain complexity, the technologies, the operational burden, and the breadth of stakeholders. When a team owns too many unrelated services, quality and speed both collapse. So bound each team's responsibilities to a domain it can genuinely master, and use platforms and enabling teams to take undifferentiated complexity off its plate. Keep teams to roughly five to nine people: small enough to communicate easily and to be fed, so to speak, by a couple of pizzas.

### Choose interaction modes deliberately

Limit team interactions to three modes. Collaboration is close, high-bandwidth work between two teams for a set period; it is powerful for discovery, but expensive, so keep it temporary. X-as-a-service is a clean provider/consumer relationship with a well-defined interface, ideal for platform consumption at scale. Facilitating is one team helping another learn, which is what enabling teams do. Name the mode for each important cross-team relationship, and read long-running collaboration between the same two teams as a signal that their boundary is in the wrong place.

### Choose an operating model for cross-cutting functions

Security, data, design, and similar disciplines can be organized in three ways: centralized (one team owns it for everyone), federated (specialists embedded part-time, coordinating through a guild), or embedded (a dedicated specialist inside each stream-aligned team). Centralized gives you consistency and depth, but it becomes a bottleneck. Embedded gives you speed and context, but it risks inconsistency and duplication. Federated (often a hub-and-spoke or [community-of-practice](https://en.wikipedia.org/wiki/Community_of_practice) model) sits between the two. Choose per function and per scale. Most large organizations land on federated for these disciplines, with a small central core that sets standards.

### Invest in inner-source

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) brings [open-source](https://en.wikipedia.org/wiki/Open-source_software) collaboration patterns inside the organization: shared internal repositories, published contribution guidelines, [code review](https://en.wikipedia.org/wiki/Code_review) across team boundaries, and clear maintainers. When a team needs a change to another team's component, it can contribute the change directly instead of filing a ticket and waiting in a queue. This relieves cross-team dependencies without dissolving ownership, and it spreads knowledge and standards naturally across a large engineering population.

## Trade-offs: pros and cons

| Model for cross-cutting functions | Pros | Cons |
| --- | --- | --- |
| Centralized (one team for all) | Consistency, deep expertise, clear standards | Bottleneck, queues, loss of product context |
| Federated (hub-and-spoke, guilds) | Balances consistency and speed; shares knowledge | Requires coordination discipline; accountability can blur |
| Embedded (specialist per team) | Fast, context-rich, high ownership | Duplication, inconsistency, hard to staff at scale |

| Team type | Best for | Risk if overused |
| --- | --- | --- |
| Stream-aligned | Most product and service delivery | None; this should dominate |
| Platform | Reducing shared cognitive load | Becomes an ivory-tower gatekeeper |
| Enabling | Spreading a capability temporarily | Turns into a permanent dependency |
| Complicated-subsystem | Genuinely deep specialist domains | Used as an excuse to hoard ordinary work |

The recurring trade-off is autonomy versus consistency. Fully autonomous teams move fast, but they drift apart in standards, tooling, and security posture. Fully centralized control keeps things consistent, but it strangles flow. Good topology design finds the seam: autonomy for stream-aligned delivery, plus thin central standards and paved-road platforms (well-supported default tooling that makes the compliant choice the easy one) for the things that genuinely have to be consistent.

## Questions to discuss with your team

1. **What concrete signals will tell you a team's cognitive load is too high, before quality collapses?** "Bound each team to a domain it can master" is easy to say and hard to act on without evidence, because cognitive load stays invisible until delivery and reliability degrade. Watch for measurable symptoms: the number of unrelated services or repositories a team owns, how long onboarding takes, how many domains a single engineer must context-switch across in a week, and rising incident rates in the corners of a team's remit. For a large organization, this matters because overloaded teams silently become bottlenecks that no reorg diagram predicts. Bring these numbers to the discussion, plus the team's own sense of what they can and cannot keep in their heads. If the signals say overloaded, the move is to shed undifferentiated work onto a platform or an enabling team, not to demand more heroics.

2. **Is a reorg genuinely worth the disruption here, or are you feeding a reorg addiction?** Redrawing boundaries to apply the inverse Conway manoeuvre is powerful, and every reorg also destroys the stability teams need to gel and resets hard-won domain knowledge. The competing considerations are the ongoing coordination tax of the current structure versus the one-time cost and morale hit of changing it. In enterprise and government settings, procurement boundaries, contractor teams, and mandated separations of duty make reorgs slower and more expensive, so the bar should be higher. Bring evidence of dependency-driven delay: how many initiatives are blocked waiting on another team, and for how long. Reorganize when that waiting is structural and large, and resist reshuffling when the pain is temporary or would be cheaper to solve with inner-source contributions and clearer interfaces.

3. **For security, data, and design, what event will trigger you to move between embedded, federated, and centralized?** The chapter's recommendation is to choose per function and per scale, and the harder discipline is deciding in advance what growth or risk will make you revisit that choice. A model that fits fifty engineers can become a bottleneck or a consistency disaster at five hundred, and enterprises and government bodies especially need to name the standards a small central core will always hold. Bring the current queue times and consistency gaps for each function: a central security team with multi-week review queues is a signal to federate, while embedded specialists producing incompatible data models is a signal to add a central standards core. Decide the trigger now, such as a queue-length threshold or an audit finding, so the change becomes a planned evolution rather than a crisis reaction. The answer determines where you invest in paved roads and champions versus a central hub.

4. **How will you know whether your platform team is genuinely lowering cognitive load or quietly becoming a gatekeeper?** A platform exists to make the compliant, reliable choice the easy one through self-service, and the same team can drift into mandating tools, hand-reviewing every request, and adding the friction it was meant to remove. For a large organization this distinction decides whether the platform investment pays back or turns into a central bottleneck that every stream-aligned team queues behind. The competing considerations are consistency and control on one side against consumer autonomy and flow on the other. Bring evidence a consumer would recognize: how long it takes a stream-aligned team to self-serve a new environment or pipeline without filing a ticket, the ratio of self-service actions to human-mediated ones, and platform adoption measured by teams that choose it rather than teams forced onto it. In enterprise and government settings, insist the platform generate audit and compliance evidence automatically rather than through manual gates, because a platform that meets separation-of-duty rules by inserting a human reviewer has recreated the bottleneck it was funded to dissolve.

5. **Which of your cross-team relationships have settled into permanent collaboration, and what would convert each one into a clean service interface or a redrawn boundary?** Collaboration mode is meant to be intense and temporary, and a pairing that never ends is usually a signal that ownership sits in the wrong place or that the interface between two teams was never made explicit. This matters at scale because unnamed, standing collaboration is where coordination cost hides: it does not appear on any org chart, yet it taxes every change the two teams touch. The competing considerations are the discovery value of staying close versus the flow you gain by turning the relationship into an X-as-a-service contract with a defined interface, or by merging the responsibility into a single team. Bring the list of team pairs that have collaborated continuously for more than a quarter, the changes that required both teams in the last few months, and whether a stable interface between them could be written down. For enterprise and government contexts, where contractor boundaries and procurement lots can freeze a hand-off in place for years, name which relationships you can convert with an interface and inner-source contributions and which are contractually fixed and must be managed as explicit dependencies.

6. **When an enabling team helps another team build a capability, how will you know it has succeeded and can step back rather than becoming a permanent dependency?** Enabling teams are meant to coach a stream-aligned team to master testing, security, or observability and then move on, and without an explicit exit condition the coaching relationship hardens into a standing service the stream-aligned team never actually absorbs. For a large organization this is the difference between spreading a capability across dozens of teams and creating a new shared bottleneck that scales worse every year. The competing considerations are the depth and consistency a specialist team provides against the autonomy and end-to-end ownership you are trying to build into stream-aligned teams. Bring evidence of capability transfer: whether the receiving team now handles the work without the enabling team present, how many teams a fixed enabling group is committed to at once, and how long each engagement has run past its intended handover. In enterprise and government settings, where a scarce specialist skill may sit behind a single central team or a single contract, decide in advance how you fund capability transfer and champions so that expertise diffuses into delivery teams rather than staying locked behind a queue that every audit and release must wait on.

## Sector lens

**Startup.** With a handful of engineers and little runway, the right topology is a single stream-aligned team that owns the whole product, and the discipline is refusing to create silos before you need them. Resist hiring a lone "DevOps" or "QA" person who becomes a gate; fold those skills into the one team as an embedded capability. Keep Conway's Law working for you by keeping the org flat, so the architecture stays as simple and changeable as the team.

**Small business.** You will not staff a dedicated platform or enabling team, so buy the platform: use managed cloud services, hosted pipelines, and off-the-shelf security tooling to take undifferentiated cognitive load off your one or two teams. Frame cross-cutting concerns like security and data as things you configure and consume rather than a function you build. Reserve any bespoke ownership for the one complicated subsystem that genuinely differentiates you, and let vendors carry the rest.

**Enterprise.** At scale the problem is coordination cost across many teams, so make topology an explicit, governed design: a shared taxonomy of the four team types, named interaction modes, a paved-road platform, and inner-source to relieve cross-team queues. Track dependency-driven delay and team cognitive load as portfolio metrics, and run reorganizations as deliberate evolutions with a high bar rather than an annual reflex. A thin central core holds the standards that must be consistent, while stream-aligned teams keep autonomy over delivery.

**Government.** Procurement rules, contractor boundaries, and mandated separations of duty fragment ownership, so design topology to meet those constraints through tooling and clear interfaces rather than human hand-offs. Favor federated models with a small standards core and a platform that generates audit and compliance evidence automatically, so separation of duty is enforced by pipelines rather than review queues. Document team boundaries, interaction modes, and the operating model openly, so structure is transparent to auditors, oversight bodies, and the public that funds it.

## Examples

**Startup.** A ten-person startup has a single stream-aligned team that owns the whole product end to end, which is exactly right at its scale: no hand-offs, no coordination tax, everyone sharing the same context. Trouble starts when they hire a dedicated "DevOps person" and a separate "QA person" and accidentally recreate functional silos, so every release now waits on two individuals. They course-correct by treating those hires as an embedded platform-and-testing capability inside the one team, rather than gates that work must pass through. At this size, the cheapest topology is the one that keeps everyone in a single flow.

**Enterprise.** A large retailer's checkout was slow to change because frontend, backend, and fulfilment logic were split across three functionally organized teams, forcing every change through three backlogs. Applying the inverse Conway manoeuvre, they reorganized into stream-aligned teams around customer journeys ("browse," "cart and checkout," "post-purchase"), each owning its slice front to back, backed by a platform team that provided deployment and observability as a service. Checkout changes that once took a quarter started shipping in days, because the coordination that used to span teams now happened inside one.

**Government.** A government tax agency ran a central security team that reviewed every release, creating a multi-week queue that delayed critical fixes. They shifted to a federated model: a small central security function set standards and provided a "paved road" of pre-approved, automatically scanned pipelines, while security champions embedded part-time in each delivery team handled the day-to-day decisions. The platform generated compliance evidence automatically. Mandated separation-of-duty requirements were still met, but through tooling and clear interfaces rather than a human bottleneck, which cut release lead time dramatically while improving audit readiness.

## Business case: motivations, ROI, and TCO

You pay for poor team design in coordination overhead, and that overhead grows faster than linearly with the number of teams that have to synchronize for a typical change. Every hand-off is a queue with waiting time, a context transfer that loses information, and a fresh chance to miscommunicate. When a routine change needs three teams to align their roadmaps, the real cost is not the sum of their work; it is the far larger cost of scheduling, waiting, and rework. Redraw boundaries so that most changes fit inside one team's ownership, and that overhead simply goes away.

The adoption cost is real. Reorganizations are disruptive, and building platforms and inner-source practices takes up-front investment before the payoff arrives. But the cost of not adopting compounds. Organizations that let structure accrete by accident pile up hand-off chains, shared bottleneck teams with quarter-long queues, and architectures fossilized by the org chart. To make the case to leadership, measure dependency-driven delay: how many active initiatives are blocked waiting on another team, and for how long. Platform and topology investments usually pay back by turning that waiting into flow, which shows up as shorter lead times and higher throughput without adding headcount.

## Anti-patterns and pitfalls

- Ignoring Conway's Law: designing an architecture the org structure cannot deliver.
- Functional silos: separate frontend, backend, QA, and ops teams that must coordinate for any change.
- Shared-services bottleneck: a central team every project must queue behind.
- Platform as gatekeeper: a platform team that mandates rather than serves, adding friction instead of removing it.
- Cognitive overload: teams owning sprawling, unrelated systems they cannot master.
- Permanent "collaboration": two teams perpetually entangled, signaling a misplaced boundary.
- Reorg addiction: reshuffling constantly, destroying the stability teams need to gel.

## Maturity model

- **Level 1, Initiate.** Teams form by accident, headcount, or legacy hierarchy; nobody names team types or interaction modes; functional silos and shared-service bottlenecks are everywhere and dependencies are hidden until they block a release.
- **Level 2, Develop.** Some stream-aligned teams exist and a first platform or inner-source effort appears, but the pattern is applied unevenly: a few teams own their slice end to end while others still queue behind central functions, and cognitive load is discussed anecdotally rather than managed.
- **Level 3, Standardize.** The four team types and the three interaction modes are documented and used deliberately across the org; platforms and inner-source relieve cross-team dependencies; an operating model for security, data, and design is chosen and written down, and new teams are formed against these standards rather than by improvisation.
- **Level 4, Manage.** Topology is measured and controlled against baselines: teams track cognitive load, dependency-driven delay (initiatives blocked waiting on another team, and for how long), platform self-service ratios and adoption, interaction-mode duration, and delivery flow metrics such as lead time and change frequency. Thresholds trigger action, for example a queue length that forces a function to federate or a standing collaboration that flags a misplaced boundary, so decisions rest on evidence rather than opinion.
- **Level 5, Orchestrate.** Team design is continuously improved and integrated with architecture, product, and risk planning; the organization reshapes boundaries as the system and business evolve, retires enabling engagements once capability has transferred, and rebalances platform investment as cognitive load shifts, keeping fast flow as an adaptive, standing property rather than a one-time reorg.

## Ideas for discussion

- For a typical change, how many teams must coordinate, and why?
- Which of our teams are carrying too much cognitive load, and what could a platform offload?
- Where are we fighting Conway's Law instead of redrawing boundaries?
- Are our platform teams serving stream-aligned teams or gatekeeping them?
- Should security, data, and design be centralized, federated, or embedded for us right now?
- Which "temporary" collaborations have quietly become permanent dependencies?

## Key takeaways

- Org structure determines architecture and delivery speed; design it deliberately.
- Use the four team types, with stream-aligned as the default and the rest in support.
- Apply the inverse Conway manoeuvre to make the desired architecture the easy path.
- Manage cognitive load; bound each team to a domain it can master.
- Limit and name cross-team interaction modes; treat lingering dependencies as boundary defects.
- Choose centralized, federated, or embedded models for cross-cutting functions per scale, and use InnerSource to relieve queues.

## References and further reading

- Matthew Skelton and Manuel Pais, "Team Topologies: Organizing Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
