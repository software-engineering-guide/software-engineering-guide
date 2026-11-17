# 4.2 Sécurité applicative

## Vue d'ensemble et motivation

La sécurité applicative est là où les menaces abstraites rencontrent le code concret. La plupart des violations qui font les gros titres remontent à un défaut de couche application : une injection, un flux d'authentification cassé, un secret exposé, ou une dépendance compromise. Pour les grandes équipes livrant de nombreux services, la partie difficile n'est pas de savoir que ces défauts existent. C'est de les prévenir de façon cohérente à travers une base de code tentaculaire écrite par des milliers de mains sur de nombreuses années.

Pour les entreprises, la sécurité applicative est une question de confiance client et d'obligation réglementaire. Un défaut dans un flux de connexion ou un chemin de paiement peut déclencher la fraude, des amendes, et une divulgation de violation obligatoire. Les systèmes gouvernementaux font face aux mêmes risques techniques avec des données à enjeux plus élevés : éligibilité aux prestations, dossiers fiscaux, données de justice pénale, et infrastructure nationale. Dans les deux contextes, l'application est la porte d'entrée, et les attaquants la sondent constamment et automatiquement.

Ce chapitre couvre les pratiques qui gardent les applications résilientes : connaître et se défendre contre les classes de vulnérabilité courantes, valider l'entrée et encoder la sortie, bien faire l'authentification et l'autorisation, gérer les secrets, et sécuriser la chaîne d'approvisionnement logicielle qui détermine de plus en plus votre vraie surface d'attaque.

