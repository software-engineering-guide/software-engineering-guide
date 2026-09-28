# 12.2 Listes de contrôle

Ces listes de contrôle sont des références rapides pratiques et prêtes à l'emploi. Copiez toute liste de contrôle dans un modèle de demande de tirage, une page wiki, un ticket, ou un ordre du jour de réunion de revue, et adaptez les éléments à votre contexte. Traitez chaque élément comme quelque chose qu'une personne peut vérifier et répondre oui ou non. Une liste de contrôle est une aide-mémoire et une norme partagée, pas un substitut au jugement ; supprimez les éléments qui ne s'appliquent pas et ajoutez les éléments que votre domaine exige.

Orientation pour bien les utiliser :

- Gardez les listes de contrôle assez courtes pour que les gens les complètent réellement. Si une liste de contrôle est routinièrement sautée, elle est trop longue ou trop générique.
- Automatisez tout élément qu'une machine peut vérifier (formatage, tests, scans) pour que les humains dépensent leur attention sur les éléments de jugement.
- Versionnez vos listes de contrôle et révisez-les périodiquement. Une liste de contrôle qui ne change jamais n'est probablement pas utilisée.
- Distinguez les éléments bloquants des éléments consultatifs quand la distinction compte pour votre processus.

## Liste de contrôle de revue de code

Pour le réviseur examinant le changement de quelqu'un d'autre.

- [ ] Le changement fait ce que sa description et le ticket lié disent qu'il fait.
- [ ] La portée est concentrée sur une seule préoccupation logique ; les changements non liés sont séparés.
- [ ] La conception s'ajuste à l'architecture existante et n'introduit pas un couplage plus simple à éviter.
- [ ] Les cas limites, chemins d'erreur, et modes d'échec sont gérés, pas seulement le chemin heureux.
- [ ] Des tests existent, sont significatifs, et échoueraient si le comportement régressait.
- [ ] Le nommage, la structure, et les commentaires rendent le code compréhensible pour un futur lecteur.
- [ ] Aucun secret, identifiant, jeton, ou donnée personnelle n'est engagé.
- [ ] L'entrée sensible à la sécurité est validée, encodée, ou paramétrée de façon appropriée.
- [ ] Les interfaces publiques, contrats, et compatibilité ascendante sont préservés ou intentionnellement versionnés.
- [ ] La journalisation, les métriques, et le rapport d'erreur sont adéquats pour exploiter le changement en production.
- [ ] La documentation, les livres d'exécution, et la configuration sont mis à jour pour correspondre au changement.
- [ ] La rétroaction est séparée en problèmes bloquants contre suggestions, et formulée à propos du code.

## Liste de contrôle d'auteur de demande de tirage

Pour l'auteur avant de demander une révision.

- [ ] La PR est assez petite et concentrée pour être révisée soigneusement en une session.
- [ ] La description énonce ce qui a changé, pourquoi, et comment cela a été vérifié.
- [ ] Le ticket, problème, ou document de conception lié donne aux réviseurs le contexte nécessaire.
- [ ] Toutes les vérifications automatisées passent localement ou en CI (construction, linteur, formatage, tests, scans).
- [ ] Le comportement nouveau et changé est couvert par des tests.
- [ ] Les refactorings mécaniques sont séparés des changements de comportement.
- [ ] L'auto-révision est complète : vous avez lu votre propre diff ligne par ligne.
- [ ] Aucun code de débogage, bloc commenté, secret, ou fichier égaré ne reste.
- [ ] Les migrations de base de données, drapeaux de fonctionnalité, et changements de configuration sont documentés et réversibles.
- [ ] Les changements cassants sont signalés explicitement avec un chemin de migration.
- [ ] Des captures d'écran, enregistrements, ou sorties d'exemple sont inclus là où ils aident la révision.
- [ ] Les bons réviseurs et tout approbateur basé sur le rôle requis sont demandés.

## Définition de terminé

La norme partagée qu'un élément de travail doit respecter avant d'être considéré complet.

