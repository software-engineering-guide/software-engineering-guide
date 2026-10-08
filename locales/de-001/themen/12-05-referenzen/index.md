# 12.5 Referenzen

Dieser Abschnitt konsolidiert den Referenzapparat des Handbuchs: eine Gegenüberstellung
mit dem SWEBOK-Wissenskorpus, einen Index der durchgehend zitierten Standards und
Frameworks, und eine kuratierte Bibliografie empfohlener Lektüre. Kapitelspezifische
Quellen erscheinen auch im Abschnitt *Referenzen und weiterführende Literatur* am Ende
jedes Kapitels.

---

# SWEBOK-Gegenüberstellung

Dieses Handbuch ist mit dem **SWEBOK V4.0** (Software Engineering Body of Knowledge)
der IEEE Computer Society ausgerichtet. Alle 18 Wissensgebiete sind abgedeckt; die
Tabelle bildet jedes auf die Kapitel ab, die es behandeln, und das Handbuch geht dann
weit über SWEBOK hinaus in KI, Daten, UX, DevOps, Nachhaltigkeit, Fluss, und
Technologie im öffentlichen Interesse.

| SWEBOK-V4.0-Wissensgebiet | Primäre Kapitel |
|---|---|
| 1. Softwareanforderungen | 2.8, 11.1, 5.1 |
| 2. Softwarearchitektur | 3.1, 3.2, 3.3 |
| 3. Softwaredesign | 2.2, 3.1 |
| 4. Softwarekonstruktion | 2.9, 2.1 |
| 5. Softwaretesten | 2.4, 8.5 |
| 6. Software-Engineering-Betrieb | 9.1, 9.2, 9.3, 8.1 |
| 7. Softwarewartung | 3.7, 3.6, 10.4 |
| 8. Software-Konfigurationsmanagement | 2.10, 2.6, 8.2 |
| 9. Software-Engineering-Management | 10.1, 10.6, 10.2 |
| 10. Software-Engineering-Prozess | 1.4, 10.7, 10.8 |
| 11. Software-Engineering-Modelle und -Methoden | 2.12, 3.1, 2.2 |
| 12. Softwarequalität | 2.11, 2.4, 3.1 |
| 13. Softwaresicherheit | 4.1, 4.2, 4.3, 4.4 |
| 14. Software-Engineering-Berufspraxis | 10.5, 1.1, 1.3 |
| 15. Software-Engineering-Ökonomie | 10.10, 10.1, 9.4 |
| 16. Computing-Grundlagen | 2.13, 3.3, 3.4 |
| 17. Mathematische Grundlagen | 2.13, 11.3 |
| 18. Engineering-Grundlagen | 2.13, 3.1 |

---

# Standards und Frameworks

Dieser Anhang ist ein organisierter Index der echten Standards, Frameworks, und
Regulierungen, die durchgehend im Handbuch referenziert werden. Er ist eine
Navigationshilfe, kein Compliance-Handbuch: konsultieren Sie immer die maßgebliche
Quelle und, wo relevant, qualifizierten rechtlichen oder Prüfungsrat für den aktuellen
Text und die Anwendbarkeit auf Ihren Kontext.

Einträge sind nach Domäne gruppiert. Jeder benennt den Standard oder das Framework,
seine ausstellende Stelle, einen einzeiligen Umfang, und die Kapitel oder Domänen, in
denen er am relevantesten ist. Wo ein Name üblicherweise abgekürzt wird, wird die
Abkürzung gezeigt. Dokumentnummern und Titel werden nur gegeben, wo sie gut etabliert
sind; keine URLs sind eingeschlossen.

## Wie dieser Anhang zu nutzen ist

- **Regulierungen** (zum Beispiel DSGVO, HIPAA) sind innerhalb ihrer Jurisdiktion
  und ihres Sektors rechtlich bindend. Sie setzen Verpflichtungen, nicht nur gute
  Praxis.
- **Standards** (zum Beispiel ISO/IEC 27001, WCAG) sind formelle, oft
  zertifizierbare Spezifikationen. Manche sind freiwillig; manche sind gesetzlich
  oder vertraglich vorgeschrieben.
- **Frameworks** (zum Beispiel NIST CSF, NIST AI RMF) sind strukturierte,
  üblicherweise freiwillige Anleitung, die Sie an Ihr Risikoprofil anpassen.
- Anwendbarkeit hängt von Jurisdiktion, Sektor, Datentypen, und Vertragsbedingungen
  ab. Viele Organisationen müssen mehrere davon gleichzeitig erfüllen.

## Sicherheit und Datenschutz

