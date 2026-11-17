# 10.8 Modelos de maturidade

## Visão geral e motivação

Um [modelo de maturidade](https://en.wikipedia.org/wiki/Maturity_model) é um modo estruturado de avaliar quão capaz e consistente é a sua prática num domínio e de descrever um caminho para melhorá-la. Define uma pequena escada de níveis. Embaixo, o trabalho é ad hoc e reativo. No topo, é medido, gerenciado e continuamente otimizado. Cada degrau tem características observáveis contra as quais se pode conferir.

Os modelos de maturidade transformam uma pergunta vaga (“somos bons nisto?”) numa resposta repetível (“estamos no nível 2 aqui, no nível 4 ali, e eis o que o nível 3 exigiria”). Este livro usa um modelo de cinco níveis em todo capítulo e os consolida no capítulo 12.4. Este capítulo trata da própria disciplina: como os modelos funcionam, quando ajudam e como enganam.

A razão pela qual importam é simples. As grandes organizações não conseguem melhorar o que não veem. Entre dezenas de equipes, a capacidade varia enormemente e de modo invisível. Algumas equipes têm excelentes testes e segurança fraca; outras, o inverso. Um modelo de maturidade dá um vocabulário compartilhado e uma régua comum, de modo que as lacunas se tornam comparáveis, o investimento pode ser priorizado e o progresso pode ser acompanhado ao longo do tempo e não meramente afirmado. Exemplos conhecidos incluem o CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), para processo), o modelo DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment); desempenho de entrega de software), o OWASP SAMM (Software Assurance Maturity Model) e o BSIMM (Building Security In Maturity Model) para segurança de software, o TMMi (Test Maturity Model integration, para testes), o modelo Agile Fluency e modelos de maturidade da gestão de dados, mais incontáveis scorecards internos.

Para empresas e especialmente para o governo, os modelos de maturidade carregam um peso particular. A contratação governamental há muito usa os níveis de avaliação do CMMI como qualificação de fornecedores, e frameworks como o CMMC dos EUA ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) ligam a maturidade de cibersegurança diretamente à elegibilidade para trabalho de defesa. Isso dá dentes reais aos modelos de maturidade. Também cria o risco central deste capítulo: quando um nível vira portão ou meta, as pessoas otimizam para a avaliação e não para a capacidade subjacente. Bem usados, os modelos de maturidade são um espelho. Mal usados, são teatro.

## Princípios fundamentais

