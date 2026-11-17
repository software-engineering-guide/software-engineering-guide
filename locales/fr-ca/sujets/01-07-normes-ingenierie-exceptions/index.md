# 1.7 Normes d'ingénierie et exceptions

## Vue d'ensemble et motivation

Une **norme d'ingénierie** est une règle documentée et convenue sur la façon dont le travail est fait. Par exemple, « tous les services doivent exposer un point de terminaison de vérification de santé », ou « toutes les pages web publiques doivent satisfaire les **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Web Content Accessibility Guidelines) 2.2 niveau AA** ». Une norme n'est pas une suggestion, et pas une simple convention. C'est un engagement que l'organisation prend envers elle-même, idéalement un que vous pouvez vérifier. Ce chapitre porte sur le cycle de vie complet des normes, comment une grande organisation les **rédige, publie, adopte, applique, et fait évoluer**, et, tout aussi important, comment elle gère les cas qui tombent légitimement en dehors grâce à un **processus d'exceptions** gouverné (aussi appelé **processus de dérogation**) : une permission documentée et à durée limitée de dévier d'une norme pour une raison énoncée.

La motivation est qu'à grande échelle, les normes informelles cessent de fonctionner. Quand cinq ingénieurs partagent une pièce, « comment on fait les choses ici » voyage par conversation et osmose. Quand cinq mille ingénieurs couvrent des dizaines d'équipes, trois fuseaux horaires, et une décennie de renouvellement de personnel, cette connaissance tacite se fragmente en centaines d'habitudes locales incompatibles. Les normes sont la façon dont vous écrivez vos leçons durement acquises une fois, afin que chaque équipe en hérite au lieu de réapprendre chacune à travers sa propre panne. Elles réduisent la [charge cognitive](https://en.wikipedia.org/wiki/Cognitive_load), rendent les [revues de code](https://en.wikipedia.org/wiki/Code_review) portées sur le fond plutôt que sur le style, permettent aux gens de circuler entre équipes, et donnent aux auditeurs et régulateurs quelque chose de concret à évaluer.

Mais les normes portent leur propre mode d'échec : la rigidité. Une norme qui n'admet aucune exception finira, tôt ou tard, par bloquer un travail légitime : un pic ponctuel, une contrainte fournisseur, un cas véritablement nouveau que les auteurs n'ont jamais imaginé. Les équipes s'arrêtent alors, ou, pire, ignorent silencieusement la norme, ce qui corrode la crédibilité de *chaque* norme. Le remède est le vieil aphorisme « l'exception confirme la règle ». Un processus d'exceptions visible et fondé sur des principes est ce qui garde les normes à la fois crédibles et humaines. Ce chapitre s'appuie sur la prise de décision et la gouvernance (chapitre 1.5) et les registres de décision (chapitre 1.6), et alimente directement les normes et le style de codage (chapitre 2.1), les listes de contrôle (chapitre 12.2), et les modèles (chapitre 12.3).

## Principes clés

- **Une norme énonce un résultat, et donne une raison.** Règle plus justification ; sans le *pourquoi*, les gens ne peuvent pas juger quand elle s'applique vraiment.
- **Si elle ne peut pas être vérifiée, ce n'est pas encore une norme.** Préférez les énoncés testables aux aspirations.
- **Les normes sont des documents vivants.** Elles sont versionnées, possédées, datées, et révisées, pas gravées dans la pierre et abandonnées.
- **Automatisez l'application là où vous le pouvez ; réservez la revue humaine au jugement.** Les machines vérifient le mécanique ; les gens vérifient le sensé.
- **Les déviations sont attendues, pas honteuses, mais elles doivent être visibles.** Une dérogation honnête vaut mieux qu'une non-conformité silencieuse à chaque fois.
- **Bornez dans le temps chaque exception.** Une exception permanente est un défaut de la norme ; faites-le remonter et corrigez la norme.
- **Des mots et des exemples plutôt que du jargon et des mandats.** Les gens suivent les normes qu'ils comprennent et dont ils peuvent copier l'exemple.

