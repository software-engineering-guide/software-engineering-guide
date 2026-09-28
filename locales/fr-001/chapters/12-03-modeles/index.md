# 12.3 Modèles

Ces modèles sont des points de départ prêts à copier-coller. Prenez tout modèle dans votre wiki, dépôt, ou système de billetterie et remplissez les espaces réservés entre crochets. Les notes en italique et commentaires en ligne expliquent ce qui appartient à chaque section ; supprimez-les une fois la section remplie. Gardez les modèles légers : un modèle plus rapide à sauter qu'à compléter ne sera pas utilisé. Adaptez les titres et sections à votre organisation, mais préservez l'intention de chaque partie.

Quelques conventions utilisées ci-dessous :

- Le texte entre `[crochets]` est un espace réservé à remplacer.
- Le texte en _italique_ ou `<!-- commentaires -->` est une orientation à supprimer.
- Gardez le document terminé aussi court que possible tout en répondant encore à ses questions.

## Enregistrement de décision d'architecture (ADR)

```markdown
# ADR [NNNN] : [Titre court de la décision]

- Statut : [Proposé | Accepté | Déprécié | Remplacé par ADR-XXXX]
- Date : [AAAA-MM-JJ]
- Décideurs : [noms ou rôles]
- Consultés : [noms ou rôles]

## Contexte

<!-- Quel est le problème, la force, ou la contrainte pilotant cette
     décision ? Énoncez les faits et exigences neutralement. Incluez
     seulement ce qu'un futur lecteur a besoin de comprendre pour
     savoir pourquoi une décision était nécessaire. -->

## Décision

<!-- Énoncez le choix en une ou deux phrases claires : « Nous allons... » -->

## Alternatives considérées

<!-- Listez les options réalistes que vous avez pesées et pourquoi
     chacune a été ou n'a pas été choisie. Au moins deux alternatives
     devraient apparaître ici. -->

- Option A : [résumé] ; rejetée parce que [raison].
- Option B : [résumé] ; rejetée parce que [raison].
- Option choisie : [résumé] ; choisie parce que [raison].

## Conséquences

<!-- Résultats honnêtes de la décision, bons et mauvais. -->

- Positif : [bénéfices gagnés]
- Négatif : [coûts, risques, ou limitations acceptés]
- Suivi : [migrations, nouveau travail, ou décisions que cela déclenche]

## Lié

<!-- Liens vers les ADR, RFC, tickets, ou documents antérieurs auxquels
     ceci se rapporte. -->
```

## RFC / document de conception

```markdown
# RFC : [Titre]

- Auteur(s) : [noms]
- Statut : [Brouillon | En révision | Approuvé | Rejeté | Implémenté]
- Réviseurs : [noms ou rôles]
- Créé : [AAAA-MM-JJ]
- Dernière mise à jour : [AAAA-MM-JJ]
- Ticket / suivi : [lien]

## Résumé

<!-- Un paragraphe : ce que ceci propose et pourquoi cela compte. Un
     lecteur devrait saisir l'essence depuis cette section seule. -->

## Problème et motivation

<!-- Quel problème résolvons-nous ? Qui est affecté ? Que se passe-t-il
     si nous ne faisons rien ? Incluez le contexte et les contraintes
     pertinents. -->

## Objectifs et non-objectifs

- Objectifs : [à quoi le succès ressemble, mesurable là où possible]
- Non-objectifs : [explicitement hors portée, pour empêcher la dérive de portée]

## Conception proposée

<!-- Le cœur du document. Décrivez l'approche, l'architecture, le
     modèle de données, les interfaces, et les flux clés. Utilisez
     des diagrammes là où ils clarifient. Expliquez comment cela
     fonctionne, pas seulement ce que c'est. -->

## Alternatives considérées

<!-- Autres approches et pourquoi elles n'ont pas été choisies. Montre
     au lecteur que l'espace de conception a été exploré. -->

## Impact et risques

- Sécurité et vie privée : [implications et atténuations]
- Performance et échelle : [charge et comportement attendus]
- Exploitabilité : [surveillance, modes d'échec, déploiement, retour en arrière]
- Coût : [impact d'infrastructure ou de licence]
- Compatibilité ascendante : [migration et dépréciation]

## Plan de test et de déploiement

<!-- Comment le changement sera validé et publié en sécurité. -->

## Questions ouvertes

<!-- Problèmes non résolus sur lesquels vous voulez que les réviseurs se prononcent. -->
```

