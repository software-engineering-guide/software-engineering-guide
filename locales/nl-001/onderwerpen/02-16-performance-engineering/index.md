# 2.16 Performance engineering

## Overzicht en motivatie

Performance engineering is het vak om code bewust snel genoeg te maken, met meting in plaats van instinct. Dit hoofdstuk werkt op het niveau van code en componenten: functies, lussen, datastructuren, queries, allocaties en de manier waarop één enkele service zijn tijd besteedt. Het is de tegenhanger van hoofdstuk 3.5, dat prestaties op systeemniveau behandelt (uitschalen, load balancing, capaciteit en veerkracht). Wanneer een systeem traag is, vraagt hoofdstuk 3.5 hoeveel machines je nodig hebt. Dit hoofdstuk vraagt waarom één machine in de eerste plaats zoveel werk doet. Meestal heb je beide nodig, en in het codeniveau verbergt zich verrassend veel kosten en latentie.

Voor grote teams doet deze discipline ertoe omdat prestaties stilletjes vervallen. Geen enkele commit maakt een service traag, maar duizend kleine, elk met een databaseaanroep of een onbegrensde lus erbij, wel. Zonder een gedeelde methode om prestaties te meten, te budgetteren en te poorten, ontdek je het verval pas wanneer een klant klaagt of een lancering smelt. Een methode verandert prestaties van een heldhaftig brandweerwerk in een routinematige eigenschap die je beschermt.

Voor ondernemingen zijn prestaties geld: snellere code betekent minder machines, lagere cloudrekeningen en het vermogen een [service-level agreement](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) over latentie te halen zonder te veel capaciteit te reserveren. Voor de overheid zijn prestaties toegang: een pagina die laadt op een oude telefoon via een zwakke mobiele verbinding is het verschil tussen een burger die een uitkeringsaanvraag voltooit en opgeeft. Publieke systemen hebben ook reproduceerbaar benchmarkbewijs nodig, omdat aanbestedings- en toezichthoudende organen je zullen vragen de cijfers te bewijzen, niet alleen te beweren.

## Kernprincipes

- **Meet voordat je optimaliseert.** Het knelpunt zit bijna nooit waar je denkt. Profileer en handel dan.
- **Vermijd voortijdige optimalisatie.** De waarschuwing van Donald Knuth blijft gelden: code optimaliseren die er niet toe doet kost helderheid en levert niets op.
- **Definieer "snel genoeg" als een getal.** Een prestatiebudget met een doel en een percentiel verandert mening in geslaagd of gezakt.
- **Gemiddelden liegen, percentielen vertellen de waarheid.** De staart (p99) is wat gebruikers voelen, niet het gemiddelde.
- **Algoritmische winst verslaat microtuning.** Een betere complexiteitsklasse overtreft elke hoeveelheid slimmigheid in constante factoren.
- **Latentie en doorvoer zijn verschillende doelen.** Het ene verbeteren kan het andere verslechteren. Weet welke je koopt.
- **Benchmark eerlijk of helemaal niet.** Opwarming, variantie en een representatieve werklast scheiden echte cijfers van fictie.
- **Poort prestaties in CI, bewaak ze in productie.** Regressies gevangen voor het samenvoegen zijn goedkoop, gevangen door gebruikers duur.

## Aanbevelingen

### Meet eerst en profileer voordat je een regel aanraakt

