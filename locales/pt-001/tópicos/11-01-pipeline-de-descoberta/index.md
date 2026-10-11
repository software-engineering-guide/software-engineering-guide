# 11.1 O pipeline de descoberta

## Visão geral e motivação

O pipeline de descoberta é o fluxo de trabalho que decide **o que construir e por quê**, e define **como será o sucesso**, antes e junto com a entrega. Onde o pipeline de entrega (capítulo 11.2) transforma ideias validadas em software em execução, o pipeline de descoberta transforma problemas, evidências e estratégia num conjunto priorizado e testável de resultados pretendidos. Na prática moderna os dois rodam continuamente e em paralelo, muitas vezes chamados de desenvolvimento de *trilha dupla*, e não como fases sequenciais. A descoberta continua alimentando a entrega com um suprimento pronto de trabalho com risco reduzido e bem enquadrado, e a entrega continua devolvendo à descoberta dados de resultado do mundo real.

Para grandes equipes, um pipeline de descoberta fraco é o modo de falha mais caro do software. Uma equipe com excelente entrega e descoberta pobre constrói a coisa errada com eficiência: entrega rápido, bate suas metas de velocidade e ainda assim não move nenhuma métrica de negócio. O custo é invisível nos painéis de engenharia e enorme no balanço. O pipeline de descoberta é como vocês tornam esse custo visível: obriga as metas a serem explícitas, mensuráveis e falseáveis antes de vocês se comprometerem com grandes investimentos.

Os contextos corporativo e governamental elevam as apostas. As empresas coordenam dezenas de equipes em torno de uma estratégia compartilhada, então metas locais desalinhadas se compõem em portfólios desperdiçados. Os programas governamentais comprometem financiamento público plurianual contra mandatos legislados, em que “construímos o que o contrato dizia” não é defesa se o resultado (cidadãos atendidos, tempos de espera reduzidos, fraude evitada) nunca se materializa. Um pipeline de descoberta disciplinado, expresso por objetivos, medidas e requisitos de qualidade explícitos, é como ambos mantêm a sua intenção auditável.

## Princípios fundamentais

- **Resultados acima de saídas.** Meçam a mudança que criam para os usuários e o negócio, não as funcionalidades que entregam.
- **Tornem a intenção explícita e mensurável.** Uma meta que vocês não conseguem medir é uma opinião que não conseguem gerenciar.
- **Reduzam o risco antes de construir.** O experimento mais barato vence a opinião mais confiante.
- **A descoberta e a entrega rodam continuamente em paralelo**, não como portões sequenciais.
- **Os atributos de qualidade são requisitos, não ideias de última hora.** Confiabilidade, segurança e acessibilidade são descobertas e especificadas, não esperadas.
- **O alinhamento vence a otimização local.** Metas aninhadas conectam o trabalho da equipe à estratégia.
- **Fechem o ciclo.** Os resultados entregues são evidências que reentram na descoberta.

## Recomendações

### Enquadre a direção com OKRs

