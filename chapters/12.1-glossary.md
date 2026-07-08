# 12.1 Glossary

This glossary defines terms and acronyms used throughout the guidebook. Entries
are grouped alphabetically. Where an entry has a common acronym, it is shown in
parentheses. Definitions are intentionally concise; consult the relevant chapter
for fuller treatment.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: An authorization model that grants access based on evaluated attributes of the user, resource, action, and environment (for example, department, clearance, time of day) rather than fixed roles. It offers fine-grained, policy-driven control at the cost of greater complexity than RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: The practice of designing and building software so that people with disabilities can perceive, understand, navigate, and interact with it. The "a11y" numeronym abbreviates the 11 letters between "a" and "y."

**ADR (Architecture Decision Record)**: A short, versioned document that captures a single significant architectural or technical decision, its context, the options considered, and its consequences. ADRs create a durable, reviewable history of why a system is the way it is.

**Aggregate**: In Domain-Driven Design, a cluster of domain objects treated as a single unit for data changes, with one entity acting as the aggregate root that enforces invariants. Aggregates define consistency and transaction boundaries.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: A defined contract through which one piece of software requests services or data from another. Well-designed APIs hide implementation detail and provide stable, versioned interfaces.

**API-first**: A development approach in which the API contract is designed and agreed before implementation, so that consumers and providers can work in parallel against a shared specification.

**arc42**: An open, template-based structure for documenting software architecture, organized into twelve sections covering context, constraints, building blocks, runtime, deployment, and decisions.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: A W3C specification defining roles, states, and properties that make dynamic and custom web components understandable to assistive technologies such as screen readers.

**ASR (Architecturally Significant Requirement)**: A requirement that has a measurable, wide-reaching effect on architecture, such as a performance, availability, security, or regulatory constraint. ASRs drive the most consequential design decisions.

**ASVS (Application Security Verification Standard)**: An OWASP standard that provides a graded checklist of security requirements and tests for designing, building, and verifying secure applications.

