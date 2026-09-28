# 5.6 Ingénierie frontend

## Vue d'ensemble et motivation

L'ingénierie frontend est la discipline de construire la couche orientée client du logiciel : le code qui s'exécute dans le navigateur ou sur l'appareil et transforme les conceptions, le contenu, et les données en une interface fonctionnelle. Elle s'étend aux choix de cadriciel et d'architecture, la stratégie de rendu, la gestion d'état, la performance, et la résilience à travers l'énorme diversité de navigateurs, appareils, et conditions de réseau du monde réel. Le frontend est là où tout le travail en amont (UX, conception, contenu, accessibilité, internationalisation) atteint l'utilisateur avec succès ou s'effondre.

Pour les grandes équipes, le frontend est particulièrement difficile, parce qu'il est exposé à un environnement que l'organisation ne contrôle pas. Les navigateurs, appareils, connexions, et paramètres des utilisateurs varient énormément, et la plateforme (le web) évolue continuellement. À l'échelle, les choix architecturaux se composent. Un cadriciel sélectionné aujourd'hui contraint l'embauche, la performance, et la maintenabilité pendant des années, et des milliers de petites décisions sur la taille de bundle et le rendu s'additionnent en l'expérience que les utilisateurs obtiennent réellement. Les normes partagées, les bibliothèques de composants, les budgets de performance, et les motifs architecturaux sont ce qui empêche de nombreuses équipes indépendantes de produire un ensemble lent, incohérent, et fragile.

La pertinence pour l'entreprise et l'administration publique est aiguë. Les entreprises maintiennent des applications de longue durée où la longévité et la maintenabilité du cadriciel comptent plus que la nouveauté, et où de nombreuses équipes doivent interopérer. Les gouvernements servent le public entier, incluant des personnes sur d'anciens appareils, des connexions lentes ou limitées, et des technologies d'assistance. Cela rend la performance, l'[amélioration progressive](https://fr.wikipedia.org/wiki/Am%C3%A9lioration_progressive), et la résilience non pas un poli optionnel mais la différence entre un service qui fonctionne pour tous et un qui exclut les moins avantagés. Un service gouvernemental qui ne fonctionne que sur le téléphone le plus récent avec une connexion rapide échoue à son mandat.

## Principes clés

- Le frontend s'exécute dans un environnement que vous ne contrôlez pas ; concevez pour la variabilité et l'échec.
- Choisissez une technologie ennuyeuse et durable pour les systèmes de longue durée ; optimisez pour la maintenabilité et l'embauche.
- La performance est une fonctionnalité et, pour de nombreux utilisateurs, un prérequis d'accès.
- Amélioration progressive : livrez d'abord une expérience de base fonctionnelle, puis superposez des améliorations.
- Envoyez moins de code ; le code le plus rapide et le plus fiable est le code que vous ne livrez pas.
- Assortissez la stratégie de rendu au type de contenu et au besoin utilisateur, pas à la mode.
- Résilience : l'interface devrait se dégrader gracieusement, pas se casser, quand les choses tournent mal.
- Les normes et fonctionnalités de plateforme survivent aux cadriciels ; appuyez-vous sur la plateforme.

## Recommandations

### Choisir les cadriciels pour la longévité et l'ajustement, pas le battage

Sélectionnez la technologie frontend selon le problème, l'équipe, l'horizon de maintenance, et le marché de l'embauche, pas selon ce qui est tendance. Pour les systèmes d'entreprise et gouvernementaux de longue durée, favorisez des technologies matures, bien soutenues, avec de grands bassins de talent, des pratiques de sortie stables, et des chemins de mise à niveau clairs. Pesez le coût total du renouvellement de cadriciel : les réécritures sont coûteuses et risquées. Préférez des approches qui s'appuient sur les [normes web](https://fr.wikipedia.org/wiki/Norme_web) pour que votre investissement survive au renouvellement de cadriciel, et isolez le code spécifique au cadriciel derrière des frontières pour que l'application ne soit pas l'otage du cycle de vie d'une bibliothèque.

### Assortir la stratégie de rendu au besoin

