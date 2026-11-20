# 12.6 Übernahme-Roadmap

Dieser Anhang ist ein praktischer Leitfaden, die Praktiken in diesem Buch *inkrementell*
auszurollen. Die einzige wichtigste Anweisung im ganzen Handbuch, in jedem Kapitel
wiederholt, ist **inkrementell übernehmen; kein Big Bang**. Eine Transformation, die
versucht, alles auf einmal zu ändern, ändert nichts dauerhaft: sie erschöpft Wohlwollen,
überwältigt Teams, und kollabiert bei der ersten Krise. Eine Transformation, die mit
echtem Schmerz beginnt, einen sichtbaren Gewinn liefert, und sich von dort aus verstärkt,
kann eine Organisation von Tausenden über ein paar Jahre bewegen.

Diese Roadmap gibt Ihnen Prinzipien der Übernahme, eine reifebasierte Sequenz von den
ersten 90 Tagen bis zwei-plus Jahre, ein Priorisierungsframework mit einem
durchgearbeiteten Beispiel, domänenweise Quick Wins, spezielle Anleitung für Unternehmen
und Behörden, Wege, Erfolg zu messen, und die zu vermeidenden Fehlschlagsmodi.

## Prinzipien der Übernahme

Diese Prinzipien gelten unabhängig von Ihrer Größe, Ihrem Sektor, oder Ihrer
Ausgangsreife.

- **Mit Schmerz beginnen, nicht mit einem Framework.** Finden Sie, was am meisten
  schmerzt, ob langsame Veröffentlichungen, häufige Ausfälle, fehlgeschlagene Audits,
  oder Fluktuation, und beheben Sie das zuerst. Schmerz erschafft die Nachfrage und
  die politische Deckung, die ein Top-down-Mandat nie kann. Niemand widersteht
  Erleichterung.
- **Golden Paths über Mandate.** Machen Sie den empfohlenen Weg den *einfachsten*
  Weg. Ein Golden Path, der schneller, sicherer, und besser dokumentiert ist,
  gewinnt Übernahme aus eigenem Verdienst; eine Richtlinie, die langsamer als der
  Workaround ist, wird umgangen. Investieren Sie in den Golden Path, bevor Sie den
  Trampelpfad ablehnen.
- **Ergebnisse messen, nicht Aktivität.** Verfolgen Sie, ob die Änderung Lieferung,
  Zuverlässigkeit, Sicherheitslage, oder Nutzerinnenergebnisse verbesserte, nicht
  wie viele Teams am Training teilnahmen oder eine Box abhakten. Instrumentieren Sie,
  bevor Sie ändern, damit Sie die Wirkung beweisen können.
- **Executive-Sponsoring sichern, und behalten.** Nachhaltige Änderung braucht eine
  rechenschaftspflichtige Führungskraft, die Finanzierung schützt, Blockierer
  entfernt, und die Linie hält, wenn die Transformation unbequem wird. Sponsoring
  ist kein Launch-Ereignis; es ist eine laufende Beziehung, die Sie mit Ergebnissen
  neu verdienen müssen.
- **Freiwillige vor Wehrpflichtigen.** Beginnen Sie mit Teams, die sich ändern
  *wollen*. Ihr Erfolg wird die Referenzgeschichte, die die widerstrebende Mehrheit
  zieht. Den Widerstand zuerst zu zwingen produziert böswillige Compliance und
  abschreckende Geschichten.
- **Machen Sie es reversibel, wo Sie können.** Bevorzugen Sie Änderungen, die Sie
  pilotieren, messen, und zurückrollen können. Reversible "Zwei-Wege-Tür"-
  Entscheidungen können schnell gehen; reservieren Sie schweren Prozess für das
  wirklich Irreversible.
- **Zeigen Sie Gewinne früh und oft.** Liefern Sie etwas Sichtbares in Wochen, nicht
  Quartalen. Momentum ist eine Ressource; nutzen Sie den ersten Gewinn, den nächsten
  zu finanzieren.
- **Treffen Sie Teams, wo sie sind.** Ein einzelner uniform angewandter Reifebalken
  ist unfair und demoralisierend. Sequenzieren Sie nach der Bereitschaft und dem
  Schmerz jedes Teams.