| Standard / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Anforderungen für ein Informationssicherheitsmanagementsystem (ISMS). | 4.1–4.6 Sicherheit und Compliance |
| ISO/IEC 27002 | ISO / IEC | Anleitung und Kontrollsatz, der ISO/IEC 27001 unterstützt. | 4.1–4.4 Sicherheit |
| ISO/IEC 27017 / 27018 | ISO / IEC | Cloud-spezifische Sicherheitskontrollen (27017) und Schutz persönlicher Daten in der Cloud (27018). | 4.3 Infrastruktur- und Cloud-Sicherheit; 4.5 Datenschutz |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Freiwilliges Framework, um Govern, Identify, Protect, Detect, Respond, Recover organisiert. | 4.1, 4.4 Sicherheitsgrundlagen und -betrieb |
| NIST SP 800-53 | National Institute of Standards and Technology | Katalog von Sicherheits- und Datenschutzkontrollen für Informationssysteme. | 4.3, 4.6 Cloud-Sicherheit und Compliance |
| NIST SP 800-63 | National Institute of Standards and Technology | Richtlinien für digitale Identität und Authentifizierungssicherheit. | 4.2, 4.3 Anwendungs- und Infrastruktursicherheit |
| OWASP Top Ten | Open Worldwide Application Security Project | Die kritischsten Webanwendungssicherheitsrisiken, periodisch aktualisiert. | 4.2 Anwendungssicherheit |
| OWASP ASVS | Open Worldwide Application Security Project | Gestufte Anforderungen und Tests zur Verifikation von Anwendungssicherheit. | 2.4, 4.2 Testen und Anwendungssicherheit |
| OWASP SAMM | Open Worldwide Application Security Project | Reifegradmodell zum Bauen und Bewerten eines Softwaresicherheitsprogramms. | 4.1 Sicherheitsgrundlagen und -kultur |
| STRIDE | Entstanden bei Microsoft | Bedrohungsmodellierungs-Taxonomie zur Klassifikation von Bedrohungen. | 4.2 Anwendungssicherheit |
| MITRE ATT&CK | MITRE | Wissensbasis von Gegnerinnentaktiken und -techniken für Erkennung und Verteidigung. | 4.4 Sicherheitsoperationen |
| SLSA | Open Source Security Foundation (OpenSSF) | Gestuftes Framework für Softwarelieferketten-Integrität und -Herkunft. | 4.2, 8.1, 10.3 Lieferkette und Lieferung |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Standardformate für Software Bills of Materials. | 4.2, 10.3 Anwendungssicherheit und Lizenzierung |
| PCI DSS | PCI Security Standards Council | Sicherheitsanforderungen für die Handhabung von Zahlungskartendaten. | 4.2, 4.5, 4.6 Sicherheit, Datenschutz, Compliance |

## Compliance und Behörden

### Vereinigte Staaten

| Regulierung / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| HIPAA | US-Gesundheitsministerium | Sicherungsmaßnahmen für geschützte Gesundheitsinformation (PHI). | 4.5, 4.6 Datenschutz und Compliance |
| SOX (Sarbanes-Oxley Act) | US-Kongress / SEC | Finanzberichterstattungs- und interne-Kontroll-Anforderungen für öffentliche Unternehmen. | 4.6, 10.2 Compliance und Audit |
| FISMA | US-Kongress | Informationssicherheitsprogrammanforderungen für föderale Behörden. | 4.3, 4.6 Cloud-Sicherheit und Compliance |
| FedRAMP | US General Services Administration / FedRAMP PMO | Standardisierte Sicherheitsautorisierung für von föderalen Behörden genutzte Cloud-Dienste. | 4.3, 4.6 Cloud-Sicherheit und Compliance |
| NIST SP 800-171 | National Institute of Standards and Technology | Schutz kontrollierter unklassifizierter Information (CUI) in nicht-föderalen Systemen. | 4.6 Compliance (Verteidigungslieferkette) |
| CMMC | US-Verteidigungsministerium | Zertifizierung der Cybersicherheitsreife von Verteidigungsauftragnehmerinnen. | 4.6 Compliance (Verteidigung) |
| FIPS 140-3 | National Institute of Standards and Technology | Sicherheitsanforderungen für kryptografische Module. | 4.3 Infrastruktur- und Cloud-Sicherheit |
| CCPA / CPRA | Bundesstaat Kalifornien | Verbraucherdatenschutzrechte und Geschäftsverpflichtungen in Kalifornien. | 4.5 Datenschutz |

### Europäische Union und Vereinigtes Königreich