Les principales stratégies de rendu correspondent chacune à un contenu différent. Le rendu côté serveur (SSR) produit un premier affichage rapide et un bon [référencement naturel](https://fr.wikipedia.org/wiki/Optimisation_pour_les_moteurs_de_recherche) (SEO) et fonctionne sans JavaScript client, convenant aux pages riches en contenu et orientées public. La [génération de site statique](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_site_statique) (SSG) pré-rend au moment de la construction pour une vitesse et une capacité de mise en cache maximales, idéale pour le contenu qui change peu fréquemment. Le rendu côté client (CSR) convient aux expériences hautement interactives semblables à des applications derrière authentification. Le streaming et l'hydratation progressive envoient et activent la page incrémentalement pour que les utilisateurs voient et utilisent le contenu plus tôt. De nombreux grands systèmes mélangent celles-ci par route plutôt que d'en choisir une globalement. Gérez l'état délibérément : gardez l'état serveur, l'état URL, et l'état UI local distincts, et évitez de sur-centraliser tout dans un seul magasin global lourd.

### Traiter la performance comme une discipline budgétisée et mesurée

Adoptez des budgets de performance (limites explicites sur la taille de bundle, le nombre de requêtes, et les métriques clés) et imposez-les en intégration continue pour que les régressions échouent la construction. Suivez les Core Web Vitals (chargement, interactivité, et stabilité visuelle) en utilisant la surveillance d'utilisateur réel depuis de vrais appareils et réseaux, pas seulement des tests de laboratoire sur des machines rapides. Réduisez agressivement le JavaScript : découpez le code et [chargez paresseusement](https://fr.wikipedia.org/wiki/Chargement_paresseux) pour que les utilisateurs téléchargent seulement ce dont une vue donnée a besoin, différez le travail non critique, et préférez les capacités de plateforme aux bibliothèques lourdes. Optimisez les images et polices, mettez en cache efficacement, et mesurez sur des appareils bas de gamme et connexions lentes représentatifs.

### Construire avec amélioration progressive et résilience

Commencez à partir d'une base qui fonctionne avec du HTML sémantique et un JavaScript minimal ou absent, puis améliorez pour les clients capables. Cela garantit que la tâche centrale reste possible quand les scripts échouent à charger, qu'un appareil est ancien, ou qu'un réseau est capricieux, une réalité courante plutôt qu'un cas limite. Gérez les erreurs gracieusement : montrez des états utiles pour les conditions de chargement, vide, erreur, et hors ligne plutôt que des écrans blancs ou des roues qui tournent indéfiniment. Pour les services dont les gens dépendent, envisagez des techniques hors ligne d'abord pour que l'application reste utilisable à travers une connectivité intermittente, se synchronisant quand la connexion revient.

### Assurer la compatibilité multi-navigateur, multi-appareil, et d'assistance

Testez à travers les navigateurs, appareils, et technologies d'assistance que vos utilisateurs ont réellement, informé par une vraie analytique plutôt que par les propres machines de l'équipe. Utilisez l'amélioration progressive et la détection de fonctionnalité plutôt que de supposer que les fonctionnalités de plateforme les plus récentes sont disponibles partout. Construisez de façon [réactive](https://fr.wikipedia.org/wiki/Conception_web_adaptative) (voir le chapitre système de conception) pour qu'une seule base de code serve des téléphones aux ordinateurs de bureau. Intégrez l'accessibilité et l'internationalisation dans l'architecture frontend dès le début, pas comme des passes ultérieures.

### Gouverner le frontend comme une infrastructure partagée

Fournissez des bibliothèques de composants partagées, du linting, du formatage, et de l'outillage de construction pour que les équipes soient cohérentes et productives. Établissez des directives architecturales (comment structurer les applications, gérer l'état, et découper les bundles) et des budgets de performance imposés en intégration continue. Pour les très grands frontends, envisagez des architectures modulaires ou micro-frontend qui permettent aux équipes de déployer indépendamment, mais pesez soigneusement la complexité et le coût de performance ajoutés, car ils ne sont pas gratuits.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| Cadriciel populaire et mature | Grand bassin de talent, stable, soutenu | Peut porter un poids hérité ; plus lent à adopter les fonctionnalités les plus récentes |
| Cadriciel le plus récent | Fonctionnalités modernes, gains de performance | Risque de renouvellement, petit bassin de talent, longévité incertaine |
| SSR / SSG | Premier affichage rapide, SEO, fonctionne sans JS | Complexité serveur ou construction, défis de mise en cache |
| CSR (SPA) | Interactivité riche, sensation d'application | Premier chargement lent, dépendant du JS, coût SEO et résilience |
| JavaScript client lourd | Fonctionnalités riches | Mauvaise performance sur appareils bas de gamme, fragile |
| Amélioration progressive | Résiliente, inclusive, fonctionne partout | Plus d'effort de conception pour définir une base fonctionnelle |
| Micro-frontends | Déploiements d'équipe indépendants, échelle | Complexité, dépendances dupliquées, surcharge de performance |

