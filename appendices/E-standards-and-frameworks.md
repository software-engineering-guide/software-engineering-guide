# Appendix E. Reference standards and frameworks

This appendix is an organized index of the real standards, frameworks, and
regulations referenced throughout the guidebook. It is a navigational aid, not a
compliance manual: always consult the authoritative source and, where relevant,
qualified legal or audit counsel for the current text and applicability to your
context.

Entries are grouped by domain. Each names the standard or framework, its issuing
body, a one-line scope, and the chapters or domains where it is most relevant.
Where a name is commonly abbreviated, the abbreviation is shown. Document numbers
and titles are given only where they are well established; no URLs are included.

## How to use this appendix

- **Regulations** (for example, GDPR, HIPAA) are legally binding within their
  jurisdiction and sector. They set obligations, not just good practice.
- **Standards** (for example, ISO/IEC 27001, WCAG) are formal, often
  certifiable specifications. Some are voluntary; some are mandated by law or
  contract.
- **Frameworks** (for example, NIST CSF, NIST AI RMF) are structured, usually
  voluntary guidance you tailor to your risk profile.
- Applicability depends on jurisdiction, sector, data types, and contractual
  terms. Many organizations must satisfy several of these at once.

## Security and privacy

| Standard / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Requirements for an Information Security Management System (ISMS). | 19–24 Security and compliance |
| ISO/IEC 27002 | ISO / IEC | Guidance and control set supporting ISO/IEC 27001. | 19–22 Security |
| ISO/IEC 27017 / 27018 | ISO / IEC | Cloud-specific security controls (27017) and protection of PII in the cloud (27018). | 21 Infrastructure and cloud security; 23 Privacy |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Voluntary framework organized around Govern, Identify, Protect, Detect, Respond, Recover. | 19, 22 Security foundations and operations |
| NIST SP 800-53 | National Institute of Standards and Technology | Catalog of security and privacy controls for information systems. | 21, 24 Cloud security and compliance |
| NIST SP 800-63 | National Institute of Standards and Technology | Digital identity and authentication assurance guidelines. | 20, 21 Application and infrastructure security |
| OWASP Top Ten | Open Worldwide Application Security Project | The most critical web application security risks, updated periodically. | 20 Application security |
| OWASP ASVS | Open Worldwide Application Security Project | Graded requirements and tests for verifying application security. | 9, 20 Testing and application security |
| OWASP SAMM | Open Worldwide Application Security Project | Maturity model for building and assessing a software-security program. | 19 Security foundations and culture |
| STRIDE | Originated at Microsoft | Threat-modeling taxonomy for classifying threats. | 20 Application security |
| MITRE ATT&CK | MITRE | Knowledge base of adversary tactics and techniques for detection and defense. | 22 Security operations |
| SLSA | Open Source Security Foundation (OpenSSF) | Graduated framework for software supply-chain integrity and provenance. | 20, 42, 53 Supply chain and delivery |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Standard formats for software bills of materials. | 20, 53 Application security and licensing |
| PCI DSS | PCI Security Standards Council | Security requirements for handling payment card data. | 20, 23, 24 Security, privacy, compliance |

## Compliance and government

### United States

| Regulation / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Safeguards for protected health information (PHI). | 23, 24 Privacy and compliance |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Financial reporting and internal-control requirements for public companies. | 24, 52 Compliance and audit |
| FISMA | US Congress | Information security program requirements for federal agencies. | 21, 24 Cloud security and compliance |
| FedRAMP | US General Services Administration / FedRAMP PMO | Standardized security authorization for cloud services used by federal agencies. | 21, 24 Cloud security and compliance |
| NIST SP 800-171 | National Institute of Standards and Technology | Protection of controlled unclassified information (CUI) in non-federal systems. | 24 Compliance (defense supply chain) |
| CMMC | US Department of Defense | Certification of defense-contractor cybersecurity maturity. | 24 Compliance (defense) |
| FIPS 140-3 | National Institute of Standards and Technology | Security requirements for cryptographic modules. | 21 Infrastructure and cloud security |
| CCPA / CPRA | State of California | Consumer privacy rights and business obligations in California. | 23 Privacy and data protection |

### European Union and United Kingdom

| Regulation / standard | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| GDPR | European Union | Comprehensive regulation on processing personal data. | 23, 24 Privacy and compliance |
| UK GDPR / Data Protection Act 2018 | United Kingdom | The UK's post-Brexit data-protection regime. | 23, 24 Privacy and compliance |
| eIDAS | European Union | Framework for electronic identification and trust services. | 20, 21 Security |
| NIS2 Directive | European Union | Cybersecurity obligations for essential and important entities. | 22, 24 Security operations and compliance |
| DORA (Digital Operational Resilience Act) | European Union | Operational-resilience requirements for the financial sector. | 47, 52 Reliability and audit |
| EU AI Act | European Union | Risk-based regulation of AI systems (see AI governance below). | 31, 35 AI strategy and responsible AI |

