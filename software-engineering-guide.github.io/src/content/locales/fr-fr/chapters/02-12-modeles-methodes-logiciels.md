# 2.12 Modèles et méthodes logiciels

## Vue d'ensemble et motivation

Un modèle logiciel est une simplification délibérée d'un système, construite pour répondre à une question spécifique. Une méthode est une façon disciplinée de produire du logiciel, incluant les modèles qu'elle utilise en chemin. Ensemble, ils forment un domaine de connaissance du Software Engineering Body of Knowledge (SWEBOK), parce que ce sont les outils mentaux que vous utilisez pour raisonner sur un système avant, pendant, et après l'avoir construit. Un diagramme de classe UML ([Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), un [diagramme entité-relation](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), une [machine à états](https://en.wikipedia.org/wiki/Finite-state_machine), une [spécification formelle](https://en.wikipedia.org/wiki/Formal_specification), et un prototype jetable sont tous des modèles. La [cascade](https://en.wikipedia.org/wiki/Waterfall_model), le [prototypage](https://en.wikipedia.org/wiki/Software_prototyping), le développement formel, et l'[agile](https://en.wikipedia.org/wiki/Agile_software_development) sont toutes des méthodes.

Pourquoi se soucier des modèles du tout ? Parce que la mémoire de travail humaine est petite et les systèmes logiciels sont grands. Personne ne peut tenir un système de cent mille lignes en tête, donc nous dessinons des images et écrivons des abstractions qui montrent une facette à la fois : les données, le flux de contrôle, les états, les interactions. Un modèle n'est jamais censé être fidèle au code ; il est censé être adapté à une décision. Un bon modèle montre exactement ce dont vous avez besoin pour décider quelque chose, et cache tout le reste.

Sur les grandes équipes, les vrais enjeux sont la coordination et la communication. Quand des centaines d'ingénieurs, architectes, analystes, et auditeurs travaillent sur un système, les modèles partagés sont le terrain commun où ils négocient la conception, les exigences, et le risque. Alors pensez à la modélisation comme un outil avec un travail à faire. Elle se rembourse quand un modèle est moins cher que l'erreur qu'il prévient. Elle devient du gaspillage quand vous le dessinez pour lui-même, le gardez longtemps après qu'il soit devenu obsolète, ou l'élaborez au-delà de la décision qu'il était censé servir. La modélisation se connecte étroitement aux exigences logicielles (chapitre 2.8), aux principes de conception logicielle (chapitre 2.2), à l'architecture et ses notations comme C4 et arc42 (chapitre 3.1), et aux façons de travailler agiles (chapitre 10.7).

## Principes clés

- Chaque modèle a un but ; si vous ne pouvez pas nommer la décision qu'un modèle informe, ne le dessinez pas.
- L'abstraction est l'acte central de la modélisation : incluez ce qui compte pour le but, omettez le reste.
- La cohérence compte à l'intérieur et à travers les modèles ; des modèles contradictoires sont pires qu'aucun.
- Les modèles sont d'abord des artefacts de communication ; leur audience détermine leur notation et détail.
- Préférez le modèle le plus léger qui répond à la question ; l'élaboration a un coût de portage.
- Un modèle ne vaut que son analyse ; un modèle non vérifié est une hypothèse non testée.
- Choisissez la méthode selon l'incertitude, le risque, et la conséquence d'échec du problème.

## Recommandations

### Modélisez avec abstraction, but, et cohérence

Commencez chaque modèle en nommant son but et son audience. Puis abstrayez sans pitié vers ce but : un diagramme de séquence destiné à résoudre une condition de course devrait montrer le timing et les messages, pas chaque champ. Gardez vos modèles cohérents entre eux, afin que les entités dans un ERD, les classes dans un diagramme de classe, et les noms dans les exigences s'accordent tous, et cohérents avec la réalité, ce qui signifie que vous mettez à jour ou supprimez un modèle quand le système évolue. Un modèle obsolète auquel les gens font confiance est un danger. Un modèle obsolète que tout le monde ignore est du gaspillage qui coûte quand même de l'attention.

### Choisissez des modèles structurels ou comportementaux selon la question

Utilisez des modèles structurels pour montrer de quoi un système est fait et comment les parties se rapportent : diagrammes de classe, diagrammes de composants, et diagrammes entité-relation pour la structure de données. Utilisez des modèles comportementaux pour montrer ce qu'un système fait dans le temps : machines à états pour les objets avec des cycles de vie significatifs, diagrammes de séquence pour les interactions à travers les composants, et diagrammes d'activité pour les flux de travail et processus métier. Choisissez la notation unique qui expose la décision devant vous. La plupart des systèmes n'ont besoin que d'une poignée de types de diagrammes, dessinés sélectivement, pas le catalogue UML complet appliqué à tout.

### Analysez les modèles, ne les dessinez pas seulement

Un modèle mérite sa place à travers l'analyse, pas seulement le dessin. Vérifiez une machine à états pour les états inaccessibles, les transitions manquantes, et l'interblocage. Vérifiez un ERD pour les problèmes de normalisation et les relations orphelines. Parcourez un diagramme de séquence contre les exigences pour trouver les chemins d'erreur manquants. Révisez vos modèles avec les experts de domaine qui peuvent repérer ce qui est faux. Et là où le coût de l'échec est élevé, tendez la main vers l'analyse assistée par outil (vérificateurs de modèle, vérificateurs de cohérence, simulation) plutôt que de l'estimer à l'œil.

### Appliquez les méthodes heuristiques comme défaut

La plupart du logiciel est construit avec des méthodes heuristiques : des approches itératives fondées sur l'expérience qui utilisent les modèles informellement et jugent les résultats contre des attentes plutôt que des preuves. Pour la plupart des systèmes métier et gouvernementaux, c'est exactement juste : les exigences évoluent, et un défaut est généralement récupérable. Les méthodes heuristiques s'associent naturellement à l'agile (chapitre 10.7) : modélisez juste assez pour aligner l'équipe, puis construisez et apprenez.

### Réservez les méthodes formelles aux noyaux à haute conséquence

Les [méthodes formelles](https://en.wikipedia.org/wiki/Formal_methods) expriment les spécifications en mathématiques et utilisent la vérification, que ce soit la preuve ou la [vérification de modèle](https://en.wikipedia.org/wiki/Model_checking) exhaustive, pour établir des propriétés. Elles coûtent une vraie compétence et du temps, et elles se remboursent précisément là où l'échec est catastrophique ou irréversible : contrôle critique pour la sécurité, protocoles cryptographiques, noyaux de règlement financier, et similaires. Appliquez-les au petit noyau critique, pas au système entier. Et notez que la spécification formelle seule, même sans preuve complète, ajoute souvent de la valeur simplement en vous forçant à être précis.

### Utilisez le prototypage pour retirer l'incertitude

Quand les exigences ou la faisabilité sont floues, construisez un prototype pour apprendre, puis décidez, à dessein, s'il faut le faire évoluer ou l'abandonner. Les prototypes jetables explorent une question à bas coût et sont ensuite supprimés. Les prototypes évolutifs deviennent le produit et doivent être construits selon les normes de production. L'échec classique est de laisser un prototype jetable glisser en production par accident. Alors nommez le type du prototype avant de le construire.

### Faites correspondre la méthode au risque, pas à la mode

Choisissez les méthodes selon l'incertitude du problème et la conséquence de l'échec. Une haute incertitude favorise le prototypage et l'itération agile. Une haute conséquence favorise l'analyse formelle et la vérification rigoureuse. Un système avec les deux a besoin d'un noyau formel critique à l'intérieur d'une enveloppe autrement agile. Quoi que vous fassiez, n'adoptez pas une méthode juste parce qu'elle est prestigieuse ou parce qu'un fournisseur la vend.

## Compromis : avantages et inconvénients

| Modèle ou méthode | Bien appliqué | Mode d'échec |
|---|---|---|
| Modèles structurels (UML, ERD) | Image partagée des parties et des données | Prolifération de diagrammes ; dérive du code |
| Modèles comportementaux (état, séquence, activité) | Expose le timing, les états, et les cas limites | Diagrammes trop détaillés que personne ne lit |
| Méthodes heuristiques | Rapides, flexibles, conviennent à la plupart des systèmes | Indisciplinées ; hypothèses cachées |
| Méthodes formelles | Propriétés prouvables pour les noyaux critiques | Coût élevé ; mal appliquées au système entier |
| Prototypage | Apprentissage peu coûteux ; retire le risque tôt | Code jetable promu en production |
| Méthodes agiles | S'adapte aux exigences changeantes | Saute la modélisation nécessaire pour les problèmes difficiles |

La tension récurrente est entre la rigueur et la vitesse. Trop peu de modélisation livre des hypothèses cachées en production. Trop de modélisation brûle de l'effort sur des diagrammes qui n'informent jamais une décision et pourrissent au moment où le code change. Il n'y a pas de dose fixe qui corrige cela, seulement une règle de proportion : investissez dans un modèle ou une méthode en proportion de l'incertitude qu'il résout et du coût de se tromper sur la décision. Un moteur de paiements et un micro-site marketing méritent un traitement différent.

## Questions à discuter avec votre équipe

1. **Analysons-nous nos modèles, ou les dessinons-nous simplement et passons à autre chose ?** Un modèle mérite sa place à travers l'analyse, pas à travers l'existence : une machine à états que vous ne vérifiez jamais pour les états inaccessibles ou les transitions manquantes est une hypothèse non testée déguisée en diagramme. Sur une grande équipe, c'est là que se cachent les vrais défauts, parce qu'une image d'apparence plausible obtient la confiance précisément quand personne ne l'a parcourue contre les exigences pour trouver le chemin d'erreur manquant ou la relation orpheline. Apportez votre modèle comportemental le plus important à la réunion et essayez de le casser : quelle transition est indéfinie, quel état n'a pas de sortie, quelle séquence n'a pas de délai d'attente ? Là où le coût de l'échec est élevé, la réponse devrait vous pousser vers l'analyse assistée par outil (vérificateurs de modèle, vérificateurs de cohérence, simulation) plutôt que l'estimation à l'œil, parce que toute la raison de modéliser un noyau critique est de trouver le défaut sur un tableau blanc au lieu de production.

2. **Quand deux de nos modèles ne sont pas d'accord, lequel gagne, et qui remarque la contradiction ?** La cohérence compte à l'intérieur et à travers les modèles, et des modèles contradictoires sont pires qu'aucun, parce que les gens agissent sur les deux. Sur un grand système, les entités dans le modèle de données, les classes dans la conception, et les noms dans les exigences dérivent silencieusement à mesure que différentes équipes mettent à jour différents artefacts, et le premier signe est souvent un bug de production où deux composants n'étaient pas d'accord sur ce qu'était une chose. Apportez un exemple : choisissez un concept central et vérifiez si l'ERD, le code, et les exigences s'accordent réellement sur sa forme et son cycle de vie. Si non, décidez quel artefact fait autorité et qui est responsable de garder les autres synchronisés, et soyez prêts à supprimer un modèle plutôt que de laisser un obsolète continuer à mentir à l'équipe.

3. **Quel noyau dans notre système, s'il est faux, perd du vrai argent ou blesse quelqu'un, et obtient-il la rigueur qu'il mérite ?** Le mouvement central de ce chapitre est de faire correspondre la méthode au risque : méthodes heuristiques et agiles pour la majorité récupérable, spécification formelle et vérification pour le petit noyau à haute conséquence, et prototypage peu coûteux pour ce qui est réellement incertain. Les modes d'échec sont symétriques et tous deux coûteux : appliquer des méthodes formelles à un micro-site marketing brûle de l'argent, et traiter un moteur de règlement ou un ensemble de règles d'éligibilité comme du travail agile ordinaire invite le défaut catastrophique et irréversible. Apportez une carte de votre système et marquez où une erreur est catastrophique contre récupérable, et où les exigences sont certaines contre inconnues. La réponse devrait concentrer votre investissement de modélisation là où sont l'argent et l'ambiguïté, et le retenir explicitement partout ailleurs, afin qu'un noyau formel critique puisse siéger à l'intérieur d'une enveloppe autrement agile sans qu'aucune méthode ne fuite dans le territoire de l'autre.

4. **Combien de modélisation faisons-nous avant d'écrire du code, et cette dose change-t-elle avec l'incertitude devant nous ?** La grande conception en amont et l'absence totale de conception sont tous deux des modes d'échec, et la bonne dose se situe entre les deux, gouvernée par combien d'incertitude un modèle retire réellement. Sur une grande équipe, la pression va dans les deux sens : un processus de gouvernance peut exiger un ensemble complet de diagrammes avant tout code, verrouillant des décisions prises avec le moins d'information, tandis que la pression de livraison peut pousser une équipe à sauter l'unique machine à états qui aurait attrapé un cas limite coûteux. Apportez vos deux derniers projets et triez les modèles que vous avez produits entre ceux qui ont informé une vraie décision et ceux dessinés seulement parce qu'un modèle le demandait. Dans les programmes d'entreprise et gouvernementaux, où une porte de phase ou un comité d'approbation mandate souvent des documents en amont, venez prêts à argumenter pour une modélisation qui suit le risque plutôt qu'une liste de livrables fixe, afin que le noyau de paiements obtienne sa rigueur et que l'outil de reporting interne ne se noie pas dans des diagrammes que personne ne lit.

5. **Avons-nous convenu d'une notation partagée et d'un foyer unique pour nos modèles, ou chaque équipe invente-t-elle le sien ?** Les modèles sont d'abord des artefacts de communication, et leur valeur s'effondre quand une machine à états dessinée dans l'outil d'une équipe ne peut pas être lue, trouvée, ou fiable par l'équipe qui en hérite. Pour des centaines d'ingénieurs, les considérations concurrentes sont réelles : une notation et un dépôt mandatés achètent la cohérence et la repérabilité, mais ils imposent aussi un coût d'apprentissage et peuvent pousser les gens vers des outils lourds quand un tableau blanc photographié suffirait. Apportez des exemples d'où un modèle a réellement vécu (un wiki, un outil de diagramme, un jeu de diapositives, l'ordinateur portable de quelqu'un) et demandez qui pourrait le trouver et le comprendre six mois plus tard. Dans les contextes d'entreprise et réglementés, l'angle d'audit aiguise cela : un auditeur qui ne peut pas localiser le modèle de données actuel ou tracer une décision jusqu'à une machine à états documentée traitera le système comme non documenté, donc convenez d'une petite notation partagée et d'un emplacement durable, et acceptez la capture légère plutôt que la cérémonie partout où la conséquence est faible.

6. **Avant de construire un prototype, décidons-nous à dessein s'il est jetable ou évolutif, et nous tenons-nous à ce choix ?** L'échec classique et coûteux est un prototype jetable qui glisse silencieusement en production parce qu'il a bien démontré et que personne n'a nommé son type en amont. La tension est authentique : les prototypes jetables achètent l'apprentissage le moins cher possible et devraient être supprimés, tandis que les prototypes évolutifs deviennent le produit et doivent être construits selon les normes de production dès la première ligne, et confondre les deux gaspille soit des reprises soit livre du code fragile dans un rôle pour lequel il n'a jamais été conçu. Apportez un prototype récent et demandez ce qui a été décidé avant qu'il ne soit construit, qui avait l'autorité de le promouvoir ou l'abandonner, et si cette décision a survécu à la pression de livraison. Au gouvernement et dans d'autres contextes responsables, où un système face aux citoyens porte des obligations de transparence et de fiabilité, traitez la promotion accidentelle comme un échec de contrôle : fixez le destin du prototype à l'avance, et faites d'abandonner un jetable réussi un résultat célébré plutôt qu'un gaspillage à éviter.

## Regard sectoriel

**Jeune pousse.** Modélisez sur un tableau blanc, photographiez-le, et avancez. Votre ressource la plus rare est l'attention d'ingénierie, alors tendez la main vers un modèle seulement quand il est moins cher que l'erreur qu'il prévient : une machine à états d'abonnement avant de coder les cas limites de facturation, pas un catalogue UML complet pour un produit qui pourrait pivoter le mois prochain. Restez heuristique et agile, gardez les méthodes formelles entièrement hors de la table, et traitez chaque prototype comme jetable sauf décision consciente contraire.

**Petite entreprise.** Vous n'avez probablement personne dont le travail est la modélisation formelle, alors appuyez-vous sur les modèles déjà intégrés dans les outils et cadres que vous achetez plutôt que de monter votre propre pratique de modélisation. Cadrez les quelques modèles que vous dessinez réellement autour de décisions concrètes : une simple esquisse de modèle de données pour convenir quelles données client vous détenez, un diagramme d'état pour l'unique flux de travail qui vous fait perdre un client quand il casse. Préférez un produit acheté avec un modèle de données éprouvé plutôt que de construire et documenter le vôtre, et gardez tout ce que vous dessinez assez léger pour qu'une personne puisse le maintenir.

**Grande entreprise.** Le problème central est la coordination à travers de nombreuses équipes, donc les modèles partagés deviennent le terrain commun : un modèle de données convenu, une notation cohérente, et un foyer où l'ERD, les diagrammes C4, et les machines à états peuvent être trouvés et fiables. Standardisez une petite notation et appliquez la cohérence afin que les entités dans les exigences, la conception, et la base de données ne dérivent pas entre équipes. Réservez la spécification formelle et la vérification de modèle aux noyaux à haute conséquence (règlement, réconciliation, contrôle d'accès), financez la compétence spécialisée que cela exige, et gardez une piste d'audit de chaque modèle documenté jusqu'à la décision qu'il a justifiée.

**Gouvernement.** Les règles fixées par la loi doivent être traçables au statut, ce qui est là où la spécification formelle mérite son coût : spécifiez la logique d'éligibilité ou d'évaluation précisément, vérifiez les propriétés clés, et laissez les auditeurs tracer chaque résultat jusqu'à la règle qui l'a produit. Les marchés publics ajoutent leur propre poids, puisque les documents et modèles sont souvent des livrables contractuels, alors convenez lesquels sont réellement porteurs de décision plutôt que produits seulement pour satisfaire une liste de contrôle. Publiez des descriptions en langage simple de comment les systèmes conséquents fonctionnent, et utilisez le prototypage jetable pour tester l'accueil face aux citoyens avec de vrais utilisateurs avant de s'engager sur une construction de production.

## Exemples

**Jeune pousse.** Une petite start-up construisant un produit de facturation par abonnement esquisse le cycle de vie de l'abonnement (essai, actif, en retard, annulé, réactivé) comme une machine à états sur un tableau blanc avant d'écrire du code. En parcourant le diagramme, ils remarquent qu'ils n'ont jamais défini ce qui arrive quand le paiement d'un compte en retard s'acquitte finalement, un cas limite qui aurait bloqué de vrais clients dans les limbes. Ce modèle de cinq minutes économise un mal de tête de production, et ils le photographient plutôt que de maintenir un outil de diagramme lourd. Partout ailleurs, ils restent agiles et modélisent juste assez pour aligner, parce qu'à leur échelle un défaut est récupérable et les méthodes formelles seraient un coût pur.

**Grande entreprise.** Une banque mondiale construit une nouvelle plateforme de paiements. L'équipe utilise un diagramme entité-relation pour convenir du modèle de données partagé à travers les équipes de comptes, de grand livre, et de messagerie, et des diagrammes C4 (chapitre 3.1) pour montrer comment les services s'assemblent. Ils modélisent le cycle de vie de la transaction (en attente, effacé, réglé, inversé, contesté) comme une machine à états explicite, et l'analyse révèle qu'il manque une transition pour les inversions partielles. La lacune est corrigée sur un tableau blanc plutôt qu'en production. Les diagrammes de séquence parcourent le flux de règlement contre les exigences (chapitre 2.8) pour faire surgir les chemins de délai d'attente et de nouvelle tentative manquants. La livraison quotidienne est agile, mais l'algorithme central de réconciliation, où une erreur signifie de l'argent réel perdu, obtient une spécification formelle et est vérifié par modèle avant l'implémentation. La modélisation est concentrée là où sont l'argent et l'ambiguïté, et gardée légère partout ailleurs.

**Gouvernement.** Une agence fiscale nationale modernise l'évaluation des prestations. Parce que les règles d'éligibilité sont fixées par la loi et auditées, l'équipe écrit une spécification formelle des règles comme des transformations pures et vérifie des propriétés clés, comme aucun demandeur n'étant à la fois éligible et inéligible et chaque cas atteignant une décision, afin que les auditeurs puissent tracer les résultats jusqu'au statut. Aux côtés du noyau formel, l'équipe construit un prototype jetable du formulaire d'accueil face aux citoyens pour tester avec de vrais utilisateurs. Ils apprennent qu'un assistant multi-étapes réduit les erreurs, puis abandonnent le prototype et reconstruisent l'accueil selon les normes de production. Les diagrammes d'activité documentent le processus de travailleur social de bout en bout pour la formation et l'audit. Les règles à haute conséquence obtiennent la rigueur formelle ; l'expérience utilisateur incertaine obtient le prototypage peu coûteux ; aucune méthode n'est appliquée là où l'autre appartient.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur la modélisation vient de trouver les défauts plus tôt, où ils sont bien moins chers à corriger. Une contradiction trouvée sur un tableau blanc coûte des minutes. La même contradiction trouvée en production peut coûter une panne, un programme de reprises, ou, dans les domaines réglementés, une responsabilité légale. Les modèles abaissent aussi le coût total de possession en servant de communication durable. Un système qui survit à ses auteurs, le cas normal en entreprise et au gouvernement, est bien moins cher à maintenir quand son modèle de données, ses machines à états, et ses flux clés sont documentés précisément.

Les coûts sont réels, et vous devez les peser. Les modèles prennent du temps à construire, de la compétence pour bien construire, et un effort continu pour rester à jour ; les méthodes formelles ajoutent du travail spécialisé. Le point d'équilibre est gouverné par l'incertitude et la conséquence. Là où les deux sont faibles, une modélisation lourde détruit de la valeur et les heuristiques agiles gagnent. Là où l'un ou l'autre est élevé, la modélisation ciblée, et, pour le noyau critique, la vérification formelle, se rembourse plusieurs fois en prévenant la classe d'échec coûteuse. Pour convaincre la direction, liez l'investissement de modélisation à des risques spécifiques retirés et à la maintenabilité des systèmes à longue durée de vie. Et suivez si les modèles sont réellement consultés, parce qu'un modèle inutilisé est un coût pur.

## Anti-patterns et pièges

- **Modéliser pour soi-même :** produire des diagrammes parce qu'un processus l'exige, pas parce qu'ils informent une décision.
- **Les modèles obsolètes fiables comme vérité :** des diagrammes qui ne correspondent plus au code mais sur lesquels on compte encore.
- **La grande conception en amont :** des modèles exhaustifs produits avant tout code, verrouillant des décisions prises avec le moins d'information.
- **La prolifération de diagrammes :** chaque type UML appliqué uniformément, noyant les quelques vues utiles dans le bruit.
- **Les méthodes formelles partout :** appliquer une vérification coûteuse à du code où la conséquence de l'échec ne la justifie pas.
- **La promotion accidentelle de prototype :** un prototype jetable silencieusement livré comme le produit.
- **La notation avant la substance :** débattre de la correction UML au lieu de si le modèle répond à la question.

## Modèle de maturité

- **Niveau 1 (Initiation) :** La modélisation est ad hoc ou absente et purement réactive ; aucune méthode n'est nommée ; les modèles, quand ils sont dessinés du tout, sont incohérents, non analysés, et abandonnés dès que la réunion se termine.
- **Niveau 2 (Développement) :** Certaines équipes dessinent des diagrammes communs et suivent une méthode nommée, mais la pratique est inégale à travers l'organisation : les modèles sont souvent produits cérémonieusement, dérivent du code, et sont rarement analysés pour les défauts.
- **Niveau 3 (Standardisation) :** Une notation partagée, un guide documenté de sélection de méthode, et des règles de cohérence sont définis et appliqués à l'échelle de l'organisation ; les modèles sont choisis par but, gardés synchronisés avec le système, révisés pour les défauts, et la méthode est adaptée au risque de chaque problème.
- **Niveau 4 (Gestion) :** La modélisation est mesurée et contrôlée par rapport à des références ; les équipes suivent combien de défauts l'analyse attrape avant l'implémentation, à quel point les modèles dérivent du code, si chaque modèle a été réellement consulté pour une vraie décision, et les reprises et le temps de cycle économisés par rapport à une référence définie ; le choix de méthode est calibré à l'incertitude et la conséquence mesurées, et les noyaux critiques sont formellement vérifiés contre des cibles de couverture convenues.
- **Niveau 5 (Orchestration) :** La modélisation et la sélection de méthode sont continuellement améliorées et intégrées à la planification de livraison et de risque à travers l'organisation ; l'investissement s'adapte à mesure que l'incertitude et la conséquence changent, les modèles sont routinièrement gardés à jour, retirés, ou approfondis sur preuve, et les méthodes formelles, heuristiques, et de prototypage sont composées afin que chacune siège exactement là où elle se rembourse.

## Pistes de réflexion

- Pour votre dernier projet, quels modèles ont informé une vraie décision, et lesquels ont été dessinés seulement parce qu'un processus l'exigeait ?
- Où dans vos systèmes une spécification formelle se rembourserait-elle, et où serait-elle du gaspillage ?
- Comment décidez-vous si un prototype est jetable ou évolutif, et appliquez-vous cette décision ?
- Comment empêchez-vous les modèles de dériver hors de synchronisation avec le code, ou acceptez-vous que certains devraient être supprimés à la place ?
- Quelle est la bonne quantité de modélisation avant le code dans votre contexte, et comment change-t-elle avec l'incertitude ?
- Quel modèle comportemental (état, séquence, ou activité) aurait attrapé votre incident de production le plus récent ?

## Points clés à retenir

- Un modèle est une abstraction intentionnelle ; si vous ne pouvez pas nommer la décision qu'il informe, ne le dessinez pas.
- Faites correspondre les modèles structurels et comportementaux à la question spécifique, et gardez-les cohérents et à jour.
- Analysez les modèles ; un modèle non vérifié est une hypothèse non testée.
- Les méthodes heuristiques et agiles conviennent à la plupart des systèmes ; réservez les méthodes formelles aux noyaux à haute conséquence.
- Utilisez des prototypes pour retirer l'incertitude, et décidez en amont s'ils sont jetables ou évolutifs.
- Investissez dans la modélisation en proportion de l'incertitude qu'elle résout et du coût de se tromper sur la décision.

## Références et lectures complémentaires

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, domaine de connaissance Modèles et Méthodes d'Ingénierie Logicielle
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modeling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modeling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* et *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (le langage de modélisation Alloy)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (le modèle C4)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
