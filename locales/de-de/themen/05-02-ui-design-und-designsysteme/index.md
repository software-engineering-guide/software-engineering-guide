# 5.2 UI-Design und Designsysteme

## Überblick und Motivation

[User-Interface-(UI)-Design](https://en.wikipedia.org/wiki/User_interface_design) ist das Handwerk, zu formen, was Menschen sehen und berühren: Layout, [Typografie](https://en.wikipedia.org/wiki/Typography), Farbe, Abstand, Steuerelemente, und Zustände. Ein [Designsystem](https://en.wikipedia.org/wiki/Design_system) nimmt dieses Handwerk und verwandelt es in einen geteilten, wiederverwendbaren, verwalteten Vermögenswert: eine dokumentierte Menge von Prinzipien, Komponenten, Mustern, und Tokens, aus denen jedes Team schöpft, damit das ganze Produkt als eines aussieht und sich verhält. UI-Design entscheidet, wie ein Bildschirm aussehen sollte. Ein Designsystem entscheidet, wie zehntausend Bildschirme über viele Teams hinweg kohärent bleiben.

Für eine große Organisation ist das Designsystem die einzelne Investition mit dem höchsten Hebel in UI-Qualität und Liefergeschwindigkeit. Ohne eines erfindet jedes Team Buttons, Formulare, Modals, und Fehlerbehandlung neu, jedes leicht unterschiedlich, jedes separat gepflegt, jedes separat kaputt. Nutzerinnen bezahlen das in Verwirrung und Misstrauen; das Geschäft bezahlt es in dupliziertem Aufwand und ungleicher Qualität. Ein Designsystem verwandelt einmalige Designentscheidungen in wiederverwendbares Kapital: lösen Sie [Barrierefreiheit](https://en.wikipedia.org/wiki/Accessibility), [Responsivität](https://en.wikipedia.org/wiki/Responsive_web_design), und Branding einmal in einer Komponente, und jedes Team erbt das Ergebnis.

Unternehmen und Behörden fügen zwei spezifische Drücke hinzu. Erstens Maßstab: Hunderte Anwendungen, viele von Anbieterinnen gebaut oder durch Fusionen erworben, müssen sich alle wie eine Organisation anfühlen. Zweitens Langlebigkeit und Wandel: Marken werden aufgefrischt, Behörden werden reorganisiert, und eine einzelne Plattform muss möglicherweise mehrere Marken oder Unterbehörden aus einer Codebasis bedienen. Ein gut architektiertes Designsystem, mit richtigem Theming und Tokenisierung, macht diese umfassenden Änderungen handhabbar statt katastrophal.

## Kernprinzipien

- Konsistenz senkt [kognitive Last](https://en.wikipedia.org/wiki/Cognitive_load); ein Button sollte überall gleich aussehen und sich gleich verhalten.
- Designentscheidungen sind Vermögenswerte: erfassen Sie sie einmal als wiederverwendbare Komponenten und Tokens.
- Tokens sind die Quelle der Wahrheit für visuelle Entscheidungen; Komponenten konsumieren Tokens, nie fest codierte Werte.
- Barrierefreiheit und Responsivität werden in Komponenten eingebaut, nicht pro Bildschirm angeschraubt.
- Ein Designsystem ist ein Produkt mit Nutzerinnen (Entwicklerinnen und Designerinnen), kein Einmal-Liefergut.
- Visuelle Hierarchie leitet Aufmerksamkeit: Type, Farbe, und Raum sollten Wichtigkeit offensichtlich machen.
- Governance hält ein System kohärent; Beitrag hält es lebendig.

## Empfehlungen

### Das System in Schichten strukturieren: Tokens, Komponenten, Muster

Design-Tokens sind benannte, plattformunabhängige Werte für Farbe, Abstand, Typografie, Radius, Erhebung, und Bewegung: die atomaren Entscheidungen. Bauen Sie sie in Stufen: eine primitive Palette (Rohwerte), semantische Tokens (`color-action-primary`, `space-inset-md`), die Bedeutung tragen, und Komponentenebene-Tokens, wo Sie sie brauchen. Komponenten konsumieren die semantischen Tokens, damit sich eine einzelne Änderung überall fortpflanzt. Über Komponenten sitzen Muster: bewährte Kompositionen wie eine Datentabelle, ein mehrstufiges Formular, oder ein leerer Zustand. Dokumentieren Sie alle drei Schichten an einem Ort, mit lebendigen Beispielen und Nutzungsanleitung.

### Die visuellen Grundlagen richtig hinbekommen

Richten Sie eine typografische Skala mit klarer Hierarchie und großzügigem Zeilenabstand für Lesbarkeit ein, und halten Sie sich an eine begrenzte Menge Größen und Gewichte. Definieren Sie Farbe als System, mit genug Kontrast für Barrierefreiheit (siehe das Barrierefreiheitskapitel) und semantischen Rollen, statt roher Farbtöne, verstreut durch die UI. Nutzen Sie eine Abstandsskala und ein Layout-Raster, damit Ausrichtung und Rhythmus konsistent bleiben, ohne Pro-Bildschirm-Rätselraten. Visuelle Hierarchie sollte die primäre Aktion und die wichtigste Information auf einen Blick offensichtlich machen.

### Responsiv und Mobile-First gestalten

Gestalten Sie zuerst für den kleinsten vernünftigen Viewport, verbessern Sie dann für größere Bildschirme. Das zwingt Sie, den essentiellen Inhalt und die Steuerelemente zu priorisieren. Nutzen Sie flüssige Layouts und relative Einheiten, damit sich Oberflächen an jeden Bildschirm anpassen, statt zwischen ein paar festen Haltepunkten zu springen. Machen Sie Touch-Ziele groß genug, und stellen Sie sicher, dass Interaktionen mit Touch, Maus, und Tastatur funktionieren. Besonders in Behörden nehmen Sie an, dass ein bedeutsamer Anteil Ihrer Nutzerinnen auf kleinen, älteren, oder günstigen Geräten ist.

### Design-zu-Entwicklung-Übergabe und Parität zu einer Anliegen erster Klasse machen

Ein Designsystem zahlt sich nur aus, wenn die ausgelieferte UI dem beabsichtigten Design entspricht und weiter entspricht. Zielen Sie auf eine einzige Quelle der Wahrheit: Tokens, aus dem Designwerkzeug exportiert, speisen direkt in Code, damit Designerinnen und Ingenieurinnen sich auf dieselben Werte beziehen. Stellen Sie eine codierte Komponentenbibliothek bereit, die Ingenieurinnen tatsächlich nutzen werden, mit denselben Namen und Props wie die Designkomponenten. Nutzen Sie visuelles Regressionstesten (automatisierter Vergleich gerenderter UI gegen genehmigte Baseline-Bilder) und Design-Prüfprüfungen, um Drift zu erwischen. Und messen Sie "Design-Code-Parität" als explizite Gesundheitskennzahl: den Anteil der UI, gebaut aus System-Komponenten versus Einmal-Code.

### Theming und White-Labeling im Unternehmensmaßstab unterstützen

Architektieren Sie für mehrere Marken von Anfang an, falls es irgendeine Chance gibt, dass Sie sie brauchen werden. Weil Komponenten semantische Tokens konsumieren, ist ein Theme nur eine andere Menge Token-Werte, ein Markenrefresh oder eine neue Untermarke wird also eine Datenänderung, keine Code-Neuschreibung. Unterstützen Sie helle und dunkle Themes, Hochkontrastmodi, und Pro-Mandant-Branding durch denselben Mechanismus. Halten Sie markenspezifische Logik aus Komponenten heraus, und schieben Sie sie stattdessen in Token-Mengen und Konfiguration.

### Das System als Produkt verwalten

Geben Sie dem Designsystem ein dediziertes Team, eine Roadmap, Versionierung, ein Änderungsprotokoll, und einen Support-Kanal. Buchstabieren Sie aus, wie Teams neue Komponenten beitragen, und wie diese geprüft und befördert werden. Balancieren Sie zentrale Kontrolle (um Kohärenz und Barrierefreiheit zu bewahren) mit einem Beitragsmodell (damit sich das System mit echten Bedürfnissen entwickelt, statt zu einem Engpass zu werden). Kommunizieren Sie Abschreibungen und Migrationen klar, und geben Sie konsumierenden Teams genug Vorlaufzeit.

## Abwägungen: Vor- und Nachteile

| Entscheidung | Vorteile | Nachteile |
|---|---|---|
| Ein Designsystem bauen | Konsistenz, Geschwindigkeit, Barrierefreiheit einmal, leichtere Rebrands | Vorab- und laufende Kosten, braucht dediziertes Team |
| Ein Fertigsystem übernehmen | Schneller Start, bewährte Muster | Generischer Look, schwerer für einzigartige Marke und Bedürfnisse anzupassen |
| Strikte zentrale Governance | Kohärenz, Qualität, Barrierefreiheit garantiert | Kann Teams zum Engpass werden, fühlt sich bürokratisch an |
| Offenes Beitragsmodell | Entwickelt sich mit echten Bedürfnissen, geteilter Besitz | Risiko von Drift und Inkonsistenz ohne Prüfung |
| Schwere Tokenisierung und Theming | Günstige Rebrands und Multi-Marken-Unterstützung | Mehr Abstraktion, steilere Lernkurve |

Designsysteme tauschen Vorab- und Governance-Kosten gegen langfristige Konsistenz und Geschwindigkeit. Für ein kleines Produkt mit einem Team zahlt sich der Overhead möglicherweise nicht aus. Für eine große Organisation mit vielen Teams und langlebigen Produkten ist die Frage nicht, ob man ein System haben sollte, sondern wie viel zu investieren und wie es zu verwalten. Das häufigste Bedauern ist Unterinvestition in Governance- und Paritätswerkzeug: das System existiert auf Papier, aber Teams driften still davon weg.

## Fragen zur Diskussion mit Ihrem Team

1. **Wie ist unsere Token-Architektur gestuft, und ist es Komponenten verboten, fest codierte Werte zu nutzen?** Die ganze Auszahlung eines Designsystems (günstige Rebrands, Multi-Marken-Theming, Barrierefreiheit einmal gelöst) hängt davon ab, dass Komponenten semantische Tokens wie `color-action-primary` konsumieren statt rohe Farbtöne und Pixelwerte, verstreut durch Code. Entscheiden Sie jetzt über die Stufen: eine primitive Palette, semantische Tokens, die Bedeutung tragen, und Komponentenebene-Tokens nur, wo Sie sie wirklich brauchen. Überabstraktion ist ein echtes Risiko, einigen Sie sich also, wie viele Schichten zu viel sind und wie eine Entwicklerin schnell das richtige Token findet. Bringen Sie ein Grep fest codierter Farben und Abstände über Ihre Codebasis als Beleg für Drift. Wenn Markenlogik in Komponenten gebacken ist, wird ein Rebrand zu einer Code-Neuschreibung statt einer Konfigurationsänderung, was genau die Katastrophe ist, die Tokenisierung verhindern soll.

2. **Wie messen und verteidigen wir Design-Code-Parität, und welches Werkzeug erwischt Drift automatisch?** Ein Designsystem, das nur als Designdatei existiert, ist ein Stickerbogen: Ingenieurinnen bauen sowieso alles neu, und die ausgelieferte UI weicht langsam von der Absicht ab. Einigen Sie sich auf eine explizite Paritätskennzahl (den Anteil der UI, gebaut aus System-Komponenten versus Einmal-Code) und verdrahten Sie visuelles Regressionstesten in CI, damit gerenderte Bildschirme gegen genehmigte Baselines verglichen werden. Das zählt im Unternehmens- und Behördenmaßstab, weil sich Hunderte Anwendungen, viele von Anbieterinnen gebaut oder durch Fusionen geerbt, alle wie eine Organisation anfühlen müssen. Bringen Sie die aktuelle Paritätszahl und eine Liste der obersten maßgeschneiderten Komponenten, die Teams immer wieder neu bauen. Wenn niemand die Kennzahl oder die Regressionssuite besitzt, gewinnt Drift bereits still.

3. **Wie verwalten wir Beitrag, Abschreibung, und Migration, damit das System weder Teams zum Engpass wird noch fragmentiert?** Strikte zentrale Kontrolle garantiert Kohärenz und Barrierefreiheit, kann aber das Designsystem-Team zu einem Engpass machen, um den Teams herumrouten; offener Beitrag hält das System lebendig, riskiert aber divergente Varianten ohne Prüfung. Entscheiden Sie den Beitragspfad: wie ein Team eine neue Komponente vorschlägt, wer sie prüft, und wie sie befördert wird. Einigen Sie sich ebenso, wie Sie brechende Änderungen kommunizieren, denn Abschreibungen ohne Migrationsunterstützung und Vorlaufzeit lassen konsumierende Teams stocken oder abspalten. Bringen Sie Beispiele von Komponenten, die Teams außerhalb des Systems bauten, und fragen Sie, warum sie nicht zurück beitrugen. Die Antwort offenbart üblicherweise, ob Ihre Governance ein Dienst oder ein Hindernis ist.

4. **Wie garantieren wir, dass Barrierefreiheit einmal in Komponenten gelöst wird, und was hindert ein Team daran, eine unzugängliche Einmalkomponente auszuliefern?** Das stärkste Argument für ein Designsystem ist, dass Farbkontrast, Fokuszustände, Tastaturbedienung, und Screenreader-Semantik einmal gelöst und überall geerbt werden, aber dieses Versprechen bricht in dem Moment zusammen, in dem Teams ihre eigenen Steuerelemente von Hand rollen. Für eine große Organisation liegt hier das größte rechtliche und Reputationsrisiko, weil ein einzelnes unzugängliches Zahlungsformular oder Datumsauswahl echte Nutzerinnen blockieren und Beschwerden über jedes Produkt auslösen kann, das es kopierte. Wägen Sie zentrale Durchsetzung (zugängliche Komponenten plus ein Linter oder Prüftor, das rohes Markup ablehnt) gegen Teamautonomie ab, und entscheiden Sie, wo die harte Linie liegt. Bringen Sie die Ergebnisse einer Barrierefreiheitsprüfung, eine Liste von Komponenten mit ihrem Konformitätsstatus, und eine Anzahl maßgeschneiderter Steuerelemente, die Teams außerhalb des Systems neu bauten. In Unternehmens- und Behördenumgebungen ist das keine Nettigkeit: Pflichten wie WCAG, Section 508, und EN 301 549 machen Konformität zu einer Beschaffungs- und Prüfungsanforderung, eine Komponentenbibliothek mit dokumentierter Konformität ist also selbst ein Compliance-Vermögenswert.

5. **Wie viele Marken, Mandantinnen, und Themes muss dieses System bedienen, und haben wir die Token-Schicht jetzt dafür architektiert, statt sie später nachzurüsten?** Theming ist günstig, wenn Sie dafür gestalteten, und brutal, wenn nicht, weil eine Marke oder Mandantin, die nie erwartet wurde, Markenlogik zurück in Komponenten zwingt und den ganzen Sinn der Tokenisierung zunichtemacht. Für ein großes Team formt diese Entscheidung Jahre der Arbeit: eine Plattform, die mehrere Marken bedienen muss, ein helles und dunkles Theme, einen Hochkontrastmodus, und Pro-Mandant-Branding braucht eine semantische Token-Schicht, sauber genug, dass ein Theme nur eine andere Menge Werte ist. Balancieren Sie diese Flexibilität gegen Überabstraktion, denn ein Token-Baum, den niemand navigieren kann, ist sein eigenes Scheitern. Bringen Sie die Roadmap der Marken und Mandantinnen, die Sie vorhersehen können, die Anzahl der aktuell im Spiel befindlichen Themes, und alle Komponenten, die bereits markenspezifische Logik durchsickern lassen. In Unternehmens- und Behördenkontexten fügen Fusionen, Übernahmen, und Behördenreorganisationen routinemäßig Marken hinzu, die Sie nicht planten, für Multi-Marke von Anfang an zu architektieren ist also der Unterschied zwischen einer Datenänderung und einer mehrjährigen Neuschreibung.

6. **Wie werden wir Legacy- und anbietergebaute Anwendungen auf das System migrieren, und wie wird das Designsystem-Team finanziert, damit es den nächsten Budgetzyklus überlebt?** Ein Designsystem liefert seine Rendite nur, wenn echte Produkte es übernehmen, doch die schwersten Anwendungen zu konvertieren sind die alten und ausgelagerten, die es am meisten brauchen, und das Team, das das System pflegt, ist oft die erste Kürzung, wenn Budgets sich straffen. Für eine große Organisation müssen Sie zwischen einer Big-Bang-Migration und einer schrittweisen wählen, und wie Sie Anbieterinnen dazu bringen, auf Ihren Komponenten zu bauen statt um sie herum. Bringen Sie ein Inventar der Anwendungen mit ihrer aktuellen Paritätsbewertung, eine Schätzung des Migrationsaufwands pro Anwendung, und die vertraglichen Hebel, die Sie über Anbieterinnen haben. In Unternehmens- und Behördenumgebungen schreiben Sie Designsystem-Konformität in Beschaffungsbedingungen, damit neue Anbieterarbeit standardmäßig auf dem System landet, und finanzieren Sie das pflegende Team als dauerhafte geteilte Infrastruktur, denn ein System, das seine Verwalterinnen in einer Reorganisation verliert, driftet binnen eines Jahres zurück in Fragmentierung.

## Branchenperspektive

**Startup.** Mit zwei oder drei Ingenieurinnen und keiner Landebahn zu verschenken, bauen Sie kein verwaltetes System. Verbringen Sie ein oder zwei Tage damit, eine kleine Menge semantischer Tokens für Farbe, Abstand, und Type zu definieren, plus ein Dutzend geteilte Komponenten, alle in einer Datei, auf die das ganze Team verweist. Stützen Sie sich auf eine Fertig-Primitivbibliothek für die schweren Teile, und halten Sie nichts fest codiert, damit Ihr erster echter Rebrand eine Token-Änderung ist statt eine Neuschreibung.

**Kleinunternehmen.** Ohne dedizierte Designerin und mit engem Budget, kaufen Sie statt zu bauen: übernehmen Sie eine bewährte Komponentenbibliothek oder ein UI-Kit und themen Sie es leicht zu Ihrer Marke. Ihr Ziel ist ein konsistentes, zugängliches Produkt ohne ein Designsystem-Team zu besetzen, bevorzugen Sie also ein System, das Barrierefreiheit und Responsivität im Lieferumfang ausliefert. Widerstehen Sie dem Drang, es abzuspalten, denn eine angepasste Kopie, die Sie nicht pflegen können, wird zur Haftung, sobald das Upstream-Projekt weiterzieht.

**Großunternehmen.** Das Problem ist Kohärenz über viele Teams und langlebige Produkte, behandeln Sie das Designsystem also als verwaltete geteilte Infrastruktur mit einem dedizierten Team, Versionierung, und einer Roadmap. Verfolgen Sie Design-Code-Parität als echte Kennzahl, verdrahten Sie visuelles Regressionstesten in CI, und architektieren Sie die Token-Schicht von Anfang an für mehrere Marken und Themes. Budgetieren Sie die Governance- und Migrationskosten explizit, und verwalten Sie Übernahme als Portfolio, statt anzunehmen, dass Teams von selbst auf das System driften werden.

**Behörde.** Beschaffungsregeln, Transparenz, und öffentliche Rechenschaftspflicht formen jede Wahl. Barrierefreiheitskonformität zu Standards wie WCAG, Section 508, und EN 301 549 ist eine gesetzliche Anforderung, keine Präferenz, eine Komponentenbibliothek mit dokumentierter Konformität wird also zu einem Compliance-Vermögenswert. Bevorzugen oder erweitern Sie ein geteiltes öffentliches Designsystem, damit Bürgerinnen dieselben Muster über Dienste hinweg treffen, schreiben Sie Designsystem-Nutzung in Anbieterverträge, und veröffentlichen Sie Ihre Komponenten und Anleitung offen, damit Behörden und ihre Lieferantinnen sie übernehmen und daran gemessen werden können.

## Beispiele

**Startup.** Ein zweiköpfiges Ingenieursstartup baute Buttons und Formularfelder auf jedem neuen Bildschirm leicht unterschiedlich neu, und das Produkt begann zusammengeflickt auszusehen. Statt eines schwergewichtigen Systems verbrachten sie zwei Tage damit, eine kleine Menge semantischer Design-Tokens für Farbe, Abstand, und Type zu definieren, plus etwa ein Dutzend geteilte Komponenten, alle in einer Datei, auf die das ganze Team verwies. Weil nichts fest codiert war, als ihre erste designbewusste Einstellung eine sauberere Palette vorschlug, war der Refresh eine Token-Änderung, die binnen eines Nachmittags über die App landete statt einer Bildschirm-für-Bildschirm-Plackerei.

**Großunternehmen.** Eine globale Softwarefirma mit Dutzenden Produktteams baute ein tokenisiertes Designsystem mit einer geteilten codierten Komponentenbibliothek. Semantische Tokens erlaubten ihnen, einen vollständigen Markenrefresh über alle Produkte in Wochen auszuliefern, statt einer mehrjährigen Pro-Team-Plackerei, weil die Änderung eine neue Token-Menge war statt Tausende fest codierter Farbbearbeitungen. Design-Code-Parität, als Dashboard-Kennzahl verfolgt, stieg, während Teams maßgeschneiderte Komponenten ersetzten, was duplizierte UI-Pflege reduzierte.

**Behörde.** Eine nationale Regierung schuf ein gemeinsames Designsystem für öffentliche Dienste (geteilte Komponenten, Muster, und Barrierefreiheit eingebaut), vorgeschrieben über Behörden hinweg. Eine Bürgerin, die zwischen einem Steuerdienst, einem Gesundheitsdienst, und einem Lizenzierungsdienst wechselt, trifft dieselbe Kopfzeile, Formularsteuerelemente, und Fehlermuster, was Vertrauen aufbaut und die Lernkurve verkürzt. Behörden und ihre Anbieterinnen liefern schneller und zugänglicher aus, weil die schweren Probleme zentral gelöst sind, und die Regierung kann Leitlinien oder Barrierefreiheitsfixes einmal aktualisieren und überall fortpflanzen lassen.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Der ROI eines Designsystems kommt vom Entfernen von Duplikation und Beschleunigen der Lieferung. Statt dass jedes Team dieselben Komponenten gestaltet und baut, komponieren sie aus einer geteilten Bibliothek, was Lieferung messbar beschleunigt und Designerinnen und Ingenieurinnen für produktspezifische Arbeit freimacht. Barrierefreiheit und Responsivität, einmal in Komponenten gelöst, sparen Ihnen die Pro-Projekt-Behebungskosten. Rebrands und Theming, die einst Jahre dauerten, dauern jetzt Wochen.

Bei Gesamtbetriebskosten sind die Übernahmekosten ein dediziertes Team, Werkzeug, und der Aufwand für existierende Produkte, auf das System zu migrieren. Die Kosten der Nicht-Übernahme werden kontinuierlich bezahlt: duplizierter Bau und Pflege über Teams hinweg, inkonsistente und unzugängliche UIs, die Support- und rechtliches Risiko schaffen, und langsame, teure Rebrands. Weil sich die Duplikation über die Budgets vieler Teams verteilt, ist sie leicht zu übersehen: ein Designsystem macht diese versteckte Kosten sichtbar und erfasst sie an einem Ort.

Um den Fall gegenüber der Führung zu machen, quantifizieren Sie die duplizierte Komponentenarbeit über Teams, den Time-to-Market-Gewinn aus Komposition, und die Kosten und Dauer Ihres letzten Rebrands versus was ein tokenisiertes System erlauben würde. Rahmen Sie das System als geteilte Infrastruktur mit einer messbaren Übernahmekennzahl (Paritätsprozentsatz), damit ihr Wert über Zeit verfolgt statt nur behauptet werden kann.

## Anti-Muster und Fallstricke

- **Designsystem als Stickerbogen**: eine statische Designdatei ohne codierte Komponenten, sodass Ingenieurinnen sowieso alles neu bauen.
- **Fest codierte Werte überall**: Farben und Abstände über Code verstreut, Theming und Rebrands unmöglich machend.
- **Keine Governance**: das System fragmentiert, während Teams divergente Varianten hinzufügen; Konsistenz erodiert.
- **Governance ohne Beitrag**: das zentrale Team wird ein Engpass, und Teams routen darum herum.
- **Parität ignorieren**: die codierte UI driftet von der Designabsicht ab, und niemand misst die Lücke.
- **Überabstraktion**: so viele Tokens und Schichten, dass niemand das richtige finden oder nutzen kann.
- **Markenlogik in Komponenten gebacken**: macht Multi-Marke und Theming zu einer Code-Neuschreibung statt einer Konfigurationsänderung.
- **Brechende Änderungen ohne Migrationsunterstützung**: konsumierende Teams stocken oder spalten das System ab.

## Reifegradmodell

**Stufe 1: Beginnen.** Jedes Team baut seine eigene UI ad hoc und reaktiv. Keine geteilten Komponenten, inkonsistentes Aussehen und Verhalten, Farben und Abstände pro Bildschirm fest codiert. Jeder Rebrand ist eine manuelle Bildschirm-für-Bildschirm-Plackerei.

**Stufe 2: Entwickeln.** Ein geteilter Styleguide oder eine Komponentenbibliothek existiert, ist aber partiell, optional, und oft zwischen Design und Code außer Synchronisation. Manche Teams nutzen sie, andere nicht, und grundlegende Praktiken variieren stark von Team zu Team.

**Stufe 3: Standardisieren.** Ein tokenisiertes Designsystem mit einer gepflegten codierten Bibliothek, Dokumentation, und Governance ist dokumentiert und über die ganze Organisation durchgesetzt. Komponenten konsumieren semantische Tokens, Theming wird unterstützt, und Barrierefreiheit und Responsivität sind eingebaut statt pro Bildschirm angeschraubt.

**Stufe 4: Steuern.** Das System wird mit Daten gegen Baselines gemessen und gesteuert. Design-Code-Parität wird als explizite Kennzahl mit Zielen pro Produkt verfolgt, visuelles Regressionstesten läuft in CI, um Drift zu erwischen, und Barrierefreiheitskonformität wird gegen Standards gemessen statt angenommen. Übernahme-Dashboards zeigen Komponentenabdeckung nach Team, und die Kosten und Dauer von Rebrands werden aufgezeichnet, damit Verbesserung über Zeit sichtbar ist.

**Stufe 5: Orchestrieren.** Das Designsystem ist ein kontinuierlich verbessertes Produkt, integriert über die Organisation und adaptiv an Wandel. Es hat Versionierung, eine Roadmap, und ein funktionierendes Beitragsmodell, damit es sich mit echten Bedürfnissen entwickelt. Rebrands und neue Themes sind Routine-Token-Änderungen, Multi-Marken- und Multi-Mandanten-Theming ist normal, und das Team zieht Muster auf Beleg aus Nutzungsdaten zurück, rahmt sie neu, und befördert sie, Designwerkzeug und Lieferpipelines aus einer einzigen Quelle der Wahrheit speisend.

## Diskussionsideen

- Wie balancieren Sie zentrale Governance gegen Teamautonomie, ohne entweder zu fragmentieren oder zum Engpass zu werden?
- Was ist die richtige Kennzahl für "Design-Code-Parität", und wie halten Sie sie ehrlich?
- Wann sollte einem Team erlaubt sein, eine Einmalkomponente zu bauen statt das System zu nutzen?
- Wie finanzieren und besetzen Sie ein Designsystem, damit es Budgetzyklen und Reorganisationen überlebt?
- Wie viel Theming-Flexibilität ist die zusätzlichen Abstraktionskosten wert?
- Wie migrieren Sie Legacy- und anbietergebaute Anwendungen auf ein geteiltes System?

## Wichtigste Erkenntnisse

- Ein Designsystem verwandelt einmalige Designentscheidungen in wiederverwendbares, verwaltetes Kapital.
- Strukturieren Sie es in Schichten (Tokens, Komponenten, Muster), wobei Komponenten semantische Tokens konsumieren.
- Bauen Sie Barrierefreiheit und Responsivität in Komponenten ein, damit jedes Team sie erbt.
- Behandeln Sie Design-Code-Parität als messbare Gesundheitskennzahl, keine Annahme.
- Tokenisierung macht Rebrands und Multi-Marken-Theming zu einer Datenänderung, keiner Neuschreibung.
- Verwalten Sie das System als Produkt mit einer Roadmap, Versionierung, und einem Beitragsmodell.
- Im Unternehmens- und Behördenmaßstab ist ein geteiltes System die verfügbare UI-Investition mit dem höchsten Hebel.

## Referenzen und weiterführende Literatur

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, Schriften über Design-Tokens und Designsystem-Governance
- W3C Design Tokens Community Group, Formatspezifikation
- Behörden-Designsysteme (z. B. UK Government Design System, U.S. Web Design System) als Referenzimplementierungen