## Accessibility

| Standard | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Guidelines for accessible web content, with A/AA/AAA conformance levels. | 27 Accessibility; 25–30 UX and frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Roles, states, and properties for accessible rich internet applications. | 27, 30 Accessibility and frontend |
| Section 508 | US Access Board / US federal law | Accessibility requirements for US federal ICT, aligned with WCAG. | 27 Accessibility (US government) |
| EN 301 549 | ETSI / CEN / CENELEC | European accessibility requirements for ICT procurement, aligned with WCAG. | 27 Accessibility (EU public sector) |
| ADA (Americans with Disabilities Act) | US Congress | Civil-rights law prohibiting disability discrimination, applied to digital services. | 27 Accessibility |
| ISO/IEC 40500 | ISO / IEC | International adoption of WCAG 2.0 as a formal standard. | 27 Accessibility |

## AI governance

| Framework / regulation | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Voluntary framework to govern, map, measure, and manage AI risk. | 31, 35 AI strategy and responsible AI |
| ISO/IEC 42001 | ISO / IEC | Requirements for an AI Management System (AIMS). | 31, 35 AI governance |
| ISO/IEC 23894 | ISO / IEC | Guidance on AI-specific risk management. | 35 Responsible and trustworthy AI |
| EU AI Act | European Union | Risk-tiered legal obligations for providers and deployers of AI systems. | 31, 33, 35 AI applications and governance |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Values-based principles for trustworthy AI, influential on policy. | 35, 55 Responsible AI and ethics |

## Quality and process

| Standard / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Software product quality model (functional suitability, reliability, security, etc.). | 7, 9 Design and testing |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Software life-cycle processes. | 4, 51 Ways of working and program management |
| ISO 9001 | ISO | Requirements for a general Quality Management System. | 52 Risk, audit, and assurance |
| CMMI | ISACA / CMMI Institute | Maturity model for process capability and improvement. | 51, 52 Program management and assurance |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | Four key delivery-performance metrics for software teams. | 42, 45, 47 Delivery, platform, reliability |
| SPACE framework | Microsoft / GitHub researchers | Multidimensional model for measuring developer productivity. | 3, 45 Growth and developer experience |
| ITIL | AXELOS / PeopleCert | Framework of IT service-management practices. | 47, 49 Reliability and incident management |

## Architecture

| Standard / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Standard for architecture description and viewpoints. | 12, 13 Documentation and architecture fundamentals |
| TOGAF | The Open Group | Enterprise-architecture framework and development method. | 13, 51 Architecture and portfolio management |
| C4 model | Community (Simon Brown) | Four-level approach to visualizing software architecture. | 12, 13 Documentation and architecture |
| arc42 | Community (Starke / Hruschka) | Template for structuring architecture documentation. | 12, 13 Documentation and architecture |
| ADRs | Community practice | Lightweight records of significant architecture decisions. | 5, 12, 13 Decision-making and documentation |

## Cloud and DevOps

| Standard / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Consensus-based secure-configuration baselines for systems and cloud. | 21, 43 Infrastructure security and IaC |
| CNCF landscape and projects | Cloud Native Computing Foundation | Ecosystem and standards for cloud-native computing (e.g., Kubernetes). | 44 Containers and cloud native |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Open standards for container image and runtime formats. | 44 Containers and cloud native |
| OpenTelemetry | Cloud Native Computing Foundation | Vendor-neutral standard for telemetry (traces, metrics, logs). | 48 Observability and monitoring |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | General-purpose policy engine for policy as code. | 24, 43, 44 Compliance, IaC, orchestration |
| SRE practices | Google (widely adopted) | SLI/SLO/error-budget-based approach to operating reliable services. | 47 Site reliability engineering |
| FinOps Framework | FinOps Foundation | Practices for cloud financial management and cost accountability. | 50 Cost, sustainability, green software |

## Data

| Standard / framework | Issuing body | Scope (one line) | Primary chapters / domains |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Body of knowledge organizing data-management disciplines. | 37 Data strategy and governance |
| ISO/IEC 38505 | ISO / IEC | Governance of data as an organizational asset. | 37 Data governance |
| ISO 8000 | ISO | Data quality and master-data standards. | 37, 38 Data governance and engineering |
| Data mesh | Community (Zhamak Dehghani) | Decentralized, domain-oriented approach to data as a product. | 37, 38 Data strategy and engineering |
| DCAM | EDM Council | Data-management capability assessment model. | 37 Data strategy and governance |

## Notes on scope and change

Standards and regulations evolve. Version numbers (for example, WCAG 2.1 versus
2.2, or ISO revision years) and control catalogs change over time, and new laws
(such as sector-specific AI and resilience regulations) continue to emerge. Treat
this appendix as a starting map: confirm the current version, jurisdiction, and
applicability before relying on any entry for a compliance or procurement
decision. Where the guidebook chapters and this appendix differ in detail, the
authoritative source document always governs.
