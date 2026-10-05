# 12.5 参考资料

本节汇总了本指南的参考体系：与 SWEBOK 知识体系的对照表、贯穿全书引用的标准与框架索引，以及一份精心编选的推荐阅读书目。各章节的具体来源也会出现在每章末尾的《参考资料与延伸阅读》部分。

---

# SWEBOK 对照表

本指南与 IEEE 计算机学会（IEEE Computer Society）的 **SWEBOK V4.0**（软件工程知识体系）保持一致。全部 18 个知识领域均已涵盖；下表将每个知识领域映射到相应涉及的章节，而本指南的内容还远远超出 SWEBOK 的范畴，进一步覆盖了人工智能、数据、用户体验、DevOps、可持续性、流动性以及公共利益技术等领域。

| SWEBOK V4.0 知识领域 | 主要章节 |
|---|---|
| 1. 软件需求 | 2.8, 11.1, 5.1 |
| 2. 软件架构 | 3.1, 3.2, 3.3 |
| 3. 软件设计 | 2.2, 3.1 |
| 4. 软件构建 | 2.9, 2.1 |
| 5. 软件测试 | 2.4, 8.5 |
| 6. 软件工程运维 | 9.1, 9.2, 9.3, 8.1 |
| 7. 软件维护 | 3.7, 3.6, 10.4 |
| 8. 软件配置管理 | 2.10, 2.6, 8.2 |
| 9. 软件工程管理 | 10.1, 10.6, 10.2 |
| 10. 软件工程过程 | 1.4, 10.7, 10.8 |
| 11. 软件工程模型与方法 | 2.12, 3.1, 2.2 |
| 12. 软件质量 | 2.11, 2.4, 3.1 |
| 13. 软件安全 | 4.1, 4.2, 4.3, 4.4 |
| 14. 软件工程职业实践 | 10.5, 1.1, 1.3 |
| 15. 软件工程经济学 | 10.10, 10.1, 9.4 |
| 16. 计算基础 | 2.13, 3.3, 3.4 |
| 17. 数学基础 | 2.13, 11.3 |
| 18. 工程基础 | 2.13, 3.1 |

---

# 标准与框架

本附录是对全书所引用的真实标准、框架与法规的系统化索引。它是一份导航工具，而非合规手册：请务必查阅权威原始文本，并在相关情况下咨询合格的法律或审计顾问，以了解现行文本及其对您所处环境的适用性。

条目按领域分组。每条列出标准或框架的名称、发布机构、一句话概述其范围，以及与之最相关的章节或领域。名称如有常用缩写，则会标出该缩写。文件编号与标题仅在已被广泛确立的情况下给出；本附录不包含任何 URL。

## 如何使用本附录

- **法规（Regulations）**（例如 GDPR、HIPAA）在其管辖范围和行业内具有法律约束力。它们设定的是义务，而不仅仅是最佳实践建议。
- **标准（Standards）**（例如 ISO/IEC 27001、WCAG）是正式的、通常可供认证的规范。有些是自愿采用的，有些则由法律或合同强制要求。
- **框架（Frameworks）**（例如 NIST CSF、NIST AI RMF）是结构化的、通常为自愿采用的指导性文件，可根据自身风险状况进行裁剪。
- 适用性取决于管辖范围、行业、数据类型和合同条款。许多组织需要同时满足其中多项要求。

## 安全与隐私

