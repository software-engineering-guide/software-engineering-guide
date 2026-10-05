# 4.8 Cryptographie et gestion des clés

## Vue d'ensemble et motivation

Presque chaque système que vous construisez dépend déjà de la [cryptographie](https://fr.wikipedia.org/wiki/Cryptographie), la pratique de protéger l'information en utilisant des techniques mathématiques pour que seules les parties prévues puissent la lire ou lui faire confiance. Votre trafic web roule sur des canaux chiffrés, vos mots de passe sont hachés, vos mises à jour logicielles sont signées, et les données de vos clients se trouvent chiffrées sur disque. La bonne nouvelle pour la plupart des ingénieurs est qu'on ne vous demande pas d'inventer quoi que ce soit de tout cela. La partie difficile n'est pas les mathématiques. C'est d'utiliser correctement des blocs de construction vérifiés et, par-dessus tout, de gérer les clés dont ces blocs de construction dépendent.

Ce chapitre est écrit pour les ingénieurs qui ne sont pas cryptographes, ce qui est presque nous tous. Vous avez besoin d'assez de compréhension pour faire des choix solides, pour savoir ce que chaque outil garantit, et pour éviter les erreurs qui transforment des algorithmes forts en fausse tranquillité. Le chapitre 4.3 (sécurité d'infrastructure et cloud) mentionne le chiffrement et la gestion de clés en passant ; ici nous allons plus profond dans quoi chiffrer, comment, et comment exploiter le cycle de vie des clés qui rend cela réel.

Pour les grandes entreprises, la cryptographie se répand à travers des milliers de services, certificats, et clés, et un seul certificat expiré ou une clé perdue peut faire tomber un système critique ou faire fuir un magasin de données. Pour l'administration publique, la cryptographie est souvent mandatée, validée, et auditée, avec des règles de classification de données qui dictent exactement quelles clés protègent quels secrets et qui peut les détenir. Dans les deux contextes, l'échec récurrent est le même : de bons algorithmes défaits par une gestion de clé négligée.

## Principes clés

- **Ne codez pas votre propre cryptographie.** Utilisez des bibliothèques vérifiées et largement relues et des algorithmes standard. Les schémas nouveaux échouent de façons que seuls les experts attrapent.
- **Les algorithmes sont la partie facile ; les clés sont la partie difficile.** Le cycle de vie d'une clé est là où vivent la plupart des échecs du monde réel.
- **Sachez ce que chaque primitive garantit.** La confidentialité, l'intégrité, et l'authenticité sont des propriétés différentes exigeant des outils différents.
- **Chiffrez en transit et au repos par défaut.** Faites de la protection la norme, pas un opt-in.
- **Séparez la garde de clé de l'accès aux données.** Quiconque gère une clé ne devrait pas automatiquement pouvoir lire les données qu'elle protège.
- **Planifiez pour le changement.** Les algorithmes s'affaiblissent, les clés fuient, et les normes évoluent. Construisez pour la rotation et la migration dès le premier jour.
- **Préférez les implémentations validées là où cela compte.** Pour le travail régulé et gouvernemental, choisissez des modules avec une validation reconnue.

## Recommandations

### Ne pas coder votre propre cryptographie

C'est la règle d'or, et elle mérite d'être énoncée en premier. Ne concevez jamais votre propre algorithme de chiffrement, n'inventez jamais votre propre protocole, et n'implémentez jamais à la main une primitive à partir d'un article. La cryptographie qui fonctionne semble simple et cache des modes d'échec subtils (canaux latéraux de minutage, oracles de remplissage, aléa faible) qui ne survivent qu'à des années de relecture experte. Utilisez des bibliothèques établies telles que le module cryptographique standard de votre plateforme ou une bibliothèque bien considérée, et utilisez-les au plus haut niveau d'abstraction disponible. Recourez aux modes de chiffrement authentifié et aux interfaces « faciles » qui font du choix sûr la valeur par défaut, plutôt que d'assembler vous-même des pièces de bas niveau.