| Regulierung / Standard | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| DSGVO | Europäische Union | Umfassende Regulierung der Verarbeitung persönlicher Daten. | 4.5, 4.6 Datenschutz und Compliance |
| UK GDPR / Data Protection Act 2018 | Vereinigtes Königreich | Das Post-Brexit-Datenschutzregime des Vereinigten Königreichs. | 4.5, 4.6 Datenschutz und Compliance |
| eIDAS | Europäische Union | Framework für elektronische Identifizierung und Vertrauensdienste. | 4.2, 4.3 Sicherheit |
| NIS2-Richtlinie | Europäische Union | Cybersicherheitsverpflichtungen für wesentliche und wichtige Einrichtungen. | 4.4, 4.6 Sicherheitsoperationen und Compliance |
| DORA (Digital Operational Resilience Act) | Europäische Union | Operative-Resilienz-Anforderungen für den Finanzsektor. | 9.1, 10.2 Zuverlässigkeit und Audit |
| EU AI Act | Europäische Union | Risikobasierte Regulierung von KI-Systemen (siehe KI-Governance unten). | 6.1, 6.5 KI-Strategie und verantwortungsvolle KI |

## Barrierefreiheit

| Standard | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Richtlinien für barrierefreien Webinhalt, mit A/AA/AAA-Konformitätsstufen. | 5.3 Barrierefreiheit; 5.1–5.6 UX und Frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Rollen, Zustände, und Eigenschaften für barrierefreie Rich Internet Applications. | 5.3, 5.6 Barrierefreiheit und Frontend |
| Section 508 | US Access Board / US-Bundesgesetz | Barrierefreiheitsanforderungen für US-Bundes-ICT, mit WCAG ausgerichtet. | 5.3 Barrierefreiheit (US-Regierung) |
| EN 301 549 | ETSI / CEN / CENELEC | Europäische Barrierefreiheitsanforderungen für ICT-Beschaffung, mit WCAG ausgerichtet. | 5.3 Barrierefreiheit (EU-öffentlicher Sektor) |
| ADA (Americans with Disabilities Act) | US-Kongress | Bürgerrechtsgesetz, das Behindertendiskriminierung verbietet, auf digitale Dienste angewandt. | 5.3 Barrierefreiheit |
| ISO/IEC 40500 | ISO / IEC | Internationale Übernahme von WCAG 2.0 als formeller Standard. | 5.3 Barrierefreiheit |

## KI-Governance

| Framework / Regulierung | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Freiwilliges Framework, KI-Risiko zu steuern, abzubilden, zu messen, und zu verwalten. | 6.1, 6.5 KI-Strategie und verantwortungsvolle KI |
| ISO/IEC 42001 | ISO / IEC | Anforderungen für ein KI-Managementsystem (AIMS). | 6.1, 6.5 KI-Governance |
| ISO/IEC 23894 | ISO / IEC | Anleitung zu KI-spezifischem Risikomanagement. | 6.5 Verantwortungsvolle und vertrauenswürdige KI |
| EU AI Act | Europäische Union | Risikogestufte rechtliche Verpflichtungen für Anbieterinnen und Betreiberinnen von KI-Systemen. | 6.1, 6.3, 6.5 KI-Anwendungen und -Governance |
| OECD-KI-Prinzipien | Organisation für wirtschaftliche Zusammenarbeit und Entwicklung | Wertebasierte Prinzipien für vertrauenswürdige KI, politikeinflussreich. | 6.5, 10.5 Verantwortungsvolle KI und Ethik |

## Qualität und Prozess

| Standard / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Softwareproduktqualitätsmodell (funktionale Eignung, Zuverlässigkeit, Sicherheit, usw.). | 2.2, 2.4 Design und Testen |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Software-Lebenszyklusprozesse. | 1.4, 10.1 Arbeitsweisen und Programmmanagement |
| ISO 9001 | ISO | Anforderungen für ein allgemeines Qualitätsmanagementsystem. | 10.2 Risiko, Audit, und Zusicherung |
| CMMI | ISACA / CMMI Institute | Reifegradmodell für Prozessfähigkeit und -verbesserung. | 10.1, 10.2 Programmmanagement und Zusicherung |
| DORA-Metriken | DevOps Research and Assessment (Google Cloud) | Vier Schlüsselliefer-Leistungsmetriken für Softwareteams. | 8.1, 8.4, 9.1 Lieferung, Plattform, Zuverlässigkeit |
| SPACE-Framework | Microsoft / GitHub-Forscherinnen | Mehrdimensionales Modell zum Messen von Entwicklerinnenproduktivität. | 1.3, 8.4 Wachstum und Entwicklerinnenerfahrung |
| ITIL | AXELOS / PeopleCert | Framework von IT-Service-Management-Praktiken. | 9.1, 9.3 Zuverlässigkeit und Vorfallmanagement |

