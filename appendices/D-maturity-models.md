# Appendix D. Maturity models

Every chapter in this guidebook ends with a "Maturity model" that describes how
a practice typically evolves. This appendix consolidates all 55 of them into one
reference so you can assess a team, a domain, or a whole organization at a glance.

## The shared four-level scale

All chapters use the same progression. Wording varies slightly between chapters
(some call Level 2 "Repeatable" or "Developing," some call Level 3 "Managed"),
but the intent is consistent:

- **Level 1 — Initial.** Ad hoc, personality-driven, reactive. Practices exist
  only where an individual chooses them. Outcomes depend on heroics and luck.
- **Level 2 — Managed.** Basic practices are in place and repeated, but they are
  inconsistent across teams, partly manual, and often bypassed under pressure.
- **Level 3 — Defined.** Practices are standardized, documented, and enforced
  across the organization. This is the level most enterprise and government work
  must reach to be auditable and dependable.
- **Level 4 — Optimizing.** Practices are measured, continuously improved, and
  adapted from evidence. The safe or correct path is the default and often
  automated; the organization learns and evolves deliberately.

### How to use it for self-assessment

1. For each chapter relevant to your context, read the four cells below and pick
   the level that honestly describes your *typical* behavior — not your best team
   on its best day, and not your written policy, but what actually happens.
2. Score each chapter 1.1–1.4. Round down when in doubt; a practice that is
   inconsistent is Level 2, not Level 3.
3. Average scores within a Part to see where a whole domain stands, then look at
   the spread: a Part at "3 on average" that hides a Level 1 chapter still has a
   Level 1 risk.
4. Re-assess periodically and track the trend. Movement matters more than any
   single snapshot.

### Maturity is a means, not an end

Higher maturity is not automatically better. The goal is *fit* — enough rigor to
manage the risk and scale you actually face, and no more. A small, low-stakes
tool does not need Level 4 chaos engineering. Reaching for a high level as a
trophy, rather than to solve a real problem, produces ceremony without value.
Read every "Level 4" below as "appropriate when the stakes justify it," and let
risk, scale, and regulatory exposure decide how far to climb.

---

## Part 1 — Foundations: Culture, People, and Process

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Engineering culture and values | Culture is accidental and personality-driven; incidents mean blame; knowledge lives in a few heads. | Some teams run postmortems and write docs, but practice is inconsistent and unreinforced by leadership. | Blameless learning, ownership models, and a writing culture are org-wide norms with clear expectations and tooling. | Culture is continuously measured and improved; safety is high, learning is fast, and practices evolve on evidence. |
| Team topologies | Teams form by accident or headcount; structure mirrors legacy hierarchy; dependencies everywhere. | Some stream-aligned teams exist, but shared bottlenecks and functional silos persist. | The four team types and explicit interaction modes are used deliberately; platforms and InnerSource cut dependencies. | Team boundaries and cognitive load are actively monitored and evolved; the org reshapes itself to sustain flow. |
| Roles, career ladders, growth | No written ladder; promotions and pay are ad hoc and personality-driven. | A basic ladder exists but is applied inconsistently; no calibration; hiring is unstructured. | Dual tracks, a clear competency matrix, calibration, and structured hiring are standard. | Growth data and equity are measured; sponsorship and apprenticeship are deliberate; the framework evolves with the work. |
| Ways of working | Process is ad hoc or cargo-cult; communication is meeting-driven and undocumented; estimates are treated as promises. | A methodology is followed consistently, but ceremonies are rote and cross-team coordination is heavy. | Practices are chosen to fit context; async, docs-first communication is the norm; estimation informs, not controls. | The team continuously tunes its way of working from flow metrics; coordination need is minimized at the source. |
| Decision-making and governance | Decisions are ad hoc and unrecorded; governance is absent or a blanket bottleneck; debt is invisible. | Some decisions are documented and some review exists, but process is inconsistent and mismatched to decision weight. | ADRs, a paved road, reversibility-based delegation, and a debt inventory are standard and transparent. | Governance is continuously tuned; scrutiny targets irreversible decisions; debt and sourcing are managed as portfolios. |