## Reifebasierte Sequenzierung

Die untenstehenden Horizonte sind kumulativ: jeder baut auf dem letzten auf. Daten
sind Anleitung, keine Fristen; eine große oder schwer regulierte Organisation mag
jede Phase länger laufen lassen. Das Muster (*stabilisieren, dann standardisieren,
dann skalieren, dann nachhaltig erhalten*) gilt unabhängig vom Tempo.

### Erste 90 Tage: Stabilisieren und beweisen

Ziel: eine Baseline etablieren, ein oder zwei Flaggschiff-Probleme wählen, und
einen glaubwürdigen ersten Gewinn mit einem willigen Team liefern.

- [ ] Eine rechenschaftspflichtige Executive-Sponsorin und eine kleine Leitkoalition benennen.
- [ ] Die vier DORA-Metriken (Bereitstellungshäufigkeit, Durchlaufzeit, Änderungsfehlschlagsrate,
      Wiederherstellungszeit) als Baseline nehmen, auch wenn die Zahlen grob sind.
- [ ] Eine leichtgewichtige Bewertung gegen die Reifegradmodelle in Kapitel 12.4
      durchführen, um die größten Lücken zu finden.
- [ ] Ein oder zwei Pilotteams wählen, die sich *freiwillig* melden und echten Schmerz haben.
- [ ] Ein hochsichtbares Problem Ende zu Ende beheben (z. B. die Bereitstellung eines
      Teams automatisieren, oder SLOs zu einem kritischen Dienst hinzufügen).
- [ ] Eine geteilte Aufzeichnung von Entscheidungen (ADRs) und einen Ort, Ergebnisse
      zu veröffentlichen, aufstellen.
- [ ] Vereinbaren, wie Sie Erfolg messen werden, *bevor* Sie irgendetwas ändern.

### Bis 6 Monate: Das gewinnende Muster standardisieren

Ziel: den Erfolg des Piloten in ein wiederholbares, dokumentiertes Muster verwandeln
und es als Golden Path der nächsten Teamkohorte anbieten.

- [ ] Den Golden Path aus dem Piloten als wiederverwendbare Vorlagen, Pipelines,
      und Dokumentation veröffentlichen.
- [ ] Ein Plattform- oder ermöglichendes Team (auch ein virtuelles) etablieren,
      um den Golden Path zu besitzen und zu unterstützen.
- [ ] Das Muster auf drei bis fünf weitere Teams ausrollen, nach Wirkung und
      Bereitschaft priorisiert.
- [ ] Automatisierte Qualitäts- und Sicherheitstore (Linting, Tests, SAST/SCA) als
      Standardeinstellungen, nicht Add-ons, in die geteilte Pipeline einführen.
- [ ] Eine schuldfreie Vorfallüberprüfungspraxis beginnen und Postmortems intern veröffentlichen.
- [ ] Ein leichtgewichtiges Governance-Forum (Architekturüberprüfung, Golden-Path-
      Stewardship) einrichten, das entblockiert statt torhütet.

### Bis 12 Monate: Über die Organisation skalieren

Ziel: den Golden Path zum Standard für die meiste neue Arbeit machen und beginnen,
die schlimmsten Legacy-Praktiken stillzulegen.

- [ ] Den Auftrag des Plattformteams erweitern; einen Dienstkatalog und Scorecards veröffentlichen.
- [ ] Organisationsweite Baselines setzen: SLOs für Tier-1-Dienste, Sicherheitskontrollen
      in jeder Pipeline, Barrierefreiheitsprüfungen in Frontend-Builds.
- [ ] Übernahmeraten pro Team verfolgen und die Daten sichtbar machen.
- [ ] Absichtliche Legacy-Modernisierung bei den Systemen höchsten Risikos mit
      Strangler-Fig- und Branch-by-Abstraction-Mustern beginnen.
- [ ] Messung in Planung falten: Teams überprüfen ihre DORA- und Zuverlässigkeitstrends
      im normalen Betriebsrhythmus.
- [ ] In Befähigung investieren (internes Training, Mentoring, Communities of Practice),
      damit sich Fähigkeit schneller als Mandate verbreitet.

### 2+ Jahre: Nachhaltig erhalten und kontinuierlich verbessern

