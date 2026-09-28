# 5.7 Développement d'applications mobiles

## Vue d'ensemble et motivation

Le [développement d'applications mobiles](https://fr.wikipedia.org/wiki/D%C3%A9veloppement_d%27applications_mobiles) est la discipline de construire du logiciel pour téléphones et tablettes. Pour de nombreuses personnes, un téléphone est maintenant le seul ou principal ordinateur qu'elles possèdent. Cela fait de l'application mobile la porte d'entrée vers votre service, et souvent la surface où les utilisateurs jugent votre organisation entière.

Le mobile est un environnement d'ingénierie distinct, pas une petite version du web ou du bureau. L'appareil fonctionne dans une poche, sur batterie, à travers des connexions qui vont et viennent. Les écrans sont petits. Le système d'exploitation contrôle ce que votre application peut faire. Deux plateformes dominantes existent ([iOS](https://fr.wikipedia.org/wiki/IOS) d'Apple et [Android](https://fr.wikipedia.org/wiki/Android) de Google), chacune avec ses propres langages, règles de conception, et magasin. Vous ne pouvez pas simplement livrer une mise à jour quand bon vous semble, parce qu'un magasin la révise d'abord, et les utilisateurs choisissent quand l'installer. Ce chapitre s'appuie sur l'ingénierie frontend (chapitre 5.6), les fondements UX (chapitre 5.1), et l'accessibilité (chapitre 5.3), et s'appuie sur la sécurité applicative (chapitre 4.2) et le CI/CD et livraison (chapitre 8.1).

La pertinence pour l'entreprise et l'administration publique est élevée. Les entreprises livrent des applications clients et des applications internes pour leur propre main-d'œuvre, souvent gérées par [gestion des appareils mobiles](https://fr.wikipedia.org/wiki/Mobile_device_management) (MDM : logiciel central qui configure et sécurise les appareils d'entreprise). Les gouvernements construisent des applications orientées citoyen pour les prestations, la santé, l'identité, et les paiements, et ils doivent servir tout le monde, incluant les personnes sur d'anciens appareils et connexions lentes, sous les lois d'accessibilité. Dans les deux contextes, le mobile est un engagement sérieux et de longue durée, donc traitez-le avec la même rigueur que vous accordez à tout autre système de production.

## Principes clés

- Concevez pour l'appareil : petit écran, batterie, et un réseau qui va et vient.
- Supposez une connectivité intermittente ; fonctionnez hors ligne d'abord et synchronisez quand vous le pouvez.
- Respectez les conventions de conception et d'interaction de chaque plateforme.
- Vous ne contrôlez pas le calendrier de sortie ; le magasin et l'utilisateur le font.
- La fragmentation est normale ; soutenez une vraie gamme d'appareils et versions de système d'exploitation.
- Stockez les données de façon sécurisée sur l'appareil, parce que les appareils se perdent et se font voler.
- L'accessibilité est une exigence, pas une touche finale.
- Choisissez votre approche de construction pour la vie entière de l'application, pas seulement le jour de lancement.

## Recommandations

### Choisir l'approche de construction délibérément

Il y a trois approches larges, et chacune convient à des besoins différents.

Le [développement natif](https://fr.wikipedia.org/wiki/D%C3%A9veloppement_d%27applications_mobiles) signifie écrire séparément pour chaque plateforme en utilisant ses propres outils : Swift pour iOS, Kotlin pour Android. Vous obtenez la meilleure performance, l'accès le plus complet aux fonctionnalités de l'appareil, et la sensation de plateforme la plus fidèle, au coût de construire et maintenir deux bases de code.

Les [cadriciels multiplateformes](https://fr.wikipedia.org/wiki/Application_multiplateforme) permettent à une base de code de cibler les deux plateformes. [React Native](https://fr.wikipedia.org/wiki/React_Native) utilise JavaScript et rend de vrais composants natifs. [Flutter](https://fr.wikipedia.org/wiki/Flutter_%28logiciel%29) utilise le langage Dart et dessine ses propres widgets. Ceux-ci réduisent l'effort dupliqué et peuvent accélérer la livraison, mais ils ajoutent une dépendance à la santé du cadriciel et peuvent traîner derrière les fonctionnalités de plateforme les plus récentes.

Une [application web progressive](https://fr.wikipedia.org/wiki/Application_web_progressive) (PWA : un site web qui peut être installé et peut fonctionner hors ligne) n'a besoin d'aucun magasin et se met à jour instantanément, mais elle a un accès limité à certaines fonctionnalités d'appareil et une présence plus faible sur l'écran d'accueil.

Choisissez selon les fonctionnalités d'appareil requises, le profil de performance, l'horizon de maintenance, les compétences que vous pouvez embaucher, et la portée dont vous avez besoin. Une application grand public à haute performance peut justifier le natif. Une application de contenu et formulaires avec une petite équipe peut bien convenir au multiplateforme ou à une PWA.

### Suivre les directives de conception de plateforme

Chaque plateforme a des conventions publiées et détaillées. Apple fournit les [Human Interface Guidelines](https://fr.wikipedia.org/wiki/Human_interface_guidelines), et Google fournit [Material Design](https://fr.wikipedia.org/wiki/Material_Design). Celles-ci couvrent la navigation, les gestes, la typographie, l'espacement, et les comportements système. Les suivre rend votre application familière, ce qui abaisse l'effort que les utilisateurs dépensent à l'apprendre. Les combattre rend une application étrangère et maladroite. Une base de code multiplateforme doit quand même honorer les conventions par plateforme où elles diffèrent, plutôt que de forcer l'apparence d'une plateforme sur l'autre.

### Concevoir pour les contraintes mobiles

Construisez hors ligne d'abord : laissez les tâches centrales fonctionner sans connexion, stockez les changements localement, et synchronisez quand le réseau revient. Gérez les conflits attentivement quand les mêmes données changent en deux endroits. Soyez économe avec la batterie et les données : groupez les appels réseau, évitez la localisation constante ou le travail en arrière-plan, compressez les charges utiles, et respectez les paramètres d'économie de données de l'utilisateur. Planifiez pour la fragmentation, la large diffusion de tailles d'écran, puissance d'appareil, et versions de système d'exploitation. Choisissez une gamme de soutien basée sur des données d'usage réelles, et testez sur du matériel modeste, pas seulement les appareils phares. Concevez pour les petits écrans avec une hiérarchie claire, de grandes cibles tactiles, et du contenu qui s'adapte à différentes tailles et orientations.

### Planifier la distribution, le versionnage, et les mises à jour

La publication passe par l'[Apple App Store](https://fr.wikipedia.org/wiki/App_Store) et [Google Play](https://fr.wikipedia.org/wiki/Google_Play), chacun avec des processus de revue et des politiques qui peuvent retarder ou rejeter une sortie. Intégrez le temps de revue dans votre calendrier, et lisez les politiques tôt. Parce que les utilisateurs choisissent quand mettre à jour, vous aurez toujours de nombreuses versions sur le terrain à la fois. Gardez votre application rétrocompatible avec les clients plus anciens, et versionnez vos API (chapitre 2.3) pour qu'une ancienne application continue de fonctionner. Fournissez une façon d'exiger une mise à jour quand vous le devez, par exemple une invite de mise à jour forcée quand une version est dangereuse ou non soutenue, et utilisez-la avec parcimonie. Les entreprises peuvent aussi distribuer des applications internes par MDM ou canaux privés plutôt que les magasins publics.

### Utiliser les notifications push et liens profonds avec soin

Les [notifications push](https://fr.wikipedia.org/wiki/Push_%28informatique%29) vous permettent d'atteindre les utilisateurs quand votre application est fermée. Utilisez-les pour une vraie valeur, respectez le consentement de l'utilisateur et les permissions de plateforme, et évitez le bruit, parce que les gens désactivent les notifications des applications qui exagèrent. Les [liens profonds](https://fr.wikipedia.org/wiki/Lien_profond) envoient un utilisateur directement vers un écran spécifique depuis un lien ou une notification. Configurez-les pour qu'un lien ouvre le bon endroit dans l'application, et se replie gracieusement vers le web quand l'application n'est pas installée.

### Sécuriser l'application et ses données

Traitez l'appareil comme non fiable et possiblement perdu. Stockez les données sensibles dans le stockage sécurisé de la plateforme (le [Trousseau iOS](https://fr.wikipedia.org/wiki/Trousseau_%28logiciel%29) ou l'Android Keystore), jamais dans des fichiers en clair. Offrez l'[authentification biométrique](https://fr.wikipedia.org/wiki/Biom%C3%A9trie) (empreinte digitale ou visage) pour déverrouiller les actions sensibles, soutenue par un code d'accès. Envisagez l'[épinglage de certificat](https://fr.wikipedia.org/wiki/%C3%89pinglage_de_cl%C3%A9_publique) (vérifier que le serveur présente un certificat attendu) pour les connexions à haute valeur, et planifiez la rotation de ces certificats. Minimisez ce que vous stockez sur l'appareil, protégez les secrets, et suivez la directive plus large en sécurité applicative (chapitre 4.2).

### Construire un vrai pipeline de test et de livraison

Testez sur de vrais appareils, pas seulement des [émulateurs](https://fr.wikipedia.org/wiki/%C3%89mulateur) et simulateurs, parce que le matériel, les capteurs, et la performance diffèrent. Utilisez un laboratoire d'appareils ou une ferme d'appareils cloud pour couvrir une diffusion représentative de modèles et versions de système d'exploitation. Automatisez les constructions, tests, signatures, et soumissions au magasin à travers l'[intégration et la livraison continues](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue) (chapitre 8.1), incluant la distribution bêta aux testeurs avant la sortie publique. Gérer en sécurité les clés de signature et identifiants de magasin fait partie de ce pipeline.

### Faire de l'accessibilité une exigence

Soutenez les fonctionnalités d'accessibilité de chaque plateforme : lecteurs d'écran ([VoiceOver](https://fr.wikipedia.org/wiki/VoiceOver) sur iOS, [TalkBack](https://fr.wikipedia.org/wiki/TalkBack) sur Android), dimensionnement de texte dynamique, contraste de couleur suffisant, et grandes cibles tactiles. Étiquetez les contrôles pour que la technologie d'assistance puisse les décrire. Testez avec les vrais outils d'assistance, pas seulement des contrôles automatisés. Pour l'administration publique spécialement, l'accessibilité est un mandat légal, et les détails vivent dans le chapitre accessibilité (5.3).

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| Natif (Swift, Kotlin) | Meilleure performance, accès complet à l'appareil, vraie sensation de plateforme | Deux bases de code, coût plus élevé, plus de personnel |
| React Native | Une base de code JavaScript, vrais composants natifs, itération rapide | Dépendance au cadriciel, complexité de pontage, retard de fonctionnalité |
| Flutter | Une base de code, UI cohérente, forte performance | Compétences Dart moins communes, taille d'application plus grande, propre modèle de widget |
| Application web progressive | Aucun magasin, mises à jour instantanées, une base de code web | Fonctionnalités d'appareil limitées, présence plus faible, limites de plateforme |
| Mises à jour forcées | Retire rapidement les anciennes versions dangereuses | Ennuie les utilisateurs si surutilisé ; peut bloquer l'accès |
| Épinglage de certificat | Protection forte contre l'interception | Se casse si les certificats tournent sans mises à jour d'application |

Le compromis récurrent est la portée et la vitesse de livraison contre la profondeur et la fidélité. Le natif donne l'expérience la plus riche et la plus fidèle mais coûte le plus à construire et maintenir. Les approches multiplateformes et PWA économisent l'effort et élargissent la portée, à un certain coût en sensation de plateforme ou accès d'appareil. Pour une petite équipe livrant des formulaires et du contenu, partager une base de code est souvent sage. Pour une application grand public exigeante, la profondeur native peut valoir le prix. Décidez avec la vie entière de l'application en vue, pas seulement le lancement.

## Questions à discuter avec votre équipe

1. **Combien de temps soutenons-nous les anciens clients sur le terrain, et notre API est-elle versionnée pour les garder fonctionnels ?** Parce que les utilisateurs choisissent quand mettre à jour, vous avez toujours de nombreuses versions de l'application installées à la fois, et un changement backend qui suppose que tout le monde est à jour cassera la longue traîne des clients plus anciens. Décidez votre fenêtre de rétrocompatibilité, versionnez vos API pour qu'une ancienne application continue de fonctionner, et gardez un chemin de mise à jour forcée rarement utilisé pour les versions véritablement dangereuses. Cela compte autant pour les applications citoyennes gouvernementales que pour les applications de main-d'œuvre d'entreprise, où les gens sur d'anciens appareils ne peuvent pas ou ne veulent pas mettre à jour selon votre calendrier. Apportez vos données de distribution de version actuelles et demandez ce qui se casse pour le plus ancien client encore en usage réel. Si vous ne connaissez pas cette distribution, instrumentez-la avant de livrer votre prochain changement cassant.

2. **Quelle est notre barre pour envoyer une notification push, et qui décide de ce qui vaut la peine d'interrompre un utilisateur ?** Les notifications push atteignent les gens quand l'application est fermée, ce qui les rend puissantes et faciles à abuser, et les utilisateurs désactivent les notifications (ou suppriment l'application) des produits qui exagèrent. Convenez de ce qui compte comme vraie valeur, comment les utilisateurs contrôlent la fréquence et le canal, et comment vous honorez le consentement de plateforme plutôt que de harceler pour la permission. Sans barre partagée, chaque équipe avec une métrique à atteindre recourra à un push, et le canal entier se dégrade en bruit. Apportez le dernier mois de notifications que vous avez envoyées et demandez lesquelles l'utilisateur vous aurait remercié pour. Si la plupart étaient promotionnelles, resserrez la politique avant que le taux de désabonnement ne le fasse pour vous.

3. **Notre pipeline de livraison mobile est-il réel, couvrant la signature, une ferme d'appareils, et la distribution bêta, ou la sortie est-elle une course précipitée manuelle stressante ?** Le mobile ajoute des dangers que le web n'a pas : la revue de magasin peut retarder ou rejeter une sortie, les clés de signature et identifiants de magasin doivent être gérés en sécurité, et le matériel et les capteurs diffèrent assez pour que les émulateurs cachent de vrais problèmes. Automatiser les constructions, tests, signatures, et soumissions au magasin à travers CI/CD, avec la distribution bêta aux testeurs et une ferme d'appareils cloud couvrant les modèles que vos utilisateurs portent réellement, est ce qui transforme les sorties d'héroïsme en routine. Décidez qui possède le pipeline et les clés de signature, et comment le temps de revue de magasin est intégré dans chaque plan de sortie. Apportez l'histoire de votre dernière sortie et comptez les étapes manuelles. Chacune est un endroit où une sortie stressante peut mal tourner sous une date limite.

4. **Avons-nous choisi natif, multiplateforme, ou une application web progressive pour la vie entière de ce produit, ou seulement pour le jour du lancement ?** L'approche de construction est le levier unique le plus important sur le coût et la capacité d'une application mobile pendant des années, et un choix fait pour livrer rapidement peut vous piéger : le natif achète l'accès d'appareil et la sensation de plateforme les plus riches au prix de deux bases de code et deux ensembles de compétences, tandis que le multiplateforme et la PWA partagent du code mais ajoutent une dépendance de cadriciel ou perdent l'accès à certaines fonctionnalités d'appareil. Pour une grande équipe, cette décision pilote l'embauche, le budget de maintenance, et à quelle vitesse vous pouvez adopter chaque sortie annuelle de système d'exploitation, donc elle mérite un propriétaire explicite plutôt qu'une valeur par défaut fixée par quiconque a écrit le premier prototype. Apportez les fonctionnalités d'appareil requises, le profil de performance, l'horizon de maintenance, et les compétences que vous pouvez réellement embaucher, et soyez honnête sur quelles fonctionnalités de plateforme vous renonceriez sous chaque option. Dans les contextes d'entreprise et gouvernementaux, pesez si l'application est un engagement de longue durée qui doit survivre au roulement de personnel et une décennie de changement de plateforme, et enregistrez la décision et sa justification pour qu'une future équipe ne soit pas laissée à deviner pourquoi la base de code paraît comme elle paraît.

5. **Quelle gamme de soutien d'appareil et de version de système d'exploitation nos vrais utilisateurs ont-ils besoin, et testons-nous sur le matériel qu'ils portent réellement plutôt que les téléphones sur nos bureaux ?** La fragmentation est la condition normale du mobile : les utilisateurs s'étendent sur une large diffusion de tailles d'écran, puissance d'appareil, et versions de système d'exploitation, et une application réglée sur les appareils phares de l'équipe se livrera lente ou cassée sur le matériel modeste que possède une grande partie de votre audience. Fixer une gamme de soutien est un compromis entre portée et effort, parce que chaque modèle plus ancien et version de système d'exploitation que vous promettez de soutenir élargit la matrice de test et le fardeau de maintenance, donc la gamme doit venir de données d'usage réelles plutôt que de supposition. Apportez votre distribution d'appareil et de version de système d'exploitation, les modèles qu'une ferme ou laboratoire d'appareils cloud couvre actuellement, et la performance que vous avez mesurée sur du matériel bas de gamme, pas seulement des simulateurs. Pour les applications citoyennes gouvernementales c'est proche du non négociable, parce que vous devez servir tout le monde incluant les personnes sur d'anciens appareils et connexions lentes sous obligations d'accessibilité, et pour les flottes d'entreprise vous devriez tester les combinés robustes exacts que le personnel porte plutôt qu'un échantillon générique.

6. **Quelles données sensibles vivent sur l'appareil, et chaque pièce est-elle protégée contre un téléphone perdu, volé, ou entre les mains de quelqu'un d'autre ?** Un appareil mobile voyage dans une poche et se perd ou se fait voler, donc toute donnée ou secret stocké dans un fichier en clair est à un téléphone égaré de l'exposition, et le rayon d'explosion grandit avec chaque utilisateur. Les considérations tirent l'une contre l'autre : mettre en cache des données sur l'appareil est ce qui fait fonctionner le hors ligne d'abord et garde l'application rapide, pourtant chaque élément mis en cache est un passif qui doit se trouver dans le stockage sécurisé de la plateforme (le Trousseau iOS ou l'Android Keystore), être minimisé, et idéalement être verrouillé derrière la biométrie ou un code d'accès. Apportez un inventaire de ce que l'application persiste exactement localement, où chaque élément est stocké, ce qui le déverrouille, et si les connexions à haute valeur utilisent l'épinglage de certificat avec un plan de rotation viable. Dans les contextes d'entreprise, liez cela à la politique de gestion d'appareils mobiles et à l'effacement à distance, et dans les contextes gouvernementaux traitez les données personnelles sur appareil comme une exposition de confidentialité et légale qui doit être justifiée, documentée, et défendable sous audit.

## Regard sectoriel

**Jeune pousse.** Avec une minuscule équipe et peu de marge de manœuvre, vous pouvez rarement vous permettre deux bases de code natives ou deux ensembles de compétences, donc un cadriciel multiplateforme ou même une PWA qui atteint les deux magasins depuis une base de code gagne habituellement. Livrez hors ligne d'abord pour la seule tâche centrale qui compte, gardez tout jeton dans le stockage sécurisé plutôt qu'un fichier en clair, et intégrez le temps de revue de magasin dans chaque sortie pour qu'un rejet ne fasse pas exploser une date de lancement. Sautez les mises à jour forcées, l'épinglage de certificat, et une ferme d'appareils jusqu'à ce que l'usage réel les justifie.

**Petite entreprise.** Sans spécialiste mobile dédié et avec un budget serré, penchez fortement vers acheter plutôt que construire : un constructeur d'application sans code, une application de marque blanche de votre fournisseur de point de vente ou réservation, ou une PWA bien faite depuis votre site web existant bat souvent une application sur mesure que vous ne pouvez pas maintenir. Si vous commissionnez une application, possédez vous-même les clés de signature et comptes de magasin pour qu'un contractant ne puisse pas prendre votre présence en otage, et insistez sur l'accessibilité et le stockage sécurisé sur appareil dans le contrat. Gardez la portée aux une ou deux tâches que les clients font réellement sur un téléphone.

**Grande entreprise.** À l'échelle, l'application est un engagement de longue durée à travers de nombreuses équipes, donc standardisez l'approche de construction, le motif de stockage sécurisé, le pipeline CI/CD, et la politique de versionnage d'API plutôt que de laisser chaque produit les réinventer. Les applications internes de main-d'œuvre passent habituellement par la gestion d'appareils mobiles pour l'installation, la configuration, l'effacement à distance, et la politique, tandis que les applications clients ont besoin d'une ferme d'appareils couvrant l'usage réel et une accessibilité et sécurité auditées. Gouvernez les clés de signature, identifiants de magasin, et calendrier de sortie centralement pour qu'un changement backend cassant n'échoue jamais la longue traîne des clients plus anciens.

**Gouvernement.** Les règles d'approvisionnement, la transparence, et la responsabilité publique façonnent chaque choix. Vous devez servir tout le monde, incluant les personnes sur d'anciens appareils et connexions lentes, donc l'accessibilité est un mandat légal vérifié avec de vrais outils d'assistance, et une large gamme de soutien d'appareil est proche du non négociable. Favorisez les approches et contrats qui évitent le verrouillage à un fournisseur, gardent les données portables, et laissent le public inspecter ce que l'application fait avec leurs données, et traitez les données personnelles sur appareil comme une exposition que vous devez justifier et documenter sous audit.

## Exemples

**Jeune pousse.** Une jeune pousse de trois personnes construisant une application de suivi d'habitudes devait atteindre iOS et Android mais ne pouvait pas se permettre deux bases de code natives ou deux ensembles de compétences. Ils ont choisi un cadriciel multiplateforme pour qu'une petite équipe puisse livrer aux deux magasins, et conçu hors ligne d'abord dès le début pour qu'un utilisateur puisse enregistrer une habitude dans le métro sans signal et synchroniser plus tard. Ils ont gardé le jeton de connexion dans le stockage sécurisé de plateforme plutôt qu'un fichier en clair, intégré le temps de revue de magasin dans chaque plan de sortie, et testé sur quelques téléphones anciens bon marché aux côtés des leurs, ce qui a attrapé une performance lente qu'ils auraient autrement livrée.

**Grande entreprise.** Une entreprise de logistique a construit une application interne pour ses chauffeurs et personnel d'entrepôt. Parce que les entrepôts et routes de livraison ont un signal inégal, l'équipe a choisi une conception hors ligne d'abord : les scans et mises à jour de statut se sauvegardent localement et se synchronisent quand une connexion revient. Ils ont utilisé un cadriciel multiplateforme pour servir une base de code aux deux plateformes avec une petite équipe. L'application est distribuée par gestion d'appareils mobiles plutôt que les magasins publics, donc l'IT contrôle l'installation, la configuration, et la politique de sécurité sur les appareils d'entreprise. Les identifiants sensibles vivent dans le stockage sécurisé de plateforme, et la biométrie déverrouille l'application. Une ferme d'appareils cloud teste une diffusion représentative des combinés robustes que le personnel porte réellement.

**Gouvernement.** Une agence nationale a livré une application orientée citoyen pour l'identité et les prestations. L'accessibilité était une exigence dure dès le premier jour : soutien complet de lecteur d'écran, dimensionnement de texte dynamique, et contraste fort, testé avec de vrais outils d'assistance pour satisfaire la loi. Parce que les citoyens utilisent une énorme gamme d'appareils, l'équipe a soutenu une large bande de modèles plus anciens et connexions lentes, et gardé les tâches centrales fonctionnelles hors ligne. Les données sensibles restent dans le stockage sécurisé de l'appareil, la biométrie protège l'accès, et les connexions à haute valeur utilisent l'épinglage de certificat avec un processus de rotation planifié. Le versionnage d'API garde les anciennes applications installées fonctionnelles, et un chemin de mise à jour forcée rarement utilisé existe pour les correctifs de sécurité. Les calendriers de revue de magasin sont intégrés dans chaque plan de sortie.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le mobile est là où de nombreux utilisateurs rencontrent votre service, donc l'application affecte l'adoption, la satisfaction, et la complétion des tâches qui comptent pour votre organisation. Une application rapide, fiable, et bien conçue augmente l'usage et réduit la charge de support. Pour les entreprises, une application mobile interne peut rendre une main-d'œuvre mobile mesurablement plus productive et réduire la paperasse. Pour les gouvernements, une application citoyenne utilisable élargit l'accès et réduit la demande de centre d'appels et en personne.

Sur le coût total de possession, le choix d'approche est le plus grand levier. Le natif signifie payer pour deux bases de code et deux ensembles de compétences sur toute la vie de l'application. Le multiplateforme échange une partie de cela contre une dépendance que vous devez garder à jour. Au-delà du code, budgétez pour les frais de magasin et cycles de revue, un laboratoire de test d'appareil ou ferme cloud, le soutien continu de version de système d'exploitation à mesure que les plateformes sortent annuellement, et le travail de sécurité que le mobile exige. Le coût de sous-investir se manifeste comme des plantages sur les appareils non soutenus, des incidents de sécurité depuis des données non protégées sur appareil, des sorties rejetées ou retardées, et des utilisateurs qui abandonnent une application lente ou maladroite.

Pour faire valoir cela auprès de la direction, connectez l'application à des résultats concrets : complétion de tâche, rétention, productivité de main-d'œuvre, ou coût de support réduit. Évaluez la décision d'approche complète à travers la vie de l'application, pas seulement la première sortie, et nommez les risques (sécurité, loi d'accessibilité, rejet de magasin) qu'une pratique mobile sérieuse réduit.

## Anti-patterns et pièges

- **Traiter le mobile comme un site web rétréci** : ignorer le tactile, les gestes, et les conventions de plateforme.
- **Supposer un réseau parfait** : aucune gestion hors ligne, donc l'application se casse au moment où le signal tombe.
- **Tester seulement sur le dernier phare** : cacher une mauvaise performance sur les appareils que les vrais utilisateurs portent.
- **Stocker des secrets dans des fichiers en clair** : données sensibles exposées quand un appareil est perdu ou volé.
- **Surcharge de notification** : trop de pushs, donc les utilisateurs coupent le son ou suppriment l'application.
- **Ignorer le temps de revue de magasin** : des plans de sortie qui supposent une publication instantanée puis dérapent.
- **Aucun chemin de mise à jour forcée** : d'anciennes versions dangereuses survivent sans moyen de les retirer.
- **Vider la batterie et les données** : travail constant en arrière-plan et réseautage bavard que les utilisateurs remarquent.
- **Accessibilité comme pensée après coup** : exclure des utilisateurs et, pour l'administration publique, enfreindre la loi.
- **Une base de code forcée à paraître identique partout** : une application qui se sent étrangère sur les deux plateformes.

## Modèle de maturité

**Niveau 1 (Initier).** Le mobile est au coup par coup et réactif. L'application est construite comme un site web, testée sur les propres téléphones de l'équipe, et se casse souvent hors ligne. Peu de réflexion va au stockage sécurisé, l'accessibilité, ou les calendriers de revue de magasin. Les sorties sont une course précipitée manuelle stressante, et personne ne possède l'approche de construction ou les clés de signature.

**Niveau 2 (Développer).** Des pratiques de base apparaissent, mais elles sont incohérentes à travers les équipes et produits. Une approche de construction est choisie pour une application donnée, elle suit les bases de plateforme et est testée sur quelques vrais appareils, et une certaine gestion hors ligne et stockage sécurisé existent. Les constructions sont partiellement automatisées et quelqu'un possède les soumissions de magasin, pourtant l'application d'une autre équipe peut encore faire tout cela différemment ou pas du tout.

**Niveau 3 (Standardiser).** La bonne pratique est documentée et imposée à l'échelle de l'organisation. Le hors ligne d'abord est la valeur par défaut, une gamme de soutien d'appareil documentée est testée sur un laboratoire d'appareils ou ferme cloud, et les directives de conception de plateforme et l'accessibilité sont suivies et vérifiées avec de vrais outils d'assistance. Le stockage sécurisé, la biométrie, et le versionnage d'API sont standard, CI/CD automatise les constructions, tests, signatures, et distribution bêta, et le temps de revue de magasin est planifié dans chaque sortie.

**Niveau 4 (Gérer).** La qualité mobile est mesurée et contrôlée contre des références. Les plantages, la performance de démarrage à froid et de rendu d'écran, l'usage de batterie et de données, et les taux de complétion de tâche sont capturés continuellement depuis de vrais appareils et suivis contre des cibles, avec des ventilations par modèle et par version de système d'exploitation pour qu'une régression sur du matériel bas de gamme soit attrapée, pas livrée. L'accessibilité et la sécurité sont auditées plutôt que supposées, les taux de désabonnement de notification et d'adoption de mise à jour sont surveillés, et la gamme de soutien et l'approche de construction sont révisées sur cette preuve. Les décisions de tuer ou corriger pour une sortie reposent sur les métriques, pas sur comment l'application se sentait sur le téléphone du responsable.

**Niveau 5 (Orchestrer).** Le mobile s'améliore continuellement et est intégré à travers l'organisation, et il s'adapte à mesure que le paysage d'appareil change. La rotation de certificat, les chemins de mise à jour forcée, et le retour en arrière sont routiniers, la gamme de soutien et l'approche de construction sont recadrées sur preuve à mesure que les plateformes sortent annuellement, et toute la diffusion d'utilisateurs et d'appareils est traitée comme de première classe. La planification mobile est jointe à la sécurité, l'accessibilité, l'API, et la pratique de livraison, pour qu'un changement de système d'exploitation, un nouveau niveau d'appareil, ou un changement de politique soit absorbé comme travail routinier plutôt qu'une urgence.

## Pistes de réflexion

- Comment décidez-vous entre natif, multiplateforme, et une application web progressive pour un produit donné ?
- Quelle gamme de soutien d'appareil et de version de système d'exploitation convient à vos données d'utilisateur réelles, et comment la gardez-vous à jour ?
- Où le hors ligne d'abord est-il essentiel dans votre application, et comment gérerez-vous les conflits de synchronisation ?
- Quand une mise à jour forcée est-elle justifiée, et comment évitez-vous de bloquer injustement les utilisateurs ?
- Comment testerez-vous sur de vrais appareils à une échelle qui reflète vos utilisateurs ?
- Quelles données sensibles vivent sur l'appareil, et comment chaque pièce est-elle protégée ?
- Comment honorez-vous les conventions de chaque plateforme depuis une base de code partagée ?

## Points clés à retenir

- Choisissez l'approche de construction (native, multiplateforme, ou PWA) pour la vie entière de l'application.
- Suivez les directives de conception de plateforme pour que l'application se sente familière et abaisse l'effort utilisateur.
- Concevez pour les contraintes mobiles : hors ligne d'abord, économe en batterie et données, fragmentation, petits écrans.
- Vous ne contrôlez pas le calendrier de sortie ; planifiez pour la revue de magasin, le versionnage, et les mises à jour forcées.
- Utilisez les notifications push et liens profonds avec retenue et consentement.
- Sécurisez les données sur appareil avec du stockage sécurisé, biométrie, et, où justifié, épinglage de certificat.
- Testez sur de vrais appareils et automatisez le pipeline mobile à travers CI/CD.
- Faites de l'accessibilité une exigence, ce qui pour l'administration publique est un mandat légal.

## Références et lectures complémentaires

- Apple, *Human Interface Guidelines*.
- Google, directives *Material Design*.
- Apple, *App Store Review Guidelines*.
- Google, *Google Play developer policies and Android developer documentation*.
- OWASP, *Mobile Application Security Verification Standard (MASVS)* et *Mobile Security Testing Guide*.
- Documentation du projet React Native.
- Documentation du projet Flutter.
- Google, directive *web.dev* sur les applications web progressives.
- Références U.S. Section 508 et WCAG (Web Content Accessibility Guidelines) pour l'accessibilité mobile.
- NIST, *Guidelines on mobile device security and management*.
