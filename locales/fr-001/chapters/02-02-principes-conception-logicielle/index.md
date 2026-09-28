# 2.2 Principes de conception logicielle

## Vue d'ensemble et motivation

Les principes de conception logicielle sont des heuristiques pour arranger le code afin de pouvoir le comprendre, le changer, et l'étendre dans le temps. Ils incluent des acronymes nommés ([SOLID](https://en.wikipedia.org/wiki/SOLID) pour cinq principes de conception [orientée objet](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) pour ne-vous-répétez-pas, [KISS](https://en.wikipedia.org/wiki/KISS_principle) pour restez-simple, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) pour vous-n'en-aurez-pas-besoin), des concepts structurels ([couplage](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [cohésion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns)), des [patrons de conception](https://en.wikipedia.org/wiki/Software_design_pattern) catalogués, des approches de modélisation de plus haut niveau comme la [conception pilotée par le domaine](https://en.wikipedia.org/wiki/Domain-driven_design) (modéliser le logiciel dans le langage du domaine métier), et le choix entre les styles orienté objet, [fonctionnel](https://en.wikipedia.org/wiki/Functional_programming), et [orienté données](https://en.wikipedia.org/wiki/Data-oriented_design). Aucun de ceux-ci n'est une loi. Ce sont de l'expérience compressée, et vous devez les appliquer avec jugement.

Pour les grandes équipes, la valeur des principes partagés est la coordination. Quand des centaines d'ingénieurs travaillent sur le même système, ils ont besoin d'un vocabulaire commun pour les discussions de conception et d'un ensemble commun de défauts afin que des modules écrits indépendamment s'assemblent. Une bonne conception est ce qui laisse de nombreuses personnes changer un système en parallèle sans collisions constantes. C'est aussi ce qui garde un système modifiable une décennie plus tard, la durée de vie normale des systèmes d'entreprise et gouvernementaux, bien après le mandat de leurs auteurs d'origine.

La compétence critique n'est pas de mémoriser les principes. C'est de savoir quand chacun vous trompe. Chaque principe a un mode d'échec : DRY peut produire la mauvaise abstraction, SOLID peut produire une indirection inutile, YAGNI peut affamer une extensibilité dont vous avez réellement besoin. Ce chapitre traite les principes comme des outils avec un domaine d'applicabilité, et il met l'accent sur le couplage et la cohésion comme les propriétés plus profondes que les acronymes tentent de servir.

## Principes clés

- Gérez le couplage et la cohésion en premier ; la plupart des principes nommés sont des façons indirectes d'améliorer ces deux propriétés.
- Optimisez pour le changement : une bonne conception minimise le coût des changements que vous devrez réellement faire.
- Préférez la conception la plus simple qui fonctionne maintenant, mais gardez des frontières là où le changement est probable.
- La duplication est moins chère que la mauvaise abstraction ; attendez que le motif soit clair.
- Rendez les dépendances explicites et pointez-les vers des choses stables.
- Modélisez le domaine dans le langage du domaine ; alignez les frontières logicielles avec les frontières métier.
- Choisissez les paradigmes selon l'adéquation, pas l'idéologie ; la plupart des grands systèmes sont pragmatiquement mixtes.

## Recommandations

### Utilisez SOLID comme un prisme, pas une liste de contrôle

Appliquez la responsabilité unique pour garder les modules cohésifs, l'inversion de dépendance pour pointer les dépendances vers des abstractions là où une frontière existe réellement, et l'ouvert-fermé là où les points d'extension sont réels. Ne fabriquez pas d'interfaces, de fabriques, et de couches juste pour satisfaire l'acronyme quand il n'y a qu'une seule implémentation et aucune seconde en vue. L'indirection a un coût, et vous le payez à chaque lecture.

### Appliquez DRY à la connaissance, pas au texte

DRY concerne le fait de ne pas dupliquer un seul élément faisant autorité de *connaissance*. Ce n'est pas éliminer des lignes qui se ressemblent simplement. Deux morceaux de code qui semblent similaires mais changent pour des raisons différentes devraient rester séparés. Préférez un peu de duplication à une abstraction partagée prématurée qui couple des choses sans rapport. Extrayez l'abstraction une fois que le vrai motif est apparu deux ou trois fois.

### Laissez KISS et YAGNI résister à la spéculation

Construisez pour les exigences que vous avez, pas celles que vous imaginez. Évitez la généralité spéculative, comme les cadres configurables, les systèmes de plugins, et les points d'extension que personne n'a demandés. Le contrepoids est qu'une certaine flexibilité est réellement moins chère à construire tôt, comme une interface stable ou une couture propre. YAGNI argumente contre l'*implémentation* spéculative, pas contre des frontières réfléchies.

### Concevez explicitement pour un faible couplage et une haute cohésion

Faites en sorte que chaque module fasse une chose bien définie (cohésion), et dépende du moins d'autres modules possible, à travers des interfaces étroites (faible couplage). Quand vous révisez une conception, demandez quels changements se répercutent à travers les frontières de module. Ces répercussions sont la vraie mesure du couplage. La séparation des préoccupations est la même idée appliquée aux couches et aux préoccupations transversales.

### Utilisez les patrons de conception comme vocabulaire, appliquez les anti-patrons comme avertissements

Les patrons sont des noms partagés utiles pour des solutions récurrentes. Tendez la main vers un quand le problème correspond réellement. N'imposez pas de patrons pour paraître sophistiqué, parce que le code chargé de patrons est souvent un signe de sur-ingénierie. Apprenez les [anti-patrons](https://en.wikipedia.org/wiki/Anti-pattern) courants (objets dieu, modèles anémiques là où inapproprié, grosses boules de boue, monolithes distribués) comme étiquettes diagnostiques.

### Adoptez la conception pilotée par le domaine là où le domaine est complexe

Pour les systèmes avec des règles métier riches, utilisez les outils tactiques et stratégiques de la DDD : un langage ubiquitaire partagé avec les experts du domaine, des contextes bornés qui découpent le système en pièces modélisées indépendamment, et des cartes de contexte qui décrivent comment ces pièces se rapportent. Les contextes bornés sont particulièrement précieux à l'échelle de l'entreprise, parce qu'ils alignent l'appropriation d'équipe avec les frontières de modèle. La DDD est excessive pour de simples systèmes [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (créer, lire, mettre à jour, supprimer).

### Choisissez les paradigmes par adéquation

Utilisez l'orientation objet pour encapsuler le comportement à état et modéliser les domaines. Utilisez le style fonctionnel pour les transformations, la concurrence, et la prévisibilité à travers l'[immuabilité](https://en.wikipedia.org/wiki/Immutable_object). Utilisez la conception orientée données là où la performance et le comportement de cache dominent. Les grands systèmes mélangent les trois. Faites le choix par composant, et gardez les frontières entre styles propres.

## Compromis : avantages et inconvénients

| Principe / approche | Bien appliqué | Mode d'échec |
|---|---|---|
| SOLID | Coutures claires là où le changement se produit ; unités testables | Prolifération d'interfaces et de couches ; indirection sans retour |
| DRY | Source de vérité unique pour une vraie connaissance | Mauvaise abstraction couplant du code sans rapport |
| KISS / YAGNI | Systèmes légers et compréhensibles | Coutures sous-conçues ; adaptations coûteuses de flexibilité nécessaire |
| Patrons de conception | Vocabulaire partagé ; structures éprouvées | Culte du cargo de patrons ; complexité accidentelle |
| Conception pilotée par le domaine | Modèles et équipes alignés ; complexité apprivoisée | Cérémonie lourde sur des domaines simples ; frontières de contexte mal placées |
| Fonctionnel / immuable | Prévisibilité ; concurrence plus sûre | Adéquation maladroite pour des problèmes intrinsèquement à état ; surprises de performance |

La tension récurrente est entre la sous-conception et la surconception. Les systèmes sous-conçus accumulent du couplage et deviennent rigides. Les systèmes surconçus se noient dans une abstraction que quelqu'un doit comprendre et maintenir. La réponse n'est pas un point fixe. C'est une discipline : différer les décisions jusqu'à avoir assez d'information, tout en gardant les coutures qui vous laissent changer d'avis.

## Questions à discuter avec votre équipe

1. **Quel est votre seuil concret pour extraire une abstraction partagée, et comment empêchez-vous DRY de produire la mauvaise ?** Ce chapitre est direct : la duplication est moins chère que la mauvaise abstraction, et vous devriez attendre que le motif soit apparu deux ou trois fois avant d'extraire. Dans une grande équipe, le danger est que quelqu'un factorise deux extraits qui se ressemblent en un module partagé à travers les frontières d'équipe, puis chaque futur changement à un appelant se répercute dans l'autre. Le signal à apporter est si les duplicats changent pour la même raison ou se ressemblent simplement en ce moment. Convenez d'une règle de trois, et exigez qu'une abstraction candidate ait réellement changé ensemble avant de coupler les appelants. Cet accord unique empêche une classe de couplage coûteuse à défaire une fois que de nombreuses équipes en dépendent.

2. **Comment rendez-vous le couplage et la cohésion visibles en revue de conception au lieu de les laisser au feeling ?** Les principes clés placent le couplage et la cohésion au-dessus de chaque acronyme, et définissent le couplage comme les changements qui se répercutent à travers les frontières de module. L'intuition ne passe pas à l'échelle à travers des centaines d'ingénieurs qui ne voient chacun que leur coin du système. Apportez des preuves qu'une machine peut produire : des graphes de dépendance, et des données de co-changement montrant quels modules continuent d'être édités ensemble dans les mêmes commits. Ajoutez une question de revue explicite qui demande quelles frontières de module un changement force à traverser. Quand deux modules changent toujours ensemble, c'est votre signal pour soit les fusionner soit corriger la frontière entre eux.

3. **Où est la ligne dans vos systèmes entre un domaine assez riche pour justifier la conception pilotée par le domaine et une simple application CRUD où c'est excessif ?** Le chapitre recommande les contextes bornés de la DDD précisément parce qu'ils alignent l'appropriation d'équipe avec les frontières de modèle, et avertit que la DDD est excessive pour de simples systèmes créer-lire-mettre à jour-supprimer et dégénère en cérémonie sans vraie modélisation. Se tromper dans l'une ou l'autre direction est coûteux : une DDD lourde sur un domaine mince enterre une application simple dans la cérémonie, tandis qu'un modèle partagé tentaculaire à travers de nombreuses équipes force une coordination inter-équipes constante. Apportez les signaux qui décident réellement : la densité des règles métier, et combien d'équipes ont besoin de posséder des pièces indépendamment. Réservez la machinerie stratégique pour le noyau complexe, et laissez les bords simples rester simples. Cela vous garde à l'écart à la fois du théâtre DDD et de la grosse boule de boue.

4. **Quand une abstraction, une interface, ou un patron de conception vaut-il l'indirection qu'il ajoute, et qui a l'autorité pour déclarer une conception surconçue ?** Ce chapitre est explicite que l'indirection a un coût que vous payez à chaque lecture, et que fabriquer des interfaces, des fabriques, et des couches pour satisfaire SOLID ou paraître sophistiqué est un mode d'échec. Dans une grande équipe, la pression va dans l'autre sens : les réviseurs laissent passer l'abstraction supplémentaire parce que ça semble discipliné, et personne ne veut être la personne qui argumente pour moins de structure. La considération concurrente est réelle, parce que certaines coutures justifient réellement leur coût et les retirer plus tard est coûteux. Apportez des preuves concrètes à la discussion : combien d'implémentations une interface a réellement aujourd'hui, à quelle fréquence le point d'extension a jamais fléchi, et combien de fichiers un lecteur doit ouvrir pour suivre un chemin de code. Convenez qu'une implémentation unique sans seconde en vue est une raison par défaut d'intégrer en ligne, et nommez qui peut étiqueter une conception comme surconçue sans que cela ne se lise comme une insulte. Dans les systèmes d'entreprise et gouvernementaux qui survivent à leurs auteurs d'une décennie, l'indirection gratuite est une taxe que chaque futur mainteneur paie, donc traitez « qu'est-ce que cette abstraction nous achète » comme une question de revue permanente, pas un défi personnel.

5. **Comment décidez-vous quel paradigme chaque composant utilise, orienté objet, fonctionnel, ou orienté données, et comment gardez-vous les frontières entre eux propres ?** Le chapitre argumente que les grands systèmes sont pragmatiquement mixtes et que vous devriez choisir par composant selon l'adéquation, en utilisant l'orientation objet pour les domaines à état, le style fonctionnel pour les transformations et la concurrence, et la conception orientée données là où la performance et le comportement de cache dominent. Non géré, le choix de paradigme devient une question de qui a écrit le module en premier, et l'état mutable fuit dans ce qui devrait être des transformations pures, ou un purisme fonctionnel combat un problème intrinsèquement à état. La preuve qui vaut la peine d'être apportée est où se trouve votre vraie douleur : quels composants sont difficiles à tester à cause d'un état caché, quels chemins chauds sont liés au cache, et où le style actuel force des contournements maladroits. Décidez délibérément du paradigme par défaut pour chaque couche et écrivez où tombent les coutures entre styles, afin qu'un noyau fonctionnel et un bord impératif ne se mélangent pas. Pour un système réglementé ou gouvernemental où un calcul doit être auditable et reproductible pour une période donnée, un noyau immuable et fonctionnel est souvent une exigence de conformité plutôt qu'un goût, et cette contrainte devrait conduire la frontière plutôt que la suivre.

6. **Comment empêchez-vous ces principes de se solidifier en dogme, et où enregistrez-vous le raisonnement derrière une décision de conception afin qu'une future équipe puisse la revisiter ?** Chaque principe de ce chapitre a un domaine d'applicabilité et un mode d'échec, et tout le cadrage les traite comme des outils à appliquer avec jugement plutôt que des lois à faire respecter. Dans une grande équipe, un principe devient silencieusement une règle : DRY interdit toute duplication, SOLID mandate une interface par classe, et les exceptions pragmatiques sont bloquées en revue par des gens citant l'acronyme plutôt que le résultat. La tension est qu'une certaine cohérence aide réellement des centaines d'ingénieurs à se coordonner, donc vous ne pouvez pas simplement déclarer chaque principe optionnel. Apportez des exemples où suivre un principe à la lettre a produit une pire conception, et apportez les registres de décision, le cas échéant, qui expliquent pourquoi une frontière ou une abstraction donnée existe. Convenez que les principes sont des défauts dont un ingénieur peut dévier avec une raison enregistrée, et capturez les choix de conception conséquents dans un court registre de décision d'architecture afin que la prochaine équipe hérite du raisonnement et pas seulement du code. Dans les systèmes d'entreprise et du secteur public, où les auteurs d'origine sont partis depuis longtemps et où les audits demandent pourquoi le système est façonné ainsi, cette trace écrite est la différence entre une conception que les futures équipes peuvent changer en sécurité et une qu'elles ont peur de toucher.

## Regard sectoriel

**Jeune pousse.** Favorisez la conception la plus simple qui livre et gardez un module bien factorisé unique jusqu'à ce qu'un vrai deuxième cas d'usage force une couture. Votre ressource la plus rare est l'attention d'ingénierie, donc les interfaces prématurées, les couches, et les cadres spéculatifs sont un coût pur. Suivez la règle de trois avant d'extraire toute abstraction partagée, et laissez YAGNI tuer les points d'extension que personne n'a encore demandés.

**Petite entreprise.** Sans architecte dédié et avec un budget serré, appuyez-vous sur la conception déjà intégrée dans les cadres et bibliothèques que vous achetez plutôt que d'inventer vos propres patrons. Réservez l'effort de conception personnalisé pour la poignée de règles qui sont réellement votre métier, et gardez tout le reste conventionnel afin qu'un prestataire ou une nouvelle recrue puisse le lire. Un peu de duplication que vous comprenez vaut mieux qu'une abstraction astucieuse que seul son auteur peut maintenir.

**Grande entreprise.** Le gain des principes partagés est la coordination à travers de nombreuses équipes : un vocabulaire commun pour la revue de conception, et des contextes bornés qui alignent les frontières de modèle avec l'appropriation d'équipe afin que les groupes évoluent indépendamment. Gérez explicitement le couplage et la cohésion avec des données de dépendance et de co-changement, et enregistrez les décisions de conception conséquentes afin que les systèmes restent modifiables longtemps après que leurs auteurs soient passés à autre chose. Gardez-vous également contre la mauvaise abstraction qui couple les équipes et la sur-ingénierie qui taxe chaque lecteur.

**Gouvernement.** L'auditabilité et la reproductibilité dictent souvent la conception. Un noyau immuable et fonctionnel vous laisse reproduire exactement un calcul historique pour une période donnée, ce qu'un graphe d'objets emmêlé avec un état mutable caché ne peut pas garantir. Préférez des contrats publiés explicites aux tables partagées aux frontières de contexte, et gardez la conception et ses registres de décision lisibles pour les auditeurs et pour quelle que soit l'équipe qui hérite du système une décennie plus tard.

## Exemples

**Jeune pousse.** Une start-up de trois ingénieurs construisant son premier produit résiste à l'envie de diviser chaque fonctionnalité en couches d'interfaces et de fabriques, gardant un module unique bien factorisé jusqu'à ce qu'un vrai deuxième cas d'usage apparaisse. Quand la même logique apparaît une troisième fois à travers les flux d'inscription et de facturation, ils extraient une petite fonction partagée plutôt qu'un cadre spéculatif. Cela garde la base de code assez petite pour que n'importe lequel d'entre eux puisse la tenir en tête, et les quelques coutures qu'ils dessinent tombent là où le produit est le plus susceptible de changer.

**Grande entreprise.** Une grande plateforme d'assurance modélise les polices, les réclamations, et la facturation comme des contextes bornés séparés, chacun possédé par une équipe dédiée avec son propre modèle de données et sa frontière de service. Là où les contextes se rencontrent, comme quand une réclamation référence une police, ils communiquent à travers des contrats publiés explicites plutôt que des tables de base de données partagées. Cela laisse les trois équipes évoluer indépendamment, et le langage ubiquitaire garde les conversations avec les souscripteurs et les actuaires précises. Une version antérieure avait partagé un modèle unique et tentaculaire, et chaque changement exigeait une coordination inter-équipes.

**Gouvernement.** Un système national de traitement fiscal favorise délibérément un noyau orienté données et fonctionnel pour son moteur de calcul. Les règles fiscales sont exprimées comme des transformations pures sur des enregistrements d'entrée immuables, ce qui les rend auditables, testables, et reproductibles pour une année fiscale donnée. Les parties impératives et à état (flux de travail, notifications) sont gardées aux bords. Les auditeurs peuvent pointer vers une version de règle spécifique et reproduire exactement tout calcul historique, ce qui est une exigence légale qu'un graphe d'objets emmêlé avec un état mutable caché ne pourrait pas garantir.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La qualité de conception est un investissement dans la *modifiabilité* d'un système, et la modifiabilité domine le coût total de possession. La plupart du coût d'un système atterrit après sa première publication, dans la modification et l'extension. Les systèmes bien conçus gardent le coût du changement à peu près plat dans le temps. Les systèmes mal conçus voient le coût de chaque changement grimper jusqu'à ce que le système devienne effectivement immodifiable et doive être réécrit, le résultat le plus coûteux de tous.

Le coût d'adoption est surtout de la compétence et de la discipline de revue : enseigner les principes, et dépenser du temps de conception en amont. Le coût de ne pas les adopter est l'accumulation lente de la [dette technique](https://en.wikipedia.org/wiki/Technical_debt), une vélocité de livraison en baisse, des taux de défauts en hausse, et d'éventuelles réécritures coûteuses. Pour convaincre la direction, reliez la discipline de conception à la prévisibilité de livraison et à l'évitement de programmes de réécriture, et suivez des indicateurs avancés comme le taux d'échec des changements et le temps pour implémenter des fonctionnalités comparables dans le temps. Méfiez-vous aussi de l'échec opposé : sur-investir dans la conception pour des futurs incertains détruit aussi de la valeur. Donc l'argument est pour une conception *appropriée*, calibrée à quel point le changement futur est probable et coûteux.

## Anti-patterns et pièges

- **La généralité spéculative :** construire de l'extensibilité pour des exigences imaginées qui n'arrivent jamais.
- **La mauvaise abstraction :** forcer du code sans rapport ensemble pour satisfaire DRY, créant un couplage pire que la duplication.
- **Le culte du cargo de patrons :** appliquer des patrons de conception pour eux-mêmes, ajoutant de l'indirection sans bénéfice.
- **Les objets anémiques ou dieu :** des modèles sans comportement, ou des objets qui font tout ; les deux signalent des responsabilités mal placées.
- **Le monolithe distribué :** des services divisés physiquement mais encore étroitement couplés, combinant les coûts des deux approches.
- **La grosse boule de boue :** aucune structure discernable ; chaque changement risque tout.
- **Le théâtre DDD :** adopter le vocabulaire et la structure de dossiers sans la modélisation de domaine qui lui donne sa valeur.

## Modèle de maturité

- **Niveau 1, Initiation :** La conception est ad hoc et réactive ; le couplage s'accumule sans contrôle ; les principes sont inconnus ou invoqués comme des slogans, et les abstractions apparaissent ou disparaissent par habitude individuelle.
- **Niveau 2, Développement :** Les équipes connaissent les principes et les appliquent, mais de façon incohérente et souvent dogmatique ; certains groupes gèrent le couplage et la cohésion délibérément tandis que d'autres non, et il n'y a pas de vocabulaire partagé à travers l'organisation.
- **Niveau 3, Standardisation :** Un vocabulaire de conception partagé, une règle de trois pour extraire les abstractions, une analyse de couplage et cohésion, et des contextes bornés alignés aux équipes sont documentés et attendus dans toute l'organisation, appliqués de manière cohérente en revue de conception plutôt que laissés au goût individuel.
- **Niveau 4, Gestion :** La santé de la conception est mesurée par rapport à des références : les données de couplage et de co-changement, le taux d'échec des changements, et le temps pour implémenter des fonctionnalités comparables sont suivis dans le temps, afin que les abstractions et frontières soient ajoutées, gardées, ou retirées sur preuve, et que la sur-ingénierie et la mauvaise abstraction soient attrapées par les données plutôt que l'opinion.
- **Niveau 5, Orchestration :** La discipline de conception est intégrée à la planification de livraison et de risque à travers l'organisation ; les principes sont appliqués avec nuance et des modes d'échec connus ; les choix de paradigme et de frontière sont délibérés et continuellement revisités, et l'organisation refactorise, recadre, et retire régulièrement les abstractions à mesure que le domaine et les preuves changent.

## Pistes de réflexion

- Comment faites-vous la différence entre une couture nécessaire et une généralité spéculative avant d'avoir l'exigence future ?
- Quand DRY a-t-il conduit votre équipe à la mauvaise abstraction, et comment l'avez-vous reconnu ?
- Où les frontières de contexte borné devraient-elles tomber, et à quel point devraient-elles refléter l'organigramme ?
- Combien de conception devrait précéder le code dans votre contexte, et comment enregistrez-vous les décisions ?
- Quelles parties de votre système bénéficieraient d'un style plus fonctionnel ou orienté données ?
- Comment empêchez-vous les principes de conception de se solidifier en dogme qui résiste aux exceptions pragmatiques ?

## Points clés à retenir

- Le couplage et la cohésion sont les propriétés qui comptent ; les acronymes sont des moyens vers ces fins.
- Chaque principe a un mode d'échec ; sachez quand chacun vous trompe.
- Préférez un peu de duplication à une abstraction prématurée ou fausse.
- Utilisez la DDD et les contextes bornés pour aligner les domaines complexes avec l'appropriation d'équipe.
- Choisissez les paradigmes par adéquation ; les grands systèmes sont pragmatiquement mixtes.
- Concevez pour les changements dont vous aurez réellement besoin, évitant à la fois la sous-conception et la surconception.

## Références et lectures complémentaires

- Robert C. Martin, *Clean Architecture* et *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* et *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
