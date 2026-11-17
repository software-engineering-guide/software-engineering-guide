# 12.2 Listas de verificação

Estas listas de verificação são referências rápidas, práticas e prontas para uso. Copiem qualquer uma para um modelo de pull request, uma página de wiki, um chamado ou a pauta de uma reunião de revisão e adaptem os itens ao seu contexto. Tratem cada item como algo que uma pessoa possa verificar e responder com sim ou não. Uma lista de verificação é um auxílio de memória e um padrão compartilhado, não um substituto do julgamento; excluam os itens que não se aplicam e acrescentem os que o seu domínio exige.

Orientações para usá-las bem:

- Mantenham as listas curtas o bastante para que as pessoas de fato as completem. Se uma lista é rotineiramente pulada, é longa ou genérica demais.
- Automatizem todo item que uma máquina possa verificar (formatação, testes, varreduras) para que os humanos gastem a atenção em itens de julgamento.
- Versionem as suas listas e revisem-nas periodicamente. Uma lista que nunca muda provavelmente não está sendo usada.
- Distingam os itens bloqueantes dos consultivos quando a distinção importar para o seu processo.

## Lista de verificação de revisão de código

Para o revisor que examina a mudança de outra pessoa.

- [ ] A mudança faz o que sua descrição e o chamado vinculado dizem que faz.
- [ ] O escopo está focado numa única preocupação lógica; mudanças não relacionadas são separadas.
- [ ] O projeto se encaixa na arquitetura existente e não introduz um acoplamento fácil de evitar.
- [ ] Casos extremos, caminhos de erro e modos de falha são tratados, não apenas o caminho feliz.
- [ ] Existem testes, são significativos e falhariam se o comportamento regredisse.
- [ ] Nomes, estrutura e comentários tornam o código compreensível a um leitor futuro.
- [ ] Nenhum segredo, credencial, token ou dado pessoal foi commitado.
- [ ] Entradas sensíveis à segurança são validadas, codificadas ou parametrizadas de forma apropriada.
- [ ] Interfaces públicas, contratos e compatibilidade retroativa são preservados ou versionados intencionalmente.
- [ ] Logs, métricas e relato de erros são adequados para operar a mudança em produção.
- [ ] Documentação, runbooks e configuração são atualizados para corresponder à mudança.
- [ ] O feedback é separado em problemas bloqueantes e sugestões, e formulado sobre o código.

## Lista de verificação do autor do pull request

Para o autor antes de pedir revisão.

- [ ] O PR é pequeno e focado o bastante para ser revisado com cuidado numa só sentada.
- [ ] A descrição diz o que mudou, por quê e como foi verificado.
- [ ] O chamado, a issue ou o documento de design vinculado dá aos revisores o contexto necessário.
- [ ] Todas as verificações automatizadas passam localmente ou no CI (build, lint, formato, testes, varreduras).
- [ ] O comportamento novo e o alterado são cobertos por testes.
- [ ] Refatorações mecânicas são separadas das mudanças de comportamento.
- [ ] A autorrevisão está completa: vocês leram o próprio diff linha por linha.
- [ ] Nenhum código de depuração, bloco comentado, segredo ou arquivo solto permanece.
- [ ] Migrações de banco de dados, flags de funcionalidade e mudanças de configuração são documentadas e reversíveis.
- [ ] Mudanças incompatíveis são apontadas explicitamente com um caminho de migração.
- [ ] Capturas de tela, gravações ou saída de exemplo são incluídas onde ajudam a revisão.
- [ ] Os revisores certos e quaisquer aprovadores exigidos por papel são solicitados.

## Definição de Pronto

O padrão compartilhado que um item de trabalho deve cumprir antes de ser considerado completo.

