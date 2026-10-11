# 12.6 Roteiro de adoção

Este apêndice é um guia prático para implantar as práticas deste livro de forma
*incremental*. A instrução mais importante de todo o guia, repetida em cada
capítulo, é **adotem de forma incremental; nada de big-bang**. Uma transformação
que tenta mudar tudo de uma vez não muda nada de modo duradouro: esgota a boa
vontade, sobrecarrega as equipes e colapsa na primeira crise. Uma transformação
que começa com uma dor real, entrega uma vitória visível e se compõe a partir daí
pode mover uma organização de milhares de pessoas ao longo de alguns anos.

Este roteiro dá princípios de adoção, uma sequência baseada em maturidade dos
primeiros 90 dias a mais de dois anos, um arcabouço de priorização com um exemplo
trabalhado, vitórias rápidas domínio a domínio, orientação especial para empresas
e governos, formas de medir o sucesso e os modos de falha a evitar.

## Princípios de adoção

Estes princípios valem seja qual for o seu tamanho, setor ou maturidade inicial.

- **Comecem pela dor, não por um arcabouço.** Achem o que mais dói, sejam
  lançamentos lentos, quedas frequentes, auditorias reprovadas ou rotatividade, e
  consertem isso primeiro. A dor cria a demanda e a cobertura política que um
  mandato de cima para baixo jamais cria. Ninguém resiste ao alívio.
- **Caminhos pavimentados acima de mandatos.** Façam do jeito recomendado o jeito
  *mais fácil*. Um caminho dourado que é mais rápido, mais seguro e mais bem
  documentado conquista a adoção por seus méritos; uma política mais lenta que o
  atalho será contornada. Invistam no caminho pavimentado antes de descontinuar a
  trilha de terra.
- **Meçam resultados, não atividade.** Acompanhem se a mudança melhorou a entrega,
  a confiabilidade, a postura de segurança ou os resultados para os usuários, não
  quantas equipes assistiram a um treinamento ou marcaram uma caixinha.
  Instrumentem antes de mudar para poder provar o efeito.
- **Garantam o patrocínio executivo, e mantenham-no.** A mudança sustentada precisa
  de um executivo responsável que proteja o financiamento, remova bloqueios e
  segure a linha quando a transformação ficar desconfortável. O patrocínio não é um
  evento de lançamento; é uma relação contínua que vocês precisam reconquistar com
  resultados.
- **Voluntários antes de recrutas.** Comecem pelas equipes que *querem* mudar. O
  sucesso delas vira a história de referência que puxa a maioria relutante. Forçar
  primeiro os resistentes produz obediência maliciosa e histórias de advertência.
- **Tornem reversível onde puderem.** Prefiram mudanças que possam pilotar, medir e
  reverter. As decisões reversíveis de “porta de duas vias” podem andar depressa;
  reservem o processo pesado para o genuinamente irreversível.
- **Mostrem vitórias cedo e com frequência.** Entreguem algo visível em semanas, não
  em trimestres. O ímpeto é um recurso; gastem a primeira vitória para financiar a
  seguinte.
- **Encontrem as equipes onde elas estão.** Uma única barra de maturidade aplicada
  uniformemente é injusta e desmoralizante. Sequenciem pela prontidão e pela dor de
  cada equipe.

## Sequenciamento baseado em maturidade

Os horizontes abaixo são cumulativos: cada um se constrói sobre o anterior. As
datas são orientação, não prazos; uma organização grande ou fortemente regulada
pode levar mais tempo em cada fase. O padrão (*estabilizar, depois padronizar,
depois escalar, depois sustentar*) vale em qualquer ritmo.

### Primeiros 90 dias: estabilizar e provar

Meta: estabelecer uma linha de base, escolher um ou dois problemas emblemáticos e
entregar uma primeira vitória crível com uma equipe disposta.

- [ ] Nomear um patrocinador executivo responsável e uma pequena coalizão
      orientadora.
- [ ] Estabelecer a linha de base das quatro métricas DORA (frequência de
      implantação, prazo de entrega, taxa de falha das mudanças, tempo para
      restaurar) mesmo que os números sejam grosseiros.
