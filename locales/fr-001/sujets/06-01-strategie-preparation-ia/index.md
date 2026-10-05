# 6.1 Stratégie et préparation à l'IA

## Vue d'ensemble et motivation

L'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) est passée d'une nouveauté de recherche à une capacité centrale que les grandes organisations sont maintenant censées déployer de façon responsable et à l'échelle. Pour les entreprises et agences gouvernementales, la vraie question n'est plus si l'IA peut faire quelque chose d'impressionnant dans une démonstration. C'est si un investissement spécifique résout un vrai problème mieux que les alternatives, peut être exploité en sécurité pendant des années, et peut survivre à l'audit, l'approvisionnement, et l'examen public. La stratégie d'IA est la discipline de décider où appliquer l'IA, où l'éviter, et quelles fondations vous avez besoin avant que le premier modèle n'atteigne la production.

Pour les grandes équipes, l'échelle et l'inertie élèvent les enjeux. Une initiative mal cadrée peut brûler des budgets, distraire des ingénieurs talentueux, et éroder la confiance avec les régulateurs et citoyens quand elle échoue publiquement. Une bien choisie peut automatiser la corvée, faire émerger de la perspicacité depuis des données que vous n'auriez jamais pu atteindre auparavant, et libérer des personnes qualifiées pour du travail à plus haute valeur. La différence est rarement le modèle lui-même. Cela dépend de la qualité avec laquelle vous cadrez le problème, de la préparation de vos données et talent, et de l'honnêteté de votre argumentaire économique.

L'administration publique et les contextes régulés ajoutent plus de contraintes. Les organismes publics doivent justifier les dépenses, garantir la transparence, éviter la discrimination illégale, et rester responsables devant les élus et le public. Les règles d'approvisionnement peuvent interdire le verrouillage à source unique, exiger l'explicabilité, et exiger que les fournisseurs exposent le comportement du modèle. Ici, traitez la conformité, l'auditabilité, et les options de sortie comme des exigences de première classe, pas des pensées après coup.

## Principes clés

- Commencez par un problème qui vaut la peine d'être résolu, pas par une technologie cherchant un usage.
- Préférez l'approche la plus simple qui satisfait le besoin ; l'IA est une option parmi d'autres, et souvent pas la meilleure.
- Traitez la préparation des données, le talent, et la maturité de plateforme comme des prérequis, pas des flux de travail parallèles à régler plus tard.
- Prenez des décisions construire-contre-acheter explicitement et révisez-les à mesure que le marché et vos capacités changent.
- Quantifiez le coût total de possession, incluant l'opération, la surveillance, et le remplacement éventuel, pas seulement la licence ou le pilote.
- Concevez pour la sortie dès le premier jour : évitez les architectures qui rendent changer de fournisseur ou de modèle prohibitivement coûteux.
- Dans les contextes régulés et publics, traitez la transparence, la conformité d'approvisionnement, et la responsabilité comme des contraintes de conception.
- Mesurez le coût de *ne pas* agir aux côtés du coût d'agir.

## Recommandations

### Cadrer le problème avant de choisir une technologie

Écrivez un énoncé de problème d'une page. Nommez la décision ou tâche que vous voulez améliorer, la référence actuelle, le résultat mesurable que vous voulez, et ce qui se passe quand le système se trompe. Puis demandez si le problème convient même à l'IA. Y a-t-il assez de données pertinentes ? La tâche est-elle basée sur des motifs plutôt que des règles ? Pouvez-vous tolérer des réponses probabilistes ? Un humain peut-il vérifier la sortie ? De nombreux problèmes sont mieux résolus avec du logiciel déterministe, une meilleure conception de processus, ou simplement une meilleure hygiène de données. Écrivez explicitement où l'IA n'est *pas* un bon ajustement : par exemple, des décisions qui doivent être parfaitement explicables par la loi, ou où le coût d'une erreur rare est catastrophique et impossible à attraper.

### Utiliser un arbre de décision construire-contre-acheter-contre-affiner-contre-inviter