Le compromis récurrent est la richesse et la commodité de développeur contre la portée, la performance, et la résilience. Les approches côté client lourdes sont agréables à construire et démontrer sur des machines rapides, mais elles excluent les utilisateurs sur des appareils et réseaux faibles. Pour les audiences d'entreprise et spécialement gouvernementales, inclinez la balance vers la performance, l'amélioration progressive, et la durabilité, parce que le coût d'exclure des utilisateurs est élevé et souvent non négociable.

## Questions à discuter avec votre équipe

1. **Comment isolons-nous le code spécifique au cadriciel pour que l'application ne soit pas l'otage du cycle de vie d'une bibliothèque ?** Pour les systèmes d'entreprise et gouvernementaux de longue durée, le renouvellement de cadriciel est la plus grande dépense évitable : une réécriture est coûteuse et risquée, et la bibliothèque tendance d'aujourd'hui contraint l'embauche et la maintenance pendant des années. S'appuyer sur les normes web et placer le code spécifique au cadriciel derrière des frontières claires signifie que votre logique métier et votre contenu survivent au prochain renouvellement de cadriciel. Décidez où se trouvent ces coutures et si un nouvel ingénieur pourrait distinguer le code de plateforme du code de cadriciel. Apportez une estimation de ce que votre dernière migration de cadriciel a coûté, ou ce que la prochaine coûtera. Si votre logique centrale est soudée aux API d'une bibliothèque, évaluez ce couplage avant de défendre le choix de cadriciel.

2. **Assortissons-nous la stratégie de rendu par route, ou forçons-nous une stratégie sur le produit entier ?** Le rendu côté serveur donne un premier affichage rapide et fonctionne sans JavaScript client pour le contenu public, la génération statique maximise la vitesse pour les pages qui changent peu fréquemment, et le rendu client convient aux surfaces interactives semblables à des applications derrière connexion. Forcer une stratégie globalement soit ralentit les pages publiques avec du JavaScript lourd soit sur-ingénierie une simple page de contenu. C'est une question de portée pour l'administration publique, où un service qui ne fonctionne qu'après le chargement d'un gros bundle exclut les utilisateurs sur d'anciens appareils et connexions lentes. Apportez vos routes clés et étiquetez chacune avec la stratégie qu'elle utilise réellement aujourd'hui. Si une page orientée public a besoin de JavaScript pour montrer son contenu, décidez si c'est un choix délibéré ou un accident.

3. **À quel point notre gestion d'état est-elle disciplinée, et sur-centralisons-nous tout dans un seul magasin global lourd ?** Garder l'état serveur, l'état URL, et l'état UI local distincts prévient le couplage et les tempêtes de re-rendu qui rendent les grands frontends lents et fragiles, pourtant la valeur par défaut tentante est de tout déverser dans un seul magasin global. Cela se compose à l'échelle, où de nombreuses équipes touchant un magasin partagé créent des dépendances cachées et une performance imprévisible. Convenez d'où appartient chaque type d'état et de ce qui n'appartient pas au magasin global. Apportez un composant qui re-rend plus qu'il ne devrait et tracez pourquoi. Si la réponse est un magasin central gonflé, décidez des frontières avant que le couplage ne se durcisse.

