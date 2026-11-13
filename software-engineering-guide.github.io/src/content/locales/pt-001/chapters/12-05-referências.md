# 12.5 Referências

Esta seção consolida o aparato de referência do guia: uma correspondência com o
corpo de conhecimento SWEBOK, um índice dos padrões e arcabouços citados ao longo
do livro e uma bibliografia selecionada de leituras recomendadas. As fontes de
cada capítulo também aparecem na seção *Referências e leitura complementar* no fim
de cada capítulo.

---

# Correspondência com o SWEBOK

Este guia está alinhado ao **SWEBOK V4.0** (Software Engineering Body of
Knowledge) da IEEE Computer Society. Todas as 18 áreas de conhecimento são
cobertas; a tabela mapeia cada uma aos capítulos que a tratam, e o guia vai bem
além do SWEBOK em IA, dados, UX, DevOps, sustentabilidade, fluxo e tecnologia de
interesse público.

| Área de conhecimento do SWEBOK V4.0 | Capítulos principais |
|---|---|
| 1. Software Requirements | 2.8, 11.1, 5.1 |
| 2. Software Architecture | 3.1, 3.2, 3.3 |
| 3. Software Design | 2.2, 3.1 |
| 4. Software Construction | 2.9, 2.1 |
| 5. Software Testing | 2.4, 8.5 |
| 6. Software Engineering Operations | 9.1, 9.2, 9.3, 8.1 |
| 7. Software Maintenance | 3.7, 3.6, 10.4 |
| 8. Software Configuration Management | 2.10, 2.6, 8.2 |
| 9. Software Engineering Management | 10.1, 10.6, 10.2 |
| 10. Software Engineering Process | 1.4, 10.7, 10.8 |
| 11. Software Engineering Models and Methods | 2.12, 3.1, 2.2 |
| 12. Software Quality | 2.11, 2.4, 3.1 |
| 13. Software Security | 4.1, 4.2, 4.3, 4.4 |
| 14. Software Engineering Professional Practice | 10.5, 1.1, 1.3 |
| 15. Software Engineering Economics | 10.10, 10.1, 9.4 |
| 16. Computing Foundations | 2.13, 3.3, 3.4 |
| 17. Mathematical Foundations | 2.13, 11.3 |
| 18. Engineering Foundations | 2.13, 3.1 |

---

# Padrões e arcabouços

Este apêndice é um índice organizado dos padrões, arcabouços e regulamentos reais
referenciados ao longo do guia. É um auxílio de navegação, não um manual de
conformidade: consultem sempre a fonte autoritativa e, quando relevante, um
assessor jurídico ou de auditoria qualificado para o texto vigente e a
aplicabilidade ao seu contexto.

As entradas são agrupadas por domínio. Cada uma nomeia o padrão ou arcabouço, o
órgão emissor, um escopo em uma linha e os capítulos ou domínios em que é mais
relevante. Quando um nome costuma ser abreviado, a abreviação é mostrada. Números
de documento e títulos são dados apenas quando bem estabelecidos; nenhuma URL é
incluída.

## Como usar este apêndice

- Os **regulamentos** (por exemplo, GDPR, HIPAA) são juridicamente vinculantes
  dentro de sua jurisdição e setor. Estabelecem obrigações, não apenas boa prática.
- Os **padrões** (por exemplo, ISO/IEC 27001, WCAG) são especificações formais,
  muitas vezes certificáveis. Alguns são voluntários; alguns são exigidos por lei
  ou contrato.
- Os **arcabouços** (por exemplo, NIST CSF, NIST AI RMF) são orientações
  estruturadas, geralmente voluntárias, que vocês adaptam ao seu perfil de risco.
- A aplicabilidade depende de jurisdição, setor, tipos de dados e termos
  contratuais. Muitas organizações precisam satisfazer vários deles ao mesmo tempo.

## Segurança e privacidade

