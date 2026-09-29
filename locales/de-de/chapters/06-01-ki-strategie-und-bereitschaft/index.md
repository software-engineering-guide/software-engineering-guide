# 6.1 KI-Strategie und -Bereitschaft

## Überblick und Motivation

[Künstliche Intelligenz](https://en.wikipedia.org/wiki/Artificial_intelligence) hat sich von einer Forschungsneuheit zu einer Kernfähigkeit entwickelt, die große Organisationen jetzt verantwortlich und im Maßstab einsetzen sollen. Für Unternehmen und Behörden ist die echte Frage nicht mehr, ob KI etwas Beeindruckendes in einer Demo tun kann. Es ist, ob eine spezifische Investition ein echtes Problem besser löst als die Alternativen, jahrelang sicher betrieben werden kann, und Prüfung, Beschaffung, und öffentliche Kontrolle übersteht. KI-Strategie ist die Disziplin, zu entscheiden, wo KI anzuwenden ist, wo sie zu vermeiden ist, und welche Grundlagen Sie brauchen, bevor das erste Modell Produktion erreicht.

Für große Teams erhöhen Maßstab und Trägheit die Einsätze. Eine schlecht gerahmte Initiative kann Budgets verbrennen, talentierte Ingenieurinnen ablenken, und Vertrauen bei Regulatorinnen und Bürgerinnen erodieren, wenn sie öffentlich scheitert. Eine gut gewählte kann Plackerei automatisieren, Einsicht aus Daten zutage fördern, die Sie nie zuvor erreichen konnten, und geschickte Menschen für höherwertige Arbeit freisetzen. Der Unterschied ist selten das Modell selbst. Es kommt darauf an, wie gut Sie das Problem rahmen, wie bereit Ihre Daten und Ihr Talent sind, und wie ehrlich Ihr Geschäftsfall ist.

Behörden- und regulierte Kontexte fügen weitere Einschränkungen hinzu. Öffentliche Stellen müssen Ausgaben rechtfertigen, Transparenz garantieren, ungesetzliche Diskriminierung vermeiden, und gegenüber gewählten Amtsträgerinnen und der Öffentlichkeit rechenschaftspflichtig bleiben. Beschaffungsregeln verbieten möglicherweise Ein-Anbieter-Lock-in, fordern Erklärbarkeit, und verlangen, dass Anbieterinnen Modellverhalten offenlegen. Behandeln Sie hier Compliance, Prüfbarkeit, und Ausstiegsoptionen als erstklassige Anforderungen, keine Nachgedanken.

## Kernprinzipien

- Beginnen Sie mit einem lohnenswerten Problem, nicht mit einer Technologie, die eine Nutzung sucht.
- Bevorzugen Sie den einfachsten Ansatz, der das Bedürfnis erfüllt; KI ist eine Option unter vielen, und oft nicht die beste.
- Behandeln Sie Datenbereitschaft, Talent, und Plattformreife als Voraussetzungen, keine parallelen Arbeitsströme, die später sortiert werden.
- Treffen Sie Bauen-versus-Kaufen-Entscheidungen explizit und überprüfen Sie sie erneut, während sich der Markt und Ihre Fähigkeiten ändern.
- Quantifizieren Sie die Gesamtbetriebskosten, einschließlich Betrieb, Überwachung, und eventuellem Ersatz, nicht nur die Lizenz oder das Pilotprojekt.
- Gestalten Sie von Tag eins für Ausstieg: vermeiden Sie Architekturen, die den Wechsel von Anbieterinnen oder Modellen unerschwinglich teuer machen.
- Behandeln Sie in regulierten und öffentlichen Umgebungen Transparenz, Beschaffungskonformität, und Rechenschaftspflicht als Designeinschränkungen.
- Messen Sie die Kosten des *Nicht*-Handelns neben den Kosten des Handelns.

## Empfehlungen

### Das Problem rahmen, bevor eine Technologie gewählt wird

Schreiben Sie eine Einseiten-Problemerklärung. Benennen Sie die Entscheidung oder Aufgabe, die Sie verbessern wollen, die aktuelle Baseline, das messbare Ergebnis, das Sie wollen, und was geschieht, wenn das System sich irrt. Fragen Sie dann, ob das Problem überhaupt zu KI passt. Gibt es genug relevante Daten? Ist die Aufgabe musterbasiert statt regelbasiert? Können Sie probabilistische Antworten tolerieren? Kann eine Person die Ausgabe prüfen? Viele Probleme werden besser mit deterministischer Software, besserem Prozessdesign, oder einfach besserer Datenhygiene gelöst. Schreiben Sie explizit auf, wo KI *nicht* gut passt: zum Beispiel Entscheidungen, die per Gesetz perfekt erklärbar sein müssen, oder wo die Kosten eines seltenen Fehlers katastrophal und unmöglich zu erwischen sind.

### Einen Bauen-versus-Kaufen-versus-Fine-Tunen-versus-Prompten-Entscheidungsbaum nutzen

Bewegen Sie sich vom günstigsten und schnellsten zum teuersten und kontrolliertesten:

1. **Ein existierendes gehostetes Modell prompten.** Wenn ein Allzweckmodell (wie Anthropics Claude, oder vergleichbare Angebote anderer Anbieterinnen) das Problem mit sorgfältigem Prompting und Retrieval löst, tun Sie das zuerst. Niedrigste Kosten, schnellste Iteration, keine Trainingsinfrastruktur.
2. **Mit Retrieval oder Werkzeugen erweitern.** Wenn die Lücke Wissen oder Handlungen ist, fügen Sie [Retrieval-Augmented Generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) hinzu, die relevante Dokumente zur Abfragezeit holt und sie dem Modell als Kontext liefert, und Werkzeugnutzung, bevor Sie Modellgewichte berühren.
3. **Fine-tunen oder anpassen.** Wenn Prompting nicht konsistent die benötigte Genauigkeit, den Ton, oder das Format erreichen kann, [fine-tunen](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) Sie ein kleineres Modell auf Ihren Daten: das heißt, trainieren Sie ein vortrainiertes Modell auf Ihren Beispielen weiter, um es zu spezialisieren. Das kauft Kontrolle auf Kosten einer [MLOps](https://en.wikipedia.org/wiki/MLOps)-(Machine-Learning-Operations)-Pipeline.
4. **Ein spezialisiertes Produkt kaufen.** Für gut definierte Domänen (Dokumentverarbeitung, Betrugsbewertung) kann ein ausgereiftes Anbieterprodukt alles schlagen, was Sie bauen.
5. **Von Grund auf bauen.** Reservieren Sie das Trainieren von [Foundation-Modellen](https://en.wikipedia.org/wiki/Foundation_model) (großen Modellen, vortrainiert auf breiten Daten und anpassbar an viele Aufgaben) für Organisationen mit einzigartigen Daten, tiefem Talent, und strategischen Gründen. Für nahezu alle Unternehmen und Behörden ist das die falsche Wahl.

### Daten-, Talent-, und Plattform-Voraussetzungen etablieren

Prüfen Sie Ihre Daten auf Verfügbarkeit, Qualität, Beschriftung, Herkunft, und rechtliche Nutzungsgrundlage. Bestätigen Sie, dass Sie tatsächlich das Recht haben, sie für KI zu nutzen, einschließlich jeglicher persönlicher oder Drittanbieterdaten. Bewerten Sie Talent ehrlich: Sie brauchen Datenwissenschaftlerinnen, und auch ML-Ingenieurinnen, Dateningenieurinnen, Produktmanagerinnen, die probabilistische Systeme verstehen, und Prüferinnen, die Ausgaben evaluieren können. Bevor Sie skalieren, richten Sie eine Plattform-Baseline ein: Experiment-Tracking, ein Modellregister (das Verzeichnis der Wahrheit für trainierte Modellversionen und ihren Genehmigungsstatus), Überwachung, und sicheres Serving, damit nicht jeder neue Anwendungsfall Betrieb neu erfindet.

### Regulierte und Behördenkontexte absichtlich handhaben

Ziehen Sie Beschaffungs-, Rechts-, und Risikoteams früh hinzu. Fordern Sie von Anbieterinnen, Modellherkunft, Trainingsdaten-Praktiken, Evaluationsergebnisse, und bekannte Einschränkungen offenzulegen. Bevorzugen Sie Verträge, die Portabilität Ihrer Daten und Prompts gewähren, und vermeiden Sie proprietäre Formate, die Sie einfangen. Wo angemessen, veröffentlichen Sie den Zweck und die Schutzmaßnahmen öffentlich zugewandter KI-Systeme, und geben Sie Menschen einen Kanal, automatisierte Entscheidungen anzufechten. Richten Sie sich an anerkannten Frameworks aus (siehe Kapitel 6.5), damit Prüfungen einen dokumentierten, verteidigbaren Prozess finden.

### Gesamtbetriebskosten berechnen und gegen Lock-in schützen

Modellieren Sie die vollen Lebenszykluskosten: Inferenz oder Lizenzierung, Datenpipelines, menschliche Prüfung, Überwachung, erneutes Training, Vorfallreaktion, und Außerbetriebnahme. Vergleichen Sie sie mit den Kosten des Status quo und der Alternativen. Reduzieren Sie Lock-in, indem Sie das Modell hinter eine interne Schnittstelle stellen, Prompts und Evaluationsdatensätze portabel halten, und von Zeit zu Zeit eine zweite Anbieterin testen.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile | Am besten wenn |
|---|---|---|---|
| Gehostetes Modell prompten | Schnell, günstig, keine Infrastruktur, leicht zu wechseln | Weniger Kontrolle, Pro-Aufruf-Kosten, Datenteilungsfragen | Prototypen, breite Aufgaben, unsichere Anforderungen |
| Retrieval-Erweiterung | Verankert Antworten in Ihren Daten, aktualisierbar | Retrieval-Qualität ist schwer, fügt Infrastruktur hinzu | Wissensschwere Aufgaben |
| Kleineres Modell fine-tunen | Kontrolle, niedrigere Pro-Aufruf-Kosten im Maßstab, On-Prem-Option | Braucht MLOps, Daten, und Instandhaltung | Stabile, hochvolumige, spezialisierte Aufgaben |
| Ein Produkt kaufen | Bewährt, unterstützt, schnell zu Wert | Lizenzkosten, Lock-in, begrenzte Passung | Gut definierte Commodity-Probleme |
| Foundation-Modell bauen | Maximale Kontrolle und Differenzierung | Enorme Kosten, seltenes Talent, hohes Risiko | Fast nie, außerhalb von Frontier-Labs |

Die dominante Abwägung ist Kontrolle gegen Kosten und Geschwindigkeit. Prompting gibt Ihnen die meiste Geschwindigkeit und Flexibilität, aber die wenigste Kontrolle; Bauen gibt Ihnen die meiste Kontrolle, fordert aber Ressourcen, die wenige Organisationen ausgeben sollten. Die meisten großen Teams sollten in der Mitte leben: zuerst prompten und abrufen, selektiv fine-tunen, und für Commodity-Bedürfnisse kaufen. Lock-in tauscht kurzfristige Bequemlichkeit gegen langfristiges Risiko, und das zählt besonders in Behörden, wo mehrjährige Ausstiegspflichten üblich sind.

## Fragen zur Diskussion mit Ihrem Team

1. **Wo sitzt jeder unserer drei Top-Kandidaten-Anwendungsfälle auf der Prompten-dann-Abrufen-dann-Fine-Tunen-dann-Kaufen-dann-Bauen-Leiter, und welcher Beleg würde ihn eine Sprosse bewegen?** Das zählt, weil die meisten verschwendeten KI-Ausgaben davon kommen, eine Sprosse zu hoch zu beginnen: ein Modell zu trainieren, wenn sorgfältiges Prompting funktioniert hätte. Für ein großes Team stoppt die Leiter als geteilten Standard zu vereinbaren, dass jede Gruppe eine teure Pipeline neu erfindet. Bringen Sie die Einseiten-Problemerklärung für jeden Kandidaten, die aktuelle Baseline, und eine ehrliche Lesart, ob die Lücke Wissen (Retrieval), Konsistenz (Fine-Tuning), oder eine gelöste Commodity (Kaufen) ist. In Unternehmens- und Behördenumgebungen fügen Sie die Beschaffungs- und Prüfungskosten jeder Sprosse hinzu, denn ein fine-getuntes Modell schleppt eine MLOps-Last mit, die ein gehosteter Aufruf nicht hat. Die Antwort sollte Ihnen erlauben, mindestens ein überdimensioniertes Projekt im Raum zu töten oder herabzustufen.

2. **Was ist unser konkreter Ausstiegsplan für die Anbieterin oder das Modell, von dem wir am meisten abhängen, und haben wir ihn tatsächlich getestet?** Lock-in ist günstig zu akzeptieren und teuer abzuwickeln, und in Behörden tragen Sie möglicherweise mehrjährige Ausstiegspflichten, die Sie nicht erfüllen können, wenn Sie sie nie geprobt haben. Bringen Sie die Liste proprietärer Features, auf die Sie sich verlassen, ob Prompts und Evaluationsdatensätze portabel sind, und wie das Modell hinter einer internen Schnittstelle sitzt (oder nicht). Das zu beobachtende Signal ist, ob jemals jemand Ihre Evaluationssuite gegen eine zweite Anbieterin durchgeführt hat; wenn nicht, ist Ihr Ausstiegsplan eine Hoffnung, kein Plan. Wenn die ehrliche Antwort ist, dass Wechseln Monate dauern und Kerncode umschreiben würde, behandeln Sie das als Designfehler, jetzt zu beheben, nicht als eine Brücke, später zu überqueren.

3. **Was sagt eine ehrliche Bereitschafts-Scorecard über unsere Datenrechte, und welche Anwendungsfälle disqualifiziert sie heute?** Datenbereitschaft zu überspringen ist der Fehlschlag, der Pilotprojekte still versenkt: das Modell funktioniert, aber Sie hatten nie die rechtliche Grundlage, die Daten zu nutzen, oder sie sind unbeschriftet und ohne Herkunftsnachweis. Für eine große Organisation werfen persönliche und Drittanbieterdaten Einwilligungs- und vertragliche Grenzen auf, die nach Rechtsprechung und Datensatz variieren. Bringen Sie eine Prüfung von Verfügbarkeit, Qualität, Beschriftung, Herkunft, und rechtlicher Grundlage für jeden Kandidaten, und seien Sie bereit, manche Anwendungsfälle als blockiert zu markieren, bis Datengrundlagen existieren. In regulierten und öffentlichen Umgebungen ist eine unbrauchbare rechtliche Grundlage keine Verzögerung, sie ist ein harter Stopp, und die Finanzierung der Bereitschaftsarbeit sollte eine explizite Zeile im Plan sein statt ein Nachgedanke.

4. **Wie werden wir wissen, dass ein lebender KI-Anwendungsfall tatsächlich funktioniert, und welcher Beleg würde uns ihn töten lassen?** Die meisten KI-Portfolios häufen Zombies an: Pilotprojekte, die ausgeliefert wurden, jemanden beeindruckten, und jetzt für immer laufen, ohne dass jemand prüft, ob sie ihre Kosten noch verdienen. Einigen Sie sich vor dem Start auf die Baseline und die Erfolgskennzahl, setzen Sie dann eine explizite Tötungsschwelle, damit die Entscheidung zu stoppen im Voraus getroffen wird statt im Moment verteidigt zu werden. Bringen Sie die aktuelle Kennzahl, die menschliche-Aufsicht-Kosten pro Ergebnis, und die Drift, die Sie seit dem Start gesehen haben. Für Unternehmens- und Behördenportfolios benennen Sie, wer jedes System in festem Takt überprüft und wer die Autorität hat, es auszumustern; ein Anwendungsfall, für dessen Überprüfung niemand rechenschaftspflichtig ist, ist einer, den niemand je abschalten wird.

5. **Wo bleibt ein Mensch im Loop, was kostet diese Aufsicht, und haben wir sie tatsächlich budgetiert?** Die günstigst aussehenden KI-Anwendungsfälle sind jene, die still volle Automatisierung annehmen, dann Kosten durch die Prüfung, Korrektur, und Eskalation lecken, die die Realität erzwingt. Entscheiden Sie absichtlich, welche Entscheidungen eine Person bestätigen muss, welche das Modell allein treffen darf, und welche es nie treffen darf, bepreisen Sie dann die menschliche Zeit, die das impliziert. Bringen Sie das Volumen niedrig-vertrauenswürdiger Fälle, die Kosten einer falschen Antwort, und den aktuellen Eskalationspfad. In regulierten und öffentlichen Umgebungen binden Sie jede automatisierte Entscheidung an eine rechenschaftspflichtige Beamtin und einen Beschwerdeweg, denn Aufsicht, die Sie nicht beschreiben können, ist Aufsicht, die Sie nicht haben.

6. **Haben wir das Talent und die Plattform, um zu betreiben, was wir vorschlagen, oder nehmen wir still Kapazität an, die uns fehlt?** Ambitionierte KI-Pläne scheitern weniger am Modell als an den unglamourösen Grundlagen: niemand, um die Pipeline zu pflegen, niemand, der Ausgaben evaluieren kann, keine Plattform, auf die deployt werden kann. Passen Sie jeden Kandidaten-Anwendungsfall an die Fähigkeiten und Infrastruktur an, die er tatsächlich braucht, und seien Sie ehrlich, wo die Lücke eine Einstellung, eine Partnerin, oder ein Grund ist, nicht zu bauen. Bringen Sie ein Inventar, wer jedes System in Produktion besitzen kann, auf welcher Plattform es laufen wird, und welche Fähigkeiten Sie kaufen müssten. Für eine große oder öffentliche Organisation fügen Sie die Beschaffungs- und Einstellungsvorlaufzeiten hinzu, denn ein Plan, der von Talent abhängt, das Sie nicht im relevanten Fenster rekrutieren können, ist ein Plan zur Unterlieferung.

## Branchenperspektive

**Startup.** Geschwindigkeit und Überleben dominieren. Wählen Sie einen engen Anwendungsfall, der Ihren Kernwert berührt, liefern Sie ihn auf einem gehosteten Modell hinter einer dünnen Schnittstelle aus, und deckeln Sie Ausgaben hart. Vermeiden Sie, Infrastruktur zu bauen oder Modelle zu trainieren: Ihre knappste Ressource ist Engineering-Aufmerksamkeit, und eine fine-getunte Pipeline, die Sie nicht pflegen können, ist eine Haftung, kein Burggraben. Halten Sie Wechsel günstig, damit Sie einem sich schnell bewegenden Markt folgen können.

**Kleinunternehmen.** Sie haben wahrscheinlich keine Datenwissenschaftlerinnen und ein enges Budget, behandeln Sie KI also als etwas, das Sie eingebettet in bereits genutzte Werkzeuge kaufen, kein Programm, das Sie besetzen. Rahmen Sie Bereitschaft als Datenhygiene- und Datenschutzfrage statt als Machine-Learning-Projekt: wissen Sie, welche Kundendaten Sie besitzen, was Sie damit tun dürfen, und wo eine falsche automatisierte Antwort Sie eine Kundin kosten würde. Bevorzugen Sie Anbieterinnen, die KI optional, transparent, und leicht abschaltbar machen.

**Großunternehmen.** Das Problem ist Portfolio-Governance über viele Teams: eine geteilte Bauen-versus-Kaufen-Leiter, konsistente Bereitschaftsbewertungen, und Lock-in- und Gesamtkosten-Analyse, damit Gruppen aufhören, teure Pipelines neu zu erfinden. Budgetieren Sie die MLOps- und menschliche-Aufsicht-Last explizit, standardisieren Sie die Schnittstellenschicht, damit Anbieterinnen austauschbar bleiben, und verwalten Sie KI-Anwendungsfälle als Portfolio mit klaren Kennzahlen und Tötungskriterien statt einer Streuung von Pilotprojekten.

**Behörde.** Transparenz, Beschaffungsregeln, und Rechenschaftspflicht formen jede Wahl. Bevorzugen Sie Systeme, die offizielle Quellen zitieren statt Richtlinie zu generieren, halten Sie eine Person für folgenreiche Entscheidungen rechenschaftspflichtig, und fordern Sie Datenportabilität und Offenlegung von Modelleinschränkungen in Verträgen. Veröffentlichen Sie eine Einfache-Sprache-Beschreibung und einen Beschwerdeweg, ehren Sie jede mehrjährige Ausstiegspflicht, die Sie unterzeichnen, und halten Sie KI aus finalen Bewertungsentscheidungen heraus, die bei einer rechenschaftspflichtigen Beamtin liegen müssen.

## Beispiele

**Startup.** Ein fünfköpfiges Terminplanungs-Startup wollte ein Natürliche-Sprache-"Buch mir ein Meeting"-Feature hinzufügen, ohne seine zwei Ingenieurinnen vom Kernprodukt abzuziehen. Es wählte das kleinste Problem, das zählte, eine Anfrage in eine vorgeschlagene Zeit zu parsen, und lieferte es mit einem gehosteten Modell hinter einer dünnen internen API aus, damit es später die Anbieterin wechseln konnte. Das Team setzte eine harte monatliche Ausgabengrenze, verfolgte, ob Nutzerinnen die vorgeschlagenen Zeiten akzeptierten, und einigte sich, ein fine-getuntes Modell nur zu überdenken, falls Volumen jemals den zusätzlichen Aufwand rechtfertigte.

**Großunternehmen.** Eine multinationale Versicherung wollte Schadenstriage beschleunigen. Statt ein maßgeschneidertes Modell zu trainieren, rahmte sie das Problem eng (eingehende Ansprüche routen und zusammenfassen), prototypte mit einem gehosteten Modell plus Retrieval über ihre Policendokumente, und maß gegen menschliche Bearbeitungszeit und Genauigkeit. Erst nachdem Wert bewiesen war, fine-tunte sie ein kleineres Modell für den höchstvolumigen Anspruchstyp, um Pro-Aufruf-Kosten zu senken. Sie hielt das Modell hinter einer internen API, damit sie Anbieterinnen austauschen konnte, und modellierte eine Drei-Jahres-Gesamtbetriebskosten-Rechnung, die menschliche Prüfung niedrig-vertrauenswürdiger Fälle einschloss.

**Behörde.** Eine nationale Steuerbehörde erwog eine KI-Assistentin, um Personal beim Beantworten von Bürgerinnenanfragen zu helfen. Weil diese Antworten rechtliche Pflichten berührten, bestand die Behörde auf Transparenz: das System konnte nur offizielle Leitlinien mit Zitaten zutage fördern, nie Richtlinie erfinden, und eine Person prüfte jeden automatisierten Vorschlag, bevor er hinausging. Beschaffung forderte von der Anbieterin, Modelleinschränkungen offenzulegen und Datenportabilität zu gewähren, und die Behörde veröffentlichte eine Einfache-Sprache-Beschreibung des Systems und einen Beschwerdeweg. Sie hielt KI vollständig aus finalen Bewertungsentscheidungen heraus, diese rechenschaftspflichtigen Beamtinnen vorbehaltend.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

KI-Strategie existiert, um Ihnen zu helfen, zwei spiegelbildliche Fehlschläge zu vermeiden: Überinvestition in KI, die sich nie auszahlt, und Unterinvestition, während Konkurrentinnen oder Partnerbehörden vorankommen. ROI kommt aus eingesparter Arbeit, reduzierter Zykluszeit, gesenkten Fehlerraten, und ermöglichten neuen Fähigkeiten. Messen Sie diese gegen eine echte Baseline, und diskontieren Sie für die echten Kosten menschlicher Aufsicht, die selten verschwindet.

Gesamtbetriebskosten müssen die unglamourösen Postenpunkte einschließen: Datenpipelines, Überwachung, erneutes Training, während die Welt driftet, Sicherheitsprüfung, und eventuelle Außerbetriebnahme. Ein Pilotprojekt, das günstig aussieht, kann teuer werden, sobald es jahrelang im Maßstab läuft. Präsentieren Sie auch die Kosten des *Nicht*-Übernehmens: langsamerer Dienst, höhere manuelle Kosten, und strategische Drift. Machen Sie den Fall gegenüber der Führung mit einer Portfolio-Ansicht: ein paar hochvertrauenswürdige Wetten, klare Erfolgskennzahlen, Tötungskriterien für Fehlschläge, und eine Bereitschaftsbewertung, die zeigt, dass Daten- und Talentgrundlagen existieren. Bitten Sie Führungskräfte, Bereitschaft explizit zu finanzieren; überspringen Sie das, und Sie garantieren teure Nacharbeit.

## Anti-Muster und Fallstricke

- **Lösung auf Problemsuche.** KI kaufen, weil Konkurrentinnen es taten, dann nach einem Anwendungsfall jagen.
- **Datenbereitschaft überspringen.** Modelle auf Daten starten, die unverfügbar, unbeschriftet, oder rechtlich unbrauchbar sind.
- **Demo-getriebene Entscheidungen.** Sich basierend auf einer polierten Demo verpflichten, ohne produktionsqualitative Evaluation.
- **Den menschlichen Loop ignorieren.** Volle Automatisierung annehmen und Prüfung unterbudgetieren, wo sich die meisten Kosten verstecken.
- **Stilles Lock-in.** Tief auf den proprietären Features einer Anbieterin bauen, ohne Ausstiegsplan.
- **Betrieb unterschätzen.** Deployment als Ziellinie behandeln statt als Beginn einer Pflegepflicht.
- **Compliance als Nachgedanke.** Transparenz und Prüfbarkeit nach dem Design nachrüsten, zu einem Vielfachen der Kosten.

## Reifegradmodell

1. **Beginnen.** Ad-hoc-Experimente, keine geteilte Strategie, Entscheidungen von Hype und individueller Begeisterung getrieben.
2. **Entwickeln.** Problemrahmung existiert für manche Projekte; eine erste Plattform-Baseline erscheint; Bauen-versus-Kaufen wird diskutiert, aber inkonsistent.
3. **Standardisieren.** Ein Portfolio von KI-Anwendungsfällen mit klaren Kennzahlen, einem dokumentierten Entscheidungsbaum, Bereitschaftsbewertungen, und Lock-in- und Gesamtkosten-Analyse, konsistent über Teams angewendet.
4. **Steuern.** Das Portfolio wird gemessen: Bereitschaft, ROI, Gesamtbetriebskosten, und menschliche-Aufsicht-Kosten werden gegen Baselines verfolgt; Tötungskriterien werden auf Beleg durchgesetzt; Liefer- und Qualitätswirkung treiben jede Go-oder-No-go-Entscheidung.
5. **Orchestrieren.** KI-Strategie ist mit Geschäfts- und Risikoplanung integriert; Bereitschaft wird kontinuierlich gepflegt; die Organisation mustert routinemäßig KI-Systeme auf Beleg aus, ersetzt sie, und rahmt sie neu, das Portfolio neu balancierend, während sich der Markt und das Risikobild verschieben.

## Diskussionsideen

- Wie entscheiden Sie, wann ein Problem wirklich ungeeignet für KI ist, und wer hat die Autorität, Nein zu sagen?
- Welche Bereitschaftsschwelle sollte ein Projekt vom Pilotprojekt zur Produktion torwächten?
- Wie viel Lock-in ist akzeptabel im Austausch für schnellere Zeit bis zum Wert?
- Wie sollten in Behörden Transparenzpflichten die Bauen-versus-Kaufen-Wahl formen?
- Wie halten Sie Gesamtbetriebskosten-Schätzungen ehrlich, wenn Anbieterinnen und Enthusiastinnen Anreize haben, sie zu unterschätzen?
- Wer besitzt das KI-Portfolio, und wie werden Tötungsentscheidungen getroffen?

## Wichtigste Erkenntnisse

- Strategie beginnt mit einem echten Problem und einer ehrlichen Baseline, nicht mit einer Technologie.
- Bevorzugen Sie die einfachste Option: prompten, dann abrufen, dann fine-tunen, dann kaufen, und selten von Grund auf bauen.
- Daten-, Talent-, und Plattformbereitschaft sind Voraussetzungen; sie zu finanzieren ist Teil des Plans.
- Regulierte und Behördenkontexte fordern Transparenz, Beschaffungskonformität, und Ausstiegsoptionen durch Design.
- Modellieren Sie volle Gesamtbetriebskosten und die Kosten der Untätigkeit, und schützen Sie sich von der ersten Architekturentscheidung an gegen Anbieter-Lock-in.

## Referenzen und weiterführende Literatur

- Ajay Agrawal, Joshua Gans, und Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*
- Andriy Burkov, *The Hundred-Page Machine Learning Book*
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*
- Organisation for Economic Co-operation and Development, *OECD AI Principles*
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*
