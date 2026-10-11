# 11.3 Teoria das filas

## Visão geral e motivação

A [teoria das filas](https://en.wikipedia.org/wiki/Queueing_theory) é o estudo matemático das filas de espera. Na engenharia de software, é a teoria silenciosa por trás de uma enorme quantidade de prática. A capacidade de resposta do atendimento ao cliente, o planejamento de [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (um método puxado que limita o [trabalho em andamento](https://en.wikipedia.org/wiki/Work_in_process) para melhorar o fluxo), as filas de mensagens entre processos, os pipelines de implantação contínua: todos são filas, e todos obedecem às mesmas leis. Entender essas leis permite a uma equipe raciocinar sobre [prazos de entrega](https://en.wikipedia.org/wiki/Lead_time), [vazão](https://en.wikipedia.org/wiki/Throughput), capacidade e o verdadeiro custo de rodar sistemas perto dos seus limites, em vez de ser surpreendida por eles em produção. Este capítulo fica na parte de Fluxo porque a teoria das filas é o alicerce formal do fluxo: explica *por que* o trabalho espera e o que de fato reduz a espera.

Eis a motivação: a intuição sobre filas é confiavelmente errada, e errada de modos caros. As pessoas presumem que um servidor rodando a 90% de utilização está “a 10% de ter problemas”, quando na verdade os tempos de espera explodem de modo não linear conforme a utilização se aproxima de 100%. Presumem que acrescentar trabalho em andamento (WIP) acelera a entrega, quando ele alonga os prazos. Planejam a capacidade em torno de médias e depois são destruídas pela variabilidade. Um pouco de teoria das filas substitui essas intuições custosas por um pequeno número de relações robustas, a mais importante a **[Lei de Little](https://en.wikipedia.org/wiki/Little%27s_law)**, que valem para filas de clientes, quadros de tarefas e pipelines de CI/CD igualmente.

Para grandes equipes, empresas e governo, a teoria das filas é uma linguagem compartilhada para capacidade e fluxo, que conecta papéis que de outro modo falam sem se entender. Os gerentes de produto se importam com o prazo de entrega da ideia ao cliente. Os SREs se importam com a utilização dos servidores e a latência. As equipes de DevOps se importam com a frequência de implantação. Os líderes de suporte se importam com os tempos de resposta. Tudo isso são métricas de fila, e exprimi-las num único arcabouço (taxa de chegada, taxa de atendimento, utilização, tempo de espera) permite à organização planejar a capacidade, definir SLOs (objetivos de nível de serviço) realistas e justificar o investimento com matemática e não com anedotas.

## Princípios fundamentais

- **Tudo o que tem espera é uma fila:** chamados, tarefas, mensagens e implantações incluídos.
- **A Lei de Little é a âncora:** itens no sistema = taxa de chegada × tempo no sistema (κ = λτ).
- **Utilização e tempo de espera são não lineares:** os últimos 15% de capacidade são os mais caros.
- **A variabilidade é a inimiga do fluxo:** as médias escondem a dor; a variância cria filas.
- **Reduzir o trabalho em andamento reduz o prazo de entrega:** a meta é o fluxo, não estar ocupado.
- **Meçam o fluxo inteiro:** chegadas, atendimento, sucessos, falhas, pulos e esperas.
- **Um processo é uma fila de filas:** modelem os estágios, depois otimizem o que restringe.

## Recomendações

### Aprendam a notação básica e usem-na de modo consistente

Um punhado de grandezas descreve qualquer fila. Padronizar nelas (as letras gregas são convencionais) remove a ambiguidade entre as equipes:

- **λ (lambda), taxa de chegada:** com que rapidez novos itens entram.
- **μ (mu), taxa de atendimento:** com que rapidez os itens são tratados. Como “taxa de atendimento” é usada de modo ambíguo, muitas vezes vale a pena dividir explicitamente a vazão em **taxa total (χ)**, **taxa de sucesso (α)**, **taxa de falha (β)** e **taxa de pulo (σ)**, em que χ = α + β + σ.
- **ρ (rho), utilização / intensidade de tráfego = λ / μ:** o resumo mais importante. ρ < 1 significa que a fila se esvazia; ρ ≥ 1 significa que ela cresce sem limite.
- **Tempos:** prazo de entrega (τ, do início ao fim), tempo de trabalho (φ, processamento real), tempo de espera (ω, pendente) e tempo de passo (θ, entre conclusões).
- **ε (epsilon), razão de erro:** falhas ÷ total.

Nomear explicitamente as falhas e os *pulos* importa em software: um item que é abandonado (um cliente que desiste, um carrinho deixado para trás, um chamado de trabalho rejeitado) sai da fila sem ser atendido, e fingir que foi “atendido” corrompe as métricas. Acompanhem **balking** (decidir não entrar), **reneging** (desistir depois de esperar) e **jockeying** (trocar de fila) como resultados de primeira classe.

### Ancorem o planejamento na Lei de Little

A Lei de Little afirma que o número médio de longo prazo de itens num sistema estável é igual à taxa média de chegada vezes o tempo médio que cada item passa no sistema: **κ = λ τ** (classicamente L = λW). É espantosamente geral (não exige nenhuma suposição sobre a distribuição das chegadas nem sobre a ordem de atendimento), o que a torna o cavalo de batalha do planejamento de fluxo. Reorganizada, diz que o **prazo de entrega = trabalho em andamento ÷ vazão**. Essa é a base matemática do kanban e do lean: se vocês querem prazos mais curtos e não conseguem elevar a vazão, precisam baixar o WIP. Também dá verificações rápidas de sanidade. Se 40 chamados estão abertos e vocês fecham 8 por dia, o chamado médio leva cerca de 5 dias, por mais ocupado que todos se sintam. Seu único requisito é a *estabilidade*: as chegadas não podem exceder persistentemente as saídas (ρ < 1), ou a fila, e as suposições da lei, desmoronam.

### Respeitem a não linearidade da utilização

A lição operacional mais importante da teoria das filas é que o tempo de resposta sobe de modo abrupto, não gradual, conforme a utilização se aproxima de 100%. As *Sete percepções sobre a teoria das filas*, de Bob Wescott, captam vividamente as consequências práticas:

1. Quanto mais lento o centro de atendimento, menor a utilização de pico para a qual vocês devem planejar.
2. É muito difícil usar os últimos 15% de qualquer coisa.
3. Quanto mais perto da borda vocês rodam, maior o preço de errar.
4. O crescimento do tempo de resposta é limitado por quantos itens podem esperar.
5. São médias, não máximos: planejem para a cauda.
6. Cuidado com o efeito de negação humana entre vários centros de atendimento.
7. Mostrem as pequenas melhorias sob sua melhor luz.

A implicação de projeto: **provisionem folga deliberadamente.** Mirar em 70–80% de utilização para sistemas sensíveis à latência não é desperdício; é comprar um tempo de resposta previsível. Isso informa diretamente o planejamento de capacidade e os SLOs (capítulos 3.5 e 9.1).

### Modelem os processos como uma fila de filas

O trabalho real flui por estágios, e um processo de vários estágios é simplesmente uma fila cujos itens estão eles mesmos em fila a cada passo. Modelem-no assim: a taxa de chegada do processo é a taxa de chegada do estágio 1; a taxa de sucesso do processo é a taxa de sucesso do último estágio; as contagens de erro e de pulo do processo são as somas entre os estágios. Duas formas comuns se repetem:

- **Funis**, em que a contagem de itens encolhe a cada estágio (contratação: prospecção → entrevista → oferta; compras: navegar → carrinho → pagar; entrega: integrar → UAT → produção). Otimizem o estágio que mais importa: maximizem as chegadas no topo do funil, minimizem os pulos no meio (abandono de carrinho) ou minimizem os erros no estágio final (lançamentos ruins em produção).
- Os fluxos de descoberta e entrega de **diamante duplo** (descobrir → definir → desenvolver → entregar), que a parte de Fluxo deste livro trata diretamente (capítulo 11.1).

Achar e aliviar o **estágio restritivo** (o gargalo) é onde a melhoria do fluxo compensa; otimizar o que não restringe apenas move a fila.

### Conectem as métricas de fila aos KPIs que as equipes já usam

As grandezas de fila mapeiam-se de forma limpa nas métricas de entrega e de confiabilidade de outras partes deste livro, o que torna a teoria prática e não acadêmica:

- O **prazo de entrega (Dτ)**, “do conceito ao cliente”, é uma medida de prazo (τ) e uma métrica DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (capítulo 11.2).
- A **frequência de implantação (Dμ)** é uma medida de taxa de atendimento.
- A **taxa de falha das mudanças (Dε)** é uma razão de erro.
- O **tempo para restaurar (Rτ)** é um prazo de restauração, isto é, o MTTR (capítulo 9.3).

Distingam os vários **MTTRs** (tempo médio para *responder*, *reparar*, *recuperar* e *resolver*) porque medem segmentos diferentes da fila de incidentes e são rotineiramente confundidos. Fundamentar SLIs/SLOs/SLAs (capítulo 9.1) em termos de fila mantém as metas honestas e comparáveis.

## Compromissos: prós e contras

| Decisão | Prós | Contras |
|---|---|---|
| **Rodar os sistemas com alta utilização** | Menor custo de hardware por unidade | Explosões não lineares de latência. Frágil a picos |
| **Provisionar folga generosa** | Latência previsível. Resiliente à variância | Custo em regime estável maior. Parece “subutilizado” |
| **Limitar o WIP (kanban)** | Prazos de entrega menores. Menos troca de contexto | Parece mais lento. Exige disciplina para manter o limite |
| **Modelagem formal de filas** | Decisões de capacidade quantificadas. Menos surpresas | Curva de aprendizado. Os modelos simplificam a realidade bagunçada |
| **Apenas regras práticas** | Rápidas, sem matemática | Erradas justamente onde é mais caro (perto da capacidade) |

O compromisso recorrente é **eficiência versus previsibilidade**: empurrar a utilização para cima poupa dinheiro até que de repente não poupa, e nesse ponto os custos de latência, falha e apagar incêndios eclipsam a economia. A contribuição da teoria das filas é dizer *onde* fica esse precipício, para que o compromisso seja uma escolha e não um acidente.

## Perguntas para discutir com sua equipe

1. **Qual é a sua meta explícita de utilização para cada sistema sensível à latência, e quem a aprovou?** A folga é uma compra deliberada de latência previsível, então deve ser política declarada e não um acidente de qualquer carga que tenha chegado. Como o tempo de resposta sobe de modo não linear, rodar a 85% já pode significar latência de cauda elevada, e no entanto as finanças veem a folga como desperdício e empurram a utilização para cima. Levem os números: a utilização atual, a curva de latência medida e o custo do seu último incidente de latência, e mostrem onde fica o precipício de cada serviço. Para sistemas corporativos e governamentais com picos sazonais (temporada de declarações, janelas de inscrição), definam a meta com base no pico, não na média. Se ninguém é dono da meta de utilização, os incidentes de latência continuarão aparecendo “do nada”.

2. **Onde nos seus sistemas há uma fila ilimitada, sem contrapressão para descartar carga quando sobrecarregada?** Uma fila ilimitada não falha com elegância; degrada-se até o colapso, porque chegadas que excedem persistentemente as saídas (rho >= 1) significam que a fila cresce sem limite. Inventariem as filas de mensagens, os pools de threads e os buffers de requisições e perguntem o que acontece em cada um quando a taxa de chegada excede a taxa de atendimento: ele descarta carga, aplica contrapressão ou cai? Isso importa de modo agudo na escala corporativa, em que um único componente a jusante saturado pode se propagar em cascata por serviços. Levem um resultado de teste de carga ou um incidente passado em que uma fila se acumulou e conferiram se o sistema rejeitou o trabalho excedente ou tentou segurar tudo. O conserto são filas limitadas com contrapressão explícita e timeouts derivados da Lei de Little, para que uma sobrecarga descarte em vez de derrubar.

3. **Vocês modelam o fluxo da ideia à produção como uma fila de filas, e as suas melhorias miram a restrição real?** Um processo de vários estágios é uma fila cujos itens esperam a cada estágio, e otimizar qualquer coisa que não seja o estágio restritivo apenas move a fila. Mapeiem o funil de entrega (integrar, UAT, produção, ou descobrir, definir, desenvolver, entregar) e meçam as taxas de chegada, de atendimento, de espera e de pulo em cada estágio para achar onde o trabalho de fato se acumula. As equipes rotineiramente otimizam o estágio que melhor entendem e não o gargalo, o que gasta esforço e não move nada. Levem dados de tempo de espera por estágio, não intuição, porque o gargalo muitas vezes é um estado de espera (revisão, aprovação, disponibilidade de ambiente) e não um estado de trabalho. Uma vez que conheçam a restrição, mirem ali e deixem em paz o que não restringe.

4. **Vocês usam a Lei de Little para definir limites de WIP, ou acrescentam capacidade para curar prazos de entrega que só mais disciplina consertaria?** A Lei de Little diz que o prazo de entrega é igual ao trabalho em andamento dividido pela vazão, então se vocês não conseguem elevar a vazão, a única alavanca restante para prazos mais curtos é baixar o WIP, o que não custa nada além de contenção. A atração contrária é real: limitar o trabalho em andamento parece mais lento e ocioso, e os gerentes sob pressão preferem contratar ou comprar hardware a dizer às equipes que comecem menos e terminem mais. Levem os números concretos, itens abertos atuais e taxa de conclusão por estágio, e calculem o prazo de entrega médio implícito, depois comparem com o que as pessoas acreditam que seja; a diferença costuma ser grande e constrangedora. Numa grande empresa ou agência, um pedido de contratação ou aquisição justificado como conserto de prazo de entrega deve ser testado primeiro contra essa aritmética, porque um aumento de pessoal que eleva o WIP pode alongar os próprios prazos que devia encurtar.

5. **Vocês planejam a capacidade em torno de médias, ou quantificaram a variabilidade que de fato cria as suas filas?** As filas se formam pela variância, não pela média, então dois sistemas com carga média idêntica podem se comportar de modo completamente diferente se um tem chegadas em rajadas ou tempos de atendimento de cauda longa. A tensão é que as médias são fáceis de coletar e tranquilizadoras de relatar, enquanto a variância e a cauda são mais difíceis de medir e indesejadas num relatório de status. Levem a distribuição, não a média: a rajada das chegadas, os tempos de atendimento e de espera nos percentis 95 e 99 e os tamanhos de lote que concentram o trabalho em picos. Para sistemas corporativos e governamentais com surtos previsíveis (temporada de declarações, folhas de pagamento, janelas de inscrição, cargas de fim de trimestre), planejem o buffer e a meta de utilização com base na variância do período de pico, porque um projeto dimensionado para a média anual falhará justamente quando o público estiver olhando.

6. **Quais das suas filas contam em silêncio abandonos e rejeições como se o trabalho tivesse sido atendido, e que demanda não atendida isso esconde?** Um item que desiste de entrar, desiste depois de esperar ou é rejeitado sai da fila sem ser tratado, e registrá-lo como “atendido” corrompe de uma vez a sua vazão, a sua razão de erro e o seu plano de capacidade. A consideração contrária é que “chamadas atendidas” ou “chamados fechados” ficam melhor num painel do que “quem ligou e desistiu”, então o número honesto é o que ninguém se oferece para trazer à tona. Levem a taxa de pulo (σ), as contagens de balking e reneging e a diferença entre carga oferecida e carga atendida, para que a demanda verdadeira fique visível. Isso importa agudamente na prestação de serviços do governo, em que os cidadãos que abandonam uma fila telefônica ou um pedido de benefício são obrigações não atendidas e não casos resolvidos, e relatá-los como tratados tanto distorce o desempenho quanto subestima a capacidade que se deve ao público.

## Perspectiva por setor

**Startup.** Vocês não têm tempo para modelagem formal de filas nem precisam dela. Busquem primeiro as duas vitórias mais baratas: apliquem a Lei de Little ao seu backlog para ver o prazo de entrega real que o seu WIP implica e observem o quadro kanban atrás do estágio em que o trabalho se acumula antes de contratar contra um gargalo que pode não existir. Mantenham a utilização longe do precipício em qualquer caminho sensível à latência deixando folga em vez de ajustá-la ao limite, porque uma queda durante um pico de crescimento custa muito mais que um pouco de capacidade ociosa.

**Pequena empresa.** Sem especialista em filas na equipe, comprem as métricas em vez de construir os modelos. Escolham um help desk, um broker de mensagens ou uma plataforma de hospedagem que já reporte taxa de chegada, tempo de espera e abandono, e leiam esses números em vez de derivá-los. Enquadrem a decisão como vigiar dois sintomas: esperas que sobem de modo não linear conforme vocês ficam mais ocupados e clientes que desistem antes de serem atendidos, já que um cliente perdido é o custo de fila que mais dói a uma pequena empresa.

**Grande empresa.** O trabalho é tornar o pensamento de filas uma disciplina compartilhada entre muitas equipes: uma notação acordada (λ, μ, ρ, prazo de entrega), políticas consistentes de WIP e de folga de utilização e padrões de contrapressão para que um componente a jusante saturado não se propague em cascata entre serviços. Definam SLOs e capacidade a partir da análise de filas e não de palpites, e gerenciem as filas como um portfólio com linhas de base e revisões para que nenhuma equipe isolada rode quente. Embutam a análise na governança de capacidade e na auditoria, para que uma meta de folga seja uma decisão documentada de que alguém é dono.

**Governo.** A contratação, a transparência e a prestação de contas públicas moldam toda escolha de capacidade. Dimensionem centrais de atendimento e sistemas voltados ao cidadão com base na variância do período de pico (temporada de declarações, janelas de inscrição) e não na média anual, e dotem de pessoal para manter a utilização longe do precipício quando a demanda surge. Acompanhem balking e reneging como demanda pública não atendida em vez de escondê-los em “chamadas atendidas” e justifiquem o gasto de capacidade com estimativas de tempo de espera pela Lei de Little, que dão a auditores e a eleitos um caso defensável e apoiado em matemática em vez de uma anedota.

## Exemplos

**Startup.** Uma equipe SaaS de cinco pessoas se afogando num backlog de suporte presume que precisa contratar mais um atendente. Antes de gastar o dinheiro, aplica a Lei de Little: 60 chamados abertos e 12 fechados por dia significam que o chamado médio espera cerca de 5 dias, o que combina com os e-mails raivosos. Observando o quadro kanban, nota que os chamados se acumulam esperando a engenharia, não o suporte, então limita o trabalho em andamento e encaminha os relatos de bugs direto para o sprint em vez de deixá-los na fila. O prazo de entrega cai para menos de dois dias sem nova contratação, e usa o orçamento liberado no gargalo real.

**Grande empresa.** Uma plataforma de pagamentos que dimensiona seu serviço de autorização mede λ ≈ 850 requisições/segundo e μ ≈ 200/segundo por nó. Ingenuamente são ~5 nós (ρ = 0,85), mas sabendo que ρ = 0,85 já significa latência de cauda acentuadamente elevada, a equipe provisiona para ρ ≈ 0,65 e usa a Lei de Little para prever o número de requisições em andamento e definir profundidades de fila e timeouts. Os incidentes de alta temporada que costumavam aparecer “do nada” desaparecem, porque a equipe já não operava na parte íngreme da curva.

**Governo.** A central de atendimento de uma agência tributária modela o suporte da temporada de declarações como uma fila: picos de chegada (λ), capacidade dos atendentes (μ) e, criticamente, a **taxa de pulo (σ)** dos cidadãos que desistem depois de longas esperas. Acompanhando balking e reneging e não apenas “chamadas atendidas”, a liderança vê a demanda não atendida verdadeira, dota de pessoal para manter a utilização longe do precipício nos picos e justifica a capacidade extra com estimativas de tempo de espera pela Lei de Little, um caso defensável e apoiado em matemática para o gasto público e não anedótico.

## Justificativa de negócio: motivações, ROI e TCO

A teoria das filas compensa ao prevenir dois erros caros: o **superprovisionamento** (pagar por capacidade ociosa de que não se precisava) e, muito mais danoso, o **subprovisionamento perto do precipício** (onde pequenos aumentos de carga causam grande latência, SLAs violados, clientes que desistem e gasto de emergência). Como o custo de rodar perto de 100% de utilização é não linear, a economia de “só pôr um pouquinho mais de carga” é pequena e o prejuízo é catastrófico, exatamente a assimetria que um pouco de matemática transforma numa decisão deliberada. O retorno se mede em quedas evitadas, SLAs cumpridos, clientes retidos que de outro modo desistiriam e rodízios de sobreaviso mais calmos.

No **custo total de propriedade**, o arcabouço é barato de adotar (é conhecimento, não ferramenta) e melhora quase toda decisão de capacidade, latência e fluxo que uma grande organização toma ao longo da vida de um sistema. A Lei de Little e os limites de WIP reduzem os prazos de entrega sem comprar nada (uma vitória puramente de processo), enquanto a disciplina de utilização troca um custo modesto e previsível em regime estável pela eliminação de falhas caras e imprevisíveis. Para defender o caso junto à liderança, traduzam um incidente recente de latência na curva de utilização e mostrem como uma meta de folga o teria prevenido, e usem a Lei de Little para ligar diretamente a redução do WIP à entrega mais rápida.

## Antipadrões e armadilhas

- **Planejar a capacidade em torno de médias:** ignorar a variância, que é o que de fato cria filas.
- **Rodar quente:** mirar em 90%+ de utilização em sistemas sensíveis à latência e se chocar com a latência de cauda.
- **Contar pulos como atendimento:** tratar clientes que desistem ou chamados rejeitados como tratados, corrompendo as métricas.
- **Empilhar WIP:** confundir estar ocupado com vazão e alongar os prazos de entrega.
- **Otimizar o que não é gargalo:** melhorar estágios que não restringem e mover a fila para outro lugar.
- **Confundir os MTTRs:** relatar “recuperação” medindo “reparo”, ou vice-versa.
- **Filas ilimitadas:** sem contrapressão, então um sistema sobrecarregado se degrada até o colapso em vez de descartar carga.
- **Médias como máximos:** projetar para a média e ser acionado pela cauda.

## Modelo de maturidade

- **Nível 1, Iniciar:** As filas (chamados, tarefas, mensagens, implantações) são não gerenciadas e reativas; a capacidade é chutada; a utilização roda onde a carga cair; os problemas de latência surpreendem a equipe e são combatidos depois do fato.
- **Nível 2, Desenvolver:** Algumas equipes coletam métricas básicas (vazão, espera média) mas as leem como médias e as aplicam de modo inconsistente; alguns grupos limitam o WIP ou deixam folga enquanto outros rodam quentes; não há notação compartilhada, então as práticas não viajam entre as equipes.
- **Nível 3, Padronizar:** Uma notação comum (λ, μ, ρ, prazo de entrega) é documentada e imposta em toda a organização; os limites de WIP e as metas de folga de utilização são definidos deliberadamente para todo sistema sensível à latência; os vários MTTRs são distinguidos; filas limitadas com contrapressão são o padrão entre os serviços.
- **Nível 4, Gerenciar:** As filas são medidas e controladas em relação a linhas de base: taxa de chegada, taxa de atendimento, utilização, latência de cauda (p95/p99) e prazo de entrega são acompanhados contra metas e SLOs definidos; profundidades de fila, timeouts e folga são derivados da Lei de Little e não chutados; balking, reneging e taxa de pulo são contados para que a carga oferecida se distinga da carga atendida; as decisões de capacidade são revisadas com base nessa evidência, não na intuição.
- **Nível 5, Orquestrar:** O fluxo é modelado continuamente como uma fila de filas; os gargalos são identificados e aliviados como prática contínua; a capacidade, os SLOs e a contrapressão se adaptam à demanda e à variância cambiantes; as métricas de fila se ligam diretamente às métricas DORA e aos KPIs de negócio, e a organização reequilibra a capacidade ao longo do fluxo inteiro conforme o quadro de carga e risco muda.

## Ideias para discussão

1. Em que utilização os seus sistemas sensíveis à latência estão de fato rodando, e onde fica o precipício deles?
2. Apliquem a Lei de Little ao seu backlog atual: que prazo de entrega o seu WIP ÷ vazão implica, e combina com a realidade?
3. Quais das suas filas contam em silêncio “pulos” (abandonos, rejeições) como se tivessem sido atendidos?
4. Onde baixar o WIP encurtaria o prazo de entrega de modo mais barato que acrescentar capacidade?
5. Qual estágio do seu fluxo da ideia à produção é o verdadeiro gargalo, e as suas melhorias miram ali?
6. Os seus painéis mostram médias onde a cauda é o que de fato dói?

## Principais conclusões

- As filas de clientes, os quadros kanban, as filas de mensagens e os pipelines de implantação são todos filas regidas pelas mesmas leis.
- A **Lei de Little (κ = λτ)** ancora o planejamento de fluxo: prazo de entrega = WIP ÷ vazão.
- Utilização e tempo de espera são **não lineares**: provisionem folga; os últimos 15% são os mais caros.
- Acompanhem o quadro completo: chegadas, atendimento, sucessos, **falhas e pulos** e esperas; não deixem o abandono se esconder.
- Modelem os processos como uma **fila de filas** e consertem o **gargalo**, não o trabalho de enchimento.
- As métricas de fila mapeiam-se diretamente nas medidas **DORA/de fluxo** e **SLI/SLO** (capítulos 11.1, 11.2, 9.1), dando a toda a organização uma só linguagem para capacidade e fluxo.

## Referências e leitura complementar

- Bob Wescott, *Seven Insights into Queueing Theory* (and *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Little's Law.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: flow-based DORA metrics that align with queue KPIs.
- Donald Reinertsen, *The Principles of Product Development Flow*: queues, batch size, and WIP economics.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Little's Law applied to kanban.
- Joel Parker Henderson, *Queueing Theory*: notation, KPIs, and queue-of-queues (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
