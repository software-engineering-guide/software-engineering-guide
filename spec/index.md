# Software Engineering Recommendations — Specification

This is the single source of truth for the guidebook's structure and build
plan. It merges the outline (parts, chapters, and appendices) with the
authoring backlog and adoption checklists. The rendered book lives in
`../README.md` (table of contents), `../chapters/` (one folder per part), and
`../appendices/`.

---

# Guidebook outline

A comprehensive guidebook of best practices for large software developer teams,
including enterprise and government organizations. It spans engineering
culture, programming craft, architecture, security, AI, data and analytics,
UI/UX, automation, delivery, and operations — and treats compliance, scale,
and long-lived systems as first-class concerns.

## Purpose and audience

- **Purpose:** Give large teams a shared, opinionated baseline of practices
  that scale across hundreds or thousands of engineers, multiple business
  units, and multi-year (often multi-decade) system lifetimes.
- **Primary audience:** Engineering leaders, staff/principal engineers,
  architects, platform teams, security teams, and program managers in
  enterprise and government contexts.
- **Secondary audience:** Individual contributors who want to understand the
  "why" behind organizational standards.
- **How to read it:** Each chapter states principles first, then concrete
  recommendations, then trade-offs and anti-patterns. Adopt incrementally;
  do not big-bang.
- **Numbering:** Parts use whole numbers; chapters use decimals. Chapter
  **N.0** introduces each part; **N.1, N.2, …** are its chapters.

## Guiding principles (the spine of the book)

1. **Optimize for the team and the decade, not the individual and the sprint.**
2. **Make the right thing the easy thing** — invest in paved roads and golden paths.
3. **Prefer boring, proven technology; reserve novelty budget for differentiators.**
4. **Everything as code** — infrastructure, policy, pipelines, docs, and configuration.
5. **Shift left, and shift everywhere** — quality, security, and accessibility early and continuous.
6. **Automate toil; reserve human judgment for design, risk, and ethics.**
7. **Measure outcomes, not activity** — instrument, learn, and iterate.
8. **Design for failure, change, and audit** — assume incidents, turnover, and scrutiny.
9. **Least privilege and least surprise** — in security and in APIs alike.
10. **Inclusive by default** — accessible, internationalized, and equitable.

---

## Part 1 — Foundations: Culture, People, and Process

### 1.1 Engineering culture and values
- Psychological safety, blameless learning, and healthy incident culture
- Ownership models: "you build it, you run it" vs. platform/ops separation
- Writing culture: design docs, RFCs, decision records
- Craft, sustainable pace, and avoiding hero culture
- Diversity, equity, inclusion, and belonging as engineering strengths

### 1.2 Team topologies and organizational design
- Stream-aligned, platform, enabling, and complicated-subsystem teams
- Conway's Law and the inverse maneuver: org design as architecture
- Team sizing, cognitive load, and the "two-pizza" heuristic at scale
- Internal open source (InnerSource) and code ownership boundaries
- Centralized vs. federated vs. embedded models for security, data, and design

### 1.3 Roles, career ladders, and growth
- IC and management tracks; staff+ engineering archetypes
- Competency matrices and leveling calibration
- Mentorship, sponsorship, and on-call apprenticeship
- Hiring, structured interviews, and reducing bias

### 1.4 Ways of working
- Agile, Scrum, Kanban, and Lean — choosing and adapting, not cargo-culting
- Scaling frameworks (SAFe, LeSS, Spotify-model) — benefits and cautions
- Estimation, planning, and the limits of story points
- Meetings, async communication, and documentation-first collaboration
- Working across time zones, contractors, and vendor teams (common in gov/enterprise)

### 1.5 Decision-making and governance
- Architecture Decision Records (ADRs) and RFC processes
- Technical steering, architecture review boards, and paved-road governance
- Build vs. buy vs. adopt (open source) decision frameworks
- Managing technical debt as a portfolio, not a backlog afterthought
- Escalation paths and reversible vs. irreversible ("one-way door") decisions