**[Availability](https://en.wikipedia.org/wiki/Availability)**: The proportion of time a system is operational and able to serve requests, often expressed in "nines" (for example, 99.9%). It is a core reliability target codified in SLOs and SLAs.

## B

**[BDD (Behavior-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: A collaborative practice that expresses requirements as concrete, human-readable examples of behavior (often in Given/When/Then form) that double as automated acceptance tests.

**BFF (Backend for Frontend)**: An architectural pattern in which a dedicated backend service is built for a specific frontend or client type, tailoring data shaping and aggregation to that client's needs.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: The tools, processes, and practices for collecting, integrating, and analyzing business data to support reporting, dashboards, and decision-making.

**Blameless postmortem**: An incident review that focuses on systemic causes and learning rather than individual fault, on the premise that people act reasonably given the information and incentives they had.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: A release strategy that runs two identical production environments ("blue" and "green"), routing traffic to one while the other is updated, enabling near-instant cutover and rollback.

**Bounded context**: In Domain-Driven Design, an explicit boundary within which a particular domain model and its ubiquitous language apply consistently. It prevents concepts from being conflated across different parts of a large system.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: The number of people who would need to be lost (metaphorically "hit by a bus") before a project stalls for lack of essential knowledge. A low bus factor signals concentrated, undocumented expertise and organizational risk.

## C

**Canary release**: A deployment technique that exposes a new version to a small subset of users or traffic first, monitors for problems, and then progressively expands the rollout if metrics stay healthy.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: A principle stating that a distributed data store can guarantee at most two of Consistency, Availability, and Partition tolerance simultaneously; because partitions are unavoidable, designers effectively trade consistency against availability during them.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**: A lightweight approach to visualizing software architecture at four levels of abstraction: System Context, Containers, Components, and Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Continuous Delivery keeps software in a releasable state so it can be deployed at any time with a manual approval; Continuous Deployment automatically releases every change that passes the pipeline.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: The practice of frequently merging developers' changes into a shared mainline, each merge validated by an automated build and test suite to detect integration problems early.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: The combined pipeline of Continuous Integration and Continuous Delivery/Deployment that automates building, testing, and releasing software.

**CMMC (Cybersecurity Maturity Model Certification)**: A US Department of Defense program that certifies the cybersecurity maturity of contractors handling federal contract information and controlled unclassified information.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: The degree to which the elements inside a module belong together and serve a single, well-defined purpose. High cohesion, paired with low coupling, is a hallmark of maintainable design.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)**: The observation that the structure of a system tends to mirror the communication structure of the organization that builds it. The "inverse Conway maneuver" deliberately shapes teams to produce a desired architecture.

**Core Web Vitals**: A set of user-centric web performance metrics defined by Google (such as Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift) that measure loading, interactivity, and visual stability.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: The degree of interdependence between modules or services. Loose coupling limits the ripple effect of change and is a central goal of good architecture.

**CQRS (Command Query Responsibility Segregation)**: A pattern that separates the model used to change state (commands) from the model used to read state (queries), allowing each to be optimized and scaled independently.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: A public catalog of disclosed security vulnerabilities, each assigned a unique identifier so that tools and teams can reference the same flaw unambiguously.

**CWV**: See Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Security testing that probes a running application from the outside, without access to source code, to find vulnerabilities that appear at runtime.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: A decentralized data architecture and operating model that treats data as a product owned by domain teams, supported by self-serve platform infrastructure and federated governance.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: An approach to software design that centers the model on the business domain, using a shared ubiquitous language, bounded contexts, and building blocks such as entities, value objects, and aggregates.

**Design tokens**: Named, platform-agnostic values (colors, spacing, typography, and the like) that encode design decisions so they can be shared consistently across a design system and multiple products.

**DevEx / DevX (Developer Experience)**: The overall quality of a developer's day-to-day interaction with tools, platforms, and processes, encompassing friction, feedback speed, and cognitive load.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: A culture and set of practices that unite software development and operations to shorten delivery cycles, increase deployment frequency, and improve reliability through automation and shared ownership.

**DORA (DevOps Research and Assessment)**: A research program and its four widely used delivery metrics (deployment frequency, lead time for changes, change failure rate, and time to restore service) used to benchmark software delivery performance.

**DPIA (Data Protection Impact Assessment)**: A structured assessment, required under GDPR for high-risk processing, that identifies and mitigates privacy risks before a project proceeds.

**Drift (configuration)**: The gradual divergence of a system's actual state from its declared or intended state, commonly caused by manual changes; Infrastructure as Code and GitOps aim to detect and correct it.

**Drift (model)**: In machine learning, the degradation of model performance over time as the statistical properties of input data (data drift) or the relationship being modeled (concept drift) change.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: The strategy, procedures, and infrastructure for restoring service and data after a major disruptive event, typically governed by RTO and RPO targets.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: A design principle stating that every piece of knowledge should have a single, authoritative representation, reducing duplication and the risk of inconsistent updates.

## E

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: The ability of a system to automatically acquire and release resources in response to changing demand, so capacity tracks load closely.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: A data integration pattern that loads raw data into a target store first and transforms it there, exploiting the scale of modern warehouses and lakehouses.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: The European standard specifying accessibility requirements for ICT products and services, referenced by public-sector procurement across the EU and aligned with WCAG.

**Error budget**: The permissible amount of unreliability allowed by an SLO over a period; when it is exhausted, teams prioritize reliability work over new features. It reconciles the tension between velocity and stability.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: A data integration pattern that extracts data from sources, transforms it into a target shape, and loads it into a destination such as a warehouse.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: European Union regulation that classifies AI systems by risk and imposes obligations accordingly, banning certain uses and heavily regulating high-risk systems.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**: A consistency model in distributed systems in which replicas may temporarily diverge but converge to the same state once updates stop propagating.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: A mechanism to enable or disable functionality at runtime without redeploying, used for gradual rollouts, experimentation, and operational control.

**Feature store**: A centralized system for defining, storing, and serving curated machine-learning features consistently for both training and inference, reducing duplication and training/serving skew.

**[FedRAMP (Federal Risk and Authorization Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: A US government program that standardizes security assessment, authorization, and continuous monitoring for cloud services used by federal agencies.

**FinOps**: A discipline and cultural practice that brings financial accountability to variable cloud spending, giving engineering, finance, and business teams shared ownership of cost and value.

**[FISMA (Federal Information Security Modernization Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: US legislation requiring federal agencies to implement, document, and monitor information security programs, operationalized largely through NIST guidance.

**Four-eyes principle**: A control requiring that a significant action be reviewed or approved by at least two people, reducing the chance of error or malfeasance.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: An automated testing technique that feeds malformed, random, or unexpected inputs to a program to uncover crashes, security flaws, and edge-case defects.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: The European Union regulation governing the processing of personal data, granting individuals rights and imposing obligations on controllers and processors, with significant penalties for non-compliance.

**GitOps**: An operational model that uses Git as the single source of truth for declarative infrastructure and applications, with automation continuously reconciling the live system to the committed state.

**Golden path / paved road**: A well-supported, opinionated default way to build and ship software within an organization, designed to make the secure, compliant, reliable choice the easiest one.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: A query language and runtime for APIs that lets clients request exactly the data they need in a single call, using a strongly typed schema.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: A high-performance, contract-first remote procedure call framework that uses HTTP/2 and, typically, Protocol Buffers for efficient service-to-service communication.

## H

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: A tamper-resistant hardware device that generates, stores, and uses cryptographic keys, providing stronger key protection than software-only approaches.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: US legislation that, among other things, sets requirements for safeguarding protected health information (PHI) and governs its use and disclosure.

**Horizontal scaling**: Increasing capacity by adding more instances or nodes ("scaling out") rather than making a single node more powerful. It underpins most large-scale, resilient architectures.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: The practice of defining and provisioning infrastructure through machine-readable, version-controlled configuration rather than manual processes, enabling repeatability and review.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: The framework of policies and technologies that ensures the right identities have the right access to the right resources at the right times.

**IDP / IdP**: "IDP" commonly denotes an Internal Developer Platform, the self-service tooling layer that abstracts infrastructure for product teams; "IdP" denotes an Identity Provider, a service that authenticates users and issues assertions. Context disambiguates the two.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**: A property whereby performing an operation multiple times has the same effect as performing it once, essential for safe retries in distributed systems and APIs.

**[i18n (Internationalization)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Designing and building software so it can be adapted to different languages, regions, and cultural conventions without engineering changes. The numeronym abbreviates the 18 letters between "i" and "n."

**InnerSource**: The application of open-source development practices (transparency, shared repositories, and cross-team contribution) inside a single organization.

**IaC drift**: See Drift (configuration).

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: An international standard specifying requirements for an Information Security Management System (ISMS), providing a certifiable framework for managing information security risk.

**ISO/IEC 42001**: An international standard specifying requirements for an AI Management System, giving organizations a certifiable framework for governing the development and use of AI responsibly.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: A compact, signed (and optionally encrypted) token format used to convey claims between parties, commonly for authentication and authorization in web and API systems.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: A lean workflow method that visualizes work on a board, limits work in progress, and manages flow to improve throughput and predictability.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: A design principle favoring the simplest solution that meets the need, on the grounds that unnecessary complexity increases cost and risk.

**KMS (Key Management Service)**: A system for creating, storing, rotating, and controlling access to cryptographic keys, often backed by hardware security modules.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: A quantifiable measure used to track progress toward a specific business or operational objective.

## L

**Lakehouse**: A data architecture that combines the low-cost, flexible storage of a data lake with the management, transactions, and performance features of a data warehouse.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)**: The elapsed time from a change being requested (or committed) to it being delivered into production; a core DORA delivery metric.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: A security principle granting each user, process, or system only the minimum access required to perform its function, limiting the damage from compromise or error.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: A machine-learning model trained on very large text corpora to predict and generate language, capable of tasks such as summarization, translation, and code generation.

**[l10n (Localization)](https://en.wikipedia.org/wiki/Language_localisation)**: Adapting internationalized software to a specific locale, including translation, formatting, and cultural conventions. The numeronym abbreviates the 10 letters between "l" and "n."

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: The discipline and tooling for creating and maintaining a single, authoritative, consistent view of core business entities (such as customers or products) across systems.

**Mean Time to Recovery (MTTR)**: The average time taken to restore service after a failure; a common reliability and incident-management metric.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: A practice in which a whole team works together on the same task at the same computer, rotating who types, to share knowledge and make decisions collectively.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: The set of practices that reliably and efficiently deploy, monitor, and maintain machine-learning models in production, extending DevOps principles to the ML lifecycle.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: A single version-control repository holding the code for many projects or the whole organization, enabling shared tooling and atomic cross-project changes at the cost of specialized scaling tooling.

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**: A technique that deliberately introduces small faults ("mutants") into code to check whether the test suite detects them, measuring the suite's real effectiveness.

## N

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: A US federal agency whose Special Publications and frameworks are widely referenced standards for cybersecurity, privacy, and AI.

**NIST AI RMF (AI Risk Management Framework)**: A voluntary NIST framework for identifying, assessing, and managing risks associated with AI systems across their lifecycle, organized around the functions Govern, Map, Measure, and Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: A NIST catalog of security and privacy controls for federal information systems, widely used as a baseline well beyond government.

**NIST SP 800-171**: A NIST publication specifying requirements for protecting controlled unclassified information (CUI) in non-federal systems, central to defense-contractor compliance.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: A requirement describing how a system should behave (its qualities such as performance, security, reliability, or usability) rather than what functions it performs.

## O

**Observability**: The degree to which a system's internal state can be inferred from its external outputs, typically achieved through telemetry: metrics, logs, and traces.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: A goal-setting framework pairing a qualitative objective with a few measurable key results to align and focus an organization.

**OpenTelemetry (OTel)**: A vendor-neutral, open standard and toolset for generating, collecting, and exporting telemetry data (traces, metrics, and logs) from software.

**OPA (Open Policy Agent)**: An open-source, general-purpose policy engine that evaluates policies (written in the Rego language) to enforce authorization and configuration rules across the stack, enabling policy as code.

**OSPO (Open Source Program Office)**: An organizational function that coordinates open-source strategy, governance, compliance, and community engagement, managing both consumption and contribution.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: A nonprofit community that produces widely used, freely available application-security resources, including the OWASP Top Ten and the ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: An extension of the CAP theorem stating that if there is a Partition, a system trades Availability against Consistency, Else (in normal operation) it trades Latency against Consistency.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: A security standard maintained by the payment card industry that specifies requirements for organizations that store, process, or transmit cardholder data.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Information that can identify a specific individual, either alone or combined with other data; its handling is governed by privacy laws and internal policy.

**Platform engineering**: The discipline of building and operating internal self-service platforms and golden paths that reduce cognitive load and accelerate product teams.

**POUR**: The four guiding principles of the Web Content Accessibility Guidelines: content must be Perceivable, Operable, Understandable, and Robust.

**Property-based testing**: A testing technique that checks that stated properties hold across many automatically generated inputs, rather than relying only on hand-picked examples.

**Pull request (PR) / merge request (MR)**: A proposed set of changes submitted for review and discussion before being merged into a shared branch, the primary unit of code review in most workflows.

## Q

**Quality gate**: An automated checkpoint in a pipeline that must be passed (for example, meeting coverage, security, or performance thresholds) before a change can progress.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: In distributed systems, the minimum number of nodes that must agree for an operation (such as a read or write) to be considered successful, used to maintain consistency despite failures.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: A responsibility-assignment model that labels each participant in a task or decision as Responsible, Accountable, Consulted, or Informed.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: A technique that grounds a language model's output by first retrieving relevant documents or data and supplying them as context, improving accuracy and reducing hallucination.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: An authorization model that assigns permissions to roles and roles to users, simplifying administration by managing access at the role level.

**Rego**: The declarative policy language used by Open Policy Agent to express rules for authorization and configuration decisions.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: An architectural style for networked applications that uses stateless operations over HTTP on addressable resources, valued for simplicity and broad tooling.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: A written proposal circulated for feedback before a significant technical decision or change, fostering transparency and shared ownership. (The term also names the Internet-standards document series.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: A measure of the value gained from an investment relative to its cost, used to justify and prioritize engineering and technology decisions.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: Software "robots" that automate repetitive, rule-based tasks by interacting with existing user interfaces and systems as a person would.

**RPO (Recovery Point Objective)**: The maximum acceptable amount of data loss measured in time (for example, "up to five minutes"), defining how frequently data must be protected.

**RTO (Recovery Time Objective)**: The maximum acceptable duration to restore a service after a disruption, guiding disaster-recovery design and investment.

## S

**Saga**: A pattern for managing data consistency across services in a distributed transaction by sequencing local transactions and issuing compensating actions when a step fails.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: A framework for applying agile and lean practices across large enterprises, coordinating many teams; valued for structure and criticized for potential heaviness.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Security testing that analyzes source code, bytecode, or binaries without executing them to find vulnerabilities early in development.

**SBOM (Software Bill of Materials)**: A formal, machine-readable inventory of the components and dependencies in a piece of software, used to manage supply-chain and vulnerability risk.

**SCA (Software Composition Analysis)**: Tooling that identifies open-source and third-party components in a codebase and flags known vulnerabilities and license risks.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: An agile framework that organizes work into fixed-length iterations (sprints) with defined roles, events, and artifacts to deliver increments of value.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: A US law requiring federal agencies to make their electronic and information technology accessible to people with disabilities, in practice aligned with WCAG.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: A system that aggregates and correlates security logs and events across an environment to enable detection, alerting, and investigation.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: A formal commitment between a service provider and its customers specifying expected service levels and the consequences of missing them.

**SLI (Service Level Indicator)**: A quantitative measure of some aspect of service quality, such as request latency or error rate, that feeds into SLOs.

**SLO (Service Level Objective)**: A target value or range for an SLI that defines the desired level of reliability, forming the basis of error budgets.

**SLSA (Supply-chain Levels for Software Artifacts)**: A framework of graduated security requirements for improving the integrity and provenance of software artifacts through the build and release process.

**SOAR (Security Orchestration, Automation, and Response)**: Tools and practices that automate and coordinate security operations, such as triage and response playbooks, to improve speed and consistency.

**SOC 2 (System and Organization Controls 2)**: An auditing framework and report, based on the AICPA Trust Services Criteria, that assesses a service organization's controls for security, availability, processing integrity, confidentiality, and privacy.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Five object-oriented design principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion) that promote maintainable, flexible code.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: US legislation establishing requirements for financial reporting and internal controls in public companies, with implications for the IT systems that support financial data.

**SPACE**: A framework for measuring developer productivity across five dimensions: Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow, cautioning against single-metric measures.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: A discipline that applies software-engineering approaches to operations, using SLOs, error budgets, and automation to run reliable systems at scale.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: A threat-modeling taxonomy categorizing threats as Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, and Elevation of privilege.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: The full lifetime cost of a system or decision, including acquisition, operation, maintenance, and eventual retirement, not just the initial price.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: A practice of writing a failing automated test before the code that makes it pass, then refactoring, in short repeated cycles to drive design and ensure coverage.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)**: The implied future cost of choosing an expedient solution now over a better one that would take longer, which must be managed deliberately rather than accrued unconsciously.

**[Threat modeling](https://en.wikipedia.org/wiki/Threat_model)**: A structured practice of identifying, enumerating, and prioritizing potential threats to a system so that defenses can be designed in early.

**Toil**: In SRE, manual, repetitive, automatable operational work that scales linearly with a service and provides no lasting value; reducing it frees capacity for engineering.

**Trunk-based development**: A source-control practice in which developers integrate small changes frequently into a single shared branch, minimizing long-lived branches and merge pain.

## U

**Ubiquitous language**: In Domain-Driven Design, a shared, precise vocabulary used consistently by developers and domain experts, and reflected directly in the code and models.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Testing performed by end users or their representatives to confirm that a system meets business needs before it is accepted for release.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: User Experience is the overall quality of a person's interaction with a product; User Interface is the specific visual and interactive surface through which that interaction occurs.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**: In Domain-Driven Design, an immutable object defined entirely by its attributes rather than a distinct identity, such as a money amount or a date range.

**Vertical scaling**: Increasing capacity by making a single node more powerful ("scaling up"), which is simple but ultimately bounded by the largest available machine.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: A tool, such as Git, that records changes to files over time so that history can be reviewed, branches can be maintained, and work can be coordinated.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: A W3C set of internationally recognized guidelines, organized around the POUR principles and conformance levels A, AA, and AAA, for making web content accessible.

**Wardley map**: A visual strategy technique that positions capabilities by their value to users and their evolutionary maturity, to inform build/buy and investment decisions.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: A web vulnerability in which an attacker injects malicious scripts that execute in other users' browsers, potentially stealing data or hijacking sessions.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: A principle advising against building functionality on speculation, on the grounds that anticipated needs often fail to materialize and add cost and complexity.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: A security model that assumes no implicit trust based on network location and continuously verifies every access request against identity, device, and context, following the maxim "never trust, always verify."
