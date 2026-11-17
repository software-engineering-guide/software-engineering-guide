# 8.1 CI/CD e entrega

## Visão geral e motivação

A [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) e a [entrega contínua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) são o tecido conectivo entre escrever código e pô-lo diante dos usuários com segurança. A integração contínua significa que toda mudança é mesclada com frequência numa linha principal compartilhada e depois construída e testada automaticamente, para que os problemas de integração apareçam em minutos e não no fim de um longo ciclo de lançamento. A entrega contínua significa que toda mudança que passa pelo pipeline é mantida num estado implantável, de modo que liberar para produção vira uma decisão de negócio e não uma correria de engenharia. A [implantação contínua](https://en.wikipedia.org/wiki/Continuous_deployment) dá mais um passo e libera automaticamente toda mudança aprovada, sem portão humano.

Para grandes equipes, essas distinções importam enormemente. Quando centenas de engenheiros fazem commits em sistemas que se sobrepõem, o custo da integração manual e do teste manual cresce de forma não linear. Um pipeline automatizado e compartilhado é o único modo prático de dar a muitos colaboradores um retorno rápido e confiável e de impedir que a mudança de uma equipe quebre em silêncio a de outra. O pipeline vira a fonte única da verdade sobre se o software está saudável e impõe uma consistência que nenhuma quantidade de documentação ou de boas intenções consegue garantir em escala.

Os contextos corporativo e governamental acrescentam mais uma dimensão: auditabilidade e controle de mudanças. Reguladores, responsáveis de segurança e auditores precisam de evidência de que as mudanças foram revisadas, testadas e aprovadas e de que o artefato em produção é exatamente o que foi construído e verificado. Um pipeline de CI/CD bem projetado transforma essas obrigações de conformidade de um fardo burocrático em subproduto automático do fluxo normal de engenharia. Bem feita, a entrega fica ao mesmo tempo mais rápida e mais segura, que é o resultado que mais importa para a liderança.

*Veja também:* capítulo 8.4 (engenharia de plataforma e experiência do desenvolvedor), capítulo 8.5 (automação de testes e de processos) e capítulo 7.4 (análises de produto e experimentação) para as práticas de [feature flag](https://en.wikipedia.org/wiki/Feature_toggle) (chaves em tempo de execução que expõem funcionalidades aos usuários sem reimplantar) e de experimentação que a entrega progressiva (lançar uma mudança gradualmente enquanto monitora automaticamente suas métricas de saúde) viabiliza.

## Princípios fundamentais

- Integrem mudanças pequenas com frequência. Branches de vida longa são o inimigo da integração contínua.
- Construam o artefato uma só vez e promovam o artefato idêntico por todos os ambientes.
- Façam do pipeline o portão autoritativo: se está verde, a mudança pode ser entregue; se está vermelho, o trabalho para até ser consertado.
- Otimizem sem trégua para um retorno rápido, para que os desenvolvedores permaneçam em fluxo e os defeitos sejam pegos com o contexto fresco.
- Automatizem tudo que se repete, incluindo testes, varreduras de segurança, provisionamento e implantação.
- Tratem as definições de pipeline como código versionado sujeito a revisão, não como configuração clicável em console.
- Projetem para lançamentos seguros e reversíveis, de modo que qualquer implantação possa ser desfeita depressa.
- Separem a implantação (instalar o código) do lançamento (expô-lo aos usuários) usando feature flags.

## Recomendações

### Projete o pipeline como uma série de portões de qualidade

Estruturem o pipeline em estágios que avançam do barato e rápido ao caro e minucioso: compilação e testes de unidade primeiro, depois testes de integração, varreduras de segurança e de licenças e por fim a implantação em staging e produção. Cada estágio é um portão que uma mudança precisa cruzar. Ordenem os portões de modo que as verificações mais rápidas e mais propensas a falhar rodem primeiro, o que dá aos desenvolvedores retorno no menor tempo possível. Mantenham o ciclo de retorno do estágio de commit abaixo de dez minutos sempre que puderem. Além disso, os desenvolvedores trocam de contexto e a produtividade cai.

### Construa uma vez, promova em toda parte

Produzam um único artefato imutável no estágio de build e promovam esse exato artefato por teste, staging e produção. Nunca reconstruam por ambiente, porque uma reconstrução pode introduzir diferenças em silêncio. A configuração que varia por ambiente deve ser injetada na hora da implantação, não assada em builds separados. Essa prática é também o que permite dizer a um auditor, com certeza, que o binário em produção é o que passou por todos os portões.

### Faça do pipeline o ponto de imposição da política

Codifiquem as verificações exigidas (aprovação de revisão de código, limiares de cobertura de testes, resultados de varredura de segurança, commits assinados) diretamente no pipeline e nas regras de proteção de branch. A política manual que vive numa wiki é rotineiramente contornada sob pressão de prazo. A política codificada no pipeline é aplicada de modo uniforme e automático a toda mudança.

### Mantenha a linha principal sempre liberável

Usem o desenvolvimento baseado em trunk (trunk-based development), que integra todo o trabalho num único branch compartilhado com poucos ou nenhum branch de vida longa, ou usem branches de funcionalidade de vida curta, e apoiem-se em feature flags para esconder o trabalho incompleto em vez de branches de vida longa. Isso mantém pequenos os conflitos de merge e mantém a linha principal sempre num estado implantável, que é a precondição para uma entrega contínua genuína.

### Escolha estratégias de implantação deliberadamente

Ajustem a estratégia de implantação ao risco e ao raio de impacto do serviço:

- As implantações **graduais (rolling)** substituem as instâncias aos poucos e são um padrão sensato para serviços sem estado.
- O **[blue-green](https://en.wikipedia.org/wiki/Blue-green_deployment)** mantém dois ambientes idênticos e troca o tráfego de uma só vez, dando um caminho de reversão instantâneo.
- Os lançamentos **canário** encaminham uma pequena porcentagem do tráfego para a nova versão, observam as métricas de saúde e só ampliam se os sinais forem bons.
- As **feature flags** desacoplam o lançamento da implantação, permitindo habilitar funcionalidades para usuários ou coortes específicos sem reimplantar.

### Adote a entrega progressiva com reversão automatizada

A entrega progressiva combina lançamentos canário com análise automatizada de métricas como taxa de erro, latência e saturação. Definam critérios objetivos de saúde de antemão e deixem o sistema promover ou reverter automaticamente com base nesses sinais. A reversão automatizada remove a hesitação humana que transforma um pequeno incidente num grande.

### Ofereça gestão de lançamentos e controle de mudanças para ambientes regulados

Em contextos regulados, mantenham um registro leve mas real de gestão de mudanças. Capturem automaticamente quem aprovou cada mudança, que testes rodaram e que artefato foi implantado. Usem processos de comitê consultivo de mudanças para mudanças genuinamente de alto risco, mas reservem-nos para esses casos. Encaminhar toda mudança rotineira a um conselho semanal destrói o valor da automação. Em vez disso, mirem tipos de mudança padrão e pré-aprovados, que fluem pelo pipeline sem cerimônia.

## Compromissos: prós e contras

| Abordagem | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| Entrega contínua (portão manual de lançamento) | O negócio controla o momento. Forte para janelas regulatórias de lançamento | Exige disciplina para manter a linha principal entregável | Empresas com janelas de mudança |
| Implantação contínua (totalmente automática) | Retorno mais rápido. Menores lotes | Exige testes e observabilidade maduros | Equipes de alta confiança e alta frequência |
| Blue-green | Reversão instantânea. Modelo mental simples | Dobra o custo do ambiente durante a troca | Serviços críticos que precisam de reversão rápida |
| Canário + entrega progressiva | Limita o raio de impacto. Guiada por dados | Complexa de construir. Precisa de boas métricas | Sistemas de grande escala voltados ao usuário |
| Feature flags | Desacoplam a implantação do lançamento | Dívida de flags se não forem limpas | Equipes que entregam trabalho incompleto com segurança |

O compromisso central é velocidade versus controle, mas muitas vezes isso é uma falsa escolha. A automação madura entrega os dois: os lançamentos são mais rápidos porque são menores e mais seguros porque cada um é verificado e reversível. O custo real é o investimento inicial em cobertura de testes, observabilidade e engenharia de pipeline, mais a disciplina contínua para mantê-los saudáveis. As organizações que poupam nesse investimento obtêm a velocidade sem a segurança, o que é pior que um processo manual lento.

## Perguntas para discutir com sua equipe

1. **Qual é a sua meta de tempo de retorno do estágio de commit, e o que é cortado quando a suíte supera os dez minutos?** Um estágio de commit lento mata em silêncio a integração contínua, porque os desenvolvedores param de esperar o verde e começam a agrupar mudanças. Decidam o número agora (este capítulo defende menos de dez minutos) e decidam o mecanismo para mantê-lo: workers paralelos, uma pirâmide de testes rigorosa e mover as verificações lentas de integração para um estágio posterior. Em escala corporativa essa é uma decisão de plataforma, já que centenas de engenheiros compartilham o mesmo pipeline e cada minuto acrescentado se multiplica por todo commit. Levem dados reais à reunião: a duração atual do pipeline em p50 e p95, os dez testes mais lentos e com que frequência as pessoas reexecutam em vez de esperar. Se vocês não conseguem declarar a meta e defendê-la com números, o seu pipeline está derivando para um processo em lote fantasiado de CI.

2. **Que estratégia de implantação cada serviço usa, e quem responde por essa escolha?** Rolling, blue-green e canário não são intercambiáveis: trocam custo, velocidade de reversão e complexidade de modos diferentes, e a escolha certa depende do raio de impacto do serviço. O blue-green compra reversão instantânea ao preço de um ambiente dobrado durante a troca, o que vale a pena para um sistema de pagamentos e é desperdício para um painel interno. O canário limita a exposição mas exige boas métricas de saúde e mais engenharia de pipeline. Para um patrimônio grande ou regulado, deixar isso ao hábito de cada equipe produz inconsistência que aparece durante um incidente, então combinem padrões por nível de serviço e registrem a decisão. Levem o catálogo de serviços e marquem cada serviço com sua estratégia, seu caminho de reversão e a pessoa que é dona dessa decisão.

3. **Como vocês provam que o artefato em produção é exatamente o que passou por todos os portões?** Construir uma vez e promover o artefato idêntico é todo o jogo da auditabilidade, e ele se quebra no momento em que alguém reconstrói por ambiente ou remenda uma máquina em execução. Em contextos corporativos e governamentais, um auditor pedirá que vocês rastreiem um binário em execução até o seu commit, a sua revisão e as suas aprovações, e vocês querem que essa resposta leve segundos, não uma semana. Decidam como a impõem: artefatos imutáveis, imagens assinadas, verificação de assinatura na implantação e configuração injetada na implantação em vez de assada em builds separados. Levem as lacunas atuais à mesa, como qualquer estágio que reconstrói, qualquer caminho manual de correção urgente e qualquer lugar onde a configuração bifurca o artefato. A resposta determina se a sua evidência de conformidade é um subproduto do pipeline ou uma correria manual antes de cada auditoria.

4. **Quando a linha principal fica vermelha, o que de fato para, e como vocês tratam os testes instáveis (flaky)?** Um pipeline só é um portão autoritativo se um build vermelho genuinamente interrompe o trabalho, mas muitas organizações toleram em silêncio uma linha principal quebrada e um acúmulo de falhas intermitentes, o que treina os desenvolvedores a reexecutar até ficar verde e a entregar em cima de falhas. Para uma grande equipe essa podridão se compõe, porque o teste instável ignorado de uma equipe vira a desculpa de todos para contornar o portão, e a confiança no pipeline é muito mais barata de manter que de reconstruir. Pesem as atrações concorrentes: uma regra rigorosa de parar a linha protege a qualidade mas pode bloquear centenas de engenheiros por um único commit ruim, enquanto uma política leniente preserva a vazão e corrói o portão. Levem evidências à discussão: o tempo atual de vermelho da linha principal, o número de testes em quarentena ou instáveis, a taxa de reexecução e com que frequência as mudanças são mescladas sobre uma verificação que falha. Em contextos corporativos e governamentais, nomeiem quem é dono da triagem de testes instáveis e quem tem autoridade para congelar merges, porque um portão pelo qual ninguém responde é um portão que os auditores descobrirão ter sido rotineiramente sobrescrito.

5. **Qual é o seu ciclo de vida das feature flags, e quem é responsável por aposentá-las?** As flags permitem separar a implantação do lançamento e esconder trabalho incompleto, mas toda flag é um ramo no seu código que nunca se limpa sozinho, e as flags não gerenciadas se acumulam em complexidade condicional em que ninguém ousa mexer. Num patrimônio grande essa dívida é perigosa, porque uma flag obsoleta pode condicionar em silêncio uma correção de segurança ou virar caminhos de código não testados para produção, e quem a criou muitas vezes já foi embora. Equilibrem a tensão: as flags compraram uma entrega incremental e segura, então o objetivo não é menos flags e sim um ciclo de vida disciplinado, com um dono, uma expectativa de expiração e ferramentas que revelem as obsoletas. Levem o inventário atual à reunião: quantas flags estão ativas, quão velha é a mais antiga, quais não têm dono e se alguma flag de vida longa agora funciona como configuração permanente que pertence a outro lugar. Para ambientes regulados, acrescentem quem pode mudar uma flag em produção e se essa mudança é registrada com o mesmo rigor de uma implantação, já que virar uma flag é um lançamento mesmo que o pipeline nunca rode.

6. **Onde fica a fronteira entre a entrega contínua com portão humano e a implantação contínua plena, e quem define os limiares de reversão?** A entrega contínua mantém uma pessoa no controle do momento do lançamento, o que serve a janelas estatutárias de mudança e a sistemas de alto raio de impacto, enquanto a implantação contínua entrega automaticamente toda mudança aprovada e exige testes, observabilidade e reversão automatizada maduros para ser segura. Para uma organização grande ou regulada a resposta raramente é uniforme: o site de marketing pode implantar continuamente enquanto o núcleo de pagamentos mantém um portão humano documentado, e traçar essa linha por nível de serviço previne tanto o atrito desnecessário quanto a automação imprudente. As considerações concorrentes são velocidade e tamanho de lote contra controle e auditabilidade, mais o custo de engenharia das métricas de saúde de que a reversão automatizada precisa. Levem as evidências: a taxa de falha de mudanças por serviço, o tempo médio de recuperação, a cadência atual de lançamentos e os sinais objetivos (taxa de erro, latência, saturação) em que vocês confiariam para promover ou reverter sem um humano. Em contextos governamentais e corporativos, liguem cada nível a quem é dono dos limiares de reversão e a quem aprova qualquer passagem de um lançamento com portão para a automação plena, para que a decisão seja deliberada e não derive.

## Perspectiva por setor

**Startup.** Apoiem-se em CI/CD gerenciado desde o primeiro dia: um runner hospedado, um pipeline, uma imagem imutável e implantação automática em staging a cada merge. Não construam infraestrutura de pipeline que depois terão de manter. As feature flags permitem a duas ou três pessoas mesclar trabalho pela metade com segurança e entregar várias vezes ao dia, e uma implantação em produção com um clique mais um desligamento rápido de flag é todo o controle de mudanças de que vocês precisam até a escala forçar mais.

**Pequena empresa.** Sem engenheiro dedicado de plataforma ou de lançamentos, favoreçam o pipeline que o seu host de código oferece (Actions embutidas ou equivalente) e sua estratégia de implantação padrão a qualquer coisa sob medida. Enquadrem com honestidade a escolha entre comprar e construir: um pipeline gerenciado e uma plataforma de hospedagem com reversão embutida custam menos que as horas de engenheiro que uma montagem sob medida consome. Mantenham o essencial, que é construir uma vez, promover o mesmo artefato e uma reversão fácil, e pulem a maquinaria de entrega progressiva até o volume justificá-la.

**Grande empresa.** O problema central é a consistência entre muitas equipes: padronizem um modelo de pipeline compartilhado que imponha revisão, varreduras, artefatos imutáveis e assinados e estratégias de implantação por nível de serviço, para que a qualidade não varie de equipe para equipe. Tratem as definições de pipeline como código revisado, capturem a evidência de controle de mudanças automaticamente e gerenciem as feature flags e os limiares de reversão como ativos governados e não como hábito privado de cada equipe. O ganho é uma entrega mais rápida e evidência de auditoria produzida como subproduto em vez de uma correria trimestral.

**Governo.** As regras de contratação, as janelas estatutárias de mudança e a prestação de contas públicas moldam o pipeline. Prefiram a entrega contínua com um portão humano documentado de lançamento à automação plena para os sistemas consequentes, classifiquem o trabalho rotineiro como mudanças padrão pré-aprovadas e mantenham um caminho instantâneo de reversão (blue-green ou canário automatizado) para os serviços de que os cidadãos dependem em janelas anuais estreitas. Garantam que o pipeline registre quem aprovou cada mudança, que testes rodaram e que artefato foi implantado, para que as obrigações de transparência e de auditoria sejam cumpridas pelo fluxo normal e não por papelada manual.

## Exemplos

**Startup.** Uma startup de SaaS de quatro pessoas monta um único pipeline do GitHub Actions que roda os testes de unidade, constrói uma imagem Docker e implanta essa mesma imagem em staging automaticamente a cada merge na main. Uma implantação em produção é um clique, e os fundadores se apoiam em feature flags para poder mesclar trabalho pela metade atrás de uma flag em vez de manter um branch vivo por semanas. Quando um lançamento ruim escapa, viram a flag para desligada em segundos e consertam com calma, o que mantém a equipe minúscula entregando várias vezes ao dia sem uma pessoa de operações dedicada.

**Grande empresa.** Um banco global consolida dezenas de jobs do Jenkins específicos de cada equipe num modelo de pipeline padronizado que toda equipe de produto herda. O modelo impõe análise estática, varredura de dependências e um artefato assinado e imutável e implanta por canário com reversão automatizada atrelada a limiares de taxa de erro e de latência. Como o mesmo artefato é promovido do teste à produção e cada portão é registrado, os auditores do banco conseguem rastrear qualquer binário de produção até o seu commit, a sua revisão e a sua aprovação em segundos, substituindo um exercício trimestral manual de coleta de evidências.

**Governo.** Uma autoridade tributária nacional que moderniza um sistema de declaração adota a entrega contínua com um portão humano explícito de lançamento, para respeitar as janelas estatutárias de mudança durante a temporada de declarações. As mudanças rotineiras são classificadas como mudanças padrão pré-aprovadas que fluem automaticamente para staging. O lançamento em produção exige uma única aprovação documentada que o pipeline registra. A implantação blue-green dá à autoridade um caminho instantâneo de reversão se um defeito chegar à produção, o que é crítico quando milhões de cidadãos dependem do serviço numa estreita janela anual.

## Justificativa de negócio: motivações, ROI e TCO

O retorno do investimento em CI/CD aparece como menor prazo de entrega das mudanças, menor taxa de falha de mudanças e recuperação mais rápida quando ocorrem incidentes: as métricas que a pesquisa consistentemente liga tanto ao desempenho de entrega quanto aos resultados organizacionais. Lançamentos mais rápidos e menores cortam a sobrecarga de coordenação que consome a capacidade de engenharia em escala, e a verificação automatizada corta o trabalho caro e desmoralizante de apagar incêndios de defeitos de produção.

O custo total de propriedade pesa o custo de adoção contra o custo de não adotar. Os custos de adoção incluem construir e manter pipelines, ampliar a cobertura de testes e investir em observabilidade e em equipe de plataforma. O custo de não adotar é maior mas menos visível: lançamentos manuais lentos, dor de integração, incidentes de produção que danificam a reputação e, em contextos regulados, auditorias malsucedidas e remediação. Para a liderança, o argumento é mais bem enquadrado em termos de redução de risco e de capacidade. A automação converte o escasso tempo de engenheiros seniores de trabalho repetitivo de lançamento em trabalho de produto, ao mesmo tempo que torna as interrupções mais raras e mais curtas.

## Antipadrões e armadilhas

- **Pipelines floco de neve.** Cada equipe monta à mão um pipeline único, de modo que melhorias e correções não podem ser compartilhadas e a qualidade varia muito.
- **Reconstruir por ambiente.** Reconstruir a cada estágio quebra a garantia de “construir uma vez” e deixa diferenças sutis chegarem à produção.
- **Builds vermelhos ignorados.** Tolerar uma linha principal persistentemente quebrada destrói a confiança no pipeline e normaliza entregar em cima de falhas.
- **Testes instáveis não tratados.** As falhas intermitentes treinam os desenvolvedores a reexecutar até ficar verde, derrotando o propósito do portão.
- **Teatro de aprovação manual.** Um comitê consultivo de mudanças que carimba tudo acrescenta atraso sem acrescentar segurança.
- **Dívida de flags.** As feature flags que nunca são removidas se acumulam em complexidade condicional impossível de manter.
- **Implantação igual a lançamento.** Acoplar as duas coisas significa que toda mudança voltada ao usuário exige uma reimplantação arriscada.

## Modelo de maturidade

**Nível 1: Iniciar.** Builds e implantações são em grande parte manuais, ad hoc e reativos. A integração acontece tarde, os lançamentos são raros e estressantes, reverter significa reimplantar uma versão antiga à mão e não há noção compartilhada de um portão de pipeline.

**Nível 2: Desenvolver.** Builds automatizados e testes de unidade rodam a cada commit, mas as práticas variam de equipe para equipe. As implantações são roteirizadas mas ainda disparadas e supervisionadas manualmente, alguns ambientes são consistentes e os artefatos ainda podem ser reconstruídos a cada estágio. Onde existe um pipeline, ele costuma ser um floco de neve que não pode ser compartilhado.

**Nível 3: Padronizar.** Um modelo de pipeline documentado e padronizado é imposto entre as equipes. Ele promove um único artefato imutável por todos os ambientes, aplica portões automatizados de qualidade e de segurança, codifica verificações exigidas como a aprovação de revisão e os resultados de varredura e captura registros de mudança automaticamente. Estratégias de implantação como canário ou blue-green são escolhidas deliberadamente por nível de serviço.

**Nível 4: Gerenciar.** A entrega é medida e controlada em relação a linhas de base. A organização acompanha o prazo de entrega das mudanças, a frequência de implantação, a taxa de falha de mudanças e o tempo médio de recuperação, junto com a duração do pipeline em p50 e p95, as taxas de testes instáveis e de reexecução e a idade das feature flags. Os limiares de reversão são definidos a partir de dados observados de taxa de erro, latência e saturação, os portões são impostos com base em evidências e não em hábito, e cada métrica tem um dono que age quando ela se afasta da meta.

**Nível 5: Orquestrar.** A entrega melhora continuamente e é integrada em toda a organização. A entrega progressiva com reversão automatizada guiada por métricas é a norma, o lançamento é desacoplado da implantação por flags bem governadas e a evidência de conformidade é produzida automaticamente como subproduto. O pipeline se adapta conforme o patrimônio muda, e as métricas de entrega alimentam o planejamento de negócio e de risco para que o investimento flua para as melhorias de maior alavancagem.

## Ideias para discussão

- Onde fica a fronteira certa entre a entrega contínua com portão humano e a implantação contínua plena para os seus sistemas mais críticos?
- Como vocês mantêm significativo um processo obrigatório de gestão de mudanças sem transformá-lo em teatro de carimbo?
- Que métricas objetivas de saúde devem governar a reversão automatizada, e quem é dono dos seus limiares?
- Como as equipes de plataforma devem equilibrar modelos padronizados de pipeline contra as necessidades legítimas de equipes com requisitos incomuns?
- Qual é a sua política e as suas ferramentas para aposentar feature flags antes que virem dívida?
- Como vocês medem se uma entrega mais rápida de fato melhora os resultados de negócio e não apenas entrega mais coisas?

## Principais conclusões

- CI, CD e implantação contínua são coisas distintas. Escolham o nível de automação que combina com a sua tolerância a risco e maturidade.
- Construam o artefato uma só vez e promovam o artefato idêntico por todos os ambientes.
- Projetem o pipeline como portões de qualidade ordenados, otimizados para retorno rápido, e tratem-no como a decisão autoritativa de entrega.
- Escolham as estratégias de implantação deliberadamente e adotem a entrega progressiva com reversão automatizada para limitar o raio de impacto.
- Desacoplem o lançamento da implantação com feature flags e gerenciem a dívida de flags.
- Em ambientes regulados, capturem a evidência de controle de mudanças automaticamente e não por papelada manual.

## Referências e leitura complementar

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