## Post-mortem / revue d'incident (sans blâme)

```markdown
# Post-mortem : [Titre de l'incident]

- ID d'incident : [ID]
- Date de l'incident : [AAAA-MM-JJ]
- Auteurs : [noms]
- Statut : [Brouillon | Final]
- Sévérité : [SEV1 | SEV2 | SEV3]

> Cette revue est sans blâme. Nous nous concentrons sur les systèmes et
> facteurs contributifs, pas sur les individus. Le but est d'apprendre
> et de prévenir la récurrence.

## Résumé

<!-- Deux ou trois phrases : ce qui s'est passé, l'impact, et la
     résolution, lisible par un non-expert. -->

## Impact

- Durée : [heure de début à heure de récupération, avec fuseau horaire]
- Utilisateurs affectés : [portée et nombre]
- Impact d'affaires : [revenu, SLA, réputation, ou autre]

## Chronologie

<!-- Séquence factuelle et horodatée d'événements. Incluez la détection,
     l'escalade, les actions clés, et la récupération. -->

- [HH:MM] [événement]
- [HH:MM] [événement]

## Facteurs contributifs

<!-- La chaîne de conditions qui a mené à l'incident. Préférez
     « facteurs contributifs » à une seule cause racine. -->

## Détection et réponse

- Comment a-t-il été détecté ? [alerte, rapport client, etc.]
- Qu'est-ce qui a aidé la réponse ?
- Qu'est-ce qui a ralenti la réponse ?

## Ce qui s'est bien passé

<!-- Reconnaissez les actions et garde-fous efficaces qui ont fonctionné. -->

## Actions

<!-- Spécifiques, possédées, et datées. Adressez la prévention, la
     détection, et l'atténuation. Suivez celles-ci dans le carnet normal. -->

| Action | Propriétaire | Date d'échéance | Type (prévenir/détecter/atténuer) | Ticket |
|--------|-------|----------|--------------------------------|--------|
| [action] | [nom] | [date] | [type] | [lien] |

## Leçons apprises

<!-- Ce que l'organisation plus large devrait retenir. -->
```

## Modèle de menace (basé sur STRIDE)

```markdown
# Modèle de menace : [Nom du système ou de la fonctionnalité]

- Auteur(s) : [noms]
- Date : [AAAA-MM-JJ]
- Réviseurs : [contact de sécurité, propriétaires]
- Portée : [ce qui est et n'est pas couvert]

## Vue d'ensemble du système

<!-- Brève description du système, son but, et ses utilisateurs. -->

## Actifs

<!-- Ce qui vaut la peine d'être protégé : données, identifiants,
     fonctionnalité, réputation. Notez la sensibilité de chacun. -->

## Frontières de confiance et flux de données

<!-- Décrivez ou diagrammez les composants, magasins de données,
     entités externes, et les frontières où la confiance change. -->

## Menaces (STRIDE)

<!-- Pour chaque élément, considérez les catégories STRIDE. Enregistrez
     chaque menace crédible, son risque, et l'atténuation ou le risque
     accepté. -->

| Menace | Catégorie STRIDE | Élément affecté | Risque (F/M/E) | Atténuation | Statut |
|--------|-----------------|------------------|--------------|------------|--------|
| [menace] | Usurpation | [élément] | [risque] | [contrôle] | [ouvert/atténué/accepté] |
| [menace] | Altération | [élément] | [risque] | [contrôle] | [statut] |
| [menace] | Répudiation | [élément] | [risque] | [contrôle] | [statut] |
| [menace] | Divulgation d'information | [élément] | [risque] | [contrôle] | [statut] |
| [menace] | Déni de service | [élément] | [risque] | [contrôle] | [statut] |
| [menace] | Élévation de privilège | [élément] | [risque] | [contrôle] | [statut] |

## Hypothèses et dépendances

<!-- Hypothèses de sécurité sur lesquelles on s'appuie et contrôles
     externes de confiance. -->

## Problèmes ouverts et suivi

<!-- Menaces nécessitant plus de travail, suivies comme tickets. -->
```

## Livre d'exécution