## Architektur

| Standard / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Standard für Architekturbeschreibung und Sichtweisen. | 2.7, 3.1 Dokumentation und Architekturgrundlagen |
| TOGAF | The Open Group | Unternehmensarchitektur-Framework und Entwicklungsmethode. | 3.1, 10.1 Architektur- und Portfoliomanagement |
| C4-Modell | Community (Simon Brown) | Vier-Ebenen-Ansatz zur Visualisierung von Softwarearchitektur. | 2.7, 3.1 Dokumentation und Architektur |
| arc42 | Community (Starke / Hruschka) | Vorlage zur Strukturierung von Architekturdokumentation. | 2.7, 3.1 Dokumentation und Architektur |
| ADRs | Community-Praxis | Leichtgewichtige Aufzeichnungen bedeutsamer Architekturentscheidungen. | 1.5, 2.7, 3.1 Entscheidungsfindung und Dokumentation |

## Cloud und DevOps

| Standard / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Konsensbasierte sichere-Konfigurations-Baselines für Systeme und Cloud. | 4.3, 8.2 Infrastruktursicherheit und IaC |
| CNCF-Landschaft und -Projekte | Cloud Native Computing Foundation | Ökosystem und Standards für Cloud-Native-Computing (z. B. Kubernetes). | 8.3 Container und Cloud-Native |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Offene Standards für Container-Image- und Laufzeitformate. | 8.3 Container und Cloud-Native |
| OpenTelemetry | Cloud Native Computing Foundation | Herstellerneutraler Standard für Telemetrie (Traces, Metriken, Protokolle). | 9.2 Beobachtbarkeit und Überwachung |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Allgemeiner Richtlinienmotor für Policy as Code. | 4.6, 8.2, 8.3 Compliance, IaC, Orchestrierung |
| SRE-Praktiken | Google (weit übernommen) | SLI/SLO/Fehlerbudget-basierter Ansatz zum Betrieb zuverlässiger Dienste. | 9.1 Site Reliability Engineering |
| FinOps Framework | FinOps Foundation | Praktiken für Cloud-Finanzmanagement und Kostenrechenschaftspflicht. | 9.4 Kosten, Nachhaltigkeit, grüne Software |

## Daten

| Standard / Framework | Ausstellende Stelle | Umfang (eine Zeile) | Primäre Kapitel / Domänen |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Wissenskorpus, der Datenmanagement-Disziplinen organisiert. | 7.1 Datenstrategie und -Governance |
| ISO/IEC 38505 | ISO / IEC | Governance von Daten als organisatorischer Vermögenswert. | 7.1 Daten-Governance |
| ISO 8000 | ISO | Datenqualitäts- und Stammdaten-Standards. | 7.1, 7.2 Daten-Governance und -Engineering |
| Data Mesh | Community (Zhamak Dehghani) | Dezentralisierter, domänenorientierter Ansatz zu Daten als Produkt. | 7.1, 7.2 Datenstrategie und -Engineering |
| DCAM | EDM Council | Datenmanagement-Fähigkeitsbewertungsmodell. | 7.1 Datenstrategie und -Governance |

## Notizen zu Umfang und Änderung

Standards und Regulierungen entwickeln sich. Versionsnummern (zum Beispiel WCAG 2.1
versus 2.2, oder ISO-Revisionsjahre) und Kontrollkataloge ändern sich über Zeit, und
neue Gesetze (wie sektorspezifische KI- und Resilienz-Regulierungen) entstehen
weiterhin. Behandeln Sie diesen Anhang als Startkarte: bestätigen Sie die aktuelle
Version, Jurisdiktion, und Anwendbarkeit, bevor Sie sich für eine Compliance- oder
Beschaffungsentscheidung auf einen Eintrag verlassen. Wo sich die Handbuchkapitel und
dieser Anhang im Detail unterscheiden, gilt immer das maßgebliche Quelldokument.


---

# Empfohlene Lektüre

Dieser Anhang ist eine kuratierte, kommentierte Leseliste, die jede Domäne des
Handbuchs umspannt. Sie bevorzugt Werke, die Praxis im großen Maßstab geformt haben:
anerkannte Klassiker, rigorose Referenzen, und die Standards und Berichte, an denen
große, Unternehmens-, und Behördenteams gemessen werden.

