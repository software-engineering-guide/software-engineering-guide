# 5.3 Toegankelijkheid

## Overzicht en motivatie

[Toegankelijkheid](https://en.wikipedia.org/wiki/Accessibility) (vaak afgekort tot "a11y") is de praktijk van software bouwen die mensen met een beperking kunnen waarnemen, begrijpen, doorlopen en gebruiken. Dat omvat mensen die blind zijn of slechtziend, doof of slechthorend, motorische beperkingen hebben, cognitieve of leerverschillen hebben en mensen die tijdelijke of situationele beperkingen ervaren, zoals een gebroken arm, felle zon of een lawaaiige ruimte. Ongeveer één op de vijf mensen heeft een beperking, en iedereen profiteert op enig moment van toegankelijk ontwerp. Dit is geen nicheaanpassing. Het is een basis van kwaliteit.

Voor grote teams moet toegankelijkheid in het systeem worden ingebouwd, niet worden overgelaten aan individuele goede bedoelingen. Wanneer veel teams in één product opleveren, kan één ontoegankelijk onderdeel (een formulierveld zonder label, een statusindicator alleen met kleur, een toetsenbordval in een modal) gebruikers met een beperking uit een hele reis buitensluiten. Toegankelijkheid inbouwen in gedeelde componenten, designtokens, testpipelines en definities van klaar is de enige manier om haar op schaal betrouwbaar te maken. Achteraf aanpassen is duur en foutgevoelig. Erin ontwerpen is goedkoop en duurzaam.

Voor de overheid is toegankelijkheid een wettelijke eis en een burgerplicht, geen nette extra. Publieke diensten moeten elk lid van het publiek bedienen, en burgers met een beperking hebben vaak geen alternatieve aanbieder: als de overheidswebsite ontoegankelijk is, kunnen ze hun uitkering, vergunning of stem niet op een andere manier krijgen. Wetten en standaarden over de hele wereld maken toegankelijkheid verplicht voor publieke organen en steeds vaker ook voor de private sector. Dit hoofdstuk behandelt toegankelijkheid als drie dingen tegelijk: een wettelijke plicht, een ethische plicht en gewoon goed ontwerp.

*Zie ook:* hoofdstuk 5.2 (UI-ontwerp en designsystemen), hoofdstuk 5.6 (frontend-engineering) en hoofdstuk 5.1 (UX-fundamenten).

## Kernprincipes

- Toegankelijkheid is een basiskwaliteitsattribuut, zoals beveiliging en prestaties, geen optionele functie.
- De POUR-principes: interfaces moeten Waarneembaar (Perceivable), Bedienbaar (Operable), Begrijpelijk (Understandable) en Robuust (Robust) zijn.
- Eerst [semantische HTML](https://en.wikipedia.org/wiki/Semantic_HTML). Gebruik [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) alleen om echte gaten te vullen, nooit als vervanging voor native elementen.
- Alles wat met een muis te gebruiken is moet met alleen een toetsenbord te gebruiken zijn.
- Breng informatie niet alleen over met kleur, vorm of positie.
- Geautomatiseerde tools vangen maar een fractie van de problemen. Handmatig testen en testen met [hulptechnologie](https://en.wikipedia.org/wiki/Assistive_technology) zijn essentieel.
- Toegankelijk ontwerp is beter ontwerp voor iedereen (het ["stoepranden-effect"](https://en.wikipedia.org/wiki/Curb_cut), waarbij functies gebouwd voor mensen met een beperking alle gebruikers ten goede komen).
- Ontwerp en test met mensen met een beperking, niet alleen voor hen.

## Aanbevelingen

### Ontwerp en bouw naar WCAG, gericht op de huidige standaard

De [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) zijn de internationale referentie. WCAG 2.1 en 2.2 zijn georganiseerd onder de vier POUR-principes, met toetsbare succescriteria op conformiteitsniveaus A, AA en AAA. Richt je op niveau AA als basis. Het is waar de meeste wetten naar verwijzen. WCAG 2.2 voegt criteria toe voor zichtbaarheid van focus, doelgrootte en het verminderen van cognitieve belasting. WCAG 3.0 is een opkomende opvolger, anders gestructureerd en nog in ontwikkeling. Houd het in de gaten, maar bouw vandaag naar 2.2 AA. Behandel de richtlijnen als vloer, niet als plafond: elk criterium halen garandeert geen werkelijk bruikbare ervaring.

### Gebruik semantische HTML en correcte ARIA

Native HTML-elementen (knoppen, links, formulierbesturing, koppen, lijsten, landmarks) komen met ingebouwde toegankelijkheidssemantiek, toetsenbordgedrag en ondersteuning voor hulptechnologie. Gebruik ze eerst. Grijp naar ARIA-rollen, -toestanden en -eigenschappen (Accessible Rich Internet Applications) alleen om aangepaste widgets te beschrijven die HTML niet kan uitdrukken, en volg de ARIA Authoring Practices. De eerste regel van ARIA is simpel: gebruik geen ARIA als een native element volstaat. Onjuiste ARIA is erger dan geen: ze misleidt [schermlezers](https://en.wikipedia.org/wiki/Screen_reader) actief. Geef de pagina een logische kopstructuur, betekenisvolle labels, alternatieve tekst voor afbeeldingen, ondertitels en transcripties voor media en een programmatische koppeling tussen elk label en zijn besturing.

### Garandeer bedienbaarheid met toetsenbord en hulptechnologie

Elk interactief element moet bereikbaar en bedienbaar zijn met alleen het toetsenbord, in een logische volgorde, met een duidelijk zichtbare focusindicator. Vermijd toetsenbordvallen. Beheer focus bewust wanneer content verandert: verplaats focus naar een dialoog wanneer die opent, geef haar terug wanneer de dialoog sluit en kondig dynamische updates aan via live regions. Test met echte hulptechnologieën, inclusief schermlezers op desktop en mobiel, schermvergroting, spraakbesturing en switchtoegang. En respecteer gebruikersvoorkeuren zoals verminderde beweging en verhoogd contrast.

### Test met geautomatiseerde tools, handmatige review en echte gebruikers

Geautomatiseerde toegankelijkheidsscanners zijn waardevol en moeten bij elke wijziging in de pipeline draaien. Maar onderzoeken tonen consequent dat ze maar een minderheid van de echte problemen vangen, ruwweg een derde. De rest vraagt menselijk oordeel: toetsenbordrondgangen, schermlezertests, contrastcontroles en vragen of de content werkelijk te begrijpen is. Het belangrijkst van alles, betrek mensen met een beperking bij usabilitytesten. Bouw toegankelijkheidsacceptatiecriteria in de definitie van klaar in, zodat problemen per story worden gevangen in plaats van in een audit vlak voor lancering.

### Maak toegankelijkheid organisatorisch, niet heroïsch

Bak toegankelijkheid in het designsysteem zodat componenten standaard toegankelijk worden opgeleverd. Bied training zodat ontwerpers, engineers, contentschrijvers en productmanagers elk weten waarvoor ze verantwoordelijk zijn. Stel een toegankelijkheidsstandaard vast, een eigenaar of expertisecentrum en een herstelproces. Publiceer een toegankelijkheidsverklaring en geef gebruikers een manier om barrières te melden. En koop toegankelijk in: eis dat leveranciers en componenten van derden voldoen en bewijs leveren (zoals een toegankelijkheidsconformiteitsrapport).

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Toegankelijkheid vanaf het begin inbouwen | Goedkoopst, duurzaam, beter voor iedereen | Vraagt training en discipline vooraf |
| Later achteraf aanpassen / herstellen | Stelt inspanning uit, maakt snelle lancering mogelijk | Veel duurder, kwetsbaar, juridische blootstelling in de tussentijd |
| Alleen geautomatiseerd testen | Snel, goedkoop, vangt regressies in CI | Mist ~twee derde van de problemen. Valse zekerheid |
| Handmatig + testen met hulptechnologie | Vangt echte usabilitybarrières | Langzamer, vraagt vaardige testers en apparaten |
| Testen met gebruikers met een beperking | Ground truth over echte ervaring | Wervingsinspanning en kosten, moet respectvol gebeuren |

De centrale afweging is discipline vooraf tegenover uitgestelde kosten. Ingebouwde toegankelijkheid is goedkoop en verbetert de kwaliteit voor iedereen. Toegankelijkheid achteraf onder juridische druk aangebracht is duur, onvolledig en stressvol. Op lange termijn is er geen echte afweging tegen "snelheid": ontoegankelijke software werkt gewoon niet voor een vijfde van je gebruikers. Dat is een defect, geen besparing.

## Vragen om met je team te bespreken

1. **Laten toegankelijkheidsregressies onze build falen zoals een kapotte test dat doet, en zo niet, waarom niet?** Geautomatiseerde scanners vangen maar ongeveer een derde van de problemen, maar degene die ze vangen (ontbrekende labels, contrastfouten, onbenoemde besturing) zijn goedkoop te vangen in CI en duur te vinden in een audit vlak voor lancering. Een regressie als buildfout behandelen is wat toegankelijkheid verplaatst van heroïsche individuele inspanning naar een betrouwbare systeemeigenschap, het enige wat werkt wanneer veel teams in één product opleveren. Besluit welke controles blokkerend zijn, welke adviserend en wie een falen mag overschrijven. Neem je huidige scannerresultaten en je definitie van klaar mee naar de vergadering. Als toegankelijkheidscriteria niet per story in de definitie van klaar staan, worden ze gedeprioriteerd zodra een deadline strakker wordt.

2. **Wat is onze regel voor aangepaste widgets, en wie beoordeelt de ARIA voordat ze wordt opgeleverd?** Native HTML-elementen komen met toetsenbordgedrag en ondersteuning voor hulptechnologie gratis, en onjuiste ARIA is erger dan geen omdat ze schermlezers actief misleidt. Spreek af dat semantische HTML de standaard is en dat elke aangepaste widget (een maatwerkdropdown, datumkiezer of modal) een rondgang met toetsenbord en schermlezer vereist vóór merge, volgens de ARIA Authoring Practices. Dit telt het zwaarst voor de interactieve componenten die veel teams hergebruiken, omdat één kapotte modal met een toetsenbordval gebruikers met een beperking uit een hele reis kan buitensluiten. Neem een lijst van je aangepaste widgets mee en vraag welke met een echte schermlezer zijn getest. Alle die dat niet zijn, zijn verplichtingen verborgen in gedeelde code.

3. **Wat is ons beleid over toegankelijkheidsoverlays, en gelooft iemand dat ze een echte oplossing zijn?** Overlays worden verkocht als script van één regel dat een site conform maakt, en ze zijn verleidelijk wanneer juridische druk komt en een deadline dreigt. Ze leveren geen echte conformiteit, ze kunnen de ervaring voor gebruikers van hulptechnologie verslechteren en voor de overheid laten ze de onderliggende wettelijke plicht onvervuld. Besluit expliciet dat je investeert in semantische opmaak, toetsenbordondersteuning en testen met mensen met een beperking in plaats van een widget te kopen die het probleem toedekt. Neem de kosten van een overlayabonnement mee en vergelijk ze met toegankelijkheid eenmaal in je componenten en pipeline bouwen. Dit vroeg formuleren voorkomt een paniekerige aankoopbeslissing later die geld uitgeeft en niets repareert.

4. **Maken mensen met een beperking deel uit van ons ontwerp en testen, of ontwerpen we nog voor een verbeelde gebruiker die we verzonnen?** Geautomatiseerde scanners en zelfs expertaudits vertellen of opmaak conform is. Ze vertellen niet of een blinde gebruiker je checkout werkelijk kan afronden of iemand met een cognitieve beperking je foutmeldingen kan begrijpen. Deelnemers met een beperking betrekken is de enige bron van ground truth en verandert wat je bouwt, maar het roept echte vragen op over hoe je eerlijk werft, hoe je mensen vergoedt voor hun tijd en hoe je voorkomt één deelnemer als woordvoerder van elke beperking te behandelen. Neem je huidige onderzoeksbestand mee, je werving- en betalingspraktijken en een eerlijke telling van hoeveel studies het afgelopen jaar deelnemers met een beperking bevatten. Voor een grote organisatie maakt een terugkerend panel met eerlijke vergoeding en dekking over visuele, auditieve, motorische en cognitieve behoeften dit van een eenmalig gebaar tot een betrouwbare input. Bij de overheid is het betrekken van het publiek dat je dient vaak onderdeel van de wettelijke en burgerlijke plicht, geen optionele aardigheid.

5. **Wanneer we een component van derden kopen of inbedden, eisen we dan bewijs van toegankelijkheid, en wie controleert het?** Veel van wat in een groot product wordt opgeleverd is niet intern geschreven: een datumkiezer uit een bibliotheek, een betaalwidget in een iframe, een grafiekpakket, een hele SaaS-module. Eén ontoegankelijke ingebedde component kan een hele reis laten falen hoe schoon je eigen code ook is, en zodra hij is ingebouwd is vervangen duur. Besluit dat toegankelijkheid een aanbestedingsvereiste is, dat leveranciers een toegankelijkheidsconformiteitsrapport moeten leveren (een document zoals een VPAT dat stelt hoe een product zich meet tegen WCAG) en dat iemand technisch de claim valideert in plaats van hem te archiveren. Neem een inventaris van je componenten van derden mee en vraag welke actueel, geloofwaardig conformiteitsbewijs hebben. Schrijf bij inkoop door onderneming en overheid WCAG 2.2 AA-conformiteit en een recht op herstel in het contract, want een belofte gedaan vóór ondertekening is veel goedkoper af te dwingen dan een barrière ontdekt na livegang.

6. **Wat is ons doelconformiteitsniveau, wie bezit het en hoe houden we het actueel naarmate standaarden verschuiven?** WCAG 2.2 AA is vandaag de vloer en de meeste wetten verwijzen ernaar, maar 2.2 voegde criteria toe die veel teams niet hebben overgenomen, en WCAG 3.0 komt met een andere structuur. Zonder benoemde eigenaar drijft de standaard af: verschillende teams richten zich op verschillende versies, niemand volgt het gat en conformiteit rot stilletjes tussen audits. Besluit de exacte versie en het niveau waarnaar je bouwt, wie de bevoegdheid heeft het te verhogen en hoe nieuwe criteria het designsysteem en de definitie van klaar bereiken. Neem je huidige geformuleerde doel mee, bewijs van waar teams er werkelijk aan voldoen en een korte roadmap voor het overnemen van 2.2-criteria die je oversloeg. Voor een grote of publieke organisatie laten een toegankelijkheidseigenaar of expertisecentrum, een gepubliceerde toegankelijkheidsverklaring en een gedocumenteerd plan voor de volgende standaardversie je een toezichthouder of rechter met bewijs antwoorden in plaats van met goede bedoelingen.

## Sectorperspectief

**Startup.** Snelheid werkt hier in je voordeel, omdat toegankelijkheid het goedkoopst is wanneer de codebasis klein is. Voeg vanaf de eerste sprint een geautomatiseerde scanner toe aan CI en een toetsenbordrondgang aan je pull-requestchecklist, en leun op semantische HTML zodat je toetsenbord- en schermlezerondersteuning gratis krijgt. Sla overlays en zware tooling over. De opbrengst is dat wanneer het aanbestedingsteam van een klant midden in een verkoop om een conformiteitsrapport vraagt, je in dagen kunt antwoorden in plaats van te haasten.

**Kleinbedrijf.** Zonder toegankelijkheidsspecialist en met een krap budget koop je toegankelijkheid in plaats van haar te bouwen: kies een platform, thema of componentbibliotheek die al conform is en dat zegt, en geef de voorkeur aan leveranciers die een toegankelijkheidsverklaring publiceren. Dek de basis met hoge waarde zelf af met gratis tools, controles met alleen toetsenbord, een contrastcontrole en duidelijke labels bij elk veld, want die vangen de falen die klanten het vaakst uitsluiten. Behandel een verkeerde of onbruikbare geautomatiseerde stroom als verloren klant, aangezien een klein bedrijf zelden een begeleid kanaal biedt om op terug te vallen.

**Grote onderneming.** Op schaal is het werk toegankelijkheid een systeemeigenschap maken over veel teams. Lever toegankelijke componenten standaard in het designsysteem, poort regressies in CI en zet een eigenaar of expertisecentrum op met een herstelproces en training voor ontwerpers, engineers en contentschrijvers. Volg conformiteit in de tijd als statistiek, schrijf WCAG-conformiteit in inkoop en beheer componenten van derden als portfolio zodat één ingebedde widget niet stilletjes een gedeelde reis kan laten falen.

**Overheid.** Toegankelijkheid is een wettelijk mandaat en een burgerplicht, aangezien burgers met een beperking vaak geen alternatieve aanbieder hebben voor een uitkering, vergunning of stem. Bouw naar de standaard die je jurisdictie noemt (bijvoorbeeld Section 508, EN 301 549 of de Europese toegankelijkheidswet afgebeeld op WCAG 2.2 AA), publiceer een toegankelijkheidsverklaring met een route om barrières te melden en test met het publiek met een beperking dat je dient. Wijs overlays af als vervanging voor echte conformiteit en eis dat leveranciers geloofwaardig bewijs en een recht op herstel in het contract leveren.

## Voorbeelden

**Startup.** Een startup van drie personen die een wervingstool bouwde voegde vanaf de allereerste sprint een toegankelijkheidsscanner toe aan hun build en een snelle toetsenbordrondgang aan hun pull-requestchecklist, redenerend dat het goedkoper was toegankelijk te blijven dan het later te repareren. Toen het aanbestedingsteam van een middelgrote klant tijdens een verkoopcyclus om een toegankelijkheidsconformiteitsrapport vroeg, gebruikte de startup al semantische HTML, labelde elk veld en had overal zichtbare focus, dus antwoordde ze in dagen in plaats van te haasten. Die gereedheid won een deal die een concurrent op dezelfde eis verloor.

**Grote onderneming.** Een grote retailer stond tegenover een collectieve rechtszaak omdat blinde klanten de checkout niet met een schermlezer konden afronden. Naast de schikking en juridische kosten moest het bedrijf herstellen onder een door de rechtbank bewaakte tijdlijn. Daarna bouwde het toegankelijkheid opnieuw in zijn designsysteem en CI-pipeline in, voegde schermlezertests toe aan de definitie van klaar en trainde zijn teams. De herbouwde, toegankelijke checkout verbeterde ook de conversie en verminderde supportcontacten voor iedereen: de reparaties die schermlezergebruikers hielpen (duidelijke labels, foutmeldingen, logische volgorde) hielpen alle gebruikers.

**Overheid.** Een publieke uitkeringsinstantie was wettelijk verplicht aan WCAG 2.1 AA te voldoen voor haar online aanvraag. Vroeg testen met blinde en slechtziende gebruikers, gebruikers met alleen toetsenbord en gebruikers met cognitieve beperkingen onthulde dat een "verplicht veld"-indicator alleen met kleur, een ontoegankelijke datumkiezer en niet-aangekondigde validatiefouten mensen belemmerden af te ronden. Door dit te repareren, via semantische opmaak, zichtbare focus, foutaankondigingen via live regions en [duidelijke taal](https://en.wikipedia.org/wiki/Plain_language) in de hulp, liet burgers met een beperking voor het eerst zelfstandig aanvragen. Dat verminderde de afhankelijkheid van hulp ter plaatse en verlaagde de kosten per dienst, terwijl aan het wettelijk mandaat werd voldaan.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De zakelijke onderbouwing rust op marktbereik, juridisch risico, kosten per dienst en kwaliteit. Mensen met een beperking en hun gezinnen beheren aanzienlijke koopkracht. Hen uitsluiten verspeelt die. Toegankelijke diensten verminderen de behoefte aan dure begeleide kanalen (telefonische en persoonlijke hulp), een directe operationele besparing, vooral voor de overheid. En omdat toegankelijkheidsverbeteringen (duidelijke labels, toetsenbordondersteuning, leesbare content, robuuste opmaak) iedereen helpen, verhogen ze doorgaans de totale voltooiing en tevredenheid.

Qua TCO zijn de adoptiekosten training, tooling en toegankelijkheid inbouwen in componenten en pipelines, allemaal bescheiden wanneer je het vanaf het begin doet. De kosten van niet adopteren zijn ernstig en komen uit meerdere richtingen: juridische aansprakelijkheid (rechtszaken, schikkingen, door de rechtbank bevolen herstel, boetes van toezichthouders), de veel hogere kosten van achteraf aanpassen onder deadlinedruk, reputatieschade en de doorlopende kosten van buitengesloten gebruikers bedienen via duurdere kanalen. Achteraf aanpassen kost doorgaans meerdere malen wat erin ontwerpen had gekost.

Begin voor het bestuur met de wettelijke verplichting waar die geldt (niet-onderhandelbaar voor de overheid en steeds vaker voor de private sector). Kwantificeer dan de adresseerbare populatie die je uitsluit, de kosten van het begeleide kanaal van die uitsluiting en de "stoepranden"-winst voor alle gebruikers. Positioneer toegankelijkheid als risicobeheer plus kwaliteit, niet als liefdadigheid.

## Antipatronen en valkuilen

- **Toegankelijkheid als vinkje voor lancering**: een audit aan het eind in plaats van continue praktijk, wat duur last-minute herwerk garandeert.
- **"Div-soep"**: niet-semantische opmaak met klikhandlers op generieke elementen, onzichtbaar voor hulptechnologie.
- **ARIA-misbruik**: ARIA op kapotte opmaak vastschroeven, wat schermlezers meer misleidt dan gewone opmaak zou doen.
- **Informatie alleen met kleur**: status alleen met kleur getoond, onzichtbaar voor kleurenblinden.
- **Onzichtbare focus**: focusomlijningen verwijderen voor esthetiek, wat toetsenbordgebruikers laat stranden.
- **Toetsenbordvallen**: modals en widgets die focus vangen of verliezen.
- **Zelfgenoegzaamheid door geautomatiseerde scans**: een scanner halen en aannemen dat het product toegankelijk is.
- **Toegankelijkheidsoverlays**: "oplossing van één regel"-widgets van derden die geen echte conformiteit leveren en de ervaring kunnen verslechteren.
- **Gebruikers met een beperking uitsluiten van onderzoek**: ontwerpen voor een verbeelde gebruiker met een beperking in plaats van met echte te testen.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Geen toegankelijkheidspraktijk. Problemen worden alleen ontdekt wanneer een gebruiker klaagt of een rechtszaak komt, en respons is reactief. Opmaak is niet-semantisch en ongetest, en niemand bezit het probleem.

**Niveau 2: Ontwikkelen.** Bewustzijn bestaat en sommige teams handelen ernaar: hier een geautomatiseerde scanner in een build, daar een toetsenbordrondgang, een audit voor lancering vóór een grote release. De praktijk is basaal en inconsistent over teams, toegankelijkheid is nog steeds een checklist in de laatste fase en wordt onder schemadruk vaak gedeprioriteerd.

**Niveau 3: Standaardiseren.** WCAG 2.2 AA is de gedocumenteerde standaard, organisatiebreed afgedwongen. Toegankelijkheid is ingebouwd in het designsysteem zodat componenten standaard toegankelijk worden opgeleverd, automatisch en handmatig getest en opgenomen in de definitie van klaar. Teams zijn getraind, een eigenaar of expertisecentrum bestaat en een herstelproces is gedefinieerd.

**Niveau 4: Beheersen.** Toegankelijkheid wordt gemeten en beheerst met data tegen uitgangswaarden. De organisatie volgt conformiteitsstatistieken in de tijd (slaagpercentages van scanners, het aantal open barrières naar ernst, schermlezertestdekking van kritieke reizen en tijd tot herstel), rapporteert ze per team op een dashboard en behandelt regressies als buildfouten in plaats van adviserende waarschuwingen. Doelen worden gesteld tegen een uitgangswaarde en voortgang wordt beoordeeld, zodat een team dat achterop raakt zichtbaar is voordat een audit het vindt.

**Niveau 5: Orkestreren.** Toegankelijkheid wordt continu verbeterd en over de organisatie geïntegreerd. Mensen met een beperking maken regelmatig deel uit van onderzoek en testen, en toegankelijkheid is ingebed in inkoop, designtokens en CI. De organisatie past zich aan naarmate standaarden verschuiven (nieuwe WCAG-criteria overnemen en zich voorbereiden op WCAG 3.0) en beïnvloedt leveranciers en partners zodat de hele toeleveringsketen conform is.

## Ideeën voor discussie

- Hoe voorkom je dat toegankelijkheid wordt gedeprioriteerd wanneer deadlines strakker worden?
- Wat is de juiste mix van geautomatiseerd, handmatig en gebruikerstesten voor jouw risicoprofiel?
- Hoe moet toegankelijkheidsconformiteit in leverancierscontracten en inkoop worden geschreven?
- Hoe ga je om met het gat tussen WCAG-conformiteit en echte bruikbaarheid voor mensen met een beperking?
- Hoe moeten teams zich op WCAG 3.0 voorbereiden terwijl ze vandaag naar 2.2 bouwen?
- Hoe werf en vergoed je deelnemers met een beperking voor onderzoek eerlijk en respectvol?

## Belangrijkste inzichten

- Toegankelijkheid is een basiskwaliteitsattribuut en, voor de overheid, een wettelijke eis.
- Ontwerp naar WCAG 2.2 AA als vloer. Gebruik de POUR-principes als mentaal model.
- Eerst semantische HTML. ARIA alleen om echte gaten te vullen, correct gedaan.
- Geautomatiseerde tools vangen ongeveer een derde van de problemen. Handmatig testen en testen met hulptechnologie zijn essentieel.
- Test met mensen met een beperking, niet alleen voor hen.
- Toegankelijkheid inbouwen is goedkoop en duurzaam. Achteraf aanpassen is duur en kwetsbaar.
- Toegankelijk ontwerp is beter ontwerp voor iedereen: het stoepranden-effect is echt.

## Referenties en verder lezen

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