Bougez du moins cher et plus rapide vers le plus coûteux et plus contrôlé :

1. **Inviter un modèle hébergé existant.** Si un modèle à usage général (tel que Claude d'Anthropic, ou des offres comparables d'autres fournisseurs) résout le problème avec une invitation soignée et de la récupération, faites cela en premier. Coût le plus bas, itération la plus rapide, aucune infrastructure d'entraînement.
2. **Augmenter avec de la récupération ou des outils.** Si la lacune est de la connaissance ou des actions, ajoutez la [génération augmentée par récupération](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_augment%C3%A9e_de_r%C3%A9cup%C3%A9ration) (RAG), qui va chercher des documents pertinents au moment de la requête et les fournit au modèle comme contexte, et l'usage d'outils avant de toucher aux poids du modèle.
3. **Affiner ou adapter.** Si l'invitation ne peut pas atteindre la précision, le ton, ou le format nécessaires de façon cohérente, [affinez](https://fr.wikipedia.org/wiki/Fine-tuning) un plus petit modèle sur vos données : c'est-à-dire, entraînez davantage un modèle pré-entraîné sur vos exemples pour le spécialiser. Cela achète du contrôle au coût d'un pipeline [MLOps](https://fr.wikipedia.org/wiki/MLOps) (opérations d'apprentissage automatique).
4. **Acheter un produit spécialisé.** Pour des domaines bien définis (traitement de document, notation de fraude), un produit de fournisseur mature peut battre tout ce que vous construisez.
5. **Construire depuis zéro.** Réservez l'entraînement de [modèles de fondation](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_fondation) (grands modèles pré-entraînés sur des données larges et adaptables à de nombreuses tâches) aux organisations avec des données uniques, un talent profond, et des raisons stratégiques. Pour presque toutes les entreprises et agences, c'est le mauvais choix.

### Établir les prérequis de données, talent, et plateforme

Auditez vos données pour la disponibilité, la qualité, l'étiquetage, la lignée, et la base légale d'usage. Confirmez que vous avez réellement le droit de les utiliser pour l'IA, incluant toute donnée personnelle ou tierce. Évaluez le talent honnêtement : vous avez besoin de data scientists, et aussi d'ingénieurs ML, d'ingénieurs de données, de chefs de produit qui comprennent les systèmes probabilistes, et de relecteurs qui peuvent évaluer les sorties. Avant de passer à l'échelle, montez une référence de plateforme : suivi d'expérience, un registre de modèle (le système d'enregistrement pour les versions de modèle entraîné et leur statut d'approbation), surveillance, et service sécurisé, pour que chaque nouveau cas d'usage ne réinvente pas les opérations.

### Gérer délibérément les contextes régulés et gouvernementaux

Impliquez tôt l'approvisionnement, le juridique, et les équipes de risque. Exigez que les fournisseurs divulguent la provenance du modèle, les pratiques de données d'entraînement, les résultats d'évaluation, et les limitations connues. Préférez les contrats qui accordent la portabilité de vos données et prompts, et évitez les formats propriétaires qui vous piègent. Où approprié, publiez le but et les garde-fous des systèmes d'IA orientés public, et donnez aux gens un canal pour contester les décisions automatisées. Alignez-vous sur des cadres reconnus (voir chapitre 6.5) pour que les audits trouvent un processus documenté et défendable.

### Calculer le coût total de possession et se prémunir contre le verrouillage