| 标准 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | 信息安全管理体系（ISMS）的要求。 | 4.1–4.6 安全与合规 |
| ISO/IEC 27002 | ISO / IEC | 支持 ISO/IEC 27001 的指南与控制措施集合。 | 4.1–4.4 安全 |
| ISO/IEC 27017 / 27018 | ISO / IEC | 云专用安全控制（27017）以及云端个人身份信息（PII）保护（27018）。 | 4.3 基础设施与云安全；4.5 隐私 |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | 围绕治理、识别、保护、检测、响应、恢复六大职能组织的自愿性框架。 | 4.1, 4.4 安全基础与运维 |
| NIST SP 800-53 | National Institute of Standards and Technology | 面向信息系统的安全与隐私控制措施目录。 | 4.3, 4.6 云安全与合规 |
| NIST SP 800-63 | National Institute of Standards and Technology | 数字身份与身份验证保障指南。 | 4.2, 4.3 应用与基础设施安全 |
| OWASP Top Ten | Open Worldwide Application Security Project | 定期更新的最关键 Web 应用安全风险列表。 | 4.2 应用安全 |
| OWASP ASVS | Open Worldwide Application Security Project | 用于验证应用安全性的分级要求与测试项。 | 2.4, 4.2 测试与应用安全 |
| OWASP SAMM | Open Worldwide Application Security Project | 用于构建和评估软件安全计划的成熟度模型。 | 4.1 安全基础与文化 |
| STRIDE | Originated at Microsoft | 用于对威胁进行分类的威胁建模分类法。 | 4.2 应用安全 |
| MITRE ATT&CK | MITRE | 用于检测与防御的对手战术和技术知识库。 | 4.4 安全运维 |
| SLSA | Open Source Security Foundation (OpenSSF) | 用于保障软件供应链完整性与来源可追溯性的分级框架。 | 4.2, 8.1, 10.3 供应链与交付 |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | 软件物料清单（SBOM）的标准格式。 | 4.2, 10.3 应用安全与许可 |
| PCI DSS | PCI Security Standards Council | 处理支付卡数据的安全要求。 | 4.2, 4.5, 4.6 安全、隐私、合规 |

## 合规与政府监管

### 美国

| 法规 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | 受保护健康信息（PHI）的保障措施。 | 4.5, 4.6 隐私与合规 |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | 针对上市公司的财务报告与内部控制要求。 | 4.6, 10.2 合规与审计 |
| FISMA | US Congress | 联邦机构的信息安全计划要求。 | 4.3, 4.6 云安全与合规 |
| FedRAMP | US General Services Administration / FedRAMP PMO | 面向联邦机构所用云服务的标准化安全授权流程。 | 4.3, 4.6 云安全与合规 |
| NIST SP 800-171 | National Institute of Standards and Technology | 非联邦系统中受控非密信息（CUI）的保护。 | 4.6 合规（国防供应链） |
| CMMC | US Department of Defense | 针对国防承包商网络安全成熟度的认证。 | 4.6 合规（国防） |
| FIPS 140-3 | National Institute of Standards and Technology | 加密模块的安全要求。 | 4.3 基础设施与云安全 |
| CCPA / CPRA | State of California | 加利福尼亚州的消费者隐私权利与企业义务。 | 4.5 隐私与数据保护 |

### 欧盟与英国

| 法规 / 标准 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| GDPR | European Union | 关于个人数据处理的综合性法规。 | 4.5, 4.6 隐私与合规 |
| UK GDPR / Data Protection Act 2018 | United Kingdom | 英国脱欧后的数据保护制度。 | 4.5, 4.6 隐私与合规 |
| eIDAS | European Union | 电子身份识别与信任服务框架。 | 4.2, 4.3 安全 |
| NIS2 Directive | European Union | 针对关键实体和重要实体的网络安全义务。 | 4.4, 4.6 安全运维与合规 |
| DORA (Digital Operational Resilience Act) | European Union | 针对金融行业的运营韧性要求。 | 9.1, 10.2 可靠性与审计 |
| EU AI Act | European Union | 基于风险的人工智能系统监管法规（另见下文"人工智能治理"）。 | 6.1, 6.5 人工智能战略与负责任人工智能 |

## 无障碍

