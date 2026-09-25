# Structure (canonical chapter manifest)

This file is the structural source of truth for the guidebook. It lists every
part and chapter with its decimal number, title, and file. The test suite
(`tests/validate.py`) checks that the files on disk match this manifest exactly,
and the navigation generator (`tools/gen_nav.py`) derives the table of contents,
index, and specification outline from the same files. Change the structure here
and in the chapter files together; the tests will catch any drift.

Totals: **12 parts**, **147 chapters** (each part opens with an N.0 introduction).

## Part 1: People

| Chapter | Title | File |
| --- | --- | --- |
| 1.0 | Introduction to Part 1: People | [`01-00-people/index.md`](../locales/en-us/chapters/01-00-people/index.md) |
| 1.1 | Software engineering values | [`01-01-software-engineering-values/index.md`](../locales/en-us/chapters/01-01-software-engineering-values/index.md) |
| 1.2 | Team topologies and organizational design | [`01-02-team-topologies/index.md`](../locales/en-us/chapters/01-02-team-topologies/index.md) |
| 1.3 | Roles, career ladders, and growth | [`01-03-roles-career-ladders-growth/index.md`](../locales/en-us/chapters/01-03-roles-career-ladders-growth/index.md) |
| 1.4 | Ways of working | [`01-04-ways-of-working/index.md`](../locales/en-us/chapters/01-04-ways-of-working/index.md) |
| 1.5 | Decision-making and governance | [`01-05-decision-making-and-governance/index.md`](../locales/en-us/chapters/01-05-decision-making-and-governance/index.md) |
| 1.6 | Decision records | [`01-06-decision-records/index.md`](../locales/en-us/chapters/01-06-decision-records/index.md) |
| 1.7 | Engineering standards and exceptions | [`01-07-engineering-standards-and-exceptions/index.md`](../locales/en-us/chapters/01-07-engineering-standards-and-exceptions/index.md) |
| 1.8 | Hiring, interviewing, and onboarding | [`01-08-hiring-interviewing-onboarding/index.md`](../locales/en-us/chapters/01-08-hiring-interviewing-onboarding/index.md) |
| 1.9 | Distributed and remote work | [`01-09-distributed-and-remote-work/index.md`](../locales/en-us/chapters/01-09-distributed-and-remote-work/index.md) |
| 1.10 | Engineering effectiveness and developer productivity | [`01-10-engineering-effectiveness-and-developer-productivity/index.md`](../locales/en-us/chapters/01-10-engineering-effectiveness-and-developer-productivity/index.md) |
| 1.11 | Engineering management | [`01-11-engineering-management/index.md`](../locales/en-us/chapters/01-11-engineering-management/index.md) |
| 1.12 | Diversity, equity, inclusion, and belonging | [`01-12-diversity-equity-inclusion-belonging/index.md`](../locales/en-us/chapters/01-12-diversity-equity-inclusion-belonging/index.md) |
| 1.13 | Mentoring, coaching, and knowledge sharing | [`01-13-mentoring-coaching-knowledge-sharing/index.md`](../locales/en-us/chapters/01-13-mentoring-coaching-knowledge-sharing/index.md) |

## Part 2: Software Programming

