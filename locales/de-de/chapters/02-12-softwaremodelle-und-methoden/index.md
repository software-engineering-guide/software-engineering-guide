# 2.12 Softwaremodelle und -methoden

## Überblick und Motivation

Ein Softwaremodell ist eine bewusste Vereinfachung eines Systems, gebaut, um eine spezifische Frage zu beantworten. Eine Methode ist ein disziplinierter Weg, Software zu produzieren, einschließlich der Modelle, die sie unterwegs nutzt. Zusammen bilden sie einen Wissensbereich des Software Engineering Body of Knowledge (SWEBOK), denn sie sind die mentalen Werkzeuge, mit denen Sie über ein System nachdenken, bevor, während, und nachdem Sie es bauen. Ein UML- ([Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)) Klassendiagramm, ein [Entity-Relationship-Diagramm](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), eine [Zustandsmaschine](https://en.wikipedia.org/wiki/Finite-state_machine), eine [formale Spezifikation](https://en.wikipedia.org/wiki/Formal_specification), und ein Wegwerf-Prototyp sind alle Modelle. [Wasserfall](https://en.wikipedia.org/wiki/Waterfall_model), [Prototyping](https://en.wikipedia.org/wiki/Software_prototyping), formale Entwicklung, und [Agile](https://en.wikipedia.org/wiki/Agile_software_development) sind alle Methoden.

Warum sich überhaupt mit Modellen abmühen? Weil menschliches Arbeitsgedächtnis klein ist und Softwaresysteme groß sind. Niemand kann ein hunderttausend-Zeilen-System im Kopf behalten, wir zeichnen also Bilder und schreiben Abstraktionen, die eine Facette auf einmal zeigen: die Daten, den Kontrollfluss, die Zustände, die Interaktionen. Ein Modell soll nie dem Code treu sein; es soll für eine Entscheidung geeignet sein. Ein gutes Modell zeigt genau, was Sie brauchen, um etwas zu entscheiden, und verbirgt alles andere.

In großen Teams sind die echten Einsätze Koordination und Kommunikation. Wenn Hunderte Ingenieurinnen, Architektinnen, Analystinnen, und Prüferinnen an einem System arbeiten, sind gemeinsame Modelle der gemeinsame Boden, auf dem sie Design, Anforderungen, und Risiko aushandeln. Betrachten Sie Modellieren also als Werkzeug mit einer Aufgabe zu erledigen. Es zahlt sich aus, wenn ein Modell günstiger ist als der Fehler, den es verhindert. Es wird zu Verschwendung, wenn Sie es um seiner selbst willen zeichnen, es lange nach dem Veralten behalten, oder es über die Entscheidung hinaus ausarbeiten, der es dienen sollte. Modellierung verbindet sich eng mit Softwareanforderungen (Kapitel 2.8), Softwaredesignprinzipien (Kapitel 2.2), Architektur und ihren Notationen wie C4 und arc42 (Kapitel 3.1), und agilen Arbeitsweisen (Kapitel 10.7).

## Kernprinzipien

- Jedes Modell hat einen Zweck; wenn Sie die Entscheidung, die ein Modell informiert, nicht benennen können, zeichnen Sie es nicht.
- Abstraktion ist der Kernakt des Modellierens: einschließen, was für den Zweck zählt, den Rest weglassen.
- Konsistenz zählt innerhalb und über Modelle hinweg; widersprüchliche Modelle sind schlimmer als keine.
- Modelle sind zuerst Kommunikationsartefakte; ihr Publikum bestimmt ihre Notation und ihr Detail.
- Bevorzugen Sie das leichteste Modell, das die Frage beantwortet; Ausarbeitung hat Trägkosten.
- Ein Modell ist nur so gut wie seine Analyse; ein ungeprüftes Modell ist eine ungetestete Annahme.
- Wählen Sie die Methode passend zu Unsicherheit, Risiko, und Folgen des Scheiterns des Problems.

## Empfehlungen

### Mit Abstraktion, Zweck, und Konsistenz modellieren

Beginnen Sie jedes Modell damit, seinen Zweck und sein Publikum zu benennen. Abstrahieren Sie dann rücksichtslos zu diesem Zweck hin: Ein Sequenzdiagramm, das eine Race Condition auflösen soll, sollte Timing und Nachrichten zeigen, nicht jedes Feld. Halten Sie Ihre Modelle untereinander konsistent, damit die Entitäten in einem ERD, die Klassen in einem Klassendiagramm, und die Substantive in den Anforderungen alle übereinstimmen, und konsistent mit der Realität, was bedeutet, Sie aktualisieren oder löschen ein Modell, wenn sich das System weiterentwickelt. Ein veraltetes Modell, dem Menschen vertrauen, ist eine Gefahr. Ein veraltetes Modell, das alle ignorieren, ist Verschwendung, die noch Aufmerksamkeit kostet.

### Strukturelle oder Verhaltensmodelle passend zur Frage wählen

Nutzen Sie strukturelle Modelle, um zu zeigen, woraus ein System besteht und wie die Teile sich beziehen: Klassendiagramme, Komponentendiagramme, und Entity-Relationship-Diagramme für Datenstruktur. Nutzen Sie Verhaltensmodelle, um zu zeigen, was ein System über Zeit tut: Zustandsmaschinen für Objekte mit bedeutsamen Lebenszyklen, Sequenzdiagramme für Interaktionen über Komponenten, und Aktivitätsdiagramme für Workflows und Geschäftsprozesse. Wählen Sie die eine Notation, die die Entscheidung vor Ihnen offenlegt. Die meisten Systeme brauchen nur eine Handvoll Diagrammtypen, selektiv gezeichnet, nicht den vollständigen UML-Katalog auf alles angewendet.

### Modelle analysieren, nicht nur zeichnen

Ein Modell verdient seinen Unterhalt durch Analyse, nicht nur durch Zeichnen. Prüfen Sie eine Zustandsmaschine auf unerreichbare Zustände, fehlende Übergänge, und Deadlock. Prüfen Sie ein ERD auf Normalisierungsprobleme und verwaiste Beziehungen. Gehen Sie ein Sequenzdiagramm gegen die Anforderungen durch, um fehlende Fehlerpfade zu finden. Prüfen Sie Ihre Modelle mit den Domänenexpertinnen, die erkennen können, was falsch ist. Und wo die Kosten des Scheiterns hoch sind, greifen Sie zu werkzeugunterstützter Analyse (Modellprüfer, Konsistenzprüfer, Simulation) statt es mit bloßem Auge zu beurteilen.

### Heuristische Methoden als Standard anwenden

Die meiste Software wird mit heuristischen Methoden gebaut: erfahrungsbasierten, iterativen Ansätzen, die Modelle informell nutzen und Ergebnisse gegen Erwartungen statt Beweise beurteilen. Für die meisten Geschäfts- und Behördensysteme ist das genau richtig: Anforderungen entwickeln sich, und ein Fehler ist normalerweise behebbar. Heuristische Methoden koppeln sich natürlich mit Agile (Kapitel 10.7): Modellieren Sie gerade genug, um das Team auszurichten, dann bauen und lernen.

### Formale Methoden für folgenreiche Kerne reservieren

[Formale Methoden](https://en.wikipedia.org/wiki/Formal_methods) drücken Spezifikationen in Mathematik aus und nutzen Verifikation, sei es Beweis oder erschöpfendes [Model Checking](https://en.wikipedia.org/wiki/Model_checking), um Eigenschaften zu etablieren. Sie kosten echte Fähigkeit und Zeit, und sie zahlen sich genau dort aus, wo Scheitern katastrophal oder unumkehrbar ist: sicherheitskritische Steuerung, kryptografische Protokolle, Finanzabwicklungskerne, und Ähnliches. Wenden Sie sie auf den kleinen kritischen Kern an, nicht das ganze System. Und beachten Sie, dass formale Spezifikation allein, selbst ohne vollen Beweis, oft Wert hinzufügt, indem sie Sie einfach zwingt, präzise zu sein.

### Prototyping nutzen, um Unsicherheit auszuräumen

Wenn Anforderungen oder Machbarkeit unklar sind, bauen Sie einen Prototyp, um zu lernen, entscheiden Sie dann absichtlich, ob Sie ihn weiterentwickeln oder verwerfen. Wegwerf-Prototypen erforschen eine Frage günstig und werden dann gelöscht. Evolutionäre Prototypen werden zum Produkt und müssen nach Produktionsstandards gebaut werden. Der klassische Fehler ist, einen Wegwerf-Prototyp versehentlich in Produktion rutschen zu lassen. Benennen Sie also den Typ des Prototyps, bevor Sie ihn bauen.

### Die Methode an Risiko anpassen, nicht an Mode

Wählen Sie Methoden nach der Unsicherheit des Problems und den Folgen des Scheiterns. Hohe Unsicherheit bevorzugt Prototyping und agile Iteration. Hohe Folgen bevorzugen formale Analyse und strenge Verifikation. Ein System mit beidem braucht einen kritischen formalen Kern innerhalb einer sonst agilen Hülle. Was auch immer Sie tun, übernehmen Sie keine Methode nur, weil sie prestigeträchtig ist oder weil ein Zulieferer sie verkauft.

## Abwägungen: Vor- und Nachteile

| Modell oder Methode | Gut angewendet | Versagensmodus |
|---|---|---|
| Strukturelle Modelle (UML, ERD) | Gemeinsames Bild von Teilen und Daten | Diagrammwucherung; Drift vom Code |
| Verhaltensmodelle (Zustand, Sequenz, Aktivität) | Legt Timing, Zustände, und Randfälle offen | Überdetaillierte Diagramme, die niemand liest |
| Heuristische Methoden | Schnell, flexibel, passt zu den meisten Systemen | Undiszipliniert; versteckte Annahmen |
| Formale Methoden | Beweisbare Eigenschaften für kritische Kerne | Hohe Kosten; falsch auf das ganze System angewendet |
| Prototyping | Günstiges Lernen; räumt Risiko früh aus | Wegwerf-Code, zur Produktion befördert |
| Agile Methoden | Passt sich ändernden Anforderungen an | Überspringt Modellierung, die für schwierige Probleme nötig ist |

Die wiederkehrende Spannung ist zwischen Strenge und Geschwindigkeit. Zu wenig Modellierung liefert versteckte Annahmen in Produktion. Zu viel Modellierung verbrennt Aufwand an Diagramme, die nie eine Entscheidung informieren und in dem Moment verrotten, in dem sich der Code ändert. Es gibt keine feste Dosis, die das behebt, nur eine Proportionsregel: Investieren Sie in ein Modell oder eine Methode proportional zur Unsicherheit, die es auflöst, und den Kosten, die Entscheidung falsch zu treffen. Eine Zahlungs-Engine und eine Marketing-Microsite verdienen unterschiedliche Behandlung.

## Fragen zur Diskussion mit Ihrem Team

1. **Analysieren wir unsere Modelle, oder zeichnen wir sie nur und machen weiter?** Ein Modell verdient seinen Unterhalt durch Analyse, nicht durch Existenz: eine Zustandsmaschine, die Sie nie auf unerreichbare Zustände oder fehlende Übergänge prüfen, ist eine ungetestete Annahme, verkleidet als Diagramm. In einem großen Team verstecken sich hier echte Fehler, denn ein plausibel aussehendes Bild wird genau dann vertraut, wenn niemand es gegen die Anforderungen durchgegangen ist, um den fehlenden Fehlerpfad oder die verwaiste Beziehung zu finden. Bringen Sie Ihr wichtigstes Verhaltensmodell zur Besprechung und versuchen Sie, es zu brechen: Welcher Übergang ist undefiniert, welcher Zustand hat keinen Ausgang, welche Sequenz hat kein Timeout? Wo die Kosten des Scheiterns hoch sind, sollte die Antwort Sie zu werkzeugunterstützter Analyse drängen (Modellprüfer, Konsistenzprüfer, Simulation) statt bloßem Augenschein, denn der ganze Grund, einen kritischen Kern zu modellieren, ist, den Fehler an einem Whiteboard zu finden statt in Produktion.

2. **Wenn zwei unserer Modelle widersprechen, welches gewinnt, und wer bemerkt den Widerspruch?** Konsistenz zählt innerhalb und über Modelle hinweg, und widersprüchliche Modelle sind schlimmer als keine, denn Menschen handeln nach beiden. In einem großen System driften die Entitäten im Datenmodell, die Klassen im Design, und die Substantive in den Anforderungen still auseinander, während verschiedene Teams verschiedene Artefakte aktualisieren, und das erste Zeichen ist oft ein Produktionsfehler, wo zwei Komponenten nicht übereinstimmten, was ein Ding ist. Bringen Sie ein Beispiel: Wählen Sie ein Kernkonzept und prüfen Sie, ob das ERD, der Code, und die Anforderungen tatsächlich über seine Form und seinen Lebenszyklus übereinstimmen. Wenn nicht, entscheiden Sie, welches Artefakt autoritativ ist und wer verantwortlich ist, die anderen im Gleichschritt zu halten, und seien Sie bereit, ein Modell zu löschen, statt ein veraltetes das Team weiter belügen zu lassen.

3. **Welcher Kern in unserem System verliert echtes Geld oder schadet jemandem, wenn er falsch ist, und bekommt er die Strenge, die er verdient?** Der zentrale Zug dieses Kapitels ist, die Methode an Risiko anzupassen: heuristische und agile Methoden für die behebbare Mehrheit, formale Spezifikation und Verifikation für den kleinen folgenreichen Kern, und günstiges Prototyping für das wirklich Unsichere. Die Versagensmodi sind symmetrisch und beide teuer: formale Methoden auf eine Marketing-Microsite anzuwenden verbrennt Geld, und eine Abwicklungs-Engine oder ein Berechtigungsregelsatz als gewöhnliche agile Arbeit zu behandeln lädt den katastrophalen, unumkehrbaren Fehler ein. Bringen Sie eine Karte Ihres Systems und markieren Sie, wo ein Fehler katastrophal gegenüber behebbar ist, und wo Anforderungen sicher gegenüber unbekannt sind. Die Antwort sollte Ihre Modellierungsinvestition dort konzentrieren, wo das Geld und die Mehrdeutigkeit sind, und sie explizit überall sonst vorenthalten, damit ein kritischer formaler Kern innerhalb einer sonst agilen Hülle sitzen kann, ohne dass eine Methode in das Territorium der anderen sickert.

4. **Wie viel Modellierung machen wir, bevor wir Code schreiben, und ändert sich diese Dosis mit der Unsicherheit vor uns?** Großes Vorabdesign und gar kein Design sind beide Versagensmodi, und die richtige Dosis sitzt dazwischen, gesteuert davon, wie viel Unsicherheit ein Modell tatsächlich ausräumt. In einem großen Team läuft der Druck in beide Richtungen: Ein Governance-Prozess mag einen vollständigen Satz Diagramme vor jedem Code verlangen, Entscheidungen mit der geringsten Information einsperrend, während Lieferdruck ein Team drängen mag, die eine Zustandsmaschine zu überspringen, die einen teuren Randfall erwischt hätte. Bringen Sie Ihre letzten zwei Projekte und sortieren Sie die produzierten Modelle in jene, die eine echte Entscheidung informierten, und jene, die nur gezeichnet wurden, weil eine Vorlage danach fragte. In Unternehmens- und Behördenprogrammen, wo ein Phasentor oder Genehmigungsgremium oft Dokumente vorab vorschreibt, kommen Sie bereit, für Modellierung zu argumentieren, die Risiko verfolgt statt einer festen Liefergegenstandsliste, damit der Zahlungskern seine Strenge bekommt und das interne Berichtswerkzeug nicht in Diagrammen ertrinkt, die niemand liest.

5. **Haben wir uns auf eine gemeinsame Notation und ein einziges Zuhause für unsere Modelle geeinigt, oder erfindet jedes Team seine eigene?** Modelle sind zuerst Kommunikationsartefakte, und ihr Wert bricht zusammen, wenn eine im Werkzeug eines Teams gezeichnete Zustandsmaschine vom Team, das sie erbt, nicht gelesen, gefunden, oder vertraut werden kann. Für Hunderte Ingenieurinnen sind die konkurrierenden Erwägungen real: eine vorgeschriebene Notation und ein Repository erkaufen Konsistenz und Auffindbarkeit, erlegen aber auch Lernkosten auf und können Menschen zu schwergewichtigen Werkzeugen drängen, wenn ein fotografiertes Whiteboard dienen würde. Bringen Sie Beispiele, wo ein Modell tatsächlich lebte (ein Wiki, ein Diagrammwerkzeug, ein Foliensatz, jemandes Laptop), und fragen Sie, wer es sechs Monate später finden und verstehen konnte. In Unternehmens- und regulierten Umgebungen schärft der Prüfungswinkel das: Eine Prüferin, die das aktuelle Datenmodell nicht lokalisieren oder eine Entscheidung nicht zu einer dokumentierten Zustandsmaschine zurückverfolgen kann, wird das System als undokumentiert behandeln, vereinbaren Sie also eine kleine gemeinsame Notation und einen dauerhaften Ort, und akzeptieren Sie leichtgewichtiges Erfassen über Zeremonie, wo immer die Folge gering ist.

6. **Bevor wir einen Prototyp bauen, entscheiden wir bewusst, ob er Wegwerf oder evolutionär ist, und halten wir uns an diese Wahl?** Der klassische, teure Fehler ist ein Wegwerf-Prototyp, der still in Produktion rutscht, weil er gut demonstrierte und niemand seinen Typ vorab benannte. Die Spannung ist echt: Wegwerf-Prototypen erkaufen das günstigste mögliche Lernen und sollten gelöscht werden, während evolutionäre Prototypen zum Produkt werden und ab der ersten Zeile nach Produktionsstandards gebaut werden müssen, und die beiden zu verwechseln verschwendet entweder Nacharbeit oder liefert zerbrechlichen Code in eine Rolle, für die er nie konstruiert wurde. Bringen Sie einen jüngsten Prototyp und fragen Sie, was entschieden wurde, bevor er gebaut wurde, wer die Autorität hatte, ihn zu befördern oder zu verwerfen, und ob diese Entscheidung Lieferdruck überlebte. In Behörden und anderen rechenschaftspflichtigen Umgebungen, wo ein bürgerorientiertes System Transparenz- und Zuverlässigkeitspflichten trägt, behandeln Sie versehentliche Beförderung als Kontrollversagen: Legen Sie das Schicksal des Prototyps im Voraus fest, und machen Sie das Verwerfen eines erfolgreichen Wegwerfs zu einem gefeierten Ergebnis statt einer zu vermeidenden Verschwendung.

## Branchenperspektive

**Startup.** Modellieren Sie auf einem Whiteboard, fotografieren Sie es, und machen Sie weiter. Ihre knappste Ressource ist technische Aufmerksamkeit, greifen Sie also nur zu einem Modell, wenn es günstiger ist als der Fehler, den es verhindert: eine Abonnement-Zustandsmaschine, bevor Sie die Abrechnungsrandfälle codieren, nicht ein vollständiger UML-Katalog für ein Produkt, das nächsten Monat pivotieren mag. Bleiben Sie heuristisch und agil, halten Sie formale Methoden ganz vom Tisch, und behandeln Sie jeden Prototyp als Wegwerf, sofern Sie nicht bewusst anders entscheiden.

**Kleinunternehmen.** Sie haben wahrscheinlich niemanden, dessen Job formale Modellierung ist, stützen Sie sich also auf die bereits in die Werkzeuge und Frameworks eingebetteten Modelle, die Sie kaufen, statt eine eigene Modellierungspraxis aufzustellen. Rahmen Sie die wenigen Modelle, die Sie zeichnen, um konkrete Entscheidungen: eine einfache Datenmodellskizze, um zu vereinbaren, welche Kundendaten Sie halten, ein Zustandsdiagramm für den einen Workflow, der Sie eine Kundin kostet, wenn er bricht. Bevorzugen Sie ein gekauftes Produkt mit bewährtem Datenmodell gegenüber dem Bauen und Dokumentieren eines eigenen, und halten Sie, was Sie zeichnen, leicht genug, dass eine Person es pflegen kann.

**Großunternehmen.** Das Kernproblem ist Koordination über viele Teams, gemeinsame Modelle werden also zum gemeinsamen Boden: ein vereinbartes Datenmodell, eine konsistente Notation, und ein Zuhause, wo das ERD, die C4-Diagramme, und die Zustandsmaschinen gefunden und vertraut werden können. Standardisieren Sie eine kleine Notation und setzen Sie Konsistenz durch, damit die Entitäten in Anforderungen, Design, und Datenbank nicht zwischen Teams auseinanderdriften. Reservieren Sie formale Spezifikation und Model Checking für die folgenreichen Kerne (Abwicklung, Abstimmung, Zugriffskontrolle), finanzieren Sie das verlangte Spezialistenkönnen, und halten Sie eine Prüfspur von jedem dokumentierten Modell zurück zur Entscheidung, die es rechtfertigte.

**Behörde.** Im Gesetz festgelegte Regeln müssen zum Gesetz nachvollziehbar sein, wo formale Spezifikation ihre Kosten verdient: Spezifizieren Sie Berechtigungs- oder Bewertungslogik präzise, verifizieren Sie Schlüsseleigenschaften, und lassen Sie Prüfer jedes Ergebnis zur Regel zurückverfolgen, die es produzierte. Beschaffung fügt ihr eigenes Gewicht hinzu, da Dokumente und Modelle oft vertragliche Liefergegenstände sind, vereinbaren Sie also, welche Modelle wirklich entscheidungstragend sind statt nur produziert, um eine Checkliste zu erfüllen. Veröffentlichen Sie klarsprachige Beschreibungen davon, wie folgenreiche Systeme funktionieren, und nutzen Sie Wegwerf-Prototyping, um bürgerorientierte Aufnahme mit echten Nutzerinnen zu testen, bevor Sie sich zu einem Produktionsbau verpflichten.

## Beispiele

**Startup.** Ein kleines Startup, das ein Abonnement-Abrechnungsprodukt baut, skizziert den Abonnementlebenszyklus (Testphase, aktiv, überfällig, gekündigt, reaktiviert) als Zustandsmaschine auf einem Whiteboard, bevor Code geschrieben wird. Beim Durchgehen des Diagramms bemerken sie, dass sie nie definiert haben, was geschieht, wenn die Zahlung eines überfälligen Kontos endlich klärt, ein Randfall, der echte Kundinnen in der Schwebe gestrandet hätte. Dieses fünfminütige Modell erspart einen Produktionskopfschmerz, und sie fotografieren es statt ein schwergewichtiges Diagrammwerkzeug zu pflegen. Überall sonst bleiben sie agil und modellieren gerade genug zur Ausrichtung, denn bei ihrer Größe ist ein Fehler behebbar und formale Methoden wären reine Kosten.

**Großunternehmen.** Eine globale Bank baut eine neue Zahlungsplattform. Das Team nutzt ein Entity-Relationship-Diagramm, um sich auf das gemeinsame Datenmodell über die Konten-, Hauptbuch-, und Nachrichtenteams zu einigen, und C4-Diagramme (Kapitel 3.1), um zu zeigen, wie die Dienste zusammenpassen. Sie modellieren den Transaktionslebenszyklus (ausstehend, geklärt, abgewickelt, storniert, angefochten) als explizite Zustandsmaschine, und Analyse zeigt, dass ein Übergang für Teilstornierungen fehlt. Die Lücke wird an einem Whiteboard behoben statt in Produktion. Sequenzdiagramme gehen den Abwicklungsfluss gegen die Anforderungen (Kapitel 2.8) durch, um fehlende Timeout- und Wiederholungspfade ans Licht zu bringen. Die tägliche Lieferung ist agil, aber der Kern-Abstimmungsalgorithmus, wo ein Fehler echtes verlorenes Geld bedeutet, bekommt eine formale Spezifikation und wird vor der Implementierung model-geprüft. Modellierung ist konzentriert, wo das Geld und die Mehrdeutigkeit sind, und bleibt überall sonst leicht.

**Behörde.** Eine nationale Steuerbehörde modernisiert Leistungsbewertung. Weil Berechtigungsregeln gesetzlich festgelegt und geprüft sind, schreibt das Team eine formale Spezifikation der Regeln als reine Transformationen und verifiziert Schlüsseleigenschaften, wie dass kein Antragsteller sowohl berechtigt als auch unberechtigt ist und jeder Fall eine Entscheidung erreicht, damit Prüfer Ergebnisse zum Gesetz zurückverfolgen können. Neben dem formalen Kern baut das Team einen Wegwerf-Prototyp des bürgerorientierten Aufnahmeformulars, um mit echten Nutzerinnen zu testen. Sie lernen, dass ein mehrstufiger Assistent Fehler reduziert, verwerfen dann den Prototyp und bauen die Aufnahme nach Produktionsstandards neu. Aktivitätsdiagramme dokumentieren den End-zu-Ende-Sachbearbeiterprozess für Training und Prüfung. Die folgenreichen Regeln bekommen formale Strenge; die unsichere Nutzererfahrung bekommt günstiges Prototyping; keine Methode wird angewendet, wo die andere hingehört.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Rendite von Modellierung kommt vom früheren Finden von Fehlern, wo sie weit günstiger zu beheben sind. Ein an einem Whiteboard gefundener Widerspruch kostet Minuten. Derselbe in Produktion gefundene Widerspruch kann einen Ausfall, ein Nacharbeitsprogramm, oder, in regulierten Domänen, eine rechtliche Haftung kosten. Modelle senken auch die Gesamtbetriebskosten, indem sie als dauerhafte Kommunikation dienen. Ein System, das seine Autoren überlebt, der Normalfall in Unternehmen und Behörden, ist weit günstiger zu pflegen, wenn sein Datenmodell, seine Zustandsmaschinen, und Schlüsselflüsse genau dokumentiert sind.

Die Kosten sind real, und Sie müssen sie abwägen. Modelle brauchen Zeit zu bauen, Fähigkeit, um sie gut zu bauen, und laufenden Aufwand, sie aktuell zu halten; formale Methoden fügen Spezialistenarbeit hinzu. Der Break-Even-Punkt wird von Unsicherheit und Folgen gesteuert. Wo beide niedrig sind, zerstört schwere Modellierung Wert, und agile Heuristiken gewinnen. Wo eines hoch ist, zahlt sich gezielte Modellierung, und, für den kritischen Kern, formale Verifikation, vielfach aus, indem sie die teure Fehlerklasse verhindert. Um Führungskräften den Fall darzulegen, verknüpfen Sie Modellierungsinvestition mit spezifisch ausgeräumten Risiken und mit der Wartbarkeit langlebiger Systeme. Und verfolgen Sie, ob Modelle tatsächlich konsultiert werden, denn ein ungenutztes Modell ist reine Kosten.

## Anti-Muster und Fallstricke

- **Modellieren um seiner selbst willen:** Diagramme produzieren, weil ein Prozess sie verlangt, nicht weil sie eine Entscheidung informieren.
- **Veraltete Modelle, denen als Wahrheit vertraut wird:** Diagramme, die nicht mehr dem Code entsprechen, denen aber noch vertraut wird.
- **Großes Vorabdesign:** erschöpfende Modelle, produziert vor jedem Code, Entscheidungen einsperrend, die mit der geringsten Information getroffen wurden.
- **Diagrammwucherung:** jeder UML-Typ einheitlich angewendet, die wenigen nützlichen Ansichten in Rauschen ertränkend.
- **Formale Methoden überall:** teure Verifikation auf Code anwenden, wo die Folgen des Scheiterns es nicht rechtfertigen.
- **Versehentliche Prototyp-Beförderung:** ein Wegwerf-Prototyp, still als Produkt ausgeliefert.
- **Notation über Substanz:** über UML-Korrektheit streiten statt darüber, ob das Modell die Frage beantwortet.

## Reifegradmodell

- **Stufe 1 (Beginnen):** Modellierung ist ad hoc oder abwesend und rein reaktiv; keine Methode wird benannt; Modelle, wenn überhaupt gezeichnet, sind uneinheitlich, unanalysiert, und aufgegeben, sobald die Besprechung endet.
- **Stufe 2 (Entwickeln):** Manche Teams zeichnen gängige Diagramme und folgen einer benannten Methode, aber die Praxis ist über die Organisation uneinheitlich: Modelle werden oft zeremoniell produziert, driften vom Code weg, und werden selten auf Fehler analysiert.
- **Stufe 3 (Standardisieren):** Eine gemeinsame Notation, ein dokumentierter Methodenwahlleitfaden, und Konsistenzregeln sind definiert und organisationsweit durchgesetzt; Modelle werden nach Zweck gewählt, mit dem System im Gleichschritt gehalten, auf Fehler geprüft, und die Methode wird an das Risiko jedes Problems angepasst.
- **Stufe 4 (Steuern):** Modellierung wird gegen Baselines gemessen und gesteuert; Teams verfolgen, wie viele Fehler Analyse vor der Implementierung erwischt, wie weit Modelle vom Code driften, ob jedes Modell tatsächlich für eine echte Entscheidung konsultiert wurde, und die gegenüber einer definierten Baseline gesparte Nacharbeit und Zykluszeit; Methodenwahl wird an gemessene Unsicherheit und Folgen kalibriert, und kritische Kerne werden formal gegen vereinbarte Abdeckungsziele verifiziert.
- **Stufe 5 (Orchestrieren):** Modellierung und Methodenwahl werden kontinuierlich verbessert und mit Liefer- und Risikoplanung über die Organisation integriert; Investition passt sich an, während sich Unsicherheit und Folgen verschieben, Modelle werden routinemäßig aktuell gehalten, ausgemustert, oder vertieft aufgrund von Belegen, und formale, heuristische, und Prototyping-Methoden werden so zusammengesetzt, dass jede genau dort sitzt, wo sie sich auszahlt.

## Diskussionsideen

- Welche Modelle in Ihrem letzten Projekt informierten eine echte Entscheidung, und welche wurden nur gezeichnet, weil ein Prozess es verlangte?
- Wo in Ihren Systemen würde sich eine formale Spezifikation auszahlen, und wo wäre sie Verschwendung?
- Wie entscheiden Sie, ob ein Prototyp Wegwerf oder evolutionär ist, und setzen Sie diese Entscheidung durch?
- Wie verhindern Sie, dass Modelle aus dem Gleichschritt mit dem Code geraten, oder akzeptieren Sie, dass manche stattdessen gelöscht werden sollten?
- Was ist die richtige Menge Modellierung vor Code in Ihrem Kontext, und wie ändert sie sich mit Unsicherheit?
- Welches Verhaltensmodell (Zustand, Sequenz, oder Aktivität) hätte Ihren jüngsten Produktionsvorfall erwischt?

## Wichtigste Erkenntnisse

- Ein Modell ist eine zweckvolle Abstraktion; wenn Sie die Entscheidung, die es informiert, nicht benennen können, zeichnen Sie es nicht.
- Passen Sie strukturelle und Verhaltensmodelle an die spezifische Frage an, und halten Sie sie konsistent und aktuell.
- Analysieren Sie Modelle; ein ungeprüftes Modell ist eine ungetestete Annahme.
- Heuristische und agile Methoden passen zu den meisten Systemen; reservieren Sie formale Methoden für folgenreiche Kerne.
- Nutzen Sie Prototypen, um Unsicherheit auszuräumen, und entscheiden Sie vorab, ob sie Wegwerf oder evolutionär sind.
- Investieren Sie in Modellierung proportional zur Unsicherheit, die sie auflöst, und den Kosten, die Entscheidung falsch zu treffen.

## Referenzen und weiterführende Literatur

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Wissensbereich Softwaremodelle und -methoden
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modeling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modeling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* und *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (die Alloy-Modellierungssprache)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (das C4-Modell)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
