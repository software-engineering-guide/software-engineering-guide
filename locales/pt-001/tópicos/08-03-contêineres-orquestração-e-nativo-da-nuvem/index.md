# 8.3 Contêineres, orquestração e cloud-native

## Visão geral e motivação

Um [contêiner](https://en.wikipedia.org/wiki/OS-level_virtualization) empacota uma aplicação junto com suas dependências numa única unidade portável e isolada. Ele roda do mesmo jeito num laptop, num ambiente de teste e em produção. As plataformas de orquestração, em especial o [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), agendam e gerenciam grandes quantidades de contêineres em frotas de máquinas. Elas cuidam de posicionamento, escala, saúde, rede e recuperação. O [cloud-native](https://en.wikipedia.org/wiki/Cloud-native_computing) é o estilo arquitetural mais amplo construído sobre essas fundações: aplicações projetadas como serviços pouco acoplados, implantáveis de forma independente e escaláveis na horizontal, que pressupõem uma infraestrutura dinâmica e autocurável.

Para grandes equipes, contêineres e orquestração resolvem um problema difícil. Vocês precisam rodar muitos serviços, construídos por muitas equipes, de modo confiável e eficiente em infraestrutura compartilhada. Os contêineres dão a cada equipe um contrato consistente de empacotamento e de execução, o que aposenta a classe de falhas do “funciona na minha máquina”. A orquestração esconde as máquinas individuais atrás de um substrato comum, de modo que as equipes implantam numa plataforma e não em servidores. Essa padronização é o que permite operar centenas ou milhares de serviços sem que cada equipe reinvente a implantação, a escala e a resiliência.

As organizações corporativas e governamentais que adotam ganham portabilidade, resiliência e um caminho para longe do aprisionamento (lock-in). Em troca, herdam complexidade real e novas responsabilidades de segurança. Uma plataforma de contêineres é poderosa precisamente porque é programável e dinâmica, o que significa que vocês precisam governá-la com cuidado. A procedência das imagens, o isolamento multilocatário, a política de rede e o custo viram todos preocupações de nível de plataforma. Os adotantes do setor público acrescentam cada vez mais exigências de soberania: controle sobre onde os dados residem e quem pode acessá-los. Isso faz da capacidade de rodar cargas consistentes em ambientes escolhidos uma capacidade estratégica, não só um detalhe técnico.

## Princípios fundamentais

- Empacotem as aplicações como imagens de contêiner pequenas, de propósito único e imutáveis.
- Pratiquem a higiene de imagens: imagens-base mínimas, versões fixadas, varredura de vulnerabilidades e assinatura.
- Projetem as aplicações para serem sem estado e escaláveis na horizontal sempre que possível, externalizando o estado.
- Tratem o modelo de estado desejado da plataforma de orquestração como a fonte da verdade e deixem-na se autocurar.
- Imponham isolamento e menor privilégio entre locatários, cargas e namespaces.
- Sigam os princípios [twelve-factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), uma metodologia para construir aplicações descartáveis, com configuração externalizada e escaláveis na horizontal, e estendam-nos para as realidades dos sistemas distribuídos.
- Façam do custo uma preocupação de engenharia de primeira classe e visível, não uma reflexão tardia.
- Prefiram abstrações portáveis e baseadas em padrões para preservar a flexibilidade estratégica.

## Recomendações

### Pratique uma higiene rigorosa de imagens

A imagem de contêiner é a sua unidade fundamental de confiança e de implantação, então tratem-na como tal. Comecem de imagens-base mínimas e confiáveis para encolher a superfície de ataque. Fixem as versões de dependências e de imagens-base por reprodutibilidade. Varram toda imagem em busca de vulnerabilidades conhecidas no pipeline de build e bloqueiem as que tenham achados críticos. Assinem as imagens e verifiquem as assinaturas na hora da implantação, para que só imagens aprovadas e sem modificação rodem. Mantenham um registro interno curado de imagens-base endurecidas a partir das quais as equipes constroem. Isso espalha bons padrões de segurança automaticamente.

### Use os padrões do Kubernetes em vez de reinventá-los

O Kubernetes recompensa as equipes que adotam seus padrões estabelecidos e pune as que brigam com o seu modelo. Usem manifestos declarativos para o estado desejado. Acrescentem sondas de saúde para que a plataforma possa detectar e substituir instâncias não saudáveis. Definam requisições e limites de recursos para que o escalonador possa empacotar as cargas com segurança. Usem o autoescalonamento horizontal para demanda elástica. Para a lógica operacional que precisa rodar continuamente, como gerenciar um banco de dados, rotacionar certificados ou reconciliar recursos personalizados, usem o padrão de operador, que codifica o conhecimento operacional humano em software que vigia o estado e age. Resistam à vontade de construir orquestração sob medida sobre a plataforma. Prefiram as construções nativas.

### Projete o multilocatário deliberadamente

Quando muitas equipes compartilham um cluster, o isolamento é uma exigência de segurança e de confiabilidade, não um luxo. Usem namespaces como fronteiras de locação. Imponham cotas de recursos para que nenhum locatário esgote os outros. Apliquem políticas de rede para restringir o tráfego ao que é explicitamente permitido. Usem o [controle de acesso baseado em papéis](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) para limitar o que cada equipe pode fazer. Para cargas com necessidades mais fortes de isolamento, considerem clusters separados ou um sandboxing mais forte. Decidam cedo se o seu modelo é de multilocação branda (equipes internas confiáveis) ou rígida (cargas que desconfiam umas das outras), porque os dois exigem controles muito diferentes.

### Construa cloud-native, twelve-factor e além

A metodologia twelve-factor, com suas dependências explícitas, configuração no ambiente, processos sem estado, descartabilidade e assim por diante, continua sendo uma excelente base para serviços que prosperam numa plataforma dinâmica. Estendam-na para as realidades adicionais dos sistemas distribuídos. Projetem para a falha parcial. Tornem as operações idempotentes e repetíveis. Exponham saúde e telemetria. Tratem a observabilidade como uma funcionalidade embutida e não um complemento. Externalizem todo o estado para serviços de dados gerenciados, de modo que as instâncias da aplicação permaneçam descartáveis e escaláveis na horizontal.

### Planeje estratégias multicloud, híbridas e soberanas de modo pragmático

A portabilidade é valiosa, mas persigam-na com olhos abertos. Padronizem em abstrações portáveis como contêineres, Kubernetes e APIs abertas, para que as cargas possam se mover se for preciso. Mas evitem a armadilha de recusar todo serviço gerenciado, que troca produtividade real por portabilidade hipotética. Para exigências híbridas e soberanas, projetem de modo que as mesmas cargas e pipelines possam rodar numa região escolhida, num data center privado ou numa nuvem soberana que atenda às regras jurisdicionais e de residência de dados. Tornem explícitas, na arquitetura e na política, as fronteiras de soberania e de residência.

### Torne o custo visível com FinOps

Em ambientes de nuvem elásticos, o custo é consequência direta de decisões de engenharia, então deem aos engenheiros visibilidade e responsabilização. Etiquetem os recursos para alocação de custos. Atribuam o gasto a equipes e serviços. Mostrem os dados de custo ao lado das métricas de desempenho. Dimensionem as cargas corretamente, usem o autoescalonamento para acompanhar a demanda e recuperem os recursos ociosos. Estabeleçam uma prática de FinOps que reúna engenharia, finanças e produto, para que o gasto em nuvem seja uma responsabilidade compartilhada e contínua e não uma surpresa trimestral.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| Kubernetes | Poderoso, portável, enorme ecossistema | Complexidade íngreme. Fardo operacional | Muitos serviços em escala |
| Serviço gerenciado de contêineres | Menos fardo operacional. Início mais rápido | Algum aprisionamento. Menos controle | Equipes que querem simplicidade |
| Um único cluster compartilhado | Uso eficiente de recursos | Isolamento mais difícil. Raio de impacto | Locatários internos confiáveis |
| Um cluster por locatário | Isolamento forte | Maior custo e sobrecarga | Cargas desconfiadas ou reguladas |
| Portabilidade multicloud | Flexibilidade. Evita aprisionamento | Serviços de menor denominador comum | Mitigação de risco estratégico |
| Serviços gerenciados profundos de uma só nuvem | Produtividade máxima | Dependência do fornecedor | Equipes focadas em velocidade |

O compromisso abrangente é capacidade versus complexidade. O Kubernetes e as arquiteturas cloud-native entregam elasticidade, resiliência e velocidade. Mas impõem um fardo operacional e cognitivo substancial que as equipes pequenas rotineiramente subestimam. Do mesmo modo, perseguir a portabilidade [multicloud](https://en.wikipedia.org/wiki/Multicloud) plena troca produtividade por opcionalidade. A resposta certa depende da escala e do risco. As grandes organizações, com muitas equipes e fortes necessidades de governança, em geral justificam o investimento. Esforços menores muitas vezes são mais bem servidos por serviços gerenciados que escondem a complexidade.

## Perguntas para discutir com sua equipe

1. **Vocês assinam as imagens e verificam as assinaturas na hora da implantação, e uma vulnerabilidade crítica de fato bloqueia o build?** A imagem é a sua unidade de confiança, então a cadeia de suprimentos ao redor dela merece portões duros e não avisos. Decidam se somente imagens assinadas e verificadas podem rodar, se a varredura bloqueia os achados críticos ou apenas os registra e quem mantém o registro curado de imagens-base endurecidas a partir das quais as equipes constroem. Para cargas corporativas e governamentais isso é frequentemente uma exigência de conformidade, e também é a sua melhor defesa contra uma dependência envenenada chegar à produção. Levem o estado atual: que fração das imagens em execução vem da sua base endurecida, quantas carregam CVEs críticas sem correção e se alguma imagem não assinada pode hoje ser agendada. Se um achado crítico não interrompe uma implantação, o seu scanner é decoração.

2. **Como as requisições, os limites e as cotas de recursos impedem que uma carga esgote as vizinhas, sem deixar ociosa uma capacidade cara?** Num cluster compartilhado, uma carga sem limites pode derrubar ou estrangular tudo ao redor, e cotas fixadas de forma generosa demais desperdiçam os ganhos de utilização que justificam a plataforma. Decidam padrões sensatos, quem os ajusta e como pegam cargas sem nenhuma requisição definida. Em escala, isso é ao mesmo tempo um controle de confiabilidade e de custo, porque o dimensionamento correto é onde mora grande parte da economia de FinOps. Levem dados: a utilização atual do cluster, com que frequência as cargas são despejadas ou estranguladas e quais namespaces não têm cotas. O objetivo é um empacotamento denso e seguro, então tratem a ausência de limites como um defeito que a plataforma rejeita.

3. **Que estado pode viver dentro de um contêiner, e para onde vai todo o resto?** A resiliência cloud-native depende de instâncias descartáveis que a plataforma pode reagendar à vontade, e isso só vale se o estado importante vive em serviços de dados gerenciados e não no disco local do contêiner. Decidam a regra explicitamente, porque um estado guardado num contêiner por acidente vira perda de dados no próximo reagendamento. Para as equipes que migram aplicações mais antigas, essa costuma ser a parte mais difícil, já que os serviços legados pressupõem um sistema de arquivos local estável. Levem um inventário: quais serviços gravam estado local, quais dependem de sessões fixas ou de afinidade de nó e o que seria preciso para externalizar cada um. Enquanto o estado não for externo, vocês têm contêineres que parecem elásticos mas que na prática não podem ser movidos.

4. **Quando muitas equipes compartilham um cluster, o seu modelo de isolamento é escolhido deliberadamente como multilocação branda ou rígida, e os controles correspondem a essa escolha?** Os namespaces separam equipes internas confiáveis, mas não contêm uma carga ativamente hostil ou comprometida, e tratar a locação branda como se fosse rígida é um incidente de segurança esperando para acontecer. Decidam por carga se os locatários apenas precisam de compartilhamento justo ou devem ser presumidos como desconfiados uns dos outros e depois alinhem os controles: namespaces, cotas, políticas de rede e RBAC para o caso brando, clusters separados ou sandboxing mais forte para o caso rígido. Para uma grande organização, essa decisão conduz o custo diretamente, porque um cluster por locatário é muito mais caro que namespaces compartilhados, então vocês querem gastar o orçamento de isolamento apenas onde o modelo de ameaça exige. Levem o inventário de locatários: quais cargas compartilham um cluster hoje, quais lidam com tráfego regulado ou voltado ao exterior e onde a política de rede ainda é de permissão por padrão. Em contextos corporativos e governamentais, misturar cargas desconfiadas sob locação branda é exatamente o achado que um auditor apontará, então nomeiem a fronteira antes que ele o faça.

5. **Quanto vocês estão pagando pela portabilidade multicloud, e vocês algum dia de fato a usarão?** Padronizar em contêineres, Kubernetes e APIs abertas mantém as cargas movíveis, mas recusar todo serviço gerenciado para preservar essa opção troca produtividade diária e real por uma portabilidade que a organização talvez nunca exerça. Decidam onde a portabilidade é uma exigência genuína, como uma obrigação de soberania ou de saída que vocês assinaram, versus onde é um cobertor de conforto que atrasa todas as equipes. A consideração concorrente é a velocidade: os serviços gerenciados profundos entregam funcionalidades mais depressa, e uma arquitetura de menor denominador comum é um imposto permanente sobre cada equipe. Levem as evidências: quais serviços gerenciados vocês evitaram e quanto isso custou em tempo de engenharia, se alguma vez moveram uma carga entre provedores e a que os seus contratos de fato obrigam. Para adotantes governamentais e regulados, as regras de residência de dados e de nuvem soberana podem tornar a portabilidade inegociável, então projetem para que os mesmos manifestos e pipelines rodem numa região soberana e num enclave privado, mas sejam honestos de que isso é um custo de conformidade e não um seguro grátis.

6. **Cada equipe consegue ver o que gasta, e alguém é dono da conta antes de ela virar surpresa?** Numa plataforma elástica, o custo é uma saída direta das decisões de engenharia, mas sem etiquetas de alocação de custos e painéis visíveis o gasto se acumula num fundo comum pelo qual ninguém se sente responsável até as finanças escalarem. Decidam como atribuem o custo a equipes e serviços, quem o revisa e se os engenheiros veem o custo ao lado das métricas de desempenho ou só ouvem falar dele uma vez por trimestre. A tensão é entre responsabilização e atrito: pressionem o custo demais e toda decisão vira uma negociação de orçamento, ignorem-no e cargas ociosas e superdimensionadas se acumulam em silêncio. Levem os números: o gasto atual por equipe, quanta capacidade está ociosa ou superdimensionada e com que rapidez uma carga fora de controle seria notada. Para orçamentos corporativos e governamentais, o gasto em nuvem sem atribuição é ao mesmo tempo uma falha de governança e um risco financeiro real, então montem uma prática de FinOps que ponha engenharia, finanças e produto na mesma conversa e não reconciliando depois do fato.

## Perspectiva por setor

**Startup.** Recorram a um serviço gerenciado de contêineres e não a um cluster Kubernetes autohospedado: com um par de serviços e sem engenheiro de plataforma, os planos de controle são uma distração que vocês não podem bancar. Empacotem imagens pequenas a partir de uma base mínima, fixem as versões, acrescentem uma varredura de vulnerabilidades ao build e ponham todo o estado num banco de dados gerenciado para que as instâncias permaneçam descartáveis. Pulem namespaces, operadores e portabilidade multicloud até de fato terem os serviços e as pessoas que os justifiquem.

**Pequena empresa.** Sem especialista dedicado em plataforma e com orçamento apertado, apoiem-se fortemente em serviços gerenciados e deixem o provedor rodar a orquestração que vocês de outro modo teriam de manter com equipe. Tratem o básico dos contêineres como o seu piso de segurança: imagens mínimas, fixação de versões e uma varredura no pipeline dão a maior parte da proteção por pouco esforço. Favoreçam comprar uma plataforma com suporte a construir uma e mantenham portabilidade suficiente, contêineres padrão e APIs abertas, para não ficarem presos se o preço ou os termos mudarem.

**Grande empresa.** A tarefa é a governança de plataforma entre muitas equipes: uma equipe central de plataforma que fornece imagens-base endurecidas, portões de assinatura e de varredura, locação por namespace com cotas, política de rede e RBAC, além de etiquetas de alocação de custos e um painel de FinOps. Padronizem o contrato de implantação para que centenas de serviços operem do mesmo jeito e gerenciem a segurança, a multilocação e o custo centralmente enquanto as equipes se servem sozinhas na implantação. Financiem a equipe de plataforma como se deve, porque uma plataforma com poucos recursos vira o gargalo pelo qual toda a organização espera.

**Governo.** A soberania, a residência de dados e a prestação de contas públicas moldam a arquitetura. Rodem as cargas em contêineres e Kubernetes padrão para que os mesmos pipelines rodem numa região soberana e num enclave local acreditado e codifiquem as fronteiras de residência e de acesso como política e não como convenção. Tirem as imagens de um registro interno endurecido, apliquem multilocação rígida aos dados mais sensíveis e mantenham a portabilidade que dá resiliência e poder de negociação, já que as regras de contratação muitas vezes proíbem o aprisionamento a um único fornecedor.

## Exemplos

**Startup.** Uma startup de seis pessoas empacota seus dois serviços como pequenas imagens de contêiner construídas a partir de uma base mínima e os roda num serviço gerenciado de contêineres, e não num cluster Kubernetes autohospedado, de modo que ninguém precise cuidar de planos de controle. Eles fixam as versões das imagens-base e acrescentam uma varredura de vulnerabilidades ao build, mas deliberadamente pulam os recursos mais pesados de orquestração até de fato terem mais que um punhado de serviços. O estado vive num banco Postgres gerenciado, o que mantém os contêineres descartáveis e deixa a plataforma reiniciá-los ou escalá-los sem nenhuma perda de dados.

**Grande empresa.** Uma empresa de telecomunicações roda várias centenas de [microsserviços](https://en.wikipedia.org/wiki/Microservices) em clusters Kubernetes compartilhados. Uma equipe de plataforma fornece imagens-base endurecidas, impõe assinatura de imagens e portões de vulnerabilidade e isola as unidades de negócio em namespaces com cotas, políticas de rede e RBAC. Etiquetas de alocação de custos e um painel de FinOps atribuem o gasto a cada linha de produto, e o autoescalonamento dimensiona a capacidade à demanda. As equipes de produto implantam dezenas de vezes por dia numa plataforma consistente sem gerenciar servidores. A empresa mantém o controle central sobre segurança e custo.

**Governo.** Um serviço nacional de saúde precisa manter os dados dos cidadãos dentro das fronteiras nacionais e sob controle legal nacional. Ele roda suas cargas numa região de nuvem soberana usando contêineres e Kubernetes padrão, de modo que os mesmos pipelines e manifestos rodam também num ambiente local acreditado para os dados mais sensíveis. As fronteiras de residência de dados e de acesso são codificadas como política, as imagens vêm de um registro interno endurecido e a multilocação rígida isola as cargas sensíveis. A portabilidade entre a região soberana e o enclave privado dá ao serviço resiliência e poder de negociação sem sacrificar a conformidade.

## Justificativa de negócio: motivações, ROI e TCO

O ROI dos contêineres e da orquestração vem de maior utilização de recursos, implantações mais rápidas e confiáveis, escala elástica que acompanha o gasto à demanda e resiliência melhorada por meio da autocura. Padronizar numa plataforma comum reduz o esforço duplicado entre as equipes e acelera a integração de novos membros, porque todo serviço segue o mesmo contrato de implantação e de operação.

A análise de TCO precisa ser honesta sobre o fardo operacional. Os custos de adoção incluem equipe de engenharia de plataforma, treinamento, ferramentas de segurança para imagens e clusters e o esforço contínuo de rodar a própria plataforma. O custo de não adotar inclui implantação sob medida e inconsistente entre as equipes, má utilização de infraestrutura cara, escala manual frágil e dificuldade em cumprir exigências de resiliência e de soberania. Para a liderança, o argumento repousa na escala. Abaixo de um certo número de serviços a complexidade pode não compensar, e um serviço gerenciado é mais sábio. Mas em escala corporativa e governamental, uma plataforma cloud-native governada costuma ser a fundação mais econômica e resiliente, desde que vocês financiem a equipe de plataforma para rodá-la como se deve.

## Antipadrões e armadilhas

- **Imagens gordas e sem varredura.** Imagens inchadas, construídas de bases não confiáveis, carregam vulnerabilidades desnecessárias e deixam tudo mais lento.
- **Kubernetes para tudo.** Adotar um orquestrador complexo para um punhado de serviços simples compra complexidade sem retorno.
- **Ignorar os limites de recursos.** Sem requisições e limites, uma carga pode esgotar ou derrubar as vizinhas.
- **Locação branda para cargas hostis.** Depender só de namespaces para isolar locatários desconfiados é um incidente de segurança esperando para acontecer.
- **Contêineres com estado por acidente.** Guardar estado importante em contêineres descartáveis leva à perda de dados no reagendamento.
- **Cegueira de custo.** Tratar o gasto em nuvem como custo fixo e não como saída de engenharia leva a contas descontroladas.
- **Teatro de portabilidade.** Recusar todos os serviços gerenciados para preservar uma portabilidade que a organização nunca vai de fato usar.

## Modelo de maturidade

**Nível 1: Iniciar.** Os contêineres são usados ad hoc, se tanto. As imagens são construídas à mão e sem varredura, a implantação é manual e reativa e não há plataforma compartilhada, nem visibilidade de custo, nem modelo de isolamento.

**Nível 2: Desenvolver.** As equipes conteinerizam as aplicações e adotam um orquestrador, mas as práticas variam entre os grupos. A varredura de imagens, os limites de recursos e a assinatura são inconsistentes, e o custo e a multilocação não são governados de forma sistemática.

**Nível 3: Padronizar.** Uma plataforma padronizada é documentada e imposta em toda a organização: imagens-base endurecidas, portões de assinatura e de varredura, locação baseada em namespaces com cotas e política de rede, RBAC e alocação de custos. Os padrões cloud-native e twelve-factor são a norma esperada e não uma escolha local.

**Nível 4: Gerenciar.** A plataforma é medida e controlada em relação a linhas de base. Vocês acompanham a utilização do cluster, a fração das imagens em execução construídas da base endurecida, as vulnerabilidades críticas sem correção, a frequência de implantação e a taxa de falha de mudanças, as taxas de despejo e de estrangulamento e o custo por equipe e serviço em relação ao orçamento. Os portões são impostos com base nessas evidências: a ausência de limites de recursos e as imagens não assinadas são rejeitadas automaticamente, e o desvio do padrão dispara ação e não um aviso.

**Nível 5: Orquestrar.** A plataforma é de autoatendimento e autocurável, integrada em toda a organização e adaptativa. O FinOps continuamente dimensiona e recupera capacidade, a arquitetura portável sustenta as exigências híbridas e soberanas e a plataforma melhora continuamente a partir do uso medido, aposentando e substituindo componentes conforme as cargas, o custo e o quadro de risco mudam.

## Ideias para discussão

- Em que escala adotar o Kubernetes deixa de ser complexidade por si só e começa a compensar?
- Onde fica a fronteira certa entre a multilocação branda e a rígida para as suas cargas?
- Quanto vocês devem investir em portabilidade multicloud versus na produtividade dos serviços gerenciados profundos?
- Como vocês dão aos engenheiros uma responsabilização real pelo custo sem transformar toda decisão numa negociação de orçamento?
- Qual é o seu modelo de governança para imagens-base, e quem mantém o registro endurecido?
- Como as exigências de soberania e de residência de dados moldam a arquitetura da sua plataforma?

## Principais conclusões

- Os contêineres padronizam o empacotamento e a execução. A orquestração padroniza a operação em escala.
- A higiene de imagens, isto é, imagens mínimas, fixadas, varridas e assinadas, é a segurança fundamental.
- Usem os padrões nativos do Kubernetes e os operadores em vez de construir orquestração sob medida.
- Escolham um modelo de multilocação deliberadamente, conforme quanto as cargas confiam umas nas outras.
- Sigam o twelve-factor e estendam-no para as realidades dos sistemas distribuídos, como a falha parcial e a observabilidade.
- Tratem o custo como uma saída de engenharia e gerenciem-no continuamente por meio do FinOps.

## Referências e leitura complementar

- Adam Wiggins, *The Twelve-Factor App* (methodology).
- Brendan Burns, Joe Beda, and Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment and Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), cloud-native definition and landscape.