| 标准 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | 面向无障碍网页内容的指南，设有 A/AA/AAA 三级合规等级。 | 5.3 无障碍；5.1–5.6 用户体验与前端 |
| WAI-ARIA | World Wide Web Consortium (W3C) | 面向无障碍富互联网应用的角色、状态与属性规范。 | 5.3, 5.6 无障碍与前端 |
| Section 508 | US Access Board / US federal law | 美国联邦信息通信技术（ICT）的无障碍要求，与 WCAG 保持一致。 | 5.3 无障碍（美国政府） |
| EN 301 549 | ETSI / CEN / CENELEC | 欧洲信息通信技术采购的无障碍要求，与 WCAG 保持一致。 | 5.3 无障碍（欧盟公共部门） |
| ADA (Americans with Disabilities Act) | US Congress | 禁止残障歧视的民权法律，适用于数字服务。 | 5.3 无障碍 |
| ISO/IEC 40500 | ISO / IEC | WCAG 2.0 作为正式标准的国际采纳版本。 | 5.3 无障碍 |

## 人工智能治理

| 框架 / 法规 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | 用于治理、梳理、衡量和管理人工智能风险的自愿性框架。 | 6.1, 6.5 人工智能战略与负责任人工智能 |
| ISO/IEC 42001 | ISO / IEC | 人工智能管理体系（AIMS）的要求。 | 6.1, 6.5 人工智能治理 |
| ISO/IEC 23894 | ISO / IEC | 针对人工智能特定风险管理的指南。 | 6.5 负责任与可信人工智能 |
| EU AI Act | European Union | 针对人工智能系统提供者与部署者的分级法律义务。 | 6.1, 6.3, 6.5 人工智能应用与治理 |
| OECD AI Principles | Organisation for Economic Co-operation and Development | 面向可信人工智能的价值观原则，对政策制定具有广泛影响。 | 6.5, 10.5 负责任人工智能与伦理 |

## 质量与过程

| 标准 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | 软件产品质量模型（功能适用性、可靠性、安全性等）。 | 2.2, 2.4 设计与测试 |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | 软件生命周期过程。 | 1.4, 10.1 工作方式与项目群管理 |
| ISO 9001 | ISO | 通用质量管理体系的要求。 | 10.2 风险、审计与保障 |
| CMMI | ISACA / CMMI Institute | 用于过程能力与改进的成熟度模型。 | 10.1, 10.2 项目群管理与保障 |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | 面向软件团队的四项关键交付绩效指标。 | 8.1, 8.4, 9.1 交付、平台、可靠性 |
| SPACE framework | Microsoft / GitHub researchers | 用于衡量开发者生产力的多维度模型。 | 1.3, 8.4 成长与开发者体验 |
| ITIL | AXELOS / PeopleCert | IT 服务管理实践框架。 | 9.1, 9.3 可靠性与事件管理 |

## 架构

| 标准 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | 用于架构描述与视角的标准。 | 2.7, 3.1 文档与架构基础 |
| TOGAF | The Open Group | 企业架构框架与开发方法。 | 3.1, 10.1 架构与组合管理 |
| C4 model | Community (Simon Brown) | 用于可视化软件架构的四层次方法。 | 2.7, 3.1 文档与架构 |
| arc42 | Community (Starke / Hruschka) | 用于组织架构文档结构的模板。 | 2.7, 3.1 文档与架构 |
| ADRs | Community practice | 记录重大架构决策的轻量级方式。 | 1.5, 2.7, 3.1 决策制定与文档 |

## 云与 DevOps

| 标准 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | 基于共识制定的系统与云安全配置基线。 | 4.3, 8.2 基础设施安全与基础设施即代码（IaC） |
| CNCF landscape and projects | Cloud Native Computing Foundation | 云原生计算的生态系统与标准（例如 Kubernetes）。 | 8.3 容器与云原生 |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | 容器镜像与运行时格式的开放标准。 | 8.3 容器与云原生 |
| OpenTelemetry | Cloud Native Computing Foundation | 面向遥测数据（链路追踪、指标、日志）的厂商中立标准。 | 9.2 可观测性与监控 |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | 用于策略即代码的通用策略引擎。 | 4.6, 8.2, 8.3 合规、基础设施即代码、编排 |
| SRE practices | Google (widely adopted) | 基于 SLI/SLO/错误预算的可靠服务运维方法。 | 9.1 站点可靠性工程 |
| FinOps Framework | FinOps Foundation | 云财务管理与成本问责实践。 | 9.4 成本、可持续性、绿色软件 |

