# 1.2 Topologias de equipes e desenho organizacional

## Visão geral e motivação

A forma como você divide as pessoas em equipes determina que software você consegue construir e com que rapidez. Isso não é uma metáfora. É uma consequência quase mecânica conhecida como [lei de Conway](https://en.wikipedia.org/wiki/Conway%27s_law): as organizações projetam sistemas que espelham suas próprias estruturas de comunicação. Se três equipes constroem um [compilador](https://en.wikipedia.org/wiki/Compiler), você obtém um compilador de três passagens. Se a lógica de pagamentos está dividida entre uma equipe de frontend, uma de backend e uma de banco de dados, toda mudança em pagamentos exige coordenação a três. Para uma organização pequena, isso é administrável. Para uma grande, o formato do organograma se torna a restrição dominante sobre sua engenharia, sua arquitetura, sua velocidade de entrega e sua qualidade. Por isso, desenhar a estrutura das equipes é uma atividade de engenharia de primeira classe, não uma reflexão tardia do RH.

As topologias de equipes oferecem um vocabulário deliberado para esse desenho. Em vez de deixar a estrutura se acumular ao acaso por meio de reorganizações e de contagem de pessoas, as organizações maduras escolhem tipos de equipe e modos de interação de propósito, e revisitam essas escolhas conforme o sistema e o negócio evoluem. O objetivo é manter baixa a [carga cognitiva](https://en.wikipedia.org/wiki/Cognitive_load) de cada equipe, o total que ela precisa manter na cabeça para ser eficaz, de modo que as equipes possam ser donas do seu domínio de ponta a ponta e entregar um fluxo constante de valor sem esperar o tempo todo pelas outras.

Para empresas e governo, essa disciplina é decisiva. Grandes organizações se espalham naturalmente em hierarquias profundas, serviços compartilhados com filas longas e cadeias de repasses que transformam uma mudança de dois dias em um projeto de dois meses. O governo acrescenta fronteiras de contratação, equipes terceirizadas e [segregações de funções](https://en.wikipedia.org/wiki/Separation_of_duties) obrigatórias que fragmentam ainda mais a responsabilidade. O desenho explícito de topologia é como essas organizações recuperam o fluxo: alinhar equipes a fluxos de valor, construir plataformas que reduzem a carga cognitiva e escolher padrões de interação que tornem as dependências visíveis e intencionais, em vez de ocultas e constantes.

## Princípios fundamentais

- A lei de Conway é inescapável. Desenhe as equipes para corresponder à engenharia de software que você deseja (a “manobra inversa”).
- Otimize a carga cognitiva da equipe, não a utilização máxima dos indivíduos.
- Prefira equipes alinhadas ao fluxo, que são donas de uma fatia de valor de ponta a ponta.
- Plataformas existem para reduzir a carga cognitiva das equipes alinhadas ao fluxo, não para servir de cancela.
- Torne as interações entre equipes explícitas e poucas: colaboração, X como serviço ou facilitação.
- Minimize dependências. Cada repasse entre equipes é uma fila e um risco.
- A estrutura das equipes é um desenho vivo que precisa evoluir conforme o sistema e o negócio mudam.

## Recomendações

### Use os quatro tipos fundamentais de equipe

As topologias de equipes definem quatro tipos que cobrem a maioria das necessidades. As equipes alinhadas ao fluxo são o padrão: cada uma é dona de um fluxo contínuo de trabalho para um produto, serviço ou jornada de usuário específico, de ponta a ponta. As equipes de plataforma fornecem produtos internos (computação, implantação, pipelines de dados, identidade) que as equipes alinhadas ao fluxo consomem em autosserviço, o que reduz a carga cognitiva delas. As equipes habilitadoras são especialistas (testes, segurança, observabilidade) que orientam as equipes alinhadas ao fluxo a construir uma capacidade e depois se afastam. As equipes de subsistema complicado são donas de componentes que exigem especialização profunda (um motor de preços, um [codec de vídeo](https://en.wikipedia.org/wiki/Video_codec), um módulo criptográfico), onde não faz sentido que todas as equipes detenham esse conhecimento. A maioria das suas equipes deve ser alinhada ao fluxo. Os outros três tipos existem para apoiá-las.

### Aplique a manobra inversa de Conway

Como o software espelha a estrutura da sua organização, molde suas equipes para produzir o software que você deseja. Quer serviços fracamente acoplados com fronteiras claras? Crie equipes fracamente acopladas com fronteiras claras de responsabilidade. Quer uma capacidade de pagamentos que seja lançada em seu próprio ritmo? Forme uma equipe de pagamentos que seja dona dela de ponta a ponta. Não lute contra a lei de Conway com coordenação heroica. Redesenhe as fronteiras das equipes para que a arquitetura que você quer se torne o caminho de menor resistência.

### Gerencie a carga cognitiva explicitamente

Uma equipe só consegue dominar uma certa quantidade. A carga cognitiva inclui a complexidade do domínio, as tecnologias, o fardo operacional e a amplitude das partes interessadas. Quando uma equipe é dona de serviços demais e sem relação entre si, qualidade e velocidade colapsam juntas. Portanto, delimite as responsabilidades de cada equipe a um domínio que ela consiga realmente dominar, e use plataformas e equipes habilitadoras para tirar do seu prato a complexidade indiferenciada. Mantenha as equipes com cerca de cinco a nove pessoas: pequenas o bastante para se comunicarem com facilidade e para serem alimentadas, por assim dizer, com duas pizzas.

### Escolha os modos de interação deliberadamente

Limite as interações entre equipes a três modos. Colaboração é o trabalho próximo e de alta largura de banda entre duas equipes por um período determinado. É poderosa para a descoberta, mas cara, então mantenha-a temporária. X como serviço é uma relação limpa de provedor e consumidor com uma interface bem definida, ideal para o consumo de plataformas em escala. Facilitação é uma equipe ajudando outra a aprender, que é o que as equipes habilitadoras fazem. Nomeie o modo de cada relação importante entre equipes e leia a colaboração de longa duração entre as mesmas duas equipes como um sinal de que a fronteira delas está no lugar errado.

### Escolha um modelo operacional para as funções transversais

Segurança, dados, design e disciplinas semelhantes podem ser organizados de três maneiras: centralizado (uma equipe é dona para todos), federado (especialistas incorporados em tempo parcial, coordenando-se por meio de uma guilda) ou incorporado (um especialista dedicado dentro de cada equipe alinhada ao fluxo). O centralizado dá consistência e profundidade, mas vira gargalo. O incorporado dá velocidade e contexto, mas arrisca inconsistência e duplicação. O federado (muitas vezes um modelo de eixo e raios ou de [comunidade de prática](https://en.wikipedia.org/wiki/Community_of_practice)) fica entre os dois. Escolha por função e por escala. A maioria das grandes organizações acaba no federado para essas disciplinas, com um pequeno núcleo central que define os padrões.

### Invista em inner-source

O [inner-source](https://en.wikipedia.org/wiki/Inner_source) traz os padrões de colaboração do [código aberto](https://en.wikipedia.org/wiki/Open-source_software) para dentro da organização: repositórios internos compartilhados, diretrizes de contribuição publicadas, [revisão de código](https://en.wikipedia.org/wiki/Code_review) entre fronteiras de equipe e mantenedores claros. Quando uma equipe precisa de uma mudança no componente de outra, ela pode contribuir com a mudança diretamente em vez de abrir um chamado e esperar numa fila. Isso alivia as dependências entre equipes sem dissolver a responsabilidade, e espalha conhecimento e padrões naturalmente por uma grande população de engenharia.

## Compromissos: prós e contras

| Modelo para funções transversais | Prós | Contras |
| --- | --- | --- |
| Centralizado (uma equipe para todos) | Consistência, especialização profunda, padrões claros | Gargalo, filas, perda de contexto de produto |
| Federado (eixo e raios, guildas) | Equilibra consistência e velocidade. Compartilha conhecimento | Exige disciplina de coordenação. A responsabilização pode ficar difusa |
| Incorporado (especialista por equipe) | Rápido, rico em contexto, alta responsabilidade | Duplicação, inconsistência, difícil de dotar de pessoal em escala |

| Tipo de equipe | Melhor para | Risco se usada em excesso |
| --- | --- | --- |
| Alinhada ao fluxo | A maior parte da entrega de produtos e serviços | Nenhum. Este tipo deve dominar |
| Plataforma | Reduzir a carga cognitiva compartilhada | Vira uma cancela de torre de marfim |
| Habilitadora | Espalhar uma capacidade temporariamente | Vira uma dependência permanente |
| Subsistema complicado | Domínios genuinamente profundos de especialistas | Usada como desculpa para acumular trabalho comum |

O compromisso recorrente é autonomia versus consistência. Equipes totalmente autônomas se movem rápido, mas se afastam em padrões, ferramentas e postura de segurança. O controle totalmente centralizado mantém a consistência, mas estrangula o fluxo. Um bom desenho de topologia encontra a costura: autonomia para a entrega alinhada ao fluxo, mais padrões centrais enxutos e plataformas de caminho pavimentado (ferramentas padrão bem apoiadas que tornam fácil a escolha em conformidade) para aquilo que realmente precisa ser consistente.

## Perguntas para discutir com sua equipe

1. **Que sinais concretos dirão que a carga cognitiva de uma equipe está alta demais, antes que a qualidade colapse?** “Delimite cada equipe a um domínio que ela consiga dominar” é fácil de dizer e difícil de pôr em prática sem evidências, porque a carga cognitiva fica invisível até que a entrega e a confiabilidade se degradem. Observe sintomas mensuráveis: o número de serviços ou repositórios sem relação entre si pelos quais uma equipe responde, quanto tempo leva a integração, entre quantos domínios um único engenheiro precisa alternar o contexto numa semana e taxas crescentes de incidentes nos cantos do escopo da equipe. Para uma grande organização, isso importa porque equipes sobrecarregadas viram gargalos em silêncio, que nenhum diagrama de reorganização prevê. Leve esses números à discussão, junto com a percepção da própria equipe sobre o que consegue e o que não consegue manter na cabeça. Se os sinais indicarem sobrecarga, o movimento é transferir o trabalho indiferenciado para uma plataforma ou para uma equipe habilitadora, não exigir mais heroísmo.

2. **Uma reorganização realmente vale a perturbação aqui, ou você está alimentando um vício em reorganizações?** Redesenhar fronteiras para aplicar a manobra inversa de Conway é poderoso, e toda reorganização também destrói a estabilidade de que as equipes precisam para se entrosar e zera o conhecimento de domínio duramente conquistado. As considerações concorrentes são o imposto contínuo de coordenação da estrutura atual versus o custo único e o golpe na moral de mudá-la. Em contextos corporativos e governamentais, fronteiras de contratação, equipes terceirizadas e segregações obrigatórias de funções tornam as reorganizações mais lentas e caras, então a barra deve ser mais alta. Leve evidências de atraso causado por dependências: quantas iniciativas estão bloqueadas esperando outra equipe, e por quanto tempo. Reorganize quando essa espera for estrutural e grande, e resista a reembaralhar quando a dor for temporária ou mais barata de resolver com contribuições inner-source e interfaces mais claras.

3. **Para segurança, dados e design, que evento fará você migrar entre incorporado, federado e centralizado?** A recomendação do capítulo é escolher por função e por escala, e a disciplina mais difícil é decidir de antemão que crescimento ou risco fará você revisitar essa escolha. Um modelo que serve para cinquenta engenheiros pode virar um gargalo ou um desastre de consistência com quinhentos, e empresas e órgãos governamentais precisam especialmente nomear os padrões que um pequeno núcleo central sempre manterá. Leve os tempos de fila e as lacunas de consistência atuais de cada função: uma equipe central de segurança com filas de revisão de várias semanas é um sinal para federar, enquanto especialistas incorporados produzindo modelos de dados incompatíveis são um sinal para acrescentar um núcleo central de padrões. Decida o gatilho agora, como um limite de comprimento de fila ou uma constatação de auditoria, para que a mudança seja uma evolução planejada e não uma reação de crise. A resposta determina onde você investe em caminhos pavimentados e campeões versus um eixo central.

4. **Como você saberá se a sua equipe de plataforma realmente reduz a carga cognitiva ou está virando, em silêncio, uma cancela?** Uma plataforma existe para tornar fácil, por autosserviço, a escolha em conformidade e confiável, e a mesma equipe pode derivar para impor ferramentas, revisar manualmente cada solicitação e acrescentar o atrito que deveria remover. Para uma grande organização, essa distinção decide se o investimento na plataforma se paga ou se transforma num gargalo central atrás do qual toda equipe alinhada ao fluxo faz fila. As considerações concorrentes são consistência e controle de um lado, contra autonomia do consumidor e fluxo do outro. Leve evidências que um consumidor reconheceria: quanto tempo uma equipe alinhada ao fluxo leva para obter em autosserviço um novo ambiente ou pipeline sem abrir chamado, a proporção entre ações de autosserviço e ações mediadas por pessoas e a adoção da plataforma medida pelas equipes que a escolhem, não pelas forçadas a usá-la. Em contextos corporativos e governamentais, insista em que a plataforma gere evidências de auditoria e conformidade automaticamente, e não por meio de portões manuais, porque uma plataforma que cumpre regras de segregação de funções inserindo uma pessoa revisora recriou o gargalo que foi financiada para dissolver.

5. **Quais das suas relações entre equipes se acomodaram em colaboração permanente, e o que converteria cada uma em uma interface de serviço limpa ou numa fronteira redesenhada?** O modo de colaboração é feito para ser intenso e temporário, e uma parceria que nunca termina costuma ser sinal de que a responsabilidade está no lugar errado ou de que a interface entre duas equipes nunca foi explicitada. Isso importa em escala porque a colaboração permanente e sem nome é onde o custo de coordenação se esconde: ela não aparece em nenhum organograma, mas taxa toda mudança que as duas equipes tocam. As considerações concorrentes são o valor de descoberta de ficar por perto versus o fluxo que se ganha ao transformar a relação num contrato de X como serviço com interface definida, ou ao fundir a responsabilidade numa única equipe. Leve a lista de pares de equipes que colaboraram continuamente por mais de um trimestre, as mudanças que exigiram as duas equipes nos últimos meses e se uma interface estável entre elas poderia ser escrita. Em contextos corporativos e governamentais, onde fronteiras de terceirizados e lotes de contratação podem congelar um repasse por anos, nomeie quais relações você pode converter com uma interface e contribuições inner-source e quais são fixadas por contrato e devem ser gerenciadas como dependências explícitas.

6. **Quando uma equipe habilitadora ajuda outra a construir uma capacidade, como você saberá que ela teve sucesso e pode se afastar, em vez de virar uma dependência permanente?** As equipes habilitadoras existem para orientar uma equipe alinhada ao fluxo a dominar testes, segurança ou observabilidade e depois seguir adiante, e sem uma condição explícita de saída a relação de orientação endurece num serviço permanente que a equipe alinhada ao fluxo nunca absorve de fato. Para uma grande organização, essa é a diferença entre espalhar uma capacidade por dezenas de equipes e criar um novo gargalo compartilhado que escala pior a cada ano. As considerações concorrentes são a profundidade e a consistência que uma equipe especialista oferece contra a autonomia e a responsabilidade de ponta a ponta que você tenta construir nas equipes alinhadas ao fluxo. Leve evidências de transferência de capacidade: se a equipe receptora agora executa o trabalho sem a equipe habilitadora presente, a quantas equipes um grupo habilitador fixo está comprometido ao mesmo tempo e quanto cada engajamento se estendeu além da passagem de bastão prevista. Em contextos corporativos e governamentais, onde uma habilidade escassa pode estar atrás de uma única equipe central ou de um único contrato, decida de antemão como financiar a transferência de capacidade e os campeões, para que a especialização se difunda nas equipes de entrega em vez de ficar trancada atrás de uma fila pela qual toda auditoria e todo lançamento precisam esperar.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e pouca pista, a topologia certa é uma única equipe alinhada ao fluxo que é dona do produto inteiro, e a disciplina é recusar-se a criar silos antes de precisar. Resista a contratar uma pessoa solitária de “DevOps” ou “QA” que vire cancela. Incorpore essas habilidades à única equipe como capacidade embutida. Faça a lei de Conway trabalhar a seu favor mantendo a organização plana, de modo que a arquitetura permaneça tão simples e mutável quanto a equipe.

**Pequena empresa.** Você não terá uma equipe de plataforma ou habilitadora dedicada, então compre a plataforma: use serviços de nuvem gerenciados, pipelines hospedados e ferramentas de segurança prontas para tirar a carga cognitiva indiferenciada das suas uma ou duas equipes. Encare preocupações transversais, como segurança e dados, como coisas que você configura e consome, e não como uma função que você constrói. Reserve qualquer responsabilidade sob medida para o único subsistema complicado que realmente diferencia você, e deixe que os fornecedores carreguem o resto.

**Grande empresa.** Em escala, o problema é o custo de coordenação entre muitas equipes, então faça da topologia um desenho explícito e governado: uma taxonomia compartilhada dos quatro tipos de equipe, modos de interação nomeados, uma plataforma de caminho pavimentado e inner-source para aliviar as filas entre equipes. Acompanhe o atraso causado por dependências e a carga cognitiva das equipes como métricas de portfólio, e conduza as reorganizações como evoluções deliberadas com uma barra alta, e não como um reflexo anual. Um núcleo central enxuto mantém os padrões que precisam ser consistentes, enquanto as equipes alinhadas ao fluxo mantêm a autonomia sobre a entrega.

**Governo.** Regras de contratação, fronteiras de terceirizados e segregações obrigatórias de funções fragmentam a responsabilidade, então desenhe a topologia para cumprir essas restrições por meio de ferramentas e interfaces claras, e não de repasses humanos. Favoreça modelos federados com um pequeno núcleo de padrões e uma plataforma que gere evidências de auditoria e conformidade automaticamente, de modo que a segregação de funções seja imposta por pipelines e não por filas de revisão. Documente abertamente as fronteiras das equipes, os modos de interação e o modelo operacional, para que a estrutura seja transparente a auditores, órgãos de controle e ao público que a financia.

## Exemplos

**Startup.** Uma startup de dez pessoas tem uma única equipe alinhada ao fluxo que é dona do produto inteiro de ponta a ponta, o que é exatamente certo para a sua escala: sem repasses, sem imposto de coordenação, todos compartilhando o mesmo contexto. O problema começa quando contratam uma “pessoa de DevOps” dedicada e uma “pessoa de QA” separada e recriam acidentalmente silos funcionais, de modo que cada lançamento agora espera por dois indivíduos. Eles corrigem o rumo tratando essas contratações como uma capacidade embutida de plataforma e testes dentro da única equipe, e não como portões pelos quais o trabalho precisa passar. Nesse tamanho, a topologia mais barata é a que mantém todos num único fluxo.

**Grande empresa.** O checkout de um grande varejista era lento para mudar porque a lógica de frontend, backend e atendimento estava dividida entre três equipes organizadas por função, forçando toda mudança a passar por três backlogs. Aplicando a manobra inversa de Conway, eles se reorganizaram em equipes alinhadas ao fluxo em torno das jornadas do cliente (“navegar”, “carrinho e checkout”, “pós-compra”), cada uma dona de sua fatia de ponta a ponta, apoiadas por uma equipe de plataforma que oferecia implantação e observabilidade como serviço. Mudanças no checkout que antes levavam um trimestre passaram a ser lançadas em dias, porque a coordenação que antes atravessava equipes agora acontecia dentro de uma só.

**Governo.** Uma agência tributária governamental mantinha uma equipe central de segurança que revisava cada lançamento, criando uma fila de várias semanas que atrasava correções críticas. Eles passaram a um modelo federado: uma pequena função central de segurança definia os padrões e fornecia um “caminho pavimentado” de pipelines pré-aprovados e escaneados automaticamente, enquanto campeões de segurança incorporados em tempo parcial em cada equipe de entrega cuidavam das decisões do dia a dia. A plataforma gerava evidências de conformidade automaticamente. Os requisitos obrigatórios de segregação de funções continuaram atendidos, mas por meio de ferramentas e interfaces claras, e não de um gargalo humano, o que reduziu drasticamente o tempo de espera dos lançamentos e melhorou a prontidão para auditoria.

## Justificativa de negócio: motivações, ROI e TCO

Você paga pelo mau desenho de equipes em custo de coordenação, e esse custo cresce mais que linearmente com o número de equipes que precisam se sincronizar para uma mudança típica. Cada repasse é uma fila com tempo de espera, uma transferência de contexto que perde informação e uma nova chance de má comunicação. Quando uma mudança rotineira exige que três equipes alinhem seus roteiros, o custo real não é a soma do trabalho delas, mas o custo muito maior de agendamento, espera e retrabalho. Redesenhe as fronteiras para que a maioria das mudanças caiba dentro da responsabilidade de uma única equipe, e esse custo simplesmente desaparece.

O custo de adoção é real. Reorganizações são perturbadoras, e construir plataformas e práticas de inner-source exige investimento inicial antes que o retorno chegue. Mas o custo de não adotar se acumula. Organizações que deixam a estrutura se acumular ao acaso empilham cadeias de repasses, equipes-gargalo compartilhadas com filas de um trimestre e arquiteturas fossilizadas pelo organograma. Para defender o caso junto à liderança, meça o atraso causado por dependências: quantas iniciativas ativas estão bloqueadas esperando outra equipe, e por quanto tempo. Os investimentos em plataforma e topologia geralmente se pagam ao transformar essa espera em fluxo, o que aparece como prazos de entrega mais curtos e maior vazão sem aumentar o quadro de pessoal.

## Antipadrões e armadilhas

- Ignorar a lei de Conway: projetar uma arquitetura que a estrutura da organização não consegue entregar.
- Silos funcionais: equipes separadas de frontend, backend, QA e operações que precisam se coordenar para qualquer mudança.
- Gargalo de serviços compartilhados: uma equipe central atrás da qual todo projeto precisa fazer fila.
- Plataforma como cancela: uma equipe de plataforma que impõe em vez de servir, acrescentando atrito em vez de removê-lo.
- Sobrecarga cognitiva: equipes responsáveis por sistemas extensos e sem relação entre si que elas não conseguem dominar.
- “Colaboração” permanente: duas equipes perpetuamente emaranhadas, sinalizando uma fronteira mal posicionada.
- Vício em reorganizações: reembaralhar constantemente, destruindo a estabilidade de que as equipes precisam para se entrosar.

## Modelo de maturidade

- **Nível 1, Iniciar.** As equipes se formam por acaso, por contagem de pessoas ou por hierarquia legada. Ninguém nomeia tipos de equipe nem modos de interação. Silos funcionais e gargalos de serviços compartilhados estão por toda parte, e as dependências ficam ocultas até bloquearem um lançamento.
- **Nível 2, Desenvolver.** Existem algumas equipes alinhadas ao fluxo e surge um primeiro esforço de plataforma ou inner-source, mas o padrão é aplicado de forma desigual: algumas equipes são donas de sua fatia de ponta a ponta enquanto outras ainda fazem fila atrás de funções centrais, e a carga cognitiva é discutida de forma anedótica em vez de gerenciada.
- **Nível 3, Padronizar.** Os quatro tipos de equipe e os três modos de interação são documentados e usados deliberadamente na organização. Plataformas e inner-source aliviam as dependências entre equipes. Um modelo operacional para segurança, dados e design é escolhido e escrito, e as novas equipes são formadas segundo esses padrões, e não por improviso.
- **Nível 4, Gerenciar.** A topologia é medida e controlada em relação a linhas de base: as equipes acompanham a carga cognitiva, o atraso causado por dependências (iniciativas bloqueadas esperando outra equipe, e por quanto tempo), as proporções de autosserviço e a adoção da plataforma, a duração dos modos de interação e métricas de fluxo de entrega, como prazo de entrega e frequência de mudanças. Limites disparam ações, por exemplo um comprimento de fila que força uma função a federar ou uma colaboração permanente que sinaliza uma fronteira mal posicionada, de modo que as decisões se apoiam em evidências e não em opiniões.
- **Nível 5, Orquestrar.** O desenho das equipes é continuamente melhorado e integrado ao planejamento de arquitetura, produto e risco. A organização remodela as fronteiras conforme o sistema e o negócio evoluem, encerra os engajamentos habilitadores quando a capacidade foi transferida e reequilibra o investimento em plataforma conforme a carga cognitiva muda, mantendo o fluxo rápido como uma propriedade adaptativa e permanente, e não como uma reorganização isolada.

## Ideias para discussão

- Para uma mudança típica, quantas equipes precisam se coordenar, e por quê?
- Quais das nossas equipes carregam carga cognitiva demais, e o que uma plataforma poderia assumir?
- Onde estamos lutando contra a lei de Conway em vez de redesenhar as fronteiras?
- Nossas equipes de plataforma estão servindo as equipes alinhadas ao fluxo ou funcionando como cancela?
- Segurança, dados e design devem ser centralizados, federados ou incorporados para nós agora?
- Quais colaborações “temporárias” se tornaram, em silêncio, dependências permanentes?

## Principais conclusões

- A estrutura da organização determina a arquitetura e a velocidade de entrega. Desenhe-a deliberadamente.
- Use os quatro tipos de equipe, com as alinhadas ao fluxo como padrão e as demais como apoio.
- Aplique a manobra inversa de Conway para tornar a arquitetura desejada o caminho fácil.
- Gerencie a carga cognitiva. Delimite cada equipe a um domínio que ela consiga dominar.
- Limite e nomeie os modos de interação entre equipes. Trate dependências persistentes como defeitos de fronteira.
- Escolha modelos centralizado, federado ou incorporado para as funções transversais conforme a escala, e use InnerSource para aliviar as filas.

## Referências e leitura complementar

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
