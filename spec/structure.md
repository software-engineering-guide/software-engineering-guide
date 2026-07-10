# Structure (canonical chapter manifest)

This file is the structural source of truth for the guidebook. It lists every
part and chapter with its decimal number, title, and file. The test suite
(`tests/validate.py`) checks that the files on disk match this manifest exactly,
and the navigation generator (`tools/gen_nav.py`) derives the table of contents,
index, and specification outline from the same files. Change the structure here
and in the chapter files together; the tests will catch any drift.

Totals: **12 parts**, **111 chapters** (each part opens with an N.0 introduction).

## Part 1: People

| Chapter | Title | File |
| --- | --- | --- |
| 1.0 | Introduction to Part 1: People | [`1.0-people.md`](../docs/chapters/1.0-people.md) |
| 1.1 | Software engineering values | [`1.1-software-engineering-values.md`](../docs/chapters/1.1-software-engineering-values.md) |
| 1.2 | Team topologies and organizational design | [`1.2-team-topologies.md`](../docs/chapters/1.2-team-topologies.md) |
| 1.3 | Roles, career ladders, and growth | [`1.3-roles-career-ladders-growth.md`](../docs/chapters/1.3-roles-career-ladders-growth.md) |
| 1.4 | Ways of working | [`1.4-ways-of-working.md`](../docs/chapters/1.4-ways-of-working.md) |
| 1.5 | Decision-making and governance | [`1.5-decision-making-and-governance.md`](../docs/chapters/1.5-decision-making-and-governance.md) |
| 1.6 | Decision records | [`1.6-decision-records.md`](../docs/chapters/1.6-decision-records.md) |
| 1.7 | Engineering standards and exceptions | [`1.7-engineering-standards-and-exceptions.md`](../docs/chapters/1.7-engineering-standards-and-exceptions.md) |
| 1.8 | Hiring, interviewing, and onboarding | [`1.8-hiring-interviewing-onboarding.md`](../docs/chapters/1.8-hiring-interviewing-onboarding.md) |
| 1.9 | Distributed and remote work | [`1.9-distributed-and-remote-work.md`](../docs/chapters/1.9-distributed-and-remote-work.md) |
| 1.10 | Engineering effectiveness and developer productivity | [`1.10-engineering-effectiveness-and-developer-productivity.md`](../docs/chapters/1.10-engineering-effectiveness-and-developer-productivity.md) |

## Part 2: Software Programming

| Chapter | Title | File |
| --- | --- | --- |
| 2.0 | Introduction to Part 2: Software Programming | [`2.0-software-programming.md`](../docs/chapters/2.0-software-programming.md) |
| 2.1 | Coding standards and style | [`2.1-coding-standards-and-style.md`](../docs/chapters/2.1-coding-standards-and-style.md) |
| 2.2 | Software design principles | [`2.2-software-design-principles.md`](../docs/chapters/2.2-software-design-principles.md) |
| 2.3 | APIs and interface design | [`2.3-apis-and-interface-design.md`](../docs/chapters/2.3-apis-and-interface-design.md) |
| 2.4 | Testing strategy | [`2.4-testing-strategy.md`](../docs/chapters/2.4-testing-strategy.md) |
| 2.5 | Code review and collaboration | [`2.5-code-review-and-collaboration.md`](../docs/chapters/2.5-code-review-and-collaboration.md) |
| 2.6 | Version control and source management | [`2.6-version-control-and-source-management.md`](../docs/chapters/2.6-version-control-and-source-management.md) |
| 2.7 | Documentation | [`2.7-documentation.md`](../docs/chapters/2.7-documentation.md) |
| 2.8 | Software requirements | [`2.8-software-requirements.md`](../docs/chapters/2.8-software-requirements.md) |
| 2.9 | Software construction | [`2.9-software-construction.md`](../docs/chapters/2.9-software-construction.md) |
| 2.10 | Software configuration management | [`2.10-software-configuration-management.md`](../docs/chapters/2.10-software-configuration-management.md) |
| 2.11 | Software quality | [`2.11-software-quality.md`](../docs/chapters/2.11-software-quality.md) |
| 2.12 | Software models and methods | [`2.12-software-models-and-methods.md`](../docs/chapters/2.12-software-models-and-methods.md) |
| 2.13 | Computing, mathematical, and engineering foundations | [`2.13-computing-mathematical-engineering-foundations.md`](../docs/chapters/2.13-computing-mathematical-engineering-foundations.md) |
| 2.14 | Project and repository structure | [`2.14-project-and-repository-structure.md`](../docs/chapters/2.14-project-and-repository-structure.md) |
| 2.15 | Debugging and troubleshooting | [`2.15-debugging-and-troubleshooting.md`](../docs/chapters/2.15-debugging-and-troubleshooting.md) |
| 2.16 | Performance engineering | [`2.16-performance-engineering.md`](../docs/chapters/2.16-performance-engineering.md) |

