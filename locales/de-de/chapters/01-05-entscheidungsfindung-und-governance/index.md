# 1.5 Entscheidungsfindung und Governance

## Überblick und Motivation

Jedes Softwaresystem ist die Summe Tausender Entscheidungen: welche [Datenbank](https://en.wikipedia.org/wiki/Database), welche Architektur, welche Bibliothek, ob man baut oder kauft, wann man Schulden aufnimmt und wann man sie abbaut. Governance ist, wie man diese Entscheidungen gut und konsistent trifft, die richtigen Menschen einbezieht, ohne Engpässe zu schaffen, und die Begründung bewahrt, damit zukünftige Teams nicht dazu verdammt sind, sie neu zu lernen. In einem kleinen Team geschehen Entscheidungen im Gespräch und leben im gemeinsamen Gedächtnis. Im großen Maßstab verdunstet dieses Gedächtnis. Menschen gehen, Teams strukturieren sich um, und das "Warum" hinter einer kritischen Wahl geht verloren, sodass Nachfolgerinnen es entweder blind nachahmen oder blind herausreißen. Gute Governance ist der Mechanismus, der Entscheidungen sichtbar, bewusst und dauerhaft über eine große und sich wandelnde Organisation hinweg macht.

Die zentrale Herausforderung für große Teams ist, Autonomie gegen Ausrichtung abzuwägen. Schieben Sie alle Entscheidungen zu einem zentralen Gremium hoch, erhalten Sie Konsistenz, aber auf Kosten lähmender Engpässe und entmachteter Teams. Schieben Sie alle Entscheidungen nach unten, erhalten Sie Geschwindigkeit, aber auf Kosten von Chaos: inkompatible Technologien, doppelte Arbeit und wiederholte Fehler. Die reife Antwort ist weder Zentralisierung noch Anarchie. Es ist ein geschichtetes Modell. Teams entscheiden die meisten Dinge lokal innerhalb eines gut markierten "ausgebauten Pfads", während ein leichtgewichtiger, transparenter Prozess die wirklich übergreifenden und schwer umkehrbaren Entscheidungen regelt. Das Ziel ist, gute Entscheidungen zum einfachen Standard zu machen und knappe Governance-Aufmerksamkeit nur dort auszugeben, wo es wirklich zählt.

Unternehmen und Behörden tragen erhöhte Einsätze. Sie müssen Prüfer, Regulierungsbehörden und Aufsichtsgremien zufriedenstellen, die dokumentierte, begründbare Entscheidungen verlangen. Sie arbeiten über lange Zeithorizonte, wo eine schlechte architektonische Wahl oder ein ungesteuerter Haufen [technischer Schulden](https://en.wikipedia.org/wiki/Technical_debt) sie ein Jahrzehnt lang belasten kann. Und ihre Beschaffungs- und Compliance-Pflichten machen Eigenbau-versus-Kauf-Entscheidungen besonders folgenreich und schwer umkehrbar. Für diese Organisationen ist disziplinierte, gut protokollierte Entscheidungsfindung nicht Bürokratie um ihrer selbst willen. Sie ist Risikomanagement, institutionelles Gedächtnis und die Grundlage von Rechenschaftspflicht.

## Kernprinzipien

- Protokollieren Sie Entscheidungen und ihre Begründung; eine Entscheidung ohne Begründung ist eine Belastung.
- Schieben Sie Entscheidungen auf die niedrigste Ebene, die den Kontext hat, innerhalb klarer Leitplanken.
- Passen Sie das Gewicht des Prozesses an das Gewicht und die Umkehrbarkeit der Entscheidung an.
- Unterscheiden Sie umkehrbare ("Zwei-Wege-Tür") von unumkehrbaren ("Ein-Wege-Tür") Entscheidungen und regeln Sie sie unterschiedlich.
- Bevorzugen Sie ausgebaute Pfade und Standardeinstellungen gegenüber fallweisen Genehmigungen.
- Behandeln Sie technische Schulden als gesteuertes Portfolio, nicht als moralisches Versagen, das versteckt werden muss.
- Machen Sie Governance transparent; verborgene Entscheidungsfindung züchtet Misstrauen und Nacharbeit.

## Empfehlungen

### Architekturentscheidungsprotokolle und einen angemessen dimensionierten RFC-Prozess übernehmen

Ein [Architekturentscheidungsprotokoll](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) ist ein kurzes, unveränderliches Dokument, das eine bedeutsame Entscheidung festhält: ihren Kontext, die erwogenen Optionen, die getroffene Wahl und die Konsequenzen. Speichern Sie ADRs in der Versionskontrolle neben dem Code, damit die Begründung mit dem System reist. Für Entscheidungen, die vor ihrem Treffen Input brauchen, nutzen Sie einen leichtgewichtigen [RFC](https://en.wikipedia.org/wiki/Request_for_Comments)-Prozess (Request for Comments): Verteilen Sie einen Vorschlag, laden Sie für einen begrenzten Zeitraum zu Kommentaren ein, entscheiden Sie dann und protokollieren Sie. Halten Sie beides leichtgewichtig. Der Wert liegt im Denken und im dauerhaften Protokoll, nicht in aufwendigen Vorlagen. Zusammen verwandeln ADRs und RFCs stillschweigende, vergessene Begründung in ein durchsuchbares institutionelles Gedächtnis.

### Durch ausgebaute Pfade regeln, nicht durch Wächter

Statt jede Entscheidung einzeln zu prüfen, investieren Sie in einen "ausgebauten Pfad": eine Reihe gesegneter, gut unterstützter Standardeinstellungen, genehmigter Sprachen, Frameworks, Bereitstellungspipelines und Muster, die Teams mit wenig Reibung und viel Unterstützung übernehmen können. Teams, die auf dem ausgebauten Pfad bleiben, brauchen wenig Governance, weil die sichere, konforme Wahl auch die einfache ist. Teams mit einem echten Grund, ihn zu verlassen, können das, übernehmen aber die zusätzliche Verantwortung und eine leichtgewichtige Prüfung. Dieses "goldener Pfad"-Modell skaliert weit besser als ein zentrales Gremium, das alles genehmigt, weil es Governance von fallweiser Wächterei zu gut gestalteten Standardeinstellungen verschiebt.

### Architektur-Review-Gremien sparsam und transparent nutzen

Ein Architektur-Review-Gremium, oder sein Äquivalent, hat eine legitime Rolle für die größten, übergreifendsten oder unumkehrbarsten Entscheidungen und zum Setzen der Standards, die den ausgebauten Pfad definieren. Halten Sie seinen Umfang eng, seine Kriterien veröffentlicht und seinen Prozess schnell und beratend, nicht einen zwingenden Engpass für Routinearbeit. Die Aufgabe des Gremiums ist, Kohärenz zu bewahren und Wissen zu teilen, nicht jede Wahl zu genehmigen. Wenn ein Gremium zu einer Warteschlange wird, in der jedes Projekt warten muss, hat es versagt. Delegieren Sie aggressiv, und reservieren Sie zentrale Prüfung für die wenigen Entscheidungen, die sie wirklich rechtfertigen.

### Eigenbau-versus-Kauf-versus-Übernahme zu einer bewussten Analyse machen

Für jede bedeutsame Fähigkeit wägen Sie drei Wege ab: im Haus bauen, ein kommerzielles Produkt kaufen, oder eine [Open-Source](https://en.wikipedia.org/wiki/Open-source_software)-Lösung übernehmen. Bauen Sie, wenn die Fähigkeit ein echtes Unterscheidungsmerkmal und Kern Ihrer Mission ist. Kaufen oder übernehmen Sie die unspezifischen Fähigkeiten, die andere besser machen. Zählen Sie die [Gesamtbetriebskosten](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), nicht nur den Vorabpreis. Kaufen verursacht Lizenz-, Integrations- und [Lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in)-Kosten. Bauen verursacht dauerhafte Wartung und Personal. Open Source übernehmen verursacht Support- und Sicherheitsverfolgungspflichten. Protokollieren Sie die Entscheidung und ihre Annahmen als ADR, damit Sie sie überdenken können, wenn sich Umstände ändern.

### Technische Schulden als Portfolio steuern

Technische Schulden sind nicht von Natur aus schlecht. Manchmal ist es die richtige Wahl, sie aufzunehmen, um früher auszuliefern. Schlecht ist ungesteuerte, unsichtbare, vergessene Schuld. Führen Sie ein explizites Inventar bedeutsamer Schulden. Notieren Sie für jedes Element die Kosten, die sie auferlegt (die laufenden "Zinsen"), und die Kosten, sie zu beheben. Dann steuern Sie sie wie ein Finanzportfolio. Zahlen Sie hochverzinsliche Schulden ab, die das Team jeden Tag verlangsamen. Tolerieren Sie niedrigverzinsliche Schulden in stabilen Ecken. Treffen Sie Schuldenentscheidungen bewusst statt zufällig. Reservieren Sie einen dauerhaften Anteil der Kapazität, um Schulden abzubauen, damit sie sich nie zu einer Krise summieren.

### Umkehrbare von unumkehrbaren Entscheidungen unterscheiden

Nicht alle Entscheidungen verdienen gleiche Bedächtigkeit. Umkehrbare "Zwei-Wege-Tür"-Entscheidungen sind leicht rückgängig zu machen, treffen Sie sie also schnell und lokal, vom Team, mit einer Neigung zum Handeln. Sich darüber zu quälen verschwendet Zeit und verlangsamt Lernen. Unumkehrbare oder teuer umzukehrende "Ein-Wege-Tür"-Entscheidungen, ein öffentlicher [API](https://en.wikipedia.org/wiki/API)-Vertrag, ein Datenmodell im großen Maßstab, eine mehrjährige Zulieferer-Verpflichtung, verdienen langsame, sorgfältige, erfahrene Bedächtigkeit und eine protokollierte Begründung. Entscheidungen so zu klassifizieren ist eine der Governance-Gewohnheiten mit dem höchsten Hebel, die Sie haben. Sie richtet knappe Prüfung dort aus, wo sie sich auszahlt, und entblockt alles andere.

## Abwägungen: Vor- und Nachteile

| Governance-Ansatz | Vorteile | Nachteile |
| --- | --- | --- |
| Zentrales Review-Gremium für alles | Maximale Konsistenz und Aufsicht | Schwerer Engpass; entmachtet Teams; langsam |
| Ausgebauter Pfad mit lokaler Autonomie | Skaliert, schnell, sicherer Standard, befähigt Teams | Erfordert Vorabinvestition in die Plattform; etwas Abdriften vom Pfad |
| Volle Teamautonomie, keine Governance | Schnell, hohe Verantwortung | Zersplitterung, Duplikation, wiederholte Fehler |
| ADRs/RFCs | Dauerhaftes Gedächtnis, bessere Entscheidungen, Transparenz | Schreibaufwand; ignoriert, wenn nicht gepflegt |

| Bezugswahl | Vorteile | Nachteile |
| --- | --- | --- |
| Bauen | Volle Kontrolle, passt genau, kann differenzieren | Dauerhafte Wartungs- und Personalkosten |
| Kaufen | Schnell, unterstützt, jemand anderes pflegt es | Lizenzkosten, Lock-in, unvollkommene Passung |
| Übernehmen (Open Source) | Keine Lizenzgebühr, prüfbar, Community | Support- und Sicherheitslast fällt auf Sie |

Die vereinheitlichende Abwägung ist Kontrolle gegen Geschwindigkeit, und zentrale Konsistenz gegen lokale Autonomie. Jede Governance-Wahl sitzt auf diesem Spektrum. Die empfohlene Haltung, ausgebaute Pfade plus umkehrbarkeitsbasierte Delegation, erkauft bewusst das meiste der Geschwindigkeit von Autonomie, während sie die Konsistenz behält, die zählt. Sie tut das, indem sie die ausgerichtete Wahl zur einfachen macht und schwergewichtigen Prozess für die seltene unumkehrbare Entscheidung reserviert.

## Fragen zur Diskussion mit Ihrem Team

1. **Wer entscheidet, ob eine gegebene Entscheidung eine Ein-Wege-Tür ist, und wie werden Sie Fehlklassifikationen in beide Richtungen erkennen?** Entscheidungen nach Umkehrbarkeit zu klassifizieren ist eine der Governance-Gewohnheiten mit dem höchsten Hebel, und ihr Wert bricht zusammen, wenn Sie Dinge falsch beschriften: Behandeln Sie eine umkehrbare Wahl als unumkehrbar, ertränken Sie sie in Bedächtigkeit; behandeln Sie eine unumkehrbare als umkehrbar, liefern Sie ein Datenmodell oder einen öffentlichen API-Vertrag aus, den Sie nicht günstig rückgängig machen können. Das konkurrierende Risiko ist, dass die Person, die der Arbeit am nächsten ist, zu Geschwindigkeit neigen kann, während ein zentrales Gremium zu Vorsicht neigen kann. Bringen Sie konkrete Beispiele in die Diskussion: Was würde es tatsächlich kosten, in Zeit und Geld, jede Entscheidung umzukehren, und wer trägt diese Kosten. In Unternehmens- und Behördenumgebungen verwandeln Beschaffungsverpflichtungen und Daten im großen Maßstab viele Wahlen in Ein-Wege-Türen, die anfangs umkehrbar aussahen. Vereinbaren Sie, wer klassifiziert, und bauen Sie die Gewohnheit einer schnellen zweiten Meinung bei allem nahe der Grenze auf, damit knappe Prüfung dort landet, wo Umkehr wirklich teuer ist.

2. **Wer besitzt, finanziert und besetzt den ausgebauten Pfad, und was verhindert, dass er zu einem Wächter verkommt?** Ein ausgebauter Pfad funktioniert nur, wenn die gesegneten Standardeinstellungen wirklich gut unterstützt und einfacher als die Alternativen sind, und das erfordert anhaltende Investition, die leicht unterfinanziert wird. Die Abwägung ist krass: Ein unterversorgter ausgebauter Pfad wird zu einer Reihe von Vorschriften ohne Unterstützung, genau der Wächterei, die das Modell ersetzen sollte, und Teams umgehen ihn dann. Bringen Sie Belege für die Gesundheit des Pfads: Adoptionsraten, wie aktuell die genehmigten Werkzeuge sind, wie schnell das Plattformteam reagiert, und wie oft Teams beantragen, vom Pfad abzuweichen. Für große und regulierte Organisationen ist der ausgebaute Pfad auch, wie die konforme Wahl zur einfachen wird, seine Finanzierung ist also eine Compliance-Investition, nicht nur eine Bequemlichkeit. Entscheiden Sie sich für einen klaren Eigentümer und ein dauerhaftes Budget, und messen Sie, ob Teams den Pfad wählen, weil er wirklich der einfachste Weg ist.

3. **Wo umgehen Teams Ihre Governance, und was sagt Ihnen diese Schatten-IT?** Teams weichen dem sanktionierten Weg aus, wenn er schmerzhafter als der Umweg ist, weit verbreitete Schatten-IT ist also weniger ein Disziplinproblem als ein Design-Urteil über Ihre Governance. Die konkurrierenden Erwägungen sind real: Manches Ausweichen ist rücksichtslos, und vieles davon ist rationales Vermeiden eines Review-Gremiums, das zu einer mehrwöchigen Warteschlange geworden ist. Bringen Sie die Belege: welche Genehmigungen übersprungen werden, welche inoffiziellen Werkzeuge sich still verbreitet haben, und wie lange der offizielle Weg tatsächlich dauert. In Unternehmens- und Behördenkontexten sind die Einsätze höher, weil nicht sanktionierte Werkzeuge Prüfungs-, Sicherheits- und Beschaffungspflichten verletzen können, die rechtliches Gewicht tragen. Wenn das Muster zeigt, dass Menschen einen Engpass umgehen, ist die Korrektur, den ausgebauten Pfad zu beschleunigen und zu erweitern und den Umfang des Gremiums auf die wenigen übergreifenden, unumkehrbaren Entscheidungen zu schrumpfen, nicht mehr Genehmigungen hinzuzufügen.

4. **Wie viel unserer Lieferkapazität geht tatsächlich in den Abbau technischer Schulden, und können wir die hochverzinslichsten Elemente benennen, die sie zuerst angehen sollte?** Technische Schulden verhalten sich wie Zinseszins, eine stille Steuer auf jede zukünftige Änderung, und eine große Organisation kann sie jahrelang tragen, bevor jemand bemerkt, dass das System langsam und spröde zum Ändern geworden ist. Der konkurrierende Druck ist unverblümt: Jede Stunde, die für Schulden aufgewendet wird, ist eine Stunde, die nicht für Funktionen aufgewendet wird, die die Führung sehen kann, Abbau ist also das Erste, was gestrichen wird, wenn eine Frist enger wird. Bringen Sie echte Belege in die Diskussion, ein schriftliches Inventar bedeutsamer Schulden, eine ehrliche Schätzung der laufenden Kosten, die jedes Element auferlegt, und der Kosten, es zu beheben, und den tatsächlichen Anteil der jüngsten Kapazität, der in Abbau versus neue Arbeit ging. Für Unternehmen und Behörden auf jahrzehntelangen Zeithorizonten erzwingt ungesteuerte Schuld schließlich eine kostspielige Neuschreibung oder einen Prüfungsbefund, behandeln Sie eine dauerhafte Abbau-Zuweisung also als Risikomanagement und entscheiden Sie, wer sie schützt, wenn Zeitpläne rutschen.

5. **Wenn wir die Begründung hinter einer vor zwei Jahren getroffenen Entscheidung brauchen, können wir sie tatsächlich finden, und hält jemand dieses Protokoll lebendig?** Der ganze Wert eines Architekturentscheidungsprotokolls ist, dass Begründung die Menschen überdauert, die sie erstellt haben, und dieser Wert bricht zusammen, wenn ADRs einmal geschrieben, nie durchsucht und still veraltet werden. Die Spannung liegt zwischen der Schreibdisziplin, die es braucht, Kontext, Optionen und Konsequenzen im Moment der Entscheidung festzuhalten, und dem täglichen Druck, einfach zu liefern und weiterzumachen. Bringen Sie konkrete Tests in die Diskussion: Wählen Sie drei wichtige jüngste Entscheidungen und sehen Sie, ob jemand die protokollierte Begründung in Minuten finden kann, und prüfen Sie, ob abgelöste ADRs als solche markiert sind, statt still der aktuellen Praxis zu widersprechen. In Unternehmens- und Behördenumgebungen ist dieses durchsuchbare Protokoll genau der begründbare Beleg, den Prüfer und Aufsichtsgremien verlangen, entscheiden Sie also, wo ADRs leben, wer sie überprüft, und was eine Entscheidung bedeutsam genug macht, um sie zu protokollieren.

6. **Wann haben wir zuletzt eine wichtige Eigenbau-versus-Kauf-Entscheidung gegen ihre ursprünglichen Annahmen wieder aufgemacht, und würden wir überhaupt bemerken, wenn diese Annahmen ablaufen?** Bezugswahlen gehören zu den teuersten und am schwersten umkehrbaren Entscheidungen, die Sie treffen, und die Annahmen dahinter (die Preisgestaltung eines Zulieferers, Ihre eigene Personalbesetzung, die Reife einer Open-Source-Option) veralten still, während die Entscheidung eingefroren bleibt. Die konkurrierenden Erwägungen wägen die versunkenen Kosten und die Störung eines Wechsels gegen die wachsenden Kosten von Lock-in, einer unvollkommenen Passung oder einer Wartungslast ab, die Sie nicht mehr wollen. Bringen Sie das ursprüngliche ADR und seine erklärten Annahmen, eine aktuelle Gesamtbetriebskostenschätzung für jeden Weg einschließlich Lizenzierung, Integration, Personal und Austrittskosten, und jedes Signal, eine Preisänderung oder eine Support-Herabstufung, dass sich eine Prämisse verschoben hat. Für behördliche und regulierte Käufer machen Beschaffungsregeln und mehrjährige Verträge diese Ein-Wege-Türen besonders bindend, vereinbaren Sie also im Voraus die Auslöser und den Rhythmus, der eine bewusste Neuentscheidung statt einer blinden Verlängerung erzwingt.

## Branchenperspektive

**Startup.** Regeln Sie fast nichts und stützen Sie sich stark auf Geschwindigkeit: Für umkehrbare Zwei-Wege-Tür-Entscheidungen entscheiden Sie am Schreibtisch und machen weiter. Reservieren Sie Ihre eine Governance-Gewohnheit für die Handvoll Ein-Wege-Türen, ein Kerndatenmodell oder ein grundlegender Zulieferer, und halten Sie jede in einem einzigen Absatz fest, damit eine zukünftige Teamkollegin sie nicht von Grund auf neu verhandelt. Überspringen Sie Review-Gremien und ausgebaute Pfade vollständig, denn bei Ihrer Größe sind sie Aufwand, den Sie sich nicht leisten können, und das ganze Team teilt bereits den Kontext.

**Kleinunternehmen.** Ohne Architektin im Personal machen Sie Eigenbau-versus-Kauf zu Ihrer zentralen Governance-Frage und beantworten sie anhand der Gesamtbetriebskosten statt Vorliebe. Setzen Sie standardmäßig auf Kaufen oder Übernehmen gut unterstützter Werkzeuge für alles, was nicht Ihr Kernunterscheidungsmerkmal ist, denn dauerhafte Wartung sind die Kosten, die Sie sich am wenigsten leisten können zu tragen. Halten Sie ein leichtgewichtiges Entscheidungsprotokoll, damit die Begründung hinter Ihren wenigen folgenreichen Wahlen überlebt, wenn eine Schlüsselperson geht.

**Großunternehmen.** Ihr Problem ist, Autonomie gegen Ausrichtung über viele Teams hinweg abzuwägen, investieren Sie also in einen finanzierten ausgebauten Pfad und reservieren Sie ein enges, schnelles Architektur-Review-Gremium für die wirklich übergreifenden und unumkehrbaren Entscheidungen. Standardisieren Sie ADRs, damit Begründung zu durchsuchbarem institutionellem Gedächtnis wird, und steuern Sie technische Schulden und Bezugswahlen als Portfolios mit dauerhaften Budgets. Messen Sie, ob Teams den Pfad wählen, weil er am einfachsten ist, und schrumpfen Sie jedes Gremium, das zu einer Warteschlange verkommen ist.

**Behörde.** Dokumentierte, begründbare Entscheidungen sind hier nicht optional: Prüfer und Aufsichtsgremien erwarten, die Begründung, die abgewogenen Optionen und die Annahmen hinter jeder folgenreichen Wahl zu sehen. Führen Sie Eigenbau-versus-Kauf als protokollierte Gesamtbetriebskostenanalyse durch, respektieren Sie Beschaffungsregeln, die Alleinanbieter-Lock-in einschränken, und halten Sie ADRs als prüfungsbereite Belegspur. Nehmen Sie lange Zeithorizonte ernst, denn ein heute getroffenes Datenmodell oder eine Zulieferer-Verpflichtung kann die Organisation ein Jahrzehnt binden, klassifizieren Sie sie also als Ein-Wege-Tür und beraten Sie entsprechend.

## Beispiele

**Startup.** Ein vierköpfiges Startup trifft die meisten Entscheidungen in Minuten über einen gemeinsamen Schreibtisch, und für umkehrbare Zwei-Wege-Tür-Wahlen ist diese Geschwindigkeit ein echter Vorteil, also widersteht es jedem Governance-Aufwand. Aber als es eine Datenbank und ein Datenmodell wählt, das später schmerzhaft zu ändern sein wird (eine Ein-Wege-Tür), halten sie inne, um eine Ein-Absatz-Notiz zu schreiben: die Optionen, die Wahl und die Annahmen dahinter. Ein Jahr später, an Skalierungsgrenzen stoßend, rettet sie diese eine Notiz davor, die Frage von Grund auf neu zu verhandeln. Sie regeln fast nichts und reservieren ihre eine leichtgewichtige Gewohnheit für die wenigen Entscheidungen, die wirklich teuer umzukehren sind.

**Großunternehmen.** Die Plattformteams eines großen Unternehmens waren durch ein Architektur-Review-Gremium gelähmt, das jede Technologiewahl genehmigen musste, was mehrwöchige Warteschlangen schuf. Das Unternehmen strukturierte Governance um einen ausgebauten Pfad um: einen kuratierten Katalog genehmigter, voll unterstützter Sprachen, Datenspeicher und Pipelines, die Teams sofort übernehmen konnten. ADRs protokollierten jede Entscheidung, abzuweichen, und eine schnelle, beratende Prüfung handhabte nur Off-Road-Wahlen. Der Umfang des Gremiums schrumpfte auf Standardsetzung und die Handvoll wirklich übergreifender Entscheidungen. Die Lieferung beschleunigte sich stark. Konsistenz verbesserte sich tatsächlich, weil der einfache Weg jetzt der konforme war. Und das ADR-Archiv gab der Organisation ein durchsuchbares Protokoll darüber, warum Dinge so gebaut wurden, wie sie waren.

**Behörde.** Eine staatliche Abteilung stand vor einer wichtigen Eigenbau-versus-Kauf-Entscheidung für eine Fallmanagementplattform unter strengen Beschaffungs- und Prüfungsregeln. Statt nach Vorliebe zu entscheiden, führte sie eine dokumentierte Gesamtbetriebskostenanalyse über drei Optionen durch: maßgeschneidert bauen, ein kommerzielles Produkt kaufen und eine Open-Source-Basis übernehmen. Sie wog Lizenzierung, Integration, langfristige Wartung, Personal und Lock-in ab und protokollierte die Entscheidung und ihre Annahmen als ADR. Jahre später, als sich die Bedingungen eines Zulieferers änderten, überdachte die Abteilung dieses ADR, stellte fest, dass ihre ursprünglichen Annahmen nicht mehr galten, und entschied mit vollem Wissen der früheren Begründung neu, was eine blinde und kostspielige Migration vermied. Die protokollierte Begründung war auch genau der begründbare Beleg, den Prüfer verlangten.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Entscheidungen sind die Kosten mit dem höchsten Hebel und der niedrigsten Sichtbarkeit in der Software. Eine einzige schlechte, unumkehrbare architektonische oder Bezugswahl kann Jahre der Bremswirkung oder eine neunstellige Sanierung auferlegen. Sie gut zu regeln, ein paar Stunden Bedächtigkeit und ein schriftliches Protokoll, kostet im Vergleich fast nichts. Die Rendite von ADRs und umkehrbarkeitsbasierter Delegation kommt aus zwei Quellen: das Vermeiden teurer Fehler bei den Ein-Wege-Tür-Entscheidungen und das Vermeiden verschwendeter Bedächtigkeit und Nacharbeit bei allem anderen. Protokollierte Begründung senkt auch drastisch die wiederkehrenden Kosten, geklärte Fragen neu zu verhandeln und dass Teams die Absicht hinter geerbten Systemen zurückentwickeln müssen.

Technische Schulden machen das TCO-Argument konkret. Ungesteuerte Schulden verhalten sich genau wie Zinseszins: eine wachsende Steuer auf jede zukünftige Änderung, bis das System effektiv unwartbar wird und eine kostspielige Neuschreibung verlangt. Schulden als Portfolio zu steuern, mit einer dauerhaften Kapazitätszuweisung, um die hochverzinslichen Elemente abzubauen, ist weit günstiger als die eventuelle Krise. Gute Governance ist günstig einzuführen, größtenteils die Disziplin, Entscheidungen aufzuschreiben, und die Vorabinvestition in einen ausgebauten Pfad. Sie zu überspringen ist teuer: Sie zahlen in vermeidbaren Neuschreibungen, Lock-in-Überraschungen, Prüfungsfehlern und verlorenem institutionellem Gedächtnis. Um Führungskräfte zu überzeugen, rahmen Sie Governance in ihrer Sprache: Risikoreduzierung, vermiedene Nacharbeit, schnellere Lieferung über den ausgebauten Pfad und prüfungsbereite Begründbarkeit. Zeigen Sie, dass das Ziel nicht mehr Prozess ist, sondern besser gezielter Prozess, schwere Prüfung nur dort, wo Umkehr teuer ist, und reibungslose Geschwindigkeit überall sonst.

## Anti-Muster und Fallstricke

- Undokumentierte Entscheidungen: Begründung verloren in dem Moment, in dem die Menschen, die sie trafen, gehen.
- Genehmigungsgremium-Engpass: eine zentrale Stelle, hinter der jedes Projekt warten muss.
- Einheitsprozess: triviale umkehrbare Entscheidungen durch schwergewichtige Prüfung zwingen.
- Analyseparalyse: sich über leicht umkehrbare Zwei-Wege-Tür-Entscheidungen quälen.
- [Schatten-IT](https://en.wikipedia.org/wiki/Shadow_IT): Teams, die Governance vollständig umgehen, weil der sanktionierte Weg zu schmerzhaft ist.
- Unsichtbare technische Schulden: Schulden nie inventarisiert, nie abgebaut, still summierend.
- Alles-bauen- oder Alles-kaufen-Reflexe: Bezug aus Gewohnheit statt TCO-Analyse.
- Governance-Theater: Dokumente und Gremien, die aus Erscheinung existieren, aber Entscheidungen nicht prägen.

## Reifegradmodell

- Stufe 1 (Beginnen): Entscheidungen sind ad hoc und unprotokolliert; Governance ist entweder abwesend oder ein pauschaler Engpass; technische Schulden sind unsichtbar, und die Begründung hinter Wahlen verdunstet, wenn Menschen gehen.
- Stufe 2 (Entwickeln): Manche Entscheidungen werden dokumentiert, und manche Prüfung existiert, aber die Praxis ist über Teams hinweg uneinheitlich, und der Prozess ist oft nicht auf das Gewicht und die Umkehrbarkeit der Entscheidung abgestimmt.
- Stufe 3 (Standardisieren): ADRs, ein ausgebauter Pfad, umkehrbarkeitsbasierte Delegation und ein Schuldeninventar sind dokumentiert und organisationsweit durchgesetzt, sodass die konforme Wahl der einfache Standard ist und Begründung durchsuchbar ist.
- Stufe 4 (Steuern): Governance wird gegen Baselines gemessen: Ausgebauter-Pfad-Adoption, ADR-Abdeckung, Entscheidungszykluszeit, Schuld als Anteil der Kapazität und Off-Road-Ausnahmeraten werden verfolgt, und Entscheidungen, Schulden abzubauen oder Bezug zu überdenken, werden durch diese Belege ausgelöst statt durch Krise.
- Stufe 5 (Orchestrieren): Governance wird kontinuierlich eingestellt und in Liefer- und Risikoplanung integriert; Prüfung ist präzise auf unumkehrbare Entscheidungen gezielt; Schuld- und Bezugswahlen werden aktiv als Portfolios neu ausbalanciert und aufgrund von Belegen neu entschieden, während sich Umstände verschieben.

## Diskussionsideen

- Können wir für unsere wichtigsten jüngsten Entscheidungen die protokollierte Begründung dahinter finden?
- Wo ist unsere Governance ein Engpass, und wo fehlt sie, wenn sie gebraucht wird?
- Welche unserer aktuellen Entscheidungen sind Ein-Wege-Türen, und behandeln wir sie als solche?
- Wie viel unserer Kapazität geht in den Abbau technischer Schulden, und ist es genug?
- Folgen unsere Teams dem ausgebauten Pfad, weil er wirklich der einfachste Weg ist, oder umgehen sie ihn?
- Wann haben wir zuletzt eine wichtige Eigenbau-versus-Kauf-Entscheidung gegen ihre ursprünglichen Annahmen überdacht?

## Wichtigste Erkenntnisse

- Protokollieren Sie bedeutsame Entscheidungen und ihre Begründung mit ADRs; machen Sie Begründung dauerhaft.
- Regeln Sie durch ausgebaute Pfade und Standardeinstellungen, nicht durch fallweise Wächterei.
- Passen Sie Prozessgewicht an Entscheidungsgewicht und Umkehrbarkeit an; delegieren Sie Zwei-Wege-Türen, beraten Sie bei Ein-Wege-Türen.
- Analysieren Sie Eigenbau-versus-Kauf-versus-Übernahme anhand der Gesamtbetriebskosten, und protokollieren Sie die Annahmen.
- Steuern Sie technische Schulden als explizites Portfolio mit einer dauerhaften Abbau-Zuweisung.
- Halten Sie Governance transparent und leichtgewichtig; zielen Sie knappe Prüfung dorthin, wo Umkehr teuer ist.

## Referenzen und weiterführende Literatur

- Michael Nygard, "Documenting Architecture Decisions" (das ursprüngliche ADR-Muster)
- Gregor Hohpe, "The Software Architect Elevator" und "37 Things One Architect Knows"
- Amazon-Aktionärsbriefe zu Typ-1- versus Typ-2- (Ein-Wege- versus Zwei-Wege-Tür-) Entscheidungen
- Ward Cunningham, die ursprüngliche "technische Schulden"-Metapher
- Martin Fowler, Schriften zu technischen Schulden und evolutionärer Architektur
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (lose gekoppelte Architektur und Autonomie)
- ISO/IEC/IEEE 42010 zur Architekturbeschreibung
