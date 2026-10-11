# 2.9 Construção de software

## Visão geral e motivação

A [construção de software](https://en.wikipedia.org/wiki/Software_construction) é onde o design se torna código em execução. É o trabalho detalhado de codificação, verificação, [testes unitários](https://en.wikipedia.org/wiki/Unit_testing), [testes de integração](https://en.wikipedia.org/wiki/Integration_testing) e [depuração](https://en.wikipedia.org/wiki/Debugging). O Guia do [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) trata a construção como uma área de conhecimento própria, e com razão: é aqui que acontece a maior parte do seu trabalho cotidiano. As escolhas que você faz linha a linha (como contém a complexidade, como trata erros, quão legível deixa as coisas) decidem se um sistema pode ser entendido, alterado e merecer confiança por anos.

Numa equipe grande, a construção é um esforço de grupo, não solitário. Centenas de engenheiros escrevem numa base de código compartilhada que sobreviverá ao tempo de qualquer pessoa na equipe. Então a barra não é “funciona na minha máquina hoje”. É “uma pessoa estranha consegue alterar isto com segurança daqui a cinco anos”. A construção se liga para cima aos requisitos (capítulo 2.8) e ao design (capítulo 2.2), que dizem o que construir e qual a sua forma. Liga-se para os lados aos padrões de codificação (capítulo 2.1), aos testes (capítulo 2.4) e à revisão de código (capítulo 2.5), que moldam como o trabalho é expresso, verificado e inspecionado. Uma boa construção transforma um design sólido num ativo mantível. Uma construção ruim transforma até um bom design num passivo.

Em contextos corporativos e governamentais, a construção carrega peso extra. Esses sistemas são de longa vida, fortemente regulamentados e muitas vezes críticos para a segurança ou para o cidadão. A [programação defensiva](https://en.wikipedia.org/wiki/Defensive_programming), o tratamento disciplinado de erros e o código obviamente correto não são requintes aqui: são requisitos de garantia, de auditoria e de continuidade ao longo de décadas e da rotatividade de pessoal. O objetivo é um código que comunique sua intenção, resista à falha e possa ser verificado. Código que apenas roda não basta.

## Princípios fundamentais

- Minimize a complexidade acima de tudo. O principal inimigo da construção em larga escala é o código que ninguém consegue entender por completo.
- Antecipe a mudança. Construa de modo que as prováveis modificações futuras sejam localizadas e baratas.
- Construa para a verificação. Escreva código cuja correção seja fácil de conferir por testes, revisão e raciocínio.
- Reutilize deliberadamente. Apoie-se em componentes existentes e confiáveis em vez de reinventar, mas evite o acoplamento às abstrações erradas.
- Siga padrões. A consistência em toda a base de código reduz o custo cognitivo de cada mudança futura.
- Trate erros e estados inválidos explicitamente. Torne visíveis os modos de falha em vez de silenciosos.
- Mantenha o código legível. Construir é comunicar-se primeiro com os futuros mantenedores e só depois com o compilador.

## Recomendações

### Minimize a complexidade como disciplina primária

Faça da redução da complexidade, essencial e acidental, o seu objetivo central. Escreva funções e módulos pequenos e de propósito único. Prefira nomes claros a truques engenhosos. Mantenha o aninhamento raso e o fluxo de controle linear. Localize as decisões para que entender um trecho de código não o obrigue a guardar o sistema inteiro na cabeça. A complexidade é o que torna as bases de código grandes lentas de mudar e perigosas de tocar, então pese cada escolha pela pergunta de se ela acrescenta complexidade ou a remove. Aplique também os princípios de design do capítulo 2.2 em pequena escala: alta coesão, baixo acoplamento e clara [separação de responsabilidades](https://en.wikipedia.org/wiki/Separation_of_concerns) importam tanto numa única função quanto numa arquitetura.

### Construa para a mudança e para a verificação

Pense adiante nas mudanças com maior probabilidade de vir (novas regras de negócio, novas integrações, novas regulamentações) e isole-as atrás de interfaces estáveis para que a mudança continue local. Ao mesmo tempo, escreva código fácil de verificar: [funções puras](https://en.wikipedia.org/wiki/Pure_function) (as mesmas entradas sempre produzem a mesma saída, sem efeitos colaterais) sempre que puder, o mínimo de estado oculto e dependências explícitas para que os testes possam substituí-las. Código difícil de testar costuma ser código difícil de entender e de mudar. A testabilidade (capítulo 2.4) é um sinal de design, não apenas uma preocupação de QA.

### Reutilize deliberadamente e padronize

Recorra a bibliotecas e componentes internos bem mantidos e confiáveis antes de reescrever lógica fundamental e use-os por meio de interfaces claras (capítulo 2.3). Construa componentes reutilizáveis apenas quando existir um segundo caso de uso genuíno, porque generalizar cedo demais é uma forma própria de complexidade. Aplique os padrões de codificação e de estilo da sua organização (capítulo 2.1) de modo uniforme, idealmente impostos por formatadores automáticos e [linters](https://en.wikipedia.org/wiki/Lint_(software)), para que toda a base de código seja lida como se um único autor cuidadoso a tivesse escrito.

### Pratique a programação defensiva com discernimento

Valide as entradas nas fronteiras de confiança (requisições externas, E/S de arquivos e de rede, entrada de usuário) e trate qualquer dado que cruze essas fronteiras como hostil até prova em contrário. Dentro de um módulo bem testado, porém, não sufoque cada linha em verificações redundantes que escondem a lógica e suprimem falhas reais. A regra é simples: defenda nas fronteiras, confie dentro delas. Use [asserções](https://en.wikipedia.org/wiki/Assertion_(software_development)) para documentar e impor invariantes que nunca deveriam ser falsas num programa correto. Use [exceções](https://en.wikipedia.org/wiki/Exception_handling) e o tratamento de erros para condições que podem legitimamente ocorrer em tempo de execução. Mantenha os dois separados: as asserções guardam premissas do programador, o tratamento de erros gerencia a falha esperada.

### Trate os erros explicitamente e falhe com segurança

Para cada erro, decida deliberadamente o que fazer: recuperar, tentar de novo, propagar ou falhar rápido. Nunca engula uma exceção em silêncio nem ignore um erro devolvido: uma falha suprimida volta depois como um defeito misterioso. Mantenha contexto nas mensagens de erro e nos logs para que as falhas possam ser diagnosticadas. Em sistemas críticos para a segurança e para o cidadão, falhe para um estado seguro e conhecido em vez de continuar num estado corrompido. Dê ao caminho de erro tanta atenção quanto ao caminho feliz, porque em produção é no caminho de erro que a confiança é ganha ou perdida.

### Embuta a qualidade durante a construção

A qualidade é embutida, não inspecionada depois. Escreva testes unitários junto com o código, rode a [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis) e os linters continuamente e mantenha as funções pequenas o bastante para raciocinar sobre elas. Use nomes e estrutura autoexplicativos para que seus comentários expliquem o porquê, não o quê. [Refatore](https://en.wikipedia.org/wiki/Code_refactoring) à medida que avança para manter o código habitável. A revisão de código (capítulo 2.5) é a última barreira humana, mas a maior parte da qualidade precisa estar lá antes mesmo de a revisão começar.

### Escolha e padronize as ferramentas de construção

Padronize a cadeia de ferramentas (compiladores, sistemas de build, formatadores, linters, analisadores estáticos, depuradores, gerenciadores de dependências e configurações de IDE) para que todo engenheiro trabalhe num ambiente consistente e reproduzível. Ligue essas ferramentas ao pipeline para que as verificações de qualidade não sejam opcionais. Traga ferramentas de programação assistida por IA deliberadamente e trate a saída delas como um rascunho que precisa passar pelos mesmos padrões, revisão e testes de qualquer outro código.

## Compromissos: prós e contras

| Prática | Prós | Contras |
|---|---|---|
| Minimização agressiva da complexidade | Legível, mutável, baixa taxa de defeitos | Pode parecer lenta. Risco de superabstração se mal aplicada |
| Muitas verificações defensivas | Pega estados ruins cedo, fronteiras robustas | Atravanca a lógica. Pode mascarar bugs reais se exagerada |
| Asserções para invariantes | Documenta e impõe premissas | Desativadas em algumas compilações de produção. Não é tratamento de erros |
| Muita reutilização de bibliotecas | Menos código para manter. Entrega mais rápida | Risco de dependência, acoplamento, exposição da cadeia de suprimentos |
| Padrões e linting estritos | Base de código uniforme e de baixo atrito | Configuração inicial. Pode parecer rígida a indivíduos |
| Construir para a testabilidade | Código verificável e mutável | Pode acrescentar indireção que alguns veem como cerimônia |

O compromisso central na construção é velocidade de curto prazo versus capacidade de mudança de longo prazo. Cortar caminho (pular o tratamento de erros, tolerar complexidade, ignorar padrões) parece mais rápido no momento e quase sempre é mais caro ao longo da vida do sistema. A falha oposta é a superengenharia: defensividade demais, abstração especulativa e generalidade de que ninguém precisa. A construção habilidosa vive no meio: tão simples quanto possível, tão defensiva quanto as fronteiras exigem, e não mais.

## Perguntas para discutir com sua equipe

1. **Qual é a nossa definição compartilhada e concreta de “complexo demais”, e onde a impomos antes da integração?** “Minimize a complexidade” é a disciplina central da construção, mas como slogan perde toda discussão para um prazo. Numa equipe grande em que centenas de pessoas escrevem numa só base de código, a complexidade precisa ser mensurável, então combinem os sinais sobre os quais vocês realmente agirão: tamanho da função, profundidade de aninhamento, complexidade ciclomática e o número de coisas que um leitor precisa guardar na cabeça para entender uma mudança. Leve seu pior caso à reunião e pergunte se a sua revisão atual o teria pegado. A resposta deve virar um portão de pipeline ou um item de lista de verificação da revisão, porque um limite imposto por uma ferramenta vale mais que um princípio imposto pela força de vontade, e poupa a sua próxima contratação do lento acúmulo de código que ninguém consegue tocar com segurança.

2. **Em produção, os nossos caminhos de erro se comportam como projetamos, e quando exercitamos um de propósito pela última vez?** O conselho de construção diz para dar ao caminho de erro tanta atenção quanto ao caminho feliz, mas o caminho de erro costuma ser o código menos testado que você possui, e num sistema crítico para o cidadão ou para a segurança é onde a confiança é ganha ou perdida. Uma exceção suprimida ou um código de retorno ignorado vira um defeito misterioso semanas depois, e “falhar para um estado seguro” é uma promessa que você não consegue cumprir se nunca viu isso acontecer. Leve o seu histórico de incidentes: quantas quedas passadas remontaram a um erro engolido ou a um caminho de recuperação não testado? A ação é testar a falha deliberadamente (injetar o cartão recusado, o tempo esgotado, a entrada malformada) e exigir que todo erro seja tratado, registrado com contexto ou propagado, nunca descartado em silêncio.

3. **Quais partes da nossa base de código são difíceis de testar, e o que essa dificuldade nos diz sobre o design?** O código que resiste ao teste é quase sempre código que esconde estado, se acopla às dependências erradas ou faz coisa demais, então a testabilidade é um sinal de design, não uma reflexão tardia de QA. Num sistema corporativo de longa vida isso importa porque os módulos que são dolorosos de testar hoje são os que uma pessoa estranha terá medo de mudar daqui a cinco anos. Leve a classe ou o serviço para o qual a sua equipe teme escrever testes e pergunte por quê: o estado está oculto, as dependências são impossíveis de substituir, a função faz três trabalhos? A resposta deve orientar a refatoração rumo a funções puras, dependências explícitas e unidades pequenas e de propósito único, porque tornar o código verificável é o mesmo trabalho que o tornar compreensível e barato de mudar.

4. **Quando reutilizamos uma biblioteca externa versus construímos a capacidade nós mesmos, e quem é responsável pelo risco da cadeia de suprimentos que assumimos?** Recorrer a uma biblioteca confiável é mais rápido que reinventar a lógica fundamental, mas toda dependência que você acrescenta é código que você não controla, não consegue auditar com facilidade e precisa corrigir no dia em que for comprometido. Numa equipe grande o perigo é cem engenheiros puxarem, cada um, as próprias dependências transitivas até ninguém conseguir dizer o que a base de código de fato executa. Leve o seu inventário de dependências e pergunte três coisas concretas: quantas bibliotecas estão sem manutenção, quantas carregam vulnerabilidades conhecidas e quantas envolvem uma lógica simples o bastante para você possuir por conta própria. A consideração concorrente é real, porque escrever a sua própria criptografia ou tratamento de datas é quase sempre pior que uma biblioteca testada em batalha, então o objetivo é uma política deliberada de reutilização e não a abstenção geral. Em contextos corporativos e governamentais, acrescente o ângulo de contratação e de conformidade de licenças, pois uma dependência não verificada pode carregar uma licença incompatível com as suas obrigações ou uma proveniência que nenhum auditor aceitará.

5. **Como submetemos o código gerado por IA aos mesmos padrões de construção do código escrito por humanos, e conseguimos distinguir os dois quando isso importa?** Os assistentes de codificação por IA produzem rascunhos plausíveis rapidamente, e a tentação é tratar a saída como acabada porque compila e parece idiomática. A regra do capítulo é que o código gerado passa pela mesma revisão, pelos mesmos testes e pelos mesmos padrões de qualquer outro, e uma equipe grande precisa tornar essa regra operacional e não aspiracional. Leve exemplos de mudanças assistidas por IA que foram entregues recentemente e pergunte se cada uma trazia testes, passou na análise estática e foi genuinamente entendida pela pessoa que a submeteu, ou se foi aprovada por confiança. A pressão concorrente é a velocidade, porque esses assistentes são genuinamente produtivos e fazer cada sugestão se arrastar joga fora o benefício. Em contextos regulamentados e governamentais, acrescente o ângulo de proveniência e de responsabilização, pois você pode ter de atestar quem é responsável por uma linha de código e se um fragmento gerado carrega uma questão de licença ou de direitos autorais que você não consegue responder.

6. **Nossa cadeia de ferramentas de construção está de fato padronizada e imposta no pipeline, ou as pessoas ainda trabalham em configurações incompatíveis?** Uma cadeia de ferramentas compartilhada de formatador, linter, analisador estático, sistema de build e gerenciador de dependências permite a um engenheiro transitar com confiança por serviços desconhecidos, porque o código é lido com uma só voz e as verificações são idênticas em toda parte. Quando ela deriva, cada equipe reinventa a própria configuração, o tempo de revisão é gasto discutindo estilo e defeitos que o analisador de uma equipe teria pegado passam na de outra. Leve a lista de repositórios que não rodam as verificações padrão a cada commit e pergunte por que cada um optou por sair. A tensão é que uma única configuração obrigatória pode parecer rígida a equipes com necessidades genuinamente diferentes, então decida onde a uniformidade vale o atrito e onde uma exceção documentada é aceitável. Para uma grande empresa ou órgão público, ligue isso à reprodutibilidade e à auditoria, porque um build que você não consegue reproduzir byte a byte a partir de uma cadeia de ferramentas controlada é um build que você não consegue defender diante de um avaliador anos depois.

## Perspectiva por setor

**Startup.** A velocidade vence, então ponha um formatador e um linter compartilhados no primeiro dia, valide as entradas na sua única fronteira externa e mantenha o código interno limpo em vez de defensivo em cada linha. Pule a abstração especulativa e o processo pesado: com duas ou três pessoas engenheiras a equipe inteira guarda a base de código na cabeça, e o risco real é a complexidade que sobrevive a essa memória compartilhada. Apoie-se em bibliotecas confiáveis para tudo que é fundamental, para escrever o mínimo de código que você consegue possuir bem.

**Pequena empresa.** Sem engenheiro de build dedicado e com orçamento apertado, prefira convenções que as suas ferramentas existentes impõem de graça: um formatador e um linter que acompanham a linguagem, padrões sensatos e um pequeno conjunto de regras que todos consigam lembrar. Compre ou adote bibliotecas bem mantidas em vez de construir infraestrutura que você não tem pessoal para manter. Gaste a sua disciplina limitada nas duas coisas que mais doem quando negligenciadas, validar a entrada na fronteira e nunca engolir um erro em silêncio.

**Grande empresa.** Com centenas de engenheiros escrevendo em código compartilhado, a prioridade é uniformidade e imposição: uma cadeia de ferramentas padrão ligada ao pipeline, portões de análise estática e regras de validação de fronteira aplicadas em toda parte, para que as pessoas transitem com confiança entre serviços. Gerencie o risco de dependências e da cadeia de suprimentos como um processo governado, e não como improviso por equipe, e use asserções para codificar invariantes de domínio que devem valer em todas as equipes. Trate os padrões de construção como o substrato que mantém uma base de código habitável ao longo de décadas e da rotatividade de pessoal.

**Governo.** Sistemas de longa vida e críticos para o cidadão fazem da construção disciplinada uma questão de garantia e de responsabilização. Isole as regras voláteis, como a legislação, atrás de interfaces estáveis para que a mudança continue local e rastreável até os requisitos, falhe para estados seguros e conhecidos em vez de continuar num estado corrompido e entregue todo módulo com testes que funcionem como evidência de auditoria. As obrigações de contratação e de transparência significam que a sua cadeia de ferramentas, as dependências e o tratamento de erros devem ser documentados o bastante para que um servidor público que chegue anos depois, ou um auditor externo, possa verificar que o código está correto.

## Exemplos

**Startup.** Uma startup de três engenheiros monta um formatador e um linter compartilhados no primeiro dia e os roda a cada commit, de modo que a base de código seja lida com uma só voz mesmo quando acrescentam terceirizados. Eles validam as entradas na fronteira da API e tratam tudo que vem de fora como hostil, mas mantêm a lógica interna limpa em vez de sufocá-la em verificações redundantes. Quando um webhook de pagamento começa a falhar, a correção é rápida porque nenhuma exceção foi engolida em silêncio e a mensagem de erro traz contexto suficiente para apontar direto a causa. Toda a configuração levou uma tarde e os poupou do lento acúmulo de complexidade que tornaria miserável a primeira semana da próxima contratação.

**Grande empresa.** Uma empresa global de pagamentos impõe uma cadeia de ferramentas compartilhada entre centenas de engenheiros: formatação e linting automáticos a cada commit, portões de análise estática no pipeline e uma regra de que todas as entradas externas são validadas nas fronteiras dos serviços. A lógica de domínio usa asserções para impor invariantes como “um lançamento contábil sempre fecha”, enquanto condições de tempo de execução como um cartão recusado são tratadas como desfechos explícitos e registrados. Como os padrões são uniformes e os erros nunca são engolidos em silêncio, os engenheiros transitam com confiança por serviços desconhecidos e os incidentes de produção podem ser diagnosticados direto dos logs.

**Governo.** Uma agência tributária nacional constrói um sistema de apuração de longa vida que deve funcionar por décadas sob legislação em mudança. A construção isola cada regra tributária atrás de uma interface estável, de modo que as mudanças legislativas anuais permaneçam locais e rastreáveis até os requisitos (capítulo 2.8). A validação defensiva protege toda entrada voltada ao cidadão. Os caminhos de erro falham para um estado seguro que nunca emite uma apuração incorreta em silêncio. Todo módulo é entregue com testes unitários como evidência de auditoria. Como a construção é padronizada e bem documentada, os novos servidores públicos conseguem manter com segurança código escrito por antecessores que saíram há muito tempo.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da construção disciplinada é a capacidade duradoura de mudar o software de forma barata e segura, e é aí que se decide a maior parte do custo total de propriedade de um sistema. Estudos de economia de software mostram de forma consistente que a maior parte do custo do ciclo de vida de um sistema é manutenção, e o custo de manutenção é dominado por quão compreensível e mutável é o código. Minimizar a complexidade, tratar erros explicitamente e seguir padrões reduzem diretamente o custo de cada mudança futura e de cada incidente em produção.

O custo de adoção é modesto e em grande parte inicial: definir os padrões, ligar os linters e analisadores e construir o hábito de escrever código verificável e defensivo. O custo da negligência, por outro lado, se acumula. A complexidade se acumula em código lento de mudar e arriscado de tocar. Erros silenciosos viram incidentes caros em produção. Um estilo inconsistente multiplica o esforço de cada revisão e de cada integração. Para defender o caso junto à liderança, ligue a qualidade da construção à taxa de falha de mudanças, ao tempo médio de recuperação, à taxa de escape de defeitos e ao tempo de integração, todos diretamente melhorados pela disciplina de construção.

## Antipadrões e armadilhas

- **Deslizamento de complexidade:** acumular código engenhoso, profundamente aninhado ou extenso até ninguém entendê-lo.
- **Engolir erros em silêncio:** blocos catch vazios e códigos de retorno ignorados que transformam falhas em futuros mistérios.
- **Exagero de programação defensiva:** verificações redundantes por toda parte que enterram a lógica e mascaram defeitos reais.
- **Confundir asserções com tratamento de erros:** usar asserções para condições de tempo de execução, ou exceções para invariantes do programador.
- **Construção por copiar e colar:** duplicar lógica em vez de reutilizar, de modo que as correções precisam ser feitas em muitos lugares.
- **Generalidade especulativa:** construir abstrações e configurabilidade para necessidades que nunca chegam.
- **Ignorar padrões:** cada engenheiro codificando à sua maneira, multiplicando a carga cognitiva na base de código.
- **Construção sem testes:** escrever código sem testes que o acompanhem, adiando a verificação para uma fase que nunca chega.

## Modelo de maturidade

- **Nível 1 (Iniciar):** A construção é ad hoc e reativa. A complexidade e o tratamento de erros variam por indivíduo. Poucos padrões existem e as falhas silenciosas são comuns.
- **Nível 2 (Desenvolver):** Existem padrões de codificação, formatadores e linters, e o tratamento básico de erros e os testes unitários são esperados, mas a prática é inconsistente e cada equipe a aplica de forma diferente.
- **Nível 3 (Padronizar):** A minimização da complexidade, a validação de fronteira, o tratamento explícito de erros e a testabilidade são documentados e impostos em toda a organização, no pipeline e na revisão, de modo que toda a base de código seja lida como se um único autor cuidadoso a tivesse escrito.
- **Nível 4 (Gerenciar):** A qualidade da construção é medida em relação a linhas de base. A equipe acompanha a complexidade ciclomática, a taxa de escape de defeitos, a taxa de falha de mudanças, a cobertura de testes dos caminhos de erro e as constatações da revisão de código e age sobre as tendências, e não sobre opiniões.
- **Nível 5 (Orquestrar):** A construção é continuamente melhorada e integrada em toda a organização. Os padrões defensivos, os padrões de codificação e as métricas realimentam a refatoração e as ferramentas. As ferramentas assistidas por IA funcionam sob os mesmos portões de qualidade, e a prática se adapta conforme linguagens, regulamentações e riscos mudam.

## Ideias para discussão

- Onde a complexidade acidental mais se acumula na sua base de código, e que hábitos de construção a criam?
- Qual é a regra real da sua equipe sobre onde validar as entradas e onde confiar nelas?
- Seus engenheiros distinguem asserções de tratamento de erros, e essa distinção é consistente?
- Quanto da sua qualidade é embutida durante a construção versus pega depois na revisão ou nos testes?
- Como você decide quando reutilizar uma biblioteca versus construir, dado o risco da cadeia de suprimentos?
- Como o código gerado por IA deve ser submetido aos mesmos padrões de construção do código escrito por humanos?

## Principais conclusões

- A construção é onde o design se torna código mantível. Minimizar a complexidade é a sua disciplina central.
- Construa para a mudança e para a verificação: código testável e mutável é código compreensível.
- Defenda nas fronteiras de confiança, confie dentro delas e nunca engula erros em silêncio.
- Use asserções para invariantes e o tratamento de erros para condições esperadas de tempo de execução. Não os confunda.
- Padronize ferramentas e estilo, reutilize deliberadamente e embuta a qualidade em vez de inspecioná-la depois.

## Referências e leitura complementar

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
