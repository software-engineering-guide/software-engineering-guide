# 2.16 Engenharia de desempenho

## Visão geral e motivação

A engenharia de desempenho é o ofício de tornar o código rápido o bastante, de propósito, usando medição em vez de instinto. Este capítulo trabalha no nível do código e dos componentes: funções, laços, estruturas de dados, consultas, alocações e a maneira como um único serviço gasta seu tempo. É o companheiro do capítulo 3.5, que trata do desempenho no nível do sistema (escalar horizontalmente, balanceamento de carga, capacidade e resiliência). Quando um sistema está lento, o capítulo 3.5 pergunta de quantas máquinas você precisa. Este capítulo pergunta por que uma máquina está fazendo tanto trabalho logo de início. Você geralmente precisará dos dois, e a visão no nível do código é onde uma quantidade surpreendente de custo e latência de fato se esconde.

Para equipes grandes, essa disciplina importa porque o desempenho decai em silêncio. Nenhum commit isolado deixa um serviço lento, mas mil pequenos, cada um acrescentando uma chamada ao banco de dados ou um laço sem limite, deixam. Sem um método compartilhado para medir, orçar e barrar o desempenho, você só descobre o apodrecimento quando um cliente reclama ou um lançamento derrete. Um método transforma o desempenho de um combate heroico a incêndio numa propriedade rotineira que você protege.

Para as empresas, o desempenho é dinheiro: código mais rápido significa menos máquinas, contas de nuvem menores e a capacidade de cumprir um [acordo de nível de serviço](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) de latência sem superprovisionar. Para o governo, o desempenho é acesso: uma página que carrega num celular antigo por uma conexão móvel fraca é a diferença entre um cidadão concluir um pedido de benefício e desistir. Os sistemas públicos também precisam de evidências reproduzíveis de benchmark, porque os órgãos de contratação e de supervisão pedirão que você prove os números, e não apenas os afirme.

## Princípios fundamentais

- **Meça antes de otimizar.** O gargalo quase nunca está onde você adivinha. Faça profiling e depois aja.
- **Evite a otimização prematura.** O alerta de Donald Knuth continua valendo: otimizar código que não importa custa clareza e não compra nada.
- **Defina “rápido o bastante” como um número.** Um orçamento de desempenho com uma meta e um percentil transforma opinião em aprovado ou reprovado.
- **Médias mentem. Percentis dizem a verdade.** A cauda (p99) é o que os usuários sentem, não a média.
- **Ganhos algorítmicos vencem microajustes.** Uma classe de complexidade melhor supera qualquer quantidade de esperteza de fator constante.
- **Latência e vazão são objetivos diferentes.** Melhorar um pode piorar o outro. Saiba qual você está comprando.
- **Faça benchmarks com honestidade ou não faça.** Aquecimento, variância e uma carga representativa separam números reais de ficção.
- **Barre o desempenho na CI, observe-o em produção.** Regressões pegas antes da integração são baratas. Pegas pelos usuários, caras.

## Recomendações

### Meça primeiro e faça profiling antes de tocar numa linha

