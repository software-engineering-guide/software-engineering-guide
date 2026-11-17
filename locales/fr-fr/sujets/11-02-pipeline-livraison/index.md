# 11.2 Le pipeline de livraison

## Vue d'ensemble et motivation

Le pipeline de livraison est le flux de travail qui transforme une idée validée en logiciel fonctionnel entre les mains des utilisateurs (de façon fiable, reproductible, et mesurable) puis réinjecte les données de résultat résultantes dans la découverte (chapitre 11.1). C'est le chemin industrialisé depuis un commit de code jusqu'à un changement de production jusqu'à un effet mesuré sur les utilisateurs et l'affaire. Là où la découverte répond *quoi et pourquoi*, la livraison répond *comment nous le livrons en sécurité, à quelle vitesse, et si cela a réellement fonctionné*.

Ce chapitre est délibérément intégratif. La mécanique vit en détail ailleurs : stratégie de test (chapitre 2.4), automatisation de test et de processus (chapitre 8.5), **[intégration continue](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue)** et **[livraison continue](https://fr.wikipedia.org/wiki/Livraison_continue)** (CI/CD) et stratégies de déploiement (chapitre 8.1), infrastructure comme code (chapitre 8.2), fiabilité et SLO (objectifs de niveau de service, chapitre 9.1), et expérimentation (chapitre 7.4). Ici nous les assemblons en un seul pipeline de bout en bout et, crucialement, attachons les **métriques de résultat** qui vous disent si toute la machine produit de la valeur plutôt que simplement produire des publications.

Pour les grandes équipes, le pipeline de livraison est l'investissement unique à plus fort levier dans l'efficacité d'ingénierie. Une décennie de recherche, la plus proéminente étant le programme DORA (**[DevOps Research and Assessment](https://fr.wikipedia.org/wiki/DevOps#DORA)**) résumé dans *Accelerate*, montre que les équipes avec des pipelines de livraison rapides, automatisés, et à faible risque surperforment sur le débit *et* la stabilité *et* les résultats organisationnels. La vieille croyance selon laquelle la vitesse et la sécurité se compensent l'une l'autre est empiriquement fausse. Dans les entreprises, un pipeline solide est ce qui permet à des centaines d'ingénieurs d'intégrer sans s'effondrer en chaos de fusion et théâtre de publication manuel. Dans le gouvernement, il remplace les publications trimestrielles, à haut cérémonial, tout-ou-rien « big bang » (historiquement une cause majeure de programmes échoués) par des changements petits, réversibles, et auditables qui satisfont les obligations de contrôle de changement *à travers* l'automatisation plutôt que malgré elle.

## Principes clés

- **Automatisez tout ce qui est reproductible.** Les étapes manuelles sont lentes, sujettes aux erreurs, et non auditables.
- **Petits lots, publications fréquentes.** Les petits changements sont plus faciles à réviser, tester, livrer, et inverser.
- **Intégrez la qualité.** Les tests et portes rapides et automatisés attrapent les défauts avant la production, pas après.
- **Séparez le déploiement de la publication.** Livrez le code dans l'obscurité ; activez les fonctionnalités avec des indicateurs quand prêt.
- **Rendez tout réversible.** Le retour en arrière rapide et l'exposition progressive transforment le déploiement d'un pari en une expérience.
- **Le pipeline est la source de vérité.** Si ce n'est pas dans le contrôle de version et le pipeline, cela n'est pas arrivé.
- **Mesurez les résultats, pas seulement les sorties.** Le compte de déploiement est une sortie ; une métrique bougée est un résultat.

## Recommandations

### Automatiser la suite de tests et conditionner dessus

L'automatisation de test est la fondation qui rend la livraison rapide sûre. Implémentez un portefeuille de tests équilibré et surtout automatisé (chapitre 2.4) : de nombreux tests unitaires rapides, moins de tests d'intégration et de contrat, un petit nombre de tests de bout en bout, plus des vérifications de sécurité automatisées (SAST/DAST/SCA : analyse statique, dynamique, et de composition logicielle), d'accessibilité, et de performance. Exécutez-les comme **portes de qualité** dans le pipeline pour qu'aucun changement n'atteigne la production sans les passer. Gardez la suite rapide et digne de confiance : une suite lente ou instable est contournée, ce qui défait son but (chapitre 8.5). Visez à ce que le pipeline donne à un développeur un signal réussite/échec clair en minutes d'un commit.

### Pratiquer l'intégration continue et la livraison continue

**L'intégration continue (CI) :** chaque développeur fusionne de petits changements dans la ligne principale fréquemment (idéalement quotidiennement), chaque fusion déclenchant une construction et exécution de test automatisées. Ceci est mieux soutenu par le développement basé sur le tronc (chapitre 2.6), qui garde les branches de courte durée et l'intégration continue. **La livraison continue (CD) :** chaque changement qui passe le pipeline est *toujours dans un état publiable* et peut être déployé à la demande. **Le déploiement continu** va une étape plus loin : chaque changement réussi se déploie en production automatiquement. Choisissez le niveau d'automatisation approprié à votre profil de risque ; les environnements régulés peuvent s'arrêter à la livraison continue avec une étape de promotion contrôlée (chapitre 8.1), mais devraient quand même automatiser tout jusqu'à cette porte.

### Déployer en sécurité avec des stratégies progressives

Découplez le **déploiement** (code fonctionnant en production) de la **publication** (utilisateurs vivant le changement), et exposez les changements graduellement :

- Les **[drapeaux de fonctionnalité](https://fr.wikipedia.org/wiki/Feature_toggle)** vous laissent déployer le code dans l'obscurité et publier vers des segments à la demande, et revenir en arrière instantanément en basculant.
- Les **publications canari** acheminent un petit pourcentage de trafic vers la nouvelle version, surveillant les métriques de santé avant d'élargir.
- Les **déploiements bleu-vert** gardent deux environnements et basculent le trafic atomiquement, avec un retour en arrière instantané.
- Les **déploiements progressifs (rolling)** remplacent les instances incrémentalement.
- La **livraison progressive** combine drapeaux, canaris, et analyse automatisée pour promouvoir ou revenir en arrière selon des signaux en direct.

Associez chaque stratégie à un retour en arrière automatisé déclenché par des violations de SLO ou une combustion de budget d'erreur (le taux auquel les échecs consomment le budget d'indisponibilité permis ; chapitre 9.1). Voir le chapitre 8.1 pour la mécanique.

### Instrumenter les métriques de résultat : mesurer le pipeline et l'impact

Un pipeline de livraison qui livre rapidement mais livre la mauvaise chose est du gaspillage rapide. Mesurez à trois niveaux :

1. **Flux de livraison, les quatre métriques DORA :**
   - *Fréquence de déploiement :* à quelle fréquence vous publiez en production.
   - *[Délai de livraison](https://fr.wikipedia.org/wiki/D%C3%A9lai_de_livraison) pour les changements :* du commit à la production.
   - *Taux d'échec de changement :* pourcentage de publications qui causent une dégradation.
   - *Temps de récupération de déploiement échoué :* à quelle vitesse vous restaurez le service (anciennement MTTR, temps moyen de récupération).
   Les performeurs d'élite déploient à la demande, avec des délais de livraison sous une heure, des taux d'échec bas, et une récupération en minutes. Ajoutez des **métriques de flux** de la pensée de flux de valeur (temps de cycle, **[travail en cours](https://fr.wikipedia.org/wiki/En-cours)**, efficacité de flux) pour voir où le travail attend.

2. **Fiabilité et qualité, les SLI et SLO** (indicateurs et objectifs de niveau de service ; chapitre 9.1) : le service respecte-t-il ses cibles de fiabilité et engagements d'attribut de qualité (chapitre 11.1) après chaque changement ?

3. **Résultats d'affaires et utilisateur** (chapitres 7.3 à 7.4) : le changement a-t-il bougé les résultats clés et KPI que la découverte a définis ? C'est là que la publication rencontre l'expérience : livrez derrière un drapeau, mesurez contre un contrôle, et ne gardez que ce qui gagne.

### Fermer la boucle en retour vers la découverte

L'acte final du pipeline de livraison n'est pas le déploiement ; c'est la **preuve**. Les métriques de résultat (l'activation a-t-elle monté, le temps de paiement a-t-il chuté, les tickets de support ont-ils baissé) rentrent dans le pipeline de découverte (chapitre 11.1) comme base pour le prochain tour de paris. Quand la découverte et la livraison sont jointes par cette boucle de rétroaction, l'organisation devient un système d'apprentissage : les hypothèses sont livrées, mesurées, et soit mises à l'échelle soit inversées, continuellement.

### Rendre la livraison auditable et gouvernée

Dans les contextes d'entreprise et gouvernementaux, traitez le pipeline lui-même comme un contrôle de conformité. Parce que chaque changement s'écoule à travers le contrôle de version et un pipeline automatisé, vous obtenez une piste d'audit immuable « gratuitement » : qui a changé quoi, quels tests et approbations l'ont conditionné, et quand il s'est déployé. Encodez la séparation des devoirs, les révisions requises, et les vérifications de politique comme **politique-comme-code** (règles de gouvernance exprimées sous une forme applicable par machine et contrôlée en version ; chapitre 8.2) pour que le contrôle de changement soit appliqué automatiquement et prouvé continuellement (chapitres 4.6 et 10.2), plutôt que reconstruit manuellement avant un audit.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| **Déploiement continu (auto vers prod)** | Rétroaction la plus rapide ; lots les plus petits ; moins de labeur manuel | Exige des tests, surveillance, retour en arrière matures ; difficile dans les portes régulées |
| **Livraison continue avec promotion manuelle** | Point de contrôle humain/conformité ; convivial pour l'audit | Plus lent ; risque de mise en lot de changements à la porte |
| **Drapeaux de fonctionnalité** | Séparation déploiement/publication ; retour en arrière instantané ; ciblage | Dette de drapeau et complexité combinatoire si non élaguée |
| **Canari / livraison progressive** | Limite le rayon d'explosion ; promotion pilotée par données | A besoin d'une observabilité forte et gestion de trafic |
| **Bleu-vert** | Bascule et retour en arrière instantanés | Double le coût d'environnement ; les migrations avec état/données sont délicates |
| **Processus de publication manuel lourd** | Se sent contrôlé ; familier aux auditeurs | Lent, sujet aux erreurs, non reproductible, mal audité en pratique |

La croyance historique de compromis, *allez plus vite et vous casserez plus*, est celle qu'il faut retirer. Les preuves montrent que les pratiques qui augmentent la vitesse (automatisation, petits lots, tests rapides, réversibilité) sont les *mêmes* pratiques qui augmentent la stabilité. Les vrais compromis concernent l'**investissement et la granularité de contrôle**, pas la vitesse-contre-sécurité.

## Questions à discuter avec votre équipe

1. **Quel est votre vrai profil de risque, et justifie-t-il de s'arrêter à la livraison continue plutôt que d'aller au déploiement continu ?** Choisir le niveau d'automatisation est une vraie décision, pas un défaut. Le déploiement continu donne la rétroaction la plus rapide et les lots les plus petits, pourtant il exige des tests matures, une observabilité forte, et un retour en arrière instantané, donc un contexte régulé peut rationnellement s'arrêter à une porte de promotion contrôlée. Apportez des preuves : votre taux d'échec de changement, votre temps de récupération, et la fiabilité de votre suite de tests, parce que ceux-ci vous disent si l'auto-vers-prod est sûr aujourd'hui. Pour l'entreprise et le gouvernement, automatisez tout jusqu'à la porte et faites de la porte elle-même une politique-comme-code, pour que l'étape humaine ajoute du contrôle sans ajouter de labeur manuel. Si vous ne pouvez pas encore faire confiance au pipeline pour attraper un mauvais changement, investissez dans les portes et l'observabilité avant de basculer l'interrupteur.

2. **Votre pipeline peut-il produire la preuve d'audit qu'un régulateur demanderait, sans que quiconque ne la reconstruise à la main ?** Traitez le pipeline lui-même comme un contrôle de conformité. Chaque changement devrait porter une piste immuable de qui a changé quoi, quels tests et approbations l'ont conditionné, et quand il s'est déployé, généré automatiquement. Dans l'entreprise et le gouvernement, encodez la séparation des devoirs et les révisions requises comme politique-comme-code pour que le contrôle de changement soit appliqué et prouvé continuellement plutôt qu'assemblé en panique avant un audit. Le signal à apporter : choisissez un changement de production récent et essayez de produire sa piste complète d'approbation-et-test en cinq minutes. Si vous ne pouvez pas, vous payez pour la préparation d'audit manuelle et portez un risque que l'automatisation retirerait.

3. **Quand une publication commence à se dégrader en production, qu'est-ce qui déclenche un retour en arrière, et est-ce automatique ?** La réversibilité est ce qui rend la vitesse rationnelle plutôt qu'imprudente, donc le déclencheur de retour en arrière mérite une conception explicite. Décidez si une violation de SLO ou une combustion de budget d'erreur revient en arrière automatiquement, ou si un humain doit remarquer, décider, et agir pendant que les utilisateurs souffrent. Apportez vos derniers incidents et mesurez l'écart entre « la métrique a commencé à se dégrader » et « le changement a été inversé » ; cet écart est votre vrai rayon d'explosion. Pour les grandes équipes livrant de nombreuses fois par jour, le retour en arrière manuel ne passe pas à l'échelle, et les drapeaux plus l'analyse canari vous laissent promouvoir ou inverser sur des signaux en direct. Si votre réponse est « quelqu'un est appelé et le comprend », vous traitez chaque déploiement comme un pari irréversible.

4. **Quand vous livrez une fonctionnalité, mesurez-vous si elle a réellement bougé la métrique qu'elle était censée bouger, ou comptez-vous le déploiement et passez à autre chose ?** Un pipeline qui livre rapidement mais ne vérifie jamais l'impact est du gaspillage rapide, et l'écart entre la sortie et le résultat est où la plupart de l'investissement de livraison fuit silencieusement. Pour une grande organisation, des centaines de publications par semaine rendent tentant de traiter la fréquence de déploiement comme le tableau de bord, pourtant la fréquence mesure le mouvement, pas la valeur ; la traction concurrente est que la mesure de résultat coûte de l'instrumentation, un groupe de contrôle, et la discipline de laisser une fonctionnalité perdante désactivée. Apportez la dernière poignée de fonctionnalités livrées et, pour chacune, la métrique cible que la découverte a définie, la mesure avant-après, et ce que vous avez fait quand elle n'a pas bougé. Dans les portefeuilles d'entreprise et gouvernementaux, nommez qui révise les résultats selon une cadence fixe et qui a l'autorité de retirer une fonctionnalité qui a été livrée mais n'a jamais payé, parce qu'un changement dont personne n'est responsable de mesurer est un que personne n'éteindra jamais. Le vrai test est de savoir si vous pouvez pointer une fonctionnalité que vous avez inversée *parce que* la preuve disait qu'elle perdait.

5. **Combien de temps votre pipeline prend-il pour donner à un développeur un signal réussite/échec, et fait-il assez confiance aux tests pour ne pas les contourner ?** La vitesse de rétroaction et la confiance dans la suite sont ce qui fait que les portes de qualité conditionnent réellement plutôt que d'être contournées, et les deux s'érodent silencieusement à mesure qu'une base de code grandit. Pour une grande équipe, une suite qui prend quarante minutes ou est instable une exécution sur dix forme des centaines d'ingénieurs à fusionner sur rouge, désactiver les vérifications, ou réexécuter jusqu'au vert, ce qui retire silencieusement la sécurité qui justifiait d'aller vite en premier lieu ; les considérations concurrentes sont la couverture et le réalisme de test contre la vitesse et la stabilité de rétroaction, et pousser trop fort l'un ou l'autre mine l'autre. Apportez la durée de pipeline actuelle, le taux de réexécution instable, et toute preuve de portes sautées ou marquées non bloquantes. Pour les contextes d'entreprise et gouvernementaux où ces portes portent aussi SAST, DAST, et des vérifications de politique qui satisfont la conformité, une porte contournée est à la fois un risque de qualité et un trou d'audit, donc mesurez si la porte est véritablement obligatoire ou simplement consultative. Si les développeurs ne peuvent pas articuler pourquoi ils font confiance à une construction verte, la porte est décorative.

6. **Qui possède garder le chemin de livraison cohérent à travers les équipes et élaguer la dette de drapeau de fonctionnalité, ou chaque équipe réinvente-t-elle son propre pipeline ?** À mesure qu'une organisation grandit, la livraison converge soit sur un chemin pavé partagé soit se fragmente en dizaines de pipelines sur mesure avec des portes incompatibles, des pistes d'audit inégales, et des drapeaux qui survivent à leur but. La tension est réelle : un chemin pavé central vous donne cohérence, gouvernance, et économies d'échelle, mais un mandat qui ignore les vraies contraintes d'une équipe engendre des pipelines fantômes et du ressentiment, donc le chemin pavé doit être assez bon pour que les équipes y adhèrent volontairement. Apportez un inventaire de combien de pipelines distincts existent aujourd'hui, comment la création et suppression de drapeau sont gouvernées, et à quel point le délai de livraison et la qualité d'audit varient entre vos meilleures et pires équipes. Dans les contextes d'entreprise et gouvernementaux, ajoutez l'angle de conformité : des pipelines incohérents signifient que la séparation des devoirs et la preuve de contrôle de changement sont prouvées différemment (ou pas du tout) dans chaque équipe, et un seul chemin pavé audité avec politique-comme-code transforme cela d'un pari par équipe en une garantie organisationnelle. Si personne ne possède le retrait des drapeaux périmés, la dette combinatoire finira par rendre le système intestable.

## Regard sectoriel

**Jeune pousse.** La vitesse est la survie, donc achetez votre pipeline plutôt que de le construire : câblez le développement basé sur le tronc à un exécuteur CI hébergé, conditionnez chaque fusion sur des tests unitaires rapides et un scan de sécurité, et déployez directement en production derrière un service de drapeau de fonctionnalité hébergé. Sautez l'équipe de plateforme et l'outillage sur mesure ; votre ressource la plus rare est l'attention d'ingénierie, et un pipeline qu'un seul généraliste peut maintenir bat un élaboré que personne n'a le temps de corriger. Suivez les quatre métriques DORA sur un tableau de bord simple dès le premier jour pour apprendre votre flux tôt et pouvoir montrer aux investisseurs que vous livrez quotidiennement sans casser les choses.

**Petite entreprise.** Sans ingénieur de publication dédié et avec un budget serré, traitez la livraison comme quelque chose que vous assemblez depuis des services gérés plutôt qu'un système que vous dotez en personnel : CI/CD géré, un outil de drapeau hébergé, et une plateforme cloud qui gère le déploiement et le retour en arrière pour vous. Résistez à construire une infrastructure de pipeline personnalisée que vous ne pouvez pas vous permettre de maintenir, et gardez le chemin assez simple pour que quiconque est d'astreinte puisse le comprendre sous pression. Préférez les outils qui rendent la livraison progressive et le retour en arrière en un clic disponibles prêts à l'emploi, parce que ce sont les capacités qui transforment un déploiement effrayant du vendredi en un routinier.

**Grande entreprise.** Le problème central est la cohérence à travers de nombreuses équipes : un pipeline de chemin pavé supporté avec des portes de test, sécurité, et politique-comme-code automatisées auxquelles les équipes adhèrent plutôt que de réinventer. Standardisez l'interface pour que les métriques DORA et SLO soient comparables à travers l'organisation, budgétez explicitement la capacité de plateforme qui maintient le chemin pavé, et gérez les drapeaux de fonctionnalité et régressions de délai de livraison comme des actifs gouvernés plutôt que du folklore par équipe. La gouvernance et l'audit suivent automatiquement quand chaque changement s'écoule à travers le même chemin contrôlé en version et conditionné.

**Gouvernement.** Les règles de marchés publics, la transparence, et la responsabilité publique façonnent le pipeline, donc favorisez la livraison continue qui s'arrête à une porte de promotion automatisée appliquant la séparation des devoirs et les approbations requises comme politique-comme-code. Faites du pipeline lui-même le contrôle de conformité : chaque changement porte une piste d'audit immuable qui satisfait les obligations de contrôle de changement et d'autorisation d'exploiter sans reconstruction manuelle. Remplacez les publications « big bang » à haut cérémonial par des changements petits, réversibles, et découplés pour pouvoir piloter un flux orienté public dans une région, mesurer les taux d'erreur et d'achèvement, et revenir en arrière en minutes si cela se dégrade.

## Exemples

**Jeune pousse.** Une équipe de trois ingénieurs livrant un outil d'analytique B2B commence par déployer à la main les vendredis après-midi, ce qui signifie une publication effrayante une fois par semaine et un week-end d'appréhension. En un après-midi, ils câblent le développement basé sur le tronc avec un pipeline GitHub Actions : tests unitaires rapides, un linteur, et un scan de sécurité conditionnent chaque fusion, et une construction réussie se déploie directement en production derrière des drapeaux LaunchDarkly. La fréquence de déploiement bondit d'hebdomadaire à plusieurs fois par jour, et parce que chaque nouvelle fonctionnalité livre dans l'obscurité et s'active d'abord pour un client amical, un export CSV cassé est attrapé et basculé en minutes au lieu de devenir un incident du lundi. Ils suivent les quatre métriques DORA sur un tableau de bord simple pour pouvoir montrer aux investisseurs que l'équipe livre quotidiennement sans casser les choses.

**Grande entreprise.** Un assureur mondial consolide 40 équipes sur un pipeline de chemin pavé partagé (une chaîne d'outils par défaut supportée et préintégrée à laquelle les équipes adhèrent ; chapitre 8.4) : développement basé sur le tronc, portes de test et de sécurité automatisées, et déploiement canari avec retour en arrière automatisé sur violation de SLO. La fréquence de déploiement monte de mensuelle à plusieurs fois par jour ; le délai de livraison chute de six semaines à moins d'un jour ; le taux d'échec de changement baisse parce que les lots sont petits et les portes automatisées. Crucialement, les fonctionnalités produit livrent maintenant derrière des drapeaux et sont mesurées contre des contrôles, donc l'assureur peut lier chaque publication à son effet sur le taux d'achèvement de devis, connectant le pipeline de livraison directement aux résultats clés côté découverte du chapitre 11.1.

**Gouvernement.** Un organisme public remplace les publications trimestrielles « big bang » (chacune un week-end d'étapes manuelles et une source fréquente de pannes) par un pipeline de livraison continue qui s'arrête à une porte de promotion automatisée appliquant la séparation des devoirs et les approbations requises comme politique-comme-code. Chaque changement porte une piste d'audit immuable satisfaisant les obligations de contrôle de changement et d'ATO (autorisation d'exploiter) de l'agence (chapitre 4.6). Les publications deviennent petites, fréquentes, et réversibles ; le temps de récupération chute de jours à minutes ; et parce que le déploiement est découplé de la publication via des drapeaux, l'agence peut piloter un nouveau flux de prestations avec une région avant le déploiement national, mesurant les taux d'achèvement et d'erreur avant de s'engager.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur l'investissement de pipeline de livraison est parmi les mieux prouvés en logiciel. Un délai de livraison plus rapide et une fréquence de déploiement plus élevée signifient que les idées atteignent les utilisateurs (et commencent à retourner de la valeur, ou à être corrigées) plus tôt. Un taux d'échec de changement plus bas et une récupération plus rapide signifient moins d'indisponibilité, moins de lutte contre les incendies, et moins de dommage réputationnel et réglementaire. La recherche DORA lie ces capacités à une performance commerciale et organisationnelle supérieure, pas seulement au confort d'ingénierie. L'effet composé compte : une équipe qui livre et apprend quotidiennement itère 20 à 30 fois plus souvent qu'une livrant mensuellement, et ce taux d'apprentissage est décisif sur la vie d'un produit.

Sur le **[coût total de possession](https://fr.wikipedia.org/wiki/Co%C3%BBt_total_de_possession)**, l'automatisation déplace le coût du labeur manuel perpétuel vers un investissement de pipeline ponctuel-plus-maintenance. Une publication manuelle consomme des heures d'ingénieur senior à chaque fois, passe mal à l'échelle, et produit une faible preuve d'audit. Un pipeline automatisé amortit ce coût, puis le *réduit* à mesure que le volume grandit, tout en produisant une preuve plus forte continuellement. La réversibilité abaisse le coût de l'échec lui-même : quand tout changement peut être inversé en secondes, le coût attendu d'un mauvais déploiement s'effondre, ce qui est ce qui rend aller vite rationnel plutôt qu'imprudent.

Pour faire valoir le dossier auprès de la direction, mesurez le référentiel actuel avec les quatre métriques DORA et les heures manuelles dépensées par publication, puis quantifiez le labeur retiré et l'indisponibilité évitée. Le coût d'adoption est réel, à savoir l'ingénierie de pipeline, l'investissement de test, et une capacité de plateforme/chemin pavé (chapitre 8.4), mais le coût de *ne pas* investir est payé continuellement en rétroaction lente, risque de jour de publication, épuisement d'ingénieur, et douleur d'audit. L'argument décisif est le lien de découverte : un pipeline de livraison rapide et mesuré est ce qui rend les paris validés du pipeline de découverte réellement testables en production.

## Anti-patterns et pièges

- **Mesurer la sortie, pas le résultat :** célébrer les comptes de déploiement tandis que les métriques cibles restent plates.
- **Les suites de tests lentes ou instables :** des portes que les développeurs apprennent à ignorer ou contourner.
- **Les publications big bang et peu fréquentes :** de grands lots qui sont risqués, difficiles à déboguer, et difficiles à inverser.
- **Déploiement et publication confondus :** aucun drapeau de fonctionnalité, donc chaque déploiement est un pari irréversible orienté utilisateur.
- **Le théâtre de publication manuel :** des listes de contrôle exécutées à la main qui sont lentes, incohérentes, et mal auditées.
- **Le pipeline automatisé, aucune observabilité :** livrer rapidement sans capacité de détecter ou diagnostiquer les régressions.
- **La dette de drapeau de fonctionnalité :** des drapeaux jamais retirés, s'accumulant en complexité combinatoire intestable.
- **Manipuler les métriques DORA :** diviser les déploiements pour gonfler la fréquence au lieu d'améliorer le flux.
- **Aucune boucle de rétroaction :** les résultats jamais mesurés, donc la livraison n'informe jamais le prochain cycle de découverte.

## Modèle de maturité

- **Niveau 1, Initier :** Publications manuelles, peu fréquentes, à haut cérémonial ; les tests sont surtout manuels et exécutés à la main ; le succès est mesuré comme « cela a été livré » ; les retours en arrière sont douloureux et improvisés ; aucune idée partagée de comment la livraison devrait fonctionner.
- **Niveau 2, Développer :** Certaines équipes érigent la CI avec des constructions automatisées et quelques tests ; les publications sont planifiées ; une surveillance de base existe ; les pratiques varient équipe par équipe et les métriques DORA ne sont pas encore suivies, donc la livraison est meilleure par poches mais incohérente à travers l'organisation.
- **Niveau 3, Standardiser :** Un pipeline de chemin pavé documenté est appliqué à l'échelle de l'organisation : livraison continue avec portes de test et de sécurité automatisées, déploiement progressif avec retour en arrière, et séparation des devoirs appliquée comme politique-comme-code. Le pipeline fournit une piste d'audit immuable, et chaque équipe suit le même chemin contrôlé en version plutôt qu'un sur mesure.
- **Niveau 4, Gérer :** Le pipeline est mesuré et contrôlé contre des référentiels. Les quatre métriques DORA (fréquence de déploiement, délai de livraison, taux d'échec de changement, temps de récupération), l'atteinte de SLO, la combustion de budget d'erreur, et les métriques de flux comme le temps de cycle et le travail en cours sont suivis contre des cibles, et les portes et retours en arrière se déclenchent sur des seuils mesurés plutôt que le jugement. La dette de drapeau, les taux de test instable, et les régressions de délai de livraison sont surveillés, et chaque décision de lancement ou d'arrêt est prise sur des preuves.
- **Niveau 5, Orchestrer :** La livraison est continuellement améliorée et intégrée avec la planification de découverte et de risque. Le déploiement continu fonctionne où approprié avec la livraison progressive et le retour en arrière automatisé ; les fonctionnalités livrent comme des expériences mesurées dont les métriques de résultat rebouclent vers le prochain tour de paris ; la performance DORA d'élite est soutenue à travers les équipes via le chemin pavé ; et l'organisation réaccorde adaptativement les portes, seuils, et capacité à mesure que la charge, le risque, et le mélange de produit changent.

## Pistes de réflexion

1. Quelles sont vos quatre métriques DORA actuelles, et où est le plus grand goulot d'étranglement dans votre flux commit-vers-production ?
2. Pouvez-vous séparer le déploiement de la publication aujourd'hui ? Sinon, que changeraient les drapeaux de fonctionnalité à votre risque ?
3. Combien de temps prend votre suite de tests, et les développeurs lui font-ils assez confiance pour ne pas la contourner ?
4. Quand vous avez livré votre dernière fonctionnalité, avez-vous mesuré si elle a bougé la métrique qu'elle était censée bouger ?
5. Dans un contexte régulé, votre processus de contrôle de changement ralentit-il la livraison *ou* est-il appliqué automatiquement à travers le pipeline ?
6. Quels drapeaux de fonctionnalité dans votre base de code auraient dû être retirés il y a des mois ?

## Points clés à retenir

- Le pipeline de livraison transforme les idées validées en logiciel fonctionnel et mesuré, et réinjecte les résultats vers la découverte (chapitre 11.1).
- Automatisez tout le chemin : des **portes de test** rapides, **CI/CD**, et **infrastructure comme code**, avec le pipeline comme source de vérité.
- **Séparez le déploiement de la publication** et utilisez des stratégies progressives (drapeaux, canari, bleu-vert) avec un retour en arrière automatisé.
- Mesurez à trois niveaux : métriques **DORA/flux**, **fiabilité/SLO**, et **résultats d'affaires/utilisateur**.
- La vitesse et la stabilité sont des **compléments**, pas des compromis : les pratiques qui livrent l'une livrent l'autre.
- Le pipeline est aussi un **contrôle de conformité** : l'automatisation produit une piste d'audit immuable et continue.
- Le ROI est rapide, bien prouvé (DORA), et composé ; le coût principal de ne pas investir est payé continuellement.

## Références et lectures complémentaires

- *Accelerate: The Science of Lean Software and DevOps*, par Nicole Forsgren, Jez Humble, Gene Kim (les métriques et preuves DORA).
- *Continuous Delivery*, par Jez Humble et David Farley (le texte fondateur).
- *The DevOps Handbook*, par Kim, Humble, Debois, Willis.
- *The Phoenix Project*, par Gene Kim, Kevin Behr, George Spafford (récit sur le flux).
- *Site Reliability Engineering*, par Beyer, Jones, Petoff, Murphy, éd. (SLI/SLO, budgets d'erreur).
- *Team Topologies*, par Matthew Skelton et Manuel Pais (chemins pavés et conception d'équipe de livraison).
- *Feature Flags / livraison progressive*, écrits de Pete Hodgson et des communautés LaunchDarkly/Split.
- Google DORA, rapports *Accelerate State of DevOps* (annuel).
- Kim, Gene, *The Unicorn Project* (vue expérience-développeur du flux).
- Reinertsen, Donald, *The Principles of Product Development Flow* (taille de lot, files d'attente, économie de flux).
