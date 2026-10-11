# 6.6 Infraestrutura e operações de IA

## Visão geral e motivação

A infraestrutura e as operações de IA são a disciplina de provisionar, escalonar e operar os sistemas especializados de computação, de armazenamento e de serviço que as cargas de IA exigem, fazendo-o com bom custo-benefício, confiabilidade e observabilidade. A IA moderna é cara de rodar. Treinar e servir grandes modelos exige aceleradores escassos ([GPUs](https://en.wikipedia.org/wiki/Graphics_processing_unit) e [TPUs](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), rede de alta largura de banda, armazenamento vetorial em larga escala para recuperação (indexar dados como vetores numéricos para achar depressa itens semelhantes) e camadas de serviço ajustadas para latência e vazão. Acertar essa infraestrutura é a diferença entre uma IA que escala de forma sustentável e uma que consome em silêncio um orçamento enquanto entrega pouco.

Para grandes equipes, os problemas centrais são escala, escassez e custo. Os aceleradores são limitados e caros, então o escalonamento e a utilização importam enormemente. GPUs ociosas são dinheiro queimado, e a inferência mal agrupada em lotes multiplica o custo por requisição. As aplicações pesadas em recuperação precisam de [bancos de dados vetoriais](https://en.wikipedia.org/wiki/Vector_database) que continuem rápidos à medida que crescem. As aplicações de IA generativa precisam de versionamento de prompts, pipelines de avaliação e observabilidade (às vezes chamados de LLMOps) para operar com segurança e melhorar com o tempo. Sem infraestrutura compartilhada e disciplina operacional, cada equipe luta as mesmas batalhas e os custos disparam.

As organizações governamentais e reguladas acrescentam exigências de soberania de dados, segurança e gasto previsível. Podem precisar de implantação local ou em nuvem soberana para que dados sensíveis e modelos nunca saiam de fronteiras controladas. Precisam prever e justificar o gasto de infraestrutura e atender a padrões de segurança e de disponibilidade. As decisões de infraestrutura de IA nesses contextos carregam consequências de vários anos, então tomem-nas com a contratação, a segurança e a saída em mente.

## Princípios fundamentais

- Tratem a computação de aceleradores como um recurso escasso e caro a escalonar e utilizar, não a acumular.
- Otimizem o custo por unidade útil de trabalho, não a capacidade bruta.
- Dimensionem modelos e hardware à tarefa. A maior opção raramente é a mais econômica.
- Projetem o serviço para latência e vazão, com o agrupamento em lotes e o cache como técnicas de primeira classe.
- Tornem os sistemas de IA observáveis: acompanhem continuamente custo, latência, qualidade e erros.
- Versionem e avaliem prompts e modelos com o mesmo rigor do código.
- Planejem a portabilidade e evitem o aprisionamento nas escolhas de infraestrutura e de serviço.

## Recomendações

### Planeje e controle a computação de aceleradores

Prevejam a demanda de treinamento e de inferência separadamente, já que têm formas diferentes. O treinamento é em rajadas e escalonável. A inferência é contínua e sensível à latência. Usem escalonadores e cotas para dividir as escassas GPUs e TPUs entre as equipes, priorizar cargas e elevar a utilização. Meçam a utilização e tratem a ociosidade crônica como um problema a consertar. Misturem capacidade reservada para a carga de base com capacidade sob demanda ou spot para as rajadas, para controlar o custo. Considerem se aceleradores mais baratos ou menores, ou inferência em CPU para modelos leves, bastariam. Escolham entre nuvem, local e híbrido com base no custo na sua escala, nas necessidades de soberania de dados e nos padrões de rajada e mantenham um caminho de saída.

### Construa a infraestrutura de recuperação: embeddings e bancos de dados vetoriais

Para aplicações aumentadas por recuperação, levantem a infraestrutura para gerar [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (representações vetoriais numéricas que põem itens semelhantes próximos) e guardá-los num banco de dados vetorial que suporte [busca aproximada de vizinho mais próximo](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (achar os vetores mais semelhantes sem comparar exaustivamente cada um) rápida na sua escala. Planejem três coisas: o custo e a latência da geração de embeddings, o frescor do índice à medida que os documentos mudam e o ônus operacional de manter os índices consistentes. Avaliem se um banco de dados vetorial dedicado, uma extensão vetorial de um banco existente ou um serviço gerenciado se ajusta melhor à sua escala e à sua tolerância a aprisionamento. Monitorem a latência e a revocação da recuperação, porque a qualidade da recuperação determina diretamente a qualidade da aplicação.

### Otimize o serviço de modelos: lotes, cache e latência

O serviço é onde o custo da inferência e a experiência do usuário são decididos. Usem o **agrupamento em lotes** (batching) para processar várias requisições juntas e elevar a vazão do acelerador, equilibrando o tamanho do lote contra a latência. Usem o **cache** de forma agressiva: façam cache de requisições idênticas ou semanticamente semelhantes, façam cache de embeddings e explorem o cache de prompt ou de prefixo onde a plataforma o suporta para evitar recomputar contexto compartilhado. Definam metas claras de latência e meçam a latência de cauda e não apenas as médias. Roteiem as requisições para modelos de tamanho certo: um modelo pequeno para os casos fáceis, um maior só quando preciso. Escalem automaticamente o serviço conforme a demanda e façam teste de carga antes do lançamento para conhecer a sua capacidade e a sua curva de custo.

### Pratique LLMOps: versionamento de prompts, pipelines de avaliação e observabilidade

Tratem os prompts como artefatos versionados em controle de código-fonte, com revisão e a capacidade de reverter. Construam pipelines de avaliação que rodem suítes de teste offline automaticamente sempre que prompts ou modelos mudam, para pegar regressões antes do lançamento. Instrumentem a produção por completo: registrem entradas, saídas, latência, uso de tokens, custo e erros, com amostragem e salvaguardas de privacidade. Acompanhem os sinais de qualidade e o feedback dos usuários online. Essa observabilidade permite pegar a degradação, controlar o custo, depurar falhas e melhorar os sistemas com segurança: a espinha dorsal operacional da IA generativa em produção.

### Gerencie o custo sem trégua e de forma observável

Atribuam o gasto com IA a equipes e casos de uso para que o custo seja visível e tenha dono. Definam orçamentos e alertas, monitorem o custo por requisição e por resultado e revisem regularmente os maiores motores de custo. Puxem as alavancas que vocês têm: dimensionar modelos, cache, lotes, aparar prompts e contexto e escolher a implantação mais barata que atenda às exigências. Os custos de IA podem escalar com o uso de modos surpreendentes, então a observabilidade contínua de custo é essencial para evitar surpresas desagradáveis.

## Compromissos: prós e contras

| Decisão | Opção A | Opção B | Troca |
|---|---|---|---|
| Localização da computação | Nuvem | Local | Elasticidade e baixo custo inicial versus controle, soberania e economia de regime permanente |
| Capacidade | Reservada | Sob demanda/spot | Custo previsível versus flexibilidade e risco de interrupção |
| Tamanho do lote | Lotes grandes | Lotes pequenos | Vazão e custo versus latência |
| Tamanho do modelo | Modelo grande | Modelo pequeno | Qualidade versus custo e velocidade |
| Armazenamento vetorial | Banco de dados dedicado | Extensão de banco existente | Desempenho em escala versus simplicidade e menos sistemas |
| Cache | Agressivo | Mínimo | Menor custo e latência versus frescor e complexidade |

A troca dominante é custo versus latência e qualidade. O agrupamento em lotes, o cache e os modelos menores cortam o custo mas podem acrescentar latência ou reduzir a qualidade. O equilíbrio certo depende da tolerância da sua aplicação. Local versus nuvem troca controle e economia de regime permanente contra elasticidade e baixo compromisso, uma decisão fortemente moldada pelas necessidades de soberania de dados e pela escala.

## Perguntas para discutir com sua equipe

1. **Qual é o nosso custo por resultado útil hoje, e que alavanca o moveria mais?** A capacidade bruta e as médias por requisição escondem o número que importa: quanto custa entregar uma unidade real de valor e como isso escala com o uso. Para uma grande equipe, a distância entre uma implantação otimizada e uma não otimizada costuma ser de várias vezes em gasto, então essa pergunta transforma uma preocupação vaga com a conta numa lista ordenada de correções. Levem a atribuição atual de custo por equipe e caso de uso, as tendências por requisição e por resultado e os maiores motores de custo. Discutam as alavancas por ordem de ganho: dimensionar modelos, cache (inclusive de prefixo e semântico), lotes e aparar prompts ou contexto. No governo, acrescentem a pressão para prever e justificar gastos de vários anos. A resposta deve atribuir a cada principal motor de custo um dono e uma alavanca, e não um dar de ombros.

2. **Se o nosso provedor atual de inferência dobrasse o preço ou saísse do ar amanhã, com que rapidez poderíamos trocar?** O aprisionamento silencioso é fácil de construir e doloroso de escapar, e as pilhas de serviço são onde ele mais fundo se esconde. Para empresas e especialmente o governo, a portabilidade é uma exigência de contratação e de continuidade e não um luxo. Levem a arquitetura: se os modelos ficam atrás de uma interface interna, se os prompts e as suítes de avaliação são portáveis e quanto comportamento específico de serviço do provedor vocês dependem. O sinal a observar é se alguém já rodou a sua suíte de avaliação contra um segundo provedor ou um segundo alvo de implantação. Se trocar levaria meses e reescreveria caminhos centrais, tratem isso como um defeito de design a tratar agora, já que opções soberanas e locais podem se tornar obrigatórias com pouco aviso.

3. **Qual é a nossa utilização de aceleradores agora, e quanto GPUs ociosas e inferência sem lotes estão queimando?** Os aceleradores são escassos e caros, então a ociosidade crônica e o serviço requisição a requisição drenam em silêncio orçamentos que poderiam financiar mais capacidade. Para uma grande organização que divide GPUs entre equipes, essa pergunta expõe se o escalonamento, as cotas e as prioridades de fato mantêm alta a utilização ou se o hardware acumulado e subutilizado é a norma. Levem números reais de utilização, a sua postura de lotes e de cache e as medições de latência de cauda, não apenas médias, já que os usuários sentem a cauda lenta. Discutam se a demanda de treinamento e a de inferência são previstas separadamente, dadas as suas formas diferentes, e se um modelo menor ou a inferência em CPU bastaria para casos leves. A resposta deve apontar capacidade ociosa específica a recuperar e requisições específicas a agrupar em lotes ou rotear para um modelo de tamanho certo.

4. **Quando uma mudança de prompt ou de modelo é entregue, o que impede uma regressão silenciosa de qualidade ou de custo de chegar aos usuários?** Uma pilha de serviço pode parecer saudável em latência e disponibilidade enquanto as respostas que ela devolve pioram em silêncio ou um novo prompt dobra o uso de tokens por requisição. Para uma grande equipe em que muitos grupos editam prompts e trocam modelos de forma independente, uma mudança sem portão é um incidente de produção esperando para acontecer, e o raio de impacto cresce com cada equipe na plataforma compartilhada. Levem a cobertura de avaliação: quais prompts e modelos têm suítes de teste offline, se essas suítes rodam automaticamente a cada mudança, que limiares de qualidade e de custo condicionam um lançamento e com que rapidez vocês conseguem reverter. Discutam se os prompts vivem em controle de código-fonte com revisão ou se alguém ainda pode editar à mão um prompt de sistema ao vivo. Em contextos corporativos e governamentais, liguem cada mudança a uma trilha de auditoria e a um aprovador nomeado, porque um regulador que pergunta “quem mudou isto e o que vocês testaram” precisa de uma resposta registrada e não lembrada.

5. **Como decidimos entre nuvem, local e implantação soberana, e precificamos a economia real de regime permanente e não a do piloto?** A escolha da localização da computação define a sua curva de custo, a sua postura de soberania de dados e as suas opções de saída por anos, e ainda assim muitas vezes é feita sobre a conta de nuvem de um piloto que não se parece em nada com a produção em escala. Para uma grande organização, a capacidade elástica de nuvem é barata para começar e pode virar a maior linha isolada quando a inferência passa a rodar continuamente, enquanto o local troca baixo compromisso por controle e economia de regime permanente. Levem os volumes previstos de treinamento e de inferência, o ponto de equilíbrio em que o hardware reservado ou próprio vence o sob demanda, as restrições de residência de dados e de segurança e os padrões de rajada que argumentam por híbrido. Em contextos governamentais e regulados, pesem as exigências de nuvem soberana ou local que podem se tornar obrigatórias com pouco aviso e confirmem que a arquitetura mantém os modelos atrás de uma interface interna para que uma mudança forçada não reescreva caminhos centrais.

6. **Somos de fato donos do nosso gasto com IA, e cada equipe consegue ver e responder pelo custo que conduz?** O custo de IA escala com o uso de modos que surpreendem as pessoas, e sem atribuição a conta chega como um número opaco de que nenhuma equipe se sente responsável por encolher. Numa grande organização, um custo de que ninguém é dono é um custo que ninguém otimiza, então a pergunta é se o gasto é marcado por equipes e casos de uso com orçamentos, alertas e tendências por resultado, ou se só é descoberto quando as finanças escalam. Levem o modelo de atribuição de custo, os maiores motores por equipe e as alavancas que cada dono controla: dimensionar modelos, cache, lotes e aparar contexto. Para orçamentos corporativos e governamentais, acrescentem a disciplina de prever e justificar gastos de infraestrutura de vários anos, já que um órgão público que não consegue explicar a conta de computação linha por linha terá dificuldade de defendê-la numa revisão.

## Perspectiva por setor

**Startup.** Não sejam donos de infraestrutura que vocês consigam evitar. Chamem uma API hospedada de inferência, roteiem as requisições fáceis para um modelo pequeno e barato e reservem um maior para os casos difíceis e façam cache agressivo para que prompts repetidos não custem nada. Usem um banco de dados vetorial gerenciado em vez de operar o seu, mantenham os prompts no git com um curto script de avaliação antes de cada mudança e registrem o custo por requisição para que uma conta descontrolada apareça antes de doer. O seu recurso mais escasso é a atenção da engenharia, então comprem operabilidade e mantenham barato o trocar.

**Pequena empresa.** Sem equipe de plataforma, tratem o serviço, a recuperação e a observabilidade como coisas que vocês compram dentro de ferramentas que já usam e não sistemas em que põem gente. Favoreçam inferência gerenciada e busca vetorial gerenciada, com preços transparentes e previsíveis, e definam um teto rígido de gasto e um alerta de cobrança desde o primeiro dia. Enquadrem a decisão como comprar versus construir com honestidade: operar GPUs ou um índice vetorial raramente compensa no seu volume, e um modelo pequeno atrás de uma API hospedada costuma atender à necessidade com uma fração do esforço.

**Grande empresa.** O problema é uma plataforma compartilhada de caminho pavimentado entre muitas equipes: aceleradores em pool, com escalonadores, cotas e prioridades para elevar a utilização, lotes e cache padrão, roteadores de dimensionamento e custo atribuído a cada equipe e caso de uso. Condicionem as mudanças de prompt e de modelo a suítes automatizadas de avaliação, padronizem a camada de interface para que provedores e alvos de implantação continuem trocáveis e gerenciem o custo por resultado como métrica de primeira classe, em vez de cada grupo reinventar infraestrutura cara e subutilizada.

**Governo.** A soberania de dados, a segurança e o gasto previsível moldam toda escolha. Favoreçam a implantação local ou em nuvem soberana para que dados sensíveis e modelos permaneçam dentro de fronteiras controladas, escalonem as escassas GPUs entre departamentos com cotas que vocês consigam justificar na contratação e prevejam a capacidade para defender gastos de vários anos linha por linha. Versionem e avaliem prompts e modelos com uma trilha de auditoria registrada, mantenham observabilidade abrangente sobre custo e qualidade e mantenham os modelos atrás de uma interface interna para que uma mudança forçada para um novo provedor ou plataforma soberana não deixe vocês encalhados.

## Exemplos

**Startup.** Uma pequena startup que opera uma funcionalidade de redação por IA manteve sensata a sua conta sem ser dona de nenhuma GPU. Chamava uma API hospedada de inferência, roteava as requisições fáceis para um modelo pequeno e mais barato e guardava o maior para os casos difíceis e fazia cache das respostas a prompts repetidos. Guardava os prompts no git, com um curto script de avaliação que rodava antes de cada mudança, usava um banco de dados vetorial gerenciado para recuperação para não ter de operar um e registrava o custo por requisição para que os fundadores vissem o gasto subir antes de virar surpresa.

**Grande empresa.** Uma empresa de mídia que opera uma funcionalidade de LLM de alto tráfego cortou substancialmente os custos de inferência. Roteou as requisições fáceis para um modelo pequeno e reservou um modelo maior para as difíceis. Fez cache das respostas a consultas repetidas e ligou o cache de prefixo para o seu prompt de sistema compartilhado. Rodou as GPUs por um escalonador compartilhado para manter alta a utilização, versionou todos os prompts no git com uma suíte automatizada de avaliação condicionando as mudanças e instrumentou o custo por requisição para que cada equipe de produto fosse dona do próprio gasto.

**Governo.** Uma agência nacional com regras estritas de soberania de dados implantou seus sistemas de IA no local, para que dados sensíveis e modelos nunca saíssem do seu ambiente controlado. Escalonou as escassas GPUs entre departamentos com cotas e prioridades, previu a capacidade para justificar a contratação de vários anos e construiu uma plataforma de busca vetorial para recuperação sobre documentos oficiais. Prompts e modelos eram versionados e avaliados antes do lançamento. A observabilidade abrangente acompanhava custo e qualidade, e a arquitetura mantinha os modelos atrás de uma interface interna para preservar um caminho de saída e evitar o aprisionamento.

## Justificativa de negócio: motivações, ROI e TCO

A motivação para uma infraestrutura de IA disciplinada é direta. A IA em escala é cara, e a distância entre uma implantação otimizada e uma não otimizada costuma ser de várias vezes em gasto. O ROI vem de maior utilização dos aceleradores, menor custo por requisição por lotes e cache, modelos de tamanho certo e de evitar o superprovisionamento. A observabilidade e os pipelines de avaliação se pagam prevenindo incidentes caros e permitindo iteração segura.

O TCO abrange a computação de aceleradores (a maior linha para muitas cargas), o armazenamento vetorial, a infraestrutura de serviço, a rede e a equipe de plataforma e de operações para operá-la. Pesem isso contra o custo de não investir: contas de inferência descontroladas, latência ruim que mina a adoção e incapacidade de escalar. Para o governo, acrescentem o custo de falhar nas exigências de soberania ou de segurança. Defendam o caso junto à liderança mostrando as tendências de custo por resultado e uma plataforma de caminho pavimentado que permite a muitas equipes implantar IA com eficiência, em vez de cada uma construir infraestrutura cara e subutilizada.

## Antipadrões e armadilhas

- **Aceleradores ociosos.** Dedicar GPUs escassas a equipes que as deixam subutilizadas.
- **Sem lotes nem cache.** Servir cada requisição individualmente e recomputar contexto compartilhado.
- **O maior modelo por padrão.** Usar um modelo caro onde um pequeno serviria.
- **Cegueira de custo.** Sem atribuição, orçamentos nem visibilidade de custo por requisição até a conta chegar.
- **Prompts sem versão.** Mudar prompts em produção sem versionamento nem portão de avaliação.
- **Negligência com a latência de cauda.** Otimizar a latência média enquanto os usuários sofrem com as caudas lentas.
- **Aprisionamento silencioso.** Construir fundo na pilha de serviço de um provedor sem portabilidade.

## Modelo de maturidade

1. **Iniciar.** Alocação ad hoc de GPUs, reagindo a quem pede mais alto, sem lotes nem cache, sem visibilidade de custo até a conta chegar, prompts editados ao vivo e sem versão, monitoramento mínimo.
2. **Desenvolver.** Algumas equipes adotam escalonamento compartilhado, cache e prompts em controle de versões, mas a prática é inconsistente na organização: um grupo agrupa em lotes e avalia enquanto outro ainda serve cada requisição individualmente e muda prompts à mão.
3. **Padronizar.** Uma plataforma documentada de caminho pavimentado é imposta em toda a organização: escalonamento compartilhado com cotas e prioridades, lotes, cache e dimensionamento padrão, infraestrutura vetorial para recuperação, pipelines automatizados de avaliação que condicionam toda mudança de prompt ou de modelo e atribuição de custo a equipes e casos de uso.
4. **Gerenciar.** A plataforma é medida e controlada em relação a linhas de base: a utilização de aceleradores, o custo por resultado útil, a latência de cauda, a revocação da recuperação e as regressões de qualidade por mudança são acompanhados com alertas e limiares, o custo é de responsabilidade de cada equipe e o seguir ou não sobre uma mudança é decidido com evidências e não por intuição.
5. **Orquestrar.** A infraestrutura melhora e se adapta continuamente: o roteamento, os lotes e o escalonamento se ajustam sozinhos a sinais ao vivo de custo e de qualidade, a capacidade é reequilibrada entre equipes e entre alvos de nuvem, locais e soberanos à medida que demanda e restrições mudam, a portabilidade é ensaiada e o planejamento de infraestrutura é integrado a produto, segurança e contratação.

## Ideias para discussão

- Como vocês elevam a utilização dos aceleradores sem deixar sem recursos as cargas prioritárias?
- Onde fica o equilíbrio certo de lotes e cache para as suas exigências de latência?
- Quando a implantação local ou soberana justifica seu custo sobre a nuvem?
- Como vocês atribuem e controlam o gasto com IA entre muitas equipes?
- O que deve condicionar a chegada de uma mudança de prompt ou de modelo à produção?
- Como vocês mantêm a infraestrutura de serviço portátil o bastante para trocar de provedor?

## Principais conclusões

- Os aceleradores são escassos e caros. Escalonem, dividam e utilizem-nos deliberadamente.
- Lotes, cache e dimensionamento de modelos são as principais alavancas de custo e de latência.
- As aplicações de recuperação precisam de infraestrutura bem operada de embeddings e de busca vetorial.
- O LLMOps (versionamento de prompts, pipelines de avaliação e observabilidade) é a espinha dorsal operacional da IA generativa.
- Gerenciem o custo de forma observável e preservem a portabilidade para evitar o aprisionamento.

## Referências e leitura complementar

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
