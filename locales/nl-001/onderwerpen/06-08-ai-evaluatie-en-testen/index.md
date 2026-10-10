# 6.8 AI-evaluatie en -testen

## Overzicht en motivatie

Gewone software testen rust op een geruststellende aanname: bij dezelfde invoer geeft het programma dezelfde uitvoer, en je kunt precies bevestigen wat die uitvoer moet zijn. Kunstmatige intelligentie breekt die aanname. Een model kan dezelfde vraag op twee verschillende manieren beantwoorden, beide acceptabel. Het kan worden beoordeeld op een spectrum van fout tot briljant in plaats van geslaagd of gefaald. En er is vaak geen enkel correct antwoord om tegen te bevestigen. Dus de discipline van evaluatie, meten hoe goed een model zich gedraagt over veel representatieve gevallen in plaats van één uitvoer tegen één verwachte waarde controleren, wordt de ruggengraat van elk betrouwbaar AI-systeem. Wanneer teams AI-functies opleveren die hen in verlegenheid brengen, is de grondoorzaak bijna altijd dat ze vóór release geen serieuze manier hadden om kwaliteit te meten.

Voor grote teams is evaluatie wat verandering veilig maakt. Je zult modellen verwisselen, prompts herschrijven, retrieval afstemmen en tools toevoegen, en elk van die wijzigingen kan gedrag dat je solide waande stilletjes degraderen. Zonder herhaalbare manier om kwaliteit te meten is elke wijziging een gok en wordt elke regressie door een gebruiker ontdekt. Dit hoofdstuk is de meetpartner van de bouwhoofdstukken: generatieve AI en LLM-applicaties (hoofdstuk 6.3), AI-agents en agentische systemen (hoofdstuk 6.7) en machine-learningengineering en MLOps (hoofdstuk 6.2). Het breidt je algemene teststrategie (hoofdstuk 2.4) uit naar de probabilistische wereld.

Omgevingen van onderneming en overheid verhogen de inzet verder. Een onderneming die tientallen AI-functies draait heeft een gedeeld evaluatieplatform nodig zodat niet elk team beoordeling van nul opnieuw uitvindt. Een overheidsinstantie heeft evaluatie nodig die gedocumenteerd en controleerbaar is, omdat "we hebben het getest" moet worden "hier is het bewijs, de dataset, de statistiek en de goedkeuring". Evaluatie is waar verantwoorde en betrouwbare AI (hoofdstuk 6.5) ophoudt een waardeverklaring te zijn en iets wordt wat je aan een toezichthouder kunt tonen.

## Kernprincipes

- Behandel evaluatie als eersterangs product, niet als bijgedachte vlak voor lancering vastgeschroefd.
- Meet met representatieve data die echt gebruik weerspiegelt, niet met speelgoedvoorbeelden die het model vleien.
- Combineer offline evaluatie voor snelle iteratie met online evaluatie voor ground truth.
- Gebruik menselijk oordeel als anker en kalibreer elke geautomatiseerde beoordelaar daartegen.
- Bescherm je evaluatiesets tegen contaminatie, anders zullen je getallen tegen je liegen.
- Bedraad evaluaties in continuous integration als poorten, zodat kwaliteit niet stilletjes kan teruglopen.
- Blijf meten in productie, want kwaliteit drijft af ook als je code dat niet doet.

## Aanbevelingen

### Neem evaluatiegedreven ontwikkeling over

Schrijf de evaluatie voordat je een prompt afstemt of een model kiest. Dit weerspiegelt testgedreven ontwikkeling: je definieert wat "goed" in meetbare termen betekent en bouwt er dan naartoe. Een evaluatie betekent hier een dataset van invoer gekoppeld aan een scoringsmethode die voor elke uitvoer een getal of cijfer teruggeeft. Begin klein. Twintig zorgvuldig gekozen gevallen die echte gebruikersintentie weerspiegelen verslaan duizend willekeurige. Laat de set groeien naarmate je leert waar het systeem faalt, en voeg elk productiefalen als permanent geval toe zodat dezelfde fout niet ongemerkt kan terugkeren.

Evaluatiegedreven ontwikkeling verandert teamgedrag. Wanneer de definitie van goed is opgeschreven en uitvoerbaar, worden discussies over of een wijziging hielp controleerbaar in plaats van een kwestie van smaak. Maak de evaluatieset een beoordeeld artefact in versiebeheer, naast de prompts en code die ze meet.

