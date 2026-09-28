# 8.3 Conteneurs, orchestration, et cloud natif

## Vue d'ensemble et motivation

Un [conteneur](https://fr.wikipedia.org/wiki/Conteneur_%28informatique%29) empaquette une application avec ses dépendances en une unité unique, portable, et isolée. Il s'exécute de la même façon sur un ordinateur portable, dans un environnement de test, et en production. Les plateformes d'orchestration, plus notablement [Kubernetes](https://fr.wikipedia.org/wiki/Kubernetes), planifient et gèrent de grands nombres de conteneurs à travers des flottes de machines. Elles gèrent le placement, la mise à l'échelle, la santé, le réseautage, et la récupération. Le [cloud natif](https://fr.wikipedia.org/wiki/Cloud_natif) est le style architectural plus large construit sur ces fondations : des applications conçues comme des services faiblement couplés, indépendamment déployables, échelonnables horizontalement qui supposent une infrastructure dynamique et auto-guérissante.

Pour les grandes équipes, les conteneurs et l'orchestration résolvent un problème difficile. Vous avez besoin d'exécuter de nombreux services, construits par de nombreuses équipes, de façon fiable et efficace sur une infrastructure partagée. Les conteneurs donnent à chaque équipe un contrat d'empaquetage et d'exécution cohérent, ce qui retire la classe d'échecs « fonctionne sur ma machine ». L'orchestration cache les machines individuelles derrière un substrat commun, pour que les équipes déploient vers une plateforme plutôt que vers des serveurs. Cette standardisation est ce qui vous permet d'exploiter des centaines ou milliers de services sans que chaque équipe ne réinvente le déploiement, la mise à l'échelle, et la résilience.

Les adoptants d'entreprise et gouvernementaux gagnent la portabilité, la résilience, et un chemin loin du verrouillage. En retour, ils héritent d'une vraie complexité et de nouvelles responsabilités de sécurité. Une plateforme de conteneur est puissante précisément parce qu'elle est programmable et dynamique, ce qui signifie que vous devez la gouverner soigneusement. La provenance d'image, l'isolation multi-tenant, la politique réseau, et le coût deviennent tous des préoccupations de niveau plateforme. Les adoptants du secteur public ajoutent de plus en plus des exigences de souveraineté : le contrôle sur où les données résident et qui peut y accéder. Cela fait de la capacité d'exécuter des charges de travail cohérentes à travers des environnements choisis une capacité stratégique, pas seulement un détail technique.

## Principes clés

- Empaquetez les applications comme de petites images de conteneur à but unique et immuables.
- Pratiquez l'hygiène d'image : images de base minimales, versions épinglées, scannées pour vulnérabilités, et signées.
- Concevez les applications pour être sans état et échelonnables horizontalement où possible, externalisant l'état.
- Traitez le modèle d'état désiré de la plateforme d'orchestration comme la source de vérité et laissez-la s'auto-guérir.
- Imposez l'isolation et le moindre privilège entre tenants, charges de travail, et espaces de noms.
- Suivez les principes [douze facteurs](https://fr.wikipedia.org/wiki/Twelve-Factor_App), une méthodologie pour construire des applications jetables, à configuration externalisée, échelonnables horizontalement, et étendez-les pour les réalités des systèmes distribués.
- Rendez le coût une préoccupation d'ingénierie visible de première classe, pas une pensée après coup.
- Préférez les abstractions portables et basées sur normes pour préserver la flexibilité stratégique.

## Recommandations

### Pratiquer une hygiène d'image rigoureuse

L'image de conteneur est votre unité fondamentale de confiance et déploiement, donc traitez-la comme telle. Commencez avec des images de base minimales et fiables pour réduire la surface d'attaque. Épinglez les versions de dépendance et image de base pour la reproductibilité. Scannez chaque image pour les vulnérabilités connues dans le pipeline de construction, et bloquez celles avec des découvertes critiques. Signez les images et vérifiez les signatures au moment du déploiement, pour que seules les images approuvées et non modifiées s'exécutent. Gardez un registre interne sélectionné d'images de base durcies dont les équipes construisent. Cela répand automatiquement de bonnes valeurs par défaut de sécurité.

### Utiliser les motifs Kubernetes plutôt que les réinventer

Kubernetes récompense les équipes qui adoptent ses motifs établis, et il punit les équipes qui combattent son modèle. Utilisez des manifestes déclaratifs pour l'état désiré. Ajoutez des sondes de santé pour que la plateforme puisse détecter et remplacer les instances malsaines. Fixez des requêtes et limites de ressource pour que le planificateur puisse empaqueter les charges de travail en sécurité. Utilisez l'auto-échelonnement horizontal pour la demande élastique. Pour la logique opérationnelle qui doit s'exécuter continuellement, telle que gérer une base de données, faire tourner des certificats, ou réconcilier des ressources personnalisées, utilisez le motif opérateur, qui code la connaissance opérationnelle humaine dans un logiciel qui observe l'état et agit. Résistez à l'envie de construire une orchestration sur mesure par-dessus la plateforme. Préférez les constructions natives.

### Concevoir le multi-tenant délibérément

Quand de nombreuses équipes partagent un cluster, l'isolation est une exigence de sécurité et fiabilité, pas une gentillesse. Utilisez les espaces de noms comme frontières de tenance. Imposez des quotas de ressource pour qu'aucun tenant ne puisse affamer les autres. Appliquez des politiques réseau pour restreindre le trafic à ce qui est explicitement permis. Utilisez le [contrôle d'accès basé sur les rôles](https://fr.wikipedia.org/wiki/Contr%C3%B4le_d%27acc%C3%A8s_bas%C3%A9_sur_les_r%C3%B4les) (RBAC) pour limiter ce que chaque équipe peut faire. Pour les charges de travail avec des besoins d'isolation plus forts, envisagez des clusters séparés ou un bac à sable plus fort. Décidez tôt si votre modèle est le multi-tenant doux (équipes internes de confiance) ou le multi-tenant dur (charges de travail se méfiant mutuellement), parce que les deux exigent des contrôles très différents.

### Construire cloud natif, douze facteurs et au-delà

La méthodologie douze facteurs, avec ses dépendances explicites, configuration dans l'environnement, processus sans état, jetabilité, et ainsi de suite, reste une excellente référence pour les services qui prospèrent sur une plateforme dynamique. Étendez-la pour les réalités ajoutées des systèmes distribués. Concevez pour l'échec partiel. Rendez les opérations idempotentes et retentables. Exposez la santé et la télémétrie. Traitez l'observabilité comme une fonctionnalité intégrée plutôt qu'un ajout. Externalisez tout état vers des services de données gérés, pour que les instances d'application restent jetables et échelonnables horizontalement.

### Planifier les stratégies multi-cloud, hybrides, et souveraines pragmatiquement

La portabilité est précieuse, mais poursuivez-la les yeux ouverts. Standardisez sur des abstractions portables telles que les conteneurs, Kubernetes, et les API ouvertes, pour que les charges de travail puissent bouger si nécessaire. Mais évitez le piège de refuser tout service géré, ce qui échange une vraie productivité contre une portabilité hypothétique. Pour les exigences hybrides et souveraines, concevez pour que les mêmes charges de travail et pipelines puissent s'exécuter dans une région choisie, un centre de données privé, ou un cloud souverain qui satisfait les règles juridictionnelles et de résidence de données. Rendez les frontières de souveraineté et résidence explicites dans l'architecture et la politique.

### Rendre le coût visible avec FinOps

Dans les environnements cloud élastiques, le coût est une conséquence directe des décisions d'ingénierie, donc donnez aux ingénieurs de la visibilité et responsabilité. Étiquetez les ressources pour l'allocation de coût. Attribuez la dépense aux équipes et services. Montrez les données de coût aux côtés des métriques de performance. Dimensionnez correctement les charges de travail, utilisez l'auto-échelonnement pour correspondre à la demande, et récupérez les ressources inactives. Établissez une pratique FinOps qui rassemble l'ingénierie, la finance, et le produit, pour que la dépense cloud devienne une responsabilité partagée et continue plutôt qu'une surprise trimestrielle.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients | Meilleur ajustement |
|---|---|---|---|
| Kubernetes | Puissant, portable, énorme écosystème | Complexité raide ; fardeau opérationnel | De nombreux services à l'échelle |
| Service de conteneur géré | Moins de fardeau d'opérations ; démarrage plus rapide | Un certain verrouillage ; moins de contrôle | Équipes voulant la simplicité |
| Cluster partagé unique | Usage de ressource efficace | Isolation plus difficile ; rayon d'explosion | Tenants internes de confiance |
| Cluster par tenant | Isolation forte | Coût et surcharge plus élevés | Charges de travail méfiantes ou régulées |
| Portabilité multi-cloud | Flexibilité ; évite le verrouillage | Services au plus petit dénominateur commun | Atténuation de risque stratégique |
| Services gérés profonds mono-cloud | Productivité maximale | Dépendance de fournisseur | Équipes axées vitesse |

Le compromis global est la capacité contre la complexité. Les architectures Kubernetes et cloud natif livrent de l'élasticité, résilience, et vélocité. Mais elles imposent un fardeau opérationnel et cognitif substantiel que les petites équipes sous-estiment routinièrement. De la même façon, poursuivre la portabilité [multi-cloud](https://fr.wikipedia.org/wiki/Cloud_hybride) complète échange la productivité contre l'optionalité. La bonne réponse dépend de l'échelle et du risque. Les grandes organisations avec de nombreuses équipes et de forts besoins de gouvernance justifient habituellement l'investissement. Les efforts plus petits sont souvent mieux servis par des services gérés qui cachent la complexité.

## Questions à discuter avec votre équipe

1. **Signez-vous les images et vérifiez-vous les signatures au moment du déploiement, et une vulnérabilité critique bloque-t-elle réellement la construction ?** L'image est votre unité de confiance, donc la chaîne d'approvisionnement autour d'elle mérite des portes dures, pas des avertissements. Décidez si seules les images signées et vérifiées peuvent s'exécuter, si le scan bloque les découvertes critiques ou les journalise simplement, et qui maintient le registre sélectionné d'images de base durcies dont les équipes construisent. Pour les charges de travail d'entreprise et gouvernementales c'est fréquemment une exigence de conformité, et c'est aussi votre meilleure défense contre une dépendance empoisonnée atteignant la production. Apportez l'état actuel : quelle fraction des images en cours d'exécution vient de votre base durcie, combien portent des CVE critiques non corrigées, et si une image non signée peut actuellement être planifiée. Si une découverte critique n'arrête pas un déploiement, votre scanner est de la décoration.

2. **Comment les requêtes, limites, et quotas de ressource empêchent-ils une charge de travail d'affamer ses voisins, sans laisser une capacité coûteuse inactive ?** Sur un cluster partagé, une charge de travail sans limites peut planter ou étrangler tout ce qui l'entoure, et des quotas fixés trop généreusement gaspillent les gains d'utilisation qui justifient la plateforme. Décidez des valeurs par défaut sensées, qui les règle, et comment vous attrapez les charges de travail sans requêtes fixées du tout. À l'échelle c'est à la fois un contrôle de fiabilité et un contrôle de coût, parce que le dimensionnement correct est là où vit une grande partie de l'économie FinOps. Apportez des données : l'utilisation de cluster actuelle, à quelle fréquence les charges de travail sont expulsées ou étranglées, et quels espaces de noms n'ont pas de quotas. L'objectif est un empaquetage dense et sûr, donc traitez les limites manquantes comme un défaut que la plateforme rejette.

3. **Quel état est autorisé à vivre à l'intérieur d'un conteneur, et où va tout le reste ?** La résilience cloud native dépend d'instances jetables que la plateforme peut replanifier à volonté, et cela ne tient que si l'état important vit dans des services de données gérés plutôt que sur le disque local du conteneur. Décidez la règle explicitement, parce que l'état stocké dans un conteneur par accident devient une perte de données à la prochaine replanification. Pour les équipes migrant d'anciennes applications c'est souvent la partie la plus difficile, puisque les services hérités supposent un système de fichiers local stable. Apportez un inventaire : quels services écrivent un état local, lesquels comptent sur des sessions collantes ou affinité de nœud, et ce qu'il faudrait pour externaliser chacun. Jusqu'à ce que l'état soit externe, vous avez des conteneurs qui paraissent élastiques mais ne peuvent pas réellement être déplacés.

4. **Quand de nombreuses équipes partagent un cluster, votre modèle d'isolation est-il délibérément choisi comme multi-tenant doux ou dur, et les contrôles correspondent-ils à ce choix ?** Les espaces de noms séparent les équipes internes de confiance, mais ils ne contiennent pas une charge de travail activement hostile ou compromise, et traiter la tenance douce comme si elle était dure est un incident de sécurité qui attend d'arriver. Décidez par charge de travail si les tenants ont simplement besoin d'un partage équitable ou doivent être supposés se méfier les uns des autres, puis assortissez les contrôles : espaces de noms, quotas, politiques réseau, et RBAC pour le cas doux, clusters séparés ou bac à sable plus fort pour le cas dur. Pour une grande organisation cette décision pilote directement le coût, parce qu'un cluster par tenant est bien plus coûteux que des espaces de noms partagés, donc vous voulez dépenser le budget d'isolation seulement là où le modèle de menace l'exige. Apportez l'inventaire de tenant : quelles charges de travail partagent un cluster aujourd'hui, lesquelles gèrent du trafic régulé ou orienté externe, et où la politique réseau est encore permettre-par-défaut. Dans les contextes d'entreprise et gouvernementaux, mélanger des charges de travail méfiantes sous tenance douce est exactement la découverte qu'un auditeur signalera, donc nommez la frontière avant lui.

5. **Combien payez-vous pour la portabilité multi-cloud, et l'utiliserez-vous jamais réellement ?** Standardiser sur les conteneurs, Kubernetes, et les API ouvertes garde les charges de travail mobiles, mais refuser tout service géré pour préserver cette option échange une vraie productivité quotidienne contre une portabilité que l'organisation pourrait ne jamais exercer. Décidez où la portabilité est une vraie exigence, telle qu'une obligation de souveraineté ou de sortie que vous avez signée, contre où c'est une couverture de confort qui ralentit chaque équipe. La considération concurrente est la vitesse : les services gérés profonds livrent des fonctionnalités plus vite, et l'architecture au plus petit dénominateur commun est une taxe permanente sur chaque équipe. Apportez la preuve : quels services gérés vous avez évités et ce que cela a coûté en temps d'ingénierie, si vous avez déjà déplacé une charge de travail entre fournisseurs, et ce que vos contrats obligent réellement. Pour les adoptants gouvernementaux et régulés, les règles de résidence de données et cloud souverain peuvent rendre la portabilité non négociable, donc concevez pour que les mêmes manifestes et pipelines s'exécutent dans une région souveraine et une enclave privée, mais soyez honnête que c'est un coût de conformité plutôt qu'une assurance gratuite.

6. **Chaque équipe peut-elle voir ce qu'elle dépense, et quelqu'un possède-t-il la facture avant qu'elle ne devienne une surprise ?** Dans une plateforme élastique, le coût est une sortie directe des décisions d'ingénierie, pourtant sans étiquettes d'allocation de coût et tableaux de bord visibles la dépense s'accumule dans un pool partagé dont personne ne se sent responsable jusqu'à ce que la finance escalade. Décidez comment vous attribuez le coût aux équipes et services, qui le révise, et si les ingénieurs voient le coût à côté des métriques de performance ou en entendent parler seulement une fois par trimestre. La tension est entre la responsabilité et la friction : poussez le coût trop fort et chaque décision devient une négociation budgétaire, l'ignorez et les charges de travail inactives et surdimensionnées se composent discrètement. Apportez les chiffres : dépense actuelle par équipe, combien de capacité est inactive ou surdimensionnée, et à quelle vitesse une charge de travail galopante serait remarquée. Pour les budgets d'entreprise et gouvernementaux, la dépense cloud non attribuée est à la fois une défaillance de gouvernance et un vrai risque financier, donc montez une pratique FinOps qui met l'ingénierie, la finance, et le produit dans la même conversation plutôt que de réconcilier après coup.

## Regard sectoriel

**Jeune pousse.** Recourez à un service de conteneur géré plutôt qu'un cluster Kubernetes auto-hébergé : avec quelques services et aucun ingénieur de plateforme, les plans de contrôle sont une distraction que vous ne pouvez pas vous permettre. Empaquetez de petites images depuis une base minimale, épinglez les versions, ajoutez un scan de vulnérabilité à la construction, et poussez tout état dans une base de données gérée pour que les instances restent jetables. Sautez les espaces de noms, opérateurs, et la portabilité multi-cloud jusqu'à ce que vous ayez réellement les services et les gens pour les justifier.

**Petite entreprise.** Sans spécialiste de plateforme dédié et avec un budget serré, appuyez-vous fortement sur les services gérés et laissez le fournisseur exécuter l'orchestration que vous devriez autrement doter. Traitez les bases de conteneur comme votre plancher de sécurité : images minimales, épinglage de version, et un scan dans le pipeline donnent la plupart de la protection pour peu d'effort. Favorisez acheter une plateforme soutenue plutôt que d'en construire une, et gardez assez de portabilité, conteneurs standard et API ouvertes, pour ne pas être piégé si les prix ou termes changent.

**Grande entreprise.** La tâche est la gouvernance de plateforme à travers de nombreuses équipes : une équipe de plateforme centrale fournissant des images de base durcies, des portes de signature et scan, une tenance d'espace de noms avec quotas, politique réseau, et RBAC, plus des étiquettes d'allocation de coût et un tableau de bord FinOps. Standardisez le contrat de déploiement pour que des centaines de services opèrent de la même façon, et gérez la sécurité, multi-tenance, et coût centralement tandis que les équipes se servent elles-mêmes du déploiement. Financez correctement l'équipe de plateforme, parce qu'une plateforme sous-dotée devient le goulot d'étranglement que toute l'organisation attend.

**Gouvernement.** La souveraineté, la résidence de données, et la responsabilité publique façonnent l'architecture. Exécutez les charges de travail sur des conteneurs standard et Kubernetes pour que les mêmes pipelines s'exécutent dans une région souveraine et une enclave sur site accréditée, et codez les frontières de résidence et d'accès comme politique plutôt que convention. Tirez les images d'un registre interne durci, appliquez le multi-tenant dur aux données les plus sensibles, et gardez la portabilité qui vous donne la résilience et le levier de négociation, puisque les règles d'approvisionnement interdisent souvent le verrouillage à un seul fournisseur.

## Exemples

**Jeune pousse.** Une jeune pousse de six personnes empaquette ses deux services comme de petites images de conteneur construites depuis une base minimale, et les exécute sur un service de conteneur géré plutôt qu'un cluster Kubernetes auto-hébergé, pour que personne n'ait à surveiller les plans de contrôle. Ils épinglent les versions d'image de base et ajoutent un scan de vulnérabilité à leur construction, mais sautent délibérément les fonctionnalités d'orchestration plus lourdes jusqu'à ce qu'ils aient réellement plus qu'une poignée de services. L'état vit dans une base de données Postgres gérée, ce qui garde les conteneurs jetables et laisse la plateforme les redémarrer ou échelonner sans aucune perte de données.

**Grande entreprise.** Une entreprise de télécommunications exécute plusieurs centaines de [microservices](https://fr.wikipedia.org/wiki/Microservices) sur des clusters Kubernetes partagés. Une équipe de plateforme fournit des images de base durcies, impose la signature d'image et les portes de vulnérabilité, et isole les unités d'affaires dans des espaces de noms avec quotas, politiques réseau, et RBAC. Des étiquettes d'allocation de coût et un tableau de bord FinOps attribuent la dépense à chaque ligne de produit, et l'auto-échelonnement dimensionne correctement la capacité à la demande. Les équipes produit déploient des dizaines de fois par jour vers une plateforme cohérente sans gérer de serveurs. L'entreprise garde le contrôle central sur la sécurité et le coût.

**Gouvernement.** Un service de santé national doit garder les données citoyennes à l'intérieur des frontières nationales et sous contrôle juridique national. Il exécute ses charges de travail sur une région cloud souveraine utilisant des conteneurs standard et Kubernetes, pour que les mêmes pipelines et manifestes s'exécutent aussi dans un environnement accrédité sur site pour les données les plus sensibles. Les frontières de résidence de données et d'accès sont codées comme politique, les images sont tirées d'un registre interne durci, et le multi-tenant dur isole les charges de travail sensibles. La portabilité à travers la région souveraine et l'enclave privée donne au service résilience et levier de négociation sans sacrifier la conformité.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur investissement des conteneurs et de l'orchestration vient d'une utilisation de ressource plus élevée, de déploiements plus rapides et fiables, d'une mise à l'échelle élastique qui assortit la dépense à la demande, et d'une résilience améliorée à travers l'auto-guérison. Standardiser sur une plateforme commune réduit l'effort dupliqué à travers les équipes et accélère l'intégration, parce que chaque service suit le même contrat de déploiement et opérationnel.

L'analyse de coût total de possession doit être honnête sur le fardeau opérationnel. Les coûts d'adoption incluent le personnel d'ingénierie de plateforme, la formation, l'outillage de sécurité pour les images et clusters, et l'effort continu d'exploiter la plateforme elle-même. Le coût de ne pas adopter inclut un déploiement sur mesure incohérent à travers les équipes, une mauvaise utilisation d'infrastructure coûteuse, une mise à l'échelle manuelle fragile, et une difficulté à satisfaire les exigences de résilience et souveraineté. Pour la direction, l'argument repose sur l'échelle. En dessous d'un certain nombre de services la complexité peut ne pas payer, et un service géré est plus sage. Mais à l'échelle entreprise et gouvernementale, une plateforme cloud native gouvernée est typiquement la fondation la plus rentable et résiliente, à condition que vous financiez correctement l'équipe de plateforme pour l'exploiter.

## Anti-patterns et pièges

- **Images grasses et non scannées.** Des images gonflées construites depuis des bases non fiables portent des vulnérabilités inutiles et ralentissent tout.
- **Kubernetes pour tout.** Adopter un orchestrateur complexe pour une poignée de services simples achète de la complexité sans gain.
- **Ignorer les limites de ressource.** Sans requêtes et limites, une charge de travail peut affamer ou planter ses voisins.
- **Tenance douce pour charges de travail hostiles.** Compter sur les espaces de noms seuls pour isoler des tenants méfiants est un incident de sécurité qui attend d'arriver.
- **Conteneurs avec état par accident.** Stocker un état important à l'intérieur de conteneurs jetables mène à la perte de données à la replanification.
- **Cécité de coût.** Traiter la dépense cloud comme une surcharge fixe plutôt qu'une sortie d'ingénierie mène à des factures galopantes.
- **Théâtre de portabilité.** Refuser tous les services gérés pour préserver une portabilité que l'organisation n'utilisera jamais réellement.

## Modèle de maturité

**Niveau 1 (Initier).** Les conteneurs sont utilisés au coup par coup, si du tout. Les images sont construites à la main et non scannées, le déploiement est manuel et réactif, et il n'y a pas de plateforme partagée, visibilité de coût, ou modèle d'isolation.

**Niveau 2 (Développer).** Les équipes conteneurisent les applications et adoptent un orchestrateur, mais les pratiques varient entre groupes. Le scan d'image, les limites de ressource, et la signature sont incohérents, et le coût et le multi-tenant ne sont pas gouvernés systématiquement.

**Niveau 3 (Standardiser).** Une plateforme standardisée est documentée et imposée à travers l'organisation : images de base durcies, portes de signature et scan, tenance basée sur espace de noms avec quotas et politique réseau, RBAC, et allocation de coût. Les motifs cloud natif et douze facteurs sont la norme attendue plutôt qu'un choix local.

**Niveau 4 (Gérer).** La plateforme est mesurée et contrôlée contre des références. Vous suivez l'utilisation de cluster, la part d'images en cours d'exécution construites depuis la base durcie, les vulnérabilités critiques non corrigées, la fréquence de déploiement et taux d'échec de changement, les taux d'expulsion et étranglement, et le coût par équipe et service contre le budget. Les portes sont imposées sur cette preuve : les limites de ressource manquantes et images non signées sont rejetées automatiquement, et la dérive du standard déclenche une action plutôt qu'un avertissement.

**Niveau 5 (Orchestrer).** La plateforme est en libre-service et auto-guérissante, intégrée à travers l'organisation et adaptative. FinOps dimensionne correctement et récupère continuellement la capacité, l'architecture portable soutient les exigences hybrides et souveraines, et la plateforme s'améliore continuellement depuis l'usage mesuré, retirant et remplaçant des composants à mesure que les charges de travail, le coût, et le paysage de risque changent.

## Pistes de réflexion

- À quelle échelle adopter Kubernetes arrête-t-il d'être de la complexité pour elle-même et commence-t-il à payer ?
- Où se trouve la bonne frontière entre le multi-tenant doux et dur pour vos charges de travail ?
- Combien devriez-vous investir dans la portabilité multi-cloud contre la productivité des services gérés profonds ?
- Comment donnez-vous aux ingénieurs une vraie responsabilité de coût sans transformer chaque décision en négociation budgétaire ?
- Quel est votre modèle de gouvernance pour les images de base, et qui maintient le registre durci ?
- Comment les exigences de souveraineté et résidence de données façonnent-elles votre architecture de plateforme ?

## Points clés à retenir

- Les conteneurs standardisent l'empaquetage et l'exécution ; l'orchestration standardise l'opération à l'échelle.
- L'hygiène d'image, signifiant des images minimales, épinglées, scannées, signées, est une sécurité fondamentale.
- Utilisez les motifs et opérateurs Kubernetes natifs plutôt que de construire une orchestration sur mesure.
- Choisissez un modèle multi-tenant délibérément basé sur combien les charges de travail se font confiance mutuellement.
- Suivez les douze facteurs et étendez-les pour les réalités de système distribué comme l'échec partiel et l'observabilité.
- Traitez le coût comme une sortie d'ingénierie et gérez-le continuellement à travers FinOps.

## Références et lectures complémentaires

- Adam Wiggins, *The Twelve-Factor App* (méthodologie).
- Brendan Burns, Joe Beda, et Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam et Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment et Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), définition et paysage cloud natif.
