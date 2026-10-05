# 5.3 Accessibilité

## Vue d'ensemble et motivation

L'[accessibilité](https://fr.wikipedia.org/wiki/Accessibilit%C3%A9_du_web) (souvent abrégée « a11y ») est la pratique de construire du logiciel que les personnes handicapées peuvent percevoir, comprendre, naviguer, et utiliser. Cela inclut les personnes aveugles ou malvoyantes, sourdes ou malentendantes, ayant des déficiences motrices, ayant des différences cognitives ou d'apprentissage, et faisant face à des limites temporaires ou situationnelles telles qu'un bras cassé, un soleil éclatant, ou une pièce bruyante. Environ une personne sur cinq a un handicap, et tout le monde bénéficie de la conception accessible à un moment donné. Ce n'est pas un accommodement de niche. C'est un plancher de qualité.

Pour les grandes équipes, l'accessibilité doit être construite dans le système, pas laissée aux bonnes intentions individuelles. Quand de nombreuses équipes livrent dans un seul produit, un seul composant inaccessible (un champ de formulaire sans étiquette, un indicateur de statut uniquement en couleur, un piège au clavier dans une fenêtre modale) peut exclure les utilisateurs handicapés d'un parcours entier. Construire l'accessibilité dans les composants partagés, les jetons de conception, les pipelines de test, et les définitions de fini est la seule façon de la rendre fiable à l'échelle. La rétro-adapter après coup est coûteux et sujet aux erreurs. La concevoir dès le début est bon marché et durable.

Pour l'administration publique, l'accessibilité est une exigence légale et une obligation civique, pas un plus agréable. Les services publics doivent servir chaque membre du public, et les citoyens handicapés n'ont souvent aucun fournisseur alternatif : si le site web gouvernemental est inaccessible, ils ne peuvent pas obtenir leur prestation, licence, ou voter d'une autre façon. Les lois et normes à travers le monde rendent l'accessibilité obligatoire pour les organismes publics, et de plus en plus pour le secteur privé aussi. Ce chapitre traite l'accessibilité comme trois choses à la fois : un devoir légal, un devoir éthique, et simplement une bonne conception.

*Voir aussi :* chapitre 5.2 (conception UI et systèmes de conception), chapitre 5.6 (ingénierie frontend), et chapitre 5.1 (fondements UX).

## Principes clés

