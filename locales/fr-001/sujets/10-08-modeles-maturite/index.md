# 10.8 Modèles de maturité

## Vue d'ensemble et motivation

Un **[modèle de maturité](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_maturit%C3%A9)** est une façon structurée d'évaluer à quel point votre pratique est capable et cohérente dans un domaine, et de décrire un chemin pour l'améliorer. Il définit une petite échelle de niveaux. En bas, le travail est ad hoc et réactif. En haut, il est mesuré, géré, et s'optimise continuellement. Chaque échelon a des caractéristiques observables contre lesquelles vous pouvez vérifier.

Les modèles de maturité transforment une question vague (« sommes-nous bons à cela ? ») en une réponse reproductible (« nous sommes au niveau 2 ici, niveau 4 là, et voici ce que le niveau 3 exigerait »). Ce livre utilise un modèle à cinq niveaux dans chaque chapitre et les consolide au chapitre 12.4. Ce chapitre parle de la discipline elle-même : comment les modèles fonctionnent, quand ils aident, et comment ils induisent en erreur.

La raison pour laquelle ils comptent est simple. Les grandes organisations ne peuvent pas améliorer ce qu'elles ne peuvent pas voir. À travers des dizaines d'équipes, la capacité varie énormément et invisiblement. Certaines équipes ont d'excellents tests et une sécurité faible ; d'autres ont l'inverse. Un modèle de maturité vous donne un vocabulaire partagé et une jauge commune, pour que les écarts deviennent comparables, l'investissement puisse être priorisé, et le progrès puisse être suivi dans le temps plutôt que simplement affirmé. Des exemples bien connus incluent CMMI (**[Capability Maturity Model Integration](https://fr.wikipedia.org/wiki/Capability_Maturity_Model_Integration)**, pour le processus), le modèle DORA (**[DevOps Research and Assessment](https://fr.wikipedia.org/wiki/DevOps#DORA)**) (performance de livraison logicielle), OWASP SAMM (Software Assurance Maturity Model) et BSIMM (Building Security In Maturity Model) pour la sécurité logicielle, TMMi (Test Maturity Model integration, pour le test), le modèle Agile Fluency, et les modèles de maturité de gestion de données, plus d'innombrables tableaux de bord internes.

Pour l'entreprise et spécialement le gouvernement, les modèles de maturité portent un poids particulier. Les marchés publics gouvernementaux utilisent depuis longtemps les niveaux d'évaluation CMMI comme qualification de fournisseur, et des cadres comme le CMMC américain (**[Cybersecurity Maturity Model Certification](https://fr.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)**) lient directement la maturité de cybersécurité à l'éligibilité pour le travail de défense. Cela donne aux modèles de maturité de vraies dents. Cela crée aussi le risque central de ce chapitre : quand un niveau devient une porte ou une cible, les gens optimisent pour l'évaluation plutôt que la capacité sous-jacente. Bien utilisés, les modèles de maturité sont un miroir. Mal utilisés, ils sont du théâtre.

## Principes clés

- **La maturité est un moyen, pas une fin.** Le but est la capacité et les résultats, pas un chiffre de niveau.
- **Évaluez pour apprendre, pas pour marquer.** Une auto-évaluation honnête bat une évaluation flatteuse.
- **Plus haut n'est pas toujours meilleur.** La bonne cible dépend du risque, du contexte, et du coût.
- **Mesurez par domaine, pas une note globale unique.** La capacité est inégale ; un seul chiffre la cache.
- **Priorisez d'abord les écarts de maturité la plus basse et de risque le plus élevé.**
- **Méfiez-vous de la [loi de Goodhart](https://fr.wikipedia.org/wiki/Loi_de_Goodhart).** Une fois qu'un niveau devient une cible, il cesse de mesurer la capacité.
- **Réévaluez périodiquement.** La maturité dérive à mesure que les gens, systèmes, et menaces changent.

## Recommandations

### Choisir le bon modèle pour le domaine

Assortissez le modèle à la capacité que vous voulez améliorer, et préférez les modèles établis et fondés sur des preuves aux modèles inventés là où ils existent :

- **Processus et livraison :** CMMI (maturité de processus large), le modèle de capacité DORA (performance de livraison, ancré dans la recherche, chapitre 11.2).
- **Sécurité :** OWASP SAMM et BSIMM (pratiques de sécurité logicielle), CMMC (cybersécurité de défense).
- **Test et qualité :** TMMi.
- **Agile et façons de travailler :** le modèle Agile Fluency (chapitre 10.7).
- **Données :** modèles de maturité de gestion de données (DMM, DCAM).

Pour un usage interne, une échelle simple à quatre ou cinq niveaux appliquée par capacité (comme ce livre le fait) est souvent plus actionnable qu'un cadre externe lourd. Réservez les modèles formels et évalués là où ils sont contractuellement requis.

### Évaluer honnêtement et par capacité

Menez des évaluations qui produisent la vérité, pas le confort. Impliquez les gens qui font le travail. Rassemblez des preuves plutôt que des opinions. Notez chaque capacité séparément, pour que l'image reflète la réalité : forte ici, faible là. Une auto-évaluation utilisée pour guider l'amélioration vaut plus qu'une évaluation externe utilisée pour gagner un badge, parce que la première récompense la franchise et la seconde récompense la présentation. Le chapitre 12.4 fournit une auto-évaluation consolidée à travers chaque domaine de ce livre ; utilisez-la comme instrument de départ.

### Utiliser la maturité pour prioriser, pas pour punir

La sortie d'une évaluation est un carnet d'amélioration priorisé, pas un bulletin pour le blâme. Combinez la maturité avec le risque. Une capacité de niveau 1 dans une zone à faible risque peut être bien. Une capacité de niveau 2 dans une zone critique pour la sécurité ou la conformité est urgente. Dirigez l'investissement vers les écarts où la faible maturité rencontre le risque élevé, et connectez le travail aux résultats (chapitre 11.1) pour que l'amélioration soit mesurée par les résultats, pas en grimpant l'échelle pour elle-même.

### Fixer les niveaux cibles délibérément : plus haut n'est pas gratuit

Chaque niveau supplémentaire coûte de l'effort et ajoute souvent du poids de processus. La bonne cible est rarement « niveau 5 partout ». C'est le niveau où la capacité supplémentaire justifie encore le coût supplémentaire pour le risque de ce domaine. Les capacités régulées et critiques pour la sécurité peuvent véritablement avoir besoin des échelons supérieurs, et l'audit exige souvent au moins un niveau 3 « défini ». Beaucoup d'autres sont bien servies au niveau 3 et n'accumuleraient que de la bureaucratie en poussant plus loin. Décidez les cibles par capacité, et arrêtez de grimper quand le retour ajusté au risque s'arrête.

### Se garder contre le théâtre de maturité

Le seul mode d'échec qui détruit la valeur des modèles de maturité est d'optimiser pour le score. Surveillez les évaluations qui notent généreusement, les preuves assemblées seulement pour l'évaluation, ou les affirmations de « niveau 5 » que les incidents de production contredisent. Gardez l'évaluation liée au comportement observable et aux vrais résultats. Faites tourner ou vérifiez extérieurement vos évaluateurs. Traitez un auto-score suspicieusement élevé comme une odeur. Au moment où le niveau devient le but, le modèle cesse de vous dire la vérité.

## Compromis : avantages et inconvénients

| Approche | Avantages | Inconvénients |
|---|---|---|
| **Modèles formels évalués (CMMI, CMMC)** | Comparables, contractuellement reconnus, rigoureux | Coûteux ; invite la manipulation ; peut ossifier le processus |
| **Tableaux de bord internes légers** | Rapides, actionnables, faible surcharge | Moins comparables extérieurement ; facile à biaiser |
| **Modèles de capacité fondés sur des preuves (DORA)** | Liés à de vrais résultats ; soutenus par la recherche | Portée plus étroite ; a besoin de vraies métriques |
| **Une seule note de maturité globale** | Simple à communiquer | Cache la capacité inégale ; induit en erreur |
| **Évaluation par capacité** | Priorisation précise et actionnable | Plus d'effort ; pas de chiffre vedette unique |

La tension centrale est **l'évaluation comme miroir contre l'évaluation comme cible**. Le même modèle qui aide une équipe à se voir clairement devient contre-productif à l'instant où un niveau est lié à la récompense, l'éligibilité, ou le statut. Plus un niveau compte, plus l'énergie s'écoule vers l'apparence de maturité plutôt que la substance.

## Questions à discuter avec votre équipe

1. **Devrions-nous garder une auto-évaluation interne franche séparée de tout niveau évalué contractuellement, et qui possède chacune ?** Quand un niveau CMMC ou CMMI conditionne le revenu, l'évaluation et la vérité dérivent l'une de l'autre, parce que l'énergie s'écoule vers réussir plutôt qu'améliorer. Pour une grande entreprise ou un fournisseur gouvernemental, cet écart est où le risque se cache : vous passez l'audit et restez exposé. Tenez délibérément deux livres. Gardez l'évaluation formelle pour l'éligibilité, et gardez un tableau de bord interne brut que personne n'est récompensé de gonfler. Nommez un propriétaire pour chacun, et traitez toute distance entre eux comme un signal à enquêter, pas à masquer. Apportez les incidents récents, les quasi-accidents, et la décomposition post-évaluation à la réunion comme preuve de quel livre dit la vérité.

2. **Pour chaque domaine, adoptons-nous un modèle établi et fondé sur des preuves ou inventons-nous notre propre tableau de bord, et est-ce le bon appel ?** Les modèles établis (DORA pour la livraison, SAMM ou BSIMM pour la sécurité, TMMi pour le test) portent la recherche et la comparabilité externe qu'une grille maison ne peut égaler. Une échelle interne légère à quatre niveaux est plus rapide et plus actionnable, et c'est souvent le meilleur choix pour le pilotage interne. Le piège est d'inventer un cadre sur mesure lourd qui a tout le cérémonial d'un modèle formel et aucune de la base de preuves. Décidez par domaine : réservez les modèles formels évalués là où un contrat les exige, utilisez les modèles fondés sur des preuves là où ils existent et s'ajustent, et gardez une échelle simple par capacité pour tout le reste. Apportez la liste des domaines, marquez quel modèle chacun utilise aujourd'hui, et challengez chaque tableau de bord inventé.

3. **Qui mène nos évaluations, comment attraperions-nous une notation généreuse, et à quelle fréquence réévaluons-nous ?** Une évaluation qui se note elle-même se flatte elle-même, et la maturité dérive à mesure que les gens, systèmes, et menaces changent, donc une évaluation vieille de deux ans est souvent de la fiction. Faites tourner les évaluateurs ou faites venir une vérification externe de bon sens, et traitez un auto-score suspicieusement élevé comme une odeur à traquer, pas une victoire à célébrer. Fixez une cadence de réévaluation liée à la vitesse à laquelle chaque domaine change : la sécurité plus souvent que, disons, la documentation. Rassemblez des preuves et impliquez les gens qui font le travail plutôt que de collecter des opinions de gestionnaires. Si votre réponse est qu'une équipe se note une fois par an sans contre-vérification, vous mesurez le confort, pas la capacité.

4. **Quel niveau de maturité cible chaque capacité a-t-elle réellement besoin, et où pousser plus haut n'achèterait-il que du poids de processus ?** Plus haut n'est pas gratuit : chaque niveau supplémentaire coûte de l'effort et ajoute habituellement du cérémonial, donc un but généralisé de niveau 5 partout draine un budget d'amélioration fini dans de la bureaucratie que certains domaines ne rembourseront jamais. Pour une grande organisation, la bonne cible varie par capacité, parce qu'une zone à faible risque assise au niveau 2 peut être parfaitement sûre tandis qu'une zone critique pour la sécurité ou la conformité au même niveau est une urgence. Apportez une notation de risque par capacité, une estimation honnête de ce que l'échelon suivant coûte en effort et processus, et tout plancher d'audit ou contractuel, puisque de nombreux audits exigent au moins un niveau 3 défini. Dans les contextes d'entreprise et gouvernementaux, certaines capacités régulées ont véritablement besoin des échelons supérieurs tandis que la plupart sont bien servies au niveau 3, donc décidez les cibles délibérément, capacité par capacité, et arrêtez de grimper une fois que le retour ajusté au risque s'arrête.

5. **La dernière fois que nous avons élevé un niveau de maturité, le résultat qu'il était censé protéger s'est-il réellement amélioré, ou seul le score a-t-il bougé ?** Un niveau qui grimpe tandis que les incidents, le délai de livraison, ou les taux de défaut restent plats est la loi de Goodhart en action : une fois que le chiffre devient la cible, il cesse de mesurer la capacité. Pour une grande équipe, cela passe facilement inaperçu, parce qu'une évaluation réussie se sent comme du progrès même quand la production raconte une histoire différente. Liez le niveau de chaque capacité à une vraie métrique de résultat avant d'investir, puis apportez la preuve avant-après à la discussion : incidents par trimestre, taux d'échec de changement, temps de récupération, quoi que la capacité existe pour améliorer. Dans les portefeuilles d'entreprise et gouvernementaux où un niveau évalué conditionne l'éligibilité, l'écart est dangereux, parce que le niveau peut monter sur des preuves assemblées tandis que la pratique sous-jacente se décompose silencieusement, et la première preuve de cela est une brèche, une panne, ou un audit échoué.

6. **Communiquons-nous une note de maturité vedette unique ou une image par capacité, et les niveaux sont-ils jamais liés à la récompense, au classement, ou au statut d'équipe ?** Un seul chiffre global est facile à présenter à la direction et cache exactement l'inégalité qui compte, parce qu'une forte livraison peut masquer une capacité de sécurité de niveau 1 ; une carte thermique par capacité est plus de travail mais montre où la faible maturité rencontre le risque élevé. La question plus difficile est comment les scores sont utilisés, parce qu'au moment où un niveau est lié à la récompense ou au classement d'une équipe, le rapport honnête meurt et l'effort s'écoule vers l'apparence de maturité plutôt que la substance. Apportez la carte thermique, et un compte-rendu franc de chaque endroit où un niveau alimente actuellement une revue de performance, une décision de budget, ou un tableau de bord de fournisseur. Pour les entreprises et fournisseurs gouvernementaux, où les niveaux évalués peuvent conditionner le revenu et l'éligibilité, soyez explicite sur quelles notes portent des conséquences et lesquelles existent seulement pour piloter, parce qu'une image de maturité que les gens sont récompensés de gonfler cesse de décrire la réalité.

## Regard sectoriel

**Jeune pousse.** Un modèle formel évalué lourd est une surcharge que vous ne pouvez pas vous permettre sur une courte marge de manœuvre. Menez une auto-évaluation d'une heure sur une échelle simple à travers une poignée de capacités, corrigez seulement l'écart de maturité le plus bas qui bloque quelque chose de concret (disons, le questionnaire de sécurité de votre premier client d'entreprise), et laissez le reste tranquille. L'évaluation devrait coûter un après-midi, pas un consultant, et sa sortie est une action suivante unique plutôt qu'un score élevé uniforme dont vous n'avez ni besoin ni les moyens.

**Petite entreprise.** Sans évaluateur dédié et avec un budget serré, empruntez un modèle public léger plutôt que de commander un cadre sur mesure : une courte liste de contrôle de livraison ou de sécurité que vous pouvez vous auto-noter. Traitez-le comme une conversation annuelle sur où un point faible vous coûterait un client, pas un programme permanent. Gardez-le bon marché et brut, parce qu'un score flatteur que vous avez payé un fournisseur pour produire vaut moins qu'un franc que vous avez fait vous-même en un après-midi.

**Grande entreprise.** La valeur est un tableau de bord par capacité partagé appliqué de façon cohérente à travers de nombreuses équipes, pour que les écarts deviennent comparables et que le budget d'amélioration s'écoule là où la faible maturité rencontre le risque élevé. Gardez-vous fermement contre le théâtre de maturité une fois que les niveaux alimentent le budget ou le statut : faites tourner ou vérifiez extérieurement les évaluateurs, et gérez les résultats comme une carte thermique qui dirige l'investissement de chemin pavé (chapitre 4.2) plutôt qu'un tableau de classement qui classe les équipes et tue le rapport honnête.

**Gouvernement.** Un niveau de maturité est souvent une porte littérale ici : CMMC pour le travail de défense, une évaluation CMMI comme qualification de fournisseur. Atteignez le niveau requis avec une vraie capacité, et gardez une auto-évaluation interne franche séparée de l'évaluation formelle pour que le plancher d'audit ne devienne jamais silencieusement le plafond. Documentez les preuves de façon transparente pour les évaluateurs, et traitez toute distance entre le niveau certifié et la vraie pratique comme un risque responsable à fermer, pas de la paperasse à classer.

## Exemples

**Jeune pousse.** Une jeune pousse SaaS de dix personnes mène une auto-évaluation d'une heure contre une échelle simple à quatre niveaux couvrant la livraison, le test, la sécurité, et l'astreinte. Elle trouve la livraison et le test au niveau 3 mais la sécurité coincée au niveau 1, ce qui compte parce qu'elle est sur le point de signer son premier client d'entreprise avec un questionnaire de sécurité. Donc les fondateurs passent le mois suivant à élever seulement la sécurité à un niveau 2 défendable et laissent le reste tranquille, plutôt que de poursuivre un score élevé uniforme dont ils n'ont ni besoin ni les moyens encore.

**Grande entreprise.** Une entreprise de services financiers évalue ses 40 équipes avec un tableau de bord par capacité léger (livraison, test, sécurité, observabilité, astreinte). La carte thermique révèle que la maturité de sécurité retarde le plus là où l'exposition réglementaire est la plus élevée, donc l'équipe de plateforme finance d'abord l'outillage de sécurité de chemin pavé (chapitre 4.2) pour ces équipes. Parce que l'évaluation est utilisée pour prioriser l'investissement plutôt que classer les équipes, les gestionnaires rapportent honnêtement. La réévaluation un an plus tard montre un vrai mouvement, et, crucialement, moins d'incidents de sécurité, pas seulement des scores plus élevés.

**Gouvernement.** Un sous-traitant de défense doit atteindre un niveau CMMC requis pour soumissionner sur le travail, et un intégrateur système détient une évaluation CMMI comme qualification de contrat. Ici, le niveau de maturité est une porte littérale vers le revenu. La version bien exécutée traite le niveau requis comme un plancher pour une vraie capacité et garde une auto-évaluation interne franche séparée de l'évaluation formelle. La version mal exécutée assemble des preuves pour l'évaluation et laisse la vraie pratique se décomposer le lendemain, passant l'audit tout en restant exposée.

## Argumentaire économique : motivations, retour sur investissement et coût total de possession

Le retour sur l'évaluation de maturité vient de **l'investissement dirigé**. Les budgets d'amélioration sont finis. Dépensés aveuglément, ils financent ce qui est le plus bruyant. Une évaluation de maturité vous montre où la capacité est la plus faible contre le risque, pour que la même dépense achète plus de réduction de risque et plus d'amélioration de résultat. L'évaluation elle-même est bon marché, seulement des jours de revue structurée et fondée sur des preuves, contre le coût de programmes d'amélioration mal alloués ou, pire, un écart de capacité non détecté qui fait surface comme une brèche, une panne, ou un audit échoué.

Sur le **coût total de possession**, la discipline est peu coûteuse quand vous la gardez légère et coûteuse quand elle durcit en bureaucratie d'évaluation. Le coût caché dominant est le *théâtre de maturité* : l'effort dépensé à produire l'apparence de maturité ne retourne rien et peut masquer un vrai risque, ce qui est un ROI négatif. Pour faire valoir le dossier auprès de la direction, présentez la maturité comme une lentille de risque et d'investissement, une carte thermique qui transforme « tout améliorer » en « améliorer ces trois choses d'abord », et budgétez explicitement contre la tentation de poursuivre des niveaux pour eux-mêmes. Là où un niveau est contractuellement requis (CMMC, CMMI), le ROI est direct : c'est le prix de l'éligibilité, et le but est de le respecter avec une vraie capacité plutôt qu'un prétexte coûteux.

## Anti-patterns et pièges

- **Le niveau comme but :** poursuivre un chiffre au lieu de la capacité qu'il est censé représenter.
- **Le théâtre de maturité :** assembler des preuves pour une évaluation tandis que la vraie pratique se décompose.
- **Une note globale unique :** un seul score de maturité qui cache une inégalité dangereuse.
- **Plus-haut-est-toujours-meilleur :** pousser chaque capacité au niveau 5 indépendamment du risque ou du coût.
- **Évaluer une fois, jamais plus :** une évaluation ponctuelle traitée comme une vérité permanente.
- **Classer les équipes pour blâmer :** utiliser la maturité pour la punition, ce qui tue le rapport honnête.
- **Le culte du modèle :** suivre le cérémonial d'un cadre lourd au-delà du point d'utilité.
- **Ignorer les résultats :** grimper l'échelle tandis que la livraison, fiabilité, ou sécurité ne s'améliorent pas.

## Modèle de maturité

- **Niveau 1, Initier.** Aucune notion partagée de maturité ; la capacité est supposée, inégale, et non mesurée ; toute évaluation est réactive, déclenchée par un incident ou une demande d'audit plutôt que planifiée.
- **Niveau 2, Développer.** Quelques équipes mènent des évaluations ad hoc contre une certaine échelle, mais le modèle, la cadence, et la rigueur varient équipe par équipe ; les résultats sont utilisés de façon incohérente et les preuves sont minces, donc noter pour l'apparence est un risque toujours présent.
- **Niveau 3, Standardiser.** Un modèle unique par capacité et une cadence d'évaluation sont documentés et appliqués à l'échelle de l'organisation ; les évaluations sont fondées sur des preuves, impliquent les gens qui font le travail, et alimentent un carnet d'amélioration priorisé plutôt qu'un bulletin.
- **Niveau 4, Gérer.** La maturité est mesurée et contrôlée avec des données : le niveau de chaque capacité est suivi contre un référentiel, lié à une métrique de résultat (incidents, délai de livraison, taux d'échec de changement), et réévalué selon une cadence fixée, pour que la dérive et la notation généreuse apparaissent comme des chiffres plutôt que des opinions, et les cibles sont fixées délibérément par domaine contre le risque et le coût.
- **Niveau 5, Orchestrer.** L'évaluation est intégrée à travers l'organisation et continuellement améliorée : la maturité, le risque, et les résultats informent l'investissement comme une image adaptative unique, les cibles sont rééquilibrées à mesure que les menaces et le contexte changent, les évaluateurs sont tournés ou vérifiés extérieurement comme une question de routine, et la pratique retire activement le cérémonial qui ne mérite plus son coût.

## Pistes de réflexion

1. Lesquelles de vos capacités supposez-vous matures sans preuve ?
2. Où votre maturité la plus basse coïncide-t-elle avec votre risque le plus élevé, et est-ce là que va votre budget d'amélioration ?
3. Un niveau de maturité dans votre organisation est-il jamais une cible ou une porte ? Quel comportement cela a-t-il produit ?
4. Quel est le bon niveau cible pour chaque capacité, et où grimper davantage n'ajouterait-il que de la bureaucratie ?
5. Vos équipes rapporteraient-elles leur maturité honnêtement, ou la façon dont vous utilisez les scores punit-elle la franchise ?
6. Quand vous avez « amélioré la maturité » pour la dernière fois, les résultats ont-ils réellement changé ?

## Points clés à retenir

- Un modèle de maturité évalue la capacité contre une échelle de niveaux et décrit un chemin pour améliorer : un miroir, pas un trophée.
- Choisissez des modèles établis et fondés sur des preuves par domaine (CMMI, DORA, SAMM/BSIMM, CMMC) ; une échelle légère par capacité est souvent la plus actionnable.
- **Évaluez honnêtement, par capacité**, et utilisez les résultats pour **prioriser par risque**, pas pour classer ou blâmer.
- **Plus haut n'est pas toujours meilleur :** fixez les niveaux cibles délibérément contre le risque et le coût.
- Méfiez-vous du **théâtre de maturité** et de la **loi de Goodhart** : un niveau qui devient une cible cesse de mesurer la capacité.
- Voir le chapitre 12.4 pour l'auto-évaluation de maturité consolidée de ce livre, et la propre section de maturité de chaque chapitre.

## Références et lectures complémentaires

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origines de la maturité du processus logiciel).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (pensée de capacité, pas de niveau de maturité, pour la livraison).
- OWASP, *Software Assurance Maturity Model (SAMM)* ; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defense, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore et Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, « Maturity Model » (bliki), sur leurs usages et abus.
