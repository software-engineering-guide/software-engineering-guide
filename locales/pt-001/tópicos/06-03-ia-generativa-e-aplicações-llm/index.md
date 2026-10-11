# 6.3 IA generativa e aplicações de LLM

## Visão geral e motivação

A [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), e os [grandes modelos de linguagem](https://en.wikipedia.org/wiki/Large_language_model) (LLMs) em particular, conseguem produzir texto fluente, código, resumos e dados estruturados a partir de instruções em linguagem natural. Isso os torna blocos de construção poderosos para assistentes, busca, processamento de documentos e automação. Mas essas forças vêm com um perfil de risco distintivo. Os LLMs são probabilísticos. Podem produzir falsidades confiantes ([alucinações](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). São sensíveis ao modo como vocês os instruem. E abrem novas superfícies de ataque como a [injeção de prompt](https://en.wikipedia.org/wiki/Prompt_injection) (instruções maliciosas contrabandeadas para as entradas para sequestrar o comportamento do modelo). Então construir aplicações dependentes de LLM é menos sobre o modelo e mais sobre a engenharia em torno dele: como vocês fornecem contexto, ancoram as respostas em conhecimento confiável, restringem as saídas e avaliam a qualidade.

Para grandes equipes, as aplicações de LLM pedem novos padrões que diferem tanto do software tradicional quanto do aprendizado de máquina clássico. Muitas vezes não há etapa de treinamento. Em vez disso, o comportamento é moldado por prompts, contexto recuperado, definições de ferramentas e guardrails (verificações em tempo de execução que restringem as entradas e saídas do modelo). Isso desloca o esforço de engenharia para o gerenciamento de contexto, a qualidade da recuperação, a orquestração e a avaliação. As empresas que adotam LLMs em escala precisam de padrões compartilhados para que cada equipe não redescubra do jeito difícil os mesmos modos de falha.

As organizações governamentais e reguladas enfrentam exigências extras. Um LLM que fabrica uma citação de política ou vaza dados sensíveis não é meramente um bug: pode ser um incidente legal ou de segurança. Esses contextos exigem ancoragem em fontes autoritativas, validação estrita de saída, supervisão humana para saídas consequentes e registros claros do que o sistema foi solicitado a fazer e do que produziu. As técnicas deste capítulo (geração aumentada por recuperação, guardrails e avaliação rigorosa) são o que torna os LLMs seguros o bastante para implantar em contextos de alto risco. Os modelos Claude da Anthropic são uma opção de ponta entre vários provedores capazes. As práticas aqui se aplicam seja qual for o modelo que vocês escolham.

## Princípios fundamentais

- Ancorem o modelo em conhecimento confiável em vez de depender do que ele memorizou.
- Tratem prompts e contexto como artefatos projetados e versionados, não cadeias descartáveis.
- Presumam que o modelo pode estar errado ou ser manipulado. Validem as saídas e restrinjam as ações.
- Deem ao modelo apenas o contexto e as ferramentas de que precisa, nada mais, para reduzir o erro e a superfície de ataque.
- Avaliem continuamente com conjuntos de teste offline, métricas online e julgamento humano.
- Mantenham humanos no circuito para saídas consequentes.
- Projetem o modelo como um componente não confiável dentro de um sistema confiável.

## Recomendações

### Projete os prompts e gerencie o contexto deliberadamente

Tratem os prompts como código: guardem-nos em controle de versões, revisem as mudanças e testem-nas contra uma suíte de exemplos. Estruturem cada prompt com clareza: papel e tarefa, restrições, exigências de formato e exemplos onde ajudarem. Tratem a janela de contexto (o trecho fixo de texto que o modelo consegue considerar de uma vez) como um recurso escasso. Incluam a informação mais relevante, ordenem-na com cuidado e removam o ruído, porque o contexto irrelevante ou excessivo degrada a qualidade e eleva o custo. Para aplicações de vários turnos, gerenciem explicitamente o estado da conversa, resumindo ou truncando o histórico para ficar dentro dos limites mantendo o que importa. Prefiram instruções claras e exemplos de poucos disparos (few-shot: um punhado de demonstrações resolvidas incluídas no prompt) a truques elaborados que quebram no instante em que um modelo muda.

### Ancore as respostas com geração aumentada por recuperação (RAG)

Para tarefas intensivas em conhecimento, recuperem documentos relevantes de um corpus confiável e forneçam-nos ao modelo como contexto, dizendo-lhe para responder só a partir desse material e citar suas fontes. O RAG mantém o conhecimento atual sem retreinamento, confina as respostas ao conteúdo aprovado e permite citação e verificação. Invistam na qualidade da recuperação: dividam os documentos em trechos de forma sensata, escolham [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (representações vetoriais numéricas que põem significados semelhantes próximos) adequados ao seu domínio e verifiquem se as passagens recuperadas de fato contêm a resposta, porque uma resposta fluente construída sobre a passagem errada é pior que nenhuma resposta. E quando nada de relevante aparece, façam o sistema dizer isso em vez de inventar conteúdo.

### Construa agentes e uso de ferramentas com comedimento

Os LLMs podem chamar ferramentas (busca, bancos de dados, calculadoras, APIs internas) e podem ser compostos em agentes que planejam e agem em vários passos. Isso acrescenta capacidade real, mas também multiplica o risco: cada ferramenta é mais um jeito de um modelo errado ou manipulado causar dano. Definam as ferramentas com esquemas precisos, validem cada argumento, apliquem o menor privilégio e exijam confirmação ou aprovação humana para ações consequentes como enviar comunicações ou mover dinheiro. Mantenham os laços de agentes limitados, observáveis e interrompíveis. Comecem com ferramentas de escopo bem delimitado e de propósito único antes de recorrer à autonomia irrestrita.

### Acrescente guardrails e valide as saídas

Envolvam o modelo em camadas de defesa. Na entrada, filtrem e detectem a injeção de prompt, em especial quando conteúdo não confiável (páginas web, documentos de usuários) entra no contexto. Na saída, validem a estrutura contra um esquema, confiram as alegações contra as fontes, filtrem conteúdo inseguro ou não conforme e rejeitem ou tentem de novo quando a validação falha. Para saídas estruturadas, interpretem e verifiquem em vez de confiar na formatação do modelo. Nunca deixem a saída bruta do modelo disparar ações irreversíveis sem validação. Tratem a mitigação de alucinações como uma propriedade do sistema que vocês alcançam por ancoragem, citação, validação e revisão humana, e não algo que o modelo gerencia sozinho.

### Avalie offline, online e com humanos

Construam uma suíte de avaliação de entradas representativas com saídas sabidamente corretas ou pontuadas por rubrica e rodem-na a cada mudança de prompt ou de modelo (avaliação offline). Meçam o comportamento real em produção com métricas como sucesso na tarefa, taxa de escalonamento e feedback do usuário (avaliação online). Para a qualidade subjetiva, usem revisores humanos e, com cuidado, a avaliação por modelo. A avaliação é a rede de segurança que permite mudar prompts e modelos com confiança. Sem ela, vocês voam às cegas.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor quando |
|---|---|---|---|
| Prompt puro | Simples, rápido, barato de mudar | Ancoragem limitada, pode alucinar | Tarefas amplas, baixo risco |
| RAG | Atual, ancorado, citável | A recuperação é difícil de acertar | Tarefas factuais pesadas em conhecimento |
| Agentes com ferramentas | Poderosos, podem agir | Maior superfície de ataque, mais difíceis de controlar | Automação bem delimitada com guardrails |
| Modelo maior e mais forte | Melhor qualidade e raciocínio | Maior custo e latência | Tarefas complexas ou de alto risco |
| Modelo menor e mais barato | Rápido e barato | Mais fraco em tarefas difíceis | Alto volume, tarefas simples |

A tensão central é capacidade versus controle e custo. Mais autonomia e modelos maiores entregam mais valor, mas exigem mais guardrails, mais avaliação e mais dinheiro. A ancoragem por RAG melhora a confiabilidade ao custo da engenharia de recuperação. O equilíbrio certo depende do que está em jogo: as aplicações de alto risco se inclinam para a ancoragem, a validação e a supervisão humana, mesmo quando isso custa mais.

## Perguntas para discutir com sua equipe

1. **Que patamar de exatidão e de ancoragem uma funcionalidade de LLM precisa cruzar antes de enfrentar o público, e quem assina?** Uma resposta fluente que cita a fonte errada ou inventa uma política é pior que nenhuma resposta, e no governo uma citação fabricada é um incidente legal e não um bug. Para uma grande equipe, um patamar explícito impede que cada grupo defina o seu próprio limiar privado por impressão. Levem a definição de vocês de “ancorado o bastante”: se toda alegação precisa se rastrear a uma fonte recuperada e verificada, se o sistema deve recusar quando a recuperação vem vazia e o que o seu conjunto adversarial de avaliação de fato cobre. O sinal a observar é se alguém hoje consegue entregar uma mudança de prompt direto aos usuários sem rodar uma regressão. Se o que está em jogo é legal ou de segurança, a resposta deve rotear as saídas de maior risco por um revisor humano com autoridade real antes do lançamento.

2. **Quais das nossas funcionalidades de LLM são secretamente agentes, e cada ferramenta recebeu o menor privilégio e um portão humano nas ações irreversíveis?** Qualquer funcionalidade que deixa o modelo chamar ferramentas ou agir em vários passos cruzou para o território dos agentes, e cada ferramenta é mais um jeito de um modelo errado ou manipulado causar dano. Para empresas que ligam LLMs a APIs internas, essa pergunta traz à tona um risco que o rótulo de “assistente simples” esconde. Levem um inventário de toda ferramenta que o modelo pode invocar, sua validação de argumentos, seu escopo de privilégio e quais ações (enviar comunicações, mover dinheiro, alterar registros) exigem confirmação. Discutam se os laços de agentes são limitados, observáveis e interrompíveis. A resposta deve apertar os escopos e acrescentar portões de aprovação humana onde uma ação consequente ou irreversível hoje é alcançável sem um.

3. **Como saberíamos em um dia que a nossa qualidade de recuperação caiu, dado que uma resposta confiante construída sobre a passagem errada parece boa?** O RAG só torna as respostas confiáveis quando a recuperação de fato traz à tona a passagem que contém a resposta, e a recuperação apodrece em silêncio à medida que os documentos mudam, os trechos ficam obsoletos ou os embeddings se afastam do seu domínio. Como o modelo continua escrevendo com fluência sobre um contexto ruim, os usuários talvez não reclamem até a confiança já estar perdida. Levem as medidas atuais de latência e de revocação da recuperação, como vocês conferem se as passagens recuperadas realmente contêm a resposta e como o frescor do índice acompanha as mudanças nos documentos. Para implantações de alto risco ou públicas, discutam registrar as fontes recuperadas para auditoria, para poder rastrear uma resposta ruim até a sua passagem ruim. Se vocês não têm nenhuma avaliação de recuperação, estão ancorando na fé.

4. **Tratamos prompts, contexto e conjuntos de avaliação como artefatos versionados e revisados, ou como cadeias espalhadas por cadernos e logs de bate-papo?** Quando os prompts se espalham entre equipes sem versão e duplicados, uma correção em um lugar nunca chega aos outros, e ninguém consegue reproduzir o que o sistema foi instruído a fazer no trimestre passado. Para uma grande equipe, um registro compartilhado de prompts e uma suíte de regressão que roda a cada mudança são o que permite trocar um modelo ou editar uma instrução sem quebrar em silêncio uma funcionalidade duas equipes adiante. A atração concorrente é a velocidade: os engenheiros iteram mais depressa quando colam um prompt e entregam, então combinem onde fica a linha entre experimentos rápidos e qualquer coisa que toque os usuários. Levem onde os seus prompts de fato vivem hoje, se um conjunto de avaliação condiciona as mudanças e como vocês versionam o corpus de recuperação ao lado do prompt. Em contextos corporativos e governamentais, acrescentem a exigência de auditoria: vocês podem ter de mostrar exatamente qual prompt e quais fontes produziram uma dada saída meses depois, e um prompt que vocês não conseguem reconstruir é um registro que vocês não conseguem defender.

5. **À medida que o volume cresce, como controlaremos o custo de inferência sem degradar a qualidade em silêncio, e quem é dono da decisão de seleção do modelo?** O TCO das funcionalidades de LLM é dominado pela inferência por chamada, e custos que parecem triviais num piloto se compõem depressa na escala de produção, tentando as equipes a baixar discretamente para um modelo mais fraco e torcer para que ninguém note a queda de qualidade. Para uma grande organização, deixar cada equipe escolher modelos e limites de custo por impressão produz tanto contas surpresa quanto qualidade inconsistente. A troca genuína é capacidade versus custo e latência: um modelo maior raciocina melhor em tarefas difíceis, um menor é mais barato e mais rápido em tarefas simples, e o cache, o roteamento e o escopo da recuperação todos movem o número. Levem o custo por tarefa resolvida, a qualidade por nível de modelo no seu conjunto de avaliação e onde o inchaço de prompt ou de contexto está inflando o gasto em tokens. No orçamento corporativo e governamental, nomeiem quem aprova a escolha do modelo e o teto de gasto, porque uma linha de custo de que ninguém é dono é uma que ninguém controla quando o tráfego triplica.

6. **Que dados sensíveis podem chegar ao modelo, para onde esses dados vão e conseguimos provar que ficaram dentro dos limites?** Todo prompt, documento recuperado e resultado de ferramenta pode carregar dados pessoais ou confidenciais para dentro do modelo e, com um provedor hospedado, para fora do seu perímetro, e um vazamento aqui é um incidente legal ou de segurança e não um chamado de defeito. Para uma grande equipe que liga LLMs a sistemas internos, o risco se esconde na tubulação: um corpus de recuperação que inclui registros que um dado usuário nunca deveria ver, ou logs que capturam entradas brutas. A tensão é capacidade versus exposição, já que a redação de dados e o escopo apertado podem embotar a funcionalidade que vocês tentam construir. Levem um mapa de fluxo de dados do que entra no contexto, os termos de retenção e de treinamento do provedor e como vocês redigem, delimitam e registram os campos sensíveis. Em contextos regulados e públicos, liguem isso às regras de residência de dados, aos deveres de retenção de registros e aos limites contratuais de como um fornecedor pode usar os seus dados, porque uma supervisão que vocês não conseguem evidenciar é uma supervisão que vocês não têm.

## Perspectiva por setor

**Startup.** Entreguem uma única funcionalidade de LLM estreita que toque o seu valor central, construída sobre um modelo hospedado com recuperação sobre o seu próprio conteúdo, e mantenham os prompts no git atrás de uma interface fina para poder trocar de provedor. Rodem um pequeno arquivo de avaliação com perguntas reais antes de cada mudança, filtrem o texto colado pelo usuário para embotar a injeção de prompt e limitem rigidamente o gasto mensal. Resistam aos agentes e à hospedagem própria: um laço de chamada de ferramentas sem limites que vocês não conseguem supervisionar é um passivo, não uma demonstração.

**Pequena empresa.** Vocês provavelmente não têm especialista em ML, então comprem funcionalidades de LLM embutidas em ferramentas que já usam em vez de pôr gente numa construção. Enquadrem o risco como uma pergunta simples: onde uma resposta errada e confiante custaria um cliente, e quem confere a saída antes de ela sair. Prefiram fornecedores que mostrem suas fontes, deixem vocês manterem um humano no circuito e tornem a IA fácil de desligar quando se comporta mal.

**Grande empresa.** O problema é a escala entre muitas equipes: publiquem padrões compartilhados para RAG, guardrails e esquemas de ferramentas, mais um arcabouço comum de avaliação e um registro de prompts, para que cada grupo pare de redescobrir os mesmos modos de falha. Orcem o custo de inferência e a revisão humana explicitamente, padronizem a camada de interface para que os modelos continuem trocáveis e governem os agentes de forma central, com menor privilégio, laços limitados e registro de auditoria. Gerenciem as funcionalidades de LLM como um portfólio, com métricas e critérios de encerramento, e não um amontoado de pilotos.

**Governo.** A transparência, as regras de contratação e a responsabilização moldam toda escolha. Ancorem estritamente em fontes aprovadas com citações, recusem quando a recuperação vem vazia e proíbam o modelo de declarar lei que não consegue citar. Mantenham um oficial responsável revisando as saídas consequentes, registrem as entradas e as fontes recuperadas para auditoria, rodem um conjunto adversarial de avaliação antes de cada lançamento e exijam no contrato a divulgação das limitações do modelo e dos termos de tratamento de dados.

## Exemplos

**Startup.** Uma startup de ferramentas para desenvolvedores de três pessoas acrescentou um assistente de bate-papo sobre sua documentação para que os usuários parassem de mandar e-mails com perguntas básicas. Usou RAG para que toda resposta citasse uma página específica da documentação, instruiu o modelo a dizer “não tenho certeza, eis a quem perguntar” quando a recuperação vinha vazia e manteve os prompts no git. Antes de cada mudança, rodava os prompts contra um pequeno arquivo de perguntas reais de usuários para pegar regressões e filtrava o texto colado pelo usuário para embotar a injeção de prompt. O assistente tratava as perguntas comuns e passava o resto, em silêncio, para a caixa de entrada compartilhada dos fundadores.

**Grande empresa.** Uma empresa de software construiu um assistente interno de suporte sobre a documentação do seu produto. Usou [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) para que as respostas citassem páginas específicas da documentação, disse ao modelo para responder “não sei” quando a recuperação falhava e verificou que toda fonte citada de fato existia. Os prompts eram versionados e testados contra uma suíte de perguntas reais de suporte a cada mudança. O assistente desviava chamados de rotina e escalava para atendentes humanos tudo de baixa confiança, enquanto métricas online acompanhavam as taxas de resolução e de correção.

**Governo.** Um órgão público implantou um assistente de LLM para ajudar os servidores a redigir respostas a consultas de cidadãos. A ancoragem era estrita: o modelo só podia compor respostas a partir de orientações aprovadas, com citações, e era proibido de declarar política que não estivesse nas fontes recuperadas. Um oficial responsável revisava cada rascunho antes de ele sair. O filtro de entrada protegia contra a injeção de prompt vinda de documentos enviados por cidadãos, as saídas eram registradas para auditoria e um conjunto de avaliação com consultas adversariais e de casos de borda rodava antes de cada lançamento para confirmar que o sistema se recusava a especular sobre questões de lei.

## Justificativa de negócio: motivações, ROI e TCO

As aplicações de LLM entregam ROI automatizando o trabalho pesado em linguagem: responder perguntas, resumir documentos, redigir conteúdo e extrair estrutura de texto não estruturado. O valor aparece como chamados desviados, redação mais rápida, menos revisão manual e novas capacidades de autoatendimento. Como muitas vezes não há etapa de treinamento, o tempo até o primeiro valor é curto, um grande atrativo.

O TCO, porém, é dominado pelo custo contínuo de inferência, pela infraestrutura de recuperação, pelos pipelines de avaliação, pelos sistemas de guardrails e pela revisão humana. Os custos por chamada se somam depressa em escala, e uma aplicação sem monitoramento pode derivar para comportamento inseguro ou caro. O custo de não adotar é ficar para trás em qualidade de serviço e produtividade da equipe. O custo de adotar sem cuidado é um incidente público de alucinação ou um vazamento de dados. Defendam o caso junto à liderança combinando uma meta concreta de produtividade com um plano concreto de segurança e de avaliação e orçando os guardrails e a supervisão humana que tornam durável o valor.

## Antipadrões e armadilhas

- **Confiar na saída fluente.** Confundir texto confiante e bem escrito com texto correto.
- **RAG sem avaliação da recuperação.** Presumir que a recuperação funciona e nunca conferir se ela traz as passagens certas.
- **Cegueira à injeção de prompt.** Alimentar prompts com conteúdo não confiável sem defesas.
- **Agentes sem limites.** Deixar os agentes tomarem ações consequentes sem limites ou aprovação humana.
- **Sem arcabouço de avaliação.** Mudar prompts e modelos no palpite, sem teste de regressão.
- **Proliferação de prompts.** Prompts espalhados, sem versão e duplicados entre equipes.
- **Automação excessiva.** Tirar os humanos de decisões que carregam peso legal ou de segurança.

## Modelo de maturidade

1. **Iniciar.** Prompts ad hoc em projetos isolados. Sem ancoragem, guardrails nem avaliação. Os prompts vivem onde alguém os colou, e as alucinações são descobertas em produção.
2. **Desenvolver.** Algumas equipes acrescentam RAG e versionamento de prompts, validação básica de saída e um pequeno conjunto manual de avaliação, mas as práticas variam de equipe para equipe e repousam em campeões individuais e não numa expectativa compartilhada.
3. **Padronizar.** Padrões documentados para RAG, guardrails, esquemas de ferramentas e versionamento de prompts são impostos em toda a organização. A avaliação offline automatizada roda a cada mudança de prompt ou de modelo. Os fluxos de alto risco carregam métricas online e revisão humana.
4. **Gerenciar.** O portfólio é medido em relação a linhas de base: a revocação da recuperação, as taxas de alucinação e de recusa, a cobertura de defesa contra injeção, o custo e a latência por chamada e as taxas de escalonamento e de correção são acompanhados em painéis. Os portões de lançamento e os critérios de encerramento disparam com base em evidências e não em opinião, e uma execução de regressão bloqueia qualquer mudança que mova uma métrica na direção errada.
5. **Orquestrar.** A avaliação contínua, offline e online, é ligada a resultados de negócio. As defesas contra injeção, os agentes e a ancoragem são governados e observáveis. A organização rotineiramente aposenta, reajusta e redimensiona funcionalidades de LLM e troca modelos à medida que qualidade, custo e risco mudam.

## Ideias para discussão

- Como vocês decidem quais saídas exigem revisão humana antes do uso?
- Qual é o seu padrão de “ancorado o bastante” antes de uma resposta poder ser mostrada aos usuários?
- Como vocês se defendem da injeção de prompt quando conteúdo não confiável precisa entrar no contexto?
- Quando um agente vale o risco adicional versus um design mais simples, de chamada única?
- Como vocês avaliam a qualidade subjetiva em escala sem depender demais da avaliação por modelo?
- Como vocês mantêm os prompts mantíveis e consistentes entre muitas equipes?

## Principais conclusões

- A confiabilidade vem da engenharia em torno do modelo: contexto, ancoragem, guardrails e avaliação.
- O RAG ancora as respostas em fontes confiáveis e permite citação e verificação.
- Tratem o modelo como um componente não confiável. Validem as saídas e restrinjam o uso de ferramentas.
- Deem aos agentes o menor privilégio, laços limitados e aprovação humana para ações consequentes.
- Avaliem offline, online e com humanos continuamente. É o que torna seguras as mudanças.

## Referências e leitura complementar

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
