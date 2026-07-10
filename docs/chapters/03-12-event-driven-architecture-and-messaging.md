# 3.12 Event-driven architecture and messaging

## Overview and motivation

[Event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture) (EDA) is a style in which components communicate by producing and reacting to events rather than by calling each other directly. An event is a fact: something that already happened, such as "OrderPlaced" or "PaymentCaptured." A producer announces the fact and moves on, and any number of consumers react on their own schedule without the producer knowing who is listening. This is a different posture from the request-and-reply calls of chapter 2.3, where a caller asks a specific service to do something and waits for the answer.

For a large organization, the appeal is decoupling at scale. When you have dozens of teams and hundreds of services, wiring everything together with direct point-to-point calls produces a brittle web where one team's change breaks another's and no one can trace why. Events let teams integrate through a shared stream of facts instead of through each other's internals, and a new consumer joins by subscribing, without the producer changing a line of code. That property, more than raw throughput, is why event-driven approaches keep spreading through enterprises replacing tangled integrations and governments joining up agencies that each own their own systems.

The public sector gets a second benefit that is easy to undervalue: a durable, ordered record of what happened is an audit and transparency asset. When a citizen asks why a benefit decision came out the way it did, an immutable log of the events that led to it answers directly. But event-driven design is not free and not always right: asynchronous flows are harder to trace, harder to reason about, and easy to over-apply. This chapter is opinionated about when the decoupling and scale pay for the added complexity, and when a plain synchronous call would have served you better. It builds on the distributed-systems realities of chapter 3.3, so read that first if you have not.

## Key principles

- **Events are facts, not instructions.** An event says what happened; a command asks for something to happen. Keep them distinct, and name events in the past tense.
- **Decoupling is the point.** Producers should not know or care who consumes their events. If they do, you have coupling wearing a messaging costume.
- **Design for at-least-once delivery.** Exactly-once delivery is a myth. Make every consumer idempotent so duplicates are harmless.
- **Order is a guarantee you pay for.** You get ordering within a partition, not across a topic. Choose partition keys deliberately.
- **The schema is the contract.** An event's shape is a public interface; evolve it with the care you would a published API.
- **Asynchronous does not mean unobservable.** If you cannot follow a message end to end, you cannot operate the system.
- **Complexity must be earned.** Event sourcing, CQRS, and sagas are powerful and costly; reach for them when the problem demands it, not by default.

## Recommendations

### Distinguish events, commands, and messages before you build anything

These three words get used interchangeably, and the confusion causes real design mistakes. A **command** is a request to do something ("CapturePayment"), directed at one handler, and it can be rejected. An **event** is a notification that something already happened ("PaymentCaptured"), broadcast to anyone interested, and it cannot be rejected because the fact is already true. A **message** is the neutral envelope that carries either over the wire. The distinction shapes coupling: commands couple the sender to a specific receiver and outcome, while events surrender control over what happens next. Name your events in the past tense, and when you catch yourself publishing an "event" that really means "please go do this specific thing," you have written a command in disguise.

### Choose queues, logs, and publish/subscribe on purpose

