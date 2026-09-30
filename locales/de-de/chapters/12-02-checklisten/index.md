# 12.2 Checklisten

Diese Checklisten sind praktische, gebrauchsfertige Schnellreferenzen. Kopieren Sie jede Checkliste in eine Pull-Request-Vorlage, eine Wiki-Seite, ein Ticket, oder eine Überprüfungstreffen-Agenda, und passen Sie die Punkte an Ihren Kontext an. Behandeln Sie jeden Punkt als etwas, das eine Person mit Ja oder Nein verifizieren kann. Eine Checkliste ist eine Gedächtnishilfe und ein geteilter Standard, kein Ersatz für Urteilsvermögen; löschen Sie Punkte, die nicht zutreffen, und fügen Sie Punkte hinzu, die Ihre Domäne fordert.

Leitfaden, sie gut zu nutzen:

- Halten Sie Checklisten kurz genug, dass Menschen sie tatsächlich vervollständigen. Falls eine Checkliste routinemäßig übersprungen wird, ist sie zu lang oder zu generisch.
- Automatisieren Sie jeden Punkt, den eine Maschine verifizieren kann (Formatierung, Tests, Scans), damit Menschen Aufmerksamkeit auf Urteilspunkte verwenden.
- Versionieren Sie Ihre Checklisten und überprüfen Sie sie periodisch. Eine Checkliste, die sich nie ändert, wird wahrscheinlich nicht genutzt.
- Unterscheiden Sie blockierende von beratenden Punkten, wenn die Unterscheidung für Ihren Prozess wichtig ist.

## Codeüberprüfungs-Checkliste

Für die Überprüferin, die die Änderung einer anderen Person untersucht.

- [ ] Die Änderung tut, was ihre Beschreibung und das verlinkte Ticket sagen, dass sie tut.
- [ ] Der Umfang ist auf ein einzelnes logisches Anliegen fokussiert; unverwandte Änderungen sind ausgegliedert.
- [ ] Das Design passt zur bestehenden Architektur und führt keine einfacher zu vermeidende Kopplung ein.
- [ ] Randfälle, Fehlerpfade, und Fehlschlagsmodi sind gehandhabt, nicht nur der Happy Path.
- [ ] Tests existieren, sind bedeutsam, und würden fehlschlagen, falls das Verhalten regressierte.
- [ ] Benennung, Struktur, und Kommentare machen den Code für eine zukünftige Leserin verständlich.
- [ ] Keine Geheimnisse, Anmeldedaten, Tokens, oder persönlichen Daten sind committed.
- [ ] Sicherheitssensible Eingabe wird angemessen validiert, kodiert, oder parametrisiert.
- [ ] Öffentliche Schnittstellen, Verträge, und Rückwärtskompatibilität sind erhalten oder absichtlich versioniert.
- [ ] Protokollierung, Metriken, und Fehlerberichterstattung sind angemessen, die Änderung in Produktion zu betreiben.
- [ ] Dokumentation, Runbooks, und Konfiguration sind aktualisiert, um zur Änderung zu passen.
- [ ] Rückmeldung ist in blockierende Probleme versus Vorschläge getrennt, und über den Code formuliert.

## Pull-Request-Autorinnen-Checkliste

Für die Autorin, bevor sie Überprüfung anfragt.

