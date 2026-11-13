# 6.3 IA générative et applications LLM

## Vue d'ensemble et motivation

L'[IA générative](https://fr.wikipedia.org/wiki/Intelligence_artificielle_g%C3%A9n%C3%A9rative), et les [grands modèles de langage](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) (LLM) en particulier, peuvent produire du texte fluide, du code, des résumés, et des données structurées à partir d'instructions en langage naturel. Cela en fait de puissants blocs de construction pour les assistants, la recherche, le traitement de document, et l'automatisation. Mais ces forces viennent avec un profil de risque distinctif. Les LLM sont probabilistes. Ils peuvent produire des faussetés confiantes ([hallucinations](https://fr.wikipedia.org/wiki/Hallucination_%28intelligence_artificielle%29)). Ils sont sensibles à comment vous les invitez. Et ils ouvrent de nouvelles surfaces d'attaque telles que l'[injection de prompt](https://fr.wikipedia.org/wiki/Injection_de_prompt) (instructions malveillantes contrebandées dans les entrées pour détourner le comportement du modèle). Donc construire des applications LLM fiables concerne moins le modèle et plus l'ingénierie autour de lui : comment vous fournissez le contexte, ancrez les réponses dans une connaissance de confiance, contraignez les sorties, et évaluez la qualité.

Pour les grandes équipes, les applications LLM exigent de nouveaux motifs qui diffèrent à la fois du logiciel traditionnel et de l'apprentissage automatique classique. Il n'y a souvent pas d'étape d'entraînement. Au lieu de cela, le comportement est façonné par les prompts, le contexte récupéré, les définitions d'outil, et les garde-fous (contrôles d'exécution qui contraignent les entrées et sorties du modèle). Cela déplace l'effort d'ingénierie vers la gestion de contexte, la qualité de récupération, l'orchestration, et l'évaluation. Les entreprises adoptant les LLM à l'échelle ont besoin de motifs partagés pour que chaque équipe ne redécouvre pas les mêmes modes d'échec de la façon difficile.

L'administration publique et les organisations régulées font face à des demandes supplémentaires. Un LLM qui fabrique une citation de politique ou fuit des données sensibles n'est pas simplement un bogue ; cela peut être un incident légal ou de sécurité. Ces contextes ont besoin d'ancrage dans des sources faisant autorité, de validation de sortie stricte, de surveillance humaine pour les sorties conséquentes, et d'enregistrements clairs de ce qu'on a demandé au système et ce qu'il a produit. Les techniques de ce chapitre (génération augmentée par récupération, garde-fous, et évaluation rigoureuse) sont ce qui rend les LLM assez sûrs pour être déployés dans des contextes à haut enjeu. Les modèles Claude d'Anthropic sont une option de premier plan parmi plusieurs fournisseurs compétents ; les pratiques ici s'appliquent peu importe le modèle que vous choisissez.

## Principes clés

- Ancrez le modèle dans une connaissance de confiance plutôt que de compter sur ce qu'il a mémorisé.
- Traitez les prompts et le contexte comme des artefacts conçus et versionnés, pas des chaînes jetables.
- Supposez que le modèle peut se tromper ou être manipulé ; validez les sorties et contraignez les actions.
- Donnez au modèle seulement le contexte et les outils dont il a besoin, pas plus, pour réduire l'erreur et la surface d'attaque.
- Évaluez continuellement avec des ensembles de test hors ligne, des métriques en ligne, et le jugement humain.
- Gardez des humains dans la boucle pour les sorties conséquentes.
- Concevez pour le modèle comme un composant non fiable dans un système fiable.

## Recommandations

### Concevoir les prompts et gérer le contexte délibérément

Traitez les prompts comme du code : stockez-les dans le contrôle de version, révisez les changements, et testez-les contre une suite d'exemples. Structurez chaque prompt clairement : rôle et tâche, contraintes, exigences de format, et exemples où ils aident. Traitez la fenêtre de contexte (l'étendue fixe de texte que le modèle peut considérer à la fois) comme une ressource rare. Incluez l'information la plus pertinente, ordonnez-la soigneusement, et retirez le bruit, parce qu'un contexte non pertinent ou excessif dégrade la qualité et élève le coût. Pour les applications multi-tours, gérez l'état de conversation explicitement, résumant ou tronquant l'historique pour rester dans les limites tout en gardant ce qui compte. Préférez des instructions claires et des exemples few-shot (une poignée de démonstrations travaillées incluses dans le prompt) aux astuces élaborées qui se cassent au moment où un modèle change.