## Part 3: Systems

| Chapter | Title | File |
| --- | --- | --- |
| 3.0 | Introduction to Part 3: Systems | [`3.0-systems.md`](../docs/chapters/3.0-systems.md) |
| 3.1 | Architecture fundamentals | [`3.1-architecture-fundamentals.md`](../docs/chapters/3.1-architecture-fundamentals.md) |
| 3.2 | Architectural styles and patterns | [`3.2-architectural-styles-and-patterns.md`](../docs/chapters/3.2-architectural-styles-and-patterns.md) |
| 3.3 | Distributed systems | [`3.3-distributed-systems.md`](../docs/chapters/3.3-distributed-systems.md) |
| 3.4 | Data architecture and storage | [`3.4-data-architecture-and-storage.md`](../docs/chapters/3.4-data-architecture-and-storage.md) |
| 3.5 | Scalability, performance, and resilience | [`3.5-scalability-performance-resilience.md`](../docs/chapters/3.5-scalability-performance-resilience.md) |
| 3.6 | Legacy modernization | [`3.6-legacy-modernization.md`](../docs/chapters/3.6-legacy-modernization.md) |
| 3.7 | Software maintenance | [`3.7-software-maintenance.md`](../docs/chapters/3.7-software-maintenance.md) |
| 3.8 | Interoperability and open standards | [`3.8-interoperability-and-open-standards.md`](../docs/chapters/3.8-interoperability-and-open-standards.md) |
| 3.9 | Systems engineering | [`3.9-systems-engineering.md`](../docs/chapters/3.9-systems-engineering.md) |
| 3.10 | Embedded and real-time systems | [`3.10-embedded-and-real-time-systems.md`](../docs/chapters/3.10-embedded-and-real-time-systems.md) |

## Part 4: Security

| Chapter | Title | File |
| --- | --- | --- |
| 4.0 | Introduction to Part 4: Security | [`4.0-security.md`](../docs/chapters/4.0-security.md) |
| 4.1 | Security foundations and culture | [`4.1-security-foundations-and-culture.md`](../docs/chapters/4.1-security-foundations-and-culture.md) |
| 4.2 | Application security | [`4.2-application-security.md`](../docs/chapters/4.2-application-security.md) |
| 4.3 | Infrastructure and cloud security | [`4.3-infrastructure-and-cloud-security.md`](../docs/chapters/4.3-infrastructure-and-cloud-security.md) |
| 4.4 | Security operations | [`4.4-security-operations.md`](../docs/chapters/4.4-security-operations.md) |
| 4.5 | Privacy and data protection | [`4.5-privacy-and-data-protection.md`](../docs/chapters/4.5-privacy-and-data-protection.md) |
| 4.6 | Compliance and governance | [`4.6-compliance-and-governance.md`](../docs/chapters/4.6-compliance-and-governance.md) |
| 4.7 | Identity and access management | [`4.7-identity-and-access-management.md`](../docs/chapters/4.7-identity-and-access-management.md) |
| 4.8 | Cryptography and key management | [`4.8-cryptography-and-key-management.md`](../docs/chapters/4.8-cryptography-and-key-management.md) |

## Part 5: UI/UX Design

| Chapter | Title | File |
| --- | --- | --- |
| 5.0 | Introduction to Part 5: UI/UX Design | [`5.0-ui-ux-design.md`](../docs/chapters/5.0-ui-ux-design.md) |
| 5.1 | UX foundations | [`5.1-ux-foundations.md`](../docs/chapters/5.1-ux-foundations.md) |
| 5.2 | UI design and design systems | [`5.2-ui-design-and-design-systems.md`](../docs/chapters/5.2-ui-design-and-design-systems.md) |
| 5.3 | Accessibility | [`5.3-accessibility.md`](../docs/chapters/5.3-accessibility.md) |
| 5.4 | Content and communication design | [`5.4-content-and-communication-design.md`](../docs/chapters/5.4-content-and-communication-design.md) |
| 5.5 | Internationalization and localization | [`5.5-internationalization-and-localization.md`](../docs/chapters/5.5-internationalization-and-localization.md) |
| 5.6 | Frontend engineering | [`5.6-frontend-engineering.md`](../docs/chapters/5.6-frontend-engineering.md) |
| 5.7 | Mobile application development | [`5.7-mobile-application-development.md`](../docs/chapters/5.7-mobile-application-development.md) |

