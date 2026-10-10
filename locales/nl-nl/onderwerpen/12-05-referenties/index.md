# 12.5 Referenties

Dit onderdeel bundelt het referentieapparaat van het handboek: een vergelijking met de
SWEBOK-kennisbasis, een index van de standaarden en kaders die overal worden aangehaald,
en een samengestelde bibliografie van aanbevolen literatuur. Bronnen per hoofdstuk staan
ook in de sectie *Referenties en verder lezen* aan het eind van elk hoofdstuk.

---

# SWEBOK-vergelijking

Dit handboek sluit aan op **SWEBOK V4.0** (Software Engineering Body of Knowledge) van de
IEEE Computer Society. Alle 18 kennisgebieden worden gedekt. De tabel koppelt elk gebied
aan de hoofdstukken die het behandelen, en het handboek gaat daarna ruim voorbij SWEBOK
naar AI, data, UX, DevOps, duurzaamheid, flow en technologie voor het publiek belang.

| SWEBOK V4.0-kennisgebied | Primaire hoofdstukken |
|---|---|
| 1. Software Requirements | 2.8, 11.1, 5.1 |
| 2. Software Architecture | 3.1, 3.2, 3.3 |
| 3. Software Design | 2.2, 3.1 |
| 4. Software Construction | 2.9, 2.1 |
| 5. Software Testing | 2.4, 8.5 |
| 6. Software Engineering Operations | 9.1, 9.2, 9.3, 8.1 |
| 7. Software Maintenance | 3.7, 3.6, 10.4 |
| 8. Software Configuration Management | 2.10, 2.6, 8.2 |
| 9. Software Engineering Management | 10.1, 10.6, 10.2 |
| 10. Software Engineering Process | 1.4, 10.7, 10.8 |
| 11. Software Engineering Models and Methods | 2.12, 3.1, 2.2 |
| 12. Software Quality | 2.11, 2.4, 3.1 |
| 13. Software Security | 4.1, 4.2, 4.3, 4.4 |
| 14. Software Engineering Professional Practice | 10.5, 1.1, 1.3 |
| 15. Software Engineering Economics | 10.10, 10.1, 9.4 |
| 16. Computing Foundations | 2.13, 3.3, 3.4 |
| 17. Mathematical Foundations | 2.13, 11.3 |
| 18. Engineering Foundations | 2.13, 3.1 |

---

# Standaarden en kaders

Deze bijlage is een geordende index van de echte standaarden, kaders en regelgeving
waarnaar het handboek verwijst. Het is een navigatiehulp, geen compliancehandboek:
raadpleeg altijd de gezaghebbende bron en, waar relevant, gekwalificeerde juridische of
auditadviseurs voor de actuele tekst en de toepasbaarheid op jouw context.

Vermeldingen zijn gegroepeerd per domein. Elke vermelding noemt de standaard of het kader,
de uitgevende instantie, een omschrijving van één regel en de hoofdstukken of domeinen
waar het het meest relevant is. Waar een naam gewoonlijk wordt afgekort, staat de afkorting
erbij. Documentnummers en titels worden alleen gegeven waar ze goed ingeburgerd zijn. Er
staan geen URL's in.

## Hoe je deze bijlage gebruikt

- **Regelgeving** (bijvoorbeeld AVG/GDPR, HIPAA) is juridisch bindend binnen haar
  rechtsgebied en sector. Ze stelt verplichtingen, niet alleen goede praktijk.
- **Standaarden** (bijvoorbeeld ISO/IEC 27001, WCAG) zijn formele, vaak certificeerbare
  specificaties. Sommige zijn vrijwillig, andere worden bij wet of contract verplicht.
- **Kaders** (bijvoorbeeld NIST CSF, NIST AI RMF) zijn gestructureerde, doorgaans
  vrijwillige richtlijnen die je op je risicoprofiel afstemt.
- Toepasbaarheid hangt af van rechtsgebied, sector, soorten data en contractvoorwaarden.
  Veel organisaties moeten aan meerdere tegelijk voldoen.

