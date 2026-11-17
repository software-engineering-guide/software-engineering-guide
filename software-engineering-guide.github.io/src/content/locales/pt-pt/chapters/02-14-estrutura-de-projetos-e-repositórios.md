# 2.14 Estrutura de projetos e repositórios

## Visão geral e motivação

A estrutura de projetos e repositórios é a organização física de uma base de código: as pastas, os arquivos e as convenções de nomenclatura que decidem onde cada coisa mora. Um *repositório* (muitas vezes abreviado para “repo”) é o contêiner [versionado](https://en.wikipedia.org/wiki/Version_control) que guarda os arquivos de um projeto e o seu histórico. Um *projeto*, às vezes chamado de *solução* quando agrupa vários componentes relacionados, é a unidade lógica de software que você está construindo. A estrutura é o mapa que você usa para encontrar, entender e alterar esse software.

Numa equipe pequena, uma pessoa consegue guardar toda a organização na cabeça. Numa equipe grande, com centenas ou milhares de engenheiros, mudanças frequentes entre equipes e terceirizados que entram e saem, cada repositório organizado de forma diferente cobra um novo imposto cognitivo. Quando você abre um repositório desconhecido, deve conseguir adivinhar onde moram o código-fonte, os testes, a documentação e a configuração de implantação sem ler um manual. Quando todos os repositórios respondem a essas perguntas do mesmo jeito, a mobilidade é barata e a integração é rápida. Quando cada repositório é um caso único, cada troca de contexto vira um pequeno projeto de pesquisa.

Em contextos corporativos e governamentais, a estrutura consistente é também uma preocupação de controle e de garantia. Auditores, revisores de segurança e mantenedores de longo prazo, muitas vezes trabalhando anos depois de os autores originais terem ido embora, precisam localizar com confiabilidade documentos de especificação, arquivos de licença, políticas de segurança e definições de build. Uma organização previsível também permite que as ferramentas automatizadas (escâneres, analisadores de dependências, verificações de conformidade) funcionem da mesma forma em todo um portfólio de sistemas. Por isso este capítulo trata a estrutura como uma convenção que você decide uma vez e aplica em toda parte. Ela está intimamente ligada aos padrões de codificação e estilo (capítulo 2.1), ao controle de versões e à gestão de código-fonte (capítulo 2.6) e à documentação (capítulo 2.7).

## Princípios fundamentais

- Siga o *[princípio da menor surpresa](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: a organização deve corresponder ao que um engenheiro experiente esperaria, para que nada precise ser decorado.
- A consistência entre repositórios vence a esperteza local. Uma estrutura uniforme o bastante em toda parte vale mais que a estrutura perfeita num só lugar.
- O [README](https://en.wikipedia.org/wiki/README) é a porta de entrada. Uma pessoa recém-chegada deve conseguir se orientar só por ele.
- Torne a estrutura autodescritiva pela nomenclatura, para que pastas e arquivos anunciem seu propósito.
- Imponha a estrutura com esqueletos e modelos, não com força de vontade e comentários de revisão.
- Separe as responsabilidades fisicamente: código-fonte, testes, documentação, build e implantação pertencem a lugares distintos e previsíveis.
- Organize as dependências para que fluam numa só direção, dos núcleos estáveis para as bordas voláteis.

## Recomendações

### Adote uma organização consistente de nível superior

Defina um conjunto padrão de pastas de nível superior que todo repositório usa quando aplicável e documente para que serve cada uma. Uma convenção comum e neutra quanto a fornecedores inclui: uma pasta de código-fonte (muitas vezes `src`) para o código de produção, uma pasta de testes (muitas vezes `test` ou `tests`) para os testes automatizados, uma pasta `docs` para a documentação, uma pasta `build` para definições e saídas de build, uma pasta `deploy` para a implantação e a *[infraestrutura como código](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (definições legíveis por máquina de servidores, redes e serviços, tratadas no capítulo 8.2), uma pasta `scripts` para automação e ferramentas do desenvolvedor, uma pasta `examples` para amostras executáveis e uma pasta `spec` ou `specification` para requisitos e especificações de design. Nem todo repositório precisa de toda pasta, mas onde uma preocupação existe, ela deve morar no lugar esperado com o nome esperado.

### Faça do README o ponto de entrada

Exija um arquivo README na raiz do repositório como o ponto de partida único e canônico. Ele deve declarar o que é o projeto, como construí-lo e executá-lo, como rodar os testes, onde achar documentação mais profunda, quem é o responsável e como contribuir. O README não é o conjunto inteiro da documentação: é o índice que aponta para o resto (capítulo 2.7). Trate um README ausente ou obsoleto como um defeito, porque é a primeira coisa que toda pessoa engenheira nova, auditora ou integradora lerá.

### Padronize os arquivos de editor e de configuração

Faça o commit da configuração compartilhada de editor e de ferramentas no repositório para que todo contribuidor receba um comportamento consistente automaticamente. Um arquivo `.editorconfig` (um arquivo simples e independente de editor que define regras de espaços em branco, indentação e fim de linha) mantém a formatação básica uniforme entre editores e sistemas operacionais diferentes. Acrescente um arquivo de ignorar para o sistema de controle de versões (para que saídas de build e artefatos locais nunca sejam commitados), junto com as configurações compartilhadas de formatador e linter descritas no capítulo 2.1. Esses arquivos tornam ativas as convenções do repositório, e não apenas documentadas.

### Defina convenções de nomenclatura e de pastas

Combine convenções para nomear pastas e arquivos (capitalização, separadores, singular versus plural e sufixos exigidos, como os que marcam testes) e aplique-as de modo uniforme. Os nomes devem revelar a intenção e corresponder ao vocabulário de domínio usado em outros lugares da organização. O objetivo é simples: um caminho deve comunicar significado, de modo que ler o nome de uma pasta ou arquivo diga o que há dentro sem abri-lo.

### Organize camadas e dependências deliberadamente

Estruture a base de código de modo que suas camadas arquiteturais apareçam na organização das pastas e que as dependências fluam numa só direção sensata. A política de nível mais alto não deve depender de detalhes de baixo nível. O código compartilhado e estável deve ficar onde muitos módulos possam alcançá-lo sem criar ciclos. Quando você torna a divisão em camadas física, refletida na árvore de diretórios, os engenheiros têm mais probabilidade de respeitá-la, e as violações ficam mais fáceis de perceber na revisão e em verificações automatizadas de dependências.

### Imponha a estrutura com esqueletos e modelos

Forneça *[esqueletos](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)* (scaffolding), a geração automatizada de um projeto inicial, para que os novos repositórios já comecem corretos. Um *modelo* ou *cookiecutter* (um esqueleto parametrizado de projeto que gera um repositório pronto a partir das respostas a algumas perguntas) codifica num só lugar a organização padrão, o README, os arquivos de configuração e a configuração de [CI](https://en.wikipedia.org/wiki/Continuous_integration). Quando os engenheiros criam novos serviços a partir de um modelo compartilhado, a consistência se torna o padrão em vez de uma aspiração, e as melhorias no modelo chegam aos projetos futuros.

### Mantenha a estrutura consistente entre muitos repositórios em escala

Trate a própria organização como um padrão governado: mantido centralmente como qualquer outro padrão de engenharia (capítulo 1.7) e versionado como código (capítulo 2.6). Publique-a, forneça os modelos que a implementam e permita desvios apenas por um processo documentado de exceção, para que “o padrão” mantenha seu significado. Em escala de portfólio, quase todo o valor da estrutura vem de sua uniformidade entre repositórios, então a deriva é o principal risco a gerenciar.

### Deixe a estrutura informar a escolha entre monorrepositório e vários repositórios

Relacione a estrutura à decisão sobre as fronteiras de repositório tratada no capítulo 2.6. Um *[monorrepositório](https://en.wikipedia.org/wiki/Monorepo)* (um repositório que abriga muitos projetos) precisa de uma convenção interna clara para separar os projetos e o código compartilhado deles, para que a árvore única continue navegável. Uma abordagem de *vários repositórios* (muitos repositórios pequenos, um por projeto ou serviço) precisa de forte consistência entre repositórios, para que cada um pareça familiar mesmo sendo independente. De um jeito ou de outro, uma estrutura documentada e baseada em modelos é o que mantém a navegação previsível. A escolha da fronteira muda onde você aplica a convenção, não se você precisa de uma.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| Organização padrão estrita para toda a organização | Familiaridade instantânea. Engenheiros portáveis. Ferramentas uniformes | Encaixe ocasionalmente ruim em projetos incomuns. Exige governança |
| Liberdade de organização por equipe | Otimização local. Alta autonomia | Fragmentação. Troca de contexto cara. Ferramentas inconsistentes |
| Esqueletos e modelos | Repositórios corretos por padrão. As mudanças se propagam | Manutenção do modelo. Risco de deriva dos repositórios gerados |
| Hierarquia de pastas profunda e em camadas | Estrutura explícita. Fronteiras claras | Custo de navegação. Caminhos longos. Risco de superengenharia |
| Organização plana e rasa | Fácil de percorrer com os olhos. Pouca cerimônia | Má separação. Deixa de servir à medida que o projeto cresce |

O compromisso dominante é uniformidade versus autonomia. Uma única organização padrão remove o atrito para os muitos engenheiros que transitam entre bases de código, ao custo do projeto ocasional cujas necessidades não cabem direito no molde. Numa grande organização, o ganho coletivo da familiaridade quase sempre supera essa perda local. Por isso a postura recomendada é um forte padrão por omissão mais um caminho documentado de exceção (capítulo 1.7), em vez de uniformidade rígida ou liberdade sem gestão. Um compromisso secundário é profundidade versus simplicidade: estrutura suficiente para separar preocupações reais, mas não tanta que a navegação vire uma caminhada por pastas vazias.

## Perguntas para discutir com sua equipe

1. **Quando um engenheiro se muda para um repositório nosso que não conhece, quanto tempo leva até encontrar os testes, a configuração de implantação e o responsável?** Este é o imposto de navegação que a estrutura existe para eliminar, e em escala de portfólio ele é pago milhares de vezes por ano em pequenas parcelas que somam um sério tempo de engenharia perdido. O sentido do princípio da menor surpresa é que um engenheiro experiente deve conseguir adivinhar onde moram o código-fonte, os testes, a documentação e a implantação sem ler um manual, então o teste honesto é se esse palpite acerta nos seus repositórios. Leve um número real à reunião: cronometrem-se orientando-se em dois ou três repositórios internos desconhecidos, ou levantem os dados de integração sobre quanto tempo as pessoas novas levam para fazer a primeira mudança. Se a resposta é medida em dias de pesquisa em vez de minutos de reconhecimento, vocês quantificaram o custo dos repositórios únicos, e isso justifica o investimento pontual numa organização padrão que todo repositório compartilhe.

2. **As nossas camadas arquiteturais aparecem na árvore de pastas, ou os ciclos de dependência se escondem dentro de uma organização plana?** A estrutura é sobre mais que a capacidade de localização: quando você torna a divisão em camadas física, os engenheiros a respeitam e os revisores e as verificações automatizadas de dependências conseguem perceber as violações, enquanto uma pilha plana deixa o acoplamento indevido e os ciclos se infiltrarem sem ser notados até a mudança ficar perigosa. Num sistema grande e de longa vida é isso que impede a política de nível mais alto de depender em silêncio de detalhes de baixo nível, e é exatamente o tipo de erosão que é barata de prevenir e cara de desfazer. Leve o seu grafo de dependências ou rode uma verificação rápida: há ciclos, e algo estável depende de algo volátil? A resposta deve empurrar vocês a refletir as camadas nos diretórios e a acrescentar verificações automatizadas da direção das dependências, para que as fronteiras sejam visíveis na árvore e impostas no pipeline em vez de viverem só no modelo mental de alguém.

3. **Nossos novos repositórios começam corretos a partir de um modelo, ou dependemos de uma página de wiki e de boas intenções?** A estrutura imposta por esqueleto é o padrão. A estrutura descrita num documento deriva, porque a realidade segue o que gera os repositórios, não o que uma página diz que eles deveriam ser. Para uma organização grande ou regulamentada isso é também uma preocupação de garantia: quando todo repositório é gerado a partir de um modelo compartilhado, os escâneres de segurança, os analisadores de dependências e os auditores encontram a licença, a política de segurança, a especificação e a definição de build no mesmo lugar todas as vezes, entre fornecedores e ao longo dos anos. Leve as evidências: quantos dos seus repositórios recentes foram gerados a partir do modelo padrão versus montados à mão, e o quanto os gerados por modelo já derivaram desde então? A ação é fazer do modelo o único jeito fácil de iniciar um repositório, governá-lo como um padrão versionado com um caminho documentado de exceção e detectar a deriva automaticamente, porque a uniformidade é onde mora quase todo o valor da estrutura.

4. **Decidimos se o nosso padrão abrange um monorrepositório ou muitos repositórios separados, e a mesma convenção de fato vale dos dois lados dessa fronteira?** A escolha da fronteira de repositório muda onde você aplica a convenção, não se você precisa de uma, e errar significa uma árvore gigante que ninguém consegue navegar ou uma proliferação de repositórios que parecem, cada um, estranhos. Um monorrepositório precisa de uma convenção interna clara para separar os projetos e o código compartilhado deles, para que a única árvore continue navegável, enquanto uma abordagem de vários repositórios precisa de forte consistência entre repositórios, para que cada repositório independente ainda pareça familiar. Leve o inventário atual: quantos repositórios vocês têm, como o código compartilhado é separado dentro de qualquer monorrepositório e um teste cronometrado de se um engenheiro encontra um projeto dentro da árvore grande tão rápido quanto encontra um num repositório independente. Para uma grande empresa ou programa governamental em que fornecedores diferentes entregam repositórios separados, decidam deliberadamente quais partes da convenção são universais e quais são específicas da fronteira, porque auditores e ferramentas de plataforma precisam funcionar da mesma forma quer o código chegue como uma árvore ou como cinquenta.

5. **Quem é o responsável pelo nosso padrão de estrutura, e o que realmente acontece quando um projeto genuinamente não se encaixa nele?** Em escala de portfólio, quase todo o valor da estrutura vem da uniformidade, então os riscos reais são um padrão sem responsável que apodrece e um caminho de exceção tão vago que toda equipe inventa em silêncio a própria organização. A tensão é entre uma uniformidade rígida que não serve a nenhum projeto incomum e uma liberdade sem gestão que fragmenta tudo, e a resposta saudável é um forte padrão por omissão mais um processo de exceção documentado e auditável, governado por um responsável nomeado e versionado como código. Leve as evidências: existe um único responsável, um documento de padrão versionado com registro de mudanças, um registro das exceções concedidas e por quê e uma contagem de desvios não documentados que vocês encontram por aí? Em contextos corporativos e governamentais, uma exceção que ninguém registrou é uma lacuna de controle, então ligue cada desvio a uma justificativa escrita e a uma data de revisão e garanta que os contratos de contratação que exigem a organização nomeiem também quem pode aprovar afastamentos dela.

6. **Nosso README e os arquivos de configuração versionados tornam ativas as nossas convenções, ou são decorativos?** O README é a porta de entrada, e o `.editorconfig`, o arquivo de ignorar e a configuração de linter versionados são o que torna as convenções autoimpostas, mas essas são as primeiras coisas a ficar obsoletas e as últimas que alguém nota até um auditor ou uma pessoa nova não conseguir fazer o projeto compilar. A tensão é entre um README enxuto que se mantém atual e um completo que deriva, e entre confiar que as pessoas formatem o código corretamente e deixar a configuração compartilhada impô-lo automaticamente. Leve uma amostra: pegue cinco repositórios e verifique quantos READMEs realmente declaram o que é o projeto, como construir, testar e executar e quem é o responsável, e quantos carregam os arquivos de configuração compartilhados em vez de depender de hábitos individuais. Para uma organização grande ou regulamentada, em que integradores, revisores de segurança e mantenedores de longo prazo leem o README antes de qualquer outra coisa, trate uma porta de entrada ausente ou obsoleta como um defeito com responsável e verifique automaticamente a presença dos arquivos de configuração para que a conformidade não dependa de boa vontade.

## Perspectiva por setor

**Startup.** A velocidade vence, então combine uma organização simples e plana o bastante para o seu primeiro repositório (src, test, docs, scripts, um README preenchido, um `.editorconfig` e arquivos de ignorar) e salve-a como um modelo leve na mesma tarde. Gere o segundo serviço a partir dele, para que os dois repositórios pareçam familiares e um terceirizado novo se integre em horas em vez de fazer engenharia reversa de um caso único. Resista a hierarquias profundas e a governança pesada de que você ainda não precisa. Todo o retorno aqui é que dois fundadores e um terceirizado compartilham um só mapa.

**Pequena empresa.** Sem especialista em plataforma e com orçamento apertado, adote a organização convencional que a sua linguagem ou framework já pressupõe em vez de inventar uma, para que as ferramentas prontas e qualquer pessoa nova cheguem já treinadas nela. Compre esqueletos (um gerador de framework ou um modelo cookiecutter) em vez de construir o seu e gaste o seu escasso esforço mantendo atual um README preenchido. Esse README é o seguro mais barato que você tem para o dia em que a única pessoa que conhecia a organização seguir adiante.

**Grande empresa.** Entre muitas equipes e centenas de repositórios, o objetivo é a uniformidade: publique um padrão de estrutura versionado, gere cada novo serviço a partir de modelos compartilhados, detecte a deriva automaticamente e permita desvios apenas por um processo documentado de exceção. Como todo repositório tem a mesma aparência, um engenheiro realocado para uma nova equipe fica produtivo em horas, e os escâneres de segurança e de dependências de todo o portfólio encontram a licença, a política de segurança e a definição de build no mesmo lugar todas as vezes. Orce explicitamente a manutenção dos modelos e a detecção de deriva, porque esse esforço é o que mantém o padrão significativo em escala.

**Governo.** A contratação, a transparência e a prestação de contas de longo prazo moldam a organização, então imponha uma estrutura comum nos padrões de entrega que vinculam todos os fornecedores. Exija uma pasta `specification` ligando o código aos requisitos aprovados, um arquivo de licença e de política de segurança na raiz e uma pasta `deploy` com as definições de infraestrutura como código, para que os auditores localizem os artefatos de conformidade do mesmo jeito em todos os sistemas. Como terceirizados de fornecedores diferentes seguem um só mapa, a manutenção depois do fim de um contrato custa muito menos, e o público ganha uma trilha defensável e inspecionável do requisito ao código em execução.

## Exemplos

**Startup.** Uma startup de três pessoas combina uma organização padrão simples para o seu primeiro repositório (src, test, docs, scripts, um README preenchido, um .editorconfig e arquivos de ignorar) e a salva como um modelo leve. Quando põem de pé o segundo serviço, um mês depois, geram-no a partir desse modelo, de modo que os dois repositórios já parecem familiares e o novo terceirizado se integra numa tarde. Resistem a hierarquias de pastas profundas de que ainda não precisam, mantendo a árvore plana o bastante para percorrer de relance. O custo foi uma tarde de preparação, e isso os poupa da proliferação de casos únicos que de outro modo faria de cada futuro repositório um pequeno projeto de pesquisa.

**Grande empresa.** Um varejista multinacional opera centenas de serviços em várias linguagens. Sua equipe de plataforma publica um padrão de estrutura de repositório versionado e um conjunto de modelos de projeto que o implementam. Todo novo serviço é gerado a partir de um modelo, de modo que chega com as pastas padrão `src`, `test`, `docs`, `deploy` e `scripts`, um README preenchido, um `.editorconfig`, arquivos de ignorar e um pipeline de CI funcionando. Como todo repositório tem a mesma aparência, um engenheiro realocado para uma nova equipe fica produtivo em horas, e os escâneres de segurança e de dependências de toda a organização rodam de modo uniforme porque sempre encontram os arquivos onde esperam.

**Governo.** Uma agência nacional que moderniza sistemas legados impõe uma organização comum de repositório como parte de seus padrões de entrega para todos os fornecedores. Cada repositório deve conter uma pasta `specification` ligando o código aos requisitos aprovados, um README documentado, um arquivo de licença e de política de segurança na raiz e uma pasta `deploy` com as definições de infraestrutura como código (capítulo 8.2). Como terceirizados de fornecedores diferentes seguem a mesma estrutura, os auditores da agência conseguem localizar os artefatos de conformidade do mesmo jeito em todos os sistemas, e a manutenção de longo prazo depois do fim de um contrato custa muito menos porque os mantenedores que chegam já conhecem o mapa.

## Justificativa de negócio: motivações, ROI e TCO

O custo de adotar um padrão de estrutura é em grande parte único: combinar a organização, construir os modelos e documentar a convenção. O custo recorrente é baixo, concentrado em manter os modelos e governar as exceções. O custo de *não* ter um padrão é recorrente e cumulativo: todo engenheiro que abre um repositório desconhecido paga um imposto de navegação, toda integração é mais lenta e as ferramentas automatizadas precisam ser configuradas por repositório porque nada está onde você espera. Numa grande organização, esses pequenos atritos se multiplicam em sérias perdas de tempo de engenharia.

O retorno aparece como integração mais rápida, mobilidade mais barata entre equipes, maior sinal das ferramentas de todo o portfólio e, em contextos regulamentados, menor custo de auditoria e de manutenção de longo prazo, porque os artefatos são sempre localizáveis. O *custo total de propriedade* (TCO, o custo do ciclo de vida inteiro de construir, operar e manter um sistema) cai mais em sistemas de longa vida, onde os mantenedores que se beneficiam de uma estrutura previsível geralmente não são os autores que a criaram. Para defender o caso junto à liderança, apresente a estrutura como um padrão de baixo custo e alta alavancagem que melhora a produtividade dos desenvolvedores e a prontidão para auditoria e ponha um número no custo atual da inconsistência usando dados de tempo de integração e o esforço gasto caçando coisas em repositórios desconhecidos.

## Antipadrões e armadilhas

- **O repositório caso único:** cada repositório organizado de um jeito, de modo que cada um precisa ser reaprendido do zero.
- **O README ausente ou obsoleto:** sem porta de entrada, forçando os recém-chegados a fazer engenharia reversa de como construir e executar o projeto.
- **Estrutura por documento, não por modelo:** uma página de wiki descreve a organização padrão, mas nada a gera nem a impõe, de modo que a realidade se afasta dela.
- **Deriva do modelo:** os repositórios gerados a partir de um modelo divergem com o tempo e as melhorias no modelo nunca chegam a eles.
- **Hierarquia superprojetada:** ninhos profundos de pastas quase vazias que acrescentam cerimônia sem ajudar na navegação.
- **Responsabilidades misturadas:** código-fonte, testes, saídas de build e segredos embaralhados, sem separação clara.
- **Saídas de build e artefatos locais com commit:** arquivos gerados versionados porque as regras de ignorar nunca foram configuradas, poluindo o histórico e os diffs.
- **Violações de camada escondidas por uma estrutura plana:** nenhuma fronteira física, de modo que ciclos de dependência e acoplamento indevido se infiltram sem ser notados.

## Modelo de maturidade

- **Nível 1 (Iniciar):** Cada repositório é organizado ad hoc por seus autores, reagindo ao que o momento exige. As organizações variam muito. Os READMEs são ausentes ou não confiáveis. As pessoas recém-chegadas precisam ser levadas a cada repositório pela mão.
- **Nível 2 (Desenvolver):** Existem convenções básicas informais e muitos repositórios se parecem, algumas equipes mantêm uma organização inicial própria, mas não há padrão autoritativo, nem esqueletos compartilhados, e a estrutura deriva de forma perceptível de uma equipe para outra.
- **Nível 3 (Padronizar):** Um padrão de estrutura documentado e versionado é imposto em toda a organização. Os novos repositórios são gerados a partir de modelos compartilhados que trazem uma organização padrão, README, arquivos de configuração e CI. Os desvios passam por um processo documentado de exceção em vez de acontecerem em silêncio.
- **Nível 4 (Gerenciar):** A conformidade com o padrão é medida e controlada com dados: verificações automatizadas relatam que fração dos repositórios corresponde à organização, o quanto os repositórios gerados por modelo derivaram, a completude do README e as violações de direção de dependência, tudo acompanhado em relação a linhas de base. Os tempos de integração e de navegação são medidos. As exceções são registradas e revisadas, e as mudanças nos modelos são aprovadas com base em evidências e não em opinião.
- **Nível 5 (Orquestrar):** A estrutura é continuamente melhorada e adaptativa: as melhorias nos modelos se propagam automaticamente para os repositórios existentes, a governança da estrutura é integrada às ferramentas de segurança, de conformidade e de plataforma, e o padrão evolui deliberadamente conforme linguagens, arquiteturas e o portfólio mudam, mantendo alta a uniformidade enquanto a organização muda ao redor.

## Ideias para discussão

- Quais pastas de nível superior devem ser realmente universais na sua organização, e quais devem ser opcionais?
- Como você impede que os repositórios gerados a partir de um modelo se afastem dele com o tempo?
- Onde está a linha entre uma hierarquia útil e em camadas e uma cerimônia de pastas superprojetada?
- Como o seu padrão de estrutura deve diferir, se é que deve, entre uma abordagem de monorrepositório e de vários repositórios?
- Qual é o processo de exceção certo para um projeto cujas necessidades genuínas não se encaixam na organização padrão?
- Quanto da sua estrutura pode ser verificado automaticamente, e o que ainda depende de revisão humana?
- Quem é o responsável pelo padrão de estrutura e pelos seus modelos, e como as mudanças são propostas e implantadas?

## Principais conclusões

- Organize cada repositório de modo que qualquer engenheiro consiga navegar por qualquer base de código por expectativa, seguindo o princípio da menor surpresa.
- Adote uma organização consistente de nível superior (código-fonte, testes, documentação, build, implantação, scripts, exemplos, especificação) e faça do README o ponto de entrada.
- Versione a configuração de editor e de ferramentas (como o `.editorconfig`) para que as convenções sejam ativas, e não apenas escritas.
- Imponha a estrutura com esqueletos e modelos para que os novos repositórios sejam corretos por padrão.
- Em escala, o valor está na uniformidade: governe o padrão, gerencie a deriva e permita desvios apenas por exceção documentada.

## Referências e leitura complementar

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
