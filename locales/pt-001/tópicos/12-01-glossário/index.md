# 12.1 Glossário

Este glossário define termos e siglas usados em todo o guia. As entradas são
agrupadas em ordem alfabética pelo termo em inglês, que é o usado na prática e
na literatura; quando existe um termo corrente em português, ele aparece entre
parênteses. Quando uma entrada tem uma sigla comum, ela é mostrada entre
parênteses. As definições são propositalmente concisas; consultem o capítulo
correspondente para um tratamento mais completo.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)** (controle de acesso baseado em atributos): Um modelo de autorização que concede acesso com base em atributos avaliados do usuário, do recurso, da ação e do ambiente (por exemplo, departamento, credencial de segurança, hora do dia) e não em papéis fixos. Oferece controle refinado e guiado por políticas ao custo de maior complexidade que o RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)** (acessibilidade): A prática de projetar e construir software de modo que pessoas com deficiência possam perceber, entender, navegar e interagir com ele. O numerônimo “a11y” abrevia as 11 letras entre “a” e “y”.

**ADR (Architecture Decision Record)** (registro de decisão de arquitetura): Um documento curto e versionado que registra uma única decisão arquitetural ou técnica significativa, seu contexto, as opções consideradas e suas consequências. Os ADRs criam um histórico durável e revisável de por que um sistema é como é.

**Aggregate** (agregado): No Domain-Driven Design, um conjunto de objetos de domínio tratado como uma unidade para mudanças de dados, com uma entidade atuando como raiz do agregado que impõe as invariantes. Os agregados definem as fronteiras de consistência e de transação.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)** (interface de programação de aplicações): Um contrato definido pelo qual um software solicita serviços ou dados de outro. APIs bem projetadas escondem detalhes de implementação e oferecem interfaces estáveis e versionadas.

**API-first**: Uma abordagem de desenvolvimento em que o contrato da API é projetado e acordado antes da implementação, para que consumidores e provedores possam trabalhar em paralelo contra uma especificação compartilhada.

**arc42**: Uma estrutura aberta, baseada em modelo, para documentar a arquitetura de software, organizada em doze seções que cobrem contexto, restrições, blocos de construção, tempo de execução, implantação e decisões.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Uma especificação do W3C que define papéis, estados e propriedades que tornam compreensíveis componentes web dinâmicos e personalizados para tecnologias assistivas, como leitores de tela.

**ASR (Architecturally Significant Requirement)** (requisito arquiteturalmente significativo): Um requisito com efeito mensurável e de amplo alcance sobre a arquitetura, como uma restrição de desempenho, disponibilidade, segurança ou regulatória. Os ASRs conduzem as decisões de projeto mais consequentes.

**ASVS (Application Security Verification Standard)**: Um padrão da OWASP que fornece uma lista de verificação graduada de requisitos e testes de segurança para projetar, construir e verificar aplicações seguras.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)** (escalonamento automático): O ajuste automático do número de instâncias de computação em execução (ou de seu tamanho) em resposta à carga, para que a capacidade acompanhe a demanda sem intervenção manual. Complementa, mas não substitui, o planejamento deliberado de capacidade.

**[Availability](https://en.wikipedia.org/wiki/Availability)** (disponibilidade): A proporção do tempo em que um sistema está operacional e capaz de atender requisições, muitas vezes expressa em “noves” (por exemplo, 99,9%). É uma meta central de confiabilidade codificada em SLOs e SLAs.

## B

**Backpressure** (contrapressão): Um mecanismo de controle de fluxo em que um componente sob carga sinaliza aos produtores a montante que desacelerem, prevenindo filas ilimitadas e falhas em cascata. É central para sistemas confiáveis de streaming e orientados a mensagens.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)** (desenvolvimento guiado por comportamento): Uma prática colaborativa que expressa requisitos como exemplos concretos e legíveis por humanos de comportamento (muitas vezes na forma Given/When/Then) que servem também como testes de aceitação automatizados.

**BFF (Backend for Frontend)**: Um padrão arquitetural em que um serviço de backend dedicado é construído para um frontend ou tipo de cliente específico, adaptando a modelagem e a agregação de dados às necessidades desse cliente.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)** (inteligência de negócios): As ferramentas, os processos e as práticas para coletar, integrar e analisar dados de negócio para apoiar relatórios, painéis e a tomada de decisão.

**Blameless postmortem** (post-mortem sem atribuição de culpa): Uma revisão de incidente que foca causas sistêmicas e aprendizado e não a falha individual, partindo da premissa de que as pessoas agem de forma razoável dadas as informações e os incentivos que tinham.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)** (implantação azul-verde): Uma estratégia de lançamento que roda dois ambientes de produção idênticos (“azul” e “verde”), encaminhando o tráfego a um enquanto o outro é atualizado, permitindo virada e rollback quase instantâneos.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Uma função de ranqueamento amplamente usada na busca de texto completo que pontua quão bem um documento corresponde a uma consulta usando frequência de termo, frequência inversa de documento e comprimento do documento. É o padrão de ranqueamento lexical em muitos mecanismos de busca.

**Bounded context** (contexto delimitado): No Domain-Driven Design, uma fronteira explícita dentro da qual um modelo de domínio particular e sua linguagem ubíqua se aplicam de forma consistente. Impede que conceitos sejam confundidos entre diferentes partes de um grande sistema.

