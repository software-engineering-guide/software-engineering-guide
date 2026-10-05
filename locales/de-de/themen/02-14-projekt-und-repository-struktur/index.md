# 2.14 Projekt- und Repository-Struktur

## Überblick und Motivation

Projekt- und Repository-Struktur ist die physische Organisation einer Codebasis: die Ordner, Dateien, und Benennungskonventionen, die entscheiden, wo eine gegebene Sache lebt. Ein *Repository* (oft "Repo" abgekürzt) ist der [versionskontrollierte](https://en.wikipedia.org/wiki/Version_control) Container, der die Dateien eines Projekts und ihre Geschichte hält. Ein *Projekt*, manchmal *Lösung* genannt, wenn es mehrere verwandte Komponenten gruppiert, ist die logische Softwareeinheit, die Sie bauen. Struktur ist die Karte, die Sie nutzen, um diese Software zu finden, zu verstehen, und zu ändern.

In einem kleinen Team kann eine Person das gesamte Layout im Kopf behalten. In einem großen Team, mit Hunderten oder Tausenden Ingenieurinnen, häufigen Wechseln zwischen Teams, und Auftragnehmern, die kommen und gehen, erhebt jedes anders organisierte Repository eine frische kognitive Steuer. Wenn Sie ein unvertrautes Repo öffnen, sollten Sie erraten können, wo die Quelle, die Tests, die Dokumentation, und die Bereitstellungskonfiguration leben, ohne ein Handbuch zu lesen. Wenn jedes Repo diese Fragen gleich beantwortet, ist Mobilität günstig und Onboarding schnell. Wenn jedes Repo eine Schneeflocke ist, wird jeder Kontextwechsel zu einem kleinen Forschungsprojekt.

In Unternehmens- und Behördenumgebungen ist konsistente Struktur auch ein Kontroll- und Absicherungsanliegen. Prüfer, Sicherheitsprüferinnen, und langfristige Pflegende, oft Jahre nach dem Weiterziehen der ursprünglichen Autoren arbeitend, müssen verlässlich Spezifikationsdokumente, Lizenzdateien, Sicherheitsrichtlinien, und Build-Definitionen lokalisieren. Ein vorhersagbares Layout lässt auch automatisiertes Werkzeug (Scanner, Abhängigkeitsanalysatoren, Compliance-Prüfungen) über ein ganzes Portfolio von Systemen hinweg gleich funktionieren. Dieses Kapitel behandelt Struktur also als Konvention, die Sie einmal entscheiden und überall anwenden. Es ist eng verwandt mit Codierstandards und Stil (Kapitel 2.1), Versionskontrolle und Quellcodeverwaltung (Kapitel 2.6), und Dokumentation (Kapitel 2.7).

## Kernprinzipien

- Folgen Sie dem *[Prinzip der geringsten Überraschung](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: Das Layout sollte dem entsprechen, was eine erfahrene Ingenieurin erwarten würde, damit nichts auswendig gelernt werden muss.
- Konsistenz über Repositorys hinweg schlägt lokale Cleverness; eine ausreichend einheitliche Struktur überall ist mehr wert als die perfekte Struktur an einem Ort.
- Die [README](https://en.wikipedia.org/wiki/README) ist die Haustür; eine Neuling sollte sich allein daran orientieren können.
- Machen Sie Struktur selbstbeschreibend durch Benennung, damit Ordner und Dateien ihren Zweck ankündigen.
- Setzen Sie Struktur mit Gerüstbau und Vorlagen durch, nicht mit Willenskraft und Prüfungskommentaren.
- Trennen Sie Belange physisch: Quelle, Tests, Dokumentation, Build, und Bereitstellung gehören an eigenständige, vorhersagbare Orte.
- Organisieren Sie Abhängigkeiten so, dass sie in eine Richtung fließen, von stabilen Kernen zu volatilen Rändern.

## Empfehlungen

### Ein konsistentes Top-Level-Layout übernehmen

Definieren Sie einen Standardsatz von Top-Level-Ordnern, den jedes Repository nutzt, wo anwendbar, und dokumentieren Sie, wofür jeder ist. Eine gängige, anbieterneutrale Konvention umfasst: einen Quellordner (oft `src`) für Produktionscode; einen Testordner (oft `test` oder `tests`) für automatisierte Tests; einen `docs`-Ordner für Dokumentation; einen `build`-Ordner für Build-Definitionen und -Ausgaben; einen `deploy`-Ordner für Bereitstellung und *[Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (maschinenlesbare Definitionen von Servern, Netzwerken, und Diensten, behandelt in Kapitel 8.2); einen `scripts`-Ordner für Automatisierung und Entwicklerwerkzeug; einen `examples`-Ordner für lauffähige Beispiele; und einen `spec`- oder `specification`-Ordner für Anforderungs- und Designspezifikationen. Nicht jedes Repo braucht jeden Ordner, aber wo ein Belang existiert, sollte er am erwarteten Ort mit dem erwarteten Namen leben.

### Die README zum Einstiegspunkt machen

Verlangen Sie eine README-Datei an der Repository-Wurzel als den einzigen, kanonischen Ausgangspunkt. Sie sollte sagen, was das Projekt ist, wie man es baut und ausführt, wie man die Tests ausführt, wo tiefere Dokumentation zu finden ist, wer es besitzt, und wie man beiträgt. Die README ist nicht die gesamte Dokumentationssammlung; sie ist der Index, der auf den Rest zeigt (Kapitel 2.7). Behandeln Sie eine fehlende oder veraltete README als Fehler, denn sie ist das Erste, was jede neue Ingenieurin, Prüferin, oder Integratorin lesen wird.

### Editor- und Konfigurationsdateien standardisieren

Checken Sie gemeinsame Editor- und Werkzeugkonfiguration ins Repository ein, damit jede Mitwirkende automatisch konsistentes Verhalten bekommt. Eine `.editorconfig`-Datei (eine einfache, editor-unabhängige Datei, die Leerraum-, Einrückungs-, und Zeilenendenregeln definiert) hält grundlegende Formatierung über verschiedene Editoren und Betriebssysteme hinweg einheitlich. Fügen Sie eine Ignorier-Datei für das Versionskontrollsystem hinzu (damit Build-Ausgaben und lokale Artefakte nie committet werden), zusammen mit den gemeinsamen Formatierer- und Linter-Konfigurationen aus Kapitel 2.1. Diese Dateien machen die Konventionen des Repositorys aktiv, nicht nur dokumentiert.

### Benennungs- und Ordnerkonventionen definieren

Vereinbaren Sie Konventionen zur Benennung von Ordnern und Dateien (Groß-/Kleinschreibung, Trenner, Singular versus Plural, und erforderliche Suffixe wie jene, die Tests markieren) und wenden Sie sie einheitlich an. Namen sollten Absicht offenbaren und dem Domänenvokabular entsprechen, das anderswo in der Organisation genutzt wird. Das Ziel ist einfach: Ein Pfad sollte Bedeutung kommunizieren, damit das Lesen eines Ordner- oder Dateinamens Ihnen sagt, was drin ist, ohne ihn zu öffnen.

### Schichten und Abhängigkeiten bewusst organisieren

Strukturieren Sie die Codebasis so, dass ihre Architekturschichten im Ordnerlayout erscheinen, und dass Abhängigkeiten in eine einzige, sinnvolle Richtung fließen. Übergeordnete Richtlinien sollten nicht von untergeordnetem Detail abhängen. Gemeinsamer, stabiler Code sollte dort sitzen, wo viele Module ihn erreichen können, ohne Zyklen zu schaffen. Wenn Sie die Schichtung physisch machen, reflektiert im Verzeichnisbaum, respektieren Ingenieurinnen sie eher, und Verletzungen sind leichter in der Prüfung und in automatisierten Abhängigkeitsprüfungen zu erkennen.

### Struktur mit Gerüstbau und Vorlagen durchsetzen

Bieten Sie *[Gerüstbau](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, die automatisierte Generierung eines Startprojekts, damit neue Repositorys bereits korrekt beginnen. Eine *Vorlage* oder ein *Cookiecutter* (ein parametrisiertes Projektgerüst, das aus Antworten auf ein paar Eingabeaufforderungen ein fertiges Repository generiert) kodiert das Standardlayout, die README, die Konfigurationsdateien, und die [CI](https://en.wikipedia.org/wiki/Continuous_integration)-Einrichtung an einem Ort. Wenn Ingenieurinnen neue Dienste aus einer gemeinsamen Vorlage erstellen, wird Konsistenz zum Standard statt zur Ambition, und Verbesserungen an der Vorlage fließen zu zukünftigen Projekten.

### Struktur über viele Repositorys hinweg im großen Maßstab konsistent halten

Behandeln Sie das Layout selbst als geregelten Standard: zentral gepflegt wie jeder andere technische Standard (Kapitel 1.7), und versioniert wie Code (Kapitel 2.6). Veröffentlichen Sie ihn, bieten Sie die Vorlagen, die ihn implementieren, und erlauben Sie Abweichungen nur durch einen dokumentierten Ausnahmeprozess, damit "der Standard" seine Bedeutung behält. Im Portfolio-Maßstab kommt fast der gesamte Wert der Struktur aus ihrer Einheitlichkeit über Repositorys hinweg, Drift ist also das Hauptrisiko, das zu managen ist.

### Struktur die Monorepo-versus-Multi-Repo-Wahl informieren lassen

Verbinden Sie Struktur mit der in Kapitel 2.6 behandelten Repository-Grenzentscheidung. Ein *[Monorepo](https://en.wikipedia.org/wiki/Monorepo)* (ein Repository, das viele Projekte hält) braucht eine klare interne Konvention zur Trennung von Projekten und ihrem gemeinsamen Code, damit der eine Baum navigierbar bleibt. Ein *Multi-Repo*-Ansatz (viele kleine Repositorys, eines pro Projekt oder Dienst) braucht starke repositoryübergreifende Konsistenz, damit sich jedes Repo vertraut anfühlt, obwohl es für sich steht. So oder so ist eine dokumentierte, vorlagenbasierte Struktur, was Navigation vorhersagbar hält. Die Grenzentscheidung ändert, wo Sie die Konvention anwenden, nicht ob Sie eine brauchen.

## Abwägungen: Vor- und Nachteile

| Wahl | Vorteile | Nachteile |
|---|---|---|
| Strikter organisationsweiter Standardlayout | Sofortige Vertrautheit; portable Ingenieurinnen; einheitliches Werkzeug | Gelegentlich schlechte Passung für ungewöhnliche Projekte; braucht Governance |
| Pro-Team-Layoutfreiheit | Lokale Optimierung; hohe Autonomie | Zersplitterung; kostspieliger Kontextwechsel; uneinheitliches Werkzeug |
| Gerüstbau und Vorlagen | Standardmäßig korrekte Repos; Änderungen verbreiten sich | Vorlagenpflege; Driftrisiko generierter Repos |
| Tiefe, geschichtete Ordnerhierarchie | Explizite Struktur; klare Grenzen | Navigationsaufwand; lange Pfade; Übertechnisierungsrisiko |
| Flaches, seichtes Layout | Leicht zu überblicken; wenig Zeremonie | Schlechte Trennung; bricht zusammen, während das Projekt wächst |

Die dominante Abwägung ist Einheitlichkeit gegen Autonomie. Ein einziges Standardlayout beseitigt Reibung für die vielen Ingenieurinnen, die sich zwischen Codebasen bewegen, auf Kosten des gelegentlichen Projekts, dessen Bedürfnisse nicht sauber in die Form passen. In einer großen Organisation überwiegt der kollektive Gewinn aus Vertrautheit fast immer diesen lokalen Verlust. Deshalb ist die empfohlene Haltung ein starker Standard plus ein dokumentierter Ausnahmeweg (Kapitel 1.7), statt entweder starrer Einheitlichkeit oder ungesteuerter Freiheit. Eine sekundäre Abwägung ist Tiefe gegen Einfachheit: genug Struktur, um echte Belange zu trennen, aber nicht so viel, dass Navigation zu einer Wanderung durch leere Ordner wird.

## Fragen zur Diskussion mit Ihrem Team

1. **Wenn eine Ingenieurin in ein unvertrautes Repo von uns wechselt, wie lange dauert es, bis sie die Tests, die Bereitstellungskonfiguration, und die Besitzerin finden kann?** Das ist die Navigationssteuer, die Struktur beseitigen soll, und im Portfolio-Maßstab wird sie Tausende Male im Jahr in kleinen Zuwächsen bezahlt, die sich zu ernsthaft verlorener technischer Zeit summieren. Der Punkt des Prinzips der geringsten Überraschung ist, dass eine erfahrene Ingenieurin erraten können sollte, wo Quelle, Tests, Dokumentation, und Bereitstellung leben, ohne ein Handbuch zu lesen, der ehrliche Test ist also, ob diese Vermutung über Ihre Repos hinweg gelingt. Bringen Sie eine echte Zahl zur Besprechung: Zeitnehmen Sie sich bei der Orientierung in zwei oder drei unvertrauten internen Repositorys, oder ziehen Sie Onboarding-Daten dazu, wie lange Neueinstellungen für eine erste Änderung brauchen. Wenn die Antwort in Tagen der Forschung statt Minuten des Erkennens gemessen wird, haben Sie die Kosten von Schneeflocken-Repos quantifiziert, und das rechtfertigt die einmalige Investition in ein Standardlayout, das jedes Repo teilt.

2. **Erscheinen unsere Architekturschichten im Ordnerbaum, oder verstecken sich Abhängigkeitszyklen in einem flachen Layout?** Struktur geht um mehr als Auffindbarkeit: Wenn Sie Schichtung physisch machen, respektieren Ingenieurinnen sie, und Prüfende und automatisierte Abhängigkeitsprüfungen können Verletzungen erkennen, während ein flacher Haufen unpassende Kopplung und Zyklen unbemerkt einschleichen lässt, bis Änderung gefährlich wird. In einem großen, langlebigen System ist das, was übergeordnete Richtlinien davon abhält, still von untergeordnetem Detail abzuhängen, und es ist genau die Art von Erosion, die günstig zu verhindern und teuer rückgängig zu machen ist. Bringen Sie Ihren Abhängigkeitsgraphen oder führen Sie eine schnelle Prüfung durch: Gibt es Zyklen, und hängt irgendetwas Stabiles von etwas Volatilem ab? Die Antwort sollte Sie drängen, Schichten in Verzeichnissen zu reflektieren und automatisierte Abhängigkeitsrichtungsprüfungen hinzuzufügen, damit die Grenzen im Baum sichtbar und in der Pipeline durchgesetzt sind, statt nur im mentalen Modell von jemandem zu leben.

3. **Beginnen unsere neuen Repositorys korrekt aus einer Vorlage, oder verlassen wir uns auf eine Wiki-Seite und gute Absichten?** Durch Gerüstbau durchgesetzte Struktur ist der Standard; in einem Dokument beschriebene Struktur driftet, denn Realität folgt dem, was Repos generiert, nicht dem, was eine Seite sagt, wie sie aussehen sollten. Für eine große oder regulierte Organisation ist das auch ein Absicherungsanliegen: Wenn jedes Repo aus einer gemeinsamen Vorlage generiert wird, finden Sicherheitsscanner, Abhängigkeitsanalysatoren, und Prüfer die Lizenz, die Sicherheitsrichtlinie, die Spezifikation, und die Build-Definition jedes Mal am selben Ort, über Zulieferer und Jahre hinweg. Bringen Sie die Belege: Wie viele Ihrer jüngsten Repos wurden aus der Standardvorlage gerüstet gegenüber von Hand zusammengesetzt, und wie weit sind die vorlagenbasierten seitdem gedriftet? Die Aktion ist, die Vorlage zum einzigen einfachen Weg zu machen, ein Repo zu starten, sie als versionierten Standard mit dokumentiertem Ausnahmeweg zu regeln, und Drift automatisch zu erkennen, denn Einheitlichkeit ist, wo fast der gesamte Wert der Struktur lebt.

4. **Haben wir entschieden, ob unser Standard ein Monorepo oder viele separate Repositorys umspannt, und hält tatsächlich dieselbe Konvention auf beiden Seiten dieser Grenze?** Die Repository-Grenzwahl ändert, wo Sie die Konvention anwenden, nicht ob Sie eine brauchen, und sie falsch zu treffen bedeutet einen einzigen riesigen Baum, den niemand navigieren kann, oder eine Wucherung von Repos, die sich jeweils fremd anfühlen. Ein Monorepo braucht eine klare interne Konvention zur Trennung von Projekten und ihrem gemeinsamen Code, damit der eine Baum navigierbar bleibt, während ein Multi-Repo-Ansatz starke repositoryübergreifende Konsistenz braucht, damit sich jedes eigenständige Repo noch vertraut anfühlt. Bringen Sie das aktuelle Inventar: wie viele Repos Sie haben, wie gemeinsamer Code innerhalb jedes Monorepos getrennt ist, und einen zeitgemessenen Test, ob eine Ingenieurin ein Projekt im großen Baum so schnell findet, wie sie eines in einem eigenständigen Repo findet. Für ein großes Unternehmen oder ein Behördenprogramm, wo verschiedene Zulieferer separate Repositorys liefern, entscheiden Sie bewusst, welche Teile der Konvention universell sind und welche grenzspezifisch, denn Prüfer und Plattformwerkzeug müssen gleich funktionieren, ob der Code als ein Baum oder fünfzig ankommt.

5. **Wer besitzt unseren Strukturstandard, und was passiert tatsächlich, wenn ein Projekt wirklich nicht hineinpasst?** Im Portfolio-Maßstab kommt fast der gesamte Wert der Struktur aus Einheitlichkeit, die echten Risiken sind also ein besitzerloser Standard, der verrottet, und ein so vager Ausnahmeweg, dass jedes Team still sein eigenes Layout erfindet. Die Spannung ist zwischen starrer Einheitlichkeit, die zu keinem ungewöhnlichen Projekt passt, und ungesteuerter Freiheit, die alles zersplittert, und die gesunde Antwort ist ein starker Standard plus ein dokumentierter, prüfbarer Ausnahmeprozess, geregelt von einer benannten Besitzerin und versioniert wie Code. Bringen Sie die Belege: Gibt es eine einzige verantwortliche Besitzerin, ein versioniertes Standarddokument mit Änderungsprotokoll, ein Protokoll gewährter Ausnahmen und warum, und eine Zahl undokumentierter Abweichungen, die Sie in freier Wildbahn finden können. In Unternehmens- und Behördenumgebungen ist eine nirgends protokollierte Ausnahme eine Kontrolllücke, verknüpfen Sie also jede Abweichung mit einer schriftlichen Rechtfertigung und einem Überprüfungsdatum, und stellen Sie sicher, dass Beschaffungsverträge, die das Layout vorschreiben, auch benennen, wer Abweichungen davon genehmigen darf.

6. **Machen unsere README und eingecheckten Konfigurationsdateien unsere Konventionen aktiv, oder sind sie dekorativ?** Eine README ist die Haustür, und die eingecheckte `.editorconfig`, Ignorier-Datei, und Linter-Konfiguration sind, was Konventionen selbstdurchsetzend macht, doch das sind die ersten Dinge, die veralten, und die letzten, die jemand bemerkt, bis eine Prüferin oder eine Neueinstellung das Projekt nicht zum Bauen bringen kann. Die Spannung ist zwischen einer schlanken README, die aktuell bleibt, und einer gründlichen, die driftet, und zwischen darauf vertrauen, dass Menschen Code korrekt formatieren, und gemeinsame Konfiguration es automatisch durchsetzen lassen. Bringen Sie eine Stichprobe: Ziehen Sie fünf Repos und prüfen Sie, wie viele READMEs tatsächlich sagen, was das Projekt ist, wie man es baut, testet, und ausführt, und wer es besitzt, und wie viele die gemeinsamen Konfigurationsdateien tragen statt sich auf individuelle Gewohnheiten zu verlassen. Für eine große oder regulierte Organisation, wo Integratoren, Sicherheitsprüferinnen, und langfristige Pflegende die README vor allem anderen lesen, behandeln Sie eine fehlende oder veraltete Haustür als Fehler mit einer Besitzerin, und prüfen Sie Konfigurationsdatei-Präsenz automatisch, damit Konformität nicht von gutem Willen abhängt.

## Branchenperspektive

**Startup.** Geschwindigkeit gewinnt, vereinbaren Sie also ein einfaches, ausreichend flaches Layout für Ihr erstes Repo (src, test, docs, scripts, eine ausgefüllte README, eine `.editorconfig`, und Ignorier-Dateien) und speichern Sie es denselben Nachmittag als leichtgewichtige Vorlage. Generieren Sie den zweiten Dienst daraus, damit sich beide Repos vertraut anfühlen und ein neuer Auftragnehmer sich in Stunden statt durch Zurückentwickeln einer Schneeflocke einarbeitet. Widerstehen Sie tiefen Hierarchien und schwerer Governance, die Sie noch nicht brauchen; die ganze Rendite hier ist, dass zwei Gründerinnen und ein Auftragnehmer eine Karte teilen.

**Kleinunternehmen.** Ohne Plattformspezialistin und mit knappem Budget übernehmen Sie das konventionelle Layout, das Ihre Sprache oder Ihr Framework bereits annimmt, statt eines zu erfinden, damit fertiges Werkzeug und jede Neueinstellung bereits darauf vortrainiert ankommen. Kaufen Sie Gerüstbau (einen Framework-Generator oder eine Cookiecutter-Vorlage), statt Ihren eigenen zu bauen, und verbringen Sie Ihren knappen Aufwand darauf, eine ausgefüllte README aktuell zu halten. Diese README ist die günstigste Versicherung, die Sie für den Tag haben, an dem die eine Person, die das Layout kannte, weiterzieht.

**Großunternehmen.** Über viele Teams und Hunderte Repositorys ist das Ziel Einheitlichkeit: Veröffentlichen Sie einen versionierten Strukturstandard, generieren Sie jeden neuen Dienst aus gemeinsamen Vorlagen, erkennen Sie Drift automatisch, und erlauben Sie Abweichungen nur durch einen dokumentierten Ausnahmeprozess. Weil jedes Repo gleich aussieht, ist eine Ingenieurin, die einem neuen Team zugewiesen wird, innerhalb von Stunden produktiv, und portfolioweite Sicherheits- und Abhängigkeitsscanner finden die Lizenz, die Sicherheitsrichtlinie, und die Build-Definition jedes Mal am selben Ort. Budgetieren Sie die Vorlagenpflege und Drift-Erkennung explizit, denn diese Instandhaltung ist, was den Standard im großen Maßstab bedeutsam hält.

**Behörde.** Beschaffung, Transparenz, und langfristige Rechenschaftspflicht formen das Layout, schreiben Sie also eine gemeinsame Struktur in die Lieferstandards vor, die jeden Zulieferer binden. Verlangen Sie einen `specification`-Ordner, der Code mit genehmigten Anforderungen verknüpft, eine Lizenz- und Sicherheitsrichtliniendatei an der Wurzel, und einen `deploy`-Ordner, der die Infrastructure-as-Code-Definitionen hält, damit Prüfer Compliance-Artefakte in jedem System auf dieselbe Weise lokalisieren. Weil Auftragnehmer verschiedener Zulieferer alle einer Karte folgen, kostet Wartung nach Vertragsende weit weniger, und die Öffentlichkeit gewinnt eine begründbare, inspizierbare Spur von Anforderung zu laufendem Code.

## Beispiele

**Startup.** Ein dreiköpfiges Startup vereinbart ein einfaches Standardlayout für sein erstes Repo (src, test, docs, scripts, eine ausgefüllte README, eine .editorconfig, und Ignorier-Dateien) und speichert es als leichtgewichtige Vorlage. Als sie einen Monat später ihren zweiten Dienst hochziehen, generieren sie ihn aus dieser Vorlage, damit sich beide Repos bereits vertraut anfühlen und der neue Auftragnehmer sich an einem Nachmittag einarbeitet. Sie widerstehen tiefen Ordnerhierarchien, die sie noch nicht brauchen, den Baum flach genug haltend, um ihn auf einen Blick zu überblicken. Die Kosten waren ein Nachmittag Einrichtung, und es erspart ihnen die Schneeflocken-Wucherung, die sonst jedes zukünftige Repo zu einem kleinen Forschungsprojekt machen würde.

**Großunternehmen.** Ein multinationaler Einzelhändler betreibt Hunderte Dienste über mehrere Sprachen. Sein Plattformteam veröffentlicht einen versionierten Repository-Strukturstandard und eine Reihe von Projektvorlagen, die ihn implementieren. Jeder neue Dienst wird aus einer Vorlage generiert, kommt also mit den Standardordnern `src`, `test`, `docs`, `deploy`, und `scripts`, einer ausgefüllten README, einer `.editorconfig`, Ignorier-Dateien, und einer funktionierenden CI-Pipeline an. Weil jedes Repository gleich aussieht, ist eine Ingenieurin, die einem neuen Team zugewiesen wird, innerhalb von Stunden produktiv, und organisationsweite Sicherheits- und Abhängigkeitsscanner laufen einheitlich, weil sie Dateien immer dort finden, wo sie sie erwarten.

**Behörde.** Eine nationale Behörde, die Altsysteme modernisiert, schreibt als Teil ihrer Lieferstandards für alle Zulieferer ein gemeinsames Repository-Layout vor. Jedes Repository muss einen `specification`-Ordner enthalten, der Code mit genehmigten Anforderungen verknüpft, eine dokumentierte README, eine Lizenz- und Sicherheitsrichtliniendatei an der Wurzel, und einen `deploy`-Ordner, der die Infrastructure-as-Code-Definitionen hält (Kapitel 8.2). Weil Auftragnehmer verschiedener Zulieferer alle derselben Struktur folgen, können die Prüfer der Behörde Compliance-Artefakte in jedem System auf dieselbe Weise lokalisieren, und langfristige Wartung nach Vertragsende kostet weit weniger, weil ankommende Pflegende die Karte bereits kennen.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Kosten der Einführung eines Strukturstandards sind größtenteils einmalig: das Layout vereinbaren, die Vorlagen bauen, und die Konvention dokumentieren. Die wiederkehrenden Kosten sind niedrig, konzentriert auf die Pflege der Vorlagen und die Regelung von Ausnahmen. Die Kosten, *keinen* Standard zu haben, sind wiederkehrend und summierend: Jede Ingenieurin, die ein unvertrautes Repo öffnet, zahlt eine Navigationssteuer, jedes Onboarding läuft langsamer, und automatisiertes Werkzeug muss pro Repo konfiguriert werden, weil nichts dort ist, wo Sie es erwarten. Über eine große Organisation summieren sich diese kleinen Reibungen zu ernsthaften Verlusten technischer Zeit.

Die Rendite zeigt sich als schnelleres Onboarding, günstigere Mobilität zwischen Teams, höheres Signal von portfolioweitem Werkzeug, und, in regulierten Umgebungen, niedrigere Prüfungs- und Langzeitwartungskosten, weil Artefakte immer auffindbar sind. Die *Gesamtbetriebskosten* (TCO, die vollständigen Lebenszeitkosten des Bauens, Betreibens, und Pflegens eines Systems) sinken am meisten in langlebigen Systemen, wo die von vorhersagbarer Struktur profitierenden Pflegenden normalerweise nicht die Autoren sind, die sie erstellten. Um Führungskräften den Fall darzulegen, rahmen Sie Struktur als günstigen, hebelstarken Standard, der Entwicklerproduktivität und Prüfungsbereitschaft verbessert, und setzen Sie eine Zahl auf die heutigen Kosten der Inkonsistenz mithilfe von Onboarding-Zeit-Daten und dem Aufwand, in unvertrauten Repositorys nach Dingen zu suchen.

## Anti-Muster und Fallstricke

- **Das Schneeflocken-Repository:** jedes Repo anders organisiert, sodass jedes von Grund auf neu gelernt werden muss.
- **Die fehlende oder veraltete README:** keine Haustür, Neulinge zwingend, zurückzuentwickeln, wie man das Projekt baut und ausführt.
- **Struktur durch Dokument, nicht durch Vorlage:** eine Wiki-Seite beschreibt das Standardlayout, aber nichts generiert oder erzwingt es, sodass die Realität davon abdriftet.
- **Vorlagendrift:** aus einer Vorlage generierte Repositorys divergieren über Zeit, und Verbesserungen an der Vorlage erreichen sie nie.
- **Übertechnisierte Hierarchie:** tiefe Verschachtelungen fast leerer Ordner, die Zeremonie hinzufügen, ohne Navigation zu helfen.
- **Vermischte Belange:** Quelle, Tests, Build-Ausgaben, und Geheimnisse ohne klare Trennung durcheinandergewürfelt.
- **Committete Build-Ausgaben und lokale Artefakte:** generierte Dateien eingecheckt, weil Ignorier-Regeln nie eingerichtet wurden, Geschichte und Diffs verschmutzend.
- **Schichtverletzungen, versteckt durch flache Struktur:** keine physischen Grenzen, sodass Abhängigkeitszyklen und unpassende Kopplung unbemerkt einschleichen.

## Reifegradmodell

- **Stufe 1 (Beginnen):** Jedes Repository wird ad hoc von seinen Autoren organisiert, reagierend auf das, was der Moment braucht; Layouts variieren stark; READMEs fehlen oder sind unzuverlässig; Neulinge müssen durch jedes Repo von Hand geführt werden.
- **Stufe 2 (Entwickeln):** Grundlegende Konventionen existieren informell, und viele Repos ähneln einander; manche Teams behalten ein eigenes Startlayout; aber es gibt keinen autoritativen Standard, kein gemeinsames Gerüst, und Struktur driftet merklich von Team zu Team.
- **Stufe 3 (Standardisieren):** Ein dokumentierter, versionierter Strukturstandard wird über die Organisation durchgesetzt; neue Repositorys werden aus gemeinsamen Vorlagen generiert, die ein Standardlayout, README, Konfigurationsdateien, und CI tragen; Abweichungen durchlaufen einen dokumentierten Ausnahmeprozess statt still zu geschehen.
- **Stufe 4 (Steuern):** Konformität mit dem Standard wird mit Daten gemessen und gesteuert: automatisierte Prüfungen berichten, welcher Anteil der Repos dem Layout entspricht, wie weit vorlagenbasierte Repos gedriftet sind, README-Vollständigkeit, und Abhängigkeitsrichtungsverletzungen, alle gegen Baselines verfolgt; Onboarding- und Navigationszeiten werden gemessen; Ausnahmen werden protokolliert und überprüft, und Vorlagenänderungen werden aufgrund von Belegen statt Meinung genehmigt.
- **Stufe 5 (Orchestrieren):** Struktur wird kontinuierlich verbessert und ist adaptiv: Vorlagenverbesserungen verbreiten sich automatisch zu bestehenden Repositorys, Strukturgovernance ist mit Sicherheit, Compliance, und Plattformwerkzeug integriert, und der Standard entwickelt sich bewusst weiter, während sich Sprachen, Architekturen, und das Portfolio verschieben, hohe Einheitlichkeit haltend, während sich die Organisation darum verändert.

## Diskussionsideen

- Welche Top-Level-Ordner sollten wirklich universell über Ihre Organisation sein, und welche sollten optional sein?
- Wie verhindern Sie, dass aus einer Vorlage generierte Repositorys über Zeit davon abdriften?
- Wo liegt die Linie zwischen einer hilfreichen, geschichteten Hierarchie und übertechnisierter Ordnerzeremonie?
- Wie sollte sich Ihr Strukturstandard, wenn überhaupt, zwischen einem Monorepo- und einem Multi-Repo-Ansatz unterscheiden?
- Was ist der richtige Ausnahmeprozess für ein Projekt, dessen echte Bedürfnisse nicht ins Standardlayout passen?
- Wie viel Ihrer Struktur kann automatisch geprüft werden, und was verlässt sich noch auf menschliche Prüfung?
- Wer besitzt den Strukturstandard und seine Vorlagen, und wie werden Änderungen vorgeschlagen und ausgerollt?

## Wichtigste Erkenntnisse

- Organisieren Sie jedes Repository so, dass jede Ingenieurin jede Codebasis nach Erwartung navigieren kann, dem Prinzip der geringsten Überraschung folgend.
- Übernehmen Sie ein konsistentes Top-Level-Layout (Quelle, Test, Dokumentation, Build, Bereitstellung, Skripte, Beispiele, Spezifikation) und machen Sie die README zum Einstiegspunkt.
- Checken Sie Editor- und Werkzeugkonfiguration ein (wie `.editorconfig`), damit Konventionen aktiv sind, nicht nur aufgeschrieben.
- Setzen Sie Struktur mit Gerüstbau und Vorlagen durch, damit neue Repositorys standardmäßig korrekt sind.
- Im großen Maßstab liegt der Wert in Einheitlichkeit: regeln Sie den Standard, managen Sie Drift, und erlauben Sie Abweichungen nur durch dokumentierte Ausnahme.

## Referenzen und weiterführende Literatur

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt und David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, und Hyrum Wright (Hrsg.), *Software Engineering at Google*
- Scott Chacon und Ben Straub, *Pro Git*
- EditorConfig-Projektdokumentation (als Referenzstandard für Editorkonfiguration)
