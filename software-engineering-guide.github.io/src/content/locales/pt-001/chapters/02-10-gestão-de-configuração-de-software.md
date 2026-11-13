# 2.10 Gestão de configuração de software

## Visão geral e motivação

A [gestão de configuração de software](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) é a disciplina de identificar os componentes de um sistema de software, controlar como eles mudam, registrar o estado de cada mudança e verificar se o que você construiu e entregou corresponde ao que pretendia. Ela responde a uma pergunta que parece simples mas fica difícil em escala: o que exatamente há neste lançamento, como chegou lá e quem o aprovou? O [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) trata a SCM como uma área de conhecimento fundamental por uma razão clara: toda outra atividade de engenharia precisa de uma configuração estável e conhecida contra a qual trabalhar.

Numa equipe grande, a SCM é o tecido conjuntivo que mantém coerentes milhares de partes móveis. Código-fonte, bibliotecas, imagens de contêiner, definições de infraestrutura, dados de configuração, documentação e artefatos de teste mudam, cada um, no seu próprio relógio, e um sistema entregue é uma combinação específica de versões específicas de todos eles. Sem uma gestão de configuração deliberada, essa combinação é desconhecida e não pode ser reproduzida. Você não consegue recriar um lançamento passado, rastrear um defeito até a mudança que o causou nem dizer com confiança o que está rodando em produção.

