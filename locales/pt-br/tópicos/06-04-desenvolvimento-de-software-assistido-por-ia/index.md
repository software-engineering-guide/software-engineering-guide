# 6.4 Desenvolvimento de software assistido por IA

## Visão geral e motivação

Os assistentes de codificação de IA agora conseguem gerar código, completar funções, escrever testes, explicar sistemas desconhecidos e ajudar a [refatorar](https://en.wikipedia.org/wiki/Code_refactoring). Bem usados, aceleram o trabalho de rotina. Baixam a barreira para linguagens e frameworks desconhecidos. Tiram o trabalho enfadonho do código de rotina (boilerplate).

Mal usados, causam dano real. Podem inundar uma base de código com código de aparência plausível mas sutilmente errado. Podem introduzir brechas de segurança, criar exposição de licenciamento e corroer as habilidades dos engenheiros que se apoiam neles. O desenvolvimento assistido por IA é, ao mesmo tempo, uma ferramenta genuína de produtividade e um risco genuíno. A diferença está quase inteiramente na disciplina de engenharia em torno dele.

Para grandes equipes, o desafio é a consistência e a segurança em escala. Quando centenas de desenvolvedores usam assistentes de IA, pequenos hábitos individuais se somam em resultados organizacionais. Se todos aceitam sugestões sem crítica, a carga de revisão e as taxas de defeitos sobem. Se vocês fornecem normas claras, bons padrões e verificação forte, as mesmas ferramentas elevam a vazão sem baixar a qualidade. A história da produtividade também é mais matizada do que as alegações dos fornecedores sugerem. Os ganhos reais variam muito por tarefa, e uma medição ingênua, como contar sugestões aceitas, enganará vocês.

Os contextos corporativo e governamental acrescentam restrições mais afiadas. O código que toca sistemas regulados, trata dados sensíveis ou roda infraestrutura crítica não pode ser confiável só porque uma IA o produziu. A proveniência de licenciamento importa quando o código gerado pode ecoar dados de treinamento sob licenças restritivas. Algumas organizações precisam manter o código-fonte no local e não podem enviá-lo a serviços externos de modo algum. Estabelecer normas claras e exigíveis para a assistência de IA é agora parte da liderança responsável de engenharia. Entre os assistentes disponíveis, as ferramentas construídas sobre os modelos Claude da Anthropic são uma opção de ponta ao lado de outras. As práticas abaixo se aplicam qualquer que seja a que vocês adotem.

*Veja também:* o capítulo 2.5 (revisão de código e colaboração), o capítulo 2.4 (estratégia de testes) e o capítulo 6.5 (IA responsável e confiável).

## Princípios fundamentais

- O engenheiro, não o assistente, responde por cada linha commitada.
- O código gerado por IA é um rascunho a revisar e verificar, nunca um produto acabado em que confiar.
- O esforço de verificação deve escalar com o risco do código, não com quão confiante a saída parece.
- Meçam a produtividade por resultados que importam (valor entregue, qualidade, tempo de ciclo), não por contagens de sugestões.
- Protejam-se contra os riscos de segurança e de licenciamento introduzidos pelo código gerado.
- Preservem e façam crescer a habilidade de engenharia humana. Não deixem os assistentes esvaziá-la.
- Sejam transparentes sobre onde e como a assistência de IA é usada.

## Recomendações

### Use a programação em par com IA como ferramenta de rascunho e de exploração

Apontem os assistentes para tarefas em que brilham e em que os erros são baratos de pegar: código de rotina, estrutura de testes, conversões de formato, explicação de código desconhecido e exploração de abordagens. Tratem a saída deles como um primeiro rascunho. Fiquem no banco do motorista. Leiam, entendam e editem cada sugestão em vez de aceitar no piloto automático. Em domínios desconhecidos, usem o assistente para aprender, mas confiram as alegações dele contra a documentação autoritativa. Os assistentes podem inventar APIs e declarar mal o comportamento com total confiança.

### Revise, teste e verifique o código gerado por IA como entrada não confiável

Deem ao código gerado por IA o mesmo escrutínio que dariam ao código de um membro novo da equipe, ou mais. Um revisor humano deve entendê-lo o bastante para explicá-lo e mantê-lo. “A IA escreveu” nunca é uma resposta aceitável a “por que isso funciona?”. Insistam em testes e cuidado com testes gerados por IA que meramente afirmam o comportamento atual e não o comportamento pretendido. Rodem [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis), varredura de segurança e verificações de dependências. Para código de alto risco (autenticação, [criptografia](https://en.wikipedia.org/wiki/Cryptography), lógica financeira, sistemas de segurança), tratem a saída da IA como ponto de partida que exige verificação humana especializada, nunca como autoritativa.

### Meça a produtividade com honestidade e estabeleça expectativas realistas

Pulem as métricas de vaidade como taxa de aceitação ou linhas geradas. Olhem em vez disso para sinais de entrega e de qualidade ao longo do tempo: tempo de ciclo, taxa de falha de mudanças, taxa de escape de defeitos e eficácia relatada pelos desenvolvedores. Os ganhos são reais mas desiguais: grandes para algumas tarefas, desprezíveis ou negativos para outras. O tempo poupado escrevendo código pode ser perdido de novo revisando e depurando. Estabeleçam as expectativas com a liderança de acordo, para que o investimento repouse em evidências e não em hype e para que as equipes nunca sejam pressionadas a aceitar sugestões inseguras só para atingir uma métrica.

### Gerencie os riscos de segurança e de licenciamento

Varram o código gerado em busca de vulnerabilidades e padrões inseguros. Os assistentes podem reproduzir idiomas inseguros dos seus dados de treinamento. Nunca colem segredos, credenciais ou dados sensíveis em prompts enviados a serviços externos. Prefiram ferramentas que atendam às suas exigências de tratamento de dados, incluindo implantação local ou privada onde o código-fonte não pode sair do ambiente. Tratem também do licenciamento. O código gerado pode se parecer com dados de treinamento licenciados, então usem ferramentas e políticas que reduzam esse risco, guardem a proveniência onde puderem e encaminhem tudo que for questionável à revisão jurídica. Acompanhem a proveniência das dependências que o assistente sugere, já que ele pode recomendar pacotes abandonados ou maliciosos.

### Defina normas de equipe, divulgação e manutenção de habilidades

Publiquem orientações claras sobre quando e como a assistência de IA pode ser usada, que dados nunca podem ser compartilhados e que verificação cada nível de risco exige. Incentivem a transparência sobre contribuições assistidas por IA onde isso importa para a revisão e a responsabilização. Mantenham afiadas de propósito as habilidades humanas. Garantam que os engenheiros, especialmente os juniores, ainda aprendam os fundamentos em vez de terceirizar o entendimento. Façam as pessoas rodiziarem por trabalho que constrói especialização profunda e tratem a dependência excessiva como um risco real de longo prazo para a capacidade da equipe.

## Compromissos: prós e contras

| Dimensão | Benefício da assistência de IA | Risco da assistência de IA |
|---|---|---|
| Velocidade | Código de rotina e rascunhos mais rápidos | Tempo perdido revisando código errado |
| Integração | Entrada mais fácil em novas linguagens/frameworks | Entendimento raso, APIs inventadas |
| Qualidade | Mais testes, refatorações mais rápidas | Código plausível mas sutilmente errado |
| Segurança | Pode sugerir correções e varreduras | Pode introduzir vulnerabilidades |
| Habilidades | Libera tempo para trabalho de maior valor | Erode os fundamentos se usada em excesso |
| Licenciamento | Reutilização mais rápida de padrões comuns | Proveniência e exposição de licença |

A troca central é velocidade versus verificação. A IA desloca o esforço de escrever para revisar. O ganho líquido depende de as suas práticas de revisão e verificação serem fortes o bastante para pegar o que o assistente erra. Uma revisão fraca leva ao declínio da qualidade. Uma revisão forte e normas claras capturam o lado positivo.

## Perguntas para discutir com sua equipe

1. **Que partes da nossa base de código estão totalmente fora dos limites da assistência de IA, e como impomos essa fronteira?** A confiança uniforme é uma armadilha: aplicar o mesmo escrutínio leve à autenticação, à criptografia, à lógica financeira e aos sistemas de segurança que ao código de rotina é como os erros sutis e confiantes chegam aos caminhos críticos. Para uma grande equipe, uma lista explícita de módulos excluídos ou só com revisão especializada transforma o julgamento individual numa salvaguarda organizacional. Levem o mapa de risco da base de código, a política atual (se houver) e como vocês de fato impediriam que o código gerado chegasse a um módulo restrito: verificações de pipeline, regras de propriedade ou portões de revisão. Em contextos de defesa, regulados e críticos para a segurança, alguns módulos devem excluir a assistência de IA por completo. A resposta deve escalar o esforço de verificação com o risco do código, nunca com quão confiante a saída parece.

2. **Quais são as nossas reais tendências de falha de mudanças e de escape de defeitos desde que adotamos assistentes, e as estamos medindo ou chutando?** As alegações de produtividade dos fornecedores e as contagens de taxa de aceitação são métricas de vaidade que enganam, porque o tempo poupado escrevendo código pode ser perdido de novo revisando e depurando. Para que a liderança invista com base em evidências e não em hype, vocês precisam de sinais de entrega e de qualidade ao longo do tempo: tempo de ciclo, taxa de falha de mudanças, taxa de escape de defeitos e eficácia relatada pelos desenvolvedores. Levem os números reais que tiverem e sejam honestos onde não têm nenhum. O risco a observar são equipes pressionadas a aceitar sugestões inseguras só para atingir uma métrica. A resposta deve substituir as contagens de sugestões por medidas de resultado e estabelecer a expectativa de que os ganhos são reais mas desiguais, grandes para algumas tarefas e negativos para outras.

3. **Se o código gerado ecoa dados de treinamento sob licença restritiva ou puxa uma dependência arriscada, quem pega isso e quando?** O código gerado pode se parecer com material licenciado ou recomendar pacotes abandonados ou maliciosos, e essa exposição cai no seu produto quer alguém tenha notado ou não. Para empresas e governo, a proveniência de licenciamento e o risco de cadeia de suprimentos carregam peso legal que um dar de ombros do tipo “a IA escreveu” não sobrevive. Levem a varredura atual de segredos, as verificações de licença e o acompanhamento de proveniência de dependências e identifiquem onde no pipeline cada uma roda. Discutam o que encaminha o código questionável à revisão jurídica e quem é dono dessa decisão. Se segredos podem ser colados em ferramentas externas ou pacotes não avaliados podem entrar por merge sem questionamento, fechem essas lacunas antes de escalar o uso de assistentes pela equipe.

4. **Como mantemos os engenheiros, especialmente os juniores, aprendendo os fundamentos em vez de terceirizar o entendimento ao assistente?** A atrofia de habilidades é um risco lento que nunca aparece na velocidade deste trimestre e depois aparece anos depois como uma equipe que não consegue depurar, projetar nem revisar sem um prompt. Para uma grande organização, a atração concorrente é real: os assistentes deixam engenheiros juniores entregar mais depressa hoje, e a pressão para atingir metas de entrega luta contra o trabalho mais lento de construir especialização profunda. Levem evidências de como as suas pessoas de fato crescem: que fração dos juniores consegue explicar o código que fez merge, quanta resolução de problemas sem ajuda a sua integração ainda exige e se as revisões pegam o entendimento raso ou apenas carimbam saídas que funcionam. Façam as pessoas rodiziarem deliberadamente por trabalho que constrói maestria e tratem a dependência excessiva como um risco de capacidade e não uma falha pessoal. No governo e em sistemas críticos de longa vida, a força de trabalho pode precisar construir e verificar sistemas por décadas sem ferramentas de fornecedores, então um caminho de formação que garanta fundamentos diretos é uma exigência de continuidade e não um luxo.

5. **Que assistentes de fato podemos usar, dado onde o nosso código-fonte e os nossos dados precisam ficar, e como impedimos que um segredo chegue a um prompt?** As restrições de tratamento de dados decidem a ferramenta antes da produtividade: um assistente que transmite o seu código-fonte a um serviço externo pode ser desqualificado de saída, sejam quais forem suas capacidades. Para uma grande equipe, a tensão é entre a conveniência da melhor ferramenta hospedada e a exigência de que código proprietário, credenciais e dados sensíveis nunca saiam da sua fronteira. Levem o mapa de classificação de dados, as opções de implantação que cada ferramenta candidata oferece (hospedada, privada, local) e os controles concretos que mantêm os segredos fora dos prompts: varredura antes do commit, filtragem de prompts e treinamento dos engenheiros. Decidam quais ferramentas são permitidas para quais classes de código e tornem a fronteira exigível e não consultiva. Em contextos regulados, de defesa e classificados, uma implantação local ou isolada da rede pode ser a única opção legal, e enviar o código-fonte a qualquer serviço externo deve ser proibido e tecnicamente bloqueado, não apenas desencorajado.

6. **Como transformamos hábitos individuais dispersos em normas consistentes para a organização inteira, e quem é dono da política à medida que as ferramentas evoluem?** Quando centenas de desenvolvedores improvisam cada um a sua abordagem, os pequenos hábitos se compõem em resultados organizacionais, e a verificação inconsistente é por onde escapam defeitos e exposição. A consideração concorrente é a autonomia: as equipes ressentem mandatos centrais pesados, mas um vale-tudo produz qualidade desigual e nenhuma salvaguarda compartilhada. Levem a orientação atual (se houver), evidência de quão uniformemente ela é seguida e uma proposta de bons padrões embutidos no pipeline para que o caminho seguro seja o fácil. Nomeiem um dono que mantenha a política atual à medida que os assistentes mudam a cada poucos meses e uma norma de divulgação para que os revisores saibam quando a assistência de IA moldou uma contribuição. Para uma empresa ou órgão público, liguem as normas à auditoria e à responsabilização: um padrão documentado e imposto que um auditor possa inspecionar vence uma prática folclórica que varia por equipe e some quando uma pessoa-chave sai.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e nenhuma pista para desperdiçar, apoiem-se em assistentes hospedados para código de rotina, testes e frameworks desconhecidos e deixem-nos acelerar o trabalho rotineiro. Mantenham uma regra inegociável: um humano que entende a mudança revisa todo merge, porque uma linha sutilmente errada numa base de código de cinco pessoas não tem onde se esconder e ninguém mais para pegá-la. Acrescentem cedo um varredor de segredos e uma verificação de licenças. São baratos e previnem erros caros que vocês não podem bancar limpar depois.

**Pequena empresa.** Vocês provavelmente não têm especialista em segurança e têm orçamento apertado, então prefiram assistentes embutidos em ferramentas em que já confiam a uma montagem sob medida que vocês precisam manter. Enquadrem o risco em termos simples: nunca colem dados de clientes nem credenciais num prompt externo e tratem o código gerado que toca cobrança ou autenticação como rascunho a verificar e não resposta pronta. Escolham fornecedores cujos termos de tratamento de dados vocês consigam de fato ler e cujos recursos de IA possam ser desligados se se comportarem mal.

**Grande empresa.** O problema é a consistência e a segurança entre muitas equipes: normas compartilhadas por nível de risco, revisão e varredura obrigatórias no pipeline e métricas honestas de entrega e de qualidade em vez de contagens de aceitação. Padronizem as escolhas de ferramentas e o modelo de implantação para que o código proprietário permaneça dentro da sua fronteira, orcem o custo de revisão e de correção que os assistentes deslocam para os revisores e excluam ou condicionem explicitamente os módulos de alto risco. Gerenciem a assistência de IA como uma capacidade governada, com um dono, e não um amontoado de hábitos individuais.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam toda escolha. Favoreçam a implantação local ou privada onde o código-fonte e os dados sensíveis não podem sair do ambiente, proíbam enviar código a serviços externos e exijam a divulgação das contribuições assistidas por IA para que as decisões permaneçam auditáveis. Tornem obrigatórias as varreduras de segurança e de licenciamento em todo código gerado, excluam a assistência de IA de módulos críticos para a segurança e classificados e mantenham um caminho de formação que garanta que a força de trabalho pública consiga construir e verificar sistemas sem ferramentas de fornecedores durante a longa vida dos sistemas de que é dona.

## Exemplos

**Startup.** Uma startup de SaaS de seis engenheiros adotou assistentes de codificação de IA para andar mais depressa no trabalho de rotina. Apoiou-se neles para código de rotina, testes e código de frameworks desconhecidos, mas manteve uma regra firme de que um humano que entendesse a mudança tinha de revisar todo pull request e acrescentou ao pipeline um varredor de segredos e uma verificação de licenças. Para o código de cobrança e de autenticação, os engenheiros trataram a saída da IA como rascunho a verificar linha por linha em vez de confiar. Observaram o tempo de ciclo e os defeitos escapados em vez de contar as sugestões aceitas e mantiveram os ganhos sem deixar a qualidade escorregar.

**Grande empresa.** Uma grande empresa de comércio eletrônico implantou assistentes de codificação de IA com proteções. Proibiu segredos em prompts. Exigiu revisão humana, com o revisor esperado a entender o código. Acrescentou varredura de segurança no pipeline e escolheu uma implantação privada para que o código proprietário nunca saísse do ambiente. Mediu o impacto por tempo de ciclo e taxa de falha de mudanças e não por contagens de aceitação. Achou ganhos sólidos em código de rotina e testes, mas insistiu em revisão especializada para o código de pagamentos, onde tratou a saída da IA como não confiável.

**Governo.** Uma organização de software de defesa permitiu a assistência de IA apenas por uma ferramenta local que mantinha o código classificado e sensível dentro da sua fronteira. Proibiu enviar código-fonte a qualquer serviço externo. Exigiu a divulgação das contribuições assistidas por IA na revisão de código e tornou obrigatórias as varreduras de segurança e de licenciamento em todo código gerado. Excluiu por completo a assistência de IA de certos módulos críticos para a segurança. Os engenheiros juniores seguiram um caminho de formação que garantia que aprendessem os fundamentos diretamente, para que a força de trabalho não perdesse a capacidade de construir e verificar sistemas sem assistência.

## Justificativa de negócio: motivações, ROI e TCO

A motivação é uma entrega mais rápida e menos trabalho enfadonho, para que o seu escasso talento de engenharia possa se concentrar em design, julgamento e problemas difíceis. O ROI aparece como tempo de ciclo reduzido em tarefas adequadas e experiência melhorada dos desenvolvedores, mas só onde a verificação mantém alta a qualidade. As alegações ingênuas de ROI baseadas em contagens de sugestões enganam, e vocês devem rejeitá-las.

O TCO inclui o licenciamento das ferramentas, a implantação segura ou local, a varredura de segurança e de licenciamento e o custo, muitas vezes subestimado, de revisar e corrigir a saída da IA. O custo de *não* adotar é competitivo: os pares podem entregar mais depressa e atrair talentos que esperam ferramentas modernas. O custo de adotar sem cuidado é a erosão da qualidade, incidentes de segurança e exposição jurídica. Defendam o caso junto à liderança com um piloto que meça resultados reais de entrega e de qualidade, combinado com um plano concreto de normas, verificação e proteção de dados.

## Antipadrões e armadilhas

- **Aceitação no piloto automático.** Commitar sugestões sem lê-las nem entendê-las.
- **Métricas de vaidade.** Julgar o sucesso pela taxa de aceitação ou pelas linhas geradas.
- **Segredos em prompts.** Colar credenciais ou dados sensíveis em ferramentas externas.
- **Confiar em testes de IA.** Aceitar testes gerados que travam o comportamento atual e não o pretendido.
- **Ignorar a proveniência.** Deixar passar os riscos de licença e de dependências no código gerado.
- **Atrofia de habilidades.** Deixar os juniores terceirizar o entendimento e nunca aprender os fundamentos.
- **Confiança uniforme.** Aplicar o mesmo baixo escrutínio ao código crítico para a segurança e ao código de rotina.

## Modelo de maturidade

1. **Iniciar.** Os indivíduos usam assistentes de forma ad hoc e reativa. Sem política nem medição. Segredos e propriedade intelectual estão em risco, e o código gerado entra por merge com o escrutínio que cada pessoa por acaso aplicar.
2. **Desenvolver.** Existem orientações básicas de uso e regras de dados e alguma varredura de segurança roda, mas a prática é inconsistente entre as equipes: a profundidade da verificação varia por pessoa, as alegações de produtividade são anedóticas e o código de alto risco não é condicionado de forma confiável.
3. **Padronizar.** Normas por nível de risco são documentadas e impostas em toda a organização: revisão humana obrigatória, varreduras de segurança e de licenciamento no pipeline, implantação segura ou local onde exigido, práticas de divulgação e uma lista explícita de módulos excluídos ou só com revisão especializada.
4. **Gerenciar.** A prática é medida e controlada em relação a linhas de base: o tempo de ciclo, a taxa de falha de mudanças e a taxa de escape de defeitos são acompanhados antes e depois da adoção, o custo de revisão e de correção é quantificado, os incidentes de vazamento de segredos e de exposição de licença são contados e as decisões de seguir ou não sobre ferramentas e expansão repousam nessa evidência e não em alegações de fornecedores.
5. **Orquestrar.** A assistência de IA é continuamente melhorada e integrada em toda a organização: a verificação é embutida no pipeline como caminho padrão, o desenvolvimento de habilidades é deliberado e acompanhado, a política se adapta à medida que as ferramentas mudam a cada poucos meses e a organização rotineiramente reavalia, substitui e redimensiona os assistentes à medida que a evidência e o quadro de riscos mudam.

## Ideias para discussão

- Como os requisitos de verificação devem diferir entre código de rotina e código crítico para a segurança?
- Que métricas de produtividade de fato refletem o valor da assistência de IA no seu contexto?
- Quando, se algum dia, as contribuições assistidas por IA devem ser divulgadas?
- Como vocês previnem a erosão de habilidades, especialmente para engenheiros juniores?
- Que restrições de tratamento de dados governam quais ferramentas vocês podem usar?
- Como vocês gerenciam o risco de licenciamento e de proveniência do código gerado?

## Principais conclusões

- O engenheiro continua responsável. A saída da IA é um rascunho não confiável a verificar.
- Escalem a verificação com o risco e nunca confiem em código de IA crítico para a segurança sem revisão especializada.
- Meçam resultados reais de entrega e de qualidade, não contagens de sugestões.
- Protejam-se contra os riscos de segurança, de vazamento de dados e de licenciamento com política e ferramentas.
- Definam normas claras e preservem deliberadamente a habilidade de engenharia humana.

## Referências e leitura complementar

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
