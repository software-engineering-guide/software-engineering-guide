# 12.3 Vorlagen

Diese Vorlagen sind kopier-und-einfüge-fertige Ausgangspunkte. Heben Sie jede Vorlage in Ihr Wiki, Repository, oder Ticketing-System, und füllen Sie die eingeklammerten Platzhalter aus. Kursivierte Hinweise und Inline-Kommentare erklären, was in jeden Abschnitt gehört; löschen Sie sie, sobald der Abschnitt gefüllt ist. Halten Sie Vorlagen leichtgewichtig: eine Vorlage, die schneller zu überspringen als auszufüllen ist, wird nicht genutzt. Passen Sie Überschriften und Abschnitte an Ihre Organisation an, aber bewahren Sie die Absicht jedes Teils.

Ein paar unten genutzte Konventionen:

- Text in `[eckigen Klammern]` ist ein zu ersetzender Platzhalter.
- Text in _Kursivschrift_ oder `<!-- Kommentaren -->` ist zu löschende Anleitung.
- Halten Sie das fertige Dokument so kurz wie möglich, während es seine Fragen noch beantwortet.

## Architekturentscheidungsaufzeichnung (ADR)

```markdown
# ADR [NNNN]: [Kurztitel der Entscheidung]

- Status: [Vorgeschlagen | Akzeptiert | Veraltet | Ersetzt durch ADR-XXXX]
- Datum: [JJJJ-MM-TT]
- Entscheiderinnen: [Namen oder Rollen]
- Konsultiert: [Namen oder Rollen]

## Kontext

<!-- Was ist das Problem, die Kraft, oder die Einschränkung, die diese
     Entscheidung antreibt? Erklären Sie die Fakten und Anforderungen
     neutral. Schließen Sie nur ein, was eine zukünftige Leserin
     braucht, um zu verstehen, warum eine Entscheidung nötig war. -->

## Entscheidung

<!-- Erklären Sie die Wahl in ein oder zwei klaren Sätzen: "Wir werden ..." -->

## Betrachtete Alternativen

<!-- Listen Sie die realistischen Optionen auf, die Sie abwogen, und
     warum jede gewählt oder nicht gewählt wurde. Mindestens zwei
     Alternativen sollten hier erscheinen. -->

- Option A: [Zusammenfassung]; abgelehnt, weil [Grund].
- Option B: [Zusammenfassung]; abgelehnt, weil [Grund].
- Gewählte Option: [Zusammenfassung]; gewählt, weil [Grund].

## Konsequenzen

<!-- Ehrliche Ergebnisse der Entscheidung, sowohl gute als auch schlechte. -->

- Positiv: [gewonnene Vorteile]
- Negativ: [akzeptierte Kosten, Risiken, oder Einschränkungen]
- Folgeschritte: [Migrationen, neue Arbeit, oder Entscheidungen, die dies auslöst]

## Verwandt

<!-- Links zu vorherigen ADRs, RFCs, Tickets, oder Dokumenten, auf die sich dies bezieht. -->
```

## RFC / Designdokument

```markdown
# RFC: [Titel]

- Autorin(nen): [Namen]
- Status: [Entwurf | In Überprüfung | Genehmigt | Abgelehnt | Implementiert]
- Überprüferinnen: [Namen oder Rollen]
- Erstellt: [JJJJ-MM-TT]
- Zuletzt aktualisiert: [JJJJ-MM-TT]
- Ticket / Verfolgung: [Link]

## Zusammenfassung

<!-- Ein Absatz: was dies vorschlägt und warum es wichtig ist. Eine
     Leserin sollte das Wesentliche allein aus diesem Abschnitt erfassen. -->

## Problem und Motivation

<!-- Welches Problem lösen wir? Wer ist betroffen? Was passiert, falls
     wir nichts tun? Schließen Sie relevanten Hintergrund und
     Einschränkungen ein. -->

## Ziele und Nicht-Ziele

- Ziele: [wie Erfolg aussieht, wo möglich messbar]
- Nicht-Ziele: [explizit außerhalb des Umfangs, um Scope Creep zu verhindern]

## Vorgeschlagenes Design

<!-- Der Kern des Dokuments. Beschreiben Sie den Ansatz, die
     Architektur, das Datenmodell, Schnittstellen, und Schlüsselflüsse.
     Nutzen Sie Diagramme, wo sie klären. Erklären Sie, wie es
     funktioniert, nicht nur was es ist. -->

## Betrachtete Alternativen

<!-- Andere Ansätze und warum sie nicht gewählt wurden. Zeigt der
     Leserin, dass der Designraum erkundet wurde. -->

## Auswirkung und Risiken

- Sicherheit und Datenschutz: [Implikationen und Minderungen]
- Leistung und Skalierung: [erwartete Last und Verhalten]
- Betreibbarkeit: [Überwachung, Fehlschlagsmodi, Rollout, Rollback]
- Kosten: [Infrastruktur- oder Lizenzierungsauswirkung]
- Rückwärtskompatibilität: [Migration und Deprecation]

## Test- und Rollout-Plan

<!-- Wie die Änderung sicher validiert und veröffentlicht wird. -->

## Offene Fragen

<!-- Ungelöste Probleme, zu denen Sie Überprüferinnen-Rückmeldung wollen. -->
```