| Padrão / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Requisitos para um Sistema de Gestão de Segurança da Informação (SGSI). | 4.1–4.6 Segurança e conformidade |
| ISO/IEC 27002 | ISO / IEC | Orientação e conjunto de controles que apoiam a ISO/IEC 27001. | 4.1–4.4 Segurança |
| ISO/IEC 27017 / 27018 | ISO / IEC | Controles de segurança específicos de nuvem (27017) e proteção de PII na nuvem (27018). | 4.3 Segurança de infraestrutura e nuvem; 4.5 Privacidade |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Arcabouço voluntário organizado em torno de Governar, Identificar, Proteger, Detectar, Responder, Recuperar. | 4.1, 4.4 Fundamentos e operações de segurança |
| NIST SP 800-53 | National Institute of Standards and Technology | Catálogo de controles de segurança e privacidade para sistemas de informação. | 4.3, 4.6 Segurança de nuvem e conformidade |
| NIST SP 800-63 | National Institute of Standards and Technology | Diretrizes de garantia de identidade digital e autenticação. | 4.2, 4.3 Segurança de aplicações e de infraestrutura |
| OWASP Top Ten | Open Worldwide Application Security Project | Os riscos de segurança mais críticos de aplicações web, atualizados periodicamente. | 4.2 Segurança de aplicações |
| OWASP ASVS | Open Worldwide Application Security Project | Requisitos e testes graduados para verificar a segurança de aplicações. | 2.4, 4.2 Testes e segurança de aplicações |
| OWASP SAMM | Open Worldwide Application Security Project | Modelo de maturidade para construir e avaliar um programa de segurança de software. | 4.1 Fundamentos e cultura de segurança |
| STRIDE | Originado na Microsoft | Taxonomia de modelagem de ameaças para classificar ameaças. | 4.2 Segurança de aplicações |
| MITRE ATT&CK | MITRE | Base de conhecimento de táticas e técnicas de adversários para detecção e defesa. | 4.4 Operações de segurança |
| SLSA | Open Source Security Foundation (OpenSSF) | Arcabouço graduado de integridade e procedência da cadeia de suprimentos de software. | 4.2, 8.1, 10.3 Cadeia de suprimentos e entrega |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Formatos padrão para listas de materiais de software. | 4.2, 10.3 Segurança de aplicações e licenciamento |
| PCI DSS | PCI Security Standards Council | Requisitos de segurança para o tratamento de dados de cartões de pagamento. | 4.2, 4.5, 4.6 Segurança, privacidade, conformidade |

## Conformidade e governo

### Estados Unidos

| Regulamento / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Salvaguardas para informações de saúde protegidas (PHI). | 4.5, 4.6 Privacidade e conformidade |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Requisitos de relatório financeiro e de controle interno para empresas de capital aberto. | 4.6, 10.2 Conformidade e auditoria |
| FISMA | US Congress | Requisitos de programa de segurança da informação para agências federais. | 4.3, 4.6 Segurança de nuvem e conformidade |
| FedRAMP | US General Services Administration / FedRAMP PMO | Autorização de segurança padronizada para serviços de nuvem usados por agências federais. | 4.3, 4.6 Segurança de nuvem e conformidade |
| NIST SP 800-171 | National Institute of Standards and Technology | Proteção de informações não classificadas controladas (CUI) em sistemas não federais. | 4.6 Conformidade (cadeia de suprimentos de defesa) |
| CMMC | US Department of Defence | Certificação da maturidade de cibersegurança de contratados de defesa. | 4.6 Conformidade (defesa) |
| FIPS 140-3 | National Institute of Standards and Technology | Requisitos de segurança para módulos criptográficos. | 4.3 Segurança de infraestrutura e nuvem |
| CCPA / CPRA | State of California | Direitos de privacidade do consumidor e obrigações das empresas na Califórnia. | 4.5 Privacidade e proteção de dados |

### União Europeia e Reino Unido

| Regulamento / padrão | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| GDPR | European Union | Regulamento abrangente sobre o tratamento de dados pessoais. | 4.5, 4.6 Privacidade e conformidade |
| UK GDPR / Data Protection Act 2018 | United Kingdom | O regime de proteção de dados do Reino Unido pós-Brexit. | 4.5, 4.6 Privacidade e conformidade |
| eIDAS | European Union | Arcabouço para identificação eletrônica e serviços de confiança. | 4.2, 4.3 Segurança |
| NIS2 Directive | European Union | Obrigações de cibersegurança para entidades essenciais e importantes. | 4.4, 4.6 Operações de segurança e conformidade |
| DORA (Digital Operational Resilience Act) | European Union | Requisitos de resiliência operacional para o setor financeiro. | 9.1, 10.2 Confiabilidade e auditoria |
| EU AI Act | European Union | Regulamentação baseada em risco de sistemas de IA (ver governança de IA abaixo). | 6.1, 6.5 Estratégia de IA e IA responsável |

