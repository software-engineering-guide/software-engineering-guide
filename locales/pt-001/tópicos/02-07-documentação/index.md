# 2.7 Documentação

## Visão geral e motivação

A [documentação](https://en.wikipedia.org/wiki/Software_documentation) é o conhecimento escrito que permite às pessoas usar, operar e alterar o software sem precisar montar o entendimento só a partir do código. Ela vem em muitos gêneros: como começar, como realizar uma tarefa, como um sistema é estruturado, como responder a um incidente, o que uma [API](https://en.wikipedia.org/wiki/API) aceita e devolve. Cada um serve a um leitor diferente, com uma necessidade diferente. Uma boa documentação não é opcional. É a diferença entre o conhecimento que escala numa grande organização e o conhecimento que vive na cabeça de umas poucas pessoas.

Para equipes grandes, a documentação é a sua melhor defesa contra o risco de dependência de pessoas-chave (o perigo de o conhecimento crítico estar com apenas uma ou poucas pessoas) e a sua forma mais rápida de integrar os recém-chegados. Quando centenas de engenheiros dependem de sistemas que não construíram, e as pessoas entram, mudam de área e saem o tempo todo, a organização só funciona se o conhecimento estiver escrito e for fácil de encontrar. Sistemas não documentados ficam frágeis: só os autores conseguem alterá-los com segurança, e quando esses autores saem, a organização perde a capacidade de manter o próprio software. Essa é uma das falhas mais comuns e caras em escala.

Os contextos corporativos e governamentais elevam ainda mais o que está em jogo. Os sistemas vivem muito tempo, então a sua documentação precisa servir a mantenedores anos, até décadas, depois de a equipe original ter ido embora. Os regimes regulatórios e de auditoria muitas vezes exigem documentos específicos como evidência de controle: registros de arquitetura, [runbooks](https://en.wikipedia.org/wiki/Runbook) (procedimentos operacionais e de resposta a incidentes passo a passo) e registros de decisão. Os sistemas do setor público passados de fornecedor a fornecedor dependem inteiramente da documentação para levar o conhecimento através das fronteiras contratuais. E, no entanto, a documentação é famosa por apodrecer, então o desafio real é mantê-la precisa à medida que o software muda.

## Princípios fundamentais

- Escreva para um leitor específico com uma necessidade específica. Tipos diferentes de documentação servem a propósitos diferentes.
- Mantenha a documentação perto do código e trate-a como código (docs como código).
- Precisão vence completude. Uma pequena quantidade de documentação confiável vence uma grande quantidade que está errada.
- Gere o que puder ser gerado. Não mantenha à mão o que uma ferramenta consegue produzir a partir da fonte da verdade.
- Combata ativamente o apodrecimento da documentação. Documentos obsoletos são piores que nenhum, porque enganam.
- Torne a documentação localizável. Conhecimento que não se encontra é, na prática, ausente.
- Registre as decisões e a sua justificativa, não apenas o estado atual.

## Recomendações

### Adote docs como código

Mantenha a documentação no [controle de versões](https://en.wikipedia.org/wiki/Version_control) ao lado do código que ela descreve, escreva-a em marcação de texto simples e revise-a pelo mesmo processo de pull requests. Isso a mantém versionada, revisável e perto do código, para que você possa atualizar os dois juntos. Publique-a por meio de um pipeline automatizado para que a versão mais recente esteja sempre disponível. Tratar a documentação como código traz a mesma disciplina que mantém o código confiável: revisão, histórico e automação.

### Estruture o conteúdo com a estrutura Diátaxis

Organize a documentação em quatro tipos distintos, porque misturá-los não serve bem a nenhum leitor: tutoriais (orientados ao aprendizado, para recém-chegados), guias práticos (orientados à tarefa, para um objetivo específico), referência (orientada à informação, precisa e completa) e explicação (orientada ao entendimento, o porquê e o contexto). Mantenha-os separados e tudo fica mais fácil de escrever, de navegar e de manter, porque cada página tem uma tarefa clara e um público claro.

### Mantenha os documentos operacionais essenciais

Dê a cada repositório um [README](https://en.wikipedia.org/wiki/README) claro como porta de entrada: o que ele é, como construí-lo e executá-lo e para onde ir em seguida. Escreva runbooks para tarefas operacionais e resposta a incidentes, para que qualquer pessoa de sobreaviso possa agir, não apenas os especialistas. Mantenha a documentação de arquitetura que explica a estrutura e os componentes principais do sistema. E forneça documentação de integração que torne uma pessoa engenheira nova produtiva rapidamente. São os documentos de que você mais sente falta quando não existem.

### Gere a documentação de API e os registros de mudanças a partir da fonte da verdade

Gere a documentação de referência da sua API a partir do contrato legível por máquina ou das anotações do código, para que ela não possa se afastar da interface real. Mantenha um [registro de mudanças](https://en.wikipedia.org/wiki/Changelog), idealmente gerado a partir de commits estruturados ou de notas de lançamento, para que os consumidores vejam o que mudou entre versões. Automatizar isso tira do seu prato a documentação mantida à mão que mais apodrece e a mantém confiável.

### Registre as decisões de arquitetura

Capture as decisões significativas de arquitetura e de design como registros leves e datados que declaram o contexto, a decisão e suas consequências. Esses registros de decisão preservam a justificativa que de outro modo se perderia, para que os futuros mantenedores vejam por que o sistema é como é, em vez de questioná-lo ou repetir erros antigos. Eles compensam especialmente ao longo das vidas longas dos sistemas corporativos e governamentais.

### Combata o apodrecimento da documentação deliberadamente

Trate a documentação obsoleta como um defeito. Atualize a documentação na mesma mudança que altera o comportamento e faça disso uma expectativa de revisão. Atribua responsabilidade para que todo documento importante tenha alguém responsável por ele. Revise de vez em quando a precisão da documentação de alto valor, pode o que está obsoleto e remova ou sinalize com clareza tudo em que você já não confia. A documentação que menos apodrece é a documentação viva: gerada ou testada contra o próprio sistema.

### Invista em gestão do conhecimento e em capacidade de localização

Torne a documentação localizável por meio de uma boa busca, de uma navegação clara e de um lar conhecido, para que as pessoas encontrem o que precisam sem ter de perguntar a alguém. Não a deixe se fragmentar em wikis e ferramentas desconectados demais. E capture o [conhecimento tácito](https://en.wikipedia.org/wiki/Tacit_knowledge), o entendimento informal que vive em conversas de chat e nas cabeças das pessoas, numa forma durável e localizável antes que escape.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Docs como código | Versionada, revisável, perto do código. Pouco apodrecimento | Exige disciplina dos engenheiros. Menos amigável a autores não técnicos |
| Wiki / base de conhecimento | Fácil de editar. Acessível a todos | Afasta-se do código. Fragmenta. Apodrece em silêncio |
| Documentação gerada (API, registro de mudanças) | Sempre precisa. Pouca manutenção | Limitada ao que a fonte expressa. Exige ferramentas |
| Explicação escrita à mão | Contexto rico e justificativa que as máquinas não produzem | Trabalhosa. Propensa a ficar obsoleta |
| Estrutura Diátaxis | Propósito claro por página. Mais fácil de navegar e manter | Esforço inicial de estruturação. Exige disciplina dos autores |

O compromisso central é esforço versus precisão e durabilidade. A documentação mais barata de escrever, uma página rápida de wiki, é também a mais propensa a apodrecer e a se fragmentar. A documentação mais durável, gerada a partir da fonte ou revisada como código, custa mais disciplina de início, mas continua confiável. Uma boa regra prática: gere o que puder, mantenha o resto perto do código e revisado como código e reserve a trabalhosa explicação escrita à mão para a justificativa que só os humanos podem fornecer.

## Perguntas para discutir com sua equipe

1. **Seus documentos são separados pela necessidade do leitor, ou tutoriais, referência e explicação se misturam numa mesma página?** Este capítulo recomenda a divisão Diátaxis em tutoriais, guias práticos, referência e explicação e lista a mistura de tipos como um antipadrão que não serve bem a nenhum leitor. Em escala, uma pessoa recém-chegada aprendendo o sistema e uma pessoa de sobreaviso caçando um fato preciso precisam de páginas diferentes, e uma única página mista desacelera as duas. Leve o sinal: escolha seus documentos mais visitados e verifique se cada um tem uma tarefa clara e um público claro. Reestruture os piores casos em tipos distintos, para que cada página seja mais fácil de escrever, de navegar e de manter atualizada. Essa estrutura é o que torna a documentação mantível à medida que a organização cresce.

2. **Vocês capturam as decisões significativas de arquitetura com a sua justificativa, ou apenas o estado atual?** O capítulo recomenda registros de decisão leves e datados que declaram contexto, decisão e consequências e observa que eles compensam mais ao longo das vidas longas dos sistemas corporativos e governamentais. Sem eles, um mantenedor anos depois não consegue ver por que o sistema é como é, então questiona escolhas sólidas ou repete erros antigos. Leve como sinal concreto uma decisão difícil recente cujo raciocínio hoje vive apenas num fio de chat ou na memória de alguém. Adote um formato curto de registro de decisão e faça de escrever um deles parte de qualquer mudança significativa de design. A justificativa é exatamente o conhecimento que só os humanos podem fornecer e que mais depressa apodrece quando não é escrito.

3. **Qualquer pessoa de sobreaviso consegue responder a um incidente só com os seus runbooks, sem acionar a pessoa que construiu o sistema?** Este capítulo nomeia os runbooks como um documento operacional essencial para que qualquer pessoa de sobreaviso possa agir, não apenas os especialistas, e descreve uma equipe governamental que só pôde herdar um sistema porque os runbooks levaram o conhecimento através de uma fronteira contratual. O risco de dependência de pessoas-chave é a falha de que isso protege: quando o único especialista está inacessível ou foi embora, um procedimento de recuperação não documentado transforma um incidente rotineiro numa queda de serviço. Leve as evidências: pegue um incidente recente e verifique se o runbook sozinho o teria resolvido. Escreva e teste runbooks para os procedimentos que as pessoas temem e trate um runbook que não se sustenta sozinho como um defeito. Essa é a diferença entre uma recuperação às 2 da manhã e uma escalada às 2 da manhã.

4. **Quais das suas referências de API e registros de mudanças são gerados a partir da fonte da verdade, e quais ainda são mantidos à mão e se afastam em silêncio?** Este capítulo manda gerar a documentação de referência a partir do contrato legível por máquina ou das anotações do código, para que ela não possa divergir da interface real, e lista a manutenção manual de conteúdo gerável como um antipadrão. Para uma equipe grande, uma documentação de API escrita à mão que fica atrás da interface real é pior que nenhuma: todo consumidor que confia nela escreve uma integração quebrada, e a falha aparece longe da página obsoleta que a causou. Leve o sinal concreto: amostre um punhado das suas interfaces mais usadas e compare a referência publicada com o contrato real para ver o quanto cada uma se afastou. Onde encontrar deriva, ligue a referência ao build para que ela se regenere a cada mudança e aposente a cópia mantida à mão. Em contextos corporativos e governamentais, onde as interfaces são consumidas entre equipes, fornecedores e fronteiras contratuais que você nunca vê, uma referência gerada e autoritativa costuma ser a única coisa que impede os integradores de construir contra a ficção.

5. **Quem é o responsável por cada documento de alto valor, e como vocês perceberiam hoje se um deles tivesse ficado obsoleto?** O capítulo trata a documentação obsoleta como um defeito e avisa que documentos sem responsável apodrecem porque atualizá-los não é tarefa de ninguém, enquanto documentos obsoletos apresentados como atuais destroem a confiança em toda a sua documentação. Em escala, o perigo não é uma única página errada, mas a lenta erosão da confiança: depois que os leitores se queimam com instruções desatualizadas, param de confiar em todo o acervo e voltam a interromper as pessoas. Leve um mapa de responsabilidade dos seus documentos mais críticos e uma resposta honesta sobre como o apodrecimento é detectado, seja por cadência de revisão, por geração, por testes contra o sistema ou por pura sorte. Atribua um responsável nomeado a todo documento que importa e prefira a documentação viva, gerada ou testada, para que a obsolescência apareça de forma mecânica e não por um leitor constrangido. Para sistemas corporativos e governamentais que sobrevivem às equipes originais, a documentação sem responsável é um passivo que um auditor ou um fornecedor que herda acabará cobrando de você.

6. **Quão localizável é a sua documentação, e quanto conhecimento crítico ainda vive apenas em conversas de chat e nas cabeças das pessoas?** Este capítulo diz que o conhecimento que não se encontra é, na prática, ausente, avisa contra fragmentar a documentação em wikis e ferramentas desconectados demais e pede que você capture o conhecimento tácito numa forma durável e localizável antes que escape. Numa grande organização, o mesmo fato é muitas vezes redescoberto, perguntado de novo e respondido de novo uma centena de vezes porque ninguém consegue achar onde ele já foi escrito, e cada saída leva embora um contexto insubstituível. Leve as evidências: conte quantos lares separados de documentação vocês mantêm, tente achar três fatos importantes só pela busca e note onde as respostas reais acabaram morando na memória de alguém ou numa mensagem enterrada. Consolide em direção a um lar conhecido com busca de verdade e navegação clara e faça da captura do conhecimento tácito uma parte rotineira do trabalho e não um resgate heroico. Em contextos do setor público e fortemente terceirizados, onde os sistemas passam entre fornecedores e equipes por contrato, o conhecimento escrito e localizável é a única coisa que sobrevive à passagem de bastão.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e nenhuma pista sobrando, documente apenas o que uma queda às 2 da manhã ou uma pessoa nova realmente precisaria: um README de verdade por serviço, um runbook testado para o procedimento de implantar e recuperar que todos temem e algumas notas datadas sobre as decisões que de outro modo você esqueceria. Gere a documentação de API a partir do contrato para nunca precisar mantê-la à mão. Resista a construir uma plataforma de documentação. Uma pasta versionada de marcação ao lado do código basta até você sentir dor de verdade.

**Pequena empresa.** Sem redator técnico e com orçamento apertado, apoie-se na documentação que as suas ferramentas já geram e em docs como código leve, em vez de um programa com pessoal dedicado. Enquadre a escolha como comprar versus construir: prefira plataformas que produzam a própria referência atual e uma base de conhecimento pesquisável a uma wiki que você precisa cuidar à mão. Gaste o seu escasso esforço nos dois ou três documentos cuja ausência pararia o negócio e deixe uma página errada ou ausente ser o gatilho para corrigir a responsabilidade.

**Grande empresa.** Entre muitas equipes, o problema é a consistência e a capacidade de localização: um pipeline compartilhado de docs como código, uma estrutura comum como a Diátaxis, referências de API e registros de mudanças gerados e registros de decisão aplicados da mesma forma em toda parte, para que o conhecimento não se fragmente em dezenas de wikis. Atribua responsabilidade a todo documento de alto valor e meça a precisão, não apenas a presença. Trate os registros de arquitetura, os runbooks e os registros de decisão como evidência de auditoria e padronize como são produzidos, para que uma revisão de controles encontre uma trilha documentada e defensável e não uma correria.

**Governo.** As regras de contratação e a responsabilização pública fazem da documentação um entregável, não uma cortesia. Escreva a documentação de arquitetura, os runbooks e os registros de decisão nos contratos como artefatos obrigatórios, revisados quanto à precisão, para que o conhecimento sobreviva a uma transição de fornecedor e um sistema possa ser operado por quem o herdar. Exija que qualquer operador autorizado consiga responder a um incidente só com o runbook e mantenha os registros de decisão como um registro público transparente de por que as escolhas foram feitas. A documentação rasa aqui não é um inconveniente privado: vira uma engenharia reversa cara financiada pelo contribuinte.

## Exemplos

**Startup.** Uma startup de cinco pessoas escreve um README de verdade para cada serviço e um runbook curto para o único procedimento de implantar e recuperar que todos temem, de modo que uma queda às 2 da manhã não dependa de acordar o único fundador que conhece o sistema. Eles geram a documentação de API a partir do contrato em vez de escrevê-la à mão e anotam algumas notas datadas explicando por que escolheram o banco de dados e a abordagem de autenticação. Continua leve, mas significa que a sexta e a sétima contratações se integram a partir de documentos e não interrompendo todo mundo.

**Grande empresa.** Uma grande empresa de software mantém toda a sua documentação nos mesmos repositórios do código, escrita em marcação e revisada em pull requests ao lado das mudanças que descreve. As referências de API são geradas a partir dos contratos dos serviços, de modo que nunca se afastam. Os registros de mudanças são gerados a partir de commits estruturados, e os registros de decisão de arquitetura preservam o raciocínio por trás das grandes escolhas. Um site de documentação publicado é construído automaticamente a cada integração. As pessoas engenheiras novas ficam produtivas rápido porque os guias de integração e os runbooks estão atuais e localizáveis, e as pessoas de sobreaviso se apoiam nos runbooks em vez de acionar os autores originais.

**Governo.** Uma agência nacional herda um sistema de um terceirizado que sai, dependendo inteiramente da documentação para levar o conhecimento através da fronteira contratual. Como o fornecedor anterior manteve documentação de arquitetura, runbooks e registros de decisão como entregáveis obrigatórios, a nova equipe consegue operar e modificar o sistema sem os autores originais. Onde a documentação era rasa, a agência enfrenta uma engenharia reversa cara. Essa experiência impulsiona uma nova política: a documentação é um entregável contratual, revisado quanto à precisão e não tratado como reflexão tardia, e os runbooks devem permitir que qualquer operador autorizado responda a incidentes.

## Justificativa de negócio: motivações, ROI e TCO

A documentação se paga em tempo de integração mais curto, menos risco de dependência de pessoas-chave, resposta a incidentes mais rápida e menor custo de mudança ao longo da vida de um sistema. Engenheiros novos chegando à produtividade em dias e não em semanas, pessoas de sobreaviso resolvendo incidentes por um runbook em vez de escalar, mantenedores mudando um sistema com confiança anos depois de construído: são economias grandes e recorrentes que se acumulam numa grande organização e numa longa vida do sistema.

Quanto custa documentar? Esforço de redação e de manutenção. Quanto custa *não* documentar? Você paga continuamente: em integração lenta, perguntas repetidas, gargalos de pessoas-chave, recuperação de incidentes mais lenta e, no extremo, sistemas que ninguém consegue alterar com segurança, forçando reescritas ou engenharias reversas caras. Em cenários de transição de fornecedor e de auditoria, a documentação ausente pode trazer custos contratuais e de conformidade diretos. Para defender o caso junto à liderança, ponha números no tempo de integração, no tempo de resposta a incidentes e em quanto conhecimento crítico está nas cabeças individuais. Depois apresente docs como código e a geração como formas de obter documentação durável sem um fardo de manutenção equivalente. E enfatize que a documentação imprecisa é um passivo, então o investimento precisa incluir mantê-la atual.

## Antipadrões e armadilhas

- **Documentação obsoleta apresentada como atual:** engana os leitores e destrói a confiança em toda a documentação.
- **A wiki de escrita única:** páginas criadas e nunca atualizadas, afastando-se em silêncio da realidade.
- **Fragmentação da documentação:** conhecimento espalhado por muitas ferramentas e wikis, de modo que nada se encontra.
- **Mistura de tipos de documentação:** tutoriais, referência e explicação embaralhados numa página, sem servir bem a nenhum leitor.
- **Manter à mão conteúdo gerável:** documentação de API escrita manualmente que inevitavelmente diverge da interface real.
- **Conhecimento tribal:** entendimento crítico guardado apenas nas cabeças das pessoas e no histórico de chat, perdido quando elas saem.
- **Documentação como reflexão tardia:** escrita no fim, se tanto, em vez de junto com a mudança.
- **Sem responsável:** documentos sem responsável apodrecem porque atualizá-los não é tarefa de ninguém.

## Modelo de maturidade

- **Nível 1, Iniciar.** A documentação é escassa, dispersa e obsoleta, e o conhecimento vive nas cabeças das pessoas. O que existe foi escrito uma vez e nunca mais tocado, então uma queda de serviço ou uma saída significa fazer engenharia reversa do sistema.
- **Nível 2, Desenvolver.** Existem documentos essenciais, como READMEs e alguns runbooks, mas são mantidos de forma inconsistente e difíceis de achar. Algumas equipes documentam bem e outras mal, e não há expectativa compartilhada sobre o que um repositório deve conter nem onde deve viver.
- **Nível 3, Padronizar.** Docs como código é a norma em toda a organização: uma estrutura comum como a Diátaxis, referências de API e registros de mudanças gerados, registros de decisão e a expectativa, na revisão, de que a documentação mude junto com o código que descreve. Todo documento de alto valor tem um responsável nomeado, e há um lar conhecido com busca de verdade.
- **Nível 4, Gerenciar.** A documentação é medida, não apenas presente. Você acompanha a cobertura dos documentos essenciais, a taxa de mudança de documentação em relação à taxa de mudança de código, o tempo de integração, a resolução de incidentes só com runbooks e a atualidade em relação a um limite definido de obsolescência, e revisa essas métricas em relação a linhas de base. O apodrecimento é pego mecanicamente por geração, testes contra o sistema e verificações de links e de precisão, e as páginas obsoletas são sinalizadas ou podadas com base em evidências e não por acaso.
- **Nível 5, Orquestrar.** A documentação é continuamente melhorada e integrada em toda a organização: viva, em grande parte gerada ou testada contra o sistema, com responsável, localizável e adaptativa. As métricas realimentam onde você investe, o conhecimento tácito é capturado como parte rotineira do trabalho e o acervo é ativamente reequilibrado e podado conforme os sistemas, as equipes e os leitores mudam.

## Ideias para discussão

- Que documentação, se sumisse amanhã, mais prejudicaria a sua organização, e ela existe hoje e se mantém atual?
- Como você faz de atualizar a documentação uma parte natural de mudar o código em vez de uma tarefa separada?
- Onde você pode substituir a documentação escrita à mão por documentação gerada, ligada à fonte da verdade?
- Como você mede se a sua documentação é precisa e usada, e não apenas presente?
- Como os assistentes de IA devem mudar a forma como você escreve, mantém e busca a documentação, e onde podem introduzir conteúdo plausível mas errado?
- Como você captura o conhecimento tácito antes que as pessoas que o detêm saiam?

## Principais conclusões

- Trate a documentação como código: versionada, revisada, perto da fonte e publicada automaticamente.
- Estruture o conteúdo pela necessidade do leitor, com tutoriais, guias práticos, referência e explicação.
- Mantenha os essenciais de alto valor: READMEs, runbooks, documentos de arquitetura, integração e registros de decisão.
- Gere a documentação de API e os registros de mudanças para que não possam se afastar da fonte da verdade.
- Combata o apodrecimento com responsabilidade, expectativas de revisão e poda. A documentação imprecisa é pior que nenhuma.

## Referências e leitura complementar

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