## Postmortem / Vorfallüberprüfung (schuldfrei)

```markdown
# Postmortem: [Vorfalltitel]

- Vorfall-ID: [ID]
- Datum des Vorfalls: [JJJJ-MM-TT]
- Autorinnen: [Namen]
- Status: [Entwurf | Final]
- Schweregrad: [SEV1 | SEV2 | SEV3]

> Diese Überprüfung ist schuldfrei. Wir fokussieren auf Systeme und
> beitragende Faktoren, nicht auf Individuen. Das Ziel ist zu lernen
> und Wiederholung zu verhindern.

## Zusammenfassung

<!-- Zwei oder drei Sätze: was passierte, die Auswirkung, und die
     Lösung, für eine Nicht-Expertin lesbar. -->

## Auswirkung

- Dauer: [Startzeit bis Erholungszeit, mit Zeitzone]
- Betroffene Nutzerinnen: [Umfang und Anzahl]
- Geschäftsauswirkung: [Umsatz, SLA, Reputation, oder anderes]

## Zeitleiste

<!-- Zeitgestempelte, faktische Sequenz von Ereignissen. Schließen Sie
     Erkennung, Eskalation, Schlüsselaktionen, und Erholung ein. -->

- [HH:MM] [Ereignis]
- [HH:MM] [Ereignis]

## Beitragende Faktoren

<!-- Die Kette von Bedingungen, die zum Vorfall führte. Bevorzugen Sie
     "beitragende Faktoren" über eine einzelne Grundursache. -->

## Erkennung und Reaktion

- Wie wurde es erkannt? [Alarm, Kundinnenbericht, usw.]
- Was half der Reaktion?
- Was verlangsamte die Reaktion?

## Was gut lief

<!-- Erkennen Sie effektive Aktionen und Sicherungen an, die funktionierten. -->

## Aktionspunkte

<!-- Spezifisch, mit Besitzerin, und datiert. Adressieren Sie
     Prävention, Erkennung, und Minderung. Verfolgen Sie diese im
     normalen Backlog. -->

| Aktion | Besitzerin | Fälligkeitsdatum | Typ (verhindern/erkennen/mindern) | Ticket |
|--------|-----------|-------------------|-------------------------------------|--------|
| [Aktion] | [Name] | [Datum] | [Typ] | [Link] |

## Gelernte Lektionen

<!-- Was die weitere Organisation mitnehmen sollte. -->
```

## Bedrohungsmodell (STRIDE-basiert)