Usem **[Objetivos e Resultados-Chave](https://en.wikipedia.org/wiki/OKR) (OKRs)** para conectar a estratégia à execução da equipe. Um *Objetivo* é uma declaração qualitativa e inspiradora de um estado final desejado (“Tornar a integração de novos usuários sem esforço”). Os *Resultados-Chave* são o pequeno número (tipicamente 2–4) de resultados mensuráveis que provam que o objetivo está sendo atingido (“Aumentar a ativação em 7 dias de 40% para 60%”; “Reduzir os chamados de suporte de integração em 30%”). Os resultados-chave expressam **resultados**, não tarefas: “entregar o novo assistente” é uma tarefa disfarçada de resultado.

Façam a cascata dos OKRs por *alinhamento*, não por ditado: a liderança define um pequeno número de objetivos da empresa; as equipes propõem resultados-chave e seus próprios objetivos que se encadeiam aos da liderança. Definam-nos numa cadência regular (comumente trimestral com uma moldura anual), revisem-nos no meio do ciclo e avaliem-nos com honestidade no fim. Mantenham-nos separados das avaliações de desempenho: OKRs avaliados para fins de remuneração logo são sabotados por metas fáceis. Vejam o capítulo 10.1 para como os OKRs se conectam à gestão de portfólio e de programas.

### Monitore a saúde com KPIs

Distingam os **[Indicadores-Chave de Desempenho](https://en.wikipedia.org/wiki/Performance_indicator) (KPIs)** dos OKRs. Os OKRs descrevem a *mudança* que vocês querem neste período; os KPIs descrevem a *saúde contínua* que vocês precisam sustentar independentemente do que estejam mudando (disponibilidade, taxa de conversão, custo por transação, satisfação do cliente). Uma métrica pode ser as duas coisas (um KPI que vocês estão tentando ativamente mover vira um resultado-chave), mas a maioria dos KPIs são guardrails que vocês monitoram, não metas para as quais correm.

Classifiquem toda métrica importante como **antecedente** (preditiva e acionável agora, como inscrições em testes) ou **consequente** (confirmatória e lenta, como a receita anual). A descoberta se apoia nos indicadores antecedentes para conduzir antes que os consequentes confirmem. Cuidado com as métricas de vaidade, que sobem de forma confiável mas não predizem nada (visualizações de página brutas, total de usuários registrados); prefiram métricas de razão e de coorte, que resistem à manipulação. Vejam os capítulos 7.3 e 7.4 para a maquinaria de análise e experimentação por trás dessas medidas.

### Especifique explicitamente os atributos de qualidade do sistema

Os requisitos funcionais dizem o que o sistema faz. Os **atributos de qualidade do sistema** (os “-ilidades”: confiabilidade, desempenho, escalabilidade, segurança, acessibilidade, manutenibilidade, operabilidade) dizem quão bem ele deve fazê-lo. Estes são rotineiramente subdescobertos: todos os presumem, ninguém os especifica, e eles surgem como incidentes de produção. Tratem-nos como saída de primeira classe da descoberta. Identifiquem os **requisitos arquiteturalmente significativos** (as exigências de qualidade que moldam materialmente a arquitetura) de cada iniciativa. Quantifiquem-nos (“latência p99 abaixo de 200 ms com 10× a carga atual”; “WCAG (Web Content Accessibility Guidelines) 2.2 AA”; “objetivo de tempo de recuperação de 15 minutos”). E, sempre que puderem, codifiquem-nos como **funções de aptidão** automatizadas (verificações executáveis que verificam continuamente um atributo de qualidade) que o pipeline de entrega possa conferir. Este é o complemento, do lado da descoberta, do capítulo 3.1 (fundamentos de arquitetura) e do capítulo 3.5 (escalabilidade, desempenho, resiliência).

### Torne toda meta SMART

Seja para escrever um resultado-chave, um critério de aceitação ou uma meta de qualidade, apliquem o teste **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)**:

- **Específica (Specific):** nomeia um resultado claro e inequívoco.
- **Mensurável (Measurable):** tem uma métrica e uma fonte da verdade.
- **Atingível (Achievable):** é realista dadas as restrições e as evidências.
- **Relevante (Relevant):** se encadeia a um objetivo superior e ao valor para o usuário.
- **Com prazo (Time-bound):** tem uma data-limite ou de revisão.

“Melhorar o desempenho” falha em todas as letras. “Reduzir o tempo mediano de checkout de 8 s para 3 s para usuários de celular até o fim do T3, medido por monitoramento de usuários reais” passa nas cinco. Os critérios SMART convertem ambição vaga em uma afirmação falseável que a descoberta pode testar e a entrega pode verificar.

### Conduza uma descoberta contínua e guiada por evidências

Estruturem a descoberta como um pipeline repetível, não uma fase única:

1. **Perceber.** Reúnam sinais: pesquisa com usuários, dados de suporte, análises, insumos de mercado e de conformidade.
2. **Enquadrar.** Mapeiem oportunidades (uma *árvore de oportunidade e solução* conecta um resultado desejado às necessidades dos usuários e às soluções candidatas que poderiam movê-lo).
3. **Formular hipóteses.** Declarem as suposições como afirmações falseáveis: “Acreditamos que [mudança] causará [resultado] para [segmento], e saberemos se [medida] se mover.”
4. **Experimentar.** Validem as suposições mais arriscadas com o teste mais barato: entrevistas, protótipos, testes de porta falsa (anunciar uma funcionalidade ainda não construída para medir a demanda real), [experimentos A/B](https://en.wikipedia.org/wiki/A/B_testing) (comparações aleatorizadas de duas variantes, capítulo 7.4).
5. **Decidir.** Perseverar, pivotar ou abandonar, e alimentar os sobreviventes no backlog de entrega com seus critérios de sucesso SMART anexados.

A saída do pipeline de descoberta não é uma lista de funcionalidades; é um fluxo de *apostas validadas e mensuráveis* prontas para a entrega.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| **Metas baseadas em resultado (OKRs)** | Alinha as equipes ao impacto. Dá autonomia no *como* | Difícil de escrever bem. Tentador preencher com tarefas. Atribuição ruidosa |
| **Roteiros de saídas/funcionalidades** | Previsíveis, fáceis de comunicar e de contratar | Recompensam entregar acima do impacto. Escondem o risco da coisa errada |
| **Descoberta inicial pesada** | Reduz o desperdício de construção. Requisitos fortes | Atrasa o início. Risco de paralisia por análise. Suposições ainda não testadas |
| **Descoberta contínua de trilha dupla** | Reduz o risco continuamente. Feedback rápido | Exige capacidade de pesquisa e disciplina. Mais difícil de agendar |
| **Atributos de qualidade explícitos como metas SMART** | Previne surpresas de “-ilidades”. Auditável | Esforço para quantificar. Pode restringir demais a exploração inicial |

A tensão central é **compromisso versus aprendizado**. As empresas, e em especial os governos, muitas vezes precisam de compromissos firmes para orçamento e contratos, o que puxa para roteiros de saídas. Bons resultados precisam de espaço para aprender, o que puxa para OKRs e experimentos. Resolvam assim: comprometam-se firmemente com *problemas e resultados* e segurem as *soluções* com leveza.

## Perguntas para discutir com sua equipe

1. **Quem na sua equipe é de fato dono da descoberta, e tem capacidade para conduzi-la continuamente e não num sprint único?** O desenvolvimento de trilha dupla só funciona quando alguém mantém a trilha de descoberta aberta toda semana e não só no começo de um trimestre. Numa grande organização, a descoberta muitas vezes não tem dono dedicado, então colapsa para quem tem tempo sobrando, que é ninguém, e a equipe cai no padrão de construir. Levem evidências: contem quantas das suas últimas dez funcionalidades passaram por uma hipótese documentada e um teste barato antes da construção, em comparação com as que foram direto para o backlog. Em contextos corporativos e governamentais, em que uma única iniciativa desalinhada pode desperdiçar vários trimestres de equipe, nomeiem um dono de produto ou um trio (produto, design, engenharia) responsável pelo ciclo perceber-enquadrar-formular hipótese-experimentar-decidir. Se ninguém é dono, dotem de pessoal antes de discutir qualquer outra coisa.

2. **Quais das suas iniciativas atuais têm requisitos arquiteturalmente significativos que vocês nunca quantificaram, e vocês poderiam codificar algum como função de aptidão?** Os “-ilidades” (confiabilidade, desempenho, segurança, acessibilidade) são presumidos e depois surgem como incidentes de produção. Percorram cada iniciativa ativa, perguntem quais atributos de qualidade moldam materialmente a arquitetura e conferiram se cada um tem um número e uma fonte da verdade: “p99 abaixo de 200 ms com 10x a carga”, “WCAG 2.2 AA”, “objetivo de tempo de recuperação de 15 minutos”. Para a empresa e o governo, requisitos de acessibilidade ou segurança não quantificados criam exposição jurídica e de auditoria direta. O sinal a trazer são os seus três últimos incidentes: quantos remontaram a um atributo de qualidade que ninguém especificou? Sempre que puderem transformar uma meta numa função de aptidão automatizada que o pipeline de entrega confira, façam-no, porque uma meta especificada mas não imposta deriva.

3. **Da última vez que vocês se comprometeram com uma solução, testaram primeiro a suposição mais arriscada ou a mais fácil?** As equipes validam de modo confiável a suposição com que se sentem mais à vontade e pulam a que de fato mataria a ideia. Para cada iniciativa, listem suas suposições (desejabilidade, viabilidade, exequibilidade) e classifiquem-nas por “quão morta fica esta ideia se estivermos errados aqui”, depois apontem o teste mais barato para o topo dessa lista. Isso importa em escala porque uma equipe confiante e sênior pode comprometer um trimestre de engenharia com uma crença não testada, e o custo permanece invisível até o lançamento. Levem o artefato: a sua última hipótese declarada como “Acreditamos que [mudança] causa [resultado] para [segmento], medido por [métrica]”, e perguntem se vocês a testaram ou só a construíram. Se vocês não conseguem nomear a suposição mais arriscada, não estão prontos para comprometer capacidade de construção.

4. **Quantos dos seus resultados-chave são resultados genuínos, e quantos são tarefas ou datas de entrega vestindo roupa de resultado?** A falha mais comum do planejamento baseado em resultado é preencher os resultados-chave com o trabalho que vocês já planejavam fazer (“lançar o novo assistente”) em vez da mudança que esse trabalho deveria causar (“elevar a ativação em 7 dias de 40% para 60%”). Em escala isso derrota em silêncio todo o propósito: dezenas de equipes relatam verde enquanto nenhuma métrica de negócio se move, porque todos se avaliaram pelo que entregaram. A atração contrária é real: os roteiros de saídas são mais fáceis de comunicar, contratar e prever, que é exatamente por que voltam a se infiltrar. Levem o seu conjunto atual de OKRs e marquem cada resultado-chave como resultado ou saída, depois conferiram se a avaliação dos OKRs está emaranhada com a remuneração, já que resultados atados ao pagamento são sabotados depressa. Para portfólios corporativos e governamentais, em que o financiamento é comprometido contra metas declaradas, um roteiro de saídas sem medida de resultado é um achado de auditoria à espera de acontecer; insistam que cada iniciativa se comprometa firmemente com um problema e um resultado mensurável enquanto segura a solução com leveza.

5. **Quais dos seus KPIs continuariam subindo mesmo que o produto estivesse piorando, e que guardrails protegem as métricas que vocês estão ativamente tentando mover?** Toda métrica que vocês elevam a meta convida a [Lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law): uma vez que uma medida vira o objetivo, as pessoas otimizam a medida e não a coisa que ela devia representar. As métricas de vaidade (visualizações de página brutas, usuários registrados acumulados) sobem de modo confiável e não predizem nada, enquanto um resultado-chave perseguido sem guardrails pode ser atingido degradando algo que vocês nunca nomearam. A tensão é que os indicadores antecedentes deixam conduzir cedo mas são ruidosos e manipuláveis, enquanto os consequentes são confiáveis mas confirmam tarde demais para agir. Levem o seu inventário de métricas classificado como antecedente ou consequente e como meta ou guardrail, e testem sob estresse cada meta perguntando “como uma equipe esperta poderia atingir este número piorando o produto”. Em contextos regulados e públicos, publiquem os guardrails ao lado das metas, porque um órgão de supervisão que vê apenas a métrica de manchete não distingue valor público genuíno de um número manipulado.

6. **Quando a entrega põe algo no ar, como o resultado do mundo real de fato reentra na descoberta, ou o ciclo permanece aberto?** O desenvolvimento de trilha dupla só se compõe se os resultados entregues fluírem de volta como evidência para a próxima rodada; quando o ciclo permanece aberto, as equipes entregam, comemoram e nunca descobrem se a aposta compensou, de modo que as mesmas suposições não testadas se repetem. Numa grande organização o caminho do feedback é onde a responsabilidade mais provavelmente cai numa fresta: a entrega é dona do lançamento, a análise é dona do painel e ninguém é dono de comparar o resultado-chave prometido com o observado. Levem as suas últimas dez iniciativas entregues e perguntem, para cada uma, se alguém conferiu a métrica de resultado contra a meta SMART original e se essa verificação mudou uma decisão posterior. Para programas corporativos e governamentais que comprometem financiamento plurianual, nomeiem a cadência e o dono para aposentar ou redefinir o escopo das funcionalidades que não moveram sua métrica, porque uma funcionalidade entregue que ninguém revisita vira custo permanente sem revisão responsável.

## Perspectiva por setor

**Startup.** Com uma equipe minúscula e pouco fôlego, o seu pipeline de descoberta é deliberadamente leve mas nunca pulado: um dia de entrevistas com clientes e um teste de porta falsa custam quase nada diante das semanas que uma construção errada queima. Escolham um indicador antecedente que represente o seu valor central, declarem cada aposta como uma única hipótese falseável e matem as ideias antes de escrever código e não depois. OKRs formais são exagero com cinco pessoas; um resultado mensurável e honesto por ciclo basta para impedir que a velocidade vire movimento sem progresso.

**Pequena empresa.** Vocês provavelmente não têm pesquisador ou analista de produto dedicado, então tratem a descoberta como hábito e não como cargo: algumas conversas estruturadas com clientes reais e uma métrica simples que vocês já coletam. A questão de construir versus comprar domina, porque a maioria dos atributos de qualidade (confiabilidade, segurança, acessibilidade) é mais barata de obter de um fornecedor reputado do que de especificar e impor por conta própria. Escrevam uma ou duas metas SMART para poder dizer se uma ferramenta comprada ou uma pequena construção de fato moveu o resultado, e evitem comprometer orçamento escasso com funcionalidades que ninguém validou que são desejadas.

**Grande empresa.** A escala transforma a descoberta num problema de coordenação entre dezenas de equipes: sem uma cadência compartilhada de OKRs e uma definição comum de “resultado”, as metas locais derivam e se duplicam, e apostas desalinhadas se compõem em portfólios desperdiçados. Padronizem como os requisitos arquiteturalmente significativos são quantificados e codifiquem-nos como funções de aptidão para que os atributos de qualidade sejam governados e não presumidos. Gerenciem a descoberta como um portfólio com critérios explícitos de encerramento e um ciclo que devolve as métricas de resultado entregues ao ciclo seguinte, para que a liderança conduza pelo impacto e não por um backlog de funcionalidades.

**Governo.** A contratação e o financiamento plurianual exigem compromissos firmes, que puxam com força para contratos de saídas, mas o valor público vive nos resultados: cidadãos atendidos, tempos de espera cortados, ônus reduzido. Enquadrem os programas em torno de resultados públicos mensuráveis e de atributos de qualidade inegociáveis (acessibilidade WCAG, linguagem simples, segurança) e façam das evidências de descoberta, inclusive testes de usabilidade com usuários de tecnologia assistiva, parte do registro que os órgãos de supervisão possam auditar. Definam o sucesso como resultados para o contribuinte ou o cidadão e não como módulos entregues, para que “construímos o que o contrato dizia” nunca possa substituir um resultado que nunca se materializou.

## Exemplos

**Startup.** Uma equipe de quatro pessoas em fase semente, que constrói um aplicativo de agendamento para salões de cabeleireiro, é tentada a construir um widget de reserva online porque alguns usuários barulhentos pediram. Em vez disso, fazem uma semana de descoberta: cinco entrevistas com donos, um botão de porta falsa “Reservar online” no site de marketing e um único indicador antecedente (a porcentagem de compromissos que terminam em falta). As entrevistas e os dados de cliques revelam que as faltas, e não a reserva, são a dor real, então escrevem um resultado-chave SMART (cortar as faltas de 22% para menos de 10% nos salões-piloto neste trimestre) e entregam primeiro uma pequena funcionalidade de depósito e lembrete, matando o widget de reserva antes de escrever uma linha dele.

**Grande empresa.** O grupo de pagamentos de um banco de varejo substitui um roteiro de contagem de funcionalidades por três OKRs trimestrais, um deles “Fazer os pagamentos do dia a dia parecerem instantâneos”, com resultados-chave para o tempo de confirmação de transferência p95, a taxa de sucesso na primeira tentativa e os contatos de suporte relacionados a pagamentos. Os atributos de qualidade do sistema são especificados de antemão (99,99% de disponibilidade, confirmação em menos de um segundo, escopo do PCI-DSS (Payment Card Industry Data Security Standard) minimizado) e ligados à entrega como funções de aptidão. A descoberta conduz entrevistas semanais com clientes e testes de porta falsa antes de comprometer a engenharia. Duas funcionalidades candidatas são mortas na descoberta por não moverem os indicadores antecedentes (poupando uma estimativa de dois trimestres de esforço de construção), enquanto uma correção de latência menor e sem glamour move mais o resultado-chave.

**Governo.** Uma agência tributária nacional que moderniza a declaração online define um objetivo de programa de “Reduzir o ônus da declaração para os contribuintes comuns”, com resultados-chave SMART: cortar o tempo mediano para declarar de 45 para 20 minutos, elevar a conclusão bem-sucedida por autoatendimento de 60% para 85% e cumprir a WCAG 2.2 AA e padrões de linguagem simples como atributos de qualidade inegociáveis. Os KPIs (disponibilidade durante a temporada de declarações, volume do centro de atendimento) são monitorados como guardrails. A descoberta usa testes de usabilidade moderados com contribuintes reais, inclusive usuários de tecnologia assistiva, antes de cada lançamento. Como o sucesso é definido como resultados para o contribuinte e não como módulos entregues, o programa pode mostrar aos órgãos de supervisão valor público mensurável, não apenas gasto.

## Justificativa de negócio: motivações, ROI e TCO

O retorno de um pipeline de descoberta é dominado pelo **desperdício evitado**. A experiência do setor, ecoada em programas de experimentos controlados em grandes empresas de tecnologia, encontra repetidamente que uma grande parcela das funcionalidades construídas, muitas vezes citada em torno da metade ou mais, não produz melhoria mensurável ou prejudica ativamente a métrica-alvo. Suponham que até um quarto da capacidade de construção de uma equipe vá para ideias que a descoberta teria matado barato. O pipeline então se paga muitas vezes: uma semana de pesquisa com usuários e um teste de porta falsa custam quase nada diante de um trimestre de engenharia, mais o ônus contínuo de manutenção de uma funcionalidade não usada.

O enquadramento do **[custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO) importa porque as funcionalidades não validadas não são gratuitas depois do lançamento. Toda funcionalidade entregue carrega custos perpétuos: manutenção, testes, superfície de segurança, suporte e carga cognitiva (capítulo 10.4). Matar uma ideia ruim na descoberta evita não só o custo de construção, mas toda a cauda da propriedade. Os atributos de qualidade explícitos seguem a mesma lógica: especificar confiabilidade e acessibilidade como metas SMART de antemão é muito mais barato que adaptá-las depois de uma queda, de uma violação ou de um processo.

Para defender o caso junto à liderança, desloquem a conversa de “quanto estamos entregando” para “quanto estamos movendo as métricas que importam” e mostrem alguns exemplos concretos de funcionalidades caras que não moveram nada. O custo de adoção é modesto (capacidade de pesquisa, uma cadência de OKRs e a disciplina de escrever critérios SMART), e o principal risco de *não* adotar é silencioso, não contado e composto.

## Antipadrões e armadilhas

- **Roteiros de funcionalidades disfarçados de estratégia:** listas de saídas sem resultado nem medida declarados.
- **Resultados-chave que são tarefas:** “lançar X” em vez de “melhorar Y em Z”.
- **Teatro de OKRs:** metas escritas, arquivadas e nunca revisadas nem avaliadas.
- **OKRs sabotados ou heroicos:** metas definidas para garantir 100% (nada se aprende) ou um desafio fantasioso sem plano.
- **Atributos de qualidade não especificados:** confiabilidade, segurança e acessibilidade presumidas em vez de quantificadas, depois descobertas em produção.
- **Métricas de vaidade:** medidas que sempre sobem e não predizem nada.
- **Descoberta como fase única:** um “sprint de descoberta” no início, depois nenhuma validação continuada.
- **Construir a solução antes de testar a suposição:** pular o experimento mais barato porque a equipe está confiante.
- **Fixação em métricas e [Lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law):** uma vez que uma medida vira a meta, deixa de ser uma boa medida; equilibrem com KPIs guardrail.

## Modelo de maturidade

- **Nível 1, Iniciar:** O trabalho é definido como funcionalidades num roteiro e o sucesso é “entregamos”. Não há medidas explícitas de resultado nem metas de qualidade; a descoberta acontece por acaso, se acontece, e as decisões são conduzidas pela opinião mais barulhenta.
- **Nível 2, Desenvolver:** OKRs e KPIs existem para algumas equipes e não para outras; as metas são declaradas mas muitas vezes em formato de saída; os atributos de qualidade são nomeados mas não quantificados. Uma equipe pode conduzir um “sprint de descoberta” único e depois parar de validar quando a construção começa, de modo que a prática é real mas inconsistente na organização.
- **Nível 3, Padronizar:** Uma cadência consistente de OKRs alinhada à estratégia, resultados-chave SMART e atributos de qualidade especificados e testáveis são documentados e esperados em toda a organização. A descoberta é uma atividade reconhecida e dotada de pessoal, com hipóteses e experimentos, e os requisitos arquiteturalmente significativos são identificados para cada iniciativa em vez de presumidos.
- **Nível 4, Gerenciar:** O portfólio é medido em relação a linhas de base. Os indicadores antecedentes e consequentes, a taxa de acerto da descoberta e o resultado que cada aposta entregue de fato moveu são acompanhados contra sua meta SMART; as hipóteses são avaliadas com base em evidências e os critérios de encerramento são impostos; as funções de aptidão relatam continuamente a conformidade dos atributos de qualidade, de modo que o desvio de uma meta especificada de confiabilidade, desempenho ou acessibilidade é pego com dados e não num incidente.
- **Nível 5, Orquestrar:** A descoberta contínua de trilha dupla é integrada ao portfólio, ao risco e ao orçamento; as apostas validadas fluem de modo estável para a entrega e as métricas de resultado voltam automaticamente para conduzir a próxima rodada. Os indicadores antecedentes conduzem o investimento, e a organização rotineiramente aposenta, redefine o escopo e reequilibra iniciativas com base em evidências, adaptando o próprio pipeline conforme o mercado e as métricas mudam.

## Ideias para discussão

1. Olhem o seu roteiro atual: quantos itens declaram um resultado mensurável em comparação com apenas uma funcionalidade a entregar?
2. Quais dos resultados-chave da sua equipe são na verdade tarefas disfarçadas, e como vocês os reescreveriam?
3. De que atributos de qualidade do sistema o seu produto depende que nunca foram explicitamente quantificados?
4. Qual é o experimento mais barato que poderia ter matado a sua última funcionalidade fracassada antes de vocês construí-la?
5. Como vocês resolvem a tensão entre os compromissos firmes que o orçamento e a contratação exigem e o aprendizado que bons resultados requerem?
6. Quais dos seus KPIs continuariam subindo mesmo que o produto estivesse piorando?

## Principais conclusões

- O pipeline de descoberta decide *o quê* e *por quê*, e define o sucesso **antes** de a entrega comprometer recursos.
- Usem **OKRs** para a mudança que querem, **KPIs** para a saúde que sustentam e classifiquem as métricas como antecedentes ou consequentes.
- Tratem os **atributos de qualidade do sistema** como requisitos explícitos, quantificados e testáveis, não como suposições.
- Tornem **SMART** toda meta, resultado-chave e critério de aceitação.
- Conduzam a descoberta **continuamente e em paralelo** com a entrega; validem as suposições mais arriscadas de forma barata.
- O ROI dominante é o **desperdício evitado**: tanto o custo de construção quanto o TCO perpétuo das funcionalidades não usadas.
- Fechem o ciclo: as **métricas de resultado** entregues (capítulo 11.2) são a evidência principal para a próxima rodada de descoberta.

## Referências e leitura complementar

- *Measure What Matters*, by John Doerr (on OKRs).
- *Radical Focus*, by Christina Wodtke (on OKRs in practice).
- *Continuous Discovery Habits*, by Teresa Torres (opportunity-solution trees, dual-track discovery).
- *Inspired* and *Empowered*, by Marty Cagan (product discovery and outcome teams).
- *Lean Analytics*, by Alistair Croll and Benjamin Yoskovitz (leading indicators, vanity metrics).
- *The Lean Startup*, by Eric Ries (build-measure-learn, validated learning).
- *Escaping the Build Trap*, by Melissa Perri (outcomes over outputs).
- *Outcomes Over Output*, by Joshua Seiden.
- *Software Architecture in Practice*, by Bass, Clements, Kazman (quality attributes).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): origin of SMART criteria.
