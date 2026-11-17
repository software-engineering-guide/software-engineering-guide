# 2.5 Revisão de código e colaboração

## Visão geral e motivação

A [revisão de código](https://en.wikipedia.org/wiki/Code_review) é a prática de fazer com que alguém que não seja o autor examine uma mudança antes de ela ser integrada. É uma das atividades de qualidade e de compartilhamento de conhecimento de maior alavancagem que uma organização de software tem e, para equipes grandes, é também um mecanismo primário de coordenação e de cultura. A revisão pega defeitos, espalha o conhecimento da base de código, impõe padrões e orienta engenheiros, mas só quando é bem feita. Mal feita, vira um gargalo, uma fonte de atrito ou um carimbo automático que dá falsa garantia.

Para equipes grandes, a revisão é onde o trabalho individual encontra a responsabilidade coletiva. Muitas vezes é o principal ponto de contato entre engenheiros que de outro modo trabalham sozinhos, então suas normas moldam como toda a organização colabora. A revisão espalha conhecimento para que nenhuma parte do sistema seja entendida por apenas uma pessoa, o que reduz o risco do [fator ônibus](https://en.wikipedia.org/wiki/Bus_factor), o perigo de o conhecimento ficar com poucas pessoas, que aflige sistemas grandes e de longa vida. Ela também cria uma trilha de auditoria de quem mudou o quê e de quem aprovou.

Em contextos corporativos e governamentais, a revisão muitas vezes carrega uma dimensão de conformidade. A [segregação de funções](https://en.wikipedia.org/wiki/Separation_of_duties) (nenhuma pessoa controla uma mudança sensível inteira), as aprovações obrigatórias e a rastreabilidade são frequentemente controles exigidos. Uma mudança que toca sistemas sensíveis pode precisar de revisão por papéis específicos, e o registro da revisão vira evidência de auditoria. O seu desafio é satisfazer esses controles mantendo a revisão rápida e construtiva, em vez de transformá-la em cerimônia.

## Princípios fundamentais

- Revise para melhorar a mudança e compartilhar conhecimento, não para se exibir.
- Mudanças pequenas recebem revisões melhores, então mantenha os pull requests (PRs) focados e de tamanho razoável.
- A latência da revisão é um custo para a equipe toda. Um retorno rápido mantém todos em movimento.
- Automatize o mecânico (estilo, testes, varreduras de segurança) para que os humanos revisem design e correção.
- Separe as questões bloqueantes das sugestões e preferências e seja explícito sobre qual é qual.
- Critique o código, não a pessoa. As normas de feedback moldam se a revisão constrói confiança ou a corrói.
- O autor é responsável por tornar a mudança fácil de revisar.

## Recomendações

### Faça pull requests pequenos e bem descritos

Mantenha cada mudança focada numa única preocupação lógica e pequena o bastante para ser revisada com cuidado. PRs grandes recebem revisões rasas. Dê uma descrição clara do que mudou, por quê e como você verificou, para que o revisor tenha contexto. Separe refatorações mecânicas e mudanças de comportamento em PRs distintos, para que cada um seja fácil de raciocinar. Uma boa descrição é a contribuição mais importante do autor para a qualidade da revisão.

### Estabeleça padrões e listas de verificação de revisão

Explicite o que os revisores devem procurar: correção, encaixe de design, adequação dos testes, implicações de segurança, legibilidade e aderência aos padrões. Uma lista de verificação leve mantém as revisões consistentes e impede que dimensões importantes escapem, sem transformar a revisão em marcação de itens. Defina o que exige revisão, quem pode aprovar e quaisquer aprovações por papel necessárias para áreas sensíveis.

### Defina e monitore normas de latência de revisão

Combine um prazo-alvo de retorno, por exemplo responder em um dia útil, e faça da revisão uma parte de primeira classe do dia, e não algo espremido por último. Filas longas de revisão paralisam a entrega e tentam os engenheiros a mudanças grandes e agrupadas. Monitore o tempo até a primeira revisão e o tempo até a integração e trate a latência sustentada como um problema de processo a corrigir, não como uma falha pessoal.

### Automatize tudo que for mecânico

Rode formatação, [linting](https://en.wikipedia.org/wiki/Lint_(software)), testes e varredura de segurança e de dependências na [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), para que os revisores nunca gastem atenção com isso. Reserve a revisão humana para o que as máquinas não conseguem julgar: se o design está certo, se a abordagem se encaixa no sistema, se os testes são significativos e se o código ainda fará sentido mais tarde.

### Use a programação em par e em grupo onde couberem

Use a [programação em par](https://en.wikipedia.org/wiki/Pair_programming), em que dois engenheiros escrevem código juntos numa só estação de trabalho, para trabalho complexo ou de alto risco, integração e transferência de conhecimento. É revisão contínua e muitas vezes elimina a necessidade de uma etapa separada de revisão. Use a [programação em grupo](https://en.wikipedia.org/wiki/Mob_programming), em que toda a equipe trabalha ao mesmo tempo numa tarefa, para decisões críticas de design ou para espalhar pela equipe o conhecimento de uma área espinhosa. Pense nelas como complementos da revisão assíncrona, escolhidos conforme o contexto, e não como substitutos a impor em toda parte.

### Adote a revisão automatizada e assistida por IA com cuidado

Use ferramentas de revisão automatizada e assistentes de IA para pegar problemas comuns, sugerir melhorias e aliviar a carga do revisor, mas trate a saída delas como insumo, não como autoridade. A revisão por IA é boa em problemas de superfície e consistência e fraca em julgamento profundo de design e contexto do sistema. Mantenha uma pessoa responsável por toda aprovação, especialmente em mudanças sensíveis à segurança e relevantes para a conformidade.

### Defina normas de feedback construtivo

Defina normas que mantenham o feedback específico, gentil e focado no código. Incentive os revisores a fazer perguntas em vez de dar ordens, a explicar o raciocínio por trás de um pedido e a elogiar o bom trabalho. Marque com clareza as preocupações bloqueantes e as sugestões opcionais (por exemplo, prefixando as notas não bloqueantes). Essas normas decidem se a revisão fortalece a equipe ou gera ressentimento.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Revisão assíncrona de PR | Flexível. Documentada. Escala entre fusos horários | Latência. Perde nuance. Pode parecer hostil |
| Programação em par | Revisão contínua. Transferência rápida de conhecimento. Alta qualidade | Duas pessoas numa tarefa. Cansativa. Mais difícil de agendar |
| Programação em grupo | Alinhamento de toda a equipe. Espalha conhecimento profundo | Cara no agregado. Não serve para trabalho de rotina |
| Múltiplos revisores obrigatórios | Forte garantia. Amigável à conformidade | Mais lenta. Dilui a responsabilidade. Pressão de fila |
| Revisão assistida por IA | Rápida, incansável em problemas comuns. Reduz a carga | Perde o contexto do sistema. Falsa confiança se houver excesso de confiança |

A tensão central é minúcia versus velocidade. Uma revisão mais profunda pega mais, mas desacelera a entrega e pode frustrar os autores. Uma revisão mais rápida mantém o fluxo, mas corre o risco de ser superficial. O caminho é ajustar a profundidade da revisão ao risco da mudança, de modo que mudanças triviais recebam uma revisão leve e as arriscadas, uma profunda, e automatizar o trabalho mecânico para que o esforço humano se concentre onde importa.

## Perguntas para discutir com sua equipe

1. **O que conta como grande demais para um pull request, e vocês separam refatorações mecânicas de mudanças de comportamento?** Este capítulo afirma com clareza que PRs grandes recebem revisões rasas e que o autor é dono da revisabilidade, e pede que você separe refatorações de mudanças de comportamento para que cada uma seja fácil de raciocinar. Numa equipe grande, um PR gigante garante um carimbo automático, que dá falsa garantia enquanto deixa passar defeitos reais. Leve as evidências: a distribuição dos tamanhos dos seus PRs e como a profundidade da revisão cai à medida que os diffs crescem. Combine uma norma prática de tamanho e o hábito de integrar refatorações puras separadamente das mudanças de lógica, para que um revisor consiga de fato guardar cada mudança na cabeça. Essa única disciplina eleva a qualidade de toda revisão que vem depois.

2. **Como vocês distinguem uma objeção bloqueante de uma sugestão opcional, e essa convenção é de fato usada?** O capítulo pede que você separe as questões bloqueantes das preferências e seja explícito sobre qual é qual, e aponta o bloqueio por preferência como um antipadrão corrosivo. Sem uma convenção compartilhada, a opinião de estilo de um revisor é lida como uma mudança exigida, o que gera ressentimento e desacelera a entrega da equipe toda. Leve exemplos de revisões recentes em que uma preferência travou uma integração como sinal concreto. Adote um marcador leve, por exemplo um prefixo que identifique as notas não bloqueantes, para que os autores saibam na hora o que precisa mudar e o que é sugestão. Isso mantém a revisão focada em correção e design e não em gosto.

3. **Quem deve aprovar mudanças em código sensível à segurança ou relevante para a conformidade, e como esse encaminhamento é imposto?** Este capítulo descreve aprovações por papel, regras de propriedade de código e segregação de funções em que nenhuma pessoa controla uma mudança sensível inteira, com a aprovação registrada como evidência de auditoria. Em contextos corporativos e governamentais esses são controles exigidos, e o risco é que ou sejam pulados ou virem um gargalo que congela a entrega. Leve o sinal: quais módulos são sensíveis e se as regras de propriedade hoje encaminham essas mudanças aos aprovadores certos automaticamente. Codifique o encaminhamento na configuração de propriedade de código e combine-o com verificações automatizadas e mudanças pequenas, para que o controle seja satisfeito sem uma fila de porteiros humanos. Decida isso deliberadamente em vez de descobrir a lacuna durante uma auditoria.

4. **Que meta de latência de revisão vocês de fato combinaram, e a medem e impõem, ou é só uma aspiração?** O capítulo trata a latência da revisão como um custo da equipe toda e pede que você monitore o tempo até a primeira revisão e o tempo até a integração, tratando o atraso sustentado como um problema de processo e não como uma falha pessoal. Numa equipe grande, uma fila de revisão sem dono taxa todos em silêncio: os autores agrupam mudanças maiores para evitar a espera, essas mudanças recebem então revisões mais rasas, e o prazo de entrega sobe sem nenhum culpado único. A consideração concorrente é que uma meta rígida de latência pode levar os revisores a passar os olhos por cima, então velocidade e profundidade precisam ser equilibradas e não trocadas às cegas. Leve as evidências: a distribuição atual do tempo até a primeira revisão, como ela varia por equipe e por tamanho de mudança e onde as revisões ficam paradas por mais tempo. Em contextos corporativos e governamentais, ligue a meta às métricas de fluxo que a liderança já acompanha, porque um controle obrigatório de múltiplos revisores sem norma de latência vira o gargalo que congela a entrega e tenta as pessoas a contornar o controle por completo.

5. **Para que tipos de mudança vocês confiam na revisão automatizada e assistida por IA, e onde uma pessoa deve continuar responsável?** O capítulo diz para tratar a saída da revisão por IA como insumo, não como autoridade: forte em problemas de superfície e consistência, fraca em julgamento profundo de design e contexto do sistema, com uma pessoa responsável por toda aprovação. Sem uma fronteira explícita, uma equipe grande deriva para o excesso de confiança, em que um comentário verde de um robô é lido como revisão aprovada e riscos reais de design e de segurança passam sob falsa confiança. A força contrária é que a revisão por IA genuinamente alivia a carga e pega defeitos comuns sem se cansar, então bani-la desperdiça alavancagem. Leve as evidências: onde as sugestões automatizadas pegaram problemas reais, onde produziram ruído e quais tipos de mudança (sensíveis à segurança, relevantes para a conformidade, arquiteturais) vocês nunca deixariam uma máquina aprovar sozinha. Para o trabalho corporativo e governamental, nomeie quem detém a responsabilidade por uma aprovação quando um assistente de IA estava no circuito, porque uma auditoria perguntará quem revisou uma mudança, e “a ferramenta” não é uma resposta que um regulador aceite.

6. **Onde o par ou o grupo devem substituir a revisão assíncrona, e como vocês usam a revisão para reduzir deliberadamente o risco do fator ônibus?** O capítulo enquadra a programação em par e em grupo como revisão contínua escolhida conforme o contexto e nomeia a revisão como o mecanismo que espalha o conhecimento para que nenhuma parte do sistema seja entendida por apenas uma pessoa. Deixado implícito, o conhecimento se concentra: o mesmo especialista revisa toda mudança num subsistema, a revisão vira um carimbo automático porque ninguém mais consegue desafiá-lo e o risco do fator ônibus cresce precisamente onde o sistema é mais crítico. A consideração concorrente é o custo, já que o grupo gasta o tempo de toda a equipe e o par prende dois engenheiros, então você não pode impô-lo em toda parte. Leve as evidências: quais módulos têm apenas um revisor crível, onde a integração empaca e onde uma área espinhosa se beneficiaria de uma sessão ao vivo em vez de fios de comentários. Numa organização grande ou pública, trate a difusão deliberada de conhecimento como gerenciamento de riscos, porque um sistema de longa vida cujas partes críticas dependem de uma pessoa é um passivo operacional e de continuidade, e não apenas um inconveniente de pessoal.

## Perspectiva por setor

**Startup.** Com três ou quatro engenheiros, mantenha a revisão leve: a aprovação de um colega num pull request pequeno, verificações mecânicas na CI e nenhum segundo revisor obrigatório que travaria uma integração. O objetivo real é menos conformidade e mais garantir que mais de uma pessoa entenda cada parte do sistema, então pareie nas peças arriscadas e trate isso como integração. Não construa um encaminhamento pesado de propriedade de código que você logo superará. Uma norma compartilhada de mudanças pequenas e bem descritas compra a maior parte do benefício quase sem custo.

**Pequena empresa.** É improvável que você tenha um especialista em ferramentas de revisão, então apoie-se no que a sua plataforma de hospedagem (por exemplo um serviço Git gerenciado) oferece pronto, em vez de construir automação sob medida. Compre as integrações de linting, de testes e de varredura de segurança em vez de mantê-las, para que seus poucos engenheiros gastem os escassos minutos de revisão em design e correção. Mantenha uma única regra simples, toda mudança passa por outro par de olhos, e resista a acrescentar processo que você não tem quem mantenha.

**Grande empresa.** O desafio é a consistência entre muitas equipes: padrões compartilhados, regras de propriedade de código que encaminham as mudanças sensíveis aos aprovadores certos e aprovações por papel registradas como evidência de auditoria. Automatize as verificações mecânicas em toda a organização para que a revisão humana se concentre no design e acompanhe a latência da revisão como uma métrica de fluxo, para que os controles obrigatórios de múltiplos revisores não virem gargalos em silêncio. Ajuste a profundidade da revisão ao risco da mudança com uma política documentada, de modo que as mudanças triviais continuem rápidas enquanto as de alto risco recebam segregação de funções e escrutínio mais profundo.

**Governo.** O controle de mudanças costuma ser obrigatório: toda mudança em produção revisada e aprovada por alguém que não seja o autor, com o registro mantido como evidência de auditoria para satisfazer os requisitos de segregação de funções. Favoreça uma trilha transparente e rastreável de quem criou, quem aprovou e quais verificações passaram e invista em automação e em mudanças pequenas e frequentes para que o controle não congele a entrega. Onde as ferramentas de revisão são contratadas, exija registros de auditoria exportáveis e evite o aprisionamento, já que a evidência precisa sobreviver a qualquer fornecedor isolado e resistir ao escrutínio público.

## Exemplos

**Startup.** Uma startup de quatro engenheiros mantém todo pull request pequeno e pede a aprovação de um colega antes de integrar, menos por conformidade e mais para garantir que nenhuma pessoa seja a única a entender uma parte do sistema. A CI roda o formatador e os testes, de modo que os humanos gastam seus poucos minutos de revisão em design e correção e não em espaçamento. Quando a equipe chega a uma peça espinhosa do fluxo de pagamentos, duas pessoas pareiam nela em vez de trocar comentários assíncronos, o que serve também de integração para a contratação mais recente.

**Grande empresa.** Uma grande empresa de software exige pelo menos uma revisão aprovadora em toda mudança, mais uma segunda aprovação para mudanças em módulos sensíveis à segurança identificados por regras de propriedade de código. A CI trata de todas as verificações de estilo e de testes, de modo que os revisores se concentram em design e correção. A equipe acompanha o tempo até a primeira revisão e trata uma mediana crescente como sinal para reequilibrar a carga de trabalho. Os novos engenheiros são integrados por meio do par, o que encurta o caminho deles até contribuir de forma independente.

**Governo.** Uma agência nacional que opera sob requisitos estritos de controle de mudanças exige que toda mudança em produção seja revisada e aprovada por alguém que não seja o autor, com a aprovação registrada para auditoria. Para evitar que esse controle vire um gargalo, a agência investe em verificações automatizadas e em mudanças pequenas e frequentes e define uma norma de resposta de revisão no mesmo dia. A trilha da revisão, cobrindo quem criou, quem aprovou e quais verificações passaram, torna-se parte da evidência de conformidade de cada lançamento, satisfazendo os requisitos de segregação de funções sem congelar a entrega.

## Justificativa de negócio: motivações, ROI e TCO

A revisão de código se paga em três moedas: defeitos pegos antes da produção, conhecimento espalhado pela equipe e padrões mantidos automaticamente ao longo do tempo. Pegar um defeito na revisão é muito mais barato que pegá-lo em produção, e o benefício do compartilhamento de conhecimento reduz o risco de dependência de pessoas-chave, que de outro modo pode custar caro a uma organização quando alguém sai. A revisão é também o mecanismo de transmissão cultural que mantém coerente uma equipe em crescimento.

O custo da revisão é tempo de engenharia e alguma latência, ambos administráveis com boas práticas. O custo de *não* revisar, ou de revisar mal, inclui defeitos em produção, conhecimento em silos, código inconsistente e, em contextos regulamentados, auditorias fracassadas e constatações de conformidade. A revisão excessivamente pesada também tem um custo real: filas longas, lotes grandes demais, engenheiros desmoralizados. Para defender o caso junto à liderança, ligue as práticas de revisão à taxa de falha de mudanças, ao prazo de entrega e à velocidade de integração e acompanhe a latência da revisão como uma métrica de fluxo explícita.

## Antipadrões e armadilhas

- **O carimbo automático:** aprovações sem exame real, dando falsa garantia e satisfazendo apenas a letra de um controle.
- **O PR gigante:** milhares de linhas que só podem ser percorridas por alto, garantindo uma revisão rasa.
- **Revisão só de minúcias:** focar em trivialidades e perder o design e a correção, muitas vezes porque as verificações mecânicas não são automatizadas.
- **Revisão como vigilância de portão:** usar a revisão para afirmar domínio ou bloquear os outros, envenenando a colaboração.
- **A fila lenta:** revisões paradas por dias, travando a entrega e incentivando o agrupamento.
- **Excesso de confiança na revisão por IA:** tratar as sugestões automatizadas como autoritativas e abandonar o julgamento humano em mudanças arriscadas.
- **Bloquear por preferência:** apresentar opiniões pessoais de estilo como mudanças exigidas sem distingui-las de defeitos reais.

## Modelo de maturidade

- **Nível 1, Iniciar:** A revisão é ad hoc e reativa. Muitas vezes é pulada ou feita de forma inconsistente, os problemas mecânicos dominam os comentários, as normas de feedback não existem e qualquer trilha de aprovação é incidental e não deliberada.
- **Nível 2, Desenvolver:** Existem práticas básicas de revisão, mas variam de equipe para equipe. A revisão é exigida em alguns lugares e lenta ou opcional em outros, a automação é parcial e o tamanho e a qualidade dos pull requests oscilam muito, sem expectativa compartilhada.
- **Nível 3, Padronizar:** Os padrões são documentados e impostos em toda a organização. PRs pequenos e focados, formatação, linting, testes e varredura de segurança automatizados na CI, listas de verificação claras, uma convenção explícita de bloqueio versus sugestão e regras de propriedade de código que encaminham as mudanças sensíveis aos aprovadores certos.
- **Nível 4, Gerenciar:** A revisão é medida e controlada em relação a linhas de base. O tempo até a primeira revisão, o tempo até a integração, a profundidade da revisão versus o risco da mudança, a taxa de escape de defeitos e a taxa de falha de mudanças são acompanhados. A latência sustentada é tratada como problema de processo, e os dados orientam onde reequilibrar a carga dos revisores e onde os controles estão desacelerando a entrega sem acrescentar garantia.
- **Nível 5, Orquestrar:** A revisão é continuamente melhorada e integrada em toda a organização. A profundidade se adapta ao risco da mudança, o par, o grupo e a assistência de IA são usados deliberadamente com uma pessoa responsável, a difusão do conhecimento e o risco do fator ônibus são geridos intencionalmente e a revisão melhora de forma mensurável a qualidade, o fluxo de entrega e a integração.

## Ideias para discussão

- Qual é a meta certa de latência de revisão para a sua equipe, e o que impede vocês de alcançá-la?
- Como você ajusta a profundidade da revisão ao risco da mudança sem acrescentar burocracia?
- Onde o par ou o grupo superam a revisão assíncrona no seu contexto?
- Quanto a revisão assistida por IA deve ser confiável, e para que tipos de mudança?
- Como você mantém o feedback da revisão construtivo à medida que a equipe cresce e se diversifica?
- Como você satisfaz exigências de aprovação de conformidade sem criar gargalos?

## Principais conclusões

- Mantenha os pull requests pequenos e bem descritos. O autor é dono da revisabilidade.
- Automatize o mecânico para que os humanos revisem design, correção e testes.
- Acompanhe e gerencie a latência da revisão como um custo de fluxo da equipe toda.
- Ajuste a profundidade da revisão ao risco da mudança e distinga questões bloqueantes de preferências.
- Use o par, o grupo e a assistência de IA como complementos adequados ao contexto, mantendo uma pessoa responsável.

## Referências e leitura complementar

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