## 数据

| 标准 / 框架 | 发布机构 | 范围概述 | 主要章节 / 领域 |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | 组织数据管理各学科的知识体系。 | 7.1 数据战略与治理 |
| ISO/IEC 38505 | ISO / IEC | 将数据作为组织资产进行治理。 | 7.1 数据治理 |
| ISO 8000 | ISO | 数据质量与主数据标准。 | 7.1, 7.2 数据治理与工程 |
| Data mesh | Community (Zhamak Dehghani) | 以数据即产品为理念的去中心化、领域导向方法。 | 7.1, 7.2 数据战略与工程 |
| DCAM | EDM Council | 数据管理能力评估模型。 | 7.1 数据战略与治理 |

## 关于范围与变更的说明

标准与法规会不断演变。版本号（例如 WCAG 2.1 与 2.2 的区别，或 ISO 的修订年份）和控制措施目录会随时间变化，新的法律（例如针对特定行业的人工智能和韧性法规）也在不断出现。请将本附录视为一份起点地图：在依据任何条目做出合规或采购决策之前，请务必确认其现行版本、适用管辖范围及适用性。如果本指南正文章节与本附录在细节上存在差异，应始终以权威原始文件为准。


---

# 推荐阅读

本附录是一份精心编选并附有注解的阅读书目，涵盖本指南的各个领域。它更倾向于收录那些在大规模实践中真正塑造了行业做法的著作：公认的经典之作、严谨的参考资料，以及大型企业和政府团队据以衡量自身水平的标准与报告。

每条条目给出书名与作者，随后用一句话说明其重要性。本书目按本指南的十个部分进行组织。请有选择性地阅读：挑选与你当前痛点最相关的两三本书，而不必通读全部书架。如果某部著作横跨多个领域，则将其归入最能发挥作用的部分；许多著作其实适用于多个部分。

关于标准的说明：NIST、OWASP、W3C/WCAG、ISO 以及 DORA 项目组等机构发布的都是会定期修订的动态文件。请引用并阅读其现行版本；以下注解描述的是它们的长期意义与用途。

## 基础篇：文化、人才与过程

- **Accelerate: The Science of Lean Software and DevOps**。Nicole Forsgren、Jez Humble、Gene Kim 著。这项研究奠定了"交付绩效可预测组织绩效"这一论断的实证基础，并定义了用于衡量交付绩效的指标（即如今的 DORA 指标）。
- **The Phoenix Project**。Gene Kim、Kevin Behr、George Spafford 著。这部商业小说让流动、在制品和 DevOps"三步工作法"这些概念，对领导者和怀疑者而言都变得直观易懂。
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**。Matthew Skelton、Manuel Pais 著。提出了一套实用词汇（流对齐团队、平台团队、赋能团队、复杂子系统团队），用于设计能够产出优质软件的组织。
- **An Elegant Puzzle: Systems of Engineering Management**。Will Larson 著。提供了经过实践检验的框架，用于确定团队规模、管理组织增长，以及做出工程领导层反复面对的各类决策。
- **Staff Engineer: Leadership Beyond the Management Track**。Will Larson 著。定义了 Staff-plus 原型角色以及技术领导力路径，适合那些希望产生影响力而不必转做管理岗位的人。
- **The Manager's Path**。Camille Fournier 著。一份从技术负责人到高管的分阶段指南，是职业发展阶梯以及向管理岗位过渡的基础参考。
- **The Staff Engineer's Path**。Tanya Reilly 著。是 Staff-plus 相关文献的又一佳作，聚焦技术领导力、影响力以及在没有正式权威的情况下引导方向的日常工作。
- **Peopleware: Productive Projects and Teams**。Tom DeMarco、Timothy Lister 著。提出了一个历久弥新的论点：软件的核心问题是社会性的，而非技术性的。
- **The Mythical Man-Month**。Frederick P. Brooks Jr. 著。布鲁克斯定律的出处，以及至今仍影响人员配置和排期的"本质复杂性与偶然复杂性"这一区分的来源。
- **The Fearless Organization: Creating Psychological Safety in the Workplace**。Amy C. Edmondson 著。为无责文化以及使人们能够从失败中学习的心理安全感，提供了研究基础。
- **Thinking, Fast and Slow**。Daniel Kahneman 著。关于认知偏差最权威的论述，对结构化面试、校准以及诚实的决策制定都至关重要。