### Scheid offline en online evaluatie, en gebruik beide

Offline evaluatie haalt een vaste dataset door je systeem in een gecontroleerde omgeving, snel, goedkoop en herhaalbaar, zodat je versies kunt vergelijken voordat iets wordt opgeleverd. Online evaluatie meet het live systeem met echte gebruikers via statistieken als taakvoltooiing, escalatiepercentage, duim-omhoog- en duim-omlaagfeedback en zakelijke uitkomsten stroomafwaarts. Offline vertelt of een wijziging waarschijnlijk veilig is. Online vertelt of ze werkelijk werkte. Je hebt beide nodig, omdat offline sets de werkelijkheid nooit volledig vangen en online signalen te laat komen om je enige vangrail te zijn.

Verbind de twee in een lus. Wanneer online statistieken dalen of gebruikers een slecht antwoord markeren, leg dat geval vast, label het en voeg het toe aan de offline set. Leid experimenten door dezelfde gecontroleerde vergelijking die je voor elke productwijziging gebruikt, het terrein van productanalytics en experimenten (hoofdstuk 7.4). Een A/B-test die toont dat een nieuw model het taaksucces verhoogt is meer waard dan welke offline score ook, maar de offline score is wat je durfde de test te draaien.

### Bouw representatieve evaluatiesets en bescherm tegen contaminatie

Je evaluatie is maar zo eerlijk als haar data. Bouw gouden datasets, samengestelde collecties invoer met gecontroleerde verwachte uitvoer of scoringsrubrieken, die de echte verdeling weerspiegelen van wat gebruikers vragen: de gangbare gevallen, de zeldzame maar kritieke gevallen, de adversariële gevallen en degene die je systeem nu fout heeft. Stratificeer ze zodat je kwaliteit per segment kunt lezen in plaats van een falende categorie te verbergen in een redelijk gemiddelde. Laat domeinexperts de verwachte antwoorden controleren, want een gouden set gebouwd op foute antwoorden is erger dan geen.

Bescherm die data dan tegen contaminatie. Testsetcontaminatie gebeurt wanneer je evaluatievoorbeelden lekken in de trainingsdata van een model of in de prompt zelf, zodat het model goed lijkt te presteren omdat het de antwoorden feitelijk heeft gezien. Daarom kan een model briljant scoren op een publieke benchmark en struikelen over je echte verkeer. Houd een deel van je evaluatiedata privé en stuur het nooit naar een derde die je niet kunt vertrouwen. Ververs sets in de tijd. Let op het subtielere lek waarbij ontwikkelaars prompts met de hand afstemmen tegen de evaluatieset tot de score betekenisloos is, een vorm van overfitten op de test in plaats van echte verbetering. Houd een verse set achter die je maar af en toe bekijkt.

### Kies statistieken die bij de taak passen