**Build cache** (cache de build): Um repositório de saídas de build já calculadas, indexado pelas entradas que as produziram, para que o trabalho inalterado seja reutilizado em vez de reconstruído. Um cache de build remoto compartilhado permite que toda uma equipe e seu CI reutilizem os resultados uns dos outros.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)** (fator ônibus): O número de pessoas que precisariam ser perdidas (metaforicamente “atropeladas por um ônibus”) antes que um projeto empaque por falta de conhecimento essencial. Um fator ônibus baixo sinaliza perícia concentrada e não documentada e risco organizacional.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)** (política de remoção de cache): A regra que um cache usa para decidir qual entrada remover quando está cheio, como a menos recentemente usada (LRU) ou a menos frequentemente usada (LFU). A política molda a taxa de acertos e, com ela, o valor do cache.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)** (invalidação de cache): O problema de remover ou atualizar dados em cache quando a fonte subjacente muda, para que os leitores não vejam valores obsoletos. É famosamente um dos problemas mais difíceis da computação.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)** (estouro de cache): Um modo de falha em que muitos clientes erram o cache para a mesma chave ao mesmo tempo e todos atingem a origem juntos, sobrecarregando-a. A coalescência de requisições e a expiração escalonada o previnem. Também chamado de thundering herd.

**Canary release** (lançamento canário): Uma técnica de implantação que expõe uma nova versão primeiro a um pequeno subconjunto de usuários ou de tráfego, monitora problemas e então expande progressivamente o lançamento se as métricas permanecem saudáveis.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)** (teorema CAP): Um princípio segundo o qual um repositório de dados distribuído pode garantir no máximo duas de Consistência, Disponibilidade e Tolerância a partições simultaneamente; como as partições são inevitáveis, os projetistas na prática trocam consistência por disponibilidade durante elas.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)** (modelo C4): Uma abordagem leve para visualizar a arquitetura de software em quatro níveis de abstração: Contexto do Sistema, Contêineres, Componentes e Código.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)** (entrega contínua / implantação contínua): A entrega contínua mantém o software num estado liberável para que possa ser implantado a qualquer momento com uma aprovação manual; a implantação contínua lança automaticamente toda mudança que passa pelo pipeline.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)** (rede de distribuição de conteúdo): Uma rede geograficamente distribuída de servidores de borda que armazenam em cache e servem conteúdo perto dos usuários, cortando a latência e aliviando a infraestrutura de origem.

**Chain-of-thought prompting** (prompt de cadeia de pensamento): Uma técnica de prompting que pede a um modelo de linguagem que percorra passos intermediários de raciocínio antes de dar uma resposta final, melhorando o desempenho em problemas de várias etapas ao custo de uma saída mais longa e lenta.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)** (integração contínua): A prática de integrar com frequência as mudanças dos desenvolvedores a uma linha principal compartilhada, cada integração validada por um build e uma suíte de testes automatizados para detectar cedo problemas de integração.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: O pipeline combinado de integração contínua e entrega/implantação contínua que automatiza a construção, o teste e o lançamento de software.

**CMMC (Cybersecurity Maturity Model Certification)**: Um programa do Departamento de Defesa dos EUA que certifica a maturidade de cibersegurança de contratados que lidam com informações de contratos federais e informações não classificadas controladas.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))** (coesão): O grau em que os elementos dentro de um módulo pertencem juntos e servem a um único propósito bem definido. Alta coesão, combinada com baixo acoplamento, é marca de um projeto manutenível.

**Context window** (janela de contexto): A quantidade máxima de texto, medida em tokens, que um modelo de linguagem consegue considerar de uma vez, abrangendo sua entrada e saída. É um orçamento escasso que o projeto de prompt e de contexto deve gerir deliberadamente.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)** (lei de Conway): A observação de que a estrutura de um sistema tende a espelhar a estrutura de comunicação da organização que o constrói. A “manobra inversa de Conway” molda deliberadamente as equipes para produzir uma arquitetura desejada.

**Core Web Vitals**: Um conjunto de métricas de desempenho web centradas no usuário definidas pelo Google (como Largest Contentful Paint, Interaction to Next Paint e Cumulative Layout Shift) que medem carregamento, interatividade e estabilidade visual.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)** (custo do atraso): O custo econômico de não ter algo terminado ainda, expresso como valor perdido por unidade de tempo. Torná-lo explícito transforma a priorização de opinião em aritmética e sustenta regras de sequenciamento como o weighted shortest job first.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))** (acoplamento): O grau de interdependência entre módulos ou serviços. O baixo acoplamento limita o efeito em cascata da mudança e é uma meta central da boa arquitetura.

**CQRS (Command Query Responsibility Segregation)**: Um padrão que separa o modelo usado para alterar o estado (comandos) do modelo usado para ler o estado (consultas), permitindo que cada um seja otimizado e escalado de forma independente.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Um catálogo público de vulnerabilidades de segurança divulgadas, cada uma com um identificador único para que ferramentas e equipes possam se referir à mesma falha sem ambiguidade.

**CWV**: Ver Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (teste dinâmico de segurança de aplicações): Teste de segurança que sonda uma aplicação em execução de fora, sem acesso ao código-fonte, para achar vulnerabilidades que aparecem em tempo de execução.

**Data-ink ratio** (razão dados-tinta): Um princípio de Edward Tufte segundo o qual um gráfico deve gastar a maior parte de sua tinta nos próprios dados e pouca na decoração, removendo linhas de grade, bordas e enfeites que não informam.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Uma arquitetura de dados descentralizada e modelo operacional que trata os dados como um produto de que as equipes de domínio são donas, apoiado por infraestrutura de plataforma de autoatendimento e governança federada.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)** (visualização de dados): A prática de codificar dados em forma visual (posição, comprimento, cor e similares) para que padrões, comparações e tendências se tornem perceptíveis e as decisões mais bem informadas.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)** (projeto orientado a domínio): Uma abordagem de projeto de software que centra o modelo no domínio de negócio, usando uma linguagem ubíqua compartilhada, contextos delimitados e blocos de construção como entidades, objetos de valor e agregados.

