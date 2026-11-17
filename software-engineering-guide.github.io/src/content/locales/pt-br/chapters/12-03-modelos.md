# 12.3 Modelos

Estes modelos são pontos de partida prontos para copiar e colar. Levem qualquer modelo para o seu wiki, repositório ou sistema de chamados e preencham os espaços reservados entre colchetes. Notas em itálico e comentários embutidos explicam o que pertence a cada seção; excluam-nos quando a seção estiver preenchida. Mantenham os modelos leves: um modelo que é mais rápido de pular do que de completar não será usado. Adaptem títulos e seções à sua organização, mas preservem a intenção de cada parte.

Algumas convenções usadas abaixo:

- O texto entre `[colchetes]` é um espaço reservado a substituir.
- O texto em _itálico_ ou `<!-- comentários -->` é orientação a excluir.
- Mantenham o documento final tão curto quanto possível enquanto ainda responde às suas perguntas.

## Registro de decisão de arquitetura (ADR)

```markdown
# ADR [NNNN]: [Título curto da decisão]

- Status: [Proposta | Aceita | Descontinuada | Substituída pela ADR-XXXX]
- Data: [AAAA-MM-DD]
- Decisores: [nomes ou papéis]
- Consultados: [nomes ou papéis]

## Contexto

<!-- Qual é o problema, a força ou a restrição que conduz esta decisão?
     Declare os fatos e requisitos de forma neutra. Inclua apenas o que um
     leitor futuro precisa para entender por que uma decisão era necessária. -->

## Decisão

<!-- Declare a escolha em uma ou duas frases claras: "Nós vamos ..." -->

## Alternativas consideradas

<!-- Liste as opções realistas que vocês pesaram e por que cada uma foi ou
     não escolhida. Pelo menos duas alternativas devem aparecer aqui. -->

- Opção A: [resumo]; rejeitada porque [razão].
- Opção B: [resumo]; rejeitada porque [razão].
- Opção escolhida: [resumo]; escolhida porque [razão].

## Consequências

<!-- Resultados honestos da decisão, bons e ruins. -->

- Positivas: [benefícios obtidos]
- Negativas: [custos, riscos ou limitações aceitos]
- Acompanhamento: [migrações, novo trabalho ou decisões que isto dispara]

## Relacionados

<!-- Links para ADRs anteriores, RFCs, chamados ou documentos relacionados. -->
```

## RFC / documento de design

```markdown
# RFC: [Título]

- Autor(es): [nomes]
- Status: [Rascunho | Em revisão | Aprovada | Rejeitada | Implementada]
- Revisores: [nomes ou papéis]
- Criada em: [AAAA-MM-DD]
- Última atualização: [AAAA-MM-DD]
- Chamado / acompanhamento: [link]

## Resumo

<!-- Um parágrafo: o que isto propõe e por que importa. Um leitor deve captar
     a essência só com esta seção. -->

## Problema e motivação

<!-- Que problema estamos resolvendo? Quem é afetado? O que acontece se
     não fizermos nada? Inclua o contexto e as restrições relevantes. -->

## Metas e não metas

- Metas: [como é o sucesso, mensurável sempre que possível]
- Não metas: [explicitamente fora do escopo, para prevenir a expansão de escopo]

## Design proposto

<!-- O cerne do documento. Descreva a abordagem, a arquitetura, o modelo
     de dados, as interfaces e os fluxos principais. Use diagramas onde
     esclareçam. Explique como funciona, não apenas o que é. -->

## Alternativas consideradas

<!-- Outras abordagens e por que não foram escolhidas. Mostra ao leitor
     que o espaço de design foi explorado. -->

## Impacto e riscos

- Segurança e privacidade: [implicações e mitigações]
- Desempenho e escala: [carga e comportamento esperados]
- Operabilidade: [monitoramento, modos de falha, lançamento, rollback]
- Custo: [impacto de infraestrutura ou licenciamento]
- Compatibilidade retroativa: [migração e descontinuação]

## Plano de testes e lançamento

<!-- Como a mudança será validada e lançada com segurança. -->

## Questões em aberto

<!-- Problemas não resolvidos sobre os quais vocês querem a opinião dos revisores. -->
```

