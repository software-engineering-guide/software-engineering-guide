# 11.2 O pipeline de entrega

## Visão geral e motivação

O pipeline de entrega é o fluxo de trabalho que transforma uma ideia validada em software em execução nas mãos dos usuários (de forma confiável, repetível e mensurável) e depois devolve os dados de resultado à descoberta (capítulo 11.1). É o caminho industrializado de um commit de código a uma mudança em produção e a um efeito medido sobre os usuários e o negócio. Onde a descoberta responde *o quê e por quê*, a entrega responde *como entregamos com segurança, com que rapidez e se de fato funcionou*.

Este capítulo é deliberadamente integrador. A mecânica vive em detalhe em outros lugares: estratégia de testes (capítulo 2.4), automação de testes e de processos (capítulo 8.5), [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) e [entrega contínua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) e estratégias de implantação (capítulo 8.1), infraestrutura como código (capítulo 8.2), confiabilidade e SLOs (objetivos de nível de serviço, capítulo 9.1) e experimentação (capítulo 7.4). Aqui os reunimos num único pipeline de ponta a ponta e, de modo crucial, anexamos as **métricas de resultado** que dizem se a máquina inteira produz valor e não meramente produz lançamentos.

Para grandes equipes, o pipeline de entrega é o investimento de maior alavancagem em eficácia de engenharia. Uma década de pesquisa, mais notavelmente o programa DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) resumido em *Accelerate*, mostra que as equipes com pipelines de entrega rápidos, automatizados e de baixo risco superam as demais em vazão *e* estabilidade *e* resultados organizacionais. A velha crença de que velocidade e segurança se trocam uma pela outra é empiricamente falsa. Nas empresas, um pipeline forte é o que permite a centenas de engenheiros integrar sem colapsar em caos de merge e teatro manual de lançamento. No governo, ele substitui os lançamentos “big bang” trimestrais, de alta cerimônia e tudo ou nada (historicamente uma das principais causas de programas fracassados) por mudanças pequenas, reversíveis e auditáveis que satisfazem as obrigações de controle de mudanças *por meio* da automação e não apesar dela.

## Princípios fundamentais

- **Automatizem tudo o que é repetível.** Passos manuais são lentos, propensos a erro e não auditáveis.
- **Lotes pequenos, lançamentos frequentes.** Mudanças pequenas são mais fáceis de revisar, testar, entregar e reverter.
- **Embutam a qualidade.** Testes e portões rápidos e automatizados pegam defeitos antes da produção, não depois.
- **Separem a implantação do lançamento.** Entreguem o código às escuras; ativem as funcionalidades com flags quando estiverem prontas.
- **Tornem tudo reversível.** Rollback rápido e exposição progressiva transformam a implantação de uma aposta num experimento.
- **O pipeline é a fonte da verdade.** Se não está no controle de versão e no pipeline, não aconteceu.
- **Meçam resultados, não só saídas.** A contagem de implantações é uma saída; uma métrica movida é um resultado.

## Recomendações

### Automatize a suíte de testes e use-a como portão

A automação de testes é a base que torna segura a entrega rápida. Implementem um portfólio de testes equilibrado e majoritariamente automatizado (capítulo 2.4): muitos testes unitários rápidos, menos testes de integração e de contrato, um pequeno número de testes de ponta a ponta, mais verificações automatizadas de segurança (SAST/DAST/SCA: análise estática, dinâmica e de composição de software), acessibilidade e desempenho. Executem-nos como **portões de qualidade** no pipeline para que nenhuma mudança chegue à produção sem passar. Mantenham a suíte rápida e confiável: uma suíte lenta ou instável é contornada, o que anula o seu propósito (capítulo 8.5). Mirem em que o pipeline dê ao desenvolvedor um sinal claro de passou/falhou em minutos após um commit.

### Pratiquem a integração contínua e a entrega contínua