| Chapter | Title | File |
| --- | --- | --- |
| 2.0 | Introduction to Part 2: Software Programming | [`02-00-software-programming/index.md`](../locales/en-us/chapters/02-00-software-programming/index.md) |
| 2.1 | Coding standards and style | [`02-01-coding-standards-and-style/index.md`](../locales/en-us/chapters/02-01-coding-standards-and-style/index.md) |
| 2.2 | Software design principles | [`02-02-software-design-principles/index.md`](../locales/en-us/chapters/02-02-software-design-principles/index.md) |
| 2.3 | APIs and interface design | [`02-03-apis-and-interface-design/index.md`](../locales/en-us/chapters/02-03-apis-and-interface-design/index.md) |
| 2.4 | Testing strategy | [`02-04-testing-strategy/index.md`](../locales/en-us/chapters/02-04-testing-strategy/index.md) |
| 2.5 | Code review and collaboration | [`02-05-code-review-and-collaboration/index.md`](../locales/en-us/chapters/02-05-code-review-and-collaboration/index.md) |
| 2.6 | Version control and source management | [`02-06-version-control-and-source-management/index.md`](../locales/en-us/chapters/02-06-version-control-and-source-management/index.md) |
| 2.7 | Documentation | [`02-07-documentation/index.md`](../locales/en-us/chapters/02-07-documentation/index.md) |
| 2.8 | Software requirements | [`02-08-software-requirements/index.md`](../locales/en-us/chapters/02-08-software-requirements/index.md) |
| 2.9 | Software construction | [`02-09-software-construction/index.md`](../locales/en-us/chapters/02-09-software-construction/index.md) |
| 2.10 | Software configuration management | [`02-10-software-configuration-management/index.md`](../locales/en-us/chapters/02-10-software-configuration-management/index.md) |
| 2.11 | Software quality | [`02-11-software-quality/index.md`](../locales/en-us/chapters/02-11-software-quality/index.md) |
| 2.12 | Software models and methods | [`02-12-software-models-and-methods/index.md`](../locales/en-us/chapters/02-12-software-models-and-methods/index.md) |
| 2.13 | Computing, mathematical, and engineering foundations | [`02-13-computing-mathematical-engineering-foundations/index.md`](../locales/en-us/chapters/02-13-computing-mathematical-engineering-foundations/index.md) |
| 2.14 | Project and repository structure | [`02-14-project-and-repository-structure/index.md`](../locales/en-us/chapters/02-14-project-and-repository-structure/index.md) |
| 2.15 | Debugging and troubleshooting | [`02-15-debugging-and-troubleshooting/index.md`](../locales/en-us/chapters/02-15-debugging-and-troubleshooting/index.md) |
| 2.16 | Performance engineering | [`02-16-performance-engineering/index.md`](../locales/en-us/chapters/02-16-performance-engineering/index.md) |
| 2.17 | Concurrency and parallelism | [`02-17-concurrency-and-parallelism/index.md`](../locales/en-us/chapters/02-17-concurrency-and-parallelism/index.md) |
| 2.18 | Dependency and supply-chain management | [`02-18-dependency-and-supply-chain-management/index.md`](../locales/en-us/chapters/02-18-dependency-and-supply-chain-management/index.md) |
| 2.19 | Refactoring and technical debt | [`02-19-refactoring-and-technical-debt/index.md`](../locales/en-us/chapters/02-19-refactoring-and-technical-debt/index.md) |
| 2.20 | Error handling and resilience patterns | [`02-20-error-handling-and-resilience-patterns/index.md`](../locales/en-us/chapters/02-20-error-handling-and-resilience-patterns/index.md) |
| 2.21 | Type systems and static analysis | [`02-21-type-systems-and-static-analysis/index.md`](../locales/en-us/chapters/02-21-type-systems-and-static-analysis/index.md) |

## Part 3: Systems

