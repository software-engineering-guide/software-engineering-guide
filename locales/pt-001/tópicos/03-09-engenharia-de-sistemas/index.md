# 3.9 Engenharia de sistemas

## Visão geral e motivação

A [engenharia de sistemas](https://en.wikipedia.org/wiki/Systems_engineering) é a disciplina de projetar um sistema complexo inteiro, de ponta a ponta, para que todas as suas partes trabalhem juntas e atendam a uma necessidade real. As partes incluem muito mais que software. Um sistema moderno costuma combinar software, hardware, pessoas, dados e processos, e precisa operar num mundo real bagunçado. A engenharia de sistemas mantém tudo isso alinhado ao longo de toda a vida do sistema.

Isso é diferente da arquitetura de software. A arquitetura de software (capítulo 3.1) decide como os componentes de software são estruturados e como conversam entre si. A engenharia de sistemas fica um nível acima. Ela pergunta o que o sistema como um todo precisa fazer, como o software, o hardware e os operadores humanos dividem o trabalho e como você provará que a coisa pronta funciona. Seu lar profissional é o [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), o International Council on Systems Engineering, e sua norma âncora é a [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), que define os processos para a vida de um sistema.

Isso importa para grandes programas corporativos e governamentais porque seus sistemas são grandes, de longa vida e críticos para a segurança ou para a missão. Uma plataforma de defesa, um sistema de tráfego aéreo ou uma constelação de satélites mistura hardware sob medida, peças de terceiros, software embarcado e em nuvem e operadores humanos, e nenhuma equipe sozinha consegue guardar o todo na cabeça. Muitas vezes também se constrói um [sistema de sistemas](https://en.wikipedia.org/wiki/System_of_systems): muitos sistemas independentes, cada um útil por si, que precisam cooperar para entregar uma capacidade maior.

Este capítulo se conecta aos requisitos de software (capítulo 2.8), aos fundamentos de arquitetura (capítulo 3.1), aos modelos e métodos de software (capítulo 2.12), à interoperabilidade e aos padrões abertos (capítulo 3.8) e ao gerenciamento de projetos (capítulo 10.6).

## Princípios fundamentais

- **Projete o todo, não as partes.** Um sistema tem sucesso ou fracassa como um todo, então otimizar um subsistema isoladamente pode piorar o conjunto.
- **Siga o ciclo de vida.** Um sistema tem uma vida do primeiro conceito até a aposentadoria final. Planeje toda ela, não apenas a construção.
- **Rastreie cada requisito.** Toda necessidade deve mapear para um requisito, um elemento de design e um teste. Se você não consegue rastrear, não consegue provar.
- **Gerencie as interfaces de propósito.** A maioria das falhas acontece nas fronteiras entre as partes, então as interfaces merecem responsabilidade e controle explícitos.
- **Verifique e valide separadamente.** Construir a coisa direito (verificação) e construir a coisa certa (validação) são perguntas diferentes, e você precisa das duas respostas.
- **Espere comportamento emergente.** Combinar partes cria comportamento que nenhuma parte sozinha mostra. Parte dele é o objetivo, e parte é uma péssima surpresa.
- **Co-projete hardware e software.** Quando ambos são sob medida, as decisões de um restringem o outro, então planeje-os juntos.

## Recomendações

### Gerencie o ciclo de vida completo do sistema

Trate o sistema como tendo uma vida inteira e planeje cada etapa. Um ciclo de vida comum corre assim: **conceito** (entender a necessidade e explorar opções), **requisitos** (declarar com precisão o que o sistema deve fazer), **design** (decidir a arquitetura e as partes), **integração** (juntar as partes), **verificação e validação** (provar que funciona e que é o sistema certo), **operação** (executá-lo e mantê-lo) e **aposentadoria** (desativá-lo com segurança, incluindo dados e descarte). A ISO/IEC/IEEE 15288 dá um arcabouço de processos para isso. As etapas não precisam ser uma cascata rígida: você pode iterar, prototipar e entregar incrementos. O ponto é que você trate conscientemente todas as etapas, inclusive as posteriores e caras que os planos iniciais costumam ignorar.

### Capture as necessidades das partes interessadas e aloque requisitos com rastreabilidade

Comece pelas pessoas que se importam com o sistema: usuários, operadores, donos, reguladores e o público. Reúna as **necessidades** delas em linguagem simples e depois transforme essas necessidades em **requisitos** projetados, específicos e testáveis (veja o capítulo 2.8). Em seguida vem a **alocação de requisitos**: atribuir cada requisito de nível de sistema a um subsistema específico, para que você saiba qual parte é responsável por atendê-lo. Mantenha uma matriz de **[rastreabilidade](https://en.wikipedia.org/wiki/Requirements_traceability)**, um registro vivo que liga cada necessidade ao seu requisito, ao elemento de design que a satisfaz e ao teste que a verifica. Ela permite provar a qualquer momento que toda necessidade está coberta e que toda parte existe por um motivo.

### Gerencie as interfaces explicitamente

As interfaces são onde as partes se encontram, e onde os sistemas mais costumam quebrar. Uma interface pode ser um conector físico, um protocolo de rede, um formato de dados ou um procedimento humano. Para cada uma, escreva um **Documento de Controle de Interface** (ICD, Interface Control Document): uma especificação acordada de exatamente como duas partes se conectam e trocam informações. Dê a cada interface um responsável claro em cada lado. Apoiar-se em especificações compartilhadas e publicadas em vez de conectores pontuais torna a integração muito mais fácil, que é o argumento de interoperabilidade do capítulo 3.8. Congele as interfaces cedo quando puder, porque uma mudança tardia reverbera em toda parte que as toca.

### Integre e depois verifique e valide

A **integração de sistemas** combina os subsistemas no todo funcional, em geral por etapas e não de uma vez, para que você ache os problemas enquanto ainda são pequenos. Depois da integração vem a **[verificação e validação](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), duas checagens distintas. A **verificação** pergunta: construímos o sistema direito, isto é, ele atende aos requisitos especificados? Vocês verificam por inspeção, análise, demonstração e teste. A **validação** pergunta: construímos o sistema certo, isto é, ele atende às necessidades reais das partes interessadas em uso real? Um sistema pode passar na verificação (atende à especificação) e ainda assim falhar na validação (a especificação estava errada). Planeje ambas cedo e escreva requisitos e interfaces de modo que possam ser verificados, para começar.

### Adote a engenharia de sistemas baseada em modelos

A engenharia de sistemas tradicional produzia montanhas de documentos que se desalinhavam. A **[engenharia de sistemas baseada em modelos](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) substitui essa pilha por um único modelo formal e compartilhado do sistema, do qual são geradas visões e relatórios. A linguagem de modelagem comum é a **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modeling Language), uma linguagem gráfica para descrever os requisitos, a estrutura, o comportamento e as restrições de um sistema. Como tudo vive num único modelo conectado, uma mudança atualiza em todo lugar, e a rastreabilidade vira uma consulta e não uma caçada manual. A MBSE se conecta às ideias de modelagem do capítulo 2.12. Adote-a gradualmente, começando pelas partes de maior risco, onde um modelo compartilhado compensa mais depressa.

### Aplique o pensamento sistêmico ao comportamento emergente

Pratique o [pensamento sistêmico](https://en.wikipedia.org/wiki/Systems_thinking): raciocine sobre o todo e sobre as relações entre as partes, não apenas sobre as partes uma a uma. É assim que se antecipa o **[comportamento emergente](https://en.wikipedia.org/wiki/Emergence)**: propriedades que aparecem só quando as partes se combinam e que nenhuma parte sozinha mostra. A boa emergência costuma ser o propósito do sistema (um bando de drones cobre uma área que nenhum drone sozinho cobriria). A má emergência é a falha-surpresa (dois subsistemas seguros interagem e criam um estado perigoso). Não se consegue testar a emergência para fora de um sistema que nunca foi modelado, então use simulação e análise estruturada de perigos para achá-la antes da operação.

### Co-projete hardware e software

Quando um sistema inclui hardware sob medida, projete o hardware e o software juntos, uma prática chamada **[co-design de hardware/software](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. As decisões se amarram umas às outras: o hardware define limites de tempo, memória e energia dentro dos quais o software precisa viver, e as necessidades do software moldam o que o hardware precisa fornecer. Os longos prazos de entrega do hardware também conduzem o cronograma. Decida cedo quais funções moram no hardware e quais no software e revisite essa divisão à medida que as restrições surgem.

## Compromissos: prós e contras

| Abordagem | Prós | Contras / custo |
|---|---|---|
| Rigor completo de engenharia de sistemas | Menos surpresas tardias, forte rastreabilidade, mais seguro e auditável | Alto custo inicial, partida mais lenta, processo pesado |
| Abordagem leve / só de software | Rápida, barata, flexível para escopo pequeno | Desmorona em sistemas grandes e multidisciplinares, perde interfaces e emergência |
| Baseada em modelos (MBSE) | Fonte única de verdade, rastreabilidade fácil, visões consistentes | Custo de ferramentas e treinamento, mudança de cultura, curva de aprendizado |
| Engenharia de sistemas baseada em documentos | Familiar, baixo custo de ferramentas, fácil de compartilhar | Os documentos se desalinham, a rastreabilidade é manual e propensa a erros |

A troca central é rigor versus velocidade. A engenharia de sistemas completa antecipa esforço em conceito, requisitos e trabalho de interfaces. Esse esforço se paga muitas vezes em sistemas grandes, de longa vida e críticos para a segurança, onde um defeito achado em operação pode custar milhares de vezes mais que o mesmo defeito achado nos requisitos. Num produto pequeno, de curta vida e só de software, esse rigor é exagero. Combine o peso do seu processo com o tamanho, a vida útil e o risco do sistema. O modo de falha é aplicar hábitos de projeto descartável a um sistema que rodará por trinta anos e carregará risco no mundo real.

## Perguntas para discutir com sua equipe

1. **Onde vocês construíram exatamente o que a especificação exigia e mesmo assim entregaram o sistema errado, e o que teria pegado isso?** A verificação (construímos certo) e a validação (construímos a coisa certa) respondem a perguntas diferentes, e um sistema pode passar em todo teste de verificação e ainda falhar na validação porque a própria especificação estava errada. Em grandes programas as duas são colapsadas em “testes”, então ninguém valida contra a necessidade real do operador até tarde, quando uma correção custa milhares de vezes mais que uma mudança de requisitos. Levem um exemplo passado em que o sistema entregue atendia aos seus requisitos mas errava a necessidade real e perguntem que atividade de validação (uma simulação com operadores reais, um protótipo antecipado em campo) o teria revelado mais cedo. Planejem as duas checagens desde o início e escrevam requisitos e interfaces de modo que possam ser verificados. A distinção decide onde vocês gastam o escasso esforço de revisão.

2. **Como vocês caçam o mau comportamento emergente antes de o sistema estar em operação, e não depois?** Combinar subsistemas seguros pode criar estados perigosos que nenhuma parte sozinha exibe, e não se consegue testar a emergência para fora de um sistema que nunca foi modelado. Num programa crítico para a segurança ou para a missão, a interação surpresa é a que fere alguém ou faz a missão fracassar, então ela precisa ser achada antes da operação real. Levem a sua abordagem para modelar o todo (simulação, análise estruturada de perigos, um modelo SysML que capture interações) e perguntem quais comportamentos entre subsistemas vocês de fato exploraram versus presumiram. A boa emergência costuma ser o propósito do sistema e vale ser projetada. A má emergência é a falha contra a qual vocês precisam projetar. Se a sua única estratégia de integração é ligar as partes e ver o que acontece, vocês estão planejando descobrir a emergência em produção.

3. **Quando as decisões de hardware de longo prazo de entrega precisam ser congeladas, e como esse prazo conduz o seu cronograma de software?** Quando um sistema inclui hardware sob medida, os dois precisam ser co-projetados: o chip define tetos de tempo, memória e energia dentro dos quais o software vive, e os prazos de entrega do hardware muitas vezes dominam todo o cronograma. As equipes que tratam o software como separável otimizam localmente e depois colidem com as restrições do hardware na integração, perdendo meses. Levem os prazos de entrega do hardware e a data até a qual a divisão de funções entre hardware e software precisa ser decidida e revisitem essa divisão à medida que as restrições surgem, em vez de congelá-la às cegas. Quanto mais cedo vocês decidem quais funções moram no silício e quais no software, menos reversões caras enfrentam. As interfaces entre os dois merecem um Documento de Controle de Interface e um responsável em cada lado, porque uma mudança tardia ali reverbera em tudo que as toca.

4. **Vocês conseguem rastrear uma única necessidade de parte interessada até o requisito, o elemento de design e o teste que a prova, e quem mantém esse elo vivo?** A rastreabilidade é o que permite mostrar a qualquer momento que toda necessidade está coberta e que toda parte existe por um motivo, e ainda assim num grande programa a matriz apodrece no instante em que ninguém é dono dela. A atração concorrente é real: os engenheiros sentem a rastreabilidade como burocracia, e uma matriz mantida à mão se desatualiza mais depressa do que o design muda. Levem um fio genuíno de um programa atual e tentem percorrê-lo de ponta a ponta na sala, de uma necessidade nomeada de parte interessada, ao requisito alocado, ao subsistema e ao elemento de design que a satisfaz, ao teste de verificação, e anotem onde a cadeia se rompe. Decidam quem é dono da matriz e se ela deveria viver num modelo onde a rastreabilidade é uma consulta e não uma caçada manual. Para programas corporativos e governamentais, a matriz também é o artefato de auditoria que reguladores e autoridades de aquisição exigem, então uma cadeia rompida faz mais que atrasar a engenharia: pode travar a certificação ou o pagamento.

5. **Uma abordagem baseada em modelos vale o custo de ferramentas e de cultura para vocês, ou viraria um caro enfeite de prateleira?** A engenharia de sistemas baseada em documentos é familiar e barata de equipar, mas seus documentos se desalinham e sua rastreabilidade é manual e propensa a erros. A MBSE substitui a pilha por um único modelo conectado, ao preço de ferramentas, treinamento e uma genuína mudança de cultura. Qualquer extremo é caro: pular a MBSE num grande programa multidisciplinar e vocês pagam em surpresas de integração, adotá-la sem a disciplina de manter o modelo atual e ela apodrece em enfeite de prateleira pior que nenhum modelo. Levem uma leitura honesta da maturidade das suas ferramentas, de quem na equipe de fato consegue criar e manter um modelo SysML e de qual subsistema de alto risco poderia pilotar a abordagem onde um modelo compartilhado compensa mais depressa. Decidam de forma gradual e não impondo a organização inteira de uma vez. Para um grande programa corporativo ou governamental com muitos fornecedores, pesem se um modelo compartilhado é a única maneira realista de manter requisitos, interfaces e testes consistentes entre contratados que de outro modo trocam documentos obsoletos.

6. **O plano de ciclo de vida de vocês financia a sério a operação e a aposentadoria, ou para em silêncio no lançamento?** As etapas que dominam o custo total de um sistema de longa vida, operá-lo por décadas e desativá-lo com segurança, são as que os planos iniciais rotineiramente ignoram, porque a pressão é sempre para entregar. A consideração concorrente é que dinheiro e atenção são mais escassos exatamente quando essas etapas posteriores parecem mais distantes, então a operação, a manutenção, a migração de dados e o descarte são adiados até virarem uma correria cara e arriscada. Levem o plano atual de ciclo de vida e verifiquem se ele nomeia responsáveis, orçamentos e critérios de saída para a operação e a aposentadoria, ou se trata o lançamento como linha de chegada. Perguntem o que acontece com os dados e o hardware no fim da vida e quem paga pelos anos de manutenção no meio. Para sistemas corporativos e governamentais que precisam funcionar por vinte ou trinta anos e depois se aposentar sob escrutínio público, uma desativação não planejada pode violar obrigações regulatórias, ambientais ou de retenção de registros, então a aposentadoria pertence ao plano e ao orçamento desde a primeira revisão de conceito.

## Perspectiva por setor

**Startup.** Uma equipe minúscula não consegue conduzir um programa formal de engenharia de sistemas e não deveria tentar, mas ainda pode tratar firmware, aplicativo e nuvem como um sistema e não como três projetos separados. Escreva um documento curto de interface que fixe como as partes conversam, mantenha uma tabela simples ligando cada necessidade do cliente à parte que a satisfaz e pule o processo pesado. Seu recurso mais escasso é a atenção da engenharia, então gaste esforço de rastreabilidade só onde uma suposição errada numa fronteira quebraria o produto em silêncio no campo.

**Pequena empresa.** Sem engenheiro de sistemas dedicado e com orçamento apertado, apoie-se em padrões publicados e em subsistemas comprados em vez de uma integração sob medida que você mesmo tem de projetar e verificar. Favoreça fornecedores que expõem especificações claras de interface para que as partes se encaixem sem um conector personalizado que você precisaria manter para sempre. Enquadre a escolha entre construir e comprar em torno de quais interfaces você consegue realisticamente controlar e verificar ao longo da vida do produto e compre o resto.

**Grande empresa.** Em escala o problema é a consistência entre muitas equipes e fornecedores: um processo de ciclo de vida compartilhado alinhado à ISO/IEC/IEEE 15288, um Documento de Controle de Interface e um responsável nomeado para cada fronteira de fornecedor e rastreabilidade de ponta a ponta para que a mudança de um componente não dispare uma correria em todo o programa. Invistam em MBSE onde um modelo compartilhado mantém requisitos, interfaces e testes alinhados entre contratados. Governem o processo para que a verificação e a validação continuem distintas e todo requisito seja alocado a uma parte responsável.

**Governo.** As regras de contratação, a transparência e a responsabilização pública moldam toda escolha. Especifiquem no contrato o processo de engenharia de sistemas, a rastreabilidade e a evidência de V&V, exijam dos fornecedores a entrega de documentos de controle de interface e de artefatos de ciclo de vida que vocês possam auditar e reservem a validação de segurança e de missão para revisão independente com operadores reais antes de qualquer virada para a operação real. Planejem e financiem explicitamente a operação e a aposentadoria, porque um programa público responde pelo ciclo de vida inteiro, inclusive a desativação segura e a retenção de registros.

## Exemplos

**Startup.** Uma startup de hardware de quatro pessoas que constrói um sensor conectado não pode bancar um programa formal de engenharia de sistemas, mas ainda assim trata o produto como um sistema de firmware, aplicativo móvel e backend em nuvem e não como três projetos separados. Elas escrevem um documento curto de interface que fixa como o dispositivo, o aplicativo e o servidor conversam (formatos de mensagem, unidades, códigos de erro) e mantêm uma tabela simples ligando cada necessidade do cliente à parte que a satisfaz. Quando um chip de sensor mais barato força uma mudança de firmware, essa interface compartilhada mostra de imediato o que o aplicativo e o backend precisam ajustar, de modo que a troca de um componente não quebra o produto em silêncio no campo.

**Grande empresa.** Uma fabricante global de automóveis constrói uma nova plataforma de veículo elétrico: um sistema de software (gerenciamento da bateria, assistência ao motorista, infoentretenimento), hardware (motores, sensores, chips) e fatores humanos, mais muitos fornecedores entregando cada qual subsistemas. A empresa conduz um programa de engenharia de sistemas. As necessidades das partes interessadas alimentam requisitos alocados, toda interface de fornecedor tem um Documento de Controle de Interface e um modelo SysML liga requisitos a design e a testes. Quando um fornecedor de células de bateria muda um componente, o modelo de rastreabilidade mostra exatamente quais requisitos, interfaces e testes são afetados, então a mudança fica contida em vez de disparar uma correria em todo o programa.

**Governo.** Uma autoridade nacional de navegação aérea moderniza seu sistema de gerenciamento de tráfego aéreo, um sistema de sistemas crítico para a segurança que abrange radares, estações de trabalho de controladores, comunicações e software, operado 24 horas por dia. O programa segue a ISO/IEC/IEEE 15288 em todo o ciclo de vida. A verificação prova que cada subsistema atende à sua especificação, e a validação por simulação com controladores reais prova que o sistema integrado sustenta operações seguras antes de qualquer tráfego real depender dele. A V&V rigorosa permite à autoridade fazer a virada por etapas, com retorno possível em cada passo, porque aqui uma falha emergente não testada é um evento de segurança pública.

## Justificativa de negócio: motivações, ROI e TCO

A motivação é que os defeitos ficam exponencialmente mais caros quanto mais tarde são achados. Um erro de requisito pego durante a etapa de requisitos custa quase nada para corrigir. O mesmo erro pego em operação pode custar milhares de vezes mais e, num sistema crítico para a segurança, pode custar vidas, recalls ou uma missão fracassada. A engenharia de sistemas desloca a descoberta de defeitos para as etapas iniciais, baratas.

Para o **retorno do investimento** (ROI, valor ganho em comparação com o custo gasto), o ganho é retrabalho evitado, menos falhas de integração e programas que cumprem cronograma e orçamento em vez de estourar. Estudos da indústria sobre grandes programas encontram repetidamente que um forte esforço de engenharia de sistemas se correlaciona com estouros menores. Para o **custo total de propriedade** (TCO, o custo total de toda a vida de construir, operar e aposentar um sistema), a engenharia de sistemas leva em conta as etapas de operação e aposentadoria que dominam o custo de longo prazo mas que projetos ad hoc ignoram. Projetar desde o início para a manutenibilidade, as interfaces e o descarte reduz o custo das décadas que o sistema passa em serviço. Veja o gerenciamento de projetos (capítulo 10.6).

## Antipadrões e armadilhas

- **Grande design antecipado sem iteração.** Tratar o ciclo de vida como uma cascata rígida de mão única, de modo que você só descobre que os requisitos estavam errados depois de construir tudo.
- **Requisitos sem rastreabilidade.** Uma pilha de requisitos que ninguém liga a design ou a testes, de modo que você não consegue provar a cobertura nem justificar nenhuma parte.
- **Ignorar as interfaces.** Presumir que os subsistemas simplesmente se encaixarão e depois perder meses na integração com desencontros de fronteira que ninguém possuía.
- **Verificação sem validação.** Provar que o sistema atende à sua especificação sem nunca checar se a especificação correspondia às necessidades reais e depois entregar o sistema errado.
- **Tratar o software como separado.** Equipes de software otimizando localmente enquanto ignoram as restrições do hardware, o tempo e os operadores humanos.
- **MBSE como enfeite de prateleira.** Construir um modelo uma vez e deixá-lo apodrecer fora de sincronia até ficar pior que nenhum modelo.
- **Pular o planejamento da aposentadoria.** Nenhum plano de desativação, migração de dados ou descarte, de modo que o fim da vida vira uma correria cara e arriscada.

## Modelo de maturidade

**Nível 1: Iniciar.** A engenharia de sistemas é ad hoc e reativa. Os requisitos vivem em documentos dispersos, as interfaces são descobertas na integração e a verificação é o teste que por acaso for feito. Grandes programas regularmente estouram e surpreendem a equipe tarde.

**Nível 2: Desenvolver.** Existem práticas básicas nos programas principais. Os requisitos são capturados e baselinados, as interfaces-chave têm documentos de controle e há um plano de verificação. A prática é inconsistente entre equipes e depende de indivíduos e não de um método compartilhado.

**Nível 3: Padronizar.** A engenharia de sistemas é uma disciplina documentada, de toda a organização, alinhada à ISO/IEC/IEEE 15288 e imposta entre as equipes. O ciclo de vida completo é planejado, a rastreabilidade é mantida de ponta a ponta, as interfaces são formalmente controladas e a verificação e a validação são distintas e planejadas. A MBSE é usada em programas complexos.

**Nível 4: Gerenciar.** A engenharia de sistemas é medida e controlada com dados. A organização acompanha métricas em relação a linhas de base: a volatilidade dos requisitos e a cobertura de rastreabilidade, os defeitos de interface achados na integração, as taxas de aprovação da verificação e da validação e o vazamento de defeitos por etapa do ciclo de vida (quantos defeitos escapam de cada etapa para serem pegos depois a custo maior). As revisões conduzem os programas por esses números, e os limiares disparam ação corretiva em vez de apagar incêndio depois do fato.

**Nível 5: Orquestrar.** A engenharia de sistemas é continuamente melhorada e integrada em toda a organização. Um modelo MBSE vivo é a fonte única de verdade, a rastreabilidade é automatizada, a simulação prevê o comportamento emergente antes da construção e as métricas de programas passados alimentam o próximo. Hardware e software são co-projetados como rotina, e o processo se adapta à medida que programas, fornecedores e riscos mudam.

## Ideias para discussão

- Onde fica a linha entre a engenharia de sistemas e a arquitetura de software na sua organização, e quem é dono do espaço entre elas?
- No seu maior programa, vocês conseguem rastrear uma única necessidade de parte interessada até o teste que a verifica? Se não, o que seria preciso?
- Qual das suas falhas recentes aconteceu numa interface, e quem era o dono dela?
- A MBSE compensaria para vocês, ou viraria um caro enfeite de prateleira dada a sua cultura e as suas ferramentas?
- O plano de ciclo de vida de vocês trata a sério a operação e a aposentadoria, ou para em silêncio no lançamento?

## Principais conclusões

- A engenharia de sistemas projeta o sistema inteiro (software, hardware, pessoas e processos) de ponta a ponta e é distinta da arquitetura de software.
- Planeje o ciclo de vida completo, do conceito aos requisitos, design, integração, V&V, operação e aposentadoria.
- Rastreie cada necessidade até um requisito, um elemento de design e um teste e aloque cada requisito a uma parte responsável.
- Gerencie as interfaces explicitamente, com responsabilidade clara e documentos de controle, porque as fronteiras são onde os sistemas quebram.
- A verificação (construímos certo) e a validação (construímos a coisa certa) são checagens diferentes, e vocês precisam das duas.
- Use MBSE e SysML para uma fonte de verdade única e conectada e use o pensamento sistêmico para antecipar o comportamento emergente.
- Combine o peso do seu processo com o tamanho, a vida útil e o risco do sistema.

## Referências e leitura complementar

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (systems engineering guidance)
