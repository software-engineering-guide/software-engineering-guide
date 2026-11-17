# 5.3 Acessibilidade

## Visão geral e motivação

A [acessibilidade](https://en.wikipedia.org/wiki/Accessibility) (muitas vezes abreviada como “a11y”) é a prática de construir software que pessoas com deficiência possam perceber, entender, navegar e usar. Isso inclui pessoas cegas ou com baixa visão, surdas ou com dificuldade de audição, com deficiências motoras, com diferenças cognitivas ou de aprendizado e que enfrentam limites temporários ou situacionais, como um braço quebrado, a luz forte do sol ou uma sala barulhenta. Aproximadamente uma em cada cinco pessoas tem uma deficiência, e todos se beneficiam de um design acessível em algum momento. Isso não é uma acomodação de nicho. É uma linha de base de qualidade.

Para grandes equipes, a acessibilidade precisa ser embutida no sistema, não deixada às boas intenções individuais. Quando muitas equipes entregam num único produto, um único componente inacessível (um campo de formulário sem rótulo, um indicador de status só por cor, uma armadilha de teclado num modal) pode trancar usuários com deficiência fora de uma jornada inteira. Embutir a acessibilidade em componentes compartilhados, tokens de design, pipelines de teste e definições de pronto é a única maneira de torná-la confiável em escala. Adaptá-la depois do fato é caro e propenso a erros. Projetá-la desde o início é barato e durável.

Para o governo, a acessibilidade é uma exigência legal e uma obrigação cívica, não um extra desejável. Os serviços públicos precisam atender a todos os membros do público, e os cidadãos com deficiência muitas vezes não têm provedor alternativo: se o site do governo é inacessível, eles não conseguem obter seu benefício, sua licença ou votar de outro modo. Leis e padrões no mundo todo tornam a acessibilidade obrigatória para os órgãos públicos e cada vez mais também para o setor privado. Este capítulo trata a acessibilidade como três coisas ao mesmo tempo: um dever legal, um dever ético e simplesmente bom design.

*Veja também:* o capítulo 5.2 (design de UI e sistemas de design), o capítulo 5.6 (engenharia de front-end) e o capítulo 5.1 (fundamentos de UX).

## Princípios fundamentais

- A acessibilidade é um atributo de qualidade de base, como a segurança e o desempenho, não uma funcionalidade opcional.
- Os princípios POUR: as interfaces devem ser Perceptíveis, Operáveis, Compreensíveis e Robustas.
- Primeiro o [HTML semântico](https://en.wikipedia.org/wiki/Semantic_HTML). Usem o [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) apenas para preencher lacunas genuínas, nunca como substituto de elementos nativos.
- Tudo que é utilizável com um mouse precisa ser utilizável só com o teclado.
- Não transmitam informação apenas por cor, forma ou posição.
- As ferramentas automatizadas pegam só uma fração dos problemas. Os testes manuais e com [tecnologia assistiva](https://en.wikipedia.org/wiki/Assistive_technology) são essenciais.
- O design acessível é melhor para todos (o [“efeito calçada rebaixada”](https://en.wikipedia.org/wiki/Curb_cut), em que funcionalidades feitas para pessoas com deficiência beneficiam todos os usuários).
- Projetem e testem com pessoas com deficiência, não apenas para elas.

## Recomendações

### Projete e construa conforme a WCAG, mirando o padrão atual

As [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) são a referência internacional. A WCAG 2.1 e a 2.2 são organizadas sob os quatro princípios POUR, com critérios de sucesso testáveis nos níveis de conformidade A, AA e AAA. Mirem o Nível AA como linha de base. É o que a maioria das leis referencia. A WCAG 2.2 acrescenta critérios para a visibilidade do foco, o tamanho dos alvos e a redução da carga cognitiva. A WCAG 3.0 é uma sucessora emergente, estruturada de modo diferente e ainda em desenvolvimento. Fiquem de olho, mas construam hoje para a 2.2 AA. Tratem as diretrizes como piso e não como teto: passar em todos os critérios não garante uma experiência genuinamente utilizável.

### Use HTML semântico e ARIA correto

Os elementos nativos do HTML (botões, links, controles de formulário, títulos, listas, marcos) vêm com semântica de acessibilidade embutida, comportamento de teclado e suporte a tecnologias assistivas. Usem-nos primeiro. Recorram aos papéis, estados e propriedades do ARIA (Accessible Rich Internet Applications) apenas para descrever widgets personalizados que o HTML não consegue expressar e sigam as ARIA Authoring Practices. A primeira regra do ARIA é simples: não usem ARIA se um elemento nativo servir. O ARIA incorreto é pior que nenhum: engana ativamente os [leitores de tela](https://en.wikipedia.org/wiki/Screen_reader). Deem à página uma estrutura lógica de títulos, rótulos significativos, texto alternativo para imagens, legendas e transcrições para mídia e uma ligação programática entre cada rótulo e seu controle.

### Garanta a operabilidade por teclado e por tecnologia assistiva

Todo elemento interativo precisa ser alcançável e operável só com o teclado, numa ordem lógica, com um indicador de foco claramente visível. Evitem armadilhas de teclado. Gerenciem o foco deliberadamente quando o conteúdo muda: movam o foco para uma caixa de diálogo quando ela abre, devolvam-no quando ela fecha e anunciem as atualizações dinâmicas por regiões ativas (live regions). Testem com tecnologias assistivas reais, incluindo leitores de tela no computador e no celular, ampliação de tela, controle por voz e acesso por chave (switch). E respeitem preferências do usuário como movimento reduzido e contraste aumentado.

### Teste com ferramentas automatizadas, revisão manual e usuários reais

Os varredores automatizados de acessibilidade são valiosos e devem rodar no pipeline a cada mudança. Mas os estudos mostram consistentemente que eles pegam só uma minoria dos problemas reais, cerca de um terço. O resto exige julgamento humano: percursos por teclado, testes com leitor de tela, verificações de contraste e a pergunta de se o conteúdo é de fato compreensível. O mais importante de tudo: incluam pessoas com deficiência nos testes de usabilidade. Embutam critérios de aceitação de acessibilidade na definição de pronto, para que os problemas sejam pegos por história e não numa auditoria pré-lançamento.

### Torne a acessibilidade organizacional, não heroica

Embutam a acessibilidade no sistema de design para que os componentes saiam acessíveis por padrão. Ofereçam treinamento para que designers, engenheiros, autores de conteúdo e gerentes de produto saibam cada um pelo que são responsáveis. Estabeleçam um padrão de acessibilidade, um dono ou centro de excelência e um processo de remediação. Publiquem uma declaração de acessibilidade e deem aos usuários um jeito de relatar barreiras. E contratem com acessibilidade: exijam que fornecedores e componentes de terceiros estejam em conformidade e forneçam evidência (como um relatório de conformidade de acessibilidade).

## Compromissos: prós e contras

| Abordagem | Prós | Contras |
|---|---|---|
| Embutir a acessibilidade desde o início | A mais barata, durável, melhor para todos | Exige treinamento e disciplina iniciais |
| Adaptar / remediar depois | Adia o esforço, desbloqueia um lançamento rápido | Muito mais cara, frágil, exposição jurídica no intervalo |
| Apenas testes automatizados | Rápidos, baratos, pegam regressões no CI | Perdem cerca de dois terços dos problemas. Falsa confiança |
| Testes manuais + com tecnologia assistiva | Pegam barreiras reais de usabilidade | Mais lentos, exigem testadores habilidosos e dispositivos |
| Testes com usuários com deficiência | Verdade de campo sobre a experiência real | Esforço e custo de recrutamento. Precisa ser feito com respeito |

A troca central é disciplina inicial versus custo adiado. A acessibilidade embutida é barata e melhora a qualidade para todos. A acessibilidade adaptada sob pressão jurídica é cara, incompleta e estressante. No longo prazo não há troca real com a “velocidade”: o software inacessível simplesmente não funciona para um quinto dos seus usuários. Isso é um defeito, não uma economia.

## Perguntas para discutir com sua equipe

1. **As regressões de acessibilidade falham o nosso build do jeito que um teste quebrado falha, e se não, por quê?** Os varredores automatizados pegam só cerca de um terço dos problemas, mas os que pegam (rótulos ausentes, falhas de contraste, controles sem rótulo) são baratos de pegar no CI e caros de achar numa auditoria pré-lançamento. Tratar uma regressão como falha de build é o que move a acessibilidade de esforço individual heroico para uma propriedade confiável do sistema, que é a única coisa que funciona quando muitas equipes entregam num único produto. Decidam quais verificações são bloqueantes, quais são consultivas e quem pode ignorar uma falha. Levem os resultados atuais do varredor e a sua definição de pronto à reunião. Se os critérios de acessibilidade não estão escritos na definição de pronto por história, eles serão despriorizados no momento em que um prazo apertar.

2. **Qual é a nossa regra para widgets personalizados, e quem revisa o ARIA antes de ele ser entregue?** Os elementos nativos do HTML vêm de graça com comportamento de teclado e suporte a tecnologia assistiva, e o ARIA incorreto é pior que nenhum porque engana ativamente os leitores de tela. Combinem que o HTML semântico é o padrão e que qualquer widget personalizado (um menu suspenso sob medida, um seletor de data ou um modal) exige um percurso por teclado e leitor de tela antes do merge, seguindo as ARIA Authoring Practices. Isso importa mais para os componentes interativos que muitas equipes reutilizam, porque um único modal quebrado com armadilha de teclado pode trancar usuários com deficiência fora de uma jornada inteira. Levem uma lista dos seus widgets personalizados e perguntem quais foram testados com um leitor de tela de verdade. Os que não foram são passivos escondidos no código compartilhado.

3. **Qual é a nossa política sobre as sobreposições de acessibilidade (overlays), e alguém acredita que sejam uma correção real?** As sobreposições são vendidas como um script de uma linha que torna um site conforme, e são tentadoras quando chega a pressão jurídica e um prazo se aproxima. Elas não entregam conformidade genuína, podem piorar a experiência de usuários de tecnologia assistiva e, para o governo, deixam sem cumprir o dever legal subjacente. Decidam explicitamente que vocês investirão em marcação semântica, suporte a teclado e testes com pessoas com deficiência em vez de comprar um widget que disfarça o problema. Levem o custo de uma assinatura de sobreposição e comparem com construir a acessibilidade nos seus componentes e pipeline uma vez. Enquadrar isso cedo previne uma decisão de compra em pânico depois, que gasta dinheiro e não conserta nada.

4. **As pessoas com deficiência fazem parte do nosso design e dos nossos testes, ou ainda projetamos para um usuário imaginário que inventamos?** Os varredores automatizados e até as auditorias de especialistas dizem se a marcação está conforme. Não dizem se um usuário cego consegue de fato terminar o seu checkout ou se uma pessoa com deficiência cognitiva entende as suas mensagens de erro. Envolver participantes com deficiência é a única fonte de verdade de campo, e muda o que vocês constroem, mas levanta questões reais sobre como recrutar com justiça, como remunerar as pessoas pelo tempo delas e como evitar tratar um participante como porta-voz de toda deficiência. Levem a sua lista atual de participantes de pesquisa, suas práticas de recrutamento e de pagamento e uma contagem honesta de quantos estudos do último ano incluíram participantes com deficiência. Para uma grande organização, um painel recorrente com remuneração justa e cobertura de necessidades visuais, auditivas, motoras e cognitivas é o que transforma isso de um gesto pontual numa entrada confiável. No governo, envolver o público que vocês servem costuma fazer parte da obrigação legal e cívica, não de uma gentileza opcional.

5. **Quando compramos ou embutimos um componente de terceiros, exigimos prova de acessibilidade, e quem a confere?** Boa parte do que é entregue num grande produto não é escrita internamente: um seletor de data de uma biblioteca, um widget de pagamentos num iframe, um pacote de gráficos, um módulo SaaS inteiro. Um único componente embutido inacessível pode fazer falhar uma jornada inteira, por mais limpo que seja o seu próprio código, e depois de ligado, substituí-lo é caro. Decidam que a acessibilidade é uma exigência de contratação, que os fornecedores devem entregar um relatório de conformidade de acessibilidade (um documento como o VPAT que declara como um produto se mede contra a WCAG) e que alguém técnico valida a alegação em vez de arquivá-la. Levem um inventário dos seus componentes de terceiros e perguntem quais têm evidência de conformidade atual e crível. Em compras corporativas e governamentais, escrevam no contrato a conformidade com a WCAG 2.2 AA e um direito à remediação, porque uma promessa feita antes de assinar é muito mais barata de impor do que uma barreira descoberta depois de entrar no ar.

6. **Qual é o nosso nível-alvo de conformidade, quem é dono dele e como o mantemos atual à medida que os padrões se movem?** A WCAG 2.2 AA é o piso de hoje e a maioria das leis a referencia, mas a 2.2 acrescentou critérios que muitas equipes não adotaram, e a WCAG 3.0 vem com uma estrutura diferente. Sem um dono nomeado, o padrão deriva: equipes diferentes miram versões diferentes, ninguém acompanha a lacuna e a conformidade apodrece em silêncio entre as auditorias. Decidam a versão e o nível exatos para os quais constroem, quem tem autoridade para elevá-lo e como os novos critérios chegam ao sistema de design e à definição de pronto. Levem o alvo declarado atual, a evidência de onde as equipes de fato o atendem e um curto roteiro para adotar os critérios da 2.2 que vocês pularam. Para uma organização grande ou pública, um dono da acessibilidade ou centro de excelência, uma declaração de acessibilidade publicada e um plano documentado para a próxima versão do padrão são o que permite responder a um regulador ou a um tribunal com evidências e não com boas intenções.

## Perspectiva por setor

**Startup.** A velocidade joga a seu favor aqui, porque a acessibilidade é mais barata quando a base de código é pequena. Acrescentem um varredor automatizado ao CI e um percurso por teclado à lista de verificação dos pull requests desde o primeiro sprint e apoiem-se no HTML semântico para obter de graça o suporte a teclado e a leitor de tela. Pulem as sobreposições e as ferramentas pesadas. O ganho é que, quando a equipe de compras de um cliente pedir um relatório de conformidade no meio de uma venda, vocês poderão responder em dias em vez de correr.

**Pequena empresa.** Sem especialista em acessibilidade e com orçamento apertado, comprem a acessibilidade em vez de construí-la: escolham uma plataforma, tema ou biblioteca de componentes que já esteja em conformidade e o declare, e prefiram fornecedores que publiquem uma declaração de acessibilidade. Cubram vocês mesmos o básico de alto valor com ferramentas gratuitas, verificações só com teclado, um verificador de contraste e rótulos claros em todo campo, porque isso pega as falhas que mais excluem clientes. Tratem um fluxo automatizado errado ou inutilizável como um cliente perdido, já que uma pequena empresa raramente oferece um canal assistido como alternativa.

**Grande empresa.** Em escala o trabalho é fazer da acessibilidade uma propriedade do sistema entre muitas equipes. Entreguem componentes acessíveis por padrão no sistema de design, façam regressões falharem o CI e levantem um dono ou centro de excelência com um processo de remediação e treinamento para designers, engenheiros e autores de conteúdo. Acompanhem a conformidade ao longo do tempo como métrica, escrevam a conformidade com a WCAG na contratação e gerenciem os componentes de terceiros como portfólio para que um widget embutido não faça falhar em silêncio uma jornada compartilhada.

**Governo.** A acessibilidade é um mandato legal e um dever cívico, já que os cidadãos com deficiência muitas vezes não têm provedor alternativo para um benefício, uma licença ou um voto. Construam para o padrão que a sua jurisdição cita (por exemplo a Section 508, a EN 301 549 ou o European Accessibility Act mapeados para a WCAG 2.2 AA), publiquem uma declaração de acessibilidade com um caminho para relatar barreiras e testem com o público com deficiência que vocês servem. Rejeitem as sobreposições como substituto da conformidade real e exijam que os fornecedores entreguem evidência crível e um direito à remediação no contrato.

## Exemplos

**Startup.** Uma startup de três pessoas que constrói uma ferramenta de recrutamento acrescentou um varredor de acessibilidade ao build e um rápido percurso por teclado à lista de verificação dos pull requests desde o primeiríssimo sprint, raciocinando que era mais barato continuar acessível do que consertar depois. Quando a equipe de compras de um cliente de médio porte pediu um relatório de conformidade de acessibilidade durante um ciclo de vendas, a startup já usava HTML semântico, rotulava todos os campos e tinha foco visível em toda parte, então respondeu em dias em vez de correr. Essa prontidão ganhou um negócio que um concorrente perdeu pela mesma exigência.

**Grande empresa.** Uma grande varejista enfrentou uma ação coletiva porque clientes cegos não conseguiam completar o checkout com um leitor de tela. Além do acordo e dos honorários, a empresa teve de remediar sob um cronograma supervisionado pelo tribunal. Depois, reconstruiu a acessibilidade no seu sistema de design e no pipeline de CI, acrescentou testes com leitor de tela à definição de pronto e treinou as equipes. O checkout reconstruído e acessível também melhorou a conversão e reduziu os contatos de suporte para todos: as correções que ajudaram usuários de leitor de tela (rótulos claros, mensagens de erro, ordem lógica) ajudaram todos os usuários.

**Governo.** Uma agência pública de benefícios era legalmente obrigada a atender à WCAG 2.1 AA no seu pedido online. Os testes iniciais com usuários cegos e de baixa visão, usuários só de teclado e usuários com deficiência cognitiva revelaram que um indicador de “campo obrigatório” só por cor, um seletor de data inacessível e erros de validação não anunciados estavam impedindo as pessoas de terminar. Corrigi-los, com marcação semântica, foco visível, anúncio de erros por regiões ativas e ajuda em [linguagem simples](https://en.wikipedia.org/wiki/Plain_language), permitiu pela primeira vez que cidadãos com deficiência fizessem o pedido por conta própria. Isso reduziu a dependência de ajuda presencial e baixou o custo de servir, cumprindo o mandato legal.

## Justificativa de negócio: motivações, ROI e TCO

O argumento de negócio repousa em alcance de mercado, risco jurídico, custo de servir e qualidade. As pessoas com deficiência e suas famílias controlam um poder de compra significativo, e excluí-las o desperdiça. Serviços acessíveis reduzem a necessidade de canais assistidos caros (ajuda por telefone e presencial), o que é uma economia operacional direta, especialmente para o governo. E como as melhorias de acessibilidade (rótulos claros, suporte a teclado, conteúdo legível, marcação robusta) ajudam todo mundo, costumam elevar a conclusão e a satisfação em geral.

No TCO, o custo de adoção é treinamento, ferramentas e embutir a acessibilidade em componentes e pipelines, tudo modesto quando feito desde o início. O custo de não adotar é severo e vem de várias direções: responsabilidade jurídica (ações, acordos, remediação determinada por tribunal, multas regulatórias), a despesa muito maior de adaptar sob pressão de prazo, o dano de reputação e o custo contínuo de servir usuários excluídos por canais mais caros. Adaptar costuma custar várias vezes o que projetar desde o início teria custado.

Para defender o caso junto à liderança, comecem pela obrigação legal onde ela se aplica (é inegociável para o governo e cada vez mais para o setor privado). Depois quantifiquem a população endereçável que vocês estão excluindo, o custo de canal assistido dessa exclusão e os ganhos da “calçada rebaixada” para todos os usuários. Posicionem a acessibilidade como gerenciamento de riscos mais qualidade, não caridade.

## Antipadrões e armadilhas

- **Acessibilidade como caixa a marcar antes do lançamento**: uma auditoria no fim em vez de prática contínua, garantindo um retrabalho caro de última hora.
- **“Sopa de div”**: marcação não semântica, com manipuladores de clique em elementos genéricos, invisível para a tecnologia assistiva.
- **Mau uso do ARIA**: parafusar ARIA em marcação quebrada, o que engana os leitores de tela mais que a marcação simples.
- **Informação só por cor**: status mostrado só por cor, invisível para usuários daltônicos.
- **Foco invisível**: remover os contornos de foco por estética, deixando os usuários de teclado encalhados.
- **Armadilhas de teclado**: modais e widgets que prendem ou perdem o foco.
- **Complacência com o varredor automatizado**: passar num varredor e presumir que o produto é acessível.
- **Sobreposições de acessibilidade**: widgets de terceiros de “correção em uma linha” que não entregam conformidade real e podem piorar a experiência.
- **Excluir usuários com deficiência da pesquisa**: projetar para um usuário imaginário com deficiência em vez de testar com os reais.

## Modelo de maturidade

**Nível 1: Iniciar.** Nenhuma prática de acessibilidade. Os problemas só são descobertos quando um usuário reclama ou uma ação chega, e a resposta é reativa. A marcação é não semântica e não testada, e ninguém é dono do problema.

**Nível 2: Desenvolver.** Existe consciência e algumas equipes agem: um varredor automatizado num build aqui, um percurso por teclado ali, uma auditoria pré-lançamento antes de um grande lançamento. A prática é básica e inconsistente entre as equipes, a acessibilidade ainda é uma lista de verificação de fase final e é frequentemente despriorizada sob pressão de cronograma.

**Nível 3: Padronizar.** A WCAG 2.2 AA é o padrão documentado, imposto em toda a organização. A acessibilidade é embutida no sistema de design para que os componentes saiam acessíveis por padrão, testados automática e manualmente e escritos na definição de pronto. As equipes são treinadas, existe um dono ou centro de excelência e um processo de remediação é definido.

**Nível 4: Gerenciar.** A acessibilidade é medida e controlada com dados em relação a linhas de base. A organização acompanha métricas de conformidade ao longo do tempo (taxas de aprovação do varredor, a contagem de barreiras em aberto por gravidade, a cobertura de testes com leitor de tela das jornadas críticas e o tempo de remediação), reporta-as por equipe num painel e trata as regressões como falhas de build e não como avisos consultivos. As metas são definidas contra uma linha de base e o progresso é revisado, de modo que uma equipe que escorrega é visível antes que uma auditoria a ache.

**Nível 5: Orquestrar.** A acessibilidade é continuamente melhorada e integrada em toda a organização. As pessoas com deficiência fazem parte da pesquisa e dos testes de forma recorrente, e a acessibilidade é embutida na contratação, nos tokens de design e no CI. A organização se adapta à medida que os padrões se movem (adotando novos critérios da WCAG e preparando-se para a WCAG 3.0) e influencia fornecedores e parceiros para que toda a cadeia de suprimentos esteja em conformidade.

## Ideias para discussão

- Como vocês evitam que a acessibilidade seja despriorizada quando os prazos apertam?
- Qual é a mistura certa de testes automatizados, manuais e com usuários para o seu perfil de risco?
- Como a conformidade de acessibilidade deve ser escrita nos contratos com fornecedores e na contratação?
- Como vocês lidam com a lacuna entre a conformidade com a WCAG e a usabilidade genuína para pessoas com deficiência?
- Como as equipes devem se preparar para a WCAG 3.0 enquanto constroem hoje para a 2.2?
- Como vocês recrutam e remuneram de forma justa e respeitosa participantes com deficiência para a pesquisa?

## Principais conclusões

- A acessibilidade é um atributo de qualidade de base e, para o governo, uma exigência legal.
- Projetem para a WCAG 2.2 AA como piso. Usem os princípios POUR como modelo mental.
- Primeiro o HTML semântico. O ARIA apenas para preencher lacunas reais, feito corretamente.
- As ferramentas automatizadas pegam cerca de um terço dos problemas. Os testes manuais e com tecnologia assistiva são essenciais.
- Testem com pessoas com deficiência, não apenas para elas.
- Embutir a acessibilidade é barato e durável. Adaptá-la é caro e frágil.
- O design acessível é melhor para todos: o efeito calçada rebaixada é real.

## Referências e leitura complementar

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