- [ ] Les critères d'acceptation dans le ticket sont tous respectés et démontrables.
- [ ] Le code est révisé par les pairs et approuvé par les réviseurs requis.
- [ ] Les tests automatisés sont écrits, réussissent, et sont fusionnés avec le changement.
- [ ] Le code est fusionné dans la ligne principale et se déploie proprement à travers le pipeline.
- [ ] Aucun défaut connu du seuil de sévérité convenu ne reste ouvert.
- [ ] La documentation, le texte d'aide, et les livres d'exécution sont mis à jour.
- [ ] L'observabilité est en place : les journaux, métriques, et alertes pertinents existent.
- [ ] Les implications de sécurité et de vie privée ont été considérées et adressées.
- [ ] Les exigences d'accessibilité pour le changement sont respectées là où orienté utilisateur.
- [ ] Les drapeaux de fonctionnalité sont configurés et le plan de déploiement est convenu.
- [ ] Le propriétaire de produit ou la partie prenante a accepté le résultat.
- [ ] Tout travail de suivi est capturé comme des tickets suivis, pas laissé implicite.

## Préparation de lancement de production / mise en service

Avant de livrer un changement significatif ou un nouveau service en production.

- [ ] Le plan de déploiement est documenté, incluant les étapes échelonnées ou canari et les critères de succès.
- [ ] Le plan de retour en arrière est documenté, testé, et peut être exécuté rapidement.
- [ ] Les tests de capacité et de charge montrent que le système respecte la demande attendue et de pic.
- [ ] La surveillance, les tableaux de bord, et les alertes sont en direct et validés avant le lancement.
- [ ] La couverture d'astreinte est planifiée et les répondants connaissent le système.
- [ ] Des livres d'exécution existent pour les scénarios d'échec et opérationnels les plus probables.
- [ ] Les dépendances, intégrations, et tiers sont confirmés prêts et les limites de débit comprises.
- [ ] La revue de sécurité et les approbations requises sont complètes.
- [ ] La migration de données, le cas échéant, est testée de bout en bout avec un retrait vérifié.
- [ ] Les drapeaux de fonctionnalité permettent de désactiver le changement sans redéploiement.
- [ ] Les approbations juridiques, de vie privée, et de conformité sont obtenues là où requis.
- [ ] Le plan de communication couvre les parties prenantes, le support, et les clients.
- [ ] Une décision de lancement ou non est prise par des propriétaires nommés contre des critères explicites.

## Liste de contrôle de revue de sécurité / modèle de menace

Pour évaluer la posture de sécurité d'un changement ou système.

