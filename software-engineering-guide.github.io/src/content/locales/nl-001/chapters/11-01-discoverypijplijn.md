# 11.1 De discoverypijplijn

## Overzicht en motivatie

De discoverypijplijn is de stroom werk die beslist **wat te bouwen en waarom**, en definieert **hoe succes eruitziet**, vóór en naast oplevering. Waar de opleveringspijplijn (hoofdstuk 11.2) gevalideerde ideeën omzet in draaiende software, zet de discoverypijplijn problemen, bewijs en strategie om in een geprioriteerde, testbare set beoogde uitkomsten. In de moderne praktijk lopen de twee continu en parallel, vaak *dual-track*-ontwikkeling genoemd, in plaats van als opeenvolgende fasen. Discovery blijft een klaar aanbod van gede-riskt, goed gekaderd werk aan oplevering voeden, en oplevering blijft echte uitkomstdata terugvoeden in discovery.

Voor grote teams is een zwakke discoverypijplijn de duurste faalwijze in software. Een team met uitstekende oplevering en slechte discovery bouwt het verkeerde efficiënt: het levert snel uit, haalt zijn velocitydoelen en beweegt toch geen enkele bedrijfsstatistiek. De kosten zijn onzichtbaar op engineeringdashboards en enorm op de balans. De discoverypijplijn is hoe je die kosten zichtbaar maakt: ze dwingt doelen expliciet, meetbaar en falsifieerbaar te zijn voordat je grote investeringen committeert.

Contexten van onderneming en overheid verhogen de inzet. Ondernemingen coördineren tientallen teams tegen een gedeelde strategie, dus niet-afgestemde lokale doelen stapelen op tot verspilde portfolio's. Overheidsprogramma's committeren meerjarige publieke financiering tegen wettelijke mandaten, waar "we bouwden wat het contract zei" geen verdediging is als de uitkomst (burgers bediend, wachttijden verminderd, fraude voorkomen) nooit materialiseert. Een gedisciplineerde discoverypijplijn, uitgedrukt via doelstellingen, maten en expliciete kwaliteitseisen, is hoe beide hun intentie controleerbaar houden.

## Kernprincipes

- **Uitkomsten boven output.** Meet de verandering die je voor gebruikers en het bedrijf creëert, niet de functies die je uitlevert.
- **Maak intentie expliciet en meetbaar.** Een doel dat je niet kunt meten is een mening die je niet kunt beheren.
- **De-risk voordat je bouwt.** Het goedkoopste experiment verslaat de meest zelfverzekerde mening.
- **Discovery en oplevering lopen continu parallel**, niet als opeenvolgende poorten.
- **Kwaliteitsattributen zijn eisen, geen bijzaak.** Betrouwbaarheid, beveiliging en toegankelijkheid worden ontdekt en gespecificeerd, niet gehoopt.
- **Afstemming verslaat lokale optimalisatie.** Genestelde doelen verbinden teamwerk aan strategie.
- **Sluit de lus.** Opgeleverde uitkomsten zijn bewijs dat terug in discovery komt.

## Aanbevelingen

### Kader richting met OKR's