Ziel: die Praktiken sind "wie wir arbeiten", kein Programm, und die Organisation
verbessert sie ohne zentralen Schub.

- [ ] Das Transformationsprogramm als benannte Initiative stilllegen; seine Arbeit
      in normale Governance und Plattformbetrieb einbetten.
- [ ] Den Golden Path als Produkt mit eigener Roadmap, Nutzerinnen, und
      Zufriedenheitsmetriken (Entwicklerinnenerfahrungsumfragen) behandeln.
- [ ] Technische Schulden und Modernisierung als stehendes Portfolio verwalten, nicht
      als einmaligen Schub.
- [ ] Periodische Reifeneubewertungen durchführen und Standards aufwärts anpassen,
      während der Boden steigt.
- [ ] Gegen Regression schützen: Sponsoring behalten, weiter messen, und Praktiken
      auffrischen, während sich Technologie und Bedrohungen entwickeln.

## Ein Priorisierungsframework

Sie werden immer mehr Verbesserungen zu machen haben als Kapazität, sie zu machen.
Priorisieren Sie mit einem einfachen, verteidigbaren Modell statt der lautesten
Stimme im Raum.

Bewerten Sie jede Kandidateninitiative auf drei Dimensionen:

- **Wirkung (1–5):** Wie sehr wird dies ein echtes Ergebnis verbessern (Liefer-
  geschwindigkeit, Zuverlässigkeit, Sicherheit, Kosten, oder Nutzerinnenwert), und
  für wie viele Teams oder Nutzerinnen?
- **Aufwand (1–5):** Wie viel Arbeit, Koordination, und Störung, um es zu liefern?
  (Höher = mehr Aufwand.)
- **Risikogewicht (0,5–2,0):** Ein Multiplikator für Dringlichkeit und Exposition.
  Sicherheits-, Compliance-, und Sicherheitsprobleme tragen ein höheres Gewicht;
  Nice-to-haves tragen weniger.

Ein nützlicher Rankingwert ist:

```
Priorität = (Wirkung × Risikogewicht) ÷ Aufwand
```

Ranken Sie nach absteigender Priorität. Sequenzieren Sie die Top-Punkte, aber
halten Sie immer mindestens einen schnellen, niedrigaufwändigen "Quick Win" in
Bewegung, um Momentum aufrechtzuerhalten, und überdenken Sie die Werte jedes
Quartal, während sich Bedingungen ändern.

### Durchgearbeitetes Beispiel

| Initiative | Wirkung | Aufwand | Risikogewicht | Priorität | Sequenz |
|---|---|---|---|---|---|
| Bereitstellung für den umsatzstärksten Dienst automatisieren | 5 | 2 | 1,5 | 3,75 | Jetzt |
| SLOs und Alarmierung zu Tier-1-Diensten hinzufügen | 4 | 2 | 1,5 | 3,00 | Jetzt |
| SAST/SCA in geteilte Pipeline einführen | 4 | 2 | 2,0 | 4,00 | Jetzt |
| Ein Designsystem für alle Frontends ausrollen | 4 | 5 | 1,0 | 0,80 | Später |
| Mainframe-Batch zur Cloud migrieren | 5 | 5 | 1,5 | 1,50 | Gestuft |
| ADRs teamübergreifend standardisieren | 3 | 1 | 1,0 | 3,00 | Jetzt (Quick Win) |
| Eine neue Programmiersprache organisationsweit übernehmen | 2 | 5 | 0,5 | 0,20 | Aufschieben |

In diesem Beispiel führt die Sicherheitspipeline-Arbeit die Liste an wegen ihres
hohen Risikogewichts und bescheidenen Aufwands, während die organisationsweite
Sprachänderung trotz Begeisterung nach unten fällt, weil ihre Wirkung niedrig und
ihr Aufwand und ihre Störung hoch sind. Das Framework macht diese Abwägung
explizit und diskutierbar, was ihr echter Wert ist.

## Domänenweise Quick Wins

Jeder Teil des Buches hat einen günstigen, hochsignifikanten ersten Schritt.
Beginnen Sie hier.

