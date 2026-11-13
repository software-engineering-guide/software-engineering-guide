# 5.4 Design de conteúdo e comunicação

## Visão geral e motivação

O design de conteúdo e comunicação é o trabalho de dar forma às palavras, mensagens e informações que um produto usa para ajudar as pessoas a agir. Ele cobre a [estratégia de conteúdo](https://en.wikipedia.org/wiki/Content_strategy) (que conteúdo deve existir, para quem e por quê), a escrita de UX e a microcópia (os rótulos, botões, dicas e mensagens de erro dentro de uma interface) e as comunicações que chegam aos usuários por e-mail, notificações e outros canais. As palavras são interface. Para a maioria dos softwares, o conteúdo é a experiência do produto muito mais do que os visuais.

Para grandes equipes, o conteúdo é um problema de coordenação e de confiança. Quando muitas equipes escrevem de forma independente, a terminologia se afasta, o tom oscila do amigável ao burocrático de tela em tela e o mesmo conceito ganha três nomes diferentes. Os usuários perdem o fio e perdem a confiança. Uma estratégia de conteúdo compartilhada resolve isso. Um guia de voz e tom, um vocabulário controlado e padrões reutilizáveis para erros e estados vazios fazem pelas palavras o que um sistema de design faz pelos pixels: permitem a equipes independentes produzir um todo coerente e digno de confiança.

Em empresas e governo, o conteúdo claro costuma ser uma exigência legal e ética, não uma questão de estilo. As leis de [linguagem simples](https://en.wikipedia.org/wiki/Plain_language) exigem que as comunicações públicas sejam compreensíveis pelas pessoas que precisam agir com base nelas. Um conteúdo mal redigido num formulário de benefícios, numa instrução médica ou num aviso de segurança pode causar dano real: um prazo perdido, uma dose errada, uma vítima de fraude. E numa era de [“padrões obscuros”](https://en.wikipedia.org/wiki/Dark_pattern) manipuladores (designs de interface que enganam ou pressionam as pessoas a escolhas contra o próprio interesse), o modo como um produto apresenta as escolhas é uma questão de confiança, de segurança e cada vez mais de regulação.

## Princípios fundamentais

- As palavras são UI. O conteúdo é parte central da experiência, não enchimento acrescentado depois.
- Escrevam para o objetivo e o contexto do leitor, em linguagem simples, no momento em que ele precisa.
- Clareza acima de esperteza. Um usuário confuso não se encanta com uma mensagem de erro espirituosa.
- A consistência de terminologia e de tom reduz a carga cognitiva e constrói confiança.
- Bons padrões e estados vazios úteis guiam as pessoas ao sucesso.
- Honestidade por design: nunca enganem, pressionem nem envergonhem os usuários para que façam escolhas.
- O conteúdo deve ser estruturado e reutilizável, não fixo no código e duplicado.
- Projetem as comunicações para toda a jornada multicanal, respeitando a atenção.

## Recomendações

### Estabeleça uma estratégia de conteúdo e uma voz

Comecem decidindo para quem é o conteúdo, que trabalhos ele ajuda a fazer e como deve soar. Escrevam um guia de voz e tom com exemplos concretos e um glossário de terminologia ([vocabulário controlado](https://en.wikipedia.org/wiki/Controlled_vocabulary)) para que a mesma coisa seja sempre chamada da mesma maneira. Deixem o tom seguir o contexto: tranquilizador num erro, calmo num aviso de segurança, comemorativo num sucesso. A voz permanece constante. O tom flexiona. Tratem o conteúdo como um ativo gerenciado, com donos, revisão e ciclo de vida, e não como texto digitado num campo na última hora.

### Escreva microcópia que ajude as pessoas a agir

Rotulem os botões com a ação que executam (“Enviar pedido”, não “OK”). Escrevam dicas e textos de ajuda que evitem os erros antes de acontecerem. Ponham no começo as palavras importantes, para que as pessoas que passam o olho pela tela ainda entendam o ponto. Usem a segunda pessoa e a voz ativa. Mantenham as frases curtas e específicas. Cada trecho de microcópia deve reduzir a incerteza sobre o que acontecerá e o que fazer em seguida.

### Faça da linguagem simples o padrão e cumpra as exigências legais

Escrevam num [nível de leitura](https://en.wikipedia.org/wiki/Readability) que sirva a todo o público, e não aos autores. Preferam palavras comuns, frases curtas e instruções concretas. Expandam o jargão e as siglas no primeiro uso ou evitem-nos. No setor público, a linguagem simples costuma ser exigida por lei e por política: sigam os padrões aplicáveis de linguagem simples e testem a compreensão com usuários reais, inclusive pessoas com menor letramento e falantes não nativos. Linguagem simples não é “emburrecer”. Leitores especialistas também preferem um texto claro e eficiente.

### Projete deliberadamente mensagens de erro, estados vazios e padrões

Uma mensagem de erro deve dizer o que deu errado, por quê e como corrigir, em linguagem simples, sem culpar e sem códigos em que o usuário não consegue agir. Guardem o que o usuário digitou e ponham a mensagem bem onde está o problema. Os estados vazios são uma oportunidade de integração: expliquem o que pertence ali e como acrescentar, em vez de mostrar um vazio em branco. Escolham padrões úteis e seguros para que a maioria dos usuários tenha sucesso sem mudar nada e façam do padrão a opção que serve ao interesse do usuário, e não apenas ao do negócio.

### Projete para a confiança e a segurança. Evite padrões obscuros

Apresentem as escolhas com honestidade e simetria: cancelar a assinatura deve ser tão fácil quanto assinar, e recusar deve ser tão proeminente quanto aceitar. Não usem o confirmshaming (“Não, obrigado, eu não gosto de economizar”), o consentimento pré-marcado, os custos escondidos, a urgência falsa nem os fluxos de motel de baratas, fáceis de entrar e difíceis de sair. Além da ética, muitos desses padrões agora são ilegais sob a lei de defesa do consumidor e de privacidade. Tenham cuidado especial com as comunicações sobre segurança, privacidade e dinheiro, porque é onde a manipulação faz mais dano e onde os golpistas imitam mensagens legítimas.

### Projete comunicações multicanal de forma coerente

E-mail, notificações push, SMS e mensagens no aplicativo fazem parte de uma só jornada. Coordenem-nos para que os usuários não sejam bombardeados nem contraditos entre canais. Respeitem a atenção: notifiquem apenas quando for oportuno e útil, deixem os usuários controlarem a frequência e o canal e tornem toda mensagem acessível e simples. Garantam que as comunicações transacionais (recibos, alertas, prazos) sejam confiáveis, claras e difíceis de confundir com [phishing](https://en.wikipedia.org/wiki/Phishing): uma identidade de remetente e uma formatação consistentes ajudam os usuários a confiar nas mensagens genuínas.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Estratégia de conteúdo centralizada | Consistência, confiança, reutilização | Custo adicional, pode desacelerar as equipes se virar gargalo |
| Linguagem simples em toda parte | Compreensão, inclusão, conformidade legal | Esforço de reescrever. Especialistas podem resistir a perder o jargão |
| Voz lúdica e de marca | Personalidade, memorabilidade | Pode falhar em erros, situações de alto risco ou públicos diversos |
| Padrões fortes | A maioria dos usuários tem sucesso sem esforço | Risco de indução. Precisam ser definidos no interesse do usuário |
| Mensagens multicanal ricas | Oportunas, envolventes | Viram ruído com facilidade. Ônus de privacidade e de consentimento |

A tensão central é entre a personalidade da marca e a clareza, e entre o engajamento e o respeito pela atenção. O contexto resolve. Deixem a voz acrescentar calor onde as apostas são baixas e priorizem uma clareza simples e calma onde as apostas são altas (erros, dinheiro, segurança, jurídico). Quanto a padrões e mensagens, a linha ética é simples: o design serve ao interesse genuíno do usuário ou explora a sua desatenção?

## Perguntas para discutir com sua equipe

1. **As mensagens de erro, os estados vazios e os padrões são padrões compartilhados no nosso sistema de design, ou reinventados em cada tela?** Estes são os momentos de maior alavancagem de toda a experiência: um bom erro diz o que deu errado, por quê e como corrigir sem culpa nem código inatingível, e um bom estado vazio ensina às pessoas o que pertence ali em vez de mostrar um vazio. Quando cada equipe os escreve do zero, vocês têm “Erro 500” num lugar e uma mensagem útil em outro, e os usuários perdem a confiança. Decidam se esses padrões vivem no sistema de design ao lado dos componentes, com estruturas acordadas e textos de exemplo. Levem três mensagens de erro reais e três estados vazios do seu produto e leiam-nos em voz alta. Se algum culpa o usuário ou não oferece caminho de recuperação, vocês acharam o primeiro item do backlog.

2. **O nosso conteúdo é estruturado e reutilizável, ou fixo no código e duplicado entre as telas?** Um texto digitado direto num componente não pode ser atualizado de forma consistente, não pode ser revisado e não pode ser localizado sem uma mudança de código, o que bloqueia em silêncio todo mercado futuro e toda correção de redação. Isso se torna agudo em escala, onde o mesmo conceito ganha três nomes porque não há glossário nem fonte única. Decidam como o conteúdo é guardado, quem é dono do vocabulário controlado e como uma mudança de redação se propaga sem uma implantação por tela. Levem um exemplo de um termo que o seu produto grafa ou nomeia de forma inconsistente e rastreiem em quantos lugares vocês teriam de editar. Se a resposta é “buscar e substituir à mão”, o seu conteúdo está preso no código.

3. **Quando os designers de conteúdo entram no fluxo de trabalho, e quem tem autoridade para bloquear um fluxo manipulativo?** Se o conteúdo é uma reflexão tardia (lorem ipsum até o lançamento, depois o que couber na caixa), as palavras que carregam a maior parte da experiência recebem o menor cuidado, e os padrões obscuros entram sob pressão de crescimento porque ninguém é dono da honestidade. Combinem que o conteúdo é uma entrada de design desde o início, com um guia de voz e tom e revisão no fluxo de trabalho, e nomeiem quem pode barrar um fluxo de confirmshaming ou de consentimento pré-marcado antes de ele ser entregue. Agora isso é uma questão jurídica além de ética, porque a lei de defesa do consumidor e de privacidade proíbe cada vez mais esses padrões. Levem um fluxo recente e perguntem se recusar é tão fácil e tão proeminente quanto aceitar. Se não é, decidam hoje quem é responsável por corrigir.

4. **Em que nível de leitura estamos de fato escrevendo, e como sabemos que os usuários reais entendem o nosso conteúdo de maior risco?** A linguagem simples é fácil de alegar e difícil de provar: os autores escrevem no seu próprio nível de compreensão, e os leitores que mais precisam de clareza, pessoas com menor letramento e falantes não nativos, são os menos representados na sala. Para uma grande organização as apostas se compõem, porque uma única carta de benefícios confusa ou um aviso de segurança é copiado para milhões de destinatários antes de alguém medir se ele funciona. Decidam um nível-alvo de leitura para todo o seu público, expandam ou banam o jargão no primeiro uso e comprometam-se com testes de compreensão com pessoas reais em vez de confiar apenas num índice de legibilidade. Levem as suas três comunicações de maior tráfego e a evidência de que alguém de fora da equipe de autoria consegue agir sobre elas corretamente. Em contextos corporativos e governamentais, acrescentem a lei ou política de linguagem simples aplicável e sejam honestos sobre quais documentos reprovariam numa auditoria hoje.

5. **Quem governa como, quando e com que frequência mandamos mensagens aos usuários por e-mail, push, SMS e no aplicativo, para que toda a jornada permaneça coerente?** Quando cada equipe é dona do seu canal, os usuários são bombardeados, contraditos e eventualmente treinados a ignorar ou cancelar tudo, inclusive as mensagens transacionais que realmente importam. Coordenar a jornada significa combinar limites de frequência, dar aos usuários controle real sobre canal e consentimento e manter uma identidade de remetente consistente para que as mensagens genuínas sejam difíceis de confundir com o phishing que as imita. Levem um registro de todas as mensagens que um único usuário poderia receber numa semana movimentada e contem as duplicadas, as contraditórias e as que poderiam ser confundidas com um golpe. A atração concorrente é a pressão por engajamento, já que as equipes de crescimento sempre querem mais um ponto de contato e o respeito pela atenção não tem métrica imediata. Em contextos corporativos e governamentais, acrescentem as obrigações de consentimento e de privacidade que transformam a mensagem não solicitada em exposição jurídica e nomeiem quem pode vetar uma campanha que abusa do canal.

6. **Como medimos se o nosso conteúdo está funcionando, e onde a voz da marca cede por inteiro à clareza simples?** O conteúdo que nunca é medido deriva por gosto, e a parte interessada mais barulhenta ganha a redação em vez do usuário. Liguem o conteúdo a sinais reais, categorias de chamados de suporte, funis de conclusão e de conversão, taxas de erro e de recurso e taxas de cancelamento de inscrição e de reclamação, para que uma reescrita seja julgada pelo resultado e não pela preferência. Ao mesmo tempo, combinem onde a voz deve ceder: um erro espirituoso, uma mensagem sobre dinheiro em tom de piada ou um aviso de segurança lúdico corrói a confiança exatamente quando as apostas são mais altas. Levem um fluxo de alto tráfego, a métrica que ele move e uma proposta de linha entre onde a personalidade ajuda e onde a clareza calma é obrigatória. Para uma organização grande ou pública, nomeiem quem é dono dessa linha e como uma melhoria comprovada se propaga entre as equipes, em vez de ganhar uma tela e perder o resto.

## Perspectiva por setor

**Startup.** Sem redator e com dois engenheiros, tratem o conteúdo como tarefa de fundador e não como contratação. Gastem um dia nas palavras de maior alavancagem: nomeiem os botões pela ação, transformem o painel vazio num tutorial de primeiro uso e façam os erros dizerem o que corrigir. Escrevam um guia de voz de uma página para que o tom continue simples à medida que vocês crescem e pulem o glossário e a plataforma de conteúdo até a inconsistência realmente doer.

**Pequena empresa.** Sem designer de conteúdo e com orçamento apertado, apoiem-se nas convenções de linguagem simples e de microcópia embutidas nas ferramentas que vocês já usam e comprem modelos de e-mail transacional em vez de criá-los do zero. Priorizem as poucas telas que perdem clientes, um estado vazio, um erro de checkout, um fluxo de cancelamento, e mantenham recusar tão fácil quanto aceitar para ficar longe da lei de padrões obscuros. Rodem um verificador gratuito de legibilidade em tudo que é voltado ao cliente antes de ser entregue.

**Grande empresa.** O problema é a coerência entre muitas equipes: um guia compartilhado de voz e tom, um vocabulário controlado para que um conceito mantenha um nome e padrões de erro, de estado vazio e de padrão que vivam no sistema de design ao lado dos componentes. Guardem o conteúdo em controle de versões, estruturado e localizável em vez de fixo no código, deem a ele donos e revisão e coordenem as mensagens multicanal para que os usuários não sejam bombardeados nem contraditos. Governem a honestidade de forma central para que nenhuma equipe entregue confirmshaming ou consentimento pré-marcado sob pressão de crescimento.

**Governo.** A linguagem simples costuma ser um dever legal e não uma preferência, então sigam os padrões aplicáveis e testem a compreensão com destinatários reais, inclusive pessoas com menor letramento e falantes não nativos. Abram cada aviso com a ação e o prazo, tirem o jargão e façam cada comunicação identificar claramente o remetente para que as pessoas não a confundam com um golpe. Mantenham as escolhas honestas e simétricas, publiquem os padrões de conteúdo a que se submetem e deem às pessoas um caminho simples para questionar uma decisão que não entendem.

## Exemplos

**Startup.** Uma pequena startup sem redatores notou que a maioria dos usuários do período de teste se cadastrava, via um painel vazio e nunca mais voltava. Um fundador gastou um dia reescrevendo a microcópia: o estado vazio agora explicava o que acrescentar e oferecia um projeto de exemplo com um clique, os botões nomeavam a ação em vez de dizer “OK” e as mensagens de erro diziam o que deu errado e como corrigir. A ativação subiu de forma perceptível na semana seguinte, e o mesmo fundador escreveu um guia de voz de uma página para que toda a equipe mantivesse o tom simples e consistente à medida que crescia.

**Grande empresa.** Uma empresa de SaaS reescreveu sua integração, suas mensagens de erro e seus estados vazios em torno de uma microcópia clara e orientada à ação e de um guia de voz documentado. Os chamados de suporte do tipo “como eu...” caíram, a ativação melhorou porque os estados vazios agora ensinavam os usuários o que fazer e a conversão de período de teste em pago subiu. A empresa também removeu um fluxo de cancelamento com confirmshaming depois que ele danificou a confiança e atraiu críticas, substituindo-o por um caminho de cancelamento direto e simétrico que, de forma contraintuitiva, melhorou a reputação e a reconquista de clientes.

**Governo.** Uma agência reescreveu uma carta de elegibilidade a benefícios que os destinatários rotineiramente liam mal, causando consultas perdidas e perda indevida de benefícios. Aplicando padrões de linguagem simples, a equipe abriu com a ação exigida e o prazo, removeu o jargão jurídico e testou a compreensão com destinatários reais, inclusive falantes não nativos. A compreensão subiu muito e as taxas de prazos perdidos caíram, reduzindo recursos e atendimentos. Como a carta agora identificava claramente a si mesma e ao remetente, os destinatários também ficaram menos propensos a confundi-la com um golpe.

## Justificativa de negócio: motivações, ROI e TCO

A qualidade do conteúdo conduz resultados mensuráveis: maior conclusão de tarefas e conversão, menor volume de suporte, menos erros e recursos e maior confiança e retenção. A microcópia clara e os padrões úteis reduzem o número de pessoas que travam e contatam o suporte ou abandonam. As comunicações em linguagem simples reduzem o custo a jusante: menos ligações confusas, menos erros a corrigir, menos recursos em contextos governamentais. Um design confiável e não manipulador protege a reputação e reduz a exposição jurídica à medida que a regulação de padrões obscuros se aperta.

No TCO, o custo de adoção é modesto: designers de conteúdo ou redatores treinados, um guia de voz e glossário e revisão no fluxo de trabalho. O custo de não adotar é difuso e grande: carga de suporte e de central de atendimento, transações abandonadas, correção de erros, recursos, multas regulatórias por padrões manipuladores ou comunicações não conformes e confiança erodida. Esses custos caem em suporte e operações e não no orçamento do produto, então a liderança tende a subestimá-los.

Para defender o caso, liguem o trabalho de conteúdo às categorias de chamados de suporte, aos funis de conclusão e de conversão, às taxas de erro e de recurso e às taxas de cancelamento de inscrição ou de reclamação. Uma pequena reescrita de um fluxo de alto tráfego ou de uma comunicação de alto volume costuma produzir uma melhoria clara e atribuível, e isso é o que justifica escalar a prática.

## Antipadrões e armadilhas

- **Conteúdo como reflexão tardia**: lorem ipsum até o lançamento, depois o que couber na caixa.
- **Jargão e linguagem interna**: escrever da perspectiva da organização e não do usuário.
- **Erros que culpam e não ajudam**: “Erro 500” ou “Entrada inválida” sem caminho de recuperação.
- **Estados vazios em branco**: um vazio onde deveria haver orientação.
- **Padrões obscuros**: confirmshaming, consentimento pré-marcado, custos escondidos, motéis de baratas, urgência falsa.
- **Terminologia inconsistente**: três nomes para um conceito no produto.
- **Spam de notificações**: excesso de mensagens que treina os usuários a ignorar ou cancelar.
- **Legibilidade sem teste**: presumir que o conteúdo é claro sem testar com usuários reais.
- **Texto fixo no código e duplicado**: impossível de atualizar ou localizar de forma consistente.

## Modelo de maturidade

**Nível 1: Iniciar.** Nenhuma prática de conteúdo. As palavras são escritas ad hoc por quem constrói a tela, reagindo ao que a caixa pede no momento. A terminologia e o tom são inconsistentes, os erros culpam o usuário ou mostram códigos inatingíveis e os estados vazios são um vazio em branco.

**Nível 2: Desenvolver.** Pode existir um guia de estilo ou algumas notas de voz, e algumas equipes pegaram hábitos de linguagem simples. O conteúdo ainda é uma atividade de fase final, por equipe, com pouca reutilização e pouco teste, de modo que a qualidade e a consistência variam muito de um esquadrão para outro.

**Nível 3: Padronizar.** Uma estratégia de conteúdo, um guia de voz e tom e um vocabulário controlado são documentados e usados entre as equipes. A linguagem simples é o padrão e, onde exigido, conforme. Erros, estados vazios e padrões seguem padrões compartilhados. O conteúdo é estruturado, revisado e reutilizável em vez de fixo no código por tela.

**Nível 4: Gerenciar.** O conteúdo é medido contra resultados com dados. Os resultados de legibilidade e de testes de compreensão, as categorias de chamados de suporte, os funis de conclusão e de conversão, as taxas de erro e de recurso e as taxas de cancelamento de inscrição e de reclamação são acompanhados contra linhas de base, e cada mudança de conteúdo é julgada por mover ou não esses números. Os padrões obscuros são auditados contra uma política documentada, e a frequência das mensagens multicanal é monitorada contra limites acordados.

**Nível 5: Orquestrar.** O conteúdo é continuamente melhorado e integrado em toda a organização. Os padrões vivem no sistema de design, localizados e acessíveis por padrão. O vocabulário controlado mantém um nome por conceito em toda parte. As comunicações multicanal são coordenadas e controladas pelo usuário. E a prática se adapta à medida que a regulação, o público e os canais mudam, aposentando e reescrevendo conteúdo com base em evidências e não em opinião.

## Ideias para discussão

- Onde a voz da marca deve ceder por inteiro à clareza simples, e quem decide a linha?
- Como vocês impõem uma política de não usar padrões obscuros quando as equipes de crescimento estão pressionadas por métricas?
- Como vocês mantêm a terminologia consistente entre muitas equipes sem gerar gargalo?
- Que nível de leitura é o certo para um serviço usado pelo público inteiro?
- Como a frequência das notificações e o controle de canais devem ser governados na organização?
- Como vocês tornam as comunicações genuínas distinguíveis do phishing que as imita?

## Principais conclusões

- O conteúdo é UI central. Projetem as palavras com o mesmo rigor dos visuais.
- A linguagem simples melhora a compreensão para todos e muitas vezes é exigida por lei.
- Erros, estados vazios e padrões são momentos de alta alavancagem: projetem-nos para ajudar.
- Evitem padrões obscuros: apresentem as escolhas com honestidade e simetria. São cada vez mais ilegais.
- A terminologia e o tom consistentes constroem confiança e reduzem a carga cognitiva.
- Coordenem as comunicações multicanal e respeitem a atenção e o controle do usuário.
- A qualidade do conteúdo aparece diretamente no volume de suporte, na conclusão, nos erros e na confiança.

## Referências e leitura complementar

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson and Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton and Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (dark patterns research)
- U.S. Federal Plain Language Guidelines and PlainLanguage.gov
- UK Government Digital Service, content design and style guidance
- Nielsen Norman Group, articles on error messages, microcopy, and readability
