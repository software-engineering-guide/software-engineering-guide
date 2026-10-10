# 4.4 Beveiligingsoperaties

## Overzicht en motivatie

Preventie is nodig, maar nooit genoeg. Vastberaden tegenstanders, nieuwe kwetsbaarheden en gewone menselijke fouten betekenen dat sommige dreigingen langs je verdedigingen glippen. Beveiligingsoperaties is de discipline om ze snel te vinden, goed te reageren en te voeden wat je leert terug in sterkere verdedigingen. Het is het verschil tussen een incident dat in minuten wordt beperkt en een dat maandenlang etterde voordat iemand het merkte.

In een grote organisatie moeten beveiligingsoperaties op schaal en snelheid werken. Duizenden services genereren oceanen aan logs. Elke week worden honderden nieuwe kwetsbaarheden bekendgemaakt. Deployment houdt nooit op. Handmatige, ambachtelijke operaties kunnen simpelweg niet bijhouden. Het antwoord is beveiliging in de leveringspipeline in te bedden ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), detectie en respons te automatiseren en de spieren op te bouwen om incidenten kalm af te handelen wanneer ze toeslaan. Voor de overheid dragen beveiligingsoperaties ook wettelijke verplichtingen: voorgeschreven termijnen voor incidentmelding, gecoördineerde bekendmaking van kwetsbaarheden en forensische rigueur die juridische toetsing kan weerstaan.

Dit hoofdstuk behandelt beveiliging in de pipeline integreren, kwetsbaarheden beheren en patchen, op incidenten reageren en forensisch onderzoek doen, detectie draaien via [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) en SOAR, en verdedigingen valideren door red en purple teaming en [penetratietesten](https://en.wikipedia.org/wiki/Penetration_test).

## Kernprincipes

- **Automatiseer het routinematige.** Machines handelen scannen, correleren en repetitieve respons af zodat mensen zich op oordeel richten.
- **Schuif beveiliging in de pipeline.** Testen en poorten leven in [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (continuous integration en continuous delivery), wat snelle feedback geeft waar engineers al werken.
- **Neem inbreuk aan en bereid je voor.** Oefen incidentrespons voordat je haar nodig hebt. Het incident is niet het moment om te improviseren.
- **Meet en verkort tijd.** Gemiddelde tijd tot detectie en gemiddelde tijd tot respons zijn de statistieken die het meest tellen.
- **Schuldvrij leren.** Elk incident en bijna-ongeluk wordt een les die het systeem verhardt, geen zoektocht naar iemand om te straffen.
- **Valideer verdedigingen vijandig.** Test je beveiliging zoals echte aanvallers zouden doen en repareer dan wat ze vinden.
- **Detectie-engineering is een product.** Behandel detecties als code: onder versiebeheer, getest en continu verbeterd.

## Aanbevelingen

### Bouw DevSecOps in de pipeline

Integreer geautomatiseerd beveiligingstesten direct in continuous integration en delivery zodat feedback engineers binnen minuten bereikt:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Static Application Security Testing) analyseert broncode op kwetsbare patronen terwijl ze wordt gecommit.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dynamic Application Security Testing) tast de draaiende applicatie af op uitbuitbare fouten.
- **SCA** (Software Composition Analysis) markeert bekend kwetsbare afhankelijkheden.
- **IaC-scanning** controleert infrastructure as code op onveilige configuraties voordat ze deployen.
- **Geheimenscanning** blokkeert dat inloggegevens de repository binnenkomen.

Stem deze tools meedogenloos af om valse positieven te beheersen. Een scanner die wolf roept wordt genegeerd. Stel risicogebaseerde poorten in: blokkeer op bevindingen met hoge ernst en hoge zekerheid en volg de rest zonder oplevering stil te leggen. Je wilt een snel, vertrouwd signaal, geen muur van ruis.

### Beheer kwetsbaarheden en patch systematisch

Een gestage stroom kwetsbaarheden vraagt om een systematisch, geprioriteerd proces, geen verse paniek bij elke kop.

