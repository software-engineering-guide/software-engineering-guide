# 3.3 Distributed systems

## Overview and motivation

A [distributed system](https://en.wikipedia.org/wiki/Distributed_computing) is any system whose components run on more than one machine and coordinate over a network. The moment you cross a process boundary over a network, you inherit some hard truths that simply do not exist inside a single process. The network is unreliable, and its latency varies. Messages can be lost, duplicated, delayed, or reordered. Remote components fail on their own. There is no shared clock. The classic "[fallacies of distributed computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)" (the network is reliable, latency is zero, bandwidth is infinite, the topology never changes) name exactly the assumptions that cause outages. Your job is to design for these realities from the start, rather than rediscover them during an incident.

For a large organization, distribution is not optional. Any system that serves national or global scale, joins up multiple departments, or needs high availability will span many machines, data centres, and often regions. Enterprises run distributed transaction systems, event pipelines, and multi-region deployments. Governments run inter-agency integrations where each agency owns its own systems and no one controls the whole. Here the gap between a robust design and a fragile one shows up as headline outages, missed benefit payments, and regulatory consequences. The techniques in this chapter (consistency reasoning, [idempotency](https://en.wikipedia.org/wiki/Idempotence), retries with backoff, [circuit breakers](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern), [sagas](https://en.wikipedia.org/wiki/Long-running_transaction), and distributed observability) are your standard defences.

The hardest part of distributed systems is that failures are partial and intermittent. A single-machine program either works or crashes. A distributed system can be half-working: some requests succeeding, some timing out, and some silently lost, all at once. This chapter focuses on the reasoning and patterns that let a large team build systems that degrade gracefully and stay understandable under partial failure.

## Key principles

- **The network is not reliable.** Design every remote interaction assuming it can be slow, fail, duplicate, or reorder.
- **You cannot have perfect consistency and perfect availability during a partition.** Choose deliberately per interaction (CAP/PACELC), and remember latency is a cost even when there is no partition.
- **Make operations idempotent.** If an operation can be safely retried, most distributed failure handling becomes tractable.
- **Every remote call needs a timeout.** Unbounded waits turn one slow dependency into a system-wide outage.
- **Prefer eventual consistency where the business allows it, but make it explicit.** Users and auditors must understand when they might see stale data.
- **Isolate failures.** Bulkheads and circuit breakers stop one failing component from cascading into all of them.
- **You cannot debug what you cannot see.** Distributed flows require correlated tracing, metrics, and logs across every hop.
- **"Exactly-once delivery" is a myth; exactly-once *processing* is an engineering achievement.** Design for at-least-once with deduplication.

## Recommendations

### Reason about consistency with CAP and PACELC

The [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) says that during a network partition a system must choose between consistency (every read sees the latest write) and availability (every request gets a response). [PACELC](https://en.wikipedia.org/wiki/PACELC_design_principle) adds a second trade: **E**lse (when there is no partition) you still trade **L**atency against **C**onsistency. Do not stamp this as a whole-system label. Decide it per operation. A bank's balance transfer needs strong consistency and will refuse rather than risk a double-spend. A social feed or a product-view counter can accept staleness in exchange for availability and speed. Write down which consistency model each data flow uses (strong, causal, read-your-writes, or eventual) so no one assumes a guarantee the system does not actually provide.

### Build idempotency, timeouts, retries, and backoff together

Treat these four techniques as one package. Give every remote operation a **timeout**, so a hung dependency cannot block a thread forever. On failure, **retry**, but only for operations that are safe to repeat. Safe to repeat means **idempotent**: assign each request a unique key and have the receiver deduplicate, so a retried "charge card" does not charge twice. Space your retries with **[exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) and jitter**, so you avoid a synchronized retry storm that turns a brief blip into a self-inflicted [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack). Cap the number of retries and the total time budget, because retrying forever just moves the failure. Without idempotency, retries are dangerous. Without backoff, retries are destructive.

### Add circuit breakers and bulkheads to stop cascades

A **circuit breaker** watches calls to a dependency and, after a threshold of failures, "opens": it fails fast for a cooldown period instead of piling more requests onto a struggling service, then "half-opens" to test recovery. This stops the cascade where a slow downstream service exhausts every caller's threads until the whole system stalls. **Bulkheads** partition resources (thread pools, connection pools) so that saturation in one dependency cannot eat the capacity others need. Pair both with graceful degradation: when a non-critical dependency is unavailable, return cached or default responses rather than failing the whole request.

### Manage distributed transactions with sagas, not two-phase commit

You usually cannot hold a single [ACID](https://en.wikipedia.org/wiki/ACID) (Atomicity, Consistency, Isolation, Durability) transaction across multiple services or databases. Distributed [two-phase commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) is slow, locks resources, and cuts availability. Use the **saga pattern** instead. Model a business transaction as a sequence of local transactions, each publishing an event that triggers the next, with a **compensating action** for each step to undo it if a later step fails. Sagas come in two flavours. **Choreography** has services react to each other's events, with no central controller. **Orchestration** has a central coordinator drive the steps, which is easier to reason about and monitor. Sagas embrace eventual consistency: the system passes through intermediate states and then converges. So design the user experience and the audit trail to account for "in-progress" and "compensated" states.

### Treat exactly-once as at-least-once plus deduplication

[Message brokers](https://en.wikipedia.org/wiki/Message_broker) cannot truly guarantee exactly-once delivery across failures. What they and you *can* achieve is **at-least-once delivery with idempotent processing**, which yields exactly-once *effects*. Design consumers to handle duplicate messages safely, using idempotency keys or a processed-message log. Know your broker's ordering and delivery guarantees precisely. For streaming, use consumer groups, partitions, and offset management on purpose, and make reprocessing safe, so you can replay a stream after a bug fix without corrupting downstream state.

### Instrument distributed flows end to end

Adopt the three pillars of observability, correlated across service boundaries. Propagate a **trace/correlation ID** through every hop, so you can follow a single user request across all the services it touches (distributed tracing). Emit structured **metrics** (latency percentiles, error rates, saturation, throughput) per service and per dependency. Emit structured **logs** that carry the correlation ID. Use all this to set service-level objectives and to alert on symptoms users actually feel, such as error rate and latency, rather than only on individual machine health. In a distributed system, observability is not optional tooling. It is the only way to understand behaviour under partial failure.

## Trade-offs: pros and cons

| Technique | Pros | Cons / cost |
|---|---|---|
| Strong consistency | Simple mental model, no stale reads | Lower availability during partitions, higher latency, coordination cost |
| Eventual consistency | High availability, low latency, scalable | Stale reads, complex reasoning, needs conflict resolution |
| Retries with backoff | Rides out transient failures automatically | Amplifies load if misused; needs idempotency and caps |
| Circuit breakers / bulkheads | Prevent cascading failure, fail fast | Added complexity, tuning thresholds, risk of premature tripping |
| Saga (vs 2PC) | Scalable, available, no distributed locks | Eventual consistency, compensation logic, harder to reason about |

The master trade-off is between coordination and independence. Every guarantee you want across machines (consistency, ordering, exactly-once) costs latency, availability, or complexity. It requires machines to agree, and agreement over an unreliable network is expensive. The skill is to buy only the guarantees the business truly needs, operation by operation, and to design everything else for graceful degradation. Over-buy consistency and your systems turn slow and fragile. Under-buy it and you get silent data corruption that surfaces as an audit failure months later.

## Questions to discuss with your team

1. **Are your resilience patterns shipped as shared platform defaults, or is every team reinventing timeouts and retries?** The chapter treats idempotency, timeouts, bounded retries, circuit breakers, and tracing as cheapest and most reliable when built once into shared libraries and platform defaults. In a large organization, leaving each team to hand-roll them guarantees inconsistency: some paths retry non-idempotent operations, some have no timeout, some emit no correlation ID. Bring evidence by auditing a sample of services and counting how many set an explicit timeout on every remote call and propagate a trace ID end to end. If that number is low, the fix is a platform investment, not a training memo. Standard defaults also make resilience testable and auditable, which regulators in finance and government increasingly expect you to demonstrate.

2. **Do your timeouts and retry budgets compose across the whole call chain, or does a deep request retry itself into an outage?** A single request often crosses many hops, and if each layer independently retries three times with its own timeout, the innermost failure multiplies and the outer caller waits far past any human-tolerable limit. Set a total time budget for the user-facing request and divide it down the chain, so an inner service knows how little time it has left and fails fast rather than retrying into a storm. Bring your dependency graph and a real trace, then add up the worst-case timeout and retry combination and compare it to what the user will actually wait. Exponential backoff with jitter and a cap on total attempts keeps a brief blip from becoming a self-inflicted denial of service. Deep, chatty synchronous chains are the enemy here, so the answer may push you toward asynchronous flows or fewer hops.

3. **When did you last inject the failures your design claims to survive, and what broke that you did not expect?** Resilience patterns are hypotheses until you make the system fail on purpose: kill an instance, add latency to a dependency, drop a fraction of messages, redeliver a batch twice. In a distributed system the interesting failures are partial and intermittent, so a circuit breaker or saga compensation that looks correct in code can still misbehave under a real timeout-that-maybe-completed. Bring the results of an actual game day or fault-injection run, not a design doc, and note which alerts fired, how long tracing took to localize the fault, and whether any retry storm formed. In regulated sectors, evidence that you have tested failure is part of demonstrating operational resilience to auditors. If you have never run one, the first experiment belongs in a test environment with a tight blast radius and an abort switch.

4. **For each major data flow, can the owning team name the consistency model it provides, and does that choice match what the business actually needs?** CAP and PACELC force a deliberate choice per operation, yet in a large organization the default is drift: a flow that started eventually consistent for a low-stakes counter gets reused for something that now approves payments or grants access, and nobody re-examines the guarantee. The competing considerations are real, since strong consistency costs availability during a partition and latency even when there is none, while eventual consistency buys speed at the price of stale reads and conflict resolution you must design for. Bring a catalogue of your top data flows, each labelled with its current model (strong, causal, read-your-writes, or eventual) and the business consequence of a stale or lost read, then look for mismatches where the guarantee is stronger or weaker than the stakes warrant. In enterprise finance and in government benefit or identity systems, an eventually consistent read behind an authoritative decision is the kind of silent defect that surfaces as an audit finding or a wrongful denial months later, so the review itself is evidence auditors will ask to see.

5. **How do your multi-service business transactions behave halfway through, and who is accountable for the compensations that unwind them?** Replacing two-phase commit with sagas means the system passes through visible intermediate states, and a step can succeed while a later step fails and triggers a compensating action that reverses it. For a large team this raises hard ownership questions: the authorize-debit-credit-ledger chain often crosses several teams, and a compensation that one team forgets to implement leaves money or records permanently inconsistent. Weigh choreography, where services react to each other's events with no central controller and the flow is hard to see, against orchestration, where a coordinator drives and monitors the steps at the cost of a component to run. Bring the state diagram for your most important saga, the list of compensating actions and their owners, and evidence that "in-progress" and "compensated" states are handled in both the user experience and the audit trail. In banking and public-sector case management, regulators expect you to reconstruct exactly what happened to a transaction that failed midway, so an unmodelled intermediate state is a compliance gap, not just a bug.

6. **Do your message consumers survive duplicate and reordered delivery, and can you prove it before the broker forces the question?** Exactly-once delivery is a myth, so your real guarantee is at-least-once, and a consumer that assumes each message arrives once and in order will double-process the day the broker redelivers a batch after a failover. Across many teams the risk compounds, because one non-idempotent consumer on a shared stream can corrupt downstream state that other teams depend on, and the failure is invisible until replay or a partition reorders events. The trade-off is the engineering cost of idempotency keys, a processed-message log, and explicit offset and partition handling, set against the cost of silent corruption. Bring the list of consumers on your critical streams, note which deduplicate and which merely hope, and bring the result of an actual redelivery or replay test rather than an assurance that it should be fine. For inter-agency government data exchange and for enterprise event pipelines, the ability to replay a stream safely after a bug fix, without creating duplicate cases or charges, is both an operational necessity and something auditors will want demonstrated.

## Sector lens

**Startup.** With two or three moving parts and no platform team, resist building distributed machinery you cannot staff. Buy resilience where it lives in the SDK your payment or messaging provider already gives you, and spend your scarce attention on the two patterns that prevent irreversible harm: an idempotency key on every money-moving or account-changing call, and a timeout with bounded retry so a flaky connection never double-acts. Keep the number of network hops small, because every synchronous dependency you add is one more thing that can fail before you have anyone on call to notice.

**Small business.** You likely have no distributed-systems specialist and a tight budget, so treat this as a buy-not-build question: prefer managed queues, managed databases, and platforms that handle retries, ordering, and deduplication for you rather than infrastructure you must operate. Frame your risk in plain terms, knowing which operations would hurt a customer if they ran twice or returned stale data, and turn on the idempotency and at-least-once features your vendors already offer. Avoid stitching services together through a shared database to fake a transaction, since that quietly recreates the hardest distributed problem with none of the tools to manage it.

**Enterprise.** The core problem is consistency across many teams, so ship idempotency, timeouts, bounded retries, circuit breakers, and correlated tracing as shared platform defaults rather than letting each group hand-roll them. Standardize how consistency models and delivery guarantees are declared per flow, run fault injection and game days on a regular cadence, and make total time budgets compose across deep call chains so one service cannot retry the platform into an outage. Manage resilience as a measured capability with service-level objectives on user-visible symptoms, because at your scale a single missing timeout can cascade into a headline outage.

**Government.** Inter-agency systems mean no one owns the whole, so design for boundaries you do not control: durable queues with at-least-once delivery, deduplication on a stable message ID, and correlation IDs that flow across agency lines to give auditors an end-to-end trace. Procurement and transparency rules push you to document the consistency model and delivery guarantee of each integration, and to keep authoritative decisions (identity, eligibility, benefit) on strongly consistent reads rather than cached endpoints. Treat evidence of tested failure and reconstructable transaction history as deliverables, since operational resilience and accountability to the public are contractual and statutory obligations, not internal niceties.

## Examples

**Startup.** A small fintech startup has just two moving parts that talk over the network: its app and a third-party payment provider. Even at this size it makes every charge request carry an idempotency key and wraps the call in a retry with backoff, so a dropped response on a flaky connection never double-charges a customer. Skipping this feels cheap on day one, but the first duplicate charge that hits a real user costs a support fire, a refund, and a dent in trust the young company cannot spare.

**Enterprise.** A global ride-sharing platform processes trip payments through a saga: authorize card, debit rider, credit driver, record ledger entry, each a local transaction with a compensating reversal. Every step carries an idempotency key, so retries after a network timeout never double-charge. Calls to the fraud-scoring service sit behind a circuit breaker; when it degrades during peak, the breaker opens and trips fall back to a conservative score instead of blocking every ride. When a customer disputes a trip, distributed tracing lets engineers follow it across a dozen services in seconds.

**Government.** A national identity service is used by many agencies for verification. It offers a strongly consistent read for authoritative status checks (you must not approve a benefit against stale identity data), plus an eventually consistent, cached endpoint for high-volume, non-critical lookups. Inter-agency data exchange runs over a durable message queue with at-least-once delivery, and each agency's consumer deduplicates on a message ID, so a redelivered record does not create a duplicate case. Correlation IDs flow across agency boundaries, giving auditors an end-to-end trace of how a citizen's data moved between departments.

## Business case: motivations, ROI, and TCO

Distributed-systems discipline is bought cheaply and its absence is paid for catastrophically. The adoption cost is engineering time to build idempotency, timeouts, retries, circuit breakers, and tracing into shared libraries and platform defaults. That is a modest, mostly one-time investment that then benefits every team. The cost of *not* adopting it is measured in major outages: a single missing timeout that cascades into a full platform outage, a non-idempotent payment path that double-charges thousands of customers, or a saga-less distributed transaction that leaves data permanently inconsistent. Each of these is a headline incident with direct revenue, remediation, and reputational cost, and in regulated sectors, fines.

Frame the case to leadership around availability and blast radius. Resilience patterns directly reduce both the frequency and the duration of severe incidents, the metrics executives already track as uptime and mean-time-to-recovery. Distributed observability is the single largest lever on MTTR: teams with correlated tracing resolve cross-service incidents in a fraction of the time. Because these capabilities are best delivered as shared platform defaults, their per-team marginal cost is low and their organization-wide payoff compounds. The TCO argument is simple: building resilience in from the start is a fraction of the cost of retrofitting it after the outage that forces the issue.

## Anti-patterns and pitfalls

- **No timeouts.** A single hung dependency exhausts every thread and takes down the whole system.
- **Retrying non-idempotent operations.** Duplicate side effects: double charges, duplicate records, doubled emails.
- **Retry storms.** Synchronized retries without backoff and jitter that amplify a small blip into an outage.
- **Assuming exactly-once delivery.** Building consumers that break on duplicate messages the broker will eventually deliver.
- **Distributed transactions via shared database.** Coupling services through one database to fake ACID, recreating a distributed monolith.
- **Ignoring partial failure.** Code that assumes a remote call either fully succeeds or fully fails, with no handling for "timed out but maybe completed."
- **No correlation IDs.** Debugging a cross-service incident by grepping unrelated logs on ten machines.
- **Chatty synchronous call chains.** Deep synchronous dependency graphs where any one slow hop stalls the entire request.

## Maturity model

- **Level 1: Initiate.** Remote calls are treated like local calls. Timeouts are missing or naive, retries are absent or reckless, and failures cascade across the system. There is no shared view of consistency or delivery, and debugging a cross-service incident means per-machine log spelunking after the fact.
- **Level 2: Develop.** Some teams add timeouts and basic retries and a little idempotency, but the practices are inconsistent from service to service. Logs are centralized yet not correlated, so tracing a request across hops is manual. Distributed transactions are hoped to work rather than modelled, and consistency guarantees live in individual engineers' heads.
- **Level 3: Standardize.** Idempotency, bounded retries, backoff with jitter, circuit breakers, and bulkheads are standard across the organization via shared libraries. Sagas with compensating actions handle multi-service transactions, distributed tracing with correlation IDs is in place, and every major data flow documents its consistency model and delivery guarantee. The rules are written down and enforced org-wide rather than left to each team.
- **Level 4: Manage.** Resilience is measured against baselines, not just present. You track error rate, latency percentiles, saturation, and throughput per service and dependency, watch retry ratios and circuit-breaker open rates, and set service-level objectives on user-visible symptoms. Total time budgets are verified to compose across call chains, mean-time-to-recovery for cross-service incidents is a monitored metric, and fault-injection and game-day results feed the numbers that gate each change.
- **Level 5: Orchestrate.** Resilience is the continuously improved platform default, integrated across the whole organization and adaptive to conditions. Fault injection runs routinely in production with tight blast radii, systems degrade gracefully by design, and consistency and delivery choices are revisited as load and business stakes shift. The metrics from Level 4 drive automated responses and steady architectural evolution, so the distributed estate gets more robust with each incident rather than merely surviving it.

## Ideas for discussion

1. Which of your critical operations are genuinely idempotent today, and which quietly are not?
2. For each major data flow, can your team state the consistency model and the delivery guarantee from memory?
3. Where would a circuit breaker have prevented your last cascading outage?
4. How long does it currently take to trace a single failing request across all the services it touches?
5. Which of your "distributed transactions" are actually relying on luck, and which are true sagas with compensations?
6. If your message broker redelivered every message twice for an hour, what would break?

## Key takeaways

- Assume the network is unreliable and failures are partial; design every remote interaction for slowness, loss, duplication, and reordering.
- Decide consistency versus availability per operation using CAP/PACELC; document the model each flow provides.
- Idempotency, timeouts, bounded retries, and backoff-with-jitter are one package; never adopt retries without the other three.
- Circuit breakers and bulkheads contain failures; sagas with compensations replace unworkable distributed transactions.
- Treat delivery as at-least-once and make processing idempotent to achieve exactly-once effects.
- Correlated tracing, metrics, and logs are the only way to understand and operate distributed flows.

## References and further reading

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew Tanenbaum and Maarten van Steen, *Distributed Systems: Principles and Paradigms*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Sam Newman, *Building Microservices*
- Chris Richardson, *Microservices Patterns* (sagas, transactional messaging)
- Eric Brewer, "CAP Twelve Years Later" and Daniel Abadi on PACELC
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"
- Cindy Sridharan, *Distributed Systems Observability*
- Nassim Nicholas Taleb's notion of antifragility (as applied by resilience-engineering literature)
