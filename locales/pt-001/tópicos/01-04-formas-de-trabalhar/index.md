# 1.4 Formas de trabalhar

## Visão geral e motivação

“Formas de trabalhar” descreve como a sua equipe de fato se coordena, planeja, se comunica e entrega no dia a dia. Como o trabalho é dividido? Quem fala com quem, e quando? Como o progresso é acompanhado, e como as decisões e o conhecimento circulam?

A maioria das organizações adota uma metodologia com nome, o [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), o [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), alguma estrutura de escala, e presume que as cerimônias equivalem ao valor que há por baixo delas. Não equivalem. As metodologias que transformaram a entrega de software foram reações contra processos pesados e movidos a repasses. Seu objetivo era feedback rápido, lotes pequenos e equipes empoderadas. Adote só os rituais, as reuniões diárias, as sprints, os pontos de história, sem os princípios, e você terá os custos do processo sem os benefícios: o agile de [culto ao cargo](https://en.wikipedia.org/wiki/Cargo_cult).

Para equipes grandes, é aqui que as boas intenções vencem ou falham. Mil engenheiros não cabem todos na mesma sala, não conseguem participar da mesma reunião nem compartilhar o mesmo contexto tácito. Quanto maior você fica, mais precisa se apoiar em comunicação escrita, colaboração assíncrona e coordenação leve, em vez de reuniões e conversas de corredor. A escala muda a física. Práticas que funcionam lindamente para oito pessoas no mesmo local podem colapsar para oitenta pessoas distribuídas. E as estruturas de escala que prometem resolver isso frequentemente reintroduzem os mesmos repasses e a mesma centralização que o [agile](https://en.wikipedia.org/wiki/Agile_software_development) pretendia eliminar.

Empresas e governo sentem cada uma dessas pressões com força total. Elas abrangem muitos fusos horários, misturam funcionários permanentes com terceirizados e fornecedores e muitas vezes carregam portões de etapa e relatórios obrigatórios. Aqui, uma forma de trabalhar centrada em documentos, assíncrona e focada em resultados não é um luxo. É a única que escala. As recomendações abaixo favorecem adaptar princípios ao contexto em vez de importar estruturas inteiras, e favorecem práticas escritas, assíncronas e transparentes que deixem forças de trabalho grandes, distribuídas e mistas colaborarem de verdade.

## Princípios fundamentais

- Adote princípios, não rituais. Entenda por que uma prática existe antes de copiá-la.
- Lotes pequenos e feedback rápido vencem planos grandes e ciclos longos.
- Prefira o fluxo (limitando o trabalho em andamento) a janelas de tempo rígidas onde couber.
- Estime para viabilizar a conversa e o planejamento, não para fabricar falsa precisão.
- Adote por padrão a comunicação assíncrona e escrita. Reserve o tempo síncrono para o que realmente precisa dele.
- Torne o trabalho e as decisões visíveis e documentados para que qualquer pessoa se atualize sem uma reunião.
- Otimize os resultados entregues, não a atividade realizada nem a capacidade utilizada.

## Recomendações

### Adapte Agile, Scrum, Kanban e Lean ao contexto

Trate-os como uma caixa de ferramentas, não como uma religião. As sprints com janela de tempo do Scrum servem a equipes com trabalho de descoberta que se beneficia de um ritmo regular de planejamento e revisão. O fluxo contínuo e os limites explícitos de trabalho em andamento do Kanban servem a equipes com trabalho imprevisível e movido a interrupções, como plataforma e operações. O foco do [Lean](https://en.wikipedia.org/wiki/Lean_software_development) em eliminar desperdício e encurtar o prazo de entrega sustenta ambos. Escolha deliberadamente. Misture onde ajudar: muitas equipes praticam o “[Scrumban](https://en.wikipedia.org/wiki/Scrumban)”. Mantenha as práticas que criam valor e abandone as cerimônias que viraram ritual vazio. O teste para qualquer prática é simples. Ela encurta o feedback, reduz o tamanho do lote ou aumenta a clareza? Se não, questione-a.

### Escale com cautela, não com culto ao cargo

As estruturas de escala, o [SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), o LeSS (Large-Scale Scrum) e o popularizado “modelo Spotify”, prometem coordenar muitas equipes. Aborde-as com olhar cético. O SAFe traz estrutura e é frequentemente escolhido por grandes empresas e pelo governo por sua abrangência e seu ecossistema de treinamento, mas pode reintroduzir planejamento pesado, hierarquia e repasses que minam a agilidade. O LeSS fica mais perto dos princípios lean, mas exige mudança organizacional real. O “modelo” Spotify foi um retrato da cultura em evolução de uma empresa, nunca um modelo, e nem mesmo o Spotify o praticava como as pessoas imaginam. Prefira escalar reduzindo a necessidade de coordenação, por meio das topologias de equipes do capítulo anterior, em vez de aparafusar uma estrutura de coordenação numa organização fragmentada.

### Estime com honestidade e leveza

Pontos de história e velocidade ajudam sua equipe a planejar o próprio trabalho de curto prazo e a conversar sobre complexidade relativa. Não são uma métrica de produtividade, uma moeda entre equipes nem uma promessa. Nunca transforme a velocidade em meta: ela será manipulada por inflação de pontos. Para previsões de prazo mais longo, prefira contar a vazão e usar dados históricos de tempo de ciclo, que costumam ser mais precisos que somar estimativas. Muitas equipes maduras reduzem o custo da estimativa fatiando o trabalho em pedaços igualmente pequenos e simplesmente contando-os. Seja qual for o método, lembre-se de que estimativas são previsões sob incerteza, não compromissos. Comunique-as como intervalos.

### Adote por padrão a comunicação assíncrona e centrada em documentos

Em organizações grandes e distribuídas, reuniões síncronas não escalam e deixam de fora as pessoas em outros fusos horários. Faça da escrita o padrão: documentos de projeto, [registros de decisão](https://en.wikipedia.org/wiki/Architectural_decision), atualizações de status escritas e tíquetes completos que carreguem contexto suficiente para agir sem uma conversa ao vivo. Grave e resuma as reuniões que você não consegue evitar. Uma cultura de documentos primeiro permite que alguém em outro fuso horário contribua plenamente, permite que novas pessoas e terceirizados se integrem lendo e deixa um registro durável. Reserve o tempo síncrono para colaboração genuína, construção de relacionamentos e esclarecimento rápido de ambiguidades. Proteja grandes blocos de tempo de foco da fragmentação por reuniões.

### Trabalhe bem entre fusos horários, terceirizados e fornecedores

Forças de trabalho distribuídas e mistas são a norma em escala. Projete para o “[siga o sol](https://en.wikipedia.org/wiki/Follow-the-sun)”, em que as passagens de bastão são escritas e completas, não verbais. Defina algumas horas centrais sobrepostas para o contato síncrono de que você precisa e divida com justiça o incômodo de horários de reunião inconvenientes, em vez de sempre sobrecarregar a mesma região. Para terceirizados e fornecedores, invista mais em contexto escrito, interfaces claras e ferramentas compartilhadas, porque eles não têm o conhecimento tácito que seus funcionários permanentes acumularam. Traga os fornecedores para os mesmos quadros e a mesma documentação visíveis, em vez de geri-los por um canal separado e opaco. Sempre que puder, estruture os contratos em torno de resultados e não de horas.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
| --- | --- | --- |
| Agile (interações com as partes interessadas) | Alta colaboração e valor mais rápido | Exige confiança e flexibilidade |
| Scrum (sprints com janela de tempo) | Cadência regular, ritmo previsível, reflexão embutida | Custo de cerimônia. Mau encaixe para trabalho movido a interrupções |
| Kanban (fluxo contínuo, limites de WIP) | Flexível, expõe gargalos, bom para operações | Menos ritmo. Exige disciplina para limitar o WIP |
| SAFe / estrutura de escala pesada | Estrutura, treinamento, familiar a grandes organizações e ao governo | Reintroduz hierarquia e repasses. Pode sufocar a agilidade |
| LeSS / escala leve | Fica perto dos princípios lean | Exige mudança organizacional profunda |
| Assíncrono / documentos primeiro | Escala entre fusos horários. Durável. Inclusivo | Mais lento para temas ambíguos. Exige disciplina de escrita |

O compromisso geral é coordenação versus autonomia, e estrutura versus adaptabilidade. Mais estrutura e mais coordenação síncrona compram previsibilidade e alinhamento, ao custo de velocidade, custo operacional e empoderamento das equipes. Menos estrutura compra velocidade e responsabilidade, ao custo de um possível desalinhamento entre muitas equipes. Para a maioria das grandes organizações, a melhor resposta é uma cadência compartilhada mínima mais fortes práticas escritas. Isso reduz o fardo da coordenação na origem, em vez de geri-lo com processo mais pesado.

## Perguntas para discutir com sua equipe

1. **Se a liderança quer a previsibilidade que uma estrutura de escala promete, como você a dará sem reintroduzir os repasses que o agile pretendia remover?** Grandes empresas e programas governamentais frequentemente exigem planejamento em grande sala no estilo SAFe e relatórios por portões de etapa porque os órgãos de supervisão exigem previsões e coordenação que possam ver. As considerações concorrentes são genuínas: a liderança precisa de previsibilidade e alinhamento entre muitas equipes, e estruturas pesadas compram isso ao custo de velocidade, custo operacional e dos próprios repasses que atrasam a entrega. Leve evidências à discussão, como quanto da semana de trabalho some em eventos de planejamento e na coordenação de dependências entre equipes, e se esses eventos removem as dependências ou apenas as expõem. O movimento mais forte é escalar reduzindo a necessidade de coordenar por meio da topologia das equipes e depois atender aos relatórios a partir de quadros vivos e interfaces escritas, e não de maratonas de planejamento. Decida qual coordenação é real e qual é cerimônia, e dê à liderança a previsão de que precisa a partir de dados de vazão e tempo de ciclo, em vez do custo operacional de uma estrutura.

2. **O que você fará de fato para impedir que a velocidade seja transformada numa métrica de produtividade entre equipes?** Os pontos de história ajudam uma única equipe a planejar o próprio trabalho de curto prazo, e se tornam inúteis no momento em que são comparados entre equipes ou definidos como meta, porque a inflação de pontos é a resposta racional. Numa organização grande, a pressão para consolidar a velocidade num painel que os executivos comparem é forte e corrompe em silêncio as estimativas de que as equipes dependem. Leve as evidências de deriva: os pontos estão inflando com o tempo, as equipes estão inflando estimativas, alguém está sendo classificado por velocidade? Prefira contar a vazão e usar dados históricos de tempo de ciclo para qualquer previsão que saia da equipe, e comunique as estimativas como intervalos sob incerteza, não como promessas. A resposta deve produzir um acordo explícito de que a velocidade nunca sai da equipe e de que a previsão entre equipes usa métricas de fluxo.

3. **Qual é a sua régua concreta para “escrito”, e quais decisões ainda precisam genuinamente de uma conversa síncrona?** Um padrão de documentos primeiro é o que escala entre fusos horários, terceirizados e fornecedores, e custa uma disciplina de escrita real que nem todos têm ainda. Seja específico sobre a régua: um tíquete carrega contexto suficiente para agir sem uma ligação ao vivo, as decisões chegam a um registro durável, as reuniões que você não consegue evitar são gravadas e resumidas? Para empresas e programas governamentais que misturam funcionários permanentes com terceirizados sem conhecimento tácito, o contexto escrito é o que permite a uma força de trabalho mista e distribuída contribuir plenamente. O compromisso é que temas ambíguos ou controversos costumam ser resolvidos mais rápido de forma síncrona, então nomeie-os explicitamente e reserve o escasso tempo síncrono para eles. Decida quem arca com o custo de construir o hábito da escrita e dos horários de reunião inconvenientes, e divida esse custo com justiça, em vez de sempre sobrecarregar a mesma região.

4. **Quais das nossas cerimônias atuais sobreviveriam se julgássemos cada uma apenas por encurtar o feedback, reduzir o tamanho do lote ou aumentar a clareza?** As cerimônias se acumulam em silêncio: uma reunião diária aqui, uma sessão de refinamento ali, uma revisão, uma retrospectiva e um evento de planejamento, até que uma grande equipe passe mais da semana em reuniões recorrentes do que no trabalho a que elas deveriam servir. As considerações concorrentes são reais, porque um ritual que parece puro custo para uma pessoa pode ser o único lugar em que uma equipe distribuída constrói contexto compartilhado ou traz à tona um impedimento. Leve evidências à discussão: o total de horas de reuniões recorrentes por pessoa por semana, a presença e o engajamento em cada cerimônia e que decisão ou sinal cada uma de fato produz que não poderia vir de uma atualização escrita. Para uma empresa ou programa governamental em que todas as equipes seguem a mesma cadência imposta, o custo acumulado é enorme, então acorde um teste explícito que cada cerimônia precisa passar para manter seu espaço e esteja disposto a cortar ou fundir as que só persistem por hábito.

5. **Quando o trabalho trava, sabemos onde ele está de fato esperando, e estamos gerenciando fluxo ou apenas alocando gente?** Na maior parte do trabalho do conhecimento, uma tarefa passa muito mais da vida esperando em filas, repasses e revisões do que sendo ativamente trabalhada, e ainda assim as equipes respondem por instinto à entrega lenta acrescentando pessoas ou pressionando por maior utilização, o que alonga as filas em vez de encurtá-las. A tensão é que limitar o trabalho em andamento parece deixar capacidade ociosa, e pessoas com aparência de ociosas deixam gestores e órgãos de supervisão desconfortáveis. Leve as evidências que expõem a verdade: distribuições de tempo de ciclo, a razão entre tempo ativo e prazo total de entrega, onde os itens ficam bloqueados no seu quadro e como os limites de trabalho em andamento (um teto de quantos itens estão em curso ao mesmo tempo) mudam a vazão quando você os aplica. Para uma organização grande ou governamental medida pela utilização de pessoal, isso reformula a meta de manter todos ocupados para manter o trabalho concluído fluindo, e essa mudança costuma ser a maior alavanca isolada sobre a velocidade de entrega.

6. **Como a nossa forma de trabalhar absorverá as pessoas que não são funcionárias permanentes no nosso fuso horário central, os terceirizados, os fornecedores e as regiões com muitas horas de diferença da sede?** Em escala, uma força de trabalho mista e distribuída é a norma, e práticas calibradas para uma equipe central no mesmo local excluem em silêncio todas as demais: o fornecedor gerido por um canal privado, o terceirizado sem o contexto tácito, a região cujo dia de trabalho nunca se sobrepõe a uma reunião de decisão. As considerações puxam em sentidos opostos, porque interfaces escritas mais rígidas e passagens de bastão escritas e completas custam disciplina real e desaceleram a coordenação informal rápida de que um grupo no mesmo local desfruta. Leve evidências como quem está rotineiramente ausente das reuniões em que as decisões são tomadas, com que frequência as regiões distantes ficam bloqueadas esperando um repasse e se os fornecedores trabalham nos mesmos quadros visíveis que a equipe ou numa trilha separada e opaca. Para empresas e programas governamentais que misturam funcionários permanentes, terceirizados e fornecedores em muitos fusos horários sob relatórios obrigatórios, trate a prática escrita, transparente e do tipo siga-o-sol como a linha de base que permite a toda a força de trabalho contribuir, e divida o ônus dos horários inconvenientes em vez de impô-lo sempre à mesma região.

## Perspectiva por setor

**Startup.** Com um punhado de pessoas e pouca pista, pule o catálogo de cerimônias e funcione com o fluxo mais leve possível: um quadro compartilhado, uma curta atualização diária por escrito e decisões registradas num documento, para que ninguém fique bloqueado esperando um colega acordar. Faça da escrita o padrão desde o primeiro dia, porque o hábito assíncrono é muito mais barato de construir com cinco pessoas do que de reformar com cinquenta. Não adote uma estrutura de escala de que você não precisará por anos. Sua vantagem é que você quase não tem o que coordenar, então proteja isso.

**Pequena empresa.** Sem coach de agile nem gerente de entrega no quadro e com orçamento apertado, favoreça a prática pronta em vez de estruturas compradas que trazem custos de treinamento e certificação que você não consegue justificar. Escolha uma metodologia que se encaixe no seu trabalho, Kanban para trabalho de serviço movido a interrupções ou uma cadência leve de Scrum para trabalho de projeto, e resista à tentação de comprar uma ferramenta pesada quando um quadro simples e tíquetes claros dão conta. Gaste seu escasso esforço de coordenação em pôr as coisas por escrito, para que uma equipe pequena não fique refém da memória de uma só pessoa.

**Grande empresa.** Entre muitas equipes, o problema é custo de coordenação e consistência: uma cadência compartilhada mínima, uma definição comum do que significa “escrito” e métricas de fluxo que se consolidem sem transformar a velocidade numa meta entre equipes. Escale reduzindo a necessidade de coordenar por meio da topologia das equipes, e não aparafusando uma estrutura que reintroduz repasses, e governe a forma de trabalhar como algo que você ajusta a partir de evidências, não como uma implantação única. Padronize as interfaces e os relatórios para que a supervisão seja atendida a partir de quadros vivos e não de maratonas de planejamento.

**Governo.** Regras de contratação, portões de etapa obrigatórios e responsabilização pública moldam cada escolha, e forças de trabalho mistas de funcionários permanentes, terceirizados e fornecedores abrangem muitos fusos horários sob relatórios de progresso exigidos. Favoreça uma forma de trabalhar transparente e centrada em documentos, em que cada item de trabalho carregue contexto escrito completo num quadro visível tanto para a equipe quanto para os fornecedores, de modo que os relatórios de status saiam direto do registro e não de reuniões separadas. Estruture os contratos de fornecedores em torno de resultados e visibilidade compartilhada, em vez de faturamento opaco por hora, e trate a trilha escrita e auditável como um ativo de conformidade, não como custo operacional.

## Exemplos

**Startup.** Uma startup distribuída de oito pessoas pula o catálogo completo de cerimônias do Scrum e funciona com um quadro Kanban compartilhado e uma curta atualização diária escrita no Slack. Como os dois fundadores ficam em fusos horários diferentes, eles fazem da escrita o padrão desde o primeiro dia: toda decisão vai para um documento, de modo que ninguém fica bloqueado esperando o outro acordar. Quando depois contratam num terceiro fuso horário, a integração é basicamente leitura, e o hábito assíncrono escala sem mudanças. A prática que nunca adotaram, a reunião síncrona de status, é a que nunca lhes faz falta.

**Grande empresa.** Um banco multinacional implantou uma estrutura de escala em centenas de equipes, completa com planejamento trimestral em grande sala. O alinhamento melhorou no papel, mas a entrega ficou mais lenta. As equipes passavam dias em eventos de planejamento e na coordenação de dependências entre equipes que a estrutura expunha, mas não removia. O banco corrigiu o rumo. Manteve apenas o alinhamento leve entre equipes de que realmente precisava, reestruturou as equipes para serem donas de seus fluxos de valor de ponta a ponta e deslocou a maior parte da coordenação para interfaces escritas e atualizações assíncronas. O prazo de entrega caiu, e as exaustivas maratonas de planejamento encolheram para sincronizações focadas e ocasionais.

**Governo.** Uma agência governamental que presta serviços aos cidadãos trabalhava com funcionários permanentes numa região e equipes terceirizadas em outras duas, abrangendo muitos fusos horários, sob relatórios obrigatórios de progresso. Adotou uma forma de trabalhar baseada em Kanban e centrada em documentos. Cada item de trabalho carregava contexto escrito completo num quadro compartilhado, visível tanto para a equipe quanto para os fornecedores. As passagens de bastão entre regiões eram escritas e completas. Os relatórios de status exigidos saíam direto do quadro, e não de reuniões separadas. Isso permitiu que uma força de trabalho distribuída e mista colaborasse continuamente, atendeu aos relatórios de supervisão como subproduto e reduziu a dependência da agência de reuniões entre fusos horários difíceis de agendar.

## Justificativa de negócio: motivações, ROI e TCO

O argumento econômico repousa na eficiência de fluxo. Na maior parte do trabalho do conhecimento, o tempo que uma unidade de trabalho passa sendo ativamente trabalhada é uma pequena fração do seu prazo total de entrega. O resto é espera: em filas, em reuniões, em repasses, em lacunas de fuso horário. Formas de trabalhar que reduzem o tamanho do lote, limitam o trabalho em andamento e substituem gargalos síncronos por fluxo assíncrono e escrito atacam essa espera diretamente. O retorno são prazos de entrega mais curtos e maior vazão sem acrescentar pessoas, mais menos defeitos, porque o feedback chega mais cedo, quando o contexto ainda está fresco.

Pese o custo de adotar contra o custo do status quo. Documentos primeiro, assíncrono e fluxo lean custam principalmente uma mudança de hábitos e algum investimento inicial em escrita e ferramentas. Não precisam de licenças caras. As estruturas de escala pesadas, por outro lado, trazem custo real: treinamento, certificação, funções dedicadas e o custo operacional contínuo de grandes eventos de planejamento. Apenas necessidades genuínas de coordenação os justificam. O custo de não fazer nada aparece como agendas saturadas de reuniões, colaboradores remotos excluídos, cerimônias de culto ao cargo que consomem tempo sem melhorar resultados e entrega lenta. Para defender o caso junto à liderança, meça o prazo de entrega, a frequência de implantação e a fração da semana de trabalho perdida em reuniões de baixo valor. Pequenas melhorias de fluxo numa grande força de trabalho somam grandes ganhos de capacidade.

## Antipadrões e armadilhas

- Agile de culto ao cargo: realizar cerimônias sem os princípios subjacentes.
- Velocidade como meta: convida à inflação de pontos e destrói a utilidade da métrica.
- Culto a estruturas: impor o SAFe ou um “modelo Spotify” independentemente do encaixe.
- Estimativas como compromissos: tratar previsões sob incerteza como promessas vinculantes.
- Cultura movida a reuniões: adotar por padrão chamadas síncronas que excluem outros fusos horários.
- Decisões não documentadas: conhecimento preso nas cabeças das pessoas e em conversas passadas.
- Caixas-pretas de fornecedores: gerir terceirizados por canais laterais opacos em vez de visibilidade compartilhada.
- Obsessão com utilização: maximizar o quanto todos estão ocupados em vez do fluxo de trabalho concluído.

## Modelo de maturidade

- **Nível 1, Iniciar.** O processo é ad hoc ou de culto ao cargo. As equipes realizam cerimônias emprestadas sem os princípios por trás delas, ou improvisam sem nenhum método compartilhado. A comunicação é movida a reuniões e não documentada, as decisões vivem nas cabeças das pessoas e as estimativas são tratadas como promessas. Colaboradores distribuídos, terceirizados e fusos horários distantes são coordenados verbalmente e ficam bloqueados sempre que a pessoa certa está dormindo.
- **Nível 2, Desenvolver.** Equipes individuais adotam uma metodologia com nome, como Scrum ou Kanban, e a seguem com alguma consistência, mas a prática varia de equipe para equipe e as cerimônias costumam ser mecânicas. Algumas equipes escrevem documentos de projeto e registros de decisão enquanto outras ainda dependem de reuniões. Estimativa e coordenação acontecem, mas sem uma régua compartilhada do que significa “escrito”, então o contexto ainda vaza e os repasses entre equipes continuam pesados.
- **Nível 3, Padronizar.** As práticas são escolhidas deliberadamente para se ajustar ao trabalho e documentadas como expectativa da organização inteira: uma cadência compartilhada mínima, uma régua definida de contexto escrito em tíquetes e registros de decisão, comunicação assíncrona centrada em documentos como padrão e estimativa usada para conversa e não para controle. O padrão é aplicado com consistência, de modo que um terceirizado ou uma pessoa nova em qualquer equipe pode se integrar lendo, e os fornecedores trabalham nos mesmos quadros visíveis que a equipe.
- **Nível 4, Gerenciar.** A forma de trabalhar é medida em relação a linhas de base em vez de presumida. As equipes acompanham o prazo de entrega, as distribuições de tempo de ciclo, a frequência de implantação, a vazão e a fração da semana de trabalho perdida em reuniões de baixo valor, e observam se a velocidade está sendo manipulada por inflação de pontos. Os limites de trabalho em andamento são aplicados com base em evidências, o fluxo é gerenciado no lugar da utilização e os dados, não a opinião, decidem quais cerimônias mantêm seu espaço e onde as filas estão crescendo. Os relatórios à liderança e aos órgãos de supervisão saem direto dessas métricas vivas.
- **Nível 5, Orquestrar.** A organização ajusta continuamente a sua forma de trabalhar a partir de métricas de fluxo e evidências de retrospectivas, e a necessidade de coordenação é minimizada na origem por meio da topologia das equipes, e não gerida com processo mais pesado. Formas de trabalhar, métricas de entrega e desenho organizacional são integrados e se adaptam conforme o quadro de pessoal, de mercado e regulatório muda. Equipes distribuídas e mistas de funcionários, terceirizados e fornecedores em muitos fusos horários colaboram sem atrito, e as práticas que deixam de justificar o próprio custo são aposentadas sem cerimônia.

## Ideias para discussão

- Quais das nossas cerimônias manteríamos se as julgássemos puramente pelo valor que criam?
- Estamos escalando acrescentando uma estrutura ou reduzindo a necessidade de coordenar?
- Nossa velocidade é um auxílio ao planejamento ou uma meta que estamos manipulando em silêncio?
- Que decisões e status vivem apenas em reuniões e na memória das pessoas, e deveriam ser escritos?
- O fuso horário de quem arca com o custo das nossas reuniões síncronas, e isso é justo?
- Nossos terceirizados e fornecedores trabalham no mesmo fluxo visível que a nossa equipe?

## Principais conclusões

- Adote os princípios por trás das metodologias, não apenas seus rituais.
- Escolha Agile, Kanban ou uma mistura para se ajustar ao trabalho. Favoreça lotes pequenos e feedback rápido.
- Aborde as estruturas de escala com ceticismo. Escale reduzindo a coordenação, não acrescentando processo.
- Use estimativas para conversa e previsão, nunca como metas de produtividade nem promessas.
- Adote por padrão a comunicação assíncrona e centrada em documentos, para que equipes grandes, distribuídas e mistas possam colaborar.
- Otimize resultados e fluxo, não atividade nem utilização.

## Referências e leitura complementar

- David J. Anderson, "Kanban: Successful Evolutionary Change for Your Technology Business"
- Donald Reinertsen, "The Principles of Product Development Flow"
- Mary and Tom Poppendieck, "Lean Software Development: An Agile Toolkit"
- Craig Larman and Bas Vodde, "Large-Scale Scrum (LeSS)"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (delivery metrics)
- The Agile Manifesto and its twelve principles
- Henrik Kniberg, "Scaling Agile @ Spotify" (with the caution that it is a snapshot, not a model)
- GitLab's public Handbook on asynchronous, remote-first working
