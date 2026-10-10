# 8.4 Platform engineering en ontwikkelaarservaring

## Overzicht en motivatie

[Platform engineering](https://en.wikipedia.org/wiki/Platform_engineering) is de discipline van een intern product bouwen en beheren, een intern ontwikkelaarsplatform (IDP), dat andere engineers gebruiken om hun software te bouwen, op te leveren en te beheren. In plaats van dat elk team zijn eigen pijplijnen, infrastructuur en tooling van nul samenstelt, levert een speciaal platformteam gecureerde, self-servicemogelijkheden langs goed ondersteunde "gouden paden", dat zijn eigenzinnige, ondersteunde routes met verstandige standaarden ingebakken. [Ontwikkelaarservaring](https://en.wikipedia.org/wiki/Developer_experience) (developer experience, DevEx) is de nauw verwante zorg van hoe het voelt om engineer te zijn in de organisatie: hoe makkelijk en snel een ontwikkelaar van idee naar draaiende software kan gaan, en hoeveel wrijving in de weg staat.

Voor grote teams doet dit ertoe omdat [cognitieve belasting](https://en.wikipedia.org/wiki/Cognitive_load) en wrijving niet soepel schalen. Wanneer je veel teams hebt, blijft het aantal tools, systemen en beslissingen dat elke engineer moet jongleren groeien. Al snel gaat een groot deel van hun tijd naar infrastructuurleidingen en coördinatie in plaats van waarde leveren. Zonder platform lost elk team dezelfde problemen, zoals provisioning, deployment, observeerbaarheid en compliance, inconsistent en herhaaldelijk op. Een goed platform absorbeert deze gedeelde complexiteit. Teams kunnen zich dan op hun domein richten terwijl ze toch de standaarden van de organisatie voor beveiliging, betrouwbaarheid en kosten erven.

De relevantie voor onderneming en overheid is hoog, omdat deze organisaties schaal combineren met strikte governance. Een platform is de natuurlijke plek om compliance-, beveiligings- en auditeisen eenmaal te coderen, als gebaande wegen die teams standaard volgen. Dat verslaat verwachten dat elk team beleid zelf correct interpreteert en implementeert. Het verandert governance van een bron van wrijving in een onzichtbare eigenschap van de standaardworkflow, precies wat grote gereguleerde organisaties nodig hebben om snel te bewegen zonder controle te verliezen.

## Kernprincipes

- Behandel het platform als product, met gebruikers, een roadmap en een mandaat om adoptie te verdienen in plaats van af te dwingen.
- Bied gouden paden: eigenzinnige, goed ondersteunde routes die de juiste manier de makkelijke manier maken.
- Maak mogelijkheden self-service zodat teams niet op tickets en menselijke overdrachten wachten.
- Leg gebaande wegen aan in plaats van poorten op te richten. Bouw vangrails in die begeleiden zonder legitiem werk te blokkeren.
- Verminder meedogenloos de cognitieve belasting van applicatieontwikkelaars.
- Meet ontwikkelaarservaring en productiviteit met evenwichtige, meerdimensionale signalen.
- Houd gouden paden optioneel maar zo goed dat teams ze kiezen.

## Aanbevelingen

### Bouw het platform als product

De belangrijkste verschuiving is het platform te behandelen als product dat interne klanten bedient, niet als van bovenaf opgelegde verplichte standaard. In de praktijk betekent dat de behoeften van ontwikkelaars begrijpen via onderzoek en feedback, een roadmap bijhouden, adoptie en tevredenheid meten en verantwoordelijk zijn voor de ervaring. Een platform dat teams moeten gebruiken maar dat hen vertraagt zal worden verfoeid en omzeild. Een platform dat teams werkelijk sneller maakt verspreidt zich op reputatie. Adoptie verdiend door kwaliteit is de ware maat van platformsucces.

### Bied gouden paden en gebaande wegen

Definieer gouden paden voor de gangbare reizen: een nieuwe service maken, haar deployen, een database toevoegen, observeerbaarheid bedraden, aan complianceeisen voldoen. Een gouden pad is een ondersteunde, eigenzinnige route van begin tot eind met verstandige standaarden ingebakken. Bed langs deze paden vangrails in, dat wil zeggen de beveiligingsscans, beleidscontroles en best practices, zodat een team dat het pad volgt automatisch conform en veilig is. Het doel is eenvoudig: de makkelijkste manier om iets te doen moet ook de juiste, veilige en conforme manier zijn. Houd de paden optioneel, zodat teams met werkelijk ongebruikelijke behoeften kunnen afwijken. Maar maak de paden aantrekkelijk genoeg dat de meeste teams dat nooit willen.

### Lever echte self-serviceinfrastructuur

Elimineer overdrachten met tickets en wachten door infrastructuur en mogelijkheden beschikbaar te stellen via self-serviceinterfaces: een portaal, een opdrachtregeltool, een API of sjabloonrepositories. Een ontwikkelaar moet in minuten een conforme omgeving kunnen inrichten, een nieuwe service uit een sjabloon kunnen opzetten of een database kunnen aanvragen, zonder een verzoek in te dienen en dagen op een ander team te wachten. Self-service is wat een platform van knelpunt in versneller verandert. En het werkt alleen omdat de onderliggende vangrails self-service veilig maken.

### Bied ontwikkelaarsportalen, servicecatalogi en scorekaarten

Een ontwikkelaarsportaal geeft je één overzicht: een catalogus van alle services met hun eigenaren, documentatie, afhankelijkheden en gezondheid. Servicecatalogi maken eigenaarschap en architectuur vindbaar. Dat is van onschatbare waarde op schaal, waar niemand het hele systeem in zijn hoofd kan houden. Scorekaarten meten elke service tegen standaarden als testdekking, beveiligingshouding, bereikbaarheidsgereedheid en documentatie, en geven teams een helder, objectief beeld van waar ze staan en wat te verbeteren. Samen verkorten deze tools de tijd die engineers besteden aan informatie zoeken, en ze verhelderen verantwoording.

### Meet ontwikkelaarservaring met evenwichtige kaders

Weersta productiviteitsstatistieken met één getal. Ze zijn makkelijk te gamen en misleidend. Gebruik meerdimensionale kaders als SPACE (satisfaction and well-being, performance, activity, communication and collaboration, efficiency and flow) om de echte textuur van ontwikkelaarservaring te vangen. Combineer waarnemingsdata uit enquêtes met systeemdata uit tooling. Volg leveringsstatistieken als doorlooptijd en deploymentfrequentie naast ontwikkelaarssentiment. Het doel is wrijving te begrijpen en weg te nemen, niet individuen te rangschikken. Meting die als surveillance voelt zal het vertrouwen eroderen waarvan het platform afhangt.

### Verminder cognitieve belasting als eersterangs doel

Cognitieve belasting, de totale mentale inspanning die een ontwikkelaar moet besteden om zijn werk te doen, is de verborgen belasting die platformen bestaan om te verminderen. Minimaliseer het aantal tools, concepten en contextwisselingen dat een applicatieontwikkelaar moet beheersen. Bied verstandige standaarden, zodat teams minder beslissingen van lage waarde nemen. Structureer eigenaarschap zodat elk team een begrensd, begrijpelijk deel van het systeem bezit. Stel bij het evalueren van elke platformfunctie één vraag: vermindert of vergroot het de belasting op de teams die haar zullen gebruiken?

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| Platform als product (opt-in) | Verdient adoptie. Blijft nuttig | Langzamer naar volledige dekking | De meeste organisaties |
| Verplicht platform | Snelle standaardisatie | Wrok. Omwegen | Alleen sterke governancebehoeften |
| Portaal/platform kopen | Sneller tot waarde | Minder op maat. Licentiekosten | Teams die een voorsprong willen |
| Intern bouwen | Past bij exacte behoeften | Hoge bouw- en onderhoudskosten | Grote, onderscheidende organisaties |
| Alleen rigide gouden paden | Maximale consistentie | Blokkeert legitieme randgevallen | Zeer uniforme werklasten |
| Flexibele paden met nooduitgangen | Balanceert consistentie en autonomie | Enige afwijking te beheren | Diverse teambehoeften |

De kernspanning is standaardisatie tegenover autonomie. Te weinig standaardisatie, en elk team vindt het wiel inconsistent opnieuw uit. Te veel, en je smoort de teams waarvan de behoeften werkelijk verschillen. De platform-als-productfilosofie lost dit op door standaardisatie aantrekkelijk te maken in plaats van verplicht. Een tweede echte afweging is bouwen tegenover kopen. Een intern platform bouwen past bij je exacte behoeften maar draagt aanzienlijke doorlopende kosten. Bestaande tools overnemen versnelt waarde, tegen de prijs van enige maatwerkbeperking.

## Vragen om met je team te bespreken

1. **Hoe weet je dat het platform cognitieve belasting vermindert in plaats van nog een tool toe te voegen om te leren?** Cognitieve belasting is de totale mentale inspanning die een engineer besteedt om het werk te doen, en een platform dat concepten en contextwisselingen toevoegt kan haar erger maken terwijl het indrukwekkend oogt. Neem één toets aan voor elke functie: vermindert of vergroot ze de belasting op de teams die haar gebruiken? Op schaal is dit beslissend, omdat een platform voor honderden engineers staat en een verwarrende abstractie ze allemaal dagelijks belast. Neem bewijs mee: hoeveel tools en portalen een ontwikkelaar aanraakt om een wijziging op te leveren, tijd-tot-eerste-deploy voor een nieuwe medewerker en kwalitatieve feedback over waar mensen vastlopen. Als het platform de toolchain laat groeien in plaats van krimpen, heb je een belasting gebouwd, geen gebaande weg.

2. **Welke standaarden dwingen je scorekaarten af, en wat gebeurt er werkelijk met een service die slecht scoort?** Scorekaarten meten elke service tegen verwachtingen als testdekking, beveiligingshouding, bereikbaarheidsgereedheid en documentatie, en hun waarde stort in als een rode score geen gevolg heeft. Besluit of scorekaarten louter adviserend zijn, in review voeden of bepaalde mogelijkheden poorten, en besluit wie de standaarden bezit. In gereguleerde organisaties kunnen scorekaarten toezichtsorganen continu zicht geven op de compliancehouding, wat handmatige rapportage vervangt, dus de lat die je stelt doet ertoe. Neem je conceptstandaarden mee en een steekproef echte services ertegen gescoord, en bespreek waar teams legitiem zouden terugduwen. Een scorekaart waar niemand naar handelt is een dashboard. Een scorekaart gekoppeld aan heldere verwachtingen verandert gedrag.

3. **Draai je het platform als echt product, met een roadmap, gebruikersonderzoek en adoptiestatistieken, of als mandaat?** De centrale weddenschap van dit hoofdstuk is dat standaardisatie aantrekkelijk moet zijn in plaats van afgedwongen, en dat houdt alleen stand als je interne engineers behandelt als klanten die je moet winnen. Besluit wie productmanager voor het platform speelt, hoe je de behoeften van ontwikkelaars verzamelt en welke adoptie- en tevredenheidsgetallen succes definiëren. Voor grote organisaties is een mandaat verleidelijk omdat het snel standaardiseert, maar het kweekt omwegen en wrok wanneer de tools mensen vertragen. Neem de huidige vrijwillige adoptiepercentages mee, tevredenheidssignalen en de top-wrijvingspunten die teams vandaag melden. Als teams het platform zouden verlaten zodra het mandaat verviel, heb je geen product gebouwd maar een beleid.

4. **Wanneer een team de rand van een gouden pad bereikt, wat is de nooduitgang, en wie beslist of het pad wordt verbreed of de lijn wordt gehouden?** Een gouden pad is een ondersteunde, eigenzinnige route met verstandige standaarden, en haar waarde komt uit de meeste teams die erop blijven, maar een pad zonder uitgang verandert in een poort die werkelijk ongebruikelijk werk helemaal van het platform duwt. Spreek vooraf af hoe een team een afwijking aanvraagt, wie haar beoordeelt en hoe je een eenmalige uitzondering onderscheidt van een signaal dat het pad zelf moet veranderen. Voor een grote organisatie is dit het verschil tussen een platform dat diversiteit absorbeert en een dat uiteenvalt in schaduwtooling zodra een team zich geblokkeerd voelt. Neem het huidige aantal teams mee dat buiten het pad is gegaan, de redenen die ze gaven en hoe lang een uitzondering nodig heeft om goedgekeurd te worden. Koppel in omgevingen van onderneming en overheid elke nooduitgang aan de compliancemaatregelen die hij omzeilt, zodat een afwijking van de gebaande weg nooit stilletjes een afwijking van de beveiligings- of accreditatiebasis wordt.

5. **Bouw je het platform intern of koop je het, en heb je de doorlopende kosten van beide paden eerlijk geprijsd?** Het platform is zelf een product met een levenscyclus, en de keuze tussen bouwen en kopen stelt jarenlang je kostenstructuur vast: een intern portaal past bij je exacte behoeften maar vraagt een gefinancierd team om haar te onderhouden, terwijl een gekocht platform sneller waarde bereikt tegen de prijs van licenties en een pasvorm die nooit perfect is. Besluit welke mogelijkheden onderscheidend genoeg zijn om te bouwen en welke standaardwaar zijn die je moet kopen, en herzie die lijn naarmate leveranciers rijpen. Voor een groot team is de inzet hefboom: een verkeerde bouwbeslissing laat schaarse senior engineers zinken in leidingen die een product had afgehandeld, terwijl een verkeerde koopbeslissing honderden ontwikkelaars vastzet aan de roadmap van een ander. Neem een realistische totale kostenschatting mee voor elke optie, inclusief onderhoud, upgrades en de exitkosten. Voeg in aanbesteding van onderneming en overheid de accreditatie- en dataoverdraagbaarheidsvoorwaarden toe, en geef de voorkeur aan contracten waarmee je kunt vertrekken zonder de servicecatalogus en scorekaarten die je erbovenop bouwde te verlaten.

6. **Hoe wordt het platformteam gefinancierd en bemeten ten opzichte van de ontwikkelaars die het bedient, en wat gebeurt er ermee wanneer budgetten krapper worden?** Een platform verdient zijn plaats door hefboom, aangezien een klein team de productiviteit vermenigvuldigt van een veel grotere populatie applicatieontwikkelaars, maar datzelfde kader maakt het een makkelijk doelwit wanneer financiën naar bezuinigingen zoekt en het voordeel diffuus is in plaats van toewijsbaar aan één productlijn. Besluit het financieringsmodel, de verhouding platformengineers tot de ontwikkelaars die ze ondersteunen en hoe je die investering met bewijs in plaats van geloof zult verdedigen. Voor een grote organisatie is een ondergefinancierd platform erger dan geen: teams hangen ervan af, het vervalt en de wrijving keert terug met een afhankelijkheid eraan vast. Neem de bezetting van het platform mee, haar adoptie- en tevredenheidstrend en een schatting van de teruggewonnen ontwikkelaarsuren over de organisatie. Formuleer het platform in overheids- en gereguleerde ondernemingen als de plek waar compliance eenmaal wordt gecodeerd, zodat het snijden ervan geen geld bespaart maar audit- en beveiligingswerk opnieuw verstrooit over elk team dat het nu met de hand moet doen.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen runway te sparen zet je geen platformteam op. Bouw één sjabloonrepository als gouden pad die een nieuwe service in een uur kan klonen en draaien. Bedraad hem vooraf met CI, een containerbuild, linting en een gezondheidscontrole, en laat hem zich verspreiden omdat hij duidelijk tijd bespaart, niet omdat iemand hem verplicht. Koop elke standaardmogelijkheid die je kunt, houd de toolchain klein en behandel cognitieve belasting, niet dekking, als wat je moet beschermen.

**Kleinbedrijf.** Je hebt geen aparte platformspecialist en een krap budget, dus leun op een beheerd platform of een eigenzinnig cloudaanbod in plaats van zelf een intern ontwikkelaarsplatform te bouwen. Formuleer de beslissing als kopen tegenover bouwen en kies standaard voor kopen: een gekocht portaal en haar sjablonen geven je generalistische engineers gouden paden zonder team om ze te onderhouden. Kies tools die self-service zijn en makkelijk te verlaten, zodat een leverancierswissel de handvol services die je draait niet laat stranden.

**Grote onderneming.** Schaal en veel teams maken portfolioconsistentie de prijs: een gefinancierd platformteam, gouden paden met vangrails, self-serviceprovisioning, een servicecatalogus en scorekaarten die eigenaarschap en kwaliteit zichtbaar maken over honderden services. Draai het platform als product dat vrijwillige adoptie verdient in plaats van een mandaat dat omwegen kweekt, en codeer beveiliging en compliance eenmaal als gebaande wegen zodat governance standaard meereist. Meet ontwikkelaarservaring met evenwichtige kaders en verdedig de financiering van het platform met teruggewonnen ontwikkelaarsuren.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven het platform vorm. Codeer verplichte beveiligingsmaatregelen en accreditatie-eisen als vangrails langs de gouden paden, zodat een team dat via het self-serviceportaal infrastructuur inricht een omgeving erft die al aan de maatregelenbasis voldoet, wat maanden handmatige accreditatie omzet in een grotendeels geautomatiseerde stap. Gebruik scorekaarten om toezichtsorganen continu, controleerbaar zicht op de compliancehouding te geven en eis in aanbesteding overdraagbaarheid van data en open interfaces zodat de catalogus en gebaande wegen die je bouwt niet aan één leverancier vastzitten.

## Voorbeelden

**Startup.** Een startup van twaalf personen heeft geen platformteam, dus besteedt één senior engineer een paar vrijdagen aan het bouwen van een enkele "nieuwe service"-sjabloonrepository die vooraf is bedraad met CI, een Dockerfile, linting en een gezondheidscontrole. Elke engineer kan haar klonen en binnen een uur een service in staging laten draaien, in plaats van configuratie uit een ouder project te kopiëren en de gaten te raden. Het sjabloon is het gouden pad, en omdat het duidelijk iedereen tijd bespaart, neemt het hele team het over zonder dat iemand dat wordt opgedragen.

**Grote onderneming.** Een grote verzekeraar vormt een platformteam dat een intern ontwikkelaarsportaal oplevert. Het catalogiseert elke service met haar eigenaar, documentatie en gezondheidsscorekaart. Nieuwe services worden gemaakt uit gouden-padsjablonen die vooraf zijn bedraad met CI/CD, beveiligingsscanning, observeerbaarheid en compliancecontroles. Databases en omgevingen worden self-service ingericht via het portaal. De onboardingtijd voor een nieuwe engineer daalt van weken naar dagen, en auditbewijs wordt automatisch geproduceerd omdat elke service dezelfde gebaande weg volgt. Platformadoptie is vrijwillig, en verspreidt zich omdat teams die haar gebruiken merkbaar sneller opleveren.

**Overheid.** Een federaal agentschap dat tientallen digitale diensten draait zet een gedeeld platform op. Het codeert de verplichte beveiligingsmaatregelen en accreditatie-eisen als vangrails langs zijn gouden paden. Een team dat infrastructuur inricht via het self-serviceportaal erft een omgeving die al aan de maatregelenbasis voldoet. Dat verandert een maanden durende handmatige accreditatieoefening in een grotendeels geautomatiseerde. Scorekaarten volgen de compliancehouding van elke dienst, wat toezichtsorganen continu zicht geeft zonder handmatige rapportage en schaars specialistisch personeel bevrijdt van repetitieve review.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van platform engineering komt uit teruggewonnen ontwikkelaarstijd en gewonnen consistentie. Wanneer engineers minder tijd besteden aan vechten met infrastructuur en zoeken naar informatie, gaat meer van hun dure tijd naar productwaarde leveren. Snellere onboarding, minder dubbele oplossingen en geautomatiseerde compliance vertalen zich allemaal in meetbare capaciteit en verminderd risico. Omdat het platform veel teams bedient, wordt elke verbetering ervan over de hele organisatie gehefboomd.

Qua TCO zijn de adoptiekosten een echte, doorlopende investering: een gefinancierd platformteam, tooling (gebouwd of gekocht) en de discipline om het platform als product te draaien met continue verbetering. De kosten van niet adopteren zijn diffuus maar groot: elk team dat dezelfde infrastructuurbelasting herhaaldelijk betaalt, inconsistente beveiliging en compliance, trage onboarding en senior engineers die opbranden op sleurwerk. Voor leiderschap wordt de zaak het best gemaakt in termen van hefboom. Een bescheiden, goed gerund platformteam vermenigvuldigt de productiviteit van een veel grotere populatie applicatieontwikkelaars, en codeert governance eenmaal in plaats van erop te vertrouwen dat elk team het goed doet.

## Antipatronen en valkuilen

- **Platform opgelegd, niet aangeboden.** Een platform verplichten dat ontwikkelaars niet bevalt kweekt omwegen en wrok.
- **Platformteam in een ivoren toren.** Bouwen zonder echte behoeften van ontwikkelaars te begrijpen produceert tools die niemand wil.
- **Poorten in plaats van gebaande wegen.** Vangrails die legitiem werk blokkeren duwen teams het platform helemaal te omzeilen.
- **Enkele productiviteitsstatistiek.** Productiviteit terugbrengen tot één gamebaar getal vervormt gedrag en erodeert vertrouwen.
- **Meting als surveillance.** DevEx-statistieken gebruikt om individuen te rangschikken vernietigen de psychologische veiligheid die het platform nodig heeft.
- **Gouden pad zonder nooduitgang.** Rigide paden die niet kunnen meebuigen voor echte randgevallen worden obstakels.
- **Ondergefinancierd platform.** Het platform als bijproject behandelen laat haar verhongeren en garandeert een slechte ervaring.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Er bestaat geen platform. Elk team stelt zijn eigen tooling en infrastructuur reactief samen, met zware overdrachten via tickets, dubbele oplossingen en hoge cognitieve belasting. Elk team lost provisioning, deployment en compliance zelf op, inconsistent.

**Niveau 2: Ontwikkelen.** Enkele gedeelde tools, sjablonen en startrepository's verschijnen, vaak gebouwd door een enthousiaste engineer, maar ze zijn gefragmenteerd en deels handmatig. Een paar teams nemen een gouden pad over terwijl andere haar negeren, self-service is beperkt en ontwikkelaarservaring wordt niet gemeten, dus de waarde van het platform rust op anekdote.

**Niveau 3: Standaardiseren.** Een platformteam draait gedocumenteerde gouden paden, self-serviceprovisioning, een ontwikkelaarsportaal met een servicecatalogus en scorekaarten, organisatiebreed toegepast. Vangrails voor beveiliging, beleid en compliance zijn ingebed in de gebaande wegen, zodat de standaardworkflow de conforme is en dezelfde conventies over teams gelden in plaats van per groep te variëren.

**Niveau 4: Beheersen.** Het platform wordt gemeten en beheerst met data tegen uitgangswaarden. Adoptie, tevredenheid, tijd-tot-eerste-deploy, doorlooptijd en deploymentfrequentie worden gevolgd met evenwichtige kaders als SPACE en gecombineerde enquête- en systeemsignalen. Scorekaartresultaten voeden review, en cognitieve belasting, onboardingtijd en teruggewonnen ontwikkelaarsuren worden bewaakt tegen doelen. Beslissingen om in een mogelijkheid te investeren of haar af te schaffen rusten op bewijs, niet op pleidooi.

**Niveau 5: Orkestreren.** Het platform is een volwassen product met hoge vrijwillige adoptie, continu verbeterd uit feedback van ontwikkelaars en statistieken en geïntegreerd met beveiligings-, compliance- en leveringsplanning over de organisatie. Gouden paden passen zich aan naarmate behoeften verschuiven, governance is een onzichtbare eigenschap van de standaardworkflow en het platformteam schaft mogelijkheden routinematig af, vervangt ze en bakent ze opnieuw af naarmate de technologie en de organisatie evolueren.

## Ideeën voor discussie

- Hoe verdien je adoptie voor een platform zonder haar te verplichten, en wanneer, als ooit, is een mandaat gerechtvaardigd?
- Welke gouden paden zouden jouw teams het eerst de meeste waarde leveren?
- Hoe meet je ontwikkelaarservaring zonder dat het als surveillance voelt?
- Waar zouden nooduitgangen moeten bestaan zodat ongebruikelijke teams niet helemaal van het platform worden gedwongen?
- Wat is de juiste omvang en het juiste financieringsmodel voor een platformteam ten opzichte van de ontwikkelaars die het bedient?
- Hoe besluit je wat je intern bouwt tegenover koopt voor je ontwikkelaarsportaal en tooling?

## Belangrijkste inzichten

- Draai het platform als product dat adoptie verdient door teams werkelijk sneller te maken.
- Bied gouden paden en gebaande wegen die de juiste, veilige, conforme manier de makkelijke manier maken.
- Lever echte self-service zodat teams ophouden op tickets en overdrachten te wachten.
- Gebruik portalen, catalogi en scorekaarten om eigenaarschap, architectuur en kwaliteit zichtbaar te maken.
- Meet ontwikkelaarservaring met evenwichtige kaders als SPACE, nooit een enkel gamebaar getal.
- Behandel cognitieve belasting verminderen als centraal doel van het platform.

## Referenties en verder lezen

- Matthew Skelton and Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, et al., "The SPACE of Developer Productivity" (paper).
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, platform engineering white paper.