| Teil | "Hier beginnen"-Quick-Win |
|---|---|
| **Grundlagen (Kultur, Teams, Prozess)** | Leichtgewichtige ADRs übernehmen und eine schuldfreie Retrospektive durchführen; Entscheidungen und Lernen sichtbar machen. |
| **Programmierhandwerk** | Einen Auto-Formatierer und Linter in CI als durchgesetzte Standardeinstellungen aktivieren, damit Stil aufhört, ein Überprüfungsthema zu sein. |
| **Architektur** | Eine einseitige Architekturentscheidung und ein C4-Kontextdiagramm für Ihr wichtigstes System schreiben. |
| **Sicherheit** | Abhängigkeitsscanning (SCA) und Geheimnisscanning zur Pipeline hinzufügen; zuerst für ein kritisches Repository aktivieren. |
| **UX / Design** | Drei günstige Nutzbarkeitstests auf Ihrem verkehrsreichsten Fluss durchführen; das größte beobachtete Problem beheben. |
| **KI / ML** | Ein einseitiges Problem-Framing und eine Datenbereitschaftsprüfung vor jeder Modellarbeit schreiben; definieren, wie Sie Erfolg evaluieren werden. |
| **Daten / Analytik** | Eine einzelne vereinbarte "Nordstern"-Metrik und ein vertrauenswürdiges Dashboard definieren; ein widersprüchliches stilllegen. |
| **DevOps / Plattform** | Ein Team zu einer vollständig automatisierten Build-Test-Deploy-Pipeline bringen und sie als Vorlage dokumentieren. |
| **Betrieb / Zuverlässigkeit** | SLIs und ein SLO für Ihre kritischste Nutzerinnenreise definieren; auf Symptome alarmieren, nicht Ursachen. |
| **Unternehmen / Behörden** | Ihre aktuellen Kontrollen auf ein Framework (NIST CSF, ISO 27001, oder SOC 2) abbilden und Nachweise für eine Kontrolle automatisieren. |

## Spezielle Anleitung für Unternehmen

Große etablierte Organisationen tragen Skalierung, viele Teams, tiefes Legacy, und
schweren Change-Management-Overhead. Passen Sie die Roadmap entsprechend an.

- **Föderieren, nicht alles zentralisieren.** Ein einzelnes zentrales Team kann
  nicht Hunderte von Produktteams bedienen. Nutzen Sie ein Plattformteam, um
  Golden Paths bereitzustellen, und ermöglichende Teams, um zu coachen, während
  Produktteams Besitz behalten. (Siehe Team Topologies.)
- **Conways Gesetz respektieren.** Ihre Architektur wird Ihr Organigramm spiegeln.
  Falls Sie entkoppelte Dienste wollen, brauchen Sie entkoppelte, befähigte Teams;
  organisieren Sie absichtlich um, statt gegen die Maserung zu kämpfen.
- **Legacy als Portfolio behandeln.** Sie können nicht alles modernisieren. Ranken
  Sie Legacy-Systeme nach Risiko und Geschäftswert, und wenden Sie Strangler-Fig-
  Migration auf die wenigen an, die zählen; frieren Sie den Rest absichtlich ein
  oder lassen Sie ihn auslaufen.
- **Change Management ist echte Arbeit.** Im Maßstab sind Kommunikation, Training,
  und Anreizausrichtung kein Overhead: sie sind die Transformation. Budgetieren Sie
  für Befähigung, Communities of Practice, und internen Evangelismus explizit.
- **Hüten Sie sich vor dem Mandat-Reflex.** Große Organisationen greifen standardmäßig
  zu Richtlinienschreiben. Widerstehen Sie. Ein Mandat ohne Golden Path produziert
  Box-Ticking; ein Golden Path ohne Mandat produziert echte Übernahme.
- **Anreize und Finanzierung ausrichten.** Von Projektfinanzierung zu dauerhaften
  Produktteams verschieben, damit Verbesserungen das Enddatum eines Projekts
  überleben. Ergebnisse belohnen, nicht Ausgabe.

## Spezielle Anleitung für Behörden

Organisationen des öffentlichen Sektors fügen Beschaffungszyklen, Compliance-Tore,
Auftragnehmerinnenverwaltung, mehrjährige Finanzierung, und Transparenzverpflichtungen
hinzu. Dies sind Designeingaben, keine Ausreden.