## 编程技艺与代码质量

- **The Pragmatic Programmer: Your Journey to Mastery**。Andrew Hunt、David Thomas 著。奠定了专业习惯（DRY 原则、正交性、示踪弹等）的基础性目录，界定了何谓工匠精神。
- **Refactoring: Improving the Design of Existing Code**。Martin Fowler 著。行为保持型代码变换的经典目录，也是持续、由测试保驾护航的代码改进这一实践的开山之作。
- **Clean Code: A Handbook of Agile Software Craftsmanship**。Robert C. Martin 著。一部被广泛使用（也颇具争议）的标准读物，涉及命名、函数与可读性，塑造了许多团队的评审预期。
- **Code Complete**。Steve McConnell 著。一部全面、有实证依据的构建实践手册，至今仍是编程质量的扎实基础读物。
- **Test-Driven Development: By Example**。Kent Beck 著。红-绿-重构循环与测试先行设计理念最原始、最实操的入门之作。
- **Working Effectively with Legacy Code**。Michael Feathers 著。为没有测试覆盖的代码添加测试并安全修改它的权威工具书，对长期维护的系统不可或缺。
- **Growing Object-Oriented Software, Guided by Tests**。Steve Freeman、Nat Pryce 著。通过一个完整实例展示了由外而内的 TDD、模拟（mocking）以及通过测试演进设计的方法。
- **A Philosophy of Software Design**。John Ousterhout 著。对复杂性、深层模块和信息隐藏进行了犀利而鲜明的论述，对部分"整洁代码"正统观点提出了富有建设性的挑战。

## 架构与系统

- **Designing Data-Intensive Applications**。Martin Kleppmann 著。关于存储、复制、分区、一致性和流处理在大规模场景下权衡取舍的当代最佳参考书。
- **Fundamentals of Software Architecture: An Engineering Approach**。Mark Richards、Neal Ford 著。对架构风格、架构特性以及架构师角色与决策方式进行了广泛而与时俱进的综述。
- **Software Architecture: The Hard Parts**。Neal Ford、Mark Richards、Pramod Sadalage、Zhamak Dehghani 著。以决策为核心，探讨分布式架构权衡、服务粒度与数据归属等问题。
- **Building Evolutionary Architectures**。Neal Ford、Rebecca Parsons、Patrick Kua 著。引入了适应度函数（fitness function）的概念，以及能够随时间安全演进的架构理念。
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**。Eric Evans 著。限界上下文、统一语言、聚合等概念的源头，构成了现代服务设计的词汇体系。
- **Building Microservices: Designing Fine-Grained Systems**。Sam Newman 著。关于服务拆分、服务边界、部署以及微服务对组织所带来影响的权威参考。
- **Monolith to Microservices**。Sam Newman 著。一份增量式拆分的模式目录，例如绞杀者模式和抽象分支法，帮助团队避免高风险的一次性重写。
- **Patterns of Enterprise Application Architecture**。Martin Fowler 著。命名模式的参考书（仓储模式、工作单元模式等），为企业系统提供了共同的语言。
- **Enterprise Integration Patterns**。Gregor Hohpe、Bobby Woolf 著。事件驱动与异步架构背后消息传递模式的权威目录。
- **Release It! Design and Deploy Production-Ready Software**。Michael T. Nygard 著。断路器、舱壁隔离等稳定性模式的出处，服务于能够承受真实生产环境考验的系统。
- **Design Patterns: Elements of Reusable Object-Oriented Software**。Erich Gamma、Richard Helm、Ralph Johnson、John Vlissides（"四人帮"）著。历史性的面向对象模式目录，塑造了共同的设计词汇。

