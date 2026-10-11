# 4.5 Privacidade e proteção de dados

## Visão geral e motivação

A segurança protege os dados contra acesso não autorizado. A privacidade faz uma pergunta diferente: vocês deveriam estar coletando, usando e guardando esses dados, e as pessoas que eles descrevem têm voz nisso? As duas se sobrepõem, mas não são a mesma coisa. Dá para ser perfeitamente seguro e ainda assim violar a privacidade. Isso acontece acumulando dados que vocês não têm por que guardar, usando-os para finalidades com as quais as pessoas nunca concordaram ou movendo-os por fronteiras de modos que a lei proíbe. Para grandes equipes, a privacidade é uma restrição de design. Ela toca todo serviço que trata informações pessoais, o que hoje significa quase todos.

As apostas são altas e crescentes. A regulação de privacidade se espalhou pelo mundo. Ela traz multas que escalam com a receita e dá aos indivíduos direitos exigíveis sobre os seus dados. Para as empresas, tratar mal os dados pessoais convida a ação regulatória, litígios coletivos e a perda de uma confiança do cliente que é cara de reconstruir. Para o governo, o dever é ainda mais pesado. Os cidadãos não podem escolher outro provedor para seus dados de impostos, de saúde ou de benefícios, então o Estado lhes deve um dever especial de cuidado. E as falhas de privacidade corroem a confiança pública de que o governo depende.