Stem je meting af op de vorm van de uitvoer. Voor classificatie en extractie, waar een correct label bestaat, gelden klassieke statistieken: [precisie en recall](https://en.wikipedia.org/wiki/Precision_and_recall) (van de items die je markeerde, hoeveel waren juist, en van de juiste items, hoeveel vond je), de [F-score](https://en.wikipedia.org/wiki/F-score) die ze balanceert en exacte-matchnauwkeurigheid. Meet voor alles waar een zelfverzekerde waarschijnlijkheid telt [kalibratie](https://en.wikipedia.org/wiki/Calibration_(statistics)), of een opgegeven zekerheid van 80 procent ongeveer 80 procent van de tijd juist is, omdat een goed gekalibreerd model dat weet wanneer het onzeker is veel veiliger is dan een overmoedig.

Generatieve uitvoer is moeilijker. Op referenties gebaseerde statistieken als [BLEU](https://en.wikipedia.org/wiki/BLEU) en ROUGE, oorspronkelijk gebouwd voor machinevertaling en samenvatten, vergelijken gegenereerde tekst met referentietekst door overlappende woorden en zinsdelen te tellen. Ze zijn goedkoop en herhaalbaar, en ze zijn zwakke proxy's voor kwaliteit: ze belonen oppervlakkige overlap en straffen een correct antwoord dat anders is geformuleerd dan de referentie. Gebruik ze als grove regressiesignalen, niet als je definitie van goed. Voor open taken werkt scoren op rubriek beter: definieer expliciete criteria (is het gegrond, compleet, veilig en correct opgemaakt) en score elk. Rubrieken maken subjectieve kwaliteit leesbaar en beoordeelbaar.

### Gebruik LLM-als-rechter, maar kalibreer tegen mensen

Generatieve uitvoer met de hand beoordelen schaalt niet, dus teams gebruiken steeds vaker een sterk [groot taalmodel](https://en.wikipedia.org/wiki/Large_language_model) als geautomatiseerde rechter, het promptend met de invoer, de uitvoer en een rubriek en het vragend te scoren. Deze LLM-als-rechter-aanpak is snel en verrassend capabel, en draagt echte vooroordelen die je moet beheren. Rechters neigen naar langere antwoorden, geven de voorkeur aan de eerste optie in een paarsgewijze vergelijking (positievooroordeel), belonen hun eigen schrijfstijl en kunnen worden beïnvloed door vloeiende maar foute redenering. Ongecontroleerd geeft een bevooroordeelde rechter je zelfverzekerde, precieze, foute getallen.

Kalibreer de rechter tegen menselijke labels. Laat mensen een steekproef beoordelen, controleer dan hoe goed de modelrechter ermee overeenkomt en blijf de rechtersprompt afstemmen tot de overeenstemming hoog genoeg is om te vertrouwen. Verminder bekende vooroordelen bewust: randomiseer de volgorde van opties, controleer voor lengte en vraag om een aan een rubriek verankerde score met redenen in plaats van een kaal getal. Behandel de rechter als meetinstrument dat periodiek herkalibratie nodig heeft, niet een vast orakel. Kies bij het bouwen van de rechter standaard het meest capabele beschikbare model, want een zwakke rechter is een zwakke liniaal.

### Houd mensen in de lus voor de ground truth

Menselijke evaluatie blijft het anker waartegen elke geautomatiseerde statistiek wordt gemeten, dus investeer in het goed doen ervan. Schrijf heldere annotatierichtlijnen, train je annotators en meet inter-annotatorovereenstemming, de mate waarin onafhankelijke reviewers hetzelfde geval hetzelfde cijfer geven. Lage overeenstemming betekent meestal dat je rubriek dubbelzinnig is, niet dat je reviewers slordig zijn, dus repareer de rubriek. Gebruik voor domeinen met hoge inzet gekwalificeerde experts, geen crowdwerkers die de context missen om een juridisch of medisch antwoord te beoordelen.

### Red-team voor veiligheid en adversariële robuustheid

Standaard evaluatiesets meten of het systeem het juiste doet bij redelijke invoer. [Red teaming](https://en.wikipedia.org/wiki/Red_team), je eigen systeem bewust aanvallen om te vinden waar het zich misdraagt, meet wat er onder druk gebeurt. Tast af op prompt-injectie, jailbreaks, onveilige content, privacylekken en bevooroordeelde uitvoer. Maak er een herhaalbare suite van, geen eenmalige oefening: zet elke geslaagde aanval om in een permanent regressiegeval zodat een gerepareerde kwetsbaarheid gerepareerd blijft. Dit werk sluit direct aan op verantwoorde en betrouwbare AI (hoofdstuk 6.5), en in gereguleerde omgevingen is het vaak het bewijs dat een veiligheidsreview tevredenstelt.

### Evalueer agents op taaksucces van begin tot eind

Agents die over veel stappen plannen en handelen kunnen niet één uitvoer per keer worden beoordeeld. Wat telt is of de hele taak slaagde: boekte de agent de vergadering, loste hij het ticket op of voltooide hij de workflow correct en veilig. Bouw evaluaties op taakniveau in een gesandboxte omgeving waar de agent kan handelen tegen realistische maar veilige fixtures, en score de uiteindelijke uitkomsten plus het traject, dat wil zeggen de reeks stappen en toolaanroepen die hij nam om er te komen. Een correct antwoord bereikt via een gevaarlijk of verspillend pad is nog steeds een probleem. Dit is essentieel voor AI-agents en agentische systemen (hoofdstuk 6.7), waar één verkeerde actie echte gevolgen kan hebben.

### Bedraad evaluaties in CI en bewaak productie

Maak evaluatie automatisch. Draai je offline suite in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI) bij elke prompt-, model- of retrievalwijziging en poort merges erop net zoals je op unittests poort, een praktijk geworteld in je bredere teststrategie (hoofdstuk 2.4). Omdat scores ruisig zijn, poort op drempels en trends in plaats van een perfecte run te eisen, en laat de build falen wanneer een sleutelstatistiek onder haar vloer zakt of voorbij een gestelde marge regresseert. Blijf dan kijken in productie: bewaak kwaliteitssignalen, uitvoerverdelingen en invoerdrift om de langzame degradatie te vangen die offline tests missen, wat aansluit op de observeerbaarheidspraktijken van machine-learningengineering en MLOps (hoofdstuk 6.2). Een model dat bij lancering nauwkeurig was kan vervallen naarmate de wereld die het beschrijft eronder verandert.

## Afwegingen: voor- en nadelen

| Evaluatieaanpak | Voordelen | Nadelen | Het best wanneer |
|---|---|---|---|
| Menselijke evaluatie | Hoogste getrouwheid, vangt nuance | Traag, kostbaar, moeilijk te schalen | Ground truth, hoge inzet, rechters kalibreren |
| LLM-als-rechter | Snel, goedkoop, schaalt naar grote sets | Bevooroordeeld, vraagt kalibratie | Frequente offline runs op generatieve uitvoer |
| Op referenties gebaseerde statistieken (BLEU, ROUGE) | Goedkoop, deterministisch, herhaalbaar | Zwakke proxy voor echte kwaliteit | Grove regressiesignalen, geen eindoordelen |
| Klassieke statistieken (precisie, recall, F-score) | Objectief, goed begrepen | Passen alleen bij taken met correcte labels | Classificatie, extractie, retrieval |
| Publieke benchmarks | Vergelijkbaar over modellen, geen opzet | Contaminatie, slechte pasvorm op je taak | Vroege modelshortlist, geen releasepoorten |
| Online evaluatie (A/B, feedback) | Weerspiegelt echte gebruikers en uitkomsten | Traag, komt na blootstelling | Bevestigen dat een wijziging werkelijk hielp |

De centrale spanning is snelheid tegenover getrouwheid. Menselijke evaluatie is het betrouwbaarst en het minst schaalbaar. Geautomatiseerde beoordeling is het omgekeerde. De oplossing is ze lagen: gebruik snelle, goedkope methoden voor constante iteratie, verankerd die methoden aan menselijk oordeel via regelmatige kalibratie en reserveer volledige menselijke review voor de beslissingen met de hoogste inzet en voor controleren dat je goedkope statistieken de werkelijkheid nog volgen. Een tweede spanning is offline gemak tegenover online waarheid. Offline sets laten je snel bewegen maar spiegelen productie nooit volledig, dus behandel een sterke offline score als toestemming om een zorgvuldige online test te draaien, niet als bewijs dat je klaar bent.

## Vragen om met je team te bespreken

1. **Wat is onze lat voor "goed genoeg", en wie bezit de evaluatieset die haar definieert?** Elke AI-functie heeft een impliciete kwaliteitsdrempel, en wanneer die impliciet blijft, stelt elke engineer de zijne op gevoel en worden geschillen beslecht door wie het meest senior in de kamer is. De lat opschrijven als uitvoerbare evaluatieset met doelscores per segment verandert die geschillen in meetbare vragen. Neem je huidige definitie van succes mee, de data erachter en een eerlijk verslag van wie haar werkelijk onderhoudt, want een evaluatieset zonder eigenaar rot net zo snel als elke andere onverzorgde code. Besluit of de lat verschilt per risicolaag, aangezien een publiek juridisch antwoord een hogere lat moet halen dan een intern brainstormhulpmiddel. Het antwoord moet vertellen of iemand nu een AI-wijziging kan opleveren zonder dat enige meting tussen hem en de gebruikers staat.

2. **Hoe weten we dat onze evaluatiegetallen eerlijk zijn in plaats van gecontamineerd of overgefit?** Een score is alleen nuttig als ze echte kwaliteit voorspelt, en er zijn veel manieren waarop ze dat kan ophouden: benchmarkdata die in training lekt, ontwikkelaars die prompts tegen de testset afstemmen tot het getal betekenisloos is of een gouden dataset gebouwd op antwoorden die nooit zijn geverifieerd. Neem bewijs mee van waar je evaluatiedata vandaan kwam, hoeveel ervan privé wordt gehouden en hoe vaak ze wordt ververst. Bespreek of je een verse holdout bewaart die je zelden bekijkt, zodat je minstens één getal hebt waartegen niemand heeft geoptimaliseerd. Als je niet kunt uitleggen waarom je scores zouden standhouden op data die het model nooit heeft beïnvloed, meet je je eigen spiegelbeeld.

3. **Waar blijven mensen in de lus, en hoe houden we onze geautomatiseerde rechters gekalibreerd tegen hen?** LLM-als-rechter en referentiestatistieken laten je op schaal beoordelen, en ze drijven op onzichtbare manieren af van menselijk oordeel tenzij je controleert. Neem je huidige overeenstemmingspercentage tussen geautomatiseerde beoordeling en menselijke review mee, hoe recent je het mat en op welke vooroordelen (lengte, positie, stijl) je hebt getest. Besluit welke beslissingen een menselijke beoordelaar vereisen ongeacht kosten, meestal die met de hoogste inzet en degene die worden gebruikt om de geautomatiseerde rechter te herkalibreren. Praat ook over annotatiekwaliteit, want een rechter gekalibreerd tegen inconsistente menselijke labels erft die inconsistentie. Het antwoord moet een schema voor herkalibratie opleveren, geen eenmalige zegen.

4. **Welke AI-wijzigingen worden vandaag op evaluatie gepoort, en welke bereiken gebruikers nog op alleen iemands zelfvertrouwen?** Een poort die op sommige wijzigingen draait maar niet op andere geeft je de illusie van veiligheid terwijl de echte regressies door het niet-gepoorte pad glippen: een stille prompttweak, een retrievalafstemming, een modelversieverhoging waarvan niemand dacht dat ze als wijziging telde. Voor een groot team groeit het gevaar met het aantal mensen dat een prompt kan aanraken, omdat elk niet-gepoort pad een manier is om een regressie op te leveren die nooit een dataset zag. Neem de lijst wijzigingstypen mee die de offline suite in continuous integration nu triggeren, degene die dat niet doen en de laatste incidenten herleid tot een niet-gepoorte wijziging. Besluit welke drempel en trend de poort afdwingt, aangezien een ruisige score een vloer en een regressiemarge vraagt in plaats van een eis van een perfecte run. Koppel de poort in omgevingen van onderneming en overheid aan het releaseregister zelf, zodat het bewijs dat een wijziging is gemeten onderdeel is van het auditspoor en niet een screenshot die iemand eenmaal maakte.

5. **Hoeveel geven we uit aan evaluatie, en is die uitgave afgestemd op het risico van elke functie?** Evaluatie is niet gratis: annotatiearbeid, de rekenkracht die geautomatiseerde rechters bij elke run verbranden en het doorlopende werk van gouden datasets representatief houden kosten echt geld, en een team dat die kosten nooit noemt neigt ertoe óf onder te investeren op een functie met hoge inzet óf een wegwerpfunctie te verguld uit te voeren. De concurrerende trek is tussen getrouwheid en budget, omdat de meest betrouwbare methode, deskundige menselijke review, ook de minst schaalbare is, dus je kunt haar niet overal betalen en moet beslissen waar ze haar prijs verdient. Neem de huidige kosten per evaluatierun mee, de annotatie-uren per functie en een eerlijke risicolaag voor elk systeem zodat de kamer kan zien waar het geld heen gaat tegenover waar het gevaar leeft. Voor een onderneming is dit het sterkste argument voor een gedeeld evaluatieplatform dat annotatie en rekenkracht over veel teams afschrijft. Voor een overheidsinstantie moet de risicolaag direct afbeelden op de diepte van het bewijs die een toezichtsorgaan later zal eisen.

6. **Wanneer een beter model arriveert, hoe snel kunnen we bewijzen of het helpt, en wie mag de overstap maken?** De waarde van een evaluatiesuite wordt het scherpst gerealiseerd op de dag dat een sterker model uitkomt, omdat een team dat zijn gouden datasets en red-teamsuite in een middag tegen het nieuwe model kan draaien verbeteringen kan overnemen die een team dat met de hand beoordeelt maandenlang mist. De spanning is tussen snelheid en voorzichtigheid: je wilt bewegen op de dag dat een beter model verschijnt, en je kunt een wissel niet stilletjes een categorie antwoorden laten degraderen die je gemiddelde score verbergt. Neem de tijd mee die een volledige offline vergelijking tegen een nieuwe aanbieder nu kost, of je evaluatiesets overdraagbaar zijn tussen modellen en de segmenten waar een regressie het meest zou tellen. Noem in gereguleerde en publieke omgevingen wie het gezag heeft een modelwijziging goed te keuren en welk gedocumenteerd bewijs ze eisen, want een ongedocumenteerde wissel van het model achter een beslissing voor een burger is precies het soort wijziging waarvoor een auditor je zal vragen het te rechtvaardigen.

## Sectorperspectief

**Startup.** Bouw de kleinste eerlijke evaluatie die je kunt en laat haar met het product groeien. Een spreadsheet van twintig tot veertig echte gevallen, elk met een gecontroleerd verwacht antwoord, vóór elke merge door een script gedraaid, verslaat elke publieke benchmark voor je niche en kost bijna niets. Sla het gedeelde platform en LLM-als-rechter over tot met de hand beoordelen werkelijk pijn doet, maar voeg vanaf dag één elk door gebruikers gemeld falen aan de set toe, want die reflex voorkomt dezelfde blamage twee keer.

**Kleinbedrijf.** Je hebt waarschijnlijk geen evaluatiespecialist en koopt je AI ingebed in tools, dus je taak is bewijs eisen in plaats van het te bouwen. Vraag elke leverancier hoe ze kwaliteit maten, of ze testen op data die op de jouwe lijkt en hoe je een regressie zou opmerken na een update die je niet koos. Houd een kleine privéset van je eigen echte gevallen om de tool zelf steekproefsgewijs te controleren, aangezien een fout geautomatiseerd antwoord dat een klant bereikt je veel meer kost dan de minuten die die controle neemt.

**Grote onderneming.** De prijs is een gedeeld evaluatieplatform zodat een dozijn teams niet elk beoordeling opnieuw uitvindt: een gemeenschappelijke opslag voor gouden datasets, offline suites gepoort in continuous integration, geregistreerde LLM-rechtersprompts met hun kalibratiescores en online statistieken per functie. Leg daar governance bovenop met risicolagen die de vereiste lat en de goedkeuring vóór release bepalen, zodat een functie met hoge inzet een hogere poort haalt dan een intern hulpmiddel. Het platform schrijft annotatie en rekenkracht over teams af, wat de sterkste reden is er een te bouwen in plaats van elke groep te laten improviseren.

**Overheid.** Evaluatie moet controleerbaar zijn, niet slechts gedaan, dus archiveer de datasetversie, de statistieken, de naam van de reviewer en de goedkeuring als verantwoordingsbewijs voor elke release. Een red-teamsuite moet bewijzen dat het systeem weigert beleid te verzinnen of wet te stellen die niet in zijn bronnen staat, en aanbesteding moet eisen dat leveranciers bekendmaken hoe ze het model evalueerden en overdraagbaarheid van je evaluatiedata verlenen. Wanneer een toezichtsorgaan vraagt hoe je weet dat de tool veilig is, moet het antwoord een gedateerd register zijn, geen geruststelling.

## Voorbeelden

**Startup.** Een bedrijf van vier personen dat een AI-assistent voor contractreview bouwde begon met een spreadsheet van veertig echte clausules, elk gelabeld door hun huisjurist met het risico dat het moest markeren. Elke promptwijziging draaide vóór het mergen tegen die set in een script, en de score werd in de pull request afgedrukt. Toen gebruikers een gemiste clausule meldden, ging die direct in de sheet, zodat de set met het product groeide. Naarmate het volume steeg voegden ze een LLM-als-rechter toe om uitlegkwaliteit te beoordelen, maar pas nadat ze hadden gecontroleerd dat hij op een steekproef met de jurist overeenkwam. Goedkoop, privé en eerlijk verslaat elke publieke benchmark voor hun niche.

**Grote onderneming.** Een grote bank draaide een dozijn AI-functies over support, zoeken en interne tooling, en elk team had anders beoordeeld. Ze bouwden een gedeeld evaluatieplatform: een gemeenschappelijke plek om gouden datasets op te slaan, offline suites in CI te draaien, LLM-rechtersprompts met hun kalibratiescores te registreren en online statistieken per functie te volgen. Governance zat daarbovenop, met risicolagen die de vereiste lat en de goedkeuring vóór release bepaalden. Een nieuwe fraude-uitlegfunctie kon pas live als haar evaluatieset was beoordeeld, haar red-teamsuite slaagde en haar verantwoordelijke eigenaar de resultaten tekende. Het platform hergebruiken betekende dat teams over hun domein discussieerden, niet over hoe te meten.

**Overheid.** Een publieke gezondheidsinstantie deployde een assistent om medewerkers te helpen vragen over uitkeringen te beantwoorden uit goedgekeurde richtlijnen. Omdat een fout antwoord iemands recht kon raken, moest evaluatie controleerbaar zijn. Elke release draaide een gedocumenteerde evaluatieset met gangbare vragen, randgevallen en adversariële prompts, en de resultaten, de datasetversie, de statistieken en de naam van de reviewer werden gearchiveerd als verantwoordingsbewijs. Een red-teamsuite controleerde dat het systeem weigerde beleid te verzinnen of wet te stellen die niet in zijn bronnen stond. Toen een toezichtsorgaan vroeg hoe de instantie wist dat de tool veilig was, was het antwoord een gedateerd register, geen geruststelling.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Evaluatie verdient zichzelf terug door elke andere AI-investering veiliger en sneller te maken. Haar return on investment (ROI) toont zich als minder productie-incidenten, snellere iteratie omdat teams prompts en modellen met vertrouwen kunnen wijzigen en het vermogen betere modellen de dag dat ze arriveren over te nemen omdat je kunt bewijzen of ze helpen. De helderste manier om haar te waarderen is de kosten van haar afwezigheid: één publieke hallucinatie, bevooroordeelde uitvoer of datalek kan veel meer kosten aan herstel, verloren vertrouwen en regelgevende blootstelling dan jaren evaluatie-infrastructuur. Het is het verschil tussen een regressie in CI gratis vinden en haar in de krant vinden.

De total cost of ownership (TCO) is echt en de moeite waard om te noemen. Je betaalt voor annotatiearbeid, voor de rekenkracht die geautomatiseerde rechters verbruiken en voor het doorlopende werk van evaluatiesets representatief houden naarmate gebruik verschuift. Op ondernemingsschaal schrijft een gedeeld platform het meeste hiervan af over veel teams, wat het sterkste argument is er een te bouwen in plaats van elke groep te laten improviseren. Maak de zaak voor het bestuur door een concreet risico (de kosten van één slecht publiek antwoord in jouw domein) te koppelen aan een concreet vermogen (de snelheid om elk nieuw model veilig over te nemen), en door evaluatie te formuleren als de maatregel waarmee de organisatie snel kan bewegen zonder roekeloos te bewegen.

## Antipatronen en valkuilen

- **Opleveren op gevoel.** AI-wijzigingen beoordelen door een paar prompts met de hand te proberen, zonder dataset en zonder herhaalbare score.
- **Benchmarktheater.** Een sterke publieke benchmarkscore vertrouwen als bewijs dat het systeem bij je taak past, contaminatie en verdelingsverschil negerend.
- **Overfitten op de evaluatieset.** Prompts tegen dezelfde vaste set afstemmen tot het getal hoog en betekenisloos is, zonder verse holdout.
- **Ongekalibreerde rechters.** Een LLM-als-rechter deployen en zijn scores vertrouwen zonder ooit de overeenstemming met menselijke beoordelaars te controleren.
- **Statistiekaanbidding.** BLEU of ROUGE optimaliseren alsof het kwaliteit was, en slechtere antwoorden opleveren die toevallig de referentietekst overlappen.
- **Eenmalig red teamen.** Het systeem eenmaal voor lancering aanvallen en bevindingen nooit omzetten in permanente regressietests.
- **Alleen offline vertrouwen.** Geloven dat een goede offline score betekent dat de functie werkt, zonder online meting van echte uitkomsten.
- **Weesevaluatiesets.** Datasets die niemand bezit, die nooit productiefalen opnemen en langzaam de werkelijkheid niet meer weerspiegelen.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** AI-wijzigingen worden met de hand beoordeeld op een paar voorbeelden, reactief, wanneer iemand zich toevallig zorgen maakt. Er is geen dataset, geen herhaalbare score en geen poort. Regressies worden door gebruikers gevonden, en niemand kan zeggen of het systeem beter of slechter is dan vorige maand.
- **Niveau 2, Ontwikkelen:** Sommige teams houden kleine gouden datasets bij en draaien ze handmatig vóór grote wijzigingen, en enkele klassieke of op referenties gebaseerde scores bestaan. Menselijke review gebeurt voor belangrijke functies, maar beoordeling is inconsistent over teams, evaluatie is niet geautomatiseerd of gepoort en elke groep doet het anders.
- **Niveau 3, Standaardiseren:** Offline suites draaien in continuous integration bij elke prompt-, model- of retrievalwijziging en poorten merges, volgens één gedocumenteerde praktijk over de organisatie. LLM-als-rechter is gekalibreerd tegen menselijke labels, red teaming is een herhaalbare suite en datasets worden bezeten, geversioneerd en gevoed door productiefalen, met contaminatie actief bewaakt.
- **Niveau 4, Beheersen:** Evaluatie wordt gemeten en beheerst met data tegen uitgangswaarden. Overeenstemmingspercentages tussen rechter en mens, red-team-slaagpercentages, scores per segment, online taaksucces en drift worden in de tijd gevolgd, en merges poorten op drempels en regressiemarges in plaats van één perfecte run. Annotatiekosten en rekenkracht per run worden per functie begroot, herkalibratie gebeurt volgens schema en elk resultaat draagt een verantwoordelijke eigenaar en goedkeuring.
- **Niveau 5, Orkestreren:** Een gedeeld evaluatieplatform bedient de hele organisatie, en offline en online evaluatie vormen een continue lus gekoppeld aan bedrijfsuitkomsten. Nieuwe modellen worden bewezen tegen overdraagbare evaluatiesets de dag dat ze arriveren, het portfolio past zich aan naarmate gebruik en risico verschuiven, evaluatiebewijs is controleerbaar voor toezichthouders en toezichtsorganen en lessen uit het falen van het ene team stromen in de datasets van elk team.

## Ideeën voor discussie

1. Hoe beslis je wanneer een offline score sterk genoeg is om een online experiment te rechtvaardigen, en wanneer niet?
2. Wat is de juiste verhouding menselijke evaluatie tot geautomatiseerde beoordeling voor jouw risicoprofiel, en hoe vaak moet je haar herzien?
3. Wanneer een publieke benchmark en je private evaluatieset het oneens zijn over welk model beter is, welke vertrouw je en waarom?
4. Hoe houd je een evaluatieset representatief naarmate gebruikersgedrag verschuift, zonder dat ze uitdijt tot iets te traags om in CI te draaien?
5. Wat hoort in een red-teamsuite voor jouw domein, en wie is gekwalificeerd om de aanvallen te ontwerpen?
6. Hoe evalueer je het traject van een agent, niet alleen zijn eindantwoord, zonder te verdrinken in de kosten van elke stap beoordelen?

## Belangrijkste inzichten

- AI-evaluatie verschilt van softwaretesten omdat uitvoer niet-deterministisch is en er zelden één correct antwoord bestaat, dus je meet kwaliteit over representatieve gevallen in plaats van exacte waarden te bevestigen.
- Oefen evaluatiegedreven ontwikkeling: definieer eerst meetbare kwaliteit, bouw er dan naartoe en voeg elk productiefalen terug in de set.
- Laag methoden naar snelheid en getrouwheid: goedkope geautomatiseerde beoordeling voor constante iteratie, menselijk oordeel als anker en kalibratie om ze uitgelijnd te houden.
- Bewaak tegen contaminatie en overfitten, anders zullen je getallen je vleien terwijl het echte systeem gebruikers teleurstelt.
- Bedraad offline evaluatie in CI als poort en blijf kwaliteit en drift in productie meten, want een model dat bij lancering goed was kan vervallen.

## Referenties en verder lezen

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviours, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