- **A maturidade é um meio, não um fim.** O objetivo é capacidade e resultados, não um número de nível.
- **Avaliem para aprender, não para pontuar.** Uma autoavaliação honesta vence uma avaliação lisonjeira.
- **Mais alto nem sempre é melhor.** A meta certa depende do risco, do contexto e do custo.
- **Meçam por domínio, não por uma nota global.** A capacidade é desigual. Um único número a esconde.
- **Priorizem primeiro as lacunas de menor maturidade e maior risco.**
- **Cuidado com a [Lei de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Assim que um nível vira meta, deixa de medir a capacidade.
- **Reavaliem periodicamente.** A maturidade deriva conforme pessoas, sistemas e ameaças mudam.

## Recomendações

### Escolha o modelo certo para o domínio

Ajustem o modelo à capacidade que vocês querem melhorar e prefiram modelos estabelecidos e baseados em evidências a modelos inventados onde eles existirem:

- **Processo e entrega:** CMMI (maturidade ampla de processo), o modelo de capacidades do DORA (desempenho de entrega, fundamentado em pesquisa, capítulo 11.2).
- **Segurança:** OWASP SAMM e BSIMM (práticas de segurança de software), CMMC (cibersegurança de defesa).
- **Testes e qualidade:** TMMi.
- **Agile e formas de trabalhar:** o modelo Agile Fluency (capítulo 10.7).
- **Dados:** modelos de maturidade da gestão de dados (DMM, DCAM).

Para uso interno, uma escala simples de quatro ou cinco níveis aplicada por capacidade (como este livro faz) costuma ser mais acionável que um framework externo pesado. Reservem os modelos formais e avaliados para onde são exigidos por contrato.

### Avalie com honestidade e por capacidade

Rodem avaliações que produzam verdade, não conforto. Envolvam as pessoas que fazem o trabalho. Reúnam evidências em vez de opiniões. Pontuem cada capacidade separadamente, para que o quadro reflita a realidade: forte aqui, fraco ali. Uma autoavaliação usada para orientar a melhoria vale mais que uma avaliação externa usada para ganhar um selo, porque a primeira recompensa a franqueza e a segunda recompensa a apresentação. O capítulo 12.4 oferece uma autoavaliação consolidada de todos os domínios deste livro; usem-na como instrumento inicial.

### Use a maturidade para priorizar, não para punir

O resultado de uma avaliação é um backlog priorizado de melhorias, não um boletim para a culpa. Combinem a maturidade com o risco. Uma capacidade de nível 1 numa área de baixo risco pode estar bem. Uma capacidade de nível 2 numa área crítica à segurança ou à conformidade é urgente. Direcionem o investimento para as lacunas em que a baixa maturidade encontra o alto risco e liguem o trabalho a resultados (capítulo 11.1) para que a melhoria seja medida por resultados e não por subir a escada por subir.

### Defina os níveis-alvo deliberadamente: mais alto não é de graça

Cada nível acima custa esforço e muitas vezes acrescenta peso de processo. A meta certa raramente é “nível 5 em toda parte”. É o nível em que a capacidade extra ainda justifica o custo extra para o risco daquele domínio. As capacidades reguladas e críticas à segurança podem genuinamente precisar dos degraus mais altos, e a auditoria muitas vezes exige pelo menos um nível 3 “definido”. Muitas outras são bem servidas no nível 3 e só acumulariam burocracia se empurradas além. Decidam as metas por capacidade e parem de subir quando o retorno ajustado ao risco parar.

### Proteja-se do teatro da maturidade

O único modo de falha que destrói o valor dos modelos de maturidade é otimizar para a nota. Fiquem atentos a avaliações que dão notas generosas, evidências montadas só para a avaliação ou alegações de “nível 5” que os incidentes de produção contradizem. Mantenham a avaliação ligada ao comportamento observável e a resultados reais. Façam rodízio dos avaliadores ou submetam-nos a uma checagem externa de sanidade. Tratem uma autonota suspeitamente alta como um mau cheiro. No instante em que o nível vira o objetivo, o modelo deixa de dizer a verdade.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| **Modelos formais avaliados (CMMI, CMMC)** | Comparáveis, reconhecidos por contrato, rigorosos | Caros. Convidam à manipulação. Podem enrijecer o processo |
| **Scorecards internos leves** | Rápidos, acionáveis, pouca sobrecarga | Menos comparáveis externamente. Fáceis de enviesar |
| **Modelos de capacidade baseados em evidências (DORA)** | Ligados a resultados reais. Apoiados em pesquisa | Escopo mais estreito. Exigem métricas reais |
| **Uma única nota geral de maturidade** | Simples de comunicar | Esconde a capacidade desigual. Engana |
| **Avaliação por capacidade** | Priorização precisa e acionável | Mais esforço. Sem número de manchete único |

A tensão central é **a avaliação como espelho versus a avaliação como meta**. O mesmo modelo que ajuda uma equipe a se ver com clareza se torna contraproducente no instante em que um nível é atrelado a recompensa, elegibilidade ou status. Quanto mais um nível importa, mais energia flui para a aparência de maturidade e não para a substância.

## Perguntas para discutir com sua equipe

1. **Devemos manter uma autoavaliação interna franca, separada de qualquer nível avaliado por contrato, e quem é dono de cada uma?** Quando um nível CMMC ou CMMI condiciona receita, a avaliação e a verdade se afastam, porque a energia flui para passar e não para melhorar. Para uma grande empresa ou um fornecedor governamental, essa lacuna é onde o risco se esconde: vocês passam na auditoria e continuam expostos. Mantenham dois livros de propósito. Guardem a avaliação formal para a elegibilidade e mantenham um scorecard interno brusco, pelo qual ninguém é recompensado por inflar. Nomeiem um dono para cada um e tratem qualquer distância entre eles como um sinal para investigar e não para disfarçar. Levem incidentes recentes, quase acidentes e o decaimento pós-avaliação à reunião como evidência de qual livro está dizendo a verdade.

2. **Para cada domínio, estamos adotando um modelo estabelecido e baseado em evidências ou inventando o nosso próprio scorecard, e essa é a decisão certa?** Os modelos estabelecidos (DORA para a entrega, SAMM ou BSIMM para a segurança, TMMi para os testes) carregam pesquisa e comparabilidade externa que uma grade caseira não iguala. Uma escala interna leve de quatro níveis é mais rápida e mais acionável e muitas vezes é a melhor escolha para a direção interna. A armadilha é inventar um framework pesado e sob medida que tem toda a cerimônia de um modelo formal e nenhuma base de evidências. Decidam por domínio: reservem os modelos formais avaliados para onde um contrato os exige, usem modelos baseados em evidências onde existem e se ajustam e mantenham uma escala simples por capacidade para todo o resto. Levem a lista de domínios, marquem qual modelo cada um usa hoje e questionem todo scorecard inventado.

3. **Quem conduz as nossas avaliações, como pegaríamos uma nota generosa e com que frequência reavaliamos?** Uma avaliação que se autopontua se lisonjeia, e a maturidade deriva conforme pessoas, sistemas e ameaças mudam, então uma avaliação de dois anos atrás muitas vezes é ficção. Façam rodízio dos avaliadores ou tragam uma checagem externa de sanidade e tratem uma autonota suspeitamente alta como um mau cheiro a perseguir e não uma vitória a celebrar. Definam uma cadência de reavaliação ligada a quão depressa cada domínio muda: segurança com mais frequência que, digamos, documentação. Reúnam evidências e envolvam as pessoas que fazem o trabalho em vez de colher opiniões de gerentes. Se a sua resposta é que uma equipe se pontua uma vez por ano sem conferência cruzada, vocês estão medindo conforto e não capacidade.

4. **Que nível-alvo de maturidade cada capacidade de fato precisa, e onde empurrar mais alto só nos compraria peso de processo?** Mais alto não é de graça: cada nível acima custa esforço e em geral acrescenta cerimônia, então uma meta uniforme de nível 5 em toda parte drena um orçamento finito de melhoria para uma burocracia que alguns domínios nunca pagarão. Para uma grande organização a meta certa varia por capacidade, porque uma área de baixo risco no nível 2 pode estar perfeitamente segura enquanto uma área crítica à segurança ou à conformidade no mesmo nível é uma emergência. Levem uma classificação de risco por capacidade, uma estimativa honesta do que o próximo degrau custa em esforço e processo e qualquer piso de auditoria ou contratual, já que muitas auditorias exigem pelo menos um nível 3 definido. Em contextos corporativos e governamentais, algumas capacidades reguladas genuinamente precisam dos degraus mais altos enquanto a maioria é bem servida no nível 3, então decidam as metas deliberadamente, capacidade por capacidade, e parem de subir quando o retorno ajustado ao risco parar.

5. **Na última vez que subimos um nível de maturidade, o resultado que ele devia proteger de fato melhorou, ou só a nota se moveu?** Um nível que sobe enquanto os incidentes, o prazo de entrega ou as taxas de defeitos ficam estáveis é a Lei de Goodhart em ação: assim que o número vira meta, deixa de medir a capacidade. Para uma grande equipe isso passa fácil, porque uma avaliação bem-sucedida parece progresso mesmo quando a produção conta outra história. Liguem o nível de cada capacidade a uma métrica de resultado real antes de investir e depois levem à discussão a evidência de antes e depois: incidentes por trimestre, taxa de falha de mudanças, tempo de recuperação, seja o que for que a capacidade existe para melhorar. Em portfólios corporativos e governamentais em que um nível avaliado condiciona a elegibilidade, a lacuna é perigosa, porque o nível pode subir com evidência montada enquanto a prática subjacente decai em silêncio, e a primeira prova disso é uma violação, uma interrupção ou uma auditoria malsucedida.

6. **Comunicamos uma única nota de maturidade de manchete ou um quadro por capacidade, e algum nível é alguma vez atrelado a recompensa, classificação ou posição da equipe?** Um único número geral é fácil de apresentar à liderança e esconde exatamente a desigualdade que importa, porque uma forte entrega pode mascarar uma capacidade de segurança de nível 1; um mapa de calor por capacidade dá mais trabalho mas mostra onde a baixa maturidade encontra o alto risco. A pergunta mais difícil é como as notas são usadas, porque no instante em que um nível é atrelado à recompensa ou à classificação de uma equipe, o relato honesto morre e o esforço flui para a aparência de maturidade e não para a substância. Levem o mapa de calor e um relato franco de todo lugar onde um nível hoje alimenta uma avaliação de desempenho, uma decisão de orçamento ou um scorecard de fornecedor. Para empresas e fornecedores governamentais, em que os níveis avaliados podem condicionar receita e elegibilidade, sejam explícitos sobre quais notas carregam consequências e quais existem só para orientar, porque um quadro de maturidade que as pessoas são recompensadas por inflar deixa de descrever a realidade.

## Perspectiva por setor

**Startup.** Um modelo pesado e avaliado é sobrecarga que vocês não podem bancar com pouco fôlego. Rodem uma autoavaliação de uma hora numa escala simples entre um punhado de capacidades, consertem apenas a lacuna de menor maturidade que bloqueia algo concreto (digamos, o questionário de segurança do seu primeiro cliente corporativo) e deixem o resto em paz. A avaliação deve custar uma tarde, não um consultor, e o seu resultado é uma única próxima ação e não uma nota alta uniforme de que vocês nem precisam nem conseguem financiar.

**Pequena empresa.** Sem avaliador dedicado e com orçamento apertado, tomem emprestado um modelo público leve em vez de encomendar um framework sob medida: uma lista de verificação curta de entrega ou de segurança que vocês possam autopontuar. Tratem-na como uma conversa anual sobre onde um ponto fraco custaria um cliente, não como um programa permanente. Mantenham-na barata e brusca, porque uma nota lisonjeira que vocês pagaram um fornecedor para produzir vale menos que uma franca que vocês mesmos fizeram numa tarde.

**Grande empresa.** O valor é um scorecard compartilhado por capacidade, aplicado de modo consistente entre muitas equipes, de modo que as lacunas se tornem comparáveis e o orçamento de melhoria flua para onde a baixa maturidade encontra o alto risco. Protejam-se com firmeza do teatro da maturidade assim que os níveis alimentarem orçamento ou status: façam rodízio ou checagem externa de sanidade dos avaliadores e gerenciem os resultados como um mapa de calor que direciona o investimento em caminhos pavimentados (capítulo 4.2) e não como uma tabela de classificação que ordena equipes e mata o relato honesto.

**Governo.** Um nível de maturidade costuma ser literalmente um portão aqui: o CMMC para trabalho de defesa, uma avaliação CMMI como qualificação de fornecedor. Cumpram o nível exigido com capacidade genuína e mantenham uma autoavaliação interna franca separada da avaliação formal, para que o piso da auditoria nunca vire em silêncio o teto. Documentem a evidência com transparência para os avaliadores e tratem qualquer distância entre o nível certificado e a prática real como risco com responsável a fechar, não papelada a arquivar.

## Exemplos

**Startup.** Uma startup de SaaS de dez pessoas roda uma autoavaliação de uma hora contra uma escala simples de quatro níveis cobrindo entrega, testes, segurança e sobreaviso. Acha a entrega e os testes no nível 3, mas a segurança presa no nível 1, o que importa porque está prestes a assinar seu primeiro cliente corporativo, com um questionário de segurança. Então os fundadores gastam o mês seguinte elevando só a segurança a um nível 2 defensável e deixam o resto em paz, em vez de perseguir uma nota alta uniforme de que ainda não precisam nem podem bancar.

**Grande empresa.** Uma empresa de serviços financeiros avalia suas 40 equipes com um scorecard leve por capacidade (entrega, testes, segurança, observabilidade, sobreaviso). O mapa de calor revela que a maturidade de segurança fica mais atrás onde a exposição regulatória é maior, então a equipe de plataforma financia primeiro, para essas equipes, ferramentas de segurança de caminho pavimentado (capítulo 4.2). Como a avaliação é usada para priorizar investimento e não para classificar equipes, os gerentes reportam com honestidade. A reavaliação um ano depois mostra movimento real e, de modo crucial, menos incidentes de segurança, não apenas notas mais altas.

**Governo.** Uma contratada de defesa precisa atingir um nível CMMC exigido para disputar trabalhos, e um integrador de sistemas mantém uma avaliação CMMI como qualificação contratual. Aqui o nível de maturidade é literalmente um portão para a receita. A versão bem conduzida trata o nível exigido como um piso de capacidade genuína e mantém uma autoavaliação interna franca separada da avaliação formal. A versão mal conduzida monta evidências para a avaliação e deixa a prática real decair no dia seguinte, passando na auditoria enquanto permanece exposta.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da avaliação de maturidade vem do **investimento direcionado**. Os orçamentos de melhoria são finitos. Gastos às cegas, financiam o que for mais barulhento. Uma avaliação de maturidade mostra onde a capacidade é mais fraca contra o risco, de modo que o mesmo gasto compra mais redução de risco e mais melhoria de resultados. A avaliação em si é barata, apenas dias de revisão estruturada e baseada em evidências, diante do custo de programas de melhoria mal alocados ou, pior, de uma lacuna de capacidade não detectada que surge como uma violação, uma interrupção ou uma auditoria malsucedida.

No **custo total de propriedade**, a disciplina é de baixo custo quando mantida leve e de alto custo quando endurece em burocracia de avaliação. O custo oculto dominante é o *teatro da maturidade*: o esforço gasto produzindo a aparência de maturidade nada devolve e pode mascarar risco real, o que é ROI negativo. Para defender o caso junto à liderança, apresentem a maturidade como uma lente de risco e de investimento, um mapa de calor que transforma “melhorar tudo” em “melhorar estas três coisas primeiro”, e orcem explicitamente contra a tentação de perseguir níveis por si sós. Onde um nível é exigido por contrato (CMMC, CMMI), o ROI é direto: é o preço da elegibilidade, e o objetivo é cumpri-lo com capacidade real e não com fingimento caro.

## Antipadrões e armadilhas

- **O nível como objetivo:** perseguir um número em vez da capacidade que ele deveria representar.
- **Teatro da maturidade:** montar evidências para uma avaliação enquanto a prática real decai.
- **Uma nota global:** uma única pontuação de maturidade que esconde uma desigualdade perigosa.
- **Mais alto é sempre melhor:** empurrar toda capacidade ao nível 5 seja qual for o risco ou o custo.
- **Avaliar uma vez e nunca mais:** uma avaliação pontual tratada como verdade permanente.
- **Classificar equipes para culpar:** usar a maturidade para punir, o que mata o relato honesto.
- **Culto ao modelo:** seguir a cerimônia de um framework pesado além do ponto de utilidade.
- **Ignorar os resultados:** subir a escada enquanto a entrega, a confiabilidade ou a segurança não melhoram.

## Modelo de maturidade

- **Nível 1, Iniciar.** Nenhuma noção compartilhada de maturidade. A capacidade é presumida, desigual e não medida. Qualquer avaliação é reativa, disparada por um incidente ou por uma exigência de auditoria e não planejada.
- **Nível 2, Desenvolver.** Algumas equipes rodam avaliações ad hoc contra alguma escala, mas o modelo, a cadência e o rigor variam de equipe para equipe. Os resultados são usados de modo inconsistente e a evidência é escassa, então pontuar pela aparência é um risco sempre presente.
- **Nível 3, Padronizar.** Um único modelo por capacidade e uma cadência de avaliação são documentados e aplicados em toda a organização. As avaliações são baseadas em evidências, envolvem as pessoas que fazem o trabalho e alimentam um backlog priorizado de melhorias e não um boletim.
- **Nível 4, Gerenciar.** A maturidade é medida e controlada com dados: o nível de cada capacidade é acompanhado contra uma linha de base, atrelado a uma métrica de resultado (incidentes, prazo de entrega, taxa de falha de mudanças) e reavaliado numa cadência definida, de modo que a deriva e a nota generosa aparecem como números e não como opiniões, e as metas são definidas deliberadamente por domínio contra risco e custo.
- **Nível 5, Orquestrar.** A avaliação é integrada em toda a organização e continuamente melhorada: maturidade, risco e resultados informam o investimento como um único quadro adaptativo, as metas são reequilibradas conforme as ameaças e o contexto mudam, os avaliadores têm rodízio ou checagem externa como rotina e a prática aposenta ativamente a cerimônia que já não merece o seu custo.

## Ideias para discussão

1. Quais das suas capacidades vocês estão presumindo maduras sem evidência?
2. Onde a sua menor maturidade coincide com o seu maior risco, e é para lá que vai o seu orçamento de melhoria?
3. Algum nível de maturidade na sua organização é uma meta ou um portão? Que comportamento isso produziu?
4. Qual é o nível-alvo certo para cada capacidade, e onde subir mais só acrescentaria burocracia?
5. As suas equipes reportariam a maturidade com honestidade, ou o modo como vocês usam as notas pune a franqueza?
6. Na última vez que vocês “melhoraram a maturidade”, os resultados de fato mudaram?

## Principais conclusões

- Um modelo de maturidade avalia a capacidade contra uma escada de níveis e descreve um caminho de melhoria: um espelho, não um troféu.
- Escolham modelos estabelecidos e baseados em evidências por domínio (CMMI, DORA, SAMM/BSIMM, CMMC). Uma escala leve por capacidade costuma ser a mais acionável.
- **Avaliem com honestidade, por capacidade**, e usem os resultados para **priorizar por risco**, não para classificar nem culpar.
- **Mais alto nem sempre é melhor:** definam os níveis-alvo deliberadamente contra risco e custo.
- Cuidado com o **teatro da maturidade** e com a **Lei de Goodhart**: um nível que vira meta deixa de medir a capacidade.
- Vejam o capítulo 12.4 para a autoavaliação consolidada de maturidade deste livro e a seção de maturidade de cada capítulo.

## Referências e leitura complementar

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