### 1.6 Decision records
- Capturing decisions with context and consequences (ADRs and beyond)
- Templates (Nygard, MADR, Y-statements); lightweight vs. heavyweight
- In-repo decision logs, naming, and immutable vs. living records
- Lifecycle, governance, and preferring "decisions" over "ADRs"
- Making decisions discoverable and testable with fitness functions

---

## Part 2 — Programming Craft and Code Quality

### 2.1 Coding standards and style
- Language style guides, linters, and formatters as enforced defaults
- Naming, readability, and code as communication
- Consistency across polyglot codebases
- Idioms, paradigms, and choosing the right tool per problem

### 2.2 Software design principles
- SOLID, DRY, KISS, YAGNI — and when each misleads
- Coupling, cohesion, and separation of concerns
- Design patterns and anti-patterns; when patterns become liabilities
- Domain-Driven Design: bounded contexts, ubiquitous language, aggregates
- Functional, object-oriented, and data-oriented approaches

### 2.3 APIs and interface design
- API-first development and contract-driven design
- REST, GraphQL, gRPC, and event-driven interfaces — selection criteria
- Versioning, deprecation, and backward compatibility
- API governance, style guides, and developer experience (DX)
- Idempotency, pagination, error semantics, and rate limiting

### 2.4 Testing strategy
- The test pyramid (and its critiques): unit, integration, end-to-end, contract
- Test-driven and behavior-driven development
- Property-based, fuzz, mutation, and snapshot testing
- Test data management, fixtures, and synthetic data
- Flaky-test management, coverage as a signal (not a target), and quality gates
- Accessibility, performance, and security testing as part of the strategy

### 2.5 Code review and collaboration
- Effective pull requests: size, description, and scope
- Review standards, checklists, and reviewer responsibilities
- Pair and mob programming; when synchronous beats asynchronous
- Automated review: linters, static analysis, and AI-assisted review
- Feedback norms and reducing review latency

### 2.6 Version control and source management
- Trunk-based development vs. long-lived branches
- Branching models (GitFlow, GitHub Flow) and their trade-offs
- Monorepo vs. polyrepo; tooling implications at scale
- Commit hygiene, conventional commits, and meaningful history
- Managing large binaries, generated code, and secrets out of history

### 2.7 Documentation
- Docs-as-code and treating docs as first-class deliverables
- The Diátaxis framework: tutorials, how-tos, reference, explanation
- READMEs, runbooks, architecture docs, and onboarding guides
- API docs, changelogs, and living documentation
- Knowledge management and fighting documentation rot

---

## Part 3 — Architecture and Systems

### 3.1 Architecture fundamentals
- Quality attributes: scalability, availability, performance, maintainability, evolvability
- The "-ilities" and architecturally significant requirements
- Fitness functions and evolutionary architecture
- Documenting architecture: C4 model, arc42, views and viewpoints
- Architecture trade-off analysis and risk-driven design

### 3.2 Architectural styles and patterns
- Monoliths, modular monoliths, microservices, and when to split
- Event-driven architecture, CQRS, and event sourcing
- Service mesh, API gateways, and the BFF pattern
- Serverless and function-as-a-service trade-offs
- Hexagonal/ports-and-adapters, clean architecture, and layering

### 3.3 Distributed systems
- CAP, PACELC, and consistency models
- Idempotency, retries, timeouts, backoff, and circuit breakers
- Saga patterns, distributed transactions, and eventual consistency
- Messaging, queues, streaming, and exactly-once illusions
- Observability of distributed flows: tracing and correlation

### 3.4 Data architecture and storage
- Relational, document, key-value, graph, columnar, and time-series stores
- Polyglot persistence and choosing the right store
- Data modeling, normalization, and schema evolution/migrations
- Caching strategies, CDNs, and invalidation
- Transactions, locking, and concurrency at scale

### 3.5 Scalability, performance, and resilience
- Horizontal vs. vertical scaling; statelessness and sharding
- Load balancing, autoscaling, and capacity planning
- Performance engineering: profiling, benchmarking, and budgets
- Resilience patterns: bulkheads, graceful degradation, chaos engineering
- Multi-region, disaster recovery, RTO/RPO, and business continuity