Modélisez le coût de cycle de vie complet : inférence ou licensing, pipelines de données, revue humaine, surveillance, réentraînement, réponse d'incident, et mise hors service. Comparez-le au coût du statu quo et des alternatives. Réduisez le verrouillage en plaçant le modèle derrière une interface interne, en gardant les prompts et jeux de données d'évaluation portables, et en testant un deuxième fournisseur de temps en temps.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients | Le mieux quand |
|---|---|---|---|
| Inviter un modèle hébergé | Rapide, bon marché, pas d'infra, facile à changer | Moins de contrôle, coût par appel, questions de partage de données | Prototypes, tâches larges, exigences incertaines |
| Augmentation par récupération | Ancre les réponses dans vos données, mise à jour | La qualité de récupération est difficile, ajoute de l'infra | Tâches riches en connaissance |
| Affiner un plus petit modèle | Contrôle, coût par appel plus bas à l'échelle, option sur site | Exige MLOps, données, et entretien | Tâches stables, à haut volume, spécialisées |
| Acheter un produit | Éprouvé, soutenu, rapide vers la valeur | Coût de licence, verrouillage, ajustement limité | Problèmes de commodité bien définis |
| Construire un modèle de fondation | Contrôle et différenciation maximaux | Coût énorme, talent rare, risque élevé | Presque jamais, en dehors des laboratoires de pointe |

Le compromis dominant est le contrôle contre le coût et la vitesse. L'invitation vous donne le plus de vitesse et de flexibilité mais le moins de contrôle ; construire vous donne le plus de contrôle mais exige des ressources que peu d'organisations devraient dépenser. La plupart des grandes équipes devraient vivre au milieu : inviter et récupérer d'abord, affiner sélectivement, et acheter pour les besoins de commodité. Le verrouillage échange la commodité à court terme contre le risque à long terme, et cela compte spécialement dans l'administration publique, où les obligations de sortie pluriannuelles sont courantes.

## Questions à discuter avec votre équipe

1. **Où chacun de nos trois premiers cas d'usage candidats se trouve-t-il sur l'échelle inviter-puis-récupérer-puis-affiner-puis-acheter-puis-construire, et quelle preuve le déplacerait d'un échelon ?** Cela compte parce que la plupart des dépenses d'IA gaspillées viennent de commencer à un échelon trop haut : entraîner un modèle alors qu'une invitation soignée aurait fonctionné. Pour une grande équipe, convenir de l'échelle comme valeur par défaut partagée empêche chaque groupe de réinventer un pipeline coûteux. Apportez l'énoncé de problème d'une page pour chaque candidat, la référence actuelle, et une lecture honnête de si la lacune est la connaissance (récupération), la cohérence (affinage), ou une commodité résolue (achat). Dans les contextes d'entreprise et gouvernementaux, ajoutez le coût d'approvisionnement et d'audit de chaque échelon, puisqu'un modèle affiné traîne un fardeau MLOps qu'un appel hébergé n'a pas. La réponse devrait vous permettre de tuer ou déclasser au moins un projet sur-cadré dans la pièce.

2. **Quel est notre plan de sortie concret pour le fournisseur ou modèle dont nous dépendons le plus, et l'avons-nous réellement testé ?** Le verrouillage est bon marché à accepter et coûteux à défaire, et dans l'administration publique vous pouvez porter des obligations de sortie pluriannuelles que vous ne pouvez pas satisfaire si vous ne les avez jamais répétées. Apportez la liste des fonctionnalités propriétaires sur lesquelles vous comptez, si les prompts et jeux de données d'évaluation sont portables, et comment le modèle se trouve derrière une interface interne (ou pas). Le signal à surveiller est si quelqu'un a déjà exécuté votre suite d'évaluation contre un deuxième fournisseur ; sinon, votre plan de sortie est un espoir, pas un plan. Si la réponse honnête est que changer prendrait des mois et réécrirait du code central, traitez cela comme un défaut de conception à corriger maintenant, pas un pont à traverser plus tard.

3. **Que dit une fiche de préparation honnête sur nos droits de données, et quels cas d'usage disqualifie-t-elle aujourd'hui ?** Sauter la préparation des données est l'échec qui coule discrètement les pilotes : le modèle fonctionne, mais vous n'avez jamais eu la base légale pour utiliser les données, ou elles ne sont ni étiquetées ni tracées. Pour une grande organisation, les données personnelles et tierces soulèvent des limites de consentement et contractuelles qui varient par juridiction et par jeu de données. Apportez un audit de la disponibilité, qualité, étiquetage, lignée, et base légale pour chaque candidat, et soyez prêt à marquer certains cas d'usage comme bloqués jusqu'à ce que les fondations de données existent. Dans les contextes régulés et publics, une base légale inutilisable n'est pas un délai, c'est un arrêt dur, et financer le travail de préparation devrait être une ligne explicite dans le plan plutôt qu'une pensée après coup.

