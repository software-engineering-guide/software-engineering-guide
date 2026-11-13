# 10.12 Open source tegenover closed source

## Overzicht en motivatie

Bijna elk modern systeem is een mengeling van software die je schreef, software die je kocht en software die je gratis nam. Twee van die drie brengen een fundamentele keuze mee: is de software **open source** of **closed source**? **[Open-sourcesoftware](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** wordt verspreid onder een licentie die iedereen het recht geeft de broncode te gebruiken, bestuderen, wijzigen en herdistribueren, de voor mensen leesbare instructies die het programma definiëren. **Closed-sourcesoftware**, ook wel **[eigen software](https://en.wikipedia.org/wiki/Proprietary_software)** genoemd, wordt verspreid als afgewerkt product waarvan de leverancier de broncode privé houdt. Je krijgt het recht haar onder een licentie te draaien, maar niet om te inspecteren of te wijzigen hoe ze werkt. Een tussencategorie, **[source-available software](https://en.wikipedia.org/wiki/Source-available_software)**, publiceert de bron om te lezen maar beperkt gebruik, wijziging of herdistributie. Ze is *zichtbaar* maar niet *open* volgens de standaarddefinitie.

Twee verduidelijkingen doen ertoe voordat je ze vergelijkt. Ten eerste is "gratis" dubbelzinnig. De gemeenschap onderscheidt **gratis-als-in-vrijheid** (de vrijheid te wijzigen en te delen, soms "libre" geschreven) van **gratis-als-in-prijs** (nul kosten, "gratis"). Open source gaat over vrijheid, niet noodzakelijk over prijs. Ten tweede vallen open-sourcelicenties in twee families uiteen. **[Permissieve licenties](https://en.wikipedia.org/wiki/Permissive_software_license)** (zoals [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD en Apache 2.0) laten je bijna alles doen, inclusief de code in een gesloten product inbedden. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft)-licenties** (zoals de [GNU General Public Licence](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) vereisen dat afgeleide werken die je distribueert ook onder dezelfde open voorwaarden worden uitgebracht, een wederkerigheidsregel die door critici soms "viraal" en door voorstanders "share-alike" wordt genoemd.

Dit hoofdstuk bekijkt de keuze van twee kanten. Als **afnemer** beslis je of je een open-source- of eigen component overneemt. Als **producent** beslis je of je software die je bouwde als open source uitbrengt. Voor grote ondernemingen en vooral de overheid dragen beide beslissingen gewicht ver voorbij het licentiebestand. Ze raken inkoop (hoofdstuk 10.3), digitale soevereiniteit (hoofdstuk 10.11), beveiliging van de toeleveringsketen (hoofdstuk 4.2), interoperabiliteit (hoofdstuk 3.8) en de afweging tussen bouwen en kopen (hoofdstuk 6.1).

## Kernprincipes

- **De licentie, niet de prijs, definieert "open."** Lees de licentie. Gratis en open source zijn verschillende beweringen.
- **Geen van beide modellen is inherent veiliger.** Beide kunnen uitstekend of nalatig zijn. De praktijken rond de code tellen meer dan haar openheid.
- **Openheid is een hefboom om afhankelijkheid te verminderen.** Toegang tot de bron is de ultieme bescherming tegen [afhankelijkheid van een leverancier](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Je bezit altijd de operationele last.** Gratis te verkrijgen is nooit gratis te draaien. [Total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) vertelt het echte verhaal.
- **Onderscheidende zaken blijven gesloten. Commodities kunnen opengaan.** Maak open source wat je niet onderscheidt. Bewaak wat dat wel doet.
- **Copyleft heeft gevolgen.** Begrijp wederkerigheidsverplichtingen voordat je copyleftcode inbedt in een product dat je distribueert.
- **Een levende gemeenschap is een bezit. Een verlaten repository is een verplichting.** Beoordeel het project, niet alleen de licentie.

## Aanbevelingen

### Beoordeel een component op het project, niet alleen de licentie

Beoordeel voordat je enige afhankelijkheid overneemt, open source of eigen, haar gezondheid: releaseritme, aantal en diversiteit van beheerders, responsiviteit op beveiligingsmeldingen en breedte van adoptie. Een open-sourcebibliotheek met één beheerder en een kleine eigen leverancier dragen hetzelfde **bus-factorrisico** (het gevaar dat een project instort als één of enkele sleutelpersonen vertrekken). Geef de voorkeur aan componenten met een brede basis van bijdragers of een financieel gezonde leverancier en leg de beoordeling vast als onderdeel van due diligence (hoofdstuk 10.2, 4.2).

### Lees en volg licenties als eersterangs verplichting

Onderhoud een inventaris van elke component en haar licentie en dwing een beleid af over welke licentiefamilies voor welk gebruik aanvaardbaar zijn. Het cruciale onderscheid is copyleft. **Permissieve** code (MIT, Apache 2.0) kan over het algemeen vrij in gesloten producten worden ingebed. **Sterke copyleft** (GPL) kan je verplichten je eigen gedistribueerde afgeleide onder dezelfde voorwaarden uit te brengen. Gebruik geautomatiseerde **software composition analysis (SCA)**, tools die je afhankelijkheden scannen om componenten, licenties en bekende kwetsbaarheden te identificeren, en genereer een **software bill of materials (SBOM)**, een formele lijst van elke component in een product (hoofdstuk 10.3, 4.2).

### Beoordeel beveiliging op praktijk, niet op openheid

Neem niet aan dat open source veilig is vanwege het **"vele ogen"-argument** ([de wet van Linus](https://en.wikipedia.org/wiki/Linus%27s_law): "met genoeg ogen zijn alle bugs oppervlakkig"). En neem niet aan dat eigen code veilig is door **[security-through-obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)** (het foute geloof dat de bron verbergen fouten verbergt). Vele ogen helpen alleen als bekwame mensen werkelijk kijken, en veel veelgebruikte projecten worden dun onderhouden. Beide modellen dragen **risico in de toeleveringsketen**: open source via gecompromitteerde of verlaten afhankelijkheden, eigen via ondoorzichtige code en updatekanalen die je niet kunt inspecteren. Pin versies, verifieer herkomst, scan continu en bewaak adviezen ongeacht het model (hoofdstuk 4.2).

### Ontwerp voor uitstap en interoperabiliteit

Geef de voorkeur aan componenten die open standaarden en overdraagbare dataformaten spreken, zodat je ze later kunt vervangen (hoofdstuk 3.8, 10.11). Met open source krijg je de ultieme uitstap: als een project stilvalt kun je het **[forken](https://en.wikipedia.org/wiki/Fork_(software_development))** (je eigen kopie maken en onderhouden). Onderhandel bij eigen software vooraf over bescherming: data-export in open formaten, gedocumenteerde API's en **[source-code-escrow](https://en.wikipedia.org/wiki/Source_code_escrow)** (een juridische regeling waarbij de leverancier de bron bij een derde deponeert, aan jou vrijgegeven als de leverancier faalt). Ontwerp zo dat geen enkele component, van beide soorten, je systeem kan gijzelen.

### Weeg total cost of ownership, niet kopprijs

Vergelijk opties op **total cost of ownership (TCO)**, de volledige levenslange kosten inclusief aanschaf, integratie, beheer, ondersteuning, training, upgrades en uiteindelijke vervanging, in plaats van alleen licentiekosten. Open source ruilt vaak licentiekosten tegen hogere operationele en personeelskosten. Eigen software ruilt vaak voorspelbare abonnementskosten tegen afhankelijkheid en minder controle. Neem de kosten van het model zelf mee: zelfondersteunende open source vraagt intern vermogen, terwijl eigen software capaciteit voor leveranciersbeheer vraagt.

### Maak als producent open source wat je niet onderscheidt

Deel je eigen software in naar wat je concurrentie- of missievoordeel geeft en wat ongedifferentieerd leidingwerk is. Houd de onderscheidende zaken eigen. Overweeg de commodity-infrastructuur als open source uit te brengen, waar een gemeenschap onderhoud en verbetering kan delen. Weeg voor de overheid **"public money, public code"** (het principe dat software betaald met belastinggeld standaard publiek beschikbaar moet zijn) als drijfveer voor transparantie, hergebruik en soevereiniteit (hoofdstuk 10.5, 10.11). Kies de licentie bewust: permissief om adoptie te maximaliseren, copyleft om het ecosysteem open te houden.

## Afwegingen: voor- en nadelen

| Dimensie | Open source | Closed / eigen |
|---|---|---|
| **Aanschafkosten** | Meestal nul om te verkrijgen | Licentie- of abonnementskosten |
| **Total cost of ownership** | Kosten verschuiven naar beheer en personeel | Voorspelbaarder, maar afhankelijkheidspremie |
| **Controle en aanpassing** | Volledig: je kunt de bron lezen en wijzigen | Beperkt tot wat de leverancier blootstelt |
| **Ondersteuning en verantwoording** | Gemeenschap, of betaalde derde. Geen enkele aanspreekbare partij | Contractuele ondersteuning en een duidelijke verantwoordelijke partij |
| **Beveiligingshouding** | Controleerbaar. "Vele ogen" als echt onderhouden | Door leverancier beheerd. Ondoorzichtig. Obscuriteit is geen bescherming |
| **Levensduur / verlating** | Kan worden geforkt als onderhouden. Kan toch verdorren | Hangt af van levensvatbaarheid en roadmap van de leverancier |
| **Afhankelijkheid van een leverancier** | Laag: bron en open formaten maken uitstap mogelijk | Hoog tenzij verzacht door standaarden en escrow |
| **Ecosysteem** | Open gemeenschap en interoperabiliteit | Gecureerd, geïntegreerd, soms ommuurd |

De terugkerende spanning is **controle tegenover gemak en verantwoording**. Open source maximaliseert controle, controleerbaarheid en vrijheid van afhankelijkheid, maar vraagt je het vermogen, de integratie en de ondersteuning zelf te leveren. Eigen software levert een ondersteund, geïntegreerd, verantwoordelijk product met een af te dwingen contract, maar staat controle af en nodigt afhankelijkheid uit. De oplossing is zelden alles-of-niets. De meeste volwassen landschappen mengen open-sourcefundamenten met eigen systemen waar ondersteuning, verantwoording of gespecialiseerd vermogen de afweging rechtvaardigt.

## Vragen om met je team te bespreken

1. **Dwingen we een licentiebeleid af met geautomatiseerde SCA en SBOM's in de pijplijn, vooral om sterke copyleft te vangen voordat die wordt uitgeleverd?** Een GPL-bibliotheek inbedden in een gedistribueerd eigen product kan je verplichten je eigen bron uit te brengen, en die verrassing komt meestal laat boven water, wanneer het duur is terug te draaien. Onderhoud een inventaris van elke component en haar licentie, dwing af welke licentiefamilies voor welk gebruik aanvaardbaar zijn en draai software composition analysis automatisch zodat de pijplijn schendingen blokkeert in plaats van een jurist ze bij uitlevering vangt. Genereer als vanzelfsprekend een SBOM. Voor een groot of overheidslandschap is dit ook hygiëne van de toeleveringsketen en vaak een inkoopeis. Neem je huidige licentie-inventaris mee, of het feit dat je er geen hebt, en besluit wie het beleid bezit.

2. **Beoordelen we bij het overnemen van een afhankelijkheid projectgezondheid en bus-factor als due diligence?** Een open-sourcebibliotheek met één beheerder en een kleine eigen leverancier dragen hetzelfde risico: het project stort in als één of enkele sleutelpersonen vertrekken. Beoordeel voordat je iets overneemt het releaseritme, het aantal en de diversiteit van beheerders, de responsiviteit op beveiligingsmeldingen en de breedte van adoptie, en leg de beoordeling vast. Geen van beide modellen is standaard veiliger. "Vele ogen" helpt alleen als bekwame mensen werkelijk kijken, en veel veelgebruikte projecten worden dun onderhouden. Neem de drie of vier afhankelijkheden mee waarop je product het meest leunt en vraag voor elk hoeveel mensen moeten weglopen voordat het jouw probleem wordt. Als je dat niet kunt beantwoorden, is dat de beoordeling die je jezelf verschuldigd bent.

3. **Regelen we bij het kopen van eigen software uitstapbescherming vooraf?** Eigen software biedt verantwoording en gemak in ruil voor controle, en de verborgen kost is afhankelijkheid: wisselkosten waarmee een leverancier prijzen kan verhogen of de dienstverlening kan verslechteren met weinig verhaal. Onderhandel over de bescherming voordat je tekent, wanneer je nog hefboom hebt: data-export in open formaten, gedocumenteerde API's en source-code-escrow die de bron vrijgeeft als de leverancier faalt. Bij open source is je uitstap het vermogen te forken. Bij eigen software moet je de uitstap in het contract schrijven. Neem je meest kritieke eigen systemen mee en vraag wat er werkelijk gebeurt als de leverancier de prijs verdubbelt of failliet gaat. Als het antwoord "we zitten vast" is, repareer het contract bij verlenging.

4. **Hoe beslissen we voor de software die we zelf bouwen wat we als open source uitbrengen en wat gesloten houden, en wie heeft de bevoegdheid die keuze te maken?** Doe dit fout in de ene richting en je geeft juist de code weg die je onderscheidt. Doe het fout in de andere en je hamstert commodity-leidingwerk waarvan een gemeenschap het onderhoud graag zou delen. De concurrerende druk is echt: engineers willen het wervings- en reputatievoordeel van een publieke repository, terwijl product en juridische zaken zich zorgen maken over rivalen een voordeel geven of een beveiligingsgevoelige heuristiek blootleggen. Neem een eerlijke indeling van je systemen mee in missieonderscheidend tegenover ongedifferentieerde infrastructuur en noem de persoon of raad die een release goedkeurt, want een ad-hocbeslissing genomen door wie de repository pushte is hoe kroonjuwelen lekken. Voor een grote onderneming is de vraag portfoliostrategie, en voor de overheid botst ze met "public money, public code", het principe dat met belastinggeld gefinancierde software standaard publiek moet zijn, dus besluit vooraf welke uitzonderingen (nationale veiligheid, fraudedetectie, persoonsgegevens) rechtvaardigen dat code gesloten blijft.

5. **Vangen onze vergelijkingen tussen bouwen en kopen de volledige total cost of ownership, of behandelen we nog steeds een licentiekost van nul als kosten van nul?** De meest gangbare financiële fout met open source is "gratis te verkrijgen" lezen als "gratis te draaien", en dan ontdekken dat integratie, beheer, beveiligingsrespons en betaalde ondersteuning elke licentie die je vermeed overtreffen. De spanning is dat een eigen abonnement duur oogt op de factuur terwijl het een afhankelijkheidspremie verbergt, en een open component gratis oogt op de factuur terwijl ze kosten op je eigen personeel verschuift. Neem een vergelijkbaar TCO-model mee voor twee of drie echte beslissingen: aanschaf, integratie, beheer, ondersteuning, training, upgrades, beveiligingsrespons en uiteindelijke vervanging, geprijsd over de volledige levensduur in plaats van het eerste jaar. Voeg in een landschap van onderneming of overheid de kosten van het bedrijfsmodel zelf toe, aangezien zelfondersteunende open source intern vermogen vraagt dat je moet werven en behouden, en behandel een vergelijking die die regels weglaat als bewijs, niet als analyse.

6. **Beoordelen we de beveiliging van een component op haar praktijken, of leunen we op het openheidslabel, of dat nu "vele ogen" is of de geheimhouding van gesloten code?** Beide standaarden zijn valstrikken: "vele ogen" beschermt je alleen wanneer bekwame mensen de code werkelijk beoordelen, en veel veelgebruikte open projecten draaien op één uitgeputte beheerder, terwijl gesloten bron die erop leunt dat aanvallers haar niet zien security through obscurity is, geen maatregel. Het debat doet ertoe omdat het verandert waar je schaarse beveiligingsinspanning heen gaat, en het eerlijke antwoord is dat beide modellen risico in de toeleveringsketen dragen, open source via gecompromitteerde of verlaten afhankelijkheden en eigen via ondoorzichtige updatekanalen die je niet kunt inspecteren. Neem bewijs mee voor je meest kritieke componenten: wie ze werkelijk beoordeelt, hoe snel adviezen worden gepatcht, of versies zijn gepind en herkomst geverifieerd en of je een SBOM genereert. Koppel dit voor een groot of overheidslandschap aan inkoop en verplichtingen tot continu scannen, want een toezichthouder zal vragen wat je inspecteerde, niet of de bron publiek was.

## Sectorperspectief

**Startup.** Met weinig runway bouw je op open-sourcefundamenten omdat je geen licentiekosten kunt betalen en de vrijheid wilt te forken als een project stilvalt. Draai een compositieanalyse voordat je uitlevert zodat een sterke-copyleftbibliotheek je niet stilletjes verplicht je eigen bron te publiceren, en houd je ene echte onderscheidende zaak strikt gesloten. Maak een klein, niet-kritiek hulpmiddel open source als het helpt bij werven, maar bemand geen onderhoudslast die je niet kunt dragen.

**Kleinbedrijf.** Zonder intern juridisch of platformspecialist behandel je de licentie als risico dat je niet verkeerd mag lezen in plaats van een onderwerp dat je kunt beheersen. Geef de voorkeur aan ondersteunde eigen tools of commerciële open-sourcedistributies waar een leverancier patches en verantwoording bezit, want een stack zelf ondersteunen die je niet kunt beheren is valse zuinigheid. Wanneer je een gratis component overneemt, controleer dan dat haar licentie je gebruik toestaat en dat het project werkelijk wordt onderhouden, niet verlaten.

**Grote onderneming.** Op schaal is het probleem consistentie over veel teams: een geschreven licentiebeleid, geautomatiseerde software composition analysis en SBOM-generatie in elke pijplijn, en op TCO gebaseerde beslissingen tussen bouwen en kopen in plaats van gewoonte per team. Beheer open en eigen software als één portfolio, standaardiseer uitstapbescherming zoals open formaten en source-code-escrow in de inkoop en volg de gezondheid van kritieke afhankelijkheden zodat één verlaten project geen incident wordt. Bestuur ook de producentenkant, met een heldere regel over wat de organisatie als open source uitbrengt tegenover gesloten houdt.

**Overheid.** Aanbestedingsregels, transparantieplichten en publieke verantwoording geven elke keuze vorm. Weeg "public money, public code", het principe dat met belastinggeld gefinancierde software standaard publiek moet zijn, om hergebruik over instanties en digitale soevereiniteit te bevorderen, terwijl je smalle uitzonderingen uitsnijdt voor beveiligingsgevoelige code of code met persoonsgegevens. Eis van elke eigen leverancier data-export in open formaten en source-code-escrow zodat een leveranciersfalen een publieke dienst niet kan laten stranden, en publiceer de niet-gevoelige bron zodat burgers de regels kunnen controleren die hen besturen.

## Voorbeelden

**Startup.** Een startup met drie oprichters bouwt haar hele product op open-sourcefundamenten (Linux, een open-sourcedatabase, een webframework) omdat ze geen licentiekosten kan betalen en de vrijheid wil te forken als een project stilvalt. Vóór het uitleveren draait een oprichter een compositieanalyse en vangt een sterke-copyleftbibliotheek die hen had verplicht hun eigen matchingalgoritme te publiceren, dus ruilen ze haar voor een permissief gelicentieerd equivalent. Ze houden dat algoritme, hun enige onderscheidende zaak, strikt gesloten en maken alleen een klein intern logginghulpmiddel open source om goodwill te bouwen en engineers aan te trekken.

**Grote onderneming.** Een grote verzekeraar draait haar kernplatform op open-sourcefundamenten: Linux, een veelgebruikte open-sourcedatabase en een containerorkestrator. Maar ze koopt een eigen actuariële modelleringssuite, omdat de domeinexpertise, wettelijke certificeringen en het ondersteuningscontract van de leverancier de vergoeding waard zijn en er geen vergelijkbaar open alternatief is. Ze betaalt een abonnement voor **commerciële open source** (door leveranciers ondersteunde distributies van de open componenten) om verantwoording en patches op het leidingwerk te krijgen, terwijl ze het prijsalgoritme dat haar onderscheidt strikt eigen en intern houdt. TCO-analyse (hoofdstuk 10.10) drijft elke keuze in plaats van ideologie.

**Overheid.** Een nationale belastingdienst bouwt onder een beleid van "public money, public code" een nieuwe dienst voor uitkeringsgeschiktheid op open-sourcecomponenten en open standaarden (hoofdstuk 3.8), zodat andere agentschappen haar kunnen hergebruiken en burgers de regels kunnen controleren. Ze publiceert de niet-gevoelige code in een publieke repository en houdt alleen fraudedetectieheuristieken om beveiligingsredenen gesloten. Dit vermindert afhankelijkheid van leveranciers en bevordert digitale soevereiniteit (hoofdstuk 10.11). Inkoopregels (hoofdstuk 10.3) eisen van elke eigen component data-export in open formaten en source-code-escrow om continuïteit te garanderen als de leverancier faalt.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De financiële aantrekkingskracht van open source, het ontbreken van een licentiekost, is het minst betrouwbare deel van de zaak, omdat aanschaf een klein deel van de TCO is. De duurzame rendementen zijn strategisch: vrijheid van afhankelijkheid (het vermogen een leverancier te wisselen of te laten vallen zonder te herarchitecteren), controleerbaarheid voor beveiliging en compliance, snellere adoptie omdat engineers kunnen proberen voor ze zich committeren en gedeeld onderhoud van commoditycode over een hele sector. De compenserende kosten zijn echt. Je moet integratie, beheer, beveiligingsrespons en vaak betaalde ondersteuning leveren, en een slecht gekozen onderhoudsloos project kan in incidenten meer kosten dan enige licentie zou hebben gedaan.

De businesscase van eigen software is verantwoording en gemak: één leverancier verantwoordelijk voor het product, een ondersteuningscontract dat je kunt afdwingen, geïntegreerde functies en voorspelbaar begroten. De verborgen kost is afhankelijkheid, de wisselkosten waarmee een leverancier prijzen kan verhogen of dienstverlening kan verslechteren met weinig verhaal, plus afhankelijkheid van de solvabiliteit en roadmap van de leverancier. Gangbare **bedrijfsmodellen** vervagen de lijn: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (een open basis met eigen betaalde uitbreidingen), **dubbele licentiëring** (dezelfde code aangeboden onder zowel een copyleft- als een betaalde commerciële licentie), **[software as a service](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (de software draait als gehoste dienst die je huurt, waar de bron irrelevant kan zijn omdat je het binaire bestand nooit bezit) en **ondersteunings-/abonnementsmodellen** die dienstverlening verkopen rond anders gratis code.

Voor een producent kan de ROI van **je eigen niet-onderscheidende software als open source uitbrengen** aanzienlijk zijn. Externe bijdragers verminderen je onderhoudslast. Het project wordt een wervings- en reputatiebezit. Externe adoptie maakt jouw standaard de feitelijke. Voor de overheid levert het transparantie en hergebruik over de publieke sector. De strategische regel is eenvoudig: maak de commodity open source om haar kosten te delen en een ecosysteem te laten groeien, en houd het onderscheidende gesloten om het voordeel te beschermen dat al het andere financiert.

## Antipatronen en valkuilen

- **"Gratis betekent gratis":** nul aanschafkosten behandelen als nul TCO en dan beheer en ondersteuning onderfinancieren.
- **Licentieblindheid:** sterke-copyleftcode inbedden in een gedistribueerd eigen product en verplichtingen triggeren waarvoor je nooit plande.
- **Geloof in "vele ogen":** aannemen dat een open project wordt geaudit terwijl het één overbelaste beheerder heeft en geen beveiligingsreview.
- **Security-through-obscurity:** geloven dat gesloten bron veilig is simpelweg omdat aanvallers haar niet kunnen lezen.
- **Ideologisch absolutisme:** "alles open" of "alles eigen" voorschrijven in plaats van per component te kiezen op verdienste en TCO.
- **Herkomst negeren:** afhankelijkheden binnenhalen zonder SBOM, versies pinnen of verificatie van de toeleveringsketen (hoofdstuk 4.2).
- **De kroonjuwelen open source maken:** juist de code uitbrengen die je onderscheidt, wat je voordeel weggeeft.
- **Forken en vergeten:** een verlaten project forken zonder het vermogen de fork werkelijk te onderhouden.

## Volwassenheidsmodel

**Niveau 1 (Initiëren).** Open-source- en eigen componenten komen ad hoc het landschap binnen. Licenties zijn ongelezen, er is geen inventaris of SBOM en de keuze tussen modellen wordt uit gewoonte of prijs alleen gemaakt. Verlating en licentierisico komen pas boven water wanneer iets breekt, en elk team reageert voor zichzelf.

**Niveau 2 (Ontwikkelen).** Sommige teams beginnen basispraktijken: een inventaris van componenten en licenties, een ruw beeld van aanvaardbare licenties en incidentele software composition analysis. Beslissingen over bouwen of kopen en open of gesloten worden opgeschreven, maar de discipline is ongelijk en inconsistent van team tot team, dus een copyleft- of bus-factorverrassing kan nog steeds binnenglippen waar de gewoonte niet is aangeslagen.

**Niveau 3 (Standaardiseren).** Een gedocumenteerd kader bestuurt zowel gebruik als productie organisatiebreed. Componenten worden gekozen op TCO en projectgezondheid, licenties worden automatisch in de pijplijn afgedwongen zodat schendingen een build blokkeren, SBOM's worden als vanzelfsprekend gegenereerd en een expliciet beleid stelt wat de organisatie als open source uitbrengt tegenover gesloten houdt. Uitstapbescherming zoals open formaten en source-code-escrow is standaard in de inkoop, en elk team volgt dezelfde regels in plaats van zijn eigen.

**Niveau 4 (Beheersen).** Het programma wordt gemeten en beheerst tegen uitgangswaarden. De organisatie volgt statistieken zoals SBOM-dekking over producten, het aandeel afhankelijkheden dat beleid schendt, gemiddelde tijd om een bekendgemaakte afhankelijkheidskwetsbaarheid te patchen, bus-factor- en gezondheidsscores voor kritieke projecten en gerealiseerde TCO tegen de schatting die elke keuze rechtvaardigde. Drempels triggeren actie: een component waarvan het onderhoud stokt of waarvan de patchlatentie voorbij het doel afdrijft wordt op bewijs gemarkeerd voor vervanging, en beslissingen over open of gesloten en bouwen of kopen worden getoetst aan de getallen in plaats van uit gewoonte verdedigd.

**Niveau 5 (Orkestreren).** Open-sourcestrategie is een bewust bedrijfsvermogen, over de organisatie geïntegreerd en continu verbeterd. De organisatie draagt bij aan en beheert soms de projecten waarvan ze afhangt, maakt haar niet-onderscheidende software als vanzelfsprekend open source en voedt afhankelijkheidsgezondheids- en TCO-data terug in inkoop, beveiliging en productplanning. Ze herbalanceert routinematig haar portfolio van open en eigen software, zich aanpassend aan verschuivingen in kosten, risico, soevereiniteit en strategisch voordeel voordat ze een crisis afdwingen.

## Ideeën voor discussie

- Waar in je landschap zou het verlies van één leverancier of beheerder existentieel zijn, en wat is je uitstapplan?
- Welke van je eigen systemen zijn commodities die je als open source kon uitbrengen, en welke zijn echte onderscheidende zaken om te beschermen?
- Behandelt je organisatie "vele ogen" als echte beveiligingsmaatregel of als onderzochte aanname?
- Voor lezers in de publieke sector: wat zou een standaard van "public money, public code" veranderen in je volgende aanbesteding?
- Hoe goed vangen je TCO-vergelijkingen de operationele en ondersteuningskosten die open source op jou verschuift?

## Belangrijkste inzichten

- **Open tegenover gesloten wordt bepaald door de licentie**, niet door de prijs. Ken het verschil tussen gratis-als-in-vrijheid en gratis-als-in-prijs, en tussen permissief en copyleft.
- **Geen van beide modellen is inherent veiliger of goedkoper.** Beoordeel de praktijken van het project en haar volledige TCO, niet het openheidslabel.
- **Openheid is het sterkste tegengif tegen afhankelijkheid**, met controleerbaarheid, overdraagbaarheid en het vermogen te forken. Eigen software biedt verantwoording en gemak in ruil voor controle.
- **Beslis per component op verdienste**, en meng modellen bewust in plaats van uit ideologie.
- **Maak als producent de commodity open source en houd het onderscheidende gesloten**, en weeg bij de overheid "public money, public code" voor transparantie, hergebruik en soevereiniteit.

## Referenties en verder lezen

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
