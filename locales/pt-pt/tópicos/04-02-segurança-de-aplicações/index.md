# 4.2 Segurança de aplicações

## Visão geral e motivação

A segurança de aplicações é onde as ameaças abstratas encontram o código concreto. A maioria das violações que chegam às manchetes remonta a uma falha na camada de aplicação: uma injeção, um fluxo de autenticação quebrado, um segredo exposto ou uma dependência comprometida. Para grandes equipes que entregam muitos serviços, a parte difícil não é saber que essas falhas existem. É preveni-las de forma consistente numa base de código espalhada, escrita por milhares de mãos ao longo de muitos anos.

Para as empresas, a segurança de aplicações é uma questão de confiança do cliente e de obrigação regulatória. Uma falha num fluxo de login ou num caminho de pagamento pode disparar fraude, multas e divulgação obrigatória de violação. Os sistemas governamentais enfrentam os mesmos riscos técnicos com dados de maior risco: elegibilidade a benefícios, registros tributários, dados da justiça criminal e infraestrutura nacional. Nos dois contextos, a aplicação é a porta da frente, e os atacantes a sondam constante e automaticamente.

Este capítulo cobre as práticas que mantêm as aplicações resilientes: conhecer e defender-se das classes comuns de vulnerabilidade, validar a entrada e codificar a saída, acertar a autenticação e a autorização, gerenciar segredos e proteger a cadeia de suprimentos de software, que cada vez mais determina a sua superfície de ataque real.

*Veja também:* o capítulo 4.1 (fundamentos de segurança, modelagem de ameaças e ciclo de vida de desenvolvimento seguro), o capítulo 10.3 (cadeia de suprimentos de código aberto e licenciamento) e o capítulo 10.2 (SBOMs, risco e garantia).

## Princípios fundamentais

- **Nunca confie na entrada.** Trate todo dado que cruza uma fronteira de confiança como hostil até ser validado.
- **Padrões seguros.** O caminho seguro deve ser o fácil. O comportamento inseguro deve exigir esforço deliberado e visível.
- **Falhe fechado.** Quando uma verificação de segurança não consegue terminar, negue o acesso em vez de permiti-lo.
- **Defesa em profundidade na camada da aplicação.** Combine validação, codificação, parametrização e proteções do framework. Não dependa de uma só.
- **Menor privilégio para identidades e tokens.** Delimite as credenciais de modo estreito e faça-as expirar depressa.
- **Suas dependências são o seu código.** Vocês respondem pela segurança de tudo que entregam, inclusive componentes de terceiros e de código aberto.
- **Padrões em vez de improviso.** Usem frameworks comprovados como o ASVS do [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) em vez de inventar seus próprios controles de segurança.

## Recomendações

### Conheça e defenda-se do OWASP Top 10, verifique com o ASVS

O OWASP Top 10 é a lista de referência do setor dos riscos mais críticos de aplicações web: controle de acesso quebrado, falhas criptográficas, injeção, design inseguro, configuração incorreta de segurança, componentes vulneráveis, falhas de autenticação, falhas de integridade de dados, falhas de registro e falsificação de requisição do lado do servidor. Tratem-no como conhecimento obrigatório para todo engenheiro, não apenas uma referência de conformidade a arquivar.

Para um padrão rigoroso e testável, adotem o **OWASP Application Security Verification Standard (ASVS)**. O ASVS define requisitos de segurança em três níveis de garantia, dando controles concretos e auditáveis contra os quais projetar e testar. Escolham o nível que se ajusta ao risco de cada aplicação e verifiquem contra ele.

### Valide a entrada e codifique a saída

As falhas de injeção continuam entre as mais danosas justamente porque são muito fáceis de introduzir. Defendam-se com controles em camadas:

