# 6.6 Infrastructure et opérations d'IA

## Vue d'ensemble et motivation

L'infrastructure et les opérations d'IA sont la discipline d'approvisionner, planifier, et exploiter le calcul, stockage, et systèmes de service spécialisés que les charges de travail d'IA exigent, en le faisant de façon rentable, fiable, et observable. L'IA moderne est coûteuse à exploiter. Entraîner et servir de grands modèles exige des accélérateurs rares ([GPU](https://fr.wikipedia.org/wiki/Processeur_graphique) et [TPU](https://fr.wikipedia.org/wiki/Tensor_Processing_Unit)), du réseautage à haute bande passante, du stockage vectoriel à grande échelle pour la récupération (indexer les données comme vecteurs numériques pour que des éléments similaires puissent être trouvés rapidement), et des couches de service réglées pour la latence et le débit. Bien faire cette infrastructure est la différence entre une IA qui s'échelonne durablement et une IA qui consomme discrètement un budget tout en sous-livrant.

Pour les grandes équipes, les problèmes centraux sont l'échelle, la rareté, et le coût. Les accélérateurs sont limités et coûteux, donc la planification et l'utilisation comptent énormément. Les GPU inactifs sont de l'argent brûlé, et l'inférence mal groupée multiplie le coût par requête. Les applications riches en récupération ont besoin de [bases de données vectorielles](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_vectorielle) qui restent rapides à mesure qu'elles grandissent. Les applications d'IA générative ont besoin de versionnage de prompt, de pipelines d'évaluation, et d'observabilité (parfois appelé LLMOps) pour opérer en sécurité et s'améliorer dans le temps. Sans infrastructure et discipline opérationnelle partagées, chaque équipe combat les mêmes batailles et les coûts spiralent.

L'administration publique et les organisations régulées ajoutent des exigences autour de la souveraineté des données, la sécurité, et la dépense prévisible. Elles peuvent avoir besoin d'un déploiement sur site ou en cloud souverain pour que les données sensibles et modèles ne quittent jamais des frontières contrôlées. Elles doivent prévoir et justifier la dépense d'infrastructure, et satisfaire des normes de sécurité et disponibilité. Les décisions d'infrastructure d'IA dans ces contextes portent des conséquences pluriannuelles, donc prenez-les avec l'approvisionnement, la sécurité, et la sortie à l'esprit.

## Principes clés

- Traitez le calcul d'accélérateur comme une ressource rare et coûteuse à planifier et utiliser, pas à thésauriser.
- Optimisez le coût par unité utile de travail, pas la capacité brute.
- Dimensionnez correctement les modèles et le matériel à la tâche ; l'option la plus grande est rarement la plus rentable.
- Concevez le service pour la latence et le débit avec le groupement et la mise en cache comme techniques de première classe.
- Rendez les systèmes d'IA observables : suivez le coût, la latence, la qualité, et les erreurs continuellement.
- Versionnez et évaluez les prompts et modèles avec la même rigueur que le code.
- Planifiez pour la portabilité et évitez le verrouillage dans les choix d'infrastructure et de service.

## Recommandations

### Planifier et contrôler le calcul d'accélérateur

Prévoyez la demande pour l'entraînement et l'inférence séparément, puisqu'ils ont des formes différentes. L'entraînement est en rafales et planifiable ; l'inférence est continue et sensible à la latence. Utilisez des planificateurs et quotas pour partager les GPU et TPU rares à travers les équipes, prioriser les charges de travail, et faire monter l'utilisation. Mesurez l'utilisation et traitez l'inactivité chronique comme un problème à corriger. Mélangez de la capacité réservée pour la charge de base avec de la capacité à la demande ou spot pour les rafales pour contrôler le coût. Considérez si des accélérateurs moins chers ou plus petits, ou l'inférence CPU pour les modèles légers, suffiraient. Choisissez entre cloud, sur site, et hybride basé sur le coût à votre échelle, les besoins de souveraineté de données, et les motifs de rafale, et gardez un chemin de sortie.

### Construire l'infrastructure de récupération : plongements et bases de données vectorielles