Jeder Eintrag gibt Titel und Autorin(nen), gefolgt von einem Satz, warum er wichtig
ist. Die Liste ist unter den zehn Teilen des Buches organisiert. Lesen Sie selektiv:
wählen Sie die zwei oder drei Werke, die Ihrem aktuellen Schmerz am nächsten sind,
nicht das ganze Regal. Wo ein Werk Domänen überspannt, ist es dort platziert, wo es
am nützlichsten ist; viele gehören in mehrere Teile.

Eine Notiz zu Standards: Stellen wie NIST, OWASP, W3C/WCAG, ISO, und das DORA-Programm
veröffentlichen lebendige Dokumente, die periodisch revidiert werden. Zitieren und
lesen Sie die aktuelle Version; die Anmerkungen unten beschreiben ihren dauerhaften
Zweck.

## Grundlagen: Kultur, Menschen, und Prozess

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Die Forschungsgrundlage, die zeigt, dass Lieferleistung organisatorische Leistung vorhersagt, und die Metriken (jetzt DORA genannt) definiert, sie zu messen.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Ein Business-Roman, der Fluss, Work in Progress, und die "Drei Wege" von DevOps für Führungskräfte und Skeptikerinnen gleichermaßen intuitiv macht.
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**. Matthew Skelton und Manuel Pais. Ein praktisches Vokabular (stream-ausgerichtete, Plattform-, ermöglichende, und komplizierte-Subsystem-Teams) zum Entwerfen von Organisationen, die gute Software produzieren.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Feldgetestete Frameworks für Teamgrößen, Verwalten organisatorischen Wachstums, und Treffen der wiederkehrenden Entscheidungen von Engineering-Führung.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Definiert die Staff-Plus-Archetypen und den technischen Führungspfad für jene, die Wirkung wollen, ohne Managerinnen zu werden.
- **The Manager's Path**. Camille Fournier. Ein stufenweiser Leitfaden von Tech Lead zu Führungskraft, der Karriereleitern und den Übergang ins Management verankert.
- **The Staff Engineer's Path**. Tanya Reilly. Ein Begleiter zur Staff-Plus-Literatur, fokussiert auf die tägliche Arbeit technischer Führung, Einfluss, und Steuern ohne Autorität.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco und Timothy Lister. Das dauerhafte Argument, dass die zentralen Probleme von Software soziologisch sind, nicht technisch.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. Der Ursprung von Brooks' Gesetz und der essenziell-versus-akzidentell-Komplexität-Unterscheidung, die noch immer Personalplanung und Terminierung steuert.
- **The Fearless Organization: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Die Forschungsgrundlage für schuldfreie Kultur und die Sicherheit, die Lernen aus Fehlschlag möglich macht.
- **Thinking, Fast and Slow**. Daniel Kahneman. Die maßgebliche Darstellung kognitiver Verzerrung, wesentlich für strukturierte Interviews, Kalibrierung, und ehrliche Entscheidungsfindung.

## Programmierhandwerk und Codequalität

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt und David Thomas. Der grundlegende Katalog professioneller Gewohnheiten (DRY, Orthogonalität, Tracer Bullets), der definiert, was Handwerkskunst bedeutet.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Der kanonische Katalog verhaltenserhaltender Transformationen und die Disziplin kontinuierlicher, testgestützter Codeverbesserung.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Ein weit genutzter (und diskutierter) Standard für Benennung, Funktionen, und Lesbarkeit, der die Überprüfungserwartungen vieler Teams formt.
- **Code Complete**. Steve McConnell. Ein umfassendes, evidenzreferenziertes Handbuch von Konstruktionspraktiken, das eine gründliche Baseline für Programmierqualität bleibt.
- **Test-Driven Development: By Example**. Kent Beck. Die ursprüngliche, praktische Einführung in den Rot-Grün-Refaktorieren-Zyklus und testerstes Design.
- **Working Effectively with Legacy Code**. Michael Feathers. Das maßgebliche Werkzeugset zum Hinzufügen von Tests zu und sicheren Ändern von Code, der keine hat, und unentbehrlich für langlebige Systeme.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman und Nat Pryce. Eine durchgearbeitete Demonstration von Outside-in-TDD, Mocking, und der Entwicklung eines Designs durch Tests.
- **A Philosophy of Software Design**. John Ousterhout. Eine scharfe, meinungsstarke Behandlung von Komplexität, tiefen Modulen, und Informationsverbergung, die manche "Clean Code"-Orthodoxie produktiv herausfordert.

## Architektur und Systeme