- L'accessibilité est un attribut de qualité de base, comme la sécurité et la performance, pas une fonctionnalité optionnelle.
- Les principes POUR : les interfaces doivent être Perceptibles, Opérables, Utilisables (compréhensibles), et Robustes.
- Le [HTML sémantique](https://fr.wikipedia.org/wiki/HTML_s%C3%A9mantique) d'abord ; utilisez [ARIA](https://fr.wikipedia.org/wiki/WAI-ARIA) seulement pour combler de vraies lacunes, jamais comme substitut aux éléments natifs.
- Tout ce qui est utilisable à la souris doit être utilisable au clavier seul.
- Ne transmettez pas d'information par la couleur, la forme, ou la position seules.
- Les outils automatisés n'attrapent qu'une fraction des problèmes ; le test manuel et avec [technologie d'assistance](https://fr.wikipedia.org/wiki/Technologie_d%27assistance) sont essentiels.
- La conception accessible est une meilleure conception pour tout le monde (l'« [effet de bordure abaissée](https://fr.wikipedia.org/wiki/Bordure_de_trottoir_abaiss%C3%A9e) », où des fonctionnalités construites pour les personnes handicapées bénéficient à tous les utilisateurs).
- Concevez et testez avec des personnes handicapées, pas seulement pour elles.

## Recommandations

### Concevoir et construire selon WCAG, en ciblant la norme actuelle

Les [Web Content Accessibility Guidelines](https://fr.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) sont la référence internationale. WCAG 2.1 et 2.2 sont organisées sous les quatre principes POUR, avec des critères de succès testables aux niveaux de conformité A, AA, et AAA. Ciblez le niveau AA comme votre base ; c'est ce que la plupart des lois référencent. WCAG 2.2 ajoute des critères pour la visibilité du focus, la taille de cible, et la réduction de la charge cognitive. WCAG 3.0 est un successeur émergent, structuré différemment et encore en développement. Gardez un œil dessus, mais construisez selon 2.2 AA aujourd'hui. Traitez les directives comme un plancher, pas un plafond : passer chaque critère ne garantit pas une expérience véritablement utilisable.

### Utiliser le HTML sémantique et l'ARIA correcte

Les éléments HTML natifs (boutons, liens, contrôles de formulaire, titres, listes, points de repère) viennent avec une sémantique d'accessibilité, un comportement clavier, et un soutien de technologie d'assistance intégrés. Utilisez-les d'abord. Recourez aux rôles, états, et propriétés ARIA (Accessible Rich Internet Applications) seulement pour décrire des widgets personnalisés que le HTML ne peut pas exprimer, et suivez les ARIA Authoring Practices. La première règle d'ARIA est simple : n'utilisez pas ARIA si un élément natif fera l'affaire. Une ARIA incorrecte est pire qu'aucune : elle induit activement en erreur les [lecteurs d'écran](https://fr.wikipedia.org/wiki/Lecteur_d%27%C3%A9cran). Donnez à la page une structure de titre logique, des étiquettes significatives, un texte alternatif pour les images, des sous-titres et transcriptions pour les médias, et un lien programmatique entre chaque étiquette et son contrôle.

### Garantir l'opérabilité au clavier et avec la technologie d'assistance

Chaque élément interactif doit être atteignable et opérable au clavier seul, dans un ordre logique, avec un indicateur de focus clairement visible. Évitez les pièges au clavier. Gérez le focus délibérément quand le contenu change : déplacez le focus vers une boîte de dialogue quand elle s'ouvre, retournez-le quand elle se ferme, et annoncez les mises à jour dynamiques à travers des régions actives. Testez avec de vraies technologies d'assistance, incluant des lecteurs d'écran sur ordinateur de bureau et mobile, la loupe d'écran, le contrôle vocal, et l'accès par contacteur. Et respectez les préférences utilisateur telles que mouvement réduit et contraste accru.

### Tester avec des outils automatisés, une revue manuelle, et de vrais utilisateurs

Les scanners d'accessibilité automatisés sont précieux, et ils devraient s'exécuter dans le pipeline à chaque changement. Mais les études montrent constamment qu'ils n'attrapent qu'une minorité de vrais problèmes, environ un tiers. Le reste a besoin de jugement humain : parcours au clavier, test avec lecteur d'écran, vérifications de contraste, et se demander si le contenu est réellement compréhensible. Le plus important de tout, incluez des personnes handicapées dans le test d'utilisabilité. Construisez des critères d'acceptation d'accessibilité dans la définition de fini, pour que les problèmes soient attrapés par récit plutôt que dans un audit avant lancement.

### Rendre l'accessibilité organisationnelle, pas héroïque

Intégrez l'accessibilité dans le système de conception pour que les composants soient livrés accessibles par défaut. Offrez de la formation pour que designers, ingénieurs, auteurs de contenu, et chefs de produit sachent chacun de quoi ils sont responsables. Établissez une norme d'accessibilité, un propriétaire ou centre d'excellence, et un processus de remédiation. Publiez une déclaration d'accessibilité et donnez aux utilisateurs une façon de rapporter des obstacles. Et approvisionnez de façon accessible : exigez que les fournisseurs et composants tiers soient conformes, et fournissent une preuve (telle qu'un rapport de conformité d'accessibilité).

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| Construire l'accessibilité dès le début | La moins chère, durable, meilleure pour tous | Exige une formation et une discipline préalables |
| Rétro-adapter / remédier plus tard | Diffère l'effort, débloque un lancement rapide | Bien plus coûteux, fragile, exposition légale dans l'intervalle |
| Test automatisé seulement | Rapide, bon marché, attrape les régressions en intégration continue | Manque environ deux tiers des problèmes ; fausse confiance |
| Test manuel + technologie d'assistance | Attrape de vrais obstacles d'utilisabilité | Plus lent, exige des testeurs et appareils qualifiés |
| Test avec des utilisateurs handicapés | Vérité terrain sur l'expérience réelle | Effort et coût de recrutement, doit être fait avec respect |

Le compromis central est la discipline préalable contre le coût différé. L'accessibilité construite dès le début est peu coûteuse et améliore la qualité pour tous ; l'accessibilité rétro-adaptée sous pression légale est coûteuse, incomplète, et stressante. À long terme il n'y a pas de vrai compromis contre la « vitesse » : le logiciel inaccessible ne fonctionne tout simplement pas pour un cinquième de vos utilisateurs. C'est un défaut, pas une économie.

## Questions à discuter avec votre équipe

1. **Nos régressions d'accessibilité échouent-elles notre construction comme le ferait un test cassé, et sinon, pourquoi pas ?** Les scanners automatisés n'attrapent qu'environ un tiers des problèmes, mais ceux qu'ils attrapent (étiquettes manquantes, échecs de contraste, contrôles sans étiquette) sont bon marché à attraper en intégration continue et coûteux à trouver dans un audit avant lancement. Traiter une régression comme un échec de construction est ce qui déplace l'accessibilité d'un effort individuel héroïque vers une propriété système fiable, ce qui est la seule chose qui fonctionne quand de nombreuses équipes livrent dans un seul produit. Décidez quels contrôles sont bloquants, lesquels sont consultatifs, et qui peut outrepasser un échec. Apportez vos résultats de scanner actuels et votre définition de fini à la réunion. Si les critères d'accessibilité ne sont pas écrits dans la définition de fini par récit, ils seront dépriorisés au moment où une date limite se resserre.

2. **Quelle est notre règle pour les widgets personnalisés, et qui révise l'ARIA avant qu'elle ne soit livrée ?** Les éléments HTML natifs viennent avec un comportement clavier et un soutien de technologie d'assistance gratuitement, et une ARIA incorrecte est pire qu'aucune parce qu'elle induit activement en erreur les lecteurs d'écran. Convenez que le HTML sémantique est la valeur par défaut et que tout widget personnalisé (un menu déroulant, sélecteur de date, ou fenêtre modale sur mesure) exige un parcours au clavier et avec lecteur d'écran avant fusion, suivant les ARIA Authoring Practices. Cela compte le plus pour les composants interactifs que de nombreuses équipes réutilisent, parce qu'une fenêtre modale cassée avec un piège au clavier peut exclure les utilisateurs handicapés d'un parcours entier. Apportez une liste de vos widgets personnalisés et demandez lesquels ont été testés avec un vrai lecteur d'écran. Ceux qui ne l'ont pas sont des passifs cachés dans le code partagé.

3. **Quelle est notre politique sur les surcouches d'accessibilité, et quelqu'un croit-il qu'elles sont une vraie correction ?** Les surcouches sont commercialisées comme un script d'une ligne qui rend un site conforme, et elles sont tentantes quand la pression légale arrive et qu'une date limite approche. Elles ne livrent pas une vraie conformité, elles peuvent empirer l'expérience pour les utilisateurs de technologie d'assistance, et pour l'administration publique elles laissent le devoir légal sous-jacent non satisfait. Décidez explicitement que vous investirez dans le balisage sémantique, le soutien clavier, et le test avec des personnes handicapées plutôt que d'acheter un widget qui masque le problème. Apportez le coût d'un abonnement de surcouche et comparez-le à construire l'accessibilité dans vos composants et pipeline une fois. Cadrer cela tôt prévient une décision d'approvisionnement paniquée plus tard qui dépense de l'argent et ne corrige rien.

4. **Les personnes handicapées font-elles partie de notre conception et test, ou concevons-nous toujours pour un utilisateur imaginé que nous avons inventé ?** Les scanners automatisés et même les audits experts vous disent si le balisage se conforme ; ils ne vous disent pas si un utilisateur aveugle peut réellement terminer votre paiement ou si une personne avec un handicap cognitif peut comprendre vos messages d'erreur. Impliquer des participants handicapés est la seule source de vérité terrain, et cela change ce que vous construisez, mais cela soulève de vraies questions sur comment vous recrutez équitablement, comment vous compensez les gens pour leur temps, et comment vous évitez de traiter un participant comme porte-parole pour chaque handicap. Apportez votre liste de recherche actuelle, vos pratiques de recrutement et de paiement, et un compte honnête de combien d'études l'année dernière ont inclus des participants handicapés. Pour une grande organisation, un panel récurrent avec une compensation équitable et une couverture à travers les besoins visuels, auditifs, moteurs, et cognitifs est ce qui transforme cela d'un geste ponctuel en un intrant fiable ; dans l'administration publique, impliquer le public que vous servez fait souvent partie de l'obligation légale et civique, pas une gentillesse optionnelle.

5. **Quand nous achetons ou intégrons un composant tiers, exigeons-nous une preuve d'accessibilité, et qui la vérifie ?** Une grande partie de ce qui est livré dans un grand produit n'est pas écrit en interne : un sélecteur de date d'une bibliothèque, un widget de paiement dans un cadre en ligne, un paquet de graphiques, un module SaaS entier. Un seul composant intégré inaccessible peut faire échouer un parcours entier peu importe la propreté de votre propre code, et une fois câblé, le remplacer est coûteux. Décidez que l'accessibilité est une exigence d'approvisionnement, que les fournisseurs doivent fournir un rapport de conformité d'accessibilité (un document tel qu'un VPAT qui indique comment un produit se mesure contre WCAG), et que quelqu'un de technique valide l'affirmation plutôt que de la classer. Apportez un inventaire de vos composants tiers et demandez lesquels ont une preuve de conformité actuelle et crédible. Dans les achats d'entreprise et gouvernementaux, écrivez la conformité WCAG 2.2 AA et un droit à la remédiation dans le contrat, parce qu'une promesse faite avant signature est bien moins chère à imposer qu'un obstacle découvert après mise en service.

6. **Quel est notre niveau de conformité cible, qui le possède, et comment le gardons-nous à jour à mesure que les normes évoluent ?** WCAG 2.2 AA est le plancher d'aujourd'hui et la plupart des lois le référencent, mais 2.2 a ajouté des critères que de nombreuses équipes n'ont pas adoptés, et WCAG 3.0 arrive avec une structure différente. Sans propriétaire nommé, la norme dérive : différentes équipes ciblent différentes versions, personne ne suit l'écart, et la conformité pourrit discrètement entre les audits. Décidez la version et le niveau exacts que vous construisez, qui a l'autorité de les relever, et comment les nouveaux critères atteignent le système de conception et la définition de fini. Apportez votre cible actuelle déclarée, la preuve d'où les équipes la satisfont réellement, et une courte feuille de route pour adopter les critères 2.2 que vous avez sautés. Pour une grande organisation ou publique, un propriétaire d'accessibilité ou centre d'excellence, une déclaration d'accessibilité publiée, et un plan documenté pour la prochaine version de norme sont ce qui vous permet de répondre à un régulateur ou un tribunal avec des preuves plutôt que de bonnes intentions.

## Regard sectoriel

**Jeune pousse.** La vitesse est de votre côté ici, parce que l'accessibilité est la moins chère quand la base de code est petite. Ajoutez un scanner automatisé à l'intégration continue et un parcours au clavier à votre liste de contrôle de demande de tirage dès le premier sprint, et appuyez-vous sur le HTML sémantique pour obtenir gratuitement le soutien clavier et lecteur d'écran. Sautez les surcouches et l'outillage lourd ; le gain est que quand l'équipe d'approvisionnement d'un client demande un rapport de conformité en milieu de vente, vous pouvez répondre en jours au lieu de vous précipiter.

**Petite entreprise.** Sans spécialiste d'accessibilité et avec un budget serré, achetez l'accessibilité plutôt que de la construire : choisissez une plateforme, un thème, ou une bibliothèque de composants qui se conforme déjà et le déclare, et préférez les fournisseurs qui publient une déclaration d'accessibilité. Couvrez vous-même les bases à haute valeur avec des outils gratuits, des vérifications clavier seul, un vérificateur de contraste, et des étiquettes claires sur chaque champ, parce que celles-ci attrapent les échecs qui excluent le plus souvent les clients. Traitez un flux automatisé faux ou inutilisable comme un client perdu, puisqu'une petite entreprise offre rarement un canal assisté de repli.

**Grande entreprise.** À l'échelle le travail est de faire de l'accessibilité une propriété système à travers de nombreuses équipes. Livrez des composants accessibles par défaut dans le système de conception, bloquez les régressions en intégration continue, et montez un propriétaire ou centre d'excellence avec un processus de remédiation et une formation pour les designers, ingénieurs, et auteurs de contenu. Suivez la conformité dans le temps comme une métrique, écrivez la conformité WCAG dans l'approvisionnement, et gérez les composants tiers comme un portefeuille pour qu'un seul widget intégré ne puisse pas faire échouer discrètement un parcours partagé.

**Gouvernement.** L'accessibilité est un mandat légal et un devoir civique, puisque les citoyens handicapés n'ont souvent aucun fournisseur alternatif pour une prestation, licence, ou vote. Construisez selon la norme que votre juridiction cite (par exemple la Section 508, l'EN 301 549, ou l'European Accessibility Act cartographié vers WCAG 2.2 AA), publiez une déclaration d'accessibilité avec une voie pour rapporter des obstacles, et testez avec le public handicapé que vous servez. Rejetez les surcouches comme substitut à une vraie conformité, et exigez que les fournisseurs fournissent une preuve crédible et un droit à la remédiation dans le contrat.

## Exemples

**Jeune pousse.** Une jeune pousse de trois personnes construisant un outil d'embauche a ajouté un scanner d'accessibilité à sa construction et un parcours au clavier rapide à sa liste de contrôle de demande de tirage dès le tout premier sprint, raisonnant qu'il était moins cher de rester accessible que de le corriger plus tard. Quand l'équipe d'approvisionnement d'un client de taille moyenne a demandé un rapport de conformité d'accessibilité pendant un cycle de vente, la jeune pousse utilisait déjà du HTML sémantique, avait étiqueté chaque champ, et avait un focus visible partout, donc ils ont répondu en jours au lieu de se précipiter. Cette préparation a remporté un contrat qu'un concurrent a perdu sur la même exigence.

**Grande entreprise.** Un grand détaillant a fait face à un recours collectif parce que des clients aveugles ne pouvaient pas terminer le paiement avec un lecteur d'écran. Au-delà du règlement et des frais légaux, l'entreprise a dû remédier sous un calendrier supervisé par un tribunal. Ensuite elle a reconstruit l'accessibilité dans son système de conception et pipeline d'intégration continue, ajouté le test avec lecteur d'écran à la définition de fini, et formé ses équipes. Le paiement accessible reconstruit a aussi amélioré la conversion et réduit les contacts de support pour tous : les corrections qui aidaient les utilisateurs de lecteur d'écran (étiquettes claires, messages d'erreur, ordre logique) aidaient tous les utilisateurs.

**Gouvernement.** Une agence de prestations publiques était légalement tenue de satisfaire WCAG 2.1 AA pour sa demande en ligne. Un test précoce avec des utilisateurs aveugles et malvoyants, des utilisateurs clavier seul, et des utilisateurs avec des handicaps cognitifs a révélé qu'un indicateur de « champ requis » uniquement en couleur, un sélecteur de date inaccessible, et des erreurs de validation non annoncées empêchaient les gens de terminer. Corriger cela, par le balisage sémantique, le focus visible, les annonces d'erreur par région active, et l'aide en [langage clair](https://fr.wikipedia.org/wiki/Langage_clair), a permis aux citoyens handicapés de postuler seuls pour la première fois. Cela a réduit la dépendance à l'aide en personne et abaissé le coût de service, tout en satisfaisant le mandat légal.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

L'argumentaire économique repose sur la portée de marché, le risque légal, le coût de service, et la qualité. Les personnes handicapées et leurs familles contrôlent un pouvoir d'achat significatif ; les exclure y renonce. Les services accessibles réduisent le besoin de canaux assistés coûteux (aide téléphonique et en personne), ce qui est une économie opérationnelle directe, spécialement pour l'administration publique. Et parce que les améliorations d'accessibilité (étiquettes claires, soutien clavier, contenu lisible, balisage robuste) aident tout le monde, elles élèvent typiquement la complétion et la satisfaction globales.

Sur le coût total de possession, le coût d'adoption est la formation, l'outillage, et la construction de l'accessibilité dans les composants et pipelines, tous modestes quand vous le faites dès le début. Le coût de ne pas adopter est sévère et vient de plusieurs directions : responsabilité légale (poursuites, règlements, remédiation ordonnée par tribunal, pénalités réglementaires), la dépense bien plus élevée de rétro-adapter sous pression de délai, le dommage réputationnel, et le coût continu de servir les utilisateurs exclus par des canaux plus coûteux. La rétro-adaptation coûte typiquement plusieurs fois ce que la conception dès le début aurait coûté.

Pour faire valoir cela auprès de la direction, menez avec l'obligation légale où elle s'applique (elle est non négociable pour l'administration publique et de plus en plus pour le secteur privé). Puis quantifiez la population adressable que vous excluez, le coût de canal assisté de cette exclusion, et les gains de « bordure abaissée » pour tous les utilisateurs. Positionnez l'accessibilité comme gestion de risque plus qualité, pas charité.

## Anti-patterns et pièges

- **Accessibilité comme case à cocher avant lancement** : un audit à la fin au lieu d'une pratique continue, garantissant un retravail coûteux de dernière minute.
- **« Soupe de div »** : un balisage non sémantique avec des gestionnaires de clic sur des éléments génériques, invisible pour la technologie d'assistance.
- **Mésusage d'ARIA** : boulonner ARIA sur du balisage cassé, ce qui induit en erreur les lecteurs d'écran plus qu'un balisage simple ne le ferait.
- **Information uniquement en couleur** : statut montré par la couleur seule, invisible pour les utilisateurs daltoniens.
- **Focus invisible** : retirer les contours de focus pour l'esthétique, échouant les utilisateurs au clavier.
- **Pièges au clavier** : fenêtres modales et widgets qui piègent ou perdent le focus.
- **Complaisance du scan automatisé** : passer un scanner et supposer que le produit est accessible.
- **Surcouches d'accessibilité** : des widgets tiers « correction d'une ligne » qui ne livrent pas une vraie conformité et peuvent empirer l'expérience.
- **Exclure les utilisateurs handicapés de la recherche** : concevoir pour un utilisateur handicapé imaginé au lieu de tester avec de vrais.

## Modèle de maturité

**Niveau 1 (Initier).** Aucune pratique d'accessibilité. Les problèmes sont découverts seulement quand un utilisateur se plaint ou qu'une poursuite arrive, et la réponse est réactive. Le balisage est non sémantique et non testé, et personne ne possède le problème.

**Niveau 2 (Développer).** La conscience existe et certaines équipes agissent dessus : un scanner automatisé dans une construction ici, un parcours au clavier là, un audit avant lancement avant une grande sortie. La pratique est basique et incohérente à travers les équipes, l'accessibilité est encore une liste de contrôle de fin d'étape, et elle est fréquemment dépriorisée sous pression de calendrier.

**Niveau 3 (Standardiser).** WCAG 2.2 AA est la norme documentée, imposée à l'échelle de l'organisation. L'accessibilité est construite dans le système de conception pour que les composants soient livrés accessibles par défaut, testée automatiquement et manuellement, et écrite dans la définition de fini. Les équipes sont formées, un propriétaire ou centre d'excellence existe, et un processus de remédiation est défini.

**Niveau 4 (Gérer).** L'accessibilité est mesurée et contrôlée avec des données contre des références. L'organisation suit les métriques de conformité dans le temps (taux de passage de scanner, le compte d'obstacles ouverts par sévérité, la couverture de test lecteur d'écran des parcours critiques, et le temps de remédiation), les rapporte par équipe sur un tableau de bord, et traite les régressions comme des échecs de construction plutôt que des avertissements consultatifs. Des cibles sont fixées contre une référence et le progrès est révisé, pour qu'une équipe qui glisse soit visible avant qu'un audit ne le trouve.

**Niveau 5 (Orchestrer).** L'accessibilité s'améliore continuellement et est intégrée à travers l'organisation. Les personnes handicapées font partie de la recherche et du test sur une base récurrente, et l'accessibilité est intégrée dans l'approvisionnement, les jetons de conception, et l'intégration continue. L'organisation s'adapte à mesure que les normes évoluent (adoptant de nouveaux critères WCAG et se préparant pour WCAG 3.0), et elle influence les fournisseurs et partenaires pour que toute la chaîne d'approvisionnement se conforme.

## Pistes de réflexion

- Comment empêchez-vous l'accessibilité d'être dépriorisée quand les délais se resserrent ?
- Quel est le bon mélange de test automatisé, manuel, et utilisateur pour votre profil de risque ?
- Comment la conformité d'accessibilité devrait-elle être écrite dans les contrats de fournisseurs et l'approvisionnement ?
- Comment gérez-vous l'écart entre la conformité WCAG et l'utilisabilité véritable pour les personnes handicapées ?
- Comment les équipes devraient-elles se préparer pour WCAG 3.0 tout en construisant selon 2.2 aujourd'hui ?
- Comment recrutez-vous et compensez-vous équitablement et respectueusement des participants handicapés pour la recherche ?

## Points clés à retenir

- L'accessibilité est un attribut de qualité de base et, pour l'administration publique, une exigence légale.
- Concevez selon WCAG 2.2 AA comme plancher ; utilisez les principes POUR comme modèle mental.
- Le HTML sémantique d'abord ; ARIA seulement pour combler de vraies lacunes, fait correctement.
- Les outils automatisés attrapent environ un tiers des problèmes ; le test manuel et avec technologie d'assistance sont essentiels.
- Testez avec des personnes handicapées, pas seulement pour elles.
- Construire l'accessibilité dès le début est bon marché et durable ; la rétro-adapter est coûteux et fragile.
- La conception accessible est une meilleure conception pour tout le monde : l'effet de bordure abaissée est réel.

## Références et lectures complémentaires

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* et documents Understanding/Techniques associés.
- W3C, *WAI-ARIA Authoring Practices Guide*.
- W3C Web Accessibility Initiative (WAI), matériaux introductifs et tutoriels.
- Laura Kalbag, *Accessibility for Everyone*.
- Sarah Horton et Whitney Quesenbery, *A Web for Everyone*.
- Regine Gilbert, *Inclusive Design for a Digital World*.
- Normes U.S. Section 508 et directives Section508.gov.
- Norme européenne EN 301 549 et l'European Accessibility Act.
- Directives d'accessibilité gouvernementales (par exemple le manuel d'accessibilité UK GDS).
- WebAIM, recherches et articles incluant les analyses d'accessibilité annuelles.
