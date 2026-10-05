# 10.6 Gestion de projet

## Vue d'ensemble et motivation

La **[gestion de projet](https://fr.wikipedia.org/wiki/Gestion_de_projet)** est la discipline de transformer l'intention en résultats livrés sous contraintes. Vous coordonnez les gens, la portée, le calendrier, le coût, le risque, et la qualité pour que le travail se termine réellement et livre de la valeur. Dans le logiciel, elle est souvent traitée avec suspicion, liée à des plans lourds et des **[diagrammes de Gantt](https://fr.wikipedia.org/wiki/Diagramme_de_Gantt)** que la réalité ignore. Mais le besoin sous-jacent ne disparaît jamais. Quelqu'un doit s'assurer que le bon travail se produit dans le bon ordre, que les dépendances sont gérées, que les risques font surface tôt, et que les **[parties prenantes](https://fr.wikipedia.org/wiki/Partie_prenante)** savent à quoi s'attendre. La question n'est pas *si* gérer les projets, mais *à quel point légèrement et adaptativement* vous pouvez le faire tout en respectant vos obligations.

Pourquoi traiter cela explicitement ? Les projets logiciels échouent à des taux alarmants, et ils échouent bien plus souvent pour des raisons de gestion que pour des raisons purement techniques : portée peu claire, dépendances non gérées, risque non adressé, parties prenantes absentes, et le fantasme d'estimations précises à long terme. Les grands programmes sont particulièrement exposés : avec de nombreuses équipes, fournisseurs, et horizons multi-trimestriels, de petits échecs de coordination se composent. La bonne gestion de projet est largement la pratique de prendre des engagements honnêtement, décomposer le travail sensiblement, et créer une rétroaction rapide pour que les problèmes fassent surface tant qu'ils sont encore bon marché à corriger.

Les contextes d'entreprise et gouvernementaux élèvent les enjeux et changent les contraintes. Les entreprises gèrent des portefeuilles d'initiatives entrelacées contre la stratégie et les cycles budgétaires (chapitre 10.1). Les gouvernements ajoutent les règles de marchés publics, les crédits pluriannuels, la gestion de sous-traitant, et la responsabilité publique. Là, le défaut historique (contrats grands, à portée fixe, en **[cascade](https://fr.wikipedia.org/wiki/Cycle_en_cascade)**) a un long historique d'échec coûteux et visible. Ce chapitre couvre les fondamentaux qui s'appliquent à travers les approches prédictive, adaptative, et hybride. Le chapitre 10.7 (Agile) approfondit la livraison adaptative, et le chapitre 10.1 couvre la gestion de portefeuille et de programme au-dessus du projet unique.

## Principes clés

- **Gérez les résultats, pas l'activité.** Terminé signifie valeur livrée, pas tâches fermées.
- **Décomposez et séquencez.** Un travail petit, ordonné, et conscient des dépendances bat les plans big bang.
- **Les estimations sont des plages, pas des promesses.** Communiquez l'incertitude honnêtement.
- **Faites surgir le risque tôt et continuellement.** Le problème le moins cher est celui attrapé en premier.
- **Assortissez la méthode au travail.** Prédictive, adaptative, ou hybride : adaptez-vous à l'incertitude et aux contraintes.
- **Rendez le statut transparent.** Un flux visible bat les rapports rassurants.
- **Les parties prenantes font partie de l'équipe.** L'absence du client est un risque de projet.

## Recommandations

### Choisir délibérément le prédictif, l'adaptatif, ou l'hybride

Il n'y a pas de modèle de livraison universellement correct ; il y a un ajustement entre la méthode et le contexte :

- **Prédictif (piloté par plan, « cascade ») :** portée fixée à l'avance, puis calendrier et coût dérivés. Convient au travail avec des exigences véritablement stables et bien comprises et des contraintes externes dures (certification réglementaire, intégration physique). Son mode d'échec est de prétendre que les exigences logicielles sont stables quand elles ne le sont pas.
- **Adaptatif (**[agile](https://fr.wikipedia.org/wiki/D%C3%A9veloppement_agile)**) :** la portée fléchit ; le temps et le coût sont fixés en courtes itérations qui livrent du logiciel fonctionnel et absorbent l'apprentissage. Convient à la plupart du travail de produit et de service numérique, où les exigences sont découvertes (chapitres 11.1, 10.7).
- **Hybride :** un noyau adaptatif à l'intérieur d'une coquille de gouvernance prédictive, courant et souvent correct en entreprise et gouvernement, où le financement, la conformité, et la contractualisation exigent des jalons et de l'audit tandis que la livraison bénéficie de l'itération.

Des cadres comme **[PMBOK](https://fr.wikipedia.org/wiki/Project_Management_Body_of_Knowledge)** (le corpus de connaissances en gestion de projet, du **[Project Management Institute](https://fr.wikipedia.org/wiki/Project_Management_Institute)**) et **[PRINCE2](https://fr.wikipedia.org/wiki/PRINCE2)** (PRojects IN Controlled Environments) codifient la pratique prédictive et hybride. Le but est d'emprunter leur discipline (rôles, risque, portes d'étape) sans importer le cérémonial dont le travail n'a pas besoin.

### Gérer la portée contre la triple contrainte

Portée, calendrier, et coût se déplacent ensemble, bornés par la qualité : le classique **[« triangle de fer »](https://fr.wikipedia.org/wiki/Triangle_de_gestion_de_projet)**. Vous ne pouvez pas fixer les trois et ajouter de la portée gratuitement. Quelque chose cède, et prétendre le contraire est comment les **[marches de la mort](https://fr.wikipedia.org/wiki/Marche_de_la_mort_%28gestion_de_projet%29)** commencent. Rendez les compromis explicites, et décidez *quelle* variable fléchit. Les méthodes adaptatives fixent le temps et le coût et fléchissent la portée. Les contrats à prix fixe fixent la portée et le coût, et en réalité fléchissent la qualité ou le calendrier sauf si vous les gérez. Contrôlez la **[dérive de portée](https://fr.wikipedia.org/wiki/D%C3%A9rive_de_p%C3%A9rim%C3%A8tre)** avec un processus de changement léger (chapitre 12.3), et préférez *réduire la portée vers un noyau précieux* plutôt que tout laisser glisser.

### Estimer honnêtement, en plages, et re-prévoir

L'estimation est où les projets se mentent le plus souvent à eux-mêmes. Traitez les estimations comme des plages probabilistes, pas des chiffres uniques, et élargissez-les pour le travail distant et mal compris (le **[« cône d'incertitude »](https://fr.wikipedia.org/wiki/Cone_of_Uncertainty)**). Préférez les méthodes relatives et empiriques : le débit historique et le temps de cycle (chapitres 11.2, 11.3) prévoient mieux que les suppositions héroïques ascendantes. Là où vous le pouvez, remplacez l'estimation par la *mesure*. Une équipe fermant 8 éléments/semaine prendra environ 5 semaines pour 40 éléments, indépendamment des points d'histoire (la **[loi de Little](https://fr.wikipedia.org/wiki/Loi_de_Little)** encore : le débit et le travail en cours, pas les estimations, fixent le temps de livraison). Re-prévoyez continuellement à mesure que la réalité arrive. Un plan qui ne change jamais n'est pas géré.

### Gérer les dépendances et le chemin critique

À l'échelle, le risque dominant est rarement la vélocité d'une seule équipe. C'est les *dépendances entre équipes et fournisseurs*. Cartographiez-les explicitement, identifiez le **[chemin critique](https://fr.wikipedia.org/wiki/M%C3%A9thode_du_chemin_critique)** (la séquence qui détermine la fin la plus précoce), et attaquez d'abord les dépendances les plus longues et les plus risquées. Réduisez le couplage où vous le pouvez (une dépendance retirée vaut plus qu'une dépendance suivie) et utilisez des interfaces et contrats clairs pour que les équipes puissent progresser en parallèle (chapitres 1.2, 2.3). Pour les programmes inter-équipes, une synchronisation régulière de dépendance et de risque bat un rapport de statut que personne ne lit.

### Exploiter un registre de risque vivant

La gestion de risque est l'activité de gestion de projet à plus fort levier, et la plus souvent sautée. Gardez un **[registre de risque](https://fr.wikipedia.org/wiki/Registre_des_risques)** simple et vivant : chaque risque avec sa probabilité, impact, propriétaire, et atténuation ou contingence (chapitre 12.3). Révisez-le régulièrement, retirez les risques qui sont passés, et ajoutez-en de nouveaux à mesure qu'ils émergent. Distinguez les risques (pourrait arriver) des problèmes (déjà en train d'arriver) et des décisions (chapitre 1.6). Le but n'est pas un document. C'est une habitude de regarder en avant, pour que vous anticipiez les problèmes au lieu de les découvrir à l'échéance.

### Engager les parties prenantes et communiquer de façon transparente

La plupart des échecs de projet « surprise » étaient visibles tôt à quelqu'un qui n'a pas été entendu. Identifiez les parties prenantes, comprenez leurs préoccupations, et gardez-les véritablement impliquées. L'absence du client est elle-même un risque de premier ordre. Communiquez le statut à travers un *flux transparent* (tableaux visibles, graphiques de burn-up, logiciel fonctionnel démontré) plutôt que des rapports vert-jaune-rouge qui récompensent l'optimisme. Escaladez honnêtement et tôt. Un projet bien géré fait voyager rapidement les mauvaises nouvelles.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| **Prédictif / cascade** | Portée et coût prévisibles ; adapté au contrat et à l'audit | Mauvais ajustement pour les exigences incertaines ; rétroaction tardive ; risque big bang |
| **Adaptatif / agile** | Rétroaction rapide ; absorbe le changement ; valeur précoce | Plus difficile de fixer la portée/coût à l'avance ; a besoin d'un client engagé |
| **Hybride** | Itération à l'intérieur de la gouvernance ; convient à l'entreprise/gouvernement | Tension entre les cadences ; peut hériter des deux jeux de surcharge |
| **Estimations détaillées à l'avance** | Confort pour les planificateurs et bailleurs de fonds | Précisément faux ; coûteux à produire ; se décomposent rapidement |
| **Prévision empirique (métriques de flux)** | Ancrée, auto-corrective | Exige de l'historique et de la discipline ; semble moins « certaine » |
| **Cérémonial lourd de risque/processus** | Approfondi ; bon pour les programmes à enjeux élevés | Ralentit les petites équipes ; peut devenir du cochage de case |

La tension centrale est **prévisibilité contre adaptabilité**. Les bailleurs de fonds, contrats, et audits veulent des engagements fermes. Le travail logiciel incertain a besoin d'espace pour apprendre. Résolvez-la comme le fait l'Agile (chapitre 10.7) : engagez-vous fermement vers les résultats et échéances tout en laissant la portée fléchir, et utilisez la gouvernance hybride pour satisfaire la surveillance sans geler la livraison.

## Questions à discuter avec votre équipe

1. **Comment envelopperez-vous les équipes de livraison adaptatives dans une coquille de gouvernance prédictive sans hériter de la surcharge des deux ?** L'hybride est courant et souvent correct en entreprise et gouvernement, où les cycles de financement, la conformité, et la contractualisation exigent des jalons et de l'audit tandis que la livraison bénéficie de l'itération. Le risque est réel : un hybride mal conçu hérite de la documentation lourde de la cascade et du cérémonial de l'agile à la fois, et les équipes ressentent la friction de deux cadences qui se battent. Apportez des preuves : cartographiez où vos portes de financement, points de contrôle de conformité, et jalons contractuels tombent réellement, et vérifiez si chacun exige un document que le travail de livraison ne produit pas autrement. La réponse devrait laisser l'itération satisfaire la surveillance plutôt que la combattre, en alimentant le rythme de gouvernance avec des incréments fonctionnels démontrés et un registre de risque vivant au lieu de s'arrêter pour assembler des rapports séparés. Empruntez la discipline d'un cadre comme PRINCE2 sans importer le cérémonial dont le travail n'a pas besoin.

2. **Le statut de votre projet est-il un flux transparent, ou des rapports vert-jaune-rouge qui récompensent l'optimisme ?** La plupart des échecs surprise étaient visibles tôt à quelqu'un qui n'a pas été entendu, et le statut pastèque (vert dehors, rouge dedans) est comment les mauvaises nouvelles honnêtes restent enterrées jusqu'à l'échéance. Remplacez les rapports rassurants par des tableaux visibles, des graphiques de burn-up, et du logiciel fonctionnel démontré, et faites d'escalader tôt un acte sûr plutôt qu'un risque de carrière. Apportez des preuves : regardez votre dernier projet troublé et demandez quand le premier signe d'avertissement existait contre quand la direction l'a entendu. L'absence du client est elle-même un risque de premier ordre, donc vérifiez si une partie prenante engagée est véritablement dans la boucle ou si vous construisez avec confiance vers la mauvaise chose. Un projet bien géré fait voyager rapidement les mauvaises nouvelles, et le correctif est autant culturel qu'outillage.

3. **Connaissez-vous le noyau minimal précieux vers lequel vous réduiriez la portée si le calendrier et le coût cessaient de bouger ?** Portée, calendrier, et coût se déplacent ensemble bornés par la qualité, et quand les bailleurs de fonds fixent les trois, la qualité devient la soupape de décharge silencieuse et les marches de la mort commencent. Les méthodes adaptatives fixent le temps et le coût et fléchissent la portée, ce qui ne fonctionne que si vous avez déjà décidé quelle tranche livre une vraie valeur et quelles fonctionnalités sont négociables. Apportez des preuves : pour votre publication actuelle, pouvez-vous nommer le noyau qui doit être livré et la liste que vous couperiez en premier, ou chaque fonctionnalité est-elle silencieusement traitée comme obligatoire ? La réponse devrait vous permettre de réduire la portée vers un noyau précieux plutôt que tout laisser glisser, et elle devrait être réglée avant que la pression n'arrive, pas improvisée à l'échéance. Contrôlez le reste avec un processus de changement léger pour que la dérive de portée ne mange pas la marge sur laquelle vous comptiez.

4. **Quelle dépendance inter-équipes est sur votre chemin critique en ce moment, et qui possède sa suppression ou son dérisquage ?** À l'échelle, la menace dominante est rarement la vélocité d'une équipe ; c'est la séquence de dépendances entre équipes et fournisseurs qui fixe la fin la plus précoce possible. Si personne ne peut nommer la dépendance de chemin critique actuelle, vous gérez le progrès local pendant que la chose qui gouverne réellement votre date dérive sans surveillance. Apportez des preuves : une carte de dépendance montrant quels transferts alimentent lesquels, où la chaîne la plus longue court, et quels liens sont encore non construits ou contractuellement bloqués, plus un propriétaire nommé pour chaque lien risqué. Visez à attaquer d'abord les dépendances les plus longues et les plus risquées et à retirer le couplage où vous le pouvez, parce qu'une dépendance supprimée vaut plus qu'une dépendance suivie. Dans les programmes d'entreprise et gouvernementaux, les liens les plus difficiles traversent souvent les frontières de fournisseur ou d'agence, donc nommez le propriétaire responsable de chaque côté et confirmez que le contrat lui permet d'agir, sinon la dépendance restera non résolue jusqu'à devenir un retard public.

5. **Comment re-prévoyez-vous à mesure que la réalité arrive, et à quelle vitesse un glissement devient-il visible aux gens qui financent le travail ?** Un plan qui ne change jamais n'est pas géré ; il est défendu, et une date à chiffre unique défendue au-delà des preuves est comment les projets glissent en silence jusqu'à l'échéance. Remplacez l'estimation par la mesure partout où vous le pouvez, prévoyant depuis le débit historique et le temps de cycle plutôt que des suppositions héroïques ascendantes, et élargissez la plage pour le travail distant et mal compris. Apportez des preuves : votre taux d'achèvement hebdomadaire réel, la taille actuelle du carnet, et la fin projetée qui en découle, comparés à la date que la direction croit actuellement. La réponse devrait donner aux bailleurs de fonds une projection honnête et rétrécissante qu'ils voient chaque cycle plutôt qu'une date fixe qui tient jusqu'à ce qu'elle s'effondre. Dans le gouvernement et d'autres contextes liés aux crédits, une prévision qui fait surgir le glissement tôt vous permet de redéfinir la portée ou rebaser dans les règles, tandis qu'un glissement caché devient un échec de surveillance et un titre.

6. **Quel est le processus le plus léger qui respecte encore vos véritables obligations, et où le cérémonial s'est-il détaché de la réduction du risque ?** La sous-gestion et la sur-gestion portent toutes deux un vrai coût : le chaos, le retravail, et les dépendances manquées d'un côté, et le cochage de case qui ralentit la livraison sans abaisser le risque de l'autre. La tension est que l'audit, la conformité, et les termes contractuels imposent de vraies exigences, pourtant les équipes ont tendance à garder chaque rituel longtemps après qu'il ait cessé de mériter sa place. Apportez des preuves : pour chaque rapport, porte, et réunion récurrents, nommez l'obligation ou risque spécifique qu'il adresse, et signalez tout ce que personne ne peut retracer à l'un ou l'autre. La réponse devrait vous permettre de retirer le cérémonial qui produit seulement du réconfort tout en préservant les artefacts qui satisfont un vrai auditeur ou bailleur de fonds. Dans les contextes d'entreprise et gouvernementaux, faites correspondre chaque cérémonial à la règle nommée de crédits, marchés publics, ou réglementaire qu'il sert, pour pouvoir défendre couper le reste à la surveillance plutôt que deviner ce que la conformité exige.

## Regard sectoriel

**Jeune pousse.** Gérez avec presque aucun cérémonial mais une vraie discipline. Décomposez la publication en petites tranches ordonnées, engagez-vous à une date de lancement tout en laissant la portée fléchir vers un noyau précieux, et citez aux fondateurs une plage au lieu d'une date unique, re-prévoyant hebdomadairement depuis combien de tranches vous fermez réellement. Un registre de risque de dix lignes dans un document partagé qui nomme la seule dépendance qui pourrait couler la date, avec un propriétaire et un plan de secours, vaut plus que tout outil, parce que votre ressource la plus rare est l'attention et un glissement que vous repérez tard peut mettre fin à l'entreprise.

**Petite entreprise.** Vous n'avez pas de gestionnaire de projet et peu de marge, donc appuyez-vous sur les outils que vous exploitez déjà plutôt que d'ériger un bureau de gouvernance. Suivez le travail sur un tableau visible, gardez une courte liste de risque vivante, et préférez acheter un produit de planification ou de billetterie plutôt que de construire le processus depuis zéro. Décidez à l'avance quelle seule fonctionnalité doit être livrée pour que la publication vaille la peine, parce que quand le calendrier se resserre, vous n'aurez pas de gens en trop pour négocier la portée sur le moment.

**Grande entreprise.** Le problème est la coordination à travers de nombreuses équipes, fournisseurs, et cycles de financement. Enveloppez les équipes adaptatives dans une coquille de gouvernance prédictive, alimentez le rythme de jalon avec des incréments démontrés et un registre de risque vivant au lieu d'assembler des rapports séparés, et maintenez une carte de dépendance inter-équipes pour que le chemin critique soit géré plutôt que découvert. Standardisez les estimations basées sur des plages et re-prévues empiriquement à travers le portefeuille pour que la direction compare les projets sur des projections honnêtes et rétrécissantes plutôt que des dates fixes optimistes.

**Gouvernement.** Les règles de marchés publics, les crédits pluriannuels, et la responsabilité publique façonnent chaque choix. Préférez des incréments modulaires et basés sur les résultats livrés adaptativement sous un cadre de gouvernance qui satisfait les crédits et la surveillance, plutôt qu'un seul contrat en cascade à prix fixe et portée fixe avec une mise en service distante. Un registre de risque vivant et des incréments transparents et démontrés donnent aux auditeurs et législateurs une vraie visibilité, et fléchir la portée vers un noyau précieux à l'intérieur d'un financement fixe vous permet de livrer une capacité utile tôt plutôt que de tout risquer sur une date.

## Exemples

**Jeune pousse.** Une jeune pousse de sept personnes courant pour livrer son premier produit payant gère le projet avec presque aucun cérémonial mais une vraie discipline. Elle décompose la publication en petites tranches ordonnées, s'engage à une date de lancement tout en laissant la portée fléchir vers un noyau précieux plutôt que de promettre chaque fonctionnalité, et cite aux fondateurs une plage au lieu d'une date unique, re-prévoyant hebdomadairement depuis combien de tranches l'équipe ferme réellement. Un registre de risque de dix lignes dans un document partagé nomme la seule dépendance qui pourrait couler la date, une intégration de paiement inachevée, avec un propriétaire et un plan de secours, pour que la plus grande menace soit surveillée au lieu d'être découverte à l'échéance.

**Grande entreprise.** Une banque remplaçant sa plateforme d'origination de prêt exécute un programme hybride : une coquille prédictive avec des jalons de financement trimestriels et des portes de conformité, enveloppant des équipes adaptatives qui livrent des incréments fonctionnels toutes les deux semaines. Une carte de dépendance inter-équipes expose qu'un service d'identité partagé est sur le chemin critique. Le programme le séquence donc en premier et le dérisque, évitant une cascade tardive. Les estimations sont exprimées comme des plages et re-prévues mensuellement depuis le débit réel, pour que la direction voie une projection honnête et rétrécissante plutôt qu'une date fixe qui glisse silencieusement.

**Gouvernement.** Une agence abandonne un seul contrat en cascade à prix fixe et portée fixe (le motif derrière plusieurs échecs publics) pour des marchés publics modulaires : des incréments plus petits et basés sur les résultats livrés adaptativement sous un cadre de gouvernance qui satisfait les crédits et la surveillance. Un registre de risque vivant et des incréments transparents et démontrés donnent aux auditeurs et législateurs une vraie visibilité. Parce que la portée fléchit vers un noyau précieux à l'intérieur d'un financement fixe, le programme peut livrer une capacité utile tôt plutôt que de tout risquer sur une mise en service distante unique (chapitres 10.1, 10.3).

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur une bonne gestion de projet est dominé par **l'échec évité**. Les grands projets logiciels sont bien plus susceptibles d'être en retard, au-dessus du budget, ou annulés que d'atteindre un plan fixe original, et les pertes sont énormes : coût irrécupérable, plus valeur renoncée, plus, dans le gouvernement, dommage public et politique. Les disciplines ici (estimation honnête, gestion de dépendance, travail de risque précoce, parties prenantes engagées, et portée adaptative) sont exactement celles qui déplacent un projet hors de la courbe d'échec. Même une réduction modeste de la probabilité d'un dépassement majeur ou d'une annulation éclipse le coût de bien gérer le projet.

Sur le **coût total de possession**, la gestion légère et adaptative abaisse le coût à travers la vie du travail. La rétroaction rapide attrape les erreurs coûteuses tôt. La livraison incrémentale commence à retourner de la valeur plus tôt, ce qui améliore le calendrier du ROI. Le flux transparent réduit la surcharge de rapport que la gouvernance lourde impose. À la fois la *sous*-gestion (chaos, retravail, dépendances manquées) et la *sur*-gestion (cérémonial qui ralentit la livraison) portent un vrai coût. Le but est le processus le plus léger qui respecte vos véritables obligations. Faites valoir le dossier auprès de la direction en contrastant le coût pleinement chargé d'un projet troublé récent avec le coût quasi nul d'un registre de risque, une carte de dépendance, et des prévisions honnêtes basées sur des plages.

## Anti-patterns et pièges

- **Les plans tout-fixé :** portée, calendrier, et coût tous verrouillés, avec la qualité comme soupape de décharge silencieuse.
- **Les estimations comme promesses :** des dates à chiffre unique traitées comme des engagements, puis défendues au-delà des preuves.
- **Ignorer les dépendances :** gérer la vélocité de chaque équipe tandis que le chemin critique inter-équipes glisse.
- **Le théâtre de registre de risque :** un document créé une fois et jamais revisité.
- **Le statut pastèque :** vert dehors, rouge dedans ; l'optimisme récompensé plutôt que l'honnêteté.
- **Le client absent :** aucune partie prenante engagée, donc la mauvaise chose est construite avec confiance.
- **La livraison big bang :** tout intégré et publié à la fin, maximisant le risque (contraste chapitre 11.2).
- **Le processus pour lui-même :** cérémonial et rapports qui consomment de l'effort sans réduire le risque.

## Modèle de maturité

- **Niveau 1 (Initier) :** Les projets fonctionnent sur l'héroïsme et l'espoir ; la portée, le risque, et les dépendances sont gérés ad hoc si tant est qu'ils le soient ; les estimations sont des chiffres uniques défendus au-delà des preuves ; les surprises arrivent à l'échéance.
- **Niveau 2 (Développer) :** Une planification de base, un rapport de statut, et une liste de risque existent sur certains projets mais pas d'autres ; la méthode de livraison est choisie par habitude plutôt que par ajustement ; l'estimation et le suivi de dépendance varient équipe par équipe, donc la pratique est incohérente à travers l'organisation.
- **Niveau 3 (Standardiser) :** Une approche documentée est appliquée à l'échelle de l'organisation : la méthode de livraison est choisie pour s'ajuster au travail, la portée est gérée contre la triple contrainte, un registre de risque vivant et une carte de dépendance sont attendus sur chaque projet, et les estimations sont basées sur des plages et re-prévues avec des parties prenantes engagées.
- **Niveau 4 (Gérer) :** La livraison est mesurée et contrôlée contre des référentiels. Le débit, le temps de cycle, la précision de prévision, les taux de fermeture de dépendance et de risque, et la variance de calendrier et de coût sont suivis par projet et remontés à travers le portefeuille ; les projections sont empiriques et rétrécissantes ; les glissements font surface tôt et déclenchent une redéfinition de portée ou un rebasage sur des preuves plutôt que l'optimisme.
- **Niveau 5 (Orchestrer) :** La gestion de projet est intégrée avec la planification de portefeuille, de financement, et de risque et continuellement améliorée. La gouvernance hybride satisfait la surveillance sans ralentir la livraison, les dépendances inter-équipes et inter-fournisseurs sont gérées proactivement, les rétrospectives réinjectent le changement mesuré dans la pratique, et l'organisation adapte ses méthodes et rééquilibre le travail à mesure que les contraintes et priorités changent.

## Pistes de réflexion

1. Quelle méthode de livraison (prédictive, adaptative, hybride) chacune de vos initiatives actuelles a-t-elle réellement besoin, et correspond-elle à ce que vous utilisez ?
2. Quand vous vous êtes engagé pour la dernière fois à une date, était-ce une plage ou un chiffre unique, et comment cela a-t-il façonné les attentes ?
3. Quelle est la dépendance de chemin critique à travers vos équipes en ce moment, et qui possède son dérisquage ?
4. Votre registre de risque est-il une habitude vivante ou un document ponctuel ?
5. Où la qualité absorbe-t-elle silencieusement la pression quand la portée, le calendrier, et le coût sont tous fixés ?
6. Comment vos prévisions changeraient-elles si vous remplaciez l'estimation par le débit mesuré ?

## Points clés à retenir

- La gestion de projet transforme l'intention en résultats livrés sous la contrainte portée-calendrier-coût-qualité.
- **Assortissez la méthode au travail :** prédictive, adaptative, ou hybride, et préférez la gouvernance hybride en entreprise/gouvernement.
- Traitez les **estimations comme des plages**, re-prévoyez depuis des **métriques de flux empiriques**, et ne laissez pas les dates à chiffre unique devenir des mensonges.
- Les **dépendances et le risque** sont les modes d'échec dominants à l'échelle : cartographiez et gérez les deux continuellement.
- Gardez les **parties prenantes engagées** et le statut **transparent** ; faites voyager rapidement les mauvaises nouvelles.
- Le ROI est l'échec évité ; le processus le plus léger qui respecte vos obligations gagne. Voir chapitres 10.7 (Agile), 10.1 (gestion de portefeuille et de programme), 11.2 (livraison), et 11.3 (théorie des files d'attente).

## Références et lectures complémentaires

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (pourquoi ajouter des gens à un projet en retard le retarde davantage).
- Tom DeMarco et Timothy Lister, *Peopleware* et *Waltzing with Bears* (gestion de risque).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (prévision empirique).
- Standish Group, *CHAOS Report* (résultats de projet logiciel, à lire de façon critique).
- U.S. Digital Service, *Digital Services Playbook* ; UK Government, *Government Service Standard* (livraison moderne du secteur public).
- Bent Flyvbjerg et Dan Gardner, *How Big Things Get Done* (livraison de mégaprojet).