### Ancrer les réponses avec la génération augmentée par récupération (RAG)

Pour les tâches à forte intensité de connaissance, récupérez des documents pertinents depuis un corpus de confiance et fournissez-les au modèle comme contexte, en lui disant de répondre seulement depuis ce matériel et de citer ses sources. RAG garde la connaissance actuelle sans réentraînement, confine les réponses au contenu approuvé, et permet la citation et vérification. Investissez dans la qualité de récupération : découpez les documents sensément, choisissez des [plongements](https://fr.wikipedia.org/wiki/Word_embedding) (représentations vectorielles numériques qui placent des sens similaires proches) adaptés à votre domaine, et vérifiez si les passages récupérés contiennent réellement la réponse, parce qu'une réponse fluide construite sur le mauvais passage est pire qu'aucune réponse. Et quand rien de pertinent n'apparaît, faites en sorte que le système le dise plutôt que d'inventer du contenu.

### Construire des agents et un usage d'outil avec retenue

Les LLM peuvent appeler des outils (recherche, bases de données, calculatrices, API internes) et peuvent être composés en agents qui planifient et agissent sur plusieurs étapes. Cela ajoute une vraie capacité, mais cela multiplie aussi le risque : chaque outil est une autre façon pour un modèle faux ou manipulé de causer du dommage. Définissez les outils avec des schémas précis, validez chaque argument, appliquez le moindre privilège, et exigez une confirmation ou approbation humaine pour les actions conséquentes telles qu'envoyer des communications ou déplacer de l'argent. Gardez les boucles d'agent bornées, observables, et interruptibles. Commencez avec des outils étroitement cadrés et à but unique avant de recourir à l'autonomie ouverte.

### Ajouter des garde-fous et valider les sorties

Enveloppez le modèle dans des couches de défense. À l'entrée, filtrez et détectez l'injection de prompt, spécialement quand du contenu non fiable (pages web, documents utilisateur) entre dans le contexte. À la sortie, validez la structure contre un schéma, vérifiez les affirmations contre des sources, filtrez le contenu dangereux ou non conforme, et rejetez ou retentez quand la validation échoue. Pour les sorties structurées, analysez et vérifiez plutôt que de faire confiance au formatage du modèle. Ne laissez jamais la sortie brute du modèle déclencher des actions irréversibles sans validation. Traitez l'atténuation d'hallucination comme une propriété système que vous atteignez à travers l'ancrage, la citation, la validation, et la revue humaine, pas quelque chose que le modèle gère seul.

### Évaluer hors ligne, en ligne, et avec des humains

Construisez une suite d'évaluation d'entrées représentatives avec des sorties connues-bonnes ou notées par rubrique, et exécutez-la à chaque changement de prompt ou modèle (évaluation hors ligne). Mesurez le vrai comportement en production avec des métriques telles que le succès de tâche, le taux d'escalade, et le retour utilisateur (évaluation en ligne). Pour la qualité subjective, utilisez des relecteurs humains et, prudemment, la notation basée sur modèle. L'évaluation est le filet de sécurité qui vous permet de changer les prompts et modèles avec confiance. Sans elle, vous volez à l'aveugle.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients | Le mieux quand |
|---|---|---|---|
| Invitation pure | Simple, rapide, bon marché à changer | Ancrage limité, peut halluciner | Tâches larges, faible enjeu |
| RAG | Actuel, ancré, citable | La récupération est difficile à bien faire | Tâches riches en connaissance, factuelles |
| Agents avec outils | Puissant, peut agir | Surface d'attaque plus large, plus difficile à contrôler | Automatisation bien cadrée avec garde-fous |
| Modèle plus grand et plus fort | Meilleure qualité et raisonnement | Coût et latence plus élevés | Tâches complexes ou à haut enjeu |
| Modèle plus petit et moins cher | Rapide et peu coûteux | Plus faible sur les tâches difficiles | Volume élevé, tâches simples |

La tension centrale est la capacité contre le contrôle et le coût. Plus d'autonomie et des modèles plus grands livrent plus de valeur, mais ils exigent plus de garde-fous, plus d'évaluation, et plus d'argent. L'ancrage via RAG améliore la fiabilité au coût de l'ingénierie de récupération. Le bon équilibre dépend des enjeux : les applications à haut enjeu penchent vers l'ancrage, la validation, et la surveillance humaine, même quand cela coûte plus.

## Questions à discuter avec votre équipe

1. **Quelle barre de précision et d'ancrage une fonctionnalité LLM doit-elle franchir avant de faire face au public, et qui l'approuve ?** Une réponse fluide qui cite la mauvaise source ou invente une politique est pire qu'aucune réponse, et dans l'administration publique une citation fabriquée est un incident légal, pas un bogue. Pour une grande équipe, une barre explicite empêche chaque groupe de fixer son propre seuil privé à l'impression. Apportez votre définition d'« assez ancré » : si chaque affirmation doit se retracer à une source récupérée et vérifiée, si le système doit refuser quand la récupération revient vide, et ce que votre ensemble d'évaluation adversarial couvre réellement. Le signal à surveiller est si quelqu'un peut actuellement livrer un changement de prompt directement aux utilisateurs sans exécution de régression. Si les enjeux sont légaux ou liés à la sécurité, la réponse devrait acheminer les sorties à plus haut risque à travers un relecteur humain avec une vraie autorité avant la sortie.

2. **Lesquelles de nos fonctionnalités LLM sont secrètement des agents, et chaque outil a-t-il reçu le moindre privilège et une porte humaine sur les actions irréversibles ?** Toute fonctionnalité qui laisse le modèle appeler des outils ou agir sur plusieurs étapes a traversé le territoire d'agent, et chaque outil est une autre façon pour un modèle faux ou manipulé de causer du dommage. Pour les entreprises câblant des LLM dans des API internes, cette question fait émerger un risque qu'une étiquette « assistant simple » cache. Apportez un inventaire de chaque outil que le modèle peut invoquer, sa validation d'argument, sa portée de privilège, et quelles actions (envoyer des communications, déplacer de l'argent, changer des enregistrements) exigent une confirmation. Discutez si les boucles d'agent sont bornées, observables, et interruptibles. La réponse devrait resserrer les portées et ajouter des portes d'approbation humaine partout où une action conséquente ou irréversible est actuellement atteignable sans une.

