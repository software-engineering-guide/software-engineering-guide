# 2.11 Qualidade de software

## Visão geral e motivação

A [qualidade de software](https://en.wikipedia.org/wiki/Software_quality) é quão bem um sistema atende às necessidades declaradas e às expectativas razoáveis. Isso significa mais que funcionar: significa se o sistema é confiável, seguro, mantível, utilizável, de bom desempenho e adequado ao seu propósito ao longo do tempo. A qualidade é mais ampla que o teste. O teste (capítulo 2.4) é uma atividade que revela defeitos. A qualidade é a disciplina inteira de construir a coisa certa e bem e de saber, com evidências, que você o fez. Um sistema pode passar em todos os testes e ainda ser de baixa qualidade se for impossível de manter, inacessível ou mal ajustado ao que os usuários de fato precisam.

Numa equipe grande, a qualidade não pode morar na cabeça de uma pessoa nem nos hábitos de uma equipe. Centenas de engenheiros, vários produtos e sistemas de longa vida precisam de uma definição compartilhada de qualidade, de processos explícitos para garanti-la e de medições que digam se ela está melhorando ou piorando. Sem isso, a “qualidade” vira uma aspiração vaga que perde toda discussão para um prazo, e os defeitos se acumulam até a mudança ficar lenta e arriscada.

Em contextos corporativos e governamentais o que está em jogo sobe ainda mais. Os sistemas regulamentados, críticos para a segurança e voltados ao cidadão precisam demonstrar a qualidade, não apenas afirmá-la: processos documentados, evidências rastreáveis e verificação independente são muitas vezes obrigatórios. A má qualidade carrega custo financeiro, jurídico e de reputação diretos e, em alguns domínios, coloca pessoas em perigo. Uma disciplina deliberada de qualidade, construída de modelos, processos, medição e cultura, é o que transforma a qualidade de um acidente em um resultado gerenciado.

## Princípios fundamentais

- Qualidade é adequação ao propósito mais conformidade com os requisitos. Defina ambos explicitamente.
- A qualidade é embutida, não testada depois. A verificação encontra defeitos, mas a prevenção os evita.
- Distinga a [garantia da qualidade](https://en.wikipedia.org/wiki/Quality_assurance) (nossos processos são sólidos?) do [controle de qualidade](https://en.wikipedia.org/wiki/Quality_control) (este produto é bom?).
- A verificação pergunta “construímos certo?”. A validação pergunta “construímos a coisa certa?”
- Meça a qualidade com um pequeno conjunto de métricas significativas. Trate as métricas como sinais, não como metas.
- O custo de um defeito sobe quanto mais tarde ele é encontrado, então desloque as atividades de qualidade para mais cedo.
- A qualidade é uma propriedade da organização inteira e de sua cultura, não um portão no fim.

## Recomendações

### Adote um modelo de qualidade compartilhado como o ISO/IEC 25010

Dê à sua organização um vocabulário comum de qualidade adotando um modelo reconhecido de qualidade do produto. O [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) define características que incluem adequação funcional, eficiência de desempenho, compatibilidade, usabilidade, confiabilidade, segurança, manutenibilidade e portabilidade. Use-o para tornar a qualidade concreta: para cada sistema, decida quais características mais importam e o que significa “bom o bastante” para cada uma. Essas características de qualidade do produto são os mesmos **atributos de qualidade** que dirigem a arquitetura (capítulo 3.1). Qualidade e arquitetura são duas visões de uma só preocupação, então deixe que compartilhem uma só lista de prioridades em vez de duas concorrentes.

### Separe a garantia da qualidade do controle de qualidade

Trate a garantia da qualidade (QA) e o controle de qualidade (QC) como atividades distintas mas complementares. A QA é orientada ao processo e preventiva: melhora a forma como o trabalho é feito, por meio de padrões, revisões, definições de pronto e treinamento, de modo que os defeitos tenham menos probabilidade de aparecer logo de início. O QC é orientado ao produto e detectivo: inspeciona os produtos de trabalho reais, como o teste, a [revisão de código](https://en.wikipedia.org/wiki/Code_review) e as auditorias, para pegar os defeitos que entraram. Uma organização madura investe em ambos, mas se inclina para a QA, porque prevenir defeitos é mais barato que encontrá-los e corrigi-los.

### Conduza processos explícitos de gestão da qualidade de software

Faça da qualidade um processo gerenciado, não uma esperança silenciosa. Para trabalho significativo, escreva um plano de qualidade que declare as características de qualidade-alvo, as atividades de garantia e de controle, os critérios de aceitação e quem é responsável. Teça-o nas práticas que você já tem: a revisão de código (capítulo 2.5) como controle e como forma de compartilhar conhecimento, a estratégia de testes (capítulo 2.4) como a rede de segurança automatizada e a [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis) como inspeção contínua. Revise os dados de qualidade regularmente e aja sobre as tendências, em vez de apenas reagir a incidentes.

### Pratique a verificação e a validação como disciplinas distintas

A verificação confirma que os produtos de trabalho atendem às suas especificações, de modo que as entradas certas de cada etapa produzam as saídas certas, por meio de revisões, análise estática e testes contra os requisitos. A validação confirma que o sistema acabado de fato atende às necessidades dos usuários e ao uso pretendido, por meio de testes com usuários, testes de aceitação, pilotos e feedback do campo. Você precisa dos dois. Um sistema pode estar correto em relação a uma especificação falha (verificado mas não válido), ou pode atender a uma necessidade real e ainda conter defeitos (válido mas não verificado). Em ambientes regulamentados, pode ser exigida uma [verificação e validação](https://en.wikipedia.org/wiki/Verification_and_validation) independentes (IV&V) por uma parte separada dos desenvolvedores.

### Meça a qualidade com métricas significativas

Escolha um pequeno conjunto de métricas que reflitam os resultados de qualidade e seus direcionadores e acompanhe-as ao longo do tempo. As medidas úteis incluem densidade de defeitos, taxa de escape de defeitos (defeitos encontrados em produção versus antes do lançamento), tempo médio para detectar e para reparar, taxa de falha de mudanças, sinais de saúde do código como complexidade e duplicação e sinais de validação como problemas relatados por usuários e conformidade de acessibilidade. Fuja de métricas de vaidade e manipuláveis: uma métrica que vira meta deixa de medir a realidade. Combine os números com sinais qualitativos de revisões e do feedback dos usuários.

### Caracterize e gerencie os defeitos sistematicamente

Trate os defeitos como dados, não apenas como incêndios a apagar. Classifique-os por gravidade, tipo e causa-raiz. Acompanhe-os da descoberta à resolução. Procure padrões para poder prevenir a recorrência. Use técnicas como a [análise de causa-raiz](https://en.wikipedia.org/wiki/Root_cause_analysis) e a categorização de defeitos para distinguir erros isolados de fraquezas sistêmicas. Realimente a QA com o que você aprende, por meio de padrões atualizados, testes acrescentados e revisões melhoradas, para que a mesma classe de defeito não volte. Um defeito corrigido sem entender sua causa é um defeito que você convidou a voltar.

### Gerencie o custo da qualidade deliberadamente

Entenda a economia da qualidade pelas categorias clássicas: custos de prevenção (treinamento, padrões, bom design, ferramentas), custos de avaliação (revisões, testes, auditorias) e custos de falha (retrabalho interno antes do lançamento, mais as falhas externas encontradas pelos usuários, que custam muito mais). Desloque o seu investimento para a prevenção e a avaliação precoce, porque cada real ali evita muitos reais de custo de falha depois. Torne esses custos visíveis, para que “não temos tempo para qualidade” seja visto pelo que é: uma escolha de gastar mais com a falha.

### Construa uma cultura de qualidade

Faça da qualidade responsabilidade de todos, de propriedade das equipes que constroem o software, em vez de entregá-la a um departamento de QA a jusante que a inspeciona no fim. Os líderes devem recompensar os resultados de qualidade, tornar seguro relatar defeitos e quase-acidentes e tratar os dados de qualidade como ferramenta de aprendizado e não como porrete. Uma abordagem sem atribuição de culpa aos defeitos traz os problemas à tona cedo. Uma abordagem de culpa os esconde até ficarem caros.

## Compromissos: prós e contras

| Prática / escolha | Prós | Contras |
|---|---|---|
| Modelo formal de qualidade (ISO 25010) | Vocabulário compartilhado. Prioridades explícitas | Custo operacional se aplicado dogmaticamente |
| Garantia da qualidade pesada (prevenção) | Menos defeitos. Menor custo total | Investimento inicial. Mais lento para mostrar retorno |
| Controle de qualidade pesado (inspeção) | Pega defeitos que escapam | Caro. Encontra defeitos tarde |
| V&V independente | Alta garantia. Objetiva | Cara. Mais lenta. Pode parecer hostil |
| Métricas ricas de qualidade | Visibilidade. Alerta precoce | Risco de manipulação. Custo de medição |
| Equipe dedicada de QA | Foco e especialização | Pode tirar a responsabilidade dos desenvolvedores |
| Qualidade de propriedade das equipes | Responsabilidade. Feedback rápido | Exige disciplina e habilidade em toda parte |

O compromisso central é investimento versus garantia, moldado pelo momento. A prevenção custa dinheiro agora para evitar custos de falha maiores depois. Assim, o nível economicamente certo de qualidade não é o máximo: é o ponto em que o custo marginal de mais garantia iguala o custo de falha que ela evita. Esse ponto fica alto para sistemas críticos para a segurança e mais baixo para ferramentas internas de baixo risco. A outra tensão recorrente é a responsabilidade. Os grupos centrais de QA constroem especialização mas podem deixar os desenvolvedores se desresponsabilizarem. A qualidade de propriedade das equipes constrói responsabilidade mas exige habilidade e disciplina em toda parte.

## Perguntas para discutir com sua equipe

1. **Quando a mesma classe de defeito aparece duas vezes, fazemos análise de causa-raiz ou apenas a corrigimos de novo?** Um defeito corrigido sem entender sua causa é um defeito que você convidou a voltar, e numa equipe grande a mesma causa-raiz pode surgir em muitos serviços antes de alguém ligar os pontos. Tratar os defeitos como dados (classificados por gravidade, tipo e causa e depois minerados em busca de padrões) é o que separa uma equipe que fica cada vez mais confiável de uma que continua ocupada corrigindo o mesmo erro. Leve o seu rastreador de defeitos à reunião e procure assinaturas recorrentes: quantos incidentes recentes compartilham uma causa que vocês nunca trataram de forma sistêmica? A resposta deve alimentar a prevenção, de modo que uma causa recorrente conduza a um padrão atualizado, a um novo auxiliar compartilhado, a um teste acrescentado ou a uma lista de verificação de revisão melhor, porque é assim que uma correção num lugar impede que a classe toda volte.

2. **É seguro, na nossa equipe, relatar um defeito ou um quase-acidente, e o que acontece com a pessoa que levanta um?** A qualidade é uma propriedade da cultura, e uma abordagem sem atribuição de culpa traz os problemas à tona cedo, enquanto uma de culpa os esconde até ficarem caros, o que num sistema regulamentado ou voltado ao cidadão pode significar uma falha pública ou uma penalidade. Isso importa mais em escala, onde o engenheiro mais próximo de um risco costuma ser júnior e o incentivo a ficar calado é forte. Leve sinais honestos: os quase-acidentes são registrados e discutidos, ou somem? Os postmortems nomeiam causas ou pessoas? A ação é tornar os dados de qualidade uma ferramenta de aprendizado e não um porrete, recompensar quem traz os problemas à tona e conduzir postmortems sem atribuição de culpa, porque você não consegue prevenir o que a sua equipe tem medo de relatar.

3. **A validação consegue de fato barrar um lançamento, e quem detém essa autoridade quando um prazo se aproxima?** A verificação (construímos certo?) e a validação (construímos a coisa certa?) são disciplinas distintas, e a validação só tem dentes se uma verificação de acessibilidade reprovada, um teste de aceitação reprovado ou uma pesquisa de usuários desfavorável puderem genuinamente impedir a entrega. Em contextos corporativos e governamentais isso costuma ser obrigatório, às vezes por meio de verificação e validação independentes por uma parte separada dos desenvolvedores, e “entregamos assim mesmo” não é uma resposta que um órgão de supervisão aceite. Leve seus últimos lançamentos: algum sinal de qualidade chegou a barrar um, ou o portão sempre cede à data? Se a validação nunca barrou um lançamento, ela é decoração, e a correção é escrever critérios de aceitação no plano de qualidade logo de início, nomear quem é dono da decisão de seguir ou não e dar a essa decisão autoridade real, independente da pressão de entrega.

4. **Conhecemos de fato o nosso custo da má qualidade, e estamos deliberadamente deslocando o gasto da falha para a prevenção?** O custo da má qualidade (COPQ) é o dinheiro perdido em retrabalho interno, incidentes de produção, correções emergenciais, carga de suporte, usuários perdidos e penalidades, e quase sempre é maior que o gasto visível em revisões e testes. Numa equipe grande, os custos de falha estão espalhados por canais de incidentes, filas de suporte e retrabalho que ninguém registra como retrabalho, de modo que permanecem invisíveis até alguém somá-los. A tensão é que a prevenção custa dinheiro agora, num ciclo orçamentário, para evitar custos de falha que caem depois e caem no orçamento de outra pessoa, o que torna fácil adiar a troca para sempre. Leve números reais: contagem e custo de incidentes, horas de retrabalho, taxa de defeitos escapados e a divisão atual do gasto entre prevenção, avaliação e falha, e então decida se a mistura deve se deslocar para mais cedo. Para sistemas corporativos e governamentais, onde a maior parte do custo do ciclo de vida cai depois do primeiro lançamento, ponha o COPQ diante de quem detém o orçamento, porque um número que um órgão de supervisão consegue ver é muito mais difícil de trocar do que um apelo vago à “qualidade”.

5. **Quais das nossas métricas de qualidade viraram metas em silêncio, e que comportamento estão agora conduzindo?** Uma métrica que vira meta deixa de medir a realidade: persiga um percentual de cobertura e você obtém testes escritos para mover o número, não testes que pegam defeitos. Em escala isso é perigoso, porque um painel de destaque compartilhado por dezenas de equipes define os incentivos de todas elas, e uma métrica manipulável espalha a manipulação por toda parte de uma vez. A consideração concorrente é que você ainda precisa de medição, então a resposta raramente é “abandonar a métrica” e sim “combiná-la com um contrassinal e lê-la ao lado de evidências qualitativas de revisões e de usuários”. Leve o seu conjunto atual de métricas e, para cada uma, pergunte o que alguém sob pressão poderia fazer para movê-la sem melhorar a qualidade e se você já viu isso acontecer. Em contextos regulamentados e voltados ao cidadão, desconfie especialmente de métricas de conformidade que parecem verdes enquanto a validação subjacente (acessibilidade, resultados reais para o usuário) nunca foi genuinamente exercitada, pois um auditor acabará testando a realidade por trás do número.

6. **Quem é dono da qualidade aqui: as equipes que escrevem o código, ou um grupo separado no fim, e qual dos dois estamos de fato financiando?** A responsabilidade molda tudo a jusante, porque um silo de QA a jusante deixa os desenvolvedores se desresponsabilizarem do código que escrevem, enquanto a qualidade de propriedade das equipes constrói responsabilidade ao custo de exigir habilidade e disciplina em cada equipe. Numa equipe grande isso não é um ou outro: o padrão sustentável costuma ser equipes donas da qualidade por meio da revisão de código e dos testes automatizados, apoiadas por um pequeno grupo central que mantém os padrões, conduz a garantia da qualidade como melhoria de processo e faz coaching, em vez de inspecionar a qualidade no fim. Leve um mapa honesto de onde o trabalho de qualidade acontece hoje, quem é responsável quando um defeito escapa e onde o orçamento e o quadro de pessoal de fato estão versus onde a retórica diz que a qualidade mora. Para empresas e organizações governamentais, acrescente a exigência de verificação e validação independentes: alguns regimes de garantia exigem uma parte separada, então decida deliberadamente quais controles pertencem às equipes de entrega e quais precisam permanecer independentes para satisfazer a auditoria.

## Perspectiva por setor

**Startup.** A velocidade importa mais que a cerimônia, então nomeie as duas ou três características de qualidade que de fato protegem o seu produto, em geral confiabilidade e manutenibilidade, e deixe o polimento esperar. Seja dono da qualidade na equipe toda com revisão de código e uma suíte modesta de testes automatizados, em vez de montar um grupo de QA separado que você não consegue sustentar. Quando a mesma classe de bug aparece duas vezes, gaste vinte minutos na causa-raiz e acrescente um auxiliar compartilhado mais um teste, para que a prevenção continue barata e a sua taxa de falha de mudanças continue baixa enquanto você se move rápido.

**Pequena empresa.** Sem especialista dedicado em qualidade e com orçamento apertado, apoie-se na qualidade embutida nas ferramentas e plataformas que você compra, e não num processo que você precise conduzir. Ao escolher um software, trate a evidência de qualidade do fornecedor como parte da compra: postura de segurança, acessibilidade, rapidez de resposta do suporte e com que frequência os lançamentos dele quebram. Acompanhe um punhado de sinais baratos e honestos (incidentes de produção, problemas relatados por clientes, tempo para corrigir) em vez de um elaborado programa de métricas que você não tem quem mantenha.

**Grande empresa.** O trabalho é a consistência entre muitas equipes: adote um modelo de qualidade compartilhado como o ISO/IEC 25010, separe a garantia da qualidade (processo) do controle de qualidade (produto) e conduza revisões de custo da qualidade que desloquem o gasto para a prevenção. Mantenha a qualidade sob responsabilidade das equipes de entrega, apoiadas por um pequeno grupo central que mantém padrões e painéis de taxa de escape de defeitos, taxa de falha de mudanças e tendências de saúde do código. Padronize o vocabulário e os portões para que os grupos parem de reinventar a prática de qualidade, deixando às equipes espaço para atingir essas barras à sua maneira.

**Governo.** A contratação, a transparência e a responsabilização pública definem o quadro, então escreva requisitos de qualidade nos contratos e exija evidências de qualidade documentadas e rastreáveis em vez de afirmações. Espere uma verificação e validação independentes por uma parte separada dos desenvolvedores, conformidade de acessibilidade obrigatória e registros de defeitos com gravidade e causa-raiz mantidos como parte da trilha de auditoria. Relate as cifras do custo da má qualidade (retrabalho, recursos, falhas de serviço) aos órgãos de supervisão e dê à validação autoridade real para barrar um lançamento que falharia com os cidadãos que dependem dele.

## Exemplos

**Startup.** Uma startup de cinco pessoas decide que, para o seu produto inicial, confiabilidade e manutenibilidade são as características de qualidade que importam, e deixa o polimento pixel-perfeito esperar. A qualidade é de propriedade da equipe toda: a revisão de código e uma suíte modesta de testes automatizados são os controles, e não há um grupo de QA separado a quem entregar defeitos. Quando a mesma classe de bug aparece duas vezes, gastam vinte minutos num rápido exame de causa-raiz e acrescentam um auxiliar compartilhado mais um teste, para que ela pare de recorrer em vez de ser corrigida de novo à mão a cada vez. Esse pequeno hábito de prevenção mantém baixa a taxa de falha de mudanças enquanto ainda se movem rápido.

**Grande empresa.** Uma grande empresa de serviços financeiros adota o ISO/IEC 25010 como seu vocabulário de qualidade e, para cada produto, registra níveis-alvo de confiabilidade, segurança e manutenibilidade. As equipes são donas da qualidade: a revisão de código e os testes automatizados são controles no pipeline, enquanto um pequeno grupo central conduz a QA mantendo padrões e fazendo coaching. Um painel de qualidade acompanha a taxa de escape de defeitos, a taxa de falha de mudanças e as tendências de saúde do código. Os defeitos são classificados e têm a causa-raiz analisada, e as causas recorrentes impulsionam atualizações em bibliotecas compartilhadas e listas de verificação. A liderança revisa trimestralmente os dados de custo da qualidade e deslocou o gasto para a prevenção, reduzindo tanto os incidentes de produção quanto o custo de corrigi-los.

**Governo.** Uma agência nacional que entrega uma plataforma de benefícios voltada ao cidadão trabalha sob um regime de garantia que exige evidências de qualidade documentadas. Ela conduz um processo formal de gestão da qualidade com um plano de qualidade por lançamento, mais verificação e validação independentes por uma equipe separada dos desenvolvedores. A verificação confere cada produto de trabalho contra requisitos rastreados até a política. A validação inclui testes de conformidade de acessibilidade e pesquisa de usuários com cidadãos reais, e qualquer um dos dois pode barrar um lançamento. Os defeitos são acompanhados com gravidade e causa-raiz como parte da trilha de auditoria, e as cifras do custo da má qualidade (retrabalho, recursos e falhas de serviço) vão aos órgãos de supervisão para justificar o investimento contínuo em prevenção.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da qualidade é um custo total de propriedade menor e uma velocidade de entrega estável. O custo da qualidade tem dois lados. O bom gasto, prevenção e avaliação, é visível e controlável: design, padrões, revisões, testes e ferramentas. O custo da má qualidade (COPQ) é maior, mas muitas vezes oculto: retrabalho interno, incidentes de produção, correções emergenciais, suporte ao cliente, usuários perdidos, penalidades regulatórias e dano à reputação. Estudos que remontam ao “Quality Is Free” de Crosby constatam de forma consistente que o custo total da má qualidade faz sombra ao custo de preveni-la e que os defeitos ficam muito mais caros quanto mais tarde você os pega: um problema encontrado no design custa uma fração do mesmo problema encontrado em produção.

Para a liderança, o argumento não é “gastar mais em qualidade”. É “gastar mais cedo para gastar menos no total”. Quantifique o COPQ a partir dos seus próprios dados (contagem e custo de incidentes, horas de retrabalho, taxa de defeitos escapados) e mostre como a prevenção e a avaliação precoce o reduzem. Ligue a qualidade aos resultados de negócio: a confiabilidade retém clientes, a manutenibilidade mantém barata a mudança futura e a segurança e a acessibilidade mantêm você longe de problemas jurídicos. Em sistemas corporativos e governamentais de longa vida, onde a maior parte do custo cai depois do primeiro lançamento, as dimensões de manutenibilidade e de confiabilidade da qualidade dominam o custo do ciclo de vida. Isso faz do investimento inicial em qualidade uma das decisões de maior alavancagem que você pode tomar.

## Antipadrões e armadilhas

- **Qualidade como portão final:** inspecionar a qualidade no fim em vez de embuti-la, de modo que os defeitos são encontrados quando são mais caros.
- **Confundir teste com qualidade:** presumir que testes aprovados significam alta qualidade, ignorando manutenibilidade, usabilidade e adequação ao propósito.
- **QA como silo separado:** uma equipe a jusante que “é dona da qualidade”, deixando os desenvolvedores se desresponsabilizarem do código que escrevem.
- **Teatro de métricas:** perseguir percentuais de cobertura ou contagens de defeitos como metas, o que convida à manipulação e esconde a qualidade real.
- **Verificação sem validação:** construir corretamente a especificação sem nunca checar se a especificação atende às necessidades reais.
- **Sem análise de causa-raiz:** corrigir os defeitos um a um sem tratar a causa sistêmica, de modo que a mesma classe recorre.
- **Ignorar o custo da má qualidade:** tratar a qualidade como custo puro porque os custos de falha são ocultos e não medidos.

## Modelo de maturidade

**Nível 1 (Iniciar).** A qualidade é indefinida e ad hoc. Ela se apoia na diligência individual, é conferida principalmente por testes manuais no fim e os defeitos são tratados de forma reativa à medida que surgem. Não há modelo compartilhado, métricas nem fronteira entre garantia e controle.

**Nível 2 (Desenvolver).** Aparecem práticas básicas: revisão de código, testes automatizados e um rastreador de defeitos. Alguns dados de qualidade são coletados, mas de forma desigual, e cada equipe o faz à sua maneira. A qualidade ainda é vista sobretudo como teste, a prevenção é mínima, a verificação acontece e a validação é informal.

**Nível 3 (Padronizar).** A organização adota um modelo de qualidade compartilhado (como o ISO/IEC 25010), separa a QA do QC e conduz processos de gestão da qualidade com planos de qualidade e critérios de aceitação, documentados e aplicados de forma consistente entre as equipes. A verificação e a validação são distintas e deliberadas, e os defeitos são classificados e têm a causa-raiz analisada segundo um esquema acordado.

**Nível 4 (Gerenciar).** A qualidade é medida e controlada em relação a linhas de base. Um pequeno conjunto de métricas significativas é acompanhado ao longo do tempo (densidade de defeitos, taxa de escape de defeitos, tempo médio para detectar e reparar, taxa de falha de mudanças e sinais de saúde do código como complexidade e duplicação), e o custo da qualidade é quantificado entre prevenção, avaliação e falha. Os portões de aceitação e de qualidade são impostos com base em evidências e não em opinião, as tendências são revisadas numa cadência fixa e a validação pode genuinamente barrar um lançamento.

**Nível 5 (Orquestrar).** A qualidade é uma disciplina continuamente melhorada e culturalmente apropriada, integrada ao planejamento de negócio e de risco. A prevenção é a ênfase, os dados de custo da qualidade orientam onde vai o investimento e as constatações de causa-raiz previnem sistematicamente a recorrência. As equipes são donas da qualidade de ponta a ponta, as métricas alimentam a melhoria contínua e a organização adapta sua prática de qualidade conforme produtos, riscos e regulamentação mudam. Isso se alinha aos níveis mais altos dos modelos de maturidade do capítulo 10.8.

## Ideias para discussão

- Quais características de qualidade do ISO/IEC 25010 mais importam para os seus sistemas, e o que é “bom o bastante” para cada uma?
- Onde a sua organização se situa na mistura de gasto entre prevenção, avaliação e falha, e ela deveria se deslocar?
- Vocês distinguem verificação de validação na prática, ou colapsam as duas em “teste”?
- A qualidade é de propriedade das equipes que constroem o software ou delegada a um grupo separado, e o que mudaria se vocês a movessem?
- Qual é o seu verdadeiro custo da má qualidade, e vocês conseguiriam medi-lo bem o bastante para fazer o argumento de negócio?
- Quais das suas métricas de qualidade são sinais genuínos, e quais viraram metas manipuláveis?

## Principais conclusões

- A qualidade é mais ampla que o teste: é adequação ao propósito mais conformidade, em características como confiabilidade, segurança e manutenibilidade.
- Use um modelo de qualidade compartilhado (ISO/IEC 25010) para que os atributos de qualidade sejam explícitos e se alinhem com a arquitetura (capítulo 3.1).
- Separe a garantia da qualidade (prevenir, processo) do controle de qualidade (detectar, produto) e incline-se para a prevenção.
- Pratique a verificação (construímos certo) e a validação (construímos a coisa certa) como disciplinas distintas.
- Meça a qualidade com poucas métricas significativas e caracterize os defeitos por gravidade e causa-raiz para prevenir a recorrência.
- Gerencie o custo da qualidade: a prevenção e a avaliação precoce são muito mais baratas que a falha, especialmente em sistemas de longa vida.
- Construa uma cultura de qualidade sem atribuição de culpa em que as equipes sejam donas da qualidade, apoiadas pela revisão de código (capítulo 2.5) e pela estratégia de testes (capítulo 2.4).

## Referências e leitura complementar

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
