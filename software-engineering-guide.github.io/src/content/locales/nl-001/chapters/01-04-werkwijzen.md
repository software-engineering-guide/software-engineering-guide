# 1.4 Werkwijzen

## Overzicht en motivatie

"Werkwijzen" beschrijft hoe je team dag aan dag daadwerkelijk coördineert, plant, communiceert en oplevert. Hoe wordt werk opgedeeld? Wie praat met wie, en wanneer? Hoe wordt voortgang bijgehouden, en hoe stromen beslissingen en kennis?

De meeste organisaties kiezen een benoemde methodiek, [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), een of ander schaalraamwerk, en nemen aan dat de ceremonies hetzelfde zijn als de waarde eronder. Dat zijn ze niet. De methodieken die de softwarelevering hebben veranderd, waren reacties tegen zware, overdrachtsgedreven processen. Hun doel was snelle feedback, kleine batches en bevoegde teams. Neem je alleen de rituelen over, standups, sprints, storypoints, zonder de principes, dan krijg je de kosten van proces zonder de voordelen: [cargocult](https://en.wikipedia.org/wiki/Cargo_cult)-agile.

Voor grote teams is dit waar goede bedoelingen slagen of falen. Duizend engineers kunnen niet allemaal in dezelfde ruimte zijn, dezelfde vergadering bijwonen of dezelfde impliciete context delen. Hoe groter je wordt, hoe meer je moet steunen op schriftelijke communicatie, asynchrone samenwerking en lichte coördinatie in plaats van vergaderingen en gesprekken op de gang. Schaal verandert de natuurkunde. Werkwijzen die prachtig werken voor acht mensen op één locatie kunnen instorten bij tachtig verspreide mensen. En schaalraamwerken die beloven dit op te lossen, voeren vaak juist de overdrachten en centralisatie opnieuw in die [agile](https://en.wikipedia.org/wiki/Agile_software_development) moest wegnemen.

Ondernemingen en overheden voelen elk van deze drukken op volle sterkte. Ze overspannen veel tijdzones, mengen vast personeel met externe medewerkers en leveranciers en dragen vaak verplichte stage gates en rapportages. Hier is een documentatie-eerst, asynchrone, resultaatgerichte werkwijze geen luxe. Het is het enige dat schaalt. De aanbevelingen hieronder geven de voorkeur aan het aanpassen van principes aan de context boven het wholesale importeren van raamwerken, en aan schriftelijke, asynchrone, transparante werkwijzen waarmee grote, verspreide, gemengde teams echt kunnen samenwerken.

## Kernprincipes

- Neem principes over, geen rituelen. Begrijp waarom een praktijk bestaat voordat je haar kopieert.
- Kleine batches en snelle feedback winnen van grote plannen en lange cycli.
- Geef de voorkeur aan flow (werk in uitvoering beperken) boven rigide timeboxing waar dat past.
- Schat in om gesprek en planning mogelijk te maken, niet om schijnprecisie te fabriceren.
- Kies standaard voor asynchrone, schriftelijke communicatie. Bewaar synchrone tijd voor wat het echt nodig heeft.
- Maak werk en beslissingen zichtbaar en gedocumenteerd, zodat iedereen kan bijpraten zonder vergadering.
- Optimaliseer voor opgeleverde resultaten, niet voor uitgevoerde activiteit of benutte capaciteit.

## Aanbevelingen

### Pas Agile, Scrum, Kanban en Lean aan op de context

Zie deze als een gereedschapskist, niet als een geloof. De timeboxed sprints van Scrum passen bij teams met ontdekkingswerk dat baat heeft bij een regelmatige plannings- en reviewcadans. De continue flow en expliciete limieten op werk in uitvoering van Kanban passen bij teams met onvoorspelbaar, onderbrekingsgedreven werk zoals platform en beheer. De focus van [Lean](https://en.wikipedia.org/wiki/Lean_software_development) op het wegnemen van verspilling en het verkorten van doorlooptijd ligt onder beide. Kies bewust. Meng waar het helpt: veel teams draaien "[Scrumban](https://en.wikipedia.org/wiki/Scrumban)". Behoud de praktijken die waarde creëren en laat de ceremonies vallen die lege rituelen zijn geworden. De toets voor elke praktijk is eenvoudig. Verkort ze de feedback, verkleint ze de batch of vergroot ze de duidelijkheid? Zo niet, stel haar dan ter discussie.

### Schaal met voorzichtigheid, niet met cargocult

Schaalraamwerken, [SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), LeSS (Large-Scale Scrum), het gepopulariseerde "Spotify-model", beloven veel teams te coördineren. Benader ze met een sceptische blik. SAFe brengt structuur en wordt vaak gekozen door grote ondernemingen en overheden vanwege zijn volledigheid en opleidingsecosysteem, maar kan zware planning, hiërarchie en overdrachten terugbrengen die de wendbaarheid ondermijnen. LeSS blijft dichter bij lean-principes, maar vraagt echte organisatorische verandering. Het Spotify-"model" was een momentopname van de zich ontwikkelende cultuur van één bedrijf, nooit een sjabloon, en zelfs Spotify draaide het niet zoals mensen zich voorstellen. Schaal liever door de behoefte aan coördinatie te verminderen, via de teamtopologieën uit het vorige hoofdstuk, in plaats van een coördinatieraamwerk op een versnipperde structuur te schroeven.

### Schat eerlijk en licht in

Storypoints en velocity helpen je team zijn eigen werk op korte termijn te plannen en te praten over relatieve complexiteit. Ze zijn geen productiviteitsmaat, geen valuta tussen teams en geen belofte. Maak van velocity nooit een doel: het wordt bespeeld via inflatie van punten. Geef voor prognoses op langere termijn de voorkeur aan het tellen van doorvoer en het gebruik van historische doorlooptijdgegevens, wat vaak nauwkeuriger is dan het optellen van schattingen. Veel volwassen teams verlagen de schatoverhead door werk in even kleine stukken te snijden en ze simpelweg te tellen. Welke methode ook, onthoud dat schattingen prognoses onder onzekerheid zijn, geen toezeggingen. Communiceer ze als bandbreedtes.

### Kies standaard voor asynchrone, documentatie-eerst communicatie

In grote, verspreide organisaties schalen synchrone vergaderingen niet, en ze sluiten mensen in andere tijdzones buiten. Maak schrijven de standaard: ontwerpdocumenten, [besluitenlogboeken](https://en.wikipedia.org/wiki/Architectural_decision), schriftelijke statusupdates en uitgebreide tickets die genoeg context bevatten om op te handelen zonder live gesprek. Leg de vergaderingen die je niet kunt vermijden vast en vat ze samen. Een documentatie-eerst cultuur laat iemand in een andere tijdzone volledig bijdragen, laat nieuwe collega's en externe medewerkers onboarden door te lezen en laat een duurzaam verslag achter. Bewaar synchrone tijd voor echte samenwerking, relatieopbouw en het snel ophelderen van onduidelijkheid. Bescherm grote blokken focustijd tegen versnippering door vergaderingen.

### Werk goed over tijdzones, externe medewerkers en leveranciers heen

Verspreide en gemengde teams zijn op schaal de norm. Ontwerp voor "[follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun)", waarbij overdrachten schriftelijk en compleet zijn, niet mondeling. Stel een paar overlappende kernuren in voor het synchrone contact dat je nodig hebt, en deel de last van ongelegen vergadertijden eerlijk in plaats van altijd dezelfde regio te belasten. Investeer voor externe medewerkers en leveranciers extra in schriftelijke context, heldere interfaces en gedeelde tooling, omdat ze de impliciete kennis missen die je vaste medewerkers opbouwen. Haal leveranciers op dezelfde zichtbare borden en documentatie in plaats van ze via een apart, ondoorzichtig kanaal te beheren. Waar mogelijk structureer je contracten rond resultaten in plaats van uren.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
| --- | --- | --- |
| Agile (interactie met stakeholders) | Veel samenwerking en snelste waarde | Vraagt vertrouwen en flexibiliteit |
| Scrum (timeboxed sprints) | Regelmatige cadans, voorspelbaar ritme, ingebouwde reflectie | Ceremonie-overhead. Slechte pasvorm voor onderbrekingsgedreven werk |
| Kanban (continue flow, WIP-limieten) | Flexibel, legt knelpunten bloot, goed voor beheer | Minder ritme. Vraagt discipline om WIP te beperken |
| SAFe / zwaar schaalraamwerk | Structuur, opleiding, vertrouwd voor grote organisaties en overheid | Brengt hiërarchie en overdrachten terug. Kan wendbaarheid verstikken |
| LeSS / lichtgewicht schalen | Blijft dicht bij lean-principes | Vraagt diepe organisatorische verandering |
| Async / documentatie-eerst | Schaalt over tijdzones. Duurzaam. Inclusief | Trager bij dubbelzinnige onderwerpen. Vraagt schrijfdiscipline |

De overkoepelende afweging is coördinatie tegenover autonomie, en structuur tegenover aanpassingsvermogen. Meer raamwerk en meer synchrone coördinatie kopen voorspelbaarheid en afstemming, ten koste van snelheid, overhead en bevoegdheid van teams. Minder raamwerk koopt snelheid en eigenaarschap, ten koste van mogelijke afstemmingsverschillen tussen veel teams. Voor de meeste grote organisaties is het beste antwoord een minimale gedeelde cadans plus sterke schriftelijke werkwijzen. Dat vermindert de coördinatielast aan de bron in plaats van die te beheren met zwaarder proces.

## Vragen om met je team te bespreken

1. **Als het bestuur de voorspelbaarheid wil die een schaalraamwerk belooft, hoe geef je hen dat zonder de overdrachten terug te brengen die agile moest wegnemen?** Grote ondernemingen en overheidsprogramma's verplichten vaak planning in de stijl van SAFe's big-room en rapportage via stage gates, omdat toezichthouders prognoses en coördinatie eisen die ze kunnen zien. De afwegingen zijn oprecht: het bestuur heeft voorspelbaarheid en afstemming over veel teams nodig, en zware raamwerken kopen dat ten koste van snelheid, overhead en juist de overdrachten die de oplevering vertragen. Neem bewijs mee naar de discussie, zoals hoeveel van de werkweek verdwijnt in planningsevenementen en het coördineren van afhankelijkheden tussen teams, en of die evenementen afhankelijkheden wegnemen of ze alleen zichtbaar maken. De sterkere zet is te schalen door de behoefte aan coördinatie te verminderen via teamtopologie, en dan aan de rapportage te voldoen vanuit live borden en schriftelijke interfaces in plaats van vanuit planningsmarathons. Bepaal welke coördinatie echt is en welke ceremonie, en geef het bestuur de prognose die het nodig heeft uit doorvoer- en doorlooptijdgegevens in plaats van uit de overhead van een raamwerk.

2. **Wat ga je daadwerkelijk doen om te voorkomen dat velocity wordt omgezet in een productiviteitsmaat tussen teams?** Storypoints helpen één team zijn eigen werk op korte termijn te plannen, en ze worden waardeloos op het moment dat ze tussen teams worden vergeleken of als doel worden gesteld, omdat puntinflatie de rationele reactie is. In een grote organisatie is de trek om velocity op te rollen in een dashboard dat bestuurders vergelijken sterk, en het corrumpeert stilletjes de schattingen waarvan de teams afhangen. Neem het bewijs van afdrijving mee: lopen punten op in de tijd, vullen teams hun schattingen op, wordt iemand gerangschikt op velocity? Geef de voorkeur aan het tellen van doorvoer en historische doorlooptijdgegevens voor elke prognose die het team verlaat, en communiceer schattingen als bandbreedtes onder onzekerheid in plaats van beloftes. Het antwoord moet een expliciete afspraak opleveren dat velocity het team nooit verlaat en dat prognoses tussen teams flowstatistieken gebruiken.

3. **Wat is je concrete lat voor "opgeschreven", en welke beslissingen vragen nog echt om een synchroon gesprek?** Een documentatie-eerst standaard is wat schaalt over tijdzones, externe medewerkers en leveranciers, en het kost echte schrijfdiscipline die nog niet iedereen heeft. Wees specifiek over de lat: bevat een ticket genoeg context om op te handelen zonder live gesprek, belanden beslissingen in een duurzaam verslag, worden de vergaderingen die je niet kunt vermijden vastgelegd en samengevat? Voor ondernemingen en overheidsprogramma's die vast personeel mengen met externe medewerkers die impliciete kennis missen, is de schriftelijke context wat een gemengd, verspreid team volledig laat bijdragen. De afweging is dat dubbelzinnige of omstreden onderwerpen vaak sneller synchroon op te lossen zijn, dus benoem die expliciet en bewaar schaarse synchrone tijd daarvoor. Bepaal wie de kosten draagt van het opbouwen van de schrijfgewoonte en van ongelegen vergadertijden, en deel die kosten eerlijk in plaats van altijd dezelfde regio te belasten.

4. **Welke van onze huidige ceremonies zouden overleven als we ze puur beoordeelden op de vraag of ze de feedback verkorten, de batchgrootte verkleinen of de duidelijkheid vergroten?** Ceremonies hopen zich stilletjes op: een standup hier, een refinementsessie daar, een review en een retro en een planningsevenement, tot een groot team meer van zijn week in terugkerende vergaderingen doorbrengt dan in het werk dat die vergaderingen moeten dienen. De afwegingen zijn reëel, want een ritueel dat voor de één als pure overhead voelt, kan de enige plek zijn waar een verspreid team gedeelde context opbouwt of een blokkade naar boven haalt. Neem bewijs mee naar de discussie: de totale terugkerende vergaderuren per persoon per week, aanwezigheid en betrokkenheid bij elke ceremonie en welke beslissing of welk signaal elk daadwerkelijk oplevert dat niet uit een schriftelijke update kan komen. Voor een onderneming of overheidsprogramma waar elk team dezelfde opgelegde cadans draait, zijn de opgestapelde kosten enorm, dus spreek een expliciete toets af waar elke ceremonie aan moet voldoen om haar plek te houden, en wees bereid die af te schaffen of samen te voegen die alleen uit gewoonte voortbestaan.

5. **Als werk stilvalt, weten we dan waar het werkelijk op wacht, en beheren we flow of bemannen we alleen?** In de meeste kenniswerk brengt een taak veel meer van haar leven door met wachten in wachtrijen, overdrachten en review dan met actief bewerkt worden, en toch reageren teams instinctief op trage oplevering door mensen toe te voegen of aan te dringen op hogere benutting, wat wachtrijen verlengt in plaats van verkort. De spanning is dat het beperken van werk in uitvoering voelt als capaciteit ongebruikt laten, en dat werkloos ogende mensen managers en toezichthouders ongemakkelijk maken. Neem het bewijs mee dat de waarheid blootlegt: verdelingen van doorlooptijd, de verhouding tussen actieve tijd en totale doorlooptijd, waar items geblokkeerd op je bord staan en hoe limieten op werk in uitvoering (een plafond op hoeveel items tegelijk onderweg zijn) de doorvoer veranderen wanneer je ze handhaaft. Voor een grote organisatie of overheid die wordt afgemeten aan personeelsbenutting herdefinieert dit het doel van iedereen bezig houden naar afgerond werk laten stromen, en die verschuiving is vaak de grootste hefboom op leveringssnelheid.

6. **Hoe gaat onze werkwijze de mensen opnemen die geen vast personeel in onze kerntijdzone zijn, de externe medewerkers, leveranciers en regio's met veel uur verschil met het hoofdkantoor?** Op schaal is een gemengd, verspreid personeelsbestand de norm, en werkwijzen die zijn afgestemd op een kernteam op één locatie sluiten stilletjes iedereen anders buiten: de leverancier die via een privékanaal wordt beheerd, de externe medewerker zonder de impliciete context, de regio waarvan de werkdag nooit overlapt met een beslissingsvergadering. De overwegingen trekken tegen elkaar in, want strakkere schriftelijke interfaces en complete schriftelijke overdrachten kosten echte discipline en vertragen de snelle informele coördinatie waar een groep op één locatie van geniet. Neem bewijs mee, zoals wie routinematig ontbreekt bij de vergaderingen waar beslissingen worden genomen, hoe vaak regio's met tijdsverschil geblokkeerd worden in afwachting van een overdracht en of leveranciers op dezelfde zichtbare borden werken als medewerkers of op een apart ondoorzichtig spoor. Behandel voor ondernemingen en overheidsprogramma's die vast personeel, externe medewerkers en leveranciers over vele tijdzones mengen onder verplichte rapportage schriftelijke, transparante follow-the-sun-praktijk als de basis die het hele personeelsbestand laat bijdragen, en deel de last van ongelegen uren in plaats van die steeds aan dezelfde regio op te leggen.

## Sectorperspectief

**Startup.** Met een handvol mensen en weinig runway sla je de catalogus van ceremonies over en draai je op de lichtst mogelijke flow: een gedeeld bord, een korte schriftelijke dagelijkse update en beslissingen vastgelegd in een document zodat niemand geblokkeerd wordt in afwachting van een teamgenoot die wakker moet worden. Maak schrijven vanaf dag één de standaard, want de asynchrone gewoonte is veel goedkoper op te bouwen bij vijf mensen dan achteraf in te voeren bij vijftig. Neem geen schaalraamwerk aan dat je jaren niet nodig hebt. Je voordeel is dat je bijna niets te coördineren hebt, dus bescherm dat.

**Kleinbedrijf.** Zonder agile coach of leveringsmanager in dienst en met een krap budget geef je de voorkeur aan kant-en-klare praktijk boven ingekochte raamwerken met opleidings- en certificeringskosten die je niet kunt rechtvaardigen. Kies één methodiek die bij je werk past, Kanban voor onderbrekingsgedreven servicewerk of een lichte Scrum-cadans voor projectwerk, en weersta de aanleiding om een zwaar hulpmiddel te kopen terwijl een eenvoudig bord en duidelijke tickets het werk doen. Besteed je schaarse coördinatie-inspanning aan dingen opschrijven, zodat een klein team niet gegijzeld wordt door het geheugen van één persoon.

**Grote onderneming.** Over veel teams zijn coördinatiekosten en consistentie het probleem: een minimale gedeelde cadans, een gemeenschappelijke definitie van wat "opgeschreven" betekent en flowstatistieken die oprollen zonder velocity tot een doel tussen teams te maken. Schaal door de behoefte aan coördinatie te verminderen via teamtopologie in plaats van een raamwerk erop te schroeven dat overdrachten terugbrengt, en beheer de werkwijze als iets wat je op basis van bewijs bijstelt, niet als een eenmalige uitrol. Standaardiseer de interfaces en de rapportage, zodat toezicht wordt bediend vanuit live borden in plaats van vanuit planningsmarathons.

**Overheid.** Aanbestedingsregels, verplichte stage gates en publieke verantwoording bepalen elke keuze, en gemengde teams van vast personeel, externe medewerkers en leveranciers overspannen vele tijdzones onder verplichte voortgangsrapportage. Geef de voorkeur aan een documentatie-eerst, transparante werkwijze waarin elk stuk werk volledige schriftelijke context draagt op een bord dat zichtbaar is voor zowel medewerkers als leveranciers, zodat statusrapporten rechtstreeks uit het verslag komen in plaats van uit aparte vergaderingen. Structureer leverancierscontracten rond resultaten en gedeelde zichtbaarheid in plaats van ondoorzichtige uurfacturering, en behandel het schriftelijke, controleerbare spoor als compliance-bezit in plaats van overhead.

## Voorbeelden

**Startup.** Een verspreide startup van acht personen slaat de volledige catalogus van Scrum-ceremonies over en draait op een gedeeld Kanban-bord plus een korte schriftelijke dagelijkse update in Slack. Omdat de twee oprichters in verschillende tijdzones zitten, maken ze schrijven vanaf dag één de standaard: elke beslissing komt in een document, zodat niemand geblokkeerd wordt in afwachting van de ander. Wanneer ze later in een derde tijdzone aannemen, is onboarding vooral lezen, en schaalt de asynchrone gewoonte ongewijzigd mee. De praktijk die ze nooit hebben ingevoerd, de synchrone statusvergadering, is degene die ze nooit missen.

**Grote onderneming.** Een internationale bank rolde een schaalraamwerk uit over honderden teams, compleet met kwartaalplanning in een big room. De afstemming verbeterde op papier, maar de oplevering vertraagde. Teams brachten dagen door in planningsevenementen en met het coördineren van afhankelijkheden tussen teams die het raamwerk zichtbaar maakte maar niet wegnam. De bank stuurde bij. Ze hield alleen de lichte afstemming tussen teams die ze echt nodig had, herstructureerde teams om hun waardestromen van begin tot eind te bezitten en verschoof het grootste deel van de coördinatie naar schriftelijke interfaces en asynchrone updates. De doorlooptijd van oplevering daalde, en de uitputtende planningsmarathons krompen tot gerichte, incidentele syncs.

**Overheid.** Een overheidsdienst die burgerdiensten leverde werkte met vast personeel in één regio en teams van externe leveranciers in twee andere, over vele tijdzones, onder verplichte voortgangsrapportage. Ze nam een documentatie-eerst, op Kanban gebaseerde werkwijze aan. Elk stuk werk droeg volledige schriftelijke context op een gedeeld bord dat zichtbaar was voor medewerkers en leveranciers. Overdrachten tussen regio's waren schriftelijk en compleet. Verplichte statusrapporten kwamen rechtstreeks van het bord in plaats van uit aparte vergaderingen. Dit liet een verspreid, gemengd team continu samenwerken, voldeed als bijproduct aan de toezichtrapportage en verminderde de afhankelijkheid van moeilijk te plannen vergaderingen over tijdzones heen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het economische argument rust op flowefficiëntie. In de meeste kenniswerk is de tijd dat een eenheid werk actief wordt bewerkt een klein deel van haar totale doorlooptijd. De rest is wachten: in wachtrijen, in vergaderingen, in overdrachten, in tijdzoneverschillen. Werkwijzen die de batchgrootte verkleinen, werk in uitvoering beperken en synchrone knelpunten vervangen door schriftelijke asynchrone flow, pakken dat wachten rechtstreeks aan. De opbrengst is kortere doorlooptijden en hogere doorvoer zonder mensen toe te voegen, plus minder defecten, omdat feedback eerder komt terwijl de context nog vers is.

Weeg de kosten van invoeren af tegen de kosten van de status quo. Documentatie-eerst, asynchrone en lean flow kosten vooral een verandering van gewoonten en wat investering vooraf in schrijven en tooling. Er zijn geen dure licenties voor nodig. Zware schaalraamwerken daarentegen dragen echte kosten: opleiding, certificering, toegewijde rollen en de doorlopende overhead van grote planningsevenementen. Alleen echte coördinatiebehoeften rechtvaardigen dat. De kosten van niets doen blijken uit door vergaderingen verzadigde agenda's, buitengesloten externe bijdragers, cargocult-ceremonies die tijd verbruiken zonder de resultaten te verbeteren en trage oplevering. Meet voor het argument bij het bestuur de doorlooptijd van oplevering, de deployfrequentie en het deel van de werkweek dat verloren gaat aan vergaderingen met weinig waarde. Kleine verbeteringen in flow over een groot personeelsbestand tellen op tot grote capaciteitswinst.

## Antipatronen en valkuilen

- Cargocult-agile: ceremonies uitvoeren zonder de onderliggende principes.
- Velocity als doel: nodigt uit tot puntinflatie en vernietigt het nut van de maat.
- Raamwerkverering: SAFe of een "Spotify-model"-sjabloon opleggen ongeacht de pasvorm.
- Schattingen als toezeggingen: prognoses onder onzekerheid behandelen als bindende beloftes.
- Vergadergedreven cultuur: standaard kiezen voor synchrone gesprekken die andere tijdzones uitsluiten.
- Ongedocumenteerde beslissingen: kennis gevangen in hoofden van mensen en eerdere gesprekken.
- Leveranciers als black box: externe medewerkers beheren via ondoorzichtige zijkanalen in plaats van gedeelde zichtbaarheid.
- Benuttingsobsessie: ieders drukte maximaliseren in plaats van de flow van afgerond werk.

## Volwassenheidsmodel

- **Niveau 1, Initiëren.** Proces is ad hoc of cargocult. Teams voeren geleende ceremonies uit zonder de principes erachter, of improviseren zonder enige gedeelde methode. Communicatie is vergadergedreven en ongedocumenteerd, beslissingen leven in hoofden van mensen en schattingen worden behandeld als beloftes. Verspreide bijdragers, externe medewerkers en tijdzones met verschil worden mondeling gecoördineerd en blijven geblokkeerd wanneer de juiste persoon slaapt.
- **Niveau 2, Ontwikkelen.** Afzonderlijke teams nemen een benoemde methodiek aan zoals Scrum of Kanban en volgen die met enige consistentie, maar de praktijk verschilt van team tot team en de ceremonies zijn vaak mechanisch. Sommige teams schrijven ontwerpdocumenten en besluitenlogboeken terwijl anderen nog op vergaderingen vertrouwen. Inschatten en coördineren gebeuren, maar zonder gedeelde lat voor wat "opgeschreven" betekent, dus context lekt nog steeds weg en overdrachten tussen teams blijven zwaar.
- **Niveau 3, Standaardiseren.** Werkwijzen worden bewust gekozen om bij het werk te passen en gedocumenteerd als organisatiebrede verwachting: een minimale gedeelde cadans, een gedefinieerde lat voor schriftelijke context in tickets en besluitenlogboeken, asynchrone documentatie-eerst communicatie als standaard en inschatting gebruikt voor gesprek in plaats van controle. De standaard wordt consistent gehandhaafd, zodat een externe medewerker of nieuwe collega in elk team kan onboarden door te lezen, en leveranciers op dezelfde zichtbare borden werken als medewerkers.
- **Niveau 4, Beheersen.** De werkwijze wordt afgemeten aan uitgangswaarden in plaats van aangenomen. Teams volgen doorlooptijd van oplevering, verdelingen van doorlooptijd, deployfrequentie, doorvoer en het deel van de werkweek dat verloren gaat aan vergaderingen met weinig waarde, en ze letten op velocity die wordt bespeeld via puntinflatie. Limieten op werk in uitvoering worden op bewijs gehandhaafd, flow wordt beheerd in plaats van benutting, en de data, niet mening, bepaalt welke ceremonies hun plek houden en waar wachtrijen langer worden. Rapportage aan het bestuur en toezichthouders komt rechtstreeks uit deze live statistieken.
- **Niveau 5, Orkestreren.** De organisatie stelt haar werkwijze continu bij op basis van flowstatistieken en retrospectief bewijs, en de behoefte aan coördinatie wordt aan de bron geminimaliseerd door teamtopologie in plaats van beheerd met zwaarder proces. Werkwijzen, leveringsstatistieken en organisatieontwerp zijn geïntegreerd en passen zich aan naarmate het personeelsbestand, de markt en het regelgevingsbeeld verschuiven. Verspreide, gemengde teams van medewerkers, externe medewerkers en leveranciers over vele tijdzones werken soepel samen, en praktijken die hun kosten niet meer waard zijn, worden zonder ceremonie afgeschaft.

## Ideeën voor discussie

- Welke van onze ceremonies zouden we houden als we ze puur beoordeelden op de waarde die ze creëren?
- Schalen we door een raamwerk toe te voegen of door de behoefte aan coördinatie te verminderen?
- Is onze velocity een planninghulp of een doel dat we stilletjes bespelen?
- Welke beslissingen en status leven alleen in vergaderingen en geheugens van mensen, en moeten worden opgeschreven?
- Wiens tijdzone draagt de kosten van onze synchrone vergaderingen, en is dat eerlijk?
- Werken onze externe medewerkers en leveranciers in dezelfde zichtbare flow als onze medewerkers?

## Belangrijkste inzichten

- Neem de principes achter methodieken over, niet alleen hun rituelen.
- Kies Agile, Kanban of een mengvorm die bij het werk past. Geef de voorkeur aan kleine batches en snelle feedback.
- Benader schaalraamwerken sceptisch. Schaal door coördinatie te verminderen, niet door proces toe te voegen.
- Gebruik schattingen voor gesprek en prognose, nooit als productiviteitsdoelen of beloftes.
- Kies standaard voor asynchrone, documentatie-eerst communicatie zodat grote, verspreide, gemengde teams kunnen samenwerken.
- Optimaliseer voor resultaten en flow, niet voor activiteit of benutting.

## Referenties en verder lezen

- David J. Anderson, "Kanban: Successful Evolutionary Change for Your Technology Business"
- Donald Reinertsen, "The Principles of Product Development Flow"
- Mary and Tom Poppendieck, "Lean Software Development: An Agile Toolkit"
- Craig Larman and Bas Vodde, "Large-Scale Scrum (LeSS)"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (delivery metrics)
- The Agile Manifesto and its twelve principles
- Henrik Kniberg, "Scaling Agile @ Spotify" (with the caution that it is a snapshot, not a model)
- GitLab's public Handbook on asynchronous, remote-first working
