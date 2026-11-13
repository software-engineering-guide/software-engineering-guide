# 9.1 Site reliability engineering

## Overzicht en motivatie

[Site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) past software-engineeringpraktijken toe op het draaien van productiesystemen. In plaats van beheer te behandelen als handmatig, door tickets gedreven werk gescheiden van ontwikkeling, behandelt SRE betrouwbaarheid als engineeringprobleem dat je oplost met code, meting en heldere serviceobjectieven. Het kernidee, gepopulariseerd door Google maar nu wijdverbreid, is eenvoudig: de mensen die systemen draaiend houden zouden het merendeel van hun tijd moeten besteden aan automatisering bouwen en systemen verbeteren, niet aan steeds weer dezelfde falen met de hand blussen.

Voor grote teams doet dit ertoe omdat schaal zowel de waarde van betrouwbaarheid als de kosten van het fout doen vergroot. Wanneer één service miljoenen gebruikers of duizenden interne afnemers ondersteunt, betekent een uur uitval verloren omzet, gemiste transacties en geërodeerd vertrouwen. Handmatig beheer dat prima werkt voor een handvol servers valt uiteen onder honderden services en [continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment). SRE geeft je een gedeelde taal voor betrouwbaarheid, een manier om de afweging tussen functies opleveren en dingen stabiel houden expliciet te maken en een manier om die lijn consistent over veel teams te houden.

Contexten van onderneming en overheid voegen verder gewicht toe. Gereguleerde sectoren als bankieren, zorg en publieke diensten dragen vaak wettelijke of contractuele beschikbaarheidsverplichtingen, auditeisen en weinig tolerantie voor uitval die burgers of veiligheid raakt. Digitale overheidsdiensten publiceren steeds vaker hun betrouwbaarheidsdoelen en prestatiedata openlijk. SRE geeft je een rigoureuze, op bewijs gebaseerde manier om te definiëren wat "betrouwbaar genoeg" betekent, het eerlijk te meten en engineeringprioriteiten aan leiderschap en toezichtsorganen te verdedigen met data in plaats van mening.

*Zie ook:* hoofdstuk 9.2 (observeerbaarheid en bewaking), hoofdstuk 9.3 (incidentmanagement) en hoofdstuk 3.5 (schaalbaarheid, prestaties en veerkracht).

## Kernprincipes

