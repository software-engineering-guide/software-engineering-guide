# 10.7 Agile

## Visão geral e motivação

O [Agile](https://en.wikipedia.org/wiki/Agile_software_development) é uma mentalidade para entregar software (e valor) de modo iterativo, incremental e em colaboração próxima com as pessoas que vão usá-lo. Codificado em 2001 no *Manifesto para o Desenvolvimento Ágil de Software*, é mais bem entendido não como um processo, mas como um conjunto de **valores e princípios**: priorizar indivíduos e interações, software funcionando, colaboração com o cliente e resposta a mudanças, acima dos padrões pesados em planos, em contratos e em documentação que vieram antes. Frameworks como o [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), o [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) e a [Programação Extrema](https://en.wikipedia.org/wiki/Extreme_programming) (XP) são *implementações* dessa mentalidade. São pontos de partida úteis, mas não são a mentalidade em si. Este capítulo complementa o capítulo 1.4 (formas de trabalhar, que examina os métodos em termos amplos) aprofundando especificamente o Agile.

O Agile é movido pela mesma força que anima os pipelines de descoberta e de entrega (capítulos 11.1–11.2): os requisitos de software são *descobertos*, não plenamente conhecidos de antemão, e o mundo muda mais depressa do que um plano longo consegue absorver. A entrega de uma vez só, que planeja tudo primeiro, repetidamente produz sistemas atrasados, acima do orçamento e, pior de tudo, errados, porque todo o aprendizado chega no fim, quando é mais caro agir sobre ele. A aposta central do Agile é simples: ciclos curtos de construir software real e funcionando e obter retorno real vencem ciclos longos de especulação. Bem feito, ele reduz o risco continuamente em vez de adiá-lo.

Para grandes equipes, empresas e governos, o Agile é ao mesmo tempo poderoso e frequentemente deturpado. As empresas o adotam em centenas de equipes e muitas vezes o reduzem a ritual (“agora fazemos reuniões diárias”) sem mudar como as decisões são tomadas nem como o valor é medido. O governo abraçou o Agile deliberadamente, porque a entrega iterativa e centrada no usuário demonstravelmente reduz o risco dos grandes programas públicos: o U.S. Digital Service e seu *Digital Services Playbook*, o Government Digital Service do Reino Unido e o Service Standard e as reformas de contratação ágil surgiram em parte como resposta a fracassos notórios da [cascata](https://en.wikipedia.org/wiki/Waterfall_model). O prêmio é real. Também o é o modo de falha do “agile só no nome”.

## Princípios fundamentais

- **Valorizem os quatro valores do Manifesto** (pessoas, software funcionando, colaboração e capacidade de resposta) acima dos artefatos de processo.
- **Entreguem software funcionando com frequência** em pequenos incrementos. Software funcionando é a principal medida de progresso.
- **Acolham a mudança**, mesmo tardia. A adaptabilidade é uma funcionalidade, não uma falha.
- **Construam em torno de equipes motivadas, empoderadas e autoorganizadas.**
- **Colaborem continuamente com usuários e partes interessadas.**
- **Reflitam e melhorem** numa cadência regular.
- **Sustentem um ritmo humano** e a excelência técnica: velocidade sem ofício colapsa.

## Recomendações

### Ancore-se em valores e princípios, não em cerimônias

A recomendação mais importante do Agile é começar pelo *porquê*. Uma equipe que faz uma reunião diária, uma revisão de sprint e uma retrospectiva, mas ainda se compromete com escopo fixo numa data fixa, esconde as más notícias e nunca muda o plano, não é ágil. É cascata com reuniões. Usem os doze princípios como lista de verificação da agilidade genuína. Vocês estão entregando software funcionando com frequência? Conseguem acolher uma mudança na próxima iteração? A equipe decide *como* fazer o trabalho? O cliente está de fato no circuito? Se as cerimônias não produzem esses resultados, consertem os resultados, não as cerimônias.

### Escolha um framework como ponto de partida, não como religião

Escolham um framework que se ajuste ao trabalho e adaptem-no:

- **Scrum:** sprints com tempo fixo, um backlog priorizado e papéis definidos (dono do produto, scrum master, desenvolvedores). Bom para a entrega de funcionalidades com um dono de produto claro. Fraco quando o trabalho é muito guiado por interrupções.
- **Kanban:** fluxo contínuo com limites explícitos de trabalho em andamento (WIP) e um sistema puxado. Bom para suporte, operações e chegadas imprevisíveis (e diretamente fundamentado em teoria do fluxo e das filas, vejam os capítulos 11.2, 11.3). Limitar o WIP encurta o prazo de entrega ([Lei de Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Programação Extrema (XP):** práticas de engenharia incluindo [desenvolvimento guiado por testes](https://en.wikipedia.org/wiki/Test-driven_development), [programação em par](https://en.wikipedia.org/wiki/Pair_programming), [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration), refatoração e pequenos lançamentos. A espinha dorsal técnica que torna sustentável qualquer framework.
- **Scrumban** e misturas: combinações pragmáticas a que muitas equipes maduras convergem.

Os frameworks são andaimes. Mantenham o que ajuda, descartem o que não ajuda e nunca deixem o “o framework manda” se sobrepor ao “os princípios dizem por quê”.

### Insista na excelência técnica

O Agile sem disciplina de engenharia degrada-se depressa em produção rápida de código impossível de manter, o “dark scrum”, em que as equipes correm em sprints para um atoleiro de defeitos e de [dívida técnica](https://en.wikipedia.org/wiki/Technical_debt). As práticas de XP não são extras opcionais. A integração contínua (capítulo 8.1), os testes automatizados (capítulo 2.4), a refatoração, o desenvolvimento baseado em trunk (capítulo 2.6) e o projeto limpo (capítulo 2.2) são o que permite a uma equipe continuar mudando o software de modo barato, que é toda a premissa da agilidade. O ritmo sustentável importa pela mesma razão: equipes esgotadas não conseguem sustentar a qualidade nem a capacidade de resposta.

### Escale com cuidado e prefira desescalar

Os frameworks de escala, como o SAFe (Scaled Agile Framework), o LeSS, o Nexus e o Scrum@Scale, coordenam muitas equipes rumo a metas compartilhadas. Podem ajudar, mas trazem um alerta (ecoando o capítulo 1.4): os frameworks pesados de escala muitas vezes reintroduzem exatamente o comando e controle e a sobrecarga de plano pesado que o Agile pretendia remover. Antes de adotar um framework grande, tentem *desescalar*. Organizem-se em torno de equipes independentes alinhadas ao fluxo, com propriedade clara e dependências mínimas entre equipes (capítulo 1.2), para precisar de menos maquinaria de coordenação desde o início. Onde a coordenação é genuinamente exigida, acrescentem a estrutura mais leve que funcione e liguem-na a resultados (OKRs, objetivos e resultados-chave, capítulo 11.1) e não a produção.

### Torne a agilidade real em contextos corporativos e governamentais

A entrega adaptativa e as restrições institucionais podem coexistir, mas isso exige projeto deliberado:

- **Governança híbrida:** um núcleo adaptativo de entrega dentro de uma casca preditiva de financiamento e de conformidade (capítulo 10.6), para que a iteração satisfaça a supervisão em vez de brigar com ela.
- **Contratação ágil:** contratos modulares e baseados em resultados e incrementos mais curtos em vez de um megacontrato de escopo fixo. É onde o Agile do setor público mais costuma ter sucesso ou fracassar.
- **Conformidade ao longo do caminho:** embutam auditoria, acessibilidade (capítulo 5.3) e segurança (capítulo 4.1) no incremento por automação e funções de aptidão (verificações automatizadas que verificam continuamente propriedades arquiteturais e de qualidade; capítulos 8.5, 1.6) e não num portão tardio.
- **Acesso real ao usuário:** o mais difícil e mais importante. As equipes precisam de contato genuíno com cidadãos ou clientes, que as regras de contratação e de segurança muitas vezes obstruem.

### Melhore continuamente, e falem sério

A retrospectiva é o motor de melhoria do Agile, e é inútil se não produz mudança. Rodem retrospectivas que gerem um pequeno número de ações concretas e com dono e de fato concluam-nas antes da seguinte. Meçam resultados (a mudança moveu um resultado-chave? vejam o capítulo 11.1) e fluxo (os prazos de entrega estão encolhendo? vejam os capítulos 11.2, 11.3). Não meçam a velocidade: ela é um sinal de capacidade que vira mentira no instante em que vocês a usam como meta de produtividade.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| **Agile (adaptativo)** | Retorno rápido. Absorve a mudança. Valor cedo e contínuo | Mais difícil fixar escopo e custo de antemão. Exige cliente engajado e disciplina |
| **Cascata (preditiva)** | Escopo previsível. Amigável a contratos e auditorias | Retorno tardio. Risco de tudo de uma vez. Mau ajuste para requisitos incertos |
| **Scrum** | Cadência, papéis, foco. Amplamente compreendido | Sobrecarga de cerimônia. Tem dificuldade com trabalho guiado por interrupções |
| **Kanban** | Fluxo, limites de WIP, flexível. Ótimo para operações | Menos estrutura. Exige disciplina para manter os limites |
| **Escala pesada (SAFe)** | Coordena muitas equipes. Familiar a grandes organizações | Pode reintroduzir comando e controle. Pesada em cerimônia |
| **Desescalar / autonomia das equipes** | Menos sobrecarga de coordenação. Equipes mais rápidas | Exige baixo acoplamento e forte plataforma e propriedade |

A tensão definidora é **adaptabilidade versus previsibilidade**, e o equívoco clássico é achar que o Agile significa “sem plano”. Não significa. Significa planejar continuamente e se comprometer com *resultados e cadência* enquanto se deixa o *escopo* flexionar. A outra armadilha recorrente é tratar o Agile como *apenas* processo (cerimônias) ou *apenas* engenharia (XP). Ele precisa de ambos.

## Perguntas para discutir com sua equipe

1. **No seu contexto corporativo ou governamental, os seus contratos são modulares e baseados em resultados, ou a entrega está trancada dentro de um megacontrato de escopo fixo?** A contratação ágil é onde a agilidade do setor público mais costuma ter sucesso ou fracassar, porque um único contrato de preço fixo e escopo fixo força a cascata seja qual for o nome que as equipes de entrega dão às suas reuniões. Contratos modulares e baseados em resultados, com incrementos mais curtos, deixam o escopo flexionar para um núcleo valioso dentro de um financiamento fixo, que é exatamente o padrão por trás dos sucessos modernos do setor público e o antídoto aos fracassos passados de tudo de uma vez. Levem evidências: olhem os seus contratos atuais e perguntem se um fornecedor é pago por software funcionando demonstrado ou por um escopo fixo aprovado anos atrás. A resposta deve moldar como vocês estruturam a próxima contratação muito mais do que o framework que as suas equipes adotam internamente. Vocês não conseguem ser adaptativos na entrega enquanto o contrato impõe um go-live distante, de tudo ou nada.

2. **Auditoria, acessibilidade e segurança estão embutidas em cada incremento por automação, ou acopladas como um portão tardio?** A conformidade ao longo do caminho é o que permite à entrega adaptativa coexistir com as restrições institucionais: embutam as verificações no incremento por automação e funções de aptidão em vez de guardá-las para uma correria pré-lançamento. Um portão tardio de conformidade reintroduz o risco de tudo de uma vez que o Agile existe para remover, porque os problemas caros surgem no fim, quando são mais difíceis de consertar. Levem evidências: para o seu último incremento, conferiram se a acessibilidade, a segurança e a evidência de auditoria foram verificadas automaticamente no pipeline ou adiadas para uma revisão manual antes do lançamento. A resposta deve empurrar essas propriedades para verificações automatizadas contínuas, para que a supervisão seja satisfeita pelo ato de construir e não por uma fase separada. Isso também mantém honesto um programa regulado entre as auditorias e não só nas semanas antes de uma.

3. **Como vocês saberiam se as suas equipes estão correndo em sprints para a dívida técnica, e o que protege o ritmo sustentável sob a pressão do lançamento?** O Agile sem disciplina de engenharia degrada-se em dark scrum, em que as equipes correm rápido para um atoleiro de defeitos e de código impossível de manter, e equipes esgotadas não conseguem sustentar a qualidade nem a capacidade de resposta. As práticas de XP (integração contínua, testes automatizados, refatoração, desenvolvimento baseado em trunk) são o que permite a uma equipe continuar mudando o software de modo barato, que é toda a premissa da agilidade, então não são extras opcionais a trocar quando uma data se aproxima. Levem evidências: acompanhem se os prazos de entrega estão encolhendo ou crescendo, se as taxas de defeitos estão subindo e se a equipe está trabalhando em silêncio mais horas para cumprir cada sprint. A resposta deve tornar a excelência técnica e o ritmo humano inegociáveis, porque a velocidade comprada sacrificando o ofício colapsa em poucas iterações. Meçam fluxo e resultados, nunca a velocidade como meta, porque no instante em que vocês fazem de um sinal de capacidade um objetivo de produtividade ele vira mentira.

4. **Antes de recorrerem a um framework pesado de escala, vocês tentaram reduzir as dependências entre equipes que criam, para começar, a necessidade de coordenar?** Isso importa mais para uma grande organização, porque o reflexo quando muitas equipes precisam entregar juntas é comprar um framework como o SAFe, o LeSS ou o Scrum@Scale, e a maquinaria pesada de escala muitas vezes contrabandeia de volta o comando e controle e a sobrecarga de plano pesado que o Agile existe para remover. A consideração contrária é real: alguma coordenação é genuinamente exigida, e desescalar em equipes independentes alinhadas ao fluxo exige baixo acoplamento, propriedade clara e uma plataforma madura o bastante para permitir que as equipes se sirvam sozinhas, o que vocês talvez ainda não tenham. Levem evidências à discussão: mapeiem as dependências reais que forçam as equipes a esperar umas pelas outras e perguntem quantas sobreviveriam a um redesenho deliberado das fronteiras de equipe e da propriedade de serviços. Em programas corporativos e governamentais, em que um organograma de dezenas de equipes é comum, a pergunta honesta é se vocês estão acrescentando estrutura de coordenação para compensar uma arquitetura e um desenho de equipes que poderiam, em vez disso, simplificar, para precisar de menos coordenação.

5. **As suas equipes têm contato genuíno e repetido com os cidadãos ou clientes para quem constroem, ou o retorno chega filtrado por intermediários?** A colaboração com o cliente é um dos quatro valores do Manifesto, e as iterações sem contato real com o usuário otimizam em silêncio a coisa errada, que é a falha mais cara que o Agile deveria prevenir. A tensão é que o acesso direto é difícil de arranjar em escala e muitas vezes é obstruído pelas mesmas regras de contratação, privacidade e segurança que as organizações grandes e públicas precisam honrar, então o caminho fácil é substituí-lo por um intermediário: um analista de negócio, um comitê de partes interessadas ou o slide de pesquisa do trimestre passado. Levem evidências: para os seus últimos incrementos, contem quantos foram validados com um usuário real de fato usando o software e quantos repousaram na opinião de alguém sobre o que os usuários querem. Para um serviço governamental, acrescentem se os seus testes de usabilidade alcançaram as pessoas mais afetadas, incluindo usuários de tecnologia assistiva e os de baixa confiança digital, porque um serviço público que só funciona para a maioria confiante falhou com a sua obrigação de prestar contas ainda que toda cerimônia tenha corrido no prazo.

6. **As suas equipes são financiadas e governadas em torno de resultados e cadência, ou em torno de um escopo fixo que força a cascata em silêncio por trás das cerimônias?** Esta é a diferença entre agilidade real e agile falso, e é decidida acima da equipe, em como o dinheiro é liberado e como o sucesso é reportado, não em se as reuniões diárias acontecem. A pressão contrária é que as funções de finanças, de portfólio e de supervisão são construídas para aprovar um escopo fixo contra um orçamento fixo com anos de antecedência, e pedir-lhes que financiem um resultado com escopo flexível parece uma perda de controle a que resistirão. Levem evidências: rastreiem como uma iniciativa atual foi financiada e sobre o que ela reporta e confiram se as equipes são medidas por resultados entregues e fluxo ou por pontos de história e aderência a um escopo aprovado há muito tempo. Em contextos corporativos e governamentais, liguem isso diretamente à casca de financiamento e de conformidade (capítulo 10.6): se o dinheiro está comprometido com um go-live distante, de tudo ou nada, as equipes não conseguem ser adaptativas por mais fielmente que executem os rituais, e a correção pertence ao modelo de governança e não às equipes de entrega.

## Perspectiva por setor

**Startup.** Vivam os valores e pulem a discussão sobre frameworks. Entreguem uma fatia funcionando a usuários reais toda semana, sentem-se perto o bastante dos fundadores e dos primeiros clientes para o retorno chegar diariamente e acolham uma mudança de direção no instante em que a evidência disser que a aposta atual está errada. O seu recurso mais escasso é a atenção da engenharia, então protejam a excelência técnica (integração contínua, testes automatizados, desenvolvimento baseado em trunk) mesmo sob a pressão do lançamento, porque essa disciplina é o que mantém vocês capazes de mudar de rumo barato na semana que vem.

**Pequena empresa.** Sem coach ágil e com orçamento apertado, tratem o Agile como um punhado de hábitos e não como um programa de transformação que vocês mantêm com equipe: um ciclo semanal curto, um quadro visível com limites de trabalho em andamento e uma melhoria concreta por semana que vocês de fato terminem. Apoiem-se no Kanban, que precisa de pouca cerimônia e se ajusta a trabalho guiado por interrupções, e adotem as práticas embutidas nas ferramentas que vocês já compram em vez de montar um processo pesado. Julguem o esforço por se vocês estão entregando software útil aos clientes com mais frequência, não por quão de perto imitam o Scrum.

**Grande empresa.** O problema é coordenar muitas equipes sem reintroduzir o comando e controle. Prefiram desescalar, isto é, reduzir as dependências entre equipes por um desenho de equipes alinhadas ao fluxo e uma plataforma sólida, antes de adotar um framework pesado de escala. Financiem e governem em torno de resultados (OKRs) e cadência e não de escopo anual fixo e pontos de história, façam das práticas de engenharia estilo XP algo inegociável entre as equipes e gerenciem a entrega como um portfólio com métricas de fluxo e medidas de resultado para que os grupos melhorem com base em evidências e não em ritual.

**Governo.** A contratação, a transparência e a prestação de contas públicas moldam toda escolha. Estruturem contratos modulares e baseados em resultados, com incrementos mais curtos, em vez de um megacontrato de escopo fixo, já que a contratação ágil é onde a agilidade do setor público mais costuma ter sucesso ou fracassar. Embutam auditoria, acessibilidade e segurança em cada incremento por automação para que a supervisão seja satisfeita pelo ato de construir, publiquem o progresso e a evidência de valor público aos órgãos de supervisão e lutem por acesso genuíno aos cidadãos (incluindo usuários de tecnologia assistiva) a cada iteração, porque é a restrição que mais costuma ser negociada.

## Exemplos

**Startup.** Uma startup de cinco pessoas pula a discussão sobre cerimônias e vive os valores do Agile diretamente. Entrega uma fatia funcionando a usuários reais toda semana, senta-se perto o bastante dos fundadores e dos primeiros clientes para o retorno chegar diariamente e acolhe uma mudança de direção na semana seguinte quando a evidência diz que a aposta atual está errada. A equipe se recusa a trocar a excelência técnica por velocidade, então a integração contínua, os testes automatizados e o desenvolvimento baseado em trunk são inegociáveis mesmo sob a pressão do lançamento, e cada retrospectiva de sexta produz uma mudança concreta que a equipe de fato termina antes da seguinte. Nunca acompanha a velocidade como meta, medindo em vez disso se o trabalho entregue moveu a ativação e se os prazos de entrega estão encolhendo.

**Grande empresa.** A transformação de 60 equipes de uma empresa de telecomunicações inicialmente “faz Scrum” mas não vê melhoria. As equipes ainda recebem escopo anual fixo e reportam a velocidade. Uma reinicialização refoca nos princípios: OKRs trimestrais substituem mandatos de funcionalidade, as equipes são reorganizadas para reduzir dependências entre equipes (desescalar) e as práticas de XP (CI, TDD, desenvolvimento baseado em trunk) tornam-se inegociáveis. Os prazos de entrega caem, os defeitos diminuem e, de modo crucial, o negócio começa a medir resultados e não pontos de história, ligando a entrega ágil ao pipeline de descoberta (capítulo 11.1).

**Governo.** Uma equipe de serviço digital reconstrói uma aplicação de benefícios voltada ao cidadão usando o Agile dentro de uma casca de governança híbrida: incrementos de duas semanas entregando software funcionando e testado com usuários, acessibilidade e segurança embutidas em cada incremento e contratação modular substituindo um único contrato de preço fixo. Testes reais de usabilidade com cidadãos (incluindo usuários de tecnologia assistiva) a cada iteração pegam problemas que o antigo processo em cascata teria entregue. O programa entrega cedo um serviço utilizável e mostra valor público mensurável aos órgãos de supervisão. Esse é o padrão por trás dos sucessos modernos do setor público e o antídoto aos fracassos passados de tudo de uma vez.

## Justificativa de negócio: motivações, ROI e TCO

O retorno do Agile vem da **redução de risco e da realização de valor mais rápida**. Ao entregar software funcionando cedo e com frequência, as equipes transformam a incerteza em evidência continuamente, pegando falhas de coisa errada e de “não vai funcionar” enquanto são baratas e não num go-live distante e caro. A pesquisa por trás da entrega moderna (os achados do DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), no capítulo 11.2) mostra que as práticas que o Agile promove (lotes pequenos, lançamentos frequentes, retorno rápido, excelência técnica) correlacionam com melhor entrega *e* estabilidade *e* desempenho organizacional. Os incrementos iniciais também começam a devolver valor mais cedo, melhorando o momento e o tamanho total do ROI em comparação com um lançamento de tudo de uma vez que nada devolve até o fim.

No **[custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, o Agile baixa o custo da mudança ao longo da vida de um sistema, desde que a disciplina de engenharia seja real. Seu risco dominante é o *agile falso*: cerimônia sem princípio nem ofício, que acrescenta sobrecarga de reuniões sem entregar nenhum dos benefícios e pode ser pior que uma cascata honesta. Então o argumento de negócio é condicional. O ROI é alto quando vocês adotam o Agile como mentalidade mais engenharia, e aproximadamente zero (ou negativo) quando o adotam como ritual. Defendam o caso junto à liderança enquadrando o Agile como redução contínua de risco e medição de resultados, não como “ir mais depressa”, e insistindo que o investimento inclua práticas técnicas e não só reuniões novas.

## Antipadrões e armadilhas

- **Agile falso / de culto à carga:** cerimônias executadas enquanto as decisões, o financiamento e a mentalidade permanecem em cascata.
- **Velocidade como produtividade:** transformar uma estimativa de capacidade em meta, o que a corrompe ([Lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** correr em sprints sem excelência técnica para um código impossível de manter e cheio de defeitos.
- **Retrospectivas sem mudança:** reflexão que não produz ações concluídas.
- **Escopo *e* data *e* custo fixos:** chamar de agile enquanto a qualidade absorve a pressão em silêncio.
- **Cliente ausente:** nenhum retorno real de usuários, de modo que as iterações otimizam a coisa errada.
- **Culto ao framework:** o “o SAFe/Scrum manda” se sobrepondo aos princípios e ao julgamento da equipe.
- **Escalar antes de desescalar:** acrescentar frameworks pesados de coordenação em vez de reduzir as dependências.

## Modelo de maturidade

- **Nível 1, Iniciar.** Entrega em cascata ou ad hoc; lançamentos de tudo de uma vez; o trabalho é reativo e pesado em planos, sem retorno iterativo nem noção compartilhada de por que o Agile poderia ajudar.
- **Nível 2, Desenvolver.** Algumas equipes adotam cerimônias do Agile (reuniões diárias, sprints, retrospectivas), mas a prática é inconsistente na organização: a mentalidade e a disciplina de engenharia ficam atrás dos rituais, a velocidade é tratada como produção e o escopo ainda é fixado de antemão.
- **Nível 3, Padronizar.** Valores e princípios guiam genuinamente o trabalho em toda a organização, documentados e esperados de toda equipe: a excelência técnica estilo XP (CI, testes automatizados, refatoração, desenvolvimento baseado em trunk) é prática padrão, as equipes se autoorganizam, os clientes são engajados a cada iteração e as retrospectivas produzem mudança concreta e concluída.
- **Nível 4, Gerenciar.** A entrega é medida e controlada em relação a linhas de base: as equipes acompanham o prazo de entrega, a frequência de implantação, a taxa de falha de mudanças e a taxa de escape de defeitos (as métricas de fluxo e de estabilidade ao estilo DORA), ao lado de medidas de resultado atreladas a resultados-chave, e comparam cada uma com uma linha de base conhecida. As ações das retrospectivas são acompanhadas até a conclusão, os sinais de ritmo sustentável, como horas extras e esgotamento, são monitorados e a velocidade nunca é usada como meta de produtividade. As decisões de ir ou não ir repousam nessa evidência e não em opinião.
- **Nível 5, Orquestrar.** A entrega adaptativa é integrada ao planejamento de negócio e de riscos em toda a organização: os resultados (OKRs) conduzem o financiamento e a cadência, o desenho de equipes de baixa dependência (desescalar) minimiza a sobrecarga de coordenação e a governança híbrida satisfaz a supervisão sem atrasar a entrega. A melhoria contínua é cultural e não cerimonial, e a organização rotineiramente redefine o escopo, reorganiza equipes e reequilibra seu portfólio conforme a evidência e o quadro de risco mudam.

## Ideias para discussão

1. Pontuem a sua equipe contra os doze princípios do Agile: onde vocês são ágeis na cerimônia mas não na substância?
2. A velocidade é usada na sua equipe como previsão ou como meta, e o que isso fez com o comportamento?
3. Quais práticas técnicas de XP estão faltando, e como a ausência delas aparece como defeitos ou mudança lenta?
4. Antes de adotar um framework de escala, vocês poderiam reduzir as dependências entre equipes?
5. No seu contexto, o que especificamente bloqueia o acesso real ao usuário a cada iteração, e como vocês poderiam removê-lo?
6. Qual foi a última mudança concreta que uma retrospectiva de fato produziu?

## Principais conclusões

- O Agile é uma **mentalidade de valores e princípios**, não um conjunto de cerimônias. Os frameworks são pontos de partida, não o objetivo.
- Entreguem **software funcionando com frequência**, acolham a mudança e empoderem **equipes autoorganizadas**.
- **A excelência técnica (práticas de XP) é inegociável.** A agilidade sem ela vira decadência rápida.
- **Escalem com cuidado e prefiram desescalar.** Reduzam as dependências antes de acrescentar frameworks de coordenação.
- Em contextos corporativos e governamentais, combinem **entrega adaptativa com governança híbrida e contratação ágil** e lutem por acesso real ao usuário.
- O ROI é **redução contínua de risco e valor mais cedo**, mas só quando o Agile é real e não ritual. Vejam os capítulos 1.4, 11.1, 11.2, 10.6 e 11.3.

## Referências e leitura complementar

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
