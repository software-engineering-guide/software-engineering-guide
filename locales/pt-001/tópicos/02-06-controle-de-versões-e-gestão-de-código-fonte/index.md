# 2.6 Controle de versões e gestão de código-fonte

## Visão geral e motivação

Pense no [controle de versões](https://en.wikipedia.org/wiki/Version_control) como o sistema de registro da sua base de código. Ele captura cada mudança, incluindo quem a fez, quando e por quê, e permite que muitas pessoas trabalhem no mesmo software sem sobrescrever umas às outras. Para uma grande organização, é muito mais que um backup. É a fundação sobre a qual repousam a colaboração, a [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), a auditoria e a gestão de lançamentos. As escolhas que você faz sobre ramificação, estrutura de repositório e disciplina de commits moldam a rapidez com que a sua equipe consegue se mover e com que segurança.

Para equipes grandes, a gestão de código-fonte é na verdade um problema de coordenação em escala. Quando centenas de engenheiros enviam mudanças para um código compartilhado, precisam de uma estratégia que mantenha as integrações pequenas, mantenha a linha principal pronta para lançamento e mantenha o histórico legível. Uma equipe que integra continuamente flui sem atritos. Uma equipe que deixa os ramos divergirem por semanas avança aos solavancos de uma crise de integração para a seguinte. A estrutura do seu repositório, um repositório grande ou vários, também molda como as equipes compartilham código e se coordenam.

Os contextos corporativos e governamentais acrescentam mais algumas exigências: rastreabilidade, controle de acesso e retenção. Uma mudança pode precisar estar ligada a um item de trabalho aprovado para fins de auditoria. Segredos nunca devem entrar no histórico. O acesso ao repositório deve respeitar as fronteiras de segurança. Aqui, as suas práticas de controle de versões passam a fazer parte da estrutura de controles da organização, e um erro como um segredo vazado ou um histórico não auditável pode ter consequências sérias.

## Princípios fundamentais

- Integre mudanças pequenas com frequência. A divergência longa é a raiz da dor de integração.
- Mantenha a linha principal sempre pronta para lançamento.
- O histórico é documentação. Escreva os commits para o futuro leitor que precisará entender o porquê.
- Nunca faça commit de segredos. Trate qualquer segredo que chegue ao histórico como comprometido.
- Automatize a imposição da higiene (hooks, verificações de CI) em vez de depender só da disciplina.
- Escolha a estrutura do repositório (mono ou poli) pela forma como as equipes realmente compartilham código e se coordenam, não pela moda.
- Ligue as mudanças à sua justificativa (itens de trabalho, tíquetes ou decisões) para fins de rastreabilidade.

## Recomendações

### Prefira o desenvolvimento baseado em tronco com ramos de vida curta

Incline-se para o [desenvolvimento baseado em tronco](https://en.wikipedia.org/wiki/Trunk-based_development): integre com frequência a uma linha principal compartilhada, usando ramos de funcionalidade de vida curta medidos em horas ou dias, não em semanas. Ramos curtos mantêm as integrações pequenas e a integração contínua, e esse hábito está fortemente associado a alto desempenho de entrega. Quando o trabalho ainda não está terminado, não o estacione num ramo de vida longa. Use [sinalizadores de funcionalidade](https://en.wikipedia.org/wiki/Feature_toggle), chaves de tempo de execução que escondem o trabalho inacabado, para poder integrá-lo com segurança. Reserve os ramos de lançamento de vida longa para o suporte genuíno a várias versões, sabendo de antemão o custo de manutenção que eles carregam.

### Escolha um modelo de ramificação que se ajuste à cadência de lançamento

Ajuste o seu [modelo de ramificação](https://en.wikipedia.org/wiki/Branching_(version_control)) à forma como você realmente lança. Se você implanta continuamente, o desenvolvimento baseado em tronco com ramificação mínima serve bem. Se você entrega versões numeradas a clientes, ou apoia várias versões ativas ao mesmo tempo, pode precisar de ramos de lançamento e de retroportagem. Fuja de modelos pesados com muitos ramos de vida longa, a menos que o seu modelo de lançamento realmente os exija, porque multiplicam o custo de integração e de manutenção.

### Decida entre monorrepositório e polirrepositório deliberadamente

Recorra a um [monorrepositório](https://en.wikipedia.org/wiki/Monorepo), um único repositório que abriga muitos projetos, quando as equipes compartilham muito código, precisam de mudanças atômicas entre projetos e querem ferramentas e visibilidade unificadas. Em troca, você aceita a necessidade de ferramentas de build em escala e de controles de acesso. Recorra a polirrepositórios, repositórios separados por projeto ou serviço, quando as equipes e os serviços são genuinamente independentes, querem acesso e ciclos de lançamento isolados e não precisam de mudanças atômicas entre repositórios. Em troca, você aceita o custo de coordenar mudanças que atravessam repositórios. Ambos funcionam em escala. É a escolha errada para o seu padrão de acoplamento que cria atrito constante.

### Imponha a higiene de commits e os commits convencionais

Peça mensagens de commit que expliquem por que uma mudança foi feita, e não apenas o quê. Adote uma convenção como os commits convencionais, para que as mensagens sejam estruturadas e legíveis por máquina, o que permite automatizar registros de mudanças e versionamento. Mantenha os commits atômicos, uma mudança lógica cada, para que o histórico continue bissectável e fácil de reverter. Deixe os hooks e as verificações de CI imporem o formato das mensagens e a higiene básica, em vez de confiar na memória.

### Mantenha binários grandes e código gerado fora do histórico comum

Não faça commit de ativos binários grandes direto no histórico principal, porque eles incham todo clone para sempre. Use, em vez disso, um mecanismo de armazenamento de arquivos grandes ou um repositório de artefatos. Como regra, evite também fazer commit de código gerado: gere-o no build. Quando você genuinamente precisar fazer commit de um artefato gerado, isole-o e marque-o com clareza para que não polua as revisões e os diffs.

### Impeça que segredos entrem no repositório

Ponha varredura automática de segredos nos seus hooks de pré-commit e na CI para que as credenciais sejam bloqueadas antes de chegar. Dê aos engenheiros um sistema adequado de gestão de segredos, para que nunca precisem fixar uma credencial no código. E trate qualquer segredo que chegue ao histórico como comprometido: rotacione-o na hora. Depois que um segredo foi enviado e clonado, removê-lo do histórico é difícil e pouco confiável.

### Estabeleça controle de acesso e rastreabilidade

Configure o acesso ao repositório para respeitar as fronteiras de segurança e o [privilégio mínimo](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Ligue commits ou pull requests a itens de trabalho, para que toda mudança seja rastreável até a sua justificativa, o que ajuda tanto o contexto de engenharia do dia a dia quanto a auditoria. Proteja os seus ramos principais com verificações e revisões obrigatórias, para que nada seja integrado sem passar pelos portões que vocês combinaram.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| Desenvolvimento baseado em tronco | Integração contínua. Integrações pequenas. Alto fluxo | Exige sinalizadores de funcionalidade e disciplina. Menos isolamento |
| Ramos de funcionalidade de vida longa | Forte isolamento do trabalho em andamento | Integrações dolorosas. Integração atrasada. Deriva |
| Monorrepositório | Mudanças atômicas entre projetos. Ferramentas compartilhadas. Visibilidade | Exige ferramentas de build em escala. Controle de acesso grosseiro por padrão |
| Polirrepositório | Lançamentos independentes. Acesso isolado. Ferramentas simples por repositório | Mudanças entre repositórios difíceis. Custo de coordenação de versões |
| Commits convencionais | Registros de mudanças e versionamento automatizados. Histórico consistente | Convenção inicial. Precisa de imposição |

O grande compromisso aqui é frequência de integração versus isolamento. Os ramos de vida longa parecem mais seguros porque o seu trabalho fica à parte, mas é esse mesmo isolamento que causa as integrações caras e as surpresas de integração depois. O desenvolvimento baseado em tronco abre mão dessa sensação de isolamento em troca de uma integração contínua e barata e pede que você traga sinalizadores de funcionalidade e disciplina. A decisão entre mono e polirrepositório troca a facilidade entre projetos pela independência das equipes. Escolha a que corresponde a quão fortemente o seu código é realmente acoplado.

## Perguntas para discutir com sua equipe

1. **Que verificações precisam passar antes que algo seja integrado à sua linha principal protegida, e essa linha principal está de fato sempre pronta para lançamento?** Este capítulo trata uma linha principal pronta para lançamento como princípio central e chama de antipadrão uma linha principal desprotegida, onde código quebrado ou não revisado chega ao ramo de que todos dependem. Numa equipe grande, uma linha principal vermelha bloqueia todos ao mesmo tempo, então o portão que você exige é uma propriedade de segurança compartilhada, não pessoal. Leve as evidências: o que a proteção do seu ramo realmente impõe hoje e com que frequência a linha principal está quebrada neste momento. Decida o conjunto exigido, testes que passam, varreduras de segurança e revisão, e torne a linha principal pronta para lançamento por política e não por esperança. Esse portão é o que permite a muitas pessoas integrar continuamente sem medo.

2. **Adotar commits convencionais vale o custo de convenção para a sua equipe, dado o que isso automatiza?** O capítulo recomenda mensagens de commit estruturadas e legíveis por máquina precisamente porque elas permitem automatizar registros de mudanças e versionamento, e pede commits atômicos para que o histórico continue bissectável e reversível. O compromisso é real: você paga uma convenção inicial e precisa de imposição, em troca de notas de lançamento geradas e de um histórico confiável. Leve o sinal do que vocês fazem à mão hoje, como escrever registros de mudanças manualmente ou caçar qual commit introduziu uma regressão. Se você lança com frequência ou mantém várias versões, a automação costuma se pagar. Se raramente corta lançamentos, uma convenção mais leve pode bastar. Deixe os hooks e a CI imporem o formato para que ele não dependa da memória.

3. **Vocês aceitaram o custo operacional que a estrutura do seu repositório exige, seja as ferramentas de monorrepositório ou a coordenação entre repositórios?** Este capítulo diz que tanto o monorrepositório quanto o polirrepositório funcionam em escala e que a escolha errada para o seu padrão de acoplamento é o que cria atrito constante. Um monorrepositório precisa de ferramentas de build em escala e de controle de acesso mais fino, enquanto os polirrepositórios fazem de qualquer mudança que atravessa repositórios um projeto de coordenação com risco de defasagem de versões. Leve o sinal concreto: com que frequência as suas mudanças cruzam as fronteiras de projeto e se as suas ferramentas de build e de acesso conseguem sustentar a estrutura que vocês têm. Se as mudanças atômicas entre projetos são comuns, invista em ferramentas de monorrepositório. Se as equipes e os serviços são genuinamente independentes, aceite deliberadamente o custo de coordenação entre repositórios. O ponto é ajustar a estrutura a quão fortemente o seu código é realmente acoplado e depois financiar as ferramentas que essa estrutura exige.

4. **Se uma credencial ativa fosse enviada agora a um repositório movimentado, com que rapidez vocês a detectariam, e a rotação é de fato automática em vez de uma esperança?** Este capítulo trata qualquer segredo que chegue ao histórico como comprometido e avisa que removê-lo depois é difícil e pouco confiável, então a prevenção e a rotação rápida são as únicas defesas reais. Para uma equipe grande, a exposição se acumula: um segredo enviado a um repositório compartilhado é clonado em dezenas de máquinas e espelhado em caches de CI em minutos, de modo que uma resposta humana lenta garante uma violação. A consideração concorrente é o atrito: a varredura agressiva no pré-commit e a rotação forçada deixam as pessoas lentas e produzem falsos positivos, então você precisa ajustar os controles em vez de desligá-los. Leve as evidências: se a varredura de segredos roda nos hooks de pré-commit e na CI, o seu tempo médio para detectar e rotacionar um vazamento conhecido e se os engenheiros ao menos têm um sistema de gestão de segredos que remova a tentação de fixar no código. Em contextos corporativos e governamentais, ligue isso ao seu processo de incidentes e às regras de retenção, porque uma credencial vazada num histórico auditável é ao mesmo tempo um evento de segurança e de conformidade, e o regulador perguntará quem sabia e com que rapidez agiu.

5. **Os seus ramos são genuinamente de vida curta e, onde não são, por que o trabalho inacabado é estacionado num ramo em vez de escondido atrás de um sinalizador de funcionalidade?** O capítulo se inclina com força para o desenvolvimento baseado em tronco porque a divergência longa é a raiz da dor de integração e oferece os sinalizadores de funcionalidade como o mecanismo que permite integrar com segurança o trabalho incompleto em vez de isolá-lo por semanas. Numa equipe grande, isso é uma propriedade de coordenação, não uma preferência pessoal: todo ramo que vive por semanas vira uma bifurcação privada da realidade que alguém precisará reconciliar, e o custo dessa reconciliação cresce com o número de pessoas. A consideração concorrente é que os sinalizadores de funcionalidade carregam o próprio custo, incluindo complexidade em tempo de execução, teste de combinações e sinalizadores obsoletos que precisam ser aposentados. Leve os dados: a distribuição real das vidas dos seus ramos, com que frequência a integração produz conflitos ou surpresas e quantos ramos de vida longa existem agora e por quê. Para uma organização grande ou regulamentada, acrescente o quadro de lançamentos, já que o suporte genuíno a várias versões pode justificar ramos de lançamento de vida longa com retroportagem disciplinada, e essa é uma decisão diferente de estacionar o trabalho cotidiano de funcionalidades fora da linha principal.

6. **Toda mudança no seu histórico pode ser rastreada até seu autor e sua justificativa dentro das fronteiras de segurança certas, e isso resistiria a uma auditoria?** Este capítulo trata o controle de acesso, o privilégio mínimo e a ligação das mudanças a itens de trabalho como parte da estrutura de controles da organização, não como um polimento opcional. Para uma equipe grande, a rastreabilidade é o que transforma um fluxo opaco de commits em algo sobre o qual você consegue raciocinar durante um incidente ou uma revisão de conformidade, e as fronteiras de acesso são o que impede que uma única conta comprometida alcance código que nunca deveria tocar. A consideração concorrente é a velocidade dos desenvolvedores: vínculos obrigatórios com itens de trabalho, permissões detalhadas e revisões exigidas acrescentam cerimônia que uma equipe pequena e ágil poderia razoavelmente dispensar. Leve as evidências: se os ramos protegidos exigem as verificações e revisões que vocês afirmam, se os commits de fato referenciam itens de trabalho aprovados e como o acesso se mapeia hoje para as suas fronteiras de segurança reais. Em contextos corporativos e governamentais, ligue isso a obrigações de classificação, de retenção e de auditoria, porque um histórico não auditável ou uma concessão de acesso ampla demais vira uma constatação que pode parar um programa ou reprovar uma acreditação.

## Perspectiva por setor

**Startup.** Velocidade e sobrevivência vencem. Use um repositório, trabalhe baseado em tronco, integre ramos de vida curta várias vezes ao dia e esconda o trabalho inacabado atrás de sinalizadores de funcionalidade simples em vez de ramos longos. Ligue a varredura de segredos desde o primeiríssimo commit, porque uma chave vazada num repositório público pode afundar uma empresa sem equipe de segurança para conter o dano. Pule modelos elaborados de ramificação e processo pesado. Um ramo principal protegido e mensagens de commit significativas são disciplina suficiente para se mover rápido.

**Pequena empresa.** Sem especialista dedicado em plataforma ou DevOps e com orçamento apertado, compre os padrões gerenciados em vez de construí-los. Um provedor de Git hospedado oferece proteção de ramos, revisões obrigatórias e varredura de segredos prontas, então apoie-se nelas em vez de hospedar por conta própria um servidor que você não consegue manter. Enquadre a decisão como higiene de dados: saiba quais repositórios guardam configuração sensível, mantenha as credenciais no gestor de segredos do provedor e deixe a plataforma impor as poucas regras de que você realmente precisa.

**Grande empresa.** O problema difícil é a consistência entre muitas equipes. Padronize a proteção de ramos, as convenções de commit e a varredura de segredos como política da organização inteira, para que os grupos parem de reinventá-las, e faça a escolha entre mono e polirrepositório deliberadamente por padrão de acoplamento, financiando as ferramentas de build em escala ou a coordenação entre repositórios que ela exige. Encaminhe as mudanças aos revisores certos com regras de propriedade de código, ligue os commits a itens de trabalho para rastreabilidade e trate a higiene do controle de versões como um controle governado, com responsáveis e métricas, e não como uma questão de hábito individual.

**Governo.** Regras de contratação, transparência e responsabilização pública moldam toda a configuração. Exija que todo commit referencie um item de trabalho aprovado, controle o acesso por fronteira de classificação e torne obrigatórias a varredura de segredos e a rotação imediata sob um processo de incidentes documentado. Apoie várias versões implantadas com ramos de lançamento de vida longa e retroportagem disciplinada onde os locais não conseguem atualizar todos ao mesmo tempo, e mantenha o histórico auditável e retido para que pedidos de acreditação, de acesso à informação e de supervisão possam ser respondidos sem correria.

## Exemplos

**Startup.** Uma startup de três pessoas trabalha baseada em tronco por hábito e por necessidade, integrando ramos de vida curta à principal várias vezes ao dia e escondendo funcionalidades pela metade atrás de sinalizadores simples. Ela liga a varredura de segredos na CI desde o primeiro commit, porque uma chave de API vazada num repositório público poderia afundar uma empresa sem equipe de segurança para conter as consequências. Um repositório, um ramo principal protegido e mensagens de commit significativas dão disciplina suficiente para se mover rápido sem tropeçar no próprio histórico.

**Grande empresa.** Uma grande empresa de tecnologia mantém um monorrepositório com centenas de serviços e bibliotecas compartilhadas. Ferramentas de build em escala e regras de propriedade de código encaminham cada mudança aos revisores certos. Um único commit pode atualizar de forma atômica uma biblioteca compartilhada e todos os consumidores de uma vez, contornando os problemas de defasagem de versões que afligem repositórios distribuídos. O desenvolvimento baseado em tronco com sinalizadores de funcionalidade mantém a linha principal pronta para lançamento, e a varredura de segredos bloqueia credenciais no momento do commit em todo o repositório.

**Governo.** Uma contratada nacional de defesa segue uma rastreabilidade estrita. Todo commit precisa referenciar um item de trabalho aprovado. A proteção de ramos exige varreduras de segurança aprovadas e revisão independente, e o acesso é rigorosamente controlado por fronteira de classificação. A varredura de segredos é obrigatória, e qualquer credencial exposta dispara rotação imediata sob um processo de incidentes. Ramos de lançamento de vida longa apoiam várias versões implantadas em locais que não podem atualizar todos ao mesmo tempo, com retroportagem disciplinada de correções de segurança.

## Justificativa de negócio: motivações, ROI e TCO

Uma boa gestão de código-fonte é quase gratuita de adotar e cara de dispensar. O desenvolvimento baseado em tronco e a integração contínua estão entre as práticas mais fortemente associadas a alto desempenho de entrega de software, que por sua vez se correlaciona com melhores resultados organizacionais. Um histórico limpo e rastreável reduz o tempo para diagnosticar incidentes e satisfazer auditorias, e uma ramificação disciplinada poupa o custo recorrente e não orçado de crises de integração e maratonas de integração.

O maior risco desproporcional são os segredos no controle de versões. Uma única credencial vazada pode causar uma violação cujo custo faz sombra a qualquer investimento em ferramentas, e o histórico faz esses vazamentos durarem. Preveni-los é barato. Limpar depois não é. As más escolhas de estrutura aparecem como atrito crônico: toda mudança entre repositórios vira um projeto de coordenação, ou todo build de monorrepositório vira um gargalo. Para defender o caso junto à liderança, ligue a sua estratégia de ramificação às métricas de entrega e ao tempo de diagnóstico de incidentes e apresente a varredura de segredos e o controle de acesso como controles de baixo custo contra o risco de alto custo de violações e de auditoria.

## Antipadrões e armadilhas

- **Ramos divergentes de vida longa:** semanas de trabalho isolado que se integram em eventos de integração dolorosos e arriscados.
- **Segredos no histórico:** credenciais fixadas no código que persistem nos clones para sempre e exigem rotação depois de expostas.
- **Fazer commit de binários grandes no histórico principal:** incha permanentemente todo clone e deixa todas as operações lentas.
- **Mensagens de commit sem sentido:** “fix”, “wip”, “changes” que destroem o valor do histórico como documentação.
- **Fazer commit de código gerado como se fosse escrito à mão:** diffs ruidosos, conflitos de integração e confusão sobre a fonte da verdade.
- **Estrutura de repositório errada para o acoplamento:** polirrepositórios para código fortemente acoplado, ou monorrepositórios sem ferramentas em escala.
- **Linha principal desprotegida:** sem verificações exigidas, de modo que código quebrado ou não revisado chega ao ramo de que todos dependem.

## Modelo de maturidade

- **Nível 1, Iniciar:** Ad hoc e reativo. A ramificação é improvisada, os ramos vivem por semanas, as mensagens de commit dizem “fix” ou “wip”, não há varredura de segredos e a integração avança aos solavancos de uma crise de integração para a seguinte.
- **Nível 2, Desenvolver:** Aparecem práticas básicas, mas variam por equipe. Um modelo de ramificação e convenções de mensagem existem em alguns lugares, mas os ramos ainda vivem tempo demais, a imposição é parcial, a varredura de segredos é irregular e a estrutura do repositório foi herdada e não escolhida.
- **Nível 3, Padronizar:** As práticas são documentadas e impostas em toda a organização: desenvolvimento baseado em tronco com ramos curtos, uma linha principal protegida e sempre pronta para lançamento, convenções de commit impostas, varredura de segredos tanto nos hooks quanto na CI, acesso de privilégio mínimo e uma escolha deliberada entre mono e polirrepositório.
- **Nível 4, Gerenciar:** As práticas de código-fonte são medidas e controladas com dados. Você acompanha a vida dos ramos, a frequência de integração, a taxa de quebra da linha principal, o tempo médio para detectar e rotacionar um segredo vazado e a rastreabilidade de mudança para item de trabalho em relação a linhas de base acordadas, e age quando os números derivam em vez de esperar o próximo incidente.
- **Nível 5, Orquestrar:** As práticas são continuamente melhoradas e integradas em toda a organização. A ramificação, a estrutura de repositório e as ferramentas se adaptam conforme as equipes e o acoplamento do código mudam, a automação impõe a higiene de ponta a ponta e os dados do controle de versões alimentam as decisões de entrega, de segurança e de risco em toda a organização.

## Ideias para discussão

- A vida dos ramos da sua equipe é de fato curta e, se não, o que impede a integração contínua?
- A sua escolha entre monorrepositório e polirrepositório corresponde a quão acoplado o seu código realmente é?
- Como vocês tratam hoje os binários grandes e os artefatos gerados, e quanto isso custa?
- O que aconteceria se uma credencial ativa fosse enviada agora, e com que rapidez vocês a detectariam e rotacionariam?
- Quanta disciplina de mensagens de commit e de rastreabilidade vale a pena impor no seu contexto?
- Como os sinalizadores de funcionalidade mudam a sua estratégia de ramificação, e que novos riscos eles introduzem?

## Principais conclusões

- Integre com frequência com ramos de vida curta. A divergência longa causa a dor que parece evitar.
- Mantenha a linha principal pronta para lançamento e protegida por verificações exigidas.
- Nunca deixe segredos entrarem no histórico. Varra automaticamente e rotacione na hora se entrarem.
- Escolha monorrepositório ou polirrepositório pelas suas reais necessidades de acoplamento e coordenação.
- Trate o histórico de commits como documentação, com commits significativos, convencionais e atômicos.

## Referências e leitura complementar

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