## Beveiliging en privacy

| Standaard / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Eisen voor een managementsysteem voor informatiebeveiliging (ISMS). | 4.1–4.6 Beveiliging en compliance |
| ISO/IEC 27002 | ISO / IEC | Richtlijnen en maatregelenset ter ondersteuning van ISO/IEC 27001. | 4.1–4.4 Beveiliging |
| ISO/IEC 27017 / 27018 | ISO / IEC | Cloudspecifieke beveiligingsmaatregelen (27017) en bescherming van persoonsgegevens in de cloud (27018). | 4.3 Infrastructuur- en cloudbeveiliging; 4.5 Privacy |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Vrijwillig kader georganiseerd rond Govern, Identify, Protect, Detect, Respond, Recover. | 4.1, 4.4 Beveiligingsfundamenten en -operaties |
| NIST SP 800-53 | National Institute of Standards and Technology | Catalogus van beveiligings- en privacymaatregelen voor informatiesystemen. | 4.3, 4.6 Cloudbeveiliging en compliance |
| NIST SP 800-63 | National Institute of Standards and Technology | Richtlijnen voor digitale identiteit en zekerheid over authenticatie. | 4.2, 4.3 Applicatie- en infrastructuurbeveiliging |
| OWASP Top Ten | Open Worldwide Application Security Project | De meest kritieke beveiligingsrisico's van webapplicaties, periodiek bijgewerkt. | 4.2 Applicatiebeveiliging |
| OWASP ASVS | Open Worldwide Application Security Project | Gegradeerde eisen en tests voor het verifiëren van applicatiebeveiliging. | 2.4, 4.2 Testen en applicatiebeveiliging |
| OWASP SAMM | Open Worldwide Application Security Project | Volwassenheidsmodel voor het opbouwen en beoordelen van een softwarebeveiligingsprogramma. | 4.1 Beveiligingsfundamenten en cultuur |
| STRIDE | Afkomstig van Microsoft | Taxonomie voor dreigingsmodellering om dreigingen te classificeren. | 4.2 Applicatiebeveiliging |
| MITRE ATT&CK | MITRE | Kennisbank van tactieken en technieken van tegenstanders voor detectie en verdediging. | 4.4 Beveiligingsoperaties |
| SLSA | Open Source Security Foundation (OpenSSF) | Gegradeerd kader voor integriteit en herkomst van de softwaretoeleveringsketen. | 4.2, 8.1, 10.3 Toeleveringsketen en oplevering |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Standaardformaten voor software bills of materials. | 4.2, 10.3 Applicatiebeveiliging en licenties |
| PCI DSS | PCI Security Standards Council | Beveiligingseisen voor het verwerken van betaalkaartgegevens. | 4.2, 4.5, 4.6 Beveiliging, privacy, compliance |

## Compliance en overheid

### Verenigde Staten

| Regelgeving / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Waarborgen voor beschermde gezondheidsinformatie (PHI). | 4.5, 4.6 Privacy en compliance |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Eisen voor financiële verslaggeving en interne beheersing bij beursgenoteerde bedrijven. | 4.6, 10.2 Compliance en audit |
| FISMA | US Congress | Eisen aan informatiebeveiligingsprogramma's van federale instanties. | 4.3, 4.6 Cloudbeveiliging en compliance |
| FedRAMP | US General Services Administration / FedRAMP PMO | Gestandaardiseerde beveiligingsautorisatie voor clouddiensten van federale instanties. | 4.3, 4.6 Cloudbeveiliging en compliance |
| NIST SP 800-171 | National Institute of Standards and Technology | Bescherming van controlled unclassified information (CUI) in niet-federale systemen. | 4.6 Compliance (defensieketen) |
| CMMC | US Department of Defence | Certificering van cyberbeveiligingsvolwassenheid van defensieaannemers. | 4.6 Compliance (defensie) |
| FIPS 140-3 | National Institute of Standards and Technology | Beveiligingseisen voor cryptografische modules. | 4.3 Infrastructuur- en cloudbeveiliging |
| CCPA / CPRA | State of California | Privacyrechten van consumenten en verplichtingen van bedrijven in Californië. | 4.5 Privacy en gegevensbescherming |

