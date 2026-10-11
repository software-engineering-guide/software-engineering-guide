# 10.12 Código aberto versus código fechado

## Visão geral e motivação

Quase todo sistema moderno é uma mistura de software que vocês escreveram, software que compraram e software que pegaram de graça. Dois desses três trazem uma escolha fundamental: o software é de **código aberto** ou de **código fechado**? O **[software de código aberto](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** é distribuído sob uma licença que concede a todos o direito de usar, estudar, modificar e redistribuir o código-fonte, as instruções legíveis por humanos que definem o programa. O **software de código fechado**, também chamado de **[software proprietário](https://en.wikipedia.org/wiki/Proprietary_software)**, é distribuído como um produto acabado cujo código-fonte o fornecedor mantém privado. Vocês obtêm o direito de rodá-lo sob uma licença, mas não de inspecionar nem de mudar como funciona. Uma categoria intermediária, o **[software de código disponível](https://en.wikipedia.org/wiki/Source-available_software)** (source-available), publica o código para leitura mas restringe o uso, a modificação ou a redistribuição. É *visível* mas não *aberto* pela definição padrão.

Dois esclarecimentos importam antes de compará-los. Primeiro, “livre” (free) é ambíguo. A comunidade distingue **livre como em liberdade** (a liberdade de modificar e compartilhar, às vezes escrita “libre”) de **livre como em preço** (custo zero, “gratis”). O código aberto trata de liberdade, não necessariamente de preço. Segundo, as licenças de código aberto se dividem em duas famílias. As **[licenças permissivas](https://en.wikipedia.org/wiki/Permissive_software_license)** (como a [MIT](https://en.wikipedia.org/wiki/MIT_License), a BSD e a Apache 2.0) deixam vocês fazerem quase qualquer coisa, inclusive embutir o código num produto fechado. As **licenças [copyleft](https://en.wikipedia.org/wiki/Copyleft)** (como a [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) exigem que as obras derivadas que vocês distribuem também sejam liberadas sob os mesmos termos abertos, uma regra de reciprocidade que os críticos às vezes chamam de “viral” e os defensores de “compartilhar igual” (share-alike).

Este capítulo olha a escolha de dois lados. Como **consumidor**, vocês decidem se adotam um componente de código aberto ou proprietário. Como **produtor**, vocês decidem se abrem o código de um software que construíram. Para grandes empresas e especialmente para o governo, as duas decisões pesam muito além do arquivo de licença. Tocam a contratação (capítulo 10.3), a soberania digital (capítulo 10.11), a segurança da cadeia de suprimentos (capítulo 4.2), a interoperabilidade (capítulo 3.8) e o cálculo de construir ou comprar (capítulo 6.1).

## Princípios fundamentais

- **A licença, não o preço, define o “aberto”.** Leiam a licença: gratuito e código aberto são alegações diferentes.
- **Nenhum modelo é inerentemente mais seguro.** Ambos podem ser excelentes ou negligentes. As práticas em torno do código importam mais que sua abertura.
- **A abertura é uma alavanca de redução de dependência.** O acesso ao código-fonte é a proteção definitiva contra o [aprisionamento a fornecedor](https://en.wikipedia.org/wiki/Vendor_lock-in) (lock-in).
- **O fardo operacional é sempre de vocês.** Grátis para adquirir nunca é grátis para rodar. O [custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership) conta a história real.
- **Os diferenciadores ficam fechados, as commodities podem abrir.** Abram o código do que não distingue vocês. Guardem o que distingue.
- **O copyleft tem consequências.** Entendam as obrigações de reciprocidade antes de embutir código copyleft num produto que vocês distribuem.
- **Uma comunidade viva é um ativo, um repositório abandonado é um passivo.** Julguem o projeto, não só a licença.

## Recomendações

### Avalie um componente pelo projeto, não só pela licença

Antes de adotar qualquer dependência, de código aberto ou proprietária, avaliem sua saúde: cadência de lançamentos, número e diversidade de mantenedores, responsividade a relatos de segurança e amplitude de adoção. Uma biblioteca de código aberto com um único mantenedor e um pequeno fornecedor proprietário carregam o mesmo **risco de fator ônibus** (o perigo de um projeto colapsar se uma ou poucas pessoas-chave saírem). Favoreçam componentes com uma base ampla de contribuidores ou um fornecedor financeiramente sólido e registrem a avaliação como parte da diligência prévia (capítulos 10.2, 4.2).

### Leia e acompanhe as licenças como uma obrigação de primeira classe

Mantenham um inventário de todo componente e sua licença e imponham uma política sobre quais famílias de licença são aceitáveis para quais usos. A distinção crítica é o copyleft. O código **permissivo** (MIT, Apache 2.0) em geral pode ser embutido livremente em produtos fechados. O **copyleft forte** (GPL) pode obrigar vocês a liberar sob os mesmos termos o seu próprio derivado distribuído. Usem a **análise de composição de software (SCA)** automatizada, ferramentas que varrem as dependências para identificar componentes, licenças e vulnerabilidades conhecidas, e gerem uma **lista de materiais de software (SBOM)**, uma lista formal de todo componente de um produto (capítulos 10.3, 4.2).

### Julgue a segurança pela prática, não pela abertura

Não presumam que o código aberto é seguro pelo **argumento dos “muitos olhos”** (a [Lei de Linus](https://en.wikipedia.org/wiki/Linus%27s_law): “com olhos suficientes, todos os bugs são superficiais”). E não presumam que o código proprietário é seguro por **[segurança por obscuridade](https://en.wikipedia.org/wiki/Security_through_obscurity)** (a crença falha de que esconder o código-fonte esconde as falhas). Muitos olhos só ajudam se gente qualificada de fato olha, e muitos projetos amplamente usados são mantidos de modo escasso. Ambos os modelos carregam **risco de cadeia de suprimentos**: o código aberto por dependências comprometidas ou abandonadas, o proprietário por código opaco e canais de atualização que vocês não conseguem inspecionar. Fixem versões, verifiquem a procedência, varram continuamente e monitorem avisos seja qual for o modelo (capítulo 4.2).

### Projete para a saída e a interoperabilidade

Prefiram componentes que falem padrões abertos e formatos de dados portáveis, para poder substituí-los depois (capítulos 3.8, 10.11). Com o código aberto, vocês ganham a saída definitiva: se um projeto empaca, vocês podem **[bifurcá-lo](https://en.wikipedia.org/wiki/Fork_(software_development))** (fork; criar e manter a própria cópia). Com o software proprietário, negociem proteções de antemão: exportação de dados em formatos abertos, APIs documentadas e **[escrow de código-fonte](https://en.wikipedia.org/wiki/Source_code_escrow)** (um arranjo legal em que o fornecedor deposita o código-fonte com um terceiro, liberado para vocês se o fornecedor falir). Projetem para que nenhum componente isolado, de qualquer tipo, possa manter o seu sistema como refém.

### Pese o custo total de propriedade, não o preço de tabela

Comparem as opções pelo **custo total de propriedade (TCO)**, o custo integral de toda a vida incluindo aquisição, integração, operação, suporte, treinamento, atualizações e substituição final, em vez de só as taxas de licença. O código aberto muitas vezes troca custo de licenciamento por maior custo operacional e de pessoal. O software proprietário muitas vezes troca taxas previsíveis de assinatura por aprisionamento e menos controle. Incluam o custo do próprio modelo: o código aberto autossustentado exige habilidade interna, enquanto o software proprietário exige capacidade de gestão de fornecedores.

### Como produtor, abra o código do que não diferencia vocês

Classifiquem o seu próprio software entre o que dá vantagem competitiva ou de missão e o que é encanamento sem diferenciação. Mantenham proprietários os diferenciadores. Considerem abrir o código da infraestrutura commodity, onde uma comunidade pode compartilhar manutenção e melhoria. Para o governo, pesem o **“dinheiro público, código público”** (o princípio de que o software financiado pelos contribuintes deve estar publicamente disponível por padrão) como condutor de transparência, reutilização e soberania (capítulos 10.5, 10.11). Escolham a licença deliberadamente: permissiva para maximizar a adoção, copyleft para manter aberto o ecossistema.

## Compromissos: prós e contras

| Dimensão | Código aberto | Código fechado / proprietário |
|---|---|---|
| **Custo de aquisição** | Em geral zero para adquirir | Taxa de licença ou de assinatura |
| **Custo total de propriedade** | O custo se desloca para operações e pessoal | Mais previsível, mas com prêmio de aprisionamento |
| **Controle e personalização** | Total: vocês podem ler e mudar o código-fonte | Limitado ao que o fornecedor expõe |
| **Suporte e responsabilização** | Comunidade ou terceiro pago. Sem um único responsável a quem cobrar | Suporte contratual e uma parte responsável clara |
| **Postura de segurança** | Auditável. “Muitos olhos” se de fato mantido | Gerido pelo fornecedor. Opaco. A obscuridade não é proteção |
| **Longevidade / abandono** | Pode ser bifurcado se mantido. Ainda pode murchar | Depende da viabilidade e do roteiro do fornecedor |
| **Aprisionamento a fornecedor** | Baixo: código-fonte e formatos abertos viabilizam a saída | Alto, a menos que mitigado por padrões e escrow |
| **Ecossistema** | Comunidade aberta e interoperabilidade | Curado, integrado, às vezes murado |

A tensão recorrente é **controle versus conveniência e responsabilização**. O código aberto maximiza o controle, a auditabilidade e a liberdade do aprisionamento, mas pede que vocês forneçam a capacidade, a integração e o suporte. O software proprietário entrega um produto com suporte, integrado e com um responsável, e um contrato para impor, mas cede controle e convida ao aprisionamento. A solução raramente é tudo ou nada. A maioria dos patrimônios maduros mistura fundações de código aberto com sistemas proprietários onde o suporte, a responsabilização ou a capacidade especializada justificam o compromisso.

## Perguntas para discutir com sua equipe

1. **Impomos uma política de licenças com SCA automatizada e SBOMs no pipeline, especialmente para pegar o copyleft forte antes que seja entregue?** Embutir uma biblioteca GPL num produto proprietário distribuído pode obrigar vocês a liberar o seu próprio código-fonte, e essa surpresa costuma aparecer tarde, quando é caro desfazer. Mantenham um inventário de todo componente e sua licença, imponham quais famílias de licença são aceitáveis para quais usos e rodem a análise de composição de software automaticamente para que o pipeline bloqueie as violações em vez de um advogado pegá-las na hora de entregar. Gerem uma SBOM como rotina. Para um patrimônio grande ou governamental, isso também é higiene da cadeia de suprimentos e muitas vezes uma exigência de contratação. Levem o inventário atual de licenças, ou o fato de que vocês não têm um, e decidam quem é dono da política.

2. **Ao adotar uma dependência, avaliamos a saúde do projeto e o fator ônibus como diligência prévia?** Uma biblioteca de código aberto com um único mantenedor e um pequeno fornecedor proprietário carregam o mesmo risco: o projeto colapsa se uma ou poucas pessoas-chave saírem. Antes de adotar qualquer coisa, avaliem a cadência de lançamentos, o número e a diversidade de mantenedores, a responsividade a relatos de segurança e a amplitude de adoção e registrem a avaliação. Nenhum modelo é mais seguro por padrão: os “muitos olhos” só ajudam se gente qualificada de fato olha, e muitos projetos amplamente usados são mantidos de modo escasso. Levem as três ou quatro dependências em que o seu produto mais se apoia e perguntem, para cada uma, quantas pessoas teriam de ir embora antes de virar problema de vocês. Se vocês não conseguem responder, essa é a avaliação que devem a si mesmos.

3. **Quando compramos software proprietário, garantimos de antemão proteções de saída?** O software proprietário oferece responsabilização e conveniência em troca de controle, e o custo oculto é o aprisionamento: custos de troca que deixam um fornecedor subir preços ou degradar o serviço com pouco recurso. Negociem as proteções antes de assinar, quando vocês ainda têm alavancagem: exportação de dados em formatos abertos, APIs documentadas e escrow de código-fonte que libera o código se o fornecedor falir. Com o código aberto, a sua saída é a capacidade de bifurcar; com o proprietário, vocês precisam escrever a saída no contrato. Levem os seus sistemas proprietários mais críticos e perguntem o que de fato acontece se o fornecedor dobrar o preço ou falir. Se a resposta é “estamos presos”, consertem o contrato na renovação.

4. **Para o software que construímos nós mesmos, como decidimos o que abrir e o que manter fechado, e quem tem a autoridade de tomar essa decisão?** Errem numa direção e vocês entregam o próprio código que os diferencia; errem na outra e vocês acumulam um encanamento commodity cuja manutenção uma comunidade teria prazer em compartilhar. As pressões concorrentes são reais: os engenheiros querem o ganho de recrutamento e de reputação de um repositório público, enquanto o produto e o jurídico temem entregar uma vantagem a rivais ou expor uma heurística sensível à segurança. Levem uma classificação honesta dos seus sistemas entre diferenciadores da missão e infraestrutura sem diferenciação e nomeiem a pessoa ou o conselho que aprova uma liberação, porque uma decisão ad hoc tomada por quem empurrou o repositório é como as joias da coroa vazam. Para uma grande empresa a questão é de estratégia de portfólio, e para o governo ela colide com o “dinheiro público, código público”, o princípio de que o software pago pelos contribuintes deve ser público por padrão, então decidam de antemão quais isenções (segurança nacional, detecção de fraude, dados pessoais) justificam manter o código fechado.

5. **As nossas comparações de construir ou comprar capturam o custo total de propriedade integral, ou ainda tratamos uma taxa de licença zero como custo zero?** O erro financeiro mais comum com o código aberto é ler “grátis para adquirir” como “grátis para rodar” e depois descobrir que a integração, as operações, a resposta de segurança e o suporte pago anulam qualquer licença que vocês evitaram. A tensão é que uma assinatura proprietária parece cara na fatura enquanto esconde um prêmio de aprisionamento, e um componente aberto parece grátis na fatura enquanto desloca o custo para a sua própria equipe. Levem um modelo de TCO comparável para duas ou três decisões reais: aquisição, integração, operação, suporte, treinamento, atualizações, resposta de segurança e substituição final, precificados ao longo de toda a vida e não do primeiro ano. Num patrimônio corporativo ou governamental, acrescentem o custo do próprio modelo operacional, já que o código aberto autossustentado exige habilidade interna que vocês precisam recrutar e reter, e tratem uma comparação que omite essas linhas como evidência e não como análise.

6. **Julgamos a segurança de um componente pelas suas práticas, ou nos apoiamos no rótulo de abertura, seja os “muitos olhos” ou o sigilo do código fechado?** Ambos os padrões são armadilhas: os “muitos olhos” só protegem vocês quando gente qualificada de fato revisa o código, e muitos projetos abertos amplamente usados rodam sobre um mantenedor esgotado, enquanto o código fechado que depende de atacantes não o verem é segurança por obscuridade, não um controle. O debate importa porque muda onde vocês gastam o escasso esforço de segurança, e a resposta honesta é que ambos os modelos carregam risco de cadeia de suprimentos, o código aberto por dependências comprometidas ou abandonadas e o proprietário por canais opacos de atualização que vocês não conseguem inspecionar. Levem evidências dos seus componentes mais críticos: quem de fato os revisa, com que rapidez os avisos são corrigidos, se as versões são fixadas e a procedência verificada e se vocês geram uma SBOM. Para um patrimônio grande ou governamental, liguem isso às obrigações de contratação e de varredura contínua, porque um regulador perguntará o que vocês inspecionaram e não se o código-fonte era público.

## Perspectiva por setor

**Startup.** Com pouco fôlego, vocês constroem sobre fundações de código aberto porque não podem bancar taxas de licença e querem a liberdade de bifurcar se um projeto empacar. Rodem uma varredura de análise de composição antes de entregar para que uma biblioteca de copyleft forte não obrigue vocês em silêncio a publicar o próprio código-fonte e mantenham o seu único diferenciador real estritamente fechado. Abram o código de uma pequena ferramenta não crítica se isso ajudar no recrutamento, mas não montem um fardo de manutenção que vocês não conseguem carregar.

**Pequena empresa.** Sem especialista jurídico nem de plataforma, tratem a licença como um risco que vocês não devem interpretar mal e não como um tema que podem dominar. Prefiram ferramentas proprietárias com suporte ou distribuições comerciais de código aberto em que um fornecedor é dono das correções e da responsabilização, porque autossustentar uma pilha que vocês não conseguem operar é uma falsa economia. Quando adotarem um componente gratuito, conferiram que a licença permite o seu uso e que o projeto é de fato mantido, não abandonado.

**Grande empresa.** Em escala o problema é a consistência entre muitas equipes: uma política escrita de licenças, análise automatizada de composição de software e geração de SBOM em todo pipeline e decisões de construir ou comprar baseadas em TCO e não em hábito de cada equipe. Gerenciem o software aberto e o proprietário como um só portfólio, padronizem proteções de saída como formatos abertos e escrow de código-fonte na contratação e acompanhem a saúde das dependências críticas para que um único projeto abandonado não vire um incidente. Governem também o lado do produtor, com uma regra clara do que a organização abre versus mantém fechado.

**Governo.** A contratação, os deveres de transparência e a prestação de contas públicas moldam toda escolha. Pesem o “dinheiro público, código público”, o princípio de que o software pago pelos contribuintes deve ser público por padrão, para avançar a reutilização entre agências e a soberania digital, reservando isenções estreitas para código sensível à segurança ou a dados pessoais. Exijam de qualquer fornecedor proprietário a exportação de dados em formatos abertos e o escrow de código-fonte para que a falência de um fornecedor não deixe encalhado um serviço público e publiquem o código-fonte não sensível para que os cidadãos possam auditar as regras que os governam.

## Exemplos

**Startup.** Uma startup de três fundadores constrói todo o produto sobre fundações de código aberto (Linux, um banco de dados de código aberto, um framework web) porque não pode bancar taxas de licença e quer a liberdade de bifurcar se um projeto empacar. Antes de entregar, um fundador roda uma varredura de análise de composição e pega uma biblioteca de copyleft forte que teria forçado a publicação do algoritmo proprietário de correspondência, então a troca por uma equivalente de licença permissiva. Mantêm esse algoritmo, seu único diferenciador, estritamente fechado e abrem apenas uma pequena ferramenta interna de logs para construir boa vontade e atrair engenheiros.

**Grande empresa.** Uma grande seguradora roda sua plataforma central sobre fundações de código aberto: Linux, um banco de dados de código aberto amplamente usado e um orquestrador de contêineres. Mas compra uma suíte proprietária de modelagem atuarial, porque a expertise de domínio do fornecedor, as certificações regulatórias e o contrato de suporte valem a taxa e não há alternativa aberta comparável. Paga uma assinatura de **código aberto comercial** (distribuições dos componentes abertos com suporte do fornecedor) para obter responsabilização e correções no encanamento, enquanto mantém o algoritmo de precificação que a diferencia estritamente proprietário e interno. A análise de TCO (capítulo 10.10) conduz cada escolha, e não a ideologia.

**Governo.** Uma autoridade tributária nacional, sob uma política de “dinheiro público, código público”, constrói um novo serviço de elegibilidade a benefícios sobre componentes de código aberto e padrões abertos (capítulo 3.8), para que outras agências possam reutilizá-lo e os cidadãos possam auditar as regras. Publica o código não sensível num repositório público, retendo como fechadas, por razões de segurança, apenas as heurísticas de detecção de fraude. Isso reduz o aprisionamento a fornecedor e avança a soberania digital (capítulo 10.11). As regras de contratação (capítulo 10.3) exigem que qualquer componente proprietário ofereça exportação de dados em formatos abertos e escrow de código-fonte, para garantir a continuidade se o fornecedor falir.

## Justificativa de negócio: motivações, ROI e TCO

O apelo financeiro do código aberto, a ausência de taxa de licença, é a parte menos confiável do argumento, porque a aquisição é uma pequena fração do TCO. Os retornos duráveis são estratégicos: a liberdade do aprisionamento (a capacidade de mudar ou largar um fornecedor sem rearquitetar), a auditabilidade para segurança e conformidade, a adoção mais rápida porque os engenheiros podem experimentar antes de se comprometer e a manutenção compartilhada de código commodity por todo um setor. Os custos compensatórios são reais. Vocês precisam fornecer integração, operações, resposta de segurança e muitas vezes suporte pago, e um projeto sem manutenção mal escolhido pode custar mais em incidentes do que qualquer licença teria custado.

O argumento de negócio do software proprietário é responsabilização e conveniência: um único fornecedor responsável pelo produto, um contrato de suporte que vocês conseguem impor, funcionalidades integradas e orçamento previsível. Seu custo oculto é o aprisionamento, os custos de troca que deixam um fornecedor subir preços ou degradar o serviço com pouco recurso, mais a dependência da solvência e do roteiro do fornecedor. **Modelos de negócio** comuns turvam a linha: o **[núcleo aberto](https://en.wikipedia.org/wiki/Open-core_model)** (open core; uma base aberta com complementos proprietários pagos), o **licenciamento duplo** (o mesmo código oferecido sob uma licença copyleft e uma licença comercial paga), o **[software como serviço](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (o software roda como um serviço hospedado que vocês alugam, em que o código-fonte pode ser irrelevante porque vocês nunca possuem o binário) e os modelos de **suporte/assinatura** que vendem serviço em torno de um código de resto gratuito.

Para um produtor, o ROI de **abrir o código do seu próprio software não diferenciador** pode ser substancial. Contribuidores externos reduzem a sua carga de manutenção. O projeto vira um ativo de recrutamento e de reputação. A adoção externa faz do seu padrão o padrão de fato. Para o governo, entrega transparência e reutilização em todo o setor público. A regra estratégica é simples: abram o código da commodity para dividir o seu custo e fazer crescer um ecossistema e mantenham fechado o diferenciador para proteger a vantagem que financia todo o resto.

## Antipadrões e armadilhas

- **“Grátis significa grátis”:** tratar a aquisição a custo zero como TCO zero e depois financiar de menos a operação e o suporte.
- **Cegueira de licença:** embutir código de copyleft forte num produto proprietário distribuído e disparar obrigações que vocês nunca planejaram.
- **Fé nos “muitos olhos”:** presumir que um projeto aberto é auditado quando tem um mantenedor sobrecarregado e nenhuma revisão de segurança.
- **Segurança por obscuridade:** acreditar que o código fechado é seguro simplesmente porque os atacantes não conseguem lê-lo.
- **Absolutismo ideológico:** impor “tudo aberto” ou “tudo proprietário” em vez de escolher por componente, pelo mérito e pelo TCO.
- **Ignorar a procedência:** puxar dependências sem SBOM, fixação de versões nem verificação da cadeia de suprimentos (capítulo 4.2).
- **Abrir o código das joias da coroa:** liberar o próprio código que diferencia vocês, entregando a sua vantagem.
- **Bifurcar e esquecer:** bifurcar um projeto abandonado sem a capacidade de de fato manter o fork.

## Modelo de maturidade

**Nível 1 (Iniciar).** Os componentes de código aberto e proprietários entram no patrimônio ad hoc. As licenças não são lidas, não há inventário nem SBOM, e a escolha entre os modelos é feita por hábito ou só pelo preço. Os riscos de abandono e de licença só surgem quando algo quebra, e cada equipe reage por conta própria.

**Nível 2 (Desenvolver).** Algumas equipes começam práticas básicas: um inventário de componentes e licenças, uma visão aproximada de licenças aceitáveis e análise de composição de software ocasional. As decisões de construir ou comprar e de aberto ou fechado são escritas, mas a disciplina é irregular e inconsistente de uma equipe a outra, de modo que uma surpresa de copyleft ou de fator ônibus ainda pode escapar onde o hábito não pegou.

**Nível 3 (Padronizar).** Um framework documentado governa tanto o consumo quanto a produção em toda a organização. Os componentes são escolhidos pelo TCO e pela saúde do projeto, as licenças são impostas automaticamente no pipeline para que as violações bloqueiem um build, as SBOMs são geradas como rotina e uma política explícita declara o que a organização abre versus mantém fechado. As proteções de saída, como formatos abertos e escrow de código-fonte, são padrão na contratação, e toda equipe segue as mesmas regras e não as suas próprias.

**Nível 4 (Gerenciar).** O programa é medido e controlado em relação a linhas de base. A organização acompanha métricas como a cobertura de SBOM entre os produtos, a fração de dependências que violam a política, o tempo médio para corrigir uma vulnerabilidade de dependência divulgada, as pontuações de fator ônibus e de saúde dos projetos críticos e o TCO realizado contra a estimativa que justificou cada escolha. Os limiares disparam ação: um componente cuja manutenção empaca ou cuja latência de correção deriva além da meta é sinalizado para substituição com base em evidências, e as decisões de aberto ou fechado e de construir ou comprar são revisadas contra os números e não defendidas por hábito.

**Nível 5 (Orquestrar).** A estratégia de código aberto é uma capacidade de negócio deliberada, integrada em toda a organização e continuamente melhorada. A organização contribui para os projetos de que depende, e às vezes é curadora deles, abre o código do seu software não diferenciador como rotina e devolve dados de saúde das dependências e de TCO à contratação, à segurança e ao planejamento de produto. Reequilibra rotineiramente seu portfólio de software aberto e proprietário, adaptando-se às mudanças de custo, risco, soberania e vantagem estratégica antes que forcem uma crise.

## Ideias para discussão

- Onde no seu patrimônio perder um único fornecedor ou mantenedor seria existencial, e qual é o seu plano de saída?
- Quais dos seus próprios sistemas são commodities cujo código vocês poderiam abrir, e quais são diferenciadores de verdade a proteger?
- A sua organização trata os “muitos olhos” como um controle de segurança real ou como uma suposição não examinada?
- Para leitores do setor público: o que um padrão de “dinheiro público, código público” mudaria na sua próxima contratação?
- Quão bem as suas comparações de TCO capturam os custos operacionais e de suporte que o código aberto desloca para vocês?

## Principais conclusões

- **Aberto versus fechado é definido pela licença**, não pelo preço. Conheçam a diferença entre livre como em liberdade e livre como em preço e entre permissiva e copyleft.
- **Nenhum modelo é inerentemente mais seguro ou mais barato.** Julguem as práticas do projeto e o seu TCO integral, não o rótulo de abertura.
- **A abertura é o antídoto mais forte ao aprisionamento**, entregando auditabilidade, portabilidade e a capacidade de bifurcar. O software proprietário oferece responsabilização e conveniência em troca de controle.
- **Decidam por componente, pelo mérito**, e misturem os modelos deliberadamente e não por ideologia.
- **Como produtor, abram o código da commodity e mantenham fechado o diferenciador** e, no governo, pesem o “dinheiro público, código público” por transparência, reutilização e soberania.

## Referências e leitura complementar

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