## 安全、隐私与信任

- **Threat Modeling: Designing for Security**。Adam Shostack 著。一部实用而全面的指南，介绍 STRIDE 以及作为常规工程实践的结构化威胁建模。
- **Security Engineering: A Guide to Building Dependable Distributed Systems**。Ross Anderson 著。一部百科全书式的参考书，讲述真实系统如何失效，以及如何构建能够抵御攻击的系统。
- **The Tangled Web: A Guide to Securing Modern Web Applications**。Michal Zalewski 著。对浏览器安全模型进行了严谨的梳理，揭示了 Web 平台如何以微妙的方式背离天真的假设。
- **Cryptography Engineering**。Niels Ferguson、Bruce Schneier、Tadayoshi Kohno 著。一本从业者指南，教你正确使用密码学并避免常见而危险的错误。
- **Building Secure and Reliable Systems**。Heather Adkins 等（Google）著。谷歌对安全性与可靠性作为相互交织、从一开始就应纳入设计的属性所做的系统总结。
- **Zero Trust Networks**。Evan Gilman、Doug Barth 著。清晰阐述了"永不信任、始终验证"网络架构的原则与实现机制。
- **OWASP Top 10**。OWASP Foundation 著。全球政策与审计广泛引用的、最关键 Web 应用安全风险的共识基线。
- **OWASP Application Security Verification Standard (ASVS)**。OWASP Foundation 著。一份分级、可测试的安全需求清单，适合用于合同和验收标准。
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**。NIST 著。美国联邦安全体系的核心控制目录，也是 FedRAMP 和 FISMA 授权的基础。
- **NIST Cybersecurity Framework (CSF)**。NIST 著。被广泛采用的"识别-保护-检测-响应-恢复"结构，用于组织安全计划。
- **NIST SP 800-207: Zero Trust Architecture**。NIST 著。大多数企业和政府零信任项目所依据的权威定义与参考架构。

## 用户体验、界面与产品设计

- **The Design of Everyday Things**。Don Norman 著。关于可供性、意符、反馈与以人为中心的设计的奠基性著作，其适用范围远超实体物品。
- **Don't Make Me Think, Revisited**。Steve Krug 著。为不言自明的可用性以及低成本、高频次可用性测试的价值，提供了简明而历久弥新的论证。
- **About Face: The Essentials of Interaction Design**。Alan Cooper、Robert Reimann、David Cronin 著。关于交互设计、人物画像（persona）与目标导向设计的全面参考。
- **Design Systems: A Practical Guide**。Alla Kholmatova 著。扎实地阐述了如何构建一致、可复用的组件体系及其背后的共同语言。
- **Refactoring UI**。Adam Wathan、Steve Schoger 著。一份实用且以实例驱动的视觉打磨指南，适合没有受过正式训练却要设计界面的工程师。
- **Letting Go of the Words: Writing Web Content that Works**。Ginny Redish 著。关于简明语言、以任务为中心的内容设计的权威指南。
- **Inclusive Design Patterns / Accessibility for Everyone**。Heydon Pickering 著；Laura Kalbag 著。构建能够服务全部人类能力范围的界面的实用伴读读物。
- **A Web for Everyone: Designing Accessible User Experiences**。Sarah Horton、Whitney Quesenbery 著。在无障碍标准与优秀用户体验之间架起了一座以原则为导向的桥梁。
- **Web Content Accessibility Guidelines (WCAG) 2.2**。W3C 著。国际公认的标准（可感知、可操作、可理解、健壮），是大多数无障碍法律的依据。
- **U.S. Web Design System (USWDS)**。U.S. government 著。一个可运行的实例，展示了如何为大规模公共服务构建无障碍、基于标准的设计系统。

