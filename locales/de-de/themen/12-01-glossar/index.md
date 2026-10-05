# 12.1 Glossar

Dieses Glossar definiert Begriffe und Akronyme, die durchgehend im Handbuch genutzt werden. Einträge sind alphabetisch gruppiert. Wo ein Eintrag ein gängiges Akronym hat, wird es in Klammern gezeigt. Definitionen sind absichtlich knapp gehalten; konsultieren Sie das relevante Kapitel für vollere Behandlung.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Ein Autorisierungsmodell, das Zugriff basierend auf bewerteten Attributen der Nutzerin, Ressource, Aktion, und Umgebung gewährt (zum Beispiel Abteilung, Freigabe, Tageszeit) statt fester Rollen. Es bietet feingranulare, richtliniengetriebene Kontrolle auf Kosten größerer Komplexität als RBAC.

**[Barrierefreiheit (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: Die Praxis, Software so zu entwerfen und zu bauen, dass Menschen mit Behinderungen sie wahrnehmen, verstehen, navigieren, und mit ihr interagieren können. Das "a11y"-Numeronym kürzt die 11 Buchstaben zwischen "a" und "y" ab.

**ADR (Architecture Decision Record)**: Ein kurzes, versioniertes Dokument, das eine einzelne bedeutsame architektonische oder technische Entscheidung, ihren Kontext, die betrachteten Optionen, und ihre Konsequenzen erfasst. ADRs erschaffen eine dauerhafte, überprüfbare Geschichte, warum ein System ist, wie es ist.

**Aggregat**: In Domain-Driven Design, ein Cluster von Domänenobjekten, als eine einzelne Einheit für Datenänderungen behandelt, mit einer Entität als Aggregat-Root, die Invarianten durchsetzt. Aggregate definieren Konsistenz- und Transaktionsgrenzen.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: Ein definierter Vertrag, durch den ein Softwarestück Dienste oder Daten von einem anderen anfragt. Gut entworfene APIs verstecken Implementierungsdetail und bieten stabile, versionierte Schnittstellen.

**API-first**: Ein Entwicklungsansatz, in dem der API-Vertrag entworfen und vereinbart wird, bevor implementiert wird, damit Konsumentinnen und Anbieterinnen parallel gegen eine geteilte Spezifikation arbeiten können.

**arc42**: Eine offene, vorlagenbasierte Struktur zur Dokumentation von Softwarearchitektur, in zwölf Abschnitte organisiert, die Kontext, Einschränkungen, Bausteine, Laufzeit, Bereitstellung, und Entscheidungen abdecken.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Eine W3C-Spezifikation, die Rollen, Zustände, und Eigenschaften definiert, die dynamische und benutzerdefinierte Webkomponenten für assistive Technologien wie Screenreader verständlich machen.

**ASR (Architecturally Significant Requirement)**: Eine Anforderung mit messbarer, weitreichender Wirkung auf Architektur, wie eine Leistungs-, Verfügbarkeits-, Sicherheits-, oder regulatorische Einschränkung. ASRs treiben die folgenreichsten Designentscheidungen.

**ASVS (Application Security Verification Standard)**: Ein OWASP-Standard, der eine gestufte Checkliste von Sicherheitsanforderungen und Tests zum Entwerfen, Bauen, und Verifizieren sicherer Anwendungen bietet.

**[Autoskalierung](https://en.wikipedia.org/wiki/Autoscaling)**: Die automatische Anpassung der Anzahl laufender Recheninstanzen (oder ihrer Größe) als Reaktion auf Last, damit Kapazität Nachfrage ohne manuellen Eingriff verfolgt. Sie ergänzt absichtliche Kapazitätsplanung, ersetzt sie aber nicht.

**[Verfügbarkeit](https://en.wikipedia.org/wiki/Availability)**: Der Anteil der Zeit, in der ein System operativ und in der Lage ist, Anfragen zu bedienen, oft in "Neunen" ausgedrückt (zum Beispiel 99,9%). Es ist ein Kernzuverlässigkeitsziel, in SLOs und SLAs kodifiziert.

## B

**Backpressure**: Ein Flusssteuerungsmechanismus, in dem eine unter Last stehende Komponente vorgelagerten Produzentinnen signalisiert, langsamer zu werden, unbegrenzte Warteschlangen und kaskadierenden Fehlschlag verhindernd. Zentral für verlässliche Streaming- und nachrichtengetriebene Systeme.

**[BDD (Behavior-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Eine kollaborative Praxis, die Anforderungen als konkrete, menschenlesbare Verhaltensbeispiele ausdrückt (oft in Given/When/Then-Form), die als automatisierte Abnahmetests dienen.

**BFF (Backend for Frontend)**: Ein Architekturmuster, in dem ein dedizierter Backend-Dienst für einen spezifischen Frontend- oder Client-Typ gebaut wird, Datenformung und -aggregation auf die Bedürfnisse dieses Clients zugeschnitten.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: Die Werkzeuge, Prozesse, und Praktiken, Geschäftsdaten zu sammeln, zu integrieren, und zu analysieren, um Berichterstattung, Dashboards, und Entscheidungsfindung zu unterstützen.

**Schuldfreies Postmortem**: Eine Vorfallüberprüfung, die auf systemische Ursachen und Lernen fokussiert statt individuelle Schuld, auf der Prämisse, dass Menschen angesichts der Information und Anreize, die sie hatten, vernünftig handeln.

**[Blau-Grün-Bereitstellung](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Eine Veröffentlichungsstrategie, die zwei identische Produktionsumgebungen ("blau" und "grün") betreibt, Verkehr zu einer leitend, während die andere aktualisiert wird, nahezu sofortigen Umstieg und Rollback ermöglichend.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Eine weit genutzte Rankingfunktion für Volltextsuche, die bewertet, wie gut ein Dokument zu einer Abfrage passt, Termfrequenz, inverse Dokumentfrequenz, und Dokumentlänge nutzend. Es ist der lexikalische-Ranking-Standard in vielen Suchmaschinen.

**Bounded Context**: In Domain-Driven Design, eine explizite Grenze, innerhalb derer ein bestimmtes Domänenmodell und seine allgegenwärtige Sprache konsistent gelten. Es verhindert, dass Konzepte über unterschiedliche Teile eines großen Systems vermischt werden.

**Build-Cache**: Ein Speicher zuvor berechneter Build-Ausgaben, nach den Eingaben geschlüsselt, die sie produzierten, damit unveränderte Arbeit wiederverwendet statt neu gebaut wird. Ein geteilter entfernter Build-Cache lässt ein ganzes Team und seine CI die Ergebnisse des jeweils anderen wiederverwenden.

**[Bus-Faktor](https://en.wikipedia.org/wiki/Bus_factor)**: Die Anzahl Menschen, die verloren gehen müssten (metaphorisch "von einem Bus überfahren"), bevor ein Projekt mangels wesentlichen Wissens stockt. Ein niedriger Bus-Faktor signalisiert konzentrierte, undokumentierte Expertise und organisatorisches Risiko.

## C

**[Cache-Verdrängungsrichtlinie](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: Die Regel, die ein Cache nutzt, um zu entscheiden, welcher Eintrag zu entfernen ist, wenn er voll ist, wie Least Recently Used (LRU) oder Least Frequently Used (LFU). Die Richtlinie formt Trefferrate und damit den Wert des Caches.

**[Cache-Invalidierung](https://en.wikipedia.org/wiki/Cache_invalidation)**: Das Problem, gecachte Daten zu entfernen oder zu aktualisieren, sobald sich die zugrunde liegende Quelle ändert, damit Leserinnen keine veralteten Werte sehen. Berühmt eines der härtesten Probleme im Computing.

**[Cache-Stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Ein Fehlschlagsmodus, in dem viele Clients gleichzeitig den Cache für denselben Schlüssel verfehlen und alle gemeinsam den Ursprung treffen, ihn überwältigend. Anfragenbündelung und gestaffelter Ablauf verhindern es. Auch tosende Herde genannt.

**Kanarienveröffentlichung**: Eine Bereitstellungstechnik, die eine neue Version zuerst einer kleinen Teilmenge Nutzerinnen oder Verkehr exponiert, auf Probleme überwacht, und dann den Rollout progressiv erweitert, falls Kennzahlen gesund bleiben.

**[CAP-Theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: Ein Prinzip, das besagt, dass ein verteilter Datenspeicher höchstens zwei von Consistency, Availability, und Partition Tolerance gleichzeitig garantieren kann; weil Partitionen unvermeidlich sind, tauschen Designerinnen während ihnen effektiv Konsistenz gegen Verfügbarkeit.

**[C4-Modell](https://en.wikipedia.org/wiki/C4_model)**: Ein leichtgewichtiger Ansatz, Softwarearchitektur auf vier Abstraktionsebenen zu visualisieren: System Context, Containers, Components, und Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Continuous Delivery hält Software in einem veröffentlichbaren Zustand, damit sie jederzeit mit manueller Genehmigung bereitgestellt werden kann; Continuous Deployment veröffentlicht automatisch jede Änderung, die die Pipeline besteht.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Ein geografisch verteiltes Netzwerk von Edge-Servern, das Inhalt nah an Nutzerinnen cacht und bedient, Latenz kürzend und Ursprungsinfrastruktur entlastend.

**Chain-of-Thought-Prompting**: Eine Prompting-Technik, die ein Sprachmodell bittet, sich durch zwischenzeitliche Denkschritte zu arbeiten, bevor es eine Endantwort gibt, Leistung bei mehrschrittigen Problemen verbessernd auf Kosten längerer, langsamerer Ausgabe.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: Die Praxis, die Änderungen von Entwicklerinnen häufig in eine geteilte Hauptlinie zu mergen, jeder Merge durch einen automatisierten Build und Testsuite validiert, um Integrationsprobleme früh zu erkennen.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Die kombinierte Pipeline aus Continuous Integration und Continuous Delivery/Deployment, die Bauen, Testen, und Veröffentlichen von Software automatisiert.

**CMMC (Cybersecurity Maturity Model Certification)**: Ein US-Verteidigungsministeriums-Programm, das die Cybersicherheitsreife von Auftragnehmerinnen zertifiziert, die föderale Vertragsinformation und kontrollierte unklassifizierte Information handhaben.

**[Kohäsion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Der Grad, zu dem die Elemente innerhalb eines Moduls zusammengehören und einem einzelnen, wohldefinierten Zweck dienen. Hohe Kohäsion, mit niedriger Kopplung gepaart, ist ein Kennzeichen pflegbaren Designs.

**Context Window**: Die maximale Textmenge, in Tokens gemessen, die ein Sprachmodell gleichzeitig berücksichtigen kann, seine Eingabe und Ausgabe umspannend. Es ist ein knappes Budget, das Prompt- und Kontextdesign absichtlich verwalten müssen.

**[Conways Gesetz](https://en.wikipedia.org/wiki/Conway's_law)**: Die Beobachtung, dass die Struktur eines Systems die Kommunikationsstruktur der Organisation widerzuspiegeln tendiert, die es baut. Das "inverse Conway-Manöver" formt Teams absichtlich, um eine gewünschte Architektur zu produzieren.

**Core Web Vitals**: Ein Satz nutzerinnenzentrierter Webleistungskennzahlen, von Google definiert (wie Largest Contentful Paint, Interaction to Next Paint, und Cumulative Layout Shift), die Laden, Interaktivität, und visuelle Stabilität messen.

**[Verzögerungskosten](https://en.wikipedia.org/wiki/Cost_of_delay)**: Die ökonomischen Kosten, etwas noch nicht fertig zu haben, als verlorener Wert pro Zeiteinheit ausgedrückt. Sie explizit zu machen verwandelt Priorisierung von Meinung in Arithmetik, und untermauert Sequenzierungsregeln wie Weighted Shortest Job First.

**[Kopplung](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Der Grad gegenseitiger Abhängigkeit zwischen Modulen oder Diensten. Lockere Kopplung begrenzt den Welleneffekt von Änderung und ist ein zentrales Ziel guter Architektur.

**CQRS (Command Query Responsibility Segregation)**: Ein Muster, das das zum Ändern von Zustand genutzte Modell (Commands) vom zum Lesen von Zustand genutzten Modell (Queries) trennt, jedes unabhängig zu optimieren und zu skalieren erlaubend.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Ein öffentlicher Katalog offengelegter Sicherheitsschwachstellen, jede einem eindeutigen Identifikator zugewiesen, damit Werkzeuge und Teams sich unzweideutig auf denselben Fehler beziehen können.

**CWV**: Siehe Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Sicherheitstesten, das eine laufende Anwendung von außen sondiert, ohne Zugriff auf Quellcode, um zur Laufzeit erscheinende Schwachstellen zu finden.

**Daten-Tinten-Verhältnis**: Ein Prinzip von Edward Tufte, das besagt, dass ein Diagramm den meisten seiner Tinte auf die Daten selbst verwenden sollte und wenig auf Dekoration, Gitternetzlinien, Rahmen, und Chartjunk entfernend, die nicht informieren.

**[Data Mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Eine dezentralisierte Datenarchitektur und Betriebsmodell, das Daten als von Domänenteams besessenes Produkt behandelt, von Self-Service-Plattforminfrastruktur und föderierter Governance unterstützt.

**[Datenvisualisierung](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: Die Praxis, Daten in visueller Form zu kodieren (Position, Länge, Farbe, und dergleichen), damit Muster, Vergleiche, und Trends wahrnehmbar werden und Entscheidungen besser informiert werden.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Ein Ansatz zu Softwaredesign, der das Modell auf die Geschäftsdomäne zentriert, eine geteilte allgegenwärtige Sprache, Bounded Contexts, und Bausteine wie Entities, Value Objects, und Aggregate nutzend.

**Design-Tokens**: Benannte, plattformunabhängige Werte (Farben, Abstände, Typografie, und dergleichen), die Designentscheidungen kodieren, damit sie konsistent über ein Designsystem und mehrere Produkte geteilt werden können.

**DevEx / DevX (Developer Experience)**: Die Gesamtqualität der täglichen Interaktion einer Entwicklerin mit Werkzeugen, Plattformen, und Prozessen, Reibung, Feedback-Geschwindigkeit, und kognitive Last umfassend.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Eine Kultur und ein Satz Praktiken, die Softwareentwicklung und Betrieb vereinen, um Lieferzyklen zu verkürzen, Bereitstellungshäufigkeit zu erhöhen, und Zuverlässigkeit durch Automatisierung und geteilten Besitz zu verbessern.

**DORA (DevOps Research and Assessment)**: Ein Forschungsprogramm und seine vier weit genutzten Lieferkennzahlen (Bereitstellungshäufigkeit, Durchlaufzeit für Änderungen, Änderungsfehlschlagsrate, und Zeit-bis-Wiederherstellung des Dienstes), genutzt, um Softwarelieferleistung zu benchmarken.

**DPIA (Data Protection Impact Assessment)**: Eine strukturierte Bewertung, unter DSGVO für hochrisiko Verarbeitung gefordert, die Datenschutzrisiken identifiziert und mindert, bevor ein Projekt fortschreitet.

**Drift (Konfiguration)**: Die graduelle Divergenz des tatsächlichen Zustands eines Systems von seinem erklärten oder beabsichtigten Zustand, üblicherweise durch manuelle Änderungen verursacht; Infrastructure as Code und GitOps zielen darauf ab, sie zu erkennen und zu korrigieren.

**Drift (Modell)**: In maschinellem Lernen, die Degradation von Modellleistung über Zeit, während sich die statistischen Eigenschaften von Eingabedaten (Datendrift) oder die modellierte Beziehung (Konzeptdrift) ändern.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: Die Strategie, Prozeduren, und Infrastruktur, Dienst und Daten nach einem größeren störenden Ereignis wiederherzustellen, typischerweise von RTO- und RPO-Zielen gesteuert.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Ein Designprinzip, das besagt, dass jedes Wissensstück eine einzelne, maßgebliche Repräsentation haben sollte, Duplikation und das Risiko inkonsistenter Updates reduzierend.

## E

**Ost-West-Verkehr**: Netzwerkverkehr zwischen Diensten innerhalb eines Systems oder Rechenzentrums, im Gegensatz zu Nord-Süd-Verkehr zwischen dem System und externen Clients. Ein Service Mesh steuert üblicherweise Ost-West-Verkehr.

**[Edge Computing](https://en.wikipedia.org/wiki/Edge_computing)**: Berechnung und Speicherung nah an dem Ort auszuführen, wo Daten produziert oder konsumiert werden, statt an einem zentralen Standort, um Latenz und Bandbreite zu kürzen. Content Delivery Networks sind eine frühe, weitverbreitete Form.

**[Elastizität](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: Die Fähigkeit eines Systems, automatisch Ressourcen zu erwerben und freizugeben als Reaktion auf sich ändernde Nachfrage, damit Kapazität Last eng verfolgt.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Ein Datenintegrationsmuster, das rohe Daten zuerst in einen Zielspeicher lädt und sie dort transformiert, den Maßstab moderner Warehouses und Lakehouses ausnutzend.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: Eine Repräsentation von Text, Bildern, oder anderen Daten als dichter numerischer Vektor, so positioniert, dass ähnliche Punkte nah zusammensitzen. Embeddings treiben semantische und Vektorsuche sowie Retrieval-Augmented Generation.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Der europäische Standard, der Barrierefreiheitsanforderungen für ICT-Produkte und -Dienste spezifiziert, von öffentliche-Sektor-Beschaffung über die EU referenziert und mit WCAG ausgerichtet.

**Fehlerbudget**: Die von einem SLO über eine Periode erlaubte Menge Unzuverlässigkeit; wenn es erschöpft ist, priorisieren Teams Zuverlässigkeitsarbeit über neue Features. Es versöhnt die Spannung zwischen Geschwindigkeit und Stabilität.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Ein Datenintegrationsmuster, das Daten aus Quellen extrahiert, in eine Zielform transformiert, und in ein Ziel wie ein Warehouse lädt.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: EU-Regulierung, die KI-Systeme nach Risiko klassifiziert und entsprechend Verpflichtungen auferlegt, bestimmte Nutzungen verbietend und hochrisiko Systeme schwer regulierend.

**[Eventuelle Konsistenz](https://en.wikipedia.org/wiki/Eventual_consistency)**: Ein Konsistenzmodell in verteilten Systemen, in dem Replikate temporär divergieren können, aber zum selben Zustand konvergieren, sobald Updates aufhören sich zu verbreiten.

## F

**[Feature Flag / Feature Toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: Ein Mechanismus, Funktionalität zur Laufzeit ohne Neubereitstellung zu aktivieren oder zu deaktivieren, für graduelle Rollouts, Experimentieren, und operative Kontrolle genutzt.

**Feature Store**: Ein zentralisiertes System, kuratierte Machine-Learning-Features konsistent für sowohl Training als auch Inferenz zu definieren, zu speichern, und zu bedienen, Duplikation und Training/Serving-Skew reduzierend.

**[FedRAMP (Federal Risk and Authorization Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Ein US-Behördenprogramm, das Sicherheitsbewertung, Autorisierung, und kontinuierliche Überwachung für von föderalen Behörden genutzte Cloud-Dienste standardisiert.

**Few-Shot-Prompting**: Einem Sprachmodell eine Handvoll durchgearbeiteter Beispiele im Prompt zu geben, um die gewünschte Aufgabe und das Ausgabeformat zu demonstrieren, im Gegensatz zu Zero-Shot-Prompting, das Anweisungen ohne Beispiele gibt.

**FinOps**: Eine Disziplin und kulturelle Praxis, die finanzielle Rechenschaftspflicht zu variablen Cloud-Ausgaben bringt, Engineering-, Finanz-, und Geschäftsteams geteilten Besitz von Kosten und Wert gebend.

**[FISMA (Federal Information Security Modernization Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: US-Gesetzgebung, die föderale Behörden fordert, Informationssicherheitsprogramme zu implementieren, zu dokumentieren, und zu überwachen, größtenteils durch NIST-Führung operationalisiert.

**Flusseffizienz**: Der Anteil der gesamten Durchlaufzeit, den ein Arbeitspunkt aktiv bearbeitet wird statt zu warten, berechnet als wertschöpfende Zeit geteilt durch gesamte Durchlaufzeit. Die meisten Systeme sind überraschend niedrig, oft unter 15 Prozent.

**Vier-Augen-Prinzip**: Eine Kontrolle, die fordert, dass eine bedeutsame Aktion von mindestens zwei Menschen überprüft oder genehmigt wird, die Chance auf Fehler oder Fehlverhalten reduzierend.

**[Fuzz-Testen (Fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Eine automatisierte Testtechnik, die fehlerhafte, zufällige, oder unerwartete Eingaben in ein Programm füttert, um Abstürze, Sicherheitsfehler, und Randfalldefekte aufzudecken.

## G

**[DSGVO (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Die EU-Regulierung, die die Verarbeitung persönlicher Daten steuert, Individuen Rechte gewährend und Verantwortlichen und Auftragsverarbeiterinnen Verpflichtungen auferlegend, mit bedeutsamen Strafen für Nicht-Compliance.

**GitOps**: Ein operatives Modell, das Git als Einzelwahrheitsquelle für deklarative Infrastruktur und Anwendungen nutzt, mit Automatisierung, die das lebende System kontinuierlich zum verpflichteten Zustand versöhnt.

**Golden Path / Paved Road**: Ein gut unterstützter, meinungsbehafteter Standardweg, Software innerhalb einer Organisation zu bauen und auszuliefern, entworfen, die sichere, konforme, zuverlässige Wahl zur leichtesten zu machen.

**Golden Record**: In Master Data Management, die einzelne, versöhnte, maßgebliche Version einer Geschäftsentität (wie einer Kundin), aus mehreren Quellsystemen durch Matching- und Survivorship-Regeln zusammengesetzt.

**[Gradual Typing](https://en.wikipedia.org/wiki/Gradual_typing)**: Ein Typsystemansatz, der statisches und dynamisches Typen in einer Codebasis koexistieren lässt, damit Typen inkrementell zu einem dynamisch typisierten Programm hinzugefügt werden können. Type Hints und optionale Typprüferinnen sind gängige Beispiele.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Eine Abfragesprache und Laufzeitumgebung für APIs, die Clients erlaubt, genau die Daten anzufragen, die sie in einem einzelnen Aufruf brauchen, ein stark typisiertes Schema nutzend.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Ein hochperformantes, vertragsgetriebenes Remote-Procedure-Call-Framework, das HTTP/2 und, typischerweise, Protocol Buffers für effiziente Dienst-zu-Dienst-Kommunikation nutzt.

## H

**Hermetischer Build**: Ein Build, der nur von explizit deklarierten Eingaben abhängt und von der Host-Umgebung isoliert ist, damit er überall dieselbe Ausgabe produziert. Hermetizität ist das Fundament reproduzierbarer Builds und verlässlichen Cachings.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Ein manipulationssicheres Hardwaregerät, das kryptografische Schlüssel generiert, speichert, und nutzt, stärkeren Schlüsselschutz als reine Softwareansätze bietend.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: US-Gesetzgebung, die unter anderem Anforderungen setzt, geschützte Gesundheitsinformation (PHI) zu sichern, und ihre Nutzung und Offenlegung steuert.

**Horizontale Skalierung**: Kapazität erhöhen, indem mehr Instanzen oder Knoten hinzugefügt werden ("Skalieren nach außen"), statt einen einzelnen Knoten mächtiger zu machen. Es untermauert die meisten großmaßstäblichen, resilienten Architekturen.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Die Praxis, Infrastruktur durch maschinenlesbare, versionskontrollierte Konfiguration zu definieren und bereitzustellen statt manuelle Prozesse, Wiederholbarkeit und Überprüfung ermöglichend.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: Das Framework von Richtlinien und Technologien, das sicherstellt, dass die richtigen Identitäten den richtigen Zugriff auf die richtigen Ressourcen zu den richtigen Zeiten haben.

**IDP / IdP**: "IDP" bezeichnet üblicherweise eine Internal Developer Platform, die Self-Service-Werkzeugschicht, die Infrastruktur für Produktteams abstrahiert; "IdP" bezeichnet eine Identity Provider, einen Dienst, der Nutzerinnen authentifiziert und Assertions ausgibt. Kontext klärt die beiden.

**[Idempotenz](https://en.wikipedia.org/wiki/Idempotence)**: Eine Eigenschaft, bei der eine Operation mehrmals durchzuführen denselben Effekt hat wie sie einmal durchzuführen, wesentlich für sichere Retries in verteilten Systemen und APIs.

**[i18n (Internationalisierung)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Software so zu entwerfen und zu bauen, dass sie ohne Engineering-Änderungen an unterschiedliche Sprachen, Regionen, und kulturelle Konventionen angepasst werden kann. Das Numeronym kürzt die 18 Buchstaben zwischen "i" und "n" ab.

**Unveränderliches Artefakt**: Eine Build-Ausgabe, die, einmal produziert und versioniert, nie geändert wird; jede Änderung ergibt eine neue Version. Unveränderlichkeit macht Veröffentlichungen reproduzierbar und lässt Sie einmal bauen und dasselbe Artefakt über Umgebungen befördern.

**InnerSource**: Die Anwendung von Open-Source-Entwicklungspraktiken (Transparenz, geteilte Repositories, und teamübergreifender Beitrag) innerhalb einer einzelnen Organisation.

**IaC-Drift**: Siehe Drift (Konfiguration).

**[Invertierter Index](https://en.wikipedia.org/wiki/Inverted_index)**: Die Kerndatenstruktur einer Suchmaschine, jeden Term auf die Liste der Dokumente abbildend, die ihn enthalten, damit Abfragen beantwortet werden können, ohne jedes Dokument zu scannen.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Ein internationaler Standard, der Anforderungen für ein Informationssicherheitsmanagementsystem (ISMS) spezifiziert, ein zertifizierbares Framework zum Verwalten von Informationssicherheitsrisiko bietend.

**ISO/IEC 42001**: Ein internationaler Standard, der Anforderungen für ein KI-Managementsystem spezifiziert, Organisationen ein zertifizierbares Framework gebend, die Entwicklung und Nutzung von KI verantwortungsvoll zu steuern.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Ein kompaktes, signiertes (und optional verschlüsseltes) Tokenformat, genutzt, um Claims zwischen Parteien zu übermitteln, üblicherweise für Authentifizierung und Autorisierung in Web- und API-Systemen.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Eine Lean-Workflow-Methode, die Arbeit auf einem Board visualisiert, Work in Progress begrenzt, und Fluss verwaltet, um Durchsatz und Vorhersagbarkeit zu verbessern.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Ein Designprinzip, das die einfachste Lösung bevorzugt, die das Bedürfnis erfüllt, auf der Grundlage, dass unnötige Komplexität Kosten und Risiko erhöht.

**KMS (Key Management Service)**: Ein System zum Erstellen, Speichern, Rotieren, und Steuern des Zugriffs auf kryptografische Schlüssel, oft von Hardware Security Modules unterstützt.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: Ein quantifizierbares Maß, genutzt, um Fortschritt zu einem spezifischen Geschäfts- oder operativen Ziel zu verfolgen.

## L

**Lakehouse**: Eine Datenarchitektur, die den günstigen, flexiblen Speicher eines Data Lake mit den Verwaltungs-, Transaktions-, und Leistungsfeatures eines Data Warehouse kombiniert.

**[Durchlaufzeit](https://en.wikipedia.org/wiki/Lead_time)**: Die verstrichene Zeit von einer angefragten (oder verpflichteten) Änderung bis zu ihrer Lieferung in Produktion; eine Kern-DORA-Lieferkennzahl.

**[Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Ein Sicherheitsprinzip, das jeder Nutzerin, jedem Prozess, oder System nur den minimalen Zugriff gewährt, ihre Funktion durchzuführen, den Schaden durch Kompromittierung oder Fehler begrenzend.

**[Littles Gesetz](https://en.wikipedia.org/wiki/Little's_law)**: Ein Ergebnis aus Warteschlangentheorie, das besagt, dass die durchschnittliche Anzahl Punkte in einem stabilen System gleich der durchschnittlichen Ankunftsrate mal der durchschnittlichen Zeit ist, die jeder Punkt im System verbringt. Es verbindet Work in Progress, Durchsatz, und Durchlaufzeit.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: Ein Machine-Learning-Modell, auf sehr großen Textkorpora trainiert, um Sprache vorherzusagen und zu generieren, fähig zu Aufgaben wie Zusammenfassung, Übersetzung, und Codegenerierung.

**[l10n (Lokalisierung)](https://en.wikipedia.org/wiki/Language_localisation)**: Internationalisierte Software an eine spezifische Locale anzupassen, einschließlich Übersetzung, Formatierung, und kultureller Konventionen. Das Numeronym kürzt die 10 Buchstaben zwischen "l" und "n" ab.

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: Die Disziplin und das Werkzeug, eine einzelne, maßgebliche, konsistente Ansicht von Kerngeschäftsentitäten (wie Kundinnen oder Produkten) über Systeme hinweg zu erschaffen und zu pflegen.

**MITRE ATT&CK**: Eine kuratierte, öffentliche Wissensbasis echtweltlicher Gegnerinnentaktiken und -techniken, weit genutzt, um Red-Team-Übungen zu planen, Erkennungsengineering zu leiten, und Bedrohungen in einem geteilten Vokabular zu beschreiben.

**Mean Time to Recovery (MTTR)**: Die durchschnittliche Zeit, Dienst nach einem Fehlschlag wiederherzustellen; eine gängige Zuverlässigkeits- und Vorfallmanagement-Kennzahl.

**[Mob-Programmierung](https://en.wikipedia.org/wiki/Mob_programming)**: Eine Praxis, in der ein ganzes Team gemeinsam an derselben Aufgabe am selben Computer arbeitet, rotierend, wer tippt, um Wissen zu teilen und Entscheidungen kollektiv zu treffen.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: Der Satz Praktiken, die Machine-Learning-Modelle verlässlich und effizient in Produktion bereitstellen, überwachen, und pflegen, DevOps-Prinzipien auf den ML-Lebenszyklus erweiternd.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Ein einzelnes Versionskontroll-Repository, das den Code für viele Projekte oder die ganze Organisation hält, geteiltes Werkzeug und atomare projektübergreifende Änderungen auf Kosten spezialisierten Skalierungswerkzeugs ermöglichend.

**mTLS (Mutual TLS)**: Eine Konfiguration von Transport Layer Security, in der beide Parteien Zertifikate präsentieren und verifizieren, damit jede die andere authentifiziert. Es ist ein Standard für Dienst-zu-Dienst-Verkehr in einem Service Mesh und Zero-Trust-Netzwerken. Siehe auch [gegenseitige Authentifizierung](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutationstesten](https://en.wikipedia.org/wiki/Mutation_testing)**: Eine Technik, die absichtlich kleine Fehler ("Mutanten") in Code einführt, um zu prüfen, ob die Testsuite sie erkennt, die echte Effektivität der Suite messend.

## N

**[NDCG (Normalized Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Eine Ranking-Qualitätskennzahl, die belohnt, hochrelevante Ergebnisse nah an die Spitze einer Ergebnisliste zu platzieren, normalisiert, damit Werte über Abfragen vergleichbar sind. Eine Grundlage der Suchrelevanzbewertung.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Eine US-Bundesbehörde, deren Special Publications und Frameworks weit referenzierte Standards für Cybersicherheit, Datenschutz, und KI sind.

**NIST AI RMF (AI Risk Management Framework)**: Ein freiwilliges NIST-Framework, mit KI-Systemen verbundene Risiken über ihren Lebenszyklus zu identifizieren, zu bewerten, und zu verwalten, um die Funktionen Govern, Map, Measure, und Manage organisiert.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Ein NIST-Katalog von Sicherheits- und Datenschutzkontrollen für föderale Informationssysteme, weit als Baseline weit über Behörden hinaus genutzt.

**NIST SP 800-171**: Eine NIST-Veröffentlichung, die Anforderungen spezifiziert, kontrollierte unklassifizierte Information (CUI) in nicht-föderalen Systemen zu schützen, zentral für Verteidigungsauftragnehmerinnen-Compliance.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Eine Anforderung, die beschreibt, wie sich ein System verhalten sollte (seine Qualitäten wie Leistung, Sicherheit, Zuverlässigkeit, oder Nutzbarkeit) statt welche Funktionen es ausführt.

**Nord-Süd-Verkehr**: Netzwerkverkehr zwischen einem System und seinen externen Clients (in und aus dem Rechenzentrum oder Cluster), im Gegensatz zu Ost-West-Verkehr zwischen internen Diensten. Ein API-Gateway steuert üblicherweise Nord-Süd-Verkehr.

## O

**Beobachtbarkeit**: Der Grad, zu dem der interne Zustand eines Systems aus seinen externen Ausgaben abgeleitet werden kann, typischerweise durch Telemetrie erreicht: Metriken, Protokolle, und Traces.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Ein Zielsetzungsframework, das ein qualitatives Objective mit ein paar messbaren Key Results paart, um eine Organisation auszurichten und zu fokussieren.

**OpenTelemetry (OTel)**: Ein herstellerneutraler, offener Standard und Werkzeugsatz, Telemetriedaten (Traces, Metriken, und Protokolle) aus Software zu generieren, zu sammeln, und zu exportieren.

**OPA (Open Policy Agent)**: Ein quelloffener, allgemeiner Richtlinienmotor, der Richtlinien (in der Rego-Sprache geschrieben) auswertet, um Autorisierungs- und Konfigurationsregeln über den Stack durchzusetzen, Policy as Code ermöglichend.

**OSPO (Open Source Program Office)**: Eine organisatorische Funktion, die Open-Source-Strategie, Governance, Compliance, und Community-Engagement koordiniert, sowohl Konsum als auch Beitrag verwaltend.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Eine Non-Profit-Community, die weit genutzte, frei verfügbare Anwendungssicherheitsressourcen produziert, einschließlich der OWASP Top Ten und der ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Eine Erweiterung des CAP-Theorems, die besagt, dass, falls es eine Partition gibt, ein System Availability gegen Consistency tauscht, Else (im Normalbetrieb) tauscht es Latency gegen Consistency.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Ein von der Zahlungskartenbranche gepflegter Sicherheitsstandard, der Anforderungen für Organisationen spezifiziert, die Karteninhaberinnendaten speichern, verarbeiten, oder übertragen.

**[Penetrationstest](https://en.wikipedia.org/wiki/Penetration_test)**: Ein autorisierter, simulierter Angriff auf ein System durch geschulte Testerinnen, um ausnutzbare Schwachstellen zu finden und zu demonstrieren, bevor echte Angreiferinnen es tun, als priorisierte, handlungsfähige Erkenntnisse geliefert.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Information, die eine spezifische Person identifizieren kann, allein oder mit anderen Daten kombiniert; ihre Handhabung wird von Datenschutzgesetzen und interner Richtlinie gesteuert.

**Plattform-Engineering**: Die Disziplin, interne Self-Service-Plattformen und Golden Paths zu bauen und zu betreiben, die kognitive Last reduzieren und Produktteams beschleunigen.

**POUR**: Die vier Leitprinzipien der Web Content Accessibility Guidelines: Inhalt muss Perceivable, Operable, Understandable, und Robust sein.

**Produktionsbereitschaftsüberprüfung**: Eine strukturierte Prüfung, vor Live-Gang eines Dienstes oder Übernahme von Bereitschaftsbesitz durchgeführt, die bestätigt, dass er Standards für Beobachtbarkeit, Zuverlässigkeit, Sicherheit, Runbooks, und operative Unterstützung erfüllt.

**[Prompt Engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**: Die Praxis, die Anweisungen, Kontext, und Beispiele, einem Sprachmodell gegeben, zu entwerfen und zu verfeinern, um verlässliche, hochwertige Ausgabe zu bekommen, als versionierte, getestete Engineering-Disziplin statt Versuch und Irrtum behandelt.

**[Prompt Injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Ein Angriff, in dem gestaltete Eingabe ein Sprachmodell dazu bringt, seine beabsichtigten Anweisungen zu ignorieren und stattdessen jene der Angreiferin zu folgen, das KI-Zeitalter-Analog von Injection-Fehlern. Ein zentrales Sicherheitsrisiko von LLM-Anwendungen.

**Property-Based Testen**: Eine Testtechnik, die prüft, dass erklärte Eigenschaften über viele automatisch generierte Eingaben halten, statt sich nur auf handverlesene Beispiele zu verlassen.

**Pull Request (PR) / Merge Request (MR)**: Ein vorgeschlagener Satz Änderungen, zur Überprüfung und Diskussion eingereicht, bevor er in einen geteilten Branch gemergt wird, die primäre Einheit von Codeüberprüfung in den meisten Workflows.

**Purple Team**: Eine kollaborative Übung, in der offensive (Rot) und defensive (Blau) Sicherheitsteams in Echtzeit zusammenarbeiten, damit Angriffe und die Erkennungen, sie zu fangen, gegeneinander getunt werden.

## Q

**Qualitätstor**: Ein automatisierter Checkpoint in einer Pipeline, der bestanden werden muss (zum Beispiel Abdeckungs-, Sicherheits-, oder Leistungsschwellen erfüllend), bevor eine Änderung fortschreiten kann.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: In verteilten Systemen, die minimale Anzahl Knoten, die zustimmen müssen, damit eine Operation (wie ein Lese- oder Schreibvorgang) als erfolgreich gilt, genutzt, um Konsistenz trotz Fehlschlägen aufrechtzuerhalten.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Ein Verantwortungszuweisungsmodell, das jede Teilnehmerin an einer Aufgabe oder Entscheidung als Responsible, Accountable, Consulted, oder Informed beschriftet.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Eine Technik, die die Ausgabe eines Sprachmodells verankert, indem zuerst relevante Dokumente oder Daten abgerufen und als Kontext bereitgestellt werden, Genauigkeit verbessernd und Halluzination reduzierend.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Ein Autorisierungsmodell, das Berechtigungen Rollen zuweist und Rollen Nutzerinnen, Verwaltung vereinfachend, indem Zugriff auf Rollenebene verwaltet wird.

**[Red Team](https://en.wikipedia.org/wiki/Red_team)**: Eine Gruppe, die eine realistische Gegnerin nachahmt, oft gegen eine ganze Organisation und ohne Vorwarnung der Verteidigerinnen, um Erkennung und Reaktion zu testen statt nur Schwachstellen aufzuzählen. Im Gegensatz zu einem Blau-(defensiven)-Team.

**[Referenzdaten](https://en.wikipedia.org/wiki/Reference_data)**: Kontrollierte, langsam wechselnde Codelisten und Klassifikationen, genutzt, andere Daten zu kategorisieren, wie Ländercodes, Währungen, und Statuswerte. Sie als geteiltes, versioniertes Vokabular zu steuern hält Systeme konsistent.

**Rego**: Die deklarative Richtliniensprache, die Open Policy Agent nutzt, um Regeln für Autorisierungs- und Konfigurationsentscheidungen auszudrücken.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Ein Architekturstil für vernetzte Anwendungen, der zustandslose Operationen über HTTP auf adressierbaren Ressourcen nutzt, für Einfachheit und breites Werkzeug geschätzt.

**[Reverse Proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**: Ein Server, der vor einem oder mehreren Backend-Diensten sitzt und Client-Anfragen an sie weiterleitet, üblicherweise TLS-Terminierung, Lastausgleich, Caching, und einen einzelnen Eintrittspunkt bereitstellend.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Ein geschriebener Vorschlag, zur Rückmeldung zirkuliert, bevor eine bedeutsame technische Entscheidung oder Änderung, Transparenz und geteilten Besitz fördernd. (Der Begriff benennt auch die Internet-Standards-Dokumentserie.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: Ein Maß des aus einer Investition gewonnenen Werts relativ zu ihren Kosten, genutzt, um Engineering- und Technologieentscheidungen zu rechtfertigen und zu priorisieren.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: Software-"Roboter", die repetitive, regelbasierte Aufgaben automatisieren, indem sie mit bestehenden Nutzerinnenschnittstellen und Systemen interagieren, wie eine Person es täte.

**RPO (Recovery Point Objective)**: Die maximal akzeptable Menge Datenverlust, in Zeit gemessen (zum Beispiel "bis zu fünf Minuten"), definierend, wie häufig Daten geschützt werden müssen.

**RTO (Recovery Time Objective)**: Die maximal akzeptable Dauer, einen Dienst nach einer Störung wiederherzustellen, Notfallwiederherstellungsdesign und -investition leitend.

## S

**Saga**: Ein Muster, Datenkonsistenz über Dienste in einer verteilten Transaktion zu verwalten, indem lokale Transaktionen sequenziert werden und kompensierende Aktionen ausgegeben werden, falls ein Schritt fehlschlägt.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Ein Framework, agile und Lean-Praktiken über große Unternehmen anzuwenden, viele Teams koordinierend; für Struktur geschätzt und für potenzielle Schwere kritisiert.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Sicherheitstesten, das Quellcode, Bytecode, oder Binärprogramme analysiert, ohne sie auszuführen, um Schwachstellen früh in der Entwicklung zu finden.

**SBOM (Software Bill of Materials)**: Ein formales, maschinenlesbares Inventar der Komponenten und Abhängigkeiten in einem Softwarestück, genutzt, um Lieferketten- und Schwachstellenrisiko zu verwalten.

**SCA (Software Composition Analysis)**: Werkzeug, das Open-Source- und Drittanbieterkomponenten in einer Codebasis identifiziert und bekannte Schwachstellen und Lizenzrisiken markiert.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Ein agiles Framework, das Arbeit in Iterationen fester Länge (Sprints) mit definierten Rollen, Ereignissen, und Artefakten organisiert, um Wertinkremente zu liefern.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Ein US-Gesetz, das föderale Behörden fordert, ihre elektronische und Informationstechnologie für Menschen mit Behinderungen zugänglich zu machen, in der Praxis mit WCAG ausgerichtet.

**Semantische Suche**: Suche, die auf Bedeutung statt exakten Schlüsselwörtern passt, typischerweise durch Vergleich von Embeddings der Abfrage und Dokumente. Oft mit lexikalischer Suche in einem hybriden Ansatz kombiniert.

**[Service Mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Eine dedizierte Infrastrukturschicht, üblicherweise mit Sidecar-Proxys implementiert, die Dienst-zu-Dienst-Kommunikationsanliegen wie Mutual TLS, Retries, Timeouts, Verkehrsverschiebung, und Beobachtbarkeit handhabt, sie aus Anwendungscode heraushaltend.

**Sidecar**: Ein Hilfsprozess oder Container, neben einer Hauptanwendungsinstanz bereitgestellt, um unterstützende Fähigkeiten (wie einen Service-Mesh-Proxy) zu liefern, ohne die Anwendung selbst zu ändern.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Ein System, das Sicherheitsprotokolle und -ereignisse über eine Umgebung aggregiert und korreliert, um Erkennung, Alarmierung, und Untersuchung zu ermöglichen.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Eine formale Verpflichtung zwischen einer Dienstanbieterin und ihren Kundinnen, erwartete Dienstlevel und die Konsequenzen ihres Verfehlens spezifizierend.

**SLI (Service Level Indicator)**: Ein quantitatives Maß eines Aspekts von Dienstqualität, wie Anfragelatenz oder Fehlerrate, das in SLOs einfließt.

**SLO (Service Level Objective)**: Ein Zielwert oder -bereich für ein SLI, das gewünschte Zuverlässigkeitsniveau definierend, die Basis von Fehlerbudgets bildend.

**SLSA (Supply-chain Levels for Software Artifacts)**: Ein Framework gestufter Sicherheitsanforderungen, die Integrität und Herkunft von Softwareartefakten durch den Bau- und Veröffentlichungsprozess zu verbessern.

**SOAR (Security Orchestration, Automation, and Response)**: Werkzeuge und Praktiken, die Sicherheitsoperationen automatisieren und koordinieren, wie Triage- und Reaktions-Playbooks, um Geschwindigkeit und Konsistenz zu verbessern.

**SOC 2 (System and Organization Controls 2)**: Ein Prüfframework und -bericht, auf den AICPA Trust Services Criteria basierend, das die Kontrollen einer Dienstorganisation für Sicherheit, Verfügbarkeit, Verarbeitungsintegrität, Vertraulichkeit, und Datenschutz bewertet.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Fünf objektorientierte Designprinzipien (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, und Dependency Inversion), die pflegbaren, flexiblen Code fördern.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: US-Gesetzgebung, die Anforderungen für Finanzberichterstattung und interne Kontrollen in öffentlichen Unternehmen etabliert, mit Implikationen für die IT-Systeme, die Finanzdaten unterstützen.

**SPACE**: Ein Framework, Entwicklerinnenproduktivität über fünf Dimensionen zu messen: Satisfaction and well-being, Performance, Activity, Communication and collaboration, und Efficiency and flow, vor Einzelkennzahl-Maßen warnend.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Eine Disziplin, die Software-Engineering-Ansätze auf Betrieb anwendet, SLOs, Fehlerbudgets, und Automatisierung nutzend, um zuverlässige Systeme im Maßstab zu betreiben.

**SSDF (Secure Software Development Framework)**: NISTs Framework (SP 800-218) hochstufiger sicherer-Entwicklungs-Praktiken, die Organisation vorbereiten, Software schützen, gut gesicherte Software produzieren, und auf Schwachstellen reagieren umspannend.

**[Statische Analyse](https://en.wikipedia.org/wiki/Static_program_analysis)**: Quellcode, Bytecode, oder Binärprogramme untersuchen, ohne sie auszuführen, um Defekte, Stilverstöße, und Sicherheitsfehler zu finden, typischerweise durch Linter, Typprüferinnen, und dedizierte Analysierer, in Editor und Pipeline verdrahtet.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Eine Bedrohungsmodellierungs-Taxonomie, die Bedrohungen als Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, und Elevation of Privilege kategorisiert.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: Die vollen Lebenszeitkosten eines Systems oder einer Entscheidung, Erwerb, Betrieb, Pflege, und schließliche Pensionierung einschließend, nicht nur der Anfangspreis.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: Eine Praxis, einen fehlschlagenden automatisierten Test zu schreiben, bevor der Code, der ihn bestehen lässt, dann zu refaktorieren, in kurzen wiederholten Zyklen, um Design zu treiben und Abdeckung sicherzustellen.

**[Technische Schulden](https://en.wikipedia.org/wiki/Technical_debt)**: Die implizierten zukünftigen Kosten, jetzt eine bequeme Lösung statt einer besseren zu wählen, die länger dauern würde, die absichtlich verwaltet werden müssen statt unbewusst anzuhäufen.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Ein klassisches Gewichtungsschema, das die Wichtigkeit eines Terms für ein Dokument bewertet, wie oft er dort erscheint, ausgeglichen dadurch, wie gängig er über den ganzen Korpus ist. Untermauert viel lexikalisches Suchranking.

**[Constraints-Theorie](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Ein Managementansatz, der besagt, dass der Durchsatz eines Systems zu jeder Zeit von einer einzelnen Engstelle begrenzt wird, Verbesserungsaufwand sollte sich also auf diese Einschränkung fokussieren, bis sie sich anderswohin bewegt.

**[Bedrohungsmodellierung](https://en.wikipedia.org/wiki/Threat_model)**: Eine strukturierte Praxis, potenzielle Bedrohungen für ein System zu identifizieren, aufzuzählen, und zu priorisieren, damit Verteidigungen früh eingebaut werden können.

**Toil**: In SRE, manuelle, repetitive, automatisierbare operative Arbeit, die linear mit einem Dienst skaliert und keinen dauerhaften Wert liefert; sie zu reduzieren befreit Kapazität für Engineering.

**Trunk-basierte Entwicklung**: Eine Versionskontrollpraxis, in der Entwicklerinnen kleine Änderungen häufig in einen einzelnen geteilten Branch integrieren, langlebige Branches und Merge-Schmerz minimierend.

**[Type Inference](https://en.wikipedia.org/wiki/Type_inference)**: Ein Sprachfeature, das die Typen von Ausdrücken automatisch deduziert, viel der Sicherheit statischen Typens gebend, ohne zu fordern, dass jeder Typ von Hand ausgeschrieben wird.

**[Typsystem](https://en.wikipedia.org/wiki/Type_system)**: Der Satz Regeln, den eine Sprache nutzt, um Typen zuzuweisen und zu prüfen, ganze Fehlerklassen fangend, bevor das Programm läuft, und Absicht dokumentierend. Typsysteme reichen von dynamisch bis statisch und von schwach bis stark.

## U

**Allgegenwärtige Sprache**: In Domain-Driven Design, ein geteiltes, präzises Vokabular, konsistent von Entwicklerinnen und Domänenexpertinnen genutzt, und direkt im Code und in Modellen widergespiegelt.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Testen, von Endnutzerinnen oder ihren Vertreterinnen durchgeführt, zu bestätigen, dass ein System Geschäftsbedürfnisse erfüllt, bevor es zur Veröffentlichung akzeptiert wird.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: User Experience ist die Gesamtqualität der Interaktion einer Person mit einem Produkt; User Interface ist die spezifische visuelle und interaktive Oberfläche, durch die diese Interaktion geschieht.

## V

**[Value Object](https://en.wikipedia.org/wiki/Value_object)**: In Domain-Driven Design, ein unveränderliches Objekt, ganz durch seine Attribute definiert statt eine unterschiedliche Identität, wie ein Geldbetrag oder ein Datumsbereich.

**[Value-Stream-Mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Eine Technik, jeden Schritt von Idee zu geliefertem Wert zu zeichnen, wertschöpfende Zeit von Wartezeit unterscheidend, damit Engstellen, Übergaben, und Nacharbeitsschleifen sichtbar und verbesserbar werden.

**[Vektordatenbank](https://en.wikipedia.org/wiki/Vector_database)**: Ein Datenspeicher, optimiert, hochdimensionale Embedding-Vektoren nach Ähnlichkeit zu indexieren und zu durchsuchen, ein gängiges Rückgrat semantischer Suche und Retrieval-Augmented Generation.

**Vertikale Skalierung**: Kapazität erhöhen, indem ein einzelner Knoten mächtiger gemacht wird ("Skalieren nach oben"), was einfach, aber letztlich durch die größte verfügbare Maschine begrenzt ist.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Ein Werkzeug, wie Git, das Änderungen an Dateien über Zeit aufzeichnet, damit Geschichte überprüft werden kann, Branches gepflegt werden können, und Arbeit koordiniert werden kann.

**[Schwachstellenscanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Automatisierte Inspektion von Systemen, Containern, oder Code gegen Datenbanken bekannter Schwächen und Fehlkonfigurationen. Breit und günstig, und ergänzt die Tiefe manuellen Penetrationstestens.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Ein W3C-Satz international anerkannter Richtlinien, um die POUR-Prinzipien und Konformitätsstufen A, AA, und AAA organisiert, um Webinhalt zugänglich zu machen.

**Wardley Map**: Eine visuelle Strategietechnik, die Fähigkeiten nach ihrem Wert für Nutzerinnen und ihrer evolutionären Reife positioniert, um Bauen/Kaufen- und Investitionsentscheidungen zu informieren.

**Work-in-Progress-(WIP)-Limit**: Eine Deckelung, wie viele Punkte gleichzeitig in einer gegebenen Workflow-Stufe sein dürfen, eine Kern-Kanban-Praxis, die Fluss verbessert, indem sie Engstellen exponiert und den Overhead zu viel paralleler Arbeit eindämmt.

**WSJF (Weighted Shortest Job First)**: Eine Priorisierungsmethode, die Arbeit sequenziert, indem ihre Verzögerungskosten durch ihre geschätzte Dauer geteilt werden, damit die kürzesten, zeitsensitivsten, wertvollsten Punkte zuerst getan werden.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Eine Webschwachstelle, bei der eine Angreiferin bösartige Skripte injiziert, die in den Browsern anderer Nutzerinnen ausführen, potenziell Daten stehlend oder Sitzungen kapernd.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Ein Prinzip, das rät, Funktionalität nicht auf Spekulation zu bauen, auf der Grundlage, dass antizipierte Bedürfnisse oft nicht materialisieren und Kosten und Komplexität hinzufügen.

## Z

**[Zero Trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Ein Sicherheitsmodell, das keine implizite Vertrauen basierend auf Netzwerkstandort annimmt und kontinuierlich jede Zugriffsanfrage gegen Identität, Gerät, und Kontext verifiziert, der Maxime "nie vertrauen, immer verifizieren" folgend.