**Design tokens**: Valores nomeados e agnósticos de plataforma (cores, espaçamento, tipografia e similares) que codificam decisões de design para que possam ser compartilhados de modo consistente por um sistema de design e vários produtos.

**DevEx / DevX (Developer Experience)** (experiência do desenvolvedor): A qualidade geral da interação do dia a dia de um desenvolvedor com ferramentas, plataformas e processos, abrangendo atrito, rapidez do feedback e carga cognitiva.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Uma cultura e um conjunto de práticas que unem desenvolvimento de software e operações para encurtar os ciclos de entrega, aumentar a frequência de implantação e melhorar a confiabilidade por meio de automação e propriedade compartilhada.

**DORA (DevOps Research and Assessment)**: Um programa de pesquisa e suas quatro métricas de entrega amplamente usadas (frequência de implantação, prazo de entrega das mudanças, taxa de falha das mudanças e tempo para restaurar o serviço) usadas para comparar o desempenho de entrega de software.

**DPIA (Data Protection Impact Assessment)** (avaliação de impacto à proteção de dados): Uma avaliação estruturada, exigida pelo GDPR para tratamento de alto risco, que identifica e mitiga riscos de privacidade antes que um projeto prossiga.

**Drift (configuration)** (deriva de configuração): A divergência gradual do estado real de um sistema em relação ao seu estado declarado ou pretendido, comumente causada por mudanças manuais; a infraestrutura como código e o GitOps visam detectá-la e corrigi-la.

**Drift (model)** (deriva de modelo): Em aprendizado de máquina, a degradação do desempenho de um modelo ao longo do tempo conforme as propriedades estatísticas dos dados de entrada (deriva de dados) ou a relação modelada (deriva de conceito) mudam.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)** (recuperação de desastres): A estratégia, os procedimentos e a infraestrutura para restaurar serviço e dados após um grande evento disruptivo, tipicamente regidos por metas de RTO e RPO.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Um princípio de projeto segundo o qual cada peça de conhecimento deve ter uma única representação autoritativa, reduzindo a duplicação e o risco de atualizações inconsistentes.

## E

**East-west traffic** (tráfego leste-oeste): Tráfego de rede entre serviços dentro de um sistema ou data center, em oposição ao tráfego norte-sul entre o sistema e clientes externos. Uma malha de serviços tipicamente governa o tráfego leste-oeste.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)** (computação de borda): Executar computação e armazenamento perto de onde os dados são produzidos ou consumidos e não num local central, para cortar latência e largura de banda. As redes de distribuição de conteúdo são uma forma inicial e difundida.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))** (elasticidade): A capacidade de um sistema de adquirir e liberar recursos automaticamente em resposta à demanda cambiante, para que a capacidade acompanhe de perto a carga.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Um padrão de integração de dados que carrega primeiro os dados brutos num repositório de destino e os transforma ali, explorando a escala dos data warehouses e lakehouses modernos.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)** (vetor de incorporação): Uma representação de texto, imagens ou outros dados como um vetor numérico denso, posicionado de modo que itens semelhantes fiquem próximos. Os embeddings sustentam a busca semântica e vetorial e a geração aumentada por recuperação.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: O padrão europeu que especifica requisitos de acessibilidade para produtos e serviços de TIC, referenciado pela contratação do setor público em toda a UE e alinhado à WCAG.

**Error budget** (orçamento de erros): A quantidade permissível de não confiabilidade permitida por um SLO ao longo de um período; quando se esgota, as equipes priorizam o trabalho de confiabilidade sobre novas funcionalidades. Reconcilia a tensão entre velocidade e estabilidade.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Um padrão de integração de dados que extrai dados das fontes, transforma-os numa forma de destino e os carrega num destino como um data warehouse.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)** (Lei de IA da UE): Regulamento da União Europeia que classifica os sistemas de IA por risco e impõe obrigações de acordo, banindo certos usos e regulando fortemente os sistemas de alto risco.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)** (consistência eventual): Um modelo de consistência em sistemas distribuídos em que as réplicas podem divergir temporariamente mas convergem ao mesmo estado quando as atualizações param de se propagar.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)** (flag de funcionalidade): Um mecanismo para ligar ou desligar funcionalidades em tempo de execução sem reimplantar, usado para lançamentos graduais, experimentação e controle operacional.

**Feature store**: Um sistema centralizado para definir, armazenar e servir features de aprendizado de máquina curadas de modo consistente tanto para treinamento quanto para inferência, reduzindo a duplicação e o desvio entre treinamento e serviço.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Um programa do governo dos EUA que padroniza a avaliação de segurança, a autorização e o monitoramento contínuo de serviços de nuvem usados por agências federais.

**Few-shot prompting** (prompt com poucos exemplos): Fornecer a um modelo de linguagem um punhado de exemplos resolvidos no prompt para demonstrar a tarefa desejada e o formato de saída, em oposição ao zero-shot prompting, que dá instruções sem exemplos.

**FinOps**: Uma disciplina e prática cultural que traz responsabilidade financeira ao gasto variável em nuvem, dando às equipes de engenharia, finanças e negócios a propriedade compartilhada do custo e do valor.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Legislação dos EUA que exige que as agências federais implementem, documentem e monitorem programas de segurança da informação, operacionalizada em grande parte por meio da orientação do NIST.

