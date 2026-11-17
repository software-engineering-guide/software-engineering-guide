# 5.7 Desenvolvimento de aplicativos móveis

## Visão geral e motivação

O [desenvolvimento de aplicativos móveis](https://en.wikipedia.org/wiki/Mobile_app_development) é a disciplina de construir software para celulares e tablets. Para muitas pessoas, o celular é hoje o computador principal ou o único que possuem. Isso faz do aplicativo móvel a porta da frente do seu serviço e, muitas vezes, a superfície em que os usuários julgam a sua organização inteira.

O móvel é um ambiente de engenharia distinto, não uma versão pequena da web ou do desktop. O dispositivo roda no bolso, com bateria, sobre conexões que vão e vêm. As telas são pequenas. O sistema operacional controla o que o seu aplicativo pode fazer. Existem duas plataformas dominantes ([iOS](https://en.wikipedia.org/wiki/IOS), da Apple, e [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29), do Google), cada uma com suas próprias linguagens, regras de design e loja. Vocês não podem simplesmente entregar uma atualização quando quiserem, porque uma loja a revisa antes e os usuários escolhem quando instalá-la. Este capítulo se apoia na engenharia de front-end (capítulo 5.6), nos fundamentos de UX (capítulo 5.1) e na acessibilidade (capítulo 5.3) e depende da segurança de aplicações (capítulo 4.2) e do CI/CD e da entrega (capítulo 8.1).

A relevância para empresas e governo é alta. As empresas entregam aplicativos para clientes e aplicativos internos para a própria força de trabalho, muitas vezes gerenciados por [gerenciamento de dispositivos móveis](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: software central que configura e protege dispositivos da empresa). Os governos constroem aplicativos voltados ao cidadão para benefícios, saúde, identidade e pagamentos e precisam atender a todos, inclusive pessoas em dispositivos antigos e conexões lentas, sob leis de acessibilidade. Nos dois contextos, o móvel é um compromisso sério e de longa vida, então tratem-no com o mesmo rigor que dão a qualquer outro sistema de produção.

## Princípios fundamentais

- Projetem para o dispositivo: tela pequena, bateria e uma rede que vai e vem.
- Presumam conectividade intermitente. Funcionem primeiro offline e sincronizem quando puderem.
- Respeitem as convenções de design e de interação de cada plataforma.
- Vocês não controlam o momento do lançamento. A loja e o usuário controlam.
- A fragmentação é normal. Suportem uma faixa real de dispositivos e versões do SO.
- Guardem os dados com segurança no dispositivo, porque os dispositivos se perdem e são roubados.
- A acessibilidade é uma exigência, não um acabamento.
- Escolham a abordagem de construção para a vida inteira do aplicativo, não apenas para o dia do lançamento.

## Recomendações

### Escolha a abordagem de construção deliberadamente

Há três abordagens amplas, e cada uma serve a necessidades diferentes.

O [desenvolvimento nativo](https://en.wikipedia.org/wiki/Mobile_app_development) significa escrever separadamente para cada plataforma usando suas próprias ferramentas: Swift para iOS, Kotlin para Android. Vocês obtêm o melhor desempenho, o acesso mais pleno aos recursos do dispositivo e a sensação de plataforma mais fiel, ao custo de construir e manter duas bases de código.

Os [frameworks multiplataforma](https://en.wikipedia.org/wiki/Cross-platform_software) permitem que uma base de código mire as duas plataformas. O [React Native](https://en.wikipedia.org/wiki/React_Native) usa JavaScript e renderiza componentes nativos de verdade. O [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) usa a linguagem Dart e desenha seus próprios widgets. Eles reduzem o esforço duplicado e podem acelerar a entrega, mas acrescentam uma dependência da saúde do framework e podem ficar atrás dos recursos mais novos da plataforma.

Um [aplicativo web progressivo](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: um site que pode ser instalado e funcionar offline) não precisa de loja e atualiza instantaneamente, mas tem acesso limitado a alguns recursos do dispositivo e uma presença mais fraca na tela inicial.

Escolham com base nos recursos de dispositivo exigidos, no perfil de desempenho, no horizonte de manutenção, nas habilidades que vocês conseguem contratar e no alcance de que precisam. Um aplicativo de consumo de alto desempenho pode justificar o nativo. Um aplicativo de conteúdo e formulários com uma equipe pequena pode se ajustar bem a um multiplataforma ou a um PWA.

### Siga as diretrizes de design da plataforma

Cada plataforma tem convenções publicadas e detalhadas. A Apple oferece as [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines) e o Google oferece o [Material Design](https://en.wikipedia.org/wiki/Material_Design). Elas cobrem navegação, gestos, tipografia, espaçamento e comportamentos do sistema. Segui-las faz o aplicativo parecer familiar, o que reduz o esforço que os usuários gastam aprendendo-o. Lutar contra elas faz um aplicativo parecer estranho e desajeitado. Uma base de código multiplataforma ainda precisa honrar as convenções de cada plataforma onde elas diferem, em vez de forçar o visual de uma plataforma sobre a outra.

### Projete para as restrições do móvel

Construam offline-first: deixem as tarefas centrais funcionarem sem conexão, guardem as mudanças localmente e sincronizem quando a rede voltar. Tratem os conflitos com cuidado quando o mesmo dado muda em dois lugares. Sejam frugais com a bateria e os dados: agrupem chamadas de rede, evitem localização constante ou trabalho em segundo plano, comprimam as cargas e respeitem as configurações de economia de dados do usuário. Planejem a fragmentação, a ampla variação de tamanhos de tela, potência de dispositivo e versões do SO. Escolham uma faixa de suporte com base em dados reais de uso e testem em hardware modesto e não apenas nos modelos topo de linha. Projetem para telas pequenas com hierarquia clara, alvos de toque grandes e conteúdo que se adapta a tamanhos e orientações diferentes.

### Planeje a distribuição, o versionamento e as atualizações

A publicação passa pela [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) e pelo [Google Play](https://en.wikipedia.org/wiki/Google_Play), cada uma com processos de revisão e políticas que podem atrasar ou rejeitar um lançamento. Incluam o tempo de revisão no cronograma e leiam as políticas cedo. Como os usuários escolhem quando atualizar, vocês sempre terão muitas versões em campo ao mesmo tempo. Mantenham o aplicativo retrocompatível com clientes mais antigos e versionem as suas APIs (capítulo 2.3) para que um aplicativo antigo continue funcionando. Ofereçam um jeito de exigir uma atualização quando for preciso, por exemplo um aviso de atualização forçada quando uma versão é insegura ou sem suporte, e usem-no com parcimônia. As empresas também podem distribuir aplicativos internos por MDM ou canais privados em vez das lojas públicas.

### Use notificações push e deep links com cuidado

As [notificações push](https://en.wikipedia.org/wiki/Push_technology) permitem alcançar os usuários quando o aplicativo está fechado. Usem-nas para valor genuíno, respeitem o consentimento do usuário e as permissões da plataforma e evitem ruído, porque as pessoas desativam as notificações de aplicativos que exageram. Os [deep links](https://en.wikipedia.org/wiki/Deep_linking) levam um usuário direto a uma tela específica a partir de um link ou de uma notificação. Configurem-nos para que um link abra o lugar certo no aplicativo e volte à web com elegância quando o aplicativo não está instalado.

### Proteja o aplicativo e seus dados

Tratem o dispositivo como não confiável e possivelmente perdido. Guardem os dados sensíveis no armazenamento seguro da plataforma (o [Keychain do iOS](https://en.wikipedia.org/wiki/Keychain_%28software%29) ou o Keystore do Android), nunca em arquivos simples. Ofereçam [autenticação biométrica](https://en.wikipedia.org/wiki/Biometrics) (digital ou rosto) para desbloquear ações sensíveis, apoiada por uma senha numérica. Considerem a [fixação de certificados](https://en.wikipedia.org/wiki/Public_key_pinning) (conferir que o servidor apresenta um certificado esperado) para conexões de alto valor e planejem a rotação desses certificados. Minimizem o que guardam no dispositivo, protejam os segredos e sigam a orientação mais ampla da segurança de aplicações (capítulo 4.2).

### Construa um pipeline real de testes e de entrega

Testem em dispositivos reais e não apenas em [emuladores](https://en.wikipedia.org/wiki/Emulator) e simuladores, porque hardware, sensores e desempenho diferem. Usem um laboratório de dispositivos ou uma fazenda de dispositivos na nuvem para cobrir uma amostra representativa de modelos e versões do SO. Automatizem builds, testes, assinatura e envio à loja por [integração e entrega contínuas](https://en.wikipedia.org/wiki/CI/CD) (capítulo 8.1), incluindo a distribuição beta a testadores antes do lançamento público. Gerenciar com segurança as chaves de assinatura e as credenciais da loja faz parte desse pipeline.

### Faça da acessibilidade uma exigência

Suportem os recursos de acessibilidade de cada plataforma: leitores de tela ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) no iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) no Android), dimensionamento dinâmico de texto, contraste de cor suficiente e alvos de toque grandes. Rotulem os controles para que a tecnologia assistiva possa descrevê-los. Testem com as ferramentas assistivas reais e não só com verificações automatizadas. Para o governo especialmente, a acessibilidade é um mandato legal, e os detalhes vivem na acessibilidade (capítulo 5.3).

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Nativo (Swift, Kotlin) | Melhor desempenho, acesso pleno ao dispositivo, sensação genuína de plataforma | Duas bases de código, custo maior, mais pessoal |
| React Native | Uma base de código JavaScript, componentes nativos reais, iteração rápida | Dependência de framework, complexidade de ponte, atraso de funcionalidades |
| Flutter | Uma base de código, UI consistente, bom desempenho | Habilidades em Dart menos comuns, aplicativo maior, modelo próprio de widgets |
| Aplicativo web progressivo | Sem loja, atualizações instantâneas, uma base de código web | Recursos de dispositivo limitados, presença mais fraca, limites da plataforma |
| Atualizações forçadas | Removem depressa versões antigas inseguras | Irritam os usuários se usadas em excesso. Podem bloquear o acesso |
| Fixação de certificados | Forte proteção contra interceptação | Quebra se os certificados rotacionam sem atualizações do aplicativo |

A troca recorrente é alcance e velocidade de entrega versus profundidade e fidelidade. O nativo dá a experiência mais rica e fiel mas custa mais para construir e manter. As abordagens multiplataforma e de PWA poupam esforço e ampliam o alcance, com algum custo em sensação de plataforma ou acesso ao dispositivo. Para uma equipe pequena que entrega formulários e conteúdo, compartilhar uma base de código costuma ser sábio. Para um aplicativo de consumo exigente, a profundidade do nativo pode valer o preço. Decidam com a vida inteira do aplicativo em vista e não apenas o lançamento.

## Perguntas para discutir com sua equipe

1. **Por quanto tempo damos suporte a clientes antigos em campo, e a nossa API é versionada para mantê-los funcionando?** Como os usuários escolhem quando atualizar, vocês sempre têm muitas versões do aplicativo instaladas ao mesmo tempo, e uma mudança no backend que presume que todos estão atualizados quebrará a longa cauda de clientes mais antigos. Decidam a sua janela de retrocompatibilidade, versionem as APIs para que um aplicativo antigo continue funcionando e mantenham um caminho de atualização forçada, raramente usado, para versões genuinamente inseguras. Isso importa tanto para aplicativos governamentais de cidadãos quanto para aplicativos corporativos de força de trabalho, onde pessoas em dispositivos antigos não podem ou não querem atualizar no seu cronograma. Levem os dados atuais de distribuição de versões e perguntem o que quebra para o cliente mais antigo ainda em uso real. Se vocês não conhecem essa distribuição, instrumentem-na antes de entregar a próxima mudança que quebra.

2. **Qual é o nosso patamar para enviar uma notificação push, e quem decide o que vale interromper um usuário?** As notificações push alcançam as pessoas quando o aplicativo está fechado, o que as torna poderosas e fáceis de abusar, e os usuários desativam as notificações (ou apagam o aplicativo) de produtos que exageram. Combinem o que conta como valor genuíno, como os usuários controlam frequência e canal e como vocês honram o consentimento da plataforma em vez de ficar importunando por permissão. Sem um patamar compartilhado, toda equipe com uma métrica a atingir recorrerá a um push, e o canal inteiro se degrada em ruído. Levem as notificações enviadas no último mês e perguntem quais o usuário teria agradecido. Se a maioria era promocional, apertem a política antes que a taxa de recusa o faça por vocês.

3. **O nosso pipeline de entrega móvel é real, cobrindo assinatura, uma fazenda de dispositivos e distribuição beta, ou o lançamento é uma correria manual estressante?** O móvel acrescenta riscos que a web não tem: a revisão da loja pode atrasar ou rejeitar um lançamento, as chaves de assinatura e as credenciais da loja precisam ser tratadas com segurança e hardware e sensores diferem o bastante para que os emuladores escondam problemas reais. Automatizar builds, testes, assinatura e envio à loja por CI/CD, com distribuição beta a testadores e uma fazenda de dispositivos na nuvem cobrindo os modelos que os seus usuários de fato carregam, é o que transforma os lançamentos de heroísmo em rotina. Decidam quem é dono do pipeline e das chaves de assinatura e como o tempo de revisão da loja é embutido em todo plano de lançamento. Levem a história do último lançamento e contem os passos manuais. Cada um é um lugar em que um lançamento estressante pode dar errado sob prazo.

4. **Escolhemos nativo, multiplataforma ou aplicativo web progressivo para a vida inteira deste produto, ou apenas para o dia do lançamento?** A abordagem de construção é a maior alavanca isolada sobre o custo e a capacidade de um aplicativo móvel por anos, e uma escolha feita para entregar depressa pode prender vocês: o nativo compra o acesso mais rico ao dispositivo e a sensação de plataforma ao preço de duas bases de código e dois conjuntos de habilidades, enquanto o multiplataforma e o PWA compartilham código mas acrescentam uma dependência de framework ou perdem o acesso a alguns recursos do dispositivo. Para uma grande equipe, essa decisão conduz a contratação, o orçamento de manutenção e a rapidez com que vocês conseguem adotar cada lançamento anual do SO, então merece um dono explícito em vez de um padrão definido por quem escreveu o primeiro protótipo. Levem os recursos de dispositivo exigidos, o perfil de desempenho, o horizonte de manutenção e as habilidades que vocês realmente conseguem contratar e sejam honestos sobre quais recursos de plataforma abririam mão em cada opção. Em contextos corporativos e governamentais, pesem se o aplicativo é um compromisso de longa vida que precisa sobreviver à rotatividade de pessoal e a uma década de mudança de plataforma e registrem a decisão e sua justificativa para que uma equipe futura não fique adivinhando por que a base de código é do jeito que é.

5. **Que faixa de suporte a dispositivos e versões do SO os nossos usuários reais precisam, e estamos testando no hardware que eles de fato carregam e não nos celulares das nossas mesas?** A fragmentação é a condição normal do móvel: os usuários abrangem uma ampla variação de tamanhos de tela, potência de dispositivo e versões do SO, e um aplicativo ajustado nos modelos topo de linha da equipe sairá lento ou quebrado no hardware modesto que boa parte do seu público possui. Definir uma faixa de suporte é uma troca entre alcance e esforço, porque cada modelo e versão do SO mais antigos que vocês prometem suportar alarga a matriz de testes e o ônus de manutenção, então a faixa precisa vir de dados reais de uso e não de suposição. Levem a distribuição de dispositivos e versões do SO, os modelos que uma fazenda de dispositivos na nuvem ou laboratório hoje cobre e o desempenho que vocês mediram em hardware de baixo desempenho, e não só em simuladores. Para aplicativos governamentais de cidadãos isso é quase inegociável, porque vocês precisam atender a todos, inclusive pessoas em dispositivos antigos e conexões lentas, sob obrigações de acessibilidade, e para frotas corporativas vocês devem testar os modelos robustos exatos que a equipe carrega e não uma amostra genérica.

6. **Que dados sensíveis vivem no dispositivo, e cada um está protegido contra um celular perdido, roubado ou nas mãos de outra pessoa?** Um dispositivo móvel viaja no bolso e é perdido ou roubado, então qualquer dado ou segredo guardado em um arquivo simples está a um celular extraviado da exposição, e o raio de impacto cresce com cada usuário. As considerações puxam umas contra as outras: guardar dados em cache no dispositivo é o que faz o offline-first funcionar e mantém o aplicativo rápido, mas cada item em cache é um passivo que precisa ficar no armazenamento seguro da plataforma (o Keychain do iOS ou o Keystore do Android), ser minimizado e, idealmente, ser protegido por biometria ou senha numérica. Levem um inventário do que exatamente o aplicativo persiste localmente, onde cada item é guardado, o que o desbloqueia e se as conexões de alto valor usam fixação de certificados com um plano viável de rotação. Em contextos corporativos, liguem isso à política de gerenciamento de dispositivos móveis e ao apagamento remoto, e em contextos governamentais tratem os dados pessoais no dispositivo como uma exposição de privacidade e jurídica que precisa ser justificada, documentada e defensável em auditoria.

## Perspectiva por setor

**Startup.** Com uma equipe minúscula e pouca pista, vocês raramente podem bancar duas bases de código nativas ou dois conjuntos de habilidades, então um framework multiplataforma, ou até um PWA que alcança as duas lojas a partir de uma base de código, costuma vencer. Entreguem offline-first para a única tarefa central que importa, mantenham qualquer token no armazenamento seguro e não num arquivo simples e incluam o tempo de revisão da loja em cada lançamento para que uma rejeição não estrague uma data de lançamento. Pulem as atualizações forçadas, a fixação de certificados e uma fazenda de dispositivos até o uso real justificá-las.

**Pequena empresa.** Sem especialista móvel dedicado e com orçamento apertado, inclinem-se firmemente para comprar em vez de construir: um construtor de aplicativos sem código, um aplicativo de marca branca do fornecedor do seu ponto de venda ou de reservas, ou um PWA bem feito a partir do site existente muitas vezes vence um aplicativo sob medida que vocês não conseguem manter. Se contratarem um aplicativo, sejam donos das chaves de assinatura e das contas da loja para que um contratado não mantenha a sua presença como refém e insistam em acessibilidade e armazenamento seguro no dispositivo no contrato. Mantenham o escopo nas uma ou duas tarefas que os clientes realmente fazem no celular.

**Grande empresa.** Em escala, o aplicativo é um compromisso de longa vida entre muitas equipes, então padronizem a abordagem de construção, o padrão de armazenamento seguro, o pipeline de CI/CD e a política de versionamento de API em vez de deixar cada produto reinventá-los. Os aplicativos internos de força de trabalho costumam passar por gerenciamento de dispositivos móveis para instalação, configuração, apagamento remoto e política, enquanto os aplicativos de clientes precisam de uma fazenda de dispositivos que cubra o uso real e de acessibilidade e segurança auditadas. Governem as chaves de assinatura, as credenciais da loja e o momento dos lançamentos de forma central para que uma mudança de backend que quebra nunca deixe encalhada a longa cauda de clientes antigos.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam toda escolha. Vocês precisam atender a todos, inclusive pessoas em dispositivos antigos e conexões lentas, então a acessibilidade é um mandato legal verificado com ferramentas assistivas reais e uma ampla faixa de suporte a dispositivos é quase inegociável. Favoreçam abordagens e contratos que evitem o aprisionamento ao fornecedor, mantenham os dados portáveis e deixem o público inspecionar o que o aplicativo faz com seus dados e tratem os dados pessoais no dispositivo como uma exposição que vocês precisam justificar e documentar sob auditoria.

## Exemplos

**Startup.** Uma startup de três pessoas que constrói um aplicativo de acompanhamento de hábitos precisava alcançar iOS e Android mas não podia bancar duas bases de código nativas nem dois conjuntos de habilidades. Escolheram um framework multiplataforma para que uma pequena equipe entregasse às duas lojas e projetaram offline-first desde o início, de modo que um usuário pudesse registrar um hábito no metrô sem sinal e sincronizar depois. Mantiveram o token de login no armazenamento seguro da plataforma e não num arquivo simples, incluíram o tempo de revisão da loja em cada plano de lançamento e testaram em alguns celulares baratos e antigos ao lado dos seus, o que pegou um desempenho lento que de outro modo teriam entregado.

**Grande empresa.** Uma empresa de logística construiu um aplicativo interno para motoristas e funcionários de armazém. Como armazéns e rotas de entrega têm sinal irregular, a equipe escolheu um design offline-first: leituras e atualizações de status são salvas localmente e sincronizadas quando a conexão volta. Usou um framework multiplataforma para servir uma base de código às duas plataformas com uma equipe pequena. O aplicativo é distribuído por gerenciamento de dispositivos móveis e não pelas lojas públicas, de modo que a TI controla a instalação, a configuração e a política de segurança nos dispositivos da empresa. As credenciais sensíveis vivem no armazenamento seguro da plataforma, e a biometria desbloqueia o aplicativo. Uma fazenda de dispositivos na nuvem testa uma amostra representativa dos modelos robustos que a equipe de fato carrega.

**Governo.** Uma agência nacional entregou um aplicativo para cidadãos de identidade e benefícios. A acessibilidade foi uma exigência rígida desde o primeiro dia: suporte completo a leitor de tela, dimensionamento dinâmico de texto e contraste forte, testados com ferramentas assistivas reais para cumprir a lei. Como os cidadãos usam uma enorme variedade de dispositivos, a equipe suportou uma ampla faixa de modelos mais antigos e conexões lentas e manteve funcionando offline as tarefas centrais. Os dados sensíveis ficam no armazenamento seguro do dispositivo, a biometria protege o acesso e as conexões de alto valor usam fixação de certificados com um processo planejado de rotação. O versionamento de API mantém funcionando os aplicativos antigos instalados, e existe um caminho de atualização forçada, raramente usado, para correções de segurança. Os prazos de revisão da loja são embutidos em todo plano de lançamento.

## Justificativa de negócio: motivações, ROI e TCO

O móvel é onde muitos usuários encontram o seu serviço, então o aplicativo afeta a adoção, a satisfação e a conclusão das tarefas que importam para a sua organização. Um aplicativo rápido, confiável e bem projetado aumenta o uso e reduz a carga de suporte. Para as empresas, um aplicativo móvel interno pode tornar mensuravelmente mais produtiva uma força de trabalho móvel e cortar papelada. Para os governos, um aplicativo utilizável para cidadãos amplia o acesso e reduz a demanda de central de atendimento e presencial.

No custo total de propriedade (TCO), a escolha da abordagem é a maior alavanca. O nativo significa pagar por duas bases de código e dois conjuntos de habilidades durante toda a vida do aplicativo. O multiplataforma troca parte disso por uma dependência que vocês precisam manter atual. Além do código, orcem as taxas de loja e os ciclos de revisão, um laboratório de testes de dispositivos ou uma fazenda na nuvem, o suporte contínuo às versões do SO à medida que as plataformas lançam todo ano e o trabalho de segurança que o móvel exige. O custo de investir pouco aparece como falhas em dispositivos sem suporte, incidentes de segurança por dados desprotegidos no dispositivo, lançamentos rejeitados ou atrasados e usuários que abandonam um aplicativo lento ou desajeitado.

Para defender o caso junto à liderança, liguem o aplicativo a resultados concretos: conclusão de tarefas, retenção, produtividade da força de trabalho ou custo de suporte reduzido. Precifiquem a decisão de abordagem inteira ao longo da vida do aplicativo e não apenas o primeiro lançamento e nomeiem os riscos (segurança, lei de acessibilidade, rejeição pela loja) que uma prática móvel séria reduz.

## Antipadrões e armadilhas

- **Tratar o móvel como um site encolhido**: ignorar o toque, os gestos e as convenções da plataforma.
- **Presumir uma rede perfeita**: sem tratamento offline, de modo que o aplicativo quebra no momento em que o sinal cai.
- **Testar só no modelo topo de linha mais recente**: esconder o desempenho ruim nos dispositivos que os usuários reais carregam.
- **Guardar segredos em arquivos simples**: dados sensíveis expostos quando um dispositivo é perdido ou roubado.
- **Excesso de notificações**: pushes demais, de modo que os usuários silenciam ou apagam o aplicativo.
- **Ignorar o tempo de revisão da loja**: planos de lançamento que presumem publicação instantânea e depois escorregam.
- **Sem caminho de atualização forçada**: versões antigas inseguras vivem sem jeito de aposentá-las.
- **Drenar bateria e dados**: trabalho constante em segundo plano e rede tagarela que os usuários notam.
- **Acessibilidade como reflexão tardia**: excluir usuários e, no governo, violar a lei.
- **Uma base de código forçada a parecer idêntica em toda parte**: um aplicativo que parece estranho nas duas plataformas.

## Modelo de maturidade

**Nível 1: Iniciar.** O móvel é ad hoc e reativo. O aplicativo é construído como um site, testado nos próprios celulares da equipe e muitas vezes quebra offline. Pouca atenção vai para o armazenamento seguro, a acessibilidade ou os prazos de revisão da loja. Os lançamentos são uma correria manual estressante, e ninguém é dono da abordagem de construção nem das chaves de assinatura.

**Nível 2: Desenvolver.** Aparecem práticas básicas, mas inconsistentes entre equipes e produtos. Uma abordagem de construção é escolhida para um dado aplicativo, segue o básico da plataforma e é testada em alguns dispositivos reais, e existem algum tratamento offline e armazenamento seguro. Os builds são parcialmente automatizados e alguém é dono dos envios à loja, mas o aplicativo de outra equipe ainda pode fazer tudo isso de modo diferente ou nem fazer.

**Nível 3: Padronizar.** A boa prática é documentada e imposta em toda a organização. O offline-first é o padrão, uma faixa documentada de suporte a dispositivos é testada num laboratório de dispositivos ou fazenda na nuvem e as diretrizes de design da plataforma e a acessibilidade são seguidas e verificadas com ferramentas assistivas reais. O armazenamento seguro, a biometria e o versionamento de API são padrão, o CI/CD automatiza builds, testes, assinatura e distribuição beta e o tempo de revisão da loja é planejado em todo lançamento.

**Nível 4: Gerenciar.** A qualidade móvel é medida e controlada em relação a linhas de base. As falhas, o desempenho de partida a frio e de renderização de telas, o uso de bateria e de dados e as taxas de conclusão de tarefas são capturados continuamente de dispositivos reais e acompanhados contra metas, com detalhamento por modelo e por versão do SO para que uma regressão em hardware de baixo desempenho seja pega e não entregue. A acessibilidade e a segurança são auditadas e não presumidas, as taxas de recusa de notificações e de adoção de atualizações são monitoradas e a faixa de suporte e a abordagem de construção são revisadas com essa evidência. As decisões de matar ou corrigir um lançamento repousam nas métricas, não em como o aplicativo pareceu no celular do líder.

**Nível 5: Orquestrar.** O móvel é continuamente melhorado e integrado em toda a organização, e se adapta à medida que o panorama de dispositivos muda. A rotação de certificados, os caminhos de atualização forçada e a reversão são rotina, a faixa de suporte e a abordagem de construção são redimensionadas com base em evidências à medida que as plataformas lançam todo ano e toda a gama de usuários e dispositivos é tratada como de primeira classe. O planejamento móvel é unido à prática de segurança, de acessibilidade, de APIs e de entrega, de modo que uma mudança de SO, um novo nível de dispositivo ou uma mudança de política é absorvida como trabalho de rotina e não como emergência.

## Ideias para discussão

- Como vocês decidem entre nativo, multiplataforma e aplicativo web progressivo para um dado produto?
- Que faixa de suporte a dispositivos e versões do SO se ajusta aos seus dados reais de usuários, e como vocês a mantêm atual?
- Onde o offline-first é essencial no seu aplicativo, e como vocês tratarão os conflitos de sincronização?
- Quando uma atualização forçada se justifica, e como vocês evitam bloquear usuários de forma injusta?
- Como vocês testarão em dispositivos reais numa escala que reflita seus usuários?
- Que dados sensíveis vivem no dispositivo, e como cada um é protegido?
- Como vocês honram as convenções de cada plataforma a partir de uma base de código compartilhada?

## Principais conclusões

- Escolham a abordagem de construção (nativo, multiplataforma ou PWA) para a vida inteira do aplicativo.
- Sigam as diretrizes de design da plataforma para que o aplicativo pareça familiar e reduza o esforço do usuário.
- Projetem para as restrições do móvel: offline-first, bateria e dados frugais, fragmentação, telas pequenas.
- Vocês não controlam o momento do lançamento. Planejem a revisão da loja, o versionamento e as atualizações forçadas.
- Usem notificações push e deep links com comedimento e consentimento.
- Protejam os dados no dispositivo com armazenamento seguro, biometria e, onde justificado, fixação de certificados.
- Testem em dispositivos reais e automatizem o pipeline móvel por CI/CD.
- Façam da acessibilidade uma exigência, que para o governo é um mandato legal.

## Referências e leitura complementar

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
