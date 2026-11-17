# 2.2 Princípios de design de software

## Visão geral e motivação

Os princípios de design de software são heurísticas para organizar o código de modo que você consiga entendê-lo, alterá-lo e estendê-lo ao longo do tempo. Incluem siglas com nome ([SOLID](https://en.wikipedia.org/wiki/SOLID) para cinco princípios de design [orientado a objetos](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) para não se repita, [KISS](https://en.wikipedia.org/wiki/KISS_principle) para mantenha simples, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) para você não vai precisar disso), conceitos estruturais ([acoplamento](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [coesão](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [separação de responsabilidades](https://en.wikipedia.org/wiki/Separation_of_concerns)), [padrões de projeto](https://en.wikipedia.org/wiki/Software_design_pattern) catalogados, abordagens de modelagem de mais alto nível como o [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (modelar o software na linguagem do domínio de negócio) e a escolha entre estilos orientado a objetos, [funcional](https://en.wikipedia.org/wiki/Functional_programming) e [orientado a dados](https://en.wikipedia.org/wiki/Data-oriented_design). Nenhum deles é lei. São experiência comprimida, e você precisa aplicá-los com discernimento.

Para equipes grandes, o valor dos princípios compartilhados é a coordenação. Quando centenas de engenheiros trabalham no mesmo sistema, precisam de um vocabulário comum para as discussões de design e de um conjunto comum de padrões para que módulos escritos de forma independente se encaixem. Um bom design é o que permite a muitas pessoas mudar um sistema em paralelo sem colisões constantes. É também o que mantém um sistema mutável uma década depois, a vida útil normal dos sistemas corporativos e governamentais, muito além da permanência de seus autores originais.

A habilidade crítica não é memorizar princípios. É saber quando cada um deles engana você. Todo princípio tem um modo de falha: o DRY pode produzir a abstração errada, o SOLID pode produzir indireção desnecessária, o YAGNI pode privar de extensibilidade de que você genuinamente precisa. Este capítulo trata os princípios como ferramentas com um domínio de aplicabilidade e enfatiza o acoplamento e a coesão como as propriedades mais profundas a que as siglas tentam servir.

## Princípios fundamentais

- Gerencie primeiro o acoplamento e a coesão. A maioria dos princípios nomeados são formas indiretas de melhorar essas duas propriedades.
- Otimize para a mudança: um bom design minimiza o custo das mudanças de que você realmente precisará.
- Prefira o design mais simples que funciona agora, mas mantenha fronteiras onde a mudança é provável.
- A duplicação é mais barata que a abstração errada. Espere até o padrão ficar claro.
- Torne as dependências explícitas e aponte-as para coisas estáveis.
- Modele o domínio na linguagem do domínio. Alinhe as fronteiras do software com as fronteiras do negócio.
- Escolha paradigmas para servir ao problema, não à ideologia. A maioria dos grandes sistemas é pragmaticamente mista.

## Recomendações

### Use o SOLID como lente, não como lista de verificação

Aplique a responsabilidade única para manter os módulos coesos, a inversão de dependência para apontar as dependências a abstrações onde uma fronteira de fato existe e o aberto-fechado onde os pontos de extensão são reais. Não fabrique interfaces, fábricas e camadas só para satisfazer a sigla quando há apenas uma implementação e nenhuma segunda à vista. A indireção tem um custo, e você o paga em cada leitura.

### Aplique o DRY ao conhecimento, não ao texto

O DRY trata de não duplicar uma única peça autoritativa de *conhecimento*. Não trata de eliminar linhas que apenas se parecem. Dois trechos de código que parecem semelhantes mas mudam por razões diferentes devem permanecer separados. Prefira um pouco de duplicação a uma abstração compartilhada prematura que acopla coisas sem relação. Extraia a abstração depois que o padrão real tiver aparecido duas ou três vezes.

### Deixe o KISS e o YAGNI resistirem à especulação

Construa para os requisitos que você tem, não para os que imagina. Evite a generalidade especulativa, como frameworks configuráveis, sistemas de plugins e pontos de extensão que ninguém pediu. O contrapeso é que alguma flexibilidade realmente é mais barata de embutir cedo, como uma interface estável ou uma costura limpa. O YAGNI argumenta contra a *implementação* especulativa, não contra fronteiras ponderadas.

### Projete explicitamente para baixo acoplamento e alta coesão

Faça cada módulo fazer uma coisa bem definida (coesão) e depender do menor número possível de outros módulos, por interfaces estreitas (baixo acoplamento). Ao revisar um design, pergunte quais mudanças reverberam através das fronteiras de módulo. Essas reverberações são a verdadeira medida do acoplamento. A separação de responsabilidades é a mesma ideia aplicada a camadas e a preocupações transversais.

### Use os padrões de projeto como vocabulário e os antipadrões como avisos

Os padrões são nomes compartilhados úteis para soluções recorrentes. Recorra a um quando o problema realmente corresponder a ele. Não imponha padrões para parecer sofisticado, porque código carregado de padrões costuma ser sinal de superengenharia. Aprenda os [antipadrões](https://en.wikipedia.org/wiki/Anti-pattern) comuns (objetos deus, modelos anêmicos onde não cabem, grandes bolas de lama, monólitos distribuídos) como rótulos de diagnóstico.

### Adote o Domain-Driven Design onde o domínio é complexo

Para sistemas com regras de negócio ricas, use as ferramentas táticas e estratégicas do DDD: uma linguagem ubíqua compartilhada com os especialistas do domínio, contextos delimitados que dividem o sistema em partes modeladas de forma independente e mapas de contexto que descrevem como essas partes se relacionam. Os contextos delimitados são especialmente valiosos em escala corporativa, porque alinham a responsabilidade das equipes com as fronteiras do modelo. O DDD é exagero para sistemas [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) simples (criar, ler, atualizar, excluir).

### Escolha os paradigmas pelo encaixe

Use a orientação a objetos para encapsular comportamento com estado e modelar domínios. Use o estilo funcional para transformações, concorrência e previsibilidade por meio da [imutabilidade](https://en.wikipedia.org/wiki/Immutable_object). Use o design orientado a dados onde o desempenho e o comportamento do cache dominam. Sistemas grandes misturam os três. Faça a escolha por componente e mantenha limpas as fronteiras entre os estilos.

## Compromissos: prós e contras

| Princípio / abordagem | Bem aplicado | Modo de falha |
|---|---|---|
| SOLID | Costuras claras onde a mudança acontece. Unidades testáveis | Proliferação de interfaces e camadas. Indireção sem retorno |
| DRY | Única fonte da verdade para conhecimento real | Abstração errada acoplando código sem relação |
| KISS / YAGNI | Sistemas enxutos e compreensíveis | Costuras subprojetadas. Adaptações caras de flexibilidade necessária |
| Padrões de projeto | Vocabulário compartilhado. Estruturas comprovadas | Culto a padrões. Complexidade acidental |
| Domain-Driven Design | Modelos e equipes alinhados. Complexidade domada | Cerimônia pesada em domínios simples. Fronteiras de contexto mal postas |
| Funcional / imutável | Previsibilidade. Concorrência mais segura | Encaixe desajeitado em problemas inerentemente com estado. Surpresas de desempenho |

A tensão recorrente é entre subprojeto e superprojeto. Sistemas subprojetados acumulam acoplamento e ficam rígidos. Sistemas superprojetados se afogam em abstração que alguém precisa entender e manter. A resposta não é um ponto fixo. É uma disciplina: adiar as decisões até ter informação suficiente, mantendo as costuras que permitem mudar de ideia.

## Perguntas para discutir com sua equipe

1. **Qual é o seu limiar concreto para extrair uma abstração compartilhada, e como você impede que o DRY produza a errada?** Este capítulo é direto ao dizer que a duplicação é mais barata que a abstração errada e que você deve esperar até o padrão ter aparecido duas ou três vezes antes de extrair. Numa equipe grande, o perigo é alguém fatorar dois trechos parecidos num módulo compartilhado através de fronteiras de equipe, e então toda mudança futura em um chamador reverberar no outro. O sinal a levar é se as duplicatas mudam pela mesma razão ou apenas se parecem agora. Combine uma regra de três e exija que uma abstração candidata tenha de fato mudado em conjunto antes de acoplar os chamadores. Esse único acordo evita uma classe de acoplamento que é cara de desfazer depois que muitas equipes dependem dela.

2. **Como você torna visíveis o acoplamento e a coesão na revisão de design em vez de deixá-los à intuição?** Os princípios fundamentais põem o acoplamento e a coesão acima de toda sigla e definem o acoplamento como as mudanças que reverberam através das fronteiras de módulo. A intuição não escala entre centenas de engenheiros que veem, cada um, só o seu canto do sistema. Leve evidências que uma máquina possa produzir: grafos de dependência e dados de co-mudança mostrando quais módulos continuam sendo editados juntos nos mesmos commits. Acrescente uma pergunta explícita de revisão sobre quais fronteiras de módulo uma mudança obriga você a cruzar. Quando dois módulos sempre mudam juntos, é sinal para fundi-los ou corrigir a fronteira entre eles.

3. **Onde está a linha, nos seus sistemas, entre um domínio rico o bastante para justificar o Domain-Driven Design e um aplicativo CRUD simples em que ele é exagero?** O capítulo recomenda os contextos delimitados do DDD precisamente porque alinham a responsabilidade das equipes com as fronteiras do modelo, e avisa que o DDD é exagero para sistemas simples de criar-ler-atualizar-excluir e degenera em cerimônia sem modelagem real. Errar em qualquer direção é caro: DDD pesado num domínio raso enterra um aplicativo simples em cerimônia, enquanto um modelo compartilhado e extenso entre muitas equipes força coordenação constante entre elas. Leve os sinais que de fato decidem: a densidade das regras de negócio e quantas equipes precisam ser donas de partes de forma independente. Reserve o maquinário estratégico para o núcleo complexo e deixe as bordas simples permanecerem simples. Isso o mantém longe tanto do teatro do DDD quanto da grande bola de lama.

4. **Quando uma abstração, interface ou padrão de projeto vale a indireção que acrescenta, e quem tem autoridade para chamar um design de superengenharia?** Este capítulo é explícito em que a indireção tem um custo que você paga em cada leitura e que fabricar interfaces, fábricas e camadas para satisfazer o SOLID ou para parecer sofisticado é um modo de falha. Numa equipe grande a pressão corre no outro sentido: os revisores deixam passar abstração extra porque parece disciplinada, e ninguém quer ser a pessoa defendendo menos estrutura. A consideração concorrente é real, porque algumas costuras de fato merecem seu lugar e removê-las depois é caro. Leve evidências concretas à discussão: quantas implementações uma interface tem de fato hoje, quantas vezes o ponto de extensão já foi usado e quantos arquivos um leitor precisa abrir para seguir um caminho de código. Combine que uma única implementação sem segunda à vista é uma razão padrão para embutir e nomeie quem pode rotular um design de superprojetado sem que isso soe como insulto. Em sistemas corporativos e governamentais que sobrevivem a seus autores por uma década, a indireção gratuita é um imposto que todo mantenedor futuro paga, então trate “o que esta abstração nos compra” como uma pergunta permanente de revisão, não como um desafio pessoal.

5. **Como você decide qual paradigma cada componente usa, orientado a objetos, funcional ou orientado a dados, e como mantém limpas as fronteiras entre eles?** O capítulo argumenta que sistemas grandes são pragmaticamente mistos e que você deve escolher por componente pelo encaixe, usando a orientação a objetos para domínios com estado, o estilo funcional para transformações e concorrência e o design orientado a dados onde o desempenho e o comportamento do cache dominam. Sem gestão, a escolha do paradigma vira questão de quem escreveu o módulo primeiro, e o estado mutável vaza para o que deveriam ser transformações puras, ou um purismo funcional luta contra um problema inerentemente com estado. A evidência que vale levar é onde está a sua dor real: quais componentes são difíceis de testar por causa de estado oculto, quais caminhos quentes são limitados pelo cache e onde o estilo atual força contornos desajeitados. Decida deliberadamente o paradigma padrão de cada camada e escreva onde caem as costuras entre os estilos, para que um núcleo funcional e uma borda imperativa não vazem um para o outro. Para um sistema regulamentado ou governamental em que um cálculo precisa ser auditável e reproduzível para um dado período, um núcleo imutável e funcional costuma ser um requisito de conformidade e não um gosto, e essa restrição deve conduzir a fronteira em vez de segui-la.

6. **Como você impede que esses princípios endureçam em dogma, e onde registra o raciocínio por trás de uma decisão de design para que uma equipe futura possa revisitá-la?** Todo princípio deste capítulo tem um domínio de aplicabilidade e um modo de falha, e todo o enquadramento os trata como ferramentas a aplicar com discernimento e não como leis a impor. Numa equipe grande, um princípio vira regra em silêncio: o DRY proíbe qualquer duplicação, o SOLID obriga uma interface por classe e as exceções pragmáticas são barradas na revisão por pessoas que citam a sigla e não o resultado. A tensão é que alguma consistência de fato ajuda centenas de engenheiros a se coordenar, então você não pode simplesmente declarar todo princípio opcional. Leve exemplos em que seguir um princípio à risca produziu um design pior e leve os registros de decisão, se houver, que explicam por que uma dada fronteira ou abstração existe. Combine que os princípios são padrões dos quais um engenheiro pode se desviar com uma razão registrada e capture as escolhas de design consequentes num curto registro de decisão de arquitetura, para que a próxima equipe herde o raciocínio e não só o código. Em sistemas corporativos e do setor público, onde os autores originais já se foram e as auditorias perguntam por que o sistema tem a forma que tem, essa trilha escrita é a diferença entre um design que equipes futuras podem mudar com segurança e um que elas têm medo de tocar.

## Perspectiva por setor

**Startup.** Favoreça o design mais simples que entrega e mantenha um único módulo bem fatorado até que um segundo caso de uso real force uma costura. Seu recurso mais escasso é a atenção de engenharia, então interfaces, camadas e frameworks especulativos prematuros são puro custo. Siga a regra de três antes de extrair qualquer abstração compartilhada e deixe o YAGNI matar os pontos de extensão que ninguém pediu ainda.

**Pequena empresa.** Sem arquiteto dedicado e com orçamento apertado, apoie-se no design já embutido nos frameworks e bibliotecas que você compra, em vez de inventar seus próprios padrões. Reserve o esforço de design sob medida para o punhado de regras que genuinamente são o seu negócio e mantenha todo o resto convencional para que um terceirizado ou uma pessoa nova consiga ler. Um pouco de duplicação que você entende vence uma abstração engenhosa que só o autor consegue manter.

**Grande empresa.** O retorno de princípios compartilhados é a coordenação entre muitas equipes: um vocabulário comum para a revisão de design e contextos delimitados que alinham as fronteiras do modelo com a responsabilidade das equipes, para que os grupos evoluam de forma independente. Gerencie o acoplamento e a coesão explicitamente com dados de dependência e de co-mudança e registre as decisões de design consequentes para que os sistemas continuem mutáveis muito depois de seus autores seguirem adiante. Proteja-se igualmente da abstração errada que acopla equipes e da superengenharia que taxa todo leitor.

**Governo.** A auditabilidade e a reprodutibilidade muitas vezes ditam o design. Um núcleo imutável e funcional permite reproduzir exatamente um cálculo histórico de um dado período, o que um grafo de objetos emaranhado com estado mutável oculto não consegue garantir. Prefira contratos publicados explícitos a tabelas compartilhadas nas fronteiras de contexto e mantenha o design e seus registros de decisão legíveis para auditores e para a equipe que herdar o sistema uma década depois.

## Exemplos

**Startup.** Uma startup de três engenheiros que constrói seu primeiro produto resiste à vontade de dividir cada funcionalidade em camadas de interfaces e fábricas, mantendo um único módulo bem fatorado até aparecer um segundo caso de uso real. Quando a mesma lógica aparece uma terceira vez nos fluxos de cadastro e de cobrança, eles extraem uma pequena função compartilhada em vez de um framework especulativo. Isso mantém a base de código pequena o bastante para que qualquer um deles a guarde na cabeça, e as poucas costuras que traçam caem onde o produto tem mais probabilidade de mudar.

**Grande empresa.** Uma grande plataforma de seguros modela apólice, sinistros e cobrança como contextos delimitados separados, cada um sob responsabilidade de uma equipe dedicada, com seu próprio modelo de dados e fronteira de serviço. Onde os contextos se encontram, como quando um sinistro referencia uma apólice, eles conversam por contratos publicados explícitos em vez de tabelas de banco de dados compartilhadas. Isso permite às três equipes evoluir de forma independente, e a linguagem ubíqua mantém precisas as conversas com subscritores e atuários. Uma versão anterior compartilhava um único modelo extenso, e toda mudança exigia coordenação entre equipes.

**Governo.** Um sistema nacional de processamento de impostos favorece deliberadamente um núcleo funcional e orientado a dados para o seu motor de cálculo. As regras tributárias são expressas como transformações puras sobre registros de entrada imutáveis, o que as torna auditáveis, testáveis e reproduzíveis para um dado ano fiscal. As partes imperativas e com estado (fluxo de trabalho, notificações) ficam nas bordas. Os auditores podem apontar uma versão específica de uma regra e reproduzir exatamente qualquer cálculo histórico, o que é uma exigência legal que um grafo de objetos emaranhado com estado mutável oculto não poderia garantir.

## Justificativa de negócio: motivações, ROI e TCO

A qualidade do design é um investimento na *capacidade de mudança* de um sistema, e a capacidade de mudança domina o custo total de propriedade. A maior parte do custo de um sistema cai depois do primeiro lançamento, em modificação e extensão. Sistemas bem projetados mantêm o custo de mudança aproximadamente constante ao longo do tempo. Os mal projetados veem o custo de cada mudança subir até o sistema se tornar efetivamente imodificável e precisar ser reescrito, o mais caro de todos os desfechos.

O custo de adoção é principalmente habilidade e disciplina de revisão: ensinar os princípios e gastar tempo de design logo no início. O custo de não adotá-los é o lento acúmulo de [dívida técnica](https://en.wikipedia.org/wiki/Technical_debt), a queda da velocidade de entrega, o aumento das taxas de defeitos e as eventuais reescritas caras. Para defender o caso junto à liderança, ligue a disciplina de design à previsibilidade de entrega e à prevenção de programas de reescrita e acompanhe indicadores antecedentes como a taxa de falha de mudanças e o tempo para implementar funcionalidades comparáveis ao longo do tempo. Cuidado também com a falha oposta: investir demais em design para futuros incertos também destrói valor. Por isso o argumento é por um design *apropriado*, calibrado conforme a probabilidade e o custo da mudança futura.

## Antipadrões e armadilhas

- **Generalidade especulativa:** construir extensibilidade para requisitos imaginados que nunca chegam.
- **A abstração errada:** forçar código sem relação a ficar junto para satisfazer o DRY, criando um acoplamento pior que a duplicação.
- **Culto a padrões:** aplicar padrões de projeto por si mesmos, acrescentando indireção sem benefício.
- **Objetos anêmicos ou deus:** modelos sem comportamento ou objetos que fazem tudo. Ambos sinalizam responsabilidades mal postas.
- **Monólito distribuído:** serviços separados fisicamente mas ainda fortemente acoplados, combinando os custos das duas abordagens.
- **Grande bola de lama:** nenhuma estrutura discernível. Toda mudança arrisca tudo.
- **Teatro do DDD:** adotar o vocabulário e a estrutura de pastas sem a modelagem de domínio que dá valor a eles.

## Modelo de maturidade

- **Nível 1, Iniciar:** O design é ad hoc e reativo. O acoplamento se acumula sem controle. Os princípios são desconhecidos ou invocados como slogans, e as abstrações aparecem ou somem por hábito individual.
- **Nível 2, Desenvolver:** As equipes conhecem os princípios e os aplicam, mas de forma inconsistente e muitas vezes dogmática. Alguns grupos gerenciam o acoplamento e a coesão deliberadamente e outros não, e não há vocabulário compartilhado na organização.
- **Nível 3, Padronizar:** Um vocabulário de design compartilhado, uma regra de três para extrair abstrações, a análise de acoplamento e coesão e contextos delimitados alinhados às equipes são documentados e esperados em toda a organização, aplicados de forma consistente na revisão de design e não deixados ao gosto individual.
- **Nível 4, Gerenciar:** A saúde do design é medida em relação a linhas de base: dados de acoplamento e de co-mudança, taxa de falha de mudanças e tempo para implementar funcionalidades comparáveis são acompanhados ao longo do tempo, de modo que abstrações e fronteiras são acrescentadas, mantidas ou removidas com base em evidências, e a superengenharia e a abstração errada são pegas por dados e não por opinião.
- **Nível 5, Orquestrar:** A disciplina de design é integrada ao planejamento de entrega e de risco em toda a organização. Os princípios são aplicados com nuance e conhecimento dos modos de falha. As escolhas de paradigma e de fronteira são deliberadas e continuamente revisitadas, e a organização rotineiramente refatora, redefine o escopo e aposenta abstrações conforme o domínio e as evidências mudam.

## Ideias para discussão

- Como você distingue uma costura necessária de uma generalidade especulativa antes de ter o requisito futuro?
- Quando o DRY levou a sua equipe à abstração errada, e como vocês a reconheceram?
- Onde devem cair as fronteiras dos contextos delimitados, e quão de perto devem espelhar o organograma?
- Quanto design deve preceder o código no seu contexto, e como vocês registram as decisões?
- Que partes do seu sistema se beneficiariam de um estilo mais funcional ou orientado a dados?
- Como você impede que os princípios de design endureçam em dogma que resiste a exceções pragmáticas?

## Principais conclusões

- Acoplamento e coesão são as propriedades que importam. As siglas são meios para esses fins.
- Todo princípio tem um modo de falha. Saiba quando cada um engana.
- Prefira um pouco de duplicação a uma abstração prematura ou errada.
- Use o DDD e os contextos delimitados para alinhar domínios complexos com a responsabilidade das equipes.
- Escolha os paradigmas pelo encaixe. Sistemas grandes são pragmaticamente mistos.
- Projete para as mudanças de que você realmente precisará, evitando tanto o subprojeto quanto o superprojeto.

## Referências e leitura complementar

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