Pour les applications augmentées par récupération, montez une infrastructure pour générer des [plongements](https://fr.wikipedia.org/wiki/Word_embedding) (représentations vectorielles numériques qui placent des éléments similaires proches les uns des autres) et les stocker dans une base de données vectorielle qui soutient la [recherche rapide du plus proche voisin approximatif](https://fr.wikipedia.org/wiki/Recherche_des_plus_proches_voisins) (trouver les vecteurs les plus similaires sans comparer exhaustivement chacun) à votre échelle. Planifiez pour trois choses : le coût et la latence de génération de plongement, la fraîcheur d'index à mesure que les documents changent, et le fardeau opérationnel de garder les index cohérents. Évaluez si une base de données vectorielle dédiée, une extension à capacité vectorielle d'une base de données existante, ou un service géré convient le mieux à votre échelle et tolérance de verrouillage. Surveillez la latence et le rappel de récupération, parce que la qualité de récupération détermine directement la qualité d'application.

### Optimiser le service de modèle : groupement, mise en cache, et latence

Le service est là où le coût d'inférence et l'expérience utilisateur sont décidés. Utilisez le **groupement** pour traiter plusieurs requêtes ensemble et élever le débit d'accélérateur, équilibrant la taille de groupe contre la latence. Utilisez la **mise en cache** agressivement : mettez en cache les requêtes identiques ou sémantiquement similaires, mettez en cache les plongements, et exploitez la mise en cache de prompt ou préfixe où la plateforme le soutient pour éviter de recalculer le contexte partagé. Fixez des cibles de latence claires, et mesurez la latence de queue, pas seulement les moyennes. Acheminez les requêtes vers des modèles bien dimensionnés : un petit modèle pour les cas faciles, un plus grand seulement quand nécessaire. Autoscalez le service selon la demande, et testez la charge avant le lancement pour connaître votre capacité et courbe de coût.

### Pratiquer LLMOps : versionnage de prompt, pipelines d'évaluation, et observabilité

Traitez les prompts comme des artefacts versionnés dans le contrôle de source, avec revue et la capacité de revenir en arrière. Construisez des pipelines d'évaluation qui exécutent automatiquement des suites de test hors ligne chaque fois que les prompts ou modèles changent, pour que vous attrapiez les régressions avant la sortie. Instrumentez la production de façon complète : journalisez les entrées, sorties, latence, usage de jeton, coût, et erreurs, avec échantillonnage et garde-fous de confidentialité. Suivez les signaux de qualité et retour utilisateur en ligne. Cette observabilité vous permet d'attraper la dégradation, contrôler le coût, déboguer les échecs, et améliorer les systèmes en sécurité : l'épine dorsale opérationnelle de l'IA générative en production.

### Gérer le coût sans relâche et de façon observable

Attribuez la dépense d'IA aux équipes et cas d'usage pour que le coût soit visible et possédé. Fixez des budgets et alertes, surveillez le coût par requête et par résultat, et révisez régulièrement les plus grands moteurs de coût. Tirez les leviers que vous avez : dimensionnement correct de modèle, mise en cache, groupement, découpage de prompt et contexte, et choix du déploiement le moins cher qui satisfait les exigences. Les coûts d'IA peuvent s'échelonner avec l'usage de façons surprenantes, donc l'observabilité de coût continue est essentielle pour éviter des surprises désagréables.

## Compromis : avantages et inconvénients

| Décision | Option A | Option B | Compromis |
|---|---|---|---|
| Emplacement de calcul | Cloud | Sur site | Élasticité et faible coût initial contre contrôle, souveraineté, et économie en régime permanent |
| Capacité | Réservée | À la demande/spot | Coût prévisible contre flexibilité et risque d'interruption |
| Taille de groupe | Grands groupes | Petits groupes | Débit et coût contre latence |
| Taille de modèle | Grand modèle | Petit modèle | Qualité contre coût et vitesse |
| Magasin vectoriel | Base de données dédiée | Extension de base de données existante | Performance à l'échelle contre simplicité et moins de systèmes |
| Mise en cache | Agressive | Minimale | Coût et latence plus bas contre fraîcheur et complexité |

Le compromis dominant est le coût contre la latence et la qualité. Le groupement, la mise en cache, et les modèles plus petits réduisent le coût mais peuvent ajouter de la latence ou réduire la qualité. Le bon équilibre dépend de la tolérance de votre application. Sur site contre cloud échange le contrôle et l'économie en régime permanent contre l'élasticité et le faible engagement, une décision fortement façonnée par les besoins de souveraineté de données et l'échelle.

## Questions à discuter avec votre équipe

1. **Quel est notre coût par résultat utile aujourd'hui, et quel levier le déplacerait le plus ?** La capacité brute et les moyennes par requête cachent le chiffre qui compte : ce qu'il en coûte pour livrer une vraie unité de valeur, et comment cela s'échelonne avec l'usage. Pour une grande équipe, l'écart entre un déploiement optimisé et non optimisé est souvent de plusieurs fois en dépense, donc cette question transforme une inquiétude vague sur la facture en une liste classée de corrections. Apportez l'attribution de coût actuelle par équipe et cas d'usage, les tendances par requête et par résultat, et les plus grands moteurs de coût. Discutez les leviers par ordre de gain : dimensionnement correct de modèle, mise en cache (incluant la mise en cache de préfixe et sémantique), groupement, et découpage de prompt ou contexte. Dans l'administration publique, ajoutez la pression de prévoir et justifier la dépense pluriannuelle. La réponse devrait assigner à chaque moteur de coût principal un propriétaire et un levier, pas un haussement d'épaules.

2. **Si notre fournisseur d'inférence actuel doublait son prix ou tombait demain, à quelle vitesse pourrions-nous changer ?** Le verrouillage silencieux est facile à construire et douloureux à échapper, et les piles de service sont là où il se cache le plus profondément. Pour les entreprises et spécialement l'administration publique, la portabilité est une exigence d'approvisionnement et de continuité, pas une gentillesse. Apportez votre architecture : si les modèles se trouvent derrière une interface interne, si les prompts et suites d'évaluation sont portables, et combien de comportement de service spécifique au fournisseur vous dépendez. Le signal à surveiller est si quelqu'un a déjà exécuté votre suite d'évaluation contre un deuxième fournisseur ou une deuxième cible de déploiement. Si changer prendrait des mois et réécrirait des chemins centraux, traitez cela comme un défaut de conception à adresser maintenant, puisque les options souveraines et sur site peuvent devenir obligatoires avec peu de préavis.

3. **Quelle est notre utilisation d'accélérateur en ce moment, et combien les GPU inactifs et l'inférence non groupée brûlent-ils ?** Les accélérateurs sont rares et coûteux, donc l'inactivité chronique et le service par requête drainent discrètement des budgets qui pourraient financer plus de capacité. Pour une grande organisation partageant des GPU à travers les équipes, cette question expose si la planification, les quotas, et les priorités gardent réellement l'utilisation haute ou si le matériel thésaurisé et sous-utilisé est la norme. Apportez de vrais chiffres d'utilisation, votre posture de groupement et mise en cache, et vos mesures de latence de queue, pas seulement les moyennes, puisque les utilisateurs ressentent la queue lente. Discutez si la demande d'entraînement et d'inférence est prévue séparément, étant donné leurs formes différentes, et si un plus petit modèle ou l'inférence CPU suffirait pour les cas légers. La réponse devrait pointer vers une capacité inactive spécifique à récupérer et des requêtes spécifiques à grouper ou acheminer vers un modèle bien dimensionné.

4. **Quand un changement de prompt ou modèle est livré, qu'est-ce qui empêche une régression silencieuse de qualité ou coût d'atteindre les utilisateurs ?** Une pile de service peut paraître saine en latence et disponibilité pendant que les réponses qu'elle retourne s'empirent discrètement ou qu'un nouveau prompt double l'usage de jeton par requête. Pour une grande équipe où de nombreux groupes éditent des prompts et échangent des modèles indépendamment, un changement non conditionné est un incident de production qui attend d'arriver, et le rayon d'explosion grandit avec chaque équipe sur la plateforme partagée. Apportez votre couverture d'évaluation : quels prompts et modèles ont des suites de test hors ligne, si ces suites s'exécutent automatiquement à chaque changement, quels seuils de qualité et coût conditionnent une sortie, et à quelle vitesse vous pouvez revenir en arrière. Discutez si les prompts vivent dans le contrôle de source avec revue, ou si quelqu'un peut encore éditer un prompt système en direct à la main. Dans les contextes d'entreprise et gouvernementaux, liez chaque changement à une piste d'audit et un approbateur nommé, parce qu'un régulateur demandant « qui a changé cela et qu'avez-vous testé » a besoin d'une réponse qui est enregistrée, pas rappelée.

5. **Comment décidons-nous entre cloud, sur site, et déploiement souverain, et avons-nous évalué la vraie économie en régime permanent plutôt que le pilote ?** Le choix d'emplacement de calcul fixe votre courbe de coût, votre posture de souveraineté de données, et vos options de sortie pour des années, pourtant il est souvent fait sur la facture cloud d'un pilote qui ne ressemble en rien à la production à l'échelle. Pour une grande organisation, la capacité cloud élastique est bon marché à démarrer et peut devenir la plus grande ligne unique une fois que l'inférence s'exécute continuellement, tandis que le sur site échange le faible engagement pour le contrôle et l'économie en régime permanent. Apportez les volumes d'entraînement et d'inférence prévus, le point d'équilibre où le matériel réservé ou possédé bat la demande, vos contraintes de résidence de données et sécurité, et les motifs de rafale qui plaident pour l'hybride. Dans les contextes régulés et gouvernementaux, pesez les exigences de cloud souverain ou sur site qui peuvent devenir obligatoires avec peu de préavis, et confirmez que l'architecture garde les modèles derrière une interface interne pour qu'un mouvement forcé ne réécrive pas les chemins centraux.

6. **Possédons-nous réellement notre dépense d'IA, et chaque équipe peut-elle voir et répondre du coût qu'elle pilote ?** Le coût d'IA s'échelonne avec l'usage de façons qui surprennent les gens, et sans attribution la facture atterrit comme un chiffre opaque unique dont aucune équipe ne se sent responsable de réduire. Dans une grande organisation, un coût que personne ne possède est un coût que personne n'optimise, donc la question est si la dépense est étiquetée aux équipes et cas d'usage avec des budgets, alertes, et tendances par résultat, ou si elle est découverte seulement quand la finance escalade. Apportez votre modèle d'attribution de coût, les plus grands moteurs par équipe, et les leviers que chaque propriétaire contrôle : dimensionnement correct, mise en cache, groupement, et découpage de contexte. Pour les budgets d'entreprise et gouvernementaux, ajoutez la discipline de prévoir et justifier la dépense d'infrastructure pluriannuelle, puisqu'un organisme public qui ne peut pas expliquer sa facture de calcul ligne par ligne luttera pour la défendre en révision.

## Regard sectoriel

**Jeune pousse.** Ne possédez aucune infrastructure que vous pouvez éviter. Appelez une API d'inférence hébergée, acheminez les requêtes faciles vers un petit modèle bon marché et réservez un plus grand pour les cas difficiles, et mettez en cache agressivement pour que les prompts répétés ne coûtent rien. Utilisez une base de données vectorielle gérée plutôt que d'en exploiter une, gardez les prompts dans git avec un court script d'évaluation avant chaque changement, et journalisez le coût par requête pour qu'une facture galopante apparaisse avant qu'elle ne fasse mal. Votre ressource la plus rare est l'attention d'ingénierie, donc achetez l'opérabilité et gardez le changement bon marché.

**Petite entreprise.** Sans équipe de plateforme, traitez le service, la récupération, et l'observabilité comme des choses que vous achetez dans des outils que vous utilisez déjà, pas des systèmes que vous dotez. Favorisez l'inférence gérée et la recherche vectorielle gérée avec une tarification transparente et prévisible, et fixez un plafond de dépense dur et une alerte de facturation dès le premier jour. Cadrez la décision comme acheter contre construire honnêtement : exploiter des GPU ou un index vectoriel paie rarement à votre volume, et un petit modèle derrière une API hébergée satisfait habituellement le besoin à une fraction de l'effort.

**Grande entreprise.** Le problème est une plateforme à chemin pavé et partagée à travers de nombreuses équipes : des accélérateurs mutualisés avec planificateurs, quotas, et priorités pour faire monter l'utilisation, un groupement et une mise en cache standard, des routeurs de dimensionnement correct, et un coût attribué à chaque équipe et cas d'usage. Conditionnez les changements de prompt et modèle avec des suites d'évaluation automatisées, standardisez la couche d'interface pour que les fournisseurs et cibles de déploiement restent interchangeables, et gérez le coût par résultat comme une métrique de première classe plutôt que chaque groupe réinventant une infrastructure coûteuse et sous-utilisée.

**Gouvernement.** La souveraineté des données, la sécurité, et la dépense prévisible façonnent chaque choix. Favorisez le déploiement sur site ou en cloud souverain pour que les données sensibles et modèles restent à l'intérieur de frontières contrôlées, planifiez les GPU rares à travers les départements avec des quotas que vous pouvez justifier en approvisionnement, et prévoyez la capacité pour défendre la dépense pluriannuelle ligne par ligne. Versionnez et évaluez les prompts et modèles avec une piste d'audit enregistrée, gardez une observabilité complète sur le coût et la qualité, et gardez les modèles derrière une interface interne pour qu'un mouvement forcé vers un nouveau fournisseur ou une plateforme souveraine ne vous coince pas.

## Exemples

**Jeune pousse.** Une petite jeune pousse exploitant une fonctionnalité d'écriture IA a gardé sa facture saine sans posséder de GPU. Elle a appelé une API d'inférence hébergée, acheminé les requêtes faciles vers un petit modèle moins cher et gardé le plus grand pour les cas difficiles, et mis en cache les réponses aux prompts répétés. Elle a stocké ses prompts dans git avec un court script d'évaluation qui s'exécutait avant chaque changement, utilisé une base de données vectorielle gérée pour la récupération pour ne pas avoir à en exploiter une, et journalisé le coût par requête pour que les fondateurs puissent voir la dépense grimper avant qu'elle ne devienne une surprise.

**Grande entreprise.** Une entreprise de médias exploitant une fonctionnalité LLM à haut trafic a réduit substantiellement les coûts d'inférence. Elle a acheminé les requêtes faciles vers un petit modèle et réservé un plus grand modèle pour les difficiles. Elle a mis en cache les réponses aux requêtes répétées et activé la mise en cache de préfixe pour son prompt système partagé. Elle a exécuté les GPU à travers un planificateur partagé pour garder l'utilisation haute, versionné tous les prompts dans git avec une suite d'évaluation automatisée conditionnant les changements, et instrumenté le coût par requête pour que chaque équipe produit possède sa dépense.

**Gouvernement.** Une agence nationale avec des règles strictes de souveraineté des données a déployé ses systèmes d'IA sur site pour que les données sensibles et modèles ne quittent jamais son environnement contrôlé. Elle a planifié les GPU rares à travers les départements avec des quotas et priorités, prévu la capacité pour justifier l'approvisionnement pluriannuel, et construit une plateforme de recherche vectorielle pour la récupération sur des documents officiels. Les prompts et modèles étaient versionnés et évalués avant la sortie. Une observabilité complète suivait le coût et la qualité, et l'architecture gardait les modèles derrière une interface interne pour préserver un chemin de sortie et éviter le verrouillage.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La motivation pour une infrastructure d'IA disciplinée est directe. L'IA à l'échelle est coûteuse, et l'écart entre un déploiement optimisé et non optimisé est souvent de plusieurs fois en dépense. Le retour sur investissement vient d'une utilisation d'accélérateur plus haute, d'un coût par requête plus bas à travers le groupement et la mise en cache, de modèles bien dimensionnés, et d'éviter le sur-approvisionnement. Les pipelines d'observabilité et d'évaluation paient en prévenant les incidents coûteux et en permettant l'itération en sécurité.

Le coût total de possession couvre le calcul d'accélérateur (la plus grande ligne pour de nombreuses charges de travail), le stockage vectoriel, l'infrastructure de service, le réseautage, et le personnel de plateforme et opérations pour l'exploiter. Pesez cela contre le coût de ne pas investir : des factures d'inférence galopantes, une mauvaise latence qui mine l'adoption, et une incapacité à s'échelonner. Pour l'administration publique, ajoutez le coût d'échouer les exigences de souveraineté ou sécurité. Faites valoir cela auprès de la direction en montrant les tendances de coût par résultat et une plateforme à chemin pavé qui laisse de nombreuses équipes déployer l'IA efficacement, plutôt que chacune construisant une infrastructure coûteuse et sous-utilisée.

## Anti-patterns et pièges

- **Accélérateurs inactifs.** Dédier des GPU rares à des équipes qui les laissent sous-utilisés.
- **Aucun groupement ou mise en cache.** Servir chaque requête individuellement et recalculer le contexte partagé.
- **Le plus grand modèle par défaut.** Utiliser un modèle coûteux là où un petit suffirait.
- **Cécité de coût.** Aucune attribution, budgets, ou visibilité de coût par requête jusqu'à ce que la facture arrive.
- **Prompts non versionnés.** Changer les prompts en production sans versionnage ou porte d'évaluation.
- **Négligence de latence de queue.** Optimiser la latence moyenne pendant que les utilisateurs souffrent des queues lentes.
- **Verrouillage silencieux.** Construire profondément sur la pile de service d'un fournisseur sans portabilité.

## Modèle de maturité

1. **Initier.** Allocation de GPU au coup par coup réagissant à quiconque demande le plus fort, aucun groupement ou mise en cache, aucune visibilité de coût jusqu'à ce que la facture arrive, prompts édités en direct et non versionnés, surveillance minimale.
2. **Développer.** Certaines équipes adoptent la planification partagée, mise en cache, et prompts contrôlés en version, mais la pratique est incohérente à travers l'organisation : un groupe groupe et évalue tandis qu'un autre sert encore chaque requête individuellement et change les prompts à la main.
3. **Standardiser.** Une plateforme à chemin pavé documentée est imposée à l'échelle de l'organisation : planification partagée avec quotas et priorités, groupement, mise en cache, et dimensionnement correct standard, infrastructure vectorielle pour la récupération, pipelines d'évaluation automatisés qui conditionnent chaque changement de prompt ou modèle, et attribution de coût aux équipes et cas d'usage.
4. **Gérer.** La plateforme est mesurée et contrôlée contre des références : l'utilisation d'accélérateur, le coût par résultat utile, la latence de queue, le rappel de récupération, et les régressions de qualité par changement sont suivis avec des alertes et seuils, le coût est possédé par chaque équipe, et le feu vert ou non sur un changement est décidé sur preuve plutôt qu'intuition.
5. **Orchestrer.** L'infrastructure s'améliore et s'adapte continuellement : le routage, le groupement, et la mise à l'échelle se règlent eux-mêmes selon les signaux de coût et qualité en direct, la capacité est rééquilibrée à travers les équipes et entre les cibles cloud, sur site, et souveraines à mesure que la demande et les contraintes changent, la portabilité est répétée, et la planification d'infrastructure est intégrée avec le produit, la sécurité, et l'approvisionnement.

## Pistes de réflexion

- Comment faites-vous monter l'utilisation d'accélérateur sans affamer les charges de travail prioritaires ?
- Où se trouve le bon équilibre de groupement et mise en cache pour vos exigences de latence ?
- Quand le déploiement sur site ou souverain justifie-t-il son coût contre le cloud ?
- Comment attribuez-vous et contrôlez-vous la dépense d'IA à travers de nombreuses équipes ?
- Qu'est-ce qui devrait conditionner un changement de prompt ou modèle avant qu'il n'atteigne la production ?
- Comment gardez-vous l'infrastructure de service assez portable pour changer de fournisseur ?

## Points clés à retenir

- Les accélérateurs sont rares et coûteux ; planifiez, partagez, et utilisez-les délibérément.
- Le groupement, la mise en cache, et le dimensionnement correct de modèle sont les leviers principaux pour le coût et la latence.
- Les applications de récupération ont besoin d'une infrastructure de plongement et recherche vectorielle bien exploitée.
- LLMOps (versionnage de prompt, pipelines d'évaluation, et observabilité) est l'épine dorsale opérationnelle de l'IA générative.
- Gérez le coût de façon observable et préservez la portabilité pour éviter le verrouillage.

## Références et lectures complémentaires

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, éditeurs).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
