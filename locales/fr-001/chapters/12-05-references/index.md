# 12.5 Références

Cette section consolide l'appareil de référence du guide : une correspondance avec le corpus de connaissances SWEBOK, un index des normes et cadres cités tout au long, et une bibliographie sélectionnée de lecture recommandée. Les sources par chapitre apparaissent aussi dans la section *Références et lectures complémentaires* à la fin de chaque chapitre.

---

# Correspondance avec SWEBOK

Ce guide est aligné avec le **SWEBOK V4.0** (Software Engineering Body of Knowledge) de l'IEEE Computer Society. Les 18 domaines de connaissance sont couverts ; le tableau associe chacun aux chapitres qui le traitent, et le guide va ensuite bien au-delà de SWEBOK vers l'IA, les données, l'UX, le DevOps, la durabilité, le flux, et la technologie d'intérêt public.

| Domaine de connaissance SWEBOK V4.0 | Chapitres principaux |
|---|---|
| 1. Exigences logicielles | 2.8, 11.1, 5.1 |
| 2. Architecture logicielle | 3.1, 3.2, 3.3 |
| 3. Conception logicielle | 2.2, 3.1 |
| 4. Construction logicielle | 2.9, 2.1 |
| 5. Test logiciel | 2.4, 8.5 |
| 6. Opérations d'ingénierie logicielle | 9.1, 9.2, 9.3, 8.1 |
| 7. Maintenance logicielle | 3.7, 3.6, 10.4 |
| 8. Gestion de configuration logicielle | 2.10, 2.6, 8.2 |
| 9. Gestion de l'ingénierie logicielle | 10.1, 10.6, 10.2 |
| 10. Processus d'ingénierie logicielle | 1.4, 10.7, 10.8 |
| 11. Modèles et méthodes d'ingénierie logicielle | 2.12, 3.1, 2.2 |
| 12. Qualité logicielle | 2.11, 2.4, 3.1 |
| 13. Sécurité logicielle | 4.1, 4.2, 4.3, 4.4 |
| 14. Pratique professionnelle de l'ingénierie logicielle | 10.5, 1.1, 1.3 |
| 15. Économie de l'ingénierie logicielle | 10.10, 10.1, 9.4 |
| 16. Fondements de l'informatique | 2.13, 3.3, 3.4 |
| 17. Fondements mathématiques | 2.13, 11.3 |
| 18. Fondements de l'ingénierie | 2.13, 3.1 |

---

# Normes et cadres

Cette annexe est un index organisé des normes, cadres, et réglementations réels cités tout au long du guide. C'est une aide à la navigation, pas un manuel de conformité : consultez toujours la source faisant autorité et, le cas échéant, un conseil juridique ou d'audit qualifié pour le texte actuel et l'applicabilité à votre contexte.

Les entrées sont groupées par domaine. Chacune nomme la norme ou le cadre, son organisme émetteur, une portée en une ligne, et les chapitres ou domaines où elle est la plus pertinente. Là où un nom est communément abrégé, l'abréviation est indiquée. Les numéros et titres de documents ne sont donnés que là où ils sont bien établis ; aucune URL n'est incluse.

## Comment utiliser cette annexe

- Les **réglementations** (par exemple, RGPD, HIPAA) sont juridiquement contraignantes dans leur juridiction et secteur. Elles fixent des obligations, pas seulement de bonnes pratiques.
- Les **normes** (par exemple, ISO/IEC 27001, WCAG) sont des spécifications formelles, souvent certifiables. Certaines sont volontaires ; certaines sont imposées par la loi ou le contrat.
- Les **cadres** (par exemple, NIST CSF, NIST AI RMF) sont des orientations structurées, généralement volontaires, que vous adaptez à votre profil de risque.
- L'applicabilité dépend de la juridiction, du secteur, des types de données, et des termes contractuels. Beaucoup d'organisations doivent satisfaire plusieurs de ces éléments à la fois.

## Sécurité et vie privée

