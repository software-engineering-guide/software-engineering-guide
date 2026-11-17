# 5.5 Internacionalização e localização

## Visão geral e motivação

A [internacionalização](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) é o trabalho de engenharia de construir software para que possa ser adaptado a qualquer idioma, região e cultura sem mudar o código. A localização (l10n) é o trabalho que vem depois: adaptar de fato um produto para uma localidade específica, traduzindo o texto, formatando datas e números, ajustando o layout e levando em conta expectativas culturais. As duas são distintas. A internacionalização é feita uma vez, na arquitetura. A localização é feita muitas vezes, no conteúdo. Acertem a arquitetura logo no início e toda localização é barata. Errem e cada uma vira uma adaptação dolorosa e propensa a erros.

Para grandes equipes, a i18n é uma decisão arquitetural fundamental. Ela toca todas as camadas: armazenamento de dados, tratamento de cadeias de texto, layout e pipelines de conteúdo. Se vocês não a estabelecem cedo e não a impõem por bibliotecas compartilhadas e regras de lint, as equipes fixam cadeias em inglês no código, concatenam fragmentos traduzidos e presumem alfabetos latinos. Essa dívida precisa ser desfeita antes de o produto entrar em qualquer mercado novo. Um framework de i18n compartilhado e um fluxo de localização permitem a dezenas de equipes entregar um produto em muitos idiomas sem que cada uma reinvente a tubulação.