- [ ] Os critérios de aceitação do chamado são todos atendidos e demonstráveis.
- [ ] O código é revisado por pares e aprovado pelos revisores exigidos.
- [ ] Os testes automatizados são escritos, passam e são integrados junto com a mudança.
- [ ] O código é integrado à linha principal e implantado sem problemas pelo pipeline.
- [ ] Nenhum defeito conhecido do limiar de gravidade acordado permanece aberto.
- [ ] Documentação, textos de ajuda e runbooks são atualizados.
- [ ] A observabilidade está no lugar: existem logs, métricas e alertas relevantes.
- [ ] As implicações de segurança e privacidade foram consideradas e tratadas.
- [ ] Os requisitos de acessibilidade da mudança são atendidos quando voltada ao usuário.
- [ ] As flags de funcionalidade estão configuradas e o plano de lançamento está acordado.
- [ ] O dono do produto ou a parte interessada aceitou o resultado.
- [ ] Qualquer trabalho de acompanhamento é registrado como chamados rastreados, não deixado implícito.

## Prontidão para lançamento em produção / go-live

Antes de entregar em produção uma mudança significativa ou um novo serviço.

- [ ] O plano de lançamento está documentado, incluindo os passos em estágios ou canário e os critérios de sucesso.
- [ ] O plano de rollback está documentado, testado e pode ser executado rapidamente.
- [ ] Os testes de capacidade e de carga mostram que o sistema atende a demanda esperada e de pico.
- [ ] Monitoramento, painéis e alertas estão ativos e validados antes do lançamento.
- [ ] A cobertura de sobreaviso está escalada e os responsáveis conhecem o sistema.
- [ ] Existem runbooks para os cenários de falha e operacionais mais prováveis.
- [ ] Dependências, integrações e terceiros estão confirmados como prontos e os limites de taxa entendidos.
- [ ] A revisão de segurança e as aprovações exigidas estão completas.
- [ ] A migração de dados, se houver, é testada de ponta a ponta com um plano de retirada verificado.
- [ ] As flags de funcionalidade permitem desativar a mudança sem reimplantação.
- [ ] As aprovações jurídicas, de privacidade e de conformidade são obtidas onde exigidas.
- [ ] O plano de comunicação cobre as partes interessadas, o suporte e os clientes.
- [ ] Uma decisão de seguir ou parar é tomada por donos nomeados contra critérios explícitos.

## Lista de verificação de revisão de segurança / modelo de ameaças

Para avaliar a postura de segurança de uma mudança ou sistema.

- [ ] As fronteiras de confiança e os fluxos de dados são identificados e documentados.
- [ ] A autenticação é imposta em todo ponto de entrada que a exige.
- [ ] As verificações de autorização impõem o privilégio mínimo para toda ação e recurso.
- [ ] Toda entrada externa é validada, e a saída é codificada para o seu destino.
- [ ] Os segredos são guardados num cofre gerenciado, nunca em código ou configuração, e são rotacionáveis.
- [ ] Os dados são criptografados em trânsito e em repouso conforme a classificação exige.
- [ ] As dependências são varridas atrás de vulnerabilidades conhecidas e mantidas atualizadas.
- [ ] Os riscos de injeção, desserialização e SSRF são mitigados para entradas não confiáveis.
- [ ] Eventos relevantes à segurança são registrados sem gravar dados sensíveis.
- [ ] Limitação de taxa, cotas e proteções contra abuso guardam os endpoints expostos.
- [ ] As mensagens de erro não vazam stack traces, detalhes internos ou informações sensíveis.
- [ ] As ameaças identificadas via STRIDE ou similar são registradas com mitigações ou risco aceito.
- [ ] O teste de segurança (SAST, DAST ou teste de intrusão) está planejado ou completo.

## Lista de verificação de privacidade e proteção de dados (estilo DPIA)

Para tratamento que envolve dados pessoais ou sensíveis.

- [ ] Os dados pessoais coletados são inventariados, classificados e minimizados ao necessário.
- [ ] A base legal ou autoridade de cada finalidade de tratamento está documentada.
- [ ] A limitação de finalidade é imposta: os dados são usados apenas para as finalidades declaradas.
- [ ] Os períodos de retenção são definidos e a exclusão ou anonimização é automatizada.
- [ ] Os direitos do titular dos dados (acesso, correção, exclusão, portabilidade) podem ser atendidos.
- [ ] O consentimento, quando usado, é livre, específico e revogável.
- [ ] Terceiros e operadores estão vinculados a termos adequados de proteção de dados.
- [ ] As transferências internacionais têm um mecanismo legal de transferência apropriado.
- [ ] O acesso a dados pessoais é restrito, registrado e revisado.
- [ ] Os riscos de privacidade aos indivíduos são avaliados e mitigados ou escalados.
- [ ] Os processos de detecção e notificação de violação de dados estão definidos.
- [ ] As escolhas de privacidade desde a concepção e por padrão estão documentadas para a funcionalidade.
- [ ] O encarregado de proteção de dados ou revisor de privacidade aprovou onde exigido.