3. **Comment saurions-nous en un jour que notre qualité de récupération a chuté, étant donné qu'une réponse confiante construite sur le mauvais passage paraît bien ?** RAG rend les réponses dignes de confiance seulement quand la récupération fait réellement émerger le passage qui contient la réponse, et la récupération pourrit silencieusement à mesure que les documents changent, les morceaux deviennent périmés, ou les plongements dérivent de votre domaine. Parce que le modèle écrit encore fluidement sur un mauvais contexte, les utilisateurs peuvent ne pas se plaindre avant que la confiance ne soit déjà perdue. Apportez vos mesures actuelles de latence et rappel de récupération, comment vous vérifiez si les passages récupérés contiennent véritablement la réponse, et comment la fraîcheur de l'index suit le rythme des changements de document. Pour les déploiements à haut enjeu ou publics, discutez de journaliser les sources récupérées pour l'audit pour que vous puissiez tracer une mauvaise réponse à son mauvais passage. Si vous n'avez aucune évaluation de récupération du tout, vous ancrez sur la foi.

4. **Traitons-nous les prompts, contexte, et ensembles d'évaluation comme des artefacts versionnés et révisés, ou comme des chaînes éparpillées à travers des carnets et journaux de chat ?** Quand les prompts s'étalent à travers les équipes non versionnés et dupliqués, une correction à un endroit n'atteint jamais les autres, et personne ne peut reproduire ce qu'on a demandé au système de faire le trimestre dernier. Pour une grande équipe, un registre de prompt partagé et une suite de régression qui s'exécute à chaque changement sont ce qui vous permet d'échanger un modèle ou d'éditer une instruction sans casser discrètement une fonctionnalité de deux équipes plus loin. L'attraction concurrente est la vitesse : les ingénieurs itèrent le plus vite quand ils collent un prompt et livrent, donc convenez où se trouve la ligne entre les expériences rapides et tout ce qui touche les utilisateurs. Apportez où vos prompts vivent réellement aujourd'hui, si un ensemble d'évaluation conditionne les changements, et comment vous versionnez le corpus de récupération aux côtés du prompt. Dans les contextes d'entreprise et gouvernementaux, ajoutez l'exigence d'audit : vous pourriez devoir montrer exactement quel prompt et quelles sources ont produit une sortie donnée des mois plus tard, et un prompt que vous ne pouvez pas reconstruire est un enregistrement que vous ne pouvez pas défendre.

