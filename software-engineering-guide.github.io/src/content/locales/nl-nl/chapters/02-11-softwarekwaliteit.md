# 2.11 Softwarekwaliteit

## Overzicht en motivatie

[Softwarekwaliteit](https://en.wikipedia.org/wiki/Software_quality) is hoe goed een systeem voldoet aan uitgesproken behoeften en redelijke verwachtingen. Dat betekent meer dan of het werkt: het betekent of het systeem betrouwbaar, veilig, onderhoudbaar, bruikbaar, performant en geschikt voor zijn doel is over de tijd. Kwaliteit is breder dan testen. Testen (hoofdstuk 2.4) is één activiteit die defecten onthult. Kwaliteit is de hele discipline van het juiste ding goed bouwen, en van met bewijs weten dat je dat hebt gedaan. Een systeem kan elke test doorstaan en toch van lage kwaliteit zijn als het ononderhoudbaar, ontoegankelijk of slecht afgestemd is op wat gebruikers werkelijk nodig hebben.

In een groot team kan kwaliteit niet in het hoofd van één persoon of de gewoonten van één team wonen. Honderden engineers, meerdere producten en langlevende systemen hebben een gedeelde definitie van kwaliteit nodig, expliciete processen om haar te waarborgen en metingen die vertellen of ze beter of slechter wordt. Zonder dat wordt "kwaliteit" een vage aspiratie die elk argument tegen een deadline verliest, en stapelen defecten zich op tot verandering traag en riskant wordt.

In omgevingen van onderneming en overheid stijgt de inzet verder. Gereguleerde, veiligheidskritieke en burgergerichte systemen moeten kwaliteit aantonen, niet alleen beweren: gedocumenteerde processen, traceerbaar bewijs en onafhankelijke verificatie zijn vaak verplicht. Slechte kwaliteit draagt directe financiële, juridische en reputatiekosten, en in sommige domeinen brengt ze mensen in gevaar. Een bewuste kwaliteitsdiscipline, opgebouwd uit modellen, processen, meting en cultuur, maakt van kwaliteit een beheerste uitkomst in plaats van een toeval.

## Kernprincipes

- Kwaliteit is geschiktheid voor het doel plus conformiteit met vereisten. Definieer beide expliciet.
- Kwaliteit wordt ingebouwd, niet ingetest. Verificatie vindt defecten, maar preventie voorkomt ze.
- Onderscheid [kwaliteitsborging](https://en.wikipedia.org/wiki/Quality_assurance) (zijn onze processen gezond?) van [kwaliteitsbeheersing](https://en.wikipedia.org/wiki/Quality_control) (is dit product goed?).
- Verificatie vraagt "hebben we het goed gebouwd?" Validatie vraagt "hebben we het juiste gebouwd?"
- Meet kwaliteit met een kleine set betekenisvolle statistieken. Behandel statistieken als signalen, niet als doelen.
- De kosten van een defect stijgen naarmate het later wordt gevonden, dus verschuif kwaliteitsactiviteiten naar eerder.
- Kwaliteit is een eigenschap van de hele organisatie en haar cultuur, geen poort aan het eind.

## Aanbevelingen

### Neem een gedeeld kwaliteitsmodel aan zoals ISO/IEC 25010

Geef je organisatie een gemeenschappelijk vocabulaire voor kwaliteit door een erkend productkwaliteitsmodel aan te nemen. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) definieert kenmerken waaronder functionele geschiktheid, prestatie-efficiëntie, compatibiliteit, bruikbaarheid, betrouwbaarheid, beveiliging, onderhoudbaarheid en overdraagbaarheid. Gebruik het om kwaliteit concreet te maken: besluit voor elk systeem welke kenmerken het meest tellen en wat "goed genoeg" voor elk betekent. Deze productkwaliteitskenmerken zijn dezelfde **kwaliteitsattributen** die architectuur sturen (hoofdstuk 3.1). Kwaliteit en architectuur zijn twee gezichtspunten op één zorg, dus laat ze één lijst van prioriteiten delen in plaats van twee concurrerende.

### Scheid kwaliteitsborging van kwaliteitsbeheersing

Behandel kwaliteitsborging (QA) en kwaliteitsbeheersing (QC) als aparte maar complementaire activiteiten. QA is procesgericht en preventief: ze verbetert hoe het werk wordt gedaan, via standaarden, reviews, definities van klaar en training, zodat defecten minder waarschijnlijk verschijnen. QC is productgericht en detecterend: ze inspecteert werkelijke werkproducten, zoals testen, [codereview](https://en.wikipedia.org/wiki/Code_review) en audits, om defecten te vangen die er wel in kwamen. Een volwassen organisatie investeert in beide, maar neigt naar QA, omdat defecten voorkomen goedkoper is dan ze vinden en herstellen.

### Voer expliciete softwarekwaliteitsmanagementprocessen uit

Maak van kwaliteit een beheerd proces, geen stille hoop. Schrijf voor belangrijk werk een kwaliteitsplan dat de doelkwaliteitskenmerken, de borgings- en beheersingsactiviteiten, de acceptatiecriteria en de verantwoordelijken benoemt. Weef het in praktijken die je al hebt: codereview (hoofdstuk 2.5) als zowel beheersmaatregel als manier om kennis te delen, teststrategie (hoofdstuk 2.4) als het geautomatiseerde vangnet en [statische analyse](https://en.wikipedia.org/wiki/Static_program_analysis) als continue inspectie. Beoordeel de kwaliteitsdata regelmatig en handel op trends, in plaats van alleen op incidenten te reageren.

### Oefen verificatie en validatie als aparte disciplines

Verificatie bevestigt dat werkproducten aan hun specificaties voldoen, zodat de juiste invoer van elke fase de juiste uitvoer oplevert, via reviews, statische analyse en testen tegen vereisten. Validatie bevestigt dat het voltooide systeem werkelijk aan gebruikersbehoeften en beoogd gebruik voldoet, via gebruikerstests, acceptatietests, pilots en veldfeedback. Je hebt beide nodig. Een systeem kan correct zijn tegen een gebrekkige specificatie (geverifieerd maar niet valide), of een echte behoefte aanpakken en toch defecten bevatten (valide maar niet geverifieerd). In gereguleerde omgevingen kan onafhankelijke [verificatie en validatie](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) door een partij los van de ontwikkelaars verplicht zijn.

### Meet kwaliteit met betekenisvolle statistieken

Kies een kleine set statistieken die kwaliteitsresultaten en hun drijfveren weerspiegelen, en volg ze over de tijd. Nuttige maten zijn defectdichtheid, percentage ontsnapte defecten (defecten gevonden in productie tegenover vóór de release), gemiddelde tijd tot detectie en herstel, faalpercentage van wijzigingen, codegezondheidssignalen zoals complexiteit en duplicatie, en validatiesignalen zoals door gebruikers gemelde problemen en toegankelijkheidsconformiteit. Mijd ijdelheids- en manipuleerbare statistieken: een statistiek die een doel wordt, meet de werkelijkheid niet meer. Combineer de cijfers met kwalitatieve signalen uit reviews en gebruikersfeedback.

### Kenmerk en beheer defecten systematisch

Behandel defecten als data, niet alleen als branden om te blussen. Classificeer ze naar ernst, type en grondoorzaak. Volg ze van ontdekking tot oplossing. Zoek patronen zodat je herhaling kunt voorkomen. Gebruik technieken als [grondoorzaakanalyse](https://en.wikipedia.org/wiki/Root_cause_analysis) en defectcategorisering om eenmalige fouten van systemische zwaktes te onderscheiden. Voed wat je leert terug in QA, via bijgewerkte standaarden, toegevoegde tests en verbeterde reviews, zodat dezelfde klasse defecten niet terugkeert. Een defect hersteld zonder zijn oorzaak te begrijpen is een defect dat je hebt uitgenodigd terug te komen.

### Beheer de kosten van kwaliteit bewust

Begrijp de economie van kwaliteit via de klassieke categorieën: preventiekosten (training, standaarden, goed ontwerp, tooling), beoordelingskosten (reviews, testen, audits) en faalkosten (intern herwerk voor de release, plus externe falen gevonden door gebruikers, die veel meer kosten). Verschuif je investering naar preventie en vroege beoordeling, want elke euro daar vermijdt vele euro's aan faalkosten later. Maak deze kosten zichtbaar, zodat "we hebben geen tijd voor kwaliteit" wordt gezien voor wat het is: een keuze om in plaats daarvan meer aan falen uit te geven.

### Bouw een kwaliteitscultuur

Maak kwaliteit ieders verantwoordelijkheid, bezeten door de teams die de software bouwen, in plaats van haar over te dragen aan een stroomafwaartse QA-afdeling die haar aan het eind inspecteert. Leiders moeten kwaliteitsresultaten belonen, het veilig maken defecten en bijna-ongelukken te melden en kwaliteitsdata behandelen als leerinstrument in plaats van als stok. Een schuldvrije omgang met defecten brengt problemen vroeg aan het licht. Een beschuldigende verbergt ze tot ze duur zijn.

## Afwegingen: voor- en nadelen

| Praktijk / keuze | Voordelen | Nadelen |
|---|---|---|
| Formeel kwaliteitsmodel (ISO 25010) | Gedeeld vocabulaire. Expliciete prioriteiten | Overhead bij dogmatische toepassing |
| Zware kwaliteitsborging (preventie) | Minder defecten. Lagere totale kosten | Investering vooraf. Langzamer rendement |
| Zware kwaliteitsbeheersing (inspectie) | Vangt defecten die doorglippen | Duur. Vindt defecten laat |
| Onafhankelijke V&V | Hoge zekerheid. Objectief | Kostbaar. Langzamer. Kan vijandig voelen |
| Rijke kwaliteitsstatistieken | Zicht. Vroegtijdige waarschuwing | Risico van manipulatie. Meetoverhead |
| Aparte QA-team | Focus en expertise | Kan verantwoordelijkheid van ontwikkelaars afschuiven |
| Kwaliteit bezeten door teams | Eigenaarschap. Snelle feedback | Vraagt discipline en vaardigheid overal |

De centrale afweging is investering tegenover zekerheid, gevormd door timing. Preventie kost nu geld om grotere faalkosten later te vermijden. Het economisch juiste kwaliteitsniveau is dus niet het maximum. Het is het punt waar de marginale kosten van meer zekerheid gelijk zijn aan de faalkosten die ze vermijdt. Dat punt ligt hoog voor veiligheidskritieke systemen en lager voor interne hulpmiddelen met lage inzet. De andere terugkerende spanning is eigenaarschap. Centrale QA-groepen bouwen expertise op maar kunnen ontwikkelaars verantwoordelijkheid laten afschuiven. Door teams bezeten kwaliteit bouwt eigenaarschap op maar vraagt overal vaardigheid en discipline.

## Vragen om met je team te bespreken

1. **Wanneer dezelfde klasse defecten twee keer opduikt, voeren we dan grondoorzaakanalyse uit, of repareren we het gewoon opnieuw?** Een defect hersteld zonder zijn oorzaak te begrijpen is een defect dat je hebt uitgenodigd terug te komen, en in een groot team kan dezelfde grondoorzaak over veel services opduiken voordat iemand de punten verbindt. Defecten als data behandelen (geclassificeerd naar ernst, type en oorzaak, daarna gemijnd op patronen) is wat een team dat gestaag betrouwbaarder wordt scheidt van een dat druk blijft met dezelfde fout opnieuw herstellen. Neem je defecttracker mee naar de vergadering en zoek naar terugkerende handtekeningen: hoeveel recente incidenten delen een oorzaak die je nooit systemisch hebt aangepakt? Het antwoord moet preventie voeden, zodat een terugkerende oorzaak een bijgewerkte standaard, een nieuwe gedeelde helper, een toegevoegde test of een betere reviewchecklist aandrijft, want zo stopt een fix op één plek de hele klasse van terugkeer.

2. **Is het op ons team veilig om een defect of bijna-ongeluk te melden, en wat gebeurt er met de persoon die er een aankaart?** Kwaliteit is een eigenschap van cultuur, en een schuldvrije omgang brengt problemen vroeg aan het licht terwijl een beschuldigende ze verbergt tot ze duur zijn, wat in een gereguleerd of burgergericht systeem een publiek falen of een boete kan betekenen. Dit telt het meest op schaal, waar de engineer die het dichtst bij een risico zit vaak junior is en de prikkel om te zwijgen sterk. Neem eerlijke signalen mee: worden bijna-ongelukken gelogd en besproken, of verdwijnen ze? Benoemen postmortems oorzaken of mensen? De actie is kwaliteitsdata een leerinstrument te maken in plaats van een stok, de mensen te belonen die problemen aan het licht brengen en schuldvrije postmortems te houden, want je kunt niet voorkomen wat je team bang is te melden.

3. **Kan validatie een release werkelijk stoppen, en wie heeft die bevoegdheid wanneer een deadline dreigt?** Verificatie (hebben we het goed gebouwd?) en validatie (hebben we het juiste gebouwd?) zijn aparte disciplines, en validatie heeft alleen tanden als een gefaalde toegankelijkheidscontrole, een gefaalde acceptatietest of vernietigend gebruikersonderzoek het opleveren werkelijk kan blokkeren. In omgevingen van onderneming en overheid is dit vaak verplicht, soms via onafhankelijke verificatie en validatie door een partij los van de ontwikkelaars, en "we hebben het toch opgeleverd" is geen antwoord dat een toezichthoudend orgaan accepteert. Neem je laatste releases mee: heeft een kwaliteitssignaal er ooit een werkelijk gestopt, of wijkt de poort altijd voor de datum? Als validatie nooit een release heeft geblokkeerd, is ze decoratie, en de oplossing is acceptatiecriteria vooraf in het kwaliteitsplan te schrijven, te benoemen wie de go/no-go-beslissing bezit en die beslissing echte bevoegdheid te geven los van de leveringsdruk.

4. **Kennen we onze kosten van slechte kwaliteit werkelijk, en verschuiven we uitgaven bewust van falen naar preventie?** Kosten van slechte kwaliteit (COPQ) zijn het geld dat verloren gaat aan intern herwerk, productie-incidenten, noodoplossingen, supportbelasting, verloren gebruikers en boetes, en ze zijn bijna altijd groter dan de zichtbare uitgaven aan reviews en testen. In een groot team zijn de faalkosten verspreid over incidentkanalen, supportwachtrijen en herwerk dat niemand als herwerk logt, dus ze blijven onzichtbaar tot iemand ze optelt. De spanning is dat preventie nu geld kost, in een budgetcyclus, om faalkosten te vermijden die later vallen en op het budget van iemand anders, wat de ruil eindeloos makkelijk uit te stellen maakt. Neem echte cijfers mee: aantal incidenten en kosten, herwerkuren, percentage ontsnapte defecten en de huidige verdeling van uitgaven over preventie, beoordeling en falen, en besluit of de mix eerder moet verschuiven. Leg voor systemen van ondernemingen en overheden, waar het meeste van de levensduurkosten na de eerste release valt, COPQ voor aan degenen die het budget beheren, want een getal dat een toezichthoudend orgaan kan zien is veel moeilijker weg te ruilen dan een vage oproep tot "kwaliteit".

5. **Welke van onze kwaliteitsstatistieken zijn stilletjes doelen geworden, en welk gedrag drijven ze nu aan?** Een statistiek die een doel wordt, meet de werkelijkheid niet meer: jaag op een dekkingspercentage en je krijgt tests geschreven om het getal te bewegen, niet tests die defecten vangen. Op schaal is dit gevaarlijk, want een kopdashboard gedeeld over tientallen teams stelt de prikkels voor al die teams, en een manipuleerbare statistiek verspreidt het manipuleren overal tegelijk. De concurrerende overweging is dat je meting nog steeds nodig hebt, dus het antwoord is zelden "laat de statistiek vallen" maar "combineer haar met een tegensignaal en lees haar naast kwalitatief bewijs uit reviews en van gebruikers". Neem je huidige set statistieken mee en vraag voor elk wat iemand onder druk kan doen om hem te bewegen zonder kwaliteit te verbeteren, en of je dat hebt zien gebeuren. Wees in gereguleerde en burgergerichte settings extra op je hoede voor conformiteitsstatistieken die groen lijken terwijl de onderliggende validatie (toegankelijkheid, echte gebruikersresultaten) nooit werkelijk is uitgeoefend, aangezien een auditor uiteindelijk de werkelijkheid achter het getal zal testen.

6. **Wie bezit hier kwaliteit: de teams die de code schrijven, of een aparte groep aan het eind, en welke financieren we werkelijk?** Eigenaarschap geeft alles stroomafwaarts vorm, want een stroomafwaarts QA-silo laat ontwikkelaars de verantwoordelijkheid voor de code die ze schrijven afschuiven, terwijl door teams bezeten kwaliteit eigenaarschap opbouwt ten koste van de eis van vaardigheid en discipline in elk team. In een groot team is dit niet het een of het ander: het duurzame patroon is meestal teams die kwaliteit bezitten via codereview en geautomatiseerde tests, ondersteund door een kleine centrale groep die standaarden onderhoudt, kwaliteitsborging als procesverbetering uitvoert en coacht, in plaats van kwaliteit aan het eind in te inspecteren. Neem een eerlijke kaart mee van waar kwaliteitswerk nu gebeurt, wie verantwoordelijk is wanneer een defect ontsnapt en waar budget en formatie werkelijk zitten tegenover waar de retoriek zegt dat kwaliteit leeft. Voeg voor organisaties van onderneming en overheid de eis van onafhankelijke verificatie en validatie toe: sommige zekerheidsregimes schrijven een aparte partij voor, dus besluit bewust welke beheersmaatregelen bij de leveringsteams horen en welke onafhankelijk moeten blijven om aan de audit te voldoen.

## Sectorperspectief

**Startup.** Snelheid telt meer dan ceremonie, dus benoem de twee of drie kwaliteitskenmerken die je product werkelijk beschermen, meestal betrouwbaarheid en onderhoudbaarheid, en laat afwerking wachten. Bezit kwaliteit met het hele team via codereview en een bescheiden geautomatiseerde testsuite in plaats van een aparte QA-groep op te zetten die je niet kunt bemannen. Wanneer dezelfde klasse bug twee keer opduikt, besteed dan twintig minuten aan grondoorzaak en voeg één gedeelde helper plus een test toe, zodat preventie goedkoop blijft en je faalpercentage van wijzigingen laag blijft terwijl je snel beweegt.

**Kleinbedrijf.** Zonder aparte kwaliteitsspecialist en met een krap budget leun je op kwaliteit die is ingebouwd in de tools en platforms die je koopt in plaats van een proces dat je moet draaien. Behandel bij het kiezen van software het kwaliteitsbewijs van de leverancier als onderdeel van de aankoop: beveiligingshouding, toegankelijkheid, reactiesnelheid van support en hoe vaak hun releases iets breken. Volg een handvol goedkope, eerlijke signalen (productie-incidenten, door klanten gemelde problemen, tijd tot herstel) in plaats van een uitgebreid statistiekenprogramma waarvoor je niemand hebt om het te onderhouden.

**Grote onderneming.** Het werk is consistentie over veel teams: neem een gedeeld kwaliteitsmodel als ISO/IEC 25010 aan, scheid kwaliteitsborging (proces) van kwaliteitsbeheersing (product) en voer kosten-van-kwaliteitreviews uit die uitgaven naar preventie verschuiven. Houd kwaliteit bezeten door de leveringsteams, ondersteund door een kleine centrale groep die standaarden en dashboards onderhoudt voor percentage ontsnapte defecten, faalpercentage van wijzigingen en trends in codegezondheid. Standaardiseer het vocabulaire en de poorten zodat groepen ophouden kwaliteitspraktijk opnieuw uit te vinden, terwijl teams ruimte houden om die lat op hun eigen manier te halen.

**Overheid.** Aanbesteding, transparantie en publieke verantwoording zetten het kader, dus schrijf kwaliteitseisen in contracten en eis gedocumenteerd, traceerbaar kwaliteitsbewijs in plaats van beweringen. Verwacht onafhankelijke verificatie en validatie door een partij los van de ontwikkelaars, verplichte toegankelijkheidsconformiteit en defectregisters met ernst en grondoorzaak bewaard als deel van het auditspoor. Rapporteer cijfers over kosten van slechte kwaliteit (herwerk, bezwaren, dienstfalen) aan toezichthoudende organen en geef validatie echte bevoegdheid een release te blokkeren die de burgers die ervan afhangen zou teleurstellen.

## Voorbeelden

**Startup.** Een startup van vijf personen besluit dat voor zijn vroege product betrouwbaarheid en onderhoudbaarheid de kwaliteitskenmerken zijn die ertoe doen, en laat pixel-perfecte afwerking wachten. Kwaliteit is van het hele team: codereview en een bescheiden geautomatiseerde testsuite zijn de beheersmaatregelen, en er is geen aparte QA-groep om defecten aan over te dragen. Wanneer dezelfde klasse bug twee keer opduikt, besteden ze twintig minuten aan een snelle grondoorzaakblik en voegen ze één gedeelde helper plus een test toe, zodat het ophoudt terug te keren in plaats van elke keer met de hand te worden hersteld. Die kleine gewoonte van preventie houdt hun faalpercentage van wijzigingen laag terwijl ze nog snel bewegen.

**Grote onderneming.** Een groot financieel dienstverlener neemt ISO/IEC 25010 aan als kwaliteitsvocabulaire en legt voor elk product doelniveaus vast voor betrouwbaarheid, beveiliging en onderhoudbaarheid. Teams bezitten kwaliteit: codereview en geautomatiseerde tests zijn beheersmaatregelen in de pipeline, terwijl een kleine centrale groep QA uitvoert door standaarden te onderhouden en te coachen. Een kwaliteitsdashboard volgt percentage ontsnapte defecten, faalpercentage van wijzigingen en trends in codegezondheid. Defecten worden geclassificeerd en tot de grondoorzaak onderzocht, en terugkerende oorzaken drijven updates van gedeelde bibliotheken en checklists. Het leiderschap bekijkt elk kwartaal kosten-van-kwaliteitdata en heeft uitgaven naar preventie verschoven, wat zowel productie-incidenten als de kosten van het herstellen ervan verlaagt.

**Overheid.** Een nationale dienst die een burgergericht uitkeringsplatform levert werkt onder een zekerheidsregime dat gedocumenteerd kwaliteitsbewijs vereist. Ze voert een formeel kwaliteitsmanagementproces uit met een kwaliteitsplan per release, plus onafhankelijke verificatie en validatie door een team los van de ontwikkelaars. Verificatie controleert elk werkproduct tegen vereisten herleid naar beleid. Validatie omvat toegankelijkheidsconformiteitstests en gebruikersonderzoek met echte burgers, en beide kunnen een release blokkeren. Defecten worden gevolgd met ernst en grondoorzaak als deel van het auditspoor, en cijfers over kosten van slechte kwaliteit (herwerk, bezwaren en dienstfalen) gaan naar toezichthoudende organen om blijvende investering in preventie te rechtvaardigen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement op kwaliteit is lagere total cost of ownership en gestage leveringssnelheid. De kosten van kwaliteit hebben twee kanten. De goede uitgaven, preventie en beoordeling, zijn zichtbaar en beheersbaar: ontwerp, standaarden, reviews, testen en tooling. De kosten van slechte kwaliteit (COPQ) zijn groter maar vaak verborgen: intern herwerk, productie-incidenten, noodoplossingen, klantsupport, verloren gebruikers, boetes van toezichthouders en reputatieschade. Onderzoek dat teruggaat tot Crosby's "Quality Is Free" vindt consequent dat de totale kosten van slechte kwaliteit de kosten van het voorkomen ervan overtreffen, en dat defecten veel duurder worden naarmate je ze later vangt: een kwestie gevonden in het ontwerp kost een fractie van dezelfde kwestie gevonden in productie.

Voor het bestuur is het argument niet "geef meer uit aan kwaliteit". Het is "geef eerder uit om in totaal minder uit te geven". Kwantificeer COPQ uit je eigen data (aantal incidenten en kosten, herwerkuren, percentage ontsnapte defecten) en laat zien hoe preventie en vroege beoordeling haar omlaag brengen. Verbind kwaliteit aan bedrijfsresultaten: betrouwbaarheid behoudt klanten, onderhoudbaarheid houdt toekomstige verandering goedkoop en beveiliging en toegankelijkheid houden je uit juridische problemen. In langlevende systemen van ondernemingen en overheden, waar het meeste van de kosten na de eerste release valt, domineren de onderhoudbaarheids- en betrouwbaarheidsdimensies van kwaliteit de levensduurkosten. Dat maakt vroege kwaliteitsinvestering een van de beslissingen met de hoogste hefboom die je kunt nemen.

## Antipatronen en valkuilen

- **Kwaliteit als eindpoort:** kwaliteit aan het eind in-inspecteren in plaats van inbouwen, zodat defecten worden gevonden wanneer ze het duurst zijn.
- **Testen verwarren met kwaliteit:** aannemen dat slagende tests hoge kwaliteit betekenen, onderhoudbaarheid, bruikbaarheid en geschiktheid voor het doel negerend.
- **QA als apart silo:** een stroomafwaarts team dat "kwaliteit bezit" en ontwikkelaars verantwoordelijkheid voor de code die ze schrijven laat afschuiven.
- **Statistiektheater:** dekkingspercentages of defectaantallen najagen als doelen, wat manipulatie uitnodigt en echte kwaliteit verbergt.
- **Verificatie zonder validatie:** de specificatie correct bouwen terwijl nooit wordt gecontroleerd of de specificatie aan echte behoeften voldoet.
- **Geen grondoorzaakanalyse:** defecten afzonderlijk herstellen zonder de systemische oorzaak aan te pakken, zodat dezelfde klasse terugkeert.
- **Kosten van slechte kwaliteit negeren:** kwaliteit behandelen als pure kost omdat faalkosten verborgen en ongemeten zijn.

## Volwassenheidsmodel

**Niveau 1 (Initiëren).** Kwaliteit is ongedefinieerd en ad hoc. Ze rust op individuele toewijding, wordt vooral gecontroleerd door handmatig testen aan het eind en defecten worden reactief afgehandeld zodra ze opduiken. Er is geen gedeeld model, geen statistieken en geen scheiding tussen borging en beheersing.

**Niveau 2 (Ontwikkelen).** Basispraktijken verschijnen: codereview, geautomatiseerde tests en een defecttracker. Wat kwaliteitsdata wordt verzameld, maar ongelijk, en elk team doet het op zijn eigen manier. Kwaliteit wordt nog vooral gezien als testen, preventie is minimaal, verificatie gebeurt en validatie is informeel.

**Niveau 3 (Standaardiseren).** De organisatie neemt een gedeeld kwaliteitsmodel aan (zoals ISO/IEC 25010), scheidt QA van QC en voert kwaliteitsmanagementprocessen uit met kwaliteitsplannen en acceptatiecriteria, gedocumenteerd en consistent toegepast over teams. Verificatie en validatie zijn gescheiden en bewust, en defecten worden geclassificeerd en tot de grondoorzaak onderzocht volgens een afgesproken schema.

**Niveau 4 (Beheersen).** Kwaliteit wordt gemeten en beheerst aan de hand van uitgangswaarden. Een kleine set betekenisvolle statistieken wordt over de tijd gevolgd (defectdichtheid, percentage ontsnapte defecten, gemiddelde tijd tot detectie en herstel, faalpercentage van wijzigingen en codegezondheidssignalen zoals complexiteit en duplicatie), en kosten van kwaliteit worden gekwantificeerd over preventie, beoordeling en falen. Acceptatie- en kwaliteitspoorten worden op bewijs afgedwongen in plaats van mening, trends worden volgens een vast ritme beoordeeld en validatie kan een release werkelijk blokkeren.

**Niveau 5 (Orkestreren).** Kwaliteit is een continu verbeterde, cultureel bezeten discipline geïntegreerd met bedrijfs- en risicoplanning. Preventie is het accent, kosten-van-kwaliteitdata sturen waar de investering heen gaat en grondoorzaakbevindingen voorkomen systematisch herhaling. Teams bezitten kwaliteit van begin tot eind, statistieken voeden continue verbetering en de organisatie past haar kwaliteitspraktijk aan naarmate producten, risico's en regelgeving verschuiven. Dit sluit aan op de hogere niveaus van de volwassenheidsmodellen in hoofdstuk 10.8.

## Ideeën voor discussie

- Welke kwaliteitskenmerken van ISO/IEC 25010 doen er het meest toe voor je systemen, en wat is "goed genoeg" voor elk?
- Waar zit je organisatie in de uitgavenmix van preventie, beoordeling en falen, en zou die moeten verschuiven?
- Onderscheid je verificatie in de praktijk van validatie, of klap je beide samen onder "testen"?
- Wordt kwaliteit bezeten door de teams die software bouwen, of gedelegeerd aan een aparte groep, en wat zou veranderen als je haar verplaatste?
- Wat zijn je werkelijke kosten van slechte kwaliteit, en kun je ze goed genoeg meten om de zakelijke onderbouwing te maken?
- Welke van je kwaliteitsstatistieken zijn echte signalen, en welke zijn manipuleerbare doelen geworden?

## Belangrijkste inzichten

- Kwaliteit is breder dan testen: het is geschiktheid voor het doel plus conformiteit, over kenmerken als betrouwbaarheid, beveiliging en onderhoudbaarheid.
- Gebruik een gedeeld kwaliteitsmodel (ISO/IEC 25010) zodat kwaliteitsattributen expliciet zijn en aansluiten op architectuur (hoofdstuk 3.1).
- Scheid kwaliteitsborging (voorkomen, proces) van kwaliteitsbeheersing (opsporen, product), en neig naar preventie.
- Oefen verificatie (goed gebouwd) en validatie (het juiste gebouwd) als aparte disciplines.
- Meet kwaliteit met een paar betekenisvolle statistieken, en kenmerk defecten naar ernst en grondoorzaak om herhaling te voorkomen.
- Beheer de kosten van kwaliteit: preventie en vroege beoordeling zijn veel goedkoper dan falen, vooral in langlevende systemen.
- Bouw een schuldvrije kwaliteitscultuur waarin teams kwaliteit bezitten, ondersteund door codereview (hoofdstuk 2.5) en teststrategie (hoofdstuk 2.4).

## Referenties en verder lezen

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
