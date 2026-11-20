# 12.1 术语表

本术语表定义了本指南通篇使用的术语和缩略语。词条按字母顺序分组。若某词条有常用缩略语，将以括号形式标出。定义力求简明；如需更完整的说明，请参阅相关章节。

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**：一种授权模型，根据对用户、资源、操作和环境所评估的属性（例如部门、密级、一天中的时间）来授予访问权限，而非固定角色。它提供细粒度、策略驱动的控制，但复杂度高于 RBAC。

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**：一种设计和构建软件的实践，使残障人士能够感知、理解、浏览软件并与之交互。数字缩写 "a11y" 代表 "a" 和 "y" 之间的 11 个字母。

**ADR (Architecture Decision Record)**：一份简短、带版本号的文档，用于记录单个重大架构或技术决策及其背景、所考虑的方案与后果。ADR 为系统为何如此设计留下了持久、可审阅的历史记录。

**Aggregate**：在 Domain-Driven Design 中，指一组被视为单一数据变更单元的领域对象集合，其中一个实体作为聚合根（aggregate root）负责维护不变量。聚合定义了一致性边界和事务边界。

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**：一份明确的契约，一个软件通过它向另一个软件请求服务或数据。设计良好的 API 隐藏实现细节，并提供稳定的、带版本管理的接口。

**API-first**：一种开发方法，先设计并商定 API 契约，再进行实现，使消费方和提供方可以依据共享规范并行开发。

**arc42**：一种开放的、基于模板的软件架构文档结构，分为十二个部分，涵盖背景、约束、构建块、运行时、部署和决策等内容。

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**：W3C 的一项规范，定义了角色、状态和属性，使动态及自定义的网页组件能够被屏幕阅读器等辅助技术理解。

**ASR (Architecturally Significant Requirement)**：对架构具有可衡量、影响广泛的需求，例如性能、可用性、安全性或合规性方面的约束。ASR 驱动着最具影响力的设计决策。

**ASVS (Application Security Verification Standard)**：OWASP 的一项标准，为设计、构建和验证安全应用程序提供分级的安全需求与测试清单。

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**：根据负载自动调整运行中的计算实例数量（或规格），使容量能够无需人工干预即可跟随需求变化。它是对审慎容量规划的补充，而非替代。

