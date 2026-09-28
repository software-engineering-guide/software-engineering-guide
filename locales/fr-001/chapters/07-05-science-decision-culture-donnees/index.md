# 7.5 Science de décision et culture informée par les données

## Vue d'ensemble et motivation

La science de décision est la pratique de connecter les données à de vraies décisions, puisant dans les statistiques, la science comportementale, et le jugement pour aider les gens à bien choisir sous incertitude. Une culture informée par les données est la condition organisationnelle dans laquelle cela se produit par défaut : les gens recourent à la preuve, raisonnent soigneusement sur la cause et l'effet, communiquent l'incertitude honnêtement, et mettent à jour leurs croyances quand les données le justifient. Ce chapitre est délibérément la pierre angulaire de la séquence de données, parce que toute la stratégie, l'ingénierie, l'analytique, et l'expérimentation qui la précèdent sont sans valeur si elles ne changent pas les décisions pour le mieux.

Pour les grandes équipes c'est là où les investissements de données échouent le plus souvent, pas dans les pipelines mais dans le dernier kilomètre de la perspicacité à l'action. Les entreprises dépensent fortement dans des plateformes et tableaux de bord et prennent quand même des décisions majeures par hiérarchie, habitude, ou le présentateur le plus confiant. Un mode d'échec courant est le théâtre de données : des tableaux de bord et analyses élaborés produits pour paraître rigoureux pendant que la vraie décision a été prise à l'avance et les données triées sur le volet pour la justifier. L'administration publique ajoute des enjeux élevés et de l'examen. Les décisions de politique justifiées par des revendications causales faibles peuvent mal allouer de l'argent public et nuire aux citoyens, et la demande de responsabilité fait du raisonnement honnête sur la preuve une obligation civique, pas seulement une bonne pratique.

