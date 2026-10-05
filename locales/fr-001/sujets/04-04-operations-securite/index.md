# 4.4 Opérations de sécurité

## Vue d'ensemble et motivation

La prévention est nécessaire, mais elle n'est jamais suffisante. Des adversaires déterminés, des vulnérabilités nouvelles, et de simples erreurs humaines signifient que certaines menaces glisseront à travers vos défenses. Les opérations de sécurité sont la discipline de les trouver rapidement, de bien y répondre, et d'alimenter en retour ce que vous apprenez dans des défenses plus fortes. C'est la différence entre un incident contenu en minutes et un qui s'envenime pendant des mois avant que quiconque ne le remarque.

Dans une grande organisation, les opérations de sécurité doivent fonctionner à l'échelle et à la vitesse. Des milliers de services génèrent des océans de journaux. Des centaines de nouvelles vulnérabilités sont divulguées chaque semaine. Le déploiement ne s'arrête jamais. Des opérations manuelles et artisanales ne peuvent simplement pas suivre le rythme. La réponse est d'intégrer la sécurité dans le pipeline de livraison ([DevSecOps](https://fr.wikipedia.org/wiki/DevSecOps)), d'automatiser la détection et la réponse, et de construire le muscle pour gérer les incidents calmement quand ils frappent. Pour l'administration publique, les opérations de sécurité portent aussi des obligations légales : des délais de rapport d'incident mandatés, une divulgation de vulnérabilité coordonnée, et une rigueur criminalistique qui peut résister à l'examen légal.

