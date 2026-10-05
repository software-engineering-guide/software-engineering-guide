# 2.2 Prinzipien des Softwaredesigns

## Überblick und Motivation

Prinzipien des Softwaredesigns sind Heuristiken zum Anordnen von Code, damit Sie ihn über Zeit verstehen, ändern, und erweitern können. Sie umfassen benannte Akronyme ([SOLID](https://en.wikipedia.org/wiki/SOLID) für fünf [objektorientierte](https://en.wikipedia.org/wiki/Object-oriented_programming) Designprinzipien, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) für wiederhole-dich-nicht, [KISS](https://en.wikipedia.org/wiki/KISS_principle) für halte-es-einfach, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) für du-wirst-es-nicht-brauchen), strukturelle Konzepte ([Kopplung](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [Kohäsion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [Trennung von Belangen](https://en.wikipedia.org/wiki/Separation_of_concerns)), katalogisierte [Designmuster](https://en.wikipedia.org/wiki/Software_design_pattern), höherstufige Modellierungsansätze wie [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (Software in der Sprache der Geschäftsdomäne modellieren), und die Wahl zwischen objektorientierten, [funktionalen](https://en.wikipedia.org/wiki/Functional_programming), und [datenorientierten](https://en.wikipedia.org/wiki/Data-oriented_design) Stilen. Keines davon sind Gesetze. Sie sind komprimierte Erfahrung, und Sie müssen sie mit Urteilsvermögen anwenden.

Für große Teams ist der Wert gemeinsamer Prinzipien Koordination. Wenn Hunderte Ingenieurinnen am selben System arbeiten, brauchen sie ein gemeinsames Vokabular für Designdiskussionen und einen gemeinsamen Satz von Standardeinstellungen, damit unabhängig geschriebene Module zusammenpassen. Gutes Design ist, was vielen Menschen erlaubt, ein System parallel zu ändern, ohne ständig zu kollidieren. Es ist auch, was ein System ein Jahrzehnt später noch änderbar hält, die normale Lebensdauer von Unternehmens- und Behördensystemen, weit über die Amtszeit ihrer ursprünglichen Autoren hinaus.

Die kritische Fähigkeit ist nicht, Prinzipien auswendig zu lernen. Es ist zu wissen, wann jedes irreführt. Jedes Prinzip hat einen Versagensmodus: DRY kann die falsche Abstraktion produzieren, SOLID kann unnötige Indirektion produzieren, YAGNI kann Erweiterbarkeit aushungern, die Sie wirklich brauchen. Dieses Kapitel behandelt Prinzipien als Werkzeuge mit einem Anwendungsbereich, und es betont Kopplung und Kohäsion als die tieferen Eigenschaften, denen die Akronyme zu dienen versuchen.

## Kernprinzipien

- Steuern Sie zuerst Kopplung und Kohäsion; die meisten benannten Prinzipien sind indirekte Wege, diese zwei Eigenschaften zu verbessern.
- Optimieren Sie für Änderung: gutes Design minimiert die Kosten der Änderungen, die Sie wirklich machen müssen.
- Bevorzugen Sie das einfachste Design, das jetzt funktioniert, aber halten Sie Grenzen dort, wo Änderung wahrscheinlich ist.
- Duplikation ist günstiger als die falsche Abstraktion; warten Sie, bis das Muster klar ist.
- Machen Sie Abhängigkeiten explizit und richten Sie sie auf stabile Dinge aus.
- Modellieren Sie die Domäne in der Sprache der Domäne; richten Sie Softwaregrenzen an Geschäftsgrenzen aus.
- Wählen Sie Paradigmen passend zum Problem, nicht Ideologie; die meisten großen Systeme sind pragmatisch gemischt.

## Empfehlungen

### SOLID als Linse nutzen, nicht als Checkliste

Wenden Sie Single-Responsibility an, um Module kohäsiv zu halten, Dependency-Inversion, um Abhängigkeiten auf Abstraktionen auszurichten, wo eine Grenze wirklich existiert, und Open-Closed, wo Erweiterungspunkte real sind. Erfinden Sie keine Schnittstellen, Fabriken, und Schichten, nur um das Akronym zu erfüllen, wenn es nur eine Implementierung gibt und keine zweite in Sicht ist. Indirektion hat Kosten, und Sie zahlen sie bei jedem Lesen.

### DRY auf Wissen anwenden, nicht auf Text

DRY handelt davon, ein einzelnes autoritatives Stück *Wissen* nicht zu duplizieren. Es geht nicht darum, Zeilen zu beseitigen, die nur ähnlich aussehen. Zwei Stücke Code, die ähnlich aussehen, aber aus verschiedenen Gründen sich ändern, sollten getrennt bleiben. Bevorzugen Sie etwas Duplikation gegenüber einer verfrühten gemeinsamen Abstraktion, die unzusammenhängende Dinge koppelt. Extrahieren Sie die Abstraktion, sobald das echte Muster zwei- oder dreimal aufgetaucht ist.

### KISS und YAGNI Spekulation widerstehen lassen

Bauen Sie für die Anforderungen, die Sie haben, nicht die, die Sie sich vorstellen. Vermeiden Sie spekulative Allgemeinheit, wie konfigurierbare Frameworks, Plugin-Systeme, und Erweiterungspunkte, um die niemand gebeten hat. Das Gegengewicht ist, dass manche Flexibilität wirklich günstiger früh eingebaut wird, wie eine stabile Schnittstelle oder eine saubere Naht. YAGNI argumentiert gegen spekulative *Implementierung*, nicht gegen durchdachte Grenzen.

### Für niedrige Kopplung und hohe Kohäsion explizit gestalten

Lassen Sie jedes Modul eine wohldefinierte Sache tun (Kohäsion), und hängen Sie von so wenigen anderen Modulen wie möglich ab, durch enge Schnittstellen (niedrige Kopplung). Wenn Sie ein Design prüfen, fragen Sie, welche Änderungen über Modulgrenzen hinweg pulsieren. Diese Pulswellen sind das wahre Maß der Kopplung. Trennung von Belangen ist dieselbe Idee, angewendet auf Schichten und übergreifende Belange.

### Designmuster als Vokabular nutzen, Anti-Muster als Warnungen anwenden

Muster sind nützliche gemeinsame Namen für wiederkehrende Lösungen. Greifen Sie zu einem, wenn das Problem tatsächlich passt. Zwingen Sie keine Muster auf, um raffiniert zu wirken, denn musterlastiger Code ist oft ein Zeichen von Übertechnisierung. Lernen Sie die gängigen [Anti-Muster](https://en.wikipedia.org/wiki/Anti-pattern) (Gott-Objekte, anämische Modelle, wo unpassend, große Schlammkugeln, verteilte Monolithen) als diagnostische Etiketten.

### Domain-Driven Design übernehmen, wo die Domäne komplex ist

Für Systeme mit reichen Geschäftsregeln nutzen Sie DDDs taktische und strategische Werkzeuge: eine allgegenwärtige Sprache, geteilt mit Domänenexperten, begrenzte Kontexte, die das System in unabhängig modellierte Stücke schneiden, und Kontextkarten, die beschreiben, wie diese Stücke sich beziehen. Begrenzte Kontexte sind besonders wertvoll im Unternehmensmaßstab, weil sie Teameigentümerschaft mit Modellgrenzen ausrichten. DDD ist Übertreibung für einfache [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (Erstellen, Lesen, Aktualisieren, Löschen)-Systeme.

### Paradigmen nach Passung wählen

Nutzen Sie Objektorientierung zur Kapselung zustandsbehafteten Verhaltens und zur Modellierung von Domänen. Nutzen Sie funktionalen Stil für Transformationen, Nebenläufigkeit, und Vorhersagbarkeit durch [Unveränderlichkeit](https://en.wikipedia.org/wiki/Immutable_object). Nutzen Sie datenorientiertes Design, wo Performance und Cache-Verhalten dominieren. Große Systeme mischen alle drei. Treffen Sie die Wahl pro Komponente, und halten Sie die Grenzen zwischen Stilen sauber.

## Abwägungen: Vor- und Nachteile

| Prinzip/Ansatz | Gut angewendet | Versagensmodus |
|---|---|---|
| SOLID | Klare Nähte, wo Änderung geschieht; testbare Einheiten | Schnittstellen- und Schichtwucherung; Indirektion ohne Auszahlung |
| DRY | Einzige Wahrheitsquelle für echtes Wissen | Falsche Abstraktion koppelt unzusammenhängenden Code |
| KISS/YAGNI | Schlanke, verständliche Systeme | Unterdesignte Nähte; kostspielige Nachrüstung benötigter Flexibilität |
| Designmuster | Gemeinsames Vokabular; bewährte Strukturen | Muster-Cargo-Kult; zufällige Komplexität |
| Domain-Driven Design | Ausgerichtete Modelle und Teams; gebändigte Komplexität | Schwere Zeremonie bei einfachen Domänen; falsch platzierte Kontextgrenzen |
| Funktional/unveränderlich | Vorhersagbarkeit; sicherere Nebenläufigkeit | Unbeholfene Passung für von Natur aus zustandsbehaftete Probleme; Performance-Überraschungen |

Die wiederkehrende Spannung ist zwischen Unterdesign und Überdesign. Unterdesignte Systeme häufen Kopplung an und werden starr. Überdesignte Systeme ertrinken in Abstraktion, die jemand verstehen und pflegen muss. Die Antwort ist kein fester Punkt. Es ist eine Disziplin: Entscheidungen aufschieben, bis Sie genug Information haben, während Sie die Nähte behalten, die Ihnen erlauben, Ihre Meinung zu ändern.

## Fragen zur Diskussion mit Ihrem Team

1. **Was ist Ihre konkrete Schwelle zum Extrahieren einer gemeinsamen Abstraktion, und wie verhindern Sie, dass DRY die falsche produziert?** Dieses Kapitel ist unverblümt, dass Duplikation günstiger ist als die falsche Abstraktion, und dass Sie warten sollten, bis das Muster zwei- oder dreimal erschienen ist, bevor Sie extrahieren. In einem großen Team ist die Gefahr, dass jemand zwei ähnlich aussehende Schnipsel in ein gemeinsames Modul über Teamgrenzen hinweg faktorisiert, und dann jede zukünftige Änderung an einem Aufrufer in den anderen pulsiert. Das mitzubringende Signal ist, ob sich die Duplikate aus demselben Grund ändern oder gerade jetzt nur ähnlich aussehen. Vereinbaren Sie eine Dreier-Regel, und verlangen Sie, dass eine Kandidaten-Abstraktion sich tatsächlich zusammen geändert hat, bevor Sie die Aufrufer koppeln. Diese eine Vereinbarung verhindert eine Art von Kopplung, die teuer rückgängig zu machen ist, sobald viele Teams davon abhängen.

2. **Wie machen Sie Kopplung und Kohäsion in der Designprüfung sichtbar, statt sie dem Bauchgefühl zu überlassen?** Die Kernprinzipien stellen Kopplung und Kohäsion über jedes Akronym und definieren Kopplung als die Änderungen, die über Modulgrenzen hinweg pulsieren. Intuition skaliert nicht über Hunderte Ingenieurinnen, die jeweils nur ihre Ecke des Systems sehen. Bringen Sie Belege, die eine Maschine produzieren kann: Abhängigkeitsgraphen, und Mitänderungsdaten, die zeigen, welche Module immer wieder zusammen in denselben Commits bearbeitet werden. Fügen Sie eine explizite Prüfungsfrage hinzu, die fragt, welche Modulgrenzen eine Änderung Sie zu überqueren zwingt. Wenn sich zwei Module immer zusammen ändern, ist das Ihr Hinweis, sie entweder zusammenzuführen oder die Grenze zwischen ihnen zu korrigieren.

3. **Wo liegt in Ihren Systemen die Linie zwischen einer Domäne, reich genug, um Domain-Driven Design zu rechtfertigen, und einer einfachen CRUD-App, wo es Übertreibung ist?** Das Kapitel empfiehlt DDDs begrenzte Kontexte genau, weil sie Teameigentümerschaft mit Modellgrenzen ausrichten, und warnt, dass DDD Übertreibung für einfache Erstellen-Lesen-Aktualisieren-Löschen-Systeme ist und ohne echte Modellierung zu Zeremonie verkommt. Dies in beide Richtungen falsch zu machen ist kostspielig: schweres DDD auf einer dünnen Domäne begräbt eine einfache App in Zeremonie, während ein ausuferndes gemeinsames Modell über viele Teams ständige teamübergreifende Koordination erzwingt. Bringen Sie die Signale, die es tatsächlich entscheiden: die Dichte der Geschäftsregeln, und wie viele Teams Stücke unabhängig besitzen müssen. Reservieren Sie die strategische Maschinerie für den komplexen Kern, und lassen Sie die einfachen Ränder einfach bleiben. Das hält Sie sowohl von DDD-Theater als auch der großen Schlammkugel fern.

4. **Wann ist eine Abstraktion, Schnittstelle, oder ein Designmuster die Indirektion wert, die sie hinzufügt, und wer hat die Autorität, ein Design als übertechnisiert zu bezeichnen?** Dieses Kapitel ist explizit, dass Indirektion Kosten hat, die Sie bei jedem Lesen zahlen, und dass das Erfinden von Schnittstellen, Fabriken, und Schichten, um SOLID zu erfüllen oder raffiniert zu wirken, ein Versagensmodus ist. In einem großen Team läuft der Druck andersherum: Prüfende winken zusätzliche Abstraktion durch, weil sie diszipliniert aussieht, und niemand will die Person sein, die für weniger Struktur argumentiert. Die konkurrierende Erwägung ist real, denn manche Nähte verdienen wirklich ihren Unterhalt, und sie später zu entfernen ist teuer. Bringen Sie konkrete Belege in die Diskussion: wie viele Implementierungen eine Schnittstelle heute tatsächlich hat, wie oft sich der Erweiterungspunkt je gebogen hat, und wie viele Dateien eine Leserin öffnen muss, um einem Code-Pfad zu folgen. Vereinbaren Sie, dass eine einzelne Implementierung ohne zweite in Sicht ein Standardgrund zum Inline-Setzen ist, und benennen Sie, wer ein Design als übertechnisiert bezeichnen kann, ohne dass es wie eine Beleidigung klingt. In Unternehmens- und Behördensystemen, die ihre Autoren um ein Jahrzehnt überleben, ist grundlose Indirektion eine Steuer, die jede zukünftige Pflegerin zahlt, behandeln Sie "was bringt uns diese Abstraktion" also als stehende Prüfungsfrage, nicht als persönliche Herausforderung.

5. **Wie entscheiden Sie, welches Paradigma jede Komponente nutzt, objektorientiert, funktional, oder datenorientiert, und wie halten Sie die Grenzen zwischen ihnen sauber?** Das Kapitel argumentiert, dass große Systeme pragmatisch gemischt sind und dass Sie pro Komponente nach Passung wählen sollten, Objektorientierung für zustandsbehaftete Domänen, funktionalen Stil für Transformationen und Nebenläufigkeit, und datenorientiertes Design, wo Performance und Cache-Verhalten dominieren. Unverwaltet wird Paradigmenwahl zu einer Frage, wer das Modul zuerst schrieb, und veränderlicher Zustand sickert in das, was reine Transformationen sein sollten, oder funktionaler Purismus bekämpft ein von Natur aus zustandsbehaftetes Problem. Der mitzubringende Beleg ist, wo Ihr echter Schmerz liegt: welche Komponenten schwer zu testen sind wegen versteckten Zustands, welche heißen Pfade cache-gebunden sind, und wo der aktuelle Stil unbeholfene Umwege erzwingt. Entscheiden Sie das Standardparadigma für jede Schicht bewusst und schreiben Sie auf, wo die Nähte zwischen Stilen fallen, damit ein funktionaler Kern und ein imperativer Rand nicht ineinander bluten. Für ein reguliertes oder behördliches System, wo eine Berechnung für einen gegebenen Zeitraum prüfbar und reproduzierbar sein muss, ist ein unveränderlicher, funktionaler Kern oft eine Compliance-Anforderung statt eines Geschmacks, und diese Einschränkung sollte die Grenze antreiben statt ihr zu folgen.

6. **Wie verhindern Sie, dass diese Prinzipien zu Dogma erstarren, und wo protokollieren Sie die Begründung hinter einer Designentscheidung, damit ein zukünftiges Team sie überdenken kann?** Jedes Prinzip in diesem Kapitel hat einen Anwendungsbereich und einen Versagensmodus, und die ganze Rahmung behandelt sie als Werkzeuge, die mit Urteilsvermögen anzuwenden sind, statt als durchzusetzende Gesetze. In einem großen Team wird ein Prinzip still zur Regel: DRY verbietet jede Duplikation, SOLID schreibt eine Schnittstelle pro Klasse vor, und pragmatische Ausnahmen werden in der Prüfung von Menschen blockiert, die das Akronym statt das Ergebnis zitieren. Die Spannung ist, dass etwas Konsistenz wirklich Hunderten Ingenieurinnen hilft zu koordinieren, Sie können also nicht einfach jedes Prinzip für optional erklären. Bringen Sie Beispiele, wo das Befolgen eines Prinzips wörtlich ein schlechteres Design produzierte, und bringen Sie die Entscheidungsprotokolle, falls vorhanden, die erklären, warum eine gegebene Grenze oder Abstraktion existiert. Vereinbaren Sie, dass Prinzipien Standardeinstellungen sind, von denen eine Ingenieurin mit protokolliertem Grund abweichen darf, und erfassen Sie folgenreiche Designwahlen in einem kurzen Architekturentscheidungsprotokoll, damit das nächste Team die Begründung erbt, nicht nur den Code. In Unternehmens- und öffentlichen Systemen, wo die ursprünglichen Autoren längst gegangen sind und Prüfungen fragen, warum das System so geformt ist, wie es ist, ist diese schriftliche Spur der Unterschied zwischen einem Design, das zukünftige Teams sicher ändern können, und einem, das sie sich fürchten zu berühren.

## Branchenperspektive

**Startup.** Bevorzugen Sie das einfachste Design, das liefert, und halten Sie ein gut faktorisiertes Modul, bis ein echter zweiter Anwendungsfall eine Naht erzwingt. Ihre knappste Ressource ist technische Aufmerksamkeit, verfrühte Schnittstellen, Schichten, und spekulative Frameworks sind also reine Kosten. Folgen Sie der Dreier-Regel, bevor Sie irgendeine gemeinsame Abstraktion extrahieren, und lassen Sie YAGNI die Erweiterungspunkte töten, um die noch niemand gebeten hat.

**Kleinunternehmen.** Ohne dedizierte Architektin und mit knappem Budget stützen Sie sich auf das Design, das bereits in den Frameworks und Bibliotheken eingebacken ist, die Sie kaufen, statt eigene Muster zu erfinden. Reservieren Sie benutzerdefinierten Designaufwand für die Handvoll Regeln, die wirklich Ihr Geschäft sind, und halten Sie alles andere konventionell, damit ein Auftragnehmer oder eine Neueinstellung es lesen kann. Etwas Duplikation, die Sie verstehen, schlägt eine clevere Abstraktion, die nur ihr Autor pflegen kann.

**Großunternehmen.** Die Auszahlung gemeinsamer Prinzipien ist Koordination über viele Teams: ein gemeinsames Vokabular für Designprüfung, und begrenzte Kontexte, die Modellgrenzen mit Teameigentümerschaft ausrichten, sodass sich Gruppen unabhängig entwickeln. Steuern Sie Kopplung und Kohäsion explizit mit Abhängigkeits- und Mitänderungsdaten, und protokollieren Sie folgenreiche Designentscheidungen, damit Systeme lange nach dem Weiterziehen ihrer Autoren änderbar bleiben. Schützen Sie sich gleichermaßen vor der falschen Abstraktion, die Teams koppelt, und der Übertechnisierung, die jede Leserin besteuert.

**Behörde.** Prüfbarkeit und Reproduzierbarkeit diktieren oft das Design. Ein unveränderlicher, funktionaler Kern lässt Sie eine historische Berechnung für einen gegebenen Zeitraum genau reproduzieren, was ein verworrener Objektgraph mit verstecktem veränderlichen Zustand nicht garantieren kann. Bevorzugen Sie explizite veröffentlichte Verträge gegenüber gemeinsamen Tabellen an Kontextgrenzen, und halten Sie das Design und seine Entscheidungsprotokolle lesbar für Prüfer und für welches Team auch immer das System ein Jahrzehnt später erbt.

## Beispiele

**Startup.** Ein dreiköpfiges Startup, das sein erstes Produkt baut, widersteht dem Drang, jede Funktion in Schichten von Schnittstellen und Fabriken zu splitten, und behält ein einzelnes gut faktoriertes Modul, bis ein echter zweiter Anwendungsfall erscheint. Als dieselbe Logik zum dritten Mal über die Anmelde- und Abrechnungsflüsse erscheint, extrahieren sie eine kleine gemeinsame Funktion statt eines spekulativen Frameworks. Das hält die Codebasis klein genug, dass jede von ihnen sie im Kopf behalten kann, und die wenigen Nähte, die sie ziehen, fallen dort, wo sich das Produkt am wahrscheinlichsten ändert.

**Großunternehmen.** Eine große Versicherungsplattform modelliert Police, Ansprüche, und Abrechnung als separate begrenzte Kontexte, jeder besessen von einem dedizierten Team mit eigenem Datenmodell und Dienstgrenze. Wo sich die Kontexte treffen, wie wenn ein Anspruch auf eine Police verweist, sprechen sie durch explizite veröffentlichte Verträge statt gemeinsamer Datenbanktabellen. Das lässt die drei Teams sich unabhängig entwickeln, und die allgegenwärtige Sprache hält Gespräche mit Versicherungsmathematikern präzise. Eine frühere Version hatte ein einziges ausuferndes Modell geteilt, und jede Änderung erforderte teamübergreifende Koordination.

**Behörde.** Ein nationales Steuerverarbeitungssystem bevorzugt bewusst einen datenorientierten, funktionalen Kern für seine Berechnungs-Engine. Steuerregeln werden als reine Transformationen über unveränderliche Eingabedatensätze ausgedrückt, was sie prüfbar, testbar, und für ein gegebenes Steuerjahr reproduzierbar macht. Die imperativen, zustandsbehafteten Teile (Workflow, Benachrichtigungen) werden an den Rändern gehalten. Prüfer können auf eine spezifische Regelversion zeigen und jede historische Berechnung genau reproduzieren, was eine gesetzliche Anforderung ist, die ein verworrener Objektgraph mit verstecktem veränderlichen Zustand nicht garantieren könnte.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Designqualität ist eine Investition in die *Änderbarkeit* eines Systems, und Änderbarkeit dominiert die Gesamtbetriebskosten. Die meisten Kosten eines Systems fallen nach seiner ersten Veröffentlichung an, in Modifikation und Erweiterung. Gut gestaltete Systeme halten die Kosten der Änderung über Zeit ungefähr flach. Schlecht gestaltete sehen die Kosten jeder Änderung steigen, bis das System effektiv unmodifizierbar wird und neu geschrieben werden muss, das teuerste Ergebnis von allen.

Die Einführungskosten sind hauptsächlich Fähigkeit und Prüfungsdisziplin: die Prinzipien lehren, und Designzeit vorab verbringen. Die Kosten, sie nicht einzuführen, sind der langsame Aufbau [technischer Schulden](https://en.wikipedia.org/wiki/Technical_debt), sinkende Liefergeschwindigkeit, steigende Fehlerraten, und eventuelle kostspielige Neuschreibungen. Um Führungskräften den Fall darzulegen, verknüpfen Sie Designdisziplin mit Liefervorhersagbarkeit und dem Vermeiden von Neuschreibungsprogrammen, und verfolgen Sie Frühindikatoren wie Änderungsfehlerrate und die Zeit, vergleichbare Funktionen über Zeit zu implementieren. Achten Sie auch auf das gegenteilige Versagen: Überinvestition in Design für unsichere Zukünfte zerstört ebenfalls Wert. Das Argument ist also für *angemessenes* Design, kalibriert danach, wie wahrscheinlich und wie kostspielig zukünftige Änderung ist.

## Anti-Muster und Fallstricke

- **Spekulative Allgemeinheit:** Erweiterbarkeit für vorgestellte Anforderungen bauen, die nie ankommen.
- **Die falsche Abstraktion:** unzusammenhängenden Code zusammenzwingen, um DRY zu erfüllen, Kopplung schaffend, die schlimmer ist als Duplikation.
- **Muster-Cargo-Kult:** Designmuster um ihrer selbst willen anwenden, Indirektion ohne Nutzen hinzufügend.
- **Anämische oder Gott-Objekte:** Modelle ohne Verhalten, oder Objekte, die alles tun; beide signalisieren falsch platzierte Verantwortlichkeiten.
- **Verteilter Monolith:** physisch gesplittete, aber immer noch eng gekoppelte Dienste, die Kosten beider Ansätze kombinierend.
- **Große Schlammkugel:** keine erkennbare Struktur; jede Änderung riskiert alles.
- **DDD-Theater:** das Vokabular und die Ordnerstruktur übernehmen ohne die Domänenmodellierung, die ihm Wert gibt.

## Reifegradmodell

- **Stufe 1, Beginnen:** Design ist ad hoc und reaktiv; Kopplung häuft sich ungeprüft an; Prinzipien sind unbekannt oder werden als Slogans beschworen, und Abstraktionen erscheinen oder verschwinden nach individueller Gewohnheit.
- **Stufe 2, Entwickeln:** Teams kennen die Prinzipien und wenden sie an, aber uneinheitlich und oft dogmatisch; manche Gruppen steuern Kopplung und Kohäsion bewusst, während andere es nicht tun, und es gibt kein gemeinsames Vokabular über die Organisation.
- **Stufe 3, Standardisieren:** Ein gemeinsames Designvokabular, eine Dreier-Regel für das Extrahieren von Abstraktionen, Kopplungs- und Kohäsionsanalyse, und an Teams ausgerichtete begrenzte Kontexte sind dokumentiert und organisationsweit erwartet, konsistent in der Designprüfung angewendet statt individuellem Geschmack überlassen.
- **Stufe 4, Steuern:** Designgesundheit wird gegen Baselines gemessen: Kopplungs- und Mitänderungsdaten, Änderungsfehlerrate, und die Zeit, vergleichbare Funktionen zu implementieren, werden über Zeit verfolgt, sodass Abstraktionen und Grenzen aufgrund von Belegen hinzugefügt, behalten, oder entfernt werden, und Übertechnisierung und die falsche Abstraktion durch Daten statt Meinung erwischt werden.
- **Stufe 5, Orchestrieren:** Designdisziplin ist mit Liefer- und Risikoplanung über die Organisation integriert; Prinzipien werden mit Nuance und bekannten Versagensmodi angewendet; Paradigmen- und Grenzwahlen sind bewusst und werden kontinuierlich überdacht, und die Organisation faktorisiert routinemäßig neu, passt den Umfang an, und mustert Abstraktionen aus, während sich die Domäne und die Belege verschieben.

## Diskussionsideen

- Wie unterscheiden Sie zwischen einer benötigten Naht und spekulativer Allgemeinheit, bevor Sie die zukünftige Anforderung haben?
- Wann hat DRY Ihr Team zur falschen Abstraktion geführt, und wie haben Sie es erkannt?
- Wo sollten begrenzte-Kontext-Grenzen fallen, und wie eng sollten sie das Organigramm widerspiegeln?
- Wie viel Design sollte in Ihrem Kontext dem Code vorausgehen, und wie protokollieren Sie die Entscheidungen?
- Welche Teile Ihres Systems würden von einem funktionaleren oder datenorientierteren Stil profitieren?
- Wie verhindern Sie, dass Designprinzipien zu Dogma erstarren, das pragmatischen Ausnahmen widersteht?

## Wichtigste Erkenntnisse

- Kopplung und Kohäsion sind die Eigenschaften, die zählen; die Akronyme sind Mittel zu diesen Zwecken.
- Jedes Prinzip hat einen Versagensmodus; wissen Sie, wann jedes irreführt.
- Bevorzugen Sie etwas Duplikation gegenüber einer verfrühten oder falschen Abstraktion.
- Nutzen Sie DDD und begrenzte Kontexte, um komplexe Domänen mit Teameigentümerschaft auszurichten.
- Wählen Sie Paradigmen nach Passung; große Systeme sind pragmatisch gemischt.
- Gestalten Sie für die Änderungen, die Sie wirklich brauchen werden, sowohl Unter- als auch Überdesign vermeidend.

## Referenzen und weiterführende Literatur

- Robert C. Martin, *Clean Architecture* und *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* und *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