## 人工智能与机器学习

- **Designing Machine Learning Systems**。Chip Huyen 著。构建端到端生产级机器学习系统（数据、特征、部署与监控）的领先实用指南。
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**。Cathy Chen 等著。将 SRE 学科（SLO、监控、事件响应）扩展应用到机器学习系统。
- **Deep Learning**。Ian Goodfellow、Yoshua Bengio、Aaron Courville 著。关于现代神经网络背后理论与方法的标准学术参考书。
- **AI Engineering: Building Applications with Foundation Models**。Chip Huyen 著。一份关于如何设计、评估和运营基于大型基础模型的应用的最新指南。
- **Weapons of Math Destruction**。Cathy O'Neil 著。有力论证了算法问责的必要性，揭示了未经审视的模型所带来的现实危害，对公共部门的人工智能应用尤为重要。
- **Interpretable Machine Learning**。Christoph Molnar 著。一份全面且可免费获取的参考资料，介绍模型及其预测结果的可解释性方法。
- **NIST AI Risk Management Framework (AI RMF 1.0)**。NIST 著。用于治理、梳理、衡量和管理人工智能风险的权威框架，在政策与采购中被日益频繁地引用。

## 数据、分析与洞察

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**。Ralph Kimball、Margy Ross 著。关于星型模式和维度建模的分析领域经典参考书。
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**。Ron Kohavi、Diane Tang、Ya Xu 著。关于如何在大规模场景下开展可靠、可产生可行动结论的实验的权威指南。
- **Fundamentals of Data Engineering**。Joe Reis、Matt Housley 著。对现代数据生命周期及其背后工程实践的厂商中立式全景梳理。
- **Data Mesh: Delivering Data-Driven Value at Scale**。Zhamak Dehghani 著。以领域为导向、以产品为中心的大规模数据组织方法的奠基之作。
- **Storytelling with Data**。Cole Nussbaumer Knaflic 著。关于诚实、清晰的数据可视化及向决策者传达洞察的实用指南。
- **The Visual Display of Quantitative Information**。Edward R. Tufte 著。关于图形完整性、数据墨水比以及诚实呈现数据之伦理的奠基性著作。
- **DAMA-DMBOK: Data Management Body of Knowledge**。DAMA International 著。数据治理、数据管理、数据质量与数据编目的全面参考框架。
- **The Book of Why**。Judea Pearl、Dana Mackenzie 著。一部通俗易懂的因果推断入门读物，对于从相关性迈向可辩护的决策至关重要。

## 自动化、DevOps 与平台工程

- **The DevOps Handbook**。Gene Kim、Jez Humble、Patrick Debois、John Willis 著。将"三步工作法"转化为流动、反馈与持续学习具体实践的全面手册。
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**。Jez Humble、David Farley 著。关于部署流水线、自动化以及安全、频繁地发布软件的奠基性著作。
- **Infrastructure as Code: Managing Servers in the Cloud**。Kief Morris 著。关于将基础设施当作软件对待（模块化、测试、不可变性与漂移管理）的权威参考。
- **Team Topologies**。Matthew Skelton、Manuel Pais 著（见"基础篇"）。在塑造平台团队及其所提供的开发者体验方面，同样是本领域不可或缺的著作。
- **Kubernetes Patterns**。Bilgin Ibryam、Roland Huß 著。在 Kubernetes 上设计云原生应用的可复用模式目录。
- **Software Engineering at Google**。Titus Winters、Tom Manshreck、Hyrum Wright 著。阐述了测试、评审、工具与依赖管理等工程实践如何在数十年间扩展到数万名工程师的规模。
- **The Twelve-Factor App**。Adam Wiggins（Heroku）著。构建可移植、可扩展、云原生服务的简明而有影响力的宣言。
- **DORA State of DevOps Report**。DORA / Google Cloud（年度报告）著。支撑四项关键交付指标及驱动绩效表现的各项能力的持续研究项目。