4. **Comment saurons-nous si un cas d'usage d'IA en direct fonctionne réellement, et quelle preuve nous ferait le tuer ?** La plupart des portefeuilles d'IA accumulent des zombies : des pilotes qui ont été livrés, ont impressionné quelqu'un, et maintenant fonctionnent pour toujours sans que personne ne vérifie s'ils gagnent encore leur coût. Convenez de la référence et de la métrique de succès avant le lancement, puis fixez un seuil de mort explicite, pour que la décision d'arrêter soit prise à l'avance plutôt que défendue sur le moment. Apportez la métrique actuelle, le coût de surveillance humaine par résultat, et la dérive que vous avez vue depuis le lancement. Pour les portefeuilles d'entreprise et gouvernementaux, nommez qui révise chaque système selon une cadence fixe et qui détient l'autorité de le retirer ; un cas d'usage dont personne n'est responsable de la révision est un dont personne n'éteindra jamais.

5. **Où un humain reste-t-il dans la boucle, combien coûte cette surveillance, et l'avons-nous réellement budgétisée ?** Les cas d'usage d'IA qui paraissent les moins chers sont ceux qui supposent discrètement une automatisation complète, puis fuient du coût à travers la revue, correction, et escalade que la réalité force à revenir. Décidez délibérément quelles décisions une personne doit confirmer, lesquelles le modèle peut prendre seul, et lesquelles il ne peut jamais prendre, puis évaluez le temps humain que cela implique. Apportez le volume de cas à faible confiance, le coût d'une mauvaise réponse, et le chemin d'escalade actuel. Dans les contextes régulés et publics, liez chaque décision automatisée à un fonctionnaire responsable et une voie d'appel, parce qu'une surveillance que vous ne pouvez pas décrire est une surveillance que vous n'avez pas.

6. **Avons-nous le talent et la plateforme pour exécuter ce que nous proposons, ou supposons-nous discrètement une capacité qui nous manque ?** Les plans d'IA ambitieux échouent moins sur le modèle que sur les fondations peu glamour : personne pour maintenir le pipeline, personne qui peut évaluer les sorties, aucune plateforme sur laquelle déployer. Assortissez chaque cas d'usage candidat aux compétences et infrastructure dont il a réellement besoin, et soyez honnête sur si la lacune est une embauche, un partenaire, ou une raison de ne pas construire. Apportez un inventaire de qui peut posséder chaque système en production, sur quelle plateforme il s'exécutera, et quelles capacités vous devrez acheter. Pour une grande organisation ou publique, ajoutez les délais d'approvisionnement et d'embauche, puisqu'un plan qui dépend d'un talent que vous ne pouvez pas recruter dans la fenêtre pertinente est un plan de sous-livraison.

## Regard sectoriel

**Jeune pousse.** La vitesse et la survie dominent. Choisissez un seul cas d'usage étroit qui touche votre valeur centrale, livrez-le sur un modèle hébergé derrière une interface mince, et plafonnez fermement les dépenses. Évitez de construire de l'infrastructure ou d'entraîner des modèles : votre ressource la plus rare est l'attention d'ingénierie, et un pipeline affiné que vous ne pouvez pas maintenir est un passif, pas un fossé défensif. Gardez le changement bon marché pour pouvoir suivre un marché qui bouge vite.

**Petite entreprise.** Vous n'avez probablement pas de data scientists et avez un budget serré, donc traitez l'IA comme quelque chose que vous achetez intégré dans des outils que vous utilisez déjà, pas un programme que vous dotez. Cadrez la préparation comme une question d'hygiène de données et de confidentialité plutôt qu'un projet d'apprentissage automatique : sachez quelles données client vous détenez, ce que vous êtes autorisé à en faire, et où une mauvaise réponse automatisée vous coûterait un client. Préférez les fournisseurs qui rendent l'IA optionnelle, transparente, et facile à désactiver.