### Assortir la primitive à la garantie dont vous avez besoin

Différents outils fournissent différentes garanties, et les confondre est une erreur courante et dangereuse. Apprenez les trois familles principales.

- La cryptographie **[à clé symétrique](https://fr.wikipedia.org/wiki/Cryptographie_sym%C3%A9trique)** utilise une clé secrète partagée pour à la fois chiffrer et déchiffrer. Elle est rapide et protège la **confidentialité**, mais les deux parties doivent déjà partager la clé. AES est le cheval de trait standard.
- La cryptographie **[à clé publique](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique)** utilise une paire de clés mathématiquement liées : une clé publique que quiconque peut détenir et une clé privée que vous gardez secrète. Elle résout la distribution de clé et permet les **signatures numériques**, qui prouvent l'**authenticité** (qui l'a envoyé) et l'**intégrité** (qu'elle n'a pas été altérée).
- Une **[fonction de hachage cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)** produit une empreinte de taille fixe des données et fournit une vérification d'**intégrité**. Le hachage est à sens unique et n'est pas du chiffrement. Pour stocker des mots de passe, utilisez une fonction de hachage de mot de passe lente et salée, jamais un hachage rapide et simple (voir chapitre 4.2 sur la sécurité applicative).

La leçon pratique : le chiffrement cache les données mais ne prouve pas qui les a envoyées, et un hachage détecte la falsification mais ne cache rien. La plupart des vrais systèmes les combinent, ce qui est exactement pourquoi vous devriez vous appuyer sur des bibliothèques qui les regroupent correctement.

### Chiffrer en transit avec TLS actuel