```markdown
# Livre d'exécution : [Nom de tâche ou de scénario]

- Service : [nom de service]
- Propriétaire : [équipe]
- Dernière révision : [AAAA-MM-JJ]
- Alertes liées : [noms d'alerte]

## But

<!-- Quand utiliser ce livre d'exécution et ce qu'il accomplit. -->

## Prérequis

<!-- Accès, outils, et permissions nécessaires avant de commencer. -->

## Détection / symptômes

<!-- Ce que l'opérateur observe : alertes, signatures d'erreur, tableaux de bord. -->

## Diagnostic

<!-- Vérifications étape par étape pour confirmer le problème et
     restreindre la cause. Incluez les commandes, requêtes, ou liens
     de tableau de bord exacts. -->

1. [étape et résultat attendu]
2. [étape et résultat attendu]

## Résolution

<!-- Étapes concrètes et ordonnées pour corriger ou atténuer. Notez
     toute étape risquée ou irréversible, et comment vérifier le succès. -->

1. [étape]
2. [vérifier la récupération]

## Retour en arrière

<!-- Comment défaire les actions si la résolution empire les choses. -->

## Escalade

<!-- Qui contacter et quand escalader. Astreinte secondaire, équipe
     propriétaire, et contacts fournisseur. -->

## Références

<!-- Tableaux de bord, livres d'exécution liés, documents d'architecture. -->
```

## README de service / entrée de catalogue de service

```markdown
# [Nom du service]

- Équipe propriétaire : [équipe]
- Astreinte : [lien de rotation]
- Niveau / criticité : [Niveau 1 | 2 | 3]
- Dépôt : [lien]
- Statut : [Actif | Déprécié]

## Ce qu'il fait

<!-- Un paragraphe sur la responsabilité du service et ses consommateurs. -->

## Architecture

<!-- Composants clés, dépendances (amont et aval), et un lien vers le
     document ou diagramme de conception. -->

## Interfaces

- API / points de terminaison : [lien vers la spécification]
- Événements publiés / consommés : [sujets]
- Magasins de données : [bases de données, caches, buckets]

## Exécution et déploiement

- Environnements : [dev, préproduction, prod]
- Comment déployer : [lien de pipeline et processus]
- Configuration et drapeaux de fonctionnalité : [où et comment]

## Observabilité

- Tableaux de bord : [liens]
- Alertes : [liens]
- Journaux : [où les trouver]
- SLO : [lien]

## Opérations

- Livres d'exécution : [liens]
- Tâches communes : [mise à l'échelle, redémarrage, remplissage]
- Problèmes et limitations connus : [notes]

## Démarrage (pour les nouveaux contributeurs)

<!-- Comment construire, tester, et exécuter localement. -->

## Contacts

- Canal Slack / discussion : [lien]
- Escalade : [chemin]
```

## Politique de SLO / budget d'erreur

```markdown
# Politique de SLO et budget d'erreur : [Nom du service ou parcours]

- Propriétaire : [équipe]
- Date d'effet : [AAAA-MM-JJ]
- Cadence de révision : [par exemple trimestrielle]

## Indicateurs de niveau de service (SLI)

<!-- Définissez chaque SLI précisément : la quantité mesurée, comment
     elle est mesurée, et depuis où (idéalement la perspective de
     l'utilisateur). -->

| SLI | Définition | Source de données |
|-----|-----------|-------------|
| Disponibilité | [par exemple requêtes réussies / requêtes totales] | [source] |
| Latence | [par exemple proportion de requêtes sous Xms] | [source] |

## Objectifs (SLO)

| SLI | Cible | Fenêtre de mesure |
|-----|--------|--------------------|
| Disponibilité | [par exemple 99,9 %] | [par exemple 28 jours glissants] |
| Latence | [par exemple 95 % sous 300ms] | [28 jours glissants] |

## Budget d'erreur

<!-- L'indisponibilité permise : 100 % moins la cible, sur la fenêtre.
     Énoncez le budget en termes concrets (par exemple minutes/mois). -->

- Budget : [allocation dérivée]

## Politique quand le budget est épuisé

<!-- Les conséquences convenues. Rendez-les concrètes et applicables. -->

- [par exemple Geler les publications de fonctionnalités non critiques jusqu'à ce que le budget récupère.]
- [par exemple Prioriser le travail de fiabilité dans le prochain cycle de planification.]
- [par exemple Escalader vers la direction d'ingénierie si violé deux fenêtres de suite.]

## Politique quand le budget est sain

<!-- Quel risque supplémentaire l'équipe peut prendre, par exemple des déploiements plus rapides. -->

## Alerte

<!-- Alertes de taux de combustion et seuils liés à ce SLO. -->
```