A regra mais antiga neste campo é a mais ignorada: encontre o gargalo antes de otimizar. Recorra a um [profiler](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), uma ferramenta que amostra ou instrumenta um programa em execução para mostrar onde ele gasta tempo e memória. Faça profiling de CPU (quais funções queimam ciclos), de memória e alocação (o que é alocado e com que frequência, já que a rotatividade de alocações impulsiona as pausas da coleta de lixo) e de E/S (tempo gasto esperando disco, rede ou banco de dados). Um [gráfico de chamas](https://en.wikipedia.org/wiki/Flame_graph), uma visualização empilhada em que cada caixa é uma função e sua largura é o tempo gasto, torna óbvio de relance o custo dominante: procure as caixas mais largas, não as pilhas mais profundas. Otimize o maior custo primeiro, meça de novo e pare quando atingir o orçamento. Isso se liga às práticas de observabilidade do capítulo 9.2, porque um profile de produção vence qualquer palpite feito num laptop.

Proteja-se também do erro oposto. A frase completa de Knuth é que a otimização prematura é a raiz de muito mal, e ele se referia às pequenas ineficiências que tentam você a sacrificar código legível por velocidade imaginada. Escreva primeiro a versão clara, meça e otimize apenas o código que o profiler incriminar.

### Defina o que significa “rápido o bastante” com orçamentos de desempenho

A velocidade não é uma virtude no abstrato: é uma meta que você cumpre ou perde. Defina um **orçamento de desempenho**: um limite concreto como “latência p99 do pagamento abaixo de 300 ms” ou “este endpoint aloca menos de 1 MB por requisição”. Ligue-o a algo que os usuários ou o negócio sentem e expresse-o como um **percentil**, não como uma média, porque a média esconde a cauda lenta onde moram os usuários reais. Se 1% das requisições leva 5 segundos, sua média pode parecer boa enquanto uma fatia significativa de clientes sofre. Os orçamentos dão a uma equipe uma definição compartilhada e indiscutível de pronto e uma linha que uma regressão visivelmente cruza.

### Recorra à eficiência algorítmica antes do microajuste

Os maiores e mais baratos ganhos vêm da [eficiência algorítmica](https://en.wikipedia.org/wiki/Algorithmic_efficiency), como o trabalho cresce à medida que a entrada cresce, descrita com a [notação Big O](https://en.wikipedia.org/wiki/Big_O_notation) (uma forma de classificar a taxa de crescimento, de modo que uma ordenação O(n log n) escala muito melhor que uma O(n ao quadrado)). Um laço aninhado que é invisível com dez itens vira uma catástrofe com dez mil. Antes de ajustar à mão uma função quente, pergunte se ela está fazendo fundamentalmente trabalho demais: uma consulta N+1 acidental, uma varredura linear que deveria ser uma busca em hash ou trabalho repetido que poderia ser memoizado. Isso se liga aos fundamentos algorítmicos do capítulo 2.13. Nenhuma quantidade de ajuste de fator constante resgata a classe de complexidade errada.

### Distinga latência de vazão e respeite a cauda

A **latência** é quanto tempo uma operação leva. A **vazão** é quantas operações se completam por unidade de tempo. Não são o mesmo objetivo, e otimizar um pode prejudicar o outro. O agrupamento em lotes melhora a vazão mas acrescenta latência ao primeiro item do lote. Acrescentar trabalhadores paralelos eleva a vazão mas pode piorar a latência de cauda por contenção. Decida de qual dos dois os seus usuários realmente precisam. E sempre observe a cauda: a latência p95 e p99, os 5% e 1% mais lentos das requisições, porque em escala um usuário faz muitas requisições e atinge a cauda com frequência. Relate os percentis, alerte sobre eles e orce para eles.

### Conheça os limites do paralelismo

Quando você paraleliza, lembre-se da [lei de Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): o ganho de velocidade de acrescentar processadores é limitado pela fração do trabalho que precisa rodar em série. Se 10% de um trabalho é inerentemente sequencial, nenhum número de núcleos leva você além de uma aceleração de 10x. A concorrência (estruturar o trabalho para que as tarefas possam progredir de forma independente) e o paralelismo (executá-las de fato ao mesmo tempo) acrescentam complexidade real, de condições de corrida a custo de coordenação. Meça a fração serial antes de presumir que mais threads vão salvar você e seja honesto de que a versão correta mais simples muitas vezes é rápida o bastante.

### Use cache e localidade de dados, e respeite os custos deles

Um [cache](https://en.wikipedia.org/wiki/Cache_(computing)), um armazenamento rápido de resultados recentes ou caros de calcular, é a ferramenta de desempenho mais poderosa que você tem e a mais perigosa. A tirada de Phil Karlton de que os dois problemas difíceis da ciência da computação são a invalidação de cache e nomear coisas é um aviso: um cache obsoleto serve respostas erradas, e a lógica de invalidação é onde nascem os bugs sutis. Faça cache de forma deliberada, defina validades e conheça a sua história de correção antes de otimizar a taxa de acerto. No nível mais baixo, a [localidade de referência](https://en.wikipedia.org/wiki/Locality_of_reference), manter próximos na memória os dados usados juntos, explora a hierarquia de cache da CPU e pode tornar o código várias vezes mais rápido sem mudança algorítmica, transformando falhas de cache em acertos. Os vetores contíguos vencem as estruturas de perseguição de ponteiros por essa razão. Isso se cruza com as escolhas de layout de dados do capítulo 3.4.

### Faça benchmarks com honestidade e desconfie dos microbenchmarks

Um benchmark que mente é pior que nenhum, porque dá falsa confiança. Aqueça antes de medir, para cronometrar o comportamento em regime estável e não a inicialização única e a compilação just-in-time. Rode muitas iterações e relate a variância, não um único número de sorte. Use uma carga representativa, com tamanhos e distribuições de dados realistas, porque um microbenchmark numa entrada de brinquedo muitas vezes mede a capacidade do compilador de apagar o seu teste e não a velocidade real do código. Cuidado com as armadilhas clássicas: um valor que o otimizador prova não usado e remove, um laço que o tempo de execução içará ou um cache que está quente no benchmark e frio em produção. Na dúvida, meça o caminho inteiro, não a função isolada.

### Barre o desempenho na CI e observe-o em produção

Faça do desempenho uma propriedade que o pipeline protege. Acrescente testes de desempenho à estratégia do capítulo 2.4, com portões de regressão que quebram o build quando um benchmark ou orçamento importante piora além de um limite. Isso pega a deterioração lenta antes de ela ser integrada. Depois feche o ciclo em produção com a telemetria do capítulo 9.2: acompanhe percentis reais de latência, taxas de alocação e consultas lentas contra os seus orçamentos, porque o tráfego de produção encontra os casos que seus benchmarks nunca imaginaram.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Otimizar já, por intuição | Parece produtivo. Vitória ocasional de sorte | Em geral ajusta o código errado. Acrescenta complexidade sem ganho |
| Medir primeiro, depois otimizar | Mira o gargalo real. Baseado em evidências | Exige ferramentas e disciplina. Mais lento para começar |
| Cache | Grandes ganhos de latência e de vazão | Bugs de invalidação. Dados obsoletos. Custo de memória |
| Mais paralelismo | Maior vazão em trabalho paralelo | Teto de Amdahl. Contenção. Bugs de concorrência |
| Microotimização | Espreme fatores constantes | Teto pequeno. Prejudica a legibilidade. Muitas vezes é ruído |
| Melhoria algorítmica | Os ganhos escalam com o tamanho da entrada | Exige análise. Às vezes uma reescrita maior |
| Portões de desempenho na CI | Param as regressões cedo e barato | Benchmarks instáveis corroem a confiança. Exige ambiente estável |

A tensão central é esforço versus retorno, e a resolução é a medição. O trabalho de desempenho tem retornos acentuadamente decrescentes: a primeira correção guiada por profiling pode reduzir a latência pela metade, a décima pode tirar um por cento enquanto dobra a complexidade do código. Você resolve isso recusando-se a otimizar sem um número em mãos e um orçamento a cumprir. Meça para encontrar a correção que vale a pena fazer e pare no momento em que superar o orçamento em vez de perseguir velocidade por si mesma.

## Perguntas para discutir com sua equipe

1. **Vocês têm um orçamento de desempenho escrito para seus caminhos críticos, e ele é expresso como um percentil?** Muitas equipes têm uma vaga noção de que as coisas deveriam ser “rápidas”, mas nenhum número contra o qual alguém pudesse falhar, o que significa que o desempenho não é tarefa de ninguém até quebrar. Um orçamento como “p99 abaixo de 300 ms” torna a meta concreta, dá aos revisores algo para impor e transforma uma regressão num evento visível em vez de um deslize lento. Isso importa mais em equipes grandes, onde a latência se infiltra por muitas mãos e nenhum autor vê o custo acumulado. Leve seus dados atuais de latência e pergunte se vocês estão relatando médias, que lisonjeiam, ou percentis, que dizem a verdade. Se vocês não conseguem dizer o que “rápido o bastante” significa como um número, isso é a primeira coisa a corrigir.

2. **Na última vez que otimizaram algo, um profiler mostrou onde olhar, ou vocês adivinharam?** O gargalo está famosamente em outro lugar que não onde os engenheiros experientes esperam, e o tempo gasto ajustando o código errado é tempo perdido duas vezes, uma no trabalho e outra na complexidade acrescentada. Uma cultura que faz profiling primeiro gasta seu esforço onde ele compensa e deixa em paz o código claro. Peça à sua equipe que lembre as três últimas correções de desempenho e se cada uma partiu de uma medição ou de um palpite. Considere se vocês conseguem fazer profiling em produção, ou num ambiente de homologação realista, porque um profile de laptop pode enganar muito. A resposta revela se o seu trabalho de desempenho é engenharia ou folclore.

3. **O que impede uma regressão de desempenho de chegar à produção hoje?** Numa equipe em crescimento, a resposta honesta muitas vezes é “uma reclamação de cliente”, o que significa que os usuários são o seu teste de regressão. Um portão de CI que quebra o build quando um benchmark ou orçamento piora pega o problema enquanto é barato de corrigir e o autor ainda se lembra da mudança. Discutam se seus benchmarks são estáveis o bastante para servir de portão, porque um teste de desempenho instável que grita lobo será ignorado ou desativado. Falem também do que vocês observam em produção, já que algumas regressões só aparecem sob tráfego e dados reais. O objetivo é fazer do desempenho uma propriedade que o sistema defende automaticamente, não uma que vocês redescobrem num incidente.

4. **Vocês otimizam para latência ou para vazão em cada caminho crítico, e alguém escreveu essa escolha?** São objetivos diferentes que puxam em sentidos opostos: o agrupamento em lotes e os trabalhadores paralelos elevam a vazão mas podem acrescentar latência a requisições individuais, então uma equipe que otimiza por instinto muitas vezes compra o eixo errado e faz os usuários esperarem para economizar tempo de máquina que ninguém estava faltando. Numa equipe grande o perigo se multiplica, porque um grupo ajusta um serviço compartilhado para vazão em massa enquanto outro depende dele para latência interativa, e nenhum conhece a meta do outro. Leve o padrão de uso real de cada caminho (requisição interativa versus lote em segundo plano), a latência percentil atual e a vazão sustentada de que vocês precisam e então decidam o eixo explicitamente em vez de deixar um padrão emergir. Para um sistema corporativo ou governamental sob um SLA, nomeiem contra qual métrica o acordo é escrito, porque otimizar o eixo não medido pode violar um contrato enquanto seus painéis parecem saudáveis.

5. **Como vocês sabem que seus benchmarks medem trabalho real e não o otimizador apagando o seu teste?** Um benchmark que mente é pior que nenhum, porque entrega à equipe falsa confiança e depois uma regressão é entregue mesmo assim. As equipes rotineiramente relatam um único número de sorte de uma execução fria numa entrada de brinquedo, que mede a inicialização, a compilação just-in-time e a capacidade do compilador de remover código não usado, e não o comportamento que os usuários de fato enfrentam. Leve um benchmark de exemplo e interrogue-o: ele aquece, roda muitas iterações, relata variância, usa tamanhos e distribuições de dados representativos e derrota a eliminação de código morto sobre o seu resultado? A atração concorrente é que benchmarks honestos são mais lentos de escrever e de rodar que microbenchmarks rápidos, então combinem onde aproximações baratas são aceitáveis e onde vocês exigem rigor. Num contexto público ou regulamentado em que órgãos de contratação e de supervisão pedirão que vocês reproduzam os números, capturem o dispositivo, a carga e o ambiente junto com o resultado para que a afirmação possa ser verificada e não apenas afirmada.

6. **Quando o trabalho de desempenho compete com funcionalidades pelos mesmos engenheiros, como vocês decidem, e quem detém a autoridade sobre o orçamento?** O desempenho tem retornos acentuadamente decrescentes, então a primeira correção guiada por profiling pode reduzir a latência pela metade enquanto a décima tira um por cento por duas vezes a complexidade do código, e sem uma regra vence a voz mais alta ou o prazo mais próximo. As considerações concorrentes são reais: a dívida de desempenho não corrigida se acumula em silêncio e fica mais cara de adaptar depois, mas perseguir velocidade além do orçamento deixa o roteiro sem recursos e acrescenta complexidade que desacelera o trabalho futuro. Leve o estado atual do orçamento de cada caminho crítico, o custo estimado do status quo em máquinas ou conversão perdida e o retorno marginal da próxima otimização, para que a troca seja feita com evidências e não sob pressão. Para uma grande empresa ou programa governamental, nomeiem quem é dono do orçamento de desempenho e quem pode autorizar o gasto de tempo de engenharia contra ele, porque uma meta que ninguém é responsável por defender é uma que se erode em silêncio.

## Perspectiva por setor

**Startup.** A velocidade de entrega vence o processo, então resista a reescritas e a grandes frameworks de desempenho. Gaste uma tarde com um profiler no caminho de que os usuários de fato reclamam, corrija o maior custo (muitas vezes uma consulta N+1 ou uma varredura linear acidental) e acrescente um orçamento leve de percentil à CI para que o ganho não possa regredir em silêncio. Reserve a otimização profunda para o momento em que um número real, e não um palpite, disser que o código está lento demais.

**Pequena empresa.** Sem especialista em desempenho e com orçamento apertado, apoie-se nas ferramentas que você já paga: o profiler do seu ambiente de execução, os percentis de latência do painel de hospedagem e o analisador de consultas embutido no banco de dados. Defina um ou dois orçamentos simples ligados a algo que os clientes sentem, como o tempo de carga da página ou do pagamento, e trate uma violação como sinal para comprar um nível mais rápido ou corrigir a pior consulta, e não para lançar um projeto de ajuste que você não consegue sustentar.

**Grande empresa.** Em escala de frota, o desempenho é custo direto, então governe-o como disciplina compartilhada: ferramentas padrão de profiling, orçamentos de percentil ligados a métricas de negócio e portões de regressão na CI aplicados de forma consistente, para que a deterioração lenta de nenhuma equipe infle a conta de nuvem inteira. Acompanhe latência, alocação e vazão em relação a linhas de base entre os serviços e mantenha evidências reproduzíveis de benchmark, porque uma redução de 30% de CPU numa frota grande é uma economia recorrente que vale auditar e defender contra penalidades de SLA.

**Governo.** O desempenho é uma garantia de acesso: uma página que carrega num celular antigo por uma conexão fraca decide se um cidadão conclui um pedido de benefício. Defina orçamentos explícitos contra dispositivos de baixo desempenho realistas e redes limitadas e publique resultados reproduzíveis de benchmark que capturem o dispositivo, a rede e a carga, para que os órgãos de contratação e de supervisão possam verificar os números em vez de aceitá-los na fé. Prefira a medição transparente e auditável às afirmações de fornecedores e exija dos fornecedores a mesma evidência reproduzível.

## Exemplos

**Startup.** Uma pequena equipe de SaaS nota que seu painel parece lento e fica tentada a reescrevê-lo num framework mais rápido. Em vez disso, passa uma tarde com um profiler e um gráfico de chamas, que mostra que 70% do tempo da requisição é um único endpoint emitindo uma consulta ao banco de dados por linha, o clássico padrão N+1. Eles a substituem por uma consulta em lote, a latência cai de 1,2 segundo para 90 milissegundos e acrescentam um orçamento p99 de 200 ms a um benchmark leve de CI para que a correção não possa regredir em silêncio. Sem reescrita, uma tarde, um ganho de dez vezes.

**Grande empresa.** Uma plataforma de varejo opera milhares de instâncias, e sua conta de nuvem é dominada por um serviço de recomendação. Uma campanha de profiling encontra uma forte rotatividade de alocações causando pausas frequentes da coleta de lixo, mais um cache com taxa de acerto ruim. Ajustar as estruturas de dados para localidade e corrigir as chaves do cache reduz a CPU por requisição em 40%, o que permite à equipe rodar o mesmo tráfego com 40% menos máquinas. A economia paga o esforço de engenharia em semanas, e um SLA de latência p99 que ocasionalmente era violado agora se sustenta com folga, evitando penalidades contratuais.

**Governo.** Uma autoridade tributária nacional precisa atender cidadãos em dispositivos antigos e conexões rurais lentas. A equipe define um orçamento explícito: a página de declaração deve ficar interativa em menos de 3 segundos num celular de baixo desempenho com um perfil de 3G limitado. Eles fazem o profiling da página, cortam o trabalho que bloqueia a interatividade e publicam resultados reproduzíveis de benchmark, capturando o dispositivo, a rede e a carga, para que os órgãos de supervisão e os auditores de acessibilidade possam verificar a afirmação em vez de aceitá-la na fé. O desempenho aqui não é uma alavanca de custo, mas uma garantia de acesso que mantém o serviço utilizável por todos.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da engenharia de desempenho aparece em três livros-caixa. O primeiro é o custo de infraestrutura: código mais rápido faz o mesmo trabalho com menos máquinas, e numa frota grande uma redução de 30% de CPU é uma economia direta e recorrente que faz sombra ao esforço único de engenharia. O segundo é a receita e a satisfação: a latência se correlaciona com conversão, abandono e confiança do usuário, então encurtar a cauda é uma alavanca de crescimento, não apenas uma tarefa de higiene. O terceiro é o risco evitado: uma violação de SLA carrega penalidades, e um lançamento que derrete sob carga carrega dano à reputação e custo de combate a incêndio.

O custo total de propriedade é modesto e concentrado no início. Você investe em ferramentas de profiling, num ambiente estável de benchmark e em portões de CI, além da disciplina de escrever orçamentos e ler profiles. O custo maior e oculto é a alternativa: a dívida de desempenho se acumula em silêncio, e adaptar velocidade a um sistema lento depois do lançamento é muito mais caro que protegê-la continuamente. Defenda o caso junto à liderança nas unidades dela. Traduza a latência em conversão ou em taxas de conclusão de cidadãos, traduza a CPU em gasto mensal de nuvem e traduza um portão de regressão em incidentes evitados. O argumento mais forte é que o desempenho é barato de proteger commit a commit e ruinoso de recuperar depois de apodrecer.

## Antipadrões e armadilhas

- **Otimizar sem fazer profiling.** Ajustar código que não é o gargalo enquanto o custo real fica intocado.
- **Otimização prematura.** Sacrificar clareza por velocidade imaginada que o profiler jamais teria sinalizado.
- **Relatar médias.** Esconder uma cauda dolorosa atrás de uma média confortável. Os usuários sentem o p99, não a média.
- **Teatro de microbenchmarks.** Números de uma carga de brinquedo que o otimizador meio apagou, sem aquecimento nem variância relatados.
- **Cache sem história de invalidação.** Perseguir a taxa de acerto enquanto serve dados obsoletos ou errados.
- **Presumir que mais threads ajudam.** Ignorar a lei de Amdahl e a fração serial e depois se afogar em contenção.
- **Sem portão de regressão.** Deixar os usuários serem o teste de desempenho porque nada na CI protege o orçamento.
- **Otimizar o eixo errado.** Comprar vazão com lotes quando os usuários precisavam de baixa latência, ou o inverso.

## Modelo de maturidade

- **Nível 1, Iniciar:** O desempenho só é tratado quando algo quebra. Sem orçamentos, sem hábito de profiling, sem benchmarks. A otimização é adivinhação guiada pela intuição, e as médias são a única métrica que alguém relata.
- **Nível 2, Desenvolver:** Algumas equipes fazem profiling durante incidentes e mantêm alguns benchmarks, mas a prática é inconsistente e depende do entusiasmo individual. Existem orçamentos informais para um ou dois caminhos críticos e os percentis aparecem em alguns painéis, mas nada barra uma regressão antes de ela ser entregue e cada equipe reinventa a própria abordagem.
- **Nível 3, Padronizar:** Os caminhos críticos carregam orçamentos de percentil escritos, e o profiling é o primeiro passo documentado e esperado antes de alguém otimizar. A CI inclui testes de desempenho com portões de regressão, regras honestas de benchmark (aquecimento, variância, dados representativos) são escritas e impostas em toda a organização e toda equipe segue o mesmo método em vez do próprio.
- **Nível 4, Gerenciar:** A organização mede o desempenho como uma propriedade controlada. Percentis de latência, vazão, taxas de alocação e contagens de consultas lentas são acompanhados em relação a linhas de base explícitas em produção e na CI, as regressões são quantificadas contra limites em vez de discutidas e os orçamentos são ligados a métricas de negócio como conversão ou gasto com nuvem, de modo que uma violação dispara uma decisão baseada em dados. As evidências de benchmark são reproduzíveis e capturadas com seu dispositivo, carga e ambiente para auditoria.
- **Nível 5, Orquestrar:** O desempenho é continuamente melhorado e integrado em toda a organização. Orçamentos, profiling, benchmark honesto e análise de gráficos de chamas são habilidades rotineiras, os portões de regressão são estáveis e confiáveis e os dados de produção e de CI fecham o ciclo automaticamente. A organização adapta os orçamentos conforme o tráfego, o hardware e as prioridades de negócio mudam, reequilibra o esforço para os caminhos onde o retorno é maior e defende o desempenho como uma propriedade permanente e não como uma campanha periódica.

## Ideias para discussão

1. Qual dos seus caminhos críticos tem hoje um orçamento escrito baseado em percentil, e quais são protegidos só pela esperança?
2. Quando um profiler o surpreendeu pela última vez, e o que isso ensinou sobre onde você presume que o tempo vai?
3. Seus benchmarks aquecem, relatam variância e usam dados representativos, ou estão medindo o otimizador?
4. Onde vocês estão gastando máquinas para encobrir código que uma campanha de profiling poderia tornar mais barato?
5. Para a sua carga mais paralelizada, qual é a fração serial, e a lei de Amdahl limita o ganho que vocês perseguem?
6. Se um colega integrasse uma mudança que dobrasse a latência p99, quanto tempo até alguém notar, e como descobririam?

## Principais conclusões

- Meça antes de otimizar. O gargalo raramente está onde você adivinha, e a otimização prematura custa clareza sem ganho.
- Defina “rápido o bastante” como um orçamento de percentil, porque as médias escondem a cauda onde moram os usuários reais.
- Prefira ganhos algorítmicos (uma classe Big O melhor) ao microajuste e saiba se você precisa de latência ou de vazão.
- Respeite os limites do paralelismo (lei de Amdahl) e os perigos do cache (invalidação e obsolescência).
- Faça benchmarks com honestidade, com aquecimento, variância e cargas representativas, e desconfie dos microbenchmarks.
- Barre o desempenho na CI (capítulo 2.4) e observe-o em produção (capítulo 9.2). Complemente a visão no nível do sistema do capítulo 3.5.
- O desempenho é custo para as empresas, acesso para os governos, barato de proteger continuamente mas caro de adaptar depois.

## Referências e leitura complementar

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimisation maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behaviour in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
