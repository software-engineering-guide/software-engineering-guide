# 11.1 Le pipeline de découverte

## Vue d'ensemble et motivation

Le pipeline de découverte est le flux de travail qui décide **quoi construire et pourquoi**, et définit **à quoi le succès ressemblera**, avant et aux côtés de la livraison. Là où le pipeline de livraison (chapitre 11.2) transforme des idées validées en logiciel fonctionnel, le pipeline de découverte transforme les problèmes, preuves, et stratégie en un ensemble priorisé et testable de résultats visés. Dans la pratique moderne, les deux fonctionnent continuellement et en parallèle, souvent appelés développement *double piste*, plutôt que comme des phases séquentielles. La découverte continue d'alimenter la livraison avec un approvisionnement prêt de travail dérisqué et bien cadré, et la livraison continue d'alimenter la découverte avec des données de résultat du monde réel.

Pour les grandes équipes, un pipeline de découverte faible est le mode d'échec le plus coûteux en logiciel. Une équipe avec une excellente livraison et une découverte faible construit efficacement la mauvaise chose : elle livre rapidement, atteint ses cibles de vélocité, et ne bouge toujours aucune métrique d'affaires. Le coût est invisible sur les tableaux de bord d'ingénierie et énorme sur le bilan. Le pipeline de découverte est comment vous rendez ce coût visible : il force les objectifs à être explicites, mesurables, et falsifiables avant d'engager de gros investissements.

Les contextes d'entreprise et gouvernementaux élèvent les enjeux. Les entreprises coordonnent des dizaines d'équipes contre une stratégie partagée, donc des objectifs locaux mal alignés se composent en portefeuilles gaspillés. Les programmes gouvernementaux engagent un financement public pluriannuel contre des mandats législatifs, où « nous avons construit ce que le contrat disait » n'est pas une défense si le résultat (citoyens servis, temps d'attente réduits, fraude prévenue) ne se matérialise jamais. Un pipeline de découverte discipliné, exprimé à travers des objectifs, mesures, et exigences de qualité explicites, est comment les deux gardent leur intention auditable.

## Principes clés

- **Les résultats plutôt que les sorties.** Mesurez le changement que vous créez pour les utilisateurs et l'affaire, pas les fonctionnalités que vous livrez.
- **Rendez l'intention explicite et mesurable.** Un objectif que vous ne pouvez pas mesurer est une opinion que vous ne pouvez pas gérer.
- **Dérisquez avant de construire.** L'expérience la moins chère bat l'opinion la plus confiante.
- **La découverte et la livraison fonctionnent continuellement en parallèle**, pas comme des portes séquentielles.
- **Les attributs de qualité sont des exigences, pas des réflexions après coup.** La fiabilité, la sécurité, et l'accessibilité sont découvertes et spécifiées, pas espérées.
- **L'alignement bat l'optimisation locale.** Des objectifs imbriqués connectent le travail d'équipe à la stratégie.
- **Fermez la boucle.** Les résultats livrés sont des preuves qui rentrent dans la découverte.

## Recommandations

### Cadrer la direction avec les OKR

