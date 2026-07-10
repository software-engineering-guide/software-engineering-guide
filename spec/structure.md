# Structure (canonical chapter manifest)

This file is the structural source of truth for the guidebook. It lists every
part and chapter with its decimal number, title, and file. The test suite
(`tests/validate.py`) checks that the files on disk match this manifest exactly,
and the navigation generator (`tools/gen_nav.py`) derives the table of contents,
index, and specification outline from the same files. Change the structure here
and in the chapter files together; the tests will catch any drift.

Totals: **12 parts**, **133 chapters** (each part opens with an N.0 introduction).

## Part 1: People

| Chapter | Title | File |
| --- | --- | --- |
| 1.0 | Introduction to Part 1: People | [`01-00-people.md`](../docs/chapters/01-00-people.md) |
| 1.1 | Software engineering values | [`01-01-software-engineering-values.md`](../docs/chapters/01-01-software-engineering-values.md) |
| 1.2 | Team topologies and organizational design | [`01-02-team-topologies.md`](../docs/chapters/01-02-team-topologies.md) |
| 1.3 | Roles, career ladders, and growth | [`01-03-roles-career-ladders-growth.md`](../docs/chapters/01-03-roles-career-ladders-growth.md) |
| 1.4 | Ways of working | [`01-04-ways-of-working.md`](../docs/chapters/01-04-ways-of-working.md) |
| 1.5 | Decision-making and governance | [`01-05-decision-making-and-governance.md`](../docs/chapters/01-05-decision-making-and-governance.md) |
| 1.6 | Decision records | [`01-06-decision-records.md`](../docs/chapters/01-06-decision-records.md) |
| 1.7 | Engineering standards and exceptions | [`01-07-engineering-standards-and-exceptions.md`](../docs/chapters/01-07-engineering-standards-and-exceptions.md) |
| 1.8 | Hiring, interviewing, and onboarding | [`01-08-hiring-interviewing-onboarding.md`](../docs/chapters/01-08-hiring-interviewing-onboarding.md) |
| 1.9 | Distributed and remote work | [`01-09-distributed-and-remote-work.md`](../docs/chapters/01-09-distributed-and-remote-work.md) |
| 1.10 | Engineering effectiveness and developer productivity | [`01-10-engineering-effectiveness-and-developer-productivity.md`](../docs/chapters/01-10-engineering-effectiveness-and-developer-productivity.md) |
| 1.11 | Engineering management | [`01-11-engineering-management.md`](../docs/chapters/01-11-engineering-management.md) |
| 1.12 | Diversity, equity, inclusion, and belonging | [`01-12-diversity-equity-inclusion-belonging.md`](../docs/chapters/01-12-diversity-equity-inclusion-belonging.md) |

## Part 2: Software Programming

| Chapter | Title | File |
| --- | --- | --- |
| 2.0 | Introduction to Part 2: Software Programming | [`02-00-software-programming.md`](../docs/chapters/02-00-software-programming.md) |
| 2.1 | Coding standards and style | [`02-01-coding-standards-and-style.md`](../docs/chapters/02-01-coding-standards-and-style.md) |
| 2.2 | Software design principles | [`02-02-software-design-principles.md`](../docs/chapters/02-02-software-design-principles.md) |
| 2.3 | APIs and interface design | [`02-03-apis-and-interface-design.md`](../docs/chapters/02-03-apis-and-interface-design.md) |
| 2.4 | Testing strategy | [`02-04-testing-strategy.md`](../docs/chapters/02-04-testing-strategy.md) |
| 2.5 | Code review and collaboration | [`02-05-code-review-and-collaboration.md`](../docs/chapters/02-05-code-review-and-collaboration.md) |
| 2.6 | Version control and source management | [`02-06-version-control-and-source-management.md`](../docs/chapters/02-06-version-control-and-source-management.md) |
| 2.7 | Documentation | [`02-07-documentation.md`](../docs/chapters/02-07-documentation.md) |
| 2.8 | Software requirements | [`02-08-software-requirements.md`](../docs/chapters/02-08-software-requirements.md) |
| 2.9 | Software construction | [`02-09-software-construction.md`](../docs/chapters/02-09-software-construction.md) |
| 2.10 | Software configuration management | [`02-10-software-configuration-management.md`](../docs/chapters/02-10-software-configuration-management.md) |
| 2.11 | Software quality | [`02-11-software-quality.md`](../docs/chapters/02-11-software-quality.md) |
| 2.12 | Software models and methods | [`02-12-software-models-and-methods.md`](../docs/chapters/02-12-software-models-and-methods.md) |
| 2.13 | Computing, mathematical, and engineering foundations | [`02-13-computing-mathematical-engineering-foundations.md`](../docs/chapters/02-13-computing-mathematical-engineering-foundations.md) |
| 2.14 | Project and repository structure | [`02-14-project-and-repository-structure.md`](../docs/chapters/02-14-project-and-repository-structure.md) |
| 2.15 | Debugging and troubleshooting | [`02-15-debugging-and-troubleshooting.md`](../docs/chapters/02-15-debugging-and-troubleshooting.md) |
| 2.16 | Performance engineering | [`02-16-performance-engineering.md`](../docs/chapters/02-16-performance-engineering.md) |
| 2.17 | Concurrency and parallelism | [`02-17-concurrency-and-parallelism.md`](../docs/chapters/02-17-concurrency-and-parallelism.md) |
| 2.18 | Dependency and supply-chain management | [`02-18-dependency-and-supply-chain-management.md`](../docs/chapters/02-18-dependency-and-supply-chain-management.md) |
| 2.19 | Refactoring and technical debt | [`02-19-refactoring-and-technical-debt.md`](../docs/chapters/02-19-refactoring-and-technical-debt.md) |
| 2.20 | Error handling and resilience patterns | [`02-20-error-handling-and-resilience-patterns.md`](../docs/chapters/02-20-error-handling-and-resilience-patterns.md) |

