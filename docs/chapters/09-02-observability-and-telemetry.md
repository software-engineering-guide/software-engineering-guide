# 9.2 Observability and telemetry

## Overview and motivation

[Telemetry](https://en.wikipedia.org/wiki/Telemetry) is the data a system emits about its own behaviour: the metrics, logs, traces, and events collected from running software. Monitoring answers questions you already knew to ask from that telemetry. Is the disk full? Is the error rate above a threshold? Is the service up? [Observability](https://en.wikipedia.org/wiki/Observability_(software)) is broader. It is the ability to ask new questions about a system's internal state from the outside, without shipping new code, so you can understand behaviour you never anticipated. As systems grow into distributed, [microservice](https://en.wikipedia.org/wiki/Microservices), and [event-driven architectures](https://en.wikipedia.org/wiki/Event-driven_architecture), the failures that hurt most are the ones nobody saw coming, and observability is what lets you debug them. Monitoring tells you that something is wrong. Observability helps you find out why.

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

The hardest production problems hit a narrow slice: one customer, one region, one API version, one device type. To investigate them you need **high-cardinality** telemetry, the ability to group and filter by fields with many distinct values such as user ID or request ID. Wide, richly attributed events that carry many dimensions per record let you ask arbitrary questions after the fact. Keep enough cardinality and sampling fidelity to isolate outliers, and favour exemplar-linked traces so a spike on a metric leads you straight to representative slow requests.

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

4. **Which of your SLOs are real user-journey commitments, and which are proxy metrics nobody outside the owning team believes?** Symptom-based alerting only works when the symptoms map to things users actually feel, so an alert wired to a CPU threshold or a made-up availability target pages people for problems that may not matter while staying silent on ones that do. For a large organization, SLOs are also the contract that lets independent teams share an on-call rotation without relitigating severity during every incident. Bring the current SLO catalogue, the user journey each objective is meant to protect, and the last quarter's breaches with whether customers actually complained. In enterprise and government settings, tie the most visible SLOs to the published performance commitments the service is held to, so the same burn-rate signal that pages an engineer is also the evidence you show a regulator or an oversight body. The discussion should retire the proxy metrics and leave you with a short list of objectives that a non-engineer would recognize as promises to users.

5. **Who owns telemetry data governance, and can you prove that personal data is redacted before it lands in your observability backend?** High-cardinality events and long log retention are exactly the features that make debugging possible, and exactly the ones that turn an observability store into an unmanaged copy of your users' personal data. The competing pull is real: engineers want richer attributes and longer retention, while privacy and legal want data minimization and short lifetimes. Bring a data-flow map showing which fields carry personal or sensitive data, where redaction or tokenization happens in the pipeline, and what your retention tiers are per data class. For regulated and public systems, name the accountable owner, map retention to the lawful basis and the data-minimization rules you operate under, and be ready to show an auditor that access to the telemetry itself is logged and controlled. The answer decides whether your observability platform is an asset or a standing breach waiting to be discovered.

6. **When an incident crosses several teams' services, does your telemetry let one responder follow the request end to end, or does the trail break at every ownership boundary?** The whole promise of correlated, ID-propagated telemetry is that a single engineer can reason about a system nobody fully owns, and that promise collapses at exactly the boundary where trace context is dropped or where two teams use incompatible identifiers and tools. Weigh the pull toward per-team autonomy in choosing observability tooling against the shared cost of a fragmented estate where every handoff is a dead end during an outage. Bring a recent cross-team incident timeline and mark where the responder lost the thread, plus an inventory of which services propagate a common correlation ID and which do not. For a large enterprise or a government platform assembled from many vendors and long-lived systems, decide how much you centrally mandate, a shared trace-context standard and a common ID scheme, versus what you leave to teams, because the components you re-procure over decades still have to interoperate on the same request. The answer tells you whether your next multi-team incident is a coordinated investigation or a round of finger-pointing.

## Sector lens

**Startup.** With a handful of services and no spare hands, instrument with OpenTelemetry from day one and ship structured JSON logs carrying one request ID end to end. That small investment turns "the app is slow" into a trace you can read, and it keeps you free to move from a free tier to a paid backend later without re-instrumenting. Skip elaborate dashboards and SLO machinery until you have users whose experience you can actually measure.

**Small business.** You have no observability specialist and a tight budget, so lean on a managed backend where instrumentation, storage, and dashboards come bundled rather than assembling your own stack. The buy-versus-build call favours buying almost every time here; your scarce attention is better spent on the two or three golden-signal alerts that tell you the service is down than on running a telemetry pipeline. Set a hard retention limit so telemetry cost cannot quietly overtake the infrastructure it watches.

**Enterprise.** The work is governance across many teams: a shared OpenTelemetry standard, a common correlation-ID scheme, and curated SLO dashboards so a single responder can follow a request across dozens of services. Manage telemetry as a cost centre with retention tiers and sampling policy, standardize alerting on SLO burn rates to keep a shared on-call sustainable, and prune noisy alerts centrally so one team's fatigue does not desensitize everyone. Treat the instrumentation layer as vendor-neutral infrastructure that outlives any single backend contract.

**Government.** Procurement rules, transparency, and public accountability shape the design. Standardize on open instrumentation so a system expected to run for decades survives re-procurement by different vendors without being held hostage to proprietary agents, and require that portability in the contract. Use structured audit logs to show who accessed which record and when, redact or tokenize personal data before it reaches the telemetry store, and reconcile retention with data-minimization law. Publish SLO dashboards for citizen-facing services so the same signals your engineers watch are visible evidence of the commitments you are held to.

## Examples

**Startup.** A four-person startup ships a mobile backend and keeps getting vague "the app is slow" complaints it cannot reproduce. The team adds OpenTelemetry to its handful of services and switches to structured JSON logs with a request ID carried from the app through every hop. The next slow report resolves in minutes: one trace shows a missing database index on the orders table under a specific query. Because they chose open instrumentation early, they later move from a free tier to a paid backend without re-instrumenting anything.

**Enterprise.** A large e-commerce platform instruments every service with OpenTelemetry, propagating a trace ID from the customer's browser through checkout, payment, inventory, and shipping. When conversion drops, an on-call engineer starts from an SLO burn-rate alert, opens the checkout dashboard's golden signals, spots elevated latency in one region, and follows an exemplar trace to a slow database call in a single service. High-cardinality attributes show the problem is confined to one product category, which guides a targeted fix in minutes rather than hours.

**Government.** A national health service runs a patient-records platform under strict audit and privacy rules. Structured logs capture who accessed which record and when, feeding both security monitoring and compliance reporting, while personally identifiable fields are redacted or tokenized in telemetry. Public SLO dashboards show availability and latency for citizen-facing appointment booking. By standardizing on open instrumentation, the agency avoids proprietary lock-in across a system expected to run for decades and to be re-procured by different vendors over its life.

## Business case: motivations, ROI, and TCO

The main return on observability is a dramatic drop in the time it takes to detect and resolve incidents. For a service where downtime is costly, cutting mean time to resolution from hours to minutes pays for the tooling many times over in a single major incident. Observability also saves the engineering time you would otherwise spend guessing, reproducing bugs, and arguing about which team is at fault, and it shortens the feedback loop that lets teams ship with confidence. The security and compliance value is real too: the same telemetry supports intrusion detection and audit evidence.

Total cost of ownership includes instrumentation effort, telemetry storage and query costs, and the discipline to curate signal from noise. These costs are visible and recurring, which tempts leadership to underinvest. The cost of not adopting is larger but harder to see: prolonged outages, undiagnosed performance problems, security incidents found late or never, and engineers burning out on alerts they can do nothing about. Make the case with concrete incident data. Show the resolution time and business impact of recent outages, and project the reduction that better telemetry would deliver. Framing observability as insurance that also speeds up delivery, rather than as a pure cost centre, wins the argument.

## Anti-patterns and pitfalls

- **Alert on everything.** Paging for every anomaly trains responders to ignore alerts, so real incidents slip through.
- **Cause-based paging.** Alerting on internal causes rather than user symptoms floods on-call with noise and misses novel failures.
- **Unstructured logs.** Free-text logs that cannot be queried or correlated force slow, manual grepping during incidents.
- **Three siloed pillars.** Metrics, logs, and traces in disconnected tools with no shared IDs prevent following an event end to end.
- **Dashboard sprawl.** Hundreds of uncurated dashboards mean nobody knows which one shows whether the system is healthy.
- **Cardinality collapse.** Stripping high-cardinality fields to save cost removes exactly the data needed to debug narrow problems.
- **Vendor lock-in.** Proprietary agents everywhere make switching backends prohibitively expensive and hold your data hostage.

## Maturity model

**Level 1, Initiate.** Observability is ad hoc and reactive. Basic uptime checks and unstructured logs live on individual machines, debugging means logging into servers to grep, and there is no shared telemetry. Alerts are noisy, cause-based, and often ignored, so real incidents surface through user complaints rather than signals.

**Level 2, Develop.** Basic practices appear but vary by team. Some services push metrics and logs to a central place, a few dashboards and threshold alerts exist, but logs are only semi-structured and traces are absent or partial. Correlation across services is manual, and whether an engineer can follow a request end to end depends on which teams happen to be involved.

**Level 3, Standardize.** Instrumentation is documented and enforced org-wide. OpenTelemetry across services with a propagated trace or correlation ID, structured logging with consistent field names, distributed tracing, curated golden-signal dashboards, and SLO-based symptom alerting are the standard every team follows. Every page links to a runbook and ties to an SLO, and on-call is sustainable rather than a source of burnout.

**Level 4, Manage.** The observability estate itself is measured and controlled against baselines. You track instrumentation coverage and trace-context propagation rate across services, the share of pages that were actioned versus ignored, mean time to detect and resolve, SLO attainment and error-budget burn, and telemetry cost per service against a budget. Gaps and alert noise are driven down with data toward explicit targets, sampling fidelity is verified so the error and slow-tail records survive, and go or no-go decisions on coverage and retention are made on evidence rather than opinion.

**Level 5, Orchestrate.** Observability is continuously improved and integrated across the organization. High-cardinality, event-rich telemetry enables ad hoc investigation of any slice, alerting is SLO burn-rate driven with minimal noise, and sampling and retention adapt to changing cost and risk. Telemetry feeds capacity planning, security detection, and product decisions as a matter of routine, and the platform re-tunes its own signals, budgets, and coverage as the system, the threat picture, and the regulatory obligations shift.

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
