# 10.8 Reifegradmodelle

## Überblick und Motivation

Ein [Reifegradmodell](https://en.wikipedia.org/wiki/Maturity_model) ist ein strukturierter Weg zu bewerten, wie fähig und konsistent Ihre Praxis in einer Domäne ist, und einen Pfad zu beschreiben, sie zu verbessern. Es definiert eine kleine Leiter von Stufen. Am Boden ist Arbeit Ad-hoc und reaktiv. Oben ist sie gemessen, gesteuert, und kontinuierlich optimierend. Jede Sprosse hat beobachtbare Eigenschaften, gegen die Sie prüfen können.

Reifegradmodelle verwandeln eine vage Frage ("sind wir gut darin?") in eine wiederholbare Antwort ("wir sind hier auf Stufe 2, dort auf Stufe 4, und das ist, was Stufe 3 fordern würde"). Dieses Buch nutzt ein Fünf-Stufen-Modell in jedem Kapitel und konsolidiert sie in Kapitel 12.4. Dieses Kapitel handelt von der Disziplin selbst: wie die Modelle funktionieren, wann sie helfen, und wie sie in die Irre führen.

Der Grund, warum sie zählen, ist einfach. Große Organisationen können nicht verbessern, was sie nicht sehen können. Über Dutzende Teams variiert Fähigkeit enorm und unsichtbar. Manche Teams haben exzellentes Testen und schwache Sicherheit; andere haben das Umgekehrte. Ein Reifegradmodell gibt Ihnen ein geteiltes Vokabular und einen gemeinsamen Maßstab, damit Lücken vergleichbar werden, Investition priorisiert werden kann, und Fortschritt über Zeit verfolgt statt nur behauptet werden kann. Bekannte Beispiele umfassen CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), für Prozess), das DORA- ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) Modell (Software-Lieferleistung), OWASP SAMM (Software Assurance Maturity Model) und BSIMM (Building Security In Maturity Model) für Software-Sicherheit, TMMi (Test Maturity Model integration, für Testen), das Agile-Fluency-Modell, und Datenmanagement-Reifegradmodelle, plus zahllose interne Scorecards.

Für Unternehmen und besonders Behörden tragen Reifegradmodelle besonderes Gewicht. Behördenvertragsvergabe nutzt seit Langem CMMI-Bewertungsstufen als Lieferantinnenqualifikation, und Frameworks wie das US CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) binden Cybersicherheitsreife direkt an Berechtigung für Verteidigungsarbeit. Das gibt Reifegradmodellen echte Zähne. Es erschafft auch das zentrale Risiko dieses Kapitels: wenn eine Stufe zu einem Tor oder Ziel wird, optimieren Menschen für die Bewertung statt die zugrunde liegende Fähigkeit. Gut genutzt, sind Reifegradmodelle ein Spiegel. Schlecht genutzt, sind sie Theater.

## Kernprinzipien

