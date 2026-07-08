# Roadmap, build backlog, and adoption checklists

This is the authoring backlog for producing and maintaining the guidebook, plus
adoption checklists organizations can use to put the recommendations into practice.

---


Actionable task backlog for producing the guidebook outlined above, plus
adoption checklists organizations can use to put the recommendations into
practice. Tasks are grouped by phase and sized for parallel work across
contributors.

Legend: `[ ]` todo · `[~]` in progress · `[x]` done · **(P)** parallelizable ·
**(gov)** government-specific · **(ent)** enterprise-specific.

---

## Phase 0: Project setup and standards

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

## Phase 1: Research and evidence base **(P)**

- [ ] Survey canonical sources per domain (books, standards, papers, industry reports)
- [ ] Catalog relevant standards and frameworks (ISO, NIST, OWASP, WCAG, etc.)
- [ ] Collect enterprise case studies and post-incident learnings
- [ ] Collect government/public-sector references (FedRAMP, GDS, USDS, 18F, gov.uk)
- [ ] Gather industry benchmarks (DORA, SPACE, State of DevOps, security reports)
- [ ] Identify subject-matter reviewers per domain
- [ ] Log open questions and areas of genuine disagreement to represent fairly

---

## Phase 2: Author Part I: Foundations (Culture, People, Process) **(P)**

- [ ] Ch. 1 Engineering culture and values
- [ ] Ch. 2 Team topologies and organizational design
- [ ] Ch. 3 Roles, career ladders, and growth
- [ ] Ch. 4 Ways of working (agile, scaling frameworks)
- [ ] Ch. 5 Decision-making and governance (ADRs, RFCs, tech debt)

## Phase 3: Author Part II: Programming Craft and Code Quality **(P)**

- [ ] Ch. 6 Coding standards and style
- [ ] Ch. 7 Software design principles
- [ ] Ch. 8 APIs and interface design
- [ ] Ch. 9 Testing strategy
- [ ] Ch. 10 Code review and collaboration
- [ ] Ch. 11 Version control and source management
- [ ] Ch. 12 Documentation

## Phase 4: Author Part III: Architecture and Systems **(P)**

- [ ] Ch. 13 Architecture fundamentals
- [ ] Ch. 14 Architectural styles and patterns
- [ ] Ch. 15 Distributed systems
- [ ] Ch. 16 Data architecture and storage
- [ ] Ch. 17 Scalability, performance, and resilience
- [ ] Ch. 18 Legacy modernization **(gov)(ent)**

## Phase 5: Author Part IV: Security, Privacy, and Trust **(P)**

- [ ] Ch. 19 Security foundations and culture
- [ ] Ch. 20 Application security
- [ ] Ch. 21 Infrastructure and cloud security
- [ ] Ch. 22 Security operations
- [ ] Ch. 23 Privacy and data protection
- [ ] Ch. 24 Compliance and governance **(gov)(ent)**

## Phase 6: Author Part V: UI, UX, and Product Design **(P)**

- [ ] Ch. 25 UX foundations
- [ ] Ch. 26 UI design and design systems
- [ ] Ch. 27 Accessibility **(gov)**
- [ ] Ch. 28 Content and communication design
- [ ] Ch. 29 Internationalization and localization
- [ ] Ch. 30 Frontend engineering

## Phase 7: Author Part VI: Artificial Intelligence and ML **(P)**

- [ ] Ch. 31 AI strategy and readiness
- [ ] Ch. 32 Machine learning engineering (MLOps)
- [ ] Ch. 33 Generative AI and LLM applications
- [ ] Ch. 34 AI-assisted software development
- [ ] Ch. 35 Responsible and trustworthy AI
- [ ] Ch. 36 AI infrastructure and operations

## Phase 8: Author Part VII: Data, Analytics, and Insight **(P)**

- [ ] Ch. 37 Data strategy and governance
- [ ] Ch. 38 Data engineering
- [ ] Ch. 39 Analytics and business intelligence
- [ ] Ch. 40 Product analytics and experimentation
- [ ] Ch. 41 Decision science and data-informed culture

## Phase 9: Author Part VIII: Automation, DevOps, Platform Engineering **(P)**

- [ ] Ch. 42 CI/CD and delivery
- [ ] Ch. 43 Infrastructure as code and configuration
- [ ] Ch. 44 Containers, orchestration, and cloud-native
- [ ] Ch. 45 Platform engineering and developer experience
- [ ] Ch. 46 Test and process automation

## Phase 10: Author Part IX: Operations, Reliability, Observability **(P)**

- [ ] Ch. 47 Site reliability engineering
- [ ] Ch. 48 Observability and monitoring
- [ ] Ch. 49 Incident management
- [ ] Ch. 50 Cost, sustainability, and green software

## Phase 11: Author Part X: Program Delivery, Risk, Enterprise/Gov **(P)**

- [ ] Ch. 51 Portfolio and program management
- [ ] Ch. 52 Risk, audit, and assurance
- [ ] Ch. 53 Procurement, open source, and licensing
- [ ] Ch. 54 Sustaining large and long-lived systems
- [ ] Ch. 55 Ethics, accountability, and public interest

---

## Phase 11b: Author Part XI: Flow (Discovery and Delivery Pipelines)

- [x] Ch. 56 The discovery pipeline (OKRs, KPIs, quality attributes, SMART, dual-track discovery)
- [x] Ch. 57 The delivery pipeline (test automation, CI/CD, deployment, DORA/outcome metrics, feedback loop)

## Phase 12: Appendices and reference material

- [x] A. Compile glossary of terms and acronyms
- [x] B. Assemble checklists (review, launch, audit, incident, threat model)
- [x] C. Assemble templates (ADR, RFC, postmortem, threat model, runbook)
- [x] D. Finalize maturity models per domain
- [x] E. Build reference/standards index with citations
- [x] F. Curate recommended reading list
- [x] G. Write the incremental adoption roadmap

---

## Phase 13: Review, quality, and release

- [ ] Technical review by subject-matter experts per part
- [x] Cross-chapter consistency pass (terminology, cross-references, overlap)
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