- [ ] Der PR ist klein und fokussiert genug, in einer Sitzung sorgfältig überprüft zu werden.
- [ ] Die Beschreibung erklärt, was sich änderte, warum, und wie es verifiziert wurde.
- [ ] Das verlinkte Ticket, Issue, oder Designdokument gibt Überprüferinnen den nötigen Kontext.
- [ ] Alle automatisierten Prüfungen bestehen lokal oder in CI (Build, Lint, Format, Tests, Scans).
- [ ] Neues und geändertes Verhalten ist durch Tests abgedeckt.
- [ ] Mechanische Refaktorierungen sind von Verhaltensänderungen getrennt.
- [ ] Selbstüberprüfung ist abgeschlossen: Sie haben Ihren eigenen Diff Zeile für Zeile gelesen.
- [ ] Kein Debug-Code, auskommentierte Blöcke, Geheimnisse, oder verirrte Dateien bleiben.
- [ ] Datenbankmigrationen, Feature Flags, und Konfigurationsänderungen sind dokumentiert und umkehrbar.
- [ ] Breaking Changes sind explizit mit einem Migrationspfad benannt.
- [ ] Screenshots, Aufnahmen, oder Beispielausgabe sind eingeschlossen, wo sie Überprüfung unterstützen.
- [ ] Die richtigen Überprüferinnen und alle geforderten rollenbasierten Genehmigerinnen sind angefragt.

## Definition of Done

Der geteilte Standard, den ein Arbeitspunkt erfüllen muss, bevor er als abgeschlossen gilt.

- [ ] Abnahmekriterien im Ticket sind alle erfüllt und demonstrierbar.
- [ ] Code ist von Peers überprüft und von den geforderten Überprüferinnen genehmigt.
- [ ] Automatisierte Tests sind geschrieben, bestehen, und sind mit der Änderung gemergt.
- [ ] Code ist zur Hauptlinie gemergt und stellt sauber durch die Pipeline bereit.
- [ ] Keine bekannten Defekte der vereinbarten Schweregradschwelle bleiben offen.
- [ ] Dokumentation, Hilfetext, und Runbooks sind aktualisiert.
- [ ] Beobachtbarkeit ist vorhanden: relevante Protokolle, Metriken, und Alarme existieren.
- [ ] Sicherheits- und Datenschutzimplikationen wurden bedacht und adressiert.
- [ ] Barrierefreiheitsanforderungen für die Änderung sind erfüllt, wo nutzerinnenzugewandt.
- [ ] Feature Flags sind konfiguriert und der Rollout-Plan ist vereinbart.
- [ ] Die Produktbesitzerin oder Stakeholderin hat das Ergebnis akzeptiert.
- [ ] Jede Folgearbeit ist als verfolgte Tickets erfasst, nicht implizit gelassen.

## Produktions-Launch- / Go-Live-Bereitschaft

Bevor eine bedeutsame Änderung oder ein neuer Dienst in Produktion ausgeliefert wird.

- [ ] Rollout-Plan ist dokumentiert, einschließlich gestufter oder Kanarienschritte und Erfolgskriterien.
- [ ] Rollback-Plan ist dokumentiert, getestet, und kann schnell ausgeführt werden.
- [ ] Kapazitäts- und Lasttests zeigen, dass das System erwartete und Spitzennachfrage erfüllt.
- [ ] Überwachung, Dashboards, und Alarme sind live und vor dem Launch validiert.
- [ ] Bereitschaftsdienstabdeckung ist geplant und die Reagierenden kennen das System.
- [ ] Runbooks existieren für die wahrscheinlichsten Fehlschlags- und operativen Szenarien.
- [ ] Abhängigkeiten, Integrationen, und Drittparteien sind als bereit bestätigt und Ratenlimits verstanden.
- [ ] Sicherheitsüberprüfung und geforderte Freigaben sind abgeschlossen.
- [ ] Datenmigration, falls vorhanden, ist Ende-zu-Ende mit verifiziertem Rückzug getestet.
- [ ] Feature Flags erlauben, die Änderung ohne Neubereitstellung zu deaktivieren.
- [ ] Rechtliche, Datenschutz-, und Compliance-Genehmigungen sind erhalten, wo gefordert.
- [ ] Kommunikationsplan deckt Stakeholderinnen, Support, und Kundinnen ab.
- [ ] Eine Go/No-Go-Entscheidung wird von benannten Besitzerinnen gegen explizite Kriterien getroffen.