## Post-mortem / revisão de incidente (sem atribuição de culpa)

```markdown
# Post-mortem: [Título do incidente]

- ID do incidente: [ID]
- Data do incidente: [AAAA-MM-DD]
- Autores: [nomes]
- Status: [Rascunho | Final]
- Gravidade: [SEV1 | SEV2 | SEV3]

> Esta revisão é sem atribuição de culpa. Focamos sistemas e fatores
> contribuintes, não indivíduos. O objetivo é aprender e prevenir a
> recorrência.

## Resumo

<!-- Duas ou três frases: o que aconteceu, o impacto e a resolução,
     legíveis por um não especialista. -->

## Impacto

- Duração: [do início à hora de recuperação, com fuso horário]
- Usuários afetados: [escopo e número]
- Impacto no negócio: [receita, SLA, reputação ou outro]

## Linha do tempo

<!-- Sequência factual e com carimbos de data e hora dos eventos. Inclua
     detecção, escalação, ações-chave e recuperação. -->

- [HH:MM] [evento]
- [HH:MM] [evento]

## Fatores contribuintes

<!-- A cadeia de condições que levou ao incidente. Prefira "fatores
     contribuintes" a uma única causa-raiz. -->

## Detecção e resposta

- Como foi detectado? [alerta, relato de cliente etc.]
- O que ajudou a resposta?
- O que atrasou a resposta?

## O que correu bem

<!-- Reconheça as ações eficazes e as salvaguardas que funcionaram. -->

## Itens de ação

<!-- Específicos, com dono e datados. Tratem de prevenção, detecção e
     mitigação. Acompanhem-nos no backlog normal. -->

| Ação | Dono | Prazo | Tipo (prevenir/detectar/mitigar) | Chamado |
|------|------|-------|----------------------------------|---------|
| [ação] | [nome] | [data] | [tipo] | [link] |

## Lições aprendidas

<!-- O que a organização mais ampla deve levar daqui. -->
```

## Modelo de ameaças (baseado em STRIDE)

```markdown
# Modelo de ameaças: [Nome do sistema ou da funcionalidade]

- Autor(es): [nomes]
- Data: [AAAA-MM-DD]
- Revisores: [contato de segurança, donos]
- Escopo: [o que está e o que não está coberto]

## Visão geral do sistema

<!-- Breve descrição do sistema, seu propósito e seus usuários. -->

## Ativos

<!-- O que vale proteger: dados, credenciais, funcionalidade, reputação.
     Anote a sensibilidade de cada um. -->

## Fronteiras de confiança e fluxo de dados

<!-- Descreva ou diagrame componentes, repositórios de dados, entidades
     externas e as fronteiras onde a confiança muda. -->

## Ameaças (STRIDE)

<!-- Para cada elemento, considere as categorias STRIDE. Registre cada
     ameaça crível, seu risco e a mitigação ou o risco aceito. -->

| Ameaça | Categoria STRIDE | Elemento afetado | Risco (B/M/A) | Mitigação | Status |
|--------|------------------|------------------|---------------|-----------|--------|
| [ameaça] | Spoofing (falsificação) | [elemento] | [risco] | [controle] | [aberta/mitigada/aceita] |
| [ameaça] | Tampering (adulteração) | [elemento] | [risco] | [controle] | [status] |
| [ameaça] | Repudiation (repúdio) | [elemento] | [risco] | [controle] | [status] |
| [ameaça] | Information disclosure (divulgação de informações) | [elemento] | [risco] | [controle] | [status] |
| [ameaça] | Denial of service (negação de serviço) | [elemento] | [risco] | [controle] | [status] |
| [ameaça] | Elevation of privilege (elevação de privilégio) | [elemento] | [risco] | [controle] | [status] |

## Suposições e dependências

<!-- Suposições de segurança em que se confia e controles externos em que se confia. -->

## Problemas em aberto e acompanhamento

<!-- Ameaças que precisam de mais trabalho, acompanhadas como chamados. -->
```

## Runbook

