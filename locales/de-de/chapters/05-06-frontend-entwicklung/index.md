# 5.6 Frontend-Entwicklung

## Überblick und Motivation

Frontend-Entwicklung ist die Disziplin, die kundenzugewandte Schicht von Software zu bauen: den Code, der im Browser oder auf dem Gerät läuft und Designs, Inhalt, und Daten in eine funktionierende Oberfläche verwandelt. Sie umfasst Framework- und Architekturwahlen, Rendering-Strategie, Zustandsverwaltung, Performance, und Resilienz über die enorme Diversität von Browsern, Geräten, und Netzwerkbedingungen in der echten Welt. Das Frontend ist, wo alle vorgelagerte Arbeit (UX, Design, Inhalt, Barrierefreiheit, Internationalisierung) entweder die Nutzerin erfolgreich erreicht oder zerfällt.

Für große Teams ist das Frontend einzigartig herausfordernd, weil es einer Umgebung ausgesetzt ist, die die Organisation nicht kontrolliert. Browser, Geräte, Verbindungen, und Einstellungen der Nutzerinnen variieren wild, und die Plattform (das Web) entwickelt sich kontinuierlich weiter. Im Maßstab verdichten sich architektonische Entscheidungen. Ein heute gewähltes Framework schränkt Einstellung, Performance, und Wartbarkeit für Jahre ein, und Tausende kleine Entscheidungen über Bundle-Größe und Rendering summieren sich zur Erfahrung, die Nutzerinnen tatsächlich bekommen. Geteilte Standards, Komponentenbibliotheken, Performance-Budgets, und architektonische Muster sind, was viele unabhängige Teams davon abhält, ein langsames, inkonsistentes, brüchiges Ganzes zu produzieren.

