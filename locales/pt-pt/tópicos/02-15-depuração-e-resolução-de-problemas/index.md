# 2.15 Depuração e resolução de problemas

## Visão geral e motivação

Depurar é o trabalho disciplinado de descobrir por que um sistema faz algo que não deveria, e resolver problemas (troubleshooting) é a mesma habilidade voltada a um sistema de produção em execução sob pressão de tempo. Ambos são o [método científico](https://en.wikipedia.org/wiki/Scientific_method) aplicado a defeitos: você observa um comportamento surpreendente, formula uma hipótese sobre sua causa, desenha um experimento que a confirmaria ou refutaria e deixa que a evidência, e não o seu palpite, diga o que mudar. Feita assim, a depuração é uma habilidade de engenharia que se aprende e se ensina. Feita como folclore, vira superstição: mudar linhas ao acaso, reiniciar servidores e torcer.

Para uma equipe grande, a diferença é cara. Um único defeito difícil pode puxar engenheiros de vários serviços, consumir horas de sobreaviso e travar um lançamento. Quando cada pessoa depura por instinto, esse esforço não se acumula, porque ninguém consegue reproduzir nem explicar o que as outras tentaram. Quando a equipe compartilha um método (reproduzir primeiro, isolar por busca, capturar o bug num teste que falha, depois corrigir), o mesmo esforço se transforma num processo repetível e numa suíte de regressão crescente. A depuração se liga estreitamente à estratégia de testes (capítulo 2.4), à qualidade de software (capítulo 2.11) e aos hábitos de construção (capítulo 2.9) que tornam o código diagnosticável desde o início.

Em contextos corporativos e governamentais, o que está em jogo sobe. Os defeitos corporativos cruzam fronteiras de serviços e de equipes, então quem vê o sintoma raramente é quem é dono da causa. Os sistemas governamentais acrescentam restrições que a maioria dos engenheiros nunca encontra: ambientes isolados da rede ou restritos em que você não pode anexar um depurador à produção, builds reproduzíveis que precisam ser diagnosticados a partir de artefatos e trilhas de auditoria que precisam registrar o que você mudou e por quê. Nos três, o objetivo é o mesmo: substituir o palpite por evidência.

## Princípios fundamentais

- **Reproduza antes de teorizar.** Um bug que você não consegue disparar sob demanda é um boato, não um defeito.
- **Depurar é testar hipóteses.** Declare o que você acredita e depois desenhe o experimento mais barato que poderia provar que você está errado.
- **Leia primeiro o erro e o rastreamento de pilha.** O sistema costuma dizer onde quebrou antes de você mudar uma linha.
- **Busque no espaço do problema, não o percorra.** Divida ao meio a região suspeita a cada passo em vez de ler de cima a baixo.
- **Reduza ao mínimo.** Despoje o caso até restar apenas o gatilho essencial.
- **Uma mudança por vez.** Edições a esmo destroem a evidência que teria dito qual mudança importou.
- **Capture o bug num teste que falha antes de corrigir.** A correção só está provada quando esse teste fica verde e permanece verde.
- **Encontre a causa-raiz, não o sintoma mais próximo.** Um remendo que esconde o sintoma deixa o defeito voltar.

## Recomendações

### Reproduza o defeito de forma confiável antes de mudar qualquer coisa

Sua primeira tarefa é uma reprodução confiável: um conjunto de passos ou um caso automatizado que dispare o bug sob demanda. Sem ela, você não consegue distinguir uma correção real de uma coincidência, porque o sintoma pode ir e vir por razões que você nunca controlou. Fixe as entradas, o ambiente, as versões e o tempo. Se o bug é intermitente, cace a variável oculta que o faz aparecer (um registro de dados específico, uma fronteira de relógio, uma requisição concorrente) até a reprodução ficar confiável. Uma reprodução confiável é o artefato mais valioso da depuração, porque tudo que vem depois se torna mensurável.

### Leia o erro, os logs e o rastreamento de pilha antes de tocar no código

Antes de formar uma única teoria, leia o que o sistema já lhe disse. O [rastreamento de pilha](https://en.wikipedia.org/wiki/Stack_trace) (o registro da cadeia de chamadas no momento da falha) costuma nomear o arquivo, a linha e a sequência que falhou. A mensagem da exceção, as linhas de log ao redor e os valores no escopo estreitam a busca antes de você ter mudado qualquer coisa. Os engenheiros desperdiçam horas teorizando sobre causas que o rastreamento já descartou na primeira linha. Trate a saída de erro como a primeira testemunha, leia-a com cuidado e por inteiro e só então decida o que investigar.

### Isole por busca binária do espaço do problema

Não percorra o código de cima a baixo. Busque nele. Use a [busca binária](https://en.wikipedia.org/wiki/Binary_search_algorithm): encontre um ponto em que o estado ainda está bom e um ponto em que já está ruim, depois verifique o ponto médio e repita, dividindo ao meio a região suspeita a cada vez. Isso transforma uma busca de mil linhas em dez perguntas. Quando a regressão apareceu ao longo de uma faixa de commits, aplique a mesma ideia ao histórico com a bisseção: o `git bisect` percorre a faixa de commits e você marca cada revisão como boa ou ruim até ele nomear a mudança exata que introduziu o defeito. Automatize o teste de bom ou ruim e a bisseção roda sozinha.

### Reduza a um exemplo mínimo reproduzível

Quando você consegue disparar o bug, encolha-o. Um [exemplo mínimo reproduzível](https://en.wikipedia.org/wiki/Minimal_reproducible_example) é a menor entrada e o menor caminho de código que ainda falha: remova dados, funcionalidades e passos até qualquer remoção adicional fazer o bug sumir. A redução não é trabalho inútil. Cada elemento que você elimina é uma causa que você descartou, então o caso mínimo muitas vezes aponta direto para o defeito. Quando a entrada é grande ou estruturada, automatize o encolhimento com a [depuração delta](https://en.wikipedia.org/wiki/Delta_debugging), um algoritmo que remove sistematicamente pedaços de uma entrada que falha para encontrar o subconjunto mínimo que falha. Uma reprodução pequena e autocontida é também o melhor relato de bug possível para entregar a outra equipe.

### Instrumente com logs e depois use um depurador interativo

Ajuste a ferramenta ao bug. Os logs e a instrumentação direcionada são melhores quando você precisa ver o comportamento ao longo do tempo, entre processos ou num ambiente que você não consegue pausar. Um depurador interativo, que permite definir pontos de interrupção, avançar linha a linha e inspecionar o estado ao vivo, é melhor quando você consegue rodar o código localmente e precisa observar de perto uma única execução. Acrescente a instrumentação como um experimento deliberado ligado a uma hipótese, e não como instruções de impressão espalhadas, e remova-a ou promova-a a log estruturado permanente quando o bug estiver resolvido. Em produção, apoie-se na depuração guiada por observabilidade: eventos de alta cardinalidade e rastreamento distribuído (capítulo 9.2) permitem seguir uma requisição por vários serviços, o que muitas vezes é a única forma de depurar um sistema distribuído ao qual você não consegue anexar um depurador.

### Escreva um teste que falha e captura o bug antes de corrigi-lo

Antes de escrever a correção, escreva um teste que falhe por causa do bug. Isso faz três coisas ao mesmo tempo: prova que você de fato entende a causa, define exatamente o que significa “corrigido” e se torna uma proteção permanente. Depois faça a correção e veja o teste ficar verde. Esse teste agora se junta à sua suíte como uma proteção de [teste de regressão](https://en.wikipedia.org/wiki/Regression_testing), de modo que o mesmo defeito não possa voltar sem ser notado. Essa prática liga a depuração diretamente à sua estratégia de testes (capítulo 2.4): todo bug difícil que você resolve deixa a suíte mais forte do que a encontrou, e um teste instável recebe o mesmo tratamento (reproduzir o não determinismo e depois proteger contra ele) em vez de uma anotação de nova tentativa.

### Encontre a causa-raiz e mantenha a análise sem atribuição de culpa

Corrigir o sintoma não é corrigir o bug. Rastreie a falha até a origem verdadeira, perguntando por quê em cada camada até chegar a uma causa que você pode remover em vez de mascarar. Para defeitos que chegaram à produção, conduza uma análise de causa-raiz sem atribuição de culpa como parte da gestão de incidentes (capítulo 9.3): concentre-se nas condições do sistema e do processo que deixaram o bug ser entregue e sobreviver, nunca na pessoa que escreveu a linha. A culpa empurra a informação para a clandestinidade, e a depuração funciona com informação. O resultado é tanto uma correção quanto uma mudança em como a classe do defeito é pega mais cedo da próxima vez.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Logs e instrumentação | Funcionam em produção e em sistemas distribuídos. Captam o comportamento ao longo do tempo | Ruído, custo e proliferação de logs. Podem perturbar bugs de temporização |
| Depurador interativo | Inspeção precisa do estado ao vivo. Rápido para bugs locais | Inútil em produção restrita ou isolada da rede. Pode esconder bugs de concorrência |
| Disciplina de reproduzir primeiro | Transforma palpite em medição. Viabiliza um teste que falha | Lenta no início. Alguns bugs são genuinamente difíceis de disparar |
| Busca binária e bisseção | Isolamento rápido, mesmo em código desconhecido | Precisa de um teste confiável de bom ou ruim. Difícil quando os bugs interagem |
| Redução por depuração delta | Encolhe entradas enormes automaticamente até o gatilho | Custo de preparação. Pressupõe que a falha é determinística |
| Corrigir o sintoma agora | Restaura o serviço rápido sob pressão | Deixa a causa-raiz voltar. Acumula dívida |

A tensão central é velocidade versus certeza. Durante um incidente de produção, você pode precisar estancar o sangramento primeiro (um rollback ou um remendo de sintoma) para restaurar o serviço, e isso é legítimo. O erro é parar aí. Resolva a tensão separando os dois trabalhos: mitigue rápido para proteger os usuários e depois reproduza, encontre a causa-raiz e acrescente a proteção de regressão antes de considerar o defeito encerrado. Uma correção de sintoma sem acompanhamento é um bug que você concordou em reencontrar.

## Perguntas para discutir com sua equipe

1. **Quando alguém enfrenta um bug difícil, qual é a primeira coisa que faz, e é reproduzir ou adivinhar?** A resposta honesta revela se a sua equipe tem um método compartilhado ou uma sala cheia de folclore privado. Peça às pessoas que narrem em voz alta o último defeito difícil: conseguiram primeiro uma reprodução confiável, ou começaram a mudar código e a reiniciar coisas? Uma equipe que reproduz primeiro consegue passar um bug de mão em mão, porque a reprodução viaja. Uma equipe que adivinha não consegue, porque cada tentativa é irrepetível. Isso importa mais à medida que a equipe cresce, já que quem vê um sintoma é cada vez menos quem consegue corrigi-lo. Se o padrão é adivinhar, combinem a reprodução primeiro como norma e façam de uma reprodução limpa o preço de entrada para um tíquete de bug.

2. **Os bugs que corrigimos voltam, e saberíamos se voltassem?** Um defeito que retorna é um defeito cuja causa-raiz nunca foi removida e cuja correção nunca foi protegida por um teste. Pegue o último trimestre de incidentes e tíquetes reabertos e conte quantos foram repetições ou primos de bugs anteriores. Cada repetição é evidência de que a equipe remendou um sintoma, pulou o teste que falha ou parou a análise de causa-raiz cedo demais. A correção é uma regra: nenhum bug é encerrado até que um teste que falha com o comportamento antigo passe com o novo e se junte à suíte. Leve um bug recente que se repete e pergunte que proteção o teria pegado, porque essa proteção é o que faltava.

3. **Conseguimos depurar os nossos sistemas de produção, dada a forma como temos permissão para tocá-los?** Em ambientes corporativos e especialmente governamentais, muitas vezes você não pode anexar um depurador, não pode reproduzir com dados reais e não pode mudar um sistema em execução sem uma trilha de auditoria. Se a sua única técnica de depuração é um depurador interativo local, você está cego exatamente onde moram os bugs mais difíceis. Pergunte que evidência uma falha de produção de fato deixa para trás: logs estruturados, rastreamentos distribuídos (capítulo 9.2), despejos de memória ou artefatos de build reproduzíveis. Decidam agora o que precisam capturar por padrão para que um incidente futuro seja diagnosticável, porque você não pode acrescentar instrumentação a uma falha que já aconteceu. Em contextos regulamentados, confirme que a mesma trilha também satisfaz suas obrigações de auditoria.

4. **Quando um incidente de produção nos obriga a estancar o sangramento rápido, como garantimos que a causa-raiz ainda seja encontrada depois?** Durante um incidente, um rollback ou um remendo de sintoma é a jogada inicial certa para proteger os usuários, mas o perigo é o tíquete se fechar no momento em que o serviço volta e o defeito subjacente nunca ser diagnosticado. Para uma equipe grande é aqui que a dívida se acumula de forma invisível, porque a mesma classe de falha ressurge em outro serviço e com outra pessoa de sobreaviso meses depois. Leve seus últimos incidentes de severidade um e verifique cada um: uma reprodução, uma análise de causa-raiz e uma proteção de regressão seguiram a mitigação, ou a história terminou em “serviço restaurado”? Combinem uma regra explícita de que um incidente mitigado continua aberto até a causa-raiz ser entendida e protegida e nomeiem quem é dono desse acompanhamento. Em contextos corporativos e governamentais, ligue isso ao seu processo de gestão de incidentes (capítulo 9.3) para que a revisão pós-incidente seja uma etapa exigida e auditável e não uma cortesia que escorrega quando o próximo incêndio começa.

5. **Quanto de uma falha conseguimos reconstruir depois do fato, e quem decidiu o que capturamos por padrão?** Você não consegue anexar instrumentação a uma falha que já aconteceu, então a diagnosticabilidade de qualquer incidente é fixada de antemão pelos logs, rastreamentos, métricas e despejos que você escolheu emitir. A consideração concorrente é o custo e o ruído: eventos de alta cardinalidade e rastreamento completo não são de graça, e o excesso de logs enterra o sinal ao mesmo tempo que infla o armazenamento e, em contextos regulamentados, a sua exposição de retenção de dados. Leve um incidente real recente e pergunte que evidência ele deixou, depois trabalhe para trás até o que vocês gostariam de ter capturado e quanto custaria guardar. Decidam deliberadamente quais sinais ficam ligados por padrão e quais são amostrados ou opcionais e registrem essa decisão para que seja uma política e não um acidente. Para um sistema corporativo ou governamental, acrescente quem é responsável por esse orçamento de observabilidade e se a trilha capturada também satisfaz as obrigações de auditoria, de privacidade e de residência de dados.

6. **Tratamos a depuração como uma habilidade ensinada e mensurável, ou as pessoas novas a absorvem por osmose?** A depuração se aprende, mas a maioria das equipes nunca a ensina explicitamente, então os juniores herdam o folclore que estiver mais perto, e o método de reproduzir primeiro se espalha de forma desigual ou nem se espalha. A tensão é que o ensino deliberado (parear em bugs difíceis, escrever as constatações pós-incidente, acompanhar métricas) custa tempo sênior que sempre parece necessário em outro lugar. Leve dois números à discussão: a sua taxa de defeitos repetidos e o seu tempo até o diagnóstico, porque, se você não consegue medi-los, não consegue dizer se o seu método está melhorando ou decaindo. Considere se a integração inclui um exercício real de depuração e se as constatações de causa-raiz de fato alimentam uma detecção mais precoce. Numa organização grande ou pública, uma prática de depuração documentada e medida também se torna evidência de rigor de engenharia que auditores, reguladores e órgãos de supervisão esperam cada vez mais ver.

## Perspectiva por setor

**Startup.** Com um punhado de engenheiros e nenhuma folga, o seu objetivo é tornar os bugs baratos de reproduzir e impossíveis de esquecer, não construir processo pesado. Apoie-se no `git bisect`, numa reprodução local rápida e num teste que falha por bug corrigido, porque esse hábito custa minutos e impede que você pague de novo pelo mesmo defeito enquanto tenta entregar. Pule os postmortems formais, mas nunca pule o teste de regressão: é o único artefato pequeno o bastante para sempre caber no bolso e valioso o bastante para sempre ser guardado.

**Pequena empresa.** Provavelmente você não tem especialista dedicado em confiabilidade ou observabilidade e tem um orçamento apertado de ferramentas, então favoreça o que a sua pilha já oferece: rastreamentos de pilha legíveis, logs estruturados e o rastreamento embutido nos frameworks e serviços hospedados que você comprou. Ao avaliar uma nova plataforma, pese quão diagnosticáveis ela torna as falhas, porque uma ferramenta barata que esconde o que deu errado custa muito mais em tempo de adivinhação do que a licença economizou. Reproduzir primeiro e uma mudança por vez são disciplinas gratuitas que compensam mais rápido quando ninguém tem horas sobrando.

**Grande empresa.** Seus bugs difíceis cruzam fronteiras de serviços e de equipes, então quem vê o sintoma raramente é dono da causa, e um método compartilhado importa mais que a habilidade de qualquer indivíduo. Padronize a reprodução primeiro, o isolamento por busca binária, um teste que falha antes da correção e os postmortems sem atribuição de culpa entre as equipes e invista em rastreamento distribuído (capítulo 9.2) para que uma só requisição possa ser seguida por vários serviços. Gerencie a depuração como uma capacidade medida: acompanhe a taxa de defeitos repetidos e o tempo até o diagnóstico e realimente as constatações de causa-raiz na detecção mais precoce para que a mesma classe de falha não percorra o seu mapa de serviços.

**Governo.** As regras de contratação, os ambientes restritos e a responsabilização pública moldam como você pode depurar. Muitas vezes não é possível anexar um depurador à produção nem copiar dados de cidadãos para um laptop, então projete o diagnóstico a partir do que é permitido: builds reproduzíveis, registros sintéticos num enclave isolado e logs estruturados e rastreamentos capturados por padrão. Registre cada passo de diagnóstico e cada mudança na trilha de auditoria e exija que os fornecedores exponham telemetria e reprodutibilidade de build suficientes para você investigar as falhas de forma independente em vez de depender da palavra do fornecedor.

## Exemplos

**Startup.** Uma equipe de quatro engenheiros vê o pagamento falhar para uma fração dos usuários, mas nunca nos testes. Em vez de adivinhar, uma pessoa captura uma reprodução confiável reexecutando a carga útil exata da requisição que falha e depois lê o rastreamento de pilha que vinha ignorando, que aponta para uma chamada de análise de datas. Um rápido `git bisect` nos commits da semana nomeia a mudança que trocou uma biblioteca de datas. Eles escrevem um teste que falha com o carimbo de data e hora ofensor, corrigem o analisador, veem o teste ficar verde e o mantêm na suíte. A investigação inteira leva uma tarde porque reproduziram antes de teorizar, e o bug nunca volta.

**Grande empresa.** Uma plataforma de pagamentos vê tempos esgotados intermitentes que nenhuma equipe isolada consegue explicar, porque o sintoma aparece no pagamento mas a causa mora a três serviços de distância. As pessoas de sobreaviso usam o rastreamento distribuído (capítulo 9.2) para seguir uma requisição que falha por fronteiras de serviço e encontram uma chamada a jusante que ocasionalmente trava sob carga concorrente, uma clássica [condição de corrida](https://en.wikipedia.org/wiki/Race_condition) em que o resultado depende de uma temporização azarada entre threads. Elas a reproduzem com um teste de carga, capturam-na num teste de integração que falha, corrigem o bloqueio e conduzem um postmortem sem atribuição de culpa (capítulo 9.3) que acrescenta um intervalo de rastreamento e um alerta para que a próxima ocorrência seja pega em minutos e não em dias.

**Governo.** Uma agência de benefícios opera seu sistema de casos num ambiente isolado da rede, onde os engenheiros não podem anexar um depurador à produção nem copiar dados de cidadãos para seus laptops. Um defeito de cálculo surge na conciliação. A equipe depura a partir do que o ambiente permite: logs estruturados, um build reproduzível que consegue montar num enclave de teste isolado e registros sintéticos que recriam o caso que falha. Cada passo de diagnóstico é registrado na trilha de auditoria, a correção é entregue com um teste que falha e depois passa como evidência e a análise de causa-raiz alimenta uma nova verificação pré-lançamento. Como a reprodução usou dados sintéticos, nenhum registro de cidadão saiu da fronteira.

## Justificativa de negócio: motivações, ROI e TCO

O retorno da depuração disciplinada se mede em horas de engenharia não gastas adivinhando e em defeitos que não se repetem. Um bug intermitente não diagnosticado pode consumir dias de tempo sênior e repetidas escaladas de sobreaviso. Um método de reproduzir primeiro transforma isso numa tarefa limitada e delegável, e o hábito do teste que falha impede que o mesmo defeito cobre de você de novo no próximo trimestre. Numa grande organização, o efeito cumulativo de nunca pagar de novo pelo mesmo bug é substancial e melhora diretamente a taxa de falha de mudanças e o tempo médio de recuperação que a liderança já acompanha.

O custo total de propriedade é principalmente treinamento e ferramentas, e é modesto. Você precisa de convenções compartilhadas (reproduzir primeiro, uma mudança por vez, um teste que falha antes da correção), depuradores e rastreamento já comuns na cadeia de ferramentas e do investimento em observabilidade descrito no capítulo 9.2. O custo maior e oculto é a alternativa: uma cultura de superstição em que os engenheiros aplicam mudanças a esmo, os sintomas são remendados e voltam e a carga de sobreaviso cresce sem limite. Só reduzir o trabalho repetitivo de sobreaviso muitas vezes já justifica o investimento, e o argumento à liderança fica mais simples assim: menos incidentes repetidos e recuperação mais rápida por um custo único em hábitos e instrumentação.

## Antipadrões e armadilhas

- **Depuração a esmo:** mudar muitas coisas de uma vez, de modo que até uma correção não ensina nada sobre a causa.
- **Corrigir sem reproduzir:** declarar vitória num bug que você nunca conseguiu disparar sob demanda.
- **Ignorar a saída de erro:** teorizar sobre causas que o rastreamento de pilha já descartou.
- **Remendar sintomas:** silenciar o sintoma enquanto a causa-raiz sobrevive para voltar.
- **Proliferação de instruções de impressão:** saída de depuração espalhada deixada no código, acrescentando ruído em vez de um experimento ligado a uma hipótese.
- **Pular o teste de regressão:** corrigir o bug mas não deixar proteção, de modo que ele possa voltar em silêncio.
- **Repetir testes instáveis:** esconder o não determinismo com novas tentativas em vez de depurar a condição de corrida subjacente ou o [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), um bug que muda ou some no momento em que você tenta observá-lo.
- **Postmortems movidos a culpa:** punir o autor, o que empurra para a clandestinidade a informação de que a depuração depende.

## Modelo de maturidade

- **Nível 1, Iniciar:** A depuração é folclore individual e reação. Os engenheiros adivinham, aplicam mudanças a esmo e reiniciam coisas. Os bugs são corrigidos no sintoma, as reproduções são raras e os mesmos defeitos recorrem. A produção mal é diagnosticável, e ninguém consegue passar um bug a outra pessoa porque nenhuma tentativa é repetível.
- **Nível 2, Desenvolver:** Alguns engenheiros reproduzem de forma confiável, leem rastreamentos de pilha e usam depuradores, mas a prática é inconsistente e varia de pessoa para pessoa e de equipe para equipe. Os logs existem mas são ruidosos e não estruturados. As correções às vezes saem com um teste que falha, muitas vezes não, e a análise de causa-raiz só acontece quando alguém insiste.
- **Nível 3, Padronizar:** Reproduzir primeiro, o isolamento por busca binária, uma mudança por vez e um teste que falha antes da correção são normas de equipe documentadas e impostas em toda a organização. A bisseção e a redução por depuração delta são prática comum. A produção tem logs estruturados e rastreamento (capítulo 9.2), e os postmortems sem atribuição de culpa (capítulo 9.3) são a resposta padrão a todo defeito que escapou.
- **Nível 4, Gerenciar:** A prática de depuração é medida e controlada em relação a linhas de base. A taxa de defeitos repetidos, o tempo até o diagnóstico, a contagem de tíquetes reabertos e a parcela de correções entregues com um teste de regressão são acompanhados por equipe e revisados numa cadência. A reprodução e a conclusão da causa-raiz são tratadas como portões e não como boas intenções, e as tendências em relação à linha de base orientam onde investir em ferramentas, treinamento e observabilidade.
- **Nível 5, Orquestrar:** A depuração é uma habilidade ensinada, integrada à qualidade (capítulo 2.11) e à gestão de incidentes (capítulo 9.3), e todo o ciclo se adapta continuamente. A observabilidade é projetada de modo que a maioria dos bugs de produção seja diagnosticável sem depurador, cada bug resolvido fortalece a suíte de regressão e as constatações de causa-raiz alimentam a detecção mais precoce, de modo que classes de defeito são prevenidas e não rediagnosticadas. A organização reequilibra o esforço conforme seus sistemas e modos de falha evoluem, e a taxa de defeitos repetidos continua caindo.

## Ideias para discussão

1. Que fração dos seus bugs recentes foi reproduzida de forma confiável antes de alguém mudar código, e o que essa fração diz sobre o seu método?
2. Quando aparece uma regressão, a sua equipe recorre à bisseção ou lê o código à mão até alguém perceber?
3. Quão diagnosticável é o seu sistema de produção hoje, e o que você daria para ter capturado sobre uma falha que já aconteceu?
4. As suas correções consistentemente saem com um teste que falha e depois passa e, se não, onde essa disciplina se quebra?
5. Como vocês tratam os testes instáveis: depuram o não determinismo ou o encobrem com novas tentativas?
6. A depuração é ensinada deliberadamente às pessoas engenheiras novas, ou elas são deixadas para absorver o folclore por osmose?

## Principais conclusões

- Depurar é testar hipóteses: reproduza de forma confiável, leia o erro e o rastreamento de pilha e depois isole por busca binária e bisseção em vez de percorrer.
- Reduza a falha a um exemplo mínimo reproduzível, usando a depuração delta para entradas grandes, porque cada elemento removido é uma causa descartada.
- Ajuste a ferramenta ao bug: instrumentação e rastreamento para produção e sistemas distribuídos (capítulo 9.2), depuradores interativos para a investigação local.
- Escreva um teste que falha e captura o bug antes de corrigi-lo, para que a correção seja provada e o defeito fique protegido de vez (capítulo 2.4).
- Encontre e remova a causa-raiz, conduza postmortems sem atribuição de culpa (capítulo 9.3) e trate a depuração como uma habilidade que se aprende, não como folclore.
- Mude uma coisa por vez. Mudanças a esmo e remendos de sintoma destroem a evidência e convidam o bug a voltar.

## Referências e leitura complementar

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller and Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (the delta debugging algorithm)
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (chapter on debugging)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (the chapters on debugging and assertions)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (the debugging chapter)
- John Regehr, "Reducers Are Fuzzers" and related writing on test-case reduction
- Charity Majors, Liz Fong-Jones, and George Miranda, *Observability Engineering* (debugging production with high-cardinality telemetry and tracing)
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (blameless postmortems and production debugging)