## Lista de verificação de acessibilidade (WCAG)

Para interfaces voltadas ao usuário, alinhada aos princípios da WCAG.

- [ ] Todo o conteúdo é alcançável e operável usando apenas o teclado.
- [ ] A ordem de foco é lógica e há um indicador de foco visível.
- [ ] O contraste de cor do texto atinge a razão-alvo (tipicamente 4,5:1 para o texto do corpo).
- [ ] Imagens e conteúdo não textual têm texto alternativo significativo.
- [ ] Os campos de formulário têm rótulos associados e mensagens de erro claras.
- [ ] Títulos, marcos e estrutura são marcados semanticamente.
- [ ] Os componentes interativos expõem nome, papel e estado corretos às tecnologias assistivas.
- [ ] O conteúdo se reorganiza e permanece utilizável com zoom de 200% e em telas pequenas.
- [ ] Os limites de tempo são ajustáveis, e o movimento ou o conteúdo de reprodução automática pode ser pausado.
- [ ] A cor não é o único meio de transmitir informação.
- [ ] A mídia tem legendas e, quando necessário, transcrições ou audiodescrição.
- [ ] A interface é testada com um leitor de tela e ferramentas automatizadas de acessibilidade.

## Lista de verificação de revisão de design de API

Antes de publicar ou alterar uma API.

- [ ] A nomenclatura de recursos e operações é consistente e previsível.
- [ ] O contrato é especificado num esquema legível por máquina (por exemplo, OpenAPI).
- [ ] A estratégia de versionamento está definida e a compatibilidade retroativa é preservada ou gerida.
- [ ] Paginação, filtragem e ordenação seguem convenções consistentes.
- [ ] As respostas de erro usam estrutura, códigos e mensagens acionáveis consistentes.
- [ ] Autenticação e autorização são especificadas para cada operação.
- [ ] A validação de entrada e os limites de tamanho são definidos e impostos.
- [ ] A idempotência é definida para as operações em que se esperam repetições.
- [ ] Limites de taxa, cotas e comportamento de limitação são documentados.
- [ ] Timeouts, repetições e semântica de falha são claros para os clientes.
- [ ] A exposição de dados sensíveis nas respostas é minimizada e justificada.
- [ ] A documentação inclui exemplos para cada operação e caso de erro.
- [ ] A política de descontinuação e os prazos de desativação estão definidos.

## Lista de verificação de revisão de decisão de arquitetura (ADR)

Para revisar um registro proposto de decisão de arquitetura.

- [ ] O contexto e o problema a resolver estão declarados com clareza.
- [ ] A decisão é declarada sem ambiguidade como uma única escolha.
- [ ] Pelo menos duas alternativas realistas foram consideradas e comparadas.
- [ ] As consequências, positivas e negativas, estão documentadas.
- [ ] Os impactos não funcionais (desempenho, segurança, custo, operabilidade) são tratados.
- [ ] A decisão se alinha aos princípios existentes e a ADRs anteriores, ou os substitui explicitamente.
- [ ] As equipes e partes interessadas afetadas foram consultadas.
- [ ] A reversibilidade e o custo da mudança são avaliados.
- [ ] Suposições e restrições são tornadas explícitas.
- [ ] O status (proposto, aceito, substituído) está definido e datado.
- [ ] A decisão é descobrível e vinculada a partir dos sistemas relevantes.
- [ ] Quaisquer ações de acompanhamento ou migrações são registradas como trabalho rastreado.

## Lista de verificação de resposta a incidentes

Durante um incidente ativo em produção.