**Grande entreprise.** Le problème est la gouvernance de portefeuille à travers de nombreuses équipes : une échelle construire-contre-acheter partagée, des évaluations de préparation cohérentes, et une analyse de verrouillage et coût total pour que les groupes arrêtent de réinventer des pipelines coûteux. Budgétisez explicitement le fardeau MLOps et de surveillance humaine, standardisez la couche d'interface pour que les fournisseurs restent interchangeables, et gérez les cas d'usage d'IA comme un portefeuille avec des métriques claires et des critères de mort plutôt qu'une dispersion de pilotes.

**Gouvernement.** La transparence, les règles d'approvisionnement, et la responsabilité façonnent chaque choix. Favorisez les systèmes qui citent des sources officielles plutôt que de générer de la politique, gardez un humain responsable pour les décisions conséquentes, et exigez la portabilité de données et la divulgation des limitations de modèle dans les contrats. Publiez une description en langage clair et une voie d'appel, honorez toute obligation de sortie pluriannuelle que vous signez, et gardez l'IA hors des décisions d'évaluation finale qui doivent reposer sur un fonctionnaire responsable.

## Exemples

**Jeune pousse.** Une jeune pousse de planification de cinq personnes voulait ajouter une fonctionnalité en langage naturel « réservez-moi une réunion » sans retirer ses deux ingénieurs du produit central. Elle a choisi le plus petit problème qui comptait, analyser une demande en un horaire proposé, et l'a livré avec un modèle hébergé derrière une API interne mince pour pouvoir changer de fournisseur plus tard. L'équipe a fixé un plafond de dépense mensuel dur, suivi si les utilisateurs acceptaient les horaires suggérés, et convenu de revisiter un modèle affiné seulement si le volume justifiait jamais le travail supplémentaire.

**Grande entreprise.** Un assureur multinational voulait accélérer le triage de réclamations. Au lieu d'entraîner un modèle sur mesure, il a cadré le problème étroitement (acheminer et résumer les réclamations entrantes), prototypé avec un modèle hébergé plus de la récupération sur ses documents de police, et mesuré contre le temps de traitement humain et la précision. Seulement après avoir prouvé la valeur a-t-il affiné un plus petit modèle pour le type de réclamation à plus haut volume pour réduire le coût par appel. Il a gardé le modèle derrière une API interne pour pouvoir échanger de fournisseurs, et a modélisé un coût total de possession sur trois ans qui incluait la revue humaine des cas à faible confiance.

**Gouvernement.** Une administration fiscale nationale a considéré un assistant IA pour aider le personnel à répondre aux requêtes citoyennes. Parce que ces réponses touchaient des obligations légales, l'agence a insisté sur la transparence : le système ne pouvait faire émerger que la directive officielle avec des citations, jamais inventer de politique, et un humain révisait chaque suggestion automatisée avant qu'elle ne sorte. L'approvisionnement exigeait que le fournisseur divulgue les limitations de modèle et accorde la portabilité de données, et l'agence a publié une description en langage clair du système et une voie d'appel. Elle a gardé l'IA entièrement hors des décisions d'évaluation finale, les réservant aux fonctionnaires responsables.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La stratégie d'IA existe pour vous aider à éviter deux échecs miroirs : sur-investir dans une IA qui ne rapporte jamais, et sous-investir pendant que des concurrents ou agences pairs prennent de l'avance. Le retour sur investissement vient du travail économisé, du temps de cycle réduit, des taux d'erreur abaissés, et de nouvelles capacités permises. Mesurez ceux-ci contre une vraie référence, et actualisez pour le vrai coût de surveillance humaine, qui disparaît rarement.

