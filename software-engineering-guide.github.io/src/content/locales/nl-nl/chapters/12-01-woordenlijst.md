# 12.1 Woordenlijst

Deze woordenlijst definieert termen en afkortingen die door het hele handboek
worden gebruikt. De vermeldingen zijn alfabetisch gegroepeerd op de Engelse
trefwoorden, die je tegenkomt in tools en documentatie. Nederlandse
equivalenten staan tussen haakjes waar een gevestigd equivalent bestaat. Waar
een vermelding een gangbare afkorting heeft, staat die tussen haakjes. De
definities zijn bewust beknopt. Raadpleeg het betreffende hoofdstuk voor een
uitgebreidere behandeling.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)** (op attributen gebaseerde toegangscontrole): Een autorisatiemodel dat toegang verleent op basis van geëvalueerde attributen van de gebruiker, resource, handeling en omgeving (bijvoorbeeld afdeling, machtigingsniveau, tijdstip van de dag) in plaats van vaste rollen. Het biedt fijnmazige, beleidsgedreven controle ten koste van meer complexiteit dan RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)** (toegankelijkheid): De praktijk van software zo ontwerpen en bouwen dat mensen met een beperking haar kunnen waarnemen, begrijpen, doorlopen en gebruiken. Het numeroniem "a11y" verkort de 11 letters tussen "a" en "y."

**ADR (Architecture Decision Record)** (architectuurbeslissingsrecord): Een kort, versiebeheerd document dat één significante architecturale of technische beslissing vastlegt, met haar context, de overwogen opties en haar gevolgen. ADR's creëren een duurzame, controleerbare geschiedenis van waarom een systeem is zoals het is.

**Aggregate** (aggregaat): In Domain-Driven Design een cluster domeinobjecten dat als één eenheid wordt behandeld voor datawijzigingen, waarbij één entiteit als aggregaatwortel fungeert en invarianten afdwingt. Aggregaten definiëren consistentie- en transactiegrenzen.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)** (applicatieprogrammeerinterface): Een gedefinieerd contract waarlangs het ene stuk software diensten of data van een ander opvraagt. Goed ontworpen API's verbergen implementatiedetails en bieden stabiele, versiebeheerde interfaces.

**API-first**: Een ontwikkelaanpak waarin het API-contract wordt ontworpen en overeengekomen vóór de implementatie, zodat afnemers en aanbieders parallel tegen een gedeelde specificatie kunnen werken.

**arc42**: Een open, sjabloongebaseerde structuur voor het documenteren van softwarearchitectuur, georganiseerd in twaalf secties die context, beperkingen, bouwstenen, runtime, deployment en beslissingen dekken.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Een W3C-specificatie die rollen, toestanden en eigenschappen definieert die dynamische en aangepaste webcomponenten begrijpelijk maken voor hulptechnologieën zoals schermlezers.

**ASR (Architecturally Significant Requirement)** (architectonisch significante eis): Een eis met een meetbaar, verreikend effect op de architectuur, zoals een prestatie-, beschikbaarheids-, beveiligings- of regelgevende beperking. ASR's drijven de meest ingrijpende ontwerpbeslissingen.

**ASVS (Application Security Verification Standard)**: Een OWASP-standaard die een gegradeerde checklist biedt van beveiligingseisen en tests voor het ontwerpen, bouwen en verifiëren van veilige applicaties.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**: De automatische aanpassing van het aantal draaiende rekeninstanties (of hun omvang) als reactie op belasting, zodat capaciteit de vraag volgt zonder handmatige ingreep. Het vult bewuste capaciteitsplanning aan, maar vervangt haar niet.

**[Availability](https://en.wikipedia.org/wiki/Availability)** (beschikbaarheid): Het deel van de tijd dat een systeem operationeel is en verzoeken kan bedienen, vaak uitgedrukt in "negens" (bijvoorbeeld 99,9%). Het is een kernbetrouwbaarheidsdoel vastgelegd in SLO's en SLA's.

## B

**Backpressure** (tegendruk): Een flowcontrolemechanisme waarin een component onder belasting stroomopwaartse producenten signaleert te vertragen, wat onbegrensde wachtrijen en cascaderend falen voorkomt. Het is centraal voor betrouwbare streaming- en berichtgedreven systemen.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)** (gedragsgedreven ontwikkeling): Een samenwerkingspraktijk die eisen uitdrukt als concrete, voor mensen leesbare voorbeelden van gedrag (vaak in Given/When/Then-vorm) die tegelijk als geautomatiseerde acceptatietests dienen.

**BFF (Backend for Frontend)**: Een architectuurpatroon waarin een speciale backendservice wordt gebouwd voor een specifiek frontend- of clienttype, die datavorming en aggregatie afstemt op de behoeften van die client.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: De tools, processen en praktijken voor het verzamelen, integreren en analyseren van bedrijfsdata ter ondersteuning van rapportage, dashboards en besluitvorming.

**Blameless postmortem** (schuldvrije nabeschouwing): Een incidentreview die zich richt op systemische oorzaken en leren in plaats van individuele schuld, uitgaande van de premisse dat mensen redelijk handelen gegeven de informatie en prikkels die ze hadden.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Een releasestrategie die twee identieke productieomgevingen ("blauw" en "groen") draait, verkeer naar de ene stuurt terwijl de andere wordt bijgewerkt, wat bijna directe omschakeling en rollback mogelijk maakt.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Een veelgebruikte rangschikkingsfunctie voor zoeken in volledige tekst die scoort hoe goed een document bij een zoekopdracht past met termfrequentie, omgekeerde documentfrequentie en documentlengte. Het is de lexicale-rangschikkingsstandaard in veel zoekmachines.

**Bounded context** (afgebakende context): In Domain-Driven Design een expliciete grens waarbinnen een bepaald domeinmodel en zijn ubiquitous language consistent gelden. Het voorkomt dat concepten over verschillende delen van een groot systeem worden verward.