## Acessibilidade

| Padrão | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Diretrizes para conteúdo web acessível, com níveis de conformidade A/AA/AAA. | 5.3 Acessibilidade; 5.1–5.6 UX e frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Papéis, estados e propriedades para aplicações ricas de internet acessíveis. | 5.3, 5.6 Acessibilidade e frontend |
| Section 508 | US Access Board / US federal law | Requisitos de acessibilidade para TIC federal dos EUA, alinhados à WCAG. | 5.3 Acessibilidade (governo dos EUA) |
| EN 301 549 | ETSI / CEN / CENELEC | Requisitos europeus de acessibilidade para contratação de TIC, alinhados à WCAG. | 5.3 Acessibilidade (setor público da UE) |
| ADA (Americans with Disabilities Act) | US Congress | Lei de direitos civis que proíbe a discriminação por deficiência, aplicada a serviços digitais. | 5.3 Acessibilidade |
| ISO/IEC 40500 | ISO / IEC | Adoção internacional da WCAG 2.0 como padrão formal. | 5.3 Acessibilidade |

## Governança de IA

| Arcabouço / regulamento | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Arcabouço voluntário para governar, mapear, medir e gerir o risco de IA. | 6.1, 6.5 Estratégia de IA e IA responsável |
| ISO/IEC 42001 | ISO / IEC | Requisitos para um Sistema de Gestão de IA (AIMS). | 6.1, 6.5 Governança de IA |
| ISO/IEC 23894 | ISO / IEC | Orientação sobre gestão de riscos específicos de IA. | 6.5 IA responsável e confiável |
| EU AI Act | European Union | Obrigações legais escalonadas por risco para provedores e implantadores de sistemas de IA. | 6.1, 6.3, 6.5 Aplicações e governança de IA |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Princípios baseados em valores para IA confiável, influentes sobre a política. | 6.5, 10.5 IA responsável e ética |

## Qualidade e processo

| Padrão / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Modelo de qualidade de produto de software (adequação funcional, confiabilidade, segurança etc.). | 2.2, 2.4 Projeto e testes |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Processos do ciclo de vida de software. | 1.4, 10.1 Formas de trabalhar e gestão de programas |
| ISO 9001 | ISO | Requisitos para um Sistema de Gestão da Qualidade geral. | 10.2 Risco, auditoria e garantia |
| CMMI | ISACA / CMMI Institute | Modelo de maturidade para capacidade e melhoria de processos. | 10.1, 10.2 Gestão de programas e garantia |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | Quatro métricas-chave de desempenho de entrega para equipes de software. | 8.1, 8.4, 9.1 Entrega, plataforma, confiabilidade |
| SPACE framework | Microsoft / GitHub researchers | Modelo multidimensional para medir a produtividade de desenvolvedores. | 1.3, 8.4 Crescimento e experiência do desenvolvedor |
| ITIL | AXELOS / PeopleCert | Arcabouço de práticas de gestão de serviços de TI. | 9.1, 9.3 Confiabilidade e gestão de incidentes |

## Arquitetura

| Padrão / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Padrão para descrição de arquitetura e pontos de vista. | 2.7, 3.1 Documentação e fundamentos de arquitetura |
| TOGAF | The Open Group | Arcabouço de arquitetura corporativa e método de desenvolvimento. | 3.1, 10.1 Arquitetura e gestão de portfólio |
| C4 model | Comunidade (Simon Brown) | Abordagem de quatro níveis para visualizar a arquitetura de software. | 2.7, 3.1 Documentação e arquitetura |
| arc42 | Comunidade (Starke / Hruschka) | Modelo para estruturar a documentação de arquitetura. | 2.7, 3.1 Documentação e arquitetura |
| ADRs | Prática da comunidade | Registros leves de decisões significativas de arquitetura. | 1.5, 2.7, 3.1 Tomada de decisão e documentação |

## Nuvem e DevOps

