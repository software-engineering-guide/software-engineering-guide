# 2.7 Documentation

## Vue d'ensemble et motivation

La [documentation](https://en.wikipedia.org/wiki/Software_documentation) est la connaissance écrite qui laisse les gens utiliser, exploiter, et changer un logiciel sans avoir à reconstituer la compréhension à partir du seul code. Elle vient en de nombreux genres : comment démarrer, comment accomplir une tâche, comment un système est structuré, comment répondre à un incident, ce qu'une [API](https://en.wikipedia.org/wiki/API) accepte et retourne. Chacun sert un lecteur différent avec un besoin différent. Une bonne documentation n'est pas optionnelle. C'est la différence entre une connaissance qui passe à l'échelle à travers une grande organisation et une connaissance qui vit dans seulement quelques têtes.

Pour les grandes équipes, la documentation est votre meilleure défense contre le risque de personne-clé (le danger quand la connaissance critique repose sur une seule ou quelques personnes) et votre façon la plus rapide d'intégrer les nouvelles recrues. Quand des centaines d'ingénieurs dépendent de systèmes qu'ils n'ont pas construits, et que les gens rejoignent, bougent, et partent tout le temps, l'organisation ne peut fonctionner que si la connaissance est écrite et facile à trouver. Les systèmes non documentés deviennent fragiles : seuls leurs auteurs peuvent les changer en sécurité, et quand ces auteurs partent, l'organisation perd la capacité de maintenir son propre logiciel. C'est l'un des échecs les plus courants et coûteux à l'échelle.

Les contextes d'entreprise et gouvernementaux élèvent davantage les enjeux. Les systèmes vivent longtemps, donc votre documentation doit servir les mainteneurs des années, même des décennies, après que l'équipe d'origine soit partie. Les régimes réglementaires et d'audit mandatent souvent des documents spécifiques comme preuve de contrôle : dossiers d'architecture, [procédures d'exploitation](https://en.wikipedia.org/wiki/Runbook) (procédures opérationnelles et de réponse aux incidents étape par étape), et journaux de décision. Les systèmes du secteur public transmis entre fournisseurs dépendent entièrement de la documentation pour porter la connaissance à travers les frontières contractuelles. Et pourtant la documentation est notoirement encline à pourrir, donc le vrai défi est de la garder exacte à mesure que le logiciel change.

## Principes clés

- Écrivez pour un lecteur spécifique avec un besoin spécifique ; différents types de documentation servent différents buts.
- Gardez la documentation près du code et traitez-la comme du code (documentation comme code).
- L'exactitude l'emporte sur l'exhaustivité ; une petite quantité de documentation digne de confiance vaut mieux qu'une grande quantité fausse.
- Générez ce qui peut être généré ; ne maintenez pas à la main ce qu'un outil peut produire depuis la source de vérité.
- Combattez activement le pourrissement de documentation ; des documents obsolètes sont pires qu'aucun parce qu'ils induisent en erreur.
- Rendez la documentation repérable ; une connaissance introuvable est effectivement absente.
- Enregistrez les décisions et leur justification, pas seulement l'état actuel.

## Recommandations

### Adoptez la documentation comme code

Gardez la documentation dans le [contrôle de version](https://en.wikipedia.org/wiki/Version_control) juste à côté du code qu'elle décrit, écrivez-la en balisage texte brut, et révisez-la à travers le même processus de pull request. Cela la garde versionnée, révisable, et proche du code, afin que vous puissiez mettre à jour les deux ensemble. Publiez-la à travers un pipeline automatisé afin que la dernière version soit toujours disponible. Traiter la documentation comme du code apporte la même discipline qui garde le code digne de confiance : revue, historique, et automatisation.

### Structurez le contenu avec le cadre Diátaxis

Organisez la documentation en quatre types distincts, parce que les mélanger ne sert bien aucun lecteur : tutoriels (orientés apprentissage, pour les nouveaux arrivants), guides pratiques (orientés tâche, pour un objectif spécifique), référence (orientée information, précise et complète), et explication (orientée compréhension, le pourquoi et le contexte). Gardez-les séparés et tout devient plus facile à écrire, naviguer, et maintenir, parce que chaque page a un travail clair et une audience claire.

### Maintenez les documents opérationnels essentiels

Donnez à chaque dépôt un [README](https://en.wikipedia.org/wiki/README) clair comme sa porte d'entrée : ce que c'est, comment le construire et le faire fonctionner, et où aller ensuite. Écrivez des procédures d'exploitation pour les tâches opérationnelles et la réponse aux incidents, afin que quiconque est d'astreinte puisse agir, pas seulement les experts. Gardez une documentation d'architecture qui explique la structure du système et ses composants clés. Et fournissez une documentation d'intégration qui rend un nouvel ingénieur productif rapidement. Ce sont les documents qui vous manquent le plus quand ils ne sont pas là.

### Générez les documents d'API et les journaux de changements depuis la source de vérité

Générez votre documentation de référence d'API depuis le contrat lisible par machine ou les annotations de code, afin qu'elle ne puisse pas dériver de l'interface réelle. Gardez un [journal des changements](https://en.wikipedia.org/wiki/Changelog), idéalement généré depuis des commits structurés ou des notes de publication, afin que les consommateurs puissent voir ce qui a changé entre les versions. Automatiser cela retire de vos épaules la documentation maintenue à la main la plus encline au pourrissement et la garde digne de confiance.

### Enregistrez les décisions d'architecture

Capturez les décisions d'architecture et de conception significatives comme des enregistrements légers et datés qui énoncent le contexte, la décision, et ses conséquences. Ces registres de décision préservent la justification qui serait sinon perdue, afin que les futurs mainteneurs puissent voir pourquoi le système est ainsi au lieu de le remettre en question ou de répéter de vieilles erreurs. Ils se remboursent spécialement sur les longues durées de vie des systèmes d'entreprise et gouvernementaux.

### Combattez délibérément le pourrissement de documentation

Traitez la documentation obsolète comme un défaut. Mettez à jour les documents comme partie du même changement qui altère le comportement, et faites-en une attente de revue. Assignez la propriété afin que chaque document important ait quelqu'un de responsable pour lui. Révisez de temps en temps la documentation à haute valeur pour l'exactitude, élaguez ce qui est obsolète, et retirez ou signalez clairement tout ce en quoi vous ne faites plus confiance. La documentation qui pourrit le moins est la documentation vivante : générée ou testée contre le système lui-même.

### Investissez dans la gestion des connaissances et la repérabilité

Rendez la documentation trouvable à travers une bonne recherche, une navigation claire, et un foyer connu, afin que les gens puissent localiser ce dont ils ont besoin sans avoir à demander à quelqu'un. Ne la laissez pas se fragmenter à travers trop de wikis et d'outils déconnectés. Et capturez la [connaissance tacite](https://en.wikipedia.org/wiki/Tacit_knowledge), la compréhension informelle qui vit dans les fils de discussion et les têtes des gens, sous une forme durable et trouvable avant qu'elle ne s'échappe.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| Documentation comme code | Versionnée, révisable, proche du code ; faible pourrissement | Exige la discipline de l'ingénieur ; moins accueillante pour les auteurs non techniques |
| Wiki / base de connaissances | Facile à éditer ; accessible à tous | Dérive du code ; se fragmente ; pourrit silencieusement |
| Documents générés (API, journal de changements) | Toujours exacts ; faible maintenance | Limités à ce que la source exprime ; a besoin d'outillage |
| Explication écrite à la main | Contexte riche et justification que les machines ne peuvent pas produire | Intensive en travail ; encline à devenir obsolète |
| Structure Diátaxis | But clair par page ; plus facile à naviguer et maintenir | Effort de structuration initial ; exige la discipline de l'auteur |

Le compromis central est l'effort contre l'exactitude et la durabilité. La documentation la moins chère à écrire, une page de wiki rapide, est aussi la plus encline au pourrissement et à la fragmentation. La documentation la plus durable, générée depuis la source ou révisée comme du code, coûte plus de discipline en amont mais reste digne de confiance. Une bonne règle empirique : générez ce que vous pouvez, gardez le reste près du code et révisé comme du code, et réservez l'explication écrite à la main intensive en travail pour la justification que seuls les humains peuvent fournir.

## Questions à discuter avec votre équipe

1. **Vos documents sont-ils séparés par besoin de lecteur, ou les tutoriels, la référence, et l'explication s'entremêlent-ils sur une page ?** Ce chapitre recommande la division Diátaxis en tutoriels, guides pratiques, référence, et explication, et liste le mélange de types comme un anti-pattern qui ne sert bien aucun lecteur. À grande échelle, un nouvel arrivant apprenant le système et un ingénieur d'astreinte chassant un fait précis ont besoin de pages différentes, et une seule page mixte ralentit les deux. Apportez le signal : choisissez vos documents les plus visités et vérifiez si chacun a un travail clair et une audience claire. Restructurez les pires contrevenants en types distincts, afin que chaque page soit plus facile à écrire, naviguer, et garder à jour. Cette structure est ce qui rend la documentation maintenable à mesure que l'organisation grandit.

2. **Capturez-vous les décisions d'architecture significatives avec leur justification, ou seulement l'état actuel ?** Le chapitre recommande des registres de décision légers et datés qui énoncent le contexte, la décision, et les conséquences, et note qu'ils se remboursent le plus sur les longues durées de vie des systèmes d'entreprise et gouvernementaux. Sans eux, un mainteneur des années plus tard ne peut pas voir pourquoi le système est ainsi, donc il remet en question de bons choix ou répète de vieilles erreurs. Apportez une décision difficile récente dont le raisonnement ne vit maintenant que dans un fil de discussion ou la mémoire de quelqu'un comme signal concret. Adoptez un format de registre de décision court et faites d'en écrire un une partie de tout changement de conception significatif. La justification est exactement la connaissance que seuls les humains peuvent fournir et qui pourrit le plus vite quand elle n'est pas écrite.

3. **N'importe quel ingénieur d'astreinte peut-il répondre à un incident depuis vos procédures d'exploitation seules, sans appeler la personne qui a construit le système ?** Ce chapitre nomme les procédures d'exploitation comme un document opérationnel essentiel afin que quiconque est d'astreinte puisse agir, pas seulement les experts, et décrit une équipe gouvernementale qui n'a pu hériter d'un système que parce que les procédures d'exploitation portaient la connaissance à travers une frontière contractuelle. Le risque de personne-clé est l'échec contre lequel cela protège : quand l'unique expert est injoignable ou parti, une procédure de récupération non documentée transforme un incident routinier en panne. Apportez les preuves : prenez un incident récent et vérifiez si la procédure d'exploitation seule l'aurait résolu. Écrivez et testez des procédures d'exploitation pour les procédures que les gens redoutent, et traitez une procédure d'exploitation qui ne peut pas tenir seule comme un défaut. C'est la différence entre une récupération à deux heures du matin et une escalade à deux heures du matin.

4. **Lesquelles de vos références d'API et journaux de changements sont générés depuis la source de vérité, et lesquels sont encore maintenus à la main et dérivent silencieusement ?** Ce chapitre vous dit de générer la documentation de référence depuis le contrat lisible par machine ou les annotations de code afin qu'elle ne puisse pas diverger de l'interface réelle, et il liste le maintien à la main de contenu générable comme un anti-pattern. Pour une grande équipe, un document d'API écrit à la main qui retarde sur l'interface réelle est pire qu'aucun : chaque consommateur qui lui fait confiance écrit une intégration cassée, et l'échec surgit loin de la page obsolète qui l'a causé. Apportez le signal concret : échantillonnez une poignée de vos interfaces les plus utilisées et comparez la référence publiée au vrai contrat pour voir à quel point chacune a dérivé. Là où vous trouvez de la dérive, câblez la référence dans la construction afin qu'elle se régénère à chaque changement, et retirez la copie gardée à la main. Dans les contextes d'entreprise et gouvernementaux, où les interfaces sont consommées à travers des équipes, fournisseurs, et frontières contractuelles que vous ne voyez jamais, une référence générée faisant autorité est souvent la seule chose qui empêche les intégrateurs de construire contre de la fiction.

5. **Qui possède chaque document à haute valeur, et comment remarqueriez-vous aujourd'hui si l'un était devenu obsolète ?** Le chapitre traite la documentation obsolète comme un défaut et avertit que les documents sans propriétaire pourrissent parce que les mettre à jour n'est le travail de personne, tandis que des documents obsolètes présentés comme actuels détruisent la confiance dans toute votre documentation. À grande échelle, le danger n'est pas une seule mauvaise page mais l'érosion lente de la confiance : une fois que les lecteurs se sont fait brûler par des instructions obsolètes, ils cessent de faire confiance à tout le corpus et retournent interrompre les gens. Apportez une carte de propriété de vos documents les plus critiques et une réponse honnête à comment le pourrissement est détecté, que ce soit par cadence de revue, génération, tests contre le système, ou pure chance. Assignez un propriétaire nommé à chaque document qui compte, et préférez la documentation vivante qui est générée ou testée afin que l'obsolescence apparaisse mécaniquement plutôt que par un lecteur embarrassé. Pour les systèmes d'entreprise et gouvernementaux qui survivent à leurs équipes d'origine, la documentation sans propriétaire est un passif qu'un auditeur ou un fournisseur héritier vous facturera éventuellement.

6. **À quel point votre documentation est-elle repérable, et combien de connaissance critique vit encore seulement dans des fils de discussion et les têtes des gens ?** Ce chapitre dit qu'une connaissance introuvable est effectivement absente, avertit contre la fragmentation des documents à travers trop de wikis et d'outils déconnectés, et vous presse de capturer la connaissance tacite sous une forme durable et trouvable avant qu'elle ne s'échappe. Dans une grande organisation, le même fait est souvent redécouvert, redemandé, et re-répondu une centaine de fois parce que personne ne peut trouver où il a déjà été écrit, et chaque départ emporte un contexte irremplaçable. Apportez les preuves : comptez combien de foyers de documentation séparés vous maintenez, essayez de trouver trois faits importants par la seule recherche, et notez où les vraies réponses se sont avérées vivre dans la mémoire de quelqu'un ou un message enterré. Consolidez vers un foyer connu avec une vraie recherche et une navigation claire, et faites de la capture de connaissance tacite une partie routinière du travail plutôt qu'un sauvetage héroïque. Dans les contextes du secteur public et fortement externalisés, où les systèmes passent entre fournisseurs et équipes par contrat, la connaissance écrite repérable est la seule chose qui survit à la transition.

## Regard sectoriel

**Jeune pousse.** Avec une poignée d'ingénieurs et pas de trésorerie à épargner, documentez seulement ce dont une panne à deux heures du matin ou une nouvelle recrue aurait réellement besoin : un vrai README par service, une procédure d'exploitation testée pour la procédure de déploiement-et-récupération que tout le monde redoute, et quelques notes datées sur les décisions que vous oublieriez sinon. Générez les documents d'API depuis le contrat afin de ne jamais les maintenir à la main. Résistez à construire une plateforme de documentation ; un dossier versionné de balisage à côté du code suffit jusqu'à ce que vous ressentiez une vraie douleur.

**Petite entreprise.** Sans rédacteur technique et avec un budget serré, appuyez-vous sur la documentation que vos outils génèrent déjà et sur une documentation comme code légère plutôt qu'un programme doté en personnel. Cadrez le choix comme acheter contre construire : préférez les plateformes qui produisent leur propre référence actuelle et base de connaissances consultable à un wiki que vous devez entretenir à la main. Dépensez votre effort rare sur les deux ou trois documents dont l'absence arrêterait l'activité, et laissez une page fausse ou manquante être le déclencheur pour corriger la propriété.

**Grande entreprise.** À travers de nombreuses équipes, le problème est la cohérence et la repérabilité : un pipeline de documentation comme code partagé, une structure commune comme Diátaxis, des références d'API et journaux de changements générés, et des registres de décision appliqués de la même façon partout afin que la connaissance ne se fragmente pas à travers des dizaines de wikis. Assignez la propriété pour chaque document à haute valeur et mesurez l'exactitude, pas seulement la présence. Traitez les dossiers d'architecture, les procédures d'exploitation, et les journaux de décision comme preuve d'audit, et standardisez comment ils sont produits afin qu'une revue de contrôle trouve une piste documentée et défendable plutôt qu'une précipitation.

**Gouvernement.** Les règles de marchés publics et la responsabilité publique font de la documentation un livrable, pas une courtoisie. Écrivez la documentation d'architecture, les procédures d'exploitation, et les registres de décision dans les contrats comme artefacts mandatés, révisés pour l'exactitude afin que la connaissance survive à une transition de fournisseur et qu'un système puisse être exploité par quiconque en hérite. Exigez que tout opérateur autorisé puisse répondre à un incident depuis la procédure d'exploitation seule, et gardez les journaux de décision comme un enregistrement public transparent de pourquoi les choix ont été faits. Une documentation mince ici n'est pas un inconvénient privé ; elle devient une rétro-ingénierie coûteuse financée par le contribuable.

## Exemples

**Jeune pousse.** Une start-up de cinq personnes écrit un vrai README pour chaque service et une courte procédure d'exploitation pour l'unique procédure de déploiement-et-récupération que tout le monde redoute, afin qu'une panne à deux heures du matin ne dépende pas de réveiller l'unique fondateur qui connaît le système. Ils génèrent les documents d'API depuis le contrat au lieu de les écrire à la main, et notent quelques remarques datées expliquant pourquoi ils ont choisi leur base de données et leur approche d'authentification. Cela reste léger, mais cela signifie que les sixième et septième recrues s'intègrent depuis des documents plutôt qu'en interrompant tout le monde.

**Grande entreprise.** Une grande société de logiciels garde toute sa documentation dans les mêmes dépôts que son code, écrite en balisage et révisée dans des pull requests juste à côté des changements qu'elle décrit. Les références d'API sont générées depuis les contrats de service, donc elles ne dérivent jamais. Les journaux de changements sont générés depuis des commits structurés, et les registres de décision d'architecture préservent le raisonnement derrière les choix majeurs. Un site de documentation publié se construit automatiquement à chaque fusion. Les nouveaux ingénieurs deviennent productifs vite parce que les guides d'intégration et les procédures d'exploitation sont à jour et repérables, et les ingénieurs d'astreinte s'appuient sur les procédures d'exploitation au lieu d'appeler les auteurs d'origine.

**Gouvernement.** Une agence nationale hérite d'un système d'un contractant sortant, dépendant entièrement de la documentation pour porter la connaissance à travers la frontière contractuelle. Parce que le fournisseur précédent maintenait la documentation d'architecture, les procédures d'exploitation, et les registres de décision comme livrables mandatés, la nouvelle équipe peut exploiter et modifier le système sans les auteurs d'origine. Là où la documentation était mince, l'agence fait face à une rétro-ingénierie coûteuse. Cette expérience conduit une nouvelle politique : la documentation est un livrable contractuel, révisée pour l'exactitude plutôt que traitée comme une réflexion après coup, et les procédures d'exploitation doivent laisser tout opérateur autorisé répondre aux incidents.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La documentation vous rembourse en temps d'intégration plus court, moins de risque de personne-clé, une réponse aux incidents plus rapide, et un coût de changement plus bas sur la vie d'un système. Des nouveaux ingénieurs atteignant la productivité en jours plutôt qu'en semaines, du personnel d'astreinte résolvant les incidents depuis une procédure d'exploitation au lieu d'escalader, des mainteneurs changeant un système avec confiance des années après sa construction : ce sont de grandes économies récurrentes qui s'accumulent à travers une grande organisation et une longue durée de vie de système.

Que coûte la documentation ? L'effort de rédaction et de maintenance. Que coûte le fait de *ne pas* documenter ? Vous payez continuellement : en intégration lente, questions répétées, goulots d'étranglement de personne-clé, récupération d'incident plus lente, et, à l'extrême, des systèmes que personne ne peut changer en sécurité, forçant des réécritures coûteuses ou de la rétro-ingénierie. Dans les scénarios de transition de fournisseur et d'audit, la documentation manquante peut porter des coûts contractuels et de conformité directs. Pour convaincre la direction, mettez des chiffres sur le temps d'intégration, le temps de réponse aux incidents, et combien de connaissance critique repose dans des têtes individuelles. Puis cadrez la documentation comme code et la génération comme des façons d'obtenir une documentation durable sans un fardeau de maintenance correspondant. Et insistez que la documentation inexacte est un passif, donc l'investissement doit inclure la garder à jour.

## Anti-patterns et pièges

- **La documentation obsolète présentée comme actuelle :** induit les lecteurs en erreur et détruit la confiance dans toute la documentation.
- **Le wiki écrit-une-fois :** des pages créées et jamais mises à jour, dérivant silencieusement de la réalité.
- **La fragmentation de documentation :** connaissance éparpillée à travers de nombreux outils et wikis afin que rien ne puisse être trouvé.
- **Mélanger les types de documentation :** tutoriels, référence, et explication entremêlés sur une page, ne servant bien aucun lecteur.
- **Maintenir à la main du contenu générable :** des documents d'API écrits manuellement qui divergent inévitablement de l'interface réelle.
- **La connaissance tribale :** une compréhension critique gardée seulement dans les têtes des gens et l'historique de discussion, perdue quand ils partent.
- **La documentation comme réflexion après coup :** écrite à la fin, si tant est, plutôt qu'aux côtés du changement.
- **Aucune propriété :** des documents sans propriétaire responsable pourrissent parce que les mettre à jour n'est le travail de personne.

## Modèle de maturité

- **Niveau 1, Initiation.** La documentation est éparse, éparpillée, et obsolète, et la connaissance vit dans les têtes des gens. Ce qui existe a été écrit une fois et jamais retouché, donc une panne ou un départ signifie de la rétro-ingénierie du système.
- **Niveau 2, Développement.** Les documents clés existent, comme les README et quelques procédures d'exploitation, mais ils sont maintenus de façon incohérente et difficiles à trouver. Certaines équipes documentent bien et d'autres à peine, et il n'y a pas d'attente partagée sur ce qu'un dépôt devrait porter ou où cela devrait vivre.
- **Niveau 3, Standardisation.** La documentation comme code est la norme à travers l'organisation : une structure commune comme Diátaxis, des références d'API et journaux de changements générés, des registres de décision, et une attente en revue que les documents changent avec le code qu'ils décrivent. Chaque document à haute valeur a un propriétaire nommé, et il y a un foyer connu avec une vraie recherche.
- **Niveau 4, Gestion.** La documentation est mesurée, pas seulement présente. Vous suivez la couverture des documents essentiels, le taux de changement de documentation contre le taux de changement de code, le temps d'intégration, la résolution d'incident depuis les procédures d'exploitation seules, et la fraîcheur contre un seuil d'obsolescence défini, et vous révisez ces métriques par rapport à des références. Le pourrissement est attrapé mécaniquement à travers la génération, les tests contre le système, et les vérifications de liens et d'exactitude, et les pages obsolètes sont signalées ou élaguées sur preuve plutôt que par hasard.
- **Niveau 5, Orchestration.** La documentation est continuellement améliorée et intégrée à travers l'organisation : vivante, largement générée ou testée contre le système, possédée, repérable, et adaptative. Les métriques alimentent où vous investissez, la connaissance tacite est capturée comme une partie routinière du travail, et le corpus est activement rééquilibré et élagué à mesure que les systèmes, équipes, et lecteurs changent.

## Pistes de réflexion

- Quelle documentation, si elle disparaissait demain, blesserait le plus votre organisation, et existe-t-elle actuellement et reste-t-elle à jour ?
- Comment rendez-vous la mise à jour de documentation une partie naturelle du changement de code plutôt qu'une corvée séparée ?
- Où pouvez-vous remplacer la documentation écrite à la main par de la documentation générée liée à la source de vérité ?
- Comment mesurez-vous si votre documentation est exacte et utilisée, pas seulement présente ?
- Comment les assistants IA devraient-ils changer comment vous écrivez, maintenez, et recherchez la documentation, et où pourraient-ils introduire du contenu plausible-mais-faux ?
- Comment capturez-vous la connaissance tacite avant que les gens qui la détiennent ne partent ?

## Points clés à retenir

- Traitez la documentation comme du code : versionnée, révisée, proche de la source, et publiée automatiquement.
- Structurez le contenu selon le besoin du lecteur en utilisant tutoriels, guides pratiques, référence, et explication.
- Maintenez les essentiels à haute valeur : README, procédures d'exploitation, documents d'architecture, intégration, et registres de décision.
- Générez les documents d'API et journaux de changements afin qu'ils ne puissent pas dériver de la source de vérité.
- Combattez le pourrissement avec la propriété, les attentes de revue, et l'élagage ; une documentation inexacte est pire qu'aucune.

## Références et lectures complémentaires

- Daniele Procida, cadre de documentation *Diátaxis*
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* et guide Season of Docs (comme exemplaires de référence)
- Michael Nygard, *Documenting Architecture Decisions* (registres de décision d'architecture)
- Andrew Hunt et David Thomas, *The Pragmatic Programmer* (sur la connaissance et la documentation)
- *Keep a Changelog* (comme convention de référence)