## Part 2 — Programming Craft and Code Quality

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Coding standards and style | Style is per-author; no shared configs; formatting is argued in review. | Each team has a formatter and linter, but configs and rules vary across teams. | Central shared configs per language; CI enforcement; new repos inherit standards via templates. | Standards are versioned, governed, measured for impact, and refined; enforcement is near-frictionless. |
| Software design principles | Design is ad hoc; coupling accumulates; principles are unknown or invoked as slogans. | Teams know the principles and apply them, but inconsistently and often dogmatically. | Shared design vocabulary, deliberate coupling/cohesion analysis, and bounded contexts aligned to teams. | Design decisions are recorded and revisited; principles applied with nuance; paradigm choices are deliberate. |
| APIs and interface design | APIs emerge from implementation; no shared conventions; breaking changes are common and unannounced. | Teams follow basic REST conventions and version informally, but consistency and docs vary. | Contract-first design, machine-readable specs, a deprecation policy, and consistent error/pagination conventions. | APIs are governed products in a catalog with strong DevEx, measured adoption, and rare, well-managed breaks. |
| Testing strategy | Testing is manual and ad hoc; automated coverage is minimal; regressions are frequent. | Automated unit and some integration tests exist, but the suite is slow or flaky and trust is low. | A balanced, fast, reliable suite gates every change; flakiness is managed; non-functional testing is integrated. | Advanced techniques (property, mutation, fuzz) target high-value code; metrics drive continuous improvement. |
| Code review and collaboration | Review is inconsistent or skipped; mechanical issues dominate; feedback norms are unset. | Review is required but slow and variable; automation is partial; PR size and quality vary widely. | Small PRs, automated mechanical checks, clear standards and feedback norms, and monitored latency. | Review depth matches risk; latency is low and tracked; pairing and AI assist deliberately improve quality. |
| Version control and source management | Ad hoc branching; long-lived branches; poor messages; no secret scanning; frequent merge pain. | A consistent branching model and message conventions exist, but branches live too long and enforcement is partial. | Trunk-based development, protected mainline, enforced commit conventions, secret scanning, deliberate repo structure. | Source practices are measured against delivery metrics; automation enforces hygiene end to end; structure evolves. |
| Documentation | Documentation is sparse, scattered, and stale; knowledge lives in people's heads. | Key docs exist (READMEs, some runbooks) but are inconsistently maintained and hard to find. | Docs-as-code with clear structure, generated API docs and changelogs, decision records, and update expectations. | Docs are living and largely generated or tested against the system, owned, discoverable, and measured for accuracy. |

## Part 3 — Architecture and Systems

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Architecture fundamentals | Architecture is implicit and lives in heads; no quality attributes or ADRs; decisions surface during incidents. | Key diagrams exist and major decisions are sometimes recorded; quality attributes named but rarely quantified; docs drift. | Quality-attribute scenarios and ASRs are specified; ADRs routine; C4/arc42 docs maintained near code; trade-off reviews happen. | Fitness functions enforce characteristics in CI; architecture evolves with data; docs are trustworthy enough for auditors. |
| Architectural styles and patterns | One tangled monolith or accidental distributed mess; boundaries follow layers or history; style chosen by fashion. | Deliberate modular boundaries or a few coarse services; some cross-cutting concerns consistent; splits still ad hoc. | Services aligned to bounded contexts owning their data; gateway/BFF where apt; clean/hexagonal layering standard. | Style decisions are evidence-based and reversible-by-design; a mature platform makes distribution cheap; re-consolidate when a split stops paying. |
| Distributed systems | Remote calls treated as local; no/naive retries; failures cascade; debugging is per-machine log spelunking. | Timeouts and basic retries exist but inconsistent; some idempotency; logs centralized but uncorrelated. | Idempotency, backoff, circuit breakers, bulkheads via shared libs; sagas; distributed tracing; documented consistency per flow. | Resilience is the platform default, continuously tested with fault injection; SLOs drive alerting; graceful degradation by design. |
| Data architecture and storage | One database for every purpose; no migration discipline; incidental caching; scale by bigger machine. | Storage choices mostly deliberate; a cache and maybe a warehouse; versioned migrations sometimes need downtime. | Polyglot persistence matched to workloads, each store owned; automated zero-downtime migrations; explicit caching and replicas. | Data architecture continuously reviewed against access patterns and cost; sharding/caching data-driven; evolution automated and audited. |
| Scalability, performance, resilience | Single-instance or vertically scaled; server-side state; no load testing or budgets; failures cause full outages. | Horizontally scaled stateless tiers; basic autoscaling; some pre-launch load testing; DR documented but rarely tested. | Capacity planned with headroom; performance budgets in CI; resilience patterns standard; RTO/RPO defined and DR tested. | Multi-region automated failover; continuous chaos and game days; capacity forecast; recovery objectives proven. |
| Legacy modernization | Legacy is feared and frozen; no inventory; modernization is all-or-nothing rewrite; knowledge in retiring heads. | An inventory exists and some risk understood; legacy wrapped with APIs; still big-bang thinking; migration underestimated. | Systems prioritized by risk and value; strangler-fig and branch-by-abstraction standard; migration reconciled with dual-running. | Modernization is continuous and portfolio-managed against risk; incremental replacement is routine, reversible, and value-delivering. |