**Flow efficiency** (eficiência do fluxo): A proporção do prazo de entrega total que um item de trabalho passa sendo ativamente trabalhado em vez de esperando, calculada como tempo que agrega valor dividido pelo prazo de entrega total. A maioria dos sistemas é surpreendentemente baixa, muitas vezes abaixo de 15 por cento.

**Four-eyes principle** (princípio dos quatro olhos): Um controle que exige que uma ação significativa seja revisada ou aprovada por pelo menos duas pessoas, reduzindo a chance de erro ou malversação.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)** (teste de fuzzing): Uma técnica de teste automatizado que alimenta um programa com entradas malformadas, aleatórias ou inesperadas para descobrir falhas, brechas de segurança e defeitos em casos extremos.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)** (Regulamento Geral de Proteção de Dados): O regulamento da União Europeia que rege o tratamento de dados pessoais, concedendo direitos aos indivíduos e impondo obrigações a controladores e operadores, com penalidades significativas por descumprimento.

**GitOps**: Um modelo operacional que usa o Git como fonte única da verdade para infraestrutura e aplicações declarativas, com automação reconciliando continuamente o sistema em operação com o estado versionado.

**Golden path / paved road** (caminho dourado / caminho pavimentado): Uma forma padrão bem suportada e opinativa de construir e entregar software dentro de uma organização, projetada para tornar a escolha segura, conforme e confiável a mais fácil.

**Golden record** (registro de ouro): Na gestão de dados mestres, a versão única, reconciliada e autoritativa de uma entidade de negócio (como um cliente), montada a partir de vários sistemas de origem por regras de correspondência e de sobrevivência.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)** (tipagem gradual): Uma abordagem de sistema de tipos que deixa a tipagem estática e a dinâmica coexistirem numa mesma base de código, de modo que tipos possam ser acrescentados incrementalmente a um programa de tipagem dinâmica. Dicas de tipo e verificadores de tipo opcionais são exemplos comuns.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Uma linguagem de consulta e um runtime para APIs que deixa os clientes pedirem exatamente os dados de que precisam numa única chamada, usando um esquema fortemente tipado.

**[gRPC](https://en.wikipedia.org/wiki/GRPC)**: Um framework de chamada de procedimento remoto de alto desempenho e contrato primeiro que usa HTTP/2 e, tipicamente, Protocol Buffers para comunicação eficiente entre serviços.

## H

**Hermetic build** (build hermético): Um build que depende apenas de entradas explicitamente declaradas e é isolado do ambiente hospedeiro, de modo que produz a mesma saída em qualquer lugar. A hermeticidade é a base dos builds reproduzíveis e do cache confiável.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)** (módulo de segurança de hardware): Um dispositivo de hardware resistente a violação que gera, armazena e usa chaves criptográficas, oferecendo proteção de chaves mais forte que abordagens só de software.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Legislação dos EUA que, entre outras coisas, estabelece requisitos para salvaguardar informações de saúde protegidas (PHI) e rege seu uso e divulgação.

**Horizontal scaling** (escalonamento horizontal): Aumentar a capacidade acrescentando mais instâncias ou nós (“scaling out”) em vez de tornar um único nó mais potente. Sustenta a maioria das arquiteturas resilientes e de grande escala.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)** (infraestrutura como código): A prática de definir e provisionar infraestrutura por meio de configuração legível por máquina e versionada, em vez de processos manuais, permitindo repetibilidade e revisão.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)** (gestão de identidade e acesso): O arcabouço de políticas e tecnologias que garante que as identidades certas tenham o acesso certo aos recursos certos nos momentos certos.

**IDP / IdP**: “IDP” denota comumente uma Internal Developer Platform (plataforma interna de desenvolvedores), a camada de ferramentas de autoatendimento que abstrai a infraestrutura para as equipes de produto; “IdP” denota um Identity Provider (provedor de identidade), um serviço que autentica usuários e emite asserções. O contexto desfaz a ambiguidade.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)** (idempotência): Uma propriedade segundo a qual executar uma operação várias vezes tem o mesmo efeito que executá-la uma vez, essencial para repetições seguras em sistemas distribuídos e APIs.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)** (internacionalização): Projetar e construir software para que possa ser adaptado a diferentes idiomas, regiões e convenções culturais sem mudanças de engenharia. O numerônimo abrevia as 18 letras entre “i” e “n”.

**Immutable artefact** (artefato imutável): Uma saída de build que, uma vez produzida e versionada, nunca é modificada; qualquer mudança gera uma nova versão. A imutabilidade torna os lançamentos reproduzíveis e permite construir uma vez e promover o mesmo artefato entre ambientes.

**InnerSource**: A aplicação de práticas de desenvolvimento de código aberto (transparência, repositórios compartilhados e contribuição entre equipes) dentro de uma única organização.

**IaC drift**: Ver Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)** (índice invertido): A estrutura de dados central de um mecanismo de busca, que mapeia cada termo à lista de documentos que o contêm, para que as consultas possam ser respondidas sem varrer cada documento.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Um padrão internacional que especifica requisitos para um Sistema de Gestão de Segurança da Informação (SGSI), oferecendo um arcabouço certificável para gerir o risco de segurança da informação.

**ISO/IEC 42001**: Um padrão internacional que especifica requisitos para um Sistema de Gestão de IA, dando às organizações um arcabouço certificável para governar o desenvolvimento e o uso responsável de IA.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Um formato compacto de token, assinado (e opcionalmente criptografado), usado para transmitir declarações entre partes, comumente para autenticação e autorização em sistemas web e de API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Um método de fluxo de trabalho lean que visualiza o trabalho num quadro, limita o trabalho em andamento e gerencia o fluxo para melhorar a vazão e a previsibilidade.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Um princípio de projeto que favorece a solução mais simples que atenda à necessidade, com base em que a complexidade desnecessária aumenta o custo e o risco.

