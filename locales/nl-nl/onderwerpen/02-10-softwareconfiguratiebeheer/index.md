# 2.10 Softwareconfiguratiebeheer

## Overzicht en motivatie

[Softwareconfiguratiebeheer](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) is de discipline van de componenten van een softwaresysteem identificeren, beheersen hoe ze veranderen, de toestand van elke wijziging vastleggen en verifiëren dat wat je bouwde en leverde overeenkomt met wat je bedoelde. Het beantwoordt een vraag die eenvoudig klinkt maar op schaal moeilijk wordt: wat zit er precies in deze release, hoe kwam het daar en wie keurde het goed? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) behandelt SCM om een duidelijke reden als fundamenteel kennisgebied: elke andere engineeringactiviteit heeft een stabiele, bekende configuratie nodig om tegenaan te werken.

In een groot team is SCM het bindweefsel dat duizenden bewegende delen samenhangend houdt. Broncode, bibliotheken, containerimages, infrastructuurdefinities, configuratiedata, documentatie en testartefacten veranderen allemaal op hun eigen klok, en een opgeleverd systeem is één specifieke combinatie van specifieke versies van al die dingen. Zonder bewust configuratiebeheer is die combinatie onbekend en niet te reproduceren. Je kunt een eerdere release niet opnieuw maken, een defect niet herleiden naar de wijziging die het veroorzaakte en niet met vertrouwen zeggen wat er in productie draait.