| Chapter | Title | File |
| --- | --- | --- |
| 3.0 | Introduction to Part 3: Systems | [`03-00-systems/index.md`](../locales/en-us/chapters/03-00-systems/index.md) |
| 3.1 | Architecture fundamentals | [`03-01-architecture-fundamentals/index.md`](../locales/en-us/chapters/03-01-architecture-fundamentals/index.md) |
| 3.2 | Architectural styles and patterns | [`03-02-architectural-styles-and-patterns/index.md`](../locales/en-us/chapters/03-02-architectural-styles-and-patterns/index.md) |
| 3.3 | Distributed systems | [`03-03-distributed-systems/index.md`](../locales/en-us/chapters/03-03-distributed-systems/index.md) |
| 3.4 | Data architecture and storage | [`03-04-data-architecture-and-storage/index.md`](../locales/en-us/chapters/03-04-data-architecture-and-storage/index.md) |
| 3.5 | Scalability, performance, and resilience | [`03-05-scalability-performance-resilience/index.md`](../locales/en-us/chapters/03-05-scalability-performance-resilience/index.md) |
| 3.6 | Legacy modernization | [`03-06-legacy-modernization/index.md`](../locales/en-us/chapters/03-06-legacy-modernization/index.md) |
| 3.7 | Software maintenance | [`03-07-software-maintenance/index.md`](../locales/en-us/chapters/03-07-software-maintenance/index.md) |
| 3.8 | Interoperability and open standards | [`03-08-interoperability-and-open-standards/index.md`](../locales/en-us/chapters/03-08-interoperability-and-open-standards/index.md) |
| 3.9 | Systems engineering | [`03-09-systems-engineering/index.md`](../locales/en-us/chapters/03-09-systems-engineering/index.md) |
| 3.10 | Embedded and real-time systems | [`03-10-embedded-and-real-time-systems/index.md`](../locales/en-us/chapters/03-10-embedded-and-real-time-systems/index.md) |
| 3.11 | Cloud architecture | [`03-11-cloud-architecture/index.md`](../locales/en-us/chapters/03-11-cloud-architecture/index.md) |
| 3.12 | Event-driven architecture and messaging | [`03-12-event-driven-architecture-and-messaging/index.md`](../locales/en-us/chapters/03-12-event-driven-architecture-and-messaging/index.md) |
| 3.13 | Networking and connectivity | [`03-13-networking-and-connectivity/index.md`](../locales/en-us/chapters/03-13-networking-and-connectivity/index.md) |
| 3.14 | Multi-tenancy and SaaS architecture | [`03-14-multi-tenancy-and-saas-architecture/index.md`](../locales/en-us/chapters/03-14-multi-tenancy-and-saas-architecture/index.md) |
| 3.15 | Caching and content delivery | [`03-15-caching-and-content-delivery/index.md`](../locales/en-us/chapters/03-15-caching-and-content-delivery/index.md) |
| 3.16 | API gateways and service mesh | [`03-16-api-gateways-and-service-mesh/index.md`](../locales/en-us/chapters/03-16-api-gateways-and-service-mesh/index.md) |
| 3.17 | Search and information retrieval | [`03-17-search-and-information-retrieval/index.md`](../locales/en-us/chapters/03-17-search-and-information-retrieval/index.md) |

## Part 4: Security

| Chapter | Title | File |
| --- | --- | --- |
| 4.0 | Introduction to Part 4: Security | [`04-00-security/index.md`](../locales/en-us/chapters/04-00-security/index.md) |
| 4.1 | Security foundations and culture | [`04-01-security-foundations-and-culture/index.md`](../locales/en-us/chapters/04-01-security-foundations-and-culture/index.md) |
| 4.2 | Application security | [`04-02-application-security/index.md`](../locales/en-us/chapters/04-02-application-security/index.md) |
| 4.3 | Infrastructure and cloud security | [`04-03-infrastructure-and-cloud-security/index.md`](../locales/en-us/chapters/04-03-infrastructure-and-cloud-security/index.md) |
| 4.4 | Security operations | [`04-04-security-operations/index.md`](../locales/en-us/chapters/04-04-security-operations/index.md) |
| 4.5 | Privacy and data protection | [`04-05-privacy-and-data-protection/index.md`](../locales/en-us/chapters/04-05-privacy-and-data-protection/index.md) |
| 4.6 | Compliance and governance | [`04-06-compliance-and-governance/index.md`](../locales/en-us/chapters/04-06-compliance-and-governance/index.md) |
| 4.7 | Identity and access management | [`04-07-identity-and-access-management/index.md`](../locales/en-us/chapters/04-07-identity-and-access-management/index.md) |
| 4.8 | Cryptography and key management | [`04-08-cryptography-and-key-management/index.md`](../locales/en-us/chapters/04-08-cryptography-and-key-management/index.md) |
| 4.9 | Secure software development lifecycle | [`04-09-secure-software-development-lifecycle/index.md`](../locales/en-us/chapters/04-09-secure-software-development-lifecycle/index.md) |
| 4.10 | Penetration testing and red teaming | [`04-10-penetration-testing-and-red-teaming/index.md`](../locales/en-us/chapters/04-10-penetration-testing-and-red-teaming/index.md) |