Le coût total de possession doit inclure les postes budgétaires peu glamour : pipelines de données, surveillance, réentraînement à mesure que le monde dérive, revue de sécurité, et mise hors service éventuelle. Un pilote qui paraît bon marché peut devenir coûteux une fois qu'il fonctionne à l'échelle pendant des années. Présentez aussi le coût de *ne pas* adopter : service plus lent, coût manuel plus élevé, et dérive stratégique. Faites valoir cela auprès de la direction avec une vue de portefeuille : quelques paris à haute confiance, des métriques de succès claires, des critères de mort pour les échecs, et une évaluation de préparation montrant que les fondations de données et talent existent. Demandez aux leaders de financer la préparation explicitement ; sautez-la, et vous garantissez un retravail coûteux.

## Anti-patterns et pièges

- **Solution en quête de problème.** Acheter de l'IA parce que des pairs l'ont fait, puis chasser un cas d'usage.
- **Sauter la préparation des données.** Lancer des modèles sur des données indisponibles, non étiquetées, ou légalement inutilisables.
- **Décisions pilotées par la démonstration.** S'engager basé sur une démonstration polie sans évaluation de qualité de production.
- **Ignorer la boucle humaine.** Supposer une automatisation complète et sous-budgétiser la revue, qui est là où se cache la plupart du coût.
- **Verrouillage silencieux.** Construire profondément sur les fonctionnalités propriétaires d'un fournisseur sans plan de sortie.
- **Sous-estimer les opérations.** Traiter le déploiement comme la ligne d'arrivée plutôt que le début d'une obligation de maintenance.
- **Conformité comme pensée après coup.** Rétro-adapter la transparence et l'auditabilité après la conception, à des multiples du coût.

## Modèle de maturité

1. **Initier.** Expériences au coup par coup, aucune stratégie partagée, décisions pilotées par le battage et l'enthousiasme individuel.
2. **Développer.** Le cadrage de problème existe pour certains projets ; une première référence de plateforme apparaît ; construire-contre-acheter est discuté mais incohérent.
3. **Standardiser.** Un portefeuille de cas d'usage d'IA avec des métriques claires, un arbre de décision documenté, des évaluations de préparation, et une analyse de verrouillage et coût total, appliqué de façon cohérente à travers les équipes.
4. **Gérer.** Le portefeuille est mesuré : la préparation, le retour sur investissement, le coût total, et le coût de surveillance humaine sont suivis contre des références ; les critères de mort sont imposés sur preuve ; l'impact de livraison et de qualité pilote chaque décision de feu vert ou non.
5. **Orchestrer.** La stratégie d'IA est intégrée à la planification d'affaires et de risque ; la préparation est continuellement maintenue ; l'organisation retire, remplace, et recadre routinièrement les systèmes d'IA basé sur la preuve, rééquilibrant le portefeuille à mesure que le marché et le paysage de risque changent.

## Pistes de réflexion

- Comment décidez-vous quand un problème est véritablement inadapté à l'IA, et qui a l'autorité de dire non ?
- Quel seuil de préparation devrait conditionner un projet du pilote à la production ?
- Combien de verrouillage est acceptable en échange d'un temps de mise en valeur plus rapide ?
- Dans l'administration publique, comment les obligations de transparence devraient-elles façonner le choix construire-contre-acheter ?
- Comment gardez-vous les estimations de coût total honnêtes quand les fournisseurs et enthousiastes ont des incitations à les sous-estimer ?
- Qui possède le portefeuille d'IA, et comment les décisions de mort sont-elles prises ?

## Points clés à retenir

- La stratégie commence par un vrai problème et une référence honnête, pas par une technologie.
- Préférez l'option la plus simple : invitez, puis récupérez, puis affinez, puis achetez, et rarement construisez depuis zéro.
- La préparation des données, du talent, et de la plateforme sont des prérequis ; les financer fait partie du plan.
- Les contextes régulés et gouvernementaux exigent la transparence, la conformité d'approvisionnement, et des options de sortie par conception.
- Modélisez le coût total complet et le coût de l'inaction, et prémunissez-vous contre le verrouillage de fournisseur dès la première décision d'architecture.

## Références et lectures complémentaires

- Ajay Agrawal, Joshua Gans, et Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
