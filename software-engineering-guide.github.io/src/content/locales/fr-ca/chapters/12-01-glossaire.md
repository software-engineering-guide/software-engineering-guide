# 12.1 Glossaire

Ce glossaire définit les termes et acronymes utilisés tout au long du guide. Les entrées sont groupées alphabétiquement. Là où une entrée a un acronyme commun, il est montré entre parenthèses. Les définitions sont intentionnellement concises ; consultez le chapitre pertinent pour un traitement plus complet.

## A

**[ABAC (Contrôle d'accès basé sur les attributs)](https://fr.wikipedia.org/wiki/Attribute-based_access_control)** : Un modèle d'autorisation qui accorde l'accès en se basant sur des attributs évalués de l'utilisateur, la ressource, l'action, et l'environnement (par exemple, département, habilitation, heure du jour) plutôt que des rôles fixes. Il offre un contrôle fin et piloté par politique au coût d'une plus grande complexité que RBAC.

**[Accessibilité (a11y)](https://fr.wikipedia.org/wiki/Accessibilit%C3%A9_num%C3%A9rique)** : La pratique de concevoir et construire du logiciel pour que les gens avec des handicaps puissent le percevoir, le comprendre, y naviguer, et interagir avec lui. Le numéronyme « a11y » abrège les 11 lettres entre « a » et « y » en anglais (accessibility).

**ADR (Enregistrement de décision d'architecture)** : Un document court et versionné qui capture une seule décision architecturale ou technique significative, son contexte, les options considérées, et ses conséquences. Les ADR créent un historique durable et révisable de pourquoi un système est comme il est.

**Agrégat** : Dans la conception pilotée par le domaine, un groupe d'objets de domaine traité comme une seule unité pour les changements de données, avec une entité agissant comme la racine d'agrégat qui applique les invariants. Les agrégats définissent les frontières de cohérence et de transaction.

**[API (Interface de programmation applicative)](https://fr.wikipedia.org/wiki/Interface_de_programmation)** : Un contrat défini à travers lequel une pièce de logiciel demande des services ou données à une autre. Les API bien conçues cachent le détail d'implémentation et fournissent des interfaces stables et versionnées.

**API-first** : Une approche de développement dans laquelle le contrat d'API est conçu et convenu avant l'implémentation, pour que les consommateurs et fournisseurs puissent travailler en parallèle contre une spécification partagée.

**arc42** : Une structure ouverte et basée sur des modèles pour documenter l'architecture logicielle, organisée en douze sections couvrant le contexte, les contraintes, les blocs de construction, l'exécution, le déploiement, et les décisions.

**[ARIA (Applications internet riches accessibles)](https://fr.wikipedia.org/wiki/WAI-ARIA)** : Une spécification W3C définissant les rôles, états, et propriétés qui rendent les composants web dynamiques et personnalisés compréhensibles aux technologies d'assistance comme les lecteurs d'écran.

**ASR (Exigence architecturalement significative)** : Une exigence qui a un effet mesurable et de grande portée sur l'architecture, comme une contrainte de performance, disponibilité, sécurité, ou réglementaire. Les ASR pilotent les décisions de conception les plus conséquentes.

**ASVS (Norme de vérification de sécurité applicative)** : Une norme OWASP qui fournit une liste de contrôle graduée d'exigences et tests de sécurité pour concevoir, construire, et vérifier des applications sécurisées.

**[Mise à l'échelle automatique (Autoscaling)](https://fr.wikipedia.org/wiki/Autoscaling)** : L'ajustement automatique du nombre d'instances de calcul en fonctionnement (ou leur taille) en réponse à la charge, pour que la capacité suive la demande sans intervention manuelle. Elle complète, mais ne remplace pas, la planification de capacité délibérée.

**[Disponibilité](https://fr.wikipedia.org/wiki/Disponibilit%C3%A9)** : La proportion de temps où un système est opérationnel et capable de servir des requêtes, souvent exprimée en « neuf » (par exemple, 99,9 %). C'est une cible de fiabilité centrale codifiée dans les SLO et SLA.

## B

**Contre-pression (Backpressure)** : Un mécanisme de contrôle de flux dans lequel un composant sous charge signale aux producteurs en amont de ralentir, empêchant les files d'attente non bornées et l'échec en cascade. Elle est centrale aux systèmes de diffusion en continu et pilotés par message fiables.

**[BDD (Développement piloté par le comportement)](https://fr.wikipedia.org/wiki/Behavior_driven_development)** : Une pratique collaborative qui exprime les exigences comme des exemples concrets et lisibles par un humain de comportement (souvent en forme Étant donné/Quand/Alors) qui servent aussi de tests d'acceptation automatisés.

**BFF (Backend pour Frontend)** : Un motif architectural dans lequel un service backend dédié est construit pour un type de frontend ou client spécifique, ajustant la forme et l'agrégation de données aux besoins de ce client.

**[BI (Intelligence d'affaires)](https://fr.wikipedia.org/wiki/Informatique_d%C3%A9cisionnelle)** : Les outils, processus, et pratiques pour collecter, intégrer, et analyser les données d'affaires pour soutenir le rapport, les tableaux de bord, et la prise de décision.

**Post-mortem sans blâme** : Une revue d'incident qui se concentre sur les causes systémiques et l'apprentissage plutôt que la faute individuelle, sur la prémisse que les gens agissent raisonnablement compte tenu de l'information et des incitations qu'ils avaient.

**[Déploiement bleu-vert](https://fr.wikipedia.org/wiki/Blue-green_deployment)** : Une stratégie de publication qui exécute deux environnements de production identiques (« bleu » et « vert »), acheminant le trafic vers l'un pendant que l'autre est mis à jour, permettant une bascule et un retour en arrière quasi instantanés.

**[BM25](https://fr.wikipedia.org/wiki/Okapi_BM25)** : Une fonction de classement largement utilisée pour la recherche de texte intégral qui note à quel point un document correspond à une requête en utilisant la fréquence de terme, la fréquence inverse de document, et la longueur de document. C'est le défaut de classement lexical dans de nombreux moteurs de recherche.

**Contexte borné** : Dans la conception pilotée par le domaine, une frontière explicite à l'intérieur de laquelle un modèle de domaine particulier et son langage ubiquitaire s'appliquent de façon cohérente. Elle empêche les concepts d'être confondus à travers différentes parties d'un grand système.

**Cache de construction** : Un magasin de sorties de construction précédemment calculées, indexé par les entrées qui les ont produites, pour que le travail inchangé soit réutilisé plutôt que reconstruit. Un cache de construction distant partagé laisse toute une équipe et sa CI réutiliser les résultats les uns des autres.

**[Facteur bus](https://fr.wikipedia.org/wiki/Facteur_bus)** : Le nombre de personnes qui devraient être perdues (métaphoriquement « frappées par un bus ») avant qu'un projet ne cale par manque de connaissance essentielle. Un facteur bus bas signale une expertise concentrée et non documentée, et un risque organisationnel.

## C

**[Politique d'éviction de cache](https://fr.wikipedia.org/wiki/Algorithme_d%27%C3%A9viction)** : La règle qu'un cache utilise pour décider quelle entrée retirer quand il est plein, comme le moins récemment utilisé (LRU) ou le moins fréquemment utilisé (LFU). La politique façonne le taux de succès et, avec lui, la valeur du cache.

**[Invalidation de cache](https://fr.wikipedia.org/wiki/Invalidation_de_cache)** : Le problème de retirer ou mettre à jour les données en cache une fois que la source sous-jacente change, pour que les lecteurs ne voient pas de valeurs périmées. C'est fameusement l'un des problèmes les plus difficiles en informatique.

**Ruée de cache (Cache stampede)** : Un mode d'échec dans lequel de nombreux clients manquent le cache pour la même clé à la fois et frappent tous l'origine ensemble, la submergeant. La coalescence de requêtes et l'expiration échelonnée la préviennent. Aussi appelée horde tonnante.

**Publication canari** : Une technique de déploiement qui expose une nouvelle version à un petit sous-ensemble d'utilisateurs ou de trafic d'abord, surveille les problèmes, puis étend progressivement le déploiement si les métriques restent saines.

**[Théorème CAP](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_CAP)** : Un principe énonçant qu'un magasin de données distribué peut garantir au plus deux de Cohérence, Disponibilité, et Tolérance au partitionnement simultanément ; parce que les partitions sont inévitables, les concepteurs échangent effectivement la cohérence contre la disponibilité pendant celles-ci.

**[Modèle C4](https://fr.wikipedia.org/wiki/C4_model)** : Une approche légère pour visualiser l'architecture logicielle à quatre niveaux d'abstraction : Contexte système, Conteneurs, Composants, et Code.

**[CD (Livraison continue / Déploiement continu)](https://fr.wikipedia.org/wiki/Livraison_continue)** : La livraison continue garde le logiciel dans un état publiable pour qu'il puisse être déployé à tout moment avec une approbation manuelle ; le déploiement continu publie automatiquement chaque changement qui passe le pipeline.

**[CDN (Réseau de diffusion de contenu)](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_diffusion_de_contenu)** : Un réseau géographiquement distribué de serveurs de périphérie qui met en cache et sert le contenu proche des utilisateurs, coupant la latence et déchargeant l'infrastructure d'origine.

**Sollicitation à chaîne de pensée (Chain-of-thought)** : Une technique de sollicitation qui demande à un modèle de langage de travailler à travers des étapes de raisonnement intermédiaires avant de donner une réponse finale, améliorant la performance sur les problèmes multi-étapes au coût d'une sortie plus longue et plus lente.

**[CI (Intégration continue)](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue)** : La pratique de fusionner fréquemment les changements des développeurs dans une ligne principale partagée, chaque fusion validée par une construction et suite de tests automatisées pour détecter les problèmes d'intégration tôt.

**[CI/CD](https://fr.wikipedia.org/wiki/CI/CD)** : Le pipeline combiné d'intégration continue et de livraison/déploiement continu qui automatise la construction, le test, et la publication du logiciel.

**CMMC (Certification du modèle de maturité de cybersécurité)** : Un programme du Département de la Défense américain qui certifie la maturité de cybersécurité des sous-traitants gérant des informations de contrat fédéral et des informations non classifiées contrôlées.

**[Cohésion](https://fr.wikipedia.org/wiki/Cohesion_%28informatique%29)** : Le degré auquel les éléments à l'intérieur d'un module appartiennent ensemble et servent un but unique et bien défini. Une haute cohésion, associée à un faible couplage, est une marque de conception maintenable.

**Fenêtre de contexte** : La quantité maximale de texte, mesurée en jetons, qu'un modèle de langage peut considérer à la fois, s'étendant sur son entrée et sortie. C'est un budget rare que la conception de prompt et de contexte doit gérer délibérément.

**[Loi de Conway](https://fr.wikipedia.org/wiki/Loi_de_Conway)** : L'observation que la structure d'un système tend à refléter la structure de communication de l'organisation qui le construit. La « manœuvre de Conway inverse » façonne délibérément les équipes pour produire une architecture désirée.

**Core Web Vitals** : Un ensemble de métriques de performance web centrées sur l'utilisateur définies par Google (comme Largest Contentful Paint, Interaction to Next Paint, et Cumulative Layout Shift) qui mesurent le chargement, l'interactivité, et la stabilité visuelle.

**[Coût du délai](https://fr.wikipedia.org/wiki/Cost_of_delay)** : Le coût économique de ne pas avoir quelque chose de terminé encore, exprimé comme la valeur perdue par unité de temps. Le rendre explicite transforme la priorisation d'opinion en arithmétique, et sous-tend les règles de séquencement comme tâche-la-plus-courte-pondérée-en-premier.

**[Couplage](https://fr.wikipedia.org/wiki/Couplage_%28programmation%29)** : Le degré d'interdépendance entre modules ou services. Le couplage lâche limite l'effet d'entraînement du changement et est un but central de la bonne architecture.

**CQRS (Séparation des responsabilités commande-requête)** : Un motif qui sépare le modèle utilisé pour changer l'état (commandes) du modèle utilisé pour lire l'état (requêtes), permettant à chacun d'être optimisé et mis à l'échelle indépendamment.

**[CVE (Vulnérabilités et expositions communes)](https://fr.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)** : Un catalogue public de vulnérabilités de sécurité divulguées, chacune assignée un identifiant unique pour que les outils et équipes puissent référencer le même défaut sans ambiguïté.

**CWV** : Voir Core Web Vitals.

## D

**[DAST (Test de sécurité applicative dynamique)](https://fr.wikipedia.org/wiki/Dynamic_application_security_testing)** : Le test de sécurité qui sonde une application en fonctionnement depuis l'extérieur, sans accès au code source, pour trouver des vulnérabilités qui apparaissent à l'exécution.

**Ratio données-encre (Data-ink ratio)** : Un principe d'Edward Tufte tenant qu'un graphique devrait dépenser la plupart de son encre sur les données elles-mêmes et peu sur la décoration, retirant les lignes de grille, bordures, et fioritures qui n'informent pas.

**[Maillage de données (Data mesh)](https://fr.wikipedia.org/wiki/Data_mesh)** : Une architecture de données décentralisée et modèle opérationnel qui traite les données comme un produit possédé par des équipes de domaine, soutenu par une infrastructure de plateforme en libre-service et une gouvernance fédérée.

**[Visualisation de données](https://fr.wikipedia.org/wiki/Visualisation_de_donn%C3%A9es)** : La pratique d'encoder les données sous forme visuelle (position, longueur, couleur, et similaires) pour que les motifs, comparaisons, et tendances deviennent perceptibles et les décisions mieux informées.

**[DDD (Conception pilotée par le domaine)](https://fr.wikipedia.org/wiki/Conception_pilot%C3%A9e_par_le_domaine)** : Une approche de conception logicielle qui centre le modèle sur le domaine d'affaires, utilisant un langage ubiquitaire partagé, des contextes bornés, et des blocs de construction comme les entités, objets valeur, et agrégats.

**Jetons de conception (Design tokens)** : Des valeurs nommées et agnostiques à la plateforme (couleurs, espacement, typographie, et similaires) qui encodent les décisions de conception pour qu'elles puissent être partagées de façon cohérente à travers un système de conception et de multiples produits.

**DevEx / DevX (Expérience développeur)** : La qualité globale de l'interaction quotidienne d'un développeur avec les outils, plateformes, et processus, englobant la friction, la vitesse de rétroaction, et la charge cognitive.

**[DevOps](https://fr.wikipedia.org/wiki/DevOps)** : Une culture et un ensemble de pratiques qui unissent le développement logiciel et les opérations pour raccourcir les cycles de livraison, augmenter la fréquence de déploiement, et améliorer la fiabilité à travers l'automatisation et la propriété partagée.

**DORA (DevOps Research and Assessment)** : Un programme de recherche et ses quatre métriques de livraison largement utilisées (fréquence de déploiement, délai de livraison pour les changements, taux d'échec de changement, et temps de restauration du service) utilisées pour évaluer la performance de livraison logicielle.

**DPIA (Analyse d'impact relative à la protection des données)** : Une évaluation structurée, exigée sous le RGPD pour le traitement à haut risque, qui identifie et atténue les risques de vie privée avant qu'un projet ne procède.

**Dérive (configuration)** : La divergence graduelle de l'état réel d'un système par rapport à son état déclaré ou visé, communément causée par des changements manuels ; l'infrastructure comme code et GitOps visent à la détecter et la corriger.

**Dérive (modèle)** : En apprentissage automatique, la dégradation de la performance de modèle dans le temps à mesure que les propriétés statistiques des données d'entrée (dérive de données) ou la relation modélisée (dérive de concept) changent.

**[RD (Récupération de désastre)](https://fr.wikipedia.org/wiki/Plan_de_reprise_d%27activit%C3%A9)** : La stratégie, procédures, et infrastructure pour restaurer le service et les données après un événement perturbateur majeur, typiquement gouvernée par des cibles RTO et RPO.

**[DRY (Ne vous répétez pas)](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas)** : Un principe de conception énonçant que chaque pièce de connaissance devrait avoir une représentation unique et faisant autorité, réduisant la duplication et le risque de mises à jour incohérentes.

## E

**Trafic est-ouest** : Le trafic réseau entre services à l'intérieur d'un système ou centre de données, par opposition au trafic nord-sud entre le système et les clients externes. Un maillage de service gouverne typiquement le trafic est-ouest.

**[Informatique de périphérie (Edge computing)](https://fr.wikipedia.org/wiki/Informatique_en_périphérie)** : Exécuter le calcul et le stockage proches d'où les données sont produites ou consommées plutôt que dans un emplacement central, pour couper la latence et la bande passante. Les réseaux de diffusion de contenu en sont une forme précoce et répandue.

**[Élasticité](https://fr.wikipedia.org/wiki/%C3%89lasticit%C3%A9_%28informatique_en_nuage%29)** : La capacité d'un système d'acquérir et libérer automatiquement des ressources en réponse à la demande changeante, pour que la capacité suive la charge de près.

**[ELT (Extraire, Charger, Transformer)](https://fr.wikipedia.org/wiki/Extract-load-transform)** : Un motif d'intégration de données qui charge d'abord les données brutes dans un magasin cible et les transforme là, exploitant l'échelle des entrepôts et lakehouses modernes.

**[Plongement (Embedding)](https://fr.wikipedia.org/wiki/Plongement_lexical)** : Une représentation de texte, images, ou autres données comme un vecteur numérique dense, positionné pour que les éléments similaires se trouvent proches les uns des autres. Les plongements alimentent la recherche sémantique et vectorielle et la génération augmentée par récupération.

**EN 301 549** : La norme européenne spécifiant les exigences d'accessibilité pour les produits et services TIC, référencée par les marchés publics du secteur public à travers l'UE et alignée avec WCAG.

**Budget d'erreur** : La quantité permise d'indisponibilité autorisée par un SLO sur une période ; quand il est épuisé, les équipes priorisent le travail de fiabilité par-dessus les nouvelles fonctionnalités. Il réconcilie la tension entre la vélocité et la stabilité.

**[ETL (Extraire, Transformer, Charger)](https://fr.wikipedia.org/wiki/Extract-transform-load)** : Un motif d'intégration de données qui extrait les données des sources, les transforme en une forme cible, et les charge dans une destination comme un entrepôt.

**[AI Act de l'UE](https://fr.wikipedia.org/wiki/R%C3%A8glement_sur_l%27intelligence_artificielle)** : Le règlement de l'Union européenne qui classifie les systèmes d'IA par risque et impose des obligations en conséquence, interdisant certains usages et régulant fortement les systèmes à haut risque.

**[Cohérence à terme (Eventual consistency)](https://fr.wikipedia.org/wiki/Coh%C3%A9rence_%C3%A0_terme)** : Un modèle de cohérence dans les systèmes distribués dans lequel les répliques peuvent temporairement diverger mais convergent vers le même état une fois que les mises à jour cessent de se propager.

## F

**[Drapeau de fonctionnalité / Bascule de fonctionnalité](https://fr.wikipedia.org/wiki/Feature_toggle)** : Un mécanisme pour activer ou désactiver la fonctionnalité à l'exécution sans redéployer, utilisé pour les déploiements graduels, l'expérimentation, et le contrôle opérationnel.

**Magasin de fonctionnalités (Feature store)** : Un système centralisé pour définir, stocker, et servir des fonctionnalités d'apprentissage automatique sélectionnées de façon cohérente à la fois pour l'entraînement et l'inférence, réduisant la duplication et le décalage entraînement/service.

**[FedRAMP (Programme fédéral de gestion des risques et des autorisations)](https://fr.wikipedia.org/wiki/FedRAMP)** : Un programme gouvernemental américain qui standardise l'évaluation de sécurité, l'autorisation, et la surveillance continue pour les services cloud utilisés par les agences fédérales.

**Sollicitation à quelques exemples (Few-shot prompting)** : Fournir à un modèle de langage une poignée d'exemples travaillés dans le prompt pour démontrer la tâche visée et le format de sortie, par opposition à la sollicitation zero-shot, qui donne des instructions sans exemples.

**FinOps** : Une discipline et pratique culturelle qui apporte la responsabilité financière à la dépense cloud variable, donnant à l'ingénierie, la finance, et les équipes d'affaires une propriété partagée du coût et de la valeur.

**[FISMA (Loi de modernisation de la sécurité de l'information fédérale)](https://fr.wikipedia.org/wiki/Federal_Information_Security_Management_Act)** : Une législation américaine exigeant que les agences fédérales implémentent, documentent, et surveillent des programmes de sécurité de l'information, opérationnalisée largement à travers l'orientation NIST.

**Efficacité de flux** : La proportion du délai de livraison total qu'un élément de travail passe activement travaillé plutôt qu'en attente, calculée comme le temps à valeur ajoutée divisé par le délai de livraison total. La plupart des systèmes sont étonnamment bas, souvent sous 15 pour cent.

**Principe des quatre yeux** : Un contrôle exigeant qu'une action significative soit révisée ou approuvée par au moins deux personnes, réduisant la chance d'erreur ou de malversation.

**[Test par fuzzing (Fuzzing)](https://fr.wikipedia.org/wiki/Fuzzing)** : Une technique de test automatisée qui alimente un programme avec des entrées malformées, aléatoires, ou inattendues pour découvrir des plantages, des défauts de sécurité, et des défauts de cas limites.

## G

**[RGPD (Règlement général sur la protection des données)](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es)** : Le règlement de l'Union européenne gouvernant le traitement des données personnelles, accordant des droits aux individus et imposant des obligations aux responsables et sous-traitants, avec des pénalités significatives pour la non-conformité.

**GitOps** : Un modèle opérationnel qui utilise Git comme la source unique de vérité pour l'infrastructure et les applications déclaratives, avec l'automatisation réconciliant continuellement le système en direct à l'état engagé.

**Chemin doré / Chemin pavé (Golden path / paved road)** : Une façon par défaut bien soutenue et opinionnée de construire et livrer du logiciel à l'intérieur d'une organisation, conçue pour rendre le choix sécurisé, conforme, et fiable le plus facile.

**Enregistrement doré (Golden record)** : En gestion des données maîtresses, la version unique, réconciliée, et faisant autorité d'une entité d'affaires (comme un client) assemblée depuis de multiples systèmes source à travers des règles de correspondance et de survivance.

**[Typage graduel](https://fr.wikipedia.org/wiki/Typage_graduel)** : Une approche de système de type qui laisse le typage statique et dynamique coexister dans une base de code, pour que les types puissent être ajoutés incrémentalement à un programme typé dynamiquement. Les indices de type et vérificateurs de type optionnels en sont des exemples courants.

**[GraphQL](https://fr.wikipedia.org/wiki/GraphQL)** : Un langage de requête et environnement d'exécution pour les API qui laisse les clients demander exactement les données dont ils ont besoin en un seul appel, utilisant un schéma fortement typé.

**[gRPC](https://fr.wikipedia.org/wiki/GRPC)** : Un cadre d'appel de procédure distante haute performance et contrat-d'abord qui utilise HTTP/2 et, typiquement, Protocol Buffers pour une communication service-à-service efficace.

## H

**Construction hermétique (Hermetic build)** : Une construction qui ne dépend que des entrées explicitement déclarées et est isolée de l'environnement hôte, pour qu'elle produise la même sortie n'importe où. L'hermétisme est la fondation des constructions reproductibles et de la mise en cache fiable.

**[HSM (Module de sécurité matériel)](https://fr.wikipedia.org/wiki/Module_mat%C3%A9riel_de_s%C3%A9curit%C3%A9)** : Un dispositif matériel résistant à la falsification qui génère, stocke, et utilise des clés cryptographiques, fournissant une protection de clé plus forte que les approches logicielles seules.

**[HIPAA (Loi sur la portabilité et la responsabilité de l'assurance santé)](https://fr.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)** : Une législation américaine qui, entre autres choses, fixe des exigences pour protéger l'information de santé protégée (PHI) et gouverne son usage et sa divulgation.

**Mise à l'échelle horizontale** : Augmenter la capacité en ajoutant plus d'instances ou de nœuds (« s'étendre »/scaling out) plutôt que de rendre un seul nœud plus puissant. Elle sous-tend la plupart des architectures résilientes à grande échelle.

## I

**[IaC (Infrastructure comme code)](https://fr.wikipedia.org/wiki/Infrastructure_en_tant_que_code)** : La pratique de définir et approvisionner l'infrastructure à travers une configuration lisible par machine et contrôlée en version plutôt que des processus manuels, permettant la reproductibilité et la révision.

**[IAM (Gestion des identités et des accès)](https://fr.wikipedia.org/wiki/Gestion_des_identit%C3%A9s)** : Le cadre de politiques et technologies qui assure que les bonnes identités ont le bon accès aux bonnes ressources aux bons moments.

**IDP / IdP** : « IDP » dénote communément une plateforme de développeur interne, la couche d'outillage en libre-service qui abstrait l'infrastructure pour les équipes produit ; « IdP » dénote un fournisseur d'identité, un service qui authentifie les utilisateurs et émet des assertions. Le contexte désambiguïse les deux.

**[Idempotence](https://fr.wikipedia.org/wiki/Idempotence)** : Une propriété par laquelle effectuer une opération plusieurs fois a le même effet que l'effectuer une fois, essentielle pour les nouvelles tentatives sûres dans les systèmes distribués et API.

**[i18n (Internationalisation)](https://fr.wikipedia.org/wiki/Internationalisation_et_localisation)** : Concevoir et construire le logiciel pour qu'il puisse être adapté à différentes langues, régions, et conventions culturelles sans changements d'ingénierie. Le numéronyme abrège les 18 lettres entre « i » et « n » en anglais.

**Artefact immuable** : Une sortie de construction qui, une fois produite et versionnée, n'est jamais modifiée ; tout changement produit une nouvelle version. L'immuabilité rend les publications reproductibles et vous laisse construire une fois et promouvoir le même artefact à travers les environnements.

**InnerSource** : L'application des pratiques de développement à code source ouvert (transparence, dépôts partagés, et contribution inter-équipes) à l'intérieur d'une seule organisation.

**Dérive IaC** : Voir Dérive (configuration).

**[Index inversé](https://fr.wikipedia.org/wiki/Index_invers%C3%A9)** : La structure de données centrale d'un moteur de recherche, cartographiant chaque terme à la liste de documents qui le contiennent, pour que les requêtes puissent être répondues sans scanner chaque document.

**[ISO/CEI 27001](https://fr.wikipedia.org/wiki/ISO/CEI_27001)** : Une norme internationale spécifiant les exigences pour un système de management de la sécurité de l'information (SMSI), fournissant un cadre certifiable pour gérer le risque de sécurité de l'information.

**ISO/CEI 42001** : Une norme internationale spécifiant les exigences pour un système de management de l'IA, donnant aux organisations un cadre certifiable pour gouverner le développement et l'usage de l'IA de façon responsable.

## J

**[JWT (JSON Web Token)](https://fr.wikipedia.org/wiki/JSON_Web_Token)** : Un format de jeton compact, signé (et optionnellement chiffré) utilisé pour véhiculer des revendications entre parties, communément pour l'authentification et l'autorisation dans les systèmes web et API.

## K

**[Kanban](https://fr.wikipedia.org/wiki/Kanban_%28d%C3%A9veloppement%29)** : Une méthode de flux de travail lean qui visualise le travail sur un tableau, limite le travail en cours, et gère le flux pour améliorer le débit et la prévisibilité.

**[KISS (Gardez ça simple, stupide)](https://fr.wikipedia.org/wiki/Principe_KISS)** : Un principe de conception favorisant la solution la plus simple qui répond au besoin, au motif que la complexité inutile augmente le coût et le risque.

**KMS (Service de gestion de clés)** : Un système pour créer, stocker, faire tourner, et contrôler l'accès aux clés cryptographiques, souvent soutenu par des modules de sécurité matériels.

**[KPI (Indicateur clé de performance)](https://fr.wikipedia.org/wiki/Indicateur_de_performance)** : Une mesure quantifiable utilisée pour suivre le progrès vers un objectif d'affaires ou opérationnel spécifique.

## L

**Lakehouse** : Une architecture de données qui combine le stockage flexible et à bas coût d'un lac de données avec les fonctionnalités de gestion, transactions, et performance d'un entrepôt de données.

**[Délai de livraison (Lead time)](https://fr.wikipedia.org/wiki/D%C3%A9lai_de_livraison)** : Le temps écoulé depuis qu'un changement est demandé (ou engagé) jusqu'à ce qu'il soit livré en production ; une métrique de livraison DORA centrale.

**[Moindre privilège](https://fr.wikipedia.org/wiki/Principe_du_moindre_privil%C3%A8ge)** : Un principe de sécurité accordant à chaque utilisateur, processus, ou système seulement l'accès minimum requis pour effectuer sa fonction, limitant le dommage d'une compromission ou erreur.

**[Loi de Little](https://fr.wikipedia.org/wiki/Loi_de_Little)** : Un résultat de la théorie des files d'attente énonçant que le nombre moyen d'éléments dans un système stable égale le taux d'arrivée moyen multiplié par le temps moyen que chaque élément passe dans le système. Elle lie le travail en cours, le débit, et le délai de livraison.

**[LLM (Grand modèle de langage)](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage)** : Un modèle d'apprentissage automatique entraîné sur de très grands corpus de texte pour prédire et générer du langage, capable de tâches comme le résumé, la traduction, et la génération de code.

**[l10n (Localisation)](https://fr.wikipedia.org/wiki/Localisation_%28traduction%29)** : Adapter le logiciel internationalisé à une locale spécifique, incluant la traduction, le formatage, et les conventions culturelles. Le numéronyme abrège les 10 lettres entre « l » et « n » en anglais.

## M

**[MDM (Gestion des données maîtresses)](https://fr.wikipedia.org/wiki/Gestion_des_donn%C3%A9es_de_r%C3%A9f%C3%A9rence)** : La discipline et l'outillage pour créer et maintenir une vue unique, faisant autorité, et cohérente des entités d'affaires centrales (comme les clients ou produits) à travers les systèmes.

**MITRE ATT&CK** : Une base de connaissances publique et sélectionnée de tactiques et techniques d'adversaire du monde réel, largement utilisée pour planifier les exercices d'équipe rouge, guider l'ingénierie de détection, et décrire les menaces dans un vocabulaire partagé.

**Temps moyen de récupération (MTTR)** : Le temps moyen pris pour restaurer le service après un échec ; une métrique de fiabilité et de gestion d'incident courante.

**[Programmation en essaim (Mob programming)](https://fr.wikipedia.org/wiki/Mob_programming)** : Une pratique dans laquelle toute une équipe travaille ensemble sur la même tâche au même ordinateur, faisant tourner qui tape, pour partager la connaissance et prendre des décisions collectivement.

**[MLOps (Opérations d'apprentissage automatique)](https://fr.wikipedia.org/wiki/MLOps)** : L'ensemble de pratiques qui déploient, surveillent, et maintiennent de façon fiable et efficace les modèles d'apprentissage automatique en production, étendant les principes DevOps au cycle de vie ML.

**[Monorepo](https://fr.wikipedia.org/wiki/Monorepo)** : Un seul dépôt de contrôle de version tenant le code de nombreux projets ou de toute l'organisation, permettant l'outillage partagé et les changements atomiques inter-projets au coût d'un outillage de mise à l'échelle spécialisé.

**mTLS (TLS mutuel)** : Une configuration de la sécurité de la couche transport dans laquelle les deux parties présentent et vérifient des certificats, pour que chacune authentifie l'autre. C'est un défaut pour le trafic service-à-service dans un maillage de service et les réseaux à confiance zéro. Voir aussi l'**[authentification mutuelle](https://fr.wikipedia.org/wiki/Authentification_mutuelle)**.

**[Test de mutation](https://fr.wikipedia.org/wiki/Test_de_mutation)** : Une technique qui introduit délibérément de petits défauts (« mutants ») dans le code pour vérifier si la suite de tests les détecte, mesurant l'efficacité réelle de la suite.

## N

**[NDCG (Gain cumulé actualisé normalisé)](https://fr.wikipedia.org/wiki/Discounted_cumulative_gain)** : Une métrique de qualité de classement qui récompense placer des résultats hautement pertinents près du sommet d'une liste de résultats, normalisée pour que les scores soient comparables à travers les requêtes. C'est un pilier de l'évaluation de pertinence de recherche.

**[NIST (Institut national des normes et de la technologie)](https://fr.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)** : Une agence fédérale américaine dont les publications spéciales et cadres sont des normes largement référencées pour la cybersécurité, la vie privée, et l'IA.

**NIST AI RMF (Cadre de gestion de risque IA)** : Un cadre NIST volontaire pour identifier, évaluer, et gérer les risques associés aux systèmes d'IA à travers leur cycle de vie, organisé autour des fonctions Gouverner, Cartographier, Mesurer, et Gérer.

**[NIST SP 800-53](https://fr.wikipedia.org/wiki/NIST_Special_Publication_800-53)** : Un catalogue NIST de contrôles de sécurité et de vie privée pour les systèmes d'information fédéraux, largement utilisé comme référentiel bien au-delà du gouvernement.

**NIST SP 800-171** : Une publication NIST spécifiant les exigences pour protéger l'information non classifiée contrôlée (CUI) dans les systèmes non fédéraux, centrale à la conformité de sous-traitant de défense.

**[NFR (Exigence non fonctionnelle)](https://fr.wikipedia.org/wiki/Exigence_non_fonctionnelle)** : Une exigence décrivant comment un système devrait se comporter (ses qualités comme la performance, sécurité, fiabilité, ou utilisabilité) plutôt que quelles fonctions il effectue.

**Trafic nord-sud** : Le trafic réseau entre un système et ses clients externes (dedans et dehors du centre de données ou cluster), par opposition au trafic est-ouest entre services internes. Une passerelle API gouverne typiquement le trafic nord-sud.

## O

**Observabilité** : Le degré auquel l'état interne d'un système peut être inféré depuis ses sorties externes, typiquement atteint à travers la télémétrie : métriques, journaux, et traces.

**[OKR (Objectifs et résultats clés)](https://fr.wikipedia.org/wiki/Objectives_and_key_results)** : Un cadre de fixation d'objectifs associant un objectif qualitatif avec quelques résultats clés mesurables pour aligner et concentrer une organisation.

**OpenTelemetry (OTel)** : Une norme et trousse à outils ouverte et neutre en fournisseur pour générer, collecter, et exporter les données de télémétrie (traces, métriques, et journaux) depuis le logiciel.

**OPA (Open Policy Agent)** : Un moteur de politique à code source ouvert et à usage général qui évalue les politiques (écrites dans le langage Rego) pour appliquer les règles d'autorisation et de configuration à travers la pile, permettant la politique comme code.

**OSPO (Bureau de programme de code source ouvert)** : Une fonction organisationnelle qui coordonne la stratégie, gouvernance, conformité, et engagement communautaire de code source ouvert, gérant à la fois la consommation et la contribution.

**[OWASP (Open Worldwide Application Security Project)](https://fr.wikipedia.org/wiki/OWASP)** : Une communauté à but non lucratif qui produit des ressources de sécurité applicative largement utilisées et librement disponibles, incluant le OWASP Top Ten et l'ASVS.

## P

**[PACELC](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_PACELC)** : Une extension du théorème CAP énonçant que s'il y a une Partition, un système échange la Disponibilité contre la Cohérence, Sinon (en opération normale) il échange la Latence contre la Cohérence.

**[PCI DSS (Norme de sécurité des données de l'industrie des cartes de paiement)](https://fr.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)** : Une norme de sécurité maintenue par l'industrie des cartes de paiement qui spécifie les exigences pour les organisations qui stockent, traitent, ou transmettent des données de titulaire de carte.

**[Test d'intrusion](https://fr.wikipedia.org/wiki/Test_d%27intrusion)** : Une attaque autorisée et simulée sur un système par des testeurs qualifiés pour trouver et démontrer des vulnérabilités exploitables avant que de vrais attaquants ne le fassent, livrée comme des résultats priorisés et actionnables.

**[PII (Information personnellement identifiable)](https://fr.wikipedia.org/wiki/Donn%C3%A9e_personnelle)** : L'information qui peut identifier un individu spécifique, seule ou combinée avec d'autres données ; son traitement est gouverné par les lois de vie privée et la politique interne.

**Ingénierie de plateforme** : La discipline de construire et exploiter des plateformes internes en libre-service et des chemins dorés qui réduisent la charge cognitive et accélèrent les équipes produit.

**POUR** : Les quatre principes directeurs des directives d'accessibilité du contenu web : le contenu doit être Perceptible, Utilisable (Operable), Compréhensible, et Robuste.

**Revue de préparation à la production** : Une vérification structurée, exécutée avant qu'un service n'entre en direct ou ne prenne la propriété d'astreinte, qui confirme qu'il respecte les normes d'observabilité, fiabilité, sécurité, livres d'exécution, et soutien opérationnel.

**[Ingénierie de prompt](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie_de_prompt)** : La pratique de concevoir et affiner les instructions, contexte, et exemples donnés à un modèle de langage pour obtenir une sortie fiable et de haute qualité, traitée comme une discipline d'ingénierie versionnée et testée plutôt qu'un essai-erreur.

**[Injection de prompt](https://fr.wikipedia.org/wiki/Injection_de_prompt)** : Une attaque dans laquelle une entrée conçue fait qu'un modèle de langage ignore ses instructions visées et suive celles de l'attaquant à la place, l'analogue à l'ère de l'IA des défauts d'injection. C'est un risque de sécurité central des applications LLM.

**Test basé sur les propriétés** : Une technique de test qui vérifie que des propriétés énoncées tiennent à travers de nombreuses entrées générées automatiquement, plutôt que de dépendre seulement d'exemples choisis à la main.

**Demande de tirage (Pull request, PR) / Demande de fusion (Merge request, MR)** : Un ensemble proposé de changements soumis pour révision et discussion avant d'être fusionné dans une branche partagée, l'unité primaire de revue de code dans la plupart des flux de travail.

**Équipe violette (Purple team)** : Un exercice collaboratif dans lequel les équipes de sécurité offensive (rouge) et défensive (bleue) travaillent ensemble en temps réel, pour que les attaques et les détections censées les attraper soient ajustées l'une contre l'autre.

## Q

**Porte de qualité** : Un point de contrôle automatisé dans un pipeline qui doit être passé (par exemple, respecter les seuils de couverture, sécurité, ou performance) avant qu'un changement ne puisse progresser.

**[Quorum](https://fr.wikipedia.org/wiki/Quorum_%28informatique_distribu%C3%A9e%29)** : Dans les systèmes distribués, le nombre minimum de nœuds qui doivent s'accorder pour qu'une opération (comme une lecture ou écriture) soit considérée réussie, utilisé pour maintenir la cohérence malgré les échecs.

## R

**[RACI](https://fr.wikipedia.org/wiki/Matrice_RACI)** : Un modèle d'assignation de responsabilité qui étiquette chaque participant dans une tâche ou décision comme Responsable, Approbateur, Consulté, ou Informé.

**[RAG (Génération augmentée par récupération)](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_augment%C3%A9e_de_r%C3%A9cup%C3%A9ration)** : Une technique qui ancre la sortie d'un modèle de langage en récupérant d'abord des documents ou données pertinents et en les fournissant comme contexte, améliorant l'exactitude et réduisant l'hallucination.

**[RBAC (Contrôle d'accès basé sur les rôles)](https://fr.wikipedia.org/wiki/Contr%C3%B4le_d%27acc%C3%A8s_bas%C3%A9_sur_les_r%C3%B4les)** : Un modèle d'autorisation qui assigne des permissions à des rôles et des rôles à des utilisateurs, simplifiant l'administration en gérant l'accès au niveau du rôle.

**[Équipe rouge (Red team)](https://fr.wikipedia.org/wiki/%C3%89quipe_rouge)** : Un groupe qui émule un adversaire réaliste, souvent contre une organisation entière et sans avertir les défenseurs, pour tester la détection et la réponse plutôt que simplement énumérer les vulnérabilités. Contraste avec une équipe bleue (défensive).

**Données de référence** : Des listes de codes et classifications contrôlées et changeant lentement utilisées pour catégoriser d'autres données, comme les codes de pays, devises, et valeurs de statut. Les gouverner comme un vocabulaire partagé et versionné garde les systèmes cohérents.

**Rego** : Le langage de politique déclaratif utilisé par Open Policy Agent pour exprimer des règles pour les décisions d'autorisation et de configuration.

**[REST (Transfert d'état représentationnel)](https://fr.wikipedia.org/wiki/Representational_state_transfer)** : Un style architectural pour les applications en réseau qui utilise des opérations sans état sur HTTP sur des ressources adressables, valorisé pour sa simplicité et son large outillage.

**[Proxy inverse](https://fr.wikipedia.org/wiki/Proxy_inverse)** : Un serveur qui se trouve devant un ou plusieurs services backend et transfère les requêtes client vers eux, fournissant communément la terminaison TLS, l'équilibrage de charge, la mise en cache, et un point d'entrée unique.

**[RFC (Demande de commentaires)](https://fr.wikipedia.org/wiki/Request_for_Comments)** : Une proposition écrite circulée pour rétroaction avant une décision technique ou un changement significatif, favorisant la transparence et la propriété partagée. (Le terme nomme aussi la série de documents de normes Internet.)

**[ROI (Retour sur investissement)](https://fr.wikipedia.org/wiki/Retour_sur_investissement)** : Une mesure de la valeur gagnée d'un investissement relative à son coût, utilisée pour justifier et prioriser les décisions d'ingénierie et de technologie.

**[RPA (Automatisation robotisée des processus)](https://fr.wikipedia.org/wiki/Automatisation_robotis%C3%A9e_des_processus)** : Des « robots » logiciels qui automatisent les tâches répétitives et basées sur des règles en interagissant avec les interfaces utilisateur et systèmes existants comme une personne le ferait.

**RPO (Objectif de point de récupération)** : La quantité maximale acceptable de perte de données mesurée en temps (par exemple, « jusqu'à cinq minutes »), définissant à quelle fréquence les données doivent être protégées.

**RTO (Objectif de temps de récupération)** : La durée maximale acceptable pour restaurer un service après une perturbation, guidant la conception et l'investissement de récupération de désastre.

## S

**Saga** : Un motif pour gérer la cohérence de données à travers les services dans une transaction distribuée en séquençant des transactions locales et émettant des actions compensatoires quand une étape échoue.

**[SAFe (Scaled Agile Framework)](https://fr.wikipedia.org/wiki/Scaled_agile_framework)** : Un cadre pour appliquer les pratiques agiles et lean à travers les grandes entreprises, coordonnant de nombreuses équipes ; valorisé pour sa structure et critiqué pour sa lourdeur potentielle.

**[SAST (Test de sécurité applicative statique)](https://fr.wikipedia.org/wiki/Static_application_security_testing)** : Le test de sécurité qui analyse le code source, bytecode, ou binaires sans les exécuter pour trouver des vulnérabilités tôt dans le développement.

**SBOM (Nomenclature logicielle)** : Un inventaire formel et lisible par machine des composants et dépendances dans une pièce de logiciel, utilisé pour gérer le risque de chaîne d'approvisionnement et de vulnérabilité.

**SCA (Analyse de composition logicielle)** : L'outillage qui identifie les composants à code source ouvert et tiers dans une base de code et signale les vulnérabilités connues et risques de licence.

**[Scrum](https://fr.wikipedia.org/wiki/Scrum_%28d%C3%A9veloppement%29)** : Un cadre agile qui organise le travail en itérations à longueur fixe (sprints) avec des rôles, événements, et artefacts définis pour livrer des incréments de valeur.

**Section 508** : Une loi américaine exigeant que les agences fédérales rendent leur technologie électronique et de l'information accessible aux gens avec des handicaps, en pratique alignée avec WCAG.

**Recherche sémantique** : La recherche qui correspond au sens plutôt qu'aux mots-clés exacts, typiquement en comparant les plongements de la requête et des documents. Elle est souvent combinée avec la recherche lexicale dans une approche hybride.

**[Maillage de service (Service mesh)](https://fr.wikipedia.org/wiki/Maillage_de_services)** : Une couche d'infrastructure dédiée, habituellement implémentée avec des proxys sidecar, qui gère les préoccupations de communication service-à-service comme le TLS mutuel, les nouvelles tentatives, les délais d'expiration, le déplacement de trafic, et l'observabilité, les gardant hors du code d'application.

**Sidecar** : Un processus ou conteneur assistant déployé aux côtés d'une instance d'application principale pour fournir des capacités de soutien (comme un proxy de maillage de service) sans changer l'application elle-même.

**[SIEM (Gestion des informations et des événements de sécurité)](https://fr.wikipedia.org/wiki/Security_information_and_event_management)** : Un système qui agrège et corrèle les journaux et événements de sécurité à travers un environnement pour permettre la détection, l'alerte, et l'enquête.

**[SLA (Accord de niveau de service)](https://fr.wikipedia.org/wiki/Accord_de_niveau_de_service)** : Un engagement formel entre un fournisseur de service et ses clients spécifiant les niveaux de service attendus et les conséquences de les manquer.

**SLI (Indicateur de niveau de service)** : Une mesure quantitative d'un aspect de la qualité de service, comme la latence de requête ou le taux d'erreur, qui alimente les SLO.

**SLO (Objectif de niveau de service)** : Une valeur ou plage cible pour un SLI qui définit le niveau désiré de fiabilité, formant la base des budgets d'erreur.

**SLSA (Niveaux de chaîne d'approvisionnement pour les artefacts logiciels)** : Un cadre d'exigences de sécurité graduées pour améliorer l'intégrité et la provenance des artefacts logiciels à travers le processus de construction et de publication.

**SOAR (Orchestration, automatisation, et réponse de sécurité)** : Des outils et pratiques qui automatisent et coordonnent les opérations de sécurité, comme le triage et les livres de jeu de réponse, pour améliorer la vitesse et la cohérence.

**SOC 2 (Contrôles système et organisation 2)** : Un cadre et rapport d'audit, basé sur les critères de services de confiance de l'AICPA, qui évalue les contrôles d'une organisation de service pour la sécurité, disponibilité, intégrité de traitement, confidentialité, et vie privée.

**[SOLID](https://fr.wikipedia.org/wiki/SOLID_%28informatique%29)** : Cinq principes de conception orientée objet (Responsabilité unique, Ouvert/Fermé, Substitution de Liskov, Ségrégation d'interface, et Inversion de dépendance) qui promeuvent un code maintenable et flexible.

**[SOX (Loi Sarbanes-Oxley)](https://fr.wikipedia.org/wiki/Loi_Sarbanes-Oxley)** : Une législation américaine établissant des exigences pour le rapport financier et les contrôles internes dans les entreprises publiques, avec des implications pour les systèmes informatiques qui soutiennent les données financières.

**SPACE** : Un cadre pour mesurer la productivité des développeurs à travers cinq dimensions : Satisfaction et bien-être, Performance, Activité, Communication et collaboration, et Efficacité et flux, mettant en garde contre les mesures à métrique unique.

**[SRE (Ingénierie de fiabilité de site)](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie_de_fiabilit%C3%A9_des_sites)** : Une discipline qui applique les approches d'ingénierie logicielle aux opérations, utilisant les SLO, budgets d'erreur, et l'automatisation pour exploiter des systèmes fiables à l'échelle.

**SSDF (Cadre de développement logiciel sécurisé)** : Le cadre NIST (SP 800-218) de pratiques de développement sécurisé de haut niveau, s'étendant sur la préparation de l'organisation, la protection du logiciel, la production de logiciel bien sécurisé, et la réponse aux vulnérabilités.

**[Analyse statique](https://fr.wikipedia.org/wiki/Analyse_statique_de_programmes)** : Examiner le code source, bytecode, ou binaires sans les exécuter pour trouver des défauts, violations de style, et défauts de sécurité, typiquement à travers des linteurs, vérificateurs de type, et analyseurs dédiés câblés dans l'éditeur et le pipeline.

**[STRIDE](https://fr.wikipedia.org/wiki/STRIDE_%28mod%C3%A8le%29)** : Une taxonomie de modélisation de menace catégorisant les menaces comme Usurpation (Spoofing), Altération (Tampering), Répudiation, Divulgation d'information, Déni de service, et Élévation de privilège.

## T

**[TCO (Coût total de possession)](https://fr.wikipedia.org/wiki/Co%C3%BBt_total_de_possession)** : Le coût de vie complète d'un système ou d'une décision, incluant l'acquisition, l'exploitation, la maintenance, et la retraite éventuelle, pas seulement le prix initial.

**[TDD (Développement piloté par les tests)](https://fr.wikipedia.org/wiki/Test_driven_development)** : Une pratique d'écrire un test automatisé échouant avant le code qui le fait réussir, puis refactoriser, en courts cycles répétés pour piloter la conception et assurer la couverture.

**[Dette technique](https://fr.wikipedia.org/wiki/Dette_technique)** : Le coût futur implicite de choisir une solution expédiente maintenant plutôt qu'une meilleure qui prendrait plus de temps, qui doit être géré délibérément plutôt qu'accumulé inconsciemment.

**TF-IDF (Fréquence de terme-fréquence inverse de document)** : Un schéma de pondération classique qui note l'importance d'un terme pour un document par sa fréquence d'apparition là, compensée par sa fréquence à travers tout le corpus. Il sous-tend une grande partie du classement de recherche lexicale.

**[Théorie des contraintes](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_contraintes)** : Une approche de gestion tenant que le débit d'un système est limité par un seul goulot d'étranglement à tout moment, donc les efforts d'amélioration devraient se concentrer sur cette contrainte jusqu'à ce qu'elle bouge ailleurs.

**[Modélisation de menace](https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_des_menaces)** : Une pratique structurée d'identifier, énumérer, et prioriser les menaces potentielles à un système pour que les défenses puissent être conçues tôt.

**Labeur (Toil)** : En SRE, le travail opérationnel manuel, répétitif, et automatisable qui s'échelonne linéairement avec un service et ne fournit aucune valeur durable ; le réduire libère de la capacité pour l'ingénierie.

**Développement basé sur le tronc** : Une pratique de contrôle de source dans laquelle les développeurs intègrent de petits changements fréquemment dans une seule branche partagée, minimisant les branches à longue durée de vie et la douleur de fusion.

**[Inférence de type](https://fr.wikipedia.org/wiki/Inf%C3%A9rence_de_types)** : Une fonctionnalité de langage qui déduit automatiquement les types des expressions, donnant une grande partie de la sécurité du typage statique sans exiger que chaque type soit écrit à la main.

**[Système de type](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_types)** : L'ensemble de règles qu'un langage utilise pour assigner et vérifier les types, attrapant des classes entières d'erreur avant que le programme ne s'exécute et documentant l'intention. Les systèmes de type vont de dynamique à statique et de faible à fort.

## U

**Langage ubiquitaire** : Dans la conception pilotée par le domaine, un vocabulaire partagé et précis utilisé de façon cohérente par les développeurs et experts de domaine, et reflété directement dans le code et les modèles.

**[UAT (Test d'acceptation utilisateur)](https://fr.wikipedia.org/wiki/Test_d%27acceptation)** : Le test effectué par les utilisateurs finaux ou leurs représentants pour confirmer qu'un système répond aux besoins d'affaires avant qu'il ne soit accepté pour la publication.

**[UX / UI (Expérience utilisateur / Interface utilisateur)](https://fr.wikipedia.org/wiki/Exp%C3%A9rience_utilisateur)** : L'expérience utilisateur est la qualité globale de l'interaction d'une personne avec un produit ; l'interface utilisateur est la surface visuelle et interactive spécifique à travers laquelle cette interaction se produit.

## V

**[Objet valeur](https://fr.wikipedia.org/wiki/Objet_valeur)** : Dans la conception pilotée par le domaine, un objet immuable défini entièrement par ses attributs plutôt qu'une identité distincte, comme un montant d'argent ou une plage de dates.

**[Cartographie de flux de valeur](https://fr.wikipedia.org/wiki/Value-stream_mapping)** : Une technique pour dessiner chaque étape depuis l'idée jusqu'à la valeur livrée, distinguant le temps à valeur ajoutée du temps d'attente, pour que les goulots d'étranglement, transferts, et boucles de retravail deviennent visibles et améliorables.

**[Base de données vectorielle](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_vectorielle)** : Un magasin de données optimisé pour indexer et rechercher des vecteurs de plongement à haute dimension par similarité, une épine dorsale courante de la recherche sémantique et la génération augmentée par récupération.

**Mise à l'échelle verticale** : Augmenter la capacité en rendant un seul nœud plus puissant (« s'étendre vers le haut »/scaling up), ce qui est simple mais finalement borné par la plus grande machine disponible.

**[VCS (Système de contrôle de version)](https://fr.wikipedia.org/wiki/Logiciel_de_gestion_de_versions)** : Un outil, comme Git, qui enregistre les changements aux fichiers dans le temps pour que l'historique puisse être révisé, les branches puissent être maintenues, et le travail puisse être coordonné.

**[Scan de vulnérabilité](https://fr.wikipedia.org/wiki/Scanner_de_vuln%C3%A9rabilit%C3%A9)** : L'inspection automatisée des systèmes, conteneurs, ou code contre des bases de données de faiblesses connues et mauvaises configurations. C'est large et bon marché, et complète la profondeur du test d'intrusion manuel.

## W

**[WCAG (Directives d'accessibilité pour le contenu web)](https://fr.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)** : Un ensemble de directives W3C internationalement reconnues, organisées autour des principes POUR et des niveaux de conformité A, AA, et AAA, pour rendre le contenu web accessible.

**Carte Wardley (Wardley map)** : Une technique de stratégie visuelle qui positionne les capacités par leur valeur pour les utilisateurs et leur maturité évolutive, pour informer les décisions construire/acheter et d'investissement.

**Limite de travail en cours (WIP)** : Un plafond sur combien d'éléments peuvent être dans une étape donnée d'un flux de travail à la fois, une pratique Kanban centrale qui améliore le flux en exposant les goulots d'étranglement et freinant la surcharge de trop de travail parallèle.

**WSJF (Tâche-la-plus-courte-pondérée-en-premier)** : Une méthode de priorisation qui séquence le travail en divisant son coût du délai par sa durée estimée, pour que les éléments les plus courts, les plus sensibles au temps, et de plus haute valeur soient faits en premier.

## X

**[XSS (Cross-Site Scripting)](https://fr.wikipedia.org/wiki/Cross-site_scripting)** : Une vulnérabilité web dans laquelle un attaquant injecte des scripts malveillants qui s'exécutent dans les navigateurs d'autres utilisateurs, potentiellement volant des données ou détournant des sessions.

## Y

**[YAGNI (Vous n'en aurez pas besoin)](https://fr.wikipedia.org/wiki/YAGNI)** : Un principe conseillant contre la construction de fonctionnalités sur spéculation, au motif que les besoins anticipés échouent souvent à se matérialiser et ajoutent du coût et de la complexité.

## Z

**[Confiance zéro (Zero trust)](https://fr.wikipedia.org/wiki/Zero_trust_security_model)** : Un modèle de sécurité qui ne suppose aucune confiance implicite basée sur l'emplacement réseau et vérifie continuellement chaque requête d'accès contre l'identité, l'appareil, et le contexte, suivant la maxime « ne jamais faire confiance, toujours vérifier ».