## Part 5: UI/UX Design

| Chapter | Title | File |
| --- | --- | --- |
| 5.0 | Introduction to Part 5: UI/UX Design | [`05-00-ui-ux-design/index.md`](../locales/en-us/chapters/05-00-ui-ux-design/index.md) |
| 5.1 | UX foundations | [`05-01-ux-foundations/index.md`](../locales/en-us/chapters/05-01-ux-foundations/index.md) |
| 5.2 | UI design and design systems | [`05-02-ui-design-and-design-systems/index.md`](../locales/en-us/chapters/05-02-ui-design-and-design-systems/index.md) |
| 5.3 | Accessibility | [`05-03-accessibility/index.md`](../locales/en-us/chapters/05-03-accessibility/index.md) |
| 5.4 | Content and communication design | [`05-04-content-and-communication-design/index.md`](../locales/en-us/chapters/05-04-content-and-communication-design/index.md) |
| 5.5 | Internationalization and localization | [`05-05-internationalization-and-localization/index.md`](../locales/en-us/chapters/05-05-internationalization-and-localization/index.md) |
| 5.6 | Frontend engineering | [`05-06-frontend-engineering/index.md`](../locales/en-us/chapters/05-06-frontend-engineering/index.md) |
| 5.7 | Mobile application development | [`05-07-mobile-application-development/index.md`](../locales/en-us/chapters/05-07-mobile-application-development/index.md) |
| 5.8 | Design research and usability testing | [`05-08-design-research-and-usability-testing/index.md`](../locales/en-us/chapters/05-08-design-research-and-usability-testing/index.md) |
| 5.9 | Service design | [`05-09-service-design/index.md`](../locales/en-us/chapters/05-09-service-design/index.md) |
| 5.10 | Data visualization design | [`05-10-data-visualization-design/index.md`](../locales/en-us/chapters/05-10-data-visualization-design/index.md) |

## Part 6: Artificial Intelligence

| Chapter | Title | File |
| --- | --- | --- |
| 6.0 | Introduction to Part 6: Artificial Intelligence | [`06-00-artificial-intelligence/index.md`](../locales/en-us/chapters/06-00-artificial-intelligence/index.md) |
| 6.1 | AI strategy and readiness | [`06-01-ai-strategy-and-readiness/index.md`](../locales/en-us/chapters/06-01-ai-strategy-and-readiness/index.md) |
| 6.2 | Machine learning engineering (MLOps) | [`06-02-mlops/index.md`](../locales/en-us/chapters/06-02-mlops/index.md) |
| 6.3 | Generative AI and LLM applications | [`06-03-generative-ai-and-llm-applications/index.md`](../locales/en-us/chapters/06-03-generative-ai-and-llm-applications/index.md) |
| 6.4 | AI-assisted software development | [`06-04-ai-assisted-software-development/index.md`](../locales/en-us/chapters/06-04-ai-assisted-software-development/index.md) |
| 6.5 | Responsible and trustworthy AI | [`06-05-responsible-and-trustworthy-ai/index.md`](../locales/en-us/chapters/06-05-responsible-and-trustworthy-ai/index.md) |
| 6.6 | AI infrastructure and operations | [`06-06-ai-infrastructure-and-operations/index.md`](../locales/en-us/chapters/06-06-ai-infrastructure-and-operations/index.md) |
| 6.7 | AI agents and agentic systems | [`06-07-ai-agents-and-agentic-systems/index.md`](../locales/en-us/chapters/06-07-ai-agents-and-agentic-systems/index.md) |
| 6.8 | AI evaluation and testing | [`06-08-ai-evaluation-and-testing/index.md`](../locales/en-us/chapters/06-08-ai-evaluation-and-testing/index.md) |
| 6.9 | Prompt engineering and context design | [`06-09-prompt-engineering-and-context-design/index.md`](../locales/en-us/chapters/06-09-prompt-engineering-and-context-design/index.md) |

