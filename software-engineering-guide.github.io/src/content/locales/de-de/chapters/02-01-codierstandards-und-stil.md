# 2.1 Codierstandards und Stil

## Überblick und Motivation

Codierstandards sind die gemeinsamen Konventionen, die vielen Menschen erlauben, Code zu schreiben, als hätte ein sorgfältiger Autor ihn geschrieben. Sie decken Benennung, Formatierung, Dateilayout, Idiome, Fehlerbehandlung, und die von einem Team bevorzugten Paradigmen ab. In einem kleinen Team kann individueller Geschmack den Tag gewinnen. In einem großen Team (Hunderte oder Tausende Ingenieurinnen, viele Auftragnehmer, hohe Fluktuation) wird Inkonsistenz zu einer Steuer, die Sie bei jedem Lesen, jeder Prüfung, und jedem Onboarding zahlen. Standards verwandeln unzählige kleine stilistische Streits in eine einmalige Entscheidung, die dann eine Maschine für Sie durchsetzt.

Für große Organisationen sind die Einsätze konkret. Code wird weit häufiger gelesen als geschrieben. In Unternehmens- und Behördenumgebungen mag eine Zeile Code von Prüfern, Sicherheitsprüferinnen, und Pflegenden Jahre gelesen werden, nachdem ihr Autor gegangen ist. Konsistenter Stil senkt die mentalen Kosten dieses Lesens, verkleinert die Angriffsfläche für Fehler, und macht automatisierte Analyse zuverlässig über [Linter](https://en.wikipedia.org/wiki/Lint_(software)) (Werkzeuge, die automatisch wahrscheinliche Fehler und Stilverletzungen kennzeichnen), Sicherheitsscanner, und [Refactoring](https://en.wikipedia.org/wiki/Code_refactoring)-Werkzeuge hinweg. Wo Regulierung gilt, wie in Finanzdienstleistungen, Gesundheitswesen, Verteidigung, und öffentlichen Systemen, sind Standards auch Teil des Belegs, dass eine Codebasis wartbar und kontrolliert ist.

Der moderne Ansatz ist, Stil als gelöstes, automatisiertes Anliegen zu behandeln statt als Frage laufenden menschlichen Urteilsvermögens. Formatierer und Linter laufen im Editor, in Pre-Commit-Hooks, und in [kontinuierlicher Integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), dem automatisierten Build-und-Test-Prozess, der bei jeder Änderung läuft. Maschinen setzen den Stil durch, damit Sie Ihre Prüfungsaufmerksamkeit auf Design und Korrektheit verwenden können. Das Ziel ist nicht Einheitlichkeit um ihrer selbst willen. Es ist die Beseitigung von Reibung: Sie sollten sich zwischen Diensten und Teams bewegen können, ohne die Grundlagen neu zu lernen.

## Kernprinzipien

- Konsistenz schlägt individuelle Präferenz; ein einziger vereinbarter Stil, überall angewendet, ist mehr wert als der "beste" Stil, ungleichmäßig angewendet.
- Automatisieren Sie Durchsetzung. Formatierer und Linter sind die Wahrheitsquelle, nicht Code-Review-Kommentare über Abstände.
- Optimieren Sie für die Leserin und die Pflegerin, nicht die ursprüngliche Autorin.
- Bevorzugen Sie Konventionen, die die breitere Sprachgemeinschaft bereits nutzt, gegenüber maßgeschneiderten Hausregeln.
- Machen Sie den Standard leicht zu übernehmen: Bieten Sie gemeinsame Konfigurationen, Vorlagen, und Werkzeuge statt eines PDFs, das niemand liest.
- Stilregeln sollten wenige, begründbare, und eindeutige sein; jede Regel hat einen Durchsetzungsmechanismus, oder sie ist nur ein Vorschlag.
- Benennung ist die hebelstärkste Lesbarkeitsentscheidung und verdient explizite Anleitung.

## Empfehlungen

### Einen kanonischen Stilleitfaden pro Sprache übernehmen

Für jede Sprache, die Sie nutzen, übernehmen Sie einen weithin anerkannten Stilleitfaden als Basislinie (zum Beispiel den Community- oder Anbieterleitfaden für diese Sprache) und dokumentieren Sie nur die Deltas, die Ihre Organisation braucht. Erfinden Sie keinen Hausstil von Grund auf. Veröffentlichen Sie Ihre Wahl an einem zentralen, auffindbaren Ort, und versionieren Sie sie wie Code.

### Formatierer zu nicht verhandelbaren Standardeinstellungen machen

Nutzen Sie einen meinungsstarken automatischen Formatierer für jede Sprache, die einen hat, mit einer einzigen gemeinsamen Konfiguration, eingecheckt ins Repository. Formatierung sollte nie in der Prüfung aufkommen, weil sie automatisch beim Speichern angewendet und in CI verifiziert wird. Wo einer Sprache ein starker Formatierer fehlt, wählen Sie eine Linter-Konfiguration und behandeln Sie sie genauso.

### Linter als durchgesetzte Tore laufen lassen, nicht als Ratschlag

Konfigurieren Sie Linter mit einem vereinbarten Regelsatz, lassen Sie den Build bei Verletzungen scheitern, und halten Sie den Regelsatz in der [Versionskontrolle](https://en.wikipedia.org/wiki/Version_control), damit Änderungen durch Prüfung gehen. Trennen Sie automatisch behebbare Regeln (automatisch anwenden) von Regeln, die menschliches Urteilsvermögen brauchen (kennzeichnen und blockieren). Führen Sie neue Regeln im "Warn"-Modus ein, räumen Sie den Rückstand auf, dann befördern Sie sie zu "Fehler".

### Auf mehreren Schichten durchsetzen

Bieten Sie Editor-Integration für sofortiges Feedback, Pre-Commit-Hooks für lokale Durchsetzung, und CI-Prüfungen als autoritatives Tor. Je früher Sie eine Verletzung erwischen, desto günstiger ist sie. CI muss die letzte Absicherung sein, weil lokale Hooks umgangen werden können.

### Benennung explizite Regeln geben

Standardisieren Sie Groß-/Kleinschreibungskonventionen pro Sprache, verlangen Sie absichtsoffenbarende Namen, verbieten Sie irreführende Abkürzungen, und definieren Sie Konventionen für Booleans, Sammlungen, Einheiten, und asynchrone Operationen. Schreiben Sie Ihr Domänenvokabular in ein gemeinsames Glossar, damit dasselbe Konzept überall denselben Namen hat.

### Polyglotte Konsistenz bewusst steuern

In einer Codebasis, die mehrere Sprachen umfasst, streben Sie konsistente Konzepte an (Fehlerbehandlungsmuster, Logging-Struktur, Projektlayout), selbst wo sich die Syntax unterscheidet. Bieten Sie sprachspezifische Konfigurationen aus einem zentralen Repository, damit ein neuer Dienst die Standards automatisch durch Vorlagen oder Gerüstbau erbt.

### Idiome und Paradigmen kodifizieren

Gehen Sie über Formatierung hinaus. Schreiben Sie Ihre bevorzugten Idiome auf, wie Fehler zu behandeln sind, wie Module strukturiert werden, und wann Ausnahmen versus Ergebnistypen zu nutzen sind, zusammen mit den Paradigmen, die Ihre Teams bevorzugen. Hier lebt echte Lesbarkeit und Wartbarkeit.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| Strikter Auto-Formatierer, keine Konfiguration | Beendet alle Formatierungsdebatten; sofortige Konsistenz; triviales Onboarding | Manche unbeliebten Wahlen sind nicht verhandelbar; großer initialer Diff bei erster Anwendung |
| Konfigurierbarer Linter mit Hausregeln | Auf Organisationsbedürfnisse zugeschnitten; kann echte Fehlerverhütungsregeln kodieren | Konfigurationsdrift; Regel-Bikeshedding; Pflegelast |
| Community-Standard pauschal übernommen | Vertraut für Neueinstellungen; starkes Werkzeug-Ökosystem; geringe Pflege | Passt möglicherweise nicht zu Nischen-Organisationsbeschränkungen; gelegentlich unbeholfene Regeln |
| Maßgeschneiderter interner Standard | Passt genau zur Organisation | Teuer zu schreiben und zu pflegen; unvertraut für Neueinstellungen; schwaches Werkzeug |
| Team-für-Team-Autonomie | Hohe lokale Moral; kontextspezifisch | Zersplitterung; schmerzhafte teamübergreifende Mobilität; uneinheitliches Werkzeug |

Durchgesetzte Standardeinstellungen tauschen etwas individuelle Autonomie gegen große kollektive Gewinne: weniger Prüfungsreibung, schnelleres Onboarding, und verlässliche Automatisierung. Das Hauptrisiko ist, den Standard zu Hunderten von Regeln zu übertechnisieren, die alle verlangsamen, ohne echte Fehler zu verhindern. Halten Sie den Regelsatz klein und belegbasiert, und neigen Sie dazu, einen bestehenden Standard zu übernehmen, damit die Pflege günstig bleibt.

## Fragen zur Diskussion mit Ihrem Team

1. **Welche Linter-Regeln sollten den Build scheitern lassen, und wie befördern Sie eine Regel von Warnung zu Fehler, ohne alle anzuhalten?** Dieses Kapitel argumentiert, dass jede Regel einen Durchsetzungsmechanismus braucht, und dass neue Regeln im Warn-Modus landen, ihren Rückstand geräumt bekommen, dann zu Fehler wechseln sollten. In einem großen Team blockiert das Umschalten einer Regel zu Fehler gegen eine unsaubere Codebasis über Nacht Hunderte nicht verwandter Änderungen. Bringen Sie harte Belege zur Besprechung: die aktuelle Verletzungszahl für jede Kandidatenregel, und ob sie automatisch behebbar ist oder menschliches Urteilsvermögen braucht. In Unternehmens- und Behördenumgebungen speist die Bestehen/Scheitern-Linie auch Prüfungstore, ein mehrdeutiger Regelsatz schwächt also Ihre Compliance-Geschichte. Entscheiden Sie einen gestaffelten Rollout: Automatisch beheben, was Sie können, die Bereinigung budgetieren, dann sperren.

2. **Wenn Sie einen Formatierer zum ersten Mal auf Ihren Altcode anwenden, wie verhindern Sie, dass diese Neuformatierung git blame ruiniert und Prüfungen ertränkt?** Die Abwägungstabelle warnt vor einem großen initialen Diff, und der Anti-Muster-Abschnitt kritisiert das Mischen von Neuformatierungs-Commits mit Logikänderungen. Eine einzige umfassende Neuformatierung schreibt Tausende Zeilen um und lässt blame auf die Neuformatierung statt die echte Autorin zeigen, was jedem schadet, der Jahre später debuggt. Machen Sie die Neuformatierung als einen isolierten, klar beschrifteten Commit, und registrieren Sie ihn in einer Blame-Ignorier-Datei, damit die Geschichte nützlich bleibt. Für Prüfer, die verfolgen, wer was geändert hat, ist diese Isolierung der Unterschied zwischen sauberem Beleg und Rauschen. Vereinbaren Sie die Reihenfolge, bevor Sie den Code berühren, nicht danach.

3. **Wer besitzt Ihr Benennungsglossar und Domänenvokabular, und wie wird ein neuer Begriff hinzugefügt?** Das Kapitel nennt Benennung die hebelstärkste Lesbarkeitsentscheidung und bittet Sie, das Domänenvokabular in ein gemeinsames Glossar zu schreiben. Ohne benannte Besitzerin bekommt dasselbe Konzept drei verschiedene Namen über Teams hinweg, und statische-Analyse- und Suchwerkzeuge verlieren Verlässlichkeit. Bringen Sie Beispiele von Konzepten, die bereits widersprüchliche Namen in Ihrer Codebasis haben, als konkretes Signal. Weisen Sie eine Besitzerin und einen leichtgewichtigen Vorschlagsweg zu, damit das Hinzufügen oder Umbenennen eines Begriffs eine kleine, geprüfte Änderung ist statt ein Streit in jeder Pull-Request. Die Antwort ändert Onboarding: eine Neueinstellung liest ein Glossar statt Absicht aus inkonsistentem Code zurückzuentwickeln.

4. **Übernehmen Sie für jede Sprache einen anerkannten Community- oder Anbieterstilleitfaden pauschal, und wo sind Hausdeltas tatsächlich gerechtfertigt?** Dieses Kapitel argumentiert, dass Sie einen bestehenden Standard als Basislinie nehmen und nur die Deltas dokumentieren sollten, die Ihre Organisation braucht, weil ein maßgeschneiderter Standard teuer zu schreiben und unvertraut für Neueinstellungen ist. Der konkurrierende Zug ist real: eine interne Einschränkung (eine Sicherheitsregel, ein Altframework, ein Barrierefreiheitsmandat) kollidiert manchmal wirklich mit dem Community-Standard, und jedes Delta, das Sie behalten, ist eine Regel, die Sie jetzt besitzen und für immer pflegen. Bringen Sie die vorgeschlagene Deltaliste zur Besprechung, jede mit der konkreten Einschränkung, die sie motiviert, und seien Sie bereit, jedes Delta zu streichen, das nur Geschmack ist. In Unternehmens- und Behördenumgebungen bedeutet eine Basislinie, die der breiteren Sprachgemeinschaft entspricht, auch, dass Auftragnehmer und neue Zulieferer bereits fließend ankommen, was Onboarding verkürzt und den Wartbarkeitsbeleg stärkt, nach dem Prüfer suchen.

5. **In einer polyglotten Codebasis, welche Konventionen sind wirklich universell, und welche bleiben sprachlokal, und wie verhindern Sie, dass Pro-Repository-Konfigurationen driften?** Das Kapitel bittet um konsistente Konzepte (Fehlerbehandlung, Logging-Struktur, Projektlayout) über Sprachen hinweg, selbst wo sich die Syntax unterscheidet, und um sprachspezifische Konfigurationen, bereitgestellt aus einem zentralen Repository, damit neue Dienste Standards automatisch erben. Die Spannung ist, dass das Aufzwingen der Idiome einer Sprache auf eine andere unbeholfenen, unidiomatischen Code produziert, während es jedem Team zu überlassen, seine eigene Konfiguration abzuzweigen, damit endet, dass "der Standard" nichts bedeutet. Bringen Sie ein Inventar Ihrer aktuellen Pro-Repository-Linter- und Formatierer-Konfigurationen und einen Diff, der zeigt, wie weit sie bereits auseinandergedriftet sind, als konkretes Signal. Für eine große Organisation, die Dutzende Dienste betreibt, entscheiden Sie den Verteilungsmechanismus (Vorlagen, Gerüstbau, ein gemeinsames Konfigurationspaket), damit eine Regeländerung sich einmal verbreitet, statt von Hand in jedes Repository kopiert zu werden.

6. **Wann ist das Deaktivieren einer Regel legitim, wer prüft die Unterdrückung, und wie verhindern Sie, dass pauschale Deaktivierungen den Standard aushöhlen?** Der Anti-Muster-Abschnitt markiert weitverbreitete Inline-Unterdrückungen als Zeichen, dass eine Regel falsch ist oder ein Team aufgegeben hat, doch eine starre Keine-Ausnahmen-Politik drängt Menschen dazu, schlechteren Code zu schreiben, nur um den Linter zufriedenzustellen. Vereinbaren Sie einen leichtgewichtigen Weg: Eine Unterdrückung muss einen Grund tragen, im engstmöglichen Umfang sitzen, und in der Prüfung sichtbar sein statt in einer globalen Ignorier-Datei begraben. Bringen Sie die aktuelle Zahl der Unterdrückungen pro Regel und pro Repository, denn eine hunderte Male unterdrückte Regel sagt Ihnen etwas über die Regel, nicht den Code. In regulierter und öffentlicher Arbeit schwächen unerklärte pauschale Unterdrückungen die Prüfungsgeschichte direkt, da die Pipeline nicht mehr zeigen kann, dass zusammengeführter Code wirklich die vereinbarten Tore bestand.

## Branchenperspektive

**Startup.** Geschwindigkeit gewinnt, übernehmen Sie also die Community-Formatierer- und Linter-Standardeinstellungen für Ihre eine Sprache ab Tag eins und verdrahten Sie sie in einen Pre-Commit-Hook und CI, bevor die zweite Ingenieurin ankommt. Schreiben Sie keinen Hausstil, den Sie keine Zeit haben zu pflegen: Die im Repository versendete Konfiguration ist der ganze Standard. Wenn Sie eine zweite Sprache hinzufügen, greifen Sie zum kanonischen Leitfaden dieser Sprache statt Konventionen von Grund auf zu erfinden.

**Kleinunternehmen.** Ohne dedizierte Werkzeugspezialistin und mit knappem Budget stützen Sie sich vollständig auf den kostenlosen, meinungsstarken Formatierer, der mit oder neben Ihrer Sprache versendet wird, und akzeptieren Sie seine Standardeinstellungen statt sie abzustimmen. Das ist ein klarer Kaufen-über-Bauen-Fall: einen benutzerdefinierten Regelsatz zu pflegen kostet Zeit, die Sie nicht haben, während ein fertiger Formatierer nichts kostet und die Stildebatte sofort beendet. Halten Sie die Konfiguration im Repository, damit der eine Auftragnehmer, den Sie nächstes Jahr einstellen, sie ohne Gespräch erbt.

**Großunternehmen.** Im großen Maßstab ist die Aufgabe Governance über viele Teams: ein zentrales Technikstandards-Repository, das die gemeinsamen Formatierer- und Linter-Konfigurationen pro Sprache hält, neue Dienste, generiert aus Vorlagen, die diese Konfigurationen ziehen, und CI-Tore, die nicht konforme Zusammenführungen blockieren. Versionieren Sie den Regelsatz wie Code und leiten Sie Änderungen durch periodische Überprüfung, damit Standards sich bewusst weiterentwickeln statt zu driften. Die Auszahlung ist, dass Ingenieurinnen sich zwischen Teams in vertrauten Code bewegen, und automatisiertes Werkzeug, das verlässliches Signal produziert, weil jedes Repository konsistent ist.

**Behörde.** Beschaffung und Rechenschaftspflicht formen die Wahl: Schreiben Sie einen spezifischen Stil- und Sicherheitsregelsatz als Teil der Betriebsgenehmigungsanforderungen vor, und lassen Sie die Pipeline einen Bericht ausgeben, der zeigt, dass jede zusammengeführte Änderung die vereinbarten Tore als Prüfungsbeleg bestand. Weil ein Formatierer automatisch angewendet wird, sieht Code von mehreren Zulieferern und Auftragnehmern konsistent aus, was die öffentliche Wartungsaufgabe lange nach Vertragsende schützt. Bevorzugen Sie anerkannte Community-Basislinien gegenüber maßgeschneiderten Regeln, damit der Standard transparent ist und jeder zukünftige Lieferant ihn ohne proprietäre Bindung übernehmen kann.

## Beispiele

**Startup.** Ein vierköpfiges Startup übernimmt die Community-Formatierer- und Linter-Standardeinstellungen für seine eine Sprache ab Tag eins und verdrahtet sie in einen Pre-Commit-Hook und CI, damit niemand über Abstände in der Prüfung streitet. Weil die Konfiguration im Repository versendet wird, erben die fünfte und sechste Neueinstellung sie automatisch und sehen nie einen Formatierungskommentar. Als das Team später eine zweite Sprache hinzufügt, greift es zum Standardleitfaden dieser Sprache statt einen Hausstil zu erfinden, den es keine Zeit hat zu pflegen.

**Großunternehmen.** Eine große Bank betreibt Dienste in Java, Python, und TypeScript über Dutzende Teams. Sie veröffentlicht ein zentrales "Technikstandards"-Repository, das die gemeinsamen Formatierer- und Linter-Konfigurationen für jede Sprache hält. Neue Dienste werden aus einer Vorlage generiert, die diese Konfigurationen zieht, sodass jedes Repository konform startet. CI blockiert Zusammenführungen bei jeder Verletzung, und eine vierteljährliche Überprüfung regelt Regeländerungen. Die Onboarding-Zeit für Ingenieurinnen, die zwischen Teams wechseln, sinkt merklich, weil jedes Repository vertraut aussieht.

**Behörde.** Eine öffentliche Behörde, die ein Altsystem modernisiert, schreibt einen Barrierefreiheits- und Sicherheits-Linting-Regelsatz als Teil ihrer Betriebsgenehmigungsanforderungen (ATO) vor, der formalen Genehmigung, um das System in Produktion zu betreiben. Stilkonformität wird Teil des Prüfungsbelegs: Die Pipeline produziert einen Bericht, der zeigt, dass aller zusammengeführter Code die vereinbarten [statische-Analyse](https://en.wikipedia.org/wiki/Static_program_analysis)-Tore bestand. Weil ein Formatierer automatisch angewendet wird, produzieren Auftragnehmer von mehreren Zulieferern visuell konsistenten Code, was die langfristige Wartungsaufgabe der Regierung nach Vertragsende erleichtert.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Kosten der Einführung von Standards sind größtenteils einmalig: Leitfäden wählen, Werkzeuge verdrahten, und einen großen initialen Neuformatierungs-Commit anwenden. Die wiederkehrenden Kosten sind niedrig, weil Durchsetzung automatisiert ist. Die Kosten, Standards *nicht* einzuführen, sind wiederkehrend und summierend: Jede Prüfung verbringt Minuten mit Stil, jedes Onboarding ist langsamer, statische-Analyse-Werkzeuge produzieren Rauschen, und inkonsistenter Code versteckt Fehler. Über eine große Organisation summieren sich diese Minuten zu Vollzeitäquivalent-Verlusten.

Die Rendite zeigt sich als reduzierte Prüfungslatenz, weniger stilbezogene Prüfungskommentare, schnelleres Onboarding, und höheres Signal von automatisiertem Werkzeug. In regulierten Umgebungen gibt es eine weitere Rendite in Prüfungsbereitschaft: nachweisbare, durchgesetzte Kontrollen reduzieren den Aufwand und das Risiko von Compliance-Prüfungen. Um Führungskräften den Fall darzulegen, rahmen Sie Standards als günstigen, hebelstarken Hebel auf Entwicklerproduktivität und Prüfungshaltung, und setzen Sie eine Zahl auf die aktuellen Kosten der Inkonsistenz mithilfe von Prüfungskommentar-Analyse und Onboarding-Umfragedaten.

## Anti-Muster und Fallstricke

- **Stil in Code-Review debattiert:** das Zeichen, dass Durchsetzung nicht automatisiert ist; verschieben Sie die Regel in Werkzeuge.
- **Das ungelesene Standarddokument:** eine Wiki-Seite ohne Durchsetzung ist Dekoration; jede Regel braucht einen Mechanismus.
- **Regelwucherung:** Hunderte pedantischer Regeln, die Arbeit verlangsamen, ohne Fehler zu verhindern.
- **Konfigurationsdrift:** Jedes Repository zweigt seine eigene Linter-Konfiguration ab, bis "der Standard" nichts bedeutet.
- **Das ganze Repository mitten in Funktionsarbeit formatieren:** Neuformatierungs-Commits mit Logikänderungen mischen zerstört Prüfung und blame; machen Sie große Neuformatierungen in isolierten, klar beschrifteten Commits.
- **Den Linter mit pauschalen Unterdrückungen ignorieren:** weitverbreitete Inline-Deaktivierungen signalisieren eine falsche Regel oder ein Team, das aufgegeben hat.
- **Standards ohne Eigentümerschaft:** keine klare Besitzerin bedeutet, dass Regeln sich nie weiterentwickeln und verrotten.

## Reifegradmodell

- **Stufe 1, Beginnen:** Stil ist pro Autor und reaktiv; keine gemeinsamen Konfigurationen; Formatierung wird in der Prüfung debattiert und von wem auch immer sich an diesem Tag am meisten kümmert entschieden.
- **Stufe 2, Entwickeln:** Einzelne Teams übernehmen einen Formatierer und Linter, aber Konfigurationen und Regelsätze variieren von Team zu Team und Repository zu Repository, sodass Konsistenz an der Grenze jedes Teams endet.
- **Stufe 3, Standardisieren:** Zentrale gemeinsame Konfigurationen pro Sprache sind dokumentiert und organisationsweit durchgesetzt; CI blockiert nicht konforme Zusammenführungen; neue Repositorys erben die Standards automatisch durch Vorlagen oder Gerüstbau.
- **Stufe 4, Steuern:** Der Standard wird mit Daten gemessen und gesteuert: Verletzungsraten, Unterdrückungszahlen, stilbezogene Prüfungskommentare, und Onboarding-Zeit werden gegen Baselines verfolgt, und Regeländerungen werden aufgrund dieser Belege statt Meinung befördert oder ausgemustert.
- **Stufe 5, Orchestrieren:** Standards werden kontinuierlich verbessert und über die Organisation integriert; polyglotte Idiome und Domänenvokabular sind dokumentiert und durchgesetzt, Durchsetzung ist nahezu reibungsfrei, und der Regelsatz passt sich an, während sich Sprachen, Werkzeuge, und Organisationsbedürfnisse verschieben.

## Diskussionsideen

- Wo liegt die Linie zwischen einer durchgesetzten Regel und einer dokumentierten Richtlinie, die dem Urteilsvermögen der Ingenieurin vertraut?
- Wie sollte die Organisation eine geliebte Community-Regel handhaben, die mit einer echten internen Einschränkung kollidiert?
- Wer besitzt die Standards, und wie werden Regeländerungen vorgeschlagen, debattiert, und ohne Störung ausgerollt?
- In einer polyglotten Codebasis, welche Konventionen sollten wirklich universell sein, und welche sollten sprachlokal bleiben?
- Wie rüsten Sie Standards auf eine große Altcodebasis nach, ohne eine störende Big-Bang-Neuformatierung?
- Welche Rolle sollte KI-unterstütztes Werkzeug beim Vorschlagen oder Durchsetzen von Idiomen über mechanische Formatierung hinaus spielen?

## Wichtigste Erkenntnisse

- Behandeln Sie Stil als automatisiertes, gelöstes Problem, damit Menschen Design und Korrektheit prüfen.
- Übernehmen Sie bestehende Community-Standards und dokumentieren Sie nur die Deltas.
- Setzen Sie auf Editor-, Pre-Commit-, und CI-Schichten durch, mit CI als autoritativem Tor.
- Halten Sie den Regelsatz klein, begründbar, und zentral geregelt.
- Benennung und Idiome, nicht Abstände, sind, wo Lesbarkeit wirklich gewonnen wird.

## Referenzen und weiterführende Literatur

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt und David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell und Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (Hrsg.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* und Sprach-Stilleitfäden (als Referenzbeispiele)