**Build cache**: Een opslag van eerder berekende builduitvoer, gesleuteld op de invoer die haar produceerde, zodat ongewijzigd werk wordt hergebruikt in plaats van opnieuw gebouwd. Een gedeelde externe buildcache laat een heel team en zijn CI elkaars resultaten hergebruiken.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: Het aantal mensen dat zou moeten wegvallen (metaforisch "door een bus aangereden") voordat een project vastloopt bij gebrek aan essentiële kennis. Een lage bus factor signaleert geconcentreerde, ongedocumenteerde expertise en organisatorisch risico.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: De regel die een cache gebruikt om te beslissen welk item te verwijderen wanneer ze vol is, zoals least recently used (LRU) of least frequently used (LFU). Het beleid vormt de hitratio en daarmee de waarde van de cache.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**: Het probleem van gecachete data verwijderen of bijwerken zodra de onderliggende bron verandert, zodat lezers geen verouderde waarden zien. Het is beroemd een van de moeilijkste problemen in de informatica.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Een faalwijze waarin veel clients tegelijk de cache missen voor dezelfde sleutel en samen de bron raken, die daardoor overweldigd raakt. Verzoeken samenvoegen en gespreide vervaltijden voorkomen het. Ook wel thundering herd genoemd.

**Canary release**: Een deploymenttechniek die een nieuwe versie eerst aan een kleine subset gebruikers of verkeer blootstelt, op problemen bewaakt en de uitrol dan progressief uitbreidt als de statistieken gezond blijven.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)** (CAP-theorema): Een principe dat stelt dat een gedistribueerde datastore hooguit twee van Consistency, Availability en Partition tolerance tegelijk kan garanderen. Omdat partities onvermijdelijk zijn, wegen ontwerpers tijdens partities in feite consistentie tegen beschikbaarheid af.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**: Een lichte aanpak om softwarearchitectuur te visualiseren op vier abstractieniveaus: Systeemcontext, Containers, Componenten en Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Continuous Delivery houdt software in een uitleverbare toestand zodat ze op elk moment met handmatige goedkeuring kan worden gedeployd. Continuous Deployment levert elke wijziging die de pijplijn doorstaat automatisch uit.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Een geografisch gedistribueerd netwerk van edge-servers die content cachen en dicht bij gebruikers aanbieden, wat latentie snijdt en de brondinfrastructuur ontlast.

**Chain-of-thought prompting**: Een promptingtechniek die een taalmodel vraagt tussenliggende redeneerstappen door te lopen voordat het een eindantwoord geeft, wat de prestaties bij meerstapsproblemen verbetert ten koste van langere, tragere uitvoer.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: De praktijk van de wijzigingen van ontwikkelaars vaak samenvoegen in een gedeelde hoofdlijn, elke samenvoeging gevalideerd door een geautomatiseerde build- en testsuite om integratieproblemen vroeg te detecteren.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: De gecombineerde pijplijn van Continuous Integration en Continuous Delivery/Deployment die bouwen, testen en uitbrengen van software automatiseert.

**CMMC (Cybersecurity Maturity Model Certification)**: Een programma van het Amerikaanse ministerie van Defensie dat de cyberbeveiligingsvolwassenheid certificeert van aannemers die federale contractinformatie en gecontroleerde niet-gerubriceerde informatie verwerken.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))** (cohesie): De mate waarin de elementen binnen een module bij elkaar horen en één enkel, goed gedefinieerd doel dienen. Hoge cohesie, gekoppeld aan lage koppeling, is een kenmerk van onderhoudbaar ontwerp.

**Context window** (contextvenster): De maximale hoeveelheid tekst, gemeten in tokens, die een taalmodel in één keer kan overwegen, over invoer en uitvoer heen. Het is een schaars budget dat prompt- en contextontwerp bewust moet beheren.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)** (wet van Conway): De waarneming dat de structuur van een systeem de communicatiestructuur van de organisatie die het bouwt de neiging heeft te weerspiegelen. De "inverse Conway-manoeuvre" geeft teams bewust vorm om een gewenste architectuur te produceren.

**Core Web Vitals**: Een set gebruikersgerichte webprestatiestatistieken gedefinieerd door Google (zoals Largest Contentful Paint, Interaction to Next Paint en Cumulative Layout Shift) die laden, interactiviteit en visuele stabiliteit meten.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)** (kosten van vertraging): De economische kosten van iets nog niet af hebben, uitgedrukt als verloren waarde per tijdseenheid. Het expliciet maken zet prioritering om van mening in rekenkunde, en onderbouwt sequencingregels zoals weighted shortest job first.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))** (koppeling): De mate van onderlinge afhankelijkheid tussen modules of services. Losse koppeling beperkt het rimpeleffect van verandering en is een centraal doel van goede architectuur.

**CQRS (Command Query Responsibility Segregation)**: Een patroon dat het model om toestand te wijzigen (commando's) scheidt van het model om toestand te lezen (queries), zodat elk onafhankelijk kan worden geoptimaliseerd en geschaald.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Een publieke catalogus van bekendgemaakte beveiligingskwetsbaarheden, elk met een unieke identifier zodat tools en teams ondubbelzinnig naar dezelfde fout kunnen verwijzen.

**CWV**: Zie Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Beveiligingstesten die een draaiende applicatie van buitenaf onderzoeken, zonder toegang tot broncode, om kwetsbaarheden te vinden die tijdens runtime verschijnen.

**Data-ink ratio**: Een principe van Edward Tufte dat stelt dat een grafiek het grootste deel van haar inkt aan de data zelf moet besteden en weinig aan decoratie, en rasterlijnen, randen en overbodige grafiekelementen verwijdert die niet informeren.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Een gedecentraliseerde dataarchitectuur en bedrijfsmodel dat data behandelt als product bezeten door domeinteams, ondersteund door self-serviceplatforminfrastructuur en gefedereerde governance.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)** (datavisualisatie): De praktijk van data in visuele vorm coderen (positie, lengte, kleur en dergelijke) zodat patronen, vergelijkingen en trends waarneembaar worden en beslissingen beter geïnformeerd.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Een aanpak van softwareontwerp die het model rond het bedrijfsdomein centreert, met een gedeelde ubiquitous language, bounded contexts en bouwstenen zoals entiteiten, value objects en aggregaten.