## Part 7: Data, Analytics, and Insight

| Chapter | Title | File |
| --- | --- | --- |
| 7.0 | Introduction to Part 7: Data, Analytics, and Insight | [`07-00-data-and-analytics/index.md`](../locales/en-us/chapters/07-00-data-and-analytics/index.md) |
| 7.1 | Data strategy and governance | [`07-01-data-strategy-and-governance/index.md`](../locales/en-us/chapters/07-01-data-strategy-and-governance/index.md) |
| 7.2 | Data engineering | [`07-02-data-engineering/index.md`](../locales/en-us/chapters/07-02-data-engineering/index.md) |
| 7.3 | Analytics and business intelligence | [`07-03-analytics-and-business-intelligence/index.md`](../locales/en-us/chapters/07-03-analytics-and-business-intelligence/index.md) |
| 7.4 | Product analytics and experimentation | [`07-04-product-analytics-and-experimentation/index.md`](../locales/en-us/chapters/07-04-product-analytics-and-experimentation/index.md) |
| 7.5 | Decision science and data-informed culture | [`07-05-decision-science-and-data-culture/index.md`](../locales/en-us/chapters/07-05-decision-science-and-data-culture/index.md) |
| 7.6 | Real-time and streaming data | [`07-06-real-time-and-streaming-data/index.md`](../locales/en-us/chapters/07-06-real-time-and-streaming-data/index.md) |
| 7.7 | Data modeling and the semantic layer | [`07-07-data-modelling-and-semantic-layer/index.md`](../locales/en-us/chapters/07-07-data-modelling-and-semantic-layer/index.md) |
| 7.8 | Data quality and observability | [`07-08-data-quality-and-observability/index.md`](../locales/en-us/chapters/07-08-data-quality-and-observability/index.md) |
| 7.9 | Master data and reference data management | [`07-09-master-data-and-reference-data-management/index.md`](../locales/en-us/chapters/07-09-master-data-and-reference-data-management/index.md) |

## Part 8: Automation

| Chapter | Title | File |
| --- | --- | --- |
| 8.0 | Introduction to Part 8: Automation | [`08-00-automation/index.md`](../locales/en-us/chapters/08-00-automation/index.md) |
| 8.1 | CI/CD and delivery | [`08-01-ci-cd-and-delivery/index.md`](../locales/en-us/chapters/08-01-ci-cd-and-delivery/index.md) |
| 8.2 | Infrastructure as code and configuration | [`08-02-infrastructure-as-code-and-configuration/index.md`](../locales/en-us/chapters/08-02-infrastructure-as-code-and-configuration/index.md) |
| 8.3 | Containers, orchestration, and cloud-native | [`08-03-containers-orchestration-cloud-native/index.md`](../locales/en-us/chapters/08-03-containers-orchestration-cloud-native/index.md) |
| 8.4 | Platform engineering and developer experience | [`08-04-platform-engineering-and-devex/index.md`](../locales/en-us/chapters/08-04-platform-engineering-and-devex/index.md) |
| 8.5 | Test and process automation | [`08-05-test-and-process-automation/index.md`](../locales/en-us/chapters/08-05-test-and-process-automation/index.md) |
| 8.6 | Release management and progressive delivery | [`08-06-release-management-and-progressive-delivery/index.md`](../locales/en-us/chapters/08-06-release-management-and-progressive-delivery/index.md) |
| 8.7 | Build systems and artifact management | [`08-07-build-systems-and-artifact-management/index.md`](../locales/en-us/chapters/08-07-build-systems-and-artifact-management/index.md) |

## Part 9: Operations, Reliability, and Observability

