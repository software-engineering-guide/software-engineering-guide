# 7.5 Ciência de decisão e cultura de dados

## Visão geral e motivação

A ciência de decisão é a prática de conectar os dados a decisões reais, apoiando-se em estatística, ciência comportamental e julgamento para ajudar as pessoas a escolher bem sob incerteza. Uma cultura informada por dados é a condição organizacional em que isso acontece por padrão: as pessoas recorrem à evidência, raciocinam com cuidado sobre causa e efeito, comunicam a incerteza com honestidade e atualizam suas crenças quando os dados justificam. Este capítulo é deliberadamente o arremate da sequência de dados, porque toda a estratégia, a engenharia, as análises e a experimentação que o precedem não valem nada se não mudarem as decisões para melhor.

Para grandes equipes, é aqui que os investimentos em dados mais falham, não nos pipelines, mas na última milha entre a percepção e a ação. As empresas gastam muito em plataformas e painéis e ainda assim tomam as grandes decisões por hierarquia, hábito ou pelo apresentador mais confiante. Um modo de falha comum é o teatro de dados: painéis e análises elaborados, produzidos para parecer rigorosos enquanto a decisão real foi tomada de antemão e os dados foram escolhidos a dedo para justificá-la. O governo acrescenta apostas altas e escrutínio. As decisões de política justificadas por alegações causais fracas podem alocar mal o dinheiro público e prejudicar cidadãos, e a exigência de prestação de contas faz do raciocínio honesto sobre a evidência uma obrigação cívica, não só uma boa prática.