```markdown
# Bedrohungsmodell: [System- oder Feature-Name]

- Autorin(nen): [Namen]
- Datum: [JJJJ-MM-TT]
- Überprüferinnen: [Sicherheitskontakt, Besitzerinnen]
- Umfang: [was abgedeckt ist und was nicht]

## Systemüberblick

<!-- Kurze Beschreibung des Systems, seines Zwecks, und seiner Nutzerinnen. -->

## Vermögenswerte

<!-- Was schützenswert ist: Daten, Anmeldedaten, Funktionalität,
     Reputation. Notieren Sie die Sensibilität jedes einzelnen. -->

## Vertrauensgrenzen und Datenfluss

<!-- Beschreiben oder diagrammieren Sie Komponenten, Datenspeicher,
     externe Entitäten, und die Grenzen, wo sich Vertrauen ändert. -->

## Bedrohungen (STRIDE)

<!-- Betrachten Sie für jedes Element die STRIDE-Kategorien. Erfassen
     Sie jede glaubwürdige Bedrohung, ihr Risiko, und die Minderung
     oder das akzeptierte Risiko. -->

| Bedrohung | STRIDE-Kategorie | Betroffenes Element | Risiko (N/M/H) | Minderung | Status |
|-----------|-------------------|----------------------|-------------------|-----------|--------|
| [Bedrohung] | Spoofing | [Element] | [Risiko] | [Kontrolle] | [offen/gemindert/akzeptiert] |
| [Bedrohung] | Tampering | [Element] | [Risiko] | [Kontrolle] | [Status] |
| [Bedrohung] | Repudiation | [Element] | [Risiko] | [Kontrolle] | [Status] |
| [Bedrohung] | Information Disclosure | [Element] | [Risiko] | [Kontrolle] | [Status] |
| [Bedrohung] | Denial of Service | [Element] | [Risiko] | [Kontrolle] | [Status] |
| [Bedrohung] | Elevation of Privilege | [Element] | [Risiko] | [Kontrolle] | [Status] |

## Annahmen und Abhängigkeiten

<!-- Verlassene Sicherheitsannahmen und vertraute externe Kontrollen. -->

## Offene Punkte und Folgeschritte

<!-- Bedrohungen, die weitere Arbeit brauchen, als Tickets verfolgt. -->
```

## Runbook

```markdown
# Runbook: [Aufgaben- oder Szenarioname]

- Dienst: [Dienstname]
- Besitzerin: [Team]
- Zuletzt überprüft: [JJJJ-MM-TT]
- Verwandte Alarme: [Alarmnamen]

## Zweck

<!-- Wann dieses Runbook zu nutzen ist und was es erreicht. -->

## Voraussetzungen

<!-- Zugriff, Werkzeuge, und Berechtigungen, die vor dem Beginnen nötig sind. -->

## Erkennung / Symptome

<!-- Was die Operatorin beobachtet: Alarme, Fehlersignaturen, Dashboards. -->

## Diagnose

<!-- Schrittweise Prüfungen, das Problem zu bestätigen und die Ursache
     einzugrenzen. Schließen Sie die exakten Befehle, Abfragen, oder
     Dashboard-Links ein. -->

1. [Schritt und erwartetes Ergebnis]
2. [Schritt und erwartetes Ergebnis]

## Lösung

<!-- Konkrete, geordnete Schritte zum Beheben oder Mindern. Notieren
     Sie jeden Schritt, der riskant oder irreversibel ist, und wie
     Erfolg zu verifizieren ist. -->

1. [Schritt]
2. [Erholung verifizieren]

## Rollback

<!-- Wie die Aktionen rückgängig zu machen sind, falls die Lösung
     Dinge verschlimmert. -->

## Eskalation

<!-- Wen zu kontaktieren und wann zu eskalieren ist. Sekundärer
     Bereitschaftsdienst, besitzendes Team, und Anbieterinnenkontakte. -->

## Referenzen

<!-- Dashboards, verwandte Runbooks, Architekturdokumente. -->
```

## Dienst-README / Dienstkatalogeintrag

```markdown
# [Dienstname]

- Besitzendes Team: [Team]
- Bereitschaftsdienst: [Rotationslink]
- Stufe / Kritikalität: [Stufe 1 | 2 | 3]
- Repository: [Link]
- Status: [Aktiv | Veraltet]

## Was er tut

<!-- Ein Absatz zur Verantwortlichkeit des Dienstes und seinen Konsumentinnen. -->

## Architektur

<!-- Schlüsselkomponenten, Abhängigkeiten (vor- und nachgelagert), und
     ein Link zum Designdokument oder Diagramm. -->

## Schnittstellen

- APIs / Endpunkte: [Link zur Spezifikation]
- Veröffentlichte / konsumierte Ereignisse: [Topics]
- Datenspeicher: [Datenbanken, Caches, Buckets]

## Laufzeit und Bereitstellung

- Umgebungen: [Dev, Staging, Prod]
- Wie bereitgestellt wird: [Pipeline-Link und Prozess]
- Konfiguration und Feature Flags: [wo und wie]

## Beobachtbarkeit

- Dashboards: [Links]
- Alarme: [Links]
- Protokolle: [wo sie zu finden sind]
- SLOs: [Link]

## Betrieb

- Runbooks: [Links]
- Gängige Aufgaben: [Skalieren, Neustart, Backfill]
- Bekannte Probleme und Einschränkungen: [Notizen]

## Erste Schritte (für neue Beitragende)

<!-- Wie lokal gebaut, getestet, und ausgeführt wird. -->

## Kontakte

- Slack- / Chat-Kanal: [Link]
- Eskalation: [Pfad]
```