Omgevingen van onderneming en overheid verhogen de inzet. Gereguleerde programma's en programma's van de publieke sector moeten aantonen dat wijzigingen zijn geautoriseerd, beoordeeld en vastgelegd, dat een opgeleverde build herleidbaar is naar goedgekeurde vereisten en broncode en dat niets ongecontroleerd het systeem binnenkwam. Hier is SCM net zozeer een bewijssysteem als een engineeringsysteem. [Versiebeheer](https://en.wikipedia.org/wiki/Version_control) (hoofdstuk 2.6) beheert de bronhistorie. SCM bestuurt de hele configuratie en het gecontroleerde proces waarmee ze verandert. Het is nauw verbonden met [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (hoofdstuk 8.2), leveringspipelines (hoofdstuk 8.1) en audit en zekerheid (hoofdstuk 10.2).

## Kernprincipes

- Alles wat systeemgedrag bepaalt is een [configuratie-item](https://en.wikipedia.org/wiki/Configuration_item) onder controle, niet alleen broncode.
- Een [baseline](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) is een bekend, afgesproken referentiepunt. Wijzigingen worden bewust tegen baselines gemaakt, niet achteloos.
- Verandering wordt gecontroleerd en vastgelegd, niet voorkomen. Het doel is geautoriseerde, traceerbare verandering.
- Statusadministratie betekent dat je altijd kunt antwoorden wat er in een configuratie zit en wat haar wijzigingsgeschiedenis is.
- Audits verifiëren dat het gebouwde en opgeleverde systeem overeenkomt met de vastgelegde configuratie en goedgekeurde vereisten.
- Reproduceerbaarheid is niet onderhandelbaar: elke uitgebrachte versie moet uit gecontroleerde invoer opnieuw te bouwen zijn.
- Automatiseer identificatie, vastlegging en verificatie. Handmatige boekhouding schaalt niet en overleeft geen audit.

## Aanbevelingen

### Definieer het SCM-proces en wijs eigenaarschap toe

Schrijf een SCM-plan op dat zegt wat onder configuratiebeheer valt, hoe items worden geïdentificeerd, hoe wijzigingen worden voorgesteld en goedgekeurd en hoe de status wordt vastgelegd en geaudit. Wijs duidelijk eigenaarschap toe, zoals een configuratiemanager of een verantwoordelijk team, zodat SCM niet van iedereen is en dus van niemand. Schaal het proces naar het risico: een klein intern hulpmiddel heeft lichte controle nodig, terwijl een veiligheidskritiek of gereguleerd systeem formele commissies en registers nodig heeft. Veranker het plan in een erkende standaard als IEEE 828, zodat auditors en partners het kunnen volgen.

### Identificeer configuratie-items en stel baselines vast

Maak een lijst van de configuratie-items die bepalen hoe het systeem zich gedraagt: broncode, afhankelijkheden, buildscripts, containerimages, infrastructuurdefinities, configuratiedata, schema's en sleuteldocumenten. Geef elk een stabiele identificatie en een versioneringsschema. Stel baselines vast op betekenisvolle punten (een uitgebrachte versie, een goedgekeurde set vereisten, een gecertificeerde build) zodat je een afgesproken referentie hebt om tegen te wijzigen en naar terug te keren. Een baseline is onveranderlijk: eenmaal verklaard bewerk je haar niet. Je vervangt haar alleen door een nieuwe baseline die via het wijzigingsproces is gemaakt.

### Beheers verandering via een gedefinieerd proces en passende commissies

Leid wijzigingen aan gecontroleerde items langs een gedefinieerd pad: voorstel, impactbeoordeling, goedkeuring, implementatie en verificatie. Gebruik voor items met hoger risico een [change control board](https://en.wikipedia.org/wiki/Change_control_board) (CCB) dat kosten, risico en planning weegt voordat het een wijziging autoriseert. Dimensioneer de commissie juist: een lichte geautomatiseerde poort voor routinematige codewijzigingen, en een formele multidisciplinaire CCB voor wijzigingen die baselines, interfaces of gereguleerd gedrag raken. Leg elke beslissing en de redenering erachter vast, en verbind belangrijke configuratiebeslissingen aan besluitenlogboeken (hoofdstuk 1.6) zodat de redenering behouden blijft.

### Onderhoud configuratiestatusadministratie

Houd een nauwkeurig, bevraagbaar register bij van elk configuratie-item: zijn huidige versie, bij welke baseline het hoort en de wijzigingsverzoeken die erop zijn toegepast. Deze statusadministratie laat je op elk moment antwoorden wat een release bevat en hoe ze daar kwam. Genereer het register automatisch uit je systemen van registratie (versiebeheer, pipeline, artefactregister) in plaats van een parallel spreadsheet bij te houden dat van de werkelijkheid afdrijft. Dit register is de ruggengraat van traceerbaarheid van vereiste naar wijziging naar build naar deployment.

### Voer configuratie-audits uit

Verifieer twee dingen volgens een vast schema. Een functionele configuratie-audit bevestigt dat de configuratie presteert zoals haar vereisten specificeren. Een fysieke configuratie-audit bevestigt dat de opgeleverde artefacten overeenkomen met de vastgelegde configuratie: dat de build kwam uit de vastgelegde broncode en afhankelijkheden en niets onverantwoords bevat. Automatiseer zoveel mogelijk: [reproduceerbare builds](https://en.wikipedia.org/wiki/Reproducible_builds), artefactchecksums, software bills of materials (SBOM's) en herkomstverklaringen veranderen auditen van een handmatige inspectie in een continue controle.

### Beheer releases en oplevering als gecontroleerde gebeurtenissen

Behandel een release als een specifieke, geïdentificeerde baseline die via een herhaalbaar proces wordt opgeleverd. Versioneer je releases expliciet, produceer een manifest of bill of materials dat precies beschrijft wat erin zit en leg de afbeelding van release naar broncoderevisie naar gedeployd artefact vast. Onderteken en checksum uitgebrachte artefacten, zodat iedereen stroomafwaarts hun integriteit kan verifiëren. Verbind releasebeheer met de leveringspipeline (hoofdstuk 8.1), zodat promotie door omgevingen zelf gecontroleerd, vastgelegd en omkeerbaar is.

### Kies en integreer SCM-tooling

Leun op tools die identificatie, beheersing, administratie en audit automatiseren in plaats van alleen op discipline: versiebeheer voor broncode, artefact- en imageregisters voor binaries, een onveranderlijke pipeline voor builds, infrastructure as code voor omgevingen en afhankelijkheids- en SBOM-tooling voor herkomst. Verbind ze zodat één wijziging traceerbaar van commit naar gedeployde release stroomt. Je wilt een toolchain waarin het configuratieregister een bijproduct is van het werk doen, geen aparte administratieve klus.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen |
|---|---|---|
| Formele change control boards | Sterke autorisatie en auditspoor. Risico gewogen vóór verandering | Lagere doorvoer. Overhead bij toepassing op routinewijzigingen |
| Lichte geautomatiseerde poorten | Snelle flow. Lage overhead. Schaalt naar veel wijzigingen | Zwakker voor baselines met hoog risico. Minder overleg |
| Strikt onveranderlijke baselines | Reproduceerbare, controleerbare referentiepunten | Discipline en tooling nodig. Wrijving bij overmatig gebruik |
| Geautomatiseerde statusadministratie | Nauwkeurig, altijd actueel register. Auditklaar | Investering vooraf in tooling en integratie |
| Handmatige configuratieregisters | Eenvoudig te starten. Geen tooling nodig | Drijft van de werkelijkheid af. Faalt op schaal en onder audit |

De centrale afweging is beheersing tegenover flow. Zware wijzigingsbeheersing geeft sterke zekerheid maar vertraagt de oplevering. Lichte beheersing stroomt snel maar verzwakt traceerbaarheid. Het antwoord is niet er globaal één te kiezen. Het is beheersing te laten afstemmen op risico: automatiseer routinewijzigingen via snelle poorten en bewaar formele commissies en onveranderlijke baselines voor de items waar autorisatie en controleerbaarheid er werkelijk toe doen. De tweede afweging is investering vooraf in tooling tegenover doorlopende administratieve kosten en auditrisico. Geautomatiseerde administratie kost meer om op te zetten en veel minder om mee te leven.

## Vragen om met je team te bespreken

1. **Wat hoort er precies op onze lijst van configuratie-items, en wie beslist wanneer er iets nieuws verschijnt?** SCM werkt alleen als de lijst met gecontroleerde items overeenkomt met de dingen die gedrag werkelijk bepalen, en in een groot systeem is die set groter dan de meeste teams denken: broncode, afhankelijkheden, buildscripts, containerimages, infrastructuurdefinities, schema's, functievlaggen en de configuratiedata die stilletjes verandert wat de software doet. Als niemand de lijst bezit, veroudert ze, en het item dat je in productie neerhaalde blijkt het ene ding dat niemand dacht te beheersen. Neem je huidige inventaris mee naar de vergadering en jaag op gedragsbepalende items die ontbreken. Wijs een verantwoordelijke eigenaar aan (een configuratiemanager of een benoemd team) zodat het toevoegen van een nieuw item een bewuste beslissing is en geen toeval, want SCM die van iedereen is, is van niemand.

2. **Kunnen we bewijzen dat een gedeployd artefact kwam uit de broncode en pipeline waarvan we denken dat het kwam, en zou dat bewijs sabotage overleven?** Reproduceerbaarheid en traceerbaarheid zijn de kern van SCM, en de scherpe versie van de vraag is of je de draaiende binary met bewijs, niet met bewering, kunt koppelen aan een specifieke commit en buildrun. In een gereguleerd of waardevol systeem is dit ook je verdediging van de toeleveringsketen: ondertekende herkomstverklaringen, artefactchecksums en een software bill of materials veranderen "we zijn er vrij zeker van" in iets wat een auditor of incidentresponder kan verifiëren. Neem je laatste release mee en probeer haar achterwaarts te doorlopen van het gedeployde artefact naar de goedgekeurde wijziging. Als een schakel een handmatige bewering is in plaats van een vastgelegde, verifieerbare koppeling, is dat waar een aanvaller of een eerlijke fout ongemerkt iets kan binnensmokkelen, en het sluiten ervan betekent ondertekening en herkomst in de pipeline koppelen zodat het register een bijproduct van oplevering is.

3. **Kan vandaag iemand een release ter plekke bewerken, en wat zou dat doen met ons vermogen haar te vertrouwen?** Een baseline is alleen nuttig als ze onveranderlijk is: zodra "de release" achteraf kan worden bewerkt, kun je haar niet meer reproduceren of als referentie gebruiken, en wordt elke stroomafwaartse audit archeologie. De klassieke fout is configuratie direct in productie bewerkt of een tag stilletjes verplaatst, precies de snelkoppeling die onschuldig voelt en een release later onmogelijk te reconstrueren maakt. Neem het eerlijke antwoord mee naar de vergadering: wie heeft toegang om een gedeployde baseline te wijzigen zonder via het wijzigingsproces te gaan, en is het gebeurd? De oplossing is baselines werkelijk onveranderlijk te maken en elke wijziging langs voorstel, impactbeoordeling, goedkeuring en verificatie te leiden, de rigueur gelaagd zodat routinewijzigingen door snelle geautomatiseerde poorten stromen terwijl baseline- en gereguleerde wijzigingen naar een commissie gaan.

4. **Wordt onze configuratiestatusadministratie automatisch gegenereerd uit onze systemen van registratie of met de hand bijgehouden, en hoever is ze afgedreven van wat er werkelijk is gedeployd?** Statusadministratie is het register waarmee je op elk moment kunt antwoorden wat een release bevat en hoe ze daar kwam, en in een groot systeem is dat register alleen betrouwbaar als het uit het werk valt in plaats van in een parallel spreadsheet te worden getypt. De concurrerende trek is dat een met de hand bijgehouden register goedkoop om te starten en flexibel voelt, terwijl automatiseren betekent versiebeheer, de pipeline en het artefactregister te integreren zodat het register een bijproduct van oplevering wordt. Neem het register mee waarop je nu leunt, kies willekeurig drie recente releases en controleer of de vastgelegde versies, baselines en toegepaste wijzigingsverzoeken overeenkomen met wat de tooling zegt dat er is opgeleverd. Voor een programma van onderneming of overheid is een statusregister dat van de werkelijkheid afwijkt geen kwestie van netheid maar een auditbevinding die op de loer ligt, want een auditor die één gat vindt stopt het hele verhaal te vertrouwen en vraagt je het met de hand te reconstrueren.

5. **Is onze wijzigingsbeheersing gelaagd naar risico, of beheerst dezelfde ceremonie elke wijziging ongeacht wat ze raakt?** Beheersing en flow trekken tegen elkaar: een formeel change control board weegt kosten, risico en planning voordat het een wijziging autoriseert, maar die ceremonie op een routinematige codeaanpassing toepassen voegt alleen vertraging toe, terwijl een gedeelde baseline of een gereguleerde betalingsstroom door een snelle geautomatiseerde poort duwen het overleg wegneemt precies waar je het nodig hebt. De faalwijzen zijn symmetrisch: uniforme zwaarte waar mensen omheen leren routeren, of uniforme laksheid die een wijziging met hoog risico ongezien laat passeren. Neem een steekproef van de wijzigingen van vorig kwartaal mee, gesorteerd op wat elk raakte, en controleer of de rigueur die het kreeg werkelijk bij het risico paste. Noem in een gereguleerde of publieke setting welke itemklassen een multidisciplinaire commissie moeten bereiken en welke door geautomatiseerde poorten mogen stromen, en leg die gelaagdheid expliciet vast, want "we gebruiken oordeel" is geen beheersmaatregel die een auditor of toezichthoudend orgaan kan verifiëren.

6. **Wanneer voerden we voor het laatst een functionele en een fysieke configuratie-audit uit, en hoeveel van het bewijs zou een levend register zijn in plaats van een reconstructie?** Een functionele configuratie-audit bevestigt dat het systeem presteert zoals haar vereisten specificeren, en een fysieke configuratie-audit bevestigt dat de opgeleverde artefacten overeenkomen met de vastgelegde configuratie en niets onverantwoords bevatten. Sla ze over en je vertrouwt erop dat je baselines en statusadministratie eerlijk zijn zonder ooit te controleren. De spanning is kosten: handmatige audits zijn traag en pijnlijk, precies waarom teams ze uitstellen, en de uitweg is de controles te automatiseren met reproduceerbare builds, artefactchecksums, software bills of materials en herkomstverklaringen zodat verificatie continu wordt. Neem je meest recente release mee en probeer ter plekke het spoor van vereiste naar wijziging naar build naar deployment en het bewijs van artefact naar broncode te produceren. Voor programma's van onderneming en overheid is dit bewijsspoor wat certificering en toezicht eisen, dus de eerlijke vraag is of de audit van morgen zou worden beantwoord uit registers die je al hebt of uit een archeologieoefening die je je niet kunt veroorloven.

## Sectorperspectief

**Startup.** Houd SCM licht maar echt. Zet broncode, infrastructuurdefinities en configuratiedata in versiebeheer, en maak van elke release een getagde build uit één pipeline in plaats van een met de hand samengesteld artefact. Sla change control boards en formele baselines over, die op jouw omvang overdreven zijn, maar laat nooit iemand configuratie direct in productie bewerken, want die ene snelkoppeling maakt een release onmogelijk te reproduceren wanneer een klant volgende dinsdag een bug raakt.

**Kleinbedrijf.** Zonder configuratiemanager en met een krap budget leun je op tools die je SCM bijna gratis geven: een gehost versiebeheerplatform, zijn ingebouwde pipeline en een artefactregister, zodat het configuratieregister een bijproduct is in plaats van een baan die je moet bemannen. Koop dit vermogen ingebed in tools die je al betaalt in plaats van een maatwerkproces te bouwen. Besteed je schaarse aandacht aan de twee gewoonten die het meest tellen: reproduceerbare getagde releases en gedragsveranderende configuratie weghouden van handmatige productiebewerkingen.

**Grote onderneming.** Het probleem is consistentie over veel teams: een gedeeld SCM-plan, een gemeenschappelijke taxonomie van configuratie-items, gelaagde wijzigingsbeheersing en statusadministratie automatisch gegenereerd uit versiebeheer, het artefactregister en de pipeline. Bewaar formele change control boards en onveranderlijke baselines voor gedeelde platform- en gereguleerde stromen, laat routinewijzigingen door geautomatiseerde poorten stromen en standaardiseer ondertekende herkomst en SBOM's zodat de release van elk team kan worden herleid en elke auditor een levend register kan bevragen in plaats van een reconstructie te bestellen.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven het proces vorm. Volg een formeel SCM-plan afgestemd op een erkende standaard als IEEE 828, baseline configuratie-items bij contractuele mijlpalen en leid elke wijziging van een gecontroleerde baseline langs een commissie die impact, besluit en motivering vastlegt. Eis dat opgeleverde artefacten reproduceerbaar zijn uit gecontroleerde invoer, van checksums voorzien en van begin tot eind herleidbaar van goedgekeurde vereiste tot opgeleverde build, want dat gedocumenteerde bewijsspoor is precies wat certificering, audit en publiek toezicht eisen.

## Voorbeelden

**Startup.** Een startup van zes personen houdt zijn SCM licht maar echt: broncode, infrastructuurdefinities en configuratiedata leven allemaal in versiebeheer, en elke release is een getagde, geversioneerde build uit dezelfde pipeline in plaats van met de hand samengesteld. Wanneer een klant een bug meldt die vorige dinsdag verscheen, herleiden ze het gedeployde artefact in minuten naar de exacte commit in plaats van te gokken. Ze slaan change control boards en formele baselines over, die op hun omvang overdreven zouden zijn, maar weigeren iemand configuratie direct in productie te laten bewerken, want die ene snelkoppeling maakt een release later onmogelijk te reproduceren.

**Grote onderneming.** Een groot financieel dienstverlener plaatst alle deployable artefacten, infrastructuurdefinities en configuratiedata onder configuratiebeheer. Elke release is een onveranderlijke, geversioneerde baseline met een gegenereerde software bill of materials, en elk gedeployd artefact draagt een ondertekende herkomstverklaring die het koppelt aan een specifieke broncoderevisie en pipelinerun. Routinematige applicatiewijzigingen stromen door geautomatiseerde pipelinepoorten, terwijl wijzigingen aan gedeelde platformbaselines of gereguleerde betalingsstromen naar een change control board gaan. Statusadministratie wordt automatisch gegenereerd uit versiebeheer, het artefactregister en de pipeline, zodat auditors een levend register bevragen in plaats van om een reconstructie te vragen.

**Overheid.** Een defensieprogramma volgt een formeel SCM-plan afgestemd op IEEE 828. Configuratie-items worden bij contractuele mijlpalen opgesomd en gebaselined, en een change control board autoriseert elke wijziging van een gecontroleerde baseline, met vastlegging van impact, besluit en motivering. Functionele configuratie-audits bevestigen dat het opgeleverde systeem aan de gespecificeerde vereisten voldoet, en fysieke configuratie-audits bevestigen dat opgeleverde artefacten exact overeenkomen met de vastgelegde configuratie. Releases zijn reproduceerbaar uit gecontroleerde invoer, van checksums voorzien en van begin tot eind herleidbaar, van goedgekeurde vereiste via wijzigingsverzoek tot opgeleverde build, precies het bewijsspoor dat certificering en toezicht eisen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

SCM bestaat om risico en kosten over de levensduur van een systeem te beheersen. Het rendement komt uit reproduceerbaarheid en traceerbaarheid: je kunt elke release opnieuw maken, defecten herleiden naar de wijzigingen die ze veroorzaakten en auditvragen beantwoorden uit registers in plaats van archeologie. Dat verkort de tijd om incidenten te diagnosticeren, verlaagt de kosten en duur van audits en voorkomt de dure klasse van falen waarbij niemand kan zeggen wat er draait of hoe het opnieuw te bouwen.

De total cost of ownership pleit voor automatisering. Handmatige configuratieregisters zijn goedkoop om te starten en steeds duurder om te onderhouden, en ze falen precies wanneer je ze het meest nodig hebt, tijdens een incident of een audit, omdat ze van de werkelijkheid zijn afgedreven. Geautomatiseerde identificatie, administratie en audit kosten vooraf meer maar maken van het configuratieregister een bijna gratis bijproduct van de leveringspipeline. Formuleer SCM voor het bestuur als de beheersmaatregel die releases reproduceerbaar en wijzigingen controleerbaar maakt, en weeg haar af tegen de kosten van niet-reproduceerbare releases, langdurige audits en het compliancerisico van ongecontroleerde verandering.

## Antipatronen en valkuilen

- **Configuratie door tribale kennis:** de ware inhoud van een release leeft alleen in het hoofd van een engineer, niet in een register.
- **Veranderlijke baselines:** "de release" wordt ter plekke bewerkt, zodat ze niet langer kan worden gereproduceerd of als referentie vertrouwd.
- **Ongecontroleerde configuratiedata:** code staat onder versiebeheer maar de configuratie die haar gedrag verandert wordt ad hoc in productie bewerkt.
- **Wijzigingsbeheersingstheater:** een commissie die alles afstempelt, wat vertraging toevoegt zonder echte toetsing.
- **Handmatige statusadministratie:** een spreadsheet van versies die stilletjes afwijkt van wat werkelijk is gedeployd.
- **Niet-reproduceerbare builds:** releases die niet uit gecontroleerde invoer opnieuw te bouwen zijn, zodat audits en herbouw gokwerk worden.
- **Niet-traceerbare releases:** geen afbeelding van gedeployd artefact terug naar broncoderevisie, wijzigingsverzoek en goedkeuring.

## Volwassenheidsmodel

- **Niveau 1 (Initiëren):** SCM is ad hoc en reactief. Alleen broncode is gecontroleerd. Releases worden met de hand samengesteld. Er zijn geen baselines, geen betrouwbaar register van wat is gedeployd en geen manier om een eerdere build te reproduceren.
- **Niveau 2 (Ontwikkelen):** Basispraktijken bestaan maar verschillen per team. Sommige systemen definiëren configuratie-items en een wijzigingsproces en versioneren hun releases, baselines bestaan hier en daar, maar registers zijn deels handmatig en de rigueur van beheersing is inconsistent over de organisatie.
- **Niveau 3 (Standaardiseren):** Praktijken zijn gedocumenteerd en organisatiebreed gehandhaafd. Een gemeenschappelijke taxonomie van configuratie-items, onveranderlijke baselines, gelaagde wijzigingsbeheersing en statusadministratie zijn vastgesteld en grotendeels geautomatiseerd. Releases zijn reproduceerbaar en traceerbaar, en audits worden ondersteund door tooling in plaats van door geheugen.
- **Niveau 4 (Beheersen):** SCM wordt gemeten en gestuurd met data. Reproduceerbaarheidspercentage, traceerbaarheidsdekking van vereiste tot gedeployd artefact, doorlooptijd van wijzigingen door elke beheersingslaag, incidenten van configuratiedrift en auditbevindingen worden gevolgd aan de hand van uitgangswaarden en doelen. Afwijkingen leiden tot correctie, en elke go/no-go-beslissing rust op dit bewijs in plaats van op bewering.
- **Niveau 5 (Orkestreren):** SCM wordt continu verbeterd en is over de organisatie geïntegreerd. Volledig geautomatiseerd en continu geverifieerd met reproduceerbare builds, SBOM's, herkomstverklaringen en levende statusadministratie, is het proces verweven met oplevering, beveiliging en audit, en past het zich aan naarmate risico en leveringsresultaten verschuiven, waarbij beheersmaatregelen op bewijs worden afgebouwd en herschikt.

## Ideeën voor discussie

- Kun je je laatste release vandaag exact reproduceren uit gecontroleerde invoer, en hoe lang zou dat duren?
- Welke configuratie-items bepalen gedrag maar staan niet werkelijk onder controle, vooral configuratiedata en infrastructuur?
- Is je wijzigingsbeheersing gelaagd naar risico, of voegt ze overal uniforme overhead of uniforme laksheid toe?
- Waar leeft je configuratieregister, en hoever is het afgedreven van wat werkelijk is gedeployd?
- Welk bewijs kun je morgen in een audit produceren, en hoeveel daarvan zou reconstructie zijn in plaats van register?
- Hoe veranderen reproduceerbare builds, SBOM's en herkomst wat je audits automatisch kunnen verifiëren?

## Belangrijkste inzichten

- SCM beheerst de hele configuratie (code, afhankelijkheden, infrastructuur en configuratiedata), niet alleen broncode.
- Baselines zijn onveranderlijke referentiepunten. Verandering wordt tegen hen geautoriseerd en vastgelegd, niet voorkomen.
- Statusadministratie moet je op elk moment laten antwoorden wat een release bevat en hoe ze daar kwam.
- Audits verifiëren dat wat is gebouwd en opgeleverd overeenkomt met de vastgelegde configuratie en goedgekeurde vereisten.
- Laag de beheersing naar risico en automatiseer identificatie, administratie en audit zodat het register een bijproduct van oplevering is.

## Referenties en verder lezen

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