## Entrée de registre de risque

```markdown
## Risque : [Titre court du risque]

- ID de risque : [ID]
- Date soulevée : [AAAA-MM-JJ]
- Propriétaire : [nom ou rôle responsable de gérer ce risque]
- Catégorie : [sécurité | opérationnel | conformité | financier | livraison | fournisseur]
- Statut : [Ouvert | En atténuation | Accepté | Fermé]

### Description

<!-- Énoncez le risque comme : cause -> événement -> conséquence. Ce
     qui pourrait arriver, et pourquoi cela compte. -->

### Évaluation

- Probabilité : [Faible | Moyenne | Élevée]
- Impact : [Faible | Moyen | Élevé]
- Note globale : [dérivée de probabilité x impact]

### Contrôles actuels

<!-- Ce qui réduit déjà ce risque aujourd'hui. -->

### Plan d'atténuation

<!-- Actions planifiées pour réduire la probabilité ou l'impact, avec
     propriétaires et dates. Si vous acceptez le risque, enregistrez
     qui l'a accepté et pourquoi. -->

| Action | Propriétaire | Date d'échéance | Statut |
|--------|-------|----------|--------|
| [action] | [nom] | [date] | [statut] |

### Révision

- Prochaine date de révision : [AAAA-MM-JJ]
- Décision / notes : [toute approbation d'acceptation ou changement]
```

## Fiche d'une page de projet / dossier de produit

```markdown
# [Nom du projet ou produit] : fiche d'une page

- Commanditaire : [nom]
- Responsable : [nom]
- Date : [AAAA-MM-JJ]
- Statut : [Idée | Approuvé | En cours | Livré]

## Problème

<!-- Un paragraphe : le problème client ou d'affaires, et la preuve
     qu'il est réel et vaut la peine d'être résolu. -->

## Audience

<!-- Qui a ce problème et qui bénéficie de le résoudre. -->

## Solution proposée

<!-- Une brève description de ce que nous allons construire ou changer.
     Gardez-la au niveau de l'intention, pas du détail d'implémentation. -->

## Pourquoi maintenant

<!-- La raison de faire cela maintenant plutôt que plus tard. -->

## Métriques de succès

<!-- Comment nous saurons que cela a fonctionné. Préférez les résultats mesurables. -->

- [métrique et cible]

## Portée

- Dans la portée : [ce que nous ferons]
- Hors portée : [ce que nous ne ferons pas]

## Risques et questions ouvertes

<!-- Principales incertitudes et dépendances. -->

## Plan approximatif et jalons

<!-- Phases de haut niveau et calendrier approximatif. -->

## Coût et ressources

<!-- Gens, temps, et budget requis. -->
```

## Notes de transfert d'astreinte

```markdown
# Transfert d'astreinte : [AAAA-MM-JJ]

- Sortant : [nom]
- Entrant : [nom]
- Service(s) : [noms]

## Statut global

<!-- Une ligne : calme, bruyant, ou problème en cours. -->

## Incidents ouverts

<!-- Tout incident actif ou récemment résolu que le prochain répondant
     doit connaître, avec des liens. -->

- [incident, statut, et ce qui reste]

## Changements en cours ou planifiés

<!-- Déploiements, migrations, fenêtres de maintenance, ou expériences
     en vol qui pourraient causer des alertes. -->

## Alertes bruyantes ou instables

<!-- Alertes qui se sont déclenchées et leur vraie signification, pour
     que la prochaine personne ne soit pas induite en erreur. Notez tout
     silence temporaire et son expiration. -->

## Éléments à surveiller

<!-- Métriques ou systèmes tendant dans une direction préoccupante. -->

## Suivis en attente

<!-- Tâches remises au prochain quart, avec des liens vers les tickets. -->

## Notes

<!-- Toute autre chose utile : bizarreries d'accès, problèmes de fournisseur, contexte. -->
```