Protégez chaque saut réseau avec le [Transport Layer Security](https://fr.wikipedia.org/wiki/Transport_Layer_Security) (TLS), le protocole qui sécurise les données pendant qu'elles se déplacent entre systèmes. Exigez des versions TLS modernes, désactivez les obsolètes, choisissez des suites de chiffrement fortes, et validez les certificats correctement plutôt que de désactiver les vérifications pour « faire fonctionner ». Chiffrez aussi le trafic interne service-à-service, pas seulement la périphérie publique, parce qu'une posture zéro confiance suppose que le réseau interne est hostile. Automatisez l'émission et le renouvellement de certificat pour que TLS soit la valeur par défaut sans effort partout.

### Chiffrer au repos avec le chiffrement d'enveloppe

Chiffrez les données stockées par défaut : bases de données, stockage d'objets, sauvegardes, et journaux. Le motif standard est le **chiffrement d'enveloppe**, où une **clé de chiffrement de données (DEK)** chiffre les données réelles, et une **clé de chiffrement de clé (KEK)** détenue dans un service de gestion de clés chiffre la DEK. Cela vous permet de faire pivoter la clé maîtresse sans rechiffrer des téraoctets de données, et cela garde la puissante clé racine à l'intérieur d'une frontière durcie. Stockez seulement la DEK enveloppée aux côtés des données, et récupérez-la et déballez-la au moment de l'usage.

### Exploiter délibérément le cycle de vie de clé

Le cycle de vie d'une clé est la partie vraiment difficile de la cryptographie, et là où proviennent la plupart des violations et pannes du monde réel. Gérez chaque étape délibérément :

- **Génération :** créez des clés à partir d'une source aléatoire forte, à une force appropriée.
- **Distribution :** amenez les clés aux systèmes qui en ont besoin sans les exposer dans le code, les fichiers de configuration, ou le chat.
- **Rotation :** remplacez les clés selon un calendrier, et soyez capable de faire pivoter rapidement en cas de compromission suspectée.
- **Révocation :** invalidez rapidement une clé ou un certificat compromis, et assurez-vous que les systèmes honorent la révocation.
- **Destruction :** retirez de façon sûre l'ancien matériel de clé pour qu'il ne puisse pas être récupéré.

Utilisez un **service de gestion de clés (KMS)** pour centraliser cela, et utilisez un [module de sécurité matériel](https://fr.wikipedia.org/wiki/Module_mat%C3%A9riel_de_s%C3%A9curit%C3%A9) (HSM), un dispositif résistant à la falsification qui génère et garde les clés pour qu'elles ne quittent jamais en clair, pour vos clés à plus haute assurance. Séparez qui peut gérer les clés de qui peut lire les données protégées, pour que la garde de clé impose la séparation des tâches. Cela se rattache directement aux règles de classification et de garde de données du chapitre 4.5 (confidentialité et protection des données).

### Distinguer la gestion de secrets de la gestion de clés

Ceux-ci se chevauchent mais ne sont pas la même chose. La **gestion de clés** gouverne les clés cryptographiques et leur cycle de vie, généralement à l'intérieur d'un KMS ou HSM qui effectue les opérations cryptographiques pour vous pour que la clé brute ne quitte jamais. La **gestion de secrets** gouverne les identifiants d'application (mots de passe de base de données, jetons API, certificats) que les services ont besoin de récupérer et utiliser en clair, généralement depuis un coffre-fort de secrets avec un accès de courte durée et audité. Utilisez un KMS pour les clés, un gestionnaire de secrets pour les identifiants, et ne collez jamais l'un ou l'autre dans le code source ou les fichiers d'environnement versionnés.

### Automatiser la PKI et les cycles de vie de certificat

L'**infrastructure à clé publique (PKI)** est le système d'autorités de certification, certificats, et chaînes de confiance qui lie les clés publiques aux identités. À l'échelle, le risque PKI dominant est l'expiration surprise de certificat qui fait tomber un service. Maintenez un inventaire de chaque certificat, surveillez les expirations, et automatisez l'émission et le renouvellement pour qu'aucun humain n'ait à s'en souvenir. Les certificats de courte durée renouvelés automatiquement sont plus sûrs que les longue durée entretenus à la main, parce que l'automatisation retire le point de défaillance unique humain. Les protocoles standard ici soutiennent l'interopérabilité à travers les fournisseurs (chapitre 3.8 sur l'interopérabilité et les normes ouvertes).

### Construire pour l'agilité cryptographique et la migration post-quantique

Les algorithmes s'affaiblissent avec le temps, et les normes bougent. L'**agilité cryptographique** signifie concevoir des systèmes pour pouvoir échanger algorithmes et tailles de clé sans réécriture pénible : abstrayez la cryptographie derrière une petite interface, versionnez vos données chiffrées pour savoir quel algorithme les a produites, et gardez un inventaire cryptographique de ce que vous utilisez où. Cela compte maintenant à cause de la [cryptographie post-quantique](https://fr.wikipedia.org/wiki/Cryptographie_post-quantique), la nouvelle famille d'algorithmes conçus pour résister aux futurs ordinateurs quantiques. Les adversaires peuvent récolter des données chiffrées aujourd'hui pour les déchiffrer plus tard, donc les secrets de longue durée ont besoin d'un plan de migration. Vous n'avez pas besoin de paniquer, mais vous devriez connaître votre inventaire et être prêt à adopter les algorithmes post-quantiques standardisés à mesure que les plateformes les livrent.

### Préférer les implémentations validées là où requis

Pour les systèmes régulés et gouvernementaux, utiliser un algorithme fort ne suffit pas ; l'implémentation doit être validée. **FIPS 140** (Federal Information Processing Standard 140) est la norme américaine pour valider les modules cryptographiques, et de nombreux contrats exigent une cryptographie validée FIPS. Le travail gouvernemental peut aussi suivre une guidance nationale telle que la suite Commercial National Security Algorithm (CNSA) de la NSA pour les systèmes classifiés. Vérifiez quel régime s'applique avant de construire, parce que rétro-adapter des modules validés tard est coûteux. Cela se rattache à la preuve de conformité et la gouvernance (chapitre 4.6).

## Compromis : avantages et inconvénients

| Décision | Avantages | Inconvénients |
|---|---|---|
| KMS géré par le fournisseur | Facile, intégré, faible fardeau opérationnel | Le fournisseur détient la garde ; moins de contrôle direct |
| Clés gérées par le client / HSM | Garde complète, satisfait des mandats stricts | Surcharge opérationnelle, risque de perdre les clés |
| Certificats automatisés de courte durée | Pas d'expiration surprise, révocation rapide | Exige un investissement d'automatisation en amont |
| Certificats de longue durée | Simple, moins de pièces mobiles | Les expirations gérées humainement causent des pannes |
| Chiffrement d'enveloppe | Rotation de clé bon marché, protège la clé maîtresse | Plus de pièces mobiles à comprendre |
| Agilité cryptographique en amont | Migrations futures bon marché | Effort d'abstraction et de conception supplémentaire maintenant |
| Adoption post-quantique précoce | Protège les secrets de longue durée | Outillage immature, clés plus grandes, un certain risque |

La tension centrale est le contrôle contre le fardeau opérationnel. Détenir vos propres clés dans un HSM donne une garde maximale et satisfait les mandats les plus stricts, mais cela exige de l'expertise et crée un nouveau risque catastrophique : perdez la clé et vous perdez les données, irrécupérablement. Les services gérés par le fournisseur retirent ce fardeau mais placent la garde chez le fournisseur. Résolvez cela en stratifiant : utilisez des services gérés avec des valeurs par défaut sensées pour la plupart des systèmes, et réservez les clés gérées par le client et les HSM aux données à plus haute classification où le contrôle supplémentaire vaut le coût et le risque.

## Questions à discuter avec votre équipe

1. **Avez-vous un inventaire complet de vos clés, certificats, et des algorithmes sur lesquels vous comptez ?** Vous ne pouvez pas faire pivoter, migrer, ou auditer ce que vous ne pouvez pas voir, et la plupart des organisations découvrent qu'elles ont bien plus de matériel cryptographique dispersé à travers les services que quiconque ne suit. Un inventaire est le prérequis pour chaque décision ultérieure : la surveillance d'expiration de certificat, la rotation de clé, la délimitation FIPS, et la planification post-quantique en dépendent tous. Apportez une liste de vos certificats actuels et leurs dates d'expiration, et demandez qui possède chacun et ce qui se casse quand il expire. Pour un grand parc, la réponse honnête est généralement qu'aucune source de vérité unique n'existe, et en construire une est le premier pas au plus grand levier. Si vous ne pouvez pas énumérer votre cryptographie aujourd'hui, l'agilité et la rotation sont des aspirations, pas des capacités.

2. **Pouvez-vous faire pivoter ou révoquer rapidement une clé compromise, et l'avez-vous jamais pratiqué ?** La rotation et la révocation sont les parties du cycle de vie de clé qui ne comptent que sous pression, et les équipes découvrent couramment pendant un incident qu'une clé est codée en dur à une douzaine d'endroits ou que la révocation ne se propage pas réellement. Décidez votre temps cible pour faire pivoter une clé et révoquer un certificat, puis répétez-le avant d'en avoir besoin. Apportez l'histoire de votre dernière exposition d'identifiant et parcourez ce que la rotation a exigé en pratique. Pour les systèmes d'entreprise et gouvernementaux, une rotation non répétée peut signifier choisir entre une exposition prolongée et une panne auto-infligée. Si la rotation n'a jamais été testée, supposez qu'elle ne fonctionne pas.

3. **Où se trouve la garde de clé, et impose-t-elle la séparation des tâches ?** Quiconque peut gérer une clé et quiconque peut lire les données qu'elle protège ne devraient pas être la même personne, parce que fusionner ces pouvoirs défait discrètement le but du chiffrement au repos. Ce choix pilote aussi si vous utilisez des clés gérées par le fournisseur, des clés gérées par le client, ou des HSM, chacun avec un contrôle différent et un risque opérationnel différent. Apportez vos politiques de clé actuelles et vérifiez si une identité quelconque peut à la fois administrer une clé et accéder au texte clair derrière elle, ce qui est une lacune silencieuse courante. Pour les données régulées et classifiées, les règles de garde peuvent être dictées par la classification de données (chapitre 4.5) et par mandat. Si la garde et l'accès ne sont pas séparés, votre chiffrement vous protège moins que le tableau de bord ne le suggère.

4. **Comment récupéreriez-vous si la clé maîtresse qui protège votre chiffrement d'enveloppe était perdue ou détruite ?** Les clés gérées par le client et les HSM vous donnent la garde, mais ils vous remettent un nouveau mode d'échec catastrophique : perdez la clé de chiffrement de clé et chaque clé de chiffrement de données qu'elle enveloppe devient définitivement illisible, avec les données derrière elles. Pesez cela contre le risque opposé d'une sauvegarde trop large qui recrée discrètement le même problème de garde que vous essayiez de résoudre. Apportez vos arrangements actuels de sauvegarde et de séquestre de clé, le rayon d'impact de chaque clé maîtresse, et la preuve qu'une restauration a réellement été effectuée plutôt que simplement documentée. Pour les parcs d'entreprise et gouvernementaux, liez cela à vos règles de classification de données : les clés les plus sensibles interdisent souvent les copies désinvoltes, donc la récupération doit être délibérément conçue, testée selon un calendrier, et réconciliée avec toute exigence réglementaire de prouver que le matériel de clé retiré a été détruit.

5. **À quel point vos systèmes sont-ils prêts pour une migration post-quantique, et quels secrets de longue durée migreriez-vous en premier ?** Les adversaires peuvent récolter le trafic et les archives chiffrés aujourd'hui et les déchiffrer une fois que les ordinateurs quantiques mûrissent, donc tout secret qui doit rester confidentiel pendant des années est déjà exposé à un futur que vous ne pouvez pas voir. La pression concurrente est que l'outillage post-quantique est encore jeune, les clés sont plus grandes, et bouger trop tôt risque de parier sur un algorithme qui change avant de se stabiliser. Apportez votre inventaire cryptographique, une liste de secrets classés par combien de temps ils doivent rester confidentiels, et une lecture honnête de si votre architecture peut échanger des algorithmes sans réécriture. Pour le travail gouvernemental et régulé, les registres avec des mandats de confidentialité de plusieurs décennies rendent cela concret plutôt que théorique, et l'approvisionnement pourrait bientôt exiger un plan de migration documenté et un support pour les algorithmes post-quantiques standardisés.

6. **Quand la réglementation exige une cryptographie validée, savez-vous exactement quels modules sont dans la portée et s'ils qualifient ?** Utiliser un algorithme fort n'est pas la même chose qu'utiliser une implémentation validée, et les équipes découvrent couramment tard qu'une bibliothèque, un runtime de langage, ou un service cloud n'est pas couvert par la frontière FIPS 140 qu'un contrat exige. La tension est que les modules validés peuvent traîner derrière les bibliothèques actuelles en fonctionnalités et vitesse, donc les choisir contraint votre pile de façons qui comptent pour l'ingénierie. Apportez la liste des modules cryptographiques que chaque système régulé appelle réellement, les certificats de validation qui les couvrent, et le mandat spécifique (FIPS 140, CNSA, ou une règle sectorielle) qui s'applique. Pour les programmes d'entreprise et gouvernementaux, décidez cela avant de construire, parce que rétro-adapter des modules validés et réautoriser un système après coup est coûteux, lent, et force souvent une reconception des composants mêmes que vous pensiez finis.

## Regard sectoriel

**Jeune pousse.** Appuyez-vous entièrement sur les valeurs par défaut vérifiées de votre plateforme et dépensez zéro temps d'ingénierie sur de la cryptographie personnalisée. Activez le chiffrement géré au repos, terminez TLS avec des certificats renouvelés automatiquement, hachez les mots de passe avec une fonction lente standard, et gardez les secrets dans le gestionnaire de secrets de la plateforme plutôt que le dépôt. Votre unique décision de conception est une interface mince autour de la poignée de champs que vous chiffrez dans l'application, pour qu'un futur déménagement hors des clés gérées par le fournisseur ne soit pas une réécriture.

**Petite entreprise.** Vous n'avez pas de cryptographe et peu d'appétit pour exploiter un HSM, donc achetez la garde plutôt que de la construire : utilisez le KMS géré par le fournisseur et le gestionnaire de secrets qui viennent avec vos outils cloud ou SaaS. Cadrez le travail comme de l'hygiène, c'est-à-dire, aucune clé dans le code, chiffrement activé partout par défaut, et expirations de certificat surveillées pour que rien n'expire par surprise. Réservez les clés gérées par le client pour les rares données qu'un contrat ou régulateur exige réellement.

**Grande entreprise.** Le problème est l'échelle et la cohérence à travers des milliers de services, certificats, et clés. Exploitez un KMS centralisé avec chiffrement d'enveloppe, automatisez le cycle de vie complet de certificat pour qu'aucune expiration ne soit entretenue à la main, et maintenez un inventaire cryptographique unique qui alimente la rotation, la délimitation FIPS, et la planification post-quantique. Séparez la garde de clé de l'accès aux données comme un contrôle à l'échelle de l'organisation, et faites du chiffrement une capacité de plateforme que chaque équipe hérite plutôt qu'une tâche que chaque équipe réinvente.

**Gouvernement.** L'approvisionnement, la validation, et l'audit façonnent chaque choix. Utilisez des modules validés FIPS 140 et suivez la guidance nationale telle que CNSA pour les systèmes classifiés, liez la garde de clé à la classification de données pour que les clés les plus sensibles se trouvent avec du personnel habilité sous une séparation des tâches stricte, et générez une preuve continue de cryptographie validée pour l'autorisation continue. Documentez un plan de migration post-quantique pour les registres qui doivent rester confidentiels pendant des décennies, et exigez que les fournisseurs divulguent quels modules sont validés avant de vous engager.

## Exemples

**Jeune pousse.** Une petite équipe construisant une application de suivi de santé s'appuie entièrement sur des valeurs par défaut vérifiées. Elle termine TLS avec des certificats renouvelés automatiquement, active le chiffrement au repos sur sa base de données gérée et son stockage d'objets avec le KMS du fournisseur, et hache les mots de passe avec une fonction lente et salée d'une bibliothèque standard. Plutôt que d'écrire toute cryptographie elle-même, elle utilise un appel de chiffrement authentifié de haut niveau pour le seul champ qu'elle doit chiffrer dans l'application. Les secrets vivent dans le gestionnaire de secrets de la plateforme, jamais dans le dépôt. Cela coûte quelques après-midis et retire une catégorie entière d'erreurs catastrophiques.

**Grande entreprise.** Une banque mondiale exploite un KMS centralisé et une flotte de HSM, avec un inventaire cryptographique qui suit chaque clé et certificat à travers des milliers de services. Le chiffrement d'enveloppe protège les données client, avec des clés de données enveloppées par des clés maîtresses qui pivotent selon un calendrier pendant que les données restent en place. L'émission et le renouvellement de certificat sont entièrement automatisés après qu'une panne orientée public leur a enseigné le coût d'un seul certificat expiré. Les administrateurs de clé sont une équipe séparée des ingénieurs d'application, donc la garde impose la séparation des tâches, et une couche d'agilité cryptographique leur permet de commencer à piloter des algorithmes post-quantiques pour les archives de longue durée.

**Gouvernement.** Une agence nationale gérant des registres classifiés utilise seulement des modules cryptographiques validés FIPS 140 et suit la guidance NSA CNSA pour ses systèmes à plus haute classification. Les clés sont générées et détenues dans des HSM qui ne libèrent jamais de matériel de clé en clair, et la garde est liée à la classification de données pour que les clés les plus sensibles se trouvent avec du personnel habilité sous une séparation des tâches stricte. Les certificats fonctionnent sur une PKI interne gérée avec des cycles de vie automatisés, et une preuve continue de cryptographie validée alimente l'autorisation continue de l'agence. Un plan de migration post-quantique documenté protège les registres qui doivent rester confidentiels pendant des décennies.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

La cryptographie est une autre zone où un investissement modeste prévient des pertes catastrophiques et médiatisées. Le coût total de possession inclut un KMS ou HSM, l'outillage de gestion de secrets et certificats, et le temps d'ingénierie pour concevoir les cycles de vie et garder un inventaire à jour. Ces coûts sont réels mais bornés. Le coût de les sauter est une violation de données non chiffrées, une panne de plusieurs heures d'un certificat expiré, ou une perte de données irrécupérable d'une clé mal gérée, chacune portant des amendes réglementaires, des coûts de notification, et un dommage réputationnel durable.

Le ROI le plus fort vient de l'automatisation et de la réutilisation. Les cycles de vie de certificat automatisés éliminent la panne auto-infligée la plus courante. La gestion de clé centralisée avec des valeurs par défaut sensées signifie que chaque nouveau service hérite du chiffrement en transit et au repos sans effort par équipe, transformant la cryptographie d'une taxe récurrente en une capacité de plateforme. Pour le travail régulé et gouvernemental, les modules validés et la preuve automatisée abaissent aussi le coût des audits et de l'autorisation. Quand vous faites valoir cela auprès de la direction, cadrez-le simplement : les algorithmes sont gratuits et prouvés, le risque vit dans la gestion de clé et les opérations de certificat, et un petit investissement automatisé là prévient les échecs coûteux.

## Anti-patterns et pièges

- **Coder sa propre cryptographie.** Des algorithmes personnalisés ou des protocoles construits à la main qui échouent de façons subtiles et expertes seulement.
- **Clés et secrets codés en dur.** Des identifiants collés dans le code source, les fichiers de configuration, ou le chat, où ils fuient et ne peuvent pas être pivotés.
- **Chiffrement sans discipline de clé.** Activer le chiffrement mais laisser l'accès aux clés grand ouvert ou ne jamais faire pivoter.
- **Confondre le hachage avec le chiffrement.** Traiter un hachage comme réversible, ou stocker des mots de passe avec un hachage rapide au lieu d'un lent et salé.
- **Roulette de certificat.** Aucun inventaire, aucune surveillance d'expiration, et des pannes surprises périodiques quand un certificat expire.
- **Garde de clé et accès aux données fusionnés.** Une identité qui peut à la fois gérer une clé et lire les données qu'elle protège.
- **Aucun plan de rotation.** Des clés qui n'ont jamais été pivotées et ne peuvent pas être pivotées rapidement sous pression.
- **Cryptographie sans agilité.** Des algorithmes câblés si profondément que les échanger exige une réécriture, bloquant toute future migration.
- **Ignorer les mandats de validation.** Utiliser des algorithmes forts dans des modules non validés là où une validation FIPS ou similaire est exigée.

## Modèle de maturité

- **Niveau 1 (Initier) :** Le chiffrement est incohérent et souvent absent, appliqué réactivement quand quelqu'un remarque une lacune. Les clés et secrets sont codés en dur ou partagés informellement sur le chat et les fichiers de configuration. Il n'y a pas d'inventaire, pas de rotation, et les certificats expirent par surprise, et les équipes écrivent occasionnellement leur propre cryptographie.
- **Niveau 2 (Développer) :** TLS et chiffrement au repos sont activés pour les systèmes majeurs, et un KMS ou gestionnaire de secrets existe, mais l'adoption est inégale et varie d'équipe à équipe. Certains certificats sont surveillés tandis que d'autres non, la rotation est manuelle et rare, et aucun inventaire cryptographique complet ne relie le tout.
- **Niveau 3 (Standardiser) :** Le chiffrement en transit et au repos est la valeur par défaut documentée imposée à l'échelle de l'organisation. Les clés vivent dans un KMS avec rotation planifiée et chiffrement d'enveloppe, la garde de clé est séparée de l'accès aux données, les cycles de vie de certificat sont automatisés, un inventaire cryptographique est maintenu, et des modules validés sont utilisés partout où la réglementation l'exige.
- **Niveau 4 (Gérer) :** Le parc cryptographique est mesuré et contrôlé par rapport à des références. Vous suivez le délai d'avance d'expiration de certificat, le pourcentage de clés pivotées selon le calendrier, le temps moyen pour révoquer une clé compromise, les détections de secrets-dans-le-code par période, et la couverture d'inventaire, et vous révisez ces métriques contre des cibles. La rotation et la révocation sont répétées selon une cadence avec des chronométrages enregistrés, et les déviations déclenchent une action corrective plutôt que de passer inaperçues.
- **Niveau 5 (Orchestrer) :** La cryptographie est une capacité de plateforme que chaque service hérite par défaut, et elle est continuellement améliorée et intégrée à travers l'organisation. La rotation et la révocation sont rapides et exercées routinièrement, les HSM protègent les clés à plus haute assurance, et l'agilité cryptographique plus un plan de migration post-quantique actif gardent le parc adaptatif à mesure que les algorithmes et mandats changent. La preuve de conformité est produite automatiquement et alimente l'autorisation continue.

## Pistes de réflexion

1. Quels systèmes dans votre parc justifient des clés gérées par le client ou des HSM étant donné leur coût opérationnel et le risque de perte catastrophique ?
2. Comment construiriez-vous et maintiendriez-vous une source de vérité unique pour chaque clé et certificat que vous possédez ?
3. Quel est votre temps réaliste pour faire pivoter une clé compromise aujourd'hui, et qu'est-ce qui le rend lent ?
4. Où votre architecture rend-elle difficile d'échanger un algorithme cryptographique, et comment corrigeriez-vous cela avant une migration forcée ?
5. Lesquels de vos secrets de longue durée compteraient si un adversaire les récoltait maintenant et les déchiffrait des années plus tard ?
6. Les secrets et clés finissent-ils jamais dans le code, la configuration, ou les journaux, et comment le sauriez-vous ?

## Points clés à retenir

- **Ne codez pas votre propre cryptographie.** Utilisez des bibliothèques vérifiées et des algorithmes standard à la plus haute abstraction sûre.
- **Les algorithmes sont faciles ; la gestion de clé est difficile.** Le cycle de vie d'une clé (génération, distribution, rotation, révocation, destruction) est là où vivent les vrais échecs.
- **Connaissez vos garanties :** le chiffrement symétrique et à clé publique protège la confidentialité, les signatures prouvent l'authenticité et l'intégrité, et le hachage détecte la falsification mais n'est pas du chiffrement.
- **Chiffrez en transit avec TLS actuel et au repos avec le chiffrement d'enveloppe**, comme valeur par défaut pour chaque système.
- **Séparez la garde de clé de l'accès aux données**, utilisez un KMS pour les clés et un gestionnaire de secrets pour les identifiants, et ne codez jamais en dur l'un ou l'autre.
- **Automatisez les cycles de vie de certificat** pour tuer la panne d'expiration surprise, et gardez un inventaire cryptographique.
- **Construisez pour l'agilité cryptographique** et commencez un plan de migration post-quantique pour les secrets de longue durée.
- **Préférez les implémentations validées** (FIPS 140 et la guidance nationale applicable) là où la réglementation ou la classification l'exige.

## Références et lectures complémentaires

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, normes de cryptographie post-quantique (FIPS 203, 204, et 205).
- Niels Ferguson, Bruce Schneier, et Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* et *Transport Layer Protection Cheat Sheet*.
- National Security Agency, guidance *Commercial National Security Algorithm (CNSA) Suite*.