## Sicherheitsüberprüfungs- / Bedrohungsmodell-Checkliste

Zum Bewerten der Sicherheitslage einer Änderung oder eines Systems.

- [ ] Vertrauensgrenzen und Datenflüsse sind identifiziert und dokumentiert.
- [ ] Authentifizierung wird an jedem Eintrittspunkt erzwungen, der sie fordert.
- [ ] Autorisierungsprüfungen erzwingen Least Privilege für jede Aktion und Ressource.
- [ ] Alle externe Eingabe wird validiert, und Ausgabe ist für ihre Senke kodiert.
- [ ] Geheimnisse sind in einem verwalteten Tresor gespeichert, nie in Code oder Konfiguration, und rotierbar.
- [ ] Daten sind während Übertragung und im Ruhezustand verschlüsselt, wie die Klassifikation fordert.
- [ ] Abhängigkeiten werden auf bekannte Schwachstellen gescannt und aktuell gehalten.
- [ ] Injection-, Deserialisierungs-, und SSRF-Risiken sind für nicht vertrauenswürdige Eingabe gemindert.
- [ ] Sicherheitsrelevante Ereignisse werden protokolliert, ohne sensible Daten aufzuzeichnen.
- [ ] Ratenbegrenzung, Kontingente, und Missbrauchsschutz schützen exponierte Endpunkte.
- [ ] Fehlermeldungen lecken keine Stack Traces, internen Details, oder sensiblen Einzelheiten.
- [ ] Über STRIDE oder Ähnliches identifizierte Bedrohungen sind mit Minderungen oder akzeptiertem Risiko erfasst.
- [ ] Sicherheitstesten (SAST, DAST, oder Penetrationstest) ist geplant oder abgeschlossen.

## Datenschutz- (DPIA-artige) Checkliste

Für Verarbeitung, die persönliche oder sensible Daten involviert.

- [ ] Die gesammelten persönlichen Daten sind inventarisiert, klassifiziert, und auf das Nötige minimiert.
- [ ] Die Rechtsgrundlage oder Befugnis für jeden Verarbeitungszweck ist dokumentiert.
- [ ] Zweckbindung wird erzwungen: Daten werden nur für die erklärten Zwecke genutzt.
- [ ] Aufbewahrungsfristen sind definiert und Löschung oder Anonymisierung ist automatisiert.
- [ ] Rechte der betroffenen Person (Zugriff, Korrektur, Löschung, Übertragbarkeit) können erfüllt werden.
- [ ] Einwilligung, wo darauf gestützt, ist freiwillig gegeben, spezifisch, und widerrufbar.
- [ ] Drittparteien und Auftragsverarbeiterinnen sind an angemessene Datenschutzbedingungen gebunden.
- [ ] Grenzüberschreitende Übertragungen haben einen angemessenen rechtlichen Übertragungsmechanismus.
- [ ] Zugriff auf persönliche Daten ist eingeschränkt, protokolliert, und überprüft.
- [ ] Datenschutzrisiken für Individuen sind bewertet und gemindert oder eskaliert.
- [ ] Datenschutzverletzungs-Erkennungs- und Benachrichtigungsprozesse sind definiert.
- [ ] Privacy by Design und Default-Entscheidungen sind für das Feature dokumentiert.
- [ ] Die Datenschutzbeauftragte oder Datenschutzüberprüferin hat freigegeben, wo gefordert.

## Barrierefreiheits- (WCAG-) Checkliste

Für nutzerinnenzugewandte Schnittstellen, an WCAG-Prinzipien ausgerichtet.

