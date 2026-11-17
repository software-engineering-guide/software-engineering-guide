# 7.1 Estratégia e governança de dados

## Visão geral e motivação

A estratégia de dados é o seu plano deliberado para tratar os dados como um ativo: como são produzidos, descritos, possuídos, protegidos, compartilhados e consumidos para criar valor. A [governança de dados](https://en.wikipedia.org/wiki/Data_governance) é o sistema operacional que torna a estratégia real: os papéis, as políticas, os padrões e os controles que mantêm os dados confiáveis e em conformidade ao longo do tempo. Em equipes pequenas essas preocupações costumam ser implícitas, carregadas na cabeça de poucos engenheiros. Na escala das grandes organizações de desenvolvimento, das empresas e das agências governamentais, essa informalidade desmorona. Centenas de equipes produzem milhares de tabelas. Dezenas de sistemas reivindicam guardar o registro “real” do cliente. E ninguém sabe dizer com confiança qual número está correto numa apresentação ao conselho ou num relatório público.

Para grandes equipes, o custo da má governança de dados não é abstrato. Os reguladores esperam linhagem e controle demonstráveis sobre dados pessoais, financeiros e de saúde sob regimes como o [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (o Regulamento Geral de Proteção de Dados da UE), o [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (a lei americana de portabilidade e responsabilidade de seguros de saúde) e regras setoriais. As empresas enfrentam exposição financeira direta por métricas relatadas de forma errada, auditorias malsucedidas e plataformas de dados duplicadas. As agências governamentais carregam obrigações adicionais de retenção de registros, de acesso à informação, de prestação de contas públicas e de tratamento equitativo dos cidadãos. Em cada um desses contextos, dados em que vocês não podem confiar são piores que nenhum dado, porque conduzem a decisões confiantes e erradas.

A ideia que impulsiona o progresso em escala é simples: tratem os dados como um produto. Em vez de os dados serem um subproduto residual das aplicações, cada conjunto importante de dados tem um dono, uma interface documentada, garantias de qualidade e consumidores tratados como clientes. Este capítulo cobre essa mentalidade de produto junto com as disciplinas clássicas de governança: curadoria, catalogação, [gestão de dados mestres](https://en.wikipedia.org/wiki/Master_data_management) e qualidade. Cobre também as escolhas organizacionais que determinam qual modelo se ajusta à sua equipe: uma [malha de dados](https://en.wikipedia.org/wiki/Data_mesh) (data mesh; dados descentralizados, de propriedade dos domínios, publicados como produtos), um data lakehouse (gestão e governança no estilo de armazém sobrepostas a um flexível [data lake](https://en.wikipedia.org/wiki/Data_lake)) e um [data warehouse](https://en.wikipedia.org/wiki/Data_warehouse) (um repositório central governado de dados modelados e prontos para consulta).

*Veja também:* capítulo 4.5 (privacidade e proteção de dados), capítulo 7.2 (engenharia de dados) e capítulo 4.6 (conformidade e governança).

## Princípios fundamentais

- Os dados são um ativo durável com donos, não um subproduto descartável das aplicações.
- Todo conjunto importante de dados tem um dono responsável nomeado e um contrato documentado.
- A governança viabiliza o uso confiável. Não é um portão burocrático que só diz não.
- Deve haver uma fonte autoritativa para cada entidade de negócio crítica.
- Qualidade, privacidade e linhagem são projetadas desde o início, não inspecionadas depois.
- Os consumidores dos dados são clientes cujas necessidades moldam o produto.
- As políticas são codificadas e impostas automaticamente sempre que possível, não deixadas à boa vontade.
- A propriedade federada escala melhor que uma única equipe central à medida que a organização cresce.

## Recomendações

### Trate os dados como um produto

Deem a cada conjunto significativo de dados um dono de produto responsável por sua adequação ao uso. Um produto de dados tem um nome, um esquema documentado, uma descrição de seu significado e de sua procedência, uma cadência de atualização definida e expectativas de qualidade publicadas. Os seus consumidores devem poder descobri-lo, entendê-lo e depender dele sem fazer uma única pergunta à equipe produtora. Apliquem a mesma disciplina que aplicam às APIs de software: versionamento, avisos de descontinuação, registros de mudanças e compatibilidade retroativa.

### Estabeleça contratos de dados e SLAs

Um contrato de dados é um acordo explícito e verificável por máquina entre um produtor e seus consumidores. Cobre esquema, semântica, atualidade, volume e mudanças permitidas. Imponham os contratos no pipeline para que uma mudança incompatível a montante falhe cedo na origem, em vez de corromper em silêncio os relatórios a jusante semanas depois. Combinem os contratos com acordos e objetivos de nível de serviço. Por exemplo: “dimensão de clientes atualizada até as 06:00 diariamente, em 99,5% dos dias, com menos de 0,1% de chaves de negócio nulas”. Publiquem-nos e alertem sobre violações.

### Construa a curadoria e um modelo operacional de governança

Mantenham a responsabilização separada da execução. Os donos dos dados (muitas vezes líderes de negócio) respondem por um domínio. Os curadores de dados (especialistas no assunto) mantêm as definições, resolvem problemas de qualidade e aprovam acessos. Um conselho enxuto de governança de dados define os padrões transversais e resolve disputas. Mantenham o modelo federado: uma equipe central de capacitação fornece ferramentas, padrões e mentoria, enquanto as equipes de domínio são donas de seus dados. Isso evita tanto o gargalo da centralização total quanto o caos da ausência total de governança.

### Invista num catálogo de dados e na linhagem

Um catálogo pesquisável é a porta de entrada do seu patrimônio de dados. Deve conter glossários de negócio, esquemas técnicos, propriedade, classificações de sensibilidade, pontuações de qualidade e linhagem de ponta a ponta, do sistema de origem passando pelas transformações até os painéis. Automatizem a coleta de metadados em vez de depender de documentação manual, que apodrece rápido. A linhagem é essencial para a análise de impacto, a resposta a incidentes, a auditoria e as solicitações regulatórias, como o acesso e a exclusão pelo titular dos dados.

### Gestão de dados mestres e uma fonte única da verdade

Para as entidades centrais (cliente, cidadão, produto, fornecedor, funcionário), usem a gestão de dados mestres para reconciliar duplicatas e registros conflitantes num registro de ouro. Escolham uma arquitetura (registro, consolidação, coexistência ou centralizada) conforme quão autoritativo o hub precisa ser. Definam explicitamente as regras de correspondência e de sobrevivência e tornem-nas auditáveis. Uma [fonte única da verdade](https://en.wikipedia.org/wiki/Single_source_of_truth) previne a falha clássica em que finanças, vendas e operações relatam, cada uma, uma receita diferente.

### Meça a qualidade dos dados por dimensões

Gerenciem a qualidade ao longo de dimensões nomeadas: exatidão, completude, consistência, atualidade, validade e unicidade. Instrumentem os pipelines com testes automatizados e observabilidade contínua dos dados (verificações de atualidade, volume, deriva de esquema e distribuição) para pegar as anomalias antes que os consumidores sejam afetados. Tratem os incidentes de dados como interrupções de produção, com detecção, triagem, análise de causa raiz e revisões pós-incidente.

### Classifique, proteja e controle o acesso

Classifiquem os dados por sensibilidade e apliquem controles proporcionais: criptografia, mascaramento, tokenização, segurança em nível de linha e de coluna e acesso de menor privilégio revisado regularmente. Mantenham um cronograma de retenção e exclusão que satisfaça tanto as exigências de minimização quanto a lei de retenção de registros. Em contextos governamentais, reconciliem deliberadamente as obrigações de transparência com as proteções de privacidade, em vez de caso a caso.

## Compromissos: prós e contras

| Abordagem | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| Equipe central de governança | Padrões consistentes, responsabilização clara | Gargalo, desconectada dos domínios | Organizações pequenas ou muito reguladas |
| Governança federada | Escala, conhecimento do domínio, propriedade | Exige ferramentas e cultura fortes | Grandes empresas multidomínio |
| Data warehouse | Maduro, governado, SQL de bom desempenho | Rígido, caro para dados não estruturados | Cargas estáveis centradas em BI |
| Data lakehouse | Flexível, unificado, trata todos os tipos de dados | Ferramentas mais jovens, esforço de governança | Análises mistas e ML |
| Malha de dados | Propriedade pelo domínio, escala organizacionalmente | Exigência alta de maturidade, custo de coordenação | Organizações muito grandes e descentralizadas |

A governança sempre troca velocidade por confiança. A governança leve deixa as equipes andarem depressa, até uma auditoria, uma violação ou um relatório errado constrangedor forçar um acerto de contas caro. A governança pesada protege a confiança mas pode sufocar a experimentação e empurrar as equipes para sistemas paralelos. A resposta durável é codificar a governança como guardrails automatizados e de autoatendimento, para que o caminho em conformidade seja também o caminho fácil. Arquiteturalmente, os warehouses favorecem a simplicidade governada, a malha favorece a escala organizacional e os lakehouses ficam no meio-termo. A escolha certa segue a estrutura da sua organização muito mais que qualquer benchmark técnico.

## Perguntas para discutir com sua equipe

1. **Que arquitetura de dados (warehouse, lakehouse ou malha) de fato se ajusta à estrutura da sua organização, e vocês são honestos sobre a exigência de maturidade que cada uma impõe?** A tabela de compromissos deixa claro que essa escolha segue a estrutura organizacional, não benchmarks: um warehouse recompensa cargas estáveis centradas em BI, um lakehouse trata análises mistas e ML e uma malha escala por muitos domínios autônomos mas exige alta maturidade e ferramentas fortes. Para uma grande empresa ou agência governamental com dezenas de domínios, saltar para uma malha antes de ter plataformas de autoatendimento e uma cultura de governança produz caos vestido de descentralização. Levem sinais concretos: quantos domínios produzem dados, se as equipes centrais já são um gargalo e se as equipes de domínio têm habilidade e incentivo para ser donas de produtos. Se hoje vocês não têm ferramentas federadas, a resposta honesta pode ser um warehouse ou lakehouse governado agora e uma malha depois. Escolham o modelo que as suas pessoas realmente conseguem operar e depois invistam na maturidade de que o próximo modelo precisa.

2. **Vocês conseguem hoje atender um pedido de exclusão de ponta a ponta, e a sua linhagem prova para onde foi cada cópia de um registro pessoal?** Sob o GDPR e regimes semelhantes, um pedido de exclusão ou de acesso do titular é uma obrigação legal com prazos rígidos, e copiar dados amplamente sem linhagem torna impossível atendê-lo. As grandes equipes rotineiramente espalham os dados em data marts, extrações, caches e planilhas, então a pergunta real é se vocês conseguem rastrear e alcançar cada cópia, não se conseguem apagar o original. Levem evidências: escolham um cliente ou cidadão real e tentem enumerar todos os lugares onde seus dados vivem. Se não conseguem, essa lacuna é ao mesmo tempo um risco de conformidade e um problema de raio de impacto de violações. A resposta deve orientar o investimento em linhagem automatizada e em controles mais firmes sobre a cópia descontrolada, porque o caminho em conformidade precisa ser construído antes de o pedido chegar.

3. **A sua governança é o caminho fácil ou um portão que as pessoas contornam, e onde estão os sistemas paralelos que o provam?** A resposta durável do capítulo é codificar a governança como guardrails automatizados de autoatendimento para que o caminho em conformidade seja também o mais rápido, porque a governança manual pesada empurra as equipes para planilhas paralelas e cópias não governadas. Para empresas e agências, os sistemas paralelos são onde nascem as violações, os números errados e as auditorias malsucedidas, justamente porque ninguém os vigia. Levem um inventário concreto: que equipes mantêm as próprias cópias, que relatórios contornam o catálogo e onde as pessoas dizem que o processo oficial é lento demais. Cada sistema paralelo é um sinal de que o caminho governado custa mais que o atalho. Consertem o atrito em vez de emitir mais uma política, para que usar dados e contratos certificados seja genuinamente mais fácil que contorná-los.

4. **Que entidade de negócio crítica mais precisa de uma fonte autoritativa única, e quem, pelo nome, responde hoje pelo seu registro de ouro?** A gestão de dados mestres existe para impedir que finanças, vendas e operações relatem, cada uma, um cliente diferente ou uma receita diferente, e em escala a ausência de uma fonte autoritativa transforma todo número entre domínios numa discussão. As considerações concorrentes são quão autoritativo o hub precisa ser (registro, consolidação, coexistência ou totalmente centralizado) e quanta lógica de correspondência e sobrevivência vocês aceitam construir e auditar, já que um hub mais pesado custa mais mas resolve mais conflitos. Levem as entidades que aparecem em mais relatórios (cliente, cidadão, produto, fornecedor, funcionário), a contagem de quantos sistemas reivindicam guardar o registro real de cada uma e as regras de correspondência que usam hoje, se houver. Para um banco ou uma agência nacional, nomeiem o dono responsável e as regras de sobrevivência de modo explícito, porque um regulador que rastreia um número do relatório público até a origem perguntará quem decidiu qual duplicata venceu, e “ninguém” não é uma resposta que sobrevive a uma auditoria.

5. **Como vocês sabem que um conjunto crítico de dados está apto para uso antes que um consumidor descubra que ele está quebrado?** Em patrimônios imaturos, a qualidade é descoberta pelo analista cujo painel quebra ou pelo executivo cujo número do conselho está errado, que é o ponto de detecção mais caro possível. A tensão está entre o custo de instrumentar a qualidade (testes, verificações de atualidade e volume, monitoramento de distribuição e de deriva de esquema ao longo de dimensões nomeadas como exatidão, completude e validade) e o custo dos incidentes que vocês previnem, e as equipes rotineiramente investem pouco porque as falhas ficam invisíveis até se tornarem catastróficas. Levem os últimos três incidentes de dados, como foram detectados e quanto tempo duraram antes de alguém notar, mais os SLAs de qualidade que vocês de fato publicam e monitoram hoje. Para relatórios corporativos e governamentais, liguem cada produto de dados crítico a limiares explícitos de qualidade e tratem uma violação como uma interrupção de produção, com triagem e revisão pós-incidente, porque um número errado numa declaração regulatória ou numa estatística pública carrega um custo jurídico e de reputação que anula a conta do monitoramento.

6. **A sua governança é genuinamente federada, com propriedade pelo domínio, ou uma equipe central é responsabilizada por dados que não entende?** O capítulo argumenta que a propriedade federada com capacitação central escala onde a centralização pura vira gargalo e a descentralização pura degenera em caos, mas muitas organizações alegam federação enquanto uma pequena equipe central continua nominalmente responsável por milhares de tabelas de que não tem conhecimento de domínio. A atração concorrente é real: as equipes centrais dão consistência e um único responsável a quem cobrar, enquanto a propriedade pelo domínio dá conhecimento e responsabilização mas exige que os donos de negócio aceitem uma responsabilidade que talvez não queiram. Levem um mapa honesto de quem responde versus quem de fato mantém as definições e resolve os problemas de qualidade dos seus principais domínios, e se os curadores têm a autoridade e o tempo que o papel exige. Numa grande empresa ou agência, conferiram que a propriedade está com pessoas que têm ao mesmo tempo conhecimento do domínio e mandato para dizer não, porque a governança entregue a uma equipe central sem autoridade produz políticas que ninguém segue e um conselho que não resolve nada.

## Perspectiva por setor

**Startup.** Velocidade e sobrevivência vencem o processo. Nomeiem um dono para cada conjunto central de dados e façam de um repositório a fonte única da verdade para entidades como “cliente ativo”, e pulem catálogos, conselhos e malha por completo. Um contrato de uma página para as suas poucas tabelas críticas (esquema, horário de atualização, uma única expectativa de qualidade) encerra a discussão de “de quem é o número certo” numa tarde. Apoiem-se na governança já embutida no seu warehouse em vez de montar uma função que vocês não podem pagar.

**Pequena empresa.** Sem especialista dedicado em dados e com orçamento apertado, tratem a governança como higiene de dados e não como um projeto de plataforma: saibam que dados pessoais vocês guardam, onde vivem e quem pode tocá-los. Prefiram um warehouse gerenciado ou uma ferramenta de BI que ofereça linhagem, controle de acesso e retenção de fábrica, para comprar a governança embutida em ferramentas que já operam em vez de construí-la. Reservem qualquer pipeline sob medida para o único conjunto de dados que de fato move o negócio.

**Grande empresa.** Em escala, entre muitas equipes, o trabalho é propriedade federada com capacitação central: um catálogo compartilhado com linhagem automatizada, contratos de dados impostos, dados mestres para as entidades centrais e SLAs de qualidade medidos contra linhas de base. Codifiquem a governança como guardrails de autoatendimento para que o caminho em conformidade seja também o rápido e gerenciem os dados como um portfólio de produtos com donos nomeados. Assim os auditores podem rastrear qualquer número do relatório até a origem, e os grupos param de reinventar os mesmos pipelines e definições.

**Governo.** As regras de contratação, a transparência e a prestação de contas públicas moldam toda escolha. Tratem os indicadores publicados como produtos de dados com metodologia documentada, lançamentos versionados e portões de qualidade, e reconciliem deliberadamente as obrigações de acesso à informação e de dados abertos com a privacidade e a minimização, em vez de caso a caso. Exijam portabilidade de dados e divulgação de linhagem nos contratos com fornecedores para evitar aprisionamento (lock-in), mantenham um cronograma defensável de retenção e exclusão e deixem um conselho de curadoria guardar as definições compartilhadas para que “domicílio” ou “desemprego” signifique a mesma coisa em todos os departamentos.

## Exemplos

**Startup.** Uma empresa de SaaS em estágio inicial descobriu que a sua planilha de cobrança, a sua ferramenta de vendas e o seu banco de dados de produto relatavam, cada um, uma contagem diferente de clientes, e ninguém sabia dizer qual estava certa para o relatório aos investidores. A equipe de quatro pessoas nomeou um dono para cada conjunto central de dados, fez do warehouse a fonte única de “cliente ativo” e escreveu um contrato de uma página descrevendo o esquema e o horário diário de atualização. Levou uma tarde e acabou com a discussão semanal sobre em qual número confiar.

**Grande empresa.** Um banco multinacional consolidou dezenas de registros de clientes conflitantes entre suas divisões de varejo, crédito e patrimônio num hub de gestão de dados mestres, com regras de sobrevivência e um registro de ouro. Cada domínio publicou produtos de dados com contratos e SLAs de atualidade, expostos num catálogo central com linhagem. O tempo de relatório regulatório caiu acentuadamente, porque os auditores agora podiam rastrear qualquer número do relatório até a origem. O banco também aposentou várias plataformas de relatórios redundantes.

**Governo.** Um instituto nacional de estatística trata seus indicadores publicados como produtos de dados, com metodologia documentada, lançamentos versionados e portões rigorosos de qualidade. Um conselho de curadoria reconcilia as definições entre departamentos, de modo que “desemprego” ou “domicílio” signifique a mesma coisa em toda parte. A classificação e o acesso controlado protegem a confidencialidade dos respondentes, enquanto um catálogo público apoia a transparência e as obrigações de acesso à informação.

## Justificativa de negócio: motivações, ROI e TCO

A motivação da governança de dados é a redução de riscos e a criação de valor, em medidas aproximadamente iguais. Do lado do risco, os custos evitados incluem multas regulatórias, responsabilidade por violações, auditorias malsucedidas e o dano à reputação de publicar números errados. Do lado do valor, dados confiáveis e descobríveis aceleram todo esforço de análise e de aprendizado de máquina a jusante, reduzem pipelines duplicados e encurtam o tempo entre a pergunta e a resposta.

O custo de adoção é real: ferramentas de catálogo e de qualidade, tempo de curadores e donos e a mudança organizacional para fazer a propriedade pegar. Pesem o TCO (custo total de propriedade) contra o custo de não adotar, que costuma ser maior, só que escondido. Sem ser medido, esse custo aparece como analistas passando a maior parte do tempo achando e limpando dados, equipes reconstruindo os mesmos pipelines e executivos tomando decisões com números que ninguém consegue defender. Defendam o caso junto à liderança na linguagem dela: a governança transforma os dados de um passivo com risco ilimitado num ativo com retornos compostos, e é pré-requisito para uma IA confiável. Comecem onde a dor e a exposição regulatória são maiores, para mostrar valor rapidamente.

## Antipadrões e armadilhas

- Governança por comitê sem automação, produzindo políticas que ninguém segue.
- Catalogar tudo de uma vez em vez dos conjuntos de dados que de fato importam.
- Projetos de dados mestres que tentam ferver o oceano e nunca entregam um registro de ouro.
- Tratar a [qualidade dos dados](https://en.wikipedia.org/wiki/Data_quality) como uma limpeza pontual e não como observabilidade contínua.
- Propriedade atribuída a uma equipe central sem conhecimento do domínio nem autoridade.
- Contratos documentados em wikis mas não impostos nos pipelines.
- Copiar dados amplamente sem linhagem, tornando impossível atender pedidos de exclusão.
- Comprar uma ferramenta e chamá-la de estratégia: ferramenta sem modelo operacional fracassa.

## Modelo de maturidade

1. Iniciar: Os dados são sem documentação e sem dono, tratados de modo ad hoc e reativo. As definições conflitam entre equipes. A qualidade é descoberta pelos consumidores quando os relatórios quebram. Não existe catálogo nem linhagem.
2. Desenvolver: Surgem práticas básicas, mas inconsistentes entre as equipes. Alguns conjuntos de dados têm donos e documentação, e existe um catálogo parcial. As verificações de qualidade são manuais e reativas. Uma política de governança está escrita, mas é imposta de forma fraca e desigual.
3. Padronizar: Propriedade, contratos e SLAs são documentados e impostos em toda a organização. Os produtos de dados críticos têm donos nomeados; um catálogo com linhagem automatizada cobre os domínios-chave; existem dados mestres para as entidades centrais; a governança é federada, com capacitação central, e aplicada de modo consistente e não equipe por equipe.
4. Gerenciar: O patrimônio é medido e controlado em relação a linhas de base. As dimensões de qualidade (exatidão, completude, atualidade, validade, unicidade) são acompanhadas contra metas de SLA publicadas; as taxas de violação de contratos, a cobertura de linhagem e de catálogo, a atualidade e o tempo para atender um pedido de exclusão são relatados em painéis; a observabilidade alerta sobre deriva de esquema e anomalias de volume; os incidentes recebem triagem, análise de causa raiz e revisão pós-incidente; as decisões de acesso e de ir ou não ir repousam em métricas contra linhas de base, não em opinião.
5. Orquestrar: A governança é continuamente melhorada e integrada em toda a organização. Dados como produto é a norma entre os domínios; os contratos são impostos automaticamente e as mudanças incompatíveis falham cedo; guardrails de autoatendimento codificam a política; qualidade e linhagem alimentam a gestão proativa de riscos; as definições são confiáveis em toda a empresa e sustentam relatórios regulados e IA. A organização rotineiramente reequilibra a propriedade, aposenta plataformas redundantes e adapta a governança conforme o negócio e a regulação mudam.

## Ideias para discussão

- Qual das suas entidades de negócio mais urgentemente precisa de uma fonte única da verdade, e por que ela está fragmentada hoje?
- Onde contratos de dados impostos teriam prevenido um incidente recente?
- A sua organização está estruturada para a propriedade federada, ou a centralização serviria melhor agora?
- Como vocês reconciliam as obrigações de transparência do governo com a privacidade e a minimização?
- Que percentual do tempo dos seus analistas é gasto achando e limpando dados, e quanto valeria reduzi-lo pela metade?
- Quem responde, pelo nome, pelo seu conjunto de dados mais importante, e essa pessoa sabe disso?

## Principais conclusões

- Tratem os dados como um produto com donos, contratos e SLAs, não como resíduo de aplicações.
- A governança federada com capacitação central escala melhor que a centralização pura.
- Um catálogo com linhagem automatizada é a porta de entrada de um patrimônio de dados confiável.
- Estabeleçam uma fonte única da verdade para as entidades centrais por meio da gestão de dados mestres.
- Gerenciem a qualidade continuamente, ao longo de dimensões nomeadas, com observabilidade e resposta a incidentes.
- Codifiquem a governança como guardrails automatizados para que o caminho em conformidade seja o caminho fácil.
- Escolham warehouse, lakehouse ou malha para se ajustar à sua organização, não à badalação.

## Referências e leitura complementar

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson and colleagues, writings on data contracts.
- ISO/IEC 38505, "Governance of data."
- ISO 8000, "Data quality" standard series.