- **Designing Data-Intensive Applications**. Martin Kleppmann. Die einzelne beste moderne Referenz zu den Abwägungen von Speicher, Replikation, Partitionierung, Konsistenz, und Stream-Verarbeitung im Maßstab.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards und Neal Ford. Eine breite, aktuelle Übersicht über Architekturstile, Eigenschaften, und die Rolle und Entscheidungsfindung der Architektin.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Eine entscheidungsfokussierte Behandlung verteilter Architekturabwägungen, Dienstgranularität, und Datenbesitz.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Führt Fitness-Funktionen und Architektur ein, die entworfen ist, sich sicher über Zeit zu ändern.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. Der Ursprung von Bounded Contexts, allgegenwärtiger Sprache, und Aggregaten: das Vokabular modernen Dienstdesigns.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Die Referenz für Dekomposition, Dienstgrenzen, Bereitstellung, und die organisatorischen Implikationen von Microservices.
- **Monolith to Microservices**. Sam Newman. Ein Musterkatalog für inkrementelle Dekomposition, wie Strangler Fig und Branch by Abstraction, ohne ein riskantes Big-Bang-Neuschreiben.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Die benannte-Muster-Referenz (Repository, Unit of Work, und mehr), die Unternehmenssystemen eine geteilte Sprache gab.
- **Enterprise Integration Patterns**. Gregor Hohpe und Bobby Woolf. Der maßgebliche Katalog von Messaging-Mustern, die ereignisgetriebene und asynchrone Architekturen untermauern.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. Die Quelle des Circuit Breaker, Bulkhead, und anderer Stabilitätsmuster für Systeme, die echte Produktion überleben.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Der historisch entscheidende Katalog objektorientierter Muster und eine geteilte Designsprache.

## Sicherheit, Datenschutz, und Vertrauen

- **Threat Modeling: Designing for Security**. Adam Shostack. Der praktische, umfassende Leitfaden zu STRIDE und strukturierter Bedrohungsmodellierung als routinierte Engineering-Praxis.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Die enzyklopädische Referenz dazu, wie echte Systeme fehlschlagen und wie man solche baut, die Angriffen widerstehen.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Eine rigorose Tour durch das Browser-Sicherheitsmodell und die subtilen Weisen, in denen Webplattformen naive Annahmen verraten.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Ein Praktikerinnenleitfaden zur korrekten Nutzung von Kryptografie und Vermeidung der gängigen, gefährlichen Fehler.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Googles Synthese von Sicherheit und Zuverlässigkeit als von Anfang an eingebaute, verflochtene Eigenschaften.
- **Zero Trust Networks**. Evan Gilman und Doug Barth. Eine klare Behandlung der Prinzipien und Mechanik von Nie-vertrauen-immer-verifizieren-Netzwerkarchitektur.
- **OWASP Top 10**. OWASP Foundation. Die Konsens-Baseline der kritischsten Webanwendungssicherheitsrisiken, weltweit von Richtlinie und Audit referenziert.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Eine gestufte, testbare Checkliste von Sicherheitsanforderungen, geeignet für Verträge und Abnahmekriterien.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**. NIST. Der Kontrollkatalog im Herzen der US-Bundessicherheit und die Grundlage für FedRAMP- und FISMA-Autorisierung.
- **NIST Cybersecurity Framework (CSF)**. NIST. Die weit übernommene Identify-Protect-Detect-Respond-Recover-Struktur zur Organisation eines Sicherheitsprogramms.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. Die Referenzdefinition und Referenzarchitekturen, die die meisten Unternehmens- und Behörden-Zero-Trust-Programme verankern.

## UX, UI, und Produktdesign

- **The Design of Everyday Things**. Don Norman. Der grundlegende Text zu Affordanzen, Signifikatoren, Feedback, und menschzentriertem Design, der weit über physische Objekte hinaus anwendbar ist.
- **Don't Make Me Think, Revisited**. Steve Krug. Das prägnante, dauerhafte Argument für selbstevidente Nutzbarkeit und den Wert günstiger, häufiger Nutzbarkeitstests.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Die umfassende Referenz zu Interaktionsdesign, Personas, und zielgerichtetem Design.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Eine fundierte Darstellung zum Bauen konsistenter, wiederverwendbarer Komponentensysteme und der geteilten Sprache dahinter.
- **Refactoring UI**. Adam Wathan und Steve Schoger. Ein praktischer, beispielgetriebener Leitfaden zu visuellem Schliff für Ingenieurinnen, die Schnittstellen ohne formelles Training gestalten.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Der maßgebliche Leitfaden zu klarsprachigem, aufgabenfokussiertem Content-Design.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Praktische Begleiter zum Bauen von Schnittstellen, die für die volle Bandbreite menschlicher Fähigkeiten funktionieren.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton und Whitney Quesenbery. Eine prinzipiengetriebene Brücke zwischen Barrierefreiheitsstandards und guter Nutzerinnenerfahrung.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Der international referenzierte Standard (wahrnehmbar, bedienbar, verständlich, robust) hinter den meisten Barrierefreiheitsgesetzen.
- **U.S. Web Design System (USWDS)**. US-Regierung. Ein funktionierendes Beispiel eines barrierefreien, standardbasierten Designsystems, gebaut für öffentliche Dienste im Maßstab.