| Padrão / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | Linhas de base de configuração segura por consenso para sistemas e nuvem. | 4.3, 8.2 Segurança de infraestrutura e IaC |
| CNCF landscape and projects | Cloud Native Computing Foundation | Ecossistema e padrões para computação nativa de nuvem (por exemplo, Kubernetes). | 8.3 Contêineres e nativo de nuvem |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Padrões abertos para formatos de imagem e de runtime de contêineres. | 8.3 Contêineres e nativo de nuvem |
| OpenTelemetry | Cloud Native Computing Foundation | Padrão neutro de fornecedor para telemetria (traces, métricas, logs). | 9.2 Observabilidade e monitoramento |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Motor de políticas de uso geral para política como código. | 4.6, 8.2, 8.3 Conformidade, IaC, orquestração |
| SRE practices | Google (amplamente adotado) | Abordagem baseada em SLI/SLO/orçamento de erros para operar serviços confiáveis. | 9.1 Engenharia de confiabilidade de sites |
| FinOps Framework | FinOps Foundation | Práticas de gestão financeira de nuvem e responsabilidade de custos. | 9.4 Custo, sustentabilidade, software verde |

## Dados

| Padrão / arcabouço | Órgão emissor | Escopo (uma linha) | Capítulos / domínios principais |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Corpo de conhecimento que organiza as disciplinas de gestão de dados. | 7.1 Estratégia e governança de dados |
| ISO/IEC 38505 | ISO / IEC | Governança de dados como ativo organizacional. | 7.1 Governança de dados |
| ISO 8000 | ISO | Padrões de qualidade de dados e de dados mestres. | 7.1, 7.2 Governança e engenharia de dados |
| Data mesh | Comunidade (Zhamak Dehghani) | Abordagem descentralizada e orientada a domínio de dados como produto. | 7.1, 7.2 Estratégia e engenharia de dados |
| DCAM | EDM Council | Modelo de avaliação de capacidade de gestão de dados. | 7.1 Estratégia e governança de dados |

## Notas sobre escopo e mudança

Os padrões e regulamentos evoluem. Os números de versão (por exemplo, WCAG 2.1
versus 2.2, ou anos de revisão da ISO) e os catálogos de controles mudam com o
tempo, e novas leis (como as regulamentações setoriais de IA e de resiliência)
continuam a surgir. Tratem este apêndice como um mapa de partida: confirmem a
versão vigente, a jurisdição e a aplicabilidade antes de confiar em qualquer
entrada para uma decisão de conformidade ou de contratação. Onde os capítulos do
guia e este apêndice diferirem em detalhe, o documento-fonte autoritativo sempre
prevalece.


---

# Leitura recomendada

Este apêndice é uma lista de leitura selecionada e anotada que abrange todos os
domínios do guia. Favorece obras que moldaram a prática em escala: clássicos
reconhecidos, referências rigorosas e os padrões e relatórios contra os quais as
equipes grandes, corporativas e governamentais são medidas.

Cada entrada dá o título e o(s) autor(es), seguidos de uma frase sobre por que
importa. A lista é organizada sob as dez partes do livro. Leiam seletivamente:
escolham as duas ou três obras mais próximas da sua dor atual, não a estante
inteira. Quando uma obra abrange vários domínios, ela é colocada onde é mais
útil; muitas pertencem a várias partes.

Uma nota sobre padrões: órgãos como NIST, OWASP, W3C/WCAG, ISO e o programa DORA
publicam documentos vivos que são revistos periodicamente. Citem e leiam a versão
vigente; as anotações abaixo descrevem seu propósito duradouro.

