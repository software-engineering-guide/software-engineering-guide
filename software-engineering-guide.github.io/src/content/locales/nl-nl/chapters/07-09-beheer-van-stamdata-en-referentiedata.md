# 7.9 Beheer van stamdata en referentiedata

## Overzicht en motivatie

Vraag vijf systemen hoeveel klanten de organisatie heeft, en je krijgt vijf verschillende getallen. Eén telt e-mailadressen, één telt contracten, één telt logins en twee verschillen van mening over of "Acme Corp" en "ACME Corporation" hetzelfde bedrijf zijn. [Stamdatabeheer](https://en.wikipedia.org/wiki/Master_data_management) (master data management, MDM) is de discipline van de kernentiteiten die je bedrijf deelt, klant, product, leverancier, medewerker, locatie, verzoenen tot één gezaghebbende versie die elk systeem kan vertrouwen.

Begin met je data te sorteren in drie soorten, omdat ze verschillende behandeling nodig hebben. Stamdata beschrijft de zelfstandige naamwoorden van je bedrijf: de mensen, plaatsen en dingen waar veel processen naar verwijzen. Referentiedata is het gecontroleerde vocabulaire dat die processen gebruiken: valutacodes, landcodes, lijsten van maateenheden, productcategorieën. Transactiedata legt de werkwoorden vast: een bestelling geplaatst, een betaling gedaan, een zending verstuurd. Stam- en referentiedata zijn lager in volume dan transacties maar overal gerefereerd, dus een fout erin besmet alles stroomafwaarts.

De kosten van het fout doen zijn concreet. Wanneer dezelfde klant bestaat als vier licht verschillende records, post je vier catalogi, kun je niet één relatie zien die het waard is te behouden en is je omzet-per-klantgetal stilletjes fout. Een [gouden record](https://en.wikipedia.org/wiki/Single_source_of_truth), de enkele vertrouwde versie van een entiteit samengesteld uit veel bronnen, is wat die conflicterende kopieën vervangt, zodat elke integratie ophoudt hetzelfde matchingprobleem opnieuw op te lossen.

Voor ondernemingen die systemen afstemmen die over decennia groei en overnames zijn opgehoopt is MDM het verschil tussen een samenhangend klantbeeld en een permanente afstemmingsbelasting. Voor de overheid stijgt de inzet: een burger die in drie instanties als drie verschillende mensen voorkomt kan een uitkering worden geweigerd, dubbel worden belast of tussen afdelingen zoekraken. Dit hoofdstuk vult datastrategie en datagovernance (hoofdstuk 7.1) aan, die eigenaarschap en beleid vaststelt, datamodellering en de semantische laag (hoofdstuk 7.7), die definieert wat entiteiten betekenen, en datakwaliteit en observeerbaarheid (hoofdstuk 7.8), die records in de tijd schoon houdt.

## Kernprincipes

- Sorteer je data in stam-, referentie- en transactiedata. Elk vraagt andere behandeling.
- Eén gouden record per entiteit uit de echte wereld, bewust samengesteld, niet bij toeval ontdekt.
- Kies een MDM-architectuurstijl die past bij je behoefte aan controle en latentie, niet bij de mode.
- Matching en overleving zijn bedrijfsregels, dus schrijf ze op en laat rentmeesters ze afstemmen.
- Referentiedata is gedeeld vocabulaire. Versioneer en publiceer haar als een API.
- Governance en rentmeesterschap zijn de motor van MDM. De software is slechts de tooling.
- Verspreid gouden records als gebeurtenissen zodat downstreamsystemen synchroon blijven, niet verouderd.
- Meet MDM aan verbeterde beslissingen en verwijderde duplicaten, niet aan geladen records.

## Aanbevelingen

### Classificeer eerst stam-, referentie- en transactiedata

Je kunt niet beheren wat je niet hebt gesorteerd, dus begin met je datadomeinen te classificeren. Een nuttige toets voor stamdata is of een foute waarde zich voortplant: als één slecht adres rimpelt in facturering, verzending en juridische kennisgevingen, kijk je naar stamdata. Dit drijft je investering: je bouwt een matchingengine voor de klantentiteit, niet voor orderregels. Benoem de domeinen expliciet, rangschik ze naar hoeveel pijn hun duplicatie veroorzaakt en begin met het ene of de twee die het meest pijn doen, meestal klant en product omdat ze omzet direct raken.

### Kies bewust een MDM-architectuurstijl

Er zijn vier gangbare architectuurstijlen, en de juiste hangt af van hoeveel gezag je kunt centraliseren en hoe snel wijzigingen moeten doorwerken. De registerstijl laat data in de bronsystemen en bouwt alleen een index van gematchte identifiers, zodat ze "deze vijf records zijn dezelfde klant" kan beantwoorden zonder data te verplaatsen. Ze is goedkoop en laag in risico, maar alleen-lezen, dus ze kan de bronnen niet repareren. De consolidatiestijl trekt kopieën in een centrale hub en voegt ze samen tot gouden records voor rapportage, maar duwt correcties niet terug, zodat de bronnen rommelig blijven. De coëxistentiestijl gaat verder: ze synchroniseert opgeschoonde waarden terug naar de bronsystemen, zodat de bronnen in de tijd verbeteren terwijl ze onafhankelijk blijven werken. De gecentraliseerde of transactionele hubstijl maakt de MDM-hub zelf het systeem van registratie, waar entiteiten direct worden aangemaakt en bewerkt en elk ander systeem eruit consumeert. Dit geeft de sterkste consistentie en controle, en is het moeilijkst over te nemen omdat het verandert waar werk gebeurt. Veel organisaties groeien van een register dat waarde bewijst naar coëxistentie naarmate vertrouwen groeit, en draaien meer dan één stijl over verschillende domeinen.

### Match, voeg samen en stel overlevingsregels expliciet vast

Het hart van MDM is beslissen wanneer twee records hetzelfde ding uit de echte wereld beschrijven. Dit is [recordkoppeling](https://en.wikipedia.org/wiki/Record_linkage), zelden zo eenvoudig als een exacte sleutelmatch omdat echte data vol typefouten, afkortingen en ontbrekende velden zit. Deterministische matching gebruikt exacte regels op gekozen velden (hetzelfde belastingnummer, of hetzelfde e-mailadres plus postcode). Probabilistische matching scoort gelijkenis over veel velden met [benaderende stringmatching](https://en.wikipedia.org/wiki/Approximate_string_matching) en gewichten, zodat "Bob Smith, 12 Main St" en "Robert Smith, 12 Main Street" boven een drempel als waarschijnlijke match kunnen worden beoordeeld. Beslissen welke records naar dezelfde entiteit verwijzen heet identiteitsresolutie, en het drijft alles van klantbeelden tot fraudedetectie.

Zodra records matchen, moet je beslissen welke waarden in het gouden record overleven. Deze overlevingsregels zijn bedrijfslogica, dus maak ze expliciet: geef de voorkeur aan de meest recente waarde voor een telefoonnummer, de meest complete waarde voor een adres, de meest vertrouwde bron voor een juridische naam. Stel een drempelband in waar matches automatisch worden samengevoegd, een lagere band waar ze automatisch worden afgewezen en een middenband waar een mens beslist, waar rentmeesterschap leeft. Houd elke samenvoeging omkeerbaar en gelogd, want een foute samenvoeging die twee echte klanten versmelt is erger dan een gemiste.

### Behandel referentiedata als geversioneerd gedeeld vocabulaire

Referentiedata is het gedeelde vocabulaire dat je systemen spreken, en vocabulaire dat afdrijft veroorzaakt stille misalignering: wanneer het ene systeem ISO-landcode "GB" gebruikt en het andere "UK", falen joins en lopen tellingen uiteen. Onderhoud elke referentielijst op één bestuurde plek, publiceer haar voor elke afnemer en, cruciaal, versioneer haar. Codes worden in de tijd toegevoegd, afgeschaft, gesplitst en samengevoegd, en als je de lijst ter plekke overschrijft, breek je historische rapporten die onder de oude codes juist waren.

Behandel een referentiedataset als een API met een contract. Publiceer haar met ingangsdata zodat een afnemer kan vragen "wat waren de geldige regiocodes op deze datum", bewaar afgeschafte codes in plaats van ze te verwijderen en leg de mapping vast wanneer een code van betekenis verandert. Geef de voorkeur aan erkende externe standaarden waar ze bestaan, zoals ISO-land- en valutacodes, omdat standaarden je interoperabiliteit gratis geven en aansluiten op de open-standaardendiscipline in hoofdstuk 3.8.

### Modelleer hiërarchieën en relaties, niet alleen platte records

Stamdata is geen hoop onafhankelijke rijen. Het is een web van relaties. Een klant hoort bij een huishouden en bij een moederbedrijf. Een product rolt op naar een categorie en een merk. Deze hiërarchieën dragen echte bedrijfsbetekenis: rol verkoop op naar moederbedrijf en het beeld verandert volledig vergeleken met oprollen per afzonderlijk account. Modelleer deze relaties expliciet zodat afnemers ze consistent doorlopen in plaats van dat elk team zijn eigen oprolling verzint.

Let op het geval waar één entiteit meerdere hiërarchieën tegelijk nodig heeft. Een product kan voor financiën op de ene manier oprollen en voor merchandising op een andere, en beide zijn legitiem, dus ondersteun meerdere benoemde hiërarchieën in plaats van één ware boom af te dwingen. Relaties tussen domeinen tellen ook, zoals welke leverancier welk product levert.

### Bedraad gouden records in de semantische laag en datakwaliteit

De gouden records die MDM produceert zijn de betrouwbare entiteiten waar de semantische laag van hoofdstuk 7.7 naar verwijst wanneer ze statistieken definieert: "actieve klanten" betekent pas iets wanneer "klant" ondubbelzinnig is. Voed je gouden records in de semantische laag zodat elke statistiek dezelfde ontdubbelde, opgeloste entiteiten telt.

MDM en datakwaliteit (hoofdstuk 7.8) zijn twee kanten van één munt: kwaliteitscontroles detecteren de duplicaten, lege waarden en opmaakschendingen die MDM dan oplost, en de matching van MDM brengt kwaliteitsproblemen naar boven die de controles misten. Draai continue kwaliteitsbewaking specifiek op je stamdata: duplicaatpercentages, verdelingen van matchzekerheid, volledigheid van sleutelvelden en de grootte van de reviewwachtrij, zodat afdrijving opduikt voordat afnemers het zien.

### Verspreid gouden records via gebeurtenissen

Een gouden record dat geen downstreamsysteem ziet helpt niemand. Het sterkste patroon is gebeurtenisgedreven verspreiding: wanneer een entiteit wordt aangemaakt, samengevoegd of gecorrigeerd, publiceert de MDM-hub een wijzigingsgebeurtenis, en abonnerende systemen werken hun lokale kopie bij. Dit bouwt voort op [gebeurtenisgedreven architectuur](https://en.wikipedia.org/wiki/Event-driven_architecture) en de streamingpatronen van hoofdstuk 7.2, tientallen systemen consistent houdend zonder kwetsbare nachtelijke batchsynchronisaties die iedereen een dag verouderd laten.

Publiceer de gebeurtenissen met genoeg context om nuttig te zijn: de entiteitsidentifier, wat veranderde, de nieuwe overlevende waarden en een versie zodat afnemers updates kunnen ordenen en gemiste kunnen detecteren. Maak afnemers idempotent zodat een gebeurtenis opnieuw afspelen geen kwaad doet, en bied een API voor systemen die niet kunnen abonneren. Het principe uit dataarchitectuur en opslag (hoofdstuk 3.4) geldt: ontwerp het gouden record zo dat het stroomt, want een record dat niemand consumeert is gewoon een dure spreadsheet.

### Wijs rentmeesterschap en governance toe vóór tooling

MDM faalt als technologieproject en slaagt als governanceproject. De cruciale rol is de [datarentmeester](https://en.wikipedia.org/wiki/Data_steward), een persoon verantwoordelijk voor de kwaliteit en regels van een specifiek domein, die dubbelzinnige matches oplost, overlevingsregels afstemt en arbitreert wanneer twee afdelingen het oneens zijn over wat "leverancier" betekent. Rentmeesters zijn meestal bedrijfsmensen met diepe domeinkennis, geen engineers, en ze hebben echt gezag en toegewezen tijd nodig, want deeltijdrentmeesterschap zonder mandaat produceert precies de afdrijving die MDM moest stoppen.

Wikkel de rentmeesters in de governancestructuren uit hoofdstuk 7.1: een data-eigenaar verantwoordelijk voor elk domein, een raad om domeinoverstijgende geschillen te beslechten en heldere beleidsregels over wie stamrecords mag aanmaken of samenvoegen. Documenteer de beslissingen, want de regels voor het matchen van een klant zijn institutionele kennis die personeelsverloop moet overleven. Tooling dient de governance. Een MDM-platform kopen voordat je je rentmeesters noemt is een motor kopen zonder bestuurder.

## Afwegingen: voor- en nadelen

| MDM-stijl | Voordelen | Nadelen |
|---|---|---|
| Register (alleen index) | Goedkoop, laag risico, bronnen onaangeroerd | Alleen-lezen. Kan brondata niet repareren |
| Consolidatie (centrale kopieën) | Snel schone records voor analytics | Bronnen blijven rommelig. Geen terugschrijven |
| Coëxistentie (terugsynchroniseren naar bronnen) | Bronnen verbeteren. Gebalanceerde controle | Meer integratie. Synchronisatieconflicten te beheren |
| Gecentraliseerd / transactionele hub | Sterkste consistentie en controle | Hoogste kosten. Verandert waar werk gebeurt |
| Deterministische matching | Voorspelbaar, uitlegbaar, controleerbaar | Mist typefouten, varianten en rommelige data |
| Probabilistische matching | Vangt variatie uit de echte wereld | Vraagt afstemming. Valse samenvoegingen bij onzorgvuldigheid |

De centrale spanning in MDM is controle tegenover verstoring. De stijlen die je de schoonste, meest consistente data geven (coëxistentie en gecentraliseerde hubs) zijn precies degene die het meest ingrijpen in hoe bronsystemen en hun eigenaren werken, en dat ingrijpen is waar MDM-programma's vastlopen. Het pragmatische pad is vertrouwen verdienen met een stijl met laag risico en alleen naar sterkere controle bewegen waar de zakelijke onderbouwing helder is. De matchingafweging loopt parallel: deterministische regels zijn controleerbaar maar broos, probabilistische scoring is krachtig maar vraagt rentmeesterschap en tolerantie voor de af en toe foute samenvoeging. De meeste volwassen programma's mengen beide.

## Vragen om met je team te bespreken

1. **Welke stamdatadomeinen veroorzaken ons werkelijk pijn, en hebben we ze gerangschikt naar kosten in plaats van ze allemaal tegelijk te behandelen?** Veel MDM-programma's storten in onder hun eigen ambitie, elke entiteit in de onderneming tegelijk willen beheren en twee jaar niets opleveren. De productieve zet is het ene of de twee domeinen te vinden waar duplicatie en conflict je echt geld of vertrouwen kosten, meestal klant of product, en die kosten te kwantificeren: de verspilde mailings, de afstemmingsuren, de foute omzetgetallen, de auditbevindingen. Neem concrete voorbeelden mee van dezelfde entiteit die op meerdere manieren over je systemen verschijnt, en laat die rangschikking vertellen waar te beginnen, want een smalle, meetbare winst bouwt de geloofwaardigheid die je nodig hebt om uit te breiden.

2. **Wie bezit elk stamdatadomein, en hebben onze rentmeesters het gezag en de tijd om het werk werkelijk te doen?** MDM-tooling zonder gemachtigd rentmeesterschap is een auto zonder bestuurder, en het gangbaarste faalpatroon is een rentmeester op een dia noemen terwijl je hem geen echt mandaat en geen toegewezen uren geeft. De mensen die dubbelzinnige matches oplossen en discussies over "wat telt als klant" beslechten hebben domeinexpertise, beslisgezag en beschermde tijd nodig. Neem je organigram mee en vraag voor je topdomein precies wie beslist wanneer twee records dezelfde persoon zijn en wie arbitreert wanneer verkoop en financiën het oneens zijn. Als je die persoon niet kunt noemen en op zijn toegewezen tijd kunt wijzen, heb je het gat gevonden dat het programma zal laten zinken.

3. **Wanneer we twee records tot een gouden record samenvoegen, kunnen we de beslissing dan uitleggen en terugdraaien, en waar komen de overlevende waarden vandaan?** Overlevingsregels zijn bedrijfslogica die de meeste teams nooit hebben opgeschreven, wat betekent dat samenvoegingen gebeuren door toeval van laadvolgorde of toolingstandaarden, en een foute samenvoeging die twee echte klanten versmelt pijnlijk is terug te draaien. Neem een echt samengevoegd record mee en traceer elk overlevend veld terug naar zijn bron en regel: waarom dit adres, waarom deze naam, waarom dit telefoonnummer. Bevestig dat elke samenvoeging is gelogd en omkeerbaar, en dat een middenband van onzekere matches naar een mens gaat in plaats van automatisch wordt samengevoegd. Als je een specifiek gouden record niet kunt uitleggen, kunnen je rentmeesters het niet verdedigen tegenover een auditor of een benadeelde klant.

4. **Welke MDM-architectuurstijl past bij elk domein dat we willen beheren, en kunnen we die keuze verdedigen tegen de verstoring die ze oplegt aan eigenaren van bronsystemen?** De stijl die je kiest bepaalt hoeveel je de data kunt opschonen en hoeveel je ingrijpt in de teams die de bronnen bezitten, en kiezen op mode of leverancierspraatje in plaats van op de realiteit van controle tegenover verstoring is hoe programma's halverwege vastlopen. Een register bewijst goedkoop waarde maar repareert nooit een bron. Een gecentraliseerde hub geeft de sterkste consistentie maar verplaatst waar records worden aangemaakt, wat een organisatieverandering is vermomd als technische. Neem voor elk kandidaatdomein een eerlijke lezing mee van hoeveel gezag je werkelijk hebt over de broneigenaren, hoe vers downstreamkopieën moeten zijn en wat een terugschrijven zou breken in bestaande workflows. Voeg in omgevingen van onderneming en overheid de migratie- en verandermanagementkosten toe van het verplaatsen van het systeem van registratie, want de teams wier dagelijks werk verhuist zullen zich verzetten tegen een hub waarover ze niet zijn geraadpleegd, en een vastgelopen coëxistentie-uitrol is duurder dan een bescheiden register dat wordt opgeleverd.

5. **Hoe stemmen we de matchingdrempels af, en hebben we afgesproken met welk percentage valse samenvoegingen en gemiste matches we kunnen leven in elk domein?** Elke probabilistische matchingengine ruilt valse samenvoegingen (twee echte entiteiten versmelten) tegen gemiste matches (één entiteit gesplitst laten), en de balans is een bedrijfsbeslissing, geen standaard die iemand in de tool liet staan. Stel de banden voor automatisch samenvoegen en automatisch afwijzen te breed in en je corrumpeert gouden records stilletjes. Stel ze te smal in en de menselijke reviewwachtrij groeit sneller dan rentmeesters kunnen wegwerken. Neem de huidige zekerheidsverdeling mee, de grootte en leeftijd van de reviewwachtrij en voorbeeldfouten van beide soorten zodat de kamer de echte kosten van elke richting kan zien. Neig in een overheidsidentiteitsdomein hard naar gemiste matches en menselijke review, want een foute samenvoeging kan een uitkering ontzeggen of de data van de ene burger aan een andere blootstellen, en de beroeps- en auditkosten van die fout overtreffen de kosten van een duplicaat dat een rentmeester volgende week oplost ruim.

6. **Hoe komen downstreamsystemen te weten dat een gouden record veranderde, en hoe verouderd kan elk zijn voordat een beslissing misgaat?** Een perfect opgelost gouden record dat geen systeem consumeert is een dure spreadsheet, en het verspreidingsmechanisme, of dat nu wijzigingsgebeurtenissen zijn, een abonnement-API of een nachtelijke batch, stelt stilletjes vast hoe actueel elke afhankelijke beslissing is. Gebeurtenisgedreven verspreiding houdt tientallen afnemers bijna realtime bij maar vraagt idempotente afnemers en geversioneerde gebeurtenissen. Een nachtelijke synchronisatie is eenvoudiger maar laat iedereen een dag verouderd, wat prima kan zijn voor een marketinglijst en gevaarlijk voor een fraudecontrole. Neem de lijst consumerende systemen mee, de versheid die elk werkelijk nodig heeft en hoe een afnemer die vandaag een update mist herstelt. Noem voor een grote of publieke organisatie wie het contract voor deze gebeurtenissen bezit en hoe een abonnee een verloren bericht detecteert, want een entiteitswijziging die één instantie stilletjes niet bereikt herschept precies de fragmentatie die MDM werd gefinancierd om weg te nemen.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen runway te sparen koop je geen MDM-platform. Beheer de ene entiteit die je getallen corrumpeert, meestal de klant gedupliceerd over self-serve en verkoop, met een matchingjob in het warehouse dat je al draait en één persoon die wekelijks onzekere matches beoordeelt. Houd elke samenvoeging gelogd en omkeerbaar zodat een slechte regel een middag kost, geen klantrelatie, en heroverweeg zwaardere tooling pas wanneer de handmatige reviewwachtrij één reviewer ontgroeit.

**Kleinbedrijf.** Je hebt geen datarentmeester en een krap budget, dus behandel dit als kopen-niet-bouwenbeslissing en leun op standaarden die je gratis krijgt. Geef de voorkeur aan tools die contacten al ontdubbelen en ISO-land- en valutacodes spreken boven een maatwerkhub die je niet kunt onderhouden, en kies het ene domein, meestal klanten of producten, waar duplicaten je echt geld kosten. Wijs de verantwoording toe aan een benoemde eigenaar, zelfs als het een fractie van de week van één persoon is, want vocabulaire dat afdrijft terwijl niemand kijkt is wat je rapporten stilletjes breekt.

**Grote onderneming.** Over een dozijn ERP- en CRM-systemen opgehoopt door overnames is het werk portfoliogovernance: rangschik domeinen naar de kosten van hun duplicatie, zet gemachtigde rentmeesters op in het bedrijf en standaardiseer overlevingsregels en versiebeheer van referentiedata zodat groepen ophouden hetzelfde matchingprobleem opnieuw op te lossen. Begroot de integratie en permanente rentmeesterschapskosten expliciet, verspreid gouden records als geversioneerde gebeurtenissen zodat bronnen in de tijd verbeteren en beheer MDM als gemeten programma met duplicaatpercentages en reviewwachtrijstatistieken in plaats van eenmalige opschoning.

**Overheid.** Aanbestedingsregels, strikte wetgeving over datadeling en publieke verantwoording geven elke keuze vorm. Sleutel de persoonsentiteit op een bestuurde nationale identifier, versioneer referentiedata naar ingangsdatum zodat historische records juist blijven en maak identiteitsresolutie bewust conservatief: onzekere matches gaan naar getrainde rentmeesters, nooit naar geautomatiseerde samenvoegingen, omdat een foute samenvoeging een uitkering kan ontzeggen of de data van de ene burger aan een andere kan lekken. Log elke match voor audit en beroep, eis overdraagbaarheid van data en bekendgemaakte matchinglogica van leveranciers en houd het hele vermogen binnen de interoperabiliteitsstandaarden waaraan de publieke sector zich al bindt.

## Voorbeelden

**Startup.** Een snelgroeiend softwarebedrijf verkoopt zowel via self-serve aanmelding als een verkoopteam, en de twee kanalen creëren dezelfde klant tweemaal onder licht verschillende bedrijfsnamen. Omzet-per-account ziet er fout uit en het verkoopteam blijft bestaande gebruikers koud bellen. In plaats van een zwaar platform te kopen beginnen ze met een lichtgewicht register: een matchingjob in hun datawarehouse die records koppelt op e-maildomein en genormaliseerde bedrijfsnaam, met één deeltijdrentmeester die onzekere matches wekelijks beoordeelt. Het kost weinig, repareert de rapportagefout en bewijst de waarde die meer investering rechtvaardigt naarmate ze groeien.

**Grote onderneming.** Een wereldwijde fabrikant is gegroeid door overnames en draait een dozijn ERP- en CRM-systemen, elk met eigen leveranciersrecords, zodat dezelfde leverancier op vijftien manieren verschijnt en het bedrijf niet als één koper kan onderhandelen of zijn ware uitgaven kan zien. Ze zet een MDM-hub in coëxistentiestijl op voor de leveranciers- en productdomeinen, met deterministische matching op belasting- en registratie-identifiers plus probabilistische scoring op namen en adressen. Benoemde rentmeesters in inkoop stemmen de overlevingsregels af en werken de reviewwachtrij weg, en gouden records worden gepubliceerd als wijzigingsgebeurtenissen die terugvloeien in elk ERP zodat opgeschoonde data de bronnen verbetert. Geconsolideerd zicht op uitgaven ontsluit betere contractvoorwaarden, en de afstemmingsbelasting die elk kwartaal financiën opslokte daalt sterk.

**Overheid.** Een nationale overheid wil dat instanties een burger behandelen als één persoon in plaats van een vreemde aan elk loket, met inachtneming van strikte wettelijke grenzen aan datadeling. Ze bouwt een gecentraliseerde stamdatahub voor de persoonsentiteit, gesleuteld op een bestuurde nationale identifier, met referentiedata geversioneerd naar ingangsdatum zodat historische records juist blijven. Identiteitsresolutie is bewust conservatief: onzekere matches gaan naar getrainde rentmeesters in plaats van geautomatiseerde samenvoegingen, omdat een foute samenvoeging iemand een uitkering kon ontzeggen of zijn data blootstellen, en elke match wordt gelogd voor audit en beroep. De opbrengst is minder gedupliceerde records, minder fraude uit gesplitste identiteiten en een burger die niet bij elke deur hoeft te bewijzen wie hij is, binnen de interoperabiliteitsstandaarden van hoofdstuk 3.8.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van MDM komt uit het wegnemen van een belasting die de meeste organisaties betalen zonder haar te noemen. Dubbele en conflicterende records kosten geld op voor de hand liggende manieren (verspilde marketing aan dezelfde persoon vijf keer, verzendfouten door verouderde adressen, gemiste volumekortingen) en op minder voor de hand liggende (analisten die tellingen afstemmen, bestuurders die beslissen op getallen die stilletjes fout zijn, auditors die uren declareren om uit te zoeken welk record echt is). Een geconsolideerd leveranciersbeeld betaalt vaak het hele programma terug alleen al via betere contractvoorwaarden.

De total cost of ownership heeft drie delen: het platform of de bouw, de integratie met bronnen en afnemers en, het grootst op de lange termijn, het doorlopende rentmeesterschap. De integratiekosten zijn makkelijk te onderschatten, omdat een dozijn verouderende bronsystemen verbinden waar MDM-programma's planning en budget bloeden, en de rentmeesterschapskosten zijn makkelijk te vergeten, omdat het een permanente operationele uitgave is, geen eenmalige bouw. Verbind MDM voor het bestuur aan getallen die ze al volgen: omzetnauwkeurigheid, marketingefficiëntie, inkoopbesparingen, auditkosten en regelgevend risico, en begin dan smal en laat een gemeten winst op één domein met veel pijn de uitbreiding financieren.

## Antipatronen en valkuilen

- **Scope om de oceaan te koken:** alle domeinen tegelijk beheren, jarenlang niets opleveren en sponsorschap verliezen vóór de eerste winst.
- **Tooling vóór governance:** een MDM-platform kopen voordat je rentmeesters en eigenaren noemt, zodat de motor geen bestuurder heeft.
- **Deeltijdrentmeesters zonder gezag:** rentmeesterschap op een dia toewijzen zonder echt mandaat of beschermde tijd.
- **Stille overleving:** records samenvoegen op toolingstandaard of laadvolgorde, zonder geschreven regels en zonder manier een gouden record uit te leggen.
- **Onomkeerbare samenvoegingen:** onzekere matches automatisch samenvoegen zonder ongedaan maken, zodat een foute versmelting van twee echte entiteiten blijvende schade wordt.
- **Referentiedata ter plekke overschreven:** codelijsten bewerken zonder versiebeheer, wat elk historisch rapport breekt dat onder de oude codes juist was.
- **Gouden records die niemand consumeert:** een pristine hub bouwen waar geen downstreamsysteem op abonneert, zodat de schone data beslissingen nooit bereikt.
- **Standaardcodes opnieuw uitvinden:** eigen land- of valutalijsten munten terwijl ISO-standaarden bestaan, en interoperabiliteit verliezen zonder reden.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Stam- en referentiedata zijn onbeheerd. Dezelfde entiteit bestaat vele malen zonder gezaghebbende versie, codelijsten lopen uiteen, matching is handmatig en reactief en niemand bezit het probleem, zodat tellingen van kernentiteiten het oneens zijn en niemand kan zeggen welke juist is.
- **Niveau 2, Ontwikkelen:** Sleuteldomeinen worden erkend en iemand ontdubbelt ze, vaak in het warehouse voor rapportage. Basis-deterministische matching bestaat, referentielijsten worden verzameld en enkele mensen fungeren als informele rentmeesters, maar de praktijk varieert per team, de bronnen blijven rommelig en regels leven in hoofden in plaats van op papier.
- **Niveau 3, Standaardiseren:** MDM is een bestuurd programma consistent toegepast over de organisatie. Stamdomeinen hebben benoemde eigenaren en gemachtigde rentmeesters, matching- en overlevingsregels zijn gedocumenteerd en afgedwongen, gouden records worden geproduceerd en verspreid naar afnemers, en referentiedata is geversioneerd en gepubliceerd met ingangsdata als een API.
- **Niveau 4, Beheersen:** Het programma wordt gemeten en beheerst aan de hand van uitgangswaarden. Duplicaatpercentages, verdelingen van matchzekerheid, percentages valse samenvoegingen en gemiste matches, volledigheid van sleutelvelden en grootte en leeftijd van de reviewwachtrij worden als statistieken gevolgd. Drempels worden afgestemd op die getallen in plaats van op gevoel. En MDM-waarde (omzetnauwkeurigheid, inkoopbesparingen, reviewkosten) wordt gekwantificeerd en volgens vast ritme aan eigenaren gerapporteerd.
- **Niveau 5, Orkestreren:** Gouden records stromen als geversioneerde gebeurtenissen bijna realtime, voeden de semantische laag en worden organisatiebreed vertrouwd. Matching wordt continu verbeterd tegen gemeten uitkomsten, beheer breidt zich uit naar nieuwe domeinen als herhaalbaar vermogen en MDM is geïntegreerd met governance en risicoplanning zodat het programma zich aanpast naarmate bronnen, standaarden en het entiteitenlandschap verschuiven.

## Ideeën voor discussie

1. Als twee van je systemen het oneens zijn over hoeveel klanten je hebt, welke is juist, en hoe zou je dat bewijzen?
2. Welk stamdatadomein zou de grootste meetbare winst opleveren als je het eerst beheerde, en wat is die winst waard?
3. Waar zou probabilistische matching je vandaag helpen, en ben je comfortabel met de af en toe foute samenvoeging die het impliceert?
4. Hoe versioneer je je referentiedata, en wat breekt er in je historische rapporten wanneer een code van betekenis verandert?
5. Wie is de benoemde rentmeester voor je belangrijkste entiteit, en heeft die het gezag en de tijd om het werk werkelijk te doen?
6. Wanneer een gouden record verandert, hoe komen je downstreamsystemen het te weten, en hoe verouderd kunnen ze zijn voordat het pijn doet?

## Belangrijkste inzichten

- Sorteer je data in stam-, referentie- en transactiedata. Investeer matching en governance waar duplicatie het meest kost.
- Produceer één gouden record per entiteit uit de echte wereld, samengesteld door expliciete, omkeerbare, gelogde overlevingsregels.
- Kies een MDM-architectuurstijl (register, consolidatie, coëxistentie of gecentraliseerde hub) die past bij je honger naar controle en je tolerantie voor verstoring.
- Behandel referentiedata als geversioneerd gedeeld vocabulaire, geef de voorkeur aan erkende standaarden en overschrijf codelijsten nooit ter plekke.
- MDM slaagt op governance en rentmeesterschap, niet op tooling. Verspreid gouden records als gebeurtenissen en meet het programma aan verbeterde beslissingen.

## Referenties en verder lezen

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