Not all messaging is the same shape, and picking the wrong one is a common early mistake. A [message queue](https://en.wikipedia.org/wiki/Message_queue) delivers each message to one consumer and typically removes it once processed, which fits work distribution: many workers pulling tasks, each done once. A durable **event log** (a stream) keeps events in order and lets many independent consumers read at their own pace, replaying history from any point, which fits event distribution and audit. **Publish/subscribe** has producers publish to a topic and multiple subscribers each get their own copy. The practical rule: if the message is a task one worker should complete, reach for a queue; if it is a fact many parties may care about now or later, reach for a durable log, which also gives you replay for recovery and onboarding new consumers. See chapter 3.4 for how these choices interact with your data storage strategy.

### Prefer choreography for autonomy, orchestration for control

When a business process spans several services, you coordinate it one of two ways. In **choreography**, each service reacts to events and emits its own, with no central brain: maximally decoupled and good for team autonomy, but the overall process exists only as emergent behavior that no single place describes. In **orchestration**, a central coordinator drives the steps and knows the whole flow: easier to monitor and modify, at the cost of a component every step depends on. A good default is choreography for loosely related reactions ("when an order ships, the loyalty service awards points") and orchestration for a defined transaction with a clear success condition and a need to report status. Do not let an important process live only as tribal knowledge scattered across ten event handlers.

### Reach for event sourcing and CQRS only when they earn their keep

**Event sourcing** stores state as an append-only sequence of events rather than a current snapshot you overwrite, and you rebuild current state by replaying them. The upside is a perfect audit trail, the ability to reconstruct any past state, and temporal queries; the cost is that you version event schemas forever, handle replay and snapshots, and carry a mental model most developers have never used. **CQRS** (Command Query Responsibility Segregation) separates the write model from one or more read models so reads and writes scale and evolve independently; it pairs naturally with event sourcing but does not require it. Both shine for domains with genuine audit, compliance, or complex-query needs, which is why regulated finance and government find them worth the trouble. For a simple create-read-update-delete service they are accidental complexity you will regret, so apply them to the slice of your domain that needs them, not the whole system by reflex.

### Manage distributed transactions with sagas, not two-phase commit

You usually cannot wrap one atomic transaction around several services and databases. Distributed [two-phase commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) holds locks across the network, cuts availability, and scales badly, so it rarely fits an event-driven system. The **saga pattern** replaces it: model the transaction as a sequence of local transactions, each emitting an event that triggers the next, and give each step a **compensating action** that undoes it if a later step fails. If "reserve inventory" succeeds but "charge card" fails, a compensation releases the inventory. Sagas can be choreographed or orchestrated, and orchestration usually wins for anything you must monitor. Because sagas embrace eventual consistency, the system passes through intermediate states ("reserved but not paid") before it converges, so design your user experience and audit trail to show "in progress" and "compensated" states honestly. Chapter 3.3 covers this same ground from the distributed-systems angle.

### Design for at-least-once delivery and make consumers idempotent

Message systems cannot truly deliver exactly once across failures, because the acknowledgment that says "I processed this" can itself be lost, forcing a redelivery. What you can achieve is **at-least-once delivery with idempotent processing**, which produces exactly-once *effects*. [Idempotence](https://en.wikipedia.org/wiki/Idempotence) means processing the same event twice leaves the same result as processing it once; get there with an idempotency key on each event and a record of what you have already handled, so a duplicate is recognized and dropped. **At-most-once** delivery (fire and forget, no redelivery) is simpler but silently loses messages, so reserve it for data you can afford to lose. Treat the "exactly-once" label some vendors advertise with suspicion: it usually means exactly-once within one system's boundary under specific conditions, not the end-to-end guarantee the phrase implies.

### Control ordering with partitions, and know your consumer groups

Ordering is not global and free; it is local and paid for. A stream is split into **partitions**, and you get ordering within a partition, not across the topic. Events route to a partition by a **partition key**, so choosing that key is how you control what stays ordered: key by customer ID and one customer's events stay in order relative to each other, while different customers process in parallel. **Consumer groups** let a set of workers share a topic's partitions, each partition handled by one worker, which is how you scale throughput while preserving per-partition order; this is where scalability meets correctness, connecting to chapter 3.5. Pick a partition key that reflects your real ordering requirement and spreads load evenly, because a key that funnels most traffic into one partition creates a hot spot no amount of workers can relieve.

### Treat schemas as contracts with a registry and evolution rules

An event's structure is a published interface consumed by teams you may never meet, so changing it carelessly breaks them at a distance. Put your event schemas in a **schema registry**, a shared catalog that stores each schema and enforces compatibility rules when a producer tries to change one. Adopt an explicit policy: backward-compatible changes (adding an optional field) are allowed; breaking changes (removing a field, changing a type, renaming) require a new schema version and a migration plan. This lets producers evolve without a synchronized deploy across every consumer, which is the whole reason you chose events. The same interface-versioning discipline from chapter 2.3 applies, because an event schema is an API by another name.

### Guarantee delivery with the transactional outbox, and handle failures explicitly

A classic bug: your service writes to its database and then publishes an event, and it crashes between the two, so the database changed but the event never went out. The **transactional outbox** fixes this by writing the event into an outbox table in the *same* database transaction as the state change, so they commit or fail together; a separate relay then reads the outbox and publishes to the broker, often using [change data capture](https://en.wikipedia.org/wiki/Change_data_capture) to tail the database log. For consumption failures, a [dead letter queue](https://en.wikipedia.org/wiki/Dead_letter_queue) holds messages that repeatedly fail so a **poison message** (one that will never succeed, perhaps because it is malformed) does not block the queue behind it forever. Add **backpressure** so a fast producer cannot overwhelm a slow consumer: bound your queues, and slow or shed load when they fill rather than exhausting memory. These four mechanisms separate a demo from a system you can run at 3 a.m.

### Make asynchronous flows observable end to end

The hardest cost of going event-driven is that a single business action now scatters across producers, brokers, and consumers with no call stack tying them together. Propagate a **correlation ID** through every event so you can follow one logical flow across every hop, the same discipline chapter 3.3 prescribes for synchronous calls. Track **consumer lag** (how far behind real time each consumer is reading) as a first-class metric, because rising lag is your earliest warning of trouble, and monitor dead letter queue depth, processing latency, and redelivery rates. Without this, an event that quietly fails to be consumed becomes an invisible bug that surfaces days later as missing data.

## Trade-offs: pros and cons

| Approach | Pros | Cons / cost |
|---|---|---|
| Synchronous request/reply | Simple to reason about, immediate result, easy tracing | Tight temporal coupling, cascading failures, limited scale |
| Event-driven (pub/sub over a log) | Decoupling, independent scaling, replay, audit trail | Eventual consistency, harder tracing, more moving parts |
| Message queue (work distribution) | Load leveling, buffering, back-pressure friendly | One consumer per message, less suited to broadcast |
| Event sourcing + CQRS | Full history, temporal queries, read/write scale independently | Schema versioning forever, replay complexity, steep learning curve |
| Saga (vs two-phase commit) | Scalable, available, no distributed locks | Eventual consistency, compensation logic, harder to reason about |

The central tension is between decoupling and comprehensibility. Every event you add loosens the coupling between producer and consumer, buying team autonomy and independent scaling, and at the same time it removes a line of the story that a synchronous call would have told you plainly: the flow becomes emergent, living in the interactions rather than in any one file. Resolve this by being selective: use events where decoupling genuinely pays, such as integration across team boundaries, fan-out to many consumers, buffering of load spikes, and audit. Keep synchronous calls where you need an immediate answer and a simple mental model, such as reading data to render a page. The failure mode to avoid is turning every internal function call into an event and calling it architecture, the same architectural judgment chapter 3.2 asks of every pattern you adopt.

## Questions to discuss with your team

1. **For this specific interaction, do we actually need an event, or would a synchronous call be clearer and safer?** Skipping this question is how a system accretes accidental complexity. The honest test is whether the producer needs a result back right now (a call) or is announcing a fact that others may react to on their own time (an event). Bring the specific interaction, not a general preference, and ask what decoupling you gain and what tracing clarity you give up. If the caller blocks waiting for the "event" to be processed, you have built a slow, hard-to-debug synchronous call and paid extra for the privilege. The default for internal, same-team, need-the-answer-now interactions should be a direct call; reserve events for where the loose coupling earns its cost.

2. **What happens when a consumer receives the same event twice, and have we actually tested it?** At-least-once delivery guarantees duplicates will happen, so every consumer must be idempotent, yet idempotency is easy to claim and easy to get wrong. Walk through a real consumer and trace exactly how a second delivery is recognized and neutralized, whether by an idempotency key, a processed-events log, or a naturally idempotent operation. Bring the results of an actual test where you redeliver a batch and confirm no doubled charges, duplicate records, or repeated notifications. Pay special attention to side effects that leave your database, such as emails, payments, and third-party calls, because those are where non-idempotent bugs hurt customers directly. If your team cannot point to a test that proves duplicate-safety, assume you are not duplicate-safe.

3. **When an event flow breaks in production, how long until we notice, and can we trace one message end to end?** Asynchronous failures are quiet, so a consumer that silently stops processing can go unnoticed until missing data becomes a customer complaint or an audit gap. Ask what your earliest signal is, and whether you monitor consumer lag and dead letter queue depth as alerting metrics rather than dashboards nobody watches. Bring a real incident or a game-day exercise and time how long it takes to follow a single correlation ID across producer, broker, and every consumer. If the answer is "we grep several services and guess," your observability is not ready for the complexity you have taken on. In regulated sectors, being able to reconstruct exactly how a message moved is often a compliance requirement, not a nicety.

## Examples

**Startup.** A small e-commerce startup begins with one synchronous flow: checkout calls the payment service and waits. As it grows, it wants order confirmation emails, inventory updates, and a loyalty program to react to purchases, and wiring each as another synchronous call inside checkout makes checkout slow and fragile. The team publishes a single "OrderPlaced" event to a durable log and lets three independent consumers react, so checkout is fast again and adding a fourth reaction later needs no change to it. They keep payment capture synchronous, because they need the yes-or-no answer before confirming the order, which is exactly the right line to draw at their size.

**Enterprise.** A global insurer is drowning in point-to-point integrations and an aging [enterprise service bus](https://en.wikipedia.org/wiki/Enterprise_service_bus) (ESB), a central hub that every system routes through and that has become a bottleneck and a single point of failure. It migrates to a durable event log where each domain publishes its facts (policy issued, claim filed, payment made) and consuming teams subscribe to what they need. A claims saga, orchestrated so operations staff can see each claim's status, coordinates the multi-step settlement with compensations for steps that fail. A schema registry lets the policy team evolve their events without a synchronized deploy across forty consuming systems, precisely the brittleness the old ESB imposed.

**Government.** A national tax agency must give citizens and auditors a defensible answer to "why did my assessment come out this way." It models the assessment domain with event sourcing, so every change is an immutable event in an ordered log and the current assessment is a replay of those events; when a citizen disputes a figure, a caseworker reconstructs the exact state at any past date and shows the sequence of facts that produced it. Inter-agency data sharing runs over durable topics with at-least-once delivery, and each agency's consumer deduplicates on an event ID so a redelivered record never creates a duplicate case. The event log doubles as the audit trail oversight bodies require, turning a compliance obligation into a byproduct of the design.

## Business case: motivations, ROI, and TCO

The return on event-driven architecture is dominated by one thing: the cost of integration over time. Point-to-point integration makes that cost grow with the number of connections, which grows faster than the number of systems, so integration becomes the tax that eats your delivery capacity. Events flatten this, because teams integrate through a shared stream of facts, a new consumer joins by subscribing, and producers evolve behind a versioned schema, so the marginal cost of the next integration drops sharply. That is the core ROI story to tell leadership: not raw performance, but the compounding reduction in the cost of change across many teams.

Name the total cost of ownership honestly so you are believed. You take on broker infrastructure to run, schema governance to maintain, and a steeper operational learning curve, because asynchronous systems are genuinely harder to debug, so budget for the observability investment up front. Weigh these against the cost of *not* adopting events where they fit: an ossified integration layer where every change is a multi-team coordination project, a legacy ESB that has become a bottleneck no one dares touch, and an inability to add capabilities without disturbing old ones. For the enterprise replacing brittle point-to-point wiring and the government building durable audit trails, the payoff is strongest where the audit and decoupling needs are real. Where those needs are absent, the honest answer is that a simpler synchronous design has the lower TCO, and you should say so.

## Anti-patterns and pitfalls

- **The distributed monolith in disguise.** Services that must all deploy together and depend on each other's internal events. You added a broker but kept the coupling, so you have the downsides of both styles.
- **Events as commands.** Publishing "events" that really mean "please do this specific thing for me," recreating tight coupling with extra latency and worse traceability.
- **Assuming exactly-once delivery.** Consumers that break, double-charge, or duplicate records when the broker inevitably redelivers a message.
- **Event sourcing everything.** Applying event sourcing and CQRS to simple create-read-update-delete domains that never needed history, buying steep complexity for no benefit.
- **No schema governance.** Producers changing event shapes freely, breaking downstream consumers at a distance with no compatibility checks.
- **Ignoring the outbox.** Writing to the database and publishing an event as two separate steps, so a crash between them silently loses events or emits phantom ones.
- **No dead letter handling.** A single poison message blocking a partition, or failed messages vanishing with no queue to catch and inspect them.
- **Invisible flows.** Asynchronous processing with no correlation IDs, no consumer-lag alerts, and no tracing, so failures stay silent until they become missing data.

## Maturity model

- **Level 1, Initial:** Integration is ad hoc point-to-point calls, or a broker exists but is used like synchronous request/reply. Duplicates break consumers, there is no schema discipline or cross-hop tracing, and failed messages disappear silently.
- **Level 2, Managed:** A broker or log is in real use for some flows. Consumers are becoming idempotent and dead letter queues catch failures, but events and commands are still muddled, schemas change informally, and observability is thin.
- **Level 3, Defined:** Events, commands, and messages are distinguished deliberately. Consumers are idempotent by standard, schemas live in a registry with a compatibility policy, and the transactional outbox guarantees delivery. Sagas handle multi-service transactions, correlation IDs propagate, and consumer lag is monitored.
- **Level 4, Optimizing:** Event-driven and synchronous styles are chosen per interaction on evidence, not fashion, and event sourcing and CQRS are applied precisely where audit and query needs justify them. Replay, schema evolution, and failure handling are tested routinely, and asynchronous flows are as observable as synchronous ones.

## Ideas for discussion

1. Which of your current "events" are secretly commands, and what coupling would you remove by modeling them honestly?
2. If you replayed a full day of events through your consumers tomorrow, what would break, and what does that tell you about your idempotency and replay-safety?
3. Which parts of your domain genuinely need event sourcing's audit trail, and which are simple state you would only complicate by sourcing?
4. How would you migrate off a legacy enterprise service bus or a web of point-to-point integrations without a risky big-bang cutover?
5. For your most important multi-service process, is it a real orchestrated saga with compensations, or an emergent choreography that no single place describes?

## Key takeaways

- Event-driven architecture buys decoupling, independent scaling, replay, and audit trails, and it costs comprehensibility and operational complexity, so choose it per interaction where the benefit is real.
- Keep events (facts that happened), commands (requests to act), and messages (the envelope) distinct, because the confusion causes real coupling mistakes.
- Design for at-least-once delivery and make every consumer idempotent; exactly-once delivery is a myth, and exactly-once effects are an engineering achievement.
- Ordering is per partition, schemas are contracts that belong in a registry, and the outbox, dead letter queues, and backpressure are the plumbing that makes messaging production-ready.
- Use sagas with compensations instead of two-phase commit, and reach for event sourcing and CQRS only where audit and query needs justify their steep cost.
- Asynchronous flows are silent when they fail, so correlation IDs, consumer-lag monitoring, and end-to-end tracing are the difference between an operable system and an invisible one.

## References and further reading

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Chris Richardson, *Microservices Patterns* (sagas, transactional outbox, CQRS)
- Sam Newman, *Building Microservices*
- Ben Stopford, *Designing Event-Driven Systems*
- Adam Bellemare, *Building Event-Driven Microservices*
- Vaughn Vernon, *Implementing Domain-Driven Design* (event sourcing and CQRS)
- Martin Fowler, "Event Sourcing" and "CQRS" (martinfowler.com articles)
- Hector Garcia-Molina and Kenneth Salem, "Sagas" (1987)
