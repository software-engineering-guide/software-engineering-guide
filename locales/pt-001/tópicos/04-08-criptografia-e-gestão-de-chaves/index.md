# 4.8 Criptografia e gestão de chaves

## Visão geral e motivação

Quase todo sistema que vocês constroem já depende da [criptografia](https://en.wikipedia.org/wiki/Cryptography), a prática de proteger informações por técnicas matemáticas para que só as partes pretendidas possam lê-las ou confiar nelas. O seu tráfego web viaja em canais criptografados, as suas senhas são transformadas em hash, as suas atualizações de software são assinadas e os dados dos seus clientes ficam criptografados em disco. A boa notícia para a maioria dos engenheiros é que não se pede que inventem nada disso. A parte difícil não é a matemática. É usar corretamente os blocos de construção comprovados e, acima de tudo, gerenciar as chaves de que esses blocos dependem.

Este capítulo é escrito para engenheiros que não são criptógrafos, o que somos quase todos. Vocês precisam de entendimento suficiente para fazer escolhas sólidas, saber o que cada ferramenta garante e evitar os erros que transformam algoritmos fortes em falso conforto. O capítulo 4.3 (segurança de infraestrutura e de nuvem) menciona de passagem a criptografia e o gerenciamento de chaves. Aqui vamos mais fundo no que criptografar, como e como conduzir o ciclo de vida das chaves que o torna real.

Para as grandes empresas, a criptografia se espalha por milhares de serviços, certificados e chaves, e um único certificado expirado ou uma chave perdida pode derrubar um sistema crítico ou vazar um repositório de dados. Para o governo, a criptografia costuma ser obrigatória, validada e auditada, com regras de classificação de dados que ditam exatamente quais chaves protegem quais segredos e quem pode detê-las. Nos dois contextos, a falha recorrente é a mesma: bons algoritmos desfeitos por um gerenciamento descuidado de chaves.

## Princípios fundamentais

- **Não crie a sua própria criptografia.** Usem bibliotecas comprovadas, amplamente revisadas, e algoritmos padrão. Esquemas inéditos falham de modos que só especialistas pegam.
- **Os algoritmos são a parte fácil. As chaves são a parte difícil.** O ciclo de vida de uma chave é onde moram a maioria das falhas do mundo real.
- **Saibam o que cada primitiva garante.** Confidencialidade, integridade e autenticidade são propriedades diferentes que exigem ferramentas diferentes.
- **Criptografem em trânsito e em repouso por padrão.** Façam da proteção o padrão, não uma adesão voluntária.
- **Separem a custódia das chaves do acesso aos dados.** Quem gerencia uma chave não deve poder ler automaticamente os dados que ela protege.
- **Planejem a mudança.** Os algoritmos enfraquecem, as chaves vazam e os padrões evoluem. Construam para a rotação e a migração desde o primeiro dia.
- **Prefiram implementações validadas onde importa.** Para trabalho regulado e governamental, escolham módulos com validação reconhecida.

## Recomendações

### Não crie a sua própria criptografia

Esta é a regra de ouro, e vale enunciá-la primeiro. Nunca projetem o seu próprio algoritmo de criptografia, nunca inventem o seu próprio protocolo e nunca implementem à mão uma primitiva a partir de um artigo. A criptografia que funciona parece simples e esconde modos sutis de falha (canais laterais de tempo, oráculos de preenchimento, aleatoriedade fraca) que só sobrevivem a anos de revisão especializada. Usem bibliotecas estabelecidas, como o módulo padrão de criptografia da sua plataforma ou uma biblioteca bem conceituada, e usem-nas no nível mais alto de abstração disponível. Recorram a modos de criptografia autenticada e a interfaces “fáceis” que façam da escolha segura o padrão, em vez de montar vocês mesmos peças de baixo nível.

### Combine a primitiva com a garantia de que vocês precisam

Ferramentas diferentes dão garantias diferentes, e confundi-las é um erro comum e perigoso. Aprendam as três famílias principais.

- A criptografia de **[chave simétrica](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** usa uma única chave secreta compartilhada tanto para criptografar quanto para decifrar. É rápida e protege a **confidencialidade**, mas as duas partes já precisam compartilhar a chave. O AES é o cavalo de batalha padrão.
- A criptografia de **[chave pública](https://en.wikipedia.org/wiki/Public-key_cryptography)** usa um par de chaves matematicamente ligadas: uma chave pública que qualquer um pode ter e uma chave privada que vocês mantêm secreta. Ela resolve a distribuição de chaves e permite as **assinaturas digitais**, que provam a **autenticidade** (quem enviou) e a **integridade** (que não foi alterado).
- Uma **[função de hash criptográfica](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** produz uma impressão digital de tamanho fixo dos dados e fornece a verificação de **integridade**. O hash é de mão única e não é criptografia. Para guardar senhas, usem uma função de hash de senhas lenta e com sal, nunca um hash rápido simples (veja o capítulo 4.2 sobre segurança de aplicações).

A lição prática: a criptografia esconde dados mas não prova quem os enviou, e um hash detecta adulteração mas não esconde nada. A maioria dos sistemas reais combina as duas coisas, que é exatamente por que vocês devem se apoiar em bibliotecas que as reúnam corretamente.

### Criptografe em trânsito com o TLS atual

Protejam todo salto de rede com o [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), o protocolo que protege os dados enquanto se movem entre sistemas. Exijam versões modernas de TLS, desativem as obsoletas, escolham suítes de cifras fortes e validem os certificados corretamente em vez de desligar as verificações para “fazer funcionar”. Criptografem também o tráfego interno entre serviços, e não apenas a borda pública, porque uma postura de confiança zero presume que a rede interna é hostil. Automatizem a emissão e a renovação de certificados para que o TLS seja o padrão sem esforço em toda parte.

### Criptografe em repouso com a criptografia em envelope

Criptografem por padrão os dados armazenados: bancos de dados, armazenamento de objetos, cópias de segurança e logs. O padrão usual é a **criptografia em envelope**, em que uma **chave de criptografia de dados (DEK)** criptografa os dados de fato, e uma **chave de criptografia de chaves (KEK)** guardada num serviço de gerenciamento de chaves criptografa a DEK. Isso permite rotacionar a chave-mestra sem recriptografar terabytes de dados e mantém a poderosa chave-raiz dentro de uma fronteira endurecida. Guardem ao lado dos dados apenas a DEK embrulhada (wrapped) e busquem-na e desembrulhem-na na hora do uso.

### Conduza o ciclo de vida das chaves deliberadamente

O ciclo de vida de uma chave é a parte genuinamente difícil da criptografia, e onde se originam a maioria das violações e quedas. Gerenciem cada etapa de propósito:

- **Geração:** criem chaves a partir de uma fonte aleatória forte, com força apropriada.
- **Distribuição:** levem as chaves aos sistemas que precisam delas sem expô-las em código, arquivos de configuração ou bate-papo.
- **Rotação:** substituam as chaves numa agenda e consigam rotacionar rápido diante de suspeita de comprometimento.
- **Revogação:** invalidem depressa uma chave ou certificado comprometido e garantam que os sistemas honrem a revogação.
- **Destruição:** aposentem com segurança o material de chave antigo para que não possa ser recuperado.

Usem um **serviço de gerenciamento de chaves (KMS)** para centralizar isso e usem um [módulo de segurança de hardware](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), um dispositivo resistente a adulteração que gera e guarda chaves de modo que nunca saiam em texto puro, para as chaves de maior garantia. Separem quem pode gerenciar chaves de quem pode ler os dados protegidos, para que a custódia das chaves imponha a separação de funções. Isso se conecta diretamente às regras de classificação de dados e de custódia do capítulo 4.5 (privacidade e proteção de dados).

### Distinga o gerenciamento de segredos do gerenciamento de chaves

Os dois se sobrepõem mas não são a mesma coisa. O **gerenciamento de chaves** rege as chaves criptográficas e seu ciclo de vida, normalmente dentro de um KMS ou HSM que executa as operações criptográficas por vocês para que a chave bruta nunca saia. O **gerenciamento de segredos** rege as credenciais de aplicação (senhas de banco de dados, tokens de API, certificados) que os serviços precisam obter e usar em texto puro, normalmente de um cofre de segredos com acesso de curta duração e auditado. Usem um KMS para chaves, um gerenciador de segredos para credenciais e nunca colem nenhum dos dois no código-fonte nem em arquivos de ambiente versionados.

### Automatize os ciclos de vida de PKI e de certificados

A **infraestrutura de chaves públicas (PKI)** é o sistema de autoridades certificadoras, certificados e cadeias de confiança que liga chaves públicas a identidades. Em escala, o risco dominante da PKI é a expiração-surpresa de certificado que derruba um serviço. Mantenham um inventário de todo certificado, monitorem as expirações e automatizem a emissão e a renovação para que nenhum humano precise se lembrar. Certificados de curta duração renovados automaticamente são mais seguros que os de longa duração tratados à mão, porque a automação remove o ponto único de falha humano. Os protocolos padrão aqui sustentam a interoperabilidade entre fornecedores (capítulo 3.8 sobre interoperabilidade e padrões abertos).

### Construa para a agilidade criptográfica e a migração pós-quântica

Os algoritmos enfraquecem com o tempo, e os padrões se movem. A **agilidade criptográfica** significa projetar os sistemas para poder trocar algoritmos e tamanhos de chave sem uma reescrita dolorosa: abstrair a criptografia atrás de uma pequena interface, versionar os dados criptografados para saber qual algoritmo os produziu e manter um inventário criptográfico do que se usa onde. Isso importa agora por causa da [criptografia pós-quântica](https://en.wikipedia.org/wiki/Post-quantum_cryptography), a nova família de algoritmos projetados para resistir aos futuros computadores quânticos. Os adversários podem colher dados criptografados hoje para decifrar depois, então os segredos de longa duração precisam de um plano de migração. Vocês não precisam entrar em pânico, mas devem conhecer o seu inventário e estar prontos para adotar os algoritmos pós-quânticos padronizados à medida que as plataformas os entreguem.

### Prefira implementações validadas onde exigido

Para sistemas regulados e governamentais, usar um algoritmo forte não basta: a implementação precisa ser validada. A **FIPS 140** (Federal Information Processing Standard 140) é o padrão dos EUA para validar módulos criptográficos, e muitos contratos exigem criptografia validada pela FIPS. O trabalho governamental também pode seguir orientações nacionais como a suíte Commercial National Security Algorithm (CNSA) da NSA para sistemas classificados. Verifiquem qual regime se aplica antes de construir, porque adaptar módulos validados tarde é caro. Isso se liga à evidência de conformidade e à governança (capítulo 4.6).

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| KMS gerenciado pelo provedor | Fácil, integrado, baixo ônus operacional | O provedor detém a custódia. Menos controle direto |
| Chaves gerenciadas pelo cliente / HSM | Custódia plena, atende a mandatos rígidos | Ônus operacional, risco de perder as chaves |
| Certificados automatizados de curta duração | Sem expirações-surpresa, revogação rápida | Exige investimento inicial em automação |
| Certificados de longa duração | Simples, menos peças móveis | Expirações geridas por humanos causam quedas |
| Criptografia em envelope | Rotação barata de chaves, protege a chave-mestra | Mais peças móveis para entender |
| Agilidade criptográfica desde o início | Migrações futuras baratas | Abstração e esforço de design extras agora |
| Adoção pós-quântica antecipada | Protege segredos de longa duração | Ferramentas imaturas, chaves maiores, algum risco |

A tensão central é controle versus ônus operacional. Guardar as próprias chaves num HSM dá a máxima custódia e satisfaz os mandatos mais rígidos, mas exige especialização e cria um novo risco catastrófico: perca a chave e vocês perdem os dados, de forma irrecuperável. Os serviços gerenciados pelo provedor removem esse ônus mas colocam a custódia com o provedor. Resolvam por camadas: usem serviços gerenciados com padrões sensatos na maioria dos sistemas e reservem as chaves gerenciadas pelo cliente e os HSMs para os dados de maior classificação, onde o controle extra vale o custo e o risco.

## Perguntas para discutir com sua equipe

1. **Vocês têm um inventário completo das suas chaves, certificados e dos algoritmos em que se apoiam?** Vocês não conseguem rotacionar, migrar nem auditar o que não enxergam, e a maioria das organizações descobre que tem muito mais material criptográfico espalhado pelos serviços do que alguém acompanha. Um inventário é o pré-requisito de toda decisão posterior: o monitoramento de expiração de certificados, a rotação de chaves, a delimitação do escopo FIPS e o planejamento pós-quântico dependem todos dele. Levem uma lista dos certificados atuais e suas datas de expiração e perguntem quem é dono de cada um e o que quebra quando ele caduca. Para um parque grande, a resposta honesta costuma ser que não existe uma fonte única de verdade, e construí-la é o primeiro passo de maior alavancagem. Se vocês não conseguem enumerar a sua criptografia hoje, a agilidade e a rotação são aspirações, não capacidades.

2. **Vocês conseguem rotacionar ou revogar depressa uma chave comprometida, e já praticaram isso alguma vez?** A rotação e a revogação são as partes do ciclo de vida das chaves que só importam sob pressão, e as equipes rotineiramente descobrem durante um incidente que uma chave está fixa em código em uma dúzia de lugares ou que a revogação na verdade não se propaga. Decidam o tempo-alvo para rotacionar uma chave e revogar um certificado e depois ensaiem antes de precisar. Levem a história da última exposição de credencial e percorram o que a rotação exigiu na prática. Para sistemas corporativos e governamentais, uma rotação não ensaiada pode significar escolher entre uma exposição prolongada e uma queda autoinfligida. Se a rotação nunca foi testada, presumam que não funciona.

3. **Onde fica a custódia das chaves, e ela impõe a separação de funções?** Quem pode gerenciar uma chave e quem pode ler os dados que ela protege não devem ser a mesma pessoa, porque fundir esses poderes derrota em silêncio o propósito da criptografia em repouso. Essa escolha também define se vocês usam chaves gerenciadas pelo provedor, chaves gerenciadas pelo cliente ou HSMs, cada um com controle e risco operacional diferentes. Levem as políticas atuais de chaves e verifiquem se alguma identidade isolada consegue ao mesmo tempo administrar uma chave e acessar o texto puro por trás dela, uma lacuna silenciosa comum. Para dados regulados e classificados, as regras de custódia podem ser ditadas pela classificação de dados (capítulo 4.5) e por mandato. Se a custódia e o acesso não estão separados, a sua criptografia está protegendo vocês menos do que o painel sugere.

4. **Como vocês se recuperariam se a chave-mestra que protege a sua criptografia em envelope fosse perdida ou destruída?** As chaves gerenciadas pelo cliente e os HSMs dão a custódia, mas entregam um novo modo catastrófico de falha: percam a chave de criptografia de chaves e toda chave de criptografia de dados que ela embrulha se torna permanentemente ilegível, junto com os dados por trás delas. Pesem isso contra o risco oposto de uma cópia de segurança ampla demais que silenciosamente recria o próprio problema de custódia que vocês tentavam resolver. Levem os arranjos atuais de cópia e de custódia de chaves em depósito, o raio de impacto de cada chave-mestra e evidência de que uma restauração foi de fato realizada e não apenas documentada. Para parques corporativos e governamentais, liguem isso às suas regras de classificação de dados: as chaves mais sensíveis muitas vezes proíbem cópias casuais, então a recuperação precisa ser projetada deliberadamente, testada numa agenda e conciliada com qualquer exigência regulatória de provar que o material de chave aposentado foi destruído.

5. **Quão prontos estão os seus sistemas para uma migração pós-quântica, e quais segredos de longa duração vocês migrariam primeiro?** Os adversários podem colher tráfego e arquivos criptografados hoje e decifrá-los quando os computadores quânticos amadurecerem, então qualquer segredo que precise permanecer confidencial por anos já está exposto a um futuro que vocês não enxergam. A pressão concorrente é que as ferramentas pós-quânticas ainda são jovens, as chaves são maiores e mover-se cedo demais arrisca apostar num algoritmo que muda antes de se assentar. Levem o inventário criptográfico, uma lista de segredos classificados por quanto tempo precisam permanecer confidenciais e uma leitura honesta de se a arquitetura consegue trocar algoritmos sem uma reescrita. Para o trabalho governamental e regulado, os registros com mandatos de confidencialidade de várias décadas tornam isso concreto e não teórico, e a contratação logo poderá exigir um plano documentado de migração e suporte aos algoritmos pós-quânticos padronizados.

6. **Quando a regulação exige criptografia validada, vocês sabem exatamente quais módulos estão no escopo e se qualificam?** Usar um algoritmo forte não é o mesmo que usar uma implementação validada, e as equipes rotineiramente descobrem tarde que uma biblioteca, um ambiente de execução de linguagem ou um serviço de nuvem não é coberto pela fronteira FIPS 140 que um contrato exige. A tensão é que os módulos validados podem ficar atrás das bibliotecas atuais em funcionalidades e velocidade, então escolhê-los restringe a sua pilha de modos que importam para a engenharia. Levem a lista de módulos criptográficos que cada sistema regulado de fato chama, os certificados de validação que os cobrem e o mandato específico (FIPS 140, CNSA ou uma regra setorial) que se aplica. Para programas corporativos e governamentais, decidam isso antes de construir, porque adaptar módulos validados e reautorizar um sistema depois do fato é caro, lento e muitas vezes força o redesenho dos próprios componentes que vocês achavam terminados.

## Perspectiva por setor

**Startup.** Apoiem-se inteiramente nos padrões comprovados da plataforma e gastem zero tempo de engenharia em criptografia própria. Liguem a criptografia gerenciada em repouso, terminem o TLS com certificados renovados automaticamente, façam hash das senhas com uma função lenta padrão e guardem os segredos no gerenciador de segredos da plataforma e não no repositório. A sua única decisão de design é uma interface fina em torno do punhado de campos que vocês criptografam na aplicação, para que uma futura saída das chaves gerenciadas pelo provedor não seja uma reescrita.

**Pequena empresa.** Vocês não têm criptógrafo e pouca vontade de operar um HSM, então comprem a custódia em vez de construí-la: usem o KMS e o gerenciador de segredos gerenciados pelo provedor que vêm com a sua nuvem ou ferramentas SaaS. Enquadrem o trabalho como higiene, isto é, nenhuma chave no código, criptografia ligada em toda parte por padrão e expirações de certificados monitoradas para que nada caduque de surpresa. Reservem as chaves gerenciadas pelo cliente para os raros dados para os quais um contrato ou regulador genuinamente as exige.

**Grande empresa.** O problema é a escala e a consistência entre milhares de serviços, certificados e chaves. Conduzam um KMS centralizado com criptografia em envelope, automatizem o ciclo de vida completo dos certificados para que nenhuma expiração seja tratada à mão e mantenham um único inventário criptográfico que alimente a rotação, a delimitação do escopo FIPS e o planejamento pós-quântico. Separem a custódia de chaves do acesso aos dados como controle de toda a organização e façam da criptografia uma capacidade de plataforma que toda equipe herda e não uma tarefa que cada equipe reinventa.

**Governo.** A contratação, a validação e a auditoria moldam toda escolha. Usem módulos validados pela FIPS 140 e sigam orientações nacionais como a CNSA para sistemas classificados, liguem a custódia das chaves à classificação de dados para que as chaves mais sensíveis fiquem com pessoal habilitado sob estrita separação de funções e gerem evidência contínua de criptografia validada para a autorização contínua. Documentem um plano de migração pós-quântica para os registros que precisam permanecer confidenciais por décadas e exijam que os fornecedores divulguem quais módulos são validados antes de vocês se comprometerem.

## Exemplos

**Startup.** Uma pequena equipe que constrói um aplicativo de acompanhamento de saúde se apoia inteiramente em padrões comprovados. Termina o TLS com certificados renovados automaticamente, liga a criptografia em repouso no banco de dados gerenciado e no armazenamento de objetos com o KMS do provedor e faz hash das senhas com uma função lenta e com sal de uma biblioteca padrão. Em vez de escrever qualquer criptografia por conta própria, usa uma chamada de criptografia autenticada de alto nível para o único campo que precisa criptografar na aplicação. Os segredos vivem no gerenciador de segredos da plataforma, nunca no repositório. Custa algumas tardes e remove uma categoria inteira de erros catastróficos.

**Grande empresa.** Um banco global opera um KMS centralizado e uma frota de HSMs, com um inventário criptográfico que acompanha cada chave e certificado em milhares de serviços. A criptografia em envelope protege os dados dos clientes, com chaves de dados embrulhadas por chaves-mestras que rotacionam numa agenda enquanto os dados ficam parados. A emissão e a renovação de certificados são totalmente automatizadas depois que uma queda pública lhes ensinou o custo de um único certificado expirado. Os administradores de chaves são uma equipe separada dos engenheiros de aplicação, de modo que a custódia impõe a separação de funções, e uma camada de agilidade criptográfica lhes permite começar a pilotar algoritmos pós-quânticos para arquivos de longa duração.

**Governo.** Uma agência nacional que trata registros classificados usa apenas módulos criptográficos validados pela FIPS 140 e segue as orientações CNSA da NSA para seus sistemas de maior classificação. As chaves são geradas e guardadas em HSMs que nunca liberam material de chave em texto puro, e a custódia é ligada à classificação de dados de modo que as chaves mais sensíveis ficam com pessoal habilitado sob estrita separação de funções. Os certificados rodam numa PKI interna gerenciada, com ciclos de vida automatizados, e a evidência contínua de criptografia validada alimenta a autorização contínua da agência. Um plano documentado de migração pós-quântica protege os registros que precisam permanecer confidenciais por décadas.

## Justificativa de negócio: motivações, ROI e TCO

A criptografia é outra área em que um investimento modesto previne perdas catastróficas, dignas de manchete. O custo total de propriedade inclui um KMS ou HSM, ferramentas de gerenciamento de segredos e de certificados e o tempo de engenharia para projetar os ciclos de vida e manter um inventário atual. Esses custos são reais mas limitados. O custo de pulá-los é uma violação de dados sem criptografia, uma queda de várias horas por um certificado expirado ou uma perda irrecuperável de dados por uma chave mal tratada, cada uma com multas regulatórias, custos de notificação e dano duradouro à reputação.

O ROI mais forte vem da automação e da reutilização. Os ciclos de vida automatizados de certificados eliminam a queda autoinfligida mais comum. O gerenciamento centralizado de chaves com padrões sensatos significa que todo novo serviço herda a criptografia em trânsito e em repouso sem esforço por equipe, transformando a criptografia de um imposto recorrente numa capacidade de plataforma. Para o trabalho regulado e governamental, os módulos validados e a evidência automatizada também reduzem o custo de auditorias e de autorização. Ao defender o caso junto à liderança, enquadrem-no com franqueza: os algoritmos são gratuitos e comprovados, o risco mora no gerenciamento de chaves e nas operações de certificados, e um pequeno investimento automatizado ali previne as falhas caras.

## Antipadrões e armadilhas

- **Criar a própria criptografia.** Algoritmos personalizados ou protocolos feitos à mão que falham de modos sutis, só visíveis a especialistas.
- **Chaves e segredos fixos no código.** Credenciais coladas no código-fonte, em arquivos de configuração ou em bate-papo, onde vazam e não podem ser rotacionadas.
- **Criptografia sem disciplina de chaves.** Ligar a criptografia mas deixar o acesso às chaves totalmente aberto ou nunca rotacioná-las.
- **Confundir hash com criptografia.** Tratar um hash como reversível, ou guardar senhas com um hash rápido em vez de um lento e com sal.
- **Roleta de certificados.** Sem inventário, sem monitoramento de expiração e quedas-surpresa periódicas quando um certificado caduca.
- **Custódia de chaves e acesso a dados fundidos.** Uma identidade que pode ao mesmo tempo gerenciar uma chave e ler os dados que ela protege.
- **Sem plano de rotação.** Chaves que nunca foram rotacionadas e não podem ser rotacionadas depressa sob pressão.
- **Criptografia sem agilidade.** Algoritmos tão enraizados que trocá-los exige uma reescrita, bloqueando qualquer migração futura.
- **Ignorar mandatos de validação.** Usar algoritmos fortes em módulos não validados onde a validação FIPS ou semelhante é exigida.

## Modelo de maturidade

- **Nível 1, Iniciar:** A criptografia é inconsistente e muitas vezes ausente, aplicada de forma reativa quando alguém nota uma lacuna. As chaves e os segredos estão fixos no código ou são compartilhados informalmente por bate-papo e arquivos de configuração. Não há inventário, nem rotação, e os certificados expiram de surpresa, e as equipes ocasionalmente escrevem a própria criptografia.
- **Nível 2, Desenvolver:** O TLS e a criptografia em repouso estão ligados nos principais sistemas, e existe um KMS ou gerenciador de segredos, mas a adoção é desigual e varia de equipe para equipe. Alguns certificados são monitorados e outros não, a rotação é manual e rara e nenhum inventário criptográfico completo os une.
- **Nível 3, Padronizar:** A criptografia em trânsito e em repouso é o padrão documentado e imposto em toda a organização. As chaves vivem num KMS com rotação agendada e criptografia em envelope, a custódia das chaves é separada do acesso aos dados, os ciclos de vida dos certificados são automatizados, um inventário criptográfico é mantido e módulos validados são usados onde a regulação os exige.
- **Nível 4, Gerenciar:** O parque criptográfico é medido e controlado em relação a linhas de base. Vocês acompanham a antecedência de expiração de certificados, a porcentagem de chaves rotacionadas no prazo, o tempo médio para revogar uma chave comprometida, as detecções de segredos no código por período e a cobertura do inventário e revisam essas métricas contra metas. A rotação e a revogação são ensaiadas numa cadência com tempos registrados, e os desvios disparam ação corretiva em vez de passar despercebidos.
- **Nível 5, Orquestrar:** A criptografia é uma capacidade de plataforma que todo serviço herda por padrão, continuamente melhorada e integrada em toda a organização. A rotação e a revogação são rápidas e rotineiramente exercitadas, HSMs protegem as chaves de maior garantia, e a agilidade criptográfica mais um plano ativo de migração pós-quântica mantêm o parque adaptativo à medida que algoritmos e mandatos mudam. A evidência de conformidade é produzida automaticamente e alimenta a autorização contínua.

## Ideias para discussão

1. Quais sistemas do seu parque justificam chaves gerenciadas pelo cliente ou HSMs, dado o custo operacional e o risco de perda catastrófica deles?
2. Como vocês construiriam e manteriam uma única fonte de verdade para toda chave e certificado que possuem?
3. Qual é o seu tempo realista hoje para rotacionar uma chave comprometida, e o que o torna lento?
4. Onde a sua arquitetura dificulta trocar um algoritmo criptográfico, e como vocês corrigiriam isso antes de uma migração forçada?
5. Quais dos seus segredos de longa duração importariam se um adversário os colhesse agora e os decifrasse anos depois?
6. Segredos e chaves alguma vez acabam em código, configuração ou logs, e como vocês saberiam?

## Principais conclusões

- **Não criem a sua própria criptografia.** Usem bibliotecas comprovadas e algoritmos padrão no mais alto nível seguro de abstração.
- **Os algoritmos são fáceis. O gerenciamento de chaves é difícil.** O ciclo de vida de uma chave (geração, distribuição, rotação, revogação, destruição) é onde moram as falhas reais.
- **Conheçam as suas garantias:** a criptografia simétrica e de chave pública protege a confidencialidade, as assinaturas provam a autenticidade e a integridade e o hash detecta adulteração mas não é criptografia.
- **Criptografem em trânsito com o TLS atual e em repouso com criptografia em envelope**, como padrão para todo sistema.
- **Separem a custódia das chaves do acesso aos dados**, usem um KMS para chaves e um gerenciador de segredos para credenciais e nunca fixem nenhum dos dois no código.
- **Automatizem os ciclos de vida dos certificados** para matar a queda por expiração-surpresa e mantenham um inventário criptográfico.
- **Construam para a agilidade criptográfica** e iniciem um plano de migração pós-quântica para segredos de longa duração.
- **Prefiram implementações validadas** (FIPS 140 e orientações nacionais aplicáveis) onde a regulação ou a classificação as exigir.

## Referências e leitura complementar

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