## Part 3: Systems

| Chapter | Title | File |
| --- | --- | --- |
| 3.0 | Introduction to Part 3: Systems | [`03-00-systems.md`](../docs/chapters/03-00-systems.md) |
| 3.1 | Architecture fundamentals | [`03-01-architecture-fundamentals.md`](../docs/chapters/03-01-architecture-fundamentals.md) |
| 3.2 | Architectural styles and patterns | [`03-02-architectural-styles-and-patterns.md`](../docs/chapters/03-02-architectural-styles-and-patterns.md) |
| 3.3 | Distributed systems | [`03-03-distributed-systems.md`](../docs/chapters/03-03-distributed-systems.md) |
| 3.4 | Data architecture and storage | [`03-04-data-architecture-and-storage.md`](../docs/chapters/03-04-data-architecture-and-storage.md) |
| 3.5 | Scalability, performance, and resilience | [`03-05-scalability-performance-resilience.md`](../docs/chapters/03-05-scalability-performance-resilience.md) |
| 3.6 | Legacy modernization | [`03-06-legacy-modernization.md`](../docs/chapters/03-06-legacy-modernization.md) |
| 3.7 | Software maintenance | [`03-07-software-maintenance.md`](../docs/chapters/03-07-software-maintenance.md) |
| 3.8 | Interoperability and open standards | [`03-08-interoperability-and-open-standards.md`](../docs/chapters/03-08-interoperability-and-open-standards.md) |
| 3.9 | Systems engineering | [`03-09-systems-engineering.md`](../docs/chapters/03-09-systems-engineering.md) |
| 3.10 | Embedded and real-time systems | [`03-10-embedded-and-real-time-systems.md`](../docs/chapters/03-10-embedded-and-real-time-systems.md) |
| 3.11 | Cloud architecture | [`03-11-cloud-architecture.md`](../docs/chapters/03-11-cloud-architecture.md) |
| 3.12 | Event-driven architecture and messaging | [`03-12-event-driven-architecture-and-messaging.md`](../docs/chapters/03-12-event-driven-architecture-and-messaging.md) |
| 3.13 | Networking and connectivity | [`03-13-networking-and-connectivity.md`](../docs/chapters/03-13-networking-and-connectivity.md) |
| 3.14 | Multi-tenancy and SaaS architecture | [`03-14-multi-tenancy-and-saas-architecture.md`](../docs/chapters/03-14-multi-tenancy-and-saas-architecture.md) |

## Part 4: Security

