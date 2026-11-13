# 4.1 Fundamentos e cultura de segurança

## Visão geral e motivação

A segurança não é uma funcionalidade que se parafusa no fim, e não é o trabalho de uma equipe especializada sentada longe da engenharia. Numa grande organização, a segurança é uma propriedade de como o sistema inteiro é projetado, construído, operado e governado. Quando milhares de engenheiros entregam código em centenas de serviços, o elo mais fraco decide quanto dano um incidente pode causar. Um único bucket de armazenamento mal configurado, uma dependência sem correção ou uma conta de serviço com privilégios demais pode expor milhões de registros. Fundamentos e cultura são o que impede que isso aconteça em escala.

Para as empresas, as apostas são financeiras e de reputação: custos de violações, multas regulatórias, clientes perdidos e avaliações deprimidas. Para o governo, elas se estendem à segurança nacional, à confiança pública e à continuidade de serviços essenciais. Os dois contextos compartilham uma verdade dura: não se consegue impor a segurança puramente por controles e portões. Ela precisa ser internalizada pelas pessoas que fazem o trabalho. Uma cultura em que os engenheiros entendem as ameaças, sentem responsabilidade e são recompensados por levantar preocupações produz resultados muito melhores que uma que se apoia numa equipe de segurança sobrecarregada jogando de goleiro.