| Norme / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Exigences pour un système de management de la sécurité de l'information (SMSI). | 4.1–4.6 Sécurité et conformité |
| ISO/IEC 27002 | ISO / IEC | Ensemble de conseils et de contrôles soutenant l'ISO/IEC 27001. | 4.1–4.4 Sécurité |
| ISO/IEC 27017 / 27018 | ISO / IEC | Contrôles de sécurité spécifiques au cloud (27017) et protection des données personnelles dans le cloud (27018). | 4.3 Sécurité de l'infrastructure et du cloud ; 4.5 Vie privée |
| Cadre de cybersécurité du NIST (CSF) | National Institute of Standards and Technology | Cadre volontaire organisé autour de Gouverner, Identifier, Protéger, Détecter, Répondre, Récupérer. | 4.1, 4.4 Fondamentaux et opérations de sécurité |
| NIST SP 800-53 | National Institute of Standards and Technology | Catalogue de contrôles de sécurité et de vie privée pour les systèmes d'information. | 4.3, 4.6 Sécurité et conformité du cloud |
| NIST SP 800-63 | National Institute of Standards and Technology | Lignes directrices d'assurance d'identité numérique et d'authentification. | 4.2, 4.3 Sécurité applicative et de l'infrastructure |
| OWASP Top Ten | Open Worldwide Application Security Project | Les risques de sécurité les plus critiques des applications web, mis à jour périodiquement. | 4.2 Sécurité applicative |
| OWASP ASVS | Open Worldwide Application Security Project | Exigences et tests gradués pour vérifier la sécurité des applications. | 2.4, 4.2 Test et sécurité applicative |
| OWASP SAMM | Open Worldwide Application Security Project | Modèle de maturité pour construire et évaluer un programme de sécurité logicielle. | 4.1 Fondamentaux et culture de sécurité |
| STRIDE | Originaire de Microsoft | Taxonomie de modélisation des menaces pour classifier les menaces. | 4.2 Sécurité applicative |
| MITRE ATT&CK | MITRE | Base de connaissances des tactiques et techniques adverses pour la détection et la défense. | 4.4 Opérations de sécurité |
| SLSA | Open Source Security Foundation (OpenSSF) | Cadre gradué pour l'intégrité et la provenance de la chaîne d'approvisionnement logicielle. | 4.2, 8.1, 10.3 Chaîne d'approvisionnement et livraison |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX) ; OWASP (CycloneDX) | Formats standard pour les nomenclatures logicielles. | 4.2, 10.3 Sécurité applicative et licences |
| PCI DSS | PCI Security Standards Council | Exigences de sécurité pour le traitement des données de carte de paiement. | 4.2, 4.5, 4.6 Sécurité, vie privée, conformité |

## Conformité et gouvernement

### États-Unis

