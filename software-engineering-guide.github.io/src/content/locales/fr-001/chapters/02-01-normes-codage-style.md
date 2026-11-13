# 2.1 Normes de codage et style

## Vue d'ensemble et motivation

Les normes de codage sont les conventions partagées qui laissent de nombreuses personnes écrire du code comme si un seul auteur méticuleux l'avait écrit. Elles couvrent le nommage, le formatage, la disposition des fichiers, les idiomes, la gestion d'erreurs, et les paradigmes qu'une équipe privilégie. Dans une petite équipe, le goût individuel peut suffire. Dans une grande équipe (des centaines ou des milliers d'ingénieurs, de nombreux prestataires, un fort renouvellement), l'incohérence devient une taxe que vous payez à chaque lecture, chaque revue, et chaque intégration. Les normes transforment d'innombrables petits débats stylistiques en une décision unique qu'une machine applique ensuite pour vous.

Pour les grandes organisations, les enjeux sont concrets. Le code est lu bien plus souvent qu'il n'est écrit. Dans les contextes d'entreprise et gouvernementaux, une ligne de code peut être lue par des auditeurs, des réviseurs de sécurité, et des mainteneurs des années après le départ de son auteur. Un style cohérent abaisse le coût mental de cette lecture, réduit la surface pour les bugs, et rend l'analyse automatisée fiable à travers les [linters](https://en.wikipedia.org/wiki/Lint_(software)) (des outils qui signalent automatiquement les bugs probables et les violations de style), les scanners de sécurité, et les outils de [refactorisation](https://en.wikipedia.org/wiki/Code_refactoring). Là où la réglementation s'applique, comme dans les services financiers, la santé, la défense, et les systèmes du secteur public, les normes forment aussi une partie de la preuve qu'une base de code est maintenable et contrôlée.

L'approche moderne consiste à traiter le style comme une préoccupation résolue et automatisée plutôt qu'une question de jugement humain continu. Les formateurs et les linters s'exécutent dans l'éditeur, dans les hooks de pré-commit, et en [intégration continue](https://en.wikipedia.org/wiki/Continuous_integration) (CI), le processus automatisé de construction et de test qui s'exécute à chaque changement. Les machines appliquent le style, afin que vous puissiez dépenser votre attention de revue sur la conception et l'exactitude. L'objectif n'est pas l'uniformité pour elle-même. C'est le retrait de la friction : vous devriez pouvoir circuler entre services et équipes sans réapprendre les bases.

## Principes clés

- La cohérence l'emporte sur la préférence individuelle ; un style unique convenu, appliqué partout, vaut plus que le « meilleur » style appliqué inégalement.
- Automatisez l'application. Les formateurs et les linters sont la source de vérité, pas les commentaires de revue de code sur l'espacement.
- Optimisez pour le lecteur et le mainteneur, pas l'auteur original.
- Préférez les conventions que la communauté de langage plus large utilise déjà aux règles maison sur mesure.
- Rendez la norme facile à adopter : fournissez des configurations partagées, des modèles, et de l'outillage plutôt qu'un PDF que personne ne lit.
- Les règles de style devraient être peu nombreuses, défendables, et sans ambiguïté ; chaque règle a un mécanisme d'application ou ce n'est qu'une suggestion.
- Le nommage est la décision de lisibilité à plus fort effet de levier et mérite des conseils explicites.

## Recommandations

### Adoptez un guide de style canonique par langage

Pour chaque langage que vous utilisez, adoptez un guide de style largement reconnu comme référence (par exemple, le guide communautaire ou du fournisseur pour ce langage) et documentez seulement les écarts dont votre organisation a besoin. N'inventez pas un style maison depuis zéro. Publiez votre choix dans un endroit central et repérable, et versionnez-le comme du code.

### Rendez les formateurs des défauts non négociables

Utilisez un formateur automatique tranché pour chaque langage qui en a un, avec une configuration unique et partagée intégrée au dépôt. Le formatage ne devrait jamais surgir en revue, parce qu'il est appliqué automatiquement à la sauvegarde et vérifié en CI. Là où un langage manque d'un formateur solide, choisissez une configuration de linter et traitez-la de la même façon.

### Faites fonctionner les linters comme des portes appliquées, pas des conseils

Configurez les linters avec un ensemble de règles convenu, faites échouer la construction sur les violations, et gardez l'ensemble de règles dans le [contrôle de version](https://en.wikipedia.org/wiki/Version_control) afin que les changements passent par la revue. Séparez les règles auto-corrigibles (appliquez-les automatiquement) des règles qui ont besoin de jugement humain (signalez et bloquez). Introduisez les nouvelles règles en mode « avertissement », nettoyez l'arriéré, puis promouvez-les en « erreur ».

### Appliquez à plusieurs couches

Fournissez une intégration d'éditeur pour un retour instantané, des hooks de pré-commit pour l'application locale, et des contrôles CI comme la porte faisant autorité. Plus tôt vous attrapez une violation, moins elle coûte. La CI doit être le dernier rempart, parce que les hooks locaux peuvent être contournés.

### Donnez des règles explicites au nommage

Standardisez les conventions de casse par langage, exigez des noms révélateurs d'intention, interdisez les abréviations trompeuses, et définissez des conventions pour les booléens, les collections, les unités, et les opérations asynchrones. Écrivez votre vocabulaire de domaine dans un glossaire partagé afin que le même concept ait le même nom partout.

### Gérez délibérément la cohérence polyglotte

Dans une base de code qui s'étend sur plusieurs langages, visez des concepts cohérents (modèles de gestion d'erreurs, structure de journalisation, disposition de projet) même là où la syntaxe diffère. Fournissez des configurations par langage depuis un dépôt central afin qu'un nouveau service hérite des normes automatiquement à travers des modèles ou de l'échafaudage.

### Codifiez les idiomes et les paradigmes

Allez au-delà du formatage. Écrivez vos idiomes préférés, comme comment gérer les erreurs, comment structurer les modules, et quand utiliser les exceptions contre les types de résultat, ainsi que les paradigmes que vos équipes privilégient. C'est là que vivent la vraie lisibilité et la maintenabilité.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| Formateur automatique strict, zéro configuration | Termine tout débat de formatage ; cohérence instantanée ; intégration triviale | Certains choix impopulaires sont non négociables ; grand diff initial à la première application |
| Linter configurable avec règles maison | Adapté aux besoins de l'organisation ; peut encoder de vraies règles de prévention de bugs | Dérive de configuration ; discussions stériles sur les règles ; charge de maintenance |
| Norme communautaire adoptée en bloc | Familière aux nouvelles recrues ; écosystème d'outillage fort ; faible maintenance | Peut ne pas convenir aux contraintes de niche de l'organisation ; règles occasionnellement maladroites |
| Norme interne sur mesure | S'adapte exactement à l'organisation | Coûteuse à écrire et maintenir ; peu familière aux recrues ; outillage faible |
| Autonomie par équipe | Moral local élevé ; spécifique au contexte | Fragmentation ; mobilité inter-équipes pénible ; outillage incohérent |

Les défauts appliqués échangent un peu d'autonomie individuelle contre de grands gains collectifs : moins de friction en revue, une intégration plus rapide, et une automatisation fiable. Le risque principal est de surconcevoir la norme en centaines de règles qui ralentissent tout le monde sans prévenir de vrais défauts. Gardez l'ensemble de règles petit et fondé sur des preuves, et penchez vers l'adoption d'une norme existante afin que la maintenance reste peu coûteuse.

## Questions à discuter avec votre équipe

1. **Quelles règles de linter devraient faire échouer la construction, et comment promouvez-vous une règle d'avertissement à erreur sans arrêter tout le monde ?** Ce chapitre argumente que chaque règle a besoin d'un mécanisme d'application, et que les nouvelles règles devraient atterrir en mode avertissement, voir leur arriéré nettoyé, puis basculer en erreur. Dans une grande équipe, basculer une règle en erreur contre une base de code sale bloque du jour au lendemain des centaines de changements sans rapport. Apportez des preuves solides à la réunion : le nombre actuel de violations pour chaque règle candidate, et si elle est auto-corrigible ou a besoin de jugement humain. Dans les contextes d'entreprise et gouvernementaux, la ligne de passage/échec alimente aussi les portes d'audit, donc un ensemble de règles ambigu affaiblit votre récit de conformité. Décidez d'un déploiement échelonné : auto-corrigez ce que vous pouvez, budgétez le nettoyage, puis fermez la porte.

2. **Quand vous appliquez un formateur pour la première fois à votre code hérité, comment empêcherez-vous ce reformatage de ravager git blame et de noyer les revues ?** Le tableau de compromis avertit d'un grand diff initial, et la section des anti-patterns signale le mélange de commits de reformatage avec des changements de logique. Un seul reformatage balayant réécrit des milliers de lignes et fait pointer le blame vers le reformatage au lieu du vrai auteur, ce qui nuit à quiconque débogue des années plus tard. Faites le reformatage comme un commit isolé et clairement étiqueté, et enregistrez-le dans un fichier d'ignorance de blame afin que l'historique reste utile. Pour les auditeurs qui tracent qui a changé quoi, cette isolation est la différence entre une preuve propre et du bruit. Convenez du séquençage avant de toucher le code, pas après.

3. **Qui possède votre glossaire de nommage et votre vocabulaire de domaine, et comment un nouveau terme est-il ajouté ?** Le chapitre appelle le nommage la décision de lisibilité à plus fort effet de levier et vous demande d'écrire le vocabulaire de domaine dans un glossaire partagé. Sans propriétaire nommé, le même concept ramasse trois noms différents à travers les équipes, et les outils d'analyse statique et de recherche perdent en fiabilité. Apportez des exemples de concepts qui ont déjà des noms conflictuels dans votre base de code comme signal concret. Assignez un propriétaire et un chemin de proposition léger, afin qu'ajouter ou renommer un terme soit un petit changement révisé plutôt qu'une dispute dans chaque pull request. La réponse change l'intégration : une nouvelle recrue lit un glossaire au lieu de rétro-concevoir l'intention à partir de code incohérent.

4. **Pour chaque langage, adoptez-vous un guide de style communautaire ou fournisseur reconnu en bloc, et où les écarts maison sont-ils réellement justifiés ?** Ce chapitre argumente que vous devriez prendre une norme existante comme référence et documenter seulement les écarts dont votre organisation a besoin, parce qu'une norme sur mesure est coûteuse à écrire et peu familière aux recrues. La tentation concurrente est réelle : une contrainte interne (une règle de sécurité, un cadre hérité, un mandat d'accessibilité) entre parfois réellement en conflit avec le défaut communautaire, et chaque écart que vous gardez est une règle que vous possédez et maintenez désormais pour toujours. Apportez la liste des écarts proposés à la réunion, chacun avec la contrainte concrète qui le motive, et soyez prêts à couper tout écart qui n'est que du goût. Dans les contextes d'entreprise et gouvernementaux, une référence qui correspond à la communauté de langage plus large signifie aussi que les prestataires et nouveaux fournisseurs arrivent déjà à l'aise, ce qui raccourcit l'intégration et renforce la preuve de maintenabilité que les auditeurs recherchent.

