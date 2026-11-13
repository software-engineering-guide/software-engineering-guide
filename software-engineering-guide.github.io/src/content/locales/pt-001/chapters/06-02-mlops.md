# 6.2 Engenharia de aprendizado de máquina (MLOps)

## Visão geral e motivação

A engenharia de aprendizado de máquina, em geral chamada de [MLOps](https://en.wikipedia.org/wiki/MLOps), é a disciplina de tirar o [aprendizado de máquina](https://en.wikipedia.org/wiki/Machine_learning) dos cadernos e dos experimentos e levá-lo a sistemas de produção confiáveis, observáveis e mantíveis. O software tradicional se comporta do jeito que seu código diz que se comportará. Um sistema de ML se comporta do jeito que seu código, seus dados e seus parâmetros de modelo aprendidos dizem juntos. Isso torna os sistemas de ML mais difíceis de testar, mais difíceis de reproduzir e propensos a falhar em silêncio à medida que o mundo se afasta dos dados com que foram treinados. O MLOps traz o rigor da engenharia de software (controle de versões, testes, entrega contínua e monitoramento) a essa realidade em três partes de código mais dados mais modelos.

Para grandes equipes, o MLOps é o que separa um modelo pontual que deslumbra numa demonstração de uma frota de modelos que muitas equipes conseguem construir, implantar e operar com segurança. Sem plataformas e práticas compartilhadas, cada equipe reinventa pipelines de dados, laços de treinamento e implantação, e vocês acabam com sistemas frágeis que ninguém consegue reproduzir seis meses depois. As empresas dependem do MLOps para escalar entre dezenas de modelos, cumprir objetivos de nível de serviço e satisfazer auditores que perguntam como uma dada previsão foi produzida.

No governo e em setores regulados, o MLOps costuma ser uma exigência de conformidade disfarçada. A reprodutibilidade, a linhagem e o versionamento são o que permite a uma agência responder a uma pergunta de relevância legal: exatamente qual modelo, treinado com quais dados, com qual código, produziu a decisão que afetou um cidadão? Uma prática madura de MLOps mantém essa pergunta respondível anos depois, o que é ao mesmo tempo boa engenharia e uma salvaguarda legal.

*Veja também:* o capítulo 8.1 (CI/CD e entrega), o capítulo 9.2 (observabilidade e monitoramento) e o capítulo 6.6 (infraestrutura e operações de IA).

## Princípios fundamentais

- Tratem dados, código e modelos como artefatos versionados em conjunto. Mudar qualquer um muda o comportamento do sistema.
- Automatizem o caminho de dados a modelo treinado a implantação para que seja repetível e auditável.
- Tornem todo modelo rastreável até os dados, o código e a configuração exatos que o produziram.
- Avaliem os modelos contra dados representativos e reservados antes da implantação e continuem avaliando depois.
- Presumam que os modelos se degradam. Monitorem a deriva (a divergência gradual dos dados ao vivo ou das relações entrada-saída em relação ao que o modelo foi treinado), os problemas de qualidade de dados e o declínio de desempenho desde o primeiro dia.
- Prefiram pipelines chatos e reprodutíveis a experimentos engenhosos e irreprodutíveis.
- Separem as preocupações de velocidade de experimentação e de confiabilidade em produção e façam a ponte entre elas deliberadamente.

## Recomendações

### Gerencie explicitamente o ciclo de vida completo de ML

Definam e instrumentem cada etapa: ingestão e validação de dados, [engenharia de atributos](https://en.wikipedia.org/wiki/Feature_engineering) (feature engineering), treinamento, avaliação, implantação e monitoramento. Tornem explícitas as fronteiras entre as etapas para que cada uma possa ser testada, repetida e auditada. Evitem a falha comum em que um modelo é treinado num caderno ad hoc e jogado por cima do muro para as operações. Em vez disso, envolvam o ciclo de vida num pipeline orquestrado que qualquer engenheiro autorizado consiga rodar a partir de um checkout limpo.

### Use feature stores, rastreamento de experimentos e registros de modelos

Um **feature store** centraliza as definições de atributos para que as mesmas transformações rodem tanto no treinamento quanto no serviço. Isso elimina a distorção entre treinamento e serviço (training-serving skew: inconsistências entre como os atributos são calculados para o treinamento versus para as previsões ao vivo) e permite às equipes reutilizar atributos em vez de recalculá-los. O **rastreamento de experimentos** registra os parâmetros, a versão do código, a versão dos dados e as métricas de cada execução de treinamento, para que os resultados sejam comparáveis e reprodutíveis. Um **registro de modelos** é o sistema de registro dos modelos treinados, guardando versões, linhagem, resultados de avaliação, status de aprovação e estágio de implantação. Juntos, eles permitem responder “o que mudou?” quando o comportamento muda e promover ou reverter modelos por estágios governados.

### Torne dados e modelos reprodutíveis e versionados, com linhagem

Versionem os seus conjuntos de dados, não apenas o código. Usem armazenamento endereçável por conteúdo ou ferramentas de versionamento de dados para que uma execução de treinamento referencie um retrato imutável. Fixem o código com commits do git e os ambientes com dependências travadas e imagens de contêiner. Capturem a linhagem de ponta a ponta: quais dados brutos alimentaram quais atributos, quais atributos e código produziram qual modelo e onde esse modelo está implantado. Quando um incidente ou auditoria chega, a linhagem transforma um pesadelo forense numa simples consulta. Registrem a aleatoriedade (sementes) e o hardware sempre que os resultados dependerem deles.

### Escolha padrões de implantação que combinem com a carga de trabalho

- A pontuação em **lote** roda numa agenda sobre grandes conjuntos de dados. É a mais simples de operar, tolera latência e é ideal para relatórios e decisões periódicas.
- O serviço **online (tempo real)** responde a requisições individuais dentro de orçamentos apertados de latência. Exige recuperação de atributos de baixa latência e planejamento cuidadoso de capacidade.
- O **streaming** pontua eventos continuamente à medida que chegam. Serve à detecção de fraude e ao monitoramento em que o frescor é crítico.
- A **borda** (edge) roda modelos em dispositivos ou hardware local por razões de latência, privacidade, conectividade ou soberania de dados, comum em contextos governamentais e de campo.

Escolham o padrão mais simples que atende à exigência e projetem o lançamento com implantações sombra, canários e reversão instantânea.

### Monitore a deriva, a degradação e a qualidade dos dados

Instrumentem entradas e saídas em produção. Observem a **deriva de dados** (as distribuições de entrada mudando), a **[deriva de conceito](https://en.wikipedia.org/wiki/Concept_drift)** (a relação entre entradas e o alvo mudando), as falhas de **qualidade de dados** (nulos, mudanças de esquema, fontes a montante quebradas) e a **degradação de desempenho** medida contra a verdade de campo atrasada onde vocês a têm. Definam limiares de alerta, escrevam runbooks e liguem o monitoramento aos gatilhos de retreinamento. A degradação silenciosa é o modo clássico de falha do ML, e o monitoramento é a única defesa de vocês contra ela.

## Compromissos: prós e contras

| Decisão | Opção A | Opção B | Troca |
|---|---|---|---|
| Padrão de serviço | Lote | Online | Simplicidade e custo versus frescor e latência |
| Cálculo de atributos | Feature store | Pipelines por modelo | Consistência e reutilização versus custo inicial de montagem |
| Plataforma | Comprar uma plataforma gerenciada de MLOps | Montar ferramentas de código aberto | Velocidade e suporte versus flexibilidade e aprisionamento |
| Retreinamento | Agendado | Disparado por deriva | Previsibilidade versus capacidade de resposta e complexidade |
| Rigor de reprodutibilidade | Versionamento completo de dados | Rastreamento leve | Força de auditoria versus armazenamento e esforço |

A troca geral é investimento agora versus fragilidade depois. A infraestrutura pesada de reprodutibilidade e de monitoramento custa esforço no começo, mas previne o custo muito maior de falhas inexplicáveis, modelos irreprodutíveis e confiança erodida. As plataformas gerenciadas aceleram as equipes mas podem criar aprisionamento. Os conjuntos de código aberto oferecem controle ao preço do trabalho de integração. As grandes organizações costumam se beneficiar de uma equipe de plataforma compartilhada que esconde essa complexidade atrás de padrões de caminho pavimentado.

## Perguntas para discutir com sua equipe

1. **Como saberíamos que um modelo implantado se degradou em silêncio antes que um cliente ou cidadão fosse prejudicado, e quem é dono desse alerta?** O declínio silencioso é o modo clássico de falha do ML: o código ainda roda, o modelo ainda devolve escores confiantes e a qualidade escorrega à medida que o mundo se afasta dos dados de treinamento. Para uma grande equipe que opera muitos modelos, vocês precisam disso respondido por modelo e não uma vez para a frota, porque cada um tem seu próprio perfil de deriva e seu próprio atraso de verdade de campo. Levem os monitores atuais de deriva de dados, deriva de conceito e quebras de qualidade de dados, os limiares de alerta e o runbook que diz quem responde. Em contextos regulados em que os rótulos chegam semanas depois, discutam sinais substitutos que vocês podem observar nesse meio-tempo, porque esperar pela verdade de campo atrasada é esperar para descobrir o dano. Se nenhum dono único é nomeado para o alerta de deriva de um modelo, esse modelo está efetivamente sem monitoramento.

2. **Se um auditor pedisse para reproduzirmos uma previsão específica de dezoito meses atrás, conseguiríamos de fato fazê-lo de ponta a ponta?** A reprodutibilidade é a exigência de conformidade escondida dentro da boa engenharia: permite a uma agência responder exatamente qual modelo, treinado com quais dados, com qual código, produziu uma decisão que afetou alguém. Levem um exemplo real e tentem rastreá-lo: o retrato imutável dos dados, o commit do git, as dependências travadas e a imagem de contêiner, as sementes registradas e a linhagem dos dados brutos pelos atributos até o modelo implantado. O sinal é se algum elo dessa cadeia está faltando ou é manual. Para governo e setores regulados, decidam o período de retenção que a lei de fato exige e confirmem que o seu armazenamento mantém a linhagem respondível por toda essa janela, já que uma lacuna transforma uma consulta de rotina numa emergência forense.

3. **Qual é a nossa regra para promover um modelo à produção e revertê-lo, e ela é imposta pelo registro ou apenas pela confiança?** A promoção sem governança é como os experimentos de caderno vazam para a produção e como um modelo ruim persiste porque ninguém consegue revertê-lo com limpeza. Para muitas equipes, a diferença entre madura e frágil é se o registro de modelos condiciona a promoção a aprovação e avaliação obrigatórias, ou se um engenheiro pode empurrar pesos à mão. Levem o caminho atual de promoção, o mecanismo de reversão e evidência de que implantações sombra ou canários de fato rodam antes do tráfego total. Discutam se o retreinamento é agendado ou disparado por deriva e se os modelos retreinados passam por portões de validação antes da implantação, porque retreinar com dados ao vivo sem validação amplifica a deriva ou o envenenamento. A resposta deve ser imposta na plataforma e não numa página de wiki que as pessoas se espera que sigam.

4. **Construímos a nossa plataforma de MLOps sobre ferramentas de código aberto, compramos uma gerenciada ou combinamos as duas, e quem pesou o aprisionamento?** Essa escolha define o teto de quão depressa todo modelo futuro é entregue e de quanto controle vocês mantêm sobre os dados e pipelines. Uma plataforma gerenciada leva as equipes à produção depressa e carrega o suporte, mas pode prender as definições de atributos, os registros de linhagem e os artefatos de modelos num formato proprietário de que vocês não conseguem sair com facilidade. Um conjunto de código aberto montado mantém vocês portáteis ao preço de trabalho real de integração e manutenção. Levem o custo total de propriedade de cada caminho (licença ou construção, armazenamento, computação para retreinamento e a equipe de plataforma para operá-la), uma leitura honesta da capacidade da sua equipe de operar infraestrutura e um teste concreto de saída: vocês conseguiriam exportar o registro, o feature store e a linhagem e reconstruir em outro lugar? Em contextos corporativos e governamentais, acrescentem as restrições de contratação e as regras de soberania de dados, já que uma plataforma que guarda dados de treinamento numa região ou formato que o seu regulador proíbe está desqualificada por mais conveniente que seja.

5. **O nosso feature store e registro de modelos devem ser uma plataforma centralizada ou federados por equipe, e quanto a distorção entre treinamento e serviço nos custa hoje?** Centralizar as definições de atributos elimina a distorção em que um atributo é calculado de um jeito no treinamento e de outro no serviço, uma fonte silenciosa e cara de perda de exatidão, mas uma única plataforma pode virar um gargalo que desacelera todas as equipes. Federar dá autonomia às equipes ao mesmo tempo que multiplica a tubulação e as chances de duas equipes definirem o mesmo atributo de forma inconsistente. Levem evidências de onde a distorção já mordeu vocês, quantas equipes reutilizam atributos versus os reconstroem e os padrões de caminho pavimentado que uma equipe de plataforma compartilhada poderia oferecer. Para uma grande organização, pesem o benefício de governança de um único sistema de registro auditável contra o custo de entrega de uma fila central e, em contextos regulados, favoreçam a linhagem centralizada que permite a um auditor rastrear qualquer previsão até o código de atributo exato que a produziu.

6. **Combinamos o padrão de implantação de cada modelo com suas reais necessidades de latência, frescor e soberania, ou tudo foi levado a um só formato por padrão?** Lote, online, streaming e borda carregam cada um custo operacional e complexidade muito diferentes, e escolher o errado ou gasta demais em infraestrutura de tempo real de que um relatório noturno nunca precisou ou deixa um pontuador de fraude sem o frescor de que depende. Decidam por carga de trabalho qual padrão a exigência de fato justifica e resistam a padronizar na opção mais complexa porque parece moderna. Levem o orçamento de latência, o volume, o custo de uma resposta obsoleta e o atraso da verdade de campo de cada modelo. Em contextos governamentais e de campo, pesem deliberadamente a implantação na borda e local, porque as regras de soberania de dados ou a conectividade intermitente podem forçar os modelos para hardware local, e essa escolha remodela como vocês versionam, monitoram e revertem cada modelo que empurram para lá.

## Perspectiva por setor

**Startup.** O seu recurso mais escasso é a atenção da engenharia, então mantenham o MLOps leve e comprem-no. Acompanhem experimentos numa ferramenta hospedada simples, fixem cada modelo implantado ao retrato dos seus dados de treinamento e ao commit do código no git e acrescentem uma verificação barata de deriva em vez de uma plataforma. Pulem o feature store e os pipelines sob medida até um segundo ou terceiro modelo tornar a reutilização compensadora. Uma pilha frágil que vocês não conseguem manter os afundará mais depressa que uma capacidade ausente.

**Pequena empresa.** Vocês provavelmente não têm especialista em plataforma de ML e têm orçamento apertado, então tratem o MLOps como algo embutido nas ferramentas que já rodam e não um sistema em que se põe gente. Prefiram um serviço gerenciado que trate por vocês o versionamento, a implantação e o monitoramento e enquadrem a disciplina como uma questão de higiene de dados e de reprodutibilidade: saibam qual modelo e quais dados produziram um dado resultado e mantenham a capacidade de reverter. Favoreçam fornecedores que deixem vocês exportar os dados e modelos, para que uma troca posterior continue possível.

**Grande empresa.** O problema é a escala entre dezenas de modelos e muitas equipes: um feature store compartilhado, rastreamento de experimentos e um registro de modelos com promoção governada para que os grupos parem de reinventar pipelines. Orcem uma equipe de plataforma que ofereça padrões de caminho pavimentado, padronizem a linhagem e o monitoramento para que todo modelo seja auditável e todo incidente explicável e gerenciem deliberadamente construir versus comprar e o aprisionamento atrás de uma interface que mantenha trocáveis as ferramentas subjacentes. Imponham portões de validação e reversão na plataforma e não por convenção.

**Governo.** A reprodutibilidade, a linhagem e o versionamento são exigências de conformidade disfarçadas, então tratem-nas como de primeira classe desde o primeiro dia. Versionem o conjunto de dados e o código exatos por trás de cada modelo implantado, retenham essa linhagem pelo período legalmente exigido e sejam capazes de reproduzir qualquer previsão histórica que afetou um cidadão. Mantenham um humano revisando decisões consequentes, pesem a implantação na borda e local onde as regras de soberania de dados o exigirem e exijam que qualquer plataforma de fornecedor conceda portabilidade total dos seus dados, atributos e linhagem.

## Exemplos

**Startup.** Uma pequena startup de análise de dados entregou seu primeiro modelo de previsão de evasão com um cientista de dados e uma configuração leve. Acompanhou os experimentos numa ferramenta hospedada simples, fixou cada modelo implantado ao retrato dos seus dados de treinamento e ao commit do código no git e acrescentou um trabalho semanal básico que comparava as entradas recentes com a distribuição do treinamento. Quando uma fonte de dados mudou o formato de data e as previsões começaram a derivar, essa verificação simples pegou o problema em dias e não depois de uma ligação irritada de cliente, e a equipe conseguiu reproduzir o último bom modelo e reverter.

**Grande empresa.** Um banco de varejo opera dezenas de modelos de crédito e de fraude. Padronizou num feature store compartilhado entre as equipes, um serviço de rastreamento de experimentos e um registro de modelos com portões obrigatórios de aprovação. Todo modelo em produção se rastreia até o retrato dos seus dados de treinamento e o commit do código. Os modelos de fraude são implantados como pontuadores em streaming. Os de crédito rodam em lote. Uma camada de monitoramento observa a deriva das entradas e alerta quando o esquema de uma fonte de dados muda, o que uma vez pegou uma fonte a montante quebrada antes que ela corrompesse as decisões.

**Governo.** Uma agência pública de benefícios usa um modelo de ML para priorizar revisões de casos. Como essas decisões afetam o acesso dos cidadãos a serviços, a agência versiona o conjunto de dados e o código exatos por trás de cada modelo implantado, mantém essa linhagem pelo período legalmente exigido e consegue reproduzir sob demanda qualquer previsão histórica. Os modelos são implantados em lote, com um humano revisando os casos sinalizados, e um monitor de deriva força uma reavaliação obrigatória sempre que a população de entrada muda, de modo que o modelo nunca é aplicado em silêncio fora das condições em que foi validado.

## Justificativa de negócio: motivações, ROI e TCO

O MLOps se paga transformando experimentos frágeis em ativos confiáveis. O ROI vem de um tempo mais rápido até a produção para novos modelos, menos incidentes caros, menos infraestrutura duplicada e da capacidade de operar muitos modelos com uma pequena equipe de plataforma. Um feature store e um registro compartilhados podem cortar drasticamente o tempo de entrega por modelo, porque as equipes param de reconstruir a mesma tubulação.

O TCO cobre a construção ou licença da plataforma, o armazenamento de dados e modelos versionados, a computação para retreinamento e a equipe para operar tudo. Pesem isso contra o custo de não adotar: modelos que vocês não conseguem reproduzir nem auditar, falhas silenciosas que prejudicam clientes ou cidadãos e achados regulatórios. Em contextos regulados, o custo de um modelo inexplicável numa auditoria pode superar todo o investimento em MLOps. Defendam o caso junto à liderança enquadrando o MLOps como redução de risco e aceleração de entrega e não custo adicional: um caminho pavimentado que todo modelo futuro percorrerá.

## Antipadrões e armadilhas

- **Saltos do caderno para a produção.** Implantar modelos treinados em cadernos sem governança e sem reprodutibilidade.
- **Distorção entre treinamento e serviço.** Código de atributos diferente no treinamento e no serviço, causando perda silenciosa de exatidão.
- **Sem versionamento de dados.** Versionar o código mas não os dados, de modo que as execuções não podem ser reproduzidas.
- **Implantar e esquecer.** Entregar um modelo sem monitoramento, descobrindo a degradação só quando os usuários reclamam.
- **Retreinamento no piloto automático.** Retreinar automaticamente com dados ao vivo sem validação, amplificando a deriva ou o envenenamento.
- **Infraestrutura pontual.** Cada equipe construindo o próprio pipeline, multiplicando custo e fragilidade.
- **Ignorar rótulos atrasados.** Presumir que dá para medir a exatidão na hora quando a verdade de campo chega semanas depois.

## Modelo de maturidade

1. **Iniciar.** Modelos construídos ad hoc em cadernos. Implantação manual. Sem versionamento de dados nem de modelos. Sem monitoramento. Reproduzir uma previsão passada é adivinhação.
2. **Desenvolver.** Aparecem algum rastreamento de experimentos e um registro de modelos, mas as práticas variam por equipe. A implantação é semiautomatizada. O monitoramento básico cobre alguns modelos. O versionamento de dados é parcial e a linhagem tem lacunas.
3. **Padronizar.** Uma plataforma compartilhada, com feature store, registro, pipelines reprodutíveis e linhagem de ponta a ponta, é documentada e imposta em toda a organização. O monitoramento de deriva e de qualidade de dados roda entre os modelos. A promoção e a reversão seguem um caminho governado que toda equipe usa.
4. **Gerenciar.** A frota é medida em relação a linhas de base: as taxas de deriva, as quebras de qualidade de dados, a exatidão do modelo contra a verdade de campo atrasada, a distorção entre treinamento e serviço, o tempo até a produção e o custo operacional por modelo são acompanhados como métricas. Os limiares de alerta e os portões de validação são impostos com base em evidências, e a saúde de cada modelo é revisada numa cadência fixa com um dono nomeado.
5. **Orquestrar.** O ciclo de vida é totalmente automatizado, auditável e adaptativo. O retreinamento disparado por deriva roda atrás de portões de validação. Caminhos pavimentados de autoatendimento permitem às equipes entregar com segurança. A avaliação contínua liga o desempenho do modelo a métricas de negócio, e a plataforma se integra à entrega, ao risco e à conformidade, de modo que os modelos são rotineiramente aposentados, substituídos e redimensionados à medida que dados e condições mudam.

## Ideias para discussão

- Como vocês equilibram a liberdade de experimentação com a reprodutibilidade em produção?
- Qual é o gatilho certo de retreinamento (agenda, deriva ou declínio de desempenho) para os seus casos de uso?
- Por quanto tempo vocês precisam reter a linhagem de dados e de modelos, e o que conduz essa exigência?
- Os feature stores e registros devem ser plataformas centralizadas ou federadas por equipe?
- Como vocês monitoram a exatidão quando os rótulos de verdade de campo chegam com longos atrasos?
- Quando a implantação na borda vale a complexidade operacional adicional?

## Principais conclusões

- O comportamento do ML vem de código mais dados mais modelos. Versionem e governem os três juntos.
- Feature stores, rastreamento de experimentos e registros são a espinha dorsal do ML reprodutível.
- A linhagem torna os modelos auditáveis e os incidentes explicáveis: essencial em contextos regulados.
- Escolham lote, online, streaming ou borda para combinar com as necessidades de latência, frescor e soberania.
- Os modelos se degradam. Monitorar a deriva, a qualidade dos dados e o declínio não é opcional.

## Referências e leitura complementar

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