4. **Quels sont nos budgets de performance, échouent-ils la construction en intégration continue, et sont-ils mesurés sur les appareils que nos utilisateurs ont réellement ?** Un budget que personne n'impose est un vœu, et un budget mesuré seulement sur les ordinateurs portables rapides de l'équipe décrit un utilisateur qui n'existe pas. Pour une grande organisation, les budgets sont le seul mécanisme qui tient la taille de bundle et les Core Web Vitals en échec à mesure que des dizaines d'équipes ajoutent des fonctionnalités à une surface partagée, parce qu'aucun relecteur unique ne peut attraper chaque régression à l'œil. La pression concurrente est la vitesse de livraison : un échec de construction dur sur quelques kilo-octets semble obstructif jusqu'à ce que vous évaluiez l'abandon qu'il prévient. Apportez vos budgets actuels, les données de surveillance d'utilisateur réel depuis des appareils bas de gamme et connexions lentes, et la liste des sorties où une régression est passée à travers. Dans l'administration publique, où le mandat est de servir le public entier incluant les personnes sur d'anciens téléphones et données limitées, liez le budget au dixième le plus lent de vos utilisateurs plutôt qu'à la médiane, et rendez la porte d'intégration continue non négociable.

5. **Lesquels de nos services doivent continuer de fonctionner sans JavaScript client, et avons-nous réellement testé ce chemin ?** L'amélioration progressive est facile à revendiquer et facile à casser discrètement, parce que le chemin amélioré est celui que les développeurs utilisent chaque jour tandis que la base pourrit non testée. Décider cela délibérément compte à l'échelle, puisque de nombreuses équipes livrant vers une plateforme supposeront chacune que les scripts se chargent toujours à moins qu'une norme partagée ne dise le contraire, et une seule dépendance dure peut casser la tâche centrale pour quiconque dont le bundle échoue. Le compromis est réel : une base fonctionnelle sans JavaScript coûte de l'effort de conception et contraint comment vous construisez l'interactivité. Apportez vos parcours utilisateur critiques, un test qui charge chacun avec les scripts désactivés ou échoués, et une preuve de la fréquence à laquelle les scripts échouent réellement à charger sur le terrain. Pour un service public, un formulaire de prestation ou fiscal qui s'effondre quand un script expire n'est pas une expérience dégradée, c'est un citoyen qui ne peut pas remplir une obligation légale, donc traitez la base comme une exigence de conformité, pas une gentillesse.

6. **Quand les micro-frontends paient-ils réellement leur complexité, et qui décide avant qu'une équipe n'en réclame un ?** Les déploiements d'équipe indépendants sont attrayants, mais les micro-frontends portent la complexité de système distribué, des dépendances dupliquées, et une taxe de performance que les utilisateurs paient en chargements plus lents. Sans point de décision partagé, les équipes ambitieuses les adoptent pour la commodité organisationnelle bien avant que l'échelle ne justifie le coût, et le produit entier hérite de la surcharge. La considération concurrente est l'autonomie : les équipes qui livrent sur une base de code partagée peuvent se bloquer mutuellement, et à une échelle véritable ce couplage est son propre problème coûteux. Apportez le nombre d'équipes touchant la surface, la contention de déploiement que vous vivez réellement aujourd'hui, et une estimation mesurée de la duplication de charge utile qu'une division introduirait. Pour les plateformes d'entreprise et gouvernementales, où les décisions d'architecture lient de nombreuses équipes pendant des années et doivent survivre à l'audit et au transfert, exigez un seuil explicite et documenté et un propriétaire qui approuve le mouvement, plutôt que de laisser chaque équipe décider isolément.

## Regard sectoriel