### 3.6 Legacy modernization
- Strangler fig, branch-by-abstraction, and incremental migration
- Assessing and prioritizing legacy risk (common in gov/enterprise)
- Mainframe, COBOL, and long-lived system stewardship
- Data migration strategies and dual-running
- Managing the "big rewrite" temptation

---

## Part 4 — Security, Privacy, and Trust

### 4.1 Security foundations and culture
- Security as everyone's job; the security champions model
- Threat modeling (STRIDE, PASTA, attack trees) as a routine practice
- Secure SDLC and shifting security left
- Defense in depth, least privilege, and zero-trust principles
- The CIA triad and risk-based prioritization

### 4.2 Application security
- OWASP Top 10 and ASVS as baselines
- Input validation, output encoding, and injection prevention
- Authentication, authorization, session management, and OAuth/OIDC
- Secrets management, key rotation, and avoiding hardcoded credentials
- Dependency and supply-chain security (SBOM, SLSA, signing, provenance)

### 4.3 Infrastructure and cloud security
- Identity and access management (IAM), RBAC, and ABAC
- Network security, segmentation, and micro-segmentation
- Encryption in transit and at rest; key management (KMS/HSM)
- Container, Kubernetes, and serverless security
- Cloud security posture management and misconfiguration prevention

### 4.4 Security operations
- DevSecOps and security automation in pipelines (SAST, DAST, SCA, IaC scanning)
- Vulnerability management, patching, and coordinated disclosure
- Incident response, forensics, and breach communication
- Security monitoring, SIEM, SOAR, and detection engineering
- Red teaming, purple teaming, and penetration testing

### 4.5 Privacy and data protection
- Privacy by design and by default
- Data minimization, retention, and the right to erasure
- PII/PHI handling, classification, and tokenization
- Consent management and lawful basis for processing
- Cross-border data transfer and data residency

### 4.6 Compliance and governance (enterprise and government)
- Regulatory landscape: GDPR, CCPA, HIPAA, PCI-DSS, SOX
- Government frameworks: FedRAMP, FISMA, NIST 800-53/171, CMMC, IL levels
- Accessibility mandates: Section 508, ADA, WCAG, EN 301 549
- Audit readiness, evidence collection, and continuous compliance
- Frameworks: ISO 27001, SOC 2, NIST CSF; mapping controls to practice
- Records management, FOIA, and public-sector transparency obligations

---

## Part 5 — UI, UX, and Product Design

### 5.1 UX foundations
- User-centered and human-centered design processes
- Research methods: interviews, usability testing, surveys, analytics
- Personas, journey maps, jobs-to-be-done, and service blueprints
- Information architecture and interaction design
- Design thinking and double-diamond, applied pragmatically

### 5.2 UI design and design systems
- Design systems, component libraries, and design tokens
- Visual hierarchy, typography, color, layout, and grids
- Responsive, adaptive, and mobile-first design
- Design-to-development handoff and design-code parity
- Consistency, theming, and white-labeling at enterprise scale

### 5.3 Accessibility (a11y)
- WCAG 2.2/3.0 principles: perceivable, operable, understandable, robust
- Keyboard, screen reader, and assistive technology support
- ARIA, semantic HTML, and accessible components
- Automated and manual accessibility testing
- Accessibility as legal requirement (esp. government) and as good design

### 5.4 Content and communication design
- Content strategy, microcopy, and UX writing
- Plain language (a legal requirement in many governments)
- Error messages, empty states, and helpful defaults
- Design for trust, safety, and reducing dark patterns
- Notifications, email, and multi-channel content

### 5.5 Internationalization and localization
- i18n architecture: locale, encoding, and text expansion
- Localization workflows and translation management
- Right-to-left, plurals, dates, currencies, and cultural adaptation
- Global vs. regional product considerations

### 5.6 Frontend engineering
- Framework selection and longevity considerations
- State management, rendering strategies (SSR/SSG/CSR/streaming)
- Performance: Core Web Vitals, bundle budgets, lazy loading
- Progressive enhancement and resilience
- Cross-browser, cross-device, and offline-first strategies

---

## Part 6 — Artificial Intelligence and Machine Learning