- [ ] Conduzir uma avaliação leve contra os modelos de maturidade do capítulo 12.4
      para achar as maiores lacunas.
- [ ] Escolher uma ou duas equipes-piloto que *se voluntariem* e tenham dor real.
- [ ] Consertar de ponta a ponta um problema de alta visibilidade (por exemplo,
      automatizar a implantação de uma equipe, ou acrescentar SLOs a um serviço
      crítico).
- [ ] Montar um registro compartilhado de decisões (ADRs) e um lugar para publicar
      resultados.
- [ ] Combinar como vocês medirão o sucesso *antes* de mudar qualquer coisa.

### Até 6 meses: padronizar o padrão vencedor

Meta: transformar o sucesso do piloto num padrão repetível e documentado e
oferecê-lo como caminho pavimentado à próxima coorte de equipes.

- [ ] Publicar o caminho dourado do piloto como modelos, pipelines e documentação
      reutilizáveis.
- [ ] Estabelecer uma equipe de plataforma ou habilitadora (mesmo que virtual) para
      ser dona do caminho pavimentado e dar suporte a ele.
- [ ] Levar o padrão a mais três a cinco equipes, priorizando por impacto e
      prontidão.
- [ ] Introduzir portões automatizados de qualidade e segurança (lint, testes,
      SAST/SCA) no pipeline compartilhado como padrão, não como complemento.
- [ ] Iniciar uma prática de revisão de incidentes sem atribuição de culpa e
      publicar internamente os post-mortems.
- [ ] Montar um fórum leve de governança (revisão de arquitetura, custódia do
      caminho pavimentado) que destrave em vez de guardar o portão.

### Até 12 meses: escalar pela organização

Meta: fazer do caminho pavimentado o padrão para a maior parte do trabalho novo e
começar a aposentar as piores práticas legadas.

- [ ] Ampliar o escopo da equipe de plataforma; publicar um catálogo de serviços e
      scorecards.
- [ ] Definir linhas de base para toda a organização: SLOs para serviços de camada
      1, controles de segurança em todo pipeline, verificações de acessibilidade
      nos builds de frontend.
- [ ] Acompanhar as taxas de adoção por equipe e tornar os dados visíveis.
- [ ] Iniciar a modernização deliberada do legado nos sistemas de maior risco usando
      os padrões strangler-fig e branch-by-abstraction.
- [ ] Incorporar a medição ao planejamento: as equipes revisam suas tendências de
      DORA e de confiabilidade no ritmo operacional normal.
- [ ] Investir em capacitação (treinamento interno, mentoria, comunidades de
      prática) para que a capacidade se espalhe mais rápido que os mandatos.

### Mais de 2 anos: sustentar e melhorar continuamente

Meta: as práticas são “como trabalhamos”, não um programa, e a organização as
melhora sem empurrão central.

- [ ] Aposentar o programa de transformação como iniciativa nomeada; embutir seu
      trabalho na governança normal e nas operações da plataforma.
- [ ] Tratar o caminho pavimentado como um produto com roteiro, usuários e métricas
      de satisfação próprios (pesquisas de experiência do desenvolvedor).
- [ ] Gerir a dívida técnica e a modernização como um portfólio permanente, não um
      esforço pontual.
- [ ] Conduzir reavaliações periódicas de maturidade e elevar os padrões conforme o
      piso sobe.
- [ ] Proteger-se contra a regressão: manter o patrocínio, continuar medindo e
      renovar as práticas conforme a tecnologia e as ameaças evoluem.

## Um arcabouço de priorização

Vocês sempre terão mais melhorias a fazer do que capacidade para fazê-las.
Priorizem com um modelo simples e defensável e não com a voz mais alta da sala.

Pontuem cada iniciativa candidata em três dimensões:

- **Impacto (1–5):** Quanto isto vai melhorar um resultado real (velocidade de
  entrega, confiabilidade, segurança, custo ou valor para o usuário), e para
  quantas equipes ou usuários?
- **Esforço (1–5):** Quanto trabalho, coordenação e ruptura para entregá-lo?
  (Mais alto = mais esforço.)