**Jeune pousse.** La vitesse et la portée comptent toutes deux quand chaque inscription compte, donc résistez à l'application monopage lourde pour les pages publiques. Rendez côté serveur votre marketing et flux d'inscription pour qu'ils chargent vite sur les téléphones milieu de gamme et données inégales que vos premiers clients utilisent, et réservez l'interactivité côté client à l'application derrière connexion. Fixez un budget de taille de bundle simple en intégration continue pour qu'une dépendance négligente ne puisse pas gonfler discrètement la page, et appuyez-vous sur les normes web pour garder une petite base de code maintenable à mesure que vous embauchez.

**Petite entreprise.** Sans spécialiste frontend dédié et avec un budget serré, préférez un cadriciel grand public bien soutenu ou un constructeur de site hébergé plutôt que quoi que ce soit sur mesure, pour que vous embauchiez depuis un grand bassin de talent et achetiez la maintenance plutôt que de la doter. Cadrez le choix comme durabilité : l'option la moins chère est celle que vous n'êtes pas forcé de réécrire dans deux ans. Insistez sur des pages rapides et adaptées au mobile et un balisage accessible de série, puisqu'un paiement lent ou cassé vous coûte des clients que vous ne pouvez pas vous permettre de perdre.

**Grande entreprise.** Le problème est la cohérence à travers de nombreuses équipes : une bibliothèque de composants partagée, des motifs architecturaux convenus, du linting et de l'outillage de construction, et des budgets de performance imposés en intégration continue pour qu'aucune équipe ne puisse régresser silencieusement l'ensemble. Choisissez les cadriciels pour la longévité et l'embauche plutôt que la nouveauté, isolez le code spécifique au cadriciel derrière des frontières pour survivre à la prochaine migration, et assortissez la stratégie de rendu par surface. Gérez le frontend comme une infrastructure partagée avec surveillance d'utilisateur réel, gouvernance, et un enregistrement auditable de pourquoi chaque choix architectural a été fait.

**Gouvernement.** Vous servez le public entier, incluant des personnes sur d'anciens appareils, des connexions lentes ou limitées, et des technologies d'assistance, donc l'amélioration progressive et la performance sont des obligations, pas un poli. Faites d'une base fonctionnelle sans JavaScript une règle dure pour les services orientés citoyen, budgétisez les pages selon les utilisateurs les plus lents plutôt que la médiane, et gardez la tâche centrale complétable quand un script échoue. L'approvisionnement et la transparence s'appliquent : favorisez une technologie durable et penchée vers les normes qui évite le verrouillage à un seul fournisseur, documentez les exigences d'accessibilité et de performance dans les contrats, et soyez capable de montrer que le service fonctionne pour l'utilisateur le moins avantagé, pas seulement l'appareil de démonstration.

## Exemples

**Jeune pousse.** Une jeune pousse en phase d'amorçage était tentée de construire son site marketing et flux d'inscription comme une application monopage lourde, mais ses clients cibles étaient des acheteurs souvent sur des téléphones milieu de gamme avec des données mobiles inégales. Les deux fondateurs ont plutôt rendu côté serveur les pages publiques pour qu'elles chargent vite et fonctionnent avant qu'aucun JavaScript ne s'exécute, et réservé l'interactivité côté client à l'application derrière connexion. Ils ont fixé un budget de taille de bundle simple en intégration continue pour qu'une dépendance négligente ne puisse pas gonfler discrètement la page. Le premier chargement mince et rapide a amélioré mesurablement les inscriptions, et s'appuyer sur les normes web a gardé leur petite base de code facile à maintenir à mesure qu'ils embauchaient.

**Grande entreprise.** Une firme de services financiers a modernisé un ensemble tentaculaire d'applications internes et clients en standardisant sur un cadriciel mature, une bibliothèque de composants partagée, et des budgets de performance imposés en intégration continue. La stratégie de rendu était choisie par surface : pages rendues côté serveur et cachables pour le marketing et contenu public, et une application rendue côté client derrière connexion pour les tableaux de bord interactifs. Les budgets de bundle et la surveillance d'utilisateur réel attrapaient les régressions avant la sortie, gardant les temps de chargement rapides à travers les nombreuses équipes de la firme et réduisant le risque de renouvellement de cadriciel qui avait auparavant forcé des réécritures coûteuses.

