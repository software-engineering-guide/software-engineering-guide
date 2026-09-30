# 11.1 Die Discovery-Pipeline

## Überblick und Motivation

Die Discovery-Pipeline ist der Arbeitsfluss, der entscheidet, **was zu bauen ist und warum**, und definiert, **wie Erfolg aussehen wird**, vor und neben Lieferung. Wo die Lieferpipeline (Kapitel 11.2) validierte Ideen in laufende Software verwandelt, verwandelt die Discovery-Pipeline Probleme, Beleg, und Strategie in einen priorisierten, testbaren Satz beabsichtigter Ergebnisse. In moderner Praxis laufen die zwei kontinuierlich und parallel, oft *Dual-Track*-Entwicklung genannt, statt als sequenzielle Phasen. Discovery speist weiter eine bereite Versorgung entrisikierter, gut gerahmter Arbeit an Lieferung, und Lieferung speist weiter Echtwelt-Ergebnisdaten zurück in Discovery.

Für große Teams ist eine schwache Discovery-Pipeline der teuerste Fehlschlagsmodus in Software. Ein Team mit exzellenter Lieferung und schlechter Discovery baut effizient das Falsche: es liefert schnell aus, trifft seine Geschwindigkeitsziele, und bewegt trotzdem keine Geschäftskennzahl. Die Kosten sind auf Engineering-Dashboards unsichtbar und enorm auf der Bilanz. Die Discovery-Pipeline ist, wie Sie diese Kosten sichtbar machen: sie zwingt Ziele, explizit, messbar, und falsifizierbar zu sein, bevor Sie große Investitionen verpflichten.

Unternehmens- und Behördenkontexte erhöhen die Einsätze. Unternehmen koordinieren Dutzende Teams gegen eine geteilte Strategie, fehlausgerichtete lokale Ziele verdichten sich also zu verschwendeten Portfolios. Behördenprogramme verpflichten mehrjährige öffentliche Finanzierung gegen gesetzliche Mandate, wo "wir bauten, was der Vertrag sagte" keine Verteidigung ist, falls das Ergebnis (bediente Bürgerinnen, reduzierte Wartezeiten, verhinderter Betrug) nie materialisiert. Eine disziplinierte Discovery-Pipeline, durch Objectives, Maße, und explizite Qualitätsanforderungen ausgedrückt, ist, wie beide ihre Absicht prüfbar halten.

## Kernprinzipien

- **Ergebnisse über Ausgaben.** Messen Sie die Änderung, die Sie für Nutzerinnen und das Geschäft schaffen, nicht die Features, die Sie ausliefern.
- **Machen Sie Absicht explizit und messbar.** Ein Ziel, das Sie nicht messen können, ist eine Meinung, die Sie nicht verwalten können.
- **Entrisikieren Sie, bevor Sie bauen.** Das günstigste Experiment schlägt die zuversichtlichste Meinung.
- **Discovery und Lieferung laufen kontinuierlich parallel**, nicht als sequenzielle Tore.
- **Qualitätseigenschaften sind Anforderungen, keine Nachgedanken.** Zuverlässigkeit, Sicherheit, und Barrierefreiheit werden entdeckt und spezifiziert, nicht erhofft.
- **Ausrichtung schlägt lokale Optimierung.** Verschachtelte Ziele verbinden Teamarbeit mit Strategie.
- **Schließen Sie die Schleife.** Gelieferte Ergebnisse sind Beleg, der wieder in Discovery eintritt.

## Empfehlungen

### Richtung mit OKRs rahmen