### 6.1 AI strategy and readiness
- Where AI helps and where it does not; problem framing
- Build vs. buy vs. fine-tune vs. prompt; the AI decision tree
- Data readiness, talent, and platform prerequisites
- AI in regulated and government contexts (procurement, transparency)
- Total cost of ownership and vendor lock-in

### 6.2 Machine learning engineering (MLOps)
- The ML lifecycle: data, features, training, evaluation, deployment
- Feature stores, experiment tracking, and model registries
- Reproducibility, versioning of data and models, and lineage
- Model deployment patterns: batch, online, streaming, edge
- Monitoring for drift, degradation, and data-quality issues

### 6.3 Generative AI and LLM applications
- Prompt engineering, context management, and system design
- Retrieval-augmented generation (RAG) and knowledge grounding
- Agents, tool use, and orchestration patterns
- Evaluation of generative systems (offline, online, human-in-the-loop)
- Guardrails, hallucination mitigation, and output validation

### 6.4 AI-assisted software development
- AI pair programming and code-generation tools
- Review, testing, and verification of AI-generated code
- Productivity measurement and realistic expectations
- Security and licensing risks of AI-generated code
- Team norms, disclosure, and skill maintenance

### 6.5 Responsible and trustworthy AI
- Fairness, bias detection, and mitigation
- Explainability, interpretability, and transparency
- Governance frameworks: NIST AI RMF, EU AI Act, ISO/IEC 42001
- Human oversight, accountability, and appeal mechanisms
- Privacy, safety, red-teaming, and misuse prevention
- Environmental cost and sustainability of AI

### 6.6 AI infrastructure and operations
- Compute (GPU/TPU) planning, cost control, and scheduling
- Vector databases, embeddings, and retrieval infrastructure
- Model serving, batching, caching, and latency optimization
- LLMOps: prompt versioning, evaluation pipelines, and observability

---

## Part 7 — Data, Analytics, and Insight

### 7.1 Data strategy and governance
- Data as a product; ownership, contracts, and SLAs
- Data governance, stewardship, and cataloging
- Master data management and single source of truth
- Data quality dimensions and observability
- Data mesh vs. data lakehouse vs. warehouse — organizational fit

### 7.2 Data engineering
- ETL vs. ELT and modern data stacks
- Batch and streaming pipelines; orchestration
- Data modeling for analytics (star schemas, dimensional, wide tables)
- Idempotent, testable, and observable pipelines
- Storage formats, partitioning, and cost optimization

### 7.3 Analytics and business intelligence
- Descriptive, diagnostic, predictive, and prescriptive analytics
- Metrics frameworks, semantic layers, and metric governance
- Dashboards, self-service BI, and avoiding dashboard sprawl
- Data visualization principles and honest charts
- Embedded analytics and operational reporting

### 7.4 Product analytics and experimentation
- Event instrumentation, tracking plans, and taxonomy
- Funnels, cohorts, retention, and engagement metrics
- A/B testing, experimentation platforms, and statistical rigor
- North-star metrics and avoiding vanity metrics
- Privacy-respecting analytics and consent

### 7.5 Decision science and data-informed culture
- From data to decisions; avoiding data theater
- Causality, confounding, and correlation traps
- Communicating uncertainty to stakeholders
- Building a measurement culture without surveillance

---

## Part 8 — Automation, DevOps, and Platform Engineering

### 8.1 CI/CD and delivery
- Continuous integration, delivery, and deployment distinctions
- Pipeline design, quality gates, and fast feedback
- Deployment strategies: blue-green, canary, rolling, feature flags
- Progressive delivery and automated rollback
- Release management and change control in regulated environments

### 8.2 Infrastructure as code and configuration
- Declarative IaC (Terraform, Pulumi, CloudFormation) and modules
- Immutable infrastructure and golden images
- Configuration management and drift detection
- GitOps and pull-based deployment
- Policy as code (OPA, Sentinel) and guardrails

### 8.3 Containers, orchestration, and cloud-native
- Containerization best practices and image hygiene
- Kubernetes patterns, operators, and multi-tenancy
- Cloud-native design (12-factor and beyond)
- Multi-cloud, hybrid-cloud, and sovereign-cloud considerations
- Cost management and FinOps