| Chapter | Title | File |
| --- | --- | --- |
| 4.0 | Introduction to Part 4: Security | [`04-00-security.md`](../docs/chapters/04-00-security.md) |
| 4.1 | Security foundations and culture | [`04-01-security-foundations-and-culture.md`](../docs/chapters/04-01-security-foundations-and-culture.md) |
| 4.2 | Application security | [`04-02-application-security.md`](../docs/chapters/04-02-application-security.md) |
| 4.3 | Infrastructure and cloud security | [`04-03-infrastructure-and-cloud-security.md`](../docs/chapters/04-03-infrastructure-and-cloud-security.md) |
| 4.4 | Security operations | [`04-04-security-operations.md`](../docs/chapters/04-04-security-operations.md) |
| 4.5 | Privacy and data protection | [`04-05-privacy-and-data-protection.md`](../docs/chapters/04-05-privacy-and-data-protection.md) |
| 4.6 | Compliance and governance | [`04-06-compliance-and-governance.md`](../docs/chapters/04-06-compliance-and-governance.md) |
| 4.7 | Identity and access management | [`04-07-identity-and-access-management.md`](../docs/chapters/04-07-identity-and-access-management.md) |
| 4.8 | Cryptography and key management | [`04-08-cryptography-and-key-management.md`](../docs/chapters/04-08-cryptography-and-key-management.md) |

## Part 5: UI/UX Design

| Chapter | Title | File |
| --- | --- | --- |
| 5.0 | Introduction to Part 5: UI/UX Design | [`05-00-ui-ux-design.md`](../docs/chapters/05-00-ui-ux-design.md) |
| 5.1 | UX foundations | [`05-01-ux-foundations.md`](../docs/chapters/05-01-ux-foundations.md) |
| 5.2 | UI design and design systems | [`05-02-ui-design-and-design-systems.md`](../docs/chapters/05-02-ui-design-and-design-systems.md) |
| 5.3 | Accessibility | [`05-03-accessibility.md`](../docs/chapters/05-03-accessibility.md) |
| 5.4 | Content and communication design | [`05-04-content-and-communication-design.md`](../docs/chapters/05-04-content-and-communication-design.md) |
| 5.5 | Internationalization and localization | [`05-05-internationalization-and-localization.md`](../docs/chapters/05-05-internationalization-and-localization.md) |
| 5.6 | Frontend engineering | [`05-06-frontend-engineering.md`](../docs/chapters/05-06-frontend-engineering.md) |
| 5.7 | Mobile application development | [`05-07-mobile-application-development.md`](../docs/chapters/05-07-mobile-application-development.md) |
| 5.8 | Design research and usability testing | [`05-08-design-research-and-usability-testing.md`](../docs/chapters/05-08-design-research-and-usability-testing.md) |
| 5.9 | Service design | [`05-09-service-design.md`](../docs/chapters/05-09-service-design.md) |

## Part 6: Artificial Intelligence

| Chapter | Title | File |
| --- | --- | --- |
| 6.0 | Introduction to Part 6: Artificial Intelligence | [`06-00-artificial-intelligence.md`](../docs/chapters/06-00-artificial-intelligence.md) |
| 6.1 | AI strategy and readiness | [`06-01-ai-strategy-and-readiness.md`](../docs/chapters/06-01-ai-strategy-and-readiness.md) |
| 6.2 | Machine learning engineering (MLOps) | [`06-02-mlops.md`](../docs/chapters/06-02-mlops.md) |
| 6.3 | Generative AI and LLM applications | [`06-03-generative-ai-and-llm-applications.md`](../docs/chapters/06-03-generative-ai-and-llm-applications.md) |
| 6.4 | AI-assisted software development | [`06-04-ai-assisted-software-development.md`](../docs/chapters/06-04-ai-assisted-software-development.md) |
| 6.5 | Responsible and trustworthy AI | [`06-05-responsible-and-trustworthy-ai.md`](../docs/chapters/06-05-responsible-and-trustworthy-ai.md) |
| 6.6 | AI infrastructure and operations | [`06-06-ai-infrastructure-and-operations.md`](../docs/chapters/06-06-ai-infrastructure-and-operations.md) |
| 6.7 | AI agents and agentic systems | [`06-07-ai-agents-and-agentic-systems.md`](../docs/chapters/06-07-ai-agents-and-agentic-systems.md) |
| 6.8 | AI evaluation and testing | [`06-08-ai-evaluation-and-testing.md`](../docs/chapters/06-08-ai-evaluation-and-testing.md) |

## Part 7: Data, Analytics, and Insight