Gebruik **[Objectives en Key Results](https://en.wikipedia.org/wiki/OKR) (OKR's)** om strategie met teamuitvoering te verbinden. Een *Objective* is een kwalitatieve, inspirerende verklaring van een gewenste eindtoestand ("Maak eerste onboarding moeiteloos"). *Key Results* zijn het kleine aantal (typisch 2–4) meetbare uitkomsten die bewijzen dat de objective wordt gehaald ("Verhoog 7-daagse activatie van 40% naar 60%"; "Verminder onboardingsupporttickets met 30%"). Key results drukken **uitkomsten** uit, geen taken: "lever de nieuwe wizard uit" is een taak vermomd als resultaat.

Cascadeer OKR's via *afstemming*, niet dictaat: leiderschap stelt een klein aantal bedrijfsobjectives, teams stellen key results en hun eigen objectives voor die erop oplopen. Stel ze volgens een vast ritme (gewoonlijk per kwartaal met een jaarkader), beoordeel ze halverwege de cyclus en beoordeel ze aan het eind eerlijk. Houd ze gescheiden van functioneringsgesprekken: OKR's beoordeeld voor beloning worden snel gezandzakt. Zie hoofdstuk 10.1 voor hoe OKR's aansluiten op portfolio- en programmamanagement.

### Bewaak gezondheid met KPI's

Onderscheid **[Key Performance Indicators](https://en.wikipedia.org/wiki/Performance_indicator) (KPI's)** van OKR's. OKR's beschrijven de *verandering* die je in deze periode wilt. KPI's beschrijven de *doorlopende gezondheid* die je moet volhouden ongeacht wat je verandert (uptime, conversiepercentage, kosten per transactie, klanttevredenheid). Een statistiek kan beide zijn (een KPI die je actief probeert te bewegen wordt een key result), maar de meeste KPI's zijn vangrails die je bewaakt, geen doelen waarnaar je sprint.

Deel elke belangrijke statistiek in als **leidend** (voorspellend en nu uitvoerbaar, zoals proefaanmeldingen) of **volgend** (bevestigend en traag, zoals jaaromzet). Discovery leunt op leidende indicatoren om te sturen voordat volgende indicatoren bevestigen. Pas op voor ijdele statistieken die betrouwbaar stijgen maar niets voorspellen (ruwe paginaweergaven, totaal geregistreerde gebruikers). Geef de voorkeur aan verhoudings- en cohortstatistieken die bespelen weerstaan. Zie hoofdstuk 7.3 en 7.4 voor de analytics- en experimenteermachinerie achter deze maten.

### Specificeer systeemkwaliteitsattributen expliciet

Functionele eisen zeggen wat het systeem doet. **Systeemkwaliteitsattributen** (de "-iteiten": betrouwbaarheid, prestaties, schaalbaarheid, beveiliging, toegankelijkheid, onderhoudbaarheid, beheerbaarheid) zeggen hoe goed het moet. Deze worden routinematig te weinig ontdekt: iedereen neemt ze aan, niemand specificeert ze en ze verschijnen als productie-incidenten. Behandel ze als eersterangs discoveryuitvoer. Identificeer de **architectonisch significante eisen** (de kwaliteitseisen die de architectuur wezenlijk vormen) voor elk initiatief. Kwantificeer ze ("p99-latentie onder 200 ms bij 10× huidige belasting"; "WCAG (Web Content Accessibility Guidelines) 2.2 AA"; "hersteltijddoelstelling van 15 minuten"). En codeer ze waar je kunt als geautomatiseerde **fitnessfuncties** (uitvoerbare controles die een kwaliteitsattribuut continu verifiëren) die de opleveringspijplijn kan controleren. Dit is het discovery-tegenstuk van hoofdstuk 3.1 (architectuurfundamenten) en hoofdstuk 3.5 (schaalbaarheid, prestaties, veerkracht).

### Maak elk doel SMART

Pas, of je nu een key result, een acceptatiecriterium of een kwaliteitsdoel schrijft, de **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)**-toets toe:

- **Specifiek:** noemt één heldere, ondubbelzinnige uitkomst.
- **Meetbaar:** heeft een statistiek en een bron van waarheid.
- **Haalbaar:** is realistisch gegeven beperkingen en bewijs.
- **Relevant:** loopt op naar een hogere objective en naar gebruikerswaarde.
- **Tijdgebonden:** heeft een deadline of herzieningsdatum.

"Verbeter prestaties" faalt op elke letter. "Verminder de mediane afrekentijd van 8s naar 3s voor mobiele gebruikers eind Q3, gemeten met real-user monitoring" slaagt voor alle vijf. SMART-criteria zetten vage ambitie om in een falsifieerbare bewering die discovery kan testen en oplevering kan verifiëren.

### Draai continue, op bewijs gedreven discovery

Structureer discovery als herhaalbare pijplijn, niet als eenmalige fase:

1. **Waarnemen.** Verzamel signalen: gebruikersonderzoek, supportdata, analytics, markt- en complianceinvoer.
2. **Kaderen.** Breng kansen in kaart (een *opportunity-solution tree* verbindt een gewenste uitkomst aan de gebruikersbehoeften en kandidaatoplossingen die haar kunnen bewegen).
3. **Hypothese.** Stel aannames als falsifieerbare beweringen: "We geloven dat [verandering] [uitkomst] zal veroorzaken voor [segment], en we weten het als [maat] beweegt."
4. **Experimenteren.** Valideer de riskantste aannames met de goedkoopste test: interviews, prototypes, fake-doortests (een nog niet gebouwde functie adverteren om echte vraag te meten), [A/B-experimenten](https://en.wikipedia.org/wiki/A/B_testing) (gerandomiseerde vergelijkingen van twee varianten, hoofdstuk 7.4).
5. **Beslissen.** Volhouden, bijsturen of laten vallen, en voed de overlevenden in de opleveringsachterstand met hun SMART-succescriteria eraan vast.

De uitkomst van de discoverypijplijn is geen functielijst. Het is een stroom *gevalideerde, meetbare weddenschappen* klaar voor oplevering.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| **Op uitkomsten gebaseerde doelen (OKR's)** | Stemt teams af op impact. Bekrachtigt autonomie in het *hoe* | Moeilijk goed te schrijven. Verleidelijk met taken aan te vullen. Rumoerige toewijzing |
| **Output-/functieroadmaps** | Voorspelbaar, makkelijk te communiceren en te contracteren | Beloont uitleveren boven impact. Verbergt risico van het verkeerde ding |
| **Zware discovery vooraf** | Vermindert bouwverspilling. Sterke eisen | Vertraagt de start. Risico van analyseverlamming. Aannames nog ongetoetst |
| **Continue dual-track-discovery** | De-risked continu. Snelle feedback | Vraagt onderzoekscapaciteit en discipline. Moeilijker te plannen |
| **Expliciete kwaliteitsattributen als SMART-doelen** | Voorkomt "-iteit"-verrassingen. Controleerbaar | Inspanning om te kwantificeren. Kan vroege verkenning overbeperken |

De centrale spanning is **toezegging tegenover leren**. Ondernemingen, en vooral overheden, hebben vaak vaste toezeggingen nodig voor begroting en contracten, wat naar outputroadmaps trekt. Goede uitkomsten hebben ruimte nodig om te leren, wat naar OKR's en experimenten trekt. Los het zo op: committeer je stevig aan *problemen en uitkomsten* en houd *oplossingen* los.

## Vragen om met je team te bespreken

1. **Wie in je team bezit discovery werkelijk, en hebben ze de capaciteit haar continu te draaien in plaats van in één eenmalige sprint?** Dual-track-ontwikkeling werkt alleen wanneer iemand de discoverytrack elke week open houdt in plaats van alleen aan het begin van een kwartaal. In een grote organisatie heeft discovery vaak geen speciale eigenaar, dus ze valt in wie tijd over heeft, wat niemand is, en het team valt terug op bouwen. Neem bewijs mee: tel hoeveel van je laatste tien functies door een gedocumenteerde hypothese en een goedkope test gingen vóór de bouw, tegenover rechtstreeks in de achterstand. Noem in omgevingen van onderneming en overheid, waar één niet-afgestemd initiatief meerdere team-kwartalen kan verspillen, een productowner of een trio (product, ontwerp, engineering) verantwoordelijk voor de lus waarnemen-kaderen-hypothese-experimenteren-beslissen. Als niemand haar bezit, bemand haar voordat je over iets anders redetwist.

2. **Welke van je huidige initiatieven hebben architectonisch significante eisen die je nooit hebt gekwantificeerd, en kon je er enkele als fitnessfuncties coderen?** De "-iteiten" (betrouwbaarheid, prestaties, beveiliging, toegankelijkheid) worden aangenomen en verschijnen dan als productie-incidenten. Loop elk actief initiatief door, vraag welke kwaliteitsattributen de architectuur wezenlijk vormen en controleer of elk een getal en een bron van waarheid heeft: "p99 onder 200 ms bij 10× belasting," "WCAG 2.2 AA," "hersteltijddoelstelling van 15 minuten." Voor onderneming en overheid creëren niet-gekwantificeerde toegankelijkheids- of beveiligingseisen directe juridische en auditblootstelling. Het signaal om mee te nemen zijn je laatste drie incidenten: hoeveel herleidden zich naar een kwaliteitsattribuut dat niemand specificeerde? Waar je een doel kunt omzetten in een geautomatiseerde fitnessfunctie die de opleveringspijplijn controleert, doe het, want een gespecificeerd maar niet-afgedwongen doel drijft af.

3. **Toen je je voor het laatst aan een oplossing committeerde, testte je de riskantste aanname eerst, of de makkelijkste?** Teams valideren betrouwbaar de aanname waar ze zich het prettigst bij voelen en slaan degene over die het idee werkelijk zou doden. Som voor elk initiatief zijn aannames op (wenselijkheid, levensvatbaarheid, haalbaarheid) en rangschik ze op "hoe dood is dit idee als we hier ongelijk hebben," en richt dan de goedkoopste test op de top van die lijst. Dit doet er op schaal toe omdat een zelfverzekerd, senior team een kwartaal engineering kan committeren aan een ongetoetste overtuiging, en de kosten onzichtbaar blijven tot de lancering. Neem het artefact mee: je laatste hypothese gesteld als "We geloven dat [verandering] [uitkomst] veroorzaakt voor [segment], gemeten door [statistiek]," en vraag of je haar testte of gewoon bouwde. Als je de riskantste aanname niet kunt noemen, ben je niet klaar om bouwcapaciteit te committeren.

4. **Hoeveel van je key results zijn echte uitkomsten, en hoeveel zijn taken of uitleverdata in uitkomstenkleren?** De meest gangbare fout in op uitkomsten gebaseerde planning is key results aanvullen met het werk dat je al van plan was te doen ("lanceer de nieuwe wizard") in plaats van de verandering die dat werk moet veroorzaken ("verhoog 7-daagse activatie van 40% naar 60%"). Op schaal ondermijnt dit stilletjes het hele punt: tientallen teams rapporteren groen terwijl geen bedrijfsstatistiek beweegt, omdat iedereen zichzelf beoordeelde op uitleveren. De concurrerende trek is echt, outputroadmaps zijn makkelijker te communiceren, contracteren en voorspellen, precies waarom ze terugsluipen. Neem je huidige OKR-set mee en markeer elk key result als uitkomst of output, controleer dan of OKR-beoordeling verstrengeld is met beloning, want resultaten gekoppeld aan loon worden snel gezandzakt. Voor portfolio's van onderneming en overheid, waar financiering wordt gecommitteerd tegen vermelde doelen, is een roadmap van outputs zonder uitkomstmaat een auditbevinding die staat te gebeuren. Sta erop dat elk initiatief zich stevig aan een probleem en een meetbare uitkomst committeert terwijl de oplossing los blijft.

5. **Welke van je KPI's zouden blijven stijgen zelfs als het product slechter werd, en welke vangrails beschermen de statistieken die je actief probeert te bewegen?** Elke statistiek die je tot doel verheft nodigt [de wet van Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law) uit: zodra een maat het doel wordt, optimaliseren mensen de maat in plaats van wat ze moest vertegenwoordigen. IJdele statistieken (ruwe paginaweergaven, cumulatief geregistreerde gebruikers) stijgen betrouwbaar en voorspellen niets, terwijl één key result zonder vangrails kan worden gehaald door iets te verslechteren dat je nooit noemde. De spanning is dat leidende indicatoren je vroeg laten sturen maar rumoerig en bespeelbaar zijn, terwijl volgende indicatoren betrouwbaar zijn maar te laat bevestigen om te handelen. Neem je statistiekeninventaris mee ingedeeld als leidend of volgend en als doel of vangrail, en test elk doel op stress door te vragen "hoe kon een slim team dit getal halen terwijl het product slechter wordt." Publiceer in gereguleerde en publieke omgevingen de vangrails naast de doelen, want een toezichtsorgaan dat alleen de kopstatistiek ziet kan echte publieke waarde niet van een bespeeld getal onderscheiden.

6. **Wanneer oplevering iets uitlevert, hoe komt de werkelijke uitkomst dan terug in discovery, of blijft de lus open?** Dual-track-ontwikkeling stapelt alleen op als opgeleverde uitkomsten terugstromen als bewijs voor de volgende ronde. Wanneer de lus open blijft, leveren teams uit, vieren ze en leren ze nooit of de weddenschap uitbetaalde, zodat dezelfde ongetoetste aannames terugkeren. In een grote organisatie is het feedbackpad waar verantwoordelijkheid het waarschijnlijkst door een gat valt: oplevering bezit de release, analytics bezit het dashboard en niemand bezit de belofte key result met de waargenomen vergelijken. Neem je laatste tien uitgeleverde initiatieven mee en vraag voor elk of iemand de uitkomststatistiek tegen het oorspronkelijke SMART-doel controleerde en of die controle een latere beslissing veranderde. Noem voor programma's van onderneming en overheid met meerjarige financiering het ritme en de eigenaar voor het afschaffen of herafbakenen van functies die hun statistiek niet bewogen, want een uitgeleverde functie die niemand herziet wordt permanente kosten zonder verantwoorde review.

## Sectorperspectief

**Startup.** Met een klein team en weinig runway is je discoverypijplijn bewust licht maar nooit overgeslagen: een dag klantinterviews en een fake-doortest kosten bijna niets tegenover de weken die een verkeerde bouw verbrandt. Kies één leidende indicator die voor je kernwaarde staat, stel elke weddenschap als één falsifieerbare hypothese en doe ideeën dood voordat je code schrijft in plaats van erna. Formele OKR's zijn overdreven bij vijf mensen. Eén eerlijke meetbare uitkomst per cyclus is genoeg om te voorkomen dat snelheid beweging zonder voortgang wordt.

**Kleinbedrijf.** Je hebt waarschijnlijk geen speciale onderzoeker of productanalist, dus behandel discovery als gewoonte, niet als rol: een paar gestructureerde gesprekken met echte klanten en een eenvoudige statistiek die je al verzamelt. De vraag tussen kopen en bouwen domineert, want de meeste kwaliteitsattributen (betrouwbaarheid, beveiliging, toegankelijkheid) zijn goedkoper bij een gerenommeerde leverancier te halen dan zelf te specificeren en af te dwingen. Schrijf een of twee SMART-doelen zodat je kunt zien of een gekocht hulpmiddel of een kleine bouw de uitkomst werkelijk bewoog, en vermijd schaars budget te committeren aan functies waarvan niemand heeft gevalideerd dat ze gewenst zijn.

**Grote onderneming.** Schaal maakt van discovery een coördinatieprobleem over tientallen teams: zonder een gedeeld OKR-ritme en een gemeenschappelijke definitie van "uitkomst" drijven lokale doelen af en dupliceren ze, en niet-afgestemde weddenschappen stapelen op tot verspilde portfolio's. Standaardiseer hoe architectonisch significante eisen worden gekwantificeerd en codeer ze als fitnessfuncties zodat kwaliteitsattributen worden bestuurd, niet aangenomen. Beheer discovery als portfolio met expliciete stopcriteria en een lus die opgeleverde uitkomststatistieken terugvoedt in de volgende cyclus, zodat leiderschap stuurt op impact in plaats van op een achterstand van functies.

**Overheid.** Aanbesteding en meerjarige financiering eisen vaste toezeggingen, die hard naar outputcontracten trekken, maar publieke waarde leeft in uitkomsten: burgers bediend, wachttijden verkort, last verminderd. Kader programma's rond meetbare publieke uitkomsten en onbetwistbare kwaliteitsattributen (WCAG-toegankelijkheid, gewone taal, beveiliging) en maak discoverybewijs, inclusief usabilitytesten met gebruikers van hulptechnologie, onderdeel van het record dat toezichtsorganen kunnen controleren. Definieer succes als belasting- of burgeruitkomsten in plaats van opgeleverde modules, zodat "we bouwden wat het contract zei" nooit een resultaat kan vervangen dat niet materialiseerde.

## Voorbeelden

**Startup.** Een seed-fase team van vier personen dat een planningsapp voor kapsalons bouwt is verleid een online-boekingswidget te bouwen omdat een paar luide gebruikers erom vroegen. In plaats daarvan draaien ze een week discovery: vijf eigenaarsinterviews, een fake-doorknop "Online boeken" op de marketingsite en één leidende indicator (het percentage afspraken dat eindigt in een no-show). De interviews en klikdata onthullen dat no-shows, niet boeken, de echte pijn zijn, dus schrijven ze één SMART key result (no-shows van 22% naar onder 10% brengen voor pilotsalons dit kwartaal) en leveren eerst een kleine functie voor aanbetaling en herinnering uit, de boekingswidget dodend voordat er een regel van is geschreven.

**Grote onderneming.** De betalingsgroep van een retailbank vervangt een functietelroadmap door drie kwartaal-OKR's, waarvan één "Laat dagelijkse betalingen direct voelen" met key results voor p95-bevestigingstijd van overschrijvingen, slagingspercentage bij eerste poging en betalingsgerelateerde supportcontacten. Systeemkwaliteitsattributen worden vooraf gespecificeerd (99,99% beschikbaarheid, bevestiging in minder dan een seconde, PCI-DSS (Payment Card Industry Data Security Standard)-reikwijdte geminimaliseerd) en als fitnessfuncties in oplevering geweven. Discovery draait wekelijkse klantinterviews en fake-doortests voordat engineering wordt gecommitteerd. Twee kandidaatfuncties worden in discovery gedood omdat ze de leidende indicatoren niet bewegen (naar schatting twee kwartalen bouwinspanning bespaard), terwijl een kleinere, onglamoureuze latentiereparatie het key result het meest beweegt.

**Overheid.** Een nationale belastingdienst die online aangifte moderniseert stelt een programmaobjective van "Verminder de last van aangifte voor gewone belastingplichtigen" met SMART key results: mediane tijd-tot-aangifte snijden van 45 naar 20 minuten, succesvolle voltooiing via zelfbediening verhogen van 60% naar 85% en voldoen aan WCAG 2.2 AA en gewone-taalstandaarden als onbetwistbare kwaliteitsattributen. KPI's (uptime tijdens het aangifteseizoen, volume van het callcenter) worden bewaakt als vangrails. Discovery gebruikt gemodereerd usabilitytesten met echte belastingplichtigen, inclusief gebruikers van hulptechnologie, vóór elke release. Omdat succes is gedefinieerd als belastingplichtigenuitkomsten in plaats van opgeleverde modules, kan het programma toezichtsorganen meetbare publieke waarde tonen, niet slechts uitgaven.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van een discoverypijplijn wordt gedomineerd door **vermeden verspilling**. Brancheervaring, weerklonken in programma's met gecontroleerde experimenten bij grote techbedrijven, vindt herhaaldelijk dat een groot deel van de gebouwde functies, vaak rond de helft of meer genoemd, geen meetbare verbetering oplevert of de doelstatistiek actief schaadt. Stel dat zelfs een kwart van de bouwcapaciteit van een team naar ideeën gaat die discovery goedkoop had gedood. De pijplijn betaalt zichzelf dan vele malen terug: een week gebruikersonderzoek en een fake-doortest kost bijna niets tegenover een kwartaal engineering, plus de doorlopende onderhoudslast van een ongebruikte functie.

De **[total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO)-kadering telt omdat ongevalideerde functies na de lancering niet gratis zijn. Elke uitgeleverde functie draagt eeuwige kosten: onderhoud, testen, beveiligingsoppervlak, ondersteuning en cognitieve last (hoofdstuk 10.4). Een slecht idee in discovery doden vermijdt niet alleen de bouwkosten maar de hele staart van eigendom. Expliciete kwaliteitsattributen volgen dezelfde logica: betrouwbaarheid en toegankelijkheid vooraf als SMART-doelen specificeren is veel goedkoper dan ze achteraf inbouwen na een uitval, inbreuk of rechtszaak.

Verschuif voor leiderschap het gesprek van "hoeveel leveren we uit" naar "hoeveel bewegen we de statistieken die ertoe doen," en toon een paar concrete voorbeelden van dure functies die niets bewogen. De adoptiekosten zijn bescheiden (onderzoekscapaciteit, een OKR-ritme en de discipline om SMART-criteria te schrijven), en het primaire risico van *niet* adopteren is stil, ongeteld en stapelt samengesteld op.

## Antipatronen en valkuilen

- **Functieroadmaps die zich voordoen als strategie:** outputlijsten zonder vermelde uitkomst of maat.
- **Key results die taken zijn:** "lanceer X" in plaats van "verbeter Y met Z."
- **OKR-toneel:** doelen geschreven, opgeborgen en nooit herzien of beoordeeld.
- **Gezandzakte of heroïsche OKR's:** doelen gesteld om 100% te garanderen (niets geleerd) of fantasieve stretch zonder plan.
- **Ongespecificeerde kwaliteitsattributen:** betrouwbaarheid, beveiliging en toegankelijkheid aangenomen in plaats van gekwantificeerd en dan in productie ontdekt.
- **IJdele statistieken:** maten die altijd stijgen en niets voorspellen.
- **Discovery als eenmalige fase:** een "discoverysprint" vooraf en dan geen voortgezette validatie.
- **De oplossing bouwen voordat je de aanname test:** het goedkoopste experiment overslaan omdat het team zelfverzekerd is.
- **Statistiekfixatie en [de wet van Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law):** zodra een maat het doel wordt, is het geen goede maat meer. Balanceer met KPI's als vangrail.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Werk wordt gedefinieerd als functies op een roadmap en succes is "we hebben het uitgeleverd." Er zijn geen expliciete uitkomstmaten of kwaliteitsdoelen. Discovery gebeurt toevallig, als al, en beslissingen worden gedreven door de luidste mening.
- **Niveau 2, Ontwikkelen:** OKR's en KPI's bestaan voor sommige teams maar niet andere. Doelen worden gesteld maar zijn vaak outputvormig. Kwaliteitsattributen worden benoemd maar niet gekwantificeerd. Een team kan een eenmalige "discoverysprint" draaien en dan ophouden te valideren zodra de bouw begint, dus de praktijk is echt maar inconsistent over de organisatie.
- **Niveau 3, Standaardiseren:** Een consistent OKR-ritme afgestemd op strategie, SMART key results en gespecificeerde, testbare kwaliteitsattributen zijn gedocumenteerd en organisatiebreed verwacht. Discovery is een erkende, bemande activiteit met hypotheses en experimenten, en architectonisch significante eisen worden voor elk initiatief geïdentificeerd in plaats van aangenomen.
- **Niveau 4, Beheersen:** Het portfolio wordt gemeten tegen uitgangswaarden. Leidende en volgende indicatoren, het slagingspercentage van discovery en de uitkomst die elke uitgeleverde weddenschap werkelijk bewoog worden gevolgd tegen haar SMART-doel. Hypotheses worden beoordeeld op bewijs en stopcriteria worden afgedwongen. Fitnessfuncties rapporteren conformiteit met kwaliteitsattributen continu, zodat afdrijving van een gespecificeerd betrouwbaarheids-, prestatie- of toegankelijkheidsdoel met data wordt gevangen in plaats van in een incident.
- **Niveau 5, Orkestreren:** Continue dual-track-discovery is geïntegreerd met portfolio, risico en begroting. Gevalideerde weddenschappen stromen gestaag naar oplevering en uitkomststatistieken lussen automatisch terug om de volgende ronde te sturen. Leidende indicatoren sturen investering, en de organisatie schaft initiatieven routinematig af, herafbakent en herbalanceert ze op bewijs, de pijplijn zelf aanpassend naarmate de markt en de statistieken verschuiven.

## Ideeën voor discussie

1. Kijk naar je huidige roadmap: hoeveel items vermelden een meetbare uitkomst tegenover slechts een functie om uit te leveren?
2. Welke van de key results van je team zijn eigenlijk vermomde taken, en hoe zou je ze herschrijven?
3. Van welke systeemkwaliteitsattributen hangt je product af die nooit expliciet zijn gekwantificeerd?
4. Wat is het goedkoopste experiment dat je laatste mislukte functie had kunnen doden voordat je haar bouwde?
5. Hoe los je de spanning op tussen de vaste toezeggingen die begroting/aanbesteding eist en het leren dat goede uitkomsten vragen?
6. Welke van je KPI's zouden blijven stijgen zelfs als het product slechter werd?

## Belangrijkste inzichten

- De discoverypijplijn beslist *wat* en *waarom*, en definieert succes **voordat** oplevering middelen committeert.
- Gebruik **OKR's** voor de verandering die je wilt, **KPI's** voor de gezondheid die je volhoudt, en deel statistieken in als leidend of volgend.
- Behandel **systeemkwaliteitsattributen** als expliciete, gekwantificeerde, testbare eisen, geen aannames.
- Maak elk doel, key result en acceptatiecriterium **SMART**.
- Draai discovery **continu en parallel** aan oplevering. Valideer de riskantste aannames goedkoop.
- Het dominante rendement is **vermeden verspilling**: zowel bouwkosten als de eeuwige TCO van ongebruikte functies.
- Sluit de lus: opgeleverde **uitkomststatistieken** (hoofdstuk 11.2) zijn het primaire bewijs voor de volgende ronde discovery.

## Referenties en verder lezen

- *Measure What Matters*, by John Doerr (on OKRs).
- *Radical Focus*, by Christina Wodtke (on OKRs in practice).
- *Continuous Discovery Habits*, by Teresa Torres (opportunity-solution trees, dual-track discovery).
- *Inspired* and *Empowered*, by Marty Cagan (product discovery and outcome teams).
- *Lean Analytics*, by Alistair Croll and Benjamin Yoskovitz (leading indicators, vanity metrics).
- *The Lean Startup*, by Eric Ries (build-measure-learn, validated learning).
- *Escaping the Build Trap*, by Melissa Perri (outcomes over outputs).
- *Outcomes Over Output*, by Joshua Seiden.
- *Software Architecture in Practice*, by Bass, Clements, Kazman (quality attributes).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): origin of SMART criteria.