### Europese Unie en Verenigd Koninkrijk

| Regelgeving / standaard | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| GDPR (AVG) | Europese Unie | Uitgebreide verordening over de verwerking van persoonsgegevens. | 4.5, 4.6 Privacy en compliance |
| UK GDPR / Data Protection Act 2018 | Verenigd Koninkrijk | Het gegevensbeschermingsregime van het VK na de Brexit. | 4.5, 4.6 Privacy en compliance |
| eIDAS | Europese Unie | Kader voor elektronische identificatie en vertrouwensdiensten. | 4.2, 4.3 Beveiliging |
| NIS2-richtlijn | Europese Unie | Cyberbeveiligingsverplichtingen voor essentiële en belangrijke entiteiten. | 4.4, 4.6 Beveiligingsoperaties en compliance |
| DORA (Digital Operational Resilience Act) | Europese Unie | Eisen aan operationele weerbaarheid voor de financiële sector. | 9.1, 10.2 Betrouwbaarheid en audit |
| EU AI Act | Europese Unie | Risicogebaseerde regelgeving voor AI-systemen (zie AI-governance hieronder). | 6.1, 6.5 AI-strategie en verantwoorde AI |

## Toegankelijkheid

| Standaard | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Richtlijnen voor toegankelijke webcontent, met conformiteitsniveaus A/AA/AAA. | 5.3 Toegankelijkheid; 5.1–5.6 UX en frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Rollen, toestanden en eigenschappen voor toegankelijke rijke internettoepassingen. | 5.3, 5.6 Toegankelijkheid en frontend |
| Section 508 | US Access Board / Amerikaanse federale wet | Toegankelijkheidseisen voor Amerikaanse federale ICT, afgestemd op WCAG. | 5.3 Toegankelijkheid (Amerikaanse overheid) |
| EN 301 549 | ETSI / CEN / CENELEC | Europese toegankelijkheidseisen voor ICT-inkoop, afgestemd op WCAG. | 5.3 Toegankelijkheid (Europese publieke sector) |
| ADA (Americans with Disabilities Act) | US Congress | Burgerrechtenwet die discriminatie op grond van een beperking verbiedt, toegepast op digitale diensten. | 5.3 Toegankelijkheid |
| ISO/IEC 40500 | ISO / IEC | Internationale overname van WCAG 2.0 als formele standaard. | 5.3 Toegankelijkheid |

## AI-governance

| Kader / regelgeving | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Vrijwillig kader om AI-risico te besturen, in kaart te brengen, te meten en te beheersen. | 6.1, 6.5 AI-strategie en verantwoorde AI |
| ISO/IEC 42001 | ISO / IEC | Eisen voor een managementsysteem voor AI (AIMS). | 6.1, 6.5 AI-governance |
| ISO/IEC 23894 | ISO / IEC | Richtlijnen voor AI-specifiek risicomanagement. | 6.5 Verantwoorde en betrouwbare AI |
| EU AI Act | Europese Unie | Wettelijke verplichtingen in risiconiveaus voor aanbieders en gebruikers van AI-systemen. | 6.1, 6.3, 6.5 AI-toepassingen en governance |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Op waarden gebaseerde principes voor betrouwbare AI, invloedrijk voor beleid. | 6.5, 10.5 Verantwoorde AI en ethiek |

## Kwaliteit en proces

