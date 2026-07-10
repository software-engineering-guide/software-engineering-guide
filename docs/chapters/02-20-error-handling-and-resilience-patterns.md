# 2.20 Error handling and resilience patterns

## Overview and motivation

Every program you write will fail. A disk fills, a network drops, a service times out, a caller passes garbage, a dependency returns something the docs never mentioned. The question is never whether failure happens; it is whether your code meets that failure with a plan or with a surprise. Error handling is the craft of deciding, line by line and function by function, what your code does when the world does not cooperate. It is the least glamorous part of construction and the part that decides, more than any feature, whether people trust your system.

This chapter is about resilience at the code and component level: the choices inside a function, a module, or an API. It complements chapter 3.5, which covers resilience at the system level (load balancing, replication, failover across services). Chapter 3.5 keeps the whole platform standing when a region goes dark; this chapter keeps a single request from corrupting your data or vanishing without a trace. The two reinforce each other. A circuit breaker in your architecture means little if the code behind it swallows exceptions, and a defensive function cannot save you if the surrounding system has no redundancy. This chapter also builds on chapter 2.9 (software construction), where handling errors was one discipline among many; here it becomes the whole subject.

For large teams, consistency is the prize. When hundreds of engineers handle errors hundreds of different ways, every service becomes a puzzle and every incident an excavation. In enterprise settings, that inconsistency raises the cost of every audit and every integration. In government and other high-stakes systems, the stakes are sharper: correctness, safe failure, and a clear audit trail are not features you add later but properties the system must have from the first commit. A benefits system that silently miscalculates, or a records system that loses a failure without logging it, is not merely buggy. It is untrustworthy in a way that erodes the institution behind it.

## Key principles

- Tell errors, faults, and failures apart, and handle each at the right layer.
- Choose fail-fast or fail-safe deliberately, per context, never by accident.
- Make the error-handling contract of every function and API explicit and honest.
- Validate at boundaries; trust within them; defend without paranoia.
- Never silently swallow an error; surface it, wrap it, or handle it on purpose.
- Make retries safe with idempotence, timeouts, backoff, and jitter.
- Give the error path the same design attention as the happy path.

## Recommendations

### Distinguish errors, faults, and failures

Sloppy vocabulary produces sloppy handling, so start with clear terms. A fault is a flaw in the system: a bug, a bad configuration, a dependency that is down. An error is the incorrect internal state that a fault produces: a null where a value should be, a balance that no longer reconciles. A failure is what the outside observer sees: the request returns the wrong answer, or no answer. One fault may cause many errors, and many errors may be caught before any becomes a visible failure. The whole point of error handling is to break that chain, to catch the error before it becomes a failure the user or the auditor experiences.

This vocabulary also tells you where to act. Faults are addressed in review, testing, and configuration. Errors are addressed at runtime by the patterns in this chapter. Failures are addressed by observability (chapter 9.2) and by the system-level resilience of chapter 3.5. When your team shares these words, incident reviews get sharper: you can say precisely where the chain should have been broken and was not, rather than arguing about what "the bug" was.

### Choose fail-fast or fail-safe per context

