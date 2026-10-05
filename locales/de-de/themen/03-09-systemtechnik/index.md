# 3.9 Systems Engineering

## Überblick und Motivation

[Systems Engineering](https://en.wikipedia.org/wiki/Systems_engineering) ist die Disziplin, ein ganzes komplexes System End-to-End zu konstruieren, sodass alle seine Teile zusammenarbeiten, um ein echtes Bedürfnis zu erfüllen. Die Teile umfassen weit mehr als Software. Ein modernes System kombiniert normalerweise Software, Hardware, Menschen, Daten, und Prozesse, und es muss in einer unordentlichen realen Welt funktionieren. Systems Engineering hält all das über die ganze Lebensdauer des Systems ausgerichtet.

Das unterscheidet sich von Softwarearchitektur. Softwarearchitektur (Kapitel 3.1) entscheidet, wie Softwarekomponenten strukturiert sind und wie sie miteinander sprechen. Systems Engineering sitzt eine Ebene höher. Es fragt, was das System als Ganzes tun muss, wie Software und Hardware und menschliche Betreiberinnen die Arbeit aufteilen, und wie Sie beweisen werden, dass das fertige Ding funktioniert. Seine professionelle Heimat ist [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), der International Council on Systems Engineering, und sein Ankerstandard ist [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), der die Prozesse für die Lebensdauer eines Systems definiert.

Das zählt für große Unternehmens- und Behördenprogramme, weil ihre Systeme groß, langlebig, und sicherheitskritisch oder missionskritisch sind. Eine Verteidigungsplattform, ein Flugverkehrssystem, oder eine Satellitenkonstellation mischt maßgeschneiderte Hardware, Drittanbieterteile, eingebettete und Cloud-Software, und menschliche Betreiberinnen, und kein einzelnes Team kann das ganze Ding im Kopf halten. Sie bauen oft auch ein [System der Systeme](https://en.wikipedia.org/wiki/System_of_systems): viele unabhängige Systeme, jedes für sich nützlich, die kooperieren müssen, um eine größere Fähigkeit zu liefern.

Dieses Kapitel verbindet sich mit Softwareanforderungen (Kapitel 2.8), Architekturgrundlagen (Kapitel 3.1), Softwaremodellen und -methoden (Kapitel 2.12), Interoperabilität und offenen Standards (Kapitel 3.8), und Projektmanagement (Kapitel 10.6).

## Kernprinzipien

- **Konstruieren Sie das Ganze, nicht die Teile.** Ein System gelingt oder scheitert als Ganzes, ein Subsystem isoliert zu optimieren kann also das Ganze schlechter machen.
- **Folgen Sie dem Lebenszyklus.** Ein System hat ein Leben vom ersten Konzept bis zur endgültigen Pensionierung. Planen Sie für alles davon, nicht nur den Bau.
- **Verfolgen Sie jede Anforderung.** Jedes Bedürfnis sollte sich einer Anforderung, einem Designelement, und einem Test zuordnen. Wenn Sie es nicht verfolgen können, können Sie es nicht beweisen.
- **Verwalten Sie Schnittstellen absichtlich.** Die meisten Scheitern geschehen an den Grenzen zwischen Teilen, Schnittstellen verdienen sich also expliziten Besitz und Kontrolle.
- **Verifizieren und validieren Sie getrennt.** Das Ding richtig zu bauen (Verifikation) und das richtige Ding zu bauen (Validierung) sind unterschiedliche Fragen, und Sie brauchen beide Antworten.
- **Erwarten Sie emergentes Verhalten.** Teile zu kombinieren erschafft Verhalten, das kein einzelner Teil zeigt. Manches davon ist der Punkt, und manches ist eine böse Überraschung.
- **Ko-Konstruieren Sie Hardware und Software.** Wenn beide maßgeschneidert sind, beschränken Entscheidungen in einer die andere, planen Sie sie also gemeinsam.

## Empfehlungen

### Den vollständigen Systemlebenszyklus verwalten

Behandeln Sie das System, als hätte es ein ganzes Leben, und planen Sie jede Stufe. Ein gängiger Lebenszyklus läuft: **Konzept** (das Bedürfnis verstehen und Optionen erkunden), **Anforderungen** (präzise angeben, was das System tun muss), **Design** (Architektur und Teile entscheiden), **Integration** (die Teile zusammenbringen), **Verifikation und Validierung** (beweisen, dass es funktioniert und das richtige System ist), **Betrieb** (es laufen lassen und pflegen), und **Pensionierung** (es sicher außer Betrieb nehmen, einschließlich Daten und Entsorgung). ISO/IEC/IEEE 15288 gibt Ihnen ein Prozess-Framework dafür. Die Stufen müssen kein starres Wasserfall sein; Sie können iterieren, prototypisieren, und in Inkrementen liefern. Der Punkt ist, dass Sie jede Stufe bewusst angehen, einschließlich der teuren späteren, die frühe Pläne oft ignorieren.

### Stakeholder-Bedürfnisse erfassen und Anforderungen mit Rückverfolgbarkeit zuweisen

Beginnen Sie bei den Menschen, denen das System wichtig ist: Nutzerinnen, Betreiberinnen, Besitzerinnen, Regulierungsbehörden, und die Öffentlichkeit. Sammeln Sie ihre **Bedürfnisse** in einfacher Sprache, verwandeln Sie diese Bedürfnisse dann in konstruierte **Anforderungen**, die spezifisch und testbar sind (siehe Kapitel 2.8). Als Nächstes kommt **Anforderungszuweisung**: jede Systemebene-Anforderung einem spezifischen Subsystem zuweisen, damit Sie wissen, welcher Teil verantwortlich ist, sie zu erfüllen. Behalten Sie eine **[Rückverfolgbarkeits](https://en.wikipedia.org/wiki/Requirements_traceability)matrix**, eine lebende Aufzeichnung, die jedes Bedürfnis mit seiner Anforderung verlinkt, mit dem Designelement, das es erfüllt, und mit dem Test, der es verifiziert. Sie lässt Sie jederzeit beweisen, dass jedes Bedürfnis abgedeckt ist und jeder Teil aus einem Grund existiert.

### Schnittstellen explizit verwalten

Schnittstellen sind, wo Teile sich treffen, und wo Systeme am häufigsten brechen. Eine Schnittstelle kann ein physischer Verbinder, ein Netzwerkprotokoll, ein Datenformat, oder ein menschliches Verfahren sein. Schreiben Sie für jede ein **Interface Control Document** (ICD): eine vereinbarte Spezifikation, genau wie zwei Teile sich verbinden und Information austauschen. Geben Sie jeder Schnittstelle eine klare Besitzerin auf jeder Seite. Sich auf geteilte, veröffentlichte Spezifikationen zu verlassen, statt einmaliger Konnektoren, macht Integration weit einfacher, was das Interoperabilitätsargument aus Kapitel 3.8 ist. Frieren Sie Schnittstellen früh ein, wo Sie können, denn eine späte Änderung wellt in jeden Teil, der sie berührt.

### Integrieren und dann verifizieren und validieren

**Systemintegration** kombiniert Subsysteme zum funktionierenden Ganzen, normalerweise in Stufen statt alles auf einmal, damit Sie Probleme finden, während sie noch klein sind. Nach Integration kommt **[Verifikation und Validierung](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), zwei eigenständige Prüfungen. **Verifikation** fragt: haben wir das System richtig gebaut, bedeutend erfüllt es seine spezifizierten Anforderungen? Sie verifizieren durch Inspektion, Analyse, Demonstration, und Test. **Validierung** fragt: haben wir das richtige System gebaut, bedeutend erfüllt es die echten Bedürfnisse der Stakeholder in echter Nutzung? Ein System kann Verifikation bestehen (es erfüllt die Spezifikation) und trotzdem Validierung scheitern (die Spezifikation war falsch). Planen Sie beide früh, und schreiben Sie Anforderungen und Schnittstellen so, dass sie überhaupt verifiziert werden können.

### Modellbasiertes Systems Engineering übernehmen

Traditionelles Systems Engineering produzierte Berge von Dokumenten, die aus der Synchronisation abdrifteten. **[Modellbasiertes Systems Engineering](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) ersetzt diesen Stapel mit einem einzelnen, geteilten, formalen Modell des Systems, aus dem Ansichten und Berichte generiert werden. Die gängige Modellierungssprache ist **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modeling Language), eine grafische Sprache, um die Anforderungen, Struktur, Verhalten, und Beschränkungen eines Systems zu beschreiben. Weil alles in einem verbundenen Modell lebt, aktualisiert eine Änderung überall, und Rückverfolgbarkeit wird zu einer Abfrage statt einer manuellen Jagd. MBSE verbindet sich mit den Modellierungsideen aus Kapitel 2.12. Übernehmen Sie es schrittweise, mit den hochriskantesten Teilen beginnend, wo sich ein geteiltes Modell am schnellsten auszahlt.

### Systemdenken auf emergentes Verhalten anwenden

Praktizieren Sie [Systemdenken](https://en.wikipedia.org/wiki/Systems_thinking): denken Sie über das Ganze und die Beziehungen zwischen Teilen nach, nicht nur die Teile einzeln. So antizipieren Sie **[emergentes Verhalten](https://en.wikipedia.org/wiki/Emergence)**: Eigenschaften, die nur erscheinen, wenn Teile kombinieren, und die kein einzelner Teil zeigt. Gutes Emergenz ist oft der Zweck des Systems (ein Schwarm Drohnen deckt einen Bereich ab, den keine einzelne Drohne könnte). Schlechtes Emergenz ist das Überraschungsscheitern (zwei sichere Subsysteme interagieren, um einen gefährlichen Zustand zu erschaffen). Sie können Emergenz nicht aus einem System heraustesten, das Sie nie modellierten, nutzen Sie also Simulation und strukturierte Gefahrenanalyse, um sie vor dem Betrieb zu finden.

### Hardware und Software ko-konstruieren

Wenn ein System maßgeschneiderte Hardware einschließt, konstruieren Sie Hardware und Software gemeinsam, eine Praxis genannt **[Hardware/Software-Co-Design](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Entscheidungen binden sich gegenseitig: der Chip setzt Timing-, Speicher-, und Stromgrenzen, in denen die Software leben muss, und die Bedürfnisse der Software formen, was die Hardware liefern muss. Lange Hardware-Vorlaufzeiten treiben auch den Zeitplan. Entscheiden Sie früh, welche Funktionen in Hardware und welche in Software leben, und überprüfen Sie diese Aufteilung, während Beschränkungen erscheinen.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile / Kosten |
|---|---|---|
| Volle Systems-Engineering-Strenge | Weniger späte Überraschungen, starke Rückverfolgbarkeit, sicherer und prüfbar | Hohe Vorabkosten, langsamerer Start, schwerer Prozess |
| Leichtgewichtiger / Software-Only-Ansatz | Schnell, günstig, flexibel für kleinen Umfang | Bricht bei großen multidisziplinären Systemen zusammen, verpasst Schnittstellen und Emergenz |
| Modellbasiert (MBSE) | Einzelne Quelle der Wahrheit, leichte Rückverfolgbarkeit, konsistente Ansichten | Werkzeug- und Trainingskosten, Kulturwandel, Lernkurve |
| Dokumentbasiertes Systems Engineering | Vertraut, niedrige Werkzeugkosten, leicht zu teilen | Dokumente driften aus der Synchronisation, Rückverfolgbarkeit ist manuell und fehleranfällig |

Der zentrale Kompromiss ist Strenge versus Geschwindigkeit. Volles Systems Engineering belastet Aufwand vorne in Konzept-, Anforderungs-, und Schnittstellenarbeit. Dieser Aufwand zahlt sich vielfach aus bei großen, langlebigen, sicherheitskritischen Systemen, wo ein im Betrieb gefundener Defekt tausendmal mehr kosten kann als derselbe Defekt, in Anforderungen gefunden. Bei einem kleinen, kurzlebigen, Software-Only-Produkt ist diese Strenge Overkill. Passen Sie das Gewicht Ihres Prozesses an die Größe, Lebensdauer, und das Risiko des Systems an. Der Scheitermodus ist, Wegwerfprojekt-Gewohnheiten auf ein System anzuwenden, das dreißig Jahre laufen und reales Risiko tragen wird.

## Fragen zur Diskussion mit Ihrem Team

1. **Wo haben Sie genau das gebaut, was die Spezifikation verlangte, und trotzdem das falsche System ausgeliefert, und was hätte es erwischt?** Verifikation (haben wir es richtig gebaut) und Validierung (haben wir das Richtige gebaut) beantworten unterschiedliche Fragen, und ein System kann jeden Verifikationstest bestehen, während es Validierung scheitert, weil die Spezifikation selbst falsch war. Bei großen Programmen werden die zwei zu "Testen" zusammengefasst, niemand validiert also gegen echtes Betreiberinnenbedürfnis bis spät, wenn eine Korrektur tausendmal mehr kostet als eine Anforderungsänderung. Bringen Sie ein vergangenes Beispiel, wo das gelieferte System seine Anforderungen erfüllte, aber das tatsächliche Bedürfnis verpasste, und fragen Sie, welche Validierungsaktivität (eine Simulation mit echten Betreiberinnen, ein früher Prototyp im Feld) es früher aufgedeckt hätte. Planen Sie beide Prüfungen von Anfang an, und schreiben Sie Anforderungen und Schnittstellen so, dass sie überhaupt verifiziert werden können. Die Unterscheidung entscheidet, wo Sie knappen Prüfaufwand ausgeben.

2. **Wie jagen Sie nach schlechtem emergentem Verhalten, bevor das System in Betrieb ist, nicht danach?** Sichere Subsysteme zu kombinieren kann gefährliche Zustände erschaffen, die kein einzelner Teil zeigt, und Sie können Emergenz nicht aus einem System heraustesten, das Sie nie modelliert haben. Für ein sicherheitskritisches oder missionskritisches Programm ist die Überraschungsinteraktion die, die jemanden verletzt oder die Mission scheitern lässt, sie muss also vor Live-Betrieb gefunden werden. Bringen Sie Ihren Ansatz, das Ganze zu modellieren (Simulation, strukturierte Gefahrenanalyse, ein SysML-Modell, das Interaktionen erfasst) und fragen Sie, welche Subsystem-übergreifenden Verhalten Sie tatsächlich erkundet haben versus wegangenommen. Gutes Emergenz ist oft der Zweck des Systems und wert, darauf hinzugestalten; schlechtes Emergenz ist das Scheitern, gegen das Sie konstruieren müssen. Wenn Ihre einzige Integrationsstrategie ist, die Teile zu verkabeln und zu sehen, was passiert, planen Sie, Emergenz in Produktion zu entdecken.

3. **Wann müssen die langfristigen Hardware-Entscheidungen eingefroren werden, und wie treibt diese Frist Ihren Software-Zeitplan?** Wenn ein System maßgeschneiderte Hardware einschließt, müssen die zwei ko-konstruiert werden: der Chip setzt Timing-, Speicher-, und Stromdecken, in denen die Software lebt, und Hardware-Vorlaufzeiten dominieren oft den ganzen Zeitplan. Teams, die Software als trennbar behandeln, optimieren lokal und kollidieren dann bei Integration mit Hardwarebeschränkungen, Monate verlierend. Bringen Sie die Hardware-Vorlaufzeiten und das Datum, bis zu dem die Hardware/Software-Funktionsaufteilung entschieden werden muss, und überprüfen Sie diese Aufteilung, während Beschränkungen erscheinen, statt sie blind einzufrieren. Je früher Sie entscheiden, welche Funktionen in Silizium und welche in Software leben, desto weniger teure Umkehrungen stehen Ihnen bevor. Schnittstellen zwischen den beiden verdienen ein Interface Control Document und eine Besitzerin auf jeder Seite, denn eine späte Änderung dort wellt durch alles, was sie berührt.

4. **Können Sie ein einzelnes Stakeholder-Bedürfnis den ganzen Weg zur Anforderung, zum Designelement, und zum Test verfolgen, der es beweist, und wer hält diese Verbindung am Leben?** Rückverfolgbarkeit ist, was Sie jederzeit zeigen lässt, dass jedes Bedürfnis abgedeckt ist und jeder Teil aus einem Grund existiert, doch bei einem großen Programm verrottet die Matrix in dem Moment, in dem niemand sie besitzt. Der konkurrierende Zug ist echt: Ingenieurinnen erleben Rückverfolgbarkeit als bürokratischen Overhead, und eine von Hand gepflegte Matrix driftet schneller aus dem Datum als sich das Design ändert. Bringen Sie einen echten Faden aus einem aktuellen Programm und versuchen Sie, ihn im Raum End-to-End zu gehen, von einem benannten Stakeholder-Bedürfnis, zur zugewiesenen Anforderung, zum Subsystem und Designelement, das es erfüllt, zum Verifikationstest, und notieren Sie, wo die Kette bricht. Entscheiden Sie, wer die Matrix besitzt und ob sie in einem Modell leben sollte, wo Rückverfolgbarkeit eine Abfrage ist statt einer manuellen Jagd. Für Unternehmens- und Behördenprogramme ist die Matrix auch das Prüfungsartefakt, das Regulierungsbehörden und Beschaffungsstellen verlangen, eine gebrochene Kette tut also mehr, als Ingenieurwesen zu verlangsamen; sie kann Zertifizierung oder Zahlung anhalten.

5. **Ist ein modellbasierter Ansatz seine Werkzeug- und Kulturkosten für Sie wert, oder würde er zu teurem Regalware werden?** Dokumentbasiertes Systems Engineering ist vertraut und günstig zu bewerkzeugen, aber seine Dokumente driften aus der Synchronisation und seine Rückverfolgbarkeit ist manuell und fehleranfällig; MBSE ersetzt den Stapel mit einem verbundenen Modell, zum Preis von Werkzeug, Training, und einem echten Kulturwandel. Beide Extreme sind teuer: MBSE bei einem großen multidisziplinären Programm überspringen und Sie zahlen in Integrationsüberraschungen, es ohne die Disziplin übernehmen, das Modell aktuell zu halten, und es verrottet zu Regalware, schlimmer als kein Modell überhaupt. Bringen Sie eine ehrliche Einschätzung Ihrer Werkzeugreife, wer im Team tatsächlich ein SysML-Modell verfassen und pflegen kann, und welches eine hochriskante Subsystem den Ansatz pilotieren könnte, wo sich ein geteiltes Modell am schnellsten auszahlt. Entscheiden Sie schrittweise statt die ganze Organisation auf einmal zu verpflichten. Für ein großes Unternehmens- oder Behördenprogramm mit vielen Zulieferern wägen Sie ab, ob ein geteiltes Modell der einzige realistische Weg ist, Anforderungen, Schnittstellen, und Tests über Auftragnehmerinnen hinweg konsistent zu halten, die sonst veraltete Dokumente austauschen.

6. **Finanziert Ihr Lebenszyklusplan ernsthaft Betrieb und Pensionierung, oder stoppt er still beim Start?** Die Stufen, die die Gesamtkosten eines langlebigen Systems dominieren, es Jahrzehnte zu betreiben und sicher außer Betrieb zu nehmen, sind jene, die frühe Pläne routinemäßig ignorieren, denn der Druck ist immer, auszuliefern. Die konkurrierende Erwägung ist, dass Geld und Aufmerksamkeit genau dann am knappsten sind, wenn sich diese späteren Stufen am fernsten anfühlen, Betrieb, Wartung, Datenmigration, und Entsorgung werden also aufgeschoben, bis sie zu einem teuren, riskanten Gerangel werden. Bringen Sie den aktuellen Lebenszyklusplan und prüfen Sie, ob er Besitzerinnen, Budgets, und Austrittskriterien für Betrieb und Pensionierung benennt, oder ob er Start als Ziellinie behandelt. Fragen Sie, was mit den Daten und der Hardware am Lebensende geschieht, und wer für die Jahre der Wartung dazwischen bezahlt. Für Unternehmens- und Behördensysteme, die zwanzig oder dreißig Jahre laufen müssen und dann unter öffentlicher Prüfung pensioniert werden, kann eine ungeplante Außerbetriebnahme regulatorische, umweltbezogene, oder Aufzeichnungsaufbewahrungspflichten verletzen, Pensionierung gehört also in den Plan und das Budget von der ersten Konzeptprüfung an.

## Branchenperspektive

**Startup.** Ein winziges Team kann kein formales Systems-Engineering-Programm betreiben und sollte es nicht versuchen, aber es kann Firmware, App, und Cloud immer noch als ein System statt drei separate Projekte behandeln. Schreiben Sie ein kurzes Schnittstellendokument, das festnagelt, wie die Teile sprechen, behalten Sie eine einfache Tabelle, die jedes Kundenbedürfnis mit dem Teil verlinkt, der es erfüllt, und überspringen Sie den schweren Prozess. Ihre knappste Ressource ist Ingenieursaufmerksamkeit, verbringen Sie Rückverfolgbarkeitsaufwand also nur dort, wo eine falsche Annahme an einer Grenze das Produkt im Feld still brechen würde.

**Kleinunternehmen.** Ohne dedizierte Systemingenieurin und mit knappem Budget stützen Sie sich auf veröffentlichte Standards und gekaufte Subsysteme statt maßgeschneiderter Integration, die Sie selbst gestalten und verifizieren müssen. Bevorzugen Sie Anbieter, die klare Schnittstellenspezifikationen offenlegen, damit die Teile ohne einen maßgeschneiderten Konnektor passen, den Sie für immer besitzen müssen. Formulieren Sie die Bauen-versus-Kaufen-Entscheidung um, welche Schnittstellen Sie realistisch über die Lebensdauer des Produkts kontrollieren und verifizieren können, und kaufen Sie den Rest.

**Großunternehmen.** Im Maßstab ist das Problem Konsistenz über viele Teams und Zulieferer: ein geteilter Lebenszyklusprozess, an ISO/IEC/IEEE 15288 ausgerichtet, ein Interface Control Document und eine benannte Besitzerin für jede Zulieferergrenze, und End-to-End-Rückverfolgbarkeit, damit eine Komponentenänderung kein programmweites Gerangel auslöst. Investieren Sie in MBSE, wo ein geteiltes Modell Anforderungen, Schnittstellen, und Tests über Auftragnehmerinnen hinweg ausgerichtet hält. Regieren Sie den Prozess, damit Verifikation und Validierung getrennt bleiben und jede Anforderung einem verantwortlichen Teil zugewiesen ist.

**Behörde.** Beschaffungsregeln, Transparenz, und öffentliche Rechenschaftspflicht formen jede Wahl. Spezifizieren Sie Systems-Engineering-Prozess, Rückverfolgbarkeit, und V&V-Beleg im Vertrag, verlangen Sie, dass Zulieferer Schnittstellenkontrolldokumente und Lebenszyklusartefakte liefern, die Sie prüfen können, und reservieren Sie Sicherheits- und Missionsvalidierung für unabhängige Prüfung mit echten Betreiberinnen vor jedem Live-Umschalten. Planen und finanzieren Sie Betrieb und Pensionierung explizit, denn ein öffentliches Programm ist für den vollen Lebenszyklus rechenschaftspflichtig, einschließlich sicherer Außerbetriebnahme und Aufzeichnungsaufbewahrung.

## Beispiele

**Startup.** Ein vierköpfiges Hardware-Startup, das einen vernetzten Sensor baut, kann sich kein formales Systems-Engineering-Programm leisten, behandelt das Produkt aber trotzdem als ein System aus Firmware, einer Mobil-App, und einem Cloud-Backend statt drei separater Projekte. Sie schreiben ein kurzes Schnittstellendokument, das festnagelt, wie Gerät, App, und Server sprechen (Nachrichtenformate, Einheiten, Fehlercodes) und behalten eine einfache Tabelle, die jedes Kundenbedürfnis mit dem Teil verlinkt, der es erfüllt. Wenn ein günstigerer Sensor-Chip eine Firmware-Änderung erzwingt, zeigt diese geteilte Schnittstelle sofort, was App und Backend anpassen müssen, sodass ein Komponententausch das Produkt im Feld nicht still bricht.

**Großunternehmen.** Ein globaler Automobilhersteller baut eine neue Elektrofahrzeugplattform: ein System aus Software (Batteriemanagement, Fahrassistenz, Infotainment), Hardware (Motoren, Sensoren, Chips), und menschlichen Faktoren, plus viele Zulieferer, jeder Subsysteme liefernd. Das Unternehmen betreibt ein Systems-Engineering-Programm. Stakeholder-Bedürfnisse speisen zugewiesene Anforderungen, jede Zulieferer-Schnittstelle hat ein Interface Control Document, und ein SysML-Modell bindet Anforderungen an Design an Tests. Wenn eine Batteriezellen-Zuliefererin eine Komponente ändert, zeigt das Rückverfolgbarkeitsmodell genau, welche Anforderungen, Schnittstellen, und Tests betroffen sind, sodass die Änderung eingedämmt ist, statt ein programmweites Gerangel auszulösen.

**Behörde.** Eine nationale Flugnavigationsbehörde modernisiert ihr Flugverkehrsmanagementsystem, ein sicherheitskritisches System der Systeme, das Radare, Fluglotsen-Arbeitsstationen, Kommunikation, und Software umspannt, rund um die Uhr betrieben. Das Programm folgt ISO/IEC/IEEE 15288 über den vollen Lebenszyklus. Verifikation beweist, dass jedes Subsystem seine Spezifikation erfüllt, und Validierung durch Simulation mit echten Fluglotsinnen beweist, dass das integrierte System sicheren Betrieb unterstützt, bevor irgendein Live-Verkehr davon abhängt. Strenge V&V lässt die Behörde in Stufen umschalten, mit Rückfallmöglichkeit bei jedem Schritt, denn hier ist ein ungetestetes emergentes Scheitern ein Ereignis öffentlicher Sicherheit.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Motivation ist, dass Defekte exponentiell teurer werden, je später Sie sie finden. Ein während der Anforderungsstufe erwischter Anforderungsfehler kostet fast nichts zu beheben. Derselbe Fehler, im Betrieb erwischt, kann tausendmal mehr kosten, und bei einem sicherheitskritischen System kann er Leben, Rückrufe, oder eine gescheiterte Mission kosten. Systems Engineering verschiebt Defektentdeckung in die günstigen frühen Stufen.

Für **Return on Investment** (ROI, gewonnener Wert im Vergleich zu ausgegebenen Kosten) ist der Ertrag vermiedene Nacharbeit, weniger Integrationsscheitern, und Programme, die Zeitplan und Budget treffen statt zu überschreiten. Branchenstudien großer Programme finden wiederholt, dass starker Systems-Engineering-Aufwand mit kleineren Überschreitungen korreliert. Für **Gesamtbetriebskosten** (TCO, die vollen Lebenszeitkosten, ein System zu bauen, zu betreiben, und zu pensionieren) macht Systems Engineering die Betriebs- und Pensionierungsstufen aus, die langfristige Kosten dominieren, aber die Ad-hoc-Projekte ignorieren. Für Wartbarkeit, Schnittstellen, und Entsorgung von Anfang an zu gestalten senkt die Kosten der Jahrzehnte, die das System im Dienst verbringt. Siehe Projektmanagement (Kapitel 10.6).

## Anti-Muster und Fallstricke

- **Großes Vorabdesign ohne Iteration.** Den Lebenszyklus als starren Einweg-Wasserfall behandeln, sodass Sie erst nach dem Bau von allem lernen, dass die Anforderungen falsch waren.
- **Anforderungen ohne Rückverfolgbarkeit.** Ein Haufen Anforderungen, die niemand mit Design oder Tests verlinkt, sodass Sie Abdeckung nicht beweisen oder irgendeinen Teil rechtfertigen können.
- **Schnittstellen ignorieren.** Annehmen, dass Subsysteme einfach zusammenpassen werden, dann Monate bei Integration an Grenzenfehlpassungen verlieren, die niemand besaß.
- **Verifikation ohne Validierung.** Beweisen, dass das System seine Spezifikation erfüllt, während nie geprüft wird, ob die Spezifikation echten Bedürfnissen entsprach, dann das falsche System ausliefern.
- **Software als getrennt behandeln.** Software-Teams optimieren lokal, während sie Hardwarebeschränkungen, Timing, und menschliche Betreiberinnen ignorieren.
- **MBSE als Regalware.** Ein Modell einmal bauen, dann es aus der Synchronisation verrotten lassen, sodass es schlimmer wird als kein Modell.
- **Pensionierungsplanung überspringen.** Kein Plan für Außerbetriebnahme, Datenmigration, oder Entsorgung, sodass Lebensende zu einem teuren, riskanten Gerangel wird.

## Reifegradmodell

**Stufe 1: Beginnen.** Systems Engineering ist Ad-hoc und reaktiv. Anforderungen leben in verstreuten Dokumenten, Schnittstellen werden bei Integration entdeckt, und Verifikation ist, was auch immer Testen zufällig geschieht. Große Programme überschreiten regelmäßig und überraschen das Team spät.

**Stufe 2: Entwickeln.** Grundlegende Praktiken existieren bei größeren Programmen. Anforderungen werden erfasst und festgelegt, Schlüsselschnittstellen haben Kontrolldokumente, und es gibt einen Verifikationsplan. Die Praxis ist zwischen Teams uneinheitlich und hängt von Einzelpersonen ab statt einer geteilten Methode.

**Stufe 3: Standardisieren.** Systems Engineering ist eine dokumentierte, organisationsweite Disziplin, an ISO/IEC/IEEE 15288 ausgerichtet und über Teams durchgesetzt. Der volle Lebenszyklus ist geplant, Rückverfolgbarkeit wird End-to-End gepflegt, Schnittstellen sind formal kontrolliert, und Verifikation und Validierung sind eigenständig und geplant. MBSE wird bei komplexen Programmen genutzt.

**Stufe 4: Steuern.** Systems Engineering wird mit Daten gemessen und gesteuert. Die Organisation verfolgt Kennzahlen gegen Baselines: Anforderungsvolatilität und Rückverfolgbarkeitsabdeckung, bei Integration gefundene Schnittstellendefekte, Verifikations- und Validierungsbestehensraten, und Defektaustritt nach Lebenszyklusstufe (wie viele Defekte jede Stufe entkommen, um später zu höheren Kosten erwischt zu werden). Prüfungen steuern Programme auf diesen Zahlen, und Schwellen lösen korrektive Aktion aus statt Nachträgliches-Feuerlöschen.

**Stufe 5: Orchestrieren.** Systems Engineering wird kontinuierlich verbessert und über die Organisation integriert. Ein lebendes MBSE-Modell ist die einzelne Quelle der Wahrheit, Rückverfolgbarkeit ist automatisiert, Simulation prognostiziert emergentes Verhalten vor dem Bau, und Kennzahlen aus vergangenen Programmen speisen das nächste. Hardware und Software werden als Selbstverständlichkeit ko-konstruiert, und der Prozess passt sich an, während sich Programme, Zulieferer, und Risiken verschieben.

## Diskussionsideen

- Wo ist die Linie zwischen Systems Engineering und Softwarearchitektur in Ihrer Organisation, und wer besitzt den Raum dazwischen?
- Können Sie bei Ihrem größten Programm ein einzelnes Stakeholder-Bedürfnis den ganzen Weg zum Test verfolgen, der es verifiziert? Wenn nicht, was würde es brauchen?
- Welche Ihrer jüngsten Scheitern geschahen an einer Schnittstelle, und wer besaß sie?
- Würde sich MBSE für Sie auszahlen, oder würde es angesichts Ihrer Kultur und Werkzeuge zu teurem Regalware werden?
- Adressiert Ihr Lebenszyklusplan ernsthaft Betrieb und Pensionierung, oder stoppt er still beim Start?

## Wichtigste Erkenntnisse

- Systems Engineering konstruiert das ganze System (Software, Hardware, Menschen, und Prozesse) End-to-End, und ist eigenständig von Softwarearchitektur.
- Planen Sie den vollen Lebenszyklus, von Konzept über Anforderungen, Design, Integration, V&V, Betrieb, bis Pensionierung.
- Verfolgen Sie jedes Bedürfnis zu einer Anforderung, einem Designelement, und einem Test, und weisen Sie jede Anforderung einem verantwortlichen Teil zu.
- Verwalten Sie Schnittstellen explizit mit klarem Besitz und Kontrolldokumenten, denn Grenzen sind, wo Systeme brechen.
- Verifikation (richtig gebaut) und Validierung (das Richtige gebaut) sind unterschiedliche Prüfungen, und Sie brauchen beide.
- Nutzen Sie MBSE und SysML für eine verbundene Quelle der Wahrheit, und nutzen Sie Systemdenken, um emergentes Verhalten zu antizipieren.
- Passen Sie das Gewicht Ihres Prozesses an die Größe, Lebensdauer, und das Risiko des Systems an.

## Referenzen und weiterführende Literatur

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, und Rick Steiner, *A Practical Guide to SysML: The Systems Modeling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage und William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede und William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin und Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defense, *Defense Acquisition Guidebook* (Systems-Engineering-Leitfaden)
