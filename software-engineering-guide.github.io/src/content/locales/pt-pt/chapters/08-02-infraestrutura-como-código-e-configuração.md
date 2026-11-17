# 8.2 Infraestrutura como código e configuração

## Visão geral e motivação

A [infraestrutura como código](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) significa definir e provisionar a infraestrutura (redes, servidores, bancos de dados, balanceadores de carga, permissões) por meio de arquivos de definição legíveis por máquina em vez de cliques manuais no console ou scripts avulsos. A [gestão de configuração](https://en.wikipedia.org/wiki/Configuration_management) estende a mesma ideia às definições e ao estado dos sistemas depois que eles existem. Juntas, transformam a infraestrutura de um artefato frágil e feito à mão em um produto versionado, revisável e reproduzível da mesma disciplina de engenharia que vocês usam para o código de aplicação.

Para grandes equipes, a IaC não é uma conveniência, é uma necessidade. Quando centenas de engenheiros precisam de ambientes e milhares de recursos precisam permanecer consistentes entre regiões e contas, o provisionamento manual não acompanha o ritmo e não se mantém correto. A infraestrutura configurada por humanos deriva, cedo ou tarde, para servidores “floco de neve” únicos que ninguém entende por completo e que não podem ser reconstruídos com confiabilidade depois de uma falha. Codificar a infraestrutura a torna consistente, auditável e descartável. Qualquer ambiente pode ser recriado a partir de sua definição, e qualquer mudança é um diff revisável.

As organizações corporativas e governamentais ganham mais um benefício decisivo: governança impositiva. Os requisitos de segurança e de conformidade, como criptografia em repouso, segmentação de rede, regiões aprovadas e etiquetas para alocação de custos, podem ser embutidos diretamente no código e verificados automaticamente antes de qualquer coisa ser provisionada. Em vez de auditar a infraestrutura depois do fato e perseguir violações, vocês impedem que a infraestrutura fora de conformidade chegue a existir. Essa passagem da detecção para a prevenção é a razão central pela qual a IaC se tornou fundamental para a prática moderna de plataforma.

## Princípios fundamentais

- Prefiram definições declarativas, que descrevem o estado desejado, a scripts imperativos, que descrevem passos.
- Guardem todas as definições de infraestrutura em controle de versões, revisadas como qualquer outro código.
- Tratem a infraestrutura como imutável: substituam em vez de modificar no lugar.
- Tornem o provisionamento idempotente, de modo que aplicar a mesma definição repetidamente dê o mesmo resultado.
- Detectem e reconciliem continuamente a deriva (drift), o ambiente vivo divergindo da definição declarada. O código, não o sistema vivo, é a fonte da verdade.
- Componham a infraestrutura de módulos reutilizáveis e versionados em vez de copiar e colar.
- Codifiquem a política como código, regras organizacionais expressas como código verificável por máquina, para que os guardrails sejam automáticos e não apenas consultivos.
- Mantenham os segredos fora das definições. Referenciem-nos de um gerenciador de segredos dedicado.

## Recomendações

### Escolha ferramentas declarativas e estruture-as em torno de módulos

Adotem uma ferramenta declarativa de IaC, como o [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), o Pulumi ou uma opção nativa da nuvem como o CloudFormation, e padronizem nela em toda a organização para evitar um panorama fragmentado de ferramentas. A prática arquitetural central é a modularidade: construam módulos pequenos, bem documentados e versionados que capturem padrões comuns (uma rede em conformidade, um banco de dados endurecido, um serviço padrão). As equipes então compõem ambientes a partir desses módulos em vez de escrever recursos brutos. Isso espalha automaticamente bons padrões e configurações de segurança e reduz drasticamente a duplicação.

### Gerencie o estado deliberadamente

As ferramentas declarativas acompanham o mapeamento entre código e recursos reais num arquivo de estado. Guardem o estado remotamente num backend compartilhado, criptografado e com controle de acesso, e usem travas para que modificações concorrentes não o corrompam. Nunca mantenham o estado num laptop e nunca o editem à mão, exceto como ação de recuperação de último recurso. O estado é sensível, porque pode conter metadados de recursos e segredos, então protejam-no de acordo.

### Construa infraestrutura imutável com imagens de ouro

Em vez de remendar servidores em execução, assem uma “imagem de ouro” (golden image) versionada (uma imagem de máquina ou de contêiner pré-configurada e endurecida) e implantem instâncias novas a partir dela. Quando precisarem de uma mudança ou correção, construam uma nova imagem e distribuam-na, aposentando as instâncias antigas. Isso elimina a deriva de configuração, torna trivial a reversão e mantém toda instância idêntica e rastreável a uma construção sabidamente boa. Os pipelines automatizados de imagem devem incluir endurecimento de segurança e varredura, para que a conformidade esteja embutida no nível da imagem.

### Detecte e reconcilie a deriva de configuração

A deriva acontece quando o ambiente vivo diverge de sua definição, em geral porque alguém fez uma mudança manual de emergência. Rodem uma detecção regular de deriva que compare o estado real com o estado declarado e sinalize as diferenças. Tratem a deriva como um defeito: reconciliem atualizando o código e reaplicando, não deixando a mudança manual no lugar. Para sistemas que precisam de imposição contínua de configuração, usem uma ferramenta de gestão de configuração que converja continuamente os hosts ao seu estado declarado.

### Adote o GitOps e a implantação por tração

No modelo GitOps, um repositório Git guarda o estado desejado declarado do sistema, e um agente automatizado rodando dentro do ambiente-alvo puxa continuamente esse estado e reconcilia o sistema vivo para coincidir com ele. Isso inverte o modelo tradicional de empurrar. Nenhum sistema externo precisa de credenciais permanentes para mudar o ambiente, porque o ambiente puxa a própria configuração. O GitOps dá um rastro de auditoria completo (toda mudança é um commit), reversão fácil (revertam o commit) e forte correção de deriva (o agente reafirma continuamente o estado desejado). É especialmente poderoso para o [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) e para organizações que querem uma fonte da verdade única e revisável.

### Imponha guardrails com política como código

Expressem as regras organizacionais, como regiões permitidas, criptografia obrigatória, etiquetas exigidas e exposição pública proibida, como políticas verificáveis por máquina usando uma ferramenta como o Open Policy Agent (OPA) ou um motor de políticas nativo da plataforma como o Sentinel. Rodem essas verificações no pipeline antes do provisionamento, para que as violações sejam bloqueadas automaticamente. A política como código transforma a intenção de uma equipe de segurança num controle executável e aplicado de modo uniforme, e escala a milhares de mudanças de um jeito que a revisão manual nunca conseguiria.

## Compromissos: prós e contras

| Escolha | Prós | Contras | Melhor ajuste |
|---|---|---|---|
| IaC declarativa (Terraform/Pulumi) | Reproduzível, revisável, com deriva detectável | Curva de aprendizado. Complexidade na gestão de estado | Quase todas as equipes em escala |
| Scripts imperativos | Familiares. Flexíveis para casos pontuais | Não idempotentes. Difíceis de auditar e repetir | Casos estreitos e transitórios |
| Imutável + imagens de ouro | Sem deriva. Reversão trivial | Sobrecarga do pipeline de build de imagens | Frotas que precisam de consistência |
| Gestão de configuração mutável | Controle contínuo e fino | Risco de deriva. Convergência mais lenta | Hosts legados ou de vida longa |
| GitOps (por tração) | Forte rastro de auditoria. Autocura | Exige agente no cluster e disciplina de Git | Kubernetes e nativo da nuvem |
| Política como código | Guardrails automáticos e uniformes | Esforço inicial de redação das políticas | Ambientes regulados |

A tensão principal é entre flexibilidade e controle. As abordagens manuais e imperativas parecem mais rápidas para uma única mudança, mas acumulam inconsistência oculta que se torna paralisante em escala. A infraestrutura declarativa, imutável e governada por políticas pede mais investimento inicial e uma mudança cultural real, já que os engenheiros precisam parar de fazer mudanças rápidas no console, mas devolve esse investimento muitas vezes em confiabilidade, auditabilidade e na capacidade de reconstruir qualquer coisa sob demanda.

## Perguntas para discutir com sua equipe

1. **Quem é dono da biblioteca compartilhada de módulos, e como uma melhoria num módulo chega a toda equipe que o usa?** Os módulos só compensam se as correções e os padrões endurecidos se propagarem, e isso exige propriedade clara e versionamento de verdade, não uma pasta da qual todos copiam. Decidam quem mantém os módulos de rede em conformidade e de banco de dados endurecido, como os versionam (versionamento semântico com registro de mudanças) e como as equipes puxam atualizações sem um alarme de incêndio. Em escala, essa é a diferença entre consertar uma configuração errada uma só vez e persegui-la por mil recursos editados à mão. Levem evidências: quantas cópias distintas do mesmo padrão existem hoje, quanto tempo uma correção de segurança leva para chegar a todo ambiente e se as equipes fixam as versões dos módulos ou as deixam flutuar. Se uma correção crítica não consegue chegar a todo o patrimônio em dias, a sua modularidade é cosmética.

2. **Qual é a sua cadência de detecção de deriva, e o que de fato acontece quando uma deriva é achada?** A deriva é o ambiente vivo divergindo em silêncio do seu estado declarado, em geral por uma mudança de emergência no console, e tolerá-la transforma o seu código em ficção. Decidam com que frequência comparam o estado real com o declarado (noturno é um padrão razoável) e, mais importante, decidam a resposta: reconciliar atualizando o código e reaplicando, nunca deixando a mudança manual no lugar. Em contextos regulados, isso é uma exigência de controle, porque os auditores precisam que o estado declarado coincida com a realidade continuamente. Levem os seus números atuais: quantos recursos derivam por semana, quanto tempo permanecem à deriva e se alguém é responsável por encerrá-los. Tratem toda deriva como um defeito com dono, ou a garantia de fonte da verdade se erode até ninguém confiar no código.

3. **Vocês migraram para o GitOps e a reconciliação por tração, ou um sistema externo ainda guarda credenciais permanentes para mudar a produção?** No modelo de tração, um agente dentro do ambiente-alvo reconcilia continuamente o sistema vivo com o Git, o que dispensa que qualquer sistema externo tenha acesso de escrita, e reafirma o estado desejado de modo que a deriva se autocorrige. Essa é uma postura forte de segurança e de auditoria, já que toda mudança é um commit e nenhum operador precisa de credenciais permanentes de produção. O custo é real: um agente no cluster para operar e uma disciplina rigorosa de Git, então pesem isso contra a sua automação atual baseada em empurrar. Levem a lista de quem e do que pode hoje alterar a produção diretamente e que rastro de auditoria essas mudanças deixam. Para o Kubernetes e para enclaves de alta garantia, essa mudança geralmente vale a pena; para um punhado de recursos estáticos pode ser exagero.

4. **Como o estado da sua infraestrutura é guardado, travado e controlado em acesso, e o que acontece no dia em que ele for corrompido ou perdido?** O estado é o mapa entre o código e os recursos reais, então um arquivo de estado perdido ou danificado pode deixar uma ferramenta cega para recursos que ela mesma criou e tentar alguém a uma reaplicação destrutiva. Para uma grande equipe o risco se multiplica, porque muitos engenheiros aplicando contra um estado compartilhado precisam de um backend remoto, criptografado e travado para que execuções concorrentes não se atropelem. Pesem a conveniência de um grande estado contra o raio de impacto que ele cria e considerem dividir o estado por ambiente ou por domínio para que um único erro não derrube tudo. Levem os fatos: onde o estado vive hoje, se a trava é imposta, quem pode lê-lo (ele pode conter segredos) e se vocês já ensaiaram uma recuperação. Em contextos corporativos e governamentais, tratem o backend de estado como um ativo sensível e com controle de acesso, com backup, log de auditoria e runbook de recuperação próprios, porque perdê-lo é perder o registro do que existe.

5. **Quando uma emergência genuína exige uma mudança manual, qual é o caminho sancionado de quebra de vidro (break-glass), e como essa mudança é reincorporada ao código?** Toda prática madura de IaC acaba encontrando o incidente das 3 da manhã em que esperar por um pipeline é inaceitável, e a pergunta honesta não é se as mudanças manuais acontecem, e sim como vocês as contêm. Decidam de antemão quem pode contornar o pipeline, no que pode mexer, como a ação é registrada e o prazo em que a mudança precisa ser reconciliada no código ou revertida. Sem esse acordo, a exceção de emergência vira em silêncio o hábito do dia a dia e o ClickOps volta pela porta dos fundos. Levem evidências: quantas mudanças fora de banda aconteceram no último trimestre, quanto tempo cada uma ficou sem reconciliação e se a detecção de deriva de fato as pegou. Para órgãos regulados e públicos, um procedimento documentado de quebra de vidro com registro automático costuma ser uma exigência de controle, porque os auditores esperam tanto que as emergências sejam possíveis quanto que cada uma deixe um rastro e devolva o sistema ao seu estado declarado.

6. **Quanto da sua linha de base de segurança e de conformidade está expresso como política que bloqueia automaticamente uma mudança ruim, versus regras que vivem num documento e dependem de alguém se lembrar delas?** Os guardrails escritos como prosa numa wiki são violados rotineiramente, porque dependem de todo engenheiro lê-los e aplicá-los sob pressão de prazo, enquanto as mesmas regras expressas como política como código rejeitam uma mudança fora de conformidade antes de ela ser provisionada. Para uma grande organização, esse é o único jeito de a intenção de uma equipe de segurança escalar a milhares de mudanças sem virar um gargalo de revisão. Pesem o custo inicial de redigir e manter políticas contra o custo recorrente da revisão manual e da remediação após o fato e decidam quais controles (criptografia, regiões aprovadas, etiquetas obrigatórias, nenhuma exposição pública) são inegociáveis o bastante para serem impostos como portões duros. Levem a lista das suas regras atuais de linha de base e marquem quais são automatizadas versus consultivas, mais com que frequência cada uma é violada na prática. Em contextos corporativos e governamentais, a política automatizada converte uma auditoria de semanas de coleta manual de evidências numa consulta a controles impostos e transforma a conformidade de detecção em prevenção.

## Perspectiva por setor

**Startup.** A velocidade vence, então ponham toda a sua pilha num único repositório declarativo (o Terraform é um padrão comum), guardem o estado num backend gerenciado e criptografado e façam toda mudança passar por um pull request mesmo com uma equipe de três. Pulem o aparato pesado de plataforma: nada de equipe central de módulos, nada de motor de políticas ainda, só controle de versões e a disciplina de nunca clicar no console. Só isso já dá ambientes reproduzíveis que vocês podem derrubar para economizar dinheiro e reconstruir para a próxima demonstração.

**Pequena empresa.** Sem especialista dedicado em plataforma, apoiem-se em serviços gerenciados e em qualquer IaC que o seu provedor de nuvem ou fornecedor já suporte, em vez de montar ferramentas sob medida que vocês não conseguem manter. Favoreçam comprar uma plataforma hospedada cujos padrões sensatos (criptografia, backups, aplicação de correções) são tratados para vocês a construir um pipeline de imagens de ouro que ninguém tem para operar. Enquadrem o objetivo de modo estreito: ponham o seu punhado de recursos críticos em código para poder reconstruí-los depois de uma falha ou da saída de um prestador.

**Grande empresa.** O problema central é a consistência entre muitas equipes, contas e regiões, então invistam numa biblioteca compartilhada e versionada de módulos, estado remoto e travado e política como código imposta no pipeline. Uma equipe central de plataforma publica módulos e guardrails endurecidos enquanto as equipes de produto se servem sozinhas dentro deles, e a detecção de deriva roda continuamente para que milhares de recursos permaneçam num estado conhecido. Orcem o custo contínuo de manter módulos e políticas, porque o valor deles vem de uma correção ou de um padrão endurecido se propagarem por toda parte de uma vez.

**Governo.** As regras de contratação, a acreditação e a prestação de contas públicas empurram para a infraestrutura imutável, commits assinados e reconciliação GitOps dentro de um enclave acreditado, de modo que nenhum operador tenha credenciais permanentes para mudar a produção. Codifiquem a linha de base de segurança exigida em imagens de ouro e em política como código e deixem o histórico de commits servir de evidência de auditoria à prova de adulteração e continuamente disponível. Favoreçam ferramentas abertas e portáveis a formatos proprietários que prendem vocês e tornem explícitos o procedimento de quebra de vidro e seu registro, para que as mudanças de emergência ainda satisfaçam as exigências de controle de configuração.

## Exemplos

**Startup.** Uma startup de cinco pessoas define toda a sua configuração na AWS, ou seja, a VPC, o banco de dados e o serviço de contêineres, num único repositório Terraform com o estado guardado num backend S3 criptografado e trava via DynamoDB. Toda mudança passa por um pull request, de modo que até um engenheiro de sobreaviso sozinho consegue ver exatamente o que vai mudar antes de rodar o apply. Quando precisam de um ambiente de staging novo para uma grande demonstração, copiam um pequeno módulo e o montam em minutos, e o derrubam com a mesma rapidez para manter baixa a conta da nuvem.

**Grande empresa.** Uma varejista multinacional gerencia a infraestrutura em várias contas e regiões de nuvem. Uma equipe central de plataforma publica módulos Terraform versionados para redes em conformidade, bancos de dados e estrutura de serviços e impõe políticas OPA que rejeitam qualquer recurso sem criptografia ou sem etiquetas de alocação de custos. As equipes de produto provisionam seus próprios ambientes em autoatendimento, mas toda mudança passa pelo pipeline, onde a política é verificada automaticamente. A detecção de deriva roda toda noite e abre chamados para qualquer mudança manual, mantendo milhares de recursos continuamente num estado conhecido e em conformidade.

**Governo.** Uma agência de defesa que opera num ambiente de alta garantia constrói imagens de ouro endurecidas que embutem a linha de base de segurança exigida e implanta apenas instâncias imutáveis a partir dessas imagens. Toda a infraestrutura é declarada no Git e reconciliada por um agente GitOps dentro do enclave acreditado, de modo que nenhum operador tem credenciais permanentes para mudar a produção diretamente. Toda mudança é um commit assinado. Isso dá aos auditores um histórico completo e à prova de adulteração e satisfaz as exigências de monitoramento contínuo e de controle de configuração sem coleta manual de evidências.

## Justificativa de negócio: motivações, ROI e TCO

O ROI da IaC vem de velocidade, confiabilidade e redução de risco. Ambientes que antes levavam semanas de provisionamento manual guiado por chamados podem ser criados em minutos, o que libera engenheiros e acelera projetos. A reprodutibilidade corta o tempo de recuperação após falhas, porque qualquer ambiente pode ser reconstruído a partir do código. A imposição automatizada de políticas reduz a frequência e o custo de incidentes de segurança e de achados de auditoria, o que para organizações reguladas pode ser substancial.

No livro-razão do TCO, os custos de adoção incluem ferramentas, treinamento, construir uma biblioteca de módulos e de políticas e a disciplina de parar de fazer mudanças manuais. O custo de não adotar é mais íngreme e se compõe com o tempo: infraestrutura floco de neve que ninguém consegue reconstruir, provisionamento lento e sujeito a erros, configurações de segurança erradas que levam a violações e auditorias que consomem semanas de esforço manual. Para a liderança, enquadrem a IaC como a conversão da infraestrutura de um passivo não gerenciado num ativo governado e reproduzível e como o mecanismo que torna a segurança e a conformidade automáticas em vez de aspiracionais.

## Antipadrões e armadilhas

- **ClickOps em produção.** Fazer mudanças à mão no console garante a deriva e destrói a reprodutibilidade.
- **Segredos no código.** Gravar credenciais nos arquivos de definição as vaza para o histórico de versões e para o estado.
- **Definições monolíticas e sem módulos.** Uma configuração enorme em que ninguém ousa mexer fica tão frágil quanto a montagem manual que ela substituiu.
- **Estado não gerenciado.** Arquivos de estado locais ou sem trava levam à corrupção e à infraestrutura perdida.
- **Deriva tolerada.** Deixar mudanças manuais no lugar erode a garantia de fonte da verdade até o código virar ficção.
- **Política como documentação.** Regras que vivem numa wiki em vez de numa verificação automatizada são rotineiramente violadas.
- **Proliferação de copiar e colar.** Duplicar a configuração entre equipes significa que correções e melhorias nunca se espalham.

## Modelo de maturidade

**Nível 1: Iniciar.** A infraestrutura é provisionada manualmente pelo console e por scripts ad hoc. Os ambientes são inconsistentes, sem documentação e não podem ser reproduzidos com confiabilidade, e a recuperação de uma falha é lenta e incerta.

**Nível 2: Desenvolver.** Parte da infraestrutura é codificada, mas as práticas variam por equipe. A gestão de estado é inconsistente, a deriva é comum, os segredos às vezes vazam para as definições e a política é imposta, se tanto, por revisão manual.

**Nível 3: Padronizar.** A IaC declarativa é o padrão documentado em toda a organização, construída a partir de módulos compartilhados e versionados, com estado remoto, gerenciado e travado. A política como código impõe guardrails no pipeline, os segredos são referenciados de um gerenciador dedicado e a detecção de deriva roda numa cadência regular.

**Nível 4: Gerenciar.** A prática é medida em relação a linhas de base. Vocês acompanham a taxa de deriva e o tempo médio de reconciliação, a adoção de versões de módulos entre equipes, as violações de política bloqueadas versus escapadas, o prazo de provisionamento e a fração dos recursos de fato sob código. Essas métricas condicionam as mudanças e orientam onde investir, de modo que as decisões repousam em evidências e não em anedotas.

**Nível 5: Orquestrar.** A infraestrutura é imutável e guiada por GitOps, autocurável contra a deriva, com evidência de conformidade produzida automaticamente. A biblioteca de módulos e de políticas melhora continuamente a partir do uso real e dos incidentes, e a prática de infraestrutura é integrada ao planejamento de segurança, custo e entrega para que todo o patrimônio se adapte conforme os requisitos mudam.

## Ideias para discussão

- Onde deve ficar a linha entre módulos governados centralmente e a autonomia das equipes para definir infraestrutura própria?
- Como vocês tratam a mudança de emergência genuína que precisa contornar o pipeline, sem normalizar o ClickOps?
- Qual é a estratégia certa para gerenciar e proteger o estado entre muitas contas e equipes?
- Quando a gestão de configuração mutável ainda se justifica versus a infraestrutura totalmente imutável?
- Como vocês mantêm a biblioteca de política como código alinhada com os requisitos de segurança e regulatórios em evolução?
- Como é um caminho realista de migração para a infraestrutura legada que antecede a IaC?

## Principais conclusões

- Definam a infraestrutura de forma declarativa, versionem-na e tratem-na como código revisável e reproduzível.
- Construam a partir de módulos pequenos e versionados para espalhar bons padrões e eliminar a duplicação.
- Prefiram a infraestrutura imutável e as imagens de ouro para abolir a deriva e simplificar a reversão.
- Gerenciem o estado deliberadamente e mantenham os segredos fora das definições.
- Adotem o GitOps para um forte rastro de auditoria e uma reconciliação que se autocura.
- Imponham guardrails com política como código, para que a conformidade seja prevenida e não auditada depois do fato.

## Referências e leitura complementar

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