**Design tokens**: Benoemde, platformonafhankelijke waarden (kleuren, spatiëring, typografie en dergelijke) die ontwerpbeslissingen coderen zodat ze consistent over een designsysteem en meerdere producten kunnen worden gedeeld.

**DevEx / DevX (Developer Experience)** (ontwikkelaarservaring): De algehele kwaliteit van de dagelijkse interactie van een ontwikkelaar met tools, platformen en processen, met wrijving, feedbacksnelheid en cognitieve last.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Een cultuur en set praktijken die softwareontwikkeling en beheer verenigen om opleveringscycli te verkorten, deploymentfrequentie te verhogen en betrouwbaarheid te verbeteren via automatisering en gedeeld eigenaarschap.

**DORA (DevOps Research and Assessment)**: Een onderzoeksprogramma en zijn vier veelgebruikte leveringsstatistieken (deploymentfrequentie, doorlooptijd voor wijzigingen, wijzigingsfaalpercentage en tijd tot herstel van de dienst) gebruikt om de prestaties van softwarelevering te benchmarken.

**DPIA (Data Protection Impact Assessment)** (gegevensbeschermingseffectbeoordeling): Een gestructureerde beoordeling, vereist onder de AVG voor verwerking met hoog risico, die privacyrisico's identificeert en beperkt voordat een project doorgaat.

**Drift (configuration)** (configuratiedrift): De geleidelijke afwijking van de werkelijke toestand van een systeem van haar verklaarde of beoogde toestand, gewoonlijk veroorzaakt door handmatige wijzigingen. Infrastructure as Code en GitOps mikken erop haar te detecteren en te corrigeren.

**Drift (model)** (modeldrift): In machine learning de achteruitgang van modelprestaties in de tijd naarmate de statistische eigenschappen van invoerdata (datadrift) of de gemodelleerde relatie (conceptdrift) veranderen.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)** (rampenherstel): De strategie, procedures en infrastructuur voor het herstellen van dienst en data na een grote verstorende gebeurtenis, doorgaans bepaald door RTO- en RPO-doelen.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Een ontwerpprincipe dat stelt dat elk stuk kennis één enkele, gezaghebbende representatie moet hebben, wat duplicatie en het risico van inconsistente updates vermindert.

## E

**East-west traffic** (oost-westverkeer): Netwerkverkeer tussen services binnen een systeem of datacentrum, in tegenstelling tot noord-zuidverkeer tussen het systeem en externe clients. Een service mesh bestuurt doorgaans oost-westverkeer.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**: Rekenen en opslag draaien dicht bij waar data wordt geproduceerd of gebruikt in plaats van op een centrale locatie, om latentie en bandbreedte te snijden. Content delivery networks zijn een vroege, wijdverbreide vorm.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))** (elasticiteit): Het vermogen van een systeem om automatisch resources te verwerven en vrij te geven als reactie op veranderende vraag, zodat capaciteit de belasting nauw volgt.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Een data-integratiepatroon dat ruwe data eerst in een doelopslag laadt en haar daar transformeert, gebruikmakend van de schaal van moderne warehouses en lakehouses.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: Een representatie van tekst, afbeeldingen of andere data als dichte numerieke vector, zo gepositioneerd dat vergelijkbare items dicht bij elkaar zitten. Embeddings drijven semantisch en vectorzoeken en retrieval-augmented generation.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: De Europese standaard die toegankelijkheidseisen voor ICT-producten en -diensten specificeert, waarnaar publieke aanbesteding in de hele EU verwijst en die is afgestemd op WCAG.

**Error budget** (foutbudget): De toelaatbare hoeveelheid onbetrouwbaarheid die een SLO over een periode toestaat. Wanneer het is uitgeput, prioriteren teams betrouwbaarheidswerk boven nieuwe functies. Het verzoent de spanning tussen snelheid en stabiliteit.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Een data-integratiepatroon dat data uit bronnen extraheert, naar een doelvorm transformeert en in een bestemming zoals een warehouse laadt.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)** (Europese AI-verordening): Europese Unie-regelgeving die AI-systemen indeelt naar risico en dienovereenkomstig verplichtingen oplegt, bepaald gebruik verbiedt en systemen met hoog risico zwaar reguleert.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)** (uiteindelijke consistentie): Een consistentiemodel in gedistribueerde systemen waarin replica's tijdelijk uiteen kunnen lopen maar naar dezelfde toestand convergeren zodra updates ophouden zich te verspreiden.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: Een mechanisme om functionaliteit tijdens runtime aan of uit te zetten zonder te herdeployen, gebruikt voor geleidelijke uitrol, experimenteren en operationele controle.

**Feature store**: Een gecentraliseerd systeem voor het definiëren, opslaan en consistent aanbieden van gecureerde machine-learningfeatures voor zowel training als inferentie, wat duplicatie en training/serving-scheefheid vermindert.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Een Amerikaans overheidsprogramma dat beveiligingsbeoordeling, autorisatie en continue bewaking standaardiseert voor clouddiensten die door federale agentschappen worden gebruikt.

**Few-shot prompting**: Een taalmodel in de prompt een handvol uitgewerkte voorbeelden geven om de gewenste taak en uitvoervorm te demonstreren, in tegenstelling tot zero-shot prompting, dat instructies geeft zonder voorbeelden.

