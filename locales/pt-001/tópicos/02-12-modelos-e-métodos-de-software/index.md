# 2.12 Modelos e métodos de software

## Visão geral e motivação

Um modelo de software é uma simplificação deliberada de um sistema, construída para responder a uma pergunta específica. Um método é uma forma disciplinada de produzir software, incluindo os modelos que ele usa pelo caminho. Juntos formam uma área de conhecimento do Software Engineering Body of Knowledge (SWEBOK), porque são as ferramentas mentais que você usa para raciocinar sobre um sistema antes, durante e depois de construí-lo. Um diagrama de classes UML ([Linguagem de Modelagem Unificada](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), um [diagrama de entidade-relacionamento](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (DER), uma [máquina de estados](https://en.wikipedia.org/wiki/Finite-state_machine), uma [especificação formal](https://en.wikipedia.org/wiki/Formal_specification) e um protótipo descartável são todos modelos. O [modelo em cascata](https://en.wikipedia.org/wiki/Waterfall_model), a [prototipagem](https://en.wikipedia.org/wiki/Software_prototyping), o desenvolvimento formal e o [ágil](https://en.wikipedia.org/wiki/Agile_software_development) são todos métodos.

Por que se dar ao trabalho de usar modelos? Porque a memória de trabalho humana é pequena e os sistemas de software são grandes. Ninguém consegue guardar na cabeça um sistema de cem mil linhas, então desenhamos figuras e escrevemos abstrações que mostram uma faceta de cada vez: os dados, o fluxo de controle, os estados, as interações. Um modelo nunca pretende ser fiel ao código. Pretende ser adequado a uma decisão. Um bom modelo mostra exatamente o que você precisa para decidir algo e esconde todo o resto.

Em equipes grandes, o que está realmente em jogo é a coordenação e a comunicação. Quando centenas de engenheiros, arquitetos, analistas e auditores trabalham em um só sistema, os modelos compartilhados são o terreno comum onde negociam design, requisitos e risco. Então pense na modelagem como uma ferramenta com um trabalho a fazer. Ela compensa quando um modelo é mais barato que o erro que evita. Vira desperdício quando você o desenha por si mesmo, o mantém muito depois de ter ficado obsoleto ou o elabora além da decisão a que se destinava. A modelagem se liga estreitamente aos requisitos de software (capítulo 2.8), aos princípios de design de software (capítulo 2.2), à arquitetura e suas notações como C4 e arc42 (capítulo 3.1) e às formas ágeis de trabalhar (capítulo 10.7).

## Princípios fundamentais

- Todo modelo tem um propósito. Se você não consegue nomear a decisão que um modelo informa, não o desenhe.
- A abstração é o ato central da modelagem: inclua o que importa para o propósito, omita o resto.
- A consistência importa dentro dos modelos e entre eles. Modelos contraditórios são piores que nenhum.
- Os modelos são, antes de tudo, artefatos de comunicação. O público deles determina a notação e o detalhe.
- Prefira o modelo mais leve que responde à pergunta. A elaboração tem um custo de manutenção.
- Um modelo só é tão bom quanto a sua análise. Um modelo não verificado é uma premissa não testada.
- Escolha o método para se ajustar à incerteza, ao risco e à consequência de falha do problema.

## Recomendações

### Modele com abstração, propósito e consistência

Comece todo modelo nomeando seu propósito e seu público. Depois abstraia sem piedade em direção a esse propósito: um diagrama de sequência destinado a resolver uma condição de corrida deve mostrar o tempo e as mensagens, não todos os campos. Mantenha seus modelos consistentes entre si, de modo que as entidades de um DER, as classes de um diagrama de classes e os substantivos dos requisitos concordem, e consistentes com a realidade, o que significa atualizar ou apagar um modelo quando o sistema segue adiante. Um modelo obsoleto em que as pessoas confiam é um risco. Um modelo obsoleto que todos ignoram é desperdício que ainda custa atenção.

### Escolha modelos estruturais ou comportamentais para corresponder à pergunta

Use modelos estruturais para mostrar de que um sistema é feito e como as partes se relacionam: diagramas de classes, diagramas de componentes e diagramas de entidade-relacionamento para a estrutura de dados. Use modelos comportamentais para mostrar o que um sistema faz ao longo do tempo: máquinas de estados para objetos com ciclos de vida significativos, diagramas de sequência para interações entre componentes e diagramas de atividades para fluxos de trabalho e processos de negócio. Escolha a notação que expõe a decisão à sua frente. A maioria dos sistemas precisa de apenas um punhado de tipos de diagrama, desenhados com seletividade, e não de todo o catálogo da UML aplicado a tudo.

### Analise os modelos, não apenas os desenhe

Um modelo se justifica pela análise, não só pelo desenho. Verifique uma máquina de estados quanto a estados inalcançáveis, transições ausentes e impasses. Verifique um DER quanto a problemas de normalização e relacionamentos órfãos. Percorra um diagrama de sequência contra os requisitos para encontrar caminhos de erro ausentes. Revise seus modelos com os especialistas do domínio que conseguem perceber o que está errado. E onde o custo da falha é alto, recorra a análise apoiada por ferramentas (verificadores de modelo, verificadores de consistência, simulação) em vez de olhar a olho nu.

### Aplique métodos heurísticos como padrão

A maior parte do software é construída com métodos heurísticos: abordagens iterativas, baseadas em experiência, que usam modelos de modo informal e julgam os resultados contra expectativas e não contra provas. Para a maioria dos sistemas empresariais e governamentais, isso é exatamente o certo: os requisitos evoluem e um defeito costuma ser recuperável. Os métodos heurísticos combinam naturalmente com o ágil (capítulo 10.7): modele só o suficiente para alinhar a equipe e depois construa e aprenda.

### Reserve os métodos formais para os núcleos de alta consequência

Os [métodos formais](https://en.wikipedia.org/wiki/Formal_methods) expressam especificações em matemática e usam verificação, seja por prova ou por [verificação de modelos](https://en.wikipedia.org/wiki/Model_checking) exaustiva, para estabelecer propriedades. Custam habilidade e tempo reais e compensam precisamente onde a falha é catastrófica ou irreversível: controle crítico para a segurança, protocolos criptográficos, núcleos de liquidação financeira e afins. Aplique-os ao pequeno núcleo crítico, não ao sistema inteiro. E note que a especificação formal sozinha, mesmo sem prova completa, muitas vezes agrega valor simplesmente por forçá-lo a ser preciso.

### Use a prototipagem para aposentar a incerteza

Quando os requisitos ou a viabilidade não estão claros, construa um protótipo para aprender e depois decida, de propósito, se vai evoluí-lo ou descartá-lo. Os protótipos descartáveis exploram uma pergunta de forma barata e depois são apagados. Os protótipos evolutivos se tornam o produto e precisam ser construídos com padrões de produção. A falha clássica é deixar um protótipo descartável escorregar para a produção por acidente. Então nomeie o tipo do protótipo antes de construí-lo.

### Ajuste o método ao risco, não à moda

Escolha os métodos pela incerteza do problema e pela consequência da falha. A alta incerteza favorece a prototipagem e a iteração ágil. A alta consequência favorece a análise formal e a verificação rigorosa. Um sistema com ambas precisa de um núcleo formal crítico dentro de um envoltório de resto ágil. Faça o que fizer, não adote um método só porque é prestigioso ou porque um fornecedor o está vendendo.

## Compromissos: prós e contras

| Modelo ou método | Bem aplicado | Modo de falha |
|---|---|---|
| Modelos estruturais (UML, DER) | Imagem compartilhada das partes e dos dados | Proliferação de diagramas. Deriva em relação ao código |
| Modelos comportamentais (estado, sequência, atividade) | Expõem tempo, estados e casos de borda | Diagramas detalhados demais que ninguém lê |
| Métodos heurísticos | Rápidos, flexíveis, adequados à maioria dos sistemas | Indisciplinados. Premissas ocultas |
| Métodos formais | Propriedades demonstráveis para núcleos críticos | Alto custo. Aplicados mal ao sistema inteiro |
| Prototipagem | Aprendizado barato. Aposenta o risco cedo | Código descartável promovido à produção |
| Métodos ágeis | Adaptam-se a requisitos em mudança | Pulam a modelagem necessária em problemas difíceis |

A tensão recorrente é entre rigor e velocidade. Modelar de menos entrega premissas ocultas à produção. Modelar demais queima esforço em diagramas que nunca informam uma decisão e apodrecem no momento em que o código muda. Não há dose fixa que resolva isso, apenas uma regra de proporção: invista num modelo ou método em proporção à incerteza que ele resolve e ao custo de errar a decisão. Um motor de pagamentos e um microsite de marketing merecem tratamento diferente.

## Perguntas para discutir com sua equipe

1. **Analisamos os nossos modelos, ou apenas os desenhamos e seguimos adiante?** Um modelo se justifica pela análise, não por existir: uma máquina de estados que você nunca verifica quanto a estados inalcançáveis ou transições ausentes é uma premissa não testada vestida de diagrama. Numa equipe grande é aqui que os defeitos reais se escondem, porque uma figura de aparência plausível ganha confiança precisamente quando ninguém a percorreu contra os requisitos para achar o caminho de erro ausente ou o relacionamento órfão. Leve à reunião o seu modelo comportamental mais importante e tente quebrá-lo: que transição está indefinida, que estado não tem saída, que sequência não tem tempo limite? Onde o custo da falha é alto, a resposta deve empurrar vocês para a análise apoiada por ferramentas (verificadores de modelo, verificadores de consistência, simulação) em vez de olhar a olho nu, porque toda a razão de modelar um núcleo crítico é encontrar a falha num quadro-branco e não em produção.

2. **Quando dois dos nossos modelos discordam, qual vence, e quem percebe a contradição?** A consistência importa dentro dos modelos e entre eles, e modelos contraditórios são piores que nenhum, porque as pessoas agem sobre ambos. Num sistema grande, as entidades do modelo de dados, as classes do design e os substantivos dos requisitos se afastam em silêncio à medida que equipes diferentes atualizam artefatos diferentes, e o primeiro sinal costuma ser um bug de produção em que dois componentes discordavam sobre o que uma coisa é. Leve um exemplo: escolha um conceito central e verifique se o DER, o código e os requisitos de fato concordam sobre sua forma e seu ciclo de vida. Se não concordam, decida qual artefato é a autoridade e quem é responsável por manter os outros em sincronia, e esteja disposto a apagar um modelo em vez de deixar um obsoleto continuar mentindo à equipe.

3. **Que núcleo do nosso sistema, se estiver errado, perde dinheiro de verdade ou faz mal a alguém, e ele recebe o rigor que merece?** A jogada central deste capítulo é ajustar o método ao risco: métodos heurísticos e ágeis para a maioria recuperável, especificação e verificação formais para o pequeno núcleo de alta consequência e prototipagem barata para o genuinamente incerto. Os modos de falha são simétricos e ambos caros: aplicar métodos formais a um microsite de marketing queima dinheiro, e tratar um motor de liquidação ou um conjunto de regras de elegibilidade como trabalho ágil comum convida ao defeito catastrófico e irreversível. Leve um mapa do seu sistema e marque onde um erro é catastrófico versus recuperável e onde os requisitos são certos versus desconhecidos. A resposta deve concentrar o seu investimento em modelagem onde estão o dinheiro e a ambiguidade e retê-lo explicitamente em todo o resto, de modo que um núcleo formal crítico possa ficar dentro de um envoltório de resto ágil sem que nenhum dos métodos vaze para o território do outro.

4. **Quanta modelagem fazemos antes de escrever código, e essa dose muda com a incerteza à nossa frente?** O grande design inicial e a ausência total de design são ambos modos de falha, e a dose certa fica entre eles, governada por quanta incerteza um modelo de fato aposenta. Numa equipe grande a pressão corre nos dois sentidos: um processo de governança pode exigir um conjunto completo de diagramas antes de qualquer código, fixando decisões tomadas com a menor informação, enquanto a pressão de entrega pode empurrar uma equipe a pular a única máquina de estados que teria pegado um caso de borda caro. Leve os seus dois últimos projetos e classifique os modelos que vocês produziram entre os que informaram uma decisão real e os desenhados só porque um modelo de documento pedia. Em programas corporativos e governamentais, onde um portão de fase ou um conselho de aprovação muitas vezes exige documentos logo de início, venha pronto para defender uma modelagem que acompanha o risco, e não uma lista fixa de entregáveis, para que o núcleo de pagamentos tenha seu rigor e a ferramenta interna de relatórios não se afogue em diagramas que ninguém lê.

5. **Combinamos uma notação compartilhada e um lar único para os nossos modelos, ou cada equipe inventa a sua?** Os modelos são, antes de tudo, artefatos de comunicação, e seu valor desmorona quando uma máquina de estados desenhada na ferramenta de uma equipe não pode ser lida, encontrada ou confiada pela equipe que a herda. Para centenas de engenheiros, as considerações concorrentes são reais: uma notação e um repositório obrigatórios compram consistência e capacidade de localização, mas também impõem um custo de aprendizado e podem empurrar as pessoas para ferramentas pesadas quando um quadro-branco fotografado serviria. Leve exemplos de onde um modelo de fato morava (uma wiki, uma ferramenta de diagramas, uma apresentação de slides, o laptop de alguém) e pergunte quem conseguiria encontrá-lo e entendê-lo seis meses depois. Em contextos corporativos e regulamentados o ângulo da auditoria o torna mais afiado: um auditor que não consegue localizar o modelo de dados atual nem rastrear uma decisão até uma máquina de estados documentada tratará o sistema como não documentado, então combinem uma pequena notação compartilhada e um local durável e aceitem o registro leve em vez da cerimônia sempre que a consequência for baixa.

6. **Antes de construir um protótipo, decidimos de propósito se ele é descartável ou evolutivo, e nos mantemos fiéis a essa escolha?** A falha clássica e cara é um protótipo descartável que escorrega em silêncio para a produção porque fez boa demonstração e ninguém nomeou seu tipo de início. A tensão é genuína: os protótipos descartáveis compram o aprendizado mais barato possível e devem ser apagados, enquanto os protótipos evolutivos se tornam o produto e precisam ser construídos com padrões de produção desde a primeira linha, e confundir os dois ou desperdiça retrabalho ou entrega código frágil a um papel para o qual nunca foi projetado. Leve um protótipo recente e pergunte o que foi decidido antes de ele ser construído, quem tinha autoridade para promovê-lo ou descartá-lo e se essa decisão sobreviveu à pressão de entrega. No governo e em outros contextos sujeitos à prestação de contas, onde um sistema voltado ao cidadão carrega obrigações de transparência e de confiabilidade, trate a promoção acidental como uma falha de controle: fixe de antemão o destino do protótipo e faça de descartar um descartável bem-sucedido um resultado celebrado e não um desperdício a evitar.

## Perspectiva por setor

**Startup.** Modele num quadro-branco, fotografe e siga adiante. Seu recurso mais escasso é a atenção de engenharia, então recorra a um modelo apenas quando ele for mais barato que o erro que evita: uma máquina de estados de assinatura antes de codificar os casos de borda da cobrança, e não um catálogo UML completo para um produto que pode mudar de rumo no mês que vem. Fique no heurístico e no ágil, deixe os métodos formais completamente de fora e trate todo protótipo como descartável, a menos que você decida o contrário conscientemente.

**Pequena empresa.** Provavelmente você não tem ninguém cujo trabalho seja a modelagem formal, então apoie-se nos modelos já embutidos nas ferramentas e frameworks que você compra, em vez de montar uma prática de modelagem própria. Enquadre os poucos modelos que desenhar em torno de decisões concretas: um esboço simples do modelo de dados para acordar que dados de clientes você guarda, um diagrama de estados para o único fluxo que faz você perder um cliente quando quebra. Prefira um produto comprado, com um modelo de dados comprovado, a construir e documentar o seu, e mantenha tudo que desenhar leve o bastante para que uma só pessoa consiga manter.

**Grande empresa.** O problema central é a coordenação entre muitas equipes, então os modelos compartilhados se tornam o terreno comum: um modelo de dados acordado, uma notação consistente e um lar onde o DER, os diagramas C4 e as máquinas de estados possam ser encontrados e merecer confiança. Padronize uma pequena notação e imponha a consistência para que as entidades dos requisitos, do design e do banco de dados não se afastem entre as equipes. Reserve a especificação formal e a verificação de modelos para os núcleos de alta consequência (liquidação, conciliação, controle de acesso), financie a habilidade especializada que isso exige e mantenha uma trilha de auditoria de cada modelo documentado até a decisão que ele justificou.

**Governo.** As regras fixadas em lei precisam ser rastreáveis até a legislação, que é onde a especificação formal justifica o seu custo: especifique a lógica de elegibilidade ou de apuração com precisão, verifique propriedades-chave e deixe os auditores rastrearem cada resultado até a regra que o produziu. A contratação acrescenta o seu próprio peso, já que documentos e modelos costumam ser entregáveis contratuais, então combinem quais modelos são genuinamente portadores de decisão e quais são produzidos só para satisfazer uma lista de verificação. Publique descrições em linguagem simples de como os sistemas consequentes funcionam e use a prototipagem descartável para testar a entrada voltada ao cidadão com usuários reais antes de se comprometer com uma construção de produção.

## Exemplos

**Startup.** Uma pequena startup que constrói um produto de cobrança por assinatura esboça o ciclo de vida da assinatura (teste, ativa, em atraso, cancelada, reativada) como uma máquina de estados num quadro-branco antes de escrever código. Ao percorrer o diagrama, notam que nunca definiram o que acontece quando o pagamento de uma conta em atraso finalmente é compensado, um caso de borda que teria deixado clientes de verdade em limbo. Esse modelo de cinco minutos poupa uma dor de cabeça em produção, e eles o fotografam em vez de manter uma ferramenta pesada de diagramas. Em todo o resto permanecem ágeis e modelam só o suficiente para alinhar, porque na escala deles um defeito é recuperável e os métodos formais seriam puro custo.

**Grande empresa.** Um banco global constrói uma nova plataforma de pagamentos. A equipe usa um diagrama de entidade-relacionamento para acordar o modelo de dados compartilhado entre as equipes de contas, de livro-razão e de mensageria, e diagramas C4 (capítulo 3.1) para mostrar como os serviços se encaixam. Eles modelam o ciclo de vida da transação (pendente, compensada, liquidada, estornada, contestada) como uma máquina de estados explícita, e a análise revela que falta uma transição para estornos parciais. A lacuna é corrigida num quadro-branco e não em produção. Diagramas de sequência percorrem o fluxo de liquidação contra os requisitos (capítulo 2.8) para trazer à tona caminhos ausentes de tempo limite e de nova tentativa. A entrega do dia a dia é ágil, mas o algoritmo central de conciliação, onde um erro significa dinheiro real perdido, recebe uma especificação formal e é verificado por verificação de modelos antes da implementação. A modelagem se concentra onde estão o dinheiro e a ambiguidade e é mantida leve em todo o resto.

**Governo.** Uma agência tributária nacional moderniza a apuração de benefícios. Como as regras de elegibilidade são fixadas em lei e auditadas, a equipe escreve uma especificação formal das regras como transformações puras e verifica propriedades-chave, como nenhum requerente ser ao mesmo tempo elegível e inelegível e todo caso chegar a uma decisão, para que os auditores possam rastrear os resultados até a legislação. Ao lado do núcleo formal, a equipe constrói um protótipo descartável do formulário de entrada voltado ao cidadão para testar com usuários reais. Aprende que um assistente de várias etapas reduz erros, depois descarta o protótipo e reconstrói a entrada com padrões de produção. Diagramas de atividades documentam o processo de ponta a ponta do atendente para treinamento e auditoria. As regras de alta consequência recebem rigor formal, a experiência incerta do usuário recebe prototipagem barata e nenhum dos métodos é aplicado onde o outro pertence.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da modelagem vem de encontrar defeitos mais cedo, onde são muito mais baratos de corrigir. Uma contradição encontrada num quadro-branco custa minutos. A mesma contradição encontrada em produção pode custar uma queda de serviço, um programa de retrabalho ou, em domínios regulamentados, uma responsabilidade legal. Os modelos também reduzem o custo total de propriedade ao servirem de comunicação durável. Um sistema que sobrevive a seus autores, o caso normal em empresas e governo, é muito mais barato de manter quando seu modelo de dados, suas máquinas de estados e seus fluxos principais estão documentados com precisão.

Os custos são reais, e você precisa pesá-los. Os modelos levam tempo para construir, habilidade para construir bem e esforço contínuo para manter atuais, e os métodos formais acrescentam mão de obra especializada. O ponto de equilíbrio é governado por incerteza e consequência. Onde ambas são baixas, a modelagem pesada destrói valor e as heurísticas ágeis vencem. Onde qualquer uma é alta, a modelagem direcionada e, para o núcleo crítico, a verificação formal, se pagam muitas vezes ao evitar a classe cara de falha. Para defender o caso junto à liderança, ligue o investimento em modelagem a riscos específicos aposentados e à manutenibilidade de sistemas de longa vida. E acompanhe se os modelos são de fato consultados, porque um modelo sem uso é puro custo.

## Antipadrões e armadilhas

- **Modelar por modelar:** produzir diagramas porque um processo os exige, não porque informam uma decisão.
- **Modelos obsoletos tomados como verdade:** diagramas que já não correspondem ao código mas ainda são usados como base.
- **Grande design inicial:** modelos exaustivos produzidos antes de qualquer código, fixando decisões tomadas com a menor informação.
- **Proliferação de diagramas:** todo tipo de UML aplicado uniformemente, afogando as poucas visões úteis em ruído.
- **Métodos formais em toda parte:** aplicar verificação cara a código em que a consequência da falha não a justifica.
- **Promoção acidental de protótipo:** um protótipo descartável entregue em silêncio como o produto.
- **Notação acima da substância:** discutir a correção da UML em vez de se o modelo responde à pergunta.

## Modelo de maturidade

- **Nível 1 (Iniciar):** A modelagem é ad hoc ou ausente e puramente reativa. Nenhum método é nomeado. Os modelos, quando desenhados, são inconsistentes, não analisados e abandonados assim que a reunião termina.
- **Nível 2 (Desenvolver):** Algumas equipes desenham diagramas comuns e seguem um método nomeado, mas a prática é desigual na organização: os modelos costumam ser produzidos de forma cerimonial, derivam do código e raramente são analisados quanto a defeitos.
- **Nível 3 (Padronizar):** Uma notação compartilhada, um guia documentado de escolha de método e regras de consistência são definidos e impostos em toda a organização. Os modelos são escolhidos pelo propósito, mantidos em sincronia com o sistema, revisados quanto a defeitos, e o método é ajustado ao risco de cada problema.
- **Nível 4 (Gerenciar):** A modelagem é medida e controlada em relação a linhas de base. As equipes acompanham quantos defeitos a análise pega antes da implementação, o quanto os modelos derivam do código, se cada modelo foi de fato consultado para uma decisão real e o retrabalho e o tempo de ciclo economizados em relação a uma linha de base definida. A escolha do método é calibrada à incerteza e à consequência medidas, e os núcleos críticos são verificados formalmente contra metas de cobertura acordadas.
- **Nível 5 (Orquestrar):** A modelagem e a escolha de método são continuamente melhoradas e integradas ao planejamento de entrega e de risco em toda a organização. O investimento se adapta conforme a incerteza e a consequência mudam, os modelos são rotineiramente mantidos atuais, aposentados ou aprofundados com base em evidências, e os métodos formais, heurísticos e de prototipagem são compostos de modo que cada um fique exatamente onde compensa.

## Ideias para discussão

- No seu último projeto, quais modelos informaram uma decisão real, e quais foram desenhados só porque um processo os exigiu?
- Onde, nos seus sistemas, uma especificação formal se pagaria, e onde seria desperdício?
- Como você decide se um protótipo é descartável ou evolutivo, e vocês impõem essa decisão?
- Como você impede que os modelos saiam de sincronia com o código, ou aceita que alguns devam ser apagados em vez disso?
- Qual é a quantidade certa de modelagem antes do código no seu contexto, e como ela muda com a incerteza?
- Que modelo comportamental (de estado, de sequência ou de atividade) teria pegado o seu incidente de produção mais recente?

## Principais conclusões

- Um modelo é uma abstração com propósito. Se você não consegue nomear a decisão que ele informa, não o desenhe.
- Ajuste os modelos estruturais e comportamentais à pergunta específica e mantenha-os consistentes e atuais.
- Analise os modelos. Um modelo não verificado é uma premissa não testada.
- Os métodos heurísticos e ágeis servem à maioria dos sistemas. Reserve os métodos formais para os núcleos de alta consequência.
- Use protótipos para aposentar a incerteza e decida de antemão se são descartáveis ou evolutivos.
- Invista em modelagem em proporção à incerteza que ela resolve e ao custo de errar a decisão.

## Referências e leitura complementar

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