- **Validem a entrada** contra listas de permissão estritas (tipo, comprimento, formato e faixa esperados). Rejeitem em vez de higienizar sempre que puderem.
- **Usem consultas parametrizadas** e [instruções preparadas](https://en.wikipedia.org/wiki/Prepared_statement) em todo acesso a banco de dados. Nunca montem SQL por concatenação de cadeias. Usem construtores de consultas e ORMs (mapeadores objeto-relacional) seguros, e corretamente.
- **Codifiquem a saída** de acordo com o contexto. HTML, atributos HTML, JavaScript, URLs e CSS exigem cada um uma codificação diferente. Apoiem-se no escape automático do framework e entendam os limites dele.
- **Previnam o [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** com codificação de saída mais uma Content Security Policy forte como segunda camada.
- **Previnam a injeção de comandos e de modelos** evitando chamar o shell com dados não confiáveis e usando modelos sem lógica ou isolados.

### Acerte a autenticação e a autorização

A autenticação prova quem é o usuário. A autorização decide o que ele pode fazer. As duas falham com frequência, então acertem-nas.

- Prefiram protocolos estabelecidos: o **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** para autorização delegada e o **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** para autenticação. Não os construam do zero.
- Imponham a **[autenticação multifator](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, em especial para o acesso privilegiado e administrativo.
- Guardem senhas apenas como hashes com sal, usando um algoritmo moderno, lento e que exige muita memória (como o [Argon2](https://en.wikipedia.org/wiki/Argon2) ou o [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Nunca guardem nem registrem credenciais em texto puro.
- Gerenciem as **sessões** com cuidado: gerem tokens criptograficamente fortes, definam os sinalizadores de cookie secure e HttpOnly, rotacionem na mudança de privilégio e expirem as sessões ociosas.
- Imponham a **autorização no servidor em toda requisição**, verificando se o principal autenticado é dono do recurso específico ou pode acessá-lo. A autorização quebrada em nível de objeto (acessar o registro de outro usuário mudando um ID) é uma das falhas de API mais comuns e graves.
- Centralizem a lógica de autorização onde for prático, para que a política seja consistente e auditável.

### Gerencie segredos e rotacione chaves

Os segredos fixos no código-fonte são uma causa perene de violações. Construam um hábito disciplinado de gerenciamento de segredos:

- Guardem os segredos num gerenciador de segredos ou cofre dedicado, nunca no código-fonte, em arquivos de configuração nem em variáveis de ambiente versionadas.
- Varram commits e repositórios em busca de segredos vazados automaticamente e bloqueiem os merges que os introduzam.
- Rotacionem chaves e credenciais regularmente e imediatamente diante de qualquer suspeita de exposição. Prefiram credenciais de curta duração, emitidas automaticamente, às estáticas de longa duração.
- Apliquem o menor privilégio a todo segredo: delimitem-no ao exato que ele precisa.
- Criptografem os segredos em repouso e em trânsito e auditem o acesso a eles.

### Proteja a cadeia de suprimentos de software

As aplicações modernas são em sua maioria montadas a partir de componentes de terceiros, o que faz da cadeia de suprimentos uma superfície de ataque primária.

- Mantenham uma **[lista de materiais de software](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** para cada aplicação, para saber exatamente o que entregam e poder responder depressa quando uma nova vulnerabilidade chegar.
- Varram continuamente as dependências (análise de composição de software, ou SCA) e remedeiem prontamente os componentes sabidamente vulneráveis.
- Fixem e verifiquem as versões das dependências. Usem arquivos de trava (lockfiles) e registros confiáveis.
- Adotem o **SLSA** (Supply-chain Levels for Software Artifacts) para elevar a integridade do build e gerem atestados de **proveniência** descrevendo como os artefatos foram construídos.
- **Assinem os artefatos** e verifiquem as assinaturas antes da implantação para poder confiar que o que roda é o que vocês construíram.
- Protejam o próprio sistema de build. Um pipeline de CI comprometido pode injetar código malicioso em todo consumidor a jusante.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| Comprar/adotar um provedor de identidade (OIDC) | Testado em batalha, MFA embutida, menos código para proteger | Dependência de fornecedor, esforço de integração, custo |
| Construir autenticação própria | Controle total, sem dependência externa | Extremamente fácil de errar, alta manutenção |
| Validação estrita por lista de permissão | Bloqueia classes inteiras de vulnerabilidade | Pode quebrar casos de borda legítimos, mais trabalho inicial |
| Credenciais de curta duração | Janela pequena de violação, revogação automática | Exige infraestrutura robusta de emissão |
| Atualizações agressivas de dependências | Menos vulnerabilidades conhecidas | Agitação, possíveis quebras, ônus de testes |
| SBOM + assinatura + proveniência | Resposta rápida a incidentes, confiança verificável | Investimento em ferramentas e processo, mudança cultural |

A troca recorrente é rigor inicial versus exposição contínua. Construir autenticação própria ou pular a higiene das dependências parece mais rápido hoje e custa enormemente depois. Adotar padrões comprovados e controles automatizados de cadeia de suprimentos custa esforço agora, mas transforma um risco ilimitado e imprevisível num gerenciado e limitado. Para grandes equipes, o multiplicador da automação é o que mais importa: um controle aplicado uma vez num modelo de caminho pavimentado protege todo serviço que o usa.

## Perguntas para discutir com sua equipe

1. **Quais controles do ASVS vocês vão embutir no seu framework de caminho pavimentado para que os engenheiros os recebam de graça?** O movimento de maior alavancagem para uma grande equipe é fazer do caminho seguro o padrão, para que um controle escrito uma vez num framework compartilhado proteja todo serviço que o adota. Decidam quais requisitos do ASVS (consultas parametrizadas, codificação de saída, sinalizadores seguros de sessão, verificações de autorização no servidor) pertencem ao modelo e não à memória de cada engenheiro. Em portfólios corporativos e governamentais, decidam também quais aplicações precisam do ASVS Nível 2 versus Nível 3 e liguem isso à sensibilidade dos dados que cada uma toca. Levem uma lista dos seus serviços e marquem quais já herdam esses padrões e quais reimplementam a segurança à mão, porque os feitos à mão são onde a injeção e o controle de acesso quebrado se escondem. Se os padrões seguros vivem apenas numa página de wiki, serão pulados sob pressão de entrega, então ponham-nos no código.

2. **Como vocês vão achar e corrigir a autorização quebrada em nível de objeto em toda API, e não apenas nas novas?** Acessar o registro de outro usuário mudando um ID é uma das falhas de API mais comuns e graves, e se esconde nos endpoints mais antigos que antecedem os seus padrões atuais. A autorização no servidor em toda requisição e em todo objeto é a regra, mas a parte difícil é verificar que ela se sustenta numa base de código espalhada, com anos, escrita por muitas mãos. Decidam se vão centralizar a lógica de autorização, acrescentar testes automatizados que tentam o acesso entre locatários ou fazer testes direcionados primeiro contra as APIs de maior risco. Levem o inventário de endpoints que expõem identificadores de objeto e classifiquem-nos pela sensibilidade do que devolvem. Sem uma varredura deliberada, vocês continuarão entregando essa falha e só a descobrirão quando um pesquisador ou um atacante a descobrir.

3. **Qual é o plano de vocês para a próxima vulnerabilidade de dependência disseminada: com que rapidez vocês conseguem achar e corrigir todo serviço afetado?** Quando uma falha crítica chega a uma biblioteca popular, as empresas com uma SBOM exata identificam os serviços afetados em horas enquanto outras passam semanas procurando, e essa diferença de velocidade decide quanto dano vocês sofrem. Decidam agora se produzem uma lista de materiais de software para cada artefato, se a varredura de dependências roda em todo pipeline e quem é dono da decisão de correção emergencial. Para compradores regulados e governamentais, as SBOMs e a proveniência assinada são cada vez mais condição para fazer negócio, então essa prontidão também protege a receita. Levem a resposta honesta a um exercício: escolham uma biblioteca que usam amplamente e cronometrem quanto leva para listar todo serviço que a entrega. Se a resposta se mede em dias, invistam em inventário e assinatura antes que o próximo incidente os force.

4. **Como vocês vão passar de segredos estáticos de longa duração para credenciais de curta duração emitidas automaticamente, e quais sistemas bloqueiam isso hoje?** Os segredos fixos e de longa duração são uma causa perene de violações, e a correção, credenciais de curta duração emitidas sob demanda, depende de uma infraestrutura de emissão que os sistemas mais antigos muitas vezes não conseguem usar. Para uma grande equipe o perigo é a adoção desigual: uma plataforma moderna rotaciona as chaves a cada hora enquanto um serviço legado ainda entrega uma senha estática de banco de dados num arquivo de configuração. Decidam quais cargas de trabalho podem consumir agora um gerenciador de segredos ou um sistema de identidade de carga de trabalho, quais precisam de investimento primeiro e quem é dono do runbook de rotação no instante em que se suspeita do vazamento de uma chave. Levem um inventário de toda credencial em uso, sua duração, seu raio de impacto se exposta e se a varredura de commits a pegaria antes do merge. Em contextos corporativos e governamentais, liguem isso à auditoria: os examinadores esperam cada vez mais evidência de rotação, acesso delimitado e registro de acesso para todo segredo, e uma credencial estática que vocês não conseguem rotacionar sem indisponibilidade é um achado esperando para ser escrito.

5. **Onde vocês ainda rodam autenticação caseira ou inconsistente, e qual é o plano para consolidar em protocolos comprovados?** Construir autenticação é um dos jeitos mais fáceis de introduzir falhas sutis e exploráveis, e ainda assim a maioria dos grandes parques carrega ao menos um fluxo de login legado que antecede a decisão de padronizar em OAuth 2.0 e OIDC. As pressões concorrentes são reais: migrar um fluxo antigo arrisca quebrar usuários e integrações existentes, enquanto deixá-lo no lugar mantém um alvo de alto valor mal defendido. Decidam se consolidam num único provedor de identidade, impõem MFA de modo uniforme e fixam um prazo para aposentar cada fluxo sob medida, ou se aceitam exceções documentadas com controles compensatórios. Levem um mapa de todo caminho de autenticação da frota, quais impõem MFA, quais guardam senhas com um hash moderno que exige memória e quais são personalizados. Para portfólios corporativos e governamentais, acrescentem o ângulo da conformidade: padrões como o NIST SP 800-63 estabelecem expectativas concretas de garantia de identidade, e um fluxo caseiro que não consegue demonstrá-las não sobreviverá a uma auditoria nem a uma revisão de autorização para operar.

6. **Como vocês verificam que esses controles de fato se sustentam em produção, e conseguem provar com evidência e não com asserção?** Escrever um padrão seguro não é o mesmo que saber que todo serviço ainda o honra, e os controles apodrecem em silêncio à medida que o código muda, as exceções se acumulam e novos endpoints são entregues. Para uma grande equipe a pergunta é a cobertura: quais serviços rodam análise estática, varredura de dependências e testes dinâmicos ou de intrusão, e como vocês sabem que os que pulam isso não são as suas aplicações de maior risco? Decidam que verificação é obrigatória no pipeline versus periódica, quem faz a triagem dos achados e que evidência vocês retêm para mostrar que um controle foi testado e passou numa dada data. Levem o mapa atual de cobertura, o tempo médio de remediação por gravidade e a lista de aplicações sem teste recente. Em contextos regulados e governamentais essa evidência não é opcional: auditores, autoridades autorizadoras e investigadores de violações pedem todos prova de que os controles foram verificados, e uma política sem registros de testes raramente os satisfaz.

## Perspectiva por setor

**Startup.** Com duas ou três pessoas de engenharia e nenhum especialista em segurança, a sua alavancagem é herdar a segurança em vez de construí-la: adotem um provedor OIDC gerenciado, apoiem-se num framework cujo ORM parametriza as consultas por padrão e guardem os segredos no gerenciador de segredos da plataforma e não em arquivos `.env` que um colega pode commitar por acidente. Liguem a varredura automatizada de dependências que abre pull requests de correção e tratem isso como suficiente por ora. Não construam autenticação nem criptografia próprias, porque uma única consulta injetada ou uma chave vazada pode acabar com a empresa antes de ela ter clientes.

**Pequena empresa.** Vocês provavelmente não têm especialista em segurança de aplicações e têm orçamento apertado, então comprem controles embutidos nas ferramentas e plataformas que já pagam em vez de pôr gente numa função dedicada. Escolham um provedor de identidade hospedado com MFA incluída, um banco de dados gerenciado que os conduza ao acesso parametrizado e um host de repositório que varre commits em busca de segredos vazados de fábrica. Concentrem a atenção escassa nos básicos do OWASP Top 10 que causam a maioria das violações do mundo real e prefiram fornecedores que entregam padrões seguros que vocês não consigam desligar casualmente.

**Grande empresa.** Entre muitas equipes o desafio é a consistência: embutam os controles do ASVS em frameworks de caminho pavimentado para que todo novo serviço herde de graça consultas parametrizadas, codificação de saída, sessões seguras e autorização no servidor. Mantenham SBOMs exatas e varredura de dependências em toda a frota para que a próxima vulnerabilidade de biblioteca disseminada seja questão de horas e não de semanas e centralizem a política de autorização para que o acesso entre locatários se torne testável. Padronizem num provedor de identidade com MFA imposta e gerenciem a segurança de aplicações como um portfólio governado, com níveis de ASVS por risco e evidência auditada.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam os controles que vocês precisam demonstrar, e não apenas implementar. Verifiquem os serviços voltados ao cidadão contra o OWASP ASVS num nível proporcional à sensibilidade dos dados, assinem todo artefato implantado e atestem sua proveniência segundo o SLSA para satisfazer os mandatos de cadeia de suprimentos e emitam credenciais de curta duração a partir de um cofre central, com registro completo de acesso. Esperem mostrar a auditores e autoridades autorizadoras uma cadeia de custódia documentada do código-fonte à produção e alinhem a garantia de identidade a padrões publicados como o NIST SP 800-63.

## Exemplos

**Startup.** Uma equipe de SaaS com três engenheiros pula a construção do próprio login e adota um provedor OIDC gerenciado desde o primeiro dia, ganhando MFA e redefinições seguras de senha sem escrever código crítico para a segurança que não pode bancar errar. Apoia-se no ORM do framework para que as consultas sejam parametrizadas por padrão, guarda os segredos no gerenciador de segredos da plataforma em vez de em arquivos `.env` que um colega pode commitar por acidente e liga a varredura automatizada de dependências que abre um pull request quando uma biblioteca precisa de correção. Nada disso desacelera a equipe, e significa que uma chave vazada ou uma consulta injetada não acaba com a empresa antes de ela ter clientes.

**Grande empresa.** Uma plataforma de varejo que atende dezenas de milhões de compradores padroniza a autenticação em OIDC por meio de um único provedor de identidade, impondo MFA para a equipe e autenticação escalonada para mudanças de conta de alto valor. Todo acesso a banco de dados passa por um ORM configurado para parametrizar as consultas, e uma Content Security Policy reforça a codificação de saída. Depois de uma vulnerabilidade amplamente divulgada numa biblioteca popular de logging, a SBOM da empresa permite identificar todo serviço afetado em horas e corrigi-los em dois dias, enquanto concorrentes sem inventário passaram semanas procurando.

**Governo.** Uma agência federal de benefícios constrói serviços voltados ao cidadão verificados contra o OWASP ASVS Nível 2, com Nível 3 para os componentes que tratam os registros mais sensíveis. Os segredos vivem num cofre central que emite credenciais de curta duração, e a varredura de commits bloqueia qualquer chave vazada. Todo artefato implantado é assinado e sua proveniência é atestada segundo o SLSA, satisfazendo um mandato federal de cadeias de suprimentos de software verificáveis e dando aos auditores uma cadeia de custódia clara do código-fonte à produção.

## Justificativa de negócio: motivações, ROI e TCO

O gasto em segurança de aplicações reduz a categoria de violação mais provável e mais cara. O custo total de propriedade inclui ferramentas (varredores, gerenciadores de segredos, provedores de identidade), o tempo de engenheiro para remediar os achados e o leve atrito dos padrões seguros. Contra isso, pesem o custo de pular tudo: as violações por injeção e por controle de acesso quebrado rotineiramente expõem milhões de registros, disparando multas regulatórias, notificação obrigatória, perdas por fraude, sprints de remediação e dano de reputação que suprime a receita por anos.

O ROI é mais forte quando os controles são automatizados e reutilizados. Uma única integração de identidade bem configurada, uma camada de consultas endurecida num framework compartilhado e um pipeline que bloqueia dependências vulneráveis protegem a frota inteira a um custo marginal por serviço. Os controles de cadeia de suprimentos em particular passaram de opcionais a essenciais: uma dependência comprometida pode transformar cada um dos seus clientes numa vítima, e os reguladores e compradores corporativos exigem cada vez mais SBOMs e proveniência assinada como condição para fazer negócio. Ao defender o caso junto à liderança, liguem o investimento a riscos específicos e nomeados e a exigências de contratação e de conformidade que bloqueiam receita se vocês não as atenderem.

## Antipadrões e armadilhas

- **Criar a própria criptografia ou autenticação.** Quase sempre produz falhas sutis e exploráveis.
- **Validação só no cliente.** Contornada trivialmente. O servidor precisa revalidar tudo.
- **Higienização por lista de bloqueio.** Tentar remover caracteres “ruins” em vez de permitir por lista os bons. Os atacantes acham as brechas.
- **Segredos no código-fonte ou em arquivos de ambiente.** A causa mais comum de vazamentos de credenciais.
- **Ignorar a autorização no acesso a objetos.** Presumir que um usuário autenticado pode acessar qualquer objeto cujo ID consiga adivinhar.
- **Dependências de configurar e esquecer.** Nunca atualizar componentes de terceiros até uma violação forçar.
- **Tratar o Top 10 como linha de chegada.** É um piso, não um padrão abrangente. Usem o ASVS para profundidade.
- **Registrar dados sensíveis.** Senhas, tokens e PII (informações de identificação pessoal) nos logs viram uma violação à espera de acontecer.

## Modelo de maturidade

**Nível 1: Iniciar.** A segurança de aplicações depende do conhecimento individual dos desenvolvedores e só reage depois de incidentes. Não há controles padrão. Os segredos ficam no código-fonte. As dependências raramente são atualizadas. A autenticação é personalizada e ad hoc, e as falhas de injeção ou de controle de acesso quebrado são achadas por sorte e não por processo.

**Nível 2: Desenvolver.** Aparecem práticas básicas, mas variam de equipe para equipe. A consciência do OWASP Top 10 se espalha, algumas proteções no nível do framework estão no lugar e existe um gerenciador de segredos, mas usado de forma desigual. A varredura de dependências roda ocasionalmente. Os novos sistemas adotam um provedor de identidade padrão, enquanto os serviços mais antigos mantêm intocados seus fluxos de login caseiros.

**Nível 3: Padronizar.** Os controles são documentados e impostos em toda a organização. Requisitos baseados no ASVS são definidos por nível de risco, as consultas parametrizadas e a codificação de saída são a norma e um provedor central de identidade com MFA é exigido. Os segredos são gerenciados e varridos automaticamente, as SBOMs são produzidas e a varredura de dependências roda em todo pipeline.

**Nível 4: Gerenciar.** A prática é medida e controlada em relação a linhas de base. A cobertura de varreduras e de testes, o tempo médio de remediação por gravidade, a parcela de serviços que herdam os padrões do caminho pavimentado, a idade de rotação de credenciais e segredos e a conformidade com o ASVS são todos acompanhados em painéis. As exceções são registradas com datas de validade, o desvio da linha de base dispara ação e os lançamentos são condicionados a limiares definidos de segurança e não a julgamentos.

**Nível 5: Orquestrar.** A segurança é continuamente melhorada e integrada em toda a organização. Os padrões seguros são embutidos em frameworks de caminho pavimentado para que o caminho seguro seja automático, as credenciais de curta duração são usadas em toda parte e a garantia completa da cadeia de suprimentos com assinatura e proveniência (SLSA) é padrão. A verificação é contínua, a resposta a novas vulnerabilidades é rápida e medida e cada incidente realimenta os modelos compartilhados, de modo que uma única correção endurece a frota inteira.

## Ideias para discussão

1. Onde a lógica de autorização deve viver para ser ao mesmo tempo consistente e mantível em muitos serviços?
2. Com que agressividade vocês devem atualizar as dependências, dada a troca entre exposição e agitação?
3. Qual nível de ASVS é apropriado para cada classe de aplicação do seu portfólio?
4. Como vocês eliminam segredos de longa duração sem criar uma infraestrutura frágil de emissão?
5. O que seria preciso para a sua organização produzir e consumir SBOMs e proveniência para todo artefato?
6. Como vocês impedem que os padrões seguros sejam desativados sob pressão de entrega?

## Principais conclusões

- O OWASP Top 10 é conhecimento essencial. O ASVS fornece o padrão testável.
- Sobreponham validação de entrada, parametrização e codificação de saída para derrotar a injeção e o XSS.
- Usem protocolos comprovados (OAuth 2.0, OIDC) e imponham MFA. Nunca construam autenticação do zero.
- Imponham a autorização no servidor em toda requisição e em todo objeto.
- Mantenham os segredos fora do código-fonte, gerenciem-nos de modo central e rotacionem para credenciais de curta duração.
- A cadeia de suprimentos é uma superfície de ataque primária. Usem SBOMs, SCA, assinatura e proveniência (SLSA).
- Controles automatizados e reutilizáveis protegem a frota inteira a um custo marginal por serviço.

## Referências e leitura complementar

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