**Gouvernement.** Une équipe de service numérique nationale a construit des services orientés citoyen avec l'amélioration progressive comme règle dure : chaque service fonctionne d'abord avec du HTML sémantique et un rendu serveur, et le JavaScript améliore seulement. Cela garantit que le service fonctionne sur d'anciens téléphones, des connexions rurales lentes, et des technologies d'assistance, des populations qu'un gouvernement ne peut pas exclure. Les budgets de performance gardent les pages légères et rapides sur les appareils bas de gamme, et la dégradation gracieuse signifie qu'un script échoué ne bloque jamais quelqu'un de terminer une demande de prestation. Le résultat est un service rapide, résilient, accessible, et utilisable par le public entier.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Les choix d'ingénierie frontend pilotent le revenu, la portée, et le coût. La performance est directement liée à la conversion, l'engagement, et la complétion de tâche. Les expériences plus rapides surpassent mesurablement les plus lentes, et pour les utilisateurs sur des appareils faibles, la performance est la ligne entre utiliser le service et abandonner. L'amélioration progressive et le soutien multi-appareil élargissent l'audience adressable, ce qui pour l'administration publique est un mandat et pour l'entreprise est une part de marché. Des choix de cadriciel et d'architecture solides réduisent la fréquence et le coût des réécritures, la plus grande dépense évitable en ingénierie frontend.