- **Betrouwbaarheid is de belangrijkste functie.** Een systeem dat niet werkt is waardeloos hoeveel functies het ook heeft, maar perfecte betrouwbaarheid is niet haalbaar en haar kosten niet waard.
- **Definieer betrouwbaarheid met meetbare doelstellingen.** Service level indicators (SLI's), objectives (SLO's) en agreements (SLA's) zetten vage verwachtingen om in getallen waarover iedereen het eens kan zijn.
- **100 procent is het verkeerde doel.** Gebruikers kunnen het verschil niet zien tussen een zeer betrouwbaar systeem en een perfect betrouwbaar, dus mik op "betrouwbaar genoeg" en besteed het resterende budget aan snelheid.
- **Foutbudgetten stemmen prikkels af.** Het gat tussen de SLO en 100 procent is een budget voor risico dat ontwikkelaars en beheerders delen, wat discussies vervangt door rekenwerk.
- **Sleurwerk is de vijand.** Repetitief, handmatig, automatiseerbaar operationeel werk moet worden gemeten, begrensd en systematisch geëlimineerd.
- **Automatiseer bewust.** Automatisering is hoe een klein team een groot systeem beheert. Erin investeren is een eersterangs engineeringactiviteit.
- **Schuldvrij leren.** Falen worden behandeld als kansen om systemen en processen te verbeteren, niet om individuen te straffen.

## Aanbevelingen

### Definieer SLI's, SLO's en SLA's bewust

Begin vanuit het perspectief van de gebruiker. Een **[service level indicator](https://en.wikipedia.org/wiki/Service-level_indicator)** is een kwantitatieve maat van het gedrag van een service, zoals het aandeel verzoeken dat in minder dan 300 milliseconden wordt bediend of het deel succesvolle responses. Kies een klein aantal SLI's die werkelijk gebruikerstevredenheid weerspiegelen: beschikbaarheid, latentie, correctheid en versheid zijn gangbare. Een **[service level objective](https://en.wikipedia.org/wiki/Service-level_objective)** is een doelwaarde of -bereik voor een SLI, bijvoorbeeld "99,9 procent van de verzoeken slaagt over een voortschrijdend venster van 28 dagen." Een **[service level agreement](https://en.wikipedia.org/wiki/Service-level_agreement)** is een contract met gevolgen (terugbetalingen, boetes) verbonden aan een beloofd niveau. Houd je SLO's strikter dan je SLA's, zodat je een waarschuwing krijgt voordat je een verplichting schendt. Publiceer je SLO's, beoordeel ze per kwartaal en behandel ze als levende documenten die strakker of losser worden naarmate je leert.

### Neem foutbudgetten aan en dwing ze af

Het foutbudget is `100% min de SLO`. Als je SLO 99,9 procent is, is je budget 0,1 procent onbetrouwbaarheid per venster, ruwweg 43 minuten per maand. Besteed het aan gepland risico: agressieve releases, experimenten en gecontroleerde faaltests. Wanneer het budget gezond is, kunnen teams snel opleveren. Wanneer het op is, moet het beleid prioriteiten automatisch verschuiven naar betrouwbaarheidswerk en riskante wijzigingen pauzeren tot het systeem herstelt. De kracht van het foutbudget is dat je er vooraf over eens bent, zodat het de emotie en politiek uit het moment van een uitval haalt.

### Meet en verminder sleurwerk

Sleurwerk is operationeel werk dat handmatig, repetitief, automatiseerbaar en tactisch is en meegroeit met het systeem. Volg het percentage SRE-tijd dat aan sleurwerk wordt besteed en stel een plafond, gewoonlijk rond de 50 procent, zodat ten minste de helft van je engineeringtijd naar duurzame verbeteringen gaat. Houd een achterstand aan van projecten om sleurwerk te verminderen, prioriteer naar frequentie maal kosten en vier een terugkerende taak uitroeien net zozeer als een nieuwe functie opleveren. Een **automatiseringsmandaat** maakt dit expliciet: elke handmatige procedure die je meer dan een vast aantal keren uitvoert wordt kandidaat voor automatisering of self-servicetooling.

### Plan capaciteit en voorspel vraag

Modelleer je verwachte belasting uit historische trends, geplande lanceringen en bedrijfsprojecties. Combineer voorspellingen van organische groei met eenmalige gebeurtenissen zoals marketingcampagnes, belastingdeadlines of uitkeringsinschrijvingsperiodes die bij de overheid veel uitmaken. Houd ruimte boven de piek aan, test de belasting om je aannames te controleren en automatiseer schaling waar je kunt terwijl je een door mensen beoordeeld [capaciteitsplan](https://en.wikipedia.org/wiki/Capacity_planning) houdt voor grote verbintenissen. Volg doorlooptijden van provisioning zodat een tekort je nooit overvalt.

### Behandel betrouwbaarheid als functie met echte kosten

Elke extra "negen" beschikbaarheid kost meestal veel meer aan redundantie, testen en operationele verfijning dan de vorige. Maak de kosten van negens expliciet, zodat productowners het doel met open ogen kiezen. Ontwerp voor soepele degradatie, zodat gedeeltelijke falen verminderde dienstverlening geven in plaats van totale uitval. Investeer in redundantie en failover naar verhouding tot de SLO, niet gelijk over elke component.

### Kies een SRE-organisatiemodel

Er is geen enkele juiste structuur. Een **gecentraliseerd** SRE-team geeft je consistentie, diepe expertise en gedeelde tooling, maar kan een knelpunt worden of een stortplaats voor andermans problemen. Een **ingebed** model plaatst SRE's binnen productteams voor nauwe samenwerking, maar riskeert inconsistentie en isolatie. Veel grote organisaties gebruiken een hybride: een centraal platform- en standaardenteam plus ingebedde betrouwbaarheidsengineers, met een helder engagementmodel dat definieert wanneer een service in aanmerking komt voor SRE-ondersteuning en welke productiegereedheidslat ze eerst moet halen.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Strikte SLO's (meer negens) | Groter gebruikersvertrouwen, voldoet aan contracten | Oplopende kosten, tragere functielevering |
| Losse SLO's (minder negens) | Sneller opleveren, lagere kosten | Risico van gebruikersverloop en SLA-boetes |
| Gecentraliseerde SRE | Consistentie, gedeelde expertise | Knelpunten, afstand tot product |
| Ingebedde SRE | Nauwe samenwerking, context | Inconsistentie, moeilijk te bemannen |
| Zware automatiseringsinvestering | Schaalt, vermindert sleurwerk | Kosten vooraf, automatisering kan zelf falen |

Betrouwbaarheidsengineering gaat echt over eindige middelen verstandig besteden. Een extra negen najagen die gebruikers niet eens kunnen waarnemen verspilt geld dat functies of lagere prijzen kon financieren. De andere kant op gaan en onderinvesteren in een systeem waarvan falen echte schade veroorzaakt is nalatig. Het foutbudgetkader bestaat juist om deze afweging zichtbaar en onderhandelbaar te maken in plaats van impliciet en omstreden. De afweging van het organisatiemodel is even echt: het juiste antwoord hangt af van bedrijfsgrootte, engineeringvolwassenheid en hoe uniform je services zijn.

## Vragen om met je team te bespreken

1. **Welke exacte SLI weerspiegelt wat je gebruikers werkelijk voelen, en kun je aantonen dat het geen ijdele statistiek is?** Kies de verkeerde indicator en elk dashboard ziet groen terwijl gebruikers lijden, wat de ijdele-SLI-valkuil is waarvoor dit hoofdstuk waarschuwt. Neem echte data mee naar de discussie: meet dezelfde gebruikersreis vanuit een echt verzoekpad (login naar dashboard, afrekenen naar bevestiging) in plaats van server-CPU of een gezondheidscontrole van de backend. Voor een groot team plant één slechte SLI zich voort: tientallen services erven haar, alarmen gaan af op het verkeerde en het foutbudget betekent niets meer. In omgevingen van onderneming en overheid waar een SLA terugbetalingen of burgerimpact draagt, is je SLI het bewijs dat je aan auditors verdedigt, dus ze moet direct herleidbaar zijn tot voor de gebruiker zichtbaar succes. Als je geen lijn kunt trekken van het getal naar de ervaring van een gebruiker, vervang het getal.

2. **Wat moet een service bewijzen voordat je SRE-team haar op bereikbaarheid neemt, en wie zegt nee?** Zonder productiegereedheidslat wordt een centraal SRE-team een stortplaats voor elke onstabiele service en verdrinkt het in andermans technische schuld. Schrijf de toelatingscriteria op: een bezeten SLO, werkende runbooks, uitvoerbare alarmen, capaciteitsruimte en een aangetoond deploy-en-rollbackpad. Voor een grote organisatie is dit engagementmodel wat het betrouwbaarheidsteam ervan weerhoudt een knelpunt te worden dat iedereen vertraagt. In gereguleerde omgevingen dient de gereedheidsreview ook als maatregel die je toezichtsorganen kunt tonen. Besluit wie het gezag heeft onboarding te weigeren, want een lat die niemand afdwingt is geen lat, en het antwoord bepaalt of SRE schaalt of instort onder geërfde pijn.

3. **Hoe ver van tevoren provisioneer je voor je enkele grootste voorspelbare piek, en ken je je doorlooptijd van provisioning?** Aannemen dat cloudelasticiteit direct en oneindig is nodigt tekorten uit tijdens precies de pieken die het meest tellen, en die pieken (belastingdeadlines, inschrijfvensters, uitverkoopevenementen) zijn de momenten waarop falen het zichtbaarst en duurst is. Neem de getallen mee: historische piekbelasting, voorspelde groei, het veelvoud waartegen je belastingtest en de echte doorlooptijd om grote gereserveerde capaciteit of gespecialiseerde instanties te verkrijgen. Voor seizoensgebonden overheidsdiensten kan de piek meerdere malen de normale belasting zijn en is hij politiek niet te missen, dus weken vooraf provisioneren verslaat hopen dat autoscaling bijblijft. Het antwoord moet een concrete kalender zetten: wanneer je belastingtest, wanneer je capaciteit vergrendelt en wie de go-beslissing bezit.

4. **Wanneer je foutbudget op is, wat gebeurt er dan werkelijk, en wie heeft de positie om het af te dwingen?** Een foutbudget waarop nooit wordt gehandeld wanneer het is uitgeput is slechts decoratie, en het moment van een uitval is het slechtste moment om het beleid van nul te onderhandelen. De concurrerende trek is echt: een toegezegde lancering, een omzetdeadline of een publieke aankondiging zal hard drukken tegen een bevriezing van riskante wijzigingen. Neem de verbrandingsdata mee, de vooraf afgesproken beleidstekst en een overzicht van de laatste keren dat het budget werd geschonden, zodat je kunt zien of de bevriezing werkelijk standhield. Voor een groot team stemt het budget prikkels alleen af als elke groep dezelfde afdwinging erft, dus besluit vooraf wie een override tekent en hoe die uitzondering wordt gelogd. In omgevingen van onderneming en overheid waar een SLA boetes of burgerimpact draagt wordt het overridespoor een auditartefact, dus noem de verantwoordelijke eigenaar nu in plaats van te improviseren wanneer het budget al weg is.

5. **Welk deel van de week van je SRE-team is sleurwerk, en is dat een gemeten getal of een gevoel?** Sleurwerk dat niemand telt breidt stilletjes uit tot het team al zijn tijd besteedt aan brandjes blussen en niets aan duurzame verbeteringen bouwen, precies de valstrik waaraan SRE moet ontsnappen. De spanning is dat sleurwerk meten zelf werk is, en engineers onder deadlinedruk zich verzetten tegen loggen waar hun uren heen gaan. Neem een eerlijke steekproef mee: een of twee weken gevolgde tijd tegen een gedeelde definitie van sleurwerk (handmatig, repetitief, automatiseerbaar, tactisch en meegroeiend met het systeem), plus de achterstand aan automatiseringsprojecten gerangschikt naar frequentie maal kosten. Voor een grote organisatie betekent een plafond van 50 procent alleen iets als het team voor team wordt gerapporteerd en verdedigd, dus spreek af wie het getal beoordeelt en wat er gebeurt wanneer een team het overschrijdt. In gereguleerde en overheidscontexten maakt sleurwerk begrenzen schaarse specialisten vrij voor het beheers- en auditwerk dat handmatig beheer verdringt, dus behandel het sleurwerkcijfer als capaciteitssignaal dat leiderschap zou moeten zien.

6. **Welk SRE-organisatiemodel draai je, en welk bewijs zou vertellen dat het niet meer past?** Een gecentraliseerd team geeft consistentie en gedeelde tooling maar kan een knelpunt worden. Een ingebed model geeft context maar drijft af naar inconsistentie. De hybride waarop de meeste grote organisaties uitkomen vraagt een helder engagementmodel anders erft ze de zwaktes van beide. Neem de signalen mee die spanning onthullen: hoe lang services op SRE-ondersteuning wachten, hoeveel betrouwbaarheidspraktijk tussen teams varieert en of ingebedde engineers zich afgesneden voelen van een professionele gemeenschap. Het juiste antwoord hangt af van bedrijfsgrootte, engineeringvolwassenheid en hoe uniform je services zijn, dus herzie het naarmate die veranderen in plaats van de eerste keuze als permanent te behandelen. Voor een onderneming of overheidsorgaan met veel teams en strikte uniformiteitseisen balanceert een centrale standaarden-en-platformgroep plus ingebedde betrouwbaarheidsengineers meestal consistentie tegen lokale context, maar alleen als het engagementmodel en de productiegereedheidslat zijn opgeschreven en iemand ze bezit.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen runway voor een speciaal betrouwbaarheidsteam kies je één enkele SLO op de gebruikersreis die het meest telt en deel je bereikbaarheid over het hele team. Leun op de beheerde services en ingebouwde bewaking van je cloudaanbieder in plaats van observeerbaarheidsinfrastructuur te bouwen, en schrijf korte nabeschouwingen in een gedeeld document zodat reparaties beklijven. Snelheid telt hier meer dan proces: een losse SLO die je werkelijk afdwingt verslaat een uitgebreide die niemand bekijkt.

**Kleinbedrijf.** Zonder specialist om betrouwbaarheid te draaien behandel je haar als discipline waarin je via je platform instapt: gehoste uptimebewaking, beheerde databases en statuspaginatooling in plaats van een maatwerkstack. Stel een of twee SLO's in gekoppeld aan de transacties die de rekeningen betalen, en besluit eerlijk welke falen je een klant zouden kosten. Koop veerkracht waar het goedkoper is dan bouwen, en houd de operationele last licht genoeg dat je bestaande engineers haar naast functiewerk kunnen dragen.

**Grote onderneming.** De uitdaging is consistentie over veel teams: een gedeeld SLO-vocabulaire, een gemeenschappelijk foutbudgetbeleid en een productiegereedheidslat die elke service haalt voordat SRE haar op bereikbaarheid neemt. Een centrale platform-en-standaardengroep plus ingebedde betrouwbaarheidsengineers houdt de praktijk uniform zonder een knelpunt te worden, en governance vraagt foutbudgetten overal op dezelfde manier gerapporteerd en afgedwongen. Begroot de observeerbaarheidsinfrastructuur en de automatiseringsinvestering expliciet, en beheer betrouwbaarheid als portfolio met statistieken die leiderschap kan zien.

**Overheid.** Publieke diensten dragen vaak gepubliceerde beschikbaarheidsdoelen, wettelijke verplichtingen en auditverplichtingen, dus SLO's en foutbudgetbeslissingen worden registraties die je aan toezichtsorganen verdedigt. Aanbestedingsregels kunnen beperken welke bewaking en hosting je mag gebruiken, en transparantieverwachtingen duwen je betrouwbaarheidsdata te publiceren op een publiek statusdashboard. Plan weken vooraf voor extreme seizoenspieken zoals belastingdeadlines en uitkeringsinschrijfvensters, en houd een schuldvrije nabeschouwingscultuur aan zodat publieke falen systeemverbetering drijven in plaats van individuele schuld.

## Voorbeelden

**Startup.** Een startup van tien personen draait één webapp en deelt bereikbaarheid over drie engineers. In plaats van een betrouwbaarheidsteam te bouwen dat ze niet kan betalen kiest ze één betekenisvolle SLO: 99,5 procent succes op de login-naar-dashboardstroom, gemeten uit echte gebruikersverzoeken. Wanneer een onbetrouwbare API van een derde het budget begint op te eten, besteedt het team een vrijdag aan een herpoging en een cache toevoegen in plaats van de volgende functie op te leveren, en schrijft dan een nabeschouwing van twee alinea's in een gedeeld document zodat de reparatie beklijft.

**Grote onderneming.** Een wereldwijd betalingsbedrijf stelt een beschikbaarheids-SLO van 99,99 procent in voor zijn transactie-API, wat een foutbudget geeft van ruwweg vier minuten per maand. Een centraal SRE-platformteam bezit gedeelde [observeerbaarheid](https://en.wikipedia.org/wiki/Observability_(software)), incidenttooling en het foutbudgetbeleid, terwijl ingebedde betrouwbaarheidsengineers binnen elke productgroep werken. Wanneer een nieuwe fraudedetectiefunctie in een week de helft van het maandbudget verbrandt, bevriest het vooraf afgesproken beleid niet-kritieke releases tot betrouwbaarheidswerk de ruimte herstelt. Bestuurders accepteren dit zonder debat, omdat ze het beleid vooraf bekrachtigden.

**Overheid.** Een nationale belastingdienst draait een online aangiftedienst met extreme seizoenspieken rond de jaarlijkse deadline. Haar SRE-team voorspelt vraag uit voorgaande jaren plus bevolkings- en beleidswijzigingen, test de belasting op meerdere malen de normale piek en provisioneert weken vooraf capaciteit. Publieke SLO's voor beschikbaarheid en paginalatentie gaan op een statusdashboard. Een schuldvrije [nabeschouwings](https://en.wikipedia.org/wiki/Postmortem_documentation)cultuur (falen beoordelen om systemen te verbeteren in plaats van individuele schuld toe te wijzen) en een automatiseringsmandaat snijden gestaag de handmatige ingrepen weg die ooit het aangifteseizoen domineerden, wat medewerkers vrijmaakt om het systeem te verbeteren in plaats van het door elke deadline te verplegen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van SRE komt uit drie bronnen: vermeden downtime, minder operationele arbeid en snellere veilige oplevering. Downtime voor een grote service kan duizenden tot miljoenen per uur kosten aan verloren omzet, boetes en herstel, dus zelfs bescheiden betrouwbaarheidswinst betaalt een team snel terug. Sleurwerk verminderen zet terugkerende handmatige kosten om in een eenmalige automatiseringsinvestering, zodat de total cost of ownership daalt naarmate schaal groeit in plaats van mee te klimmen. Foutbudgetten laten het bedrijf sneller opleveren wanneer betrouwbaarheid gezond is, de functiewaarde vangend die overdreven voorzichtig beheer zou laten liggen.

De adoptiekosten zijn echt. SRE vraagt bekwame engineers, observeerbaarheidsinfrastructuur en cultuurverandering die met functiedeadlines strijdt. Maar de kosten van niet adopteren zijn op schaal hoger: onbegrensde operationele bezetting, onvoorspelbare uitval, burn-out en verloop van personeel en reputatieschade die moeilijk te kwantificeren maar makkelijk te lijden is. Maak de zaak voor leiderschap door SRE te formuleren als risicobeheer met meetbare opbrengsten. Presenteer de huidige kosten van incidenten en handmatige operaties, de SLO-doelen gekoppeld aan bedrijfsverplichtingen en de geprojecteerde vermindering van beide. Veranker het argument op het foutbudget als governancetool dat leiderschap een hefboom geeft over de afweging tussen betrouwbaarheid en snelheid.

## Antipatronen en valkuilen

- **SRE als herdoopt beheer.** Een ops-team hernoemen zonder de engineeringtijd, het automatiseringsmandaat en het gezag om terug te duwen verandert niets.
- **Mikken op 100 procent.** Perfecte betrouwbaarheid najagen verspilt geld en blokkeert oplevering voor winst die gebruikers niet kunnen waarnemen.
- **IJdele SLI's.** Server-CPU meten in plaats van voor de gebruiker zichtbaar succes geeft getallen die goed ogen terwijl gebruikers lijden.
- **Foutbudgetten zonder tanden.** Een budget dat nooit wordt afgedwongen wanneer het is uitgeput is slechts decoratie.
- **Sleurwerk zonder meting.** Als je sleurwerk niet volgt, verbruikt het stilletjes het team tot er geen verbeterwerk meer gebeurt.
- **SRE als stortplaats.** Gecentraliseerde teams die elke onstabiele service erven zonder gereedheidslat verdrinken in andermans technische schuld.
- **Capaciteitsdoorlooptijden negeren.** Aannemen dat cloudelasticiteit direct en oneindig is nodigt tekorten uit tijdens precies de pieken die het meest tellen.

## Volwassenheidsmodel

**Niveau 1, Initiëren.** Beheer is handmatig en reactief. Er zijn geen formele SLO's, betrouwbaarheid is een kwestie van mening en dezelfde incidenten keren terug terwijl brandjes blussen domineert. Enige automatisering is incidenteel, en niemand bezit betrouwbaarheid als engineeringzorg.

**Niveau 2, Ontwikkelen.** Sommige services hebben basis-SLI's en -SLO's en rudimentaire bewaking en alarmering, maar de praktijk varieert sterk tussen teams. Sleurwerk wordt erkend maar niet gemeten, automatisering is ad hoc en nabeschouwingen gebeuren inconsistent. Betrouwbaarheid verbetert in de zakken waar individuen haar duwen, niet omdat de organisatie het vereist.

**Niveau 3, Standaardiseren.** SLI's, SLO's en een foutbudgetbeleid zijn gedocumenteerd en consistent over teams toegepast. Sleurwerk is gedefinieerd en gevolgd, capaciteitsplanning is routine, een SRE-engagementmodel met productiegereedheidsreviews bestaat en automatisering is een gefinancierde werkstroom in plaats van een bijproject. Betrouwbaarheidspraktijk is opgeschreven en organisatiebreed afgedwongen.

**Niveau 4, Beheersen.** Het betrouwbaarheidsprogramma wordt gemeten en beheerst met data tegen uitgangswaarden. Verbrandingssnelheid van het foutbudget, sleurwerkpercentage, SLO-behaling, gemiddelde hersteltijd en doorlooptijden van provisioning worden als statistieken gevolgd, volgens vast ritme beoordeeld en gebruikt om teams aan hun doelen te houden. Budgetschendingen triggeren de afgesproken bevriezing, capaciteit wordt voorspeld tegen vraagmodellen en elke go/no-go-beslissing rust op bewijs in plaats van mening.

**Niveau 5, Orkestreren.** Betrouwbaarheidsengineering is over de organisatie geïntegreerd en wordt continu verbeterd. Foutbudgetbeleid is geautomatiseerd en wordt overal gerespecteerd, de meeste operaties zijn self-service, capaciteit wordt proactief geprovisioneerd en betrouwbaarheidsdata drijft adaptieve afwegingen tussen snelheid en stabiliteit. De organisatie bakent SLO's routinematig opnieuw af, schaft sleurwerk af en herbalanceert betrouwbaarheidsinvestering naarmate het bedrijf en het risicobeeld verschuiven.

## Ideeën voor discussie

- Hoe moet een organisatie haar eerste SLO's stellen wanneer ze geen historische betrouwbaarheidsdata heeft om ze aan te verankeren?
- Wanneer het foutbudget is uitgeput maar een grote lancering is toegezegd, wie heeft het gezag de bevriezing te overrulen, en hoe wordt die beslissing vastgelegd?
- Is een gecentraliseerd, ingebed of hybride SRE-model juist voor jouw organisatie, en wat zou een verandering triggeren?
- Hoe waardeer je een extra negen beschikbaarheid tegen de functies die dezelfde investering kon financieren?
- Wat telt in jouw context als sleurwerk, en waar ligt de lijn tussen waardevol handmatig oordeel en elimineerbare herhaling?
- Hoe moeten betrouwbaarheidsdoelen verschillen tussen burgergerichte overheidsdiensten en interne ondernemingstools?

## Belangrijkste inzichten

- SRE past software-engineering toe op beheer en behandelt betrouwbaarheid als meetbare, financierbare functie.
- SLI's, SLO's en SLA's zetten betrouwbaarheid om van mening in afgesproken getallen. Houd SLO's strikter dan SLA's.
- Het foutbudget stemt ontwikkelaars en beheerders af door de afweging tussen betrouwbaarheid en snelheid expliciet en vooraf onderhandeld te maken.
- Meet en begrens sleurwerk, en behandel automatisering als eersterangs engineering zodat beheer sublineair schaalt.
- Plan capaciteit uit vraagvoorspellingen en respecteer doorlooptijden van provisioning, vooral voor seizoenspieken.
- Kies een SRE-organisatiemodel bewust en definieer een helder engagement- en productiegereedheidsniveau.

## Referenties en verder lezen

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
