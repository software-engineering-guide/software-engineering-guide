# 2.4 Stratégie de test

## Vue d'ensemble et motivation

Une stratégie de [test](https://en.wikipedia.org/wiki/Software_testing) est l'ensemble délibéré de choix sur quoi tester, à quel niveau, à quel point automatiquement, et avec quelle confiance, afin que votre équipe puisse changer le code rapidement sans le casser. Les tests sont ce qui laisse une grande organisation déployer souvent et en sécurité. Ils encodent le comportement attendu, attrapent les régressions, et donnent aux ingénieurs la confiance pour [refactoriser](https://en.wikipedia.org/wiki/Code_refactoring). Sans une stratégie cohérente, le test tend à aller dans l'une de deux mauvaises directions : absent (développement piloté par la peur, lent) ou boursouflé (des milliers de tests lents et instables auxquels personne ne fait confiance).

Pour une grande équipe, la stratégie compte plus que tout test individuel. Des centaines d'ingénieurs travaillant dans une base de code partagée ont besoin d'un filet de sécurité rapide et fiable. Sans cela, chaque changement est risqué et chaque publication se transforme en épreuve manuelle. Les tests fonctionnent aussi comme documentation exécutable du comportement voulu, ce qui est inestimable une fois que les auteurs d'origine sont passés à autre chose. La stratégie décide si votre suite de tests est un atout qui accélère la livraison ou un passif qui la freine.

Dans les contextes d'entreprise et gouvernementaux, le test porte un poids supplémentaire. Les réglementations peuvent exiger une couverture de test documentée et des preuves. Les systèmes critiques pour la sécurité et face aux citoyens exigent une haute assurance. Les tests d'accessibilité et de sécurité peuvent être légalement requis. Donc la stratégie doit équilibrer vitesse, confiance, coût, et conformité, et elle doit traiter la couverture comme un signal, pas une cible à détourner.

## Principes clés

- Testez pour gagner la confiance de changer, pas pour atteindre un chiffre.
- Favorisez des tests rapides, fiables, et isolés. Les tests lents ou instables érodent la confiance qui rend une suite utile.
- Poussez les tests au niveau le plus bas qui donne une vraie confiance, et gardez les tests lents et larges pour un vrai risque d'intégration.
- Un test instable est un test cassé. Traitez l'instabilité comme un défaut de premier ordre.
- La couverture est un signal, pas un objectif. Une haute couverture de code trivial ne prouve pas grand-chose.
- Testez le comportement et les contrats, pas les détails d'implémentation, afin que vos tests survivent à la refactorisation.
- Faites du test non fonctionnel (accessibilité, performance, sécurité) une partie de la stratégie, pas une réflexion après coup.

## Recommandations

### Utilisez la pyramide de tests comme défaut, et connaissez ses critiques

Optez par défaut pour de nombreux [tests unitaires](https://en.wikipedia.org/wiki/Unit_testing) rapides, moins de [tests d'intégration](https://en.wikipedia.org/wiki/Integration_testing), et un petit nombre de tests de bout en bout, parce que le coût et la fragilité augmentent avec la portée. Connaissez aussi les critiques : la forme devrait suivre votre architecture, pas le dogme. Un système riche en services peut avoir besoin d'une plus grande couche d'intégration (le « trophée de test »), et le vrai objectif est la confiance par unité de coût et de vitesse, pas une silhouette particulière. Quoi que vous fassiez, évitez la pyramide inversée de tests de bout en bout surtout lents.

### Adoptez le TDD, le BDD, et le développement piloté par les spécifications là où ils aident

Utilisez le [développement piloté par les tests](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) pour conduire la conception et garantir la testabilité, spécialement pour la logique complexe. C'est une discipline de conception autant que de test. Utilisez le [développement piloté par le comportement](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) pour exprimer les tests dans le langage de domaine que vous partagez avec les parties prenantes, ce qui est précieux pour les critères d'acceptation dans des environnements réglementés ou riches en exigences. Le développement piloté par les spécifications va un pas plus loin : il traite une spécification exécutable (le comportement convenu, exprimé comme des exemples) comme la source de vérité unique qui guide l'implémentation et la vérifie. Cela brille là où les exigences doivent être traçables aux preuves d'acceptation, comme dans les programmes gouvernementaux et réglementés. Lié aux trois est le **[test décalé à gauche](https://en.wikipedia.org/wiki/Shift-left_testing)** (shift-left) : déplacer la vérification aussi tôt que possible dans le cycle de vie, écrivant les tests aux côtés ou avant le code et les exécutant continuellement, afin d'attraper les défauts quand ils sont les moins chers à corriger, plutôt que dans des phases de test tardives ou en production. Aucun de ceux-ci n'est obligatoire partout. Appliquez-les là où ils ajoutent de la clarté.

### Employez des techniques avancées pour le code à haute valeur

Utilisez le test basé sur les propriétés pour vérifier des invariants à travers de nombreuses entrées générées, attrapant des cas limites que les tests basés sur des exemples ratent. Utilisez le [test fuzzing](https://en.wikipedia.org/wiki/Fuzzing) sur les analyseurs et les frontières d'entrée non fiables pour trouver des plantages et des failles de sécurité. Utilisez le [test de mutation](https://en.wikipedia.org/wiki/Mutation_testing) pour mesurer si vos tests détectent réellement des fautes injectées, un bien meilleur signal de qualité que la couverture brute. Utilisez le test d'instantané avec discernement pour la sortie sérialisée, et méfiez-vous du piège de réapprouver aveuglément les instantanés.

### Gérez les données de test et utilisez des données synthétiques

Rendez les tests déterministes avec des données de test contrôlées et isolées, et évitez les fixtures mutables partagées qui couplent les tests ensemble. Générez des [données synthétiques](https://en.wikipedia.org/wiki/Synthetic_data) qui reflètent les caractéristiques de production sans exposer de vraies informations personnelles, ce qui est essentiel là où les règles de confidentialité interdisent d'utiliser des données de production dans les environnements de test. Fournissez des fabriques ou des constructeurs afin que chaque test puisse construire exactement les données dont il a besoin.

### Traitez les tests instables comme des défauts

Détectez l'instabilité automatiquement, déplacez les tests instables hors du chemin bloquant, et corrigez-les ou supprimez-les sur une échéance. Une suite qui échoue au hasard entraîne les ingénieurs à ignorer les échecs, ce qui détruit toute sa valeur. Suivez les taux d'instabilité et faites de la fiabilité une métrique de qualité explicite pour la suite de tests elle-même.

### Utilisez la couverture comme signal, et ajoutez le test non fonctionnel

Mesurez la couverture pour trouver les zones non testées, mais ne la transformez pas en une cible dure qui invite au détournement avec des tests sans assertion. Complétez-la avec le test de mutation pour la profondeur. Intégrez le test d'accessibilité (contrôles automatisés plus audits manuels), le test de performance (références de charge et de latence avec détection de régression), et le test de sécurité (analyse de dépendances, [analyse statique](https://en.wikipedia.org/wiki/Static_program_analysis), et test dynamique) dans le pipeline.

## Compromis : avantages et inconvénients

| Type de test / pratique | Avantages | Inconvénients |
|---|---|---|
| Tests unitaires | Rapides, précis, peu coûteux, stables | Ratent les bugs d'intégration et de niveau système |
| Tests d'intégration | Attrapent les défauts d'interface et de câblage | Plus lents ; plus de configuration ; plus fragiles |
| Tests de bout en bout | Confiance la plus haute dans le comportement réel | Lents, instables, coûteux à maintenir |
| TDD | Meilleure conception, testabilité garantie | Courbe d'apprentissage ; semble lent initialement |
| Test basé sur les propriétés | Trouve les cas limites, encode les invariants | Exige de penser en propriétés ; plus difficile à écrire |
| Test de mutation | Vraie mesure de l'efficacité des tests | Coûteux en calcul ; lent à exécuter |
| Cible de haute couverture | Fait surgir le code non testé | Détournable ; peut inciter des tests à faible valeur |

Le compromis central est la confiance contre la vitesse et le coût. Des tests plus larges donnent plus de confiance mais s'exécutent plus lentement et cassent plus souvent. Des tests plus étroits sont rapides et stables mais ratent les défauts de niveau système. Le bon mélange maximise la confiance par seconde de retour et par heure de maintenance. Et le sur-test est un vrai mode d'échec : une suite boursouflée de tests redondants, lents, et fragiles peut coûter plus que les bugs qu'elle prévient.

## Questions à discuter avec votre équipe

1. **Quels tests non fonctionnels, accessibilité, performance, et sécurité, devraient bloquer une publication, et lesquels devraient seulement rapporter ?** Ce chapitre argumente que le test non fonctionnel appartient à la stratégie plutôt qu'à une réflexion après coup, et note que l'accessibilité peut être légalement requise et que le test de sécurité peut faire partie de la preuve d'autorisation d'exploitation. Pour un grand système ou un système face aux citoyens, une porte bloquante ralentit la livraison, mais un défaut d'accessibilité ou de sécurité trouvé en production porte un coût de remédiation, de réputation, et légal qui éclipse le test. Apportez les signaux qui décident : votre exposition réglementaire, si le système fait face aux citoyens, et à quelle fréquence ces défauts s'échappent actuellement vers la production. Rendez les contrôles légalement requis bloquants et laissez les contrôles à risque plus faible rapporter avec une tendance, afin que la porte reflète le vrai risque plutôt que le dogme. La réponse fixe directement ce qui peut et ne peut pas fusionner.

2. **Fixez-vous un pourcentage de couverture dur comme porte, et si oui, qu'est-ce qui empêche les ingénieurs de le détourner avec des tests sans assertion ?** Le chapitre est ferme que la couverture est un signal, pas un objectif, qu'une haute couverture de code trivial ne prouve pas grand-chose, et qu'une cible dure invite au détournement. Un seul chiffre imposé à travers une grande organisation produit fiablement des tests qui exécutent du code sans rien affirmer, ce qui élève la métrique et abaisse la vraie confiance. Apportez un meilleur signal à la discussion : un score de test de mutation sur vos modules à plus haute valeur, qui mesure si les tests détectent réellement des fautes injectées. Utilisez la couverture pour trouver les zones non testées et le test de mutation pour la profondeur, et résistez à transformer l'un ou l'autre en une cible que la direction suit isolément. Décidez où le chiffre aide réellement et où il n'invite que le théâtre.

3. **Quelle est votre politique quand la suite de tests devient trop lente pour que les ingénieurs l'attendent ?** Le compromis central de ce chapitre est la confiance contre la vitesse et le coût, et il nomme le sur-test comme un vrai mode d'échec où une suite boursouflée, redondante, et lente coûte plus que les bugs qu'elle prévient. Dans une grande équipe, le temps d'exécution de la suite est une taxe partagée payée à chaque changement, et une suite que les gens apprennent à contourner perd toute sa valeur. Apportez les preuves : le temps horloge de la CI, les tests les plus lents, et combien de couverture de bout en bout redondante duplique des tests unitaires moins chers. Poussez les tests au niveau le plus bas qui donne une vraie confiance, parallélisez, et supprimez les tests lents redondants sur une échéance. Optimiser la confiance par seconde de retour, pas le nombre brut de tests, est l'objectif.

4. **Quand un test devient instable, qui le possède, à quelle vitesse doit-il être corrigé ou supprimé, et qu'est-ce qui applique cette échéance ?** Ce chapitre traite un test instable comme un test cassé, un défaut de premier ordre, parce qu'une suite qui échoue au hasard entraîne une grande équipe à ignorer les constructions rouges et détruit silencieusement le filet de sécurité dont tout le monde dépend. La pression concurrente est réelle : mettre en quarantaine un test instable débloque la livraison aujourd'hui mais risque de masquer un vrai bug intermittent, tandis que bloquer dessus arrête des centaines d'ingénieurs sur un échec qui peut être du bruit pur. Apportez la preuve qui tranche : votre taux d'instabilité actuel, combien de temps les tests restent en quarantaine avant que quiconque n'y touche, et combien de tests en quarantaine se sont avérés cacher un vrai défaut. Assignez un propriétaire à chaque test en quarantaine, fixez une échéance dure pour corriger ou supprimer, et suivez la fiabilité comme une métrique explicite pour la suite elle-même. Dans les contextes d'entreprise et gouvernementaux où une construction verte fait partie de la preuve de publication, une pile de quarantaine non gérée est aussi un passif d'audit, parce que vous livrez sur un signal auquel vous avez privément convenu de ne pas faire confiance.

5. **Êtes-vous autorisés à utiliser des données de production dans les environnements de test, et sinon, comment générerez-vous des données synthétiques assez fidèles pour attraper de vrais défauts ?** Le chapitre est direct que les règles de confidentialité interdisent souvent les vraies données personnelles en test, et que les données synthétiques doivent refléter les caractéristiques de production sinon vos tests donnent une fausse confiance. Pour une grande organisation, la tension est entre la fidélité et la conformité : les données de production attrapent les cas limites désordonnés que les données synthétiques ratent, mais chaque copie multiplie votre exposition et vos obligations. Apportez les spécificités : quels ensembles de données portent des données personnelles ou réglementées, ce que vos règles de confidentialité et de résidence des données exigent réellement, et à quel point vos fixtures actuelles reproduisent les distributions et cas limites vus en production. Standardisez des fabriques ou constructeurs afin que chaque test construise exactement les données dont il a besoin, et investissez dans une génération synthétique qui correspond aux vraies distributions démographiques et de volume. Dans les programmes gouvernementaux et réglementés, utiliser des données citoyennes dans un environnement de test n'est pas un raccourci, c'est une violation signalable, donc la stratégie de données doit être réglée avant que le premier environnement ne soit monté.

6. **Où le TDD, le BDD, ou le développement piloté par les spécifications devraient-ils être attendus plutôt qu'optionnels, et qui décide ?** Ce chapitre présente ceux-ci comme des disciplines à appliquer là où elles ajoutent de la clarté, pas des mandats pour chaque ligne de code, pourtant une grande équipe bénéficie d'un défaut partagé afin que la pratique ne se fragmente pas équipe par équipe. Le compromis est entre les bénéfices de conception et de traçabilité (des spécifications exécutables que les experts de politique peuvent réviser, des tests qui survivent à la refactorisation) et la véritable courbe d'apprentissage et la lenteur initiale qui font qu'un mandat général se retourne contre lui-même. Apportez des preuves pour le cadrer : quels modules portent une logique complexe ou des taux d'échec de changement élevés, où les critères d'acceptation doivent être traçables aux exigences, et comment les équipes pratiquant déjà cela rapportent sur la vitesse et les taux de défauts. Réservez l'attente pour la logique complexe et les zones riches en exigences, et laissez le code plus simple choisir pour lui-même. Dans les programmes réglementés et gouvernementaux où le logiciel doit être traçable à la loi qu'il implémente, le développement piloté par les spécifications avec une preuve d'acceptation exécutable est moins une préférence qu'une route vers votre autorisation d'exploitation, donc nommez explicitement où c'est requis.

## Regard sectoriel

**Jeune pousse.** Une toute petite équipe ne peut pas doter une QA, alors faites en sorte que la suite justifie son coût : des tests unitaires rapides à chaque commit plus quelques tests de bout en bout sur l'unique chemin qui paie les factures, et rien que vous ne maintiendrez pas. Sautez les cibles de couverture et testez la logique que vous avez le plus peur de casser, afin de pouvoir livrer plusieurs fois par jour sans passe de régression manuelle. Corrigez un test instable le jour même, parce qu'à ce stade une suite que l'équipe apprend à ignorer est pire que pas de suite du tout.

**Petite entreprise.** Sans ingénieur de test dédié et avec un budget serré, appuyez-vous sur le test intégré aux cadres et outils que vous faites déjà fonctionner plutôt qu'un harnais sur mesure que vous ne pouvez pas supporter. Priorisez la poignée de contrôles qui protègent le revenu et la confiance client, et utilisez une CI hébergée afin de ne pas maintenir l'infrastructure de construction vous-même. Préférez acheter le scan d'accessibilité et de sécurité comme service plutôt que le construire, puisqu'un seul défaut manqué peut coûter plus qu'une année de l'outil.

**Grande entreprise.** À travers de nombreuses équipes, le problème de stratégie est la cohérence : un défaut de pyramide partagé, une quarantaine automatique de tests instables, et des portes non fonctionnelles qui signifient la même chose partout, afin qu'une construction verte soit fiable peu importe qui l'a produite. Budgétez le temps d'exécution de la suite comme une taxe partagée et parallélisez agressivement, parce que le temps horloge de la CI est payé à chaque changement par chaque ingénieur. Gérez les scores de couverture et de mutation comme des signaux de portefeuille avec une propriété claire, pas des chiffres que la direction suit isolément.

**Gouvernement.** Les marchés publics et la surveillance font du test une preuve, pas seulement de l'hygiène d'ingénierie. Exprimez les règles d'éligibilité et de politique comme des spécifications exécutables révisées par des experts de domaine, afin de pouvoir tracer le logiciel à la loi qu'il implémente, et rendez le test d'accessibilité et de sécurité bloquant parce qu'ils sont légalement requis et font partie de la preuve d'autorisation d'exploitation. Utilisez des données synthétiques générées pour correspondre aux vraies distributions, puisque des données citoyennes dans un environnement de test sont une violation signalable, et gardez les artefacts de test auditables afin qu'un réviseur externe puisse confirmer exactement ce qui a été vérifié.

## Exemples

**Jeune pousse.** Une start-up de cinq personnes ne peut pas se permettre une équipe QA, alors elle s'appuie sur une suite de tests unitaires rapide qui s'exécute à chaque commit plus quelques tests de bout en bout couvrant le chemin d'inscription-à-paiement qui paie les factures. Les fondateurs sautent la couverture exhaustive et testent à la place la logique qu'ils ont le plus peur de casser, ce qui leur permet de livrer plusieurs fois par jour sans passe de régression manuelle. Quand un test instable commence à échouer au hasard, ils le corrigent le jour même, parce qu'une suite que l'équipe apprend à ignorer est pire que pas de suite au stade où la confiance est tout.

**Grande entreprise.** Une grande plateforme de commerce électronique maintient des milliers de tests unitaires rapides qui s'exécutent à chaque commit en quelques minutes, un ensemble ciblé de tests d'intégration autour des frontières de paiement et d'inventaire, et une petite suite de tests de bout en bout pour les parcours de paiement critiques. Les tests de bout en bout instables sont automatiquement mis en quarantaine et assignés pour réparation. Parce que les ingénieurs font confiance à la suite, ils déploient plusieurs fois par jour, confiants qu'une construction rouge signifie un vrai problème.

**Gouvernement.** Un système national de prestations opérant sous surveillance réglementaire utilise le BDD pour exprimer les règles d'éligibilité comme des spécifications exécutables révisées par des experts de politique, ce qui donne une preuve traçable que le logiciel implémente la loi. Il utilise des données synthétiques générées pour correspondre aux vraies distributions démographiques, parce que les règles de confidentialité interdisent les données citoyennes dans les environnements de test. Le test d'accessibilité est obligatoire et bloque la publication, puisque le service doit être utilisable par tous les citoyens. Et le test de sécurité fait partie de la preuve d'autorisation d'exploitation (ATO), l'approbation formelle pour faire fonctionner le système en production.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur le test est la capacité de changer le logiciel rapidement et en sécurité, ce qui est le fondement de la vitesse de livraison soutenue. Une suite automatisée fiable remplace le [test de régression](https://en.wikipedia.org/wiki/Regression_testing) manuel lent et coûteux et attrape les défauts quand ils sont les moins chers à corriger, avant la publication plutôt qu'en production. Dans un système réglementé ou face aux citoyens, le coût d'un défaut de production (remédiation, réputation, et exposition légale potentielle) éclipse le coût des tests qui l'auraient attrapé.

Le coût d'adoption est réel : vous écrivez et maintenez des tests, et construisez l'infrastructure d'[intégration continue](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Mais le coût de ne pas tester est plus élevé et il s'accumule : un développement piloté par la peur qui ralentit jusqu'à ramper, des régressions fréquentes, et des processus de publication manuels qui ne peuvent pas passer à l'échelle. Il y a aussi un coût au sur-test, donc l'argument est pour une stratégie bien conçue, pas le nombre maximum de tests. Pour convaincre la direction, reliez la suite à la fréquence de déploiement, au taux d'échec des changements, et au temps moyen de rétablissement, et quantifiez l'effort de test manuel qu'elle remplace et les incidents de production qu'elle prévient.

## Anti-patterns et pièges

- **Le test en cône de glace :** surtout des tests de bout en bout lents sur une base unitaire mince ; lent, instable, coûteux.
- **La couverture comme cible :** poursuivre un pourcentage avec des tests sans assertion ou triviaux qui ne prouvent rien.
- **Tester les détails d'implémentation :** des tests couplés aux internes qui cassent à chaque refactorisation, décourageant le changement.
- **L'instabilité tolérée :** des échecs aléatoires qui entraînent l'équipe à ignorer les constructions rouges.
- **Les données de test mutables partagées :** des tests qui interfèrent entre eux et échouent de façon imprévisible.
- **Utiliser des données de production en test :** une violation de confidentialité et de conformité qui attend d'arriver.
- **Le test non fonctionnel sauté :** accessibilité, performance, et sécurité découvertes seulement en production.
- **La suite non fiable :** si peu fiable que les ingénieurs la réexécutent ou la contournent couramment, niant son but.

## Modèle de maturité

- **Niveau 1, Initiation :** Le test est manuel et réactif ; la couverture automatisée est minimale ; les régressions sont fréquentes et attrapées tard, souvent par les utilisateurs plutôt que la suite.
- **Niveau 2, Développement :** Des tests unitaires automatisés et quelques tests d'intégration existent, mais la suite est lente ou instable, la confiance est basse, et la pratique varie largement d'une équipe à l'autre.
- **Niveau 3, Standardisation :** Une suite équilibrée, rapide, et fiable conditionne chaque changement ; un défaut de pyramide documenté, une politique de test instable, et le test non fonctionnel (accessibilité, performance, sécurité) sont appliqués de manière cohérente entre équipes.
- **Niveau 4, Gestion :** La santé de la suite est mesurée et contrôlée par rapport à des références ; le taux d'instabilité, le temps horloge de la CI, le score de mutation sur les modules à haute valeur, et le taux de défauts échappés sont suivis et révisés ; la couverture est un signal parmi plusieurs, et les portes se déclenchent sur preuve plutôt qu'opinion.
- **Niveau 5, Orchestration :** Des techniques avancées (basées sur les propriétés, mutation, fuzzing) ciblent le code à haute valeur ; le test est intégré aux métriques de livraison comme la fréquence de déploiement, le taux d'échec des changements, et le temps moyen de rétablissement ; l'organisation remodèle continuellement la suite selon son architecture et son risque, retirant les tests redondants et investissant là où les preuves montrent que des défauts s'échappent encore.

## Pistes de réflexion

- Quelle forme votre distribution de tests prend-elle réellement, et correspond-elle à votre architecture et votre risque ?
- Comment décidez-vous quand un morceau de code justifie un test basé sur les propriétés ou de mutation contre des tests d'exemple ?
- Quelle est votre politique pour les tests instables, et est-elle réellement appliquée ?
- Comment générez-vous des données synthétiques réalistes sans fuiter d'informations sensibles ?
- Où la couverture vous aide-t-elle réellement, et où a-t-elle été détournée ?
- Comment les tests générés par IA devraient-ils être révisés afin qu'ils ajoutent de la confiance plutôt que du bruit ?

## Points clés à retenir

- Testez pour gagner la confiance de changer ; optimisez la confiance par unité de vitesse et de coût.
- Utilisez la pyramide comme défaut mais façonnez le test selon votre architecture.
- Traitez les tests instables comme des défauts et la couverture comme un signal, pas une cible.
- Appliquez des techniques avancées là où la valeur justifie le coût.
- Incluez le test d'accessibilité, de performance, et de sécurité dans la stratégie, et utilisez des données synthétiques pour protéger la confidentialité.

## Références et lectures complémentaires

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin et Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles sur la pyramide de tests et les patrons liés au test