## Recommandations

### Écrivez des normes claires, testables, et justifiées

Une bonne norme est un document court et autonome avec une forme prévisible afin que les lecteurs sachent où regarder. Adoptez un **modèle de norme** (chapitre 12.3) et utilisez-le partout. Les sections essentielles incluent :

- **Titre et identifiant :** un nom stable et un numéro de référence pour citation.
- **Statut :** brouillon, actif, remplacé, ou retiré, avec une date.
- **La règle :** énoncée comme un résultat, simplement et sans ambiguïté (« doit », « devrait », « peut », utilisés délibérément, selon les conventions **RFC 2119** pour les mots-clés d'exigence).
- **Justification :** *pourquoi* cette règle existe ; le coût ou le risque qu'elle prévient.
- **Exemples :** un exemple conforme et un non conforme ; le concret vaut mieux que l'abstrait.
- **Comment elle est vérifiée :** le test automatisé, la règle de linter, ou l'étape de revue qui la vérifie.
- **Propriétaire et date de revue :** qui la maintient et quand elle est prochainement revisitée.

Les champs justification et « comment elle est vérifiée » sont ce qui distingue une vraie norme d'un vœu pieux. Si vous ne pouvez pas dire pourquoi une règle existe, demandez-vous si elle devrait exister. Si vous ne pouvez pas dire comment la conformité est vérifiée, la règle sera appliquée de manière incohérente et provoquera du ressentiment.

### Associez chaque norme à une liste de contrôle de bonnes pratiques

Les normes définissent la destination. Une **liste de contrôle de bonnes pratiques**, une liste courte et ordonnée d'étapes ou d'éléments concrets à confirmer, aide les gens à y arriver et leur permet de s'auto-vérifier avant la revue. Les manuels d'ingénierie du secteur public utilisent abondamment ce modèle. **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** et Digital Health and Care Wales (DHCW) publient des normes d'ingénierie avec des listes de contrôle pratiques, et le **[UK Government Digital Service](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS)** associe son Service Standard et son Technology Code of Practice avec les conseils actionnables du Service Manual. La liste de contrôle est la norme rendue utilisable : « Avez-vous ajouté un audit d'accessibilité ? Avez-vous testé avec un lecteur d'écran ? Avez-vous couvert la navigation au clavier seul ? » Voir le chapitre 12.2 pour le modèle de liste de contrôle en entier.

### Publiez les normes là où les gens travaillent déjà, et gardez-les repérables

Stockez les normes dans le **[contrôle de version](https://en.wikipedia.org/wiki/Version_control)** (un dépôt source) en Markdown, rendues sur un site interne consultable, afin qu'elles obtiennent l'historique, la revue par pull request, et les différences gratuitement, le même argument que pour les registres de décision (chapitre 1.6). Un catalogue, un modèle, une boîte de recherche. La mise en avant compte autant que le stockage. Liez la norme pertinente depuis le modèle de pull request, le message d'erreur du linter, et l'échafaudage du service, afin que la bonne règle apparaisse au moment du travail plutôt que dans un dossier que personne ne visite.

### Appliquez d'abord par l'automatisation, la revue humaine ensuite

Il y a deux façons d'appliquer une norme, et les organisations matures utilisent les deux délibérément :

- **Application automatisée :** les [linters](https://en.wikipedia.org/wiki/Lint_(software)), les formateurs, l'[analyse statique](https://en.wikipedia.org/wiki/Static_program_analysis), la politique en tant que code (par exemple, **Open Policy Agent (OPA)**), les portes d'[intégration continue](https://en.wikipedia.org/wiki/Continuous_integration) (CI), et les **fonctions d'aptitude d'architecture** (tests automatisés qui affirment qu'une propriété de conception tient toujours). L'automatisation est cohérente, infatigable, immédiate, et incontestable, ce qui la rend idéale pour la majorité mécanique des normes (formatage, nommage, règles de dépendances, métadonnées requises).
- **Revue humaine :** la revue de code, les comités de revue d'architecture, et la revue de sécurité, réservées à ce que les machines ne peuvent pas juger : si une abstraction est solide, si un compromis est judicieux, si l'*intention* d'une norme est satisfaite même quand sa lettre est maladroite.

La règle empirique : **automatisez ce qui est vérifiable, et dépensez l'attention humaine rare sur le jugement.** Chaque norme que vous pouvez déplacer de la revue vers la CI libère les réviseurs pour faire la réflexion qu'eux seuls peuvent faire.

### Gouvernez les déviations avec un processus documenté d'exceptions/dérogations

Aucune norme ne convient à tous les cas, alors concevez la trappe de sortie exprès. Un bon processus d'exceptions spécifie :

- **Qui peut accorder une dérogation :** une autorité nommée et responsable, proportionnée au risque (un tech lead pour une déviation de style à faible enjeu ; un comité d'architecture ou de sécurité pour une dérogation de contrôle de sécurité). Cela se rattache directement au modèle de gouvernance du chapitre 1.5.
- **Ce qui doit être enregistré :** la norme dont on dévie, la raison spécifique, la portée, les contrôles compensatoires ou les mitigations, et le risque accepté. Capturez cela comme un registre de décision (chapitre 1.6) afin que la justification soit préservée.
- **Une expiration obligatoire :** chaque dérogation est **bornée dans le temps** avec une date de fin explicite. C'est la règle unique la plus importante : elle empêche une exception temporaire de devenir silencieusement une politique permanente.
- **Revue périodique :** un propriétaire révise les dérogations ouvertes sur une cadence et soit les renouvelle avec une justification fraîche, soit les clôture quand le travail se conforme, soit, si la même exception revient sans cesse, traite cela comme la preuve que la *norme elle-même* est fausse et la révise.

Ce dernier point est le cœur de « l'exception confirme la règle ». Un flux constant de dérogations contre une norme n'est pas un échec de discipline. C'est une donnée. Cela vous indique que la norme est mal calibrée, et la correction consiste à faire évoluer la norme, pas à continuer d'accorder des exceptions.

### Traitez les normes comme des documents vivants avec une propriété claire

Donnez à chaque norme un **propriétaire** (un rôle, pas seulement une personne) responsable de la garder à jour, et une **cadence de revue** (au moins annuelle). Offrez un chemin léger pour que n'importe qui propose un changement via une pull request ou un **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (demande de commentaires)**, une proposition écrite diffusée pour retour avant adoption. Versionnez les normes, dépréciez-les explicitement, et annoncez les changements. Un catalogue de normes jamais révisé pourrit en folklore que les gens citent sélectivement et auquel ils font peu confiance.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients |
|---|---|---|
| **Beaucoup de normes détaillées** | Cohérence, intégration facile, prête pour l'audit | Rigidité ; charge de maintenance ; peut dépasser la pratique |
| **Peu de normes de haut niveau** | Flexible ; faible entretien | Incohérence ; plus de replaidoiries par équipe |
| **Application automatisée** | Cohérente, immédiate, infatigable, évolutive | Coût initial ; faux positifs ; aveugle à l'intention |
| **Application par revue humaine** | Juge l'intention et la nuance | Lente, incohérente, un goulot d'étranglement à l'échelle |
| **Stricte, sans exceptions** | Message simple ; rien à détourner | Bloque le travail légitime ; provoque la non-conformité silencieuse |
| **Processus d'exceptions gouverné** | Garde les normes crédibles et humaines | Exige gouvernance, enregistrements, et suivi |

La tension centrale est **cohérence contre flexibilité**. Une norme existe pour retirer la variation ; un processus d'exceptions existe pour admettre la variation véritablement justifiée. Penchez trop vers la rigidité et les gens contournent vos normes. Penchez trop vers le laxisme et les normes ne signifient rien. Le processus d'exceptions est la soupape de pression qui vous laisse tenir une ligne ferme *et* rester honnête sur la réalité.

## Questions à discuter avec votre équipe

1. **Combien de normes est le bon nombre pour votre échelle, et les vôtres dérivent-elles vers la rigidité ou vers l'incohérence ?** Le catalogue lui-même est un compromis : beaucoup de normes détaillées achètent cohérence, intégration facile, et disponibilité pour l'audit au prix de la rigidité et de la charge de maintenance, tandis que peu de normes de haut niveau restent flexibles mais laissent chaque équipe replaider les mêmes questions. Pour une grande entreprise ou un organisme gouvernemental, la bonne taille dépend de combien de variation vous pouvez réellement tolérer contre combien vos auditeurs et votre intégration ont besoin d'être fixés. Apportez des preuves : combien de normes actives vous avez, combien ont été révisées l'an dernier, et à quelle fréquence les équipes redébattent des choses qu'une norme aurait pu régler. Un catalogue qui dépasse la pratique devient folklore, et un catalogue trop mince déplace le coût sur chaque équipe. Décidez délibérément ce qui mérite une norme, et élaguez celles qui ne justifient plus leur coût.

2. **Où la lettre d'une norme passe-t-elle automatiquement pendant que son intention est silencieusement violée, et comment attraperez-vous cela ?** L'automatisation est cohérente, infatigable, et aveugle à l'intention, ce qui signifie qu'un linter ou un contrôle de politique peut passer au vert pendant que l'objectif réel (une abstraction solide, un compromis judicieux, une page réellement accessible) est manqué. La règle empirique est d'automatiser le vérifiable et de dépenser la revue humaine rare sur le jugement, et la partie difficile est de convenir de quelles normes ont une intention qu'aucune porte de CI ne peut affirmer. Apportez des exemples : des normes que les gens satisfont à la lettre tout en défaisant le but, comme un point de terminaison de vérification de santé qui rapporte sain pendant que le service est cassé, ou du code qui passe le formateur mais obscurcit le sens. Dans les contextes réglementés, l'intention compte le plus pour les contrôles de sécurité et de sûreté, où une case verte peut cacher un risque réel. Décidez quelles normes gardent spécifiquement un réviseur humain pour juger l'intention, et formulez ces normes autour du résultat afin que la machine et le réviseur visent la même cible.

3. **Qui possède la boucle de rétroaction dérogation-vers-norme, et à quel point une exception récurrente vous force-t-elle à changer la règle ?** Un flux constant de dérogations contre une norme est une donnée, pas de l'indiscipline, et le signal se perd à moins que quelqu'un soit responsable de le lire et d'agir. La considération concurrente est que réviser une norme est un vrai travail, donc il reste plus facile de continuer à approuver des dérogations que de corriger la règle mal calibrée en dessous. Apportez les chiffres : quelles normes génèrent le plus d'exceptions, si les dérogations sont réellement bornées dans le temps et révisées sur une cadence, et combien sont silencieusement devenues permanentes. Pour les normes critiques pour la sécurité et la sûreté en entreprise et au gouvernement, une dérogation doit enregistrer des contrôles compensatoires, une mitigation, le risque accepté, et une expiration ferme, sinon une déviation temporaire devient une politique non documentée qui refait surface au prochain audit. Assignez un propriétaire pour réviser les dérogations ouvertes, fixez un seuil auquel des exceptions répétées déclenchent une révision de norme, et traitez une exception permanente comme un défaut de la norme à corriger.

4. **La bonne norme apparaît-elle au moment du travail, ou vit-elle dans un dossier que personne n'ouvre ?** Une norme que personne ne peut trouver est appliquée par chance, et à grande échelle la plupart de la non-conformité n'est pas de la défiance mais de l'ignorance : un ingénieur n'a jamais su que la règle existait ou n'a pas pu la localiser quand cela comptait. La considération concurrente est l'effort, puisque mettre en avant une norme dans le modèle de pull request, le message d'erreur du linter, et l'échafaudage du service coûte un vrai travail d'intégration qu'un site central unique ne demande pas. Apportez des preuves sur la repérabilité : comment les ingénieurs trouvent réellement les normes aujourd'hui, si une nouvelle recrue peut localiser la règle d'accessibilité ou de sécurité qui gouverne sa tâche en moins d'une minute, et à quelle fréquence les réviseurs citent une norme que l'auteur n'avait simplement pas vue. Pour une grande entreprise ou un organisme gouvernemental, les auditeurs demandent de plus en plus non seulement si une norme existe mais si elle a été communiquée et accessible au moment de la décision, donc traitez la mise en avant comme faisant partie de la norme, pas une réflexion après coup, et mesurez si les gens peuvent atteindre la règle quand ils en ont besoin.

5. **Qui possède chaque norme active, quand a-t-elle été révisée pour la dernière fois, et comment repéreriez-vous celles qui ont silencieusement pourri en folklore ?** Les normes se décomposent silencieusement : une règle écrite il y a trois ans pour un cadre que vous n'utilisez plus reste assise dans le catalogue, citée sélectivement et peu fiable, traînant vers le bas la crédibilité des normes encore justes. Pour une grande organisation, le coût de la propriété est la cadence de revue elle-même, qui semble être des frais généraux jusqu'à ce qu'une panne ou un audit expose une norme qui ne correspond plus à la réalité. Apportez les chiffres à la discussion : combien de normes ont un propriétaire nommé (un rôle, pas seulement un individu parti), combien ont été révisées l'an dernier, combien sont formellement dépréciées contre simplement obsolètes, et lesquelles sont les plus et les moins citées. Dans les contextes d'entreprise et gouvernementaux, un auditeur s'attend à ce que chaque norme soit versionnée, datée, et démontrablement actuelle, donc convenez d'une cadence de revue minimale, assignez à chaque norme un propriétaire responsable, et retirez celles qui ne justifient plus leur coût avant qu'elles ne sapent la confiance dans le reste.

6. **L'autorité d'accorder une dérogation est-elle réellement proportionnée au risque de la norme dérogée ?** Une déviation de style et une déviation de contrôle de sécurité ne sont pas la même décision, pourtant beaucoup d'organisations soit acheminent les deux vers un comité lourd (qui paralyse le travail légitime) soit laissent les deux passer par un seul tech lead (ce qui permet qu'un risque sérieux soit accepté par quelqu'un sans le mandat de l'accepter). La tension est la vitesse contre la responsabilité : trop de friction d'approbation entraîne la non-conformité silencieuse, tandis que trop peu signifie que des déviations conséquentes passent dans un fil de discussion. Apportez une carte de vos normes vers leurs autorités d'approbation, plus un échantillon de dérogations récemment accordées, et vérifiez si quelqu'un a dérogé à un contrôle critique pour la sûreté ou la sécurité sans le comité correspondant, le contrôle compensatoire, la mitigation, et l'acceptation de risque enregistrée. Pour l'entreprise et le gouvernement, c'est une question de séparation des tâches que les régulateurs scrutent directement, donc liez chaque classe de norme à une autorité nommée proportionnée à son risque, et assurez-vous que la personne acceptant un risque est réellement responsable des conséquences.

## Regard sectoriel

**Jeune pousse.** Gardez le catalogue minuscule : écrivez seulement la poignée de règles dont l'absence vous blesserait réellement, comme une configuration de formateur, une exigence de point de terminaison de vérification de santé, et des pages navigables au clavier, et appliquez chacune avec un linter ou un contrôle CI plutôt qu'une réunion de revue. Sautez entièrement le comité de dérogations ; un TODO daté dans le code et une note d'une ligne dans la pull request est une exception parfaitement bonne et bornée dans le temps à cette échelle. Votre ressource la plus rare est l'attention d'ingénierie, alors résistez à rédiger des normes pour des problèmes que vous n'avez pas encore.

**Petite entreprise.** Sans propriétaire de normes dédié et avec un budget serré, achetez vos normes plutôt que de les construire : adoptez des références publiées telles que le UK GDS Service Standard, les conseils de sécurité OWASP, ou les règles de lint recommandées de votre cadre, et appuyez-vous sur les contrôles déjà intégrés à vos outils et à votre CI hébergée. Gardez une courte page de règles locales pour les quelques choses réellement spécifiques à vous. Quiconque dirige l'ingénierie accorde et enregistre les exceptions dans le ticket, avec une date d'expiration, afin que même un processus léger reste honnête.

**Grande entreprise.** Le travail est la gouvernance à travers de nombreuses équipes : un catalogue, un modèle, une justification et des exemples pour chaque norme, et une politique en tant que code qui fait échouer le pipeline pour la majorité mécanique. Gérez un processus de dérogation dont l'autorité d'approbation est proportionnée au risque, bornez dans le temps chaque exception, révisez les dérogations ouvertes sur une cadence, et exploitez les dérogations récurrentes comme le signal qu'une norme doit changer. Mesurez la part de normes appliquées automatiquement et le volume et l'âge des dérogations ouvertes, et rapportez les deux à la fonction de gouvernance afin que les normes restent un système géré plutôt qu'un cimetière.

**Gouvernement.** Publiez vos normes d'ingénierie ouvertement dans la tradition DHCW et GDS, et associez chacune à une liste de contrôle que les équipes complètent avant une évaluation de service, afin que la conformité soit visible pour le public et les organismes de surveillance. Faites d'un propriétaire senior responsable nommé l'autorité pour les dérogations conséquentes, et exigez que chaque exception enregistre le critère spécifique, le contrôle compensatoire ou la mitigation provisoire, un plan de remédiation, et une expiration ferme. Les règles de marchés publics et de transparence signifient que vos normes et vos déviations font toutes deux partie du dossier public, alors traitez l'auditabilité et la traçabilité comme des exigences de conception dès le départ.

## Exemples

**Jeune pousse.** Une start-up de sept personnes garde exactement trois normes écrites (une configuration de formateur partagée, une exigence de point de terminaison de vérification de santé, et « toutes les pages publiques doivent être navigables au clavier »), chacune appliquée par un linter ou un contrôle CI plutôt qu'une réunion de revue. Quand une ingénieure a besoin de livrer un prototype jetable qui enfreint la règle de vérification de santé, il n'y a pas de comité de dérogations : elle laisse un TODO daté dans le code et une note d'une ligne dans la pull request expliquant pourquoi et quand elle le corrigera. C'est une exception bornée dans le temps à l'échelle d'une start-up, honnête et visible sans frais généraux de processus. Les trois contrôles se remboursent en gardant la revue de code portée sur le fond plutôt que le style.

**Grande entreprise.** Une banque mondiale maintient un manuel d'ingénierie interne d'environ quarante normes actives, chacune dans un modèle avec une justification, des exemples, et une liste de contrôle de bonnes pratiques liée. Environ 70 % sont appliquées automatiquement : formatage, politique de dépendances, métadonnées de service obligatoires, et contrôles de sécurité codés comme politique en tant que code qui fait échouer le pipeline CI. Une équipe de paiements doit livrer sur une base de données qui ne prend pas encore en charge une fonctionnalité de chiffrement mandatée. Plutôt que de bloquer la publication, elle dépose une dérogation nommant la norme, le contrôle compensatoire ([chiffrement](https://en.wikipedia.org/wiki/Encryption) au niveau de l'application), et une expiration de 90 jours. Le comité de sécurité l'accorde et l'enregistre. Quatre-vingt-dix jours plus tard, la revue trouve que la plateforme prend désormais en charge la fonctionnalité nativement, et la dérogation est clôturée. La norme a tenu, le travail a été livré, et la déviation est entièrement traçable pour le prochain audit.

**Gouvernement.** Une agence nationale de santé modelée sur l'approche DHCW et GDS publie ses normes d'ingénierie ouvertement, chacune associée à une liste de contrôle que les équipes complètent avant une évaluation de service. L'accessibilité aux WCAG 2.2 AA est une norme ferme, appliquée par un audit automatisé en CI plus une évaluation manuelle. Un système clinique hérité ne peut pas immédiatement satisfaire un critère d'accessibilité sans risquer une fonctionnalité critique pour la sécurité des patients. L'équipe demande une exception bornée dans le temps. Un propriétaire senior responsable nommé l'accorde, et enregistre le critère spécifique, la mitigation provisoire (une ligne téléphonique d'accès assisté), le plan de remédiation, et une expiration de six mois, créant exactement la preuve traçable et révisable que les organismes de surveillance exigent (chapitres 4.6, 10.4).

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Une norme coûte le temps de l'écrire, d'automatiser sa vérification, et de la maintenir. Le retour est payé chaque fois que le contrôle s'exécute, et chaque fois qu'un ingénieur n'a pas à s'arrêter et débattre d'une question réglée. Les normes convertissent un coût de décision récurrent et distribué en un coût de rédaction unique, la même économie que les registres de décision (chapitre 1.6), amplifiée parce qu'une norme gouverne des milliers d'instances futures, pas un choix passé.

Sur le **coût total de possession (TCO)**, le coût de vie complet de construire, exploiter, et maintenir un système, les normes abaissent les postes les plus importants : l'intégration (les nouvelles recrues héritent de la cohérence au lieu de la rétro-concevoir), la maintenance (le code uniforme est moins cher à changer), et l'assurance (les audits sont moins chers quand la conformité est vérifiable par machine et les déviations sont déjà documentées). Le processus d'exceptions protège ce retour sur investissement de sa principale menace : les normes se dégradant en folklore ignoré. Un processus de dérogation crédible garde les normes fiables, et les normes fiables sont celles que les gens suivent réellement. Le coût de sauter tout cela est invisible sur tout tableau de bord. Il apparaît comme une intégration lente, une qualité incohérente, et des conclusions d'audit, et il s'accumule à chaque nouvelle équipe et chaque départ.

## Anti-patterns et pièges

- **Règles sans justification :** une norme que personne ne comprend est une norme que personne ne peut appliquer correctement ni contester honnêtement.
- **Normes aspirationnelles et invérifiables :** « le code devrait être maintenable » est une valeur, pas une norme ; elle ne peut être ni appliquée ni contestée.
- **Aucun processus d'exceptions :** force un faux choix entre bloquer le travail légitime et tolérer la non-conformité silencieuse.
- **Exceptions permanentes :** des dérogations sans expiration qui deviennent silencieusement la vraie politique, non documentée.
- **Dérogations sans enregistrement :** des déviations accordées dans un couloir ou un fil de discussion, invisibles pour le prochain audit et le prochain ingénieur.
- **Ignorer le signal :** accorder la même exception à répétition au lieu de la lire comme la preuve que la norme doit changer.
- **Application par harcèlement :** compter sur les réviseurs pour attraper ce qu'un linter devrait, gaspillant le jugement sur le mécanique.
- **Cimetière de normes :** un catalogue écrit une fois, possédé par personne, jamais révisé, cité sélectivement, fiable pour peu.
- **Contrôle d'accès par jargon :** des normes écrites pour leurs auteurs plutôt que leurs lecteurs, sans exemples à copier.

## Modèle de maturité

- **Niveau 1 (Initiation) :** Les normes sont une connaissance tribale dans les têtes des ingénieurs seniors, appliquées réactivement. L'application est un harcèlement ad hoc en revue de code ; les déviations sont invisibles ; « la façon dont on le fait » varie selon l'équipe et qui a révisé le changement.
- **Niveau 2 (Développement) :** Certaines normes sont écrites, dans des formats incohérents et des emplacements dispersés, et l'adoption varie largement d'une équipe à l'autre. L'application est surtout manuelle. Les exceptions se produisent de manière informelle, sans enregistrement ni date d'expiration.
- **Niveau 3 (Standardisation) :** Un catalogue unique, un modèle, une justification et des exemples pour chaque norme, et des listes de contrôle de bonnes pratiques, appliqués de manière cohérente entre équipes. Application automatisée pour la majorité mécanique. Un processus d'exceptions documenté avec des approbateurs nommés, une justification enregistrée, et des dérogations bornées dans le temps.
- **Niveau 4 (Gestion) :** Le système de normes est mesuré par rapport à des références. Vous suivez la part de normes appliquées automatiquement contre par revue humaine, le volume de dérogations par norme, le temps de clôture, et combien de dérogations ont expiré en restant ouvertes, et vous rapportez cela à la fonction de gouvernance. L'autorité d'approbation est proportionnée au risque et auditée ; la cadence de revue et l'expiration sont appliquées sur preuve plutôt que sur bonne volonté ; une norme dont le taux de dérogation dépasse un seuil convenu est signalée pour révision.
- **Niveau 5 (Orchestration) :** Les normes sont mises en avant au moment du travail et appliquées par la politique en tant que code et les fonctions d'aptitude. Les dérogations sont exploitées comme signal afin que les exceptions récurrentes fassent continuellement évoluer les normes, et le catalogue est rééquilibré à mesure que la pratique change. Normes, listes de contrôle, et dérogations forment un seul système vivant et adaptatif intégré à travers l'intégration, la livraison, et l'audit.

## Pistes de réflexion

1. Lesquelles de vos normes pouvez-vous énoncer avec une règle testable *et* une justification claire, et lesquelles ne sont vraiment que des aspirations ?
2. Quelle part de vos normes est appliquée automatiquement contre par un réviseur qui remarque ? Que faudrait-il pour en déplacer dix de plus vers la CI ?
3. Où les déviations se produisent-elles aujourd'hui, et le sauriez-vous seulement ? Sont-elles enregistrées et bornées dans le temps, ou silencieuses ?
4. Qui est autorisé à accorder une dérogation contre votre norme la plus critique pour la sûreté ou la sécurité, et cette autorité est-elle proportionnée au risque ?
5. Regardez votre norme la plus dérogée. Est-ce un problème de discipline, ou la norme est-elle simplement fausse ?
6. Quand chaque norme active a-t-elle été révisée pour la dernière fois, et qui la possède ? Lesquelles sont silencieusement devenues folklore ?

## Points clés à retenir

- Une norme d'ingénierie est une **règle énoncée comme un résultat, avec une justification, des exemples, et une façon de la vérifier** : si elle ne peut pas être vérifiée, ce n'est pas encore une norme.
- Associez chaque norme à une **liste de contrôle de bonnes pratiques** pour que les gens puissent s'auto-vérifier, en suivant le modèle des manuels du secteur public (NHS Wales / DHCW, UK GDS).
- Stockez les normes dans le **contrôle de version**, gardez-les **vivantes** avec des propriétaires nommés et des dates de revue, et mettez-les en avant au moment du travail.
- **Automatisez le vérifiable** avec des linters, la politique en tant que code, et des fonctions d'aptitude ; réservez la **revue humaine** au jugement.
- Gouvernez les déviations avec un **processus d'exceptions/dérogations documenté et borné dans le temps** : approbateur nommé, justification enregistrée, expiration obligatoire, revue périodique.
- Une exception récurrente est un **signal pour corriger la norme**, pas seulement pour continuer d'accorder des dérogations : « l'exception confirme la règle ». Voir les chapitres 1.5 (gouvernance), 1.6 (registres de décision), 2.1 (normes de codage), 12.2 (listes de contrôle), et 12.3 (modèles).

## Références et lectures complémentaires

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice*, et *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* et conseils d'ingénierie.
- Digital Health and Care Wales (DHCW) / NHS Wales, normes d'ingénierie publiées et listes de contrôle de bonnes pratiques.
- Scott Bradner, *RFC 2119 : Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons, et Patrick Kua, *Building Evolutionary Architectures* (les fonctions d'aptitude comme gouvernance automatisée).
- Torin Sandall et al., documentation *Open Policy Agent* (politique en tant que code).
- GitLab, *The GitLab Handbook* : un exemple public de normes organisationnelles vivantes et sous contrôle de version.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright) : normes, lisibilité, et application automatisée à grande échelle.
- Atul Gawande, *The Checklist Manifesto* : l'argument des listes de contrôle comme pratique professionnelle.