| Chapter | Title | File |
| --- | --- | --- |
| 7.0 | Introduction to Part 7: Data, Analytics, and Insight | [`07-00-data-and-analytics.md`](../docs/chapters/07-00-data-and-analytics.md) |
| 7.1 | Data strategy and governance | [`07-01-data-strategy-and-governance.md`](../docs/chapters/07-01-data-strategy-and-governance.md) |
| 7.2 | Data engineering | [`07-02-data-engineering.md`](../docs/chapters/07-02-data-engineering.md) |
| 7.3 | Analytics and business intelligence | [`07-03-analytics-and-business-intelligence.md`](../docs/chapters/07-03-analytics-and-business-intelligence.md) |
| 7.4 | Product analytics and experimentation | [`07-04-product-analytics-and-experimentation.md`](../docs/chapters/07-04-product-analytics-and-experimentation.md) |
| 7.5 | Decision science and data-informed culture | [`07-05-decision-science-and-data-culture.md`](../docs/chapters/07-05-decision-science-and-data-culture.md) |
| 7.6 | Real-time and streaming data | [`07-06-real-time-and-streaming-data.md`](../docs/chapters/07-06-real-time-and-streaming-data.md) |
| 7.7 | Data modeling and the semantic layer | [`07-07-data-modeling-and-semantic-layer.md`](../docs/chapters/07-07-data-modeling-and-semantic-layer.md) |
| 7.8 | Data quality and observability | [`07-08-data-quality-and-observability.md`](../docs/chapters/07-08-data-quality-and-observability.md) |

## Part 8: Automation

| Chapter | Title | File |
| --- | --- | --- |
| 8.0 | Introduction to Part 8: Automation | [`08-00-automation.md`](../docs/chapters/08-00-automation.md) |
| 8.1 | CI/CD and delivery | [`08-01-ci-cd-and-delivery.md`](../docs/chapters/08-01-ci-cd-and-delivery.md) |
| 8.2 | Infrastructure as code and configuration | [`08-02-infrastructure-as-code-and-configuration.md`](../docs/chapters/08-02-infrastructure-as-code-and-configuration.md) |
| 8.3 | Containers, orchestration, and cloud-native | [`08-03-containers-orchestration-cloud-native.md`](../docs/chapters/08-03-containers-orchestration-cloud-native.md) |
| 8.4 | Platform engineering and developer experience | [`08-04-platform-engineering-and-devex.md`](../docs/chapters/08-04-platform-engineering-and-devex.md) |
| 8.5 | Test and process automation | [`08-05-test-and-process-automation.md`](../docs/chapters/08-05-test-and-process-automation.md) |
| 8.6 | Release management and progressive delivery | [`08-06-release-management-and-progressive-delivery.md`](../docs/chapters/08-06-release-management-and-progressive-delivery.md) |

## Part 9: Operations, Reliability, and Observability

| Chapter | Title | File |
| --- | --- | --- |
| 9.0 | Introduction to Part 9: Operations, Reliability, and Observability | [`09-00-operations-and-reliability.md`](../docs/chapters/09-00-operations-and-reliability.md) |
| 9.1 | Site reliability engineering | [`09-01-site-reliability-engineering.md`](../docs/chapters/09-01-site-reliability-engineering.md) |
| 9.2 | Observability and telemetry | [`09-02-observability-and-telemetry.md`](../docs/chapters/09-02-observability-and-telemetry.md) |
| 9.3 | Incident management | [`09-03-incident-management.md`](../docs/chapters/09-03-incident-management.md) |
| 9.4 | Cost, sustainability, and green software | [`09-04-cost-sustainability-green-software.md`](../docs/chapters/09-04-cost-sustainability-green-software.md) |
| 9.5 | Disaster recovery and business continuity | [`09-05-disaster-recovery-and-business-continuity.md`](../docs/chapters/09-05-disaster-recovery-and-business-continuity.md) |
| 9.6 | Chaos engineering and resilience testing | [`09-06-chaos-engineering-and-resilience-testing.md`](../docs/chapters/09-06-chaos-engineering-and-resilience-testing.md) |

## Part 10: Project/Product/Program Management