- [ ] Declarem o incidente e designem um único comandante do incidente.
- [ ] Avaliem e comuniquem a gravidade, o escopo e o impacto aos clientes.
- [ ] Abram um canal de comunicação dedicado e um registro do incidente.
- [ ] Atribuam papéis claros: comandante, líder de comunicação e líder de operações.
- [ ] Priorizem a mitigação e a restauração do serviço sobre a análise de causa-raiz.
- [ ] Publiquem atualizações regulares de status às partes interessadas numa cadência definida.
- [ ] Capturem uma linha do tempo de eventos, ações e decisões conforme acontecem.
- [ ] Escalem para respondentes adicionais ou fornecedores quando necessário.
- [ ] Notifiquem o jurídico, a segurança e a conformidade se dados ou regulamentação estiverem envolvidos.
- [ ] Verifiquem a correção e confirmem que o sistema se recuperou por completo.
- [ ] Encerrem formalmente o incidente e comuniquem a resolução.
- [ ] Agendem o post-mortem sem atribuição de culpa antes que as pessoas se dispersem.

## Lista de verificação de post-mortem

Para a revisão retrospectiva após um incidente.

- [ ] A revisão é sem atribuição de culpa e foca sistemas e fatores contribuintes.
- [ ] Uma linha do tempo factual e com carimbos de data e hora do incidente está documentada.
- [ ] O impacto aos clientes e ao negócio é quantificado (duração, escopo, custo).
- [ ] A detecção é analisada: como e quando o problema foi notado.
- [ ] A resposta é analisada: o que ajudou e o que atrasou a recuperação.
- [ ] As causas contribuintes são identificadas, não apenas uma única causa-raiz.
- [ ] O que correu bem é registrado, assim como o que deu errado.
- [ ] Os itens de ação são específicos, atribuídos a donos e têm prazos.
- [ ] Os itens de ação tratam de prevenção, detecção e mitigação.
- [ ] Os itens de acompanhamento são rastreados até a conclusão no backlog normal.
- [ ] O post-mortem é compartilhado amplamente para que outros possam aprender com ele.
- [ ] Os padrões sistêmicos entre incidentes são revisados periodicamente.

## Lista de verificação de prontidão para o sobreaviso

Antes de alguém assumir um turno de sobreaviso.

- [ ] O respondente tem acesso a todos os sistemas, painéis e ferramentas de que precisa.
- [ ] O alerta chega ao respondente de forma confiável e é testado.
- [ ] Os caminhos de escalação e os contatos do sobreaviso secundário são conhecidos e atuais.
- [ ] Existem runbooks para os alertas mais comuns e mais graves.
- [ ] O respondente concluiu a integração ou o acompanhamento em sombra para esses sistemas.
- [ ] Mudanças recentes, incidentes em curso e problemas conhecidos são repassados.
- [ ] Os limiares de alerta são ajustados para minimizar o ruído e os acionamentos falsos.
- [ ] O respondente sabe como declarar um incidente e alcançar o comandante.
- [ ] O acesso à produção é possível a partir do ambiente de trabalho do respondente.
- [ ] Os canais de comunicação e os contatos das partes interessadas estão documentados.
- [ ] A escala de sobreaviso é publicada e a cobertura não tem lacunas.
- [ ] A compensação, as expectativas e os limites de carga de trabalho do sobreaviso são claros.

## Lista de verificação de definição de SLO

Ao definir um objetivo de nível de serviço.

- [ ] A jornada do usuário ou capacidade que o SLO protege está claramente identificada.
- [ ] Os indicadores de nível de serviço (SLIs) são definidos como grandezas claras e mensuráveis.
- [ ] Os SLIs são medidos da perspectiva do usuário sempre que possível.
- [ ] A meta do objetivo é definida num nível de que os usuários de fato precisam, não 100%.
- [ ] A janela de medição (por exemplo, 28 dias móveis) está especificada.
- [ ] O orçamento de erros derivado da meta é calculado e compreendido.
- [ ] Uma política define o que acontece quando o orçamento de erros se esgota.
- [ ] As fontes de dados dos SLIs são confiáveis e instrumentadas.
- [ ] O alerta está atado à taxa de queima, não apenas a violações de limiar.
- [ ] Donos e partes interessadas concordam que o SLO é realista e significativo.
- [ ] O SLO está documentado e visível num painel.
- [ ] Existe um calendário para revisar e rever os SLOs conforme o serviço evolui.