5. **À mesure que le volume croît, comment contrôlerons-nous le coût d'inférence sans dégrader discrètement la qualité, et qui possède la décision de sélection de modèle ?** Le coût total de possession pour les fonctionnalités LLM est dominé par l'inférence par appel, et les coûts qui paraissent triviaux dans un pilote se composent vite à l'échelle de production, tentant les équipes de discrètement descendre vers un modèle plus faible et espérer que personne ne remarque le glissement de qualité. Pour une grande organisation, laisser chaque équipe choisir les modèles et limites de coût à l'instinct produit à la fois des factures surprises et une qualité incohérente. Le vrai compromis est la capacité contre le coût et la latence : un modèle plus grand raisonne mieux sur les tâches difficiles, un plus petit est moins cher et plus rapide sur les simples, et la mise en cache, le routage, et la portée de récupération déplacent tous le chiffre. Apportez le coût par tâche résolue, la qualité par niveau de modèle sur votre ensemble d'évaluation, et où le gonflement de prompt ou contexte inflate les dépenses de jeton. Dans la budgétisation d'entreprise et gouvernementale, nommez qui approuve le choix de modèle et le plafond de dépense, parce qu'une ligne de coût que personne ne possède est une que personne ne contrôle quand le trafic triple.

6. **Quelles données sensibles peuvent atteindre le modèle, où vont ces données, et pouvons-nous prouver qu'elles sont restées dans les limites ?** Chaque prompt, document récupéré, et résultat d'outil peut porter des données personnelles ou confidentielles dans le modèle et, avec un fournisseur hébergé, hors de votre périmètre, et une fuite ici est un incident légal ou de sécurité, pas un ticket de défaut. Pour une grande équipe câblant des LLM dans des systèmes internes, le risque se cache dans la plomberie : un corpus de récupération qui inclut des enregistrements qu'un utilisateur donné ne devrait jamais voir, ou des journaux qui capturent des entrées brutes. La tension est la capacité contre l'exposition, puisque la rédaction et le cadrage étroit peuvent émousser la fonctionnalité que vous essayez de construire. Apportez une carte de flux de données de ce qui entre dans le contexte, les termes de rétention et d'entraînement du fournisseur, et comment vous rédigez, cadrez, et journalisez les champs sensibles. Dans les contextes régulés et publics, liez cela aux règles de résidence de données, devoirs de rétention d'enregistrements, et limites contractuelles sur comment un fournisseur peut utiliser vos données, parce qu'une surveillance que vous ne pouvez pas prouver est une surveillance que vous n'avez pas.

## Regard sectoriel

**Jeune pousse.** Livrez une fonctionnalité LLM étroite qui touche votre valeur centrale, construite sur un modèle hébergé avec récupération sur votre propre contenu, et gardez les prompts dans git derrière une interface mince pour pouvoir échanger de fournisseurs. Exécutez un petit fichier d'évaluation de vraies questions avant chaque changement, filtrez le texte utilisateur collé pour émousser l'injection de prompt, et plafonnez fermement la dépense mensuelle. Résistez aux agents et à l'auto-hébergement : une boucle d'appel d'outil non bornée que vous ne pouvez pas superviser est un passif, pas une démonstration.

**Petite entreprise.** Vous n'avez probablement pas de spécialiste d'apprentissage automatique, donc achetez des fonctionnalités LLM intégrées dans des outils que vous utilisez déjà plutôt que de doter une construction. Cadrez le risque comme une question simple : où une mauvaise réponse confiante vous coûterait-elle un client, et qui vérifie la sortie avant qu'elle ne sorte. Préférez les fournisseurs qui montrent leurs sources, vous laissent garder un humain dans la boucle, et rendent l'IA facile à désactiver quand elle se comporte mal.