**[Availability](https://en.wikipedia.org/wiki/Availability)**：系统处于可运行状态并能够处理请求的时间比例，通常以"几个九"表示（例如 99.9%）。它是 SLO 和 SLA 中明确规定的核心可靠性目标。

## B

**Backpressure**：一种流量控制机制：处于高负载下的组件向上游生产者发出信号使其减速，从而防止队列无限增长和级联故障。它是可靠的流式处理和消息驱动系统的核心机制。

**[BDD (Behavior-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**：一种协作实践，以具体、易读的行为示例（通常采用 Given/When/Then 形式）表达需求，这些示例同时也可用作自动化验收测试。

**BFF (Backend for Frontend)**：一种架构模式，为特定前端或客户端类型构建专用的后端服务，根据该客户端的需求定制数据整形和聚合方式。

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**：用于收集、整合和分析业务数据以支持报表、仪表盘和决策的工具、流程与实践。

**Blameless postmortem**：一种事后总结（postmortem）方式，其前提是人们在当时所掌握的信息和激励条件下都会采取合理行动，因此评审重点在于系统性原因和经验教训，而非追究个人过失。

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**：一种发布策略，同时运行两套相同的生产环境（"蓝色"和"绿色"），将流量路由到其中一套，同时对另一套进行更新，从而实现近乎即时的切换和回滚。

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**：一种广泛使用的全文检索排序函数，利用词频、逆文档频率和文档长度来衡量文档与查询的匹配程度。它是许多搜索引擎中默认的词汇排序方法。

**Bounded context**：在 Domain-Driven Design 中，指一个明确的边界，在该边界内特定的领域模型及其统一语言（ubiquitous language）保持一致适用。它可以防止大型系统不同部分之间的概念相互混淆。

**Build cache**：一种存储先前构建产物的机制，以产生该产物的输入作为键，使未变更的工作可以被复用而无需重新构建。共享的远程构建缓存能让整个团队及其 CI 相互复用彼此的构建结果。

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**：指需要失去多少人（比喻为"被公交车撞到"）才会因缺乏关键知识而使项目陷入停滞的人数。较低的"巴士系数"表明专业知识过度集中且缺乏文档记录，存在组织风险。

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**：缓存在容量已满时用于决定移除哪个条目的规则，例如最近最少使用（LRU）或最不经常使用（LFU）。该策略决定了命中率，进而决定了缓存的价值。

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**：在底层数据源发生变化后移除或更新缓存数据、以避免读取方看到过期值的问题。它是计算机科学中著名的难题之一。

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**：一种故障模式：大量客户端同时对同一个键发生缓存未命中，并同时请求源站，从而使源站不堪重负。请求合并（request coalescing）和错峰过期可以防止这种情况发生，也称为"惊群效应"（thundering herd）。

**Canary release**：一种部署技术，先将新版本发布给一小部分用户或流量，监测是否出现问题，若各项指标保持正常，再逐步扩大发布范围。

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**：该原理指出，分布式数据存储最多只能同时保证一致性（Consistency）、可用性（Availability）和分区容错性（Partition tolerance）三者中的两项；由于网络分区不可避免，设计者实际上是在分区发生期间于一致性和可用性之间做权衡。

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**：一种轻量级的软件架构可视化方法，包含四个抽象层级：系统上下文（System Context）、容器（Containers）、组件（Components）和代码（Code）。

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**：持续交付（Continuous Delivery）使软件始终保持可发布状态，从而可以在获得人工批准后随时部署；持续部署（Continuous Deployment）则会自动发布每一项通过流水线的变更。

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**：由地理位置分散的边缘服务器组成的网络，在靠近用户的位置缓存并提供内容，从而降低延迟并减轻源站基础设施的负担。

**Chain-of-thought prompting**：一种提示技术，要求语言模型在给出最终答案之前先逐步完成中间推理步骤，从而提升在多步骤问题上的表现，但代价是输出更长、速度更慢。

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**：一种实践，指频繁地将开发者的变更合并到共享主干中，每次合并都由自动化构建和测试套件进行验证，以尽早发现集成问题。

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**：持续集成与持续交付/部署相结合的流水线，实现软件构建、测试和发布的自动化。

**CMMC (Cybersecurity Maturity Model Certification)**：美国国防部的一项认证计划，用于评估处理联邦合同信息和受控非密信息的承包商的网络安全成熟度。

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**：模块内部各元素彼此关联、共同服务于单一明确目的的程度。高内聚与低耦合相结合，是可维护设计的标志。

**Context window**：语言模型一次能够处理的最大文本量，以 token 计量，涵盖输入和输出。这是一种稀缺资源，提示词和上下文设计必须审慎管理。

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)**：该观察指出，系统的结构往往会映射出构建该系统的组织的沟通结构。"逆康威调动"（inverse Conway manoeuvre）则是有意塑造团队结构，以产生期望的架构。

**Core Web Vitals**：由 Google 定义的一组以用户为中心的网页性能指标（例如最大内容绘制 Largest Contentful Paint、下一次交互延迟 Interaction to Next Paint 和累积布局偏移 Cumulative Layout Shift），用于衡量加载速度、交互性和视觉稳定性。

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)**：尚未完成某项工作所带来的经济成本，以单位时间损失的价值来表示。将其明确量化能把优先级排序从主观判断变为算术计算，也是加权最短作业优先（WSJF）等排序规则的基础。

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**：模块或服务之间相互依赖的程度。松耦合能限制变更带来的连锁影响，是优秀架构的核心目标之一。

**CQRS (Command Query Responsibility Segregation)**：一种模式，将用于改变状态的模型（命令）与用于读取状态的模型（查询）分离，使两者可以独立进行优化和扩展。

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**：一份公开的已披露安全漏洞目录，每个漏洞都被赋予唯一标识符，使工具和团队能够明确无误地引用同一个缺陷。

**CWV**：参见 Core Web Vitals。

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**：一种安全测试方式，在无法访问源代码的情况下从外部探测正在运行的应用程序，以发现运行时才会出现的漏洞。

**Data-ink ratio**：由 Edward Tufte 提出的一项原则，主张图表应将大部分"墨水"用于数据本身，尽量减少装饰性元素，去除无助于传达信息的网格线、边框和图表垃圾（chartjunk）。

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**：一种去中心化的数据架构与运营模式，将数据视为由各领域团队拥有的产品，并由自助式平台基础设施和联邦式治理提供支撑。

**[Data visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization)**：以位置、长度、颜色等视觉形式对数据进行编码的实践，使规律、对比和趋势变得可感知，从而支持更明智的决策。

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**：一种软件设计方法，以业务领域为核心构建模型，使用共享的统一语言、限界上下文（bounded context）以及实体、值对象、聚合等构建块。

**Design tokens**：带有命名的、与平台无关的取值（如颜色、间距、排版等），用于编码设计决策，使其能够在设计系统和多个产品之间保持一致地共享。

**DevEx / DevX (Developer Experience)**：开发者日常与工具、平台和流程交互的整体质量，涵盖摩擦程度、反馈速度和认知负荷等方面。

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**：一种文化与实践的集合，将软件开发与运维结合起来，通过自动化和共同承担责任来缩短交付周期、提高部署频率并改善可靠性。

**DORA (DevOps Research and Assessment)**：一项研究计划及其广泛使用的四项交付指标（部署频率、变更前置时间、变更失败率和服务恢复时间），用于衡量软件交付绩效。

**DPIA (Data Protection Impact Assessment)**：一种结构化评估，GDPR 要求对高风险数据处理活动进行此类评估，在项目推进之前识别并降低隐私风险。

**Drift (configuration)**：系统的实际状态逐渐偏离其声明或预期状态，通常由人工变更所致；IaC 和 GitOps 旨在检测并纠正这种漂移。

**Drift (model)**：在机器学习中，指随着输入数据的统计特性（数据漂移）或所建模的关系（概念漂移）发生变化，模型性能随时间下降的现象。

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**：在发生重大中断事件后恢复服务和数据的策略、流程和基础设施，通常以 RTO 和 RPO 目标为准绳。

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**：一项设计原则，主张每一份知识都应只有一个权威的表达形式，以减少重复并降低更新不一致的风险。

## E

**East-west traffic**：系统或数据中心内部服务之间的网络流量，与系统和外部客户端之间的南北向流量相对。服务网格通常用于管理东西向流量。

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**：在数据产生或使用的位置附近而非集中式位置运行计算和存储，以降低延迟并节省带宽。内容分发网络是这一理念早期且广泛应用的形式。

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**：系统根据需求变化自动获取和释放资源的能力，使容量能够紧密跟随负载变化。

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**：一种数据集成模式，先将原始数据加载到目标存储中，再在其中进行转换，从而利用现代数据仓库和湖仓一体（lakehouse）架构的规模优势。

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**：将文本、图像或其他数据表示为稠密数值向量的方式，使相似的项目在向量空间中彼此靠近。嵌入（embedding）是语义搜索、向量搜索和检索增强生成的基础。

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**：欧洲标准，规定了信息通信技术（ICT）产品和服务的无障碍要求，在欧盟公共部门采购中被广泛引用，并与 WCAG 保持一致。

**Error budget**：SLO 在一段时期内所允许的不可靠性额度；一旦耗尽，团队就需要优先处理可靠性工作而非新功能开发。它调和了开发速度与系统稳定性之间的张力。

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**：一种数据集成模式，从数据源中提取数据，将其转换为目标形态，再加载到诸如数据仓库之类的目的地。

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**：欧盟法规，按风险等级对人工智能系统进行分类并据此施加相应义务，禁止某些用途，并对高风险系统实施严格监管。

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**：分布式系统中的一种一致性模型，各副本可能暂时出现分歧，但在更新停止传播后会收敛到相同状态。

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**：一种在运行时启用或禁用功能而无需重新部署的机制，用于灰度发布、实验和运维控制。

**Feature store**：一种集中式系统，用于定义、存储并一致地提供经过整理的机器学习特征，供训练和推理共同使用，从而减少重复并避免训练与推理之间的偏差（training/serving skew）。

**[FedRAMP (Federal Risk and Authorization Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**：美国政府的一项计划，为联邦机构所使用的云服务制定统一的安全评估、授权和持续监控标准。

**Few-shot prompting**：在提示词中向语言模型提供少量示例，以演示所期望的任务和输出格式，与不提供任何示例、仅给出指令的零样本提示（zero-shot prompting）相对。

**FinOps**：一种学科和文化实践，为可变的云支出引入财务问责机制，使工程、财务和业务团队共同承担成本和价值的责任。

**[FISMA (Federal Information Security Modernization Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**：美国立法，要求联邦机构实施、记录并监控信息安全计划，主要通过 NIST 的指南加以落实。

**Flow efficiency**：工作项处于实际处理状态（而非等待状态）的时间占总前置时间的比例，计算方式为增值时间除以总前置时间。大多数系统的流动效率出人意料地低，通常不足 15%。

**Four-eyes principle**：一项控制措施，要求重大操作至少由两人审核或批准，以降低出错或舞弊的可能性。

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**：一种自动化测试技术，向程序输入畸形、随机或意外的数据，以发现崩溃、安全缺陷和边界情况下的缺陷。

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**：欧盟规范个人数据处理的法规，赋予个人相应权利，并对数据控制者和处理者施加义务，违规将面临严厉处罚。

**GitOps**：一种运维模式，将 Git 作为声明式基础设施和应用程序的唯一可信来源，通过自动化持续地使运行中的系统与已提交的状态保持一致。

**Golden path / paved road**：组织内部一条得到良好支持、带有明确倾向性的默认软件构建和发布路径，旨在使安全、合规、可靠的选择成为最容易做出的选择。

**Golden record**：在主数据管理中，指通过匹配和存续（survivorship）规则从多个源系统整合而成的、关于某个业务实体（如客户）的单一、经过协调的权威版本。

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)**：一种类型系统方案，使静态类型和动态类型能够在同一代码库中共存，从而可以为动态类型程序逐步添加类型。类型提示（type hint）和可选的类型检查器是常见的例子。

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**：一种面向 API 的查询语言和运行时，借助强类型的模式（schema），使客户端能够在一次调用中精确获取所需的数据。

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**：一种高性能、契约优先的远程过程调用框架，使用 HTTP/2，并通常配合 Protocol Buffers，实现高效的服务间通信。

## H

**Hermetic build**：一种仅依赖显式声明的输入、与宿主环境隔离的构建方式，从而无论在何处执行都能产生相同的结果。这种"密闭性"（hermeticity）是可复现构建和可靠缓存的基础。

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**：一种防篡改的硬件设备，用于生成、存储和使用加密密钥，比纯软件方案提供更强的密钥保护。

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**：美国立法，其内容之一是规定了保护受保护健康信息（PHI）的要求，并对其使用和披露进行规范。

**Horizontal scaling**：通过增加更多实例或节点（即"横向扩展"）而非增强单个节点性能来提升容量的方式。它是大多数大规模、具备弹性的架构的基础。

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**：通过机器可读、受版本控制的配置来定义和供给基础设施，而非通过人工流程，从而实现可重复性和可审阅性的实践。

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**：一套政策和技术框架，确保正确的身份在正确的时间获得对正确资源的正确访问权限。

**IDP / IdP**："IDP" 通常指内部开发者平台（Internal Developer Platform），即为产品团队抽象基础设施的自助式工具层；"IdP" 则指身份提供方（Identity Provider），即负责验证用户身份并签发断言的服务。二者需根据上下文加以区分。

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**：一种特性，指多次执行某项操作与仅执行一次的效果相同，这对于分布式系统和 API 中的安全重试至关重要。

**[i18n (Internationalization)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**：设计和构建软件，使其能够适配不同的语言、地区和文化习惯，而无需进行工程改动。数字缩写 "i18n" 代表 "i" 和 "n" 之间的 18 个字母。

**Immutable artefact**：一种构建产物，一旦生成并赋予版本号后就永不修改；任何变更都会产生一个新版本。不可变性使发布可复现，并支持"构建一次、跨环境晋级同一产物"。

**InnerSource**：在单一组织内部应用开源开发实践（透明性、共享代码仓库和跨团队贡献）的做法。

**IaC drift**：参见 Drift (configuration)。

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)**：搜索引擎的核心数据结构，将每个词映射到包含该词的文档列表，从而无需扫描全部文档即可回答查询。

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**：国际标准，规定了信息安全管理体系（ISMS）的要求，为管理信息安全风险提供了可认证的框架。

**ISO/IEC 42001**：国际标准，规定了人工智能管理体系的要求，为组织负责任地治理人工智能的开发和使用提供了可认证的框架。

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**：一种紧凑的、经过签名（可选加密）的令牌格式，用于在各方之间传递声明（claim），常用于 Web 和 API 系统中的身份验证和授权。

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**：一种精益工作流方法，在看板上将工作可视化，限制在制品数量，并管理流动过程，以提升吞吐量和可预测性。

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**：一项设计原则，倾向于选择能满足需求的最简单方案，理由是不必要的复杂性会增加成本和风险。

**KMS (Key Management Service)**：用于创建、存储、轮换加密密钥并控制其访问权限的系统，通常由硬件安全模块作为支撑。

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**：一种可量化的度量指标，用于跟踪实现特定业务或运营目标的进展情况。

## L

**Lakehouse**：一种数据架构，将数据湖低成本、灵活的存储特性与数据仓库的管理能力、事务支持和性能特性相结合。

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)**：从提出（或提交）某项变更到该变更交付至生产环境所经过的时间；是 DORA 的核心交付指标之一。

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**：一项安全原则，仅授予每个用户、进程或系统执行其功能所需的最小访问权限，以限制因入侵或错误而造成的损害。

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)**：排队论中的一个结论，指出稳定系统中的平均项目数等于平均到达速率乘以每个项目在系统中停留的平均时间。它将在制品数量、吞吐量和前置时间联系了起来。

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**：一种在超大规模文本语料上训练的机器学习模型，用于预测和生成语言，能够完成摘要、翻译和代码生成等任务。

**[l10n (Localization)](https://en.wikipedia.org/wiki/Language_localisation)**：将已国际化的软件适配到特定区域设置的过程，包括翻译、格式和文化习惯等方面。数字缩写 "l10n" 代表 "l" 和 "n" 之间的 10 个字母。

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**：用于在各系统之间创建和维护核心业务实体（如客户或产品）的单一、权威、一致视图的学科和工具体系。

**MITRE ATT&CK**：一个经过整理的公开知识库，收录真实世界中的攻击者战术和技术，被广泛用于规划红队演习、指导检测工程建设，并以共同的词汇描述威胁。

**Mean Time to Recovery (MTTR)**：故障发生后恢复服务所需的平均时间；是常见的可靠性和事件管理指标。

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**：一种实践，整个团队在同一台电脑上共同完成同一项任务，轮流担任打字者，以共享知识并集体做出决策。

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**：一套将 DevOps 理念延伸至机器学习生命周期的实践，用于可靠、高效地在生产环境中部署、监控和维护机器学习模型。

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**：一个存放多个项目乃至整个组织代码的单一版本控制仓库，能够实现工具共享和跨项目的原子化变更，但代价是需要专门的扩展工具来支撑。

**mTLS (mutual TLS)**：一种传输层安全（TLS）配置，通信双方都出示并验证证书，从而实现双向身份认证。它是服务网格和零信任网络中服务间通信的默认配置。另请参阅[双向身份验证](https://en.wikipedia.org/wiki/Mutual_authentication)。

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**：一种技术，故意向代码中引入微小缺陷（"变异体"），以检验测试套件能否发现它们，从而衡量测试套件的真实有效性。

## N

**[NDCG (Normalized Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**：一种衡量排序质量的指标，对将高度相关的结果排在列表靠前位置给予奖励，并经过归一化处理使不同查询之间的分数具有可比性。它是搜索相关性评估中的常用指标。

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**：美国联邦机构，其特别出版物（Special Publications）和框架是网络安全、隐私和人工智能领域广泛引用的标准。

**NIST AI RMF (AI Risk Management Framework)**：NIST 的一项自愿性框架，用于在人工智能系统的整个生命周期中识别、评估和管理相关风险，围绕治理（Govern）、映射（Map）、度量（Measure）和管理（Manage）四项职能组织。

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**：NIST 制定的联邦信息系统安全与隐私控制目录，其应用范围远超政府部门，被广泛用作基线标准。

**NIST SP 800-171**：NIST 的一份出版物，规定了在非联邦系统中保护受控非密信息（CUI）的要求，是国防承包商合规的核心依据。

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**：描述系统应如何表现（如性能、安全性、可靠性或可用性等质量属性）而非系统执行何种功能的需求。

**North-south traffic**：系统与其外部客户端之间进出数据中心或集群的网络流量，与内部服务之间的东西向流量相对。API 网关通常用于管理南北向流量。

## O

**Observability**：系统内部状态能够通过其外部输出被推断的程度，通常借助遥测数据（metrics 指标、logs 日志和 traces 追踪）来实现。

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**：一种目标设定框架，将定性的目标与若干可衡量的关键结果相配对，以帮助组织对齐方向并聚焦重点。

**OpenTelemetry (OTel)**：一套厂商中立的开放标准和工具集，用于从软件中生成、收集和导出遥测数据（追踪、指标和日志）。

**OPA (Open Policy Agent)**：一款开源的通用策略引擎，通过评估以 Rego 语言编写的策略来在整个技术栈中强制执行授权和配置规则，从而实现"策略即代码"（policy as code）。

**OSPO (Open Source Program Office)**：一个组织职能部门，负责统筹开源战略、治理、合规和社区参与，同时管理开源软件的使用和贡献。

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**：一个非营利社区，制作被广泛使用的免费应用安全资源，包括 OWASP Top Ten 和 ASVS。

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**：CAP 定理的扩展，指出如果发生分区（Partition），系统需要在可用性（Availability）和一致性（Consistency）之间权衡；否则（在正常运行时），系统需要在延迟（Latency）和一致性之间权衡。

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**：由支付卡行业维护的安全标准，规定了存储、处理或传输持卡人数据的组织所需满足的要求。

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)**：由专业测试人员对系统发起的经过授权的模拟攻击，旨在抢在真正的攻击者之前发现并演示可被利用的漏洞，最终以按优先级排列的、可付诸行动的发现结果呈现。

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**：能够单独或结合其他数据识别出特定个人的信息；其处理受隐私法律和内部政策的约束。

**Platform engineering**：构建和运营内部自助式平台及黄金路径（golden path）的学科，旨在降低认知负荷并加快产品团队的开发速度。

**POUR**：《网页内容无障碍指南》（WCAG）的四项指导原则：内容必须可感知（Perceivable）、可操作（Operable）、可理解（Understandable）和健壮（Robust）。

**Production readiness review**：在服务上线或开始承担待命（on-call）职责之前进行的结构化检查，用于确认该服务在可观测性、可靠性、安全性、操作手册和运维支持等方面达到标准。

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**：设计和完善提供给语言模型的指令、上下文和示例、以获得可靠、高质量输出的实践，被视为一门经过版本管理和测试的工程学科，而非单纯的试错。

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**：一种攻击方式，精心构造的输入会使语言模型忽略其原本的指令，转而遵循攻击者的指令，是人工智能时代对应于注入类漏洞的攻击手法。它是 LLM 应用的核心安全风险之一。

**Property-based testing**：一种测试技术，通过大量自动生成的输入来验证所声明的属性是否始终成立，而不仅仅依赖人工挑选的示例。

**Pull request (PR) / merge request (MR)**：提交以供评审和讨论、随后合并到共享分支中的一组变更提案，是大多数工作流程中代码评审的基本单位。

**Purple team**：一种协作演练，进攻方（红队）和防守方（蓝队）安全团队实时协同工作，使攻击手法和用于捕捉攻击的检测机制能够相互调优。

## Q

**Quality gate**：流水线中的一道自动化检查点，变更必须通过该检查点（例如达到覆盖率、安全性或性能阈值）才能继续推进。

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**：在分布式系统中，指某项操作（如读或写）被视为成功所需达成一致的最少节点数，用于在出现故障时仍维持一致性。

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**：一种职责分配模型，将任务或决策中的每位参与者标记为负责人（Responsible）、批准人（Accountable）、被咨询者（Consulted）或被告知者（Informed）。

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**：一种技术，先检索相关文档或数据并将其作为上下文提供给语言模型，从而为其输出提供依据，提升准确性并减少幻觉（hallucination）。

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**：一种授权模型，将权限分配给角色，再将角色分配给用户，通过在角色层面管理访问权限来简化管理工作。

**[Red team](https://en.wikipedia.org/wiki/Red_team)**：一个模拟真实对手的团队，通常针对整个组织、且不事先通知防守方，用以检验检测和响应能力，而不仅仅是枚举漏洞。与蓝队（防守方）相对。

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)**：用于对其他数据进行分类的、受控且缓慢变化的代码列表和分类体系，例如国家代码、货币和状态值。将其作为一份共享、带版本管理的词汇表来治理，可以保持各系统之间的一致性。

**Rego**：Open Policy Agent 使用的声明式策略语言，用于表达授权和配置决策的规则。

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**：一种面向网络应用程序的架构风格，通过 HTTP 对可寻址资源执行无状态操作，因其简单性和丰富的工具生态而受到推崇。

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**：位于一个或多个后端服务前面、负责转发客户端请求的服务器，通常提供 TLS 终止、负载均衡、缓存和统一入口等功能。

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**：在做出重大技术决策或变更之前，为征求反馈而传阅的书面提案，有助于促进透明度和共同责任感。（该术语也用于指代互联网标准文档系列。）

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**：衡量投资所获价值相对于其成本的指标，用于论证和排序工程与技术决策的优先级。

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**：以类似人工操作的方式与现有用户界面和系统交互，从而自动化重复性、基于规则的任务的软件"机器人"。

**RPO (Recovery Point Objective)**：以时间衡量的最大可接受数据丢失量（例如"最多五分钟"），用以界定数据必须以何种频率受到保护。

**RTO (Recovery Time Objective)**：服务中断后恢复服务所允许的最长时间，用以指导灾难恢复的设计和投入。

## S

**Saga**：一种模式，通过对本地事务排序、并在某一步骤失败时发起补偿操作，来管理分布式事务中跨服务的数据一致性。

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**：一种在大型企业中应用敏捷和精益实践、协调众多团队的框架；因其结构性而受到重视，也因可能过于繁重而受到批评。

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**：一种安全测试方式，在不执行源代码、字节码或二进制文件的情况下对其进行分析，以便在开发早期发现漏洞。

**SBOM (Software Bill of Materials)**：一份正式的、机器可读的软件组件和依赖清单，用于管理供应链和漏洞风险。

**SCA (Software Composition Analysis)**：用于识别代码库中开源和第三方组件、并标记已知漏洞和许可证风险的工具。

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**：一种敏捷框架，将工作组织为固定长度的迭代（冲刺，sprint），配以明确的角色、事件和工件，以交付增量价值。

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**：美国法律，要求联邦机构使其电子和信息技术对残障人士无障碍可用，实践中与 WCAG 保持一致。

**Semantic search**：根据语义而非精确关键词进行匹配的搜索方式，通常通过比较查询和文档的嵌入向量来实现。它常与词汇搜索结合，形成混合式方案。

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**：一个专用的基础设施层，通常以 sidecar 代理实现，用于处理服务间通信相关的问题，如双向 TLS、重试、超时、流量切换和可观测性，从而将这些问题从应用代码中剥离出来。

**Sidecar**：与主应用实例一同部署的辅助进程或容器，用于提供支持性能力（例如服务网格代理），而无需改变应用本身。

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**：一种系统，用于聚合和关联整个环境中的安全日志与事件，从而支持检测、告警和调查。

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**：服务提供方与客户之间的正式承诺，规定了预期的服务水平以及未达标时的后果。

**SLI (Service Level Indicator)**：对服务质量某一方面（如请求延迟或错误率）的量化度量，是 SLO 的输入指标。

**SLO (Service Level Objective)**：针对某项 SLI 设定的目标值或范围，界定了期望达到的可靠性水平，也是错误预算的基础。

**SLSA (Supply-chain Levels for Software Artifacts)**：一套分级安全要求框架，用于在构建和发布过程中提升软件制品的完整性和来源可追溯性。

**SOAR (Security Orchestration, Automation, and Response)**：用于自动化和协调安全运营（例如分诊和响应剧本）的工具与实践，以提升速度和一致性。

**SOC 2 (System and Organization Controls 2)**：一套基于 AICPA 信任服务标准（Trust Services Criteria）的审计框架及报告，用于评估服务型组织在安全性、可用性、处理完整性、保密性和隐私方面的控制措施。

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**：五项面向对象设计原则（单一职责、开闭原则、里氏替换、接口隔离和依赖倒置），旨在促成可维护、灵活的代码。

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**：美国立法，为上市公司的财务报告和内部控制确立了要求，对支撑财务数据的 IT 系统亦有相应影响。

**SPACE**：一个从五个维度衡量开发者生产力的框架：满意度与幸福感（Satisfaction and well-being）、绩效（Performance）、活动量（Activity）、沟通与协作（Communication and collaboration）以及效率与流动（Efficiency and flow），主张避免依赖单一指标。

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**：一门将软件工程方法应用于运维的学科，利用 SLO、错误预算和自动化来大规模运行可靠的系统。

**SSDF (Secure Software Development Framework)**：NIST 的框架（SP 800-218），提出了一套高层次的安全开发实践，涵盖组织准备、保护软件、生产安全软件和应对漏洞等方面。

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)**：在不执行源代码、字节码或二进制文件的情况下对其进行检查，以发现缺陷、代码风格违规和安全缺陷，通常通过接入编辑器和流水线的代码检查工具（linter）、类型检查器和专用分析工具实现。

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**：一种威胁建模分类法，将威胁分为伪装（Spoofing）、篡改（Tampering）、抵赖（Repudiation）、信息泄露（Information disclosure）、拒绝服务（Denial of service）和权限提升（Elevation of privilege）六类。

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**：系统或决策的全生命周期成本，涵盖购置、运行、维护直至最终退役，而不仅仅是初始价格。

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**：一种实践，先编写一个会失败的自动化测试，再编写使其通过的代码，随后进行重构，通过这种短周期的反复循环来驱动设计并确保测试覆盖。

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)**：选择当下权宜方案而非耗时更长的更优方案所隐含的未来成本，必须审慎管理，而非无意识地不断累积。

**TF-IDF (Term Frequency-Inverse Document Frequency)**：一种经典的权重计算方案，根据某个词在文档中出现的频率、并结合其在整个语料库中的常见程度来评分该词对文档的重要性。它是许多词汇搜索排序方法的基础。

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)**：一种管理方法，主张系统的吞吐量在任意时刻都受限于单一瓶颈，因此改进工作应聚焦于该约束，直至瓶颈转移到别处。

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)**：一种结构化的实践，用于识别、枚举并排定系统潜在威胁的优先级，从而能够在早期设计相应的防御措施。

**Toil**：在 SRE 中，指手动、重复、可自动化的运维工作，其工作量随服务规模线性增长且不产生持久价值；减少此类工作可以释放工程产能。

**Trunk-based development**：一种源代码管理实践，开发者频繁地将小的变更集成到单一共享分支中，从而减少长期存在的分支和痛苦的合并过程。

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)**：一种语言特性，能够自动推断表达式的类型，在无需手动逐一写出每个类型的情况下，提供静态类型系统的大部分安全性。

