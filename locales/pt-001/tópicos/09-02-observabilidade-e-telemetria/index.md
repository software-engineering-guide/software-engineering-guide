# 9.2 Observabilidade e telemetria

## Visão geral e motivação

A [telemetria](https://en.wikipedia.org/wiki/Telemetry) é o dado que um sistema emite sobre o próprio comportamento: as métricas, os logs, os rastros e os eventos coletados do software em execução. O monitoramento responde, a partir dessa telemetria, a perguntas que vocês já sabiam fazer. O disco está cheio? A taxa de erro está acima de um limiar? O serviço está no ar? A [observabilidade](https://en.wikipedia.org/wiki/Observability_(software)) é mais ampla. É a capacidade de fazer novas perguntas sobre o estado interno de um sistema, de fora, sem entregar código novo, para entender comportamentos que vocês nunca anteciparam. À medida que os sistemas crescem para arquiteturas distribuídas, de [microsserviços](https://en.wikipedia.org/wiki/Microservices) e [orientadas a eventos](https://en.wikipedia.org/wiki/Event-driven_architecture), as falhas que mais doem são as que ninguém viu chegar, e a observabilidade é o que permite depurá-las. O monitoramento diz que algo está errado. A observabilidade ajuda a descobrir por quê.

Para grandes equipes, essa distinção é decisiva. Dava para entender um monolito lendo logs numa máquina. Uma plataforma moderna abrange centenas de serviços, muitas equipes, várias regiões e dependências de terceiros, e uma única requisição de usuário pode tocar dezenas de componentes. Nenhuma pessoa guarda o sistema inteiro na cabeça. A telemetria compartilhada e de alta qualidade vira o tecido conectivo que permite a qualquer engenheiro seguir uma requisição entre fronteiras, alinhar sintomas entre serviços e raciocinar sobre um sistema de que ninguém é dono por inteiro. Sem ela, os incidentes se arrastam, a culpa voa entre as equipes e as causas raiz permanecem escondidas.

Os sistemas corporativos e governamentais elevam as apostas com conformidade, auditabilidade e prestação de contas públicas. Os reguladores podem exigir evidência de quem acessou o quê e quando. As equipes de segurança precisam de telemetria para detectar intrusões. Os serviços voltados ao cidadão precisam mostrar que cumprem seus compromissos publicados de desempenho. Uma boa observabilidade serve a tudo isso ao mesmo tempo: é uma ferramenta de engenharia, um controle de segurança e um mecanismo de prestação de contas num só. Padronizar numa instrumentação aberta evita o aprisionamento (lock-in) aos agentes proprietários de um único fornecedor, o que importa enormemente quando os sistemas precisam durar décadas e sobreviver a ciclos de contratação.

*Veja também:* capítulo 9.1 (engenharia de confiabilidade de sites e SLOs), capítulo 9.3 (gestão de incidentes) e capítulo 3.3 (sistemas distribuídos).

## Princípios fundamentais

- **Instrumentem para perguntas desconhecidas.** Projetem a telemetria para poder investigar falhas novas, além das que vocês previram.
- **Três pilares, uma história.** Métricas, logs e rastros são visões complementares. O valor deles se multiplica quando correlacionados e não isolados.
- **Estruturem tudo.** A telemetria estruturada e interpretável por máquina vence o texto livre que só humanos conseguem ler.
- **Correlacionem com identificadores compartilhados.** IDs de rastro e de requisição propagados em toda parte permitem costurar um único evento entre serviços.
- **Alertem sobre sintomas, não causas.** Acionem humanos para problemas visíveis ao usuário. Deixem painéis e investigação revelarem a causa subjacente.
- **Todo acionamento deve ser acionável.** Um alerta que não exige ação humana é ruído que erode a confiança e causa fadiga.
- **A alta cardinalidade é uma funcionalidade.** A capacidade de fatiar por usuário, requisição, região e versão é o que torna possível depurar em produção.
- **Sejam donos da sua instrumentação.** Padronizem numa telemetria aberta e neutra quanto a fornecedores para controlar seus dados e poder trocar de backend.

## Recomendações

### Construa sobre os três pilares e além

As **métricas** são séries temporais numéricas, baratas de armazenar e ideais para painéis, tendências e limiares de alerta. Os **logs** são registros discretos e com carimbo de data de eventos, ricos em detalhe e essenciais para a investigação forense. Os **[rastros](https://en.wikipedia.org/wiki/Tracing_(software))** (traces) acompanham uma única requisição ao se mover pelos serviços, mostrando latência e dependências ao longo do grafo distribuído de chamadas. Além desses, considerem **eventos** (mudanças de estado significativas, como implantações), **perfis** (onde o código gasta CPU e memória) e o **[monitoramento de usuários reais](https://en.wikipedia.org/wiki/Real_user_monitoring)** da experiência efetiva do cliente. Nenhum pilar basta por si só. O objetivo é transitar com fluidez entre eles durante uma investigação.

### Padronize no OpenTelemetry e no registro estruturado de logs

Adotem o [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) como o padrão neutro quanto a fornecedores para gerar e coletar métricas, logs e rastros. Ele separa a instrumentação do backend de análise, de modo que vocês podem trocar de fornecedor sem reinstrumentar centenas de serviços. Essa propriedade é crítica para sistemas corporativos e governamentais de vida longa. Emitam os logs como registros estruturados (por exemplo JSON) com nomes de campo consistentes para carimbo de data, severidade, serviço e identificadores. Propaguem um ID de rastro ou de correlação da borda por toda chamada a jusante e incluam-no em toda linha de log e em todo exemplar de métrica, para que os três pilares se liguem automaticamente.

### Projete alertas para a acionabilidade e o baixo ruído

A sua filosofia de alertas decide se o sobreaviso é sustentável. Alertem principalmente sobre sintomas que os usuários sentem, expressos como taxas de consumo de SLO ([objetivo de nível de serviço](https://en.wikipedia.org/wiki/Service-level_objective)). Acionem quando vocês estão queimando o orçamento de erros (a falha permitida em relação a esse objetivo) depressa o bastante para estourá-lo, usando alertas de taxa de consumo em várias janelas para equilibrar a detecção rápida contra os alarmes falsos. Reservem o acionamento para problemas que exigem ação humana imediata e encaminhem todo o resto para chamados ou painéis. Podem sem piedade os alertas que disparam sem exigir ação, porque a fadiga de alertas é uma das principais causas de incidentes reais perdidos e de esgotamento no sobreaviso. Todo alerta deve apontar para um runbook.

### Modele a saúde com painéis e monitoramento de SLO

Construam painéis em torno de um modelo claro de saúde e não de uma parede com todas as métricas que vocês têm. Um bom framework inicial são os “quatro sinais dourados”: latência, tráfego, erros e saturação. Criem painéis em nível de serviço que mostrem o estado do SLO e o orçamento de erros restante num relance, mais painéis de nível mais alto que modelem a saúde geral do sistema e das jornadas de usuário. Curem-nos deliberadamente, porque painéis que mostram tudo não comunicam nada. Mantenham-nos perto dos alertas e dos runbooks, para que quem responde vá depressa do sinal ao contexto e à ação.

### Viabilize a depuração em produção com alta cardinalidade

Os problemas de produção mais difíceis atingem uma fatia estreita: um cliente, uma região, uma versão de API, um tipo de dispositivo. Para investigá-los vocês precisam de telemetria de **alta cardinalidade**, a capacidade de agrupar e filtrar por campos com muitos valores distintos, como ID de usuário ou ID de requisição. Eventos largos e ricamente atribuídos, que carregam muitas dimensões por registro, permitem fazer perguntas arbitrárias depois do fato. Mantenham cardinalidade e fidelidade de amostragem suficientes para isolar casos atípicos e favoreçam rastros ligados a exemplares para que um pico numa métrica leve direto a requisições lentas representativas.

### Gerencie custo, retenção e amostragem

O volume de telemetria cresce com o sistema e pode virar uma grande despesa. Definam políticas de retenção por classe de dado: guardem dados de alta resolução brevemente e agregados por mais tempo. Apliquem amostragem inteligente aos rastros, enviesada para manter erros e requisições lentas, de modo a reter a cauda interessante sem pagar por cada sucesso rotineiro. Revisem regularmente o gasto com telemetria, porque custos de observabilidade não gerenciados podem rivalizar com a infraestrutura que observam.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Eventos de alta cardinalidade | Depuração poderosa, perguntem qualquer coisa | Maior custo de armazenamento e de consulta |
| Amostragem agressiva | Custo menor, menos ruído | Pode perder eventos raros |
| Alertas baseados em sintomas | Menos acionamentos, e acionáveis | Precisa de bons SLOs para funcionar bem |
| Padrão OpenTelemetry | Neutro quanto a fornecedores, portável | Esforço de migração, ferramentas ainda amadurecendo |
| Retenção longa de logs | Melhor forense e auditoria | Custo de armazenamento, exposição de privacidade |

As decisões de observabilidade se resumem a uma tensão entre fidelidade e custo. Capturar tudo em resolução plena dá uma visão retrospectiva perfeita, mas em escala é proibitivamente caro. Cortar de forma agressiva economiza dinheiro, mas vocês podem jogar fora o único registro que teria explicado uma interrupção. A amostragem e os níveis de retenção são como as equipes maduras caminham nessa linha, mantendo erros e casos atípicos enquanto desbastam os dados de rotina. O compromisso dos alertas é entre sensibilidade e ruído: alertas demais causam fadiga e incidentes perdidos, de menos deixam os problemas apodrecer. Os alertas baseados em sintomas e guiados por SLO resolvem boa parte disso, mas só se vocês tiverem SLOs significativos.

## Perguntas para discutir com sua equipe

1. **Qual é o seu plano para migrar os serviços legados para o OpenTelemetry, e como vocês evitam pagar por duas pilhas de instrumentação durante a transição?** A instrumentação neutra quanto a fornecedores é a propriedade que permite trocar de backend sem reinstrumentar centenas de serviços, e importa mais para os sistemas corporativos e governamentais de vida longa que sobrevivem a qualquer contrato de fornecedor. A migração é onde as boas intenções empacam: patrimônios instrumentados pela metade deixam lacunas exatamente onde uma requisição passa de um serviço novo para um antigo, quebrando o rastro de ponta a ponta. Levem um inventário à discussão: quais serviços emitem dados de agente proprietário, quais emitem OpenTelemetry e onde o contexto do rastro se perde na fronteira. Decidam um sequenciamento que siga os caminhos reais das requisições e não os organogramas e orcem a janela em que vocês rodam os dois coletores. A resposta determina se vocês de fato são donos da sua telemetria ou ficam presos aos agentes de um único fornecedor.

2. **Quando vocês auditaram pela última vez todo alerta quanto à acionabilidade, e quantos acionamentos do mês passado não exigiram ação humana?** A fadiga de alertas é uma das principais causas de incidentes reais perdidos e de esgotamento no sobreaviso, então um acionamento que não exige ação não é ruído inofensivo, ele erode ativamente a resposta de que vocês dependem. Levem os comprovantes: puxem os acionamentos do mês passado, marquem cada um como atendido ou ignorado e contem quantos correspondiam a um runbook. Para uma grande equipe que abrange muitos serviços, os alertas ruidosos de uma equipe dessensibilizam o sobreaviso compartilhado de todos. Estabeleçam o padrão de que todo acionamento aponta para um runbook e se liga a uma taxa de consumo de SLO e depois apaguem o resto sem piedade. O resultado dessa auditoria deve cortar diretamente o seu volume de acionamentos e dizer quais serviços não têm um SLO significativo por trás dos alertas.

3. **Qual é a sua estratégia de amostragem de rastros, e quão confiantes vocês estão de que ela mantém os erros e a cauda lenta?** O volume de telemetria cresce com o sistema e o custo de observabilidade não gerenciado pode rivalizar com a infraestrutura que ela observa, então vocês vão amostrar, e a pergunta é se amostram de modo inteligente. Tirar cardinalidade ou amostrar às cegas remove exatamente os registros necessários para depurar os problemas estreitos que atingem um cliente, uma região ou uma versão de API. Levem seus níveis atuais de retenção e regras de amostragem: vocês enviesam para manter erros e requisições lentas, usando rastros ligados a exemplares para que um pico de métrica leve a uma requisição lenta representativa? Para sistemas auditados e sujeitos a privacidade, reconciliem a retenção com as regras de minimização de dados para não acumular dados pessoais só para depurar. A resposta define onde vocês gastam o orçamento de telemetria e se a sua próxima interrupção difícil será explicável ou um mistério.

4. **Quais dos seus SLOs são compromissos reais de jornada do usuário, e quais são métricas substitutas em que ninguém fora da equipe dona acredita?** O alerta baseado em sintomas só funciona quando os sintomas correspondem a coisas que os usuários de fato sentem, então um alerta ligado a um limiar de CPU ou a uma meta de disponibilidade inventada aciona pessoas por problemas que talvez não importem enquanto fica calado sobre os que importam. Para uma grande organização, os SLOs são também o contrato que permite a equipes independentes dividir um rodízio de sobreaviso sem rediscutir a severidade a cada incidente. Levem o catálogo atual de SLOs, a jornada do usuário que cada objetivo deve proteger e as violações do último trimestre, com se os clientes de fato reclamaram. Em contextos corporativos e governamentais, liguem os SLOs mais visíveis aos compromissos de desempenho publicados a que o serviço é cobrado, para que o mesmo sinal de taxa de consumo que aciona um engenheiro seja também a evidência que vocês mostram a um regulador ou a um órgão de supervisão. A discussão deve aposentar as métricas substitutas e deixar uma lista curta de objetivos que um não engenheiro reconheceria como promessas aos usuários.

5. **Quem é dono da governança dos dados de telemetria, e vocês conseguem provar que os dados pessoais são redigidos antes de chegar ao seu backend de observabilidade?** Os eventos de alta cardinalidade e a retenção longa de logs são exatamente as funcionalidades que tornam possível depurar, e exatamente as que transformam um repositório de observabilidade numa cópia não gerenciada dos dados pessoais dos seus usuários. A atração contrária é real: os engenheiros querem atributos mais ricos e retenção mais longa, enquanto privacidade e jurídico querem minimização de dados e vidas curtas. Levem um mapa de fluxo de dados mostrando quais campos carregam dados pessoais ou sensíveis, onde a redação ou a tokenização acontece no pipeline e quais são seus níveis de retenção por classe de dado. Para sistemas regulados e públicos, nomeiem o dono responsável, liguem a retenção à base legal e às regras de minimização de dados sob as quais vocês operam e estejam prontos para mostrar a um auditor que o acesso à própria telemetria é registrado e controlado. A resposta decide se a sua plataforma de observabilidade é um ativo ou uma violação permanente esperando para ser descoberta.

6. **Quando um incidente atravessa os serviços de várias equipes, a sua telemetria permite a um único responsável seguir a requisição de ponta a ponta, ou o rastro se quebra em cada fronteira de propriedade?** Toda a promessa da telemetria correlacionada e com IDs propagados é que um único engenheiro consiga raciocinar sobre um sistema de que ninguém é dono por inteiro, e essa promessa desaba exatamente na fronteira onde o contexto do rastro se perde ou onde duas equipes usam identificadores e ferramentas incompatíveis. Pesem a atração pela autonomia de cada equipe na escolha das ferramentas de observabilidade contra o custo compartilhado de um patrimônio fragmentado em que cada passagem de bastão é um beco sem saída durante uma interrupção. Levem a linha do tempo de um incidente recente entre equipes e marquem onde quem respondia perdeu o fio, mais um inventário de quais serviços propagam um ID de correlação comum e quais não. Para uma grande empresa ou uma plataforma governamental montada com muitos fornecedores e sistemas de vida longa, decidam quanto vocês impõem centralmente, um padrão compartilhado de contexto de rastro e um esquema comum de IDs, versus o que deixam às equipes, porque os componentes que vocês recontratam ao longo de décadas ainda precisam interoperar sobre a mesma requisição. A resposta diz se o seu próximo incidente entre várias equipes será uma investigação coordenada ou uma rodada de apontar o dedo.

## Perspectiva por setor

**Startup.** Com um punhado de serviços e sem mãos sobrando, instrumentem com OpenTelemetry desde o primeiro dia e entreguem logs JSON estruturados que carregam um ID de requisição de ponta a ponta. Esse pequeno investimento transforma “o app está lento” num rastro que vocês conseguem ler e mantém vocês livres para passar de um nível gratuito a um backend pago depois sem reinstrumentar. Pulem painéis elaborados e a maquinaria de SLO até terem usuários cuja experiência vocês consigam de fato medir.

**Pequena empresa.** Vocês não têm especialista em observabilidade e têm orçamento apertado, então apoiem-se num backend gerenciado em que instrumentação, armazenamento e painéis vêm juntos, em vez de montar a própria pilha. A escolha entre comprar e construir favorece comprar quase sempre aqui; a sua escassa atenção é mais bem gasta nos dois ou três alertas de sinais dourados que dizem que o serviço caiu do que operando um pipeline de telemetria. Definam um limite rígido de retenção para que o custo da telemetria não ultrapasse em silêncio a infraestrutura que ela vigia.

**Grande empresa.** O trabalho é governança entre muitas equipes: um padrão compartilhado de OpenTelemetry, um esquema comum de IDs de correlação e painéis curados de SLO para que um único responsável possa seguir uma requisição por dezenas de serviços. Gerenciem a telemetria como um centro de custo, com níveis de retenção e política de amostragem, padronizem os alertas nas taxas de consumo de SLO para manter sustentável um sobreaviso compartilhado e podem os alertas ruidosos centralmente para que a fadiga de uma equipe não dessensibilize todos. Tratem a camada de instrumentação como infraestrutura neutra quanto a fornecedores que sobrevive a qualquer contrato de backend.

**Governo.** As regras de contratação, a transparência e a prestação de contas públicas moldam o projeto. Padronizem numa instrumentação aberta para que um sistema que deve rodar por décadas sobreviva à recontratação por fornecedores diferentes sem ficar refém de agentes proprietários, e exijam essa portabilidade no contrato. Usem logs de auditoria estruturados para mostrar quem acessou qual registro e quando, redijam ou tokenizem os dados pessoais antes de chegarem ao repositório de telemetria e reconciliem a retenção com a lei de minimização de dados. Publiquem painéis de SLO dos serviços voltados ao cidadão para que os mesmos sinais que os seus engenheiros vigiam sejam evidência visível dos compromissos a que vocês são cobrados.

## Exemplos

**Startup.** Uma startup de quatro pessoas entrega um backend móvel e vive recebendo queixas vagas de “o app está lento” que não consegue reproduzir. A equipe acrescenta o OpenTelemetry aos seus poucos serviços e passa a logs JSON estruturados com um ID de requisição carregado do aplicativo por todos os saltos. O próximo relato de lentidão se resolve em minutos: um rastro mostra um índice de banco de dados ausente na tabela de pedidos sob uma consulta específica. Como escolheram cedo a instrumentação aberta, depois passam de um nível gratuito a um backend pago sem reinstrumentar nada.

**Grande empresa.** Uma grande plataforma de comércio eletrônico instrumenta todo serviço com OpenTelemetry, propagando um ID de rastro do navegador do cliente pelo checkout, pagamento, estoque e entrega. Quando a conversão cai, um engenheiro de sobreaviso parte de um alerta de taxa de consumo de SLO, abre os sinais dourados do painel do checkout, nota latência elevada numa região e segue um rastro de exemplar até uma chamada lenta de banco de dados num único serviço. Os atributos de alta cardinalidade mostram que o problema se limita a uma categoria de produto, o que orienta uma correção direcionada em minutos e não em horas.

**Governo.** Um serviço nacional de saúde roda uma plataforma de prontuários sob rígidas regras de auditoria e privacidade. Os logs estruturados capturam quem acessou qual registro e quando, alimentando tanto o monitoramento de segurança quanto os relatórios de conformidade, enquanto os campos de identificação pessoal são redigidos ou tokenizados na telemetria. Painéis públicos de SLO mostram disponibilidade e latência do agendamento de consultas voltado ao cidadão. Ao padronizar numa instrumentação aberta, a agência evita o aprisionamento proprietário num sistema que deve rodar por décadas e ser recontratado por fornecedores diferentes ao longo da vida.

## Justificativa de negócio: motivações, ROI e TCO

O principal retorno da observabilidade é uma queda dramática no tempo para detectar e resolver incidentes. Para um serviço em que a indisponibilidade é cara, cortar o tempo médio de resolução de horas para minutos paga as ferramentas muitas vezes num único grande incidente. A observabilidade também poupa o tempo de engenharia que vocês de outro modo gastariam adivinhando, reproduzindo bugs e discutindo qual equipe é culpada, e encurta o ciclo de retorno que permite às equipes entregar com confiança. O valor de segurança e de conformidade também é real: a mesma telemetria sustenta a detecção de intrusões e a evidência de auditoria.

O custo total de propriedade inclui o esforço de instrumentação, os custos de armazenamento e de consulta da telemetria e a disciplina de curar o sinal do ruído. Esses custos são visíveis e recorrentes, o que tenta a liderança a investir pouco. O custo de não adotar é maior mas mais difícil de ver: interrupções prolongadas, problemas de desempenho não diagnosticados, incidentes de segurança achados tarde ou nunca e engenheiros se esgotando com alertas contra os quais nada podem fazer. Defendam o caso com dados concretos de incidentes. Mostrem o tempo de resolução e o impacto de negócio das interrupções recentes e projetem a redução que uma telemetria melhor entregaria. Enquadrar a observabilidade como um seguro que também acelera a entrega, e não como um centro de custo puro, ganha a discussão.

## Antipadrões e armadilhas

- **Alertar sobre tudo.** Acionar por toda anomalia treina quem responde a ignorar alertas, e os incidentes reais passam.
- **Acionamento por causa.** Alertar sobre causas internas e não sobre sintomas do usuário inunda o sobreaviso de ruído e perde falhas novas.
- **Logs não estruturados.** Logs de texto livre que não podem ser consultados nem correlacionados forçam buscas manuais lentas durante os incidentes.
- **Três pilares isolados.** Métricas, logs e rastros em ferramentas desconectadas e sem IDs compartilhados impedem seguir um evento de ponta a ponta.
- **Dispersão de painéis.** Centenas de painéis sem curadoria significam que ninguém sabe qual mostra se o sistema está saudável.
- **Colapso de cardinalidade.** Remover campos de alta cardinalidade para economizar custo elimina exatamente os dados necessários para depurar problemas estreitos.
- **Aprisionamento a fornecedor.** Agentes proprietários em toda parte tornam proibitivamente caro trocar de backend e mantêm seus dados como refém.

## Modelo de maturidade

**Nível 1, Iniciar.** A observabilidade é ad hoc e reativa. Verificações básicas de disponibilidade e logs não estruturados vivem em máquinas individuais, depurar significa entrar nos servidores para fazer grep e não há telemetria compartilhada. Os alertas são ruidosos, baseados em causas e muitas vezes ignorados, de modo que os incidentes reais surgem por queixas de usuários e não por sinais.

**Nível 2, Desenvolver.** Aparecem práticas básicas, mas variam por equipe. Alguns serviços enviam métricas e logs a um lugar central, existem alguns painéis e alertas por limiar, mas os logs são apenas semiestruturados e os rastros estão ausentes ou parciais. A correlação entre serviços é manual, e se um engenheiro consegue seguir uma requisição de ponta a ponta depende de quais equipes calham de estar envolvidas.

**Nível 3, Padronizar.** A instrumentação é documentada e imposta em toda a organização. O OpenTelemetry em todos os serviços com um ID de rastro ou de correlação propagado, o registro estruturado de logs com nomes de campo consistentes, o rastreamento distribuído, painéis curados de sinais dourados e os alertas de sintomas baseados em SLO são o padrão que toda equipe segue. Todo acionamento aponta para um runbook e se liga a um SLO, e o sobreaviso é sustentável e não uma fonte de esgotamento.

**Nível 4, Gerenciar.** O próprio patrimônio de observabilidade é medido e controlado em relação a linhas de base. Vocês acompanham a cobertura de instrumentação e a taxa de propagação do contexto de rastro entre os serviços, a fração de acionamentos atendidos versus ignorados, o tempo médio de detecção e de resolução, o atingimento dos SLOs e o consumo do orçamento de erros e o custo de telemetria por serviço contra um orçamento. As lacunas e o ruído de alertas são reduzidos com dados rumo a metas explícitas, a fidelidade da amostragem é verificada para que os registros de erros e da cauda lenta sobrevivam, e as decisões de ir ou não ir sobre cobertura e retenção são tomadas com base em evidências e não em opinião.

**Nível 5, Orquestrar.** A observabilidade é continuamente melhorada e integrada em toda a organização. A telemetria de alta cardinalidade e rica em eventos viabiliza a investigação ad hoc de qualquer fatia, os alertas são guiados por taxa de consumo de SLO com ruído mínimo e a amostragem e a retenção se adaptam à mudança de custo e de risco. A telemetria alimenta o planejamento de capacidade, a detecção de segurança e as decisões de produto como rotina, e a plataforma reajusta os próprios sinais, orçamentos e cobertura conforme o sistema, o quadro de ameaças e as obrigações regulatórias mudam.

## Ideias para discussão

- Onde fica o equilíbrio certo entre a fidelidade da telemetria e o custo para os seus serviços mais críticos?
- Como vocês decidem o que merece um acionamento versus um chamado versus apenas uma entrada em painel?
- Qual é a sua estratégia para propagar IDs de correlação entre equipes que não compartilham uma base de código nem um ciclo de lançamento?
- Como vocês preservam o poder de depuração de alta cardinalidade enquanto cumprem as exigências de privacidade e de minimização de dados?
- As ferramentas de observabilidade devem ser impostas centralmente ou escolhidas por equipe, e quais são as consequências de cada caminho?
- Como vocês demonstrariam aos auditores que a sua telemetria é completa e à prova de adulteração?

## Principais conclusões

- O monitoramento detecta problemas conhecidos. A observabilidade permite investigar os desconhecidos sem entregar código novo.
- Métricas, logs e rastros são mais valiosos quando correlacionados por identificadores compartilhados e não isolados.
- Padronizem no OpenTelemetry e no registro estruturado de logs para permanecerem neutros quanto a fornecedores e portáveis ao longo de vidas longas de sistemas.
- Alertem sobre sintomas visíveis ao usuário por meio de taxas de consumo de SLO, tornem todo acionamento acionável e podem o ruído sem trégua.
- Curem os painéis em torno de um modelo claro de saúde, como os sinais dourados, em vez de mostrar toda métrica.
- A telemetria de alta cardinalidade e rica em eventos é o que torna possível depurar problemas estreitos de produção.

## Referências e leitura complementar

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