**Grande entreprise.** Le problème est l'échelle à travers de nombreuses équipes : publiez des motifs partagés pour RAG, garde-fous, et schémas d'outil, plus un harnais d'évaluation commun et un registre de prompt pour que chaque groupe arrête de redécouvrir les mêmes modes d'échec. Budgétisez explicitement le coût d'inférence et la revue humaine, standardisez la couche d'interface pour que les modèles restent interchangeables, et gouvernez les agents centralement avec le moindre privilège, des boucles bornées, et une journalisation d'audit. Gérez les fonctionnalités LLM comme un portefeuille avec des métriques et critères de mort, pas une dispersion de pilotes.

**Gouvernement.** La transparence, les règles d'approvisionnement, et la responsabilité façonnent chaque choix. Ancrez strictement dans des sources approuvées avec des citations, refusez quand la récupération revient vide, et interdisez au modèle d'énoncer une loi qu'il ne peut pas citer. Gardez un fonctionnaire responsable révisant les sorties conséquentes, journalisez les entrées et sources récupérées pour l'audit, exécutez un ensemble d'évaluation adversarial avant chaque sortie, et exigez la divulgation des limitations de modèle et termes de gestion de données dans le contrat.

## Exemples

**Jeune pousse.** Une jeune pousse d'outils de développeur à trois personnes a ajouté un assistant de chat par-dessus sa propre documentation pour que les utilisateurs arrêtent d'envoyer par courriel des questions de base. Elle a utilisé RAG pour que chaque réponse cite une page de documentation spécifique, instruit le modèle de dire « Je ne suis pas sûr, voici à qui demander » quand la récupération revenait vide, et gardé ses prompts dans git. Avant chaque changement elle a exécuté les prompts contre un petit fichier de vraies questions d'utilisateur pour attraper les régressions, et a filtré le texte collé par l'utilisateur pour émousser l'injection de prompt. L'assistant a géré les questions courantes et discrètement transmis le reste à la boîte de réception partagée des fondateurs.

**Grande entreprise.** Une entreprise logicielle a construit un assistant de support interne par-dessus sa documentation de produit. Elle a utilisé [RAG](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_augment%C3%A9e_de_r%C3%A9cup%C3%A9ration) pour que les réponses citent des pages de documentation spécifiques, dit au modèle de dire « je ne sais pas » quand la récupération échouait, et vérifié que chaque source citée existait réellement. Les prompts étaient contrôlés en version et testés contre une suite de vraies questions de support à chaque changement. L'assistant a dévié les tickets routiniers et escaladé tout ce qui était à faible confiance vers des agents humains, tandis que des métriques en ligne suivaient les taux de résolution et de correction.

**Gouvernement.** Une agence publique a déployé un assistant LLM pour aider le personnel à rédiger des réponses aux requêtes citoyennes. L'ancrage était strict : le modèle ne pouvait composer des réponses qu'à partir de directives approuvées avec citations, et il lui était interdit d'énoncer une politique qui n'était pas présente dans les sources récupérées. Un fonctionnaire responsable révisait chaque brouillon avant qu'il ne sorte. Le filtrage d'entrée gardait contre l'injection de prompt depuis les documents soumis par citoyens, les sorties étaient journalisées pour l'audit, et un ensemble d'évaluation de requêtes adversariales et de cas limites s'exécutait avant chaque sortie pour confirmer que le système refusait de spéculer sur des questions de droit.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Les applications LLM livrent un retour sur investissement en automatisant le travail riche en langage : répondre à des questions, résumer des documents, rédiger du contenu, et extraire de la structure depuis du texte non structuré. La valeur se manifeste comme des tickets déviés, une rédaction plus rapide, moins de revue manuelle, et de nouvelles capacités en libre-service. Parce qu'il n'y a souvent pas d'étape d'entraînement, le temps jusqu'à la première valeur est court, un attrait majeur.