**FinOps**: Een discipline en culturele praktijk die financiële verantwoording brengt in variabele cloudkosten, waarbij engineering-, financiën- en bedrijfsteams gedeeld eigenaarschap van kosten en waarde krijgen.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Amerikaanse wetgeving die federale agentschappen verplicht informatiebeveiligingsprogramma's te implementeren, documenteren en bewaken, grotendeels geoperationaliseerd via NIST-richtlijnen.

**Flow efficiency** (flowefficiëntie): Het deel van de totale doorlooptijd dat een werkitem actief wordt bewerkt in plaats van wacht, berekend als waardetoevoegende tijd gedeeld door totale doorlooptijd. De meeste systemen scoren verrassend laag, vaak onder 15 procent.

**Four-eyes principle** (vierogenprincipe): Een controle die vereist dat een significante handeling door minstens twee mensen wordt beoordeeld of goedgekeurd, wat de kans op fouten of kwade opzet vermindert.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Een geautomatiseerde testtechniek die misvormde, willekeurige of onverwachte invoer aan een programma voedt om crashes, beveiligingsfouten en randgevalsdefecten bloot te leggen.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)** (AVG, Algemene verordening gegevensbescherming): De Europese Unie-verordening die de verwerking van persoonsgegevens bestuurt, individuen rechten verleent en verwerkingsverantwoordelijken en verwerkers verplichtingen oplegt, met aanzienlijke boetes bij niet-naleving.

**GitOps**: Een operationeel model dat Git gebruikt als enkele bron van waarheid voor declaratieve infrastructuur en applicaties, waarbij automatisering het live systeem continu verzoent met de gecommitteerde toestand.

**Golden path / paved road** (gouden pad / gebaande weg): Een goed ondersteunde, eigenzinnige standaardmanier om software binnen een organisatie te bouwen en uit te leveren, ontworpen om de veilige, conforme, betrouwbare keuze de makkelijkste te maken.

**Golden record** (gouden record): In master data management de enkele, verzoende, gezaghebbende versie van een bedrijfsentiteit (zoals een klant) samengesteld uit meerdere bronsystemen via matching- en survivorshipregels.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)** (geleidelijke typering): Een typesysteemaanpak die statische en dynamische typering in één codebasis laat samenbestaan, zodat types incrementeel aan een dynamisch getypeerd programma kunnen worden toegevoegd. Typehints en optionele typecheckers zijn gangbare voorbeelden.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Een querytaal en runtime voor API's die clients precies de data laat opvragen die ze nodig hebben in één aanroep, met een sterk getypeerd schema.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Een hoogpresterend, contract-first remote-procedure-callframework dat HTTP/2 en doorgaans Protocol Buffers gebruikt voor efficiënte communicatie tussen services.

## H

**Hermetic build** (hermetische build): Een build die alleen afhangt van expliciet gedeclareerde invoer en geïsoleerd is van de hostomgeving, zodat ze overal dezelfde uitvoer produceert. Hermeticiteit is het fundament van reproduceerbare builds en betrouwbaar cachen.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Een manipulatiebestendig hardwareapparaat dat cryptografische sleutels genereert, opslaat en gebruikt, wat sterkere sleutelbescherming biedt dan aanpakken met alleen software.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Amerikaanse wetgeving die onder meer eisen stelt aan het beveiligen van beschermde gezondheidsinformatie (PHI) en het gebruik en de openbaarmaking ervan bestuurt.

**Horizontal scaling** (horizontaal schalen): Capaciteit vergroten door meer instanties of nodes toe te voegen ("uitschalen") in plaats van een enkele node krachtiger te maken. Het onderbouwt de meeste grootschalige, veerkrachtige architecturen.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: De praktijk van infrastructuur definiëren en inrichten via machineleesbare, versiebeheerde configuratie in plaats van handmatige processen, wat herhaalbaarheid en review mogelijk maakt.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)** (identiteits- en toegangsbeheer): Het kader van beleid en technologieën dat zorgt dat de juiste identiteiten op de juiste momenten de juiste toegang tot de juiste resources hebben.

**IDP / IdP**: "IDP" duidt gewoonlijk op een Internal Developer Platform, de self-servicetoolinglaag die infrastructuur abstraheert voor productteams. "IdP" duidt op een Identity Provider, een service die gebruikers authenticeert en beweringen uitgeeft. De context maakt het onderscheid.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)** (idempotentie): Een eigenschap waarbij een bewerking meermaals uitvoeren hetzelfde effect heeft als haar eenmaal uitvoeren, essentieel voor veilige herhalingen in gedistribueerde systemen en API's.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)** (internationalisering): Software zo ontwerpen en bouwen dat ze zonder engineeringwijzigingen kan worden aangepast aan verschillende talen, regio's en culturele conventies. Het numeroniem verkort de 18 letters tussen "i" en "n."

**Immutable artefact** (onveranderlijk artefact): Een builduitvoer die, eenmaal geproduceerd en geversioneerd, nooit wordt gewijzigd. Elke wijziging levert een nieuwe versie. Onveranderlijkheid maakt releases reproduceerbaar en laat je eenmaal bouwen en hetzelfde artefact over omgevingen promoveren.

**InnerSource**: De toepassing van open-sourceontwikkelpraktijken (transparantie, gedeelde repositories en bijdragen over teams heen) binnen één organisatie.

**IaC drift**: Zie Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)** (omgekeerde index): De kerndatastructuur van een zoekmachine, die elke term koppelt aan de lijst documenten die haar bevatten, zodat zoekopdrachten kunnen worden beantwoord zonder elk document te scannen.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Een internationale standaard die eisen specificeert voor een Information Security Management System (ISMS), met een certificeerbaar kader voor het beheren van informatiebeveiligingsrisico.

