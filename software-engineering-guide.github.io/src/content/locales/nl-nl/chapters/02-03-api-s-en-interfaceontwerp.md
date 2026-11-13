# 2.3 API's en interfaceontwerp

## Overzicht en motivatie

Een [API](https://en.wikipedia.org/wiki/API) (application programming interface) is het contract waarmee het ene stuk software capaciteit aanbiedt aan een ander. Het is waar teams, systemen en organisaties elkaar ontmoeten, en het is het duurzaamste en duurste ding om fout te doen. Je kunt de signatuur van een interne functie vrij refactoren. Een gepubliceerde API is anders: het is een belofte aan afnemers die je misschien nooit ontmoet, en haar breken breekt hen. Naarmate organisaties [monolieten](https://en.wikipedia.org/wiki/Monolithic_application) in services opsplitsen en capaciteiten openstellen voor partners en het publiek, wordt de API het belangrijkste productoppervlak en het belangrijkste integratierisico.

Voor grote teams zijn API's wat mensen onafhankelijk laat werken. Een goed ontworpen interface laat je je binnenwerk wijzigen zonder te coördineren met elke afnemer, wat het hele punt van een servicegrens is. Een slecht ontworpen interface lekt interne details, forceert gelijkgeschakelde deployments en verandert een set services in een gedistribueerde monoliet: services die uit elkaar zijn gesplitst maar zo gekoppeld zijn dat ze samen moeten worden gebouwd en gedeployd. Je API-ontwerp bepaalt direct hoe onafhankelijk je teams kunnen bewegen.

In omgevingen van onderneming en overheid dragen API's ook verplichtingen op het gebied van compliance, beveiliging en levensduur. Een publieke API kan verplicht zijn [open standaarden](https://en.wikipedia.org/wiki/Open_standard) te volgen, jarenlang stabiel te blijven en externe ontwikkelaars te bedienen met wie je niet kunt coördineren. API's van ondernemingen vormen de basis van partnerintegraties met contractuele servicenivo's. Dit alles verhoogt de lat voor versiediscipline, [achterwaartse compatibiliteit](https://en.wikipedia.org/wiki/Backward_compatibility), governance en ontwikkelaarservaring.

## Kernprincipes

- Ontwerp eerst het contract. De interface is een bewuste productbeslissing, geen bijproduct van de implementatie.
- Optimaliseer voor de ervaring van de afnemer, niet voor je eigen gemak.
- Behandel achterwaartse compatibiliteit als belofte. Brekende wijzigingen vragen een nieuwe versie en een migratiepad.
- Maak het makkelijke ding correct: verstandige standaarden, voorspelbare fouten, consistente conventies.
- Ontwerp voor falen. [Idempotentie](https://en.wikipedia.org/wiki/Idempotence) (een herhaald verzoek heeft hetzelfde effect als één verzoek), herhalingen, paginering en [ratebeperking](https://en.wikipedia.org/wiki/Rate_limiting) zijn volwaardige zorgen, geen bijzaken.
- Kies de protocolstijl naar de interactie, niet naar de mode.
- Bestuur API's als producten, met eigenaren, levenscycli en documentatie.

## Aanbevelingen

### Werk API-eerst en contractgedreven

Definieer en beoordeel het API-contract, inclusief haar resources, operaties, schema's en foutsemantiek, voordat je de implementatie schrijft. Gebruik een machineleesbare specificatie, zodat het contract documentatie, client- en serverstubs, mockservers en validatie kan genereren. Nu kunnen afnemers beginnen te integreren tegen de mock terwijl jij bouwt, en wordt het contract de enige bron van waarheid waartegen beide kanten testen.

### Kies de interactiestijl bewust

Kies tussen [REST](https://en.wikipedia.org/wiki/REST) (representational state transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) en [gebeurtenisgedreven berichtenverkeer](https://en.wikipedia.org/wiki/Event-driven_architecture) op basis van de interactie, niet van persoonlijke voorkeur. Gebruik REST voor resourcegeoriënteerde, breed interoperabele, cachebare interfaces. Gebruik GraphQL wanneer uiteenlopende clients flexibele, geaggregeerde leesacties over een rijke graaf nodig hebben. Gebruik gRPC voor krachtige, sterk getypeerde aanroepen tussen interne services. Gebruik gebeurtenisgedreven berichtenverkeer voor asynchrone, ontkoppelde workflows en voor het verspreiden van toestandswijzigingen. Veel grote systemen gebruiken meerdere stijlen tegelijk, elk waar het past.

### Versioneer en schaf af met discipline

Neem een expliciete versiestrategie en een gepubliceerd afschaffingsbeleid aan: hoe je wijzigingen indeelt, hoe lang je oude versies ondersteunt en hoe je afnemers op de hoogte stelt. Trek een duidelijke lijn tussen achterwaarts compatibele wijzigingen (optionele velden toevoegen, nieuwe eindpunten) en brekende wijzigingen (velden verwijderen of hernoemen, typen of semantiek wijzigen). Geef nooit de betekenis van een bestaand veld een andere bestemming. Geef afnemers overlappende vensters om te migreren en communiceer tijdlijnen ruim van tevoren.

### Maak foutsemantiek consistent en machineleesbaar

Retourneer gestructureerde, voorspelbare fouten: stabiele machineleesbare codes, voor mensen leesbare berichten en genoeg context om op te handelen, zonder gevoelige interne zaken te lekken. Gebruik dezelfde statussemantiek over elk eindpunt, zodat clients fouten uniform kunnen afhandelen. Documenteer elke fout waar een afnemer tegenaan kan lopen.

### Bouw idempotentie, paginering en ratebeperking in

Maak schrijfoperaties veilig om te herhalen door idempotentiesleutels te ondersteunen, zodat een client die na een time-out opnieuw probeert niet dubbel afschrijft of dubbel aanmaakt. Pagineer elk lijsteindpunt vanaf dag één, en geef de voorkeur aan cursorgebaseerde paginering voor grote of veranderende datasets. Pas ratelimieten toe en documenteer ze, en retourneer de huidige limietstatus aan clients zodat ze netjes kunnen terugschakelen.

### Bestuur API's en investeer in ontwikkelaarservaring

Behandel elke API als een product, met een eigenaar, een levenscyclus en een catalogusvermelding. Zet een ontwerpreview of een API-standaardenraad op, zodat interfaces consistent blijven over teams. Investeer in ontwikkelaarservaring: accurate referentiedocumentatie, quickstarts, voorbeelden, een sandbox en een changelog. In een groot ecosysteem is een portaal of catalogus die API's vindbaar maakt essentieel.

## Afwegingen: voor- en nadelen

| Stijl | Het best voor | Voordelen | Nadelen |
|---|---|---|---|
| REST / HTTP | Publieke, resourcegeoriënteerde API's | Alomtegenwoordig, cachebaar, eenvoudig, interoperabel | Te veel/te weinig ophalen. Veel roundtrips. Losse contracten tenzij gespecificeerd |
| GraphQL | Flexibele leesacties voor uiteenlopende clients | Door de client gespecificeerde queries. Eén eindpunt. Sterk schema | Complexiteit van caching en ratebeperking. Risico's van querykosten. Complexiteit aan serverzijde |
| gRPC | Interne krachtige aanroepen | Snel, compact, sterk getypeerd, streaming | Slechte browserondersteuning. Minder leesbaar voor mensen. Zwaardere tooling |
| Gebeurtenisgedreven | Asynchrone, ontkoppelde workflows | Losse koppeling. Schaalbaar. Veerkrachtig | Moeilijker om over te redeneren. Uiteindelijke consistentie. Operationele complexiteit |

Versiestrategieën wegen stabiliteit tegen onderhoud. Veel oude versies ondersteunen beschermt afnemers, maar vermenigvuldigt de code die je moet onderhouden en testen. Achterwaartse compatibiliteit ruilt je eigen vrijheid in voor stabiliteit van afnemers, meestal de juiste ruil voor een breed gebruikte API. Het grote plaatje: de kosten van een slechte API-beslissing worden betaald door elke afnemer gedurende het hele leven van de interface. Het is dus de moeite waard aan de grens meer ontwerpinspanning te besteden dan bijna overal anders.

## Vragen om met je team te bespreken

1. **Hoe deel je een wijziging in als achterwaarts compatibel of brekend, en welke geautomatiseerde controle vangt een stille breuk op voordat die wordt opgeleverd?** Dit hoofdstuk trekt een harde lijn: optionele velden en nieuwe eindpunten toevoegen is veilig, terwijl het verwijderen of hernoemen van velden, het wijzigen van typen of het herbestemmen van de betekenis van een veld afnemers breekt. In een groot team kan de persoon die de wijziging maakt vaak niet elke afnemer zien, zodat een "kleine" aanpassing stilletjes partners kan breken met wie je nooit praat. Neem het concrete signaal mee naar de vergadering: draai je geautomatiseerde contractcompatibiliteitscontroles in CI tegen de gepubliceerde specificatie, of vertrouw je erop dat iemand de regel onthoudt. In omgevingen van onderneming en overheid, waar een brekende wijziging een gecoördineerde migratie afdwingt over elke partner en leveranciers- en bestuurswisselingen kan overspannen, schalen de kosten met het aantal afnemers. Bepaal de indelingsregels en koppel een compatibiliteitspoort, zodat een onverenigbare wijziging de build laat falen in plaats van een integratie.

2. **Welke betrouwbaarheidsprimitieven, idempotentiesleutels, paginering en ratebeperking, zijn vanaf dag één verplicht op elk nieuw eindpunt?** Het hoofdstuk staat erop dat dit volwaardige zorgen zijn, omdat het achteraf aanbrengen van een idempotentiesleutel op een live afschrijvingseindpunt of het toevoegen van paginering aan een lijst die al live is zelf een brekende wijziging is. Een groot ecosysteem versterkt dit: een eindpunt dat in testen werkt, bezwijkt onder echt datavolume, en een niet-idempotente schrijfactie verandert één netwerkstoring in dubbele afschrijvingen. Neem het bewijs mee van welke huidige eindpunten deze missen en wat een herhaalstorm zou doen. Maak de standaarden niet-onderhandelbaar voor nieuwe eindpunten: cursorpaginering op elke lijst, idempotentiesleutels op elke schrijfactie, gedocumenteerde ratelimieten die hun huidige status teruggeven. Dat zet een toekomstige geforceerde migratie om in een eenmalige ontwerpgewoonte.

3. **Ontwerp en beoordeel je het contract werkelijk vóór het schrijven van de implementatie, of lekt de interface uit de code?** De API-eerst aanbeveling vraagt om een machineleesbare specificatie, vooraf beoordeeld, die documentatie, stubs en mocks genereert en afnemers laat integreren tegen een mock terwijl jij bouwt. Wanneer het contract achter de implementatie aan loopt, onthult de interface de interne databasestructuur en verschuift ze elke keer dat de implementatie verandert, wat het belangrijkste antipatroon in dit hoofdstuk is. Het signaal om te onderzoeken: kan een afnemer vandaag beginnen te integreren tegen je mock, of moet die wachten op een draaiende backend. Voor publieke en partner-API's, waar de interface het productoppervlak is en het duurste om fout te doen, bespaart een dag aan het contract besteden weken aan supportgedoe. Maak contractreview een verplichte stap voordat de implementatie begint.

4. **Wanneer twee teams dezelfde capaciteit moeten blootstellen, welke interactiestijl wint, en wie heeft de bevoegdheid nee te zeggen tegen een vierde protocol?** Dit hoofdstuk zegt je REST, GraphQL, gRPC of gebeurtenisgedreven berichtenverkeer te kiezen naar interactiepasvorm, maar op schaal is het echte risico dat elk team zijn eigen favoriet kiest en afnemers bij elk eindpunt een andere conventie tegenkomen. Een grote organisatie betaalt voor die fragmentatie in clientbibliotheken, gateways, monitoring en de cognitieve belasting van elke integrator die nu vier idiomen leert in plaats van één. Neem de inventaris van protocollen die al in productie zijn mee, de interactie die elk moest dienen en de afnemers die meer dan één overspannen. De concurrerende overweging is echt: een gedeelde standaard vermindert woekering, maar een rigide verplichting dwingt gRPC-vormige problemen in een REST-vormig gat. Noem de standaardeninstantie of architectuurreview die het uitzonderingsproces bezit, want in omgevingen van onderneming en overheid wordt een wildgroei aan stijlen een permanente belasting op integratie en moeilijk terug te draaien zodra partners van elk afhangen.

5. **Wat is ons gepubliceerde afschaffingsbeleid, en kunnen we bewijzen dat we het ondersteuningsvenster dat we adverteren daadwerkelijk eerbiedigen?** Het hoofdstuk behandelt versiebeheer en afschaffing als discipline: een schriftelijk beleid voor hoe lang oude versies leven, hoe afnemers worden geïnformeerd en welke overlap ze krijgen om te migreren. Een belofte die je niet kunt afdwingen is erger dan geen, omdat een groot ecosysteem afnemers omvat met wie je nooit spreekt en die een ingetrokken versie blijven aanroepen tot ze in productie breekt. Neem het bewijs mee naar de discussie: hoeveel live versies je vandaag draagt, het werkelijke gebruik van elk, of je kunt zien welke afnemers nog een afgeschaft eindpunt aanroepen en hoe ver van tevoren je laatste uitfasering werd aangekondigd. De concurrerende druk is onderhoudskosten tegenover stabiliteit voor afnemers, en beide zijn echt. Voor partners van ondernemingen onder contractuele servicenivo's en publieke API's die bestuursperiodes en leverancierswissels moeten overleven is het ondersteuningsvenster een verbintenis die het team dat haar aanging kan overleven, dus bepaal wie haar bezit en hoe een uitfasering veilig wordt bewezen voordat die plaatsvindt.

6. **Hoe weten we dat onze ontwikkelaarservaring goed is, of nemen we dat aan omdat de API voor ons werkt?** Dit hoofdstuk kadert elke API als een product waarvan de adoptie afhangt van accurate referentiedocumentatie, quickstarts, voorbeelden, een sandbox, een changelog en een vindbare catalogus. Teams verwarren routinematig "de API functioneert" met "de API is bruikbaar", en de kloof blijkt uit supporttickets, mislukte integraties en afnemers die stilletjes opgeven. Neem meetbare signalen mee in plaats van meningen: tijd tot eerste succesvolle aanroep voor een nieuwe integrator, aantal supporttickets per eindpunt, hoe verouderd de gepubliceerde documentatie is ten opzichte van het live contract en of een nieuweling zichzelf kan bedienen vanuit het portaal zonder je team te mailen. De spanning is dat documentatie en portalen echte inspanning kosten die concurreert met het opleveren van functies, maar in een groot ecosysteem verschuift slechte ontwikkelaarservaring integratiekosten tegelijk naar honderden afnemers. Bij de overheid, waar een open API externe ontwikkelaars bedient met wie je niet kunt coördineren en transparantie vaak verplicht is, is een bruikbare, goed gedocumenteerde, vindbare interface deel van de publieke verantwoordingsplicht, geen luxe.

## Sectorperspectief

**Startup.** Met twee of drie engineers en geen tijd voor ceremonie houd je het contract licht maar echt: één machineleesbare specificatie waartegen je eerste designpartner-klanten kunnen integreren terwijl je bouwt. Zet nog geen API-gateway, catalogus of governanceraad op, maar leg wel de twee gewoonten vast die pijnlijk zijn om later toe te voegen, idempotentiesleutels op schrijfacties en cursorpaginering op lijsten, omdat ze achteraf aanbrengen op een live eindpunt een brekende wijziging is die je je niet kunt veroorloven. Geef de voorkeur aan één interactiestijl, vrijwel altijd REST, zodat je geen protocolwoekering meeneemt in je eerste jaar.

**Kleinbedrijf.** Zonder aparte API-specialist en met een krap budget leun je op tools die documentatie, mocks en clientstubs uit een specificatie genereren, zodat een generalist de interface kan onderhouden zonder diepe protocolexpertise. Weeg kopen tegen bouwen zwaar: een kant-en-klare gateway of API-beheerplatform geeft je ratebeperking, sleutels en een ontwikkelaarsportaal dat je anders met de hand zou moeten bouwen. Houd het oppervlak klein en de conventies consistent, want elk extra eindpunt en elk eenmalig foutformaat is iets wat een dun team voor altijd moet ondersteunen.

**Grote onderneming.** Over veel autonome teams is het centrale probleem consistentie zonder een knelpunt te worden: een gedeelde stijlgids, een API-standaardenreview, een catalogus die interfaces vindbaar maakt en geautomatiseerde controles op achterwaartse compatibiliteit in CI zodat een stille breuk de build laat falen in plaats van een integratie. Bestuur elke API als een product met een benoemde eigenaar, een levenscyclus en een gepubliceerd afschaffingsbeleid, en meet adoptie, supportlast en frequentie van brekende wijzigingen zodat het portfolio gezond blijft. Standaardiseer de interactiestijlen en de versieregels organisatiebreed, want op deze schaal is fragmentatie de dure standaard.

**Overheid.** Aanbestedingsregels, verplichtingen rond open standaarden en publieke verantwoording bepalen elke keuze. Publiceer het contract openlijk, volg de verplichte open standaarden en bied een sandbox en referentiedocumentatie, zodat externe ontwikkelaars met wie je niet kunt coördineren zichzelf kunnen bedienen. Behandel achterwaartse compatibiliteit op lange termijn als beleidseis, omdat integraties bestuursperiodes en leverancierswissels moeten overleven, en maak brekende wijzigingen zeldzaam, zwaar bestuurd en ruim van tevoren aangekondigd. Houd de API en haar documentatie transparant genoeg om publieke en auditscrutinie te doorstaan, en vermijd gesloten formaten die een toekomstig bestuur zouden insluiten.

## Voorbeelden

**Startup.** Een startup in de zaaifase die zijn eerste publieke API oplevert schrijft het contract als machineleesbare specificatie vóór het coderen, zodat zijn twee designpartner-klanten kunnen integreren tegen een mock terwijl de backend nog wordt gebouwd. Zelfs met slechts een handvol afnemers voegt het idempotentiesleutels toe aan het afschrijvingseindpunt en cursorpaginering aan elke lijst, omdat het achteraf aanbrengen ervan zodra partners van de API afhangen een brekende wijziging zou betekenen die het zich niet kan veroorloven. Het contract vooraf kost een dag en bespaart weken heen-en-weer met support.

**Grote onderneming.** Een groot betalingsbedrijf stelt een publieke REST-API open voor duizenden handelaren. Elk schrijfeindpunt accepteert een idempotentiesleutel, zodat een netwerkherhaling nooit een dubbele afschrijving maakt. Elk lijsteindpunt gebruikt cursorpaginering. Fouten dragen stabiele codes die in een publieke referentie zijn gedocumenteerd. Een formeel afschaffingsbeleid garandeert een lang ondersteuningsvenster voor elke versie, met voorafgaande kennisgeving en migratiegidsen. Deze discipline is een concurrentievoordeel: integrators vertrouwen erop dat de API niet onder hen breekt.

**Overheid.** Een nationale digitale dienst publiceert een open API voor burgerdata, volgens verplichte open standaarden en een API-eerst ontwerpproces. Het contract wordt gespecificeerd en beoordeeld vóór de bouw, gepubliceerd in een centrale API-catalogus van de overheid en geserveerd met een sandbox, zodat ontwikkelaars van derden, die niet individueel kunnen worden gecoördineerd, zelfstandig kunnen integreren. Achterwaartse compatibiliteit op lange termijn is een beleidseis, omdat integraties bestuursperiodes en leverancierswissels moeten overleven. Brekende wijzigingen zijn daarom zeldzaam en zwaar bestuurd.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Goed API-ontwerp verlaagt integratiekosten, vaak de grootste kostenpost bij het koppelen van systemen en het onboarden van partners. Met een heldere, stabiele, goed gedocumenteerde API integreren afnemers in dagen zonder één supportticket. Een slechte genereert eindeloze supportlast, mislukte integraties en reputatieschade. Wanneer de API zelf het product is, drijft ontwikkelaarservaring direct adoptie en omzet.

De grootste verborgen kostenpost zijn brekende wijzigingen. Elke brekende wijziging dwingt een gecoördineerde migratie af over alle afnemers, interne teams en externe partners gelijk, en de totale kosten schalen met het aantal afnemers en hoe moeilijk het voor hen is gelijkgeschakeld te bewegen. Vooraf investeren in contract-eerst ontwerp, achterwaartse compatibiliteit en versiediscipline vermijdt deze dure, organisatiebrede migratiegebeurtenissen. Formuleer API-kwaliteit als je met het bestuur praat als de hefboom voor teamautonomie, groei van het partnerecosysteem en het vermijden van kostbare geforceerde migraties. Volg integratietijd, aantal supporttickets en frequentie van brekende wijzigingen als je bewijs.

## Antipatronen en valkuilen

- **API's implementatie-eerst:** de interface lekt interne databasestructuur en verandert wanneer de implementatie verandert.
- **Stille brekende wijzigingen:** een veld herbestemmen of validatie aanscherpen zonder versieverhoging breekt afnemers onvoorspelbaar.
- **Praatzieke interfaces:** ontwerpen die veel roundtrips vereisen voor één logische operatie, wat prestaties en bruikbaarheid schaadt.
- **Inconsistente conventies:** elk eindpunt verzint zijn eigen naamgeving, foutformaat en paginering, zodat clients niet kunnen generaliseren.
- **Geen paginering of ratebeperking:** eindpunten die in testen werken en bezwijken onder echt datavolume of echte belasting.
- **Niet-idempotente schrijfacties:** herhalingen veroorzaken duplicaten. Eén netwerkstoring corrumpeert data.
- **Versiewoekering:** te veel live versies zonder afschaffing, wat het onderhoud vermenigvuldigt tot het onbeheersbaar is.
- **Documentatie als bijzaak:** ongedocumenteerde of verouderde referenties die alle integratiekosten op afnemers afwentelen.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** API's ontstaan uit de implementatie als bijproduct. Er zijn geen gedeelde conventies. De interface lekt interne databasestructuur. Brekende wijzigingen zijn gebruikelijk, niet aangekondigd en worden ontdekt wanneer de integratie van een afnemer faalt.
- **Niveau 2, Ontwikkelen:** Sommige teams volgen basisconventies van REST, versioneren informeel en schrijven documentatie met de hand, maar de praktijk is inconsistent over teams. Idempotentie, paginering en ratebeperking verschijnen op sommige eindpunten en niet op andere. Afnemers leren nog steeds de eigenaardigheden van elke API geval voor geval.
- **Niveau 3, Standaardiseren:** Contract-eerst ontwerp met machineleesbare specificaties is gedocumenteerd en organisatiebreed gehandhaafd. Een gepubliceerd afschaffingsbeleid, consistente foutsemantiek en verplichte idempotentie, cursorpaginering en ratebeperking gelden voor elk nieuw eindpunt. Een gedeelde stijlgids en een API-standaardenreview houden interfaces consistent over teams.
- **Niveau 4, Beheersen:** Het API-portfolio wordt gemeten en gestuurd aan de hand van uitgangswaarden: geautomatiseerde controles op achterwaartse compatibiliteit grinden elke wijziging in CI, en je volgt tijd tot eerste succesvolle aanroep, supporttickets per eindpunt, frequentie van brekende wijzigingen, aantal live versies en gebruik per eindpunt, zodat afschaffing en ontwerpbeslissingen op bewijs rusten in plaats van mening. Elke API is een bestuurd product in een catalogus met een benoemde eigenaar, en statistieken triggeren actie wanneer een service van haar doelen afwijkt.
- **Niveau 5, Orkestreren:** API-strategie wordt continu verbeterd en is over de organisatie geïntegreerd. De catalogus, gateway, versieregels en compatibiliteitspoorten werken als één systeem. De organisatie schaft interfaces routinematig af, consolideert en begrenst ze opnieuw op basis van gemeten adoptie en kosten. Interactiestijl- en versiestandaarden passen zich aan naarmate het ecosysteem, partners en technologie verschuiven. En brekende wijzigingen zijn zeldzaam en goed beheerd.

## Ideeën voor discussie

- Hoe besluit je wanneer een interne API stabiel genoeg is om extern te publiceren?
- Wat is het juiste ondersteuningsvenster voor afgeschafte versies in jouw context, en wie betaalt ervoor?
- Waar moeten GraphQL of gRPC intern REST vervangen, en waar zouden ze meer complexiteit dan waarde toevoegen?
- Hoe dwing je API-consistentie af over veel autonome teams zonder een knelpunt te worden?
- Hoe moeten voor AI bruikbare API's en agent-toolinterfaces je ontwerpconventies veranderen?
- Welke geautomatiseerde controles kunnen achterwaarts onverenigbare wijzigingen opvangen voordat ze worden opgeleverd?

## Belangrijkste inzichten

- Ontwerp eerst het contract. De API is een product en een langlevende belofte.
- Achterwaartse compatibiliteit beschermt afnemers. Brekende wijzigingen vragen nieuwe versies en migratiepaden.
- Kies REST, GraphQL, gRPC of gebeurtenissen naar interactiepasvorm, niet naar mode.
- Bouw idempotentie, paginering, ratebeperking en consistente fouten vanaf dag één in.
- Bestuur API's als producten met eigenaren, catalogi en sterke ontwikkelaarservaring.

## Referenties en verder lezen

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
