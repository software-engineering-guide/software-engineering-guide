# 2.8 Requisitos de software

## Visão geral e motivação

Um [requisito de software](https://en.wikipedia.org/wiki/Software_requirements) é uma declaração de uma capacidade ou condição que um sistema deve fornecer, satisfazer ou possuir para ser aceitável às suas partes interessadas. A [engenharia de requisitos](https://en.wikipedia.org/wiki/Requirements_engineering), o trabalho disciplinado de elicitar, analisar, especificar, validar e gerenciar essas declarações, fica logo no início da cadeia de valor. Tudo o que vem depois, da arquitetura ao código e aos [testes de aceitação](https://en.wikipedia.org/wiki/Acceptance_testing), é uma tentativa de satisfazer requisitos. Assim, quando os requisitos estão errados, incompletos ou ambíguos, todo o esforço gasto em construir a coisa errada de forma correta é puro desperdício, e é o desperdício mais caro que existe, porque você o descobre por último. A área de conhecimento de Requisitos de Software do [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) trata isso como uma disciplina de engenharia de verdade, e não como um prelúdio burocrático ao trabalho real.

Para equipes grandes, os requisitos são o entendimento compartilhado que permite a muitas pessoas construir um sistema coerente. Um único desenvolvedor consegue guardar a intenção na cabeça. Centenas de pessoas em muitas equipes não conseguem. Os requisitos se tornam o contrato entre quem precisa de uma capacidade e quem a constrói, a base para dividir o trabalho entre equipes e a régua para julgar quando algo está “pronto”. Eles se ligam diretamente à descoberta (capítulo 11.1), onde problemas e oportunidades emergem, aos fundamentos de UX (capítulo 5.1), onde você entende as necessidades dos usuários, às APIs e ao design de interfaces (capítulo 2.3), onde as obrigações de interface são fixadas, à arquitetura e aos atributos de qualidade (capítulo 3.1), onde os requisitos não funcionais dirigem a estrutura, e à gestão de projetos (capítulo 10.6), onde escopo, custo e cronograma são planejados em torno deles.

Em contextos corporativos e governamentais, os requisitos carregam peso jurídico, contratual e de segurança. Um sistema regulamentado precisa mostrar que toda obrigação imposta (acessibilidade, privacidade, segurança, retenção de registros, controle financeiro) está capturada como um requisito, implementada e verificada com evidências. As contratações governamentais costumam ser construídas em torno de uma especificação de requisitos, e o pagamento, a auditoria e a certificação dependem de rastrear cada requisito até a evidência de que foi atendido. Aqui, os requisitos são mais que boa prática: são a espinha dorsal da responsabilização.

## Princípios fundamentais

- Um requisito expressa uma necessidade ou restrição, não uma solução. Diz o quê e por quê, não como.
- Todo requisito deve ser necessário, inequívoco, verificável, viável e rastreável.
- Os requisitos são descobertos e negociados com as partes interessadas, não inventados em isolamento.
- Os requisitos não funcionais e as restrições moldam a arquitetura tanto quanto a funcionalidade.
- Os requisitos evoluem. Gerencie a mudança deliberadamente em vez de congelá-la ou ignorá-la.
- A rastreabilidade, da necessidade ao requisito, ao design, ao teste e à evidência, é o tecido conjuntivo da responsabilização.
- O nível certo de formalidade depende do risco, da escala e do contexto regulatório, não do hábito.

## Recomendações

### Defina os requisitos com clareza e categorize-os

Nomeie as categorias de propósito. Os **[requisitos funcionais](https://en.wikipedia.org/wiki/Functional_requirement)** dizem o que o sistema deve fazer: os comportamentos, transformações e serviços que ele fornece. Os **[requisitos não funcionais](https://en.wikipedia.org/wiki/Non-functional_requirement)** (atributos de qualidade) dizem quão bem ele deve fazê-lo: desempenho, disponibilidade, segurança, usabilidade, acessibilidade, manutenibilidade e mais. Eles se ligam estreitamente à arquitetura (capítulo 3.1). As **restrições** são os limites inegociáveis sobre a solução: tecnologias obrigatórias, padrões, orçamentos, regras legais ou interfaces com sistemas existentes. E separe os **requisitos de negócio** (por que a organização quer o sistema) dos **requisitos de usuário** (o que os usuários precisam realizar) e dos **requisitos de sistema** (o que o software deve, portanto, fazer). Misture esses níveis e a confusão de escopo logo se segue.

### Elicite a partir de fontes reais, não de suposições

A elicitação é descoberta ativa. Extraia os requisitos das partes interessadas por meio de entrevistas, oficinas, observação, [protótipos](https://en.wikipedia.org/wiki/Software_prototyping) e análise de sistemas e documentos existentes. Encontre toda parte interessada relevante, inclusive as fáceis de ignorar: operadores, auditores, equipe de suporte e pessoas afetadas pelo sistema que nunca o usam diretamente. Ligue a elicitação ao pipeline de descoberta (capítulo 11.1) e à pesquisa de UX (capítulo 5.1), para que os desejos declarados remetam às necessidades subjacentes. Registre a fonte e a justificativa de cada requisito, porque saber por que um requisito existe é exatamente o que permite alterá-lo com segurança depois.

### Analise, negocie e priorize

As necessidades elicitadas em bruto entram em conflito, se sobrepõem e somam mais do que é viável. A análise é como você as reconcilia: classifique os requisitos, identifique conflitos, pese viabilidade e risco e negocie as prioridades com as partes interessadas. Priorize às claras, por exemplo com distinções de deve/convém/poderia ou com um ranking de valor versus custo, para que, quando o tempo acabar, você corte o escopo certo. E modele os requisitos onde um modelo acrescenta clareza: fluxos de processo, diagramas de estado, modelos de dados e definições de interface expõem lacunas que a prosa esconde.

### Especifique no nível certo de formalidade

Escreva os requisitos numa forma que se ajuste ao risco e ao público. Um sistema governamental de alta garantia pode justificar uma especificação formal estruturada segundo um padrão como o IEEE 29148. Uma equipe de produto de ritmo acelerado pode capturar os requisitos como [histórias de usuário](https://en.wikipedia.org/wiki/User_story) com critérios de aceitação num backlog. De um jeito ou de outro, cada requisito deve ser atômico, verificável e livre de palavras escorregadias como “rápido”, “amigável” ou “etc.”. Anexe critérios de aceitação, para definir como verificar um requisito no mesmo instante em que o escreve. E mantenha uma única fonte autoritativa, em vez de deixar os requisitos se espalharem por e-mails, tíquetes e slides.

### Valide antes de construir

A validação confirma que os requisitos que você especificou são os certos e fazem sentido em conjunto. Revise-os com as partes interessadas, percorra cenários e, quando puder, use protótipos para tornar concretas as declarações abstratas. A validação é mais barata que qualquer correção posterior: um defeito pego numa revisão de requisitos custa uma fração do mesmo defeito pego em produção.

### Gerencie os requisitos e mantenha a rastreabilidade

Os requisitos mudam. O seu trabalho é controlar essa mudança, não resistir a ela. Estabeleça um processo de mudança: pese cada mudança proposta quanto a impacto, custo e efeito em cadeia antes de aceitá-la. Estabeleça linhas de base dos requisitos em pontos acordados e versione-os. Mantenha uma **[rastreabilidade bidirecional](https://en.wikipedia.org/wiki/Requirements_traceability)** que liga cada requisito, para a frente, ao design, ao código e aos testes e, para trás, à necessidade de que veio. A rastreabilidade responde às duas perguntas pelas quais as equipes grandes vivem: se esta necessidade mudar, o que isso afeta; e, para esta funcionalidade entregue, qual necessidade a justificou? Em contextos regulamentados, estenda o rastreamento até a evidência de aceitação (resultados de testes, registros de auditoria, aprovações) para poder demonstrar a conformidade e não apenas afirmá-la.

### Adapte-se a contextos ágeis e dirigidos por plano

Em programas dirigidos por plano e regulamentados, você especifica e estabelece linha de base dos requisitos bem cedo, com controle formal de mudanças. Em contextos ágeis, os requisitos vivem como um backlog priorizado e em evolução, elaborado pouco antes da implementação e validado continuamente por software em funcionamento. As atividades subjacentes são as mesmas nos dois casos. Só mudam o momento, a formalidade e os artefatos. As grandes organizações muitas vezes combinam os dois: especificam e rastreiam formalmente as obrigações estáveis e de alta garantia enquanto elaboram o comportamento do produto de forma iterativa. Escolha o equilíbrio pelo risco, não pela ideologia.

## Compromissos: prós e contras

| Abordagem | Melhor para | Prós | Contras |
|---|---|---|---|
| Especificação formal inicial | Contratos de alta garantia, regulamentados e de escopo fixo | Forte rastreabilidade. Base de aceitação clara. Auditável | Lenta para mudar. Risco de especificar demais antes de aprender |
| Backlog ágil | Produtos em evolução com partes interessadas engajadas | Feedback rápido. Adapta-se ao aprendizado. Menos desperdício com escopo não construído | Rastreabilidade de longo prazo mais fraca. Mais difícil de auditar e de contratar |
| Híbrido (restrições formais + comportamento ágil) | Empresas com obrigações mistas | Rigor onde importa, flexibilidade no resto | Exige julgamento sobre quais partes são quais |

A tensão central é entre estabilidade e aprendizado. Fixar os requisitos cedo compra uma base de aceitação firme e auditabilidade, mas custa a capacidade de se adaptar ao que você aprende enquanto constrói. Adiá-los compra adaptabilidade, mas custa rastreabilidade de longo prazo e clareza contratual. Investir mais em engenharia de requisitos também troca velocidade de curto prazo por menos retrabalho depois: uma troca que compensa à medida que a escala, a longevidade e a consequência de falha de um sistema aumentam. Os maiores projetos e os mais regulamentados ficam firmemente do lado do alto investimento. Uma ferramenta interna de baixo risco, não.

## Perguntas para discutir com sua equipe

1. **Quem conta como parte interessada do nosso sistema de maior risco, e quais continuamos deixando de fora até a aceitação?** Num programa grande, as pessoas que são puladas raramente são os usuários óbvios: são os operadores que mantêm a coisa funcionando às 3 da manhã, os auditores que precisam certificá-la, a equipe de suporte que atende às falhas e os não usuários afetados que nunca entram mas cujos dados você guarda. Deixe-as de fora e você descobre os requisitos delas no momento mais caro, durante a aceitação ou depois que um regulador perguntar. Leve um mapa concreto das partes interessadas à reunião e teste-o sob estresse: para cada obrigação imposta (acessibilidade, privacidade, retenção de registros, segurança), nomeie a pessoa responsável por ela e o requisito que a captura. Se você não consegue nomear um responsável, encontrou uma lacuna, e a correção é acrescentar essa parte interessada à elicitação agora, em vez de adaptar as necessidades dela depois numa arquitetura fixa.

2. **Quando um requisito muda, conseguimos responder o que ele afeta antes de aprovar a mudança?** Este é o teste prático de se a sua rastreabilidade bidirecional é real ou decorativa. Num sistema grande ou regulamentado, uma única mudança de regra pode reverberar no design, no código, nos testes e na evidência de aceitação, e aprová-la às cegas é como você entrega um sistema que parece em conformidade mas viola em silêncio uma regra que antes satisfazia. Leve um pedido de mudança recente e tente rastreá-lo para a frente na reunião: se leva uma tarde de arqueologia, a sua rastreabilidade não está cumprindo o papel. A resposta deve remodelar o seu processo de mudança, de modo que a avaliação de impacto seja uma consulta rápida a um rastreamento vivo e não uma caça manual, e que as linhas de base e o versionamento deem um ponto estável contra o qual mudar.

3. **Onde vive a única fonte autoritativa dos nossos requisitos, e quanta verdade está espalhada fora dela?** A proliferação de requisitos (a especificação real vivendo entre e-mails, tíquetes, slides e a memória de alguém) é uma das falhas mais comuns em equipes grandes, e é fatal em sistemas auditados, onde você precisa mostrar o que foi acordado. Decida, em voz alta, qual sistema de registro é canônico e trate qualquer coisa declarada em outro lugar como rascunho até chegar lá com sua fonte e justificativa anexadas. Leve evidências: conte quantas disputas recentes de escopo se resumiram a duas pessoas citando versões “finais” diferentes. Se a contagem for maior que zero, a ação é consolidar numa única fonte e escrever a justificativa de cada requisito, porque saber por que um requisito existe é exatamente o que permite alterá-lo ou descartá-lo com segurança depois.

4. **Os nossos requisitos não funcionais são capturados cedo o bastante para orientar a arquitetura, ou continuamos descobrindo-os depois que a estrutura está fixada?** As obrigações de desempenho, disponibilidade, segurança e acessibilidade moldam a arquitetura mais que a maioria das funcionalidades, e num programa grande são os requisitos que mais costumam aparecer tarde demais, quando a estrutura que teria de satisfazê-los já está concretada. A atração concorrente é real: o comportamento funcional é o que as partes interessadas pedem em voz alta e que se demonstra bem, enquanto um requisito de “resposta em menos de um segundo sob pico de carga” ou de “conformidade de acessibilidade com as WCAG” é invisível até ser violado. Leve a lista atual de requisitos não funcionais do seu sistema de maior risco, o ponto da linha do tempo em que cada um foi escrito e se a arquitetura (capítulo 3.1) os recebeu como direcionadores explícitos ou os inferiu. Em contextos corporativos e governamentais, acrescente as obrigações de qualidade impostas (criptografia, retenção de registros, lei de acessibilidade) e verifique se cada uma é um requisito escrito e mensurável entregue ao design e não uma suposição, porque adaptar um atributo de qualidade depois da aceitação é onde orçamentos e cronogramas morrem em silêncio.

5. **Que nível de formalidade é o certo para cada sistema que possuímos, e o escolhemos pelo risco ou pelo hábito?** Uma única grande organização costuma operar um leque de sistemas, de uma ferramenta interna descartável a uma plataforma regulamentada de risco à vida ou à segurança, e aplicar uma só cerimônia a todos ou enterra o trabalho de baixo risco em papelada ou deixa o de alto risco subespecificado. A tensão é entre a auditabilidade e a base firme de aceitação da especificação formal inicial e o feedback rápido e o desperdício reduzido de um backlog em evolução, e a resposta honesta para a maioria das empresas é uma mistura deliberada: formalizar e rastrear as obrigações estáveis e de alta garantia enquanto elabora o comportamento do produto de forma iterativa. Leve um breve inventário dos seus sistemas classificados por consequência de falha, exposição regulatória e taxa de mudança e, para cada um, nomeie a formalidade que vocês de fato usam versus a que o risco justifica. Para um programa governamental ancorado a um edital e a um padrão como o IEEE 29148, a formalidade é em parte ditada pelo contrato, então a discussão é sobre onde você pode sobrepor a elaboração ágil sem quebrar a rastreabilidade de que a auditoria depende.

6. **Todo requisito do nosso sistema de maior risco pode ser verificado, e cada um traz critérios de aceitação escritos no momento em que o requisito foi escrito?** Um requisito que você não consegue verificar não é um requisito, é um desejo, e palavras escorregadias como “rápido”, “seguro” ou “amigável” passam na revisão precisamente porque ninguém consegue reprová-las. Para uma equipe grande isso importa em dobro: requisitos não verificáveis produzem disputas de escopo na aceitação e tornam impossível dizer quando uma funcionalidade está genuinamente pronta. A consideração concorrente é a velocidade, já que anexar um critério mensurável e um método de verificação a cada requisito é mais lento de início que escrever prosa, mas é a defesa mais barata contra o retrabalho tardio mais caro. Leve uma amostra de requisitos recentes e teste cada um contra uma barra simples: é atômico, é mensurável e nomeia como será verificado? Em contextos regulamentados e governamentais, estenda o teste à evidência: um requisito sem evidência de aceitação rastreada e aprovada não é considerado entregue, não importa o que o software pareça fazer, então os critérios de aceitação são a semente do registro de conformidade que você acabará tendo de produzir.

## Perspectiva por setor

**Startup.** Com uma equipe minúscula e pouca pista, mantenha os requisitos tão leves quanto conseguir: histórias de usuário com critérios de aceitação num único backlog compartilhado, e não um documento de especificação. A disciplina que compensa até aqui é conversar com usuários reais antes de construir e registrar a fonte e a justificativa de cada história, para que a semana que você teria desperdiçado construindo a funcionalidade errada seja a semana que você poupa. Pule a rastreabilidade formal, mas nunca pule a conversa que diz qual é a necessidade real.

**Pequena empresa.** Você provavelmente não tem analista de negócios nem especialista em requisitos, então o trabalho cabe a quem estiver mais perto do cliente, e a pergunta de comprar versus construir domina. Enquadre os requisitos como uma lista curta e priorizada dos resultados de que você precisa e use-a para avaliar ferramentas prontas, e não para especificar uma construção sob medida. Seja rigoroso em separar a necessidade subjacente da lista de funcionalidades de um fornecedor, porque um requisito escrito como “precisamos do produto X” fecha em silêncio opções mais baratas que teriam atendido à necessidade real.

**Grande empresa.** A escala transforma os requisitos no contrato que permite a muitas equipes construir um sistema coerente, então a prioridade é um processo padrão aplicado de forma consistente: categorias definidas, rastreabilidade bidirecional da necessidade ao teste, uma única fonte autoritativa e mudança controlada com linhas de base. Separe explicitamente requisitos de negócio, de usuário e de sistema e entregue os requisitos não funcionais à arquitetura como direcionadores, para que escopo e obrigações de qualidade não se espalhem entre equipes. Combine a especificação formal para obrigações estáveis e de alta garantia com a elaboração ágil do comportamento do produto e governe o equilíbrio pelo risco, e não pela preferência de uma equipe.

**Governo.** As regras de contratação costumam construir todo o contrato em torno de uma especificação de requisitos, frequentemente estruturada segundo um padrão como o IEEE 29148, então precisão e completude são contratuais, não opcionais. Mantenha uma matriz de rastreabilidade de requisitos que ligue cada requisito ao design, aos casos de teste e à evidência de aceitação, porque o pagamento do fornecedor, a auditoria e a autorização para operar dependem de cobertura demonstrada. A transparência e a responsabilização pública elevam ainda mais a barra: as obrigações impostas de acessibilidade, privacidade e retenção de registros devem aparecer, cada uma, como um requisito explícito e verificável, e um requisito sem evidência rastreada e aprovada simplesmente não foi entregue.

## Exemplos

**Startup.** Uma startup de quatro pessoas que constrói um aplicativo de agendamento captura os requisitos como histórias de usuário com critérios de aceitação num backlog compartilhado, e não numa especificação formal. Antes de escrever a funcionalidade de sincronização de calendário, o fundador passa uma tarde conversando com cinco clientes em potencial e descobre que a necessidade real é evitar reservas duplicadas entre duas ferramentas, e não a sincronização que haviam presumido. Essa única conversa reenquadra a história e poupa uma semana construindo a coisa errada. Mesmo nessa escala, eles anotam a fonte e a justificativa de cada história, de modo que, quando as prioridades mudam, podem descartar ou retrabalhar o escopo sem rediscutir por que ele existia.

**Grande empresa.** Um banco multinacional substitui sua plataforma de originação de empréstimos. A equipe de requisitos separa os requisitos de negócio (reduzir o tempo de aprovação, atender às regulamentações de crédito), os requisitos de usuário (os analistas de crédito precisam comparar ofertas numa única tela) e os requisitos de sistema (a plataforma deve se integrar a três sistemas centrais). Os requisitos não funcionais (resposta em menos de um segundo para consultas comuns, 99,95% de disponibilidade, criptografia de dados pessoais) são capturados explicitamente e entregues à arquitetura (capítulo 3.1) como direcionadores. Todo requisito é rastreado, pelo backlog, até testes de aceitação automatizados. Assim, quando um regulador pergunta como uma regra de crédito específica é imposta, a equipe simplesmente segue o rastreamento da regra até o teste que a verifica.

**Governo.** Uma agência nacional contrata um sistema de elegibilidade a benefícios por meio de um edital formal. O contrato é ancorado a uma especificação de requisitos estruturada segundo o IEEE 29148, cobrindo as regras funcionais de elegibilidade, a conformidade de acessibilidade imposta, as restrições de privacidade e de retenção de registros e os controles de segurança. Uma matriz de rastreabilidade de requisitos liga cada requisito a elementos de design, casos de teste e evidência de aceitação. Os pagamentos ao fornecedor e a autorização para operar (a aprovação formal para rodar o sistema em produção) dependem de cobertura demonstrada. Um requisito sem evidência de aceitação rastreada e aprovada simplesmente não é considerado entregue, não importa o que o software pareça fazer.

## Justificativa de negócio: motivações, ROI e TCO

O argumento econômico da engenharia de requisitos repousa no custo de corrigir defeitos tarde. Estudos do setor constatam de forma consistente que os defeitos de requisitos estão entre as causas mais comuns e mais caras de fracasso de projetos e que o custo de corrigir um defeito sobe em ordens de grandeza da fase de requisitos até a produção. Assim, o dinheiro gasto em esclarecer e validar requisitos é na verdade alavancagem: um investimento modesto no início poupa você de construir, testar e operar a coisa errada.

O custo total de propriedade dos requisitos inclui o esforço contínuo de elicitação, especificação, ferramentas e gestão de mudanças ao longo de toda a vida do sistema, não é um custo único. Contra ele está o custo dos requisitos ruins: retrabalho, disputas de escopo, estouros de cronograma, aceitação fracassada, penalidades contratuais e, em contextos regulamentados, multas ou perda de autorização. Para a liderança, apresente a maturidade de requisitos como redução de risco e previsibilidade. Acompanhe a volatilidade dos requisitos, a origem dos defeitos e a parcela do trabalho entregue rastreável até uma necessidade validada e ligue isso à previsão da gestão de projetos (capítulo 10.6). O retorno não aparece como uma funcionalidade. Aparece como as falhas e o retrabalho que nunca aconteceram.

## Antipadrões e armadilhas

- **Soluções disfarçadas de requisitos:** especificar uma tecnologia escolhida ou um layout de tela em vez da necessidade subjacente, fechando opções melhores.
- **Linguagem ambígua:** “rápido”, “seguro”, “intuitivo” sem critério mensurável, tornando o requisito não verificável.
- **[Banho de ouro](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** capturar requisitos de que nenhuma parte interessada realmente precisa, inflando escopo e custo.
- **Requisitos não funcionais ausentes:** descobrir obrigações de desempenho, segurança ou acessibilidade só depois de a arquitetura estar fixada.
- **Proliferação de requisitos:** a verdade espalhada por e-mails, tíquetes e slides, sem fonte autoritativa.
- **Mudança congelada ou descontrolada:** ou recusar toda mudança ou aceitar toda mudança sem avaliação de impacto.
- **Sem rastreabilidade:** incapacidade de responder o que uma mudança afeta ou por que uma funcionalidade existe, fatal em sistemas auditados.
- **Paralisia por análise:** especificação sem fim que atrasa o aprendizado com software em funcionamento.
- **Partes interessadas ignoradas:** operadores, auditores e não usuários afetados deixados de fora até a aceitação.

## Modelo de maturidade

- **Nível 1, Iniciar.** Os requisitos são implícitos ou verbais, capturados de forma inconsistente e reativa. Disputas de escopo e retrabalho são comuns. Não há rastreabilidade, critérios de aceitação nem processo definido.
- **Nível 2, Desenvolver.** Algumas equipes escrevem os requisitos e os acompanham por projeto, com priorização básica e tratamento ad hoc de mudanças. As práticas existem mas variam por equipe e por pessoa, de modo que categorias, formalidade e qualidade são inconsistentes na organização.
- **Nível 3, Padronizar.** Um processo padrão de requisitos é documentado e imposto em toda a organização: categorias definidas, práticas de elicitação e validação, critérios de aceitação anexados na hora da redação, uma única fonte autoritativa e rastreabilidade bidirecional da necessidade ao teste, adaptados de forma consistente ao contexto ágil ou dirigido por plano.
- **Nível 4, Gerenciar.** O processo é medido e controlado com dados. A volatilidade dos requisitos, a origem dos defeitos, a cobertura de rastreabilidade e a parcela do trabalho entregue rastreável até uma necessidade validada são acompanhadas em relação a linhas de base. A rastreabilidade se estende à evidência de aceitação e à conformidade. E as métricas de requisitos alimentam a previsão de projetos (capítulo 10.6), de modo que as decisões de mudança e de qualidade se apoiam em evidências e não em opinião.
- **Nível 5, Orquestrar.** A prática de requisitos é continuamente melhorada e integrada em toda a organização. A formalidade é ajustada de forma adaptativa por risco e resultado, as ferramentas de elicitação e rastreabilidade se conectam à descoberta, à arquitetura e à entrega, e a organização usa o próprio histórico de medições para prevenir defeitos recorrentes de requisitos antes que cheguem ao código.

## Ideias para discussão

- Como você distingue um requisito genuíno de uma solução prematura quando uma parte interessada sênior o declara como solução?
- Que nível de formalidade de requisitos é o certo para o seu sistema de maior risco versus o de menor risco, e quem decide?
- Como você mantém a rastreabilidade bidirecional atual num backlog ágil de ritmo acelerado sem que ela vire custo burocrático?
- Quais requisitos não funcionais são descobertos tarde com mais frequência na sua organização, e por quê?
- Num programa regulamentado, o que constitui evidência de aceitação suficiente de que um requisito foi atendido?
- Como as ferramentas de elicitação e especificação assistidas por IA devem mudar a sua prática de requisitos, e que novos riscos introduzem?

## Principais conclusões

- Os requisitos declaram necessidades e restrições, não soluções. Devem ser necessários, inequívocos, verificáveis e rastreáveis.
- Separe os requisitos funcionais, não funcionais e de restrição e os níveis de negócio, de usuário e de sistema.
- Eliciteve a partir de partes interessadas reais, analise e priorize, especifique com a formalidade adequada, valide antes de construir e gerencie a mudança.
- A rastreabilidade bidirecional da necessidade à evidência de aceitação é a espinha dorsal da responsabilização, especialmente em contextos regulamentados.
- Contextos ágeis e dirigidos por plano compartilham as mesmas atividades. Diferem em momento, formalidade e artefatos, então escolha pelo risco.
- O custo dos requisitos ruins é pago tarde e multiplicado. Investir cedo é alavancagem contra o retrabalho e a aceitação fracassada.

## Referências e leitura complementar

- IEEE and ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, Software Requirements knowledge area
- Karl Wiegers and Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson and James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (requirements engineering chapters)