**ISO/IEC 42001**: Een internationale standaard die eisen specificeert voor een AI-managementsysteem, met een certificeerbaar kader voor organisaties om de ontwikkeling en het gebruik van AI verantwoord te besturen.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Een compact, ondertekend (en optioneel versleuteld) tokenformaat gebruikt om claims tussen partijen over te brengen, gangbaar voor authenticatie en autorisatie in web- en API-systemen.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Een lean workflowmethode die werk op een bord visualiseert, werk in uitvoering begrenst en flow beheert om doorvoer en voorspelbaarheid te verbeteren.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Een ontwerpprincipe dat de eenvoudigste oplossing verkiest die aan de behoefte voldoet, op grond dat onnodige complexiteit kosten en risico verhoogt.

**KMS (Key Management Service)** (sleutelbeheerdienst): Een systeem voor het aanmaken, opslaan, roteren en controleren van toegang tot cryptografische sleutels, vaak gesteund door hardware security modules.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)** (kritieke prestatie-indicator): Een kwantificeerbare maat gebruikt om voortgang naar een specifieke bedrijfs- of operationele doelstelling te volgen.

## L

**Lakehouse**: Een dataarchitectuur die de goedkope, flexibele opslag van een datalake combineert met de beheer-, transactie- en prestatiefuncties van een datawarehouse.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)** (doorlooptijd): De verstreken tijd van het aanvragen (of committen) van een wijziging tot haar oplevering in productie. Een kern-DORA-leveringsstatistiek.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)** (minimale rechten): Een beveiligingsprincipe dat elke gebruiker, elk proces of systeem alleen de minimale toegang verleent die nodig is om zijn functie uit te voeren, wat de schade van compromittering of fouten beperkt.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)** (wet van Little): Een resultaat uit de wachtrijtheorie dat stelt dat het gemiddelde aantal items in een stabiel systeem gelijk is aan de gemiddelde aankomstsnelheid vermenigvuldigd met de gemiddelde tijd die elk item in het systeem doorbrengt. Het verbindt werk in uitvoering, doorvoer en doorlooptijd.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)** (groot taalmodel): Een machine-learningmodel getraind op zeer grote tekstcorpora om taal te voorspellen en te genereren, in staat tot taken als samenvatten, vertalen en codegeneratie.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)** (lokalisatie): Geïnternationaliseerde software aanpassen aan een specifieke locale, inclusief vertaling, opmaak en culturele conventies. Het numeroniem verkort de 10 letters tussen "l" en "n."

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)** (stamdatabeheer): De discipline en tooling voor het creëren en onderhouden van één enkel, gezaghebbend, consistent beeld van kernbedrijfsentiteiten (zoals klanten of producten) over systemen.

**MITRE ATT&CK**: Een gecureerde, publieke kennisbank van tactieken en technieken van echte tegenstanders, veel gebruikt om red-teamoefeningen te plannen, detectie-engineering te sturen en dreigingen in een gedeeld vocabulaire te beschrijven.

**Mean Time to Recovery (MTTR)** (gemiddelde hersteltijd): De gemiddelde tijd om dienst te herstellen na een falen. Een gangbare betrouwbaarheids- en incidentmanagementstatistiek.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: Een praktijk waarin een heel team samen aan dezelfde taak werkt op dezelfde computer, wisselend wie typt, om kennis te delen en beslissingen collectief te nemen.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: De set praktijken die machine-learningmodellen betrouwbaar en efficiënt in productie deployen, bewaken en onderhouden, en DevOps-principes uitbreidt naar de ML-levenscyclus.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Een enkele versiebeheerrepository die de code voor veel projecten of de hele organisatie bevat, wat gedeelde tooling en atomaire wijzigingen over projecten heen mogelijk maakt ten koste van gespecialiseerde schaaltooling.

**mTLS (mutual TLS)**: Een configuratie van Transport Layer Security waarin beide partijen certificaten tonen en verifiëren, zodat elk de ander authenticeert. Het is een standaard voor verkeer tussen services in een service mesh en zero-trustnetwerken. Zie ook [wederzijdse authenticatie](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)** (mutatietesten): Een techniek die bewust kleine fouten ("mutanten") in code introduceert om te controleren of de testsuite ze detecteert, wat de werkelijke effectiviteit van de suite meet.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Een rangschikkingskwaliteitsstatistiek die beloont dat zeer relevante resultaten bovenaan een resultatenlijst staan, genormaliseerd zodat scores over zoekopdrachten vergelijkbaar zijn. Een vast onderdeel van evaluatie van zoekrelevantie.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Een Amerikaans federaal agentschap wiens Special Publications en kaders veelgenoemde standaarden zijn voor cyberbeveiliging, privacy en AI.

**NIST AI RMF (AI Risk Management Framework)**: Een vrijwillig NIST-kader voor het identificeren, beoordelen en beheren van risico's van AI-systemen over hun levenscyclus, georganiseerd rond de functies Govern, Map, Measure en Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Een NIST-catalogus van beveiligings- en privacymaatregelen voor federale informatiesystemen, ruim buiten de overheid gebruikt als basislijn.

**NIST SP 800-171**: Een NIST-publicatie die eisen specificeert voor het beschermen van gecontroleerde niet-gerubriceerde informatie (CUI) in niet-federale systemen, centraal voor compliance van defensieaannemers.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)** (niet-functionele eis): Een eis die beschrijft hoe een systeem zich moet gedragen (haar kwaliteiten zoals prestaties, beveiliging, betrouwbaarheid of bruikbaarheid) in plaats van welke functies ze uitvoert.

**North-south traffic** (noord-zuidverkeer): Netwerkverkeer tussen een systeem en zijn externe clients (het datacentrum of cluster in en uit), in tegenstelling tot oost-westverkeer tussen interne services. Een API-gateway bestuurt doorgaans noord-zuidverkeer.

## O

**Observability** (observeerbaarheid): De mate waarin de interne toestand van een systeem uit haar externe uitvoer kan worden afgeleid, doorgaans bereikt via telemetrie: statistieken, logs en traces.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Een doelstellingskader dat een kwalitatieve objective koppelt aan een paar meetbare key results om een organisatie af te stemmen en te focussen.