- [ ] Aller Inhalt ist ausschließlich mit einer Tastatur erreichbar und bedienbar.
- [ ] Fokusreihenfolge ist logisch und ein sichtbarer Fokusindikator ist vorhanden.
- [ ] Textfarbkontrast erfüllt das Zielverhältnis (typischerweise 4,5:1 für Fließtext).
- [ ] Bilder und Nicht-Text-Inhalt haben bedeutsamen alternativen Text.
- [ ] Formularfelder haben zugeordnete Labels und klare Fehlermeldungen.
- [ ] Überschriften, Landmarken, und Struktur sind semantisch ausgezeichnet.
- [ ] Interaktive Komponenten exponieren korrekten Namen, Rolle, und Zustand für assistive Technologie.
- [ ] Inhalt fließt neu und bleibt bei 200%-Zoom und auf kleinen Bildschirmen nutzbar.
- [ ] Zeitlimits sind anpassbar, und Bewegung oder automatisch abspielender Inhalt kann pausiert werden.
- [ ] Farbe ist nicht das einzige Mittel, Information zu übermitteln.
- [ ] Medien haben Untertitel und, wo nötig, Transkripte oder Audiobeschreibung.
- [ ] Die Schnittstelle ist mit einem Screenreader und automatisiertem Barrierefreiheitswerkzeug getestet.

## API-Design-Überprüfungs-Checkliste

Bevor eine API veröffentlicht oder geändert wird.

- [ ] Ressourcen- und Operationsbenennung ist konsistent und vorhersagbar.
- [ ] Der Vertrag ist in einem maschinenlesbaren Schema spezifiziert (zum Beispiel OpenAPI).
- [ ] Versionierungsstrategie ist definiert und Rückwärtskompatibilität ist erhalten oder verwaltet.
- [ ] Pagination, Filterung, und Sortierung folgen konsistenten Konventionen.
- [ ] Fehlerantworten nutzen konsistente Struktur, Codes, und handlungsfähige Meldungen.
- [ ] Authentifizierung und Autorisierung sind für jede Operation spezifiziert.
- [ ] Eingabevalidierung und Größenlimits sind definiert und durchgesetzt.
- [ ] Idempotenz ist für Operationen definiert, bei denen Retries erwartet werden.
- [ ] Ratenlimits, Kontingente, und Drosselungsverhalten sind dokumentiert.
- [ ] Timeouts, Retries, und Fehlschlagssemantik sind Clients klar.
- [ ] Exposition sensibler Daten in Antworten ist minimiert und gerechtfertigt.
- [ ] Dokumentation schließt Beispiele für jede Operation und jeden Fehlerfall ein.
- [ ] Deprecation-Richtlinie und Sunset-Zeitpläne sind definiert.

## Architekturentscheidungs- (ADR-) Überprüfungs-Checkliste

Zum Überprüfen einer vorgeschlagenen Architekturentscheidungsaufzeichnung.

- [ ] Der Kontext und das gelöste Problem sind klar erklärt.
- [ ] Die Entscheidung ist unzweideutig als eine einzelne Wahl erklärt.
- [ ] Mindestens zwei realistische Alternativen wurden betrachtet und verglichen.
- [ ] Konsequenzen, sowohl positive als auch negative, sind dokumentiert.
- [ ] Nicht-funktionale Auswirkungen (Leistung, Sicherheit, Kosten, Betreibbarkeit) sind adressiert.
- [ ] Die Entscheidung richtet sich an bestehenden Prinzipien und vorherigen ADRs aus, oder ersetzt sie explizit.
- [ ] Betroffene Teams und Stakeholderinnen wurden konsultiert.
- [ ] Die Umkehrbarkeit und die Änderungskosten sind bewertet.
- [ ] Annahmen und Einschränkungen sind explizit gemacht.
- [ ] Der Status (vorgeschlagen, akzeptiert, ersetzt) ist gesetzt und datiert.
- [ ] Die Entscheidung ist auffindbar und von relevanten Systemen verlinkt.
- [ ] Jede Folgeaktion oder Migration ist als verfolgte Arbeit erfasst.

## Vorfallreaktions-Checkliste

Während eines aktiven Produktionsvorfalls.