**KMS (Key Management Service)** (serviço de gestão de chaves): Um sistema para criar, armazenar, rotacionar e controlar o acesso a chaves criptográficas, muitas vezes apoiado por módulos de segurança de hardware.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)** (indicador-chave de desempenho): Uma medida quantificável usada para acompanhar o progresso em direção a um objetivo específico de negócio ou operacional.

## L

**Lakehouse**: Uma arquitetura de dados que combina o armazenamento flexível e de baixo custo de um data lake com os recursos de gestão, transações e desempenho de um data warehouse.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)** (prazo de entrega): O tempo decorrido desde que uma mudança é solicitada (ou commitada) até ser entregue em produção; uma métrica central de entrega da DORA.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)** (privilégio mínimo): Um princípio de segurança que concede a cada usuário, processo ou sistema apenas o acesso mínimo necessário para desempenhar sua função, limitando o dano de um comprometimento ou erro.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)** (Lei de Little): Um resultado da teoria das filas segundo o qual o número médio de itens num sistema estável é igual à taxa média de chegada multiplicada pelo tempo médio que cada item passa no sistema. Liga o trabalho em andamento, a vazão e o prazo de entrega.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)** (grande modelo de linguagem): Um modelo de aprendizado de máquina treinado em corpora de texto muito grandes para prever e gerar linguagem, capaz de tarefas como resumo, tradução e geração de código.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)** (localização): Adaptar software internacionalizado a uma localidade específica, incluindo tradução, formatação e convenções culturais. O numerônimo abrevia as 10 letras entre “l” e “n”.

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)** (gestão de dados mestres): A disciplina e as ferramentas para criar e manter uma visão única, autoritativa e consistente das entidades centrais de negócio (como clientes ou produtos) entre sistemas.

**MITRE ATT&CK**: Uma base de conhecimento pública e curada de táticas e técnicas de adversários do mundo real, amplamente usada para planejar exercícios de red team, orientar a engenharia de detecção e descrever ameaças num vocabulário compartilhado.

**Mean Time to Recovery (MTTR)** (tempo médio de recuperação): O tempo médio necessário para restaurar o serviço após uma falha; uma métrica comum de confiabilidade e de gestão de incidentes.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)** (programação em grupo): Uma prática em que toda uma equipe trabalha junta na mesma tarefa no mesmo computador, alternando quem digita, para compartilhar conhecimento e tomar decisões coletivamente.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: O conjunto de práticas que implanta, monitora e mantém de forma confiável e eficiente modelos de aprendizado de máquina em produção, estendendo os princípios de DevOps ao ciclo de vida de ML.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Um único repositório de controle de versão que guarda o código de muitos projetos ou de toda a organização, permitindo ferramentas compartilhadas e mudanças atômicas entre projetos ao custo de ferramentas especializadas de escala.

**mTLS (mutual TLS)** (TLS mútuo): Uma configuração do Transport Layer Security em que ambas as partes apresentam e verificam certificados, de modo que cada uma autentica a outra. É um padrão para o tráfego entre serviços numa malha de serviços e em redes zero-trust. Vejam também [autenticação mútua](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)** (teste de mutação): Uma técnica que introduz deliberadamente pequenas falhas (“mutantes”) no código para conferir se a suíte de testes as detecta, medindo a eficácia real da suíte.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Uma métrica de qualidade de ranqueamento que recompensa colocar resultados altamente relevantes perto do topo de uma lista de resultados, normalizada para que as pontuações sejam comparáveis entre consultas. É um esteio da avaliação de relevância de busca.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Uma agência federal dos EUA cujas Publicações Especiais e arcabouços são padrões amplamente referenciados para cibersegurança, privacidade e IA.

**NIST AI RMF (AI Risk Management Framework)**: Um arcabouço voluntário do NIST para identificar, avaliar e gerir riscos associados a sistemas de IA ao longo de seu ciclo de vida, organizado em torno das funções Governar, Mapear, Medir e Gerir.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Um catálogo do NIST de controles de segurança e privacidade para sistemas de informação federais, amplamente usado como linha de base bem além do governo.

**NIST SP 800-171**: Uma publicação do NIST que especifica requisitos para proteger informações não classificadas controladas (CUI) em sistemas não federais, central para a conformidade de contratados de defesa.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)** (requisito não funcional): Um requisito que descreve como um sistema deve se comportar (suas qualidades, como desempenho, segurança, confiabilidade ou usabilidade) e não quais funções executa.

**North-south traffic** (tráfego norte-sul): Tráfego de rede entre um sistema e seus clientes externos (para dentro e para fora do data center ou cluster), em oposição ao tráfego leste-oeste entre serviços internos. Um gateway de API tipicamente governa o tráfego norte-sul.

## O

**Observability** (observabilidade): O grau em que o estado interno de um sistema pode ser inferido de suas saídas externas, tipicamente obtido por telemetria: métricas, logs e traces.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)** (objetivos e resultados-chave): Um arcabouço de definição de metas que combina um objetivo qualitativo com alguns resultados-chave mensuráveis para alinhar e focar uma organização.

**OpenTelemetry (OTel)**: Um padrão aberto e agnóstico de fornecedor, com conjunto de ferramentas, para gerar, coletar e exportar dados de telemetria (traces, métricas e logs) de software.