## Demande de changement (pour le contrôle de changement régulé)

```markdown
# Demande de changement : [Titre du changement]

- ID de changement : [ID]
- Demandeur : [nom]
- Date de soumission : [AAAA-MM-JJ]
- Type : [Standard | Normal | Urgence]
- Priorité : [Faible | Moyenne | Élevée]
- Statut : [Soumis | Approuvé | Rejeté | Implémenté | Fermé]

## Description du changement

<!-- Ce qui change et pourquoi. Référencez le ticket ou l'exigence. -->

## Systèmes et composants affectés

<!-- Services, données, environnements, et utilisateurs impactés. -->

## Justification et impact d'affaires

<!-- La raison du changement et l'impact de ne pas le faire. -->

## Évaluation de risque

- Niveau de risque : [Faible | Moyen | Élevé]
- Impact potentiel si le changement échoue : [description]
- Impact sur la sécurité, la vie privée, ou la conformité : [description]

## Plan d'implémentation

<!-- Étapes ordonnées, parties responsables, et calendrier. -->

## Plan de test et de validation

<!-- Comment le succès sera vérifié avant et après le changement. -->

## Plan de retrait / retour en arrière

<!-- Comment inverser le changement s'il échoue, et le temps de récupération. -->

## Calendrier

- Fenêtre proposée : [début et fin, avec fuseau horaire]
- Indisponibilité attendue : [durée ou aucune]

## Approbations

| Rôle | Nom | Décision | Date |
|------|------|----------|------|
| Propriétaire du changement | [nom] | [approuver/rejeter] | [date] |
| Réviseur technique | [nom] | [approuver/rejeter] | [date] |
| Comité consultatif de changement | [nom] | [approuver/rejeter] | [date] |

## Revue post-implémentation

<!-- Résultat, problèmes rencontrés, et si le retrait a été nécessaire. -->
```

## Plan d'analyse d'impact relative à la protection des données (AIPD)

```markdown
# Analyse d'impact relative à la protection des données : [Nom de l'activité de traitement]

- Évaluateur : [nom]
- Date : [AAAA-MM-JJ]
- Réviseurs : [DPO / contact de vie privée]
- Statut : [Brouillon | Révisé | Approuvé]

## 1. Description du traitement

<!-- Quelles données personnelles sont traitées, comment, par qui, et
     dans quel but. Incluez les flux de données depuis la collecte
     jusqu'à la suppression. -->

- Personnes concernées : [de qui les données parlent]
- Catégories de données : [types de données personnelles, notez toute catégorie spéciale]
- Buts : [pourquoi les données sont traitées]
- Destinataires et sous-traitants : [qui reçoit ou gère les données]
- Période de rétention : [combien de temps les données sont gardées et méthode de suppression]
- Transferts internationaux : [destinations et mécanisme de transfert]

## 2. Nécessité et proportionnalité

<!-- Le traitement est-il nécessaire pour le but ? Est-ce l'option la
     moins intrusive ? Quelle est la base légale ou l'autorité ? -->

- Base légale / autorité : [base pour chaque but]
- Minimisation de données : [pourquoi chaque champ est nécessaire]
- Justification d'exactitude et de rétention : [notes]
- Comment les droits des personnes concernées sont soutenus : [accès, suppression, etc.]

## 3. Consultation

<!-- Parties prenantes, et là où pertinent les personnes concernées, consultées. -->

## 4. Risques pour les individus

<!-- Identifiez les risques de vie privée et notez chacun. -->

| Risque pour les individus | Probabilité | Sévérité | Global |
|---------------------|-----------|----------|---------|
| [par exemple accès non autorisé à des données sensibles] | [F/M/E] | [F/M/E] | [note] |

## 5. Mesures pour réduire le risque

<!-- Pour chaque risque, l'atténuation et le risque résiduel après. -->

| Risque | Mesure | Risque résiduel | Accepté par |
|------|---------|---------------|-------------|
| [risque] | [contrôle] | [F/M/E] | [nom] |

## 6. Résultat et approbation

- Risque résiduel acceptable : [Oui | Non]
- Mesures approuvées par : [nom, rôle]
- Consultation de l'autorité de surveillance requise : [Oui | Non]
- Date de révision : [AAAA-MM-JJ]
```
