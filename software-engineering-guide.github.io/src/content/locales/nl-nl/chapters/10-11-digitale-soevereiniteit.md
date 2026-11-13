# 10.11 Digitale soevereiniteit

## Overzicht en motivatie

[Digitale soevereiniteit](https://en.wikipedia.org/wiki/Digital_sovereignty) is de mate waarin een organisatie, natie of blok betekenisvolle controle houdt over haar eigen data, software en infrastructuur. Dat betekent controle over waar data fysiek verblijft, welke wetten en regeringen toegang ertoe kunnen afdwingen en of kritieke systemen kunnen blijven opereren zonder afhankelijk te zijn van een buitenlandse macht of één leverancier. Het heeft verschillende dimensies: **[datasoevereiniteit](https://en.wikipedia.org/wiki/Data_sovereignty)** (wiens jurisdictie en wetten de data besturen), **operationele soevereiniteit** (het vermogen systemen te draaien en te beheren zonder toestemming of aanwezigheid van een derde), **softwaresoevereiniteit** (toegang tot en controle over de bron en haar evolutie) en **toeleveringsketensoevereiniteit** (vrijheid van knelpunten in hardware, diensten en afhankelijkheden). Dit hoofdstuk staat in het managementdeel omdat soevereiniteit fundamenteel een strategie-, inkoop- en risicobeslissing is (hoofdstuk 10.1–10.3) met diepe technische gevolgen.

De motivatie is verschoven van theoretisch naar urgent. [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) concentreerde een groot deel van de infrastructuur van de wereld bij een handvol aanbieders, meestal onder de jurisdictie van één land. Extraterritoriale wetten zoals de Amerikaanse [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) (die een aanbieder kan dwingen data bekend te maken ongeacht waar die is opgeslagen) botsen met regimes als de [AVG](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (GDPR) van de EU, een spanning gekristalliseerd door de uitspraak *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* die het EU-VS Privacy Shield ongeldig verklaarde. Voeg geopolitieke schokken, sancties en het risico toe dat een aanbieder wordt afgesneden, en afhankelijkheid wordt een strategische kwetsbaarheid, niet slechts een voetnoot bij leveranciersbeheer. Soevereiniteit is de discipline van bewust beslissen hoeveel van die afhankelijkheid je meest kritieke systemen en data veilig kunnen dragen.

Voor onderneming en vooral overheid is de inzet direct. Multinationals moeten conflicterende gegevensbeschermingsregimes verzoenen en afhankelijkheid van een leverancier vermijden die een toezichthouder of geopolitieke gebeurtenis kan omzetten in een existentiële migratie. Overheden houden data (zorgdossiers, belasting, defensie, burgeridentiteit) waarvan blootstelling aan een buitenlandse jurisdictie een kwestie van nationale veiligheid en publiek vertrouwen is. Daarom zijn "soevereine cloud"-aanbiedingen, initiatieven als het [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) van de EU en nationale certificeringen als SecNumCloud in Frankrijk ontstaan. Het doel is geen autarkie. Het is evenredige controle afgestemd op de gevoeligheid van wat op het spel staat.

## Kernprincipes

- **Soevereiniteit is een spectrum, geen schakelaar.** Stem de mate van controle af op de gevoeligheid van de data en workload.
- **Locatie is geen jurisdictie.** Lokaal opgeslagen data kan nog steeds wettelijk bereikbaar zijn voor een buitenlandse regering. Residentie alleen is geen soevereiniteit.
- **Ontwerp voor uitstap.** Het vermogen een aanbieder te verlaten is de zuiverste maat van soevereiniteit.
- **[Open standaarden](https://en.wikipedia.org/wiki/Open_standard) en [open source](https://en.wikipedia.org/wiki/Open-source_software) verminderen afhankelijkheid:** ze zijn gereedschappen voor strategische autonomie, niet alleen kostenbesparers.
- **Beheer de sleutels.** Wie versleutelingssleutels houdt en beheert doet vaak meer ertoe dan waar de bytes staan.
- **Ruil niet de ene afhankelijkheid voor de andere.** Een enkele "soevereine" leverancier kan even gevangen zijn als een hyperscaler.
- **Wees evenredig.** Soevereiniteit heeft echte kosten. Overal overdraaien verspilt geld en vertraagt oplevering.

## Aanbevelingen

### Deel data en workloads in naar soevereiniteitsgevoeligheid

Niet alles heeft dezelfde bescherming nodig. Deel data en systemen in naar het gevolg van toegang door een buitenlandse jurisdictie of verlies van een aanbieder. Publieke en laag-risicoworkloads kunnen voor schaal en kosten op globale hyperscale-infrastructuur staan. Zeer gevoelige data (nationale veiligheid, zorg, burgeridentiteit, gereguleerde records) verdient sterkere soevereiniteitsmaatregelen. Deze indeling, dezelfde risicogebaseerde logica als dataclassificatie in hoofdstuk 4.5, houdt soevereiniteit betaalbaar, door dure maatregelen te richten waar ze gerechtvaardigd zijn in plaats van alles te lokaliseren.

### Begrijp jurisdictie, niet alleen residentie

**Dataresidentie** (de fysieke of geografische locatie waar data wordt opgeslagen) is noodzakelijk maar niet voldoende. Wat juridisch telt is *jurisdictie*: welke regeringen openbaarmaking kunnen afdwingen, en onder welke wetten. Een dataset in een datacentrum in eigen land beheerd door een buitenlands gevestigde aanbieder kan nog steeds bereikbaar zijn onder het recht van het thuisland van die aanbieder (het CLOUD Act-probleem). Breng de juridische blootstelling van elk systeem in kaart: hoofdkantoor van de aanbieder, toepasselijke wetten en eventuele adequaatheidsbesluiten of overdrachtsmechanismen (Standard Contractual Clauses, het EU-VS Data Privacy Framework). Behandel die juridische kaart dan als eersterangs onderdeel van de architectuur (hoofdstuk 4.5, 4.6).

### Ontwerp voor overdraagbaarheid en omkeerbaarheid

De meest duurzame soevereiniteitsmaatregel is een geloofwaardige uitstap. Geef de voorkeur aan open standaarden en overdraagbare formaten (hoofdstuk 3.8). Containeriseer workloads zodat ze kunnen verhuizen. Houd infrastructure as code (hoofdstuk 8.2) zodat een omgeving elders kan worden herbouwd. Vermijd diepe afhankelijkheid van de eigen diensten van één aanbieder voor je meest kritieke systemen. Onderhoud en *test* periodiek een uitstapplan, een escrow van data en configuratie plus een gerepeteerd pad naar een alternatief, zodat "we zouden kunnen vertrekken als we moesten" een aangetoond feit is, geen hoop. Dit is het tegengif voor **[afhankelijkheid van een leverancier](https://en.wikipedia.org/wiki/Vendor_lock-in)**, de toestand niet van aanbieder te kunnen wisselen zonder onbetaalbare kosten of verstoring.

### Gebruik soevereine infrastructuur en sleutelbeheer waar gerechtvaardigd

Voor de meest gevoelige laag bestaan sterkere technische maatregelen: **soevereine cloud**-aanbiedingen (cloudregio's beheerd door of in partnerschap met entiteiten binnen de jurisdictie, soms gecertificeerd zoals SecNumCloud), **[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing)** (hardwaregebaseerde vertrouwde uitvoering die data versleuteld houdt zelfs terwijl die wordt verwerkt) en door de klant beheerde versleutelingssleutels: **bring your own key (BYOK)** en, sterker, **hold your own key (HYOK)**, waar de aanbieder nooit toegang heeft tot de sleutels die de data ontgrendelen. Sleutels beheren kan veel van het praktische voordeel van soevereiniteit leveren, zelfs op gedeelde infrastructuur. Data die een aanbieder niet kan ontsleutelen is data die ze niet betekenisvol kan bekendmaken.

### Geef de voorkeur aan open source en open ecosystemen voor strategische autonomie

Open-sourcesoftware en open standaarden zijn onder de sterkste soevereiniteitshefbomen, omdat ze de noodknop van één leverancier verwijderen. De bron kan worden gedraaid, geaudit, geforkt en onderhouden onafhankelijk van enige leverancier (hoofdstuk 10.3, 3.8). Beleid van "public money, public code" in de publieke sector en initiatieven als Gaia-X weerspiegelen dit. Open source is niet automatisch soeverein. Ze heeft nog steeds bekwame mensen nodig om te draaien en te ondersteunen, en haar toeleveringsketen moet worden beveiligd (hoofdstuk 4.2). Maar ze zet afhankelijkheid van een leverancier om in afhankelijkheid van een gemeenschap en je eigen vermogen, wat veel makkelijker te beheersen is.

### Bestuur soevereiniteit als evenredig risico, niet als absolute

Zet een soevereiniteitsrisicokader op naast je andere governance (hoofdstuk 10.2, 1.5). Beoordeel het concentratie- en jurisdictierisico van grote platformen. Besluit doelniveaus van soevereiniteit per datalaag en weeg ze tegen kosten, vermogen en leveringssnelheid. Het doel is een verdedigbare, gedocumenteerde positie ("deze workloads accepteren hyperscale-afhankelijkheid, deze vereisen controle binnen de jurisdictie, hier is onze uitstaphouding"), herzien naarmate geopolitiek en regelgeving veranderen, geen eenmalig absoluut standpunt.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| **Globale hyperscale-cloud** | Schaal, functies, lage kosten, snelheid | Jurisdictieblootstelling. Concentratie- en afhankelijkheidsrisico |
| **Soevereine cloud / aanbieder binnen de jurisdictie** | Juridische controle. Past bij nationale veiligheid. Vertrouwen | Hogere kosten. Minder functies. Vaak kleinere schaal. Nieuwe afhankelijkheid |
| **Sleutelbeheer (BYOK/HYOK) op gedeelde infrastructuur** | Veel van het voordeel tegen lagere kosten. Behoudt schaal | Operationele complexiteit. Risico van sleutelbeheer. Niet absoluut |
| **Open source / zelf gehost** | Controleerbaarheid, forkbaarheid, geen noodknop van een leverancier | Vraagt intern vermogen. Je bezit het beheer en de beveiliging |
| **Verplichte datalokalisatie** | Regelgevende naleving. Politieke zekerheid | Kostbaar. Versnippert data. Kan veerkracht en bruikbaarheid verminderen |

De bepalende spanning is **controle tegenover vermogen en kosten**. Maximale soevereiniteit (zelf gehost, binnen de jurisdictie, open source, volledig overdraagbaar) offert de schaal, functies en snelheid van globale platformen op. Maximaal vermogen accepteert afhankelijkheid en jurisdictieblootstelling. De oplossing is indeling in lagen: betaal voor soevereiniteit waar het gevolg het rechtvaardigt en neem pragmatische afhankelijkheid waar niet.

## Vragen om met je team te bespreken

1. **Hebben we onze data en workloads ingedeeld naar soevereiniteitsgevoeligheid, zodat dure maatregelen alleen landen waar ze gerechtvaardigd zijn?** Soevereiniteit is een spectrum, geen schakelaar, en alles lokaliseren verbrandt geld, verspeelt vermogen en kan zelfs veerkracht verminderen door je opties te verkleinen. Deel elk systeem in naar het gevolg van toegang door een buitenlandse jurisdictie of verlies van een aanbieder: publieke en laag-risicoworkloads kunnen op globale hyperscale-infrastructuur staan, terwijl data over nationale veiligheid, zorg of burgeridentiteit sterkere maatregelen verdient. Dit is dezelfde risicogebaseerde logica als dataclassificatie, en het houdt soevereiniteit betaalbaar. Neem je kroonjuweelsystemen en hun huidige hosting mee en vraag of de bescherming bij de gevoeligheid past. Als je alles gelijk beschermt, betaal je vrijwel zeker ergens te veel en ben je elders blootgesteld.

2. **Maken open standaarden en open source deel uit van onze soevereiniteitsstrategie, of behandelen we ze alleen als kostenbesparers?** Bron die je kunt draaien, auditen, forken en onderhouden verwijdert de noodknop van één leverancier, een van de sterkste autonomiehefbomen die je hebt. Open standaarden en overdraagbare formaten maken een geloofwaardige uitstap mogelijk, en een geloofwaardige uitstap is de zuiverste maat van soevereiniteit. De subtielere valkuil is een hyperscaler ontsnappen om dan volledig gevangen te raken bij één "soevereine" leverancier zonder uitstap: je ruilde de ene afhankelijkheid voor de andere. Neem je meest kritieke platformen mee en vraag hoe strak elk aan de eigen diensten van één aanbieder is gebonden. Waar het antwoord "heel" is, zijn open standaarden en gecontaineriseerde, herbouwbare omgevingen de goedkoopste manier om de greep te verlossen.

3. **Wie bezit ons soevereiniteitsrisicokader, en hoe vaak herzien we het standpunt naarmate recht en geopolitiek verschuiven?** Een soevereiniteitspositie die eenmaal wordt vastgesteld en nooit herzien wordt fictie op het moment dat een uitspraak, sanctie of nieuwe wet landt, en die schokken komen nu regelmatig. Zet een levend kader op naast je andere governance: beoordeel het concentratie- en jurisdictierisico van grote platformen, stel doelniveaus van soevereiniteit per datalaag en documenteer een verdedigbare positie die je een toezichthouder kunt tonen. Noem de eigenaar en het herzieningsritme. Neem de vraag mee hoe een sanctie of ongunstige uitspraak tegen je belangrijkste aanbieder je kritieke diensten volgende week zou raken. Als niemand kan antwoorden, bestaat het kader nog niet.

4. **Wie houdt de versleutelingssleutels voor onze meest gevoelige data, en zou onze aanbieder kunnen worden gedwongen die data in leesbare vorm over te dragen?** Residentie en zelfs een "soevereine" regio tellen weinig als de beheerder de sleutels behoudt, omdat een openbaarmakingsbevel dan ontsleutelde data bereikt waar de bytes ook staan. De sleutels zelf beheren, via bring your own key of het sterkere hold your own key, waar de aanbieder ze nooit ziet, levert vaak het grootste deel van het praktische voordeel van soevereiniteit op gedeelde infrastructuur tegen een fractie van de kosten van alles verhuizen. De concurrerende overweging is operationeel: sleutelbeheer is meedogenloos, en een verloren of verkeerd behandelde sleutel kan je net zo zeker buitensluiten van je eigen data als elke sanctie. Neem een inventaris mee van welke datasets zijn versleuteld, wie elke sleutel werkelijk houdt en wat je herstelpad is als een sleutel verloren gaat, en leg dat naast je soevereiniteitslagen. Behandel voor onderneming en overheid sleutelbewaring als de lijn die bepaalt of een buitenlands openbaarmakingsbevel versleutelde tekst of leesbare tekst oplevert, en maak dat een inkoopeis in plaats van een latere nabouw.

5. **Zouden we onze primaire aanbieder werkelijk kunnen verlaten binnen een termijn die ertoe doet, en wanneer repeteerden we dat voor het laatst?** Een geloofwaardige uitstap is de zuiverste maat van soevereiniteit, maar de meeste uitstapplannen leven op papier en zijn nooit uitgevoerd, zodat overdraagbaarheid een hoop blijft in plaats van een aangetoond feit. De spanning is kosten en focus: een uitstap repeteren, workloads gecontaineriseerd houden en een escrow van data en configuratie houden verbruiken allemaal engineeringaandacht die leveringsdruk liever elders zou besteden. Neem je meest kritieke systeem mee, een eerlijke schatting van hoe lang een gedwongen migratie zou duren, de lijst van eigen diensten waarvan het afhangt en de datum van je laatste werkelijke repetitie (als die er was). Voor een grote of publieke organisatie met meerjarige uitstapverplichtingen in contracten is een ongerepeteerde uitstap een toezegging die je wettelijk misschien niet kunt nakomen, dus behandel een repetitieritme als onderdeel van de beheerkosten van het systeem, niet een optionele oefening.

6. **Weten we voor elk kroonjuweelsysteem welke regeringen er vandaag wettelijk toegang toe kunnen afdwingen, ongeacht waar de data fysiek staat?** Locatie is geen jurisdictie: data in een datacentrum in eigen land kan nog steeds bereikbaar zijn onder het thuisland-recht van een buitenlands gevestigde beheerder, en teams verwarren routinematig residentie met juridische bescherming. Het moeilijke is dat het antwoord juridische en inkoopinput vraagt, niet slechts een architectuurdiagram, en de kaart verschuift naarmate adequaatheidsbesluiten, uitspraken en overdrachtsmechanismen veranderen. Neem voor elke kritieke dataset het hoofdkantoor van de aanbieder mee, de wetten die erop reiken en het overdrachtsmechanisme waarop je leunt, en wees eerlijk waar niemand het werkelijk weet. In gereguleerde en publieke omgevingen is een niet-in-kaart-gebrachte juridische blootstelling op burger- of nationale-veiligheidsdata een bevinding die staat te gebeuren bij de volgende audit, dus financier het juridische in-kaartbrengen even expliciet als je de infrastructuur financiert.

## Sectorperspectief

**Startup.** Snelheid en runway domineren, dus koop soevereiniteit als dunne functie in plaats van een soevereine stack te bouwen die je niet kunt bemannen. Als de jurisdictie van een klant de beperking is, deploy dan naar de regio-optie van je bestaande aanbieder, houd je eigen versleutelingssleutels zodat de beheerder gevoelige records niet kan ontsleutelen en houd de workload gecontaineriseerd zodat ze overdraagbaar blijft. Dat sluit de deal tegen een kostenpost van een seed-fase en vermijdt een herarchitectuur waarvoor je geen runway hebt.

**Kleinbedrijf.** Zonder soevereiniteitsspecialist en met een krap budget behandel je dit als contractreview en leverancierskeuze, niet een engineeringprogramma. Geef de voorkeur aan leveranciers die regio's binnen de jurisdictie, transparante gegevensverwerkingsvoorwaarden en door de klant beheerde sleutels als standaardfuncties bieden, en lees de clausules over subverwerkers en openbaarmaking voordat je tekent. Zelf hosten voor soevereiniteit loont hier zelden: je zou de last van beheer en beveiliging erven zonder de mensen om die te dragen.

**Grote onderneming.** De taak is portfoliogovernance over veel teams: een gedeelde indeling van data naar soevereiniteitsgevoeligheid, een concentratierisicoblik op hoeveel kritieke belasting bij één aanbieder of jurisdictie zit en gestandaardiseerd sleutelbeheer, overdraagbaarheid en uitstaprepetities zodat elke groep ophoudt zijn eigen ongecoördineerde weddenschap te nemen. Begroot de hogere kosten en operationele last van de gevoelige laag expliciet en houd een gedocumenteerd, controleerbaar standpunt dat je een toezichthouder kunt tonen. Beheer soevereiniteit als levend risico met statistieken en herzieningsritme, niet als eenmalige migratie.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Geef de voorkeur aan gecertificeerde soevereine infrastructuur (bijvoorbeeld kwalificatie in SecNumCloud-stijl) en open standaarden en open source zodat het platform onafhankelijk van enige enkele leverancier kan worden onderhouden, en eis overdraagbaarheid en openbaarmaking van juridische blootstelling in het contract zelf. Publiceer een beschrijving in gewone taal van waar burgerdata staat en wie erbij kan, reserveer dure soevereine maatregelen voor de werkelijk gevoelige laag en houd minder gevoelige publieke diensten op goedkopere globale infrastructuur.

## Voorbeelden

**Startup.** Een kleine health-techstartup landt haar eerste ziekenhuisklant in Duitsland, wat vereist dat patiëntdata onder EU-jurisdictie blijft. In plaats van een soevereine stack te overbouwen die ze zich niet kan veroorloven, deployen de oprichters naar de EU-regio van hun bestaande cloudaanbieder, houden ze hun eigen versleutelingssleutels zodat de aanbieder de gevoelige records niet kan ontsleutelen en houden ze de workload gecontaineriseerd zodat ze overdraagbaar blijft. Dit koopt het grootste deel van het soevereiniteitsvoordeel dat de klant nodig heeft tegen een prijs die een team in seed-fase kan dragen, en sluit de deal zonder een volledige herarchitectuur.

**Grote onderneming.** Een multinationale bank moet bepaalde klantdata binnen de EU houden en buiten bereik van buitenlands openbaarmakingsrecht. In plaats van haar globale cloudaanbieder te verlaten deelt ze haar landschap in. Algemene workloads blijven voor schaal op hyperscale-regio's. Gereguleerde klantdata draait in EU-regio's met **hold your own key**-versleuteling (de aanbieder kan haar niet ontsleutelen) en een getest uitstapplan naar een alternatieve aanbieder. Dit voldoet aan toezichthouders en aan de eigen concentratierisicobereidheid van de bank (hoofdstuk 10.2) zonder een volledige, vermogensvernietigende migratie.

**Overheid.** Een nationale gezondheidsdienst houdt de medische dossiers van burgers en acht blootstelling aan een buitenlandse jurisdictie onaanvaardbaar. Ze koopt een soevereine cloud aan, dat wil zeggen infrastructuur beheerd door een entiteit in eigen land onder nationale certificering (bijv. in SecNumCloud-stijl), met confidential computing voor de meest gevoelige verwerking, en schrijft open standaarden (hoofdstuk 3.8) en open-sourcecomponenten voor zodat het platform onafhankelijk van enige enkele leverancier kan worden onderhouden. De hogere kosten en smallere functieset worden aanvaard als prijs van controle voor nationale veiligheid en publiek vertrouwen. Ondertussen blijven minder gevoelige diensten (een publiek informatieportaal) op goedkopere globale infrastructuur.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De economie van digitale soevereiniteit is asymmetrisch en wordt het best geformuleerd als verzekering tegen gebeurtenissen met lage kans en grote impact. De kosten zijn zichtbaar en terugkerend: soevereine infrastructuur en infrastructuur binnen de jurisdictie is doorgaans duurder, biedt minder beheerde diensten en vraagt meer intern operationeel vermogen, wat allemaal de total cost of ownership verhoogt en oplevering kan vertragen. De voordelen zijn vooral vermeden catastrofes: wettelijke boetes en gedwongen herarchitectuur na een uitspraak als *Schrems II*, een bedrijfsbeëindigend verlies van toegang als een aanbieder wordt gesanctioneerd of afgesneden, of de reputatie- en nationale-veiligheidsschade van buitenlandse openbaarmaking van gevoelige data. Omdat die staartrisico's ernstig en steeds plausibeler zijn, is evenredige investering in soevereiniteit, vooral goedkope-maar-krachtige maatregelen als sleuteleigendom, overdraagbaarheid en open standaarden, vaak sterk positief in verwachte waarde, ook al lijkt het op een spreadsheet met stabiele toestand puur kosten.

De valkuil aan beide kanten is onevenredigheid. *Onder*investeren laat kritieke data en systemen blootgesteld aan één jurisdictie of leverancier zonder uitstap, wat een beheersbaar risico in een existentieel verandert. *Over*investeren, door alles te lokaliseren en alle globale platformen te weigeren, verbrandt geld, verspeelt vermogen en kan *veerkracht verminderen* door je opties te verkleinen. Koppel soevereiniteitsuitgaven voor leiderschap aan een risico-indeling van data en workloads. Kwantificeer de concentratie- en jurisdictieblootstelling van de kroonjuweelsystemen. Prijs de goedkope maatregelen (sleutels, overdraagbaarheid, uitstaprepetities) die ze de-risken. Reserveer dure soevereine infrastructuur voor de laag die het werkelijk verdient.

## Antipatronen en valkuilen

- **Soevereiniteitstoneel:** dataresidentie in eigen land adverteren terwijl een buitenlands gevestigde aanbieder wettelijke toegang tot de data behoudt.
- **Versleuteling verwarren met soevereiniteit:** data versleutelen maar de aanbieder de sleutels laten houden, zodat die nog steeds kan worden gedwongen te ontsleutelen.
- **Overdraaien:** alles lokaliseren en zelf hosten tegen ruïneuze kosten en verminderd vermogen, ongeacht gevoeligheid.
- **Nieuwe enkele afhankelijkheid:** een hyperscaler ontsnappen door volledig gevangen te raken bij één "soevereine" leverancier zonder uitstap.
- **Geen geteste uitstap:** een uitstapplan dat op papier bestaat maar nooit is gerepeteerd, zodat overdraagbaarheid onbewezen is.
- **De menselijke toeleveringsketen negeren:** aannemen dat open source of zelf hosten soevereiniteit verleent zonder de bekwame mensen om het te draaien.
- **Statisch standpunt:** een soevereiniteitspositie eenmaal vaststellen en nooit herzien naarmate recht en geopolitiek verschuiven.

## Volwassenheidsmodel

- **Niveau 1 (Initiëren):** Soevereiniteit wordt niet overwogen en is reactief. Data en kritieke systemen staan waar het het goedkoopst is, zonder kaart van jurisdictie- of concentratierisico en zonder eigenaar.
- **Niveau 2 (Ontwikkelen):** Dataresidentie wordt aangepakt voor de meest voor de hand liggende gereguleerde data op sommige projecten, maar jurisdictie, sleutelbeheer en uitstap worden niet systematisch overwogen. Praktijken variëren per team en afhankelijkheid van enkele aanbieders is onbeproefd.
- **Niveau 3 (Standaardiseren):** Data en workloads zijn ingedeeld naar soevereiniteitsgevoeligheid onder een gedocumenteerd beleid organisatiebreed toegepast. Jurisdictie is in kaart gebracht. Sleutelbeheer, overdraagbaarheid en open standaarden zijn vereist op gevoelige lagen. Uitstapplannen bestaan en zijn voorgeschreven in plaats van optioneel.
- **Niveau 4 (Beheersen):** Het standpunt wordt gemeten en beheerst tegen uitgangswaarden: concentratierisico (het aandeel kritieke workloads bij één aanbieder of jurisdictie), dekking van sleuteleigendom over gevoelige datasets, volledigheid van jurisdictiekaart en gerepeteerde uitstaptijden worden als statistieken gevolgd, aan governance gerapporteerd en tegen drempels afgedwongen, zodat een afdrijvende afhankelijkheid actie op bewijs triggert in plaats van na een schok.
- **Niveau 5 (Orkestreren):** Soevereiniteit wordt continu verbeterd en over de organisatie geïntegreerd: het levende risicokader voedt standaard architectuur-, inkoop- en risicoplanning, uitstappen worden routinematig gerepeteerd en de organisatie bakent lagen adaptief opnieuw af, herbalanceert aanbieders en herziet haar standpunt naarmate uitspraken, sancties en regelgeving verschuiven.

## Ideeën voor discussie

1. Welke regeringen kunnen voor je meest gevoelige dataset vandaag wettelijk toegang afdwingen, en weet je dat?
2. Is je dataresidentie echte soevereiniteit, of houdt een buitenlands gevestigde aanbieder nog de sleutels en de juridische blootstelling?
3. Zou je je primaire cloudaanbieder werkelijk kunnen verlaten als het moest, en heb je het ooit getest?
4. Welke van je workloads hebben werkelijk soevereine infrastructuur nodig, en welke bescherm je te veel tegen nodeloze kosten?
5. Waar zou het beheren van je eigen versleutelingssleutels je het grootste deel van het soevereiniteitsvoordeel geven tegen een fractie van de kosten?
6. Hoe zou een sanctie, uitval of juridische uitspraak tegen je belangrijkste aanbieder je kritieke diensten volgende week raken?

## Belangrijkste inzichten

- Digitale soevereiniteit is evenredige controle over je data, software en infrastructuur, over de dimensies van data, operatie, software en toeleveringsketen.
- **Locatie is geen jurisdictie:** residentie alleen voorkomt geen buitenlandse juridische toegang. Breng in kaart wie openbaarmaking kan afdwingen.
- **Ontwerp voor uitstap** en **beheer je sleutels:** overdraagbaarheid en sleuteleigendom zijn de maatregelen met de hoogste hefboom en laagste kosten.
- **Open standaarden en open source** zijn gereedschappen voor strategische autonomie. Reserveer dure **soevereine cloud** voor de laag die het verdient.
- Bestuur soevereiniteit als **evenredig, levend risico** (hoofdstuk 10.2, 10.3, 4.5, 4.6, 3.8), onderbescherming en ruïneus overdraaien beide vermijdend.
- Het rendement is verzekering tegen ernstige staartrisico's (regelgevend, geopolitiek en afhankelijkheid) afgezet tegen echte, terugkerende kosten.

## Referenties en verder lezen

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, *SecNumCloud* qualification framework (France).
- Gaia-X European Association for Data and Cloud (Gaia-X initiative).
- ENISA, reports on cloud security and EU cybersecurity certification (EUCS).
- Julia Pohle and Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, writings on European digital autonomy and dependency on foreign providers.
- Kai Zenner and others, analyses of EU digital sovereignty policy (for context; verify current sources).