## Part 6: Artificial Intelligence

| Chapter | Title | File |
| --- | --- | --- |
| 6.0 | Introduction to Part 6: Artificial Intelligence | [`6.0-artificial-intelligence.md`](../docs/chapters/6.0-artificial-intelligence.md) |
| 6.1 | AI strategy and readiness | [`6.1-ai-strategy-and-readiness.md`](../docs/chapters/6.1-ai-strategy-and-readiness.md) |
| 6.2 | Machine learning engineering (MLOps) | [`6.2-mlops.md`](../docs/chapters/6.2-mlops.md) |
| 6.3 | Generative AI and LLM applications | [`6.3-generative-ai-and-llm-applications.md`](../docs/chapters/6.3-generative-ai-and-llm-applications.md) |
| 6.4 | AI-assisted software development | [`6.4-ai-assisted-software-development.md`](../docs/chapters/6.4-ai-assisted-software-development.md) |
| 6.5 | Responsible and trustworthy AI | [`6.5-responsible-and-trustworthy-ai.md`](../docs/chapters/6.5-responsible-and-trustworthy-ai.md) |
| 6.6 | AI infrastructure and operations | [`6.6-ai-infrastructure-and-operations.md`](../docs/chapters/6.6-ai-infrastructure-and-operations.md) |
| 6.7 | AI agents and agentic systems | [`6.7-ai-agents-and-agentic-systems.md`](../docs/chapters/6.7-ai-agents-and-agentic-systems.md) |

## Part 7: Data, Analytics, and Insight

| Chapter | Title | File |
| --- | --- | --- |
| 7.0 | Introduction to Part 7: Data, Analytics, and Insight | [`7.0-data-and-analytics.md`](../docs/chapters/7.0-data-and-analytics.md) |
| 7.1 | Data strategy and governance | [`7.1-data-strategy-and-governance.md`](../docs/chapters/7.1-data-strategy-and-governance.md) |
| 7.2 | Data engineering | [`7.2-data-engineering.md`](../docs/chapters/7.2-data-engineering.md) |
| 7.3 | Analytics and business intelligence | [`7.3-analytics-and-business-intelligence.md`](../docs/chapters/7.3-analytics-and-business-intelligence.md) |
| 7.4 | Product analytics and experimentation | [`7.4-product-analytics-and-experimentation.md`](../docs/chapters/7.4-product-analytics-and-experimentation.md) |
| 7.5 | Decision science and data-informed culture | [`7.5-decision-science-and-data-culture.md`](../docs/chapters/7.5-decision-science-and-data-culture.md) |

## Part 8: Automation

| Chapter | Title | File |
| --- | --- | --- |
| 8.0 | Introduction to Part 8: Automation | [`8.0-automation.md`](../docs/chapters/8.0-automation.md) |
| 8.1 | CI/CD and delivery | [`8.1-ci-cd-and-delivery.md`](../docs/chapters/8.1-ci-cd-and-delivery.md) |
| 8.2 | Infrastructure as code and configuration | [`8.2-infrastructure-as-code-and-configuration.md`](../docs/chapters/8.2-infrastructure-as-code-and-configuration.md) |
| 8.3 | Containers, orchestration, and cloud-native | [`8.3-containers-orchestration-cloud-native.md`](../docs/chapters/8.3-containers-orchestration-cloud-native.md) |
| 8.4 | Platform engineering and developer experience | [`8.4-platform-engineering-and-devex.md`](../docs/chapters/8.4-platform-engineering-and-devex.md) |
| 8.5 | Test and process automation | [`8.5-test-and-process-automation.md`](../docs/chapters/8.5-test-and-process-automation.md) |
| 8.6 | Release management and progressive delivery | [`8.6-release-management-and-progressive-delivery.md`](../docs/chapters/8.6-release-management-and-progressive-delivery.md) |

## Part 9: Operations, Reliability, and Observability

| Chapter | Title | File |
| --- | --- | --- |
| 9.0 | Introduction to Part 9: Operations, Reliability, and Observability | [`9.0-operations-and-reliability.md`](../docs/chapters/9.0-operations-and-reliability.md) |
| 9.1 | Site reliability engineering | [`9.1-site-reliability-engineering.md`](../docs/chapters/9.1-site-reliability-engineering.md) |
| 9.2 | Observability and telemetry | [`9.2-observability-and-telemetry.md`](../docs/chapters/9.2-observability-and-telemetry.md) |
| 9.3 | Incident management | [`9.3-incident-management.md`](../docs/chapters/9.3-incident-management.md) |
| 9.4 | Cost, sustainability, and green software | [`9.4-cost-sustainability-green-software.md`](../docs/chapters/9.4-cost-sustainability-green-software.md) |
| 9.5 | Disaster recovery and business continuity | [`9.5-disaster-recovery-and-business-continuity.md`](../docs/chapters/9.5-disaster-recovery-and-business-continuity.md) |