- **Peso de risco (0,5–2,0):** Um multiplicador de urgência e exposição. Segurança,
  conformidade e questões de segurança física carregam peso maior; o que é
  desejável mas dispensável carrega menos.

Uma pontuação útil de ranqueamento é:

```
Prioridade = (Impacto × Peso de risco) ÷ Esforço
```

Ranqueiem em ordem decrescente de prioridade. Sequenciem os primeiros itens, mas
mantenham sempre pelo menos uma “vitória rápida” de baixo esforço em andamento
para sustentar o ímpeto, e revisitem as pontuações a cada trimestre conforme as
condições mudam.

### Exemplo trabalhado

| Iniciativa | Impacto | Esforço | Peso de risco | Prioridade | Sequência |
|---|---|---|---|---|---|
| Automatizar a implantação do serviço de maior receita | 5 | 2 | 1,5 | 3,75 | Agora |
| Acrescentar SLOs e alertas aos serviços de camada 1 | 4 | 2 | 1,5 | 3,00 | Agora |
| Introduzir SAST/SCA no pipeline compartilhado | 4 | 2 | 2,0 | 4,00 | Agora |
| Lançar um sistema de design em todos os frontends | 4 | 5 | 1,0 | 0,80 | Depois |
| Migrar o batch do mainframe para a nuvem | 5 | 5 | 1,5 | 1,50 | Em fases |
| Padronizar ADRs entre as equipes | 3 | 1 | 1,0 | 3,00 | Agora (vitória rápida) |
| Adotar uma nova linguagem de programação em toda a organização | 2 | 5 | 0,5 | 0,20 | Adiar |

Neste exemplo, o trabalho do pipeline de segurança lidera a lista por causa do seu
alto peso de risco e esforço modesto, enquanto a mudança de linguagem em toda a
organização cai para o fim apesar do entusiasmo, porque seu impacto é baixo e seu
esforço e ruptura são altos. O arcabouço torna esse compromisso explícito e
discutível, que é o seu valor real.

## Vitórias rápidas domínio a domínio

Cada parte do livro tem um primeiro passo de baixo custo e alto sinal. Comecem aqui.

| Parte | Vitória rápida “comecem aqui” |
|---|---|
| **Fundamentos (cultura, equipes, processo)** | Adotem ADRs leves e conduzam uma retrospectiva sem atribuição de culpa; tornem visíveis as decisões e o aprendizado. |
| **Ofício da programação** | Liguem um formatador automático e um linter no CI como padrões impostos, para que o estilo deixe de ser tema de revisão. |
| **Arquitetura** | Escrevam uma decisão de arquitetura de uma página e um diagrama de contexto C4 para o seu sistema mais importante. |
| **Segurança** | Acrescentem varredura de dependências (SCA) e de segredos ao pipeline; habilitem-nas primeiro para um repositório crítico. |
| **UX / design** | Conduzam três testes de usabilidade baratos no seu fluxo de maior tráfego; consertem o principal problema observado. |
| **IA / ML** | Escrevam um enquadramento de problema de uma página e uma verificação de prontidão dos dados antes de qualquer trabalho de modelo; definam como avaliarão o sucesso. |
| **Dados / análise** | Definam uma única métrica “estrela-guia” acordada e um painel confiável; aposentem um conflitante. |
| **DevOps / plataforma** | Levem uma equipe a um pipeline de build-teste-implantação totalmente automatizado e documentem-no como modelo. |
| **Operações / confiabilidade** | Definam SLIs e um SLO para a sua jornada de usuário mais crítica; alertem sobre sintomas, não sobre causas. |
| **Empresa / governo** | Mapeiem os seus controles atuais a um arcabouço (NIST CSF, ISO 27001 ou SOC 2) e automatizem a evidência de um controle. |

## Orientação especial para empresas

As grandes organizações estabelecidas carregam escala, muitas equipes, legado
profundo e pesada sobrecarga de gestão da mudança. Adaptem o roteiro de acordo.

- **Federem, não centralizem tudo.** Uma única equipe central não consegue servir
  centenas de equipes de produto. Usem uma equipe de plataforma para oferecer
  caminhos pavimentados e equipes habilitadoras para orientar, enquanto as equipes
  de produto mantêm a propriedade. (Vejam Team Topologies.)
