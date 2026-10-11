# 10.1 Gestão de portfólio e de programas

## Visão geral e motivação

A [gestão de programas](https://en.wikipedia.org/wiki/Program_management) e de portfólio é a disciplina de decidir o que uma grande organização de engenharia deve construir, financiar esse trabalho ao longo do tempo, sequenciá-lo entre muitas equipes e conduzi-lo a resultados estratégicos em vez de produções isoladas. Uma única equipe pode se virar com alinhamento informal e um backlog compartilhado. Uma empresa ou agência governamental que roda dezenas ou centenas de equipes não pode. Todo esse trabalho compete pelo mesmo orçamento escasso, pelas mesmas habilidades especializadas, pelas mesmas plataformas compartilhadas e pela mesma atenção da liderança. Sem uma camada deliberada de portfólio, vocês acabam com otimização local: toda equipe ocupada, todo roteiro plausível e, ainda assim, o conjunto entregando muito menos valor estratégico do que deveria.

Para grandes equipes as apostas se compõem. O esforço duplicado, as prioridades desalinhadas e as dependências entre equipes não geridas tributam em silêncio toda iniciativa. Uma funcionalidade que uma equipe poderia entregar num sprint espera três trimestres porque depende de uma equipe de plataforma que nunca ouviu falar dela. No governo o problema é ainda mais agudo. Dotações anuais, financiamento de capital plurianual, lei de contratação e prestação de contas públicas significam que um programa mal enquadrado pode prender uma agência a anos de gasto comprometido na coisa errada. Acertar a [gestão de portfólio](https://en.wikipedia.org/wiki/Project_portfolio_management) não é, portanto, sobrecarga burocrática. É como uma grande organização transforma estratégia em software entregue.

Este capítulo trata a gestão de portfólio e de programas como uma preocupação de liderança de engenharia, não apenas como uma função de [escritório de gestão de projetos (PMO)](https://en.wikipedia.org/wiki/Project_management_office). O objetivo é ligar estratégia e objetivos a roteiros, priorizar com honestidade sob restrições reais, tratar dependências e fornecedores como riscos de primeira classe e navegar os ciclos de orçamento e de contratação, especialmente os ritmos plurianuais de financiamento que dominam o trabalho do setor público.

## Princípios fundamentais

- **Resultados em vez de produções.** Financiem e meçam a mudança no mundo (adoção, custo, confiabilidade, resultados da missão), não o volume de funcionalidades entregues.
- **A estratégia precisa ser legível.** Toda equipe deve poder rastrear seu trabalho até um pequeno número de objetivos publicados.
- **Priorizar é subtrair.** Um portfólio que diz sim a tudo não tem estratégia. O valor está no que vocês deliberadamente não fazem.
- **As dependências são o cronograma real.** Para grandes organizações, o custo de coordenação, não o esforço de programação, costuma ser a restrição que amarra.
- **Financiem equipes duráveis, não projetos temporários.** Equipes estáveis e alinhadas ao produto superam grupos de pessoal remontados por projeto.
- **Combinem a cadência de financiamento com a cadência de aprendizado.** Comprometam dinheiro em incrementos que permitam parar, mudar de rumo ou dobrar a aposta conforme a evidência chega.
- **Os fornecedores são extensões do portfólio, não estão fora dele.** O trabalho de contratados e de [integradores de sistemas](https://en.wikipedia.org/wiki/Systems_integrator) deve ser governado com a mesma visibilidade do trabalho interno.

## Recomendações

### Alinhe a engenharia à estratégia e aos OKRs

Publiquem um pequeno conjunto de objetivos de nível organizacional (idealmente de três a cinco) e façam a cascata de forma leve. Deixem as equipes definir seus próprios resultados-chave a serviço desses objetivos compartilhados em vez de entregar-lhes tarefas atribuídas. Mantenham a cascata rasa: dois ou três níveis no máximo, ou o tecido conectivo entre a estratégia e o trabalho diário vira ficção. Revisem os objetivos numa cadência fixa (tipicamente trimestral para o progresso, anual para os próprios objetivos) e aposentem ou reescrevam abertamente os que não importam mais. Resistam a transformar os [OKRs](https://en.wikipedia.org/wiki/OKR) (objetivos e resultados-chave) numa arma de avaliação de desempenho. No instante em que os resultados-chave conduzem bônus individuais, as equipes subestimam as metas e vocês perdem o sinal.

### Faça roteiros com intenção e horizontes honestos

Mantenham os roteiros em várias altitudes. Um roteiro de portfólio mostra temas e resultados ao longo de trimestres; os roteiros de equipe mostram entregas de curto prazo. Enquadrem-nos em torno de problemas e resultados, com a confiança decrescendo com o tempo. Horizontes “agora / em seguida / depois” comunicam a incerteza muito melhor que [gráficos de Gantt](https://en.wikipedia.org/wiki/Gantt_chart) datados, que implicam falsa precisão. Revisitem os roteiros numa cadência regular e tratem-nos como compromissos com uma direção, não como contratos de datas específicas num futuro distante.

### Priorize com frameworks explícitos e compromissos nomeados

Escolham um método de priorização leve e consistente e apliquem-no de modo uniforme, para poder comparar em todo o portfólio. As opções comuns incluem a pontuação ponderada (valor, custo, risco, ajuste estratégico), o [custo do atraso](https://en.wikipedia.org/wiki/Cost_of_delay) (o valor perdido a cada unidade de tempo que uma entrega valiosa espera) e sua variante Weighted-Shortest-Job-First (WSJF), e o RICE (alcance, impacto, confiança, esforço). Nenhuma fórmula decide por vocês. O valor real de um framework é forçar as suposições a aparecer, onde os líderes podem discuti-las. Registrem sempre o compromisso que estão fazendo (o que estão adiando e por quê) para poder revisitar a decisão quando os fatos mudarem.

### Gerencie as dependências entre muitas equipes

Tornem as dependências visíveis antes que mordam. Mantenham um mapa ou registro de dependências que nomeie, para cada iniciativa significativa, o que ela precisa de outras equipes e até quando. Usem um evento regular de planejamento entre equipes (uma sessão trimestral de planejamento em sala grande é comum nos frameworks escalados) para trazer à tona e negociar as dependências às claras. Melhor ainda, eliminem-nas por projeto: invistam em plataformas de autoatendimento, APIs bem documentadas e contratos internos claros para que as equipes possam seguir sem esperar umas pelas outras. Deem a toda dependência transversal um único dono responsável. As dependências sem dono são onde os programas escorregam em silêncio.

### Governe fornecedores, contratados e integradores de sistemas

Tratem os parceiros externos de entrega como parte do portfólio. Peçam a mesma visibilidade sobre seus backlogs, velocidade, qualidade e riscos que vocês esperam internamente. Estruturem os contratos em torno de resultados e de software funcionando entregue em incrementos, não de volumes de documentação ou de corpos em assentos. Mantenham capacidade técnica interna suficiente para especificar o trabalho, julgar a qualidade e assumir se um fornecedor falhar. Nunca terceirizem a função de comprador inteligente. Protejam-se do [aprisionamento](https://en.wikipedia.org/wiki/Vendor_lock-in) (lock-in) sendo donos dos seus dados, exigindo interfaces abertas e insistindo em cláusulas de saída e de transição desde o primeiro dia.

### Navegue a contratação, o orçamento e o financiamento plurianual

Entendam o ritmo de financiamento em que operam e projetem os programas para se ajustar a ele. No governo, especialmente, as dotações podem ser anuais enquanto os sistemas levam anos para ser construídos, o que cria pressão para gastar antes do fim do ano e para superdimensionar o compromisso inicial. Contrariem isso de três modos: estruturem os programas em incrementos independentemente valiosos (contratação modular), busquem autoridade para financiamento incremental e ágil onde as regras permitirem e construam estimativas genuínas de custo que separem construção, operação e sustentação. Envolvam cedo a [contratação](https://en.wikipedia.org/wiki/Procurement), as finanças e o jurídico (eles moldam o que é possível muito mais do que a maioria dos engenheiros percebe) e traduzam os planos técnicos para as categorias orçamentárias e as fronteiras de ano fiscal de que essas funções precisam.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Controle centralizado do portfólio | Forte alinhamento estratégico. Menos duplicação. Compromissos de financiamento mais fáceis | Decisões mais lentas. Pode suprimir a autonomia das equipes e a inovação local |
| Autonomia descentralizada das equipes | Equipes rápidas e motivadas. Expertise local honrada | Duplicação. Coerência estratégica fraca. Risco oculto entre equipes |
| Financiamento por projeto | Escopo e responsabilização claros por iniciativa | Rotatividade de equipes. Imediatismo. Propriedade fraca no longo prazo |
| Financiamento por produto/equipe | Propriedade durável. Qualidade sustentada | Mais difícil de realocar. Risco de financiar esforços zumbis |
| Priorização por fórmula | Transparente, comparável, defensável | Falsa precisão. Entradas manipuláveis. Pode afastar o julgamento |
| Programas plurianuais de escopo fixo | Estabilidade de financiamento. Investimento de longo horizonte | Trava as suposições iniciais. Caro corrigir o rumo |

A tensão central é entre coerência e velocidade. Controle central demais e a organização anda devagar e desmotiva as melhores pessoas. De menos e ela se fragmenta em cem ótimos locais. As organizações maduras centralizam apenas as poucas coisas que precisam ser coerentes (estratégia, plataformas compartilhadas, padrões transversais e o compromisso de financiamento) e empurram as decisões de execução o mais perto possível das equipes. A tensão entre estabilidade de financiamento e adaptabilidade se resolve do mesmo modo: não escolhendo uma, mas comprometendo dinheiro de forma incremental contra equipes duráveis, para que a estabilidade das pessoas conviva com a flexibilidade da direção.

## Perguntas para discutir com sua equipe

1. **Quais poucas coisas precisam permanecer coerentes em toda a organização, e quais decisões vocês devem empurrar para as equipes?** A tensão central num portfólio é coerência versus velocidade, e errar a fronteira é caro nos dois sentidos. Centralizem demais e as decisões se arrastam enquanto as melhores pessoas perdem autonomia; centralizem de menos e vocês se fragmentam em cem ótimos locais, com sistemas duplicados e risco oculto entre equipes. As organizações maduras guardam no centro só uma lista curta: estratégia, plataformas compartilhadas, padrões transversais e o compromisso de financiamento. Levem evidências à reunião: contem quantas equipes resolvem o mesmo problema de modo independente e quantas decisões recentes empacaram esperando a aprovação central. Se qualquer um dos números for alto, vocês traçaram a linha no lugar errado, então movam direitos de decisão específicos em vez de discutir a centralização em abstrato.

2. **Como vocês financiarão resultados em vez de produções sem perder a responsabilização que o financiamento por projeto dava?** Financiar equipes duráveis e alinhadas ao produto vence financiar projetos temporários, porque equipes estáveis sustentam a qualidade e são donas da operação, não apenas da construção. O porém: o financiamento por projeto dava aos líderes um escopo limpo e uma linha clara de responsabilização, e o financiamento persistente de equipes pode derivar para pagar esforços zumbis muito depois de a premissa deles ter falhado. Resolvam comprometendo dinheiro de forma incremental contra equipes duráveis, revisando cada tema numa cadência trimestral e realocando capacidade entre temas em vez de desfazer equipes. Levem a evidência que importa: para cada equipe financiada, que resultado (adoção, custo, confiabilidade, resultado da missão) se moveu no último trimestre e o que vocês deixariam de financiar se o dinheiro de repente ficasse escasso. Se vocês não conseguem nomear o resultado, ainda estão financiando produção.

3. **Quanta capacidade interna de engenharia vocês precisam manter para continuar sendo um comprador inteligente do trabalho de fornecedores e integradores de sistemas?** Quando vocês entregam a execução a contratados ou a um integrador de sistemas, mantêm a responsabilização, então precisam de profundidade interna suficiente para especificar o trabalho, julgar a qualidade e assumir se o fornecedor falhar. Percam essa capacidade e vocês obtêm contratação de tipo “bodyshop”: compram horas em vez de resultados e não conseguem mais dizer se estão sendo atendidos ou capturados. Pesem o custo de reter engenheiros seniores que não escrevem a maior parte do código contra o custo muito maior do aprisionamento ao fornecedor e de uma missão mantida como refém. Levem sinais concretos: a sua equipe consegue hoje ler o backlog do fornecedor, reproduzir um build e ser dona dos dados e das interfaces? Insistam em cláusulas de saída e de transição desde o primeiro dia, porque o momento de negociar alavancagem é antes de assinar e não quando a relação azeda.

4. **Quais iniciativas vocês deliberadamente recusam financiar neste ciclo, e toda equipe consegue rastrear esse não até a estratégia?** Priorizar é subtrair, e um portfólio que diz sim a tudo em silêncio não tem estratégia: apenas espalha a capacidade escassa de modo fino demais para terminar qualquer coisa bem. Para uma grande organização o dano é difuso, porque nenhuma aprovação isolada parece imprudente, mas a soma deixa à míngua as poucas apostas que de fato moveriam um objetivo. A atração contrária é real: toda iniciativa recusada tem um patrocinador que acredita ser essencial, e um framework (pontuação ponderada, custo do atraso, RICE) não decidirá por vocês, apenas força as suposições a aparecer onde os líderes podem discuti-las. Levem a lista classificada, o compromisso explícito registrado para cada adiamento e a contagem de iniciativas em andamento versus o número que vocês têm capacidade de terminar. Em contextos corporativos e governamentais, acrescentem o custo político de cada não e quem detém a autoridade de fazê-lo valer, porque uma decisão de priorização que qualquer patrocinador pode derrubar escalando não é uma decisão, é uma sugestão.

5. **Onde estão hoje as suas dependências entre equipes, e quais vocês estão eliminando por projeto em vez de apenas acompanhar?** Para uma grande organização, o custo de coordenação, não o esforço de programação, costuma ser a restrição que amarra, de modo que uma funcionalidade que uma equipe entregaria num sprint pode esperar três trimestres por uma equipe de plataforma que nunca ouviu falar dela. Acompanhar as dependências num registro as torna visíveis, mas visibilidade não é resolução; a jogada de maior alavancagem é eliminá-las por projeto, com plataformas de autoatendimento, APIs documentadas e contratos internos claros, para que as equipes parem de esperar umas pelas outras. O compromisso é que o investimento em plataforma custa capacidade real agora contra atrasos de dependência que se compõem em silêncio depois, e é sempre tentador financiar a funcionalidade visível em vez da plataforma invisível. Levem o mapa de dependências das suas principais iniciativas, a contagem de entregas que escorregaram no último trimestre esperando outra equipe e se cada dependência transversal tem um único dono responsável. Em programas corporativos e governamentais em que dezenas de equipes e integradores externos se entrelaçam, nomeiem a cadência de planejamento entre equipes que revela isso cedo, porque uma dependência descoberta na hora da integração já é uma falha de cronograma.

6. **A forma como vocês estruturaram o financiamento e os contratos combina com o ritmo em que vocês de fato aprendem?** Comprometer dinheiro em grandes blocos plurianuais trava as suas suposições mais iniciais e menos informadas, mas muitos regimes de financiamento, especialmente as dotações anuais do governo, empurram vocês a superdimensionar o compromisso inicial e a gastar antes do fim do ano. A consideração contrária é que a estabilidade de financiamento permite às equipes duráveis investir para o longo horizonte, então a resposta não são contratos minúsculos, e sim incrementos independentemente valiosos financiados em estágios atrelados a resultados demonstrados. Levem a forma dos seus compromissos atuais: quanto está comprometido antes de o primeiro software funcionando ser entregue, se as estimativas de custo separam construção, operação e sustentação e quão tarde vocês ainda conseguem parar ou redirecionar sem desperdiçar a dotação. Para leitores corporativos e governamentais, as equipes de contratação e jurídico moldam o que é possível muito mais do que os engenheiros esperam, então envolvam-nas cedo e perguntem explicitamente que contratação modular e autoridade de financiamento incremental as regras já permitem antes de presumir que precisam de um contrato monolítico.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e pouco fôlego, os fundadores são a camada de portfólio, então mantenham num quadro branco: dois ou três resultados publicados, o trabalho atrelado a eles e todo o resto cortado de imediato. Financiem em apostas curtas que vocês possam parar em semanas em vez de comprometer um trimestre à frente e pulem os frameworks, registros e eventos de planejamento que custariam mais coordenação do que economizariam. O seu único risco real de portfólio é o punhado de dependências externas que vocês não conseguem evitar, então nomeiem um dono para cada uma.

**Pequena empresa.** Sem PMO nem gerente de programas dedicado, a gestão de portfólio é uma conversa recorrente entre as pessoas que vocês já têm, não um papel a contratar. Apoiem-se em comprar em vez de construir para qualquer coisa fora do seu núcleo e julguem os fornecedores por quão facilmente vocês poderiam deixá-los, já que o aprisionamento machuca mais quando falta pessoal para migrar. Mantenham uma única lista honesta do que vocês estão financiando e do que deliberadamente não estão e revisitem-na numa cadência fixa e leve para que o orçamento escasso siga os poucos resultados que pagam as contas.

**Grande empresa.** Entre dezenas ou centenas de equipes o trabalho é coerência sem paralisia: centralizem apenas a estratégia, as plataformas compartilhadas, os padrões transversais e o compromisso de financiamento e empurrem a execução para as equipes. Financiem equipes duráveis e alinhadas ao produto de forma persistente, rodem uma revisão trimestral de portfólio que realoque capacidade entre temas e gerenciem as dependências por um registro compartilhado e planejamento entre equipes. A governança e a auditoria são inegociáveis nessa escala, então tornem o trabalho de fornecedores tão visível quanto o interno e registrem o compromisso por trás de toda decisão de priorização.

**Governo.** A lei de contratação, as dotações anuais e a prestação de contas públicas moldam cada movimento. Favoreçam a contratação modular em vez de uma adjudicação monolítica plurianual, financiem em estágios atrelados a resultados demonstrados e separem construção, operação e sustentação nas estimativas para que a sustentação nunca seja uma surpresa. Mantenham uma equipe interna de comprador inteligente, sejam donos dos seus dados e interfaces e escrevam cláusulas de saída e de transição em todo contrato, porque as obrigações de transparência significam que um programa fracassado vira um evento público e auditado e não uma baixa silenciosa.

## Exemplos

**Startup.** Uma startup de estágio semente com doze pessoas roda dois pequenos squads, e os fundadores atuam como toda a camada de portfólio. Toda segunda-feira atrelam o trabalho a apenas dois resultados publicados, ativação e margem bruta, e cortam abertamente tudo que não serve a nenhum, de modo que um pedido de integração brilhante é deixado de lado em favor de consertar a desistência na integração de novos usuários. Financiam em apostas curtas em vez de comprometer um trimestre adiantado e nomeiam um dono para a única dependência externa que não conseguem evitar, o provedor de pagamentos, para que ela nunca faça um lançamento escorregar em silêncio.

**Grande empresa.** Um banco global roda mais de cem equipes de entrega em varejo, pagamentos e risco. Realiza uma revisão trimestral de portfólio em que um pequeno grupo executivo aloca financiamento a uma dúzia de temas estratégicos, cada um liderado por uma dupla responsável: um líder de negócio, um líder de engenharia. As equipes são financiadas de forma persistente, não por projeto. A revisão trimestral realoca capacidade entre temas em vez de desfazer equipes. Um registro compartilhado de dependências e um evento trimestral de planejamento revelam cedo as necessidades entre equipes. O resultado: menos escorregões surpresa e a capacidade de redirecionar o investimento dentro de um trimestre quando as condições de mercado mudam.

**Governo.** Uma autoridade tributária nacional que moderniza um sistema de declaração de décadas recusa um único contrato monolítico plurianual em favor da contratação modular: uma sequência de incrementos menores e independentemente valiosos, cada um entregando software funcionando que os cidadãos podem usar. Pede financiamento em estágios atrelados a resultados demonstrados, o que reduz o risco de um grande programa fracassado. A autoridade mantém uma equipe técnica interna como comprador inteligente, é dona de todos os dados e interfaces e escreve cláusulas explícitas de saída em todo contrato de fornecedor, de modo que nenhum integrador possa manter a missão como refém.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da gestão de portfólio vem de três fontes: desperdício evitado, entrega de valor mais rápida e menos fracassos de grandes programas. O desperdício evitado são os sistemas duplicados que vocês nunca constroem e as iniciativas de baixo valor que nunca financiam porque uma visão de portfólio tornou visível a redundância. O valor mais rápido vem de eliminar por projeto as dependências para que as equipes parem de esperar umas pelas outras. O maior retorno, porém, é a redução de risco. Os grandes programas de software fracassam ou estouram muito os prazos em altas taxas, e um único fracasso plurianual evitado pode anular o custo inteiro da função de portfólio.

O custo de adoção é real: papéis de portfólio e de programas, cadências de planejamento, ferramentas e o tempo de coordenação que tudo isso consome. O custo de *não* adotar é maior mas difuso, e por isso é fácil de ignorar: gasto não coordenado, [custo afundado](https://en.wikipedia.org/wiki/Sunk_cost) em trabalho desalinhado e o arrasto composto dos atrasos de dependências em toda iniciativa. Ao defender o caso junto à liderança, enquadrem a gestão de portfólio como o mecanismo que transforma a estratégia dela em entrega e a protege de fracassos de grandes programas que encerram carreiras. Mostrem o [custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership) ao longo de construção, operação e sustentação plurianual, não apenas da construção inicial, porque os líderes que financiam só a construção são invariavelmente surpreendidos pela operação.

## Antipadrões e armadilhas

- **Priorização por HiPPO.** Decisões conduzidas pela opinião da pessoa mais bem paga em vez de por evidência ou de um framework combinado.
- **Roteiro como promessa de datas.** Publicar datas de futuro distante como compromissos e depois gerir pelo calendário e não pelo resultado.
- **Tudo é prioridade um.** Um portfólio sem nenhum não explícito, de modo que a capacidade escassa é espalhada fina demais para terminar qualquer coisa.
- **Cegueira de dependências.** Descobrir as dependências entre equipes na hora da integração em vez de na hora do planejamento.
- **Contratação de tipo bodyshop.** Comprar horas de contratados em vez de resultados e perder a capacidade interna de julgar a qualidade.
- **Gastar ou perder.** Correrias de orçamento no fim do ano que financiam trabalho de baixo valor para evitar devolver dotações.
- **OKRs como torre de controle.** Transformar os objetivos em tarefas atribuídas e em métricas de avaliação, destruindo o sinal honesto que existem para fornecer.
- **Programas zumbis.** Esforços plurianuais que continuam sendo financiados por inércia muito depois de a premissa ter falhado.

## Modelo de maturidade

**Nível 1: Iniciar.** As prioridades são definidas ad hoc e mudam com quem pedir mais alto. Não há visão de portfólio, então as dependências surgem como crises de integração e os sistemas duplicados passam despercebidos. Os fornecedores são geridos por volume contratual e não por resultados, e o financiamento segue correrias anuais de fim de ano.

**Nível 2: Desenvolver.** Existe um inventário de portfólio revisado periodicamente, mas a prática varia de equipe para equipe. Os objetivos são publicados mas fracamente ligados ao trabalho diário; algumas equipes mantêm um registro de dependências e gerenciam alguns fornecedores por resultados enquanto outras não fazem nenhum dos dois. O orçamento é previsível mas ainda baseado em projetos, de modo que a responsabilização é mais clara que a coerência estratégica.

**Nível 3: Padronizar.** A estratégia desce limpa até as equipes por uma estrutura rasa de OKRs, e um framework de priorização é documentado e aplicado em todo o portfólio. Os eventos de planejamento entre equipes revelam as dependências antes que mordam, as equipes são financiadas de forma persistente e não por projeto, e a contratação modular com financiamento incremental é a norma da organização e não um experimento local.

**Nível 4: Gerenciar.** O portfólio é medido contra linhas de base, não apenas documentado. Os líderes acompanham o movimento de resultados por tema financiado, o custo do atraso nas principais iniciativas, as taxas de escorregão de dependências, a entrega dos fornecedores contra resultados combinados e a fração do gasto comprometido atrelada a resultados demonstrados. Os compromissos de priorização e os critérios de interrupção são impostos com base nessa evidência, e a variância entre previsto e real em custo e cronograma conduz cada decisão de financiamento em lugar da advocacia.

**Nível 5: Orquestrar.** O planejamento de portfólio, de programas e de riscos é integrado, e o portfólio é continuamente reequilibrado conforme a evidência chega. As dependências são em grande parte eliminadas por projeto por meio de plataformas e contratos internos claros, o trabalho de fornecedores e o interno compartilham uma visão única de valor e de risco, e a cadência de financiamento combina com a de aprendizado, de modo que a organização rotineiramente para, redireciona ou redefine o escopo do trabalho sem drama.

## Ideias para discussão

- Quão rasa pode ser uma cascata de OKRs antes de deixar de orientar o trabalho, e quão funda antes de virar ficção?
- Quando uma fórmula de priorização melhora as decisões, e quando apenas lava a resposta predeterminada de alguém?
- As equipes de plataforma devem ser financiadas por um orçamento central ou cobradas das equipes consumidoras, e como isso muda seus incentivos?
- Num contexto governamental, até onde vocês podem empurrar o financiamento incremental e modular dentro da lei de dotações existente antes de precisar de mudança legislativa?
- Como vocês mantêm o trabalho de fornecedores tão visível quanto o interno sem se afogar em sobrecarga de relatórios?
- Qual é a resposta certa quando o produto de uma equipe durável perde relevância estratégica: realocar as pessoas, ou desfazer e reconstruir?

## Principais conclusões

- A gestão de portfólio converte a estratégia em software entregue decidindo o que financiar, em que ordem, entre muitas equipes.
- Priorizem por subtração e registrem os compromissos. Um portfólio que diz sim a tudo não tem estratégia.
- Para grandes organizações, as dependências entre equipes, não o esforço de programação, costumam ser a restrição que amarra. Tornem-nas visíveis e eliminem-nas por projeto.
- Financiem equipes duráveis e alinhadas ao produto e comprometam dinheiro de forma incremental para que a estabilidade das pessoas conviva com a flexibilidade da direção.
- Governem os fornecedores como parte do portfólio, retenham internamente a função de comprador inteligente e protejam-se do aprisionamento com propriedade de dados e cláusulas de saída.
- No governo, estruturem os programas em incrementos independentemente valiosos para se ajustar aos ciclos plurianuais de financiamento e reduzir o risco de fracasso de grandes programas.

## Referências e leitura complementar

- Donald G. Reinertsen, *The Principles of Product Development Flow*
- Marty Cagan, *Inspired* and *Empowered*
- John Doerr, *Measure What Matters*
- Christina Wodtke, *Radical Focus: Achieving Your Most Important Goals with OKRs*
- Mik Kersten, *Project to Product*
- Jez Humble, Joanne Molesky, and Barry O'Reilly, *Lean Enterprise*
- Project Management Institute, *The Standard for Portfolio Management*
- Axelos, *Managing Successful Programmes (MSP)*
- U.S. Digital Service, *Digital Services Playbook*
- UK Government Digital Service, *Service Manual* and *Technology Code of Practice*
- U.S. Government Accountability Office, *Agile Assessment Guide*
