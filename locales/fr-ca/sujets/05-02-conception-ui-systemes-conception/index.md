# 5.2 Conception UI et systèmes de conception

## Vue d'ensemble et motivation

La [conception d'interface utilisateur](https://fr.wikipedia.org/wiki/Conception_d%27interface_utilisateur) (UI) est l'art de façonner ce que les gens voient et touchent : mise en page, [typographie](https://fr.wikipedia.org/wiki/Typographie), couleur, espacement, contrôles, et états. Un [système de conception](https://fr.wikipedia.org/wiki/Design_system) prend cet art et le transforme en un actif partagé, réutilisable, et gouverné : un ensemble documenté de principes, composants, motifs, et jetons dans lequel chaque équipe puise, pour que le produit entier paraisse et se comporte comme un seul. La conception UI décide comment un écran devrait paraître. Un système de conception décide comment dix mille écrans à travers de nombreuses équipes restent cohérents.

Pour une grande organisation, le système de conception est l'investissement à plus haut levier en qualité UI et vitesse de livraison. Sans lui, chaque équipe réinvente des boutons, formulaires, fenêtres modales, et gestion d'erreur, chacun légèrement différent, chacun maintenu séparément, chacun cassé séparément. Les utilisateurs paient cela en confusion et méfiance ; l'entreprise le paie en effort dupliqué et qualité inégale. Un système de conception transforme les décisions de conception ponctuelles en capital réutilisable : résolvez l'[accessibilité](https://fr.wikipedia.org/wiki/Accessibilit%C3%A9_du_web), la [réactivité](https://fr.wikipedia.org/wiki/Conception_web_adaptative), et l'image de marque une fois dans un composant, et chaque équipe hérite du résultat.

L'entreprise et l'administration publique ajoutent deux pressions spécifiques. Premièrement, l'échelle : des centaines d'applications, beaucoup construites par des fournisseurs ou acquises par fusions, doivent toutes ressembler à une seule organisation. Deuxièmement, la longévité et le changement : les marques sont rafraîchies, les agences sont réorganisées, et une seule plateforme peut avoir besoin de servir plusieurs marques ou sous-agences depuis une seule base de code. Un système de conception bien architecturé, avec un thématisation et une tokenisation appropriées, rend ces changements radicaux gérables au lieu de catastrophiques.

## Principes clés

- La cohérence abaisse la [charge cognitive](https://fr.wikipedia.org/wiki/Charge_cognitive) ; un bouton devrait paraître et se comporter de la même façon partout.
- Les décisions de conception sont des actifs : capturez-les une fois comme composants et jetons réutilisables.
- Les jetons sont la source de vérité pour les décisions visuelles ; les composants consomment des jetons, jamais des valeurs codées en dur.
- L'accessibilité et la réactivité sont construites dans les composants, pas boulonnées par écran.
- Un système de conception est un produit avec des utilisateurs (développeurs et designers), pas un livrable ponctuel.
- La hiérarchie visuelle guide l'attention : le type, la couleur, et l'espace devraient rendre l'importance évidente.
- La gouvernance garde un système cohérent ; la contribution le garde vivant.

## Recommandations

### Structurer le système en couches : jetons, composants, motifs

Les **jetons de conception** sont des valeurs nommées et indépendantes de plateforme pour la couleur, l'espacement, la typographie, le rayon, l'élévation, et le mouvement : les décisions atomiques. Construisez-les en niveaux : une palette primitive (valeurs brutes), des jetons sémantiques (`color-action-primary`, `space-inset-md`) qui portent du sens, et des jetons au niveau composant où vous en avez besoin. Les composants consomment les jetons sémantiques, pour qu'un changement unique se propage partout. Au-dessus des composants se trouvent les motifs : des compositions éprouvées telles qu'un tableau de données, un formulaire multi-étapes, ou un état vide. Documentez les trois couches en un seul endroit, avec des exemples vivants et des directives d'usage.

### Bien faire les fondamentaux visuels

Établissez une échelle typographique avec une hiérarchie claire et un espacement de ligne généreux pour la lisibilité, et tenez-vous à un ensemble limité de tailles et graisses. Définissez la couleur comme un système, avec assez de contraste pour l'accessibilité (voir le chapitre accessibilité) et des rôles sémantiques, plutôt que des teintes brutes éparpillées à travers l'UI. Utilisez une échelle d'espacement et une grille de mise en page pour que l'alignement et le rythme restent cohérents sans tâtonnement par écran. La hiérarchie visuelle devrait rendre l'action primaire et l'information la plus importante évidentes d'un coup d'œil.

### Concevoir de façon réactive et mobile d'abord

Concevez d'abord pour la plus petite fenêtre d'affichage raisonnable, puis améliorez pour les écrans plus grands. Cela vous force à prioriser le contenu et les contrôles essentiels. Utilisez des mises en page fluides et des unités relatives pour que les interfaces s'adaptent à tout écran, plutôt que de sauter entre quelques points de rupture fixes. Rendez les cibles tactiles assez grandes, et assurez-vous que les interactions fonctionnent avec le tactile, la souris, et le clavier. En administration publique spécialement, supposez qu'une part significative de vos utilisateurs se trouve sur des appareils petits, anciens, ou économiques.

### Faire du transfert conception-développement et de la parité une préoccupation de premier ordre

Un système de conception ne paie que quand l'UI livrée correspond à la conception voulue et continue de correspondre. Visez une source de vérité unique : les jetons exportés depuis l'outil de conception alimentent directement le code, pour que designers et ingénieurs référencent les mêmes valeurs. Fournissez une bibliothèque de composants codée que les ingénieurs utiliseront réellement, avec les mêmes noms et propriétés que les composants de conception. Utilisez le test de régression visuelle (comparaison automatisée de l'UI rendue contre des images de référence approuvées) et des contrôles de revue de conception pour attraper la dérive. Et mesurez la « parité conception-code » comme une métrique de santé explicite : la part de l'UI construite à partir de composants système contre du code ponctuel.

### Soutenir la thématisation et le marquage blanc à l'échelle de l'entreprise

Architecturez pour plusieurs marques dès le début s'il y a une quelconque chance que vous en ayez besoin. Parce que les composants consomment des jetons sémantiques, un thème n'est qu'un ensemble différent de valeurs de jeton, donc un rafraîchissement de marque ou une nouvelle sous-marque devient un changement de données, pas une réécriture de code. Soutenez les thèmes clair et sombre, les modes à haut contraste, et l'image de marque par locataire à travers le même mécanisme. Gardez la logique spécifique à la marque hors des composants, et poussez-la plutôt dans des ensembles de jetons et de la configuration.

### Gouverner le système comme un produit

Donnez au système de conception une équipe dédiée, une feuille de route, un versionnage, un journal des modifications, et un canal de support. Précisez comment les équipes contribuent de nouveaux composants, et comment ceux-ci sont révisés et promus. Équilibrez le contrôle central (pour préserver la cohérence et l'accessibilité) avec un modèle de contribution (pour que le système évolue avec les vrais besoins plutôt que de devenir un goulot d'étranglement). Communiquez clairement les dépréciations et migrations, et donnez aux équipes consommatrices assez de temps d'anticipation.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| Construire un système de conception | Cohérence, vitesse, accessibilité une fois, refontes de marque plus faciles | Coût initial et continu, exige une équipe dédiée |
| Adopter un système prêt à l'emploi | Démarrage rapide, motifs éprouvés | Apparence générique, plus difficile à adapter à une marque et des besoins uniques |
| Gouvernance centrale stricte | Cohérence, qualité, accessibilité garanties | Peut créer un goulot d'étranglement pour les équipes, sembler bureaucratique |
| Modèle de contribution ouvert | Évolue avec les vrais besoins, propriété partagée | Risque de dérive et d'incohérence sans revue |
| Tokenisation et thématisation lourdes | Refontes de marque bon marché et soutien multi-marque | Plus d'abstraction, courbe d'apprentissage plus raide |

Les systèmes de conception échangent un coût initial et de gouvernance contre une cohérence et vélocité à long terme. Pour un petit produit avec une équipe, la surcharge peut ne pas payer. Pour une grande organisation avec de nombreuses équipes et des produits de longue durée, la question n'est pas d'avoir un système mais combien investir et comment le gouverner. Le regret le plus courant est le sous-investissement dans l'outillage de gouvernance et de parité : le système existe sur papier, mais les équipes en dérivent discrètement.

## Questions à discuter avec votre équipe

1. **Comment notre architecture de jetons est-elle hiérarchisée, et les composants sont-ils interdits d'utiliser des valeurs codées en dur ?** Le gain entier d'un système de conception (refontes de marque bon marché, thématisation multi-marque, accessibilité résolue une fois) dépend des composants consommant des jetons sémantiques comme `color-action-primary` plutôt que des teintes brutes et valeurs de pixel éparpillées à travers le code. Décidez des niveaux maintenant : une palette primitive, des jetons sémantiques qui portent du sens, et des jetons au niveau composant seulement où vous en avez vraiment besoin. La sur-abstraction est un risque réel, donc convenez de combien de couches est trop et comment un développeur trouve rapidement le bon jeton. Apportez un grep de couleurs et espacements codés en dur à travers votre base de code comme preuve de dérive. Si la logique de marque est cuite dans les composants, une refonte de marque devient une réécriture de code au lieu d'un changement de configuration, ce qui est exactement la catastrophe que la tokenisation existe pour prévenir.

2. **Comment mesurons-nous et défendons-nous la parité conception-code, et quel outillage attrape la dérive automatiquement ?** Un système de conception qui n'existe que comme fichier de conception est une planche d'autocollants : les ingénieurs reconstruisent tout de toute façon et l'UI livrée diverge lentement de l'intention. Convenez d'une métrique de parité explicite (la part de l'UI construite à partir de composants système contre du code ponctuel) et câblez le test de régression visuelle dans l'intégration continue pour que les écrans rendus soient comparés contre des références approuvées. Cela compte à l'échelle de l'entreprise et gouvernementale parce que des centaines d'applications, beaucoup construites par des fournisseurs ou héritées par fusions, doivent toutes ressembler à une seule organisation. Apportez le nombre de parité actuel et une liste des principaux composants sur mesure que les équipes continuent de reconstruire. Si personne ne possède la métrique ou la suite de régression, la dérive gagne déjà discrètement.

3. **Comment gouvernons-nous la contribution, la dépréciation, et la migration pour que le système ne crée ni goulot d'étranglement ni fragmentation pour les équipes ?** Un contrôle central strict garantit la cohérence et l'accessibilité mais peut transformer l'équipe de système de conception en goulot d'étranglement que les équipes contournent ; une contribution ouverte garde le système vivant mais risque des variantes divergentes sans revue. Décidez le chemin de contribution : comment une équipe propose un nouveau composant, qui le révise, et comment il est promu. De même, convenez comment vous communiquez les changements cassants, parce que les dépréciations sans soutien de migration et temps d'anticipation causent les équipes consommatrices à s'arrêter ou forker. Apportez des exemples de composants que les équipes ont construits en dehors du système et demandez pourquoi elles n'ont pas contribué en retour. La réponse révèle habituellement si votre gouvernance est un service ou un obstacle.

4. **Comment garantissons-nous que l'accessibilité est résolue une fois à l'intérieur des composants, et qu'est-ce qui empêche une équipe de livrer un composant ponctuel inaccessible ?** L'argument le plus fort pour un système de conception est que le contraste de couleur, les états de focus, l'opération au clavier, et la sémantique de lecteur d'écran sont résolus une fois et hérités partout, mais cette promesse s'effondre au moment où les équipes codent à la main leurs propres contrôles. Pour une grande organisation c'est là que se trouve le plus grand risque légal et réputationnel, parce qu'un seul formulaire de paiement ou sélecteur de date inaccessible peut bloquer de vrais utilisateurs et déclencher des plaintes à travers chaque produit qui l'a copié. Pesez l'imposition centrale (composants accessibles plus un linter ou une porte de revue qui rejette le balisage brut) contre l'autonomie d'équipe, et décidez où se trouve la ligne dure. Apportez les résultats d'un audit d'accessibilité, une liste de composants avec leur statut de conformité, et un compte de contrôles sur mesure que les équipes ont reconstruits en dehors du système. Dans les contextes d'entreprise et gouvernementaux ce n'est pas une gentillesse : des obligations telles que WCAG, la Section 508, et l'EN 301 549 font de la conformité une exigence d'approvisionnement et d'audit, donc une bibliothèque de composants avec une conformité documentée est elle-même un actif de conformité.

5. **Combien de marques, locataires, et thèmes ce système doit-il servir, et avons-nous architecturé la couche de jetons pour cela maintenant plutôt que de la rétro-adapter plus tard ?** La thématisation est bon marché si vous avez conçu pour elle et brutale si vous ne l'avez pas fait, parce qu'une marque ou un locataire jamais anticipé force la logique de marque à revenir dans les composants et défait tout le point de la tokenisation. Pour une grande équipe cette décision façonne des années de travail : une plateforme qui doit servir plusieurs marques, un thème clair et sombre, un mode à haut contraste, et une image de marque par locataire a besoin d'une couche de jetons sémantiques assez propre pour qu'un thème ne soit qu'un ensemble différent de valeurs. Équilibrez cette flexibilité contre la sur-abstraction, puisqu'un arbre de jetons que personne ne peut naviguer est son propre échec. Apportez la feuille de route des marques et locataires que vous pouvez prévoir, le compte de thèmes en jeu aujourd'hui, et tout composant qui laisse déjà fuiter une logique spécifique à la marque. Dans les contextes d'entreprise et gouvernementaux les fusions, acquisitions, et réorganisations d'agence ajoutent régulièrement des marques que vous n'aviez pas planifiées, donc architecturer pour le multi-marque dès le début est la différence entre un changement de données et une réécriture pluriannuelle.

6. **Comment migrerons-nous les applications héritées et construites par des fournisseurs vers le système, et comment l'équipe de système de conception est-elle financée pour qu'elle survive au prochain cycle budgétaire ?** Un système de conception ne livre son retour que quand de vrais produits l'adoptent, pourtant les applications les plus difficiles à convertir sont les anciennes et sous-traitées qui en ont le plus besoin, et l'équipe qui maintient le système est souvent la première coupée quand les budgets se resserrent. Pour une grande organisation vous devez décider entre une migration à grand fracas et une incrémentale, et comment amener les fournisseurs à construire sur vos composants plutôt qu'autour. Apportez un inventaire d'applications avec leur score de parité actuel, une estimation de l'effort de migration par application, et les leviers contractuels que vous détenez sur les fournisseurs. Dans les contextes d'entreprise et gouvernementaux, écrivez la conformité au système de conception dans les termes d'approvisionnement pour que le nouveau travail de fournisseur atterrisse sur le système par défaut, et financez l'équipe de maintenance comme une infrastructure partagée durable, parce qu'un système qui perd ses intendants dans une réorganisation dérive vers la fragmentation en moins d'un an.

## Regard sectoriel

**Jeune pousse.** Avec deux ou trois ingénieurs et aucune marge pour épargner, ne construisez pas de système gouverné. Passez un jour ou deux à définir un petit ensemble de jetons sémantiques pour la couleur, l'espacement, et le type, plus une douzaine de composants partagés, tous dans un seul fichier que toute l'équipe référence. Appuyez-vous sur une bibliothèque primitive prête à l'emploi pour les parties difficiles, et ne gardez rien codé en dur pour que votre première vraie refonte de marque soit un changement de jeton plutôt qu'une réécriture.

**Petite entreprise.** Sans designer dédié et avec un budget serré, achetez plutôt que construisez : adoptez une bibliothèque de composants ou un kit UI éprouvé et thématisez-le légèrement à votre marque. Votre objectif est un produit cohérent et accessible sans doter une équipe de système de conception, donc favorisez un système qui livre l'accessibilité et la réactivité de série. Résistez à l'envie de le forker, parce qu'une copie personnalisée que vous ne pouvez pas maintenir devient un passif au moment où le projet amont avance.

**Grande entreprise.** Le problème est la cohérence à travers de nombreuses équipes et produits de longue durée, donc traitez le système de conception comme une infrastructure partagée gouvernée avec une équipe dédiée, un versionnage, et une feuille de route. Suivez la parité conception-code comme une vraie métrique, câblez le test de régression visuelle dans l'intégration continue, et architecturez la couche de jetons pour plusieurs marques et thèmes dès le début. Budgétez explicitement le coût de gouvernance et de migration, et gérez l'adoption comme un portefeuille plutôt que de supposer que les équipes dériveront vers le système par elles-mêmes.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la responsabilité publique façonnent chaque choix. La conformité d'accessibilité à des normes telles que WCAG, la Section 508, et l'EN 301 549 est une exigence légale, pas une préférence, donc une bibliothèque de composants avec une conformité documentée devient un actif de conformité. Favorisez ou étendez un système de conception public partagé pour que les citoyens rencontrent les mêmes motifs à travers les services, écrivez l'usage du système de conception dans les contrats de fournisseurs, et publiez ouvertement vos composants et directives pour que les agences et leurs fournisseurs puissent les adopter et en être tenus responsables.

## Exemples

**Jeune pousse.** Une jeune pousse à deux ingénieurs continuait de reconstruire des boutons et champs de formulaire légèrement différemment à chaque nouvel écran, et le produit commençait à paraître cousu ensemble. Au lieu d'un système lourd, ils ont passé deux jours à définir un petit ensemble de jetons de conception sémantiques pour la couleur, l'espacement, et le type, plus environ une douzaine de composants partagés, tous dans un seul fichier que toute l'équipe référençait. Parce que rien n'était codé en dur, quand leur première embauche orientée conception a proposé une palette plus propre, le rafraîchissement a été un changement de jeton qui a atterri à travers l'application en un après-midi plutôt qu'un labeur écran par écran.

**Grande entreprise.** Une entreprise logicielle mondiale avec des dizaines d'équipes produit a construit un système de conception tokenisé avec une bibliothèque de composants codée partagée. Les jetons sémantiques leur ont permis de livrer une refonte de marque complète à travers tous les produits en semaines, au lieu d'un labeur pluriannuel équipe par équipe, parce que le changement était un nouvel ensemble de jetons plutôt que des milliers d'éditions de couleur codées en dur. La parité conception-code, suivie comme une métrique de tableau de bord, a augmenté à mesure que les équipes remplaçaient des composants sur mesure, ce qui a réduit la maintenance UI dupliquée.

**Gouvernement.** Un gouvernement national a créé un système de conception commun pour les services publics (composants partagés, motifs, et accessibilité intégrés) mandaté à travers les agences. Un citoyen se déplaçant entre un service fiscal, un service de santé, et un service de licence rencontre le même en-tête, les mêmes contrôles de formulaire, et les mêmes motifs d'erreur, ce qui construit la confiance et raccourcit la courbe d'apprentissage. Les agences et leurs fournisseurs livrent plus rapidement et plus accessiblement parce que les problèmes difficiles sont résolus centralement, et le gouvernement peut mettre à jour la directive ou les corrections d'accessibilité une fois et les faire se propager partout.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur investissement d'un système de conception vient de la suppression de la duplication et de l'accélération de la livraison. Au lieu que chaque équipe conçoive et construise les mêmes composants, elles composent à partir d'une bibliothèque partagée, ce qui accélère mesurablement la livraison et libère les designers et ingénieurs pour du travail spécifique au produit. L'accessibilité et la réactivité, résolues une fois dans les composants, vous économisent le coût de remédiation par projet. Les refontes de marque et la thématisation qui prenaient autrefois des années prennent maintenant des semaines.

Sur le coût total de possession, le coût d'adoption est une équipe dédiée, de l'outillage, et l'effort pour que les produits existants migrent vers le système. Le coût de ne pas adopter est payé continuellement : construction et maintenance dupliquées à travers les équipes, UI incohérentes et inaccessibles qui créent un risque de support et légal, et refontes de marque lentes et coûteuses. Parce que la duplication est répartie à travers les budgets de nombreuses équipes, elle est facile à négliger : un système de conception rend ce coût caché visible et le capture en un seul endroit.

Pour faire valoir cela auprès de la direction, quantifiez le travail de composant dupliqué à travers les équipes, le gain de délai de mise sur le marché de la composition, et le coût et la durée de votre dernière refonte de marque contre ce qu'un système tokenisé permettrait. Cadrez le système comme une infrastructure partagée avec une métrique d'adoption mesurable (pourcentage de parité), pour que sa valeur puisse être suivie dans le temps plutôt que simplement affirmée.

## Anti-patterns et pièges

- **Système de conception comme planche d'autocollants** : un fichier de conception statique sans composants codés, pour que les ingénieurs reconstruisent tout de toute façon.
- **Valeurs codées en dur partout** : couleurs et espacements éparpillés à travers le code, rendant la thématisation et les refontes de marque impossibles.
- **Aucune gouvernance** : le système se fragmente à mesure que les équipes ajoutent des variantes divergentes ; la cohérence s'érode.
- **Gouvernance sans contribution** : l'équipe centrale devient un goulot d'étranglement et les équipes la contournent.
- **Ignorer la parité** : l'UI codée dérive de l'intention de conception et personne ne mesure l'écart.
- **Sur-abstraction** : tant de jetons et de couches que personne ne peut trouver ou utiliser le bon.
- **Logique de marque cuite dans les composants** : rend le multi-marque et la thématisation une réécriture de code au lieu d'un changement de configuration.
- **Changements cassants sans soutien de migration** : les équipes consommatrices s'arrêtent ou forkent le système.

## Modèle de maturité

**Niveau 1 (Initier).** Chaque équipe construit sa propre UI au coup par coup et réactivement. Aucun composant partagé, apparence et comportement incohérents, couleurs et espacements codés en dur par écran. Chaque refonte de marque est un labeur manuel écran par écran.

**Niveau 2 (Développer).** Un guide de style partagé ou une bibliothèque de composants existe mais est partiel, optionnel, et souvent désynchronisé entre la conception et le code. Certaines équipes l'utilisent, d'autres non, et les pratiques de base varient largement d'équipe à équipe.

**Niveau 3 (Standardiser).** Un système de conception tokenisé avec une bibliothèque codée maintenue, de la documentation, et une gouvernance est documenté et imposé à travers l'organisation entière. Les composants consomment des jetons sémantiques, la thématisation est soutenue, et l'accessibilité et la réactivité sont construites plutôt que boulonnées par écran.

**Niveau 4 (Gérer).** Le système est mesuré et contrôlé avec des données contre des références. La parité conception-code est suivie comme une métrique explicite avec des cibles par produit, le test de régression visuelle s'exécute dans l'intégration continue pour attraper la dérive, et la conformité d'accessibilité est mesurée contre des normes plutôt que supposée. Des tableaux de bord d'adoption montrent la couverture de composant par équipe, et le coût et la durée des refontes de marque sont enregistrés pour que l'amélioration soit visible dans le temps.

**Niveau 5 (Orchestrer).** Le système de conception est un produit en amélioration continue intégré à travers l'organisation et adaptatif au changement. Il a un versionnage, une feuille de route, et un modèle de contribution fonctionnel, pour qu'il évolue avec les vrais besoins. Les refontes de marque et nouveaux thèmes sont des changements de jeton routiniers, la thématisation multi-marque et multi-locataire est normale, et l'équipe retire, recadre, et promeut des motifs sur la base de preuves issues de données d'usage, alimentant l'outillage de conception et les pipelines de livraison depuis une source de vérité unique.

## Pistes de réflexion

- Comment équilibrez-vous la gouvernance centrale contre l'autonomie d'équipe sans fragmenter ni créer un goulot d'étranglement ?
- Quelle est la bonne métrique pour la « parité conception-code », et comment la gardez-vous honnête ?
- Quand une équipe devrait-elle être autorisée à construire un composant ponctuel plutôt que d'utiliser le système ?
- Comment financez-vous et dotez-vous un système de conception pour qu'il survive aux cycles budgétaires et réorganisations ?
- Combien de flexibilité de thématisation vaut le coût d'abstraction ajouté ?
- Comment migrez-vous les applications héritées et construites par des fournisseurs vers un système partagé ?

## Points clés à retenir

- Un système de conception transforme les décisions de conception ponctuelles en capital réutilisable et gouverné.
- Structurez-le en couches (jetons, composants, motifs), avec les composants consommant des jetons sémantiques.
- Construisez l'accessibilité et la réactivité dans les composants pour que chaque équipe en hérite.
- Traitez la parité conception-code comme une métrique de santé mesurable, pas une supposition.
- La tokenisation fait des refontes de marque et de la thématisation multi-marque un changement de données, pas une réécriture.
- Gouvernez le système comme un produit avec une feuille de route, un versionnage, et un modèle de contribution.
- À l'échelle de l'entreprise et gouvernementale, un système partagé est l'investissement UI à plus haut levier disponible.

## Références et lectures complémentaires

- Brad Frost, *Atomic Design*.
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*.
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*.
- Robert Bringhurst, *The Elements of Typographic Style*.
- Ellen Lupton, *Thinking with Type*.
- Luke Wroblewski, *Mobile First*.
- Ethan Marcotte, *Responsive Web Design*.
- Nathan Curtis, écrits sur les jetons de conception et la gouvernance de système de conception.
- W3C Design Tokens Community Group, spécification de format.
- Systèmes de conception gouvernementaux (par exemple UK Government Design System, U.S. Web Design System) comme implémentations de référence.