### 8.4 Platform engineering and developer experience
- Internal developer platforms (IDPs) and golden paths
- Self-service infrastructure and paved roads
- Developer portals, service catalogs, and scorecards
- Measuring and improving developer productivity (DevEx, SPACE)
- Reducing cognitive load and undifferentiated heavy lifting

### 8.5 Test and process automation
- Automated testing infrastructure and parallelization
- Release, compliance, and evidence automation
- ChatOps, runbooks-as-code, and automated remediation
- Robotic process automation (RPA) and its place
- Automating governance, security, and cost controls

---

## Part 9 — Operations, Reliability, and Observability

### 9.1 Site reliability engineering
- SLIs, SLOs, SLAs, and error budgets
- Toil reduction and the automation mandate
- Capacity planning and demand forecasting
- Reliability as a feature and the cost of nines
- Embedding vs. centralizing SRE

### 9.2 Observability and monitoring
- The three pillars: metrics, logs, traces (and beyond)
- OpenTelemetry, structured logging, and correlation
- Alerting philosophy: actionable, symptom-based, low-noise
- Dashboards, SLO monitoring, and health modeling
- Debugging in production and high-cardinality observability

### 9.3 Incident management
- On-call practices, rotations, and sustainable load
- Incident command, severity levels, and roles
- Communication during incidents (internal and public)
- Blameless postmortems and corrective actions
- Learning from incidents and organizational memory

### 9.4 Cost, sustainability, and green software
- FinOps: visibility, optimization, and accountability
- Carbon-aware and energy-efficient software
- Sustainable architecture and rightsizing
- Balancing cost, performance, and reliability

---

## Part 10 — Program Delivery, Risk, and the Enterprise/Government Context

### 10.1 Portfolio and program management
- Aligning engineering with strategy and OKRs
- Roadmapping, prioritization frameworks, and trade-offs
- Managing dependencies across many teams
- Vendor, contractor, and systems-integrator management
- Procurement, budgeting, and multi-year funding cycles (government)

### 10.2 Risk, audit, and assurance
- Enterprise risk management applied to software
- Third-party risk and supply-chain assurance
- Audit trails, evidence, and continuous controls monitoring
- Business continuity and disaster-recovery governance
- Managing concentration risk and single points of failure

### 10.3 Procurement, open source, and licensing
- Open source strategy, consumption, and contribution policy
- License compliance, obligations, and copyleft risk
- Open source program offices (OSPOs)
- Government open-source and "public money, public code" mandates
- Managing dependencies and end-of-life software

### 10.4 Sustaining large and long-lived systems
- Stewardship, ownership continuity, and bus-factor mitigation
- Deprecation, sunsetting, and end-of-life planning
- Knowledge transfer and reducing key-person risk
- Managing 10-, 20-, and 30-year systems
- Balancing innovation with stability and citizen/customer trust

### 10.5 Ethics, accountability, and public interest
- Professional ethics and codes of conduct
- Accessibility and equity as obligations, not features
- Algorithmic accountability and public transparency
- Sustainability and social responsibility
- Serving citizens and customers with dignity and fairness

---

## Part 11 — Flow: Discovery and Delivery Pipelines

### 11.1 The discovery pipeline
- Deciding *what to build and why*, and defining success before delivery
- OKRs (objectives and key results) and cascading alignment
- KPIs, plus leading vs. lagging indicators and vanity-metric traps
- System quality attributes (the "-ilities") as explicit, quantified requirements
- SMART criteria for goals, key results, and acceptance criteria
- Continuous, dual-track discovery: hypotheses, opportunity–solution trees, experiments
- Closing the loop: outcome metrics re-entering discovery

### 11.2 The delivery pipeline
- Turning validated ideas into running, measured software
- Test automation and quality gates
- CI/CD: continuous integration, delivery, and deployment
- Deployment strategies: feature flags, canary, blue-green, progressive delivery
- Separating deploy from release; reversibility and automated rollback
- Outcome metrics: DORA four keys, flow metrics, SLOs, and business outcomes
- The pipeline as a compliance control; closing the loop back to discovery

