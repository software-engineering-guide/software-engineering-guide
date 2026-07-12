# 2.17 Concurrency and parallelism

## Overview and motivation

[Concurrency](https://en.wikipedia.org/wiki/Concurrency_(computer_science)) is the art of structuring a program as independent tasks that can make progress without waiting for each other. [Parallelism](https://en.wikipedia.org/wiki/Parallel_computing) is actually executing those tasks at the same instant on multiple processors. The distinction is not pedantic. Concurrency is a way to organize code so that a slow network call does not freeze the whole program; parallelism is a way to finish a large computation faster by spreading it across cores. Confusing the two leads teams to add threads hoping for speed and receive only bugs.

For large teams, this topic matters because concurrency is where correctness quietly dies. A single author writing single-threaded code can reason about it line by line, but the moment many authors share memory across threads, the number of possible interleavings explodes, and a program that passes every test can still fail one time in a million under production load, not with a loud crash but with corrupted data, hung requests, and incidents no one can reproduce. This chapter builds on the code-level focus of chapter 2.16 (performance engineering) and the computing foundations of chapter 2.13, and it feeds into the coordination problems of chapter 3.3 (distributed systems), which is concurrency across machines with the added cruelty of an unreliable network.

For enterprises, concurrency bugs are throughput bugs. High-traffic services live or die on their ability to handle thousands of simultaneous requests without racing on shared state, and a single unsynchronized counter can corrupt a ledger under load. For government, the stakes are correctness and auditability in systems that run for decades and touch safety, benefits, or public records. A race in a tax or health system is not an inconvenience; it is a wrong answer that someone must later explain to an oversight body. In both settings the goal is the same: make the safe path the default, so that the many people who touch the code do not each have to be a concurrency expert.

## Key principles

- **Concurrency is structure; parallelism is execution.** Decide which one you actually need before you reach for threads.
- **Shared mutable state is the enemy.** Almost every concurrency bug traces back to two tasks touching the same changeable data.
- **Prefer immutability and message passing.** Data that cannot change cannot be raced on, and messages beat shared memory for safety.
- **Non-determinism is the core difficulty.** The bug that appears one run in a thousand is the whole problem, not an edge case.
- **Bound everything.** Unbounded queues, thread counts, and work in flight turn a spike into an outage.
- **Higher-level models beat raw locks.** Actors, channels, and structured concurrency give many authors a safe default, and every lock has a cost.
- **Test the interleavings, not just the happy path.** Deterministic tests cannot catch a bug that only a rare ordering reveals.

## Recommendations

### Decide whether you need concurrency or parallelism

Start by naming the problem. If your service spends most of its time waiting (on databases, network calls, or disk), you have an I/O-bound workload, and concurrency is the answer: structure the code so that while one request waits, others proceed. A single thread with async/await, or a small pool, can serve thousands of waiting requests. If instead your program is CPU-bound, grinding through computation with little waiting, then parallelism across cores is what buys speed, and here the ceiling is set by Amdahl's law (see chapter 2.16): the serial fraction caps your speedup no matter how many cores you add. Measure which regime you are in before you design.

### Treat shared mutable state as the enemy

Nearly every concurrency defect reduces to the same shape: two tasks read and write the same changeable data without agreeing on an order. This is a [race condition](https://en.wikipedia.org/wiki/Race_condition), and it produces lost updates, half-written objects, and values that violate invariants the code assumed were safe. The most reliable defence is to have less shared mutable state. Give each task its own data, pass copies rather than references, and confine mutable state to a single owner that others reach through messages. When you genuinely must share, make the sharing explicit and small, so a reviewer can see every place the state is touched.

### Prefer immutability and message passing as defaults

The safest shared data is data that cannot change. An [immutable object](https://en.wikipedia.org/wiki/Immutable_object), once constructed, can be read by any number of threads with zero synchronization, because there is nothing to race on. Make immutability your default and mutability the deliberate exception. When tasks must coordinate, prefer message passing over shared memory: rather than share a common variable, have one task send the value to the other, which is the philosophy behind the Go proverb "do not communicate by sharing memory; share memory by communicating." Message passing turns invisible, order-dependent bugs into explicit, inspectable data flow, and that clarity is almost always worth its per-message cost in code that many people maintain.

### Reach for higher-level models before raw locks

Hand-written locking is correct in principle and disastrous in practice, because humans are bad at reasoning about every interleaving. Prefer models that make safe concurrency the default. The [actor model](https://en.wikipedia.org/wiki/Actor_model) gives each actor private state and a mailbox: actors never share memory and only send messages, so whole classes of race disappear. [Communicating sequential processes](https://en.wikipedia.org/wiki/Communicating_sequential_processes) (CSP), the model behind channels in languages like Go, has independent processes pass values over typed channels. Structured concurrency ties the lifetime of concurrent tasks to a lexical scope, so tasks cannot outlive the block that spawned them and errors propagate instead of vanishing. Async/await lets you write concurrent, I/O-bound code in a sequential style. Each of these raises the floor for the average author, which is what a large team needs.

### Understand your memory model, atomicity, and visibility

When you do share memory, two properties bite. **Atomicity** means an operation happens all at once or not at all; a plain increment (`x = x + 1`) is not atomic, because it reads, adds, and writes as three steps that another thread can interrupt, which is how counters lose updates. **Visibility** means that a write by one thread becomes observable to another; without proper synchronization, a value written on one core may sit in a cache unseen by another, so a thread can loop forever on a flag that was already set. The memory model of your language defines when writes become visible and what orderings the compiler and CPU may rearrange, so you cannot assume code runs in the order you wrote it. Use the language's atomic types and synchronization primitives rather than inventing your own lock-free scheme.

### Use synchronization primitives deliberately, and design against deadlock

When sharing is unavoidable, reach for the right primitive and respect its price. A lock or mutex (mutual exclusion) lets one thread at a time enter a critical section, but serializes access, so a hot lock becomes a bottleneck that erases the benefit of many cores. A semaphore limits how many tasks may proceed at once, which is how you bound a pool. Atomic operations offer lock-free updates for simple values like counters, cheaper than a lock but easy to misuse for anything compound. Locks bring three classic failure modes. A [deadlock](https://en.wikipedia.org/wiki/Deadlock) is when tasks wait on each other in a cycle and none can proceed, the textbook case being two threads each holding one lock and wanting the other. A **livelock** is when tasks keep reacting to each other but make no progress. **Starvation** is when a task never gets a resource because others keep jumping ahead. The disciplines that prevent these are concrete: impose a global lock ordering, hold locks briefly, add timeouts so a stuck task fails loudly, never call unknown code while holding a lock, and use fair scheduling where starvation is a risk. Write these rules down, because a new author cannot rediscover them from the code alone.

### Bound your queues, pools, and work in flight with backpressure

An unbounded queue is a time bomb. Under a traffic spike, work arrives faster than it drains, the queue grows without limit, memory fills, and the service dies in a way that looks like a mysterious out-of-memory crash rather than the overload it is. Bound every queue, cap every thread pool, and apply [backpressure](https://en.wikipedia.org/wiki/Back_pressure): when the system is full, signal upstream to slow down or reject work fast rather than accepting infinite work you cannot finish. Size pools to the workload (roughly the core count for CPU-bound work, higher for I/O-bound work where threads mostly wait), and treat the bound as a deliberate capacity decision. This connects to the resilience patterns of chapter 3.3.

### Use data parallelism where the work is embarrassingly parallel

Some problems split cleanly: apply the same operation to every element of a large dataset, with no element depending on another. This data parallelism is the friendliest kind, because there is little shared state to race on and the speedup can approach the core count, as map-reduce pipelines, parallel array operations, and vectorized numeric code all show. Even here, respect Amdahl's law: the merge or reduce step is often serial and caps your gain, and the overhead of splitting can dominate for small inputs. Reach for it when the per-element work is substantial and the elements are truly independent; otherwise the simplest sequential version is often both fast enough and far easier to keep correct, a point the construction practices of chapter 2.9 reinforce.

### Test and debug non-deterministic code on purpose

Concurrency bugs are non-deterministic, so ordinary tests, which run one interleaving, mostly miss them. Attack the problem deliberately with stress and fuzz tests that run many tasks under randomized timing to shake out rare orderings. Reach for race detectors and thread sanitizers, tooling that instruments memory access to catch data races even when the buggy interleaving did not happen this run. Where your platform offers it, use deterministic simulation or controlled schedulers that replay a specific interleaving, turning a heisenbug into a reproducible one, and design so that a production hang lets you capture thread states and lock ownership, which ties into the debugging discipline of chapter 2.15. Above all, prefer designs (immutability, message passing, single ownership) that make whole categories of these bugs impossible, because a bug you cannot create is one you never have to debug.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Shared memory with locks | Fast per operation; familiar | Race, deadlock, and visibility bugs; hard for many authors to keep correct |
| Immutability | No synchronization needed; trivially thread-safe reads | Copying cost; awkward for large mutable structures |
| Message passing (actors, channels) | Explicit data flow; whole bug classes vanish | Per-message overhead; can hide backpressure if queues are unbounded |
| Async/await | Cheap concurrency for I/O-bound work; sequential-looking code | No parallelism for CPU work; blocking a task stalls others |
| Structured concurrency | Clear task lifetimes; errors propagate; no leaked tasks | Newer, less available in some ecosystems |
| Data parallelism | Near-linear speedup on independent work | Amdahl ceiling; overhead dominates small inputs |
| Atomics / lock-free | No lock contention for simple values | Extremely easy to get subtly wrong; hard to review |

The central tension is safety versus raw speed, and the resolution is to buy correctness first and spend performance only where measurement proves you must. Raw shared-memory locking is the fastest per operation and the most dangerous per line of code; higher-level models cost a little throughput and return a great deal of safety and clarity, and for code maintained by many hands that trade is decisively worth making. Reserve hand-tuned lock-free concurrency for the small hot spots where a profiler (chapter 2.16) proves the coordination overhead matters, and keep even those behind a well-tested boundary.

## Questions to discuss with your team

1. **For your busiest service, is the workload I/O-bound or CPU-bound, and does your concurrency design match?** Teams routinely add thread pools to services that spend 95% of their time waiting on a database, gaining contention but no throughput, or they try to parallelize a computation whose serial fraction caps any speedup. The right design follows from the regime: async or a small pool for waiting-heavy work, real parallelism across cores for compute-heavy work. Bring a profile that shows where time actually goes, not an assumption, and if most time is spent computing, measure the serial fraction and let Amdahl's law tell you the ceiling. The answer shapes whether you reach for async, a bounded pool, or data parallelism.

2. **What is your team's default for sharing state across tasks, and is it safe by construction?** On a large team, the default matters more than the exceptions, because most code is written by people who are not concurrency specialists and who copy whatever pattern is already there. If the default is shared mutable objects guarded by ad hoc locks, you are one forgotten lock away from a race that surfaces months later in production. If the default is immutability and message passing, whole categories of bug never occur, and the rare place that truly needs shared memory stands out for careful review. Discuss what a new engineer would reach for today, whether your reviews would catch an unsynchronized write, and how to make the safe path the easy one.

3. **How would you find, reproduce, and fix a concurrency bug that appears once in a million requests in production?** The honest answer for many teams is that they could not, because the bug vanishes when they look and their tests only ever run one benign interleaving. That should worry you, because these bugs corrupt data silently and erode trust. Talk about whether you run race detectors and thread sanitizers in continuous integration, whether you stress test with randomized timing, and whether your production observability captures thread and lock state at the moment of a hang. The best teams answer by making most such bugs impossible through their choice of model, so the residual few are rare and contained.

4. **Where in your system does an unbounded queue or an uncapped thread pool still exist, and what happens to it under a sudden tenfold spike?** This matters because unbounded work in flight is the failure that masquerades as a mysterious out-of-memory crash: work arrives faster than it drains, memory fills, and the service dies looking like a hardware fault rather than the overload it is. The competing considerations are real, because a bound you set too low rejects legitimate traffic and a bound too high defers the crash instead of preventing it, so the number is a capacity decision, not a guess. Bring an inventory of every queue and pool, its current bound (or the admission that it has none), the backpressure behaviour when it fills, and load-test evidence of how the system degrades at the edge. For an enterprise fleet a single unbounded queue can cascade into a fleet-wide outage, and for a government platform that must stay available to citizens, graceful rejection with a clear error is a service obligation, so the bound and its rejection path belong in the capacity plan and the runbook, not in one engineer's memory.

5. **What is your team's policy for using higher-level concurrency models versus hand-written locks, and where have you allowed exceptions?** The default model decides how safe the average change is, because most authors are not concurrency specialists and will copy whatever pattern already exists: actors, channels, and structured concurrency raise the floor for everyone, while raw locking is correct in theory and a source of deadlocks in practice. The tension is that higher-level models cost a little per-message or per-task overhead, and a profiler will occasionally prove that a hot path needs hand-tuned lock-free code, so a blanket ban is as wrong as a free-for-all. Bring the list of places you have reached below the safe default, the profiling evidence that justified each one, and how each exception is fenced behind a tested boundary and a documented lock ordering. In a large enterprise this policy is what keeps thousands of contributors from each reinventing an unsafe scheme, and in a long-lived government system it is what lets a reviewer years later understand why a dangerous pattern was allowed and confirm it is still warranted.

6. **When you decide to parallelize a computation, how do you measure the serial fraction, and who is accountable for confirming the speedup is real?** Teams routinely spread a computation across cores and celebrate a number that a profiler would never confirm, because Amdahl's law caps the gain at the reciprocal of the serial fraction no matter how many cores you add, and the split-and-merge overhead can erase the benefit entirely for small inputs. The competing pull is that parallelism adds real complexity and new race surface, so the question is whether the measured speedup justifies the correctness risk you are taking on. Bring a profile that isolates the serial portion, the input sizes where parallelism actually wins, and a before-and-after benchmark on representative hardware rather than a hopeful estimate. For an enterprise paying for a large compute fleet, an honest serial-fraction analysis turns into hardware spend saved or wasted, and for a government body answerable for the cost of a public system, the person who signed off on the parallel design should be able to show the measurement that justified it under audit.

## Sector lens

**Startup.** With a tiny team and no runway to spare, buy correctness with structure, not with a concurrency specialist you cannot hire. Reach for the single safe default your language gives you, async/await for I/O-bound work, one owning task or an actor for any shared state, and skip hand-tuned locking entirely. A lost-update race in a payments path can sink you faster than a missed feature, so spend the small amount of extra code to make that class of bug impossible and move on.

**Small business.** You have no one whose job is concurrency, so favour platforms and managed services that handle it for you: a database transaction, a hosted queue, or a framework's request model beats threads you maintain by hand. When you evaluate a tool, treat "does this make concurrency safe by default" as a buy-versus-build question, and prefer the option where a wrong interleaving cannot silently corrupt a customer's record. Keep shared mutable state out of your own code wherever a bounded, managed service can hold it instead.

**Enterprise.** Across many teams the goal is a house default that keeps thousands of contributors safe: immutability and message passing as the norm, higher-level models over raw locks, bounded queues and pools with backpressure, and a documented global lock ordering. Encode these in engineering standards, enforce them with race detectors and stress tests in CI, and govern the exceptions where a profiler justified lock-free code so each one stays behind a tested, reviewed boundary. Manage concurrency capacity as a fleet-wide concern with queue bounds and pool sizes tied to measured load.

**Government.** Correctness and auditability in systems that run for decades outrank raw throughput. Demand that every state transition be recorded and replayable, so a suspected race can be reproduced and the fix proven to an oversight body, and keep AI-free deterministic paths for decisions that touch benefits, safety, or public records. Procurement should require that vendors disclose their concurrency model and evidence of race-detector and stress-test coverage, because a wrong answer under load in a public system is not an inconvenience, it is something an accountable officer must later explain.

## Examples

**Startup.** A small team ships a payments feature and notices that account balances occasionally drift by a few cents under load. The cause is a plain read-modify-write on a balance field from concurrent request handlers, a lost-update race. Rather than sprinkle locks, they move each account's balance behind a single owning task that processes debits and credits as messages, one at a time. The drift disappears, the code becomes easy to reason about, and they add a stress test that fires thousands of concurrent transfers to guard the fix. One structural change, an entire class of bug retired.

**Enterprise.** A high-throughput order service handling tens of thousands of requests per second suffers periodic latency spikes and occasional out-of-memory crashes during traffic surges. Investigation finds an unbounded work queue behind a thread pool that grows without limit once demand exceeds capacity. The team bounds the queue, caps the pool at a size tied to core count, and adds backpressure that rejects excess load quickly with a clear error. Throughput becomes predictable, the crashes stop, and a hot lock on a shared cache is replaced with a lock-free structure only after a profiler proves the contention is real. Safe defaults for the many authors, tuned concurrency only where measured.

**Government.** A national benefits platform runs for decades and must produce auditable, correct results even under concurrent case updates. The team chooses immutability and message passing as the house default, confines every piece of mutable state to a single owner, and imposes a global lock ordering wherever locks remain, all written into the engineering standards. They run thread sanitizers and randomized stress tests in the pipeline, and design so that every state transition is recorded and replayable for oversight, which lets them reproduce and prove the fix when a rare interleaving is suspected. Correctness and auditability are treated as first-class requirements, not performance afterthoughts.

## Business case: motivations, ROI, and TCO

The return on disciplined concurrency shows up as incidents that never happen. A single production race can corrupt data across thousands of records, and the cost includes both the engineering hours to find a bug that hides when observed and the far larger cost of reconciling bad data, notifying affected users, and rebuilding trust. These are among the most expensive defects to diagnose precisely because they are non-deterministic, so chasing one heisenbug can dwarf the effort of choosing a safe model up front.

The upside also shows up as throughput and cost. Right-sizing concurrency lets a service handle far more load on the same hardware, a recurring saving for a large fleet, while backpressure and bounded queues prevent the cascading outages that turn a traffic spike into a public incident. The total cost of ownership is modest and mostly cultural: you invest in a house style (immutability, message passing, structured concurrency), in tooling (race detectors, thread sanitizers, stress harnesses in CI), and in standards that encode lock ordering and bounding. The alternative is a codebase where correctness depends on every author being an expert forever, which no growing team can sustain. Make the case to leadership in their units: translate a prevented race into data-corruption incidents avoided, backpressure into outages prevented, and a safe default into onboarding time saved.

## Anti-patterns and pitfalls

- **Adding threads for speed on I/O-bound work.** More threads on a waiting-heavy service buy contention, not throughput.
- **Shared mutable state everywhere.** Any thread mutating any object makes correctness a matter of luck no reviewer can verify.
- **Unbounded queues and pools.** A spike grows the queue until memory dies; the crash looks mysterious but is plain overload.
- **Ad hoc locking without a global order.** Locks taken in different orders across the codebase deadlock under load.
- **Assuming code runs in written order.** Ignoring the memory model, so a visibility bug leaves a thread spinning on a stale value.
- **Hand-rolled lock-free cleverness.** Custom lock-free schemes are almost always subtly wrong and nearly impossible to review.
- **Testing only the happy interleaving.** Deterministic tests pass while the one-in-a-million ordering corrupts production.
- **Calling unknown code while holding a lock.** A callback that blocks or re-enters turns a critical section into a deadlock.

## Maturity model

- **Level 1, Initiate:** Concurrency is ad hoc and reactive. Threads and locks are added by instinct, shared mutable state is everywhere, and queues are unbounded. Race conditions surface as unreproducible production incidents no one can diagnose, and no tooling exists to catch them.
- **Level 2, Develop:** Some teams have learned basic practices: they use locks with more care and bound their most obvious queues. There is informal awareness of races and deadlocks, and a few critical paths get extra scrutiny. Practice is inconsistent across teams, testing is still mostly single-interleaving, and safe patterns live in individuals rather than in writing.
- **Level 3, Standardize:** The organization has a documented house style enforced org-wide: immutability and message passing as defaults, higher-level models over raw locks, bounded queues and pools with backpressure, and a documented global lock ordering. Race detectors and stress tests run in CI, and concurrency choices follow from whether work is I/O-bound or CPU-bound.
- **Level 4, Manage:** The organization measures and controls its concurrency posture against baselines. It tracks race-detector and thread-sanitizer coverage across services, records queue depth, lock-wait time, pool saturation, and rejection rates as monitored metrics, and load-tests the degradation curve so every bound is a data-backed capacity decision. Concurrency incidents are counted and trended, serial fractions of parallelized workloads are measured against the speedup actually achieved, and go or no-go decisions on new designs rest on that evidence rather than on instinct.
- **Level 5, Orchestrate:** Safe concurrency is the path of least resistance for every author, and the practice is continuously improved and integrated across the organization. Whole bug classes are impossible by construction, hot spots are tuned only where profiling proves it, and deterministic replay makes the rare residual bug reproducible. Correctness and auditability are continuously defended properties, capacity bounds adapt to observed load, and the standards evolve as the platform and the workload shift.

## Ideas for discussion

1. If you audited your busiest service today, how much of its state is shared and mutable, and how much of that sharing is truly necessary?
2. What is your team's default answer when someone needs two tasks to coordinate, and would you rather it were immutability or message passing?
3. Where do unbounded queues or uncapped pools still hide in your system, and what would happen to them under a sudden tenfold traffic spike?
4. Do your continuous integration runs include a race detector or thread sanitizer, and when did one last catch something before production?
5. For your most parallelized workload, what is the serial fraction, and does Amdahl's law cap the speedup you are actually chasing?
6. Could your team reproduce a one-in-a-million interleaving bug on demand, and what would it take to get there?

## Key takeaways

- Concurrency structures a program as independent tasks; parallelism executes them at once. Decide which you need before adding threads.
- Shared mutable state is the root of nearly every concurrency bug; prefer immutability and message passing as safe defaults for many authors.
- Reach for higher-level models (actors, channels, structured concurrency, async/await) before hand-written locks, which are correct in theory and dangerous in practice.
- Understand atomicity, visibility, and your memory model; use the right primitive, hold locks briefly, and impose a global lock order to avoid deadlock, livelock, and starvation.
- Bound every queue and pool and apply backpressure, so a spike degrades gracefully instead of crashing (chapter 3.3).
- Test the interleavings on purpose with race detectors, stress tests, and replay (chapter 2.15), and respect Amdahl's law when parallelizing (chapter 2.16).
- For enterprises this is throughput and prevented incidents; for government it is correctness and auditability in long-lived systems.

## References and further reading

- Brian Goetz et al., *Java Concurrency in Practice* (atomicity, visibility, the memory model, and safe publication).
- Herb Sutter, "The Free Lunch Is Over" (why software must embrace concurrency as clock speeds plateau).
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (ordering and the foundations of concurrent reasoning).
- C. A. R. Hoare, "Communicating Sequential Processes" (*Communications of the ACM*, 1978): the CSP model behind channels.
- Carl Hewitt, Peter Bishop, and Richard Steiger, "A Universal Modular Actor Formalism for Artificial Intelligence" (the origin of the actor model).
- Edsger W. Dijkstra, "Cooperating Sequential Processes" (semaphores, mutual exclusion, and the deadlock problem).
- Maurice Herlihy and Nir Shavit, *The Art of Multiprocessor Programming* (locks, atomics, and lock-free data structures).
- Nathaniel J. Smith, "Notes on Structured Concurrency, or: Go Statement Considered Harmful" (the case for structured concurrency).
- Martin Kleppmann, *Designing Data-Intensive Applications* (concurrency and consistency where memory meets distributed systems).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
