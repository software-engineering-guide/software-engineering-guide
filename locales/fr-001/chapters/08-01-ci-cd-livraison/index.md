# 8.1 CI/CD et livraison

## Vue d'ensemble et motivation

L'[intégration continue](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue) et la [livraison continue](https://fr.wikipedia.org/wiki/D%C3%A9ploiement_continu) (CI/CD) sont le tissu connectif entre écrire du code et le mettre devant les utilisateurs en sécurité. L'intégration continue signifie que chaque changement est fusionné fréquemment dans une ligne principale partagée, puis automatiquement construit et testé, pour que les problèmes d'intégration fassent surface en minutes plutôt qu'à la fin d'un long cycle de sortie. La livraison continue signifie que chaque changement qui passe le pipeline est gardé dans un état déployable, pour que sortir en production devienne une décision d'affaires plutôt qu'une course précipitée d'ingénierie. Le [déploiement continu](https://fr.wikipedia.org/wiki/D%C3%A9ploiement_continu) va un pas plus loin et sort chaque changement qui passe automatiquement, sans porte humaine.

Pour les grandes équipes, ces distinctions comptent énormément. Quand des centaines d'ingénieurs commettent dans des systèmes qui se chevauchent, le coût de l'intégration manuelle et du test manuel croît de façon non linéaire. Un pipeline partagé et automatisé est la seule façon pratique de donner à de nombreux contributeurs un retour rapide et digne de confiance et d'empêcher le changement d'une équipe de casser discrètement celui d'une autre. Le pipeline devient la source unique de vérité sur si le logiciel est sain, et il impose une cohérence qu'aucune quantité de documentation ou bonnes intentions ne peut garantir à l'échelle.

Les contextes d'entreprise et gouvernementaux ajoutent une dimension de plus : l'auditabilité et le contrôle de changement. Les régulateurs, agents de sécurité, et auditeurs ont besoin de preuves que les changements ont été révisés, testés, et approuvés, et que l'artefact fonctionnant en production est exactement celui qui a été construit et vérifié. Un pipeline CI/CD bien conçu transforme ces obligations de conformité d'un fardeau de paperasse en un sous-produit automatique du flux de travail d'ingénierie normal. Bien fait, la livraison devient plus rapide et plus sûre en même temps, ce qui est le résultat qui compte le plus pour la direction.

*Voir aussi :* chapitre 8.4 (ingénierie de plateforme et expérience développeur), chapitre 8.5 (automatisation de test et processus), et chapitre 7.4 (analytique de produit et expérimentation) pour les pratiques de [drapeau de fonctionnalité](https://fr.wikipedia.org/wiki/Feature_toggle) (interrupteurs d'exécution qui exposent une fonctionnalité aux utilisateurs sans redéployer) et d'expérimentation que la livraison progressive (sortir un changement graduellement tout en surveillant automatiquement ses métriques de santé) permet.

## Principes clés

- Intégrez de petits changements fréquemment ; les branches de longue durée sont l'ennemi de l'intégration continue.
- Construisez l'artefact une fois et promouvez l'artefact identique à travers chaque environnement.
- Faites du pipeline la porte faisant autorité : s'il est vert, le changement est livrable ; s'il est rouge, le travail s'arrête jusqu'à ce qu'il soit corrigé.
- Optimisez sans relâche pour un retour rapide pour que les développeurs restent dans le flux et que les défauts soient attrapés pendant que le contexte est frais.
- Automatisez tout ce qui est répété, incluant les tests, scans de sécurité, approvisionnement, et déploiement.
- Traitez les définitions de pipeline comme du code contrôlé en version sujet à revue, pas comme une configuration de console cliquable.
- Concevez pour des sorties sûres et réversibles pour que tout déploiement puisse être défait rapidement.
- Séparez le déploiement (installer le code) de la sortie (l'exposer aux utilisateurs) en utilisant des drapeaux de fonctionnalité.

## Recommandations

### Concevoir le pipeline comme une série de portes de qualité

Structurez le pipeline en étapes qui progressent du bon marché et rapide au coûteux et approfondi : compiler et tests unitaires d'abord, puis tests d'intégration, scan de sécurité et licence, et enfin déploiement vers la pré-production et production. Chaque étape est une porte qu'un changement doit passer. Ordonnez les portes pour que les vérifications les plus rapides et les plus susceptibles d'échouer s'exécutent en premier, ce qui donne aux développeurs un retour dans le temps le plus court possible. Gardez la boucle de retour de l'étape de commit sous dix minutes partout où vous le pouvez. Au-delà de cela, les développeurs changent de contexte et la productivité chute.

### Construire une fois, promouvoir partout

Produisez un seul artefact immuable à l'étape de construction et promouvez cet artefact exact à travers le test, la pré-production, et la production. Ne reconstruisez jamais par environnement, parce qu'une reconstruction peut introduire silencieusement des différences. La configuration qui varie par environnement devrait être injectée au moment du déploiement, pas cuite dans des constructions séparées. Cette pratique est aussi ce qui vous permet de dire à un auditeur, avec certitude, que le binaire en production est celui qui a passé chaque porte.

### Faire du pipeline le point d'imposition de la politique

Codez les vérifications requises (approbation de revue de code, seuils de couverture de test, résultats de scan de sécurité, commits signés) directement dans le pipeline et les règles de protection de branche. La politique manuelle qui vit dans un wiki est routinièrement contournée sous pression de délai. La politique codée dans le pipeline est appliquée uniformément et automatiquement à chaque changement.

### Garder la ligne principale livrable en tout temps

Utilisez le développement basé sur tronc, qui intègre tout le travail dans une seule branche partagée avec peu ou pas de branches de longue durée, ou utilisez des branches de fonctionnalité à courte durée, et comptez sur les drapeaux de fonctionnalité pour cacher le travail incomplet plutôt que des branches de longue durée. Cela garde les conflits de fusion petits et garde la ligne principale toujours dans un état déployable, ce qui est la précondition pour une véritable livraison continue.

### Choisir les stratégies de déploiement délibérément

Assortissez la stratégie de déploiement au risque et rayon d'explosion du service :

- Les déploiements **roulants** remplacent les instances graduellement et sont une valeur par défaut sensée pour les services sans état.
- **[Bleu-vert](https://fr.wikipedia.org/wiki/D%C3%A9ploiement_bleu-vert)** maintient deux environnements identiques et bascule le trafic tout à la fois, donnant un chemin de retour en arrière instantané.
- Les sorties **canari** acheminent un petit pourcentage de trafic vers la nouvelle version, surveillent les métriques de santé, et étendent seulement si les signaux sont bons.
- Les **drapeaux de fonctionnalité** découplent la sortie du déploiement, vous laissant activer la fonctionnalité pour des utilisateurs ou cohortes spécifiques sans redéployer.

### Adopter la livraison progressive avec retour en arrière automatisé

La livraison progressive combine les sorties canari avec l'analyse automatisée de métriques telles que le taux d'erreur, la latence, et la saturation. Définissez des critères de santé objectifs à l'avance, puis laissez le système promouvoir ou revenir en arrière automatiquement basé sur ces signaux. Le retour en arrière automatisé retire l'hésitation humaine qui transforme un petit incident en un majeur.

### Fournir la gestion de sortie et le contrôle de changement pour les environnements régulés

Dans les contextes régulés, gardez un enregistrement de gestion de changement léger mais réel. Capturez automatiquement qui a approuvé chaque changement, quels tests se sont exécutés, et quel artefact a été déployé. Utilisez des processus de conseil consultatif de changement pour les changements véritablement à haut risque, mais réservez-les pour ces cas. Acheminer chaque changement routinier à travers un conseil hebdomadaire détruit la valeur de l'automatisation. Visez plutôt des types de changement standard et pré-approuvés qui coulent à travers le pipeline sans cérémonie.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients | Meilleur ajustement |
|---|---|---|---|
| Livraison continue (porte de sortie manuelle) | L'entreprise contrôle le calendrier ; fort pour les fenêtres de sortie régulées | Exige de la discipline pour garder la ligne principale livrable | Entreprises avec fenêtres de changement |
| Déploiement continu (entièrement automatique) | Retour le plus rapide ; plus petits lots | Exige des tests et observabilité matures | Équipes à haute confiance et fréquence |
| Bleu-vert | Retour en arrière instantané ; modèle mental simple | Double le coût d'environnement pendant le basculement | Services critiques ayant besoin d'un retour rapide |
| Canari + livraison progressive | Limite le rayon d'explosion ; piloté par données | Complexe à construire ; exige de bonnes métriques | Systèmes orientés utilisateur à grande échelle |
| Drapeaux de fonctionnalité | Découple le déploiement de la sortie | Dette de drapeau si non nettoyé | Équipes livrant du travail incomplet en sécurité |

Le compromis central est la vitesse contre le contrôle, mais c'est souvent un faux choix. L'automatisation mature livre les deux : les sorties sont plus rapides parce qu'elles sont plus petites, et plus sûres parce que chacune est vérifiée et réversible. Le vrai coût est l'investissement en amont dans la couverture de test, l'observabilité, et l'ingénierie de pipeline, plus la discipline continue pour les garder sains. Les organisations qui lésinent sur cet investissement obtiennent la vitesse sans la sécurité, ce qui est pire qu'un processus manuel lent.

## Questions à discuter avec votre équipe

1. **Quelle est votre cible pour le temps de retour de l'étape de commit, et qu'est-ce qui est coupé quand la suite dépasse dix minutes ?** Une étape de commit lente tue discrètement l'intégration continue, parce que les développeurs arrêtent d'attendre le vert et commencent à grouper les changements. Décidez le nombre maintenant (ce chapitre argumente pour moins de dix minutes) et décidez le mécanisme pour le tenir : travailleurs parallèles, une pyramide de test stricte, et déplacer les vérifications d'intégration lentes vers une étape ultérieure. À l'échelle entreprise c'est une décision de plateforme, puisque des centaines d'ingénieurs partagent le même pipeline et chaque minute ajoutée se multiplie à travers chaque commit. Apportez de vraies données à la réunion : la durée de pipeline p50 et p95 actuelle, les dix tests les plus lents, et à quelle fréquence les gens réexécutent plutôt que d'attendre. Si vous ne pouvez pas énoncer la cible et la défendre avec des chiffres, votre pipeline dérive vers un processus par lots portant un costume CI.

2. **Quelle stratégie de déploiement chaque service utilise-t-il, et qui est responsable de ce choix ?** Roulant, bleu-vert, et canari ne sont pas interchangeables : ils échangent le coût, la vitesse de retour en arrière, et la complexité différemment, et le bon choix dépend du rayon d'explosion du service. Bleu-vert achète un retour en arrière instantané au prix d'un environnement doublé pendant le basculement, ce qui vaut la peine pour un système de paiement et gaspillage pour un tableau de bord interne. Canari limite l'exposition mais exige de bonnes métriques de santé et plus d'ingénierie de pipeline. Pour un parc large ou régulé, laisser cela à l'habitude de chaque équipe produit une incohérence qui fait surface pendant un incident, donc convenez de valeurs par défaut par niveau de service et enregistrez la décision. Apportez votre catalogue de service et étiquetez chaque service avec sa stratégie, son chemin de retour en arrière, et la personne qui possède cet appel.

3. **Comment prouvez-vous que l'artefact en production est exactement celui qui a passé chaque porte ?** Construire une fois et promouvoir l'artefact identique est tout le jeu pour l'auditabilité, et cela se casse au moment où quelqu'un reconstruit par environnement ou corrige une boîte en cours d'exécution. Dans les contextes d'entreprise et gouvernementaux un auditeur vous demandera de tracer un binaire en cours d'exécution jusqu'à son commit, sa revue, et ses approbations, et vous voulez que cette réponse prenne des secondes, pas une semaine. Décidez comment vous l'imposez : artefacts immuables, images signées, vérification de signature au moment du déploiement, et configuration injectée au déploiement plutôt que cuite dans des constructions séparées. Apportez les lacunes actuelles à la table, telles que toute étape qui reconstruit, tout chemin de correctif manuel, et tout endroit où la config fourche l'artefact. La réponse détermine si votre preuve de conformité est un sous-produit du pipeline ou une course précipitée manuelle avant chaque audit.

4. **Quand la ligne principale devient rouge, qu'est-ce qui s'arrête réellement, et comment gérez-vous les tests instables ?** Un pipeline n'est une porte faisant autorité que si une construction rouge arrête véritablement le travail, pourtant de nombreuses organisations tolèrent discrètement une ligne principale cassée en permanence et un arriéré d'échecs intermittents, ce qui entraîne les développeurs à réexécuter jusqu'au vert et à livrer par-dessus des échecs. Pour une grande équipe cette pourriture se compose, parce que l'instabilité ignorée d'une équipe devient l'excuse de tous pour contourner la porte, et la confiance dans le pipeline est bien moins chère à garder qu'à reconstruire. Pesez les attractions concurrentes : une règle stricte d'arrêt-de-la-ligne protège la qualité mais peut bloquer des centaines d'ingénieurs sur un seul mauvais commit, tandis qu'une politique clémente préserve le débit et érode la porte. Apportez une preuve à la discussion : votre temps rouge de ligne principale actuel, le nombre de tests mis en quarantaine ou instables, le taux de réexécution, et à quelle fréquence les changements fusionnent malgré une vérification échouée. Dans les contextes d'entreprise et gouvernementaux, nommez qui possède le triage d'instabilité et qui a l'autorité de geler les fusions, parce qu'une porte que personne n'est responsable d'imposer est une que les auditeurs trouveront routinièrement outrepassée.

5. **Quel est votre cycle de vie pour les drapeaux de fonctionnalité, et qui est en jeu pour les retirer ?** Les drapeaux sont ce qui vous permet de séparer le déploiement de la sortie et cacher le travail incomplet, mais chaque drapeau est une branche dans votre code qui n'est jamais nettoyée d'elle-même, et les drapeaux non gérés s'accumulent en complexité conditionnelle qu'ingérable. Dans un large parc cette dette est dangereuse, parce qu'un drapeau périmé peut discrètement conditionner un correctif de sécurité ou basculer des chemins de code non testés en production, et la personne qui l'a créé est souvent partie. Équilibrez la tension : les drapeaux vous ont acheté une livraison sûre et incrémentale, donc l'objectif n'est pas moins de drapeaux mais un cycle de vie discipliné avec un propriétaire, une attente d'expiration, et un outillage qui fait surface les périmés. Apportez l'inventaire actuel à la réunion : combien de drapeaux sont en direct, quel âge a le plus ancien, lesquels n'ont pas de propriétaire, et si un drapeau de longue durée fonctionne maintenant comme configuration permanente qui appartient ailleurs. Pour les environnements régulés, ajoutez qui peut changer un drapeau en production et si ce changement est journalisé avec la même rigueur qu'un déploiement, puisqu'un basculement de drapeau est une sortie même quand le pipeline ne s'exécute jamais.

6. **Où se trouve la frontière entre la livraison continue avec une porte humaine et le déploiement continu complet, et qui fixe les seuils de retour en arrière ?** La livraison continue garde une personne en contrôle du calendrier de sortie, ce qui convient aux fenêtres de changement statutaires et systèmes à haut rayon d'explosion, tandis que le déploiement continu livre chaque changement qui passe automatiquement et exige des tests matures, de l'observabilité, et un retour en arrière automatisé pour être sûr. Pour une grande organisation ou régulée la réponse est rarement uniforme : votre site marketing peut se déployer continuellement tandis que votre cœur de paiement garde une porte humaine documentée, et tracer cette ligne par niveau de service prévient à la fois la friction inutile et l'automatisation imprudente. Les considérations concurrentes sont la vitesse et la taille de lot contre le contrôle et l'auditabilité, plus le coût d'ingénierie des métriques de santé que le retour en arrière automatisé exige. Apportez la preuve : taux d'échec de changement par service, temps moyen de récupération, cadence de sortie actuelle, et les signaux objectifs (taux d'erreur, latence, saturation) auxquels vous feriez confiance pour promouvoir ou revenir en arrière sans un humain. Dans les contextes gouvernementaux et d'entreprise, liez chaque niveau à qui possède les seuils de retour en arrière et qui approuve tout mouvement d'une sortie conditionnée vers l'automatisation complète, pour que la décision soit délibérée plutôt que dérivante.

## Regard sectoriel

**Jeune pousse.** Appuyez-vous sur le CI/CD géré dès le premier jour : un exécuteur hébergé, un pipeline, une image immuable, et un déploiement automatique vers la pré-production à la fusion. Ne construisez pas d'infrastructure de pipeline que vous devrez ensuite maintenir. Les drapeaux de fonctionnalité laissent deux ou trois ingénieurs fusionner du travail à moitié terminé en sécurité et livrer plusieurs fois par jour, et un déploiement de production en un clic plus un désactivateur de drapeau rapide sont tout le contrôle de changement dont vous avez besoin jusqu'à ce que l'échelle en force plus.

**Petite entreprise.** Sans ingénieur de plateforme ou sortie dédié, favorisez le pipeline que votre hôte source vous donne (Actions intégrées ou équivalent) et sa stratégie de déploiement par défaut plutôt que quoi que ce soit sur mesure. Cadrez le choix acheter-contre-construire honnêtement : un pipeline géré et une plateforme d'hébergement avec retour en arrière intégré coûtent moins que les heures d'ingénieur qu'une configuration sur mesure consomme. Gardez les essentiels, qui sont construire une fois, promouvoir le même artefact, et un retour facile, et sautez la machinerie de livraison progressive jusqu'à ce que le volume la justifie.

**Grande entreprise.** Le problème central est la cohérence à travers de nombreuses équipes : standardisez un modèle de pipeline partagé qui impose la revue, le scan, les artefacts immuables signés, et les stratégies de déploiement par niveau, pour que la qualité ne varie pas équipe par équipe. Traitez les définitions de pipeline comme du code révisé, capturez la preuve de contrôle de changement automatiquement, et gérez les drapeaux de fonctionnalité et seuils de retour en arrière comme des actifs gouvernés plutôt que l'habitude privée de chaque équipe. Le gain est une livraison plus rapide et une preuve d'audit produite comme sous-produit au lieu d'une course précipitée trimestrielle.

**Gouvernement.** Les règles d'approvisionnement, fenêtres de changement statutaires, et responsabilité publique façonnent le pipeline. Préférez la livraison continue avec une porte de sortie humaine documentée à l'automatisation complète pour les systèmes conséquents, classifiez le travail routinier comme changements standard pré-approuvés, et gardez un chemin de retour en arrière instantané (bleu-vert ou canari automatisé) pour les services dont les citoyens dépendent pendant des fenêtres annuelles étroites. Assurez-vous que le pipeline enregistre qui a approuvé chaque changement, quels tests se sont exécutés, et quel artefact a été déployé, pour que les obligations de transparence et d'audit soient satisfaites par le flux de travail normal plutôt que par la paperasse manuelle.

## Exemples

**Jeune pousse.** Une jeune pousse SaaS de quatre personnes câble un seul pipeline GitHub Actions qui exécute des tests unitaires, construit une image Docker, et déploie cette même image vers la pré-production automatiquement à chaque fusion vers main. Un déploiement de production est un clic, et les fondateurs s'appuient sur les drapeaux de fonctionnalité pour fusionner du travail à moitié terminé derrière un drapeau au lieu de garder une branche en vie pendant des semaines. Quand une mauvaise sortie passe à travers, ils désactivent le drapeau en secondes et le corrigent calmement, ce qui garde leur minuscule équipe livrant plusieurs fois par jour sans personne d'opérations dédiée.

**Grande entreprise.** Une banque mondiale consolide des dizaines de tâches Jenkins spécifiques à l'équipe en un modèle de pipeline standardisé que chaque équipe produit hérite. Le modèle impose l'analyse statique, le scan de dépendance, et un artefact immuable signé, et il déploie via canari avec retour en arrière automatisé clé sur des seuils de taux d'erreur et latence. Parce que le même artefact est promu du test à la production et chaque porte est journalisée, les auditeurs de la banque peuvent tracer tout binaire de production jusqu'à son commit, revue, et approbation en secondes, remplaçant un exercice de collecte de preuve manuel trimestriel.

**Gouvernement.** Une administration fiscale nationale modernisant un système de dépôt adopte la livraison continue avec une porte de sortie humaine explicite, pour pouvoir respecter les fenêtres de changement statutaires pendant la saison de dépôt. Les changements routiniers sont classifiés comme changements standard pré-approuvés qui coulent automatiquement vers la pré-production. La sortie de production exige une seule approbation documentée que le pipeline enregistre. Le déploiement bleu-vert donne à l'agence un chemin de retour en arrière instantané si un défaut atteint la production, ce qui est critique quand des millions de citoyens dépendent du service pendant une fenêtre annuelle étroite.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur l'investissement CI/CD se manifeste comme un délai de changement réduit, un taux d'échec de changement plus bas, et une récupération plus rapide quand des incidents se produisent : les métriques que la recherche lie constamment à la fois à la performance de livraison et aux résultats organisationnels. Des sorties plus rapides et plus petites réduisent la surcharge de coordination qui consomme la capacité d'ingénierie à l'échelle, et la vérification automatisée réduit le travail coûteux et démoralisant de lutte contre les incendies de défauts de production.

Le coût total de possession pèse le coût d'adoption contre le coût de ne pas adopter. Les coûts d'adoption incluent construire et maintenir des pipelines, faire grandir la couverture de test, et investir dans l'observabilité et le personnel de plateforme. Le coût de ne pas adopter est plus grand mais moins visible : des sorties manuelles lentes, de la douleur d'intégration, des incidents de production qui endommagent la réputation, et, dans les contextes régulés, des audits échoués et remédiation. Pour la direction, l'argument est mieux cadré en termes de réduction de risque et capacité. L'automatisation convertit le temps rare d'ingénieur senior du labeur de sortie répétitif en travail de produit, tout en rendant les pannes plus rares et plus courtes.

## Anti-patterns et pièges

- **Pipelines flocon de neige.** Chaque équipe construit à la main un pipeline unique, donc les améliorations et corrections ne peuvent pas être partagées et la qualité varie sauvagement.
- **Reconstruire par environnement.** Reconstruire pour chaque étape casse la garantie « construire une fois » et laisse des différences subtiles atteindre la production.
- **Constructions rouges ignorées.** Tolérer une ligne principale cassée en permanence détruit la confiance dans le pipeline et normalise la livraison par-dessus des échecs.
- **Tests instables laissés non adressés.** Les échecs intermittents entraînent les développeurs à réexécuter jusqu'au vert, défaisant le but de la porte.
- **Théâtre d'approbation manuelle.** Un conseil consultatif de changement qui tamponne tout ajoute du délai sans ajouter de sécurité.
- **Dette de drapeau.** Les drapeaux de fonctionnalité jamais retirés s'accumulent en complexité conditionnelle ingérable.
- **Déploiement égale sortie.** Coupler les deux signifie que chaque changement orienté utilisateur exige un redéploiement risqué.

## Modèle de maturité

**Niveau 1 (Initier).** Les constructions et déploiements sont largement manuels, au coup par coup, et réactifs. L'intégration se passe tard, les sorties sont peu fréquentes et stressantes, le retour en arrière signifie redéployer une ancienne version à la main, et il n'y a pas de notion partagée d'une porte de pipeline.

**Niveau 2 (Développer).** Les constructions automatisées et tests unitaires s'exécutent à chaque commit, mais les pratiques varient équipe par équipe. Les déploiements sont scriptés mais encore déclenchés et supervisés manuellement, certains environnements sont cohérents, et les artefacts peuvent encore être reconstruits par étape. Où un pipeline existe c'est souvent un flocon de neige qui ne peut pas être partagé.

**Niveau 3 (Standardiser).** Un modèle de pipeline documenté et standardisé est imposé à travers les équipes. Il promeut un seul artefact immuable à travers tous les environnements, applique des portes de qualité et sécurité automatisées, code des vérifications requises telles que l'approbation de revue et les résultats de scan, et capture les enregistrements de changement automatiquement. Les stratégies de déploiement telles que canari ou bleu-vert sont choisies délibérément par niveau de service.

**Niveau 4 (Gérer).** La livraison est mesurée et contrôlée contre des références. L'organisation suit le délai de changement, la fréquence de déploiement, le taux d'échec de changement, et le temps moyen de récupération, avec la durée de pipeline p50 et p95, les taux de test instable et réexécution, et l'âge de drapeau de fonctionnalité. Les seuils de retour en arrière sont fixés depuis les données observées de taux d'erreur, latence, et saturation, les portes sont imposées sur preuve plutôt qu'habitude, et chaque métrique a un propriétaire qui agit quand elle dérive de la cible.

**Niveau 5 (Orchestrer).** La livraison s'améliore continuellement et est intégrée à travers l'organisation. La livraison progressive avec retour en arrière automatisé et piloté par métrique est la norme, la sortie est découplée du déploiement via des drapeaux bien gouvernés, et la preuve de conformité est produite automatiquement comme sous-produit. Le pipeline s'adapte à mesure que le parc change, et les métriques de livraison alimentent la planification d'affaires et de risque pour que l'investissement coule vers les améliorations à plus haut levier.

## Pistes de réflexion

- Où se trouve la bonne frontière entre la livraison continue avec une porte humaine et le déploiement continu complet pour vos systèmes les plus critiques ?
- Comment gardez-vous un processus de gestion de changement obligatoire significatif sans le transformer en théâtre de tampon ?
- Quelles métriques de santé objectives devraient gouverner le retour en arrière automatisé, et qui possède leurs seuils ?
- Comment les équipes de plateforme devraient-elles équilibrer les modèles de pipeline standardisés contre les besoins légitimes d'équipes avec des exigences inhabituelles ?
- Quelle est votre politique et outillage pour retirer les drapeaux de fonctionnalité avant qu'ils ne deviennent de la dette ?
- Comment mesurez-vous si une livraison plus rapide améliore réellement les résultats d'affaires plutôt que juste livrer plus ?

## Points clés à retenir

- CI, CD, et déploiement continu sont distincts ; choisissez le niveau d'automatisation qui correspond à votre tolérance au risque et maturité.
- Construisez l'artefact une fois et promouvez l'artefact identique à travers chaque environnement.
- Concevez le pipeline comme des portes de qualité ordonnées optimisées pour un retour rapide, et traitez-le comme la décision de livraison faisant autorité.
- Choisissez les stratégies de déploiement délibérément, et adoptez la livraison progressive avec retour en arrière automatisé pour limiter le rayon d'explosion.
- Découplez la sortie du déploiement avec des drapeaux de fonctionnalité, et gérez la dette de drapeau.
- Dans les environnements régulés, capturez la preuve de contrôle de changement automatiquement plutôt qu'à travers la paperasse manuelle.

## Références et lectures complémentaires

- Jez Humble et David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, et Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, et John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, et George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, et Niall Richard Murphy (éd.), *Site Reliability Engineering*.
- Pete Hodgson, « Feature Toggles (Feature Flags) » (essai).
- ITIL (Information Technology Infrastructure Library), directive de gestion de changement.