Ce chapitre couvre l'intégration de la sécurité dans le pipeline, la gestion des vulnérabilités et des correctifs, la réponse aux incidents et la conduite de la criminalistique, l'exécution de la détection à travers [SIEM](https://fr.wikipedia.org/wiki/Gestion_des_informations_et_des_%C3%A9v%C3%A9nements_de_s%C3%A9curit%C3%A9) et SOAR, et la validation des défenses à travers l'équipe rouge et violette et le [test d'intrusion](https://fr.wikipedia.org/wiki/Test_d%27intrusion).

## Principes clés

- **Automatisez la routine.** Les machines gèrent le scan, la corrélation, et la réponse répétitive pour que les humains se concentrent sur le jugement.
- **Décalez la sécurité dans le pipeline.** Les tests et les portes vivent dans [CI/CD](https://fr.wikipedia.org/wiki/CI/CD) (intégration continue et livraison continue), donnant un retour rapide là où les ingénieurs travaillent déjà.
- **Supposez la violation et préparez-vous.** Répétez la réponse aux incidents avant d'en avoir besoin ; l'incident n'est pas le moment d'improviser.
- **Mesurez et réduisez le temps.** Le temps moyen de détecter et le temps moyen de répondre sont les métriques qui comptent le plus.
- **Apprentissage sans blâme.** Chaque incident et quasi-accident devient une leçon qui durcit le système, pas une recherche de quelqu'un à punir.
- **Validez les défenses de façon adversariale.** Testez votre sécurité comme le feraient de vrais attaquants, puis corrigez ce qu'ils trouvent.
- **L'ingénierie de détection est un produit.** Traitez les détections comme du code : versionnées, testées, et continuellement améliorées.

## Recommandations

### Construire DevSecOps dans le pipeline

Intégrez le test de sécurité automatisé directement dans l'intégration et la livraison continues pour que le retour atteigne les ingénieurs en quelques minutes :

- **[SAST](https://fr.wikipedia.org/wiki/Test_de_s%C3%A9curit%C3%A9_des_applications_statique)** (Static Application Security Testing) analyse le code source pour des motifs vulnérables au moment du commit.
- **[DAST](https://fr.wikipedia.org/wiki/Test_de_s%C3%A9curit%C3%A9_des_applications_dynamique)** (Dynamic Application Security Testing) sonde l'application en fonctionnement pour des défauts exploitables.
- **SCA** (Software Composition Analysis) signale les dépendances connues comme vulnérables.
- **Le scan d'IaC** vérifie l'infrastructure-en-tant-que-code pour des configurations non sûres avant le déploiement.
- **Le scan de secrets** bloque les identifiants d'entrer dans le dépôt.

Réglez ces outils sans pitié pour contrôler les faux positifs. Un scanner qui crie au loup est ignoré. Fixez des portes fondées sur le risque : bloquez sur les constatations à haute sévérité et haute confiance, et suivez le reste sans arrêter la livraison. Vous voulez un signal rapide et de confiance, pas un mur de bruit.

### Gérer les vulnérabilités et corriger systématiquement

Un flux constant de vulnérabilités appelle un processus systématique et priorisé, pas une nouvelle panique à chaque une.

- Maintenez un inventaire d'actifs précis pour savoir ce qui pourrait être affecté par toute vulnérabilité donnée.
- Priorisez la remédiation par vrai risque : combinez sévérité, exploitabilité (est-elle exploitée dans la nature ?), exposition, et criticité d'actif plutôt que de corriger par simple score brut.
- Définissez et imposez des **SLA de remédiation** (accords de niveau de service) par palier de sévérité, et mesurez l'adhésion.
- Automatisez les correctifs là où vous pouvez le faire en sécurité, spécialement pour l'infrastructure et les dépendances.
- Exécutez un programme de **divulgation de vulnérabilité coordonnée** avec un canal d'admission clair et, là où approprié, une [prime de bug](https://fr.wikipedia.org/wiki/Programme_de_prime_aux_bogues), pour que les chercheurs externes puissent rapporter des défauts de façon responsable au lieu de les déverser publiquement.

### Se préparer et exécuter la réponse aux incidents

Quand un incident frappe, un processus répété vaut plus que tout outil.

- Maintenez un **plan de réponse aux incidents** avec des rôles définis (commandant d'incident, responsable communication, enquêteurs), des classifications de sévérité, et des chemins d'escalade.
- Établissez des phases claires : **préparation, détection et analyse, confinement, éradication, récupération, et revue post-incident.**
- Préservez la preuve correctement pour la **[criminalistique](https://fr.wikipedia.org/wiki/Investigation_num%C3%A9rique)** : capturez les journaux, la mémoire, et les images disque avec une chaîne de possession documentée pour que les constatations tiennent légalement et que l'analyse soit solide.
- Planifiez les **communications de violation** à l'avance : qui notifie les clients, régulateurs, et le public, selon quel calendrier, avec l'implication légale et RP. Les horloges réglementaires (souvent 72 heures ou moins) commencent à courir à la découverte.
- Exécutez des **exercices de simulation sur table** régulièrement pour que l'équipe connaisse le plan avant une vraie crise, et menez des revues post-incident sans blâme qui produisent des améliorations concrètes.

### Exploiter la détection avec SIEM et SOAR, et concevoir des détections

Rassemblez vos signaux de sécurité et agissez sur eux à l'échelle.

- Utilisez un **SIEM** (Security Information and Event Management) pour agréger et corréler les journaux et événements à travers le parc, faisant surgir des motifs suspects.
- Utilisez **SOAR** (Security Orchestration, Automation, and Response) pour automatiser les livres de jeu de triage et de réponse : enrichissant les alertes, isolant les hôtes, désactivant les identifiants, et ouvrant des dossiers sans attendre un humain pour les étapes routinières.
- Pratiquez l'**ingénierie de détection** : traitez les règles de détection comme du code versionné et testé aligné sur un cadre comme [MITRE ATT&CK](https://fr.wikipedia.org/wiki/MITRE_ATT%26CK), mesurez leurs taux de vrais et faux positifs, et améliorez continuellement la couverture des vraies techniques adverses.
- Assurez une journalisation complète et résistante à la falsification à travers les applications et l'infrastructure ; vous ne pouvez pas détecter ce que vous ne journalisez pas.

### Valider les défenses avec l'équipe rouge et violette et le test d'intrusion

Tester vos défenses comme le ferait un attaquant est le seul moyen de savoir qu'elles fonctionnent réellement.

- Le **test d'intrusion** fournit une évaluation ciblée et ponctuelle de systèmes spécifiques, souvent pour la conformité.
- L'**[équipe rouge](https://fr.wikipedia.org/wiki/%C3%89quipe_rouge)** simule un adversaire réaliste poursuivant des objectifs à travers votre environnement, testant la détection et la réponse autant que la prévention.
- L'**équipe violette** rassemble les attaquants (rouge) et les défenseurs (bleu) de façon collaborative pour que chaque attaque simulée améliore immédiatement les détections et contrôles, transformant un exercice en capacité durable.
- Réinjectez toutes les constatations dans l'ingénierie de détection, la remédiation, et la formation.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| Portes de pipeline bloquantes | Arrête les problèmes connus d'être livrés | Friction, les faux positifs frustrent les équipes |
| Scan non bloquant | Faible friction, livraison rapide | Les problèmes peuvent être livrés ; exige de la discipline pour corriger |
| SOC interne | Contexte profond, contrôle complet | Coûteux, difficile à doter en personnel 24/7 |
| Détection/réponse gérée | Couverture 24/7, expertise à la demande | Moins de contexte, dépendance fournisseur |
| Correction automatisée | Rapide, ferme les fenêtres rapidement | Risque de changements cassants |
| Équipe rouge fréquente | Validation réaliste, trouve de vraies lacunes | Coûteux, intensif en ressources |
| Programme de prime de bug | Découverte en foule, bonne couverture | Fardeau de triage, coûts de paiement, bruit |

La tension centrale est la vitesse contre l'assurance, et la couverture contre le coût. Les portes bloquantes et la correction automatisée maximisent l'assurance mais ajoutent de la friction et du risque. Les approches non bloquantes bougent plus vite mais dépendent du suivi. La détection continue est essentielle à l'échelle mais coûteuse à construire en interne, ce qui pousse de nombreuses organisations vers des modèles hybrides. Le chemin durable automatise la routine à haute confiance, sauve l'attention humaine pour le vrai jugement, et continue de régler l'équilibre en utilisant des résultats mesurés plutôt que la peur.

## Questions à discuter avec votre équipe

1. **Quels sont vos SLA de remédiation par sévérité, et qu'est-ce qui les impose réellement ?** Un flux constant de vulnérabilités a besoin d'un processus systématique et priorisé, pas une nouvelle panique à chaque une, et les SLA par palier de sévérité sont comment vous gardez le rythme. Décidez vos horloges (par exemple, critique en jours, élevé en semaines) et, tout aussi important, comment vous mesurez l'adhésion et qui est responsable quand une échéance glisse. Priorisez par vrai risque, combinant sévérité avec exploitabilité dans la nature, exposition, et criticité d'actif, plutôt que de corriger par simple score CVSS brut. Apportez votre arriéré actuel de constatations ouvertes triées par âge et sévérité, parce que les critiques non corrigées dépassant leur fenêtre sont la preuve qui compte. Si le SLA n'a aucune imposition et aucun propriétaire, c'est un souhait, et scanner sans remédier construit juste une dette d'audit et un faux sentiment de sécurité.

2. **Quand un incident frappe à 2 heures du matin, qui est le commandant d'incident et à quelle vitesse l'horloge réglementaire commence-t-elle ?** Un processus répété vaut plus que tout outil, donc vous avez besoin de rôles nommés (commandant d'incident, responsable communication, enquêteurs), de niveaux de sévérité définis, et de chemins d'escalade consignés avant la crise. Les horloges réglementaires courent souvent 72 heures ou moins et commencent à la découverte, donc décidez à l'avance qui notifie les clients, régulateurs, et le public, et confirmez que le légal et les RP sont dans la boucle. Préserver la preuve criminalistique avec une chaîne de possession documentée doit se produire avant que quiconque ne reconstruise un hôte compromis, ou vous perdez la capacité de comprendre ou prouver ce qui s'est passé. Apportez la date de votre dernier exercice de simulation sur table, parce que s'il était il y a longtemps ou jamais, votre plan est non testé. Pour les équipes gouvernementales, les échéances de rapport légales rendent cela non optionnel, donc répétez le chemin de notification, pas seulement la réponse technique.

3. **Quelles actions de réponse routinières laisserez-vous SOAR prendre sans humain dans la boucle ?** L'automatisation est une multiplication de force qui permet à une équipe légère de couvrir un grand parc, et la métrique qui compte est le temps moyen de répondre, que les livres de jeu automatisés peuvent réduire d'heures à minutes. Décidez quelles actions à haute confiance (isoler un hôte, révoquer un identifiant, ouvrir un dossier) vous faites confiance pour fonctionner automatiquement, et lesquelles ont besoin d'un jugement humain d'abord. Le risque est qu'un faux positif déclenche une action perturbatrice, donc liez l'automatisation à la qualité de détection et réglez sans pitié, parce qu'un système qui crie au loup est éteint. Apportez votre volume d'alerte actuel et votre taux de faux positif, parce que ces chiffres vous disent quels livres de jeu sont sûrs à automatiser aujourd'hui. Si chaque étape de réponse attend un humain, vous ne suivrez pas à l'échelle, et le temps de résidence, qui pilote le coût de violation, restera élevé.

4. **Quelles constatations de pipeline bloquent une livraison, lesquelles sont seulement suivies, et qui garde le taux de faux positif assez bas pour que les ingénieurs fassent encore confiance à la porte ?** Un scanner qui crie au loup est ignoré, et une fois que les ingénieurs perdent foi en une porte, ils font pression pour la retirer, donc la valeur de DevSecOps repose sur la qualité du signal plutôt que la couverture brute. La tension est réelle : bloquer sur trop peu et du code vulnérable est livré ; bloquer sur trop et vous ajoutez de la friction, ralentissez la livraison, et brûlez la bonne volonté. Apportez les taux de vrais et faux positifs pour chaque scanner (SAST, DAST, SCA, IaC, et scan de secrets), à quelle fréquence les équipes outrepassent ou suppriment une porte, et l'âge des constatations que vous suivez seulement sans corriger. Pour une entreprise ou un organisme gouvernemental exploitant des centaines de pipelines, fixez la politique bloquer-contre-suivre centralement et réglez-la avec des données, parce que des portes qui diffèrent arbitrairement d'équipe à équipe créent à la fois des lacunes d'audit et le sentiment que la sécurité est capricieuse.

5. **Quelle confiance avez-vous que vos détections couvrent encore les techniques qu'un vrai attaquant utiliserait, et qui les possède comme code testé et versionné ?** Les détections se dégradent discrètement à mesure que votre environnement et vos adversaires évoluent, donc un ensemble de règles qui semblait complet l'année dernière peut perdre de la couverture bien avant qu'un incident ne révèle finalement la lacune. Traiter les détections comme du code, versionné, testé, et mappé à un cadre tel que MITRE ATT&CK, est ce qui sépare une pratique d'ingénierie d'un tas d'alertes obsolètes, pourtant cela entre en compétition pour le même temps d'analyste rare que le triage en direct. Apportez votre carte de couverture ATT&CK actuelle, le taux mesuré de vrais et faux positifs de vos meilleures détections, et les résultats de votre dernier exercice d'équipe violette, puisque le test collaboratif rouge-et-bleu est le moyen le plus rapide de prouver quelles détections se déclenchent réellement. Dans les contextes d'entreprise et gouvernementaux où un cadre peut être mandaté, liez chaque détection à un propriétaire nommé et une cadence de révision, parce qu'une couverture que personne ne maintient est une couverture que vous découvrez avoir perdue seulement après la violation.

6. **Construisez-vous la détection et la réponse en interne, achetez-vous la détection et réponse gérée, ou mélangez-vous les deux, et avez-vous chiffré ce que coûte une vraie couverture 24/7 ?** Le temps de résidence pilote le coût de violation, donc les heures non couvertes (nuits, week-ends, jours fériés) sont exactement quand un intrus non détecté fait le plus de dommage, et pourtant doter en personnel un centre d'opérations de sécurité 24/7 en interne est coûteux et difficile à soutenir. Le compromis est le contexte et le contrôle contre le coût et la vitesse vers la couverture : une équipe interne connaît profondément votre parc mais est lente et coûteuse à construire, tandis qu'un fournisseur géré donne une expertise instantanée autour de l'horloge au prix d'un contexte plus mince et d'une dépendance fournisseur. Apportez vos heures de couverture actuelles, votre temps moyen de détecter et répondre pendant les heures creuses, votre volume d'alerte, et une lecture honnête de si vous pouvez recruter et retenir les analystes qu'un centre auto-exploité exige. Pour les entreprises gouvernementales et régulées, pesez la résidence des données, l'habilitation du personnel, et les obligations de rapport légal que le fournisseur doit pouvoir satisfaire, et confirmez que le contrat préserve la rigueur criminalistique et la chaîne de possession que les procédures légales exigent.

## Regard sectoriel

**Jeune pousse.** La vitesse et la survie viennent en premier, donc achetez la sécurité comme sous-produit d'outils que vous exploitez déjà plutôt que de doter des opérations en personnel. Câblez des scanners gratuits dans CI pour bloquer les fuites de secret et les dépendances connues comme vulnérables au moment du commit, transférez les journaux vers un service géré à bas coût avec une poignée d'alertes à haute valeur, et écrivez un plan d'incident d'une page (qui appeler, comment faire pivoter les identifiants, instantané avant de reconstruire) avant d'en avoir jamais besoin. Votre ressource la plus rare est l'attention d'ingénierie, donc automatisez la routine et résistez à monter un centre d'opérations de sécurité que vous ne pouvez pas garder en fonctionnement.

**Petite entreprise.** Sans spécialiste de sécurité dédié et avec un budget serré, appuyez-vous sur la détection et réponse gérée et sur les fonctionnalités de sécurité déjà intégrées dans vos plateformes. Traitez la correction et l'inventaire d'actifs comme les habitudes au plus grand levier : sachez ce que vous exploitez, gardez-le à jour, et imposez une échéance de remédiation simple par sévérité. Préférez les fournisseurs qui gèrent la surveillance autour de l'horloge, l'admission de divulgation coordonnée, et la capture criminalistique pour vous, et répétez la seule chose que vous ne pouvez pas sous-traiter, qui est de décider qui déclare un incident et qui parle aux clients.

**Grande entreprise.** Le défi est la cohérence à travers de nombreuses équipes et des centaines de pipelines : une politique de porte bloquer-contre-suivre partagée, des SLA de remédiation imposés à l'échelle de l'organisation, une plateforme SIEM et SOAR avec des détections mesurées, et une équipe violette qui transforme chaque exercice en nouvelle couverture. Gérez les opérations de sécurité comme un portefeuille avec des tableaux de bord pour le temps moyen de détecter et répondre, l'adhésion aux SLA, et la précision de détection, et décidez délibérément où la profondeur interne bat l'échelle gérée. Budgétez explicitement le coût de supervision humaine du triage et du réglage, parce que l'automatisation déplace l'effort plutôt que de le retirer.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la redevabilité publique façonnent chaque choix. Les échéances légales de rapport d'incident et la divulgation de vulnérabilité coordonnée sont des obligations plutôt que des options, donc répétez le chemin de notification vers l'autorité nationale aussi soigneusement que la réponse technique, et préservez la preuve criminalistique sous une chaîne de possession qui résiste à l'examen légal. Favorisez les contrats qui gardent la logique de détection et les données portables, exigez que tout fournisseur géré satisfasse les exigences de résidence et d'habilitation, et attendez-vous à ce que les évaluations d'équipe rouge et le scan continu alimentent un processus d'autorisation auquel le public peut faire confiance.

## Exemples

**Jeune pousse.** Une start-up sans centre d'opérations de sécurité câble des scanners gratuits dans son pipeline CI pour que les fuites de secret et les dépendances connues comme vulnérables soient attrapées au moment du commit, bloquant seulement sur les constatations à haute confiance pour que les deux ingénieurs ne soient pas noyés dans le bruit. Elle écrit un plan d'incident d'une page avant d'en avoir besoin : qui appeler, comment faire pivoter les identifiants, et prendre un instantané d'un hôte compromis avant de le reconstruire pour pouvoir apprendre ce qui s'est passé. Elle transfère les journaux vers un service géré à bas coût et fixe quelques alertes sur les événements qui signaleraient réellement une violation, pour qu'un problème apparaisse en heures plutôt que les mois qu'il faut pour le remarquer par accident.

**Grande entreprise.** Une entreprise de logiciel en tant que service exécute SAST, SCA, IaC, et le scan de secrets dans chaque pipeline, bloquant seulement sur les constatations à haute sévérité et haute confiance et suivant le reste sur un tableau de bord avec des SLA de remédiation. Un SIEM alimente une plateforme SOAR qui isole automatiquement les hôtes et révoque les identifiants sur les alertes à haute confiance, réduisant le temps moyen de répondre d'heures à minutes. Des exercices trimestriels d'équipe violette contre les techniques MITRE ATT&CK génèrent directement de nouvelles règles de détection, fermant régulièrement les lacunes de couverture.

**Gouvernement.** Une agence fédérale exploite un centre d'opérations de sécurité (SOC) avec un rapport d'incident mandaté à une autorité cyber nationale dans des délais légaux. Elle exécute un programme de divulgation de vulnérabilité coordonnée avec un canal d'admission public comme exigé par politique, et préserve la preuve criminalistique sous des procédures strictes de chaîne de possession adaptées aux procédures légales. Les évaluations annuelles d'équipe rouge et le scan continu de vulnérabilité alimentent l'autorisation continue de l'agence et ses SLA de remédiation fondés sur le risque.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Presque tout dans l'argumentaire pour les opérations de sécurité se résume au temps de résidence : plus longtemps un attaquant reste non détecté, plus la violation coûte. Les études montrent systématiquement que les incidents contenus rapidement coûtent dramatiquement moins que ceux qui traînent pendant des mois. Le coût total de possession inclut l'outillage (SIEM, SOAR, scanners), la dotation en personnel ou les services gérés pour la détection et la réponse, et le temps pour construire et répéter les processus d'incident. Contre cela se trouve le coût de ne pas investir : une violation découverte tard, se propageant à travers les systèmes, attirant des amendes réglementaires, des notifications obligatoires, des litiges, et un dommage réputationnel, tout aggravé par le chaos d'une réponse non répétée.

Le ROI vient d'une détection et réponse plus rapides, de l'automatisation qui permet à une équipe légère de couvrir un grand parc, et des améliorations de prévention réinjectées depuis chaque incident et exercice. DevSecOps en particulier rapporte en attrapant les problèmes dans le pipeline où ils sont bon marché, plutôt qu'en production où ils sont coûteux et publics. Quand vous faites valoir cela auprès de la direction, mettez des chiffres sur votre temps moyen actuel de détecter et répondre, montrez comment ces chiffres se lient au temps de résidence et au coût, et cadrez l'automatisation comme une multiplication de force qui évite de faire croître l'effectif au rythme du parc. Pour l'administration publique, insistez sur le fait que les obligations légales de rapport et de divulgation rendent les opérations matures non optionnelles.

## Anti-patterns et pièges

- **Fatigue d'alerte.** Tant d'alertes que les analystes se déconnectent et manquent la vraie.
- **Scanner sans remédier.** Générer des constatations que personne ne corrige, créant un faux sentiment de sécurité et une dette d'audit.
- **Aucun plan d'incident.** Improviser pendant une crise, gaspillant des minutes critiques et mal gérant la preuve.
- **Détruire la preuve.** Reconstruire un hôte compromis avant de capturer la criminalistique, perdant la capacité de comprendre ou prouver ce qui s'est passé.
- **Culture du blâme dans les revues.** Punir les répondants pour que le prochain incident soit caché ou géré défensivement.
- **Test d'intrusion de conformité seulement.** Un seul test annuel pour satisfaire un auditeur, avec des constatations ignorées jusqu'à l'année prochaine.
- **Portes bloquantes avec des faux positifs élevés.** Érodant la confiance jusqu'à ce que les ingénieurs exigent que les portes soient entièrement retirées.
- **Détections fixées et oubliées.** Des règles qui se dégradent à mesure que l'environnement et les adversaires évoluent, perdant silencieusement de la couverture.

## Modèle de maturité

**Niveau 1 : Initier.** Les opérations de sécurité sont ad hoc et réactives. Le test de sécurité est manuel et rare, et il n'y a pas de journalisation centrale ou de SIEM. Aucun plan d'incident n'existe, donc la réponse est improvisée sur le moment. La correction n'a lieu que quand un titre force la question, et les défenses ne sont jamais testées de façon adversariale.

**Niveau 2 : Développer.** Des pratiques de base apparaissent mais sont incohérentes à travers les équipes. Certains pipelines exécutent des scanners pendant que d'autres n'en exécutent aucun, et la journalisation centrale existe par pièces. Un plan d'incident de base est documenté mais rarement répété, la correction suit des calendriers lâches, et un test d'intrusion annuel satisfait la conformité sans changer grand-chose. La couverture et la rigueur dépendent de quelle équipe vous demandez.

**Niveau 3 : Standardiser.** Les pratiques sont documentées et imposées à l'échelle de l'organisation. Le scan DevSecOps complet avec des portes fondées sur le risque est appliqué de façon cohérente, un SIEM corrèle les événements, et les premiers livres de jeu SOAR fonctionnent. La réponse aux incidents est répétée avec des simulations sur table et des revues sans blâme, les SLA de remédiation par sévérité sont imposés avec des propriétaires nommés, et la divulgation de vulnérabilité coordonnée et l'équipe rouge régulière sont la norme plutôt que l'exception.

**Niveau 4 : Gérer.** Les opérations sont mesurées et contrôlées par rapport à des références. Le temps moyen de détecter et répondre, l'adhésion aux SLA par palier de sévérité, la couverture de scan, les taux de vrais et faux positifs de détection, et le temps de résidence sont suivis sur des tableaux de bord et révisés selon une cadence. Les détections portent une précision et un rappel mesurés mappés sur MITRE ATT&CK, les décisions d'automatisation sont conditionnées sur des données de faux positif plutôt que l'espoir, et une métrique qui dérive au-delà de sa référence déclenche une réponse définie au lieu de passer inaperçue.

**Niveau 5 : Orchestrer.** Les opérations de sécurité sont continuellement améliorées, intégrées à travers l'organisation, et adaptatives. L'ingénierie de détection, l'équipe violette, la remédiation, et la revue d'incident alimentent une boucle qui s'adapte aux nouvelles techniques adverses à mesure qu'elles émergent. Les livres de jeu automatisés gèrent la routine à travers tout le parc pour que les humains se concentrent sur le jugement, la sécurité est planifiée aux côtés de la livraison et du risque, et chaque incident et exercice durcit mesurablement le système tandis que les métriques centrales continuent de baisser.

## Pistes de réflexion

1. Quelles constatations de pipeline devraient bloquer une livraison, et lesquelles devraient seulement être suivies ?
2. Construire un SOC interne, utiliser la détection et réponse gérée, ou mélanger les deux, et pourquoi ?
3. Comment empêchez-vous les règles de détection de se dégrader à mesure que votre environnement évolue ?
4. À quel point la correction devrait-elle être agressivement automatisée étant donné le risque de changements cassants ?
5. À quoi ressemble une revue post-incident vraiment sans blâme dans votre culture ?
6. Comment mesurez-vous si l'équipe rouge et violette améliore réellement vos défenses ?

## Points clés à retenir

- La prévention échoue éventuellement ; les opérations existent pour détecter et répondre rapidement.
- Intégrez SAST, DAST, SCA, IaC, et le scan de secrets dans le pipeline avec des portes fondées sur le risque.
- Priorisez la correction par vraie exploitabilité et criticité d'actif, sous des SLA imposés.
- Répétez la réponse aux incidents, préservez la preuve criminalistique, et planifiez les communications de violation à l'avance.
- Utilisez SIEM et SOAR pour corréler et automatiser ; traitez les détections comme du code conçu et testé.
- Validez les défenses avec le test d'intrusion, l'équipe rouge, et l'équipe violette collaborative.
- Le temps de résidence pilote le coût de violation, donc le temps moyen de détecter et répondre sont les métriques qui comptent.

## Références et lectures complémentaires

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin et autres, *Logging and Log Management* / littérature SIEM
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, guidance *Coordinated Vulnerability Disclosure* et spécification *CVSS*
