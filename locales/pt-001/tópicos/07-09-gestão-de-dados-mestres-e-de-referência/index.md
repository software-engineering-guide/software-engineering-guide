# 7.9 Gestão de dados mestres e de referência

## Visão geral e motivação

Perguntem a cinco sistemas quantos clientes a organização tem e vocês terão cinco números diferentes. Um conta endereços de e-mail, outro conta contratos, outro conta logins, e dois discordam sobre se “Acme Corp” e “ACME Corporation” são a mesma empresa. A [gestão de dados mestres](https://en.wikipedia.org/wiki/Master_data_management) (MDM) é a disciplina de reconciliar as entidades centrais que o seu negócio compartilha, cliente, produto, fornecedor, funcionário, local, numa versão autoritativa em que todo sistema possa confiar.

Comecem classificando os dados em três tipos, porque eles pedem tratamentos diferentes. Os dados mestres descrevem os substantivos do negócio: as pessoas, os lugares e as coisas a que muitos processos se referem. Os dados de referência são o vocabulário controlado que esses processos usam: códigos de moeda, códigos de país, listas de unidades de medida, categorias de produto. Os dados transacionais registram os verbos: um pedido feito, um pagamento realizado, uma remessa enviada. Os dados mestres e de referência têm volume menor que as transações mas são referenciados em toda parte, então um erro neles contamina tudo que vem a jusante.

O custo de errar é concreto. Quando o mesmo cliente existe como quatro registros ligeiramente diferentes, vocês enviam quatro catálogos, não enxergam um único relacionamento que valia a pena manter e o seu número de receita por cliente está silenciosamente errado. Um [registro de ouro](https://en.wikipedia.org/wiki/Single_source_of_truth) (golden record), a versão única e confiável de uma entidade montada a partir de muitas fontes, é o que substitui essas cópias conflitantes, para que cada integração pare de resolver de novo o mesmo problema de correspondência.

Para empresas que reconciliam sistemas acumulados por décadas de crescimento e de aquisições, a MDM é a diferença entre uma visão coerente do cliente e um imposto permanente de reconciliação. Para o governo, as apostas sobem: um cidadão que aparece como três pessoas diferentes em três agências pode ter um benefício negado, ser tributado duas vezes ou se perder entre departamentos. Este capítulo complementa a estratégia e governança de dados (capítulo 7.1), que define propriedade e política; a modelagem de dados e a camada semântica (capítulo 7.7), que define o que as entidades significam; e a qualidade e observabilidade de dados (capítulo 7.8), que mantém os registros limpos ao longo do tempo.

## Princípios fundamentais

- Classifiquem os dados em mestres, de referência e transacionais. Cada um exige um tratamento diferente.
- Um registro de ouro por entidade do mundo real, montado deliberadamente, não descoberto por acidente.
- Escolham um estilo de arquitetura de MDM que se ajuste às suas necessidades de controle e de latência, não à moda.
- Correspondência e sobrevivência são regras de negócio, então escrevam-nas e deixem os curadores ajustá-las.
- Os dados de referência são vocabulário compartilhado. Versionem-nos e publiquem-nos como uma API.
- Governança e curadoria são o motor da MDM. O software é apenas a ferramenta.
- Propaguem os registros de ouro como eventos para que os sistemas a jusante permaneçam sincronizados, não obsoletos.
- Meçam a MDM por decisões melhoradas e duplicatas removidas, não por registros carregados.

## Recomendações

### Classifique primeiro os dados mestres, de referência e transacionais

Vocês não conseguem gerenciar o que não classificaram, então comecem classificando os seus domínios de dados. Um bom teste para dados mestres é se um valor errado se propaga: se um endereço ruim se espalha para a cobrança, a entrega e as notificações legais, vocês estão diante de dados mestres. Isso conduz o seu investimento: vocês constroem um motor de correspondência para a entidade cliente, não para itens de linha de pedido. Nomeiem os domínios explicitamente, classifiquem-nos pela dor que a sua duplicação causa e comecem pelo um ou dois que mais doem, em geral cliente e produto, porque tocam a receita diretamente.

### Escolha deliberadamente um estilo de arquitetura de MDM

Há quatro estilos comuns de arquitetura, e o certo depende de quanta autoridade vocês conseguem centralizar e de quão depressa as mudanças precisam se propagar. O estilo de registro (registry) deixa os dados nos sistemas de origem e constrói apenas um índice de identificadores correspondentes, de modo que consegue responder “estes cinco registros são o mesmo cliente” sem mover dados; é barato e de baixo risco, mas somente de leitura, então não consegue consertar as origens. O estilo de consolidação puxa cópias para um hub central e as mescla em registros de ouro para relatórios, mas não empurra as correções de volta, de modo que as origens continuam bagunçadas. O estilo de coexistência vai além: sincroniza os valores limpos de volta com os sistemas de origem, de modo que as origens melhoram com o tempo enquanto ainda operam de forma independente. O estilo de hub centralizado ou transacional faz do hub de MDM o próprio sistema de registro, em que as entidades são criadas e editadas diretamente e todo outro sistema consome dele; isso dá a consistência e o controle mais fortes e é o mais difícil de adotar porque muda onde o trabalho acontece. Muitas organizações progridem de um registro que prova valor rumo à coexistência à medida que a confiança cresce e rodam mais de um estilo em domínios diferentes.

### Correspondência, mescla e regras de sobrevivência explícitas

O coração da MDM é decidir quando dois registros descrevem a mesma coisa do mundo real. Isso é a [ligação de registros](https://en.wikipedia.org/wiki/Record_linkage) (record linkage), raramente tão simples quanto uma correspondência exata de chave, porque os dados reais estão cheios de erros de digitação, abreviações e campos ausentes. A correspondência determinística usa regras exatas sobre campos escolhidos (mesmo CPF ou CNPJ, ou mesmo e-mail mais código postal). A correspondência probabilística pontua a similaridade entre muitos campos usando [correspondência aproximada de cadeias](https://en.wikipedia.org/wiki/Approximate_string_matching) e pesos, de modo que “Bob Smith, 12 Main St” e “Robert Smith, 12 Main Street” possam ser julgados uma correspondência provável acima de um limiar. Decidir que registros se referem à mesma entidade se chama resolução de identidade, e ela sustenta tudo, de visões do cliente à detecção de fraude.

Quando os registros correspondem, vocês precisam decidir que valores sobrevivem no registro de ouro. Essas regras de sobrevivência são lógica de negócio, então tornem-nas explícitas: preferir o valor mais recente para um telefone, o valor mais completo para um endereço, a fonte mais confiável para um nome legal. Definam uma faixa de limiar em que as correspondências são mescladas automaticamente, uma faixa inferior em que são rejeitadas automaticamente e uma faixa intermediária em que um humano decide, que é onde mora a curadoria. Mantenham toda mescla reversível e registrada, porque uma mescla errada que funde dois clientes reais é pior que uma correspondência perdida.

### Trate os dados de referência como vocabulário compartilhado e versionado

Os dados de referência são o vocabulário compartilhado que os seus sistemas falam, e um vocabulário que deriva causa desalinhamento silencioso: quando um sistema usa o código de país ISO “GB” e outro usa “UK”, as junções falham e as contagens divergem. Mantenham cada lista de referência num único lugar governado, publiquem-na para todos os consumidores e, de forma crucial, versionem-na. Os códigos são acrescentados, aposentados, divididos e fundidos ao longo do tempo, e se vocês sobrescrevem a lista no lugar, quebram relatórios históricos que estavam corretos sob os códigos antigos.

Tratem um conjunto de dados de referência como uma API com um contrato. Publiquem-no com datas de vigência para que um consumidor possa perguntar “quais eram os códigos de região válidos nesta data”, guardem os códigos aposentados em vez de apagá-los e registrem o mapeamento quando um código muda de significado. Prefiram padrões externos reconhecidos onde existirem, como os códigos ISO de país e de moeda, porque os padrões dão interoperabilidade de graça e se ligam à disciplina de padrões abertos do capítulo 3.8.

### Modele hierarquias e relacionamentos, não só registros planos

Os dados mestres não são uma pilha de linhas independentes: são uma teia de relacionamentos. Um cliente pertence a uma família e a uma matriz corporativa. Um produto se agrega a uma categoria e a uma marca. Essas hierarquias carregam significado de negócio real: agreguem as vendas por matriz corporativa e o quadro muda por completo em comparação com agregar por conta individual. Modelem esses relacionamentos explicitamente para que os consumidores os percorram de modo consistente em vez de cada equipe inventar a própria agregação.

Atentem ao caso em que uma entidade precisa de várias hierarquias ao mesmo tempo. Um produto pode se agregar de um jeito para as finanças e de outro para o merchandising, e ambos são legítimos, então deem suporte a várias hierarquias nomeadas em vez de forçar uma árvore verdadeira. Os relacionamentos entre domínios também importam, como qual fornecedor fornece qual produto.

### Ligue os registros de ouro à camada semântica e à qualidade de dados

Os registros de ouro que a MDM produz são as entidades confiáveis às quais a camada semântica do capítulo 7.7 se refere ao definir métricas: “clientes ativos” só significa algo quando “cliente” é inequívoco. Alimentem a camada semântica com os seus registros de ouro para que toda métrica conte as mesmas entidades desduplicadas e resolvidas.

A MDM e a qualidade de dados (capítulo 7.8) são dois lados da mesma moeda: as verificações de qualidade detectam as duplicatas, os nulos e as violações de formato que a MDM então resolve, e a correspondência da MDM revela problemas de qualidade que as verificações perderam. Rodem monitoramento contínuo de qualidade especificamente sobre os seus dados mestres: taxas de duplicatas, distribuições de confiança das correspondências, completude dos campos-chave e o tamanho da fila de revisão, para que a deriva apareça antes de os consumidores a verem.

### Propague os registros de ouro por meio de eventos

Um registro de ouro que nenhum sistema a jusante vê não ajuda ninguém. O padrão mais forte é a propagação orientada a eventos: quando uma entidade é criada, mesclada ou corrigida, o hub de MDM publica um evento de mudança, e os sistemas assinantes atualizam a cópia local. Isso se apoia na [arquitetura orientada a eventos](https://en.wikipedia.org/wiki/Event-driven_architecture) e nos padrões de streaming do capítulo 7.2, mantendo dezenas de sistemas consistentes sem sincronizações em lote noturnas frágeis que deixam todos um dia desatualizados.

Publiquem os eventos com contexto suficiente para serem úteis: o identificador da entidade, o que mudou, os novos valores sobreviventes e uma versão para que os consumidores possam ordenar as atualizações e detectar as que perderam. Tornem os consumidores idempotentes para que reproduzir um evento não cause dano e ofereçam uma API para os sistemas que não conseguem assinar. Aplica-se o princípio da arquitetura e armazenamento de dados (capítulo 3.4): projetem para que o registro de ouro flua, porque um que ninguém consome é só uma planilha cara.

### Atribua curadoria e governança antes das ferramentas

A MDM fracassa como projeto de tecnologia e tem sucesso como projeto de governança. O papel crítico é o [curador de dados](https://en.wikipedia.org/wiki/Data_steward) (data steward), uma pessoa responsável pela qualidade e pelas regras de um domínio específico, que resolve correspondências ambíguas, ajusta as regras de sobrevivência e arbitra quando dois departamentos discordam sobre o que significa “fornecedor”. Os curadores costumam ser pessoas de negócio com profundo conhecimento do domínio, não engenheiros, e precisam de autoridade real e tempo alocado, porque uma curadoria em tempo parcial e sem mandato produz exatamente a deriva que a MDM deveria deter.

Envolvam os curadores nas estruturas de governança do capítulo 7.1: um dono de dados responsável por cada domínio, um conselho para resolver disputas entre domínios e políticas claras sobre quem pode criar ou mesclar registros mestres. Documentem as decisões, porque as regras para corresponder um cliente são conhecimento institucional que precisa sobreviver à rotatividade de pessoal. A ferramenta serve à governança: comprar uma plataforma de MDM antes de nomear os curadores é comprar um motor sem motorista.

## Compromissos: prós e contras

| Estilo de MDM | Prós | Contras |
|---|---|---|
| Registro (apenas índice) | Barato, baixo risco, origens intocadas | Somente leitura. Não conserta os dados de origem |
| Consolidação (cópias centrais) | Registros limpos para análises rapidamente | As origens continuam bagunçadas. Sem escrita de volta |
| Coexistência (sincroniza de volta com as origens) | As origens melhoram. Controle equilibrado | Mais integração. Conflitos de sincronização a gerenciar |
| Hub centralizado / transacional | Consistência e controle mais fortes | Custo mais alto. Muda onde o trabalho acontece |
| Correspondência determinística | Previsível, explicável, auditável | Perde erros de digitação, variantes e dados bagunçados |
| Correspondência probabilística | Pega a variação do mundo real | Precisa de ajuste. Mesclas falsas se descuidada |

A tensão central da MDM é controle versus ruptura. Os estilos que dão os dados mais limpos e consistentes (coexistência e hubs centralizados) são exatamente os que mais interferem em como os sistemas de origem e seus donos trabalham, e essa interferência é onde os programas de MDM emperram. O caminho pragmático é ganhar confiança com um estilo de baixo risco e avançar para um controle mais forte apenas onde o argumento de negócio é claro. O compromisso da correspondência corre em paralelo: as regras determinísticas são auditáveis mas frágeis, a pontuação probabilística é poderosa mas exige curadoria e tolerância à mescla errada ocasional. A maioria dos programas maduros combina as duas.

## Perguntas para discutir com sua equipe

1. **Quais domínios de dados mestres de fato nos causam dor, e nós os classificamos por custo em vez de tratá-los todos de uma vez?** Muitos programas de MDM desabam sob a própria ambição, tentando dominar toda entidade da empresa de uma vez e não entregando nada por dois anos. O movimento produtivo é achar o um ou dois domínios em que a duplicação e o conflito custam dinheiro ou confiança de verdade, em geral cliente ou produto, e quantificar esse custo: as correspondências desperdiçadas, as horas de reconciliação, os números de receita errados, os achados de auditoria. Levem exemplos concretos da mesma entidade aparecendo de várias formas entre os seus sistemas e deixem essa classificação dizer onde começar, porque uma vitória estreita e mensurável constrói a credibilidade de que vocês precisam para se expandir.

2. **Quem é dono de cada domínio de dados mestres, e os nossos curadores têm a autoridade e o tempo para de fato fazer o trabalho?** A ferramenta de MDM sem uma curadoria empoderada é um carro sem motorista, e o modo de falha mais comum é nomear um curador num slide sem dar a ele nenhum mandato real nem horas alocadas. As pessoas que resolvem correspondências ambíguas e encerram as disputas sobre “o que conta como cliente” precisam de expertise de domínio, autoridade de decisão e tempo protegido. Levem o organograma e perguntem, para o seu principal domínio, exatamente quem decide quando dois registros são a mesma pessoa e quem arbitra quando vendas e finanças discordam. Se vocês não conseguem nomear essa pessoa e apontar o tempo alocado a ela, acharam a lacuna que afundará o programa.

3. **Quando mesclamos dois registros num registro de ouro, conseguimos explicar e reverter a decisão, e de onde vêm os valores sobreviventes?** As regras de sobrevivência são lógica de negócio que a maioria das equipes nunca escreveu, o que significa que as mesclas acontecem por acidente da ordem de carga ou de padrões da ferramenta, e uma mescla errada que funde dois clientes reais é dolorosa de desfazer. Levem um registro mesclado real e rastreiem cada campo sobrevivente até sua origem e regra: por que este endereço, por que este nome, por que este telefone. Confirmem que toda mescla é registrada e reversível e que uma faixa intermediária de correspondências incertas vai a um humano em vez de ser mesclada automaticamente. Se vocês não conseguem explicar um registro de ouro específico, os seus curadores não conseguem defendê-lo diante de um auditor ou de um cliente prejudicado.

4. **Que estilo de arquitetura de MDM serve a cada domínio que planejamos dominar, e conseguimos defender essa escolha contra a ruptura que ela impõe aos donos dos sistemas de origem?** O estilo que vocês escolhem decide o quanto conseguem limpar os dados e o quanto interferem nas equipes que são donas das origens, e escolher por moda ou pelo discurso de um fornecedor, e não pela realidade de controle versus ruptura, é como os programas emperram no meio do caminho. Um registro prova valor barato mas nunca conserta uma origem; um hub centralizado dá a consistência mais forte mas muda de lugar onde os registros são criados, o que é uma mudança organizacional disfarçada de técnica. Levem, para cada domínio candidato, uma leitura honesta de quanta autoridade vocês de fato têm sobre os donos das origens, quão frescas as cópias a jusante precisam ser e o que uma escrita de volta quebraria nos fluxos de trabalho existentes. Em contextos corporativos e governamentais, acrescentem o custo de migração e de gestão da mudança de mover o sistema de registro, porque as equipes cujo trabalho diário muda resistirão a um hub sobre o qual não foram consultadas, e uma implantação de coexistência emperrada é mais cara que um registro modesto que entrega.

5. **Como ajustamos os limiares de correspondência, e combinamos que taxa de mesclas falsas e de correspondências perdidas conseguimos tolerar em cada domínio?** Todo motor de correspondência probabilística troca mesclas falsas (fundir duas entidades reais) por correspondências perdidas (deixar uma entidade dividida), e o equilíbrio é uma decisão de negócio, não um padrão que alguém deixou na ferramenta. Se as faixas de mescla automática e de rejeição automática forem largas demais, vocês corrompem os registros de ouro em silêncio; se forem estreitas demais, a fila de revisão humana cresce mais depressa do que os curadores conseguem esvaziá-la. Levem a distribuição atual de confiança, o tamanho e a idade da fila de revisão e amostras de erros dos dois tipos para que a sala veja o custo real de cada direção. Num domínio governamental de identidade, errem com firmeza rumo às correspondências perdidas e à revisão humana, porque uma mescla errada pode negar um benefício ou expor os dados de um cidadão a outro, e o custo de recurso e de auditoria desse erro anula o custo de uma duplicata que um curador resolve na semana seguinte.

6. **Como os sistemas a jusante ficam sabendo que um registro de ouro mudou, e quão desatualizado cada um pode ficar antes que uma decisão dê errado?** Um registro de ouro perfeitamente resolvido que nenhum sistema consome é uma planilha cara, e o mecanismo de propagação, seja eventos de mudança, uma API de assinatura ou um lote noturno, define em silêncio quão atual é cada decisão dependente. A propagação orientada a eventos mantém dezenas de consumidores quase em tempo real mas exige consumidores idempotentes e eventos versionados; uma sincronização noturna é mais simples mas deixa todos um dia desatualizados, o que pode ser aceitável para uma lista de marketing e perigoso para uma verificação de fraude. Levem a lista dos sistemas consumidores, a atualidade de que cada um de fato precisa e como um consumidor que perde uma atualização hoje se recupera. Para uma organização grande ou pública, nomeiem quem é dono do contrato desses eventos e como um assinante detecta uma mensagem perdida, porque uma mudança de entidade que silenciosamente deixa de chegar a uma agência recria a própria fragmentação que a MDM foi financiada para remover.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e sem fôlego sobrando, não comprem uma plataforma de MDM. Dominem a única entidade que está corrompendo os seus números, em geral o cliente duplicado entre o autoatendimento e as vendas, com um job de correspondência no warehouse que vocês já operam e uma pessoa revisando as correspondências incertas semanalmente. Mantenham toda mescla registrada e reversível para que uma regra ruim custe uma tarde e não um relacionamento com um cliente, e revisitem ferramentas mais pesadas apenas quando a fila de revisão manual superar um único revisor.

**Pequena empresa.** Vocês não têm curador de dados e têm orçamento apertado, então tratem isto como uma decisão de comprar e não de construir e apoiem-se em padrões que vêm de graça. Prefiram ferramentas que já desduplicam contatos e falam os códigos ISO de país e de moeda a um hub sob medida que vocês não conseguem manter, e escolham o único domínio, tipicamente clientes ou produtos, em que as duplicatas custam dinheiro de verdade. Atribuam a responsabilidade a um dono nomeado, mesmo que seja uma fração da semana de uma pessoa, porque um vocabulário que deriva sem ninguém vigiando é o que quebra em silêncio os seus relatórios.

**Grande empresa.** Entre uma dúzia de sistemas de ERP e CRM acumulados por aquisições, o trabalho é governança de portfólio: classifiquem os domínios pelo custo da sua duplicação, montem curadores empoderados no negócio e padronizem as regras de sobrevivência e o versionamento dos dados de referência para que os grupos parem de resolver de novo o mesmo problema de correspondência. Orcem explicitamente a integração e o custo permanente da curadoria, propaguem os registros de ouro como eventos versionados para que as origens melhorem com o tempo e gerenciem a MDM como um programa medido, com taxas de duplicatas e métricas da fila de revisão, e não como uma limpeza pontual.

**Governo.** As regras de contratação, a lei estrita de compartilhamento de dados e a prestação de contas públicas moldam toda escolha. Identifiquem a entidade pessoa por um identificador nacional governado, versionem os dados de referência por data de vigência para que os registros históricos permaneçam corretos e tornem a resolução de identidade deliberadamente conservadora: as correspondências incertas vão a curadores treinados, nunca a mesclas automatizadas, porque uma mescla errada pode negar um benefício ou vazar os dados de um cidadão para outro. Registrem toda correspondência para auditoria e recurso, exijam dos fornecedores portabilidade de dados e divulgação da lógica de correspondência e mantenham toda a capacidade dentro dos padrões de interoperabilidade com que o setor público já se comprometeu.

## Exemplos

**Startup.** Uma empresa de software de rápido crescimento vende tanto por cadastro de autoatendimento quanto por uma equipe de vendas, e os dois canais criam o mesmo cliente duas vezes, com nomes de empresa ligeiramente diferentes. A receita por conta parece errada e a equipe de vendas continua ligando a frio para usuários existentes. Em vez de comprar uma plataforma pesada, começam com um registro leve: um job de correspondência no data warehouse que liga os registros por domínio de e-mail e nome de empresa normalizado, com um curador em tempo parcial revisando semanalmente as correspondências incertas. Custa pouco, conserta o erro de relatório e prova o valor que justifica mais investimento à medida que crescem.

**Grande empresa.** Um fabricante global cresceu por aquisições e roda uma dúzia de sistemas de ERP e CRM, cada um com seus registros de fornecedores, de modo que o mesmo fornecedor aparece de quinze maneiras e a empresa não consegue negociar como um único comprador nem ver seu gasto verdadeiro. Ela monta um hub de MDM em estilo de coexistência para os domínios de fornecedor e de produto, usando correspondência determinística em identificadores fiscais e de registro mais pontuação probabilística em nomes e endereços. Curadores nomeados em compras ajustam as regras de sobrevivência e trabalham a fila de revisão, e os registros de ouro são publicados como eventos de mudança que voltam para cada ERP, de modo que os dados limpos melhoram as origens. A visibilidade consolidada do gasto destrava condições contratuais melhores, e o imposto de reconciliação que consumia as finanças a cada trimestre cai bruscamente.

**Governo.** Um governo nacional quer que as agências tratem um cidadão como uma só pessoa e não como um estranho em cada balcão, respeitando limites legais estritos ao compartilhamento de dados. Ele constrói um hub centralizado de dados mestres para a entidade pessoa, identificada por um identificador nacional governado, com dados de referência versionados por data de vigência para que os registros históricos permaneçam corretos. A resolução de identidade é deliberadamente conservadora: as correspondências incertas vão a curadores treinados e não a mesclas automatizadas, porque uma mescla errada poderia negar um benefício a alguém ou expor seus dados, e toda correspondência é registrada para auditoria e recurso. O ganho são menos registros duplicados, menos fraude por identidades divididas e um cidadão que não precisa provar quem é em cada porta, dentro dos padrões de interoperabilidade do capítulo 3.8.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da MDM vem de remover um imposto que a maioria das organizações paga sem nomear. Registros duplicados e conflitantes custam dinheiro de modos óbvios (marketing desperdiçado com a mesma pessoa cinco vezes, erros de entrega por endereços obsoletos, descontos por volume perdidos) e de modos menos óbvios (analistas reconciliando contagens, executivos decidindo com números silenciosamente errados, auditores cobrando horas para desembaraçar qual registro é o real). Uma visão consolidada de fornecedores frequentemente paga o programa inteiro só por meio de melhores condições contratuais.

O custo total de propriedade tem três partes: a plataforma ou a construção, a integração com origens e consumidores e, a maior ao longo do tempo, a curadoria contínua. O custo de integração é fácil de subestimar, porque conectar uma dúzia de sistemas de origem envelhecidos é onde os programas de MDM sangram cronograma e orçamento, e o custo da curadoria é fácil de esquecer, porque é uma despesa operacional permanente e não uma construção pontual. Para defender o caso junto à liderança, liguem a MDM a números que ela já acompanha: exatidão da receita, eficiência do marketing, economia em compras, custo de auditoria e risco regulatório, e depois comecem estreito e deixem uma vitória medida num domínio de alta dor financiar a expansão.

## Antipadrões e armadilhas

- **Escopo de ferver o oceano:** dominar todos os domínios de uma vez, não entregar nada por anos e perder o patrocínio antes da primeira vitória.
- **Ferramenta antes da governança:** comprar uma plataforma de MDM antes de nomear curadores e donos, de modo que o motor fica sem motorista.
- **Curadores em tempo parcial sem autoridade:** atribuir a curadoria num slide sem dar mandato real nem tempo protegido.
- **Sobrevivência silenciosa:** mesclar registros por padrão da ferramenta ou ordem de carga, sem regras escritas e sem como explicar um registro de ouro.
- **Mesclas irreversíveis:** mesclar automaticamente correspondências incertas sem desfazer, de modo que uma fusão errada de duas entidades reais vira dano permanente.
- **Dados de referência sobrescritos no lugar:** editar listas de códigos sem versionamento, quebrando todo relatório histórico que estava correto sob os códigos antigos.
- **Registros de ouro que ninguém consome:** construir um hub impecável em que nenhum sistema a jusante se inscreve, de modo que os dados limpos nunca chegam às decisões.
- **Reinventar códigos padrão:** criar as próprias listas de país ou de moeda quando existem padrões ISO, perdendo interoperabilidade sem razão.

## Modelo de maturidade

- **Nível 1, Iniciar:** Os dados mestres e de referência não são gerenciados. A mesma entidade existe muitas vezes sem versão autoritativa, as listas de códigos divergem, a correspondência é manual e reativa e ninguém é dono do problema, então as contagens de entidades centrais discordam e ninguém sabe dizer qual está certa.
- **Nível 2, Desenvolver:** Os domínios-chave são reconhecidos e alguém os desduplica, muitas vezes no warehouse para relatórios. Existe correspondência determinística básica, as listas de referência são coletadas e algumas pessoas atuam como curadores informais, mas a prática varia de equipe para equipe, as origens continuam bagunçadas e as regras vivem na cabeça das pessoas e não no papel.
- **Nível 3, Padronizar:** A MDM é um programa governado, aplicado de modo consistente na organização. Os domínios mestres têm donos nomeados e curadores empoderados, as regras de correspondência e de sobrevivência são documentadas e impostas, os registros de ouro são produzidos e propagados aos consumidores, e os dados de referência são versionados e publicados com datas de vigência como uma API.
- **Nível 4, Gerenciar:** O programa é medido e controlado em relação a linhas de base. As taxas de duplicatas, as distribuições de confiança das correspondências, as taxas de mesclas falsas e de correspondências perdidas, a completude dos campos-chave e o tamanho e a idade da fila de revisão são acompanhados como métricas. Os limiares são ajustados contra esses números e não por intuição, e o valor da MDM (exatidão da receita, economia em compras, custo de revisão) é quantificado e relatado aos donos numa cadência fixa.
- **Nível 5, Orquestrar:** Os registros de ouro fluem como eventos versionados quase em tempo real, alimentam a camada semântica e são confiáveis em toda a organização. A correspondência é continuamente melhorada contra resultados medidos, o domínio se estende a novos domínios como uma capacidade repetível, e a MDM é integrada à governança e ao planejamento de riscos para que o programa se adapte conforme as origens, os padrões e o panorama de entidades mudam.

## Ideias para discussão

1. Se dois dos seus sistemas discordam sobre quantos clientes vocês têm, qual está certo, e como vocês provariam?
2. Que domínio de dados mestres entregaria a maior vitória mensurável se dominado primeiro, e quanto vale essa vitória?
3. Onde a correspondência probabilística ajudaria vocês hoje, e vocês estão à vontade com a mescla errada ocasional que ela implica?
4. Como vocês versionam seus dados de referência, e o que quebra nos relatórios históricos quando um código muda de significado?
5. Quem é o curador nomeado da sua entidade mais importante, e essa pessoa tem a autoridade e o tempo para de fato fazer o trabalho?
6. Quando um registro de ouro muda, como os seus sistemas a jusante ficam sabendo, e quão desatualizados podem ficar antes de doer?

## Principais conclusões

- Classifiquem os dados em mestres, de referência e transacionais. Invistam correspondência e governança onde a duplicação custa mais.
- Produzam um registro de ouro por entidade do mundo real, montado por regras de sobrevivência explícitas, reversíveis e registradas.
- Escolham um estilo de arquitetura de MDM (registro, consolidação, coexistência ou hub centralizado) que se ajuste ao seu apetite por controle e ruptura.
- Tratem os dados de referência como vocabulário compartilhado e versionado, prefiram padrões reconhecidos e nunca sobrescrevam listas de códigos no lugar.
- A MDM tem sucesso pela governança e pela curadoria, não pela ferramenta. Propaguem os registros de ouro como eventos e meçam o programa por decisões melhoradas.

## Referências e leitura complementar

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