**OpenTelemetry (OTel)**: Een leveranciersneutrale, open standaard en toolset voor het genereren, verzamelen en exporteren van telemetriedata (traces, statistieken en logs) uit software.

**OPA (Open Policy Agent)**: Een open-source, algemene beleidsengine die beleid (geschreven in de taal Rego) evalueert om autorisatie- en configuratieregels over de stack af te dwingen, wat policy as code mogelijk maakt.

**OSPO (Open Source Program Office)**: Een organisatiefunctie die open-sourcestrategie, governance, compliance en gemeenschapsbetrokkenheid coördineert en zowel gebruik als bijdragen beheert.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Een non-profitgemeenschap die veelgebruikte, vrij beschikbare applicatiebeveiligingsbronnen produceert, waaronder de OWASP Top Ten en de ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Een uitbreiding van het CAP-theorema die stelt dat als er een Partitie is, een systeem Beschikbaarheid tegen Consistentie afweegt, Else (in normaal bedrijf) Latentie tegen Consistentie.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Een door de betaalkaartsector beheerde beveiligingsstandaard die eisen specificeert voor organisaties die kaarthoudergegevens opslaan, verwerken of verzenden.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)** (penetratietesten): Een geautoriseerde, gesimuleerde aanval op een systeem door bekwame testers om uitbuitbare kwetsbaarheden te vinden en aan te tonen voordat echte aanvallers het doen, geleverd als geprioriteerde, uitvoerbare bevindingen.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)** (persoonsgegevens): Informatie die een specifiek individu kan identificeren, alleen of gecombineerd met andere data. De verwerking ervan wordt bepaald door privacywetten en intern beleid.

**Platform engineering**: De discipline van interne self-serviceplatformen en gouden paden bouwen en beheren die cognitieve last verminderen en productteams versnellen.

**POUR**: De vier leidende principes van de Web Content Accessibility Guidelines: content moet Perceivable (waarneembaar), Operable (bedienbaar), Understandable (begrijpelijk) en Robust (robuust) zijn.

**Production readiness review** (productiegereedheidsreview): Een gestructureerde controle, uitgevoerd voordat een service live gaat of bereikbaarheidseigenaarschap overneemt, die bevestigt dat ze voldoet aan standaarden voor observeerbaarheid, betrouwbaarheid, beveiliging, runbooks en operationele ondersteuning.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)** (promptengineering): De praktijk van de instructies, context en voorbeelden ontwerpen en verfijnen die aan een taalmodel worden gegeven om betrouwbare uitvoer van hoge kwaliteit te krijgen, behandeld als een versiebeheerde, geteste engineeringdiscipline in plaats van vallen en opstaan.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Een aanval waarin vervaardigde invoer een taalmodel zijn beoogde instructies laat negeren en die van de aanvaller volgt, het AI-tijdperkequivalent van injectiefouten. Het is een centraal beveiligingsrisico van LLM-applicaties.

**Property-based testing** (eigenschapsgebaseerd testen): Een testtechniek die controleert dat vermelde eigenschappen gelden over veel automatisch gegenereerde invoeren, in plaats van alleen op met de hand gekozen voorbeelden te leunen.

**Pull request (PR) / merge request (MR)**: Een voorgestelde set wijzigingen ingediend voor review en discussie voordat ze in een gedeelde branch worden samengevoegd, de primaire eenheid van codereview in de meeste workflows.

**Purple team**: Een samenwerkingsoefening waarin offensieve (rode) en defensieve (blauwe) beveiligingsteams in real time samenwerken, zodat aanvallen en de detecties die ze moeten vangen op elkaar worden afgestemd.

## Q

**Quality gate** (kwaliteitspoort): Een geautomatiseerd controlepunt in een pijplijn dat moet worden gepasseerd (bijvoorbeeld het halen van dekkings-, beveiligings- of prestatiedrempels) voordat een wijziging kan doorgaan.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: In gedistribueerde systemen het minimale aantal nodes dat het eens moet zijn voordat een bewerking (zoals een lees- of schrijfactie) als geslaagd geldt, gebruikt om consistentie te behouden ondanks falen.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Een verantwoordelijkhedentoewijzingsmodel dat elke deelnemer aan een taak of beslissing labelt als Responsible, Accountable, Consulted of Informed.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Een techniek die de uitvoer van een taalmodel gronden door eerst relevante documenten of data op te halen en als context aan te leveren, wat nauwkeurigheid verbetert en hallucinatie vermindert.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)** (op rollen gebaseerde toegangscontrole): Een autorisatiemodel dat rechten aan rollen toewijst en rollen aan gebruikers, wat beheer vereenvoudigt door toegang op rolniveau te beheren.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: Een groep die een realistische tegenstander nabootst, vaak tegen een hele organisatie en zonder waarschuwing van de verdedigers, om detectie en respons te testen in plaats van slechts kwetsbaarheden op te sommen. Contrast met een blauw (defensief) team.

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)** (referentiedata): Gecontroleerde, langzaam veranderende codelijsten en classificaties gebruikt om andere data te categoriseren, zoals landcodes, valuta's en statuswaarden. Haar beheren als gedeeld, versiebeheerd vocabulaire houdt systemen consistent.

**Rego**: De declaratieve beleidstaal die Open Policy Agent gebruikt om regels voor autorisatie- en configuratiebeslissingen uit te drukken.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Een architectuurstijl voor genetwerkte applicaties die stateless bewerkingen over HTTP op adresseerbare resources gebruikt, gewaardeerd om eenvoud en brede tooling.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)** (omgekeerde proxy): Een server die voor een of meer backendservices zit en clientverzoeken naar hen doorstuurt, doorgaans TLS-terminatie, load balancing, caching en een enkel toegangspunt biedend.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Een geschreven voorstel dat voor feedback circuleert vóór een significante technische beslissing of wijziging, wat transparantie en gedeeld eigenaarschap bevordert. (De term benoemt ook de documentenreeks van internetstandaarden.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)** (rendement op investering): Een maat voor de waarde verkregen uit een investering ten opzichte van haar kosten, gebruikt om engineering- en technologiebeslissingen te rechtvaardigen en te prioriteren.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: Software-"robots" die repetitieve, regelgebaseerde taken automatiseren door met bestaande gebruikersinterfaces en systemen te werken zoals een persoon dat zou doen.