## Part 4 — Security, Privacy, and Trust

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Security foundations and culture | Security is reactive and centralized; reviews late if at all; no threat modeling; security is "someone else's problem." | A security team defines standards; some threat modeling on major projects; basic training; security seen as a gate. | Security champions embedded; threat modeling routine; secure SDLC documented; risk-based prioritization; blameless reviews. | Security is genuinely everyone's job; threat modeling is habitual; zero-trust largely realized; metrics drive improvement. |
| Application security | Security depends on individual knowledge; no standard controls; secrets in code; stale deps; ad hoc auth. | OWASP Top 10 awareness; some framework protections; secrets manager unevenly used; occasional dependency scanning. | ASVS-based requirements per tier; parameterized queries; central identity with MFA; managed secrets; SBOMs and pipeline scanning. | Secure defaults in paved-road frameworks; short-lived credentials; full supply-chain assurance (SLSA); continuous verification. |
| Infrastructure and cloud security | Manual provisioning; broad permissions and static keys; flat networks; inconsistent encryption; no posture management. | Some IAM roles and MFA; basic network tiers; encryption at rest for major stores; periodic manual reviews; partial IaC. | Least-privilege RBAC/ABAC with short-lived creds; default-deny segmentation; encryption by default with KMS; CSPM with policy. | Secure defaults in landing zones and IaC; micro-segmentation; customer-managed keys/HSMs; preventive guardrails; drift auto-remediated. |
| Security operations | Security testing manual and rare; no central logging or SIEM; no incident plan; ad hoc patching; never adversarially tested. | Some scanners in the pipeline; central logging; a basic incident plan; loose patching timelines; annual pentest. | Full DevSecOps scanning with risk-based gates; SIEM with some SOAR; rehearsed IR with tabletops; remediation SLAs; red teaming. | Testing and response highly automated; detection engineering mapped to adversary techniques; purple teaming; MTTD/MTTR low and falling. |
| Privacy and data protection | Personal data collected freely; no inventory, minimization, or retention; consent an afterthought; no rights process. | A privacy policy and basic consent exist; some retention awareness; rights requests handled manually and slowly. | Privacy by design with DPIAs; data mapped and classified; retention enforced; lawful basis documented; rights met on deadline. | Privacy is a default engineering constraint; minimization and automated retention standard; rights requests self-service; posture measured. |
| Compliance and governance | Compliance is reactive; no control framework; evidence assembled manually under deadline; frequent findings. | Key frameworks identified; some documented controls; audits pass with heavy manual effort; accessibility considered late. | A unified control framework cross-maps standards; evidence partly automated; accessibility tested; records and authorizations established. | Continuous compliance with always-on evidence and compliance-as-code; new certifications are low-cost; audit-ready at any moment. |