## Lista de verificação de pipeline de CI/CD

Para um pipeline de integração e entrega contínuas.

- [ ] Todo commit dispara um build e uma execução de testes automatizados.
- [ ] O pipeline falha rápido e relata os resultados com clareza aos autores.
- [ ] Lint, formatação e análise estática rodam automaticamente.
- [ ] Testes unitários, de integração e os de ponta a ponta relevantes rodam no pipeline.
- [ ] A varredura de segurança e de dependências roda em todo build.
- [ ] Os artefatos de build são versionados, imutáveis e guardados num registro.
- [ ] Os segredos são injetados com segurança e nunca impressos nos logs.
- [ ] As implantações são automatizadas e repetíveis entre ambientes.
- [ ] A estratégia de implantação (canário, azul-verde, gradual) está definida e é usada.
- [ ] O rollback é automatizado ou uma única ação documentada.
- [ ] As permissões do pipeline seguem o privilégio mínimo e são auditáveis.
- [ ] A configuração do pipeline é guardada no controle de versão como código.
- [ ] A procedência do build e uma lista de materiais de software são produzidas onde exigido.

## Lista de verificação de revisão de infraestrutura como código

Para revisar infraestrutura definida como código.

- [ ] As mudanças são expressas inteiramente em código e aplicadas pelo pipeline.
- [ ] Um plano ou a saída de uma execução a seco é revisado antes de aplicar.
- [ ] O estado é guardado com segurança e com bloqueio para prevenir mudanças concorrentes.
- [ ] Os recursos seguem convenções de nomenclatura, etiquetagem e propriedade.
- [ ] Papéis e políticas de IAM de privilégio mínimo são usados, sem curingas onde evitável.
- [ ] A exposição de rede é minimizada; sem acesso público não intencional.
- [ ] Segredos e valores sensíveis são referenciados de um cofre, não fixados no código.
- [ ] A criptografia está habilitada para armazenamento, bancos de dados e trânsito.
- [ ] As mudanças são idempotentes e seguras de reaplicar.
- [ ] O raio de impacto é compreendido; as mudanças destrutivas são apontadas.
- [ ] O impacto de custo da mudança é considerado.
- [ ] Os módulos são reutilizáveis, versionados e testados.
- [ ] Existe detecção de deriva para pegar mudanças fora do pipeline.

## Lista de verificação de lançamento de modelo de IA/ML

Antes de lançar um modelo de aprendizado de máquina em produção.

- [ ] O uso pretendido, o escopo e as limitações do modelo estão documentados.
- [ ] A procedência, o licenciamento e o consentimento dos dados de treinamento e avaliação são verificados.
- [ ] Os dados e o modelo são versionados e reproduzíveis.
- [ ] O desempenho é avaliado em dados de teste representativos e separados.
- [ ] A equidade e o viés são avaliados entre os subgrupos relevantes.
- [ ] O modelo é avaliado contra o incumbente ou uma linha de base.
- [ ] Os modos de falha, os casos extremos e o comportamento fora da distribuição são compreendidos.
- [ ] Os riscos de segurança, mau uso e saídas nocivas são avaliados e mitigados.
- [ ] Existe monitoramento de deriva, qualidade dos dados e degradação de desempenho.
- [ ] Existe um rollback ou alternativa para um modelo anterior ou um caminho baseado em regras.
- [ ] Supervisão humana ou recurso é oferecido para decisões consequentes.
- [ ] A revisão de privacidade cobre os dados de treinamento e as entradas e saídas de inferência.
- [ ] Um cartão do modelo ou documentação equivalente é publicado para as partes interessadas.

## Lista de verificação de qualidade de pipeline de dados

Para um pipeline de dados que alimenta análises ou produtos.

