# 11.3 La théorie des files d'attente

## Vue d'ensemble et motivation

La **[théorie des files d'attente](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_files_d%27attente)** est l'étude mathématique des files d'attente. En ingénierie logicielle, c'est la théorie silencieuse derrière une énorme quantité de pratique. La réactivité de service client, la planification **[kanban](https://fr.wikipedia.org/wiki/Kanban_%28d%C3%A9veloppement%29)** (une méthode basée sur la traction qui plafonne le **[travail en cours](https://fr.wikipedia.org/wiki/En-cours)** pour améliorer le flux), les files d'attente de messages inter-processus, les pipelines de déploiement continu : ce sont tous des files d'attente, et elles obéissent toutes aux mêmes lois. Comprendre ces lois permet à une équipe de raisonner sur les **[délais de livraison](https://fr.wikipedia.org/wiki/D%C3%A9lai_de_livraison)**, le **[débit](https://fr.wikipedia.org/wiki/D%C3%A9bit_%28informatique%29)**, la capacité, et le vrai coût de faire fonctionner les systèmes près de leurs limites, au lieu d'en être surpris en production. Ce chapitre se trouve dans la partie Flux parce que la théorie des files d'attente est la fondation formelle du flux : elle explique *pourquoi* le travail attend, et ce qui réduit réellement l'attente.

Voici la motivation : l'intuition sur les files d'attente est fiablement fausse, et fausse de façons coûteuses. Les gens supposent qu'un serveur fonctionnant à 90 % d'utilisation est « à 10 % du problème », alors qu'en fait les temps d'attente explosent non linéairement à mesure que l'utilisation approche 100 %. Ils supposent qu'ajouter du travail en cours (WIP) accélère la livraison, alors que cela allonge les délais de livraison. Ils planifient la capacité autour de moyennes, puis sont détruits par la variabilité. Un peu de théorie des files d'attente remplace ces intuitions coûteuses par un petit nombre de relations robustes, la plus importante étant la **[loi de Little](https://fr.wikipedia.org/wiki/Loi_de_Little)**, qui tiennent à travers les files d'attente clients, tableaux de tâches, et pipelines CI/CD pareillement.

Pour les grandes équipes, l'entreprise, et le gouvernement, la théorie des files d'attente est un langage partagé pour la capacité et le flux, un qui connecte des rôles qui autrement se parlent sans se comprendre. Les chefs de produit se soucient du délai de livraison depuis l'idée jusqu'au client. Les SRE se soucient de l'utilisation du serveur et de la latence. Les équipes DevOps se soucient de la fréquence de déploiement. Les responsables de support se soucient des temps de réponse. Ce sont tous des métriques de file d'attente, et les exprimer dans un seul cadre (taux d'arrivée, taux de service, utilisation, temps d'attente) permet à une organisation de planifier la capacité, fixer des SLO (objectifs de niveau de service) réalistes, et justifier l'investissement avec des mathématiques plutôt que de l'anecdote.

## Principes clés

- **Tout ce qui a une attente est une file d'attente :** tickets, tâches, messages, et déploiements inclus.
- **La loi de Little est l'ancre :** éléments dans le système = taux d'arrivée × temps dans le système (κ = λτ).
- **L'utilisation et le temps d'attente sont non linéaires :** les derniers 15 % de capacité sont les plus chers.
- **La variabilité est l'ennemie du flux :** les moyennes cachent la douleur ; la variance crée les files d'attente.
- **Réduire le travail en cours réduit le délai de livraison :** le flux, pas l'occupation, est le but.
- **Mesurez tout le flux :** arrivées, service, succès, échecs, sauts, et attentes.
- **Un processus est une file d'attente de files d'attente :** modélisez les étapes, puis optimisez celle qui contraint.

## Recommandations

### Apprendre la notation centrale et l'utiliser de façon cohérente

Une poignée de quantités décrivent toute file d'attente. Les standardiser (les lettres grecques sont conventionnelles) retire l'ambiguïté à travers les équipes :

- **λ (lambda), taux d'arrivée :** à quelle vitesse de nouveaux éléments entrent.
- **μ (mu), taux de service :** à quelle vitesse les éléments sont traités. Parce que « taux de service » est utilisé de façon ambiguë, il vaut souvent la peine de diviser explicitement le débit en **taux total (χ)**, **taux de succès (α)**, **taux d'échec (β)**, et **taux de saut (σ)**, où χ = α + β + σ.
- **ρ (rho), utilisation / intensité de trafic = λ / μ :** le résumé le plus important. ρ < 1 signifie que la file se vide ; ρ ≥ 1 signifie qu'elle grandit sans limite.
- **Temps :** délai de livraison (τ, du début à la fin), temps de travail (φ, traitement réel), temps d'attente (ω, en attente), et temps d'étape (θ, entre achèvements).
- **ε (epsilon), ratio d'erreur :** échecs ÷ total.

Nommer explicitement les échecs et les *sauts* compte en logiciel : un élément qui est abandonné (un client qui abandonne, un panier laissé, un ticket de travail rejeté) quitte la file sans être servi, et prétendre qu'il a été « servi » corrompt vos métriques. Suivez le **refus** (décider de ne pas rejoindre), le **abandon** (renoncer après avoir attendu), et le **changement de file** (basculer de file) comme des résultats de premier ordre.

### Ancrer la planification sur la loi de Little

La loi de Little énonce que le nombre moyen à long terme d'éléments dans un système stable égale le taux d'arrivée moyen multiplié par le temps moyen que chaque élément passe dans le système : **κ = λτ** (classiquement L = λW). Elle est étonnamment générale (elle n'a besoin d'aucune hypothèse sur la distribution d'arrivée ou l'ordre de service), ce qui en fait le cheval de bataille de la planification de flux. Réarrangée, elle vous dit que le **délai de livraison = travail en cours ÷ débit**. C'est la base mathématique du kanban et du lean : si vous voulez des délais de livraison plus courts et ne pouvez pas élever le débit, vous devez baisser le WIP. Elle donne aussi des vérifications de bon sens rapides. Si 40 tickets sont ouverts et que vous en fermez 8 par jour, le ticket moyen prend environ 5 jours, peu importe à quel point tout le monde se sent occupé. Sa seule exigence est la *stabilité* : les arrivées ne doivent pas dépasser persistamment les départs (ρ < 1), sinon la file, et les hypothèses de la loi, s'effondrent.

### Respecter la non-linéarité de l'utilisation

La leçon opérationnelle la plus importante de la théorie des files d'attente est que le temps de réponse monte brusquement, pas graduellement, à mesure que l'utilisation approche 100 %. Les *Sept perspectives sur la théorie des files d'attente* de Bob Wescott capturent vivement les conséquences pratiques :

1. Plus le centre de service est lent, plus l'utilisation de pic pour laquelle vous devriez planifier est basse.
2. Il est très difficile d'utiliser les derniers 15 % de quoi que ce soit.
3. Plus vous fonctionnez près du bord, plus le prix de se tromper est élevé.
4. La croissance du temps de réponse est bornée par combien d'éléments peuvent attendre.
5. Ce sont des moyennes, pas des maximums : planifiez pour la queue.
6. Méfiez-vous de l'effet de déni humain à travers de multiples centres de service.
7. Montrez les petites améliorations sous leur meilleur jour.

L'implication de conception : **approvisionnez délibérément de la marge.** Viser 70 à 80 % d'utilisation pour les systèmes sensibles à la latence n'est pas du gaspillage ; c'est acheter un temps de réponse prévisible. Cela informe directement la planification de capacité et les SLO (chapitres 3.5 et 9.1).

### Modéliser les processus comme une file d'attente de files d'attente

Le vrai travail s'écoule à travers des étapes, et un processus multi-étapes est simplement une file d'attente dont les éléments sont eux-mêmes mis en file à chaque étape. Modélisez-le ainsi : le taux d'arrivée du processus est le taux d'arrivée de l'étape 1 ; le taux de succès du processus est le taux de succès de l'étape finale ; les comptes d'erreur et de saut du processus sont les sommes à travers les étapes. Deux formes communes se répètent :

- **Les entonnoirs**, où les comptes d'éléments rétrécissent à chaque étape (embauche : sensibilisation → entretien → offre ; achat : parcourir → panier → payer ; livraison : intégrer → tests d'acceptation utilisateur → production). Optimisez l'étape qui compte le plus : maximisez les arrivées en haut de l'entonnoir, minimisez les sauts au milieu de l'entonnoir (abandon de panier), ou minimisez les erreurs à l'étape finale (mauvais déploiements de production).
- **Les flux de découverte-et-livraison en double losange** (découvrir → définir → développer → livrer), que la partie Flux de ce livre traite directement (chapitre 11.1).

Trouver et soulager l'**étape contraignante** (le goulot d'étranglement) est où l'amélioration de flux paie ; optimiser les non-contraintes ne fait que déplacer la file.