- [ ] Den Vorfall erklären und eine einzelne Incident Commander zuweisen.
- [ ] Schweregrad, Umfang, und Kundinnenauswirkung bewerten und kommunizieren.
- [ ] Einen dedizierten Kommunikationskanal und Vorfallsaufzeichnung öffnen.
- [ ] Klare Rollen zuweisen: Commander, Kommunikationsleitung, und Betriebsleitung.
- [ ] Minderung und Diensterholung über Ursachenanalyse priorisieren.
- [ ] Regelmäßige Statusupdates in festgesetztem Takt an Stakeholderinnen senden.
- [ ] Eine Zeitleiste von Ereignissen, Aktionen, und Entscheidungen erfassen, während sie passieren.
- [ ] Bei Bedarf zu zusätzlichen Reagierenden oder Anbieterinnen eskalieren.
- [ ] Recht, Sicherheit, und Compliance benachrichtigen, falls Daten oder Regulierung involviert sind.
- [ ] Den Fix verifizieren und bestätigen, dass sich das System vollständig erholt hat.
- [ ] Den Vorfall formell schließen und die Lösung kommunizieren.
- [ ] Das schuldfreie Postmortem planen, bevor sich Menschen zerstreuen.

## Postmortem-Checkliste

Für die retrospektive Überprüfung nach einem Vorfall.

- [ ] Die Überprüfung ist schuldfrei und fokussiert auf Systeme und beitragende Faktoren.
- [ ] Eine faktische, zeitgestempelte Zeitleiste des Vorfalls ist dokumentiert.
- [ ] Kundinnen- und Geschäftsauswirkung ist quantifiziert (Dauer, Umfang, Kosten).
- [ ] Erkennung wird analysiert: wie und wann das Problem bemerkt wurde.
- [ ] Reaktion wird analysiert: was half und was Erholung verlangsamte.
- [ ] Beitragende Ursachen sind identifiziert, nicht nur eine einzelne Grundursache.
- [ ] Was gut lief wird erfasst, sowie was schieflief.
- [ ] Aktionspunkte sind spezifisch, Besitzerinnen zugewiesen, und haben Fälligkeitsdaten.
- [ ] Aktionspunkte adressieren Prävention, Erkennung, und Minderung.
- [ ] Folgepunkte werden im normalen Backlog bis zur Fertigstellung verfolgt.
- [ ] Das Postmortem wird breit geteilt, damit andere daraus lernen können.
- [ ] Systemische Muster über Vorfälle hinweg werden periodisch überprüft.

## Bereitschaftsdienst-Bereitschafts-Checkliste

Bevor jemand eine Bereitschaftsdienstschicht übernimmt.

- [ ] Die Reagierende hat Zugriff auf alle Systeme, Dashboards, und Werkzeuge, die sie braucht.
- [ ] Alarmierung erreicht die Reagierende verlässlich und ist getestet.
- [ ] Eskalationspfade und sekundäre Bereitschaftsdienstkontakte sind bekannt und aktuell.
- [ ] Runbooks existieren für die häufigsten und schwerwiegendsten Alarme.
- [ ] Die Reagierende hat Onboarding oder Shadowing für diese Systeme abgeschlossen.
- [ ] Kürzliche Änderungen, laufende Vorfälle, und bekannte Probleme sind übergeben.
- [ ] Alarmschwellen sind getunt, um Rauschen und Fehlalarme zu minimieren.
- [ ] Die Reagierende weiß, wie sie einen Vorfall erklärt und die Commander erreicht.
- [ ] Zugriff auf Produktion ist von der Arbeitsumgebung der Reagierenden möglich.
- [ ] Kommunikationskanäle und Stakeholderinnen-Kontakte sind dokumentiert.
- [ ] Der Bereitschaftsdienstplan ist veröffentlicht und Abdeckung hat keine Lücken.
- [ ] Vergütung, Erwartungen, und Arbeitslastlimits für Bereitschaftsdienst sind klar.