```markdown
# Runbook: [Nome da tarefa ou do cenário]

- Serviço: [nome do serviço]
- Dono: [equipe]
- Última revisão: [AAAA-MM-DD]
- Alertas relacionados: [nomes dos alertas]

## Propósito

<!-- Quando usar este runbook e o que ele realiza. -->

## Pré-requisitos

<!-- Acesso, ferramentas e permissões necessários antes de começar. -->

## Detecção / sintomas

<!-- O que o operador observa: alertas, assinaturas de erro, painéis. -->

## Diagnóstico

<!-- Verificações passo a passo para confirmar o problema e estreitar a
     causa. Inclua os comandos, consultas ou links de painel exatos. -->

1. [passo e resultado esperado]
2. [passo e resultado esperado]

## Resolução

<!-- Passos concretos e ordenados para consertar ou mitigar. Anote qualquer
     passo arriscado ou irreversível e como verificar o sucesso. -->

1. [passo]
2. [verificar a recuperação]

## Rollback

<!-- Como desfazer as ações se a resolução piorar as coisas. -->

## Escalação

<!-- Quem contatar e quando escalar. Sobreaviso secundário, equipe dona
     e contatos de fornecedores. -->

## Referências

<!-- Painéis, runbooks relacionados, documentos de arquitetura. -->
```

## README de serviço / entrada de catálogo de serviços

```markdown
# [Nome do serviço]

- Equipe dona: [equipe]
- Sobreaviso: [link da escala]
- Camada / criticidade: [Camada 1 | 2 | 3]
- Repositório: [link]
- Status: [Ativo | Descontinuado]

## O que faz

<!-- Um parágrafo sobre a responsabilidade do serviço e seus consumidores. -->

## Arquitetura

<!-- Componentes principais, dependências (a montante e a jusante) e um
     link para o documento de design ou diagrama. -->

## Interfaces

- APIs / endpoints: [link para a especificação]
- Eventos publicados / consumidos: [tópicos]
- Repositórios de dados: [bancos de dados, caches, buckets]

## Execução e implantação

- Ambientes: [dev, staging, prod]
- Como implantar: [link do pipeline e processo]
- Configuração e flags de funcionalidade: [onde e como]

## Observabilidade

- Painéis: [links]
- Alertas: [links]
- Logs: [onde encontrá-los]
- SLOs: [link]

## Operações

- Runbooks: [links]
- Tarefas comuns: [escalonamento, reinício, preenchimento retroativo]
- Problemas conhecidos e limitações: [notas]

## Primeiros passos (para novos contribuidores)

<!-- Como construir, testar e rodar localmente. -->

## Contatos

- Canal de Slack / chat: [link]
- Escalação: [caminho]
```

## Política de SLO / orçamento de erros

```markdown
# Política de SLO e orçamento de erros: [Nome do serviço ou da jornada]

- Dono: [equipe]
- Data de vigência: [AAAA-MM-DD]
- Cadência de revisão: [por exemplo, trimestral]

## Indicadores de nível de serviço (SLIs)

<!-- Defina cada SLI com precisão: a grandeza medida, como é medida e de
     onde (idealmente da perspectiva do usuário). -->

| SLI | Definição | Fonte de dados |
|-----|-----------|----------------|
| Disponibilidade | [por exemplo, requisições bem-sucedidas / total de requisições] | [fonte] |
| Latência | [por exemplo, proporção de requisições abaixo de X ms] | [fonte] |

## Objetivos (SLOs)

| SLI | Meta | Janela de medição |
|-----|------|-------------------|
| Disponibilidade | [por exemplo, 99,9%] | [por exemplo, 28 dias móveis] |
| Latência | [por exemplo, 95% abaixo de 300 ms] | [28 dias móveis] |

## Orçamento de erros

<!-- A não confiabilidade permitida: 100% menos a meta, ao longo da
     janela. Declare o orçamento em termos concretos (por exemplo,
     minutos/mês). -->

- Orçamento: [folga derivada]

## Política quando o orçamento se esgota

<!-- As consequências acordadas. Torne-as concretas e aplicáveis. -->

- [por exemplo, Congelar os lançamentos de funcionalidades não críticas até o orçamento se recuperar.]
- [por exemplo, Priorizar o trabalho de confiabilidade no próximo ciclo de planejamento.]
- [por exemplo, Escalar à liderança de engenharia se violado em duas janelas seguidas.]

## Política quando o orçamento está saudável

<!-- Que risco extra a equipe pode assumir, por exemplo, lançamentos mais rápidos. -->

## Alertas

<!-- Alertas de taxa de queima e limiares ligados a este SLO. -->
```