- **Für die ATO vom ersten Tag an entwerfen.** Authorization to Operate und
  kontinuierliche-Überwachungs-Tore (gemäß NIST RMF / 800-37) können Zeitpläne
  dominieren. Bauen Sie Sicherheitskontrollen und Nachweiserhebung früh in die
  Pipeline ein, damit Compliance kontinuierlich ist, nicht ein spätes, blockierendes
  Gerangel.
- **Inkrementell einkaufen.** Mehrjährige Big-Bang-Beschaffungen institutionalisieren
  den Big-Bang-Fehlschlag, vor dem dieses Buch warnt. Bevorzugen Sie modulare
  Vertragsgestaltung, kleinere Zuschläge, und ergebnisbasierte Leistungsbeschreibungen,
  die Iteration erlauben.
- **Anbieterinnen und Integratorinnen als Teil des Teams verwalten.** Viel
  Behörden-Engineering wird von Auftragnehmerinnen geliefert. Schreiben Sie Golden
  Paths, Qualitätstore, und Transparenzanforderungen in Verträge, und stellen Sie
  Wissens- und Codetransfer zur Behörde sicher, um Lock-in und Bus-Faktor-Risiko
  zu vermeiden.
- **Um Finanzierungszyklen herum planen.** Mehrjährige und jährliche Bewilligungen
  schränken ein, wozu Sie sich verpflichten können. Sequenzieren Sie Arbeit, damit
  jedes finanzierte Inkrement eigenständigen Wert liefert und Sie nicht mitten in
  der Transformation stranden lässt, falls sich Finanzierung verschiebt.
- **Barrierefreiheit und Klarsprache sind rechtliche Verpflichtungen.** Section 508,
  der ADA, WCAG, und Klarsprache-Mandate sind Anforderungen, keine Verbesserungen.
  Backen Sie Barrierefreiheitsprüfungen in Pipelines und Inhaltsüberprüfung in den
  Workflow ein.