Utilisez les **[objectifs et résultats clés](https://fr.wikipedia.org/wiki/Objectives_and_key_results) (OKR)** pour connecter la stratégie à l'exécution d'équipe. Un *objectif* est une déclaration qualitative et inspirante d'un état final désiré (« rendre l'intégration de première fois sans effort »). Les *résultats clés* sont le petit nombre (typiquement 2 à 4) de résultats mesurables qui prouvent que l'objectif est atteint (« augmenter l'activation à 7 jours de 40 % à 60 % » ; « réduire les tickets de support d'intégration de 30 % »). Les résultats clés expriment des **résultats**, pas des tâches : « livrer le nouvel assistant » est une tâche déguisée en résultat.

Cascadez les OKR par *alignement*, pas par dictée : la direction fixe un petit nombre d'objectifs d'entreprise ; les équipes proposent des résultats clés et leurs propres objectifs qui remontent vers eux. Fixez-les selon une cadence régulière (communément trimestrielle avec un cadre annuel), révisez-les à mi-cycle, et notez-les honnêtement à la fin. Gardez-les séparés des revues de performance : les OKR notés pour la compensation deviennent rapidement sous-estimés. Voir le chapitre 10.1 pour comment les OKR se connectent à la gestion de portefeuille et de programme.

### Surveiller la santé avec les KPI

Distinguez les **[indicateurs clés de performance](https://fr.wikipedia.org/wiki/Indicateur_de_performance) (KPI)** des OKR. Les OKR décrivent le *changement* que vous voulez cette période ; les KPI décrivent la *santé continue* que vous devez soutenir indépendamment de ce que vous changez (disponibilité, taux de conversion, coût par transaction, satisfaction client). Une métrique peut être les deux (un KPI que vous essayez activement de bouger devient un résultat clé), mais la plupart des KPI sont des garde-fous que vous surveillez, pas des cibles vers lesquelles vous sprintez.

Classifiez chaque métrique importante comme **avancée** (prédictive et actionnable maintenant, comme les inscriptions d'essai) ou **retardée** (confirmatoire et lente, comme le revenu annuel). La découverte s'appuie sur les indicateurs avancés pour piloter avant que les indicateurs retardés ne confirment. Méfiez-vous des métriques de vanité qui montent fiablement mais ne prédisent rien (pages vues brutes, total d'utilisateurs enregistrés) ; préférez les métriques de ratio et de cohorte qui résistent à la manipulation. Voir les chapitres 7.3 et 7.4 pour la machinerie analytique et d'expérimentation derrière ces mesures.

### Spécifier les attributs de qualité système explicitement

Les exigences fonctionnelles disent ce que le système fait. Les **attributs de qualité système** (les « -ilités » : fiabilité, performance, évolutivité, sécurité, accessibilité, maintenabilité, exploitabilité) disent à quel point il doit bien le faire. Ceux-ci sont routinièrement sous-découverts : tout le monde les suppose, personne ne les spécifie, et ils font surface comme des incidents de production. Traitez-les comme une sortie de découverte de premier ordre. Identifiez les **exigences architecturalement significatives** (les demandes de qualité qui façonnent matériellement l'architecture) pour chaque initiative. Quantifiez-les (« latence p99 sous 200 ms à 10× la charge actuelle » ; « WCAG (Web Content Accessibility Guidelines) 2.2 AA » ; « objectif de temps de récupération de 15 minutes »). Et là où vous le pouvez, encodez-les comme des **fonctions de fitness** automatisées (vérifications exécutables qui vérifient continuellement un attribut de qualité) que le pipeline de livraison peut vérifier. C'est le complément côté découverte du chapitre 3.1 (fondamentaux d'architecture) et du chapitre 3.5 (évolutivité, performance, résilience).

### Rendre chaque objectif SMART

Que vous écriviez un résultat clé, un critère d'acceptation, ou une cible de qualité, appliquez le test **[SMART](https://fr.wikipedia.org/wiki/Objectif_SMART)** :

- **Spécifique :** nomme un résultat clair et non ambigu.
- **Mesurable :** a une métrique et une source de vérité.
- **Atteignable :** est réaliste compte tenu des contraintes et preuves.
- **Pertinent :** remonte vers un objectif plus élevé et vers la valeur utilisateur.
- **Temporellement borné :** a une échéance ou date de révision.

« Améliorer la performance » échoue à chaque lettre. « Réduire le temps médian de paiement de 8s à 3s pour les utilisateurs mobiles d'ici la fin du T3, mesuré par la surveillance d'utilisateur réel » réussit les cinq. Les critères SMART convertissent l'ambition vague en une affirmation falsifiable que la découverte peut tester et que la livraison peut vérifier.

### Exécuter une découverte continue et pilotée par preuves

Structurez la découverte comme un pipeline reproductible, pas une phase ponctuelle :

1. **Sentir.** Rassemblez les signaux : recherche utilisateur, données de support, analytique, entrées de marché et de conformité.
2. **Cadrer.** Cartographiez les opportunités (un *arbre opportunité-solution* connecte un résultat désiré aux besoins utilisateur et solutions candidates qui pourraient le bouger).
3. **Hypothétiser.** Énoncez les hypothèses comme des affirmations falsifiables : « Nous croyons que [changement] causera [résultat] pour [segment], et nous saurons si [mesure] bouge. »
4. **Expérimenter.** Validez les hypothèses les plus risquées avec le test le moins cher : entretiens, prototypes, tests de fausse porte (annoncer une fonctionnalité pas encore construite pour mesurer la vraie demande), **[expériences A/B](https://fr.wikipedia.org/wiki/Test_A/B)** (comparaisons randomisées de deux variantes, chapitre 7.4).
5. **Décider.** Persévérer, pivoter, ou abandonner, et alimenter les survivants dans le carnet de livraison avec leurs critères de succès SMART attachés.

La sortie du pipeline de découverte n'est pas une liste de fonctionnalités ; c'est un flux de *paris validés et mesurables* prêts pour la livraison.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| **Objectifs basés sur les résultats (OKR)** | Aligne les équipes sur l'impact ; habilite l'autonomie dans le *comment* | Difficile à bien écrire ; tentant de remplir avec des tâches ; attribution bruyante |
| **Feuilles de route de sortie/fonctionnalité** | Prévisible, facile à communiquer et contracter | Récompense la livraison plutôt que l'impact ; cache le risque de mauvaise chose |
| **Découverte lourde à l'avance** | Réduit le gaspillage de construction ; exigences solides | Ralentit le démarrage ; risque de paralysie d'analyse ; hypothèses encore non testées |
| **Découverte continue à double piste** | Dérisque continuellement ; rétroaction rapide | Exige capacité de recherche et discipline ; plus difficile à planifier |
| **Attributs de qualité explicites comme cibles SMART** | Empêche les surprises « -ilité » ; auditable | Effort à quantifier ; peut sur-contraindre l'exploration précoce |

La tension centrale est **engagement contre apprentissage**. Les entreprises, et spécialement les gouvernements, ont souvent besoin d'engagements fermes pour la budgétisation et les contrats, ce qui tire vers les feuilles de route de sortie. Les bons résultats ont besoin d'espace pour apprendre, ce qui tire vers les OKR et expériences. Résolvez-le ainsi : engagez-vous fermement envers les *problèmes et résultats*, et tenez les *solutions* lâchement.

## Questions à discuter avec votre équipe

1. **Qui dans votre équipe possède réellement la découverte, et a-t-il la capacité de l'exécuter continuellement plutôt que dans un sprint ponctuel ?** Le développement à double piste ne fonctionne que quand quelqu'un tient la piste de découverte ouverte chaque semaine plutôt que seulement au début d'un trimestre. Dans une grande organisation, la découverte n'a souvent pas de propriétaire dédié, donc elle s'effondre vers quiconque a du temps libre, ce qui n'est personne, et l'équipe fait défaut vers la construction. Apportez des preuves : comptez combien de vos dix dernières fonctionnalités sont passées par une hypothèse documentée et un test bon marché avant la construction, contre directement dans le carnet. Dans les contextes d'entreprise et gouvernementaux, où une initiative mal alignée peut gaspiller de multiples trimestres-équipe, nommez un propriétaire de produit ou un trio (produit, conception, ingénierie) responsable de la boucle sentir-cadrer-hypothétiser-expérimenter-décider. Si personne ne la possède, dotez-la avant de vous disputer sur quoi que ce soit d'autre.

2. **Lesquelles de vos initiatives actuelles ont des exigences architecturalement significatives que vous n'avez jamais quantifiées, et pourriez-vous en encoder certaines comme fonctions de fitness ?** Les « -ilités » (fiabilité, performance, sécurité, accessibilité) sont supposées puis font surface comme des incidents de production. Parcourez chaque initiative active, demandez quels attributs de qualité façonnent matériellement l'architecture, et vérifiez si chacun a un chiffre et une source de vérité : « p99 sous 200 ms à 10x la charge », « WCAG 2.2 AA », « objectif de temps de récupération de 15 minutes ». Pour l'entreprise et le gouvernement, des exigences d'accessibilité ou de sécurité non quantifiées créent une exposition légale et d'audit directe. Le signal à apporter est vos trois derniers incidents : combien remontaient à un attribut de qualité que personne n'a spécifié ? Là où vous pouvez transformer une cible en fonction de fitness automatisée que le pipeline de livraison vérifie, faites-le, parce qu'une cible spécifiée mais non appliquée dérive.

3. **Quand vous vous êtes engagé pour la dernière fois envers une solution, avez-vous testé l'hypothèse la plus risquée en premier, ou la plus facile ?** Les équipes valident fiablement l'hypothèse avec laquelle elles sont le plus à l'aise et sautent celle qui tuerait réellement l'idée. Pour chaque initiative, listez ses hypothèses (désirabilité, viabilité, faisabilité) et classez-les par « à quel point cette idée est-elle morte si nous avons tort ici », puis visez le test le moins cher sur le haut de cette liste. Cela compte à l'échelle parce qu'une équipe senior confiante peut engager un trimestre d'ingénierie sur une croyance non testée, et le coût reste invisible jusqu'au lancement. Apportez l'artefact : votre dernière hypothèse énoncée comme « Nous croyons que [changement] cause [résultat] pour [segment], mesuré par [métrique] », et demandez si vous l'avez testée ou juste construite. Si vous ne pouvez pas nommer l'hypothèse la plus risquée, vous n'êtes pas prêt à engager la capacité de construction.

4. **Combien de vos résultats clés sont de véritables résultats, et combien sont des tâches ou dates de livraison déguisées en résultats ?** L'échec le plus commun dans la planification basée sur les résultats est de remplir les résultats clés avec le travail que vous aviez déjà prévu de faire (« lancer le nouvel assistant ») au lieu du changement que ce travail est censé causer (« élever l'activation à 7 jours de 40 % à 60 % »). À l'échelle, cela défait silencieusement tout le but : des dizaines d'équipes rapportent vert tandis qu'aucune métrique d'affaires ne bouge, parce que tout le monde s'est noté sur la livraison. La traction concurrente est réelle, les feuilles de route de sortie sont plus faciles à communiquer, contracter, et prévoir, ce qui est exactement pourquoi elles reviennent en douce. Apportez votre ensemble d'OKR actuel et marquez chaque résultat clé comme résultat ou sortie, puis vérifiez si la notation OKR est entremêlée avec la compensation, puisque les résultats liés à la paie sont rapidement sous-estimés. Pour les portefeuilles d'entreprise et gouvernementaux, où le financement est engagé contre des objectifs énoncés, une feuille de route de sorties sans mesure de résultat est un constat d'audit en attente de se produire ; insistez pour que chaque initiative s'engage fermement envers un problème et un résultat mesurable tout en tenant la solution lâchement.

5. **Lesquels de vos KPI continueraient de grimper même si le produit empirait, et quels garde-fous protègent les métriques que vous essayez activement de bouger ?** Chaque métrique que vous élevez en cible invite la **[loi de Goodhart](https://fr.wikipedia.org/wiki/Loi_de_Goodhart)** : une fois qu'une mesure devient le but, les gens optimisent la mesure plutôt que la chose qu'elle était censée représenter. Les métriques de vanité (pages vues brutes, utilisateurs enregistrés cumulatifs) montent fiablement et ne prédisent rien, tandis qu'un seul résultat clé poursuivi sans garde-fous peut être atteint en dégradant quelque chose que vous n'avez jamais nommé. La tension est que les indicateurs avancés vous laissent piloter tôt mais sont bruyants et manipulables, tandis que les indicateurs retardés sont dignes de confiance mais confirment trop tard pour agir. Apportez votre inventaire de métriques classifié comme avancé ou retardé et comme cible ou garde-fou, et testez sous stress chaque cible en demandant « comment une équipe astucieuse pourrait-elle atteindre ce chiffre tout en rendant le produit pire ». Dans les contextes régulés et publics, publiez les garde-fous aux côtés des cibles, parce qu'un organe de surveillance qui ne voit que la métrique vedette ne peut pas distinguer la vraie valeur publique d'un chiffre manipulé.

6. **Quand la livraison expédie quelque chose, comment le résultat du monde réel rentre-t-il réellement dans la découverte, ou la boucle reste-t-elle ouverte ?** Le développement à double piste ne se compose que si les résultats livrés reviennent comme preuve pour le prochain tour ; quand la boucle reste ouverte, les équipes livrent, célèbrent, et n'apprennent jamais si le pari a payé, donc les mêmes hypothèses non testées se répètent. Dans une grande organisation, le chemin de rétroaction est où la responsabilité est le plus susceptible de tomber dans un trou : la livraison possède la publication, l'analytique possède le tableau de bord, et personne ne possède la comparaison du résultat clé promis au résultat observé. Apportez vos dix dernières initiatives livrées et demandez, pour chacune, si quelqu'un a vérifié la métrique de résultat contre la cible SMART originale et si cette vérification a changé une décision suivante. Pour les programmes d'entreprise et gouvernementaux engageant un financement pluriannuel, nommez la cadence et le propriétaire pour retirer ou redéfinir la portée des fonctionnalités qui n'ont pas réussi à bouger leur métrique, parce qu'une fonctionnalité livrée que personne ne revisite devient un coût permanent sans révision responsable.

## Regard sectoriel

**Jeune pousse.** Avec une minuscule équipe et peu de marge de manœuvre, votre pipeline de découverte est délibérément léger mais jamais sauté : un jour d'entretiens client et un test de fausse porte coûtent presque rien contre les semaines qu'une mauvaise construction brûle. Choisissez un indicateur avancé qui se substitue à votre valeur centrale, énoncez chaque pari comme une seule hypothèse falsifiable, et tuez les idées avant d'écrire du code plutôt qu'après. Les OKR formels sont excessifs à cinq personnes ; un résultat mesurable honnête par cycle suffit pour empêcher la vitesse de devenir du mouvement sans progrès.

**Petite entreprise.** Vous n'avez probablement pas de chercheur dédié ou d'analyste produit, donc traitez la découverte comme une habitude, pas un rôle : quelques conversations structurées avec de vrais clients et une métrique simple que vous collectez déjà. La question construire-contre-acheter domine, parce que la plupart des attributs de qualité (fiabilité, sécurité, accessibilité) sont moins chers à obtenir d'un fournisseur réputé qu'à spécifier et appliquer vous-même. Écrivez une ou deux cibles SMART pour pouvoir dire si un outil acheté ou une petite construction a réellement bougé le résultat, et évitez d'engager un budget rare pour des fonctionnalités que personne n'a validé que quelqu'un veuille.

**Grande entreprise.** L'échelle transforme la découverte en problème de coordination à travers des dizaines d'équipes : sans une cadence OKR partagée et une définition commune de « résultat », les objectifs locaux dérivent et se dupliquent, et des paris mal alignés se composent en portefeuilles gaspillés. Standardisez comment les exigences architecturalement significatives sont quantifiées et encodez-les comme fonctions de fitness pour que les attributs de qualité soient gouvernés, pas supposés. Gérez la découverte comme un portefeuille avec des critères d'arrêt explicites et une boucle qui réinjecte les métriques de résultat livrées vers le cycle suivant, pour que la direction pilote sur l'impact plutôt que sur un carnet de fonctionnalités.

**Gouvernement.** Les marchés publics et le financement pluriannuel exigent des engagements fermes, ce qui tire fort vers les contrats de sortie, pourtant la valeur publique vit dans les résultats : citoyens servis, temps d'attente coupés, fardeau réduit. Cadrez les programmes autour de résultats publics mesurables et d'attributs de qualité non négociables (accessibilité WCAG, langage clair, sécurité), et faites de la preuve de découverte, incluant le test d'utilisabilité avec des utilisateurs de technologie d'assistance, une partie du registre que les organes de surveillance peuvent auditer. Définissez le succès comme des résultats de contribuable ou citoyen plutôt que des modules livrés, pour que « nous avons construit ce que le contrat disait » ne puisse jamais se substituer à un résultat qui ne s'est jamais matérialisé.

## Exemples

**Jeune pousse.** Une équipe en phase d'amorçage de quatre personnes construisant une application de planification pour salons de coiffure est tentée de construire un widget de réservation en ligne parce que quelques utilisateurs bruyants l'ont demandé. Au lieu de cela, ils exécutent une semaine de découverte : cinq entretiens de propriétaire, un bouton « Réserver en ligne » de fausse porte sur le site marketing, et un seul indicateur avancé (pourcentage de rendez-vous qui se terminent en absence). Les entretiens et les données de clic révèlent que les absences, pas la réservation, sont la vraie douleur, donc ils écrivent un résultat clé SMART (couper les absences de 22 % à moins de 10 % pour les salons pilotes ce trimestre) et livrent d'abord une petite fonctionnalité de dépôt-et-rappel, tuant le widget de réservation avant d'en écrire une ligne.

**Grande entreprise.** Le groupe de paiements d'une banque de détail remplace une feuille de route de comptage de fonctionnalités par trois OKR trimestriels, l'un étant « rendre les paiements quotidiens instantanés » avec des résultats clés pour le temps de confirmation de virement p95, le taux de succès de première tentative, et les contacts de support liés au paiement. Les attributs de qualité système sont spécifiés à l'avance (disponibilité de 99,99 %, confirmation sous la seconde, portée PCI-DSS (Payment Card Industry Data Security Standard) minimisée) et câblés dans la livraison comme fonctions de fitness. La découverte exécute des entretiens client hebdomadaires et des tests de fausse porte avant d'engager l'ingénierie. Deux fonctionnalités candidates sont tuées en découverte pour ne pas avoir bougé les indicateurs avancés (économisant environ deux trimestres d'effort de construction), tandis qu'un correctif de latence plus petit et peu glamoureux bouge le plus le résultat clé.

**Gouvernement.** Une agence fiscale nationale modernisant le dépôt en ligne fixe un objectif de programme de « réduire le fardeau de dépôt pour les contribuables ordinaires », avec des résultats clés SMART : couper le temps médian de dépôt de 45 à 20 minutes, élever l'achèvement réussi en libre-service de 60 % à 85 %, et respecter les normes WCAG 2.2 AA et de langage clair comme attributs de qualité non négociables. Les KPI (disponibilité pendant la saison de dépôt, volume de centre d'appels) sont surveillés comme garde-fous. La découverte utilise le test d'utilisabilité modéré avec de vrais contribuables, incluant des utilisateurs de technologie d'assistance, avant chaque publication. Parce que le succès est défini comme des résultats de contribuable plutôt que des modules livrés, le programme peut montrer aux organes de surveillance une valeur publique mesurable, pas seulement de la dépense.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur un pipeline de découverte est dominé par le **gaspillage évité**. L'expérience de l'industrie, reflétée dans les programmes d'expérience contrôlée dans les grandes entreprises technologiques, trouve répétitivement qu'une grande part des fonctionnalités construites, souvent citée autour de la moitié ou plus, ne produit aucune amélioration mesurable ou nuit activement à la métrique cible. Supposez que même un quart de la capacité de construction d'une équipe va à des idées que la découverte aurait tuées bon marché. Le pipeline se rembourse alors plusieurs fois : une semaine de recherche utilisateur et un test de fausse porte coûtent presque rien contre un trimestre d'ingénierie, plus le fardeau de maintenance continu d'une fonctionnalité inutilisée.

Le cadrage du **[coût total de possession](https://fr.wikipedia.org/wiki/Co%C3%BBt_total_de_possession)** (TCO) compte parce que les fonctionnalités non validées ne sont pas gratuites après le lancement. Chaque fonctionnalité livrée porte des coûts perpétuels : maintenance, tests, surface de sécurité, support, et charge cognitive (chapitre 10.4). Tuer une mauvaise idée en découverte évite non seulement le coût de construction mais toute la queue de propriété. Les attributs de qualité explicites suivent la même logique : spécifier la fiabilité et l'accessibilité comme cibles SMART à l'avance est bien moins cher que de les rétro-adapter après une panne, une brèche, ou un procès.

Pour faire valoir le dossier auprès de la direction, déplacez la conversation de « combien livrons-nous » à « combien bougeons-nous les métriques qui comptent », et montrez quelques exemples concrets de fonctionnalités coûteuses qui n'ont rien bougé. Le coût d'adoption est modeste (capacité de recherche, une cadence OKR, et la discipline d'écrire des critères SMART), et le risque primaire de *ne pas* adopter est silencieux, non compté, et composé.

## Anti-patterns et pièges

- **Les feuilles de route de fonctionnalités déguisées en stratégie :** des listes de sortie sans résultat ou mesure énoncés.
- **Les résultats clés qui sont des tâches :** « lancer X » au lieu de « améliorer Y de Z ».
- **Le théâtre OKR :** des objectifs écrits, classés, et jamais révisés ou notés.
- **Les OKR sous-estimés ou héroïques :** des cibles fixées pour garantir 100 % (rien appris) ou un étirement fantaisiste sans plan.
- **Les attributs de qualité non spécifiés :** fiabilité, sécurité, et accessibilité supposées plutôt que quantifiées, puis découvertes en production.
- **Les métriques de vanité :** des mesures qui montent toujours et ne prédisent rien.
- **La découverte comme phase ponctuelle :** un « sprint de découverte » à l'avance, puis aucune validation continue.
- **Construire la solution avant de tester l'hypothèse :** sauter l'expérience la moins chère parce que l'équipe est confiante.
- **La fixation sur les métriques et la [loi de Goodhart](https://fr.wikipedia.org/wiki/Loi_de_Goodhart) :** une fois qu'une mesure devient la cible, elle cesse d'être une bonne mesure ; équilibrez avec des KPI de garde-fou.

## Modèle de maturité

- **Niveau 1, Initier :** Le travail est défini comme des fonctionnalités sur une feuille de route et le succès est « nous l'avons livré ». Il n'y a pas de mesures de résultat ou cibles de qualité explicites ; la découverte se produit par accident, le cas échéant, et les décisions sont pilotées par l'opinion la plus bruyante.
- **Niveau 2, Développer :** Les OKR et KPI existent pour certaines équipes mais pas d'autres ; les objectifs sont énoncés mais souvent formés en sortie ; les attributs de qualité sont nommés mais non quantifiés. Une équipe peut mener un « sprint de découverte » ponctuel, puis arrêter de valider une fois que la construction commence, donc la pratique est réelle mais incohérente à travers l'organisation.
- **Niveau 3, Standardiser :** Une cadence OKR cohérente alignée sur la stratégie, des résultats clés SMART, et des attributs de qualité spécifiés et testables sont documentés et attendus à l'échelle de l'organisation. La découverte est une activité reconnue et dotée en personnel avec des hypothèses et expériences, et les exigences architecturalement significatives sont identifiées pour chaque initiative plutôt que supposées.
- **Niveau 4, Gérer :** Le portefeuille est mesuré contre des référentiels. Les indicateurs avancés et retardés, le taux de succès de découverte, et le résultat que chaque pari livré a réellement bougé sont suivis contre sa cible SMART ; les hypothèses sont notées sur des preuves et les critères d'arrêt sont appliqués ; les fonctions de fitness rapportent la conformité d'attribut de qualité continuellement, pour que la dérive d'une cible de fiabilité, performance, ou accessibilité spécifiée soit attrapée avec des données plutôt que dans un incident.
- **Niveau 5, Orchestrer :** La découverte continue à double piste est intégrée avec le portefeuille, le risque, et la budgétisation ; les paris validés s'écoulent régulièrement vers la livraison et les métriques de résultat rebouclent automatiquement pour piloter le prochain tour. Les indicateurs avancés pilotent l'investissement, et l'organisation retire, redéfinit la portée, et rééquilibre routinièrement les initiatives sur des preuves, adaptant le pipeline lui-même à mesure que le marché et les métriques changent.

## Pistes de réflexion

1. Regardez votre feuille de route actuelle : combien d'éléments énoncent un résultat mesurable contre juste une fonctionnalité à livrer ?
2. Lesquels des résultats clés de votre équipe sont en fait des tâches déguisées, et comment les réécririez-vous ?
3. Quels attributs de qualité système votre produit dépend-il qui n'ont jamais été explicitement quantifiés ?
4. Quelle est l'expérience la moins chère qui aurait pu tuer votre dernière fonctionnalité échouée avant que vous ne la construisiez ?
5. Comment résolvez-vous la tension entre les engagements fermes que la budgétisation/les marchés publics exigent et l'apprentissage que les bons résultats requièrent ?
6. Lesquels de vos KPI continueraient de monter même si le produit empirait ?

## Points clés à retenir

- Le pipeline de découverte décide *quoi* et *pourquoi*, et définit le succès **avant** que la livraison n'engage des ressources.
- Utilisez les **OKR** pour le changement que vous voulez, les **KPI** pour la santé que vous soutenez, et classifiez les métriques comme avancées ou retardées.
- Traitez les **attributs de qualité système** comme des exigences explicites, quantifiées, et testables, pas des hypothèses.
- Rendez chaque objectif, résultat clé, et critère d'acceptation **SMART**.
- Exécutez la découverte **continuellement et en parallèle** avec la livraison ; validez les hypothèses les plus risquées à bas coût.
- Le ROI dominant est le **gaspillage évité** : à la fois le coût de construction et le TCO perpétuel des fonctionnalités inutilisées.
- Fermez la boucle : les **métriques de résultat** livrées (chapitre 11.2) sont la preuve primaire pour le prochain tour de découverte.

## Références et lectures complémentaires

- *Measure What Matters*, par John Doerr (sur les OKR).
- *Radical Focus*, par Christina Wodtke (sur les OKR en pratique).
- *Continuous Discovery Habits*, par Teresa Torres (arbres opportunité-solution, découverte à double piste).
- *Inspired* et *Empowered*, par Marty Cagan (découverte de produit et équipes de résultat).
- *Lean Analytics*, par Alistair Croll et Benjamin Yoskovitz (indicateurs avancés, métriques de vanité).
- *The Lean Startup*, par Eric Ries (construire-mesurer-apprendre, apprentissage validé).
- *Escaping the Build Trap*, par Melissa Perri (résultats plutôt que sorties).
- *Outcomes Over Output*, par Joshua Seiden.
- *Software Architecture in Practice*, par Bass, Clements, Kazman (attributs de qualité).
- Doran, G. T., « There's a S.M.A.R.T. way to write management's goals and objectives » (*Management Review*, 1981) : origine des critères SMART.
