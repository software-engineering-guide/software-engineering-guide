# 3.9 Systeemengineering

## Overzicht en motivatie

[Systeemengineering](https://en.wikipedia.org/wiki/Systems_engineering) is de discipline van een heel complex systeem van begin tot eind engineeren, zodat al zijn delen samenwerken om aan een echte behoefte te voldoen. De delen omvatten veel meer dan software. Een modern systeem combineert doorgaans software, hardware, mensen, data en processen, en moet opereren in een rommelige echte wereld. Systeemengineering houdt dit alles op elkaar afgestemd over het hele leven van het systeem.

Dit verschilt van softwarearchitectuur. Softwarearchitectuur (hoofdstuk 3.1) beslist hoe softwarecomponenten zijn gestructureerd en hoe ze met elkaar praten. Systeemengineering zit een niveau hoger. Het vraagt wat het systeem als geheel moet doen, hoe software en hardware en menselijke operators het werk verdelen en hoe je zult bewijzen dat het afgewerkte ding werkt. Zijn professionele thuis is [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), de International Council on Systems Engineering, en zijn ankerstandaard is [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), die de processen voor het leven van een systeem definieert.

Dit doet ertoe voor grote programma's van onderneming en overheid omdat hun systemen groot, langlevend en veiligheidskritiek of missiekritiek zijn. Een defensieplatform, een luchtverkeerssysteem of een satellietconstellatie mengt maatwerkhardware, onderdelen van derden, embedded en cloudsoftware en menselijke operators, en geen enkel team kan het geheel in zijn hoofd houden. Je bouwt ook vaak een [systeem van systemen](https://en.wikipedia.org/wiki/System_of_systems): veel onafhankelijke systemen, elk op zichzelf nuttig, die moeten samenwerken om een groter vermogen te leveren.

Dit hoofdstuk sluit aan op softwarevereisten (hoofdstuk 2.8), architectuurfundamenten (hoofdstuk 3.1), softwaremodellen en -methoden (hoofdstuk 2.12), interoperabiliteit en open standaarden (hoofdstuk 3.8) en projectmanagement (hoofdstuk 10.6).

## Kernprincipes

- **Engineer het geheel, niet de delen.** Een systeem slaagt of faalt als geheel, dus één subsysteem geïsoleerd optimaliseren kan het geheel slechter maken.
- **Volg de levenscyclus.** Een systeem heeft een leven van eerste concept tot definitieve uitfasering. Plan voor alles, niet alleen de bouw.
- **Herleid elke vereiste.** Elke behoefte moet worden afgebeeld op een vereiste, een ontwerpelement en een test. Als je het niet kunt herleiden, kun je het niet bewijzen.
- **Beheer interfaces met opzet.** De meeste falen gebeuren aan de grenzen tussen delen, dus interfaces verdienen expliciet eigenaarschap en beheersing.
- **Verifieer en valideer apart.** Het ding goed bouwen (verificatie) en het juiste ding bouwen (validatie) zijn verschillende vragen, en je hebt beide antwoorden nodig.
- **Verwacht emergent gedrag.** Delen combineren schept gedrag dat geen enkel deel vertoont. Een deel ervan is het doel, een deel is een nare verrassing.
- **Co-engineer hardware en software.** Wanneer beide maatwerk zijn, beperken beslissingen in de een de ander, dus plan ze samen.

## Aanbevelingen

### Beheer de volledige systeemlevenscyclus

Behandel het systeem als een geheel leven hebbend en plan elke fase. Een gangbare levenscyclus loopt: **concept** (de behoefte begrijpen en opties verkennen), **vereisten** (precies stellen wat het systeem moet doen), **ontwerp** (de architectuur en de delen vaststellen), **integratie** (de delen samenbrengen), **verificatie en validatie** (bewijzen dat het werkt en het juiste systeem is), **bedrijf** (het draaien en onderhouden) en **uitfasering** (het veilig ontmantelen, inclusief data en afvoer). ISO/IEC/IEEE 15288 geeft je daarvoor een procesraamwerk. De fasen hoeven geen starre waterval te zijn. Je kunt itereren, prototypen en in incrementen opleveren. Het punt is dat je elke fase bewust aanpakt, inclusief de dure latere die vroege plannen vaak negeren.

### Leg behoeften van stakeholders vast en wijs vereisten toe met traceerbaarheid

Begin bij de mensen die om het systeem geven: gebruikers, operators, eigenaren, toezichthouders en het publiek. Verzamel hun **behoeften** in gewone taal en zet die behoeften dan om in geëngineerde **vereisten** die specifiek en testbaar zijn (zie hoofdstuk 2.8). Dan komt **vereistentoewijzing**: elke vereiste op systeemniveau aan een specifiek subsysteem toewijzen, zodat je weet welk deel verantwoordelijk is voor het halen ervan. Houd een **[traceerbaarheids](https://en.wikipedia.org/wiki/Requirements_traceability)matrix** bij, een levend register dat elke behoefte koppelt aan zijn vereiste, aan het ontwerpelement dat eraan voldoet en aan de test die het verifieert. Zo kun je op elk moment bewijzen dat elke behoefte gedekt is en elk deel een reden heeft om te bestaan.

### Beheer interfaces expliciet

Interfaces zijn waar delen elkaar ontmoeten, en waar systemen het vaakst breken. Een interface kan een fysieke connector zijn, een netwerkprotocol, een dataformaat of een menselijke procedure. Schrijf voor elk een **Interface Control Document** (ICD): een afgesproken specificatie van precies hoe twee delen verbinden en informatie uitwisselen. Geef elke interface aan elke kant een heldere eigenaar. Leunen op gedeelde, gepubliceerde specificaties in plaats van eenmalige connectoren maakt integratie veel makkelijker, wat het interoperabiliteitsargument in hoofdstuk 3.8 is. Bevries interfaces vroeg waar je kunt, want een late wijziging rimpelt door naar elk deel dat ze raakt.

### Integreer en verifieer en valideer dan

**Systeemintegratie** combineert subsystemen tot het werkende geheel, meestal in fasen in plaats van alles tegelijk, zodat je problemen vindt terwijl ze nog klein zijn. Na integratie komt **[verificatie en validatie](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), twee aparte controles. **Verificatie** vraagt: hebben we het systeem goed gebouwd, dat wil zeggen voldoet het aan zijn gespecificeerde vereisten? Je verifieert via inspectie, analyse, demonstratie en test. **Validatie** vraagt: hebben we het juiste systeem gebouwd, dat wil zeggen voldoet het aan de echte behoeften van de stakeholders in echt gebruik? Een systeem kan verificatie doorstaan (het voldoet aan de spec) en toch validatie falen (de spec was fout). Plan beide vroeg, en schrijf vereisten en interfaces zo dat ze überhaupt kunnen worden geverifieerd.

### Neem modelgebaseerde systeemengineering aan

Traditionele systeemengineering produceerde bergen documenten die uit de pas liepen. **[Modelgebaseerde systeemengineering](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) vervangt die stapel door één enkel, gedeeld, formeel model van het systeem, waaruit gezichtspunten en rapporten worden gegenereerd. De gangbare modelleertaal is **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), een grafische taal om de vereisten, structuur, gedrag en beperkingen van een systeem te beschrijven. Omdat alles in één verbonden model leeft, werkt een wijziging overal door en wordt traceerbaarheid een query in plaats van een handmatige zoektocht. MBSE sluit aan op de modelleerideeën in hoofdstuk 2.12. Neem het geleidelijk aan, beginnend met de delen met het hoogste risico waar een gedeeld model zich het snelst uitbetaalt.

### Pas systeemdenken toe op emergent gedrag

Oefen [systeemdenken](https://en.wikipedia.org/wiki/Systems_thinking): redeneer over het geheel en de relaties tussen delen, niet alleen over de delen één voor één. Zo anticipeer je op **[emergent gedrag](https://en.wikipedia.org/wiki/Emergence)**: eigenschappen die alleen verschijnen wanneer delen combineren en die geen enkel deel vertoont. Goede emergentie is vaak het doel van het systeem (een zwerm drones dekt een gebied dat geen enkele drone kan). Slechte emergentie is het verrassende falen (twee veilige subsystemen werken zo op elkaar in dat ze een gevaarlijke toestand creëren). Je kunt emergentie niet uit een systeem wegtesten dat je nooit modelleerde, dus gebruik simulatie en gestructureerde gevarenanalyse om het te vinden voor het bedrijf.

### Co-engineer hardware en software

Wanneer een systeem maatwerkhardware bevat, engineer de hardware en software dan samen, een praktijk genaamd **[hardware/software-co-design](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Beslissingen binden elkaar: de hardware stelt timing-, geheugen- en stroomlimieten waarbinnen de software moet leven, en de behoeften van de software bepalen wat de hardware moet bieden. Lange levertijden van hardware drijven ook de planning. Besluit vroeg welke functies in hardware en welke in software leven, en herzie die verdeling naarmate beperkingen opduiken.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen / kosten |
|---|---|---|
| Volledige rigueur van systeemengineering | Minder late verrassingen, sterke traceerbaarheid, veiliger en controleerbaar | Hoge kosten vooraf, tragere start, zwaar proces |
| Lichte / alleen-software-aanpak | Snel, goedkoop, flexibel voor kleine reikwijdte | Valt uiteen bij grote multidisciplinaire systemen, mist interfaces en emergentie |
| Modelgebaseerd (MBSE) | Eén bron van waarheid, makkelijke traceerbaarheid, consistente gezichtspunten | Kosten van tooling en training, cultuurverandering, leercurve |
| Documentgebaseerde systeemengineering | Vertrouwd, lage toolingkosten, makkelijk te delen | Documenten lopen uit de pas, traceerbaarheid is handmatig en foutgevoelig |

De centrale afweging is rigueur tegenover snelheid. Volledige systeemengineering legt inspanning vooraf in concept-, vereisten- en interfacewerk. Die inspanning betaalt zich vele malen terug bij grote, langlevende, veiligheidskritieke systemen, waar een defect gevonden in bedrijf duizenden keren meer kan kosten dan hetzelfde defect gevonden in vereisten. Bij een klein, kortlevend, alleen-softwareproduct is die rigueur overdreven. Stem het gewicht van je proces af op de omvang, levensduur en het risico van het systeem. De faalwijze is wegwerpprojectgewoonten toepassen op een systeem dat dertig jaar zal draaien en echt risico draagt.

## Vragen om met je team te bespreken

1. **Waar heb je precies gebouwd wat de spec eiste en toch het verkeerde systeem opgeleverd, en wat had het gevangen?** Verificatie (hebben we het goed gebouwd) en validatie (hebben we het juiste gebouwd) beantwoorden verschillende vragen, en een systeem kan elke verificatietest doorstaan en toch validatie falen omdat de spec zelf fout was. Bij grote programma's worden de twee samengeklapt tot "testen", zodat niemand tot laat tegen de echte operatorbehoefte valideert, wanneer een oplossing duizenden keren meer kost dan een vereistenwijziging. Neem een eerder voorbeeld mee waar het opgeleverde systeem aan zijn vereisten voldeed maar de werkelijke behoefte miste, en vraag welke validatieactiviteit (een simulatie met echte operators, een vroeg prototype in het veld) het eerder aan het licht had gebracht. Plan beide controles vanaf het begin, en schrijf vereisten en interfaces zo dat ze überhaupt kunnen worden geverifieerd. Het onderscheid bepaalt waar je schaarse reviewinspanning besteedt.

2. **Hoe jaag je op slecht emergent gedrag voordat het systeem in bedrijf is, niet erna?** Veilige subsystemen combineren kan gevaarlijke toestanden creëren die geen enkel deel vertoont, en je kunt emergentie niet uit een systeem wegtesten dat je nooit modelleerde. Voor een veiligheidskritiek of missiekritiek programma is de verrassende interactie degene die iemand verwondt of de missie laat mislukken, dus ze moet worden gevonden voor live bedrijf. Neem je aanpak mee om het geheel te modelleren (simulatie, gestructureerde gevarenanalyse, een SysML-model dat interacties vastlegt) en vraag welk gedrag over subsystemen heen je werkelijk hebt verkend tegenover wegaangenomen. Goede emergentie is vaak het doel van het systeem en het waard om naartoe te ontwerpen. Slechte emergentie is het falen waartegen je moet engineeren. Als je enige integratiestrategie is de delen aan elkaar te koppelen en te kijken wat er gebeurt, plan je emergentie in productie te ontdekken.

3. **Wanneer moeten de beslissingen over hardware met lange levertijd worden bevroren, en hoe stuurt die deadline je softwareplanning?** Wanneer een systeem maatwerkhardware bevat, moeten de twee samen worden geëngineerd: de chip stelt timing-, geheugen- en stroomplafonds waarbinnen de software leeft, en levertijden van hardware domineren vaak de hele planning. Teams die software als scheidbaar behandelen optimaliseren lokaal en botsen dan bij integratie op hardwarebeperkingen, wat maanden kost. Neem de levertijden van hardware mee en de datum waarop de verdeling van functies tussen hardware en software moet worden besloten, en herzie die verdeling naarmate beperkingen opduiken in plaats van haar blind te bevriezen. Hoe eerder je besluit welke functies in silicium en welke in software leven, hoe minder dure omkeringen je tegenkomt. De interfaces tussen de twee verdienen een Interface Control Document en een eigenaar aan elke kant, want een late wijziging daar rimpelt door alles wat ze raakt.

4. **Kun je één behoefte van een stakeholder helemaal herleiden naar de vereiste, het ontwerpelement en de test die het bewijst, en wie houdt die schakel in leven?** Traceerbaarheid is wat je op elk moment laat tonen dat elke behoefte gedekt is en elk deel een reden heeft om te bestaan, maar bij een groot programma verrot de matrix zodra niemand haar bezit. De concurrerende trek is echt: engineers ervaren traceerbaarheid als bureaucratische overhead, en een met de hand bijgehouden matrix drijft sneller uit de pas dan het ontwerp verandert. Neem één echte draad uit een huidig programma mee en probeer hem in de kamer van begin tot eind te lopen, van een benoemde stakeholderbehoefte, naar de toegewezen vereiste, naar het subsysteem en ontwerpelement dat eraan voldoet, naar de verificatietest, en noteer waar de keten breekt. Besluit wie de matrix bezit en of ze in een model moet leven waar traceerbaarheid een query is in plaats van een handmatige zoektocht. Voor programma's van onderneming en overheid is de matrix ook het auditartefact dat toezichthouders en aanbestedende autoriteiten eisen, dus een gebroken keten vertraagt niet alleen de engineering. Ze kan certificering of betaling stilleggen.

5. **Is een modelgebaseerde aanpak zijn tooling- en cultuurkosten waard voor jou, of zou ze dure shelfware worden?** Documentgebaseerde systeemengineering is vertrouwd en goedkoop te voorzien van tooling, maar zijn documenten lopen uit de pas en zijn traceerbaarheid is handmatig en foutgevoelig. MBSE vervangt de stapel door één verbonden model, tegen de prijs van tooling, training en een echte cultuurverandering. Beide uitersten zijn duur: sla MBSE over bij een groot multidisciplinair programma en je betaalt in integratieverrassingen, neem het aan zonder de discipline om het model actueel te houden en het rot weg tot shelfware die erger is dan geen model. Neem een eerlijke lezing mee van je toolingvolwassenheid, wie in het team werkelijk een SysML-model kan schrijven en onderhouden en welk ene subsysteem met hoog risico de aanpak kan pilotten waar een gedeeld model zich het snelst uitbetaalt. Besluit geleidelijk in plaats van de hele organisatie tegelijk te verplichten. Weeg voor een groot ondernemings- of overheidsprogramma met veel leveranciers af of een gedeeld model de enige realistische manier is om vereisten, interfaces en tests consistent te houden over aannemers die anders verouderde documenten uitwisselen.

6. **Financiert je levenscyclusplan bedrijf en uitfasering serieus, of stopt het stilletjes bij de lancering?** De fasen die de totale kosten van een langlevend systeem domineren, het decennialang draaien en het veilig ontmantelen, zijn degene die vroege plannen routinematig negeren, omdat de druk altijd is op te leveren. De concurrerende overweging is dat geld en aandacht het schaarst zijn precies wanneer deze latere fasen het verst weg voelen, dus bedrijf, onderhoud, datamigratie en afvoer worden uitgesteld tot ze een dure, riskante haast worden. Neem het huidige levenscyclusplan mee en controleer of het eigenaren, budgetten en uitstapcriteria noemt voor bedrijf en uitfasering, of dat het de lancering als finishlijn behandelt. Vraag wat er met de data en de hardware gebeurt aan het einde van de levensduur, en wie de jaren onderhoud ertussenin betaalt. Voor systemen van onderneming en overheid die twintig of dertig jaar moeten draaien en dan onder publieke toetsing uitfaseren, kan een ongeplande ontmanteling regelgevende, milieu- of bewaartermijnverplichtingen schenden, dus uitfasering hoort vanaf de eerste conceptreview in het plan en het budget.

## Sectorperspectief

**Startup.** Een piepklein team kan geen formeel systeemengineeringprogramma draaien en moet het niet proberen, maar kan firmware, app en cloud toch behandelen als één systeem in plaats van drie aparte projecten. Schrijf één kort interfacedocument dat vastpint hoe de delen praten, houd een eenvoudige tabel bij die elke klantbehoefte koppelt aan het deel dat eraan voldoet en sla het zware proces over. Je schaarsste middel is engineeringaandacht, dus besteed traceerbaarheidsinspanning alleen waar een foute aanname aan een grens het product in het veld stilletjes zou breken.

**Kleinbedrijf.** Zonder aparte systeemengineer en met een krap budget leun je op gepubliceerde standaarden en gekochte subsystemen in plaats van maatwerkintegratie die je zelf moet ontwerpen en verifiëren. Geef de voorkeur aan leveranciers die heldere interfacespecificaties blootleggen zodat de delen passen zonder een maatwerkconnector die je voor altijd moet bezitten. Formuleer de keuze tussen bouwen en kopen rond welke interfaces je realistisch kunt beheersen en verifiëren over de levensduur van het product, en koop de rest.

**Grote onderneming.** Op schaal is het probleem consistentie over veel teams en leveranciers: een gedeeld levenscyclusproces afgestemd op ISO/IEC/IEEE 15288, een Interface Control Document en een benoemde eigenaar voor elke leveranciersgrens, en traceerbaarheid van begin tot eind zodat één componentwijziging geen programmabrede haast triggert. Investeer in MBSE waar een gedeeld model vereisten, interfaces en tests afgestemd houdt over aannemers. Bestuur het proces zodat verificatie en validatie gescheiden blijven en elke vereiste is toegewezen aan een verantwoordelijk deel.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Specificeer systeemengineeringproces, traceerbaarheid en V&V-bewijs in het contract, eis dat leveranciers interfacecontroledocumenten en levenscyclusartefacten leveren die je kunt auditen en bewaar veiligheids- en missievalidatie voor onafhankelijke review met echte operators voor enige live overschakeling. Plan en financier bedrijf en uitfasering expliciet, want een publiek programma is verantwoording schuldig voor de volledige levenscyclus, inclusief veilige ontmanteling en bewaartermijnen van archieven.

## Voorbeelden

**Startup.** Een hardwarestartup van vier personen die een verbonden sensor bouwt kan zich geen formeel systeemengineeringprogramma veroorloven, maar behandelt het product toch als één systeem van firmware, een mobiele app en een cloudbackend in plaats van drie aparte projecten. Ze schrijven één kort interfacedocument dat vastpint hoe het apparaat, de app en de server praten (berichtformaten, eenheden, foutcodes) en houden een eenvoudige tabel bij die elke klantbehoefte koppelt aan het deel dat eraan voldoet. Wanneer een goedkopere sensorchip een firmwarewijziging afdwingt, toont dat gedeelde interface onmiddellijk wat de app en backend moeten aanpassen, zodat een componentwissel het product niet stilletjes breekt in het veld.

**Grote onderneming.** Een wereldwijde autofabrikant bouwt een nieuw platform voor elektrische voertuigen: een systeem van software (batterijbeheer, rijhulp, infotainment), hardware (motoren, sensoren, chips) en menselijke factoren, plus vele leveranciers die elk subsystemen leveren. Het bedrijf draait een systeemengineeringprogramma. Behoeften van stakeholders voeden toegewezen vereisten, elke leveranciersinterface heeft een Interface Control Document en een SysML-model koppelt vereisten aan ontwerp aan tests. Wanneer een leverancier van batterijcellen een component wijzigt, toont het traceerbaarheidsmodel precies welke vereisten, interfaces en tests worden geraakt, zodat de wijziging wordt beperkt in plaats van een programmabrede haast te triggeren.

**Overheid.** Een nationale luchtnavigatie-autoriteit moderniseert haar luchtverkeersbeheersysteem, een veiligheidskritiek systeem van systemen dat radars, controllerwerkstations, communicatie en software beslaat, rond de klok bediend. Het programma volgt ISO/IEC/IEEE 15288 over de volledige levenscyclus. Verificatie bewijst dat elk subsysteem aan zijn specificatie voldoet, en validatie via simulatie met echte verkeersleiders bewijst dat het geïntegreerde systeem veilige operaties ondersteunt voordat enig live verkeer ervan afhangt. Rigoureuze V&V laat de autoriteit in fasen overschakelen, met terugval bij elke stap, omdat hier een niet-geteste emergente storing een publiek-veiligheidsgebeurtenis is.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De motivatie is dat defecten exponentieel duurder worden naarmate je ze later vindt. Een vereistenfout gevangen tijdens de vereistenfase kost bijna niets om te herstellen. Dezelfde fout gevangen in bedrijf kan duizenden keren meer kosten, en bij een veiligheidskritiek systeem kan ze levens, terugroepacties of een mislukte missie kosten. Systeemengineering verschuift defectontdekking naar de goedkope vroege fasen.

Voor **return on investment** (ROI, behaalde waarde ten opzichte van uitgegeven kosten) is de opbrengst vermeden herwerk, minder integratiefalen en programma's die planning en budget halen in plaats van uit te lopen. Brancheonderzoeken van grote programma's vinden herhaaldelijk dat sterke systeemengineeringinspanning correleert met kleinere overschrijdingen. Voor **total cost of ownership** (TCO, de volledige levensduurkosten van bouwen, draaien en uitfaseren van een systeem) verantwoordt systeemengineering de bedrijfs- en uitfaseringsfasen die de langetermijnkosten domineren maar die ad hoc projecten negeren. Vanaf het begin ontwerpen voor onderhoudbaarheid, interfaces en afvoer verlaagt de kosten van de decennia die het systeem in dienst doorbrengt. Zie projectmanagement (hoofdstuk 10.6).

## Antipatronen en valkuilen

- **Big design up front zonder iteratie.** De levenscyclus behandelen als starre eenrichtingswaterval, zodat je pas leert dat de vereisten fout waren nadat je alles hebt gebouwd.
- **Vereisten zonder traceerbaarheid.** Een stapel vereisten die niemand koppelt aan ontwerp of tests, zodat je dekking niet kunt bewijzen of enig deel kunt rechtvaardigen.
- **Interfaces negeren.** Aannemen dat subsystemen gewoon passen, en dan maanden verliezen bij integratie aan grensmismatches die niemand bezat.
- **Verificatie zonder validatie.** Bewijzen dat het systeem aan zijn spec voldoet zonder ooit te controleren of de spec bij echte behoeften paste, en dan het verkeerde systeem opleveren.
- **Software als apart behandelen.** Softwareteams die lokaal optimaliseren terwijl ze hardwarebeperkingen, timing en menselijke operators negeren.
- **MBSE als shelfware.** Een model eenmaal bouwen en het dan uit de pas laten rotten tot het slechter is dan geen model.
- **Uitfaseringsplanning overslaan.** Geen plan voor ontmanteling, datamigratie of afvoer, zodat het einde van de levensduur een dure, riskante haast wordt.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Systeemengineering is ad hoc en reactief. Vereisten leven in verspreide documenten, interfaces worden bij integratie ontdekt en verificatie is wat testen er toevallig gedaan wordt. Grote programma's lopen regelmatig uit en verrassen het team laat.

**Niveau 2: Ontwikkelen.** Basispraktijken bestaan bij grote programma's. Vereisten worden vastgelegd en gebaselined, sleutelinterfaces hebben controledocumenten en er is een verificatieplan. De praktijk is inconsistent tussen teams en hangt af van individuen in plaats van een gedeelde methode.

**Niveau 3: Standaardiseren.** Systeemengineering is een gedocumenteerde, organisatiebrede discipline afgestemd op ISO/IEC/IEEE 15288 en gehandhaafd over teams. De volledige levenscyclus wordt gepland, traceerbaarheid wordt van begin tot eind onderhouden, interfaces worden formeel beheerst en verificatie en validatie zijn gescheiden en gepland. MBSE wordt gebruikt bij complexe programma's.

**Niveau 4: Beheersen.** Systeemengineering wordt gemeten en gestuurd met data. De organisatie volgt statistieken aan de hand van uitgangswaarden: vereistenvolatiliteit en traceerbaarheidsdekking, interfacedefecten gevonden bij integratie, slagingspercentages van verificatie en validatie en defectlekkage per levenscyclusfase (hoeveel defecten uit elke fase ontsnappen om later tegen hogere kosten te worden gevangen). Reviews sturen programma's op deze getallen, en drempels triggeren corrigerende actie in plaats van brandjes blussen achteraf.

**Niveau 5: Orkestreren.** Systeemengineering wordt continu verbeterd en is over de organisatie geïntegreerd. Een levend MBSE-model is de enige bron van waarheid, traceerbaarheid is geautomatiseerd, simulatie voorspelt emergent gedrag voor de bouw en statistieken van eerdere programma's voeden het volgende. Hardware en software worden vanzelfsprekend samen geëngineerd, en het proces past zich aan naarmate programma's, leveranciers en risico's verschuiven.

## Ideeën voor discussie

- Waar ligt in je organisatie de grens tussen systeemengineering en softwarearchitectuur, en wie bezit de ruimte ertussen?
- Kun je bij je grootste programma één behoefte van een stakeholder helemaal herleiden naar de test die haar verifieert? Zo niet, wat zou er nodig zijn?
- Welke van je recente falen gebeurden aan een interface, en wie bezat die?
- Zou MBSE zich voor jou uitbetalen, of zou het gezien je cultuur en tooling dure shelfware worden?
- Behandelt je levenscyclusplan bedrijf en uitfasering serieus, of stopt het stilletjes bij de lancering?

## Belangrijkste inzichten

- Systeemengineering engineert het hele systeem (software, hardware, mensen en processen) van begin tot eind en is te onderscheiden van softwarearchitectuur.
- Plan de volledige levenscyclus, van concept via vereisten, ontwerp, integratie, V&V, bedrijf en uitfasering.
- Herleid elke behoefte naar een vereiste, een ontwerpelement en een test, en wijs elke vereiste toe aan een verantwoordelijk deel.
- Beheer interfaces expliciet met heldere eigenaarschap en controledocumenten, want grenzen zijn waar systemen breken.
- Verificatie (goed gebouwd) en validatie (het juiste gebouwd) zijn verschillende controles, en je hebt beide nodig.
- Gebruik MBSE en SysML voor één verbonden bron van waarheid, en gebruik systeemdenken om emergent gedrag te anticiperen.
- Stem het gewicht van je proces af op de omvang, levensduur en het risico van het systeem.

## Referenties en verder lezen

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (systems engineering guidance)
