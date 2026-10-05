# 8.2 Infrastructure comme code et configuration

## Vue d'ensemble et motivation

L'[infrastructure comme code](https://fr.wikipedia.org/wiki/Infrastructure_as_code) (IaC) signifie définir et approvisionner l'infrastructure (réseaux, serveurs, bases de données, équilibreurs de charge, permissions) à travers des fichiers de définition lisibles par machine plutôt que des clics de console manuels ou scripts au coup par coup. La [gestion de configuration](https://fr.wikipedia.org/wiki/Gestion_de_configuration) étend la même idée aux paramètres et à l'état des systèmes une fois qu'ils existent. Ensemble elles transforment l'infrastructure d'un artefact fait à la main et fragile en un produit versionné, révisable, reproductible de la même discipline d'ingénierie que vous utilisez pour le code d'application.

Pour les grandes équipes, l'IaC n'est pas une commodité mais une nécessité. Quand des centaines d'ingénieurs ont besoin d'environnements et que des milliers de ressources doivent rester cohérentes à travers les régions et comptes, l'approvisionnement manuel ne peut pas suivre et ne peut pas rester correct. L'infrastructure configurée par des humains dérive, tôt ou tard, vers des serveurs « flocon de neige » uniques que personne ne comprend entièrement et qui ne peuvent pas être reconstruits de façon fiable après un échec. Codifier l'infrastructure la rend cohérente, auditable, et jetable. Tout environnement peut être recréé depuis sa définition, et tout changement est un diff révisable.

Les organisations d'entreprise et gouvernementales gagnent un bénéfice décisif de plus : une gouvernance applicable. Les exigences de sécurité et conformité, telles que le chiffrement au repos, la segmentation réseau, les régions approuvées, et l'étiquetage pour l'allocation de coût, peuvent être intégrées directement dans le code et vérifiées automatiquement avant que quoi que ce soit ne soit approvisionné. Au lieu d'auditer l'infrastructure après coup et de poursuivre les violations, vous empêchez l'infrastructure non conforme d'exister du tout. Ce passage de la détection à la prévention est la raison centrale pour laquelle l'IaC est devenue fondamentale pour la pratique de plateforme moderne.

## Principes clés

- Préférez les définitions déclaratives qui décrivent l'état désiré aux scripts impératifs qui décrivent les étapes.
- Stockez toutes les définitions d'infrastructure dans le contrôle de version, révisées comme tout autre code.
- Traitez l'infrastructure comme immuable : remplacez plutôt que modifier sur place.
- Rendez l'approvisionnement idempotent pour qu'appliquer la même définition à répétition produise le même résultat.
- Détectez et réconciliez la dérive, l'environnement en direct divergeant de sa définition déclarée, continuellement ; le code, pas le système en direct, est la source de vérité.
- Composez l'infrastructure depuis des modules réutilisables et versionnés plutôt que copier-coller.
- Codez la politique comme code, des règles organisationnelles exprimées comme code vérifiable par machine, pour que les garde-fous soient automatiques, pas consultatifs.
- Gardez les secrets hors des définitions ; référencez-les depuis un gestionnaire de secrets dédié.

## Recommandations

### Choisir l'outillage déclaratif et le structurer autour de modules

Adoptez un outil IaC déclaratif, tel que [Terraform](https://fr.wikipedia.org/wiki/Terraform_%28logiciel%29), Pulumi, ou une option cloud native comme CloudFormation, et standardisez dessus à travers l'organisation pour éviter un paysage d'outillage fragmenté. La pratique architecturale clé est la modularité : construisez de petits modules bien documentés et versionnés qui capturent des motifs communs (un réseau conforme, une base de données durcie, un service standard). Les équipes composent ensuite les environnements depuis ces modules plutôt que d'écrire des ressources brutes. Cela répand automatiquement de bonnes valeurs par défaut et paramètres de sécurité et réduit dramatiquement la duplication.

### Gérer l'état délibérément

Les outils déclaratifs suivent le mapping entre le code et les vraies ressources dans un fichier d'état. Stockez l'état à distance dans un backend partagé, chiffré, et à accès contrôlé, et utilisez le verrouillage pour que des modifications concurrentes ne puissent pas le corrompre. Ne gardez jamais l'état sur un ordinateur portable, et ne l'éditez jamais à la main sauf comme action de récupération de dernier recours. L'état est sensible, parce qu'il peut contenir des métadonnées de ressource et secrets, donc protégez-le en conséquence.

### Construire une infrastructure immuable avec des images dorées

Plutôt que de corriger des serveurs en cours d'exécution, cuisez une « image dorée » versionnée (une image de machine ou conteneur pré-configurée et durcie) et déployez de nouvelles instances depuis elle. Quand vous avez besoin d'un changement ou correctif, construisez une nouvelle image et déployez-la, retirant les anciennes instances. Cela élimine la dérive de configuration, rend le retour en arrière trivial, et garde chaque instance identique et traçable à une construction connue-bonne. Les pipelines d'image automatisés devraient inclure le durcissement et scan de sécurité, pour que la conformité soit intégrée au niveau de l'image.

### Détecter et réconcilier la dérive de configuration

La dérive se produit quand l'environnement en direct diverge de sa définition, habituellement parce que quelqu'un a fait un changement manuel d'urgence. Exécutez une détection de dérive régulière qui compare l'état réel à l'état déclaré et signale les différences. Traitez la dérive comme un défaut : réconciliez en mettant à jour le code et réappliquant, pas en laissant le changement manuel en place. Pour les systèmes qui ont besoin d'une imposition de configuration continue, utilisez un outil de gestion de configuration qui converge continuellement les hôtes vers leur état déclaré.

### Adopter GitOps et le déploiement basé sur pull

Dans le modèle GitOps, un dépôt Git tient l'état désiré déclaré du système, et un agent automatisé s'exécutant à l'intérieur de l'environnement cible tire continuellement cet état et réconcilie le système en direct pour correspondre. Cela inverse le modèle push traditionnel. Aucun système externe n'a besoin d'identifiants permanents pour changer l'environnement, parce que l'environnement tire sa propre configuration. GitOps vous donne une piste d'audit complète (chaque changement est un commit), un retour en arrière facile (annuler le commit), et une forte correction de dérive (l'agent réaffirme continuellement l'état désiré). C'est spécialement puissant pour [Kubernetes](https://fr.wikipedia.org/wiki/Kubernetes) et pour les organisations qui veulent une source de vérité unique et révisable.

### Imposer des garde-fous avec la politique comme code

Exprimez les règles organisationnelles, telles que les régions permises, le chiffrement obligatoire, les étiquettes requises, et l'exposition publique interdite, comme politiques vérifiables par machine en utilisant un outil tel qu'Open Policy Agent (OPA) ou un moteur de politique natif de plateforme comme Sentinel. Exécutez ces vérifications dans le pipeline avant l'approvisionnement, pour que les violations soient bloquées automatiquement. La politique comme code transforme l'intention d'une équipe de sécurité en un contrôle exécutable et uniformément appliqué, et cela s'échelonne à des milliers de changements d'une façon que la revue manuelle ne pourrait jamais.

## Compromis : avantages et inconvénients

| Choix | Avantages | Inconvénients | Meilleur ajustement |
|---|---|---|---|
| IaC déclaratif (Terraform/Pulumi) | Reproductible, révisable, dérive détectable | Courbe d'apprentissage ; complexité de gestion d'état | Presque toutes les équipes à l'échelle |
| Scripts impératifs | Familier ; flexible pour les ponctuels | Non idempotent ; difficile à auditer et répéter | Cas étroits et transitoires |
| Immuable + images dorées | Aucune dérive ; retour en arrière trivial | Surcharge de pipeline de construction d'image | Flottes ayant besoin de cohérence |
| Gestion de configuration mutable | Contrôle continu à grain fin | Risque de dérive ; convergence plus lente | Hôtes hérités ou de longue durée |
| GitOps (basé sur pull) | Piste d'audit forte ; auto-guérison | Exige un agent dans le cluster et discipline Git | Kubernetes et cloud natif |
| Politique comme code | Garde-fous automatiques et uniformes | Effort de rédaction de politique en amont | Environnements régulés |

La tension principale est entre la flexibilité et le contrôle. Les approches manuelles et impératives se sentent plus rapides pour un seul changement, mais elles accumulent une incohérence cachée qui devient paralysante à l'échelle. L'infrastructure déclarative, immuable, et gouvernée par politique demande plus d'investissement en amont et un vrai changement culturel, puisque les ingénieurs doivent arrêter de faire des changements de console rapides, mais cela rembourse cet investissement de nombreuses fois en fiabilité, auditabilité, et la capacité de reconstruire n'importe quoi à la demande.

## Questions à discuter avec votre équipe

1. **Qui possède la bibliothèque de modules partagée, et comment une amélioration dans un module atteint-elle chaque équipe qui l'utilise ?** Les modules ne paient que si les corrections et valeurs par défaut durcies se propagent, et cela exige une propriété claire et un vrai versionnage, pas un dossier duquel tout le monde copie. Décidez qui maintient les modules réseau-conforme et base-de-données-durcie, comment vous les versionnez (versionnage sémantique avec journal de modification), et comment les équipes tirent les mises à niveau sans course précipitée. À l'échelle c'est la différence entre corriger une mauvaise configuration une fois et la poursuivre à travers mille ressources éditées à la main. Apportez une preuve : combien de copies distinctes du même motif existent aujourd'hui, combien de temps un correctif de sécurité prend pour atteindre chaque environnement, et si les équipes épinglent les versions de module ou les laissent flotter. Si un correctif critique ne peut pas atteindre le parc entier en jours, votre modularité est cosmétique.

2. **Quelle est votre cadence de détection de dérive, et que se passe-t-il réellement quand une dérive est trouvée ?** La dérive est l'environnement en direct divergeant discrètement de son état déclaré, habituellement depuis un changement de console d'urgence, et la tolérer transforme votre code en fiction. Décidez à quelle fréquence vous comparez l'état réel à l'état déclaré (nocturne est une valeur par défaut raisonnable) et, plus important, décidez la réponse : réconciliez en mettant à jour le code et réappliquant, jamais en laissant le changement manuel en place. Dans les contextes régulés c'est une exigence de contrôle, parce que les auditeurs ont besoin que l'état déclaré corresponde à la réalité continuellement. Apportez vos chiffres actuels : combien de ressources dérivent chaque semaine, combien de temps elles restent dérivées, et si quelqu'un est responsable de les fermer. Traitez chaque dérive comme un défaut avec un propriétaire, ou la garantie de source de vérité s'érode jusqu'à ce que personne ne fasse confiance au code.

3. **Êtes-vous passés à GitOps et la réconciliation basée sur pull, ou un système externe détient-il encore des identifiants permanents pour changer la production ?** Dans le modèle pull un agent à l'intérieur de l'environnement cible réconcilie continuellement le système en direct avec Git, ce qui retire le besoin pour tout système extérieur de détenir l'accès en écriture, et il réaffirme l'état désiré pour que la dérive s'auto-corrige. C'est une forte posture de sécurité et audit, puisque chaque changement est un commit et aucun opérateur n'a besoin d'identifiants de production permanents. Le coût est réel : un agent dans le cluster à exécuter et une discipline Git stricte, donc pesez cela contre votre automatisation basée sur push actuelle. Apportez la liste de qui et quoi peut actuellement muter la production directement, et quelle piste d'audit ces changements laissent. Pour Kubernetes et les enclaves à haute assurance ce changement en vaut habituellement la peine ; pour une poignée de ressources statiques cela peut être excessif.

4. **Comment votre état d'infrastructure est-il stocké, verrouillé, et à accès contrôlé, et que se passe-t-il le jour où il est corrompu ou perdu ?** L'état est la carte entre votre code et les vraies ressources, donc un fichier d'état perdu ou endommagé peut laisser un outil aveugle aux ressources qu'il a créées et tenter quelqu'un vers une réapplication destructrice. Pour une grande équipe le risque se multiplie, parce que de nombreux ingénieurs appliquant contre un état partagé ont besoin d'un backend distant, chiffré, et verrouillé pour que des exécutions concurrentes ne puissent pas s'écraser mutuellement. Pesez la commodité d'un grand état contre le rayon d'explosion qu'il crée, et envisagez de diviser l'état par environnement ou par domaine pour qu'une seule erreur ne puisse pas tout faire tomber. Apportez les faits : où l'état vit aujourd'hui, si le verrouillage est imposé, qui peut le lire (il peut contenir des secrets), et si vous avez déjà répété une récupération. Dans les contextes d'entreprise et gouvernementaux, traitez le backend d'état comme un actif sensible et à accès contrôlé avec sa propre sauvegarde, journal d'audit, et livre d'exécution de récupération, parce que le perdre c'est perdre votre enregistrement de ce qui existe.

5. **Quand une véritable urgence exige un changement manuel, quel est le chemin de bris de verre sanctionné, et comment ce changement est-il replié dans le code ?** Chaque pratique IaC mature rencontre éventuellement l'incident de trois heures du matin où attendre un pipeline n'est pas acceptable, et la vraie question n'est pas si des changements manuels se produisent mais comment vous les contenez. Décidez à l'avance qui peut contourner le pipeline, ce qu'il est autorisé à toucher, comment l'action est journalisée, et le délai auquel le changement doit être réconcilié dans le code ou annulé. Sans cet accord, l'exception d'urgence devient discrètement l'habitude quotidienne et le ClickOps revient par la porte arrière. Apportez une preuve : combien de changements hors bande se sont produits le dernier trimestre, combien de temps chacun est resté non réconcilié, et si la détection de dérive les a réellement attrapés. Pour les organismes régulés et publics, une procédure de bris de verre documentée avec journalisation automatique est souvent une exigence de contrôle, parce que les auditeurs s'attendent à la fois à ce que les urgences soient possibles et que chacune laisse une piste et ramène le système à son état déclaré.

6. **Combien de votre référence de sécurité et conformité est exprimée comme politique qui bloque automatiquement un mauvais changement, contre des règles qui vivent dans un document et comptent sur quelqu'un qui s'en souvient ?** Les garde-fous écrits en prose dans un wiki sont violés routinièrement, parce qu'ils dépendent de chaque ingénieur les lisant et appliquant sous pression de délai, tandis que les mêmes règles exprimées comme politique comme code rejettent un changement non conforme avant qu'il ne soit jamais approvisionné. Pour une grande organisation c'est la seule façon dont l'intention d'une équipe de sécurité s'échelonne à des milliers de changements sans devenir un goulot d'étranglement de revue. Pesez le coût en amont de rédiger et maintenir les politiques contre le coût récurrent de la revue manuelle et remédiation après coup, et décidez quels contrôles (chiffrement, régions approuvées, étiquettes obligatoires, aucune exposition publique) sont assez non négociables pour être imposés comme portes dures. Apportez la liste de vos règles de référence actuelles et marquez lesquelles sont automatisées contre consultatives, plus à quelle fréquence chacune est violée en pratique. Dans les contextes d'entreprise et gouvernementaux, la politique automatisée transforme un audit de semaines de collecte de preuve manuelle en une requête contre des contrôles imposés, et elle transforme la conformité de la détection en prévention.

## Regard sectoriel

**Jeune pousse.** La vitesse gagne, donc placez toute votre pile dans un seul dépôt déclaratif (Terraform est une valeur par défaut commune), gardez l'état dans un backend chiffré géré, et acheminez chaque changement à travers une demande de tirage même avec une équipe de trois. Sautez l'appareil de plateforme lourd : pas d'équipe de module centrale, pas de moteur de politique encore, juste le contrôle de version et la discipline de ne jamais cliquer dans la console. Cela seul vous donne des environnements reproductibles que vous pouvez démolir pour économiser de l'argent et reconstruire pour la prochaine démonstration.

**Petite entreprise.** Sans spécialiste de plateforme dédié, appuyez-vous sur les services gérés et quel que soit l'IaC que votre fournisseur cloud ou vendeur soutient déjà plutôt que de monter un outillage sur mesure que vous ne pouvez pas maintenir. Favorisez acheter une plateforme hébergée dont les valeurs par défaut sensées (chiffrement, sauvegardes, correctifs) sont gérées pour vous plutôt que de construire un pipeline d'image dorée que vous n'avez personne pour exploiter. Cadrez l'objectif étroitement : mettez votre poignée de ressources critiques dans le code pour pouvoir les reconstruire après un échec ou un contractant partant.

**Grande entreprise.** Le problème central est la cohérence à travers de nombreuses équipes, comptes, et régions, donc investissez dans une bibliothèque de module partagée versionnée, un état verrouillé à distance, et une politique comme code imposée dans le pipeline. Une équipe de plateforme centrale publie des modules et garde-fous durcis tandis que les équipes produit se servent elles-mêmes dedans, et la détection de dérive s'exécute continuellement pour que des milliers de ressources restent dans un état connu. Budgétisez le coût continu de maintenir les modules et politiques, parce que leur valeur vient d'une correction ou valeur par défaut durcie se propageant partout à la fois.

**Gouvernement.** Les règles d'approvisionnement, l'accréditation, et la responsabilité publique vous poussent vers l'infrastructure immuable, les commits signés, et la réconciliation GitOps à l'intérieur d'une enclave accréditée, pour qu'aucun opérateur ne détienne d'identifiants permanents pour changer la production. Codez la référence de sécurité requise dans les images dorées et la politique comme code, et laissez l'historique de commit servir de preuve d'audit résistante à la falsification et continuellement disponible. Favorisez l'outillage ouvert et portable aux formats propriétaires qui vous piègent, et rendez la procédure de bris de verre et sa journalisation explicites pour que les changements d'urgence satisfassent encore les exigences de contrôle de configuration.

## Exemples

**Jeune pousse.** Une jeune pousse de cinq personnes définit toute sa configuration AWS, signifiant le VPC, la base de données, et le service de conteneur, dans un seul dépôt Terraform avec l'état gardé dans un backend S3 chiffré et le verrouillage à travers DynamoDB. Chaque changement passe à travers une demande de tirage, donc même un ingénieur d'astreinte solo peut voir exactement ce qui va changer avant d'exécuter apply. Quand ils ont besoin d'un nouvel environnement de pré-production pour une grande démonstration, ils copient un petit module et le montent en minutes, et le démolissent tout aussi vite pour garder la facture cloud basse.

**Grande entreprise.** Un détaillant multinational gère l'infrastructure à travers plusieurs comptes et régions cloud. Une équipe de plateforme centrale publie des modules Terraform versionnés pour les réseaux, bases de données, et échafaudage de service conformes, et impose des politiques OPA qui rejettent toute ressource manquant de chiffrement ou d'étiquettes d'allocation de coût. Les équipes produit approvisionnent leurs propres environnements en libre-service, mais chaque changement coule à travers le pipeline, où la politique est vérifiée automatiquement. La détection de dérive s'exécute nocturnement et ouvre des tickets pour tout changement manuel, gardant des milliers de ressources continuellement dans un état connu et conforme.

**Gouvernement.** Une agence de défense opérant dans un environnement à haute assurance construit des images dorées durcies qui intègrent la référence de sécurité requise, et déploie seulement des instances immuables depuis ces images. Toute l'infrastructure est déclarée dans Git et réconciliée par un agent GitOps à l'intérieur de l'enclave accréditée, pour qu'aucun opérateur ne détienne d'identifiants permanents pour changer la production directement. Chaque changement est un commit signé. Cela donne aux auditeurs un historique complet et résistant à la falsification et satisfait les exigences de surveillance continue et contrôle de configuration sans collecte de preuve manuelle.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur investissement de l'IaC vient de la vitesse, fiabilité, et réduction de risque. Les environnements qui prenaient autrefois des semaines d'approvisionnement manuel piloté par ticket peuvent être créés en minutes, ce qui libère les ingénieurs et accélère les projets. La reproductibilité réduit drastiquement le temps de récupération après les échecs, parce que tout environnement peut être reconstruit depuis le code. L'imposition de politique automatisée réduit la fréquence et le coût des incidents de sécurité et découvertes d'audit, ce qui pour les organisations régulées peut être substantiel.

Sur le registre du coût total de possession, les coûts d'adoption incluent l'outillage, la formation, construire une bibliothèque de module et politique, et la discipline d'arrêter de faire des changements manuels. Le coût de ne pas adopter est plus raide et se compose dans le temps : infrastructure flocon de neige que personne ne peut reconstruire, approvisionnement lent et sujet aux erreurs, mauvaises configurations de sécurité qui mènent à des violations, et audits qui consomment des semaines d'effort manuel. Pour la direction, cadrez l'IaC comme convertir l'infrastructure d'un passif non géré en un actif gouverné et reproductible, et comme le mécanisme qui rend la sécurité et conformité automatiques plutôt qu'aspirationnelles.

## Anti-patterns et pièges

- **ClickOps en production.** Faire des changements à la main dans la console garantit la dérive et détruit la reproductibilité.
- **Secrets dans le code.** Coder en dur des identifiants dans les fichiers de définition les fuit dans l'historique de version et l'état.
- **Définitions monolithiques et non modularisées.** Une énorme configuration que personne n'ose changer devient aussi fragile que la configuration manuelle qu'elle remplace.
- **État non géré.** Les fichiers d'état locaux ou non verrouillés mènent à la corruption et perte d'infrastructure.
- **Dérive tolérée.** Laisser les changements manuels en place érode la garantie de source de vérité jusqu'à ce que le code soit fiction.
- **Politique comme documentation.** Les règles qui vivent dans un wiki au lieu d'une vérification automatisée sont violées routinièrement.
- **Prolifération de copier-coller.** Dupliquer la configuration à travers les équipes signifie que les corrections et améliorations ne se propagent jamais.

## Modèle de maturité

**Niveau 1 (Initier).** L'infrastructure est approvisionnée manuellement à travers la console et scripts au coup par coup. Les environnements sont incohérents, non documentés, et ne peuvent pas être reproduits de façon fiable, et la récupération d'un échec est lente et incertaine.

**Niveau 2 (Développer).** Une certaine infrastructure est codifiée, mais les pratiques varient par équipe. La gestion d'état est incohérente, la dérive est commune, les secrets fuient parfois dans les définitions, et la politique est imposée, si du tout, à travers la revue manuelle.

**Niveau 3 (Standardiser).** L'IaC déclaratif est la norme documentée à travers l'organisation, construite depuis des modules partagés et versionnés avec un état géré, distant, et verrouillé. La politique comme code impose des garde-fous dans le pipeline, les secrets sont référencés depuis un gestionnaire dédié, et la détection de dérive s'exécute selon une cadence régulière.

**Niveau 4 (Gérer).** La pratique est mesurée contre des références. Vous suivez le taux de dérive et le temps moyen pour réconcilier, l'adoption de version de module à travers les équipes, les violations de politique bloquées contre échappées, le délai d'approvisionnement, et la part de ressources réellement sous code. Ces métriques conditionnent les changements et orientent où vous investissez, donc les décisions reposent sur la preuve plutôt que l'anecdote.

**Niveau 5 (Orchestrer).** L'infrastructure est immuable et pilotée par GitOps, auto-guérissante contre la dérive, avec la preuve de conformité produite automatiquement. La bibliothèque de module et politique s'améliore continuellement depuis l'usage réel et les incidents, et la pratique d'infrastructure est intégrée avec la sécurité, le coût, et la planification de livraison pour que le parc entier s'adapte à mesure que les exigences changent.

## Pistes de réflexion

- Où devrait se trouver la ligne entre les modules gouvernés centralement et l'autonomie d'équipe pour définir une infrastructure personnalisée ?
- Comment gérez-vous le vrai changement d'urgence qui doit contourner le pipeline, sans normaliser le ClickOps ?
- Quelle est la bonne stratégie pour gérer et sécuriser l'état à travers de nombreux comptes et équipes ?
- Quand la gestion de configuration mutable est-elle encore justifiée contre l'infrastructure entièrement immuable ?
- Comment gardez-vous la bibliothèque de politique comme code alignée avec les exigences de sécurité et réglementaires évolutives ?
- À quoi ressemble un chemin de migration réaliste pour l'infrastructure héritée qui précède l'IaC ?

## Points clés à retenir

- Définissez l'infrastructure déclarativement, versionnez-la, et traitez-la comme du code révisable et reproductible.
- Construisez depuis de petits modules versionnés pour répandre de bonnes valeurs par défaut et éliminer la duplication.
- Préférez l'infrastructure immuable et les images dorées pour abolir la dérive et simplifier le retour en arrière.
- Gérez l'état délibérément et gardez les secrets hors des définitions.
- Adoptez GitOps pour une piste d'audit forte et une réconciliation auto-guérissante.
- Imposez des garde-fous avec la politique comme code pour que la conformité soit prévenue dans son existence, pas auditée après coup.

## Références et lectures complémentaires

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, et Niall Richard Murphy (éd.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, et John Willis, *The DevOps Handbook*.
- Weaveworks, écrits fondateurs « GitOps » (Alexis Richardson et al.).
- Documentation Open Policy Agent et le langage de politique Rego.
- National Institute of Standards and Technology Special Publication 800-53, contrôles de sécurité et confidentialité (famille gestion de configuration).
