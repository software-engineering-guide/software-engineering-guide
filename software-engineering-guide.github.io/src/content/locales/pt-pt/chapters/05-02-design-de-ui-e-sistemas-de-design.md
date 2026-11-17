# 5.2 Design de UI e sistemas de design

## Visão geral e motivação

O [design de interface de usuário (UI)](https://en.wikipedia.org/wiki/User_interface_design) é o ofício de dar forma ao que as pessoas veem e tocam: layout, [tipografia](https://en.wikipedia.org/wiki/Typography), cor, espaçamento, controles e estados. Um [sistema de design](https://en.wikipedia.org/wiki/Design_system) pega esse ofício e o transforma num ativo compartilhado, reutilizável e governado: um conjunto documentado de princípios, componentes, padrões e tokens de que toda equipe se serve, para que o produto inteiro tenha a aparência e o comportamento de um só. O design de UI decide como uma tela deve parecer. Um sistema de design decide como dez mil telas de muitas equipes permanecem coerentes.

Para uma grande organização, o sistema de design é o investimento de maior alavancagem em qualidade de UI e velocidade de entrega. Sem um, cada equipe reinventa botões, formulários, modais e tratamento de erros, cada um um pouco diferente, cada um mantido separadamente, cada um quebrando separadamente. Os usuários pagam por isso em confusão e desconfiança. O negócio paga em esforço duplicado e qualidade desigual. Um sistema de design transforma decisões de design pontuais em capital reutilizável: resolvam a [acessibilidade](https://en.wikipedia.org/wiki/Accessibility), a [responsividade](https://en.wikipedia.org/wiki/Responsive_web_design) e a marca uma vez num componente, e toda equipe herda o resultado.

Empresas e governo acrescentam duas pressões específicas. Primeiro, a escala: centenas de aplicações, muitas construídas por fornecedores ou adquiridas em fusões, precisam todas parecer uma só organização. Segundo, a longevidade e a mudança: as marcas são renovadas, as agências são reorganizadas e uma única plataforma pode precisar atender várias marcas ou subagências a partir de uma única base de código. Um sistema de design bem arquitetado, com temas e tokenização adequados, torna tratáveis, e não catastróficas, essas mudanças amplas.

## Princípios fundamentais

- A consistência reduz a [carga cognitiva](https://en.wikipedia.org/wiki/Cognitive_load). Um botão deve ter a mesma aparência e o mesmo comportamento em toda parte.
- As decisões de design são ativos: capturem-nas uma vez como componentes e tokens reutilizáveis.
- Os tokens são a fonte de verdade das decisões visuais. Os componentes consomem tokens, nunca valores fixos no código.
- A acessibilidade e a responsividade são embutidas nos componentes, não parafusadas por tela.
- Um sistema de design é um produto com usuários (desenvolvedores e designers), não uma entrega única.
- A hierarquia visual guia a atenção: tipo, cor e espaço devem tornar óbvia a importância.
- A governança mantém um sistema coerente. A contribuição o mantém vivo.

## Recomendações

### Estruture o sistema em camadas: tokens, componentes, padrões

Os tokens de design são valores nomeados e agnósticos de plataforma para cor, espaçamento, tipografia, raio, elevação e movimento: as decisões atômicas. Construam-nos em níveis: uma paleta primitiva (valores brutos), tokens semânticos (`color-action-primary`, `space-inset-md`) que carregam significado e tokens em nível de componente onde precisarem. Os componentes consomem os tokens semânticos, de modo que uma única mudança se propaga por toda parte. Acima dos componentes ficam os padrões: composições comprovadas como uma tabela de dados, um formulário de várias etapas ou um estado vazio. Documentem as três camadas num só lugar, com exemplos vivos e orientações de uso.

### Acerte os fundamentos visuais

Montem uma escala tipográfica com hierarquia clara e espaçamento generoso entre linhas para facilitar a leitura e fiquem com um conjunto limitado de tamanhos e pesos. Definam a cor como um sistema, com contraste suficiente para a acessibilidade (veja o capítulo de acessibilidade) e papéis semânticos, em vez de matizes brutos espalhados pela UI. Usem uma escala de espaçamento e uma grade de layout para que o alinhamento e o ritmo continuem consistentes sem palpite por tela. A hierarquia visual deve tornar óbvia, à primeira vista, a ação principal e a informação mais importante.

### Projete para responsividade e com prioridade ao celular

Projetem primeiro para a menor janela de visualização razoável e depois melhorem para telas maiores. Isso obriga a priorizar o conteúdo e os controles essenciais. Usem layouts fluidos e unidades relativas para que as interfaces se adaptem a qualquer tela, em vez de saltar entre alguns pontos de quebra fixos. Façam alvos de toque grandes o bastante e garantam que as interações funcionem com toque, mouse e teclado. No governo especialmente, presumam que uma parcela significativa dos seus usuários está em dispositivos pequenos, antigos ou baratos.

### Faça da passagem do design para o desenvolvimento e da paridade uma preocupação de primeira classe

Um sistema de design só compensa quando a UI entregue corresponde ao design pretendido e continua correspondendo. Mirem uma fonte única de verdade: os tokens exportados da ferramenta de design alimentam diretamente o código, de modo que designers e engenheiros referenciam os mesmos valores. Forneçam uma biblioteca de componentes em código que os engenheiros de fato usarão, com os mesmos nomes e propriedades dos componentes de design. Usem o teste de regressão visual (comparação automatizada da UI renderizada contra imagens-base aprovadas) e verificações de revisão de design para pegar a deriva. E meçam a “paridade design-código” como métrica explícita de saúde: a parcela da UI construída a partir de componentes do sistema versus código pontual.

### Suporte temas e marca branca em escala corporativa

Arquitetem para várias marcas desde o início se houver qualquer chance de precisarem delas. Como os componentes consomem tokens semânticos, um tema é apenas um conjunto diferente de valores de tokens, então uma renovação de marca ou uma nova submarca vira uma mudança de dados e não uma reescrita de código. Suportem temas claro e escuro, modos de alto contraste e marca por locatário pelo mesmo mecanismo. Mantenham a lógica específica de marca fora dos componentes e empurrem-na para conjuntos de tokens e configuração.

### Governe o sistema como um produto

Deem ao sistema de design uma equipe dedicada, um roteiro, versionamento, um registro de mudanças e um canal de suporte. Detalhem como as equipes contribuem com novos componentes e como eles são revisados e promovidos. Equilibrem o controle central (para preservar a coerência e a acessibilidade) com um modelo de contribuição (para que o sistema evolua com necessidades reais em vez de virar um gargalo). Comuniquem com clareza as descontinuações e migrações e deem às equipes consumidoras antecedência suficiente.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Construir um sistema de design | Consistência, velocidade, acessibilidade uma vez, renovações de marca mais fáceis | Custo inicial e contínuo, exige uma equipe dedicada |
| Adotar um sistema de prateleira | Início rápido, padrões comprovados | Aparência genérica, mais difícil de ajustar a marca e às necessidades únicas |
| Governança central estrita | Coerência, qualidade, acessibilidade garantidas | Pode gerar gargalo nas equipes, parecer burocrática |
| Modelo aberto de contribuição | Evolui com necessidades reais, responsabilidade compartilhada | Risco de deriva e inconsistência sem revisão |
| Tokenização e temas pesados | Renovações de marca baratas e suporte a várias marcas | Mais abstração, curva de aprendizado mais íngreme |

Os sistemas de design trocam custo inicial e de governança por consistência e velocidade de longo prazo. Para um produto pequeno, de uma só equipe, o custo adicional pode não compensar. Para uma grande organização com muitas equipes e produtos de longa vida, a pergunta não é se ter um sistema, mas quanto investir e como governá-lo. O arrependimento mais comum é investir pouco em governança e em ferramentas de paridade: o sistema existe no papel, mas as equipes se afastam dele em silêncio.

## Perguntas para discutir com sua equipe

1. **Como é a hierarquia de camadas da nossa arquitetura de tokens, e os componentes são proibidos de usar valores fixos no código?** Todo o ganho de um sistema de design (renovações de marca baratas, temas multimarca, acessibilidade resolvida uma vez) depende de os componentes consumirem tokens semânticos como `color-action-primary` e não matizes brutos e valores em pixels espalhados pelo código. Decidam agora os níveis: uma paleta primitiva, tokens semânticos que carregam significado e tokens em nível de componente só onde realmente precisarem. A abstração excessiva é um risco real, então combinem quantas camadas são demais e como um desenvolvedor acha depressa o token certo. Levem uma busca (grep) de cores e espaçamentos fixos no código como evidência de deriva. Se a lógica de marca está embutida nos componentes, uma renovação de marca vira uma reescrita de código em vez de uma mudança de configuração, que é exatamente a catástrofe que a tokenização existe para prevenir.

2. **Como medimos e defendemos a paridade design-código, e que ferramentas pegam a deriva automaticamente?** Um sistema de design que existe apenas como arquivo de design é uma folha de adesivos: os engenheiros reconstroem tudo de qualquer modo e a UI entregue lentamente diverge da intenção. Combinem uma métrica explícita de paridade (a parcela da UI construída com componentes do sistema versus código pontual) e liguem o teste de regressão visual ao CI para que as telas renderizadas sejam comparadas com bases aprovadas. Isso importa em escala corporativa e governamental porque centenas de aplicações, muitas construídas por fornecedores ou herdadas de fusões, precisam todas parecer uma só organização. Levem o número atual de paridade e uma lista dos principais componentes sob medida que as equipes continuam reconstruindo. Se ninguém é dono da métrica nem da suíte de regressão, a deriva já está vencendo em silêncio.

3. **Como governamos a contribuição, a descontinuação e a migração para que o sistema não gere gargalo nas equipes nem se fragmente?** O controle central estrito garante coerência e acessibilidade mas pode transformar a equipe do sistema de design num gargalo que as equipes contornam. A contribuição aberta mantém o sistema vivo mas arrisca variantes divergentes sem revisão. Decidam o caminho de contribuição: como uma equipe propõe um novo componente, quem o revisa e como ele é promovido. Igualmente, combinem como comunicam as mudanças que quebram, porque descontinuações sem apoio à migração e sem antecedência fazem as equipes consumidoras travar ou criar forks. Levem exemplos de componentes que as equipes construíram fora do sistema e perguntem por que não contribuíram de volta. A resposta costuma revelar se a sua governança é um serviço ou um obstáculo.

4. **Como garantimos que a acessibilidade seja resolvida uma vez dentro dos componentes, e o que impede uma equipe de entregar um componente pontual inacessível?** O argumento mais forte para um sistema de design é que o contraste de cor, os estados de foco, a operação por teclado e a semântica para leitores de tela são resolvidos uma vez e herdados em toda parte, mas essa promessa desmorona no instante em que as equipes fazem à mão seus próprios controles. Para uma grande organização é aqui que mora o maior risco jurídico e de reputação, porque um único formulário de pagamento ou seletor de data inacessível pode bloquear usuários reais e disparar reclamações em todo produto que o copiou. Pesem a imposição central (componentes acessíveis mais um linter ou portão de revisão que rejeita marcação bruta) contra a autonomia das equipes e decidam onde fica a linha rígida. Levem os resultados de uma auditoria de acessibilidade, uma lista de componentes com seu status de conformidade e uma contagem dos controles sob medida que as equipes reconstruíram fora do sistema. Em contextos corporativos e governamentais isso não é gentileza: obrigações como a WCAG, a Section 508 e a EN 301 549 tornam a conformidade uma exigência de contratação e de auditoria, então uma biblioteca de componentes com conformidade documentada é em si um ativo de conformidade.

5. **Quantas marcas, locatários e temas este sistema precisa atender, e arquitetamos a camada de tokens para isso agora em vez de adaptá-la depois?** Os temas são baratos se vocês projetaram para eles e brutais se não, porque uma marca ou locatário nunca previsto força a lógica de marca de volta para dentro dos componentes e desfaz todo o ponto da tokenização. Para uma grande equipe essa decisão molda anos de trabalho: uma plataforma que precisa atender várias marcas, um tema claro e escuro, um modo de alto contraste e marca por locatário precisa de uma camada semântica de tokens limpa o bastante para que um tema seja apenas um conjunto diferente de valores. Equilibrem essa flexibilidade contra a abstração excessiva, já que uma árvore de tokens que ninguém consegue navegar é uma falha em si. Levem o roteiro de marcas e locatários que vocês conseguem prever, a contagem de temas em uso hoje e quaisquer componentes que já vazam lógica específica de marca. Em contextos corporativos e governamentais as fusões, aquisições e reorganizações de agências rotineiramente acrescentam marcas que vocês não planejaram, então arquitetar para várias marcas desde o início é a diferença entre uma mudança de dados e uma reescrita de vários anos.

6. **Como migraremos aplicações legadas e construídas por fornecedores para o sistema, e como a equipe do sistema de design é financiada para sobreviver ao próximo ciclo orçamentário?** Um sistema de design só entrega seu retorno quando produtos reais o adotam, e ainda assim as aplicações mais difíceis de converter são as antigas e as terceirizadas, que mais precisam dele, e a equipe que mantém o sistema costuma ser a primeira a ser cortada quando os orçamentos apertam. Para uma grande organização vocês têm de decidir entre uma migração em big bang e uma incremental e como fazer os fornecedores construírem sobre os seus componentes e não em volta deles. Levem um inventário de aplicações com sua nota atual de paridade, uma estimativa do esforço de migração por aplicação e as alavancas contratuais que vocês têm sobre os fornecedores. Em contextos corporativos e governamentais, escrevam a conformidade com o sistema de design nos termos de contratação para que o novo trabalho de fornecedores caia no sistema por padrão e financiem a equipe mantenedora como infraestrutura compartilhada durável, porque um sistema que perde seus guardiões numa reorganização volta a se fragmentar em um ano.

## Perspectiva por setor

**Startup.** Com dois ou três engenheiros e nenhuma pista de sobra, não construam um sistema governado. Gastem um ou dois dias definindo um pequeno conjunto de tokens semânticos de cor, espaçamento e tipografia, mais uma dúzia de componentes compartilhados, tudo num único arquivo que a equipe inteira referencia. Apoiem-se numa biblioteca primitiva de prateleira para as partes difíceis e não deixem nada fixo no código, para que a primeira renovação de marca de verdade seja uma mudança de token e não uma reescrita.

**Pequena empresa.** Sem designer dedicado e com orçamento apertado, comprem em vez de construir: adotem uma biblioteca de componentes ou kit de UI comprovado e apliquem um tema leve da sua marca. O objetivo é um produto consistente e acessível sem pôr gente numa equipe de sistema de design, então favoreçam um sistema que traga acessibilidade e responsividade de fábrica. Resistam à vontade de fazer um fork dele, porque uma cópia personalizada que vocês não conseguem manter vira um passivo no momento em que o projeto original segue adiante.

**Grande empresa.** O problema é a coerência entre muitas equipes e produtos de longa vida, então tratem o sistema de design como infraestrutura compartilhada governada, com equipe dedicada, versionamento e roteiro. Acompanhem a paridade design-código como métrica real, liguem o teste de regressão visual ao CI e arquitetem a camada de tokens para várias marcas e temas desde o início. Orcem explicitamente o custo de governança e de migração e gerenciem a adoção como portfólio em vez de presumir que as equipes derivarão para o sistema sozinhas.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam toda escolha. A conformidade de acessibilidade com padrões como a WCAG, a Section 508 e a EN 301 549 é uma exigência legal, não uma preferência, então uma biblioteca de componentes com conformidade documentada vira um ativo de conformidade. Favoreçam ou estendam um sistema de design público compartilhado para que os cidadãos encontrem os mesmos padrões entre os serviços, escrevam o uso do sistema de design nos contratos com fornecedores e publiquem abertamente os componentes e as orientações para que as agências e seus fornecedores possam adotá-los e ser cobrados por eles.

## Exemplos

**Startup.** Uma startup de dois engenheiros continuava reconstruindo botões e campos de formulário um pouco diferentes em cada nova tela, e o produto começava a parecer remendado. Em vez de um sistema pesado, eles gastaram dois dias definindo um pequeno conjunto de tokens semânticos de design para cor, espaçamento e tipografia, mais cerca de uma dúzia de componentes compartilhados, tudo num único arquivo que a equipe inteira referenciava. Como nada estava fixo no código, quando a primeira contratação com sensibilidade de design propôs uma paleta mais limpa, a renovação foi uma mudança de token que chegou a todo o aplicativo numa tarde e não uma labuta tela a tela.

**Grande empresa.** Uma empresa global de software com dezenas de equipes de produto construiu um sistema de design tokenizado com uma biblioteca compartilhada de componentes em código. Os tokens semânticos permitiram entregar uma renovação completa de marca em todos os produtos em semanas, em vez de uma labuta de vários anos por equipe, porque a mudança era um novo conjunto de tokens e não milhares de edições de cores fixas no código. A paridade design-código, acompanhada como métrica de painel, subiu à medida que as equipes substituíam componentes sob medida, o que cortou a manutenção duplicada de UI.

**Governo.** Um governo nacional criou um sistema de design comum para os serviços públicos (componentes, padrões e acessibilidade embutida compartilhados), obrigatório entre as agências. Um cidadão que se move entre um serviço de impostos, um de saúde e um de licenciamento encontra o mesmo cabeçalho, os mesmos controles de formulário e os mesmos padrões de erro, o que constrói confiança e encurta a curva de aprendizado. As agências e seus fornecedores entregam mais depressa e com mais acessibilidade porque os problemas difíceis são resolvidos de forma central, e o governo pode atualizar orientações ou correções de acessibilidade uma vez e vê-las se propagarem por toda parte.

## Justificativa de negócio: motivações, ROI e TCO

O ROI de um sistema de design vem de remover a duplicação e acelerar a entrega. Em vez de cada equipe projetar e construir os mesmos componentes, elas compõem a partir de uma biblioteca compartilhada, o que acelera mensuravelmente a entrega e libera designers e engenheiros para o trabalho específico do produto. A acessibilidade e a responsividade, resolvidas uma vez nos componentes, poupam o custo de remediação por projeto. As renovações de marca e os temas que levavam anos agora levam semanas.

No TCO, o custo de adoção é uma equipe dedicada, ferramentas e o esforço para os produtos existentes migrarem para o sistema. O custo de não adotar é pago continuamente: construção e manutenção duplicadas entre as equipes, UIs inconsistentes e inacessíveis que criam risco de suporte e jurídico e renovações de marca lentas e caras. Como a duplicação se espalha pelos orçamentos de muitas equipes, é fácil de ignorar: um sistema de design torna visível esse custo oculto e o captura num só lugar.

Para defender o caso junto à liderança, quantifiquem o trabalho duplicado de componentes entre as equipes, o ganho de tempo de lançamento pela composição e o custo e a duração da última renovação de marca versus o que um sistema tokenizado permitiria. Enquadrem o sistema como infraestrutura compartilhada com uma métrica mensurável de adoção (porcentagem de paridade), para que o valor dele possa ser acompanhado ao longo do tempo e não apenas afirmado.

## Antipadrões e armadilhas

- **Sistema de design como folha de adesivos**: um arquivo de design estático, sem componentes em código, de modo que os engenheiros reconstroem tudo de qualquer modo.
- **Valores fixos em toda parte**: cores e espaçamentos espalhados pelo código, tornando impossíveis os temas e as renovações de marca.
- **Sem governança**: o sistema se fragmenta à medida que as equipes acrescentam variantes divergentes e a consistência se erode.
- **Governança sem contribuição**: a equipe central vira um gargalo e as equipes a contornam.
- **Ignorar a paridade**: a UI em código se afasta da intenção do design e ninguém mede a lacuna.
- **Abstração excessiva**: tantos tokens e camadas que ninguém consegue achar ou usar o certo.
- **Lógica de marca embutida nos componentes**: faz do multimarca e dos temas uma reescrita de código e não uma mudança de configuração.
- **Mudanças que quebram sem apoio à migração**: as equipes consumidoras travam ou criam forks do sistema.

## Modelo de maturidade

**Nível 1: Iniciar.** Cada equipe constrói sua própria UI de forma ad hoc e reativa. Sem componentes compartilhados, aparência e comportamento inconsistentes, cores e espaçamentos fixos no código por tela. Toda renovação de marca é uma labuta manual, tela a tela.

**Nível 2: Desenvolver.** Existe um guia de estilo ou biblioteca de componentes compartilhada, mas parcial, opcional e muitas vezes fora de sincronia entre design e código. Algumas equipes a usam, outras não, e as práticas básicas variam muito de equipe para equipe.

**Nível 3: Padronizar.** Um sistema de design tokenizado, com biblioteca em código mantida, documentação e governança, é documentado e imposto em toda a organização. Os componentes consomem tokens semânticos, os temas são suportados e a acessibilidade e a responsividade são embutidas e não parafusadas por tela.

**Nível 4: Gerenciar.** O sistema é medido e controlado com dados em relação a linhas de base. A paridade design-código é acompanhada como métrica explícita, com metas por produto, o teste de regressão visual roda no CI para pegar a deriva e a conformidade de acessibilidade é medida contra padrões e não presumida. Painéis de adoção mostram a cobertura de componentes por equipe, e o custo e a duração das renovações de marca são registrados para que a melhoria seja visível ao longo do tempo.

**Nível 5: Orquestrar.** O sistema de design é um produto em melhoria contínua, integrado em toda a organização e adaptativo à mudança. Tem versionamento, roteiro e um modelo de contribuição que funciona, de modo que evolui com as necessidades reais. As renovações de marca e os novos temas são mudanças rotineiras de tokens, os temas multimarca e multilocatário são normais e a equipe aposenta, redimensiona e promove padrões com base em evidências de dados de uso, alimentando as ferramentas de design e os pipelines de entrega a partir de uma fonte única de verdade.

## Ideias para discussão

- Como vocês equilibram a governança central contra a autonomia das equipes sem fragmentar nem gerar gargalo?
- Qual é a métrica certa para a “paridade design-código”, e como vocês a mantêm honesta?
- Quando uma equipe deve poder construir um componente pontual em vez de usar o sistema?
- Como vocês financiam e dotam de pessoal um sistema de design para que sobreviva a ciclos orçamentários e reorganizações?
- Quanta flexibilidade de temas vale o custo adicional de abstração?
- Como vocês migram aplicações legadas e construídas por fornecedores para um sistema compartilhado?

## Principais conclusões

- Um sistema de design transforma decisões de design pontuais em capital reutilizável e governado.
- Estruturem-no em camadas (tokens, componentes, padrões), com os componentes consumindo tokens semânticos.
- Embutam a acessibilidade e a responsividade nos componentes para que toda equipe as herde.
- Tratem a paridade design-código como uma métrica mensurável de saúde, não uma suposição.
- A tokenização faz das renovações de marca e dos temas multimarca uma mudança de dados e não uma reescrita.
- Governem o sistema como um produto, com roteiro, versionamento e um modelo de contribuição.
- Em escala corporativa e governamental, um sistema compartilhado é o investimento de UI de maior alavancagem disponível.

## Referências e leitura complementar

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, writings on design tokens and design system governance
- W3C Design Tokens Community Group, format specification
- Government design systems (e.g., UK Government Design System, U.S. Web Design System) as reference implementations
