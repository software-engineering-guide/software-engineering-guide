# 1.2 Teamtopologieën en organisatieontwerp

## Overzicht en motivatie

Hoe je mensen in teams verdeelt, bepaalt welke software je kunt bouwen en hoe snel je die kunt bouwen. Dit is geen metafoor. Het is een bijna mechanisch gevolg dat bekendstaat als de [wet van Conway](https://en.wikipedia.org/wiki/Conway%27s_law): organisaties ontwerpen systemen die hun eigen communicatiestructuren spiegelen. Als drie teams een [compiler](https://en.wikipedia.org/wiki/Compiler) bouwen, krijg je een compiler met drie passes. Als je betalingslogica is verdeeld over een frontendteam, een backendteam en een databaseteam, vraagt elke betalingswijziging om afstemming tussen drie partijen. Voor een kleine organisatie is dat beheersbaar. Voor een grote wordt de vorm van het organigram de dominante beperking voor je engineering, je architectuur, je opleversnelheid en je kwaliteit. Het ontwerpen van teamstructuur is dus een volwaardige engineeringactiviteit, geen bijzaak van HR.

Teamtopologieën geven je een bewust vocabulaire voor dit ontwerp. In plaats van structuur bij toeval te laten aangroeien via reorganisaties en personeelsaantallen, kiezen volwassen organisaties bewust teamtypen en interactiemodi, en heroverwegen ze die keuzes naarmate het systeem en het bedrijf evolueren. Het doel is de [cognitieve belasting](https://en.wikipedia.org/wiki/Cognitive_load) van elk team laag te houden, de totale hoeveelheid die een team in zijn hoofd moet houden om effectief te zijn, zodat teams hun domein van begin tot eind kunnen bezitten en een gestage stroom waarde kunnen leveren zonder voortdurend op anderen te wachten.

Voor ondernemingen en overheden is deze discipline beslissend. Grote organisaties groeien vanzelf uit tot diepe hiërarchieën, shared services met lange wachtrijen en overdrachtsketens die een wijziging van twee dagen veranderen in een project van twee maanden. Overheden voegen aanbestedingsgrenzen, teams van externe leveranciers en verplichte [functiescheidingen](https://en.wikipedia.org/wiki/Separation_of_duties) toe die het eigenaarschap verder versnipperen. Expliciet topologieontwerp is hoe deze organisaties de flow terugwinnen: teams afstemmen op waardestromen, platforms bouwen die cognitieve belasting verlagen en interactiepatronen kiezen die afhankelijkheden zichtbaar en bewust maken in plaats van verborgen en constant.

## Kernprincipes

- De wet van Conway is onontkoombaar. Ontwerp teams naar de software engineering die je wilt (de "omgekeerde manoeuvre").
- Optimaliseer voor de cognitieve belasting van teams, niet voor maximale bezetting van individuen.
- Geef de voorkeur aan stream-aligned teams die een stuk waarde van begin tot eind bezitten.
- Platforms bestaan om de cognitieve belasting van stream-aligned teams te verlagen, niet om poortwachter te spelen.
- Maak teaminteracties expliciet en beperkt: samenwerking, X-as-a-service of faciliteren.
- Minimaliseer afhankelijkheden. Elke overdracht tussen teams is een wachtrij en een risico.
- Teamstructuur is een levend ontwerp dat moet evolueren naarmate het systeem en het bedrijf veranderen.

## Aanbevelingen

### Gebruik de vier fundamentele teamtypen

Teamtopologieën definiëren vier teamtypen die de meeste behoeften dekken. Stream-aligned teams zijn de standaard: elk bezit een continue stroom werk voor een specifiek product, een service of een gebruikerstraject, van begin tot eind. Platformteams leveren interne producten (rekenkracht, deployment, datapipelines, identiteit) die stream-aligned teams via self-service afnemen, wat hun cognitieve belasting verlaagt. Enabling teams zijn specialisten (testen, beveiliging, observeerbaarheid) die stream-aligned teams coachen om een vaardigheid op te bouwen en vervolgens een stap terug doen. Complicated-subsystem teams bezitten componenten die diepe specialistische expertise vragen (een prijsmotor, een [videocodec](https://en.wikipedia.org/wiki/Video_codec), een cryptografische module), waarbij het geen zin heeft dat elk team die kennis bezit. De meeste van je teams moeten stream-aligned zijn. De andere drie typen bestaan om hen te ondersteunen.

### Pas de omgekeerde Conway-manoeuvre toe

Omdat software de structuur van je organisatie spiegelt, geef je je teams vorm om de software te produceren die je wilt. Wil je losjes gekoppelde services met heldere grenzen? Maak dan losjes gekoppelde teams met heldere eigenaarschapsgrenzen. Wil je een betalingsvermogen dat op een eigen tijdschema oplevert? Vorm dan een betalingsteam dat het van voor naar achter bezit. Bestrijd de wet van Conway niet met heroïsche coördinatie. Teken de teamgrenzen opnieuw zodat de architectuur die je wilt de weg van de minste weerstand wordt.

### Beheer cognitieve belasting expliciet

Een team kan maar zoveel beheersen. Cognitieve belasting omvat de complexiteit van het domein, de technologieën, de operationele last en de breedte van de stakeholders. Als een team te veel niet-verwante services bezit, storten kwaliteit en snelheid allebei in. Begrens daarom de verantwoordelijkheden van elk team tot een domein dat het werkelijk kan beheersen, en gebruik platforms en enabling teams om ongedifferentieerde complexiteit van zijn bord te nemen. Houd teams op ruwweg vijf tot negen mensen: klein genoeg om gemakkelijk te communiceren en, zoals men zegt, met een paar pizza's te voeden.

### Kies interactiemodi bewust

Beperk teaminteracties tot drie modi. Samenwerking is nauw, hoogbandbreedte werk tussen twee teams gedurende een vaste periode. Het is krachtig voor ontdekking maar duur, dus houd het tijdelijk. X-as-a-service is een schone relatie tussen aanbieder en afnemer met een goed gedefinieerde interface, ideaal voor het gebruik van platforms op schaal. Faciliteren is dat één team een ander helpt leren, wat enabling teams doen. Benoem de modus voor elke belangrijke relatie tussen teams, en lees langdurige samenwerking tussen dezelfde twee teams als een teken dat hun grens op de verkeerde plek ligt.

### Kies een bedrijfsmodel voor overkoepelende functies

Beveiliging, data, ontwerp en vergelijkbare disciplines kunnen op drie manieren worden georganiseerd: gecentraliseerd (één team bezit het voor iedereen), gefedereerd (specialisten deeltijds ingebed, coördinerend via een gilde) of ingebed (een toegewijde specialist in elk stream-aligned team). Gecentraliseerd geeft je consistentie en diepgang, maar wordt een knelpunt. Ingebed geeft je snelheid en context, maar riskeert inconsistentie en duplicatie. Gefedereerd (vaak een hub-and-spoke- of [community-of-practice](https://en.wikipedia.org/wiki/Community_of_practice)-model) zit ertussenin. Kies per functie en per schaal. De meeste grote organisaties kiezen voor deze disciplines voor gefedereerd, met een kleine centrale kern die standaarden vaststelt.

### Investeer in inner-source

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) brengt samenwerkingspatronen van [open source](https://en.wikipedia.org/wiki/Open-source_software) binnen de organisatie: gedeelde interne repositories, gepubliceerde bijdrageregels, [codereview](https://en.wikipedia.org/wiki/Code_review) over teamgrenzen heen en duidelijke maintainers. Als een team een wijziging nodig heeft in het component van een ander team, kan het die wijziging rechtstreeks bijdragen in plaats van een ticket aan te maken en in een wachtrij te staan. Dit verlicht afhankelijkheden tussen teams zonder het eigenaarschap op te heffen, en het verspreidt kennis en standaarden vanzelf over een grote engineeringpopulatie.

## Afwegingen: voor- en nadelen

| Model voor overkoepelende functies | Voordelen | Nadelen |
| --- | --- | --- |
| Gecentraliseerd (één team voor allen) | Consistentie, diepe expertise, heldere standaarden | Knelpunt, wachtrijen, verlies van productcontext |
| Gefedereerd (hub-and-spoke, gilden) | Balanceert consistentie en snelheid. Deelt kennis | Vraagt coördinatiediscipline. Verantwoording kan vervagen |
| Ingebed (specialist per team) | Snel, rijk aan context, sterk eigenaarschap | Duplicatie, inconsistentie, moeilijk te bemensen op schaal |

| Teamtype | Het best voor | Risico bij overmatig gebruik |
| --- | --- | --- |
| Stream-aligned | De meeste product- en servicelevering | Geen. Dit moet domineren |
| Platform | Gedeelde cognitieve belasting verlagen | Wordt een poortwachter in een ivoren toren |
| Enabling | Een vaardigheid tijdelijk verspreiden | Verandert in een permanente afhankelijkheid |
| Complicated-subsystem | Echt diepe specialistische domeinen | Gebruikt als excuus om gewoon werk op te potten |

De terugkerende afweging is autonomie tegenover consistentie. Volledig autonome teams bewegen snel, maar drijven uit elkaar in standaarden, tooling en beveiligingsniveau. Volledig gecentraliseerde controle houdt dingen consistent, maar wurgt de flow. Goed topologieontwerp vindt de naad: autonomie voor stream-aligned oplevering, plus dunne centrale standaarden en platforms op een gebaande weg (goed ondersteunde standaardtooling die de compliante keuze de gemakkelijke maakt) voor de dingen die werkelijk consistent moeten zijn.

## Vragen om met je team te bespreken

1. **Welke concrete signalen vertellen je dat de cognitieve belasting van een team te hoog is, voordat de kwaliteit instort?** "Begrens elk team tot een domein dat het kan beheersen" is makkelijk gezegd en moeilijk uit te voeren zonder bewijs, omdat cognitieve belasting onzichtbaar blijft tot oplevering en betrouwbaarheid verslechteren. Let op meetbare symptomen: het aantal niet-verwante services of repositories dat een team bezit, hoe lang onboarding duurt, over hoeveel domeinen één engineer in een week van context moet wisselen en stijgende incidentcijfers in de hoeken van het werkgebied van een team. Voor een grote organisatie is dit belangrijk omdat overbelaste teams stilletjes knelpunten worden die geen reorganisatieschema voorspelt. Neem deze cijfers mee naar de discussie, plus het eigen gevoel van het team over wat het wel en niet in zijn hoofd kan houden. Wijzen de signalen op overbelasting, dan is de oplossing ongedifferentieerd werk over te dragen aan een platform of een enabling team, niet om meer heldendaden te eisen.

2. **Is een reorganisatie hier werkelijk de verstoring waard, of voed je een reorganisatieverslaving?** Grenzen opnieuw trekken om de omgekeerde Conway-manoeuvre toe te passen is krachtig, en elke reorganisatie vernietigt ook de stabiliteit die teams nodig hebben om te klikken en reset zwaarbevochten domeinkennis. De afwegingen zijn de doorlopende coördinatiebelasting van de huidige structuur tegenover de eenmalige kosten en het moreel van het veranderen ervan. In onderneming en overheid maken aanbestedingsgrenzen, teams van externe leveranciers en verplichte functiescheidingen reorganisaties trager en duurder, dus de lat moet hoger liggen. Neem bewijs mee van vertraging door afhankelijkheden: hoeveel initiatieven wachten op een ander team, en hoe lang. Reorganiseer wanneer dat wachten structureel en groot is, en weersta het herschudden wanneer de pijn tijdelijk is of goedkoper op te lossen met inner-source-bijdragen en duidelijkere interfaces.

3. **Welke gebeurtenis zet je aan om voor beveiliging, data en ontwerp te wisselen tussen ingebed, gefedereerd en gecentraliseerd?** De aanbeveling van dit hoofdstuk is te kiezen per functie en per schaal, en de moeilijker discipline is vooraf te bepalen welke groei of welk risico je die keuze laat heroverwegen. Een model dat past bij vijftig engineers kan bij vijfhonderd een knelpunt of een consistentieramp worden, en ondernemingen en overheden moeten vooral de standaarden benoemen die een kleine centrale kern altijd beheert. Neem de huidige wachttijden en consistentiekloven per functie mee: een centraal beveiligingsteam met wachtrijen van weken is een signaal om te federeren, terwijl ingebedde specialisten die onverenigbare datamodellen produceren een signaal is om een centrale standaardkern toe te voegen. Bepaal de trigger nu, zoals een drempel voor wachtrijlengte of een auditbevinding, zodat de verandering een geplande evolutie wordt in plaats van een crisisreactie. Het antwoord bepaalt waar je investeert in gebaande wegen en champions tegenover een centrale hub.

4. **Hoe weet je of je platformteam de cognitieve belasting echt verlaagt of stilletjes een poortwachter wordt?** Een platform bestaat om de compliante, betrouwbare keuze via self-service de makkelijke te maken, en hetzelfde team kan afdrijven naar het voorschrijven van tools, het met de hand beoordelen van elk verzoek en het toevoegen van de wrijving die het moest wegnemen. Voor een grote organisatie bepaalt dit onderscheid of de platforminvestering zich terugbetaalt of verandert in een centraal knelpunt waar elk stream-aligned team achter in de rij staat. De afwegingen zijn consistentie en controle aan de ene kant tegenover autonomie van afnemers en flow aan de andere. Neem bewijs mee dat een afnemer zou herkennen: hoe lang een stream-aligned team erover doet om zonder ticket zelf een nieuwe omgeving of pipeline te regelen, de verhouding tussen self-serviceacties en door mensen bemiddelde acties en platformadoptie gemeten aan teams die het kiezen in plaats van teams die erop worden gedwongen. Dring er in onderneming en overheid op aan dat het platform audit- en compliancebewijs automatisch genereert in plaats van via handmatige poorten, want een platform dat aan functiescheidingsregels voldoet door er een menselijke beoordelaar tussen te zetten, heeft het knelpunt opnieuw gecreëerd dat het moest oplossen.

5. **Welke van je relaties tussen teams zijn vastgelopen in permanente samenwerking, en wat zou elk ervan omzetten in een schone service-interface of een herziene grens?** De samenwerkingsmodus is bedoeld als intens en tijdelijk, en een pairing die nooit eindigt, is meestal een teken dat eigenaarschap op de verkeerde plek zit of dat de interface tussen twee teams nooit expliciet is gemaakt. Op schaal doet dit ertoe omdat naamloze, permanente samenwerking de plek is waar coördinatiekosten zich verbergen: het staat op geen enkel organigram, maar belast elke wijziging die de twee teams raakt. De afwegingen zijn de ontdekkingswaarde van dicht bij elkaar blijven tegenover de flow die je wint door de relatie om te zetten in een X-as-a-service-contract met een gedefinieerde interface, of door de verantwoordelijkheid samen te voegen in één team. Neem de lijst mee van teamparen die langer dan een kwartaal continu hebben samengewerkt, de wijzigingen van de afgelopen maanden waarvoor beide teams nodig waren en of een stabiele interface ertussen op papier gezet zou kunnen worden. Benoem in onderneming en overheid, waar leveranciersgrenzen en aanbestedingspercelen een overdracht jarenlang vast kunnen zetten, welke relaties je kunt omzetten met een interface en inner-source-bijdragen en welke contractueel vastliggen en als expliciete afhankelijkheden beheerd moeten worden.

6. **Als een enabling team een ander team helpt een vaardigheid op te bouwen, hoe weet je dan dat het geslaagd is en een stap terug kan doen in plaats van een permanente afhankelijkheid te worden?** Enabling teams zijn bedoeld om een stream-aligned team te coachen in testen, beveiliging of observeerbaarheid en dan door te gaan, en zonder expliciete uitstapvoorwaarde verhardt de coachingrelatie tot een vaste dienst die het stream-aligned team nooit echt overneemt. Voor een grote organisatie is dit het verschil tussen een vaardigheid verspreiden over tientallen teams en een nieuw gedeeld knelpunt creëren dat elk jaar slechter schaalt. De afwegingen zijn de diepte en consistentie die een specialistisch team biedt tegenover de autonomie en het begin-tot-eind-eigenaarschap dat je in stream-aligned teams probeert te bouwen. Neem bewijs mee van kennisoverdracht: of het ontvangende team het werk nu afhandelt zonder dat het enabling team erbij is, aan hoeveel teams een vaste enabling-groep tegelijk is gekoppeld en hoe lang elk traject voorbij de beoogde overdracht is doorgelopen. Bepaal in onderneming en overheid, waar een schaarse specialistische vaardigheid achter één centraal team of één contract kan zitten, vooraf hoe je kennisoverdracht en champions financiert, zodat expertise doordringt in leveringsteams in plaats van opgesloten te blijven achter een wachtrij waar elke audit en elke release op moet wachten.

## Sectorperspectief

**Startup.** Met een handvol engineers en weinig runway is de juiste topologie één stream-aligned team dat het hele product bezit, en de discipline is weigeren silo's te creëren voordat je ze nodig hebt. Weersta het aannemen van een eenzame "DevOps"- of "QA"-medewerker die een poort wordt. Vouw die vaardigheden als ingebedde capaciteit in het ene team. Laat de wet van Conway voor je werken door de organisatie plat te houden, zodat de architectuur zo eenvoudig en veranderbaar blijft als het team.

**Kleinbedrijf.** Je gaat geen eigen platform- of enabling team bemensen, dus koop het platform: gebruik beheerde clouddiensten, gehoste pipelines en kant-en-klare beveiligingstooling om ongedifferentieerde cognitieve belasting van je ene of twee teams af te nemen. Zie overkoepelende zaken zoals beveiliging en data als dingen die je configureert en afneemt in plaats van een functie die je bouwt. Bewaar maatwerk-eigenaarschap voor het ene complexe subsysteem dat je werkelijk onderscheidt, en laat leveranciers de rest dragen.

**Grote onderneming.** Op schaal is het probleem de coördinatiekosten over vele teams, dus maak topologie een expliciet, beheerd ontwerp: een gedeelde taxonomie van de vier teamtypen, benoemde interactiemodi, een platform op een gebaande weg en inner-source om wachtrijen tussen teams te verlichten. Volg door afhankelijkheden veroorzaakte vertraging en de cognitieve belasting van teams als portfoliostatistieken en voer reorganisaties uit als bewuste evoluties met een hoge lat in plaats van als jaarlijkse reflex. Een dunne centrale kern houdt de standaarden die consistent moeten zijn, terwijl stream-aligned teams autonomie houden over de oplevering.

**Overheid.** Aanbestedingsregels, leveranciersgrenzen en verplichte functiescheidingen versnipperen eigenaarschap, dus ontwerp de topologie om aan die beperkingen te voldoen via tooling en heldere interfaces in plaats van menselijke overdrachten. Geef de voorkeur aan gefedereerde modellen met een kleine standaardkern en een platform dat audit- en compliancebewijs automatisch genereert, zodat functiescheiding wordt afgedwongen door pipelines in plaats van beoordelingswachtrijen. Documenteer teamgrenzen, interactiemodi en het bedrijfsmodel openlijk, zodat de structuur transparant is voor auditors, toezichthouders en het publiek dat het financiert.

## Voorbeelden

**Startup.** Een startup van tien personen heeft één stream-aligned team dat het hele product van begin tot eind bezit, en dat is precies goed op zijn schaal: geen overdrachten, geen coördinatiebelasting, iedereen deelt dezelfde context. De problemen beginnen wanneer ze een aparte "DevOps-persoon" en een aparte "QA-persoon" aannemen en per ongeluk functionele silo's nabouwen, zodat elke release nu op twee individuen wacht. Ze sturen bij door die aanwervingen te behandelen als een ingebedde platform-en-testcapaciteit binnen het ene team, in plaats van als poorten waar werk doorheen moet. Op deze grootte is de goedkoopste topologie degene die iedereen in één flow houdt.

**Grote onderneming.** De checkout van een grote retailer was traag te wijzigen omdat frontend-, backend- en fulfilmentlogica waren verdeeld over drie functioneel georganiseerde teams, wat elke wijziging door drie backlogs dwong. Met de omgekeerde Conway-manoeuvre reorganiseerden ze in stream-aligned teams rond klanttrajecten ("bladeren", "winkelwagen en afrekenen", "na de aankoop"), die elk hun stuk van voor naar achter bezaten, ondersteund door een platformteam dat deployment en observeerbaarheid als dienst leverde. Checkout-wijzigingen die vroeger een kwartaal duurden, gingen in dagen live, omdat de coördinatie die vroeger over teams heen liep nu binnen één team plaatsvond.

**Overheid.** Een belastingdienst had een centraal beveiligingsteam dat elke release beoordeelde, wat een wachtrij van weken creëerde die kritieke fixes vertraagde. Ze stapten over op een gefedereerd model: een kleine centrale beveiligingsfunctie stelde standaarden vast en leverde een "gebaande weg" van vooraf goedgekeurde, automatisch gescande pipelines, terwijl beveiligingschampions die deeltijds in elk leveringsteam waren ingebed de dagelijkse beslissingen namen. Het platform genereerde compliancebewijs automatisch. Verplichte eisen aan functiescheiding werden nog steeds gehaald, maar via tooling en heldere interfaces in plaats van een menselijk knelpunt, wat de doorlooptijd van releases dramatisch verkortte en de auditgereedheid verbeterde.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Je betaalt voor slecht teamontwerp in coördinatieoverhead, en die overhead groeit sneller dan lineair met het aantal teams dat voor een typische wijziging moet synchroniseren. Elke overdracht is een wachtrij met wachttijd, een contextoverdracht die informatie verliest en een nieuwe kans op miscommunicatie. Als een routinewijziging vraagt dat drie teams hun roadmaps op elkaar afstemmen, zijn de echte kosten niet de som van hun werk. Het zijn de veel grotere kosten van plannen, wachten en herwerk. Trek grenzen opnieuw zodat de meeste wijzigingen binnen het eigenaarschap van één team passen, en die overhead verdwijnt eenvoudig.

De invoeringskosten zijn reëel. Reorganisaties zijn ontwrichtend, en het bouwen van platforms en inner-source-praktijken vraagt investering vooraf voordat de opbrengst komt. Maar de kosten van niet invoeren stapelen zich op. Organisaties die structuur bij toeval laten aangroeien, stapelen overdrachtsketens op, gedeelde knelpuntteams met wachtrijen van een kwartaal en architecturen die door het organigram zijn versteend. Meet voor het argument bij het bestuur de door afhankelijkheden veroorzaakte vertraging: hoeveel lopende initiatieven wachten op een ander team, en hoe lang. Platform- en topologie-investeringen betalen zich meestal terug door dat wachten om te zetten in flow, wat zichtbaar wordt in kortere doorlooptijden en hogere doorvoer zonder extra personeel.

## Antipatronen en valkuilen

- De wet van Conway negeren: een architectuur ontwerpen die de organisatiestructuur niet kan leveren.
- Functionele silo's: aparte frontend-, backend-, QA- en ops-teams die voor elke wijziging moeten coördineren.
- Knelpunt van gedeelde diensten: een centraal team waar elk project achter moet aansluiten.
- Platform als poortwachter: een platformteam dat voorschrijft in plaats van dient en wrijving toevoegt in plaats van weg te nemen.
- Cognitieve overbelasting: teams die uitdijende, niet-verwante systemen bezitten die ze niet kunnen beheersen.
- Permanente "samenwerking": twee teams die eindeloos verstrengeld zijn, wat wijst op een misplaatste grens.
- Reorganisatieverslaving: voortdurend herschudden, waardoor de stabiliteit die teams nodig hebben om te klikken wordt vernietigd.

## Volwassenheidsmodel

- **Niveau 1, Initiëren.** Teams ontstaan bij toeval, door personeelsaantallen of de erfenis van de hiërarchie. Niemand benoemt teamtypen of interactiemodi. Functionele silo's en knelpunten van gedeelde diensten zijn overal en afhankelijkheden blijven verborgen tot ze een release blokkeren.
- **Niveau 2, Ontwikkelen.** Er bestaan enkele stream-aligned teams en een eerste platform- of inner-source-inspanning verschijnt, maar het patroon wordt ongelijk toegepast: een paar teams bezitten hun stuk van begin tot eind terwijl anderen nog achter centrale functies in de rij staan, en cognitieve belasting wordt anekdotisch besproken in plaats van beheerd.
- **Niveau 3, Standaardiseren.** De vier teamtypen en de drie interactiemodi zijn gedocumenteerd en worden bewust gebruikt in de hele organisatie. Platforms en inner-source verlichten afhankelijkheden tussen teams. Een bedrijfsmodel voor beveiliging, data en ontwerp is gekozen en vastgelegd, en nieuwe teams worden gevormd volgens deze standaarden in plaats van door improvisatie.
- **Niveau 4, Beheersen.** Topologie wordt gemeten en gestuurd aan de hand van uitgangswaarden: teams volgen cognitieve belasting, door afhankelijkheden veroorzaakte vertraging (initiatieven die wachten op een ander team, en hoe lang), self-serviceverhoudingen en adoptie van het platform, duur van interactiemodi en leveringsflowstatistieken zoals doorlooptijd en wijzigingsfrequentie. Drempels zetten aan tot actie, bijvoorbeeld een wachtrijlengte die een functie dwingt te federeren of een permanente samenwerking die een misplaatste grens signaleert, zodat beslissingen op bewijs rusten in plaats van op mening.
- **Niveau 5, Orkestreren.** Teamontwerp wordt continu verbeterd en is geïntegreerd met architectuur-, product- en risicoplanning. De organisatie geeft grenzen opnieuw vorm naarmate het systeem en het bedrijf evolueren, beëindigt enabling-trajecten zodra de vaardigheid is overgedragen en herbalanceert platforminvesteringen naarmate de cognitieve belasting verschuift, zodat snelle flow een adaptieve, blijvende eigenschap is in plaats van een eenmalige reorganisatie.

## Ideeën voor discussie

- Hoeveel teams moeten voor een typische wijziging coördineren, en waarom?
- Welke van onze teams dragen te veel cognitieve belasting, en wat kan een platform overnemen?
- Waar vechten we tegen de wet van Conway in plaats van grenzen opnieuw te trekken?
- Dienen onze platformteams stream-aligned teams of fungeren ze als poortwachter?
- Moeten beveiliging, data en ontwerp voor ons nu gecentraliseerd, gefedereerd of ingebed zijn?
- Welke "tijdelijke" samenwerkingen zijn stilletjes permanente afhankelijkheden geworden?

## Belangrijkste inzichten

- Organisatiestructuur bepaalt architectuur en opleversnelheid. Ontwerp haar bewust.
- Gebruik de vier teamtypen, met stream-aligned als standaard en de rest als ondersteuning.
- Pas de omgekeerde Conway-manoeuvre toe om de gewenste architectuur de gemakkelijke weg te maken.
- Beheer cognitieve belasting. Begrens elk team tot een domein dat het kan beheersen.
- Beperk en benoem interactiemodi tussen teams. Behandel slepende afhankelijkheden als grensdefecten.
- Kies voor overkoepelende functies per schaal gecentraliseerde, gefedereerde of ingebedde modellen, en gebruik InnerSource om wachtrijen te verlichten.

## Referenties en verder lezen

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
