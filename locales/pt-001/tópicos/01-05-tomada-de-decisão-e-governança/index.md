# 1.5 Tomada de decisão e governança

## Visão geral e motivação

Todo sistema de software é a soma de milhares de decisões: qual [banco de dados](https://en.wikipedia.org/wiki/Database), qual arquitetura, qual biblioteca, se vai construir ou comprar, quando contrair dívida e quando quitá-la. Governança é como você toma essas decisões bem e de forma consistente, envolve as pessoas certas sem criar gargalos e preserva o raciocínio para que as equipes futuras não estejam condenadas a reaprendê-lo. Numa equipe pequena, as decisões acontecem em conversa e vivem na memória compartilhada. Em escala, essa memória se evapora. As pessoas saem, as equipes se reorganizam e o “porquê” de uma escolha crítica se perde, deixando os sucessores com a opção de copiá-la sem entender ou arrancá-la às cegas. Boa governança é a engrenagem que torna as decisões visíveis, deliberadas e duráveis numa organização grande e em mudança.

O desafio central para equipes grandes é equilibrar autonomia e alinhamento. Empurre todas as decisões para cima, para um conselho central, e você obtém consistência, ao custo de gargalos paralisantes e equipes sem poder. Empurre todas as decisões para baixo e você obtém velocidade, ao custo do caos: tecnologias incompatíveis, esforço duplicado e erros repetidos. A resposta madura não é nem centralização nem anarquia. É um modelo em camadas. As equipes decidem a maior parte das coisas localmente, dentro de um “caminho pavimentado” bem sinalizado, enquanto um processo leve e transparente governa as escolhas genuinamente transversais e difíceis de reverter. O objetivo é tornar as boas decisões o padrão fácil e gastar a escassa atenção de governança só onde ela realmente importa.

Empresas e governo carregam riscos maiores. Precisam satisfazer auditores, reguladores e órgãos de supervisão que exigem decisões documentadas e defensáveis. Trabalham em horizontes de tempo longos, em que uma má escolha de arquitetura ou uma pilha sem gestão de [dívida técnica](https://en.wikipedia.org/wiki/Technical_debt) pode onerá-las por uma década. E suas obrigações de contratação e conformidade tornam as decisões de construir ou comprar especialmente consequentes e difíceis de reverter. Para essas organizações, a tomada de decisão disciplinada e bem registrada não é burocracia por si mesma. É gerenciamento de riscos, memória institucional e a base da responsabilização.

## Princípios fundamentais

- Registre as decisões e o seu raciocínio. Uma decisão sem justificativa é um passivo.
- Empurre as decisões para o nível mais baixo que tenha o contexto, dentro de limites claros.
- Ajuste o peso do processo ao peso e à reversibilidade da decisão.
- Distinga decisões reversíveis (“porta de duas vias”) de irreversíveis (“porta de mão única”) e governe-as de formas diferentes.
- Prefira caminhos pavimentados e padrões a aprovações caso a caso.
- Trate a dívida técnica como um portfólio gerenciado, não como uma falha moral a esconder.
- Torne a governança transparente. A tomada de decisão oculta gera desconfiança e retrabalho.

## Recomendações

### Adote Registros de Decisão de Arquitetura e um processo de RFC na medida certa

Um [Registro de Decisão de Arquitetura](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) é um documento curto e imutável que captura uma decisão significativa: seu contexto, as opções consideradas, a escolha feita e as consequências. Armazene os ADRs no controle de versões junto com o código, para que o raciocínio viaje com o sistema. Para decisões que precisam de contribuições antes de serem tomadas, use um processo leve de [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (pedido de comentários): circule uma proposta, convide comentários por um período limitado, depois decida e registre. Mantenha ambos leves. O valor está no pensamento e no registro durável, não em modelos elaborados. Juntos, ADRs e RFCs transformam o raciocínio tácito e esquecido em memória institucional pesquisável.

### Governe por caminhos pavimentados, não por porteiros

Em vez de revisar cada decisão uma a uma, invista num “caminho pavimentado”: um conjunto de padrões abençoados e bem apoiados, linguagens, frameworks, pipelines de implantação e padrões aprovados, que as equipes possam adotar com pouco atrito e muito suporte. As equipes que ficam no caminho pavimentado precisam de pouca governança, porque a escolha segura e em conformidade também é a fácil. As equipes com uma razão genuína para sair dele podem fazê-lo, mas assumem a responsabilidade extra e uma revisão leve. Esse modelo de “caminho dourado” escala muito melhor que um conselho central aprovando tudo, porque desloca a governança da vigilância caso a caso para padrões bem desenhados.

### Use conselhos de revisão de arquitetura com parcimônia e transparência

Um conselho de revisão de arquitetura, ou seu equivalente, tem um papel legítimo para as decisões maiores, mais transversais ou mais irreversíveis, e para definir os padrões que delineiam o caminho pavimentado. Mantenha seu escopo estreito, seus critérios publicados e seu processo rápido e consultivo, não um gargalo obrigatório para o trabalho de rotina. O trabalho do conselho é zelar pela coerência e compartilhar conhecimento, não aprovar cada escolha. Quando um conselho vira uma fila em que todo projeto precisa esperar, ele falhou. Delegue com firmeza e reserve a revisão central para as poucas decisões que de fato a justificam.

### Faça de construir, comprar ou adotar uma análise deliberada

Para qualquer capacidade significativa, pese três caminhos: construí-la internamente, comprar um produto comercial ou adotar uma solução de [código aberto](https://en.wikipedia.org/wiki/Open-source_software). Construa quando a capacidade for um diferencial genuíno e central para a sua missão. Compre ou adote as capacidades indiferenciadas que outros fazem melhor. Conte o [custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), não só o preço inicial. Comprar acarreta custos de licenciamento, integração e [aprisionamento](https://en.wikipedia.org/wiki/Vendor_lock-in). Construir acarreta manutenção e pessoal perpétuos. Adotar código aberto acarreta obrigações de suporte e de acompanhamento de segurança. Registre a decisão e as suas premissas como um ADR, para poder revisitá-la quando as circunstâncias mudarem.

### Gerencie a dívida técnica como um portfólio

A dívida técnica não é inerentemente ruim. Às vezes assumi-la para entregar mais cedo é a decisão certa. O que é ruim é a dívida sem gestão, invisível e esquecida. Mantenha um inventário explícito das dívidas significativas. Para cada item, anote o custo que ele impõe (os “juros” contínuos) e o custo para corrigi-lo. Depois gerencie-o como um portfólio financeiro. Quite a dívida de juros altos que atrasa a equipe todos os dias. Tolere a dívida de juros baixos em cantos estáveis. Tome as decisões sobre dívida conscientemente, e não por acidente. Reserve uma fração permanente da capacidade para quitar dívidas, de modo que ela nunca se acumule numa crise.

### Distinga decisões reversíveis de irreversíveis

Nem todas as decisões merecem a mesma deliberação. As decisões reversíveis de “porta de duas vias” são facilmente desfeitas, então tome-as rápido e localmente, pela equipe, com viés para a ação. Agonizar sobre elas desperdiça tempo e desacelera o aprendizado. As decisões irreversíveis ou de reversão cara, de “porta de mão única”, um contrato de [API](https://en.wikipedia.org/wiki/API) público, um modelo de dados em escala, um compromisso de vários anos com um fornecedor, merecem uma deliberação lenta, cuidadosa e sênior e uma justificativa registrada. Classificar as decisões assim é um dos hábitos de governança de maior alavancagem que você tem. Ele aponta o escasso escrutínio para onde compensa e libera todo o resto.

## Compromissos: prós e contras

| Abordagem de governança | Prós | Contras |
| --- | --- | --- |
| Conselho central de revisão para tudo | Máxima consistência e supervisão | Gargalo severo. Tira o poder das equipes. Lento |
| Caminho pavimentado com autonomia local | Escala, é rápido, é um padrão seguro, empodera as equipes | Exige investimento inicial em plataforma. Algum desvio para fora do caminho |
| Autonomia total das equipes, sem governança | Rápido, alta responsabilidade | Fragmentação, duplicação, erros repetidos |
| ADRs / RFCs | Memória durável, melhores decisões, transparência | Custo de escrita. Ignorados se não forem mantidos |

| Escolha de fornecimento | Prós | Contras |
| --- | --- | --- |
| Construir | Controle total, encaixe exato, pode diferenciar | Custo perpétuo de manutenção e de pessoal |
| Comprar | Rápido, com suporte, outra pessoa mantém | Custo de licença, aprisionamento, encaixe imperfeito |
| Adotar (código aberto) | Sem taxa de licença, inspecionável, comunidade | O ônus de suporte e de segurança recai sobre você |

O compromisso unificador é controle versus velocidade, e consistência central versus autonomia local. Toda escolha de governança está nesse espectro. A postura recomendada, caminhos pavimentados mais delegação baseada em reversibilidade, compra deliberadamente a maior parte da velocidade da autonomia e mantém a consistência que importa. Ela faz isso tornando fácil a escolha alinhada e reservando o processo pesado para a rara decisão irreversível.

## Perguntas para discutir com sua equipe

1. **Quem decide se uma dada decisão é uma porta de mão única, e como você detectará classificações erradas nos dois sentidos?** Classificar as decisões por reversibilidade é um dos hábitos de governança de maior alavancagem, e seu valor desmorona se você rotula errado: trate uma escolha reversível como irreversível e a afoga em deliberação, trate uma irreversível como reversível e você entrega um modelo de dados ou contrato de API público que não consegue desfazer a baixo custo. O risco concorrente é que a pessoa mais próxima do trabalho pode ter viés para a velocidade, enquanto um conselho central pode ter viés para a cautela. Leve exemplos concretos à discussão: quanto custaria de fato, em tempo e dinheiro, reverter cada decisão, e quem arca com esse custo. Em contextos corporativos e governamentais, compromissos de contratação e dados em escala transformam muitas escolhas em portas de mão única que pareciam reversíveis de início. Combine quem classifica e crie o hábito de uma segunda opinião rápida sobre qualquer coisa perto da fronteira, para que o escasso escrutínio caia onde a reversão é genuinamente cara.

2. **Quem é dono, financia e dota de pessoal o caminho pavimentado, e o que o impede de degenerar em porteiro?** Um caminho pavimentado só funciona se os padrões abençoados forem genuinamente bem apoiados e mais fáceis que as alternativas, e isso exige um investimento sustentado que é fácil de subfinanciar. O compromisso é nítido: um caminho pavimentado sem recursos vira um conjunto de mandatos sem suporte, que é exatamente a vigilância que o modelo pretendia substituir, e as equipes então o contornam. Leve evidências da saúde do caminho: taxas de adoção, quão atuais estão as ferramentas aprovadas, a rapidez de resposta da equipe de plataforma e com que frequência as equipes pedem para sair do caminho. Para organizações grandes e regulamentadas, o caminho pavimentado é também como a escolha em conformidade se torna a fácil, então seu financiamento é um investimento em conformidade, não apenas uma conveniência. Decida um responsável claro e um orçamento permanente, e meça se as equipes escolhem o caminho porque ele é genuinamente o mais fácil.

3. **Onde as equipes estão contornando a sua governança, e o que esse shadow IT está lhe dizendo?** As equipes evitam o caminho sancionado quando ele é mais penoso que o atalho, então o shadow IT generalizado é menos um problema de disciplina e mais um veredicto de desenho sobre a sua governança. As considerações concorrentes são reais: parte da evasão é imprudente, e boa parte é uma esquiva racional de um conselho de revisão que virou uma fila de várias semanas. Leve as evidências: quais aprovações são puladas, quais ferramentas não oficiais se espalharam em silêncio e quanto tempo o caminho oficial realmente leva. Em contextos corporativos e governamentais, os riscos são maiores, porque ferramentas não sancionadas podem violar obrigações de auditoria, de segurança e de contratação que têm peso legal. Se o padrão mostra pessoas contornando um gargalo, a correção é acelerar e alargar o caminho pavimentado e reduzir o escopo do conselho às poucas decisões transversais e irreversíveis, não acrescentar mais aprovações.

4. **Quanto da nossa capacidade de entrega realmente vai para quitar dívida técnica, e conseguimos nomear os itens de juros mais altos que ela deveria atacar primeiro?** A dívida técnica se comporta como juros compostos, um imposto silencioso sobre toda mudança futura, e uma grande organização pode carregá-la por anos antes que alguém perceba que o sistema ficou lento e frágil de modificar. A pressão concorrente é direta: cada hora gasta com dívida é uma hora não gasta em funcionalidades que a liderança enxerga, então a quitação é a primeira coisa a ser cortada quando um prazo aperta. Leve evidências reais à discussão, um inventário escrito das dívidas significativas, uma estimativa honesta do custo contínuo que cada item impõe e do custo para corrigi-lo e a fração real da capacidade recente que foi para quitação versus trabalho novo. Para empresas e órgãos governamentais com horizontes de uma década, a dívida sem gestão acaba forçando uma reescrita cara ou uma constatação de auditoria, então trate uma alocação permanente de quitação como gerenciamento de riscos e decida quem a guarda quando os cronogramas escorregam.

5. **Quando precisamos do raciocínio por trás de uma decisão tomada dois anos atrás, conseguimos de fato encontrá-lo, e alguém mantém esse registro vivo?** Todo o valor de um Registro de Decisão de Arquitetura é que o raciocínio sobreviva às pessoas que o formaram, e esse valor desmorona se os ADRs são escritos uma vez, nunca consultados e ficam em silêncio desatualizados. A tensão está entre a disciplina de escrita necessária para capturar contexto, opções e consequências no momento da decisão e a pressão diária de simplesmente entregar e seguir em frente. Leve testes concretos à discussão: escolha três decisões recentes importantes e veja se alguém consegue localizar a justificativa registrada em minutos, e verifique se os ADRs substituídos estão marcados como tal, em vez de contradizer em silêncio a prática atual. Em contextos corporativos e governamentais, esse registro pesquisável é exatamente a evidência defensável que auditores e órgãos de supervisão exigem, então decida onde os ADRs vivem, quem os revisa e o que torna uma decisão significativa o bastante para ser registrada.

6. **Quando foi a última vez que reabrimos uma grande decisão de construir ou comprar contra as premissas originais, e perceberíamos quando essas premissas expirassem?** As escolhas de fornecimento estão entre as decisões mais caras e difíceis de reverter que você toma, e as premissas por trás delas (o preço de um fornecedor, sua própria equipe, a maturidade de uma opção de código aberto) ficam obsoletas em silêncio enquanto a decisão permanece congelada. As considerações concorrentes pesam o custo irrecuperável e a perturbação de trocar contra o custo crescente do aprisionamento, de um encaixe imperfeito ou de um fardo de manutenção que você não quer mais. Leve o ADR original e as suas premissas declaradas, uma estimativa atual de custo total de propriedade para cada caminho incluindo licenciamento, integração, pessoal e custo de saída, e qualquer sinal, uma mudança de preço ou um rebaixamento de suporte, de que uma premissa mudou. Para compradores governamentais e regulamentados, regras de contratação e contratos de vários anos tornam essas portas de mão única especialmente vinculantes, então combine de antemão os gatilhos e a cadência que forçarão uma nova decisão deliberada em vez de uma renovação às cegas.

## Perspectiva por setor

**Startup.** Governe quase nada e se apoie com força na velocidade: para escolhas reversíveis de porta de duas vias, decida na mesa e siga em frente. Reserve seu único hábito de governança para o punhado de portas de mão única, um modelo de dados central ou um fornecedor fundamental, e registre cada uma num único parágrafo para que um futuro colega não precise rediscutir tudo do zero. Pule conselhos de revisão e caminhos pavimentados por completo, porque no seu tamanho são custos que você não pode bancar e a equipe toda já compartilha o contexto.

**Pequena empresa.** Sem arquiteto na equipe, faça de construir ou comprar a sua principal pergunta de governança e responda-a pelo custo total de propriedade, e não por preferência. Compre ou adote por padrão ferramentas bem apoiadas para tudo que não seja seu diferencial central, porque a manutenção perpétua é o custo que você menos pode carregar. Mantenha um único registro leve de decisões para que o raciocínio por trás das suas poucas escolhas consequentes sobreviva à saída de uma pessoa-chave.

**Grande empresa.** Seu problema é equilibrar autonomia e alinhamento entre muitas equipes, então invista num caminho pavimentado financiado e reserve um conselho de revisão de arquitetura estreito e rápido para as decisões genuinamente transversais e irreversíveis. Padronize os ADRs para que o raciocínio se torne memória institucional pesquisável e gerencie a dívida técnica e as escolhas de fornecimento como portfólios com orçamentos permanentes. Meça se as equipes escolhem o caminho porque ele é o mais fácil e reduza qualquer conselho que tenha degenerado em fila.

**Governo.** Decisões documentadas e defensáveis não são opcionais aqui: auditores e órgãos de supervisão esperam ver o raciocínio, as opções pesadas e as premissas por trás de toda escolha consequente. Conduza construir ou comprar como uma análise registrada de custo total de propriedade, respeite as regras de contratação que restringem o aprisionamento por fornecedor único e mantenha os ADRs como a trilha de evidências pronta para auditoria. Leve a sério os horizontes de tempo longos, porque um modelo de dados ou compromisso com fornecedor assumido hoje pode vincular a organização por uma década, então classifique-o como porta de mão única e delibere de acordo.

## Exemplos

**Startup.** Uma startup de quatro pessoas toma a maioria das decisões em minutos, numa mesa compartilhada, e para escolhas reversíveis de porta de duas vias essa velocidade é uma vantagem real, então resiste a qualquer custo de governança. Mas quando escolhe um banco de dados e um modelo de dados que serão dolorosos de mudar depois (uma porta de mão única), faz uma pausa para escrever uma nota de um parágrafo: as opções, a escolha e as premissas por trás dela. Um ano depois, ao chegar a limites de escala, essa única nota os poupa de rediscutir a questão do zero. Governam quase nada e reservam seu único hábito leve para as poucas decisões genuinamente caras de reverter.

**Grande empresa.** As equipes de plataforma de uma grande empresa estavam paralisadas por um conselho de revisão de arquitetura que precisava aprovar toda escolha de tecnologia, criando filas de várias semanas. A empresa reestruturou a governança em torno de um caminho pavimentado: um catálogo curado de linguagens, armazenamentos de dados e pipelines aprovados e totalmente apoiados que as equipes podiam adotar na hora. Os ADRs registravam qualquer decisão de se desviar, e uma revisão rápida e consultiva tratava apenas das escolhas fora do caminho. O escopo do conselho encolheu para a definição de padrões e o punhado de decisões realmente transversais. A entrega acelerou muito. A consistência na verdade melhorou, porque o caminho fácil agora era o que estava em conformidade. E o arquivo de ADRs deu à organização um registro pesquisável de por que as coisas foram construídas como foram.

**Governo.** Um departamento governamental enfrentava uma grande decisão de construir ou comprar para uma plataforma de gestão de casos sob regras estritas de contratação e auditoria. Em vez de decidir por preferência, conduziu uma análise documentada de custo total de propriedade em três opções: construir sob medida, comprar um produto comercial e adotar uma base de código aberto. Pesou licenciamento, integração, manutenção de longo prazo, pessoal e aprisionamento, e registrou a decisão e as suas premissas como um ADR. Anos depois, quando os termos de um fornecedor mudaram, o departamento revisitou esse ADR, constatou que as premissas originais já não valiam e decidiu de novo com pleno conhecimento do raciocínio anterior, evitando uma migração cega e cara. A justificativa registrada era também exatamente a evidência defensável que os auditores exigiam.

## Justificativa de negócio: motivações, ROI e TCO

As decisões são o custo de maior alavancagem e menor visibilidade em software. Uma única escolha ruim e irreversível de arquitetura ou de fornecimento pode impor anos de arrasto ou uma remediação de nove dígitos. Governá-la bem, algumas horas de deliberação e um registro escrito, custa quase nada em comparação. O retorno dos ADRs e da delegação baseada em reversibilidade vem de duas fontes: evitar erros caros nas decisões de porta de mão única e evitar deliberação desperdiçada e retrabalho em todo o resto. A justificativa registrada também reduz drasticamente o custo recorrente de rediscutir questões já resolvidas e de equipes fazendo engenharia reversa da intenção por trás de sistemas herdados.

A dívida técnica torna concreto o argumento do TCO. A dívida sem gestão se comporta exatamente como juros compostos: um imposto crescente sobre toda mudança futura, até que o sistema se torne efetivamente impossível de manter e exija uma reescrita cara. Gerenciar a dívida como um portfólio, com uma alocação permanente de capacidade para quitar os itens de juros altos, é muito mais barato que a crise final. Boa governança é barata de adotar, principalmente a disciplina de pôr as decisões por escrito e o investimento inicial num caminho pavimentado. Pulá-la é caro: você paga em reescritas evitáveis, surpresas de aprisionamento, falhas de auditoria e memória institucional perdida. Para convencer a liderança, apresente a governança na linguagem dela: redução de risco, retrabalho evitado, entrega mais rápida pelo caminho pavimentado e defensabilidade pronta para auditoria. Mostre que o objetivo não é mais processo, mas processo mais bem apontado, escrutínio pesado só onde a reversão é cara e velocidade sem atrito em todo o resto.

## Antipadrões e armadilhas

- Decisões não documentadas: o raciocínio se perde no momento em que as pessoas que o formaram saem.
- Gargalo do conselho de aprovação: um órgão central atrás do qual todo projeto precisa fazer fila.
- Processo de tamanho único: forçar decisões reversíveis triviais por uma revisão pesada.
- Paralisia por análise: agonizar sobre decisões de porta de duas vias facilmente reversíveis.
- [Shadow IT](https://en.wikipedia.org/wiki/Shadow_IT): equipes que evitam a governança por completo porque o caminho sancionado é penoso demais.
- Dívida técnica invisível: dívida nunca inventariada, nunca quitada, se acumulando em silêncio.
- Reflexos de construir tudo ou comprar tudo: fornecimento por hábito em vez de análise de TCO.
- Teatro de governança: documentos e conselhos que existem pela aparência, mas não moldam as decisões.

## Modelo de maturidade

- Nível 1 (Iniciar): As decisões são ad hoc e não registradas. A governança é ou ausente ou um gargalo generalizado. A dívida técnica é invisível e o raciocínio por trás das escolhas se evapora quando as pessoas saem.
- Nível 2 (Desenvolver): Algumas decisões são documentadas e existe alguma revisão, mas a prática é inconsistente entre as equipes e o processo muitas vezes é incompatível com o peso e a reversibilidade da decisão.
- Nível 3 (Padronizar): ADRs, um caminho pavimentado, delegação baseada em reversibilidade e um inventário de dívida são documentados e aplicados em toda a organização, de modo que a escolha em conformidade seja o padrão fácil e o raciocínio seja pesquisável.
- Nível 4 (Gerenciar): A governança é medida em relação a linhas de base: adoção do caminho pavimentado, cobertura de ADRs, tempo de ciclo das decisões, dívida como parcela da capacidade e taxas de exceção fora do caminho são acompanhadas, e as decisões de quitar dívida ou de revisitar o fornecimento são disparadas por essa evidência, e não por crise.
- Nível 5 (Orquestrar): A governança é continuamente ajustada e integrada ao planejamento de entrega e de risco. O escrutínio é apontado com precisão para as decisões irreversíveis. A dívida e as escolhas de fornecimento são ativamente reequilibradas como portfólios e redecididas com base em evidências à medida que as circunstâncias mudam.

## Ideias para discussão

- Para as nossas decisões recentes mais importantes, conseguimos encontrar o raciocínio registrado por trás delas?
- Onde a nossa governança é um gargalo e onde ela está ausente quando é necessária?
- Quais das nossas decisões atuais são portas de mão única, e as estamos tratando como tal?
- Quanto da nossa capacidade vai para quitar dívida técnica, e é suficiente?
- Nossas equipes seguem o caminho pavimentado porque ele é genuinamente o mais fácil, ou o contornam?
- Quando foi a última vez que revisitamos uma grande decisão de construir ou comprar contra as premissas originais?

## Principais conclusões

- Registre as decisões significativas e a sua justificativa com ADRs. Torne o raciocínio durável.
- Governe por caminhos pavimentados e padrões, não por vigilância caso a caso.
- Ajuste o peso do processo ao peso e à reversibilidade da decisão. Delegue as portas de duas vias, delibere sobre as de mão única.
- Analise construir, comprar ou adotar pelo custo total de propriedade e registre as premissas.
- Gerencie a dívida técnica como um portfólio explícito com uma alocação permanente de quitação.
- Mantenha a governança transparente e leve. Aponte o escasso escrutínio para onde a reversão é cara.

## Referências e leitura complementar

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
