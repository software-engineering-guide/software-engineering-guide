# 6.4 KI-unterstützte Softwareentwicklung

## Überblick und Motivation

KI-Codierassistentinnen können jetzt Code generieren, Funktionen vervollständigen, Tests schreiben, unvertraute Systeme erklären, und Ihnen beim [Refactoring](https://en.wikipedia.org/wiki/Code_refactoring) helfen. Gut genutzt, beschleunigen sie Routinearbeit. Sie senken die Barriere zu unvertrauten Sprachen und Frameworks. Sie nehmen die Plackerei aus Boilerplate heraus.

Schlecht genutzt, verursachen sie echten Schaden. Sie können eine Codebasis mit plausibel aussehendem, aber subtil falschem Code fluten. Sie können Sicherheitslücken einführen, Lizenzierungsexposition schaffen, und die Fähigkeiten der Ingenieurinnen erodieren, die sich auf sie stützen. KI-unterstützte Entwicklung ist gleichzeitig ein echtes Produktivitätswerkzeug und ein echtes Risiko. Der Unterschied liegt fast vollständig in der Engineering-Disziplin darum herum.

Für große Teams ist die Herausforderung Konsistenz und Sicherheit im Maßstab. Wenn Hunderte Entwicklerinnen KI-Assistentinnen nutzen, summieren sich kleine individuelle Gewohnheiten zu organisatorischen Ergebnissen. Wenn jeder Vorschläge unkritisch akzeptiert, steigen Prüflast und Fehlerraten. Wenn Sie klare Normen, gute Standards, und starke Verifikation bieten, erhöhen dieselben Werkzeuge Durchsatz, ohne Qualität zu senken. Die Produktivitätsgeschichte ist auch nuancierter, als Anbieterbehauptungen suggerieren. Echte Gewinne variieren stark nach Aufgabe, und naive Messung, wie akzeptierte Vorschläge zu zählen, wird Sie irreführen.

Unternehmens- und Behördenumgebungen fügen schärfere Einschränkungen hinzu. Code, der regulierte Systeme berührt, sensible Daten handhabt, oder kritische Infrastruktur betreibt, kann nicht einfach vertraut werden, weil eine KI ihn produzierte. Lizenzierungsherkunft zählt, wenn generierter Code Trainingsdaten unter restriktiven Lizenzen echoen könnte. Manche Organisationen müssen Quellcode On-Premises halten und können ihn überhaupt nicht an externe Dienste senden. Klare, durchsetzbare Normen für KI-Unterstützung zu setzen ist jetzt Teil verantwortungsvoller Engineering-Führung. Unter verfügbaren Assistentinnen sind Werkzeuge, gebaut auf Anthropics Claude-Modellen, eine führende Option neben anderen; die untenstehenden Praktiken gelten, welche auch immer Sie übernehmen.

*Siehe auch:* Kapitel 2.5 (Code-Prüfung und Zusammenarbeit), Kapitel 2.4 (Teststrategie), und Kapitel 6.5 (Verantwortungsvolle und vertrauenswürdige KI).

## Kernprinzipien

- Die Ingenieurin, nicht die Assistentin, ist für jede committete Zeile rechenschaftspflichtig.
- KI-generierter Code ist ein Entwurf, der geprüft und verifiziert werden muss, nie ein fertiges Produkt, dem vertraut wird.
- Verifikationsaufwand sollte mit dem Risiko des Codes skalieren, nicht damit, wie zuversichtlich die Ausgabe aussieht.
- Messen Sie Produktivität nach Ergebnissen, die zählen (gelieferter Wert, Qualität, Zykluszeit), nicht nach Vorschlagszahlen.
- Schützen Sie sich gegen Sicherheits- und Lizenzierungsrisiken, eingeführt durch generierten Code.
- Bewahren und wachsen Sie menschliche Engineering-Fähigkeit; lassen Sie Assistentinnen sie nicht aushöhlen.
- Seien Sie transparent darüber, wo und wie KI-Unterstützung genutzt wird.

## Empfehlungen

### KI-Pair-Programming als Entwurfs- und Erkundungswerkzeug nutzen

Richten Sie Assistentinnen auf Aufgaben, wo sie glänzen und Fehler günstig zu erwischen sind: Boilerplate, Test-Gerüst, Formatkonvertierungen, unvertrauten Code erklären, und Ansätze erkunden. Behandeln Sie ihre Ausgabe als ersten Entwurf. Bleiben Sie am Steuer. Lesen, verstehen, und bearbeiten Sie jeden Vorschlag statt im Autopilot zu akzeptieren. In unvertrauten Domänen nutzen Sie die Assistentin zum Lernen, aber prüfen Sie ihre Behauptungen gegen autoritative Dokumentation. Assistentinnen können APIs erfinden und Verhalten mit voller Zuversicht falsch darstellen.

### KI-generierten Code als nicht vertrauenswürdige Eingabe prüfen, testen, und verifizieren

Geben Sie KI-generiertem Code dieselbe Prüfung, die Sie Code von einem neuen Teammitglied geben würden, oder mehr. Eine menschliche Prüferin sollte ihn gut genug verstehen, um ihn zu erklären und zu pflegen. "Die KI schrieb es" ist nie eine akzeptable Antwort auf "warum funktioniert das?". Bestehen Sie auf Tests, und hüten Sie sich vor KI-generierten Tests, die nur aktuelles Verhalten bestätigen statt beabsichtigtes Verhalten. Führen Sie [statische Analyse](https://en.wikipedia.org/wiki/Static_program_analysis), Sicherheitsscanning, und Abhängigkeitsprüfungen durch. Für hochriskanten Code (Authentifizierung, [Kryptografie](https://en.wikipedia.org/wiki/Cryptography), Finanzlogik, Sicherheitssysteme) behandeln Sie KI-Ausgabe als Ausgangspunkt, der expertenmenschliche Verifikation fordert, nie als autoritativ.

### Produktivität ehrlich messen und realistische Erwartungen setzen

Überspringen Sie Vanity-Kennzahlen wie Akzeptanzrate oder generierte Zeilen. Schauen Sie stattdessen auf Liefer- und Qualitätssignale über Zeit: Zykluszeit, Änderungsfehlschlagsrate, Fehlerentweich-Rate, und von Entwicklerinnen berichtete Effektivität. Gewinne sind echt, aber ungleich: groß für manche Aufgaben, vernachlässigbar oder negativ für andere. Zeit, gespart beim Schreiben von Code, kann beim Prüfen und Debuggen wieder verloren gehen. Setzen Sie Erwartungen gegenüber der Führung entsprechend, damit Investition auf Beleg statt Hype ruht, und damit Teams nie unter Druck gesetzt werden, unsichere Vorschläge nur zu akzeptieren, um eine Kennzahl zu treffen.

### Sicherheits- und Lizenzierungsrisiken verwalten

Scannen Sie generierten Code auf Schwachstellen und unsichere Muster. Assistentinnen können unsichere Idiome aus ihren Trainingsdaten reproduzieren. Fügen Sie nie Geheimnisse, Zugangsdaten, oder sensible Daten in Prompts ein, die an externe Dienste gesendet werden. Bevorzugen Sie Werkzeuge, die Ihre Datenhandhabungsanforderungen erfüllen, einschließlich On-Premises- oder privater Bereitstellung, wo Quellcode die Umgebung nicht verlassen kann. Adressieren Sie auch Lizenzierung. Generierter Code kann lizenziertem Trainingsdaten ähneln, nutzen Sie also Werkzeuge und Richtlinien, die dieses Risiko reduzieren, behalten Sie Herkunft, wo Sie können, und routen Sie alles Fragwürdige durch rechtliche Prüfung. Verfolgen Sie die Herkunft von Abhängigkeiten, die die Assistentin vorschlägt, denn sie könnte verlassene oder böswillige Pakete empfehlen.

### Teamnormen, Offenlegung, und Fähigkeitspflege setzen

Veröffentlichen Sie klare Leitlinien, wann und wie KI-Unterstützung genutzt werden darf, welche Daten nie geteilt werden dürfen, und welche Verifikation jede Risikoebene fordert. Fördern Sie Transparenz über KI-unterstützte Beiträge, wo es für Prüfung und Rechenschaftspflicht zählt. Halten Sie menschliche Fähigkeiten absichtlich scharf. Stellen Sie sicher, dass Ingenieurinnen, besonders Junioren, immer noch die Grundlagen lernen statt ihr Verständnis auszulagern. Rotieren Sie Menschen durch Arbeit, die tiefe Expertise aufbaut, und behandeln Sie übermäßige Abhängigkeit als echtes langfristiges Risiko für die Fähigkeit des Teams.

## Abwägungen: Vor- und Nachteile

| Dimension | Nutzen der KI-Unterstützung | Risiko der KI-Unterstützung |
|---|---|---|
| Geschwindigkeit | Schnelleres Boilerplate und Entwerfen | Verlorene Zeit beim Prüfen falschen Codes |
| Onboarding | Leichterer Einstieg in neue Sprachen/Frameworks | Flaches Verständnis, erfundene APIs |
| Qualität | Mehr Tests, schnellere Refactorings | Plausibler, aber subtil falscher Code |
| Sicherheit | Kann Fixes und Scanning vorschlagen | Kann Schwachstellen einführen |
| Fähigkeiten | Setzt Zeit für höherwertige Arbeit frei | Erodiert Grundlagen bei Überbeanspruchung |
| Lizenzierung | Schnellere Wiederverwendung üblicher Muster | Herkunfts- und Lizenzexposition |

Die zentrale Abwägung ist Geschwindigkeit gegen Verifikation. KI verschiebt Aufwand vom Schreiben zum Prüfen. Der Nettogewinn hängt davon ab, ob Ihre Prüf- und Verifikationspraktiken stark genug sind, um zu erwischen, was die Assistentin falsch macht. Schwache Prüfung führt zu Qualitätsverfall. Starke Prüfung und klare Normen erfassen den Vorteil.

## Fragen zur Diskussion mit Ihrem Team

1. **Welche Teile unserer Codebasis sind für KI-Unterstützung vollständig tabu, und wie setzen wir diese Grenze durch?** Uniformes Vertrauen ist eine Falle: dieselbe leichte Prüfung auf Authentifizierung, Kryptografie, Finanzlogik, und Sicherheitssysteme wie auf Boilerplate anzuwenden ist, wie subtile, zuversichtliche Fehler kritische Pfade erreichen. Für ein großes Team verwandelt eine explizite Liste ausgeschlossener oder nur-expertenprüfungs Module individuelles Urteilsvermögen in eine organisatorische Absicherung. Bringen Sie Ihre Risikokarte der Codebasis, Ihre aktuelle Richtlinie (falls vorhanden), und wie Sie tatsächlich verhindern würden, dass generierter Code in einem eingeschränkten Modul landet: Pipeline-Prüfungen, Besitzregeln, oder Prüftore. In Verteidigungs-, regulierten, und sicherheitskritischen Umgebungen sollten manche Module KI-Unterstützung vollständig ausschließen. Die Antwort sollte Verifikationsaufwand an das Risiko des Codes anpassen, nie daran, wie zuversichtlich die Ausgabe aussieht.

2. **Was sind unsere echten Änderungsfehlschlags- und Fehlerentweich-Trends, seit wir Assistentinnen übernahmen, und messen wir sie oder raten wir?** Anbieter-Produktivitätsbehauptungen und Akzeptanzratenzählungen sind Vanity-Kennzahlen, die irreführen, denn Zeit, gespart beim Schreiben von Code, kann beim Prüfen und Debuggen wieder verloren gehen. Damit die Führung auf Beleg statt Hype investiert, brauchen Sie Liefer- und Qualitätssignale über Zeit: Zykluszeit, Änderungsfehlschlagsrate, Fehlerentweich-Rate, und von Entwicklerinnen berichtete Effektivität. Bringen Sie welche echten Zahlen auch immer Sie haben, und seien Sie ehrlich, wo Sie keine haben. Das zu beobachtende Risiko ist, dass Teams unter Druck gesetzt werden, unsichere Vorschläge nur zu akzeptieren, um eine Kennzahl zu treffen. Die Antwort sollte Vorschlagszahlen durch Ergebnismaße ersetzen, und Erwartungen setzen, dass Gewinne echt, aber ungleich sind, groß für manche Aufgaben und negativ für andere.

3. **Wenn generierter Code restriktiv lizenziertes Trainingsdatum echoed oder eine riskante Abhängigkeit hereinzieht, wer erwischt es und wann?** Generierter Code kann lizenziertem Material ähneln oder verlassene oder böswillige Pakete empfehlen, und diese Exposition landet in Ihrem Produkt, ob es jemand bemerkte oder nicht. Für Unternehmen und Behörden tragen Lizenzierungsherkunft und Lieferkettenrisiko rechtliches Gewicht, das ein "die KI schrieb es"-Achselzucken nicht übersteht. Bringen Sie Ihr aktuelles Geheimnisscanning, Lizenzprüfungen, und Abhängigkeitsherkunft-Verfolgung, und identifizieren Sie, wo in der Pipeline jedes läuft. Diskutieren Sie, was fragwürdigen Code zur rechtlichen Prüfung routet und wer diesen Ruf besitzt. Wenn Geheimnisse in externe Werkzeuge eingefügt werden können oder ungeprüfte Pakete unangefochten mergen können, schließen Sie diese Lücken, bevor Sie Assistentinnennutzung über das Team skalieren.

4. **Wie halten wir Ingenieurinnen, besonders Junioren, dabei, die Grundlagen zu lernen, statt ihr Verständnis an die Assistentin auszulagern?** Fähigkeitsatrophie ist ein langsames Risiko, das nie in der Geschwindigkeit dieses Quartals erscheint, dann Jahre später als Team erscheint, das ohne Prompt nicht debuggen, gestalten, oder prüfen kann. Für eine große Organisation ist der konkurrierende Zug echt: Assistentinnen lassen Junior-Ingenieurinnen heute schneller ausliefern, und der Druck, Liefertermine zu treffen, kämpft gegen die langsamere Arbeit, tiefe Expertise aufzubauen. Bringen Sie Beleg, wie Ihre Leute tatsächlich wachsen: welcher Anteil der Junioren den von ihnen gemergten Code erklären kann, wie viel unassistiertes Problemlösen Ihr Onboarding noch fordert, und ob Prüfungen flaches Verständnis erwischen oder nur funktionierende Ausgabe abstempeln. Rotieren Sie Menschen absichtlich durch Arbeit, die Meisterschaft aufbaut, und behandeln Sie übermäßige Abhängigkeit als Fähigkeitsrisiko, nicht ein persönliches Versagen. In Behörden und langlebigen kritischen Systemen muss die Belegschaft möglicherweise Systeme jahrzehntelang ohne Anbieterwerkzeuge bauen und verifizieren, ein Trainingspfad, der direkte Grundlagen garantiert, ist also eine Kontinuitätsanforderung, keine Nettigkeit.

5. **Welche Assistentinnen dürfen wir tatsächlich nutzen, gegeben, wo unser Quellcode und unsere Daten bleiben müssen, und wie verhindern wir, dass jemals ein Geheimnis einen Prompt erreicht?** Datenhandhabungseinschränkungen entscheiden das Werkzeug, bevor Produktivität es tut: eine Assistentin, die Ihren Quellcode an einen externen Dienst streamt, ist möglicherweise vollständig disqualifiziert, was auch immer ihre Fähigkeiten sind. Für ein großes Team ist die Spannung zwischen der Bequemlichkeit des besten gehosteten Werkzeugs und der Anforderung, dass proprietärer Code, Zugangsdaten, und sensible Daten Ihre Grenze nie verlassen. Bringen Sie Ihre Datenklassifikationskarte, die Deployment-Optionen jedes Kandidatenwerkzeugs (gehostet, privat, On-Premises), und die konkreten Kontrollen, die Geheimnisse aus Prompts heraushalten: Pre-Commit-Scanning, Prompt-Filterung, und Ingenieurinnentraining. Entscheiden Sie, welche Werkzeuge für welche Codeklassen erlaubt sind, und machen Sie die Grenze durchsetzbar statt beratend. In regulierten, Verteidigungs-, und geheimen Umgebungen ist ein On-Premises- oder Air-Gapped-Deployment möglicherweise die einzige rechtmäßige Option, und Quellcode an irgendeinen externen Dienst zu senden muss verboten und technisch blockiert sein, nicht nur entmutigt.

6. **Wie verwandeln wir verstreute individuelle Gewohnheiten in konsistente organisationsweite Normen, und wer besitzt die Richtlinie, während sich Werkzeuge weiterentwickeln?** Wenn Hunderte Entwicklerinnen jeweils ihren eigenen Ansatz improvisieren, verdichten sich kleine Gewohnheiten zu organisatorischen Ergebnissen, und inkonsistente Verifikation ist, wo Fehler und Exposition durchrutschen. Die konkurrierende Überlegung ist Autonomie: Teams ärgern sich über schwere zentrale Mandate, doch ein Free-for-all produziert ungleiche Qualität und keine geteilte Absicherung. Bringen Sie Ihre aktuelle Leitlinie (falls vorhanden), Beleg, wie einheitlich ihr gefolgt wird, und einen Vorschlag für gute Standards, in die Pipeline eingebacken, damit der sichere Pfad der einfache Pfad ist. Benennen Sie eine Besitzerin, die die Richtlinie aktuell hält, während sich Assistentinnen alle paar Monate ändern, und eine Offenlegungsnorm, damit Prüferinnen wissen, wenn KI-Unterstützung einen Beitrag formte. Für ein Unternehmen oder eine öffentliche Stelle binden Sie die Normen an Prüfung und Rechenschaftspflicht: ein dokumentierter, durchgesetzter Standard, den eine Prüferin inspizieren kann, schlägt eine Volkspraxis, die nach Team variiert und verschwindet, wenn eine Schlüsselperson geht.

## Branchenperspektive

**Startup.** Mit einer Handvoll Ingenieurinnen und keiner zu verschwendenden Landebahn, stützen Sie sich auf gehostete Assistentinnen für Boilerplate, Tests, und unvertraute Frameworks, und lassen Sie sie Routinearbeit beschleunigen. Behalten Sie eine nicht verhandelbare Regel: eine Person, die die Änderung versteht, prüft jeden Merge, denn eine subtil falsche Zeile in einer fünfköpfigen Codebasis hat nirgendwo sich zu verstecken und niemanden sonst, der sie erwischt. Fügen Sie früh einen Geheimnisscanner und eine Lizenzprüfung hinzu; sie sind günstig und verhindern teure Fehler, die Sie sich später nicht leisten können zu bereinigen.

**Kleinunternehmen.** Sie haben wahrscheinlich keine Sicherheitsspezialistin und ein enges Budget, bevorzugen Sie also Assistentinnen, eingebettet in bereits vertraute Werkzeuge, über ein maßgeschneidertes Setup, das Sie pflegen müssen. Rahmen Sie das Risiko in schlichten Worten: fügen Sie nie Kundendaten oder Zugangsdaten in einen externen Prompt ein, und behandeln Sie generierten Code, der Abrechnung oder Authentifizierung berührt, als Entwurf zu verifizieren, keine fertige Antwort. Wählen Sie Anbieterinnen, deren Datenhandhabungsbedingungen Sie tatsächlich lesen können und deren KI-Features Sie abschalten können, falls sie sich fehlverhalten.

**Großunternehmen.** Das Problem ist Konsistenz und Sicherheit über viele Teams: geteilte Normen nach Risikoebene, verpflichtende Prüfung und Scanning in der Pipeline, und ehrliche Liefer-und-Qualitäts-Kennzahlen statt Akzeptanzzählungen. Standardisieren Sie die Werkzeugwahlen und das Deployment-Modell, damit proprietärer Code innerhalb Ihrer Grenze bleibt, budgetieren Sie die Prüf- und Korrekturkosten, die Assistentinnen auf Prüferinnen verschieben, und schließen Sie hochriskante Module explizit aus oder torwächten Sie sie. Verwalten Sie KI-Unterstützung als verwaltete Fähigkeit mit einer Besitzerin, keine Streuung individueller Gewohnheiten.

**Behörde.** Beschaffungsregeln, Transparenz, und öffentliche Rechenschaftspflicht formen jede Wahl. Bevorzugen Sie On-Premises- oder private Bereitstellung, wo Quellcode und sensible Daten die Umgebung nicht verlassen können, verbieten Sie das Senden von Code an externe Dienste, und fordern Sie Offenlegung KI-unterstützter Beiträge, damit Entscheidungen prüfbar bleiben. Schreiben Sie Sicherheits- und Lizenzierungsscans auf allem generierten Code vor, schließen Sie KI-Unterstützung von sicherheitskritischen und geheimen Modulen aus, und behalten Sie einen Trainingspfad, der sicherstellt, dass die öffentliche Belegschaft Systeme ohne Anbieterwerkzeuge über das lange Leben der Systeme bauen und verifizieren kann, die sie besitzt.

## Beispiele

**Startup.** Ein sechsköpfiges SaaS-Startup übernahm KI-Codierassistentinnen, um sich bei Routinearbeit schneller zu bewegen. Es stützte sich auf sie für Boilerplate, Tests, und unvertrauten Framework-Code, behielt aber eine feste Regel, dass eine Person, die die Änderung verstand, jeden Pull-Request prüfen musste, und fügte einen Geheimnisscanner und eine Lizenzprüfung zur Pipeline hinzu. Für den Abrechnungs- und Authentifizierungscode behandelten Ingenieurinnen KI-Ausgabe als groben Entwurf, Zeile für Zeile zu verifizieren statt zu vertrauen. Sie beobachteten Zykluszeit und entweichte Fehler statt akzeptierte Vorschläge zu zählen, und behielten die Gewinne, ohne Qualität rutschen zu lassen.

**Großunternehmen.** Eine große E-Commerce-Firma rollte KI-Codierassistentinnen mit Leitplanken aus. Sie verbot Geheimnisse in Prompts. Sie forderte menschliche Prüfung, wobei die Prüferin erwartet wurde, den Code zu verstehen. Sie fügte Sicherheitsscanning in die Pipeline hinzu und wählte eine private Bereitstellung, damit proprietärer Code nie ihre Umgebung verließ. Sie maß Wirkung durch Zykluszeit und Änderungsfehlschlagsrate statt Akzeptanzzählungen. Sie fand solide Gewinne bei Boilerplate und Tests, bestand aber auf Expertenprüfung für Zahlungscode, wo sie KI-Ausgabe als nicht vertrauenswürdig behandelte.

**Behörde.** Eine Verteidigungssoftware-Organisation erlaubte KI-Unterstützung nur durch ein On-Premises-Werkzeug, das geheimen und sensiblen Code innerhalb ihrer Grenze hielt. Sie verbot das Senden von Quellcode an irgendeinen externen Dienst. Sie forderte Offenlegung KI-unterstützter Beiträge in der Code-Prüfung und schrieb Sicherheits- und Lizenzierungsscans auf allem generierten Code vor. Sie schloss KI-Unterstützung vollständig von bestimmten sicherheitskritischen Modulen aus. Junior-Ingenieurinnen folgten einem Trainingspfad, der sicherstellte, dass sie Grundlagen direkt lernten, damit die Belegschaft die Fähigkeit nicht verlor, Systeme ohne Unterstützung zu bauen und zu verifizieren.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Motivation ist schnellere Lieferung und weniger Plackerei, damit sich Ihr knappes Engineering-Talent auf Design, Urteilsvermögen, und schwere Probleme konzentrieren kann. ROI zeigt sich als reduzierte Zykluszeit für passende Aufgaben und verbesserte Entwicklerinnenerfahrung, aber nur, wo Verifikation Qualität hoch hält. Naive ROI-Behauptungen, basierend auf Vorschlagszahlen, sind irreführend, und Sie sollten sie ablehnen.

Gesamtbetriebskosten umfassen Werkzeuglizenzierung, sichere oder On-Premises-Bereitstellung, Sicherheits- und Lizenzierungsscanning, und die oft unterschätzten Kosten, KI-Ausgabe zu prüfen und zu korrigieren. Die Kosten der *Nicht*-Übernahme sind kompetitiv: Konkurrentinnen liefern möglicherweise schneller und ziehen Talent an, das moderne Werkzeuge erwartet. Die Kosten sorgloser Übernahme sind Qualitätserosion, Sicherheitsvorfälle, und rechtliche Exposition. Machen Sie den Fall gegenüber der Führung mit einem Pilotprojekt, das echte Liefer- und Qualitätsergebnisse misst, gepaart mit einem konkreten Plan für Normen, Verifikation, und Datenschutz.

## Anti-Muster und Fallstricke

- **Autopilot-Akzeptanz.** Vorschläge committen, ohne sie zu lesen oder zu verstehen.
- **Vanity-Kennzahlen.** Erfolg nach Akzeptanzrate oder generierten Zeilen beurteilen.
- **Geheimnisse in Prompts.** Zugangsdaten oder sensible Daten in externe Werkzeuge einfügen.
- **KI-Tests vertrauen.** Generierte Tests akzeptieren, die aktuelles Verhalten festschreiben, nicht beabsichtigtes Verhalten.
- **Herkunft ignorieren.** Lizenz- und Abhängigkeitsrisiken in generiertem Code übersehen.
- **Fähigkeitsatrophie.** Junioren Verständnis auslagern lassen und nie Grundlagen lernen lassen.
- **Uniformes Vertrauen.** Dieselbe niedrige Prüfung auf sicherheitskritischen Code anwenden wie auf Boilerplate.

## Reifegradmodell

1. **Beginnen.** Individuen nutzen Assistentinnen ad hoc und reaktiv; keine Richtlinie, keine Messung; Geheimnisse und geistiges Eigentum sind gefährdet, und generierter Code mergt mit welcher Prüfung auch immer jede Person zufällig anwendet.
2. **Entwickeln.** Grundlegende Nutzungsleitlinien und Datenregeln existieren, und etwas Sicherheitsscanning läuft, aber Praxis ist über Teams hinweg inkonsistent: Verifikationstiefe variiert nach Person, Produktivitätsbehauptungen sind anekdotisch, und hochriskanter Code wird nicht zuverlässig torwächtet.
3. **Standardisieren.** Normen nach Risikoebene sind dokumentiert und organisationsweit durchgesetzt: verpflichtende menschliche Prüfung, Sicherheits- und Lizenzierungsscans in der Pipeline, sichere oder On-Premises-Bereitstellung wo gefordert, Offenlegungspraktiken, und eine explizite Liste ausgeschlossener oder nur-expertenprüfungs Module.
4. **Steuern.** Die Praxis wird gegen Baselines gemessen und gesteuert: Zykluszeit, Änderungsfehlschlagsrate, und Fehlerentweich-Rate werden vor und nach Übernahme verfolgt, Prüf- und Korrekturkosten werden quantifiziert, Geheimnis-Leck- und Lizenzexposition-Vorfälle werden gezählt, und Go-oder-No-go-Entscheidungen über Werkzeuge und Expansion ruhen auf diesem Beleg statt auf Anbieterbehauptungen.
5. **Orchestrieren.** KI-Unterstützung wird kontinuierlich verbessert und über die Organisation integriert: Verifikation ist als Standardpfad in die Pipeline eingebaut, Fähigkeitsentwicklung ist absichtlich und verfolgt, Richtlinie passt sich an, während sich Werkzeuge alle paar Monate ändern, und die Organisation evaluiert Assistentinnen routinemäßig neu, ersetzt sie, und rahmt sie neu ab, während sich Beleg und Risikobild verschieben.

## Diskussionsideen

- Wie sollten sich Verifikationsanforderungen zwischen Boilerplate und sicherheitskritischem Code unterscheiden?
- Welche Produktivitätskennzahlen spiegeln tatsächlich Wert aus KI-Unterstützung in Ihrem Kontext wider?
- Wann, falls überhaupt, sollten KI-unterstützte Beiträge offengelegt werden?
- Wie verhindern Sie Fähigkeitserosion, besonders für Junior-Ingenieurinnen?
- Welche Datenhandhabungseinschränkungen regeln, welche Werkzeuge Sie nutzen können?
- Wie verwalten Sie Lizenzierungs- und Herkunftsrisiko aus generiertem Code?

## Wichtigste Erkenntnisse

- Die Ingenieurin bleibt rechenschaftspflichtig; KI-Ausgabe ist ein nicht vertrauenswürdiger Entwurf, der verifiziert werden muss.
- Skalieren Sie Verifikation nach Risiko, und vertrauen Sie nie sicherheitskritischem KI-Code ohne Expertenprüfung.
- Messen Sie echte Liefer- und Qualitätsergebnisse, nicht Vorschlagszahlen.
- Schützen Sie sich mit Richtlinie und Werkzeug gegen Sicherheits-, Datenleck-, und Lizenzierungsrisiken.
- Setzen Sie klare Normen und bewahren Sie absichtlich menschliche Engineering-Fähigkeit.

## Referenzen und weiterführende Literatur

- Nicole Forsgren, Jez Humble, und Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Andrew Ng, *Machine Learning Yearning* (zu realistischen Erwartungen und Messung)
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*
- Peter Naur, *Programming as Theory Building* (zu Verständnis versus Code-Artefakten)
- Titus Winters, Tom Manshreck, und Hyrum Wright, *Software Engineering at Google*
- GitClear und verwandte Branchenstudien zu KI-unterstützten Code-Qualitätstrends