| Chapter | Title | File |
| --- | --- | --- |
| 9.0 | Introduction to Part 9: Operations, Reliability, and Observability | [`09-00-operations-and-reliability/index.md`](../locales/en-us/chapters/09-00-operations-and-reliability/index.md) |
| 9.1 | Site reliability engineering | [`09-01-site-reliability-engineering/index.md`](../locales/en-us/chapters/09-01-site-reliability-engineering/index.md) |
| 9.2 | Observability and telemetry | [`09-02-observability-and-telemetry/index.md`](../locales/en-us/chapters/09-02-observability-and-telemetry/index.md) |
| 9.3 | Incident management | [`09-03-incident-management/index.md`](../locales/en-us/chapters/09-03-incident-management/index.md) |
| 9.4 | Cost, sustainability, and green software | [`09-04-cost-sustainability-green-software/index.md`](../locales/en-us/chapters/09-04-cost-sustainability-green-software/index.md) |
| 9.5 | Disaster recovery and business continuity | [`09-05-disaster-recovery-and-business-continuity/index.md`](../locales/en-us/chapters/09-05-disaster-recovery-and-business-continuity/index.md) |
| 9.6 | Chaos engineering and resilience testing | [`09-06-chaos-engineering-and-resilience-testing/index.md`](../locales/en-us/chapters/09-06-chaos-engineering-and-resilience-testing/index.md) |
| 9.7 | Capacity planning and demand forecasting | [`09-07-capacity-planning-and-demand-forecasting/index.md`](../locales/en-us/chapters/09-07-capacity-planning-and-demand-forecasting/index.md) |
| 9.8 | On-call and operational readiness | [`09-08-on-call-and-operational-readiness/index.md`](../locales/en-us/chapters/09-08-on-call-and-operational-readiness/index.md) |

## Part 10: Project/Product/Programme Management

| Chapter | Title | File |
| --- | --- | --- |
| 10.0 | Introduction to Part 10: Project/Product/Program Management | [`10-00-project-product-programme-management/index.md`](../locales/en-us/chapters/10-00-project-product-programme-management/index.md) |
| 10.1 | Portfolio and program management | [`10-01-portfolio-and-programme-management/index.md`](../locales/en-us/chapters/10-01-portfolio-and-programme-management/index.md) |
| 10.2 | Risk, audit, and assurance | [`10-02-risk-audit-and-assurance/index.md`](../locales/en-us/chapters/10-02-risk-audit-and-assurance/index.md) |
| 10.3 | Procurement, open source, and licensing | [`10-03-procurement-open-source-and-licensing/index.md`](../locales/en-us/chapters/10-03-procurement-open-source-and-licensing/index.md) |
| 10.4 | Sustaining large and long-lived systems | [`10-04-sustaining-large-and-long-lived-systems/index.md`](../locales/en-us/chapters/10-04-sustaining-large-and-long-lived-systems/index.md) |
| 10.5 | Ethics, accountability, and public interest | [`10-05-ethics-accountability-public-interest/index.md`](../locales/en-us/chapters/10-05-ethics-accountability-public-interest/index.md) |
| 10.6 | Project management | [`10-06-project-management/index.md`](../locales/en-us/chapters/10-06-project-management/index.md) |
| 10.7 | Agile | [`10-07-agile/index.md`](../locales/en-us/chapters/10-07-agile/index.md) |
| 10.8 | Maturity models | [`10-08-maturity-models/index.md`](../locales/en-us/chapters/10-08-maturity-models/index.md) |
| 10.9 | Innovation partnership | [`10-09-innovation-partnership/index.md`](../locales/en-us/chapters/10-09-innovation-partnership/index.md) |
| 10.10 | Software engineering economics | [`10-10-software-engineering-economics/index.md`](../locales/en-us/chapters/10-10-software-engineering-economics/index.md) |
| 10.11 | Digital sovereignty | [`10-11-digital-sovereignty/index.md`](../locales/en-us/chapters/10-11-digital-sovereignty/index.md) |
| 10.12 | Open source vs closed source | [`10-12-open-source-vs-closed-source/index.md`](../locales/en-us/chapters/10-12-open-source-vs-closed-source/index.md) |
| 10.13 | Interorganization collaboration | [`10-13-interorganization-collaboration/index.md`](../locales/en-us/chapters/10-13-interorganization-collaboration/index.md) |
| 10.14 | Product management and discovery | [`10-14-product-management-and-discovery/index.md`](../locales/en-us/chapters/10-14-product-management-and-discovery/index.md) |
| 10.15 | Estimation and forecasting | [`10-15-estimation-and-forecasting/index.md`](../locales/en-us/chapters/10-15-estimation-and-forecasting/index.md) |
| 10.16 | Stakeholder management and communication | [`10-16-stakeholder-management-and-communication/index.md`](../locales/en-us/chapters/10-16-stakeholder-management-and-communication/index.md) |
| 10.17 | Organizational change management | [`10-17-organizational-change-management/index.md`](../locales/en-us/chapters/10-17-organizational-change-management/index.md) |
| 10.18 | Open source program office (OSPO) and upstream contribution | [`10-18-open-source-program-office/index.md`](../locales/en-us/chapters/10-18-open-source-program-office/index.md) |

