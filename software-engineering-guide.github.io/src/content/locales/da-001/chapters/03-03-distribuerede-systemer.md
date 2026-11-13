# 3.3 Distribuerede systemer

## Overblik og motivation

Et [distribueret system](https://en.wikipedia.org/wiki/Distributed_computing) er ethvert system, hvis komponenter kører på mere end én maskine og koordinerer over et netværk. I det øjeblik du krydser en procesgrænse over et netværk, arver du nogle hårde sandheder, der simpelthen ikke findes inde i en enkelt proces. Netværket er upålideligt, og dets latens varierer. Beskeder kan gå tabt, duplikeres, forsinkes eller omordnes. Fjerne komponenter fejler af sig selv. Der er intet fælles ur. De klassiske "[fejlslutninger om distribueret databehandling](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)" (netværket er pålideligt, latens er nul, båndbredde er uendelig, topologien ændrer sig aldrig) navngiver præcis de antagelser, der forårsager nedbrud. Dit job er at designe til disse realiteter fra begyndelsen, frem for at genopdage dem under en hændelse.

For en stor organisation er distribution ikke valgfri. Ethvert system, der betjener national eller global skala, forbinder flere afdelinger eller har brug for høj tilgængelighed, vil spænde over mange maskiner, datacentre og ofte regioner. Virksomheder driver distribuerede transaktionssystemer, hændelsespipelines og udrulninger i flere regioner. Det offentlige driver integrationer mellem myndigheder, hvor hver myndighed ejer sine egne systemer, og ingen kontrollerer helheden. Her viser kløften mellem et robust og et skrøbeligt design sig som overskriftsnedbrud, missede ydelsesudbetalinger og regulatoriske konsekvenser. Teknikkerne i dette kapitel (konsistensræsonnement, [idempotens](https://en.wikipedia.org/wiki/Idempotence), genforsøg med backoff, [circuit breakers](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern), [sagaer](https://en.wikipedia.org/wiki/Long-running_transaction) og distribueret observerbarhed) er dine standardforsvar.

Den sværeste del af distribuerede systemer er, at fejl er delvise og intermitterende. Et program på en enkelt maskine virker enten eller crasher. Et distribueret system kan være halvt fungerende: nogle anmodninger lykkes, nogle får timeout, og nogle går stille tabt, alt sammen på én gang. Dette kapitel fokuserer på de ræsonnementer og mønstre, der lader et stort team bygge systemer, der nedgraderer elegant og forbliver forståelige under delvis fejl.

## Grundprincipper

- **Netværket er ikke pålideligt.** Design hver fjerninteraktion under antagelse af, at den kan være langsom, fejle, duplikere eller omordne.
- **Du kan ikke få perfekt konsistens og perfekt tilgængelighed under en partition.** Vælg bevidst pr. interaktion (CAP/PACELC), og husk at latens er en omkostning, selv når der ikke er nogen partition.
- **Gør operationer idempotente.** Hvis en operation sikkert kan gentages, bliver det meste distribueret fejlhåndtering overkommeligt.
- **Hvert fjernkald har brug for en timeout.** Ubegrænsede ventetider forvandler én langsom afhængighed til et systemdækkende nedbrud.
- **Foretræk eventual consistency, hvor forretningen tillader det, men gør det eksplicit.** Brugere og revisorer skal forstå, hvornår de kan se forældede data.
- **Isolér fejl.** Skotter og circuit breakers forhindrer, at én fejlende komponent kaskaderer ind i dem alle.
- **Du kan ikke fejlsøge det, du ikke kan se.** Distribuerede flows kræver korreleret sporing, målinger og logs på tværs af hvert spring.
- **"Præcis-én-gang-levering" er en myte; præcis-én-gang-*behandling* er en ingeniørpræstation.** Design til mindst-én-gang med deduplikering.

## Anbefalinger

### Ræsonnér om konsistens med CAP og PACELC

[CAP-sætningen](https://en.wikipedia.org/wiki/CAP_theorem) siger, at et system under en netværkspartition må vælge mellem konsistens (hver læsning ser den seneste skrivning) og tilgængelighed (hver anmodning får et svar). [PACELC](https://en.wikipedia.org/wiki/PACELC_design_principle) tilføjer en anden afvejning: **E**lse (når der ikke er nogen partition) afvejer du stadig **L**atens mod **C**onsistency. Stempl ikke dette som en etiket på hele systemet. Beslut det pr. operation. En banks saldooverførsel kræver stærk konsistens og vil afvise frem for at risikere dobbeltforbrug. Et socialt feed eller en produktvisningstæller kan acceptere forældelse til gengæld for tilgængelighed og hastighed. Skriv ned, hvilken konsistensmodel hvert dataflow bruger (stærk, kausal, læs-dine-skrivninger eller eventual), så ingen antager en garanti, systemet faktisk ikke giver.

### Byg idempotens, timeouts, genforsøg og backoff sammen

Behandl disse fire teknikker som én pakke. Giv hver fjernoperation en **timeout**, så en hængt afhængighed ikke kan blokere en tråd for evigt. Ved fejl så **prøv igen**, men kun for operationer, der er sikre at gentage. Sikre at gentage betyder **idempotente**: tildel hver anmodning en unik nøgle og lad modtageren deduplikere, så en gentaget "debitér kort" ikke debiterer to gange. Afstem dine genforsøg med **[eksponentiel backoff](https://en.wikipedia.org/wiki/Exponential_backoff) og jitter**, så du undgår en synkroniseret genforsøgsstorm, der forvandler et kort glimt til et selvforskyldt [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack). Begræns antallet af genforsøg og det samlede tidsbudget, for at prøve for evigt flytter blot fejlen. Uden idempotens er genforsøg farlige. Uden backoff er genforsøg destruktive.

### Tilføj circuit breakers og skotter for at stoppe kaskader

En **circuit breaker** holder øje med kald til en afhængighed og "åbner" efter en tærskel af fejl: den fejler hurtigt i en afkølingsperiode i stedet for at stable flere anmodninger på en kæmpende tjeneste, og "halvåbner" derefter for at teste genopretning. Det stopper den kaskade, hvor en langsom nedstrøms tjeneste udtømmer hver kalders tråde, til hele systemet går i stå. **Skotter** (bulkheads) partitionerer ressourcer (trådpuljer, forbindelsespuljer), så mætning i én afhængighed ikke kan æde den kapacitet, andre har brug for. Par begge med elegant nedgradering: når en ikke-kritisk afhængighed er utilgængelig, så returnér cachede eller standardsvar frem for at fejle hele anmodningen.

### Styr distribuerede transaktioner med sagaer, ikke totrinscommit

Du kan som regel ikke holde en enkelt [ACID](https://en.wikipedia.org/wiki/ACID)-transaktion (Atomicity, Consistency, Isolation, Durability) på tværs af flere tjenester eller databaser. Distribueret [totrinscommit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) er langsomt, låser ressourcer og skærer tilgængelighed. Brug i stedet **saga-mønstret**. Modellér en forretningstransaktion som en sekvens af lokale transaktioner, der hver udgiver en hændelse, som udløser den næste, med en **kompenserende handling** for hvert trin til at fortryde det, hvis et senere trin fejler. Sagaer kommer i to varianter. **Koreografi** lader tjenester reagere på hinandens hændelser uden en central controller. **Orkestrering** lader en central koordinator drive trinene, hvilket er lettere at ræsonnere om og overvåge. Sagaer omfavner eventual consistency: systemet passerer gennem mellemtilstande og konvergerer derefter. Så design brugeroplevelsen og revisionssporet til at tage højde for "i gang"- og "kompenseret"-tilstande.

### Behandl præcis-én-gang som mindst-én-gang plus deduplikering

[Beskedmæglere](https://en.wikipedia.org/wiki/Message_broker) kan ikke reelt garantere præcis-én-gang-levering på tværs af fejl. Det, de og du *kan* opnå, er **mindst-én-gang-levering med idempotent behandling**, som giver præcis-én-gang-*effekter*. Design forbrugere til at håndtere duplikerede beskeder sikkert ved hjælp af idempotensnøgler eller en log over behandlede beskeder. Kend din mæglers rækkefølge- og leveringsgarantier præcist. Til streaming så brug forbrugergrupper, partitioner og offsetstyring med vilje, og gør genbehandling sikker, så du kan afspille en strøm igen efter en fejlrettelse uden at korrumpere nedstrøms tilstand.

### Instrumentér distribuerede flows fra ende til anden

Adoptér observerbarhedens tre søjler, korreleret på tværs af tjenestegrænser. Propagér et **spor-/korrelations-ID** gennem hvert spring, så du kan følge en enkelt brugeranmodning på tværs af alle de tjenester, den rører (distribueret sporing). Udsend strukturerede **målinger** (latenspercentiler, fejlrater, mætning, gennemløb) pr. tjeneste og pr. afhængighed. Udsend strukturerede **logs**, der bærer korrelations-ID'et. Brug alt dette til at sætte serviceniveaumål og til at alarmere på symptomer, brugere faktisk mærker, såsom fejlrate og latens, frem for kun på sundheden af enkelte maskiner. I et distribueret system er observerbarhed ikke valgfrit værktøj. Det er den eneste måde at forstå adfærd under delvis fejl.

## Afvejninger: fordele og ulemper

| Teknik | Fordele | Ulemper / omkostning |
|---|---|---|
| Stærk konsistens | Simpel mental model, ingen forældede læsninger | Lavere tilgængelighed under partitioner, højere latens, koordinationsomkostning |
| Eventual consistency | Høj tilgængelighed, lav latens, skalerbar | Forældede læsninger, kompleks ræsonnering, kræver konfliktløsning |
| Genforsøg med backoff | Rider transiente fejl af automatisk | Forstærker belastning hvis misbrugt; kræver idempotens og grænser |
| Circuit breakers / skotter | Forebygger kaskadefejl, fejler hurtigt | Ekstra kompleksitet, justering af tærskler, risiko for for tidlig udløsning |
| Saga (vs 2PC) | Skalerbar, tilgængelig, ingen distribuerede låse | Eventual consistency, kompensationslogik, sværere at ræsonnere om |

Den overordnede afvejning er mellem koordinering og uafhængighed. Hver garanti, du vil have på tværs af maskiner (konsistens, rækkefølge, præcis-én-gang), koster latens, tilgængelighed eller kompleksitet. Den kræver, at maskiner er enige, og enighed over et upålideligt netværk er dyr. Færdigheden er kun at købe de garantier, forretningen virkelig har brug for, operation for operation, og at designe alt andet til elegant nedgradering. Overkøb konsistens, og jeres systemer bliver langsomme og skrøbelige. Underkøb den, og I får stille datakorruption, der viser sig som et revisionssvigt måneder senere.

## Spørgsmål til drøftelse med dit team

1. **Leveres jeres robusthedsmønstre som fælles platformsstandarder, eller genopfinder hvert team timeouts og genforsøg?** Kapitlet behandler idempotens, timeouts, afgrænsede genforsøg, circuit breakers og sporing som billigst og mest pålidelige, når de bygges én gang ind i fælles biblioteker og platformsstandarder. I en stor organisation garanterer det ensartethedsfejl at lade hvert team håndrulle dem: nogle stier prøver ikke-idempotente operationer igen, nogle har ingen timeout, nogle udsender intet korrelations-ID. Tag dokumentation med ved at revidere en stikprøve af tjenester og tælle, hvor mange der sætter en eksplicit timeout på hvert fjernkald og propagerer et spor-ID fra ende til anden. Hvis det tal er lavt, er rettelsen en platformsinvestering, ikke et uddannelsesnotat. Standardstandarder gør også robusthed testbar og reviderbar, hvilket tilsynsmyndigheder i finans og det offentlige i stigende grad forventer, at I kan påvise.

2. **Komponerer jeres timeouts og genforsøgsbudgetter på tværs af hele kaldekæden, eller genforsøger en dyb anmodning sig selv ind i et nedbrud?** En enkelt anmodning krydser ofte mange spring, og hvis hvert lag uafhængigt prøver igen tre gange med sin egen timeout, multipliceres den inderste fejl, og den ydre kalder venter langt ud over enhver menneskeligt tolerabel grænse. Sæt et samlet tidsbudget for den brugervendte anmodning og del det ned gennem kæden, så en indre tjeneste ved, hvor lidt tid den har tilbage, og fejler hurtigt frem for at genforsøge ind i en storm. Tag jeres afhængighedsgraf og et reelt spor med, læg derefter den værst tænkelige kombination af timeout og genforsøg sammen og sammenlign den med, hvad brugeren faktisk vil vente. Eksponentiel backoff med jitter og en grænse for samlede forsøg holder et kort glimt fra at blive et selvforskyldt denial of service. Dybe, snakkesalige synkrone kæder er fjenden her, så svaret kan skubbe jer mod asynkrone flows eller færre spring.

3. **Hvornår injicerede I sidst de fejl, jeres design påstår at overleve, og hvad gik i stykker, som I ikke havde forventet?** Robusthedsmønstre er hypoteser, indtil I får systemet til at fejle med vilje: dræb en instans, tilføj latens til en afhængighed, drop en brøkdel af beskeder, gensend en batch to gange. I et distribueret system er de interessante fejl delvise og intermitterende, så en circuit breaker eller sagakompensation, der ser korrekt ud i kode, stadig kan opføre sig forkert under en reel timeout-der-måske-gennemførte. Tag resultaterne af en faktisk game day eller fejlinjektionskørsel med, ikke et designdokument, og notér, hvilke alarmer der udløstes, hvor lang tid sporing tog om at lokalisere fejlen, og om en genforsøgsstorm opstod. I regulerede sektorer er dokumentation for, at I har testet fejl, en del af at påvise operationel robusthed over for revisorer. Hvis I aldrig har kørt en, hører det første eksperiment hjemme i et testmiljø med en stram sprængradius og en afbrydelseskontakt.

4. **Kan det ejende team for hvert større dataflow navngive den konsistensmodel, det giver, og matcher det valg, hvad forretningen faktisk har brug for?** CAP og PACELC tvinger et bevidst valg pr. operation, men i en stor organisation er standarden drift: et flow, der begyndte eventual consistent til en tæller med lav indsats, genbruges til noget, der nu godkender betalinger eller giver adgang, og ingen gentester garantien. De modstridende hensyn er reelle, da stærk konsistens koster tilgængelighed under en partition og latens, selv når der ingen er, mens eventual consistency køber hastighed til prisen af forældede læsninger og konfliktløsning, I skal designe til. Tag et katalog over jeres vigtigste dataflows med, hver mærket med sin nuværende model (stærk, kausal, læs-dine-skrivninger eller eventual) og forretningskonsekvensen af en forældet eller tabt læsning, og led så efter uoverensstemmelser, hvor garantien er stærkere eller svagere, end indsatsen berettiger. I virksomhedsfinans og i offentlige ydelses- eller identitetssystemer er en eventual consistent læsning bag en autoritativ beslutning netop den slags stille fejl, der viser sig som et revisionsfund eller en uberettiget afvisning måneder senere, så selve gennemgangen er dokumentation, revisorer vil bede om at se.

5. **Hvordan opfører jeres forretningstransaktioner over flere tjenester sig halvvejs, og hvem er ansvarlig for de kompensationer, der løser dem op?** At erstatte totrinscommit med sagaer betyder, at systemet passerer gennem synlige mellemtilstande, og et trin kan lykkes, mens et senere trin fejler og udløser en kompenserende handling, der omgør det. For et stort team rejser det hårde ejerskabsspørgsmål: godkend-debitér-kreditér-hovedbogs-kæden krydser ofte flere teams, og en kompensation, ét team glemmer at implementere, efterlader penge eller poster permanent inkonsistente. Vej koreografi, hvor tjenester reagerer på hinandens hændelser uden en central controller, og flowet er svært at se, mod orkestrering, hvor en koordinator driver og overvåger trinene på bekostning af en komponent at drive. Tag tilstandsdiagrammet for jeres vigtigste saga med, listen over kompenserende handlinger og deres ejere og dokumentation for, at "i gang"- og "kompenseret"-tilstande håndteres både i brugeroplevelsen og revisionssporet. I bankvæsen og offentlig sagsbehandling forventer tilsynsmyndigheder, at I kan rekonstruere præcis, hvad der skete med en transaktion, der fejlede midtvejs, så en ikke-modelleret mellemtilstand er et compliance-hul, ikke blot en fejl.

6. **Overlever jeres beskedforbrugere duplikeret og omordnet levering, og kan I bevise det, før mægleren tvinger spørgsmålet?** Præcis-én-gang-levering er en myte, så jeres reelle garanti er mindst-én-gang, og en forbruger, der antager, at hver besked ankommer én gang og i rækkefølge, vil dobbeltbehandle den dag, mægleren gensender en batch efter en failover. På tværs af mange teams akkumuleres risikoen, fordi én ikke-idempotent forbruger på en fælles strøm kan korrumpere nedstrøms tilstand, andre teams afhænger af, og fejlen er usynlig, til afspilning eller en partition omordner hændelser. Afvejningen er ingeniøromkostningen ved idempotensnøgler, en log over behandlede beskeder og eksplicit offset- og partitionshåndtering sat over for omkostningen ved stille korruption. Tag listen over forbrugere på jeres kritiske strømme med, notér hvilke der deduplikerer, og hvilke blot håber, og tag resultatet af en faktisk gensendelses- eller afspilningstest med frem for en forsikring om, at det nok er fint. For dataudveksling mellem offentlige myndigheder og for virksomheders hændelsespipelines er evnen til at afspille en strøm sikkert igen efter en fejlrettelse, uden at skabe duplikerede sager eller debiteringer, både en operationel nødvendighed og noget, revisorer vil se påvist.

## Sektorperspektiv

**Startup.** Med to eller tre bevægelige dele og intet platformsteam så modstå at bygge distribueret maskineri, du ikke kan bemande. Køb robusthed, hvor den bor i den SDK, din betalings- eller beskedudbyder allerede giver, og brug din knappe opmærksomhed på de to mønstre, der forebygger uigenkaldelig skade: en idempotensnøgle på hvert pengeflyttende eller kontoændrende kald og en timeout med afgrænset genforsøg, så en ustabil forbindelse aldrig dobbeltudfører. Hold antallet af netværksspring lavt, for hver synkron afhængighed, du tilføjer, er endnu en ting, der kan fejle, før du har nogen på vagt til at opdage det.

**Lille virksomhed.** Du har sandsynligvis ingen specialist i distribuerede systemer og et stramt budget, så behandl dette som et køb-ikke-byg-spørgsmål: foretræk administrerede køer, administrerede databaser og platforme, der håndterer genforsøg, rækkefølge og deduplikering for dig, frem for infrastruktur du selv skal drive. Ram din risiko ind i almindelige vendinger, vid hvilke operationer der ville skade en kunde, hvis de kørte to gange eller returnerede forældede data, og slå de idempotens- og mindst-én-gang-funktioner til, dine leverandører allerede tilbyder. Undgå at sy tjenester sammen gennem en fælles database for at forfalske en transaktion, da det stille genskaber det sværeste distribuerede problem uden værktøjerne til at styre det.

**Stor virksomhed.** Kerneproblemet er ensartethed på tværs af mange teams, så lever idempotens, timeouts, afgrænsede genforsøg, circuit breakers og korreleret sporing som fælles platformsstandarder frem for at lade hver gruppe håndrulle dem. Standardisér, hvordan konsistensmodeller og leveringsgarantier erklæres pr. flow, kør fejlinjektion og game days efter en regelmæssig kadence, og få samlede tidsbudgetter til at komponere på tværs af dybe kaldekæder, så én tjeneste ikke kan genforsøge platformen ind i et nedbrud. Styr robusthed som en målt evne med serviceniveaumål på brugersynlige symptomer, fordi en enkelt manglende timeout i jeres skala kan kaskadere til et overskriftsnedbrud.

**Offentlig sektor.** Systemer på tværs af myndigheder betyder, at ingen ejer helheden, så design til grænser, du ikke kontrollerer: holdbare køer med mindst-én-gang-levering, deduplikering på et stabilt besked-ID og korrelations-ID'er, der flyder på tværs af myndighedsgrænser og giver revisorer et spor fra ende til anden. Indkøbs- og åbenhedsregler skubber dig til at dokumentere konsistensmodellen og leveringsgarantien for hver integration og til at holde autoritative beslutninger (identitet, berettigelse, ydelse) på stærkt konsistente læsninger frem for cachede endpoints. Behandl dokumentation for testet fejl og rekonstruerbar transaktionshistorik som leverancer, da operationel robusthed og ansvarlighed over for offentligheden er kontraktlige og lovbestemte forpligtelser, ikke interne høfligheder.

## Eksempler

**Startup.** Et lille fintech-startup har blot to bevægelige dele, der taler over netværket: sin app og en tredjeparts betalingsudbyder. Selv i denne størrelse får det hver debiteringsanmodning til at bære en idempotensnøgle og pakker kaldet ind i et genforsøg med backoff, så et tabt svar på en ustabil forbindelse aldrig dobbeltdebiterer en kunde. At springe dette over føles billigt på dag ét, men den første dobbeltdebitering, der rammer en rigtig bruger, koster en supportbrand, en refusion og et knæk i tilliden, det unge firma ikke har råd til.

**Stor virksomhed.** En global samkørselsplatform behandler turbetalinger gennem en saga: godkend kort, debitér rytter, kreditér chauffør, registrér hovedbogspost, hver en lokal transaktion med en kompenserende tilbageførsel. Hvert trin bærer en idempotensnøgle, så genforsøg efter en netværkstimeout aldrig dobbeltdebiterer. Kald til svindelscoringstjenesten sidder bag en circuit breaker; når den forringes ved spidsbelastning, åbner breakeren, og ture falder tilbage til en konservativ score i stedet for at blokere hver tur. Når en kunde bestrider en tur, lader distribueret sporing ingeniører følge den på tværs af et dusin tjenester på sekunder.

**Offentlig sektor.** En national identitetstjeneste bruges af mange myndigheder til verifikation. Den tilbyder en stærkt konsistent læsning til autoritative statuskontroller (I må ikke godkende en ydelse mod forældede identitetsdata) plus et eventual consistent, cachet endpoint til opslag med højt volumen og lav kritikalitet. Dataudveksling mellem myndigheder kører over en holdbar beskedkø med mindst-én-gang-levering, og hver myndigheds forbruger deduplikerer på et besked-ID, så en gensendt post ikke skaber en duplikeret sag. Korrelations-ID'er flyder på tværs af myndighedsgrænser og giver revisorer et spor fra ende til anden af, hvordan en borgers data bevægede sig mellem afdelinger.

## Business case: motivation, ROI og TCO

Disciplin i distribuerede systemer købes billigt, og dens fravær betales katastrofalt. Indførelsesomkostningen er ingeniørtid til at bygge idempotens, timeouts, genforsøg, circuit breakers og sporing ind i fælles biblioteker og platformsstandarder. Det er en beskeden, mest engangs investering, der så gavner hvert team. Omkostningen ved *ikke* at indføre det måles i større nedbrud: en enkelt manglende timeout, der kaskaderer til et fuldt platformsnedbrud, en ikke-idempotent betalingssti, der dobbeltdebiterer tusindvis af kunder, eller en distribueret transaktion uden saga, der efterlader data permanent inkonsistente. Hver af dem er en overskriftshændelse med direkte omsætnings-, afhjælpnings- og omdømmeomkostning og i regulerede sektorer bøder.

Ram sagen ind over for ledelsen omkring tilgængelighed og sprængradius. Robusthedsmønstre reducerer direkte både hyppigheden og varigheden af alvorlige hændelser, de målinger direktører allerede følger som oppetid og middeltid til genopretning. Distribueret observerbarhed er den største enkeltløftestang for MTTR: teams med korreleret sporing løser hændelser på tværs af tjenester på en brøkdel af tiden. Fordi disse evner leveres bedst som fælles platformsstandarder, er deres marginale omkostning pr. team lav, og deres organisationsdækkende afkast akkumuleres. TCO-argumentet er enkelt: at bygge robusthed ind fra begyndelsen er en brøkdel af omkostningen ved at eftermontere den efter det nedbrud, der tvinger sagen.

## Anti-mønstre og faldgruber

- **Ingen timeouts.** En enkelt hængt afhængighed udtømmer hver tråd og tager hele systemet ned.
- **Genforsøg af ikke-idempotente operationer.** Duplikerede bivirkninger: dobbelte debiteringer, duplikerede poster, fordoblede e-mails.
- **Genforsøgsstorme.** Synkroniserede genforsøg uden backoff og jitter, der forstærker et lille glimt til et nedbrud.
- **At antage præcis-én-gang-levering.** At bygge forbrugere, der går i stykker på duplikerede beskeder, mægleren til sidst leverer.
- **Distribuerede transaktioner via fælles database.** At koble tjenester gennem én database for at forfalske ACID og genskabe en distribueret monolit.
- **At ignorere delvis fejl.** Kode der antager, at et fjernkald enten fuldt lykkes eller fuldt fejler, uden håndtering af "fik timeout, men gennemførte måske."
- **Ingen korrelations-ID'er.** At fejlsøge en hændelse på tværs af tjenester ved at søge i urelaterede logs på ti maskiner.
- **Snakkesalige synkrone kaldekæder.** Dybe synkrone afhængighedsgrafer, hvor ethvert langsomt spring standser hele anmodningen.

## Modenhedsmodel

- **Niveau 1: Opstart.** Fjernkald behandles som lokale kald. Timeouts mangler eller er naive, genforsøg er fraværende eller hensynsløse, og fejl kaskaderer på tværs af systemet. Der er intet fælles billede af konsistens eller levering, og fejlsøgning af en hændelse på tværs af tjenester betyder logjagt maskine for maskine bagefter.
- **Niveau 2: Udvikling.** Nogle teams tilføjer timeouts og grundlæggende genforsøg og lidt idempotens, men praksis er inkonsistent fra tjeneste til tjeneste. Logs er centraliserede, men ikke korrelerede, så sporing af en anmodning på tværs af spring er manuel. Distribuerede transaktioner håbes at virke frem for at blive modelleret, og konsistensgarantier bor i enkelte ingeniørers hoveder.
- **Niveau 3: Standardisering.** Idempotens, afgrænsede genforsøg, backoff med jitter, circuit breakers og skotter er standard i hele organisationen via fælles biblioteker. Sagaer med kompenserende handlinger håndterer transaktioner over flere tjenester, distribueret sporing med korrelations-ID'er er på plads, og hvert større dataflow dokumenterer sin konsistensmodel og leveringsgaranti. Reglerne er skrevet ned og håndhævet i hele organisationen frem for overladt til hvert team.
- **Niveau 4: Styring.** Robusthed måles mod baselines, ikke blot til stede. I følger fejlrate, latenspercentiler, mætning og gennemløb pr. tjeneste og afhængighed, holder øje med genforsøgsforhold og circuit-breaker-åbningsrater og sætter serviceniveaumål på brugersynlige symptomer. Samlede tidsbudgetter verificeres til at komponere på tværs af kaldekæder, middeltid til genopretning for hændelser på tværs af tjenester er en overvåget måling, og resultater fra fejlinjektion og game days føder de tal, der lukker porten for hver ændring.
- **Niveau 5: Orkestrering.** Robusthed er den løbende forbedrede platformsstandard, integreret i hele organisationen og adaptiv over for forhold. Fejlinjektion kører rutinemæssigt i produktion med stramme sprængradier, systemer nedgraderer elegant ved design, og konsistens- og leveringsvalg genbesøges, efterhånden som belastning og forretningsindsats skifter. Målingerne fra niveau 4 driver automatiserede responser og støt arkitektonisk udvikling, så det distribuerede landskab bliver mere robust med hver hændelse frem for blot at overleve den.

## Idéer til drøftelse

1. Hvilke af jeres kritiske operationer er reelt idempotente i dag, og hvilke er stille ikke?
2. Kan jeres team for hvert større dataflow angive konsistensmodellen og leveringsgarantien udenad?
3. Hvor ville en circuit breaker have forebygget jeres sidste kaskadenedbrud?
4. Hvor lang tid tager det i øjeblikket at spore en enkelt fejlende anmodning på tværs af alle de tjenester, den rører?
5. Hvilke af jeres "distribuerede transaktioner" støtter sig til held, og hvilke er ægte sagaer med kompensationer?
6. Hvis jeres beskedmægler gensendte hver besked to gange i en time, hvad ville gå i stykker?

## Vigtigste pointer

- Antag at netværket er upålideligt og fejl er delvise; design hver fjerninteraktion til langsomhed, tab, duplikering og omordning.
- Beslut konsistens versus tilgængelighed pr. operation med CAP/PACELC; dokumentér den model, hvert flow giver.
- Idempotens, timeouts, afgrænsede genforsøg og backoff-med-jitter er én pakke; adoptér aldrig genforsøg uden de tre andre.
- Circuit breakers og skotter indeholder fejl; sagaer med kompensationer erstatter uarbejdbare distribuerede transaktioner.
- Behandl levering som mindst-én-gang og gør behandling idempotent for at opnå præcis-én-gang-effekter.
- Korreleret sporing, målinger og logs er den eneste måde at forstå og drive distribuerede flows på.

## Referencer og videre læsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew Tanenbaum and Maarten van Steen, *Distributed Systems: Principles and Paradigms*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Sam Newman, *Building Microservices*
- Chris Richardson, *Microservices Patterns* (sagas, transactional messaging)
- Eric Brewer, "CAP Twelve Years Later" and Daniel Abadi on PACELC
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"
- Cindy Sridharan, *Distributed Systems Observability*
- Nassim Nicholas Taleb's notion of antifragility (as applied by resilience-engineering literature)
