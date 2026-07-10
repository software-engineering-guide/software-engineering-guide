# 9.2 Observability and telemetry

## Overview and motivation

[Telemetry](https://en.wikipedia.org/wiki/Telemetry) is the data a system emits about its own behavior: the metrics, logs, traces, and events collected from running software. Monitoring answers questions you already knew to ask from that telemetry. Is the disk full? Is the error rate above a threshold? Is the service up? [Observability](https://en.wikipedia.org/wiki/Observability_(software)) is broader. It is the ability to ask new questions about a system's internal state from the outside, without shipping new code, so you can understand behavior you never anticipated. As systems grow into distributed, [microservice](https://en.wikipedia.org/wiki/Microservices), and [event-driven architectures](https://en.wikipedia.org/wiki/Event-driven_architecture), the failures that hurt most are the ones nobody saw coming, and observability is what lets you debug them. Monitoring tells you that something is wrong. Observability helps you find out why.

For large teams, this distinction is decisive. You could understand a monolith by reading logs on one machine. A modern platform spans hundreds of services, many teams, multiple regions, and third-party dependencies, where a single user request may touch dozens of components. No one person holds the whole system in their head. Shared, high-quality telemetry becomes the connective tissue that lets any engineer follow a request across boundaries, line up symptoms across services, and reason about a system nobody fully owns. Without it, incidents drag on, blame flies between teams, and root causes stay hidden.

Enterprise and government systems raise the stakes with compliance, auditability, and public accountability. Regulators may require evidence of who accessed what and when. Security teams need telemetry to detect intrusions. Citizen-facing services must show they meet their published performance commitments. Good observability serves all of these at once: it is an engineering tool, a security control, and an accountability mechanism in one. Standardizing on open instrumentation avoids lock-in to a single vendor's proprietary agents, which matters enormously when systems have to last decades and survive procurement cycles.

*See also:* chapter 9.1 (site reliability engineering and SLOs), chapter 9.3 (incident management), and chapter 3.3 (distributed systems).

## Key principles

- **Instrument for unknown questions.** Design telemetry so you can investigate novel failures, beyond the ones you predicted.
- **Three pillars, one story.** Metrics, logs, and traces are complementary views; their value multiplies when correlated, not siloed.
- **Structure everything.** Structured, machine-parseable telemetry with consistent fields beats free-text that only humans can read.
- **Correlate with shared identifiers.** Trace and request IDs propagated everywhere let you stitch a single event across services.
- **Alert on symptoms, not causes.** Page humans for user-visible problems; let dashboards and investigation surface the underlying cause.
- **Every page must be actionable.** An alert that requires no human action is noise that erodes trust and causes fatigue.
- **High cardinality is a feature.** The ability to slice by user, request, region, and version is what makes debugging in production possible.
- **Own your instrumentation.** Standardize on open, vendor-neutral telemetry so you control your data and can switch backends.

## Recommendations

### Build on the three pillars and beyond

**Metrics** are numeric time series, cheap to store and ideal for dashboards, trends, and alerting thresholds. **Logs** are discrete, timestamped records of events, rich in detail and essential for forensic investigation. **[Traces](https://en.wikipedia.org/wiki/Tracing_(software))** follow a single request as it moves through services, showing latency and dependencies across the distributed call graph. Beyond these, consider **events** (meaningful state changes such as deploys), **profiles** (where code spends CPU and memory), and **[real user monitoring](https://en.wikipedia.org/wiki/Real_user_monitoring)** of the actual client experience. No single pillar is enough on its own. The goal is to move fluidly between them during an investigation.

### Standardize on OpenTelemetry and structured logging

Adopt [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) as the vendor-neutral standard for generating and collecting metrics, logs, and traces. It separates instrumentation from the analysis backend, so you can change vendors without re-instrumenting hundreds of services. That property is critical for long-lived enterprise and government systems. Emit logs as structured records (for example JSON) with consistent field names for timestamp, severity, service, and identifiers. Propagate a trace or correlation ID from the edge through every downstream call, and include it in every log line and metric exemplar, so the three pillars link up automatically.

### Design alerting for actionability and low noise

Your alerting philosophy decides whether on-call is sustainable. Alert mainly on symptoms that users feel, expressed as SLO ([service level objective](https://en.wikipedia.org/wiki/Service-level_objective)) burn rates. Page when you are burning through your error budget (the allowed shortfall from that objective) fast enough to breach it, using multi-window burn-rate alerts to balance fast detection against false alarms. Reserve paging for problems that need immediate human action, and route everything else to tickets or dashboards. Prune alerts that fire without requiring action, without mercy, because alert fatigue is a leading cause of missed real incidents and on-call burnout. Every alert should link to a runbook.

### Model health with dashboards and SLO monitoring

Build dashboards around a clear health model, not a wall of every metric you have. A good starting framework is the "four golden signals": latency, traffic, errors, and saturation. Create service-level dashboards that show SLO status and remaining error budget at a glance, plus higher-level dashboards that model overall system and user-journey health. Curate them deliberately, because dashboards that show everything communicate nothing. Keep them close to the alerts and runbooks, so responders move quickly from signal to context to action.

### Enable debugging in production with high cardinality

The hardest production problems hit a narrow slice: one customer, one region, one API version, one device type. To investigate them you need **high-cardinality** telemetry, the ability to group and filter by fields with many distinct values such as user ID or request ID. Wide, richly attributed events that carry many dimensions per record let you ask arbitrary questions after the fact. Keep enough cardinality and sampling fidelity to isolate outliers, and favor exemplar-linked traces so a spike on a metric leads you straight to representative slow requests.

### Manage cost, retention, and sampling

Telemetry volume grows with the system and can turn into a major expense. Set retention policies by data class: keep high-resolution data briefly and aggregates longer. Apply intelligent sampling to traces, biased toward keeping errors and slow requests, so you hold onto the interesting tail without paying for every routine success. Review your telemetry spend regularly, because unmanaged observability costs can rival the infrastructure they observe.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| High-cardinality events | Powerful debugging, ask anything | Higher storage and query cost |
| Aggressive sampling | Lower cost, less noise | May miss rare events |
| Symptom-based alerting | Fewer, actionable pages | Needs good SLOs to work well |
| OpenTelemetry standard | Vendor-neutral, portable | Migration effort, maturing tooling |
| Long log retention | Better forensics and audit | Storage cost, privacy exposure |

Observability decisions come down to a tension between fidelity and cost. Capturing everything at full resolution gives you perfect hindsight, but at scale it is prohibitively expensive. Cut aggressively and you save money, but you may throw away the one record that would have explained an outage. Sampling and retention tiers are how mature teams walk this line, keeping errors and outliers while thinning routine data. The alerting trade-off is between sensitivity and noise: too many alerts cause fatigue and missed incidents, too few let problems fester. Symptom-based, SLO-driven alerting resolves much of this, but only if you have meaningful SLOs in place.

## Questions to discuss with your team

1. **What is your plan to move legacy services onto OpenTelemetry, and how do you avoid paying for two instrumentation stacks during the transition?** Vendor-neutral instrumentation is the property that lets you switch backends without re-instrumenting hundreds of services, and it matters most for the long-lived enterprise and government systems that outlast any single vendor contract. The migration is where good intentions stall: half-instrumented estates leave gaps exactly where a request crosses from a new service to an old one, breaking the end-to-end trace. Bring an inventory to the discussion: which services emit proprietary agent data, which emit OpenTelemetry, and where trace context is dropped at the boundary. Decide a sequencing that follows real request paths rather than org charts, and budget for the window where you run both collectors. The answer determines whether you actually own your telemetry or stay locked to one vendor's agents.

2. **When did you last audit every alert for actionability, and how many pages last month required no human action?** Alert fatigue is a leading cause of missed real incidents and on-call burnout, so a page that needs no action is not harmless noise, it actively erodes the response you depend on. Bring the receipts: pull last month's pages, mark each as actioned or ignored, and count how many mapped to a runbook. For a large team spanning many services, noisy alerts from one team desensitize the shared on-call for everyone. Set a standard that every page links to a runbook and ties to an SLO burn rate, then delete the rest without mercy. The result of this audit should directly cut your paging volume and tell you which services have no meaningful SLO behind their alerts.

3. **What is your trace sampling strategy, and how confident are you that it keeps the errors and the slow tail?** Telemetry volume grows with the system and unmanaged observability cost can rival the infrastructure it observes, so you will sample, and the question is whether you sample intelligently. Stripping cardinality or sampling blindly removes exactly the records needed to debug the narrow problems that hit one customer, one region, or one API version. Bring your current retention tiers and sampling rules: are you biasing toward keeping errors and slow requests, using exemplar-linked traces so a metric spike leads to a representative slow request? For audited and privacy-bound systems, reconcile retention with data-minimization rules so you are not hoarding personal data to debug. The answer sets where you spend telemetry budget and whether your next hard outage is explainable or a mystery.

## Examples

**Startup.** A four-person startup ships a mobile backend and keeps getting vague "the app is slow" complaints it cannot reproduce. The team adds OpenTelemetry to its handful of services and switches to structured JSON logs with a request ID carried from the app through every hop. The next slow report resolves in minutes: one trace shows a missing database index on the orders table under a specific query. Because they chose open instrumentation early, they later move from a free tier to a paid backend without re-instrumenting anything.

**Enterprise.** A large e-commerce platform instruments every service with OpenTelemetry, propagating a trace ID from the customer's browser through checkout, payment, inventory, and shipping. When conversion drops, an on-call engineer starts from an SLO burn-rate alert, opens the checkout dashboard's golden signals, spots elevated latency in one region, and follows an exemplar trace to a slow database call in a single service. High-cardinality attributes show the problem is confined to one product category, which guides a targeted fix in minutes rather than hours.

**Government.** A national health service runs a patient-records platform under strict audit and privacy rules. Structured logs capture who accessed which record and when, feeding both security monitoring and compliance reporting, while personally identifiable fields are redacted or tokenized in telemetry. Public SLO dashboards show availability and latency for citizen-facing appointment booking. By standardizing on open instrumentation, the agency avoids proprietary lock-in across a system expected to run for decades and to be re-procured by different vendors over its life.

## Business case: motivations, ROI, and TCO

The main return on observability is a dramatic drop in the time it takes to detect and resolve incidents. For a service where downtime is costly, cutting mean time to resolution from hours to minutes pays for the tooling many times over in a single major incident. Observability also saves the engineering time you would otherwise spend guessing, reproducing bugs, and arguing about which team is at fault, and it shortens the feedback loop that lets teams ship with confidence. The security and compliance value is real too: the same telemetry supports intrusion detection and audit evidence.

Total cost of ownership includes instrumentation effort, telemetry storage and query costs, and the discipline to curate signal from noise. These costs are visible and recurring, which tempts leadership to underinvest. The cost of not adopting is larger but harder to see: prolonged outages, undiagnosed performance problems, security incidents found late or never, and engineers burning out on alerts they can do nothing about. Make the case with concrete incident data. Show the resolution time and business impact of recent outages, and project the reduction that better telemetry would deliver. Framing observability as insurance that also speeds up delivery, rather than as a pure cost center, wins the argument.

## Anti-patterns and pitfalls

- **Alert on everything.** Paging for every anomaly trains responders to ignore alerts, so real incidents slip through.
- **Cause-based paging.** Alerting on internal causes rather than user symptoms floods on-call with noise and misses novel failures.
- **Unstructured logs.** Free-text logs that cannot be queried or correlated force slow, manual grepping during incidents.
- **Three siloed pillars.** Metrics, logs, and traces in disconnected tools with no shared IDs prevent following an event end to end.
- **Dashboard sprawl.** Hundreds of uncurated dashboards mean nobody knows which one shows whether the system is healthy.
- **Cardinality collapse.** Stripping high-cardinality fields to save cost removes exactly the data needed to debug narrow problems.
- **Vendor lock-in.** Proprietary agents everywhere make switching backends prohibitively expensive and hold your data hostage.

## Maturity model

**Level 1, Initial.** Basic uptime checks and unstructured logs on individual machines. Debugging means logging into servers. Alerts are noisy and often ignored.

**Level 2, Repeatable.** Centralized metrics and log aggregation exist. Some dashboards and threshold alerts are in place, but logs are semi-structured and traces are absent or partial. Correlation across services is manual.

**Level 3, Defined.** OpenTelemetry-based instrumentation across services with propagated trace IDs. Structured logging, distributed tracing, curated dashboards, and SLO-based symptom alerting are standard. On-call is sustainable.

**Level 4, Optimizing.** High-cardinality, event-rich observability enables ad hoc investigation of any slice. Alerting is SLO burn-rate driven with minimal noise, sampling and retention are cost-optimized, and telemetry actively informs capacity, security, and product decisions.

## Ideas for discussion

- Where is the right balance between telemetry fidelity and cost for your most critical services?
- How do you decide what deserves a page versus a ticket versus only a dashboard entry?
- What is your strategy for propagating correlation IDs across teams that do not share a codebase or release cycle?
- How do you preserve high-cardinality debugging power while meeting privacy and data-minimization requirements?
- Should observability tooling be centrally mandated or chosen per team, and what are the consequences either way?
- How would you demonstrate to auditors that your telemetry is complete and tamper-evident?

## Key takeaways

- Monitoring detects known problems; observability lets you investigate unknown ones without shipping new code.
- Metrics, logs, and traces are most valuable when correlated through shared identifiers, not siloed.
- Standardize on OpenTelemetry and structured logging to stay vendor-neutral and portable across long system lifetimes.
- Alert on user-visible symptoms via SLO burn rates, make every page actionable, and prune noise relentlessly.
- Curate dashboards around a clear health model such as the golden signals rather than showing every metric.
- High-cardinality, event-rich telemetry is what makes debugging narrow production problems possible.

## References and further reading

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
