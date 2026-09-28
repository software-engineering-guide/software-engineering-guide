# 6.4 Développement logiciel assisté par IA

## Vue d'ensemble et motivation

Les assistants de codage IA peuvent maintenant générer du code, compléter des fonctions, écrire des tests, expliquer des systèmes inconnus, et vous aider à [refactoriser](https://fr.wikipedia.org/wiki/Refactorisation). Bien utilisés, ils accélèrent le travail routinier. Ils abaissent la barrière vers des langages et cadriciels inconnus. Ils retirent la corvée du code passe-partout.

Mal utilisés, ils causent un vrai dommage. Ils peuvent inonder une base de code de code qui paraît plausible mais est subtilement faux. Ils peuvent introduire des trous de sécurité, créer une exposition de licensing, et éroder les compétences des ingénieurs qui s'y appuient. Le développement assisté par IA est un vrai outil de productivité et un vrai risque en même temps. La différence réside presque entièrement dans la discipline d'ingénierie autour de lui.

Pour les grandes équipes, le défi est la cohérence et la sécurité à l'échelle. Quand des centaines de développeurs utilisent des assistants IA, de petites habitudes individuelles s'additionnent en résultats organisationnels. Si tout le monde accepte les suggestions sans esprit critique, la charge de revue et les taux de défaut augmentent. Si vous fournissez des normes claires, de bonnes valeurs par défaut, et une vérification forte, les mêmes outils augmentent le débit sans abaisser la qualité. L'histoire de productivité est aussi plus nuancée que les affirmations de fournisseur ne le suggèrent. Les vrais gains varient largement par tâche, et une mesure naïve, comme compter les suggestions acceptées, vous induira en erreur.

Les contextes d'entreprise et gouvernementaux ajoutent des contraintes plus nettes. Le code qui touche des systèmes régulés, gère des données sensibles, ou exécute une infrastructure critique ne peut pas être fiable simplement parce qu'une IA l'a produit. La provenance de licensing compte quand le code généré peut écho des données d'entraînement sous licences restrictives. Certaines organisations doivent garder le code source sur site et ne peuvent pas l'envoyer du tout à des services externes. Fixer des normes claires et applicables pour l'assistance IA fait maintenant partie du leadership d'ingénierie responsable. Parmi les assistants disponibles, les outils construits sur les modèles Claude d'Anthropic sont une option de premier plan aux côtés d'autres ; les pratiques ci-dessous s'appliquent quel que soit celui que vous adoptez.

*Voir aussi :* chapitre 2.5 (revue de code et collaboration), chapitre 2.4 (stratégie de test), et chapitre 6.5 (IA responsable et digne de confiance).

## Principes clés

- L'ingénieur, pas l'assistant, est responsable de chaque ligne commise.
- Le code généré par IA est un brouillon à réviser et vérifier, jamais un produit fini à qui faire confiance.
- L'effort de vérification devrait s'échelonner avec le risque du code, pas avec à quel point la sortie paraît confiante.
- Mesurez la productivité par des résultats qui comptent (valeur livrée, qualité, temps de cycle), pas par des comptes de suggestion.
- Protégez contre les risques de sécurité et licensing introduits à travers le code généré.
- Préservez et développez la compétence d'ingénierie humaine ; ne laissez pas les assistants la vider.
- Soyez transparent sur où et comment l'assistance IA est utilisée.

## Recommandations

### Utiliser la programmation en binôme IA comme un outil de brouillon et d'exploration

Pointez les assistants vers des tâches où ils brillent et les erreurs sont bon marché à attraper : code passe-partout, échafaudage de test, conversions de format, expliquer du code inconnu, et explorer des approches. Traitez leur sortie comme un premier brouillon. Restez au volant. Lisez, comprenez, et éditez chaque suggestion plutôt que d'accepter en pilote automatique. Dans les domaines inconnus, utilisez l'assistant pour apprendre, mais vérifiez ses affirmations contre la documentation faisant autorité. Les assistants peuvent inventer des API et mal énoncer le comportement avec une confiance totale.

### Réviser, tester, et vérifier le code généré par IA comme une entrée non fiable

Donnez au code généré par IA le même examen que vous donneriez au code d'un nouveau membre d'équipe, ou plus. Un relecteur humain devrait le comprendre assez bien pour l'expliquer et le maintenir. « L'IA l'a écrit » n'est jamais une réponse acceptable à « pourquoi cela fonctionne-t-il ? » Insistez sur les tests, et méfiez-vous des tests générés par IA qui affirment simplement le comportement actuel plutôt que le comportement voulu. Exécutez de l'[analyse statique](https://fr.wikipedia.org/wiki/Analyse_statique_de_programmes), du scan de sécurité, et des vérifications de dépendance. Pour le code à haut risque (authentification, [cryptographie](https://fr.wikipedia.org/wiki/Cryptographie), logique financière, systèmes de sécurité), traitez la sortie IA comme un point de départ qui exige une vérification humaine experte, jamais comme faisant autorité.

### Mesurer la productivité honnêtement et fixer des attentes réalistes

Sautez les métriques de vanité comme le taux d'acceptation ou les lignes générées. Regardez plutôt les signaux de livraison et de qualité dans le temps : temps de cycle, taux d'échec de changement, taux d'échappement de défaut, et efficacité rapportée par les développeurs. Les gains sont réels mais inégaux : grands pour certaines tâches, négligeables ou négatifs pour d'autres. Le temps économisé à écrire du code peut être perdu de nouveau à le réviser et le déboguer. Fixez les attentes avec la direction en conséquence, pour que l'investissement repose sur la preuve plutôt que le battage, et pour que les équipes ne soient jamais pressées d'accepter des suggestions dangereuses juste pour atteindre une métrique.

### Gérer les risques de sécurité et licensing

Scannez le code généré pour les vulnérabilités et motifs dangereux. Les assistants peuvent reproduire des idiomes dangereux de leurs données d'entraînement. Ne collez jamais de secrets, identifiants, ou données sensibles dans des prompts envoyés à des services externes. Préférez les outils qui satisfont vos exigences de gestion de données, incluant le déploiement sur site ou privé où le code source ne peut pas quitter l'environnement. Adressez aussi le licensing. Le code généré peut ressembler à des données d'entraînement sous licence, donc utilisez des outils et politiques qui réduisent ce risque, gardez la provenance où vous le pouvez, et acheminez tout ce qui est questionnable à travers une revue juridique. Suivez la provenance des dépendances que l'assistant suggère, puisqu'il peut recommander des paquets abandonnés ou malveillants.

### Fixer des normes d'équipe, divulgation, et maintien de compétence

Publiez une directive claire sur quand et comment l'assistance IA peut être utilisée, quelles données ne peuvent jamais être partagées, et quelle vérification chaque niveau de risque exige. Encouragez la transparence sur les contributions assistées par IA où cela compte pour la revue et la responsabilité. Gardez les compétences humaines aiguisées délibérément. Assurez-vous que les ingénieurs, spécialement les juniors, apprennent encore les fondamentaux plutôt que de sous-traiter leur compréhension. Faites tourner les gens à travers du travail qui construit une expertise profonde, et traitez la sur-dépendance comme un vrai risque à long terme pour la capacité de l'équipe.

## Compromis : avantages et inconvénients

| Dimension | Bénéfice de l'assistance IA | Risque de l'assistance IA |
|---|---|---|
| Vitesse | Passe-partout et brouillon plus rapides | Temps perdu à réviser du mauvais code |
| Intégration | Entrée plus facile vers de nouveaux langages/cadriciels | Compréhension superficielle, API inventées |
| Qualité | Plus de tests, refactorisations plus rapides | Code plausible mais subtilement faux |
| Sécurité | Peut suggérer des corrections et scans | Peut introduire des vulnérabilités |
| Compétences | Libère du temps pour du travail à plus haute valeur | Érode les fondamentaux si surutilisé |
| Licensing | Réutilisation plus rapide de motifs communs | Exposition de provenance et licence |

Le compromis central est la vitesse contre la vérification. L'IA déplace l'effort de l'écriture vers la revue. Le gain net dépend de si vos pratiques de revue et vérification sont assez fortes pour attraper ce que l'assistant fait mal. Une revue faible mène au déclin de qualité. Une revue forte et des normes claires capturent le potentiel.

## Questions à discuter avec votre équipe

1. **Quelles parties de notre base de code sont entièrement interdites à l'assistance IA, et comment imposons-nous cette frontière ?** La confiance uniforme est un piège : appliquer le même examen léger à l'authentification, la cryptographie, la logique financière, et les systèmes de sécurité qu'au passe-partout est comment des erreurs subtiles et confiantes atteignent les chemins critiques. Pour une grande équipe, une liste explicite de modules exclus ou réservés à la revue experte transforme le jugement individuel en une garantie organisationnelle. Apportez votre carte de risque de la base de code, votre politique actuelle (le cas échéant), et comment vous empêcheriez réellement le code généré d'atterrir dans un module restreint : contrôles de pipeline, règles de propriété, ou portes de revue. Dans les contextes de défense, régulés, et critiques pour la sécurité, certains modules devraient exclure complètement l'assistance IA. La réponse devrait échelonner l'effort de vérification au risque du code, jamais à quel point la sortie paraît confiante.

2. **Quelles sont nos vraies tendances d'échec de changement et d'échappement de défaut depuis que nous avons adopté des assistants, et les mesurons-nous ou devinons-nous ?** Les affirmations de productivité de fournisseur et les comptes de taux d'acceptation sont des métriques de vanité qui induisent en erreur, parce que le temps économisé à écrire du code peut être perdu de nouveau à le réviser et déboguer. Pour que la direction investisse sur preuve plutôt que battage, vous avez besoin de signaux de livraison et de qualité dans le temps : temps de cycle, taux d'échec de changement, taux d'échappement de défaut, et efficacité rapportée par les développeurs. Apportez tous les vrais chiffres que vous avez, et soyez honnête où vous n'en avez aucun. Le risque à surveiller est des équipes pressées d'accepter des suggestions dangereuses juste pour atteindre une métrique. La réponse devrait remplacer les comptes de suggestion par des mesures de résultat, et fixer des attentes que les gains sont réels mais inégaux, grands pour certaines tâches et négatifs pour d'autres.

3. **Si du code généré écho des données d'entraînement sous licence restrictive ou tire une dépendance risquée, qui l'attrape et quand ?** Le code généré peut ressembler à du matériel sous licence ou recommander des paquets abandonnés ou malveillants, et cette exposition atterrit dans votre produit que quelqu'un l'ait remarqué ou non. Pour les entreprises et l'administration publique, la provenance de licensing et le risque de chaîne d'approvisionnement portent un poids légal qu'un haussement d'épaules « l'IA l'a écrit » ne survit pas. Apportez votre scan de secret actuel, vos vérifications de licence, et suivi de provenance de dépendance, et identifiez où dans le pipeline chacun s'exécute. Discutez ce qui achemine le code questionnable vers la revue juridique et qui possède cette décision. Si des secrets peuvent être collés dans des outils externes ou des paquets non vérifiés peuvent fusionner sans contestation, fermez ces lacunes avant d'échelonner l'usage d'assistant à travers l'équipe.

4. **Comment gardons-nous les ingénieurs, spécialement les juniors, apprenant les fondamentaux plutôt que de sous-traiter leur compréhension à l'assistant ?** L'atrophie de compétence est un risque lent qui n'apparaît jamais dans la vélocité de ce trimestre, puis apparaît des années plus tard comme une équipe qui ne peut pas déboguer, concevoir, ou réviser sans un prompt. Pour une grande organisation, l'attraction concurrente est réelle : les assistants laissent les ingénieurs juniors livrer plus vite aujourd'hui, et la pression d'atteindre les cibles de livraison combat contre le travail plus lent de construire une expertise profonde. Apportez une preuve de comment vos gens grandissent réellement : quelle fraction de juniors peut expliquer le code qu'ils ont fusionné, combien de résolution de problème non assistée votre intégration exige encore, et si les revues attrapent la compréhension superficielle ou tamponnent simplement la sortie fonctionnelle. Faites tourner délibérément les gens à travers du travail qui construit la maîtrise, et traitez la sur-dépendance comme un risque de capacité, pas un échec personnel. Dans l'administration publique et les systèmes critiques de longue durée, la main-d'œuvre peut avoir besoin de construire et vérifier des systèmes pendant des décennies sans outils de fournisseur, donc un chemin de formation qui garantit des fondamentaux directs est une exigence de continuité, pas une gentillesse.

5. **Quels assistants sommes-nous réellement autorisés à utiliser étant donné où notre code source et données doivent rester, et comment empêchons-nous un secret d'atteindre un jour un prompt ?** Les contraintes de gestion de données décident l'outil avant que la productivité ne le fasse : un assistant qui diffuse votre source vers un service externe peut être disqualifié d'emblée, peu importe ses capacités. Pour une grande équipe la tension est entre la commodité du meilleur outil hébergé et l'exigence que le code propriétaire, les identifiants, et les données sensibles ne quittent jamais votre frontière. Apportez votre carte de classification de données, les options de déploiement que chaque outil candidat offre (hébergé, privé, sur site), et les contrôles concrets qui gardent les secrets hors des prompts : scan pré-commit, filtrage de prompt, et formation d'ingénieur. Décidez quels outils sont permis pour quelles classes de code, et rendez la frontière applicable plutôt que consultative. Dans les contextes régulés, de défense, et classifiés, un déploiement sur site ou isolé peut être la seule option légale, et envoyer la source à tout service externe doit être interdit et techniquement bloqué, pas simplement découragé.

6. **Comment transformons-nous des habitudes individuelles dispersées en normes cohérentes à l'échelle de l'organisation, et qui possède la politique à mesure que les outils évoluent ?** Quand des centaines de développeurs improvisent chacun leur propre approche, de petites habitudes se composent en résultats organisationnels, et la vérification incohérente est là où les défauts et l'exposition s'infiltrent. La considération concurrente est l'autonomie : les équipes ressentent les mandats centraux lourds, pourtant une mêlée générale produit une qualité inégale et aucune garantie partagée. Apportez votre directive actuelle (le cas échéant), une preuve de comment uniformément elle est suivie, et une proposition de bonnes valeurs par défaut cuites dans le pipeline pour que le chemin sûr soit le chemin facile. Nommez un propriétaire qui garde la politique à jour à mesure que les assistants changent tous les quelques mois, et une norme de divulgation pour que les relecteurs sachent quand l'assistance IA a façonné une contribution. Pour une entreprise ou organisme public, liez les normes à l'audit et responsabilité : une norme documentée et imposée qu'un auditeur peut inspecter bat une pratique populaire qui varie par équipe et disparaît quand une personne clé part.

## Regard sectoriel

**Jeune pousse.** Avec une poignée d'ingénieurs et aucune marge à gaspiller, appuyez-vous sur les assistants hébergés pour le passe-partout, les tests, et les cadriciels inconnus, et laissez-les accélérer le travail routinier. Gardez une règle non négociable : un humain qui comprend le changement révise chaque fusion, parce qu'une ligne subtilement fausse dans une base de code à cinq personnes n'a nulle part où se cacher et personne d'autre pour l'attraper. Ajoutez un scanner de secret et une vérification de licence tôt ; ils sont bon marché et préviennent des erreurs coûteuses que vous ne pouvez pas vous permettre de nettoyer plus tard.

**Petite entreprise.** Vous n'avez probablement pas de spécialiste de sécurité et avez un budget serré, donc préférez les assistants intégrés dans des outils que vous faites déjà confiance à une configuration sur mesure que vous devez maintenir. Cadrez le risque en termes simples : ne collez jamais de données client ou identifiants dans un prompt externe, et traitez le code généré touchant la facturation ou l'authentification comme un brouillon à vérifier, pas une réponse finie. Choisissez des fournisseurs dont vous pouvez réellement lire les termes de gestion de données et dont vous pouvez désactiver les fonctionnalités IA si elles se comportent mal.

**Grande entreprise.** Le problème est la cohérence et la sécurité à travers de nombreuses équipes : des normes partagées par niveau de risque, une revue et scan obligatoires dans le pipeline, et des métriques honnêtes de livraison et qualité plutôt que des comptes d'acceptation. Standardisez les choix d'outil et le modèle de déploiement pour que le code propriétaire reste à l'intérieur de votre frontière, budgétisez le coût de revue et correction que les assistants déplacent vers les relecteurs, et excluez ou conditionnez explicitement les modules à haut risque. Gérez l'assistance IA comme une capacité gouvernée avec un propriétaire, pas une dispersion d'habitudes individuelles.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la responsabilité publique façonnent chaque choix. Favorisez le déploiement sur site ou privé où le code source et les données sensibles ne peuvent pas quitter l'environnement, interdisez d'envoyer du code à des services externes, et exigez la divulgation des contributions assistées par IA pour que les décisions restent auditables. Mandatez des scans de sécurité et licensing sur tout code généré, excluez l'assistance IA des modules critiques pour la sécurité et classifiés, et gardez un chemin de formation qui garantit que la main-d'œuvre publique peut construire et vérifier des systèmes sans outils de fournisseur sur la longue vie des systèmes qu'elle possède.

## Exemples

**Jeune pousse.** Une jeune pousse SaaS à six ingénieurs a adopté des assistants de codage IA pour aller plus vite sur le travail routinier. Elle s'est appuyée dessus pour le passe-partout, les tests, et le code de cadriciel inconnu, mais a gardé une règle ferme qu'un humain qui comprenait le changement devait réviser chaque demande de tirage, et a ajouté un scanner de secret et une vérification de licence au pipeline. Pour le code de facturation et authentification, les ingénieurs ont traité la sortie IA comme un brouillon grossier à vérifier ligne par ligne plutôt qu'à faire confiance. Ils ont surveillé le temps de cycle et les défauts échappés plutôt que de compter les suggestions acceptées, et gardé les gains sans laisser la qualité glisser.

**Grande entreprise.** Une grande entreprise de commerce électronique a déployé des assistants de codage IA avec des garde-fous. Elle a interdit les secrets dans les prompts. Elle a exigé une revue humaine, avec le relecteur censé comprendre le code. Elle a ajouté un scan de sécurité dans le pipeline et choisi un déploiement privé pour que le code propriétaire ne quitte jamais son environnement. Elle a mesuré l'impact à travers le temps de cycle et le taux d'échec de changement plutôt que les comptes d'acceptation. Elle a trouvé des gains solides sur le passe-partout et les tests, mais a insisté sur une revue experte pour le code de paiement, où elle a traité la sortie IA comme non fiable.

**Gouvernement.** Une organisation logicielle de défense a permis l'assistance IA seulement à travers un outil sur site qui gardait le code classifié et sensible à l'intérieur de sa frontière. Elle a interdit d'envoyer la source à tout service externe. Elle a exigé la divulgation des contributions assistées par IA dans la revue de code et mandaté des scans de sécurité et licensing sur tout code généré. Elle a exclu entièrement l'assistance IA de certains modules critiques pour la sécurité. Les ingénieurs juniors ont suivi un chemin de formation qui assurait qu'ils apprenaient directement les fondamentaux, pour que la main-d'œuvre ne perde pas la capacité de construire et vérifier des systèmes sans assistance.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La motivation est une livraison plus rapide et moins de corvée, pour que votre talent d'ingénierie rare puisse se concentrer sur la conception, le jugement, et les problèmes difficiles. Le retour sur investissement se manifeste comme un temps de cycle réduit pour les tâches appropriées et une expérience développeur améliorée, mais seulement là où la vérification garde la qualité haute. Les affirmations de retour sur investissement naïves basées sur les comptes de suggestion sont trompeuses, et vous devriez les rejeter.

Le coût total de possession inclut le licensing d'outil, le déploiement sécurisé ou sur site, le scan de sécurité et licensing, et le coût souvent sous-estimé de réviser et corriger la sortie IA. Le coût de *ne pas* adopter est compétitif : les pairs peuvent livrer plus vite et attirer du talent qui attend des outils modernes. Le coût d'adopter avec négligence est l'érosion de qualité, les incidents de sécurité, et l'exposition légale. Faites valoir cela auprès de la direction avec un pilote qui mesure les vrais résultats de livraison et qualité, associé à un plan concret pour les normes, la vérification, et la protection de données.

## Anti-patterns et pièges

- **Acceptation en pilote automatique.** Commettre des suggestions sans les lire ou comprendre.
- **Métriques de vanité.** Juger le succès par le taux d'acceptation ou les lignes générées.
- **Secrets dans les prompts.** Coller des identifiants ou données sensibles dans des outils externes.
- **Faire confiance aux tests IA.** Accepter des tests générés qui verrouillent le comportement actuel, pas le comportement voulu.
- **Ignorer la provenance.** Négliger les risques de licence et de dépendance dans le code généré.
- **Atrophie de compétence.** Laisser les juniors sous-traiter la compréhension et ne jamais apprendre les fondamentaux.
- **Confiance uniforme.** Appliquer le même examen faible au code critique pour la sécurité qu'au passe-partout.

## Modèle de maturité

1. **Initier.** Les individus utilisent les assistants au coup par coup et réactivement ; aucune politique, aucune mesure ; les secrets et la propriété intellectuelle sont à risque, et le code généré fusionne avec quel que soit l'examen que chaque personne applique.
2. **Développer.** Une directive d'usage de base et des règles de données existent, et un certain scan de sécurité s'exécute, mais la pratique est incohérente à travers les équipes : la profondeur de vérification varie par personne, les affirmations de productivité sont anecdotiques, et le code à haut risque n'est pas de façon fiable conditionné.
3. **Standardiser.** Des normes par niveau de risque sont documentées et imposées à l'échelle de l'organisation : revue humaine obligatoire, scans de sécurité et licensing dans le pipeline, déploiement sécurisé ou sur site où requis, pratiques de divulgation, et une liste explicite de modules exclus ou réservés à la revue experte.
4. **Gérer.** La pratique est mesurée et contrôlée contre des références : le temps de cycle, taux d'échec de changement, et taux d'échappement de défaut sont suivis avant et après adoption, le coût de revue et correction est quantifié, les incidents de fuite de secret et d'exposition de licence sont comptés, et les décisions de feu vert ou non sur les outils et l'expansion reposent sur cette preuve plutôt que sur les affirmations de fournisseur.
5. **Orchestrer.** L'assistance IA s'améliore continuellement et est intégrée à travers l'organisation : la vérification est construite dans le pipeline comme le chemin par défaut, le développement de compétence est délibéré et suivi, la politique s'adapte à mesure que les outils changent tous les quelques mois, et l'organisation réévalue, remplace, et recadre routinièrement les assistants à mesure que la preuve et le paysage de risque changent.

## Pistes de réflexion

- Comment les exigences de vérification devraient-elles différer entre le passe-partout et le code critique pour la sécurité ?
- Quelles métriques de productivité reflètent réellement la valeur de l'assistance IA dans votre contexte ?
- Quand, si jamais, les contributions assistées par IA devraient-elles être divulguées ?
- Comment prévenez-vous l'érosion de compétence, spécialement pour les ingénieurs juniors ?
- Quelles contraintes de gestion de données gouvernent quels outils vous pouvez utiliser ?
- Comment gérez-vous le risque de licensing et provenance depuis le code généré ?

## Points clés à retenir

- L'ingénieur reste responsable ; la sortie IA est un brouillon non fiable à vérifier.
- Échelonnez la vérification au risque, et ne faites jamais confiance au code IA critique pour la sécurité sans revue experte.
- Mesurez les vrais résultats de livraison et qualité, pas les comptes de suggestion.
- Protégez contre les risques de sécurité, fuite de données, et licensing avec de la politique et de l'outillage.
- Fixez des normes claires et préservez délibérément la compétence d'ingénierie humaine.

## Références et lectures complémentaires

- Nicole Forsgren, Jez Humble, et Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (sur les attentes réalistes et la mesure).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (sur la compréhension contre les artefacts de code).
- Titus Winters, Tom Manshreck, et Hyrum Wright, *Software Engineering at Google*.
- GitClear et études industrielles associées sur les tendances de qualité de code assisté par IA.