**OPA (Open Policy Agent)**: Um motor de políticas de código aberto e de uso geral que avalia políticas (escritas na linguagem Rego) para impor regras de autorização e de configuração em toda a pilha, permitindo política como código.

**OSPO (Open Source Program Office)** (escritório de programa de código aberto): Uma função organizacional que coordena a estratégia, a governança, a conformidade e o engajamento de comunidade em código aberto, gerindo tanto o consumo quanto a contribuição.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Uma comunidade sem fins lucrativos que produz recursos de segurança de aplicações amplamente usados e gratuitos, incluindo o OWASP Top Ten e o ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Uma extensão do teorema CAP segundo a qual, havendo Partição, um sistema troca Disponibilidade por Consistência, Else (em operação normal) troca Latência por Consistência.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Um padrão de segurança mantido pela indústria de cartões de pagamento que especifica requisitos para organizações que armazenam, processam ou transmitem dados de portadores de cartão.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)** (teste de intrusão): Um ataque simulado e autorizado a um sistema por testadores habilidosos para achar e demonstrar vulnerabilidades exploráveis antes dos atacantes reais, entregue como achados priorizados e acionáveis.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)** (informações de identificação pessoal): Informações que podem identificar um indivíduo específico, sozinhas ou combinadas com outros dados; seu tratamento é regido por leis de privacidade e política interna.

**Platform engineering** (engenharia de plataforma): A disciplina de construir e operar plataformas internas de autoatendimento e caminhos dourados que reduzem a carga cognitiva e aceleram as equipes de produto.

**POUR**: Os quatro princípios orientadores das Web Content Accessibility Guidelines: o conteúdo deve ser Perceptível, Operável, Compreensível e Robusto.

**Production readiness review** (revisão de prontidão para produção): Uma verificação estruturada, executada antes de um serviço entrar no ar ou assumir o sobreaviso, que confirma que ele atende aos padrões de observabilidade, confiabilidade, segurança, runbooks e suporte operacional.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)** (engenharia de prompts): A prática de projetar e refinar as instruções, o contexto e os exemplos dados a um modelo de linguagem para obter uma saída confiável e de alta qualidade, tratada como disciplina de engenharia versionada e testada e não como tentativa e erro.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)** (injeção de prompt): Um ataque em que uma entrada elaborada faz um modelo de linguagem ignorar suas instruções pretendidas e seguir as do atacante, o análogo da era da IA para as falhas de injeção. É um risco de segurança central das aplicações de LLM.

**Property-based testing** (teste baseado em propriedades): Uma técnica de teste que verifica se propriedades declaradas valem para muitas entradas geradas automaticamente, em vez de depender apenas de exemplos escolhidos à mão.

**Pull request (PR) / merge request (MR)**: Um conjunto proposto de mudanças enviado para revisão e discussão antes de ser integrado a um branch compartilhado, a unidade principal de revisão de código na maioria dos fluxos.

**Purple team**: Um exercício colaborativo em que as equipes de segurança ofensiva (red) e defensiva (blue) trabalham juntas em tempo real, de modo que os ataques e as detecções feitas para pegá-los sejam ajustados uns contra os outros.

## Q

**Quality gate** (portão de qualidade): Um ponto de verificação automatizado num pipeline que precisa ser passado (por exemplo, atingir limiares de cobertura, segurança ou desempenho) antes que uma mudança possa avançar.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: Em sistemas distribuídos, o número mínimo de nós que precisam concordar para que uma operação (como uma leitura ou escrita) seja considerada bem-sucedida, usado para manter a consistência apesar de falhas.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Um modelo de atribuição de responsabilidades que rotula cada participante de uma tarefa ou decisão como Responsável, Aprovador (Accountable), Consultado ou Informado.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)** (geração aumentada por recuperação): Uma técnica que fundamenta a saída de um modelo de linguagem recuperando primeiro documentos ou dados relevantes e fornecendo-os como contexto, melhorando a precisão e reduzindo as alucinações.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)** (controle de acesso baseado em papéis): Um modelo de autorização que atribui permissões a papéis e papéis a usuários, simplificando a administração ao gerir o acesso no nível do papel.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: Um grupo que emula um adversário realista, muitas vezes contra uma organização inteira e sem avisar os defensores, para testar a detecção e a resposta e não meramente enumerar vulnerabilidades. Contrasta com um blue team (defensivo).

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)** (dados de referência): Listas de códigos e classificações controladas e de mudança lenta usadas para categorizar outros dados, como códigos de país, moedas e valores de status. Governá-los como um vocabulário compartilhado e versionado mantém os sistemas consistentes.

**Rego**: A linguagem declarativa de políticas usada pelo Open Policy Agent para exprimir regras de decisões de autorização e de configuração.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Um estilo arquitetural para aplicações em rede que usa operações sem estado sobre HTTP em recursos endereçáveis, valorizado pela simplicidade e pelas amplas ferramentas.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)** (proxy reverso): Um servidor que fica na frente de um ou mais serviços de backend e encaminha as requisições dos clientes a eles, comumente oferecendo terminação de TLS, balanceamento de carga, cache e um ponto único de entrada.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Uma proposta escrita circulada para feedback antes de uma decisão ou mudança técnica significativa, fomentando a transparência e a propriedade compartilhada. (O termo também nomeia a série de documentos de padrões da Internet.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)** (retorno sobre o investimento): Uma medida do valor obtido de um investimento em relação ao seu custo, usada para justificar e priorizar decisões de engenharia e tecnologia.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)** (automação robótica de processos): “Robôs” de software que automatizam tarefas repetitivas e baseadas em regras interagindo com interfaces de usuário e sistemas existentes como uma pessoa faria.