A relevância para empresas e governo é direta. As empresas multinacionais precisam atender clientes e funcionários entre países, idiomas e regimes regulatórios. Os governos precisam atender populações linguisticamente diversas. Muitos países são oficialmente multilíngues e muitos são legalmente obrigados a prestar serviços em vários idiomas, inclusive escritas da [direita para a esquerda](https://en.wikipedia.org/wiki/Bidirectional_text) e línguas indígenas ou minoritárias. Para os serviços públicos, o acesso linguístico é uma questão de equidade e legal: um cidadão que não consegue ler o único idioma disponível está efetivamente com o serviço negado.

## Princípios fundamentais

- Internacionalizem a arquitetura uma vez. Localizem o conteúdo muitas vezes.
- Nunca fixem no código o texto voltado ao usuário. Externalizem todas as cadeias em recursos gerenciados.
- Usem o [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) em toda parte. Presumam que o texto pode estar em qualquer escrita.
- Nunca concatenem fragmentos traduzidos. A gramática e a ordem das palavras diferem por idioma.
- Planejem a expansão do texto, as escritas da direita para a esquerda e as regras complexas de plural e de gênero.
- Formatem datas, números, moedas e nomes segundo a localidade, não segundo o código.
- Separem o conteúdo traduzível do código para que os tradutores nunca toquem o código-fonte.
- A localização é cultural, não apenas linguística: cores, imagens e exemplos importam.

## Recomendações

### Construa uma arquitetura sólida de internacionalização

Guardem e processem todo o texto como Unicode (UTF-8) de ponta a ponta (banco de dados, APIs e UI) para que qualquer escrita seja representável. Externalizem toda cadeia voltada ao usuário em arquivos de recursos ou num catálogo de mensagens com chave por identificador, nunca embutida no código ou na marcação. Representem uma localidade como idioma mais região (e escrita onde preciso) para poder distinguir, por exemplo, as variantes de um idioma entre países. Mantenham a lógica de formatação numa biblioteca de internacionalização bem testada em vez de fazer à mão a formatação de datas, números e moedas. Guardem os dados em formas neutras e inequívocas (carimbos de data e hora em UTC, códigos ISO de país e de moeda, unidades-base) e formatem só na camada de apresentação.

### Trate corretamente a complexidade dos idiomas

Não presumam o comprimento do texto. Deixem muito espaço, porque as traduções costumam ser bem mais longas que o inglês, e projetem layouts que se reacomodam em vez de truncar ou se sobrepor. Suportem as escritas bidirecionais (da direita para a esquerda) usando propriedades de layout lógicas e não físicas e espelhando a interface onde apropriado. Usem as regras de plural da localidade por meio da sua biblioteca de i18n (os idiomas têm de uma a seis formas de plural) em vez de uma lógica ingênua de singular/plural. Tratem o gênero e a concordância gramatical onde o idioma exige. Nunca montem frases por concatenação. Usem modelos de mensagem completos e parametrizados para que os tradutores controlem a ordem das palavras.

### Estabeleça um fluxo de localização e a gestão de traduções

Tratem a localização como um pipeline contínuo, não um lote pré-lançamento. Extraiam as cadeias automaticamente, enviem-nas a um [sistema de gerenciamento de traduções](https://en.wikipedia.org/wiki/Translation_management_system) e puxem de volta as traduções prontas, idealmente integrado ao CI, de modo que as novas cadeias sejam sinalizadas e as versões localizadas permaneçam em sincronia. Deem contexto aos tradutores: capturas de tela, descrições, limites de caracteres e um glossário e guia de estilo por idioma para manter a terminologia e o tom consistentes. Usem a [memória de tradução](https://en.wikipedia.org/wiki/Translation_memory) para reaproveitar trabalho anterior e cortar custo. Decidam deliberadamente onde a [tradução automática](https://en.wikipedia.org/wiki/Machine_translation) é aceitável (conteúdo de baixo risco e alto volume) e onde são exigidas tradução e revisão humanas (jurídico, médico, segurança, crítico para a marca). Façam a [pseudolocalização](https://en.wikipedia.org/wiki/Pseudolocalization) cedo, substituindo as cadeias por marcadores alongados e acentuados, para pegar cadeias fixas no código, truncamentos e bugs de codificação antes de a tradução real começar.

### Localize formatos, cultura e conteúdo, não apenas palavras

Formatem datas, horas, números, moedas, endereços, telefones e nomes por localidade, respeitando as convenções locais (ordem da data, separadores decimais e de milhar, posição da moeda, ordem do nome). Adaptem imagens, ícones, cores, exemplos e metáforas ao significado cultural local, já que símbolos e cores carregam conotações diferentes entre culturas. Levem em conta as diferenças locais de conteúdo jurídico e regulatório. Distingam a consistência global (marca, funcionalidade central) da adaptação regional (conteúdo, exemplos, conformidade) e decidam explicitamente quais elementos são fixos e quais flexionam.

### Governe a i18n como infraestrutura compartilhada

Forneçam uma biblioteca compartilhada de i18n, regras de lint de externalização de cadeias e um mecanismo padrão de resolução de localidade para que as equipes não consigam fixar texto no código por acidente. Estabeleçam a propriedade do pipeline de localização e dos glossários. Testem em várias localidades no CI, incluindo uma localidade da direita para a esquerda e uma pseudolocalidade de texto longo, para que as regressões sejam pegas automaticamente.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Internacionalizar desde o primeiro dia | Entrada barata em mercados depois, sem adaptação | Custo inicial mesmo antes de uma segunda localidade ser necessária |
| Adaptar a i18n depois | Adia o custo se a necessidade global é incerta | Muito caro e arriscado desfazer suposições fixas no código |
| Tradução humana | Alta qualidade, culturalmente exata | Mais lenta e mais cara |
| Tradução automática | Rápida, barata, escala para volumes enormes | Risco de qualidade e de exatidão. Inadequada para conteúdo de alto risco |
| Pipeline contínuo de localização | As localidades permanecem em sincronia, sem correria de lançamento | Investimento em ferramentas e processo |
| Adaptação cultural profunda por região | Melhor ajuste e confiança locais | Mais variantes de conteúdo para construir e manter |

A troca decisiva é quando investir na internacionalização. Adaptar a i18n num produto cheio de código fixo, concatenado e que presume o alfabeto latino é uma das formas mais caras de dívida técnica a quitar. Para qualquer organização com ambições internacionais ou multilíngues plausíveis, o que inclui essencialmente todas as grandes empresas e os governos multilíngues, internacionalizar a arquitetura cedo é muito mais barato que adaptar, embora o ganho seja adiado.

## Perguntas para discutir com sua equipe

1. **Impomos a externalização de cadeias com regras de lint, e a pseudolocalização roda no CI antes de qualquer tradução real?** A dívida que torna cara a internacionalização (cadeias em inglês fixas no código, fragmentos de frase concatenados, suposições de alfabeto latino) se acumula em silêncio a menos que as ferramentas a impeçam na hora do commit. Regras de lint que sinalizam texto de usuário fixo no código, mais uma pseudolocalidade acentuada de texto longo rodada no CI, pegam truncamento, sobreposição e bugs de codificação enquanto são baratos de corrigir. É isso que permite a dezenas de equipes entregar um produto em muitos idiomas sem que cada uma reinvente a tubulação ou desfaça suposições sob prazo depois. Levem uma busca por cadeias fixas no código e perguntem se alguma equipe poderia entregar uma por acidente hoje. Se nada no pipeline a pegaria, essa é a lacuna a fechar primeiro.

2. **Onde guardamos os dados canônicos, e a formatação fica confinada à camada de apresentação?** Guardar carimbos de data e hora em UTC, países e moedas como códigos ISO e valores em unidades-base significa que qualquer localidade pode formatá-los corretamente na borda, enquanto a lógica de formatação embutida na camada de dados produz bugs dolorosos de desfazer. Combinem que datas, números, moedas, endereços e nomes são formatados apenas na apresentação, por uma biblioteca bem testada e não por código feito à mão. Isso importa para empresas multinacionais e governos multilíngues, onde um cidadão precisa ver a ordem de data, os separadores decimais e a ordem de nomes corretos na própria convenção. Levem um exemplo de um valor que o seu sistema guarda já formatado e rastreiem o que quebra quando uma nova localidade o precisa de outro jeito. Se dados e apresentação estão emaranhados, decidam como desemaranhá-los antes de acrescentar localidades.

3. **Onde exatamente a tradução automática é aceitável, e como o nosso pipeline de localização é mantido contínuo e não em lote?** A tradução automática é rápida e barata para conteúdo de baixo risco e alto volume, mas inadequada para texto jurídico, médico, de segurança ou crítico para a marca, em que uma tradução errada causa dano real, então a fronteira precisa ser uma política explícita e não um palpite por equipe. Igualmente, tratar a localização como um lote pré-lançamento garante uma correria de tradução, enquanto extrair cadeias automaticamente e sincronizar por um sistema de gerenciamento de traduções mantém toda localidade atual. Decidam quem é dono do pipeline, dos glossários e do portão de revisão humana para as cadeias de alto risco. Levem um lançamento recente e perguntem quanto tempo suas novas cadeias levaram para aparecer em todos os idiomas. Se as localidades se afastam entre lançamentos, o seu pipeline é um lote disfarçado.

4. **Testamos automaticamente uma localidade da direita para a esquerda e uma pseudolocalidade de texto longo, ou presumimos em silêncio alfabetos latinos e layouts do comprimento do inglês?** O suporte bidirecional (da direita para a esquerda) e a expansão do texto são as suposições que quebram de modo mais visível num mercado novo: interfaces espelhadas que nunca foram espelhadas e botões que truncam quando o alemão ou o finlandês correm quarenta por cento mais longos que o inglês. A atração concorrente é a velocidade, já que construir sobre propriedades lógicas de layout e não físicas e ligar uma pseudolocalidade acentuada à integração contínua (CI) custa esforço antes de qualquer cliente real precisar. Levem uma captura de tela das suas telas mais movimentadas renderizadas numa localidade da direita para a esquerda e numa pseudolocalidade alongada e contem as sobreposições, os rótulos cortados e as setas presas. Para uma multinacional ou um governo legalmente obrigado a servir uma língua da direita para a esquerda ou minoritária, um layout que não consegue espelhar não é um defeito cosmético, é um mercado ou uma obrigação estatutária que vocês não conseguem cumprir sem uma reconstrução.

5. **Quais partes do produto são globalmente fixas e quais flexionam por região, e quem tem autoridade para decidir?** A localização é cultural e não meramente linguística, então cores, imagens, exemplos, formas de tratamento e até quais funcionalidades são oferecidas podem diferir por mercado, e ainda assim cada variante regional que vocês permitem é mais um artefato a construir, traduzir, revisar e manter para sempre. A tensão é entre o ajuste local, que constrói confiança e conversão, e a consistência, que mantém a marca coerente e o ônus de manutenção limitado. Levem uma lista concreta do que uma nova localidade proposta mudaria além das cadeias traduzidas e precifiquem a manutenção contínua de cada variante, e não só a primeira construção. Numa grande empresa essa decisão precisa de um dono nomeado para que as equipes regionais não criem forks do produto ad hoc, e no governo precisa respeitar regras jurídicas e de acessibilidade de conteúdo que variam por jurisdição e não são opcionais.

6. **A quais localidades de fato nos comprometemos, como mantemos a terminologia consistente entre elas e que evidência conduz essa lista?** Acrescentar um idioma é fácil de prometer e caro de sustentar, porque cada um precisa de um glossário, um guia de estilo, revisão humana para cadeias de alto risco e tratamento correto de plural e de gênero, que uma lógica ingênua de singular ou plural erra na maioria dos idiomas. As considerações concorrentes são alcance contra custo: um mercado ou população servida mal pode ser pior que um não servido. Levem a população ou a receita por trás de cada localidade candidata, a cobertura de regras de plural e de formatação que a sua biblioteca oferece para ela e quem é dono do glossário. Para uma multinacional o motor é o mercado endereçável e o custo de suporte por idioma, enquanto para o governo é a obrigação legal de acesso linguístico e a equidade, quantificadas pelo número de residentes que só conseguem transacionar naquele idioma.

## Perspectiva por setor

**Startup.** Façam as escolhas arquiteturais baratas no primeiro dia e parem aí: UTF-8 de ponta a ponta, toda cadeia voltada ao usuário num catálogo de mensagens e datas, números e moedas formatados por uma biblioteca que reconhece a localidade. Isso custa quase nada enquanto vocês entregam em um idioma e poupa uma reescrita quando o primeiro grande cliente quiser um segundo. Não levantem um pipeline de tradução nem suportem localidades que ninguém ainda está pagando. Mantenham a porta aberta, não a casa inteira mobiliada.

**Pequena empresa.** Sem especialista em internacionalização e com orçamento apertado, apoiem-se nos recursos de i18n já presentes no seu framework e num serviço hospedado de gerenciamento de traduções em vez de construir pipelines vocês mesmos. Usem a tradução automática para conteúdo de baixo risco e alto volume e paguem tradução humana apenas onde um erro custaria um cliente ou violaria uma regra, como texto jurídico, de segurança ou de cobrança. Comprometam-se com uma localidade só quando um mercado específico claramente justificar o custo contínuo de tradução e revisão.

**Grande empresa.** O problema é a governança entre muitas equipes: uma biblioteca compartilhada de i18n, regras de lint que rejeitam cadeias fixas no código, um pipeline contínuo de localização com memória de tradução e glossários por idioma e CI com várias localidades que inclua uma da direita para a esquerda e uma pseudolocalidade de texto longo. Conduzam a localização como infraestrutura compartilhada com um dono claro para que os grupos parem de reinventar a tubulação ou de se afastar em sincronia. Meçam a cobertura de idiomas, a qualidade da localização e o tempo para lançar uma nova localidade e gerenciem o portfólio de localidades por esses números em vez de lançar mercados ad hoc.

**Governo.** O acesso linguístico costuma ser uma obrigação legal, cobrindo idiomas oficiais, escritas da direita para a esquerda e línguas indígenas ou minoritárias, então a transparência e a equidade moldam toda escolha. Construam um framework compartilhado de i18n e um fluxo de tradução entre as agências, exijam revisão humana para a terminologia jurídica e de segurança e publiquem glossários para que os termos permaneçam consistentes entre os serviços. A contratação deve exigir nos contratos suporte a localidades, a escritas da direita para a esquerda e à acessibilidade, e a população atendida em cada idioma é a métrica que justifica o gasto perante o público.

## Exemplos

**Startup.** Uma pequena startup que entregava só em inglês ainda assim fez algumas escolhas arquiteturais baratas no primeiro dia: UTF-8 em toda parte, toda cadeia voltada ao usuário puxada para um catálogo de mensagens em vez de fixa no código e datas e moedas formatadas por uma biblioteca que reconhece a localidade. Custou quase nada enquanto tinham um idioma. Um ano depois, quando o maior prospecto pediu uma versão em francês e alemão, acrescentar essas localidades foi sobretudo um exercício de tradução entregue a um contratado e não uma reescrita, e eles fecharam o negócio em semanas em vez de adiá-lo por um trimestre de trabalho de engenharia.

**Grande empresa.** Uma empresa global de comércio eletrônico internacionalizou a plataforma cedo: UTF-8 em toda parte, cadeias externalizadas, uma biblioteca de formatação que reconhece a localidade e um pipeline contínuo de localização com memória de tradução e glossários por idioma. Entrar num novo mercado virou em grande parte um exercício de conteúdo (traduzir, revisar, ajustar imagens) e não um projeto de engenharia, permitindo à empresa lançar em novas localidades em semanas. O suporte da direita para a esquerda construído sobre propriedades lógicas de layout significou que os mercados árabe e hebraico exigiram pouco trabalho novo de UI.

**Governo.** Um governo nacional legalmente obrigado a prestar serviços em vários idiomas oficiais, incluindo uma escrita da direita para a esquerda e línguas minoritárias, construiu um framework compartilhado de i18n e um fluxo de tradução usados por todas as agências. A pseudolocalização no CI pegou cadeias fixas no código e truncamentos antes do lançamento. Um glossário compartilhado manteve consistente a terminologia jurídica entre serviços e idiomas. Os cidadãos conseguem completar transações de impostos, saúde e benefícios no próprio idioma, com formatação correta de data, número e nome, satisfazendo a lei de acesso linguístico e melhorando a equidade para falantes de idiomas não majoritários.

## Justificativa de negócio: motivações, ROI e TCO

O ROI da internacionalização é acesso a mercados e velocidade. Um produto bem internacionalizado pode entrar em novos países e mercados linguísticos depressa e barato, transformando cada nova localidade em receita incremental ou alcance de cidadãos e não num grande projeto. A qualidade da localização conduz a conversão, a confiança e o custo de suporte em cada mercado: os usuários transacionam mais e contatam menos o suporte quando o produto fala corretamente o idioma deles e respeita suas convenções.

No TCO, o custo de adoção é a engenharia inicial para internacionalizar, mais os custos contínuos de tradução e de pipeline. O custo de não adotar é a adaptação cara: desfazer cadeias fixas no código, concatenação, bugs de codificação e suposições de layout em toda uma base de código, muitas vezes sob um prazo conduzido por um mercado ou uma exigência legal. A localização ruim também carrega custos ocultos: vendas perdidas em mercados mal servidos, ônus de suporte por formatos confusos e dano jurídico ou de reputação por conteúdo de alto risco mal traduzido. A localização contínua evita caras correrias de tradução pré-lançamento.

Para defender o caso junto à liderança, enquadrem a internacionalização como uma opção sobre mercados futuros. É um investimento inicial modesto que reduz drasticamente o custo e o tempo de toda futura entrada em mercados. Para o governo, o motor é a obrigação legal de acesso linguístico e a equidade, quantificadas pela população atendida em cada idioma.

## Antipadrões e armadilhas

- **Cadeias fixas no código**: texto de usuário embutido no código, forçando mudanças de código por localidade.
- **Concatenação de cadeias**: montar frases a partir de fragmentos, o que quebra a gramática e a ordem das palavras.
- **Suposições não Unicode**: bugs de codificação, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (texto ilegível por codificações de caracteres descasadas) e incapacidade de representar escritas.
- **Presumir o comprimento do texto em inglês**: layouts que truncam ou se sobrepõem quando traduzidos.
- **Ignorar a direita para a esquerda**: usar layout físico de esquerda/direita que não consegue espelhar.
- **Pluralização ingênua**: lógica de singular/plural que está errada na maioria dos idiomas.
- **Formatação cega à localidade**: formatos de data, número e moeda fixos no código.
- **Traduzir sem contexto**: tradutores adivinhando o significado e produzindo erros.
- **Localização em lote, de última hora**: uma correria pré-lançamento em vez de um pipeline contínuo.
- **Insensibilidade cultural**: imagens, cores ou exemplos que ofendem ou confundem localmente.

## Modelo de maturidade

**Nível 1: Iniciar.** Um único idioma, cadeias fixas no código, suposições não Unicode e texto montado por concatenação. A internacionalização é reativa: qualquer nova localidade significa mudar código, e os bugs de codificação e de layout são achados por acaso em produção.

**Nível 2: Desenvolver.** Algumas cadeias são externalizadas e o Unicode é usado em alguns lugares, mas a prática é inconsistente entre as equipes. A localização é um esforço manual, em lote, pré-lançamento, e a formatação, o tratamento de plurais e o suporte à direita para a esquerda são tratados de forma diferente (ou nem tratados) de uma equipe para outra.

**Nível 3: Padronizar.** Uma arquitetura compartilhada de i18n e uma biblioteca de formatação que reconhece a localidade são o padrão documentado e imposto em toda a organização. A externalização de cadeias é verificada por regras de lint, um sistema de gerenciamento de traduções e um pipeline contínuo estão no lugar, com glossários e memória de tradução, e a pseudolocalização mais os testes em várias localidades (incluindo uma da direita para a esquerda e uma de texto longo) rodam no CI.

**Nível 4: Gerenciar.** O programa de localização é medido e controlado em relação a linhas de base. As equipes acompanham a cobertura de idiomas, a qualidade da localização e as taxas de defeitos, a latência de sincronização de cadeias do commit ao lançamento traduzido, os defeitos de truncamento e de renderização da direita para a esquerda pegos por lançamento, o custo de tradução por localidade e o tempo para lançar uma nova localidade, e essas métricas condicionam lançamentos e conduzem onde investir revisão humana versus tradução automática.

**Nível 5: Orquestrar.** A internacionalização e a localização são continuamente melhoradas e integradas em toda a organização. A localização é contínua, a tradução automática e a humana são escolhidas deliberadamente por classe de conteúdo e a adaptação cultural é sistemática. A organização acrescenta, aposenta e redimensiona localidades em resposta a evidências de mercado e de equidade, e as novas localidades são lançadas rapidamente e com alta qualidade, sem adaptação.

## Ideias para discussão

- Com que antecedência um produto deve se internacionalizar se a demanda internacional é incerta?
- Onde a tradução automática é aceitável, e onde humanos precisam revisar?
- Como vocês mantêm a terminologia consistente entre muitos idiomas e equipes?
- Quanta adaptação cultural regional vale a manutenção adicional de variantes?
- Como o suporte à direita para a esquerda e a idiomas minoritários deve ser priorizado e testado?
- Como vocês dão aos tradutores contexto suficiente sem desacelerar o pipeline?

## Principais conclusões

- Internacionalizem a arquitetura uma vez. Localizem o conteúdo muitas vezes.
- Usem o Unicode em toda parte, externalizem todas as cadeias e nunca concatenem traduções.
- Planejem a expansão do texto, as escritas da direita para a esquerda e as regras de plural e de formatação específicas de cada localidade.
- Conduzam um pipeline contínuo de localização com memória de tradução, glossários e contexto.
- Pseudolocalizem cedo no CI para pegar bugs de i18n antes da tradução real.
- A localização é cultural, não apenas linguística.
- Internacionalizar cedo é muito mais barato que adaptar. Para o governo, é uma exigência legal de equidade.

## Referências e leitura complementar

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