Os contextos corporativos e governamentais elevam o que está em jogo. Programas regulamentados e do setor público precisam mostrar que as mudanças foram autorizadas, revisadas e registradas, que um build entregue remonta a requisitos e a código-fonte aprovados e que nada entrou no sistema sem controle. Aqui a SCM é tanto um sistema de evidências quanto um sistema de engenharia. O [controle de versões](https://en.wikipedia.org/wiki/Version_control) (capítulo 2.6) gerencia o histórico do código-fonte. A SCM governa toda a configuração e o processo controlado pelo qual ela muda. Ela está intimamente ligada à [infraestrutura como código](https://en.wikipedia.org/wiki/Infrastructure_as_code) (capítulo 8.2), aos pipelines de entrega (capítulo 8.1) e à auditoria e garantia (capítulo 10.2).

## Princípios fundamentais

- Tudo que determina o comportamento do sistema é um [item de configuração](https://en.wikipedia.org/wiki/Configuration_item) sob controle, não apenas o código-fonte.
- Uma [linha de base](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) é um ponto de referência conhecido e acordado. As mudanças são feitas contra linhas de base deliberadamente, não casualmente.
- A mudança é controlada e registrada, não impedida. O objetivo é a mudança autorizada e rastreável.
- A contabilização de status significa que você sempre pode responder o que há numa configuração e qual é o seu histórico de mudanças.
- As auditorias verificam se o sistema construído e entregue corresponde à configuração registrada e aos requisitos aprovados.
- A reprodutibilidade é inegociável: qualquer versão lançada deve poder ser reconstruída a partir de insumos controlados.
- Automatize a identificação, o registro e a verificação. A contabilidade manual não escala e não sobrevive à auditoria.

## Recomendações

### Defina o processo de SCM e atribua responsabilidade

Escreva um plano de SCM que diga o que está sob controle de configuração, como os itens são identificados, como as mudanças são propostas e aprovadas e como o status é registrado e auditado. Atribua uma responsabilidade clara, como um gestor de configuração ou uma equipe responsável, para que a SCM não seja tarefa de todos e, portanto, de ninguém. Ajuste o processo ao risco: uma ferramenta interna pequena precisa de um controle leve, enquanto um sistema crítico para a segurança ou regulamentado precisa de conselhos e registros formais. Ancore o plano num padrão reconhecido, como o IEEE 828, para que auditores e parceiros possam acompanhá-lo.

### Identifique os itens de configuração e estabeleça linhas de base

Liste os itens de configuração que determinam como o sistema se comporta: código-fonte, dependências, scripts de build, imagens de contêiner, definições de infraestrutura, dados de configuração, esquemas e documentos importantes. Dê a cada um um identificador estável e um esquema de versionamento. Estabeleça linhas de base em pontos significativos (uma versão lançada, um conjunto aprovado de requisitos, um build certificado) para ter uma referência acordada contra a qual mudar e à qual voltar. Uma linha de base é imutável: depois que você a declara, não a edita. Você apenas a substitui por uma nova linha de base criada pelo processo de mudança.

### Controle a mudança por um processo definido e por conselhos adequados

Encaminhe as mudanças nos itens controlados por um caminho definido: proposta, avaliação de impacto, aprovação, implementação e verificação. Para itens de maior risco, use um [conselho de controle de mudanças](https://en.wikipedia.org/wiki/Change_control_board) (CCB) que pese custo, risco e cronograma antes de autorizar uma mudança. Dimensione o conselho na medida certa: um portão automatizado leve para mudanças rotineiras de código e um CCB formal e multifuncional para mudanças que tocam linhas de base, interfaces ou comportamento regulamentado. Registre cada decisão e o raciocínio por trás dela e ligue as decisões de configuração significativas a registros de decisão (capítulo 1.6) para que o raciocínio sobreviva.

### Mantenha a contabilização do status de configuração

Mantenha um registro preciso e consultável de cada item de configuração: sua versão atual, a linha de base a que pertence e os pedidos de mudança aplicados a ele. Essa contabilização de status é o que permite responder, a qualquer momento, o que um lançamento contém e como chegou lá. Gere o registro automaticamente a partir das suas ferramentas de registro (controle de versões, pipeline, repositório de artefatos) em vez de manter uma planilha paralela que deriva da realidade. Esse registro é a espinha dorsal da rastreabilidade do requisito à mudança, ao build e à implantação.

### Conduza auditorias de configuração

Verifique duas coisas numa cadência regular. Uma auditoria funcional de configuração confirma que a configuração funciona como seus requisitos especificam. Uma auditoria física de configuração confirma que os artefatos entregues correspondem à configuração registrada: que o build veio do código-fonte e das dependências registrados e não contém nada não contabilizado. Automatize o máximo que puder: [builds reproduzíveis](https://en.wikipedia.org/wiki/Reproducible_builds), somas de verificação de artefatos, listas de materiais de software (SBOMs) e atestações de proveniência transformam a auditoria de uma inspeção manual numa verificação contínua.

### Gerencie lançamentos e entrega como eventos controlados

Trate um lançamento como uma linha de base específica e identificada, entregue por um processo repetível. Versione seus lançamentos explicitamente, produza um manifesto ou lista de materiais que descreva exatamente o que está incluído e registre o mapeamento do lançamento para a revisão do código-fonte e para o artefato implantado. Assine e calcule a soma de verificação dos artefatos lançados para que qualquer pessoa a jusante possa verificar sua integridade. Ligue a gestão de lançamentos ao pipeline de entrega (capítulo 8.1) para que a promoção entre ambientes seja, ela mesma, controlada, registrada e reversível.

### Escolha e integre as ferramentas de SCM

Apoie-se em ferramentas que automatizam a identificação, o controle, a contabilização e a auditoria em vez de depender só da disciplina: controle de versões para o código-fonte, registros de artefatos e de imagens para os binários, um pipeline imutável para os builds, infraestrutura como código para os ambientes e ferramentas de dependências e de SBOM para a proveniência. Conecte-as para que uma única mudança flua de forma rastreável do commit ao lançamento implantado. O que você busca é uma cadeia de ferramentas em que o registro de configuração seja um subproduto de fazer o trabalho, e não uma tarefa burocrática à parte.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| Conselhos formais de controle de mudanças | Forte autorização e trilha de auditoria. Risco pesado antes da mudança | Menor vazão. Custo operacional se aplicados a mudanças rotineiras |
| Portões automatizados leves | Fluxo rápido. Baixo custo operacional. Escala para muitas mudanças | Mais fracos para linhas de base de alto risco. Menos deliberação |
| Linhas de base imutáveis estritas | Pontos de referência reproduzíveis e auditáveis | Exigem disciplina e ferramentas. Atrito se usadas em excesso |
| Contabilização de status automatizada | Registro preciso e sempre atual. Pronto para auditoria | Investimento inicial em ferramentas e integração |
| Registros manuais de configuração | Simples de começar. Não exigem ferramentas | Derivam da realidade. Falham em escala e sob auditoria |

O compromisso central é controle versus fluxo. O controle de mudanças pesado dá forte garantia mas desacelera a entrega. O controle leve flui rápido mas enfraquece a rastreabilidade. A resposta não é escolher um globalmente: é graduar o controle pelo risco, automatizando as mudanças rotineiras por portões rápidos e reservando conselhos formais e linhas de base imutáveis para os itens em que a autorização e a auditabilidade realmente importam. O segundo compromisso é o investimento inicial em ferramentas versus o custo burocrático contínuo e o risco de auditoria. A contabilização automatizada custa mais para montar e muito menos para conviver.

## Perguntas para discutir com sua equipe

1. **O que exatamente pertence à nossa lista de itens de configuração, e quem é dono da decisão quando algo novo aparece?** A SCM só funciona se a lista de itens controlados corresponder ao conjunto de coisas que de fato determinam o comportamento, e num sistema grande esse conjunto é maior do que a maioria das equipes pensa: código-fonte, dependências, scripts de build, imagens de contêiner, definições de infraestrutura, esquemas, sinalizadores de funcionalidade e os dados de configuração que mudam em silêncio o que o software faz. Se ninguém é dono da lista, ela fica obsoleta, e o item que derrubou você em produção acaba sendo a única coisa que ninguém pensou em controlar. Leve o seu inventário atual à reunião e procure itens que determinam comportamento e estão faltando nele. Atribua um responsável (um gestor de configuração ou uma equipe nomeada) para que acrescentar um novo item seja uma decisão deliberada e não um acidente, porque a SCM que é tarefa de todos é tarefa de ninguém.

2. **Conseguimos provar que um artefato implantado veio do código-fonte e do pipeline que pensamos, e essa prova sobreviveria a uma adulteração?** A reprodutibilidade e a rastreabilidade são todo o sentido da SCM, e a versão afiada da pergunta é se você consegue ligar o binário em execução a um commit e a uma execução de build específicos com evidência, e não com afirmação. Num sistema regulamentado ou de alto valor, essa é também a sua defesa da cadeia de suprimentos: atestações de proveniência assinadas, somas de verificação de artefatos e uma lista de materiais de software transformam “temos bastante certeza” em algo que um auditor ou um responsável por incidente pode verificar. Leve o seu último lançamento e tente percorrê-lo para trás, do artefato implantado até a mudança aprovada. Se qualquer salto é uma afirmação manual e não um vínculo registrado e verificável, é por aí que um atacante ou um erro honesto pode introduzir algo sem ser notado, e fechá-lo significa ligar assinatura e proveniência ao pipeline para que o registro seja um subproduto da entrega.

3. **Hoje alguém consegue editar um lançamento no próprio lugar, e o que isso faria à nossa capacidade de confiar nele?** Uma linha de base só é útil se for imutável: no momento em que “o lançamento” pode ser editado depois do fato, você não consegue mais reproduzi-lo nem confiar nele como referência, e toda auditoria a jusante vira arqueologia. A falha clássica é a configuração editada direto em produção ou uma etiqueta movida em silêncio, que é exatamente o atalho que parece inofensivo e torna um lançamento impossível de reconstruir depois. Leve a resposta honesta à reunião: quem tem acesso para mudar uma linha de base implantada sem passar pelo processo de mudança, e isso já aconteceu? A correção é tornar as linhas de base genuinamente imutáveis e encaminhar toda mudança por proposta, avaliação de impacto, aprovação e verificação, graduando o rigor para que as mudanças rotineiras fluam por portões automatizados rápidos enquanto as mudanças em linhas de base e as regulamentadas vão a um conselho.

4. **A nossa contabilização do status de configuração é gerada automaticamente a partir das ferramentas de registro, ou mantida à mão, e quanto ela derivou do que está de fato implantado?** A contabilização de status é o registro que permite responder, a qualquer momento, o que um lançamento contém e como chegou lá, e num sistema grande esse registro só é confiável se resultar do trabalho, e não for digitado numa planilha paralela. A atração concorrente é que um registro mantido à mão parece barato para começar e flexível, enquanto automatizá-lo significa integrar o controle de versões, o pipeline e o repositório de artefatos para que o registro vire um subproduto da entrega. Leve o registro em que vocês confiam hoje, escolha três lançamentos recentes ao acaso e verifique se as versões registradas, as linhas de base e os pedidos de mudança aplicados correspondem ao que as ferramentas dizem que foi entregue. Para uma empresa ou programa governamental, um registro de status que diverge da realidade não é um problema de arrumação, é uma constatação de auditoria à espera de acontecer, porque um auditor que pega uma lacuna deixa de confiar em todo o relato e pede que você o reconstrua à mão.

5. **O nosso controle de mudanças é graduado pelo risco, ou o mesmo nível de cerimônia governa toda mudança, seja o que for que ela toque?** Controle e fluxo puxam em sentidos opostos: um conselho formal de controle de mudanças pesa custo, risco e cronograma antes de autorizar uma mudança, mas aplicar essa cerimônia a um ajuste rotineiro de código só acrescenta atraso, enquanto empurrar uma linha de base compartilhada ou um fluxo de pagamento regulamentado por um portão automatizado rápido remove a deliberação exatamente onde você a quer. Os modos de falha são simétricos, uma lentidão uniforme que as pessoas aprendem a contornar, ou uma frouxidão uniforme que deixa uma mudança de alto risco passar sem exame. Leve uma amostra das mudanças do último trimestre classificadas pelo que cada uma tocou e verifique se o rigor que recebeu correspondeu de fato ao seu risco. Em contextos regulamentados e do setor público, nomeie quais classes de itens precisam chegar a um conselho multifuncional e quais podem fluir por portões automatizados e registre essa graduação explicitamente, porque “usamos julgamento” não é um controle que um auditor ou um órgão de supervisão possa verificar.

6. **Quando foi a última vez que realizamos uma auditoria funcional e uma física de configuração, e quanta das evidências seria um registro vivo e não uma reconstrução?** Uma auditoria funcional de configuração confirma que o sistema funciona como seus requisitos especificam, e uma auditoria física de configuração confirma que os artefatos entregues correspondem à configuração registrada e não contêm nada não contabilizado. Pule-as e você estará confiando em que suas linhas de base e a contabilização de status são honestas sem nunca verificar. A tensão é o custo: as auditorias manuais são lentas e dolorosas, e é exatamente por isso que as equipes as adiam, e a saída é automatizar as verificações com builds reproduzíveis, somas de verificação de artefatos, listas de materiais de software e atestações de proveniência para que a verificação se torne contínua. Leve o seu lançamento mais recente e tente produzir, na hora, o rastreamento de requisito para mudança, build e implantação e a prova de artefato para código-fonte. Para empresas e programas governamentais, essa trilha de evidências é o que a certificação e a supervisão exigem, então a pergunta honesta é se a auditoria de amanhã seria respondida com registros que vocês já têm ou com um exercício de arqueologia que vocês não podem bancar.

## Perspectiva por setor

**Startup.** Mantenha a SCM leve mas real. Ponha o código-fonte, as definições de infraestrutura e os dados de configuração no controle de versões e faça de cada lançamento um build etiquetado produzido por um único pipeline e não um artefato montado à mão. Pule os conselhos de controle de mudanças e as linhas de base formais, que são exagero no seu tamanho, mas nunca deixe ninguém editar a configuração direto em produção, porque esse único atalho é o que torna um lançamento impossível de reproduzir quando um cliente encontrar um bug na próxima terça-feira.

**Pequena empresa.** Sem gestor de configuração e com orçamento apertado, apoie-se em ferramentas que dão a SCM quase de graça: uma plataforma de controle de versões hospedada, o pipeline embutido nela e um repositório de artefatos, para que o registro de configuração seja um subproduto e não um trabalho que você precise dotar de pessoal. Compre essa capacidade embutida em ferramentas que você já paga em vez de construir um processo sob medida. Gaste a sua escassa atenção nos dois hábitos que mais importam, lançamentos etiquetados e reproduzíveis e manter a configuração que muda o comportamento longe de edições manuais em produção.

**Grande empresa.** O problema é a consistência entre muitas equipes: um plano de SCM compartilhado, uma taxonomia comum de itens de configuração, um controle de mudanças graduado e uma contabilização de status gerada automaticamente a partir do controle de versões, do repositório de artefatos e do pipeline. Reserve os conselhos formais de controle de mudanças e as linhas de base imutáveis para a plataforma compartilhada e os fluxos regulamentados, deixe as mudanças rotineiras fluírem por portões automatizados e padronize a proveniência assinada e as SBOMs para que o lançamento de qualquer equipe possa ser rastreado e qualquer auditor possa consultar um registro vivo em vez de encomendar uma reconstrução.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam o processo. Siga um plano formal de SCM alinhado a um padrão reconhecido, como o IEEE 828, estabeleça linhas de base dos itens de configuração em marcos contratuais e encaminhe toda mudança numa linha de base controlada por um conselho que registre impacto, decisão e justificativa. Exija que os artefatos entregues sejam reproduzíveis a partir de insumos controlados, com soma de verificação e rastreáveis de ponta a ponta, do requisito aprovado ao build entregue, porque essa trilha de evidências documentada é exatamente o que a certificação, a auditoria e a supervisão pública exigem.

## Exemplos

**Startup.** Uma startup de seis pessoas mantém a SCM leve mas real: código-fonte, definições de infraestrutura e dados de configuração vivem todos no controle de versões, e cada lançamento é um build etiquetado e versionado produzido pelo mesmo pipeline, e não montado à mão. Quando um cliente relata um bug que apareceu na terça-feira passada, eles rastreiam o artefato implantado até o commit exato em minutos em vez de adivinhar. Pulam os conselhos de controle de mudanças e as linhas de base formais, que seriam exagero no tamanho deles, mas se recusam a deixar qualquer pessoa editar a configuração direto em produção, porque esse único atalho é o que torna um lançamento impossível de reproduzir depois.

**Grande empresa.** Uma grande empresa de serviços financeiros põe todos os artefatos implantáveis, as definições de infraestrutura e os dados de configuração sob controle de configuração. Cada lançamento é uma linha de base imutável e versionada, com uma lista de materiais de software gerada, e cada artefato implantado carrega uma atestação de proveniência assinada que o liga a uma revisão específica do código-fonte e a uma execução do pipeline. As mudanças rotineiras de aplicação fluem por portões automatizados do pipeline, enquanto as mudanças em linhas de base da plataforma compartilhada ou em fluxos de pagamento regulamentados vão a um conselho de controle de mudanças. A contabilização de status é gerada automaticamente a partir do controle de versões, do repositório de artefatos e do pipeline, de modo que os auditores consultam um registro vivo em vez de pedir uma reconstrução.

**Governo.** Um programa de defesa segue um plano formal de SCM alinhado ao IEEE 828. Os itens de configuração são listados e têm linhas de base estabelecidas em marcos contratuais, e um conselho de controle de mudanças autoriza toda mudança numa linha de base controlada, registrando impacto, decisão e justificativa. As auditorias funcionais de configuração confirmam que o sistema entregue atende aos requisitos especificados, e as auditorias físicas de configuração confirmam que os artefatos entregues correspondem exatamente à configuração registrada. Os lançamentos são reproduzíveis a partir de insumos controlados, têm soma de verificação e são rastreáveis de ponta a ponta, do requisito aprovado ao pedido de mudança e ao build entregue, que é exatamente a trilha de evidências que a certificação e a supervisão exigem.

## Justificativa de negócio: motivações, ROI e TCO

A SCM existe para controlar risco e custo ao longo da vida de um sistema. O retorno vem da reprodutibilidade e da rastreabilidade: você consegue recriar qualquer lançamento, rastrear defeitos até as mudanças que os causaram e responder a perguntas de auditoria a partir de registros e não de arqueologia. Isso encurta o tempo de diagnóstico de incidentes, reduz o custo e a duração das auditorias e evita a classe cara de falha em que ninguém consegue dizer o que está rodando nem como reconstruí-lo.

O custo total de propriedade favorece a automação. Os registros manuais de configuração são baratos para começar e cada vez mais caros de manter, e falham exatamente quando você mais precisa deles, durante um incidente ou uma auditoria, porque derivaram da realidade. A identificação, a contabilização e a auditoria automatizadas custam mais de início, mas transformam o registro de configuração num subproduto quase gratuito do pipeline de entrega. Para defender o caso junto à liderança, apresente a SCM como o controle que torna os lançamentos reproduzíveis e as mudanças auditáveis e pese-a contra o custo de lançamentos irreproduzíveis, auditorias prolongadas e o risco de conformidade da mudança sem controle.

## Antipadrões e armadilhas

- **Configuração por conhecimento tribal:** o conteúdo verdadeiro de um lançamento vive só na cabeça de um engenheiro, não em qualquer registro.
- **Linhas de base mutáveis:** “o lançamento” é editado no próprio lugar, de modo que não pode mais ser reproduzido nem usado como referência confiável.
- **Dados de configuração sem controle:** o código está sob controle de versões, mas a configuração que muda o seu comportamento é editada ad hoc em produção.
- **Teatro do controle de mudanças:** um conselho que carimba tudo, acrescentando atraso sem acrescentar escrutínio real.
- **Contabilização de status manual:** uma planilha de versões que diverge em silêncio do que está de fato implantado.
- **Builds irreproduzíveis:** lançamentos que não podem ser reconstruídos a partir de insumos controlados, de modo que auditorias e reconstruções viram adivinhação.
- **Lançamentos não rastreáveis:** nenhum mapeamento do artefato implantado de volta à revisão do código-fonte, ao pedido de mudança e à aprovação.

## Modelo de maturidade

- **Nível 1 (Iniciar):** A SCM é ad hoc e reativa. Apenas o código-fonte é controlado, os lançamentos são montados à mão, não há linhas de base nem registro confiável do que está implantado e não há como reproduzir um build passado.
- **Nível 2 (Desenvolver):** Existem práticas básicas, mas variam de equipe para equipe. Alguns sistemas definem itens de configuração e um processo de mudança e versionam seus lançamentos, existem linhas de base aqui e ali, mas os registros são em parte manuais e o rigor do controle é inconsistente na organização.
- **Nível 3 (Padronizar):** As práticas são documentadas e impostas em toda a organização. Uma taxonomia comum de itens de configuração, linhas de base imutáveis, controle de mudanças graduado e contabilização de status estão estabelecidos e em grande parte automatizados. Os lançamentos são reproduzíveis e rastreáveis, e as auditorias são apoiadas por ferramentas e não pela memória.
- **Nível 4 (Gerenciar):** A SCM é medida e controlada com dados. A taxa de reprodutibilidade, a cobertura de rastreabilidade do requisito ao artefato implantado, o prazo de mudança em cada nível de controle, os incidentes de deriva de configuração e as constatações de auditoria são acompanhados em relação a linhas de base e metas. Os desvios disparam correção, e cada decisão de seguir ou não se apoia nessa evidência e não em afirmação.
- **Nível 5 (Orquestrar):** A SCM é continuamente melhorada e integrada em toda a organização. Totalmente automatizada e continuamente verificada com builds reproduzíveis, SBOMs, atestações de proveniência e contabilização de status ao vivo, o processo é tecido na entrega, na segurança e na auditoria e se adapta conforme o risco e os resultados de entrega mudam, aposentando e redefinindo o escopo de controles com base em evidências.

## Ideias para discussão

- Vocês conseguem reproduzir hoje o seu último lançamento exatamente a partir de insumos controlados, e quanto tempo levaria?
- Quais itens de configuração determinam o comportamento mas não estão de fato sob controle, especialmente dados de configuração e infraestrutura?
- O seu controle de mudanças é graduado pelo risco, ou acrescenta custo uniforme ou frouxidão uniforme em toda parte?
- Onde vive o seu registro de configuração, e quanto ele derivou do que está de fato implantado?
- Que evidências vocês conseguiriam produzir numa auditoria amanhã, e quanto delas seria reconstrução e não registro?
- Como os builds reproduzíveis, as SBOMs e a proveniência mudam o que as suas auditorias podem verificar automaticamente?

## Principais conclusões

- A SCM controla toda a configuração (código, dependências, infraestrutura e dados de configuração), não apenas o código-fonte.
- As linhas de base são pontos de referência imutáveis. A mudança é autorizada e registrada contra elas, não impedida.
- A contabilização de status deve permitir responder, a qualquer momento, o que um lançamento contém e como chegou lá.
- As auditorias verificam se o que foi construído e entregue corresponde à configuração registrada e aos requisitos aprovados.
- Gradue o controle pelo risco e automatize a identificação, a contabilização e a auditoria para que o registro seja um subproduto da entrega.

## Referências e leitura complementar

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