Sur le coût total de possession, les coûts d'adoption sont la discipline des budgets de performance et du test, l'effort de l'amélioration progressive, et l'investissement dans l'outillage partagé et les bibliothèques de composants. Le coût de ne pas adopter est payé en expériences lentes qui perdent des utilisateurs et du revenu, exclusion des utilisateurs bas de gamme et de technologie d'assistance (avec exposition légale dans l'administration publique), applications fragiles qui se cassent sur le terrain, et renouvellement de cadriciel et réécritures coûteux pilotés par la poursuite des tendances. Les problèmes frontend se manifestent comme un abandon diffus et une charge de support plutôt qu'une seule ligne budgétaire, donc ils sont faciles à sous-investir.

Pour faire valoir cela auprès de la direction, connectez les Core Web Vitals et les temps de chargement aux entonnoirs de conversion et complétion, quantifiez les utilisateurs exclus par les approches côté client lourdes, et évaluez le coût des réécritures passées ou imminentes contre la stabilité d'une architecture durable et penchée vers les normes. Cadrez les budgets de performance et l'amélioration progressive comme réduction de risque et expansion de portée.

## Anti-patterns et pièges

- **Poursuite de cadriciel** : réécrire sur la dernière bibliothèque, encourant du renouvellement sans bénéfice utilisateur.
- **Expériences uniquement JavaScript** : rien ne fonctionne jusqu'à ce qu'un gros bundle se charge et s'exécute, excluant de nombreux utilisateurs.
- **Tester seulement sur des appareils rapides** : les ordinateurs portables phares de l'équipe cachent la vraie expérience utilisateur.
- **Ignorer la taille de bundle** : une croissance de dépendance non bornée jusqu'à ce que les pages soient lentes partout.
- **Aucun budget de performance** : les régressions s'accumulent silencieusement sortie après sortie.
- **Échecs d'écran blanc** : aucun état de chargement, vide, erreur, ou hors ligne ; une requête échouée casse la page.
- **État global sur-centralisé** : tout dans un magasin, créant du couplage et des tempêtes de re-rendu.
- **Micro-frontends prématurés** : complexité de système distribué et charges utiles dupliquées sans l'échelle pour les justifier.
- **Négliger l'accessibilité et l'i18n dans l'architecture** : les boulonner plus tard à coût élevé.

## Modèle de maturité

**Niveau 1 (Initier).** Frontend au coup par coup construit par équipe sans normes partagées. Code côté client lourd, aucun budget de performance, testé seulement sur les propres appareils de l'équipe. Choix de cadriciel faits par préférence ou battage, et un script échoué peut laisser les utilisateurs fixer un écran blanc.

**Niveau 2 (Développer).** Certaines équipes adoptent de l'outillage partagé et une bibliothèque de composants, mais la pratique est incohérente à travers l'organisation. La performance est mesurée occasionnellement plutôt que budgétisée ou imposée. La stratégie de rendu est souvent uniforme indépendamment du type de contenu, et le test multi-appareil est limité et manuel.

**Niveau 3 (Standardiser).** Le cadriciel et l'architecture sont choisis délibérément pour la longévité, et les choix sont documentés et imposés à l'échelle de l'organisation. La stratégie de rendu est assortie par surface, l'amélioration progressive et la dégradation gracieuse sont la norme, et les bibliothèques de composants partagées, le linting, et l'outillage de construction s'appliquent à chaque équipe. Le multi-navigateur, l'accessibilité, et l'internationalisation sont construits plutôt que boulonnés.

**Niveau 4 (Gérer).** Le frontend est mesuré et contrôlé avec des données. Les budgets de performance sont imposés en intégration continue pour que les régressions échouent la construction, et les Core Web Vitals sont suivis avec la surveillance d'utilisateur réel depuis de vrais appareils bas de gamme et connexions lentes contre des références explicites. La taille de bundle, la couverture d'état d'erreur et hors ligne, et la part d'utilisateurs servis sur les connexions les plus lentes sont rapportées et révisées, pour que les décisions reposent sur la preuve plutôt que l'opinion.

**Niveau 5 (Orchestrer).** La performance, la résilience, et la portée s'améliorent continuellement et sont liées aux résultats d'affaires à travers l'organisation entière. Le frontend s'appuie sur les normes web pour la durabilité, isole les dépendances de cadriciel pour que les migrations soient bon marché, et fait évoluer l'architecture de façon adaptative à mesure que les appareils, la plateforme, et les données d'utilisateur réel changent. Le public entier et tous les appareils sont de première classe, et la pratique frontend est intégrée avec la conception, l'accessibilité, et la planification produit plutôt que traitée comme une préoccupation séparée.

## Pistes de réflexion

- Comment décidez-vous quand une migration de cadriciel vaut son coût et risque ?
- Quels Core Web Vitals et budgets de bundle devraient être des seuils d'échec de construction durs ?
- Où l'amélioration progressive est-elle essentielle, et où une application côté client est-elle acceptable ?
- Comment gardez-vous l'architecture frontend cohérente à travers de nombreuses équipes autonomes ?
- Quand les micro-frontends paient-ils réellement leur complexité ?
- Comment le test sur appareil réel et réseau lent devrait-il être construit dans le pipeline ?

## Points clés à retenir

- Le frontend s'exécute dans un environnement que vous ne contrôlez pas : concevez pour la variabilité et l'échec.
- Choisissez une technologie durable et bien soutenue pour les systèmes de longue durée ; appuyez-vous sur les normes web.
- Assortissez la stratégie de rendu (SSR, SSG, CSR, streaming) au contenu et au besoin, souvent mélangée par route.
- Traitez la performance comme une discipline budgétisée et mesurée imposée en intégration continue avec des données d'utilisateur réel.
- Construisez avec amélioration progressive pour que l'expérience centrale fonctionne partout.
- Livrez moins de JavaScript ; découpez le code, chargez paresseusement, et préférez les capacités de plateforme.
- Pour l'administration publique spécialement, la performance et la résilience sont des prérequis d'accès équitable.

## Références et lectures complémentaires

- Jeremy Keith, *Resilient Web Design*.
- Aaron Gustafson, *Adaptive Web Design* (amélioration progressive).
- Steve Souders, *High Performance Web Sites*.
- Ilya Grigorik, *High Performance Browser Networking*.
- Addy Osmani, écrits sur la performance, le découpage de code, et le coût du JavaScript.
- Google, *Web Vitals* et directives de performance web.dev.
- MDN Web Docs, références de plateforme web et d'amélioration progressive.
- Alex Russell, essais sur le coût du JavaScript et la diversité d'appareils.
- UK Government Digital Service, directives d'amélioration progressive et frontend.
- WHATWG HTML Living Standard et spécifications de plateforme web W3C.