| Standaard / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Kwaliteitsmodel voor softwareproducten (functionele geschiktheid, betrouwbaarheid, beveiliging enz.). | 2.2, 2.4 Ontwerp en testen |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Levenscyclusprocessen van software. | 1.4, 10.1 Werkwijzen en programmamanagement |
| ISO 9001 | ISO | Eisen aan een algemeen kwaliteitsmanagementsysteem. | 10.2 Risico, audit en assurance |
| CMMI | ISACA / CMMI Institute | Volwassenheidsmodel voor procesvermogen en verbetering. | 10.1, 10.2 Programmamanagement en assurance |
| DORA-statistieken | DevOps Research and Assessment (Google Cloud) | Vier kernstatistieken voor leveringsprestaties van softwareteams. | 8.1, 8.4, 9.1 Oplevering, platform, betrouwbaarheid |
| SPACE-kader | Onderzoekers van Microsoft / GitHub | Multidimensionaal model om de productiviteit van ontwikkelaars te meten. | 1.3, 8.4 Groei en ontwikkelaarservaring |
| ITIL | AXELOS / PeopleCert | Kader van praktijken voor IT-servicemanagement. | 9.1, 9.3 Betrouwbaarheid en incidentmanagement |

## Architectuur

| Standaard / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Standaard voor architectuurbeschrijving en gezichtspunten. | 2.7, 3.1 Documentatie en architectuurfundamenten |
| TOGAF | The Open Group | Enterprise-architectuurkader en ontwikkelmethode. | 3.1, 10.1 Architectuur en portfoliomanagement |
| C4-model | Gemeenschap (Simon Brown) | Aanpak in vier niveaus om softwarearchitectuur te visualiseren. | 2.7, 3.1 Documentatie en architectuur |
| arc42 | Gemeenschap (Starke / Hruschka) | Sjabloon voor het structureren van architectuurdocumentatie. | 2.7, 3.1 Documentatie en architectuur |
| ADR's | Gemeenschapspraktijk | Lichtgewicht records van belangrijke architectuurbeslissingen. | 1.5, 2.7, 3.1 Besluitvorming en documentatie |

## Cloud en DevOps

| Standaard / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | Op consensus gebaseerde basislijnen voor veilige configuratie van systemen en cloud. | 4.3, 8.2 Infrastructuurbeveiliging en IaC |
| CNCF-landschap en -projecten | Cloud Native Computing Foundation | Ecosysteem en standaarden voor cloudnative computing (bijv. Kubernetes). | 8.3 Containers en cloudnative |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Open standaarden voor containerimage- en runtimeformaten. | 8.3 Containers en cloudnative |
| OpenTelemetry | Cloud Native Computing Foundation | Leveranciersneutrale standaard voor telemetrie (traces, statistieken, logs). | 9.2 Observeerbaarheid en bewaking |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Beleidsengine voor algemeen gebruik voor policy as code. | 4.6, 8.2, 8.3 Compliance, IaC, orkestratie |
| SRE-praktijken | Google (breed overgenomen) | Aanpak op basis van SLI/SLO/foutbudget om betrouwbare diensten te beheren. | 9.1 Site reliability engineering |
| FinOps Framework | FinOps Foundation | Praktijken voor financieel beheer van de cloud en kostenverantwoording. | 9.4 Kosten, duurzaamheid, groene software |

## Data

| Standaard / kader | Uitgevende instantie | Reikwijdte (één regel) | Primaire hoofdstukken / domeinen |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Kennisbasis die de disciplines van databeheer ordent. | 7.1 Datastrategie en datagovernance |
| ISO/IEC 38505 | ISO / IEC | Governance van data als organisatiebezit. | 7.1 Datagovernance |
| ISO 8000 | ISO | Standaarden voor datakwaliteit en stamdata. | 7.1, 7.2 Datagovernance en data-engineering |
| Data mesh | Gemeenschap (Zhamak Dehghani) | Gedecentraliseerde, domeingeoriënteerde aanpak van data als product. | 7.1, 7.2 Datastrategie en data-engineering |
| DCAM | EDM Council | Beoordelingsmodel voor databeheervermogen. | 7.1 Datastrategie en datagovernance |

## Opmerkingen over reikwijdte en verandering