### Connecter les métriques de file d'attente aux KPI que les équipes utilisent déjà

Les quantités de file d'attente correspondent proprement aux métriques de livraison et de fiabilité ailleurs dans ce livre, ce qui rend la théorie pratique plutôt qu'académique :

- Le **délai de livraison (Dτ)**, « du concept au client », est une mesure de délai de livraison (τ) et une métrique DORA (**[DevOps Research and Assessment](https://fr.wikipedia.org/wiki/DevOps#DORA)**) (chapitre 11.2).
- La **fréquence de déploiement (Dμ)** est une mesure de taux de service.
- Le **taux d'échec de changement (Dε)** est un ratio d'erreur.
- Le **temps de restauration (Rτ)** est un délai de livraison de restauration, c'est-à-dire le MTTR (chapitre 9.3).

Distinguez les plusieurs **MTTR** (temps moyen pour *répondre*, *réparer*, *récupérer*, et *résoudre*) parce qu'ils mesurent différents segments de la file d'incident et sont routinièrement confondus. Ancrer les SLI/SLO/SLA (chapitre 9.1) en termes de file d'attente garde les cibles honnêtes et comparables.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| **Faire fonctionner les systèmes à haute utilisation** | Coût matériel/unitaire plus bas | Explosions de latence non linéaires ; fragile aux pics |
| **Approvisionner une marge généreuse** | Latence prévisible ; résilient à la variance | Coût en état stable plus élevé ; semble « sous-utilisé » |
| **Limiter le WIP (kanban)** | Délais de livraison plus courts ; moins de changement de contexte | Se sent plus lent ; exige de la discipline pour tenir la limite |
| **Modélisation formelle de file d'attente** | Décisions de capacité quantifiées ; moins de surprises | Courbe d'apprentissage ; les modèles simplifient la réalité désordonnée |
| **Règles empiriques seulement** | Rapide, sans mathématiques | Fausse précisément là où c'est le plus coûteux (près de la capacité) |

Le compromis récurrent est **efficacité contre prévisibilité** : pousser l'utilisation vers le haut économise de l'argent jusqu'à ce que soudainement ce ne soit plus le cas, moment auquel la latence, l'échec, et les coûts de lutte contre les incendies éclipsent les économies. La contribution de la théorie des files d'attente est de vous dire *où* se trouve cette falaise pour que le compromis soit un choix, pas un accident.

## Questions à discuter avec votre équipe

1. **Quelle est votre cible d'utilisation explicite pour chaque système sensible à la latence, et qui l'a approuvée ?** La marge est un achat délibéré de latence prévisible, donc cela devrait être une politique énoncée, pas un accident de quelle que soit la charge qui est arrivée. Parce que le temps de réponse monte non linéairement, fonctionner à 85 % peut déjà signifier une latence de queue élevée, pourtant la finance voit la marge comme du gaspillage et pousse l'utilisation vers le haut. Apportez les chiffres : utilisation actuelle, courbe de latence mesurée, et le coût de votre dernier incident de latence, puis montrez où se trouve la falaise pour chaque service. Pour les systèmes d'entreprise et gouvernementaux avec des pics saisonniers (saison de dépôt, fenêtres d'inscription), fixez la cible depuis la falaise pour le pic, pas la moyenne. Si personne ne possède la cible d'utilisation, les incidents de latence continueront d'apparaître « de nulle part ».

2. **Où dans vos systèmes une file d'attente est-elle non bornée, sans contre-pression pour délester la charge quand submergée ?** Une file non bornée n'échoue pas gracieusement ; elle se dégrade en effondrement, parce que des arrivées dépassant persistamment les départs (rho >= 1) signifie que la file grandit sans limite. Inventoriez vos files de messages, pools de threads, et tampons de requête, et demandez ce qui se passe à chacun quand le taux d'arrivée dépasse le taux de service : délestent-ils la charge, appliquent-ils la contre-pression, ou s'effondrent-ils ? Cela compte aigüment à l'échelle d'entreprise, où un aval saturé peut cascader à travers les services. Apportez un résultat de test de charge ou un incident passé où une file s'est engorgée, et vérifiez si le système a rejeté le travail excédentaire ou a essayé de tout retenir. Le correctif est des files bornées avec contre-pression et délais d'expiration explicites dérivés de la loi de Little, pour qu'une surcharge délestre plutôt que ne bascule.

3. **Modélisez-vous votre flux idée-vers-production comme une file d'attente de files d'attente, et vos améliorations visent-elles la vraie contrainte ?** Un processus multi-étapes est une file d'attente dont les éléments sont mis en file à chaque étape, et optimiser tout sauf l'étape contraignante ne fait que déplacer la file. Cartographiez votre entonnoir de livraison (intégrer vers tests d'acceptation utilisateur vers production, ou découvrir vers définir vers développer vers livrer) et mesurez les taux d'arrivée, de service, d'attente, et de saut à chaque étape pour trouver où le travail s'accumule réellement. Les équipes optimisent routinièrement l'étape qu'elles comprennent le mieux plutôt que le goulot d'étranglement, ce qui dépense de l'effort et ne bouge rien. Apportez des données de temps d'attente par étape, pas de l'instinct, parce que le goulot d'étranglement est souvent un état d'attente (révision, approbation, disponibilité d'environnement) plutôt qu'un état de travail. Une fois que vous connaissez la contrainte, visez là et laissez les non-contraintes tranquilles.

4. **Utilisez-vous la loi de Little pour fixer des limites de WIP, ou ajoutez-vous de la capacité pour guérir des délais de livraison que seule plus de discipline corrigerait ?** La loi de Little dit que le délai de livraison égale le travail en cours divisé par le débit, donc si vous ne pouvez pas élever le débit, le seul levier restant pour des délais de livraison plus courts est de baisser le WIP, ce qui ne coûte rien sauf de la retenue. La traction concurrente est réelle : plafonner le travail en cours semble plus lent et inactif, et les gestionnaires sous pression préféreraient embaucher ou acheter du matériel plutôt que de dire aux équipes de commencer moins et finir plus. Apportez les chiffres durs, les éléments ouverts actuels et le taux d'achèvement par étape, et calculez le délai de livraison moyen implicite, puis comparez-le à ce que les gens croient qu'il est ; l'écart est habituellement grand et embarrassant. Dans une grande entreprise ou agence, une demande d'embauche ou de marché public justifiée comme correctif de délai de livraison devrait être testée contre cette arithmétique en premier, parce qu'une augmentation d'effectif qui élève le WIP peut allonger les délais de livraison mêmes qu'elle était censée raccourcir.

5. **Planifiez-vous la capacité autour des moyennes, ou avez-vous quantifié la variabilité qui crée réellement vos files d'attente ?** Les files d'attente se forment depuis la variance, pas depuis la moyenne, donc deux systèmes avec une charge moyenne identique peuvent se comporter complètement différemment si l'un a des arrivées en rafale ou des temps de service à queue longue. La tension est que les moyennes sont faciles à rassembler et rassurantes à rapporter, tandis que la variance et la queue sont plus difficiles à mesurer et mal accueillies dans une mise à jour de statut. Apportez la distribution, pas la moyenne : le caractère en rafale des arrivées, les temps de service et d'attente au 95e et 99e centile, et les tailles de lot qui concentrent le travail en pics. Pour les systèmes d'entreprise et gouvernementaux avec des poussées prévisibles (saison de dépôt, cycles de paie, fenêtres d'inscription, charges de fin de trimestre), planifiez le tampon et la cible d'utilisation depuis la variance de période de pic, parce qu'une conception dimensionnée pour la moyenne annuelle échouera précisément quand le public regarde.

6. **Lesquelles de vos files comptent silencieusement les abandons et rejets comme si le travail avait été servi, et quelle demande non satisfaite cela cache-t-il ?** Un élément qui refuse, abandonne, ou est rejeté quitte la file sans être géré, et l'enregistrer comme « servi » corrompt à la fois votre débit, votre ratio d'erreur, et votre plan de capacité. La considération concurrente est que « appels répondus » ou « tickets fermés » semble mieux sur un tableau de bord que « appelants qui ont abandonné », donc le chiffre honnête est celui que personne ne se porte volontaire pour faire surgir. Apportez le taux de saut (σ), les comptes de refus et d'abandon, et la différence entre la charge offerte et la charge servie, pour que la vraie demande devienne visible. Cela compte aigüment dans la livraison de service gouvernemental, où les citoyens qui abandonnent une file téléphonique ou une demande de prestations sont des obligations non satisfaites plutôt que des cas résolus, et les rapporter comme gérés à la fois fausse la performance et sous-estime la capacité que le public mérite.

## Regard sectoriel

**Jeune pousse.** Vous n'avez pas le temps pour une modélisation formelle de file d'attente et n'en avez pas besoin. Atteignez d'abord pour les deux gains les moins chers : appliquez la loi de Little à votre carnet pour voir le vrai délai de livraison que votre WIP implique, et surveillez votre tableau kanban pour l'étape où le travail s'accumule avant d'embaucher contre un goulot d'étranglement qui pourrait ne pas exister. Gardez l'utilisation loin de la falaise sur tout chemin sensible à la latence en laissant de la marge plutôt qu'en l'ajustant, parce qu'une panne pendant un pic de croissance coûte bien plus qu'un peu de capacité inactive.

**Petite entreprise.** Sans spécialiste de file d'attente en personnel, achetez les métriques plutôt que construire les modèles. Choisissez un service d'assistance, courtier de messages, ou plateforme d'hébergement qui rapporte déjà le taux d'arrivée, le temps d'attente, et l'abandon, et lisez ces chiffres au lieu de les dériver. Cadrez la décision comme surveiller deux symptômes : des attentes qui grimpent non linéairement à mesure que vous devenez occupé, et des clients qui abandonnent avant d'être servis, puisqu'un client perdu est le coût de file d'attente qui fait le plus mal à une petite entreprise.

**Grande entreprise.** Le travail est de faire de la pensée de file d'attente une discipline partagée à travers de nombreuses équipes : une notation convenue (λ, μ, ρ, délai de livraison), des politiques cohérentes de WIP et de marge d'utilisation, et des normes de contre-pression pour qu'un aval saturé ne puisse pas cascader à travers les services. Fixez les SLO et la capacité depuis l'analyse de file d'attente plutôt que la supposition, et gérez vos files d'attente comme un portefeuille avec des référentiels et révisions pour qu'aucune équipe unique ne fonctionne chaude isolément. Intégrez l'analyse dans la gouvernance et l'audit de capacité, pour qu'une cible de marge soit une décision documentée que quelqu'un possède.

**Gouvernement.** Les marchés publics, la transparence, et la responsabilité publique façonnent chaque choix de capacité. Dimensionnez les centres de contact et systèmes orientés citoyen depuis la variance de période de pic (saison de dépôt, fenêtres d'inscription), pas la moyenne annuelle, et dotez en personnel pour garder l'utilisation loin de la falaise quand la demande monte. Suivez le refus et l'abandon comme demande publique non satisfaite plutôt que de les cacher dans « appels répondus », et justifiez la dépense de capacité avec des estimations de temps d'attente de loi de Little, qui donnent aux auditeurs et élus un dossier défendable et soutenu par les mathématiques au lieu d'une anecdote.

## Exemples

**Jeune pousse.** Une équipe SaaS de cinq personnes noyée dans un arriéré de support suppose qu'elle a besoin d'embaucher un autre agent. Avant de dépenser l'argent, elle applique la loi de Little : 60 tickets ouverts et 12 fermés par jour signifie qu'un ticket moyen attend environ 5 jours, ce qui correspond aux courriels furieux. En surveillant leur tableau kanban, ils remarquent que les tickets s'accumulent en attendant l'ingénierie, pas le support, donc ils plafonnent le travail en cours et acheminent les rapports de bug directement dans le sprint au lieu de les laisser en file. Le délai de livraison chute à moins de deux jours sans nouvelle embauche, et ils utilisent le budget libéré sur le vrai goulot d'étranglement à la place.

**Grande entreprise.** Une plateforme de paiements dimensionnant son service d'autorisation mesure λ ≈ 850 requêtes/seconde et μ par nœud ≈ 200/seconde. Naïvement, c'est environ 5 nœuds (ρ = 0,85), mais sachant que ρ = 0,85 signifie déjà une latence de queue fortement élevée, l'équipe approvisionne à ρ ≈ 0,65 et utilise la loi de Little pour prédire les comptes de requêtes en vol et fixer les profondeurs de file et délais d'expiration. Les incidents de saison de pic qui apparaissaient auparavant « de nulle part » disparaissent, parce que l'équipe n'opérait plus sur la partie abrupte de la courbe.

**Gouvernement.** Le centre de contact d'une agence fiscale modélise le support de saison de dépôt comme une file d'attente : pics d'arrivée (λ), capacité d'agent (μ), et, crucialement, le **taux de saut (σ)** des citoyens qui abandonnent après de longues attentes. En suivant le refus et l'abandon plutôt que seulement « appels répondus », la direction voit la vraie demande non satisfaite, dote en personnel pour garder l'utilisation loin de la falaise pendant les pics, et justifie la capacité supplémentaire avec des estimations de temps d'attente de loi de Little, un dossier défendable et soutenu par les mathématiques pour la dépense publique plutôt qu'anecdotique.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La théorie des files d'attente se rentabilise en prévenant deux erreurs coûteuses : le **sur-approvisionnement** (payer pour une capacité inactive dont vous n'aviez pas besoin) et, bien plus dommageable, le **sous-approvisionnement près de la falaise** (où de petites augmentations de charge causent une grande latence, des SLA violés, des clients abandonnés, et une dépense d'urgence). Parce que le coût de fonctionner près de 100 % d'utilisation est non linéaire, les économies de « ajoutez juste un peu plus de charge » sont petites et le désavantage est catastrophique, exactement l'asymétrie qu'un peu de mathématiques transforme en décision délibérée. Le retour se mesure en pannes évitées, SLA respectés, clients retenus qui auraient autrement refusé, et rotations d'astreinte plus calmes.

Sur le **coût total de possession**, le cadre est bon marché à adopter (c'est de la connaissance, pas de l'outillage) et il améliore presque chaque décision de capacité, latence, et flux qu'une grande organisation prend sur la vie d'un système. La loi de Little et les limites de WIP réduisent les délais de livraison sans rien acheter (un pur gain de processus), tandis que la discipline d'utilisation échange un coût en état stable modeste et prévisible contre l'élimination d'échecs coûteux et imprévisibles. Pour faire valoir le dossier auprès de la direction, traduisez un incident de latence récent en la courbe d'utilisation et montrez comment une cible de marge l'aurait empêché, et utilisez la loi de Little pour connecter la réduction de WIP directement à une livraison plus rapide.

## Anti-patterns et pièges

- **Planifier la capacité autour des moyennes :** ignorer la variance, qui est ce qui crée réellement les files d'attente.
- **Fonctionner chaud :** viser 90 %+ d'utilisation sur les systèmes sensibles à la latence et être choqué par la latence de queue.
- **Compter les sauts comme service :** traiter les clients abandonnés ou tickets rejetés comme gérés, corrompant les métriques.
- **Empiler le WIP :** confondre l'occupation avec le débit et allonger les délais de livraison.
- **Optimiser un non-goulot d'étranglement :** améliorer des étapes qui ne sont pas la contrainte et déplacer la file ailleurs.
- **Confondre les MTTR :** rapporter « récupération » tout en mesurant « réparation », ou vice versa.
- **Les files d'attente non bornées :** aucune contre-pression, donc un système surchargé se dégrade en effondrement au lieu de délester la charge.
- **Les moyennes comme maximums :** concevoir vers la moyenne et être appelé par la queue.

## Modèle de maturité

- **Niveau 1, Initier :** Les files d'attente (tickets, tâches, messages, déploiements) ne sont pas gérées et sont réactives ; la capacité est devinée ; l'utilisation fonctionne où que la charge atterrisse ; les problèmes de latence surprennent l'équipe et sont combattus après coup.
- **Niveau 2, Développer :** Quelques équipes rassemblent des métriques de base (débit, attente moyenne) mais les lisent comme des moyennes et les appliquent de façon incohérente ; certains groupes plafonnent le WIP ou laissent de la marge tandis que d'autres fonctionnent chauds ; il n'y a pas de notation partagée, donc les pratiques ne voyagent pas à travers les équipes.
- **Niveau 3, Standardiser :** Une notation commune (λ, μ, ρ, délai de livraison) est documentée et appliquée à l'échelle de l'organisation ; les limites de WIP et cibles de marge d'utilisation sont fixées délibérément pour chaque système sensible à la latence ; les plusieurs MTTR sont distingués ; les files d'attente bornées avec contre-pression sont le défaut à travers les services.
- **Niveau 4, Gérer :** Les files d'attente sont mesurées et contrôlées contre des référentiels : le taux d'arrivée, taux de service, utilisation, latence de queue (p95/p99), et délai de livraison sont suivis contre des cibles et SLO définis ; les profondeurs de file, délais d'expiration, et marge sont dérivés de la loi de Little plutôt que devinés ; le refus, l'abandon, et le taux de saut sont comptés pour que la charge offerte soit distinguée de la charge servie ; les décisions de capacité sont révisées sur ces preuves, pas sur le ressenti.
- **Niveau 5, Orchestrer :** Le flux est modélisé continuellement comme une file d'attente de files d'attente ; les goulots d'étranglement sont identifiés et soulagés comme pratique continue ; la capacité, les SLO, et la contre-pression s'adaptent à la demande et variance changeantes ; les métriques de file d'attente se lient directement aux KPI DORA et d'affaires, et l'organisation rééquilibre la capacité à travers tout le flux à mesure que le tableau de charge et de risque change.

## Pistes de réflexion

1. À quelle utilisation vos systèmes sensibles à la latence fonctionnent-ils réellement, et où est leur falaise ?
2. Appliquez la loi de Little à votre carnet actuel : quel délai de livraison votre WIP ÷ débit implique-t-il, et cela correspond-il à la réalité ?
3. Lesquelles de vos files d'attente comptent silencieusement les « sauts » (abandons, rejets) comme s'ils avaient été servis ?
4. Où baisser le WIP raccourcirait-il le délai de livraison moins cher qu'ajouter de la capacité ?
5. Quelle étape dans votre flux idée-vers-production est le vrai goulot d'étranglement, et vos améliorations visent-elles là ?
6. Vos tableaux de bord montrent-ils des moyennes là où la queue est ce qui vous fait réellement mal ?

## Points clés à retenir

- Les files d'attente clients, tableaux kanban, files de messages, et pipelines de déploiement sont tous des files d'attente gouvernées par les mêmes lois.
- La **loi de Little (κ = λτ)** ancre la planification de flux : délai de livraison = WIP ÷ débit.
- L'utilisation et le temps d'attente sont **non linéaires** : approvisionnez de la marge ; les derniers 15 % sont les plus chers.
- Suivez l'image complète : arrivées, service, succès, **échecs et sauts**, et attentes ; ne laissez pas l'abandon se cacher.
- Modélisez les processus comme une **file d'attente de files d'attente** et corrigez le **goulot d'étranglement**, pas le travail occupé.
- Les métriques de file d'attente correspondent directement aux mesures **DORA/flux** et **SLI/SLO** (chapitres 11.1, 11.2, 9.1), donnant à toute l'organisation un langage pour la capacité et le flux.

## Références et lectures complémentaires

- Bob Wescott, *Seven Insights into Queueing Theory* (et *The Every Computer Performance Book*).
- John D. C. Little, « A Proof for the Queuing Formula L = λW » (1961) : la loi de Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* : métriques DORA basées sur le flux qui s'alignent avec les KPI de file d'attente.
- Donald Reinertsen, *The Principles of Product Development Flow* : files d'attente, taille de lot, et économie de WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* : la loi de Little appliquée au kanban.
- Joel Parker Henderson, *Queueing Theory* : notation, KPI, et file de files (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, « The most important thing to understand about queues » (2016).
- Wikipédia : « Théorie des files d'attente », « File M/M/1 », « Loi de Little », « Chaîne de Markov ».
