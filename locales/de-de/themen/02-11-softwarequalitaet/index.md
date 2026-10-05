# 2.11 Softwarequalität

## Überblick und Motivation

[Softwarequalität](https://en.wikipedia.org/wiki/Software_quality) ist, wie gut ein System erklärte Bedürfnisse und angemessene Erwartungen erfüllt. Das bedeutet mehr, als ob es funktioniert: Es bedeutet, ob das System zuverlässig, sicher, wartbar, nutzbar, performant, und über Zeit für seinen Zweck geeignet ist. Qualität ist breiter als Testen. Testen (Kapitel 2.4) ist eine Aktivität, die Fehler offenbart. Qualität ist die ganze Disziplin, das Richtige gut zu bauen, und mit Belegen zu wissen, dass Sie das getan haben. Ein System kann jeden Test bestehen und trotzdem geringe Qualität haben, wenn es unwartbar, unzugänglich, oder schlecht dafür geeignet ist, was Nutzerinnen tatsächlich brauchen.

In einem großen Team kann Qualität nicht im Kopf einer Person oder den Gewohnheiten eines Teams leben. Hunderte Ingenieurinnen, mehrere Produkte, und langlebige Systeme brauchen eine gemeinsame Definition von Qualität, explizite Prozesse, sie abzusichern, und Messungen, die Ihnen sagen, ob sie besser oder schlechter wird. Ohne das wird "Qualität" zu einer vagen Ambition, die jedes Argument gegen eine Frist verliert, und Fehler häufen sich, bis Änderung langsam und riskant wird.

In Unternehmens- und Behördenumgebungen steigen die Einsätze höher. Regulierte, sicherheitskritische, und bürgerorientierte Systeme müssen Qualität demonstrieren, nicht nur behaupten: dokumentierte Prozesse, nachvollziehbare Belege, und unabhängige Verifikation sind oft obligatorisch. Schlechte Qualität trägt direkte finanzielle, rechtliche, und Reputationskosten, und in manchen Domänen bringt sie Menschen in Gefahr. Eine bewusste Qualitätsdisziplin, gebaut aus Modellen, Prozessen, Messung, und Kultur, ist es, was Qualität von einem Zufall zu einem gesteuerten Ergebnis macht.

## Kernprinzipien

- Qualität ist Zweckeignung plus Konformität mit Anforderungen; definieren Sie beide explizit.
- Qualität wird eingebaut, nicht hineingetestet; Verifikation findet Fehler, aber Prävention vermeidet sie.
- Unterscheiden Sie [Qualitätssicherung](https://en.wikipedia.org/wiki/Quality_assurance) (sind unsere Prozesse solide?) von [Qualitätskontrolle](https://en.wikipedia.org/wiki/Quality_control) (ist dieses Produkt gut?).
- Verifikation fragt "haben wir es richtig gebaut?"; Validierung fragt "haben wir das Richtige gebaut?"
- Messen Sie Qualität mit einer kleinen Menge bedeutsamer Kennzahlen; behandeln Sie Kennzahlen als Signale, nicht Ziele.
- Die Kosten eines Fehlers steigen, je später er gefunden wird, verschieben Sie Qualitätsaktivitäten also früher.
- Qualität ist eine Eigenschaft der gesamten Organisation und ihrer Kultur, kein Tor am Ende.

## Empfehlungen

### Ein gemeinsames Qualitätsmodell wie ISO/IEC 25010 übernehmen

Geben Sie Ihrer Organisation ein gemeinsames Vokabular für Qualität, indem Sie ein anerkanntes Produktqualitätsmodell übernehmen. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) definiert Charakteristiken einschließlich funktionaler Eignung, Performance-Effizienz, Kompatibilität, Nutzbarkeit, Zuverlässigkeit, Sicherheit, Wartbarkeit, und Portabilität. Nutzen Sie es, um Qualität konkret zu machen: Entscheiden Sie für jedes System, welche Charakteristiken am meisten zählen und was "gut genug" für jede bedeutet. Diese Produktqualitätscharakteristiken sind dieselben **Qualitätsattribute**, die Architektur antreiben (Kapitel 3.1). Qualität und Architektur sind zwei Ansichten eines Anliegens, lassen Sie sie also eine Prioritätenliste teilen statt zwei konkurrierende.

### Qualitätssicherung von Qualitätskontrolle trennen

Behandeln Sie Qualitätssicherung (QA) und Qualitätskontrolle (QC) als eigenständige, aber ergänzende Aktivitäten. QA ist prozessorientiert und präventiv: Sie verbessert die Art, wie Arbeit erledigt wird, durch Standards, Prüfungen, Definitionen von "erledigt", und Training, damit Fehler von vornherein weniger wahrscheinlich auftreten. QC ist produktorientiert und detektivisch: Sie inspiziert tatsächliche Arbeitsprodukte, wie Testen, [Code-Review](https://en.wikipedia.org/wiki/Code_review), und Prüfungen, um Fehler zu erwischen, die tatsächlich hineinkamen. Eine reife Organisation investiert in beide, neigt aber zu QA, denn Fehler zu verhindern ist günstiger als sie zu finden und zu beheben.

### Explizite Softwarequalitätsmanagementprozesse durchführen

Machen Sie Qualität zu einem gesteuerten Prozess, keiner stillen Hoffnung. Schreiben Sie für bedeutsame Arbeit einen Qualitätsplan, der die Zielqualitätscharakteristiken, die Sicherungs- und Kontrollaktivitäten, die Akzeptanzkriterien, und die Verantwortliche nennt. Weben Sie ihn in Praktiken ein, die Sie bereits haben: Code-Review (Kapitel 2.5) sowohl als Kontrolle als auch als Weg, Wissen zu teilen, Teststrategie (Kapitel 2.4) als das automatisierte Sicherheitsnetz, und [statische Analyse](https://en.wikipedia.org/wiki/Static_program_analysis) als kontinuierliche Inspektion. Überprüfen Sie die Qualitätsdaten regelmäßig und handeln Sie nach Trends, statt nur auf Vorfälle zu reagieren.

### Verifikation und Validierung als eigenständige Disziplinen praktizieren

Verifikation bestätigt, dass Arbeitsprodukte ihre Spezifikationen erfüllen, damit die richtigen Eingaben in jede Stufe die richtigen Ausgaben produzieren, durch Prüfungen, statische Analyse, und Testen gegen Anforderungen. Validierung bestätigt, dass das fertige System tatsächlich Nutzerbedürfnisse und seinen beabsichtigten Gebrauch erfüllt, durch Nutzertests, Abnahmetests, Pilotprojekte, und Feldfeedback. Sie brauchen beide. Ein System kann korrekt gegen eine fehlerhafte Spezifikation sein (verifiziert, aber nicht valide), oder es kann ein echtes Bedürfnis erfüllen, während es noch Fehler enthält (valide, aber nicht verifiziert). In regulierten Umgebungen mag unabhängige [Verifikation und Validierung](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) durch eine von den Entwicklerinnen getrennte Partei erforderlich sein.

### Qualität mit bedeutsamen Kennzahlen messen

Wählen Sie eine kleine Menge Kennzahlen, die Qualitätsergebnisse und ihre Treiber widerspiegeln, und beobachten Sie sie über Zeit. Nützliche Maße umfassen Fehlerdichte, entwichene Fehlerrate (in Produktion gefundene Fehler gegenüber vor der Veröffentlichung), mittlere Zeit zur Erkennung und Reparatur, Änderungsfehlerrate, Code-Gesundheitssignale wie Komplexität und Duplikation, und Validierungssignale wie nutzergemeldete Probleme und Barrierefreiheitskonformität. Meiden Sie Vanity- und manipulierbare Kennzahlen: eine Kennzahl, die zum Ziel wird, hört auf, Realität zu messen. Koppeln Sie die Zahlen mit qualitativen Signalen aus Prüfungen und Nutzerfeedback.

### Fehler systematisch charakterisieren und managen

Behandeln Sie Fehler als Daten, nicht nur als zu löschende Brände. Klassifizieren Sie sie nach Schwere, Typ, und Grundursache. Verfolgen Sie sie von der Entdeckung bis zur Lösung. Suchen Sie nach Mustern, damit Sie Wiederholung verhindern können. Nutzen Sie Techniken wie [Grundursachenanalyse](https://en.wikipedia.org/wiki/Root_cause_analysis) und Fehlerkategorisierung, um einmalige Fehler von systemischen Schwächen zu unterscheiden. Speisen Sie, was Sie lernen, zurück in QA, durch aktualisierte Standards, hinzugefügte Tests, und verbesserte Prüfungen, damit dieselbe Fehlerklasse nicht zurückkehrt. Ein ohne Verständnis seiner Ursache behobener Fehler ist ein Fehler, den Sie zurückeingeladen haben.

### Die Qualitätskosten bewusst managen

Verstehen Sie Qualitätsökonomie durch die klassischen Kategorien: Präventionskosten (Training, Standards, gutes Design, Werkzeug), Bewertungskosten (Prüfungen, Testen, Audits), und Fehlerkosten (interne Nacharbeit vor der Veröffentlichung, plus externe Fehler, gefunden von Nutzerinnen, die weit mehr kosten). Verschieben Sie Ihre Investition zu Prävention und früher Bewertung, denn jeder Dollar dort vermeidet viele Dollar späterer Fehlerkosten. Machen Sie diese Kosten sichtbar, damit "wir haben keine Zeit für Qualität" für das gesehen wird, was es ist: eine Wahl, stattdessen mehr für Fehler auszugeben.

### Eine Qualitätskultur aufbauen

Machen Sie Qualität zur Verantwortung aller, besessen von den Teams, die die Software bauen, statt an eine nachgelagerte QA-Abteilung übergeben, die sie am Ende inspiziert. Führungskräfte sollten Qualitätsergebnisse belohnen, es sicher machen, Fehler und Beinahe-Vorfälle zu melden, und Qualitätsdaten als Lernwerkzeug statt als Knüppel behandeln. Ein schuldfreier Ansatz zu Fehlern bringt Probleme früh ans Licht. Ein beschuldigender versteckt sie, bis sie teuer sind.

## Abwägungen: Vor- und Nachteile

| Praxis/Wahl | Vorteile | Nachteile |
|---|---|---|
| Formales Qualitätsmodell (ISO 25010) | Gemeinsames Vokabular; explizite Prioritäten | Aufwand bei dogmatischer Anwendung |
| Schwere Qualitätssicherung (Prävention) | Weniger Fehler; niedrigere Gesamtkosten | Vorabinvestition; langsamer, um Auszahlung zu zeigen |
| Schwere Qualitätskontrolle (Inspektion) | Erwischt durchrutschende Fehler | Teuer; findet Fehler spät |
| Unabhängige V&V | Hohe Absicherung; objektiv | Kostspielig; langsamer; kann gegnerisch wirken |
| Reiche Qualitätskennzahlen | Sichtbarkeit; Frühwarnung | Manipulationsrisiko; Messaufwand |
| Dediziertes QA-Team | Fokus und Fachwissen | Kann Verantwortung von Entwicklerinnen abladen |
| Von Teams besessene Qualität | Eigentümerschaft; schnelles Feedback | Erfordert Disziplin und Fähigkeit überall |

Die zentrale Abwägung ist Investition gegen Absicherung, geformt durch Timing. Prävention kostet jetzt Geld, um größere Fehlerkosten später zu vermeiden. Die wirtschaftlich richtige Qualitätsstufe ist also nicht das Maximum; es ist der Punkt, wo die Grenzkosten von mehr Absicherung den Fehlerkosten entsprechen, die sie vermeidet. Dieser Punkt sitzt hoch für sicherheitskritische Systeme und niedriger für risikoarme interne Werkzeuge. Die andere wiederkehrende Spannung ist Eigentümerschaft. Zentrale QA-Gruppen bauen Fachwissen auf, können aber Entwicklerinnen erlauben, Verantwortung abzuladen. Von Teams besessene Qualität baut Eigentümerschaft auf, verlangt aber überall Fähigkeit und Disziplin.

## Fragen zur Diskussion mit Ihrem Team

1. **Wenn dieselbe Fehlerklasse zweimal auftaucht, führen wir Grundursachenanalyse durch, oder beheben wir es einfach nochmal?** Ein ohne Verständnis seiner Ursache behobener Fehler ist ein Fehler, den Sie zurückeingeladen haben, und in einem großen Team kann dieselbe Grundursache über viele Dienste hinweg auftauchen, bevor jemand die Punkte verbindet. Fehler als Daten zu behandeln (klassifiziert nach Schwere, Typ, und Ursache, dann nach Mustern durchsucht) ist, was ein Team, das stetig zuverlässiger wird, von einem trennt, das beschäftigt bleibt, denselben Fehler nachzubessern. Bringen Sie Ihren Fehlertracker zur Besprechung und suchen Sie nach wiederkehrenden Signaturen: Wie viele jüngste Vorfälle teilen eine Ursache, die Sie nie systemisch angegangen sind? Die Antwort sollte in Prävention einfließen, sodass eine wiederkehrende Ursache einen aktualisierten Standard, einen neuen gemeinsamen Helfer, einen hinzugefügten Test, oder eine bessere Prüfungscheckliste antreibt, denn so verhindert eine Korrektur an einem Ort, dass die ganze Klasse zurückkehrt.

2. **Ist es in unserem Team sicher, einen Fehler oder Beinahe-Vorfall zu melden, und was passiert mit der Person, die einen aufwirft?** Qualität ist eine Eigenschaft der Kultur, und ein schuldfreier Ansatz bringt Probleme früh ans Licht, während ein beschuldigender sie versteckt, bis sie teuer sind, was in einem regulierten oder bürgerorientierten System einen öffentlichen Fehler oder eine Strafe bedeuten kann. Das zählt am meisten im großen Maßstab, wo die einem Risiko am nächsten stehende Ingenieurin oft Junior ist und der Anreiz, still zu bleiben, stark ist. Bringen Sie ehrliche Signale: Werden Beinahe-Vorfälle protokolliert und diskutiert, oder verschwinden sie? Benennen Nach-Vorfall-Prüfungen Ursachen oder Menschen? Die Aktion ist, Qualitätsdaten zu einem Lernwerkzeug statt einem Knüppel zu machen, die Menschen zu belohnen, die Probleme ans Licht bringen, und schuldfreie Nach-Vorfall-Prüfungen durchzuführen, denn Sie können nicht verhindern, was Ihr Team sich fürchtet zu melden.

3. **Kann Validierung eine Veröffentlichung tatsächlich stoppen, und wer hält diese Autorität, wenn eine Frist droht?** Verifikation (haben wir es richtig gebaut?) und Validierung (haben wir das Richtige gebaut?) sind eigenständige Disziplinen, und Validierung hat nur Zähne, wenn eine gescheiterte Barrierefreiheitsprüfung, ein gescheiterter Abnahmetest, oder verdammende Nutzerforschung wirklich das Ausliefern blockieren können. In Unternehmens- und Behördenumgebungen ist das oft obligatorisch, manchmal durch unabhängige Verifikation und Validierung durch eine von den Entwicklerinnen getrennte Partei, und "wir haben es trotzdem ausgeliefert" ist keine Antwort, die ein Aufsichtsgremium akzeptiert. Bringen Sie Ihre letzten paar Veröffentlichungen: Hat je ein Qualitätssignal tatsächlich eine gestoppt, oder weicht das Tor immer dem Datum? Wenn Validierung nie eine Veröffentlichung blockiert hat, ist sie Dekoration, und die Korrektur ist, Akzeptanzkriterien vorab in den Qualitätsplan zu schreiben, zu benennen, wer die Go/No-go-Entscheidung besitzt, und dieser Entscheidung echte Autorität unabhängig vom Lieferdruck zu geben.

4. **Kennen wir tatsächlich unsere Kosten schlechter Qualität, und verschieben wir bewusst Ausgaben von Fehler zu Prävention?** Kosten schlechter Qualität (COPQ) sind das Geld, verloren an interner Nacharbeit, Produktionsvorfällen, Notfallkorrekturen, Support-Last, verlorenen Nutzerinnen, und Strafen, und es ist fast immer größer als die sichtbaren Ausgaben für Prüfungen und Testen. In einem großen Team sind die Fehlerkosten über Vorfallkanäle, Support-Warteschlangen, und Nacharbeit, die niemand als Nacharbeit protokolliert, verstreut, sie bleiben also unsichtbar, bis jemand sie zusammenzählt. Die Spannung ist, dass Prävention jetzt Geld kostet, in einem Budgetzyklus, um Fehlerkosten zu vermeiden, die später landen und auf dem Budget von jemand anderem landen, was den Tausch leicht auf ewig aufschiebbar macht. Bringen Sie echte Zahlen: Vorfallzahl und -kosten, Nacharbeitsstunden, entwichene Fehlerrate, und die aktuelle Aufteilung der Ausgaben über Prävention, Bewertung, und Fehler, und entscheiden Sie dann, ob sich die Mischung früher verschieben sollte. Für Unternehmens- und Behördensysteme, wo der Großteil der Lebenszeitkosten nach der ersten Veröffentlichung landet, bringen Sie COPQ vor die Menschen, die das Budget halten, denn eine Zahl, die ein Aufsichtsgremium sehen kann, ist weit schwerer wegzuhandeln als ein vager Appell an "Qualität".

5. **Welche unserer Qualitätskennzahlen sind still zu Zielen geworden, und welches Verhalten treiben sie jetzt an?** Eine Kennzahl, die zum Ziel wird, hört auf, Realität zu messen: Jagen Sie einen Abdeckungsprozentsatz, und Sie bekommen Tests, geschrieben, um die Zahl zu bewegen, nicht Tests, die Fehler erwischen. Im großen Maßstab ist das gefährlich, denn ein Schlagzeilen-Dashboard, geteilt über Dutzende Teams, setzt die Anreize für alle von ihnen, und eine manipulierbare Kennzahl verbreitet die Manipulation überall gleichzeitig. Die konkurrierende Erwägung ist, dass Sie immer noch Messung brauchen, die Antwort ist also selten "Kennzahl streichen", sondern "sie mit einem Gegensignal koppeln und neben qualitativem Beleg aus Prüfungen und Nutzerinnen lesen". Bringen Sie Ihre aktuelle Kennzahlenmenge, und fragen Sie für jede, was jemand unter Druck tun könnte, um sie zu bewegen, ohne Qualität zu verbessern, und ob Sie das geschehen sahen. In regulierten und bürgerorientierten Umgebungen seien Sie besonders wachsam bei Konformitätskennzahlen, die grün aussehen, während die zugrunde liegende Validierung (Barrierefreiheit, echte Nutzerergebnisse) nie wirklich ausgeübt wurde, denn eine Prüferin wird schließlich die Realität hinter der Zahl testen.

6. **Wer besitzt Qualität hier: die Teams, die den Code schreiben, oder eine separate Gruppe am Ende, und welche besetzen wir tatsächlich?** Eigentümerschaft formt alles nachgelagerte, denn ein nachgelagertes QA-Silo lässt Entwicklerinnen Verantwortung für den Code abladen, den sie schreiben, während von Teams besessene Qualität Eigentümerschaft auf Kosten verlangter Fähigkeit und Disziplin in jedem Team aufbaut. In einem großen Team ist das kein Entweder-oder: Das nachhaltige Muster ist normalerweise, dass Teams Qualität durch Code-Review und automatisierte Tests besitzen, unterstützt von einer kleinen zentralen Gruppe, die Standards pflegt, QA als Prozessverbesserung durchführt, und coacht, statt Qualität am Ende zu inspizieren. Bringen Sie eine ehrliche Karte, wo Qualitätsarbeit derzeit geschieht, wer verantwortlich ist, wenn ein Fehler entwischt, und wo Budget und Personalzahlen tatsächlich sitzen gegenüber wo die Rhetorik sagt, Qualität lebe. Für Unternehmens- und Behördenorganisationen fügen Sie die unabhängige Verifikations- und Validierungsanforderung hinzu: manche Absicherungsregime schreiben eine separate Partei vor, entscheiden Sie also bewusst, welche Kontrollen den Lieferteams gehören und welche unabhängig bleiben müssen, um Prüfung zu erfüllen.

## Branchenperspektive

**Startup.** Geschwindigkeit zählt mehr als Zeremonie, benennen Sie also die zwei oder drei Qualitätscharakteristiken, die Ihr Produkt tatsächlich schützen, normalerweise Zuverlässigkeit und Wartbarkeit, und lassen Sie Politur warten. Besitzen Sie Qualität über das ganze Team mit Code-Review und einer bescheidenen automatisierten Testsuite, statt eine separate QA-Gruppe aufzustellen, die Sie nicht besetzen können. Wenn dieselbe Fehlerklasse zweimal erscheint, verbringen Sie zwanzig Minuten mit der Grundursache und fügen Sie einen gemeinsamen Helfer plus einen Test hinzu, damit Prävention günstig bleibt und Ihre Änderungsfehlerrate niedrig, während Sie sich schnell bewegen.

**Kleinunternehmen.** Ohne dedizierte Qualitätsspezialistin und mit knappem Budget stützen Sie sich auf Qualität, die in die Werkzeuge und Plattformen eingebaut ist, die Sie kaufen, statt einen Prozess, den Sie selbst durchführen müssen. Wenn Sie Software wählen, behandeln Sie den Qualitätsbeleg des Zulieferers als Teil des Kaufs: Sicherheitshaltung, Barrierefreiheit, Support-Reaktionsfähigkeit, und wie oft ihre Veröffentlichungen brechen. Verfolgen Sie eine Handvoll günstiger, ehrlicher Signale (Produktionsvorfälle, kundengemeldete Probleme, Zeit zur Korrektur) statt eines aufwendigen Kennzahlenprogramms, das Sie niemanden zum Pflegen haben.

**Großunternehmen.** Die Arbeit ist Konsistenz über viele Teams: ein gemeinsames Qualitätsmodell wie ISO/IEC 25010 übernehmen, Qualitätssicherung (Prozess) von Qualitätskontrolle (Produkt) trennen, und Qualitätskostenüberprüfungen durchführen, die Ausgaben zu Prävention verschieben. Halten Sie Qualität im Besitz der Lieferteams, unterstützt von einer kleinen zentralen Gruppe, die Standards und Dashboards für entwichene Fehlerrate, Änderungsfehlerrate, und Code-Gesundheitstrends pflegt. Standardisieren Sie das Vokabular und die Tore, damit Gruppen aufhören, Qualitätspraxis neu zu erfinden, während Teams Raum bleibt, diese Messlatten auf ihre eigene Weise zu erfüllen.

**Behörde.** Beschaffung, Transparenz, und öffentliche Rechenschaftspflicht setzen den Rahmen, schreiben Sie Qualitätsanforderungen also in Verträge und verlangen Sie dokumentierten, nachvollziehbaren Qualitätsbeleg statt Behauptungen. Erwarten Sie unabhängige Verifikation und Validierung durch eine von den Entwicklerinnen getrennte Partei, obligatorische Barrierefreiheitskonformität, und Fehlerprotokolle mit Schwere und Grundursache, gehalten als Teil der Prüfspur. Berichten Sie Kosten-schlechter-Qualität-Zahlen (Nacharbeit, Widersprüche, Dienstausfälle) an Aufsichtsgremien, und geben Sie Validierung echte Autorität, eine Veröffentlichung zu blockieren, die den Bürgerinnen versagen würde, die darauf angewiesen sind.

## Beispiele

**Startup.** Ein fünfköpfiges Startup entscheidet, dass für sein frühes Produkt Zuverlässigkeit und Wartbarkeit die zählenden Qualitätscharakteristiken sind, und lässt pixelgenaue Politur warten. Qualität wird vom ganzen Team besessen: Code-Review und eine bescheidene automatisierte Testsuite sind die Kontrollen, und es gibt keine separate QA-Gruppe, an die Fehler übergeben werden. Wenn dieselbe Fehlerklasse zweimal auftaucht, verbringen sie zwanzig Minuten mit einem schnellen Grundursachenblick und fügen einen gemeinsamen Helfer plus einen Test hinzu, damit sie aufhört, wiederzukehren, statt jedes Mal von Hand nachgebessert zu werden. Diese kleine Präventionsgewohnheit hält ihre Änderungsfehlerrate niedrig, während sie sich noch schnell bewegen.

**Großunternehmen.** Ein großes Finanzdienstleistungsunternehmen übernimmt ISO/IEC 25010 als sein Qualitätsvokabular und protokolliert für jedes Produkt Zielstufen für Zuverlässigkeit, Sicherheit, und Wartbarkeit. Teams besitzen Qualität: Code-Review und automatisierte Tests sind Kontrollen in der Pipeline, während eine kleine zentrale Gruppe QA durchführt, indem sie Standards pflegt und coacht. Ein Qualitätsdashboard verfolgt entwichene Fehlerrate, Änderungsfehlerrate, und Code-Gesundheitstrends. Fehler werden klassifiziert und ursachenanalysiert, und wiederkehrende Ursachen treiben Aktualisierungen gemeinsamer Bibliotheken und Checklisten an. Die Führung überprüft Qualitätskostendaten vierteljährlich und hat Ausgaben zu Prävention verschoben, sowohl Produktionsvorfälle als auch die Kosten, sie zu beheben, senkend.

**Behörde.** Eine nationale Behörde, die eine bürgerorientierte Leistungsplattform liefert, arbeitet unter einem Absicherungsregime, das dokumentierten Qualitätsbeleg verlangt. Sie führt einen formalen Qualitätsmanagementprozess mit einem Qualitätsplan pro Veröffentlichung durch, plus unabhängiger Verifikation und Validierung durch ein von den Entwicklerinnen getrenntes Team. Verifikation prüft jedes Arbeitsprodukt gegen zu Richtlinien nachvollzogene Anforderungen. Validierung umfasst Barrierefreiheitskonformitätstests und Nutzerforschung mit echten Bürgerinnen, und beide können eine Veröffentlichung blockieren. Fehler werden mit Schwere und Grundursache als Teil der Prüfspur verfolgt, und Kosten-schlechter-Qualität-Zahlen (Nacharbeit, Widersprüche, und Dienstausfälle) gehen an Aufsichtsgremien, um fortgesetzte Investition in Prävention zu rechtfertigen.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Rendite von Qualität sind niedrigere Gesamtbetriebskosten und stetige Liefergeschwindigkeit. Die Qualitätskosten haben zwei Seiten. Die gute Ausgabe, Prävention und Bewertung, ist sichtbar und steuerbar: Design, Standards, Prüfungen, Testen, und Werkzeug. Die Kosten schlechter Qualität (COPQ) sind größer, aber oft versteckt: interne Nacharbeit, Produktionsvorfälle, Notfallkorrekturen, Kundensupport, verlorene Nutzerinnen, regulatorische Strafen, und Reputationsschaden. Studien, zurückgehend auf Crosbys "Quality Is Free", finden konsistent, dass die Gesamtkosten schlechter Qualität die Kosten ihrer Verhinderung bei Weitem übersteigen, und dass Fehler weit teurer werden, je später Sie sie erwischen: Ein im Design gefundenes Problem kostet einen Bruchteil desselben, in Produktion gefundenen Problems.

Für die Führung ist das Argument nicht "mehr für Qualität ausgeben." Es ist "früher ausgeben, um insgesamt weniger auszugeben." Quantifizieren Sie COPQ aus Ihren eigenen Daten (Vorfallzahl und -kosten, Nacharbeitsstunden, entwichene Fehlerrate) und zeigen Sie, wie Prävention und frühe Bewertung sie senken. Verbinden Sie Qualität mit Geschäftsergebnissen: Zuverlässigkeit hält Kundinnen, Wartbarkeit hält zukünftige Änderung günstig, und Sicherheit und Barrierefreiheit halten Sie aus rechtlichen Schwierigkeiten. In langlebigen Unternehmens- und Behördensystemen, wo der Großteil der Kosten nach der ersten Veröffentlichung landet, dominieren die Wartbarkeits- und Zuverlässigkeitsdimensionen von Qualität die Lebenszeitkosten. Das macht frühe Qualitätsinvestition zu einer der hebelstärksten Entscheidungen, die Sie treffen können.

## Anti-Muster und Fallstricke

- **Qualität als letztes Tor:** Qualität am Ende hineininspizieren statt sie einzubauen, sodass Fehler gefunden werden, wenn sie am teuersten sind.
- **Testen mit Qualität verwechseln:** annehmen, bestandene Tests bedeuten hohe Qualität, Wartbarkeit, Nutzbarkeit, und Zweckeignung ignorierend.
- **QA als separates Silo:** ein nachgelagertes Team, das "Qualität besitzt", Entwicklerinnen erlaubend, Verantwortung für den Code abzuladen, den sie schreiben.
- **Kennzahlentheater:** Abdeckungsprozentsätze oder Fehlerzahlen als Ziele jagen, was Manipulation einlädt und echte Qualität versteckt.
- **Verifikation ohne Validierung:** die Spezifikation korrekt bauen, während nie geprüft wird, dass die Spezifikation echte Bedürfnisse erfüllt.
- **Keine Grundursachenanalyse:** Fehler einzeln beheben, ohne die systemische Ursache anzugehen, sodass dieselbe Klasse wiederkehrt.
- **Kosten schlechter Qualität ignorieren:** Qualität als reine Kosten behandeln, weil Fehlerkosten versteckt und ungemessen sind.

## Reifegradmodell

**Stufe 1 (Beginnen).** Qualität ist undefiniert und ad hoc. Sie reitet auf individueller Sorgfalt, wird hauptsächlich durch manuelles Testen am Ende geprüft, und Fehler werden reaktiv gehandhabt, während sie auftauchen. Es gibt kein gemeinsames Modell, keine Kennzahlen, und keine Linie zwischen Sicherung und Kontrolle.

**Stufe 2 (Entwickeln).** Grundlegende Praktiken erscheinen: Code-Review, automatisierte Tests, und ein Fehlertracker. Manche Qualitätsdaten werden erhoben, aber uneinheitlich, und jedes Team macht es auf seine eigene Weise. Qualität wird noch größtenteils als Testen gesehen, Prävention ist minimal, Verifikation geschieht, und Validierung ist informell.

**Stufe 3 (Standardisieren).** Die Organisation übernimmt ein gemeinsames Qualitätsmodell (wie ISO/IEC 25010), trennt QA von QC, und führt Qualitätsmanagementprozesse mit Qualitätsplänen und Akzeptanzkriterien durch, dokumentiert und konsistent über Teams angewendet. Verifikation und Validierung sind eigenständig und bewusst, und Fehler werden nach einem vereinbarten Schema klassifiziert und ursachenanalysiert.

**Stufe 4 (Steuern).** Qualität wird gegen Baselines gemessen und gesteuert. Eine kleine Menge bedeutsamer Kennzahlen wird über Zeit verfolgt (Fehlerdichte, entwichene Fehlerrate, mittlere Zeit zur Erkennung und Reparatur, Änderungsfehlerrate, und Code-Gesundheitssignale wie Komplexität und Duplikation), und Qualitätskosten werden über Prävention, Bewertung, und Fehler quantifiziert. Akzeptanz- und Qualitätstore werden aufgrund von Belegen statt Meinung durchgesetzt, Trends werden in festem Rhythmus überprüft, und Validierung kann wirklich eine Veröffentlichung blockieren.

**Stufe 5 (Orchestrieren).** Qualität ist eine kontinuierlich verbesserte, kulturell besessene Disziplin, integriert mit Geschäfts- und Risikoplanung. Prävention ist die Betonung, Qualitätskostendaten leiten, wohin Investition geht, und Grundursachenbefunde verhindern systematisch Wiederholung. Teams besitzen Qualität von Ende zu Ende, Kennzahlen speisen kontinuierliche Verbesserung, und die Organisation passt ihre Qualitätspraxis an, während sich Produkte, Risiken, und Regulierung verschieben. Das richtet sich an den höheren Stufen der Reifegradmodelle aus Kapitel 10.8 aus.

## Diskussionsideen

- Welche ISO/IEC-25010-Qualitätscharakteristiken zählen am meisten für Ihre Systeme, und was ist "gut genug" für jede?
- Wo sitzt Ihre Organisation bei der Prävention-Bewertung-Fehler-Ausgabenmischung, und sollte sie sich verschieben?
- Unterscheiden Sie Verifikation von Validierung in der Praxis, oder verschmelzen Sie beide zu "Testen"?
- Wird Qualität von den Teams besessen, die Software bauen, oder an eine separate Gruppe delegiert, und was würde sich ändern, wenn Sie sie verschieben würden?
- Was sind Ihre wahren Kosten schlechter Qualität, und könnten Sie sie gut genug messen, um den Geschäftsfall zu machen?
- Welche Ihrer Qualitätskennzahlen sind echte Signale, und welche sind zu manipulierbaren Zielen geworden?

## Wichtigste Erkenntnisse

- Qualität ist breiter als Testen: Sie ist Zweckeignung plus Konformität, über Charakteristiken wie Zuverlässigkeit, Sicherheit, und Wartbarkeit.
- Nutzen Sie ein gemeinsames Qualitätsmodell (ISO/IEC 25010), damit Qualitätsattribute explizit sind und sich an Architektur ausrichten (Kapitel 3.1).
- Trennen Sie Qualitätssicherung (verhindern, Prozess) von Qualitätskontrolle (erkennen, Produkt), und neigen Sie zu Prävention.
- Praktizieren Sie Verifikation (es richtig gebaut) und Validierung (das Richtige gebaut) als eigenständige Disziplinen.
- Messen Sie Qualität mit ein paar bedeutsamen Kennzahlen, und charakterisieren Sie Fehler nach Schwere und Grundursache, um Wiederholung zu verhindern.
- Managen Sie die Qualitätskosten: Prävention und frühe Bewertung sind weit günstiger als Fehler, besonders in langlebigen Systemen.
- Bauen Sie eine schuldfreie Qualitätskultur, in der Teams Qualität besitzen, unterstützt von Code-Review (Kapitel 2.5) und Teststrategie (Kapitel 2.4).

## Referenzen und weiterführende Literatur

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Wissensbereich Softwarequalität.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC-25000-Serie (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones und Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (Qualitätssicherungs- und V&V-Prozesskontext).
