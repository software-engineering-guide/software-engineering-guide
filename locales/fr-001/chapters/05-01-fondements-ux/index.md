# 5.1 Fondements UX

## Vue d'ensemble et motivation

L'**[expérience utilisateur](https://fr.wikipedia.org/wiki/Exp%C3%A9rience_utilisateur)** (UX) consiste à comprendre les gens (leurs objectifs, leurs contextes, leurs contraintes) puis à façonner le logiciel pour qu'il les aide à réussir avec le moins de friction possible. Ce n'est pas une décoration que vous appliquez à la fin. C'est une façon de travailler qui commence avant la première ligne de code et continue bien après la sortie. Ce chapitre couvre les pratiques de recherche, de modélisation, et de [pensée design](https://fr.wikipedia.org/wiki/Design_thinking) qui permettent à une grande organisation de prendre des décisions de produit à partir de preuves plutôt que de suppositions.

Pour les grandes équipes, l'UX est un problème de coordination autant qu'un métier. Quand des dizaines d'escouades livrent dans un seul produit partagé, des modèles mentaux discordants, des flux dupliqués, et une terminologie contradictoire s'empilent en un ensemble confus qu'aucune équipe unique ne possède. Un fondement UX partagé, construit à partir de personas communs, de cartes de parcours convenues, et d'une [architecture de l'information](https://fr.wikipedia.org/wiki/Architecture_de_l%27information) documentée, donne à chaque équipe la même carte de l'utilisateur, pour que leurs décisions séparées s'additionnent en une expérience cohérente. Sans cela, chaque équipe optimise localement et le produit dans son ensemble n'a plus de sens.

L'entreprise et l'administration publique élèvent les enjeux. Le logiciel d'entreprise a souvent des utilisateurs captifs qui ne peuvent pas partir, donc la mauvaise UX se paie en formation, tickets de support, erreurs, et productivité perdue plutôt qu'en gens qui s'en vont. Les services gouvernementaux atteignent souvent le public entier, y compris des personnes en crise, sur d'anciens appareils, avec une faible confiance numérique, ou sans fournisseur alternatif. Ici la qualité UX est une question d'équité et de confiance civique : une demande de prestation mal conçue peut priver quelqu'un de nourriture ou de logement, non parce qu'il n'y est pas éligible, mais parce qu'il n'a pas pu terminer le formulaire.

## Principes clés

- Concevez pour de vraies personnes faisant de vraies tâches dans de vraies conditions, pas pour un utilisateur idéalisé sur une connexion rapide avec pleine attention.
- La recherche réduit le risque. Le moment le moins cher pour découvrir une hypothèse fausse est avant d'avoir construit par-dessus.
- Les utilisateurs ne peuvent pas vous dire de manière fiable ce qu'ils feront ; observez le comportement, pas seulement la préférence déclarée.
- Concentrez-vous sur la tâche que l'utilisateur essaie d'accomplir, pas sur la fonctionnalité que vous voulez livrer.
- La cohérence est une fonctionnalité : un modèle mental cohérent à travers le produit abaisse la charge cognitive.
- L'[accessibilité](https://fr.wikipedia.org/wiki/Accessibilit%C3%A9_du_web) et l'inclusion font partie de la bonne UX dès le début, pas une passe de conformité ultérieure.
- Les méthodes qualitatives et quantitatives répondent à des questions différentes ; utilisez les deux.
- De petites études fréquentes battent des études rares et lourdes.

## Recommandations

### Établir une recherche continue et à méthodes mixtes

Visez une pratique de recherche légère mais continue plutôt que des grandes études occasionnelles. Les entretiens révèlent les motivations et les modèles mentaux. Le [test d'utilisabilité](https://fr.wikipedia.org/wiki/Test_d%27utilisabilit%C3%A9) révèle où les conceptions s'effondrent ; cinq à huit participants par cycle font émerger la plupart des problèmes graves. Les enquêtes mesurent les attitudes à l'échelle mais ne peuvent pas expliquer le « pourquoi. » L'analytique et l'instrumentation montrent ce que les gens font réellement à travers toute la population. Associez une méthode qualitative (pourquoi) à une quantitative (combien), pour que les découvertes soient à la fois expliquées et dimensionnées. Et gardez un dépôt de recherche, pour que les perspicacités restent cherchables et réutilisables à travers les équipes au lieu de se perdre dans les diapositives d'une escouade.

### Modéliser les utilisateurs avec des personas, cartes de parcours, et tâches à accomplir

Construisez un petit ensemble de personas fondés sur des preuves qui capturent les objectifs, contextes, et contraintes, pas des caricatures démographiques. Cadrez les besoins comme des **tâches à accomplir** (jobs-to-be-done), le résultat sous-jacent qu'un utilisateur essaie d'atteindre plutôt qu'une fonctionnalité (« quand je perds mon emploi, je veux comprendre rapidement à quel soutien j'ai droit, pour pouvoir continuer à payer le loyer »). Cela garde l'attention sur les résultats plutôt que sur les fonctionnalités. Les cartes de parcours cartographient l'expérience entière à travers les canaux et dans le temps, exposant des lacunes et transferts qu'aucun écran unique ne révèle. Pour les services avec de lourdes opérations en coulisse (centres d'appels, agents de dossier, exécution), utilisez des [schémas de service](https://fr.wikipedia.org/wiki/Service_blueprint) pour connecter l'expérience d'avant-scène aux systèmes et au personnel derrière elle.

### Concevoir l'architecture de l'information délibérément

L'**architecture de l'information** (AI) est comment le contenu, les fonctionnalités, et la navigation sont structurés et étiquetés. Utilisez le [tri de cartes](https://fr.wikipedia.org/wiki/Tri_de_cartes) et le test d'arborescence pour dériver cette structure des modèles mentaux des utilisateurs plutôt que de votre organigramme. Un échec courant dans les grandes organisations est d'exposer les frontières départementales internes comme navigation de premier niveau. Établissez un vocabulaire contrôlé pour que le même concept ait le même nom partout. La [conception d'interaction](https://fr.wikipedia.org/wiki/Design_d%27interaction) définit ensuite le comportement moment par moment : états, retour, récupération d'erreur, et le flux entre les étapes.

### Appliquer la pensée design pragmatiquement

Le modèle du double diamant (diverger puis converger pour définir le bon problème, puis diverger et converger pour concevoir la bonne solution) est un cadre utile. Traitez-le cependant comme un état d'esprit, pas un processus rigide à portes. En pratique, exécutez des boucles serrées : cadrez une hypothèse, esquissez, testez avec une poignée d'utilisateurs, et apprenez en quelques jours. Gardez la découverte plus lourde pour les problèmes véritablement nouveaux ou à haut risque. Et méfiez-vous du « théâtre d'innovation », où les ateliers produisent des notes autocollantes mais aucun changement livré.

### Intégrer l'UX dans la livraison

Intégrez les designers et chercheurs dans les équipes de livraison plutôt que d'exécuter un « département UX » séparé qui transmet des spécifications par-dessus un mur. Faites des découvertes de recherche un intrant permanent de la priorisation. Placez des portes de qualité UX, telles que des références d'utilisabilité et des contrôles d'accessibilité, dans la définition de fini. Et suivez les métriques de résultat (réussite de tâche, temps sur tâche, taux d'erreur, satisfaction) directement aux côtés de vos métriques de livraison.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| Recherche de découverte continue | Attrape les problèmes tôt, construit une compréhension partagée | Coût continu, exige un pipeline de recrutement et du personnel qualifié |
| Recherche préalable lourde | Perspicacité profonde avant un investissement majeur | Lente, peut retarder l'apprentissage que seule la livraison révèle |
| Décisions basées uniquement sur l'analytique | S'échelle, objectif, bon marché une fois instrumenté | Explique quoi mais pas pourquoi ; aveugle aux non-utilisateurs et cas limites |
| Personas et cartes de parcours | Alignent de nombreuses équipes sur un modèle de l'utilisateur | Se périment, peuvent devenir fiction si non rafraîchis avec des données |
| Designers intégrés | Retour rapide, propriété partagée | Plus difficile de garder l'art cohérent à travers de nombreuses équipes |

Chaque organisation équilibre l'investissement de recherche contre la vitesse de livraison. L'erreur est de traiter cela comme un ou-bien. La posture productive est proportionnelle : dépensez plus de découverte sur les décisions coûteuses à inverser (AI centrale, flux primaires, choix de plateforme), et moins sur les détails que vous pouvez facilement changer plus tard. Le coût de la recherche est presque toujours petit à côté du coût de bien construire la mauvaise chose.

## Questions à discuter avec votre équipe

1. **Qui possède l'architecture de l'information partagée et le vocabulaire contrôlé, et que se passe-t-il quand une équipe veut dévier ?** À l'échelle l'échec le plus courant est de laisser chaque escouade exposer sa propre structure d'organigramme et ses propres noms pour le même concept, pour que le produit finisse avec trois mots pour une chose et une navigation qui reflète les départements plutôt que les tâches utilisateur. Décidez maintenant si l'AI et le vocabulaire sont possédés centralement, dérivés du tri de cartes et du test d'arborescence plutôt que de la politique interne, et comment une équipe demande un changement. Cela compte plus en entreprise et administration publique parce que les utilisateurs captifs ne peuvent pas partir, donc l'incohérence se paie en formation, tickets de support, et erreurs plutôt qu'en désabonnement. Apportez la liste actuelle de termes dupliqués et flux contradictoires comme preuve. Si vous ne pouvez pas nommer un propriétaire, c'est votre premier élément d'action.

2. **Quel est notre pipeline de recrutement pour les participants de recherche, et atteint-il les utilisateurs assistés-numériques, à faible confiance, et non-numériques ?** La découverte continue ne fonctionne que si vous pouvez vous mettre devant de vrais utilisateurs chaque semaine, et les personnes les plus difficiles à recruter sont souvent celles qui ont le plus besoin du service : des gens en crise, sur d'anciens appareils, ou qui comptent normalement sur de l'aide. Tester seulement des volontaires confiants et connectés vous donne une lecture flatteuse mais fausse, spécialement pour les services publics où l'équité d'accès est tout l'enjeu. Convenez de qui gère le recrutement, quelles incitations vous offrez, et comment vous observez les sessions assistées-numériques sans ajouter au fardeau d'une personne vulnérable. Apportez les démographies de participants de vos trois dernières études et vérifiez-les contre votre base d'utilisateurs réelle. Si elles penchent vers des utilisateurs faciles à atteindre, corrigez le pipeline avant de faire confiance aux découvertes.

3. **Quelles portes de qualité UX appartiennent à notre définition de fini, et comment empêchons-nous qu'elles deviennent du théâtre ?** Intégrer des designers et chercheurs ne paie que si la recherche est un intrant permanent de la priorisation et si les contrôles d'utilisabilité et d'accessibilité bloquent réellement un récit de livraison, pas un jeu de diapositives que tout le monde hoche la tête et ignore. Choisissez des métriques de résultat concrètes que vous suivrez aux côtés des métriques de livraison : réussite de tâche, temps sur tâche, taux d'erreur, et satisfaction. Le risque est une recherche exécutée pour justifier des décisions déjà prises, donc convenez qui peut opposer son veto à un lancement sur une porte UX et quelle preuve outrepasse l'opinion d'un cadre. Apportez une fonctionnalité récente et demandez si sa recherche a changé la décision ou l'a simplement décorée. Si les découvertes ne déplacent jamais une feuille de route, vos portes sont cosmétiques.

4. **Comment gardons-nous nos personas, cartes de parcours, et AI de se décomposer en fiction une fois que la recherche qui les a produits a un an ?** Les modèles partagés sont ce qui permet à des dizaines d'équipes de concevoir vers une seule expérience cohérente, mais ils ne fonctionnent que tant qu'ils décrivent toujours de vrais utilisateurs, et au moment où un persona devient un artefact que les gens citent pour gagner des arguments plutôt qu'un résumé de preuve, il fait un dommage actif. Décidez qui possède le rafraîchissement de chaque modèle, à quelle cadence, et contre quelles données (nouveaux entretiens, analytique, thèmes de support), et convenez d'une date de « dernière validation » visible pour que les modèles périmés soient évidents. La considération concurrente est le coût : rafraîchir tout continuellement est gaspillage, donc liez la fréquence de rafraîchissement à la vitesse à laquelle cette partie de la base d'utilisateurs ou du parcours change réellement. Apportez la provenance de vos principaux personas actuels et demandez quand chacun a été vérifié pour la dernière fois contre un vrai utilisateur. En entreprise et administration publique, où une base d'utilisateurs captive ou publique change lentement mais avec conséquence (une population vieillissante, une nouvelle prestation, une transition d'appareil), un modèle qui dérive silencieusement hors de date peut orienter des années d'investissement vers des utilisateurs qui n'existent plus.

5. **Où l'accessibilité vit-elle dans notre processus, et pouvons-nous prouver qu'une sortie la satisfait avant qu'elle ne soit livrée plutôt qu'après une plainte ?** Traiter l'accessibilité comme une passe de conformité tardive est à la fois l'échec le plus courant et le plus coûteux, parce que rétro-adapter la sémantique, l'ordre de focus, et le contraste dans une interface construite coûte bien plus que de les concevoir dès le début. Décidez à quelle norme vous vous tenez (par exemple WCAG, les Web Content Accessibility Guidelines), si la conformité est une porte bloquante dans la définition de fini, et qui est responsable quand une fonctionnalité inaccessible atteint la production. La tension est vitesse contre inclusion, et les équipes sous pression de délai abandonneront discrètement les contrôles qui ne sont pas imposés. Apportez votre dernier audit, la couverture automatisée et manuelle derrière lui, et le nombre de problèmes d'accessibilité trouvés après la sortie plutôt qu'avant. Pour l'administration publique spécialement ce n'est pas une politesse optionnelle : c'est souvent un devoir légal et une question d'équité, puisqu'un service public qui exclut les utilisateurs handicapés ou assistés-numériques a échoué à son but principal, pas secondaire.

6. **Quand notre analytique et notre recherche qualitative sont en désaccord, comment décidons-nous laquelle croire, et qui arbitre ?** Les grandes organisations accumulent à la fois des tableaux de bord qui montrent ce que des milliers d'utilisateurs font et des entretiens qui expliquent pourquoi une poignée se comporte comme elle le fait, et les deux pointeront régulièrement dans des directions opposées : un flux à haute complétion qui humilie discrètement les gens, ou une fonctionnalité que les utilisateurs louent en session mais ne touchent jamais à l'échelle. Convenez à l'avance de comment vous triangulez, quelle question chaque méthode est fiable pour répondre (l'analytique pour l'ampleur et la portée, la recherche pour la cause et le sens), et qui a l'autorité de trancher la décision quand elles entrent en conflit. Le risque est de sélectionner la source qui flatte le plan déjà choisi. Apportez un désaccord récent concret et parcourez comment il a réellement été résolu. Dans les contextes d'entreprise et publics les enjeux sont accentués parce que l'analytique sous-compte systématiquement les personnes mêmes qui comptent le plus : les non-utilisateurs, les abandonneurs, et ceux sur technologie d'assistance apparaissent rarement dans l'entonnoir, donc faire confiance aux chiffres seuls peut rendre invisibles les exclus.

## Regard sectoriel

**Jeune pousse.** Vous n'avez pas de chercheur et pas de temps pour un dépôt, donc faites de la recherche une habitude de fondateur : asseyez-vous à côté de cinq vrais utilisateurs pendant un après-midi avant de construire la prochaine chose. Sautez les personas et cartes de parcours formels ; une compréhension partagée de la seule tâche que vous résolvez, rafraîchie en observant les gens hebdomadairement, bat la documentation que personne ne maintient. Votre avantage est que toute l'équipe peut absorber une perspicacité le jour même où elle apparaît, donc protégez cette vitesse et résistez à la cérémonie.

**Petite entreprise.** Sans spécialiste UX et avec un budget serré, appuyez-vous sur les conventions que vos utilisateurs connaissent déjà plutôt que d'inventer les vôtres, et achetez des outils avec des valeurs par défaut sensées au lieu de concevoir des flux à partir de zéro. Faites vous-même la recherche bon marché et à haute valeur : une poignée de sessions d'utilisabilité par appel vidéo et une lecture de vos tickets de support feront émerger la plupart des problèmes graves. Traitez les bases d'accessibilité (contraste, étiquettes, accès clavier) comme des prérequis que vous obtenez d'une bonne bibliothèque de composants plutôt qu'un projet que vous dotez.

**Grande entreprise.** Le problème central est la cohérence à travers de nombreuses équipes, donc investissez dans les fondations partagées : personas possédés, cartes de parcours maintenues, vocabulaire contrôlé, et une architecture de l'information documentée vers laquelle les escouades conçoivent plutôt qu'autour. Intégrez les designers et chercheurs dans les équipes de livraison, mais gouvernez l'art centralement pour que le produit ne se fracture pas en dialectes incohérents. Financez un dépôt de recherche et des portes de qualité dans la définition de fini, et suivez les métriques de résultat UX comme un portefeuille pour qu'aucune optimisation locale d'une équipe unique ne dégrade l'ensemble.

**Gouvernement.** L'accessibilité et l'équité d'accès sont des devoirs, pas des préférences, donc tenez les sorties à une norme publiée et faites de la recherche avec l'éventail complet du public, y compris les utilisateurs assistés-numériques, à faible confiance, et non-numériques. L'approvisionnement et la transparence façonnent la livraison : publiez vos principes de conception et méthodes de recherche, structurez les services autour des événements de vie des citoyens plutôt que des départements internes, et gardez la preuve de test pour l'audit. Parce que les utilisateurs n'ont souvent aucun fournisseur alternatif, un flux qu'ils ne peuvent pas terminer refuse un service, donc traitez la complétion par l'utilisateur le plus difficile à atteindre comme la vraie mesure de succès.

## Exemples

**Jeune pousse.** Une jeune pousse de quatre personnes construisant un outil de planification pour de petites cliniques avait des opinions fortes sur ce dont les réceptionnistes avaient besoin, mais aucune preuve. Avant d'écrire plus de fonctionnalités, les fondateurs se sont assis à côté de cinq réceptionnistes pendant un après-midi chacune et les ont regardées travailler. Ils ont appris que la vraie douleur n'était pas la vitesse de réservation mais les doubles réservations causées par une vue de calendrier confuse, quelque chose que personne n'avait pensé à mentionner dans les appels de vente précédents. Recadrer le produit autour de cette seule tâche, et esquisser et tester des corrections avec les mêmes cinq personnes sur une semaine, a transformé un essai bloqué en leurs premiers clients payants.

**Grande entreprise.** Une banque multinationale a consolidé sept outils régionaux internes d'origination de prêts en une seule plateforme. Plutôt que de fusionner les ensembles de fonctionnalités, l'équipe a exécuté de la cartographie de parcours et des schémas de service avec des souscripteurs à travers les régions. Ils ont découvert que les « différences régionales » que tout le monde supposait étaient surtout une terminologie et un ordre d'écran incohérents, pas de vraies différences de processus. Une AI unifiée et un vocabulaire partagé ont réduit substantiellement le temps de formation des souscripteurs et diminué les erreurs de traitement, parce que le personnel partageait maintenant un modèle mental.

**Gouvernement.** Une administration fiscale nationale redessinant son service de déclaration en ligne a exécuté du test d'utilisabilité modéré avec des contribuables couvrant des âges, appareils, et niveaux de confiance numérique, plus de l'observation assistée-numérique de personnes qui comptent normalement sur de l'aide. Le test a révélé que des titres de section chargés de jargon causaient des abandons ou des erreurs de dépôt. Recadrer le contenu autour des tâches à accomplir des contribuables, et restructurer l'AI autour des événements de vie plutôt que des codes fiscaux internes, a augmenté la complétion en libre-service réussie et réduit le volume de centre d'appels, abaissant directement le coût de service tout en améliorant l'équité d'accès.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur l'UX vient de trois leviers : plus de réussite (plus d'utilisateurs terminent des tâches précieuses), un coût de service plus bas (moins de contacts de support, moins de formation, moins d'erreurs), et moins de retravail (attraper les mauvaises directions avant qu'elles ne soient construites). Dans les contextes d'entreprise où les utilisateurs sont captifs, le gain se manifeste en productivité et moins d'erreurs plutôt qu'en conversion ; quelques secondes économisées par transaction, à travers des milliers d'employés, se composent en larges économies annuelles.

Le coût total de possession doit peser le coût d'adopter contre le coût de ne pas adopter. Les coûts d'adoption sont faciles à voir : chercheurs et designers, recrutement et incitations pour les participants, outillage, et temps dans le calendrier. Le coût de ne pas adopter est plus grand mais plus difficile à repérer : transactions abandonnées, surcharge de support et de formation, refontes tardives coûteuses, lancements échoués, et exposition réputationnelle ou légale quand les services publics excluent des gens. Parce que ces coûts sont répartis à travers les budgets de support, de formation, et d'opérations plutôt que la ligne de produit, le leadership les sous-estime souvent.

Pour faire valoir cela auprès de la direction, liez l'UX à des métriques que les cadres suivent déjà : taux de complétion et de conversion, coût par transaction, volume de tickets de support, jours de formation, et taux d'erreur et de retravail. Exécutez un pilote petit et instrumenté qui montre un avant-après mesurable, puis extrapolez à travers le portefeuille. Cadrer la recherche comme une réduction de risque sur des décisions irréversibles tend à résonner avec les parties prenantes de finance et de gouvernance.

## Anti-patterns et pièges

- **Conception pilotée par l'opinion du plus payé** : des décisions prises par l'opinion de la personne la mieux payée au lieu de preuves.
- **Théâtre de recherche** : des études exécutées pour justifier des décisions déjà prises, découvertes ignorées.
- **Personas comme fiction** : des profils inventés jamais validés contre de vrais utilisateurs, utilisés pour gagner des arguments.
- **Organigramme comme AI** : une navigation qui reflète les départements internes plutôt que les tâches utilisateur.
- **Recherche à grand fracas** : des études rares et coûteuses qui arrivent trop tard pour changer quoi que ce soit.
- **Tester seulement le chemin heureux** : ignorer les états d'erreur, cas limites, et utilisateurs sous stress.
- **Conception comme dernière couche de peinture** : faire intervenir l'UX seulement pour faire « bien paraître » une construction terminée.
- **Ignorer les utilisateurs assistés et non-numériques** : concevoir seulement pour des utilisateurs confiants et connectés.

## Modèle de maturité

**Niveau 1 (Initier).** Aucune pratique UX dédiée. Les décisions sont prises par opinion et l'instinct de la personne la mieux payée. La recherche, si elle se produit du tout, est au coup par coup et réactive, déclenchée par un lancement qui s'est mal passé. Les flux et la terminologie sont incohérents à travers les équipes, et personne ne possède l'expérience globale.

**Niveau 2 (Développer).** Certaines équipes ont des designers et exécutent des tests d'utilisabilité occasionnels, et quelques personas ou cartes de parcours existent, mais la pratique varie largement entre escouades et n'est pas maintenue. L'UX est traitée comme une phase plutôt qu'une discipline continue, et elle est souvent contournée sous pression de calendrier. Du bon travail se produit en poches mais ne s'additionne pas à travers le produit.

**Niveau 3 (Standardiser).** La recherche continue à méthodes mixtes alimente la priorisation, et des personas partagés, des cartes de parcours, et une AI à vocabulaire contrôlé sont documentés et utilisés à travers les équipes. Les portes de qualité UX, incluant des références d'utilisabilité et des contrôles d'accessibilité, se trouvent dans la définition de fini et sont imposées à l'échelle de l'organisation. Un dépôt de recherche cherchable garde les perspicacités réutilisables plutôt que piégées dans les diapositives d'une escouade.

**Niveau 4 (Gérer).** La pratique est mesurée contre des références plutôt que simplement exécutée. Vous suivez la réussite de tâche, le temps sur tâche, le taux d'erreur, la satisfaction, et la conformité d'accessibilité comme des métriques convenues, fixez des cibles, et les surveillez à travers les sorties. Les échantillons de participants de recherche sont vérifiés contre la base d'utilisateurs réelle pour que les découvertes soient représentatives, les portes de qualité rapportent des taux de passage plutôt que des opinions, et le coût de la recherche est pesé contre des réductions mesurées de contacts de support, formation, et retravail. Les décisions de livrer ou retenir reposent sur la preuve contre ces références.

**Niveau 5 (Orchestrer).** La recherche est continue, liée aux résultats, et intégrée à la planification produit, affaires, et risque à travers l'organisation. Les équipes exécutent des expériences contrôlées, ferment la boucle de la perspicacité au changement livré à l'effet mesuré, et retirent ou recadrent les modèles d'utilisateurs à mesure que la population et ses parcours changent. Le fondement UX s'adapte continuellement : personas, parcours, AI, et normes sont rafraîchis sur preuve, et l'organisation rééquilibre où elle investit la découverte à mesure que la réversibilité et le risque changent.

## Pistes de réflexion

- Combien de découverte est « suffisant » avant de s'engager dans une direction, et qui décide ?
- Comment gardez-vous les personas et cartes de parcours vivants plutôt que de les laisser devenir des artefacts périmés ?
- Quand l'analytique quantitative et la recherche qualitative sont en désaccord, laquelle croyez-vous et pourquoi ?
- Comment une grande organisation devrait-elle équilibrer une norme UX centrale avec l'autonomie de chaque équipe ?
- Quelle est la bonne façon de faire de la recherche sur des services utilisés par des personnes en crise sans ajouter à leur fardeau ?
- Comment mesurez-vous le retour sur investissement d'une recherche qui prévient une erreur que vous n'avez donc jamais commise ?

## Points clés à retenir

- L'UX est une façon de travailler depuis le début, pas une décoration à la fin.
- Combinez des méthodes qualitatives (pourquoi) avec des méthodes quantitatives (combien).
- Modélisez les utilisateurs avec des personas fondés sur des preuves, des cartes de parcours, des tâches à accomplir, et des schémas de service.
- Structurez l'information autour des modèles mentaux des utilisateurs, pas de l'organigramme.
- Traitez la pensée design comme un état d'esprit pragmatique avec des boucles d'apprentissage serrées, pas un processus rigide.
- Le coût de la recherche est petit comparé au coût de construire la mauvaise chose.
- En entreprise et administration publique, la qualité UX se traduit directement en productivité, coût de service, et équité d'accès.

## Références et lectures complémentaires

- Don Norman, *The Design of Everyday Things*.
- Steve Krug, *Don't Make Me Think*.
- Erika Hall, *Just Enough Research*.
- Kim Goodwin, *Designing for the Digital Age*.
- Louis Rosenfeld, Peter Morville, et Jorge Arango, *Information Architecture: For the Web and Beyond*.
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done).
- Alan Cooper, *The Inmates Are Running the Asylum*.
- Jakob Nielsen, *Usability Engineering*.
- UK Government Digital Service, *Service Manual* et *Design Principles*.
- U.S. General Services Administration, *18F Methods* et la guidance de recherche du *U.S. Web Design System*.
- Nielsen Norman Group, articles et rapports sur les méthodes de recherche.