Standaarden en regelgeving evolueren. Versienummers (bijvoorbeeld WCAG 2.1 tegenover
2.2, of revisiejaren van ISO) en maatregelencatalogi veranderen in de loop van de tijd, en
nieuwe wetten (zoals sectorspecifieke regelgeving voor AI en weerbaarheid) blijven
verschijnen. Behandel deze bijlage als een beginkaart: bevestig de actuele versie, het
rechtsgebied en de toepasbaarheid voordat je op een vermelding vertrouwt voor een
compliance- of inkoopbeslissing. Waar de hoofdstukken van het handboek en deze bijlage in
detail verschillen, geldt altijd het gezaghebbende brondocument.


---

# Aanbevolen literatuur

Deze bijlage is een samengestelde, geannoteerde leeslijst over alle domeinen van het
handboek. Ze geeft de voorkeur aan werken die de praktijk op schaal hebben gevormd:
erkende klassiekers, degelijke naslagwerken en de standaarden en rapporten waaraan grote
teams, ondernemingen en overheden worden afgemeten.

Elke vermelding geeft de titel en de auteur(s), gevolgd door één zin over waarom het ertoe
doet. De lijst is geordend onder de tien delen van het boek. Lees selectief: kies de twee
of drie werken die het dichtst bij je huidige pijn liggen, niet de hele plank. Waar een
werk meerdere domeinen beslaat, staat het waar het het nuttigst is. Veel horen in meerdere
delen thuis.

Een opmerking over standaarden: instanties zoals NIST, OWASP, W3C/WCAG, ISO en het
DORA-programma publiceren levende documenten die periodiek worden herzien. Citeer en lees
de actuele versie. De annotaties hieronder beschrijven hun blijvende doel.

## Fundamenten: cultuur, mensen en proces

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Het onderzoeksfundament dat toont dat leveringsprestaties organisatieprestaties voorspellen, en de statistieken definieert (nu DORA genoemd) om ze te meten.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Een bedrijfsroman die flow, werk in uitvoering en de "Three Ways" van DevOps invoelbaar maakt voor leiders en sceptici.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. Een praktisch vocabulaire (stroomgerichte, platform-, ondersteunende en complicated-subsystemteams) om organisaties te ontwerpen die goede software voortbrengen.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. In de praktijk beproefde kaders voor het dimensioneren van teams, het beheren van organisatiegroei en de terugkerende beslissingen van engineeringleiderschap.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Definieert de staff-plusarchetypen en het technische leiderschapspad voor wie impact wil zonder manager te worden.
- **The Manager's Path**. Camille Fournier. Een gids per fase van tech lead tot directie die loopbaanladders verankert en de overgang naar management begeleidt.
- **The Staff Engineer's Path**. Tanya Reilly. Een aanvulling op de staff-pluslitteratuur gericht op het dagelijkse werk van technisch leiderschap, invloed en sturen zonder gezag.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. Het blijvende betoog dat de kernproblemen van software sociologisch zijn, niet technisch.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. De oorsprong van de wet van Brooks en het onderscheid tussen essentiële en toevallige complexiteit dat bemanning en planning nog steeds bepaalt.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Het onderzoeksfundament voor schuldvrije cultuur en de veiligheid die leren van falen mogelijk maakt.
- **Thinking, Fast and Slow**. Daniel Kahneman. Het toonaangevende verslag van cognitieve vooroordelen, essentieel voor gestructureerde interviews, kalibratie en eerlijke besluitvorming.

## Programmeervak en codekwaliteit

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. De fundamentele catalogus van professionele gewoonten (DRY, orthogonaliteit, tracer bullets) die bepaalt wat vakmanschap betekent.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. De canonieke catalogus van gedragsbehoudende transformaties en de discipline van continue, door tests gedekte codeverbetering.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Een breed gebruikte (en omstreden) standaard voor naamgeving, functies en leesbaarheid die de reviewverwachtingen van veel teams vormt.
- **Code Complete**. Steve McConnell. Een uitgebreid, op bewijs gebaseerd handboek van bouwpraktijken dat een grondige basislijn voor programmeerkwaliteit blijft.
- **Test-Driven Development: By Example**. Kent Beck. De oorspronkelijke, praktische introductie van de red-green-refactorcyclus en test-eerstontwerp.
- **Working Effectively with Legacy Code**. Michael Feathers. De toonaangevende gereedschapskist om tests toe te voegen aan code die ze niet heeft en die veilig te wijzigen, onmisbaar voor langlevende systemen.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. Een uitgewerkte demonstratie van outside-in TDD, mocking en het laten evolueren van een ontwerp via tests.
- **A Philosophy of Software Design**. John Ousterhout. Een scherpe, uuitgesproken behandeling van complexiteit, diepe modules en informatieverberging die enige "clean code"-orthodoxie productief uitdaagt.