*Voir aussi :* le chapitre 4.1 (fondements de sécurité, modélisation de menace, et cycle de vie de développement sécurisé), le chapitre 10.3 (chaîne d'approvisionnement open source et licences), et le chapitre 10.2 (SBOM, risque, et assurance).

## Principes clés

- **Ne faites jamais confiance à l'entrée.** Traitez toutes les données traversant une frontière de confiance comme hostiles jusqu'à validation.
- **Valeurs par défaut sûres.** Le chemin sûr devrait être le chemin facile ; le comportement non sûr devrait exiger un effort délibéré et visible.
- **Échouez fermé.** Quand une vérification de sécurité ne peut pas se terminer, refusez l'accès plutôt que de l'autoriser.
- **Défense en profondeur à la couche application.** Combinez validation, encodage, paramétrisation, et protections de framework ; ne comptez pas sur une seule.
- **Moindre privilège pour les identités et jetons.** Délimitez étroitement les identifiants et faites-les expirer rapidement.
- **Vos dépendances sont votre code.** Vous êtes responsable de la sécurité de tout ce que vous livrez, incluant les composants tiers et open source.
- **Normes plutôt qu'improvisation.** Utilisez des frameworks vérifiés tels que l'ASVS de l'[OWASP](https://fr.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) plutôt que d'inventer vos propres contrôles de sécurité.

## Recommandations

### Connaître et défendre le Top 10 OWASP, vérifier avec ASVS

Le Top 10 OWASP est la liste de référence de l'industrie des risques les plus critiques d'application web : contrôle d'accès cassé, échecs cryptographiques, injection, conception non sûre, mauvaise configuration de sécurité, composants vulnérables, échecs d'authentification, échecs d'intégrité de données, échecs de journalisation, et falsification de requête côté serveur. Traitez-le comme un savoir requis pour chaque ingénieur, pas juste une référence de conformité à classer.

Pour une norme rigoureuse et testable, adoptez le **Application Security Verification Standard (ASVS) de l'OWASP**. ASVS définit des exigences de sécurité à trois niveaux d'assurance, vous donnant des contrôles concrets et auditables à concevoir et tester. Choisissez le niveau qui convient au risque de chaque application, et vérifiez-le contre lui.

### Valider l'entrée et encoder la sortie

Les défauts d'injection restent parmi les plus dommageables précisément parce qu'ils sont si faciles à introduire. Défendez-vous avec des contrôles stratifiés :

- **Validez l'entrée** contre des listes d'autorisation strictes (type attendu, longueur, format, plage). Rejetez plutôt que d'assainir là où vous le pouvez.
- **Utilisez des requêtes paramétrées** et des [instructions préparées](https://fr.wikipedia.org/wiki/Requ%C3%AAte_pr%C3%A9par%C3%A9e) pour tout accès à la base de données ; ne construisez jamais du SQL par concaténation de chaîne. Utilisez des constructeurs de requête sûrs et des ORM (mappeurs objet-relationnel) correctement.
- **Encodez la sortie** contextuellement. HTML, attributs HTML, JavaScript, URL, et CSS exigent chacun un encodage différent. Comptez sur l'auto-échappement du framework et comprenez ses limites.
- **Prévenez le [script intersite](https://fr.wikipedia.org/wiki/Cross-site_scripting) (XSS)** avec l'encodage de sortie plus une politique de sécurité de contenu forte comme seconde couche.
- **Prévenez l'injection de commande et de gabarit** en évitant d'appeler le shell avec des données non fiables et en utilisant des gabarits sans logique ou en bac à sable.

### Bien faire l'authentification et l'autorisation

L'authentification prouve qui est un utilisateur. L'autorisation décide ce qu'il peut faire. Les deux échouent souvent, donc bien les faire.

- Préférez les protocoles établis : **[OAuth 2.0](https://fr.wikipedia.org/wiki/OAuth)** pour l'autorisation déléguée et **[OpenID Connect](https://fr.wikipedia.org/wiki/OpenID_Connect) (OIDC)** pour l'authentification. Ne construisez pas ceux-ci à partir de zéro.
- Imposez l'**[authentification multifacteur](https://fr.wikipedia.org/wiki/Authentification_multifacteur) (MFA)**, spécialement pour l'accès privilégié et administratif.
- Stockez les mots de passe seulement comme hachages salés utilisant un algorithme moderne, lent, et difficile en mémoire (tel qu'[Argon2](https://fr.wikipedia.org/wiki/Argon2) ou [bcrypt](https://fr.wikipedia.org/wiki/Bcrypt)). Ne stockez ou journalisez jamais des identifiants en clair.
- Gérez les **sessions** soigneusement : générez des jetons cryptographiquement forts, fixez les drapeaux de cookie secure et HttpOnly, faites pivoter au changement de privilège, et faites expirer les sessions inactives.
- Imposez l'**autorisation côté serveur pour chaque requête**, vérifiant que le principal authentifié possède ou peut accéder à la ressource spécifique. L'autorisation cassée au niveau objet (accéder au dossier d'un autre utilisateur en changeant un ID) est l'un des défauts d'API les plus courants et sévères.
- Centralisez la logique d'autorisation là où pratique pour que la politique soit cohérente et auditable.

### Gérer les secrets et faire pivoter les clés

Les secrets codés en dur dans le code source sont une cause perpétuelle de violations. Construisez une habitude disciplinée autour de la gestion de secrets :

- Stockez les secrets dans un gestionnaire de secrets dédié ou coffre-fort, jamais dans la source, les fichiers de configuration, ou les variables d'environnement versionnées.
- Scannez les commits et dépôts pour les secrets divulgués automatiquement, et bloquez les fusions qui les introduisent.
- Faites pivoter les clés et identifiants régulièrement et immédiatement sur toute exposition suspectée. Préférez les identifiants de courte durée et émis automatiquement aux statiques de longue durée.
- Appliquez le moindre privilège à chaque secret : délimitez-le à exactement ce dont il a besoin.
- Chiffrez les secrets au repos et en transit, et auditez l'accès à eux.

### Sécuriser la chaîne d'approvisionnement logicielle

Les applications modernes sont surtout assemblées à partir de composants tiers, ce qui fait de la chaîne d'approvisionnement une surface d'attaque primaire.

- Maintenez une **[nomenclature logicielle](https://fr.wikipedia.org/wiki/Nomenclature_logicielle) (SBOM)** pour chaque application pour savoir exactement ce que vous livrez et pouvoir répondre rapidement quand une nouvelle vulnérabilité tombe.
- Scannez continuellement les dépendances (Software Composition Analysis, ou SCA) et remédiez promptement aux composants connus comme vulnérables.
- Épinglez et vérifiez les versions de dépendance ; utilisez des fichiers de verrouillage et des registres de confiance.
- Adoptez **SLSA** (Supply-chain Levels for Software Artifacts) pour élever l'intégrité de construction, et générez des attestations de **provenance** décrivant comment les artefacts ont été construits.
- **Signez les artefacts** et vérifiez les signatures avant le déploiement pour pouvoir faire confiance que ce qui fonctionne est ce que vous avez construit.
- Sécurisez le système de construction lui-même ; un pipeline CI compromis peut injecter du code malveillant dans chaque consommateur en aval.

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| Acheter/adopter un fournisseur d'identité (OIDC) | Éprouvé au combat, MFA intégré, moins de code à sécuriser | Dépendance fournisseur, effort d'intégration, coût |
| Construire une authentification personnalisée | Contrôle complet, aucune dépendance externe | Extrêmement facile à mal faire, maintenance élevée |
| Validation stricte par liste d'autorisation | Bloque des classes entières de vulnérabilité | Peut casser des cas limites légitimes, plus de travail en amont |
| Identifiants de courte durée | Petite fenêtre de violation, révocation automatique | Exige une infrastructure d'émission robuste |
| Mises à jour de dépendance agressives | Moins de vulnérabilités connues | Renouvellement, changements cassants potentiels, fardeau de test |
| SBOM + signature + provenance | Réponse d'incident rapide, confiance vérifiable | Investissement d'outillage et de processus, changement culturel |

Le compromis récurrent est la rigueur en amont contre l'exposition continue. Construire une authentification personnalisée ou sauter l'hygiène de dépendance semble plus rapide aujourd'hui et vous coûte énormément plus tard. Adopter des normes vérifiées et des contrôles de chaîne d'approvisionnement automatisés coûte de l'effort maintenant, mais transforme un risque non borné et imprévisible en un risque géré et borné. Pour les grandes équipes, le multiplicateur d'automatisation compte le plus : un contrôle appliqué une fois dans un gabarit de route pavée protège chaque service qui l'utilise.

## Questions à discuter avec votre équipe

1. **Quels contrôles ASVS intégrerez-vous dans votre framework de route pavée pour que les ingénieurs les obtiennent gratuitement ?** Le mouvement au plus grand levier pour une grande équipe est de faire du chemin sûr la valeur par défaut, pour qu'un contrôle écrit une fois dans un framework partagé protège chaque service qui l'adopte. Décidez quelles exigences ASVS (requêtes paramétrées, encodage de sortie, drapeaux de session sécurisés, vérifications d'autorisation côté serveur) appartiennent au gabarit plutôt qu'à la mémoire de chaque ingénieur. Pour les portefeuilles d'entreprise et gouvernementaux, décidez aussi quelles applications ont besoin d'ASVS niveau 2 contre niveau 3, et liez cela à la sensibilité des données que chacune touche. Apportez une liste de vos services et marquez lesquels héritent déjà de ces valeurs par défaut et lesquels réimplémentent la sécurité à la main, parce que ceux codés à la main sont là où se cachent l'injection et le contrôle d'accès cassé. Si les valeurs par défaut sûres ne vivent que sur une page de wiki, elles seront sautées sous pression de livraison, donc mettez-les dans le code.

2. **Comment trouverez-vous et corrigerez-vous l'autorisation cassée au niveau objet à travers chaque API, pas juste les nouvelles ?** Accéder au dossier d'un autre utilisateur en changeant un ID est l'un des défauts d'API les plus courants et sévères, et il se cache dans les anciens points de terminaison qui précèdent vos normes actuelles. L'autorisation côté serveur à chaque requête et chaque objet est la règle, mais la partie difficile est de vérifier qu'elle tient à travers une base de code tentaculaire et vieille de plusieurs années écrite par de nombreuses mains. Décidez si vous centraliserez la logique d'autorisation, ajouterez des tests automatisés qui tentent un accès inter-locataire, ou exécuterez un test ciblé contre vos API à plus haut risque en premier. Apportez votre inventaire de points de terminaison qui exposent des identifiants d'objet et classez-les par sensibilité de ce qu'ils renvoient. Sans un balayage délibéré, vous continuerez à livrer ce défaut et ne le découvrirez que quand un chercheur ou un attaquant le fera.

3. **Quel est votre plan pour la prochaine vulnérabilité de dépendance répandue : à quelle vitesse pouvez-vous trouver et corriger chaque service affecté ?** Quand un défaut critique tombe dans une bibliothèque populaire, les entreprises avec une SBOM précise identifient les services affectés en heures pendant que d'autres passent des semaines à chercher, et cet écart de vitesse décide combien de dommage vous prenez. Décidez maintenant si vous produisez une nomenclature logicielle pour chaque artefact, si le scan de dépendances fonctionne dans chaque pipeline, et qui possède la décision de correctif d'urgence. Pour les acheteurs régulés et gouvernementaux, les SBOM et la provenance signée sont de plus en plus une condition pour faire affaire, donc cette préparation protège aussi le revenu. Apportez la réponse honnête à un exercice : choisissez une bibliothèque que vous utilisez largement et chronométrez combien de temps il faut pour lister chaque service qui la livre. Si la réponse se mesure en jours, investissez dans l'inventaire et la signature avant que le prochain incident ne vous y force.

4. **Comment passerez-vous des secrets statiques de longue durée aux identifiants de courte durée émis automatiquement, et quels systèmes bloquent cela aujourd'hui ?** Les secrets codés en dur et de longue durée sont une cause perpétuelle de violation, et la correction, des identifiants de courte durée émis à la demande, dépend d'une infrastructure d'émission que les anciens systèmes ne peuvent souvent pas utiliser. Pour une grande équipe, le danger est une adoption inégale : une plateforme moderne fait pivoter les clés toutes les heures pendant qu'un service hérité livre encore un mot de passe de base de données statique dans un fichier de configuration. Décidez quelles charges de travail peuvent consommer un gestionnaire de secrets ou un système d'identité de charge de travail maintenant, lesquelles ont besoin d'investissement d'abord, et qui possède le manuel de rotation au moment où une clé est suspectée divulguée. Apportez un inventaire de chaque identifiant en usage, sa durée de vie, son rayon d'impact si exposé, et si le scan de commit l'attraperait avant fusion. Dans les contextes d'entreprise et gouvernementaux, liez cela à l'audit : les examinateurs attendent de plus en plus une preuve de rotation, d'accès délimité, et de journalisation d'accès pour chaque secret, et un identifiant statique que vous ne pouvez pas faire pivoter sans temps d'arrêt est une constatation qui attend d'être écrite.

5. **Où exécutez-vous encore une authentification maison ou incohérente, et quel est le plan pour consolider sur des protocoles vérifiés ?** Construire l'authentification est l'un des moyens les plus faciles d'introduire des défauts subtils et exploitables, pourtant la plupart des grands parcs portent au moins un flux de connexion hérité qui précède la décision de se standardiser sur OAuth 2.0 et OIDC. Les pressions concurrentes sont réelles : migrer un ancien flux risque de casser les utilisateurs et intégrations existants, tandis que le laisser en place garde une cible de haute valeur sous-défendue. Décidez si vous consolidez sur un seul fournisseur d'identité, imposez le MFA uniformément, et fixez une échéance pour retirer chaque flux sur mesure, ou acceptez des exceptions documentées avec des contrôles compensatoires. Apportez une carte de chaque chemin d'authentification dans la flotte, lesquels imposent le MFA, lesquels stockent les mots de passe avec un hachage moderne difficile en mémoire, et lesquels sont personnalisés. Pour les portefeuilles d'entreprise et gouvernementaux, ajoutez l'angle de conformité : des normes telles que NIST SP 800-63 fixent des attentes concrètes pour l'assurance d'identité, et un flux maison qui ne peut pas les démontrer ne survivra pas à un audit ou une revue d'autorisation d'exploiter.

6. **Comment vérifiez-vous que ces contrôles tiennent réellement en production, et pouvez-vous le prouver avec des preuves plutôt qu'une affirmation ?** Écrire une valeur par défaut sûre n'est pas la même chose que savoir que chaque service l'honore encore, et les contrôles pourrissent discrètement à mesure que le code change, que les exceptions s'accumulent, et que de nouveaux points de terminaison sont livrés. Pour une grande équipe, la question est la couverture : quels services exécutent l'analyse statique, le scan de dépendances, et le test dynamique ou d'intrusion, et comment savez-vous que ceux qui les sautent ne sont pas vos applications à plus haut risque ? Décidez ce qui est obligatoire dans le pipeline contre périodique, qui trie les constatations, et quelle preuve vous retenez pour montrer qu'un contrôle a été testé et réussi à une date donnée. Apportez votre carte de couverture actuelle, votre temps moyen de remédiation par sévérité, et la liste des applications sans test récent. Dans les contextes régulés et gouvernementaux, cette preuve n'est pas optionnelle : les auditeurs, les fonctionnaires autorisateurs, et les enquêteurs de violation demandent tous une preuve que les contrôles ont été vérifiés, et une politique sans enregistrements de test les satisfait rarement.

## Regard sectoriel

**Jeune pousse.** Avec deux ou trois ingénieurs et aucun spécialiste de sécurité, votre levier est d'hériter la sécurité plutôt que de la construire : adoptez un fournisseur d'identité OIDC géré, appuyez-vous sur un framework dont l'ORM paramètre les requêtes par défaut, et gardez les secrets dans le gestionnaire de secrets de votre plateforme plutôt que des fichiers `.env` qu'un coéquipier pourrait commettre par accident. Activez le scan de dépendances automatisé qui ouvre des demandes de tirage de correctif, et traitez cela comme suffisant pour l'instant. Ne construisez pas d'authentification ou de cryptographie personnalisée, parce qu'une seule requête injectée ou une clé divulguée peut mettre fin à l'entreprise avant qu'elle n'ait de clients.

**Petite entreprise.** Vous n'avez probablement pas de spécialiste de sécurité applicative et un budget serré, donc achetez des contrôles intégrés dans les outils et plateformes que vous payez déjà plutôt que de doter une fonction dédiée en personnel. Choisissez un fournisseur d'identité hébergé avec MFA inclus, une base de données gérée qui vous guide vers un accès paramétré, et un hébergeur de dépôt qui scanne les commits pour les secrets divulgués prêt à l'emploi. Concentrez votre attention rare sur les bases du Top 10 OWASP qui causent la plupart des violations du monde réel, et préférez les fournisseurs qui livrent des valeurs par défaut sûres que vous ne pouvez pas désactiver négligemment.

**Grande entreprise.** À travers de nombreuses équipes, le défi est la cohérence : intégrez les contrôles ASVS dans les frameworks de route pavée pour que chaque nouveau service hérite gratuitement de requêtes paramétrées, d'encodage de sortie, de sessions sécurisées, et d'autorisation côté serveur. Exécutez des SBOM précises et un scan de dépendances à l'échelle de la flotte pour que la prochaine vulnérabilité de bibliothèque répandue soit une question d'heures, pas de semaines, et centralisez la politique d'autorisation pour que l'accès inter-locataire devienne testable. Standardisez sur un fournisseur d'identité avec MFA imposé, et gérez la sécurité applicative comme un portefeuille gouverné avec des niveaux ASVS échelonnés par risque et une preuve auditée.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la redevabilité publique façonnent les contrôles que vous devez démontrer, pas simplement implémenter. Vérifiez les services orientés citoyens contre l'ASVS OWASP à un niveau assorti à la sensibilité des données, signez chaque artefact déployé et attestez sa provenance selon SLSA pour satisfaire les mandats de chaîne d'approvisionnement, et émettez des identifiants de courte durée depuis un coffre-fort central avec journalisation d'accès complète. Attendez-vous à montrer aux auditeurs et fonctionnaires autorisateurs une chaîne de possession documentée de la source à la production, et alignez l'assurance d'identité sur des normes publiées telles que NIST SP 800-63.

## Exemples

**Jeune pousse.** Une équipe SaaS de trois ingénieurs saute la construction de sa propre connexion et adopte un fournisseur OIDC géré dès le premier jour, gagnant le MFA et des réinitialisations de mot de passe sûres sans écrire de code critique pour la sécurité qu'elle ne peut pas se permettre de mal faire. Elle s'appuie sur l'ORM du framework pour que les requêtes soient paramétrées par défaut, garde les secrets dans le gestionnaire de secrets de la plateforme plutôt que dans des fichiers `.env` qu'un coéquipier pourrait commettre par accident, et active le scan de dépendances automatisé qui ouvre une demande de tirage quand une bibliothèque a besoin d'être corrigée. Rien de tout cela ne ralentit l'équipe, et cela signifie qu'une clé divulguée ou une requête injectée ne met pas fin à l'entreprise avant qu'elle n'ait de clients.

**Grande entreprise.** Une plateforme de vente au détail servant des dizaines de millions d'acheteurs standardise l'authentification sur OIDC à travers un seul fournisseur d'identité, imposant le MFA pour le personnel et l'authentification renforcée pour les changements de compte à haute valeur. Tout l'accès à la base de données passe par un ORM configuré pour paramétrer les requêtes, et une politique de sécurité de contenu soutient l'encodage de sortie. Après une vulnérabilité largement publicisée dans une bibliothèque de journalisation populaire, la SBOM de l'entreprise lui permet d'identifier chaque service affecté en quelques heures et de les corriger en deux jours, pendant que les concurrents sans inventaires passent des semaines à chercher.

**Gouvernement.** Une agence fédérale de prestations construit des services orientés citoyens vérifiés contre l'ASVS OWASP niveau 2, avec le niveau 3 pour les composants gérant les dossiers les plus sensibles. Les secrets vivent dans un coffre-fort central émettant des identifiants de courte durée ; le scan de commit bloque toute clé divulguée. Chaque artefact déployé est signé et sa provenance attestée selon SLSA, satisfaisant un mandat fédéral pour des chaînes d'approvisionnement logicielles vérifiables et donnant aux auditeurs une chaîne de possession claire de la source à la production.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La dépense de sécurité applicative rachète la catégorie de violation la plus probable et la plus coûteuse. Le coût total de possession inclut l'outillage (scanners, gestionnaires de secrets, fournisseurs d'identité), le temps d'ingénieur pour remédier aux constatations, et la friction légère des valeurs par défaut sûres. Contre cela, pesez le coût de le sauter : les violations d'injection et de contrôle d'accès cassé exposent couramment des millions d'enregistrements, déclenchant des amendes réglementaires, une notification obligatoire, des pertes de fraude, des sprints de remédiation, et un dommage réputationnel qui supprime le revenu pendant des années.

Le ROI est le plus fort quand les contrôles sont automatisés et réutilisés. Une seule intégration d'identité bien configurée, une couche de requête durcie dans un framework partagé, et un pipeline qui bloque les dépendances vulnérables protègent toute la flotte à coût marginal par service. Les contrôles de chaîne d'approvisionnement en particulier sont passés d'optionnels à essentiels : une dépendance compromise peut transformer chacun de vos clients en victime, et les régulateurs et acheteurs d'entreprise exigent de plus en plus des SBOM et une provenance signée comme condition pour faire affaire. Quand vous faites valoir cela auprès de la direction, liez l'investissement à des risques spécifiques et nommés et à des exigences d'approvisionnement et de conformité qui bloquent le revenu si vous ne les satisfaites pas.

## Anti-patterns et pièges

- **Coder sa propre cryptographie ou authentification.** Produit presque toujours des défauts subtils et exploitables.
- **Validation côté client seulement.** Trivialement contournée ; le serveur doit tout revalider.
- **Assainissement par liste de blocage.** Essayer de retirer les « mauvais » caractères au lieu de mettre sur liste d'autorisation les bons ; les attaquants trouvent les lacunes.
- **Secrets dans la source ou les fichiers d'environnement.** La cause la plus courante de divulgation d'identifiant.
- **Ignorer l'autorisation sur l'accès à l'objet.** Supposer qu'un utilisateur authentifié peut accéder à tout objet dont il peut deviner l'ID.
- **Dépendances fixées et oubliées.** Ne jamais mettre à jour les composants tiers jusqu'à ce qu'une violation le force.
- **Traiter le Top 10 comme la ligne d'arrivée.** C'est un plancher, pas une norme complète ; utilisez ASVS pour la profondeur.
- **Journaliser des données sensibles.** Mots de passe, jetons, et DIP (données identifiantes personnelles) dans les journaux deviennent une violation qui attend de se produire.

## Modèle de maturité

**Niveau 1 : Initier.** La sécurité applicative dépend de la connaissance individuelle des développeurs et réagit seulement après les incidents. Aucun contrôle standard. Les secrets se trouvent dans la source. Les dépendances sont rarement mises à jour. L'authentification est personnalisée et ad hoc, et les défauts d'injection ou de contrôle d'accès cassé sont trouvés par chance plutôt que par processus.

**Niveau 2 : Développer.** Des pratiques de base apparaissent mais varient d'équipe à équipe. La conscience du Top 10 OWASP se répand, certaines protections au niveau framework sont en place, et un gestionnaire de secrets existe mais est utilisé de façon inégale. Le scan de dépendances fonctionne occasionnellement. Les nouveaux systèmes adoptent un fournisseur d'identité standard, tandis que les services plus anciens gardent leurs flux de connexion maison intacts.

**Niveau 3 : Standardiser.** Les contrôles sont documentés et imposés à travers l'organisation. Les exigences fondées sur ASVS sont fixées par palier de risque, les requêtes paramétrées et l'encodage de sortie sont la norme, et un fournisseur d'identité central avec MFA est exigé. Les secrets sont gérés et scannés automatiquement, les SBOM sont produites, et le scan de dépendances fonctionne dans chaque pipeline.

**Niveau 4 : Gérer.** La pratique est mesurée et contrôlée par rapport à des références. La couverture de scan et de test, le temps moyen de remédiation par sévérité, la part de services héritant des valeurs par défaut de route pavée, l'âge de rotation des identifiants et secrets, et la conformité ASVS sont tous suivis sur des tableaux de bord. Les exceptions sont consignées avec des dates d'expiration, la dérive par rapport à la référence déclenche une action, et les livraisons sont conditionnées à des seuils de sécurité définis plutôt qu'à des appels de jugement.

**Niveau 5 : Orchestrer.** La sécurité est continuellement améliorée et intégrée à travers l'organisation. Les valeurs par défaut sûres sont intégrées dans les frameworks de route pavée pour que le chemin sûr soit automatique, les identifiants de courte durée sont utilisés partout, et l'assurance complète de chaîne d'approvisionnement avec signature et provenance (SLSA) est standard. La vérification est continue, la réponse aux nouvelles vulnérabilités est rapide et mesurée, et chaque incident alimente en retour les gabarits partagés pour qu'une seule correction durcisse toute la flotte.

## Pistes de réflexion

1. Où la logique d'autorisation devrait-elle vivre pour être à la fois cohérente et maintenable à travers de nombreux services ?
2. À quel point devriez-vous mettre à jour agressivement les dépendances étant donné le compromis entre exposition et renouvellement ?
3. Quel niveau ASVS convient à chaque classe d'application dans votre portefeuille ?
4. Comment éliminez-vous les secrets de longue durée sans créer une infrastructure d'émission fragile ?
5. Que faudrait-il à votre organisation pour produire et consommer des SBOM et de la provenance pour chaque artefact ?
6. Comment empêchez-vous les valeurs par défaut sûres d'être désactivées sous pression de livraison ?

## Points clés à retenir

- Le Top 10 OWASP est un savoir essentiel ; ASVS fournit la norme testable.
- Stratifiez la validation d'entrée, la paramétrisation, et l'encodage de sortie pour vaincre l'injection et le XSS.
- Utilisez des protocoles vérifiés (OAuth 2.0, OIDC) et imposez le MFA ; ne construisez jamais l'authentification à partir de zéro.
- Imposez l'autorisation côté serveur pour chaque requête et chaque objet.
- Gardez les secrets hors de la source, gérez-les centralement, et faites-les pivoter vers des identifiants de courte durée.
- La chaîne d'approvisionnement est une surface d'attaque primaire ; utilisez SBOM, SCA, signature, et provenance (SLSA).
- Des contrôles automatisés et réutilisables protègent toute la flotte à coût marginal par service.

## Références et lectures complémentaires

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Validation d'entrée, Authentification, Autorisation, Gestion des secrets)
- Dafydd Stuttard et Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation et OpenSSF, cadre *SLSA* et guidance *Supply-chain Security*