Este capítulo trata a privacidade como uma disciplina de engenharia. Cobrimos projetar para a privacidade desde o início, minimizar e reter dados com responsabilidade, classificar e proteger categorias sensíveis como [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) e [PHI](https://en.wikipedia.org/wiki/Protected_health_information), tratar o consentimento e a base legal e gerenciar as exigências de transferência entre fronteiras e de residência que cada vez mais moldam a arquitetura.

*Veja também:* o capítulo 4.6 (conformidade e governança), o capítulo 7.1 (estratégia e governança de dados) e o capítulo 4.1 (fundamentos e cultura de segurança).

## Princípios fundamentais

- **[Privacidade desde a concepção](https://en.wikipedia.org/wiki/Privacy_by_design) e por padrão.** Construa a privacidade desde o início e faça da configuração mais protetora da privacidade o padrão.
- **[Minimização de dados](https://en.wikipedia.org/wiki/Data_minimization).** Colete apenas o que você genuinamente precisa, guarde-o só pelo tempo de que precisa e compartilhe-o só quando necessário.
- **Limitação de finalidade.** Use os dados apenas para as finalidades específicas divulgadas quando foram coletados.
- **Base legal.** Tenha uma justificativa jurídica válida para toda atividade de tratamento.
- **Direitos individuais.** Honre os direitos das pessoas de acessar, corrigir, excluir e portar seus dados.
- **Transparência.** Diga às pessoas com clareza o que você coleta, por quê e com quem compartilha.
- **Responsabilização.** Seja capaz de demonstrar a conformidade, e não apenas afirmá-la.

## Recomendações

### Projete para a privacidade desde o início

A privacidade parafusada num sistema pronto é cara e incompleta. Embutam-na desde o início.

- Conduzam **[Avaliações de Impacto sobre a Proteção de Dados](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIAs)** para novos sistemas e funcionalidades que tratam dados pessoais em escala ou carregam risco maior, identificando e mitigando os riscos de privacidade antes de construir.
- Façam os padrões protetores da privacidade: adesão voluntária (opt-in) em vez de recusa (opt-out) para o tratamento não essencial, campos mínimos de dados e a retenção sensata mais curta.
- Envolvam a especialização em privacidade cedo no design, ao lado da modelagem de ameaças de segurança, para que as duas sejam consideradas na fase das fronteiras de confiança.
- Mantenham um **mapa ou inventário de dados**: que dados pessoais vocês guardam, onde vivem, por quê e por onde fluem. Vocês não conseguem proteger nem prestar contas de dados que não enxergam.

### Minimize, retenha e apague com responsabilidade

Cada dado pessoal que vocês guardam é um passivo tanto quanto um ativo.

- **Minimizem a coleta:** questionem cada campo. Se não precisam dele para uma finalidade declarada, não o coletem.
- **Definam cronogramas de retenção** por tipo de dado e finalidade e imponham-nos com exclusão automatizada. Dados guardados “por via das dúvidas” são dados esperando para ser violados ou intimados.
- **Suportem o direito ao apagamento:** construam a capacidade de achar e excluir os dados de um indivíduo em todos os sistemas, inclusive cópias de segurança e cópias a jusante, dentro dos prazos legais. Isso é muito mais fácil quando projetado desde o início do que acrescentado depois.
- **[Anonimizem](https://en.wikipedia.org/wiki/Data_anonymization) ou agreguem** os dados para análise e teste, para que dados identificáveis não se espalhem para ambientes secundários.

### Classifique e proteja os dados sensíveis

Nem todo dado pessoal carrega o mesmo risco, e algumas categorias carregam peso jurídico especial.

- Classifiquem os dados em níveis, distinguindo **PII** (informações de identificação pessoal), **PHI** (informações protegidas de saúde), dados financeiros e categorias especiais (como raça, religião, saúde, biometria ou sexualidade) que carregam proteção legal reforçada.
- Apliquem proteção proporcional à sensibilidade: controles de acesso, criptografia e monitoramento mais fortes para os níveis mais sensíveis.
- Usem a **[tokenização](https://en.wikipedia.org/wiki/Tokenization_(data_security))** para substituir valores sensíveis (como números de cartão ou identificadores nacionais) por tokens não sensíveis, encolhendo os sistemas que algum dia tocam os dados brutos e, com isso, o escopo de conformidade.
- Usem a **[pseudonimização](https://en.wikipedia.org/wiki/Pseudonymization)** para separar os identificadores do resto de um registro, de modo que os dados sejam menos diretamente atribuíveis, reduzindo o risco e mantendo a utilidade.
- Mascarem os dados sensíveis em logs, mensagens de erro, análises e ambientes de não produção.

### Trate corretamente o consentimento e a base legal

Tratar dados pessoais exige uma fundação jurídica válida, e o consentimento é apenas uma entre várias.

- Identifiquem e documentem a **base legal** de cada atividade de tratamento: consentimento, contrato, obrigação legal, interesses vitais, tarefa pública ou interesses legítimos, conforme o regime aplicável.
- Onde o consentimento é a base, façam-no **livre, específico, informado e inequívoco**, com um jeito igualmente fácil de retirá-lo. Caixas pré-marcadas e consentimento em pacote não são válidos.
- Registrem o consentimento: com o que a pessoa concordou, quando e em que termos, para poder demonstrá-lo.
- Respeitem a **limitação de finalidade**: não reaproveitem dados para algo incompatível com o motivo da coleta sem uma nova base.
- Honrem sinais como o [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) e pedidos de recusa onde as leis exigem.

### Gerencie a transferência entre fronteiras e a residência de dados

Onde os dados fisicamente vivem e se movem é agora uma preocupação arquitetural de primeira ordem.

- Entendam as exigências de **residência de dados**: algumas jurisdições exigem que certos dados permaneçam dentro das fronteiras nacionais, e alguns dados governamentais precisam ficar em ambientes soberanos ou credenciados específicos.
- Para as **transferências entre fronteiras**, garantam que um mecanismo jurídico válido (decisões de adequação, cláusulas contratuais padrão ou equivalente) esteja no lugar e documentado.
- Projetem a arquitetura para a residência desde o início: armazenamento fixado por região, localização de dados e controle cuidadoso de para onde fluem cópias de segurança, logs e dados de análise, pois esses costumam vazar dados entre fronteiras sem serem notados.
- Acompanhem os suboperadores e terceiros. Um fornecedor que move dados para o exterior pode violar obrigações de residência em seu nome.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Minimização agressiva de dados | Menos risco, menor impacto de violação, conformidade mais simples | Pode limitar a análise e as opções futuras de produto |
| Retenção longa | Histórico rico para análise, aprendizado de máquina, disputas | Maior passivo, exposição a violações, complexidade de exclusão |
| Tokenização | Encolhe o escopo de conformidade, protege os dados brutos | Complexidade adicional de sistema, um cofre de tokens para proteger |
| Padrões de adesão voluntária (opt-in) | Mais confiança, conformidade clara | Menores volumes de dados, métricas de crescimento mais difíceis |
| Residência regional de dados | Atende a mandatos legais, constrói confiança de soberania | Complexidade arquitetural, custo maior, infraestrutura duplicada |
| Data lake centralizado | Poder analítico, fonte única | Risco concentrado, limitação de finalidade mais difícil |

A tensão central é entre o apetite do negócio por dados e o passivo que esses dados representam. As equipes de produto e de análise naturalmente querem coletar mais e guardar por mais tempo. A disciplina de privacidade puxa no sentido oposto. A resolução madura reenquadra os dados como um passivo a justificar e não um ativo a acumular. Cada decisão de coleta e de retenção precisa merecer seu lugar contra o risco que cria. A residência de dados acrescenta uma dimensão de custo versus conformidade. Atender às exigências de soberania pode multiplicar a infraestrutura, mas é simplesmente inegociável em alguns mercados e contextos governamentais.

## Perguntas para discutir com sua equipe

1. **Qual é o seu cronograma de retenção para cada classe de dado pessoal, e o que impõe a exclusão?** Dados guardados “por via das dúvidas” são dados esperando para ser violados ou intimados, então cada campo e cada registro precisa de um tempo de vida definido, ligado à sua finalidade. Decidam o cronograma por tipo de dado e depois imponham-no com exclusão automatizada em vez de confiar que alguém se lembre. Para as empresas, isso encolhe ao mesmo tempo a exposição a violações e o custo de armazenamento, e para o governo se alinha às obrigações estatutárias de guardar dados de cidadãos não além do que a lei permite. Levem uma amostra dos seus registros armazenados mais antigos e perguntem quem ainda precisa deles e sob que base, porque a resposta honesta muitas vezes é ninguém. Se a exclusão é manual ou inexistente, os dados se acumulam para sempre e o seu passivo cresce em silêncio no balanço.

2. **Quais campos sensíveis vocês podem tokenizar ou pseudonimizar para encolher tanto o risco quanto o escopo de conformidade?** Substituir números de cartão ou identificadores nacionais por tokens confina os valores brutos a um cofre pequeno e fortemente controlado, o que corta bastante os sistemas no escopo de auditorias como o PCI-DSS. A pseudonimização separa os identificadores do resto de um registro, reduzindo o risco e mantendo os dados úteis para análise e teste. Decidam quais valores de alta sensibilidade justificam um cofre de tokens (complexidade adicional, um cofre para proteger) e quais apenas precisam de mascaramento em logs e em ambientes de não produção. Levem um mapa de por onde os valores sensíveis brutos fluem hoje, porque todo sistema que os toca é um sistema que vocês precisam proteger e auditar. Para dados regulados e governamentais, essa redução de escopo é um dos poucos movimentos que reduz ao mesmo tempo custo e risco, então mirem primeiro seus campos mais sensíveis.

3. **Antes de a sua próxima funcionalidade ser entregue, o que dispara uma Avaliação de Impacto sobre a Proteção de Dados e quem a conduz?** A privacidade parafusada num sistema pronto é cara e incompleta, então uma DPIA precisa rodar cedo, ao lado da modelagem de ameaças de segurança, quando ainda dá para mudar o design de forma barata. Decidam o gatilho (novo tratamento em escala, dados de categoria especial, uma nova finalidade) e nomeiem quem é dono da avaliação para que ela não caia pelas frestas sob pressão de entrega. Uma DPIA de verdade pode pegar a coleta excessiva antes do lançamento, por exemplo trocando a localização precisa por dados de região aproximada sem perda de produto. Levem uma funcionalidade próxima e percorram-na: que dados pessoais ela coleta, por quê e se um design menos invasivo alcança o mesmo objetivo. Para serviços governamentais de que os cidadãos não podem optar por sair, essa verificação antecipada faz parte do dever de cuidado, então façam dela um portão e não uma reflexão tardia.

4. **Quando dados pessoais cruzam uma fronteira, inclusive por cópias de segurança, logs e suboperadores, qual mecanismo jurídico cobre cada travessia, e vocês conseguem provar?** As regras de residência e de transferência agora moldam a arquitetura tanto quanto qualquer requisito de desempenho, e as travessias que pegam as equipes raramente são as óbvias: um log enviado a uma ferramenta de observabilidade no exterior, uma cópia de segurança replicada para uma região mais barata ou um suboperador que move dados para fora em silêncio. Para uma grande organização as pressões concorrentes são reais, porque a infraestrutura fixada por região custa mais e duplica operações, mas uma única transferência ilícita pode anular a entrada num mercado ou disparar uma ordem de execução. Levem um mapa atual de fluxo de dados que nomeie todo lugar em que dados pessoais fisicamente repousam ou viajam, o mecanismo jurídico de cada fronteira que cruzam (decisão de adequação, cláusulas contratuais padrão ou equivalente) e a lista de suboperadores com suas localizações. Em contextos governamentais e de dados soberanos, tratem a residência como uma restrição arquitetural rígida e não uma cláusula de contrato, já que alguns registros nunca podem sair de ambientes nacionais credenciados, e o órgão responsável não pode delegar esse dever a um fornecedor.

5. **Que base legal sustenta cada atividade de tratamento, e vocês conseguiriam defender essa escolha diante de um regulador amanhã?** O consentimento é apenas uma entre várias fundações jurídicas, e as equipes frequentemente recorrem a ele por padrão quando o contrato, a obrigação legal, a tarefa pública ou os interesses legítimos seriam ao mesmo tempo mais honestos e mais duráveis. Isso importa em escala porque uma base fraca ou mal escolhida pode invalidar um pipeline inteiro, e desfazer um tratamento que vocês não tinham direito de realizar é muito mais caro que escolher a base correta desde o início. Pesem as considerações concorrentes abertamente: o consentimento dá controle aos indivíduos mas pode ser retirado e precisa ser livre, específico e desagregado, enquanto uma base como os interesses legítimos evita a fadiga de consentimento mas exige um teste de ponderação documentado. Levem um registro que mapeie cada atividade de tratamento à base alegada, a evidência que a sustenta e como vocês retirariam ou trocariam a base se contestados. No governo, a maior parte do tratamento central repousa na tarefa pública e não no consentimento, então sejam precisos sobre onde começa o consentimento opcional e retirável, porque borrar os dois corrói a confiança que os cidadãos não têm escolha senão estender.

6. **Se uma pessoa exercesse hoje o seu direito de acesso, exclusão ou portabilidade, vocês conseguiriam atendê-la em todos os sistemas dentro do prazo legal?** Os direitos individuais são fáceis de prometer numa política de privacidade e difíceis de honrar numa arquitetura que espalhou cópias de dados pessoais em cópias de segurança, caches, repositórios de análise e serviços a jusante. Para uma grande equipe esse é o momento em que a conformidade abstrata vira um teste concreto de engenharia, e um prazo estatutário perdido é ao mesmo tempo uma falha reportável e um sinal de que vocês não conseguem de fato enxergar os próprios dados. A consideração concorrente é custo e complexidade, já que construir um apagamento e uma exportação genuínos entre sistemas é trabalho de verdade, mas a alternativa é um atendimento manual, lento e propenso a erros, que não escala e viola a lei em silêncio. Levem um passo a passo honesto de um pedido real, da entrada à conclusão, incluindo como as cópias de segurança e os terceiros são alcançados, e cronometrem-no contra o prazo legal. Para serviços governamentais que as pessoas não podem deixar, tratem o atendimento de direitos por autoatendimento, completo e auditável como parte do dever de cuidado, não uma funcionalidade a agendar para depois.

## Perspectiva por setor

**Startup.** Com uma equipe minúscula e pouca pista, tratem a privacidade como seguro barato e não como um programa que vocês não conseguem pôr gente para fazer. Coletem apenas os campos de que a funcionalidade central precisa, mantenham um mapa de dados leve em planilha para poder de fato responder a um pedido de exclusão e mantenham e-mails e tokens fora dos logs. Um fluxo claro de consentimento e um apagamento real custam uma tarde agora. Adaptá-los depois que o primeiro cliente corporativo ou regulador pedir custa muito mais, e os dados coletados em excesso são um passivo com o qual vocês nada ganham.

**Pequena empresa.** Sem especialista dedicado em privacidade e com orçamento apertado, apoiem-se nos controles de privacidade já embutidos nas ferramentas que compram e prefiram fornecedores que tornam transparente o tratamento de dados e clara a residência. Enquadrem a decisão como comprar versus construir: vocês quase nunca constroem tokenização nem atendimento de direitos por conta própria, então escolham plataformas que ofereçam regras de retenção, exportação e exclusão de fábrica. Saibam que dados pessoais guardam e onde um registro errado ou perdido custaria um cliente, e escrevam uma base legal para cada uso, mesmo que o documento seja curto.

**Grande empresa.** Em escala o problema é a consistência entre muitas equipes: um mapa de dados compartilhado, níveis padronizados de classificação e retenção imposta para que nenhum grupo vire o elo fraco. Orcem explicitamente a engenharia do apagamento entre sistemas, dos cofres de tokenização e da arquitetura sensível à residência e governem os suboperadores de forma central para que um fornecedor não possa violar em seu nome uma obrigação de transferência. Façam das DPIAs um portão no processo de entrega e meçam a postura de privacidade, porque os auditores e reguladores pedirão que vocês demonstrem a conformidade, e não apenas a afirmem.

**Governo.** As regras de contratação, os deveres de transparência e a responsabilização pública moldam toda escolha, e os cidadãos não podem levar seus dados de impostos, de saúde ou de benefícios para outro lugar, então o dever de cuidado é reforçado. Fixem os registros sensíveis em ambientes nacionais credenciados, inclusive cópias de segurança e análise, vinculem contratualmente todo fornecedor às mesmas obrigações de residência e de exclusão e documentem uma base legal (muitas vezes a tarefa pública) para o tratamento central, mantendo os usos opcionais sob consentimento separado e retirável. Publiquem descrições em linguagem simples do que coletam e por quê e tornem confiável o atendimento de direitos dentro dos prazos estatutários, porque uma falha de privacidade aqui corrói a confiança pública de que o serviço depende.

## Exemplos

**Startup.** Um aplicativo de consumo em estágio inicial coleta apenas os dados de que realmente precisa, porque cada campo extra é um passivo que prefere não defender depois. Mantém uma simples planilha de mapa de dados de onde vivem os dados pessoais para poder de fato responder a um pedido de exclusão, mantém e-mails e tokens fora dos logs e define uma regra básica de retenção para expurgar os dados de contas mortas há muito. Construir agora um fluxo claro de consentimento e uma exclusão real custa uma tarde. Adaptá-los depois que o primeiro cliente corporativo ou regulador pedir custa muito mais.

**Grande empresa.** Um aplicativo de consumo global conduz uma DPIA antes de lançar uma nova funcionalidade de recomendação e descobre que ela coletaria localização precisa desnecessariamente. A equipe passa a usar dados de região aproximada, reduzindo o risco sem perda de produto. Os números de cartão são tokenizados para que só um pequeno cofre, rigorosamente controlado, guarde os valores brutos, cortando drasticamente o escopo [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (setor de cartões de pagamento) da empresa. Regras automatizadas de retenção expurgam os dados de contas inativas no prazo, e um fluxo de autoatendimento permite aos usuários exportar e excluir seus dados dentro do prazo legal em todos os sistemas, inclusive as cópias de segurança.

**Governo.** Um serviço nacional de saúde classifica todos os prontuários de pacientes como PHI e dados de categoria especial, impondo controles de acesso estritos, criptografia e registro de auditoria. A política de residência de dados mantém todos os registros dentro das fronteiras nacionais, inclusive cópias de segurança e análise, e todo fornecedor está contratualmente obrigado à mesma regra. Os cidadãos têm uma base legal documentada (tarefa pública) para o tratamento central, enquanto os usos opcionais de pesquisa exigem consentimento separado e retirável, que é registrado e honrado. Um mapa de dados sustenta a capacidade de responder a pedidos de acesso e de apagamento dentro dos prazos estatutários.

## Justificativa de negócio: motivações, ROI e TCO

O investimento em privacidade costuma ser enquadrado como puro custo de conformidade, mas isso o subestima. O custo total de propriedade inclui os processos de DPIA, as ferramentas de mapeamento e inventário de dados, a infraestrutura de tokenização e de retenção e a engenharia para sustentar os direitos individuais e a residência. Pesem isso contra o custo de não investir, que é severo e cada vez mais provável. As multas de privacidade já chegam a porcentagens da receita global, as ações coletivas se seguem às grandes violações e os reguladores mostraram que agirão. Além das multas, o tratamento inadequado da privacidade destrói a confiança do cliente que sustenta a receita. E remediar uma falha de privacidade depois do fato (adaptar a exclusão, desembaraçar fluxos de dados ilícitos) custa muito mais que construí-la desde o início.

O ROI também tem um lado positivo real. Uma privacidade forte é um diferencial competitivo e, em mercados regulados e governamentais, é pré-condição para ganhar negócios. A minimização de dados reduz diretamente a exposição a violações e o custo de armazenamento, e a tokenização encolhe o escopo caro de auditorias como o PCI-DSS. Ao defender o caso junto à liderança, apresentem a privacidade de duas maneiras: como gerenciamento de passivo ajustado ao risco, com exposição regulatória real, e como um ativo de confiança que abre mercados. Enfatizem que a privacidade desde a concepção é barata comparada à privacidade por processo judicial e que dados acumulados sem finalidade são um passivo no balanço, esperando para ser realizado.

## Antipadrões e armadilhas

- **Coletar tudo, decidir depois.** Acumular dados sem finalidade, maximizando o passivo sem benefício.
- **Retenção por negligência.** Nunca excluir nada porque não existe cronograma, de modo que os dados se acumulam para sempre.
- **Teatro de consentimento.** Caixas pré-marcadas, consentimento em pacote ou padrões obscuros que são juridicamente inválidos e corroem a confiança.
- **Apagamento que perde as cópias de segurança.** Excluir do repositório principal mas deixar cópias em backups, logs e análise.
- **PII em logs e dados de teste.** Espalhar dados sensíveis para ambientes de baixo controle onde são facilmente expostos.
- **Ignorar os fluxos de dados.** Deixar de notar que logs, cópias de segurança, análise e suboperadores movem dados entre fronteiras.
- **Privacidade como preocupação só jurídica.** Tratá-la como burocracia e não como restrição de design de engenharia.
- **Sem mapa de dados.** Não conseguir responder onde vivem os dados pessoais, o que torna impossíveis os pedidos de direitos e a resposta a violações.

## Modelo de maturidade

**Nível 1: Iniciar.** A privacidade é tratada de forma reativa, se tanto. Os dados pessoais são coletados livremente, sem inventário, minimização nem limites de retenção. O consentimento é uma reflexão tardia, não há processo para pedidos de acesso ou de apagamento e onde os dados fisicamente vivem não é considerado.

**Nível 2: Desenvolver.** Aparecem práticas básicas mas variam por equipe. Existe uma política de privacidade e o consentimento básico é capturado, com alguma consciência da retenção. Os pedidos de direitos são tratados manualmente e devagar, a classificação de dados é informal e uma equipe pode mapear seus dados enquanto outra coleta livremente. Nada é imposto de modo consistente na organização.

**Nível 3: Padronizar.** A privacidade desde a concepção é documentada e imposta em toda a organização. As DPIAs rodam para projetos de maior risco, os dados são mapeados e classificados em níveis e os cronogramas de retenção são impostos com exclusão automatizada. Uma base legal é documentada para cada atividade de tratamento, existem mecanismos válidos de consentimento, os pedidos de direitos são atendidos dentro dos prazos e a residência é tratada para dados regulados.

**Nível 4: Gerenciar.** O programa de privacidade é medido e controlado em relação a linhas de base. Vocês acompanham o tempo de atendimento dos pedidos de direitos contra os prazos estatutários, a cobertura da política de retenção e a idade dos registros mais antigos, a contagem de campos de dados pessoais no escopo e quantos são tokenizados ou pseudonimizados, as taxas de conclusão de DPIA para funcionalidades qualificadas e o número de fluxos não gerenciados entre fronteiras achados em auditorias. As métricas alimentam limiares definidos, de modo que a violação de uma meta (um pedido de direitos perto do prazo, uma transferência inesperada, uma deriva de retenção) dispara uma resposta documentada em vez de passar despercebida.

**Nível 5: Orquestrar.** A privacidade é uma restrição padrão de engenharia, continuamente melhorada e integrada em toda a organização. A minimização, a tokenização e a retenção automatizada são padrão, os pedidos de direitos são de autoatendimento e completos em todos os sistemas, inclusive as cópias de segurança, e os fluxos de dados e a residência são continuamente acompanhados e impostos. A postura de privacidade se adapta conforme a regulação, os mercados e a arquitetura mudam, devolvendo as lições ao design para que a linha de base continue subindo e não apenas se mantenha.

## Ideias para discussão

1. Como vocês resolvem a tensão entre as equipes de análise querendo mais dados e a privacidade querendo menos?
2. Qual é uma arquitetura realista para honrar o apagamento entre repositórios principais, cópias de segurança e cópias a jusante?
3. Que base legal se ajusta a cada uma das suas atividades de tratamento, e vocês conseguem defender a escolha?
4. Como vocês mantêm os dados pessoais fora dos logs e dos ambientes de não produção sem atrapalhar a depuração?
5. Que exigências de residência de dados se aplicam aos seus mercados, e como as cópias de segurança e a análise as complicam?
6. Como a modelagem de ameaças de privacidade e de segurança deve ser combinada numa única atividade de design?

## Principais conclusões

- A privacidade rege se e como vocês usam dados pessoais. É distinta da segurança e complementar a ela.
- Projetem a privacidade desde o início, com DPIAs e padrões protetores da privacidade.
- Minimizem a coleta, imponham cronogramas de retenção e construam uma capacidade genuína de apagamento.
- Classifiquem PII, PHI e categorias especiais e protejam-nas proporcionalmente com tokenização e mascaramento.
- Estabeleçam e documentem uma base legal. Façam o consentimento livre, específico e retirável.
- Tratem a residência de dados e a transferência entre fronteiras como restrições arquiteturais de primeira ordem.
- Os dados são um passivo tanto quanto um ativo. Acumulá-los sem finalidade é risco esperando para ser realizado.

## Referências e leitura complementar

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- European Union, *General Data Protection Regulation (GDPR)* text and guidance
- National Institute of Standards and Technology, *Privacy Framework* and *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* and *Fair Information Practice Principles (FIPPs)*
- California Consumer Privacy Act (CCPA/CPRA) statutory text and regulator guidance