## Künstliche Intelligenz und Machine Learning

- **Designing Machine Learning Systems**. Chip Huyen. Der führende praktische Leitfaden zum Bauen von Produktions-ML-Systemen Ende zu Ende: Daten, Features, Bereitstellung, und Überwachung.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Erweitert SRE-Disziplin (SLOs, Überwachung, Vorfallreaktion) auf Machine-Learning-Systeme.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Die Standard-akademische Referenz zur Theorie und den Methoden hinter modernen neuronalen Netzwerken.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Ein aktueller Leitfaden zum Entwerfen, Evaluieren, und Betreiben von Anwendungen, die auf großen Foundation Models gebaut sind.
- **Weapons of Math Destruction**. Cathy O'Neil. Ein lebhaftes Argument für algorithmische Rechenschaftspflicht und die echtweltlichen Schäden unexaminierter Modelle, wesentlich für KI im öffentlichen Sektor.
- **Interpretable Machine Learning**. Christoph Molnar. Eine umfassende, frei verfügbare Referenz zu Erklärbarkeitsmethoden für Modelle und ihre Vorhersagen.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Das Referenzframework zum Steuern, Abbilden, Messen, und Verwalten von KI-Risiko, zunehmend in Richtlinie und Beschaffung zitiert.

## Daten, Analytik, und Einsicht

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. Ralph Kimball und Margy Ross. Die kanonische Referenz zu Sternschemata und dimensionaler Modellierung für Analytik.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Der maßgebliche Leitfaden zum Durchführen von Experimenten, die verlässliche, handlungsfähige Ergebnisse im Maßstab liefern.
- **Fundamentals of Data Engineering**. Joe Reis und Matt Housley. Eine herstellerneutrale Karte des modernen Datenlebenszyklus und der Engineering-Praktiken dahinter.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Der Gründungstext des domänenorientierten, produktzentrierten Ansatzes, Daten im Maßstab zu organisieren.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Ein praktischer Leitfaden zu ehrlicher, klarer Datenvisualisierung und dem Kommunizieren von Einsicht an Entscheidungsträgerinnen.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Das grundlegende Werk zu grafischer Integrität, Daten-Tinte, und der Ethik ehrlicher Datenpräsentation.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Das umfassende Referenzframework für Daten-Governance, Stewardship, Qualität, und Katalogisierung.
- **The Book of Why**. Judea Pearl und Dana Mackenzie. Eine lesbare Einführung in kausale Inferenz, wesentlich für den Übergang von Korrelation zu verteidigbaren Entscheidungen.

## Automatisierung, DevOps, und Plattform-Engineering

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Das umfassende Playbook, das die "Drei Wege" in konkrete Praktiken für Fluss, Feedback, und kontinuierliches Lernen übersetzt.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble und David Farley. Der grundlegende Text zu Bereitstellungspipelines, Automatisierung, und sicherem, häufigem Softwareveröffentlichen.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Die Referenz zur Behandlung von Infrastruktur als Software: Module, Testen, Unveränderlichkeit, und Drift.
- **Team Topologies**. Matthew Skelton und Manuel Pais. (Siehe Grundlagen.) Auch hier wesentlich für das Formen von Plattformteams und der Entwicklerinnenerfahrung, die sie bieten.
- **Kubernetes Patterns**. Bilgin Ibryam und Roland Huß. Ein Katalog wiederverwendbarer Muster zum Entwerfen Cloud-nativer Anwendungen auf Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Wie Engineering-Praktiken wie Testen, Überprüfung, Werkzeug, und Abhängigkeitsmanagement über Jahrzehnte auf zehntausende Ingenieurinnen skalieren.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Das prägnante, einflussreiche Manifest zum Bauen portabler, skalierbarer, Cloud-nativer Dienste.
- **DORA State of DevOps Report**. DORA / Google Cloud (jährlich). Das laufende Forschungsprogramm hinter den vier Schlüsselliefer-Metriken und den Fähigkeiten, die Leistung treiben.