**RPO (Recovery Point Objective)** (objetivo de ponto de recuperação): A quantidade máxima aceitável de perda de dados medida em tempo (por exemplo, “até cinco minutos”), definindo com que frequência os dados devem ser protegidos.

**RTO (Recovery Time Objective)** (objetivo de tempo de recuperação): A duração máxima aceitável para restaurar um serviço após uma interrupção, orientando o projeto e o investimento em recuperação de desastres.

## S

**Saga**: Um padrão para gerir a consistência de dados entre serviços numa transação distribuída, sequenciando transações locais e emitindo ações compensatórias quando um passo falha.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Um arcabouço para aplicar práticas ágeis e lean em grandes empresas, coordenando muitas equipes; valorizado pela estrutura e criticado por seu potencial de peso.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)** (teste estático de segurança de aplicações): Teste de segurança que analisa código-fonte, bytecode ou binários sem executá-los para achar vulnerabilidades cedo no desenvolvimento.

**SBOM (Software Bill of Materials)** (lista de materiais de software): Um inventário formal e legível por máquina dos componentes e dependências de um software, usado para gerir o risco de cadeia de suprimentos e de vulnerabilidades.

**SCA (Software Composition Analysis)** (análise de composição de software): Ferramentas que identificam componentes de código aberto e de terceiros numa base de código e sinalizam vulnerabilidades conhecidas e riscos de licença.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Um arcabouço ágil que organiza o trabalho em iterações de duração fixa (sprints) com papéis, eventos e artefatos definidos para entregar incrementos de valor.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Uma lei dos EUA que exige que as agências federais tornem sua tecnologia eletrônica e da informação acessível a pessoas com deficiência, na prática alinhada à WCAG.

**Semantic search** (busca semântica): Busca que corresponde pelo significado e não por palavras-chave exatas, tipicamente comparando embeddings da consulta e dos documentos. É muitas vezes combinada com a busca lexical numa abordagem híbrida.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)** (malha de serviços): Uma camada de infraestrutura dedicada, geralmente implementada com proxies sidecar, que trata de preocupações da comunicação entre serviços como TLS mútuo, repetições, timeouts, deslocamento de tráfego e observabilidade, mantendo-as fora do código da aplicação.

**Sidecar**: Um processo ou contêiner auxiliar implantado ao lado de uma instância da aplicação principal para oferecer capacidades de apoio (como um proxy de malha de serviços) sem alterar a própria aplicação.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)** (gestão de informações e eventos de segurança): Um sistema que agrega e correlaciona logs e eventos de segurança em todo um ambiente para permitir detecção, alertas e investigação.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)** (acordo de nível de serviço): Um compromisso formal entre um provedor de serviço e seus clientes que especifica os níveis de serviço esperados e as consequências de não cumpri-los.

**SLI (Service Level Indicator)** (indicador de nível de serviço): Uma medida quantitativa de algum aspecto da qualidade do serviço, como a latência de requisições ou a taxa de erro, que alimenta os SLOs.

**SLO (Service Level Objective)** (objetivo de nível de serviço): Um valor ou faixa-alvo para um SLI que define o nível desejado de confiabilidade, formando a base dos orçamentos de erros.

**SLSA (Supply-chain Levels for Software Artifacts)**: Um arcabouço de requisitos de segurança graduados para melhorar a integridade e a procedência dos artefatos de software ao longo do processo de build e lançamento.

**SOAR (Security Orchestration, Automation, and Response)**: Ferramentas e práticas que automatizam e coordenam as operações de segurança, como a triagem e os playbooks de resposta, para melhorar a velocidade e a consistência.

**SOC 2 (System and Organisation Controls 2)**: Um arcabouço de auditoria e relatório, baseado nos Trust Services Criteria da AICPA, que avalia os controles de uma organização prestadora de serviços para segurança, disponibilidade, integridade de processamento, confidencialidade e privacidade.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Cinco princípios de projeto orientado a objetos (Responsabilidade Única, Aberto/Fechado, Substituição de Liskov, Segregação de Interfaces e Inversão de Dependência) que promovem código manutenível e flexível.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Legislação dos EUA que estabelece requisitos para relatório financeiro e controles internos em empresas de capital aberto, com implicações para os sistemas de TI que apoiam os dados financeiros.

**SPACE**: Um arcabouço para medir a produtividade de desenvolvedores em cinco dimensões: Satisfação e bem-estar, Desempenho, Atividade, Comunicação e colaboração, e Eficiência e fluxo, alertando contra medidas de uma só métrica.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)** (engenharia de confiabilidade de sites): Uma disciplina que aplica abordagens de engenharia de software às operações, usando SLOs, orçamentos de erros e automação para rodar sistemas confiáveis em escala.