## SLO- / Fehlerbudget-Richtlinie

```markdown
# SLO- und Fehlerbudget-Richtlinie: [Dienst- oder Reisename]

- Besitzerin: [Team]
- Wirksam ab: [JJJJ-MM-TT]
- Überprüfungstakt: [z. B. vierteljährlich]

## Service Level Indicators (SLIs)

<!-- Definieren Sie jedes SLI präzise: die gemessene Größe, wie sie
     gemessen wird, und woher (idealerweise aus der Perspektive der
     Nutzerin). -->

| SLI | Definition | Datenquelle |
|-----|-----------|-------------|
| Verfügbarkeit | [z. B. erfolgreiche Anfragen / Gesamtanfragen] | [Quelle] |
| Latenz | [z. B. Anteil der Anfragen unter Xms] | [Quelle] |

## Ziele (SLOs)

| SLI | Zielwert | Messfenster |
|-----|---------|-------------|
| Verfügbarkeit | [z. B. 99,9%] | [z. B. rollende 28 Tage] |
| Latenz | [z. B. 95% unter 300ms] | [rollende 28 Tage] |

## Fehlerbudget

<!-- Die erlaubte Unzuverlässigkeit: 100% minus dem Ziel, über das
     Fenster. Formulieren Sie das Budget in konkreten Begriffen
     (z. B. Minuten/Monat). -->

- Budget: [abgeleitete Erlaubnis]

## Richtlinie, wenn das Budget erschöpft ist

<!-- Die vereinbarten Konsequenzen. Machen Sie sie konkret und durchsetzbar. -->

- [z. B. Nicht-kritische Feature-Veröffentlichungen einfrieren, bis sich das Budget erholt.]
- [z. B. Zuverlässigkeitsarbeit im nächsten Planungszyklus priorisieren.]
- [z. B. An die Engineering-Führung eskalieren, falls zwei Fenster in Folge verletzt.]

## Richtlinie, wenn das Budget gesund ist

<!-- Welches zusätzliche Risiko das Team eingehen darf, z. B. schnellere Rollouts. -->

## Alarmierung

<!-- An dieses SLO gebundene Verbrauchsraten-Alarme und Schwellen. -->
```

## Risikoregistereintrag

```markdown
## Risiko: [Kurztitel des Risikos]

- Risiko-ID: [ID]
- Datum erhoben: [JJJJ-MM-TT]
- Besitzerin: [Name oder für die Verwaltung dieses Risikos verantwortliche Rolle]
- Kategorie: [Sicherheit | operativ | Compliance | finanziell | Lieferung | Anbieterin]
- Status: [Offen | In Minderung | Akzeptiert | Geschlossen]

### Beschreibung

<!-- Formulieren Sie das Risiko als: Ursache -> Ereignis -> Konsequenz.
     Was passieren könnte, und warum es wichtig ist. -->

### Bewertung

- Wahrscheinlichkeit: [Niedrig | Mittel | Hoch]
- Auswirkung: [Niedrig | Mittel | Hoch]
- Gesamtbewertung: [abgeleitet aus Wahrscheinlichkeit x Auswirkung]

### Aktuelle Kontrollen

<!-- Was dieses Risiko heute bereits reduziert. -->

### Minderungsplan

<!-- Geplante Aktionen, Wahrscheinlichkeit oder Auswirkung zu
     reduzieren, mit Besitzerinnen und Daten. Falls das Risiko
     akzeptiert wird, erfassen Sie, wer es akzeptierte und warum. -->

| Aktion | Besitzerin | Fälligkeitsdatum | Status |
|--------|-----------|-------------------|--------|
| [Aktion] | [Name] | [Datum] | [Status] |

### Überprüfung

- Nächstes Überprüfungsdatum: [JJJJ-MM-TT]
- Entscheidung / Notizen: [jede Akzeptanzfreigabe oder Änderung]
```

