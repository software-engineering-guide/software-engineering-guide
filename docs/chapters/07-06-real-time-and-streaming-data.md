# 7.6 Real-time and streaming data

## Overview and motivation

Most of what you know about data pipelines assumes the data holds still. You collect a day of records, run a job overnight, and read the results in the morning. Real-time and streaming data flips that assumption. Instead of processing a finished pile of data, you process an endless flow of events as they arrive, and you produce answers continuously. This is the difference between [batch processing](https://en.wikipedia.org/wiki/Batch_processing), which operates on a bounded, complete dataset, and [stream processing](https://en.wikipedia.org/wiki/Stream_processing), which operates on an unbounded, never-finished flow.

For large teams, streaming shows up the moment latency starts to matter to the business. A fraud decision that arrives an hour late is worthless. A personalization signal that lands tomorrow personalizes nothing. An operational dashboard that lags reality by a shift misleads the people watching it. Chapter 7.2 (data engineering) argues that you should choose batch by default and reach for streaming only where latency genuinely pays, and this chapter takes you the rest of the way: when real time earns its cost, and how to build it without setting fire to your operations budget. Streaming sits close to the event-driven messaging patterns in chapter 3.12 (event-driven architecture and messaging), the storage choices in chapter 3.4 (data architecture and storage), and the telemetry practices in chapter 9.2 (observability and telemetry).

Enterprise and government settings raise the stakes. A bank scores transactions for fraud in the time it takes a card reader to blink. A transit agency tracks vehicles and predicts arrivals for millions of riders. A benefits agency watches for anomalies in claims while keeping an auditable record of every decision. In all of these, the value comes from acting on data while it is still fresh, and the risk comes from acting on data that is wrong, incomplete, or impossible to reconstruct later. This chapter is opinionated about both.

## Key principles

- Reach for streaming only when latency has a clear business value; batch is cheaper and simpler.
- Distinguish bounded (finite) data from unbounded (never-ending) data, and design accordingly.
- Treat event time, not arrival time, as the source of truth, and plan for late and out-of-order data.
- Windows and watermarks are how you get finite answers from infinite streams.
- Prefer effectively-once results through idempotent sinks over fragile exactly-once promises.
- Stateful processing needs checkpointing so it can recover without losing or double-counting.
- Design for backpressure and reprocessing from day one, not as an afterthought.
- Keep streaming logic observable and auditable; a silent stream is worse than a failed batch.

## Recommendations

### Justify real time before you build it

The most important streaming decision is whether to stream at all. Real time roughly doubles your operational complexity and cost, because you trade a job that runs and stops for a system that must stay healthy every second. Before you commit, name the decision that fresh data enables and the cost of that decision arriving late. Fraud scoring, operational alerting, and live personalization usually clear the bar. A dashboard that a human looks at twice a day almost never does, no matter how satisfying "real-time" sounds in a planning meeting. Write down the latency requirement as a number, in seconds or minutes, and check it against reality. Much of what people call real time is served well by micro-batches that run every few minutes at a fraction of the cost.

### Design around event time, not processing time

The single hardest idea in streaming is that events happen at one moment and get processed at another. Event time is when the thing actually occurred, for example when a rider tapped a card. Processing time is when your system got around to handling it. These drift apart constantly: a phone loses signal in a tunnel and uploads three minutes of taps at once, a network hiccup reorders messages, a partition lags. If you compute on processing time, your numbers wobble with your infrastructure rather than reflecting the world. This late and out-of-order problem is the heart of the discipline, and it connects directly to the event modeling in [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture). Stamp every event with its event time at the source, carry that timestamp through the whole pipeline, and compute your results against it.

### Use windows and watermarks to get finite answers

An unbounded stream never ends, so "count the events" has no answer until you bound it. Windows do that bounding. Tumbling windows chop time into fixed, non-overlapping buckets, for example every minute. Sliding windows overlap, so a five-minute window that advances every minute gives you a smooth moving figure. Session windows group bursts of activity separated by gaps of inactivity, which suits user sessions well. Once you have windows, you need to decide when a window is done, because late data might still arrive. A watermark is the system's estimate that it has probably seen all events up to a given event time. When the watermark passes a window's end, you emit the result. Tune how long you wait: hold windows open longer and you tolerate more lateness at the cost of latency and memory, close them faster and you risk dropping stragglers. Decide explicitly what happens to data that arrives after a window closes, whether you drop it, log it, or emit a correction.

### Make sinks idempotent and prefer effectively-once

Delivery guarantees sound simple and are not. At-least-once delivery means every event is processed, but some may be processed more than once after a retry, so counts can inflate. Exactly-once sounds ideal but is expensive and, taken literally across arbitrary external systems, often impossible. The practical target is effectively-once: the observable result is as if each event were processed once, even if the machinery retried underneath. You get there by making your [idempotent](https://en.wikipedia.org/wiki/Idempotence) sinks safe to write to repeatedly, using deterministic keys and upserts so a replayed event overwrites rather than duplicates. Combine at-least-once delivery with idempotent writes and you get correct results without paying for heavyweight transactional coordination everywhere. Reserve true exactly-once machinery for the narrow places that genuinely need it.

### Checkpoint stateful processing so it can recover

Many useful streaming computations are stateful: running counts, joins across streams, deduplication, fraud models that remember recent behavior. That state lives in memory and would vanish when a process restarts. Checkpointing periodically snapshots the state and the stream position together, so after a crash the system resumes from a consistent point rather than replaying everything or losing its memory. Size your state deliberately, because unbounded state is a common way to run a streaming job out of memory in production. Use expiry and time-to-live on state you no longer need, and monitor state size as a first-class metric. Recovery time after a failure is a real service-level concern, so test it before your users do.

### Stream from operational databases with change data capture

You often want to react to changes in a database that was never designed to emit events. [Change data capture](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) solves this by reading the database's transaction log and turning every insert, update, and delete into a stream of change events. This is far better than polling the table on a timer, which is slow, misses intermediate states, and hammers the source. CDC lets you keep a search index, a cache, an analytics store, or a downstream service continuously in sync with a system of record, and it does so without invasive changes to the application. Treat the change stream as a first-class data product: version its schema, document its meaning, and watch its lag, because everything downstream inherits that lag.

### Prefer a streaming-first architecture over maintaining two codebases

The classic [Lambda architecture](https://en.wikipedia.org/wiki/Lambda_architecture) runs a batch layer for accurate, complete history alongside a speed layer for fresh, approximate results, then merges them. It works, but it makes you write and maintain the same business logic twice, in two systems, and reconcile the differences forever. The Kappa architecture collapses this: keep a durable, replayable log of events and run all processing as stream processing, reprocessing history by replaying the log when logic changes. The industry has drifted toward this streaming-first shape because a single codebase is dramatically cheaper to maintain and reason about. If you can express your batch needs as replays over a retained event log, you avoid the two-codebase tax entirely. Use log-based brokers that retain history so that reprocessing is a matter of rewinding, not rebuilding.

### Expose streams as SQL, materialized views, and real-time OLAP

Not everyone who needs streaming should have to write low-level stream processing code. Streaming SQL lets analysts and engineers express windows, joins, and aggregations in a language they already know, and it keeps the results continuously up to date as materialized views. For low-latency analytical queries over fresh data, a real-time [online analytical processing](https://en.wikipedia.org/wiki/Online_analytical_processing) (OLAP) store ingests the stream and answers slice-and-dice queries in milliseconds, which is what powers a genuinely live operational dashboard. Pair these with the product analytics practices in chapter 7.4 (product analytics and experimentation) when the goal is fast feedback on features and experiments. Choose these higher-level tools where they fit, and save hand-written stream processors for logic they cannot express.

### Plan for backpressure and reprocessing from the start

A stream can arrive faster than you can process it. Backpressure is the mechanism that lets a slow consumer signal upstream to slow down rather than falling over or dropping data silently. Make sure every stage in your pipeline honors it, and monitor consumer lag as a headline metric, because growing lag is the earliest warning that you are losing the race. Reprocessing is the other capability people wish they had built in. When you find a bug or change a rule, you want to replay history through the corrected logic. That is only possible if your event log retains enough history and your sinks are idempotent enough to absorb the replay. Design both in from day one; retrofitting them under incident pressure is miserable.

## Trade-offs: pros and cons

| Choice | Pros | Cons | Best fit |
| --- | --- | --- | --- |
| Batch | Simple, cheap, easy to test and backfill | High latency, stale between runs | Reporting, most analytics |
| Micro-batch (minutes) | Near-real-time, far simpler than streaming | Not truly instant | "Real-time" dashboards |
| True streaming (sub-second) | Instant reaction, continuous results | Complex, costly, hard to test | Fraud, alerting, live personalization |
| At-least-once + idempotent sink | Correct results, affordable, resilient | Requires disciplined key design | Most streaming pipelines |
| Exactly-once machinery | Strong guarantee end to end | Expensive, limited across systems | Narrow high-stakes paths |
| Lambda (batch + speed) | Accurate history plus fresh view | Two codebases to maintain | Legacy migrations |
| Kappa (streaming-first) | One codebase, replayable | Needs retained, durable log | New streaming platforms |

The central tension is latency against complexity. Every step toward real time costs you in operational burden, testing difficulty, and money, and the returns are not linear: going from daily to every-few-minutes is cheap and often enough, while going from minutes to sub-second is where the expense concentrates. Resolve the tension by pricing the decision, not the technology. Ask what action the freshness enables and what lateness costs, then buy only as much latency reduction as that action justifies. When you do need streaming, lean on at-least-once delivery with idempotent sinks and a streaming-first log, because that combination gives you correctness and replayability without the heaviest guarantees.

## Questions to discuss with your team

1. **What decision does real-time data actually enable for us, and what does it cost when that data arrives a minute late instead of instantly?** This is the question that should gate every streaming project, because streaming roughly doubles your operational cost and complexity compared to batch. A large team can burn quarters building a real-time platform that serves dashboards a human checks twice a day, which is money set on fire. Bring the concrete action the data drives, whether that is blocking a fraudulent transaction, paging an operator, or changing what a user sees, and put a number on the cost of latency for each. If the honest answer is that a five-minute micro-batch would serve the need, that is a finding worth celebrating, not hiding. The answer should directly change whether you build true streaming, settle for micro-batches, or stay in batch.

2. **How do we handle late and out-of-order events, and what happens to data that arrives after a window closes?** Late and out-of-order data is the hard part of streaming, and teams that skip this question discover it in production when their numbers refuse to reconcile. The competing pressures are latency and correctness: hold windows open longer to catch stragglers and you delay every result and consume more memory, close them faster and you silently drop real data. Bring evidence about how late your data actually arrives, measured as the gap between event time and processing time across your sources, since a mobile source in tunnels behaves very differently from a server-side event. Decide explicitly whether late data is dropped, logged, or triggers a correction, and make sure everyone downstream knows which. In a government context where figures must be defensible, silently dropping late events can be a compliance problem, so the policy needs to be deliberate and documented.

3. **Are our sinks idempotent enough that we can safely replay history, and does our event log retain enough to make replay possible?** Reprocessing is the capability teams most often wish they had built in and most often did not, and it depends on two things working together: idempotent sinks that absorb replayed events without duplicating, and a durable log that retains enough history to replay from. Without both, fixing a logic bug means you cannot cleanly recompute the affected period, and you are stuck patching numbers by hand under pressure. Bring your current retention window and a concrete test: pick a real bug from the last quarter and ask whether you could have replayed the corrected logic over the affected data. The pull against this is cost, since retaining history and designing idempotent writes takes storage and discipline upfront. But the alternative surfaces at the worst possible moment, during an incident, so the answer shapes how much you invest in replayability before you need it.

## Examples

**Startup.** A consumer app wants to show users a live activity feed and flag suspicious logins as they happen. The team resists standing up a heavy streaming platform. They put events on a single retained log-based broker, run a lightweight stream processor for the login-risk logic, and feed a real-time OLAP store that powers the activity feed. Every sink is keyed and idempotent, so an at-least-once retry never double-counts. When they later find a bug in the risk rule, they simply replay the log through the fixed logic overnight, because they kept a week of history and never needed a second batch codebase.

**Enterprise.** A retail bank scores every card transaction for fraud within the authorization window, joining the live transaction stream against a stateful model of recent account behavior. Checkpointing lets the scoring service recover from a node failure in seconds without losing its memory of the last few minutes. Separately, change data capture streams updates from the core banking database into a search index and a personalization service, keeping both fresh without polling. Operational dashboards read from a real-time OLAP store so risk and operations teams watch the business as it moves, and the whole pipeline emits the lag and throughput telemetry described in chapter 9.2.

**Government.** A metropolitan transit authority ingests vehicle positions and fare taps to predict arrivals and monitor crowding in real time, feeding both public apps and an operations center. Because riders in tunnels upload taps in delayed bursts, the team computes ridership on event time with watermarks tuned to the observed lateness, and logs any event that arrives after its window closes rather than dropping it silently. Every processed event is retained in an auditable log so that ridership figures reported to oversight bodies can be reconstructed exactly. When a fare rule changes, they replay the affected period through the corrected logic and produce a defensible restatement.

## Business case: motivations, ROI, and TCO

The return on real-time data comes from acting while action still matters. Fraud caught during authorization prevents a loss that a nightly batch would only report. Personalization that responds within a session lifts conversion in a way that tomorrow's recommendation cannot. Operational monitoring that reflects the present lets you intervene before a small problem becomes an outage or a public incident. In each case, the value is the delta between acting now and acting later, and that delta is what you should quantify when you make the case.

The total cost of ownership is higher than batch, and honesty about that protects your credibility. You pay for always-on infrastructure, for engineers who understand event time, watermarks, state, and delivery semantics, and for the harder testing and on-call burden of a system that must stay healthy continuously rather than run and stop. A streaming-first architecture on a retained log lowers ongoing cost by sparing you a duplicate batch codebase, and choosing at-least-once with idempotent sinks avoids the expense of end-to-end exactly-once machinery. The most expensive mistake is building real time where micro-batch or batch would do, so the strongest cost argument is often a decision not to stream. Frame the pitch to leadership around specific latency-sensitive decisions and their measurable payoff, and be equally clear about where staying in batch saves money with no loss of value.

## Anti-patterns and pitfalls

- Building streaming for prestige when a micro-batch every few minutes would meet the need.
- Computing on processing time, so your numbers wobble with your infrastructure instead of the world.
- Ignoring late and out-of-order data until reconciliation fails in production.
- Chasing literal exactly-once everywhere instead of at-least-once with idempotent sinks.
- Unbounded state with no expiry, quietly growing until a job runs out of memory.
- No checkpointing, so a restart loses state or forces a full replay.
- Polling operational databases on a timer instead of using change data capture.
- Maintaining a Lambda batch layer and speed layer with duplicated, drifting logic.
- A retention window too short to replay history when you find a bug.
- Streams with no lag, throughput, or freshness metrics, failing silently.

## Maturity model

- **Level 1, Initial:** Everything is batch, or a few hand-built streaming jobs run without monitoring. Numbers are computed on processing time, late data is ignored, and a restart loses state. Nobody can replay history to fix a bug.
- **Level 2, Managed:** Core streaming pipelines run on a log-based broker with checkpointing. The team distinguishes event time from processing time and uses basic windows. Delivery is at-least-once, though not all sinks are idempotent, and lag is watched informally.
- **Level 3, Defined:** Event time, watermarks, and an explicit late-data policy are standard. Sinks are idempotent for effectively-once results, state has expiry, and change data capture feeds downstream systems. A retained log supports replay, and lag, throughput, and freshness are monitored with alerts.
- **Level 4, Optimizing:** A streaming-first architecture serves both fresh and historical needs from one replayable log. Streaming SQL, materialized views, and real-time OLAP make fresh data broadly accessible. Reprocessing is routine and tested, state and cost are actively managed, and every stream is observable and auditable end to end.

## Ideas for discussion

1. Where in your stack does "real-time" actually earn its cost, and where is it an unexamined wish?
2. How large is the gap between event time and processing time across your sources, and do you measure it?
3. Could you collapse a Lambda batch-and-speed setup into a single streaming-first codebase, and what would block it?
4. Which of your sinks are truly idempotent, and could you safely replay last quarter's data through corrected logic today?
5. What is your policy for data that arrives after a window closes, and does everyone downstream know it?
6. How would change data capture change the way you keep search, caches, and analytics in sync?

## Key takeaways

- Reach for streaming only when a latency-sensitive decision pays for it; batch and micro-batch are cheaper defaults.
- Compute on event time, and treat late and out-of-order data as the core problem, handled with windows and watermarks.
- Prefer at-least-once delivery with idempotent sinks for effectively-once results over literal exactly-once everywhere.
- Checkpoint stateful processing, bound your state, and monitor consumer lag as a headline metric.
- Use change data capture to stream from operational databases instead of polling.
- Favor a streaming-first architecture on a retained, replayable log over maintaining two codebases.
- Expose streams through streaming SQL, materialized views, and real-time OLAP, and keep every stream observable and auditable.

## References and further reading

- Tyler Akidau, Slava Chernyak, and Reuven Lax, "Streaming Systems."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Jay Kreps, "Questioning the Lambda Architecture" (O'Reilly Radar).
- Fabian Hueske and Vasiliki Kalavri, "Stream Processing with Apache Flink."
- Ben Stopford, "Designing Event-Driven Systems."
- Tyler Akidau and colleagues, "The Dataflow Model" (VLDB paper on windowing and watermarks).
