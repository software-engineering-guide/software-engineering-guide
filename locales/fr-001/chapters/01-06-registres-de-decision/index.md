# 1.6 Registres de décision

## Vue d'ensemble et motivation

Un **registre de décision** est un document qui capture une décision importante avec son contexte et ses conséquences. La forme la plus connue est le **[registre de décision d'architecture](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, une note courte, immuable de préférence, qui enregistre un choix architecturalement significatif, pourquoi il a été fait, et ce qui en découle. L'ensemble complet des registres d'un projet est son **journal de décisions (ADL)**, et la discipline de les tenir fait partie de la **gestion des connaissances d'architecture (AKM)**. Ce chapitre s'appuie sur les pratiques de prise de décision et de gouvernance du chapitre 1.5, en se concentrant sur comment vous écrivez, stockez, et entretenez les registres de décision à grande échelle.

La motivation est simple, et douloureuse à apprendre à ses dépens. Sur tout système à longue durée de vie, la question la plus coûteuse est « pourquoi diable a-t-il été construit ainsi ? », posée des mois ou des années plus tard par des personnes qui n'étaient pas dans la pièce. Le code montre *ce que* le système fait. Les tests montrent qu'il *fonctionne*. Mais ni l'un ni l'autre ne capture *pourquoi* vous avez choisi ce chemin plutôt que les alternatives que vous avez envisagées et rejetées. Sans registres de décision, ce raisonnement s'évapore avec le renouvellement du personnel. Les équipes replaident des questions réglées, inversent de bonnes décisions pour de mauvaises raisons, ou gardent de mauvaises décisions par peur. Un registre de décision est une lettre peu coûteuse au futur qui préserve le raisonnement.

Pour les grandes équipes, c'est un outil de coordination autant qu'une aide-mémoire. Les entreprises font fonctionner des dizaines d'équipes prenant des décisions qui se chevauchent. Un journal de décisions partagé transforme le raisonnement durement acquis d'une équipe en un atout réutilisable, et empêche des décisions divergentes et incompatibles. Dans les contextes gouvernementaux et réglementés, les registres de décision sont proches de l'obligation. Les auditeurs, les organismes de surveillance, et les entrepreneurs successeurs ont tous besoin d'une justification traçable reliant les exigences architecturalement significatives aux choix faits face à elles. Un journal de décisions bien tenu fait souvent la différence entre un système que vous pouvez garantir et auditer et un système que vous ne pouvez pas.

## Principes clés

- **Enregistrez le *pourquoi*, pas seulement le *quoi*.** Le contexte et les alternatives rejetées sont le but.
- **Une décision par registre.** Gardez chaque registre spécifique et autonome.
- **Petit et léger vaut mieux que complet et inutilisé.** Un registre d'une page qui existe vaut mieux qu'un rapport jamais écrit.
- **Horodatez tout.** Les coûts, les contraintes, et les fournisseurs changent ; datez chaque affirmation.
- **Préférez un journal vivant, avec pragmatisme.** L'immuabilité est l'idéal ; en pratique, amendez avec des notes datées.
- **Les mots plutôt que les abréviations.** « Décisions » invite plus de contribution que « ADR ».
- **Rendez les décisions repérables et, où possible, testables.** Faites surgir le bon registre au bon moment ; garantissez-le avec des fonctions d'aptitude.

## Recommandations

### Capturez la structure essentielle

Un bon registre de décision a quelques sections essentielles. Adaptez un modèle connu plutôt que d'en inventer un :

- **Titre :** une phrase impérative courte, au présent (« Utiliser [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) pour le grand livre »).
- **Statut :** proposé, accepté, remplacé, obsolète.
- **Contexte :** la situation, les forces, les priorités commerciales, et les contraintes qui rendent cette décision nécessaire ; incluez l'exigence architecturalement significative qu'elle adresse.
- **Décision :** le choix fait, énoncé simplement.
- **Conséquences :** ce qui devient plus facile et ce qui devient plus difficile, les décisions consécutives déclenchées, et les risques acceptés.

Les modèles populaires incluent celui de Michael Nygard (simple et largement adopté), celui de Tyree et Akerman (plus élaboré, avec des alternatives pondérées), MADR (Markdown Any Decision Records, fort sur les options et leurs avantages/inconvénients), et les Y-statements (une forme structurée en une phrase). Standardisez-en un par organisation, afin que les registres soient comparables. Voir le chapitre 12.3 pour un modèle prêt à copier-coller.

### Écrivez des registres spécifiques, datés, et quasi immuables

Gardez chaque registre à propos d'exactement une décision. Horodatez les affirmations individuelles, surtout tout ce qui dérive : tarification, chiffres de mise à l'échelle, capacités des fournisseurs, termes de licence. En théorie, un registre devrait être immuable. Quand une décision change, vous écrivez un *nouveau* registre qui remplace l'ancien, préservant l'historique. En pratique, beaucoup d'équipes trouvent qu'une approche de **document vivant** fonctionne mieux : insérer de nouvelles informations dans le registre existant avec un horodatage et une note indiquant qu'elles sont arrivées après la décision. Les deux sont légitimes. Le style immuable est plus fort pour les pistes d'audit ; le style vivant est meilleur pour la connaissance quotidienne de l'équipe. Choisissez délibérément, et soyez cohérent.

### Stockez les registres là où se trouve le travail

Placez les registres de décision dans le [contrôle de version](https://en.wikipedia.org/wiki/Version_control) aux côtés du code : un répertoire `decisions/` (ou `adr/`) de fichiers [Markdown](https://en.wikipedia.org/wiki/Markdown), un par décision, nommés avec une phrase verbale impérative en minuscules séparée par des tirets (`choisir-base-de-donnees.md`, `formater-horodatages.md`). Cela vous donne l'historique, la revue, et la comparaison de différences gratuitement, et garde la justification à côté de ce qu'elle explique. Si votre équipe préfère les [wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs, ou un traqueur de style Jira, utilisez-les à la place. L'outil compte bien moins que l'habitude. Un outil léger en ligne de commande (comme `adr-tools`) peut échafauder et indexer les registres.

### Nommez-les « décisions », et élargissez au-delà de l'architecture

Une intuition pratique de beaucoup d'équipes : l'étiquette compte. Certains développeurs et managers se hérissent au mot « architecture », et « registre » peut sembler de la paperasse après coup. Renommer simplement le répertoire « décisions » actionne souvent un déclic. Les équipes commencent à enregistrer les choix de fournisseurs, les décisions de planification, les décisions de calendrier, les décisions de données et de conformité, toutes avec le même modèle. Les gens apprennent plus vite des mots que des abréviations, et ils contribuent davantage quand le cadrage est « aidez vos futurs coéquipiers à réfléchir » plutôt que « remplissez le formulaire obligatoire ».

### Définissez le cycle de vie et la gouvernance

Pour que les registres de décision passent à l'échelle, mettez-vous d'accord sur le processus environnant (c'est là que la gouvernance du chapitre 1.5 rencontre la pratique) :

- **Qui peut en lever un, et ce qui le justifie :** typiquement tout contributeur informé ; levez un registre quand les futurs développeurs auront besoin du *pourquoi*, et sautez-le pour les choix à faible risque, autonomes, ou déjà documentés.
- **Cycle de vie :** un flux simple tel que *Initiation → Recherche → Évaluation → Mise en œuvre → Maintenance → Retrait*, avec des critères d'acceptation pour passer d'une étape à l'autre (problème articulé, alternatives envisagées, compromis documentés, parties prenantes consultées).
- **Rôles :** proposant, chercheur, réviseur, approbateur, et un mainteneur responsable qui révise le registre périodiquement (au moins annuellement) et pilote l'éventuel retrait.
- **Gouvernance :** comment fonctionnent le consensus, le conflit, l'escalade, et le veto, et toute contrainte de conformité. Appuyez-vous sur des principes comme le *biais pour l'action* et le [désaccord-puis-engagement](https://en.wikipedia.org/wiki/Disagree_and_commit), et réservez un processus plus lourd aux décisions irréversibles à fort rayon d'impact (« porte à sens unique »).

### Rendez les décisions testables et repérables

Un registre de décision *documente* une décision ; une **fonction d'aptitude** la *garantit* : un contrôle automatisé, exécuté en [intégration continue](https://en.wikipedia.org/wiki/Continuous_integration) (CI), qui vérifie que la décision tient toujours (« tous les changements d'état doivent émettre des événements », « aucun module ne peut importer à travers ces frontières », en utilisant des outils comme ArchUnit). Cela transforme la gouvernance d'une revue manuelle périodique en une application continue et évolutive, ce qui est particulièrement précieux pour les objectifs réglementaires et d'audit (chapitres 3.1, 4.6, 8.5). Puis faites surgir le *bon* registre au *bon* moment. Un outillage qui attache les décisions pertinentes à une pull request, quand un développeur touche le code qu'elles gouvernent, vaut mieux qu'espérer que les gens lisent un dossier de documentation.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients |
|---|---|---|
| **ADR légers (Nygard/MADR)** | Rapides à écrire, effectivement écrits ; faible cérémonie | Moins de rigueur pour les décisions à fort enjeu et contestées |
| **Modèles lourds (Tyree-Akerman)** | Alternatives pondérées ; forts pour les choix grands et coûteux | Plus lents ; peuvent décourager l'enregistrement de routine |
| **Immuable + remplacement** | Piste d'audit propre ; historique préservé | Plus de registres ; les lecteurs doivent tracer les chaînes |
| **Document vivant (amendements datés)** | Source de vérité actuelle unique ; facile à maintenir | Récit d'audit plus faible ; risque de modifications silencieuses |
| **Markdown dans le dépôt** | Versionné, révisable, à côté du code | Moins accessible aux non-développeurs |
| **Wiki / outil de documentation** | Accessible à tous les rôles | Historique et revue plus faibles ; dérive du code |

La tension centrale est **rigueur contre adoption**. Le système le plus rigoureux que personne n'utilise n'enregistre rien. Le système le plus léger que tout le monde utilise s'accumule en valeur. Optez par défaut pour le léger, et réservez un processus plus lourd aux quelques décisions coûteuses et difficiles à inverser.

## Questions à discuter avec votre équipe

1. **Comment le bon registre de décision atteindra-t-il un développeur au moment où il touche le code qu'il gouverne, plutôt que de rester dans un dossier que personne n'ouvre ?** Un journal en écriture seule enregistre un raisonnement qui ne change jamais le comportement, ce qui est la façon la plus courante dont les registres de décision échouent : ils existent, et personne ne les lit quand cela compte. La considération concurrente est l'effort, parce que faire surgir les registres automatiquement (les attacher à une pull request quand quelqu'un modifie le code gouverné) exige un investissement d'outillage qu'un wiki ou un dossier de documentation ne demande pas. Apportez des preuves à la discussion : quand quelqu'un a récemment inversé ou replaidé une question réglée, le registre pertinent était-il repérable à ce moment-là, ou enterré ? Pour une grande organisation faisant fonctionner des dizaines d'équipes, la repérabilité est ce qui transforme le raisonnement durement acquis d'une équipe en un atout réutilisable au lieu d'une archive privée. Décidez s'il faut stocker les registres dans le contrôle de version à côté du code et les câbler dans le flux de pull request, afin que le registre apparaisse là où le travail se passe.

2. **Qui est le mainteneur responsable de chaque registre, et qu'est-ce qui empêche votre journal de se dégrader en désinformation confiante ?** Le mode d'échec dangereux d'un journal de décisions n'est pas un dossier vide, c'est un dossier plein de registres dont les coûts, les capacités de fournisseurs, et les contraintes sont silencieusement devenus obsolètes il y a des années. Chaque registre a besoin d'un propriétaire responsable qui le révise sur une cadence (au moins annuellement) et pilote son remplacement ou son retrait, sinon le journal pourrit en folklore que les gens citent sélectivement et auquel ils font peu confiance. Apportez des preuves : combien de vos registres sont non datés, combien décrivent un fournisseur ou un prix qui a depuis changé, et quand chacun a été révisé pour la dernière fois. Dans les contextes gouvernementaux et réglementés, cela devient plus aigu, parce qu'une chaîne immuable et remplacée est exactement ce sur quoi les auditeurs et les entrepreneurs successeurs s'appuient pour une justification traçable. Décidez explicitement votre cycle de vie, horodatez les affirmations individuelles qui dérivent, et assignez des mainteneurs, afin que le journal reste un atout vivant plutôt qu'un cimetière.

3. **Devriez-vous standardiser sur un modèle à travers toutes les équipes, et combien de rigueur vos décisions à plus fort enjeu ont-elles réellement besoin ?** La comparabilité est un bénéfice réel : quand chaque équipe utilise la même forme (Nygard, MADR, ou similaire), une nouvelle équipe peut trouver trois registres antérieurs et adopter le raisonnement en un après-midi au lieu d'un mois de débat. La tension centrale est rigueur contre adoption, parce que le modèle le plus lourd que personne n'utilise n'enregistre rien, tandis que le plus léger que tout le monde utilise s'accumule en valeur. Apportez des preuves : les registres sont-ils réellement écrits, et séparément, de grandes décisions coûteuses et contestées ont-elles été sous-analysées parce que la forme légère a sauté la pesée des alternatives ? Pour les entreprises coordonnant des choix qui se chevauchent entre équipes, un modèle partagé plus un index consultable empêchent des décisions divergentes et incompatibles. Optez par défaut pour le léger dans le cas commun, et convenez à l'avance quelles décisions à porte à sens unique justifient une forme plus lourde avec des alternatives pondérées.

4. **Qu'est-ce qui justifie réellement de lever un registre de décision, et qui a l'autorité de dire qu'un choix n'en a pas besoin ?** Fixez la barre trop haut et le raisonnement derrière des choix conséquents s'évapore ; fixez-la trop bas et le journal se remplit de trivialités qui enterrent les registres dont les gens ont réellement besoin. Pour une grande organisation, un seuil flou signifie que chaque équipe improvise le sien, donc la couverture devient inégale et personne ne peut faire confiance qu'un registre manquant signale une décision peu importante. Apportez des preuves à la discussion : une poignée de décisions récentes qui ont été enregistrées mais n'auraient pas dû l'être, et des décisions douloureuses qui n'ont pas été enregistrées et vous ont coûté plus tard une redécouverte. Convenez d'un test simple, comme enregistrer chaque fois qu'un futur développeur aura besoin du *pourquoi* et sauter les choix à faible risque, autonomes, ou déjà documentés. Dans les contextes réglementés et gouvernementaux, le calcul change, parce qu'un mandat d'audit peut exiger un registre pour chaque exigence architecturalement significative, que l'équipe le juge digne d'être écrit ou non, donc nommez à l'avance quelles décisions sont non négociables.

5. **Vos registres sont-ils un raisonnement authentique capturé au moment de la décision, ou de la paperasse écrite après coup pour satisfaire un mandat ?** Un registre produit après coup pour clôturer un ticket tend à blanchir l'option choisie et à omettre silencieusement les alternatives réellement pesées, ce qui est précisément l'information dont un futur lecteur a le plus besoin. La pression concurrente est réelle : écrire le *pourquoi* avant ou pendant une décision semble plus lent que livrer, et admettre par écrit les chemins rejetés exige une sécurité psychologique que certaines équipes n'ont pas. Apportez un échantillon de registres récents à la table et demandez honnêtement si le contexte et les alternatives rejetées se lisent comme une véritable délibération ou comme une justification rétroadaptée. Pour une grande équipe, des registres creux sont pires que pas de registres du tout, parce qu'ils apprennent aux gens que le journal n'est pas fiable. Dans l'audit d'entreprise et gouvernemental, cette distinction est nette : les organismes de surveillance et les entrepreneurs successeurs dépendent d'une justification qui reflète ce qui a vraiment été envisagé, et un registre qui se lit comme du théâtre sape la garantie que le journal existe pour fournir.

6. **Lesquelles de vos décisions à plus fort enjeu pouvez-vous garantir avec une fonction d'aptitude automatisée, plutôt que de faire confiance à une revue manuelle périodique pour attraper une violation ?** Un registre de décision documente un choix, mais seul un contrôle automatisé exécuté en intégration continue empêche ce choix de s'éroder silencieusement à mesure que des dizaines de développeurs touchent le code au fil des ans. Le compromis est l'investissement, parce qu'écrire et maintenir des fonctions d'aptitude (avec des outils comme ArchUnit) coûte du temps d'ingénierie, et beaucoup de décisions, surtout les choix de processus ou de fournisseurs, ne sont pas mécaniquement testables du tout. Apportez des preuves : quelles décisions de frontière (dépendances de module, émission d'événements, règles d'accès aux données) ont été silencieusement violées et attrapées seulement tard en revue ou en production. Pour une entreprise faisant fonctionner de nombreuses équipes, les fonctions d'aptitude transforment la gouvernance d'un goulot d'étranglement central en une application continue qui passe à l'échelle sans ralentir tout le monde. Dans les contextes réglementés et gouvernementaux, un contrôle automatisé et toujours actif est une preuve d'audit bien plus forte qu'une signature sur une revue, parce qu'il prouve que la décision tient encore aujourd'hui plutôt que quelqu'un l'a approuvée un jour.

## Regard sectoriel

**Jeune pousse.** Gardez-le à l'habitude et rien de plus : un dossier `decisions/` dans votre dépôt principal, et une note à deux sections (contexte et choix) chaque fois que vous prenez une décision que votre futur vous remettra en question. Sautez entièrement le cycle de vie, les rôles, et les approbateurs, parce qu'un processus que vous ne pouvez pas soutenir est un processus que vous abandonnerez. Le seul registre qui épargne à votre première embauche de demander pourquoi le système est construit ainsi a déjà remboursé toute la pratique.

**Petite entreprise.** Sans architecte dédié et avec peu de temps, placez les registres là où votre équipe travaille déjà, que ce soit un wiki, un document partagé, ou le dépôt, plutôt que d'acheter un outil dédié. L'habitude compte bien plus que l'outillage, alors abaissez la barrière : nommez le répertoire `decisions` plutôt que `adr`, et capturez les choix de fournisseurs et de construire-ou-acheter dans le même souffle que les choix techniques. Quand vous vous appuyez sur des prestataires externes, un court registre daté de pourquoi vous avez choisi un fournisseur ou une plateforme est une assurance peu coûteuse contre le fait d'être enfermé dans un choix que personne ne pourra plus tard expliquer.

**Grande entreprise.** Le travail est la coordination entre de nombreuses équipes : standardisez sur un modèle, publiez un index consultable inter-équipes, et appuyez les décisions de frontière clés avec des fonctions d'aptitude afin que les violations fassent échouer la construction plutôt que d'attendre la revue. Assignez un mainteneur responsable à chaque registre avec une cadence de revue, afin que le journal reste un atout vivant plutôt que de se dégrader en folklore. Bien fait, le raisonnement d'une équipe sur un choix difficile devient un atout que l'équipe suivante adopte en un après-midi au lieu de le replaider.

**Gouvernement.** Les règles de marchés publics, la transparence, et la responsabilité publique rendent les registres de décision proches de l'obligation. Exigez un registre immuable et remplacé pour chaque exigence architecturalement significative, chacun reliant le choix au mandat ou au contrôle de conformité qu'il satisfait, afin que les organismes de surveillance trouvent une justification traçable plutôt qu'une reconstruction. Parce que les systèmes publics couvrent des durées de vie pluriannuelles et multi-fournisseurs, un journal bien tenu est souvent ce qui permet à un entrepreneur successeur de comprendre pourquoi le système est façonné ainsi et de poursuivre le travail sans replaider un terrain réglé.

## Exemples

**Jeune pousse.** Une start-up de cinq personnes ajoute un simple dossier `decisions/` à son dépôt principal, avec une note à deux sections (contexte et choix) chaque fois que quelqu'un prend une décision que leurs futurs eux-mêmes remettront en question. Il n'y a ni cycle de vie, ni rôles, ni approbateurs : juste l'habitude d'écrire le *pourquoi* à côté du code. Quand leur première embauche arrive six mois plus tard, elle lit tout le dossier en une heure et arrête de demander « pourquoi est-ce construit ainsi ? ». Le journal léger coûte des minutes par entrée et leur épargne la taxe de redécouverte qui mord bien avant qu'une équipe ne grandisse.

**Grande entreprise.** Un détaillant avec 30 équipes d'ingénierie standardise sur des registres au format MADR dans chaque dépôt, plus un index central consultable. Quand une nouvelle équipe fait face à « [monorepo](https://en.wikipedia.org/wiki/Monorepo) contre multi-dépôts », elle trouve trois registres antérieurs avec contexte et conséquences, et adopte le raisonnement en un après-midi au lieu d'un mois de débat. Les décisions de frontière clés (appropriation de service, règles d'accès aux données) sont appuyées par des fonctions d'aptitude ArchUnit, afin que les violations fassent échouer la construction plutôt que d'être attrapées en revue. C'est une gouvernance qui passe à l'échelle sans goulot d'étranglement central.

**Gouvernement.** Une agence modernisant un système de prestations exige un ADR pour chaque exigence architecturalement significative, chacun reliant la décision au mandat ou au contrôle de conformité qu'il satisfait (accessibilité, résidence des données, auditabilité). Les registres sont immuables et remplacés, produisant un journal traçable qui satisfait la revue de surveillance. Surtout, cela permet aussi à un entrepreneur successeur de comprendre *pourquoi* le système est façonné ainsi, préservant la continuité à travers les durées de vie pluriannuelles et multi-fournisseurs typiques des programmes publics (chapitres 4.6, 10.4).

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Un registre de décision coûte des minutes à écrire et quelques minutes de plus à réviser. Le retour est un coût de *re-décision* évité et un coût de *mauvaise inversion* évité, tous deux importants et récurrents sur les systèmes à longue durée de vie. Chaque fois qu'une équipe replaide une question réglée, ou inverse un choix judicieux parce que personne ne se souvenait de la contrainte derrière lui, elle paie en temps d'ingénieur senior et souvent en incident. Un journal de décisions convertit cette taxe récurrente en une écriture unique.

Sur le **coût total de possession**, les registres de décision sont parmi la documentation à plus fort effet de levier que vous puissiez garder, parce qu'ils ciblent l'atout le plus sensible au renouvellement de personnel : la justification. L'intégration est plus rapide (les nouvelles recrues lisent le *pourquoi*, pas seulement le code). La modernisation est plus sûre (chapitre 3.6 : vous pouvez distinguer les décisions essentielles des décisions accidentelles). Les audits sont moins chers (la preuve existe déjà). Le coût de *ne pas* les garder est invisible sur tout tableau de bord, et il s'accumule silencieusement à chaque départ. Pour convaincre la direction, pointez vers une redécouverte coûteuse récente, ou une décision inversée qui a causé un incident, et notez que la correction coûte presque rien à instituer.

## Anti-patterns et pièges

- **Enregistrer le *quoi* sans le *pourquoi* :** omettre le contexte et les alternatives rejetées, tout le but.
- **Paperasse après coup :** registres écrits pour satisfaire un mandat, pas pour réfléchir ; ils se lisent comme creux et personne ne leur fait confiance.
- **Méga-documents multi-décisions :** une page géante que personne ne peut naviguer ni remplacer proprement.
- **Affirmations non datées :** coûts et contraintes qui étaient vrais un jour, présentés comme intemporels.
- **Modifications silencieuses :** changer l'historique d'une décision sans note datée, détruisant la piste d'audit.
- **Journaux en écriture seule :** registres créés et jamais mis en avant au moment où ils sont pertinents, donc ils n'influencent pas le comportement.
- **Contrôle d'accès par abréviation :** insister sur « ADR » et « architecture » et décourager ainsi la contribution.
- **Aucun cycle de vie :** registres jamais révisés, remplacés, ou retirés, se dégradant en désinformation.

## Modèle de maturité

- **Niveau 1 (Initiation) :** Les décisions vivent dans les têtes des gens, les fils de discussion, et les messages de commit ; la capture est réactive et ad hoc, et la justification se perd couramment avec le renouvellement du personnel.
- **Niveau 2 (Développement) :** Certaines équipes tiennent des registres, dans des formats et modèles variés, chaque fois qu'un individu s'en souvient ; la pratique est incohérente entre les équipes, sans journal, nommage, ou processus partagé.
- **Niveau 3 (Standardisation) :** Un modèle unique, un stockage dans le dépôt, et un cycle de vie et une gouvernance définis (critères de levée/saut, rôles, cadence de revue) sont documentés et appliqués de manière cohérente dans toute l'organisation ; les registres sont révisés et remplacés plutôt que modifiés silencieusement.
- **Niveau 4 (Gestion) :** Le journal de décisions est mesuré par rapport à des références : couverture (la part des décisions architecturalement significatives qui portent un registre), fraîcheur (la part des registres révisés dans leur cadence, plus le compte des affirmations non datées ou obsolètes), et repérabilité (à quelle fréquence un registre pertinent a réellement atteint le développeur qui a changé le code gouverné). Les mainteneurs responsables agissent sur ces métriques, remplaçant les registres obsolètes et comblant les lacunes de couverture sur preuve plutôt que sur anecdote.
- **Niveau 5 (Orchestration) :** Un journal de décisions consultable inter-équipes est intégré au travail quotidien : les registres pertinents surgissent automatiquement sur les changements qu'ils gouvernent, les décisions clés sont garanties par des fonctions d'aptitude en intégration continue, et le journal alimente l'intégration, la modernisation, et l'audit comme un atout vivant. L'organisation améliore continuellement la pratique elle-même, retirant, remplaçant, et recadrant les registres à mesure que le système et ses contraintes évoluent, et rééquilibrant où elle investit de la rigueur à mesure que le portefeuille de décisions grandit.

## Pistes de réflexion

1. Quelle a été la dernière décision que votre équipe a inversée ou replaidée parce que personne ne se souvenait du raisonnement d'origine ?
2. Renommer votre répertoire `adr/` en `decisions/` changerait-il qui contribue et ce qui est enregistré ?
3. Lesquelles de vos décisions critiques pourraient être garanties par une fonction d'aptitude automatisée dès aujourd'hui ?
4. Immuable-et-remplacé ou document vivant : lequel convient à vos obligations d'audit et à votre culture, et pourquoi ?
5. Comment une nouvelle recrue (ou un entrepreneur successeur) découvrirait-elle actuellement *pourquoi* votre système est façonné ainsi ?
6. Qu'est-ce qui justifie de lever un registre de décision dans votre équipe, et qu'est-ce qui justifie de *ne pas* en lever un ?

## Points clés à retenir

- Un registre de décision capture une décision importante avec son **contexte et ses conséquences** : le *pourquoi*, pas seulement le *quoi*.
- Gardez les registres **spécifiques, horodatés, et légers** ; standardisez sur un modèle (Nygard, MADR, ou similaire).
- Stockez-les **dans le contrôle de version à côté du code** ; envisagez de les nommer « décisions » pour élargir la contribution.
- Définissez un **cycle de vie et une gouvernance** (critères de levée/saut, rôles, cadence de revue) ; réservez le processus lourd aux décisions à porte à sens unique.
- Rendez les décisions **repérables** au moment du changement et, où possible, **testables** via des fonctions d'aptitude.
- Le retour sur investissement est la redécouverte et le coût de mauvaise inversion évités ; l'argument du coût total de possession est le plus fort là où le renouvellement de personnel, la modernisation, et l'audit comptent le plus. Voir le chapitre 1.5 (prise de décision et gouvernance) et le chapitre 3.1 (fondamentaux de l'architecture).

## Références et lectures complémentaires

- Michael Nygard, « Documenting Architecture Decisions » (2011) : l'ADR léger fondateur.
- MADR : le projet Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree et Art Akerman, « Architecture Decisions: Demystifying Architecture » (*IEEE Software*, 2005).
- Olaf Zimmermann, « Y-Statements » et « Architectural Decision Making » (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)* : modèles, exemples, et guide de travail d'équipe (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar : « Lightweight Architecture Decision Records ».
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fonctions d'aptitude).
- AWS Prescriptive Guidance, « ADR process » ; Red Hat, « Why you should use ADRs ».
- Wikipédia, « Architectural decision » et « Architecturally significant requirements ».