- [ ] Les frontières de confiance et flux de données sont identifiés et documentés.
- [ ] L'authentification est appliquée sur chaque point d'entrée qui l'exige.
- [ ] Les vérifications d'autorisation appliquent le moindre privilège pour chaque action et ressource.
- [ ] Toute entrée externe est validée, et la sortie est encodée pour sa destination.
- [ ] Les secrets sont stockés dans un coffre géré, jamais dans le code ou la configuration, et sont rotables.
- [ ] Les données sont chiffrées en transit et au repos selon ce que la classification exige.
- [ ] Les dépendances sont scannées pour les vulnérabilités connues et gardées à jour.
- [ ] Les risques d'injection, désérialisation, et SSRF sont atténués pour l'entrée non fiable.
- [ ] Les événements pertinents pour la sécurité sont journalisés sans enregistrer de données sensibles.
- [ ] La limitation de débit, les quotas, et les protections contre l'abus gardent les points de terminaison exposés.
- [ ] Les messages d'erreur ne fuient pas les traces de pile, internes, ou détails sensibles.
- [ ] Les menaces identifiées via STRIDE ou similaire sont enregistrées avec des atténuations ou un risque accepté.
- [ ] Le test de sécurité (SAST, DAST, ou test d'intrusion) est planifié ou complet.

## Liste de contrôle de vie privée et protection des données (style DPIA)

Pour le traitement impliquant des données personnelles ou sensibles.

- [ ] Les données personnelles collectées sont inventoriées, classifiées, et minimisées à ce qui est nécessaire.
- [ ] La base légale ou l'autorité pour chaque but de traitement est documentée.
- [ ] La limitation de but est appliquée : les données sont utilisées seulement pour les buts énoncés.
- [ ] Les périodes de rétention sont définies et la suppression ou anonymisation est automatisée.
- [ ] Les droits de la personne concernée (accès, correction, suppression, portabilité) peuvent être satisfaits.
- [ ] Le consentement, là où utilisé, est librement donné, spécifique, et révocable.
- [ ] Les tiers et sous-traitants sont liés par des termes de protection de données adéquats.
- [ ] Les transferts transfrontaliers ont un mécanisme de transfert légal approprié.
- [ ] L'accès aux données personnelles est restreint, journalisé, et révisé.
- [ ] Les risques de vie privée pour les individus sont évalués et atténués ou escaladés.
- [ ] Les processus de détection et notification de brèche de données sont définis.
- [ ] La vie privée dès la conception et les choix par défaut sont documentés pour la fonctionnalité.
- [ ] Le délégué à la protection des données ou le réviseur de vie privée a approuvé là où requis.

## Liste de contrôle d'accessibilité (WCAG)

Pour les interfaces orientées utilisateur, alignées aux principes WCAG.

- [ ] Tout le contenu est atteignable et utilisable en utilisant seulement un clavier.
- [ ] L'ordre de focus est logique et un indicateur de focus visible est présent.
- [ ] Le contraste de couleur du texte respecte le ratio cible (typiquement 4,5:1 pour le texte de corps).
- [ ] Les images et le contenu non textuel ont un texte alternatif significatif.
- [ ] Les champs de formulaire ont des étiquettes associées et des messages d'erreur clairs.
- [ ] Les titres, repères, et la structure sont balisés sémantiquement.
- [ ] Les composants interactifs exposent le nom, rôle, et état corrects aux technologies d'assistance.
- [ ] Le contenu se réorganise et reste utilisable à 200 % de zoom et sur de petits écrans.
- [ ] Les limites de temps sont ajustables, et le contenu en mouvement ou en lecture automatique peut être mis en pause.
- [ ] La couleur n'est pas le seul moyen de transmettre l'information.
- [ ] Les médias ont des sous-titres et, là où nécessaire, des transcriptions ou une description audio.
- [ ] L'interface est testée avec un lecteur d'écran et un outillage d'accessibilité automatisé.

## Liste de contrôle de revue de conception d'API

Avant de publier ou changer une API.

- [ ] Le nommage de ressource et d'opération est cohérent et prévisible.
- [ ] Le contrat est spécifié dans un schéma lisible par machine (par exemple OpenAPI).
- [ ] La stratégie de versionnement est définie et la compatibilité ascendante est préservée ou gérée.
- [ ] La pagination, le filtrage, et le tri suivent des conventions cohérentes.
- [ ] Les réponses d'erreur utilisent une structure, des codes, et des messages actionnables cohérents.
- [ ] L'authentification et l'autorisation sont spécifiées pour chaque opération.
- [ ] La validation d'entrée et les limites de taille sont définies et appliquées.
- [ ] L'idempotence est définie pour les opérations où les nouvelles tentatives sont attendues.
- [ ] Les limites de débit, quotas, et le comportement de limitation sont documentés.
- [ ] Les délais d'expiration, nouvelles tentatives, et la sémantique d'échec sont clairs pour les clients.
- [ ] L'exposition de données sensibles dans les réponses est minimisée et justifiée.
- [ ] La documentation inclut des exemples pour chaque opération et cas d'erreur.
- [ ] La politique de dépréciation et les délais de retrait sont définis.

## Liste de contrôle de revue de décision d'architecture (ADR)

Pour réviser un enregistrement de décision d'architecture proposé.

- [ ] Le contexte et le problème résolu sont énoncés clairement.
- [ ] La décision est énoncée sans ambiguïté comme un choix unique.
- [ ] Au moins deux alternatives réalistes ont été considérées et comparées.
- [ ] Les conséquences, positives et négatives, sont documentées.
- [ ] Les impacts non fonctionnels (performance, sécurité, coût, exploitabilité) sont adressés.
- [ ] La décision s'aligne avec les principes existants et les ADR antérieurs, ou les remplace explicitement.
- [ ] Les équipes et parties prenantes affectées ont été consultées.
- [ ] La réversibilité et le coût du changement sont évalués.
- [ ] Les hypothèses et contraintes sont rendues explicites.
- [ ] Le statut (proposé, accepté, remplacé) est fixé et daté.
- [ ] La décision est découvrable et liée depuis les systèmes pertinents.
- [ ] Toute action de suivi ou migration est capturée comme travail suivi.

## Liste de contrôle de réponse d'incident

Pendant un incident de production actif.

- [ ] Déclarer l'incident et assigner un seul commandant d'incident.
- [ ] Évaluer et communiquer la sévérité, portée, et impact client.
- [ ] Ouvrir un canal de communication dédié et un enregistrement d'incident.
- [ ] Assigner des rôles clairs : commandant, responsable des communications, et responsable des opérations.
- [ ] Prioriser l'atténuation et la restauration du service par-dessus l'analyse de cause racine.
- [ ] Poster des mises à jour de statut régulières aux parties prenantes selon une cadence fixée.
- [ ] Capturer une chronologie d'événements, actions, et décisions à mesure qu'ils se produisent.
- [ ] Escalader vers des répondants ou fournisseurs supplémentaires quand nécessaire.
- [ ] Notifier le juridique, la sécurité, et la conformité si des données ou une réglementation sont impliquées.
- [ ] Vérifier le correctif et confirmer que le système a entièrement récupéré.
- [ ] Fermer formellement l'incident et communiquer la résolution.
- [ ] Planifier le post-mortem sans blâme avant que les gens ne se dispersent.

## Liste de contrôle de post-mortem

Pour la revue rétrospective après un incident.

- [ ] La revue est sans blâme et se concentre sur les systèmes et facteurs contributifs.
- [ ] Une chronologie factuelle et horodatée de l'incident est documentée.
- [ ] L'impact client et d'affaires est quantifié (durée, portée, coût).
- [ ] La détection est analysée : comment et quand le problème a été remarqué.
- [ ] La réponse est analysée : ce qui a aidé et ce qui a ralenti la récupération.
- [ ] Les causes contributives sont identifiées, pas seulement une seule cause racine.
- [ ] Ce qui s'est bien passé est enregistré, ainsi que ce qui s'est mal passé.
- [ ] Les actions sont spécifiques, assignées à des propriétaires, et ont des dates d'échéance.
- [ ] Les actions adressent la prévention, détection, et atténuation.
- [ ] Les éléments de suivi sont suivis jusqu'à l'achèvement dans le carnet normal.
- [ ] Le post-mortem est partagé largement pour que d'autres puissent en apprendre.
- [ ] Les motifs systémiques à travers les incidents sont révisés périodiquement.

## Liste de contrôle de préparation d'astreinte

Avant que quelqu'un ne prenne un quart d'astreinte.

- [ ] Le répondant a accès à tous les systèmes, tableaux de bord, et outils dont il a besoin.
- [ ] L'alerte atteint le répondant de façon fiable et est testée.
- [ ] Les chemins d'escalade et contacts d'astreinte secondaires sont connus et actuels.
- [ ] Des livres d'exécution existent pour les alertes les plus communes et les plus sévères.
- [ ] Le répondant a complété l'intégration ou l'accompagnement pour ces systèmes.
- [ ] Les changements récents, incidents en cours, et problèmes connus sont transférés.
- [ ] Les seuils d'alerte sont ajustés pour minimiser le bruit et les faux appels.
- [ ] Le répondant sait comment déclarer un incident et atteindre le commandant.
- [ ] L'accès à la production est possible depuis l'environnement de travail du répondant.
- [ ] Les canaux de communication et contacts de parties prenantes sont documentés.
- [ ] Le calendrier d'astreinte est publié et la couverture n'a aucun trou.
- [ ] La compensation, les attentes, et les limites de charge pour l'astreinte sont claires.

## Liste de contrôle de définition de SLO

Lors de la définition d'un objectif de niveau de service.

- [ ] Le parcours utilisateur ou capacité que le SLO protège est clairement identifié.
- [ ] Les indicateurs de niveau de service (SLI) sont définis comme des quantités claires et mesurables.
- [ ] Les SLI sont mesurés depuis la perspective de l'utilisateur là où possible.
- [ ] La cible d'objectif est fixée à un niveau dont les utilisateurs ont réellement besoin, pas 100 %.
- [ ] La fenêtre de mesure (par exemple 28 jours glissants) est spécifiée.
- [ ] Le budget d'erreur dérivé de la cible est calculé et compris.
- [ ] Une politique définit ce qui arrive quand le budget d'erreur est épuisé.
- [ ] Les sources de données pour les SLI sont fiables et instrumentées.
- [ ] L'alerte est liée au taux de combustion, pas seulement aux violations de seuil.
- [ ] Les propriétaires et parties prenantes conviennent que le SLO est réaliste et significatif.
- [ ] Le SLO est documenté et visible sur un tableau de bord.
- [ ] Un calendrier existe pour réviser et réviser les SLO à mesure que le service évolue.

## Liste de contrôle de pipeline CI/CD

Pour un pipeline d'intégration et livraison continues.

- [ ] Chaque commit déclenche une construction et exécution de test automatisées.
- [ ] Le pipeline échoue rapidement et rapporte les résultats clairement aux auteurs.
- [ ] Le linting, formatage, et l'analyse statique fonctionnent automatiquement.
- [ ] Les tests unitaires, d'intégration, et de bout en bout pertinents fonctionnent dans le pipeline.
- [ ] Le scan de sécurité et de dépendance fonctionne sur chaque construction.
- [ ] Les artefacts de construction sont versionnés, immuables, et stockés dans un registre.
- [ ] Les secrets sont injectés en sécurité et jamais imprimés dans les journaux.
- [ ] Les déploiements sont automatisés et reproductibles à travers les environnements.
- [ ] La stratégie de déploiement (canari, bleu-vert, progressif) est définie et utilisée.
- [ ] Le retour en arrière est automatisé ou une seule action documentée.
- [ ] Les permissions de pipeline suivent le moindre privilège et sont auditables.
- [ ] La configuration de pipeline est stockée en contrôle de version comme code.
- [ ] La provenance de construction et une nomenclature logicielle sont produites là où requis.

## Liste de contrôle de revue d'infrastructure comme code

Pour réviser l'infrastructure définie comme code.

- [ ] Les changements sont exprimés entièrement en code et appliqués à travers le pipeline.
- [ ] Un plan ou une sortie d'essai à blanc est révisé avant l'application.
- [ ] L'état est stocké en sécurité avec verrouillage pour prévenir les changements concurrents.
- [ ] Les ressources suivent les conventions de nommage, étiquetage, et propriété.
- [ ] Les rôles et politiques IAM à moindre privilège sont utilisés, sans caractères génériques là où évitable.
- [ ] L'exposition réseau est minimisée ; aucun accès public non intentionnel.
- [ ] Les secrets et valeurs sensibles sont référencés depuis un coffre, pas codés en dur.
- [ ] Le chiffrement est activé pour le stockage, bases de données, et transit.
- [ ] Les changements sont idempotents et sûrs à réappliquer.
- [ ] Le rayon d'explosion est compris ; les changements destructifs sont signalés.
- [ ] L'impact de coût du changement est considéré.
- [ ] Les modules sont réutilisables, versionnés, et testés.
- [ ] La détection de dérive est en place pour attraper les changements hors bande.

## Liste de contrôle de publication de modèle IA/ML

Avant de publier un modèle d'apprentissage automatique en production.

- [ ] L'usage visé, la portée, et les limitations du modèle sont documentés.
- [ ] La provenance, licence, et consentement des données d'entraînement et d'évaluation sont vérifiés.
- [ ] Les données et le modèle sont versionnés et reproductibles.
- [ ] La performance est évaluée sur des données de test représentatives et retenues.
- [ ] L'équité et le biais sont évalués à travers les sous-groupes pertinents.
- [ ] Le modèle est évalué contre l'existant ou un référentiel.
- [ ] Les modes d'échec, cas limites, et le comportement hors distribution sont compris.
- [ ] Les risques de sécurité, mésusage, et sortie nuisible sont évalués et atténués.
- [ ] La surveillance de dérive, qualité de données, et dégradation de performance est en place.
- [ ] Un retour en arrière ou repli vers un modèle précédent ou chemin basé sur règles existe.
- [ ] La surveillance ou l'appel humain est fourni pour les décisions conséquentes.
- [ ] La revue de vie privée couvre les données d'entraînement et les entrées et sorties d'inférence.
- [ ] Une fiche de modèle ou documentation équivalente est publiée pour les parties prenantes.

## Liste de contrôle de qualité de pipeline de données

Pour un pipeline de données qui alimente l'analytique ou les produits.

- [ ] Les schémas de données source sont validés et les changements de schéma sont détectés.
- [ ] L'ingestion gère correctement les enregistrements tardifs, dupliqués, et hors ordre.
- [ ] Les vérifications de qualité de données (complétude, unicité, plages) fonctionnent automatiquement.
- [ ] Les enregistrements échoués sont mis en quarantaine et signalés, pas silencieusement abandonnés.
- [ ] Les transformations sont testées avec des entrées représentatives et de cas limite.
- [ ] Le pipeline est idempotent et sûr à réexécuter après échec.
- [ ] La fraîcheur et latence des sorties sont surveillées contre les attentes.
- [ ] La lignée est documentée pour que les consommateurs sachent d'où viennent les données.
- [ ] Les données personnelles et sensibles sont classifiées, masquées, ou restreintes de façon appropriée.
- [ ] Les remplissages et retraitements sont supportés et documentés.
- [ ] L'alerte notifie les propriétaires des échecs et violations de qualité.
- [ ] Les politiques de rétention et suppression sont appliquées sur les données stockées.
- [ ] Les consommateurs en aval et les SLA sont documentés.

## Liste de contrôle d'admission et de revue de licence de code source ouvert

Avant d'adopter un composant à code source ouvert.

- [ ] La licence du composant est identifiée et est sur la liste approuvée.
- [ ] Les obligations de licence (attribution, copyleft, avis) sont comprises et respectées.
- [ ] La compatibilité de licence avec votre modèle de distribution est confirmée.
- [ ] Le projet est activement maintenu et a une communauté saine.
- [ ] Les vulnérabilités connues sont vérifiées et la version est actuelle.
- [ ] La dépendance et ses dépendances transitives sont inventoriées.
- [ ] La posture de sécurité et l'historique d'incidents passés sont révisés.
- [ ] Le composant comble un vrai besoin sans duplication significative.
- [ ] Le coût de sortie et la remplaçabilité du composant sont considérés.
- [ ] Le composant est enregistré dans la nomenclature logicielle.
- [ ] Un propriétaire nommé est responsable de suivre les mises à jour et avis.
- [ ] Les politiques de contribution en retour et de bifurcation interne sont suivies si modifié.

## Liste de contrôle de risque de fournisseur / tiers

Avant d'intégrer un fournisseur ou service externe.

- [ ] Le besoin d'affaires et les données auxquelles le fournisseur accédera sont clairement définis.
- [ ] La posture de sécurité du fournisseur est évaluée (certifications, audits, questionnaire).
- [ ] Les termes de traitement de données, propriété, et suppression à la sortie sont contractuellement clairs.
- [ ] Les sous-traitants et emplacements de données du fournisseur sont divulgués et acceptables.
- [ ] La conformité aux réglementations pertinentes est vérifiée.
- [ ] Les engagements de disponibilité, support, et SLA sont documentés.
- [ ] Les obligations et délais de notification de brèche sont dans le contrat.
- [ ] L'accès est délimité au moindre privilège et révocable.
- [ ] La continuité d'affaires et l'impact d'un échec de fournisseur sont évalués.
- [ ] Un plan de sortie et de migration de données existe pour éviter la dépendance.
- [ ] Les coûts, termes de renouvellement, et clauses de changement de prix sont compris.
- [ ] Le fournisseur est ajouté au registre de risque avec une date de révision.

## Liste de contrôle de préparation de conformité gouvernementale (style ATO / FedRAMP)

Pour les systèmes exigeant une autorisation formelle d'exploiter.

- [ ] La frontière du système et les flux de données sont définis et diagrammés.
- [ ] Les données sont catégorisées par niveau d'impact et sensibilité.
- [ ] Le référentiel de contrôle applicable est sélectionné et adapté.
- [ ] Un plan de sécurité système documente comment chaque contrôle est implémenté.
- [ ] Les contrôles sont implémentés, prouvés, et cartographiés vers le plan.
- [ ] La surveillance continue et le scan de vulnérabilité sont opérationnels.
- [ ] Un plan d'action et de jalons suit les constats ouverts jusqu'à la remédiation.
- [ ] Le contrôle d'accès, la journalisation d'audit, et la gestion d'identité respectent les exigences.
- [ ] Le chiffrement utilise des algorithmes approuvés et des modules validés.
- [ ] Un plan de réponse d'incident est documenté et testé.
- [ ] Un plan de contingence et de récupération de désastre est documenté et testé.
- [ ] Une évaluation ou un audit indépendant des contrôles est complété.
- [ ] Le fonctionnaire autorisant a l'évaluation de risque nécessaire pour accorder l'autorisation.
- [ ] Les déclencheurs de réautorisation et la cadence d'autorisation continue sont définis.
