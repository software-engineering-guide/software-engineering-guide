# 6.7 Agentes de IA e sistemas agênticos

## Visão geral e motivação

Um **agente de IA** é um [grande modelo de linguagem](https://en.wikipedia.org/wiki/Large_language_model) (LLM) envolvido num laço: recebe um objetivo, pode chamar ferramentas, guarda alguma memória do que fez e decide o próprio passo seguinte até o objetivo ser atingido ou ele desistir. Esse laço é toda a diferença entre um agente e as chamadas simples de prompt e resposta do capítulo 6.3. Uma única chamada responde a uma pergunta. Um agente lê o seu e-mail, busca num banco de dados, abre um chamado, confere o resultado e tenta de novo. O modelo já não está apenas produzindo texto: está escolhendo ações nos seus sistemas.

Essa mudança altera o problema de engenharia. Quando um modelo apenas escreve palavras, uma saída ruim é uma frase ruim. Quando um modelo conduz ferramentas, uma saída ruim pode enviar uma mensagem errada, apagar um registro ou mover dinheiro. Então um [agente inteligente](https://en.wikipedia.org/wiki/Intelligent_agent) se entende melhor como um planejador não confiável sentado dentro de um sistema confiável, e a maior parte do trabalho de vocês vai para limitar o que esse planejador tem permissão de fazer. Este capítulo se apoia diretamente nos fundamentos de LLM do capítulo 6.3, nas preocupações de confiança e responsabilização do capítulo 6.5 e nas práticas de plataforma do capítulo 6.6.

Para grandes equipes, as apostas são tanto organizacionais quanto técnicas. As empresas querem agentes ligados a sistemas internos reais (chamados, finanças, registros de clientes), o que significa que os agentes herdam controles de acesso reais e obrigações reais de gestão de mudanças. O governo acrescenta a responsabilização pública: uma ação autônoma que afeta um cidadão precisa ser explicável, supervisionável e auditável depois do fato. O padrão é poderoso. Implantado sem disciplina, é um jeito rápido de automatizar erros.

## Princípios fundamentais

- Um agente é um modelo mais um laço, ferramentas, memória e um objetivo. O risco mora no laço, não na prosa.
- Limitem a autonomia à tarefa. Deem a menor liberdade que faça o trabalho.
- Prefiram um fluxo de trabalho fixo quando os passos são conhecidos. Recorram à autonomia irrestrita apenas quando não são.
- Tratem cada ferramenta como superfície de ataque e concedam a ela o menor privilégio com que consegue funcionar.
- Ponham um humano no circuito para ações consequentes ou irreversíveis e tornem barata a reversão.
- Avaliem pelo sucesso da tarefa, não pelo que a transcrição parece.
- Rastreiem toda execução. Uma ação que vocês não conseguem reconstruir é uma ação que não conseguem governar.
- O design mais simples que funciona costuma ser o certo. Muitas vezes isso não é um agente de modo algum.

## Recomendações

### Comece por um fluxo de trabalho e acrescente autonomia apenas onde precisar

O erro mais comum é recorrer a um agente autônomo quando um pipeline fixo bastaria. Se vocês já conhecem os passos (extrair campos, validá-los, buscar um registro, redigir uma resposta), escrevam isso como um fluxo de trabalho orquestrado com o modelo preenchendo espaços específicos. A autonomia merece seu lugar quando o caminho genuinamente não pode ser predeterminado, por exemplo pesquisa aberta ou triagem entre muitas ferramentas possíveis. Limitem a autonomia à tarefa: restrinjam o número de passos, o conjunto de ferramentas ao de que este objetivo precisa e definam uma condição clara de parada. Uma boa regra é dar ao modelo exatamente tanta liberdade quanto o problema exige e nem um grau a mais.

### Faça do uso de ferramentas a capacidade central e torne-o seguro

O uso de ferramentas (também chamado de chamada de função) é o que transforma um modelo em agente. Definam cada ferramenta com um esquema preciso, validem cada argumento que o modelo fornece e apliquem o [princípio do menor privilégio](https://en.wikipedia.org/wiki/Principle_of_least_privilege): um agente de relatórios somente de leitura recebe credenciais somente de leitura, nunca um acesso de escrita que poderia mal usar. Rodem as ferramentas dentro de uma [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) para que uma chamada ruim não alcance além do seu raio de impacto. Prefiram muitas ferramentas estreitas e de propósito único a poucas amplas, porque uma ferramenta estreita é mais fácil de raciocinar, de permissionar e de auditar. É o mesmo comedimento que o capítulo 6.3 recomenda para o uso de ferramentas por LLMs, posto aqui no centro.

### Use padrões explícitos de raciocínio e de planejamento

Os agentes funcionam melhor quando seu pensamento é estruturado. Num padrão de raciocinar e agir (popularizado pela pesquisa ReAct), o modelo alterna entre raciocinar sobre a situação e executar uma ação, depois observa o resultado antes de raciocinar de novo. Para objetivos mais difíceis, façam o modelo planejar primeiro (decompor em subtarefas) e depois executar, para poder inspecionar e até aprovar o plano antes de qualquer ferramenta rodar. Mantenham esses laços observáveis e interrompíveis. Um plano que vocês conseguem ler é um plano que conseguem parar.

### Mantenha humanos no circuito para ações consequentes

Decidam, por ferramenta e por ação, se o modelo pode agir sozinho ou precisa perguntar primeiro. As ações reversíveis e de baixo risco (buscar, redigir) podem rodar sem supervisão. As consequentes ou irreversíveis (enviar comunicações externas, mover dinheiro, mudar dados de produção, decidir o caso de um cidadão) exigem um portão com [humano no circuito](https://en.wikipedia.org/wiki/Human-in-the-loop) com autoridade real para dizer não. Projetem para a reversibilidade sempre que puderem: prefiram preparar uma mudança a confirmá-la e façam do desfazer um recurso de primeira classe para que uma ação equivocada custe minutos e não um incidente.

### Trate o modelo de segurança como adversarial

Os agentes alargam a superfície de ataque descrita no capítulo 4.2. A ameaça de destaque é a [injeção de prompt](https://en.wikipedia.org/wiki/Prompt_injection): instruções maliciosas escondidas numa página web, documento ou e-mail que o agente lê e obedece. Intimamente relacionado é o [problema do deputado confuso](https://en.wikipedia.org/wiki/Confused_deputy_problem), em que um atacante engana um agente privilegiado para que use mal o próprio acesso legítimo, por exemplo exfiltrando dados por uma ferramenta que o agente tem permissão de chamar. Presumam que qualquer conteúdo que o agente ingere pode ser hostil. Separem as instruções confiáveis dos dados não confiáveis, restrinjam as ferramentas para que um agente sequestrado não alcance sistemas sensíveis e nunca deixem a saída bruta do modelo disparar uma ação irreversível sem validação.

### Avalie pelo sucesso da tarefa e faça teste de regressão do não determinismo

Julguem os agentes por se cumprem a tarefa, não por a transcrição soar inteligente. Construam um conjunto de avaliação de objetivos representativos com critérios de sucesso verificáveis (o chamado recebeu a prioridade certa, o reembolso correspondeu à política) e rodem-no a cada mudança de prompt, modelo ou ferramenta. Como os agentes são não determinísticos, uma única passada prova pouco: rodem cada caso várias vezes e acompanhem uma taxa de sucesso, não um passou ou falhou. Isso estende a disciplina de avaliação offline e online dos capítulos 6.3 e 6.2 (engenharia de aprendizado de máquina e MLOps) a sistemas cuja saída é uma sequência de ações.

### Instrumente as execuções para observabilidade, custo e tratamento de falhas

Vocês não governam o que não enxergam. Rastreiem toda execução de agente de ponta a ponta (capítulo 6.6): o objetivo, cada passo de raciocínio, cada chamada de ferramenta com seus argumentos e resultado, os tokens gastos e o resultado final. Esse rastreamento é ao mesmo tempo o seu depurador, a sua trilha de auditoria e o seu medidor de custo. Definam orçamentos rígidos para passos, tempo e gasto, porque um agente que entra em laço pode queimar latência e dinheiro depressa. Tratem a falha explicitamente: tentem de novo os erros transitórios de ferramentas com recuo, mas detectem os laços em que o modelo repete uma ação que falha e falhem com segurança em vez de se debater.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor quando |
|---|---|---|---|
| Fluxo de trabalho fixo (o modelo preenche espaços) | Previsível, barato, fácil de testar e auditar | Rígido. Quebra em caminhos imprevistos | Os passos são conhecidos de antemão |
| Agente autônomo único | Flexível, trata objetivos abertos | Mais difícil de controlar, avaliar e limitar | O caminho não pode ser predeterminado |
| Orquestração multiagente | Paralelismo, papéis especializados | Custo de coordenação, erros que se compõem, maior gasto | Uma tarefa realmente se decompõe em partes independentes |
| Ação sem supervisão | Rápida, baixo atrito | Os erros são executados sem verificação | As ações são reversíveis e de baixo risco |
| Portão com humano no circuito | Segurança, responsabilização, reversibilidade | Mais lento, exige capacidade de revisores | As ações são consequentes ou irreversíveis |

A tensão central é autonomia versus controle. Mais autonomia trata mais situações mas exige mais guardrails, mais avaliação e mais dinheiro e falha de modos mais difíceis de prever. Os designs multiagente tentam as equipes com elegância, mas cada agente adicional acrescenta custo de coordenação e mais um lugar onde um pequeno erro se compõe num resultado errado. Resolvam a tensão começando com a menor autonomia que resolve o problema e acrescentando liberdade apenas quando uma tarefa concreta forçar, sempre combinada com uma proteção correspondente.

## Perguntas para discutir com sua equipe

1. **Esta funcionalidade de fato precisa de um agente, ou um fluxo de trabalho fixo seria mais seguro e mais barato?** A autonomia é sedutora, mas a maioria dos trabalhos tem passos conhecíveis que um pipeline orquestrado trata com muito menos risco. Para uma grande equipe, adotar agentes por padrão significa que todo grupo assume ônus de avaliação, de rastreamento e de segurança que um design mais simples evitaria. Levem a tarefa específica e perguntem se os passos dela podem ser predeterminados. Se podem, um agente provavelmente é engenharia em excesso. Reservem a autonomia irrestrita para objetivos em que o caminho genuinamente varia por caso. A resposta deve empurrar a maioria das funcionalidades para um fluxo de trabalho e deixar um conjunto pequeno e deliberado como agentes de verdade.

2. **Para cada ferramenta que o nosso agente pode chamar, qual é a pior coisa que um agente sequestrado poderia fazer com ela, e o que impede isso?** A injeção de prompt e os ataques do deputado confuso viram contra vocês o próprio acesso legítimo do agente, então a lente certa é a adversarial (capítulo 4.2). Inventariem cada ferramenta, seu escopo de privilégio e se uma instrução maliciosa contrabandeada por conteúdo ingerido poderia alcançá-la. Para empresas que ligam agentes a sistemas internos, é aqui que o menor privilégio, a sandbox e os portões humanos nas ações irreversíveis ficam reais. Levem a lista de ferramentas e as credenciais que cada uma detém. Se alguma ação consequente é alcançável sem validação ou verificação humana, essa é a primeira coisa a consertar.

3. **Como saberíamos que a taxa de sucesso de um agente caiu, dado que toda execução parece plausível?** Os agentes são não determinísticos, então uma transcrição que se lê bem ainda pode ter tomado a ação errada, e uma execução verde não prova nada. Perguntem se vocês têm um conjunto de avaliação de objetivos com resultados verificáveis, rodado muitas vezes por caso para produzir uma taxa de sucesso e não uma única passada. Para implantações de alto risco ou públicas, discutam como os rastros de execução permitem reconstruir exatamente o que aconteceu quando algo dá errado (capítulos 6.5 e 6.6). Se o seu único sinal são as reclamações dos usuários, vocês já estão tarde demais. A resposta deve financiar um arcabouço de avaliação antes da escala e não depois de um incidente.

4. **Quais ações deste agente são verdadeiramente irreversíveis, quem detém a autoridade para aprová-las e temos capacidade de revisores para dotar de pessoal esse portão?** A tentação é deixar o modelo agir sem supervisão em tudo, mas um portão humano só é real se uma pessoa nomeada com autoridade para dizer não está disponível quando o agente pergunta. Para uma grande equipe, uma fila de aprovação de que ninguém é dono vira em silêncio um carimbo de borracha, e a segurança que vocês projetaram evapora sob volume. Levem a lista completa de ações que o agente pode tomar, marquem cada uma como reversível ou irreversível e estimem o volume diário de casos de baixa confiança que cairiam sobre um revisor. Pesem o atrito e o custo de pessoal de um portão contra o raio de impacto de um erro sem supervisão e prefiram redesenhar uma ação irreversível numa preparada e desfazível a acrescentar outro revisor. Em contextos corporativos e governamentais, liguem cada ação consequente a um oficial responsável e a um registro de gestão de mudanças, porque uma ação autônoma que afeta um cidadão ou um cliente e que nenhum humano aprovou é exatamente a falha que uma auditoria achará.

5. **Estamos recorrendo a um design multiagente porque a tarefa de fato se decompõe, ou porque parece elegante?** Dividir o trabalho entre agentes especializados é sedutor, mas cada agente extra acrescenta custo de coordenação e mais um lugar onde um pequeno erro se compõe num resultado errado. Para uma grande organização o custo não é só gasto e latência: um sistema multiagente é muito mais difícil de rastrear, avaliar e raciocinar quando falha, então o ônus de governança se multiplica com cada papel que vocês acrescentam. Levem a tarefa e mostrem, concretamente, quais partes rodam de forma independente e em paralelo e depois comparem a taxa de sucesso e o custo medidos de uma versão multiagente contra um agente único no mesmo conjunto de avaliação. Se o agente único vence ou empata, o design elegante é engenharia em excesso. Para implantações reguladas ou públicas, lembrem que cada agente na cadeia é mais um componente que um órgão de supervisão precisa conseguir inspecionar, então estrutura adicional que vocês não conseguem justificar é passivo adicional.

6. **Quais são os orçamentos rígidos de passos, tempo e gasto de um agente, e como um agente em laço seria pego antes de acumular custo ou latência?** Um agente que repete uma ação que falha pode queimar dinheiro e tempo sem aviso, então a autonomia sem limites é um risco financeiro tanto quanto de segurança. Para uma grande equipe que roda muitos agentes, um único laço descontrolado pode disparar uma conta de nuvem ou esgotar um limite de taxa que deixa à míngua todas as outras cargas, o que faz dos tetos por execução uma preocupação operacional compartilhada e não um problema de uma equipe. Levem os orçamentos atuais de passos, tempo e tokens de cada agente, o alerta que dispara quando uma execução os excede e a detecção de laços que falha com segurança em vez de se debater. Pesem orçamentos apertados, que podem cortar uma tarefa legitimamente difícil, contra os frouxos, que deixam o custo fugir. Em contextos corporativos e governamentais em que o gasto precisa ser previsto e justificado, um agente cujo custo é ilimitado é uma linha de despesa que vocês não conseguem defender numa revisão orçamentária ou numa auditoria.

## Perspectiva por setor

**Startup.** Entreguem um agente estreito que toque o seu valor central, num modelo hospedado, com o menor conjunto de ferramentas que faça o trabalho e um teto rígido de passos e de gasto. Resistam à demonstração multiagente: a sua escassa atenção de engenharia é mais bem gasta limitando a autonomia de um único agente e rastreando suas execuções do que coordenando papéis que vocês não conseguem manter. Mantenham toda ação consequente atrás de um único portão de “rascunhar, nunca enviar” para que um erro custe um clique para desfazer e não um incidente.

**Pequena empresa.** Vocês não têm quem rode um arcabouço de avaliação nem uma sandbox, então prefiram agentes embutidos em ferramentas em que já confiam e liguem apenas a autonomia que vocês conseguem supervisionar a olho. Tratem qualquer agente que possa enviar, pagar ou excluir em seu nome como algo a manter desligado até uma pessoa confirmar cada ação, porque uma mensagem automatizada errada a um cliente custa a vocês o relacionamento. Favoreçam fornecedores que mostrem o que o agente fez e deixem vocês desligar a automação.

**Grande empresa.** O problema é governar agentes entre muitas equipes: padrões compartilhados para limitar a autonomia, credenciais de ferramentas de menor privilégio, sandbox, portões com humano no circuito e rastreamento de ponta a ponta para que nenhum grupo reinvente as proteções. Liguem os agentes aos sistemas internos sob os mesmos controles de acesso que um humano teria, condicionem as ações irreversíveis a aprovadores nomeados e à gestão de mudanças e gerenciem o portfólio com métricas de taxa de sucesso, orçamentos por execução e testes adversariais de injeção. Padronizem a camada de rastreamento e de avaliação para que o comportamento de qualquer agente possa ser reconstruído e auditado.

**Governo.** A contratação, a transparência e a responsabilização pública limitam toda escolha. Mantenham os agentes em reunir fatos e redigir e reservem toda decisão que afete um cidadão para um humano responsável, porque a responsabilidade por uma decisão do setor público não pode ser delegada a um modelo. Registrem toda execução para que um órgão de supervisão veja quais fontes foram consultadas e o que foi feito, exijam que os fornecedores divulguem as ferramentas e limitações do agente e provem, por um conjunto adversarial de avaliação, que o agente se recusa a agir além do seu escopo limitado.

## Exemplos

**Startup.** Uma startup de análise de dados de cinco pessoas constrói um agente de triagem de suporte. Ele lê um chamado de entrada, busca na documentação e ou redige uma resposta ou roteia o chamado a um humano, e esse é todo o conjunto de ferramentas. As credenciais são somente de leitura mais uma única ação de “criar rascunho” que nunca envia sem uma pessoa clicar em enviar. Toda execução é rastreada para que os fundadores vejam por que um chamado foi roteado para onde foi, e um conjunto de avaliação noturno de cinquenta chamados reais roda o agente cinco vezes cada um para acompanhar uma taxa de exatidão do roteamento. Quando a demonstração multiagente engenhosa de um concorrente os tenta, ficam no agente único porque a tarefa deles não se decompõe.

**Grande empresa.** Um banco constrói um agente para ajudar a equipe de operações a conciliar pagamentos que falharam. Integra-se aos sistemas internos sob os mesmos controles de acesso que um escriturário humano tem, concedidos por credenciais de serviço de menor privilégio delimitadas apenas à conciliação. O agente pode investigar livremente (ler livros-razão, buscar o histórico de transações), mas qualquer ação que mova dinheiro ou edite um registro é preparada e exige um aprovador humano nomeado, satisfazendo a gestão de mudanças. Os documentos ingeridos são tratados como não confiáveis para embotar a injeção de prompt, as ferramentas rodam em sandbox e toda execução é rastreada de ponta a ponta para auditoria. Um conjunto offline de avaliação condiciona cada mudança de modelo ou de prompt, e orçamentos por execução limitam passos e gasto para que um agente em laço não acumule custo nem latência.

**Governo.** Uma agência de benefícios pilota um agente para ajudar os assistentes sociais a reunir os fatos de um pedido: puxando registros, conferindo as regras de elegibilidade e redigindo um resumo. A agência traça uma linha rígida: o agente reúne e redige, mas um assistente social humano toma e assume toda decisão que afeta um cidadão, porque a responsabilização por decisões do setor público não pode ser delegada a um modelo (capítulo 6.5). Cada execução é totalmente registrada, mostrando quais fontes foram consultadas e o que foi redigido, para que um órgão de supervisão possa auditar qualquer caso. A autonomia é deliberadamente limitada a ler e redigir, as ferramentas são de menor privilégio e em sandbox e um conjunto adversarial de avaliação confirma que o agente se recusa a agir além de reunir fatos.

## Justificativa de negócio: motivações, ROI e TCO

Os agentes entregam retorno automatizando trabalho de vários passos que antes exigia uma pessoa clicando entre sistemas: triagem, conciliação, pesquisa e operações de rotina. O valor aparece como trabalho concluído sem um humano em cada passo, tempos de ciclo mais rápidos e equipe liberada para tarefas pesadas em julgamento. Como os agentes se constroem sobre LLMs e ferramentas existentes, o tempo até um protótipo funcionando é curto, que é exatamente por que as equipes constroem em excesso.

O custo total de propriedade é onde os agentes diferem das simples funcionalidades de LLM. Além do custo de inferência, vocês pagam pelas integrações de ferramentas, pela tubulação de sandbox e de permissões, pelo arcabouço de avaliação, pela pilha de rastreamento e de observabilidade (capítulo 6.6) e pelos revisores humanos que dotam de pessoal os portões de aprovação. Um agente em laço ou mal limitado acrescenta um custo variável que pode disparar sem aviso, então os orçamentos de passos e de gasto fazem parte do design e não uma reflexão tardia. O custo de não adotar são operações mais lentas e trabalho manual que os concorrentes automatizam. O custo de adotar sem cuidado é uma ação autônoma que envia a mensagem errada, vaza dados ou toma uma decisão sem responsável. Defendam o caso junto à liderança combinando uma meta concreta de automação com um plano concreto de guardrails, avaliação e supervisão humana e sendo honestos que os guardrails são a maior parte do custo.

## Antipadrões e armadilhas

- **Agente quando um fluxo de trabalho bastaria.** Assumir todo o risco da autonomia para uma tarefa cujos passos eram conhecíveis.
- **Ferramentas e credenciais amplas demais.** Uma ferramenta “faz tudo” em vez de ferramentas estreitas e de menor privilégio.
- **Cegueira à injeção de prompt.** Alimentar com conteúdo não confiável um agente que detém privilégios reais.
- **Sem portão humano nas ações irreversíveis.** Deixar o modelo enviar, pagar ou excluir sem verificação.
- **Teatro multiagente.** Dividir uma tarefa simples entre agentes, pagando custo de coordenação sem ganho.
- **Avaliação por impressão.** Julgar por como a transcrição se lê em vez de pela taxa de sucesso da tarefa.
- **Laços sem limite.** Sem teto de passos, tempo ou gasto, de modo que um agente empacado queima dinheiro e latência.
- **Execuções sem rastro.** Sem registro do que o agente fez, deixando vocês incapazes de depurar, auditar ou prestar contas.

## Modelo de maturidade

- **Nível 1, Iniciar:** Os agentes são prototipados ad hoc, com amplo acesso a ferramentas e sem limites. O sucesso é julgado por demonstrações, de forma reativa, depois que algo quebra. Não há conjunto de avaliação, nem rastreamento, nem portão humano nas ações consequentes.
- **Nível 2, Desenvolver:** Alguns agentes têm laços limitados e ferramentas de menor privilégio, e existe rastreamento básico, mas a prática varia de equipe para equipe. Um conjunto manual de avaliação pega regressões grosseiras em alguns projetos enquanto outros não têm nenhum. A aprovação humana protege as ações irreversíveis mais óbvias, mas a cobertura é desigual e não documentada.
- **Nível 3, Padronizar:** Padrões compartilhados governam a autonomia, as permissões de ferramentas, a sandbox e os portões com humano no circuito, documentados e impostos em todas as equipes. Toda ação consequente é condicionada ou validada, os agentes são rastreados de ponta a ponta e um conjunto automatizado de avaliação com pontuação de taxa de sucesso roda a cada mudança. A injeção de prompt é tratada como ameaça permanente, com resposta definida.
- **Nível 4, Gerenciar:** O portfólio de agentes é medido e controlado em relação a linhas de base. A taxa de sucesso por tarefa, a taxa de aprovação na defesa contra injeção de prompt, o custo e a contagem de passos por execução, a latência de aprovação humana e os incidentes de laço ou de falha são acompanhados como métricas. Os limiares de reversão e de encerramento são impostos com base nessa evidência e não em reclamações. Os orçamentos por execução de passos, tempo e gasto são monitorados, e uma regressão em qualquer métrica dispara ação antes da escala e não depois de um incidente.
- **Nível 5, Orquestrar:** A autonomia é combinada com o risco da tarefa por política e ajustada continuamente à medida que chegam os resultados. A avaliação contínua, offline e online, liga o comportamento do agente a resultados de negócio, e a organização rotineiramente aposenta, redimensiona ou repermissiona agentes à medida que o quadro de riscos muda. O rastreamento, os orçamentos de custo e as trilhas de auditoria são uniformes no portfólio. As defesas contra injeção e contra o deputado confuso são testadas de forma adversarial. A responsabilização por ações autônomas é clara e auditável.

## Ideias para discussão

1. Quais das suas funcionalidades atuais de LLM viraram agentes em silêncio, e a autonomia de cada uma foi limitada de propósito?
2. Para cada ferramenta de agente, qual é o jeito mais barato de um atacante abusar dela por conteúdo injetado, e o que impede isso?
3. Onde vocês escolheram designs multiagente, e conseguem mostrar que o custo de coordenação se pagou versus um agente único?
4. Quais ações do agente são verdadeiramente irreversíveis, e todas elas poderiam ser redesenhadas para serem reversíveis ou preparadas?
5. Se um agente tomasse uma ação danosa amanhã, vocês conseguiriam reconstruir exatamente o que ele fez e quem era o responsável?

## Principais conclusões

- Um agente é um LLM num laço com ferramentas, memória e um objetivo. O risco mora no laço e nas ferramentas, não no texto.
- Prefiram um fluxo de trabalho fixo quando os passos são conhecidos. Reservem a autonomia para objetivos genuinamente abertos e limitem-na com firmeza.
- O uso de ferramentas é a capacidade central. Deem a cada ferramenta o menor privilégio, um esquema validado e uma sandbox.
- Condicionem as ações consequentes e irreversíveis a um humano com autoridade real e projetem para uma reversão barata.
- Tratem os agentes como adversariais: defendam-se da injeção de prompt e do abuso do deputado confuso (capítulo 4.2).
- Avaliem pela taxa de sucesso da tarefa em muitas execuções e rastreiem toda execução para depuração, controle de custo e auditoria (capítulos 6.5 e 6.6).
- Muitas vezes a resposta certa é não construir um agente de modo algum.

## Referências e leitura complementar

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
