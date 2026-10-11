# 5.1 Fundamentos de UX

## Visão geral e motivação

A [experiência do usuário](https://en.wikipedia.org/wiki/User_experience) (UX) trata de entender as pessoas (seus objetivos, seus contextos, suas restrições) e depois moldar o software para que as ajude a ter sucesso com o mínimo de atrito. Não é decoração que se aplica no fim. É um jeito de trabalhar que começa antes da primeira linha de código e continua bem depois do lançamento. Este capítulo cobre as práticas de pesquisa, modelagem e [design thinking](https://en.wikipedia.org/wiki/Design_thinking) que permitem a uma grande organização tomar decisões de produto a partir de evidências e não de palpites.

Para grandes equipes, a UX é tanto um problema de coordenação quanto um ofício. Quando dezenas de esquadrões entregam num único produto compartilhado, modelos mentais descasados, fluxos duplicados e terminologia contraditória se acumulam num todo confuso de que nenhuma equipe é dona. Uma fundação de UX compartilhada, construída com personas comuns, mapas de jornada acordados e uma [arquitetura da informação](https://en.wikipedia.org/wiki/Information_architecture) documentada, dá a toda equipe o mesmo mapa do usuário, de modo que suas decisões separadas somem uma experiência coerente. Sem ela, cada equipe otimiza localmente e o produto como um todo não faz sentido.

Empresas e governo elevam as apostas. O software corporativo muitas vezes tem usuários cativos que não podem ir embora, então a má UX é paga em treinamento, chamados de suporte, erros e produtividade perdida e não em pessoas indo embora. Os serviços governamentais muitas vezes alcançam o público inteiro, inclusive pessoas em crise, em dispositivos antigos, com pouca confiança digital ou sem nenhum provedor alternativo. Aqui a qualidade da UX é uma questão de equidade e de confiança cívica: um pedido de benefício mal projetado pode negar comida ou moradia a alguém, não porque a pessoa seja inelegível, mas porque não conseguiu terminar o formulário.

## Princípios fundamentais

- Projetem para pessoas reais fazendo tarefas reais em condições reais, não para um usuário idealizado com conexão rápida e atenção total.
- A pesquisa reduz o risco. O momento mais barato para descobrir uma suposição errada é antes de ter construído em cima dela.
- Os usuários não conseguem dizer com confiabilidade o que farão. Observem o comportamento, não apenas a preferência declarada.
- Concentrem-se no trabalho que o usuário tenta fazer, não na funcionalidade que vocês querem entregar.
- A consistência é uma funcionalidade: um modelo mental coerente no produto reduz a carga cognitiva.
- A [acessibilidade](https://en.wikipedia.org/wiki/Accessibility) e a inclusão fazem parte da boa UX desde o início, não de uma passada posterior de conformidade.
- Métodos qualitativos e quantitativos respondem a perguntas diferentes. Usem os dois.
- Pesquisa pequena e frequente vence estudos raros e pesados.

## Recomendações

### Estabeleça uma pesquisa contínua e de métodos mistos

Mirem uma prática de pesquisa leve mas contínua em vez de grandes estudos ocasionais. As entrevistas revelam motivações e modelos mentais. Os [testes de usabilidade](https://en.wikipedia.org/wiki/Usability_testing) revelam onde os designs falham. De cinco a oito participantes por rodada trazem à tona a maioria dos problemas graves. As pesquisas de opinião medem atitudes em escala mas não conseguem explicar o “porquê”. A análise de dados e a instrumentação mostram o que as pessoas de fato fazem em toda a população. Combinem um método qualitativo (por quê) com um quantitativo (quantos), para que os achados sejam ao mesmo tempo explicados e dimensionados. E mantenham um repositório de pesquisa, para que os discernimentos continuem pesquisáveis e reutilizáveis entre as equipes em vez de se perderem nos slides de um esquadrão.

### Modele os usuários com personas, mapas de jornada e jobs-to-be-done

Construam um pequeno conjunto de personas baseadas em evidências que capturem objetivos, contextos e restrições, e não caricaturas demográficas. Enquadrem as necessidades como jobs-to-be-done (trabalhos a serem feitos), o resultado subjacente que o usuário tenta alcançar e não uma funcionalidade (“quando eu perder o emprego, quero entender depressa a que apoio tenho direito, para continuar pagando o aluguel”). Isso mantém o foco nos resultados e não nas funcionalidades. Os mapas de jornada traçam a experiência inteira entre canais e ao longo do tempo, expondo lacunas e passagens de bastão que nenhuma tela isolada revela. Para serviços com muita operação de bastidores (centrais de atendimento, assistentes sociais, atendimento de pedidos), usem [blueprints de serviço](https://en.wikipedia.org/wiki/Service_blueprint) para ligar a experiência de palco aos sistemas e à equipe por trás.

### Projete a arquitetura da informação deliberadamente

A arquitetura da informação (AI) é como o conteúdo, as funcionalidades e a navegação são estruturados e rotulados. Usem a [classificação de cartões](https://en.wikipedia.org/wiki/Card_sorting) (card sorting) e o teste de árvore para derivar essa estrutura dos modelos mentais dos usuários e não do seu organograma. Uma falha comum em grandes organizações é expor as fronteiras departamentais internas como navegação de nível superior. Estabeleçam um vocabulário controlado para que o mesmo conceito tenha o mesmo nome em toda parte. O [design de interação](https://en.wikipedia.org/wiki/Interaction_design) então define o comportamento momento a momento: estados, feedback, recuperação de erros e o fluxo entre os passos.

### Aplique o design thinking de forma pragmática

O modelo do duplo diamante (divergir e depois convergir para definir o problema certo, depois divergir e convergir para projetar a solução certa) é um enquadramento útil. Tratem-no, porém, como uma mentalidade e não como um processo rígido com portões. Na prática, conduzam ciclos curtos: formulem uma hipótese, esbocem, testem com um punhado de usuários e aprendam em dias. Guardem a descoberta mais pesada para problemas genuinamente inéditos ou de alto risco. E cuidado com o “teatro da inovação”, em que as oficinas produzem notas adesivas mas nenhuma mudança entregue.

### Integre a UX à entrega

Embutam designers e pesquisadores nas equipes de entrega em vez de manter um “departamento de UX” separado que passa especificações por cima do muro. Façam dos achados de pesquisa uma entrada permanente da priorização. Ponham portões de qualidade de UX, como parâmetros de usabilidade e verificações de acessibilidade, na definição de pronto. E acompanhem métricas de resultado (sucesso na tarefa, tempo na tarefa, taxa de erro, satisfação) ao lado das métricas de entrega.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Pesquisa de descoberta contínua | Pega problemas cedo, constrói entendimento compartilhado | Custo contínuo, exige pipeline de recrutamento e pessoal habilidoso |
| Pesquisa pesada e antecipada | Discernimento profundo antes de um grande investimento | Lenta, pode atrasar um aprendizado que só a entrega revela |
| Decisões só por dados de análise | Escala, objetiva, barata depois de instrumentada | Explica o quê mas não o porquê. Cega para não usuários e casos de borda |
| Personas e mapas de jornada | Alinham muitas equipes num modelo do usuário | Envelhecem, podem virar ficção se não forem renovados com dados |
| Designers embutidos | Feedback rápido, responsabilidade compartilhada | Mais difícil manter o ofício consistente entre muitas equipes |

Toda organização equilibra o investimento em pesquisa contra a velocidade de entrega. O erro é tratar isso como um ou outro. A postura produtiva é proporcional: gastar mais descoberta em decisões caras de reverter (AI central, fluxos principais, escolhas de plataforma) e menos em detalhes que vocês podem mudar facilmente depois. O custo da pesquisa é quase sempre pequeno ao lado do custo de construir bem a coisa errada.

## Perguntas para discutir com sua equipe

1. **Quem é dono da arquitetura da informação compartilhada e do vocabulário controlado, e o que acontece quando uma equipe quer se desviar?** Em escala, a falha mais comum é deixar cada esquadrão expor a estrutura do seu próprio organograma e seus próprios nomes para o mesmo conceito, de modo que o produto acaba com três palavras para uma coisa e uma navegação que espelha departamentos em vez de tarefas do usuário. Decidam agora se a AI e o vocabulário têm dono central, derivados de classificação de cartões e teste de árvore e não de política interna, e como uma equipe pede uma mudança. Isso importa mais em empresas e governo porque usuários cativos não podem ir embora, então a incoerência é paga em treinamento, chamados de suporte e erros e não em evasão. Levem como evidência a lista atual de termos duplicados e fluxos conflitantes. Se vocês não conseguem nomear um dono, esse é o primeiro item de ação.

2. **Qual é o nosso pipeline de recrutamento de participantes de pesquisa, e ele alcança usuários com assistência digital, pouco confiantes e não digitais?** A descoberta contínua só funciona se vocês conseguem pôr-se diante de usuários reais toda semana, e as pessoas mais difíceis de recrutar costumam ser as que mais precisam do serviço: pessoas em crise, em dispositivos antigos ou que normalmente dependem de ajuda. Testar só voluntários confiantes e conectados dá uma leitura lisonjeira mas falsa, especialmente para serviços públicos em que a equidade de acesso é o ponto inteiro. Combinem quem conduz o recrutamento, que incentivos oferecem e como observam sessões de assistência digital sem acrescentar ao fardo de uma pessoa vulnerável. Levem os dados demográficos dos participantes dos últimos três estudos e conferiram-nos com a sua base real de usuários. Se pendem para usuários fáceis de alcançar, consertem o pipeline antes de confiar nos achados.

3. **Quais portões de qualidade de UX pertencem à nossa definição de pronto, e como evitamos que virem teatro?** Embutir designers e pesquisadores só compensa se a pesquisa é uma entrada permanente da priorização e se as verificações de usabilidade e de acessibilidade de fato impedem uma história de ser entregue, e não um conjunto de slides com que todos concordam e depois ignoram. Escolham métricas concretas de resultado que acompanharão ao lado das de entrega: sucesso na tarefa, tempo na tarefa, taxa de erro e satisfação. O risco é pesquisa conduzida para justificar decisões já tomadas, então combinem quem pode vetar um lançamento por um portão de UX e que evidência se sobrepõe à opinião de um executivo. Levem uma funcionalidade recente e perguntem se a pesquisa dela mudou a decisão ou apenas a decorou. Se os achados nunca movem um roteiro, os seus portões são cosméticos.

4. **Como evitamos que as nossas personas, mapas de jornada e AI decaiam em ficção quando a pesquisa que os produziu tem um ano?** Os modelos compartilhados são o que permite a dezenas de equipes projetar rumo a uma única experiência coerente, mas só funcionam enquanto ainda descrevem usuários reais, e no momento em que uma persona vira um artefato que as pessoas citam para ganhar discussões e não um resumo de evidências, ela faz dano ativo. Decidam quem é dono de renovar cada modelo, em que cadência e contra que dados (entrevistas novas, análise de dados, temas de suporte) e combinem uma data visível de “última validação” para que modelos obsoletos sejam óbvios. A consideração concorrente é o custo: renovar tudo continuamente é um desperdício, então liguem a frequência de renovação à rapidez com que aquela parte da base de usuários ou da jornada de fato muda. Levem a proveniência das suas principais personas atuais e perguntem quando cada uma foi conferida pela última vez com um usuário real. Em empresas e governo, onde uma base de usuários cativa ou pública muda devagar mas com consequências (uma população envelhecendo, um novo benefício, uma transição de dispositivos), um modelo que deriva em silêncio pode conduzir anos de investimento para usuários que já não existem.

5. **Onde a acessibilidade mora no nosso processo, e conseguimos provar que um lançamento a atende antes de ser entregue e não depois de uma reclamação?** Tratar a acessibilidade como uma passada tardia de conformidade é ao mesmo tempo a falha mais comum e a mais cara, porque adaptar semântica, ordem de foco e contraste a uma interface pronta custa muito mais que projetá-los desde o início. Decidam a que padrão vocês se submetem (por exemplo a WCAG, as Web Content Accessibility Guidelines), se a conformidade é um portão bloqueante na definição de pronto e quem responde quando uma funcionalidade inacessível chega à produção. A tensão é velocidade versus inclusão, e as equipes sob pressão de prazo deixarão cair em silêncio as verificações que não são impostas. Levem a última auditoria, a cobertura automatizada e manual por trás dela e o número de problemas de acessibilidade achados depois do lançamento e não antes. Para o governo especialmente isso não é gentileza opcional: costuma ser um dever legal e uma questão de equidade, já que um serviço público que exclui usuários com deficiência ou com assistência digital falhou em seu propósito central, não num secundário.

6. **Quando a nossa análise de dados e a nossa pesquisa qualitativa discordam, como decidimos em qual acreditar, e quem arbitra?** As grandes organizações acumulam tanto painéis que mostram o que milhares de usuários fazem quanto entrevistas que explicam por que um punhado se comporta como se comporta, e os dois rotineiramente apontarão em sentidos opostos: um fluxo com alta conclusão que humilha as pessoas em silêncio, ou uma funcionalidade que os usuários elogiam nas sessões mas nunca tocam em escala. Combinem de antemão como triangulam, a que pergunta cada método merece confiança para responder (análise de dados para magnitude e alcance, pesquisa para causa e significado) e quem tem autoridade para decidir quando conflitam. O risco é escolher a dedo a fonte que lisonjeia o plano já escolhido. Levem um desacordo recente concreto e percorram como ele foi de fato resolvido. Em contextos corporativos e públicos as apostas são afiadas porque a análise de dados sistematicamente subconta as pessoas que mais importam: os não usuários, os que abandonam e os que usam tecnologia assistiva raramente aparecem no funil, então confiar só nos números pode tornar invisíveis os excluídos.

## Perspectiva por setor

**Startup.** Vocês não têm pesquisador nem tempo para um repositório, então façam da pesquisa um hábito dos fundadores: sentem-se ao lado de cinco usuários reais por uma tarde antes de construir a próxima coisa. Pulem as personas e mapas de jornada formais. Um entendimento compartilhado do único trabalho que vocês resolvem, renovado observando as pessoas toda semana, vence uma documentação que ninguém mantém. A vantagem de vocês é que a equipe inteira consegue absorver um discernimento no mesmo dia em que ele aparece, então protejam essa velocidade e resistam ao cerimonial.

**Pequena empresa.** Sem especialista em UX e com orçamento apertado, apoiem-se nas convenções que seus usuários já conhecem em vez de inventar as suas e comprem ferramentas com padrões sensatos em vez de projetar fluxos do zero. Façam vocês mesmos a pesquisa barata e de alto valor: um punhado de sessões de usabilidade por videochamada e uma leitura dos seus chamados de suporte trarão à tona a maior parte dos problemas graves. Tratem o básico de acessibilidade (contraste, rótulos, acesso por teclado) como o mínimo que se obtém de uma boa biblioteca de componentes e não um projeto para pôr gente.

**Grande empresa.** O problema central é a coerência entre muitas equipes, então invistam nas fundações compartilhadas: personas com dono, mapas de jornada mantidos, um vocabulário controlado e uma arquitetura da informação documentada rumo à qual os esquadrões projetam e não em torno da qual. Embutam designers e pesquisadores nas equipes de entrega, mas governem o ofício de forma central para que o produto não se fratura em dialetos inconsistentes. Financiem um repositório de pesquisa e portões de qualidade na definição de pronto e acompanhem as métricas de resultado de UX como portfólio, para que a otimização local de nenhuma equipe degrade o todo.

**Governo.** A acessibilidade e a equidade de acesso são deveres, não preferências, então sujeitem os lançamentos a um padrão publicado e pesquisem com toda a gama do público, inclusive usuários com assistência digital, pouco confiantes e não digitais. A contratação e a transparência moldam a entrega: publiquem seus princípios de design e métodos de pesquisa, estruturem os serviços em torno dos eventos de vida dos cidadãos e não de departamentos internos e guardem evidência dos testes para auditoria. Como os usuários muitas vezes não têm provedor alternativo, um fluxo que eles não conseguem terminar nega um serviço, então tratem a conclusão pelo usuário mais difícil de alcançar como a medida real de sucesso.

## Exemplos

**Startup.** Uma startup de quatro pessoas que constrói uma ferramenta de agendamento para pequenas clínicas tinha opiniões fortes sobre o que as recepcionistas precisavam, mas nenhuma evidência. Antes de escrever mais funcionalidades, os fundadores se sentaram ao lado de cinco recepcionistas por uma tarde cada uma e as observaram trabalhar. Aprenderam que a dor real não era a velocidade de agendar, mas as marcações duplicadas causadas por uma visão confusa do calendário, algo que ninguém tinha pensado em mencionar em chamadas de vendas anteriores. Reenquadrar o produto em torno desse único trabalho, e esboçar e testar correções com as mesmas cinco pessoas ao longo de uma semana, transformou um período de teste que empacava nos seus primeiros clientes pagantes.

**Grande empresa.** Um banco multinacional consolidou sete ferramentas regionais internas de originação de empréstimos numa única plataforma. Em vez de fundir conjuntos de funcionalidades, a equipe conduziu mapeamento de jornada e blueprints de serviço com analistas de crédito de várias regiões. Descobriram que as “diferenças regionais” que todos presumiam eram em sua maioria terminologia inconsistente e ordem de telas e não diferenças genuínas de processo. Uma AI unificada e um vocabulário compartilhado cortaram bastante o tempo de treinamento dos analistas e reduziram os erros de processamento, porque a equipe agora compartilhava um modelo mental.

**Governo.** Uma autoridade tributária nacional que redesenhava seu serviço de declaração online conduziu testes moderados de usabilidade com contribuintes de várias idades, dispositivos e níveis de confiança digital, mais observação de assistência digital de pessoas que normalmente dependem de ajuda. Os testes revelaram que títulos de seção carregados de jargão faziam as pessoas abandonar ou preencher errado. Reenquadrar o conteúdo em torno dos jobs-to-be-done dos contribuintes, e reestruturar a AI em torno de eventos de vida e não de códigos tributários internos, aumentou a conclusão bem-sucedida por autoatendimento e reduziu o volume da central de atendimento, baixando diretamente o custo de servir e melhorando a equidade de acesso.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da UX vem de três alavancas: mais sucesso (mais usuários completam tarefas valiosas), menor custo de servir (menos contatos de suporte, menos treinamento, menos erros) e menos retrabalho (pegar direções erradas antes de serem construídas). Em contextos corporativos em que os usuários são cativos, o ganho aparece como produtividade e menos erros e não como conversão. Alguns segundos poupados por transação, entre milhares de funcionários, se compõem em grandes economias anuais.

O custo total de propriedade precisa pesar o custo de adotar contra o custo de não adotar. Os custos de adoção são fáceis de ver: pesquisadores e designers, recrutamento e incentivos para participantes, ferramentas e tempo no cronograma. O custo de não adotar é maior mas mais difícil de notar: transações abandonadas, ônus de suporte e de treinamento, caros redesenhos tardios, lançamentos fracassados e exposição de reputação ou jurídica quando serviços públicos excluem pessoas. Como esses custos se espalham por orçamentos de suporte, treinamento e operações e não pela linha de produto, a liderança costuma subestimá-los.

Para defender o caso junto à liderança, liguem a UX às métricas que os executivos já acompanham: taxas de conclusão e de conversão, custo por transação, volume de chamados de suporte, dias de treinamento e taxas de erro e de retrabalho. Conduzam um piloto pequeno e instrumentado que mostre um antes e depois mensurável e depois extrapolem para o portfólio. Enquadrar a pesquisa como redução de risco em decisões irreversíveis tende a ressoar com as partes interessadas de finanças e de governança.

## Antipadrões e armadilhas

- **Design guiado pelo HiPPO**: decisões tomadas pela opinião da pessoa mais bem paga em vez de por evidências.
- **Teatro de pesquisa**: estudos conduzidos para justificar decisões já tomadas, com os achados ignorados.
- **Personas como ficção**: perfis inventados, nunca validados com usuários reais, usados para ganhar discussões.
- **Organograma como AI**: navegação que espelha departamentos internos em vez de tarefas do usuário.
- **Pesquisa em big bang**: estudos raros e caros que chegam tarde demais para mudar qualquer coisa.
- **Testar só o caminho feliz**: ignorar estados de erro, casos de borda e usuários sob estresse.
- **Design como demão final de tinta**: trazer a UX só para fazer um build pronto “ficar bonito”.
- **Ignorar usuários com assistência e não digitais**: projetar só para usuários confiantes e conectados.

## Modelo de maturidade

**Nível 1: Iniciar.** Nenhuma prática dedicada de UX. As decisões são tomadas por opinião e pelo instinto da pessoa mais bem paga. A pesquisa, se acontece, é ad hoc e reativa, disparada por um lançamento que correu mal. Os fluxos e a terminologia são inconsistentes entre as equipes, e ninguém é dono da experiência geral.

**Nível 2: Desenvolver.** Algumas equipes têm designers e conduzem testes ocasionais de usabilidade, e existem algumas personas ou mapas de jornada, mas a prática varia muito entre esquadrões e não é mantida. A UX é tratada como fase e não como disciplina contínua, e é muitas vezes contornada sob pressão de cronograma. O bom trabalho acontece em bolsões mas não se soma no produto.

**Nível 3: Padronizar.** A pesquisa contínua de métodos mistos alimenta a priorização, e personas compartilhadas, mapas de jornada e uma AI de vocabulário controlado são documentados e usados entre as equipes. Os portões de qualidade de UX, incluindo parâmetros de usabilidade e verificações de acessibilidade, ficam na definição de pronto e são impostos em toda a organização. Um repositório pesquisável de pesquisa mantém os discernimentos reutilizáveis em vez de presos nos slides de um esquadrão.

**Nível 4: Gerenciar.** A prática é medida em relação a linhas de base e não apenas realizada. Vocês acompanham sucesso na tarefa, tempo na tarefa, taxa de erro, satisfação e conformidade de acessibilidade como métricas acordadas, definem metas e as observam ao longo dos lançamentos. As amostras de participantes da pesquisa são conferidas com a base real de usuários para que os achados sejam representativos, os portões de qualidade reportam taxas de aprovação e não opiniões e o custo da pesquisa é pesado contra reduções medidas em contatos de suporte, treinamento e retrabalho. As decisões de entregar ou segurar repousam em evidências contra essas linhas de base.

**Nível 5: Orquestrar.** A pesquisa é contínua, ligada a resultados e integrada ao planejamento de produto, de negócio e de risco em toda a organização. As equipes conduzem experimentos controlados, fecham o ciclo do discernimento à mudança entregue ao efeito medido e aposentam ou redimensionam modelos de usuários à medida que a população e suas jornadas mudam. A fundação de UX se adapta continuamente: personas, jornadas, AI e padrões são renovados com base em evidências, e a organização reequilibra onde investe a descoberta à medida que a reversibilidade e o risco mudam.

## Ideias para discussão

- Quanta descoberta é “o bastante” antes de se comprometer com uma direção, e quem decide?
- Como vocês mantêm personas e mapas de jornada vivos em vez de deixá-los virar artefatos obsoletos?
- Quando a análise quantitativa e a pesquisa qualitativa discordam, em qual vocês confiam e por quê?
- Como uma grande organização deve equilibrar um padrão central de UX com a autonomia de cada equipe?
- Qual é a forma certa de pesquisar serviços usados por pessoas em crise sem acrescentar ao fardo delas?
- Como vocês medem o ROI de uma pesquisa que previne um erro que, por isso, vocês nunca cometeram?

## Principais conclusões

- A UX é um jeito de trabalhar desde o início, não decoração no fim.
- Combinem métodos qualitativos (por quê) com quantitativos (quantos).
- Modelem os usuários com personas baseadas em evidências, mapas de jornada, jobs-to-be-done e blueprints de serviço.
- Estruturem a informação em torno dos modelos mentais dos usuários, não do organograma.
- Tratem o design thinking como uma mentalidade pragmática com ciclos curtos de aprendizado, não um processo rígido.
- O custo da pesquisa é pequeno comparado ao custo de construir a coisa errada.
- Em empresas e governo, a qualidade da UX se traduz diretamente em produtividade, custo de servir e equidade de acesso.

## Referências e leitura complementar

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, and Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* and *Design Principles*
- U.S. General Services Administration, *18F Methods* and the *U.S. Web Design System* research guidance
- Nielsen Norman Group, research method articles and reports