## Architectuur en systemen

- **Designing Data-Intensive Applications**. Martin Kleppmann. Het beste moderne naslagwerk over de afwegingen van opslag, replicatie, partitionering, consistentie en streamverwerking op schaal.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. Een brede, actuele verkenning van architectuurstijlen, kenmerken en de rol en besluitvorming van de architect.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Een beslissingsgerichte behandeling van afwegingen in gedistribueerde architectuur, servicegranulariteit en data-eigenaarschap.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Introduceert fitnessfuncties en architectuur die ontworpen is om in de loop van de tijd veilig te veranderen.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. De oorsprong van afgebakende contexten, ubiquitous language en aggregates: het vocabulaire van modern servicontwerp.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Het naslagwerk voor decompositie, servicegrenzen, deployment en de organisatorische gevolgen van microservices.
- **Monolith to Microservices**. Sam Newman. Een patroncatalogus voor incrementele decompositie, zoals strangler fig en branch by abstraction, zonder riskante big-bangherschrijving.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Het naslagwerk met benoemde patronen (repository, unit of work en meer) dat enterprisesystemen een gedeelde taal gaf.
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. De toonaangevende catalogus van berichtenpatronen onder gebeurtenisgedreven en asynchrone architecturen.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. De bron van de circuit breaker, de bulkhead en andere stabiliteitspatronen voor systemen die echte productie overleven.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). De historisch bepalende catalogus van objectgeoriënteerde patronen en een gedeeld ontwerpvocabulaire.

## Beveiliging, privacy en vertrouwen

- **Threat Modelling: Designing for Security**. Adam Shostack. De praktische, uitgebreide gids voor STRIDE en gestructureerde dreigingsmodellering als routinematige engineeringpraktijk.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Het encyclopedische naslagwerk over hoe echte systemen falen en hoe je er bouwt die aanvallen weerstaan.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Een nauwgezette rondleiding door het beveiligingsmodel van de browser en de subtiele manieren waarop webplatformen naïeve aannames verraden.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Een gids voor de praktijk om cryptografie correct te gebruiken en de gangbare, gevaarlijke fouten te vermijden.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Googles synthese van beveiliging en betrouwbaarheid als verweven eigenschappen die vanaf het begin worden ingebouwd.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. Een heldere behandeling van de principes en werking van een netwerkarchitectuur die nooit vertrouwt en altijd verifieert.
- **OWASP Top 10**. OWASP Foundation. De consensusbasislijn van de meest kritieke beveiligingsrisico's van webapplicaties, wereldwijd aangehaald door beleid en audit.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Een gelaagde, toetsbare checklist van beveiligingseisen, geschikt voor contracten en acceptatiecriteria.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. De maatregelencatalogus in het hart van Amerikaanse federale beveiliging en de basis voor FedRAMP- en FISMA-autorisatie.
- **NIST Cybersecurity Framework (CSF)**. NIST. De veelgebruikte structuur identificeren-beschermen-detecteren-reageren-herstellen om een beveiligingsprogramma te organiseren.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. De referentiedefinitie en referentiearchitecturen die de meeste zero-trustprogramma's van ondernemingen en overheden verankeren.

## UX, UI en productontwerp