## Part 5 — UI, UX, and Product Design

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| UX foundations | No dedicated UX practice; decisions by opinion; research ad hoc; inconsistent flows and terminology. | Some designers and occasional usability testing; personas unmaintained; UX is a phase, often bypassed. | Continuous mixed-method research feeds prioritization; shared personas, journey maps, and IA; UX quality gates in the DoD. | Research is continuous and outcome-linked; UX metrics track alongside business metrics; controlled experiments close the loop. |
| UI design and design systems | Each team builds its own UI; no shared components; inconsistent look; hard-coded colors and spacing. | A partial style guide or component library exists but is optional and often out of sync between design and code. | A tokenized design system with a maintained coded library, docs, and governance is used across teams; a11y built in. | The system is a governed product with versioning and roadmap; design-code parity measured; rebrands are token changes. |
| Accessibility | No accessibility practice; issues found via complaint or lawsuit; non-semantic, untested markup. | Awareness exists; some automated scanning and a pre-launch audit; a11y is a late checklist, often deprioritized. | WCAG 2.2 AA is the standard; a11y built into the design system, tested, and in the DoD; teams trained with an owner. | Accessibility is continuous and measured; disabled people involved in research; embedded in procurement, tokens, and CI. |
| Content and communication design | No content practice; words written ad hoc; inconsistent terminology and tone; unhelpful errors and empty states. | A style guide may exist; some plain-language awareness; content is still late-stage and per-team with little reuse. | A content strategy, voice-and-tone guide, and glossary used across teams; plain language standard; shared patterns. | Content is continuously tested against outcomes; dark patterns prohibited and audited; patterns localized and accessible by default. |
| Internationalization and localization | Single language; hard-coded strings; non-Unicode assumptions; new locales require code changes. | Strings externalized and Unicode used, but localization is a manual pre-launch batch; formatting and plurals inconsistent. | Shared i18n architecture and locale-aware formatting; a TMS and continuous pipeline; pseudo-localization and multi-locale CI. | i18n enforced by tooling and lint across teams; localization continuous; cultural adaptation systematic; new locales launch fast. |
| Frontend engineering | Ad hoc per-team frontend; heavy client code; no budgets; tested only on team devices; framework by hype. | Some shared tooling and a component library; performance measured occasionally, not budgeted; limited cross-device testing. | Framework and rendering chosen deliberately per surface; budgets enforced in CI with RUM; progressive enhancement standard. | Performance, resilience, and reach continuously measured against real users and tied to outcomes; regressions fail the build. |

## Part 6 — Artificial Intelligence and Machine Learning

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| AI strategy and readiness | Ad hoc experiments; no shared strategy; decisions driven by hype and individual enthusiasm. | Problem framing on some projects; a first platform baseline; build-versus-buy discussed but inconsistent. | A portfolio of use cases with clear metrics, a decision tree, readiness assessments, and lock-in/TCO analysis. | AI strategy integrated with business and risk planning; readiness continuously maintained; systems routinely re-scoped on evidence. |
| MLOps | Models built ad hoc in notebooks; manual deployment; no data/model versioning; no monitoring. | Some experiment tracking and a model registry; semi-automated deployment; basic monitoring for a few models. | Shared platform with feature store, registry, reproducible pipelines, lineage; drift/quality monitoring; governed promotion. | Fully automated, auditable lifecycle; drift-triggered retraining with gates; self-service paved roads; continuous eval tied to business. |
| Generative AI and LLM applications | Ad hoc prompting in isolated projects; no grounding, guardrails, or eval; hallucinations found in production. | Some RAG and prompt versioning; basic output validation; a small manual evaluation set. | Shared patterns for RAG, guardrails, and tool use; automated offline eval on every change; online metrics and human review. | Continuous offline and online eval tied to outcomes; robust injection defenses; governed, observable agents; systematic mitigation. |
| AI-assisted software development | Individuals use assistants ad hoc; no policy; no measurement; secrets and IP at risk. | Basic usage guidance and data rules; some security scanning; anecdotal productivity claims. | Clear norms by risk level; mandatory review and scanning; honest outcome metrics; secure deployment and disclosure. | Continuous measurement of delivery/quality impact; strong verification in the pipeline; deliberate skill development; adaptive policy. |
| Responsible and trustworthy AI | No fairness testing, explanations, or governance; responsibility undefined; issues found only after harm. | Some bias testing and documentation; ad hoc oversight; framework awareness but partial adoption. | Governance mapped to recognized frameworks; systematic fairness/safety/privacy testing; documented oversight and appeals; red-teaming. | Continuous production monitoring of fairness and safety; governance integrated into delivery; responsibility is everyone's job. |
| AI infrastructure and operations | Ad hoc GPU allocation; no batching or caching; no cost visibility; unversioned prompts; minimal monitoring. | Some shared scheduling and caching; basic cost tracking; prompts in version control; ad hoc evaluation. | Shared platform with scheduling, quotas, batching, caching, right-sizing; vector infra; automated eval; cost attribution. | Continuously optimized utilization and cost per outcome; automated routing/scaling; full LLMOps observability; portability maintained. |