## Projekt-Onepager / Produktbrief

```markdown
# [Projekt- oder Produktname]: Onepager

- Sponsorin: [Name]
- Leitung: [Name]
- Datum: [JJJJ-MM-TT]
- Status: [Idee | Genehmigt | In Arbeit | Ausgeliefert]

## Problem

<!-- Ein Absatz: das Kunden- oder Geschäftsproblem, und Belege, dass
     es real und lösenswert ist. -->

## Zielgruppe

<!-- Wer dieses Problem hat und wer von seiner Lösung profitiert. -->

## Vorgeschlagene Lösung

<!-- Eine kurze Beschreibung, was wir bauen oder ändern werden. Halten
     Sie sie auf der Ebene der Absicht, nicht des Implementierungsdetails. -->

## Warum jetzt

<!-- Der Grund, dies jetzt zu tun statt später. -->

## Erfolgskennzahlen

<!-- Wie wir wissen werden, dass es funktionierte. Bevorzugen Sie
     messbare Ergebnisse. -->

- [Kennzahl und Zielwert]

## Umfang

- Im Umfang: [was wir tun werden]
- Außerhalb des Umfangs: [was wir nicht tun werden]

## Risiken und offene Fragen

<!-- Hauptunsicherheiten und Abhängigkeiten. -->

## Grober Plan und Meilensteine

<!-- Hochstufige Phasen und ungefähres Timing. -->

## Kosten und Ressourcen

<!-- Benötigte Menschen, Zeit, und Budget. -->
```

## Bereitschaftsdienst-Übergabenotizen

```markdown
# Bereitschaftsdienst-Übergabe: [JJJJ-MM-TT]

- Abgehende: [Name]
- Ankommende: [Name]
- Dienst(e): [Namen]

## Gesamtstatus

<!-- Eine Zeile: ruhig, laut, oder laufendes Problem. -->

## Offene Vorfälle

<!-- Jeder aktive oder kürzlich gelöste Vorfall, den die nächste
     Reagierende kennen muss, mit Links. -->

- [Vorfall, Status, und was bleibt]

## Laufende oder geplante Änderungen

<!-- Bereitstellungen, Migrationen, Wartungsfenster, oder laufende
     Experimente, die Alarme verursachen könnten. -->

## Laute oder unzuverlässige Alarme

<!-- Ausgelöste Alarme und ihre wahre Bedeutung, damit die nächste
     Person nicht in die Irre geführt wird. Notieren Sie jede
     temporäre Stummschaltung und ihr Ablaufdatum. -->

## Beobachtungspunkte

<!-- Metriken oder Systeme, die sich in eine besorgniserregende Richtung entwickeln. -->

## Ausstehende Folgeschritte

<!-- An die nächste Schicht übergebene Aufgaben, mit Links zu Tickets. -->

## Notizen

<!-- Alles andere Nützliche: Zugriffseigenheiten, Anbieterinnenprobleme, Kontext. -->
```

## Änderungsantrag (für regulierte Änderungskontrolle)