Les problèmes difficiles ici sont cognitifs et culturels, pas techniques. Les gens confondent [corrélation et causalité](https://fr.wikipedia.org/wiki/Corr%C3%A9lation_n%27implique_pas_causalit%C3%A9), ignorent les [facteurs de confusion](https://fr.wikipedia.org/wiki/Facteur_de_confusion) (variables cachées qui pilotent à la fois la cause supposée et l'effet), ancrent sur le premier nombre qu'ils voient, et lisent les estimations ponctuelles comme des certitudes. Et dans la poussée à devenir piloté par les données, les organisations peuvent dériver vers la surveillance : mesurer les individus si intrusivement qu'elles détruisent la confiance et provoquent la manipulation. Construire une véritable culture de mesure signifie bien faire le raisonnement, communiquer l'incertitude fidèlement, et mesurer les systèmes et résultats sans transformer les données en outil de contrôle sur les gens.

## Principes clés

- Le but des données est de meilleures décisions, pas la production de rapports.
- Décidez ce qui changerait votre avis avant de regarder les données.
- La corrélation n'est pas la causalité ; interrogez les facteurs de confusion avant d'agir.
- Communiquez l'incertitude honnêtement ; une estimation ponctuelle sans plage trompe.
- Soyez informé par les données, pas asservi aux données ; le jugement et le contexte comptent encore.
- Mesurez pour apprendre et améliorer les systèmes, pas pour surveiller et punir les individus.
- Mettez à jour les croyances quand la preuve le justifie ; changer d'avis est une force.
- La [sécurité psychologique](https://fr.wikipedia.org/wiki/S%C3%A9curit%C3%A9_psychologique) est un prérequis pour l'analyse honnête et la dissidence.

## Recommandations

### Connecter les données aux décisions et éviter le théâtre de données

Liez l'analyse à une décision spécifique dès le début : que ferons-nous différemment selon ce que nous trouvons ? Avant de rassembler des données, énoncez la décision, les options, et quelle preuve favoriserait chacune, idéalement quel résultat changerait votre avis. Cela garde contre le théâtre de données, où l'analyse ne fait que décorer une décision déjà prise. Si aucune découverte réaliste n'altérerait le choix, ne dépensez pas pour l'analyse. Faites l'appel de jugement honnêtement et dites-le. Insistez pour que les présentations mènent avec la décision et la recommandation, pas une visite de graphiques.

### Raisonner soigneusement sur la causalité

La plupart des questions d'affaires et de politique sont causales (cette action produira-t-elle ce résultat), mais la plupart des données disponibles sont observationnelles et pleines de facteurs de confusion. Enseignez aux équipes la différence entre corrélation et causalité, et les pièges : variables de confusion, [biais de sélection](https://fr.wikipedia.org/wiki/Biais_de_s%C3%A9lection), causalité inversée, et corrélation fallacieuse. Préférez les expériences randomisées pour les revendications causales où faisable. Où les expériences sont impossibles, utilisez des techniques d'[inférence causale](https://fr.wikipedia.org/wiki/Inf%C3%A9rence_causale) soigneuses et énoncez vos hypothèses explicitement plutôt que de glisser de « associé à » vers « cause ». Soyez spécialement sceptique d'une histoire convaincante construite sur une seule corrélation.

### Communiquer l'incertitude aux parties prenantes

Les nombres présentés comme des estimations ponctuelles précises invitent à une fausse confiance. Communiquez des plages, des intervalles de confiance ou crédibles, et les hypothèses clés derrière tout chiffre. Utilisez un langage clair et des visuels honnêtes (barres d'erreur, plages, bandes de scénario) pour que les décideurs saisissent ce qui est connu et inconnu. Distinguez ce que les données montrent, ce que vous inférez, et ce que vous supposez. Calibrez la confiance à la preuve : présentez une prévision issue de données minces exactement comme cela. L'incertitude communiquée honnêtement construit plus de confiance que la fausse précision, parce qu'elle survit au contact avec la réalité.

### Construire une culture de mesure sans surveillance

Créez un environnement où les équipes définissent routinièrement des métriques de succès, mesurent les résultats, et en apprennent, mais dirigez la mesure vers les systèmes, processus, et résultats plutôt que vers la surveillance des individus. Les métriques utilisées pour surveiller et classer les gens sont manipulées, engendrent la peur, et détruisent l'honnêteté que les bonnes décisions exigent (une dynamique capturée par la [loi de Goodhart](https://fr.wikipedia.org/wiki/Loi_de_Goodhart) : une mesure qui devient une cible cesse d'être une bonne mesure). Favorisez les métriques agrégées et orientées résultat. Impliquez les équipes dans le choix de leurs propres mesures, et séparez les métriques d'apprentissage de l'évaluation de performance. Protégez la sécurité psychologique pour que les gens fassent surface les mauvaises nouvelles et la dissidence tôt.

### Favoriser de bonnes habitudes de données et la littératie

Élevez la littératie de données largement pour que les gens puissent lire un graphique de façon critique, questionner la définition d'une métrique, et repérer une revendication trompeuse. Normalisez demander « comment le savons-nous ? » et « qu'est-ce qui changerait notre avis ? » Récompensez les gens pour mettre à jour leurs vues à la lumière de la preuve et pour exécuter des expériences qui échouent de façon informative. Rendez sûr de dire « les données ne nous disent pas » plutôt que de fabriquer de la certitude. Les leaders fixent le ton : quand ils changent des décisions basées sur la preuve et admettent l'incertitude, la culture suit.

### Se prémunir contre le biais et le mésusage

Surveillez les biais prévisibles : le [biais de confirmation](https://fr.wikipedia.org/wiki/Biais_de_confirmation) en sélectionnant des données de soutien, le [biais de survivant](https://fr.wikipedia.org/wiki/Biais_du_survivant) en ignorant ce qui manque, l'ancrage sur un nombre initial, et le biais rétrospectif dans les post-mortems. Intégrez la revue d'avocat du diable, le pré-enregistrement de ce que vous attendez de trouver, et des perspectives diverses sur les analyses importantes. Prenez l'éthique de données au sérieux (équité, transparence, et éviter le dommage), spécialement quand les décisions affectent les moyens de subsistance, prestations, ou droits des gens.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients | Meilleur ajustement |
|---|---|---|---|
| Piloté par les données (les données décident) | Réduit le biais, cohérent | Ignore le contexte, manipulé, cassant | Domaines bien compris |
| Informé par les données (données plus jugement) | Équilibre preuve et contexte | Plus lent, exige du jugement | Décisions complexes ou nouvelles |
| Expérience pour la causalité | Preuve causale forte | Coûteux, lent, pas toujours faisable | Choix réversibles à haut enjeu |
| Inférence observationnelle | Utilise les données disponibles | Risque de confusion, revendications plus faibles | Quand les expériences sont impossibles |
| Métriques de résultat/système | Pilote l'amélioration, peu de manipulation | Moins de responsabilité individuelle | Cultures d'apprentissage |
| Surveillance individuelle | Visibilité granulaire | Manipulation, peur, confiance érodée | Rarement justifiée |

La tension définissante est la rigueur contre la vitesse et faisabilité. Les expériences randomisées donnent la preuve causale la plus forte, mais elles coûtent du temps et sont souvent impossibles pour des choix stratégiques ou de politique ponctuels, où un jugement soigneux sur les facteurs de confusion et des hypothèses explicites doivent suffire. La deuxième tension est entre la mesure et la confiance : plus vous mesurez granulairement les individus, plus vous pouvez voir et moins de comportement honnête vous obtenez. Une culture mature penche vers le jugement informé par les données et la mesure agrégée orientée résultat. Elle accepte une précision apparente légèrement moindre en échange de décisions qui tiennent et d'une main-d'œuvre qui dit la vérité.

## Questions à discuter avec votre équipe

1. **Énoncez-vous ce qui changerait votre avis avant de regarder les données, et cette question est-elle écrite dans vos documents de décision ?** La garde la plus forte du chapitre contre le théâtre de données est de nommer la décision, les options, et la preuve qui favoriserait chacune, idéalement le résultat qui retournerait votre choix, avant de rassembler des données. Si aucune découverte réaliste n'altérerait la décision, le mouvement honnête est de sauter l'analyse et de faire l'appel de jugement ouvertement. Pour les entreprises et agences où un seul choix stratégique ou de politique peut gaspiller plus que tout un programme d'analytique ne coûte, cette discipline a un levier élevé. Apportez une décision récente et demandez si une découverte quelconque aurait pu la changer, ou si les graphiques ne faisaient que décorer une conclusion déjà atteinte. Si « qu'est-ce qui changerait notre avis ? » n'est pas une invite standard dans vos documents de décision, faites-en une, et insistez pour que les présentations mènent avec la recommandation, pas une visite de graphiques.

2. **Quand une corrélation convaincante apparaît, comment interrogez-vous les facteurs de confusion avant d'agir, et préférez-vous une expérience là où une est faisable ?** Le chapitre avertit que la plupart des questions d'affaires et de politique sont causales tandis que la plupart des données disponibles sont observationnelles et pleines de facteurs de confusion, biais de sélection, et causalité inversée. Ses propres exemples répètent un piège : les clients engagés s'auto-sélectionnent dans une fonctionnalité ou programme, donc la corrélation brute avec un désabonnement plus bas ou une recherche d'emploi plus haute disparaît sous une comparaison contrôlée. Agir sur cette corrélation signifie une campagne ou politique coûteuse et mal dirigée. Apportez une décision récente qui reposait sur une seule corrélation et demandez quelle variable cachée pourrait piloter les deux côtés. Où une expérience est faisable, préférez-la ; où elle ne l'est pas, utilisez des méthodes d'inférence causale soigneuses et énoncez vos hypothèses explicitement plutôt que de glisser de « associé à » vers « cause ».

3. **Vos métriques visent-elles à améliorer les systèmes et résultats, ou à surveiller les individus, et avez-vous séparé les métriques d'apprentissage de l'évaluation de performance ?** Le chapitre trace une ligne nette : la mesure pointée vers les gens est manipulée, engendre la peur, et détruit l'honnêteté que les bonnes décisions exigent, une dynamique que la loi de Goodhart prédit une fois qu'une mesure devient une cible. Il favorise les métriques agrégées et orientées résultat, impliquant les équipes dans le choix de leurs propres mesures, et protégeant la sécurité psychologique pour que les gens fassent surface les mauvaises nouvelles tôt. Pour les contextes gouvernementaux et d'entreprise, surveiller le personnel de première ligne érode la confiance qui rend possible des données précises en premier lieu. Apportez la question concrète : laquelle de vos métriques pourrait être utilisée pour classer ou punir des individus, et les gens les manipuleraient-ils sous pression ? Si les métriques d'apprentissage et l'évaluation de performance sont emmêlées ensemble, séparez-les, pour que la mesure pilote l'amélioration au lieu du comportement défensif.

4. **Quand un nombre atteint un décideur, arrive-t-il comme une plage avec ses hypothèses attachées, ou comme une estimation ponctuelle qui invite à une fausse confiance ?** Le chapitre argumente que l'incertitude communiquée honnêtement construit plus de confiance que la fausse précision, parce qu'elle survit au contact avec la réalité, pourtant l'attraction vers un seul chiffre confiant est forte quand un leader veut une réponse propre. Pour une grande équipe la pression concurrente est réelle : les plages et barres d'erreur peuvent se lire comme évasives pour des cadres qui récompensent la décisivité, donc les analystes apprennent à dépouiller les réserves pour être entendus. Apportez un rapport récent et vérifiez s'il distinguait ce que les données montrent, ce que vous avez inféré, et ce que vous avez supposé, et si une prévision construite sur des données minces était étiquetée exactement comme cela. Dans les contextes d'entreprise et gouvernementaux, où un chiffre peut finir dans une présentation de conseil, une soumission budgétaire, ou un témoignage public, une estimation ponctuelle présentée comme certitude est un passif, donc convenez d'une norme maison que les chiffres conséquents portent une plage, les hypothèses clés, et un énoncé simple de confiance.

5. **Est-il véritablement sûr ici de dire « les données ne nous disent pas », et qui est autorisé à contester comment une métrique est définie ?** Le chapitre traite la littératie de données et la sécurité psychologique comme des prérequis : les gens ont besoin de lire un graphique de façon critique, demander « comment le savons-nous ? », et admettre l'incertitude sans pénalité, sinon la culture fabrique de fausses certitudes par défaut. La tension pour une grande organisation est que la littératie large prend du vrai temps et budget de formation, et questionner la métrique favorite d'une personne senior peut sembler limitant pour la carrière, donc des nombres non examinés voyagent vers le haut sans contestation. Apportez une preuve de qui dans la pièce peut réellement interroger la définition et provenance d'une métrique, et rappelez-vous la dernière fois que quelqu'un a été récompensé plutôt que puni pour avoir mis à jour sa vue ou rapporté un échec informatif. Pour les organismes d'entreprise et gouvernementaux, où une mesure mal définie peut piloter le financement ou le rapport public, nommez explicitement qui a le statut de questionner une métrique et protégez-les quand ils l'utilisent.

6. **Comment gardez-vous les analyses importantes contre le biais prévisible, et intégrez-vous la dissidence avant une décision plutôt qu'après ?** Le chapitre liste les pièges qui corrompent discrètement la preuve : biais de confirmation en sélectionnant des données de soutien, biais de survivant en ignorant ce qui manque, ancrage sur un nombre initial, et biais rétrospectif dans les post-mortems. La considération concurrente est la vitesse, puisque la revue d'avocat du diable, le pré-enregistrement de ce que vous attendez de trouver, et des perspectives diverses ralentissent tous une décision et sont les premières choses coupées sous pression de délai. Apportez une analyse récente à haut enjeu et demandez ce qui aurait fait surface si quelqu'un avait été assigné à argumenter le cas opposé, et si l'équipe a écrit ses attentes avant de voir les résultats. Dans les contextes d'entreprise et spécialement gouvernementaux, où les décisions affectent les moyens de subsistance, prestations, ou droits des gens, traitez l'éthique de données et la dissidence structurée comme des exigences permanentes sur les analyses conséquentes, pas des extras qu'un trimestre occupé peut discrètement abandonner.

## Regard sectoriel

**Jeune pousse.** Sans analystes et seulement quelques semaines de marge par pari, votre science de décision est une habitude plutôt qu'une fonction : avant un grand engagement, demandez quel résultat changerait votre avis et si une expérience bon marché peut y répondre plus vite qu'une réunion. Gardez-vous fermement contre parier le trimestre sur une seule corrélation tape-à-l'œil, parce qu'une minuscule équipe ne peut pas récupérer d'une feuille de route mal dirigée. Gardez-le léger, une ligne écrite dans le document de décision nommant le signal qui vous ferait arrêter, pas une revue formelle que vous n'exécuterez jamais.

**Petite entreprise.** Vous n'avez probablement pas de spécialiste de données et achetez de l'analytique dans des outils que vous utilisez déjà, donc le risque est de faire confiance à un tableau de bord de fournisseur sans questionner comment une métrique est définie ou si sa comparaison est équitable. Dépensez votre attention rare sur le raisonnement plutôt que l'outillage : séparez la corrélation de la causalité sur les une ou deux décisions qui déplacent réellement l'entreprise, et énoncez-vous la plage honnête avant de vous engager sur de l'argent que vous ne pouvez pas récupérer. Quand un outil offre d'automatiser une décision, gardez une personne dans la boucle partout où un mauvais appel vous coûterait un client.

**Grande entreprise.** À travers de nombreuses équipes le problème est la cohérence et la gouvernance : une attente partagée que les analyses nomment la décision et les critères de mort en amont, que les revendications causales énoncent leurs hypothèses, et que les chiffres conséquents portent des plages dans les présentations de conseil et audits. Séparez les métriques d'apprentissage de l'évaluation de performance à l'échelle de l'organisation pour que la mesure ne tourne pas en surveillance et manipulation. Investissez dans une littératie de données large et dans des pratiques de revue telles que l'avocat du diable et le pré-enregistrement, pour qu'un présentateur confiant ne puisse pas substituer la preuve à l'échelle.

**Gouvernement.** L'approvisionnement, la transparence, et la responsabilité publique élèvent les enjeux sur chaque revendication causale, parce qu'une politique justifiée par une corrélation fallacieuse mal alloue l'argent public et peut nuire aux citoyens. Préférez des conceptions de comparaison rigoureuses pour l'évaluation de programme, communiquez les effets comme plages avec des hypothèses énoncées aux organismes de surveillance, et documentez le raisonnement pour qu'un audit puisse le suivre. Dirigez la mesure vers les résultats de programme plutôt que vers la surveillance des agents de dossier, et donnez au public un compte clair de comment la preuve a façonné la décision.

## Exemples

**Jeune pousse.** Une jeune pousse pré-Série-A a remarqué que les utilisateurs qui rejoignaient son forum communautaire se désabonnaient bien moins, et les fondateurs étaient prêts à pointer toute la feuille de route vers les fonctionnalités de forum. Avant de s'engager, l'un d'eux a demandé ce qui changerait leur avis, et un coup d'œil rapide a montré que les clients déjà engagés étaient simplement ceux qui prenaient la peine de rejoindre le forum. Ils ont exécuté une petite expérience au lieu de parier le trimestre sur une corrélation, et ont fait de « qu'est-ce qui changerait notre avis ? » une question standard dans leurs documents de décision.

**Grande entreprise.** Une firme de services financiers a remarqué que les clients utilisant une fonctionnalité particulière avaient un désabonnement bien plus bas et a presque lancé une campagne coûteuse pour pousser tout le monde vers elle. Une revue de science de décision a signalé le facteur de confusion évident : les clients déjà engagés s'auto-sélectionnaient dans la fonctionnalité. Une expérience contrôlée a ensuite montré que la fonctionnalité elle-même avait peu d'effet causal sur le désabonnement. La firme a évité un large investissement mal dirigé, et le leadership a adopté « qu'est-ce qui changerait notre avis ? » comme question standard avant les grandes dépenses.

**Gouvernement.** Une agence publique évaluant un programme d'emploi a résisté à revendiquer le succès depuis la statistique brute que les participants trouvaient des emplois à un taux élevé, reconnaissant que les gens motivés s'auto-sélectionnent dans de tels programmes. Elle a utilisé une conception de comparaison rigoureuse et communiqué l'effet estimé comme une plage avec des hypothèses énoncées aux organismes de surveillance. La mesure s'est concentrée sur les résultats de programme plutôt que sur la surveillance des agents de dossier, ce qui a préservé la confiance de première ligne tout en pilotant quand même la responsabilité et l'amélioration.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur investissement de la science de décision est le coût évité de décisions confiantes mais fausses et la qualité améliorée des décisions qu'une organisation prend des milliers de fois. Un seul choix stratégique ou de politique majeur justifié par une corrélation fallacieuse peut gaspiller bien plus que le coût entier de construire de bonnes pratiques de décision. Une meilleure calibration (savoir ce que vous savez et ne savez pas) vous permet de dimensionner les paris de façon appropriée et d'éviter à la fois les engagements imprudents et la paralysie. En agrégé, une culture informée par les données se compose : chaque équipe prenant des décisions légèrement meilleures et mieux raisonnées est un levier énorme.

Le coût d'adoption est surtout culturel et éducatif : formation en littératie de données, temps pour l'analyse et revue soigneuses, et volonté du leadership de changer les décisions et admettre l'incertitude. C'est moins cher en dollars que les plateformes des chapitres précédents mais plus difficile à installer, parce que cela demande aux gens puissants d'être gouvernés par la preuve. Pesez-le contre le coût de ne pas adopter : le théâtre de données qui gaspille l'effort analytique, des décisions pilotées par la voix la plus confiante, des revendications causales qui s'effondrent au contact avec la réalité, et, où la surveillance s'installe, une main-d'œuvre qui manipule les métriques et cache les mauvaises nouvelles. Auprès de la direction, l'argument est simple. Tout l'investissement de données antérieur ne paie que si le dernier kilomètre de la perspicacité à la décision est solide, et la science de décision est ce dernier kilomètre.

## Anti-patterns et pièges

- Théâtre de données : analyse produite pour justifier une décision déjà prise.
- Glisser de « corrélé avec » à « cause » sans interroger les facteurs de confusion.
- Présenter des estimations ponctuelles comme certitudes, cachant la plage d'incertitude.
- Biais de confirmation : chercher seulement des données qui soutiennent une conclusion préférée.
- Décisions HiPPO où l'opinion de la personne la mieux payée outrepasse la preuve.
- Transformer les métriques en surveillance individuelle, provoquant la manipulation et la peur.
- Loi de Goodhart en action : une métrique cible qui arrête de mesurer ce qui compte.
- Punir les gens pour des échecs informatifs, tuant l'honnêteté et l'expérimentation.

## Modèle de maturité

1. **Initier.** Les décisions fonctionnent sur la hiérarchie et l'intuition, et la voix la plus forte ou senior gagne. La corrélation est librement traitée comme causalité, l'incertitude est ignorée, et les quelques métriques utilisées surveillent les individus et sont manipulées.
2. **Développer.** Certaines équipes consultent les données et montrent une conscience des pièges causaux, mais l'analyse est souvent sélective, produite pour justifier une décision déjà prise. L'incertitude est rarement communiquée, et les pratiques de mesure sont incohérentes d'équipe à équipe.
3. **Standardiser.** L'organisation documente et impose une pratique partagée : les analyses sont liées à une décision nommée avec des critères prédéfinis, les équipes distinguent la corrélation de la causalité et préfèrent les expériences pour les revendications causales, les nombres portent des plages et hypothèses énoncées, et la mesure vise les résultats plutôt que les individus, avec la sécurité psychologique protégée.
4. **Gérer.** La qualité de décision est mesurée et contrôlée contre des références. L'organisation suit à quelle fréquence les analyses ont nommé un signal de mort avant que les données n'arrivent, la part de chiffres conséquents livrés avec une plage communiquée, combien de revendications causales reposaient sur des expériences contre une simple corrélation, et si les décisions se sont renversées sur preuve. Les pratiques de garde contre le biais telles que le pré-enregistrement et la revue d'avocat du diable sont auditées, et les métriques qui commencent à être manipulées sont attrapées et retirées.
5. **Orchestrer.** Le raisonnement solide s'améliore continuellement et est intégré à travers l'organisation. « Qu'est-ce qui changerait notre avis ? » est routinier avant toute décision majeure, la rigueur causale et l'incertitude honnête sont des normes culturelles, et les leaders mettent à jour visiblement sur la preuve et admettent ce qui est inconnu. La mesure pilote l'apprentissage sans surveillance, les pratiques de décision s'adaptent à mesure que l'organisation et ses risques changent, et chaque niveau décide mieux en conséquence.

## Pistes de réflexion

- Où dans votre organisation les données sont-elles utilisées pour décorer des décisions déjà prises ?
- Quelle décision récente reposait sur une corrélation qui pourrait ne pas être causale ?
- À quel point vos rapports communiquent-ils honnêtement l'incertitude, et qui résiste aux plages ?
- Vos métriques visent-elles à améliorer les systèmes ou à surveiller les individus ?
- Quand un leader a-t-il pour la dernière fois visiblement changé une décision à cause des données ?
- Comment empêchez-vous la poursuite de la mesure de basculer en surveillance ?

## Points clés à retenir

- Le but des données est de meilleures décisions ; gardez-vous contre le théâtre de données.
- Énoncez ce qui changerait votre avis avant de regarder les données.
- Ne confondez jamais la corrélation avec la causalité ; interrogez les facteurs de confusion et préférez les expériences.
- Communiquez l'incertitude honnêtement ; la fausse précision détruit la confiance quand elle échoue.
- Soyez informé par les données, pas asservi aux données ; le jugement et le contexte comptent encore.
- Mesurez les systèmes et résultats pour apprendre, pas les individus pour surveiller.
- Protégez la sécurité psychologique pour que les gens mettent à jour leurs croyances et fassent surface les mauvaises nouvelles.

## Références et lectures complémentaires

- Daniel Kahneman, « Thinking, Fast and Slow ».
- Judea Pearl et Dana Mackenzie, « The Book of Why ».
- Douglas W. Hubbard, « How to Measure Anything ».
- Nate Silver, « The Signal and the Noise ».
- Cathy O'Neil, « Weapons of Math Destruction ».
- Darrell Huff, « How to Lie with Statistics ».
- Philip Tetlock et Dan Gardner, « Superforecasting ».
- Charles Wheelan, « Naked Statistics ».
