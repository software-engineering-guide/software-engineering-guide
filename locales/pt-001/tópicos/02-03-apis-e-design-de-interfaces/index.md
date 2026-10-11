# 2.3 APIs e design de interfaces

## Visão geral e motivação

Uma [API](https://en.wikipedia.org/wiki/API) (interface de programação de aplicações) é o contrato pelo qual um software oferece capacidade a outro. É onde equipes, sistemas e organizações se encontram, e é a coisa mais duradoura e cara de errar. Você pode refatorar livremente a assinatura de uma função interna. Uma API publicada é diferente: é uma promessa a consumidores que você talvez nunca conheça, e quebrá-la os quebra. À medida que as organizações dividem [monólitos](https://en.wikipedia.org/wiki/Monolithic_application) em serviços e abrem capacidades a parceiros e ao público, a API se torna a principal superfície do produto e o principal risco de integração.

Para equipes grandes, as APIs são o que permite às pessoas trabalhar de forma independente. Uma interface bem projetada permite mudar seus internos sem coordenar com todos os consumidores, que é todo o sentido de uma fronteira de serviço. Uma mal projetada vaza detalhes internos, força implantações em sincronia e transforma um conjunto de serviços num monólito distribuído: serviços separados mas tão acoplados que precisam ser construídos e implantados juntos. O design da sua API determina diretamente quão independentemente suas equipes conseguem se mover.

Em contextos corporativos e governamentais, as APIs também carregam obrigações de conformidade, segurança e longevidade. Uma API do setor público pode ser obrigada a seguir [padrões abertos](https://en.wikipedia.org/wiki/Open_standard), permanecer estável por anos e atender desenvolvedores externos com quem você não consegue se coordenar. As APIs corporativas sustentam integrações com parceiros sob níveis de serviço contratuais. Tudo isso eleva a barra da disciplina de versionamento, da [compatibilidade retroativa](https://en.wikipedia.org/wiki/Backward_compatibility), da governança e da experiência do desenvolvedor.

## Princípios fundamentais

- Projete o contrato primeiro. A interface é uma decisão deliberada de produto, não um subproduto da implementação.
- Otimize a experiência do consumidor, não a sua própria conveniência.
- Trate a compatibilidade retroativa como uma promessa. Mudanças que quebram exigem uma nova versão e um caminho de migração.
- Faça o que é fácil ser correto: padrões sensatos, erros previsíveis, convenções consistentes.
- Projete para a falha. A [idempotência](https://en.wikipedia.org/wiki/Idempotence) (uma requisição repetida tem o mesmo efeito que uma única), as novas tentativas, a paginação e a [limitação de taxa](https://en.wikipedia.org/wiki/Rate_limiting) são preocupações de primeira classe, não reflexões tardias.
- Escolha o estilo de protocolo para servir à interação, não à moda.
- Governe as APIs como produtos, com responsáveis, ciclos de vida e documentação.

## Recomendações

### Trabalhe com API primeiro e guiado por contrato

Defina e revise o contrato da API, incluindo seus recursos, operações, esquemas e semântica de erros, antes de escrever a implementação. Use uma especificação legível por máquina, para que o contrato possa gerar documentação, esqueletos de cliente e de servidor, servidores simulados e validação. Assim os consumidores podem começar a se integrar com o servidor simulado enquanto você constrói, e o contrato se torna a única fonte da verdade contra a qual os dois lados testam.

### Escolha o estilo de interação deliberadamente

Escolha entre [REST](https://en.wikipedia.org/wiki/REST) (transferência de estado representacional), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) e [mensageria orientada a eventos](https://en.wikipedia.org/wiki/Event-driven_architecture) com base na interação, não na preferência pessoal. Use o REST para interfaces orientadas a recursos, amplamente interoperáveis e passíveis de cache. Use o GraphQL quando clientes diversos precisam de leituras flexíveis e agregadas sobre um grafo rico. Use o gRPC para chamadas de alto desempenho e fortemente tipadas entre serviços internos. Use a mensageria orientada a eventos para fluxos de trabalho assíncronos e desacoplados e para propagar mudanças de estado. Muitos sistemas grandes usam vários estilos ao mesmo tempo, cada um onde se encaixa.

### Versione e torne obsoleto com disciplina

Adote uma estratégia explícita de versionamento e uma política de descontinuação publicada: como você classifica as mudanças, por quanto tempo apoia versões antigas e como notifica os consumidores. Trace uma linha clara entre mudanças compatíveis (acrescentar campos opcionais, novos endpoints) e mudanças que quebram (remover ou renomear campos, mudar tipos ou semântica). Nunca reaproveite o significado de um campo existente. Dê aos consumidores janelas de sobreposição para migrar e comunique os prazos com bastante antecedência.

### Torne a semântica de erros consistente e legível por máquina

Devolva erros estruturados e previsíveis: códigos estáveis legíveis por máquina, mensagens legíveis por humanos e contexto suficiente para agir, sem vazar internos sensíveis. Use a mesma semântica de status em todos os endpoints, para que os clientes possam tratar os erros de modo uniforme. Documente todo erro que um consumidor possa encontrar.

### Embuta idempotência, paginação e limitação de taxa

Torne as operações de escrita seguras para repetir, aceitando chaves de idempotência, de modo que um cliente que tenta de novo depois de um tempo esgotado não cobre duas vezes nem crie duas vezes. Pagine todo endpoint de listagem desde o primeiro dia e prefira a paginação por cursor para conjuntos de dados grandes ou em mudança. Aplique e documente limites de taxa e devolva aos clientes o estado atual do limite para que recuem com elegância.

### Governe as APIs e invista na experiência do desenvolvedor

Trate cada API como um produto, com um responsável, um ciclo de vida e uma entrada de catálogo. Estabeleça uma revisão de design ou um conselho de padrões de API para que as interfaces permaneçam consistentes entre equipes. Invista na experiência do desenvolvedor: documentação de referência precisa, guias de início rápido, exemplos, um ambiente de teste (sandbox) e um registro de mudanças. Num grande ecossistema, um portal ou catálogo que torne as APIs localizáveis é essencial.

## Compromissos: prós e contras

| Estilo | Melhor para | Prós | Contras |
|---|---|---|---|
| REST / HTTP | APIs públicas orientadas a recursos | Onipresente, passível de cache, simples, interoperável | Busca demais ou de menos. Muitas idas e vindas. Contratos frouxos a menos que especificados |
| GraphQL | Leituras flexíveis para clientes variados | Consultas especificadas pelo cliente. Um só endpoint. Esquema forte | Complexidade de cache e de limitação de taxa. Riscos de custo de consulta. Complexidade no servidor |
| gRPC | Chamadas internas de alto desempenho | Rápido, compacto, fortemente tipado, com streaming | Suporte fraco em navegadores. Menos legível por humanos. Ferramentas mais pesadas |
| Orientado a eventos | Fluxos de trabalho assíncronos e desacoplados | Baixo acoplamento. Escalável. Resiliente | Mais difícil de raciocinar. Consistência eventual. Complexidade operacional |

As estratégias de versionamento trocam estabilidade por manutenção. Apoiar muitas versões antigas protege os consumidores, mas multiplica o código que você precisa manter e testar. A compatibilidade retroativa troca a sua própria liberdade pela estabilidade do consumidor, em geral a troca certa para uma API amplamente usada. O quadro geral: o custo de uma má decisão de API é pago por cada consumidor ao longo de toda a vida da interface. Por isso vale a pena gastar mais esforço de design na fronteira do que em quase qualquer outro lugar.

## Perguntas para discutir com sua equipe

1. **Como você classifica uma mudança como compatível ou como quebra, e que verificação automatizada pega uma quebra silenciosa antes de ela ser entregue?** Este capítulo traça uma linha rígida: acrescentar campos opcionais e novos endpoints é seguro, enquanto remover ou renomear campos, mudar tipos ou reaproveitar o significado de um campo quebra os consumidores. Numa equipe grande, quem faz a mudança muitas vezes não consegue ver todos os consumidores, então um ajuste “pequeno” pode quebrar em silêncio parceiros com quem você nunca fala. Leve o sinal concreto à reunião: vocês rodam verificações automatizadas de compatibilidade de contrato na CI contra a especificação publicada, ou dependem de alguém se lembrar da regra? Em contextos corporativos e governamentais, onde uma mudança que quebra força uma migração coordenada entre todos os parceiros e pode atravessar trocas de fornecedor e de administração, o custo cresce com o número de consumidores. Decida as regras de classificação e instale um portão de compatibilidade, para que uma mudança incompatível quebre o build em vez de uma integração.

2. **Quais primitivas de confiabilidade, chaves de idempotência, paginação e limitação de taxa, são obrigatórias em todo novo endpoint desde o primeiro dia?** O capítulo insiste que são preocupações de primeira classe, porque adaptar uma chave de idempotência a um endpoint de cobrança já em produção, ou acrescentar paginação a uma listagem que já é entregue, é em si uma mudança que quebra. Um grande ecossistema amplifica isso: um endpoint que funciona em teste colapsa sob volume real de dados, e uma escrita não idempotente transforma um único soluço de rede em cobranças duplicadas. Leve a evidência de quais endpoints atuais não as têm e o que uma tempestade de novas tentativas faria. Torne os padrões inegociáveis em novos endpoints: paginação por cursor em toda listagem, chaves de idempotência em toda escrita, limites de taxa documentados que devolvem o estado atual. Isso converte uma futura migração forçada num hábito de design de uma só vez.

3. **Vocês realmente projetam e revisam o contrato antes de escrever a implementação, ou a interface vaza do código?** A recomendação de API primeiro pede uma especificação legível por máquina, revisada de antemão, que gera documentação, esqueletos e servidores simulados e permite aos consumidores se integrar a um servidor simulado enquanto você constrói. Quando o contrato vem depois da implementação, a interface expõe a estrutura interna do banco de dados e muda sempre que a implementação muda, que é o principal antipadrão deste capítulo. O sinal a examinar: um consumidor consegue começar a se integrar ao seu servidor simulado hoje, ou precisa esperar um backend em execução? Para APIs públicas e de parceiros, em que a interface é a superfície do produto e a coisa mais cara de errar, gastar um dia no contrato poupa semanas de vaivém de suporte. Faça da revisão do contrato uma etapa obrigatória antes de a implementação começar.

4. **Quando duas equipes precisam expor a mesma capacidade, qual estilo de interação vence, e quem tem autoridade para dizer não a um quarto protocolo?** Este capítulo manda escolher REST, GraphQL, gRPC ou mensageria orientada a eventos pelo encaixe da interação, mas em escala o risco real é que cada equipe escolha o seu favorito e os consumidores enfrentem uma convenção diferente em cada endpoint. Uma grande organização paga por essa fragmentação em bibliotecas de cliente, gateways, monitoramento e na carga cognitiva de cada integrador que agora aprende quatro idiomas em vez de um. Leve o inventário de protocolos já em produção, a interação que cada um foi escolhido para servir e os consumidores que abrangem mais de um. A consideração concorrente é genuína: um padrão compartilhado reduz a proliferação, mas um mandato rígido força problemas com formato de gRPC num buraco com formato de REST. Nomeie o órgão de padrões ou a revisão de arquitetura que é dono do processo de exceção, porque em parques corporativos e governamentais uma proliferação de estilos vira um imposto permanente sobre a integração e um problema difícil de reverter depois que os parceiros dependem de cada um.

5. **Qual é a nossa política publicada de descontinuação, e conseguimos provar que de fato honramos a janela de suporte que anunciamos?** O capítulo trata o versionamento e a descontinuação como disciplina: uma política escrita sobre quanto tempo as versões antigas vivem, como os consumidores são notificados e que sobreposição eles têm para migrar. Uma promessa que você não consegue cumprir é pior que nenhuma, porque um grande ecossistema inclui consumidores com quem você nunca fala e que continuarão chamando uma versão aposentada até ela quebrar em produção. Leve as evidências à discussão: quantas versões ativas você carrega hoje, o uso real em cada uma, se você consegue ver quais consumidores ainda chamam um endpoint descontinuado e com que antecedência o seu último encerramento foi anunciado. A pressão concorrente é o custo de manutenção contra a estabilidade do consumidor, e ambos são reais. Para parceiros corporativos sob níveis de serviço contratuais e APIs do setor público que precisam sobreviver a administrações e trocas de fornecedor, a janela de suporte é um compromisso que pode durar mais que a equipe que o assumiu, então decida quem é responsável por ela e como um encerramento é provado seguro antes de acontecer.

6. **Como sabemos que a nossa experiência do desenvolvedor é boa, ou estamos presumindo isso porque a API funciona para nós?** Este capítulo enquadra cada API como um produto cuja adoção depende de documentação de referência precisa, guias de início rápido, exemplos, um ambiente de teste, um registro de mudanças e um catálogo localizável. As equipes rotineiramente confundem “a API funciona” com “a API é utilizável”, e a distância aparece como chamados de suporte, integrações fracassadas e consumidores que desistem em silêncio. Leve sinais mensuráveis em vez de opiniões: o tempo até a primeira chamada bem-sucedida de um novo integrador, o volume de chamados de suporte por endpoint, quão desatualizada está a documentação publicada em relação ao contrato real e se uma pessoa recém-chegada consegue se virar sozinha no portal sem escrever à sua equipe. A tensão é que documentação e portais custam esforço real que compete com a entrega de funcionalidades, e ainda assim num grande ecossistema uma experiência do desenvolvedor ruim empurra o custo de integração para centenas de consumidores de uma vez. No governo, onde uma API aberta atende desenvolvedores externos com quem você não consegue se coordenar e a transparência é muitas vezes obrigatória, uma interface utilizável, bem documentada e localizável faz parte da obrigação de prestação de contas pública, não é um mimo.

## Perspectiva por setor

**Startup.** Com duas ou três pessoas engenheiras e sem tempo para cerimônia, mantenha o contrato leve mas real: uma única especificação legível por máquina com a qual seus primeiros clientes parceiros de design possam se integrar enquanto você constrói. Não monte ainda um gateway de API, um catálogo nem um conselho de governança, mas fixe os dois hábitos que são dolorosos de acrescentar depois, chaves de idempotência nas escritas e paginação por cursor nas listagens, porque adaptá-los a um endpoint em produção é uma mudança que quebra e que você não pode bancar. Favoreça um único estilo de interação, quase sempre REST, para não carregar proliferação de protocolos no seu primeiro ano.

**Pequena empresa.** Sem especialista dedicado em API e com orçamento apertado, apoie-se em ferramentas que gerem documentação, servidores simulados e esqueletos de cliente a partir de uma especificação, para que um generalista consiga manter a interface sem profunda especialização em protocolos. Pese com firmeza comprar versus construir: um gateway pronto ou uma plataforma de gestão de APIs dá a você limitação de taxa, chaves e um portal do desenvolvedor que você de outro modo montaria à mão. Mantenha a superfície pequena e as convenções consistentes, já que cada endpoint extra e cada formato de erro avulso é algo que uma equipe enxuta precisa apoiar para sempre.

**Grande empresa.** Entre muitas equipes autônomas, o problema central é a consistência sem virar gargalo: um guia de estilo compartilhado, uma revisão de padrões de API, um catálogo que torna as interfaces localizáveis e verificações automatizadas de compatibilidade retroativa na CI, para que uma quebra silenciosa quebre o build em vez de uma integração. Governe cada API como um produto com um responsável nomeado, um ciclo de vida e uma política publicada de descontinuação e meça a adoção, a carga de suporte e a frequência de mudanças que quebram, para que o portfólio continue saudável. Padronize os estilos de interação e as regras de versionamento em toda a organização, porque nessa escala a fragmentação é o padrão caro.

**Governo.** Regras de contratação, mandatos de padrões abertos e responsabilização pública moldam cada escolha. Publique o contrato abertamente, siga os padrões abertos obrigatórios e ofereça um ambiente de teste e documentação de referência para que desenvolvedores externos com quem você não consegue se coordenar possam se virar sozinhos. Trate a compatibilidade retroativa de longo prazo como um requisito de política, já que as integrações precisam sobreviver a administrações e trocas de fornecedor, e torne as mudanças que quebram raras, fortemente governadas e anunciadas com muita antecedência. Mantenha a API e a sua documentação transparentes o bastante para resistir ao escrutínio público e de auditoria e evite formatos proprietários que prenderiam uma futura administração.

## Exemplos

**Startup.** Uma startup em estágio inicial que lança sua primeira API pública escreve o contrato como uma especificação legível por máquina antes de programar, para que seus dois clientes parceiros de design possam se integrar a um servidor simulado enquanto o backend ainda está sendo construído. Mesmo com apenas um punhado de consumidores, acrescenta chaves de idempotência ao endpoint de cobrança e paginação por cursor a toda listagem, porque adaptá-las depois que os parceiros dependem da API significaria uma mudança que quebra e que ela não pode bancar. O contrato inicial custa um dia e poupa semanas de vaivém de suporte.

**Grande empresa.** Uma grande empresa de pagamentos expõe uma API REST pública a milhares de comerciantes. Todo endpoint de escrita aceita uma chave de idempotência, de modo que uma nova tentativa de rede nunca cria uma cobrança duplicada. Todo endpoint de listagem usa paginação por cursor. Os erros trazem códigos estáveis documentados numa referência pública. Uma política formal de descontinuação garante uma longa janela de suporte a qualquer versão, com aviso prévio e guias de migração. Essa disciplina é uma vantagem competitiva: os integradores confiam em que a API não vai quebrar por baixo deles.

**Governo.** Um serviço digital nacional publica uma API aberta para dados de cidadãos, seguindo padrões abertos obrigatórios e um processo de design com API primeiro. O contrato é especificado e revisado antes da construção, publicado num catálogo central de APIs do governo e servido com um ambiente de teste, de modo que desenvolvedores de terceiros, que não podem ser coordenados individualmente, consigam se integrar por conta própria. A compatibilidade retroativa de longo prazo é um requisito de política, porque as integrações precisam sobreviver a administrações e trocas de fornecedor. Por isso as mudanças que quebram são raras e fortemente governadas.

## Justificativa de negócio: motivações, ROI e TCO

Um bom design de API reduz o custo de integração, que muitas vezes é o maior custo de conectar sistemas e integrar parceiros. Com uma API clara, estável e bem documentada, os consumidores se integram em dias sem um único chamado de suporte. Uma ruim gera carga de suporte infinita, integrações fracassadas e dano à reputação. Quando a API é ela mesma o produto, a experiência do desenvolvedor impulsiona diretamente a adoção e a receita.

O maior custo oculto são as mudanças que quebram. Toda mudança que quebra força uma migração coordenada entre todos os consumidores, equipes internas e parceiros externos igualmente, e o custo total cresce com o número de consumidores e com a dificuldade que eles têm de se mover em sincronia. Investir de início em design guiado por contrato, compatibilidade retroativa e disciplina de versionamento evita esses eventos de migração caros e que atingem toda a organização. Ao falar com a liderança, apresente a qualidade da API como o ponto de alavancagem para a autonomia das equipes, o crescimento do ecossistema de parceiros e a prevenção de migrações forçadas caras. Acompanhe o tempo de integração, o volume de chamados de suporte e a frequência de mudanças que quebram como sua evidência.

## Antipadrões e armadilhas

- **APIs com implementação primeiro:** a interface vaza a estrutura interna do banco de dados e muda sempre que a implementação muda.
- **Mudanças que quebram em silêncio:** reaproveitar um campo ou endurecer a validação sem aumentar a versão quebra os consumidores de forma imprevisível.
- **Interfaces tagarelas:** designs que exigem muitas idas e vindas para uma única operação lógica, prejudicando o desempenho e a usabilidade.
- **Convenções inconsistentes:** cada endpoint inventa a própria nomenclatura, formato de erro e paginação, de modo que os clientes não conseguem generalizar.
- **Sem paginação nem limitação de taxa:** endpoints que funcionam em teste e colapsam sob volume real de dados ou de carga.
- **Escritas não idempotentes:** as novas tentativas causam duplicatas. Um único soluço de rede corrompe dados.
- **Proliferação de versões:** versões ativas demais, sem descontinuação, multiplicando a manutenção até ela se tornar ingerenciável.
- **Documentação como reflexão tardia:** referências sem documentação ou desatualizadas que empurram todo o custo de integração para os consumidores.

## Modelo de maturidade

- **Nível 1, Iniciar:** As APIs surgem da implementação como subproduto. Não há convenções compartilhadas. A interface vaza a estrutura interna do banco de dados. As mudanças que quebram são comuns, sem aviso e descobertas quando a integração de um consumidor falha.
- **Nível 2, Desenvolver:** Algumas equipes seguem convenções básicas de REST, versionam informalmente e escrevem a documentação à mão, mas a prática é inconsistente entre as equipes. Idempotência, paginação e limitação de taxa aparecem em alguns endpoints e em outros não. Os consumidores ainda aprendem as peculiaridades de cada API caso a caso.
- **Nível 3, Padronizar:** O design guiado por contrato com especificações legíveis por máquina é documentado e imposto em toda a organização. Uma política publicada de descontinuação, uma semântica de erros consistente e idempotência, paginação por cursor e limitação de taxa obrigatórias se aplicam a todo novo endpoint. Um guia de estilo compartilhado e uma revisão de padrões de API mantêm as interfaces consistentes entre as equipes.
- **Nível 4, Gerenciar:** O portfólio de APIs é medido e controlado em relação a linhas de base: verificações automatizadas de compatibilidade retroativa funcionam como portão de cada mudança na CI, e você acompanha o tempo até a primeira chamada bem-sucedida, o volume de chamados de suporte por endpoint, a frequência de mudanças que quebram, a contagem de versões ativas e o uso por endpoint, de modo que as decisões de descontinuação e de design se apoiam em evidências e não em opinião. Cada API é um produto governado num catálogo, com um responsável nomeado, e as métricas disparam ação quando um serviço se afasta de suas metas.
- **Nível 5, Orquestrar:** A estratégia de API é continuamente melhorada e integrada em toda a organização. O catálogo, o gateway, as regras de versionamento e os portões de compatibilidade funcionam como um só sistema. A organização rotineiramente aposenta, consolida e redefine o escopo de interfaces com base em adoção e custo medidos. Os padrões de estilo de interação e de versionamento se adaptam conforme o ecossistema, os parceiros e a tecnologia mudam, e as mudanças que quebram são raras e bem geridas.

## Ideias para discussão

- Como você decide quando uma API interna está estável o bastante para ser publicada externamente?
- Qual é a janela certa de suporte para versões descontinuadas no seu contexto, e quem paga por ela?
- Onde o GraphQL ou o gRPC devem substituir o REST internamente, e onde acrescentariam mais complexidade que valor?
- Como você impõe a consistência das APIs entre muitas equipes autônomas sem virar gargalo?
- Como as APIs consumíveis por IA e as interfaces de ferramentas de agentes devem mudar as suas convenções de design?
- Que verificações automatizadas conseguem pegar mudanças incompatíveis com versões anteriores antes de serem entregues?

## Principais conclusões

- Projete o contrato primeiro. A API é um produto e uma promessa de longa vida.
- A compatibilidade retroativa protege os consumidores. Mudanças que quebram exigem novas versões e caminhos de migração.
- Escolha REST, GraphQL, gRPC ou eventos pelo encaixe da interação, não pela moda.
- Embuta idempotência, paginação, limitação de taxa e erros consistentes desde o primeiro dia.
- Governe as APIs como produtos, com responsáveis, catálogos e uma forte experiência do desenvolvedor.

## Referências e leitura complementar

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
