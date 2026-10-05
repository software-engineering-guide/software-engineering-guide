# 6.2 Ingénierie d'apprentissage automatique (MLOps)

## Vue d'ensemble et motivation

L'ingénierie d'apprentissage automatique, habituellement appelée [MLOps](https://fr.wikipedia.org/wiki/MLOps), est la discipline de sortir l'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) des carnets et expériences pour l'amener dans des systèmes de production fiables, observables, et maintenables. Le logiciel traditionnel se comporte comme son code dit qu'il le fera. Un système d'apprentissage automatique se comporte comme son code, ses données, et ses paramètres de modèle appris disent ensemble qu'il le fera. Cela rend les systèmes d'apprentissage automatique plus difficiles à tester, plus difficiles à reproduire, et sujets à échouer silencieusement à mesure que le monde dérive des données sur lesquelles ils ont été entraînés. Le MLOps apporte la rigueur de l'ingénierie logicielle (contrôle de version, test, livraison continue, et surveillance) à cette réalité en trois parties du code plus des données plus des modèles.

Pour les grandes équipes, le MLOps est ce qui sépare un modèle ponctuel qui éblouit dans une démonstration d'une flotte de modèles que de nombreuses équipes peuvent construire, déployer, et exploiter en sécurité. Sans plateformes et pratiques partagées, chaque équipe réinvente les pipelines de données, boucles d'entraînement, et déploiement, et vous finissez avec des systèmes fragiles que personne ne peut reproduire six mois plus tard. Les entreprises comptent sur le MLOps pour s'échelonner à travers des dizaines de modèles, satisfaire des objectifs de niveau de service, et satisfaire les auditeurs qui demandent comment une prédiction donnée a été produite.

Dans l'administration publique et les industries régulées, le MLOps est souvent une exigence de conformité déguisée. La reproductibilité, la lignée, et le versionnage sont ce qui permet à une agence de répondre à une question légalement significative : exactement quel modèle, entraîné sur quelles données, avec quel code, a produit la décision qui a affecté un citoyen ? Une pratique MLOps mature garde cette question répondable des années plus tard, ce qui est à la fois de la bonne ingénierie et une garantie légale.

*Voir aussi :* chapitre 8.1 (CI/CD et livraison), chapitre 9.2 (observabilité et surveillance), et chapitre 6.6 (infrastructure et opérations d'IA).

## Principes clés

- Traitez les données, le code, et les modèles comme des artefacts conjointement versionnés ; changer l'un change le comportement du système.
- Automatisez le chemin des données au modèle entraîné au déploiement pour qu'il soit répétable et auditable.
- Rendez chaque modèle traçable aux données, code, et configuration exacts qui l'ont produit.
- Évaluez les modèles contre des données représentatives et mises de côté avant le déploiement, et continuez d'évaluer après.
- Supposez que les modèles se dégradent ; surveillez la dérive (la divergence graduelle des données en direct ou des relations entrée-sortie de ce sur quoi le modèle a été entraîné), les problèmes de qualité de données, et la décroissance de performance dès le premier jour.
- Préférez des pipelines ennuyeux et reproductibles à des expériences astucieuses et irreproductibles.
- Séparez les préoccupations de vitesse d'expérimentation et de fiabilité de production, et pontez-les délibérément.

## Recommandations

### Gérer explicitement le cycle de vie ML complet

Définissez et instrumentez chaque étape : ingestion et validation de données, [ingénierie de caractéristiques](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie_des_caract%C3%A9ristiques), entraînement, évaluation, déploiement, et surveillance. Rendez les frontières entre étapes explicites pour que chacune puisse être testée, retentée, et auditée. Évitez l'échec courant où un modèle est entraîné dans un carnet au coup par coup et jeté par-dessus le mur aux opérations. Au lieu de cela, enveloppez le cycle de vie dans un pipeline orchestré que tout ingénieur autorisé peut exécuter depuis un extrait propre.

### Utiliser des magasins de caractéristiques, du suivi d'expérience, et des registres de modèle

Un **magasin de caractéristiques** centralise les définitions de caractéristiques pour que les mêmes transformations s'exécutent à la fois en entraînement et en service. Cela élimine le biais entraînement-service (des incohérences entre comment les caractéristiques sont calculées pour l'entraînement contre les prédictions en direct) et laisse les équipes réutiliser les caractéristiques plutôt que de les recalculer. Le **suivi d'expérience** enregistre les paramètres, la version de code, la version de données, et les métriques de chaque exécution d'entraînement, pour que les résultats soient comparables et reproductibles. Un **registre de modèle** est le système d'enregistrement pour les modèles entraînés, tenant les versions, la lignée, les résultats d'évaluation, le statut d'approbation, et l'étape de déploiement. Ensemble, ceux-ci vous laissent répondre « qu'est-ce qui a changé ? » quand le comportement bascule, et promouvoir ou revenir en arrière sur des modèles à travers des étapes gouvernées.

### Rendre les données et modèles reproductibles et versionnés avec lignée

Versionnez vos jeux de données, pas seulement votre code. Utilisez le stockage adressable par contenu ou des outils de versionnage de données pour qu'une exécution d'entraînement référence un instantané immuable. Épinglez le code avec des commits git, et épinglez les environnements avec des dépendances verrouillées et des images de conteneur. Capturez la lignée de bout en bout : quelles données brutes ont alimenté quelles caractéristiques, quelles caractéristiques et code ont produit quel modèle, et où ce modèle est déployé. Quand un incident ou audit frappe, la lignée transforme un cauchemar forensique en une simple requête. Enregistrez l'aléa (graines) et le matériel partout où les résultats en dépendent.

### Choisir des motifs de déploiement assortis à la charge de travail

- **Le scoring par lots** s'exécute selon un calendrier sur de grands jeux de données ; le plus simple à exploiter, tolérant à la latence, idéal pour les rapports et décisions périodiques.
- **Le service en ligne (temps réel)** répond aux requêtes individuelles dans des budgets de latence serrés ; a besoin d'une récupération de caractéristiques à faible latence et d'une planification de capacité soigneuse.
- **Le streaming** score les événements continuellement à mesure qu'ils arrivent ; convient à la détection de fraude et la surveillance où la fraîcheur est critique.
- **Le bord (edge)** exécute des modèles sur des appareils ou du matériel sur site pour des raisons de latence, confidentialité, connectivité, ou souveraineté de données, courant dans les contextes gouvernementaux et de terrain.

Choisissez le motif le plus simple qui satisfait l'exigence, et concevez votre déploiement avec des déploiements fantômes, des canaris, et un retour en arrière instantané.

### Surveiller la dérive, la dégradation, et la qualité de données

Instrumentez les entrées et sorties en production. Surveillez la **dérive de données** (distributions d'entrée qui basculent), la **[dérive de concept](https://fr.wikipedia.org/wiki/D%C3%A9rive_de_concept)** (la relation entre les entrées et la cible qui change), les échecs de **qualité de données** (nulls, changements de schéma, sources amont cassées), et la **dégradation de performance** mesurée contre la vérité terrain retardée où vous l'avez. Fixez des seuils d'alerte, écrivez des livres d'exécution, et câblez la surveillance à vos déclencheurs de réentraînement. La dégradation silencieuse est le mode d'échec classique de l'apprentissage automatique, et la surveillance est votre seule défense contre lui.

## Compromis : avantages et inconvénients

| Décision | Option A | Option B | Compromis |
|---|---|---|---|
| Motif de service | Par lots | En ligne | Simplicité et coût contre fraîcheur et latence |
| Calcul de caractéristiques | Magasin de caractéristiques | Pipelines par modèle | Cohérence et réutilisation contre surcharge de configuration |
| Plateforme | Acheter une plateforme MLOps gérée | Assembler des outils open source | Vitesse et support contre flexibilité et verrouillage |
| Réentraînement | Planifié | Déclenché par dérive | Prévisibilité contre réactivité et complexité |
| Rigueur de reproductibilité | Versionnage de données complet | Suivi léger | Force d'audit contre stockage et effort |

Le compromis global est l'investissement maintenant contre la fragilité plus tard. Une infrastructure lourde de reproductibilité et surveillance coûte de l'effort en amont, mais elle prévient le coût bien plus large d'échecs inexplicables, de modèles non reproductibles, et de confiance érodée. Les plateformes gérées accélèrent les équipes mais peuvent créer du verrouillage ; les piles open source offrent du contrôle au prix du travail d'intégration. Les grandes organisations bénéficient habituellement d'une équipe de plateforme partagée qui cache cette complexité derrière des valeurs par défaut de chemin pavé.

## Questions à discuter avec votre équipe

1. **Comment apprendrions-nous qu'un modèle déployé s'est discrètement dégradé avant qu'un client ou citoyen ne soit lésé, et qui possède cette alerte ?** La décroissance silencieuse est le mode d'échec classique de l'apprentissage automatique : le code s'exécute toujours, le modèle retourne toujours des scores confiants, et la qualité glisse à mesure que le monde dérive des données d'entraînement. Pour une grande équipe exploitant de nombreux modèles, vous avez besoin que cela soit répondu par modèle, pas une fois pour la flotte, parce que chacun a son propre profil de dérive et son propre délai de vérité terrain. Apportez vos moniteurs actuels pour la dérive de données, la dérive de concept, et les ruptures de qualité de données, les seuils d'alerte, et le livre d'exécution qui dit qui répond. Dans les contextes régulés où les étiquettes arrivent des semaines en retard, discutez des signaux de proxy que vous pouvez surveiller dans l'intervalle, parce qu'attendre la vérité terrain retardée signifie attendre pour découvrir le dommage. Si aucun propriétaire unique n'est nommé pour l'alerte de dérive d'un modèle, ce modèle est effectivement non surveillé.

2. **Si un auditeur nous demandait de reproduire une prédiction spécifique d'il y a dix-huit mois, pourrions-nous réellement le faire de bout en bout ?** La reproductibilité est l'exigence de conformité cachée dans la bonne ingénierie : elle permet à une agence de répondre exactement quel modèle, entraîné sur quelles données, avec quel code, a produit une décision qui a affecté quelqu'un. Apportez un vrai exemple et essayez de le tracer : l'instantané de données immuable, le commit git, les dépendances verrouillées et l'image de conteneur, les graines enregistrées, et la lignée des données brutes à travers les caractéristiques jusqu'au modèle déployé. Le signal est si un maillon quelconque de cette chaîne manque ou est manuel. Pour l'administration publique et les industries régulées, décidez la période de rétention que la loi exige réellement et confirmez que votre stockage garde la lignée répondable pour toute cette fenêtre, puisqu'un écart transforme une requête routinière en urgence forensique.

3. **Quelle est notre règle pour promouvoir un modèle en production et revenir en arrière, et est-elle imposée par le registre ou seulement par confiance ?** La promotion non gouvernée est comment les expériences de carnet fuient en production et comment un mauvais modèle persiste parce que personne ne peut le revenir en arrière proprement. Pour de nombreuses équipes, la différence entre mature et fragile est si le registre de modèle conditionne la promotion avec une approbation et évaluation obligatoires, ou si un ingénieur peut pousser des poids à la main. Apportez votre chemin de promotion actuel, votre mécanisme de retour en arrière, et une preuve que les déploiements fantômes ou canaris s'exécutent réellement avant le trafic complet. Discutez si le réentraînement est planifié ou déclenché par dérive, et si les modèles réentraînés passent des portes de validation avant déploiement, parce que le réentraînement sur des données en direct sans validation amplifie la dérive ou l'empoisonnement. La réponse devrait être imposée dans la plateforme, pas dans une page wiki que les gens sont censés suivre.

4. **Construisons-nous notre plateforme MLOps sur des outils open source, en achetons-nous une gérée, ou mélangeons-nous les deux, et qui a pesé le verrouillage ?** Ce choix fixe le plafond de la vitesse à laquelle tout futur modèle est livré et combien de contrôle vous gardez sur vos données et pipelines. Une plateforme gérée amène les équipes rapidement en production et porte du support, mais elle peut piéger vos définitions de caractéristiques, enregistrements de lignée, et artefacts de modèle dans un format propriétaire que vous ne pouvez pas facilement quitter ; une pile open source assemblée vous garde portable au prix d'un vrai travail d'intégration et maintenance. Apportez le coût total de possession pour chaque chemin (licence ou construction, stockage, calcul pour réentraînement, et le personnel de plateforme pour l'exploiter), une lecture honnête de la capacité de votre équipe à exploiter l'infrastructure, et un vrai test de sortie : pourriez-vous exporter votre registre, magasin de caractéristiques, et lignée et reconstruire ailleurs ? Dans les contextes d'entreprise et gouvernementaux, ajoutez les contraintes d'approvisionnement et les règles de souveraineté des données, puisqu'une plateforme qui stocke les données d'entraînement dans une région ou format que votre régulateur interdit est disqualifiée peu importe sa commodité.

5. **Notre magasin de caractéristiques et registre de modèle devraient-ils être une plateforme centralisée unique ou fédérés par équipe, et combien nous coûte le biais entraînement-service aujourd'hui ?** Centraliser les définitions de caractéristiques élimine le biais où une caractéristique est calculée d'une façon en entraînement et d'une autre en service, ce qui est une source silencieuse et coûteuse de perte de précision, mais une seule plateforme peut devenir un goulot d'étranglement qui ralentit chaque équipe. Fédérer donne aux équipes de l'autonomie tout en multipliant la plomberie et les chances que deux équipes définissent la même caractéristique de façon incohérente. Apportez une preuve d'où le biais vous a déjà mordu, combien d'équipes réutilisent des caractéristiques contre les reconstruisent, et les valeurs par défaut de chemin pavé qu'une équipe de plateforme partagée pourrait offrir. Pour une grande organisation, pesez le bénéfice de gouvernance d'un système d'enregistrement auditable unique contre le coût de livraison d'une file centrale, et dans les contextes régulés favorisez la lignée centralisée qui permet à un auditeur de tracer toute prédiction au code de caractéristique exact qui l'a produite.

6. **Avons-nous assorti le motif de déploiement de chaque modèle à ses vrais besoins de latence, fraîcheur, et souveraineté, ou tout mettons-nous par défaut à une seule forme ?** Le par lots, en ligne, streaming, et bord portent chacun un coût et une complexité opérationnels très différents, et choisir le mauvais soit surdépense sur de l'infrastructure temps réel qu'un rapport nocturne n'a jamais eu besoin soit affame un scoreur de fraude de la fraîcheur dont il dépend. Décidez par charge de travail quel motif l'exigence justifie réellement, et résistez à standardiser sur l'option la plus complexe parce qu'elle se sent moderne. Apportez le budget de latence, le volume, le coût d'une réponse périmée, et le délai de vérité terrain pour chaque modèle. Dans les contextes gouvernementaux et de terrain, pesez le déploiement en bord et sur site délibérément, parce que les règles de souveraineté de données ou la connectivité intermittente peuvent forcer les modèles sur du matériel local, et ce choix remodèle comment vous versionnez, surveillez, et revenez en arrière sur chaque modèle que vous y poussez.

## Regard sectoriel

**Jeune pousse.** Votre ressource la plus rare est l'attention d'ingénierie, donc gardez le MLOps léger et achetez-le. Suivez les expériences dans un outil hébergé simple, épinglez chaque modèle déployé à son instantané de données d'entraînement et commit de code dans git, et ajoutez un contrôle de dérive bon marché plutôt qu'une plateforme. Sautez le magasin de caractéristiques et les pipelines sur mesure jusqu'à ce qu'un deuxième ou troisième modèle rende la réutilisation valable ; une pile fragile que vous ne pouvez pas maintenir vous coulera plus vite qu'une capacité manquante.

**Petite entreprise.** Vous n'avez probablement pas de spécialiste de plateforme ML et avez un budget serré, donc traitez le MLOps comme quelque chose intégré dans les outils que vous exécutez déjà plutôt qu'un système que vous dotez. Préférez un service géré qui gère le versionnage, le déploiement, et la surveillance pour vous, et cadrez la discipline comme une question d'hygiène de données et de reproductibilité : sachez quel modèle et données ont produit un résultat donné, et gardez la capacité de revenir en arrière. Favorisez les fournisseurs qui vous laissent exporter vos données et modèles pour qu'un changement ultérieur reste possible.

**Grande entreprise.** Le problème est l'échelle à travers des dizaines de modèles et de nombreuses équipes : un magasin de caractéristiques partagé, du suivi d'expérience, et un registre de modèle avec une promotion gouvernée pour que les groupes arrêtent de réinventer des pipelines. Budgétisez une équipe de plateforme qui offre des valeurs par défaut de chemin pavé, standardisez la lignée et surveillance pour que chaque modèle soit auditable et chaque incident explicable, et gérez construire-contre-acheter et le verrouillage délibérément derrière une interface qui garde les outils sous-jacents interchangeables. Imposez les portes de validation et retour en arrière dans la plateforme, pas dans la convention.

**Gouvernement.** La reproductibilité, la lignée, et le versionnage sont des exigences de conformité déguisées, donc traitez-les comme de première classe dès le premier jour. Versionnez le jeu de données et code exacts derrière chaque modèle déployé, retenez cette lignée pour la période légalement requise, et soyez capable de reproduire toute prédiction historique qui a affecté un citoyen. Gardez un humain révisant les décisions conséquentes, pesez le déploiement en bord et sur site où les règles de souveraineté de données l'exigent, et exigez que toute plateforme de fournisseur accorde la portabilité complète de vos données, caractéristiques, et lignée.

## Exemples

**Jeune pousse.** Une petite jeune pousse analytique a livré son premier modèle de prédiction de désabonnement avec un data scientist et une configuration légère. Elle a suivi les expériences dans un outil hébergé simple, épinglé chaque modèle déployé à son instantané de données d'entraînement et commit de code dans git, et ajouté une tâche hebdomadaire de base qui comparait les entrées récentes contre la distribution d'entraînement. Quand une source de données a changé son format de date et que les prédictions ont commencé à dériver, ce contrôle simple l'a attrapé en jours plutôt qu'après un appel client en colère, et l'équipe a pu reproduire le dernier bon modèle et revenir en arrière.

**Grande entreprise.** Une banque de détail exploite des dizaines de modèles de crédit et de fraude. Elle a standardisé sur un magasin de caractéristiques partagé à travers les équipes, un service de suivi d'expérience, et un registre de modèle avec des portes d'approbation obligatoires. Chaque modèle en production se retrace à son instantané de données d'entraînement et commit de code. Les modèles de fraude se déploient comme scoreurs de streaming ; les modèles de crédit s'exécutent par lots. Une couche de surveillance observe la dérive d'entrée et alerte quand un schéma de source de données change, ce qui a une fois attrapé un flux amont cassé avant qu'il ne corrompe les décisions.

**Gouvernement.** Une agence de prestations publiques utilise un modèle d'apprentissage automatique pour prioriser les révisions de dossier. Parce que ces décisions affectent l'accès des citoyens aux services, l'agence versionne le jeu de données et code exacts derrière chaque modèle déployé, garde cette lignée pour la période légalement requise, et peut reproduire toute prédiction historique sur demande. Les modèles se déploient par lots avec un humain révisant les cas signalés, et un moniteur de dérive force une réévaluation obligatoire chaque fois que la population entrante bascule, pour que le modèle ne soit jamais discrètement appliqué en dehors des conditions pour lesquelles il a été validé.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le MLOps se rembourse en transformant des expériences fragiles en actifs fiables. Le retour sur investissement vient d'un délai de mise en production plus rapide pour les nouveaux modèles, moins d'incidents coûteux, moins d'infrastructure dupliquée, et la capacité d'exploiter de nombreux modèles avec une petite équipe de plateforme. Un magasin de caractéristiques et registre partagés peuvent réduire dramatiquement le temps de livraison par modèle, parce que les équipes arrêtent de reconstruire la même plomberie.

Le coût total de possession couvre la construction ou licence de plateforme, le stockage pour les données et modèles versionnés, le calcul pour réentraînement, et le personnel pour tout exploiter. Pesez cela contre le coût de ne pas adopter : des modèles que vous ne pouvez pas reproduire ou auditer, des échecs silencieux qui lèsent des clients ou citoyens, et des découvertes réglementaires. Dans les contextes régulés, le coût d'un modèle inexplicable dans un audit peut éclipser tout l'investissement MLOps. Faites valoir cela auprès de la direction en cadrant le MLOps comme une réduction de risque et accélération de livraison, pas de la surcharge : un chemin pavé que tout futur modèle voyagera.

## Anti-patterns et pièges

- **Sauts de carnet à production.** Déployer des modèles entraînés dans des carnets non gouvernés sans reproductibilité.
- **Biais entraînement-service.** Un code de caractéristique différent en entraînement et en service, causant une perte de précision silencieuse.
- **Aucun versionnage de données.** Versionner le code mais pas les données, pour que les exécutions ne puissent pas être reproduites.
- **Déployer et oublier.** Livrer un modèle sans surveillance, découvrant la dégradation seulement quand les utilisateurs se plaignent.
- **Réentraînement en pilote automatique.** Réentraîner automatiquement sur des données en direct sans validation, amplifiant la dérive ou l'empoisonnement.
- **Infrastructure ponctuelle.** Chaque équipe construisant son propre pipeline, multipliant le coût et la fragilité.
- **Ignorer les étiquettes retardées.** Supposer que vous pouvez mesurer la précision instantanément quand la vérité terrain arrive des semaines plus tard.

## Modèle de maturité

1. **Initier.** Modèles construits au coup par coup dans des carnets ; déploiement manuel ; aucun versionnage de données ou modèles ; aucune surveillance ; reproduire une prédiction passée est une supposition.
2. **Développer.** Un certain suivi d'expérience et un registre de modèle apparaissent, mais les pratiques varient par équipe ; le déploiement est semi-automatisé ; la surveillance de base couvre quelques modèles ; le versionnage de données est partiel et la lignée a des lacunes.
3. **Standardiser.** Une plateforme partagée avec un magasin de caractéristiques, un registre, des pipelines reproductibles, et une lignée de bout en bout est documentée et imposée à l'échelle de l'organisation ; la surveillance de la dérive et qualité de données s'exécute à travers les modèles ; la promotion et retour en arrière suivent un chemin gouverné que chaque équipe utilise.
4. **Gérer.** La flotte est mesurée contre des références : taux de dérive, ruptures de qualité de données, précision de modèle contre vérité terrain retardée, biais entraînement-service, temps de mise en production, et coût d'exploitation par modèle sont suivis comme métriques ; les seuils d'alerte et portes de validation sont imposés sur preuve, et la santé de chaque modèle est révisée selon une cadence fixe avec un propriétaire nommé.
5. **Orchestrer.** Le cycle de vie est entièrement automatisé, auditable, et adaptatif ; le réentraînement déclenché par dérive s'exécute derrière des portes de validation ; des chemins pavés en libre-service laissent les équipes livrer en sécurité ; l'évaluation continue lie la performance de modèle aux métriques d'affaires, et la plateforme s'intègre avec la livraison, le risque, et la conformité pour que les modèles soient routinièrement retirés, remplacés, et recadrés à mesure que les données et conditions changent.

## Pistes de réflexion

- Comment équilibrez-vous la liberté d'expérimentation avec la reproductibilité de production ?
- Quel est le bon déclencheur de réentraînement (calendrier, dérive, ou décroissance de performance) pour vos cas d'usage ?
- Combien de temps devez-vous retenir les données et la lignée de modèle, et qu'est-ce qui pilote cette exigence ?
- Les magasins de caractéristiques et registres devraient-ils être des plateformes centralisées ou fédérées par équipe ?
- Comment surveillez-vous la précision quand les étiquettes de vérité terrain arrivent avec de longs délais ?
- Quand le déploiement en bord vaut-il sa complexité opérationnelle ajoutée ?

## Points clés à retenir

- Le comportement d'apprentissage automatique vient du code plus des données plus des modèles ; versionnez et gouvernez les trois ensemble.
- Les magasins de caractéristiques, le suivi d'expérience, et les registres sont l'épine dorsale de l'apprentissage automatique reproductible.
- La lignée rend les modèles auditables et les incidents explicables : essentiel dans les contextes régulés.
- Choisissez par lots, en ligne, streaming, ou bord pour assortir les besoins de latence, fraîcheur, et souveraineté.
- Les modèles se dégradent ; la surveillance de la dérive, qualité de données, et décroissance n'est pas optionnelle.

## Références et lectures complémentaires

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, et Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