## Fundamentos: cultura, pessoas e processo

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. A base de pesquisa que mostra que o desempenho de entrega prediz o desempenho organizacional e define as métricas (hoje chamadas DORA) para medi-lo.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Um romance de negócios que torna intuitivos, para líderes e céticos, o fluxo, o trabalho em andamento e as “Três Maneiras” do DevOps.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. Um vocabulário prático (equipes alinhadas ao fluxo, de plataforma, habilitadoras e de subsistema complicado) para projetar organizações que produzem bom software.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Arcabouços testados em campo para dimensionar equipes, gerir o crescimento organizacional e tomar as decisões recorrentes da liderança de engenharia.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Define os arquétipos staff-plus e a trilha de liderança técnica para quem quer impacto sem virar gerente.
- **The Manager's Path**. Camille Fournier. Um guia etapa por etapa de líder técnico a executivo que ancora as trilhas de carreira e a transição para a gestão.
- **The Staff Engineer's Path**. Tanya Reilly. Um companheiro da literatura staff-plus focado no trabalho do dia a dia da liderança técnica, da influência e de conduzir sem autoridade.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. O argumento duradouro de que os problemas centrais do software são sociológicos, não técnicos.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. A origem da Lei de Brooks e da distinção entre complexidade essencial e acidental que ainda governa o dimensionamento de equipes e o cronograma.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. A base de pesquisa da cultura sem atribuição de culpa e da segurança que torna possível aprender com a falha.
- **Thinking, Fast and Slow**. Daniel Kahneman. O relato definitivo do viés cognitivo, essencial para entrevistas estruturadas, calibração e tomada de decisão honesta.

## Ofício da programação e qualidade de código

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. O catálogo fundamental de hábitos profissionais (DRY, ortogonalidade, tracer bullets) que define o que significa ofício.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. O catálogo canônico de transformações que preservam o comportamento e a disciplina da melhoria contínua do código com apoio de testes.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Um padrão amplamente usado (e debatido) de nomeação, funções e legibilidade que molda as expectativas de revisão de muitas equipes.
- **Code Complete**. Steve McConnell. Um manual abrangente e com referências a evidências das práticas de construção que continua sendo uma linha de base completa de qualidade de programação.
- **Test-Driven Development: By Example**. Kent Beck. A introdução original e prática ao ciclo vermelho-verde-refatorar e ao projeto com teste primeiro.
- **Working Effectively with Legacy Code**. Michael Feathers. O kit de ferramentas definitivo para acrescentar testes a código que não os tem e alterá-lo com segurança, indispensável para sistemas de longa vida.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. Uma demonstração trabalhada de TDD de fora para dentro, de mocking e de evolução de um projeto por meio de testes.
- **A Philosophy of Software Design**. John Ousterhout. Um tratamento afiado e opinativo da complexidade, dos módulos profundos e do ocultamento de informação que desafia de forma produtiva parte da ortodoxia do “código limpo”.

## Arquitetura e sistemas

- **Designing Data-Intensive Applications**. Martin Kleppmann. A melhor referência moderna sobre os compromissos de armazenamento, replicação, particionamento, consistência e processamento de fluxos em escala.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. Um levantamento amplo e atual de estilos arquiteturais, características e do papel e da tomada de decisão do arquiteto.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Um tratamento focado em decisões dos compromissos da arquitetura distribuída, da granularidade de serviços e da propriedade de dados.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Apresenta as funções de aptidão e a arquitetura projetada para mudar com segurança ao longo do tempo.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. A origem dos contextos delimitados, da linguagem ubíqua e dos agregados: o vocabulário do projeto moderno de serviços.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. A referência para decomposição, fronteiras de serviço, implantação e as implicações organizacionais dos microsserviços.
- **Monolith to Microservices**. Sam Newman. Um catálogo de padrões para decomposição incremental, como strangler fig e branch by abstraction, sem uma reescrita big-bang arriscada.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. A referência de padrões nomeados (repository, unit of work e mais) que deu uma linguagem compartilhada aos sistemas corporativos.
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. O catálogo definitivo de padrões de mensageria que sustentam as arquiteturas orientadas a eventos e assíncronas.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. A fonte do disjuntor, da antepara e de outros padrões de estabilidade para sistemas que sobrevivem à produção real.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). O catálogo historicamente decisivo de padrões orientados a objetos e um vocabulário de projeto compartilhado.

## Segurança, privacidade e confiança