**SSDF (Secure Software Development Framework)**: O arcabouço do NIST (SP 800-218) de práticas de alto nível de desenvolvimento seguro, abrangendo preparar a organização, proteger o software, produzir software bem protegido e responder a vulnerabilidades.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)** (análise estática): Examinar código-fonte, bytecode ou binários sem executá-los para achar defeitos, violações de estilo e falhas de segurança, tipicamente por meio de linters, verificadores de tipo e analisadores dedicados ligados ao editor e ao pipeline.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Uma taxonomia de modelagem de ameaças que categoriza as ameaças como Spoofing (falsificação), Tampering (adulteração), Repudiation (repúdio), Information disclosure (divulgação de informações), Denial of service (negação de serviço) e Elevation of privilege (elevação de privilégio).

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (custo total de propriedade): O custo completo ao longo da vida de um sistema ou decisão, incluindo aquisição, operação, manutenção e eventual aposentadoria, e não apenas o preço inicial.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)** (desenvolvimento guiado por testes): Uma prática de escrever um teste automatizado que falha antes do código que o faz passar, depois refatorar, em ciclos curtos e repetidos para conduzir o projeto e garantir cobertura.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)** (dívida técnica): O custo futuro implícito de escolher agora uma solução conveniente em vez de uma melhor que levaria mais tempo, que deve ser gerido deliberadamente e não acumulado sem perceber.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Um esquema clássico de ponderação que pontua a importância de um termo para um documento pela frequência com que aparece nele, compensada por quão comum é em todo o corpus. Sustenta boa parte do ranqueamento de busca lexical.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)** (teoria das restrições): Uma abordagem de gestão segundo a qual a vazão de um sistema é limitada por um único gargalo a cada momento, de modo que os esforços de melhoria devem focar essa restrição até que ela se mova para outro lugar.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)** (modelagem de ameaças): Uma prática estruturada de identificar, enumerar e priorizar ameaças potenciais a um sistema para que as defesas possam ser projetadas desde cedo.

**Toil** (trabalho repetitivo): Na SRE, trabalho operacional manual, repetitivo e automatizável que escala linearmente com um serviço e não traz valor duradouro; reduzi-lo libera capacidade para a engenharia.

**Trunk-based development** (desenvolvimento baseado em trunk): Uma prática de controle de código-fonte em que os desenvolvedores integram com frequência pequenas mudanças a um único branch compartilhado, minimizando branches de vida longa e a dor de merge.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)** (inferência de tipos): Um recurso de linguagem que deduz automaticamente os tipos das expressões, dando boa parte da segurança da tipagem estática sem exigir que cada tipo seja escrito à mão.

**[Type system](https://en.wikipedia.org/wiki/Type_system)** (sistema de tipos): O conjunto de regras que uma linguagem usa para atribuir e verificar tipos, pegando classes inteiras de erro antes de o programa rodar e documentando a intenção. Os sistemas de tipos vão do dinâmico ao estático e do fraco ao forte.

## U

**Ubiquitous language** (linguagem ubíqua): No Domain-Driven Design, um vocabulário compartilhado e preciso usado de modo consistente por desenvolvedores e especialistas de domínio e refletido diretamente no código e nos modelos.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)** (teste de aceitação do usuário): Teste realizado por usuários finais ou seus representantes para confirmar que um sistema atende às necessidades de negócio antes de ser aceito para lançamento.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)** (experiência do usuário / interface do usuário): A experiência do usuário é a qualidade geral da interação de uma pessoa com um produto; a interface do usuário é a superfície visual e interativa específica por meio da qual essa interação ocorre.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)** (objeto de valor): No Domain-Driven Design, um objeto imutável definido inteiramente por seus atributos e não por uma identidade distinta, como um valor monetário ou um intervalo de datas.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)** (mapeamento do fluxo de valor): Uma técnica para desenhar cada passo da ideia ao valor entregue, distinguindo o tempo que agrega valor do tempo de espera, de modo que gargalos, passagens de bastão e ciclos de retrabalho se tornem visíveis e melhoráveis.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)** (banco de dados vetorial): Um repositório de dados otimizado para indexar e buscar por similaridade vetores de embedding de alta dimensão, uma espinha dorsal comum da busca semântica e da geração aumentada por recuperação.

**Vertical scaling** (escalonamento vertical): Aumentar a capacidade tornando um único nó mais potente (“scaling up”), o que é simples mas em última instância limitado pela maior máquina disponível.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)** (sistema de controle de versão): Uma ferramenta, como o Git, que registra mudanças em arquivos ao longo do tempo para que o histórico possa ser revisado, branches possam ser mantidos e o trabalho possa ser coordenado.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)** (varredura de vulnerabilidades): Inspeção automatizada de sistemas, contêineres ou código contra bancos de dados de fraquezas e configurações incorretas conhecidas. É ampla e barata, e complementa a profundidade do teste de intrusão manual.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Um conjunto de diretrizes do W3C, reconhecidas internacionalmente, organizado em torno dos princípios POUR e dos níveis de conformidade A, AA e AAA, para tornar o conteúdo web acessível.

**Wardley map**: Uma técnica visual de estratégia que posiciona capacidades por seu valor para os usuários e sua maturidade evolutiva, para informar decisões de construir/comprar e de investimento.

**Work in progress (WIP) limit** (limite de trabalho em andamento): Um teto para quantos itens podem estar num dado estágio de um fluxo de trabalho ao mesmo tempo, uma prática central do Kanban que melhora o fluxo expondo gargalos e contendo a sobrecarga do excesso de trabalho paralelo.

**WSJF (Weighted Shortest Job First)**: Um método de priorização que sequencia o trabalho dividindo seu custo do atraso por sua duração estimada, de modo que os itens mais curtos, mais sensíveis ao tempo e de maior valor sejam feitos primeiro.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Uma vulnerabilidade web em que um atacante injeta scripts maliciosos que executam nos navegadores de outros usuários, potencialmente roubando dados ou sequestrando sessões.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Um princípio que aconselha não construir funcionalidades por especulação, com base em que as necessidades antecipadas muitas vezes não se materializam e acrescentam custo e complexidade.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)** (confiança zero): Um modelo de segurança que não presume nenhuma confiança implícita com base na localização na rede e verifica continuamente cada requisição de acesso contra identidade, dispositivo e contexto, seguindo a máxima “nunca confie, sempre verifique”.