- **The Design of Everyday Things**. Don Norman. De fundamentele tekst over affordances, signifiers, feedback en mensgericht ontwerp die veel verder reikt dan fysieke objecten.
- **Don't Make Me Think, Revisited**. Steve Krug. Het beknopte, blijvende pleidooi voor vanzelfsprekende bruikbaarheid en de waarde van goedkope, frequente usabilitytests.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Het uitgebreide naslagwerk over interactieontwerp, persona's en doelgericht ontwerp.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Een onderbouwd verslag van het bouwen van consistente, herbruikbare componentsystemen en de gedeelde taal erachter.
- **Refactoring UI**. Adam Wathan and Steve Schoger. Een praktische, voorbeeldgedreven gids voor visuele verfijning voor engineers die interfaces ontwerpen zonder formele opleiding.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. De toonaangevende gids voor contentontwerp in gewone taal en gericht op taken.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Praktische metgezellen voor het bouwen van interfaces die werken voor het volledige spectrum van menselijke mogelijkheden.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. Een op principes gebaseerde brug tussen toegankelijkheidsstandaarden en goede gebruikerservaring.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. De internationaal aangehaalde standaard (waarneembaar, bedienbaar, begrijpelijk, robuust) achter de meeste toegankelijkheidswetgeving.
- **U.S. Web Design System (USWDS)**. U.S. government. Een werkend voorbeeld van een toegankelijk, op standaarden gebaseerd designsysteem gebouwd voor publieke diensten op schaal.

## Kunstmatige intelligentie en machine learning

- **Designing Machine Learning Systems**. Chip Huyen. De toonaangevende praktische gids voor het bouwen van ML-systemen in productie van begin tot eind: data, features, deployment en bewaking.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Breidt de SRE-discipline (SLO's, bewaking, incidentrespons) uit naar machine-learningsystemen.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Het academische standaardwerk over de theorie en methoden onder moderne neurale netwerken.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Een actuele gids voor het ontwerpen, evalueren en beheren van toepassingen op basis van grote foundationmodellen.
- **Weapons of Maths Destruction**. Cathy O'Neil. Een levendig pleidooi voor algoritmische verantwoording en de reële schade van niet-onderzochte modellen, essentieel voor AI in de publieke sector.
- **Interpretable Machine Learning**. Christoph Molnar. Een uitgebreid, vrij beschikbaar naslagwerk over uitlegmethoden voor modellen en hun voorspellingen.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Het referentiekader om AI-risico te besturen, in kaart te brengen, te meten en te beheersen, steeds vaker aangehaald in beleid en inkoop.

## Data, analytics en inzicht

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball and Margy Ross. Het canonieke naslagwerk over sterschema's en dimensioneel modelleren voor analytics.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. De gezaghebbende gids voor experimenten die op schaal betrouwbare, bruikbare resultaten opleveren.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. Een leveranciersneutrale kaart van de moderne datalevenscyclus en de engineeringpraktijken erachter.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. De grondlegger van de domeingeoriënteerde, productgerichte aanpak om data op schaal te organiseren.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Een praktische gids voor eerlijke, heldere datavisualisatie en het overbrengen van inzicht aan beslissers.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Het fundamentele werk over grafische integriteit, data-ink en de ethiek van het eerlijk tonen van data.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Het uitgebreide referentiekader voor datagovernance, stewardship, kwaliteit en catalogisering.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. Een leesbare introductie in causale inferentie, essentieel om van correlatie naar verdedigbare beslissingen te komen.

## Automatisering, DevOps en platformengineering

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Het uitgebreide draaiboek dat de "Three Ways" vertaalt naar concrete praktijken voor flow, feedback en voortdurend leren.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. De fundamentele tekst over deploymentpijplijnen, automatisering en software veilig en vaak uitbrengen.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Het naslagwerk over infrastructuur behandelen als software: modules, testen, onveranderlijkheid en drift.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (Zie Fundamenten.) Ook hier essentieel voor het vormgeven van platformteams en de ontwikkelaarservaring die ze bieden.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Een catalogus van herbruikbare patronen voor het ontwerpen van cloudnative applicaties op Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Hoe engineeringpraktijken als testen, review, tooling en afhankelijkheidsbeheer over tientallen jaren schalen naar tienduizenden engineers.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Het beknopte, invloedrijke manifest voor het bouwen van draagbare, schaalbare, cloudnative diensten.
- **DORA State of DevOps Report**. DORA / Google Cloud (jaarlijks). Het doorlopende onderzoeksprogramma achter de vier kernstatistieken voor oplevering en de vermogens die prestaties aandrijven.

## Beheer, betrouwbaarheid en observeerbaarheid

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). De fundamentele tekst die SLI's, SLO's, foutbudgetten en de discipline van betrouwbaarheidsengineering definieert.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). De praktische aanvulling met voorbeelden, uitgewerkte SLO's en implementatierichtlijnen.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. De moderne definitie van observeerbaarheid, data met hoge kardinaliteit en het debuggen van onbekende onbekenden in productie.
- **Implementing Service Level Objectives**. Alex Hidalgo. Een grondige, praktische gids voor het goed ontwerpen, meten en gebruiken van SLO's en foutbudgetten.
- **Release It!**. Michael T. Nygard. (Zie Architectuur.) Ook hier fundamenteel voor stabiliteitspatronen in productie en het beheren van veerkrachtige systemen.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. Een datagedreven aanpak om vraag te voorspellen en capaciteit te plannen voor groeiende systemen.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. De toonaangevende behandeling van het bewust injecteren van falen om vertrouwen in de weerbaarheid van een systeem op te bouwen.
- **Google SRE Book, Chapter on Postmortems**. Google. Het veel nagevolgde model voor schuldvrije nabeschouwingen en leren van incidenten.

