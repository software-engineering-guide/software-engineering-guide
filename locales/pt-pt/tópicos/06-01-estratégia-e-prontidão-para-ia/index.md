# 6.1 Estratégia e prontidão para IA

## Visão geral e motivação

A [inteligência artificial](https://en.wikipedia.org/wiki/Artificial_intelligence) passou de novidade de pesquisa a capacidade central que as grandes organizações agora devem implantar com responsabilidade e em escala. Para empresas e agências governamentais, a pergunta real já não é se a IA consegue fazer algo impressionante numa demonstração. É se um investimento específico resolve um problema real melhor que as alternativas, pode ser operado com segurança por anos e consegue sobreviver a auditoria, contratação e escrutínio público. A estratégia de IA é a disciplina de decidir onde aplicar a IA, onde evitá-la e de que fundações vocês precisam antes de o primeiro modelo chegar à produção.

Para grandes equipes, a escala e a inércia elevam as apostas. Uma iniciativa mal enquadrada pode queimar orçamentos, distrair engenheiros talentosos e corroer a confiança de reguladores e cidadãos quando falha em público. Uma bem escolhida pode automatizar o trabalho enfadonho, trazer discernimento de dados que vocês nunca conseguiriam alcançar antes e liberar pessoas habilidosas para trabalho de maior valor. A diferença raramente é o modelo em si. Resume-se a quão bem vocês enquadram o problema, quão prontos estão os seus dados e talentos e quão honesto é o seu argumento de negócio.

Os contextos governamental e regulado acrescentam mais restrições. Os órgãos públicos precisam justificar gastos, garantir transparência, evitar discriminação ilícita e prestar contas a autoridades eleitas e ao público. As regras de contratação podem proibir o aprisionamento por fonte única, exigir explicabilidade e requerer que os fornecedores exponham o comportamento do modelo. Aqui, tratem a conformidade, a auditabilidade e as opções de saída como exigências de primeira classe, não reflexões tardias.

## Princípios fundamentais

- Comecem de um problema que vale resolver, não de uma tecnologia à procura de um uso.
- Prefiram a abordagem mais simples que atende à necessidade. A IA é uma opção entre muitas, e muitas vezes não a melhor.
- Tratem a prontidão de dados, de talentos e da plataforma como pré-requisitos, não como frentes de trabalho paralelas a resolver depois.
- Façam as decisões entre construir e comprar explicitamente e revisitem-nas à medida que o mercado e as suas capacidades mudam.
- Quantifiquem o custo total de propriedade, incluindo operação, monitoramento e eventual substituição, e não apenas a licença ou o piloto.
- Projetem a saída desde o primeiro dia: evitem arquiteturas que tornem proibitivamente caro trocar de fornecedor ou de modelo.
- Em contextos regulados e públicos, tratem a transparência, a conformidade de contratação e a responsabilização como restrições de design.
- Meçam o custo de *não* agir ao lado do custo de agir.

## Recomendações

### Enquadre o problema antes de escolher uma tecnologia

Escrevam uma declaração de problema de uma página. Nomeiem a decisão ou tarefa que querem melhorar, a linha de base atual, o resultado mensurável que querem e o que acontece quando o sistema erra. Depois perguntem se o problema sequer se presta à IA. Há dados relevantes suficientes? A tarefa é baseada em padrões e não em regras? Vocês toleram respostas probabilísticas? Um humano consegue conferir a saída? Muitos problemas são mais bem resolvidos com software determinístico, melhor desenho de processo ou simplesmente melhor higiene de dados. Escrevam explicitamente onde a IA *não* é um bom ajuste: por exemplo, decisões que precisam ser perfeitamente explicáveis por lei, ou em que o custo de um erro raro é catastrófico e impossível de pegar.

### Use uma árvore de decisão entre construir, comprar, ajustar finamente e fazer prompt

Movam-se do mais barato e rápido ao mais caro e controlado:

1. **Façam prompt num modelo hospedado existente.** Se um modelo de uso geral (como o Claude da Anthropic, ou ofertas comparáveis de outros provedores) resolve o problema com prompts cuidadosos e recuperação, façam isso primeiro. Menor custo, iteração mais rápida, sem infraestrutura de treinamento.
2. **Aumentem com recuperação ou ferramentas.** Se a lacuna é de conhecimento ou de ações, acrescentem a [geração aumentada por recuperação](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), que busca documentos relevantes na hora da consulta e os fornece ao modelo como contexto, e o uso de ferramentas antes de tocar nos pesos do modelo.
3. **Ajustem finamente ou adaptem.** Se o prompt não consegue atingir de forma consistente a exatidão, o tom ou o formato necessários, façam o [ajuste fino](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) (fine-tuning) de um modelo menor com os seus dados: isto é, treinem mais um modelo pré-treinado com os seus exemplos para especializá-lo. Isso compra controle ao custo de um pipeline de [MLOps](https://en.wikipedia.org/wiki/MLOps) (operações de aprendizado de máquina).
4. **Comprem um produto especializado.** Para domínios bem definidos (processamento de documentos, pontuação de fraude), um produto maduro de fornecedor pode vencer qualquer coisa que vocês construam.
5. **Construam do zero.** Reservem o treinamento de [modelos de fundação](https://en.wikipedia.org/wiki/Foundation_model) (modelos grandes pré-treinados em dados amplos e adaptáveis a muitas tarefas) para organizações com dados únicos, talento profundo e razões estratégicas. Para quase todas as empresas e agências, essa é a escolha errada.

### Estabeleça os pré-requisitos de dados, talentos e plataforma

Auditem os seus dados quanto a disponibilidade, qualidade, rotulagem, linhagem e base legal de uso. Confirmem que vocês de fato têm o direito de usá-los para IA, inclusive quaisquer dados pessoais ou de terceiros. Avaliem os talentos com honestidade: vocês precisam de cientistas de dados e também de engenheiros de ML, engenheiros de dados, gerentes de produto que entendam sistemas probabilísticos e revisores capazes de avaliar saídas. Antes de escalar, levantem uma linha de base de plataforma: rastreamento de experimentos, um registro de modelos (o sistema de registro das versões treinadas de modelos e de seu status de aprovação), monitoramento e serviço seguro, para que cada novo caso de uso não reinvente as operações.

### Trate deliberadamente os contextos regulados e governamentais

Tragam cedo as equipes de contratação, jurídico e risco. Exijam que os fornecedores divulguem a proveniência do modelo, as práticas de dados de treinamento, os resultados de avaliação e as limitações conhecidas. Prefiram contratos que concedam portabilidade dos seus dados e prompts e evitem formatos proprietários que os prendam. Onde apropriado, publiquem a finalidade e as salvaguardas dos sistemas de IA voltados ao público e deem às pessoas um canal para contestar decisões automatizadas. Alinhem-se a frameworks reconhecidos (veja o capítulo 6.5) para que as auditorias achem um processo documentado e defensável.

### Calcule o custo total de propriedade e proteja-se contra o aprisionamento

Modelem o custo do ciclo de vida inteiro: inferência ou licenciamento, pipelines de dados, revisão humana, monitoramento, retreinamento, resposta a incidentes e desativação. Comparem com o custo do status quo e das alternativas. Reduzam o aprisionamento pondo o modelo atrás de uma interface interna, mantendo portáveis os prompts e os conjuntos de dados de avaliação e testando um segundo provedor de tempos em tempos.

## Compromissos: prós e contras

| Abordagem | Prós | Contras | Melhor quando |
|---|---|---|---|
| Prompt num modelo hospedado | Rápido, barato, sem infraestrutura, fácil de trocar | Menos controle, custo por chamada, questões de compartilhamento de dados | Protótipos, tarefas amplas, requisitos incertos |
| Aumento por recuperação | Ancora as respostas nos seus dados, atualizável | A qualidade da recuperação é difícil, acrescenta infraestrutura | Tarefas pesadas em conhecimento |
| Ajuste fino de modelo menor | Controle, menor custo por chamada em escala, opção local | Exige MLOps, dados e manutenção | Tarefas estáveis, de alto volume e especializadas |
| Comprar um produto | Comprovado, com suporte, rápido para dar valor | Custo de licença, aprisionamento, ajuste limitado | Problemas commodity bem definidos |
| Construir um modelo de fundação | Máximo controle e diferenciação | Custo enorme, talento raro, alto risco | Quase nunca, fora dos laboratórios de fronteira |

A troca dominante é controle versus custo e velocidade. O prompt dá a máxima velocidade e flexibilidade mas o mínimo de controle. Construir dá o máximo de controle mas exige recursos que poucas organizações deveriam gastar. A maioria das grandes equipes deve viver no meio: fazer prompt e recuperação primeiro, ajustar finamente seletivamente e comprar para necessidades commodity. O aprisionamento troca conveniência de curto prazo por risco de longo prazo, e isso importa especialmente no governo, onde as obrigações de saída de vários anos são comuns.

## Perguntas para discutir com sua equipe

1. **Onde cada um dos nossos três principais casos de uso candidatos fica na escada de prompt, depois recuperação, depois ajuste fino, depois compra, depois construção, e que evidência o moveria um degrau?** Isso importa porque a maior parte do gasto desperdiçado em IA vem de começar um degrau alto demais: treinar um modelo quando um prompt cuidadoso teria funcionado. Para uma grande equipe, combinar a escada como padrão compartilhado impede que cada grupo reinvente um pipeline caro. Levem a declaração de problema de uma página de cada candidato, a linha de base atual e uma leitura honesta de se a lacuna é de conhecimento (recuperação), de consistência (ajuste fino) ou de um commodity resolvido (compra). Em contextos corporativos e governamentais, acrescentem o custo de contratação e de auditoria de cada degrau, já que um modelo ajustado arrasta consigo um ônus de MLOps que uma chamada hospedada não tem. A resposta deve permitir matar ou rebaixar ao menos um projeto de escopo excessivo na sala.

2. **Qual é o nosso plano concreto de saída para o fornecedor ou modelo de que mais dependemos, e de fato o testamos?** O aprisionamento é barato de aceitar e caro de desfazer, e no governo vocês podem carregar obrigações de saída de vários anos que não conseguem cumprir se nunca ensaiaram. Levem a lista de recursos proprietários em que vocês se apoiam, se os prompts e os conjuntos de dados de avaliação são portáveis e como o modelo fica atrás de uma interface interna (ou não fica). O sinal a observar é se alguém já rodou a sua suíte de avaliação contra um segundo provedor. Se não, o plano de saída de vocês é uma esperança e não um plano. Se a resposta honesta é que trocar levaria meses e reescreveria código central, tratem isso como um defeito de design a consertar agora, não uma ponte a cruzar depois.

3. **O que diz um cartão de pontuação honesto de prontidão sobre os nossos direitos de dados, e quais casos de uso ele desqualifica hoje?** Pular a prontidão dos dados é a falha que afunda pilotos em silêncio: o modelo funciona, mas vocês nunca tiveram base legal para usar os dados, ou eles não têm rótulos nem linhagem. Para uma grande organização, os dados pessoais e de terceiros levantam limites de consentimento e contratuais que variam por jurisdição e por conjunto de dados. Levem uma auditoria de disponibilidade, qualidade, rotulagem, linhagem e base legal para cada candidato e estejam dispostos a marcar alguns casos de uso como bloqueados até as fundações de dados existirem. Em contextos regulados e públicos, uma base legal inutilizável não é um atraso, é uma parada obrigatória, e financiar o trabalho de prontidão deve ser uma linha explícita do plano e não uma reflexão tardia.

4. **Como saberemos que um caso de uso de IA em operação está de fato funcionando, e que evidência nos faria matá-lo?** A maioria dos portfólios de IA acumula zumbis: pilotos que foram entregues, impressionaram alguém e agora rodam para sempre sem que ninguém confira se ainda merecem o seu custo. Combinem a linha de base e a métrica de sucesso antes do lançamento e depois definam um limiar explícito de encerramento, para que a decisão de parar seja tomada de antemão e não defendida no momento. Levem a métrica atual, o custo de supervisão humana por resultado e a deriva que vocês viram desde o lançamento. Para portfólios corporativos e governamentais, nomeiem quem revisa cada sistema numa cadência fixa e quem tem autoridade para aposentá-lo. Um caso de uso que ninguém é responsável por revisar é um que ninguém jamais desligará.

5. **Onde um humano permanece no circuito, quanto essa supervisão custa e de fato a orçamos?** Os casos de uso de IA de aparência mais barata são os que presumem em silêncio a automação total e depois vazam custo pela revisão, correção e escalonamento que a realidade força de volta. Decidam deliberadamente quais decisões uma pessoa precisa confirmar, quais o modelo pode tomar sozinho e quais ele nunca pode tomar e depois precifiquem o tempo humano que isso implica. Levem o volume de casos de baixa confiança, o custo de uma resposta errada e o caminho atual de escalonamento. Em contextos regulados e públicos, liguem cada decisão automatizada a um oficial responsável e a uma via de recurso, porque uma supervisão que vocês não conseguem descrever é uma supervisão que vocês não têm.

6. **Temos os talentos e a plataforma para operar o que estamos propondo, ou presumimos em silêncio uma capacidade que não temos?** Os planos ambiciosos de IA falham menos pelo modelo do que pelas fundações pouco glamorosas: ninguém para manter o pipeline, ninguém que consiga avaliar as saídas, nenhuma plataforma em que implantar. Combinem cada caso de uso candidato com as habilidades e a infraestrutura de que ele de fato precisa e sejam honestos onde a lacuna é uma contratação, um parceiro ou um motivo para não construir. Levem um inventário de quem consegue ser dono de cada sistema em produção, em que plataforma ele rodará e quais capacidades vocês teriam de comprar. Para uma organização grande ou pública, acrescentem os prazos de contratação e de recrutamento, já que um plano que depende de talentos que vocês não conseguem recrutar na janela relevante é um plano para entregar menos.

## Perspectiva por setor

**Startup.** A velocidade e a sobrevivência dominam. Escolham um caso de uso estreito que toque o seu valor central, entreguem-no num modelo hospedado atrás de uma interface fina e limitem o gasto com firmeza. Evitem construir infraestrutura ou treinar modelos: o seu recurso mais escasso é a atenção da engenharia, e um pipeline ajustado que vocês não conseguem manter é um passivo, não um fosso de proteção. Mantenham barato o trocar, para poderem seguir um mercado que se move depressa.

**Pequena empresa.** Vocês provavelmente não têm cientistas de dados e têm orçamento apertado, então tratem a IA como algo que se compra embutido em ferramentas que vocês já usam e não um programa em que se põe gente. Enquadrem a prontidão como uma questão de higiene de dados e de privacidade e não um projeto de aprendizado de máquina: saibam que dados de clientes guardam, o que podem fazer com eles e onde uma resposta automatizada errada custaria um cliente. Prefiram fornecedores que tornem a IA opcional, transparente e fácil de desligar.

**Grande empresa.** O problema é a governança de portfólio entre muitas equipes: uma escada compartilhada de construir versus comprar, avaliações consistentes de prontidão e análise de aprisionamento e de custo total para que os grupos parem de reinventar pipelines caros. Orcem explicitamente o ônus de MLOps e de supervisão humana, padronizem a camada de interface para que os provedores continuem trocáveis e gerenciem os casos de uso de IA como um portfólio, com métricas claras e critérios de encerramento, em vez de um amontoado de pilotos.

**Governo.** A transparência, as regras de contratação e a responsabilização moldam toda escolha. Favoreçam sistemas que citam fontes oficiais em vez de gerar política, mantenham um humano responsável por decisões consequentes e exijam nos contratos a portabilidade de dados e a divulgação das limitações do modelo. Publiquem uma descrição em linguagem simples e uma via de recurso, honrem quaisquer obrigações de saída de vários anos que assinarem e mantenham a IA fora das decisões finais de avaliação, que devem repousar com um oficial responsável.

## Exemplos

**Startup.** Uma startup de agendamento de cinco pessoas queria acrescentar um recurso em linguagem natural de “marque uma reunião para mim” sem tirar seus dois engenheiros do produto central. Escolheu o menor problema que importava, transformar um pedido numa proposta de horário, e entregou-o com um modelo hospedado atrás de uma API interna fina para poder trocar de provedor depois. A equipe definiu um teto rígido de gasto mensal, acompanhou se os usuários aceitavam os horários sugeridos e combinou revisitar um modelo ajustado apenas se o volume um dia justificasse o trabalho extra.

**Grande empresa.** Uma seguradora multinacional queria acelerar a triagem de sinistros. Em vez de treinar um modelo sob medida, enquadrou o problema de forma estreita (rotear e resumir os sinistros recebidos), prototipou com um modelo hospedado mais recuperação sobre seus documentos de apólice e mediu contra o tempo de tratamento humano e a exatidão. Só depois de provar valor ajustou finamente um modelo menor para o tipo de sinistro de maior volume, para cortar o custo por chamada. Manteve o modelo atrás de uma API interna para poder trocar de provedor e modelou um TCO de três anos que incluía a revisão humana dos casos de baixa confiança.

**Governo.** Uma autoridade tributária nacional considerou um assistente de IA para ajudar os servidores a responder consultas de cidadãos. Como essas respostas tocavam obrigações legais, a agência insistiu na transparência: o sistema só podia trazer orientações oficiais com citações, nunca inventar política, e um humano revisava cada sugestão automatizada antes de ela sair. A contratação exigiu que o fornecedor divulgasse as limitações do modelo e concedesse portabilidade de dados, e a agência publicou uma descrição em linguagem simples do sistema e uma via de recurso. Manteve a IA fora das decisões finais de apuração por inteiro, reservando-as para oficiais responsáveis.

## Justificativa de negócio: motivações, ROI e TCO

A estratégia de IA existe para ajudar vocês a evitar duas falhas em espelho: investir demais em IA que nunca se paga e investir de menos enquanto concorrentes ou agências pares passam à frente. O ROI vem de trabalho poupado, tempo de ciclo reduzido, taxas de erro menores e novas capacidades viabilizadas. Meçam isso contra uma linha de base genuína e descontem o custo real da supervisão humana, que raramente desaparece.

O TCO precisa incluir os itens pouco glamorosos: pipelines de dados, monitoramento, retreinamento à medida que o mundo deriva, revisão de segurança e eventual desativação. Um piloto que parece barato pode ficar caro quando roda em escala por anos. Apresentem também o custo de *não* adotar: serviço mais lento, maior custo manual e deriva estratégica. Defendam o caso junto à liderança com uma visão de portfólio: algumas apostas de alta confiança, métricas claras de sucesso, critérios de encerramento para as falhas e uma avaliação de prontidão mostrando que as fundações de dados e de talentos existem. Peçam à liderança que financie explicitamente a prontidão. Pulem-na e vocês garantem um caro retrabalho.

## Antipadrões e armadilhas

- **Solução à procura de um problema.** Comprar IA porque os pares compraram e depois caçar um caso de uso.
- **Pular a prontidão de dados.** Lançar modelos sobre dados indisponíveis, sem rótulos ou legalmente inutilizáveis.
- **Decisões guiadas por demonstração.** Comprometer-se com base numa demonstração polida sem uma avaliação de qualidade de produção.
- **Ignorar o circuito humano.** Presumir a automação total e orçar pouco a revisão, que é onde a maior parte do custo se esconde.
- **Aprisionamento silencioso.** Construir fundo sobre os recursos proprietários de um fornecedor sem plano de saída.
- **Subestimar as operações.** Tratar a implantação como linha de chegada e não como o começo de uma obrigação de manutenção.
- **Conformidade como reflexão tardia.** Adaptar a transparência e a auditabilidade depois do design, a múltiplos do custo.

## Modelo de maturidade

1. **Iniciar.** Experimentos ad hoc, sem estratégia compartilhada, decisões conduzidas por hype e entusiasmo individual.
2. **Desenvolver.** O enquadramento do problema existe para alguns projetos. Aparece uma primeira linha de base de plataforma. Construir versus comprar é discutido, mas de modo inconsistente.
3. **Padronizar.** Um portfólio de casos de uso de IA com métricas claras, uma árvore de decisão documentada, avaliações de prontidão e análise de aprisionamento e de TCO, aplicados de modo consistente entre as equipes.
4. **Gerenciar.** O portfólio é medido: prontidão, ROI, TCO e custo de supervisão humana são acompanhados contra linhas de base. Os critérios de encerramento são impostos com base em evidências. O impacto na entrega e na qualidade conduz cada decisão de seguir ou não.
5. **Orquestrar.** A estratégia de IA é integrada ao planejamento de negócio e de risco. A prontidão é mantida continuamente. A organização rotineiramente aposenta, substitui e redimensiona sistemas de IA com base em evidências, reequilibrando o portfólio à medida que o mercado e o quadro de riscos mudam.

## Ideias para discussão

- Como vocês decidem quando um problema é genuinamente inadequado para a IA, e quem tem autoridade para dizer não?
- Que limiar de prontidão deve condicionar um projeto a passar de piloto a produção?
- Quanto aprisionamento é aceitável em troca de um tempo mais rápido até o valor?
- No governo, como as obrigações de transparência devem moldar a escolha entre construir e comprar?
- Como vocês mantêm honestas as estimativas de TCO quando fornecedores e entusiastas têm incentivos para subestimá-las?
- Quem é dono do portfólio de IA, e como são tomadas as decisões de encerramento?

## Principais conclusões

- A estratégia começa com um problema real e uma linha de base honesta, não com uma tecnologia.
- Prefiram a opção mais simples: prompt, depois recuperação, depois ajuste fino, depois compra e raramente construir do zero.
- A prontidão de dados, de talentos e da plataforma são pré-requisitos. Financiá-las faz parte do plano.
- Os contextos regulados e governamentais exigem transparência, conformidade de contratação e opções de saída por design.
- Modelem o TCO completo e o custo da inação e protejam-se contra o aprisionamento ao fornecedor desde a primeira decisão de arquitetura.

## Referências e leitura complementar

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
