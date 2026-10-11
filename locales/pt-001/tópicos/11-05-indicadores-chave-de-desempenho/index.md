# 11.5 Indicadores-chave de desempenho (KPIs)

## Visão geral e motivação

Um **[indicador-chave de desempenho](https://en.wikipedia.org/wiki/Performance_indicator) (KPI)** é uma métrica que a sua organização escolhe deliberadamente acompanhar porque reflete a saúde contínua de algo que importa. A palavra *chave* carrega o peso aqui: um KPI não é qualquer número que vocês possam coletar, mas o pequeno conjunto pelo qual decidiram que vale a pena conduzir. Onde um objetivo e resultado-chave (OKR) descreve uma mudança que vocês estão conduzindo agora, um KPI descreve o estado estável que vocês estão protegendo. Este é o jeito mais limpo de manter os dois separados: os OKRs são a mudança que vocês querem; os KPIs são a saúde que vocês sustentam. O capítulo 11.4 é o capítulo companheiro sobre OKRs, sua cadência e sua avaliação; este capítulo trata de escolher KPIs, defini-los e protegê-los da distorção.

Para grandes equipes, a disciplina que um bom KPI impõe vale tanto quanto a métrica em si. Nas empresas, dezenas de equipes perseguem números locais que divergem em silêncio da estratégia, e um único KPI bem escolhido pode alinhar centenas de pessoas em torno do valor que os clientes de fato recebem. No governo, programas plurianuais comprometem fundos públicos contra mandatos legislados, e “entregamos os módulos do termo de referência” não é defesa se os tempos de espera ou a fraude nunca melhoraram. Um KPI mal escolhido corrompe em silêncio: uma central de atendimento medida em *chamadas encerradas por hora* encerrará chamadas, não resolverá problemas.

Este capítulo trata de acertar essas escolhas, e os guardrails ao redor delas. O capítulo 11.1 apresenta brevemente os KPIs como parte do pipeline de descoberta; aqui vocês têm a profundidade. As apostas são altas porque um KPI é uma instrução disfarçada de medição. As pessoas otimizam o que vocês contam, então o que vocês contam é melhor que seja o que vocês querem.

## Princípios fundamentais

- **Chave, não muitos.** Um KPI é uma das poucas métricas pelas quais vocês escolheram conduzir, não tudo o que podem coletar.
- **Mensurável, acionável e com dono.** Todo KPI tem uma definição precisa, uma fonte da verdade, um dono e uma alavanca que o move.
- **Saúde, não mudança.** Os KPIs acompanham o estado estável que vocês protegem; os OKRs (capítulo 11.4) conduzem a mudança que vocês querem.
- **Antecipem onde puderem, confirmem onde precisarem.** Prefiram indicadores antecedentes; usem os consequentes para verificar.
- **Pesem em direção aos resultados.** Insumos e saídas são fáceis de contar; o valor vive nos resultados.
- **Presumam que toda métrica será manipulada.** Projetem contra a [lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law) com razões, coortes e guardrails pareados.
- **Rejeitem a vaidade.** Se nenhuma leitura mudaria uma decisão, a métrica é decoração.
- **Visualizem com honestidade.** Um painel deve informar em segundos sem enganar.

## Recomendações

### Definam o que faz um KPI ser “bom”

Um bom KPI passa em quatro testes. É **alinhado**: remonta a uma meta declarada, então movê-lo significa algo. É **mensurável**: uma definição precisa, uma **fonte da verdade** nomeada (o sistema autoritativo de registro), uma unidade e um método de coleta, para que duas pessoas que o calculem separadamente cheguem ao mesmo número. É **acionável**: a equipe dona tem alavancas que de fato o movem. É **com dono**: uma pessoa ou equipe responsável responde por sua tendência, sua definição e a qualidade dos seus dados. Uma métrica que falha em qualquer um dos quatro testes é candidata à exclusão, não a um painel. A maior parte da bagunça de métricas nas grandes organizações são números que falham em pelo menos dois desses testes e nunca foram aposentados.

### Classifiquem as métricas por tempo e por cadeia de valor

Duas lentes mantêm um conjunto de KPIs equilibrado. A primeira é o tempo. Um **indicador antecedente** é preditivo e movível agora (inscrições em testes, conclusão da integração); um **indicador consequente** é confirmatório e lento (receita anual, cancelamentos). Os indicadores antecedentes permitem conduzir antes que os consequentes entreguem um veredicto que vocês já não podem mudar. A segunda lente é a cadeia de valor. Uma **métrica de insumo** mede o esforço gasto (horas trabalhadas, dólares aplicados); uma **métrica de saída** mede o que o sistema produziu (funcionalidades entregues, chamados fechados); uma **métrica de resultado** mede a mudança que vocês de fato queriam (receita retida, tempo de espera reduzido). As equipes gravitam para insumos e saídas porque são fáceis de contar e inteiramente sob seu controle, mas o valor vive nos resultados. Pesem o seu conjunto em direção aos resultados e tratem um painel todo de saídas como sinal de alerta.

### Projetem métricas que resistam à manipulação

Presumam a lei de Goodhart: quando uma medida vira meta, deixa de ser uma boa medida. Projetem contra ela desde o começo em vez de reagir depois de a distorção aparecer.

- **Prefiram razões e taxas a contagens brutas.** “Chamados fechados” recompensa o volume; “porcentagem resolvida no primeiro contato” recompensa a resolução. Uma contagem bruta é manipulável fazendo mais de algo sem valor.
- **Usem coortes.** Uma **coorte** é um grupo definido por um ponto de partida compartilhado (todos os usuários que se inscreveram em março). Relatar por coorte impede que uma tendência em declínio se esconda dentro de um agregado lisonjeiro sustentado por um mês recente forte.
- **Pareiem todo KPI incentivado com um guardrail.** Uma **métrica guardrail** é uma contramétrica pareada que não deve se degradar enquanto vocês empurram a principal: tempo médio de atendimento pareado com a satisfação do cliente, ativação pareada com a carga de suporte. O guardrail torna visivelmente cara a trapaça.

### Rejeitem as métricas de vaidade; exijam acionabilidade

Uma **métrica de vaidade** sobe de modo confiável, parece impressionante e não muda nenhuma decisão: usuários registrados acumulados, visualizações de página, linhas de código. Os sinais são consistentes. Só sobe. É uma contagem absoluta e não uma taxa. E não tem resposta para a pergunta “o que faríamos diferente se este número dobrasse?”. Uma **métrica acionável**, ao contrário, liga-se a um comportamento específico que vocês podem influenciar e a uma decisão que ela mudaria. Antes de adotar qualquer KPI, perguntem que ação uma boa leitura e uma má leitura disparariam. Se as duas leituras levam ao mesmo comportamento, descartem a métrica. Só este teste reduzirá à metade a maioria dos painéis propostos.

### Construam uma árvore de KPIs sob uma única métrica estrela-guia

Não acompanhem os KPIs como uma lista plana. Arranjem-nos como uma **árvore de KPIs** (ou árvore de métricas): uma métrica de topo decomposta nas métricas que a conduzem matemática ou causalmente, nível por nível, até as medidas operacionais de que as equipes individuais são donas. A árvore diz qual métrica inferior investigar quando uma de topo se move, o que transforma “o número caiu” em “o tempo de permanência deste hub é a causa”. No topo, nomeiem uma única **métrica estrela-guia (north-star)**: a medida que melhor capta o valor central entregue aos clientes. Para um marketplace pode ser transações concluídas; para um produto, o uso ativo semanal da funcionalidade central. Uma estrela-guia alinha o esforço e impede que os departamentos otimizem números locais conflitantes, mas só se mede valor e não vaidade, e só se guardrails a equilibram. Se a sua métrica de topo pudesse continuar subindo enquanto os clientes recebiam menos valor, é vaidade vestida de estratégia.

### Definam linhas de base, metas e limiares

Um KPI sem ponto de referência é só um número numa tela. Deem a cada um três referências. Uma **linha de base** é o valor atual ou histórico, para que uma mudança seja significativa e não misteriosa. Uma **meta** é o valor que vocês pretendem alcançar, com uma data. Os **limiares** disparam ação antes que uma meta seja ganha ou perdida: um **limiar de alerta** chama a atenção, e um **limiar crítico** chama a intervenção. Fundamentem as metas em evidências (uma tendência passada, um benchmark externo ou um modelo de capacidade) em vez de otimismo de número redondo e escrevam o raciocínio. O raciocínio registrado é o que permite a um erro ensinar algo em vez de apenas decepcionar, porque vocês podem comparar o que aconteceu com a suposição que definiu a meta.

### Visualizem com honestidade nos painéis

Um painel de KPIs deve deixar o leitor captar status e tendência em segundos sem ser enganado. Mostrem a tendência ao longo do tempo, não um instantâneo isolado. Comecem os eixos de valor em zero a menos que tenham uma razão declarada para não fazê-lo, porque eixos truncados exageram pequenas mudanças em dramáticas. Mostrem a variação e a incerteza em vez de falsa precisão. Anotem o contexto para que o leitor distinga uma mudança real de ruído: implantações, incidentes, sazonalidade, mudanças de política. Evitem os truques de gráfico que lisonjeiam um número: eixos duplos que sugerem uma correlação, intervalos de datas escolhidos a dedo e efeitos 3-D que distorcem proporções. Essas práticas se ligam diretamente à análise e inteligência de negócios (capítulo 7.3) e à análise de produto e experimentação (capítulo 7.4), em que os mesmos padrões de honestidade governam como vocês leem o que uma métrica está dizendo.

### Adotem os vocabulários de KPIs operacionais

A saúde operacional tem vocabulários de KPIs bem estabelecidos que vocês devem reutilizar em vez de reinventar. Da engenharia de confiabilidade de sites (capítulo 9.1): um **indicador de nível de serviço (SLI)** é um sinal medido da saúde do serviço (latência, taxa de sucesso); um **objetivo de nível de serviço (SLO)** é a faixa-alvo de um SLI (99,9% das requisições têm sucesso); e o **orçamento de erros** é a falta permitida (os 0,1% que vocês podem gastar em risco antes de parar de entregar e estabilizar). Do pipeline de entrega (capítulo 11.2): as **métricas de fluxo** acompanham o trabalho pelo sistema (tempo de fluxo, [vazão](https://en.wikipedia.org/wiki/Throughput), [trabalho em andamento](https://en.wikipedia.org/wiki/Work_in_process), eficiência do fluxo), e as quatro métricas do programa [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA) pareiam velocidade com estabilidade: frequência de implantação, prazo de entrega das mudanças, taxa de falha das mudanças e tempo para restaurar o serviço. Os dois vocabulários põem a velocidade ao lado da estabilidade por projeto, de modo que nenhuma equipe possa postar um ótimo número de velocidade sacrificando em silêncio a confiabilidade. Esses mesmos KPIs operacionais alimentam o trabalho de eficácia de engenharia e produtividade de desenvolvedores (capítulo 1.10).

### Cumpram os deveres de relato de desempenho do setor público

O governo acrescenta uma exigência distinta: os KPIs são frequentemente **medidas de desempenho publicadas** reportadas a legislaturas, órgãos de supervisão e ao público, às vezes por estatuto. Tratem-nas com rigor extra. Mantenham a definição estável entre os períodos de relato, para que uma tendência seja genuinamente comparável de um ano para o outro. Documentem a metodologia e a fonte dos dados. Sejam honestos sobre as limitações. Como uma medida publicada cria fortes incentivos, é especialmente propensa à distorção de Goodhart: uma meta de reduzir uma lista de espera é cumprida redefinindo quem conta como esperando. Pareiem cada medida publicada com guardrails e auditem a própria definição, não só o número. A pergunta mais importante sobre um KPI público muitas vezes não é “melhorou?”, e sim “ainda mede o que alegava medir?”.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| **Métricas de resultado** | Alinham o esforço ao impacto real. Difíceis de manipular | Difíceis de definir. Lentas, ruidosas. A atribuição é difícil |
| **Métricas de insumo/saída** | Fáceis de medir. Responsabilidade clara. Feedback rápido | Recompensam atividade acima de impacto. Elo fraco com o valor |
| **Indicadores antecedentes** | Permitem conduzir cedo | Preditivos, portanto mais ruidosos e menos certos |
| **Indicadores consequentes** | Confirmação autoritativa | Chegam tarde demais para mudar o resultado |
| **Poucos KPIs** | Foco, clareza, fáceis de comunicar | Podem perder dimensões. Pontos cegos |
| **Muitos KPIs** | Cobertura ampla. Menos surpresas | Atenção diluída. Fadiga de painel. Sinais conflitantes |
| **Relato público de desempenho** | Prestação de contas, transparência, confiança | Forte pressão de manipulação. As definições viram políticas |

A tensão central é **foco versus cobertura**, afiada por **motivação versus distorção**. Vocês querem medidas suficientes para ver o quadro todo, poucas o bastante para uma equipe de fato agir sobre elas e cada uma protegida para que o ato de incentivá-la não a corrompa. Resolvam a tensão mantendo um pequeno conjunto de KPIs com dono e pesados para resultados, arranjados numa árvore sob uma métrica estrela-guia, e pareando toda medida incentivada com um guardrail. A cobertura então vem da estrutura da árvore e não do mero número de métricas na tela.

## Perguntas para discutir com sua equipe

1. **Vocês têm uma única métrica estrela-guia, e ela mede valor entregue ou apenas atividade?** Uma lista plana de KPIs deixa os departamentos otimizarem números locais conflitantes, enquanto uma estrela-guia alinha todos no valor que os clientes de fato recebem: transações concluídas para um marketplace, ativação para um produto. Perguntem se a sua métrica de topo continuaria subindo se os clientes estivessem recebendo *menos* valor, porque se pode, é vaidade vestida de estratégia. Numa grande organização a estrela-guia é o que impede a vitória de uma equipe de ser a derrota de outra, então precisa ficar no topo de uma árvore de KPIs das medidas operacionais que as equipes controlam. Levem a sua métrica de topo atual e tentem rastreá-la até aquilo de que cada equipe é dona. Se a árvore não conecta, a estrela-guia é decoração e não um mecanismo de condução.

2. **Para cada KPI incentivado, qual é a forma mais barata de manipulá-lo, e que guardrail exporia essa trapaça?** Toda métrica a que vocês atam uma recompensa ou uma reputação convida à otimização do número e não do resultado, e o caminho mais barato raramente é o que vocês pretendiam. Sentem-se e, para cada KPI, projetem deliberadamente o abuso: como uma equipe racional faria este número parecer bom fazendo menos do que vocês de fato querem? Depois nomeiem a contramétrica que o pegaria (tempo de atendimento pareado com satisfação, ativação pareada com chamados de suporte, velocidade pareada com taxa de erro). Esse exercício importa mais para as métricas que vocês reportam para cima ou publicam, porque carregam os incentivos mais fortes e, portanto, a pressão de distorção mais forte. Se vocês não conseguem nomear um guardrail para um KPI, ainda não estão prontos para incentivá-lo.

3. **As suas metas são fundamentadas em evidências, e vocês escreveram o raciocínio por trás de cada uma?** Um KPI sem linha de base é só um número, e uma meta definida num valor redondo porque soava ambicioso não pode ser interpretada quando vocês a erram. Para cada KPI, conferiram se carrega uma linha de base, uma meta com data, limiares de alerta e crítico e uma justificativa registrada tirada de uma tendência passada, um benchmark ou um modelo de capacidade. Isso importa mais para medidas que carregam peso estatutário ou contratual, em que “pagar 90% dos pedidos válidos em 21 dias” precisa ser defensável e não um palpite aspiracional. Levem as metas atuais e perguntem, para cada uma, “por que este número e não um maior ou menor?”. Se a resposta é silêncio, a meta foi otimismo, e um erro não ensinará nada.

4. **Se vocês tivessem de defender cada métrica do painel principal, quais sobreviveriam, e quanto cada uma não usada está custando?** Todo KPI carrega um custo recorrente: instrumentação, pipelines, um bloco do painel e uma fatia de atenção em cada revisão, então um conjunto que cresceu por acréscimo taxa em silêncio a organização sem ninguém ter decidido que devia. A tensão é foco versus cobertura: poucas métricas e vocês desenvolvem pontos cegos, muitas e nenhuma equipe consegue agir sobre qualquer uma. Levem o inventário completo e, para cada métrica, respondam que decisão uma boa ou uma má leitura dispararia; as que não têm resposta são decoração que vocês pagam para manter. Para uma empresa com dezenas de painéis de equipe, ou um órgão público que reporta contra um arcabouço estatutário, a disciplina de aposentar métricas importa tanto quanto a de acrescentá-las, porque uma medida publicada não usada ainda convida à manipulação e ainda precisa ser defendida em auditoria.

5. **Que parcela do seu painel mede o resultado que vocês de fato queriam, em vez do esforço gasto ou da saída produzida?** As equipes derivam para insumos e saídas porque são fáceis de contar e ficam inteiramente sob o controle da equipe, mas o valor vive nos resultados, que são mais lentos, mais ruidosos e mais difíceis de atribuir. Contem os blocos: se um painel é quase todo funcionalidades entregues, chamados fechados e horas registradas, mede atividade e a chama de desempenho. Levem cada métrica classificada como insumo, saída ou resultado e sejam honestos sobre quais decisões mudariam se só o resultado se movesse. Numa grande organização esse equilíbrio é onde a otimização local se esconde, porque uma divisão pode postar excelentes números de saída por anos enquanto o resultado de que o financiador se importa, receita retida ou espera reduzida, se erode em silêncio; no governo um relato só de saídas (“módulos entregues”) é precisamente a resposta em que os órgãos de supervisão aprenderam a desconfiar.

6. **Para cada KPI, quem é dono da sua definição e fonte da verdade, e duas equipes que o calculassem de forma independente chegariam ao mesmo número?** Uma métrica sem um dono responsável e um sistema autoritativo de registro vira uma discussão permanente, já que dois grupos relatam “usuários ativos” a partir de consultas diferentes e passam a reunião reconciliando números em vez de gerir a tendência. A atração contrária é autonomia versus consistência, pois as equipes querem instrumentar do seu jeito, mas um KPI que significa coisas diferentes em salas diferentes não pode se consolidar numa estrela-guia compartilhada. Levem a definição, a unidade, a fonte da verdade e o dono nomeado de cada métrica e testem algumas pedindo a duas pessoas que as calculem do zero. Para empresas que consolidam métricas entre unidades de negócio, e para medidas governamentais mantidas estáveis entre períodos de relato por estatuto, uma definição à deriva ou contestada não é um incômodo, é a falha que torna indefensável um relatório de desempenho inteiro.

## Perspectiva por setor

**Startup.** Com um punhado de pessoas e pouco fôlego, todo o painel da empresa deve caber numa tela: uma única métrica estrela-guia que mede se os clientes continuam recebendo valor, seus dois ou três condutores e um guardrail. Aposentem cedo as contagens de vaidade como inscrições acumuladas, antes que moldem decisões, e separem a estrela-guia em coortes por semana de inscrição para que um lançamento forte não esconda o cancelamento por baixo. A velocidade importa mais que um conjunto rico de métricas, então instrumentem só os poucos números sobre os quais vocês de fato agirão e pulem o resto.

**Pequena empresa.** Vocês provavelmente não têm analista nem tempo para construir pipelines, então apoiem-se nos vocabulários de KPIs já embutidos nas ferramentas que possuem: os painéis do seu ponto de venda, suporte ou software contábil. Escolham duas ou três medidas que mapeiem a sobrevivência (taxa de recompra, dias de caixa disponíveis, entrega pontual) e deem a cada uma uma linha de base e uma meta em vez de ver contagens brutas à deriva. Prefiram razões que vocês leiam num relance a relatórios que precisam montar à mão.

**Grande empresa.** O problema são dezenas de equipes otimizando números locais conflitantes, então o trabalho é uma árvore de KPIs sob uma estrela-guia, definições precisas com uma fonte da verdade nomeada e um guardrail em toda medida incentivada. Padronizem as definições para que uma métrica se consolide limpa entre as unidades de negócio, integrem SLIs, SLOs e métricas DORA operacionais com os KPIs de negócio e governem o conjunto como um portfólio que é podado e não apenas cultivado. Auditem as definições, não só os números, porque em escala uma métrica redefinida em silêncio engana milhares de pessoas de uma vez.

**Governo.** Os KPIs costumam ser medidas de desempenho publicadas, reportadas a legislaturas por estatuto, então mantenham cada definição estável entre os períodos, documentem a metodologia e a fonte dos dados e sejam honestos sobre as limitações. As metas publicadas carregam a maior pressão de manipulação, então pareiem cada uma com guardrails e encomendem uma auditoria independente da própria definição, confirmando que (por exemplo) os requerentes que ainda esperam não são reclassificados para fora da contagem. Definam o sucesso como resultados para o cidadão e não como módulos entregues, porque “entregamos o termo de referência” não é resposta a uma legislatura que pergunta se os tempos de espera ou a fraude de fato melhoraram.

## Exemplos

**Startup.** Uma startup de seis pessoas de um aplicativo de produtividade comemora um gráfico crescente de “total de usuários registrados” até um membro do conselho perguntar se alguém de fato continua usando o produto. Aposentam essa contagem de vaidade e adotam a ativação em 7 dias como métrica estrela-guia, separada em coortes por semana de inscrição para que um lançamento forte não esconda o cancelamento por baixo. Dão-lhe uma linha de base (25%), uma meta (45%) e limiares de alerta e crítico, e a pareiam com um guardrail (chamados de suporte por usuário ativo) para não inflar a ativação com um fluxo de integração insistente. Todo o painel da empresa cabe numa tela: a estrela-guia, seus dois condutores e o guardrail. Quando o KPI tende ao limiar de alerta, sabem pela árvore qual condutor investigar primeiro.

**Grande empresa.** Uma empresa global de logística adota a *taxa de entrega pontual* como sua métrica estrela-guia e constrói uma árvore de KPIs sob ela: pontualidade de coleta, tempo de permanência no hub e sucesso na última milha, cada uma de que um líder regional nomeado é dono, com uma linha de base, uma meta e limiares de alerta e crítico. Cada KPI de velocidade é pareado com um guardrail, de modo que a taxa de pontualidade viaja com a taxa de avarias e nenhuma região consegue bater seu número apressando pacotes até quebrarem. Os SLOs da plataforma (99,95% de disponibilidade da API de rastreamento, capítulo 9.1) e as métricas DORA (capítulo 11.2) ficam no painel de engenharia ao lado dos KPIs de negócio. Quando a taxa de pontualidade cai em direção ao limiar de alerta numa região, a árvore aponta o tempo de permanência daquele hub como causa, e o conserto é direcionado e não uma correria de toda a empresa. As métricas que a equipe decide *mover* neste trimestre viram resultados-chave nos OKRs daquela equipe (capítulo 11.4); o resto permanece como guardrails permanentes.

**Governo.** Uma agência estadual de seguro-desemprego reporta a *mediana de dias do pedido ao primeiro pagamento* como sua medida de desempenho publicada, separada em coortes por mês do pedido para que um bom trimestre não mascare um backlog piorando, em vez da contagem de vaidade de “pedidos processados”. Ela pareia essa medida com guardrails (precisão do pagamento e taxa de reversão em recursos) para que a velocidade não possa ser comprada com erros. A definição de “mediana de dias” é congelada ao longo dos anos e documentada publicamente, e uma auditoria independente confere a própria definição, confirmando que os requerentes que ainda esperam não são reclassificados em silêncio para fora da contagem. Os SLIs da linha de frente (disponibilidade do portal, taxa de atendimento de chamadas) alimentam o painel operacional sob as medidas publicadas. Como o sucesso é definido como *resultados para os requerentes* e não como *módulos entregues*, a agência pode mostrar à legislatura valor público mensurável que sobrevive ao escrutínio.

## Justificativa de negócio: motivações, ROI e TCO

O retorno de um bom KPI vem do **foco e do alinhamento**, que evitam o maior custo oculto das grandes organizações: muitas equipes trabalhando duro, dentro do prazo, em coisas que não fazem avançar a estratégia. Quando o pequeno conjunto de medidas que importam é explícito e visível, o esforço duplicado aparece, as metas locais contraditórias são reconciliadas antes de colidir e o trabalho de baixo valor perde sua cobertura. O recurso mais caro de uma grande organização é a atenção alinhada de suas pessoas, e o retorno dominante dos KPIs é a capacidade redirecionada.

O custo do KPI *errado* não é o painel. São trimestres de esforço otimizando um número enquanto o resultado real se erode, mais o custo de desfazer depois o comportamento manipulado. Uma central de atendimento que passou um ano minimizando o tempo de atendimento e maximizando os contatos repetidos produziu retorno negativo inteiramente por uma única métrica bem-intencionada, e depois teve de reconstruir tanto o processo quanto a confiança da equipe.

O **[custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO)** de um KPI é modesto mas real e recorrente. Cada métrica carrega um custo contínuo: instrumentação e pipelines para coletá-la, painéis para exibi-la, reuniões de revisão para discuti-la e a carga mental de mais uma coisa a vigiar. Esse custo recorrente é o argumento mais forte para um conjunto *pequeno* em que todo KPI justifica sua permanência, porque uma métrica não usada ainda custa dinheiro para manter. Mantenham o conjunto pequeno, as definições precisas e os guardrails no lugar, e os seus KPIs repõem sua sobrecarga muitas vezes em desvios evitados.

## Antipadrões e armadilhas

- **Métricas de vaidade:** contagens acumuladas que só sobem e não mudam nenhuma decisão.
- **Fixação em métricas:** o comportamento otimiza o número, não o resultado, porque nenhum guardrail expõe a diferença.
- **KPIs sem dono ou mal definidos:** nenhuma pessoa responsável, ou duas equipes calculando “usuário ativo” de modos diferentes e discutindo em vez de gerir.
- **Painéis só de saídas:** tudo o que se mede é o que a equipe produziu; nada mede a mudança que ela causou.
- **Uma lista plana sem árvore:** dezenas de mostradores e nenhuma estrela-guia, então um número que se move não dá pista de onde olhar.
- **Metas de número redondo sem justificativa:** um objetivo escolhido porque soava ousado, impossível de interpretar quando errado.
- **Gráficos desonestos:** eixos truncados ou duplos, janelas escolhidas a dedo e efeitos 3-D que fabricam uma história.
- **Medidas publicadas manipuladas por redefinição:** uma meta de lista de espera cumprida mudando quem conta como esperando.
- **Confundir KPIs com OKRs:** tratar uma métrica de saúde permanente como meta de mudança trimestral, ou vice-versa (capítulo 11.4).

## Modelo de maturidade

- **Nível 1, Iniciar:** As métricas são em sua maioria contagens de vaidade sem linhas de base, metas, donos nem definições compartilhadas. Os painéis mostram instantâneos sem tendência, o relato é reativo e ad hoc e ninguém sabe dizer qual número mais importa.
- **Nível 2, Desenvolver:** Existem KPIs para algumas equipes com linhas de base e metas, mas são em sua maioria saídas, as definições variam entre as equipes e os guardrails estão ausentes. A prática é inconsistente na organização, e a manipulação aparece e não é reconhecida como manipulação.
- **Nível 3, Padronizar:** Um conjunto coerente de KPIs com dono tem definições precisas e uma fonte da verdade nomeada, documentadas e impostas em toda a organização. As métricas são classificadas como antecedentes ou consequentes e como insumo, saída ou resultado; as medidas incentivadas são pareadas com guardrails; e os gráficos seguem padrões de visualização honesta em todas as equipes.
- **Nível 4, Gerenciar:** O próprio conjunto de KPIs é medido e controlado em relação a linhas de base. A precisão das definições, as taxas de erro de qualidade dos dados e a frequência com que cada métrica é manipulada são acompanhadas ao longo do tempo; as metas são revisadas contra evidências a cada ciclo; os limiares de alerta e crítico disparam intervenções documentadas; e as definições são auditadas para que uma medida publicada ainda meça o que alegava. Os efeitos de Goodhart são monitorados deliberadamente em vez de descobertos depois do dano.
- **Nível 5, Orquestrar:** Uma árvore de KPIs liga as medidas da linha de frente a uma única métrica estrela-guia; as métricas de resultado dominam o conjunto; e os SLIs, SLOs e as métricas DORA e de fluxo operacionais se integram aos KPIs de negócio. As métricas que uma equipe escolhe mover alimentam com limpeza seus OKRs (capítulo 11.4), e a organização continuamente aposenta, substitui e redefine o escopo dos KPIs conforme a estratégia e o quadro de risco mudam.

## Ideias para discussão

1. Quais dos seus KPIs continuariam subindo mesmo que o produto ou o serviço estivesse piorando?
2. Para cada KPI incentivado, qual é a forma mais barata de manipulá-lo, e que guardrail exporia essa trapaça?
3. Quantas das métricas do seu painel são resultados, e quantas são insumos ou saídas que vocês contam porque são fáceis?
4. Quais das suas métricas carecem de dono ou de uma definição única acordada, e quanto essa ambiguidade custou em discussões?
5. Para uma medida que vocês reportam ou publicam, a meta poderia ser cumprida redefinindo a medida em vez de melhorar o resultado?
6. Se vocês tivessem de cortar o painel para cinco métricas, quais sobreviveriam, e há uma estrela-guia no topo dessas cinco?

## Principais conclusões

- Um **KPI** é uma métrica escolhida porque reflete uma meta que vocês querem proteger; um bom KPI é **alinhado, mensurável, acionável e com dono**.
- **Os OKRs são a mudança que vocês querem; os KPIs são a saúde que vocês sustentam.** Para OKRs, cadência e avaliação, vejam o capítulo 11.4.
- Classifiquem as métricas como **antecedentes ou consequentes** e **insumo, saída ou resultado**, e pesem o seu conjunto em direção aos **resultados**.
- Presumam a **lei de Goodhart**: pareiem todo KPI incentivado com um **guardrail** e prefiram **razões e coortes** a contagens brutas.
- Rejeitem as **métricas de vaidade**; organizem os KPIs numa **árvore** sob uma única **métrica estrela-guia**; deem a cada um uma **linha de base, meta e limiares**.
- Visualizem com **honestidade** (capítulos 7.3 e 7.4) e reutilizem os vocabulários operacionais: **SLIs, SLOs e orçamentos de erros** (capítulo 9.1) e **métricas DORA e de fluxo** (capítulo 11.2).
- No governo, tratem as **medidas publicadas** com rigor extra de definição e auditem a definição, não só o número.

## Referências e leitura complementar

- *Key Performance Indicators: Developing, Implementing, and Using Winning KPIs*, by David Parmenter (a practical framework for selecting and structuring KPIs).
- *Lean Analytics*, by Alistair Croll and Benjamin Yoskovitz (vanity versus actionable metrics, and the One Metric That Matters).
- *The Lean Startup*, by Eric Ries (actionable versus vanity metrics, and cohort analysis).
- *How to Measure Anything*, by Douglas W. Hubbard (defining and quantifying the seemingly unmeasurable).
- *The Visual Display of Quantitative Information*, by Edward R. Tufte (honest, high-integrity data graphics).
- *Site Reliability Engineering*, by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds. (SLIs, SLOs, and error budgets).
- *Accelerate*, by Nicole Forsgren, Jez Humble, and Gene Kim (the DORA delivery and stability metrics).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law; see also Marilyn Strathern's widely quoted formulation.
- U.S. Government Accountability Office (GAO) guidance on performance measurement and the GPRA Modernisation Act: public-sector performance-reporting practice.
