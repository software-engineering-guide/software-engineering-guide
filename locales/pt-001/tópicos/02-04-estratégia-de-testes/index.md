# 2.4 Estratégia de testes

## Visão geral e motivação

Uma estratégia de [testes](https://en.wikipedia.org/wiki/Software_testing) é o conjunto deliberado de escolhas sobre o que testar, em que nível, com que grau de automação e com que confiança, para que a sua equipe possa mudar código rapidamente sem quebrá-lo. Os testes são o que permite a uma grande organização implantar com frequência e com segurança. Eles codificam o comportamento esperado, pegam regressões e dão aos engenheiros a confiança para [refatorar](https://en.wikipedia.org/wiki/Code_refactoring). Sem uma estratégia coerente, os testes tendem a seguir um de dois maus caminhos: ausentes (desenvolvimento movido pelo medo e lento) ou inchados (milhares de testes lentos e instáveis em que ninguém confia).

Para uma equipe grande, a estratégia importa mais que qualquer teste isolado. Centenas de engenheiros trabalhando numa base de código compartilhada precisam de uma rede de segurança rápida e confiável. Sem ela, toda mudança é arriscada e todo lançamento vira um calvário manual. Os testes também funcionam como documentação executável do comportamento pretendido, o que não tem preço depois que os autores originais seguiram adiante. A estratégia decide se a sua suíte de testes é um ativo que acelera a entrega ou um passivo que a arrasta.

Em contextos corporativos e governamentais, os testes carregam peso extra. As regulamentações podem exigir cobertura de testes e evidências documentadas. Sistemas críticos para a segurança e voltados ao cidadão exigem alta garantia. Testes de acessibilidade e de segurança podem ser exigidos por lei. Por isso a estratégia precisa equilibrar velocidade, confiança, custo e conformidade, e tratar a cobertura como um sinal, não como uma meta a ser manipulada.

## Princípios fundamentais

- Teste para ganhar a confiança de mudar, não para atingir um número.
- Favoreça testes rápidos, confiáveis e isolados. Testes lentos ou instáveis corroem a confiança que torna a suíte útil.
- Empurre os testes para o nível mais baixo que dá confiança real e reserve os testes lentos e amplos para o risco genuíno de integração.
- Um teste instável é um teste quebrado. Trate a instabilidade como um defeito de primeira classe.
- A cobertura é um sinal, não um objetivo. Alta cobertura de código trivial prova pouco.
- Teste comportamento e contratos, não detalhes de implementação, para que seus testes sobrevivam à refatoração.
- Faça dos testes não funcionais (acessibilidade, desempenho, segurança) parte da estratégia, não uma reflexão tardia.

## Recomendações

### Use a pirâmide de testes como padrão e conheça suas críticas

Adote por padrão muitos [testes unitários](https://en.wikipedia.org/wiki/Unit_testing) rápidos, menos [testes de integração](https://en.wikipedia.org/wiki/Integration_testing) e um pequeno número de testes de ponta a ponta, porque o custo e a fragilidade crescem com o escopo. Conheça também as críticas: o formato deve seguir a sua arquitetura, não o dogma. Um sistema com muitos serviços pode precisar de uma camada de integração maior (o “troféu de testes”), e o objetivo real é confiança por unidade de custo e de velocidade, não uma silhueta específica. Faça o que fizer, evite a pirâmide invertida de testes de ponta a ponta majoritariamente lentos.

### Adote TDD, BDD e desenvolvimento guiado por especificação onde ajudarem

Use o [desenvolvimento guiado por testes](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) para conduzir o design e garantir a testabilidade, especialmente para lógica complexa. É uma disciplina de design tanto quanto de teste. Use o [desenvolvimento guiado por comportamento](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) para expressar os testes na linguagem do domínio que você compartilha com as partes interessadas, o que é valioso para critérios de aceitação em ambientes regulamentados ou carregados de requisitos. O desenvolvimento guiado por especificação vai um passo além: trata uma especificação executável (o comportamento acordado, expresso como exemplos) como a única fonte da verdade, que tanto orienta a implementação quanto a verifica. Isso brilha onde os requisitos precisam ser rastreáveis até a evidência de aceitação, como em programas governamentais e regulamentados. Relacionado aos três está o **[teste deslocado à esquerda (shift-left)](https://en.wikipedia.org/wiki/Shift-left_testing)**: mover a verificação o mais cedo possível no ciclo de vida, escrevendo testes junto com o código ou antes dele e rodando-os continuamente, para pegar os defeitos quando são mais baratos de corrigir, e não em fases tardias de teste ou em produção. Nenhum deles é obrigatório em toda parte. Aplique-os onde acrescentam clareza.

### Empregue técnicas avançadas para o código de alto valor

Use o teste baseado em propriedades para verificar invariantes em muitas entradas geradas, pegando casos de borda que testes baseados em exemplos deixam passar. Use o [teste de fuzzing](https://en.wikipedia.org/wiki/Fuzzing) em analisadores sintáticos e fronteiras de entrada não confiável para encontrar travamentos e falhas de segurança. Use o [teste de mutação](https://en.wikipedia.org/wiki/Mutation_testing) para medir se os seus testes realmente detectam falhas injetadas, um sinal de qualidade muito melhor que a cobertura bruta. Use o teste de snapshot com critério para saídas serializadas e cuidado com a armadilha de reaprovar snapshots às cegas.

### Gerencie os dados de teste e use dados sintéticos

Torne os testes determinísticos com dados de teste controlados e isolados e evite fixtures mutáveis compartilhadas que acoplam os testes entre si. Gere [dados sintéticos](https://en.wikipedia.org/wiki/Synthetic_data) que espelhem as características da produção sem expor informações pessoais reais, o que é essencial onde as regras de privacidade proíbem usar dados de produção em ambientes de teste. Forneça fábricas ou construtores para que cada teste possa montar exatamente os dados de que precisa.

### Trate os testes instáveis como defeitos

Detecte a instabilidade automaticamente, tire os testes instáveis do caminho bloqueante e corrija-os ou apague-os dentro de um prazo. Uma suíte que falha ao acaso treina os engenheiros a ignorar falhas, o que destrói todo o seu valor. Acompanhe as taxas de instabilidade e faça da confiabilidade uma métrica de qualidade explícita da própria suíte de testes.

### Use a cobertura como sinal e acrescente testes não funcionais

Meça a cobertura para encontrar áreas sem teste, mas não a transforme numa meta rígida que convida à manipulação com testes sem asserções. Complemente-a com o teste de mutação para profundidade. Incorpore ao pipeline os testes de acessibilidade (verificações automatizadas mais auditorias manuais), de desempenho (linhas de base de carga e de latência com detecção de regressão) e de segurança (varredura de dependências, [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis) e teste dinâmico).

## Compromissos: prós e contras

| Tipo de teste / prática | Prós | Contras |
|---|---|---|
| Testes unitários | Rápidos, precisos, baratos, estáveis | Deixam passar bugs de integração e de nível de sistema |
| Testes de integração | Pegam defeitos de interface e de ligação | Mais lentos. Mais preparação. Mais frágeis |
| Testes de ponta a ponta | Maior confiança no comportamento real | Lentos, instáveis, caros de manter |
| TDD | Melhor design, testabilidade garantida | Curva de aprendizado. Parece lento no início |
| Teste baseado em propriedades | Encontra casos de borda, codifica invariantes | Exige pensar em propriedades. Mais difícil de escrever |
| Teste de mutação | Medida real da eficácia dos testes | Computacionalmente caro. Lento de rodar |
| Meta alta de cobertura | Revela código sem teste | Manipulável. Pode incentivar testes de baixo valor |

O compromisso central é confiança versus velocidade e custo. Testes mais amplos dão mais confiança, mas rodam mais devagar e quebram com mais frequência. Testes mais estreitos são rápidos e estáveis, mas deixam passar defeitos de nível de sistema. A mistura certa maximiza a confiança por segundo de feedback e por hora de manutenção. E o excesso de testes é um modo de falha real: uma suíte inchada de testes redundantes, lentos e frágeis pode custar mais que os bugs que evita.

## Perguntas para discutir com sua equipe

1. **Quais testes não funcionais, de acessibilidade, desempenho e segurança, devem bloquear um lançamento, e quais devem apenas relatar?** Este capítulo argumenta que o teste não funcional pertence à estratégia e não a uma reflexão tardia, e observa que a acessibilidade pode ser exigida por lei e que o teste de segurança pode fazer parte da evidência de autorização para operar. Para um sistema grande ou voltado ao cidadão, um portão bloqueante atrasa a entrega, mas um defeito de acessibilidade ou de segurança descoberto em produção carrega custos de correção, de reputação e jurídicos que fazem sombra ao teste. Leve os sinais que decidem: a sua exposição regulatória, se o sistema é voltado ao cidadão e com que frequência esses defeitos hoje escapam para a produção. Torne bloqueantes as verificações exigidas por lei e deixe as de menor risco relatarem com uma tendência, para que o portão reflita o risco real e não o dogma. A resposta define diretamente o que pode e o que não pode ser integrado.

2. **Vocês definem um percentual rígido de cobertura como portão e, se sim, o que impede os engenheiros de manipulá-lo com testes sem asserções?** O capítulo é firme em que a cobertura é um sinal, não um objetivo, em que alta cobertura de código trivial prova pouco e em que uma meta rígida convida à manipulação. Um único número imposto em uma grande organização produz de forma confiável testes que executam código sem afirmar nada, o que eleva a métrica e reduz a confiança real. Leve um sinal melhor à discussão: uma pontuação de teste de mutação nos seus módulos de maior valor, que mede se os testes de fato detectam falhas injetadas. Use a cobertura para encontrar áreas sem teste e o teste de mutação para profundidade e resista a transformar qualquer dos dois numa meta que a liderança acompanha isoladamente. Decida onde o número genuinamente ajuda e onde apenas convida ao teatro.

3. **Qual é a sua política quando a suíte de testes cresce devagar demais para os engenheiros esperarem por ela?** O compromisso central deste capítulo é confiança versus velocidade e custo, e ele nomeia o excesso de testes como um modo de falha real em que uma suíte inchada, redundante e lenta custa mais que os bugs que evita. Numa equipe grande, o tempo de execução da suíte é um imposto compartilhado pago a cada mudança, e uma suíte que as pessoas aprendem a contornar perde todo o seu valor. Leve as evidências: o tempo de relógio da CI, os testes mais lentos e quanta cobertura de ponta a ponta redundante duplica testes unitários mais baratos. Empurre os testes para o nível mais baixo que dá confiança real, paralelize e apague testes lentos e redundantes dentro de um prazo. Otimizar a confiança por segundo de feedback, e não a contagem bruta de testes, é o objetivo.

4. **Quando um teste fica instável, quem é o responsável, com que rapidez ele deve ser corrigido ou apagado e o que impõe esse prazo?** Este capítulo trata um teste instável como um teste quebrado, um defeito de primeira classe, porque uma suíte que falha ao acaso treina uma grande equipe a ignorar builds vermelhos e destrói em silêncio a rede de segurança de que todos dependem. A pressão concorrente é real: pôr um teste instável em quarentena desbloqueia a entrega hoje, mas arrisca mascarar um bug intermitente genuíno, enquanto bloquear por causa dele trava centenas de engenheiros por causa de uma falha que pode ser puro ruído. Leve as evidências que resolvem: a sua taxa atual de instabilidade, quanto tempo os testes ficam em quarentena antes de alguém tocá-los e quantos testes em quarentena acabaram escondendo um defeito real. Atribua um responsável a cada teste em quarentena, defina um prazo rígido para corrigir ou apagar e acompanhe a confiabilidade como uma métrica explícita da própria suíte. Em contextos corporativos e governamentais, em que um build verde faz parte da evidência de lançamento, uma pilha de quarentena sem gestão também é um passivo de auditoria, porque você está entregando com base num sinal em que combinou em privado não confiar.

5. **Vocês podem usar dados de produção em ambientes de teste e, se não, como vão gerar dados sintéticos fiéis o bastante para pegar defeitos reais?** O capítulo é direto em que as regras de privacidade muitas vezes proíbem dados pessoais reais em teste e em que os dados sintéticos precisam espelhar as características da produção ou seus testes dão falsa confiança. Para uma grande organização, a tensão é entre fidelidade e conformidade: os dados de produção pegam os casos de borda bagunçados que os dados sintéticos deixam passar, mas cada cópia deles multiplica a sua exposição e as suas obrigações. Leve os detalhes: quais conjuntos de dados carregam dados pessoais ou regulamentados, o que as suas regras de privacidade e de residência de dados de fato exigem e quão bem as suas fixtures atuais reproduzem as distribuições e os casos de borda vistos em produção. Padronize fábricas ou construtores para que cada teste monte exatamente os dados de que precisa e invista em geração sintética que corresponda a distribuições demográficas e de volume reais. Em programas governamentais e regulamentados, usar dados de cidadãos num ambiente de teste não é um atalho, é uma violação reportável, então a estratégia de dados precisa estar resolvida antes de o primeiro ambiente ser montado.

6. **Onde o TDD, o BDD ou o desenvolvimento guiado por especificação devem ser esperados e não opcionais, e quem decide?** Este capítulo apresenta essas práticas como disciplinas a aplicar onde acrescentam clareza, não como mandatos para cada linha de código, mas uma equipe grande se beneficia de um padrão compartilhado para que a prática não se fragmente equipe por equipe. O compromisso é entre os benefícios de design e de rastreabilidade (especificações executáveis que especialistas em políticas podem revisar, testes que sobrevivem à refatoração) e a curva de aprendizado genuína e a lentidão inicial que fazem um mandato geral sair pela culatra. Leve evidências para delimitar: quais módulos carregam lógica complexa ou altas taxas de falha de mudanças, onde os critérios de aceitação precisam ser rastreáveis até os requisitos e o que as equipes que já praticam isso relatam sobre velocidade e taxas de defeitos. Reserve a expectativa para a lógica complexa e as áreas carregadas de requisitos e deixe o código mais simples escolher por si. Em programas regulamentados e governamentais em que o software precisa ser rastreável até a lei que implementa, o desenvolvimento guiado por especificação com evidência de aceitação executável é menos uma preferência e mais um caminho para a sua autorização para operar, então nomeie explicitamente onde ele é exigido.

## Perspectiva por setor

**Startup.** Uma equipe minúscula não consegue manter uma equipe de QA, então faça a suíte merecer seu lugar: testes unitários rápidos a cada commit mais alguns testes de ponta a ponta sobre o único caminho que paga as contas, e nada que você não vá manter. Pule as metas de cobertura e teste a lógica que você mais tem medo de quebrar, para poder entregar várias vezes por dia sem uma passagem manual de regressão. Corrija um teste instável no mesmo dia, porque nesse estágio uma suíte que a equipe aprende a ignorar é pior que nenhuma suíte.

**Pequena empresa.** Sem engenheiro de testes dedicado e com orçamento apertado, apoie-se nos testes embutidos nos frameworks e ferramentas que você já usa em vez de um arcabouço sob medida que você não consegue manter. Priorize o punhado de verificações que protegem a receita e a confiança dos clientes e use CI hospedada para não manter você mesmo a infraestrutura de build. Prefira comprar a varredura de acessibilidade e de segurança como serviço a construí-la, já que um único defeito perdido pode custar mais que um ano da ferramenta.

**Grande empresa.** Entre muitas equipes, o problema da estratégia é a consistência: um padrão compartilhado de pirâmide, quarentena automática de testes instáveis e portões não funcionais que significam a mesma coisa em toda parte, para que um build verde seja confiável não importa quem o produziu. Oriente o tempo de execução da suíte como um imposto compartilhado e paralelize com firmeza, porque o tempo de relógio da CI é pago a cada mudança por cada engenheiro. Gerencie as pontuações de cobertura e de mutação como sinais de portfólio com responsáveis claros, não como números que a liderança acompanha isoladamente.

**Governo.** A contratação e a supervisão fazem dos testes evidência, não apenas higiene de engenharia. Expresse regras de elegibilidade e de política como especificações executáveis revisadas por especialistas do domínio, para poder rastrear o software até a lei que ele implementa, e torne bloqueantes os testes de acessibilidade e de segurança porque são exigidos por lei e fazem parte da evidência de autorização para operar. Use dados sintéticos gerados para corresponder a distribuições reais, já que dados de cidadãos num ambiente de teste são uma violação reportável, e mantenha os artefatos de teste auditáveis para que um revisor externo confirme exatamente o que foi verificado.

## Exemplos

**Startup.** Uma startup de cinco pessoas não pode bancar uma equipe de QA, então se apoia numa suíte rápida de testes unitários que roda a cada commit mais alguns testes de ponta a ponta cobrindo o caminho do cadastro ao pagamento que paga as contas. Os fundadores pulam a cobertura exaustiva e testam a lógica que mais temem quebrar, o que lhes permite entregar várias vezes por dia sem uma passagem manual de regressão. Quando um teste instável começa a falhar ao acaso, eles o corrigem no mesmo dia, porque uma suíte que a equipe aprende a ignorar é pior que nenhuma suíte no estágio em que a confiança é tudo.

**Grande empresa.** Uma grande plataforma de comércio eletrônico mantém milhares de testes unitários rápidos que rodam a cada commit em minutos, um conjunto focado de testes de integração em torno das fronteiras de pagamento e de estoque e uma pequena suíte de testes de ponta a ponta para as jornadas críticas de pagamento. Os testes de ponta a ponta instáveis são postos automaticamente em quarentena e atribuídos para conserto. Como os engenheiros confiam na suíte, implantam muitas vezes por dia, confiantes de que um build vermelho significa um problema real.

**Governo.** Um sistema nacional de benefícios que opera sob supervisão regulatória usa o BDD para expressar as regras de elegibilidade como especificações executáveis revisadas por especialistas em políticas, o que dá evidência rastreável de que o software implementa a lei. Usa dados sintéticos gerados para corresponder a distribuições demográficas reais, porque as regras de privacidade proíbem dados de cidadãos em ambientes de teste. O teste de acessibilidade é obrigatório e bloqueia o lançamento, já que o serviço precisa ser utilizável por todos os cidadãos. E o teste de segurança faz parte da evidência de autorização para operar (ATO), a aprovação formal para rodar o sistema em produção.

## Justificativa de negócio: motivações, ROI e TCO

O retorno dos testes é a capacidade de mudar o software com rapidez e segurança, que é a base de uma velocidade de entrega sustentada. Uma suíte automatizada confiável substitui o [teste de regressão](https://en.wikipedia.org/wiki/Regression_testing) manual, lento e caro e pega defeitos quando são mais baratos de corrigir, antes do lançamento e não em produção. Num sistema regulamentado ou voltado ao cidadão, o custo de um defeito em produção (correção, reputação e potencial exposição jurídica) faz sombra ao custo dos testes que o teriam pegado.

O custo de adoção é real: você escreve e mantém testes e constrói a infraestrutura de [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Mas o custo de não testar é maior e se acumula: desenvolvimento movido pelo medo que desacelera até se arrastar, regressões frequentes e processos manuais de lançamento que não escalam. Também há um custo em testar demais, então o argumento é por uma estratégia bem projetada, não pelo número máximo de testes. Para defender o caso junto à liderança, ligue a suíte à frequência de implantação, à taxa de falha de mudanças e ao tempo médio de recuperação e quantifique o esforço de teste manual que ela substitui e os incidentes de produção que ela evita.

## Antipadrões e armadilhas

- **Teste em casquinha de sorvete:** majoritariamente testes de ponta a ponta lentos sobre uma base unitária fina. Lento, instável, caro.
- **Cobertura como meta:** perseguir um percentual com testes triviais ou sem asserções que não provam nada.
- **Testar detalhes de implementação:** testes acoplados a internos que quebram a cada refatoração, desencorajando a mudança.
- **Instabilidade tolerada:** falhas aleatórias que treinam a equipe a ignorar builds vermelhos.
- **Dados de teste mutáveis e compartilhados:** testes que interferem uns nos outros e falham de modo imprevisível.
- **Usar dados de produção em teste:** uma violação de privacidade e de conformidade esperando para acontecer.
- **Teste não funcional pulado:** acessibilidade, desempenho e segurança descobertos só em produção.
- **A suíte sem confiança:** tão pouco confiável que os engenheiros rotineiramente a rodam de novo ou a contornam, anulando seu propósito.

## Modelo de maturidade

- **Nível 1, Iniciar:** O teste é manual e reativo. A cobertura automatizada é mínima. As regressões são frequentes e pegas tarde, muitas vezes pelos usuários e não pela suíte.
- **Nível 2, Desenvolver:** Existem testes unitários automatizados e alguns de integração, mas a suíte é lenta ou instável, a confiança é baixa e a prática varia muito de uma equipe para outra.
- **Nível 3, Padronizar:** Uma suíte equilibrada, rápida e confiável é o portão de cada mudança. Um padrão documentado de pirâmide, uma política de testes instáveis e o teste não funcional (acessibilidade, desempenho, segurança) são impostos de forma consistente entre as equipes.
- **Nível 4, Gerenciar:** A saúde da suíte é medida e controlada em relação a linhas de base. A taxa de instabilidade, o tempo de relógio da CI, a pontuação de mutação em módulos de alto valor e a taxa de defeitos escapados são acompanhados e revisados. A cobertura é um sinal entre vários, e os portões disparam por evidência e não por opinião.
- **Nível 5, Orquestrar:** Técnicas avançadas (baseadas em propriedades, de mutação, de fuzzing) miram o código de alto valor. O teste é integrado a métricas de entrega como frequência de implantação, taxa de falha de mudanças e tempo médio de recuperação. A organização remodela continuamente a suíte conforme a sua arquitetura e o seu risco, aposentando testes redundantes e investindo onde as evidências mostram que os defeitos ainda escapam.

## Ideias para discussão

- Que formato a sua distribuição de testes realmente tem, e ele corresponde à sua arquitetura e ao seu risco?
- Como você decide quando um trecho de código justifica teste baseado em propriedades ou de mutação em vez de testes de exemplo?
- Qual é a sua política para testes instáveis, e ela é de fato imposta?
- Como você gera dados sintéticos realistas sem vazar informações sensíveis?
- Onde a cobertura genuinamente ajuda você, e onde ela foi manipulada?
- Como os testes gerados por IA devem ser revisados para acrescentar confiança em vez de ruído?

## Principais conclusões

- Teste para ganhar confiança de mudar. Otimize a confiança por unidade de velocidade e de custo.
- Use a pirâmide como padrão, mas molde o teste à sua arquitetura.
- Trate os testes instáveis como defeitos e a cobertura como um sinal, não uma meta.
- Aplique técnicas avançadas onde o valor justifica o custo.
- Inclua testes de acessibilidade, desempenho e segurança na estratégia e use dados sintéticos para proteger a privacidade.

## Referências e leitura complementar

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles on the Test Pyramid and test-related patterns
