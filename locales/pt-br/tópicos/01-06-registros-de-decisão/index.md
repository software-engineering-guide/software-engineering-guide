# 1.6 Registros de decisão

## Visão geral e motivação

Um **registro de decisão** é um documento que captura uma decisão importante junto com seu contexto e suas consequências. A forma mais conhecida é o **[registro de decisão de arquitetura](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, uma nota curta, imutável por preferência, que registra uma escolha arquiteturalmente significativa, por que foi feita e o que decorre dela. O conjunto completo de registros de um projeto é o seu **log de decisões (ADL)**, e a disciplina de mantê-los faz parte da **gestão do conhecimento de arquitetura (AKM)**. Este capítulo se apoia nas práticas de tomada de decisão e governança do capítulo 1.5, com foco em como você escreve, armazena e sustenta registros de decisão em escala.

A motivação é simples, e dolorosa de aprender na prática. Em qualquer sistema de longa vida, a pergunta mais cara é “por que diabos isto foi construído assim?”, feita meses ou anos depois por pessoas que não estavam na sala. O código mostra *o que* o sistema faz. Os testes mostram que ele *funciona*. Mas nenhum dos dois captura *por que* você escolheu este caminho em vez das alternativas que considerou e rejeitou. Sem registros de decisão, esse raciocínio se evapora com a rotatividade de pessoal. As equipes rediscutem questões já resolvidas, revertem boas decisões por más razões ou mantêm más decisões por medo. Um registro de decisão é uma carta barata para o futuro que preserva o raciocínio.

Para equipes grandes, isso é tanto uma ferramenta de coordenação quanto um auxílio à memória. Empresas têm dezenas de equipes tomando escolhas que se sobrepõem. Um log de decisões compartilhado transforma o raciocínio duramente conquistado de uma equipe num ativo reutilizável e evita decisões divergentes e incompatíveis. Em contextos governamentais e regulamentados, os registros de decisão são quase obrigatórios. Auditores, órgãos de supervisão e terceirizados sucessores precisam de uma justificativa rastreável que ligue os requisitos arquiteturalmente significativos às escolhas feitas diante deles. Um log de decisões bem mantido é muitas vezes a diferença entre um sistema que você consegue garantir e auditar e um que não consegue.

## Princípios fundamentais

- **Registre o *porquê*, não apenas o *quê*.** O contexto e as alternativas rejeitadas são o ponto central.
- **Uma decisão por registro.** Mantenha cada registro específico e autocontido.
- **Pequeno e leve vence abrangente e sem uso.** Um registro de uma página que existe vence um relatório que nunca é escrito.
- **Date tudo.** Custos, restrições e fornecedores mudam. Date cada afirmação.
- **Prefira um log vivo, pragmaticamente.** A imutabilidade é o ideal. Na prática, corrija com notas datadas.
- **Palavras em vez de siglas.** “Decisões” convida mais contribuição que “ADRs”.
- **Torne as decisões localizáveis e, quando possível, testáveis.** Faça aparecer o registro certo no momento certo e garanta-o com funções de aptidão.

## Recomendações

### Capture a estrutura essencial

Um bom registro de decisão tem algumas seções essenciais. Adapte um modelo conhecido em vez de inventar um:

- **Título:** uma frase curta, imperativa e no presente (“Usar o [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) para o livro-razão”).
- **Status:** proposta, aceita, substituída, obsoleta.
- **Contexto:** a situação, as forças, as prioridades de negócio e as restrições que tornam esta decisão necessária. Inclua o requisito arquiteturalmente significativo a que ela responde.
- **Decisão:** a escolha feita, declarada com clareza.
- **Consequências:** o que fica mais fácil e o que fica mais difícil, as decisões subsequentes disparadas e os riscos aceitos.

Os modelos populares incluem o de Michael Nygard (simples e amplamente adotado), o de Tyree e Akerman (mais elaborado, com alternativas ponderadas), o MADR (Markdown Any Decision Records, forte em opções e seus prós e contras) e as declarações Y (uma forma estruturada de uma frase). Padronize um por organização, para que os registros sejam comparáveis. Veja o capítulo 12.3 para um modelo de copiar e colar.

### Escreva registros específicos, datados e quase imutáveis

Mantenha cada registro sobre exatamente uma decisão. Date as afirmações individuais, especialmente tudo que deriva: preços, números de escala, capacidades de fornecedores, termos de licença. Em teoria, um registro deve ser imutável. Quando uma decisão muda, você escreve um *novo* registro que substitui o antigo, preservando o histórico. Na prática, muitas equipes acham que uma abordagem de **documento vivo** funciona melhor: inserir novas informações no registro existente com uma data e uma nota de que chegaram depois da decisão. As duas são legítimas. O estilo imutável é mais forte para trilhas de auditoria. O estilo vivo é melhor para o conhecimento cotidiano da equipe. Escolha deliberadamente e seja consistente.

### Armazene os registros onde o trabalho acontece

Ponha os registros de decisão no [controle de versões](https://en.wikipedia.org/wiki/Version_control) junto com o código: um diretório `decisions/` (ou `adr/`) de arquivos [Markdown](https://en.wikipedia.org/wiki/Markdown), um por decisão, nomeados com uma locução verbal imperativa em minúsculas e separada por hífens (`choose-database.md`, `format-timestamps.md`). Isso lhe dá histórico, revisão e comparação de graça e mantém a justificativa ao lado do que ela explica. Se a sua equipe prefere [wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs ou um rastreador no estilo Jira, use esses. A ferramenta importa muito menos que o hábito. Uma ferramenta leve de linha de comando (como o `adr-tools`) pode gerar o esqueleto e indexar os registros.

### Chame-os de “decisões” e amplie para além da arquitetura

Uma percepção prática de muitas equipes: o rótulo importa. Alguns desenvolvedores e gestores se irritam com a palavra “arquitetura”, e “registro” pode parecer papelada feita depois do fato. Renomear o diretório simplesmente para “decisions” muitas vezes vira uma chave. As equipes começam a registrar escolhas de fornecedores, decisões de planejamento, decisões de cronograma, decisões de dados e de conformidade, tudo com o mesmo modelo. As pessoas aprendem mais rápido com palavras do que com siglas e contribuem mais quando o enquadramento é “ajude seus futuros colegas a pensar” em vez de “preencha o formulário obrigatório”.

### Defina o ciclo de vida e a governança

Para que os registros de decisão escalem, combine o processo em torno deles (é aqui que a governança do capítulo 1.5 encontra a prática):

- **Quem pode abrir um e o que o justifica:** em geral qualquer colaborador informado. Abra um registro quando os desenvolvedores futuros precisarem do *porquê* e dispense-o para escolhas de baixo risco, autocontidas ou já documentadas.
- **Ciclo de vida:** um fluxo simples como *Iniciar → Pesquisar → Avaliar → Implementar → Manter → Encerrar*, com critérios de aceitação para passar de uma etapa a outra (problema articulado, alternativas consideradas, compromissos documentados, partes interessadas consultadas).
- **Papéis:** proponente, pesquisador, revisor, aprovador e um mantenedor responsável que revisa o registro periodicamente (pelo menos uma vez por ano) e conduz o eventual encerramento.
- **Governança:** como funcionam o consenso, o conflito, a escalada e o veto, e quaisquer restrições de conformidade. Apoie-se em princípios como *viés para a ação* e *[discordar e comprometer-se](https://en.wikipedia.org/wiki/Disagree_and_commit)*, e reserve processo mais pesado para decisões irreversíveis e de grande raio de impacto (“portas de mão única”).

### Torne as decisões testáveis e localizáveis

Um registro de decisão *documenta* uma decisão. Uma **função de aptidão** a *garante*: uma verificação automatizada, executada na [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), que confirma que a decisão ainda vale (“toda mudança de estado deve emitir eventos”, “nenhum módulo pode importar através destas fronteiras”, usando ferramentas como o ArchUnit). Isso transforma a governança de revisão manual periódica em imposição contínua e escalável, o que é especialmente valioso para metas regulatórias e de auditoria (capítulos 3.1, 4.6, 8.5). Depois faça aparecer o registro *certo* no momento *certo*. Ferramentas que anexam as decisões relevantes a um pull request, quando um desenvolvedor mexe no código que elas governam, vencem a esperança de que as pessoas leiam uma pasta de documentos.

## Compromissos: prós e contras

| Escolha | Prós | Contras |
|---|---|---|
| **ADRs leves (Nygard/MADR)** | Rápidos de escrever, de fato são escritos. Pouca cerimônia | Menos rigor para decisões contestadas e de alto risco |
| **Modelos pesados (Tyree-Akerman)** | Alternativas ponderadas. Fortes para escolhas grandes e caras | Mais lentos. Podem desencorajar o registro de rotina |
| **Imutável + substituir** | Trilha de auditoria limpa. Histórico preservado | Mais registros. Os leitores precisam seguir cadeias |
| **Documento vivo (correções datadas)** | Uma única fonte atual da verdade. Fácil de manter | História de auditoria mais fraca. Risco de edições silenciosas |
| **Markdown no repositório** | Versionado, revisável, ao lado do código | Menos amigável a quem não é desenvolvedor |
| **Wiki / ferramenta de documentos** | Acessível a todos os papéis | Histórico e revisão mais fracos. Afasta-se do código |

A tensão central é **rigor versus adoção**. O sistema mais rigoroso que ninguém usa não registra nada. O sistema mais leve que todos usam ganha valor composto. Adote o leve por padrão e reserve processo mais pesado para as poucas decisões caras e difíceis de reverter.

## Perguntas para discutir com sua equipe

1. **Como o registro de decisão certo chegará a um desenvolvedor no momento em que ele mexe no código que ele governa, em vez de ficar numa pasta que ninguém abre?** Um log só de escrita registra raciocínio que nunca muda o comportamento, que é a forma mais comum de os registros de decisão falharem: eles existem, e ninguém os lê quando importa. A consideração concorrente é o esforço, porque fazer os registros aparecerem automaticamente (anexando-os a um pull request quando alguém edita o código governado) exige um investimento em ferramentas que uma wiki ou pasta de documentos não exige. Leve evidências à discussão: quando alguém recentemente reverteu ou rediscutiu uma questão resolvida, o registro relevante era localizável naquele momento ou estava enterrado? Para uma organização grande com dezenas de equipes, a capacidade de localizar é o que transforma o raciocínio duramente conquistado de uma equipe num ativo reutilizável em vez de um arquivo privado. Decida se vai armazenar os registros no controle de versões ao lado do código e ligá-los ao fluxo de pull requests, para que o registro apareça onde o trabalho acontece.

2. **Quem é o mantenedor responsável por cada registro, e o que impede que o seu log degenere em desinformação confiante?** O modo de falha perigoso de um log de decisões não é uma pasta vazia, é uma pasta cheia de registros cujos custos, capacidades de fornecedores e restrições ficaram obsoletos em silêncio anos atrás. Cada registro precisa de um responsável que o revise com regularidade (pelo menos uma vez por ano) e conduza a substituição ou o encerramento, ou o log apodrece em folclore que as pessoas citam seletivamente e em que pouco confiam. Leve evidências: quantos dos seus registros não têm data, quantos descrevem um fornecedor ou preço que mudou desde então e quando cada um foi revisado pela última vez. Em contextos governamentais e regulamentados isso é mais agudo, porque uma cadeia imutável de registros substituídos é exatamente aquilo em que auditores e terceirizados sucessores se apoiam para uma justificativa rastreável. Decida explicitamente o seu ciclo de vida, date as afirmações individuais que derivam e atribua mantenedores, para que o log continue sendo um ativo vivo em vez de um cemitério.

3. **Você deve padronizar um modelo único para todas as equipes, e quanto rigor as suas decisões de maior risco de fato exigem?** A comparabilidade é um benefício real: quando todas as equipes usam o mesmo formato (Nygard, MADR ou similar), uma nova equipe consegue achar três registros anteriores e adotar o raciocínio numa tarde em vez de um mês de debate. A tensão central é rigor versus adoção, porque o modelo mais pesado que ninguém usa não registra nada, enquanto o mais leve que todos usam ganha valor composto. Leve evidências: os registros estão de fato sendo escritos e, separadamente, alguma decisão grande, contestada e cara foi pouco analisada porque a forma leve pulou a ponderação de alternativas? Para empresas que coordenam escolhas sobrepostas entre equipes, um modelo compartilhado mais um índice pesquisável evita decisões divergentes e incompatíveis. Adote o leve por padrão para o caso comum e combine de antemão quais decisões de porta de mão única justificam uma forma mais pesada, com alternativas ponderadas.

4. **O que de fato justifica abrir um registro de decisão, e quem tem autoridade para dizer que uma escolha não precisa de um?** Se a barra for alta demais, o raciocínio por trás das escolhas consequentes se evapora. Se for baixa demais, o log se enche de trivialidades que enterram os registros de que as pessoas realmente precisam. Para uma organização grande, um limiar pouco claro significa que cada equipe improvisa o seu, de modo que a cobertura fica desigual e ninguém pode confiar que a ausência de um registro sinaliza uma decisão sem importância. Leve evidências à discussão: um punhado de decisões recentes que foram registradas mas não precisavam ser e outras dolorosas que não foram registradas e depois custaram uma redescoberta. Combine um teste simples, como registrar sempre que um desenvolvedor futuro precisar do *porquê* e dispensar escolhas de baixo risco, autocontidas ou já documentadas. Em contextos regulamentados e governamentais o cálculo muda, porque um mandato de auditoria pode exigir um registro para cada requisito arquiteturalmente significativo, quer a equipe julgue que vale a pena escrevê-lo ou não, então nomeie de início quais decisões são inegociáveis.

5. **Os seus registros são raciocínio genuíno capturado no momento da decisão, ou papelada escrita depois para cumprir um mandato?** Um registro produzido depois do fato para fechar um tíquete tende a lavar a opção escolhida e a omitir em silêncio as alternativas que de fato foram pesadas, que é precisamente a informação de que um leitor futuro mais precisa. A pressão concorrente é real: escrever o *porquê* antes ou durante uma decisão parece mais lento que entregar, e admitir por escrito os caminhos rejeitados exige uma segurança psicológica que algumas equipes não têm. Leve uma amostra de registros recentes à mesa e pergunte com honestidade se o contexto e as alternativas rejeitadas soam como deliberação real ou como justificativa retroativa. Para uma equipe grande, registros vazios são piores que nenhum, porque ensinam às pessoas que o log não merece confiança. Em auditorias corporativas e governamentais essa distinção é nítida: órgãos de supervisão e terceirizados sucessores dependem de uma justificativa que reflita o que foi realmente considerado, e um registro que parece teatro mina a garantia que o log existe para dar.

6. **Quais das suas decisões de maior risco você consegue garantir com uma função de aptidão automatizada, em vez de confiar que a revisão manual periódica pegará uma violação?** Um registro de decisão documenta uma escolha, mas só uma verificação automatizada executada na integração contínua impede que essa escolha se erode em silêncio à medida que dezenas de desenvolvedores mexem no código ao longo dos anos. O compromisso é o investimento, porque escrever e manter funções de aptidão (com ferramentas como o ArchUnit) custa tempo de engenharia, e muitas decisões, especialmente de processo ou de fornecedor, simplesmente não são testáveis mecanicamente. Leve evidências: quais decisões de fronteira (dependências entre módulos, emissão de eventos, regras de acesso a dados) foram violadas em silêncio e só detectadas tarde, na revisão ou em produção. Para uma empresa com muitas equipes, as funções de aptidão transformam a governança de gargalo central em imposição contínua que escala sem atrasar todo mundo. Em contextos regulamentados e governamentais, uma verificação automatizada e sempre ativa é uma evidência de auditoria muito mais forte que uma assinatura numa revisão, porque prova que a decisão ainda vale hoje, e não que alguém um dia a aprovou.

## Perspectiva por setor

**Startup.** Fique no hábito e em nada mais: uma pasta `decisions/` no repositório principal e uma nota de duas seções (contexto e escolha) sempre que você tomar uma decisão que o seu eu futuro vai questionar. Pule ciclo de vida, papéis e aprovadores por completo, porque um processo que você não consegue sustentar é um processo que você vai abandonar. O único registro que poupa a sua primeira contratação de perguntar por que o sistema é construído assim já paga a prática inteira.

**Pequena empresa.** Sem arquiteto dedicado e com pouco tempo, ponha os registros onde a sua equipe já trabalha, seja uma wiki, um documento compartilhado ou o repositório, em vez de comprar uma ferramenta dedicada. O hábito importa muito mais que a ferramenta, então baixe a barreira: chame o diretório de `decisions` em vez de `adr` e capture as escolhas de fornecedor e de construir ou comprar no mesmo fôlego que as técnicas. Quando você depende de terceirizados externos, um registro curto e datado de por que escolheu um fornecedor ou uma plataforma é um seguro barato contra ficar preso a uma escolha que ninguém consegue explicar depois.

**Grande empresa.** O trabalho é a coordenação entre muitas equipes: padronize um modelo, publique um índice pesquisável entre equipes e apoie as decisões de fronteira importantes com funções de aptidão, para que as violações quebrem o build em vez de esperar a revisão. Atribua um mantenedor responsável a cada registro com uma cadência de revisão, para que o log continue um ativo vivo em vez de degenerar em folclore. Bem feito, o raciocínio de uma equipe sobre uma escolha difícil vira um ativo que a próxima equipe adota numa tarde em vez de rediscutir.

**Governo.** Regras de contratação, transparência e responsabilização pública tornam os registros de decisão quase obrigatórios. Exija um registro imutável e substituído para cada requisito arquiteturalmente significativo, cada um ligando a escolha ao mandato ou ao controle de conformidade que ela satisfaz, para que os órgãos de supervisão encontrem uma justificativa rastreável e não uma reconstrução. Como os sistemas públicos atravessam vidas de vários anos e vários fornecedores, um log bem mantido é muitas vezes o que permite a um terceirizado sucessor entender por que o sistema tem a forma que tem e continuar o trabalho sem rediscutir terreno já resolvido.

## Exemplos

**Startup.** Uma startup de cinco pessoas acrescenta uma pasta simples `decisions/` ao repositório principal, com uma nota de duas seções (contexto e escolha) sempre que alguém toma uma decisão que o seu eu futuro vai questionar. Não há ciclo de vida, nem papéis, nem aprovadores: só o hábito de escrever o *porquê* ao lado do código. Quando a primeira contratação chega, seis meses depois, ela lê a pasta inteira em uma hora e para de perguntar “por que foi construído assim?”. O log leve custa minutos por entrada e os poupa do imposto de redescoberta, que morde muito antes de a equipe crescer.

**Grande empresa.** Um varejista com 30 equipes de engenharia padroniza registros no formato MADR em cada repositório, mais um índice central pesquisável. Quando uma nova equipe enfrenta o dilema “[monorepo](https://en.wikipedia.org/wiki/Monorepo) versus multirrepo”, encontra três registros anteriores com contexto e consequências e adota o raciocínio numa tarde em vez de um mês de debate. As decisões de fronteira importantes (propriedade de serviços, regras de acesso a dados) são apoiadas por funções de aptidão do ArchUnit, de modo que as violações quebram o build em vez de serem pegas na revisão. Isso é governança que escala sem um gargalo central.

**Governo.** Uma agência que moderniza um sistema de benefícios exige um ADR para cada requisito arquiteturalmente significativo, cada um ligando a decisão ao mandato ou ao controle de conformidade que ela satisfaz (acessibilidade, residência de dados, auditabilidade). Os registros são imutáveis e substituídos, produzindo um log rastreável que satisfaz a revisão de supervisão. De forma crucial, isso também permite que um terceirizado sucessor entenda *por que* o sistema tem a forma que tem, preservando a continuidade ao longo das vidas de vários anos e vários fornecedores típicas dos programas públicos (capítulos 4.6, 10.4).

## Justificativa de negócio: motivações, ROI e TCO

Um registro de decisão custa minutos para escrever e alguns outros para revisar. O retorno é o custo evitado de *redecidir* e o custo evitado de *reverter errado*, ambos grandes e recorrentes em sistemas de longa vida. Toda vez que uma equipe rediscute uma questão resolvida, ou reverte uma escolha sólida porque ninguém se lembrava da restrição por trás dela, paga em tempo de engenheiros seniores e muitas vezes em um incidente. Um log de decisões converte esse imposto recorrente numa escrita única.

No **custo total de propriedade**, os registros de decisão estão entre a documentação de maior alavancagem que você pode manter, porque miram o ativo mais sensível à rotatividade: a justificativa. A integração é mais rápida (as pessoas novas leem o *porquê*, não só o código). A modernização é mais segura (capítulo 3.6: você distingue as decisões essenciais das incidentais). As auditorias são mais baratas (a evidência já existe). O custo de *não* mantê-los é invisível em qualquer painel e se acumula em silêncio a cada saída. Para defender o caso junto à liderança, aponte uma redescoberta cara recente, ou uma decisão revertida que causou um incidente, e observe que a correção custa quase nada para instituir.

## Antipadrões e armadilhas

- **Registrar o *quê* sem o *porquê*:** omitir o contexto e as alternativas rejeitadas, que são o ponto central.
- **Papelada depois do fato:** registros escritos para cumprir um mandato, não para pensar. Soam vazios e ninguém confia neles.
- **Mega-documentos de várias decisões:** uma página gigante que ninguém consegue navegar nem substituir de forma limpa.
- **Afirmações sem data:** custos e restrições que foram verdadeiros um dia, apresentados como atemporais.
- **Edições silenciosas:** mudar a história de uma decisão sem uma nota datada, destruindo a trilha de auditoria.
- **Logs só de escrita:** registros criados e nunca mostrados no momento em que são relevantes, de modo que não influenciam o comportamento.
- **Elitismo de siglas:** insistir em “ADR” e “arquitetura” e assim desencorajar a contribuição.
- **Sem ciclo de vida:** registros que nunca são revisados, substituídos ou encerrados, degenerando em desinformação.

## Modelo de maturidade

- **Nível 1 (Iniciar):** As decisões vivem nas cabeças das pessoas, em conversas de chat e em mensagens de commit. A captura é reativa e ad hoc, e a justificativa se perde rotineiramente com a rotatividade de pessoal.
- **Nível 2 (Desenvolver):** Algumas equipes mantêm registros, em formatos e modelos variados, sempre que um indivíduo se lembra. A prática é inconsistente entre as equipes, sem log, nomenclatura ou processo compartilhados.
- **Nível 3 (Padronizar):** Um modelo único, o armazenamento no repositório e um ciclo de vida e uma governança definidos (critérios de abrir ou dispensar, papéis, cadência de revisão) são documentados e aplicados de forma consistente na organização. Os registros são revisados e substituídos em vez de editados em silêncio.
- **Nível 4 (Gerenciar):** O log de decisões é medido em relação a linhas de base: cobertura (a parcela das decisões arquiteturalmente significativas que têm registro), atualidade (a parcela de registros revisados dentro da sua cadência, mais a contagem de afirmações sem data ou obsoletas) e capacidade de localização (com que frequência um registro relevante de fato chegou ao desenvolvedor que mudou o código governado). Os mantenedores responsáveis agem sobre essas métricas, substituindo registros obsoletos e fechando lacunas de cobertura com base em evidências e não em anedotas.
- **Nível 5 (Orquestrar):** Um log de decisões pesquisável entre equipes é integrado ao trabalho diário: os registros relevantes aparecem automaticamente nas mudanças que governam, as decisões importantes são garantidas por funções de aptidão na integração contínua e o log alimenta a integração, a modernização e a auditoria como um ativo vivo. A organização melhora continuamente a própria prática, aposentando, substituindo e redefinindo o escopo dos registros conforme o sistema e suas restrições mudam, e reequilibrando onde investe rigor à medida que o portfólio de decisões cresce.

## Ideias para discussão

1. Qual foi a última decisão que a sua equipe reverteu ou rediscutiu porque ninguém se lembrava do raciocínio original?
2. Renomear o seu diretório `adr/` para `decisions/` mudaria quem contribui e o que é registrado?
3. Quais das suas decisões críticas poderiam ser garantidas hoje por uma função de aptidão automatizada?
4. Imutável e substituir, ou documento vivo: qual se ajusta às suas obrigações de auditoria e à sua cultura, e por quê?
5. Como uma pessoa recém-contratada (ou um terceirizado sucessor) descobriria hoje *por que* o seu sistema tem a forma que tem?
6. O que justifica abrir um registro de decisão na sua equipe, e o que justifica *não* abrir um?

## Principais conclusões

- Um registro de decisão captura uma decisão importante com seu **contexto e suas consequências**: o *porquê*, não só o *quê*.
- Mantenha os registros **específicos, datados e leves**. Padronize um modelo (Nygard, MADR ou similar).
- Armazene-os **no controle de versões ao lado do código**. Considere chamá-los de “decisions” para ampliar a contribuição.
- Defina um **ciclo de vida e uma governança** (critérios de abrir ou dispensar, papéis, cadência de revisão). Reserve o processo pesado para decisões de porta de mão única.
- Torne as decisões **localizáveis** no momento da mudança e, quando possível, **testáveis** por funções de aptidão.
- O ROI é o custo evitado de redescoberta e de reversão errada. O argumento do TCO é mais forte onde a rotatividade, a modernização e a auditoria mais importam. Veja o capítulo 1.5 (tomada de decisão e governança) e o capítulo 3.1 (fundamentos de arquitetura).

## Referências e leitura complementar

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