**[Type system](https://en.wikipedia.org/wiki/Type_system)**：一门语言用于赋予和检查类型的一套规则，能够在程序运行之前捕获整类错误，并记录代码意图。类型系统从动态到静态、从弱类型到强类型各不相同。

## U

**Ubiquitous language**：在 Domain-Driven Design 中，指开发者和领域专家共同一致使用的、精确的共享词汇，并直接体现在代码和模型之中。

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**：由最终用户或其代表执行的测试，用于在系统被验收发布之前确认其满足业务需求。

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**：用户体验（User Experience）是指一个人与产品交互的整体质量；用户界面（User Interface）则是指该交互所通过的具体视觉和交互界面。

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**：在 Domain-Driven Design 中，指完全由其属性而非独立身份定义的不可变对象，例如金额或日期范围。

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)**：一种技术，用于绘制从构想到交付价值的每一个步骤，区分增值时间与等待时间，从而使瓶颈、交接和返工循环变得可见、可改进。

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)**：一种针对按相似度索引和搜索高维嵌入向量而优化的数据存储，是语义搜索和检索增强生成的常见支撑技术。

**Vertical scaling**：通过增强单个节点的性能（即"纵向扩展"）来提升容量的方式，简单易行，但最终受限于可用的最大规格机器。

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**：一种工具（如 Git），随时间记录文件的变更，使历史记录可供审阅、分支可被维护、工作可被协调。

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**：针对已知缺陷和错误配置数据库，对系统、容器或代码进行的自动化检查。它覆盖面广、成本低，可以与人工渗透测试的深度互为补充。

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**：W3C 制定的一套国际公认指南，围绕 POUR 原则和 A、AA、AAA 三个合规等级组织，用于使网页内容无障碍可访问。

**Wardley map**：一种可视化战略技术，根据各项能力对用户的价值及其演化成熟度对其进行定位，以支持构建/购买及投资决策。

**Work in progress (WIP) limit**：对工作流程某一阶段中可同时存在的项目数量所设的上限，是看板方法的核心实践，通过暴露瓶颈和抑制过多并行工作带来的开销来改善流动性。

**WSJF (Weighted Shortest Job First)**：一种优先级排序方法，将延迟成本除以预计工期来对工作进行排序，使耗时最短、时效性最强、价值最高的项目最先完成。

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**：一种网页漏洞，攻击者借此注入恶意脚本，使其在其他用户的浏览器中执行，可能窃取数据或劫持会话。

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**：一项原则，建议不要基于猜测构建功能，理由是预期中的需求往往并不会真正出现，反而增加成本和复杂性。

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**：一种安全模型，不基于网络位置赋予任何隐式信任，而是持续依据身份、设备和上下文验证每一次访问请求，遵循"从不信任，始终验证"的准则。
