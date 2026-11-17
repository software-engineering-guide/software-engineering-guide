# 1.7 Padrões de engenharia e exceções

## Visão geral e motivação

Um **padrão de engenharia** é uma regra documentada e acordada sobre como o trabalho é feito. Por exemplo, “todo serviço deve expor um endpoint de verificação de saúde” ou “todas as páginas web públicas devem atender às **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Diretrizes de Acessibilidade para Conteúdo Web) 2.2 nível AA**”. Um padrão não é uma sugestão, nem uma mera convenção. É um compromisso ao qual a organização se submete, idealmente um que você consiga verificar. Este capítulo trata do ciclo de vida completo dos padrões, como uma grande organização os **redige, publica, adota, impõe e evolui** e, com igual importância, como trata os casos que legitimamente ficam fora deles por meio de um **processo de exceções** governado (também chamado de **processo de dispensa**): uma permissão documentada e com prazo para se desviar de um padrão por um motivo declarado.

A motivação é que, em escala, as normas informais deixam de funcionar. Quando cinco engenheiros dividem uma sala, o “jeito como fazemos as coisas aqui” viaja por conversa e osmose. Quando cinco mil engenheiros se espalham por dezenas de equipes, três fusos horários e uma década de rotatividade, esse conhecimento tácito se fragmenta em centenas de hábitos locais incompatíveis. Os padrões são como você escreve suas lições duramente conquistadas uma só vez, para que cada equipe as herde em vez de reaprender cada uma por meio da própria queda de serviço. Eles reduzem a [carga cognitiva](https://en.wikipedia.org/wiki/Cognitive_load), fazem as [revisões de código](https://en.wikipedia.org/wiki/Code_review) tratarem de substância e não de estilo, permitem que as pessoas transitem entre equipes e dão a auditores e reguladores algo concreto para avaliar.

Mas os padrões trazem um modo de falha próprio: a rigidez. Um padrão que não admite exceções vai, mais cedo ou mais tarde, bloquear trabalho legítimo: uma investigação exploratória, uma restrição de fornecedor, um caso genuinamente novo que os autores nunca imaginaram. As equipes então ou param por completo ou, pior, ignoram o padrão em silêncio, o que corrói a credibilidade de *todos* os padrões. O remédio é o velho aforismo “a exceção confirma a regra”. Um processo de exceções visível e fundamentado é o que mantém os padrões ao mesmo tempo críveis e humanos. Este capítulo se apoia na tomada de decisão e governança (capítulo 1.5) e nos registros de decisão (capítulo 1.6) e alimenta diretamente os padrões de codificação e estilo (capítulo 2.1), as listas de verificação (capítulo 12.2) e os modelos (capítulo 12.3).

## Princípios fundamentais

- **Um padrão declara um resultado e dá uma razão.** Regra mais justificativa. Sem o *porquê*, as pessoas não conseguem julgar quando ele realmente se aplica.
- **Se não pode ser verificado, ainda não é um padrão.** Prefira afirmações testáveis a aspirações.
- **Os padrões são documentos vivos.** São versionados, têm responsável, data e revisão, não são esculpidos na pedra e abandonados.
- **Automatize a imposição onde puder. Reserve a revisão humana para o julgamento.** As máquinas verificam o mecânico. As pessoas verificam o significativo.
- **Desvios são esperados, não vergonhosos, mas devem ser visíveis.** Uma dispensa honesta vence a não conformidade silenciosa sempre.
- **Dê prazo a toda exceção.** Uma exceção permanente é um defeito no padrão. Traga-a à tona e corrija o padrão.
- **Palavras e exemplos em vez de jargão e mandatos.** As pessoas seguem padrões que entendem e dos quais podem copiar.

## Recomendações

### Escreva padrões claros, testáveis e justificados

Um bom padrão é um documento curto e autocontido com uma forma previsível, para que os leitores saibam onde olhar. Adote um **modelo de padrão** (capítulo 12.3) e use-o em toda parte. As seções essenciais incluem:

- **Título e identificador:** um nome estável e um número de referência para citação.
- **Status:** rascunho, ativo, substituído ou aposentado, com uma data.
- **A regra:** declarada como um resultado, com clareza e sem ambiguidade (“deve”, “convém” e “pode”, usados deliberadamente, conforme as convenções da **RFC 2119** para palavras-chave de requisitos).
- **Justificativa:** *por que* esta regra existe, o custo ou risco que ela evita.
- **Exemplos:** um exemplo em conformidade e outro fora dela. O concreto vence o abstrato.
- **Como é verificado:** o teste automatizado, a regra de linter ou a etapa de revisão que o verifica.
- **Responsável e data de revisão:** quem o mantém e quando será revisitado.

Os campos de justificativa e de “como é verificado” são o que separa um padrão de verdade de um desejo. Se você não consegue dizer por que uma regra existe, questione se ela deveria existir. Se não consegue dizer como a conformidade é verificada, a regra será aplicada de forma inconsistente e ressentida.

### Associe cada padrão a uma lista de verificação de boas práticas

Os padrões definem o destino. Uma **lista de verificação de boas práticas**, uma lista curta e ordenada de passos concretos ou itens a confirmar, ajuda as pessoas a chegar lá e permite que se autoverifiquem antes da revisão. Os manuais de engenharia do setor público usam muito esse padrão. O **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** e o **Digital Health and Care Wales (DHCW)** publicam padrões de engenharia com listas de verificação práticas, e o **[Government Digital Service](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS) do Reino Unido** associa seu Service Standard e seu Technology Code of Practice à orientação prática do Service Manual. A lista de verificação é o padrão tornado utilizável: “Você acrescentou uma auditoria de acessibilidade? Testou com um leitor de tela? Cobriu a navegação somente por teclado?” Veja o capítulo 12.2 para o padrão de lista de verificação completo.

### Publique os padrões onde as pessoas já trabalham e mantenha-os localizáveis

Armazene os padrões no **[controle de versões](https://en.wikipedia.org/wiki/Version_control)** (um repositório de código-fonte) como Markdown, renderizados num site interno pesquisável, para que ganhem histórico, revisão por pull requests e comparação de graça, o mesmo argumento dos registros de decisão (capítulo 1.6). Um catálogo, um modelo, uma caixa de busca. Fazer aparecer importa tanto quanto armazenar. Ligue o padrão relevante a partir do modelo de pull request, da mensagem de erro do linter e do esqueleto do serviço, para que a regra certa apareça no momento do trabalho e não numa pasta que ninguém visita.

### Imponha primeiro por automação, depois por revisão humana

Há duas maneiras de impor um padrão, e as organizações maduras usam ambas deliberadamente:

- **Imposição automatizada:** [linters](https://en.wikipedia.org/wiki/Lint_(software)), formatadores, [análise estática](https://en.wikipedia.org/wiki/Static_program_analysis), política como código (por exemplo, **Open Policy Agent (OPA)**), portões de **[integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI)** e **funções de aptidão de arquitetura** (testes automatizados que afirmam que uma propriedade de projeto continua valendo). A automação é consistente, incansável, imediata e indiscutível, o que a torna ideal para a maioria mecânica dos padrões (formatação, nomenclatura, regras de dependência, metadados obrigatórios).
- **Revisão humana:** revisão de código, conselhos de revisão de arquitetura e revisão de segurança, reservadas para o que as máquinas não conseguem julgar: se uma abstração é sólida, se um compromisso é sensato, se a *intenção* de um padrão é cumprida mesmo quando a sua letra é desajeitada.

A regra prática: **automatize o verificável e gaste a escassa atenção humana no julgamento.** Todo padrão que você consegue mover da revisão para a CI libera os revisores para fazer o raciocínio que só eles podem fazer.

### Governe os desvios com um processo documentado de exceções/dispensas

Nenhum padrão serve a todos os casos, então projete a válvula de escape de propósito. Um bom processo de exceções especifica:

- **Quem pode conceder uma dispensa:** uma autoridade nomeada e responsável, proporcional ao risco (um tech lead para um desvio de estilo de baixo risco, um conselho de arquitetura ou de segurança para a dispensa de um controle de segurança). Isso se liga diretamente ao modelo de governança do capítulo 1.5.
- **O que deve ser registrado:** o padrão do qual se desvia, o motivo específico, o escopo, os controles compensatórios ou as mitigações e o risco aceito. Capture isso como um registro de decisão (capítulo 1.6) para que a justificativa seja preservada.
- **Uma validade obrigatória:** toda dispensa tem **prazo** com uma data de término explícita. Esta é a regra mais importante: ela impede que uma exceção temporária se torne, em silêncio, política permanente.
- **Revisão periódica:** um responsável revisa as dispensas abertas com regularidade e ou as renova com nova justificativa, ou as encerra quando o trabalho passa a estar em conformidade ou, se a mesma exceção continua se repetindo, trata isso como evidência de que o *próprio padrão* está errado e o revisa.

Este último ponto é o coração de “a exceção confirma a regra”. Um fluxo constante de dispensas contra um padrão não é uma falha de disciplina. É dado. Ele diz que o padrão está mal calibrado, e a correção é evoluir o padrão, não continuar concedendo exceções.

### Trate os padrões como documentos vivos com responsabilidade clara

Dê a cada padrão um **responsável** (um papel, não só uma pessoa) encarregado de mantê-lo atual e uma **cadência de revisão** (pelo menos anual). Ofereça um caminho leve para que qualquer pessoa proponha uma mudança por um pull request ou por uma **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (pedido de comentários)**, uma proposta escrita circulada para feedback antes da adoção. Versione os padrões, torne-os obsoletos explicitamente e anuncie as mudanças. Um catálogo de padrões que nunca é revisado apodrece em folclore que as pessoas citam seletivamente e em que pouco confiam.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| **Muitos padrões detalhados** | Consistência, integração fácil, pronto para auditoria | Rigidez. Custo de manutenção. Pode ultrapassar a prática |
| **Poucos padrões de alto nível** | Flexível. Baixa manutenção | Inconsistência. Mais rediscussão por equipe |
| **Imposição automatizada** | Consistente, imediata, incansável, escalável | Custo inicial. Falsos positivos. Cega à intenção |
| **Imposição por revisão humana** | Julga intenção e nuance | Lenta, inconsistente, gargalo em escala |
| **Rígido, sem exceções** | Mensagem simples. Nada para manipular | Bloqueia trabalho legítimo. Gera não conformidade silenciosa |
| **Processo de exceções governado** | Mantém os padrões críveis e humanos | Exige governança, registros e acompanhamento |

A tensão central é **consistência versus flexibilidade**. Um padrão existe para remover a variação. Um processo de exceções existe para admitir a variação que é genuinamente justificada. Incline-se demais para a rigidez e as pessoas contornarão seus padrões. Incline-se demais para a frouxidão e os padrões não significarão nada. O processo de exceções é a válvula de pressão que permite manter uma linha firme *e* ser honesto sobre a realidade.

## Perguntas para discutir com sua equipe

1. **Qual é o número certo de padrões para a sua escala, e os seus estão derivando para a rigidez ou para a inconsistência?** O próprio catálogo é um compromisso: muitos padrões detalhados compram consistência, integração fácil e prontidão para auditoria ao custo de rigidez e custo de manutenção, enquanto poucos padrões de alto nível ficam flexíveis, mas deixam cada equipe rediscutir as mesmas questões. Para uma grande empresa ou órgão governamental, o tamanho certo depende de quanta variação você consegue de fato tolerar versus quanto os seus auditores e a sua integração precisam deixar fixado. Leve evidências: quantos padrões ativos você tem, quantos foram revisados no último ano e com que frequência as equipes rediscutem coisas que um padrão poderia ter resolvido. Um catálogo que ultrapassa a prática vira folclore, e um muito escasso empurra o custo para cada equipe. Decida deliberadamente o que merece um padrão e pode aqueles que já não justificam o seu custo.

2. **Onde a letra de um padrão passa automaticamente enquanto a sua intenção é violada em silêncio, e como você vai detectar isso?** A automação é consistente, incansável e cega à intenção, o que significa que um linter ou uma verificação de política pode ficar verde enquanto o objetivo real (uma abstração sólida, um compromisso sensato, uma página genuinamente acessível) é perdido. A regra prática é automatizar o verificável e gastar a escassa revisão humana em julgamento, e a parte difícil é concordar quais padrões têm uma intenção que nenhum portão de CI consegue afirmar. Leve exemplos: padrões que as pessoas cumprem à letra enquanto derrotam o propósito, como um endpoint de verificação de saúde que informa saudável enquanto o serviço está quebrado, ou código que passa no formatador mas obscurece o significado. Em contextos regulamentados, a intenção importa mais para os controles de segurança física e de segurança da informação, onde uma caixinha verde pode esconder risco real. Decida quais padrões mantêm um revisor humano especificamente para julgar a intenção e redija esses padrões em torno do resultado, para que máquina e revisor mirem o mesmo alvo.

3. **Quem é dono do ciclo de retroalimentação da dispensa para o padrão, e em que ponto uma exceção recorrente obriga você a mudar a regra?** Um fluxo constante de dispensas contra um padrão é dado, não indisciplina, e o sinal é desperdiçado a menos que alguém seja responsável por lê-lo e agir. A consideração concorrente é que revisar um padrão dá trabalho de verdade, de modo que continua mais fácil carimbar dispensas do que corrigir a regra mal calibrada por baixo delas. Leve os números: quais padrões geram mais exceções, se as dispensas de fato têm prazo e são revisadas com regularidade e quantas se tornaram permanentes em silêncio. Para padrões críticos para a segurança física e a segurança da informação em empresas e governo, uma dispensa deve registrar controles compensatórios, uma mitigação, o risco aceito e uma validade rígida, ou um desvio temporário vira política não documentada que emerge na próxima auditoria. Atribua um responsável para revisar as dispensas abertas, defina um limiar a partir do qual exceções repetidas disparam uma revisão do padrão e trate uma exceção permanente como um defeito do padrão a ser corrigido.

4. **O padrão certo aparece no momento do trabalho, ou vive numa pasta que ninguém abre?** Um padrão que ninguém encontra é imposto pela sorte, e em escala a maior parte da não conformidade não é desafio, é ignorância: uma pessoa engenheira nunca soube que a regra existia ou não conseguiu localizá-la quando importava. A consideração concorrente é o esforço, já que fazer um padrão aparecer no modelo de pull request, na mensagem de erro do linter e no esqueleto do serviço custa um trabalho real de integração que um único site central não custa. Leve evidências sobre a capacidade de localização: como as pessoas engenheiras de fato encontram os padrões hoje, se uma pessoa recém-contratada consegue localizar em menos de um minuto a regra de acessibilidade ou de segurança que governa a sua tarefa e com que frequência os revisores citam um padrão que o autor simplesmente não tinha visto. Para uma grande empresa ou órgão governamental, os auditores perguntam cada vez mais não só se um padrão existe, mas se ele foi comunicado e estava acessível no momento da decisão, então trate o fazer aparecer como parte do padrão, não como uma reflexão tardia, e meça se as pessoas conseguem chegar à regra quando precisam.

5. **Quem é o responsável por cada padrão ativo, quando foi revisado pela última vez e como você identificaria os que apodreceram em silêncio e viraram folclore?** Os padrões decaem em silêncio: uma regra escrita três anos atrás para um framework que você já não usa ainda está no catálogo, citada seletivamente e pouco confiável, arrastando a credibilidade dos padrões que ainda estão certos. Para uma organização grande, o custo da responsabilidade é a própria cadência de revisão, que parece custo operacional até que uma queda de serviço ou uma auditoria exponha um padrão que não corresponde mais à realidade. Leve os números à discussão: quantos padrões têm um responsável nomeado (um papel, não só um indivíduo que saiu), quantos foram revisados no último ano, quantos estão formalmente obsoletos versus apenas desatualizados e quais são mais e menos citados. Em contextos corporativos e governamentais, um auditor espera que cada padrão seja versionado, datado e demonstravelmente atual, então combine uma cadência mínima de revisão, atribua a cada padrão um responsável e aposente os que já não justificam o seu custo antes que minem a confiança nos demais.

6. **A autoridade para conceder uma dispensa é de fato proporcional ao risco do padrão que está sendo dispensado?** Um desvio de estilo e um desvio de controle de segurança não são a mesma decisão, mas muitas organizações ou encaminham ambos a um conselho pesado (o que paralisa o trabalho legítimo) ou deixam ambos passar por um único tech lead (o que deixa um risco sério ser aceito por alguém sem o mandato para aceitá-lo). A tensão é velocidade contra responsabilização: atrito de aprovação demais gera não conformidade silenciosa, enquanto pouco demais significa que desvios consequentes passam numa conversa de chat. Leve um mapa dos seus padrões para as respectivas autoridades de aprovação, mais uma amostra de dispensas concedidas recentemente, e verifique se alguém dispensou um controle crítico para a segurança física ou a segurança da informação sem o conselho, o controle compensatório, a mitigação e a aceitação de risco registrada correspondentes. Para empresas e governo, esta é uma questão de segregação de funções que os reguladores examinam diretamente, então ligue cada classe de padrão a uma autoridade nomeada e proporcional ao seu risco e garanta que quem aceita um risco seja genuinamente responsável pelas consequências.

## Perspectiva por setor

**Startup.** Mantenha o catálogo minúsculo: escreva apenas o punhado de regras cuja ausência realmente o prejudicaria, como uma configuração de formatador, um requisito de verificação de saúde e páginas navegáveis por teclado, e imponha cada uma com um linter ou verificação de CI e não com uma reunião de revisão. Pule por completo o conselho de dispensas. Um TODO datado no código e uma nota de uma linha no pull request são uma exceção com prazo perfeitamente boa nessa escala. Seu recurso mais escasso é a atenção de engenharia, então resista a redigir padrões para problemas que você ainda não tem.

**Pequena empresa.** Sem um responsável dedicado por padrões e com orçamento apertado, compre seus padrões em vez de construí-los: adote bases publicadas como o Service Standard do GDS do Reino Unido, a orientação de segurança da OWASP ou as regras de lint recomendadas pelo seu framework, e apoie-se nas verificações já embutidas nas suas ferramentas e na CI hospedada. Mantenha uma única página curta de regras locais para as poucas coisas genuinamente específicas suas. Quem lidera a engenharia concede e registra as exceções no tíquete, com data de validade, para que até um processo leve continue honesto.

**Grande empresa.** O trabalho é governança entre muitas equipes: um catálogo, um modelo, justificativa e exemplos para cada padrão e política como código que quebra o pipeline para a maioria mecânica. Conduza um processo de dispensas cuja autoridade de aprovação seja proporcional ao risco, dê prazo a toda exceção, revise as dispensas abertas com regularidade e minere as dispensas recorrentes como o sinal de que um padrão precisa mudar. Meça a parcela de padrões impostos automaticamente e o volume e a idade das dispensas abertas, e relate ambos à função de governança para que os padrões continuem um sistema gerenciado e não um cemitério.

**Governo.** Publique seus padrões de engenharia abertamente, na tradição do DHCW e do GDS, e associe cada um a uma lista de verificação que as equipes preenchem antes de uma avaliação de serviço, para que a conformidade seja visível ao público e aos órgãos de supervisão. Faça de um responsável sênior nomeado a autoridade para as dispensas consequentes e exija que toda exceção registre o critério específico, o controle compensatório ou a mitigação provisória, um plano de correção e uma validade rígida. As regras de contratação e transparência significam que seus padrões e seus desvios se tornam parte do registro público, então trate a auditabilidade e a rastreabilidade como requisitos de projeto desde o início.

## Exemplos

**Startup.** Uma startup de sete pessoas mantém exatamente três padrões escritos (uma configuração compartilhada de formatador, um requisito de endpoint de verificação de saúde e “todas as páginas públicas devem ser navegáveis por teclado”), cada um imposto por um linter ou verificação de CI e não por uma reunião de revisão. Quando uma engenheira precisa lançar um protótipo descartável que quebra a regra de verificação de saúde, não há conselho de dispensas: ela deixa um TODO datado no código e uma nota de uma linha no pull request dizendo por quê e quando vai corrigir. Essa é uma exceção com prazo na escala de uma startup, honesta e visível, sem custo de processo. As três verificações se pagam por manter a revisão de código sobre substância e não sobre estilo.

**Grande empresa.** Um banco global mantém um manual interno de engenharia com cerca de quarenta padrões ativos, cada um num único modelo com justificativa, exemplos e uma lista de verificação de boas práticas vinculada. Cerca de 70% são impostos automaticamente: formatação, política de dependências, metadados obrigatórios de serviço e controles de segurança codificados como política como código que quebra o pipeline de CI. Uma equipe de pagamentos precisa lançar num banco de dados que ainda não suporta um recurso de criptografia obrigatório. Em vez de bloquear o lançamento, ela registra uma dispensa nomeando o padrão, o controle compensatório ([criptografia](https://en.wikipedia.org/wiki/Encryption) na camada da aplicação) e uma validade de 90 dias. O conselho de segurança a concede e a registra. Noventa dias depois, a revisão constata que a plataforma agora suporta o recurso nativamente, e a dispensa é encerrada. O padrão se manteve, o trabalho foi entregue e o desvio é totalmente rastreável para a próxima auditoria.

**Governo.** Uma agência nacional de saúde, inspirada na abordagem do DHCW e do GDS, publica seus padrões de engenharia abertamente, cada um associado a uma lista de verificação que as equipes preenchem antes de uma avaliação de serviço. A acessibilidade segundo as WCAG 2.2 AA é um padrão rígido, imposto por uma auditoria automatizada na CI mais uma avaliação manual. Um sistema clínico legado não consegue atender de imediato a um critério de acessibilidade sem arriscar funcionalidades críticas para a segurança do paciente. A equipe solicita uma exceção com prazo. Um responsável sênior nomeado a concede e registra o critério específico, a mitigação provisória (uma linha telefônica de acesso assistido), o plano de correção e uma validade de seis meses, criando exatamente a evidência rastreável e revisável que os órgãos de supervisão exigem (capítulos 4.6, 10.4).

## Justificativa de negócio: motivações, ROI e TCO

Um padrão custa o tempo de escrevê-lo, de automatizar sua verificação e de mantê-lo. O retorno é pago toda vez que a verificação roda e toda vez que uma pessoa engenheira não precisa parar e debater uma questão resolvida. Os padrões convertem o custo de decisão recorrente e distribuído num custo único de redação, a mesma economia dos registros de decisão (capítulo 1.6), amplificada porque um padrão governa milhares de instâncias futuras, não uma escolha passada.

No **custo total de propriedade (TCO)**, o custo do ciclo de vida inteiro de construir, operar e manter um sistema, os padrões reduzem as maiores linhas de despesa: integração (as pessoas novas herdam consistência em vez de fazer engenharia reversa dela), manutenção (código uniforme é mais barato de mudar) e garantia (as auditorias são mais baratas quando a conformidade é verificável por máquina e os desvios já estão documentados). O processo de exceções protege esse ROI da sua principal ameaça: padrões decaindo em folclore ignorado. Um processo de dispensas crível mantém os padrões confiáveis, e padrões confiáveis são os que as pessoas de fato seguem. O custo de pular tudo isso é invisível em qualquer painel. Aparece como integração lenta, qualidade inconsistente e constatações de auditoria, e se acumula a cada nova equipe e a cada saída.

## Antipadrões e armadilhas

- **Regras sem justificativa:** um padrão que ninguém entende é um padrão que ninguém consegue aplicar corretamente nem contestar com honestidade.
- **Padrões aspiracionais e não verificáveis:** “o código deve ser fácil de manter” é um valor, não um padrão. Não pode ser imposto nem contestado.
- **Sem processo de exceções:** força uma falsa escolha entre bloquear trabalho legítimo e tolerar a não conformidade silenciosa.
- **Exceções permanentes:** dispensas sem validade que viram em silêncio a política real e não documentada.
- **Dispensas sem registro:** desvios concedidos num corredor ou numa conversa de chat, invisíveis para a próxima auditoria e para a próxima pessoa engenheira.
- **Ignorar o sinal:** conceder repetidamente a mesma exceção em vez de lê-la como prova de que o padrão precisa mudar.
- **Imposição por insistência:** depender de revisores para pegar o que um linter deveria pegar, desperdiçando julgamento no mecânico.
- **Cemitério de padrões:** um catálogo escrito uma vez, sem responsável, nunca revisado, citado seletivamente e em que poucos confiam.
- **Elitismo de jargão:** padrões escritos para seus autores e não para seus leitores, sem exemplos para copiar.

## Modelo de maturidade

- **Nível 1 (Iniciar):** Os padrões são conhecimento tribal nas cabeças das pessoas engenheiras seniores, aplicados de forma reativa. A imposição é insistência ad hoc na revisão de código. Os desvios são invisíveis. O “jeito como fazemos” varia por equipe e por quem revisou a mudança.
- **Nível 2 (Desenvolver):** Alguns padrões estão escritos, em formatos inconsistentes e locais dispersos, e a adoção varia muito de equipe para equipe. A imposição é em sua maioria manual. As exceções acontecem de modo informal, sem registros nem datas de validade.
- **Nível 3 (Padronizar):** Um catálogo único, um modelo, justificativa e exemplos para cada padrão e listas de verificação de boas práticas, aplicados de forma consistente entre as equipes. Imposição automatizada para a maioria mecânica. Um processo de exceções documentado, com aprovadores nomeados, justificativa registrada e dispensas com prazo.
- **Nível 4 (Gerenciar):** O sistema de padrões é medido em relação a linhas de base. Você acompanha a parcela de padrões impostos automaticamente versus por revisão humana, o volume de dispensas por padrão, o tempo até o encerramento e quantas dispensas expiraram ainda abertas, e relata isso à função de governança. A autoridade de aprovação é proporcional ao risco e auditada. A cadência de revisão e a validade são impostas com base em evidências e não na boa vontade. Um padrão cuja taxa de dispensas cruza um limiar combinado é sinalizado para revisão.
- **Nível 5 (Orquestrar):** Os padrões aparecem no momento do trabalho e são impostos por política como código e funções de aptidão. As dispensas são mineradas como sinal, de modo que exceções recorrentes levam continuamente os padrões a evoluir, e o catálogo é reequilibrado conforme a prática muda. Padrões, listas de verificação e dispensas são um sistema vivo e adaptativo integrado à integração, à entrega e à auditoria.

## Ideias para discussão

1. Quais dos seus padrões você consegue declarar com uma regra testável *e* uma justificativa clara, e quais são na verdade apenas aspirações?
2. Que parcela dos seus padrões é imposta automaticamente versus por um revisor que percebe? O que seria preciso para mover mais dez para a CI?
3. Onde acontecem os desvios hoje, e você sequer saberia? Eles são registrados e têm prazo, ou são silenciosos?
4. Quem pode conceder uma dispensa contra o seu padrão mais crítico para segurança física ou segurança da informação, e essa autoridade é proporcional ao risco?
5. Olhe para o seu padrão mais dispensado. É um problema de disciplina, ou o padrão está simplesmente errado?
6. Quando cada padrão ativo foi revisado pela última vez, e quem é o responsável por ele? Quais viraram folclore em silêncio?

## Principais conclusões

- Um padrão de engenharia é uma **regra declarada como um resultado, com justificativa, exemplos e uma forma de verificação**: se não pode ser verificado, ainda não é um padrão.
- Associe cada padrão a uma **lista de verificação de boas práticas** para que as pessoas possam se autoverificar, seguindo o padrão dos manuais do setor público (NHS Wales / DHCW, GDS do Reino Unido).
- Armazene os padrões no **controle de versões**, mantenha-os **vivos** com responsáveis nomeados e datas de revisão e faça-os aparecer no momento do trabalho.
- **Automatize o verificável** com linters, política como código e funções de aptidão. Reserve a **revisão humana** para o julgamento.
- Governe os desvios com um **processo documentado de exceções/dispensas, com prazo**: aprovador nomeado, justificativa registrada, validade obrigatória, revisão periódica.
- Uma exceção recorrente é um **sinal para corrigir o padrão**, não só para continuar concedendo dispensas: “a exceção confirma a regra”. Veja os capítulos 1.5 (governança), 1.6 (registros de decisão), 2.1 (padrões de codificação), 12.2 (listas de verificação) e 12.3 (modelos).

## Referências e leitura complementar

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice*, and *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* and engineering guidance.
- Digital Health and Care Wales (DHCW) / NHS Wales, published engineering standards and good-practice checklists.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures* (fitness functions as automated governance).
- Torin Sandall et al., *Open Policy Agent* documentation (policy-as-code).
- GitLab, *The GitLab Handbook*: a public example of living, version-controlled organizational standards.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): standards, readability, and automated enforcement at scale.
- Atul Gawande, *The Checklist Manifesto*: the case for checklists as professional practice.
