# 8.5 Automação de testes e de processos

## Visão geral e motivação

A automação de testes e de processos é a prática de substituir o trabalho repetitivo, manual, de engenharia e de operações por fluxos de trabalho confiáveis, executados por máquina. Do lado dos testes, isso significa a [automação de testes](https://en.wikipedia.org/wiki/Test_automation): suítes automatizadas de testes que rodam continuamente para verificar correção, desempenho e segurança. Do lado dos processos, estende-se à maquinaria que cerca a entrega e a operação de software: coletar evidências de conformidade, executar runbooks operacionais, remediar problemas conhecidos e impor controles de governança, de segurança e de custo. A ideia unificadora é simples. Tudo que é feito de modo repetido e previsível deve ser codificado, para rodar de forma consistente, rápida e sem trabalho repetitivo (toil) humano.

Para grandes equipes, a automação é o único modo de impedir que a qualidade e o controle desabem sob a escala. O teste manual não acompanha centenas de engenheiros fazendo milhares de mudanças. Vira um gargalo, e sua cobertura fica inconsistente e pouco confiável. Os procedimentos operacionais manuais também sofrem. Reiniciar um serviço, rotacionar uma credencial e reunir evidências de auditoria ficam todos lentos e sujeitos a erros quando humanos cansados os fazem sob pressão em um grande patrimônio. Automatizar esse trabalho torna os resultados repetíveis. Também libera engenheiros qualificados para os problemas que exigem julgamento e que genuinamente precisam de percepção humana.

Em contextos corporativos e governamentais, a automação também é a chave para tornar a conformidade sustentável. As organizações reguladas precisam demonstrar continuamente que os controles estão em vigor e que as evidências são coletadas. Fazer isso à mão é caro, lento e sujeito a lacunas. Automatizar a coleta de evidências e a imposição de controles transforma a conformidade de um alarme de incêndio periódico em uma propriedade contínua e verificável do sistema. Essa abordagem de “conformidade como código” reduz o custo e reforça a garantia que auditores e reguladores exigem.

## Princípios fundamentais

- Automatizem o trabalho repetido, previsível e baseado em regras. Reservem o esforço humano para o julgamento.
- Tornem os testes automatizados rápidos, confiáveis e determinísticos, ou serão ignorados.
- Rodem os testes em paralelo e desloquem-nos para mais cedo para que o retorno continue rápido à medida que a suíte cresce.
- Codifiquem os procedimentos operacionais como [runbooks](https://en.wikipedia.org/wiki/Runbook) como código, para que sejam versionados, testáveis e executáveis.
- Prefiram uma automação bem integrada a scripts frágeis que se prendem aos sistemas por fora.
- Gerem a evidência de conformidade automaticamente como subproduto dos fluxos de trabalho normais.
- Mantenham um humano no circuito para as ações de alto risco. Automatizem primeiro o seguro e o rotineiro.

## Recomendações

### Construa uma infraestrutura de testes rápida, confiável e paralela

Uma suíte de testes só tem valor se os engenheiros confiam nela e se ela devolve retorno depressa. Invistam numa infraestrutura de testes que rode as suítes em paralelo em muitos workers, para que o tempo total de relógio permaneça baixo mesmo quando o número de testes cresce para milhares. Estruturem a suíte como uma pirâmide: muitos [testes de unidade](https://en.wikipedia.org/wiki/Unit_testing) rápidos, menos testes de integração e um pequeno número de testes de ponta a ponta. Assim a maior parte do retorno chega em segundos. Eliminem sem piedade os testes instáveis (flaky). Um teste que falha de forma intermitente é pior que nenhum teste, porque treina os engenheiros a ignorar falhas. Ofereçam ambientes de teste efêmeros e sob demanda para que os testes de integração e de ponta a ponta rodem contra uma infraestrutura realista e isolada.

### Automatize o lançamento, a conformidade e a coleta de evidências

Estendam a automação além do teste, até o fluxo de lançamento e de conformidade. Façam o pipeline produzir automaticamente os artefatos de que os auditores precisam: registros de quem aprovou uma mudança, que testes rodaram e passaram, o que as varreduras de segurança acharam e exatamente qual artefato foi implantado. Tratem os controles como código, para que as verificações exigidas sejam impostas de modo uniforme e seus resultados registrados. Essa “conformidade como código” transforma a coleta de evidências de uma correria manual antes de uma auditoria em um registro contínuo e sempre atual. Também torna observável a qualquer momento a postura de conformidade do sistema.

### Adote o ChatOps e os runbooks como código

Codifiquem os procedimentos operacionais como runbooks executáveis guardados em controle de versões, em vez de documentos em prosa que ficam desatualizados. Onde um procedimento é seguro e bem compreendido, liguem-no a uma automação que possa rodá-lo sob demanda. O ChatOps traz essas operações para uma interface de bate-papo compartilhada, de modo que os operadores disparam e observam ações automatizadas numa conversa transparente, colaborativa e registrada. Isso torna as operações visíveis a toda a equipe e cria um registro automático do que foi feito. Também reduz a barreira para que engenheiros menos experientes rodem procedimentos com segurança, porque a automação codifica os passos corretos.

### Implemente a remediação automatizada com cuidado

Para problemas recorrentes e bem compreendidos, construam uma remediação automatizada que detecte uma condição e aplique uma correção conhecida, como reiniciar um processo que falhou, escalar sob carga, limpar um disco cheio ou fazer o failover de um componente. Comecem por remediações de baixo risco e alta confiança. Exijam confirmação humana para qualquer coisa de raio de impacto significativo. A remediação automatizada reduz o tempo médio de recuperação e elimina a fadiga repetitiva de alertas. Mas precisa ser construída sobre uma detecção sólida e incluir salvaguardas, porque a automação que age sobre um sinal falso pode amplificar um incidente. Registrem toda ação automatizada, para que os operadores mantenham visibilidade total e possam intervir.

### Coloque a automação robótica de processos (RPA) no lugar certo

A [automação robótica de processos](https://en.wikipedia.org/wiki/Robotic_process_automation) conduz interfaces de usuário e aplicações existentes para automatizar tarefas, imitando os cliques e as teclas que um humano executaria. A RPA tem um lugar legítimo como ponte para sistemas legados ou de terceiros que não expõem API e não podem ser integrados de nenhum outro modo. Usem-na com pragmatismo nesses casos, mas conheçam seus limites. A automação guiada pela interface é inerentemente frágil: quebra sempre que a interface muda e não resolve a falta subjacente de integração. Onde uma API ou integração adequada está disponível, prefiram-na. Tratem a RPA como um paliativo tático, não como uma fundação estratégica, e planejem substituí-la à medida que os sistemas se modernizam.

### Automatize os controles de governança, de segurança e de custo

Codifiquem os controles organizacionais como verificações automatizadas que rodam continuamente: política como código para guardrails de infraestrutura, varredura automatizada de segurança nos pipelines e detecção automatizada de anomalias de custo e de recursos ociosos. Automatizar a governança torna os controles uniformes e impossíveis de contornar e escala a um volume de mudança que a revisão manual jamais cobriria. A mesma abordagem que impõe uma política de segurança pode sinalizar uma conta de nuvem descontrolada ou uma etiqueta obrigatória ausente. A governança passa de uma auditoria manual periódica a um guardrail automatizado contínuo.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| Testes automatizados amplos | Retorno rápido e consistente. Viabiliza a mudança | Custo de construção e manutenção. Risco de instabilidade | Todas as equipes em escala |
| Conformidade como código | Evidência contínua e pronta para auditoria | Engenharia inicial para codificar os controles | Organizações reguladas |
| Runbooks como código + ChatOps | Operações repetíveis, visíveis e registradas | Esforço para codificar e manter | Equipes com carga operacional real |
| Remediação automatizada | Recuperação mais rápida. Menos trabalho repetitivo (toil) | Risco se a detecção estiver errada | Problemas recorrentes e bem compreendidos |
| RPA (automação de interface) | Faz ponte com sistemas sem API | Frágil. Mascara lacunas de integração | Sistemas legados como paliativo |
| Governança automatizada | Controles uniformes e impossíveis de contornar | Esforço de redação e ajuste de políticas | Patrimônios grandes e governados |

O compromisso central é investimento inicial versus trabalho repetitivo (toil) e risco contínuos. A automação sempre custa esforço para construir e manter. A automação mal construída, seja de testes instáveis, de RPA frágil ou de remediação disparada por sinais ruins, pode ser pior que nenhuma, porque erode a confiança ou amplifica as falhas. A disciplina é tripla: automatizar o que é genuinamente repetível e confiável, investir em tornar essa automação digna de confiança e manter os humanos no circuito onde o julgamento ou o alto risco exigem. Bem feita, a automação se paga muitas vezes. Feita com descuido, vira um passivo por si só.

## Perguntas para discutir com sua equipe

1. **Os seus testes de integração e de ponta a ponta rodam contra ambientes realistas e efêmeros, ou contra uma máquina de staging compartilhada pela qual todos brigam?** Ambientes isolados sob demanda por pull request permitem que os testes de integração e de ponta a ponta exercitem uma infraestrutura realista sem que as equipes se bloqueiem nem poluam o estado compartilhado. Um único ambiente de staging compartilhado vira um gargalo e uma fonte de falhas instáveis e dependentes de ordem à medida que mais equipes se amontoam nele. Decidam se conseguem criar ambientes efêmeros, quanto custam e quais testes genuinamente os exigem versus um substituto rápido em memória. Levem dados: com que frequência o staging é disputado, quantas falhas se devem à interferência do ambiente compartilhado e o tempo atual de relógio do nível de integração. A resposta molda tanto a confiabilidade dos seus testes quanto a rapidez com que as camadas superiores da pirâmide devolvem retorno.

2. **Os procedimentos operacionais estão codificados como runbooks como código e expostos pelo ChatOps, ou ainda vivem como prosa que fica desatualizada?** Os runbooks codificados e versionados são testáveis e executáveis, e rodá-los por uma interface de bate-papo compartilhada torna toda ação visível e registrada automaticamente. Isso reduz a barreira para um engenheiro de sobreaviso menos experiente agir com segurança, porque a automação codifica os passos corretos em vez de depender da memória tribal. Decidam quais procedimentos são seguros e bem compreendidos o bastante para ligar primeiro e como mantêm o humano capaz de intervir. Para um grande patrimônio, essa transparência vale também como registro de auditoria de quem fez o quê e quando. Levem os runbooks atuais, anotem quais estão obsoletos e identifiquem os dois ou três procedimentos mais executados para codificar primeiro.

3. **No seu pipeline, quais varreduras de segurança e verificações de política bloqueiam um merge, e quais apenas avisam?** A governança automatizada só vale a pena construir se os controles forem impossíveis de contornar, porque uma verificação que apenas avisa é ignorada sob pressão de prazo exatamente como uma política de wiki. Decidam, controle a controle, o que bloqueia e o que avisa: uma vulnerabilidade crítica ou uma etiqueta de criptografia ausente provavelmente bloqueia, enquanto um achado de estilo de menor severidade pode avisar. Em escala, é assim que vocês impõem guardrails de segurança e de custo de modo uniforme sobre um volume de mudança que nenhuma revisão manual cobriria. Levem o inventário atual de verificações e marquem cada uma como bloqueante ou consultiva e depois discutam a taxa de falsos positivos, porque uma verificação bloqueante ruidosa treina as pessoas a exigir exceções. A linha entre bloquear e avisar é onde a sua governança tem dentes ou não tem.

4. **Quais remediações automatizadas aceitamos deixar agir sem que um humano confirme antes, e qual é o raio de impacto se a detecção estiver errada?** A remediação automatizada corta o tempo de recuperação e a fadiga de alertas, mas uma correção disparada por um sinal falso pode transformar um pequeno soluço numa interrupção total, então a decisão do que roda sem supervisão é uma decisão de risco, não de conveniência. Pesem as atrações concorrentes: a ação sem supervisão é a mais rápida, porém a mais arriscada, enquanto a confirmação com humano no circuito é mais segura mas reintroduz o atraso e o trabalho repetitivo (toil) que vocês queriam remover. Levem as remediações candidatas classificadas por frequência e pelo raio de impacto no pior caso, a taxa histórica de falsos positivos da detecção por trás de cada uma e se toda ação é registrada e reversível. Para um grande patrimônio corporativo ou governamental, acrescentem uma autoridade formal de mudança e um plano de reversão para qualquer coisa que toque dados de produção ou serviços voltados ao cidadão, porque uma autorremediação que não pode ser auditada nem desfeita é uma que um regulador vai obrigar vocês a desligar.

5. **Como financiamos e atribuímos a propriedade da manutenção da nossa automação para que ela não decaia num passivo?** Testes, runbooks, verificações de política e bots de RPA apodrecem à medida que os sistemas ao redor mudam, e a automação negligenciada é pior que nenhuma: um runbook obsoleto dá falsa confiança numa crise e um bot de RPA quebrado descarta trabalho em silêncio. A tensão é que a manutenção compete com o trabalho de funcionalidades pelos mesmos engenheiros e é invisível até algo quebrar, então é a primeira coisa cortada sob pressão de prazo. Levem o inventário atual dos ativos de automação, o acúmulo de testes instáveis e de bots quebrados e uma estimativa honesta das horas de engenheiro que já vão para a manutenção versus o que está orçado. Num contexto corporativo ou governamental, nomeiem o dono responsável de cada automação crítica e financiem sua manutenção como item de linha explícito, porque os auditores e as revisões de incidentes perguntarão quem era responsável quando um controle sem manutenção falhou em silêncio.

6. **Para cada sistema legado que automatizamos com RPA, qual é o plano concreto e o gatilho para aposentar essa RPA em favor de uma integração de verdade?** A RPA é uma ponte legítima para sistemas que não expõem API, mas uma ponte sem plano de saída endurece em silêncio e vira infraestrutura permanente e frágil que quebra a cada mudança de interface e entrincheira a própria lacuna de integração que deveria vencer. O compromisso é real: a RPA entrega valor rápido e barato agora, enquanto uma integração adequada por API custa mais de início mas é durável, então a disciplina é tratar a RPA como um empréstimo com data, não como uma compra. Levem a lista de bots de RPA em produção, os sistemas de que cada um depende, com que frequência cada um quebra e se um esforço de modernização ou de integração está de fato financiado e agendado para o sistema subjacente. Para patrimônios corporativos e governamentais que carregam aplicações centrais de décadas, liguem cada bot de RPA a um marco nomeado de modernização, porque a RPA que virou crítica em silêncio e sem data de aposentadoria é dívida técnica que se compõe a cada ano em que a interface raspada continua mudando.

## Perspectiva por setor

**Startup.** Com duas ou três pessoas na engenharia e sem tempo para construir infraestrutura, mantenham uma pirâmide de testes pequena e rápida que rode em alguns minutos a cada mudança e tratem qualquer teste instável como um bug real a corrigir ou apagar naquela semana. Pulem a ferramenta pesada de conformidade e a política como código de que vocês ainda não precisam e codifiquem apenas as duas ou três correções operacionais mais executadas como scripts simples disparados pelo bate-papo. Automatizem o que remove o trabalho repetitivo (toil) diário e resistam a construir maquinaria de governança antes de terem um problema de governança.

**Pequena empresa.** Sem especialista dedicado em teste ou plataforma, apoiem-se na automação embutida nas ferramentas pelas quais já pagam: os executores de teste do serviço de CI, seus complementos de varredura e ambientes gerenciados, em vez de uma construção sob medida de infraestrutura de testes. Enquadrem a escolha entre comprar e construir em torno de uma manutenção que vocês realisticamente conseguem sustentar, porque um pipeline sob medida e engenhoso que ninguém consegue manter é um resultado pior que um mais simples e hospedado. Usem a RPA com parcimônia e só onde uma ferramenta de fornecedor faz ponte com um sistema que vocês não conseguem integrar de nenhum outro modo.

**Grande empresa.** Entre muitas equipes, o objetivo é controles uniformes e impossíveis de contornar numa escala que a revisão manual não cobre: infraestrutura compartilhada e paralela de testes com ambientes efêmeros, guardrails de política como código e evidência de conformidade gerada automaticamente a cada execução de pipeline. Padronizem as interfaces para que as equipes reutilizem as ferramentas de remediação e de runbooks em vez de cada uma reinventar scripts frágeis e gerenciem a automação como um portfólio com dono e financiado, com orçamentos claros de manutenção. Cuidem para que uma verificação que apenas avisa numa equipe não seja tratada como bloqueante em outra, porque a imposição inconsistente mina a garantia pela qual vocês estão pagando.

**Governo.** As regras de contratação, os deveres de transparência e os mandatos de monitoramento contínuo tornam a conformidade como código quase essencial: cada execução de pipeline deve registrar os controles verificados, as varreduras realizadas e as aprovações concedidas como evidência à prova de adulteração e pronta para auditoria. Favoreçam a automação aberta e portável ao aprisionamento proprietário para que um contrato futuro possa migrar para outro fornecedor e mantenham um humano responsável por qualquer remediação que toque serviços voltados ao cidadão. Onde um sistema de décadas forçar a RPA, documentem-na como uma ponte deliberada e temporária, com um plano público de modernização, e mantenham as verificações de governança na linha de base de segurança exigida a cada mudança.

## Exemplos

**Startup.** Uma startup de sete pessoas mantém uma pirâmide de testes enxuta, de testes de unidade em sua maioria rápidos mais alguns de integração, todos rodando em paralelo para que a suíte completa termine em menos de três minutos a cada pull request. Quando um teste começa a falhar de forma intermitente, tratam-no como um bug real e o corrigem ou o apagam naquela semana, porque com uma equipe tão pequena um único build vermelho ignorado erodiria a confiança em toda a suíte. Também codificam as duas correções operacionais mais comuns, reiniciar um worker travado e limpar um disco cheio, como pequenos scripts disparados pelo Slack, de modo que quem estiver de sobreaviso possa rodá-los com segurança sem acionar o único engenheiro que os escreveu.

**Grande empresa.** Uma grande empresa de comércio eletrônico roda uma suíte de dezenas de milhares de testes, paralelizada numa frota de workers para que a suíte completa termine em minutos. Ambientes efêmeros sobem por pull request para testes realistas de integração. As operações correm pelo ChatOps: os engenheiros de sobreaviso disparam runbooks codificados pelo bate-papo, e as falhas comuns, como um serviço sobrecarregado, são remediadas automaticamente, com a ação registrada para revisão. O pipeline coleta automaticamente a evidência das varreduras de segurança e das aprovações, de modo que a auditoria anual se apoia num registro sempre atual e não numa caça manual de evidências.

**Governo.** Uma agência pública sujeita a rígidas exigências de monitoramento contínuo implementa a conformidade como código. Cada execução de pipeline registra os controles verificados, as varreduras realizadas e as aprovações concedidas, produzindo evidência à prova de adulteração que satisfaz os auditores sob demanda. Como um de seus sistemas centrais é uma aplicação de décadas sem API, a agência usa a RPA como ponte deliberada para automatizar a entrada de dados nele enquanto um esforço de modernização avança, com um plano explícito de aposentar a RPA quando existir uma integração adequada. As verificações automatizadas de governança impõem a linha de base de segurança obrigatória a cada mudança de infraestrutura.

## Justificativa de negócio: motivações, ROI e TCO

O ROI da automação de testes e de processos aparece como tempo de engenheiro recuperado, entrega mais rápida e segura, recuperação de incidentes mais ágil e custo de conformidade dramaticamente menor. Os testes automatizados viabilizam a mudança rápida e confiante que sustenta o desempenho de entrega. As operações e a remediação automatizadas cortam o trabalho repetitivo (toil) e a indisponibilidade que drenam equipes e orçamentos. A conformidade como código pode transformar uma auditoria de semanas de preparação manual numa consulta de rotina, uma economia ao mesmo tempo financeira e de reputação.

A comparação de TCO pesa o custo real e contínuo de construir e manter a automação contra o custo de não automatizar. O teste e as operações manuais não custam apenas as horas gastas. Custam também os defeitos que escapam, os incidentes que se arrastam, as auditorias que consomem a equipe especialista e o esgotamento de engenheiros que fazem trabalho repetitivo (toil). Para a liderança, o argumento é direto: a automação converte despesa operacional e risco recorrentes num investimento de custo único mais manutenção que escala e torna a qualidade e a conformidade contínuas e não episódicas. Uma ressalva vale ser dita com clareza. A automação precisa ser mantida e merecer confiança. A automação sem financiamento e negligenciada decai num passivo.

## Antipadrões e armadilhas

- **Testes instáveis tolerados.** As falhas intermitentes destroem a confiança e treinam os engenheiros a ignorar resultados vermelhos.
- **Automatizar um processo quebrado.** Automatizar um fluxo ruim só faz a bagunça acontecer mais depressa. Consertem primeiro o processo.
- **RPA como estratégia.** Depender de uma automação frágil de interface como solução permanente mascara e entrincheira lacunas de integração.
- **Remediação sem detecção sólida.** Correções automatizadas disparadas por sinais ruins podem amplificar um incidente.
- **Runbooks como prosa obsoleta.** Procedimentos que vivem em documentos desatualizados dão falsa confiança numa crise.
- **Evidência de conformidade coletada manualmente.** As caças manuais periódicas de evidências são caras e deixam lacunas entre as auditorias.
- **Nenhum humano no circuito para ações de alto risco.** A automação total de operações perigosas remove o julgamento que previne desastres.

## Modelo de maturidade

**Nível 1, Iniciar.** O teste e as operações são em grande parte manuais e reativos. A cobertura é ad hoc, os procedimentos vivem na cabeça das pessoas ou em documentos obsoletos, a remediação acontece à mão durante os incidentes e a evidência de conformidade é montada numa correria antes de cada auditoria.

**Nível 2, Desenvolver.** Existem testes automatizados, mas são lentos, instáveis ou rodam de modo inconsistente, e as práticas variam muito entre as equipes. Alguns scripts operacionais e runbooks existem em bolsões, mas a remediação ainda é manual e a governança é imposta por revisão periódica e não por verificações contínuas.

**Nível 3, Padronizar.** Uma infraestrutura de testes rápida, paralela e confiável é o padrão documentado da organização. Os runbooks como código e o ChatOps estão em uso geral, a evidência de conformidade é gerada automaticamente a partir das execuções de pipeline e os controles de governança rodam como verificações automatizadas impostas e aplicadas de modo consistente entre as equipes.

**Nível 4, Gerenciar.** A própria automação é medida e controlada em relação a linhas de base. Vocês acompanham a taxa de testes instáveis, o tempo de relógio da suíte, o tempo médio de recuperação dos incidentes autorremediados, a fração de controles com evidência automatizada e as taxas de falsos positivos das verificações bloqueantes, e mantêm cada métrica numa meta combinada. As decisões de remediação e de cobertura são conduzidas por esses dados, e toda ação automatizada é registrada para que tendências e regressões fiquem visíveis e não adivinhadas.

**Nível 5, Orquestrar.** A automação é continuamente melhorada e integrada em toda a organização. A remediação automatizada trata os incidentes de rotina com salvaguardas comprovadas, a conformidade é contínua e está sempre pronta para auditoria, e as cadeias de ferramentas de teste, de operações e de governança se adaptam conforme os sistemas mudam, com as pontes de RPA ativamente aposentadas à medida que as integrações amadurecem. Os humanos se concentram no julgamento enquanto as máquinas tratam o repetível, e todo o sistema se reequilibra com base em evidências.

## Ideias para discussão

- Quais procedimentos operacionais são seguros para automatizar por completo, e quais precisam manter um humano no circuito?
- Como vocês mantêm rápida e sem instabilidade uma suíte grande de testes à medida que ela cresce?
- Onde a RPA é uma ponte justificada para os seus sistemas legados, e qual é o plano para aposentá-la?
- Quais controles vocês poderiam converter primeiro de auditoria manual para conformidade contínua como código?
- Como vocês constroem confiança na remediação automatizada sem arriscar incidentes amplificados?
- Como vocês financiam a manutenção contínua de que a automação precisa para que ela não decaia num passivo?

## Principais conclusões

- Automatizem o repetido, o previsível e o baseado em regras. Reservem o esforço humano para o julgamento e as decisões de alto risco.
- Tornem os testes automatizados rápidos, paralelos e confiáveis e eliminem sem piedade a instabilidade.
- Codifiquem as operações como runbooks como código e exponham-nos pelo ChatOps para visibilidade e registro.
- Gerem a evidência de conformidade automaticamente para que as auditorias se apoiem num registro contínuo e atual.
- Usem a RPA apenas como uma ponte deliberada e temporária para sistemas sem API e planejem sua aposentadoria.
- Imponham os controles de governança, de segurança e de custo como verificações automatizadas contínuas, com humanos supervisionando as ações arriscadas.

## Referências e leitura complementar

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