## Betrieb, Zuverlässigkeit, und Beobachtbarkeit

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (Hrsg.). Der grundlegende Text, der SLIs, SLOs, Fehlerbudgets, und die Disziplin des Engineering von Zuverlässigkeit definiert.
- **The Site Reliability Workbook**. Betsy Beyer et al. (Hrsg.). Der praktische Begleiter mit praktischen Beispielen, durchgearbeiteten SLOs, und Implementierungsanleitung.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. Die moderne Definition von Beobachtbarkeit, hochkardinalen Daten, und Debugging unbekannter Unbekannter in Produktion.
- **Implementing Service Level Objectives**. Alex Hidalgo. Ein gründlicher, praktischer Leitfaden zum guten Entwerfen, Messen, und Nutzen von SLOs und Fehlerbudgets.
- **Release It!**. Michael T. Nygard. (Siehe Architektur.) Auch hier grundlegend für Produktionsstabilitätsmuster und den Betrieb resilienter Systeme.
- **The Art of Capacity Planning**. Arun Kejariwal und John Allspaw. Ein datengetriebener Ansatz zum Prognostizieren von Nachfrage und Planen von Kapazität für wachsende Systeme.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal und Nora Jones. Die maßgebliche Behandlung des absichtlichen Injizierens von Fehlschlag, um Vertrauen in Systemresilienz aufzubauen.
- **Google SRE Book, Chapter on Postmortems**. Google. Das weit nachgeahmte Modell für schuldfreie Postmortems und das Lernen aus Vorfällen.

## Unternehmen, Behörden, und öffentliches Interesse

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Die wesentliche Studie dazu, wie Open Source tatsächlich getragen wird, und die Pflegelast hinter den Abhängigkeiten, auf die sich Unternehmen verlassen.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Eine klarsichtige Darstellung, warum Technologie im öffentlichen Sektor fehlschlägt und wie liefer-fokussierte Reform sie beheben kann.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lektionen vom UK Government Digital Service zur Transformation öffentlicher Dienste durch Liefern, nicht Planen.
- **Project to Product**. Mik Kersten. Das Flow Framework zum Verschieben großer Unternehmen von projektbasierter Finanzierung zu dauerhaften Produktwertströmen.
- **Escaping the Build Trap**. Melissa Perri. Wie Organisationen Ausgabe mit Ergebnis verwechseln, und wie Produktmanagement es behebt, mit direkter Relevanz für Portfolio- und Programm-Governance.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Ein prägnanter Satz Spielzüge zum Liefern effektiver, nutzerinnenzentrierter Regierungsdigitaldienste.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Ein funktionierender, veröffentlichter Standard zum Bauen guter öffentlicher Dienste, weit von anderen Regierungen nachgeahmt.
- **NIST SP 800-37: Risk Management Framework**. NIST. Das Prozessframework hinter Authorization to Operate (ATO) und kontinuierlicher Überwachung in US-Bundessystemen.
- **The FinOps Foundation Framework**. FinOps Foundation. Das Referenzmodell für Cloud-Kostentransparenz, -Optimierung, und -Rechenschaftspflicht über Finanz und Engineering.

## Wie diese Liste zu nutzen ist

- **Beginnen Sie bei Ihrem Schmerz.** Falls Bereitstellungen langsam und beängstigend sind, lesen Sie *Accelerate*, *Continuous Delivery*, und die *DORA*-Berichte vor allem anderen.
- **Lesen Sie für das Jahrzehnt, nicht den Sprint.** Bevorzugen Sie Werke, die dauerhafte Prinzipien erklären, über solche, die an eine spezifische Werkzeugversion gebunden sind.
- **Verifizieren Sie die aktuelle Ausgabe von Standards.** NIST, OWASP, WCAG, ISO, und DORA revidieren ihre Veröffentlichungen; arbeiten Sie immer von der neuesten Ausgabe und notieren Sie die Version in Ihren eigenen Richtlinien.
- **Bauen Sie ein geteiltes Regal.** Ein Team, das zwei oder drei dieser Bücher gemeinsam gelesen hat, streitet weniger und entscheidet schneller, weil es ein Vokabular und einen Satz Referenzpunkte teilt.
- **Siehe auch Kapitel 12.5** für den vollen Index von Referenzstandards und Frameworks, und **Kapitel 12.6** dafür, wie die Übernahme der von diesen Werken beschriebenen Praktiken zu sequenzieren ist.
