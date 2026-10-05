# 7.3 Analytique et intelligence d'affaires

## Vue d'ensemble et motivation

L'analytique et l'intelligence d'affaires transforment des données gouvernées et conçues en compréhension et action. L'[intelligence d'affaires](https://fr.wikipedia.org/wiki/Informatique_d%C3%A9cisionnelle) (BI) signifie traditionnellement le rapport, les tableaux de bord, et les outils en libre-service qui laissent les gens voir ce qui se passe dans l'entreprise. L'analytique est la pratique plus large de poser et répondre à des questions avec des données, de descriptions simples du passé à des modèles qui recommandent quoi faire ensuite. Ensemble, elles sont comment une organisation se voit elle-même.

Pour les grandes équipes, cette couche est là où les données soit gagnent leur place soit deviennent une source de confusion. Quand des milliers d'employés peuvent construire leurs propres rapports, le risque n'est pas trop peu d'information mais trop d'information contradictoire : trois tableaux de bord montrant trois chiffres de revenu différents, chacun défendable, aucun faisant autorité. Les entreprises vivent et meurent par les chiffres dans les présentations de conseil et dépôts réglementaires. Les agences gouvernementales rapportent aux législatures, organismes de surveillance, et au public. Dans les deux, une métrique qui signifie des choses différentes pour des gens différents est un passif. Un graphique qui trompe, même innocemment, peut piloter des décisions fausses et coûteuses ou éroder la confiance publique.

L'idée clé pour dompter cela à l'échelle est la [couche sémantique](https://fr.wikipedia.org/wiki/Couche_s%C3%A9mantique) : une définition centrale et gouvernée des métriques et dimensions dont chaque outil et rapport tire, pour que « client actif » ou « revenu mensuel » soit calculé d'une façon convenue partout. Autour de cette idée se trouvent les disciplines de la visualisation honnête, la conception délibérée de tableau de bord, et la gestion de la dispersion que le libre-service produit inévitablement. Ce chapitre vous montre comment donner aux gens un accès large aux données sans renoncer à une seule version de la vérité.

## Principes clés

- Il devrait y avoir une définition gouvernée de chaque métrique importante, utilisée partout.
- Assortissez le type d'analytique à la question : décrire, diagnostiquer, prédire, ou prescrire.
- Le libre-service est puissant mais doit être gouverné pour prévenir la prolifération de métrique.
- Les graphiques doivent être honnêtes ; l'objectif est la compréhension, pas la persuasion par distorsion.
- Les tableaux de bord devraient piloter des décisions, pas simplement afficher des données.
- Certifiez le contenu de confiance pour que les consommateurs sachent sur quoi compter.
- Sélectionnez et retirez ; plus de tableaux de bord n'est pas plus de perspicacité.
- Intégrez l'analytique là où les décisions sont prises, plutôt que seulement dans un portail BI séparé.

## Recommandations

### Comprendre les quatre types d'analytique

L'analytique descriptive rapporte ce qui s'est passé. L'analytique diagnostique explique pourquoi c'est arrivé. L'[analytique prédictive](https://fr.wikipedia.org/wiki/Analytique_pr%C3%A9dictive) prévoit ce qui est susceptible d'arriver. L'[analytique prescriptive](https://fr.wikipedia.org/wiki/Analytique_prescriptive) recommande quoi en faire. La plupart des organisations sur-investissent dans les tableaux de bord descriptifs et sous-investissent dans le diagnostic et l'action. Poussez votre travail délibérément vers le haut de cette échelle. Associez chaque métrique importante à la capacité d'explorer les causes, et connectez les prédictions à des décisions et interventions concrètes. De cette façon l'analytique change le comportement plutôt que de simplement le décrire.

### Construire une couche sémantique et gouverner les métriques

Définissez les métriques et dimensions une fois, dans une couche sémantique centrale, et faites que chaque outil BI, carnet, et rapport intégré calcule depuis ces définitions. Cela tue le problème classique des chiffres divergents. Cela rend aussi la logique de métrique contrôlée en version, testable, et révisable. Gouvernez les métriques comme une API : chaque métrique certifiée a un propriétaire, une définition claire, et un journal de modification. Gardez les métriques certifiées séparées des expérimentales, pour que les consommateurs sachent ce qui fait autorité.

### Permettre le libre-service dans des garde-fous

Donnez aux analystes et utilisateurs d'affaires un accès en libre-service pour explorer les données. Les équipes BI centrales ne peuvent pas répondre à chaque question, et les goulots d'étranglement poussent simplement les gens vers des feuilles de calcul. Mais fournissez des garde-fous : des jeux de données certifiés sélectionnés, la couche sémantique pour des métriques cohérentes, des modèles, et de la formation. L'objectif est simple : faire que le chemin facile utilise des définitions gouvernées. Marquez des niveaux de contenu (certifié, soutenu par équipe, et personnel) pour que la liberté d'explorer ne se fasse pas passer pour vérité officielle.

### Concevoir les tableaux de bord pour les décisions

Commencez chaque tableau de bord depuis la décision qu'il soutient et l'audience qui la prend. Menez avec les quelques métriques qui comptent. Fournissez du contexte (cibles, tendances, comparaisons) pour que les chiffres soient interprétables, et permettez l'exploration de détail pour le diagnostic. Résistez à l'envie d'entasser chaque graphique disponible sur une page. Un tableau de bord qui répond « sommes-nous sur la bonne voie, et sinon, où dois-je regarder ? » vaut bien plus qu'un montrant cinquante métriques sur lesquelles personne n'agit.

### Pratiquer la visualisation de données honnête

Choisissez des types de graphique qui conviennent aux données : lignes pour les tendances dans le temps, barres pour les comparaisons à travers les catégories. Évitez les camemberts pour tout au-delà de quelques tranches. Commencez les axes de graphique à barres à zéro, gardez les échelles cohérentes, et évitez les axes doubles qui fabriquent de fausses corrélations. Utilisez la couleur de façon intentionnelle et accessible, pas décorative. Étiquetez clairement, et montrez l'incertitude là où elle compte. Le test est simple : un spectateur informé atteindrait-il la même conclusion que les données soutiennent, ou la conception l'a-t-elle poussé vers une différente ?

### Sélectionner le contenu et combattre la dispersion

Le libre-service sans sélection produit des milliers de tableaux de bord périmés, dupliqués, et abandonnés. Mettez en place la gestion de cycle de vie : suivez l'usage, archivez le contenu non utilisé, retirez les doublons, et recertifiez périodiquement ce qui reste. Rendez le catalogue certifié facile à trouver, pour que les gens réutilisent le contenu de confiance plutôt que de le reconstruire. Un ensemble plus petit de tableaux de bord de confiance et bien maintenus bat un cimetière tentaculaire.

### Intégrer l'analytique et le rapport opérationnel

Toute analytique n'appartient pas à un portail séparé. Intégrez les métriques et rapports pertinents directement dans les applications opérationnelles où les gens travaillent déjà, telles que le CRM (système de [gestion de la relation client](https://fr.wikipedia.org/wiki/Gestion_de_la_relation_client)), le système de gestion de dossier, ou l'outil de billetterie, pour que la perspicacité arrive au point de décision. Pour le rapport opérationnel avec des exigences strictes de latence ou formatage (factures, relevés, dépôts réglementaires), utilisez un rapport conçu sur mesure. N'étirez pas les tableaux de bord interactifs pour faire un travail auquel ils conviennent mal.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients | Meilleur ajustement |
|---|---|---|---|
| Équipe BI centralisée | Cohérente, gouvernée, contrôlée en qualité | Goulot d'étranglement, lente à répondre | Rapport régulé |
| BI en libre-service | Rapide, échelonnable, autonomise les utilisateurs | Dispersion, métriques incohérentes | Exploration large |
| Couche sémantique | Une vérité, réutilisable, gouvernée | Modélisation et maintenance en amont | Toute organisation au-delà de la petite échelle |
| Analytique intégrée | Perspicacité au point de décision | Coût d'ingénierie, plus difficile à gouverner | Flux de travail opérationnels |
| Tableaux de bord riches | Vue complète | Accablant, faible taux d'action | Rarement idéal |
| Tableaux de bord ciblés | Pilote les décisions | Exige une discipline éditoriale | La plupart des cas d'usage |

La tension centrale est l'accès contre la cohérence. Verrouiller la BI dans une équipe centrale garantit des chiffres cohérents, mais cela affame l'organisation de réponses opportunes et engendre des feuilles de calcul de l'ombre. Le libre-service complet autonomise tout le monde, mais cela multiplie les métriques contradictoires et le contenu périmé. Vous n'avez pas à choisir un côté. Combinez un large accès en libre-service avec une couche sémantique gouvernée et la certification, pour que les gens soient libres d'explorer pendant que les chiffres importants restent uniques et dignes de confiance.

## Questions à discuter avec votre équipe

1. **Avez-vous investi dans une couche sémantique, et gouvernez-vous chaque métrique certifiée comme une API avec un propriétaire, une définition, et un journal de modification ?** L'idée centrale du chapitre est une définition gouvernée unique de chaque métrique dont chaque outil, carnet, et rapport intégré calcule, ce qui tue le problème classique de trois tableaux de bord montrant trois chiffres de revenu. Pour les entreprises dont les présentations de conseil et dépôts réglementaires dépendent d'un chiffre unique, et pour les agences dont les sorties publiques doivent correspondre aux chiffres internes, une métrique divergente est un passif direct. Le compromis est réel : la couche sémantique a besoin de modélisation en amont et de maintenance continue. Apportez une preuve : comptez combien de définitions de votre métrique la plus importante existent aujourd'hui et ce qu'une réconciliation coûte actuellement en heures d'analyste. Si le compte est supérieur à un, la couche sémantique se rembourse, et gouverner les métriques avec des propriétaires et journaux de modification la garde unique dans le temps.

2. **Où se trouve la ligne entre la liberté de libre-service et la prolifération de métrique, et quels garde-fous gardent le chemin facile gouverné ?** Le chapitre argumente que vous ne devriez pas choisir entre une BI centrale verrouillée et un libre-service sans entrave : les équipes centrales deviennent des goulots d'étranglement qui poussent les gens vers des feuilles de calcul, tandis que le libre-service complet multiplie les métriques contradictoires et les tableaux de bord périmés. La résolution est un large accès par-dessus des jeux de données certifiés, la couche sémantique, des modèles, et des niveaux de contenu clairs (certifié, soutenu par équipe, personnel) pour que l'exploration ne se fasse pas passer pour vérité officielle. Apportez des signaux concrets : combien de tableaux de bord existent, combien sont réellement utilisés, et si les consommateurs peuvent distinguer le contenu de confiance des expériences. Si les gens ne peuvent pas dire, la certification et la gestion de cycle de vie (suivre l'usage, archiver le non utilisé, recertifier le reste) devraient devenir une pratique permanente, parce qu'un ensemble de confiance plus petit bat un cimetière tentaculaire.

3. **Vos graphiques sont-ils assez honnêtes pour survivre à l'examen, et qui vérifie que la conception soutient la conclusion que les données garantissent réellement ?** Le chapitre fixe un test clair : un spectateur informé atteindrait-il la même conclusion que les données soutiennent, ou la conception l'a-t-elle poussé ailleurs ? Les axes tronqués, les axes doubles qui fabriquent de fausses corrélations, et les camemberts 3D sont des pièges nommés. Pour les sorties gouvernementales vers les citoyens et pour les dépôts régulés, un graphique innocemment trompeur érode la confiance publique ou invite une découverte, donc l'honnêteté ici est une préoccupation de gouvernance, pas seulement de goût. Apportez un exemple où un graphique dans votre organisation a trompé son audience, et décidez si vous avez besoin de normes de visualisation (axes de barre basés zéro, échelles cohérentes, incertitude montrée) imposées sur le contenu publié. La réponse devrait fixer des attentes de revue pour tout ce qui quitte le bâtiment.

4. **Lesquels de vos tableaux de bord changent réellement une décision, et quel est votre critère pour retirer celui qui ne le fait pas ?** Le chapitre insiste qu'un tableau de bord devrait commencer depuis la décision qu'il soutient, pourtant la plupart des grandes organisations accumulent des tableaux de bord de vanité qui sont observés et jamais agis, confondus avec une culture pilotée par les données. Cela compte à l'échelle parce que chaque tableau de bord porte un coût caché : il doit être maintenu, ses métriques gardées cohérentes avec la couche sémantique, et sa présence dilue l'attention des rapports qui pilotent réellement l'action. L'attraction concurrente est que les gens se sentent plus en sécurité avec plus de visibilité, et aucune équipe n'aime avoir son tableau de bord archivé. Apportez la télémétrie d'usage (qui ouvre chaque tableau de bord, à quelle fréquence, et si une action en aval suit) et une liste candide des décisions que vos principaux tableaux de bord sont censés informer. Pour les entreprises cela alimente la sélection de portefeuille et le contrôle de coût de licence ; pour une agence gouvernementale, cela répond aussi aux questions de surveillance sur si la dépense de rapport produit une valeur opérationnelle mesurable plutôt que des écrans que personne ne lit.

5. **Êtes-vous sur-investis à décrire le passé quand la valeur est dans le diagnostic, la prédiction, et la prescription, et qu'est-ce qui déplacerait une métrique clé vers le haut de cette échelle ?** Le chapitre cadre quatre types d'analytique (descriptive, diagnostique, prédictive, prescriptive) et avertit que la plupart des organisations empilent des tableaux de bord descriptifs tout en sous-investissant dans le diagnostic et l'action qui changent réellement les résultats. Pour une grande équipe, rester coincé à la description signifie que les analystes passent leur temps à re-rapporter ce que tout le monde sait déjà, tandis que la question plus difficile de pourquoi c'est arrivé et quoi faire ensuite reste sans réponse. La tension est que le travail diagnostique et prédictif a besoin d'une ingénierie de données plus profonde, gouvernance de modèle, et compétence d'analyste, donc il est plus facile de financer un autre tableau de bord. Apportez la répartition actuelle de votre effort d'analytique à travers les quatre types et une métrique où explorer les causes ou prévoir changerait démontrablement une décision. Dans une entreprise cela connecte l'analytique à la marge et au risque ; dans une agence publique, le travail prédictif et prescriptif (par exemple prévoir la demande pour un service) doit aussi porter des garde-fous d'explicabilité et équité avant d'informer des décisions sur les citoyens.

6. **Où la perspicacité doit-elle arriver à l'intérieur des outils dans lesquels les gens travaillent déjà, et où devriez-vous utiliser un rapport opérationnel adapté au but plutôt qu'un tableau de bord ?** Le chapitre distingue la BI interactive de l'analytique intégrée et du rapport opérationnel conçu sur mesure tel que les factures, relevés, et dépôts réglementaires, et avertit contre étirer un tableau de bord pour faire un travail auquel il convient mal. Cela compte pour les grandes équipes parce que le personnel de première ligne quitte rarement son CRM ou système de gestion de dossier pour consulter un portail BI séparé, donc la perspicacité qui vit seulement dans un portail reste inutilisée au moment de la décision. Les considérations concurrentes sont le coût d'ingénierie et la gouvernance : intégrer les métriques dans les applications opérationnelles est plus difficile à construire et plus difficile à garder cohérent avec les définitions certifiées, tandis que le rapport pixel-parfait a besoin de latence et formatage stricts que l'outil de tableau de bord ne peut pas garantir. Apportez une carte d'où les décisions sont réellement prises et lesquelles exigent actuellement que quelqu'un change d'outil pour trouver le chiffre. Pour une entreprise cela façonne où investir l'effort d'ingénierie ; pour une agence gouvernementale, les dépôts statutaires et relevés orientés citoyen ont souvent des règles légales de formatage et rétention qui rendent le rapport conçu sur mesure obligatoire plutôt qu'optionnel.

## Regard sectoriel

**Jeune pousse.** Définissez votre poignée de métriques centrales une fois, même dans un outil léger, pour que la présentation de conseil et le tableau de bord produit ne soient jamais en désaccord. Sautez une plateforme de couche sémantique lourde : une source unique et partagée de définitions et une courte liste de tableaux de bord de confiance suffit tant que l'équipe est minuscule. La vitesse compte plus que le poli ici, donc favorisez un outil BI hébergé que vous pouvez pointer vers votre entrepôt aujourd'hui plutôt que quoi que ce soit que vous devriez construire.

**Petite entreprise.** Sans spécialiste BI dédié, appuyez-vous sur l'analytique déjà intégrée dans les outils que vous possédez, tels que votre CRM ou logiciel comptable, plutôt que de monter une plateforme séparée. Cadrez le choix comme acheter contre construire et laissez acheter gagner par défaut ; votre risque est une culture de feuille de calcul où chaque personne porte un chiffre de « revenu » différent, donc convenez des quelques définitions qui comptent et écrivez-les. Préférez les outils qui rendent les rapports certifiés faciles à partager et difficiles à forker accidentellement.

**Grande entreprise.** Le problème central est la cohérence à travers de nombreuses équipes : investissez dans une couche sémantique gouvernée, certifiez le contenu de confiance, et gérez la dispersion de tableau de bord comme un cycle de vie continu avec propriétaires, suivi d'usage, et recertification. Traitez chaque métrique certifiée comme une API avec une définition, un propriétaire, et un journal de modification, et séparez le contenu certifié de l'expérimental pour que le libre-service ne se fasse pas passer pour vérité officielle. Budgétisez explicitement l'effort de modélisation et sélection, parce qu'à l'échelle l'alternative est des analystes réconciliant des chiffres divergents indéfiniment.

**Gouvernement.** Les chiffres publiés doivent correspondre aux internes et survivre à l'examen public et législatif, donc une couche sémantique gouvernée et des normes de visualisation imposées (axes basés zéro, échelles honnêtes, incertitude montrée) sont des exigences de responsabilité, pas des gentillesses. Les règles d'approvisionnement peuvent contraindre quels outils BI vous pouvez acheter et exiger la portabilité de données, donc évitez le verrouillage dans la logique de métrique propriétaire d'un seul fournisseur. Gardez les sorties publiques certifiées séparées de l'analyse expérimentale, et donnez aux citoyens des graphiques assez honnêtes pour qu'un spectateur informé atteigne la conclusion que les données garantissent réellement.

## Exemples

**Jeune pousse.** Dans une place de marché en phase précoce, les deux fondateurs gardaient chacun une feuille de calcul de « revenu mensuel », et les chiffres ne correspondaient jamais tout à fait quand ils préparaient la présentation de conseil. Ils ont défini la métrique une fois dans une petite couche sémantique, pointé un seul outil BI dessus, et marqué une courte liste de tableaux de bord comme les fiables que tout le monde devrait utiliser. Le rapport est passé d'une réconciliation de dimanche soir à un lien qu'ils pouvaient ouvrir avec confiance.

**Grande entreprise.** Une entreprise de télécommunications souffrait de finance, marketing, et opérations rapportant chacun des comptes différents d'« abonné actif ». Elle a introduit une couche sémantique qui définit chaque métrique centrale une fois, migré les tableaux de bord pour calculer depuis elle, et certifié un ensemble sélectionné de rapports de confiance tout en archivant des milliers de périmés. Le rapport de conseil a cessé d'être un exercice de réconciliation, et l'adoption de libre-service a augmenté parce que les gens faisaient confiance aux chiffres.

**Gouvernement.** Un département de santé publique a construit des tableaux de bord certifiés qui tirent d'une couche sémantique gouvernée, pour que les comptes de cas et taux soient calculés identiquement à travers la prise de décision interne et les sorties publiques. Les normes de visualisation gardent les graphiques publiés aux citoyens honnêtes (axes basés zéro, bandes d'incertitude claires), ce qui protège la confiance publique. Les rapports intégrés font émerger des métriques locales à l'intérieur des outils de gestion de dossier que le personnel de première ligne utilise déjà.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur investissement de l'analytique et BI bien exploitées vient de décisions plus rapides et meilleures et de la réduction du gaspillage. Quand les gens font confiance à un seul ensemble de chiffres, les réunions cessent d'être des disputes sur quelle feuille de calcul est correcte et deviennent des discussions sur quoi faire. Le libre-service réduit l'arriéré sur les équipes centrales, et une couche sémantique prévient le coût récurrent de réconcilier des métriques divergentes. Des tableaux de bord honnêtes et axés décision élèvent le taux auquel la perspicacité se transforme en action.

Le coût d'adoption inclut le licensing de plateforme BI, construire et maintenir la couche sémantique, l'effort de sélection, et la formation. Pesez-le contre le coût de ne pas adopter : des analystes et cadres gaspillant des heures à réconcilier des chiffres contradictoires, des décisions prises sur des graphiques trompeurs, un empilement de tableaux de bord non maintenus, et, dans les contextes publics, une confiance érodée quand les chiffres publiés se contredisent. Auprès de la direction, l'argument est simple. Une couche sémantique gouvernée plus un libre-service sélectionné est la différence entre les données étant un actif que tout le monde fait confiance et une source perpétuelle de confusion et retravail.

## Anti-patterns et pièges

- Chaque équipe calculant les métriques clés à sa propre façon, produisant des chiffres contradictoires.
- Tableaux de bord construits pour tout afficher plutôt que soutenir une décision.
- Graphiques trompeurs (axes tronqués, axes doubles, camemberts 3D) qui déforment les conclusions.
- Traiter le libre-service comme un substitut à la gouvernance plutôt qu'un complément.
- Des milliers de tableaux de bord périmés et dupliqués sans gestion de cycle de vie.
- Tableaux de bord de vanité sur lesquels personne n'agit, confondus avec une culture pilotée par les données.
- Étirer la BI interactive pour produire des documents réglementaires pixel-parfaits.
- Aucune certification, donc les consommateurs ne peuvent pas distinguer le contenu de confiance des expériences.

## Modèle de maturité

1. **Initier.** Les rapports sont construits au coup par coup dans des feuilles de calcul, les métriques sont définies de façon incohérente, et les graphiques sont souvent trompeurs. Il n'y a pas de couche sémantique, pas de certification, et pas de sélection, donc les chiffres divergents sont la norme.
2. **Développer.** Un outil BI est en place avec quelques tableaux de bord partagés, mais les définitions de métrique divergent encore à travers les équipes. Le libre-service est incontrôlé et la dispersion commence ; quelques groupes peuvent modéliser les métriques soigneusement, mais la pratique est incohérente et rien n'est imposé à l'échelle de l'organisation.
3. **Standardiser.** Une couche sémantique définit les métriques centrales une fois, documentée et imposée à travers chaque outil et rapport. Le contenu certifié est distingué de l'expérimental, le libre-service opère dans des garde-fous, les normes de visualisation sont publiées, et la gestion de cycle de vie de contenu est une pratique permanente plutôt qu'un nettoyage occasionnel.
4. **Gérer.** Le parc d'analytique est mesuré contre des références. L'usage de tableau de bord est suivi et le contenu non utilisé est quantifié et retiré selon une cadence ; le nombre de définitions divergentes de métriques clés est surveillé vers un ; la conformité de revue de graphique, l'adoption de libre-service, et le temps de réponse sont suivis ; et le coût de réconciliation et le délai de changement de métrique sont mesurés pour que la dérive des définitions certifiées soit attrapée et corrigée sur preuve.
5. **Orchestrer.** Les métriques sont gouvernées comme des API avec propriétaires et journaux de modification, l'analytique s'étend du descriptif au prescriptif et se connecte à l'action concrète, et les rapports sont intégrés aux points de décision. L'organisation fait confiance à une version unique de la vérité partout, freine activement la dispersion, et recadre et recertifie continuellement son analytique à mesure que l'entreprise et ses questions changent.

## Pistes de réflexion

- Combien de définitions différentes de votre métrique la plus importante existent aujourd'hui ?
- Lesquels de vos tableaux de bord changent réellement une décision, et lesquels sont juste observés ?
- Où un graphique dans votre organisation a-t-il trompé son audience, innocemment ou non ?
- Êtes-vous sur-investis à décrire le passé contre diagnostiquer et agir ?
- Que ferait un niveau de certification pour le contenu à la confiance et réutilisation dans votre organisation ?
- Comment équilibrez-vous le besoin des citoyens ou régulateurs de graphiques honnêtes avec l'attraction vers des persuasifs ?

## Points clés à retenir

- Définissez chaque métrique importante une fois dans une couche sémantique gouvernée utilisée partout.
- Poussez l'analytique en haut de l'échelle du descriptif au diagnostique, prédictif, et prescriptif.
- Permettez le libre-service dans des garde-fous ; certifiez le contenu de confiance.
- Concevez les tableaux de bord autour des décisions, pas autour des données disponibles.
- Rendez chaque graphique honnête ; l'objectif est la compréhension, pas la persuasion.
- Sélectionnez sans pitié et retirez le contenu périmé pour combattre la dispersion.
- Intégrez l'analytique au point de décision, et utilisez un rapport opérationnel adapté au but.

## Références et lectures complémentaires

- Edward Tufte, « The Visual Display of Quantitative Information ».
- Stephen Few, « Show Me the Numbers » et « Information Dashboard Design ».
- Cole Nussbaumer Knaflic, « Storytelling with Data ».
- Alberto Cairo, « How Charts Lie ».
- Ralph Kimball et Margy Ross, « The Data Warehouse Toolkit ».
- Darrell Huff, « How to Lie with Statistics ».
- Benn Stancil et autres, écrits sur la couche sémantique et les magasins de métriques.
