# 2.1 Padrões de codificação e estilo

## Visão geral e motivação

Os padrões de codificação são as convenções compartilhadas que permitem a muitas pessoas escrever código como se um único autor cuidadoso o tivesse escrito. Eles cobrem nomenclatura, formatação, organização de arquivos, idiomas de programação, tratamento de erros e os paradigmas que uma equipe favorece. Numa equipe pequena, o gosto individual pode prevalecer. Numa equipe grande (centenas ou milhares de engenheiros, muitos terceirizados, alta rotatividade), a inconsistência se torna um imposto pago a cada leitura, a cada revisão e a cada integração. Os padrões transformam inúmeras pequenas discussões de estilo numa decisão única que uma máquina então impõe por você.

Para grandes organizações, o que está em jogo é concreto. O código é lido muito mais vezes do que é escrito. Em contextos corporativos e governamentais, uma linha de código pode ser lida por auditores, revisores de segurança e mantenedores anos depois de o autor ter saído. Um estilo consistente reduz o custo mental dessa leitura, diminui a superfície para bugs e torna confiável a análise automatizada entre [linters](https://en.wikipedia.org/wiki/Lint_(software)) (ferramentas que sinalizam automaticamente prováveis bugs e violações de estilo), escâneres de segurança e ferramentas de [refatoração](https://en.wikipedia.org/wiki/Code_refactoring). Onde há regulamentação, como em serviços financeiros, saúde, defesa e sistemas do setor público, os padrões também fazem parte da evidência de que uma base de código é mantível e controlada.

A abordagem moderna é tratar o estilo como uma preocupação resolvida e automatizada, e não como uma questão de julgamento humano contínuo. Formatadores e linters rodam no editor, em hooks de pré-commit e na [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), o processo automatizado de build e teste que roda a cada mudança. As máquinas impõem o estilo, para que você possa gastar a atenção da revisão no design e na correção. O objetivo não é a uniformidade pela uniformidade. É a remoção de atrito: você deve conseguir transitar entre serviços e equipes sem reaprender o básico.

## Princípios fundamentais

- Consistência vence preferência individual. Um único estilo acordado, aplicado em toda parte, vale mais que o “melhor” estilo aplicado de forma desigual.
- Automatize a imposição. Formatadores e linters são a fonte da verdade, não comentários de revisão de código sobre espaçamento.
- Otimize para o leitor e o mantenedor, não para o autor original.
- Prefira as convenções que a comunidade mais ampla da linguagem já usa a regras caseiras sob medida.
- Facilite a adoção do padrão: forneça configurações compartilhadas, modelos e ferramentas em vez de um PDF que ninguém lê.
- As regras de estilo devem ser poucas, defensáveis e inequívocas. Toda regra tem um mecanismo de imposição ou é apenas uma sugestão.
- A nomenclatura é a decisão de legibilidade de maior alavancagem e merece orientação explícita.

## Recomendações

### Adote um guia de estilo canônico por linguagem

Para cada linguagem que você usa, adote um guia de estilo amplamente reconhecido como base (por exemplo, o guia da comunidade ou do fornecedor para essa linguagem) e documente apenas as diferenças de que a sua organização precisa. Não invente um estilo caseiro do zero. Publique a sua escolha num lugar central e localizável e versione-a como código.

### Faça dos formatadores padrões inegociáveis

Use um formatador automático opinativo para toda linguagem que tenha um, com uma única configuração compartilhada versionada no repositório. A formatação nunca deve aparecer na revisão, porque é aplicada automaticamente ao salvar e verificada na CI. Onde a linguagem não tem um formatador forte, escolha uma configuração de linter e trate-a da mesma forma.

### Rode linters como portões impostos, não como conselho

Configure os linters com um conjunto de regras acordado, quebre o build diante de violações e mantenha o conjunto de regras no [controle de versões](https://en.wikipedia.org/wiki/Version_control), para que as mudanças passem por revisão. Separe as regras corrigíveis automaticamente (aplique-as automaticamente) das que precisam de julgamento humano (sinalize e bloqueie). Introduza novas regras no modo “aviso”, zere o acúmulo e depois promova-as a “erro”.

### Imponha em várias camadas

Ofereça integração com o editor para feedback instantâneo, hooks de pré-commit para imposição local e verificações de CI como portão autoritativo. Quanto mais cedo você pega uma violação, mais barato é. A CI precisa ser a última barreira, porque os hooks locais podem ser contornados.

### Dê regras explícitas à nomenclatura

Padronize as convenções de capitalização por linguagem, exija nomes que revelem a intenção, proíba abreviações enganosas e defina convenções para booleanos, coleções, unidades e operações assíncronas. Registre o seu vocabulário de domínio num glossário compartilhado para que o mesmo conceito tenha o mesmo nome em toda parte.

### Gerencie a consistência poliglota deliberadamente

Numa base de código que abrange várias linguagens, busque conceitos consistentes (padrões de tratamento de erros, estrutura de logs, organização de projeto) mesmo onde a sintaxe difere. Forneça configurações por linguagem a partir de um repositório central, para que um novo serviço herde os padrões automaticamente por modelos ou esqueletos.

### Codifique idiomas e paradigmas

Vá além da formatação. Escreva os seus idiomas preferidos, como tratar erros, como estruturar módulos e quando usar exceções versus tipos de resultado, junto com os paradigmas que suas equipes favorecem. É aqui que vivem a legibilidade e a manutenibilidade reais.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Formatador automático estrito, sem configuração | Acaba com todo debate de formatação. Consistência instantânea. Integração trivial | Algumas escolhas de que não se gosta são inegociáveis. Grande diff inicial quando aplicado pela primeira vez |
| Linter configurável com regras da casa | Sob medida para as necessidades da organização. Pode codificar regras reais de prevenção de bugs | Deriva de configuração. Discussões triviais sobre regras. Custo de manutenção |
| Padrão da comunidade adotado por inteiro | Familiar às pessoas contratadas. Forte ecossistema de ferramentas. Baixa manutenção | Pode não servir a restrições específicas da organização. Regras ocasionalmente desajeitadas |
| Padrão interno sob medida | Serve exatamente à organização | Caro de escrever e manter. Desconhecido das pessoas contratadas. Ferramentas fracas |
| Autonomia por equipe | Moral local alta. Específico ao contexto | Fragmentação. Mobilidade entre equipes dolorosa. Ferramentas inconsistentes |

Os padrões impostos trocam um pouco de autonomia individual por grandes ganhos coletivos: menos atrito na revisão, integração mais rápida e automação confiável. O principal risco é superprojetar o padrão em centenas de regras que atrasam todo mundo sem evitar defeitos reais. Mantenha o conjunto de regras pequeno e baseado em evidências e incline-se a adotar um padrão existente para que a manutenção continue barata.

## Perguntas para discutir com sua equipe

1. **Quais regras de linter devem quebrar o build, e como você promove uma regra de aviso a erro sem parar todo mundo?** Este capítulo argumenta que toda regra precisa de um mecanismo de imposição e que as novas regras devem entrar no modo aviso, ter o acúmulo zerado e só então virar erro. Numa equipe grande, virar uma regra para erro contra uma base de código suja bloqueia centenas de mudanças não relacionadas da noite para o dia. Leve evidências concretas à reunião: a contagem atual de violações de cada regra candidata e se ela é corrigível automaticamente ou exige julgamento humano. Em contextos corporativos e governamentais, a linha entre passar e falhar também alimenta portões de auditoria, então um conjunto de regras ambíguo enfraquece a sua história de conformidade. Decida uma implantação em etapas: corrija automaticamente o que puder, oriente a limpeza e só então imponha o portão.

2. **Quando você aplicar um formatador pela primeira vez ao seu código legado, como evitará que essa reformatação destrua o git blame e afogue as revisões?** A tabela de compromissos avisa sobre um grande diff inicial, e a seção de antipadrões destaca a mistura de commits de reformatação com mudanças de lógica. Uma única reformatação abrangente reescreve milhares de linhas e faz o blame apontar para a reformatação e não para o autor real, o que prejudica quem depura anos depois. Faça a reformatação num único commit isolado e claramente rotulado e registre-o num arquivo de ignorar-blame para que o histórico continue útil. Para os auditores que rastreiam quem mudou o quê, esse isolamento é a diferença entre evidência limpa e ruído. Combine a sequência antes de mexer no código, não depois.

3. **Quem é o responsável pelo seu glossário de nomenclatura e vocabulário de domínio, e como um termo novo é acrescentado?** O capítulo chama a nomenclatura de decisão de legibilidade de maior alavancagem e pede que você registre o vocabulário de domínio num glossário compartilhado. Sem um responsável nomeado, o mesmo conceito ganha três nomes diferentes entre as equipes, e as ferramentas de análise estática e de busca perdem a confiabilidade. Leve exemplos de conceitos que já têm nomes conflitantes na sua base de código como sinal concreto. Atribua um responsável e um caminho leve de proposta, para que acrescentar ou renomear um termo seja uma pequena mudança revisada e não uma discussão em cada pull request. A resposta muda a integração: uma pessoa nova lê um glossário em vez de fazer engenharia reversa da intenção a partir de código inconsistente.

4. **Para cada linguagem, vocês adotam por inteiro um guia de estilo reconhecido da comunidade ou do fornecedor, e onde as diferenças da casa são realmente justificadas?** Este capítulo argumenta que você deve tomar um padrão existente como base e documentar apenas as diferenças de que a sua organização precisa, porque um padrão sob medida é caro de escrever e desconhecido das pessoas contratadas. A força contrária é real: uma restrição interna (uma regra de segurança, um framework legado, um mandato de acessibilidade) às vezes de fato entra em conflito com o padrão da comunidade, e toda diferença que você mantém é uma regra que agora é sua e que você mantém para sempre. Leve a lista de diferenças propostas à reunião, cada uma com a restrição concreta que a motiva, e esteja pronto para cortar qualquer diferença que seja só gosto. Em contextos corporativos e governamentais, uma base que corresponde à comunidade mais ampla da linguagem também significa que terceirizados e novos fornecedores chegam já fluentes, o que encurta a integração e reforça a evidência de manutenibilidade que os auditores procuram.

5. **Numa base de código poliglota, quais convenções são realmente universais e quais permanecem locais à linguagem, e como você impede que as configurações por repositório derivem?** O capítulo pede conceitos consistentes (tratamento de erros, estrutura de logs, organização de projeto) entre linguagens mesmo onde a sintaxe difere, e configurações por linguagem servidas de um repositório central para que novos serviços herdem os padrões automaticamente. A tensão é que forçar os idiomas de uma linguagem sobre outra produz código desajeitado e não idiomático, enquanto deixar cada equipe bifurcar a própria configuração faz “o padrão” não significar nada. Leve um inventário das suas atuais configurações de linter e formatador por repositório e um diff mostrando o quanto elas já se afastaram, como sinal concreto. Para uma grande organização que opera dezenas de serviços, decida o mecanismo de distribuição (modelos, esqueletos, um pacote de configuração compartilhado) para que uma mudança de regra se propague uma vez em vez de ser copiada à mão para cada repositório.

6. **Quando desativar uma regra é legítimo, quem revisa a supressão e como você impede que desativações em bloco esvaziem o padrão?** A seção de antipadrões aponta supressões inline generalizadas como sinal de que uma regra está errada ou de que uma equipe desistiu, mas uma política rígida sem exceções leva as pessoas a escrever código pior só para satisfazer o linter. Combine um caminho leve: uma supressão precisa trazer um motivo, ficar no menor escopo possível e ser visível na revisão, e não enterrada num arquivo global de ignorar. Leve a contagem atual de supressões por regra e por repositório, porque uma regra suprimida centenas de vezes está dizendo algo sobre a regra, não sobre o código. No trabalho regulamentado e do setor público, supressões em bloco sem explicação enfraquecem diretamente a história de auditoria, já que o pipeline deixa de poder mostrar que o código integrado genuinamente passou pelos portões acordados.

## Perspectiva por setor

**Startup.** A velocidade vence, então adote os padrões da comunidade de formatador e linter para a sua única linguagem no primeiro dia e ligue-os a um hook de pré-commit e à CI antes de a segunda pessoa engenheira chegar. Não escreva um estilo caseiro que você não tem tempo de manter: a configuração enviada no repositório é o padrão inteiro. Ao acrescentar uma segunda linguagem, recorra ao guia canônico dessa linguagem em vez de inventar convenções do zero.

**Pequena empresa.** Sem especialista dedicado em ferramentas e com orçamento apertado, apoie-se inteiramente no formatador gratuito e opinativo que acompanha a sua linguagem ou existe ao lado dela e aceite os padrões dele em vez de ajustá-los. É um caso claro de comprar em vez de construir: manter um conjunto de regras sob medida custa um tempo que você não tem, enquanto um formatador pronto não custa nada e encerra o debate de estilo de imediato. Mantenha a configuração no repositório para que o terceirizado que você contratar no ano que vem a herde sem uma conversa.

**Grande empresa.** Em escala, o trabalho é governança entre muitas equipes: um repositório central de padrões de engenharia com as configurações compartilhadas de formatador e linter por linguagem, novos serviços gerados a partir de modelos que puxam essas configurações e portões de CI que bloqueiam integrações em desconformidade. Versione o conjunto de regras como código e encaminhe as mudanças por uma revisão periódica, para que os padrões evoluam deliberadamente em vez de derivar. O retorno são engenheiros que transitam entre equipes para um código familiar e ferramentas automatizadas que produzem sinal confiável porque todo repositório é consistente.

**Governo.** A contratação e a responsabilização pública moldam a escolha: imponha um estilo específico e um conjunto de regras de segurança como parte dos requisitos de autorização para operar, e faça o pipeline emitir um relatório mostrando que toda mudança integrada passou pelos portões acordados, como evidência de auditoria. Como um formatador é aplicado automaticamente, o código de vários fornecedores e terceirizados parece consistente, o que protege o trabalho público de manutenção muito depois do fim dos contratos. Favoreça bases reconhecidas da comunidade em vez de regras sob medida, para que o padrão seja transparente e qualquer fornecedor futuro possa adotá-lo sem aprisionamento proprietário.

## Exemplos

**Startup.** Uma startup de quatro pessoas adota os padrões da comunidade de formatador e linter para a sua única linguagem no primeiro dia, ligando-os a um hook de pré-commit e à CI para que ninguém discuta espaçamento na revisão. Como a configuração vem dentro do repositório, a quinta e a sexta contratações a herdam automaticamente e nunca veem um comentário de formatação. Quando a equipe depois acrescenta uma segunda linguagem, recorre ao guia padrão dessa linguagem em vez de inventar um estilo caseiro que não tem tempo de manter.

**Grande empresa.** Um grande banco opera serviços em Java, Python e TypeScript em dezenas de equipes. Ele publica um repositório central de “padrões de engenharia” com as configurações compartilhadas de formatador e linter para cada linguagem. Os novos serviços são gerados a partir de um modelo que puxa essas configurações, de modo que todo repositório já começa em conformidade. A CI bloqueia as integrações diante de qualquer violação, e uma revisão trimestral governa as mudanças de regra. O tempo de integração de engenheiros que transitam entre equipes cai de forma perceptível, porque todo repositório parece familiar.

**Governo.** Uma agência do setor público que moderniza um sistema legado impõe um conjunto de regras de linting de acessibilidade e segurança como parte de seus requisitos de autorização para operar (ATO), a aprovação formal necessária para rodar o sistema em produção. A conformidade de estilo passa a fazer parte da evidência de auditoria: o pipeline produz um relatório mostrando que todo o código integrado passou pelos portões acordados de [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis). Como um formatador é aplicado automaticamente, terceirizados de vários fornecedores produzem código visualmente consistente, o que facilita o trabalho de manutenção de longo prazo do governo depois do fim dos contratos.

## Justificativa de negócio: motivações, ROI e TCO

O custo de adotar padrões é em grande parte único: escolher guias, montar as ferramentas e aplicar um grande commit inicial de reformatação. O custo recorrente é baixo, porque a imposição é automatizada. O custo de *não* adotar padrões é recorrente e cumulativo: cada revisão gasta minutos com estilo, cada integração é mais lenta, as ferramentas de análise estática produzem ruído e o código inconsistente esconde bugs. Numa grande organização, esses minutos somam perdas equivalentes a tempo integral.

O retorno aparece como menor latência de revisão, menos comentários de revisão sobre estilo, integração mais rápida e maior sinal das ferramentas automatizadas. Em ambientes regulamentados há um retorno adicional em prontidão para auditoria: controles demonstráveis e impostos reduzem o esforço e o risco das revisões de conformidade. Para defender o caso junto à liderança, apresente os padrões como uma alavanca de baixo custo e alto impacto sobre a produtividade dos desenvolvedores e a postura de auditoria e ponha um número no custo atual da inconsistência usando análise de comentários de revisão e dados de pesquisas de integração.

## Antipadrões e armadilhas

- **Estilo debatido na revisão de código:** o sinal de que a imposição não é automatizada. Mova a regra para as ferramentas.
- **O documento de padrões não lido:** uma página de wiki sem imposição é decoração. Toda regra precisa de um mecanismo.
- **Proliferação de regras:** centenas de regras pedantes que atrasam o trabalho sem evitar defeitos.
- **Deriva de configuração:** cada repositório bifurca a própria configuração de linter até “o padrão” não significar nada.
- **Formatar o repositório inteiro no meio do trabalho de uma funcionalidade:** misturar commits de reformatação com mudanças de lógica destrói a revisão e o blame. Faça grandes reformatações em commits isolados e claramente rotulados.
- **Ignorar o linter com supressões em bloco:** desativações inline generalizadas sinalizam uma regra errada ou uma equipe que desistiu.
- **Padrões sem responsável:** sem um responsável claro, as regras nunca evoluem e apodrecem.

## Modelo de maturidade

- **Nível 1, Iniciar:** O estilo é por autor e reativo. Não há configurações compartilhadas. A formatação é discutida na revisão e decidida por quem mais se importa naquele dia.
- **Nível 2, Desenvolver:** Equipes individuais adotam um formatador e um linter, mas as configurações e os conjuntos de regras variam de equipe para equipe e de repositório para repositório, de modo que a consistência para na fronteira de cada equipe.
- **Nível 3, Padronizar:** Configurações centrais compartilhadas por linguagem são documentadas e impostas em toda a organização. A CI bloqueia integrações em desconformidade. Os novos repositórios herdam os padrões automaticamente por modelos ou esqueletos.
- **Nível 4, Gerenciar:** O padrão é medido e controlado com dados: taxas de violação, contagens de supressão, comentários de revisão sobre estilo e tempo de integração são acompanhados em relação a linhas de base, e as mudanças de regra são promovidas ou aposentadas com base nessa evidência e não em opinião.
- **Nível 5, Orquestrar:** Os padrões são continuamente melhorados e integrados em toda a organização. Os idiomas poliglotas e o vocabulário de domínio são documentados e impostos, a imposição é quase sem atrito e o conjunto de regras se adapta conforme linguagens, ferramentas e necessidades da organização mudam.

## Ideias para discussão

- Onde está a linha entre uma regra imposta e uma diretriz documentada que confia no julgamento do engenheiro?
- Como a organização deve tratar uma regra querida da comunidade que entra em conflito com uma restrição interna genuína?
- Quem é o responsável pelos padrões, e como as mudanças de regra são propostas, debatidas e implantadas sem perturbação?
- Numa base de código poliglota, quais convenções devem ser realmente universais e quais devem permanecer locais à linguagem?
- Como você adapta padrões a uma grande base de código legada sem uma reformatação disruptiva de uma só vez?
- Que papel as ferramentas assistidas por IA devem ter ao sugerir ou impor idiomas além da formatação mecânica?

## Principais conclusões

- Trate o estilo como um problema automatizado e resolvido, para que as pessoas revisem design e correção.
- Adote padrões existentes da comunidade e documente apenas as diferenças.
- Imponha nas camadas do editor, do pré-commit e da CI, com a CI como portão autoritativo.
- Mantenha o conjunto de regras pequeno, defensável e governado centralmente.
- Nomenclatura e idiomas, não espaçamento, são onde a legibilidade é realmente conquistada.

## Referências e leitura complementar

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell and Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* and language style guides (as reference exemplars)