## Onderneming, overheid en het publiek belang

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. De essentiële studie van hoe open source werkelijk in stand wordt gehouden, en de last van onderhouders achter de afhankelijkheden waarop ondernemingen leunen.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Een nuchter verslag van waarom technologie in de publieke sector faalt en hoe op oplevering gerichte hervorming dat kan verhelpen.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lessen van de Britse Government Digital Service over het transformeren van publieke diensten door op te leveren in plaats van te plannen.
- **Project to Product**. Mik Kersten. Het Flow Framework om grote ondernemingen te verschuiven van projectgebaseerde financiering naar duurzame productwaardestromen.
- **Escaping the Build Trap**. Melissa Perri. Hoe organisaties output voor uitkomst aanzien, en hoe productmanagement dat herstelt, met directe relevantie voor portfolio- en programmagovernance.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Een beknopte set spelregels voor het opleveren van effectieve, gebruikersgerichte digitale overheidsdiensten.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Een werkende, gepubliceerde standaard voor het bouwen van goede publieke diensten, door andere overheden veel nagevolgd.
- **NIST SP 800-37: Risk Management Framework**. NIST. Het procesraamwerk achter authorisation to operate (ATO) en continue bewaking in Amerikaanse federale systemen.
- **The FinOps Foundation Framework**. FinOps Foundation. Het referentiemodel voor kostenzicht, optimalisatie en verantwoording in de cloud, over financiën en engineering heen.

## Hoe je deze lijst gebruikt

- **Begin bij je pijn.** Als deployments traag en eng zijn, lees dan *Accelerate*, *Continuous Delivery* en de *DORA*-rapporten voor al het andere.
- **Lees voor het decennium, niet voor de sprint.** Geef de voorkeur aan werken die blijvende principes uitleggen boven werken die aan een specifieke toolversie hangen.
- **Controleer de actuele editie van standaarden.** NIST, OWASP, WCAG, ISO en DORA herzien hun publicaties. Werk altijd vanuit de laatste release en noteer de versie in je eigen beleid.
- **Bouw een gedeelde plank.** Een team dat twee of drie van deze boeken gemeenschappelijk heeft gelezen, discussieert minder en beslist sneller, omdat het een vocabulaire en een set referentiepunten deelt.
- **Zie ook hoofdstuk 12.5** voor de volledige index van referentiestandaarden en -kaders, en **hoofdstuk 12.6** voor hoe je de invoering van de praktijken uit deze werken in volgorde zet.