## Part 7 — Data, Analytics, and Insight

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Data strategy and governance | Data undocumented and unowned; conflicting definitions; quality found when reports break; no catalog or lineage. | Some datasets have owners and docs; a partial catalog; manual, reactive quality checks; policy written but weakly enforced. | Critical data products have owners, contracts, SLAs; catalog with automated lineage; continuous quality; federated governance. | Data-as-product is the norm; contracts enforced automatically; self-service guardrails; definitions trusted enterprise-wide. |
| Data engineering | Ad hoc scripts, manual runs, no tests or monitoring; failures found by consumers; costs unmanaged. | Some orchestration and scheduling; basic transformations in version control; occasional tests; reactive firefighting. | ELT with layered, tested, versioned models; orchestrated dependencies with retries/backfills; observability; costs tracked. | Pipelines are software with CI/CD, data contracts, and testing; proactive anomaly detection; SLAs; new products ship fast. |
| Analytics and business intelligence | Reports built ad hoc in spreadsheets; inconsistent metrics; misleading charts; no governance. | A BI tool with some shared dashboards; metric definitions still diverge; uncontrolled self-service and sprawl begins. | A semantic layer defines core metrics once; certified vs experimental content; self-service within guardrails; managed lifecycle. | Metrics governed like APIs with owners and changelogs; analytics spans descriptive to prescriptive and embeds at decision points. |
| Product analytics and experimentation | Little/inconsistent instrumentation; decisions by opinion; no experiments; vanity metrics; careless consent. | Some events tracked but taxonomy inconsistent; occasional A/B tests without power analysis; north star proposed, not embedded. | A governed, validated tracking plan; funnels/cohorts/retention routine; experiments on a shared platform; consent handled properly. | Experimentation is the default; predefined metrics and shared results repo; instrumentation owned; org learns cumulatively. |
| Decision science and data culture | Decisions by hierarchy and intuition; correlation treated as causation; uncertainty ignored; metrics surveil and are gamed. | Data consulted selectively to justify decisions; some awareness of causal traps; uncertainty rarely communicated. | Analyses tied to decisions with predefined criteria; correlation vs causation distinguished; uncertainty communicated; outcome focus. | "What would change our mind?" is routine; causal rigor and honest uncertainty are norms; leaders update visibly on evidence. |