- **Respeitem a lei de Conway.** A sua arquitetura espelhará o seu organograma. Se
  vocês querem serviços desacoplados, precisam de equipes desacopladas e
  empoderadas; reorganizem deliberadamente em vez de lutar contra a corrente.
- **Tratem o legado como um portfólio.** Vocês não conseguem modernizar tudo.
  Classifiquem os sistemas legados por risco e valor de negócio e apliquem a
  migração strangler-fig aos poucos que importam; congelem ou desativem
  deliberadamente o resto.
- **A gestão da mudança é trabalho real.** Em escala, comunicação, treinamento e
  alinhamento de incentivos não são sobrecarga: são a transformação. Orcem
  explicitamente a capacitação, as comunidades de prática e a evangelização
  interna.
- **Cuidado com o reflexo do mandato.** As grandes organizações recorrem por padrão
  a memorandos de política. Resistam. Um mandato sem caminho pavimentado produz
  cumprimento de caixinha; um caminho pavimentado sem mandato produz adoção
  genuína.
- **Alinhem incentivos e financiamento.** Passem do financiamento por projeto para
  equipes de produto duráveis, para que as melhorias sobrevivam à data final de um
  projeto. Recompensem resultados, não saídas.

## Orientação especial para governo

As organizações do setor público acrescentam ciclos de contratação, portões de
conformidade, gestão de contratados, financiamento plurianual e obrigações de
transparência. Isso são insumos de projeto, não desculpas.

- **Projetem para o ATO desde o primeiro dia.** Os portões de autorização para
  operar e de monitoramento contínuo (conforme o NIST RMF / 800-37) podem dominar
  os prazos. Construam cedo no pipeline os controles de segurança e a coleta de
  evidências para que a conformidade seja contínua, não uma correria tardia e
  bloqueante.
- **Comprem de forma incremental.** Contratações plurianuais e big-bang
  institucionalizam o fracasso big-bang contra o qual este livro alerta. Prefiram a
  contratação modular, adjudicações menores e termos de referência baseados em
  resultado que permitam iterar.
- **Gerenciem fornecedores e integradores como parte da equipe.** Grande parte da
  engenharia governamental é entregue por contratados. Escrevam nos contratos
  caminhos pavimentados, portões de qualidade e requisitos de transparência, e
  garantam que conhecimento e código sejam transferidos ao governo para evitar o
  aprisionamento (lock-in) e o risco de fator ônibus.
- **Planejem em torno dos ciclos de financiamento.** As dotações plurianuais e
  anuais restringem aquilo a que vocês podem se comprometer. Sequenciem o trabalho
  para que cada incremento financiado entregue valor independente e não os deixe
  encalhados no meio da transformação se o financiamento mudar.
- **Acessibilidade e linguagem simples são obrigações legais.** A Section 508, a
  ADA, a WCAG e os mandatos de linguagem simples são requisitos, não melhorias.
  Embutam verificações de acessibilidade nos pipelines e a revisão de conteúdo no
  fluxo de trabalho.
- **A transparência é uma funcionalidade.** As leis de acesso à informação (FOIA),
  os mandatos de código aberto (“dinheiro público, código público”) e os padrões
  de serviço publicados significam que o seu trabalho está sujeito ao escrutínio
  público. Projetem para isso: registros claros, abertos onde apropriado e dados
  de desempenho publicados com honestidade.
- **Sigam padrões comprovados do setor público.** O U.S. Digital Services Playbook,
  o GOV.UK Service Standard e o USWDS codificam lições duramente conquistadas;
  adotem-nos em vez de reinventar.

## Medindo o sucesso da adoção

Meçam tanto indicadores *antecedentes* (sinais precoces de que a mudança está
pegando) quanto *consequentes* (os resultados que vocês afinal importam). Observem
a tendência, não uma única leitura, e nunca deixem uma métrica virar uma meta a
ser manipulada.