| Réglementation / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| HIPAA | Département américain de la Santé et des Services sociaux | Protections pour les informations de santé protégées (PHI). | 4.5, 4.6 Vie privée et conformité |
| SOX (loi Sarbanes-Oxley) | Congrès américain / SEC | Exigences de reporting financier et de contrôle interne pour les sociétés cotées. | 4.6, 10.2 Conformité et audit |
| FISMA | Congrès américain | Exigences de programme de sécurité de l'information pour les agences fédérales. | 4.3, 4.6 Sécurité et conformité du cloud |
| FedRAMP | Administration des services généraux des États-Unis / FedRAMP PMO | Autorisation de sécurité standardisée pour les services cloud utilisés par les agences fédérales. | 4.3, 4.6 Sécurité et conformité du cloud |
| NIST SP 800-171 | National Institute of Standards and Technology | Protection des informations non classifiées contrôlées (CUI) dans les systèmes non fédéraux. | 4.6 Conformité (chaîne d'approvisionnement de la défense) |
| CMMC | Département de la Défense des États-Unis | Certification de la maturité en cybersécurité des sous-traitants de la défense. | 4.6 Conformité (défense) |
| FIPS 140-3 | National Institute of Standards and Technology | Exigences de sécurité pour les modules cryptographiques. | 4.3 Sécurité de l'infrastructure et du cloud |
| CCPA / CPRA | État de Californie | Droits de vie privée des consommateurs et obligations des entreprises en Californie. | 4.5 Vie privée et protection des données |

### Union européenne et Royaume-Uni

| Réglementation / norme | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| RGPD | Union européenne | Réglementation complète sur le traitement des données personnelles. | 4.5, 4.6 Vie privée et conformité |
| UK GDPR / Data Protection Act 2018 | Royaume-Uni | Le régime de protection des données du Royaume-Uni après le Brexit. | 4.5, 4.6 Vie privée et conformité |
| eIDAS | Union européenne | Cadre pour l'identification électronique et les services de confiance. | 4.2, 4.3 Sécurité |
| Directive NIS2 | Union européenne | Obligations de cybersécurité pour les entités essentielles et importantes. | 4.4, 4.6 Opérations de sécurité et conformité |
| DORA (loi sur la résilience opérationnelle numérique) | Union européenne | Exigences de résilience opérationnelle pour le secteur financier. | 9.1, 10.2 Fiabilité et audit |
| Règlement européen sur l'IA (EU AI Act) | Union européenne | Réglementation fondée sur le risque des systèmes d'IA (voir gouvernance de l'IA ci-dessous). | 6.1, 6.5 Stratégie IA et IA responsable |

## Accessibilité

| Norme | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Lignes directrices pour le contenu web accessible, avec des niveaux de conformité A/AA/AAA. | 5.3 Accessibilité ; 5.1–5.6 UX et frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Rôles, états, et propriétés pour les applications internet riches accessibles. | 5.3, 5.6 Accessibilité et frontend |
| Section 508 | US Access Board / loi fédérale américaine | Exigences d'accessibilité pour les TIC fédérales américaines, alignées sur WCAG. | 5.3 Accessibilité (gouvernement américain) |
| EN 301 549 | ETSI / CEN / CENELEC | Exigences européennes d'accessibilité pour l'approvisionnement en TIC, alignées sur WCAG. | 5.3 Accessibilité (secteur public de l'UE) |
| ADA (loi américaine sur les personnes handicapées) | Congrès américain | Loi sur les droits civiques interdisant la discrimination fondée sur le handicap, appliquée aux services numériques. | 5.3 Accessibilité |
| ISO/IEC 40500 | ISO / IEC | Adoption internationale de WCAG 2.0 comme norme formelle. | 5.3 Accessibilité |

## Gouvernance de l'IA

| Cadre / réglementation | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| Cadre de gestion des risques de l'IA du NIST (AI RMF) | National Institute of Standards and Technology | Cadre volontaire pour gouverner, cartographier, mesurer, et gérer le risque de l'IA. | 6.1, 6.5 Stratégie IA et IA responsable |
| ISO/IEC 42001 | ISO / IEC | Exigences pour un système de management de l'IA (AIMS). | 6.1, 6.5 Gouvernance de l'IA |
| ISO/IEC 23894 | ISO / IEC | Conseils sur la gestion des risques spécifique à l'IA. | 6.5 IA responsable et digne de confiance |
| Règlement européen sur l'IA (EU AI Act) | Union européenne | Obligations légales échelonnées par risque pour les fournisseurs et déployeurs de systèmes d'IA. | 6.1, 6.3, 6.5 Applications et gouvernance de l'IA |
| Principes de l'OCDE sur l'IA | Organisation de coopération et de développement économiques | Principes fondés sur des valeurs pour une IA digne de confiance, influents sur les politiques publiques. | 6.5, 10.5 IA responsable et éthique |

## Qualité et processus

| Norme / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Modèle de qualité du produit logiciel (adéquation fonctionnelle, fiabilité, sécurité, etc.). | 2.2, 2.4 Conception et test |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Processus du cycle de vie du logiciel. | 1.4, 10.1 Façons de travailler et gestion de programme |
| ISO 9001 | ISO | Exigences pour un système de management de la qualité général. | 10.2 Risque, audit, et assurance |
| CMMI | ISACA / CMMI Institute | Modèle de maturité pour la capacité et l'amélioration des processus. | 10.1, 10.2 Gestion de programme et assurance |
| Indicateurs DORA | DevOps Research and Assessment (Google Cloud) | Quatre indicateurs clés de performance de livraison pour les équipes logicielles. | 8.1, 8.4, 9.1 Livraison, plateforme, fiabilité |
| Cadre SPACE | Chercheurs de Microsoft / GitHub | Modèle multidimensionnel pour mesurer la productivité des développeurs. | 1.3, 8.4 Croissance et expérience développeur |
| ITIL | AXELOS / PeopleCert | Cadre de pratiques de gestion des services informatiques. | 9.1, 9.3 Fiabilité et gestion des incidents |

## Architecture

| Norme / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Norme pour la description et les points de vue d'architecture. | 2.7, 3.1 Documentation et fondamentaux de l'architecture |
| TOGAF | The Open Group | Cadre et méthode de développement d'architecture d'entreprise. | 3.1, 10.1 Architecture et gestion de portefeuille |
| Modèle C4 | Communauté (Simon Brown) | Approche à quatre niveaux pour visualiser l'architecture logicielle. | 2.7, 3.1 Documentation et architecture |
| arc42 | Communauté (Starke / Hruschka) | Modèle pour structurer la documentation d'architecture. | 2.7, 3.1 Documentation et architecture |
| ADR | Pratique communautaire | Enregistrements légers des décisions d'architecture significatives. | 1.5, 2.7, 3.1 Prise de décision et documentation |

## Cloud et DevOps

| Norme / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Références de configuration sécurisée fondées sur le consensus pour les systèmes et le cloud. | 4.3, 8.2 Sécurité de l'infrastructure et IaC |
| Paysage et projets CNCF | Cloud Native Computing Foundation | Écosystème et normes pour l'informatique cloud native (par exemple, Kubernetes). | 8.3 Conteneurs et cloud natif |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Normes ouvertes pour les formats d'image et d'exécution de conteneurs. | 8.3 Conteneurs et cloud natif |
| OpenTelemetry | Cloud Native Computing Foundation | Norme neutre vis-à-vis des fournisseurs pour la télémétrie (traces, métriques, journaux). | 9.2 Observabilité et surveillance |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Moteur de politique polyvalent pour la politique en tant que code. | 4.6, 8.2, 8.3 Conformité, IaC, orchestration |
| Pratiques SRE | Google (largement adoptées) | Approche basée sur les SLI/SLO/budgets d'erreur pour exploiter des services fiables. | 9.1 Ingénierie de fiabilité de site |
| Cadre FinOps | FinOps Foundation | Pratiques pour la gestion financière du cloud et la responsabilisation des coûts. | 9.4 Coût, durabilité, logiciel vert |

## Données

| Norme / cadre | Organisme émetteur | Portée (une ligne) | Chapitres / domaines principaux |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Corpus de connaissances organisant les disciplines de gestion des données. | 7.1 Stratégie et gouvernance des données |
| ISO/IEC 38505 | ISO / IEC | Gouvernance des données en tant qu'actif organisationnel. | 7.1 Gouvernance des données |
| ISO 8000 | ISO | Normes de qualité des données et de données de référence. | 7.1, 7.2 Gouvernance et ingénierie des données |
| Data mesh (maillage de données) | Communauté (Zhamak Dehghani) | Approche décentralisée et orientée domaine des données en tant que produit. | 7.1, 7.2 Stratégie et ingénierie des données |
| DCAM | EDM Council | Modèle d'évaluation des capacités de gestion des données. | 7.1 Stratégie et gouvernance des données |

## Remarques sur la portée et le changement

Les normes et réglementations évoluent. Les numéros de version (par exemple, WCAG 2.1 contre 2.2, ou les années de révision ISO) et les catalogues de contrôles changent avec le temps, et de nouvelles lois (comme les réglementations sectorielles sur l'IA et la résilience) continuent d'émerger. Traitez cette annexe comme une carte de départ : confirmez la version actuelle, la juridiction, et l'applicabilité avant de vous appuyer sur une entrée pour une décision de conformité ou d'approvisionnement. Là où les chapitres du guide et cette annexe diffèrent dans le détail, le document source faisant autorité gouverne toujours.


---

# Lectures recommandées

Cette annexe est une liste de lecture sélectionnée et annotée couvrant chaque domaine du guide. Elle privilégie les travaux qui ont façonné la pratique à grande échelle : des classiques reconnus, des références rigoureuses, et les normes et rapports auxquels les équipes de grande entreprise et de gouvernement sont comparées.

Chaque entrée donne le titre et le ou les auteurs, suivis d'une phrase sur son importance. La liste est organisée selon les dix parties du livre. Lisez sélectivement : choisissez les deux ou trois travaux les plus proches de votre douleur actuelle, pas toute l'étagère. Là où un travail couvre plusieurs domaines, il est placé là où il est le plus utile ; beaucoup appartiennent à plusieurs parties.

Une remarque sur les normes : des organismes comme le NIST, l'OWASP, le W3C/WCAG, l'ISO, et le programme DORA publient des documents vivants qui sont révisés périodiquement. Citez et lisez la version actuelle ; les annotations ci-dessous décrivent leur objet durable.

## Fondamentaux : culture, personnes, et processus

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Le fondement de recherche montrant que la performance de livraison prédit la performance organisationnelle, et définissant les indicateurs (aujourd'hui appelés DORA) pour la mesurer.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Un roman d'entreprise qui rend le flux, le travail en cours, et les « trois voies » du DevOps intuitifs pour les leaders comme pour les sceptiques.
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**. Matthew Skelton et Manuel Pais. Un vocabulaire pratique (équipes alignées sur le flux, plateforme, habilitantes, et sous-système complexe) pour concevoir des organisations qui produisent de bons logiciels.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Des cadres éprouvés sur le terrain pour dimensionner les équipes, gérer la croissance organisationnelle, et prendre les décisions récurrentes du leadership d'ingénierie.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Définit les archétypes staff-plus et le chemin de leadership technique pour ceux qui veulent de l'impact sans devenir managers.
- **The Manager's Path**. Camille Fournier. Un guide étape par étape du tech lead au dirigeant qui ancre les échelles de carrière et la transition vers le management.
- **The Staff Engineer's Path**. Tanya Reilly. Un compagnon de la littérature staff-plus centré sur le travail quotidien du leadership technique, de l'influence, et du pilotage sans autorité.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco et Timothy Lister. L'argument durable selon lequel les problèmes centraux du logiciel sont sociologiques, pas techniques.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. L'origine de la loi de Brooks et de la distinction complexité essentielle contre accidentelle qui gouverne encore la dotation en personnel et la planification.
- **The Fearless Organization: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Le fondement de recherche pour la culture sans blâme et la sécurité qui rend possible l'apprentissage par l'échec.
- **Thinking, Fast and Slow**. Daniel Kahneman. Le compte rendu définitif du biais cognitif, essentiel pour les entretiens structurés, la calibration, et la prise de décision honnête.

## Métier de la programmation et qualité du code

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt et David Thomas. Le catalogue fondateur des habitudes professionnelles (DRY, orthogonalité, balles traçantes) qui définit ce que signifie le métier.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Le catalogue canonique des transformations préservant le comportement et la discipline de l'amélioration continue du code soutenue par les tests.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Une norme largement utilisée (et débattue) pour le nommage, les fonctions, et la lisibilité qui façonne les attentes de revue de nombreuses équipes.
- **Code Complete**. Steve McConnell. Un manuel complet et référencé par des preuves des pratiques de construction qui reste une référence approfondie pour la qualité de programmation.
- **Test-Driven Development: By Example**. Kent Beck. L'introduction originale et pratique au cycle rouge-vert-refactorisation et à la conception pilotée par les tests.
- **Working Effectively with Legacy Code**. Michael Feathers. La boîte à outils définitive pour ajouter des tests à du code qui n'en a pas et le modifier sans risque, indispensable pour les systèmes de longue durée.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman et Nat Pryce. Une démonstration travaillée du TDD outside-in, du mocking, et de l'évolution d'une conception à travers les tests.
- **A Philosophy of Software Design**. John Ousterhout. Un traitement tranchant et opiniâtre de la complexité, des modules profonds, et de la dissimulation d'information qui remet utilement en question une partie de l'orthodoxie du « code propre ».

## Architecture et systèmes

- **Designing Data-Intensive Applications**. Martin Kleppmann. La meilleure référence moderne sur les compromis de stockage, de réplication, de partitionnement, de cohérence, et de traitement de flux à grande échelle.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards et Neal Ford. Un large panorama actuel des styles architecturaux, des caractéristiques, et du rôle et de la prise de décision de l'architecte.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Un traitement centré sur la décision des compromis d'architecture distribuée, de la granularité des services, et de la propriété des données.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Introduit les fonctions de fitness et l'architecture conçue pour changer en toute sécurité dans le temps.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. L'origine des contextes bornés, du langage omniprésent, et des agrégats : le vocabulaire de la conception de services moderne.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. La référence pour la décomposition, les frontières de service, le déploiement, et les implications organisationnelles des microservices.
- **Monolith to Microservices**. Sam Newman. Un catalogue de motifs pour la décomposition incrémentale, comme la figue étrangleuse et le branchement par abstraction, sans réécriture risquée en big-bang.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. La référence de motifs nommés (dépôt, unité de travail, et plus) qui a donné un langage partagé aux systèmes d'entreprise.
- **Enterprise Integration Patterns**. Gregor Hohpe et Bobby Woolf. Le catalogue définitif des motifs de messagerie sous-tendant les architectures événementielles et asynchrones.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. La source du disjoncteur, de la cloison, et d'autres motifs de stabilité pour les systèmes qui survivent à la vraie production.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (le « Gang of Four »). Le catalogue historiquement décisif des motifs orientés objet et un vocabulaire de conception partagé.

## Sécurité, vie privée, et confiance

- **Threat Modeling: Designing for Security**. Adam Shostack. Le guide pratique et complet de STRIDE et de la modélisation structurée des menaces comme pratique d'ingénierie routinière.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. La référence encyclopédique sur la façon dont les vrais systèmes échouent et comment en construire qui résistent aux attaques.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Une tournée rigoureuse du modèle de sécurité du navigateur et des façons subtiles dont les plateformes web trahissent des hypothèses naïves.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Un guide de praticien pour utiliser correctement la cryptographie et éviter les erreurs courantes et dangereuses.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). La synthèse de Google de la sécurité et de la fiabilité comme propriétés entrelacées conçues dès le départ.
- **Zero Trust Networks**. Evan Gilman et Doug Barth. Un traitement clair des principes et des mécanismes de l'architecture réseau ne-jamais-faire-confiance-toujours-vérifier.
- **OWASP Top 10**. Fondation OWASP. La base de référence consensuelle des risques de sécurité des applications web les plus critiques, référencée par les politiques et audits dans le monde entier.
- **OWASP Application Security Verification Standard (ASVS)**. Fondation OWASP. Une liste de contrôle graduée et testable d'exigences de sécurité adaptée aux contrats et aux critères d'acceptation.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**. NIST. Le catalogue de contrôles au cœur de la sécurité fédérale américaine et la base de l'autorisation FedRAMP et FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. La structure largement adoptée identifier-protéger-détecter-répondre-récupérer pour organiser un programme de sécurité.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. La définition de référence et les architectures de référence qui ancrent la plupart des programmes de confiance zéro en grande entreprise et au gouvernement.

## UX, UI, et conception de produit

- **The Design of Everyday Things**. Don Norman. Le texte fondateur sur les affordances, les signifiants, le retour, et la conception centrée sur l'humain qui s'applique bien au-delà des objets physiques.
- **Don't Make Me Think, Revisited**. Steve Krug. L'argument concis et durable pour l'utilisabilité évidente et la valeur des tests d'utilisabilité peu coûteux et fréquents.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. La référence complète sur la conception d'interaction, les personas, et la conception orientée but.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Un compte rendu concret de la construction de systèmes de composants cohérents et réutilisables et du langage partagé derrière eux.
- **Refactoring UI**. Adam Wathan et Steve Schoger. Un guide pratique et illustré du soin visuel pour les ingénieurs qui conçoivent des interfaces sans formation formelle.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Le guide définitif de la conception de contenu en langage clair et axée sur la tâche.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering ; Laura Kalbag. Des compagnons pratiques pour construire des interfaces qui fonctionnent pour toute la gamme des capacités humaines.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton et Whitney Quesenbery. Un pont fondé sur des principes entre les normes d'accessibilité et une bonne expérience utilisateur.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. La norme internationalement référencée (perceptible, utilisable, compréhensible, robuste) derrière la plupart des lois sur l'accessibilité.
- **U.S. Web Design System (USWDS)**. Gouvernement des États-Unis. Un exemple concret de système de conception accessible et fondé sur des normes, construit pour les services publics à grande échelle.

## Intelligence artificielle et apprentissage automatique

- **Designing Machine Learning Systems**. Chip Huyen. Le guide pratique de référence pour construire des systèmes d'apprentissage automatique en production de bout en bout : données, caractéristiques, déploiement, et surveillance.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Étend la discipline SRE (SLO, surveillance, réponse aux incidents) aux systèmes d'apprentissage automatique.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. La référence académique standard pour la théorie et les méthodes sous-jacentes aux réseaux de neurones modernes.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Un guide actuel pour concevoir, évaluer, et exploiter des applications construites sur de grands modèles de fondation.
- **Weapons of Math Destruction**. Cathy O'Neil. Un plaidoyer saisissant pour la responsabilité algorithmique et les préjudices réels des modèles non examinés, essentiel pour l'IA du secteur public.
- **Interpretable Machine Learning**. Christoph Molnar. Une référence complète et librement disponible sur les méthodes d'explicabilité pour les modèles et leurs prédictions.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Le cadre de référence pour gouverner, cartographier, mesurer, et gérer le risque de l'IA, de plus en plus cité dans les politiques publiques et l'approvisionnement.

## Données, analytique, et perspicacité

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. Ralph Kimball et Margy Ross. La référence canonique sur les schémas en étoile et la modélisation dimensionnelle pour l'analytique.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Le guide faisant autorité pour mener des expériences qui produisent des résultats fiables et exploitables à grande échelle.
- **Fundamentals of Data Engineering**. Joe Reis et Matt Housley. Une carte neutre vis-à-vis des fournisseurs du cycle de vie moderne des données et des pratiques d'ingénierie qui le soutiennent.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Le texte fondateur de l'approche orientée domaine et centrée produit de l'organisation des données à grande échelle.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Un guide pratique de la visualisation de données honnête et claire et de la communication de perspicacité aux décideurs.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. L'ouvrage fondateur sur l'intégrité graphique, l'encre-donnée, et l'éthique de la présentation honnête des données.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Le cadre de référence complet pour la gouvernance, l'intendance, la qualité, et le catalogage des données.
- **The Book of Why**. Judea Pearl et Dana Mackenzie. Une introduction accessible à l'inférence causale, vitale pour passer de la corrélation à des décisions défendables.

## Automatisation, DevOps, et ingénierie de plateforme

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Le manuel complet traduisant les « trois voies » en pratiques concrètes pour le flux, le retour, et l'apprentissage continu.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble et David Farley. Le texte fondateur sur les pipelines de déploiement, l'automatisation, et la publication de logiciels en toute sécurité et fréquemment.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. La référence sur le traitement de l'infrastructure comme un logiciel : modules, tests, immuabilité, et dérive.
- **Team Topologies**. Matthew Skelton et Manuel Pais. (Voir Fondamentaux.) Également essentiel ici pour façonner les équipes de plateforme et l'expérience développeur qu'elles fournissent.
- **Kubernetes Patterns**. Bilgin Ibryam et Roland Huß. Un catalogue de motifs réutilisables pour concevoir des applications cloud natives sur Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Comment des pratiques d'ingénierie comme le test, la revue, l'outillage, et la gestion des dépendances passent à l'échelle de dizaines de milliers d'ingénieurs sur des décennies.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Le manifeste concis et influent pour construire des services portables, scalables, et cloud natifs.
- **DORA State of DevOps Report**. DORA / Google Cloud (annuel). Le programme de recherche continu derrière les quatre indicateurs clés de livraison et les capacités qui pilotent la performance.

## Opérations, fiabilité, et observabilité

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (dir.). Le texte fondateur définissant les SLI, SLO, budgets d'erreur, et la discipline de l'ingénierie de la fiabilité.
- **The Site Reliability Workbook**. Betsy Beyer et al. (dir.). Le compagnon pratique avec des exemples concrets, des SLO travaillés, et des conseils de mise en œuvre.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. La définition moderne de l'observabilité, des données à haute cardinalité, et du débogage des inconnues-inconnues en production.
- **Implementing Service Level Objectives**. Alex Hidalgo. Un guide approfondi et pratique pour bien concevoir, mesurer, et utiliser les SLO et les budgets d'erreur.
- **Release It!**. Michael T. Nygard. (Voir Architecture.) Également fondateur ici pour les motifs de stabilité en production et l'exploitation de systèmes résilients.
- **The Art of Capacity Planning**. Arun Kejariwal et John Allspaw. Une approche fondée sur les données pour prévoir la demande et planifier la capacité pour des systèmes en croissance.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal et Nora Jones. Le traitement définitif de l'injection délibérée de défaillance pour construire la confiance dans la résilience du système.
- **Google SRE Book, chapitre sur les post-mortems**. Google. Le modèle largement imité pour les post-mortems sans blâme et l'apprentissage par les incidents.

## Grande entreprise, gouvernement, et l'intérêt public

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. L'étude essentielle de la façon dont le code source ouvert est réellement soutenu, et du fardeau des mainteneurs derrière les dépendances dont dépendent les grandes entreprises.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Un compte rendu lucide des raisons pour lesquelles la technologie du secteur public échoue et de la façon dont une réforme axée sur la livraison peut y remédier.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Des leçons du service numérique du gouvernement britannique sur la transformation des services publics par la livraison, pas la planification.
- **Project to Product**. Mik Kersten. Le Flow Framework pour faire passer les grandes entreprises d'un financement par projet à des flux de valeur produit durables.
- **Escaping the Build Trap**. Melissa Perri. Comment les organisations confondent production et résultat, et comment la gestion de produit corrige cela, avec une pertinence directe pour la gouvernance de portefeuille et de programme.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Un ensemble concis de pratiques pour livrer des services numériques gouvernementaux efficaces et centrés sur l'utilisateur.
- **GOV.UK Service Manual and Service Standard**. Service numérique du gouvernement britannique. Une norme concrète et publiée pour construire de bons services publics, largement imitée par d'autres gouvernements.
- **NIST SP 800-37: Risk Management Framework**. NIST. Le cadre de processus derrière l'autorisation d'exploiter (ATO) et la surveillance continue dans les systèmes fédéraux américains.
- **The FinOps Foundation Framework**. FinOps Foundation. Le modèle de référence pour la visibilité, l'optimisation, et la responsabilisation des coûts du cloud à travers la finance et l'ingénierie.

## Comment utiliser cette liste

- **Commencez par votre douleur.** Si les déploiements sont lents et effrayants, lisez *Accelerate*, *Continuous Delivery*, et les rapports *DORA* avant tout le reste.
- **Lisez pour la décennie, pas le sprint.** Préférez les travaux qui expliquent des principes durables à ceux liés à une version d'outil spécifique.
- **Vérifiez l'édition actuelle des normes.** Le NIST, l'OWASP, le WCAG, l'ISO, et DORA révisent leurs publications ; travaillez toujours à partir de la dernière version et notez le numéro de version dans vos propres politiques.
- **Construisez une étagère partagée.** Une équipe qui a lu deux ou trois de ces livres en commun se dispute moins et décide plus vite, parce qu'elle partage un vocabulaire et un ensemble de points de référence.
- **Voir aussi le chapitre 12.5** pour l'index complet des normes et cadres de référence, et le **chapitre 12.6** pour comment séquencer l'adoption des pratiques que ces travaux décrivent.