### 11.3 Queueing theory
- Waiting lines behind tickets, kanban, message queues, and pipelines
- Notation: arrival/service rates, utilization, lead/wait/work time
- Little's Law; lead time = WIP ÷ throughput; utilization non-linearity
- Queue of queues; funnels; the seven insights; bottlenecks
- Mapping queue metrics to DORA, SLIs/SLOs, and flow KPIs

---

## Part 12 — Project Management

### 12.1 Project management
- Predictive, adaptive, and hybrid delivery; PMBOK and PRINCE2
- Scope, schedule, cost, quality — the triple constraint
- Estimation as ranges; empirical, flow-based forecasting
- Dependencies, critical path, and the living risk register
- Stakeholder engagement and transparent status

### 12.2 Agile
- The Agile Manifesto: values and principles over ceremonies
- Scrum, Kanban, XP, and Scrumban as starting points
- Technical excellence; scaling with care and descaling
- Agile in enterprise and government; agile procurement
- Continuous improvement and outcome-based measurement

---

## Appendices

- **A. Glossary** of terms and acronyms
- **B. Checklists** — quick-reference for reviews, launches, and audits
- **C. Templates** — ADRs, RFCs, postmortems, threat models, runbooks
- **D. Maturity models** — assessing and leveling up each domain
- **E. Reference standards and frameworks** — index with citations
- **F. Recommended reading** — books, papers, and canonical sources
- **G. Adoption roadmap** — how to roll out these practices incrementally

---

## Cross-cutting themes (woven through every part)

- **Security, privacy, and accessibility** are not chapters to visit once; they
  appear in every domain.
- **Automation and "everything as code"** underpin repeatability and audit.
- **Measurement and feedback loops** turn practices into learning systems.
- **Documentation and knowledge continuity** protect against turnover and scale.
- **Regulatory and government constraints** are treated as design inputs, not
  afterthoughts.


---

# Build backlog and adoption checklists

Actionable task backlog for producing the guidebook outlined above, plus
adoption checklists organizations can use to put the recommendations into
practice. Tasks are grouped by phase and sized for parallel work across
contributors.

Legend: `[ ]` todo · `[~]` in progress · `[x]` done · **(P)** parallelizable ·
**(gov)** government-specific · **(ent)** enterprise-specific.

---

## Phase 0 — Project setup and standards

- [ ] Define the guidebook's scope, non-goals, and target audiences
- [ ] Establish a style guide (voice, tone, terminology, plain language)
- [ ] Choose docs-as-code tooling (static site generator, linting, CI)
- [ ] Set up the repository structure: one file/section per chapter
- [ ] Create contribution guide, PR template, and review checklist
- [ ] Define the per-chapter template: principles → recommendations → trade-offs → anti-patterns → checklist → references
- [ ] Set up citation/reference management and a master bibliography
- [ ] Establish a maturity-model rubric applied consistently across chapters
- [ ] Define accessibility and internationalization standards for the book itself

---

## Phase 1 — Research and evidence base **(P)**

- [ ] Survey canonical sources per domain (books, standards, papers, industry reports)
- [ ] Catalog relevant standards and frameworks (ISO, NIST, OWASP, WCAG, etc.)
- [ ] Collect enterprise case studies and post-incident learnings
- [ ] Collect government/public-sector references (FedRAMP, GDS, USDS, 18F, gov.uk)
- [ ] Gather industry benchmarks (DORA, SPACE, State of DevOps, security reports)
- [ ] Identify subject-matter reviewers per domain
- [ ] Log open questions and areas of genuine disagreement to represent fairly

---

## Phase 2 — Author Part I: Foundations (Culture, People, Process) **(P)**

- [ ] Ch. 1 Engineering culture and values
- [ ] Ch. 2 Team topologies and organizational design
- [ ] Ch. 3 Roles, career ladders, and growth
- [ ] Ch. 4 Ways of working (agile, scaling frameworks)
- [ ] Ch. 5 Decision-making and governance (ADRs, RFCs, tech debt)

## Phase 3 — Author Part II: Programming Craft and Code Quality **(P)**

