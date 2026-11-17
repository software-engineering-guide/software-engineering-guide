# 9.1 Engenharia de confiabilidade de sites

## Visão geral e motivação

A [engenharia de confiabilidade de sites](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) aplica as práticas de engenharia de software à operação de sistemas de produção. Em vez de tratar as operações como trabalho manual, guiado por chamados e mantido separado do desenvolvimento, a SRE trata a confiabilidade como um problema de engenharia que se resolve com código, medição e objetivos de serviço claros. A ideia central, popularizada pelo Google mas hoje difundida, é simples: as pessoas que mantêm os sistemas funcionando devem gastar a maior parte do tempo construindo automação e melhorando sistemas e não apagando à mão, de novo e de novo, as mesmas falhas.

Para grandes equipes isso importa porque a escala eleva tanto o valor da confiabilidade quanto o custo de errar. Quando um serviço sustenta milhões de usuários ou milhares de consumidores internos, uma hora de indisponibilidade significa receita perdida, transações perdidas e confiança erodida. As operações manuais que funcionam bem para um punhado de servidores desmoronam diante de centenas de serviços e da [implantação contínua](https://en.wikipedia.org/wiki/Continuous_deployment). A SRE dá uma linguagem compartilhada para a confiabilidade, um modo de tornar explícito o compromisso entre entregar funcionalidades e manter a estabilidade e um modo de sustentar essa linha com consistência entre muitas equipes.

Os contextos corporativo e governamental acrescentam peso. As indústrias reguladas, como bancos, saúde e serviços públicos, muitas vezes carregam compromissos legais ou contratuais de disponibilidade, exigências de auditoria e pouca tolerância a interrupções que afetam cidadãos ou segurança. Os serviços digitais governamentais publicam cada vez mais suas metas de confiabilidade e seus dados de desempenho abertamente. A SRE dá um modo rigoroso e baseado em evidências de definir o que significa “confiável o bastante”, medi-lo com honestidade e defender as prioridades de engenharia junto à liderança e aos órgãos de supervisão com dados e não com opinião.

*Veja também:* capítulo 9.2 (observabilidade e monitoramento), capítulo 9.3 (gestão de incidentes) e capítulo 3.5 (escalabilidade, desempenho e resiliência).

## Princípios fundamentais

- **A confiabilidade é a funcionalidade mais importante.** Um sistema que não funciona não vale nada por mais funcionalidades que tenha, mas a confiabilidade perfeita nem é alcançável nem vale o seu custo.
- **Definam a confiabilidade com objetivos mensuráveis.** Os indicadores (SLIs), objetivos (SLOs) e acordos (SLAs) de nível de serviço transformam expectativas vagas em números com que todos podem concordar.
- **100 por cento é a meta errada.** Os usuários não distinguem entre um sistema muito confiável e um perfeitamente confiável, então mirem o “confiável o bastante” e gastem o orçamento restante em velocidade.
- **Os orçamentos de erro alinham os incentivos.** A diferença entre o SLO e 100 por cento é um orçamento de risco que desenvolvedores e operadores compartilham, trocando discussões por aritmética.
- **O trabalho repetitivo (toil) é o inimigo.** O trabalho operacional repetitivo, manual e automatizável deve ser medido, limitado e sistematicamente eliminado.
- **Automatizem deliberadamente.** A automação é como uma equipe pequena opera um sistema grande. Investir nela é uma atividade de engenharia de primeira classe.
- **Aprendizado sem atribuição de culpa.** As falhas são tratadas como oportunidades de melhorar sistemas e processos, não de punir indivíduos.

## Recomendações

### Defina SLIs, SLOs e SLAs deliberadamente

Comecem pela perspectiva do usuário. Um **[indicador de nível de serviço](https://en.wikipedia.org/wiki/Service-level_indicator)** é uma medida quantitativa do comportamento de um serviço, como a proporção de requisições atendidas em menos de 300 milissegundos ou a fração de respostas bem-sucedidas. Escolham um pequeno número de SLIs que genuinamente reflitam a satisfação do usuário: disponibilidade, latência, correção e atualidade são comuns. Um **[objetivo de nível de serviço](https://en.wikipedia.org/wiki/Service-level_objective)** é um valor ou faixa alvo para um SLI, por exemplo “99,9 por cento das requisições têm sucesso numa janela móvel de 28 dias”. Um **[acordo de nível de serviço](https://en.wikipedia.org/wiki/Service-level_agreement)** é um contrato com consequências (reembolsos, penalidades) atreladas a um nível prometido. Mantenham os SLOs mais rigorosos que os SLAs, para ter um aviso antes de violar um compromisso. Publiquem os SLOs, revisem-nos trimestralmente e tratem-nos como documentos vivos que se apertam ou afrouxam conforme vocês aprendem.

### Adote orçamentos de erro e imponha-os

O orçamento de erros é `100% menos o SLO`. Se o SLO é de 99,9 por cento, o orçamento é de 0,1 por cento de não confiabilidade por janela, cerca de 43 minutos por mês. Gastem-no em risco planejado: lançamentos agressivos, experimentos e testes controlados de falha. Quando o orçamento está saudável, as equipes podem entregar depressa. Quando se esgota, a política deve deslocar automaticamente as prioridades para o trabalho de confiabilidade e pausar as mudanças arriscadas até o sistema se recuperar. O poder do orçamento de erros é que vocês o combinam de antemão, de modo que ele tira a emoção e a política do momento de uma interrupção.

### Meça e reduza o trabalho repetitivo (toil)

O toil é o trabalho operacional manual, repetitivo, automatizável, tático e que cresce em compasso com o sistema. Acompanhem a porcentagem do tempo de SRE gasta em toil e definam um teto, comumente em torno de 50 por cento, para que pelo menos metade do tempo de engenharia vá para melhorias duráveis. Mantenham um backlog de projetos de redução de toil, priorizem por frequência vezes custo e celebrem matar uma tarefa recorrente tanto quanto entregar uma nova funcionalidade. Um **mandato de automação** torna isso explícito: qualquer procedimento manual executado mais que um número definido de vezes vira candidato à automação ou a uma ferramenta de autoatendimento.

### Planeje a capacidade e preveja a demanda

Modelem a carga esperada a partir de tendências históricas, lançamentos planejados e projeções de negócio. Combinem previsões de crescimento orgânico com eventos pontuais como campanhas de marketing, prazos de impostos ou períodos de inscrição em benefícios, que importam muito no governo. Mantenham folga acima do pico, façam testes de carga para conferir as suposições e automatizem a escala onde puderem, mantendo um [plano de capacidade](https://en.wikipedia.org/wiki/Capacity_planning) revisado por humanos para compromissos grandes. Acompanhem os prazos de provisionamento para que uma escassez nunca pegue vocês de surpresa.

### Trate a confiabilidade como uma funcionalidade com custo real

Cada “nove” extra de disponibilidade costuma custar muito mais em redundância, testes e sofisticação operacional que o anterior. Tornem explícito o custo dos noves, para que os donos de produto escolham a meta de olhos abertos. Projetem para a degradação graciosa, de modo que falhas parciais deem um serviço reduzido e não interrupções totais. Invistam em redundância e failover em proporção ao SLO, não de modo uniforme em todo componente.

### Escolha um modelo organizacional de SRE

Não existe uma estrutura única correta. Uma equipe de SRE **centralizada** dá consistência, expertise profunda e ferramentas compartilhadas, mas pode virar um gargalo ou um depósito dos problemas de outras pessoas. Um modelo **embutido** coloca os SREs dentro das equipes de produto para uma colaboração próxima, mas corre o risco de inconsistência e isolamento. Muitas grandes organizações usam um híbrido: uma equipe central de plataforma e padrões mais engenheiros de confiabilidade embutidos, com um modelo claro de engajamento que define quando um serviço se qualifica para o apoio de SRE e que patamar de prontidão de produção ele precisa cruzar primeiro.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| SLOs rigorosos (mais noves) | Maior confiança do usuário, cumpre contratos | Custo crescente, entrega de funcionalidades mais lenta |
| SLOs frouxos (menos noves) | Entrega mais rápida, custo menor | Risco de perda de usuários e penalidades de SLA |
| SRE centralizada | Consistência, expertise compartilhada | Gargalos, distância do produto |
| SRE embutida | Colaboração próxima, contexto | Inconsistência, difícil de dotar de pessoal |
| Forte investimento em automação | Escala, reduz o toil | Custo inicial, a automação pode ela mesma falhar |

A engenharia de confiabilidade trata, na verdade, de gastar recursos finitos com sabedoria. Perseguir um nove extra que os usuários nem percebem desperdiça dinheiro que poderia financiar funcionalidades ou baixar preços. Ir para o outro lado e investir pouco num sistema cujas falhas causam dano real é negligência. O framework do orçamento de erros existe justamente para tornar esse compromisso visível e negociável em vez de implícito e conflituoso. O compromisso do modelo organizacional é igualmente real: a resposta certa depende do tamanho da empresa, da maturidade de engenharia e de quão uniformes são os seus serviços.

## Perguntas para discutir com sua equipe

1. **Que SLI exato reflete o que os seus usuários de fato sentem, e vocês conseguem mostrar que não é uma métrica de vaidade?** Escolham o indicador errado e todo painel fica verde enquanto os usuários sofrem, que é a armadilha do SLI de vaidade contra a qual este capítulo alerta. Levem dados reais à discussão: meçam a mesma jornada do usuário a partir de um caminho real de requisição (login até o painel, checkout até a confirmação) e não a CPU do servidor ou uma verificação de saúde do backend. Para uma grande equipe, um SLI ruim se propaga: dezenas de serviços o herdam, os alertas disparam sobre a coisa errada e o orçamento de erros deixa de significar qualquer coisa. Em contextos corporativos e governamentais, em que um SLA carrega reembolsos ou impacto sobre o cidadão, o seu SLI é a evidência que vocês defendem perante os auditores, então ele precisa se ligar diretamente ao sucesso visível ao usuário. Se vocês não conseguem traçar uma linha do número à experiência de um usuário, troquem o número.

2. **O que um serviço precisa provar antes de a sua equipe de SRE assumir o sobreaviso dele, e quem diz não?** Sem um patamar de prontidão de produção, uma equipe central de SRE vira um depósito de todo serviço instável e se afoga na dívida técnica alheia. Escrevam os critérios de entrada: um SLO com dono, runbooks que funcionam, alertas acionáveis, folga de capacidade e um caminho demonstrado de implantação e reversão. Para uma grande organização, esse modelo de engajamento é o que impede a equipe de confiabilidade de virar um gargalo que atrasa todo mundo. Em contextos regulados, a revisão de prontidão vale também como um controle que vocês podem mostrar aos órgãos de supervisão. Decidam quem tem a autoridade de recusar a integração, porque um patamar que ninguém impõe não é um patamar, e a resposta muda se a SRE escala ou desaba sob a dor herdada.

3. **Com que antecedência vocês pré-provisionam para o seu maior pico previsível, e vocês sabem o seu prazo de provisionamento?** Presumir que a elasticidade da nuvem é instantânea e infinita convida a escassez justamente nos picos que mais importam, e esses picos (prazos de impostos, janelas de inscrição, eventos de venda) são os momentos em que a falha é mais visível e mais cara. Levem os números: a carga de pico histórica, o crescimento previsto, o múltiplo a que vocês fazem teste de carga e o prazo real para adquirir grande capacidade reservada ou instâncias especializadas. Para serviços governamentais sazonais, o pico pode ser várias vezes a carga normal e é politicamente impossível de perder, então pré-provisionar com semanas de antecedência vence esperar que o autoescalonamento acompanhe. A resposta deve fixar um calendário concreto: quando vocês fazem teste de carga, quando travam a capacidade e quem é dono da decisão de seguir.

4. **Quando o seu orçamento de erros se esgota, o que de fato acontece, e quem tem a legitimidade de impor?** Um orçamento de erros em que nunca se age quando esgotado é só decoração, e o momento de uma interrupção é o pior para negociar a política do zero. A atração contrária é real: um lançamento comprometido, um prazo de receita ou um anúncio público vão pressionar com força contra um congelamento de mudanças arriscadas. Levem os dados de taxa de consumo, o texto da política pré-combinada e um registro das últimas vezes em que o orçamento foi estourado, para ver se o congelamento de fato se manteve. Para uma grande equipe, o orçamento só alinha incentivos se todo grupo herdar a mesma imposição, então decidam de antemão quem aprova uma sobrescrita e como essa exceção é registrada. Em contextos corporativos e governamentais em que um SLA carrega penalidades ou impacto sobre o cidadão, o rastro das sobrescritas vira um artefato de auditoria, então nomeiem agora o dono responsável em vez de improvisar quando o orçamento já acabou.

5. **Que fração da semana da sua equipe de SRE é toil, e isso é um número medido ou uma sensação?** O toil que ninguém conta se expande em silêncio até a equipe gastar todo o tempo apagando incêndios e nenhum construindo melhorias duráveis, que é exatamente a armadilha da qual a SRE existe para escapar. A tensão é que medir o toil é em si trabalho, e os engenheiros sob pressão de prazo resistem a registrar onde vão suas horas. Levem uma amostra honesta: uma ou duas semanas de tempo acompanhado contra uma definição compartilhada de toil (manual, repetitivo, automatizável, tático e que cresce com o sistema), mais o backlog de projetos de automação classificados por frequência vezes custo. Para uma grande organização, um teto de 50 por cento só significa algo se for reportado e defendido equipe por equipe, então combinem quem revisa o número e o que acontece quando uma equipe o estoura. Em contextos regulados e governamentais, limitar o toil libera especialistas escassos para o trabalho de controle e de auditoria que as operações manuais espremem, então tratem o número de toil como um sinal de capacidade que a liderança deve ver.

6. **Que modelo organizacional de SRE vocês rodam, e que evidência diria que ele deixou de servir?** Uma equipe centralizada dá consistência e ferramentas compartilhadas mas pode virar gargalo; um modelo embutido dá contexto mas deriva para a inconsistência; o híbrido em que a maioria das grandes organizações se estabelece precisa de um modelo claro de engajamento ou herda as fraquezas dos dois. Levem os sinais que revelam tensão: quanto tempo os serviços esperam pelo apoio de SRE, quanto a prática de confiabilidade varia entre as equipes e se os engenheiros embutidos se sentem cortados de uma comunidade profissional. A resposta certa depende do tamanho da empresa, da maturidade de engenharia e de quão uniformes são os seus serviços, então revisitem-na conforme isso muda em vez de tratar a primeira escolha como permanente. Para um órgão corporativo ou governamental com muitas equipes e fortes exigências de uniformidade, um grupo central de padrões e plataforma mais engenheiros de confiabilidade embutidos costuma equilibrar consistência e contexto local, mas só se o modelo de engajamento e o patamar de prontidão de produção estiverem escritos e alguém for dono deles.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e sem fôlego para uma equipe dedicada de confiabilidade, escolham um único SLO sobre a jornada do usuário que mais importa e dividam o sobreaviso por toda a equipe. Apoiem-se nos serviços gerenciados do seu provedor de nuvem e no monitoramento embutido em vez de construir infraestrutura de observabilidade e escrevam revisões pós-incidente curtas num documento compartilhado para que as correções peguem. A velocidade importa mais que o processo aqui: um SLO frouxo que vocês de fato impõem vence um elaborado que ninguém vigia.

**Pequena empresa.** Sem especialista para cuidar da confiabilidade, tratem-na como uma disciplina em que vocês entram pela plataforma: monitoramento hospedado de disponibilidade, bancos de dados gerenciados e ferramentas de página de status em vez de uma pilha sob medida. Definam um ou dois SLOs ligados às transações que pagam as contas e decidam com honestidade quais falhas custariam um cliente. Comprem resiliência onde for mais barato que construir e mantenham o fardo operacional leve o bastante para que os engenheiros que vocês já têm o carreguem junto com o trabalho de funcionalidades.

**Grande empresa.** O desafio é a consistência entre muitas equipes: um vocabulário compartilhado de SLOs, uma política comum de orçamento de erros e um patamar de prontidão de produção que todo serviço cruza antes de a SRE assumir o sobreaviso dele. Um grupo central de plataforma e padrões mais engenheiros de confiabilidade embutidos mantém a prática uniforme sem virar gargalo, e a governança precisa de orçamentos de erro reportados e impostos do mesmo modo em toda parte. Orcem explicitamente a infraestrutura de observabilidade e o investimento em automação e gerenciem a confiabilidade como um portfólio, com métricas que a liderança consiga ver.

**Governo.** Os serviços públicos muitas vezes carregam metas publicadas de disponibilidade, compromissos estatutários e obrigações de auditoria, de modo que as decisões sobre SLOs e orçamentos de erro viram registros que vocês defendem perante os órgãos de supervisão. As regras de contratação podem restringir que monitoramento e hospedagem vocês podem usar, e as expectativas de transparência empurram a publicar os dados de confiabilidade num painel público de status. Planejem com semanas de antecedência os picos sazonais extremos, como prazos de impostos e janelas de inscrição em benefícios, e mantenham uma cultura de revisão pós-incidente sem atribuição de culpa para que as falhas públicas conduzam à melhoria do sistema e não à culpa individual.

## Exemplos

**Startup.** Uma startup de dez pessoas roda um único aplicativo web e divide o sobreaviso entre três engenheiros. Em vez de montar uma equipe de confiabilidade que não pode bancar, escolhe um SLO significativo: 99,5 por cento de sucesso no fluxo de login até o painel, medido a partir de requisições reais de usuários. Quando uma API instável de terceiros começa a devorar esse orçamento, a equipe gasta uma sexta-feira acrescentando uma nova tentativa e um cache em vez de entregar a próxima funcionalidade e depois escreve uma revisão pós-incidente de dois parágrafos num documento compartilhado para que a correção pegue.

**Grande empresa.** Uma empresa global de pagamentos fixa um SLO de disponibilidade de 99,99 por cento para a sua API de transações, o que dá um orçamento de erros de cerca de quatro minutos por mês. Uma equipe central de plataforma de SRE é dona da [observabilidade](https://en.wikipedia.org/wiki/Observability_(software)) compartilhada, das ferramentas de incidentes e da política de orçamento de erros, enquanto engenheiros de confiabilidade embutidos trabalham dentro de cada grupo de produto. Quando uma nova funcionalidade de detecção de fraude queima metade do orçamento mensal em uma semana, a política pré-combinada congela os lançamentos não críticos até o trabalho de confiabilidade restaurar a folga. Os executivos aceitam isso sem debate, porque ratificaram a política de antemão.

**Governo.** Uma autoridade tributária nacional roda um serviço online de declaração com picos sazonais extremos em torno do prazo anual. Sua equipe de SRE prevê a demanda a partir dos anos anteriores mais mudanças de população e de política, faz teste de carga em vários múltiplos do pico normal e pré-provisiona capacidade com semanas de antecedência. SLOs públicos de disponibilidade e de latência de página vão para um painel de status. Uma cultura de [revisão pós-incidente](https://en.wikipedia.org/wiki/Postmortem_documentation) sem atribuição de culpa (revisar as falhas para melhorar sistemas e não atribuir culpa individual) e um mandato de automação cortam de forma constante as intervenções manuais que antes dominavam a temporada de declarações, liberando a equipe para melhorar o sistema em vez de ninar cada prazo.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da SRE vem de três fontes: indisponibilidade evitada, menos trabalho operacional e entrega segura mais rápida. A indisponibilidade de um grande serviço pode custar de milhares a milhões por hora em receita perdida, penalidades e remediação, então até ganhos modestos de confiabilidade pagam uma equipe depressa. A redução do toil transforma o custo manual recorrente num investimento único de automação, de modo que o custo total de propriedade cai conforme a escala cresce e não sobe em compasso com ela. Os orçamentos de erro deixam o negócio entregar mais depressa quando a confiabilidade está saudável, capturando o valor de funcionalidades que operações excessivamente cautelosas deixariam na mesa.

O custo de adoção é real. A SRE precisa de engenheiros qualificados, infraestrutura de observabilidade e uma mudança cultural que compete com os prazos de funcionalidades. Mas o custo de não adotar é maior em escala: um número ilimitado de pessoas nas operações, interrupções imprevisíveis, esgotamento e evasão de pessoal e dano à reputação que é difícil de quantificar mas fácil de sofrer. Para defender o caso junto à liderança, enquadrem a SRE como gestão de risco com retornos mensuráveis. Apresentem o custo atual dos incidentes e das operações manuais, as metas de SLO ligadas aos compromissos de negócio e a redução projetada de ambos. Ancorem o argumento no orçamento de erros como uma ferramenta de governança que dá à liderança uma alavanca sobre o compromisso entre confiabilidade e velocidade.

## Antipadrões e armadilhas

- **SRE como operações rebatizadas.** Renomear uma equipe de operações sem o tempo de engenharia, o mandato de automação e a autoridade de recusar não muda nada.
- **Mirar 100 por cento.** Perseguir a confiabilidade perfeita desperdiça dinheiro e bloqueia a entrega por ganhos que os usuários não percebem.
- **SLIs de vaidade.** Medir a CPU do servidor em vez do sucesso visível ao usuário dá números que parecem bons enquanto os usuários sofrem.
- **Orçamentos de erro sem dentes.** Um orçamento que nunca é imposto quando esgotado é só decoração.
- **Toil sem medição.** Se vocês não acompanham o toil, ele consome a equipe em silêncio até nenhum trabalho de melhoria acontecer.
- **SRE como depósito.** As equipes centralizadas que herdam todo serviço instável sem um patamar de prontidão se afogam na dívida técnica alheia.
- **Ignorar os prazos de capacidade.** Presumir que a elasticidade da nuvem é instantânea e infinita convida a escassez justamente nos picos que mais importam.

## Modelo de maturidade

**Nível 1, Iniciar.** As operações são manuais e reativas. Não há SLOs formais, a confiabilidade é questão de opinião e os mesmos incidentes se repetem enquanto o combate a incêndios domina. Qualquer automação é incidental, e ninguém é dono da confiabilidade como preocupação de engenharia.

**Nível 2, Desenvolver.** Alguns serviços têm SLIs e SLOs básicos e monitoramento e alertas rudimentares, mas a prática varia muito entre as equipes. O toil é reconhecido mas não medido, a automação é ad hoc e as revisões pós-incidente acontecem de forma inconsistente. A confiabilidade melhora nos bolsões onde indivíduos a empurram, não porque a organização a exija.

**Nível 3, Padronizar.** Os SLIs, SLOs e uma política de orçamento de erros são documentados e aplicados de modo consistente entre as equipes. O toil é definido e acompanhado, o planejamento de capacidade é rotineiro, existe um modelo de engajamento de SRE com revisões de prontidão de produção e a automação é uma frente de trabalho financiada e não um projeto paralelo. A prática de confiabilidade é escrita e imposta em toda a organização.

**Nível 4, Gerenciar.** O programa de confiabilidade é medido e controlado com dados em relação a linhas de base. A taxa de consumo do orçamento de erros, a porcentagem de toil, o atingimento dos SLOs, o tempo médio de recuperação e os prazos de provisionamento são acompanhados como métricas, revisados numa cadência fixa e usados para cobrar as equipes por suas metas. As violações de orçamento disparam o congelamento combinado, a capacidade é prevista contra modelos de demanda e cada decisão de ir ou não ir repousa em evidências e não em opinião.

**Nível 5, Orquestrar.** A engenharia de confiabilidade é integrada em toda a organização e continuamente melhorada. A política de orçamento de erros é automatizada e respeitada em toda parte, a maioria das operações é de autoatendimento, a capacidade é provisionada de forma proativa e os dados de confiabilidade conduzem compromissos adaptativos entre velocidade e estabilidade. A organização rotineiramente redefine o escopo dos SLOs, aposenta o toil e reequilibra o investimento em confiabilidade conforme o negócio e o quadro de risco mudam.

## Ideias para discussão

- Como uma organização deve definir seus primeiros SLOs quando não tem dados históricos de confiabilidade para ancorá-los?
- Quando o orçamento de erros está esgotado mas um grande lançamento está comprometido, quem tem autoridade para sobrescrever o congelamento, e como essa decisão é registrada?
- Um modelo de SRE centralizado, embutido ou híbrido é o certo para a sua organização, e o que dispararia uma mudança?
- Como vocês valorizam um nove extra de disponibilidade contra as funcionalidades que o mesmo investimento poderia financiar?
- O que conta como toil no seu contexto, e onde fica a linha entre o julgamento manual valioso e a repetição eliminável?
- Como as metas de confiabilidade devem diferir entre os serviços governamentais voltados ao cidadão e as ferramentas corporativas internas?

## Principais conclusões

- A SRE aplica a engenharia de software às operações, tratando a confiabilidade como uma funcionalidade mensurável e financiável.
- Os SLIs, SLOs e SLAs transformam a confiabilidade de opinião em números combinados. Mantenham os SLOs mais rigorosos que os SLAs.
- O orçamento de erros alinha desenvolvedores e operadores ao tornar explícito e pré-negociado o compromisso entre confiabilidade e velocidade.
- Meçam e limitem o toil e tratem a automação como engenharia de primeira classe, para que as operações escalem de forma sublinear.
- Planejem a capacidade a partir de previsões de demanda e respeitem os prazos de provisionamento, especialmente nos picos sazonais.
- Escolham um modelo organizacional de SRE deliberadamente e definam um modelo claro de engajamento e um patamar de prontidão de produção.

## Referências e leitura complementar

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
