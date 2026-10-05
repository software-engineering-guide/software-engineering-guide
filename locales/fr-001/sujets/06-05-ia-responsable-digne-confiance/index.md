# 6.5 IA responsable et digne de confiance

## Vue d'ensemble et motivation

L'IA responsable et digne de confiance est la pratique de construire et exploiter des systèmes d'IA qui sont équitables, transparents, responsables, sûrs, et respectueux de la confidentialité. Cela signifie aussi être capable de montrer tout cela aux personnes affectées et aux régulateurs. À mesure que l'IA prend en charge des décisions qui façonnent la vie des gens (embauche, prêt, éligibilité aux prestations), la question n'est plus seulement « est-ce que cela fonctionne ? » mais « est-ce juste, et pouvons-nous le justifier ? » Un système qui est précis en moyenne peut quand même être injuste envers un sous-groupe, inexplicable à la personne qu'il affecte, ou dangereux quand mal utilisé. Vous gagnez la confiance en adressant ces dimensions délibérément, pas en espérant qu'elles se règlent d'elles-mêmes.

Pour les grandes équipes, l'IA responsable ne peut pas être le travail d'une seule personne ou une case à cocher à la fin. Tissez-la dans comment vous concevez, évaluez, déployez, et gouvernez les systèmes, avec une propriété et une escalade claires. À l'échelle, de petits biais et lacunes de surveillance affectent de nombreuses personnes. Un seul échec très médiatisé peut endommager votre réputation et inviter la réglementation. Les cadres de gouvernance existent précisément parce que les bonnes intentions au coup par coup ne s'échelonnent pas.