## Part 10: Project/Product/Program Management

| Chapter | Title | File |
| --- | --- | --- |
| 10.0 | Introduction to Part 10: Project/Product/Program Management | [`10.0-project-product-program-management.md`](../docs/chapters/10.0-project-product-program-management.md) |
| 10.1 | Portfolio and program management | [`10.1-portfolio-and-program-management.md`](../docs/chapters/10.1-portfolio-and-program-management.md) |
| 10.2 | Risk, audit, and assurance | [`10.2-risk-audit-and-assurance.md`](../docs/chapters/10.2-risk-audit-and-assurance.md) |
| 10.3 | Procurement, open source, and licensing | [`10.3-procurement-open-source-and-licensing.md`](../docs/chapters/10.3-procurement-open-source-and-licensing.md) |
| 10.4 | Sustaining large and long-lived systems | [`10.4-sustaining-large-and-long-lived-systems.md`](../docs/chapters/10.4-sustaining-large-and-long-lived-systems.md) |
| 10.5 | Ethics, accountability, and public interest | [`10.5-ethics-accountability-public-interest.md`](../docs/chapters/10.5-ethics-accountability-public-interest.md) |
| 10.6 | Project management | [`10.6-project-management.md`](../docs/chapters/10.6-project-management.md) |
| 10.7 | Agile | [`10.7-agile.md`](../docs/chapters/10.7-agile.md) |
| 10.8 | Maturity models | [`10.8-maturity-models.md`](../docs/chapters/10.8-maturity-models.md) |
| 10.9 | Innovation partnership | [`10.9-innovation-partnership.md`](../docs/chapters/10.9-innovation-partnership.md) |
| 10.10 | Software engineering economics | [`10.10-software-engineering-economics.md`](../docs/chapters/10.10-software-engineering-economics.md) |
| 10.11 | Digital sovereignty | [`10.11-digital-sovereignty.md`](../docs/chapters/10.11-digital-sovereignty.md) |
| 10.12 | Open source vs closed source | [`10.12-open-source-vs-closed-source.md`](../docs/chapters/10.12-open-source-vs-closed-source.md) |
| 10.13 | Interorganization collaboration | [`10.13-interorganization-collaboration.md`](../docs/chapters/10.13-interorganization-collaboration.md) |

## Part 11: Flow: Discovery and Delivery Pipelines

| Chapter | Title | File |
| --- | --- | --- |
| 11.0 | Introduction to Part 11: Flow: Discovery and Delivery Pipelines | [`11.0-flow-discovery-and-delivery.md`](../docs/chapters/11.0-flow-discovery-and-delivery.md) |
| 11.1 | The discovery pipeline | [`11.1-discovery-pipeline.md`](../docs/chapters/11.1-discovery-pipeline.md) |
| 11.2 | The delivery pipeline | [`11.2-delivery-pipeline.md`](../docs/chapters/11.2-delivery-pipeline.md) |
| 11.3 | Queueing theory | [`11.3-queueing-theory.md`](../docs/chapters/11.3-queueing-theory.md) |
| 11.4 | Objectives and key results (OKRs) | [`11.4-objectives-and-key-results.md`](../docs/chapters/11.4-objectives-and-key-results.md) |
| 11.5 | Key performance indicators (KPIs) | [`11.5-key-performance-indicators.md`](../docs/chapters/11.5-key-performance-indicators.md) |

## Part 12: Appendices

| Chapter | Title | File |
| --- | --- | --- |
| 12.0 | Appendices | [`12.0-appendices.md`](../docs/chapters/12.0-appendices.md) |
| 12.1 | Glossary | [`12.1-glossary.md`](../docs/chapters/12.1-glossary.md) |
| 12.2 | Checklists | [`12.2-checklists.md`](../docs/chapters/12.2-checklists.md) |
| 12.3 | Templates | [`12.3-templates.md`](../docs/chapters/12.3-templates.md) |
| 12.4 | Maturity self-assessment | [`12.4-maturity-self-assessment.md`](../docs/chapters/12.4-maturity-self-assessment.md) |
| 12.5 | References | [`12.5-references.md`](../docs/chapters/12.5-references.md) |
| 12.6 | Adoption roadmap | [`12.6-adoption-roadmap.md`](../docs/chapters/12.6-adoption-roadmap.md) |
| 12.7 | Index | [`12.7-index.md`](../docs/chapters/12.7-index.md) |
