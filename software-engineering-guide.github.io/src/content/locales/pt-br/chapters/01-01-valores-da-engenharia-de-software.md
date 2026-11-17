# 1.1 Valores da engenharia de software

## Visão geral e motivação

Os valores da [engenharia de software](https://en.wikipedia.org/wiki/Software_engineering) são as crenças compartilhadas, as normas e os comportamentos cotidianos que moldam como as pessoas constroem software juntas. Eles não são os cartazes na parede nem as palavras do manual do funcionário. Eles são o que realmente acontece quando um incidente acorda alguém às 3 da manhã, quando uma pessoa júnior discorda de uma pessoa principal ou quando um prazo colide com a qualidade. Os valores são o sistema invisível por baixo de toda decisão técnica.

Numa equipe pequena, os valores se espalham por osmose: as pessoas sentam juntas, absorvem as normas e se autocorrigem. Numa equipe maior, a osmose falha. Agora é preciso tornar os valores explícitos, escrevê-los, fazer com que as lideranças os pratiquem e reforçá-los por meio dos seus sistemas. Se você pular essa etapa, a cultura se fragmenta em dezenas de microculturas incompatíveis que taxam silenciosamente toda colaboração.

Para uma equipe maior, o que está em jogo é estrutural. Valores fracos aparecem como rotatividade, decisões lentas, conhecimento acumulado e incidentes repetidos cujas causas-raiz nunca são totalmente corrigidas. Valores fortes aparecem como mudanças rápidas, seguras e confiáveis: as pessoas engenheiras levantam problemas cedo, aprendem com a falha e assumem a responsabilidade. A distância entre esses dois estados costuma ser maior que a de qualquer escolha de tecnologia.

Empresas e organizações governamentais sentem isso de forma aguda, porque trabalham em escala, sob escrutínio e em horizontes longos. Sistemas construídos hoje podem rodar por uma década ou mais, mantidos por pessoas que nunca conheceram os autores originais. Nesses contextos, a cultura é o que carrega a intenção ao longo do tempo e da rotatividade.

Empresas regulamentadas enfrentam mais uma pressão: a tentação de substituir confiança por processo. Quando a responsabilização é alta e os erros são visíveis, o reflexo é empilhar controles, aprovações e culpa. É compreensível, mas sai pela culatra. As organizações mais confiáveis, seguras e em conformidade costumam ser as de culturas de aprendizado mais fortes, não as mais punitivas. Valores e conformidade são aliados, não opostos.

## Princípios fundamentais

- A [segurança psicológica](https://en.wikipedia.org/wiki/Psychological_safety) é a base. Sem ela, toda outra prática se degrada.
- A falha é dado. O aprendizado sem atribuição de culpa transforma incidentes em melhoria duradoura.
- Responsabilidade significa prestar contas por resultados, não só por entregas: “você constrói, você opera”.
- Escrever é pensar. Uma cultura que registra suas decisões por escrito escala o seu discernimento.
- Ritmo sustentável vence o heroísmo. O [esgotamento profissional](https://en.wikipedia.org/wiki/Occupational_burnout) é uma falha de sistema, não pessoal.
- [Diversidade, equidade e inclusão](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) são forças da engenharia que melhoram a qualidade das decisões.
- Os valores são modelados de cima para baixo e reforçados de baixo para cima. As ações das lideranças pesam mais que suas palavras.

## Recomendações

### Construa segurança psicológica de forma deliberada

Segurança psicológica é a crença compartilhada de que você pode se manifestar, fazer perguntas, admitir erros e questionar decisões sem medo de humilhação ou punição. É o mais forte preditor isolado da eficácia de equipes em estudos de larga escala. Construa-a de propósito. Faça com que as lideranças assumam os próprios erros em voz alta (“eis um erro que cometi e o que aprendi”). Receba más notícias com curiosidade, não com punição. Convide a divergência abertamente nas reuniões. Alterne quem fala primeiro, para que as vozes seniores não ancorem a discussão. E torne normal dizer “não sei” e “preciso de ajuda”.

### Pratique o aprendizado sem atribuição de culpa

Quando algo quebra, olhe para as condições que permitiram a falha, não para a pessoa que a desencadeou. Adote [postmortems](https://en.wikipedia.org/wiki/Postmortem_documentation) sem atribuição de culpa: um registro escrito do que aconteceu, a linha do tempo, os fatores contribuintes e itens de ação concretos, com responsáveis e datas. Parta da premissa de que todos agiram de forma razoável diante do que sabiam na hora. Pergunte “o que tornou isto fácil de errar?” em vez de “quem errou?”. E acompanhe os itens de ação até a conclusão. Uma cultura de postmortem que nunca fecha seus acompanhamentos é só teatro.

### Estabeleça modelos claros de responsabilidade

“Você constrói, você opera” torna a equipe que escreve um serviço responsável por operá-lo, incluindo o sobreaviso. Isso aperta o ciclo de feedback entre as decisões de projeto e a dor operacional, e melhora a qualidade. Combine isso com um catálogo de serviços que registre, para cada sistema, quem é responsável por ele, como contatá-lo, suas dependências e seus runbooks. Mantenha a responsabilidade explícita e sem sobreposição. Responsabilidade ambígua é como os sistemas apodrecem e os incidentes se arrastam. Quando uma equipe realmente não consegue operar um sistema sozinha, dê a ela apoio de plataforma em vez de diluir a responsabilidade.

### Cultive uma cultura de escrita

Escrever afia o pensamento e cria artefatos que atravessam fusos horários e anos. Torne rotineiros os documentos de projeto e os registros de decisão para mudanças significativas: um documento curto que declare o problema, as opções consideradas, a abordagem proposta e os compromissos, circulado para comentários antes de construir. Isso traz as discordâncias à tona cedo, enquanto ainda são baratas, e deixa um registro durável de por que você decidiu o que decidiu. Mantenha modelos leves e expectativas proporcionais ao peso da decisão. E recompense a boa escrita em público.

### Proteja o ritmo sustentável

A cultura do herói, em que poucas pessoas resgatam repetidamente a organização com esforço insustentável, é sintoma de fraqueza, não virtude. Ela esgota as pessoas, concentra o conhecimento de forma perigosa e esconde os problemas subjacentes que você deveria estar corrigindo. Portanto, meça e gerencie a carga de sobreaviso. Se uma pessoa é acionada constantemente, trate isso como um defeito a eliminar por engenharia. Torne normal tirar folga, proteja o tempo de foco e julgue a produção ao longo de um trimestre, não de uma semana.

### Trate a DEI como uma força da engenharia

Equipes diversas tomam melhores decisões. Elas pesam mais perspectivas e caem com menos frequência no [pensamento de grupo](https://en.wikipedia.org/wiki/Groupthink) e em pontos cegos, o que importa enormemente para acessibilidade, segurança e atendimento a populações amplas. Incorpore a inclusão à sua engenharia cotidiana: documentação acessível, linguagem inclusiva no código e nas interfaces, práticas de reunião que deixam vozes mais quietas contribuir e uma divisão justa tanto do trabalho glamoroso quanto do trabalho de cola.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
| --- | --- | --- |
| Postmortems sem atribuição de culpa | Revelam causas-raiz reais. Constroem confiança. Impulsionam correções sistêmicas | Podem parecer “sem responsabilização” para quem está de fora. Exigem disciplina para concluir as ações |
| “Você constrói, você opera” | Ciclo de feedback de qualidade estreito. Responsabilidade clara | Carga de sobreaviso. Precisa de forte apoio de plataforma para evitar esgotamento |
| Cultura de documentos primeiro / RFC | Decisões duráveis. Escala apesar da rotatividade. Amigável ao assíncrono | Mais lenta para mudanças triviais. Risco de burocracia se aplicada em excesso |
| Ritmo sustentável | Retenção, confiabilidade, velocidade de longo prazo | Parece mais lento em períodos de aperto. Exige que a liderança sustente a linha |

A tensão central é velocidade de curto prazo versus saúde de longo prazo. Heroísmo e culpa compram uma explosão de aparente controle, seguida de um colapso lento da moral e da confiabilidade. Aprendizado sem atribuição de culpa, responsabilidade e ritmo sustentável parecem mais lentos em qualquer semana isolada, mas se acumulam em uma velocidade muito maior ao longo de trimestres e anos. As lideranças precisam estar dispostas a absorver o desconforto de curto prazo para proteger a capacidade de longo prazo.

## Perguntas para discutir com sua equipe

1. **Como evitar que “sem atribuição de culpa” seja lido como “sem responsabilização” por auditores, executivos e pelo público?** Numa empresa regulamentada ou numa agência governamental sob supervisão, um postmortem que não nomeia nenhum culpado pode parecer um acobertamento para quem está fora da engenharia. As considerações concorrentes são reais: você precisa da honestidade que só a ausência de culpa produz, e também precisa que os tomadores de decisão confiem em que as falhas são tratadas. Leve evidências concretas à discussão, como sua taxa de recorrência de incidentes e a taxa de conclusão dos itens de ação dos postmortems, porque um sistema que fecha de forma confiável os seus acompanhamentos é visivelmente responsável, mesmo sem um bode expiatório. Separe duas perguntas que a cultura da culpa funde: o que tornou isto fácil de errar, e alguém agiu com negligência genuína ou má-fé. Se sua resposta é que a responsabilização está em corrigir as condições e fechar as ações, publique esse mecanismo para que os de fora vejam a responsabilização que procuram.

2. **Quais equipes carregam sistemas de sobreaviso que não conseguem realisticamente operar, e quem paga por essa lacuna?** “Você constrói, você opera” aperta o ciclo de feedback e pressupõe que uma equipe tem o apoio de plataforma para operar o que construiu. Na escala corporativa e governamental, algumas equipes herdam sistemas legados, caixas-pretas de fornecedores ou infraestrutura transversal que nenhuma equipe pequena consegue realmente possuir sozinha. O compromisso está entre diluir a responsabilidade (ruim) e preparar uma equipe para falhar num pager que ela não consegue atender (também ruim). Leve os dados de acionamentos: se uma pessoa ou uma equipe é acionada constantemente, trate isso como um defeito a eliminar por engenharia, não como uma medalha de honra. A resposta deve dizer onde investir em equipes de plataforma, lançamentos em estágios e runbooks atualizados, para que a responsabilidade permaneça clara e a carga operacional permaneça humana.

3. **Os comportamentos que você de fato promove correspondem aos valores que você publica?** Os valores decaem em cinismo no momento em que as lideranças premiam o que os cartazes condenam, e em escala essa lacuna permanece invisível até que a rotatividade e o acúmulo silencioso de conhecimento a revelem. Olhe com atenção para o seu último ciclo de promoções: ele premiou o combate a incêndios e o heroísmo, ou a prevenção de incêndios e o trabalho de cola que mantém saudável uma equipe grande? Empresas e órgãos governamentais agravam o risco, porque sistemas rígidos de graus e longas permanências deixam um incentivo desalinhado rodar por anos antes que alguém corrija. Leve evidências reais, como quem foi promovido, quem foi elogiado em público e o que essas pessoas de fato fizeram. Se o heroísmo recebe as recompensas, você está treinando a sua organização para fabricar as crises que depois celebra resolver, e a correção é mudar os incentivos, não a arte na parede.

4. **Como você realmente saberia se a segurança psicológica de uma determinada equipe é alta ou baixa, em vez de presumi-la a partir do organograma?** A segurança é a base sobre a qual toda outra prática repousa, e também é a coisa mais fácil de se enganar a respeito, porque as equipes com menos segurança são as menos propensas a contar a você. Em escala, a média entre mil pessoas esconde a variância que importa: um gestor pode, discretamente, conduzir uma equipe baseada no medo dentro de uma organização, de resto saudável. As considerações concorrentes são franqueza versus conforto, já que as perguntas de pesquisa que revelam problemas reais são as que as pessoas têm mais relutância em responder com honestidade, e coletar o sinal pode, em si, parecer inseguro. Leve evidências concretas em vez de impressões: resultados por equipe de um instrumento validado de segurança, a taxa em que as pessoas admitem erros por escrito, relatos de quase-acidentes que surgiram antes de virar incidentes e temas de entrevistas de desligamento. Numa empresa ou órgão governamental, insista em que os dados permaneçam no nível da equipe e nunca sejam usados para punir uma equipe de pontuação baixa, porque no momento em que uma pontuação de segurança vira um porrete, ela deixa de medir segurança e passa a medir o medo da medição.

5. **Qual é a sua carga real de sobreaviso e de heroísmo, e você está premiando quem previne incêndios ou quem os combate?** O ritmo sustentável é onde as boas intenções silenciosamente colapsam sob a pressão de entrega, e uma grande organização pode funcionar por anos com as horas extras invisíveis de umas poucas pessoas exaustas antes de perceber. A tensão é honesta: o heroísmo realmente salva você no momento, e depender dele concentra conhecimento, esconde defeitos sistêmicos e esgota os seus engenheiros mais comprometidos. Leve os dados operacionais à discussão: acionamentos por pessoa por semana, implantações fora do horário, a distribuição da carga de sobreaviso na equipe e quanto dela cai sobre os mesmos poucos nomes mês após mês. Olhe também para quem o seu último ciclo de promoções recompensou. Em empresas e órgãos governamentais com escadas de graus rígidas e longas permanências, uma cultura que paga pelo combate a incêndios pode persistir sem contestação por uma década, então a resposta deve dizer onde reduzir o pager por engenharia e como tornar a prevenção de incêndios um ato visivelmente promovível.

6. **Quais decisões significativas dos últimos dois anos não têm registro escrito do seu raciocínio, e quanto isso custará quando os autores se forem?** Uma cultura de escrita é o que carrega a intenção através da rotatividade, e sua ausência é invisível até o momento em que alguém precisa mudar um sistema que ninguém mais entende. A força contrária é a velocidade: escrever um documento de projeto ou um registro de decisão parece atrito no momento e, aplicado em excesso, azeda em burocracia que atrasa mudanças triviais. Leve evidências para calibrar: a fatia de mudanças relevantes que tem documento de projeto ou registro de decisão, com que frequência as pessoas conseguem de fato encontrar e citar o raciocínio por trás de uma arquitetura existente e quanto tempo uma pessoa nova leva para ficar produtiva num serviço não documentado. Para empresas e organizações governamentais cujos sistemas sobrevivem à permanência de todos que os construíram, e que podem enfrentar auditoria ou escrutínio de acesso à informação, o registro escrito é ao mesmo tempo memória institucional e evidência de diligência devida, então a resposta deve traçar a linha onde o peso da decisão justifique a escrita e nada abaixo disso.

## Perspectiva por setor

**Startup.** Os valores ainda se espalham por osmose, então não importe processo pesado, mas nomeie o comportamento ou dois que mais importam, geralmente honestidade sem atribuição de culpa sobre os erros e uma inclinação a trazer más notícias cedo. Os fundadores dão o tom ao assumir os próprios erros em voz alta, porque numa equipe minúscula uma única reação ríspida no Slack pode ensinar todo mundo a esconder problemas por meses. Sua pista curta é um motivo para proteger a segurança, não para pulá-la: uma equipe que esconde bugs custa muito mais que uma retrospectiva de cinco minutos.

**Pequena empresa.** Sem especialista dedicado em cultura de engenharia e com orçamento apertado, apoie-se em rituais leves em vez de ferramentas que você precise comprar ou manter. Um canal compartilhado de incidentes, um registro de decisões de uma página e o hábito de perguntar “o que tornou isto fácil de errar?” não custam nada e carregam a maior parte do valor. Seja deliberado também na fronteira entre comprar e construir para as práticas: adote um modelo pronto de postmortem e uma escala simples de sobreaviso em vez de construir um sistema sob medida que você não consegue manter.

**Grande empresa.** Em escala, a tarefa é consistência sem uniformidade: aprendizado sem atribuição de culpa, responsabilidade clara e sem sobreposição e uma cultura de escrita tornam-se normas da organização inteira, com ferramentas, expectativas e um catálogo de serviços por trás. Governança e auditoria empurram você para controles, então defenda que uma forte cultura de aprendizado é a opção mais confiável e em conformidade, e mostre isso com métricas de recorrência de incidentes e de fechamento de itens de ação. Observe a variância entre equipes, porque as médias escondem os bolsões baseados no medo que vazam talento e conhecimento em silêncio.

**Governo.** Regras de aquisição, obrigações de transparência e responsabilização pública moldam como os valores são expressos, especialmente em torno da culpa. Um postmortem que não nomeia nenhum culpado pode ser lido como acobertamento por órgãos de controle externos, então publique o mecanismo, mostrando que a responsabilização está em corrigir condições e fechar ações, e deixe cidadãos e auditores vê-lo. Como os sistemas sobrevivem às administrações e a rotatividade de pessoal se mede em anos, trate os registros de decisão escritos tanto como memória institucional quanto como evidência de diligência devida sob escrutínio de acesso à informação.

## Exemplos

**Startup.** Uma startup de seis pessoas funciona na confiança e na conversa de corredor, então ninguém escreve os valores da equipe. Quando um fundador-engenheiro envia uma migração ruim e o CTO o repreende rispidamente no Slack, a sala silencia, e os dois bugs seguintes são escondidos em vez de trazidos à tona. A equipe se recupera adotando um hábito leve: uma conversa de cinco minutos, sem atribuição de culpa, sobre “o que tornou isto fácil de errar?” depois de cada incidente, sem modelo necessário. Esse pequeno ritual mantém saudável a cultura osmótica sem o custo de processo que uma organização maior exigiria.

**Grande empresa.** Uma grande empresa de serviços financeiros sofreu uma grande interrupção quando uma mudança rotineira de configuração se propagou em cascata pelos serviços. Numa cultura de culpa, o engenheiro que enviou a mudança teria sido repreendido, e esse seria o fim. Em vez disso, um postmortem sem atribuição de culpa mostrou que a ferramenta de implantação fazia a mudança perigosa parecer idêntica a uma segura, que não existia lançamento em estágios e que o runbook estava desatualizado. A empresa investiu em lançamentos progressivos e validação de configuração, e mudanças semelhantes agora falham com segurança. Escolher olhar para o sistema em vez de para a pessoa produziu uma melhoria de engenharia duradoura.

**Governo.** Uma agência de serviços digitais do governo adotou “você constrói, você opera” junto com um rigoroso processo de [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (pedido de comentários) com documentos primeiro. Como seus sistemas precisam sobreviver a mudanças de administração política e a uma rotatividade de pessoal medida em anos, toda decisão significativa é registrada em um documento de projeto que explica o contexto e os compromissos. Engenheiros novos, e contratados que chegam, podem ler o raciocínio por trás de uma arquitetura de dez anos em vez de fazer engenharia reversa dela. Essa [memória institucional](https://en.wikipedia.org/wiki/Institutional_memory) escrita é o que permite à agência manter confiáveis os serviços públicos apesar da alta rotatividade e de exigências rigorosas de responsabilização.

## Justificativa de negócio: motivações, ROI e TCO

O retorno sobre a cultura é real, mas indireto, razão pela qual é cronicamente subfinanciado. Ao longo da vida de um sistema, o custo dominante não é construí-lo. É manutenção, resposta a incidentes, retrabalho e o custo de perder e recontratar pessoas qualificadas. Uma forte cultura de aprendizado melhora cada um desses itens. Postmortems sem atribuição de culpa reduzem incidentes repetidos. Responsabilidade clara reduz o tempo médio de recuperação. Uma cultura de escrita reduz o custo de [integração](https://en.wikipedia.org/wiki/Onboarding) e o custo de decisões tomadas sem conhecer o raciocínio anterior.

Considere só a rotatividade. Substituir um engenheiro de nível pleno costuma custar entre metade e duas vezes o seu salário anual, contando recrutamento, curva de aprendizado e o conhecimento institucional que sai pela porta. Se uma cultura mais saudável reduz a rotatividade lamentada em apenas alguns pontos percentuais numa organização de mil pessoas, a economia faz sombra ao custo modesto de conduzir postmortems e escrever documentos. O custo de adoção é principalmente atenção da liderança e um pouco de custo de processo. O custo de não adotar é pago de forma contínua e invisível: entrega mais lenta, incidentes recorrentes e fuga silenciosa de talentos.

Para defender o caso junto à liderança, conecte a cultura a métricas que os executivos já acompanham: tempo de espera de entrega, taxa de falha de mudanças, tempo médio de recuperação, recorrência de incidentes e rotatividade lamentada. Apresente a segurança psicológica não como um benefício intangível, mas como o mecanismo que faz todo outro investimento de engenharia render, porque equipes inseguras escondem exatamente os problemas que esses investimentos pretendem corrigir.

## Antipadrões e armadilhas

- Revisões de incidentes de culpa e vergonha: empurram os problemas para a clandestinidade e as pessoas param de relatar.
- Culto ao herói: premiar o combate a incêndios em vez da prevenção perpetua os incêndios.
- “Valores” que as lideranças violam: valores declarados contrariados pelo comportamento geram cinismo.
- Responsabilidade sem apoio: atribuir sobreaviso para sistemas que as equipes não conseguem realisticamente operar.
- Processo como substituto da confiança: empilhar aprovações em vez de construir segurança genuína.
- Teatro de documentos: escrever documentos que ninguém lê ou que nunca influenciam decisões.
- Inclusão como caixa de seleção: contratar por diversidade enquanto exclui essas mesmas vozes das decisões.

## Modelo de maturidade

- Nível 1, Iniciar: Os valores são acidentais e guiados por personalidades. Incidentes significam culpa, o conhecimento vive em poucas cabeças e o heroísmo é como as coisas são feitas. Ninguém escreveu no que a equipe acredita nem como ela se comporta sob pressão.
- Nível 2, Desenvolver: Algumas equipes começam postmortems sem atribuição de culpa, escrevem um documento de projeto ocasional e falam sobre responsabilidade, mas as práticas são inconsistentes, aplicadas de forma desigual e ainda não reforçadas pela liderança. Cair numa equipe saudável é, em grande parte, sorte.
- Nível 3, Padronizar: Aprendizado sem atribuição de culpa, responsabilidade clara e sem sobreposição e uma cultura de escrita são normas documentadas na organização inteira, com modelos, um catálogo de serviços e expectativas definidas de sobreaviso. As lideranças modelam os valores e os mesmos comportamentos são esperados em toda parte, não apenas onde um bom gestor por acaso está.
- Nível 4, Gerenciar: A cultura é medida em relação a linhas de base e controlada com dados. Você acompanha pontuações de segurança psicológica por equipe, recorrência de incidentes, taxa de fechamento de itens de ação de postmortems, distribuição da carga de sobreaviso, tempo médio de recuperação e rotatividade lamentada, e age sobre os números quando uma equipe se desvia. Elimine incentivos ao combate a incêndios com base em evidências e recompense a prevenção de incêndios porque agora você consegue vê-la.
- Nível 5, Orquestrar: A cultura é continuamente melhorada e integrada à forma como a organização inteira planeja, contrata e promove. A segurança é alta, o aprendizado é rápido e as práticas se adaptam conforme evidências e contexto mudam. A organização reequilibra a carga de sobreaviso, atualiza os registros de decisão e evolui suas normas deliberadamente em vez de esperar que uma crise force a questão.

## Ideias para discussão

- Onde em nossa organização as pessoas não se sentem seguras para dizer “não sei” ou “discordo”, e por quê?
- Nossas revisões de incidentes mudam o sistema, ou apenas atribuem culpa e seguem em frente?
- Estamos premiando heroísmos que deveríamos eliminar por engenharia?
- Quais decisões importantes dos últimos dois anos não têm registro escrito do seu raciocínio?
- Com que equilíbrio o trabalho de cola e a carga de sobreaviso estão distribuídos na equipe?
- Nossos valores declarados correspondem ao que de fato faz alguém ser promovido aqui?

## Principais conclusões

- Os valores são o sistema operacional invisível por trás de toda decisão técnica. Em escala, precisam ser explícitos.
- A segurança psicológica é fundamental. Sem ela, as demais práticas decaem.
- O aprendizado sem atribuição de culpa converte a falha em melhoria sistêmica duradoura.
- A responsabilidade clara (“você constrói, você opera”) aperta o ciclo de feedback de qualidade.
- A cultura de escrita escala o discernimento entre fusos horários e rotatividade.
- Ritmo sustentável e inclusão são multiplicadores de velocidade de longo prazo, não custos.

## Referências e leitura complementar

- Amy C. Edmondson, "The Fearless Organisation" and "Teaming"
- Google re:Work / Project Aristotle research on team effectiveness
- Sidney Dekker, "The Field Guide to Understanding 'Human Error'"
- John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate: The Science of Lean Software and DevOps"
- Gene Kim et al., "The Phoenix Project" and "The DevOps Handbook"
- Camille Fournier, "The Manager's Path"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Tom DeMarco and Timothy Lister, "Peopleware: Productive Projects and Teams"