Nutzen Sie [Objectives and Key Results](https://en.wikipedia.org/wiki/OKR) (OKRs), um Strategie mit Teamausführung zu verbinden. Ein *Objective* ist eine qualitative, inspirierende Erklärung eines gewünschten Endzustands ("Erstmaliges Onboarding mühelos machen"). *Key Results* sind die kleine Anzahl (üblicherweise 2–4) messbarer Ergebnisse, die beweisen, dass das Objective erfüllt wird ("7-Tage-Aktivierung von 40% auf 60% erhöhen"; "Onboarding-Support-Tickets um 30% reduzieren"). Key Results drücken **Ergebnisse** aus, keine Aufgaben: "den neuen Assistenten ausliefern" ist eine als Ergebnis verkleidete Aufgabe.

Kaskadieren Sie OKRs durch *Ausrichtung*, nicht Diktat: Führung setzt eine kleine Anzahl Unternehmens-Objectives; Teams schlagen Key Results und ihre eigenen Objectives vor, die zu ihnen hochführen. Setzen Sie sie in regelmäßiger Kadenz (üblicherweise vierteljährlich mit einem Jahresrahmen), überprüfen Sie sie mitten im Zyklus, und benoten Sie sie am Ende ehrlich. Halten Sie sie getrennt von Leistungsüberprüfungen: für Vergütung benotete OKRs werden schnell sandgebaggt. Siehe Kapitel 10.1, wie OKRs sich mit Portfolio- und Programmmanagement verbinden.

### Gesundheit mit KPIs überwachen

Unterscheiden Sie [Key Performance Indicators](https://en.wikipedia.org/wiki/Performance_indicator) (KPIs) von OKRs. OKRs beschreiben die *Änderung*, die Sie diese Periode wollen; KPIs beschreiben die *laufende Gesundheit*, die Sie aufrechterhalten müssen, unabhängig davon, was Sie ändern (Uptime, Konversionsrate, Kosten pro Transaktion, Kundinnenzufriedenheit). Eine Kennzahl kann beides sein (ein KPI, den Sie aktiv zu bewegen versuchen, wird ein Key Result), aber die meisten KPIs sind Leitplanken, die Sie überwachen, keine Ziele, denen Sie hinterhersprinten.

Klassifizieren Sie jede wichtige Kennzahl als **führend** (prädiktiv und jetzt handlungsfähig, wie Testversionsanmeldungen) oder **nachlaufend** (bestätigend und langsam, wie Jahresumsatz). Discovery stützt sich auf führende Indikatoren, um zu steuern, bevor nachlaufende Indikatoren bestätigen. Hüten Sie sich vor Vanity-Kennzahlen, die verlässlich steigen, aber nichts vorhersagen (rohe Seitenaufrufe, Gesamtzahl registrierter Nutzerinnen); bevorzugen Sie Verhältnis- und Kohortenkennzahlen, die Tricksen widerstehen. Siehe Kapitel 7.3 und 7.4 für die Analytik- und Experimentiermaschinerie hinter diesen Maßen.

### Systemqualitätseigenschaften explizit spezifizieren

Funktionale Anforderungen sagen, was das System tut. **Systemqualitätseigenschaften** (die "-keiten": Zuverlässigkeit, Leistung, Skalierbarkeit, Sicherheit, Barrierefreiheit, Pflegbarkeit, Betreibbarkeit) sagen, wie gut es es tun muss. Diese werden routinemäßig unterentdeckt: jeder nimmt sie an, niemand spezifiziert sie, und sie tauchen als Produktionsvorfälle auf. Behandeln Sie sie als erstklassige Discovery-Ausgabe. Identifizieren Sie die **architektonisch bedeutsamen Anforderungen** (die Qualitätsforderungen, die die Architektur wesentlich formen) für jede Initiative. Quantifizieren Sie sie ("p99-Latenz unter 200 ms bei 10-facher aktueller Last"; "WCAG (Web Content Accessibility Guidelines) 2.2 AA"; "Wiederherstellungszeitziel von 15 Minuten"). Und wo Sie können, kodieren Sie sie als automatisierte **Fitnessfunktionen** (ausführbare Checks, die kontinuierlich eine Qualitätseigenschaft verifizieren), die die Lieferpipeline prüfen kann. Das ist das Discovery-seitige Gegenstück zu Kapitel 3.1 (Architekturgrundlagen) und Kapitel 3.5 (Skalierbarkeit, Leistung, Resilienz).

### Jedes Ziel SMART machen

Ob Sie ein Key Result, ein Abnahmekriterium, oder ein Qualitätsziel schreiben, wenden Sie den [SMART](https://en.wikipedia.org/wiki/SMART_criteria)-Test an:

- **Spezifisch:** benennt ein klares, unzweideutiges Ergebnis.
- **Messbar:** hat eine Kennzahl und eine Wahrheitsquelle.
- **Erreichbar:** ist realistisch angesichts Einschränkungen und Beleg.
- **Relevant:** führt zu einem höheren Objective und Nutzerinnenwert hoch.
- **Terminiert:** hat eine Frist oder ein Überprüfungsdatum.

"Leistung verbessern" scheitert an jedem Buchstaben. "Mediane Checkout-Zeit von 8s auf 3s für mobile Nutzerinnen bis Ende Q3 reduzieren, gemessen durch Real-User-Monitoring" besteht alle fünf. SMART-Kriterien verwandeln vage Ambition in eine falsifizierbare Behauptung, die Discovery testen und Lieferung verifizieren kann.

### Kontinuierliche, evidenzgetriebene Discovery durchführen

Strukturieren Sie Discovery als wiederholbare Pipeline, keine einmalige Phase:

1. **Wahrnehmen.** Sammeln Sie Signale: Nutzerinnenforschung, Supportdaten, Analytik, Markt- und Compliance-Eingaben.
2. **Rahmen.** Kartieren Sie Opportunitäten (ein *Opportunity-Solution-Tree* verbindet ein gewünschtes Ergebnis mit den Nutzerinnenbedürfnissen und Kandidatenlösungen, die es bewegen könnten).
3. **Hypothese bilden.** Erklären Sie Annahmen als falsifizierbare Behauptungen: "Wir glauben, [Änderung] wird [Ergebnis] für [Segment] verursachen, und wir wissen es, falls sich [Maß] bewegt."
4. **Experimentieren.** Validieren Sie die riskantesten Annahmen mit dem günstigsten Test: Interviews, Prototypen, Fake-Door-Tests (ein noch nicht gebautes Feature bewerben, um echte Nachfrage zu messen), [A/B-Experimente](https://en.wikipedia.org/wiki/A/B_testing) (randomisierte Vergleiche zweier Varianten, Kapitel 7.4).
5. **Entscheiden.** Fortsetzen, schwenken, oder fallenlassen, und die Überlebenden mit ihren angehängten SMART-Erfolgskriterien in den Lieferungsrückstand speisen.

Die Ausgabe der Discovery-Pipeline ist keine Feature-Liste; es ist ein Strom *validierter, messbarer Wetten*, bereit für Lieferung.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| **Ergebnisbasierte Ziele (OKRs)** | Richtet Teams auf Wirkung aus; ermächtigt Autonomie im *Wie* | Schwer gut zu schreiben; verlockend mit Aufgaben nachzufüllen; verrauschte Zuschreibung |
| **Ausgabe-/Feature-Roadmaps** | Vorhersagbar, leicht zu kommunizieren und vertraglich zu fassen | Belohnt Ausliefern über Wirkung; versteckt falsches-Ding-Risiko |
| **Schwere Vorab-Discovery** | Reduziert Bauverschwendung; starke Anforderungen | Verlangsamt Start; Analyse-Lähmungsrisiko; Annahmen immer noch ungetestet |
| **Kontinuierliche Dual-Track-Discovery** | Entrisikiert kontinuierlich; schnelles Feedback | Fordert Forschungskapazität und Disziplin; schwerer zu planen |
| **Explizite Qualitätseigenschaften als SMART-Ziele** | Verhindert "-keiten"-Überraschungen; prüfbar | Aufwand zu quantifizieren; kann frühe Exploration überbeschränken |

Die zentrale Spannung ist **Verpflichtung vs. Lernen**. Unternehmen, und besonders Behörden, brauchen oft feste Verpflichtungen für Budgetierung und Verträge, was zu Ausgabe-Roadmaps zieht. Gute Ergebnisse brauchen Raum zu lernen, was zu OKRs und Experimenten zieht. Lösen Sie das so: verpflichten Sie sich fest zu *Problemen und Ergebnissen*, und halten Sie *Lösungen* locker.

## Fragen zur Diskussion mit Ihrem Team

1. **Wer in Ihrem Team besitzt tatsächlich Discovery, und haben sie die Kapazität, sie kontinuierlich statt in einem Einmal-Sprint durchzuführen?** Dual-Track-Entwicklung funktioniert nur, wenn jemand den Discovery-Track jede Woche offen hält statt nur zu Quartalsbeginn. In einer großen Organisation hat Discovery oft keine dedizierte Besitzerin, sie kollabiert also zu wer auch immer übrige Zeit hat, was niemand ist, und das Team fällt standardmäßig aufs Bauen zurück. Bringen Sie Beleg: zählen Sie, wie viele Ihrer letzten zehn Features durch eine dokumentierte Hypothese und einen günstigen Test vor dem Bau gingen, versus direkt in den Rückstand. In Unternehmens- und Behördenumgebungen, wo eine fehlausgerichtete Initiative mehrere Teamquartale verschwenden kann, benennen Sie eine Produktbesitzerin oder ein Trio (Produkt, Design, Engineering), rechenschaftspflichtig für die Wahrnehmen-Rahmen-Hypothese-Experiment-Entscheiden-Schleife. Wenn niemand sie besitzt, besetzen Sie sie, bevor Sie über irgendetwas anderes streiten.

2. **Welche Ihrer aktuellen Initiativen haben architektonisch bedeutsame Anforderungen, die Sie nie quantifiziert haben, und könnten Sie welche als Fitnessfunktionen kodieren?** Die "-keiten" (Zuverlässigkeit, Leistung, Sicherheit, Barrierefreiheit) werden angenommen und tauchen dann als Produktionsvorfälle auf. Gehen Sie jede aktive Initiative durch, fragen Sie, welche Qualitätseigenschaften die Architektur wesentlich formen, und prüfen Sie, ob jede eine Zahl und eine Wahrheitsquelle hat: "p99 unter 200 ms bei 10-facher Last," "WCAG 2.2 AA," "Wiederherstellungszeitziel von 15 Minuten." Für Unternehmen und Behörden erschaffen nicht quantifizierte Barrierefreiheits- oder Sicherheitsanforderungen direkte rechtliche und Prüfungsexposition. Das Signal, das zu bringen ist, sind Ihre letzten drei Vorfälle: wie viele wurden auf eine Qualitätseigenschaft zurückverfolgt, die niemand spezifizierte? Wo Sie ein Ziel in eine automatisierte Fitnessfunktion verwandeln können, die die Lieferpipeline prüft, tun Sie es, denn ein spezifiziertes, aber nicht durchgesetztes Ziel driftet.

3. **Als Sie sich zuletzt zu einer Lösung verpflichteten, testeten Sie zuerst die riskanteste Annahme, oder die leichteste?** Teams validieren verlässlich die Annahme, mit der sie am bequemsten sind, und überspringen jene, die die Idee tatsächlich töten würde. Listen Sie für jede Initiative ihre Annahmen (Erwünschtheit, Lebensfähigkeit, Machbarkeit) und rangieren Sie sie nach "wie tot ist diese Idee, falls wir hier falsch liegen," dann zielen Sie den günstigsten Test auf die Spitze dieser Liste. Das zählt im Maßstab, weil ein zuversichtliches, leitendes Team ein Quartal Engineering an einen ungetesteten Glauben verpflichten kann, und die Kosten bleiben bis zur Einführung unsichtbar. Bringen Sie das Artefakt: Ihre letzte Hypothese, erklärt als "Wir glauben, [Änderung] verursacht [Ergebnis] für [Segment], gemessen durch [Kennzahl]," und fragen Sie, ob Sie es testeten oder nur bauten. Wenn Sie die riskanteste Annahme nicht benennen können, sind Sie nicht bereit, Baukapazität zu verpflichten.

4. **Wie viele Ihrer Key Results sind echte Ergebnisse, und wie viele sind Aufgaben oder Einführungsdaten, in Ergebniskleidung?** Der einzige häufigste Fehlschlag in ergebnisbasierter Planung ist, Key Results mit der bereits geplanten Arbeit nachzufüllen ("den neuen Assistenten einführen") statt der Änderung, die diese Arbeit verursachen soll ("7-Tage-Aktivierung von 40% auf 60% erhöhen"). Im Maßstab besiegt das still den ganzen Punkt: Dutzende Teams berichten grün, während keine Geschäftskennzahl sich bewegt, weil sich jeder selbst am Ausliefern benotete. Der konkurrierende Zug ist echt, Ausgabe-Roadmaps sind leichter zu kommunizieren, vertraglich zu fassen, und zu prognostizieren, genau deshalb schleichen sie sich zurück. Bringen Sie Ihren aktuellen OKR-Satz und markieren Sie jedes Key Result als Ergebnis oder Ausgabe, dann prüfen Sie, ob OKR-Benotung mit Vergütung verwoben ist, denn an Bezahlung gebundene Ergebnisse werden schnell sandgebaggt. Für Unternehmens- und Behördenportfolios, wo Finanzierung gegen erklärte Ziele verpflichtet ist, ist eine Roadmap aus Ausgaben ohne Ergebnismaß ein Prüfungsbefund, der darauf wartet zu passieren; bestehen Sie darauf, dass sich jede Initiative fest zu einem Problem und einem messbaren Ergebnis verpflichtet, während sie die Lösung locker hält.

5. **Welche Ihrer KPIs würden weiter steigen, selbst wenn das Produkt schlechter würde, und welche Leitplanken schützen die Kennzahlen, die Sie aktiv zu bewegen versuchen?** Jede Kennzahl, die Sie zu einem Ziel erheben, lädt [Goodharts Gesetz](https://en.wikipedia.org/wiki/Goodhart%27s_law) ein: sobald ein Maß zum Ziel wird, optimieren Menschen das Maß statt das Ding, das es repräsentieren sollte. Vanity-Kennzahlen (rohe Seitenaufrufe, kumulative registrierte Nutzerinnen) steigen verlässlich und sagen nichts vorher, während ein einzelnes ohne Leitplanken gejagtes Key Result erfüllt werden kann, indem etwas degradiert wird, das Sie nie benannten. Die Spannung ist, dass führende Indikatoren Sie früh steuern lassen, aber verrauscht und trickbar sind, während nachlaufende Indikatoren vertrauenswürdig sind, aber zu spät bestätigen, um zu handeln. Bringen Sie Ihr Kennzahleninventar, als führend oder nachlaufend und als Ziel oder Leitplanke klassifiziert, und stresstesten Sie jedes Ziel, indem Sie fragen "wie könnte ein cleveres Team diese Zahl treffen, während es das Produkt schlechter macht." In regulierten und öffentlichen Umgebungen, veröffentlichen Sie die Leitplanken neben den Zielen, denn ein Aufsichtsgremium, das nur die Schlagzeilenkennzahl sieht, kann echten öffentlichen Wert nicht von einer getrickten Zahl unterscheiden.

6. **Wenn Lieferung etwas ausliefert, wie tritt das Echtwelt-Ergebnis tatsächlich wieder in Discovery ein, oder bleibt die Schleife offen?** Dual-Track-Entwicklung verdichtet sich nur, wenn gelieferte Ergebnisse als Beleg für die nächste Runde zurückfließen; wenn die Schleife offen bleibt, liefern Teams aus, feiern, und lernen nie, ob sich die Wette auszahlte, dieselben ungetesteten Annahmen wiederholen sich also. In einer großen Organisation ist der Feedback-Pfad, wo Verantwortung am wahrscheinlichsten durch eine Lücke fällt: Lieferung besitzt die Veröffentlichung, Analytik besitzt das Dashboard, und niemand besitzt den Vergleich des versprochenen Key Results mit dem beobachteten. Bringen Sie Ihre letzten zehn ausgelieferten Initiativen und fragen Sie für jede, ob irgendjemand die Ergebniskennzahl gegen das ursprüngliche SMART-Ziel prüfte und ob diese Prüfung eine nachfolgende Entscheidung änderte. Für Unternehmens- und Behördenprogramme, die mehrjährige Finanzierung verpflichten, benennen Sie die Kadenz und die Besitzerin, Features zu pensionieren oder neu abzugrenzen, die ihre Kennzahl nicht bewegten, denn ein ausgeliefertes Feature, das niemand überdenkt, wird zu permanenten Kosten ohne rechenschaftspflichtige Überprüfung.

## Branchenperspektive

**Startup.** Mit einem winzigen Team und wenig Landebahn ist Ihre Discovery-Pipeline absichtlich leichtgewichtig, aber nie übersprungen: ein Tag Kundinneninterviews und ein Fake-Door-Test kosten fast nichts gegen die Wochen, die ein falscher Bau verbrennt. Wählen Sie einen führenden Indikator, der für Ihren Kernwert steht, erklären Sie jede Wette als einzelne falsifizierbare Hypothese, und töten Sie Ideen, bevor Sie Code schreiben, statt danach. Formale OKRs sind Overkill bei fünf Menschen; ein ehrliches messbares Ergebnis pro Zyklus reicht, um Geschwindigkeit davon abzuhalten, Bewegung ohne Fortschritt zu werden.

**Kleinunternehmen.** Sie haben wahrscheinlich keine dedizierte Forscherin oder Produktanalystin, behandeln Sie Discovery also als Gewohnheit, keine Rolle: ein paar strukturierte Gespräche mit echten Kundinnen und eine einfache Kennzahl, die Sie bereits sammeln. Die Bauen-versus-Kaufen-Frage dominiert, denn die meisten Qualitätseigenschaften (Zuverlässigkeit, Sicherheit, Barrierefreiheit) sind günstiger von einer angesehenen Anbieterin zu bekommen, als selbst zu spezifizieren und durchzusetzen. Schreiben Sie ein oder zwei SMART-Ziele, damit Sie sagen können, ob ein gekauftes Werkzeug oder ein kleiner Bau das Ergebnis tatsächlich bewegte, und vermeiden Sie, knappes Budget an Features zu verpflichten, die niemand als gewollt validierte.

**Großunternehmen.** Maßstab verwandelt Discovery in ein Koordinationsproblem über Dutzende Teams: ohne eine geteilte OKR-Kadenz und eine gemeinsame Definition von "Ergebnis" driften und duplizieren sich lokale Ziele, und fehlausgerichtete Wetten verdichten sich zu verschwendeten Portfolios. Standardisieren Sie, wie architektonisch bedeutsame Anforderungen quantifiziert werden, und kodieren Sie sie als Fitnessfunktionen, damit Qualitätseigenschaften gesteuert statt angenommen werden. Verwalten Sie Discovery als Portfolio mit expliziten Kill-Kriterien und einer Schleife, die gelieferte Ergebniskennzahlen zurück in den nächsten Zyklus speist, damit Führung auf Wirkung statt auf einen Feature-Rückstand steuert.

**Behörde.** Beschaffung und mehrjährige Finanzierung fordern feste Verpflichtungen, was hart zu Ausgabe-Verträgen zieht, doch öffentlicher Wert lebt in Ergebnissen: bediente Bürgerinnen, gekürzte Wartezeiten, reduzierte Last. Rahmen Sie Programme um messbare öffentliche Ergebnisse und nicht verhandelbare Qualitätseigenschaften (WCAG-Barrierefreiheit, klare Sprache, Sicherheit), und machen Sie Discovery-Beleg, einschließlich Usability-Testen mit Assistive-Technologie-Nutzerinnen, zu Teil der Aufzeichnung, die Aufsichtsgremien prüfen können. Definieren Sie Erfolg als Steuerzahlerinnen- oder Bürgerinnenergebnisse statt gelieferte Module, damit "wir bauten, was der Vertrag sagte" nie ein Ergebnis ersetzen kann, das nie materialisierte.

## Beispiele

**Startup.** Ein vierköpfiges Team in der Seed-Phase, das eine Planungsapp für Friseursalons baut, ist versucht, ein Online-Buchungs-Widget zu bauen, weil ein paar laute Nutzerinnen danach fragten. Stattdessen führen sie eine Woche Discovery durch: fünf Besitzerinneninterviews, einen Fake-Door-"Online buchen"-Knopf auf der Marketingseite, und einen einzelnen führenden Indikator (Prozentsatz der Termine, die in Nichterscheinen enden). Die Interviews und Klickdaten enthüllen, dass Nichterscheinen, nicht Buchung, der echte Schmerz ist, sie schreiben also ein SMART-Key-Result (Nichterscheinen von 22% auf unter 10% für Pilotsalons dieses Quartal senken) und liefern zuerst ein kleines Anzahlungs-und-Erinnerungs-Feature, das Buchungs-Widget tötend, bevor eine Zeile davon geschrieben wird.

**Großunternehmen.** Die Zahlungsgruppe einer Einzelhandelsbank ersetzt eine Feature-Zähl-Roadmap durch drei vierteljährliche OKRs, eines "alltägliche Zahlungen fühlen sich sofort an" mit Key Results für p95-Überweisungsbestätigungszeit, Erst-Versuch-Erfolgsrate, und zahlungsbezogene Support-Kontakte. Systemqualitätseigenschaften sind im Voraus spezifiziert (99,99% Verfügbarkeit, Unter-Sekunde-Bestätigung, minimierter PCI-DSS-(Payment-Card-Industry-Data-Security-Standard)-Umfang) und als Fitnessfunktionen in Lieferung verdrahtet. Discovery führt wöchentliche Kundinneninterviews und Fake-Door-Tests durch, bevor Engineering verpflichtet wird. Zwei Kandidatenfeatures werden in Discovery getötet, weil sie die führenden Indikatoren nicht bewegen (geschätzte zwei Quartale Bauaufwand sparend), während ein kleinerer, unglamouröser Latenzfix das Key Result am meisten bewegt.

**Behörde.** Eine nationale Steuerbehörde, die Online-Einreichung modernisiert, setzt ein Programmziel "die Last des Einreichens für gewöhnliche Steuerzahlerinnen reduzieren," mit SMART-Key-Results: mediane Zeit-bis-Einreichung von 45 auf 20 Minuten kürzen, erfolgreichen Self-Service-Abschluss von 60% auf 85% erhöhen, und WCAG-2.2-AA- und Klare-Sprache-Standards als nicht verhandelbare Qualitätseigenschaften erfüllen. KPIs (Uptime während Einreichungssaison, Callcenter-Volumen) werden als Leitplanken überwacht. Discovery nutzt moderiertes Usability-Testen mit echten Steuerzahlerinnen, einschließlich Assistive-Technologie-Nutzerinnen, vor jeder Veröffentlichung. Weil Erfolg als Steuerzahlerinnenergebnisse statt gelieferte Module definiert ist, kann das Programm Aufsichtsgremien messbaren öffentlichen Wert zeigen, nicht nur Ausgabe.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Rendite auf eine Discovery-Pipeline wird von **vermiedener Verschwendung** dominiert. Branchenerfahrung, in kontrollierte-Experiment-Programmen bei großen Technologiefirmen widergehallt, findet wiederholt, dass ein großer Anteil gebauter Features, oft um die Hälfte oder mehr zitiert, keine messbare Verbesserung produzieren oder die Zielkennzahl aktiv schädigen. Angenommen, selbst ein Viertel der Baukapazität eines Teams geht zu Ideen, die Discovery günstig getötet hätte. Die Pipeline zahlt sich dann vielfach aus: eine Woche Nutzerinnenforschung und ein Fake-Door-Test kosten fast nichts gegen ein Quartal Engineering, plus die laufende Pflegelast eines ungenutzten Features.

Die [Gesamtbetriebskosten](https://en.wikipedia.org/wiki/Total_cost_of_ownership)-(TCO)-Rahmung zählt, weil unvalidierte Features nach Einführung nicht kostenlos sind. Jedes ausgelieferte Feature trägt ewige Kosten: Pflege, Testen, Sicherheitsoberfläche, Unterstützung, und kognitive Last (Kapitel 10.4). Eine schlechte Idee in Discovery zu töten vermeidet nicht nur die Baukosten, sondern den gesamten Besitzschwanz. Explizite Qualitätseigenschaften folgen derselben Logik: Zuverlässigkeit und Barrierefreiheit im Voraus als SMART-Ziele zu spezifizieren ist weit günstiger als sie nach einem Ausfall, Verstoß, oder Rechtsstreit nachzurüsten.

Um den Fall gegenüber Führung zu machen, verschieben Sie das Gespräch von "wie viel liefern wir aus" zu "wie stark bewegen wir die Kennzahlen, die zählen," und zeigen Sie ein paar konkrete Beispiele teurer Features, die nichts bewegten. Die Übernahmekosten sind bescheiden (Forschungskapazität, eine OKR-Kadenz, und die Disziplin, SMART-Kriterien zu schreiben), und das primäre Risiko, es *nicht* zu übernehmen, ist still, ungezählt, und sich verdichtend.

## Anti-Muster und Fallstricke

- **Roadmaps aus Features, als Strategie verkleidet:** Ausgabelisten ohne erklärtes Ergebnis oder Maß.
- **Key Results, die Aufgaben sind:** "X einführen" statt "Y um Z verbessern."
- **OKR-Theater:** Ziele geschrieben, abgelegt, und nie überprüft oder benotet.
- **Sandgebaggte oder heldenhafte OKRs:** Ziele gesetzt, um 100% zu garantieren (nichts gelernt) oder Fantasie-Stretch ohne Plan.
- **Unspezifizierte Qualitätseigenschaften:** Zuverlässigkeit, Sicherheit, und Barrierefreiheit angenommen statt quantifiziert, dann in Produktion entdeckt.
- **Vanity-Kennzahlen:** Maße, die immer steigen und nichts vorhersagen.
- **Discovery als einmalige Phase:** ein "Discovery-Sprint" im Voraus, dann keine fortgesetzte Validierung.
- **Die Lösung bauen, bevor die Annahme getestet wird:** das günstigste Experiment überspringen, weil das Team zuversichtlich ist.
- **Kennzahlenfixierung und [Goodharts Gesetz](https://en.wikipedia.org/wiki/Goodhart%27s_law):** sobald ein Maß zum Ziel wird, hört es auf, ein gutes Maß zu sein; balancieren Sie mit Leitplanken-KPIs.

## Reifegradmodell

- **Stufe 1, Beginnen:** Arbeit wird als Features auf einer Roadmap definiert und Erfolg ist "wir haben es ausgeliefert." Es gibt keine expliziten Ergebnismaße oder Qualitätsziele; Discovery geschieht zufällig, falls überhaupt, und Entscheidungen werden von der lautesten Meinung getrieben.
- **Stufe 2, Entwickeln:** OKRs und KPIs existieren für manche Teams, aber nicht andere; Ziele werden erklärt, sind aber oft ausgabenförmig geformt; Qualitätseigenschaften sind benannt, aber nicht quantifiziert. Ein Team führt vielleicht einen einmaligen "Discovery-Sprint" durch, hört dann auf zu validieren, sobald der Bau beginnt, Praxis ist also echt, aber inkonsistent über die Organisation.
- **Stufe 3, Standardisieren:** Eine konsistente, an Strategie ausgerichtete OKR-Kadenz, SMART-Key-Results, und spezifizierte, testbare Qualitätseigenschaften sind organisationsweit dokumentiert und erwartet. Discovery ist eine anerkannte, besetzte Aktivität mit Hypothesen und Experimenten, und architektonisch bedeutsame Anforderungen werden für jede Initiative identifiziert statt angenommen.
- **Stufe 4, Steuern:** Das Portfolio wird gegen Baselines gemessen. Führende und nachlaufende Indikatoren, Discovery-Trefferquote, und das Ergebnis, das jede ausgelieferte Wette tatsächlich bewegte, werden gegen ihr SMART-Ziel verfolgt; Hypothesen werden auf Beleg benotet und Kill-Kriterien werden durchgesetzt; Fitnessfunktionen berichten Qualitätseigenschaft-Konformität kontinuierlich, sodass Drift von einem spezifizierten Zuverlässigkeits-, Leistungs-, oder Barrierefreiheitsziel mit Daten statt in einem Vorfall gefangen wird.
- **Stufe 5, Orchestrieren:** Kontinuierliche Dual-Track-Discovery ist mit Portfolio-, Risiko-, und Budgetierungsplanung integriert; validierte Wetten fließen stetig zu Lieferung und Ergebniskennzahlen schleifen automatisch zurück, um die nächste Runde zu steuern. Führende Indikatoren steuern Investition, und die Organisation pensioniert, grenzt neu ab, und balanciert Initiativen routinemäßig auf Beleg, die Pipeline selbst anpassend, während sich Markt und Kennzahlen verschieben.

## Diskussionsideen

1. Schauen Sie sich Ihre aktuelle Roadmap an: wie viele Punkte erklären ein messbares Ergebnis versus nur ein auszulieferndes Feature?
2. Welche Key Results Ihres Teams sind tatsächlich verkleidete Aufgaben, und wie würden Sie sie umschreiben?
3. Welche Systemqualitätseigenschaften, von denen Ihr Produkt abhängt, wurden nie explizit quantifiziert?
4. Was ist das günstigste Experiment, das Ihr letztes gescheitertes Feature hätte töten können, bevor Sie es bauten?
5. Wie lösen Sie die Spannung zwischen den festen Verpflichtungen, die Budgetierung/Beschaffung fordert, und dem Lernen, das gute Ergebnisse fordern?
6. Welche Ihrer KPIs würden weiter steigen, selbst wenn das Produkt schlechter würde?

## Wichtigste Erkenntnisse

- Die Discovery-Pipeline entscheidet *was* und *warum*, und definiert Erfolg, **bevor** Lieferung Ressourcen verpflichtet.
- Nutzen Sie **OKRs** für die Änderung, die Sie wollen, **KPIs** für die Gesundheit, die Sie aufrechterhalten, und klassifizieren Sie Kennzahlen als führend oder nachlaufend.
- Behandeln Sie **Systemqualitätseigenschaften** als explizite, quantifizierte, testbare Anforderungen, keine Annahmen.
- Machen Sie jedes Ziel, Key Result, und Abnahmekriterium **SMART**.
- Führen Sie Discovery **kontinuierlich und parallel** mit Lieferung durch; validieren Sie die riskantesten Annahmen günstig.
- Der dominante ROI ist **vermiedene Verschwendung**: sowohl Baukosten als auch die ewigen TCO ungenutzter Features.
- Schließen Sie die Schleife: gelieferte **Ergebniskennzahlen** (Kapitel 11.2) sind der primäre Beleg für die nächste Discovery-Runde.

## Referenzen und weiterführende Literatur

- *Measure What Matters*, von John Doerr (über OKRs).
- *Radical Focus*, von Christina Wodtke (über OKRs in der Praxis).
- *Continuous Discovery Habits*, von Teresa Torres (Opportunity-Solution-Trees, Dual-Track-Discovery).
- *Inspired* und *Empowered*, von Marty Cagan (Produkt-Discovery und Ergebnisteams).
- *Lean Analytics*, von Alistair Croll und Benjamin Yoskovitz (führende Indikatoren, Vanity-Kennzahlen).
- *The Lean Startup*, von Eric Ries (Build-Measure-Learn, validiertes Lernen).
- *Escaping the Build Trap*, von Melissa Perri (Ergebnisse über Ausgaben).
- *Outcomes Over Output*, von Joshua Seiden.
- *Software Architecture in Practice*, von Bass, Clements, Kazman (Qualitätseigenschaften).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): Ursprung der SMART-Kriterien.