- [ ] Os esquemas dos dados de origem são validados e as mudanças de esquema são detectadas.
- [ ] A ingestão trata corretamente registros atrasados, duplicados e fora de ordem.
- [ ] As verificações de qualidade de dados (completude, unicidade, faixas) rodam automaticamente.
- [ ] Os registros com falha são postos em quarentena e expostos, não descartados em silêncio.
- [ ] As transformações são testadas com entradas representativas e de casos extremos.
- [ ] O pipeline é idempotente e seguro de reexecutar após uma falha.
- [ ] A atualidade e a latência das saídas são monitoradas contra as expectativas.
- [ ] A linhagem é documentada para que os consumidores saibam de onde vêm os dados.
- [ ] Dados pessoais e sensíveis são classificados, mascarados ou restritos de forma apropriada.
- [ ] Reprocessamentos e preenchimentos retroativos são suportados e documentados.
- [ ] O alerta notifica os donos de falhas e violações de qualidade.
- [ ] As políticas de retenção e exclusão são impostas aos dados armazenados.
- [ ] Os consumidores a jusante e os SLAs são documentados.

## Lista de verificação de admissão de código aberto e revisão de licença

Antes de adotar um componente de código aberto.

- [ ] A licença do componente é identificada e consta na lista aprovada.
- [ ] As obrigações da licença (atribuição, copyleft, avisos) são compreendidas e cumpridas.
- [ ] A compatibilidade da licença com o seu modelo de distribuição é confirmada.
- [ ] O projeto é ativamente mantido e tem uma comunidade saudável.
- [ ] As vulnerabilidades conhecidas são conferidas e a versão está atual.
- [ ] A dependência e suas dependências transitivas são inventariadas.
- [ ] A postura de segurança e o histórico de incidentes passados são revisados.
- [ ] O componente atende a uma necessidade real sem duplicação significativa.
- [ ] O custo de saída e a substituibilidade do componente são considerados.
- [ ] O componente é registrado na lista de materiais de software.
- [ ] Um dono nomeado é responsável por acompanhar atualizações e avisos.
- [ ] As políticas de contribuição de volta e de fork interno são seguidas se ele for modificado.

## Lista de verificação de risco de fornecedor / terceiros

Antes de integrar um fornecedor ou serviço externo.

- [ ] A necessidade de negócio e os dados a que o fornecedor terá acesso estão claramente definidos.
- [ ] A postura de segurança do fornecedor é avaliada (certificações, auditorias, questionário).
- [ ] Os termos de tratamento de dados, a propriedade e a exclusão na saída são contratualmente claros.
- [ ] Os subprocessadores e as localizações de dados do fornecedor são divulgados e aceitáveis.
- [ ] A conformidade com as regulamentações relevantes é verificada.
- [ ] Os compromissos de disponibilidade, suporte e SLA estão documentados.
- [ ] As obrigações e prazos de notificação de violação estão no contrato.
- [ ] O acesso é limitado ao privilégio mínimo e revogável.
- [ ] A continuidade de negócios e o impacto da falha do fornecedor são avaliados.
- [ ] Existe um plano de saída e de migração de dados para evitar o aprisionamento (lock-in).
- [ ] Custos, termos de renovação e cláusulas de mudança de preço são compreendidos.
- [ ] O fornecedor é adicionado ao registro de riscos com uma data de revisão.

## Lista de verificação de prontidão de conformidade governamental (estilo ATO / FedRAMP)

Para sistemas que exigem autorização formal para operar.

- [ ] A fronteira do sistema e os fluxos de dados são definidos e diagramados.
- [ ] Os dados são categorizados por nível de impacto e sensibilidade.
- [ ] A linha de base de controles aplicável é selecionada e adaptada.
- [ ] Um plano de segurança do sistema documenta como cada controle é implementado.
- [ ] Os controles são implementados, evidenciados e mapeados ao plano.
- [ ] O monitoramento contínuo e a varredura de vulnerabilidades estão operacionais.
- [ ] Um plano de ação e marcos acompanha os achados abertos até a remediação.
- [ ] O controle de acesso, o registro de auditoria e a gestão de identidade atendem aos requisitos.
- [ ] A criptografia usa algoritmos aprovados e módulos validados.
- [ ] Um plano de resposta a incidentes está documentado e testado.
- [ ] Um plano de contingência e de recuperação de desastres está documentado e testado.
- [ ] Uma avaliação ou auditoria independente dos controles está concluída.
- [ ] O responsável autorizador tem a avaliação de risco necessária para conceder a autorização.
- [ ] Os gatilhos de reautorização e a cadência contínua de autorização estão definidos.