5. **Dans une base de code polyglotte, quelles conventions sont vraiment universelles et lesquelles restent locales au langage, et comment empêchez-vous les configurations par dépôt de dériver ?** Le chapitre demande des concepts cohérents (gestion d'erreurs, structure de journalisation, disposition de projet) à travers les langages même là où la syntaxe diffère, et des configurations par langage servies depuis un dépôt central afin que les nouveaux services héritent des normes automatiquement. La tension est que forcer les idiomes d'un langage sur un autre produit du code maladroit et non idiomatique, tandis que laisser chaque équipe forker sa propre configuration finit avec « la norme » ne signifiant rien. Apportez un inventaire de vos configurations actuelles de linter et de formateur par dépôt et un diff montrant à quel point elles ont déjà dérivé, comme signal concret. Pour une grande organisation faisant fonctionner des dizaines de services, décidez du mécanisme de distribution (modèles, échafaudage, un paquet de configuration partagé) afin qu'un changement de règle se propage une fois plutôt que d'être copié à la main dans chaque dépôt.

6. **Quand désactiver une règle est-il légitime, qui révise la suppression, et comment empêchez-vous les désactivations générales de vider la norme de sa substance ?** La section des anti-patterns signale les suppressions en ligne répandues comme un signe qu'une règle est fausse ou qu'une équipe a abandonné, pourtant une politique rigide sans exception pousse les gens à écrire un pire code juste pour satisfaire le linter. Convenez d'un chemin léger : une suppression doit porter une raison, se situer à la portée la plus étroite possible, et être visible en revue plutôt qu'enterrée dans un fichier d'ignorance global. Apportez le compte actuel des suppressions par règle et par dépôt, parce qu'une règle supprimée des centaines de fois vous dit quelque chose sur la règle, pas sur le code. Dans le travail réglementé et du secteur public, les suppressions générales inexpliquées affaiblissent directement le récit d'audit, puisque le pipeline ne peut plus montrer que le code fusionné a réellement passé les portes convenues.

## Regard sectoriel

**Jeune pousse.** La vitesse gagne, alors adoptez les défauts communautaires de formateur et de linter pour votre unique langage dès le premier jour et câblez-les dans un hook de pré-commit et la CI avant l'arrivée du deuxième ingénieur. N'écrivez pas de style maison que vous n'avez pas le temps de maintenir : la configuration livrée dans le dépôt est la norme entière. Quand vous ajoutez un deuxième langage, tendez la main vers le guide canonique de ce langage plutôt que d'inventer des conventions depuis zéro.

**Petite entreprise.** Sans spécialiste d'outillage dédié et avec un budget serré, appuyez-vous entièrement sur le formateur gratuit et tranché livré avec ou aux côtés de votre langage, et acceptez ses défauts plutôt que de les ajuster. C'est un cas clair d'acheter plutôt que construire : maintenir un ensemble de règles personnalisé coûte du temps que vous n'avez pas, tandis qu'un formateur prêt à l'emploi ne coûte rien et termine le débat de style immédiatement. Gardez la configuration dans le dépôt afin que l'unique prestataire que vous embaucherez l'an prochain en hérite sans conversation.

**Grande entreprise.** À grande échelle, le travail est la gouvernance à travers de nombreuses équipes : un dépôt central de normes d'ingénierie détenant les configurations de formateur et de linter partagées par langage, de nouveaux services générés depuis des modèles qui tirent ces configurations, et des portes CI qui bloquent les fusions non conformes. Versionnez l'ensemble de règles comme du code et acheminez les changements à travers une revue périodique afin que les normes évoluent délibérément plutôt que de dériver. Le gain est des ingénieurs circulant entre équipes vers du code familier, et un outillage automatisé qui produit un signal fiable parce que chaque dépôt est cohérent.

**Gouvernement.** Les marchés publics et la responsabilité façonnent le choix : mandatez un style spécifique et un ensemble de règles de sécurité comme partie des exigences d'autorisation d'exploitation, et faites en sorte que le pipeline émette un rapport montrant que chaque changement fusionné a passé les portes convenues comme preuve d'audit. Parce qu'un formateur est appliqué automatiquement, le code de plusieurs fournisseurs et prestataires semble cohérent, ce qui protège le travail de maintenance publique longtemps après la fin des contrats. Favorisez les références communautaires reconnues plutôt que des règles sur mesure afin que la norme soit transparente et que tout futur fournisseur puisse l'adopter sans verrouillage propriétaire.

## Exemples

**Jeune pousse.** Une start-up de quatre personnes adopte les défauts communautaires de formateur et de linter pour son unique langage dès le premier jour, les câblant dans un hook de pré-commit et la CI afin que personne ne débatte de l'espacement en revue. Parce que la configuration est livrée dans le dépôt, les cinquième et sixième recrues en héritent automatiquement et ne voient jamais un commentaire de formatage. Quand l'équipe ajoute plus tard un deuxième langage, elle tend la main vers le guide standard de ce langage plutôt que d'inventer un style maison qu'elle n'a pas le temps de maintenir.

**Grande entreprise.** Une grande banque fait fonctionner des services en Java, Python, et TypeScript à travers des dizaines d'équipes. Elle publie un dépôt central « normes d'ingénierie » qui détient les configurations de formateur et de linter partagées pour chaque langage. Les nouveaux services sont générés depuis un modèle qui tire ces configurations, donc chaque dépôt commence conforme. La CI bloque les fusions sur toute violation, et une revue trimestrielle gouverne les changements de règles. Le temps d'intégration pour les ingénieurs circulant entre équipes chute notablement, parce que chaque dépôt semble familier.

**Gouvernement.** Une agence du secteur public modernisant un système hérité mandate un ensemble de règles de linting d'accessibilité et de sécurité comme partie de ses exigences d'autorisation d'exploitation (ATO), l'approbation formelle nécessaire pour faire fonctionner le système en production. La conformité de style devient partie de la preuve d'audit : le pipeline produit un rapport montrant que tout le code fusionné a passé les portes d'[analyse statique](https://en.wikipedia.org/wiki/Static_program_analysis) convenues. Parce qu'un formateur est appliqué automatiquement, les prestataires de plusieurs fournisseurs produisent du code visuellement cohérent, ce qui rend le travail de maintenance à long terme du gouvernement plus facile après la fin des contrats.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le coût d'adoption des normes est surtout ponctuel : choisir des guides, câbler l'outillage, et appliquer un grand commit initial de reformatage. Le coût récurrent est faible, parce que l'application est automatisée. Le coût de *ne pas* adopter de normes est récurrent et cumulatif : chaque revue dépense des minutes sur le style, chaque intégration est plus lente, les outils d'analyse statique produisent du bruit, et le code incohérent cache des bugs. À travers une grande organisation, ces minutes s'additionnent en pertes équivalentes à temps plein.

Le retour apparaît comme une latence de revue réduite, moins de commentaires de revue liés au style, une intégration plus rapide, et un signal plus élevé de l'outillage automatisé. Dans les environnements réglementés, il y a un retour supplémentaire en préparation à l'audit : des contrôles démontrables et appliqués réduisent l'effort et le risque des revues de conformité. Pour convaincre la direction, présentez les normes comme un levier peu coûteux et à fort effet de levier sur la productivité des développeurs et la posture d'audit, et mettez un chiffre sur le coût actuel de l'incohérence en utilisant l'analyse des commentaires de revue et les données de sondage d'intégration.

## Anti-patterns et pièges

- **Le style débattu en revue de code :** le signe que l'application n'est pas automatisée ; déplacez la règle dans l'outillage.
- **Le document de normes non lu :** une page de wiki sans application est de la décoration ; chaque règle a besoin d'un mécanisme.
- **La prolifération de règles :** des centaines de règles pédantes qui ralentissent le travail sans prévenir les défauts.
- **La dérive de configuration :** chaque dépôt fourche sa propre configuration de linter jusqu'à ce que « la norme » ne signifie rien.
- **Formater tout le dépôt au milieu du travail de fonctionnalité :** mélanger les commits de reformatage avec les changements de logique détruit la revue et le blame ; faites les grands reformatages dans des commits isolés et clairement étiquetés.
- **Ignorer le linter avec des suppressions générales :** des désactivations en ligne répandues signalent une règle fausse ou une équipe qui a abandonné.
- **Des normes sans propriété :** aucun propriétaire clair signifie que les règles n'évoluent jamais et pourrissent.

## Modèle de maturité

- **Niveau 1, Initiation :** Le style est par auteur et réactif ; aucune configuration partagée ; le formatage est débattu en revue et réglé par qui s'en soucie le plus ce jour-là.
- **Niveau 2, Développement :** Des équipes individuelles adoptent un formateur et un linter, mais les configurations et ensembles de règles varient d'équipe en équipe et de dépôt en dépôt, donc la cohérence s'arrête à la frontière de chaque équipe.
- **Niveau 3, Standardisation :** Des configurations centrales partagées par langage sont documentées et appliquées dans toute l'organisation ; la CI bloque les fusions non conformes ; les nouveaux dépôts héritent des normes automatiquement à travers des modèles ou de l'échafaudage.
- **Niveau 4, Gestion :** La norme est mesurée et contrôlée avec des données : taux de violation, comptes de suppression, commentaires de revue liés au style, et temps d'intégration sont suivis par rapport à des références, et les changements de règles sont promus ou retirés sur cette preuve plutôt que l'opinion.
- **Niveau 5, Orchestration :** Les normes sont continuellement améliorées et intégrées à travers l'organisation ; les idiomes polyglottes et le vocabulaire de domaine sont documentés et appliqués, l'application est quasi sans friction, et l'ensemble de règles s'adapte à mesure que les langages, l'outillage, et les besoins organisationnels changent.

## Pistes de réflexion

- Où est la ligne entre une règle appliquée et une directive documentée qui fait confiance au jugement de l'ingénieur ?
- Comment l'organisation devrait-elle gérer une règle communautaire chérie qui entre en conflit avec une véritable contrainte interne ?
- Qui possède les normes, et comment les changements de règles sont-ils proposés, débattus, et déployés sans perturbation ?
- Dans une base de code polyglotte, quelles conventions devraient être vraiment universelles et lesquelles devraient rester locales au langage ?
- Comment adaptez-vous rétroactivement les normes sur une grande base de code héritée sans un reformatage perturbateur en big bang ?
- Quel rôle l'outillage assisté par IA devrait-il jouer dans la suggestion ou l'application d'idiomes au-delà du formatage mécanique ?

## Points clés à retenir

- Traitez le style comme un problème automatisé et résolu afin que les humains révisent la conception et l'exactitude.
- Adoptez les normes communautaires existantes et documentez seulement les écarts.
- Appliquez aux couches éditeur, pré-commit, et CI, avec la CI comme porte faisant autorité.
- Gardez l'ensemble de règles petit, défendable, et gouverné centralement.
- Le nommage et les idiomes, pas l'espacement, sont là où la lisibilité se gagne réellement.

## Références et lectures complémentaires

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt et David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell et Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (éd.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* et les guides de style de langages (comme exemplaires de référence)
