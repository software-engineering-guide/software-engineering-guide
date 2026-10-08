# 10.7 Agile

## Überblick und Motivation

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) ist eine Denkweise, Software (und Wert) iterativ, inkrementell, und in enger Zusammenarbeit mit den Menschen zu liefern, die sie nutzen werden. Im 2001er *Manifest für Agile Softwareentwicklung* kodifiziert, wird es am besten nicht als Prozess verstanden, sondern als ein Satz **Werte und Prinzipien**: Individuen und Interaktionen, funktionierende Software, Kundinnenzusammenarbeit, und Reaktion auf Veränderung priorisieren, über die planungslastigen, vertragslastigen, dokumentationslastigen Standards, die davor kamen. Frameworks wie [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), und Extreme Programming ([XP](https://en.wikipedia.org/wiki/Extreme_programming)) sind *Implementierungen* dieser Denkweise. Sie sind nützliche Startpunkte, aber nicht die Denkweise selbst. Dieses Kapitel ergänzt Kapitel 1.4 (Arbeitsweisen, das Methoden breit übersieht), indem es tief in Agile speziell geht.

Agile wird von derselben Kraft getrieben, die die Discovery- und Lieferpipelines animiert (Kapitel 11.1–11.2): Anforderungen für Software werden *entdeckt*, nicht vollständig im Voraus bekannt, und die Welt ändert sich schneller, als ein langer Plan absorbieren kann. Big-Bang-, alles-zuerst-planen-Lieferung produziert wiederholt Systeme, die spät, über Budget, und, am schlimmsten, falsch sind, weil das ganze Lernen am Ende ankommt, wenn es am teuersten ist, danach zu handeln. Agiles Kernwette ist einfach: kurze Zyklen, echte, funktionierende Software zu bauen und echtes Feedback zu bekommen, schlagen lange Zyklen der Spekulation. Gut gemacht, reduziert es Risiko kontinuierlich statt es aufzuschieben.

Für große Teams, Unternehmen, und Behörden ist Agile sowohl mächtig als auch häufig verstümmelt. Unternehmen übernehmen es über Hunderte Teams und reduzieren es oft auf Ritual ("wir machen jetzt Stand-ups"), ohne zu ändern, wie Entscheidungen getroffen werden oder wie Wert gemessen wird. Behörden haben Agile absichtlich umarmt, denn iterative, nutzerinnenzentrierte Lieferung reduziert nachweisbar das Risiko großer öffentlicher Programme: der U.S. Digital Service und sein *Digital Services Playbook*, der britische Government Digital Service und Service Standard, und agile Beschaffungsreformen entstanden teilweise als Reaktion auf hochkarätige [Wasserfall](https://en.wikipedia.org/wiki/Waterfall_model)-Fehlschläge. Der Preis ist echt. Genauso wie der Fehlschlagsmodus von "Agile nur dem Namen nach".

## Kernprinzipien

- **Schätzen Sie die vier Werte des Manifests** (Menschen, funktionierende Software, Zusammenarbeit, und Reaktionsfähigkeit) über Prozessartefakte.
- **Liefern Sie funktionierende Software häufig** in kleinen Inkrementen; funktionierende Software ist das primäre Fortschrittsmaß.
- **Begrüßen Sie Änderung**, selbst spät; Anpassungsfähigkeit ist ein Feature, kein Fehlschlag.
- **Bauen Sie um motivierte, ermächtigte, selbstorganisierende Teams herum.**
- **Arbeiten Sie kontinuierlich mit Nutzerinnen und Stakeholdern zusammen.**
- **Reflektieren und verbessern Sie** in regelmäßiger Kadenz.
- **Erhalten Sie ein menschliches Tempo** und technische Exzellenz: Geschwindigkeit ohne Handwerk kollabiert.

## Empfehlungen

### An Werten und Prinzipien verankern, nicht Zeremonien

Die einzige wichtigste Agile-Empfehlung ist, mit dem *Warum* zu führen. Ein Team, das ein tägliches Stand-up, eine Sprintüberprüfung, und eine Retrospektive abhält, sich aber trotzdem zu festem Umfang zu einem festen Datum verpflichtet, schlechte Nachrichten versteckt, und nie den Plan ändert, ist nicht agil. Es ist Wasserfall mit Meetings. Nutzen Sie die zwölf Prinzipien als Checkliste für echte Agilität. Liefern Sie funktionierende Software oft? Können Sie eine Änderung in der nächsten Iteration begrüßen? Entscheidet das Team, *wie* die Arbeit zu tun ist? Ist die Kundin tatsächlich im Loop? Wenn die Zeremonien diese Ergebnisse nicht produzieren, beheben Sie die Ergebnisse, nicht die Zeremonien.

### Ein Framework als Startpunkt wählen, nicht als Religion

Wählen Sie ein Framework, das zur Arbeit passt, und passen Sie es an:

- **Scrum:** zeitgeboxte Sprints, ein priorisierter Rückstand, und definierte Rollen (Product Owner, Scrum Master, Entwicklerinnen). Gut für Feature-Lieferung mit klarer Product Owner; schwach, wenn Arbeit stark unterbrechungsgetrieben ist.
- **Kanban:** kontinuierlicher Fluss mit expliziten Work-in-Progress-Limits und einem Pull-System. Gut für Support, Betrieb, und unvorhersehbare Ankunft (und direkt in Fluss- und Warteschlangentheorie verankert, siehe Kapitel 11.2, 11.3). WIP zu begrenzen verkürzt Durchlaufzeit ([Littles Gesetz](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** Engineering-Praktiken einschließlich [testgetriebener Entwicklung](https://en.wikipedia.org/wiki/Test-driven_development), [Paarprogrammierung](https://en.wikipedia.org/wiki/Pair_programming), [kontinuierlicher Integration](https://en.wikipedia.org/wiki/Continuous_integration), Refactoring, kleiner Veröffentlichungen. Das technische Rückgrat, das jedes Framework nachhaltig macht.
- **Scrumban** und Mischungen: pragmatische Kombinationen, zu denen viele reife Teams konvergieren.

Frameworks sind Gerüst. Behalten Sie, was hilft, verwerfen Sie, was nicht hilft, und lassen Sie nie "das Framework sagt so" das "die Prinzipien sagen warum" übersteuern.


### Auf technischer Exzellenz bestehen

Agile ohne Engineering-Disziplin degradiert schnell zu schneller Produktion unpflegbaren Codes, "Dark Scrum", wo Teams sich selbst in einen Teergrubensumpf aus Defekten und [technischen Schulden](https://en.wikipedia.org/wiki/Technical_debt) sprinten. Die XP-Praktiken sind keine optionalen Extras. Kontinuierliche Integration (Kapitel 8.1), automatisiertes Testen (Kapitel 2.4), Refactoring, Trunk-basierte Entwicklung (Kapitel 2.6), und sauberes Design (Kapitel 2.2) sind, was einem Team erlaubt, Software günstig weiter zu ändern, was die gesamte Prämisse von Agilität ist. Nachhaltiges Tempo zählt aus demselben Grund: ausgebrannte Teams können weder Qualität noch Reaktionsfähigkeit aufrechterhalten.

### Mit Sorgfalt skalieren, und Entskalieren bevorzugen

Skalierungsframeworks, wie SAFe (das Scaled Agile Framework), LeSS, Nexus, und Scrum@Scale, koordinieren viele Teams zu geteilten Zielen. Sie können helfen, tragen aber eine Warnung (Kapitel 1.4 nachhallend): schwere Skalierungsframeworks reintroduzieren oft genau die Command-and-Control-, planungslastige Overhead, die Agile beheben sollte. Bevor Sie ein großes Framework übernehmen, versuchen Sie *Entskalieren*. Organisieren Sie um unabhängige, strom-ausgerichtete Teams mit klarem Besitz und minimalen teamübergreifenden Abhängigkeiten (Kapitel 1.2), damit Sie überhaupt weniger Koordinationsmaschinerie brauchen. Wo Koordination echt gefordert ist, fügen Sie die leichteste funktionierende Struktur hinzu, und binden Sie sie an Ergebnisse (OKRs, Objectives and Key Results, Kapitel 11.1), nicht Ausgabe.

### Agilität in Unternehmen und Behörden echt machen

Adaptive Lieferung und institutionelle Einschränkungen können koexistieren, aber es braucht absichtliches Design:

- **Hybride Governance:** ein adaptiver Lieferkern innerhalb einer prädiktiven Finanzierungs-/Compliance-Hülle (Kapitel 10.6), damit Iteration Aufsicht erfüllt statt bekämpft.
- **Agile Beschaffung:** modulare, ergebnisbasierte Verträge und kürzere Inkremente statt eines einzelnen umfangsfesten Megavertrags; hier gelingt oder scheitert öffentliche-Sektor-Agile am häufigsten.
- **Compliance im Gehen:** bauen Sie Prüfung, Barrierefreiheit (Kapitel 5.3), und Sicherheit (Kapitel 4.1) in das Inkrement via Automatisierung und Fitnessfunktionen (automatisierte Checks, die kontinuierlich architektonische und Qualitätseigenschaften verifizieren; Kapitel 8.5, 1.6), nicht ein spätes Tor.
- **Echter Nutzerinnenzugang:** der härteste und wichtigste. Teams brauchen echten Kontakt mit Bürgerinnen oder Kundinnen, den Beschaffungs- und Sicherheitsregeln oft behindern.

### Kontinuierlich verbessern, und es ernst meinen

Die Retrospektive ist Agiles Verbesserungsmotor, und sie ist wertlos, wenn sie keine Änderung produziert. Führen Sie Retrospektiven durch, die eine kleine Anzahl konkreter, besessener Aktionen generieren, und schließen Sie sie tatsächlich ab, bevor die nächste kommt. Messen Sie Ergebnisse (bewegte die Änderung ein Key Result? siehe Kapitel 11.1) und Fluss (schrumpfen Durchlaufzeiten? siehe Kapitel 11.2, 11.3). Messen Sie nicht Geschwindigkeit: sie ist ein Kapazitätssignal, das zur Lüge wird, sobald Sie sie als Produktivitätsziel nutzen.

## Abwägungen: Vor- und Nachteile

| Entscheidung | Vorteile | Nachteile |
|---|---|---|
| **Agile (adaptiv)** | Schnelles Feedback; absorbiert Änderung; früher, kontinuierlicher Wert | Schwerer, Umfang/Kosten im Voraus zu fixieren; fordert engagierte Kundin & Disziplin |
| **Wasserfall (prädiktiv)** | Vorhersagbarer Umfang; vertrags-/prüfungsfreundlich | Spätes Feedback; Big-Bang-Risiko; schlechte Passung für unsichere Anforderungen |
| **Scrum** | Kadenz, Rollen, Fokus; weit verstanden | Zeremonie-Overhead; kämpft mit unterbrechungsgetriebener Arbeit |
| **Kanban** | Fluss, WIP-Limits, flexibel; großartig für Betrieb | Weniger Struktur; braucht Disziplin, Limits zu halten |
| **Schwere Skalierung (SAFe)** | Koordiniert viele Teams; vertraut für große Organisationen | Kann Command-and-Control reintroduzieren; zeremonielastig |
| **Entskalieren/Teamautonomie** | Weniger Koordinations-Overhead; schnellere Teams | Fordert niedrige Kopplung und starke Plattform/Besitz |

Die definierende Spannung ist **Anpassungsfähigkeit versus Vorhersagbarkeit**, und die klassische Fehllesung ist, dass Agile "kein Plan" bedeutet. Das tut es nicht. Es bedeutet, kontinuierlich zu planen und sich zu *Ergebnissen und Kadenz* zu verpflichten, während *Umfang* flexen darf. Die andere wiederkehrende Falle ist, Agile als *nur* Prozess (Zeremonien) oder *nur* Engineering (XP) zu behandeln. Es braucht beides.

## Fragen zur Diskussion mit Ihrem Team

1. **In Ihrem Unternehmens- oder Behördenkontext, sind Ihre Verträge modular und ergebnisbasiert, oder ist Lieferung in einem einzelnen umfangsfesten Megavertrag gesperrt?** Agile Beschaffung ist, wo öffentliche-Sektor-Agilität am häufigsten gelingt oder scheitert, denn ein einzelner festpreis-, umfangsfester Vertrag erzwingt Wasserfall, egal wie die Lieferteams ihre Meetings nennen. Modulare, ergebnisbasierte Verträge mit kürzeren Inkrementen lassen Umfang innerhalb fester Finanzierung zu einem wertvollen Kern flexen, was genau das Muster hinter modernen öffentliche-Sektor-Erfolgen ist und das Gegenmittel zu vergangenen Big-Bang-Fehlschlägen. Bringen Sie Beleg: schauen Sie sich Ihre aktuellen Verträge an und fragen Sie, ob eine Anbieterin für demonstrierte funktionierende Software bezahlt wird oder für einen vor Jahren abgezeichneten festen Umfang. Die Antwort sollte formen, wie Sie die nächste Beschaffung strukturieren, weit mehr als welches Framework Ihre Teams intern übernehmen. Sie können in der Lieferung nicht adaptiv sein, während Ihr Vertrag einen entfernten Alles-oder-Nichts-Go-Live vorschreibt.

2. **Sind Prüfung, Barrierefreiheit, und Sicherheit durch Automatisierung in jedes Inkrement eingebaut, oder als spätes Tor angeschraubt?** Compliance-im-Gehen ist, was adaptive Lieferung mit institutionellen Einschränkungen koexistieren lässt: bauen Sie die Checks via Automatisierung und Fitnessfunktionen in das Inkrement, statt sie für ein Vor-Veröffentlichung-Gedränge aufzusparen. Ein spätes Compliance-Tor reintroduziert das Big-Bang-Risiko, das Agile beheben soll, denn die teuren Probleme tauchen am Ende auf, wenn sie am schwersten zu beheben sind. Bringen Sie Beleg: prüfen Sie für Ihr letztes Inkrement, ob Barrierefreiheits-, Sicherheits-, und Prüfbeleg automatisch in der Pipeline verifiziert oder auf eine manuelle Überprüfung vor Einführung aufgeschoben wurden. Die Antwort sollte diese Eigenschaften in kontinuierliche automatisierte Checks drücken, damit Aufsicht durch den Akt des Bauens erfüllt wird statt durch eine separate Phase. Das ist auch, was ein reguliertes Programm zwischen Prüfungen ehrlich hält statt nur in den Wochen davor.

3. **Wie würden Sie wissen, ob Ihre Teams sich in technische Schulden sprinten, und was schützt nachhaltiges Tempo unter Einführungsdruck?** Agile ohne Engineering-Disziplin degradiert zu Dark Scrum, wo Teams schnell in einen Teergrubensumpf aus Defekten und unpflegbarem Code sprinten, und ausgebrannte Teams können weder Qualität noch Reaktionsfähigkeit aufrechterhalten. Die XP-Praktiken (kontinuierliche Integration, automatisiertes Testen, Refactoring, Trunk-basierte Entwicklung) sind, was einem Team erlaubt, Software günstig weiter zu ändern, was die gesamte Prämisse von Agilität ist, sie sind also keine optionalen Extras, gegen die zu tauschen ist, wenn ein Datum droht. Bringen Sie Beleg: verfolgen Sie, ob Durchlaufzeiten schrumpfen oder wachsen, ob Defektraten klettern, und ob das Team still länger arbeitet, um jeden Sprint zu treffen. Die Antwort sollte technische Exzellenz und menschliches Tempo nicht verhandelbar machen, denn Geschwindigkeit, durch Opferung von Handwerk gekauft, kollabiert binnen weniger Iterationen. Messen Sie Fluss und Ergebnisse, nie Geschwindigkeit als Ziel, denn in dem Moment, in dem Sie ein Kapazitätssignal zu einem Produktivitätsziel machen, wird es zur Lüge.

4. **Bevor Sie zu einem schweren Skalierungsframework greifen, haben Sie versucht, die teamübergreifenden Abhängigkeiten zu reduzieren, die den Koordinationsbedarf überhaupt erst erschaffen?** Das zählt am meisten für eine große Organisation, denn der Reflex, wenn viele Teams gemeinsam ausliefern müssen, ist, ein Framework wie SAFe, LeSS, oder Scrum@Scale zu kaufen, und schwere Skalierungsmaschinerie schmuggelt oft die Command-and-Control-, planungslastige Overhead zurück, die Agile beheben soll. Die konkurrierende Überlegung ist echt: manche Koordination ist echt gefordert, und Entskalieren zu unabhängigen, strom-ausgerichteten Teams fordert niedrige Kopplung, klaren Besitz, und eine Plattform, reif genug, Teams Self-Service zu erlauben, die Sie vielleicht noch nicht haben. Bringen Sie Beleg zur Diskussion: kartieren Sie die tatsächlichen Abhängigkeiten, die Teams zwingen, aufeinander zu warten, und fragen Sie, wie viele einen absichtlichen Redesign von Teamgrenzen und Dienstbesitz überleben würden. In Unternehmens- und Behördenprogrammen, wo ein Organigramm von Dutzenden Teams gängig ist, ist die ehrliche Frage, ob Sie Koordinationsstruktur hinzufügen, um eine Architektur und ein Teamdesign zu kompensieren, das Sie stattdessen vereinfachen könnten, damit Sie überhaupt weniger Koordination brauchen.

5. **Haben Ihre Teams echten, wiederholten Kontakt mit den Bürgerinnen oder Kundinnen, für die sie bauen, oder kommt Feedback durch Proxys gefiltert an?** Kundinnenzusammenarbeit ist einer der vier Manifest-Werte, und Iterationen ohne echten Nutzerinnenkontakt optimieren still das Falsche, was der teuerste Fehlschlag ist, den Agile verhindern soll. Die Spannung ist, dass direkter Zugang schwer im Maßstab zu arrangieren ist und oft von genau den Beschaffungs-, Datenschutz-, und Sicherheitsregeln behindert wird, die große und öffentliche Organisationen erfüllen müssen, der leichte Pfad ist also, einen Proxy zu ersetzen: eine Business-Analystin, ein Stakeholder-Komitee, oder die Forschungsfolie des letzten Quartals. Bringen Sie Beleg: zählen Sie für Ihre letzten paar Inkremente, wie viele mit einer echten Nutzerin validiert wurden, die die Software tatsächlich nutzte, und wie viele auf der Meinung von jemandem ruhten, was Nutzerinnen wollen. Für einen Behördendienst, fügen Sie hinzu, ob Ihr Usability-Testen die am meisten Betroffenen erreichte, einschließlich Assistive-Technologie-Nutzerinnen und jene mit niedrigem digitalen Vertrauen, denn ein öffentlicher Dienst, der nur für die zuversichtliche Mehrheit funktioniert, hat seine Rechenschaftsverpflichtung versagt, selbst wenn jede Zeremonie planmäßig lief.

6. **Werden Ihre Teams um Ergebnisse und Kadenz finanziert und gesteuert, oder um einen festen Umfang, der still Wasserfall-Verhalten hinter den Zeremonien erzwingt?** Das ist der Unterschied zwischen echter Agilität und gefälschtem Agile, und er wird über dem Team entschieden, darin, wie Geld freigegeben und Erfolg berichtet wird, nicht darin, ob Stand-ups stattfinden. Der konkurrierende Zug ist, dass Finanz-, Portfolio-, und Aufsichtsfunktionen gebaut sind, einen festen Umfang gegen ein festes Budget Jahre im Voraus zu genehmigen, und sie zu bitten, ein Ergebnis mit flexiblem Umfang zu finanzieren, fühlt sich wie ein Kontrollverlust an, gegen den sie sich sträuben werden. Bringen Sie Beleg: verfolgen Sie, wie eine aktuelle Initiative finanziert wurde und worüber sie berichtet, und prüfen Sie, ob Teams an gelieferten Ergebnissen und Fluss gemessen werden oder an Story-Points und Einhaltung eines lange zuvor abgezeichneten Umfangs. In Unternehmens- und Behördenumgebungen, binden Sie das direkt an die Finanzierungs- und Compliance-Hülle (Kapitel 10.6): wenn das Geld an einen entfernten, Alles-oder-Nichts-Go-Live gebunden ist, können die Teams nicht adaptiv sein, egal wie treu sie die Rituale durchführen, und der Fix gehört zum Governance-Modell, nicht zu den Lieferteams.

## Branchenperspektive

**Startup.** Leben Sie die Werte und überspringen Sie die Framework-Debatte. Liefern Sie jede Woche eine funktionierende Scheibe an echte Nutzerinnen, sitzen Sie nah genug an Gründerinnen und frühen Kundinnen, dass Feedback täglich ankommt, und begrüßen Sie eine Richtungsänderung in dem Moment, in dem Beleg sagt, die aktuelle Wette ist falsch. Ihre knappste Ressource ist Engineering-Aufmerksamkeit, schützen Sie also technische Exzellenz (kontinuierliche Integration, automatisierte Tests, Trunk-basierte Entwicklung) selbst unter Einführungsdruck, denn diese Disziplin ist, was Sie nächste Woche günstig schwenkfähig hält.

**Kleinunternehmen.** Ohne agile Coachin und mit engem Budget, behandeln Sie Agile als eine Handvoll Gewohnheiten statt ein Transformationsprogramm, das Sie besetzen: ein kurzer wöchentlicher Zyklus, ein sichtbares Board mit Work-in-Progress-Limits, und eine konkrete Verbesserung jede Woche, die Sie tatsächlich abschließen. Stützen Sie sich auf Kanban, das wenig Zeremonie braucht und zu unterbrechungsgetriebener Arbeit passt, und übernehmen Sie die in bereits gekauften Werkzeugen eingebetteten Praktiken statt einen schwergewichtigen Prozess aufzurichten. Beurteilen Sie den Aufwand danach, ob Sie öfter nützliche Software an Kundinnen ausliefern, nicht danach, wie eng Sie Scrum nachahmen.

**Großunternehmen.** Das Problem ist, viele Teams zu koordinieren, ohne Command-and-Control zu reintroduzieren. Bevorzugen Sie Entskalieren, das heißt, teamübergreifende Abhängigkeiten durch strom-ausgerichtetes Teamdesign und eine solide Plattform zu reduzieren, bevor Sie ein schweres Skalierungsframework übernehmen. Finanzieren und steuern Sie um Ergebnisse (OKRs) und Kadenz statt festen jährlichen Umfang und Story-Points, machen Sie XP-artige Engineering-Praktiken über Teams nicht verhandelbar, und verwalten Sie Lieferung als Portfolio mit Fluss-Kennzahlen und Ergebnismaßen, damit Gruppen sich auf Beleg statt Ritual verbessern.

**Behörde.** Beschaffungsregeln, Transparenz, und öffentliche Rechenschaftspflicht formen jede Wahl. Strukturieren Sie modulare, ergebnisbasierte Verträge mit kürzeren Inkrementen statt eines einzelnen umfangsfesten Megavertrags, denn agile Beschaffung ist, wo öffentliche-Sektor-Agilität am häufigsten gelingt oder scheitert. Bauen Sie Prüfung, Barrierefreiheit, und Sicherheit durch Automatisierung in jedes Inkrement, damit Aufsicht durch den Akt des Bauens erfüllt wird, veröffentlichen Sie Fortschritt und Beleg öffentlichen Werts an Aufsichtsgremien, und kämpfen Sie für echten Zugang zu Bürgerinnen (einschließlich Assistive-Technologie-Nutzerinnen) jede Iteration, denn das ist die Einschränkung, die am häufigsten wegverhandelt wird.

## Beispiele

**Startup.** Ein fünfköpfiges Startup überspringt die Zeremonie-Debatte und lebt die Agile-Werte direkt. Es liefert jede Woche eine funktionierende Scheibe an echte Nutzerinnen, sitzt nah genug an Gründerinnen und frühen Kundinnen, dass Feedback täglich ankommt, und begrüßt nächste Woche eine Richtungsänderung, wenn der Beleg sagt, die aktuelle Wette ist falsch. Das Team weigert sich, technische Exzellenz für Geschwindigkeit zu tauschen, kontinuierliche Integration, automatisierte Tests, und Trunk-basierte Entwicklung sind also selbst unter Einführungsdruck nicht verhandelbar, und jede Freitagsretrospektive produziert eine konkrete Änderung, die das Team vor der nächsten tatsächlich abschließt. Es verfolgt nie Geschwindigkeit als Ziel, sondern misst stattdessen, ob ausgelieferte Arbeit Aktivierung bewegte und ob Durchlaufzeiten schrumpfen.

**Großunternehmen.** Die 60-Team-Transformation eines Telekomunternehmens "macht" zunächst Scrum, sieht aber keine Verbesserung. Teams erhalten immer noch festen jährlichen Umfang und berichten über Geschwindigkeit. Ein Neustart fokussiert sich neu auf Prinzipien: vierteljährliche OKRs ersetzen Feature-Mandate, Teams werden reorganisiert, um teamübergreifende Abhängigkeiten zu reduzieren (Entskalieren), und XP-Praktiken (CI, TDD, Trunk-basierte Entwicklung) werden nicht verhandelbar. Durchlaufzeiten fallen, Defekte sinken, und, entscheidend, das Geschäft beginnt Ergebnisse statt Story-Points zu messen, Agile Lieferung mit der Discovery-Pipeline verbindend (Kapitel 11.1).

**Behörde.** Ein Digitaldienstteam baut eine bürgerinnenorientierte Leistungsanwendung mit Agile innerhalb einer hybriden Governance-Hülle neu: zweiwöchige Inkremente, funktionierende, nutzerinnengetestete Software liefernd; Barrierefreiheit und Sicherheit in jedes Inkrement gebaut; und modulare Beschaffung, die einen einzelnen Festpreisvertrag ersetzt. Echtes Usability-Testen mit Bürgerinnen (einschließlich Assistive-Technologie-Nutzerinnen) jede Iteration fängt Probleme, die der alte Wasserfallprozess ausgeliefert hätte. Das Programm liefert früh einen nutzbaren Dienst und zeigt messbaren öffentlichen Wert gegenüber Aufsichtsgremien. Das ist das Muster hinter modernen öffentliche-Sektor-Erfolgen, und das Gegenmittel zu vergangenen Big-Bang-Fehlschlägen.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Agiles Rendite kommt aus **Risikoreduktion und schnellerer Wertverwirklichung**. Indem sie funktionierende Software früh und oft liefern, verwandeln Teams Unsicherheit kontinuierlich in Beleg, falsches-Ding- und funktioniert-nicht-Fehlschläge fangend, während sie günstig sind, statt bei einem entfernten, teuren Go-Live. Die Forschung hinter moderner Lieferung (die DORA-Erkenntnisse, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), in Kapitel 11.2) zeigt, dass die von Agile geförderten Praktiken (kleine Batches, häufige Veröffentlichungen, schnelles Feedback, technische Exzellenz) mit besserer Lieferung *und* Stabilität *und* organisatorischer Leistung korrelieren. Frühe Inkremente beginnen auch, Wert früher zurückzugeben, das Timing und die Gesamtgröße des ROI gegenüber einer Big-Bang-Veröffentlichung verbessernd, die nichts bis zum Ende zurückgibt.

Bei **[Gesamtbetriebskosten](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** senkt Agile die Kosten der Änderung über die Lebensdauer eines Systems, vorausgesetzt die Engineering-Disziplin ist echt. Sein dominantes Risiko ist *gefälschtes Agile*: Zeremonie ohne Prinzip oder Handwerk, das Meeting-Overhead hinzufügt, während es keinen der Vorteile liefert, und schlimmer sein kann als ein ehrlicher Wasserfall. Der Geschäftsfall ist also bedingt. Der ROI ist hoch, wenn Sie Agile als Denkweise-plus-Engineering übernehmen, und ungefähr null (oder negativ), wenn Sie es als Ritual übernehmen. Machen Sie den Fall gegenüber Führung, indem Sie Agile als kontinuierliche Risikoreduktion und Ergebnismessung rahmen, nicht als "schneller werden", und indem Sie darauf bestehen, dass die Investition technische Praktiken einschließt, nicht nur neue Meetings.

## Anti-Muster und Fallstricke

- **Gefälschtes/Cargo-Cult-Agile:** Zeremonien durchgeführt, während Entscheidungen, Finanzierung, und Denkweise Wasserfall bleiben.
- **Geschwindigkeit als Produktivität:** eine Kapazitätsschätzung in ein Ziel verwandeln, was sie korrumpiert ([Goodharts Gesetz](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark Scrum:** ohne technische Exzellenz in unpflegbaren, defektreichen Code sprinten.
- **Retrospektiven ohne Änderung:** Reflexion, die keine abgeschlossenen Aktionen produziert.
- **Fester Umfang *und* Datum *und* Kosten:** es agil nennen, während Qualität still den Druck absorbiert.
- **Abwesende Kundin:** kein echtes Nutzerinnenfeedback, sodass Iterationen das Falsche optimieren.
- **Framework-Anbetung:** "SAFe/Scrum sagt so" übersteuert die Prinzipien und das Urteil des Teams.
- **Skalieren vor Entskalieren:** schwere Koordinationsframeworks hinzufügen statt Abhängigkeiten zu reduzieren.

## Reifegradmodell

- **Stufe 1, Beginnen.** Wasserfall oder Ad-hoc-Lieferung; Big-Bang-Veröffentlichungen; Arbeit ist reaktiv und planungslastig, ohne iteratives Feedback und keinen geteilten Sinn, warum Agile helfen könnte.
- **Stufe 2, Entwickeln.** Ein paar Teams übernehmen Agile-Zeremonien (Stand-ups, Sprints, Retrospektiven), aber Praxis ist inkonsistent über die Organisation: Denkweise und Engineering-Disziplin hinken den Ritualen hinterher, Geschwindigkeit wird als Ausgabe behandelt, und Umfang ist immer noch im Voraus fixiert.
- **Stufe 3, Standardisieren.** Werte und Prinzipien leiten Arbeit echt organisationsweit, dokumentiert und von jedem Team erwartet: XP-artige technische Exzellenz (CI, automatisiertes Testen, Refactoring, Trunk-basierte Entwicklung) ist Standardpraxis, Teams organisieren sich selbst, Kundinnen sind jede Iteration engagiert, und Retrospektiven produzieren konkrete, abgeschlossene Änderung.
- **Stufe 4, Steuern.** Lieferung wird gegen Baselines gemessen und gesteuert: Teams verfolgen Durchlaufzeit, Bereitstellungshäufigkeit, Änderungsfehlschlagsrate, und Defekt-Escape-Rate (die DORA-artigen Fluss- und Stabilitätskennzahlen), neben Ergebnismaßen, an Key Results gebunden, und vergleichen jede gegen eine bekannte Baseline. Retrospektiv-Aktionen werden bis zum Abschluss verfolgt, nachhaltiges-Tempo-Signale wie Überstunden und Burnout werden überwacht, und Geschwindigkeit wird nie als Produktivitätsziel genutzt. Go- und No-Go-Entscheidungen ruhen auf diesem Beleg statt Meinung.
- **Stufe 5, Orchestrieren.** Adaptive Lieferung ist mit Geschäfts- und Risikoplanung über die Organisation integriert: Ergebnisse (OKRs) treiben Finanzierung und Kadenz, niedrige-Abhängigkeit-Teamdesign (Entskalieren) minimiert Koordinations-Overhead, und hybride Governance erfüllt Aufsicht, ohne Lieferung zu verlangsamen. Kontinuierliche Verbesserung ist kulturell statt zeremoniell, und die Organisation grenzt ihr Portfolio routinemäßig neu ab, formt Teams neu, und balanciert neu, während sich Beleg und Risikobild verschieben.

## Diskussionsideen

1. Bewerten Sie Ihr Team gegen die zwölf Agile-Prinzipien: wo sind Sie agil in Zeremonie, aber nicht in Substanz?
2. Wird Geschwindigkeit in Ihrem Team als Prognose oder als Ziel genutzt, und was hat das mit Verhalten gemacht?
3. Welche XP-technischen Praktiken fehlen, und wie zeigt sich ihre Abwesenheit als Defekte oder langsame Änderung?
4. Bevor Sie ein Skalierungsframework übernehmen, könnten Sie stattdessen teamübergreifende Abhängigkeiten reduzieren?
5. In Ihrem Kontext, was blockiert spezifisch echten Nutzerinnenzugang jede Iteration, und wie könnten Sie es entfernen?
6. Was war die letzte konkrete Änderung, die eine Retrospektive tatsächlich produzierte?

## Wichtigste Erkenntnisse

- Agile ist eine **Denkweise von Werten und Prinzipien**, kein Satz Zeremonien; Frameworks sind Startpunkte, nicht das Ziel.
- Liefern Sie **funktionierende Software häufig**, begrüßen Sie Änderung, und ermächtigen Sie **selbstorganisierende Teams**.
- **Technische Exzellenz (XP-Praktiken) ist nicht verhandelbar.** Agilität ohne sie wird zu schnellem Verfall.
- **Skalieren Sie mit Sorgfalt; bevorzugen Sie Entskalieren.** Reduzieren Sie Abhängigkeiten, bevor Sie Koordinationsframeworks hinzufügen.
- In Unternehmen/Behörden, kombinieren Sie **adaptive Lieferung mit hybrider Governance und agiler Beschaffung**, und kämpfen Sie für echten Nutzerinnenzugang.
- Der ROI ist **kontinuierliche Risikoreduktion und früherer Wert**, aber nur, wenn Agile echt ist, kein Ritual. Siehe Kapitel 1.4, 11.1, 11.2, 10.6, und 11.3.

## Referenzen und weiterführende Literatur

- Kent Beck et al., *Manifesto for Agile Software Development* und seine zwölf Prinzipien (agilemanifesto.org, 2001).
- Ken Schwaber und Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* und *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton und Manuel Pais, *Team Topologies* (Teamdesign und Entskalieren).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (Beleg für Agile-/DevOps-Praktiken).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