**RPO (Recovery Point Objective)**: Het maximaal aanvaardbare dataverlies gemeten in tijd (bijvoorbeeld "tot vijf minuten"), dat definieert hoe frequent data moet worden beschermd.

**RTO (Recovery Time Objective)**: De maximaal aanvaardbare duur om een service te herstellen na een verstoring, die ontwerp en investering voor rampenherstel stuurt.

## S

**Saga**: Een patroon voor het beheren van dataconsistentie over services in een gedistribueerde transactie door lokale transacties te sequencen en compenserende handelingen uit te geven wanneer een stap faalt.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Een kader voor het toepassen van agile en lean praktijken over grote ondernemingen, dat veel teams coördineert. Gewaardeerd om structuur en bekritiseerd om mogelijke zwaarte.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Beveiligingstesten die broncode, bytecode of binaire bestanden analyseren zonder ze uit te voeren om kwetsbaarheden vroeg in de ontwikkeling te vinden.

**SBOM (Software Bill of Materials)**: Een formele, machineleesbare inventaris van de componenten en afhankelijkheden in een stuk software, gebruikt om risico in de toeleveringsketen en kwetsbaarheden te beheren.

**SCA (Software Composition Analysis)**: Tooling die open-source- en derde-partijcomponenten in een codebasis identificeert en bekende kwetsbaarheden en licentierisico's markeert.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Een agile kader dat werk organiseert in iteraties van vaste lengte (sprints) met gedefinieerde rollen, gebeurtenissen en artefacten om waardeincrementen op te leveren.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Een Amerikaanse wet die federale agentschappen verplicht hun elektronische en informatietechnologie toegankelijk te maken voor mensen met een beperking, in de praktijk afgestemd op WCAG.

**Semantic search** (semantisch zoeken): Zoeken dat op betekenis matcht in plaats van exacte trefwoorden, doorgaans door embeddings van de zoekopdracht en documenten te vergelijken. Het wordt vaak gecombineerd met lexicaal zoeken in een hybride aanpak.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Een speciale infrastructuurlaag, meestal geïmplementeerd met sidecarproxy's, die zorgen rond communicatie tussen services afhandelt zoals mutual TLS, herhalingen, timeouts, verkeersverschuiving en observeerbaarheid, en ze uit applicatiecode houdt.

**Sidecar**: Een hulpproces of container naast een hoofdapplicatie-instantie gedeployd om ondersteunende mogelijkheden te bieden (zoals een service-meshproxy) zonder de applicatie zelf te wijzigen.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Een systeem dat beveiligingslogs en -gebeurtenissen over een omgeving aggregeert en correleert om detectie, alarmering en onderzoek mogelijk te maken.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Een formele toezegging tussen een serviceaanbieder en zijn klanten die verwachte serviceniveaus en de gevolgen van missen specificeert.

**SLI (Service Level Indicator)**: Een kwantitatieve maat van een aspect van servicekwaliteit, zoals verzoeklatentie of foutpercentage, die SLO's voedt.

**SLO (Service Level Objective)**: Een doelwaarde of -bereik voor een SLI dat het gewenste betrouwbaarheidsniveau definieert en de basis vormt van foutbudgetten.

**SLSA (Supply-chain Levels for Software Artifacts)**: Een kader van gegradeerde beveiligingseisen om de integriteit en herkomst van softwareartefacten te verbeteren via het build- en releaseproces.

**SOAR (Security Orchestration, Automation, and Response)**: Tools en praktijken die beveiligingsoperaties automatiseren en coördineren, zoals triage- en responsdraaiboeken, om snelheid en consistentie te verbeteren.

**SOC 2 (System and Organisation Controls 2)**: Een auditkader en rapport, gebaseerd op de Trust Services Criteria van de AICPA, dat de maatregelen van een serviceorganisatie beoordeelt voor beveiliging, beschikbaarheid, verwerkingsintegriteit, vertrouwelijkheid en privacy.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Vijf objectgeoriënteerde ontwerpprincipes (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation en Dependency Inversion) die onderhoudbare, flexibele code bevorderen.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Amerikaanse wetgeving die eisen stelt aan financiële rapportage en interne beheersing bij beursgenoteerde bedrijven, met gevolgen voor de IT-systemen die financiële data ondersteunen.

**SPACE**: Een kader voor het meten van ontwikkelaarsproductiviteit over vijf dimensies: Satisfaction en welzijn, Performance, Activity, Communication en samenwerking en Efficiency en flow, dat waarschuwt tegen maten met één statistiek.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Een discipline die software-engineeringaanpakken toepast op beheer, met SLO's, foutbudgetten en automatisering om betrouwbare systemen op schaal te draaien.