De oudste regel op dit gebied is de meest genegeerde: vind het knelpunt voordat je optimaliseert. Grijp naar een [profiler](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), een tool die een draaiend programma samplet of instrumenteert om te tonen waar het tijd en geheugen besteedt. Profileer CPU (welke functies cycli verbranden), geheugen en allocatie (wat wordt toegewezen en hoe vaak, aangezien allocatieomloop pauzes van garbage collection aandrijft) en I/O (tijd besteed aan wachten op schijf, netwerk of database). Een [flamegraph](https://en.wikipedia.org/wiki/Flame_graph), een gestapelde visualisatie waarin elk vak een functie is en zijn breedte de bestede tijd, maakt de dominante kost in één oogopslag duidelijk: zoek de breedste vakken, niet de diepste stapels. Optimaliseer de grootste kost eerst, meet opnieuw en stop wanneer je het budget haalt. Dit sluit aan op de observeerbaarheidspraktijken van hoofdstuk 9.2, want een productieprofiel verslaat elke gok vanaf een laptop.

Bescherm je ook tegen de tegenovergestelde fout. Knuths volledige zin is dat voortijdige optimalisatie de wortel is van veel kwaad, en hij bedoelde het over de kleine inefficiënties die je verleiden leesbare code op te offeren voor ingebeelde snelheid. Schrijf eerst de heldere versie, meet en optimaliseer alleen de code die de profiler aanklaagt.

### Definieer wat "snel genoeg" betekent met prestatiebudgetten

Snelheid is geen deugd in het abstracte. Het is een doel dat je haalt of mist. Stel een **prestatiebudget** vast: een concrete limiet zoals "p99-checkoutlatentie onder 300 ms" of "dit endpoint alloceert minder dan 1 MB per verzoek". Koppel het aan iets wat gebruikers of het bedrijf voelen en druk het uit als **percentiel**, niet als gemiddelde, omdat het gemiddelde de trage staart verbergt waar echte gebruikers wonen. Als 1% van de verzoeken 5 seconden duurt, kan je gemiddelde er prima uitzien terwijl een betekenisvol deel van de klanten lijdt. Budgetten geven een team een gedeelde, onbetwistbare definitie van klaar en een lijn die een regressie zichtbaar overschrijdt.

### Grijp naar algoritmische efficiëntie vóór microoptimalisatie

De grootste, goedkoopste winst komt uit [algoritmische efficiëntie](https://en.wikipedia.org/wiki/Algorithmic_efficiency), hoe het werk groeit naarmate de invoer groeit, beschreven met [big-O-notatie](https://en.wikipedia.org/wiki/Big_O_notation) (een manier om groeisnelheid te classificeren, zodat een O(n log n)-sortering veel beter schaalt dan een O(n kwadraat)). Een geneste lus die onzichtbaar is bij tien items wordt een catastrofe bij tienduizend. Vraag voordat je een hete functie met de hand afstemt of ze fundamenteel te veel werk doet: een toevallige N+1-query, een lineaire scan die een hashopzoeking zou moeten zijn of herhaald werk dat gememoïseerd kan worden. Dit sluit aan op de algoritmische fundamenten in hoofdstuk 2.13. Geen hoeveelheid afstemming van constante factoren redt de verkeerde complexiteitsklasse.

### Onderscheid latentie van doorvoer en respecteer de staart

**Latentie** is hoe lang één bewerking duurt. **Doorvoer** is hoeveel bewerkingen per tijdseenheid worden voltooid. Ze zijn niet hetzelfde doel, en het ene optimaliseren kan het andere schaden. Batchen verbetert doorvoer maar voegt latentie toe aan het eerste item in de batch. Parallelle workers toevoegen verhoogt doorvoer maar kan de staartlatentie verslechteren door contentie. Besluit welke je gebruikers werkelijk nodig hebben. En let altijd op de staart: p95- en p99-latentie, de traagste 5% en 1% van de verzoeken, want op schaal doet een gebruiker veel verzoeken en raakt hij de staart vaak. Rapporteer percentielen, alarmeer erop en budgetteer ervoor.

### Ken de grenzen van parallellisme

Wanneer je parallelliseert, onthoud dan de [wet van Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): de versnelling door processoren toe te voegen wordt begrensd door de fractie van het werk die serieel moet draaien. Als 10% van een taak inherent sequentieel is, brengt geen aantal cores je voorbij een versnelling van 10x. Gelijktijdigheid (werk zo structureren dat taken onafhankelijk vooruitgang kunnen boeken) en parallellisme (ze daadwerkelijk tegelijk uitvoeren) voegen echte complexiteit toe, van race conditions tot coördinatie-overhead. Meet de seriële fractie voordat je aanneemt dat meer threads je redden, en wees eerlijk dat de eenvoudigste correcte versie vaak snel genoeg is.

### Gebruik caching en datalocaliteit, en respecteer hun kosten

Een [cache](https://en.wikipedia.org/wiki/Cache_(computing)), een snel geheugen van recent of duur berekende resultaten, is het krachtigste prestatiegereedschap dat je hebt en het gevaarlijkste. De grap van Phil Karlton dat de twee moeilijke problemen in de informatica cache-invalidatie en dingen benoemen zijn, is een waarschuwing: een verouderde cache levert foute antwoorden, en invalidatielogica is waar subtiele bugs broeden. Cache bewust, stel verlooptijden in en ken je correctheidsverhaal voordat je de hitrate optimaliseert. Op het laagste niveau benut [referentielokaliteit](https://en.wikipedia.org/wiki/Locality_of_reference), data die samen wordt gebruikt dicht bij elkaar in het geheugen houden, de CPU-cachehiërarchie en kan code meerdere malen sneller maken zonder algoritmische verandering, door cache-misses in hits te veranderen. Aaneengesloten arrays verslaan om die reden structuren met pointers. Dit raakt aan keuzes voor datalay-out in hoofdstuk 3.4.

### Benchmark eerlijk en wantrouw microbenchmarks

Een benchmark die liegt is erger dan geen, omdat ze valse zekerheid geeft. Warm op voordat je meet, zodat je het gedrag in stabiele toestand tijdt in plaats van eenmalige opstart en just-in-time-compilatie. Draai veel iteraties en rapporteer de variantie, niet één gelukkig getal. Gebruik een representatieve werklast met realistische datagroottes en -verdelingen, want een microbenchmark op een speelgoedinvoer meet vaak het vermogen van de compiler om je test te verwijderen in plaats van de echte snelheid van de code. Pas op voor de klassieke valkuilen: een waarde die de optimizer als ongebruikt bewijst en verwijdert, een lus die de runtime optilt of een cache die warm is in de benchmark en koud in productie. Meet bij twijfel het hele pad, niet de geïsoleerde functie.

### Poort prestaties in CI en observeer ze in productie

Maak van prestaties een eigenschap die de pipeline beschermt. Voeg prestatietests toe aan de strategie van hoofdstuk 2.4, met regressiepoorten die de build laten falen wanneer een sleutelbenchmark of budget verder verslechtert dan een drempel. Dit vangt het trage sluipen voordat het wordt samengevoegd. Sluit dan de lus in productie met de telemetrie van hoofdstuk 9.2: volg echte latentiepercentielen, allocatiesnelheden en trage queries tegen je budgetten, want productieverkeer vindt de gevallen die je benchmarks zich nooit voorstelden.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Nu optimaliseren op intuïtie | Voelt productief. Af en toe een gelukstreffer | Stemt meestal de verkeerde code af. Voegt complexiteit toe zonder winst |
| Eerst meten, dan optimaliseren | Richt zich op het echte knelpunt. Op bewijs gebaseerd | Vraagt tooling en discipline. Langzamer om te beginnen |
| Caching | Grote winst in latentie en doorvoer | Invalidatiebugs. Verouderde data. Geheugenkosten |
| Meer parallellisme | Hogere doorvoer op parallel werk | Plafond van Amdahl. Contentie. Concurrencybugs |
| Microoptimalisatie | Perst constante factoren uit | Laag plafond. Schaadt leesbaarheid. Vaak ruis |
| Algoritmische verbetering | Winst schaalt met invoergrootte | Vraagt analyse. Soms een grotere herschrijving |
| CI-prestatiepoorten | Stopt regressies vroeg en goedkoop | Onbetrouwbare benchmarks ondermijnen vertrouwen. Vraagt een stabiele omgeving |

De centrale spanning is inspanning tegenover opbrengst, en de oplossing is meting. Prestatiewerk heeft sterk afnemende opbrengsten: de eerste door het profiel geleide oplossing kan de latentie halveren, de tiende kan een procent afschaven terwijl de codecomplexiteit verdubbelt. Je lost het op door te weigeren te optimaliseren zonder een getal in de hand en een budget om te halen. Meet om de oplossing te vinden die de moeite waard is, en stop zodra je het budget haalt in plaats van snelheid om zichzelf na te jagen.

## Vragen om met je team te bespreken

1. **Heb je een schriftelijk prestatiebudget voor je kritieke paden, en is het uitgedrukt als percentiel?** Veel teams hebben een vaag gevoel dat dingen "snel" zouden moeten zijn maar geen getal waartegen iemand kan falen, wat betekent dat prestaties niemands taak zijn tot ze breken. Een budget als "p99 onder 300 ms" maakt het doel concreet, geeft reviewers iets om af te dwingen en maakt van een regressie een zichtbare gebeurtenis in plaats van een langzame glijbaan. Het telt het meest in grote teams, waar latentie door veel handen binnensluipt en geen enkele auteur de cumulatieve kosten ziet. Neem je huidige latentiedata mee en vraag of je gemiddelden rapporteert, die je vleien, of percentielen, die de waarheid vertellen. Als je niet kunt zeggen wat "snel genoeg" als getal betekent, is dat het eerste wat je moet repareren.

2. **Toen je voor het laatst iets optimaliseerde, vertelde een profiler je waar je moest kijken, of gokte je?** Het knelpunt zit berucht ergens anders dan waar ervaren engineers het verwachten, en tijd besteed aan het afstemmen van de verkeerde code is tweemaal verloren tijd, eenmaal in het werk en eenmaal in de toegevoegde complexiteit. Een cultuur die eerst profileert besteedt haar inspanning waar het loont en laat heldere code met rust. Vraag je team de laatste drie prestatieoplossingen te herinneren en of elk begon met een meting of een gok. Overweeg of je in productie kunt profileren, of in een realistische stagingomgeving, want een profiel van een laptop kan ernstig misleiden. Het antwoord onthult of je prestatiewerk engineering is of folklore.

3. **Wat stopt vandaag een prestatieregressie om productie te bereiken?** In een groeiend team is het eerlijke antwoord vaak "een klantenklacht", wat betekent dat gebruikers je regressietest zijn. Een CI-poort die de build laat falen wanneer een benchmark of budget verslechtert, vangt het probleem terwijl het goedkoop te herstellen is en de auteur zich de wijziging nog herinnert. Bespreek of je benchmarks stabiel genoeg zijn om op te poorten, want een onbetrouwbare prestatietest die wolf roept zal worden genegeerd of uitgeschakeld. Praat ook over wat je in productie bewaakt, aangezien sommige regressies alleen onder echt verkeer en echte data verschijnen. Het doel is prestaties een eigenschap te maken die het systeem automatisch verdedigt, niet een die je bij een incident herontdekt.

4. **Optimaliseer je voor latentie of doorvoer op elk kritiek pad, en heeft iemand die keuze opgeschreven?** Dit zijn verschillende doelen die in tegengestelde richting trekken: batchen en parallelle workers verhogen doorvoer maar kunnen latentie toevoegen aan individuele verzoeken, dus een team dat op instinct optimaliseert koopt vaak de verkeerde as en laat gebruikers wachten om machinetijd te besparen waaraan niemand tekort had. In een groot team vermenigvuldigt het gevaar zich, omdat de ene groep een gedeelde service afstemt op bulkdoorvoer terwijl een andere ervan afhangt voor interactieve latentie, en geen van beide het doel van de ander kent. Neem het werkelijke gebruikspatroon van elk pad mee (interactief verzoek tegenover achtergrondbatch), de huidige percentiellatentie en de aanhoudende doorvoer die je nodig hebt, en besluit de as dan expliciet in plaats van een standaard te laten ontstaan. Noem voor een systeem van onderneming of overheid onder een SLA op welke maat de overeenkomst is geschreven, want de ongemeten as optimaliseren kan een contract schenden terwijl je dashboards er gezond uitzien.

5. **Hoe weet je dat je benchmarks echt werk meten in plaats van dat de optimizer je test verwijdert?** Een benchmark die liegt is erger dan geen, omdat ze het team valse zekerheid geeft en er dan toch een regressie wordt opgeleverd. Teams rapporteren routinematig één gelukkig getal uit een koude run op een speelgoedinvoer, wat opstart, just-in-time-compilatie en het vermogen van de compiler om ongebruikte code te verwijderen meet in plaats van het gedrag dat gebruikers werkelijk raken. Neem een voorbeeldbenchmark mee en ondervraag hem: warmt hij op, draait hij veel iteraties, rapporteert hij variantie, gebruikt hij representatieve datagroottes en -verdelingen en verslaat hij eliminatie van dode code op zijn resultaat. De concurrerende trek is dat eerlijke benchmarks langzamer te schrijven en te draaien zijn dan snelle microbenchmarks, dus spreek af waar goedkope benaderingen acceptabel zijn en waar je rigueur eist. Leg in een publieke of gereguleerde setting, waar aanbestedings- en toezichthoudende organen je zullen vragen de cijfers te reproduceren, het apparaat, de werklast en de omgeving naast het resultaat vast zodat de bewering kan worden geverifieerd in plaats van alleen beweerd.

6. **Wanneer prestatiewerk met functies strijdt om dezelfde engineers, hoe beslis je, en wie heeft de budgetbevoegdheid?** Prestaties hebben sterk afnemende opbrengsten, dus de eerste door het profiel geleide oplossing kan de latentie halveren terwijl de tiende een procent afschaaft voor dubbele codecomplexiteit, en zonder regel wint de luidste stem of de dichtstbijzijnde deadline. De concurrerende overwegingen zijn echt: onopgeloste prestatieschuld stapelt zich stilletjes op en wordt duurder om achteraf in te bouwen, maar snelheid najagen voorbij het budget laat de roadmap verhongeren en voegt complexiteit toe die toekomstig werk vertraagt. Neem de huidige budgetstatus voor elk kritiek pad mee, de geschatte kosten van de status quo in machines of verloren conversie en de marginale opbrengst van de volgende optimalisatie, zodat de afweging op bewijs wordt gemaakt in plaats van onder druk. Noem voor een groot ondernemings- of overheidsprogramma wie het prestatiebudget bezit en wie engineeringtijd ertegen mag autoriseren, want een doel waarvoor niemand verantwoordelijk is het te verdedigen erodeert stilletjes.

## Sectorperspectief

**Startup.** Snelheid van oplevering verslaat proces, dus weersta herschrijvingen en grootse prestatieframeworks. Besteed een middag met een profiler aan het pad waarover gebruikers werkelijk klagen, repareer de grootste kost (vaak een N+1-query of een toevallige lineaire scan) en voeg één lichtgewicht percentielbudget toe aan CI zodat de winst niet ongemerkt kan regresseren. Bewaar diepe optimalisatie voor het moment dat een echt getal, geen gok, zegt dat de code te traag is.

**Kleinbedrijf.** Zonder prestatiespecialist en met een krap budget leun je op de tools die je al betaalt: de profiler in je runtime, de latentiepercentielen in je hostingdashboard en de ingebouwde queryanalyser in je database. Stel een of twee eenvoudige budgetten vast gekoppeld aan iets wat klanten voelen, zoals paginalaad- of checkouttijd, en behandel een overschrijding als signaal om een snellere tier te kopen of de slechtste query te repareren in plaats van een afstemmingsproject te starten dat je niet kunt bemannen.

**Grote onderneming.** Op vlootschaal zijn prestaties directe kosten, dus bestuur ze als gedeelde discipline: standaard profileertools, percentielbudgetten gekoppeld aan bedrijfsstatistieken en CI-regressiepoorten consistent toegepast zodat het trage sluipen van geen enkel team de hele cloudrekening opblaast. Volg latentie, allocatie en doorvoer tegen uitgangswaarden over services, en bewaar reproduceerbaar benchmarkbewijs, want een CPU-reductie van 30% op een grote vloot is een terugkerende besparing die het waard is te auditen en te verdedigen tegen SLA-boetes.

**Overheid.** Prestaties zijn een toegangsgarantie: een pagina die laadt op een oude telefoon via een zwakke verbinding bepaalt of een burger een uitkeringsaanvraag voltooit. Stel expliciete budgetten vast tegen realistische low-end apparaten en afgeknepen netwerken, en publiceer reproduceerbare benchmarkresultaten die het apparaat, het netwerk en de werklast vastleggen, zodat aanbestedings- en toezichthoudende organen de cijfers kunnen verifiëren in plaats van op goed vertrouwen aan te nemen. Geef de voorkeur aan transparante, controleerbare meting boven beweringen van leveranciers, en houd leveranciers aan hetzelfde reproduceerbare bewijs.

## Voorbeelden

**Startup.** Een klein SaaS-team merkt dat hun dashboard traag aanvoelt en is in de verleiding het in een sneller framework te herschrijven. In plaats daarvan besteden ze een middag aan een profiler en een flamegraph, die toont dat 70% van de verzoektijd één endpoint is dat één databasequery per rij uitvoert, het klassieke N+1-patroon. Ze vervangen het door één gebatchte query, de latentie daalt van 1,2 seconden naar 90 milliseconden en ze voegen een p99-budget van 200 ms toe aan een lichtgewicht CI-benchmark zodat de oplossing niet ongemerkt kan regresseren. Geen herschrijving, één middag, een tienvoudige winst.

**Grote onderneming.** Een retailplatform draait duizenden instanties, en zijn cloudrekening wordt gedomineerd door één aanbevelingsservice. Een profileercampagne vindt zware allocatieomloop die frequente garbage-collection-pauzes veroorzaakt, plus een cache met een slechte hitrate. Datastructuren afstemmen op lokaliteit en de cachesleutels repareren verlaagt de CPU per verzoek met 40%, waardoor het team hetzelfde verkeer op 40% minder machines kan draaien. De besparing betaalt de engineeringinspanning in weken terug, en een p99-latentie-SLA die af en toe werd geschonden houdt nu ruimschoots stand, wat contractuele boetes vermijdt.

**Overheid.** Een nationale belastingdienst moet burgers bedienen op oude apparaten en trage plattelandsverbindingen. Het team stelt een expliciet budget vast: de aangiftepagina moet binnen 3 seconden interactief worden op een low-end telefoon via een afgeknepen 3G-profiel. Ze profileren de pagina, snijden het interactiviteitsblokkerende werk weg en publiceren reproduceerbare benchmarkresultaten, met vastlegging van het apparaat, het netwerk en de werklast, zodat toezichthoudende organen en toegankelijkheidsauditors de bewering kunnen verifiëren in plaats van op goed vertrouwen aan te nemen. Prestaties zijn hier geen kostenhefboom maar een toegangsgarantie die de dienst voor iedereen bruikbaar houdt.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van performance engineering toont zich in drie grootboeken. Het eerste is infrastructuurkosten: snellere code doet hetzelfde werk op minder machines, en voor een grote vloot is een CPU-reductie van 30% een directe, terugkerende besparing die de eenmalige engineeringinspanning in de schaduw stelt. Het tweede is omzet en tevredenheid: latentie correleert met conversie, afhaken en gebruikersvertrouwen, dus de staart afschaven is een groeihefboom, niet alleen een hygiënetaak. Het derde is vermeden risico: een SLA-schending draagt boetes, en een lancering die onder belasting smelt draagt reputatieschade en brandweerkosten.

De total cost of ownership is bescheiden en vooraf geladen. Je investeert in profileertools, een stabiele benchmarkomgeving en CI-poorten, plus de discipline om budgetten te schrijven en profielen te lezen. De grotere, verborgen kosten zijn het alternatief: prestatieschuld stapelt zich stilletjes op, en snelheid achteraf inbouwen in een traag systeem na de lancering is veel duurder dan haar continu beschermen. Maak de zakelijke onderbouwing voor het bestuur in hun eigen eenheden. Vertaal latentie in conversie of voltooiingspercentages van burgers, vertaal CPU in maandelijkse cloudkosten en vertaal een regressiepoort in vermeden incidenten. Het sterkste argument is dat prestaties goedkoop zijn te beschermen commit voor commit en ruïneus om te herstellen nadat ze zijn weggerot.

## Antipatronen en valkuilen

- **Optimaliseren zonder te profileren.** Code afstemmen die niet het knelpunt is terwijl de echte kost onaangeroerd blijft.
- **Voortijdige optimalisatie.** Helderheid opofferen voor ingebeelde snelheid die de profiler nooit zou hebben gemarkeerd.
- **Gemiddelden rapporteren.** Een pijnlijke staart verbergen achter een comfortabel gemiddelde. Gebruikers voelen p99, niet het gemiddelde.
- **Microbenchmarktheater.** Getallen van een speelgoedwerklast die de optimizer half verwijderde, zonder opwarming of gerapporteerde variantie.
- **Cache zonder invalidatieverhaal.** De hitrate najagen terwijl verouderde of foute data wordt geleverd.
- **Aannemen dat meer threads helpen.** De wet van Amdahl en de seriële fractie negeren en dan verdrinken in contentie.
- **Geen regressiepoort.** Gebruikers de prestatietest laten zijn omdat niets in CI het budget bewaakt.
- **De verkeerde as optimaliseren.** Doorvoer kopen met batchen terwijl gebruikers lage latentie nodig hadden, of andersom.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Prestaties worden alleen aangepakt wanneer iets breekt. Geen budgetten, geen profileergewoonte, geen benchmarks. Optimalisatie is gokwerk gedreven door intuïtie, en gemiddelden zijn de enige statistiek die iemand rapporteert.
- **Niveau 2, Ontwikkelen:** Sommige teams profileren tijdens incidenten en houden een paar benchmarks bij, maar de praktijk is inconsistent en hangt af van individuele gedrevenheid. Budgetten bestaan informeel voor een of twee kritieke paden en percentielen verschijnen op sommige dashboards, maar niets poort een regressie voordat ze wordt opgeleverd en elk team vindt zijn eigen aanpak opnieuw uit.
- **Niveau 3, Standaardiseren:** Kritieke paden dragen schriftelijke percentielbudgetten, en profileren is de gedocumenteerde, verwachte eerste stap voordat iemand optimaliseert. CI bevat prestatietests met regressiepoorten, regels voor eerlijk benchmarken (opwarming, variantie, representatieve data) zijn opgeschreven en organisatiebreed gehandhaafd, en elk team volgt dezelfde methode in plaats van zijn eigen.
- **Niveau 4, Beheersen:** De organisatie meet prestaties als beheerste eigenschap. Latentiepercentielen, doorvoer, allocatiesnelheden en aantallen trage queries worden gevolgd tegen expliciete uitgangswaarden in productie en CI, regressies worden gekwantificeerd tegen drempels in plaats van bediscussieerd, en budgetten zijn gekoppeld aan bedrijfsstatistieken zoals conversie of cloudkosten zodat een overschrijding een met data onderbouwde beslissing triggert. Benchmarkbewijs is reproduceerbaar en vastgelegd met zijn apparaat, werklast en omgeving voor audit.
- **Niveau 5, Orkestreren:** Prestaties worden continu verbeterd en zijn over de organisatie geïntegreerd. Budgetten, profileren, eerlijk benchmarken en flamegraph-analyse zijn routinevaardigheden, regressiepoorten zijn stabiel en vertrouwd, en productie- en CI-data sluiten de lus automatisch. De organisatie past budgetten aan naarmate verkeer, hardware en bedrijfsprioriteiten verschuiven, herbalanceert inspanning naar de paden waar de opbrengst het hoogst is en verdedigt prestaties als blijvende eigenschap in plaats van periodieke campagne.

## Ideeën voor discussie

1. Welk van je kritieke paden heeft vandaag een schriftelijk, op percentielen gebaseerd budget, en welke worden alleen door hoop beschermd?
2. Wanneer verraste een profiler je voor het laatst, en wat leerde dat je over waar je denkt dat tijd heen gaat?
3. Warmen je benchmarks op, rapporteren ze variantie en gebruiken ze representatieve data, of meten ze de optimizer?
4. Waar geef je machines uit om code toe te dekken die een profileercampagne goedkoper zou kunnen maken?
5. Wat is voor je meest geparallelliseerde werklast de seriële fractie, en begrenst de wet van Amdahl de versnelling die je najaagt?
6. Als een teamgenoot een wijziging samenvoegde die de p99-latentie verdubbelde, hoe lang duurt het voor iemand het merkte, en hoe zouden ze het ontdekken?

## Belangrijkste inzichten

- Meet voordat je optimaliseert. Het knelpunt zit zelden waar je denkt, en voortijdige optimalisatie kost helderheid zonder winst.
- Definieer "snel genoeg" als percentielbudget, omdat gemiddelden de staart verbergen waar echte gebruikers wonen.
- Geef de voorkeur aan algoritmische winst (een betere big-O-klasse) boven microtuning, en weet of je latentie of doorvoer nodig hebt.
- Respecteer de grenzen van parallellisme (wet van Amdahl) en de gevaren van caching (invalidatie en veroudering).
- Benchmark eerlijk met opwarming, variantie en representatieve werklasten, en wantrouw microbenchmarks.
- Poort prestaties in CI (hoofdstuk 2.4) en observeer ze in productie (hoofdstuk 9.2). Vul het systeemniveau in hoofdstuk 3.5 aan.
- Prestaties zijn kosten voor ondernemingen, toegang voor overheden, en goedkoop continu te beschermen maar duur om achteraf in te bouwen.

## Referenties en verder lezen

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimisation maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behaviour in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