Este capítulo apresenta os modelos mentais e as práticas culturais que sustentam todos os outros capítulos de segurança deste guia. Ele cobre fazer da segurança trabalho de todos, a [modelagem de ameaças](https://en.wikipedia.org/wiki/Threat_model), o ciclo de vida de desenvolvimento seguro, princípios arquiteturais fundamentais como a [defesa em profundidade](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) e a [confiança zero](https://en.wikipedia.org/wiki/Zero_trust_security_model) e como priorizar o trabalho de segurança pelo risco real e não pelo medo ou pela moda.

*Veja também:* o capítulo 4.2 (segurança de aplicações), o capítulo 4.3 (segurança de infraestrutura e de nuvem), o capítulo 4.4 (operações de segurança) e o capítulo 4.6 (conformidade e governança) se apoiam nestes fundamentos.

## Princípios fundamentais

- **A segurança é trabalho de todos.** Cada engenheiro, gerente de produto e operador é dono da segurança do que constrói. A equipe de segurança viabiliza, aconselha e audita. Ela não faz, e não consegue fazer, o trabalho sozinha.
- **Presuma a violação.** Projete como se os atacantes já estivessem dentro. Minimize o que um componente comprometido consegue alcançar.
- **Defesa em profundidade.** Nenhum controle isolado basta. Sobreponha controles independentes para que a falha de um não signifique a falha de todos.
- **[Menor privilégio](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Conceda o acesso mínimo necessário, pelo tempo mínimo, e revogue-o automaticamente quando não for mais preciso.
- **Desloque para a esquerda (shift left).** Ache e corrija os problemas o mais cedo possível, quando são mais baratos de remediar.
- **Priorização baseada em risco.** Gaste esforço onde a combinação de probabilidade e impacto é maior, guiado pela tríade CIA (confidencialidade, integridade e disponibilidade), e não no que virou notícia nesta semana.
- **Aprendizado sem atribuição de culpa.** Trate incidentes de segurança e quase-acidentes como oportunidades de aprendizado, não como ocasiões de punição.

## Recomendações

### Estabeleça um programa de campeões de segurança

Embuta um campeão de segurança designado em cada equipe de engenharia. Os campeões não são especialistas de segurança em tempo integral. São engenheiros com treinamento extra e uma linha direta com a equipe central de segurança. Eles revisam designs, fazem a triagem de achados, respondem às perguntas dos colegas e levam o contexto de segurança ao planejamento. Isso escala a especialização em segurança pela organização sem contratar um especialista para cada equipe, e constrói confiança, porque o conselho vem de um par que de fato conhece a base de código.

Deem aos campeões apoio de verdade: um fórum regular para compartilhar o que aprendem, orçamento para treinamento e conferências, reconhecimento nas avaliações de desempenho e tempo reservado dos compromissos de entrega. Um programa de campeões que existe só no papel não produz nada.

### Pratique a modelagem de ameaças como rotina

A modelagem de ameaças é o hábito disciplinado de perguntar “o que pode dar errado?” antes de construir. Façam-na para novos serviços, grandes funcionalidades e qualquer mudança nas fronteiras de confiança. Mantenham-na leve o bastante para que aconteça com frequência.

- O **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** é uma lista de verificação prática mapeada para propriedades de segurança: Spoofing (autenticação), Tampering (integridade), Repudiation (não repúdio), Information disclosure (confidencialidade), Denial of service (disponibilidade) e Elevation of privilege (autorização). Percorram cada fluxo de dados e perguntem como cada categoria se aplica.
- O **PASTA** (Process for Attack Simulation and Threat Analysis) é um método de sete etapas, mais pesado e centrado em risco, que liga ameaças técnicas ao impacto no negócio. Usem-no para sistemas de alto valor.
- As **[árvores de ataque](https://en.wikipedia.org/wiki/Attack_tree)** decompõem um objetivo (“roubar dados de clientes”) nos passos ramificados que um atacante daria, ajudando a achar e podar caminhos.

Mantenham os modelos de ameaças como documentos vivos ao lado do código e revisitem-nos sempre que a arquitetura mudar.

### Construa um ciclo de vida de desenvolvimento seguro de software

Teçam a segurança em cada fase em vez de tratá-la como um portão final:

- **Requisitos:** capturem requisitos de segurança e de privacidade ao lado dos funcionais.
- **Design:** modelem as ameaças e revisem as fronteiras de confiança.
- **Implementação:** imponham padrões de codificação segura, revisão de código e varredura de segredos antes do commit.
- **Testes:** rodem [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (teste estático de segurança de aplicações), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (teste dinâmico de segurança de aplicações) e varredura de dependências no pipeline (veja o capítulo 4.4).
- **Lançamento:** verifiquem a proveniência, assinem os artefatos e confiram a configuração.
- **Operação:** monitorem, corrijam e respondam.

O ponto do shift left não é empilhar todo o trabalho mais cedo e sobrecarregar os engenheiros. É pegar os tipos de defeito que são muito mais baratos de corrigir cedo.

### Adote os princípios da arquitetura de confiança zero

A segurança tradicional de perímetro presume que tudo dentro da rede é confiável. Essa suposição falha no instante em que um atacante consegue uma brecha. A confiança zero substitui a confiança implícita na rede por verificação explícita e contínua: autentique e autorize toda requisição com base na identidade, na postura do dispositivo e no contexto, não importa de onde ela venha na rede. Combinem identidade forte, autorização de menor privilégio, microssegmentação e [criptografia](https://en.wikipedia.org/wiki/Encryption) em toda parte. A confiança zero é uma jornada, não um produto, então abordem-na um passo de cada vez.

### Priorize por risco usando a tríade CIA

Enquadrem cada ativo e controle em torno de **Confidencialidade**, **Integridade** e **Disponibilidade**. Nem todo dado precisa da mesma proteção: uma página pública de marketing e um banco de dados de prontuários têm necessidades de confidencialidade muito diferentes. Classifiquem os seus ativos, estimem a probabilidade e o impacto de um comprometimento e apontem o escasso esforço de segurança para as combinações de maior risco. Escrevam as suas decisões de risco para que outros possam revisá-las e defendê-las depois.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| A equipe central de segurança é dona de toda a segurança | Especialização profunda, padrões consistentes | Gargalo, os engenheiros se desengajam, não escala |
| Segurança distribuída (campeões) | Escala, constrói responsabilidade, feedback mais rápido | Exige investimento, habilidade desigual, precisa de coordenação |
| Modelagem de ameaças pesada e antecipada para tudo | Completa, pega falhas de design | Desacelera a entrega, pode virar preenchimento de caixas |
| Modelagem de ameaças leve e direcionada ao risco | Rápida, focada no que importa | Pode perder ameaças em sistemas de “baixo risco” |
| Portões rígidos que bloqueiam lançamentos | Impõe a conformidade | Atrito, incentiva gambiarras |

A tensão central é entre velocidade e garantia. Inclinem-se demais para portões e controle central e vocês criam um atrito que os engenheiros contornam, gerando TI sombra e ressentimento. Inclinem-se demais para a autonomia sem apoio e vocês obtêm uma segurança inconsistente e não auditada. A resposta sustentável é uma cultura forte com proteções habilitadoras: automatizadas onde possível, humanas onde o julgamento é necessário e sempre explicadas, nunca simplesmente impostas.

## Perguntas para discutir com sua equipe

1. **Quais dos seus sistemas merecem uma modelagem de ameaças pesada, e quem decide o nível?** Num parque grande não se consegue rodar uma análise PASTA de sete etapas em cada serviço, então vocês precisam de uma regra explícita sobre quando uma passada de 30 minutos de STRIDE basta e quando um sistema de alto valor merece uma modelagem profunda, guiada pelo impacto no negócio. Ancorem a decisão na sua classificação CIA: sistemas com registros regulados, fluxos de pagamento ou lógica de autenticação ficam no topo, e uma página pública de marketing não. Em trabalhos corporativos e governamentais, um auditor pedirá que vocês defendam por que um dado sistema foi modelado do jeito que foi, então escrevam os critérios dos níveis e nomeiem o responsável que os aplica. Levem a sua classificação atual de ativos e uma lista de serviços sem modelo de ameaças à reunião, porque a lacuna entre elas é o seu risco real. Se vocês não conseguem concordar quanto ao patamar, cairão em modelar tudo de leve ou nada a fundo, e as duas coisas falham com vocês.

2. **Quando um campeão de segurança e um prazo de entrega colidem, quem de fato pode parar o lançamento?** Um programa de campeões só muda resultados se o campeão tem autoridade de verdade, não apenas treinamento extra e boas intenções. Decidam de antemão se um campeão pode bloquear uma entrega, se escala para a equipe central de AppSec e que gravidade de achado justifica parar a entrega em vez de só acompanhá-lo. Isso importa mais sob pressão, quando um gerente de produto quer dispensar uma falha de design na semana anterior ao lançamento, que é exatamente quando as falhas não tratadas são mais caras de corrigir. Levem um exemplo recente em que uma preocupação de segurança encontrou um prazo e rastreiem quem decidiu e como, porque essa história revela o seu verdadeiro caminho de escalonamento. Se a resposta honesta é que a entrega sempre vence, os seus campeões são decorativos e vocês devem consertar o incentivo antes de acrescentar mais deles.

3. **O que “presuma a violação” muda concretamente na sua próxima revisão de design?** O princípio é fácil de aprovar com a cabeça e difícil de operacionalizar, então prendam-no a compromissos específicos: quais fronteiras de confiança vocês vão apertar, onde vão acrescentar microssegmentação e como vão encolher o que uma única conta de serviço comprometida alcança. Para uma grande equipe, o ganho é a redução do raio de impacto, para que um atacante que cai num serviço não consiga se deslocar para o repositório de dados atrás dele. Em contextos corporativos e governamentais isso também molda as decisões de menor privilégio e de credenciais de curta duração, que são baratas de projetar desde o início e dolorosas de adaptar depois. Levem um diagrama real de serviço e perguntem o que um atacante faz depois de dominar a camada web, depois comprometam-se com duas mudanças de contenção neste trimestre. Um acordo vago de que as violações acontecem não vale nada a menos que mova uma permissão, uma regra de rede ou a duração de uma credencial.

4. **Como vocês saberão que a sua cultura de segurança está de fato melhorando, e que métrica defenderiam diante do conselho?** As taxas de conclusão de treinamento e as contagens de chamados são fáceis de coletar e quase inúteis, porque medem atividade e não redução de risco, e uma grande organização se afoga nelas. Escolham métricas de resultado pelas quais vocês arriscariam um orçamento: a mediana do tempo para remediar achados de alta gravidade, a parcela de serviços com um modelo de ameaças atual, a fração de incidentes pegos antes da produção e a taxa de quase-acidentes autorrelatados, que deve subir à medida que a confiança cresce e não cair. A consideração concorrente é que toda boa métrica pode ser manipulada, então combinem cada uma com uma contramétrica e revisem a tendência e não o retrato. Levem o painel atual e perguntem quais números mudariam se a segurança de fato piorasse. Os que não mudariam são decoração. Em contextos corporativos e governamentais, um regulador ou comitê de auditoria pedirá evidência de que os controles funcionam, então escolham métricas que vocês possam defender sob escrutínio e não as que apenas parecem verdes.

5. **O que de fato acontece da próxima vez que um engenheiro relatar um erro, e o seu processo é sem atribuição de culpa na prática ou só no slide?** O aprendizado sem atribuição de culpa é o princípio mais professado e menos vivido, porque o primeiro incidente sério testa se a liderança realmente fala sério. Decidam de antemão como separam a responsabilidade por corrigir um problema da punição por tê-lo causado e quem conduz a revisão pós-incidente para que ela continue sendo sobre sistemas quebrados e não sobre indivíduos nomeados. A tensão é real: as partes interessadas querem alguém responsabilizado, mas punir quem relatou garante que o próximo erro continue escondido até virar uma violação. Levem as duas últimas revisões de incidentes e verifiquem se culparam uma pessoa ou um controle e se o engenheiro que deu o alarme foi agradecido ou discretamente deixado de lado. Para governos e empresas reguladas, as regras obrigatórias de divulgação de violações elevam as apostas, porque uma cultura que esconde erros também perderá os prazos de relato que carregam penalidades legais.

6. **Quem é dono do atrito das suas ferramentas de shift left, e vocês estão comprando, construindo ou se afogando nelas?** A análise estática e dinâmica automatizada, a varredura de dependências e a varredura de segredos são a espinha dorsal de um ciclo de vida de desenvolvimento seguro, mas um pipeline que inunda os engenheiros de falsos positivos os ensina a ignorar a saída de segurança, o que é pior que nenhuma varredura. Decidam quem ajusta as ferramentas, quem faz a triagem dos achados e se vocês compram uma plataforma integrada ou montam varredores de código aberto que depois terão de manter por conta própria. As considerações concorrentes são cobertura versus ruído e controle versus custo: um varredor barato que grita “lobo!” queima a confiança que um programa de campeões levou anos para construir. Levem a taxa atual de falsos positivos, o tempo médio que os engenheiros esperam por uma verificação bloqueante e a lista de equipes que desativaram um portão em silêncio. Em grandes empresas e no governo, acrescentem o ângulo da contratação e da proliferação de ferramentas, porque dez equipes comprando cada uma o seu varredor produzem uma cobertura inconsistente que nenhum auditor consegue conciliar.

## Perspectiva por setor

**Startup.** Sem equipe de segurança e com pouca pista, a cultura é o seu único controle acessível. Façam de uma lousa de modelagem de ameaças de 30 minutos o hábito antes de qualquer funcionalidade que toque autenticação ou pagamentos, liguem o menor privilégio e o MFA em toda parte porque não custam nada e mantenham um canal sem atribuição de culpa onde qualquer pessoa possa sinalizar uma preocupação. Pulem o processo e as ferramentas pesados: os engenheiros fundadores não conseguem mantê-los, e a disciplina que vocês constroem agora é o que permitirá aos compradores corporativos confiarem em vocês depois.

**Pequena empresa.** Vocês não têm especialista dedicado em segurança e têm orçamento apertado, então apoiem-se nos padrões seguros das ferramentas que já compram em vez de levantar o seu próprio pipeline. Favoreçam plataformas gerenciadas que impõem MFA, correções e menor privilégio por vocês e tratem a segurança como uma questão de higiene de dados: saibam que dados sensíveis guardam e quem consegue alcançá-los. Quando precisarem escolher entre construir e comprar, comprem, porque um controle gerenciado que vocês mantêm atualizado vence um sob medida que deixam apodrecer.

**Grande empresa.** Na escala de centenas de serviços e milhares de engenheiros, o desafio é a consistência e a governança entre muitas equipes. Conduzam um programa de campeões de segurança, padronizem níveis de modelagem de ameaças ligados à classificação CIA e forneçam modelos de caminho pavimentado e verificações automatizadas de pipeline para que cada equipe herde bons padrões. Acompanhem as métricas de remediação e de cobertura contra linhas de base e mantenham uma trilha de auditoria que mostre por que cada sistema foi modelado e controlado do jeito que foi.

**Governo.** As regras de contratação, as obrigações de transparência e a responsabilização pública moldam toda escolha. Os princípios de confiança zero e as credenciais de curta duração costumam ser exigidos por política executiva, e vocês precisam conseguir mostrar a um auditor uma justificativa documentada e baseada em risco de para onde foi o orçamento de endurecimento. Priorizem primeiro os sistemas que guardam os registros mais sensíveis de cidadãos, publiquem as salvaguardas onde o público tem o direito de saber e exijam que os fornecedores divulguem limitações em vez de aceitar caixas-pretas opacas.

## Exemplos

**Startup.** Uma startup de dez pessoas não tem equipe de segurança nem orçamento para uma, então os dois engenheiros fundadores fazem da modelagem de ameaças um hábito de lousa de 30 minutos antes de qualquer funcionalidade que toque autenticação ou pagamentos, perguntando o que pode dar errado e quem gostaria que desse. Eles adotam alguns hábitos fundamentais que não custam nada: menor privilégio em todo papel de nuvem, MFA em toda conta e um canal sem atribuição de culpa onde qualquer pessoa pode levantar uma preocupação sem medo de ser culpada. Quando depois levantam uma rodada e os compradores corporativos perguntam como tratam a segurança, aquela cultura inicial lhes permite responder com honestidade em vez de correr para inventar uma.

**Grande empresa.** Um banco global com 6.000 engenheiros conduz um programa de campeões de segurança com um campeão treinado por esquadrão. Os campeões participam de uma guilda mensal, completam treinamento trimestral e lideram a modelagem de ameaças de todo novo serviço usando STRIDE. A equipe central de AppSec mantém modelos de caminho pavimentado e verificações automatizadas de pipeline. Em dois anos, a mediana do tempo para remediar achados de alta gravidade caiu de 45 dias para 9, e a modelagem de ameaças na fase de design pegou uma falha de autorização numa API de pagamentos antes de chegar à produção, evitando um provável incidente de notificação obrigatória.

**Governo.** Uma autoridade tributária nacional que moderniza sistemas legados adota princípios de confiança zero exigidos por política executiva. Toda chamada de serviço interno é autenticada com credenciais de curta duração e autorizada por requisição. Os segmentos de rede já não conferem confiança. A agência modela as ameaças de cada serviço voltado ao cidadão contra árvores de ataque enraizadas em “exfiltrar registros de contribuintes” e “alterar uma declaração”. A priorização baseada em risco, alinhada aos níveis de impacto CIA, concentra primeiro o orçamento de endurecimento nos sistemas que guardam os registros mais sensíveis.

## Justificativa de negócio: motivações, ROI e TCO

O custo de construir uma cultura de segurança é real: tempo dos campeões, treinamento, ferramentas e o modesto arrasto de fazer modelagem de ameaças e revisões. Mas esse custo é pequeno ao lado do custo de não fazê-lo. A violação de dados grave média chega a milhões quando se contam a investigação, a notificação, a remediação, as multas regulatórias, a exposição jurídica e os negócios perdidos. As violações governamentais acrescentam a perturbação da missão e a erosão da confiança pública, que nenhuma fatura captura por completo.

O retorno do investimento em segurança vem de três lugares: **incidentes evitados** (a violação que nunca acontece), **menor custo de remediação** (os defeitos corrigidos na hora do design custam uma fração dos corrigidos em produção) e **entrega mais rápida** (caminhos pavimentados e verificações automatizadas permitem às equipes entregar com confiança em vez de esperar por revisão manual). Ao defender o caso junto à liderança, enquadrem a segurança como gerenciamento de riscos com preço, não como um bem abstrato. Mostrem a perda esperada (probabilidade vezes impacto) dos principais riscos, o custo de reduzi-los e o risco que ainda permanece. Os executivos financiam a redução de risco que conseguem medir.

## Antipadrões e armadilhas

- **Teatro de segurança.** Controles que parecem impressionantes mas não reduzem nenhum risco real, adotados para satisfazer uma auditoria e não para proteger algo.
- **A equipe de segurança como portão no fim.** Descobrir falhas de design na semana anterior ao lançamento, quando são mais caras de corrigir e mais prováveis de serem dispensadas.
- **Cultura de culpa.** Punir o engenheiro que relata um erro garante que o próximo erro continue escondido.
- **Modelagem de ameaças de preencher caixas.** Preencher um modelo que ninguém lê, produzindo documentos divorciados da arquitetura real.
- **Controles de tamanho único.** Aplicar o mesmo processo pesado a um site público e a um sistema de pagamentos, desperdiçando esforço e gerando ressentimento.
- **Priorização guiada pelo medo.** Perseguir qualquer vulnerabilidade que esteja em alta nas notícias em vez do que de fato ameaça os seus ativos.
- **Campeões só no nome.** Nomear campeões sem lhes dar tempo, treinamento ou autoridade.

## Modelo de maturidade

**Nível 1: Iniciar.** A segurança é reativa e centralizada. As revisões acontecem tarde, se acontecem, e não há modelagem de ameaças. Os incidentes conduzem correções ad hoc. Os engenheiros veem a segurança como problema de outra pessoa, e não existe padrão compartilhado.

**Nível 2: Desenvolver.** Existe uma equipe de segurança que define padrões, mas a prática é inconsistente entre as equipes. Alguma modelagem de ameaças acontece em grandes projetos e nenhuma em outros. Há treinamento básico disponível. A segurança ainda é percebida como um portão, e o shift left é aspiracional e não real.

**Nível 3: Padronizar.** Os campeões de segurança estão embutidos em todas as equipes. A modelagem de ameaças é rotina para novos serviços, em níveis ligados à classificação CIA, e o ciclo de vida de desenvolvimento seguro é documentado e imposto em toda a organização. A priorização baseada em risco guia o trabalho, os padrões de codificação segura e as verificações de pipeline são o caminho pavimentado padrão e as revisões pós-incidente sem atribuição de culpa são a norma.

**Nível 4: Gerenciar.** Os resultados de segurança são medidos e controlados em relação a linhas de base. A organização acompanha a mediana do tempo para remediar achados de alta gravidade, a cobertura de modelos de ameaças, a parcela de incidentes pegos antes da produção e as taxas de relato de quase-acidentes, detalhadas por equipe. A autoridade dos campeões para parar um lançamento é definida e de fato exercida. As decisões de risco são quantificadas como probabilidade vezes impacto, registradas e revisadas numa cadência fixa, de modo que as lacunas de controle aparecem como dados e não como surpresas.

**Nível 5: Orquestrar.** A segurança é genuinamente trabalho de todos e integrada à entrega, ao risco e ao planejamento de negócio. A modelagem de ameaças e o design seguro são habituais e leves, e os princípios de confiança zero estão em grande parte realizados. As métricas conduzem a melhoria contínua, a organização aprende com os quase-acidentes entre as equipes e os controles se adaptam automaticamente à medida que o quadro de ameaças e a arquitetura mudam.

## Ideias para discussão

1. Como vocês medem se uma cultura de segurança está de fato melhorando, além de contar conclusões de treinamento?
2. Onde fica a fronteira certa entre o que os campeões de segurança tratam e o que a equipe central possui?
3. Como vocês mantêm a modelagem de ameaças valiosa sem deixá-la virar uma caixa burocrática a marcar?
4. Uma arquitetura de confiança zero completa é realista para o seu parque legado e, se não, qual é o subconjunto pragmático?
5. Como o trabalho de segurança deve ser priorizado contra a entrega de funcionalidades quando os dois disputam os mesmos engenheiros?
6. Que incentivos de fato mudam o comportamento dos engenheiros rumo à responsabilidade pela segurança?

## Principais conclusões

- A segurança é uma propriedade cultural das grandes organizações, não uma tarefa delegada a uma equipe.
- Os campeões de segurança escalam a especialização e a responsabilidade por toda a engenharia.
- A modelagem de ameaças (STRIDE, PASTA, árvores de ataque) revela falhas de design cedo e barato.
- Um SDLC seguro e a mentalidade de shift left pegam defeitos quando custam menos.
- A defesa em profundidade, o menor privilégio e a confiança zero são os princípios arquiteturais fundamentais.
- A tríade CIA e a priorização baseada em risco dirigem o esforço escasso para onde ele mais importa.
- O custo de construir uma cultura de segurança é muito menor que o custo das violações que ela previne.

## Referências e leitura complementar

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modelling* and *Security Champions* guidance
