# 3.10 Indlejrede systemer og realtidssystemer

## Overblik og motivation

Et [indlejret system](https://en.wikipedia.org/wiki/Embedded_system) er software, der kører på en enhed frem for på en almindelig computer. Det lever inde i en bil, en pacemaker, en termostat, en fabriksrobot eller en styreenhed. Softwaren er dedikeret til den enhed, og enheden har som regel stramme grænser for hukommelse, processorkraft og energi. Du kan ikke altid tilføje flere ressourcer ved at klikke på en knap i en cloud-konsol. Det, du leverer, er ofte det, der kører i årevis.

Et [realtidssystem](https://en.wikipedia.org/wiki/Real-time_computing) er et, hvor korrekthed afhænger af timing, ikke blot af at producere det rigtige svar. En airbagcontroller, der beregner en perfekt udløsningskommando et sekund for sent, har fejlet totalt. Realtidsarbejde tilføjer et hårdt spørgsmål til hver opgave: vil denne blive færdig til sin deadline, hver gang, i det værst tænkelige tilfælde? Det er en anden disciplin end den gennemløb-først-tænkning, der er almindelig i web- og cloud-software.

For en stor organisation betyder dette mere, end det først ser ud. Virksomheder bygger forbundne biler, medicinsk udstyr, industrielle controllere og milliarder af [tingenes internet](https://en.wikipedia.org/wiki/Internet_of_things) (IoT)-enheder. Det offentlige driver forsvarsplatforme, flyelektronik, elnetcontrollere og medicinske tilsynsmyndigheder. I disse domæner kan en softwarefejl skade mennesker, standse en produktionslinje eller kompromittere national sikkerhed. Reglerne her er strengere, testningen er sværere, og standarderne er juridisk bindende. Dette kapitel hjælper dig med at bygge software, der er korrekt, rettidig, sikker og tryg under reelle begrænsninger. Det hænger sammen med softwarekonstruktion (kapitel 2.9), distribuerede systemer (kapitel 3.3), skalerbarhed og ydeevne (kapitel 3.5), infrastruktur- og cloudsikkerhed (kapitel 4.3) og softwarevedligeholdelse (kapitel 3.7).

## Grundprincipper

- **Timing er et korrekthedskrav, ikke en ydeevnefinesse.** Et sent svar kan være et forkert svar.
- **Design til det værst tænkelige tilfælde, ikke gennemsnittet.** Realtidsgarantier hviler på worst-case-adfærd, ikke typisk hastighed.
- **Determinisme slår rå hastighed.** Et forudsigeligt system, der altid overholder sin deadline, slår et hurtigere, der nogle gange misser.
- **Ressourcer er endelige og faste.** Budgettér hukommelse, CPU-cyklusser og energi lige så bevidst, som du budgetterer penge.
- **Sikkerhed og tryghed konstrueres ind, ikke tilføjes senere.** I regulerede domæner skal du vise dit arbejde, ikke blot påstå kvalitet.
- **Hardwaren er en del af systemet.** Du kan ikke ræsonnere om softwaren uden at ræsonnere om chippen, sensorerne og fysikken.
- **Feltopdateringer er en livscyklusevne, ikke en eftertanke.** Enheder i verden har brug for en sikker måde at modtage rettelser på.

## Anbefalinger

### Klassificér hvert timingkrav som hårdt, fast eller blødt

Ikke alle deadlines er ens. En hård realtidsdeadline må aldrig misses, fordi en miss forårsager systemfejl eller skade: tænk motorstyring eller flyvekontrolflader. En fast deadline tåler sjældne misses, men et sent resultat er ubrugeligt og kasseres. En blød realtidsdeadline nedgraderer værdi elegant: en videoramme, der ankommer lidt for sent, sænker kvaliteten, men forårsager ingen katastrofe. Mærk hver timingfølsom opgave med dens klasse, fordi indsatsen, testens stringens og omkostningen adskiller sig enormt. To egenskaber beskriver timingadfærd. [Latens](https://en.wikipedia.org/wiki/Latency_%28engineering%29) er forsinkelsen mellem en hændelse og svaret. [Jitter](https://en.wikipedia.org/wiki/Jitter) er variationen i den latens fra den ene forekomst til den næste. Hårde realtidssystemer bekymrer sig lige så meget om at begrænse jitter som om at sænke latens, fordi forudsigelighed er det, der lader dig bevise, at en deadline altid overholdes.

### Vælg dit eksekveringsfundament bevidst: RTOS eller bare metal

Du har to hovedfundamenter. Bare-metal firmware kører direkte på hardwaren uden operativsystem og bruger en simpel løkke og afbrydelseshåndterere. Det er den mindste og mest forudsigelige mulighed, og det passer til små enheder med ét klart job. Et [realtidsoperativsystem](https://en.wikipedia.org/wiki/Real-time_operating_system) (RTOS) er et lille operativsystem, der skedulerer opgaver efter prioritet og garanterer timinggrænser. Det giver dig flere opgaver, en skeduler og tjenester som timere og beskedkøer, mens timingen holdes forudsigelig. Vælg et RTOS, når du har flere samtidige opgaver med forskellige deadlines. Vælg bare metal, når enheden er meget begrænset, eller timingen skal være bevisligt enkel. Til hårdt realtidsarbejde så foretræk en præemptiv prioritetsbaseret skeduler, og analysér den med en metode som rate-monotonic scheduling, som tildeler prioriteter efter opgavefrekvens og lader dig bevise, at opgavesættet kan skeduleres.

### Budgettér hukommelse, CPU og strøm som førsteklasses ressourcer

Behandl hver knap ressource som et budget med et hårdt loft. For hukommelse så foretræk statisk allokering frem for dynamisk allokering på heapen, fordi dynamisk hukommelse kan fragmentere og kan fejle uforudsigeligt i det værst mulige øjeblik. Mange sikkerhedsstandarder begrænser eller forbyder heapbrug efter opstart netop af den grund. For CPU så mål [værst tænkelige eksekveringstid](https://en.wikipedia.org/wiki/Worst-case_execution_time) (WCET), den længste tid en opgave kan tage, og skeduler mod det tal, ikke gennemsnittet. For strøm så husk, at mange enheder kører på batteri eller høster energi, så design arbejdscyklusser, dvaletilstande og vækningshændelser til at ramme et energibudget, der skal holde måneder eller år. Skriv disse budgetter ned og gennemgå dem som ethvert andet krav.

### Håndtér afbrydelser og samtidighed med streng disciplin

En [afbrydelse](https://en.wikipedia.org/wiki/Interrupt) (interrupt) er et hardwaresignal, der pauser det nuværende arbejde for at køre en håndterer med det samme. Afbrydelser er, hvordan enheder reagerer øjeblikkeligt på verden, og de er en stor kilde til subtile fejl. Hold håndterere så korte som muligt: kvittér hændelsen, gem minimale data og udskyd det egentlige arbejde til en normal opgave. Fordi en afbrydelse kan udløses mellem to vilkårlige instruktioner, skal du beskytte delte data mod [kapløbstilstande](https://en.wikipedia.org/wiki/Race_condition) med omhu. Brug låsefri teknikker, korte kritiske sektioner eller velforståede primitiver, og værn mod prioritetsinversion, hvor en lavprioritetsopgave, der holder en lås, blokerer en højprioritetsopgave. Denne samtidighed deler ræsonnementet i kapitel 3.3, men med strammere timing og intet rum til et genforsøg.

### Skriv enhedsdrivere, der isolerer hardwaredetaljer

En [enhedsdriver](https://en.wikipedia.org/wiki/Device_driver) er det softwarelag, der taler med et bestemt stykke hardware: en sensor, en radio, en motorcontroller. Hold hardwarespecifik kode bag en ren grænseflade, så resten af din software afhænger af en stabil abstraktion frem for af registeradresser. Det gør koden testbar uden for målenheden, lettere at portere, når en chip udgår, og enklere at ræsonnere om. Dokumentér hver antagelse om timing, byte-rækkefølge og hardwareparticulariteter, fordi det er de detaljer, der forårsager feltfejl. Det er konstruktionsdisciplinen fra kapitel 2.9 anvendt, hvor en forkert bit kan standse en motor.

### Adoptér den funktionelle sikkerhedsstandard, der styrer dit domæne

Hvis din enhed kan skade mennesker eller ejendom, gælder der sandsynligvis en standard for [funktionel sikkerhed](https://en.wikipedia.org/wiki/Functional_safety), og den er ofte loven. IEC 61508 er den generelle standard for sikkerheden i elektroniske systemer og forælder til flere andre. [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) styrer vejkøretøjers sikkerhed. [DO-178C](https://en.wikipedia.org/wiki/DO-178C) styrer luftbåren software i civil luftfart. IEC 62304 styrer software i medicinsk udstyr. Til kodning er [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) et bredt anvendt sæt regler, der begrænser risikable C-sprogfeatures for at gøre kode sikrere og mere analyserbar. Disse standarder kræver sporbarhed fra krav til kode til test, definerede processer og dokumentation, du kan aflevere til en revisor eller en tilsynsmyndighed. Adoptér den rette tidligt, fordi at eftermontere papirsporet senere er smertefuldt og nogle gange umuligt.

### Test med simulering og hardware-in-the-loop

Du kan ikke teste indlejret software, som du tester en webapp. Byg en lagdelt strategi. Kør enhedstests på en normal computer mod hardwareabstraktionsgrænsefladen. Brug simulering til at modellere enheden og dens miljø, når reel hardware er knap eller farlig at belaste. Brug derefter [hardware-in-the-loop](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation) (HIL)-test, hvor den rigtige controller kører mod en simuleret version af det fysiske system, den styrer, så du sikkert kan teste fejltilstande som en fastlåst sensor eller en pludselig belastning. Automatisér disse tests i din pipeline, så hver ændring kontrolleres under realistiske forhold, før den når en enhed.

### Design over-the-air-opdateringer og enhedssikkerhed fra dag ét

Enheder i marken får brug for rettelser, så planlæg for over-the-air (OTA)-opdateringer: en måde at levere ny firmware sikkert over et netværk. Et sikkert OTA-design signerer hver opdatering kryptografisk, verificerer signaturen før installation, opdaterer atomisk og kan rulle tilbage til et kendt godt aftryk, hvis det nye ikke starter. Par dette med sikkerhedsprincipperne i kapitel 4.3, tilpasset begrænset hardware. Brug en hardware root of trust og secure boot, så kun signeret firmware kører. Krypter data under transport og i hvile. Skift standardlegitimationsoplysninger og deaktivér ubrugte grænseflader. En IoT-flåde er et distribueret system med en enorm angrebsflade, og en enkelt svag standardadgangskode kan kompromittere millioner af enheder på én gang.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper / omkostning |
|---|---|---|
| RTOS | Multitasking, prioritetsskedulering, timingtjenester | Overhead, større fodaftryk, indlæringskurve |
| Bare metal | Mindst, mest forudsigelig, fuld kontrol | Svært at skalere til mange opgaver, mere manuelt arbejde |
| Statisk allokering | Forudsigelig, ingen fragmentering, sikkerhedsvenlig | Mindre fleksibel, alt skal dimensioneres på forhånd |
| Formel sikkerhedscertificering | Juridisk markedsadgang, stringent dokumentation, højere tillid | Stor tids- og pengeomkostning, langsommere iteration |
| OTA-opdateringer | Ret og forbedr enheder i marken, forlæng levetid | Opdateringsinfrastruktur, sikkerhedsbyrde, tilbagerulningsrisiko |

Den overordnede afvejning er mellem forudsigelighed og fleksibilitet. Alt, der gør et almindeligt system bekvemt (dynamisk hukommelse, garbage collection i baggrunden, best-effort-skedulering, elastiske ressourcer), virker imod garantien for, at en opgave altid bliver færdig til tiden inden for et fast fodaftryk. Indlejret og realtidsingeniørarbejde opgiver bevidst fleksibilitet for at købe determinisme og sikkerhed. Færdigheden er kun at bruge den handel, hvor deadlinen eller risikoen reelt kræver det, og at holde de fleksible, hurtigere bevægende dele (som en enheds cloud-backend) på den anden side af en ren grænse.

## Spørgsmål til drøftelse med dit team

1. **Måler I jitter, eller kun gennemsnitlig latens, på jeres timingkritiske stier?** Hård realtidskorrekthed hviler på at begrænse variationen i svartid (jitter), ikke blot at sænke den typiske latens, fordi forudsigelighed er det, der lader jer bevise, at en deadline altid overholdes. En kontrolløkke med et lavt gennemsnit, men lejlighedsvise store spidser, kan stadig misse sin deadline og forårsage skade, og gennemsnittet vil skjule det. Tag målinger af spredningen med, worst case inkluderet, for hver timingkritisk opgave, og mærk hver som hård, fast eller blød, så testens stringens matcher konsekvensen af en miss. Alt bekvemt i almindelige systemer (dynamisk hukommelse, garbage collection, best-effort-skedulering) angriber forudsigeligheden, så det bliver uden for den hårde sti. Hvis I kun rapporterer gennemsnit, kan I ikke ærligt påstå, at en hård deadline overholdes.

2. **Er jeres valg af RTOS eller bare metal stadig det rette, og kan I bevise, at opgavesættet kan skeduleres?** Eksekveringsfundamentet er en beslutning at genbesøge, efterhånden som enheden vokser: bare metal er mindst og mest forudsigeligt til ét klart job, mens et RTOS fortjener sin overhead, når I har flere samtidige opgaver med forskellige deadlines. Til hårdt realtidsarbejde peger kapitlet på en præemptiv prioritetsbaseret skeduler analyseret med en metode som rate-monotonic scheduling, som lader jer bevise, at opgaverne passer, frem for at håbe. Tag det nuværende opgavesæt, deres frekvenser og deres værst tænkelige eksekveringstider med, og tjek om skedulerbarheden faktisk holder, eller om opgaver stille er akkumuleret ud over, hvad fundamentet kan garantere. Værn mod prioritetsinversion, hvor en lavprioritetsopgave, der holder en lås, standser en højprioritetsopgave. At vælge fundamentet ved vane frem for ved opgavesættet er, hvordan timinggarantier stille eroderes.

3. **Hvor går præcis grænsen mellem den deterministiske enhed og den fleksible cloud-backend, og er den ren nok til at bevæge sig hurtigt på den ene side uden at bringe den anden i fare?** Kapitlets overordnede afvejning opgiver fleksibilitet for at købe determinisme og sikkerhed, og færdigheden er kun at bruge den handel, hvor deadlinen eller risikoen reelt kræver det. En ren grænse lader den sikkerhedskritiske firmware forblive konservativ og certificeret, mens cloud-backenden itererer hurtigt, så de to udvikler sig i deres eget sikre tempo. Tag jeres arkitektur med og find den søm: hvad skal bevises deterministisk og opdateres gennem en signeret, verificeret sti, versus hvad kan ændre sig ugentligt på serveren. At udviske linjen trækker cloud-vaner (dynamisk allokering, best-effort-timing) ind i kontrolstien eller sinker unødigt backenden til firmwarens kadence. At få grænsen rigtig er det, der holder både sikkerhedsdokumentationen og leveringshastigheden intakt.

4. **Hvilken funktionel sikkerhedsstandard styrer hvert produkt, og hvor langt er den nuværende dokumentation fra det, en revisor ville acceptere?** Standarden (IEC 61508, ISO 26262 for vejkøretøjer, DO-178C for luftbåren software, IEC 62304 for medicinsk udstyr) er ofte loven, og den kræver sporbarhed fra krav til kode til test, som I ikke kan forfalske til sidst. For et stort team er risikoen, at grupper adopterer papirsporet uens, så én produktlinje er revisionsparat, mens en anden midtvejs i certificeringen opdager, at dens krav aldrig blev sporet. Det modstridende træk er hastighed: fuld sporbarhed og håndhævelse af MISRA C sinker den daglige iteration, og et team under deadlinepres fristes til at udskyde dokumentationen til "senere". Tag den nuværende sporbarhedsmatrix med, de statiske analysefund, der stadig er åbne, og en ærlig hulanalyse mod det ønskede sikringsniveau. I virksomheds- og offentlige sammenhænge så tilføj certificeringens ledetid og revisorens forventninger, for at eftermontere dokumentation efter design er langsomt, dyrt og nogle gange umuligt, og en skredet certificering kan blokere markedsadgang helt.

5. **Hvis en alvorlig fejl blev fundet i en enhed i marken i morgen, hvor hurtigt kunne I rette den sikkert på tværs af hele flåden, og har I øvet tilbagerulningen?** En enhed, I ikke kan patche, bliver et permanent sikkerheds- og tryghedsansvar, og en fysisk tilbagekaldelse koster størrelsesordener mere end en signeret over-the-air-opdatering. Spændingen er, at en skødesløs opdateringsmekanisme selv er en angrebsflade og en brickingrisiko: en OTA-sti, der installerer usignerede aftryk, eller som ikke kan rulle en dårlig opstart tilbage, kan forvandle én dårlig udgivelse til millioner af døde enheder. Tag jeres opdateringsdesign med (kryptografisk signering, signaturverifikation før installation, atomisk installation, automatisk tilbagerulning til et kendt godt aftryk), status for secure boot og hardware root of trust og hvornår nogen sidst faktisk øvede en tilbagerulning på reel hardware. For en virksomheds- eller offentlig flåde så tilføj, hvem der er ansvarlig for signeringsnøglerne, og hvordan I ville tilbagekalde en kompromitteret, fordi en lækket nøgle eller en fælles standardlegitimation kan kompromittere hele flåden på én gang.

6. **Er jeres hukommelses-, CPU- og strømbudgetter skrevet ned med hårde lofter, og øver jeres teststrategi både simulering og reel hardware?** Realtidsgarantier hviler på værst tænkelig eksekveringstid og et fast ressourcefodaftryk, ikke gennemsnitlig adfærd, så en ubudgetteret heapallokering eller en utestet worst-case-belastning er, hvor determinisme stille eroderes. For et stort team er faren drift: opgaver akkumuleres, hukommelsen kryber op, og ingen ejer budgettet, til en enhed fejler i marken efter ugers oppetid. Afvejningen er dækning versus omkostning, fordi en hardware-in-the-loop-rig, der injicerer fejl som en fastlåst sensor, er dyr at bygge, mens ren simulering skjuler timingfejl, der kun dukker op på den rigtige chip. Tag de dokumenterede budgetter, de målte værst tænkelige eksekveringstider mod dem og dokumentation for, at jeres pipeline kører enhedstests på abstraktionslaget, simulering og hardware-in-the-loop før en udgivelse. I regulerede og offentlige sammenhænge så bind dette til den strukturelle testdækning, standarden kræver, da en revisor vil have bevis for, at fejltilstande blev udøvet, ikke en forsikring om, at gennemsnitstilfældet så fint ud.

## Sektorperspektiv

**Startup.** Hastighed og overlevelse dominerer, så vælg et let RTOS eller en simpel bare-metal-løkke, forbyd dynamisk allokering efter opstart, og mål den værst tænkelige tid for din ene kritiske løkke frem for at jage et certificeringsbudget, du ikke har. Spring formelle funktionelle sikkerhedsprocesser over, medmindre dit marked tvinger dem, men spring aldrig signerede over-the-air-opdateringer med automatisk tilbagerulning over: et ungt firma overlever ikke en felttilbagekaldelse, og en fjernrettelse er forskellen mellem en dårlig nat og et dødt produkt. Hold enhedens firmware lille og konservativ, så dine knappe ingeniører ikke vedligeholder en pipeline, de ikke har råd til.

**Lille virksomhed.** Uden en indlejret specialist på stat så støt dig til gennemprøvede moduler, referencedesigns og leverandørs RTOS-distributioner frem for at rulle din egen skeduler eller bootloader. Ram køb-versus-byg-valget ind omkring, hvem der vil patche enheden det næste årti: en købt sikkerheds- og opdateringsstak, du kan stole på, slår en skræddersyet, ingen tilbageværende kan vedligeholde. Behandl standardadgangskoder, åbne fejlsøgningsgrænseflader og usignerede opdateringer som de fejl, der med størst sandsynlighed vil skade dig, fordi de er billige at forebygge og ruinerende at opdage i marken.

**Stor virksomhed.** Problemet er ensartethed på tværs af mange produktlinjer og teams: en fælles politik for eksekveringsfundament, fælles skabeloner for ressourcebudgetter, håndhævet MISRA C og statisk analyse og én certificeret over-the-air-opdaterings- og secure-boot-platform, så hver gruppe ikke genopfinder den. Budgettér byrden ved funktionel sikkerhed og hardware-in-the-loop eksplicit, standardisér hardwareabstraktionsgrænsefladen, så en chip, der udgår, ikke efterlader et produkt strandet, og styr flådens timingdokumentation, sikkerhedsartefakter og sikkerhedsholdning som styrede aktiver frem for folklore pr. team. En enkelt svag standardlegitimation på tværs af flåden er en forpligtelse i virksomhedsskala, så centralisér legitimations- og nøglestyring.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former hvert valg. Kræv at leverandører udvikler luftbåren, medicinsk eller forsvarssoftware efter den gældende standard (DO-178C, IEC 62304, IEC 61508) på det sikringsniveau, der matcher faren, og afleverer sporbarheds- og strukturelle dækningsdokumentation, revisorer vil gennemgå. Kræv secure boot, en hardware root of trust og en kontrolleret, signeret feltopdateringsproces, fordi en ikke-verificeret opdatering til et flyvnings- eller netsystem er uacceptabel. Foretræk kontrakter, der giver rettigheder til kildekode, sikkerhedsartefakter og muligheden for at gencertificere med en anden leverandør, så en leverandør, der går konkurs, ikke efterlader et system, offentligheden afhænger af i årtier.

## Eksempler

**Startup.** Et lille hardwarestartup, der bygger en batteridrevet luftkvalitetsmonitor, skriver sin firmware mod et let RTOS med et fast sæt opgaver og ingen dynamisk allokering efter opstart, så den enhed, der leveres, er den enhed, der kører i årevis på et knapcellebatteri. Selv uden et certificeringsbudget måler teamet den værst tænkelige tid af sin sensoraflæsningsløkke og tester enheden mod injicerede fejltilstande på en bænkrig før hver udgivelse. Signerede over-the-air-opdateringer med automatisk tilbagerulning lader dem rette en fejl på tværs af hver leveret enhed, så en dårlig aflæsning i marken ikke betyder en tilbagekaldelse, det unge firma ikke kunne overleve.

**Stor virksomhed.** En producent af forbundne køretøjer bygger en elektronisk bremsecontroller. Den hårde realtidskontrolløkke kører på et RTOS med rate-monotonic scheduling og statisk hukommelse, og hver opgave bærer en målt værst tænkelig eksekveringstid. Teamet udvikler efter ISO 26262 med fuld sporbarhed fra krav til kode til test og håndhæver MISRA C med statisk analyse på hver commit. En hardware-in-the-loop-rig afspiller tusindvis af vejscenarier, herunder injicerede sensorfejl, før nogen firmware leveres. Signerede OTA-opdateringer lader firmaet rette en fejl på tværs af hele flåden uden en dyr tilbagekaldelse, med automatisk tilbagerulning, hvis en bil ikke starter det nye aftryk.

**Offentlig sektor.** En national luftfartsmyndighed certificerer en ny flyvestyringscomputer. Leverandøren udvikler den luftbårne software efter DO-178C på det sikringsniveau, der matcher faren, og producerer dokumentation for kravdækning og strukturel testdækning, revisorer gennemgår. Timing bevises deterministisk under worst-case-belastning, med afgrænset afbrydelseslatens og ingen dynamisk allokering efter opstart. Secure boot og en hardware root of trust sikrer, at kun signeret, certificeret firmware kører. Feltopdateringer følger en kontrolleret, signeret proces, fordi en ikke-verificeret opdatering til et flyvningssystem er uacceptabel.

## Business case: motivation, ROI og TCO

Business casen domineres af omkostningen ved fejl og omkostningen ved adgang til et marked. I regulerede domæner kan du slet ikke sælge produktet uden sikkerhedscertificeringen, så procesomkostningen er simpelthen indgangsprisen. Ud over det er fejl i hardware i marken ekstraordinært dyre: en fysisk tilbagekaldelse koster langt mere end en cloud-hotfix, og en sikkerhedshændelse bærer ansvar, regulatoriske bøder og omdømmeskade, der kan afslutte en produktlinje. At bygge sikkerhed, determinisme og opdaterbarhed ind fra begyndelsen er billigt i forhold til at opdage deres fravær i marken.

Ram afkastet ind omkring undgåede tilbagekaldelser, hurtigere certificering og længere enhedslevetid. En robust OTA-evne omsætter mange potentielle tilbagekaldelser til billige fjernrettelser, og hver undgået tilbagekaldelse kan betale hele opdateringsprogrammet. Stringent WCET-analyse og ressourcebudgettering lader dig levere på billigere hardware med tillid, hvilket sænker omkostningen pr. enhed på tværs af en stor flåde. For totale ejeromkostninger så husk, at disse enheder lever i år eller årtier: vedligeholdelses-, sikkerhedspatch- og supportbyrden (kapitel 3.7) dværger det indledende byg. At designe til opdaterbarhed, klar hardwareabstraktion og dokumenterede budgetter er det, der holder den lange hale overkommelig.

## Anti-mønstre og faldgruber

- **Optimering for gennemsnitstilfældet.** At overholde deadlinen "som regel" er at fejle et hårdt realtidskrav.
- **Dynamisk allokering i kontrolstien.** Heapfragmentering forårsager en fejl, der først dukker op efter ugers oppetid.
- **Fede afbrydelseshåndterere.** At lægge tung behandling inde i en afbrydelse sprænger dit timingbudget og skaber kapløbstilstande.
- **At ignorere standarden til revisionen.** At eftermontere sporbarhed og dokumentation sent er langsomt, dyrt og nogle gange umuligt.
- **At levere uden en opdateringssti.** En enhed, du ikke kan patche, bliver et permanent sikkerheds- og tryghedsansvar.
- **Standardadgangskoder og åbne grænseflader.** Én svag legitimation forvandler en IoT-flåde til et botnet.
- **Kun at teste på en simulator eller kun på hardware.** Hver skjuler fejl, den anden ville fange; I har brug for begge.
- **At behandle hardwaren som en andens problem.** Timing, byte-rækkefølge og sensorparticulariteter er softwareanliggender her.

## Modenhedsmodel

- **Niveau 1: Opstart.** Timing håbes på, ikke analyseres. Hukommelse allokeres dynamisk efter forgodtbefindende. Ingen funktionel sikkerhedsstandard følges. Test er manuel og kun på enheden. Enheder kan ikke opdateres, når de er leveret, så en feltfejl betyder en tilbagekaldelse eller et permanent ansvar.
- **Niveau 2: Udvikling.** Nogle opgaver har målt timing, og et grundlæggende RTOS eller en struktureret løkke er på plads, men praksis varierer fra team til team. Kodningsretningslinjer findes, men håndhæves ikke. Test omfatter noget simulering. En manuel, risikabel opdateringssti findes på nogle produkter og ikke andre. Gode vaner er til stede, men inkonsistente, og intet garanterer, at den næste produktlinje arver dem.
- **Niveau 3: Standardisering.** Timingkrav klassificeres som hårde, faste eller bløde og analyseres med værst tænkelig eksekveringstid og en skedulerbarhedsmetode, dokumenteret og håndhævet i hele organisationen. Ressourcebudgetter for hukommelse, CPU og strøm er skrevet ned med hårde lofter. Den gældende funktionelle sikkerhedsstandard følges med sporbarhed fra krav til kode til test, og MISRA C eller et tilsvarende håndhæves af statisk analyse på hver commit. Hardware-in-the-loop-test kører i pipelinen. Signerede, atomiske over-the-air-opdateringer med tilbagerulning og secure boot er det krævede grundniveau overalt.
- **Niveau 4: Styring.** Organisationen måler og styrer sit indlejrede landskab mod baselines. Den følger marginer på værst tænkelig eksekveringstid, jitterfordelinger, deadline-miss-rater, hukommelses- og strømmargen, åbne fund fra statisk analyse, dækning af certificeringsdokumentation og succes- og tilbagerulningsrater for over-the-air-opdateringer og sammenligner dem med aftalte mål. Drift mod et ressource- eller timingbudget udløser handling, før en enhed fejler i marken, og go/no-go-beslutninger om udgivelse hviler på disse data frem for på dømmekraft i øjeblikket. Ledere kan se, hvilke produktlinjer der er revisionsparate, og hvilke der trender mod en misset deadline eller et sprængt budget.
- **Niveau 5: Orkestrering.** Determinisme, sikkerhedsdokumentation og tryghed verificeres og automatiseres løbende. Fejlinjektion og hardware-in-the-loop kører på hver ændring, og certificeringsartefakter genereres som et biprodukt af processen. Flåden overvåges, patches og opdateres sikkert i stor skala gennem en lang levetid. Organisationen tilpasser sine eksekveringsfundamenter, ressourcebudgetter og standardadoption, efterhånden som chips udgår, trusler udvikler sig, og reguleringer ændrer sig, og genbalancerer hele porteføljen af enheder på dokumentation frem for at reagere på hver krise alene.

## Idéer til drøftelse

1. Hvilke af jeres enheds opgaver er reelt hårde realtid, og kan I bevise, at hver altid overholder sin deadline?
2. Kender I den værst tænkelige eksekveringstid for jeres kritiske kontrolløkke, eller kun dens gennemsnit?
3. Hvilken funktionel sikkerhedsstandard styrer jeres produkt, og hvor langt er jeres nuværende dokumentation fra det, den kræver?
4. Hvis en alvorlig fejl blev fundet i en enhed i marken i morgen, hvordan ville I rette den, og hvor hurtigt?
5. Hvor findes dynamisk hukommelsesallokering stadig i jeres kontrolsti, og hvad sker der, hvis den fejler ved time 1000?
6. Hvordan ville jeres IoT-flåde modstå en angriber, der fandt én fælles standardlegitimation?

## Vigtigste pointer

- Indlejret software kører på begrænset hardware, og realtidskorrekthed afhænger af timing, ikke blot af det rigtige svar.
- Klassificér hver deadline som hård, fast eller blød, og design til worst-case-timing, afgrænset jitter og determinisme frem for rå hastighed.
- Vælg RTOS eller bare metal bevidst, og budgettér hukommelse, CPU og strøm som faste, førsteklasses ressourcer.
- Hold afbrydelseshåndterere bittesmå, værn delte data, og isolér hardware bag rene, testbare driver-grænseflader.
- Adoptér den funktionelle sikkerhedsstandard, dit domæne kræver, tidligt (IEC 61508, ISO 26262, DO-178C, IEC 62304, MISRA C), med fuld sporbarhed.
- Test med simulering og hardware-in-the-loop, og byg sikre, signerede, tilbagerulningsdygtige OTA-opdateringer og enhedssikkerhed fra dag ét.

## Referencer og videre læsning

- IEC 61508, *Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*
- ISO 26262, *Road Vehicles: Functional Safety*
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*
- IEC 62304, *Medical Device Software: Software Life Cycle Processes*
- MISRA, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Michael Barr and Anthony Massa, *Programming Embedded Systems*
- Elecia White, *Making Embedded Systems*
- Jane W. S. Liu, *Real-Time Systems*
- Giorgio Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*
- Colin Walls, *Embedded Software: The Works*
- Philip Koopman, *Better Embedded System Software*
- OWASP Internet of Things (IoT) security guidance
