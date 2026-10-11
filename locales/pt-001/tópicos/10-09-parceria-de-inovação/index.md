# 10.9 Parceria de inovação

## Visão geral e motivação

Uma parceria de inovação é uma colaboração deliberada entre a sua organização e uma parte externa (uma startup, um fornecedor, uma universidade, um laboratório de pesquisa, um [consórcio](https://en.wikipedia.org/wiki/Consortium) ou uma agência pública) para desenvolver uma capacidade que nenhum dos dois construiria tão bem sozinho. Vai de arranjos leves (pilotos, pesquisa conjunta, colaboração em código aberto) a profundos (codesenvolvimento, [joint ventures](https://en.wikipedia.org/wiki/Joint_venture), [capital de risco corporativo](https://en.wikipedia.org/wiki/Corporate_venture_capital) e os procedimentos formais de contratação de “parceria de inovação” hoje escritos na lei pública). O fio comum é dividir risco, conhecimento e recompensa para chegar a uma inovação mais depressa ou a menor custo do que o esforço interno ou uma compra de prateleira permitiriam. Este capítulo fica na parte de gestão porque decidir quando e como fazer parceria para inovar é uma decisão de portfólio e de contratação (capítulos 10.1, 10.3) tanto quanto técnica.

Eis a motivação. Nenhuma grande organização pode construir tudo, então a pergunta de “construir versus comprar” (capítulo 6.1) tem uma terceira opção crucial: *fazer parceria*. Quando uma capacidade é nova demais para comprar de prateleira, distante demais do núcleo para construir bem internamente ou arriscada demais para financiar sozinho, uma parceria pode transformar uma aposta incerta numa compartilhada e em estágios. As parcerias também importam talento, tecnologia e pensamento novo que as organizações estabelecidas têm dificuldade de cultivar por conta própria, o antídoto clássico ao problema de inovação da incumbente. Bem feitas, ampliam o seu alcance e a sua velocidade. Mal feitas, produzem o “purgatório dos pilotos” (pilotos que têm sucesso mas nunca chegam à produção), [propriedade intelectual](https://en.wikipedia.org/wiki/Intellectual_property) (PI) vazada e dependência de um parceiro cujos incentivos divergem dos seus.

Para empresas e governos, as apostas e os mecanismos são distintos. As empresas usam braços de capital de risco corporativo, aceleradoras e acordos de codesenvolvimento para ficar perto da tecnologia emergente. Os governos construíram instrumentos formais para o mesmo fim. O procedimento de contratação de *parceria de inovação* da União Europeia permite a um comprador público desenvolver e depois adquirir uma solução ainda inexistente. O programa americano [Small Business Innovation Research](https://en.wikipedia.org/wiki/Small_Business_Innovation_Research) (SBIR) e os mecanismos de desafios e prêmios financiam inovação externa para missões públicas. Os programas de “GovTech” fazem parceria entre agências e startups. Eles existem precisamente porque a contratação normal (capítulo 10.3) compra o que já existe, enquanto as missões públicas precisam cada vez mais do que ainda não existe.

## Princípios fundamentais

- **Façam parceria quando não conseguem nem comprar nem construir bem sozinhos.** É a terceira opção, escolhida deliberadamente.
- **Alinhem primeiro os incentivos.** Uma parceria só funciona se os dois lados ganham com o mesmo resultado.
- **Escalonem o risco.** Financiem em incrementos atrelados a marcos validados, não em um grande compromisso.
- **Resolvam PI, dados e saída de antemão.** As conversas mais difíceis são as mais baratas antes de assinar.
- **Protejam o núcleo, abram as bordas.** Compartilhem o suficiente para colaborar, não o suficiente para se esvaziar.
- **Levem os pilotos à produção deliberadamente.** Um piloto que não escala é uma demonstração, não uma parceria.
- **Gerenciem a relação, não só o contrato.** Confiança e governança a sustentam, não a papelada.

## Recomendações

### Escolha o modelo de parceria que se ajusta ao objetivo

Objetivos diferentes pedem estruturas diferentes; escolham a mais leve que o alcance:

- **Pilotos e [provas de conceito](https://en.wikipedia.org/wiki/Proof_of_concept):** testes baratos e com tempo fixo da tecnologia de uma startup ou fornecedor contra um problema real.
- **Acordos de codesenvolvimento / desenvolvimento conjunto:** construção compartilhada de uma capacidade específica, com contribuições definidas e divisão de PI.
- **Parcerias de pesquisa:** com universidades ou laboratórios, para capacidade ainda pré-produto.
- **Capital de risco corporativo (CVC) e aceleradoras:** participações acionárias ou programas em coortes para ficar perto da tecnologia e do talento emergentes.
- **Consórcios e colaboração em código aberto:** investimento compartilhado em infraestrutura não diferenciadora (capítulo 10.3).
- **Instrumentos públicos de inovação:** parcerias de inovação da UE, SBIR/STTR, desafios e prêmios e programas de GovTech para missões em que a solução precisa ser criada.

### Alinhe os incentivos e governe a relação

A causa mais comum do fracasso de parcerias é o incentivo desalinhado vestido num contrato alinhado. Antes de definir uma estrutura, perguntem o que cada parte de fato quer (receita, acesso a mercado, um cliente de referência, produção de pesquisa, impacto na missão) e confirmem que o *mesmo* resultado faz os dois lados ganharem. Depois governem a relação ativamente: um roteiro compartilhado, revisões conjuntas regulares, direitos de decisão claros e donos responsáveis nomeados de cada lado (aplicam-se as disciplinas de ADR, registro de decisão de arquitetura, e de governança dos capítulos 1.5–1.6). As parcerias vivem ou morrem de confiança e comunicação muito mais que de cláusulas contratuais.

### Resolva PI, dados, segurança e saída antes de assinar

As conversas que vocês mais querem adiar são exatamente as que devem ter primeiro: quem é dono da propriedade intelectual, quem pode usar os dados, como as obrigações de segurança e de conformidade fluem para o parceiro e como cada lado sai. A propriedade de PI não resolvida envenena um codesenvolvimento que de outro modo teria sucesso. O compartilhamento de dados não gerenciado cria exposição de privacidade e de segurança (capítulos 4.5, 4.3). A ausência de plano de saída cria aprisionamento (lock-in). Tratem um parceiro como parte da sua cadeia de suprimentos para fins de risco e de garantia (capítulo 10.2), incluindo a revisão de segurança de terceiros.

### Escalone o investimento e vença o purgatório dos pilotos

Financiem as parcerias de inovação como bons investidores financiam startups: em estágios, cada parcela liberada contra marcos validados (a disciplina de descoberta do capítulo 11.1). Isso limita a perda nas muitas apostas que não vão dar certo e preserva o ganho nas poucas que vão. A armadilha empresarial específica é o *purgatório dos pilotos*: um cemitério de pilotos bem-sucedidos que nunca chegam à produção porque ninguém é dono do caminho até a escala, do orçamento ou do trabalho de integração. Projetem o caminho de produção desde o início. Nomeiem o dono interno que operacionalizará um piloto bem-sucedido e tratem “isto consegue escalar para o nosso patrimônio?” como uma pergunta de portão e não como reflexão tardia.

### Proteja o núcleo enquanto abre as bordas

Façam parceria mais livremente em capacidades não diferenciadoras e em pesquisa pré-competitiva e guardem as suas fontes genuínas de vantagem. Compartilhem contexto, dados e acesso suficientes para o parceiro ter sucesso. Mas estruturem a relação para não transferir o seu valor central nem ficar dependente de uma única parte externa para algo crítico à missão (risco de concentração, capítulo 10.2). O objetivo é importar inovação nas bordas sem esvaziar o centro.

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| **Fazer parceria (codesenvolver)** | Risco compartilhado. Talento e tecnologia importados. Mais rápido que construir | Complexidade de PI e de incentivos. Custo de coordenação. Dependência |
| **Construir internamente** | Controle total e PI. Ajuste profundo | Lento. Pode faltar talento ou novidade. Custo de oportunidade |
| **Comprar de prateleira** | Rápido, comprovado, com suporte | Só compra o que existe. Commoditizado, sem vantagem |
| **Participação acionária / CVC** | Perto da tecnologia emergente. Potencial de ganho | Distração. Horizontes desalinhados. Carga de governança |
| **Procedimentos públicos de inovação (IP da UE, SBIR)** | Desenvolvem legalmente o ainda inexistente. Ajuste à missão | Complexidade procedimental. Ciclos longos. Fardo administrativo |

A tensão definidora é **abertura versus proteção**. As parcerias de inovação exigem compartilhar conhecimento, dados e acesso, mas a mesma abertura pode vazar vantagem ou criar dependência. A solução é um escopo deliberado, ser generoso nas bordas não diferenciadoras e disciplinado quanto ao núcleo, mais um compromisso escalonado, para que a confiança e o valor sejam provados antes de a exposição se aprofundar.

## Perguntas para discutir com sua equipe

1. **Financiamos as parcerias de inovação como um portfólio escalonado com uma taxa de fracasso deliberadamente alta, ou apostamos pesado em cada uma?** As boas parcerias se comportam como apostas de capital de risco: a maioria fracassa, algumas poucas pagam por tudo, e o jeito de sobreviver a essa conta é financiar em parcelas liberadas contra marcos validados. Um único grande compromisso inicial elimina a sua opção de sair barato, que é a principal vantagem de fazer parceria sobre construir. Para uma empresa ou agência que roda várias parcerias ao mesmo tempo, definam um orçamento explícito que espere que a maioria dos pilotos termine e alguns poucos escalem. Levem o gasto em parcerias do ano passado, quantas apostas vocês financiaram e quantas chegaram à produção. Se toda parceria foi um compromisso de uma vez só, sem estágios, vocês estão carregando uma perda que poderiam ter limitado.

2. **Antes de assinar, confirmamos que os dois lados ganham com o mesmo resultado, e quem governa a relação depois?** A causa mais comum do fracasso de parcerias é o incentivo desalinhado vestido num contrato alinhado. Perguntem o que cada parte de fato quer (receita, um cliente de referência, produção de pesquisa, impacto na missão) e confirmem que o mesmo resultado faz os dois lados terem sucesso. Depois decidam quem governa a relação após a assinatura: donos responsáveis nomeados de cada lado, um roteiro compartilhado e revisões conjuntas regulares, porque as parcerias vivem de confiança e comunicação muito mais que de cláusulas. Registrem os direitos de decisão como registrariam uma decisão de arquitetura. Cheguem com o incentivo real de cada parte escrito com clareza, e se eles não apontam para o mesmo resultado, consertem a estrutura antes de se comprometer.

3. **Tratamos os parceiros como parte da nossa cadeia de suprimentos para fins de segurança e de risco de concentração?** Um parceiro com acesso aos seus dados e sistemas é um terceiro, e as fraquezas dele viram as suas. Rodem a mesma revisão de segurança e diligência prévia que aplicam a qualquer fornecedor e resolvam direitos de dados, obrigações de segurança e saída antes de o trabalho começar, porque essas são as conversas mais baratas antes de assinar e as mais envenenadas depois. Atentem ao risco de concentração: uma capacidade crítica à missão presa a um único parceiro externo é uma dependência, não uma parceria. Levem um mapa do que cada parceiro pode acessar e do que quebraria se ele falhasse ou fosse embora. Se algum parceiro isolado guarda algo que vocês não conseguiriam substituir, projetem a saída agora.

4. **Para cada piloto que financiamos, quem é dono do caminho até a produção, e que integração e orçamento a escala de fato exige?** O purgatório dos pilotos é a falha característica da inovação das grandes organizações: pilotos que têm sucesso tecnicamente, impressionam um patrocinador e depois morrem porque ninguém foi dono do trabalho sem glamour de escalá-los para dentro do patrimônio. A atração contrária é real, já que nomear um dono de produção e reservar orçamento de integração de antemão parece prematuro quando a maioria dos pilotos fracassará de qualquer modo, mas sem isso até os vencedores empacam. Levem a contagem de pilotos que vocês rodaram no ano passado, quantos chegaram à produção e, para os sobreviventes, o custo de integração e o dono interno pelo nome. Para uma empresa, o bloqueio costuma ser a integração ao patrimônio e o ajuste à plataforma; para uma agência, é a contratação subsequente e a linha orçamentária que precisam existir antes de o piloto terminar, ou o protótipo bem-sucedido não tem onde pousar.

5. **O que exatamente estamos dispostos a compartilhar, e onde fica a linha que protege a nossa vantagem central?** As parcerias só funcionam se vocês compartilham contexto, dados e acesso suficientes para o parceiro ter sucesso, e a mesma abertura pode vazar a própria capacidade que diferencia vocês. A tensão é genuína: um escopo apertado demais e o parceiro não consegue entregar, solto demais e vocês entregam a sua vantagem ou criam uma dependência que não conseguem desfazer. Levem um inventário explícito do que é não diferenciador e seguro de abrir, do que é núcleo e permanece protegido e de quais conjuntos de dados carregam limites de privacidade ou contratuais ao compartilhamento. Numa empresa, essa linha deve se mapear para a sua estratégia de risco de concentração e de PI; no governo, acrescentem as obrigações de transparência e de concorrência justa que podem exigir compartilhar de modo mais aberto com todos os licitantes enquanto se protegem os dados dos cidadãos e se evita o aprisionamento a um fornecedor.

6. **Ajustamos cada parceria ao modelo mais leve que alcança o objetivo, incluindo os instrumentos públicos de inovação disponíveis para nós?** A estrutura carrega custo e risco reais, e as equipes costumam recorrer por padrão a um veículo pesado (participação acionária, uma joint venture, um acordo de codesenvolvimento de vários anos) quando um piloto com tempo fixo ou um acordo de pesquisa responderia à pergunta de modo mais barato. Pesem a carga de coordenação, o fardo de governança e a dificuldade de saída de cada modelo contra quanta certeza vocês de fato precisam antes de se comprometer. Levem o objetivo declarado com clareza (receita, capacidade, acesso a talento, resultado da missão), a estrutura mais curta que poderia testá-lo e o custo de saída da estrutura que vocês propõem. Para um órgão público, essa também é uma questão legal: instrumentos como o procedimento de parceria de inovação da UE, os prêmios SBIR/STTR e os prêmios de desafio existem precisamente para permitir desenvolver e depois comprar o que ainda não existe, e escolher o certo mantém a contratação legal, competitiva e auditável.

## Perspectiva por setor

**Startup.** Façam parceria para tomar emprestado o que vocês não podem bancar construir: hardware, ciência de domínio, distribuição ou um cliente de referência. Mantenham todo acordo com tempo fixo e barato de sair, porque o seu recurso mais escasso é a atenção da engenharia e um compromisso de codesenvolvimento que vocês não conseguem manter com equipe afundará a empresa mais depressa que a capacidade que falta. Resolvam por escrito a PI e a propriedade dos clientes antes do primeiro sprint, já que entregar o seu núcleo numa parceria inicial é um erro que não se recompra.

**Pequena empresa.** Sem braço de capital de risco corporativo nem equipe de inovação, tratem a parceria como um atalho de comprar versus construir e não como uma estratégia: achem um fornecedor, laboratório ou universidade local disposto a rodar um pequeno piloto pago sobre um problema concreto. Atentem ao risco de concentração, porque um único parceiro que guarda uma capacidade de que vocês dependem é uma ameaça maior para uma firma pequena que para uma grande. Prefiram parceiros que deixem vocês donos dos seus dados e capazes de ir embora sem reescrever as operações.

**Grande empresa.** A tarefa é a governança de portfólio entre muitas equipes: um manual compartilhado de parcerias cobrindo a escolha do modelo, o financiamento escalonado por marcos, os termos de PI, dados e saída, a revisão de segurança de terceiros e um dono de produção nomeado para cada piloto. Padronizem a interface e a camada de integração para que um piloto bem-sucedido tenha onde pousar e gerenciem as parcerias como um livro de opções escalonadas com uma taxa de fracasso deliberadamente alta e não como um amontoado de anúncios. Orcem explicitamente o trabalho de escala, porque o purgatório dos pilotos é onde o dinheiro de inovação das empresas desaparece em silêncio.

**Governo.** A contratação, a transparência e a prestação de contas públicas moldam toda parceria. Usem os instrumentos formais feitos para isso (o procedimento de parceria de inovação da UE, SBIR/STTR, desafios e prêmios) para poder financiar legalmente fornecedores que desenvolvam o que ainda não existe e depois adquirir o melhor em escala. Mantenham a concorrência justa e o processo auditável, insistam em termos de PI e de dados que previnam o aprisionamento a um único fornecedor e publiquem o suficiente sobre o arranjo para satisfazer o escrutínio público enquanto protegem os dados dos cidadãos.

## Exemplos

**Startup.** Uma startup de dados climáticos de quatro pessoas não tem o hardware de sensores nem a ciência de domínio para validar seus modelos sozinha, então faz parceria com um laboratório universitário num piloto de pesquisa conjunta com tempo fixo. Resolvem os termos primeiro: o laboratório publica a ciência, a startup guarda seu software e suas relações com clientes e cada estágio do financiamento depende de atingir um marco compartilhado e combinado. Como a startup nomeia um fundador como dono de transformar qualquer resultado promissor numa funcionalidade entregável, o piloto produz um incremento real de produto em vez de um artigo juntando poeira.

**Grande empresa.** Uma empresa de logística quer uma capacidade de otimização de rotas que nenhum fornecedor vende e que a própria equipe não consegue construir depressa. Roda uma parceria escalonada de codesenvolvimento com uma startup de IA: um piloto pago sobre dados reais (anonimizados), financiamento atrelado a marcos, uma divisão clara de PI (a startup guarda seu modelo central; a empresa é dona da integração e dos próprios dados) e um dono interno nomeado responsável por escalar um piloto bem-sucedido para a produção. Como o caminho de produção é projetado desde o início, o piloto escapa do purgatório dos pilotos e entra no ar. A estrutura escalonada limita a perda nos pilotos anteriores que não deram certo.

**Governo.** Uma agência de transporte precisa de um sistema de previsão de congestionamento que ainda não existe. Em vez de comprar a coisa errada ou tentar construí-lo internamente, usa um procedimento de parceria de inovação ao estilo da UE (ou, nos EUA, um prêmio SBIR) para financiar vários fornecedores a desenvolver protótipos concorrentes e depois adquire o melhor em escala, comprando legalmente uma inovação que precisava ser criada. Salvaguardas de interesse público se aplicam o tempo todo: transparência, concorrência justa, acessibilidade e direitos claros de PI e de dados que impeçam a agência de ficar presa a um fornecedor (capítulos 10.3, 10.5).

## Justificativa de negócio: motivações, ROI e TCO

O retorno das parcerias de inovação é **opcionalidade e velocidade**. Pelo custo de um piloto escalonado, vocês compram uma opção real sobre uma capacidade que não teriam conseguido comprar nem construir tão depressa, e podem ir embora barato se a aposta falhar. Comparem com construir, que compromete o custo integral de início contra uma capacidade interna incerta, e com comprar, que não consegue adquirir o que ainda não existe. Fazer parceria costuma ter o melhor retorno ajustado ao risco quando a capacidade é nova, não central ou arriscada demais para financiar sozinho. O talento e a tecnologia importados também se compõem: as organizações que fazem boas parcerias ficam mais perto da fronteira do que as que apenas constroem ou compram.

No **custo total de propriedade**, os custos visíveis são coordenação, governança e as muitas apostas que não se pagam. Os custos ocultos são o vazamento de PI, a exposição de segurança e a dependência quando as parcerias são estruturadas com descuido. Escalonar o investimento e resolver de antemão PI, dados e saída é o que mantém o TCO sob controle. O maior custo silencioso é o *purgatório dos pilotos*, dinheiro real gasto em pilotos que nunca escalam, e é por isso que o caminho de produção e um dono interno responsável pertencem ao argumento de negócio desde o primeiro dia. Para defender o caso junto à liderança, enquadrem as parcerias como um portfólio de opções baratas e escalonadas sobre capacidade, explicitamente orçado para uma alta taxa de fracasso e algumas poucas vitórias descomunais, com uma regra rígida: nenhum piloto é financiado sem um dono nomeado para escalá-lo.

## Antipadrões e armadilhas

- **Purgatório dos pilotos:** um cemitério de pilotos bem-sucedidos que nunca chegam à produção.
- **Teatro da inovação:** parcerias anunciadas pela imagem, sem intenção real de integração.
- **PI não resolvida:** adiar as questões de propriedade até envenenarem uma colaboração em andamento.
- **Desalinhamento de incentivos:** um contrato assinado mascarando partes que querem resultados diferentes.
- **Vazamento do núcleo:** compartilhar nas bordas capacidade ou dados genuinamente diferenciadores.
- **Dependência de um só parceiro:** capacidade crítica à missão presa a uma única parte externa.
- **Compromisso de uma vez só:** financiar uma grande parceria numa parcela única em vez de escalonar por marcos.
- **Contrato acima da relação:** confiar às cláusulas o trabalho que a governança e a confiança devem fazer.

## Modelo de maturidade

- **Nível 1, Iniciar.** A inovação é só construir ou comprar. As parcerias externas são ad hoc, guiadas por personalidades e reativas. PI, incentivos e escala são resolvidos caso a caso, e os pilotos raramente chegam à produção.
- **Nível 2, Desenvolver.** Rodam alguns pilotos, vínculos de pesquisa e colaborações com fornecedores, e algumas pessoas aprenderam a escalonar o financiamento e a resolver termos, mas a prática é inconsistente de equipe para equipe. O purgatório dos pilotos é comum e depende de quem conduz o acordo.
- **Nível 3, Padronizar.** Um manual deliberado de parcerias é documentado e imposto em toda a organização: escolha do modelo, financiamento escalonado por marcos, termos de PI, dados e saída, donos de produção nomeados e revisão de segurança de terceiros são aplicados de modo consistente a toda parceria.
- **Nível 4, Gerenciar.** As parcerias são medidas contra linhas de base: taxa de conversão de piloto em produção, custo e tempo por aposta escalonada, taxa de fracasso do portfólio versus algumas vitórias descomunais, exposição de saída e de concentração e PI realizada. Os portões de marcos são impostos com base nessa evidência, e as decisões de ir ou não ir e de escala são conduzidas pelas métricas e não pela advocacia.
- **Nível 5, Orquestrar.** A parceria é integrada à estratégia de portfólio, de contratação e de risco e continuamente melhorada. A organização é um parceiro de escolha que abre de forma adaptativa as bordas certas, aposenta e redefine o escopo das parcerias conforme a fronteira se desloca e converte de modo confiável a inovação externa em capacidade entregue.

## Ideias para discussão

1. Na sua última decisão de “construir versus comprar”, “fazer parceria” estava genuinamente em jogo?
2. Quantos dos seus pilotos chegaram à produção no ano passado, e quem foi dono do caminho até a escala?
3. Os seus contratos de parceria resolvem PI, direitos de dados e saída antes de o trabalho começar?
4. Onde vocês podem estar compartilhando vantagem central nas bordas sem perceber?
5. Alguma capacidade crítica à missão depende de um único parceiro externo?
6. Num contexto do setor público, quais instrumentos de inovação (parcerias da UE, SBIR, desafios) se ajustam à sua missão?

## Principais conclusões

- A parceria de inovação é a terceira opção deliberada além de construir e comprar: colaborar para dividir risco, conhecimento e recompensa.
- **Escolham o modelo para se ajustar ao objetivo**, de pilotos ao codesenvolvimento e aos procedimentos públicos de inovação (parcerias de inovação da UE, SBIR).
- **Alinhem os incentivos, resolvam PI, dados e saída de antemão** e governem a relação, não só o contrato.
- **Escalonem o investimento** e projetem o caminho de produção para escapar do **purgatório dos pilotos**.
- **Protejam o núcleo, abram as bordas:** importem inovação sem vazar vantagem nem criar dependência.
- O ROI é opcionalidade e velocidade. Vejam os capítulos 10.3 (contratação), 10.1 (portfólio), 10.2 (risco de terceiros) e 6.1 (construir, comprar ou fazer parceria para IA).

## Referências e leitura complementar

- Henry Chesbrough, *Open Innovation* and *Open Business Models*.
- Clayton Christensen, *The Innovator's Dilemma* (why incumbents struggle to innovate internally).
- European Union, Directive 2014/24/EU, the *innovation partnership* procurement procedure.
- U.S. Small Business Administration, *Small Business Innovation Research (SBIR/STTR)* programme.
- Vijay Govindarajan and Chris Trimble, *The Other Side of Innovation* (executing innovation, beating pilot purgatory).
- Ronald Adner, *The Wide Lens* (innovation ecosystems and partner dependencies).
- GovTech and public-sector innovation resources (e.g., GDS, USDS, Public Digital); see chapter 10.3.