- [ ] Ch. 6 Coding standards and style
- [ ] Ch. 7 Software design principles
- [ ] Ch. 8 APIs and interface design
- [ ] Ch. 9 Testing strategy
- [ ] Ch. 10 Code review and collaboration
- [ ] Ch. 11 Version control and source management
- [ ] Ch. 12 Documentation

## Phase 4 — Author Part III: Architecture and Systems **(P)**

- [ ] Ch. 13 Architecture fundamentals
- [ ] Ch. 14 Architectural styles and patterns
- [ ] Ch. 15 Distributed systems
- [ ] Ch. 16 Data architecture and storage
- [ ] Ch. 17 Scalability, performance, and resilience
- [ ] Ch. 18 Legacy modernization **(gov)(ent)**

## Phase 5 — Author Part IV: Security, Privacy, and Trust **(P)**

- [ ] Ch. 19 Security foundations and culture
- [ ] Ch. 20 Application security
- [ ] Ch. 21 Infrastructure and cloud security
- [ ] Ch. 22 Security operations
- [ ] Ch. 23 Privacy and data protection
- [ ] Ch. 24 Compliance and governance **(gov)(ent)**

## Phase 6 — Author Part V: UI, UX, and Product Design **(P)**

- [ ] Ch. 25 UX foundations
- [ ] Ch. 26 UI design and design systems
- [ ] Ch. 27 Accessibility **(gov)**
- [ ] Ch. 28 Content and communication design
- [ ] Ch. 29 Internationalization and localization
- [ ] Ch. 30 Frontend engineering

## Phase 7 — Author Part VI: Artificial Intelligence and ML **(P)**

- [ ] Ch. 31 AI strategy and readiness
- [ ] Ch. 32 Machine learning engineering (MLOps)
- [ ] Ch. 33 Generative AI and LLM applications
- [ ] Ch. 34 AI-assisted software development
- [ ] Ch. 35 Responsible and trustworthy AI
- [ ] Ch. 36 AI infrastructure and operations

## Phase 8 — Author Part VII: Data, Analytics, and Insight **(P)**

- [ ] Ch. 37 Data strategy and governance
- [ ] Ch. 38 Data engineering
- [ ] Ch. 39 Analytics and business intelligence
- [ ] Ch. 40 Product analytics and experimentation
- [ ] Ch. 41 Decision science and data-informed culture

## Phase 9 — Author Part VIII: Automation, DevOps, Platform Engineering **(P)**

- [ ] Ch. 42 CI/CD and delivery
- [ ] Ch. 43 Infrastructure as code and configuration
- [ ] Ch. 44 Containers, orchestration, and cloud-native
- [ ] Ch. 45 Platform engineering and developer experience
- [ ] Ch. 46 Test and process automation

## Phase 10 — Author Part IX: Operations, Reliability, Observability **(P)**

- [ ] Ch. 47 Site reliability engineering
- [ ] Ch. 48 Observability and monitoring
- [ ] Ch. 49 Incident management
- [ ] Ch. 50 Cost, sustainability, and green software

## Phase 11 — Author Part X: Program Delivery, Risk, Enterprise/Gov **(P)**

- [ ] Ch. 51 Portfolio and program management
- [ ] Ch. 52 Risk, audit, and assurance
- [ ] Ch. 53 Procurement, open source, and licensing
- [ ] Ch. 54 Sustaining large and long-lived systems
- [ ] Ch. 55 Ethics, accountability, and public interest

---

## Phase 11b — Author Part XI: Flow (Discovery and Delivery Pipelines)

- [x] Ch. 56 The discovery pipeline (OKRs, KPIs, quality attributes, SMART, dual-track discovery)
- [x] Ch. 57 The delivery pipeline (test automation, CI/CD, deployment, DORA/outcome metrics, feedback loop)

## Phase 12 — Appendices and reference material

- [x] A. Compile glossary of terms and acronyms
- [x] B. Assemble checklists (review, launch, audit, incident, threat model)
- [x] C. Assemble templates (ADR, RFC, postmortem, threat model, runbook)
- [x] D. Finalize maturity models per domain
- [x] E. Build reference/standards index with citations
- [x] F. Curate recommended reading list
- [x] G. Write the incremental adoption roadmap

