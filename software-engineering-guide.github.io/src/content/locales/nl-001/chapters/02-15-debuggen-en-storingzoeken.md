# 2.15 Debuggen en storingzoeken

## Overzicht en motivatie

Debuggen is het gedisciplineerde werk uitzoeken waarom een systeem iets doet wat het niet zou moeten doen, en storingzoeken (troubleshooting) is dezelfde vaardigheid toegepast op een draaiend productiesysteem onder tijdsdruk. Beide zijn de [wetenschappelijke methode](https://en.wikipedia.org/wiki/Scientific_method) toegepast op defecten: je observeert een verrassend gedrag, vormt een hypothese over de oorzaak, ontwerpt een experiment dat haar zou bevestigen of weerleggen en laat het bewijs, niet je gevoel, bepalen wat je wijzigt. Zo gedaan is debuggen een leerbare, onderwijsbare engineeringvaardigheid. Als folklore wordt het bijgeloof: willekeurige regels veranderen, servers herstarten en hopen.

Voor een groot team is het verschil duur. Eén moeilijk defect kan engineers over meerdere services binnentrekken, uren bereikbaarheidsdienst opslokken en een release stilleggen. Wanneer iedereen op instinct debugt, stapelt die inspanning zich niet op, want niemand kan reproduceren of uitleggen wat een ander probeerde. Wanneer het team een methode deelt (eerst reproduceren, isoleren door te zoeken, de bug vastleggen in een falende test, dan repareren), verandert dezelfde inspanning in een herhaalbaar proces en een groeiende regressiesuite. Debuggen sluit nauw aan op teststrategie (hoofdstuk 2.4), softwarekwaliteit (hoofdstuk 2.11) en de constructiegewoonten (hoofdstuk 2.9) die code überhaupt diagnosticeerbaar maken.

In omgevingen van onderneming en overheid stijgt de inzet. Defecten in ondernemingen overschrijden service- en teamgrenzen, dus degene die het symptoom ziet is zelden degene die de oorzaak bezit. Overheidssystemen voegen beperkingen toe die de meeste engineers nooit tegenkomen: air-gapped of beperkte omgevingen waar je geen debugger aan productie kunt koppelen, reproduceerbare builds die uit artefacten moeten worden gediagnosticeerd en auditsporen die moeten vastleggen wat je veranderde en waarom. In alle drie is het doel hetzelfde: gokken vervangen door bewijs.

## Kernprincipes

- **Reproduceer voordat je theoretiseert.** Een bug die je niet op verzoek kunt triggeren is een gerucht, geen defect.
- **Debuggen is hypothesen testen.** Zeg wat je gelooft en ontwerp dan het goedkoopste experiment dat je ongelijk zou kunnen bewijzen.
- **Lees eerst de fout en de stacktrace.** Het systeem vertelt je meestal waar het brak voordat je een regel verandert.
- **Doorzoek de probleemruimte, scan haar niet.** Halveer bij elke stap het verdachte gebied in plaats van van boven naar beneden te lezen.
- **Reduceer tot het minimum.** Strip het geval tot alleen de essentiële trigger overblijft.
- **Eén wijziging tegelijk.** Hagelschot-bewerkingen vernietigen het bewijs dat je had verteld welke wijziging ertoe deed.
- **Leg de bug vast in een falende test voordat je repareert.** De oplossing is pas bewezen wanneer die test groen wordt en groen blijft.
- **Vind de grondoorzaak, niet het dichtstbijzijnde symptoom.** Een patch die het symptoom verbergt laat het defect terugkeren.

## Aanbevelingen

### Reproduceer het defect betrouwbaar voordat je iets verandert

Je eerste taak is een betrouwbare reproductie: een reeks stappen of een geautomatiseerd geval dat de bug op verzoek triggert. Zonder haar kun je een echte oplossing niet onderscheiden van toeval, omdat het symptoom kan komen en gaan om redenen die je nooit beheerste. Leg de invoer, de omgeving, de versies en de timing vast. Als de bug intermitterend is, jaag dan op de verborgen variabele die hem laat verschijnen (een specifiek datarecord, een klokgrens, een gelijktijdig verzoek) tot de reproductie betrouwbaar is. Een betrouwbare reproductie is het waardevolste artefact bij debuggen, omdat alles erna meetbaar wordt.

### Lees de fout, de logs en de stacktrace voordat je code aanraakt

Lees voordat je één theorie vormt wat het systeem je al vertelde. De [stacktrace](https://en.wikipedia.org/wiki/Stack_trace) (de registratie van de aanroepketen op het moment van falen) noemt meestal het bestand, de regel en de volgorde die faalde. De uitzonderingsmelding, de logregels eromheen en de waarden in scope beperken de zoektocht voordat je iets hebt veranderd. Engineers verspillen uren aan theoretiseren over oorzaken die de traceback op regel één uitsloot. Behandel de foutuitvoer als eerste getuige, lees haar zorgvuldig en volledig, en besluit dan pas wat je onderzoekt.

### Isoleer door binair zoeken in de probleemruimte

Scan de code niet van boven naar beneden. Doorzoek haar. Gebruik [binair zoeken](https://en.wikipedia.org/wiki/Binary_search_algorithm): vind een punt waar de toestand nog goed is en een punt waar hij al slecht is, controleer dan het midden en herhaal, het verdachte gebied elke keer halverend. Dit verandert een zoektocht van duizend regels in tien vragen. Wanneer de regressie over een reeks commits verscheen, pas je hetzelfde idee toe op de geschiedenis met bisectie: `git bisect` loopt de commitreeks door, en je markeert elke revisie als goed of slecht tot het de exacte wijziging noemt die het defect introduceerde. Automatiseer de goed-of-slecht-test en bisectie draait vanzelf.

### Reduceer tot een minimaal reproduceerbaar voorbeeld

Zodra je de bug kunt triggeren, krimp hem. Een [minimaal reproduceerbaar voorbeeld](https://en.wikipedia.org/wiki/Minimal_reproducible_example) is de kleinste invoer en codepad die nog faalt: verwijder data, functies en stappen tot elke verdere verwijdering de bug laat verdwijnen. Reductie is geen bezigheidstherapie. Elk element dat je elimineert is een oorzaak die je hebt uitgesloten, dus het minimale geval wijst vaak rechtstreeks naar het defect. Wanneer de invoer groot of gestructureerd is, automatiseer je het krimpen met [delta debugging](https://en.wikipedia.org/wiki/Delta_debugging), een algoritme dat systematisch brokken van een falende invoer verwijdert om de minimale falende deelverzameling te vinden. Een kleine, op zichzelf staande reproductie is ook het best mogelijke bugrapport om aan een ander team te geven.

### Instrumenteer met logs en gebruik dan een interactieve debugger

Stem het gereedschap af op de bug. Logging en gerichte instrumentatie zijn het best wanneer je gedrag over de tijd, over processen heen of in een omgeving die je niet kunt pauzeren moet zien. Een interactieve debugger, waarmee je breakpoints kunt zetten, regel voor regel kunt stappen en live toestand kunt inspecteren, is het best wanneer je de code lokaal kunt draaien en één enkele uitvoering van dichtbij moet bekijken. Voeg instrumentatie toe als bewust experiment gekoppeld aan een hypothese, niet als verspreide printopdrachten, en verwijder haar of promoveer haar tot permanente gestructureerde logging zodra de bug is opgelost. Leun in productie op debuggen gedreven door observeerbaarheid: events met hoge cardinaliteit en gedistribueerde tracing (hoofdstuk 9.2) laten je één verzoek over veel services volgen, wat vaak de enige manier is om een gedistribueerd systeem te debuggen waaraan je geen debugger kunt koppelen.

### Schrijf een falende test die de bug vastlegt voordat je repareert

Schrijf voordat je de oplossing schrijft een test die faalt door de bug. Dit doet drie dingen tegelijk: het bewijst dat je de oorzaak werkelijk begrijpt, het definieert precies wat "gerepareerd" betekent en het wordt een permanente bewaker. Maak dan de oplossing en kijk hoe de test groen wordt. Die test sluit zich nu aan bij je suite als [regressietest](https://en.wikipedia.org/wiki/Regression_testing), zodat hetzelfde defect niet ongemerkt kan terugkeren. Deze praktijk verbindt debuggen direct met je teststrategie (hoofdstuk 2.4): elke moeilijke bug die je oplost laat de suite sterker achter dan hij hem vond, en een onbetrouwbare (flaky) test krijgt dezelfde behandeling (reproduceer het niet-determinisme, bewaak het dan) in plaats van een retryannotatie.

### Vind de grondoorzaak en houd de analyse schuldvrij

Het symptoom repareren is de bug niet repareren. Herleid het falen naar zijn ware oorsprong, vraag op elke laag waarom tot je een oorzaak bereikt die je kunt verwijderen in plaats van maskeren. Voer voor defecten die productie bereikten een schuldvrije grondoorzaakanalyse uit als onderdeel van incidentmanagement (hoofdstuk 9.3): richt je op de systeem- en procesomstandigheden die de bug lieten opleveren en overleven, nooit op het individu dat de regel schreef. Beschuldiging drijft informatie ondergronds, en debuggen draait op informatie. De uitkomst is zowel een oplossing als een verandering in hoe de klasse defecten de volgende keer eerder wordt gevangen.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Logging en instrumentatie | Werkt in productie en gedistribueerde systemen. Legt gedrag over de tijd vast | Ruis, kosten en logwildgroei. Kan timingbugs verstoren |
| Interactieve debugger | Nauwkeurige inspectie van live toestand. Snel voor lokale bugs | Nutteloos in beperkte of air-gapped productie. Kan concurrencybugs verbergen |
| Eerst-reproduceren-discipline | Verandert gokken in meten. Maakt een falende test mogelijk | Langzaam vooraf. Sommige bugs zijn echt moeilijk te triggeren |
| Binair zoeken en bisectie | Snelle isolatie, zelfs in onbekende code | Vraagt een betrouwbare goed-of-slecht-test. Moeilijk wanneer bugs op elkaar inwerken |
| Reductie met delta debugging | Krimpt enorme invoer automatisch tot de trigger | Opzetkosten. Neemt aan dat het falen deterministisch is |
| Het symptoom nu repareren | Herstelt snel de service onder druk | Laat de grondoorzaak terugkeren. Bouwt schuld op |

De centrale spanning is snelheid tegenover zekerheid. Bij een productie-incident moet je misschien eerst de bloeding stelpen (een rollback of een symptoompatch) om de service te herstellen, en dat is legitiem. De fout is daar te stoppen. Los de spanning op door de twee taken te scheiden: mitigeer snel om gebruikers te beschermen, reproduceer dan, vind de grondoorzaak en voeg de regressiebewaker toe voordat je het defect als gesloten beschouwt. Een symptoomfix zonder vervolg is een bug die je hebt afgesproken opnieuw te ontmoeten.

## Vragen om met je team te bespreken

1. **Wanneer iemand een moeilijke bug raakt, wat is het eerste wat die persoon doet, en is het reproduceren of gokken?** Het eerlijke antwoord onthult of je team een gedeelde methode heeft of een kamer vol privéfolklore. Vraag mensen hun laatste moeilijke defect hardop te vertellen: kregen ze eerst een betrouwbare reproductie, of begonnen ze code te veranderen en dingen te herstarten? Een team dat eerst reproduceert kan een bug tussen mensen doorgeven, omdat de reproductie meereist. Een team dat gokt kan dat niet, omdat elke poging onherhaalbaar is. Dit telt zwaarder naarmate het team groeit, aangezien degene die een symptoom ziet steeds vaker niet degene is die het kan repareren. Als gokken de standaard is, spreek dan eerst-reproduceren af als norm en maak een schone reproductie de toegangsprijs voor een bugticket.

2. **Komen de bugs die we repareren terug, en zouden we het weten als ze dat deden?** Een defect dat terugkeert is een defect waarvan de grondoorzaak nooit is verwijderd en waarvan de oplossing nooit door een test is bewaakt. Haal je incidenten en heropende tickets van het laatste kwartaal op en tel hoeveel herhalingen of nauwe verwanten van eerdere bugs waren. Elke herhaling is bewijs dat het team een symptoom patchte, de falende test oversloeg of de grondoorzaakanalyse te vroeg stopte. De oplossing is een regel: geen bug is gesloten voordat een test die faalt op het oude gedrag slaagt op het nieuwe en zich bij de suite voegt. Neem een recente terugkerende bug mee en vraag welke bewaker haar had gevangen, want die bewaker is wat je miste.

3. **Kunnen we onze productiesystemen überhaupt debuggen, gezien hoe we ze mogen aanraken?** In omgevingen van onderneming en vooral overheid kun je vaak geen debugger koppelen, niet met echte data reproduceren en een draaiend systeem niet wijzigen zonder auditspoor. Als je enige debugtechniek een lokale interactieve debugger is, ben je blind precies waar de moeilijkste bugs wonen. Vraag welk bewijs een productiefalen werkelijk achterlaat: gestructureerde logs, gedistribueerde traces (hoofdstuk 9.2), core dumps of reproduceerbare buildartefacten. Besluit nu wat je standaard moet vastleggen zodat een toekomstig incident diagnosticeerbaar is, want je kunt geen instrumentatie toevoegen aan een falen dat al is gebeurd. Bevestig in gereguleerde settings dat hetzelfde spoor ook aan je auditverplichtingen voldoet.

4. **Wanneer een productie-incident ons dwingt de bloeding snel te stelpen, hoe zorgen we dat de grondoorzaak achteraf nog wordt gevonden?** Bij een incident is een rollback of een symptoompatch de juiste eerste zet om gebruikers te beschermen, maar het gevaar is dat het ticket sluit zodra de service terug is en het onderliggende defect nooit wordt gediagnosticeerd. Voor een groot team is dit waar schuld onzichtbaar oploopt, omdat dezelfde klasse falen maanden later opduikt op een andere service en bij een andere engineer met bereikbaarheidsdienst. Neem je laatste paar severity-één-incidenten mee en controleer elk: volgden een reproductie, een grondoorzaakanalyse en een regressiebewaker op de mitigatie, of eindigde het verhaal bij "service hersteld"? Spreek een expliciete regel af dat een gemitigeerd incident open blijft tot de grondoorzaak is begrepen en bewaakt, en noem wie dat vervolg bezit. Koppel dit in omgevingen van onderneming en overheid aan je incidentmanagementproces (hoofdstuk 9.3), zodat de review na het incident een vereiste, controleerbare stap is in plaats van een beleefdheid die verdwijnt wanneer het volgende vuur begint.

5. **Hoeveel van een falen kunnen we achteraf werkelijk reconstrueren, en wie besliste wat we standaard vastleggen?** Je kunt geen instrumentatie aan een falen koppelen dat al is gebeurd, dus de diagnosticeerbaarheid van elk incident ligt vooraf vast door de logs, traces, metrics en dumps die je koos uit te zenden. De concurrerende overweging is kosten en ruis: events met hoge cardinaliteit en volledige tracing zijn niet gratis, en te veel loggen begraaft het signaal terwijl het opslag opblaast en, in gereguleerde contexten, je blootstelling aan bewaartermijnen vergroot. Neem een echt recent incident mee en vraag welk bewijs het achterliet, werk dan terug naar wat je had willen vastleggen en wat het zou kosten dat te bewaren. Besluit bewust welke signalen standaard aan staan tegenover gesampled of opt-in, en leg dat besluit vast zodat het beleid is, geen toeval. Voeg voor een systeem van onderneming of overheid toe wie verantwoordelijk is voor dat observeerbaarheidsbudget en of het vastgelegde spoor ook voldoet aan audit-, privacy- en dataresidentieverplichtingen.

6. **Behandelen we debuggen als een geleerde, meetbare vaardigheid, of nemen nieuwe engineers het op door osmose?** Debuggen is leerbaar, maar de meeste teams onderwijzen het nooit expliciet, dus junioren erven welke folklore er het dichtstbij zit, en de eerst-reproduceren-methode verspreidt zich ongelijk of helemaal niet. De spanning is dat bewust onderwijs (pairen op moeilijke bugs, bevindingen na incidenten opschrijven, statistieken bijhouden) seniortijd kost die altijd elders nodig lijkt. Neem twee getallen mee naar de discussie: je percentage herhaalde defecten en je tijd-tot-diagnose, want als je ze niet kunt meten kun je niet zien of je methode verbetert of vervalt. Overweeg of onboarding een echte debugoefening bevat en of grondoorzaakbevindingen werkelijk eerdere detectie voeden. In een grote of publieke organisatie wordt een gedocumenteerde, gemeten debugpraktijk ook bewijs van engineeringrigueur dat auditors, toezichthouders en controlerende organen steeds vaker verwachten te zien.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen speelruimte is je doel bugs goedkoop te reproduceren en onmogelijk te vergeten te maken, niet zwaar proces te bouwen. Leun op `git bisect`, een snelle lokale reproductie en één falende test per gerepareerde bug, want die gewoonte kost minuten en stopt je dezelfde defecten opnieuw te betalen terwijl je probeert op te leveren. Sla formele postmortems over, maar sla nooit de regressietest over: het is het ene artefact dat klein genoeg is om altijd te betalen en waardevol genoeg om altijd te bewaren.

**Kleinbedrijf.** Je hebt waarschijnlijk geen aparte betrouwbaarheids- of observeerbaarheidsspecialist en een krap toolingbudget, dus geef de voorkeur aan wat je stack al geeft: leesbare stacktraces, gestructureerde logs en de tracing ingebouwd in de frameworks en gehoste diensten die je hebt gekocht. Weeg bij het evalueren van een nieuw platform hoe diagnosticeerbaar het falen maakt, want een goedkope tool die verbergt wat er misging kost je veel meer aan gokken dan de licentie bespaarde. Eerst-reproduceren en één-wijziging-tegelijk zijn gratis disciplines die het snelst lonen wanneer niemand uren over heeft.

**Grote onderneming.** Je moeilijke bugs overschrijden service- en teamgrenzen, dus degene die het symptoom ziet bezit zelden de oorzaak, en een gedeelde methode doet er meer toe dan de vaardigheid van wie dan ook. Standaardiseer eerst-reproduceren, isolatie door binair zoeken, een falende test voor de oplossing en schuldvrije postmortems over teams, en investeer in gedistribueerde tracing (hoofdstuk 9.2) zodat één verzoek over services kan worden gevolgd. Beheer debuggen als gemeten vermogen: volg het percentage herhaalde defecten en de tijd-tot-diagnose, en voed grondoorzaakbevindingen terug in eerdere detectie zodat dezelfde klasse falen niet langs je servicekaart toert.

**Overheid.** Aanbestedingsregels, beperkte omgevingen en publieke verantwoording bepalen hoe je überhaupt mag debuggen. Je kunt vaak geen debugger aan productie koppelen of burgerdata naar een laptop kopiëren, dus ontwerp voor diagnose met wat is toegestaan: reproduceerbare builds, synthetische records in een geïsoleerde enclave en gestructureerde logs en traces standaard vastgelegd. Leg elke diagnostische stap en elke wijziging vast in het auditspoor, en eis dat leveranciers genoeg telemetrie en buildreproduceerbaarheid blootleggen om falen zelfstandig te onderzoeken in plaats van van het woord van de leverancier af te hangen.

## Voorbeelden

**Startup.** Een team van vier engineers ziet de checkout voor een deel van de gebruikers falen, maar nooit in testen. In plaats van te gokken legt één engineer een betrouwbare reproductie vast door de exacte falende request-payload af te spelen, en leest dan de stacktrace die ze negeerden, die naar een datumparseraanroep wijst. Een snelle `git bisect` over de commits van de week noemt de wijziging die een datumbibliotheek verving. Ze schrijven een falende test met het schuldige tijdstempel, repareren de parser, zien de test groen worden en houden hem in de suite. Het hele onderzoek duurt een middag omdat ze reproduceerden voordat ze theoretiseerden, en de bug komt nooit terug.

**Grote onderneming.** Een betalingsplatform ziet intermitterende time-outs die geen enkel team kan verklaren, omdat het symptoom in de checkout verschijnt maar de oorzaak drie services verderop leeft. Engineers met bereikbaarheidsdienst gebruiken gedistribueerde tracing (hoofdstuk 9.2) om één falend verzoek over servicegrenzen te volgen en vinden een downstreamaanroep die af en toe vastloopt onder gelijktijdige belasting, een klassieke [race condition](https://en.wikipedia.org/wiki/Race_condition) waarbij het resultaat afhangt van ongelukkige timing tussen threads. Ze reproduceren hem met een belastingtest, leggen hem vast in een falende integratietest, repareren de locking en voeren een schuldvrije postmortem (hoofdstuk 9.3) uit die een tracingspan en een alert toevoegt zodat de volgende keer binnen minuten wordt gevangen, niet binnen dagen.

**Overheid.** Een uitkeringsinstantie draait haar zaaksysteem in een air-gapped omgeving waar engineers geen debugger aan productie kunnen koppelen en geen burgerdata naar hun laptop kunnen kopiëren. Een rekendefect duikt op in de reconciliatie. Het team debugt vanuit wat de omgeving wel toestaat: gestructureerde logs, een reproduceerbare build die ze in een geïsoleerde testenclave kunnen opzetten en synthetische records die het falende geval nabootsen. Elke diagnostische stap wordt vastgelegd in het auditspoor, de oplossing wordt geleverd met een eerst-falende-dan-slagende test als bewijs en de grondoorzaakanalyse voedt een nieuwe controle vóór de release. Omdat de reproductie synthetische data gebruikte, verliet nooit een burgerrecord de grens.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van gedisciplineerd debuggen wordt gemeten in engineeruren die niet aan gokken worden besteed en in defecten die niet terugkeren. Een ongediagnosticeerde intermitterende bug kan dagen seniortijd en herhaalde escalaties van de bereikbaarheidsdienst opslokken. Een eerst-reproduceren-methode maakt daar een begrensde, delegeerbare taak van, en de gewoonte van de falende test stopt dat hetzelfde defect je volgend kwartaal opnieuw factureert. Over een grote organisatie is het stapeleffect van nooit twee keer voor dezelfde bug betalen aanzienlijk, en het verbetert direct het faalpercentage van wijzigingen en de gemiddelde hersteltijd die het bestuur al volgt.

De total cost of ownership is vooral training en tooling, en is bescheiden. Je hebt gedeelde conventies nodig (eerst reproduceren, één wijziging tegelijk, een falende test voor de oplossing), debuggers en tracing die al gangbaar zijn in de toolchain en de observeerbaarheidsinvestering uit hoofdstuk 9.2. De grotere, verborgen kosten zijn het alternatief: een cultuur van bijgeloof waar engineers hagelschotwijzigingen toepassen, symptomen worden gepatcht en terugkeren en de belasting van de bereikbaarheidsdienst onbegrensd groeit. Alleen al het verminderen van sleurwerk bij bereikbaarheidsdienst rechtvaardigt vaak de investering, en de zakelijke onderbouwing is het eenvoudigst te stellen als minder herhaalde incidenten en sneller herstel voor een eenmalige kost in gewoonten en instrumentatie.

## Antipatronen en valkuilen

- **Hagelschotdebuggen:** veel dingen tegelijk veranderen, zodat zelfs een oplossing je niets leert over de oorzaak.
- **Repareren zonder te reproduceren:** de overwinning uitroepen op een bug die je nooit op verzoek kon triggeren.
- **De foutuitvoer negeren:** theoretiseren over oorzaken die de stacktrace al uitsloot.
- **Symptoompatchen:** het symptoom het zwijgen opleggen terwijl de grondoorzaak overleeft om terug te keren.
- **Wildgroei van printopdrachten:** verspreide debuguitvoer die in de code blijft staan en ruis toevoegt in plaats van een aan een hypothese gekoppeld experiment.
- **De regressietest overslaan:** de bug repareren maar geen bewaker achterlaten, zodat hij stilletjes kan terugkomen.
- **Onbetrouwbare tests herhalen:** niet-determinisme verbergen met retries in plaats van de onderliggende race condition of [heisenbug](https://en.wikipedia.org/wiki/Heisenbug) te debuggen, een bug die verandert of verdwijnt zodra je hem probeert te observeren.
- **Op schuld gerichte postmortems:** de auteur straffen, wat de informatie waarvan debuggen afhangt ondergronds drijft.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Debuggen is individuele folklore en reactie. Engineers gokken, passen hagelschotwijzigingen toe en herstarten dingen. Bugs worden bij het symptoom gerepareerd, reproducties zijn zeldzaam en dezelfde defecten keren terug. Productie is nauwelijks diagnosticeerbaar, en niemand kan een bug aan een ander doorgeven omdat geen poging herhaalbaar is.
- **Niveau 2, Ontwikkelen:** Sommige engineers reproduceren betrouwbaar, lezen stacktraces en gebruiken debuggers, maar de praktijk is inconsistent en verschilt van persoon tot persoon en team tot team. Logging bestaat maar is rumoerig en ongestructureerd. Oplossingen worden soms met een falende test geleverd, vaak niet, en grondoorzaakanalyse gebeurt alleen wanneer iemand erop aandringt.
- **Niveau 3, Standaardiseren:** Eerst-reproduceren, isolatie door binair zoeken, één wijziging tegelijk en een falende test voor de oplossing zijn gedocumenteerde teamnormen die organisatiebreed worden gehandhaafd. Bisectie en reductie met delta debugging zijn gangbare praktijk. Productie heeft gestructureerde logging en tracing (hoofdstuk 9.2), en schuldvrije postmortems (hoofdstuk 9.3) zijn de standaardrespons op elk ontsnapt defect.
- **Niveau 4, Beheersen:** De debugpraktijk wordt gemeten en beheerst aan de hand van uitgangswaarden. Percentage herhaalde defecten, tijd-tot-diagnose, aantal heropende tickets en het aandeel oplossingen dat met een regressietest werd geleverd worden per team gevolgd en volgens een ritme beoordeeld. Reproductie en voltooiing van grondoorzaakanalyse worden als poorten behandeld in plaats van goede bedoelingen, en trends ten opzichte van de uitgangswaarde sturen waar je in tooling, training en observeerbaarheid investeert.
- **Niveau 5, Orkestreren:** Debuggen is een onderwezen vaardigheid geïntegreerd met kwaliteit (hoofdstuk 2.11) en incidentmanagement (hoofdstuk 9.3), en de hele lus past zich continu aan. Observeerbaarheid is ingebouwd zodat de meeste productiebugs zonder debugger diagnosticeerbaar zijn, elke opgeloste bug versterkt de regressiesuite en grondoorzaakbevindingen voeden eerdere detectie zodat klassen defecten worden voorkomen in plaats van opnieuw gediagnosticeerd. De organisatie herbalanceert inspanning naarmate haar systemen en faalwijzen evolueren, en het percentage herhaalde defecten blijft dalen.

## Ideeën voor discussie

1. Welk deel van je recente bugs werd betrouwbaar gereproduceerd voordat iemand code veranderde, en wat zegt dat deel over je methode?
2. Wanneer een regressie verschijnt, grijpt je team dan naar bisectie, of leest het code met de hand tot iemand het ziet?
3. Hoe diagnosticeerbaar is je productiesysteem vandaag, en wat zou je geven om vast te hebben gelegd over een falen dat al is gebeurd?
4. Worden je oplossingen consequent geleverd met een eerst-falende-dan-slagende test, en zo niet, waar breekt die discipline?
5. Hoe ga je om met onbetrouwbare tests: het niet-determinisme debuggen, of het toedekken met retries?
6. Wordt debuggen bewust onderwezen aan nieuwe engineers, of moeten ze folklore door osmose opnemen?

## Belangrijkste inzichten

- Debuggen is hypothesen testen: reproduceer betrouwbaar, lees de fout en stacktrace en isoleer dan door binair zoeken en bisectie in plaats van te scannen.
- Reduceer het falen tot een minimaal reproduceerbaar voorbeeld, met delta debugging voor grote invoer, want elk verwijderd element is een uitgesloten oorzaak.
- Stem het gereedschap af op de bug: instrumentatie en tracing voor productie en gedistribueerde systemen (hoofdstuk 9.2), interactieve debuggers voor lokaal onderzoek.
- Schrijf een falende test die de bug vastlegt voordat je repareert, zodat de oplossing bewezen is en het defect voorgoed bewaakt (hoofdstuk 2.4).
- Vind en verwijder de grondoorzaak, voer schuldvrije postmortems uit (hoofdstuk 9.3) en behandel debuggen als leerbare vaardigheid, niet als folklore.
- Verander één ding tegelijk. Hagelschotwijzigingen en symptoompatches vernietigen bewijs en nodigen de bug uit terug te komen.

## Referenties en verder lezen

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller and Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (the delta debugging algorithm)
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (chapter on debugging)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (the chapters on debugging and assertions)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (the debugging chapter)
- John Regehr, "Reducers Are Fuzzers" and related writing on test-case reduction
- Charity Majors, Liz Fong-Jones, and George Miranda, *Observability Engineering* (debugging production with high-cardinality telemetry and tracing)
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (blameless postmortems and production debugging)