Os problemas difíceis aqui são cognitivos e culturais, não técnicos. As pessoas confundem [correlação com causalidade](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation), ignoram [fatores de confusão](https://en.wikipedia.org/wiki/Confounding) (variáveis ocultas que conduzem tanto a suposta causa quanto o efeito), ancoram no primeiro número que veem e leem estimativas pontuais como certezas. E na pressa de se tornarem guiadas por dados, as organizações podem derivar para a vigilância: medir indivíduos de modo tão intrusivo que destroem a confiança e provocam manipulação. Construir uma genuína cultura de medição significa acertar o raciocínio, comunicar a incerteza com fidelidade e medir sistemas e resultados sem transformar os dados num instrumento de controle sobre as pessoas.

## Princípios fundamentais

- O propósito dos dados é decidir melhor, não produzir relatórios.
- Decidam o que mudaria a sua opinião antes de olhar os dados.
- Correlação não é causalidade. Interroguem os fatores de confusão antes de agir.
- Comuniquem a incerteza com honestidade: uma estimativa pontual sem faixa engana.
- Sejam informados por dados, não escravos dos dados. Julgamento e contexto ainda importam.
- Meçam para aprender e melhorar os sistemas, não para vigiar e punir indivíduos.
- Atualizem as crenças quando a evidência justifica. Mudar de ideia é uma força.
- A [segurança psicológica](https://en.wikipedia.org/wiki/Psychological_safety) é pré-requisito para a análise honesta e a divergência.

## Recomendações

### Conecte os dados às decisões e evite o teatro de dados

Liguem a análise a uma decisão específica desde o início: o que faremos de diferente conforme o que acharmos? Antes de reunir dados, declarem a decisão, as opções e que evidência favoreceria cada uma, idealmente que resultado mudaria a sua opinião. Isso protege contra o teatro de dados, em que a análise meramente decora uma decisão já tomada. Se nenhum achado realista alteraria a escolha, não gastem com a análise. Façam o julgamento com honestidade e digam isso. Insistam que as apresentações abram com a decisão e a recomendação, não com um passeio por gráficos.

### Raciocine com cuidado sobre a causalidade

A maioria das perguntas de negócio e de política é causal (esta ação produzirá este resultado), mas a maioria dos dados disponíveis é observacional e cheia de fatores de confusão. Ensinem às equipes a diferença entre correlação e causalidade e as armadilhas: variáveis de confusão, [viés de seleção](https://en.wikipedia.org/wiki/Selection_bias), causalidade reversa e correlação espúria. Prefiram experimentos aleatorizados para as alegações causais onde viável. Onde os experimentos são impossíveis, usem técnicas cuidadosas de [inferência causal](https://en.wikipedia.org/wiki/Causal_inference) e declarem as suas suposições explicitamente em vez de escorregar de “associado a” para “causa”. Sejam especialmente céticos com uma história atraente construída sobre uma única correlação.

### Comunique a incerteza às partes interessadas

Números apresentados como estimativas pontuais precisas convidam à falsa confiança. Comuniquem faixas, intervalos de confiança ou de credibilidade e as suposições-chave por trás de qualquer número. Usem linguagem simples e visuais honestos (barras de erro, faixas, bandas de cenário) para que os tomadores de decisão captem o que se sabe e o que não se sabe. Distingam o que os dados mostram, o que vocês inferem e o que vocês supõem. Calibrem a confiança à evidência: apresentem uma previsão feita com poucos dados como exatamente isso. A incerteza comunicada com honestidade gera mais confiança que a falsa precisão, porque sobrevive ao contato com a realidade.

### Construa uma cultura de medição sem vigilância

Criem um ambiente em que as equipes rotineiramente definem métricas de sucesso, medem resultados e aprendem com eles, mas mirem a medição em sistemas, processos e resultados e não no monitoramento de indivíduos. As métricas usadas para vigiar e classificar pessoas são manipuladas, geram medo e destroem a honestidade de que as boas decisões precisam (uma dinâmica captada pela [lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart's_law): uma medida que vira meta deixa de ser uma boa medida). Favoreçam métricas agregadas e orientadas a resultados. Envolvam as equipes na escolha das próprias medidas e separem as métricas de aprendizado da avaliação de desempenho. Protejam a segurança psicológica para que as pessoas tragam à tona más notícias e divergências cedo.

### Fomente hábitos saudáveis e letramento em dados

Ampliem o letramento em dados para que as pessoas leiam um gráfico criticamente, questionem a definição de uma métrica e identifiquem uma alegação enganosa. Normalizem perguntar “como sabemos disso?” e “o que mudaria a nossa opinião?”. Recompensem as pessoas por atualizarem seus pontos de vista diante da evidência e por rodarem experimentos que falham de modo informativo. Tornem seguro dizer “os dados não nos dizem” em vez de fabricar certeza. Os líderes dão o tom: quando mudam decisões com base em evidências e admitem a incerteza, a cultura segue.

### Proteja-se contra o viés e o mau uso

Fiquem atentos aos vieses previsíveis: o [viés de confirmação](https://en.wikipedia.org/wiki/Confirmation_bias) ao selecionar dados de apoio, o [viés de sobrevivência](https://en.wikipedia.org/wiki/Survivorship_bias) ao ignorar o que falta, a ancoragem num número inicial e o viés retrospectivo nas revisões pós-incidente. Incorporem a revisão do advogado do diabo, o pré-registro do que vocês esperam achar e perspectivas diversas nas análises importantes. Levem a ética de dados a sério (equidade, transparência e evitar dano), especialmente quando as decisões afetam o sustento, os benefícios ou os direitos das pessoas.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| Guiada por dados (os dados decidem) | Reduz o viés, consistente | Ignora o contexto, é manipulável, frágil | Domínios bem compreendidos |
| Informada por dados (dados mais julgamento) | Equilibra evidência e contexto | Mais lenta, exige julgamento | Decisões complexas ou inéditas |
| Experimentar para a causalidade | Evidência causal forte | Cara, lenta, nem sempre viável | Escolhas reversíveis de alto risco |
| Inferência observacional | Usa os dados disponíveis | Risco de confusão, alegações mais fracas | Quando os experimentos são impossíveis |
| Métricas de resultado/sistema | Conduz a melhoria, pouca manipulação | Menos responsabilização individual | Culturas de aprendizado |
| Vigilância individual | Visibilidade granular | Manipulação, medo, confiança corroída | Raramente justificada |

A tensão definidora é rigor versus velocidade e viabilidade. Os experimentos aleatorizados dão a evidência causal mais forte, mas custam tempo e muitas vezes são impossíveis para escolhas estratégicas ou de política pontuais, onde um julgamento cuidadoso sobre os fatores de confusão e suposições explícitas precisam bastar. A segunda tensão é entre medição e confiança: quanto mais granularmente vocês medem os indivíduos, mais conseguem ver e menos comportamento honesto obtêm. Uma cultura madura se inclina ao julgamento informado por dados e à medição agregada, orientada a resultados. Aceita um pouco menos de precisão aparente em troca de decisões que se sustentam e de uma força de trabalho que diz a verdade.

## Perguntas para discutir com sua equipe

1. **Vocês declaram o que mudaria a sua opinião antes de olhar os dados, e essa pergunta está escrita nos seus documentos de decisão?** A proteção mais forte do capítulo contra o teatro de dados é nomear a decisão, as opções e a evidência que favoreceria cada uma, idealmente o resultado que inverteria a sua escolha, antes de reunir dados. Se nenhum achado realista alteraria a decisão, o movimento honesto é pular a análise e fazer o julgamento abertamente. Para empresas e agências em que uma única escolha estratégica ou de política pode desperdiçar mais que um programa de análises inteiro custa, essa disciplina tem alta alavancagem. Levem uma decisão recente e perguntem se algum achado poderia tê-la mudado, ou se os gráficos meramente decoraram uma conclusão já alcançada. Se “o que mudaria a nossa opinião?” não é uma pergunta-padrão nos seus documentos de decisão, tornem-na uma e insistam que as apresentações abram com a recomendação, não com um passeio por gráficos.

2. **Quando surge uma correlação atraente, como vocês interrogam os fatores de confusão antes de agir, e preferem um experimento onde ele é viável?** O capítulo alerta que a maioria das perguntas de negócio e de política é causal enquanto a maioria dos dados disponíveis é observacional e cheia de fatores de confusão, viés de seleção e causalidade reversa. Seus próprios exemplos repetem uma armadilha: os clientes engajados se autosselecionam para uma funcionalidade ou programa, e a correlação bruta com menos churn ou mais empregos encontrados some numa comparação controlada. Agir sobre essa correlação significa uma campanha ou política cara e mal direcionada. Levem uma decisão recente que repousou numa única correlação e perguntem que variável oculta poderia conduzir os dois lados. Onde um experimento é viável, prefiram-no. Onde não é, usem métodos cuidadosos de inferência causal e declarem as suas suposições explicitamente em vez de escorregar de “associado a” para “causa”.

3. **As suas métricas visam melhorar sistemas e resultados, ou monitorar indivíduos, e vocês separaram as métricas de aprendizado da avaliação de desempenho?** O capítulo traça uma linha nítida: a medição apontada para pessoas é manipulada, gera medo e destrói a honestidade de que as boas decisões precisam, uma dinâmica que a lei de Goodhart prevê assim que uma medida vira meta. Ele favorece métricas agregadas e orientadas a resultados, o envolvimento das equipes na escolha das próprias medidas e a proteção da segurança psicológica para que as pessoas tragam más notícias cedo. Em contextos governamentais e corporativos, vigiar o pessoal da linha de frente corrói a confiança que torna possível, para começar, ter dados exatos. Levem a pergunta concreta: quais das suas métricas poderiam ser usadas para classificar ou punir indivíduos, e as pessoas as manipulariam sob pressão? Se as métricas de aprendizado e a avaliação de desempenho estão emaranhadas, separem-nas, para que a medição conduza a melhoria em vez de comportamento defensivo.

4. **Quando um número chega a um tomador de decisão, ele chega como uma faixa com suas suposições anexadas, ou como uma estimativa pontual que convida à falsa confiança?** O capítulo argumenta que a incerteza comunicada com honestidade gera mais confiança que a falsa precisão, porque sobrevive ao contato com a realidade, mas a atração por um único número confiante é forte quando um líder quer uma resposta limpa. Para uma grande equipe, a pressão concorrente é real: faixas e barras de erro podem soar evasivas a executivos que recompensam a decisão rápida, então os analistas aprendem a tirar as ressalvas para serem ouvidos. Levem um relatório recente e conferiram se ele distinguiu o que os dados mostram, o que se inferiu e o que se supôs, e se uma previsão construída com poucos dados foi rotulada como exatamente isso. Em contextos corporativos e governamentais, em que um número pode acabar num pacote para o conselho, numa proposta orçamentária ou num testemunho público, uma estimativa pontual apresentada como certeza é um passivo, então combinem um padrão da casa em que os números consequentes carreguem uma faixa, as suposições-chave e uma declaração simples de confiança.

5. **É genuinamente seguro aqui dizer “os dados não nos dizem”, e quem tem permissão para questionar como uma métrica é definida?** O capítulo trata o letramento em dados e a segurança psicológica como pré-requisitos: as pessoas precisam ler um gráfico criticamente, perguntar “como sabemos disso?” e admitir a incerteza sem penalidade, ou a cultura fabrica falsa certeza por padrão. A tensão para uma grande organização é que um letramento amplo exige tempo e orçamento reais de treinamento, e questionar a métrica favorita de uma pessoa sênior pode parecer limitante para a carreira, então números não examinados sobem sem contestação. Levem evidências sobre quem na sala de fato consegue interrogar a definição e a procedência de uma métrica e lembrem a última vez que alguém foi recompensado, e não punido, por atualizar seu ponto de vista ou relatar um fracasso informativo. Para órgãos corporativos e governamentais, em que uma medida mal definida pode conduzir financiamento ou relatórios públicos, nomeiem explicitamente quem tem legitimidade para questionar uma métrica e protejam essa pessoa quando a usar.

6. **Como vocês protegem as análises importantes contra o viés previsível, e incorporam a divergência antes de uma decisão e não depois?** O capítulo lista as armadilhas que corrompem a evidência em silêncio: o viés de confirmação ao selecionar dados de apoio, o viés de sobrevivência ao ignorar o que falta, a ancoragem num número inicial e o viés retrospectivo nas revisões pós-incidente. A consideração concorrente é a velocidade, já que a revisão do advogado do diabo, o pré-registro do que vocês esperam achar e as perspectivas diversas atrasam uma decisão e são as primeiras coisas cortadas sob pressão de prazo. Levem uma análise recente de alto risco e perguntem o que teria vindo à tona se alguém tivesse sido designado para defender o caso oposto e se a equipe escreveu as suas expectativas antes de ver os resultados. Em contextos corporativos e especialmente governamentais, em que as decisões afetam o sustento, os benefícios ou os direitos das pessoas, tratem a ética de dados e a divergência estruturada como exigências permanentes nas análises consequentes, não extras que um trimestre cheio pode descartar em silêncio.

## Perspectiva por setor

**Startup.** Sem analistas e com apenas algumas semanas de fôlego por aposta, a sua ciência de decisão é um hábito e não uma função: antes de um grande compromisso, perguntem que resultado mudaria a sua opinião e se um experimento barato consegue respondê-lo mais depressa que uma reunião. Protejam-se com firmeza de apostar o trimestre numa única correlação vistosa, porque uma equipe minúscula não se recupera de um roteiro mal direcionado. Mantenham leve: uma linha escrita no documento de decisão nomeando o sinal que os faria parar, não uma revisão formal que vocês nunca vão rodar.

**Pequena empresa.** Vocês provavelmente não têm especialista em dados e compram análises dentro de ferramentas que já usam, então o risco é confiar num painel do fornecedor sem questionar como uma métrica é definida ou se a comparação é justa. Gastem a sua escassa atenção com o raciocínio e não com as ferramentas: separem correlação de causalidade nas uma ou duas decisões que de fato movem o negócio e declarem a si mesmos a faixa honesta antes de comprometer dinheiro que não volta. Quando uma ferramenta se oferecer para automatizar uma decisão, mantenham uma pessoa no circuito sempre que uma decisão errada custaria um cliente.

**Grande empresa.** Entre muitas equipes, o problema é consistência e governança: uma expectativa compartilhada de que as análises nomeiem de antemão a decisão e os critérios de interrupção, de que as alegações causais declarem suas suposições e de que os números consequentes levem faixas para os pacotes do conselho e as auditorias. Separem as métricas de aprendizado da avaliação de desempenho em toda a organização para que a medição não azede em vigilância e manipulação. Invistam num letramento amplo em dados e em práticas de revisão como o advogado do diabo e o pré-registro, para que um apresentador confiante não possa substituir a evidência em escala.

**Governo.** A contratação, a transparência e a prestação de contas públicas elevam as apostas de toda alegação causal, porque uma política justificada por uma correlação espúria aloca mal o dinheiro público e pode prejudicar cidadãos. Prefiram desenhos rigorosos de comparação para avaliar programas, comuniquem os efeitos como faixas com suposições declaradas aos órgãos de supervisão e documentem o raciocínio para que uma auditoria possa segui-lo. Mirem a medição nos resultados dos programas e não na vigilância dos assistentes sociais e deem ao público um relato claro de como a evidência moldou a decisão.

## Exemplos

**Startup.** Uma startup pré-Série A notou que os usuários que entravam no fórum da comunidade tinham muito menos churn, e os fundadores estavam prontos para apontar todo o roteiro para funcionalidades do fórum. Antes de se comprometerem, um deles perguntou o que mudaria suas opiniões, e uma olhada rápida mostrou que os clientes já comprometidos eram simplesmente os que se davam ao trabalho de entrar no fórum. Rodaram um pequeno experimento em vez de apostar o trimestre numa correlação e fizeram de “o que mudaria a nossa opinião?” uma pergunta-padrão nos documentos de decisão.

**Grande empresa.** Uma empresa de serviços financeiros notou que os clientes que usavam uma determinada funcionalidade tinham muito menos churn e quase lançou uma campanha cara para empurrar todos para ela. Uma revisão de ciência de decisão apontou o fator de confusão óbvio: os clientes já engajados se autosselecionavam para a funcionalidade. Um experimento controlado mostrou então que a própria funcionalidade tinha pouco efeito causal sobre o churn. A empresa evitou um grande investimento mal direcionado, e a liderança adotou “o que mudaria a nossa opinião?” como pergunta-padrão antes de grandes gastos.

**Governo.** Uma agência pública que avaliava um programa de emprego resistiu a alegar sucesso a partir da estatística bruta de que os participantes achavam emprego a uma taxa alta, reconhecendo que pessoas motivadas se autosselecionam para esses programas. Usou um desenho rigoroso de comparação e comunicou o efeito estimado como uma faixa com suposições declaradas aos órgãos de supervisão. A medição se concentrou nos resultados do programa e não na vigilância dos assistentes sociais, o que preservou a confiança da linha de frente e ainda assim impulsionou a prestação de contas e a melhoria.

## Justificativa de negócio: motivações, ROI e TCO

O ROI da ciência de decisão é o custo evitado de decisões erradas e confiantes e a qualidade melhorada das decisões que uma organização toma milhares de vezes. Uma única grande escolha estratégica ou de política justificada por uma correlação espúria pode desperdiçar muito mais que o custo inteiro de construir boas práticas de decisão. Uma melhor calibração (saber o que se sabe e o que não se sabe) permite dimensionar as apostas de modo apropriado e evitar tanto compromissos imprudentes quanto a paralisia. No agregado, uma cultura informada por dados se compõe: cada equipe tomando decisões um pouco melhores e mais bem raciocinadas é uma alavancagem enorme.

O custo de adoção é sobretudo cultural e educacional: treinamento em letramento de dados, tempo para análise e revisão cuidadosas e disposição da liderança para mudar decisões e admitir a incerteza. É mais barato em dinheiro que as plataformas dos capítulos anteriores, mas mais difícil de instalar, porque pede que pessoas poderosas sejam governadas pela evidência. Pesem-no contra o custo de não adotar: teatro de dados que desperdiça esforço analítico, decisões conduzidas pela voz mais confiante, alegações causais que desmoronam no contato com a realidade e, onde a vigilância se instala, uma força de trabalho que manipula métricas e esconde más notícias. À liderança, o argumento é simples. Todo o investimento anterior em dados só se paga se a última milha entre a percepção e a decisão for sólida, e a ciência de decisão é essa última milha.

## Antipadrões e armadilhas

- Teatro de dados: análise produzida para justificar uma decisão já tomada.
- Escorregar de “correlacionado com” para “causa” sem interrogar os fatores de confusão.
- Apresentar estimativas pontuais como certezas, escondendo a faixa de incerteza.
- Viés de confirmação: buscar apenas os dados que sustentam uma conclusão preferida.
- Decisões HiPPO, em que a opinião da pessoa mais bem paga se sobrepõe à evidência.
- Transformar métricas em vigilância individual, provocando manipulação e medo.
- A lei de Goodhart em ação: uma métrica-alvo que deixa de medir o que importa.
- Punir as pessoas por fracassos informativos, matando a honestidade e a experimentação.

## Modelo de maturidade

1. **Iniciar.** As decisões correm por hierarquia e intuição, e a voz mais alta ou mais sênior vence. A correlação é livremente tratada como causalidade, a incerteza é ignorada e as poucas métricas em uso vigiam indivíduos e são manipuladas.
2. **Desenvolver.** Algumas equipes consultam dados e mostram consciência das armadilhas causais, mas a análise muitas vezes é seletiva, produzida para justificar uma decisão já tomada. A incerteza raramente é comunicada, e as práticas de medição são inconsistentes de equipe para equipe.
3. **Padronizar.** A organização documenta e impõe uma prática compartilhada: as análises são ligadas a uma decisão nomeada com critérios predefinidos, as equipes distinguem correlação de causalidade e preferem experimentos para as alegações causais, os números carregam faixas e suposições declaradas, e a medição é voltada a resultados e não a indivíduos, com a segurança psicológica protegida.
4. **Gerenciar.** A qualidade das decisões é medida e controlada em relação a linhas de base. A organização acompanha com que frequência as análises nomearam um sinal de interrupção antes de os dados chegarem, a fração dos números consequentes que saíram com uma faixa comunicada, quantas alegações causais repousaram em experimentos versus correlação nua e se as decisões foram revertidas com base em evidências. As práticas de proteção contra o viés, como o pré-registro e a revisão do advogado do diabo, são auditadas, e as métricas que começam a ser manipuladas são pegas e aposentadas.
5. **Orquestrar.** O raciocínio sólido é continuamente melhorado e integrado em toda a organização. “O que mudaria a nossa opinião?” é rotina antes de qualquer grande decisão, o rigor causal e a incerteza honesta são normas culturais, e os líderes atualizam visivelmente com base em evidências e admitem o que não se sabe. A medição conduz o aprendizado sem vigilância, as práticas de decisão se adaptam conforme a organização e seus riscos mudam, e todos os níveis decidem melhor como resultado.

## Ideias para discussão

- Onde, na sua organização, os dados são usados para decorar decisões já tomadas?
- Que decisão recente repousou numa correlação que talvez não seja causal?
- Quão honestamente os seus relatórios comunicam a incerteza, e quem resiste às faixas?
- As suas métricas visam melhorar sistemas ou monitorar indivíduos?
- Quando foi a última vez que um líder mudou visivelmente uma decisão por causa dos dados?
- Como vocês impedem que a busca por medição tombe para a vigilância?

## Principais conclusões

- O ponto dos dados é decidir melhor. Protejam-se do teatro de dados.
- Declarem o que mudaria a sua opinião antes de olhar os dados.
- Nunca confundam correlação com causalidade. Interroguem os fatores de confusão e prefiram experimentos.
- Comuniquem a incerteza com honestidade: a falsa precisão destrói a confiança quando falha.
- Sejam informados por dados, não escravos dos dados. Julgamento e contexto ainda importam.
- Meçam sistemas e resultados para aprender, não indivíduos para vigiar.
- Protejam a segurança psicológica para que as pessoas atualizem crenças e tragam à tona más notícias.

## Referências e leitura complementar

- Daniel Kahneman, "Thinking, Fast and Slow."
- Judea Pearl and Dana Mackenzie, "The Book of Why."
- Douglas W. Hubbard, "How to Measure Anything."
- Nate Silver, "The Signal and the Noise."
- Cathy O'Neil, "Weapons of Maths Destruction."
- Darrell Huff, "How to Lie with Statistics."
- Philip Tetlock and Dan Gardner, "Superforecasting."
- Charles Wheelan, "Naked Statistics."