## Part 11: Flow: Discovery and Delivery Pipelines

| Chapter | Title | File |
| --- | --- | --- |
| 11.0 | Introduction to Part 11: Flow: Discovery and Delivery Pipelines | [`11-00-flow-discovery-and-delivery/index.md`](../locales/en-us/chapters/11-00-flow-discovery-and-delivery/index.md) |
| 11.1 | The discovery pipeline | [`11-01-discovery-pipeline/index.md`](../locales/en-us/chapters/11-01-discovery-pipeline/index.md) |
| 11.2 | The delivery pipeline | [`11-02-delivery-pipeline/index.md`](../locales/en-us/chapters/11-02-delivery-pipeline/index.md) |
| 11.3 | Queueing theory | [`11-03-queueing-theory/index.md`](../locales/en-us/chapters/11-03-queueing-theory/index.md) |
| 11.4 | Objectives and key results (OKRs) | [`11-04-objectives-and-key-results/index.md`](../locales/en-us/chapters/11-04-objectives-and-key-results/index.md) |
| 11.5 | Key performance indicators (KPIs) | [`11-05-key-performance-indicators/index.md`](../locales/en-us/chapters/11-05-key-performance-indicators/index.md) |
| 11.6 | Value stream mapping and cost of delay | [`11-06-value-stream-mapping-and-cost-of-delay/index.md`](../locales/en-us/chapters/11-06-value-stream-mapping-and-cost-of-delay/index.md) |

## Part 12: Appendices

| Chapter | Title | File |
| --- | --- | --- |
| 12.0 | Appendices | [`12-00-appendices/index.md`](../locales/en-us/chapters/12-00-appendices/index.md) |
| 12.1 | Glossary | [`12-01-glossary/index.md`](../locales/en-us/chapters/12-01-glossary/index.md) |
| 12.2 | Checklists | [`12-02-checklists/index.md`](../locales/en-us/chapters/12-02-checklists/index.md) |
| 12.3 | Templates | [`12-03-templates/index.md`](../locales/en-us/chapters/12-03-templates/index.md) |
| 12.4 | Maturity self-assessment | [`12-04-maturity-self-assessment/index.md`](../locales/en-us/chapters/12-04-maturity-self-assessment/index.md) |
| 12.5 | References | [`12-05-references/index.md`](../locales/en-us/chapters/12-05-references/index.md) |
| 12.6 | Adoption roadmap | [`12-06-adoption-roadmap/index.md`](../locales/en-us/chapters/12-06-adoption-roadmap/index.md) |
| 12.7 | Index | [`12-07-index/index.md`](../locales/en-us/chapters/12-07-index/index.md) |