Le coût total de possession, cependant, est dominé par le coût d'inférence continu, l'infrastructure de récupération, les pipelines d'évaluation, les systèmes de garde-fous, et la revue humaine. Les coûts par appel s'additionnent rapidement à l'échelle, et une application non surveillée peut dériver vers un comportement dangereux ou coûteux. Le coût de ne pas adopter est de prendre du retard sur la qualité de service et la productivité du personnel. Le coût d'adopter avec négligence est un incident d'hallucination public ou une fuite de données. Faites valoir cela auprès de la direction en associant une cible de productivité concrète à un plan de sécurité et d'évaluation concret, et en budgétisant pour les garde-fous et la surveillance humaine qui gardent la valeur durable.

## Anti-patterns et pièges

- **Faire confiance à la sortie fluide.** Confondre un texte confiant et bien écrit avec un texte correct.
- **RAG sans évaluation de récupération.** Supposer que la récupération fonctionne et ne jamais vérifier si elle fait émerger les bons passages.
- **Aveuglement à l'injection de prompt.** Alimenter du contenu non fiable dans les prompts sans défenses.
- **Agents non bornés.** Laisser les agents prendre des actions conséquentes sans limites ou approbation humaine.
- **Aucun harnais d'évaluation.** Changer les prompts et modèles à l'instinct, sans test de régression.
- **Étalement de prompt.** Prompts éparpillés, non versionnés, et dupliqués à travers les équipes.
- **Sur-automatisation.** Retirer les humains des décisions qui portent un poids légal ou de sécurité.

## Modèle de maturité

1. **Initier.** Invitation au coup par coup dans des projets isolés ; aucun ancrage, garde-fou, ou évaluation ; les prompts vivent partout où quelqu'un les a collés, et les hallucinations sont découvertes en production.
2. **Développer.** Certaines équipes ajoutent RAG et versionnage de prompt, validation de sortie de base, et un petit ensemble d'évaluation manuel, mais les pratiques varient d'équipe à équipe et reposent sur des champions individuels plutôt qu'une attente partagée.
3. **Standardiser.** Des motifs documentés pour RAG, garde-fous, schémas d'outil, et versionnage de prompt sont imposés à l'échelle de l'organisation ; l'évaluation hors ligne automatisée s'exécute à chaque changement de prompt ou modèle ; les flux à haut enjeu portent des métriques en ligne et revue humaine.
4. **Gérer.** Le portefeuille est mesuré contre des références : le rappel de récupération, les taux d'hallucination et de refus, la couverture de défense d'injection, le coût et la latence par appel, et les taux d'escalade et de correction sont suivis sur des tableaux de bord ; les portes de sortie et critères de mort se déclenchent sur preuve plutôt qu'opinion, et une exécution de régression bloque tout changement qui déplace une métrique dans la mauvaise direction.
5. **Orchestrer.** L'évaluation continue hors ligne et en ligne est liée aux résultats d'affaires ; les défenses d'injection, agents, et ancrage sont gouvernés et observables ; l'organisation retire, réajuste, et recadre routinièrement les fonctionnalités LLM, et échange les modèles à mesure que la qualité, le coût, et le risque changent.

## Pistes de réflexion

- Comment décidez-vous quelles sorties exigent une revue humaine avant usage ?
- Quelle est votre norme pour « assez ancré » avant qu'une réponse ne puisse être montrée aux utilisateurs ?
- Comment vous défendez-vous contre l'injection de prompt quand du contenu non fiable doit entrer dans le contexte ?
- Quand un agent vaut-il son risque ajouté contre une conception plus simple à un seul appel ?
- Comment évaluez-vous la qualité subjective à l'échelle sans trop compter sur la notation basée sur modèle ?
- Comment gardez-vous les prompts maintenables et cohérents à travers de nombreuses équipes ?

## Points clés à retenir

- La fiabilité vient de l'ingénierie autour du modèle : contexte, ancrage, garde-fous, et évaluation.
- RAG ancre les réponses dans des sources de confiance et permet la citation et vérification.
- Traitez le modèle comme un composant non fiable ; validez les sorties et contraignez l'usage d'outil.
- Donnez aux agents le moindre privilège, des boucles bornées, et une approbation humaine pour les actions conséquentes.
- Évaluez continuellement hors ligne, en ligne, et avec des humains ; c'est ce qui rend le changement sûr.

## Références et lectures complémentaires

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (directive d'ingénierie).
- Louis-François Bouchard et Louie Peters, *Building LLMs for Production*.
