# 10.3 Inkoop, open source en licenties

## Overzicht en motivatie

Bijna elk modern softwaresysteem is grotendeels samengesteld uit componenten die iemand anders schreef. [Open-sourcesoftware](https://en.wikipedia.org/wiki/Open-source_software) vormt het fundament van besturingssystemen, talen, frameworks, databases en cloudinfrastructuur. Ze komt de onderneming op twee manieren binnen: via bewuste [inkoop](https://en.wikipedia.org/wiki/Procurement) en via achteloze `import`-regels van individuele ontwikkelaars. Dit hoofdstuk gaat over dat gebruik (en, waar het past, bijdragen) bewust doen. Dat betekent een strategie, licentienaleving, begrip van verplichtingen en copyleft-risico en een plan voor het onvermijdelijke [einde van de levensduur](https://en.wikipedia.org/wiki/End-of-life_(product)) van de componenten waarvan je afhangt.

Voor grote teams zijn de inzetten tegelijk juridisch, operationeel en strategisch. Juridisch zijn open-source-[licenties](https://en.wikipedia.org/wiki/Software_license) afdwingbare contracten met echte verplichtingen. [Copyleft](https://en.wikipedia.org/wiki/Copyleft) (licentiëring die kan eisen dat afgeleide werken onder dezelfde voorwaarden worden gedeeld) verkeerd doen kan in het slechtste geval openbaarmaking van eigen broncode afdwingen of een rechtszaak uitlokken. Licentieschendingen kunnen zelfs een overname of beursgang blokkeren tijdens [due diligence](https://en.wikipedia.org/wiki/Due_diligence). Operationeel rotten onbeheerde afhankelijkheden: componenten worden niet meer onderhouden, stapelen kwetsbaarheden op en bereiken het einde van hun levensduur terwijl ze nog diep in productie begraven zitten. Strategisch is open source meer dan een kostenbesparende invoer. Het is een manier om [afhankelijkheid van een leverancier](https://en.wikipedia.org/wiki/Vendor_lock-in) te vermijden, talent aan te trekken en de ecosystemen te vormen waarvan je afhangt, voordelen die je alleen vangt als je er bewust mee bezig bent.

De overheid heeft een extra dimensie. Veel jurisdicties hebben nu expliciet beleid dat open source, open standaarden en het delen van code tussen instanties begunstigt. Dit wordt vaak uitgedrukt als "public money, public code": het principe dat software betaald met belastinggeld standaard beschikbaar moet zijn voor het publiek. Dus engineers in de publieke sector moeten zowel licentienaleving als actieve mandaten om open source te verkiezen, te publiceren en te hergebruiken doorlopen. Dit hoofdstuk wil dit alles op schaal beheersbaar maken.

## Kernprincipes

- **Open source is een toeleveringsketen, geen gratis spul.** Behandel gebruikte componenten met dezelfde nauwgezetheid als elke kritieke leverancier.
- **Licenties zijn verplichtingen, geen toestemming om te negeren.** Elke afhankelijkheid draagt voorwaarden. Ken ze voordat je uitlevert.
- **Copyleft is een ontwerpbeperking, geen taboe.** Copyleftlicenties zijn bruikbaar en waardevol. Ze vereisen alleen dat je begrijpt hoe je software combineert en distribueert.
- **Gebruik bewust, draag strategisch bij.** Besluit wat je binnenhaalt en investeer, waar het je dient, in bijdragen aan upstream in plaats van forken.
- **Inventariseer alles.** Je kunt niet voldoen aan, beveiligen of bijwerken wat je niet ziet. Een SBOM (software bill of materials, een complete inventaris van de componenten in je software) is het minimum.
- **Plan het einde van de levensduur vanaf het begin.** Elke afhankelijkheid wordt ooit niet meer onderhouden. Ken je uitweg voordat je tot een gedwongen wordt.
- **Bij de overheid, standaard open.** Geef de voorkeur aan [open standaarden](https://en.wikipedia.org/wiki/Open_standard) en open source, en publiceer code betaald met publiek geld tenzij er een specifieke reden is om het niet te doen.

## Aanbevelingen

### Stel een open-sourcestrategie en gebruiksbeleid vast

Publiceer een helder beleid voor hoe ontwikkelaars open source in de organisatie mogen brengen: welke licenties vooraf zijn goedgekeurd, welke review vereisen en welke voor jouw gebruiksgevallen verboden zijn. Bied een snel, wrijvingsarm goedkeuringspad. Een beleid dat trager is dan code kopiëren wordt gewoon genegeerd. Onderscheid contexten, want dezelfde licentie gedraagt zich anders wanneer een component intern als service wordt gebruikt, wordt ingebed in een gedistribueerd product of wordt gelinkt in een eigen applicatie. Maak het makkelijke pad het conforme pad: een gecureerde interne repository van gecontroleerde componenten, geautomatiseerd scannen in de pijplijn en heldere richtlijnen die ontwikkelaars kunnen volgen zonder voor routinegevallen een jurist te bellen.

### Beheer licentienaleving, verplichtingen en copyleft-risico

Leer de families van licenties en hun verplichtingen kennen. [Permissieve licenties](https://en.wikipedia.org/wiki/Permissive_software_license) (zoals MIT, BSD en Apache 2.0) vereisen vooral naamsvermelding en behoud van mededelingen. Apache 2.0 voegt een expliciete patentverlening toe. Zwakke copyleft (zoals [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) en MPL) vereist dat je wijzigingen aan de gedekte bestanden deelt maar laat je meestal combineren met eigen code. Sterke copyleft (zoals [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) kan eisen dat het hele gedistribueerde werk onder dezelfde voorwaarden wordt aangeboden. Netwerkcopyleft ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) breidt die verplichting uit tot software die over een netwerk wordt aangeboden, niet slechts als binaire bestanden gedistribueerd. De verplichtingen die het meest tellen hangen af van twee dingen: of je de software distribueert en hoe nauw je componenten combineert. Automatiseer naleving: scan afhankelijkheden op licenties, genereer en lever de vereiste naamsvermeldings- en mededelingsbestanden en poort de build op beleid zodat een verboden licentie niet ongemerkt in productie komt.

### Richt een Open Source Program Office (OSPO) in

Als je open source op schaal gebruikt, creëer dan een centraal punt, een OSPO, dat open-sourcestrategie, beleid, compliancetooling, bijdragebestuur en gemeenschapsrelaties bezit. Het OSPO beteugelt de chaos van elk team dat zijn eigen beslissingen neemt. Het biedt expertise die individuele teams niet kunnen onderhouden. En het vangt strategische waarde: beslissen in welke projecten te investeren, wanneer aan upstream bij te dragen en hoe je je eigen open-sourceprojecten goed uitbrengt. Zelfs een klein OSPO (soms één persoon plus een multidisciplinaire werkgroep) verbetert de consistentie dramatisch en vermindert juridisch risico vergeleken met een vrijbuiterij.

### Bestuur bijdragen en, waar passend, publicatie

Besluit bewust wanneer je teruggeeft. Reparaties en functies upstreamen naar projecten waarvan je afhangt vermindert je onderhoudslast, omdat je ophoudt eigen patches mee te dragen. Het bouwt ook goodwill en invloed en versterkt componenten die voor jou kritiek zijn. Geef ontwikkelaars een helder, snel proces voor goedgekeurde bijdragen, inclusief hoe intellectueel eigendom en bijdrageovereenkomsten worden afgehandeld. Wanneer je je eigen open-sourceprojecten uitbrengt, doe het goed: kies een passende licentie, documenteer het bestuur en committeer je aan rentmeesterschap. Een verlaten project schaadt je reputatie meer dan geen project.

### Voldoe aan open-sourcemandaten en "public money, public code" bij de overheid

Teams in de publieke sector moeten openheid als standaard behandelen. Geef de voorkeur aan open standaarden om afhankelijkheid te vermijden en over instanties en leveranciers heen te werken. Publiceer broncode ontwikkeld met publieke middelen openlijk, tenzij een specifieke, gedocumenteerde uitzondering geldt: voor beveiligingsgevoelige componenten, rechten van derden of privacyzorgen. Hergebruik voor je bouwt: controleer of een andere instantie al geschikte code heeft uitgebracht. Bak deze verwachtingen in de inkoop, zodat leveranciers open, herbruikbare, goed gedocumenteerde code opleveren waarbij de overheid passende rechten houdt, in plaats van eigen zwarte dozen die het agentschap niet kan onderhouden of delen.

### Beheer afhankelijkheden en software aan het einde van de levensduur

Onderhoud een live inventaris (SBOM) van elke component en haar versie, licentie en onderhoudsstatus. Houd afhankelijkheden redelijk actueel. Kleine, frequente updates zijn veel goedkoper en veiliger dan zeldzame, gigantische sprongen. Let op aankondigingen van upstreamprojecten over einde van levensduur en beveiligingsondersteuningsvensters, en plan migraties voordat ondersteuning eindigt, niet nadat een kwetsbaarheid een wedloop afdwingt. Besluit voor kritieke componenten met risico op verlating vooraf of je de beheerder financiert, zelf onderhoud bijdraagt, forkt of vervangt. Volg het einde van de levensduur voor commerciële en open-sourcesoftware even goed, en houd zonder ondersteuning raken aan dezelfde maatstaf als elk ander operationeel risico.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen |
|---|---|---|
| Open source vrij gebruiken | Snelle oplevering. Enorme hefboom. Geen licentiekosten | Licentie-, beveiligings- en onderhoudsverplichtingen die je nu bezit |
| Strikte licentietoelatingslijst | Laag juridisch risico. Voorspelbaar | Vertraagt teams. Kan werkelijk nuttige componenten uitsluiten |
| Alleen permissieve licenties | Minimale verplichtingen. Makkelijk te combineren | Mist waardevolle copyleftprojecten. Minder wederkerigheid |
| Copyleft accepteren waar passend | Toegang tot sterke ecosystemen. Voordelen van wederkerigheid | Vraagt zorg bij combineren en distribueren |
| Bijdragen aan upstream | Minder last van eigen patches. Invloed. Goodwill | Doorlopende inspanning. Overhead van IP en proces |
| In plaats daarvan eigen bouwen | Volledige controle. Geen externe verplichtingen | Hoge kosten. Vindt commodity opnieuw uit. Je onderhoudt het voor altijd |
| Overheid publiceert standaard | Transparantie. Hergebruik. Vermijdt afhankelijkheid | Publicatie-inspanning. Beveiligingsreview. Aanhoudend rentmeesterschap |

De centrale spanning is tussen ontwikkelsnelheid en controle. Sluit alles achter zware review en ontwikkelaars werken om het beleid heen. Dat creëert onbeheerde schaduwafhankelijkheden, wat erger is dan een permissief-maar-zichtbare aanpak. Laat het volledig ongecontroleerd en je stapelt onzichtbaar juridische en beveiligingsschuld op. De oplossing is automatisering en curatie: maak het conforme pad het snelste pad, via vooraf gecontroleerde componenten, scannen in de pijplijn en heldere standaarden, zodat je controle krijgt zonder wrijving. Bij copyleft is de afweging niet "riskant tegenover veilig" maar "begrepen tegenover niet." Copyleft is volledig bruikbaar zodra je weet hoe je combineert en distribueert.

## Vragen om met je team te bespreken

1. **Wat is je expliciete regel voor sterke en netwerkcopyleft in interne, gedistribueerde en via het netwerk aangeboden contexten?** Copyleft is een ontwerpbeperking, geen taboe, en de verplichtingen hangen af van twee dingen: of je de software distribueert en hoe nauw je componenten combineert. GPL in een interne tool gedraagt zich heel anders dan GPL gelinkt in een product dat je uitlevert, en AGPL breidt openbaarmakingsplichten uit tot software die je slechts over een netwerk aanbiedt, wat je afweging tussen bouwen en adopteren verandert voor alles wat je als service draait. Schrijf de regel op per context, zodat een ontwikkelaar zonder een jurist te bellen weet dat (bijvoorbeeld) permissief overal vooraf is goedgekeurd, sterke copyleft intern prima is maar uit het uitgeleverde product is geblokkeerd, en AGPL review vraagt voordat het een netwerkservice raakt. Neem bewijs mee: scan je huidige afhankelijkhedenboom en vind waar copyleftcomponenten al zitten ten opzichte van je distributiegrens. Poort dan de build op dat beleid, want een regel die geen scanner afdwingt is een regel die ontwikkelaars per ongeluk zullen breken.

2. **Heb je een Open Source Program Office nodig, en wie bezit vandaag licentiebeleid, scannen en bijdragebeslissingen?** Als het eerlijke antwoord "niemand" is of "elk team beslist," draai je een vrijbuiterij die onzichtbaar juridische en beveiligingsschuld opstapelt. Een OSPO, zelfs één persoon plus een multidisciplinaire werkgroep, beteugelt die chaos en vangt strategische waarde: in welke upstreamprojecten te investeren, wanneer bij te dragen en hoe je je eigen projecten goed uitbrengt. Neem bewijs mee naar de vergadering: kan iemand de huidige goedgekeurde licentielijst produceren, de SBOM en de naam van de persoon die een copyleftvraag zou afhandelen tijdens due diligence bij een overname? Het antwoord moet helder eigenaarschap toewijzen en het conforme pad het snelste pad maken, via vooraf gecontroleerde componenten en scannen in de pijplijn, zodat ontwikkelaars controle krijgen zonder wrijving. Een beleid dat trager is dan code kopiëren wordt gewoon genegeerd.

3. **Welke afhankelijkheden zouden het meeste pijn doen als ze morgen werden verlaten, en wat is je vooraf bepaalde respons voor elk?** Elke afhankelijkheid bereikt uiteindelijk het einde van haar levensduur, en de dure versie van die gebeurtenis is ontdekken dat een kerncomponent maanden geleden ondersteuning verloor, pas wanneer een kwetsbaarheid aandacht afdwingt. Besluit voor je kritieke componenten met risico op verlating vooraf of je de beheerder financiert, zelf onderhoud bijdraagt, forkt of vervangt. Neem bewijs mee: som uit je SBOM de componenten op waarvan falen een omzet- of missiekritieke service zou stoppen en noteer van elk de onderhoudsstatus en het beveiligingsondersteuningsvenster. Het antwoord moet het einde van de levensduur van een verrassing omzetten in een gevolgd operationeel risico met een geplande migratie, gehouden aan dezelfde maatstaf als elk ander risico. Afhankelijkheden in kleine, frequente stappen actueel houden is veel goedkoper dan de zeldzame, gigantische, gedwongen sprong.

4. **Kun je een complete, actuele SBOM produceren die helemaal door je transitieve afhankelijkhedenboom reikt, en hoe snel?** Wanneer een kwetsbaarheid in de krantenkoppen landt in een veelgebruikte bibliotheek is de eerste vraag van leiderschap "zijn we blootgesteld, en waar?" Een team dat niet binnen uren kan antwoorden loopt al achter, want het echte risico zit meestal meerdere lagen diep in afhankelijkheden die niemand met opzet koos. De concurrerende overweging is kosten en ruis: een volledige transitieve inventaris over veel services genereert een grote, wisselende lijst, en overmatig alarmeren traint mensen haar te negeren, dus je moet beslissen welke diepte en welke ernst werkelijk actie triggeren. Neem bewijs mee naar de discussie: probeer nu een verse SBOM te genereren voor één productieservice, tel hoeveel componenten direct tegenover transitief zijn en tijd hoe lang het duurde. Koppel dit voor een onderneming of overheidsorgaan aan een concreet doel voor incidentrespons en aan elke wettelijke plicht getroffen componenten te melden, want een mandaat om blootstelling te melden die je niet kunt opsommen is een mandaat dat je zult schenden.

5. **Wanneer is een kritieke afhankelijkheid het waard te financieren, eraan bij te dragen of te beheren, in plaats van als gratis te behandelen?** De meeste organisaties gebruiken open source als een nutsvoorziening en zijn dan geschokt wanneer een component die een omzetservice draagt één onbetaalde vrijwilliger blijkt te zijn. Bewust besluiten een beheerder te financieren, reparaties te upstreamen of je eigen project uit te brengen en te beheren zet een kwetsbare gratis invoer om in een duurzame, beïnvloede, en het houdt je engineers ervan eigen patches door elke upgrade te dragen. De spanning is dat bijdragen en rentmeesterschap echte, doorlopende engineeringtijd kosten en IP- en procesoverhead dragen, dus je kunt het niet voor alles doen. Neem bewijs mee: markeer uit je SBOM de handvol componenten waarvan falen een missiekritieke service zou stoppen en noteer van elk het aantal beheerders, de financiering en hoeveel eigen patches je er al tegenaan draagt. Weeg voor een grote of publieke organisatie de reputatiekosten van een verlaten open-sourceuitgave die je met veel tamtam publiceerde, en behandel bij de overheid aanhoudend rentmeesterschap van gepubliceerde code betaald met publiek geld als onderdeel van de oplevering, niet als optionele extra.

6. **Levert je inkoop werkelijk open, herbruikbare, goed gedocumenteerde code met de rechten die je nodig hebt, of eigen zwarte dozen die je niet kunt onderhouden of verlaten?** Contracten geschreven zonder open-sourceexpertise geven routinematig een leverancier controle waar je spijt van krijgt: gesloten formaten, geen recht om te publiceren of te wijzigen en afhankelijkheden die het agentschap niet kan patchen wanneer de leverancier verder trekt. Dit vroeg goed doen is veel goedkoper dan bij verlenging ontdekken dat je niet kunt vertrekken. De concurrerende overwegingen zijn snelheid en leverancierskeuze: open opleveringen en overdraagbaarheid eisen kan het veld vernauwen en een gunning vertragen, en sommige werkelijk nuttige leveranciers verzetten zich ertegen. Neem bewijs mee: haal twee recente contracten op en controleer of ze licentievoorwaarden, aanlevering van broncode, documentatiestandaarden, SBOM-verstrekking en de rechten die de organisatie behoudt specificeren. Koppel dit voor inkoop door ondernemingen aan afhankelijkheid en total-cost-analyse. Koppel het bij de overheid aan mandaten van open-by-default en "public money, public code" en aan het gedocumenteerde uitzonderingsproces waarmee je alleen de beveiligingsgevoelige delen sluit in plaats van het hele systeem.

## Sectorperspectief

**Startup.** Je stelt bijna alles samen uit open source en hebt geen jurist, dus houd de regel op één pagina: permissieve licenties als MIT en Apache 2.0 zijn vooraf goedgekeurd, sterke copyleft is prima voor interne tooling maar geblokkeerd uit het uitgeleverde product, en alles vreemds krijgt een snelle review van een oprichter. Voeg een licentie- en kwetsbaarheidsscan aan de pijplijn toe en houd vanaf dag één een SBOM bij, want het goedkoopste moment om dit goed te doen is voordat de due diligence van een overnemer je afhankelijkhedenboom doorkamt. Verbied copyleft niet uit angst. Begrijp het en ga door.

**Kleinbedrijf.** Zonder open-sourcespecialist en met een krap budget leun je op tooling in plaats van formatie: een scanner in de build en een korte lijst goedgekeurde licenties doen het meeste werk dat een persoon zou doen. Formuleer gebruik eerlijk als koop-of-bouw, aangezien een goed onderhouden open component opnieuw uitvinden meestal de dure keuze is, maar afhankelijk zijn van een die je nooit inventariseert ook. Houd een eenvoudig overzicht bij van wat je gebruikt en onder welke licentie, zodat een beveiligingsvragenlijst van een klant of een kwetsbaarheidsalarm geen wedloop wordt.

**Grote onderneming.** Op schaal is het probleem consistentie over veel teams, dus zet een OSPO op dat beleid, geautomatiseerd scannen, het genereren van naamsvermelding en bijdragebestuur bezit, en maak het conforme pad het snelste pad via gecureerde, vooraf gecontroleerde componenten. Dwing copyleftregels per context af in de pijplijn, onderhoud SBOM's over services en beheer actualiteit van afhankelijkheden en einde van levensduur als gevolgd operationeel risico. Behandel open source als beheer van de toeleveringsketen voor het merendeel van je codebasis, met auditklaar bewijs voor due diligence bij overnames.

**Overheid.** Openheid is vaak voorgeschreven, niet optioneel, dus kies standaard voor open standaarden en publiceer code betaald met publiek geld tenzij een gedocumenteerde uitzondering geldt voor beveiliging, rechten van derden of privacy. Hergebruik voor je bouwt door een catalogus over de hele overheid te raadplegen en bak open, herbruikbare, goed gedocumenteerde opleveringen en behouden rechten in de inkoop zodat je onderhoudbare code ontvangt in plaats van eigen zwarte dozen. Houd gepubliceerde code aan echt rentmeesterschap en houd het uitzonderingsproces smal en transparant zodat het alleen sluit wat het moet.

## Voorbeelden

**Startup.** Een startup van vier personen die een mobiele app bouwt stelt bijna alles samen uit open source en heeft geen jurist in dienst. In plaats van copyleft uit angst te verbieden schrijven de oprichters een beleid van één pagina: permissieve licenties als MIT en Apache 2.0 zijn vooraf goedgekeurd, sterke copyleft zoals GPL is prima voor interne tooling maar geblokkeerd uit de uitgeleverde app om openbaarmakingsplichten te vermijden, en alles ongewoons krijgt een snelle review van een oprichter. Ze voegen een licentie- en kwetsbaarheidsscan aan de pijplijn toe zodat een verboden licentie niet in een release kan glippen, houden vanaf dag één een SBOM bij en upstreamen een kleine reparatie naar een kritieke bibliotheek zodat ze ophouden een eigen patch door elke upgrade te dragen. Dit vroeg goed doen bespaart hen ook een pijnlijke verrassing wanneer de due diligence van een overnemer uiteindelijk de afhankelijkhedenboom doorkamt.

**Grote onderneming.** Een softwareleverancier die een gedistribueerd product uitlevert draait een OSPO. Het OSPO onderhoudt een goedgekeurde licentielijst, een interne gecureerde componentrepository en geautomatiseerd licentie- en kwetsbaarheidsscannen in elke pijplijn. Wanneer een ontwikkelaar een nieuwe afhankelijkheid binnenhaalt, controleert de pijplijn haar licentie tegen het beleid, genereert de naamsvermeldingen die met het product meegaan en markeert alles wat review vraagt. Sterke-copyleftcomponenten zijn toegestaan voor interne tooling maar geblokkeerd uit het gedistribueerde product, om openbaarmakingsverplichtingen te vermijden. Het bedrijf upstreamt reparaties naar een paar kritieke afhankelijkheden. Dat elimineerde een achterstand aan eigen patches die zijn engineers vroeger bij elke upgrade meedroegen.

**Overheid.** Een nationale digitale dienst opereert onder een beleid van "public money, public code". Nieuwe services worden gebouwd op open standaarden, standaard openlijk ontwikkeld op een publieke coderepository en hergebruikt over instanties. De inkoopsjablonen eisen van leveranciers open, goed gedocumenteerde, herbruikbare code op te leveren, waarbij de overheid de rechten houdt om te publiceren en te wijzigen. Voordat ze een nieuwe component beginnen zoeken teams in een catalogus over de hele overheid naar bestaande herbruikbare code. Beveiligingsgevoelige modules worden via een gedocumenteerd proces van publicatie vrijgesteld, in plaats van het hele systeem gesloten te maken.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Open source goed beheren is het verschil tussen de enorme hefboom vangen en betalen voor de verborgen kosten. Open source laat een grote organisatie staan op een fundament dat ze nooit kon betalen te bouwen. Maar de [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) omvat compliance, beveiligingspatches en uiteindelijke migratie, kosten die komen of je ervoor plant of niet. Bewust beheer zet onvoorspelbare, dure crises om in kleine, stabiele, geplande kosten. Die crises omvatten een copyleftschending gevonden tijdens due diligence bij een overname, een noodmigratie weg van een verlaten component of een kwetsbaarheid in een afhankelijkheid waarvan niemand wist dat die er was.

De adoptiekosten zijn bescheiden naast de blootstelling: een OSPO of werkgroep, scantooling en de discipline van een inventaris bijhouden. De kosten van *niet* adopteren verschijnen als juridische aansprakelijkheid, mislukte due diligence, beveiligingsincidenten herleid tot ongepatchte afhankelijkheden en de samengestelde kosten van uitgestelde upgrades die uiteindelijk pijnlijke big-bangmigraties afdwingen. Wanneer je de zaak voor leiderschap maakt, formuleer open-sourcebeheer als beheer van de toeleveringsketen voor het merendeel van je codebasis. Noem ook de strategische kant: vermeden afhankelijkheid, snellere oplevering, talent aantrekken en invloed op de ecosystemen waarvan je afhangt. Voeg bij de overheid de mandaatdimensie toe. Openheid is vaak vereist, niet optioneel, en het goed doen vermijdt zowel niet-naleving als dubbele publieke uitgaven.

## Antipatronen en valkuilen

- **Kopieer-plak-licentiëring.** Ontwikkelaars die componenten binnenhalen zonder licentiecontrole en pas bij audit of overname verplichtingen ontdekken.
- **Geen inventaris.** Niet kunnen antwoorden op "wat gebruiken we en onder welke licentie?" wanneer een kwetsbaarheid of licentievraag losbarst.
- **Copyleftpaniek.** Alle copyleft verbieden uit angst in plaats van begrip, waardoor waardevolle ecosystemen worden gemist.
- **De verlaten open-sourceuitgave.** Een project publiceren met veel tamtam en het dan nooit onderhouden, wat de reputatie schaadt.
- **Transitieve afhankelijkheden negeren.** Directe afhankelijkheden controleren terwijl het echte risico meerdere lagen dieper zit.
- **Verrassing van einde levensduur.** Ontdekken dat een kerncomponent maanden geleden ondersteuning verloor, pas wanneer een kwetsbaarheid aandacht afdwingt.
- **Beleid trager dan kopiëren.** Een compliance-proces zo zwaar dat ontwikkelaars eromheen werken, wat onzichtbare schaduwafhankelijkheden creëert.
- **Zwarte dozen bij de overheid.** Eigen systemen inkopen die het agentschap niet kan onderhouden, delen of verlaten, in strijd met open-by-defaultprincipes.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Ontwikkelaars voegen vrijelijk open source toe zonder beleid of inventaris. Licenties zijn onbeproefd en copyleftverplichtingen onbekend. Einde van levensduur wordt per ongeluk ontdekt, meestal wanneer een kwetsbaarheid aandacht afdwingt. Niemand bezit open-sourcestrategie.

**Niveau 2: Ontwikkelen.** Een basisbeleid en goedgekeurde licentielijst bestaan, en sommige teams volgen ze. Scannen gebeurt, maar vaak handmatig, laat of alleen op enkele projecten. Een inventaris wordt bijgehouden voor grote systemen terwijl transitieve afhankelijkheden niet in kaart zijn gebracht. Bijdragen en afhandeling van einde van levensduur zijn ad hoc en inconsistent tussen teams.

**Niveau 3: Standaardiseren.** Een OSPO of gelijkwaardig bezit strategie, beleid en tooling organisatiebreed. Licentie- en kwetsbaarheidsscannen is geautomatiseerd in elke pijplijn, naamsvermeldings- en mededelingsbestanden worden automatisch gegenereerd en de build is gepoort zodat een verboden licentie er niet in kan. SBOM's worden onderhouden door de transitieve boom, bijdragen volgen een gedocumenteerd proces, einde van levensduur wordt gevolgd met geplande migraties en overheidsteams publiceren standaard.

**Niveau 4: Beheersen.** Het programma wordt gemeten en beheerst tegen uitgangswaarden. Je volgt dekking van beleidsscans over services, gemiddelde tijd om een bekendgemaakte afhankelijkheidskwetsbaarheid te patchen, het aandeel componenten binnen hun beveiligingsondersteuningsvenster, het ontsnappingspercentage van licentieschendingen, achterstand in actualiteit van afhankelijkheden en het aantal eigen patches dat naar upstream is gedragen. Plaatsing van copyleft ten opzichte van de distributiegrens wordt bewaakt, en statistieken tegen doelen drijven elke go/no-go-beslissing in plaats van mening.

**Niveau 5: Orkestreren.** Open source is een continu verbeterd strategisch bezit geïntegreerd over de organisatie. Compliance is volledig geautomatiseerd en niet-conforme componenten kunnen productie niet bereiken. Je investeert bewust in kritieke upstreamprojecten, draagt routinematig bij en beheert je eigen goed gedraaide projecten. Actualiteit van afhankelijkheden en einde van levensduur worden adaptief beheerd naarmate risico en statistieken verschuiven, en openheid wordt een werkelijk concurrerend en maatschappelijk voordeel.

## Ideeën voor discussie

- Waar ligt de juiste lijn tussen een snelle permissieve standaard en de controle nodig om juridische en beveiligingsschuld te vermijden?
- Wanneer zou een organisatie een kritieke upstreamafhankelijkheid moeten financieren of onderhouden in plaats van haar als gratis te behandelen?
- Hoe beslis je welke van je eigen componenten het waard zijn om als open source uit te brengen en te beheren?
- Wat is voor de overheid een verdedigbaar proces om componenten vrij te stellen van publiceren-als-standaard zonder het principe uit te hollen?
- Hoe diep in transitieve afhankelijkheden moet licentie- en beveiligingsreview realistisch gaan?
- Verandert netwerkcopyleft (AGPL) je afweging tussen bouwen en adopteren voor software die je als service aanbiedt?

## Belangrijkste inzichten

- Open source is het merendeel van de meeste codebases en moet worden beheerd als toeleveringsketen, niet behandeld als gratis en zonder gevolgen.
- Licenties dragen echte verplichtingen. Begrijp de families permissief, zwakke copyleft, sterke copyleft en netwerkcopyleft en hoe distributie en combinatie plichten triggeren.
- Maak het conforme pad het snelste pad via curatie, geautomatiseerd scannen en heldere standaarden, anders werken ontwikkelaars om beleid heen.
- Zet een OSPO op om strategie, compliance, bijdragen en rentmeesterschap op schaal te bezitten.
- Onderhoud een SBOM, houd afhankelijkheden in kleine stappen actueel en plan het einde van de levensduur voordat het een crisis afdwingt.
- Kies bij de overheid standaard voor open standaarden en publiceer code betaald met publiek geld, en hergebruik voor je bouwt.

## Referenties en verder lezen

- Heather Meeker, *Open (Source) for Business* and *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation and TODO Group, *OSPO guides* and *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* and *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* and approved licence list
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy and Code.gov guidance
- UK Government, *Technology Code of Practice* and open-standards principles
