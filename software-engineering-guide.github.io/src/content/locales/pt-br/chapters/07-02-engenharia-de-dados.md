# 7.2 Engenharia de dados

## Visão geral e motivação

A [engenharia de dados](https://en.wikipedia.org/wiki/Data_engineering) é a disciplina de construir e operar os pipelines e as plataformas que levam os dados de onde são produzidos até onde criam valor. Cobre a ingestão a partir dos sistemas de origem, a transformação em formas limpas e modeladas, o armazenamento em formatos econômicos, a orquestração do fluxo inteiro e as práticas de confiabilidade que mantêm tudo isso confiável. Se a estratégia de dados decide que dados devem existir e quem é dono deles, a engenharia de dados é o encanamento e a maquinaria que os faz fluir.

Para grandes equipes, essa disciplina é fundamental. As análises, a [inteligência de negócio](https://en.wikipedia.org/wiki/Business_intelligence), a experimentação de produto, o [aprendizado de máquina](https://en.wikipedia.org/wiki/Machine_learning) e os relatórios regulatórios ficam todos a jusante dos pipelines de dados. Quando esses pipelines são frágeis, lentos ou opacos, toda função dependente sofre. Os painéis mostram números obsoletos. Os modelos treinam com atributos corrompidos. Os auditores não conseguem reconstruir como um número foi produzido. Em escala corporativa e governamental, os pipelines processam bilhões de registros de muitos sistemas de origem, e uma única falha silenciosa pode empurrar dados errados para decisões, pagamentos ou estatísticas públicas.

O campo cresceu a partir de scripts sob medida e de ferramentas monolíticas de [ETL (extrair, transformar, carregar)](https://en.wikipedia.org/wiki/Extract,_transform,_load) até a pilha moderna de dados: componentes modulares, em grande parte guiados por SQL, para ingestão, transformação, orquestração e armazenamento, conectados por formatos abertos. Essa modularidade é ao mesmo tempo um presente e uma armadilha. Permite montar as melhores ferramentas de cada categoria, mas sem disciplina de engenharia produz uma dispersão de jobs sem documentação e sem testes. Este capítulo cobre as práticas que mantêm os pipelines idempotentes, testáveis, observáveis e acessíveis em escala.

## Princípios fundamentais

- Os pipelines são software e merecem controle de versões, testes, revisão e CI/CD.
- Prefiram transformações idempotentes e reproduzíveis que possam ser reexecutadas com segurança.
- Tornem os fluxos de dados observáveis: atualidade, volume, esquema e qualidade são monitorados.
- Modelem os dados deliberadamente para seus consumidores em vez de despejar tabelas brutas.
- Escolham batch ou streaming com base em necessidades reais de latência, não em novidade.
- Otimizem formato de armazenamento, particionamento e custo de computação como preocupações de primeira classe.
- Separem ingestão, transformação e disponibilização para que cada uma evolua de forma independente.
- Falhem alto e cedo: um pipeline quebrado é mais seguro que dados errados em silêncio.

## Recomendações

### Escolha ETL ou ELT deliberadamente

O ETL transforma os dados antes de carregá-los no destino. O [ELT (extrair, carregar, transformar)](https://en.wikipedia.org/wiki/Extract,_load,_transform) carrega primeiro os dados brutos e os transforma dentro de um warehouse ou lakehouse poderoso. As plataformas modernas de nuvem fizeram do ELT o padrão, porque o armazenamento é barato e a computação é elástica, e guardar os dados brutos permite reprocessar quando a lógica muda ou surgem bugs. Prefiram o ELT para cargas de análise: depositem dados brutos imutáveis e depois construam transformações em camadas por cima. Reservem a transformação pré-carga para os casos em que privacidade, custo ou restrições contratuais exijam limpar ou filtrar os dados antes de eles chegarem.

### Projete pipelines batch e de streaming para suas necessidades de latência

A maioria das necessidades de análise é bem atendida por pipelines batch agendados, que são mais simples de raciocinar, testar e reprocessar. Recorram ao streaming apenas quando o negócio realmente precisa de dados de baixa latência: detecção de fraude, alertas operacionais, personalização em tempo real. O streaming acrescenta complexidade real em torno de ordenação, semântica de exatamente-uma-vez, dados que chegam atrasados e gestão de estado. Onde precisarem de ambos, considerem arquiteturas que unifiquem a lógica de batch e de streaming em vez de manter duas bases de código divergentes. Sejam honestos sobre seus requisitos de latência. “Tempo real” costuma ser um desejo não examinado que dobra o seu custo.

### Orquestre com dependências explícitas

Usem um orquestrador para expressar os pipelines como [grafos acíclicos dirigidos (DAGs)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) de tarefas com dependências explícitas, novas tentativas e agendamento. Isso dá visibilidade sobre o que rodou, o que falhou e o que está bloqueado, além da capacidade de reprocessar e reexecutar de forma determinística. Baseiem as dependências na disponibilidade dos dados, não apenas no horário do relógio, para que os jobs a jusante esperem os dados a montante em vez de disparar por palpite. Mantenham a lógica de orquestração em controle de versões e tratem as mudanças de DAG como mudanças de código.

### Modele os dados para o consumo

As tabelas brutas raramente servem aos analistas. Apliquem a [modelagem dimensional](https://en.wikipedia.org/wiki/Dimensional_modeling), que organiza fatos e dimensões conformadas em [esquemas estrela](https://en.wikipedia.org/wiki/Star_schema), onde vocês precisam de análises governadas, reutilizáveis e de autoatendimento. As tabelas largas e desnormalizadas (“uma tabela grande”) podem render mais em certos padrões de consulta e são mais simples para alguns consumidores, ao custo de duplicação e flexibilidade. Estratifiquem as transformações em camadas: uma camada de preparação bruta, uma camada central limpa e conformada e data marts voltados ao consumidor. Essa separação permite corrigir a lógica num só lugar e permite que os consumidores dependam de interfaces estáveis.

### Torne os pipelines idempotentes e testáveis

Projetem as transformações para que reexecutá-las produza o mesmo resultado, em vez de duplicar ou corromper dados, por exemplo usando upserts determinísticos baseados em identificadores de negócio e padrões de sobrescrita de partição. Escrevam testes em vários níveis: testes de unidade para a lógica de transformação, testes de esquema e testes de dados que afirmam expectativas como unicidade, chaves não nulas, integridade referencial e faixas de valores aceitas. Rodem-nos no CI, para que uma mudança ruim seja pega antes de chegar aos dados de produção.

### Instrumente observabilidade e confiabilidade

Monitorem os quatro sinais centrais da saúde dos dados: atualidade (está em dia), volume (a contagem de linhas está na faixa esperada), esquema (a estrutura mudou de forma inesperada) e distribuição (os valores derivaram de forma anômala). Alertem sobre violações e encaminhem-nas à equipe dona. Mantenham runbooks, rodízios de sobreaviso e revisões pós-incidente sem atribuição de culpa para os incidentes de dados, assim como fariam para os serviços. Acompanhem a linhagem, para que, quando algo quebrar, vocês vejam o impacto a jusante de imediato.

### Otimize o armazenamento e o custo

Usem formatos colunares abertos como o Parquet, ou formatos abertos de tabela que suportem evolução de esquema, viagem no tempo e atualizações eficientes. Particionem os dados pelas colunas em que mais filtram, tipicamente a data, e evitem a proliferação de arquivos minúsculos por meio de compactação. Separem dados quentes e frios com armazenamento em camadas e políticas de ciclo de vida. Monitorem o gasto de computação por pipeline e por consulta. Custos descontrolados costumam vir de varreduras completas, partições ausentes e reprocessamento sem limites. Tratem o custo como uma métrica com donos, não como uma surpresa na conta mensal.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| ELT (transformar no destino) | Guarda dados brutos, armazenamento barato, reprocessável | Grande pegada de armazenamento, exige governança | Análises em nuvem |
| ETL (transformar antes de carregar) | Controla o custo, filtra dados sensíveis cedo | Perde o bruto, mais difícil de reprocessar | Cargas reguladas ou restritas |
| Batch | Simples, testável, reprocessamento fácil | Maior latência | A maioria das análises |
| Streaming | Baixa latência, reação em tempo real | Complexo, caro, difícil de testar | Fraude, alertas operacionais |
| Esquema estrela | Governado, reutilizável, amigável ao autoatendimento | Esforço de modelagem inicial | BI compartilhada |
| Tabela larga | Rápida para consultas conhecidas, simples | Duplicação, menos flexível | Uso estreito de alto desempenho |

O compromisso dominante é simplicidade versus latência e flexibilidade. O batch e o ELT com esquemas estrela em camadas dão um sistema testável, reprocessável e bem compreendido que atende à maioria das necessidades a um custo acessível. O streaming, o tempo real e os desenhos altamente desnormalizados compram velocidade e desempenho específico, mas a um custo alto em complexidade operacional e dificuldade de teste. Adotem complexidade apenas onde um requisito concreto de negócio a paga e mantenham o caminho simples como padrão.

## Perguntas para discutir com sua equipe

1. **Vocês escolheram deliberadamente o ELT em vez do ETL e estão guardando dados brutos imutáveis para poder reprocessar quando a lógica muda ou aparecem bugs?** O padrão do capítulo é o ELT: depositar dados brutos de forma barata e depois construir transformações em camadas, porque guardar o bruto permite reexecutar tudo quando uma regra muda ou um bug aparece semanas depois. Apagar o bruto elimina essa opção e é uma armadilha comum e dolorosa. O argumento concorrente a favor do ETL é real em cargas reguladas ou restritas, onde privacidade, custo ou termos contratuais exigem filtrar ou mascarar os dados antes de eles chegarem. Levem evidências: com que frequência vocês precisaram reprocessar o histórico e quanto custou quando não puderam? Para um pipeline governamental ou corporativo que precisa rastrear qualquer número até a origem, os registros brutos imutáveis também são uma exigência de auditabilidade, então a resposta molda tanto a sua política de armazenamento quanto a sua defensabilidade jurídica.

2. **Quais dos quatro sinais de saúde dos dados vocês de fato monitoram, e quem é acionado quando um quebra?** O capítulo nomeia quatro sinais que valem ser vigiados: atualidade, volume, esquema e distribuição. Muitas equipes não monitoram nenhum e descobrem as falhas por um executivo encarando um painel obsoleto, que é o pior detector possível. Em escala corporativa e governamental, uma única falha silenciosa pode empurrar dados errados para pagamentos, relatórios ou estatísticas públicas, então o custo da detecção tardia se mede em confiança e dinheiro, não só em retrabalho. Levem o seu tempo médio real de detecção e o nome de quem hoje acha os incidentes primeiro. Se a resposta é “um consumidor”, vocês precisam de alertas encaminhados à equipe dona, mais runbooks e revisões pós-incidente sem atribuição de culpa, tratando os incidentes de dados exatamente como interrupções de serviço.

3. **Os seus analistas consomem data marts modelados e testados, ou vocês despejam tabelas brutas sobre eles e chamam de autoatendimento?** O capítulo é direto: as tabelas brutas raramente servem aos analistas, e estratificar as transformações numa camada bruta de preparação, um núcleo conformado e data marts voltados ao consumidor permite corrigir a lógica uma só vez e dar aos consumidores interfaces estáveis. A atração concorrente é a velocidade, já que modelar com esquemas estrela ou tabelas largas deliberadas custa esforço inicial e é tentador pulá-lo. Mas despejar dados brutos empurra o custo da modelagem para cada analista repetidamente, produzindo números divergentes e horas desperdiçadas. Levem um sinal: que fração do tempo dos analistas vai para remodelar dados brutos e quantas equipes reconstruíram os mesmos joins. Se o número é alto, invistam numa camada central conformada para que os consumidores dependam de interfaces testadas e reutilizáveis em vez de reinventá-las.

4. **Onde o “tempo real” realmente merece o seu custo, e onde é um desejo não examinado que silenciosamente dobra a sua carga operacional?** O padrão do capítulo é o batch agendado, que é mais simples de raciocinar, testar e reprocessar, com o streaming reservado aos casos em que o negócio de fato precisa de baixa latência, como a detecção de fraude ou os alertas operacionais. A atração concorrente é o prestígio e os pedidos vagos de partes interessadas por dados “ao vivo”, que soam baratos numa reunião de planejamento e ficam caros em produção, porque o streaming arrasta ordenação, semântica de exatamente-uma-vez, dados que chegam atrasados e gestão de estado, além de uma segunda base de código a manter em compasso com a lógica do batch. Levem evidências à discussão: para cada pipeline de streaming que vocês operam ou propõem, nomeiem a decisão que ele alimenta e a latência que essa decisão de fato tolera, medida em minutos ou horas e não em adjetivos. Para uma grande plataforma corporativa ou governamental, acrescentem o custo de sobreaviso e de teste de cada caminho em tempo real, porque um pipeline de streaming que ninguém consegue testar nem cobrir com escala 24 horas é um passivo de confiabilidade disfarçado de funcionalidade, e a resposta honesta muitas vezes reduz um requisito de “tempo real” a um batch horário que serve à mesma decisão.

5. **Quais dos seus pipelines não poderiam ser reexecutados com segurança hoje, e o que seria preciso para tornar toda transformação idempotente?** O capítulo insiste em transformações idempotentes e reproduzíveis, usando upserts determinísticos baseados em identificadores de negócio e padrões de sobrescrita de partição, para que uma reexecução produza o mesmo resultado em vez de duplicar ou corromper dados. A pressão concorrente é a velocidade de entrega, já que um job ingênuo, só de acréscimo, sai mais rápido que um projetado para ser reexecutável, e o custo desse atalho fica escondido até uma falha forçar uma reexecução parcial às 2 da manhã e alguém contar a receita em dobro. Levem um inventário concreto: listem os jobs que corromperiam dados se reexecutados a partir de um ponto de falha e estimem o raio de impacto do pior deles. Em escala corporativa e governamental, onde uma única falha silenciosa pode empurrar dados errados para pagamentos, relatórios ou estatísticas públicas, o processamento não idempotente não é meramente inconveniente: ele mina a auditabilidade que permite reprocessar um período depois de uma mudança de regra e ainda rastrear cada número até a origem, então financiar o retrabalho para tornar seguras as reexecuções é uma questão de controle, não apenas de arrumação.

6. **Vocês sabem quanto custa rodar cada pipeline, quem é dono desse número e quanto da sua conta de nuvem vem de varreduras completas e partições ausentes?** O capítulo trata formato de armazenamento, particionamento e gasto de computação como preocupações de primeira classe com donos, alertando que custos descontrolados costumam vir de varreduras completas, partições ausentes e reprocessamento sem limites. A consideração concorrente é que o trabalho de custo parece menos urgente que entregar funcionalidades, então é adiado até a conta mensal virar uma surpresa e as finanças começarem a fazer perguntas que a engenharia não sabe responder. Levem evidências: o gasto por pipeline e por consulta, a fração do custo vinda de varreduras sem partição e a contagem de arquivos minúsculos que deveriam ser compactados. Para uma grande organização que roda bilhões de registros de muitos sistemas de origem, uma conta de nuvem sem dono cresce sem que nenhuma equipe se sinta responsável, e em contextos governamentais o gasto público precisa ser justificado linha a linha, então atribuir o custo de computação a um dono nomeado com uma métrica acompanhada transforma uma despesa opaca numa gerida e muitas vezes revela economias grandes o bastante para financiar o próximo investimento em plataforma.

## Perspectiva por setor

**Startup.** A velocidade vence a arquitetura. Liguem a ingestão a um conector gerenciado, construam um punhado de transformações em controle de versões e rodem-nas num orquestrador leve que tenta de novo e reprocessa sozinho, em vez de montar à mão jobs de cron que quebram em silêncio durante a noite. Mantenham todo modelo idempotente desde o primeiro commit e acrescentem alguns testes baratos para chaves nulas e contagens de linhas, para que uma mudança ruim na origem falhe no CI em vez de aparecer no painel de segunda-feira do fundador. Não montem streaming nem uma plataforma sob medida: o seu recurso mais escasso é a atenção da engenharia.

**Pequena empresa.** Sem engenheiro de dados dedicado, prefiram comprar uma pilha integrada a montar uma. Um serviço gerenciado de ELT mais um warehouse em nuvem dão conectores, agendamento e armazenamento sem uma equipe de plataforma para mantê-los. Enquadrem a escolha como higiene de dados e não como um projeto de pipeline: saibam quais sistemas de origem alimentam os seus relatórios, guardem os dados brutos para que um número errado possa ser rastreado e reprocessado e escolham ferramentas de custo previsível para que uma varredura de tabela inteira não estoure o orçamento mensal.

**Grande empresa.** O problema é a consistência entre muitas equipes e bilhões de registros de muitos sistemas de origem. Padronizem o padrão ELT, o modelo em camadas de preparação, núcleo e mart e os quatro sinais de saúde dos dados para que os grupos parem de reinventar pipelines frágeis. Imponham testes de dados e CI em todo modelo, atribuam o custo de computação às equipes donas e passem os incidentes de dados pela mesma disciplina de sobreaviso, runbook e revisão pós-incidente sem atribuição de culpa que usam para os serviços, para que uma falha silenciosa nunca chegue a um painel sem ser notada.

**Governo.** As regras de contratação, a transparência e a prestação de contas públicas moldam o pipeline. Depositem registros brutos imutáveis para auditabilidade, transformem-nos em estágios testados e em camadas e mantenham a linhagem completa para que um auditor possa rastrear qualquer número publicado até seus documentos de origem, muitas vezes uma exigência legal. O processamento idempotente permite reprocessar uma declaração ou um período de relatório com segurança quando uma regra muda, e favorecer formatos abertos e código de transformação portável evita que vocês fiquem presos a um único fornecedor ao longo de um contrato de vários anos.

## Exemplos

**Startup.** Uma startup de análises de dez pessoas tinha crescido um emaranhado de jobs de cron que quebravam em silêncio durante a noite e às vezes contavam linhas em dobro quando um engenheiro reexecutava um à mão. A equipe migrou para um conector gerenciado de ingestão, um framework de transformação para modelos em controle de versões e um orquestrador leve que tenta de novo e reprocessa sozinho. Tornaram todo modelo idempotente e acrescentaram um punhado de testes para chaves nulas e contagens de linhas, de modo que uma mudança ruim na origem agora falha no CI em vez de aparecer no painel de segunda-feira do fundador.

**Grande empresa.** Uma varejista global substituiu centenas de scripts de extração escritos à mão por uma pilha ELT. Conectores gerenciados depositam os dados brutos de origem, um framework de transformação constrói modelos testados e versionados num lakehouse e um orquestrador gerencia as dependências com novas tentativas e reprocessamentos. Testes de dados pegam a deriva de esquema dos sistemas de origem antes de ela chegar aos painéis. O armazenamento colunar particionado cortou substancialmente os custos de consulta, ao mesmo tempo que melhorou a atualidade de diária para horária.

**Governo.** Uma autoridade tributária ingere declarações e dados de terceiros por um pipeline governado que deposita registros brutos imutáveis para auditabilidade e depois os transforma em estágios testados e em camadas. O processamento idempotente permite reprocessar com segurança um período de declaração quando uma regra muda. A linhagem completa permite aos auditores rastrear qualquer número calculado até os documentos de origem, uma exigência legal de prestação de contas públicas.

## Justificativa de negócio: motivações, ROI e TCO

O ROI da engenharia de dados disciplinada vem de confiabilidade, velocidade e controle de custos. Pipelines confiáveis significam que decisões e relatórios repousam em dados confiáveis, evitando o retrabalho caro e o dano à reputação de números errados. Pipelines modulares e testados permitem que as equipes entreguem novos produtos de dados mais depressa, compondo o valor de cada investimento em análise e ML a jusante. Otimizar armazenamento e computação reduz diretamente a conta de nuvem, muitas vezes em margens grandes assim que o particionamento e os padrões de consulta são corrigidos.

O custo de adoção inclui ferramentas de plataforma, tempo de engenharia para construir pipelines modulares e testados e a disciplina de tratar os dados como software. Pesem isso contra o custo de não adotar: jobs frágeis e sob medida que só o autor entende, corrupção silenciosa de dados descoberta por executivos, gasto de nuvem inflado por varreduras de tabela inteira e analistas bloqueados esperando por dados. À liderança, enquadrem a engenharia de dados como a fundação que torna as análises, a BI e a IA confiáveis e acessíveis. Se investirem pouco aqui, vocês limitam o retorno de toda iniciativa de dados acima.

## Antipadrões e armadilhas

- Pipelines construídos como scripts avulsos, sem controle de versões, testes nem revisão.
- Jobs não idempotentes que duplicam ou corrompem dados quando reexecutados após uma falha.
- Adotar o streaming por prestígio quando o batch atenderia ao requisito de latência.
- Despejar tabelas brutas sobre os analistas e chamar de autoatendimento.
- Nenhuma observabilidade, de modo que as falhas são descobertas pelos consumidores a jusante.
- Ignorar particionamento e tamanho de arquivos até a conta de nuvem explodir.
- Acoplar ingestão, transformação e disponibilização de modo que nada possa mudar com segurança.
- Apagar os dados brutos, tornando impossível reprocessar quando a lógica muda.

## Modelo de maturidade

1. Iniciar: Scripts ad hoc e execuções manuais, sem testes nem monitoramento. As falhas são descobertas pelos consumidores a jusante, os jobs não podem ser reexecutados com segurança e os custos de nuvem são não gerenciados e sem atribuição.
2. Desenvolver: Algumas equipes adotaram um orquestrador e puseram transformações básicas em controle de versões, mas a prática é inconsistente na organização. Existem testes ocasionais, a idempotência é irregular e pipelines quebrados ainda significam combate reativo a incêndios.
3. Padronizar: O ELT com um modelo em camadas de preparação, núcleo e mart, testado e versionado, é o padrão documentado aplicado entre as equipes. Dependências orquestradas com novas tentativas e reprocessamentos, testes de dados rodando no CI e convenções compartilhadas de modelagem em esquema estrela e de particionamento são impostos em toda a organização e não deixados a cada grupo.
4. Gerenciar: A plataforma é medida e controlada. Atualidade, volume, esquema e distribuição são monitorados com alertas encaminhados às equipes donas, e os SLAs de pipeline, o tempo médio de detecção, as taxas de aprovação de qualidade dos dados e o custo de computação por pipeline e por consulta são acompanhados contra linhas de base. Os limiares de reversão e de interrupção são impostos com base em evidências, e custo e confiabilidade têm donos nomeados cobrados por metas.
5. Orquestrar: Os pipelines são tratados plenamente como software, com CI/CD, contratos de dados e detecção automatizada de anomalias que pega a deriva antes dos consumidores. A lógica de batch e de streaming é unificada onde a latência realmente compensa, a plataforma é continuamente melhorada e de autoatendimento, e a capacidade, as camadas de armazenamento e o custo são reequilibrados de forma adaptativa conforme as cargas mudam, para que novos produtos de dados sejam entregues rapidamente sobre uma fundação estável.

## Ideias para discussão

- Onde, na sua pilha, o “tempo real” realmente merece o seu custo, e onde é ilusão?
- Quais pipelines não poderiam ser reexecutados com segurança hoje, e o que seria preciso para corrigir isso?
- Quanto da sua conta de dados na nuvem vem de varreduras completas e partições ausentes?
- Os seus analistas consomem data marts modelados ou tabelas brutas, e quanto isso lhes custa?
- Qual é o seu tempo médio de detecção de um incidente de dados, e quem o encontra primeiro?
- Unificar a lógica de batch e de streaming reduziria a sua carga de manutenção ou acrescentaria risco?

## Principais conclusões

- Tratem os pipelines como software: controle de versões, testes, revisão, CI/CD e observabilidade.
- Prefiram o ELT com modelos em camadas e testados. Guardem os dados brutos para reprocessamento.
- Escolham batch por padrão e streaming apenas onde a latência realmente compensa.
- Tornem as transformações idempotentes para que as reexecuções sejam seguras.
- Modelem os dados para os consumidores com esquemas estrela ou tabelas largas deliberadas.
- Monitorem atualidade, volume, esquema e distribuição e tratem os incidentes de dados como interrupções.
- Otimizem formatos de armazenamento, particionamento e custo de computação como preocupações de primeira classe.

## Referências e leitura complementar

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