| Chapter | Title | File |
| --- | --- | --- |
| 10.0 | Introduction to Part 10: Project/Product/Program Management | [`10-00-project-product-program-management.md`](../docs/chapters/10-00-project-product-program-management.md) |
| 10.1 | Portfolio and program management | [`10-01-portfolio-and-program-management.md`](../docs/chapters/10-01-portfolio-and-program-management.md) |
| 10.2 | Risk, audit, and assurance | [`10-02-risk-audit-and-assurance.md`](../docs/chapters/10-02-risk-audit-and-assurance.md) |
| 10.3 | Procurement, open source, and licensing | [`10-03-procurement-open-source-and-licensing.md`](../docs/chapters/10-03-procurement-open-source-and-licensing.md) |
| 10.4 | Sustaining large and long-lived systems | [`10-04-sustaining-large-and-long-lived-systems.md`](../docs/chapters/10-04-sustaining-large-and-long-lived-systems.md) |
| 10.5 | Ethics, accountability, and public interest | [`10-05-ethics-accountability-public-interest.md`](../docs/chapters/10-05-ethics-accountability-public-interest.md) |
| 10.6 | Project management | [`10-06-project-management.md`](../docs/chapters/10-06-project-management.md) |
| 10.7 | Agile | [`10-07-agile.md`](../docs/chapters/10-07-agile.md) |
| 10.8 | Maturity models | [`10-08-maturity-models.md`](../docs/chapters/10-08-maturity-models.md) |
| 10.9 | Innovation partnership | [`10-09-innovation-partnership.md`](../docs/chapters/10-09-innovation-partnership.md) |
| 10.10 | Software engineering economics | [`10-10-software-engineering-economics.md`](../docs/chapters/10-10-software-engineering-economics.md) |
| 10.11 | Digital sovereignty | [`10-11-digital-sovereignty.md`](../docs/chapters/10-11-digital-sovereignty.md) |
| 10.12 | Open source vs closed source | [`10-12-open-source-vs-closed-source.md`](../docs/chapters/10-12-open-source-vs-closed-source.md) |
| 10.13 | Interorganization collaboration | [`10-13-interorganization-collaboration.md`](../docs/chapters/10-13-interorganization-collaboration.md) |
| 10.14 | Product management and discovery | [`10-14-product-management-and-discovery.md`](../docs/chapters/10-14-product-management-and-discovery.md) |
| 10.15 | Estimation and forecasting | [`10-15-estimation-and-forecasting.md`](../docs/chapters/10-15-estimation-and-forecasting.md) |
| 10.16 | Stakeholder management and communication | [`10-16-stakeholder-management-and-communication.md`](../docs/chapters/10-16-stakeholder-management-and-communication.md) |
| 10.17 | Organizational change management | [`10-17-organizational-change-management.md`](../docs/chapters/10-17-organizational-change-management.md) |
| 10.18 | Open source program office (OSPO) and upstream contribution | [`10-18-open-source-program-office.md`](../docs/chapters/10-18-open-source-program-office.md) |

## Part 11: Flow: Discovery and Delivery Pipelines

| Chapter | Title | File |
| --- | --- | --- |
| 11.0 | Introduction to Part 11: Flow: Discovery and Delivery Pipelines | [`11-00-flow-discovery-and-delivery.md`](../docs/chapters/11-00-flow-discovery-and-delivery.md) |
| 11.1 | The discovery pipeline | [`11-01-discovery-pipeline.md`](../docs/chapters/11-01-discovery-pipeline.md) |
| 11.2 | The delivery pipeline | [`11-02-delivery-pipeline.md`](../docs/chapters/11-02-delivery-pipeline.md) |
| 11.3 | Queueing theory | [`11-03-queueing-theory.md`](../docs/chapters/11-03-queueing-theory.md) |
| 11.4 | Objectives and key results (OKRs) | [`11-04-objectives-and-key-results.md`](../docs/chapters/11-04-objectives-and-key-results.md) |
| 11.5 | Key performance indicators (KPIs) | [`11-05-key-performance-indicators.md`](../docs/chapters/11-05-key-performance-indicators.md) |

## Part 12: Appendices

| Chapter | Title | File |
| --- | --- | --- |
| 12.0 | Appendices | [`12-00-appendices.md`](../docs/chapters/12-00-appendices.md) |
| 12.1 | Glossary | [`12-01-glossary.md`](../docs/chapters/12-01-glossary.md) |
| 12.2 | Checklists | [`12-02-checklists.md`](../docs/chapters/12-02-checklists.md) |
| 12.3 | Templates | [`12-03-templates.md`](../docs/chapters/12-03-templates.md) |
| 12.4 | Maturity self-assessment | [`12-04-maturity-self-assessment.md`](../docs/chapters/12-04-maturity-self-assessment.md) |
| 12.5 | References | [`12-05-references.md`](../docs/chapters/12-05-references.md) |
| 12.6 | Adoption roadmap | [`12-06-adoption-roadmap.md`](../docs/chapters/12-06-adoption-roadmap.md) |
| 12.7 | Index | [`12-07-index.md`](../docs/chapters/12-07-index.md) |
