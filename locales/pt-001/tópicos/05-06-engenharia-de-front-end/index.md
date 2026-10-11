# 5.6 Engenharia de front-end

## Visão geral e motivação

A engenharia de front-end é a disciplina de construir a camada do software voltada ao cliente: o código que roda no navegador ou no dispositivo e transforma designs, conteúdo e dados numa interface que funciona. Ela abrange escolhas de framework e de arquitetura, estratégia de renderização, gerenciamento de estado, desempenho e resiliência diante da enorme diversidade de navegadores, dispositivos e condições de rede do mundo real. O front-end é onde todo o trabalho a montante (UX, design, conteúdo, acessibilidade, internacionalização) ou chega ao usuário com sucesso ou desmorona.

Para grandes equipes, o front-end é singularmente desafiador, porque está exposto a um ambiente que a organização não controla. Os navegadores, dispositivos, conexões e configurações dos usuários variam enormemente, e a plataforma (a web) evolui continuamente. Em escala, as escolhas arquiteturais se compõem. Um framework escolhido hoje restringe a contratação, o desempenho e a manutenibilidade por anos, e milhares de pequenas decisões sobre o tamanho do pacote e a renderização se somam à experiência que os usuários de fato recebem. Padrões compartilhados, bibliotecas de componentes, orçamentos de desempenho e padrões arquiteturais são o que impede muitas equipes independentes de produzir um todo lento, inconsistente e frágil.