L'administration publique et les organisations régulées font face à des obligations contraignantes. Les lois émergentes, telles que l'[EU AI Act](https://fr.wikipedia.org/wiki/R%C3%A8glement_sur_l%27intelligence_artificielle), imposent des exigences graduées par risque. Des normes comme le NIST AI Risk Management Framework et l'ISO/IEC 42001 vous donnent des façons structurées de les satisfaire. Les organismes publics doivent éviter la discrimination illégale, fournir des voies pour contester les décisions automatisées, et être transparents sur comment l'IA est utilisée dans l'exercice de l'autorité publique. L'IA responsable dans ces contextes est à la fois un devoir éthique et une nécessité légale.

*Voir aussi :* chapitre 6.1 (stratégie et préparation à l'IA), chapitre 10.5 (éthique, responsabilité, et intérêt public), et chapitre 4.5 (confidentialité et protection des données).

## Principes clés

- L'équité est un objectif de conception à mesurer et gérer, pas à supposer.
- Les personnes affectées par les décisions d'IA méritent une explication et une voie pour les contester.
- La responsabilité repose sur les humains et l'organisation, jamais sur le modèle.
- La confidentialité et la sécurité doivent être conçues, incluant la protection contre le mésusage et l'abus.
- La gouvernance devrait suivre des cadres reconnus pour qu'elle soit défendable et auditable.
- La surveillance humaine doit être significative, avec une vraie autorité pour outrepasser et arrêter.
- Considérez les coûts plus larges de l'IA, incluant son empreinte environnementale.

## Recommandations

### Détecter et atténuer le biais et l'iniquité

Définissez ce que l'équité signifie pour votre contexte. Il y a de multiples définitions mathématiques, parfois contradictoires, et la bonne dépend de la décision et de la loi. Testez les modèles pour la performance disparate à travers les groupes protégés et vulnérables en utilisant des données représentatives. Faites cela avant le déploiement et continuez de le faire après, parce que le [biais](https://fr.wikipedia.org/wiki/Biais_algorithmique) peut émerger à mesure que les populations changent. Atténuez à travers de meilleures données, repondération, contraintes, ou changement de comment le système est utilisé, et documentez les compromis que vous avez acceptés. Retirer un attribut protégé ne retire pas le biais, puisque les proxys demeurent. Traitez l'équité comme une discipline continue de mesure et gestion, pas une autorisation ponctuelle.

### Fournir l'explicabilité, l'interprétabilité, et la transparence

Assortissez le niveau d'explication aux enjeux et à l'audience. Pour les décisions conséquentes, donnez aux personnes affectées une raison claire et en langage simple qu'elles peuvent comprendre et sur laquelle agir. Pour la gouvernance interne, gardez assez d'[interprétabilité](https://fr.wikipedia.org/wiki/Intelligence_artificielle_explicable) technique pour déboguer et défendre le système. Préférez les modèles intrinsèquement interprétables où les enjeux sont élevés et l'interprétabilité est atteignable. Où des modèles complexes sont nécessaires, utilisez des techniques d'explication tout en étant honnête sur leurs limites. Soyez transparent sur quand l'IA est utilisée du tout, spécialement dans les interactions avec le public.

### Gouverner avec des cadres reconnus

Adoptez une approche de gouvernance structurée plutôt que d'en inventer une. Le **NIST AI Risk Management Framework** organise le travail autour de gouverner, cartographier, mesurer, et gérer le risque d'IA. L'**EU AI Act** classifie les systèmes par risque et impose des obligations en conséquence, avec des exigences strictes pour les usages à haut risque. **ISO/IEC 42001** définit un système de gestion d'IA qui peut être audité et certifié. Cartographiez vos systèmes vers ces cadres. Maintenez de la documentation telle que des fiches de modèle et de données (résumés standardisés du but, performance, et limitations d'un modèle ou jeu de données). Exécutez des évaluations de risque avant le déploiement, et gardez un inventaire des systèmes d'IA avec leurs niveaux de risque et propriétaires. Une bonne gouvernance assigne des rôles clairs, droits de décision, et chemins d'escalade.

### Assurer la surveillance humaine, la responsabilité, et l'appel

Gardez un humain significativement en contrôle des décisions conséquentes, avec une vraie autorité et l'information nécessaire pour outrepasser le système, pas un tampon en caoutchouc. Assignez une responsabilité claire : nommez un propriétaire responsable du comportement de chaque système. Donnez aux personnes affectées par des décisions automatisées un droit à l'explication et un processus viable pour faire appel à un humain qui peut changer le résultat. Journalisez les décisions et leur base, pour que vous puissiez gérer les appels et audits équitablement et rapidement.

### Protéger la confidentialité, la sécurité, et contre le mésusage

Minimisez les données personnelles que vous collectez et utilisez, établissez une base légale, et appliquez des techniques de confidentialité adaptées à la sensibilité impliquée. Faites de l'[équipe rouge](https://fr.wikipedia.org/wiki/%C3%89quipe_rouge) sur les systèmes avant et après le déploiement pour trouver des façons dont ils peuvent être manipulés, débridés, ou mal utilisés pour causer du dommage, et corrigez ce que vous trouvez. Construisez des garde-fous contre la génération de contenu dangereux, la fuite de données sensibles, ou l'activation d'abus. Planifiez pour les incidents : surveillance, réponse, et divulgation. Considérez le [double usage](https://fr.wikipedia.org/wiki/Technologie_%C3%A0_double_usage) (la même capacité servant des fins bénéfiques et dangereuses) et le mésusage en aval, pas seulement l'usage voulu.

### Tenir compte du coût environnemental

Entraîner et servir de grands modèles consomme de l'énergie et de l'eau significatives. Mesurez et rapportez l'empreinte des principales charges de travail d'IA. Préférez des modèles et matériel efficaces où ils satisfont le besoin. Dimensionnez correctement les modèles à la tâche plutôt que de choisir par défaut le plus grand, et intégrez le coût environnemental dans les décisions d'architecture et d'approvisionnement.

## Compromis : avantages et inconvénients

| Tension | Un côté | L'autre côté |
|---|---|---|
| Précision contre équité | Précision moyenne la plus haute | Résultats équitables à travers les groupes |
| Performance contre interprétabilité | Modèles complexes et puissants | Modèles explicables et défendables |
| Automatisation contre surveillance | Efficacité et échelle | Contrôle humain et responsabilité |
| Utilité de données contre confidentialité | Modèles plus riches depuis plus de données | Minimisation et protection de données |
| Capacité contre sécurité | Fonctionnalité large et ouverte | Comportement contraint et gardé |
| Vitesse contre gouvernance | Déploiement rapide | Revue et documentation approfondies |

Il n'y a rarement de déjeuner gratuit. Améliorer l'équité peut coûter de la précision. L'interprétabilité peut coûter de la performance. La gouvernance coûte du temps. Le chemin responsable est de faire ces compromis consciemment, de les documenter, et de choisir en faveur des personnes affectées et de la défendabilité quand les enjeux sont élevés. Cadrer la gouvernance comme un frein à l'innovation est une fausse dichotomie. Le risque d'IA non géré est lui-même une menace à l'innovation soutenue.

## Questions à discuter avec votre équipe

1. **Lesquels de nos systèmes d'IA déployés l'EU AI Act classifierait-il comme haut risque, et satisfaisons-nous ces obligations aujourd'hui ?** La loi graduée par risque est maintenant contraignante, pas hypothétique, et un système qui décide l'embauche, le prêt, ou l'éligibilité aux prestations peut porter des exigences strictes que vous violez peut-être déjà. Pour une grande organisation, cette question force un inventaire honnête plutôt qu'une supposition confortable que la gouvernance est « gérée ». Apportez votre liste de systèmes d'IA avec leurs niveaux de risque et propriétaires, cartographiés contre l'EU AI Act, le NIST AI Risk Management Framework, et l'ISO/IEC 42001 où pertinent. Le signal à surveiller est tout système conséquent sans classification de risque, sans évaluation d'impact, et sans fiche de modèle ou de données. Pour les organismes publics exerçant l'autorité publique, des obligations manquantes ne sont pas un élément d'arriéré, c'est une exposition légale, et la réponse devrait déclencher les évaluations et la documentation que ces systèmes exigent.

2. **Quand un de nos modèles refuse quelqu'un, cette personne peut-elle obtenir une raison en langage simple et atteindre un humain qui peut réellement renverser le résultat ?** Un droit à l'explication et un appel viable sont ce qui sépare l'IA responsable d'une boîte noire qui nuit aux gens sans recours. L'équité mesurée en moyenne peut quand même échouer un individu, et l'interprétabilité choisie après le déploiement est habituellement du théâtre. Apportez une décision déployée spécifique et tracez-la : la raison que la personne affectée reçoit, le canal d'appel, et si l'humain de l'autre côté a une vraie autorité et la base journalisée pour outrepasser. Dans l'administration publique et les contextes régulés, une voie d'appel est souvent une exigence légale, pas une courtoisie. Si la raison est inintelligible ou l'appel mène à un tampon en caoutchouc, c'est la lacune à corriger avant la prochaine sortie.

3. **Qui est la seule personne nommée responsable quand un modèle cause du dommage, et a-t-elle une vraie autorité pour l'arrêter ?** La responsabilité repose sur les humains et l'organisation, jamais sur le modèle, mais ce principe est vide jusqu'à ce qu'un nom soit attaché à chaque système et que cette personne puisse réellement débrancher. Pour une grande équipe, la propriété diffuse signifie que quand un échec d'équité ou un débridage fait surface, tout le monde suppose que quelqu'un d'autre surveille. Apportez votre carte de propriété, vos chemins d'escalade, et une preuve que la surveillance est significative : le propriétaire nommé obtient-il l'information et le pouvoir d'outrepasser ou arrêter le système, ou seulement de hocher la tête ? Discutez comment vous faites de l'équipe rouge pour le mésusage et l'abus que vous n'avez pas encore imaginé, puisque tester seulement l'usage voulu manque les échecs qui font les gros titres. La réponse devrait ne laisser aucun système conséquent sans propriétaire responsable qui peut l'arrêter.

4. **Pour chaque modèle conséquent, quelle définition d'équité avons-nous choisie, qui l'a approuvée, et nos métriques de sous-groupe tiennent-elles réellement en production ?** L'équité a plusieurs définitions mathématiques qui entrent en conflit entre elles, donc un modèle qui satisfait des taux de faux positif égaux peut violer des résultats égaux, et choisir une définition est un jugement de valeur qui ne devrait pas être laissé à quiconque a écrit la boucle d'entraînement. Pour une grande équipe, une valeur par défaut non examinée cache le choix à l'intérieur du code et fait que chaque groupe en aval hérite d'une décision que personne n'a débattue. Apportez la métrique d'équité que vous avez optimisée, les groupes protégés et vulnérables à travers lesquels vous avez testé, les données représentatives que vous avez utilisées, et la dérive que vous avez vue depuis le lancement, puisque retirer un attribut protégé laisse des proxys qui gardent le biais vivant. Dans les contextes d'entreprise et gouvernementaux, nommez la personne avec l'autorité d'accepter un compromis d'équité et enregistrez-le, parce qu'un régulateur ou un ombudsman demandera qui a décidé que cette définition de juste était la bonne pour les gens refusés un prêt, une prestation, ou un emploi. Si aucune métrique de sous-groupe n'est surveillée après le déploiement, traitez le modèle comme non mesuré plutôt que juste.

5. **Sur combien peu de données personnelles chaque système peut-il fonctionner, et l'avons-nous soumis à l'équipe rouge pour le mésusage et double usage auxquels nous préférerions ne pas penser ?** La confidentialité et la sécurité doivent être conçues, et la façon la moins chère de réduire à la fois le risque de violation et la surface d'abus est de collecter et retenir moins de données en premier lieu, pourtant les équipes thésaurisent routinièrement les entrées « au cas où elles aideraient plus tard ». Pour une grande organisation, chaque champ supplémentaire est une question de base légale, une obligation de rétention, et un prix plus grand pour un attaquant ou un débridage. Apportez l'inventaire de données et la base légale pour chaque système, les résultats de l'équipe rouge pour la manipulation, la fuite, et la génération dangereuse, et une liste honnête de capacités à double usage où la même fonctionnalité qui aide un utilisateur légitime aide aussi quelqu'un agissant de mauvaise foi. Dans les contextes régulés et publics, liez cela à votre plan d'incident : surveillance, réponse, et divulgation, parce qu'un organisme public qui fuit des données sensibles ou livre un système débridable fait face à des devoirs statutaires, pas seulement de l'embarras. Si l'équipe rouge n'a jamais exercé que le chemin voulu, vous avez testé la démonstration, pas le système.

6. **Mesurons-nous et possédons-nous l'empreinte environnementale de nos principales charges de travail d'IA, ou « utiliser le plus grand modèle » est-il une valeur par défaut non évaluée ?** Entraîner et servir de grands modèles consomme de la vraie énergie et de l'eau, et choisir par défaut le plus grand modèle pour des tâches qu'un plus petit gérerait transforme un raccourci d'ingénierie en un coût récurrent que l'organisation ne voit jamais sur un tableau de bord. Pour une grande équipe exploitant de nombreuses charges de travail, de petites inefficacités par appel se composent en une empreinte qui devient un passif d'approvisionnement et de rapport à mesure que les attentes de divulgation se resserrent. Apportez l'empreinte mesurée de vos charges de travail les plus lourdes, une comparaison de tailles de modèle contre la précision que la tâche exige réellement, et les choix de matériel et de service que vous pourriez dimensionner correctement. Dans les contextes d'entreprise et gouvernementaux, connectez cela aux engagements de durabilité et critères d'approvisionnement, puisque les organismes publics doivent de plus en plus rapporter l'impact environnemental et justifier la dépense, et une empreinte non mesurée est un chiffre qu'on vous demandera un jour de produire et que vous ne pourrez pas. Décidez si le coût environnemental est un intrant formel du choix de modèle, ou admettez qu'aujourd'hui il ne l'est pas.

## Regard sectoriel

**Jeune pousse.** Vous ne pouvez pas doter un conseil de gouvernance, donc faites la version légère qui compte encore. Choisissez des modèles interprétables où la décision est conséquente, écrivez une fiche de modèle d'une page, testez pour des résultats disparates à travers les groupes que vous pouvez mesurer, et journalisez les décisions pour pouvoir revisiter l'équité à mesure que vous grandissez. Donnez à toute décision défavorable une raison simple et une voie vers un humain. Sauter cela n'est pas de la vitesse, c'est un passif que vous ne pouvez pas vous permettre si une seule décision injuste atteint la presse ou un régulateur.

**Petite entreprise.** Sans spécialiste dédié, traitez l'IA responsable comme une question d'achat : préférez les fournisseurs qui documentent le test d'équité, exposent des fiches de modèle et de données, et vous laissent divulguer aux clients quand l'IA est utilisée. Sachez quelles données personnelles vos outils collectent et si vous avez une base légale pour les utiliser. Où une mauvaise réponse automatisée pourrait nuire à un client, gardez une personne dans la boucle plutôt que de faire confiance à un outil que vous ne pouvez pas inspecter ou expliquer.

**Grande entreprise.** La tâche est la gouvernance à l'échelle à travers de nombreuses équipes : cartographiez chaque système vers le NIST AI Risk Management Framework, l'EU AI Act, et l'ISO/IEC 42001, gardez un inventaire avec des niveaux de risque et propriétaires nommés, et exigez le test d'équité, sécurité, et confidentialité avant et après le lancement. Standardisez les fiches de modèle et de données, l'équipe rouge, et les processus d'appel pour que les groupes arrêtent de les réinventer. Budgétisez explicitement les coûts de gouvernance, surveillance, et interprétabilité, et traitez le risque d'IA non géré comme une menace à la licence d'opérer.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la responsabilité publique façonnent chaque choix. Publiez un avis de transparence en langage clair, exécutez une évaluation d'impact avant le déploiement, et gardez une prise de décision humaine significative pour toute action affectant un citoyen, avec une voie d'appel viable. Exigez que les fournisseurs divulguent les limitations de modèle et accordent la portabilité de données, évitez la discrimination illégale, nommez un fonctionnaire responsable pour chaque système, et rapportez l'empreinte environnementale des principales charges de travail.

## Exemples

**Jeune pousse.** Une petite jeune pousse de prêt construisant une fonctionnalité de notation de crédit précoce ne pouvait pas doter un conseil de gouvernance, donc elle a fait la version légère qui comptait encore. Deux fondateurs ont approuvé le modèle ensemble, l'ont testé pour des résultats disparates à travers les groupes qu'ils pouvaient mesurer, et écrit une courte fiche de modèle d'une page couvrant ses données, limites, et risques connus. Ils ont choisi un modèle plus simple et plus interprétable pour pouvoir donner à tout candidat refusé une raison simple et un chemin vers une revue humaine, et ils ont journalisé les décisions pour pouvoir revisiter l'équité à mesure qu'ils grandissaient.

**Grande entreprise.** Une banque déployant un modèle de crédit a établi un conseil de gouvernance d'IA, cartographié le modèle vers une catégorie à haut risque, et exigé un test d'équité à travers les groupes démographiques avant et après le lancement. Elle a documenté le modèle dans une fiche de modèle. Elle a donné aux candidats refusés une raison en langage clair et un appel à un souscripteur humain, et a soumis le système à l'équipe rouge pour la manipulation. Elle a choisi un modèle quelque peu moins précis mais plus interprétable, parce qu'elle devait expliquer et défendre chaque décision aux régulateurs.

**Gouvernement.** Une agence publique utilisant l'IA pour aider à allouer les ressources d'inspection a aligné son programme sur le NIST AI RMF et les dispositions pertinentes de la loi d'IA applicable. Elle a publié un avis de transparence décrivant comment le système fonctionnait et ses garde-fous. Elle a conduit une évaluation d'impact avant le déploiement, gardé une prise de décision humaine significative pour toute action affectant un citoyen, et fourni un processus d'appel. L'équité était surveillée continuellement, le coût environnemental de la charge de travail était rapporté, et un fonctionnaire responsable était nommé comme redevable du système.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

L'IA responsable protège la valeur autant qu'elle en crée. Le retour sur investissement est largement du coût évité : moins de plaintes de discrimination, pénalités réglementaires, et désastres réputationnels ; des audits plus fluides ; et une plus grande confiance utilisateur et publique, qui pilote l'adoption. Les systèmes dignes de confiance sont aussi plus robustes, parce que la discipline qui produit l'équité et la sécurité produit aussi une meilleure ingénierie.

Le coût total de possession inclut le personnel de gouvernance, le test d'équité et sécurité, la documentation, l'équipe rouge, les processus de surveillance, et la performance parfois échangée pour l'interprétabilité ou l'équité. Pesez cela contre le coût de ne pas investir : responsabilité légale, arrêts forcés, confiance publique perdue, et le coût bien plus élevé de rétro-adapter la gouvernance après un échec. Dans les contextes régulés, l'investissement en IA responsable est de plus en plus non négociable. Faites valoir cela auprès de la direction en le cadrant comme gestion de risque et licence d'opérer : la précondition pour déployer l'IA à l'échelle du tout.

## Anti-patterns et pièges

- **Équité par omission.** Supposer qu'un modèle est équitable parce qu'il ignore les attributs protégés.
- **Théâtre d'explicabilité.** Produire des explications qui ne reflètent pas réellement comment les décisions sont prises.
- **Surveillance de tampon en caoutchouc.** Une revue humaine nominale sans vraie autorité ou information pour outrepasser.
- **Gouvernance comme pensée après coup.** Boulonner la documentation et la revue après la conception et le déploiement.
- **Aucune voie d'appel.** Laisser les personnes affectées sans façon de contester une décision automatisée.
- **Ignorer le mésusage.** Tester seulement l'usage voulu et manquer les débridages et abus.
- **Cécité d'empreinte.** Choisir par défaut le plus grand modèle sans égard pour le coût environnemental.

## Modèle de maturité

1. **Initier.** Aucun test d'équité, explications, ou gouvernance ; la responsabilité est indéfinie ; les problèmes de biais, mésusage, et confidentialité font surface seulement après le dommage, et il n'y a aucun inventaire de systèmes d'IA ou de leurs risques.
2. **Développer.** Un certain test de biais, des fiches de modèle, et de l'équipe rouge se produisent sur des systèmes individuels, mais la pratique est incohérente à travers les équipes ; la surveillance est au coup par coup ; des cadres comme le NIST AI Risk Management Framework et l'EU AI Act sont connus mais seulement partiellement adoptés.
3. **Standardiser.** La gouvernance est documentée et imposée à l'échelle de l'organisation : les systèmes sont cartographiés vers des cadres reconnus et l'ISO/IEC 42001, chacun a un niveau de risque et un propriétaire nommé, et le test d'équité, sécurité, et confidentialité, les fiches de modèle et de données, les voies d'appel, et l'équipe rouge pour les systèmes à haut risque sont exigés plutôt qu'optionnels.
4. **Gérer.** Le programme est mesuré et contrôlé avec des données : les métriques d'équité de sous-groupe, les découvertes de sécurité et débridage, les volumes d'appel et taux de renversement, les taux d'outrepassement de surveillance, et l'empreinte de charge de travail sont suivis contre des références et seuils ; la dérive et les résultats disparates déclenchent une action définie ; les décisions de feu vert ou non reposent sur la preuve plutôt que l'assurance.
5. **Orchestrer.** L'IA responsable s'améliore continuellement et est intégrée à travers l'organisation : la surveillance de l'équité, sécurité, et mésusage s'exécute en production, la gouvernance est construite dans la livraison, le coût environnemental est un intrant formel du choix de modèle, et l'organisation adapte ses contrôles à mesure que la loi, le risque, et la capacité changent, avec la responsabilité possédée par tous plutôt qu'une seule équipe.

## Pistes de réflexion

- Quelle définition d'équité s'applique à une décision donnée, et qui décide ?
- Combien de précision ou performance est-il acceptable d'échanger pour l'équité ou l'interprétabilité ?
- Qu'est-ce qui rend la surveillance humaine significative plutôt qu'un tampon en caoutchouc ?
- Comment les appels contre les décisions automatisées devraient-ils être conçus pour être équitables et opportuns ?
- Comment faites-vous de l'équipe rouge pour le mésusage que vous n'avez pas encore imaginé ?
- Le coût environnemental devrait-il influencer le choix de modèle, et comment le pèseriez-vous ?

## Points clés à retenir

- L'IA digne de confiance est équitable, explicable, responsable, sûre, et respectueuse de la confidentialité, par conception.
- L'équité et la sécurité sont des disciplines de mesure et gestion continues, pas des vérifications ponctuelles.
- Alignez la gouvernance sur le NIST AI RMF, l'EU AI Act, et l'ISO/IEC 42001 pour être défendable et auditable.
- Gardez une surveillance humaine significative, une responsabilité claire, et un vrai droit d'appel.
- Concevez pour la confidentialité et contre le mésusage, et tenez compte du coût environnemental.

## Références et lectures complémentaires

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, et Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Math Destruction*.
- Emma Strubell, Ananya Ganesh, et Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