## SLO-Definitions-Checkliste

Beim Definieren eines Service Level Objective.

- [ ] Die geschützte Nutzerinnenreise oder Fähigkeit ist klar identifiziert.
- [ ] Service Level Indicators (SLIs) sind als klare, messbare Größen definiert.
- [ ] SLIs werden, wo möglich, aus der Perspektive der Nutzerin gemessen.
- [ ] Das Zielniveau ist auf einem Niveau gesetzt, das Nutzerinnen tatsächlich brauchen, nicht 100%.
- [ ] Das Messfenster (zum Beispiel rollende 28 Tage) ist spezifiziert.
- [ ] Das aus dem Ziel abgeleitete Fehlerbudget ist berechnet und verstanden.
- [ ] Eine Richtlinie definiert, was passiert, wenn das Fehlerbudget erschöpft ist.
- [ ] Datenquellen für die SLIs sind verlässlich und instrumentiert.
- [ ] Alarmierung ist an Verbrauchsrate gebunden, nicht nur Schwellenverletzungen.
- [ ] Besitzerinnen und Stakeholderinnen stimmen zu, dass das SLO realistisch und bedeutsam ist.
- [ ] Das SLO ist dokumentiert und auf einem Dashboard sichtbar.
- [ ] Ein Zeitplan existiert, SLOs zu überprüfen und zu revidieren, während sich der Dienst entwickelt.

## CI/CD-Pipeline-Checkliste

Für eine Continuous-Integration- und -Delivery-Pipeline.

- [ ] Jeder Commit löst einen automatisierten Build- und Testlauf aus.
- [ ] Die Pipeline schlägt schnell fehl und meldet Ergebnisse klar an Autorinnen.
- [ ] Linting, Formatierung, und statische Analyse laufen automatisch.
- [ ] Unit-, Integrations-, und relevante End-zu-End-Tests laufen in der Pipeline.
- [ ] Sicherheits- und Abhängigkeitsscanning laufen bei jedem Build.
- [ ] Build-Artefakte sind versioniert, unveränderlich, und in einer Registry gespeichert.
- [ ] Geheimnisse werden sicher injiziert und nie in Protokollen ausgegeben.
- [ ] Bereitstellungen sind automatisiert und über Umgebungen hinweg wiederholbar.
- [ ] Bereitstellungsstrategie (Kanarie, Blau-Grün, rollend) ist definiert und genutzt.
- [ ] Rollback ist automatisiert oder eine einzelne dokumentierte Aktion.
- [ ] Pipeline-Berechtigungen folgen Least Privilege und sind überprüfbar.
- [ ] Pipeline-Konfiguration ist als Code in Versionskontrolle gespeichert.
- [ ] Build-Herkunft und ein Software Bill of Materials werden produziert, wo gefordert.

## Infrastructure-as-Code-Überprüfungs-Checkliste

Zum Überprüfen von als Code definierter Infrastruktur.

- [ ] Änderungen sind vollständig in Code ausgedrückt und durch die Pipeline angewendet.
- [ ] Ein Plan oder Dry-Run-Ausgabe wird vor Anwendung überprüft.
- [ ] Zustand wird sicher mit Sperrung gespeichert, um gleichzeitige Änderungen zu verhindern.
- [ ] Ressourcen folgen Benennungs-, Tagging-, und Besitzkonventionen.
- [ ] Least-Privilege-IAM-Rollen und -Richtlinien werden genutzt, ohne Wildcards, wo vermeidbar.
- [ ] Netzwerkexposition ist minimiert; kein unbeabsichtigter öffentlicher Zugriff.
- [ ] Geheimnisse und sensible Werte werden aus einem Tresor referenziert, nicht hartcodiert.
- [ ] Verschlüsselung ist für Speicher, Datenbanken, und Übertragung aktiviert.
- [ ] Änderungen sind idempotent und sicher erneut anzuwenden.
- [ ] Blast Radius ist verstanden; destruktive Änderungen sind benannt.
- [ ] Kostenauswirkung der Änderung wird bedacht.
- [ ] Module sind wiederverwendbar, versioniert, und getestet.
- [ ] Drift-Erkennung ist vorhanden, um Out-of-Band-Änderungen zu fangen.