A relevância para empresas e governo é aguda. As empresas mantêm aplicações de longa vida em que a longevidade do framework e a manutenibilidade importam mais que a novidade e em que muitas equipes precisam interoperar. Os governos atendem o público inteiro, inclusive pessoas em dispositivos antigos, conexões lentas ou com franquia de dados e tecnologias assistivas. Isso faz do desempenho, do [aprimoramento progressivo](https://en.wikipedia.org/wiki/Progressive_enhancement) e da resiliência algo não opcional, mas a diferença entre um serviço que funciona para todos e um que exclui os menos favorecidos. Um serviço governamental que só funciona no celular mais novo com conexão rápida falha em seu mandato.

## Princípios fundamentais

- O front-end roda num ambiente que vocês não controlam. Projetem para a variabilidade e a falha.
- Escolham tecnologia chata e durável para sistemas de longa vida. Otimizem a manutenibilidade e a contratação.
- O desempenho é uma funcionalidade e, para muitos usuários, um pré-requisito de acesso.
- Aprimoramento progressivo: entreguem primeiro uma experiência central que funciona e depois acrescentem melhorias em camadas.
- Enviem menos código. O código mais rápido e confiável é o que vocês não entregam.
- Combinem a estratégia de renderização com o tipo de conteúdo e a necessidade do usuário, não com a moda.
- Resiliência: a interface deve se degradar com elegância, não quebrar, quando algo dá errado.
- Padrões e recursos da plataforma sobrevivem aos frameworks. Apoiem-se na plataforma.

## Recomendações

### Escolha frameworks pela longevidade e pelo ajuste, não pelo hype

Selecionem a tecnologia de front-end com base no problema, na equipe, no horizonte de manutenção e no mercado de contratação, e não no que está em alta. Para sistemas corporativos e governamentais de longa vida, favoreçam tecnologias maduras e bem apoiadas, com grandes bancos de talentos, práticas estáveis de lançamento e caminhos claros de atualização. Pesem o custo total da agitação de frameworks: as reescritas são caras e arriscadas. Prefiram abordagens que se apoiam em [padrões web](https://en.wikipedia.org/wiki/Web_standards) para que o seu investimento sobreviva à rotatividade de frameworks e isolem o código específico de framework atrás de fronteiras para que a aplicação não fique refém do ciclo de vida de uma biblioteca.

### Combine a estratégia de renderização com a necessidade

As principais estratégias de renderização se ajustam cada uma a um conteúdo diferente. A renderização no servidor (SSR) produz uma primeira pintura rápida e bom SEO ([otimização para mecanismos de busca](https://en.wikipedia.org/wiki/Search_engine_optimization)) e funciona sem JavaScript no cliente, servindo a páginas pesadas em conteúdo e voltadas ao público. A [geração estática de sites](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) pré-renderiza na hora do build para máxima velocidade e capacidade de cache, ideal para conteúdo que muda com pouca frequência. A renderização no cliente (CSR) serve a experiências muito interativas, tipo aplicativo, atrás de autenticação. O streaming e a hidratação progressiva enviam e ativam a página de modo incremental para que os usuários vejam e usem o conteúdo mais cedo. Muitos grandes sistemas misturam essas estratégias por rota em vez de escolher uma globalmente. Gerenciem o estado deliberadamente: mantenham distintos o estado do servidor, o estado da URL e o estado local da UI e evitem centralizar demais tudo num único armazenamento global pesado.

### Trate o desempenho como uma disciplina orçada e medida

Adotem orçamentos de desempenho (limites explícitos de tamanho do pacote, número de requisições e métricas-chave) e imponham-nos no CI para que as regressões falhem o build. Acompanhem os Core Web Vitals (carregamento, interatividade e estabilidade visual) usando monitoramento de usuários reais, de dispositivos e redes de verdade e não apenas testes de laboratório em máquinas rápidas. Reduzam o JavaScript de forma agressiva: dividam o código e façam [carregamento preguiçoso](https://en.wikipedia.org/wiki/Lazy_loading) para que os usuários baixem apenas o de que uma dada visão precisa, adiem o trabalho não crítico e prefiram os recursos da plataforma a bibliotecas pesadas. Otimizem imagens e fontes, façam cache com eficácia e meçam em dispositivos de baixo desempenho representativos e conexões lentas.

### Construa com aprimoramento progressivo e resiliência

Comecem de uma linha de base que funciona com HTML semântico e pouco ou nenhum JavaScript e depois melhorem para clientes capazes. Isso garante que a tarefa central continue possível quando scripts não carregam, um dispositivo é antigo ou uma rede é instável, uma realidade comum e não um caso de borda. Tratem os erros com elegância: mostrem estados úteis para carregando, vazio, erro e offline em vez de telas em branco ou indicadores de carregamento infinitos. Para serviços de que as pessoas dependem, considerem técnicas offline-first para que o aplicativo continue utilizável com conectividade intermitente, sincronizando quando a conexão voltar.

### Garanta a compatibilidade entre navegadores, dispositivos e tecnologias assistivas

Testem nos navegadores, dispositivos e tecnologias assistivas que os seus usuários de fato têm, guiados por dados reais de análise e não pelas máquinas da equipe. Usem aprimoramento progressivo e detecção de recursos em vez de presumir que os recursos mais novos da plataforma estão disponíveis em toda parte. Construam de forma [responsiva](https://en.wikipedia.org/wiki/Responsive_web_design) (veja o capítulo do sistema de design) para que uma base de código sirva de celulares a computadores. Integrem a acessibilidade e a internacionalização à arquitetura do front-end desde o início, e não em passadas posteriores.

### Governe o front-end como infraestrutura compartilhada

Forneçam bibliotecas compartilhadas de componentes, lint, formatação e ferramentas de build para que as equipes sejam consistentes e produtivas. Estabeleçam diretrizes arquiteturais (como estruturar aplicações, gerenciar estado e dividir pacotes) e orçamentos de desempenho impostos no CI. Para front-ends muito grandes, considerem arquiteturas modulares ou de micro-front-ends que permitam às equipes implantar de forma independente, mas pesem com cuidado a complexidade e o custo de desempenho adicionais, pois não são gratuitos.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Framework popular e maduro | Grande banco de talentos, estável, com apoio | Pode carregar peso legado. Mais lento para adotar as funcionalidades mais novas |
| Framework mais novo | Funcionalidades modernas, ganhos de desempenho | Risco de agitação, pequeno banco de talentos, longevidade incerta |
| SSR / SSG | Primeira pintura rápida, SEO, funciona sem JS | Complexidade de servidor ou de build, desafios de cache |
| CSR (SPA) | Interatividade rica, sensação de aplicativo | Primeiro carregamento lento, dependente de JS, custo de SEO e de resiliência |
| Muito JavaScript no cliente | Funcionalidades ricas | Desempenho ruim em dispositivos de baixo desempenho, frágil |
| Aprimoramento progressivo | Resiliente, inclusivo, funciona em toda parte | Mais esforço de design para definir uma linha de base que funcione |
| Micro-front-ends | Implantações independentes por equipe, escala | Complexidade, dependências duplicadas, custo adicional de desempenho |

A troca recorrente é riqueza e conveniência do desenvolvedor versus alcance, desempenho e resiliência. As abordagens pesadas no cliente são agradáveis de construir e demonstrar em máquinas rápidas, mas excluem usuários em dispositivos e redes fracos. Para públicos corporativos e especialmente governamentais, inclinem a balança para o desempenho, o aprimoramento progressivo e a durabilidade, porque o custo de excluir usuários é alto e muitas vezes inegociável.

## Perguntas para discutir com sua equipe

1. **Como isolamos o código específico de framework para que a aplicação não fique refém do ciclo de vida de uma biblioteca?** Para sistemas corporativos e governamentais de longa vida, a agitação de frameworks é a maior despesa evitável: uma reescrita é cara e arriscada, e a biblioteca em alta hoje restringe a contratação e a manutenção por anos. Apoiar-se em padrões web e pôr o código específico de framework atrás de fronteiras claras significa que a sua lógica de negócio e o seu conteúdo sobrevivem à próxima rotatividade de frameworks. Decidam onde ficam essas costuras e se um engenheiro novo saberia distinguir código de plataforma de código de framework. Levem uma estimativa do que custou a última migração de framework, ou do que custará a que se aproxima. Se a sua lógica central está soldada às APIs de uma biblioteca, precifiquem esse acoplamento antes de defender a escolha do framework.

2. **Combinamos a estratégia de renderização por rota, ou forçamos uma estratégia sobre o produto inteiro?** A renderização no servidor dá uma primeira pintura rápida e funciona sem JavaScript no cliente para conteúdo público, a geração estática maximiza a velocidade das páginas que mudam pouco e a renderização no cliente serve a superfícies interativas, tipo aplicativo, atrás de login. Forçar uma só globalmente ou deixa lentas as páginas públicas com JavaScript pesado ou engenheira demais uma simples página de conteúdo. Isso é uma questão de alcance para o governo, onde um serviço que só funciona depois que um pacote grande carrega exclui usuários em dispositivos antigos e conexões lentas. Levem as rotas principais e rotulem cada uma com a estratégia que ela de fato usa hoje. Se uma página voltada ao público precisa de JavaScript para mostrar o conteúdo, decidam se isso é uma escolha deliberada ou um acidente.

3. **Quão disciplinado é o nosso gerenciamento de estado, e estamos centralizando demais tudo num único armazenamento global pesado?** Manter distintos o estado do servidor, o estado da URL e o estado local da UI previne o acoplamento e as tempestades de re-renderização que tornam lentos e frágeis os grandes front-ends, mas o padrão tentador é despejar tudo num único armazenamento global. Isso se agrava em escala, onde muitas equipes tocando um armazenamento compartilhado criam dependências ocultas e desempenho imprevisível. Combinem onde cada tipo de estado pertence e o que não pertence ao armazenamento global. Levem um componente que re-renderiza mais do que deveria e rastreiem por quê. Se a resposta é um armazenamento central inchado, decidam as fronteiras antes que o acoplamento endureça.

4. **Quais são os nossos orçamentos de desempenho, eles falham o build no CI e são medidos nos dispositivos que os nossos usuários de fato têm?** Um orçamento que ninguém impõe é um desejo, e um orçamento medido apenas nos notebooks rápidos da equipe descreve um usuário que não existe. Para uma grande organização, os orçamentos são o único mecanismo que mantém sob controle o tamanho do pacote e os Core Web Vitals à medida que dezenas de equipes acrescentam funcionalidades a uma superfície compartilhada, porque nenhum revisor isolado consegue pegar toda regressão a olho nu. A pressão concorrente é a velocidade de entrega: uma falha dura de build por alguns quilobytes parece obstrutiva até vocês precificarem o abandono que ela previne. Levem os orçamentos atuais, os dados de monitoramento de usuários reais de dispositivos de baixo desempenho e conexões lentas e a lista de lançamentos em que uma regressão escapou. No governo, onde o mandato é servir o público inteiro, inclusive pessoas em celulares antigos e dados com franquia, liguem o orçamento ao décimo mais lento dos seus usuários e não à mediana e façam do portão de CI algo inegociável.

5. **Quais dos nossos serviços precisam continuar funcionando sem JavaScript no cliente, e de fato testamos esse caminho?** O aprimoramento progressivo é fácil de alegar e fácil de quebrar em silêncio, porque o caminho aprimorado é o que os desenvolvedores usam todo dia enquanto a linha de base apodrece sem teste. Decidir isso deliberadamente importa em escala, já que muitas equipes entregando numa plataforma presumirão cada uma que os scripts sempre carregam a menos que um padrão compartilhado diga o contrário, e uma única dependência dura pode quebrar a tarefa central para quem teve o pacote falhando. A troca é real: uma linha de base que funciona sem JavaScript custa esforço de design e restringe como vocês constroem a interatividade. Levem as jornadas críticas de usuários, um teste que carrega cada uma com scripts desativados ou falhando e evidência de com que frequência os scripts de fato deixam de carregar em campo. Para um serviço público, um formulário de benefícios ou de impostos que desmorona quando um script expira não é uma experiência degradada: é um cidadão que não consegue cumprir uma obrigação legal, então tratem a linha de base como uma exigência de conformidade e não um luxo.

6. **Quando os micro-front-ends genuinamente compensam a sua complexidade, e quem decide antes de uma equipe recorrer a um?** As implantações independentes por equipe são atraentes, mas os micro-front-ends carregam a complexidade de sistemas distribuídos, dependências duplicadas e um imposto de desempenho que os usuários pagam em carregamentos mais lentos. Sem um ponto de decisão compartilhado, equipes ambiciosas os adotam por conveniência organizacional muito antes de a escala justificar o custo, e o produto inteiro herda o custo adicional. A consideração concorrente é a autonomia: equipes que entregam numa única base de código compartilhada podem bloquear umas às outras, e em escala genuína esse acoplamento é por si um problema caro. Levem o número de equipes que tocam a superfície, a disputa de implantações que vocês realmente experimentam hoje e uma estimativa medida da duplicação de carga útil que uma divisão introduziria. Para plataformas corporativas e governamentais, onde as decisões de arquitetura obrigam muitas equipes por anos e precisam sobreviver a auditoria e passagem de bastão, exijam um limiar explícito e documentado e um dono que aprove a mudança, em vez de deixar cada equipe decidir isoladamente.

## Perspectiva por setor

**Startup.** Velocidade e alcance importam quando cada cadastro conta, então resistam ao pesado aplicativo de página única para páginas públicas. Renderizem no servidor o seu marketing e o fluxo de cadastro para que carreguem depressa nos celulares intermediários e nos dados irregulares que seus primeiros clientes usam e reservem a interatividade no cliente para o aplicativo atrás do login. Definam um simples orçamento de tamanho de pacote no CI para que uma dependência descuidada não infle a página em silêncio e apoiem-se em padrões web para manter mantível uma base de código minúscula à medida que contratam.

**Pequena empresa.** Sem especialista dedicado em front-end e com orçamento apertado, prefiram um framework mainstream bem apoiado ou um construtor de sites hospedado a qualquer coisa sob medida, para contratar de um grande banco de talentos e comprar manutenção em vez de pôr gente para fazê-la. Enquadrem a escolha como durabilidade: a opção mais barata é a que vocês não são forçados a reescrever em dois anos. Insistam em páginas rápidas e amigáveis ao celular e em marcação acessível de fábrica, já que um checkout lento ou quebrado custa clientes que vocês não podem se dar ao luxo de perder.

**Grande empresa.** O problema é a consistência entre muitas equipes: uma biblioteca compartilhada de componentes, padrões arquiteturais acordados, lint e ferramentas de build e orçamentos de desempenho impostos no CI para que nenhuma equipe possa regredir o todo em silêncio. Escolham frameworks pela longevidade e pela contratação e não pela novidade, isolem o código específico de framework atrás de fronteiras para sobreviver à próxima migração e combinem a estratégia de renderização por superfície. Gerenciem o front-end como infraestrutura compartilhada, com monitoramento de usuários reais, governança e um registro auditável de por que cada escolha arquitetural foi feita.

**Governo.** Vocês servem o público inteiro, inclusive pessoas em dispositivos antigos, conexões lentas ou com franquia e tecnologias assistivas, então o aprimoramento progressivo e o desempenho são obrigações e não polimento. Façam de uma linha de base que funciona sem JavaScript uma regra rígida para os serviços voltados ao cidadão, orcem as páginas para os usuários mais lentos e não para a mediana e mantenham a tarefa central completável quando um script falha. Aplicam-se a contratação e a transparência: favoreçam tecnologia durável e inclinada a padrões, que evite o aprisionamento a um único fornecedor, documentem nos contratos as exigências de acessibilidade e de desempenho e sejam capazes de mostrar que o serviço funciona para o usuário menos favorecido, e não apenas no dispositivo da demonstração.

## Exemplos

**Startup.** Uma startup em estágio inicial foi tentada a construir o site de marketing e o fluxo de cadastro como um pesado aplicativo de página única, mas seus clientes-alvo eram compradores muitas vezes em celulares intermediários com dados móveis irregulares. Os dois fundadores renderizaram em vez disso as páginas públicas no servidor, para que carregassem depressa e funcionassem antes de qualquer JavaScript rodar, e reservaram a interatividade no cliente para o aplicativo atrás do login. Definiram um simples orçamento de tamanho de pacote no CI para que uma dependência descuidada não inflasse a página em silêncio. O primeiro carregamento enxuto e rápido melhorou mensuravelmente os cadastros, e apoiar-se em padrões web manteve fácil de manter a pequena base de código à medida que contratavam.

**Grande empresa.** Uma empresa de serviços financeiros modernizou um conjunto sem fim de aplicações internas e de clientes padronizando um framework maduro, uma biblioteca compartilhada de componentes e orçamentos de desempenho impostos no CI. A estratégia de renderização foi escolhida por superfície: páginas renderizadas no servidor e passíveis de cache para marketing e conteúdo públicos e um aplicativo renderizado no cliente atrás do login para painéis interativos. Os orçamentos de pacote e o monitoramento de usuários reais pegaram regressões antes do lançamento, mantendo rápidos os tempos de carregamento entre as muitas equipes da empresa e reduzindo o risco de agitação de frameworks que antes havia forçado reescritas caras.

**Governo.** Uma equipe nacional de serviço digital construiu serviços voltados ao cidadão com o aprimoramento progressivo como regra rígida: todo serviço funciona primeiro com HTML semântico e renderização no servidor, e o JavaScript apenas aprimora. Isso garante que o serviço funcione em celulares antigos, conexões rurais lentas e tecnologias assistivas, populações que um governo não pode excluir. Os orçamentos de desempenho mantêm leves e rápidas as páginas em dispositivos de baixo desempenho, e a degradação elegante significa que um script que falha nunca impede alguém de completar um pedido de benefícios. O resultado é um serviço rápido, resiliente, acessível e utilizável pelo público inteiro.

## Justificativa de negócio: motivações, ROI e TCO

As escolhas de engenharia de front-end conduzem receita, alcance e custo. O desempenho está diretamente ligado à conversão, ao engajamento e à conclusão de tarefas. As experiências mais rápidas superam mensuravelmente as mais lentas, e para usuários em dispositivos fracos, o desempenho é a linha entre usar o serviço e abandoná-lo. O aprimoramento progressivo e o suporte a vários dispositivos ampliam o público endereçável, o que para o governo é um mandato e para a empresa é participação de mercado. Boas escolhas de framework e de arquitetura reduzem a frequência e o custo das reescritas, a maior despesa evitável da engenharia de front-end.

No TCO, os custos de adoção são a disciplina dos orçamentos de desempenho e dos testes, o esforço do aprimoramento progressivo e o investimento em ferramentas e bibliotecas de componentes compartilhadas. O custo de não adotar é pago em experiências lentas que perdem usuários e receita, na exclusão de usuários de dispositivos de baixo desempenho e de tecnologia assistiva (com exposição jurídica no governo), em aplicações frágeis que quebram em campo e em caras agitações de frameworks e reescritas movidas por perseguir modas. Os problemas de front-end aparecem como abandono difuso e carga de suporte e não como uma única linha de despesa, então é fácil investir pouco neles.

Para defender o caso junto à liderança, liguem os Core Web Vitals e os tempos de carregamento aos funis de conversão e de conclusão, quantifiquem os usuários excluídos por abordagens pesadas no cliente e precifiquem o custo de reescritas passadas ou iminentes contra a estabilidade de uma arquitetura durável e inclinada a padrões. Enquadrem os orçamentos de desempenho e o aprimoramento progressivo como redução de risco e ampliação de alcance.

## Antipadrões e armadilhas

- **Perseguir frameworks**: reescrever na biblioteca mais recente, incorrendo em agitação sem benefício ao usuário.
- **Experiências só de JavaScript**: nada funciona até um pacote grande carregar e rodar, excluindo muitos usuários.
- **Testar só em dispositivos rápidos**: os notebooks topo de linha da equipe escondem a experiência real do usuário.
- **Ignorar o tamanho do pacote**: crescimento ilimitado de dependências até as páginas ficarem lentas em toda parte.
- **Sem orçamento de desempenho**: as regressões se acumulam em silêncio, lançamento após lançamento.
- **Falhas de tela em branco**: sem estados de carregando, vazio, erro ou offline. Uma requisição que falha quebra a página.
- **Estado global centralizado demais**: tudo num só armazenamento, criando acoplamento e tempestades de re-renderização.
- **Micro-front-ends prematuros**: complexidade de sistemas distribuídos e cargas úteis duplicadas sem a escala para justificá-las.
- **Negligenciar a acessibilidade e a i18n na arquitetura**: parafusá-las depois a alto custo.

## Modelo de maturidade

**Nível 1: Iniciar.** Front-end ad hoc, construído por equipe, sem padrões compartilhados. Muito código no cliente, sem orçamentos de desempenho, testado apenas nos próprios dispositivos da equipe. As escolhas de framework são feitas por preferência ou hype, e um script que falha pode deixar os usuários olhando para uma tela em branco.

**Nível 2: Desenvolver.** Algumas equipes adotam ferramentas compartilhadas e uma biblioteca de componentes, mas a prática é inconsistente na organização. O desempenho é medido ocasionalmente em vez de orçado ou imposto. A estratégia de renderização costuma ser uniforme independentemente do tipo de conteúdo, e o teste entre dispositivos é limitado e manual.

**Nível 3: Padronizar.** O framework e a arquitetura são escolhidos deliberadamente pela longevidade, e as escolhas são documentadas e impostas em toda a organização. A estratégia de renderização é combinada por superfície, o aprimoramento progressivo e a degradação elegante são o padrão e bibliotecas compartilhadas de componentes, lint e ferramentas de build se aplicam a toda equipe. A compatibilidade entre navegadores, a acessibilidade e a internacionalização são embutidas e não parafusadas.

**Nível 4: Gerenciar.** O front-end é medido e controlado com dados. Os orçamentos de desempenho são impostos no CI para que as regressões falhem o build, e os Core Web Vitals são acompanhados com monitoramento de usuários reais de dispositivos de baixo desempenho e conexões lentas de verdade contra linhas de base explícitas. O tamanho do pacote, a cobertura de estados de erro e offline e a parcela de usuários atendidos nas conexões mais lentas são reportados e revisados, de modo que as decisões repousam em evidências e não em opinião.

**Nível 5: Orquestrar.** O desempenho, a resiliência e o alcance são continuamente melhorados e ligados a resultados de negócio em toda a organização. O front-end se apoia em padrões web para a durabilidade, isola as dependências de framework para que as migrações sejam baratas e evolui a arquitetura de modo adaptativo à medida que dispositivos, a plataforma e os dados de usuários reais mudam. O público inteiro e todos os dispositivos são de primeira classe, e a prática de front-end é integrada ao design, à acessibilidade e ao planejamento de produto e não tratada como uma preocupação separada.

## Ideias para discussão

- Como vocês decidem quando uma migração de framework vale o seu custo e risco?
- Que Core Web Vitals e orçamentos de pacote devem ser limiares rígidos que falham o build?
- Onde o aprimoramento progressivo é essencial, e onde um aplicativo no cliente é aceitável?
- Como vocês mantêm consistente a arquitetura de front-end entre muitas equipes autônomas?
- Quando os micro-front-ends genuinamente compensam a sua complexidade?
- Como o teste em dispositivos reais e em redes lentas deve ser embutido no pipeline?

## Principais conclusões

- O front-end roda num ambiente que vocês não controlam. Projetem para a variabilidade e a falha.
- Escolham tecnologia durável e bem apoiada para sistemas de longa vida. Apoiem-se em padrões web.
- Combinem a estratégia de renderização (SSR, SSG, CSR, streaming) com o conteúdo e a necessidade, muitas vezes misturada por rota.
- Tratem o desempenho como uma disciplina orçada e medida, imposta no CI com dados de usuários reais.
- Construam com aprimoramento progressivo para que a experiência central funcione em toda parte.
- Enviem menos JavaScript. Dividam o código, façam carregamento preguiçoso e prefiram os recursos da plataforma.
- Para o governo especialmente, o desempenho e a resiliência são pré-requisitos do acesso equitativo.

## Referências e leitura complementar

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