- **Threat Modelling: Designing for Security**. Adam Shostack. O guia prático e abrangente do STRIDE e da modelagem estruturada de ameaças como prática rotineira de engenharia.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. A referência enciclopédica sobre como os sistemas reais falham e como construir os que resistem a ataques.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Um passeio rigoroso pelo modelo de segurança do navegador e pelos modos sutis em que as plataformas web traem suposições ingênuas.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Um guia de praticante para usar a criptografia corretamente e evitar os erros comuns e perigosos.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). A síntese do Google da segurança e da confiabilidade como propriedades entrelaçadas, projetadas desde o início.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. Um tratamento claro dos princípios e da mecânica da arquitetura de rede de nunca confiar, sempre verificar.
- **OWASP Top 10**. OWASP Foundation. A linha de base de consenso dos riscos de segurança mais críticos de aplicações web, referenciada por políticas e auditorias no mundo todo.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Uma lista de verificação graduada e testável de requisitos de segurança adequada a contratos e critérios de aceitação.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. O catálogo de controles no coração da segurança federal dos EUA e a base da autorização FedRAMP e FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. A estrutura amplamente adotada de identificar-proteger-detectar-responder-recuperar para organizar um programa de segurança.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. A definição de referência e as arquiteturas de referência que ancoram a maioria dos programas corporativos e governamentais de zero-trust.

## UX, UI e design de produto

- **The Design of Everyday Things**. Don Norman. O texto fundamental sobre affordances, signifiers, feedback e design centrado no ser humano, que se aplica muito além de objetos físicos.
- **Don't Make Me Think, Revisited**. Steve Krug. O argumento conciso e duradouro a favor da usabilidade autoevidente e do valor do teste de usabilidade barato e frequente.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. A referência abrangente sobre design de interação, personas e design orientado a objetivos.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Um relato fundamentado da construção de sistemas de componentes consistentes e reutilizáveis e da linguagem compartilhada por trás deles.
- **Refactoring UI**. Adam Wathan and Steve Schoger. Um guia prático, guiado por exemplos, de acabamento visual para engenheiros que projetam interfaces sem formação formal.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. O guia definitivo de design de conteúdo em linguagem simples e focado em tarefas.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Companheiros práticos para construir interfaces que funcionam para toda a gama de capacidades humanas.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. Uma ponte guiada por princípios entre os padrões de acessibilidade e a boa experiência do usuário.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. O padrão internacionalmente referenciado (perceptível, operável, compreensível, robusto) por trás da maior parte da legislação de acessibilidade.
- **U.S. Web Design System (USWDS)**. U.S. government. Um exemplo funcional de sistema de design acessível e baseado em padrões, construído para serviços públicos em escala.

## Inteligência artificial e aprendizado de máquina

- **Designing Machine Learning Systems**. Chip Huyen. O principal guia prático para construir sistemas de ML em produção de ponta a ponta: dados, features, implantação e monitoramento.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Estende a disciplina de SRE (SLOs, monitoramento, resposta a incidentes) a sistemas de aprendizado de máquina.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. A referência acadêmica padrão da teoria e dos métodos que sustentam as redes neurais modernas.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Um guia atual para projetar, avaliar e operar aplicações construídas sobre grandes modelos de fundação.
- **Weapons of Maths Destruction**. Cathy O'Neil. Um argumento vívido a favor da responsabilidade algorítmica e dos danos reais de modelos não examinados, essencial para a IA no setor público.
- **Interpretable Machine Learning**. Christoph Molnar. Uma referência abrangente e gratuita sobre métodos de explicabilidade de modelos e de suas previsões.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. O arcabouço de referência para governar, mapear, medir e gerir o risco de IA, cada vez mais citado em políticas e contratações.

## Dados, análise e insight

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball and Margy Ross. A referência canônica sobre esquemas estrela e modelagem dimensional para análise.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. O guia autoritativo para conduzir experimentos que dão resultados confiáveis e acionáveis em escala.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. Um mapa neutro de fornecedor do ciclo de vida moderno dos dados e das práticas de engenharia por trás dele.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. O texto fundador da abordagem orientada a domínio e centrada em produto para organizar dados em escala.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Um guia prático de visualização de dados honesta e clara e de comunicação de insights a quem decide.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. A obra fundamental sobre integridade gráfica, dados-tinta e a ética de mostrar dados com honestidade.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. O arcabouço de referência abrangente de governança, custódia, qualidade e catalogação de dados.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. Uma introdução legível à inferência causal, vital para passar da correlação a decisões defensáveis.