[Fail-fast](https://en.wikipedia.org/wiki/Fail-fast_system) means stopping the moment something is wrong, refusing to proceed on bad state so the problem surfaces loudly and close to its cause. Fail-safe means degrading into a known, harmless state and continuing to serve what you safely can. Neither is universally right, and the skill is choosing per context. During development and at internal boundaries, fail-fast is your friend: a program that halts on a violated invariant hands you a short stack trace instead of a long mystery. In production, at the edges of a user-facing system, fail-safe often wins: a recommendation panel that returns nothing is better than a checkout page that will not load.

Decide this deliberately for each boundary and write the decision down. A flight-control or medical-device component fails safe into a defined state because continuing on corrupt data could hurt someone. A ledger posting fails fast because posting a wrong entry is worse than posting none. The wrong pairing is dangerous in both directions: fail-safe where you needed fail-fast hides corruption, and fail-fast where you needed fail-safe turns a cosmetic hiccup into an outage.

### Pick your error-signaling mechanism and use it consistently

Languages give you two broad ways to signal that something went wrong. [Exception handling](https://en.wikipedia.org/wiki/Exception_handling) throws an object up the call stack until some handler catches it, separating the error path from the main logic. The alternative is explicit error values: the function returns both a result and an error, and the caller must inspect both. Many modern languages formalize the latter with a [Result type](https://en.wikipedia.org/wiki/Result_type), often called Result or Either, which forces the caller to unwrap either a success or a failure before using the value. Each approach has a cost. Exceptions keep the happy path clean but can hide control flow and tempt developers into catch-all blocks that erase information. Explicit results make every failure visible in the type signature but add ceremony and can be ignored if the language does not force the check.

The right answer is less about which mechanism than about consistency and honesty. Pick the idiom your language and ecosystem favor, and apply it uniformly across your services so a reader always knows how failure travels. Reserve exceptions for genuinely exceptional conditions, not ordinary control flow like "user not found," which is better modeled as a normal result. Whatever you choose, never let a failure become invisible: an unchecked error value is as dangerous as an empty catch block. In a large codebase, a written convention plus a linter that flags ignored errors beats any individual's preference.

### Make the error-handling contract explicit

Every function and every API has an error-handling contract, whether or not anyone wrote it down. It answers: what can go wrong here, how will you learn about it, and what is guaranteed about state when it does? Make that contract explicit. Document which errors a function can return or throw, distinguish recoverable errors (the caller can sensibly retry or fall back) from unrecoverable ones (the caller cannot fix this and should propagate or abort), and state whether the function leaves state unchanged on failure. This last property, sometimes called the strong exception guarantee, means a failed call is as if it never happened, which is exactly what lets a caller retry safely.

For a public or cross-team API, this contract is part of the interface, as real as the parameter types. Design a small, stable error taxonomy: a bounded set of categories such as validation error, not found, conflict, unauthorized, dependency-unavailable, and internal error. Callers can then branch on category without parsing strings. A clear taxonomy makes error handling composable across many services, and it makes failures auditable, because every failure maps to a known, named kind.

### Validate at boundaries and defend without paranoia

Treat data crossing a trust boundary (a network request, a file, user input, a message from another service) as hostile until validated, and validate it at the boundary, once, thoroughly. This is [defensive programming](https://en.wikipedia.org/wiki/Defensive_programming) applied with judgment. Inside a module whose inputs you already validated, redundant checks on every line hide the logic and suppress the very failures you would want to see. The discipline is: defend hard at the edges, trust within them. Validate structure, ranges, and invariants where data enters, convert it into types that make illegal states unrepresentable, and let the interior code assume it is working with clean data.

Paranoia has a real cost. Code smothered in null checks and defensive branches is harder to read, and worse, it often turns a clear failure into a silent shrug, returning a default where it should have raised an alarm. Defensiveness that masks bugs is not safety; it is deferral.

### Make retries safe, bounded, and polite

Many faults are transient: a momentary network blip, a service restarting, a brief lock contention. In any distributed system (chapter 3.3), these partial failures are the normal case rather than the exception. Retrying is the natural response, but a naive retry loop is a loaded gun. First, make the operation you retry [idempotent](https://en.wikipedia.org/wiki/Idempotence), meaning that performing it twice has the same effect as performing it once. Without idempotence, a retry after a timeout may charge a card twice or create two records, because you cannot tell whether the first attempt failed or merely its acknowledgment was lost. Use idempotency keys for writes so the receiver can recognize and dedupe a repeat.

Second, put a timeout on every remote call so a hung dependency cannot hang you. Third, space retries with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff), doubling the wait after each attempt, and add jitter (a small random delay) so a thousand clients recovering at once do not synchronize into a stampede that knocks the recovering service back down. Fourth, cap the number of retries and the total time, then give up gracefully. Retries without limits, backoff, jitter, and idempotence are one of the most common ways a small hiccup becomes a self-inflicted outage.

### Add circuit breakers, bulkheads, and graceful degradation in code

When a dependency is genuinely down, retrying it just wastes effort and deepens the hole. A [circuit breaker](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) watches the failure rate of calls to a dependency and, once failures cross a threshold, "opens" to fail immediately for a cooldown period rather than waiting on doomed calls. After the cooldown it lets a trial call through and closes again if the dependency has recovered. This protects both your callers (fast, predictable failures instead of piled-up timeouts) and the struggling dependency (breathing room to recover). The bulkhead pattern, named after a ship's watertight compartments, isolates resources so one saturated dependency cannot consume every thread or connection and sink the whole process; you give each dependency its own bounded pool.

These patterns pair with graceful degradation at the code level: when a non-essential dependency is unavailable, return a reduced but useful result rather than an error. Show cached data with a staleness note, hide the personalization panel, queue the write for later. This is the local complement to the system-level resilience of chapter 3.5: the architecture provides redundancy across machines, and your code provides sane behavior when a piece is missing.

### Wrap errors with context and never swallow them

An error that reads "connection refused" ten layers up from where it happened is nearly useless. As an error propagates, wrap it with context: what you were trying to do, which entity or request, which dependency, while preserving the original cause so the root is not lost. Good languages and libraries support this error chaining directly. The goal is that a single log line tells the on-call engineer what failed, during what operation, for which input. This is the raw material for the observability of chapter 9.2 and the debugging of chapter 2.15.

The cardinal sin is swallowing an error: an empty catch block, an ignored return value, a `catch` that logs at debug level and continues as if nothing happened. A swallowed error does not disappear; it re-emerges later as corrupted data or an inexplicable defect, now detached from its cause. Every error must meet one of three fates: handle it (recover or degrade), wrap and propagate it, or, at the top of the stack, log it with full context and fail. If you catch an error and do none of these, you have chosen to hide a future incident from your future self.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Exceptions | Clean happy path; hard to ignore if unchecked | Hidden control flow; tempts catch-all erasure |
| Explicit error values / Result types | Failure visible in signature; forces handling | More ceremony; can be ignored without enforcement |
| Fail-fast | Surfaces bugs loudly, close to the cause | Poor user experience if used at the edge |
| Fail-safe | Keeps serving; protects users and data | Can mask corruption if used where you needed fail-fast |
| Retries with backoff | Rides out transient faults automatically | Amplifies load and double-writes without idempotence |
| Circuit breaker | Fast failures; lets dependencies recover | Added state and tuning; can mask a persistent problem |
| Defensive validation at boundaries | Catches bad data early, once, loudly | Overdone, it clutters logic and hides real failures |

The central tension is between visibility and noise. Handle errors too quietly and you hide problems until they are expensive; handle them too loudly and everywhere, and you drown the signal in ceremony and mask the failures that matter. Resolve it by location and intent. Be loud and strict at boundaries, where bad data and dependency failures enter. Be quiet and trusting in the interior, where inputs are already clean. Decide fail-fast versus fail-safe per boundary and write it down. The aim is code where every failure has exactly one clear owner and one clear destiny, and nothing falls silently between the cracks.

## Questions to discuss with your team

1. **Do we have one shared error taxonomy and error-handling convention across our services, or does every team improvise?** On a large team this is the difference between failures that compose and failures that confuse. When one service returns HTTP 500 for a validation problem, another throws a typed exception, and a third returns a null, every integration becomes a negotiation and every incident a translation exercise. Bring examples of the same logical failure, say "record not found," as it appears across three of your services, and see how differently they signal it. The answer should become a written standard: a bounded set of error categories, a consistent way to signal them, and a linter or review checklist that enforces it. Consistency here pays off in every future integration, audit, and on-call shift.

2. **For each critical boundary, have we chosen fail-fast or fail-safe on purpose, and does the code match that choice?** Most teams have never made this decision explicitly, which means it was made for them by whoever wrote the code first, and inconsistently. The competing considerations are real: failing safe keeps users served but can let corruption spread, while failing fast protects data but can turn a minor dependency outage into a visible failure. Bring your incident history and ask, for the worst few, whether the code failed the way you would have chosen if asked in advance. The evidence you want is a map of your boundaries with a deliberate label on each, especially anywhere money, safety, or citizen records are involved. Where the label and the code disagree, you have found your next fix.

3. **When did we last exercise an error path on purpose, and did it behave as designed?** The error path is usually the least-tested code you own, yet it is where trust is won or lost, and "we fail safely" is a claim you cannot back up if you have never watched it happen. A retry loop without idempotence, a circuit breaker whose threshold is wrong, a swallowed exception in a rarely hit branch: these hide until a real incident finds them for you. Bring the results of deliberately injecting failure (a killed dependency, an induced timeout, a malformed payload) into a realistic environment. The action that follows is to make failure injection routine, so recovery, degradation, and safe-failure behavior are verified continuously rather than hoped for. Any error path you have never triggered is a promise you have not tested.

## Examples

**Startup.** A four-person startup ships an app that calls a third-party payment provider and an email service. Early on they add a naive retry loop and promptly double-charge a customer when a timeout masks a successful charge. The fix teaches the lesson: they add idempotency keys to every write, put a timeout on every outbound call, and switch to exponential backoff with jitter. They adopt a Result type for core service functions so failure shows up in the signature, and a lint rule flags any ignored error. When email sending fails, checkout degrades gracefully by queuing the message rather than blocking the sale. The discipline costs a few days and spares them a class of incidents that would have cost far more in refunds and trust.

**Enterprise.** A global logistics company runs hundreds of services and standardizes error handling across all of them. Every service maps failures to a shared taxonomy (validation, not-found, conflict, dependency-unavailable, internal), so callers branch on category rather than parsing messages. A common library provides circuit breakers, bounded retries with backoff and jitter, and bulkheaded connection pools, so no one hand-rolls these patterns wrong. Every error is logged with correlation context that feeds the observability platform of chapter 9.2, so an on-call engineer can trace a failure across service hops from a single line. Because the standard is uniform and enforced in the pipeline, engineers move confidently across unfamiliar services and auditors can see that every failure is recorded, categorized, and traceable.

**Government.** A national benefits agency builds an eligibility and payment system where a wrong answer can deny someone rent money or overpay from the public purse. Correctness and safe failure are non-negotiable, so the code fails fast on any violated financial invariant: a calculation that cannot reconcile refuses to post rather than post a wrong figure. Every citizen-facing input is validated at the boundary, and illegal states are made unrepresentable in the domain types. Each failure is written to an immutable audit log with full context, satisfying the legal requirement that decisions be explainable and reviewable years later. Where a non-critical dependency such as document preview is down, the system degrades gracefully so a caseworker can still process the claim. New civil servants inherit code whose error contracts are documented, so they can maintain it safely long after the original authors have moved on.

## Business case: motivations, ROI, and TCO

The return on disciplined error handling shows up as fewer incidents, shorter incidents, and cheaper ones. Most production outages are not exotic; they trace to a swallowed exception, a missing timeout, a retry storm, or a boundary that trusted data it should have validated. Each is preventable with the patterns here, and each prevented incident saves not just the direct cost of downtime but the compounding costs of emergency response, customer churn, and investigation. Because a wrapped, well-logged error can be diagnosed in minutes rather than hours, mean time to recovery drops, and change-failure rate drops with it as engineers stop fearing the error path.

The cost to adopt is modest and mostly one-time. You write down an error taxonomy, provide a shared library for retries and circuit breakers so teams do not reinvent them badly, add lint rules against ignored errors, and build the habit of failure injection. The cost of neglect compounds silently: swallowed errors accrete into corrupted data that is expensive to unwind, and inconsistent handling multiplies the cost of every integration and every audit. In regulated and government settings, an unauditable failure is a compliance and legal exposure, not just an engineering problem. To make the case to leadership, connect error-handling discipline to the metrics they already watch: incident frequency, mean time to recovery, change-failure rate, and audit findings.

## Anti-patterns and pitfalls

- **Silent swallowing:** empty catch blocks and ignored return values that turn a failure into a delayed, detached mystery.
- **Catch-all erasure:** a broad `catch` that logs a generic message and discards the original error and its context.
- **Retry without idempotence:** re-running non-idempotent writes after a timeout, double-charging or duplicating records.
- **Retry storms:** no backoff, no jitter, and no cap, so clients synchronize and hammer a recovering dependency back down.
- **No timeouts:** unbounded remote calls that let one hung dependency exhaust threads and freeze the whole process.
- **Exceptions as control flow:** throwing and catching for ordinary outcomes like "not found," hiding logic and slowing code.
- **Defensive paranoia:** checks on every line that bury the logic and convert real failures into silent defaults.
- **Stringly-typed errors:** callers parsing error message text because there is no stable, categorized taxonomy to branch on.
- **Fail-safe where you needed fail-fast:** continuing on corrupt state in a system where a wrong answer is worse than none.

## Maturity model

- **Level 1, Initial:** Error handling is ad hoc and per-developer. Empty catch blocks and ignored returns are common, retries are naive, timeouts are missing, and failures surface as corrupted data or mystery defects with no consistent logging.
- **Level 2, Managed:** Teams agree on basic practices. Errors are logged with some context, obvious swallowing is discouraged in review, and timeouts and simple retries exist, but conventions vary between services and the error path is rarely tested.
- **Level 3, Defined:** A shared error taxonomy and handling convention are documented and enforced. Boundary validation, idempotent retries with backoff and jitter, circuit breakers, and error wrapping are standard, provided by common libraries, and errors feed a unified observability pipeline.
- **Level 4, Optimizing:** Failure injection and resilience testing are routine, error-handling behavior is measured, fail-fast and fail-safe choices are deliberate and reviewed, and the organization continuously refines its taxonomy, libraries, and standards as it learns from every incident.

## Ideas for discussion

1. Where in your codebase does an error currently get swallowed, and how would you know if you are wrong that it does not?
2. Which of your write operations are idempotent, and which would double-execute if a retry fired after a lost acknowledgment?
3. Should "user not found" be an exception, an error value, or a normal result, and does your team answer that consistently?
4. What is your actual rule for where validation happens, and can you point to a boundary that trusts data it should not?
5. How do you decide the threshold and cooldown for a circuit breaker, and how would you know the current settings are wrong?
6. If an auditor asked to see every failure your system experienced last month, could you produce it, categorized and with context?

## Key takeaways

- Distinguish faults, errors, and failures, and break the chain before an internal error becomes a visible failure.
- Choose fail-fast or fail-safe deliberately per boundary, and make the error-handling contract of every function explicit.
- Validate hard at trust boundaries and trust within them; defensiveness that masks failures is deferral, not safety.
- Make retries safe with idempotence, timeouts, exponential backoff, and jitter, and add circuit breakers and graceful degradation in code.
- Wrap errors with context, feed them to observability, and never swallow them; every error must be handled, propagated, or logged and surfaced.

## References and further reading

- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Marc Brooker, "Timeouts, Retries, and Backoff with Jitter," Amazon Builders' Library
- Martin Fowler, "CircuitBreaker," martinfowler.com
- Nassim Nicholas Taleb, *Antifragile: Things That Gain from Disorder*
