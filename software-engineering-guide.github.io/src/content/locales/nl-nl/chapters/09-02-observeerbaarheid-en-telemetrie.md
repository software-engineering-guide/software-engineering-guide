# 9.2 Observeerbaarheid en telemetrie

## Overzicht en motivatie

[Telemetrie](https://en.wikipedia.org/wiki/Telemetry) is de data die een systeem uitzendt over haar eigen gedrag: de statistieken, logs, traces en gebeurtenissen die uit draaiende software worden verzameld. Bewaking beantwoordt vragen waarvan je al wist dat je ze moest stellen, op basis van die telemetrie. Is de schijf vol? Ligt het foutpercentage boven een drempel? Is de service up? [Observeerbaarheid](https://en.wikipedia.org/wiki/Observability_(software)) is breder. Het is het vermogen om nieuwe vragen te stellen over de interne toestand van een systeem van buitenaf, zonder nieuwe code uit te leveren, zodat je gedrag begrijpt dat je nooit had voorzien. Naarmate systemen uitgroeien tot gedistribueerde, [microservice](https://en.wikipedia.org/wiki/Microservices)- en [gebeurtenisgedreven architecturen](https://en.wikipedia.org/wiki/Event-driven_architecture), zijn de falen die het meest pijn doen degene die niemand zag aankomen, en observeerbaarheid is wat je ze laat debuggen. Bewaking vertelt je dát er iets mis is. Observeerbaarheid helpt je uitzoeken waaróm.

Voor grote teams is dit onderscheid beslissend. Een monoliet kon je begrijpen door logs op één machine te lezen. Een modern platform omspant honderden services, veel teams, meerdere regio's en afhankelijkheden van derden, waar één gebruikersverzoek tientallen componenten kan raken. Niemand houdt het hele systeem in zijn hoofd. Gedeelde telemetrie van hoge kwaliteit wordt het bindweefsel dat elke engineer een verzoek over grenzen laat volgen, symptomen over services heen laat uitlijnen en laat redeneren over een systeem dat niemand volledig bezit. Zonder dat slepen incidenten voort, vliegt de schuld tussen teams heen en weer en blijven grondoorzaken verborgen.

Systemen van onderneming en overheid verhogen de inzet met compliance, controleerbaarheid en publieke verantwoording. Toezichthouders kunnen bewijs eisen van wie wanneer bij wat kwam. Beveiligingsteams hebben telemetrie nodig om inbraken te detecteren. Burgergerichte diensten moeten laten zien dat ze hun gepubliceerde prestatietoezeggingen halen. Goede observeerbaarheid dient dit alles tegelijk: het is een engineeringtool, een beveiligingsmaatregel en een verantwoordingsmechanisme in één. Standaardiseren op open instrumentatie voorkomt afhankelijkheid van de eigen agents van één leverancier, wat enorm telt wanneer systemen decennia moeten meegaan en aanbestedingscycli moeten overleven.

*Zie ook:* hoofdstuk 9.1 (site reliability engineering en SLO's), hoofdstuk 9.3 (incidentmanagement) en hoofdstuk 3.3 (gedistribueerde systemen).

## Kernprincipes

- **Instrumenteer voor onbekende vragen.** Ontwerp telemetrie zodat je nieuwe falen kunt onderzoeken, voorbij degene die je voorspelde.
- **Drie pijlers, één verhaal.** Statistieken, logs en traces zijn complementaire gezichtspunten. Hun waarde vermenigvuldigt zich wanneer ze gecorreleerd zijn, niet gescheiden.
- **Structureer alles.** Gestructureerde, machineleesbare telemetrie verslaat vrije tekst die alleen mensen kunnen lezen.
- **Correleer met gedeelde identifiers.** Overal doorgegeven trace- en verzoek-ID's laten je één gebeurtenis over services heen aan elkaar naaien.
- **Alarmeer op symptomen, niet op oorzaken.** Roep mensen op voor voor de gebruiker zichtbare problemen. Laat dashboards en onderzoek de onderliggende oorzaak boven water brengen.
- **Elke oproep moet uitvoerbaar zijn.** Een alarm dat geen menselijke actie vraagt is ruis die vertrouwen erodeert en vermoeidheid veroorzaakt.
- **Hoge kardinaliteit is een functie.** Het vermogen om te segmenteren op gebruiker, verzoek, regio en versie maakt debuggen in productie mogelijk.
- **Bezit je instrumentatie.** Standaardiseer op open, leveranciersneutrale telemetrie zodat je je data beheert en van backend kunt wisselen.

## Aanbevelingen

### Bouw op de drie pijlers en verder

**Statistieken** zijn numerieke tijdreeksen, goedkoop op te slaan en ideaal voor dashboards, trends en alarmdrempels. **Logs** zijn losse, van tijdstempel voorziene registraties van gebeurtenissen, rijk aan detail en essentieel voor forensisch onderzoek. **[Traces](https://en.wikipedia.org/wiki/Tracing_(software))** volgen één verzoek terwijl het door services beweegt en tonen latentie en afhankelijkheden over de gedistribueerde aanroepgraaf. Daarnaast kun je **gebeurtenissen** overwegen (betekenisvolle toestandswijzigingen zoals deploys), **profielen** (waar code CPU en geheugen besteedt) en **[real user monitoring](https://en.wikipedia.org/wiki/Real_user_monitoring)** van de werkelijke clientervaring. Geen enkele pijler is op zichzelf genoeg. Het doel is vloeiend tussen ze te bewegen tijdens een onderzoek.

### Standaardiseer op OpenTelemetry en gestructureerde logging

Neem [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) aan als leveranciersneutrale standaard voor het genereren en verzamelen van statistieken, logs en traces. Het scheidt instrumentatie van de analysebackend, zodat je van leverancier kunt wisselen zonder honderden services opnieuw te instrumenteren. Die eigenschap is cruciaal voor langlevende systemen van onderneming en overheid. Zend logs uit als gestructureerde records (bijvoorbeeld JSON) met consistente veldnamen voor tijdstempel, ernst, service en identifiers. Geef een trace- of correlatie-ID van de rand door aan elke downstreamaanroep en neem het op in elke logregel en statistiek-exemplar, zodat de drie pijlers automatisch aan elkaar koppelen.

### Ontwerp alarmering voor uitvoerbaarheid en weinig ruis

Je alarmeringsfilosofie bepaalt of bereikbaarheid houdbaar is. Alarmeer vooral op symptomen die gebruikers voelen, uitgedrukt als verbrandingssnelheden van SLO's ([service level objectives](https://en.wikipedia.org/wiki/Service-level_objective)). Roep op wanneer je je foutbudget (de toegestane afwijking van die doelstelling) snel genoeg verbrandt om het te schenden, met alarmen op verbrandingssnelheid over meerdere vensters om snelle detectie tegen valse alarmen af te wegen. Reserveer oproepen voor problemen die directe menselijke actie vragen en stuur al het andere naar tickets of dashboards. Snoei alarmen die afgaan zonder actie te vereisen genadeloos, want alarmmoeheid is een belangrijke oorzaak van gemiste echte incidenten en burn-out bij bereikbaarheid. Elk alarm moet naar een runbook verwijzen.

### Modelleer gezondheid met dashboards en SLO-bewaking

Bouw dashboards rond een helder gezondheidsmodel, niet een muur van elke statistiek die je hebt. Een goed startkader zijn de "vier gouden signalen": latentie, verkeer, fouten en verzadiging. Maak dashboards op serviceniveau die SLO-status en resterend foutbudget in één oogopslag tonen, plus dashboards op hoger niveau die de algehele systeem- en gebruikersreisgezondheid modelleren. Cureer ze bewust, want dashboards die alles tonen communiceren niets. Houd ze dicht bij de alarmen en runbooks, zodat responders snel van signaal naar context naar actie bewegen.

### Maak debuggen in productie mogelijk met hoge kardinaliteit

De moeilijkste productieproblemen raken een smalle plak: één klant, één regio, één API-versie, één apparaattype. Om ze te onderzoeken heb je telemetrie met **hoge kardinaliteit** nodig, het vermogen te groeperen en filteren op velden met veel verschillende waarden zoals gebruikers-ID of verzoek-ID. Brede, rijk geattribueerde gebeurtenissen die veel dimensies per record dragen laten je achteraf willekeurige vragen stellen. Houd genoeg kardinaliteit en samplingtrouw om uitschieters te isoleren, en geef de voorkeur aan traces gekoppeld aan exemplars zodat een piek op een statistiek je recht naar representatieve trage verzoeken leidt.

### Beheer kosten, bewaring en sampling

Telemetrievolume groeit met het systeem en kan een grote uitgave worden. Stel bewaarbeleid in per dataklasse: bewaar data met hoge resolutie kort en aggregaten langer. Pas slimme sampling toe op traces, vertekend naar het behouden van fouten en trage verzoeken, zodat je de interessante staart vasthoudt zonder te betalen voor elk routinesucces. Beoordeel je telemetrieuitgaven regelmatig, want onbeheerde observeerbaarheidskosten kunnen de infrastructuur die ze observeren evenaren.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Gebeurtenissen met hoge kardinaliteit | Krachtig debuggen, vraag alles | Hogere opslag- en querykosten |
| Agressieve sampling | Lagere kosten, minder ruis | Kan zeldzame gebeurtenissen missen |
| Alarmering op symptomen | Minder, uitvoerbare oproepen | Heeft goede SLO's nodig om goed te werken |
| OpenTelemetry-standaard | Leveranciersneutraal, overdraagbaar | Migratie-inspanning, rijpende tooling |
| Lange logbewaring | Betere forensiek en audit | Opslagkosten, privacyblootstelling |

Observeerbaarheidsbeslissingen komen neer op een spanning tussen trouw en kosten. Alles op volledige resolutie vastleggen geeft je perfect achteraf inzicht, maar op schaal is het onbetaalbaar. Snijd agressief en je bespaart geld, maar je gooit mogelijk het ene record weg dat een uitval had verklaard. Sampling en bewaarlagen zijn hoe volwassen teams deze lijn lopen: fouten en uitschieters behouden terwijl routinedata wordt uitgedund. De alarmeringsafweging is tussen gevoeligheid en ruis: te veel alarmen veroorzaken vermoeidheid en gemiste incidenten, te weinig laten problemen etteren. Alarmering op symptomen gedreven door SLO's lost veel hiervan op, maar alleen als je betekenisvolle SLO's hebt.

## Vragen om met je team te bespreken

1. **Wat is je plan om legacyservices naar OpenTelemetry te verplaatsen, en hoe voorkom je dat je tijdens de overgang voor twee instrumentatiestacks betaalt?** Leveranciersneutrale instrumentatie is de eigenschap die je van backend laat wisselen zonder honderden services opnieuw te instrumenteren, en ze telt het meest voor de langlevende systemen van onderneming en overheid die elk enkel leverancierscontract overleven. De migratie is waar goede bedoelingen vastlopen: half geïnstrumenteerde landschappen laten gaten precies waar een verzoek van een nieuwe naar een oude service gaat, waardoor de end-to-endtrace breekt. Neem een inventaris mee: welke services zenden data van eigen agents uit, welke OpenTelemetry en waar tracecontext bij de grens wegvalt. Besluit een volgorde die echte verzoekpaden volgt in plaats van organigrammen, en begroot het venster waarin je beide collectors draait. Het antwoord bepaalt of je je telemetrie werkelijk bezit of aan de agents van één leverancier vastzit.

2. **Wanneer heb je voor het laatst elk alarm op uitvoerbaarheid doorgelicht, en hoeveel oproepen vorige maand vroegen geen menselijke actie?** Alarmmoeheid is een belangrijke oorzaak van gemiste echte incidenten en burn-out bij bereikbaarheid, dus een oproep die geen actie vraagt is geen onschuldige ruis, maar erodeert actief de respons waarvan je afhangt. Neem de bewijzen mee: haal de oproepen van vorige maand op, markeer elk als opgevolgd of genegeerd en tel hoeveel naar een runbook verwezen. Voor een groot team over veel services desensibiliseert lawaaierige alarmering van één team de gedeelde bereikbaarheid voor iedereen. Stel een standaard dat elke oproep naar een runbook verwijst en aan een SLO-verbrandingssnelheid is gekoppeld, en verwijder de rest genadeloos. Het resultaat van deze audit moet je oproepvolume direct verlagen en je vertellen welke services geen betekenisvolle SLO achter hun alarmen hebben.

3. **Wat is je tracesamplingstrategie, en hoe zeker ben je dat ze de fouten en de trage staart behoudt?** Telemetrievolume groeit met het systeem en onbeheerde observeerbaarheidskosten kunnen de geobserveerde infrastructuur evenaren, dus je gaat samplen, en de vraag is of je slim samplet. Kardinaliteit strippen of blind samplen verwijdert precies de records die nodig zijn om de smalle problemen te debuggen die één klant, één regio of één API-versie raken. Neem je huidige bewaarlagen en samplingregels mee: vertek je naar het behouden van fouten en trage verzoeken, met aan exemplars gekoppelde traces zodat een statistiekpiek tot een representatief traag verzoek leidt? Verzoen voor gecontroleerde en privacygebonden systemen bewaring met dataminimalisatieregels zodat je geen persoonsgegevens hamstert om te debuggen. Het antwoord bepaalt waar je telemetriebudget naartoe gaat en of je volgende zware uitval verklaarbaar is of een mysterie.

4. **Welke van je SLO's zijn echte gebruikersreistoezeggingen, en welke zijn proxystatistieken die niemand buiten het eigenaarsteam gelooft?** Alarmering op symptomen werkt alleen als de symptomen overeenkomen met wat gebruikers werkelijk voelen, dus een alarm gekoppeld aan een CPU-drempel of een verzonnen beschikbaarheidsdoel roept mensen op voor problemen die er mogelijk niet toe doen terwijl het zwijgt over degene die dat wel doen. Voor een grote organisatie zijn SLO's ook het contract waarmee onafhankelijke teams een bereikbaarheidsrooster kunnen delen zonder tijdens elk incident de ernst opnieuw te bepleiten. Neem de huidige SLO-catalogus mee, de gebruikersreis die elke doelstelling moet beschermen en de schendingen van het laatste kwartaal met of klanten werkelijk klaagden. Koppel in omgevingen van onderneming en overheid de zichtbaarste SLO's aan de gepubliceerde prestatietoezeggingen waaraan de dienst wordt gehouden, zodat hetzelfde verbrandingssignaal dat een engineer oproept ook het bewijs is dat je een toezichthouder of toezichtsorgaan toont. De discussie moet de proxystatistieken laten vallen en je een korte lijst doelstellingen overlaten die een niet-engineer zou herkennen als beloftes aan gebruikers.

5. **Wie bezit de governance van telemetriedata, en kun je bewijzen dat persoonsgegevens worden gewist voordat ze in je observeerbaarheidsbackend landen?** Gebeurtenissen met hoge kardinaliteit en lange logbewaring zijn precies de functies die debuggen mogelijk maken, en precies degene die een observeerbaarheidsopslag omzetten in een onbeheerde kopie van de persoonsgegevens van je gebruikers. De concurrerende trek is echt: engineers willen rijkere attributen en langere bewaring, terwijl privacy en juridische zaken dataminimalisatie en korte levensduur willen. Neem een datastroomkaart mee die toont welke velden persoonlijke of gevoelige data dragen, waar redactie of tokenisatie in de pijplijn plaatsvindt en wat je bewaarlagen per dataklasse zijn. Noem voor gereguleerde en publieke systemen de verantwoordelijke eigenaar, koppel bewaring aan de rechtsgrond en de dataminimalisatieregels waaronder je opereert en wees klaar een auditor te tonen dat toegang tot de telemetrie zelf wordt gelogd en beheerst. Het antwoord bepaalt of je observeerbaarheidsplatform een bezit is of een permanente inbreuk die ontdekt wil worden.

6. **Wanneer een incident de services van meerdere teams doorkruist, laat je telemetrie één responder het verzoek end-to-end volgen, of breekt het spoor bij elke eigenaarsgrens?** De hele belofte van gecorreleerde, ID-doorgevende telemetrie is dat één engineer kan redeneren over een systeem dat niemand volledig bezit, en die belofte stort in precies op de grens waar tracecontext wegvalt of waar twee teams incompatibele identifiers en tools gebruiken. Weeg de trek naar autonomie per team bij het kiezen van observeerbaarheidstooling tegen de gedeelde kosten van een gefragmenteerd landschap waar elke overdracht tijdens een uitval een doodlopende weg is. Neem een recente tijdlijn van een teamoverstijgend incident mee en markeer waar de responder de draad verloor, plus een inventaris van welke services een gemeenschappelijk correlatie-ID doorgeven en welke niet. Besluit voor een grote onderneming of een overheidsplatform samengesteld uit veel leveranciers en langlevende systemen hoeveel je centraal oplegt, een gedeelde tracecontextstandaard en een gemeenschappelijk ID-schema, tegenover wat je aan teams overlaat, want de componenten die je over decennia opnieuw aanbesteedt moeten nog steeds op hetzelfde verzoek samenwerken. Het antwoord vertelt je of je volgende incident met meerdere teams een gecoördineerd onderzoek is of een ronde vingerwijzen.

## Sectorperspectief

**Startup.** Met een handvol services en geen vrije handen instrumenteer je vanaf dag één met OpenTelemetry en lever je gestructureerde JSON-logs met één verzoek-ID end-to-end. Die kleine investering zet "de app is traag" om in een trace die je kunt lezen, en houdt je vrij later van een gratis laag naar een betaalde backend te gaan zonder opnieuw te instrumenteren. Sla uitgebreide dashboards en SLO-machinerie over tot je gebruikers hebt wier ervaring je werkelijk kunt meten.

**Kleinbedrijf.** Je hebt geen observeerbaarheidsspecialist en een krap budget, dus leun op een beheerde backend waar instrumentatie, opslag en dashboards gebundeld komen in plaats van je eigen stack samen te stellen. De koop-of-bouwkeuze valt hier bijna altijd op kopen. Je schaarse aandacht is beter besteed aan de twee of drie gouden-signaalalarmen die vertellen dat de service down is dan aan het draaien van een telemetriepijplijn. Stel een harde bewaarlimiet in zodat telemetriekosten niet stilletjes de bewaakte infrastructuur inhalen.

**Grote onderneming.** Het werk is governance over veel teams: een gedeelde OpenTelemetry-standaard, een gemeenschappelijk correlatie-ID-schema en gecureerde SLO-dashboards zodat één responder een verzoek over tientallen services kan volgen. Beheer telemetrie als kostenpost met bewaarlagen en samplingbeleid, standaardiseer alarmering op SLO-verbrandingssnelheden om een gedeelde bereikbaarheid houdbaar te houden en snoei lawaaierige alarmen centraal zodat de vermoeidheid van één team niet iedereen desensibiliseert. Behandel de instrumentatielaag als leveranciersneutrale infrastructuur die elk enkel backendcontract overleeft.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven het ontwerp vorm. Standaardiseer op open instrumentatie zodat een systeem dat decennia moet draaien herbesteding aan andere leveranciers overleeft zonder gegijzeld te worden door eigen agents, en eis die overdraagbaarheid in het contract. Gebruik gestructureerde auditlogs om te tonen wie welk record wanneer opende, wis of tokeniseer persoonsgegevens voordat ze de telemetrieopslag bereiken en verzoen bewaring met dataminimalisatiewetgeving. Publiceer SLO-dashboards voor burgergerichte diensten zodat dezelfde signalen die je engineers bekijken zichtbaar bewijs zijn van de toezeggingen waaraan je wordt gehouden.

## Voorbeelden

**Startup.** Een startup van vier personen levert een mobiele backend en krijgt steeds vage klachten dat de app traag is die ze niet kan reproduceren. Het team voegt OpenTelemetry toe aan zijn handvol services en schakelt over op gestructureerde JSON-logs met een verzoek-ID dat van de app door elke hop wordt meegedragen. De volgende meldingen over traagheid zijn in minuten opgelost: één trace toont een ontbrekende database-index op de orderstabel onder een specifieke query. Omdat ze vroeg voor open instrumentatie kozen, stappen ze later van een gratis laag naar een betaalde backend over zonder iets opnieuw te instrumenteren.

**Grote onderneming.** Een groot e-commerceplatform instrumenteert elke service met OpenTelemetry en geeft een trace-ID door van de browser van de klant door afrekenen, betaling, voorraad en verzending. Wanneer de conversie daalt, begint een engineer in bereikbaarheid vanuit een SLO-verbrandingssnelheidsalarm, opent de gouden signalen van het afrekendashboard, ziet verhoogde latentie in één regio en volgt een exemplar-trace naar een trage databaseaanroep in één service. Attributen met hoge kardinaliteit tonen dat het probleem beperkt is tot één productcategorie, wat in minuten in plaats van uren een gerichte reparatie stuurt.

**Overheid.** Een nationale gezondheidsdienst draait een patiëntendossierplatform onder strikte audit- en privacyregels. Gestructureerde logs leggen vast wie welk record wanneer opende, wat zowel beveiligingsbewaking als compliancerapportage voedt, terwijl persoonlijk identificeerbare velden in telemetrie worden gewist of getokeniseerd. Publieke SLO-dashboards tonen beschikbaarheid en latentie voor burgergerichte afspraakboeking. Door op open instrumentatie te standaardiseren vermijdt het agentschap afhankelijkheid van eigen oplossingen in een systeem dat decennia moet draaien en tijdens zijn leven door verschillende leveranciers opnieuw wordt aanbesteed.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het belangrijkste rendement van observeerbaarheid is een dramatische daling van de tijd die het kost incidenten te detecteren en op te lossen. Voor een service waar downtime duur is betaalt de gemiddelde oplostijd terugbrengen van uren naar minuten de tooling vele malen terug in één groot incident. Observeerbaarheid bespaart ook de engineeringtijd die je anders zou besteden aan gokken, bugs reproduceren en ruziën over welk team de schuld heeft, en verkort de feedbacklus waarmee teams met vertrouwen opleveren. De beveiligings- en compliancewaarde is ook echt: dezelfde telemetrie ondersteunt inbraakdetectie en auditbewijs.

De total cost of ownership omvat instrumentatie-inspanning, telemetrieopslag en querykosten en de discipline om signaal uit ruis te cureren. Deze kosten zijn zichtbaar en terugkerend, wat leiderschap verleidt tot onderinvestering. De kosten van niet adopteren zijn groter maar moeilijker te zien: langdurige uitval, ongediagnosticeerde prestatieproblemen, beveiligingsincidenten die laat of nooit worden gevonden en engineers die opbranden op alarmen waar ze niets aan kunnen doen. Maak de zaak met concrete incidentdata. Toon de oplostijd en bedrijfsimpact van recente uitval en projecteer de vermindering die betere telemetrie zou leveren. Observeerbaarheid formuleren als verzekering die ook oplevering versnelt, in plaats van als zuivere kostenpost, wint het argument.

## Antipatronen en valkuilen

- **Alarmeren op alles.** Oproepen voor elke afwijking traint responders alarmen te negeren, zodat echte incidenten ontsnappen.
- **Oproepen op oorzaken.** Alarmeren op interne oorzaken in plaats van gebruikerssymptomen overspoelt bereikbaarheid met ruis en mist nieuwe falen.
- **Ongestructureerde logs.** Vrije-tekstlogs die niet te bevragen of te correleren zijn dwingen tot traag, handmatig grep'pen tijdens incidenten.
- **Drie gescheiden pijlers.** Statistieken, logs en traces in losse tools zonder gedeelde ID's verhinderen een gebeurtenis end-to-end te volgen.
- **Dashboardwildgroei.** Honderden ongecureerde dashboards betekenen dat niemand weet welk toont of het systeem gezond is.
- **Kardinaliteitsineenstorting.** Velden met hoge kardinaliteit strippen om kosten te besparen verwijdert precies de data die nodig is om smalle problemen te debuggen.
- **Leveranciersafhankelijkheid.** Eigen agents overal maken van backend wisselen onbetaalbaar en houden je data gegijzeld.

## Volwassenheidsmodel

**Niveau 1, Initiëren.** Observeerbaarheid is ad hoc en reactief. Basale uptimecontroles en ongestructureerde logs leven op individuele machines, debuggen betekent op servers inloggen om te grep'pen en er is geen gedeelde telemetrie. Alarmen zijn lawaaierig, oorzaakgebaseerd en vaak genegeerd, dus echte incidenten komen aan het licht via gebruikersklachten in plaats van signalen.

**Niveau 2, Ontwikkelen.** Basispraktijken verschijnen maar variëren per team. Sommige services pushen statistieken en logs naar een centrale plek, een paar dashboards en drempelalarmen bestaan, maar logs zijn slechts half gestructureerd en traces ontbreken of zijn gedeeltelijk. Correlatie over services is handmatig, en of een engineer een verzoek end-to-end kan volgen hangt af van welke teams toevallig betrokken zijn.

**Niveau 3, Standaardiseren.** Instrumentatie is gedocumenteerd en organisatiebreed afgedwongen. OpenTelemetry over services met een doorgegeven trace- of correlatie-ID, gestructureerde logging met consistente veldnamen, gedistribueerde tracing, gecureerde gouden-signaaldashboards en SLO-gebaseerde symptoomalarmering zijn de standaard die elk team volgt. Elke oproep verwijst naar een runbook en is aan een SLO gekoppeld, en bereikbaarheid is houdbaar in plaats van een bron van burn-out.

**Niveau 4, Beheersen.** Het observeerbaarheidslandschap zelf wordt gemeten en beheerst tegen uitgangswaarden. Je volgt instrumentatiedekking en tracecontextdoorgifte over services, het aandeel oproepen dat werd opgevolgd tegenover genegeerd, gemiddelde tijd tot detecteren en oplossen, SLO-behaling en foutbudgetverbranding en telemetriekosten per service tegen een budget. Gaten en alarmruis worden met data naar expliciete doelen teruggedrongen, samplingtrouw wordt geverifieerd zodat de fout- en trage-staartrecords overleven, en go/no-go-beslissingen over dekking en bewaring worden op bewijs genomen in plaats van mening.

**Niveau 5, Orkestreren.** Observeerbaarheid wordt continu verbeterd en over de organisatie geïntegreerd. Gebeurtenisrijke telemetrie met hoge kardinaliteit maakt ad-hoconderzoek van elke plak mogelijk, alarmering wordt gedreven door SLO-verbrandingssnelheid met minimale ruis en sampling en bewaring passen zich aan veranderende kosten en risico aan. Telemetrie voedt capaciteitsplanning, beveiligingsdetectie en productbeslissingen als routine, en het platform stemt haar eigen signalen, budgetten en dekking opnieuw af naarmate het systeem, het dreigingsbeeld en de wettelijke verplichtingen verschuiven.

## Ideeën voor discussie

- Waar ligt de juiste balans tussen telemetrietrouw en kosten voor je meest kritieke services?
- Hoe beslis je wat een oproep verdient tegenover een ticket tegenover alleen een dashboardvermelding?
- Wat is je strategie voor het doorgeven van correlatie-ID's over teams die geen codebasis of releasecyclus delen?
- Hoe behoud je het debugvermogen van hoge kardinaliteit en voldoe je aan privacy- en dataminimalisatie-eisen?
- Moet observeerbaarheidstooling centraal worden opgelegd of per team gekozen, en wat zijn de gevolgen elke kant op?
- Hoe zou je auditors aantonen dat je telemetrie compleet en manipulatiebestendig is?

## Belangrijkste inzichten

- Bewaking detecteert bekende problemen. Observeerbaarheid laat je onbekende onderzoeken zonder nieuwe code uit te leveren.
- Statistieken, logs en traces zijn het waardevolst wanneer ze via gedeelde identifiers zijn gecorreleerd, niet gescheiden.
- Standaardiseer op OpenTelemetry en gestructureerde logging om leveranciersneutraal en overdraagbaar te blijven over lange systeemlevens.
- Alarmeer op voor de gebruiker zichtbare symptomen via SLO-verbrandingssnelheden, maak elke oproep uitvoerbaar en snoei ruis onophoudelijk.
- Cureer dashboards rond een helder gezondheidsmodel zoals de gouden signalen in plaats van elke statistiek te tonen.
- Gebeurtenisrijke telemetrie met hoge kardinaliteit maakt het debuggen van smalle productieproblemen mogelijk.

## Referenties en verder lezen

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