## KI/ML-Modell-Veröffentlichungs-Checkliste

Bevor ein Machine-Learning-Modell in Produktion veröffentlicht wird.

- [ ] Der beabsichtigte Gebrauch, Umfang, und die Grenzen des Modells sind dokumentiert.
- [ ] Herkunft, Lizenzierung, und Einwilligung von Trainings- und Evaluationsdaten sind verifiziert.
- [ ] Daten und Modell sind versioniert und reproduzierbar.
- [ ] Leistung ist auf repräsentativen, zurückgehaltenen Testdaten evaluiert.
- [ ] Fairness und Bias sind über relevante Untergruppen bewertet.
- [ ] Das Modell wird gegen den Vorgänger oder eine Baseline evaluiert.
- [ ] Fehlschlagsmodi, Randfälle, und Out-of-Distribution-Verhalten sind verstanden.
- [ ] Sicherheits-, Missbrauchs-, und schädliche-Ausgabe-Risiken sind bewertet und gemindert.
- [ ] Überwachung auf Drift, Datenqualität, und Leistungsdegradation ist vorhanden.
- [ ] Ein Rollback oder Fallback zu einem vorherigen Modell oder regelbasierten Pfad existiert.
- [ ] Menschliche Aufsicht oder Einspruch wird für folgenreiche Entscheidungen bereitgestellt.
- [ ] Datenschutzüberprüfung deckt Trainingsdaten und Inferenzeingaben und -ausgaben ab.
- [ ] Eine Model Card oder gleichwertige Dokumentation wird für Stakeholderinnen veröffentlicht.

## Datenpipeline-Qualitäts-Checkliste

Für eine Datenpipeline, die Analytik oder Produkte speist.

- [ ] Quelldatenschemata werden validiert und Schemaänderungen werden erkannt.
- [ ] Ingestion handhabt späte, doppelte, und außer-der-Reihe-Datensätze korrekt.
- [ ] Datenqualitätsprüfungen (Vollständigkeit, Einzigartigkeit, Bereiche) laufen automatisch.
- [ ] Fehlgeschlagene Datensätze werden isoliert und sichtbar gemacht, nicht still verworfen.
- [ ] Transformationen sind mit repräsentativen und Randfall-Eingaben getestet.
- [ ] Die Pipeline ist idempotent und sicher nach Fehlschlag erneut auszuführen.
- [ ] Aktualität und Latenz von Ausgaben werden gegen Erwartungen überwacht.
- [ ] Herkunft ist dokumentiert, damit Konsumentinnen wissen, woher Daten kommen.
- [ ] Persönliche und sensible Daten sind angemessen klassifiziert, maskiert, oder eingeschränkt.
- [ ] Backfills und Reprocessing werden unterstützt und dokumentiert.
- [ ] Alarmierung benachrichtigt Besitzerinnen über Fehlschläge und Qualitätsverletzungen.
- [ ] Aufbewahrungs- und Löschrichtlinien werden auf gespeicherten Daten durchgesetzt.
- [ ] Nachgelagerte Konsumentinnen und SLAs sind dokumentiert.

## Open-Source-Aufnahme- und Lizenzüberprüfungs-Checkliste

Bevor eine Open-Source-Komponente übernommen wird.