**Integração contínua (CI):** cada desenvolvedor integra pequenas mudanças à linha principal com frequência (idealmente diária), e cada integração dispara um build e uma execução de testes automatizados. Isso é mais bem sustentado pelo desenvolvimento baseado em trunk (capítulo 2.6), que mantém os branches de vida curta e a integração contínua. **Entrega contínua (CD):** toda mudança que passa pelo pipeline está *sempre num estado liberável* e pode ser implantada sob demanda. A **implantação contínua** vai um passo além: toda mudança que passa é implantada em produção automaticamente. Escolham o nível de automação adequado ao seu perfil de risco; os ambientes regulados podem parar na entrega contínua com um passo controlado de promoção (capítulo 8.1), mas ainda devem automatizar tudo até esse portão.

### Implante com segurança usando estratégias progressivas

Desacoplem a **implantação** (código rodando em produção) do **lançamento** (usuários vivenciando a mudança) e exponham as mudanças gradualmente:

- As **[feature flags](https://en.wikipedia.org/wiki/Feature_toggle)** permitem implantar código às escuras e lançar para segmentos sob demanda, e reverter instantaneamente alternando a flag.
- Os **lançamentos canário** encaminham uma pequena porcentagem do tráfego para a nova versão, observando as métricas de saúde antes de ampliar.
- As **implantações azul-verde** mantêm dois ambientes e trocam o tráfego de forma atômica, com rollback instantâneo.
- As **implantações graduais (rolling)** substituem as instâncias de forma incremental.
- A **entrega progressiva** combina flags, canários e análise automatizada para promover ou reverter com base em sinais ao vivo.

Combinem toda estratégia com rollback automatizado disparado por violações de SLO ou queima do orçamento de erros (a taxa em que as falhas consomem o orçamento de não confiabilidade permitido; capítulo 9.1). Vejam o capítulo 8.1 para a mecânica.

### Instrumentem métricas de resultado: meçam o pipeline e o impacto

Um pipeline de entrega que entrega rápido mas entrega a coisa errada é desperdício veloz. Meçam em três níveis:

1. **Fluxo de entrega, as quatro métricas DORA:**
   - *Frequência de implantação:* com que frequência vocês lançam em produção.
   - *[Prazo de entrega](https://en.wikipedia.org/wiki/Lead_time) das mudanças:* do commit à produção.
   - *Taxa de falha das mudanças:* porcentagem de lançamentos que causam uma degradação.
   - *Tempo de recuperação de implantação com falha:* com que rapidez vocês restauram o serviço (antes MTTR, tempo médio de recuperação).
   Os desempenhos de elite implantam sob demanda, com prazos de entrega abaixo de uma hora, baixas taxas de falha e recuperação em minutos. Acrescentem **métricas de fluxo** do pensamento de fluxo de valor (tempo de ciclo, [trabalho em andamento](https://en.wikipedia.org/wiki/Work_in_process), eficiência do fluxo) para ver onde o trabalho espera.

2. **Confiabilidade e qualidade, SLIs e SLOs** (indicadores e objetivos de nível de serviço; capítulo 9.1): o serviço está cumprindo suas metas de confiabilidade e seus compromissos de atributos de qualidade (capítulo 11.1) após cada mudança?

3. **Resultados de negócio e de usuário** (capítulos 7.3–7.4): a mudança moveu os resultados-chave e os KPIs que a descoberta definiu? É aqui que o lançamento encontra o experimento: entreguem atrás de uma flag, meçam contra um controle e fiquem só com o que vence.

### Fechem o ciclo de volta à descoberta

O ato final do pipeline de entrega não é a implantação; é a **evidência**. As métricas de resultado (a ativação subiu, o tempo de checkout caiu, os chamados de suporte diminuíram) fluem de volta ao pipeline de descoberta (capítulo 11.1) como base para a próxima rodada de apostas. Quando a descoberta e a entrega são unidas por esse ciclo de feedback, a organização vira um sistema que aprende: as hipóteses são entregues, medidas e ou ampliadas ou revertidas, continuamente.

### Tornem a entrega auditável e governada

Em contextos corporativos e governamentais, tratem o próprio pipeline como um controle de conformidade. Como toda mudança flui pelo controle de versão e por um pipeline automatizado, vocês ganham uma trilha de auditoria imutável “de graça”: quem mudou o quê, quais testes e aprovações a condicionaram e quando foi implantada. Codifiquem a separação de funções, as revisões obrigatórias e as verificações de política como **política como código** (regras de governança expressas numa forma imposta por máquina e versionada; capítulo 8.2) para que o controle de mudanças seja imposto automaticamente e evidenciado continuamente (capítulos 4.6 e 10.2), em vez de reconstruído à mão antes de uma auditoria.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| **Implantação contínua (automática em produção)** | Feedback mais rápido. Menores lotes. Menos trabalho repetitivo manual | Exige testes, monitoramento e rollback maduros. Difícil com portões regulados |
| **Entrega contínua com promoção manual** | Ponto de controle humano/de conformidade. Amigável à auditoria | Mais lenta. Risco de acumular mudanças no portão |
| **Feature flags** | Separação implantação/lançamento. Rollback instantâneo. Segmentação | Dívida de flags e complexidade combinatória se não forem podadas |
| **Canário / entrega progressiva** | Limita o raio de impacto. Promoção guiada por dados | Exige forte observabilidade e gestão de tráfego |
| **Azul-verde** | Troca e rollback instantâneos | Dobra o custo do ambiente. Migrações de estado/dados são delicadas |
| **Processo de lançamento manual pesado** | Parece controlado. Familiar aos auditores | Lento, propenso a erro, irreprodutível, mal auditado na prática |

A crença histórica de compromisso, *andem mais rápido e quebrarão mais*, é a principal a aposentar. A evidência mostra que as práticas que aumentam a velocidade (automação, lotes pequenos, testes rápidos, reversibilidade) são as *mesmas* práticas que aumentam a estabilidade. Os compromissos reais são sobre **investimento e granularidade de controle**, não sobre velocidade versus segurança.

## Perguntas para discutir com sua equipe

1. **Qual é o seu perfil de risco real, e ele justifica parar na entrega contínua em vez de ir à implantação contínua?** Escolher o nível de automação é uma decisão real, não um padrão. A implantação contínua dá o feedback mais rápido e os menores lotes, mas exige testes maduros, forte observabilidade e rollback instantâneo, então um contexto regulado pode racionalmente parar num portão de promoção controlado. Levem evidências: a taxa de falha das mudanças, o tempo de recuperação e a confiabilidade da suíte de testes, pois elas dizem se o automático em produção é seguro hoje. Para a empresa e o governo, automatizem tudo até o portão e façam do próprio portão política como código, para que o passo humano acrescente controle sem acrescentar trabalho repetitivo manual. Se vocês ainda não confiam que o pipeline pegue uma mudança ruim, invistam em portões e observabilidade antes de virar a chave.

2. **O seu pipeline consegue produzir a evidência de auditoria que um regulador pediria, sem ninguém reconstruí-la à mão?** Tratem o próprio pipeline como um controle de conformidade. Toda mudança deve carregar uma trilha imutável de quem mudou o quê, quais testes e aprovações a condicionaram e quando foi implantada, gerada automaticamente. Na empresa e no governo, codifiquem a separação de funções e as revisões obrigatórias como política como código para que o controle de mudanças seja imposto e evidenciado continuamente e não montado em pânico antes de uma auditoria. O sinal a trazer: escolham uma mudança recente em produção e tentem produzir sua trilha completa de aprovação e testes em cinco minutos. Se não conseguem, vocês pagam por uma preparação manual de auditoria e carregam um risco que a automação removeria.

3. **Quando um lançamento começa a se degradar em produção, o que dispara um rollback, e ele é automático?** A reversibilidade é o que torna racional e não temerária a velocidade, então o gatilho de rollback merece um projeto explícito. Decidam se uma violação de SLO ou a queima do orçamento de erros reverte automaticamente, ou se um humano precisa notar, decidir e agir enquanto os usuários sofrem. Levem os seus últimos incidentes e meçam a diferença entre “a métrica começou a se degradar” e “a mudança foi revertida”; essa diferença é o seu raio de impacto real. Para grandes equipes que entregam muitas vezes por dia, o rollback manual não escala, e flags mais análise de canário permitem promover ou reverter com base em sinais ao vivo. Se a sua resposta é “alguém é acionado no sobreaviso e se vira”, vocês tratam cada implantação como uma aposta irreversível.

4. **Quando vocês entregam uma funcionalidade, medem se ela de fato moveu a métrica que devia mover, ou contam a implantação e seguem em frente?** Um pipeline que entrega rápido mas nunca confere o impacto é desperdício veloz, e a diferença entre saída e resultado é por onde a maior parte do investimento em entrega vaza em silêncio. Para uma grande organização, centenas de lançamentos por semana tornam tentador tratar a frequência de implantação como placar, mas a frequência mede movimento, não valor; a atração contrária é que medir resultado custa instrumentação, um grupo de controle e a disciplina de deixar desligada uma funcionalidade perdedora. Levem as últimas funcionalidades entregues e, para cada uma, a métrica-alvo que a descoberta definiu, o antes e depois medido e o que vocês fizeram quando ela não se moveu. Em portfólios corporativos e governamentais, nomeiem quem revisa os resultados numa cadência fixa e quem tem autoridade para aposentar uma funcionalidade que foi entregue mas nunca se pagou, porque uma mudança que ninguém é responsável por medir é uma que ninguém jamais desligará. O teste honesto é se vocês conseguem apontar uma funcionalidade que reverteram *porque* a evidência disse que perdeu.

5. **Quanto tempo o seu pipeline leva para dar ao desenvolvedor um sinal de passou/falhou, e eles confiam nos testes o bastante para não contorná-los?** A rapidez do feedback e a confiança na suíte são o que faz os portões de qualidade de fato barrarem em vez de serem contornados, e ambas se erodem em silêncio conforme a base de código cresce. Para uma grande equipe, uma suíte que leva quarenta minutos ou falha de forma instável uma execução em dez treina centenas de engenheiros a integrar no vermelho, desativar verificações ou rerrodar até ficar verde, o que remove em silêncio a segurança que justificava ir rápido em primeiro lugar; as considerações contrárias são cobertura e realismo dos testes versus rapidez e estabilidade do feedback, e forçar qualquer um dos dois demais prejudica o outro. Levem a duração atual do pipeline, a taxa de reexecuções por instabilidade e qualquer evidência de portões pulados ou marcados como não bloqueantes. Em contextos corporativos e governamentais, em que esses portões também carregam SAST, DAST e verificações de política que satisfazem a conformidade, um portão contornado é tanto um risco de qualidade quanto uma lacuna de auditoria, então meçam se o portão é genuinamente obrigatório ou meramente consultivo. Se os desenvolvedores não conseguem articular por que confiam num build verde, o portão é decoração.

6. **Quem é responsável por manter o caminho de entrega consistente entre as equipes e por podar a dívida de feature flags, ou cada equipe reinventa o seu próprio pipeline?** Conforme a organização cresce, a entrega ou converge para um caminho pavimentado compartilhado ou se fragmenta em dezenas de pipelines sob medida com portões incompatíveis, trilhas de auditoria desiguais e flags que sobrevivem ao seu propósito. A tensão é real: um caminho pavimentado central dá consistência, governança e economia de escala, mas um mandato que ignora as restrições genuínas de uma equipe gera pipelines-sombra e ressentimento, então o caminho pavimentado precisa ser bom o bastante para que as equipes o adotem de bom grado. Levem um inventário de quantos pipelines distintos existem hoje, como a criação e a remoção de flags são governadas e quanto o prazo de entrega e a qualidade de auditoria variam entre as suas melhores e piores equipes. Em contextos corporativos e governamentais, acrescentem o ângulo da conformidade: pipelines inconsistentes significam que a separação de funções e a evidência de controle de mudanças são provadas de modo diferente (ou de modo nenhum) em cada equipe, e um único caminho pavimentado auditado com política como código transforma isso de uma aposta por equipe numa garantia organizacional. Se ninguém é responsável por remover flags obsoletas, a dívida combinatória acabará tornando o sistema intestável.

## Perspectiva por setor

**Startup.** A velocidade é sobrevivência, então comprem o pipeline em vez de construí-lo: liguem o desenvolvimento baseado em trunk a um executor de CI hospedado, condicionem cada integração a testes unitários rápidos e uma varredura de segurança e implantem direto em produção atrás de um serviço hospedado de feature flags. Pulem a equipe de plataforma e as ferramentas sob medida; o seu recurso mais escasso é a atenção de engenharia, e um pipeline que um único generalista consiga manter vence um elaborado que ninguém tem tempo de consertar. Acompanhem as quatro métricas DORA num painel simples desde o primeiro dia para aprender o seu fluxo cedo e poder mostrar aos investidores que vocês entregam diariamente sem quebrar as coisas.

**Pequena empresa.** Sem engenheiro de lançamento dedicado e com orçamento apertado, tratem a entrega como algo que vocês montam a partir de serviços gerenciados e não como um sistema que vocês dotam de pessoal: CI/CD gerenciado, uma ferramenta de flags hospedada e uma plataforma de nuvem que cuida do lançamento e do rollback por vocês. Resistam a construir infraestrutura de pipeline personalizada que vocês não têm como manter e mantenham o caminho simples o bastante para que quem esteja de sobreaviso o entenda sob pressão. Prefiram ferramentas que ofereçam entrega progressiva e rollback com um clique de fábrica, porque são as capacidades que transformam uma assustadora implantação de sexta-feira numa rotineira.

**Grande empresa.** O problema central é a consistência entre muitas equipes: um pipeline de caminho pavimentado com suporte e portões automatizados de teste, segurança e política como código que as equipes adotam em vez de reinventar. Padronizem a interface para que as métricas DORA e de SLO sejam comparáveis em toda a organização, orcem explicitamente a capacidade de plataforma que mantém o caminho pavimentado e gerenciem as feature flags e as regressões de prazo de entrega como ativos governados e não como folclore por equipe. A governança e a auditoria vêm de carona automaticamente quando toda mudança flui pelo mesmo caminho versionado e condicionado por portões.

**Governo.** As regras de contratação, a transparência e a prestação de contas públicas moldam o pipeline, então favoreçam a entrega contínua que para num portão de promoção automatizado que impõe a separação de funções e as aprovações obrigatórias como política como código. Façam do próprio pipeline o controle de conformidade: toda mudança carrega uma trilha de auditoria imutável que satisfaz as obrigações de controle de mudanças e de autorização para operar sem reconstrução manual. Substituam os lançamentos “big bang” de alta cerimônia por mudanças pequenas, reversíveis e desacopladas para poder pilotar um fluxo voltado ao público numa região, medir as taxas de erro e de conclusão e reverter em minutos se ele se degradar.

## Exemplos

**Startup.** Uma equipe de três engenheiros que entrega uma ferramenta de análise B2B começa implantando à mão nas tardes de sexta, o que significa um lançamento assustador por semana e um fim de semana de apreensão. Numa tarde, ligam o desenvolvimento baseado em trunk a um pipeline do GitHub Actions: testes unitários rápidos, um linter e uma varredura de segurança condicionam cada integração, e um build aprovado é implantado direto em produção atrás de flags do LaunchDarkly. A frequência de implantação salta de semanal para várias vezes por dia e, como cada nova funcionalidade é entregue às escuras e ativada primeiro para um cliente amistoso, uma exportação de CSV quebrada é pega e desligada em minutos em vez de virar um incidente de segunda-feira. Eles acompanham as quatro métricas DORA num painel simples para poder mostrar aos investidores que a equipe entrega diariamente sem quebrar as coisas.

**Grande empresa.** Uma seguradora global consolida 40 equipes num pipeline de caminho pavimentado compartilhado (uma cadeia de ferramentas padrão com suporte e pré-integrada que as equipes adotam; capítulo 8.4): desenvolvimento baseado em trunk, portões automatizados de teste e segurança e implantação canário com rollback automatizado em violação de SLO. A frequência de implantação sobe de mensal para muitas vezes por dia; o prazo de entrega cai de seis semanas para menos de um dia; a taxa de falha das mudanças cai porque os lotes são pequenos e os portões são automatizados. Crucialmente, as funcionalidades de produto agora são entregues atrás de flags e medidas contra controles, de modo que a seguradora pode ligar cada lançamento ao seu efeito na taxa de conclusão de cotações, conectando o pipeline de entrega diretamente aos resultados-chave do lado da descoberta do capítulo 11.1.

**Governo.** Uma agência pública substitui os lançamentos “big bang” trimestrais (cada um um fim de semana de passos manuais e fonte frequente de quedas) por um pipeline de entrega contínua que para num portão de promoção automatizado que impõe a separação de funções e as aprovações obrigatórias como política como código. Toda mudança carrega uma trilha de auditoria imutável que satisfaz as obrigações da agência de controle de mudanças e de ATO (autorização para operar) (capítulo 4.6). Os lançamentos ficam pequenos, frequentes e reversíveis; o tempo de recuperação cai de dias para minutos; e, como a implantação é desacoplada do lançamento por flags, a agência pode pilotar um novo fluxo de benefícios numa região antes da implantação nacional, medindo conclusão e taxas de erro antes de se comprometer.

## Justificativa de negócio: motivações, ROI e TCO

O retorno do investimento em pipeline de entrega está entre os mais bem evidenciados do software. Prazo de entrega menor e maior frequência de implantação significam que as ideias chegam aos usuários (e começam a devolver valor, ou a ser corrigidas) mais cedo. Taxa de falha das mudanças menor e recuperação mais rápida significam menos tempo fora do ar, menos apagar incêndios e menos dano reputacional e regulatório. A pesquisa DORA liga essas capacidades a desempenho comercial e organizacional superior, não meramente a conforto de engenharia. O efeito composto importa: uma equipe que entrega e aprende diariamente itera de 20 a 30 vezes mais que uma que entrega mensalmente, e essa taxa de aprendizado é decisiva ao longo da vida de um produto.

No **[custo total de propriedade](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, a automação desloca o custo do trabalho repetitivo manual perpétuo para um investimento de pipeline único mais manutenção. Um lançamento manual consome horas de engenheiros sêniores toda vez, escala mal e produz evidência de auditoria fraca. Um pipeline automatizado amortiza esse custo e depois o *reduz* conforme o volume cresce, tudo isso produzindo evidência mais forte continuamente. A reversibilidade baixa o custo da própria falha: quando qualquer mudança pode ser revertida em segundos, o custo esperado de uma implantação ruim colapsa, o que torna racional e não temerário andar depressa.

Para defender o caso junto à liderança, meçam a linha de base atual com as quatro métricas DORA e as horas manuais gastas por lançamento, depois quantifiquem o trabalho repetitivo removido e o tempo fora do ar evitado. O custo de adoção é real, a saber engenharia de pipeline, investimento em testes e uma capacidade de plataforma/caminho pavimentado (capítulo 8.4), mas o custo de *não* investir é pago continuamente em feedback lento, risco no dia do lançamento, esgotamento de engenheiros e dor de auditoria. O argumento decisivo é o elo com a descoberta: um pipeline de entrega rápido e medido é o que torna as apostas validadas do pipeline de descoberta de fato testáveis em produção.

## Antipadrões e armadilhas

- **Medir a saída, não o resultado:** celebrar a contagem de implantações enquanto as métricas-alvo ficam estáveis.
- **Suítes de testes lentas ou instáveis:** portões que os desenvolvedores aprendem a ignorar ou contornar.
- **Lançamentos big-bang e pouco frequentes:** grandes lotes arriscados, difíceis de depurar e difíceis de reverter.
- **Implantação e lançamento misturados:** sem feature flags, então cada implantação é uma aposta irreversível voltada ao usuário.
- **Teatro manual de lançamento:** listas de verificação executadas à mão, lentas, inconsistentes e mal auditadas.
- **Pipeline automatizado, sem observabilidade:** entregar rápido sem capacidade de detectar ou diagnosticar regressões.
- **Dívida de feature flags:** flags nunca removidas, que se acumulam em complexidade combinatória intestável.
- **Manipular as métricas DORA:** dividir implantações para inflar a frequência em vez de melhorar o fluxo.
- **Sem ciclo de feedback:** resultados nunca medidos, então a entrega nunca informa o próximo ciclo de descoberta.

## Modelo de maturidade

- **Nível 1, Iniciar:** Lançamentos manuais, pouco frequentes e de alta cerimônia; testes na maior parte manuais e executados à mão; sucesso medido como “foi entregue”; rollbacks dolorosos e improvisados; nenhuma ideia compartilhada de como a entrega deve funcionar.
- **Nível 2, Desenvolver:** Algumas equipes montam CI com builds automatizados e alguns testes; os lançamentos são agendados; existe monitoramento básico; as práticas variam de equipe para equipe e as métricas DORA ainda não são acompanhadas, então a entrega é melhor em bolsões mas inconsistente na organização.
- **Nível 3, Padronizar:** Um pipeline de caminho pavimentado documentado é imposto em toda a organização: entrega contínua com portões automatizados de teste e segurança, implantação progressiva com rollback e separação de funções imposta como política como código. O pipeline fornece uma trilha de auditoria imutável, e toda equipe segue o mesmo caminho versionado e não um caminho sob medida.
- **Nível 4, Gerenciar:** O pipeline é medido e controlado em relação a linhas de base. As quatro métricas DORA (frequência de implantação, prazo de entrega, taxa de falha das mudanças, tempo de recuperação), o cumprimento de SLOs, a queima do orçamento de erros e métricas de fluxo como tempo de ciclo e trabalho em andamento são acompanhados contra metas, e os portões e rollbacks disparam por limiares medidos e não por julgamento. A dívida de flags, as taxas de testes instáveis e as regressões de prazo de entrega são monitoradas, e cada decisão de seguir ou parar é tomada com base em evidências.
- **Nível 5, Orquestrar:** A entrega é continuamente melhorada e integrada à descoberta e ao planejamento de riscos. A implantação contínua roda onde apropriado com entrega progressiva e rollback automatizado; as funcionalidades são entregues como experimentos medidos cujas métricas de resultado voltam para a próxima rodada de apostas; o desempenho DORA de elite é sustentado entre as equipes pelo caminho pavimentado; e a organização reajusta de forma adaptativa portões, limiares e capacidade conforme a carga, o risco e o mix de produtos mudam.

## Ideias para discussão

1. Quais são as suas quatro métricas DORA atuais, e onde está o maior gargalo no seu fluxo do commit à produção?
2. Vocês conseguem hoje separar a implantação do lançamento? Se não, o que as feature flags mudariam no seu risco?
3. Quanto tempo leva a sua suíte de testes, e os desenvolvedores confiam nela o bastante para não contorná-la?
4. Quando vocês entregaram a última funcionalidade, mediram se ela moveu a métrica que devia mover?
5. Num contexto regulado, o seu processo de controle de mudanças atrasa a entrega *ou* é imposto automaticamente pelo pipeline?
6. Quais feature flags da sua base de código deviam ter sido removidas meses atrás?

## Principais conclusões

- O pipeline de entrega transforma ideias validadas em software em execução e medido, e devolve os resultados à descoberta (capítulo 11.1).
- Automatizem todo o caminho: **portões de teste** rápidos, **CI/CD** e **infraestrutura como código**, com o pipeline como fonte da verdade.
- **Separem a implantação do lançamento** e usem estratégias progressivas (flags, canário, azul-verde) com rollback automatizado.
- Meçam em três níveis: métricas **DORA/de fluxo**, **confiabilidade/SLOs** e **resultados de negócio/usuário**.
- Velocidade e estabilidade são **complementares**, não compromissos: as práticas que entregam uma entregam a outra.
- O pipeline também é um **controle de conformidade**: a automação produz uma trilha de auditoria imutável e contínua.
- O ROI é rápido, bem evidenciado (DORA) e composto; o principal custo de não investir é pago continuamente.

## Referências e leitura complementar

- *Accelerate: The Science of Lean Software and DevOps*, by Nicole Forsgren, Jez Humble, Gene Kim (the DORA metrics and evidence).
- *Continuous Delivery*, by Jez Humble and David Farley (the foundational text).
- *The DevOps Handbook*, by Kim, Humble, Debois, Willis.
- *The Phoenix Project*, by Gene Kim, Kevin Behr, George Spafford (narrative on flow).
- *Site Reliability Engineering*, by Beyer, Jones, Petoff, Murphy, eds. (SLIs/SLOs, error budgets).
- *Team Topologies*, by Matthew Skelton and Manuel Pais (paved roads and delivery-team design).
- *Feature Flags / progressive delivery*, writings by Pete Hodgson and the LaunchDarkly/Split communities.
- Google DORA, *Accelerate State of DevOps* reports (annual).
- Kim, Gene, *The Unicorn Project* (developer-experience view of flow).
- Reinertsen, Donald, *The Principles of Product Development Flow* (batch size, queues, flow economics).