**SSDF (Secure Software Development Framework)**: Het kader van NIST (SP 800-218) van veilige-ontwikkelpraktijken op hoog niveau, dat de organisatie voorbereiden, software beschermen, goed beveiligde software produceren en reageren op kwetsbaarheden omvat.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)** (statische analyse): Broncode, bytecode of binaire bestanden onderzoeken zonder ze uit te voeren om defecten, stijlschendingen en beveiligingsfouten te vinden, doorgaans via linters, typecheckers en speciale analysers in de editor en pijplijn.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Een taxonomie voor dreigingsmodellering die dreigingen indeelt als Spoofing, Tampering, Repudiation, Information disclosure, Denial of service en Elevation of privilege.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: De volledige levenslange kosten van een systeem of beslissing, inclusief aanschaf, beheer, onderhoud en uiteindelijke uitfasering, niet alleen de initiële prijs.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)** (testgedreven ontwikkeling): Een praktijk van een falende geautomatiseerde test schrijven vóór de code die haar laat slagen, dan refactoren, in korte herhaalde cycli om ontwerp te sturen en dekking te verzekeren.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)** (technische schuld): De geïmpliceerde toekomstige kosten van nu een opportune oplossing kiezen boven een betere die langer zou duren, die bewust moet worden beheerd in plaats van onbewust opgebouwd.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Een klassiek wegingsschema dat het belang van een term voor een document scoort naar hoe vaak ze er voorkomt, gecompenseerd door hoe gangbaar ze is over het hele corpus. Het onderbouwt veel lexicale zoekrangschikking.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Een managementaanpak die stelt dat de doorvoer van een systeem op elk moment wordt beperkt door één enkel knelpunt, dus verbeterinspanningen moeten zich op die beperking richten tot ze elders heen verschuift.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)** (dreigingsmodellering): Een gestructureerde praktijk van mogelijke dreigingen voor een systeem identificeren, opsommen en prioriteren zodat verdediging vroeg kan worden ingebouwd.

**Toil** (sleurwerk): In SRE handmatig, repetitief, automatiseerbaar operationeel werk dat lineair meegroeit met een service en geen blijvende waarde biedt. Het verminderen ervan maakt capaciteit voor engineering vrij.

**Trunk-based development**: Een broncodebeheerpraktijk waarin ontwikkelaars vaak kleine wijzigingen integreren in één gedeelde branch, wat langlevende branches en samenvoegpijn minimaliseert.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)** (typeafleiding): Een taalfunctie die de types van expressies automatisch afleidt, wat veel van de veiligheid van statische typering geeft zonder dat elk type met de hand hoeft te worden uitgeschreven.

**[Type system](https://en.wikipedia.org/wiki/Type_system)** (typesysteem): De set regels die een taal gebruikt om types toe te wijzen en te controleren, wat hele klassen fouten vangt voordat het programma draait en intentie documenteert. Typesystemen lopen van dynamisch tot statisch en van zwak tot sterk.

## U

**Ubiquitous language**: In Domain-Driven Design een gedeeld, precies vocabulaire dat consistent door ontwikkelaars en domeinexperts wordt gebruikt en direct in de code en modellen wordt weerspiegeld.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)** (gebruikersacceptatietest): Testen uitgevoerd door eindgebruikers of hun vertegenwoordigers om te bevestigen dat een systeem aan bedrijfsbehoeften voldoet voordat het voor release wordt geaccepteerd.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: User Experience is de algehele kwaliteit van iemands interactie met een product. User Interface is het specifieke visuele en interactieve oppervlak waardoor die interactie plaatsvindt.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)** (waardeobject): In Domain-Driven Design een onveranderlijk object dat volledig wordt gedefinieerd door zijn attributen in plaats van een aparte identiteit, zoals een geldbedrag of een datumbereik.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)** (waardestroomanalyse): Een techniek om elke stap van idee tot opgeleverde waarde te tekenen, waardetoevoegende tijd van wachttijd onderscheidend, zodat knelpunten, overdrachten en herwerklussen zichtbaar en verbeterbaar worden.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)** (vectordatabase): Een datastore geoptimaliseerd voor het indexeren en doorzoeken van hoogdimensionale embeddingvectoren op gelijkenis, een gangbare ruggengraat van semantisch zoeken en retrieval-augmented generation.

**Vertical scaling** (verticaal schalen): Capaciteit vergroten door een enkele node krachtiger te maken ("opschalen"), wat eenvoudig is maar uiteindelijk wordt begrensd door de grootste beschikbare machine.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)** (versiebeheersysteem): Een tool, zoals Git, die wijzigingen aan bestanden in de tijd vastlegt zodat geschiedenis kan worden beoordeeld, branches kunnen worden onderhouden en werk kan worden gecoördineerd.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)** (kwetsbaarheidsscannen): Geautomatiseerde inspectie van systemen, containers of code tegen databases van bekende zwaktes en misconfiguraties. Het is breed en goedkoop en vult de diepte van handmatige penetratietesten aan.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Een W3C-set internationaal erkende richtlijnen, georganiseerd rond de POUR-principes en conformiteitsniveaus A, AA en AAA, om webcontent toegankelijk te maken.

**Wardley map**: Een visuele strategietechniek die capaciteiten positioneert naar hun waarde voor gebruikers en hun evolutionaire volwassenheid, om beslissingen over bouwen/kopen en investering te informeren.

**Work in progress (WIP) limit** (WIP-limiet): Een grens aan hoeveel items tegelijk in een bepaalde fase van een workflow mogen zijn, een kern-kanbanpraktijk die flow verbetert door knelpunten bloot te leggen en de overhead van te veel parallel werk te beteugelen.

**WSJF (Weighted Shortest Job First)**: Een prioriteringsmethode die werk sequenct door zijn kosten van vertraging te delen door zijn geschatte duur, zodat de kortste, meest tijdgevoelige, meest waardevolle items eerst worden gedaan.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Een webkwetsbaarheid waarbij een aanvaller kwaadaardige scripts injecteert die in de browsers van andere gebruikers worden uitgevoerd, mogelijk data stelen of sessies kapen.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Een principe dat afraadt functionaliteit op speculatie te bouwen, op grond dat verwachte behoeften vaak niet materialiseren en kosten en complexiteit toevoegen.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Een beveiligingsmodel dat geen impliciet vertrouwen aanneemt op basis van netwerklocatie en elk toegangsverzoek continu verifieert tegen identiteit, apparaat en context, volgens het adagium "vertrouw nooit, verifieer altijd."