## Entrada de registro de riscos

```markdown
## Risco: [Título curto do risco]

- ID do risco: [ID]
- Data de registro: [AAAA-MM-DD]
- Dono: [nome ou papel responsável por gerir este risco]
- Categoria: [segurança | operacional | conformidade | financeiro | entrega | fornecedor]
- Status: [Aberto | Em mitigação | Aceito | Encerrado]

### Descrição

<!-- Declare o risco como: causa -> evento -> consequência. O que poderia
     acontecer e por que importa. -->

### Avaliação

- Probabilidade: [Baixa | Média | Alta]
- Impacto: [Baixo | Médio | Alto]
- Classificação geral: [derivada de probabilidade x impacto]

### Controles atuais

<!-- O que já reduz este risco hoje. -->

### Plano de mitigação

<!-- Ações planejadas para reduzir a probabilidade ou o impacto, com donos
     e datas. Se aceitar o risco, registre quem o aceitou e por quê. -->

| Ação | Dono | Prazo | Status |
|------|------|-------|--------|
| [ação] | [nome] | [data] | [status] |

### Revisão

- Próxima data de revisão: [AAAA-MM-DD]
- Decisão / notas: [qualquer aprovação de aceitação ou mudança]
```

## Resumo de uma página de projeto / briefing de produto

```markdown
# [Nome do projeto ou produto]: resumo de uma página

- Patrocinador: [nome]
- Líder: [nome]
- Data: [AAAA-MM-DD]
- Status: [Ideia | Aprovado | Em andamento | Entregue]

## Problema

<!-- Um parágrafo: o problema do cliente ou do negócio e a evidência de
     que é real e vale resolver. -->

## Público

<!-- Quem tem este problema e quem se beneficia de resolvê-lo. -->

## Solução proposta

<!-- Uma descrição curta do que vamos construir ou mudar. Mantenha no
     nível da intenção, não do detalhe de implementação. -->

## Por que agora

<!-- A razão para fazer isto agora e não depois. -->

## Métricas de sucesso

<!-- Como saberemos que funcionou. Prefira resultados mensuráveis. -->

- [métrica e meta]

## Escopo

- Dentro do escopo: [o que vamos fazer]
- Fora do escopo: [o que não vamos fazer]

## Riscos e questões em aberto

<!-- Principais incertezas e dependências. -->

## Plano aproximado e marcos

<!-- Fases de alto nível e prazos aproximados. -->

## Custo e recursos

<!-- Pessoas, tempo e orçamento necessários. -->
```

## Notas de passagem de sobreaviso

```markdown
# Passagem de sobreaviso: [AAAA-MM-DD]

- Quem sai: [nome]
- Quem entra: [nome]
- Serviço(s): [nomes]

## Status geral

<!-- Uma linha: calmo, barulhento ou problema em curso. -->

## Incidentes abertos

<!-- Quaisquer incidentes ativos ou recentemente resolvidos que o próximo
     respondente precisa conhecer, com links. -->

- [incidente, status e o que resta]

## Mudanças em curso ou planejadas

<!-- Implantações, migrações, janelas de manutenção ou experimentos em
     andamento que poderiam causar alertas. -->

## Alertas barulhentos ou instáveis

<!-- Alertas que dispararam e seu significado real, para que a próxima
     pessoa não seja enganada. Anote quaisquer silenciamentos temporários
     e sua expiração. -->

## Itens a vigiar

<!-- Métricas ou sistemas que tendem numa direção preocupante. -->

## Acompanhamentos pendentes

<!-- Tarefas passadas ao próximo turno, com links para os chamados. -->

## Notas

<!-- Qualquer outra coisa útil: peculiaridades de acesso, problemas de fornecedores, contexto. -->
```

## Requisição de mudança (para controle de mudanças regulado)