```markdown
# Änderungsantrag: [Änderungstitel]

- Änderungs-ID: [ID]
- Antragstellerin: [Name]
- Datum eingereicht: [JJJJ-MM-TT]
- Typ: [Standard | Normal | Notfall]
- Priorität: [Niedrig | Mittel | Hoch]
- Status: [Eingereicht | Genehmigt | Abgelehnt | Implementiert | Geschlossen]

## Beschreibung der Änderung

<!-- Was sich ändert und warum. Referenzieren Sie das Ticket oder die
     Anforderung. -->

## Betroffene Systeme und Komponenten

<!-- Betroffene Dienste, Daten, Umgebungen, und Nutzerinnen. -->

## Rechtfertigung und Geschäftsauswirkung

<!-- Der Grund für die Änderung und die Auswirkung, sie nicht zu tun. -->

## Risikobewertung

- Risikoniveau: [Niedrig | Mittel | Hoch]
- Potenzielle Auswirkung, falls die Änderung fehlschlägt: [Beschreibung]
- Auswirkung auf Sicherheit, Datenschutz, oder Compliance: [Beschreibung]

## Implementierungsplan

<!-- Geordnete Schritte, verantwortliche Parteien, und Timing. -->

## Test- und Validierungsplan

<!-- Wie Erfolg vor und nach der Änderung verifiziert wird. -->

## Rückzugs- / Rollback-Plan

<!-- Wie die Änderung rückgängig zu machen ist, falls sie fehlschlägt,
     und die Erholungszeit. -->

## Zeitplan

- Vorgeschlagenes Fenster: [Start und Ende, mit Zeitzone]
- Erwartete Ausfallzeit: [Dauer oder keine]

## Genehmigungen

| Rolle | Name | Entscheidung | Datum |
|-------|------|---------------|-------|
| Änderungsbesitzerin | [Name] | [genehmigt/abgelehnt] | [Datum] |
| Technische Überprüferin | [Name] | [genehmigt/abgelehnt] | [Datum] |
| Änderungsberatungsgremium | [Name] | [genehmigt/abgelehnt] | [Datum] |

## Überprüfung nach Implementierung

<!-- Ergebnis, aufgetretene Probleme, und ob Rückzug nötig war. -->
```

## Gliederung der Datenschutz-Folgenabschätzung (DPIA)

```markdown
# Datenschutz-Folgenabschätzung: [Name der Verarbeitungstätigkeit]

- Bewerterin: [Name]
- Datum: [JJJJ-MM-TT]
- Überprüferinnen: [DSB / Datenschutzkontakt]
- Status: [Entwurf | Überprüft | Genehmigt]

## 1. Beschreibung der Verarbeitung

<!-- Welche persönlichen Daten verarbeitet werden, wie, von wem, und
     zu welchem Zweck. Schließen Sie Datenflüsse von Erhebung bis
     Löschung ein. -->

- Betroffene Personen: [über wen die Daten sind]
- Datenkategorien: [Arten persönlicher Daten, besondere Kategorien notieren]
- Zwecke: [warum die Daten verarbeitet werden]
- Empfängerinnen und Auftragsverarbeiterinnen: [wer die Daten erhält oder handhabt]
- Aufbewahrungsfrist: [wie lange Daten aufbewahrt werden und Löschmethode]
- Internationale Übertragungen: [Ziele und Übertragungsmechanismus]

## 2. Notwendigkeit und Verhältnismäßigkeit

<!-- Ist die Verarbeitung für den Zweck notwendig? Ist sie die am
     wenigsten eingreifende Option? Was ist die Rechtsgrundlage oder
     Befugnis? -->

- Rechtsgrundlage / Befugnis: [Grundlage für jeden Zweck]
- Datenminimierung: [warum jedes Feld notwendig ist]
- Rechtfertigung von Genauigkeit und Aufbewahrung: [Notizen]
- Wie Rechte der betroffenen Person unterstützt werden: [Zugriff, Löschung, usw.]

## 3. Konsultation

<!-- Konsultierte Stakeholderinnen, und, wo relevant, betroffene Personen. -->

## 4. Risiken für Individuen

<!-- Identifizieren Sie Datenschutzrisiken und bewerten Sie jedes. -->

| Risiko für Individuen | Wahrscheinlichkeit | Schweregrad | Gesamt |
|------------------------|----------------------|----------------|--------|
| [z. B. unautorisierter Zugriff auf sensible Daten] | [N/M/H] | [N/M/H] | [Bewertung] |

## 5. Maßnahmen zur Risikoreduktion

<!-- Für jedes Risiko die Minderung und das Restrisiko danach. -->

| Risiko | Maßnahme | Restrisiko | Akzeptiert von |
|--------|----------|-------------|------------------|
| [Risiko] | [Kontrolle] | [N/M/H] | [Name] |

## 6. Ergebnis und Freigabe

- Restrisiko akzeptabel: [Ja | Nein]
- Maßnahmen genehmigt von: [Name, Rolle]
- Konsultation der Aufsichtsbehörde erforderlich: [Ja | Nein]
- Überprüfungsdatum: [JJJJ-MM-TT]
```