## Part 8 — Automation, DevOps, and Platform Engineering

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| CI/CD and delivery | Builds and deploys largely manual and inconsistent; late integration; infrequent, stressful releases; manual rollback. | Automated builds and unit tests per commit; scripted but manually supervised deploys; artifacts may be rebuilt per stage. | A standardized pipeline promotes one immutable artifact through envs with automated gates; canary/blue-green; auto change records. | Progressive delivery with metric-driven rollback; release decoupled via flags; pipeline self-improves; compliance evidence automatic. |
| Infrastructure as code and configuration | Infrastructure provisioned manually; inconsistent, undocumented environments; slow, uncertain recovery. | Some infrastructure scripted, but practices vary; inconsistent state; common drift; policy enforced by manual review. | Declarative IaC standard from shared versioned modules with remote state; policy-as-code guardrails; regular drift detection. | Immutable, GitOps-driven, self-healing infrastructure; compliance evidence automatic; module and policy library continuously improves. |
| Containers, orchestration, cloud-native | Containers used ad hoc; hand-built unscanned images; manual deploy; no shared platform or isolation model. | Teams containerize and use an orchestrator, but practices vary; inconsistent scanning and limits; ungoverned cost and tenancy. | A standardized platform with hardened images, signing/scanning gates, namespace tenancy with quotas and network policy, cost allocation. | Self-service, self-healing platform; strong multi-tenancy; automated FinOps cost optimization; portable, hybrid/sovereign-ready. |
| Platform engineering and DevEx | No platform; each team assembles its own tooling inconsistently; ticket-driven handoffs; high cognitive load. | Some shared tools and templates, but fragmented and partly manual; limited self-service; DevEx unmeasured. | A platform team runs golden paths, self-service provisioning, a developer portal, and scorecards; guardrails in paved roads; DevEx measured. | A mature platform product with high voluntary adoption, improved from feedback; cognitive load managed; governance invisible in the workflow. |
| Test and process automation | Testing and ops largely manual; inconsistent coverage; procedures in heads or stale docs; compliance evidence by hand. | Automated tests exist but slow/flaky and run inconsistently; some operational scripts; manual remediation; periodic-review governance. | Fast, parallel, reliable test infra; codified runbooks; ChatOps; auto-generated compliance evidence; governance as automated checks. | Automated remediation of routine incidents with safeguards; continuous, always-audit-ready compliance; humans focus on judgment. |

## Part 9 — Operations, Reliability, and Observability

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Site reliability engineering | Operations manual and reactive; no SLOs; reliability is opinion; the same incidents recur; firefighting dominates. | Key services have basic SLIs/SLOs; some monitoring and alerting; toil acknowledged but unmeasured; inconsistent postmortems. | Error budgets influence prioritization; toil measured and capped; routine capacity planning; funded automation; PRR and engagement model. | Error-budget policy automated and respected; toil consistently low; self-service ops; proactive capacity; data-informed velocity/stability trade-offs. |
| Observability and monitoring | Basic uptime checks and unstructured logs per machine; debugging means SSH; noisy, ignored alerts. | Centralized metrics and log aggregation; some dashboards and threshold alerts; partial/absent traces; manual correlation. | OpenTelemetry instrumentation with propagated trace IDs; structured logs, tracing, curated dashboards, SLO symptom alerting; sustainable on-call. | High-cardinality, event-rich observability for ad hoc investigation; burn-rate alerting; cost-optimized retention; telemetry informs decisions. |
| Incident management | Incidents handled ad hoc by whoever notices; no roles, severities, or postmortems; informal on-call; failures recur. | Basic on-call rotations and severities; some postmortems, but unclear roles and inconsistently tracked corrective actions. | A formal incident command system with clear roles and criteria; blameless postmortems standard; actions tracked; on-call compensated. | Response is rehearsed via game days; on-call sustainable and quiet; aggregate analysis drives structural investment; incident rate trends down. |
| Cost, sustainability, green software | Cloud costs are a monthly surprise; no tagging, allocation, or carbon awareness; generous, unrevisited provisioning. | Basic cost visibility and tagging; some reactive rightsizing and idle cleanup; sustainability acknowledged but unmeasured. | A FinOps practice with attribution, budgets, forecasts, anomaly alerts, commitments, rightsizing; carbon measured for major services. | Cost and carbon are continuous team-owned signals; efficient defaults and automated optimization; carbon-aware scheduling; transparent reporting. |

## Part 10 — Program Delivery, Risk, and the Enterprise/Government Context