```markdown
# Requisição de mudança: [Título da mudança]

- ID da mudança: [ID]
- Solicitante: [nome]
- Data de envio: [AAAA-MM-DD]
- Tipo: [Padrão | Normal | Emergencial]
- Prioridade: [Baixa | Média | Alta]
- Status: [Enviada | Aprovada | Rejeitada | Implementada | Encerrada]

## Descrição da mudança

<!-- O que está mudando e por quê. Referencie o chamado ou o requisito. -->

## Sistemas e componentes afetados

<!-- Serviços, dados, ambientes e usuários impactados. -->

## Justificativa e impacto no negócio

<!-- A razão da mudança e o impacto de não fazê-la. -->

## Avaliação de risco

- Nível de risco: [Baixo | Médio | Alto]
- Impacto potencial se a mudança falhar: [descrição]
- Impacto em segurança, privacidade ou conformidade: [descrição]

## Plano de implementação

<!-- Passos ordenados, responsáveis e cronograma. -->

## Plano de testes e validação

<!-- Como o sucesso será verificado antes e depois da mudança. -->

## Plano de retirada / rollback

<!-- Como reverter a mudança se ela falhar e o tempo de recuperação. -->

## Cronograma

- Janela proposta: [início e fim, com fuso horário]
- Indisponibilidade esperada: [duração ou nenhuma]

## Aprovações

| Papel | Nome | Decisão | Data |
|-------|------|---------|------|
| Dono da mudança | [nome] | [aprovar/rejeitar] | [data] |
| Revisor técnico | [nome] | [aprovar/rejeitar] | [data] |
| Comitê consultivo de mudanças | [nome] | [aprovar/rejeitar] | [data] |

## Revisão pós-implementação

<!-- Resultado, problemas encontrados e se a retirada foi necessária. -->
```

## Esboço de avaliação de impacto à proteção de dados (DPIA)

```markdown
# Avaliação de impacto à proteção de dados: [Nome da atividade de tratamento]

- Avaliador: [nome]
- Data: [AAAA-MM-DD]
- Revisores: [encarregado de proteção de dados / contato de privacidade]
- Status: [Rascunho | Revisada | Aprovada]

## 1. Descrição do tratamento

<!-- Que dados pessoais são tratados, como, por quem e para qual
     finalidade. Inclua os fluxos de dados da coleta à exclusão. -->

- Titulares dos dados: [de quem são os dados]
- Categorias de dados: [tipos de dados pessoais, anote quaisquer categorias especiais]
- Finalidades: [por que os dados são tratados]
- Destinatários e operadores: [quem recebe ou trata os dados]
- Período de retenção: [por quanto tempo os dados são mantidos e método de exclusão]
- Transferências internacionais: [destinos e mecanismo de transferência]

## 2. Necessidade e proporcionalidade

<!-- O tratamento é necessário para a finalidade? É a opção menos
     intrusiva? Qual é a base legal ou a autoridade? -->

- Base legal / autoridade: [base de cada finalidade]
- Minimização de dados: [por que cada campo é necessário]
- Justificativa de exatidão e retenção: [notas]
- Como os direitos dos titulares são apoiados: [acesso, exclusão etc.]

## 3. Consulta

<!-- Partes interessadas e, quando relevante, titulares dos dados consultados. -->

## 4. Riscos para os indivíduos

<!-- Identifique os riscos de privacidade e classifique cada um. -->

| Risco para os indivíduos | Probabilidade | Gravidade | Geral |
|--------------------------|---------------|-----------|-------|
| [por exemplo, acesso não autorizado a dados sensíveis] | [B/M/A] | [B/M/A] | [classificação] |

## 5. Medidas para reduzir o risco

<!-- Para cada risco, a mitigação e o risco residual depois dela. -->

| Risco | Medida | Risco residual | Aceito por |
|-------|--------|----------------|------------|
| [risco] | [controle] | [B/M/A] | [nome] |

## 6. Resultado e aprovação

- Risco residual aceitável: [Sim | Não]
- Medidas aprovadas por: [nome, papel]
- Consulta à autoridade supervisora necessária: [Sim | Não]
- Data de revisão: [AAAA-MM-DD]
```