- [ ] Die Lizenz der Komponente ist identifiziert und auf der genehmigten Liste.
- [ ] Lizenzverpflichtungen (Attribution, Copyleft, Hinweise) sind verstanden und erfüllt.
- [ ] Lizenzkompatibilität mit Ihrem Distributionsmodell ist bestätigt.
- [ ] Das Projekt wird aktiv gepflegt und hat eine gesunde Community.
- [ ] Bekannte Schwachstellen sind geprüft und die Version ist aktuell.
- [ ] Die Abhängigkeit und ihre transitiven Abhängigkeiten sind inventarisiert.
- [ ] Sicherheitslage und vergangene Vorfallsgeschichte sind überprüft.
- [ ] Die Komponente erfüllt einen echten Bedarf ohne bedeutsame Duplikation.
- [ ] Die Ausstiegskosten und Ersetzbarkeit der Komponente sind bedacht.
- [ ] Die Komponente ist im Software Bill of Materials erfasst.
- [ ] Eine benannte Besitzerin ist verantwortlich, Updates und Advisories zu verfolgen.
- [ ] Contribution-back- und interne-Fork-Richtlinien werden befolgt, falls modifiziert.

## Anbieter- / Drittparteien-Risiko-Checkliste

Bevor eine externe Anbieterin oder ein Dienst eingebunden wird.

- [ ] Der Geschäftsbedarf und die Daten, auf die die Anbieterin zugreifen wird, sind klar definiert.
- [ ] Die Sicherheitslage der Anbieterin ist bewertet (Zertifizierungen, Audits, Fragebogen).
- [ ] Datenverarbeitungsbedingungen, Eigentum, und Löschung bei Ausstieg sind vertraglich klar.
- [ ] Die Unterauftragsverarbeiterinnen und Datenstandorte der Anbieterin sind offengelegt und akzeptabel.
- [ ] Compliance mit relevanten Regulierungen ist verifiziert.
- [ ] Betriebszeit-, Support-, und SLA-Verpflichtungen sind dokumentiert.
- [ ] Verletzungsbenachrichtigungsverpflichtungen und Zeitrahmen sind im Vertrag.
- [ ] Zugriff ist auf Least Privilege begrenzt und widerrufbar.
- [ ] Geschäftskontinuität und die Auswirkung eines Anbieterinnenausfalls sind bewertet.
- [ ] Ein Ausstiegs- und Datenmigrationsplan existiert, um Lock-in zu vermeiden.
- [ ] Kosten, Erneuerungsbedingungen, und Preisänderungsklauseln sind verstanden.
- [ ] Die Anbieterin ist mit einem Überprüfungsdatum im Risikoregister erfasst.

## Behördliche-Compliance- (ATO- / FedRAMP-artige) Bereitschafts-Checkliste

Für Systeme, die formelle Betriebsautorisierung fordern.

- [ ] Die Systemgrenze und Datenflüsse sind definiert und diagrammiert.
- [ ] Daten sind nach Auswirkungsniveau und Sensibilität kategorisiert.
- [ ] Die anwendbare Kontrollbaseline ist ausgewählt und angepasst.
- [ ] Ein System Security Plan dokumentiert, wie jede Kontrolle implementiert ist.
- [ ] Kontrollen sind implementiert, belegt, und dem Plan zugeordnet.
- [ ] Kontinuierliche Überwachung und Schwachstellenscanning sind operativ.
- [ ] Ein Plan of Action and Milestones verfolgt offene Befunde bis zur Behebung.
- [ ] Zugriffskontrolle, Audit-Protokollierung, und Identitätsverwaltung erfüllen Anforderungen.
- [ ] Verschlüsselung nutzt genehmigte Algorithmen und validierte Module.
- [ ] Ein Vorfallreaktionsplan ist dokumentiert und getestet.
- [ ] Ein Notfall- und Notfallwiederherstellungsplan ist dokumentiert und getestet.
- [ ] Eine unabhängige Bewertung oder ein Audit der Kontrollen ist abgeschlossen.
- [ ] Die autorisierende Amtsträgerin hat die für die Autorisierungserteilung nötige Risikobewertung.
- [ ] Reauthorisierungsauslöser und der laufende Autorisierungstakt sind definiert.