## Automação, DevOps e engenharia de plataforma

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. O manual abrangente que traduz as “Três Maneiras” em práticas concretas de fluxo, feedback e aprendizado contínuo.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. O texto fundamental sobre pipelines de implantação, automação e lançamento de software com segurança e frequência.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. A referência sobre tratar a infraestrutura como software: módulos, testes, imutabilidade e deriva.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (Ver Fundamentos.) Também essencial aqui para moldar equipes de plataforma e a experiência do desenvolvedor que elas oferecem.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Um catálogo de padrões reutilizáveis para projetar aplicações nativas de nuvem no Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Como práticas de engenharia como teste, revisão, ferramentas e gestão de dependências escalam para dezenas de milhares de engenheiros ao longo de décadas.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). O manifesto conciso e influente para construir serviços portáteis, escaláveis e nativos de nuvem.
- **DORA State of DevOps Report**. DORA / Google Cloud (annual). O programa de pesquisa contínuo por trás das quatro métricas-chave de entrega e das capacidades que conduzem o desempenho.

## Operações, confiabilidade e observabilidade

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). O texto fundamental que define SLIs, SLOs, orçamentos de erros e a disciplina de engenhar a confiabilidade.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). O companheiro prático com exemplos, SLOs trabalhados e orientação de implementação.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. A definição moderna de observabilidade, dos dados de alta cardinalidade e da depuração do desconhecido em produção.
- **Implementing Service Level Objectives**. Alex Hidalgo. Um guia minucioso e prático para projetar, medir e usar bem SLOs e orçamentos de erros.
- **Release It!**. Michael T. Nygard. (Ver Arquitetura.) Também fundamental aqui para os padrões de estabilidade em produção e a operação de sistemas resilientes.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. Uma abordagem guiada por dados para prever a demanda e planejar a capacidade de sistemas em crescimento.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. O tratamento definitivo da injeção deliberada de falhas para construir confiança na resiliência do sistema.
- **Google SRE Book, Chapter on Postmortems**. Google. O modelo amplamente imitado de post-mortems sem atribuição de culpa e de aprendizado com incidentes.

## Empresa, governo e interesse público

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. O estudo essencial de como o código aberto é de fato sustentado e do ônus dos mantenedores por trás das dependências em que as empresas se apoiam.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Um relato lúcido de por que a tecnologia do setor público fracassa e de como uma reforma focada na entrega pode consertá-la.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lições do UK Government Digital Service sobre transformar serviços públicos entregando e não planejando.
- **Project to Product**. Mik Kersten. O Flow Framework para deslocar grandes empresas do financiamento por projeto para fluxos de valor de produto duráveis.
- **Escaping the Build Trap**. Melissa Perri. Como as organizações confundem saída com resultado e como a gestão de produto conserta isso, com relevância direta para a governança de portfólio e de programas.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Um conjunto conciso de jogadas para entregar serviços digitais governamentais eficazes e centrados no usuário.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Um padrão publicado e em uso para construir bons serviços públicos, amplamente imitado por outros governos.
- **NIST SP 800-37: Risk Management Framework**. NIST. O arcabouço de processo por trás da autorização para operar (ATO) e do monitoramento contínuo em sistemas federais dos EUA.
- **The FinOps Foundation Framework**. FinOps Foundation. O modelo de referência para visibilidade, otimização e responsabilidade de custos de nuvem entre finanças e engenharia.

## Como usar esta lista

- **Comecem pela sua dor.** Se as implantações são lentas e assustadoras, leiam *Accelerate*, *Continuous Delivery* e os relatórios *DORA* antes de qualquer outra coisa.
- **Leiam para a década, não para o sprint.** Prefiram as obras que explicam princípios duradouros às ligadas a uma versão específica de ferramenta.
- **Verifiquem a edição vigente dos padrões.** NIST, OWASP, WCAG, ISO e DORA revisam suas publicações; trabalhem sempre a partir da versão mais recente e anotem a versão nas suas próprias políticas.
- **Construam uma estante compartilhada.** Uma equipe que leu em comum duas ou três destas obras discute menos e decide mais rápido, porque compartilha um vocabulário e um conjunto de pontos de referência.
- **Vejam também o capítulo 12.5** para o índice completo de padrões e arcabouços de referência, e o **capítulo 12.6** para como sequenciar a adoção das práticas que essas obras descrevem.