## 运维、可靠性与可观测性

- **Site Reliability Engineering: How Google Runs Production Systems**。Betsy Beyer、Chris Jones、Jennifer Petoff、Niall Richard Murphy（编）著。定义 SLI、SLO、错误预算以及工程化可靠性这一学科的奠基性著作。
- **The Site Reliability Workbook**。Betsy Beyer 等（编）著。配套的实操手册，提供实践案例、已完成的 SLO 范例以及落地实施指南。
- **Observability Engineering**。Charity Majors、Liz Fong-Jones、George Miranda 著。对可观测性、高基数数据以及调试生产环境中"未知的未知"问题的现代定义。
- **Implementing Service Level Objectives**。Alex Hidalgo 著。一份全面、实用的指南，介绍如何妥善设计、衡量和运用 SLO 与错误预算。
- **Release It!**。Michael T. Nygard 著（见"架构与系统"）。在生产稳定性模式和运行具备韧性的系统方面，同样是本领域的基础性著作。
- **The Art of Capacity Planning**。Arun Kejariwal、John Allspaw 著。一种数据驱动的方法，用于预测需求并为持续增长的系统规划容量。
- **Chaos Engineering: System Resiliency in Practice**。Casey Rosenthal、Nora Jones 著。关于主动注入故障以建立系统韧性信心这一做法的权威论述。
- **Google SRE Book, Chapter on Postmortems**。Google 著。被广泛效仿的无责事后总结模型，以及从事件中学习的方法。

## 企业、政府与公共利益

- **Working in Public: The Making and Maintenance of Open Source Software**。Nadia Eghbal 著。关于开源软件究竟如何被维系下去的重要研究，揭示了企业所依赖的各类依赖项背后维护者所承受的负担。
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**。Jennifer Pahlka 著。清醒地剖析了公共部门技术为何屡屡失败，以及以交付为导向的改革如何加以修复。
- **Digital Transformation at Scale: Why the Strategy Is Delivery**。Andrew Greenway 等著。来自英国政府数字服务局（UK Government Digital Service）的经验总结：通过交付而非仅仅规划来转型公共服务。
- **Project to Product**。Mik Kersten 著。介绍了"流动框架"（Flow Framework），用以推动大型企业从项目制资助转向持久的产品价值流。
- **Escaping the Build Trap**。Melissa Perri 著。讲述了组织如何误将产出当作成果，以及产品管理如何纠正这一误区，对组合与项目群治理具有直接意义。
- **U.S. Digital Services Playbook**。U.S. Digital Service 著。一套简明的行动方案，用于交付高效、以用户为中心的政府数字服务。
- **GOV.UK Service Manual and Service Standard**。UK Government Digital Service 著。一份可运行、已发布的标准，用于构建优质公共服务，被其他多国政府广泛效仿。
- **NIST SP 800-37: Risk Management Framework**。NIST 著。美国联邦系统中"运行授权"（ATO）及持续监控背后的过程框架。
- **The FinOps Foundation Framework**。FinOps Foundation 著。用于财务与工程团队之间云成本可见性、优化与问责的参考模型。

## 如何使用本书目

- **从你的痛点入手。** 如果部署缓慢且令人提心吊胆，请先阅读《Accelerate》《Continuous Delivery》以及 *DORA* 报告，再去看其他内容。
- **为未来十年而读，而非只为当前这个冲刺。** 优先选择那些阐述持久原则的著作，而不是与特定工具版本绑定的内容。
- **核实标准的现行版本。** NIST、OWASP、WCAG、ISO 和 DORA 会不断修订各自的出版物；请始终以最新版本为准，并在自己的政策中注明版本号。
- **打造一个共同的书架。** 一个团队如果共同读过其中两三本书，争论会更少、决策会更快，因为大家共享着同一套词汇和参照系。
- **另见第 12.5 章**，其中提供了参考标准与框架的完整索引；以及**第 12.6 章**，其中介绍了如何为本书目所述实践的落地采纳排定顺序。