- Houd een nauwkeurige bezittingeninventaris bij zodat je weet wat door een gegeven kwetsbaarheid kan worden getroffen.
- Prioriteer herstel naar echt risico: combineer ernst, uitbuitbaarheid (wordt het in het wild uitgebuit?), blootstelling en kritiek van het bezit in plaats van op de ruwe score alleen te patchen.
- Definieer en dwing **herstel-SLA's** (service-level agreements) af per ernstlaag en meet naleving.
- Automatiseer patchen waar je het veilig kunt, vooral voor infrastructuur en afhankelijkheden.
- Draai een programma voor **gecoördineerde bekendmaking van kwetsbaarheden** met een duidelijk meldkanaal en, waar passend, een [bugbounty](https://en.wikipedia.org/wiki/Bug_bounty_program), zodat externe onderzoekers fouten verantwoord kunnen melden in plaats van ze publiek te dumpen.

### Bereid je voor op en voer incidentrespons uit

Wanneer een incident toeslaat, is een geoefend proces meer waard dan welke tool ook.

- Houd een **incidentresponsplan** bij met gedefinieerde rollen (incidentcommandant, communicatieleider, onderzoekers), ernstclassificaties en escalatiepaden.
- Stel heldere fasen vast: **voorbereiding, detectie en analyse, beperking, uitroeiing, herstel en review na het incident.**
- Bewaar bewijs goed voor **[forensisch onderzoek](https://en.wikipedia.org/wiki/Digital_forensics)**: leg logs, geheugen en schijfimages vast met een gedocumenteerde bewakingsketen zodat bevindingen juridisch standhouden en de analyse deugdelijk is.
- Plan **inbreukcommunicatie** vooraf: wie klanten, toezichthouders en het publiek informeert, op welke termijn, met betrokkenheid van juristen en communicatie. Klokken van toezichthouders (vaak 72 uur of minder) beginnen te tikken bij ontdekking.
- Houd regelmatig **tabletopoefeningen** zodat het team het plan kent voor een echte crisis, en voer schuldvrije reviews na incidenten uit die concrete verbeteringen opleveren.

### Draai detectie met SIEM en SOAR en engineer detecties

Breng je beveiligingssignalen samen en handel er op schaal naar.

- Gebruik een **SIEM** (Security Information and Event Management) om logs en gebeurtenissen uit het hele landschap te aggregeren en te correleren, verdachte patronen naar boven brengend.
- Gebruik **SOAR** (Security Orchestration, Automation, and Response) om triage en responsdraaiboeken te automatiseren: alarmen verrijken, hosts isoleren, inloggegevens uitschakelen en zaken openen zonder op een mens te wachten voor routinestappen.
- Oefen **detectie-engineering**: behandel detectieregels als geversioneerde, geteste code afgestemd op een raamwerk als [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), meet hun percentages ware en valse positieven en verbeter continu de dekking van echte tegenstandertechnieken.
- Zorg voor uitgebreide, sabotagebestendige logging over applicaties en infrastructuur. Je kunt niet detecteren wat je niet logt.

### Valideer verdedigingen met red en purple teaming en pentesten

Je verdedigingen testen zoals een aanvaller het zou doen is de enige manier om te weten dat ze werkelijk werken.

- **Penetratietesten** bieden gerichte beoordeling op een moment van specifieke systemen, vaak voor compliance.
- **[Red teaming](https://en.wikipedia.org/wiki/Red_team)** simuleert een realistische tegenstander die doelen nastreeft over je omgeving, en test detectie en respons evenals preventie.
- **Purple teaming** brengt aanvallers (rood) en verdedigers (blauw) samenwerkend bijeen zodat elke gesimuleerde aanval onmiddellijk detecties en maatregelen verbetert, een oefening omzettend in blijvend vermogen.
- Voed alle bevindingen terug in detectie-engineering, herstel en training.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Blokkerende pipelinepoorten | Stopt bekende problemen om op te leveren | Wrijving, valse positieven frustreren teams |
| Niet-blokkerend scannen | Weinig wrijving, snelle oplevering | Problemen kunnen worden opgeleverd. Vraagt discipline om te repareren |
| Eigen SOC | Diepe context, volledige controle | Duur, moeilijk 24/7 te bemannen |
| Beheerde detectie/respons | 24/7 dekking, expertise op afroep | Minder context, leveranciersafhankelijkheid |
| Geautomatiseerd patchen | Snel, sluit vensters snel | Risico van brekende wijzigingen |
| Frequent red teaming | Realistische validatie, vindt echte gaten | Kostbaar, middelenintensief |
| Bugbountyprogramma | Crowdsourced ontdekking, goede dekking | Triagelast, uitbetalingskosten, ruis |

De kernspanning is snelheid tegenover zekerheid, en dekking tegenover kosten. Blokkerende poorten en geautomatiseerd patchen maximaliseren zekerheid maar voegen wrijving en risico toe. Niet-blokkerende aanpakken bewegen sneller maar hangen af van opvolging. Detectie rond de klok is op schaal essentieel maar duur om in huis te bouwen, wat veel organisaties naar hybride modellen duwt. Het duurzame pad automatiseert het routinematige met hoge zekerheid, bewaart menselijke aandacht voor echt oordeel en blijft de balans afstemmen met gemeten uitkomsten in plaats van angst.

## Vragen om met je team te bespreken

1. **Wat zijn je herstel-SLA's per ernst, en wat dwingt ze werkelijk af?** Een gestage stroom kwetsbaarheden vraagt om een systematisch, geprioriteerd proces, geen verse paniek bij elke kop, en SLA's per ernstlaag zijn hoe je bijblijft. Besluit je klokken (bijvoorbeeld kritiek in dagen, hoog in weken) en, net zo belangrijk, hoe je naleving meet en wie verantwoordelijk is wanneer een deadline schuift. Prioriteer naar echt risico, ernst combinerend met uitbuitbaarheid in het wild, blootstelling en kritiek van het bezit, in plaats van alleen op ruwe CVSS-score te patchen. Neem je huidige achterstand aan open bevindingen mee gesorteerd op leeftijd en ernst, want niet-gepatchte kritieke bevindingen die voorbij hun venster zitten zijn het bewijs dat telt. Als de SLA geen handhaving en geen eigenaar heeft, is ze een wens, en scannen zonder herstel bouwt alleen auditschuld en een vals gevoel van veiligheid.

2. **Wanneer een incident om 2 uur 's nachts toeslaat, wie is de incidentcommandant en hoe snel begint de klok van de toezichthouder te lopen?** Een geoefend proces is meer waard dan welke tool ook, dus je hebt benoemde rollen nodig (incidentcommandant, communicatieleider, onderzoekers), gedefinieerde ernstniveaus en escalatiepaden opgeschreven voor de crisis. Klokken van toezichthouders lopen vaak 72 uur of minder en beginnen bij ontdekking, dus besluit vooraf wie klanten, toezichthouders en het publiek informeert en bevestig dat juristen en communicatie in de lus zitten. Forensisch bewijs bewaren met een gedocumenteerde bewakingsketen moet gebeuren voordat iemand een gecompromitteerde host herbouwt, of je verliest het vermogen te begrijpen of te bewijzen wat er gebeurde. Neem de datum van je laatste tabletopoefening mee, want als die lang geleden was of nooit, is je plan niet getest. Voor overheidsteams maken wettelijke meldingsdeadlines dit niet optioneel, dus oefen het meldingspad, niet alleen de technische respons.

3. **Welke routinematige responsacties laat je SOAR zonder mens in de lus nemen?** Automatisering is krachtvermenigvuldiging die een klein team een groot landschap laat dekken, en de statistiek die telt is gemiddelde tijd tot respons, die geautomatiseerde draaiboeken van uren naar minuten kunnen terugbrengen. Besluit welke acties met hoge zekerheid (een host isoleren, een inloggegeven intrekken, een zaak openen) je vertrouwt automatisch te draaien, en welke eerst menselijk oordeel nodig hebben. Het risico is een valse positief die een ontwrichtende actie triggert, dus koppel automatisering aan detectiekwaliteit en stem meedogenloos af, want een systeem dat wolf roept wordt uitgezet. Neem je huidige alarmvolume en percentage valse positieven mee, want die getallen vertellen welke draaiboeken vandaag veilig te automatiseren zijn. Als elke responsstap op een mens wacht, hou je het op schaal niet bij, en blijft verblijftijd, die inbreukkosten drijft, hoog.

4. **Welke pipelinebevindingen blokkeren een release, welke worden alleen gevolgd, en wie houdt het percentage valse positieven laag genoeg dat engineers de poort nog vertrouwen?** Een scanner die wolf roept wordt genegeerd, en zodra engineers het geloof in een poort verliezen, lobbyen ze om haar te verwijderen, dus de waarde van DevSecOps rust op signaalkwaliteit in plaats van ruwe dekking. De spanning is echt: blokkeer op te weinig en kwetsbare code wordt opgeleverd, blokkeer op te veel en je voegt wrijving toe, vertraagt oplevering en verbrandt goodwill. Neem de percentages ware en valse positieven voor elke scanner mee (SAST, DAST, SCA, IaC en geheimenscanning), hoe vaak teams een poort overschrijven of onderdrukken en de leeftijd van de bevindingen die je alleen volgt zonder te repareren. Stel voor een onderneming of overheidsorgaan dat honderden pipelines draait het beleid van blokkeren-versus-volgen centraal vast en stem het af met data, want poorten die willekeurig van team tot team verschillen creëren zowel auditgaten als het gevoel dat beveiliging grillig is.

5. **Hoe zeker ben je dat je detecties nog de technieken dekken die een echte aanvaller zou gebruiken, en wie bezit ze als geteste, geversioneerde code?** Detecties verslechteren stilletjes naarmate je omgeving en je tegenstanders evolueren, dus een regelset die vorig jaar volledig leek kan dekking verliezen lang voordat een incident het gat uiteindelijk onthult. Detecties als code behandelen, onder versiebeheer, getest en afgebeeld op een raamwerk als MITRE ATT&CK, is wat een engineeringpraktijk scheidt van een stapel verouderde alarmen, en toch strijdt ze om dezelfde schaarse analistentijd als live triage. Neem je huidige ATT&CK-dekkingskaart mee, het gemeten percentage ware en valse positieven van je belangrijkste detecties en de resultaten van je laatste purple-teamoefening, aangezien samenwerkend rood-en-blauw testen de snelste manier is om te bewijzen welke detecties werkelijk afgaan. Koppel in omgevingen van onderneming en overheid waar een raamwerk kan worden voorgeschreven elke detectie aan een benoemde eigenaar en een reviewritme, want dekking die niemand onderhoudt is dekking waarvan je pas na de inbreuk ontdekt dat je haar verloor.

6. **Bouw je detectie en respons in huis, koop je beheerde detectie en respons, of meng je beide, en heb je geprijsd wat echte dekking rond de klok kost?** Verblijftijd drijft inbreukkosten, dus de niet-gedekte uren (nachten, weekenden, feestdagen) zijn precies wanneer een onopgemerkte indringer de meeste schade aanricht, en toch is een SOC van 24/7 in huis bemannen duur en moeilijk vol te houden. De ruil is context en controle tegenover kosten en snelheid tot dekking: een eigen team kent je landschap diep maar is traag en duur om te bouwen, terwijl een beheerde provider directe expertise rond de klok geeft tegen de prijs van dunnere context en een leveranciersafhankelijkheid. Neem je huidige dekkingsuren mee, je gemiddelde tijd tot detectie en respons buiten kantooruren, je alarmvolume en een eerlijke lezing of je de analisten kunt werven en behouden die een zelf gedraaid centrum nodig heeft. Weeg voor overheid en gereguleerde ondernemingen dataresidentie, personeelsscreening en wettelijke meldingsverplichtingen die de provider moet kunnen nakomen, en bevestig dat het contract de forensische rigueur en bewakingsketen behoudt die juridische procedures eisen.

## Sectorperspectief

**Startup.** Snelheid en overleven gaan voor, dus koop beveiliging als bijproduct van tools die je al draait in plaats van operaties te bemannen. Koppel gratis scanners aan CI om geheimenlekken en bekend kwetsbare afhankelijkheden bij commit te blokkeren, stuur logs naar een goedkope beheerde dienst met een handvol alarmen met hoge waarde en schrijf een incidentplan van één pagina (wie te bellen, hoe inloggegevens te roteren, momentopname voor je herbouwt) voordat je het ooit nodig hebt. Je schaarsste middel is engineeringaandacht, dus automatiseer het routinematige en weersta het opzetten van een beveiligingsoperatiecentrum dat je niet draaiend kunt houden.

**Kleinbedrijf.** Zonder aparte beveiligingsspecialist en met een krap budget leun je op beheerde detectie en respons en op de beveiligingsfuncties die al in je platforms zijn gebouwd. Behandel patchen en bezittingeninventaris als de gewoonten met de hoogste hefboom: weet wat je draait, houd het actueel en dwing een eenvoudige hersteldeadline af per ernst. Geef de voorkeur aan leveranciers die bewaking rond de klok, meldingen van gecoördineerde bekendmaking en forensische vastlegging voor je afhandelen, en oefen het ene wat je niet kunt uitbesteden, namelijk beslissen wie een incident uitroept en wie met klanten praat.

**Grote onderneming.** De uitdaging is consistentie over veel teams en honderden pipelines: een gedeeld poortbeleid van blokkeren-versus-volgen, organisatiebreed afgedwongen herstel-SLA's, een SIEM- en SOAR-platform met gemeten detecties en purple teaming die elke oefening omzet in nieuwe dekking. Beheer beveiligingsoperaties als portfolio met dashboards voor gemiddelde tijd tot detectie en respons, SLA-naleving en detectieprecisie, en besluit bewust waar eigen diepte beter is dan beheerde schaal. Begroot de kosten van menselijk toezicht op triage en afstemming expliciet, want automatisering verschuift inspanning in plaats van haar weg te nemen.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Wettelijke deadlines voor incidentmelding en gecoördineerde bekendmaking van kwetsbaarheden zijn verplichtingen in plaats van opties, dus oefen het meldingspad naar de nationale autoriteit even zorgvuldig als de technische respons, en bewaar forensisch bewijs onder een bewakingsketen die juridische toetsing weerstaat. Geef de voorkeur aan contracten die detectielogica en data overdraagbaar houden, eis dat elke beheerde provider aan eisen voor residentie en screening voldoet en verwacht dat red-teambeoordelingen en continu scannen een autorisatieproces voeden dat het publiek kan vertrouwen.

## Voorbeelden

**Startup.** Een startup zonder beveiligingsoperatiecentrum koppelt gratis scanners aan zijn CI-pipeline zodat geheimenlekken en bekend kwetsbare afhankelijkheden bij commit worden gevangen, alleen blokkerend op bevindingen met hoge zekerheid zodat de twee engineers niet verdrinken in ruis. Ze schrijven een incidentplan van één pagina voordat ze het nodig hebben: wie te bellen, hoe inloggegevens te roteren en een gecompromitteerde host eerst een momentopname te nemen voor ze hem herbouwen zodat ze kunnen leren wat er gebeurde. Ze sturen logs naar een goedkope beheerde dienst en stellen een paar alarmen in op de gebeurtenissen die werkelijk een inbreuk zouden signaleren, zodat een probleem in uren verschijnt in plaats van de maanden die het kost om het per ongeluk te merken.

**Grote onderneming.** Een software-als-dienstbedrijf draait SAST, SCA, IaC- en geheimenscanning in elke pipeline, alleen blokkerend op bevindingen met hoge ernst en hoge zekerheid en de rest volgend op een dashboard met herstel-SLA's. Een SIEM voedt een SOAR-platform dat bij alarmen met hoge zekerheid automatisch hosts isoleert en inloggegevens intrekt, wat de gemiddelde tijd tot respons van uren naar minuten terugbrengt. Kwartaalmatige purple-teamoefeningen tegen MITRE ATT&CK-technieken genereren direct nieuwe detectieregels en dichten gestaag dekkingsgaten.

**Overheid.** Een federale instantie opereert een beveiligingsoperatiecentrum (SOC) met voorgeschreven incidentmelding aan een nationale cyberautoriteit binnen wettelijke deadlines. Ze draait een programma voor gecoördineerde bekendmaking van kwetsbaarheden met een publiek meldkanaal zoals beleid vereist, en bewaart forensisch bewijs onder strikte bewakingsketenprocedures geschikt voor juridische procedures. Jaarlijkse red-teambeoordelingen en continu kwetsbaarheidsscannen voeden de lopende autorisatie van de instantie en haar risicogebaseerde herstel-SLA's.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Bijna alles aan de zaak voor beveiligingsoperaties komt neer op verblijftijd: hoe langer een aanvaller onopgemerkt blijft, hoe meer de inbreuk kost. Onderzoeken tonen consequent dat incidenten die snel worden beperkt dramatisch minder kosten dan die welke maandenlang blijven hangen. De total cost of ownership omvat tooling (SIEM, SOAR, scanners), personeel of beheerde diensten voor detectie en respons en de tijd om incidentprocessen te bouwen en te oefenen. Daartegenover staan de kosten van niet investeren: een inbreuk laat ontdekt, die zich over systemen verspreidt, boetes van toezichthouders, verplichte meldingen, rechtszaken en reputatieschade trekt, alles erger gemaakt door de chaos van een ongeoefende respons.

Het ROI komt uit snellere detectie en respons, automatisering die een klein team een groot landschap laat dekken en preventieverbeteringen teruggevoerd uit elk incident en elke oefening. DevSecOps in het bijzonder betaalt zich uit door problemen in de pipeline te vangen waar ze goedkoop zijn, in plaats van in productie waar ze duur en publiek zijn. Zet voor het bestuur getallen op je huidige gemiddelde tijd tot detectie en respons, toon hoe die aan verblijftijd en kosten zijn gekoppeld en formuleer automatisering als krachtvermenigvuldiging die vermijdt dat de formatie in de pas met het landschap groeit. Benadruk voor de overheid dat wettelijke meldings- en bekendmakingsverplichtingen volwassen operaties niet optioneel maken.

## Antipatronen en valkuilen

- **Alarmmoeheid.** Zoveel alarmen dat analisten ze wegfilteren en het echte missen.
- **Scannen zonder herstel.** Bevindingen genereren die niemand repareert, wat een vals gevoel van veiligheid en auditschuld creëert.
- **Geen incidentplan.** Improviseren tijdens een crisis, kritieke minuten verspillend en bewijs verkeerd afhandelend.
- **Bewijs vernietigen.** Een gecompromitteerde host herbouwen voor forensische vastlegging, en het vermogen verliezen te begrijpen of te bewijzen wat er gebeurde.
- **Beschuldigingscultuur in reviews.** Responders straffen zodat het volgende incident wordt verborgen of defensief wordt afgehandeld.
- **Pentesten alleen voor compliance.** Eén jaarlijkse test om een auditor tevreden te stellen, met bevindingen genegeerd tot volgend jaar.
- **Blokkerende poorten met veel valse positieven.** Vertrouwen eroderen tot engineers eisen dat de poorten helemaal worden verwijderd.
- **Detecties zetten en vergeten.** Regels die verslechteren naarmate de omgeving en tegenstanders evolueren, stilletjes dekking verliezend.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Beveiligingsoperaties zijn ad hoc en reactief. Beveiligingstesten is handmatig en zeldzaam, en er is geen centrale logging of SIEM. Er bestaat geen incidentplan, dus respons wordt in het moment geïmproviseerd. Patchen gebeurt alleen wanneer een kop het afdwingt, en verdedigingen worden nooit vijandig getest.

**Niveau 2: Ontwikkelen.** Basispraktijken verschijnen maar zijn inconsistent over teams. Sommige pipelines draaien scanners terwijl andere er geen draaien, en centrale logging bestaat in zakken. Een basaal incidentplan is gedocumenteerd maar zelden geoefend, patchen volgt losse termijnen en een jaarlijkse pentest stelt compliance tevreden zonder veel te veranderen. Dekking en rigueur hangen af van welk team je vraagt.

**Niveau 3: Standaardiseren.** Praktijken zijn gedocumenteerd en organisatiebreed gehandhaafd. Volledige DevSecOps-scanning met risicogebaseerde poorten wordt consistent toegepast, een SIEM correleert gebeurtenissen en eerste SOAR-draaiboeken draaien. Incidentrespons wordt geoefend met tabletops en schuldvrije reviews, herstel-SLA's per ernst worden afgedwongen met benoemde eigenaren, en gecoördineerde bekendmaking van kwetsbaarheden en regelmatig red teaming zijn de norm in plaats van de uitzondering.

**Niveau 4: Beheersen.** Operaties worden gemeten en beheerst aan de hand van uitgangswaarden. Gemiddelde tijd tot detectie en respons, SLA-naleving per ernstlaag, scandekking, percentages ware en valse positieven van detecties en verblijftijd worden op dashboards gevolgd en volgens een ritme beoordeeld. Detecties dragen gemeten precisie en recall afgebeeld op MITRE ATT&CK, automatiseringsbeslissingen worden gepoort op data over valse positieven in plaats van hoop, en een statistiek die voorbij haar uitgangswaarde afdrijft triggert een gedefinieerde reactie in plaats van onopgemerkt te blijven.

**Niveau 5: Orkestreren.** Beveiligingsoperaties worden continu verbeterd, geïntegreerd over de organisatie en adaptief. Detectie-engineering, purple teaming, herstel en incidentreview voeden één lus die zich aanpast aan nieuwe tegenstandertechnieken zodra ze opduiken. Geautomatiseerde draaiboeken handelen het routinematige af over het hele landschap zodat mensen zich op oordeel concentreren, beveiliging wordt samen met oplevering en risico gepland en elk incident en elke oefening verhardt het systeem meetbaar terwijl de kernstatistieken omlaag blijven trenden.

## Ideeën voor discussie

1. Welke pipelinebevindingen moeten een release blokkeren, en welke slechts worden gevolgd?
2. Een eigen SOC bouwen, beheerde detectie en respons gebruiken of de twee mengen, en waarom?
3. Hoe voorkom je dat detectieregels verslechteren naarmate je omgeving evolueert?
4. Hoe agressief moet patchen worden geautomatiseerd gezien het risico van brekende wijzigingen?
5. Hoe ziet een werkelijk schuldvrije review na een incident eruit in jouw cultuur?
6. Hoe meet je of red en purple teaming je verdedigingen werkelijk verbeteren?

## Belangrijkste inzichten

- Preventie faalt uiteindelijk. Operaties bestaan om snel te detecteren en te reageren.
- Bed SAST, DAST, SCA, IaC en geheimenscanning in de pipeline met risicogebaseerde poorten.
- Prioriteer patchen naar echte uitbuitbaarheid en kritiek van het bezit, onder afgedwongen SLA's.
- Oefen incidentrespons, bewaar forensisch bewijs en plan inbreukcommunicatie vooraf.
- Gebruik SIEM en SOAR om te correleren en te automatiseren. Behandel detecties als geëngineerde, geteste code.
- Valideer verdedigingen met pentesten, red teaming en samenwerkend purple teaming.
- Verblijftijd drijft inbreukkosten, dus gemiddelde tijd tot detectie en respons zijn de statistieken die tellen.

## Referenties en verder lezen

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / SIEM literature
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, *Coordinated Vulnerability Disclosure* guidance and *CVSS* specification