- **Transparenz ist ein Feature.** FOIA, Open-Source-Mandate ("öffentliches Geld,
  öffentlicher Code"), und veröffentlichte Dienststandards bedeuten, dass Ihre
  Arbeit öffentlicher Prüfung unterliegt. Entwerfen Sie dafür: klare Aufzeichnungen,
  offen wo angemessen, und ehrliche veröffentlichte Leistungsdaten.
- **Bewährten öffentlichen-Sektor-Mustern folgen.** Das U.S. Digital Services
  Playbook, der GOV.UK Service Standard, und USWDS kodifizieren hart erkämpfte
  Lektionen; übernehmen Sie sie, statt neu zu erfinden.

## Übernahmeerfolg messen

Messen Sie sowohl *führende* Indikatoren (frühe Signale, dass die Änderung Fuß
fasst) als auch *nachlaufende* Indikatoren (die Ergebnisse, die Ihnen letztlich
wichtig sind). Beobachten Sie den Trend, nicht eine einzelne Ablesung, und lassen
Sie nie eine Metrik zu einem getrickten Ziel werden.

| Typ | Indikator | Was er Ihnen sagt |
|---|---|---|
| Führend | Anzahl Teams auf dem Golden Path | Wie schnell sich Übernahme verbreitet |
| Führend | Pipeline-Tor-Abdeckung (Tests, SAST, a11y) | Wie eingebettet Qualität/Sicherheit geworden sind |
| Führend | Entwicklerinnenerfahrungsumfrage-Werte | Ob der Golden Path wirklich hilft |
| Führend | Prozentsatz der als ADRs erfassten Entscheidungen | Ob die Schreib-/Lernkultur echt ist |
| Nachlaufend | Bereitstellungshäufigkeit (DORA) | Lieferdurchsatz |
| Nachlaufend | Durchlaufzeit für Änderungen (DORA) | Geschwindigkeit von Commit zu Produktion |
| Nachlaufend | Änderungsfehlschlagsrate (DORA) | Qualität des Lieferprozesses |
| Nachlaufend | Zeit, Dienst wiederherzustellen (DORA) | Operative Resilienz |
| Nachlaufend | Vorfallhäufigkeits- und Schweregradtrend | Zuverlässigkeitsverbesserung über Zeit |
| Nachlaufend | Auditbefunde / Kontrollfehlschläge | Compliance-Lage |
| Nachlaufend | Bindung und Fluktuation | Ob sich die Kultur verbessert |

Die vier DORA-Metriken sind die am validiertesten branchenübergreifenden Ergebnismaße
für Lieferung; behandeln Sie Verbesserung über alle vier gemeinsam als das
Hauptsignal, und schützen Sie sich davor, eines auf Kosten eines anderen zu
verbessern.

## Gängige Fehlschlagsmodi und wie sie zu vermeiden sind

| Fehlschlagsmodus | Wie es aussieht | Wie es zu vermeiden ist |
|---|---|---|
| **Big-Bang-Rollout** | Alles für alle auf einmal ändern; das Programm kollabiert unter seinem eigenen Gewicht. | Nach Schmerz und Bereitschaft sequenzieren; pilotieren, beweisen, dann skalieren. |
| **Mandat ohne Golden Path** | Richtlinie fordert den neuen Weg, aber der neue Weg ist langsamer; Teams erfüllen auf Papier und umgehen ihn. | Den einfacheren, besseren Pfad *zuerst* bauen; Übernahme aus Verdienst verdienen. |
| **Ein Framework cargo-kultieren** | SAFe, das Spotify-Modell, oder die Struktur einer anderen Organisation ohne deren Kontext kopieren. | Von Ihrem eigenen Schmerz und Prinzipien beginnen; anpassen, nicht verpflanzen. |
| **Aktivität statt Ergebnisse messen** | Abgeschlossenes Training und abgehakte Boxen feiern, während sich Lieferung und Zuverlässigkeit nicht bewegen. | Ergebnisse (DORA, Vorfälle, Nutzerinnenwert) von Anfang an instrumentieren. |
| **Werkzeug-erste Transformation** | Eine Plattform kaufen und erwarten, dass Kultur folgt. | Mit Praktiken und Golden Paths führen; Werkzeuge dienen ihnen, nicht umgekehrt. |
| **Sponsoring verlieren** | Die Executive-Championin geht oder engagiert sich nicht mehr; das Programm stockt. | Die Änderung in normaler Governance institutionalisieren; eine Koalition bauen, keinen einzelnen Fehlschlagspunkt. |
| **Vanity-Metriken und Tricksen** | Abdeckungs- oder Geschwindigkeitszahlen steigen, während Qualität fällt. | Metriken als Signale mit ausgleichenden Maßen nutzen; nie als alleinige Ziele. |
| **Den Ozean für Legacy kochen** | Versuchen, alles zu modernisieren, nichts liefern. | Nach Risiko und Wert ranken; die kritischen wenigen strangulieren, den Rest einfrieren. |
| **Transformationsmüdigkeit** | Endlose Änderung ohne sichtbaren Ertrag; Teams engagieren sich nicht mehr. | Frühe Gewinne liefern; nachhaltiges Tempo schützen; das Programm enden lassen und normale Arbeit werden lassen. |
| **Das Organigramm ignorieren** | Neue Architektur kämpft gegen die bestehende Teamstruktur. | Das inverse Conway-Manöver anwenden: Teams zur gewünschten Architektur formen. |

## Die kürzestmögliche Version

Falls Sie sich nichts anderes aus diesem Anhang merken:

1. Finden Sie den größten Schmerz und beheben Sie ihn mit einem willigen Team.
2. Verwandeln Sie diesen Fix in einen Golden Path, der wirklich einfacher als der
   alte Weg ist.
3. Messen Sie das Ergebnis, zeigen Sie den Gewinn, und nutzen Sie ihn, den nächsten
   Schritt zu finanzieren.
4. Wiederholen Sie, den Kreis erweiternd, bis der Golden Path einfach ist, wie Sie
   arbeiten.
5. Behalten Sie Sponsoring, messen Sie weiter, und nie Big Bang.

Siehe **Kapitel 12.4** für die Reifegradmodelle, die die Bewertungen verankern, und
**Kapitel 12.2** für die Launch-, Überprüfungs-, und Audit-Checklisten, die jeden
Schritt operationalisieren.