- **Reife ist ein Mittel, kein Zweck.** Das Ziel ist Fähigkeit und Ergebnisse, keine Stufenzahl.
- **Bewerten Sie, um zu lernen, nicht um zu punkten.** Ehrliche Selbsteinschätzung schlägt eine schmeichelnde Bewertung.
- **Höher ist nicht immer besser.** Das richtige Ziel hängt von Risiko, Kontext, und Kosten ab.
- **Messen Sie pro Domäne, nicht eine globale Note.** Fähigkeit ist ungleichmäßig; eine einzelne Zahl versteckt das.
- **Priorisieren Sie zuerst die Lücken mit niedrigster Reife und höchstem Risiko.**
- **Hüten Sie sich vor [Goodharts Gesetz](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Sobald eine Stufe ein Ziel ist, hört sie auf, Fähigkeit zu messen.
- **Bewerten Sie periodisch neu.** Reife driftet, während sich Menschen, Systeme, und Bedrohungen ändern.

## Empfehlungen

### Das richtige Modell für die Domäne wählen

Passen Sie das Modell an die Fähigkeit an, die Sie verbessern wollen, und bevorzugen Sie etablierte, evidenzbasierte Modelle über erfundene, wo sie existieren:

- **Prozess und Lieferung:** CMMI (breite Prozessreife), das DORA-Fähigkeitsmodell (Lieferleistung, in Forschung verankert, Kapitel 11.2).
- **Sicherheit:** OWASP SAMM und BSIMM (Software-Sicherheitspraktiken), CMMC (Verteidigungs-Cybersicherheit).
- **Testen und Qualität:** TMMi.
- **Agile und Arbeitsweisen:** das Agile-Fluency-Modell (Kapitel 10.7).
- **Daten:** Datenmanagement-Reifegradmodelle (DMM, DCAM).

Für internen Gebrauch ist eine einfache Vier- oder Fünf-Stufen-Skala, pro Fähigkeit angewendet (wie dieses Buch es tut), oft handlungsfähiger als ein schwergewichtiges externes Framework. Reservieren Sie formale, bewertete Modelle für dort, wo sie vertraglich gefordert sind.

### Ehrlich und pro Fähigkeit bewerten

Führen Sie Bewertungen durch, die Wahrheit statt Komfort produzieren. Beziehen Sie die Menschen ein, die die Arbeit tun. Sammeln Sie Beleg statt Meinungen. Bewerten Sie jede Fähigkeit separat, damit das Bild Realität widerspiegelt: stark hier, schwach dort. Eine Selbsteinschätzung, genutzt, um Verbesserung zu leiten, ist mehr wert als eine externe Bewertung, genutzt, um ein Abzeichen zu verdienen, denn die erste belohnt Offenheit und die zweite belohnt Präsentation. Kapitel 12.4 bietet eine konsolidierte Selbsteinschätzung über jede Domäne in diesem Buch; nutzen Sie es als Startinstrument.

### Reife nutzen, um zu priorisieren, nicht zu bestrafen

Die Ausgabe einer Bewertung ist ein priorisierter Verbesserungsrückstand, kein Zeugnis für Schuldzuweisung. Kombinieren Sie Reife mit Risiko. Eine Stufe-1-Fähigkeit in einem Niedrigrisikobereich mag okay sein. Eine Stufe-2-Fähigkeit in einem sicherheits- oder compliance-kritischen Bereich ist dringend. Lenken Sie Investition zu den Lücken, wo niedrige Reife auf hohes Risiko trifft, und binden Sie die Arbeit an Ergebnisse (Kapitel 11.1), damit Verbesserung an Resultaten gemessen wird, nicht am Aufsteigen der Leiter um ihrer selbst willen.

### Zielstufen absichtlich setzen: höher ist nicht kostenlos

Jede Stufe nach oben kostet Aufwand und fügt oft Prozessgewicht hinzu. Das richtige Ziel ist selten "Stufe 5 überall". Es ist die Stufe, wo die zusätzliche Fähigkeit die zusätzlichen Kosten für das Risiko dieser Domäne noch rechtfertigt. Regulierte und sicherheitskritische Fähigkeiten brauchen vielleicht echt die obersten Sprossen, und Prüfung fordert oft mindestens ein "definiertes" Stufe-3-Niveau. Viele andere sind bei Stufe 3 gut bedient und würden nur Bürokratie anhäufen, indem sie weiter drücken. Entscheiden Sie Ziele pro Fähigkeit, und hören Sie auf zu klettern, wenn die risikoangepasste Rendite es tut.

### Vor Reifetheater schützen

Der eine Fehlschlagsmodus, der den Wert von Reifegradmodellen zerstört, ist Optimieren für die Punktzahl. Achten Sie auf Bewertungen, die großzügig benoten, Beleg, nur für die Bewertung zusammengestellt, oder "Stufe 5"-Behauptungen, die Produktionsvorfälle widersprechen. Halten Sie die Bewertung an beobachtbares Verhalten und echte Ergebnisse gebunden. Rotieren oder extern gegenprüfen Sie Ihre Bewertende. Behandeln Sie eine verdächtig hohe Selbstpunktzahl als Geruch. In dem Moment, in dem die Stufe zum Ziel wird, hört das Modell auf, Ihnen die Wahrheit zu sagen.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| **Formale bewertete Modelle (CMMI, CMMC)** | Vergleichbar, vertraglich anerkannt, rigoros | Teuer; lädt Tricksen ein; kann Prozess versteinern |
| **Leichtgewichtige interne Scorecards** | Schnell, handlungsfähig, niedriger Overhead | Extern weniger vergleichbar; leicht voreingenommen |
| **Evidenzbasierte Fähigkeitsmodelle (DORA)** | An echte Ergebnisse gebunden; forschungsgestützt | Engerer Umfang; braucht echte Kennzahlen |
| **Einzelne Gesamtreifenote** | Einfach zu kommunizieren | Versteckt ungleichmäßige Fähigkeit; führt in die Irre |
| **Pro-Fähigkeit-Bewertung** | Genaue, handlungsfähige Priorisierung | Mehr Aufwand; keine einzelne Schlagzeilenzahl |

Die zentrale Spannung ist **Bewertung als Spiegel vs. Bewertung als Ziel**. Dasselbe Modell, das einem Team hilft, sich klar zu sehen, wird kontraproduktiv in dem Moment, in dem eine Stufe an Belohnung, Berechtigung, oder Status gebunden wird. Je mehr eine Stufe zählt, desto mehr Energie fließt in den Anschein von Reife statt die Substanz.

## Fragen zur Diskussion mit Ihrem Team

1. **Sollten wir eine offene interne Selbsteinschätzung getrennt von jeder vertraglich bewerteten Stufe halten, und wer besitzt jede?** Wenn eine CMMC- oder CMMI-Stufe Umsatz tort, driften Bewertung und Wahrheit auseinander, denn Energie fließt zum Bestehen statt zum Verbessern. Für ein großes Unternehmen oder eine Behördenlieferantin ist diese Lücke, wo sich Risiko versteckt: Sie bestehen die Prüfung und bleiben exponiert. Führen Sie absichtlich zwei Bücher. Halten Sie die formale Bewertung für Berechtigung, und halten Sie eine unverblümte interne Scorecard, für deren Aufblähen niemand belohnt wird. Benennen Sie eine Besitzerin für jede, und behandeln Sie jede Distanz zwischen ihnen als Signal zu untersuchen, nicht zu übertünchen. Bringen Sie jüngste Vorfälle, Beinahe-Unfälle, und Nach-Bewertung-Verfall zum Meeting als Beleg, welches Buch die Wahrheit sagt.

2. **Übernehmen wir für jede Domäne ein etabliertes evidenzbasiertes Modell oder erfinden wir unsere eigene Scorecard, und ist das der richtige Ruf?** Etablierte Modelle (DORA für Lieferung, SAMM oder BSIMM für Sicherheit, TMMi für Testen) tragen Forschung und externe Vergleichbarkeit, die ein selbstgemachtes Raster nicht erreichen kann. Eine leichtgewichtige interne Vier-Stufen-Skala ist schneller und handlungsfähiger, und ist oft die bessere Wahl für interne Steuerung. Die Falle ist, ein schwergewichtiges maßgeschneidertes Framework zu erfinden, das die ganze Zeremonie eines formalen Modells hat und keine seiner Evidenzbasis. Entscheiden Sie pro Domäne: reservieren Sie formale bewertete Modelle dort, wo ein Vertrag sie fordert, nutzen Sie evidenzbasierte Modelle, wo sie existieren und passen, und halten Sie eine einfache Pro-Fähigkeit-Skala für alles andere. Bringen Sie die Liste der Domänen, markieren Sie, welches Modell jede heute nutzt, und fordern Sie jede erfundene Scorecard heraus.

3. **Wer führt unsere Bewertungen durch, wie würden wir großzügige Benotung fangen, und wie oft bewerten wir neu?** Eine Bewertung, die sich selbst benotet, schmeichelt sich selbst, und Reife driftet, während sich Menschen, Systeme, und Bedrohungen ändern, eine zwei Jahre alte Bewertung ist also oft Fiktion. Rotieren Sie Bewertende oder holen Sie eine externe Gegenprüfung, und behandeln Sie eine verdächtig hohe Selbstpunktzahl als Geruch, dem nachzugehen ist, nicht ein Sieg zu feiern. Setzen Sie eine Neubewertungskadenz, gebunden daran, wie schnell sich jede Domäne ändert: Sicherheit öfter als, sagen wir, Dokumentation. Sammeln Sie Beleg und beziehen Sie die Menschen ein, die die Arbeit tun, statt Meinungen von Managerinnen zu sammeln. Wenn Ihre Antwort ist, dass ein Team sich einmal jährlich ohne Gegenprüfung selbst bewertet, messen Sie Komfort, keine Fähigkeit.

4. **Welche Zielreifestufe braucht jede Fähigkeit tatsächlich, und wo würde höher zu drücken nur Prozessgewicht kaufen?** Höher ist nicht kostenlos: jede Stufe nach oben kostet Aufwand und fügt üblicherweise Zeremonie hinzu, ein Pauschalziel von Stufe 5 überall entwässert also ein endliches Verbesserungsbudget in Bürokratie, die manche Domänen nie zurückzahlen werden. Für eine große Organisation variiert das richtige Ziel nach Fähigkeit, denn ein Niedrigrisikobereich bei Stufe 2 mag völlig sicher sein, während ein sicherheits- oder compliance-kritischer Bereich auf derselben Stufe ein Notfall ist. Bringen Sie eine Pro-Fähigkeit-Risikobewertung, eine ehrliche Schätzung, was die nächste Sprosse an Aufwand und Prozess kostet, und jede Prüfungs- oder Vertragsuntergrenze, denn viele Prüfungen fordern mindestens ein definiertes Stufe-3-Niveau. In Unternehmens- und Behördenumgebungen brauchen manche regulierten Fähigkeiten echt die obersten Sprossen, während die meisten bei Stufe 3 gut bedient sind, entscheiden Sie Ziele also absichtlich, Fähigkeit für Fähigkeit, und hören Sie auf zu klettern, sobald die risikoangepasste Rendite es tut.

5. **Als wir letztes Mal eine Reifestufe erhöhten, verbesserte sich das Ergebnis, das sie schützen sollte, tatsächlich, oder bewegte sich nur die Punktzahl?** Eine Stufe, die klettert, während Vorfälle, Durchlaufzeit, oder Defektraten flach bleiben, ist Goodharts Gesetz in Aktion: sobald die Zahl zum Ziel wird, hört sie auf, Fähigkeit zu messen. Für ein großes Team rutscht das leicht durch, denn eine erfolgreiche Bewertung fühlt sich wie Fortschritt an, selbst wenn Produktion eine andere Geschichte erzählt. Binden Sie die Stufe jeder Fähigkeit an eine echte Ergebniskennzahl, bevor Sie investieren, dann bringen Sie den Vorher-Nachher-Beleg zur Diskussion: Vorfälle pro Quartal, Änderungsfehlschlagsrate, Erholungszeit, was auch immer die Fähigkeit zu verbessern existiert. In Unternehmens- und Behördenportfolios, wo eine bewertete Stufe Berechtigung tort, ist die Lücke gefährlich, denn die Stufe kann auf zusammengestelltem Beleg steigen, während die zugrunde liegende Praxis still verfällt, und der erste Beweis dafür ist ein Verstoß, Ausfall, oder eine gescheiterte Prüfung.

6. **Kommunizieren wir eine Schlagzeilen-Reifenote oder ein Pro-Fähigkeit-Bild, und sind Stufen je an Belohnung, Rangfolge, oder Teamstand gebunden?** Eine einzelne Gesamtzahl ist leicht Führung zu präsentieren und versteckt genau die Ungleichmäßigkeit, die zählt, denn starke Lieferung kann eine Stufe-1-Sicherheitsfähigkeit maskieren; eine Pro-Fähigkeit-Heatmap ist mehr Arbeit, zeigt aber, wo niedrige Reife auf hohes Risiko trifft. Die härtere Frage ist, wie die Punktzahlen genutzt werden, denn in dem Moment, in dem eine Stufe an die Belohnung oder Rangfolge eines Teams gebunden ist, stirbt ehrliche Berichterstattung und Aufwand fließt in den Anschein von Reife statt die Substanz. Bringen Sie die Heatmap, und einen offenen Bericht jedes Orts, wo eine Stufe aktuell eine Leistungsüberprüfung, eine Budgetentscheidung, oder eine Anbieterinnen-Scorecard speist. Für Unternehmen und Behördenlieferantinnen, wo bewertete Stufen Umsatz und Berechtigung toren können, seien Sie explizit, welche Noten Konsequenzen tragen und welche nur zum Steuern existieren, denn ein Reifebild, für dessen Aufblähen Menschen belohnt werden, hört auf, Realität zu beschreiben.

## Branchenperspektive

**Startup.** Ein schwergewichtiges bewertetes Modell ist Overhead, den Sie sich auf kurzer Landebahn nicht leisten können. Führen Sie eine einstündige Selbsteinschätzung auf einer einfachen Skala über eine Handvoll Fähigkeiten durch, beheben Sie nur die Lücke niedrigster Reife, die etwas Konkretes blockiert (sagen wir, den Sicherheitsfragebogen Ihrer ersten Unternehmenskundin), und lassen Sie den Rest in Ruhe. Die Bewertung sollte einen Nachmittag kosten, keine Beraterin, und ihre Ausgabe ist eine einzelne nächste Aktion statt einer einheitlich hohen Punktzahl, die Sie weder brauchen noch finanzieren können.

**Kleinunternehmen.** Ohne dedizierte Bewertende und mit engem Budget, leihen Sie ein leichtgewichtiges öffentliches Modell statt ein maßgeschneidertes Framework zu beauftragen: eine kurze Liefer- oder Sicherheitscheckliste, die Sie selbst bewerten können. Behandeln Sie es als jährliches Gespräch darüber, wo eine Schwachstelle Sie eine Kundin kosten würde, kein stehendes Programm. Halten Sie es günstig und schlicht, denn eine schmeichelnde Punktzahl, für die Sie eine Anbieterin bezahlten, ist weniger wert als eine offene, die Sie selbst an einem Nachmittag produzierten.

**Großunternehmen.** Der Wert ist eine geteilte Pro-Fähigkeit-Scorecard, konsistent über viele Teams angewendet, damit Lücken vergleichbar werden und Verbesserungsbudget dorthin fließt, wo niedrige Reife auf hohes Risiko trifft. Schützen Sie sich hart gegen Reifetheater, sobald Stufen Budget oder Status speisen: rotieren oder extern gegenprüfen Sie Bewertende, und verwalten Sie die Ergebnisse als Heatmap, die Paved-Road-Investition lenkt (Kapitel 4.2), statt einer Ranglisten-Tabelle, die Teams rangiert und ehrliche Berichterstattung tötet.

**Behörde.** Eine Reifestufe ist hier oft ein buchstäbliches Tor: CMMC für Verteidigungsarbeit, eine CMMI-Bewertung als Lieferantinnenqualifikation. Erfüllen Sie die geforderte Stufe mit echter Fähigkeit, und halten Sie eine offene interne Selbsteinschätzung getrennt von der formalen Bewertung, damit die Prüfungsuntergrenze nie still zur Decke wird. Dokumentieren Sie Beleg transparent für Bewertende, und behandeln Sie jede Distanz zwischen der zertifizierten Stufe und echter Praxis als rechenschaftspflichtiges Risiko zu schließen, keinen Papierkram einzureichen.

## Beispiele

**Startup.** Ein zehnköpfiges SaaS-Startup führt eine einstündige Selbsteinschätzung gegen eine einfache Vier-Stufen-Skala durch, die Lieferung, Testen, Sicherheit, und Bereitschaftsdienst abdeckt. Es findet Lieferung und Testen auf Stufe 3, aber Sicherheit auf Stufe 1 festsitzend, was zählt, weil es kurz davor steht, seine erste Unternehmenskundin mit einem Sicherheitsfragebogen zu unterschreiben. Also verbringen die Gründerinnen den nächsten Monat damit, nur Sicherheit auf eine verteidigbare Stufe 2 zu heben und lassen den Rest in Ruhe, statt einer einheitlich hohen Punktzahl nachzujagen, die sie weder brauchen noch sich leisten können.

**Großunternehmen.** Eine Finanzdienstleistungsfirma bewertet ihre 40 Teams mit einer leichtgewichtigen Pro-Fähigkeit-Scorecard (Lieferung, Testen, Sicherheit, Beobachtbarkeit, Bereitschaftsdienst). Die Heatmap enthüllt, dass Sicherheitsreife dort am meisten hinterherhinkt, wo regulatorische Exposition am höchsten ist, das Plattformteam finanziert also Paved-Road-Sicherheitswerkzeug (Kapitel 4.2) zuerst für diese Teams. Weil die Bewertung genutzt wird, Investition zu priorisieren statt Teams zu rangieren, berichten Managerinnen ehrlich. Neubewertung ein Jahr später zeigt echte Bewegung, und, entscheidend, weniger Sicherheitsvorfälle, nicht nur höhere Punktzahlen.

**Behörde.** Eine Verteidigungsauftragnehmerin muss eine geforderte CMMC-Stufe erreichen, um auf Arbeit zu bieten, und eine Systemintegratorin hält eine CMMI-Bewertung als Vertragsqualifikation. Hier ist die Reifestufe ein buchstäbliches Tor zu Umsatz. Die gut geführte Version behandelt die geforderte Stufe als Boden für echte Fähigkeit und hält eine offene interne Selbsteinschätzung getrennt von der formalen Bewertung. Die schlecht geführte Version stellt Beleg für die Bewertung zusammen und lässt echte Praxis am Tag danach verfallen, die Prüfung bestehend, während sie exponiert bleibt.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Rendite auf Reifebewertung kommt aus **gelenkter Investition**. Verbesserungsbudgets sind endlich. Blind ausgegeben finanzieren sie, was auch immer am lautesten ist. Eine Reifebewertung zeigt Ihnen, wo Fähigkeit gegen Risiko am schwächsten ist, damit dieselbe Ausgabe mehr Risikoreduktion und mehr Ergebnisverbesserung kauft. Die Bewertung selbst ist günstig, nur Tage strukturierter, evidenzbasierter Überprüfung, gegen die Kosten fehlallozierter Verbesserungsprogramme oder, schlimmer, einer unentdeckten Fähigkeitslücke gesetzt, die als Verstoß, Ausfall, oder gescheiterte Prüfung auftaucht.

Bei **Gesamtbetriebskosten** ist die Disziplin günstig, wenn Sie sie leichtgewichtig halten, und teuer, wenn sie zu Bewertungsbürokratie verhärtet. Die dominante versteckte Kosten ist *Reifetheater*: Aufwand, den Anschein von Reife zu produzieren, gibt nichts zurück und kann echtes Risiko maskieren, was negativer ROI ist. Um den Fall gegenüber Führung zu machen, präsentieren Sie Reife als Risiko-und-Investitions-Linse, eine Heatmap, die "alles verbessern" in "diese drei Dinge zuerst verbessern" verwandelt, und budgetieren Sie explizit gegen die Versuchung, Stufen um ihrer selbst willen zu jagen. Wo eine Stufe vertraglich gefordert ist (CMMC, CMMI), ist der ROI direkt: es ist der Preis der Berechtigung, und das Ziel ist, sie mit echter Fähigkeit statt teurem Vorwand zu erfüllen.

## Anti-Muster und Fallstricke

- **Stufe als Ziel:** einer Zahl nachjagen statt der Fähigkeit, die sie repräsentieren soll.
- **Reifetheater:** Beleg für eine Bewertung zusammenstellen, während echte Praxis verfällt.
- **Eine globale Note:** eine einzelne Reifepunktzahl, die gefährliche Ungleichmäßigkeit versteckt.
- **Höher-ist-immer-besser:** jede Fähigkeit zu Stufe 5 drücken, unabhängig von Risiko oder Kosten.
- **Einmal bewerten, nie wieder:** eine einmalige Bewertung, als dauerhafte Wahrheit behandelt.
- **Teams zur Schuldzuweisung rangieren:** Reife für Bestrafung nutzen, was ehrliche Berichterstattung tötet.
- **Modellanbetung:** der Zeremonie eines schwergewichtigen Frameworks über den Punkt der Nützlichkeit hinaus folgen.
- **Ergebnisse ignorieren:** die Leiter klettern, während sich Lieferung, Zuverlässigkeit, oder Sicherheit nicht verbessern.

## Reifegradmodell

- **Stufe 1, Beginnen.** Kein geteilter Begriff von Reife; Fähigkeit wird angenommen, ist ungleichmäßig, und ungemessen; jede Bewertung ist reaktiv, von einem Vorfall oder einer Prüfungsforderung ausgelöst statt geplant.
- **Stufe 2, Entwickeln.** Ein paar Teams führen Ad-hoc-Bewertungen gegen manche Skala durch, aber Modell, Kadenz, und Strenge variieren Team für Team; Ergebnisse werden inkonsistent genutzt und Beleg ist dünn, Punkten für Anschein ist also ein stetig präsentes Risiko.
- **Stufe 3, Standardisieren.** Ein einzelnes Pro-Fähigkeit-Modell und Bewertungskadenz sind organisationsweit dokumentiert und angewendet; Bewertungen sind evidenzbasiert, beziehen die Menschen ein, die die Arbeit tun, und speisen einen priorisierten Verbesserungsrückstand statt eines Zeugnisses.
- **Stufe 4, Steuern.** Reife wird mit Daten gemessen und gesteuert: die Stufe jeder Fähigkeit wird gegen eine Baseline verfolgt, an eine Ergebniskennzahl gebunden (Vorfälle, Durchlaufzeit, Änderungsfehlschlagsrate), und in gesetzter Kadenz neu bewertet, sodass Drift und großzügiges Benoten als Zahlen statt Meinungen auftauchen, und Ziele werden absichtlich pro Domäne gegen Risiko und Kosten gesetzt.
- **Stufe 5, Orchestrieren.** Bewertung ist über die Organisation integriert und kontinuierlich verbessert: Reife, Risiko, und Ergebnisse informieren Investition als ein adaptives Bild, Ziele werden neu balanciert, während sich Bedrohungen und Kontext verschieben, Bewertende werden routinemäßig rotiert oder extern geprüft, und die Praxis pensioniert aktiv Zeremonie, die ihre Kosten nicht mehr verdient.

## Diskussionsideen

1. Welche Ihrer Fähigkeiten nehmen Sie ohne Beleg als reif an?
2. Wo trifft Ihre niedrigste Reife auf Ihr höchstes Risiko, und geht dorthin Ihr Verbesserungsbudget?
3. Ist irgendeine Reifestufe in Ihrer Organisation ein Ziel oder ein Tor? Welches Verhalten hat das produziert?
4. Was ist die richtige Zielstufe für jede Fähigkeit, und wo würde weiteres Klettern nur Bürokratie hinzufügen?
5. Würden Ihre Teams ihre Reife ehrlich berichten, oder bestraft die Art, wie Sie Punktzahlen nutzen, Offenheit?
6. Als Sie zuletzt "Reife verbesserten", änderten sich Ergebnisse tatsächlich?

## Wichtigste Erkenntnisse

- Ein Reifegradmodell bewertet Fähigkeit gegen eine Leiter von Stufen und beschreibt einen Pfad zur Verbesserung: ein Spiegel, keine Trophäe.
- Wählen Sie etablierte, evidenzbasierte Modelle pro Domäne (CMMI, DORA, SAMM/BSIMM, CMMC); eine leichtgewichtige Pro-Fähigkeit-Skala ist oft am handlungsfähigsten.
- **Bewerten Sie ehrlich, pro Fähigkeit**, und nutzen Sie Ergebnisse, um **nach Risiko zu priorisieren**, nicht zu rangieren oder Schuld zuzuweisen.
- **Höher ist nicht immer besser:** setzen Sie Zielstufen absichtlich gegen Risiko und Kosten.
- Hüten Sie sich vor **Reifetheater** und **Goodharts Gesetz**: eine Stufe, die zum Ziel wird, hört auf, Fähigkeit zu messen.
- Siehe Kapitel 12.4 für die konsolidierte Reifeselbsteinschätzung dieses Buches, und den eigenen Reifeabschnitt jedes Kapitels.

## Referenzen und weiterführende Literatur

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (Ursprünge der Software-Prozessreife).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (Fähigkeits-, nicht Reifestufen-Denken für Lieferung).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defense, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore und Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (Bliki), über ihre Nutzungen und Missbräuche.