---

## Phase 13 — Review, quality, and release

- [ ] Technical review by subject-matter experts per part
- [x] Cross-chapter consistency pass (terminology, cross-references, overlap) — see `consistency-report.md`
- [ ] Ensure cross-cutting themes (security, privacy, a11y, automation) appear everywhere
- [ ] Copyedit for plain language, tone, and readability
- [ ] Accessibility audit of the published guidebook (WCAG)
- [ ] Verify all citations, links, and standards references
- [ ] Legal/compliance review of regulatory claims **(gov)(ent)**
- [ ] Beta-read with target audience; collect and incorporate feedback
- [ ] Publish v1.0; establish versioning and update cadence
- [ ] Set up a mechanism for corrections, issues, and community contributions

---

## Adoption checklists (for organizations using the guidebook)

These are outcome checklists an organization can use to self-assess and roll
out the practices. Treat as a maturity journey, not a one-time audit.

### Foundations
- [ ] Documented engineering values and blameless incident culture
- [ ] Clear team topologies with explicit ownership boundaries
- [ ] Career ladders and calibration in place
- [ ] ADR/RFC process adopted and used
- [ ] Technical-debt managed as a visible portfolio

### Programming and quality
- [ ] Enforced formatting, linting, and static analysis in CI
- [ ] Defined testing strategy with meaningful quality gates
- [ ] Code review standards and reasonable review latency
- [ ] Trunk-based or well-governed branching model
- [ ] Docs-as-code with living, discoverable documentation

### Architecture
- [ ] Documented architecture (C4/arc42) and ADRs
- [ ] Quality attributes and fitness functions defined
- [ ] Resilience patterns and DR tested (RTO/RPO validated)
- [ ] Data architecture and migration strategy governed
- [ ] Legacy-modernization plan for critical systems

### Security and privacy
- [ ] Threat modeling routine in the SDLC
- [ ] Automated SAST/DAST/SCA/IaC scanning in pipelines
- [ ] Secrets management and key rotation enforced
- [ ] SBOM and supply-chain provenance in place
- [ ] Privacy by design; data classification and retention enforced
- [ ] Compliance controls mapped to frameworks **(gov)(ent)**
- [ ] Incident response plan tested via exercises

### UX and accessibility
- [ ] Design system and component library adopted
- [ ] Accessibility (WCAG) tested automatically and manually
- [ ] Plain-language and content standards applied
- [ ] i18n/l10n supported where needed
- [ ] Frontend performance budgets (Core Web Vitals) enforced

### AI and ML
- [ ] AI use cases prioritized against clear problem framing
- [ ] MLOps lifecycle with versioning, lineage, and monitoring
- [ ] Generative-AI guardrails and evaluation in place
- [ ] AI-generated code review and licensing policy defined
- [ ] Responsible-AI governance mapped (NIST AI RMF / EU AI Act / ISO 42001)

### Data and analytics
- [ ] Data governance, catalog, and ownership established
- [ ] Data-quality monitoring and observability in place
- [ ] Metrics/semantic layer with governed definitions
- [ ] Experimentation platform with statistical rigor
- [ ] Privacy-respecting analytics and consent management

### Automation and platform
- [ ] CI/CD with progressive delivery and automated rollback
- [ ] Infrastructure and policy as code with drift detection
- [ ] Internal developer platform / golden paths available
- [ ] Toil measured and systematically reduced
- [ ] FinOps visibility and cost accountability

### Operations and reliability
- [ ] SLOs and error budgets defined and monitored
- [ ] Observability with metrics, logs, and traces (OpenTelemetry)
- [ ] Actionable, low-noise alerting
- [ ] Sustainable on-call and blameless postmortems
- [ ] Sustainability/green-software practices considered

### Enterprise and government
- [ ] Portfolio aligned to strategy/OKRs with managed dependencies
- [ ] Third-party and supply-chain risk assessed
- [ ] Open source policy, OSPO, and license compliance
- [ ] Long-lived-system stewardship and bus-factor mitigation
- [ ] Ethics, accountability, and public-transparency obligations met