| Topic | Level 1 Initial | Level 2 Managed | Level 3 Defined | Level 4 Optimizing |
| --- | --- | --- | --- | --- |
| Portfolio and program management | Priorities set ad hoc by whoever asks loudest; no portfolio view; dependencies surface as crises; annual funding scrambles. | A periodically reviewed portfolio inventory; published objectives weakly linked to work; a dependency register; project-based budgeting. | Strategy cascades via OKRs; a consistent prioritization framework; cross-team planning manages dependencies; persistent team funding. | The portfolio is continuously rebalanced on outcome evidence; dependencies designed away; funding cadence matches learning cadence. |
| Risk, audit, and assurance | Risk handled reactively after incidents; no framework or register; undocumented controls; painful manual audits. | Risk registers for major systems; a control framework adopted, audits pass but manual and point-in-time; suppliers assessed at onboarding. | Three-lines model and common framework org-wide; many controls automated; continuous monitoring; supplier/SBOM inventories; scheduled DR. | Assurance is continuous and largely automated; auditors sample live evidence; explicit risk appetite; supply-chain integrity verified. |
| Procurement, open source, licensing | Open source added freely; no policy or inventory; licenses unexamined; end-of-life found by accident; no owner. | A basic policy and approved-license list; some manual/late scanning; an inventory for major systems; ad hoc contribution. | An OSPO owns strategy and tooling; automated license/vuln scanning and attribution; SBOMs; clear contribution; EOL tracked. | Open source is a managed strategic asset; fully automated compliance; deliberate upstream investment; continuous currency and EOL management. |
| Sustaining large and long-lived systems | Systems depend on heroes; ownership by memory; undocumented knowledge; systems frozen until they break; retirements never finish. | Ownership assigned and recorded for major systems; some docs and runbooks; obvious critical functions have a backup person; reactive maintenance. | Team-level ownership in a catalog surviving reorgs; bus factor measured and mitigated; decision records and runbooks; incremental modernization. | Stewardship is a funded discipline; no critical system is a single point of human failure; continuous knowledge transfer; planned endings. |
| Ethics, accountability, public interest | Ethics unaddressed or reactive after scandal; accessibility ignored; opaque automated decisions with no recourse; bias untested. | A code of conduct and some (late) accessibility; high-profile automated decisions get some oversight; occasional bias checks. | Ethical review is part of the process; accessibility designed in and user-tested; consequential decisions carry explanation and recourse. | Responsibility is embedded in how the org builds; equity is a non-negotiable default; algorithmic accountability is standard and monitored. |

---

## Overall maturity self-assessment

Use the matrices above to produce a lightweight, honest score.

### Scoring rubric

1. **Score each chapter 1.1–1.4** using the level whose description best matches your
   *typical* reality. When behavior is inconsistent, score the lower level.
2. **Average by Part.** Sum the chapter scores in a Part and divide by the number
   of chapters. This gives a per-Part maturity (e.g., "Part IV averages 2.5").
3. **Record the minimum, not just the mean.** A Part that averages 3.0 but
   contains a Level 1 chapter carries that chapter's risk regardless of the mean.
4. **Plot the trend.** Re-score every quarter or two and watch direction of
   travel. A domain moving 2 → 3 is healthier than one stuck at a static 3.

A simple worksheet per Part:

| Part | Chapters scored | Average (mean) | Lowest chapter | Notes / priority |
| --- | --- | --- | --- | --- |
| I–X | count | mean | min level | ... |

### Prioritizing what to improve

Do not try to raise everything at once, and do not chase the highest average.
Prioritize by **risk-weighted maturity gap**: attack the domains where a low
level meets high consequence.

- **First:** the lowest-maturity chapters in your highest-risk domains — for most
  organizations that means security, privacy, reliability, compliance, and any
  system whose failure harms people or violates law. A Level 1 here is urgent.
- **Next:** foundational enablers (culture, ways of working, CI/CD, IaC,
  observability) that raise the ceiling for every other domain. Improving these
  makes later gains cheaper.
- **Later:** domains that are already at Level 3 and merely could reach Level 4.
  Only push to Level 4 where the stakes and scale justify the added investment.

### The enterprise and government baseline

Enterprise and government contexts usually cannot stop at "it works." To pass
audits, sustain authorizations, and meet regulatory and public-accountability
obligations, most domains must reach **at least Level 3 (Defined)** — the level
where practices are standardized, documented, enforced across teams, and produce
evidence. Level 2 typically fails audit because it is inconsistent and
manually assembled under deadline; Level 1 fails outright.

Read Level 3 as the floor for anything auditable or safety-relevant, and Level 4
as the target only where continuous assurance, scale, or public trust make the
extra rigor worth it. Maturity remains a means: the aim is a defensible,
proportionate level of control for the risk you actually carry — not a perfect
score.