Unternehmens- und Behördenrelevanz ist akut. Unternehmen pflegen langlebige Anwendungen, wo Framework-Langlebigkeit und Wartbarkeit mehr zählen als Neuheit, und wo viele Teams interoperieren müssen. Regierungen bedienen die gesamte Öffentlichkeit, einschließlich Menschen auf alten Geräten, langsamen oder getakteten Verbindungen, und assistiven Technologien. Das macht Performance, [progressive Verbesserung](https://en.wikipedia.org/wiki/Progressive_enhancement), und Resilienz nicht zu optionalem Feinschliff, sondern zum Unterschied zwischen einem Dienst, der für alle funktioniert, und einem, der die am wenigsten Begünstigten ausschließt. Ein Behördendienst, der nur auf dem neuesten Handy mit schneller Verbindung funktioniert, versagt an seinem Mandat.

## Kernprinzipien

- Das Frontend läuft in einer Umgebung, die Sie nicht kontrollieren; gestalten Sie für Variabilität und Fehlschlag.
- Wählen Sie langweilige, dauerhafte Technologie für langlebige Systeme; optimieren Sie für Wartbarkeit und Einstellung.
- Performance ist ein Feature und, für viele Nutzerinnen, eine Voraussetzung für Zugang.
- Progressive Verbesserung: liefern Sie zuerst eine funktionierende Kernerfahrung, schichten Sie dann Verbesserungen.
- Senden Sie weniger Code; der schnellste und verlässlichste Code ist der Code, den Sie nicht ausliefern.
- Passen Sie Rendering-Strategie an Inhaltstyp und Nutzerbedürfnis an, nicht an Mode.
- Resilienz: die Oberfläche sollte anmutig degradieren, nicht brechen, wenn Dinge schiefgehen.
- Standards und Plattform-Features überleben Frameworks; stützen Sie sich auf die Plattform.

## Empfehlungen

### Frameworks für Langlebigkeit und Passung wählen, nicht Hype

Wählen Sie Frontend-Technologie basierend auf dem Problem, dem Team, dem Wartungshorizont, und dem Einstellungsmarkt, nicht darauf, was gerade trendet. Für langlebige Unternehmens- und Behördensysteme bevorzugen Sie ausgereifte, gut unterstützte Technologien mit großen Talentpools, stabilen Veröffentlichungspraktiken, und klaren Upgrade-Pfaden. Wägen Sie die Gesamtkosten von Framework-Wechsel ab: Neuschreibungen sind teuer und riskant. Bevorzugen Sie Ansätze, die sich auf [Web-Standards](https://en.wikipedia.org/wiki/Web_standards) stützen, damit Ihre Investition Framework-Wechsel überlebt, und isolieren Sie frameworkspezifischen Code hinter Grenzen, damit die Anwendung nicht Geisel des Lebenszyklus einer Bibliothek ist.

### Rendering-Strategie an den Bedarf anpassen

Die Haupt-Rendering-Strategien passen jeweils zu unterschiedlichem Inhalt. Server-seitiges Rendering (SSR) produziert schnellen ersten Anstrich und gute SEO ([Suchmaschinenoptimierung](https://en.wikipedia.org/wiki/Search_engine_optimization)) und funktioniert ohne Client-JavaScript, passend für inhaltsschwere und öffentlich zugewandte Seiten. [Statische Seitengenerierung](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) rendert zur Build-Zeit vor für maximale Geschwindigkeit und Cachebarkeit, ideal für Inhalt, der sich selten ändert. Client-seitiges Rendering (CSR) passt zu hochinteraktiven app-artigen Erfahrungen hinter Authentifizierung. Streaming und progressive Hydration senden und aktivieren die Seite inkrementell, damit Nutzerinnen Inhalt früher sehen und nutzen. Viele große Systeme mischen diese pro Route statt eines global zu wählen. Verwalten Sie Zustand absichtlich: halten Sie Serverzustand, URL-Zustand, und lokalen UI-Zustand getrennt, und vermeiden Sie, alles in einen schweren globalen Speicher zu überzentralisieren.

### Performance als budgetierte, gemessene Disziplin behandeln

Übernehmen Sie Performance-Budgets (explizite Grenzen für Bundle-Größe, Anzahl der Anfragen, und Schlüsselkennzahlen) und setzen Sie sie in CI durch, damit Regressionen den Build scheitern lassen. Verfolgen Sie die Core Web Vitals (Laden, Interaktivität, und visuelle Stabilität) mit Real-User-Monitoring von echten Geräten und Netzwerken, nicht nur Labortests auf schnellen Maschinen. Reduzieren Sie JavaScript aggressiv: teilen Sie Code auf und [lazy-loaden](https://en.wikipedia.org/wiki/Lazy_loading) Sie, damit Nutzerinnen nur herunterladen, was eine gegebene Ansicht braucht, verschieben Sie nicht-kritische Arbeit, und bevorzugen Sie Plattformfähigkeiten über schwere Bibliotheken. Optimieren Sie Bilder und Schriftarten, cachen Sie effektiv, und messen Sie auf repräsentativen Low-End-Geräten und langsamen Verbindungen.

### Mit progressiver Verbesserung und Resilienz bauen

Beginnen Sie mit einer Baseline, die mit semantischem HTML und minimalem oder keinem JavaScript funktioniert, verbessern Sie dann für fähige Clients. Das stellt sicher, dass die Kernaufgabe möglich bleibt, wenn Skripte nicht laden, ein Gerät alt ist, oder ein Netzwerk wackelig ist, eine häufige Realität statt eines Randfalls. Handhaben Sie Fehler anmutig: zeigen Sie nützliche Zustände für Laden, Leer, Fehler, und Offline-Bedingungen statt leerer Bildschirme oder unendlicher Spinner. Für Dienste, auf die sich Menschen verlassen, erwägen Sie Offline-First-Techniken, damit die App durch intermittierende Konnektivität nutzbar bleibt, synchronisierend, wenn die Verbindung zurückkehrt.

### Cross-Browser-, Cross-Geräte-, und assistive Kompatibilität sicherstellen

Testen Sie über die Browser, Geräte, und assistiven Technologien, die Ihre Nutzerinnen tatsächlich haben, informiert durch echte Analytics statt die eigenen Maschinen des Teams. Nutzen Sie progressive Verbesserung und Feature-Erkennung statt anzunehmen, dass die neuesten Plattform-Features überall verfügbar sind. Bauen Sie [responsiv](https://en.wikipedia.org/wiki/Responsive_web_design) (siehe das Designsystem-Kapitel), damit eine Codebasis Handys bis Desktops bedient. Integrieren Sie Barrierefreiheit und Internationalisierung von Anfang an in die Frontend-Architektur, nicht als spätere Durchgänge.

### Das Frontend als geteilte Infrastruktur verwalten

Stellen Sie geteilte Komponentenbibliotheken, Linting, Formatierung, und Build-Werkzeug bereit, damit Teams konsistent und produktiv sind. Etablieren Sie architektonische Leitlinien (wie Anwendungen strukturiert, Zustand verwaltet, und Bundles aufgeteilt werden) und in CI durchgesetzte Performance-Budgets. Für sehr große Frontends erwägen Sie modulare oder Micro-Frontend-Architekturen, die Teams erlauben, unabhängig zu deployen, aber wägen Sie die zusätzliche Komplexität und Performance-Kosten sorgfältig ab, denn sie sind nicht kostenlos.

## Abwägungen: Vor- und Nachteile

| Entscheidung | Vorteile | Nachteile |
|---|---|---|
| Populäres ausgereiftes Framework | Großer Talentpool, stabil, unterstützt | Kann Legacy-Gewicht tragen; langsamer, die neuesten Features zu übernehmen |
| Neuestes Framework | Moderne Features, Performance-Gewinne | Wechselrisiko, kleiner Talentpool, unsichere Langlebigkeit |
| SSR/SSG | Schneller erster Anstrich, SEO, funktioniert ohne JS | Server- oder Build-Komplexität, Caching-Herausforderungen |
| CSR (SPA) | Reiche Interaktivität, app-artiges Gefühl | Langsames erstes Laden, JS-abhängig, SEO- und Resilienz-Kosten |
| Schweres Client-JavaScript | Reiche Features | Schlechte Performance auf Low-End-Geräten, brüchig |
| Progressive Verbesserung | Resilient, inklusiv, funktioniert überall | Mehr Designaufwand, eine funktionierende Baseline zu definieren |
| Micro-Frontends | Unabhängige Team-Deploys, Skalierung | Komplexität, duplizierte Abhängigkeiten, Performance-Overhead |

Die wiederkehrende Abwägung ist Reichhaltigkeit und Entwicklerinnenkomfort gegen Reichweite, Performance, und Resilienz. Schwere client-seitige Ansätze sind angenehm zu bauen und auf schnellen Maschinen zu demonstrieren, aber sie schließen Nutzerinnen auf schwachen Geräten und Netzwerken aus. Für Unternehmens- und besonders Behördenpublikum neigen Sie die Balance zu Performance, progressiver Verbesserung, und Dauerhaftigkeit, denn die Kosten, Nutzerinnen auszuschließen, sind hoch und oft nicht verhandelbar.

## Fragen zur Diskussion mit Ihrem Team

1. **Wie isolieren wir frameworkspezifischen Code, damit die Anwendung nicht Geisel des Lebenszyklus einer Bibliothek ist?** Für langlebige Unternehmens- und Behördensysteme ist Framework-Wechsel die größte vermeidbare Ausgabe: eine Neuschreibung ist teuer und riskant, und die heute trendende Bibliothek schränkt Einstellung und Wartung für Jahre ein. Sich auf Web-Standards zu stützen und frameworkspezifischen Code hinter klaren Grenzen zu platzieren bedeutet, dass Ihre Geschäftslogik und Ihr Inhalt den nächsten Framework-Wechsel überleben. Entscheiden Sie, wo diese Nähte sind und ob eine neue Ingenieurin Plattform-Code von Framework-Code unterscheiden könnte. Bringen Sie eine Schätzung, was Ihre letzte Framework-Migration kostete, oder was die drohende kosten wird. Wenn Ihre Kernlogik an die APIs einer Bibliothek geschweißt ist, bepreisen Sie diese Kopplung, bevor Sie die Framework-Wahl verteidigen.

2. **Passen wir die Rendering-Strategie pro Route an, oder erzwingen wir eine Strategie für das ganze Produkt?** Server-seitiges Rendering gibt schnellen ersten Anstrich und funktioniert ohne Client-JavaScript für öffentlichen Inhalt, statische Generierung maximiert Geschwindigkeit für selten sich ändernde Seiten, und Client-Rendering passt zu interaktiven app-artigen Oberflächen hinter Login. Eines global zu erzwingen verlangsamt entweder öffentliche Seiten mit schwerem JavaScript oder überentwickelt eine einfache Inhaltsseite. Das ist eine Reichweitenfrage für Behörden, wo ein Dienst, der nur funktioniert, nachdem ein großes Bundle lädt, Nutzerinnen auf alten Geräten und langsamen Verbindungen ausschließt. Bringen Sie Ihre Schlüsselrouten und beschriften Sie jede mit der Strategie, die sie heute tatsächlich nutzt. Wenn eine öffentlich zugewandte Seite JavaScript braucht, um ihren Inhalt zu zeigen, entscheiden Sie, ob das eine absichtliche Wahl oder ein Unfall ist.

3. **Wie diszipliniert ist unsere Zustandsverwaltung, und überzentralisieren wir alles in einen schweren globalen Speicher?** Serverzustand, URL-Zustand, und lokalen UI-Zustand getrennt zu halten verhindert die Kopplung und Neu-Render-Stürme, die große Frontends langsam und brüchig machen, doch der verlockende Standard ist, alles in einen globalen Speicher zu kippen. Das verdichtet sich im Maßstab, wo viele Teams, die einen geteilten Speicher berühren, versteckte Abhängigkeiten und unvorhersehbare Performance schaffen. Einigen Sie sich, wohin jede Art Zustand gehört und was nicht in den globalen Speicher gehört. Bringen Sie eine Komponente, die mehr neu rendert, als sie sollte, und verfolgen Sie warum. Wenn die Antwort ein aufgeblähter zentraler Speicher ist, entscheiden Sie die Grenzen, bevor die Kopplung sich verhärtet.

4. **Was sind unsere Performance-Budgets, sind sie in CI build-scheiternd, und werden sie auf den Geräten gemessen, die unsere Nutzerinnen tatsächlich haben?** Ein Budget, das niemand durchsetzt, ist ein Wunsch, und ein Budget, nur auf den schnellen Laptops des Teams gemessen, beschreibt eine Nutzerin, die nicht existiert. Für eine große Organisation sind Budgets der einzige Mechanismus, der Bundle-Größe und Core Web Vitals im Zaum hält, während Dutzende Teams Features zu einer geteilten Oberfläche hinzufügen, denn keine einzelne Prüferin kann jede Regression mit bloßem Auge erwischen. Der konkurrierende Druck ist Liefergeschwindigkeit: ein harter Build-Fehlschlag über ein paar Kilobyte fühlt sich behindernd an, bis Sie die Abbrüche bepreisen, die er verhindert. Bringen Sie Ihre aktuellen Budgets, die Real-User-Monitoring-Daten von Low-End-Geräten und langsamen Verbindungen, und die Liste der Veröffentlichungen, wo eine Regression durchrutschte. In Behörden, wo das Mandat ist, die gesamte Öffentlichkeit zu bedienen, einschließlich Menschen auf alten Handys und getakteten Daten, binden Sie das Budget an das langsamste Zehntel Ihrer Nutzerinnen statt den Median, und machen Sie das CI-Tor nicht verhandelbar.

5. **Welche unserer Dienste müssen ohne Client-JavaScript weiter funktionieren, und haben wir diesen Pfad tatsächlich getestet?** Progressive Verbesserung ist leicht zu behaupten und leicht still zu brechen, denn der verbesserte Pfad ist der, den Entwicklerinnen täglich nutzen, während die Baseline ungetestet verrottet. Das absichtlich zu entscheiden zählt im Maßstab, denn viele Teams, die zu einer Plattform ausliefern, werden jeweils annehmen, dass Skripte immer laden, sofern ein geteilter Standard nichts anderes sagt, und eine einzelne harte Abhängigkeit kann die Kernaufgabe für jeden brechen, dessen Bundle scheitert. Die Abwägung ist echt: eine funktionierende Ohne-JavaScript-Baseline kostet Designaufwand und schränkt ein, wie Sie Interaktivität bauen. Bringen Sie Ihre kritischen Nutzerjourneys, einen Test, der jede mit deaktivierten oder gescheiterten Skripten lädt, und Beleg, wie oft Skripte im Feld tatsächlich nicht laden. Für einen öffentlichen Dienst ist ein Leistungs- oder Steuerformular, das zusammenbricht, wenn ein Skript ein Timeout hat, keine degradierte Erfahrung, es ist eine Bürgerin, die eine gesetzliche Pflicht nicht erfüllen kann, behandeln Sie die Baseline also als Compliance-Anforderung, keine Nettigkeit.

6. **Wann zahlen sich Micro-Frontends tatsächlich für ihre Komplexität aus, und wer entscheidet, bevor ein Team zu einem greift?** Unabhängige Team-Deploys sind attraktiv, aber Micro-Frontends tragen verteilte-System-Komplexität, duplizierte Abhängigkeiten, und eine Performance-Steuer, die Nutzerinnen in langsameren Ladezeiten bezahlen. Ohne einen geteilten Entscheidungspunkt übernehmen ambitionierte Teams sie aus organisatorischer Bequemlichkeit lange bevor der Maßstab die Kosten rechtfertigt, und das ganze Produkt erbt den Overhead. Die konkurrierende Überlegung ist Autonomie: Teams, die auf einer geteilten Codebasis ausliefern, können sich gegenseitig blockieren, und in echtem Maßstab ist diese Kopplung ihr eigenes teures Problem. Bringen Sie die Anzahl der Teams, die die Oberfläche berühren, die Deploy-Konkurrenz, die Sie heute tatsächlich erleben, und eine gemessene Schätzung der Payload-Duplikation, die eine Aufteilung einführen würde. Für Unternehmens- und Behördenplattformen, wo Architekturentscheidungen viele Teams für Jahre binden und Prüfung und Übergabe überleben müssen, fordern Sie eine explizite, dokumentierte Schwelle und eine Besitzerin, die den Schritt genehmigt, statt jedes Team isoliert entscheiden zu lassen.

## Branchenperspektive

**Startup.** Geschwindigkeit und Reichweite zählen beide, wenn jede Anmeldung zählt, widerstehen Sie also der schweren Single-Page-App für öffentliche Seiten. Server-rendern Sie Ihren Marketing- und Anmeldeablauf, damit sie schnell auf den Mittelklasse-Handys und lückenhaften Daten laden, die Ihre frühen Kundinnen nutzen, und reservieren Sie client-seitige Interaktivität für die App hinter Login. Setzen Sie ein einfaches Bundle-Größe-Budget in CI, damit eine nachlässige Abhängigkeit die Seite nicht still aufblähen kann, und stützen Sie sich auf Web-Standards, um eine winzige Codebasis wartbar zu halten, während Sie einstellen.

**Kleinunternehmen.** Ohne dedizierte Frontend-Spezialistin und mit engem Budget, bevorzugen Sie ein gut unterstütztes Mainstream-Framework oder einen gehosteten Site-Builder über irgendetwas Maßgeschneidertes, damit Sie aus einem großen Talentpool einstellen und Wartung kaufen statt sie zu besetzen. Rahmen Sie die Wahl als Dauerhaftigkeit: die günstigste Option ist die, die Sie nicht in zwei Jahren neu schreiben müssen. Bestehen Sie auf schnellen, mobilfreundlichen Seiten und barrierefreiem Markup von Haus aus, denn ein langsamer oder kaputter Checkout kostet Sie Kundinnen, die Sie sich nicht leisten können zu verlieren.

**Großunternehmen.** Das Problem ist Konsistenz über viele Teams: eine geteilte Komponentenbibliothek, vereinbarte architektonische Muster, Linting und Build-Werkzeug, und in CI durchgesetzte Performance-Budgets, damit kein Team das Ganze still regressieren kann. Wählen Sie Frameworks für Langlebigkeit und Einstellung statt Neuheit, isolieren Sie frameworkspezifischen Code hinter Grenzen, um die nächste Migration zu überleben, und passen Sie Rendering-Strategie pro Oberfläche an. Verwalten Sie das Frontend als geteilte Infrastruktur mit Real-User-Monitoring, Governance, und einer prüfbaren Aufzeichnung, warum jede architektonische Wahl getroffen wurde.

**Behörde.** Sie bedienen die gesamte Öffentlichkeit, einschließlich Menschen auf alten Geräten, langsamen oder getakteten Verbindungen, und assistiven Technologien, progressive Verbesserung und Performance sind also Pflichten, kein Feinschliff. Machen Sie eine funktionierende Ohne-JavaScript-Baseline zu einer harten Regel für bürgerzugewandte Dienste, budgetieren Sie Seiten für die langsamsten Nutzerinnen statt den Median, und halten Sie die Kernaufgabe abschließbar, wenn ein Skript scheitert. Beschaffung und Transparenz gelten: bevorzugen Sie dauerhafte, standardgestützte Technologie, die Ein-Anbieter-Lock-in vermeidet, dokumentieren Sie die Barrierefreiheits- und Performance-Anforderungen in Verträgen, und seien Sie in der Lage zu zeigen, dass der Dienst für die am wenigsten begünstigte Nutzerin funktioniert, nicht nur das Demo-Gerät.

## Beispiele

**Startup.** Ein Seed-Stage-Startup war versucht, seine Marketing-Seite und Anmeldeablauf als schwere Single-Page-App zu bauen, aber ihre Zielkundinnen waren Einkäuferinnen, oft auf Mittelklasse-Handys über lückenhafte mobile Daten. Die zwei Gründerinnen server-renderten stattdessen die öffentlichen Seiten, damit sie schnell luden und funktionierten, bevor irgendein JavaScript lief, und reservierten client-seitige Interaktivität für die App hinter Login. Sie setzten ein einfaches Bundle-Größe-Budget in CI, damit eine nachlässige Abhängigkeit die Seite nicht still aufblähen konnte. Das schlanke, schnelle erste Laden verbesserte Anmeldungen messbar, und sich auf Web-Standards zu stützen hielt ihre kleine Codebasis leicht wartbar, während sie einstellten.

**Großunternehmen.** Eine Finanzdienstleistungsfirma modernisierte eine ausufernde Menge interner und kundenzugewandter Anwendungen durch Standardisierung auf ein ausgereiftes Framework, eine geteilte Komponentenbibliothek, und durchgesetzte Performance-Budgets in CI. Rendering-Strategie wurde pro Oberfläche gewählt: server-gerenderte, cachebare Seiten für öffentliches Marketing und Inhalt, und eine client-gerenderte Anwendung hinter Login für interaktive Dashboards. Bundle-Budgets und Real-User-Monitoring erwischten Regressionen vor der Veröffentlichung, Ladezeiten über die vielen Teams der Firma hinweg schnell haltend und das Framework-Wechsel-Risiko reduzierend, das zuvor kostspielige Neuschreibungen erzwungen hatte.

**Behörde.** Ein nationales Digitaldienst-Team baute bürgerzugewandte Dienste mit progressiver Verbesserung als harter Regel: jeder Dienst funktioniert zuerst mit semantischem HTML und Server-Rendering, und JavaScript verbessert nur. Das garantiert, dass der Dienst auf alten Handys, langsamen ländlichen Verbindungen, und assistiven Technologien funktioniert, Populationen, die eine Regierung nicht ausschließen kann. Performance-Budgets halten Seiten leicht und schnell auf Low-End-Geräten, und anmutige Degradation bedeutet, dass ein gescheitertes Skript nie jemanden daran hindert, einen Leistungsantrag abzuschließen. Das Ergebnis ist ein Dienst, der schnell, resilient, barrierefrei, und für die gesamte Öffentlichkeit nutzbar ist.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Frontend-Engineering-Entscheidungen treiben Umsatz, Reichweite, und Kosten. Performance ist direkt an Konversion, Engagement, und Aufgabenabschluss gebunden. Schnellere Erfahrungen übertreffen langsamere messbar, und für Nutzerinnen auf schwachen Geräten ist Performance die Linie zwischen Nutzung des Dienstes und Abbruch. Progressive Verbesserung und Cross-Geräte-Unterstützung erweitern das adressierbare Publikum, was für Behörden ein Mandat ist und für Unternehmen Marktanteil. Solide Framework- und Architekturentscheidungen reduzieren die Häufigkeit und Kosten von Neuschreibungen, die größte vermeidbare Ausgabe in Frontend-Engineering.

Bei Gesamtbetriebskosten sind Übernahmekosten die Disziplin von Performance-Budgets und Testen, der Aufwand progressiver Verbesserung, und die Investition in geteiltes Werkzeug und Komponentenbibliotheken. Die Kosten der Nicht-Übernahme werden in langsamen Erfahrungen bezahlt, die Nutzerinnen und Umsatz verlieren, Ausschluss von Low-End- und assistive-Technologie-Nutzerinnen (mit rechtlicher Exposition in Behörden), brüchigen Anwendungen, die im Feld brechen, und teurem Framework-Wechsel und Neuschreibungen, getrieben von Trend-Jagd. Frontend-Probleme zeigen sich als diffuser Abbruch und Support-Last statt eines einzelnen Postens, sie sind also leicht zu unterinvestieren.

Um den Fall gegenüber der Führung zu machen, verbinden Sie Core Web Vitals und Ladezeiten mit Konversions- und Abschluss-Funnels, quantifizieren Sie die durch schwere client-seitige Ansätze ausgeschlossenen Nutzerinnen, und bepreisen Sie die Kosten vergangener oder drohender Neuschreibungen gegen die Stabilität einer dauerhaften, standardgestützten Architektur. Rahmen Sie Performance-Budgets und progressive Verbesserung als Risikoreduktion und Reichweitenerweiterung.

## Anti-Muster und Fallstricke

- **Framework-Jagd**: auf der neuesten Bibliothek neu schreiben, Wechsel ohne Nutzerinnen-Nutzen erleidend.
- **Nur-JavaScript-Erfahrungen**: nichts funktioniert, bis ein großes Bundle lädt und läuft, viele Nutzerinnen ausschließend.
- **Nur auf schnellen Geräten testen**: die Flaggschiff-Laptops des Teams verstecken die echte Nutzererfahrung.
- **Bundle-Größe ignorieren**: unbegrenztes Abhängigkeitswachstum, bis Seiten überall langsam sind.
- **Kein Performance-Budget**: Regressionen häufen sich still Veröffentlichung für Veröffentlichung.
- **Leerer-Bildschirm-Fehlschläge**: kein Lade-, Leer-, Fehler-, oder Offline-Zustand; eine gescheiterte Anfrage bricht die Seite.
- **Überzentralisierter globaler Zustand**: alles in einem Speicher, Kopplung und Neu-Render-Stürme schaffend.
- **Vorzeitige Micro-Frontends**: verteilte-System-Komplexität und duplizierte Payloads ohne den Maßstab, der sie rechtfertigt.
- **Barrierefreiheit und i18n in der Architektur vernachlässigen**: sie später zu hohen Kosten anschrauben.

## Reifegradmodell

**Stufe 1: Beginnen.** Ad-hoc-Frontend, pro Team gebaut, ohne geteilte Standards. Schwerer client-seitiger Code, keine Performance-Budgets, nur auf den eigenen Geräten des Teams getestet. Framework-Wahlen nach Präferenz oder Hype getroffen, und ein gescheitertes Skript kann Nutzerinnen auf einen leeren Bildschirm starren lassen.

**Stufe 2: Entwickeln.** Manche Teams übernehmen geteiltes Werkzeug und eine Komponentenbibliothek, aber die Praxis ist über die Organisation hinweg inkonsistent. Performance wird gelegentlich gemessen statt budgetiert oder durchgesetzt. Rendering-Strategie ist oft einheitlich unabhängig vom Inhaltstyp, und Cross-Geräte-Testen ist begrenzt und manuell.

**Stufe 3: Standardisieren.** Framework und Architektur werden absichtlich für Langlebigkeit gewählt, und die Entscheidungen sind dokumentiert und organisationsweit durchgesetzt. Rendering-Strategie wird pro Oberfläche angepasst, progressive Verbesserung und anmutige Degradation sind der Standard, und geteilte Komponentenbibliotheken, Linting, und Build-Werkzeug gelten für jedes Team. Cross-Browser, Barrierefreiheit, und Internationalisierung sind eingebaut statt angeschraubt.

**Stufe 4: Steuern.** Das Frontend wird mit Daten gemessen und gesteuert. Performance-Budgets werden in CI durchgesetzt, damit Regressionen den Build scheitern lassen, und Core Web Vitals werden mit Real-User-Monitoring von echten Low-End-Geräten und langsamen Verbindungen gegen explizite Baselines verfolgt. Bundle-Größe, Fehler- und Offline-Zustand-Abdeckung, und der Anteil der auf den langsamsten Verbindungen bedienten Nutzerinnen werden berichtet und überprüft, damit Entscheidungen auf Beleg statt Meinung ruhen.

**Stufe 5: Orchestrieren.** Performance, Resilienz, und Reichweite werden kontinuierlich verbessert und über die ganze Organisation an Geschäftsergebnisse gebunden. Das Frontend stützt sich auf Web-Standards für Dauerhaftigkeit, isoliert Framework-Abhängigkeiten, damit Migrationen günstig sind, und entwickelt Architektur adaptiv weiter, während sich Geräte, die Plattform, und Real-User-Daten verschieben. Die gesamte Öffentlichkeit und alle Geräte sind erstklassig, und Frontend-Praxis ist mit Design-, Barrierefreiheits-, und Produktplanung integriert statt als separates Anliegen behandelt.

## Diskussionsideen

- Wie entscheiden Sie, wann eine Framework-Migration ihre Kosten und ihr Risiko wert ist?
- Welche Core Web Vitals und Bundle-Budgets sollten harte build-scheiternde Schwellen sein?
- Wo ist progressive Verbesserung essentiell, und wo ist eine client-seitige App akzeptabel?
- Wie halten Sie Frontend-Architektur über viele autonome Teams hinweg konsistent?
- Wann zahlen sich Micro-Frontends tatsächlich für ihre Komplexität aus?
- Wie sollte echtes-Gerät- und langsames-Netzwerk-Testen in die Pipeline eingebaut werden?

## Wichtigste Erkenntnisse

- Das Frontend läuft in einer Umgebung, die Sie nicht kontrollieren: gestalten Sie für Variabilität und Fehlschlag.
- Wählen Sie dauerhafte, gut unterstützte Technologie für langlebige Systeme; stützen Sie sich auf Web-Standards.
- Passen Sie Rendering-Strategie (SSR, SSG, CSR, Streaming) an Inhalt und Bedarf an, oft pro Route gemischt.
- Behandeln Sie Performance als budgetierte, gemessene Disziplin, in CI mit Real-User-Daten durchgesetzt.
- Bauen Sie mit progressiver Verbesserung, damit die Kernerfahrung überall funktioniert.
- Liefern Sie weniger JavaScript; teilen Sie Code auf, lazy-loaden Sie, und bevorzugen Sie Plattformfähigkeiten.
- Besonders für Behörden sind Performance und Resilienz Voraussetzungen für gerechten Zugang.

## Referenzen und weiterführende Literatur

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive Verbesserung)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, Schriften über Performance, Code-Splitting, und die Kosten von JavaScript
- Google, *Web Vitals* und web.dev-Performance-Leitlinien
- MDN Web Docs, Web-Plattform- und Progressive-Enhancement-Referenzen
- Alex Russell, Essays über die Kosten von JavaScript und Gerätediversität
- UK Government Digital Service, Progressive-Enhancement- und Frontend-Leitlinien
- WHATWG HTML Living Standard und W3C-Web-Plattform-Spezifikationen