| Tipo | Indicador | O que diz |
|---|---|---|
| Antecedente | Número de equipes no caminho pavimentado | Com que rapidez a adoção está se espalhando |
| Antecedente | Cobertura dos portões do pipeline (testes, SAST, a11y) | Quão embutidas estão a qualidade e a segurança |
| Antecedente | Pontuações da pesquisa de experiência do desenvolvedor | Se o caminho pavimentado de fato ajuda |
| Antecedente | Porcentagem de decisões registradas como ADRs | Se a cultura de escrita e aprendizado é real |
| Consequente | Frequência de implantação (DORA) | Vazão de entrega |
| Consequente | Prazo de entrega das mudanças (DORA) | Rapidez do commit à produção |
| Consequente | Taxa de falha das mudanças (DORA) | Qualidade do processo de entrega |
| Consequente | Tempo para restaurar o serviço (DORA) | Resiliência operacional |
| Consequente | Tendência de frequência e gravidade de incidentes | Melhoria de confiabilidade ao longo do tempo |
| Consequente | Achados de auditoria / falhas de controle | Postura de conformidade |
| Consequente | Retenção e rotatividade | Se a cultura está melhorando |

As quatro métricas DORA são as medidas de resultado entre setores mais validadas
para a entrega; tratem a melhoria nas quatro em conjunto como o sinal principal e
protejam-se de melhorar uma sacrificando outra.

## Modos de falha comuns e como evitá-los

| Modo de falha | Como se parece | Como evitá-lo |
|---|---|---|
| **Lançamento big-bang** | Mudar tudo para todos de uma vez; o programa colapsa sob o próprio peso. | Sequenciar por dor e prontidão; pilotar, provar, depois escalar. |
| **Mandato sem caminho pavimentado** | A política exige o jeito novo, mas o jeito novo é mais lento; as equipes cumprem no papel e o contornam. | Construir *primeiro* o caminho mais fácil e melhor; conquistar a adoção por mérito. |
| **Culto a um arcabouço (cargo-culting)** | Copiar o SAFe, o modelo Spotify ou a estrutura de outra organização sem o contexto delas. | Partir da própria dor e dos próprios princípios; adaptar, não transplantar. |
| **Medir atividade, não resultados** | Celebrar treinamentos concluídos e caixinhas marcadas enquanto entrega e confiabilidade não se movem. | Instrumentar resultados (DORA, incidentes, valor para o usuário) desde o início. |
| **Transformação começando pela ferramenta** | Comprar uma plataforma e esperar que a cultura a siga. | Liderar com práticas e caminhos pavimentados; as ferramentas os servem, não o contrário. |
| **Perder o patrocínio** | O campeão executivo sai ou se desengaja; o programa empaca. | Institucionalizar a mudança na governança normal; construir uma coalizão, não um ponto único de falha. |
| **Métricas de vaidade e manipulação** | Os números de cobertura ou velocidade sobem enquanto a qualidade cai. | Usar as métricas como sinais com medidas de contrapeso; nunca como metas únicas. |
| **Ferver o oceano no legado** | Tentar modernizar tudo, entregando nada. | Ranquear por risco e valor; estrangular os poucos críticos, congelar o resto. |
| **Fadiga de transformação** | Mudança sem fim e sem retorno visível; as equipes se desengajam. | Entregar vitórias cedo; proteger o ritmo sustentável; deixar o programa acabar e virar trabalho normal. |
| **Ignorar o organograma** | A nova arquitetura briga com a estrutura de equipes existente. | Aplicar a manobra inversa de Conway: moldar as equipes para a arquitetura desejada. |

## A versão mais curta possível

Se vocês não lembrarem de mais nada deste apêndice:

1. Achem a maior dor e consertem-na com uma equipe disposta.
2. Transformem esse conserto num caminho pavimentado genuinamente mais fácil que o
   jeito antigo.
3. Meçam o resultado, mostrem a vitória e usem-na para financiar o passo seguinte.
4. Repitam, alargando o círculo, até o caminho pavimentado ser simplesmente como
   vocês trabalham.
5. Mantenham o patrocínio, continuem medindo e nunca façam big-bang.

Vejam o **capítulo 12.4** para os modelos de maturidade que ancoram as avaliações e
o **capítulo 12.2** para as listas de verificação de lançamento, revisão e
auditoria que operacionalizam cada passo.
