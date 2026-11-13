# 7.2 Datateknik

## Overblik og motivation

[Datateknik](https://en.wikipedia.org/wiki/Data_engineering) er disciplinen at bygge og drive de pipelines og platforme, der flytter data fra det sted, de produceres, til det sted, de skaber værdi. Den dækker indtag fra kildesystemer, transformation til rene og modellerede former, lagring i omkostningseffektive formater, orkestrering af hele flowet og de pålidelighedspraksisser, der holder alt troværdigt. Hvis datastrategi afgør, hvilke data der bør findes, og hvem der ejer dem, er datateknik rørføringen og maskineriet, der får dem til at flyde.

For store teams er denne disciplin grundlæggende. Analyse, [business intelligence](https://en.wikipedia.org/wiki/Business_intelligence), produkteksperimenter, [maskinlæring](https://en.wikipedia.org/wiki/Machine_learning) og regulatorisk rapportering sidder alle nedstrøms for datapipelines. Når disse pipelines er skrøbelige, langsomme eller uigennemsigtige, lider enhver afhængig funktion. Dashboards viser forældede tal. Modeller trænes på korrupte features. Revisorer kan ikke rekonstruere, hvordan et tal blev produceret. I virksomheds- og offentlig skala behandler pipelines milliarder af poster på tværs af mange kildesystemer, og en enkelt stille fejl kan skubbe forkerte data ind i beslutninger, betalinger eller offentlig statistik.

Feltet er vokset op fra skræddersyede scripts og monolitiske [ETL (extract, transform, load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)-værktøjer til den moderne datastak: modulære, stort set SQL-drevne komponenter til indtag, transformation, orkestrering og lagring, forbundet af åbne formater. Denne modularitet er både en gave og en fælde. Den lader jer samle best-of-breed-værktøjer, men uden ingeniørdisciplin producerer den en vildtvækst af udokumenterede, utestede job. Dette kapitel dækker de praksisser, der holder pipelines idempotente, testbare, observerbare og overkommelige i skala.

## Grundprincipper

- Pipelines er software og fortjener versionsstyring, test, gennemgang og CI/CD.
- Foretræk idempotente, reproducerbare transformationer, der sikkert kan køre igen.
- Gør dataflow observerbare: friskhed, volumen, skema og kvalitet overvåges.
- Modellér data bevidst til deres forbrugere frem for at dumpe rå tabeller.
- Vælg batch eller streaming ud fra reelle latensbehov, ikke nyhed.
- Optimér lagerformat, partitionering og beregningsomkostning som førsteklasses anliggender.
- Adskil indtag, transformation og servering, så hver kan udvikle sig uafhængigt.
- Fejl højlydt og tidligt; en ødelagt pipeline er sikrere end stille forkerte data.

## Anbefalinger

### Vælg ETL eller ELT bevidst

ETL transformerer data, før de indlæses i destinationen. [ELT (extract, load, transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) indlæser rå data først og transformerer dem inde i et kraftfuldt varehus eller lakehouse. Moderne cloudplatforme har gjort ELT til standarden, fordi lager er billigt og beregning er elastisk, og fordi det at beholde rå data lader jer genbehandle, når logik ændres, eller fejl dukker op. Foretræk ELT til analysearbejdsbyrder: land rå, uforanderlige data, og byg så lagdelte transformationer oven på. Gem transformation før indlæsning til tilfælde, hvor privatliv, omkostning eller kontraktlige begrænsninger kræver rensning eller filtrering, før dataene lander.

### Design batch- og streamingpipelines efter deres latensbehov

De fleste analysebehov betjenes godt af planlagte batchpipelines, som er enklere at ræsonnere om, teste og efterfylde. Ræk kun ud efter streaming, når forretningen reelt har brug for data med lav latens: svindeldetektion, operationel alarmering, realtidspersonalisering. Streaming tilføjer reel kompleksitet omkring rækkefølge, præcis-én-gang-semantik, sent ankommende data og tilstandshåndtering. Hvor I har brug for begge, så overvej arkitekturer, der samler batch- og streaminglogik frem for at vedligeholde to divergerende kodebaser. Vær ærlige om jeres latenskrav. "Realtid" er ofte et uprøvet ønske, der fordobler jeres omkostning.

### Orkestrér med eksplicitte afhængigheder

Brug en orkestrator til at udtrykke pipelines som [rettede acykliske grafer (DAG'er)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) af opgaver med eksplicitte afhængigheder, genforsøg og planlægning. Det giver jer overblik over, hvad der kørte, hvad der fejlede, og hvad der er blokeret, plus evnen til at efterfylde og genkøre deterministisk. Baser afhængigheder på datatilgængelighed, ikke blot klokkeslæt, så nedstrøms job venter på opstrøms data i stedet for at udløses på et gæt. Hold orkestreringslogik i versionsstyring, og behandl DAG-ændringer som kodeændringer.

### Modellér data til forbrug

Rå tabeller er sjældent egnede til analytikere. Anvend [dimensionel modellering](https://en.wikipedia.org/wiki/Dimensional_modeling), der arrangerer fakta og konforme dimensioner i [stjerneskemaer](https://en.wikipedia.org/wiki/Star_schema), hvor I har brug for styret, genbrugelig, selvbetjent analyse. Brede denormaliserede tabeller ("én stor tabel") kan yde bedre til specifikke forespørgselsmønstre og er enklere for nogle forbrugere, til prisen af duplikering og fleksibilitet. Læg jeres transformationer i lag: et råt staginglag, et renset og konformt kernelag og forbrugervendte marts. Den adskillelse lader jer rette logik ét sted, og den lader forbrugere afhænge af stabile grænseflader.

### Gør pipelines idempotente og testbare

Design transformationer, så de ved genkørsel producerer det samme resultat frem for at duplikere eller korrumpere data, for eksempel ved at bruge deterministiske upserts nøglet på forretningsidentifikatorer og partitionsoverskrivningsmønstre. Skriv tests på flere niveauer: unit tests for transformationslogik, skematests og datatests, der hævder forventninger som unikhed, ikke-nul-nøgler, referentiel integritet og accepterede værdiintervaller. Kør dem i CI, så en dårlig ændring fanges, før den når produktionsdata.

### Instrumentér observerbarhed og pålidelighed

Overvåg de fire kernesignaler for datasundhed: friskhed (er det opdateret), volumen (er rækkeantallet i det forventede interval), skema (er strukturen ændret uventet) og fordeling (er værdier drevet anomalt). Alarmér ved brud, og dirigér dem til det ejende team. Hold runbooks, vagtrotationer og skyldfrie postmortems for datahændelser, ligesom I ville for tjenester. Spor afstamning, så I, når noget går i stykker, straks kan se den nedstrøms påvirkning.

### Optimér lager og omkostning

Brug kolonneorienterede åbne formater som Parquet eller åbne tabelformater, der understøtter skemaudvikling, tidsrejser og effektive opdateringer. Partitionér data efter de kolonner, I filtrerer mest på, typisk dato, og undgå en vildtvækst af små filer ved at komprimere. Adskil varme og kolde data med lagdelt lager og livscyklusrækværk. Overvåg beregningsudgift pr. pipeline og pr. forespørgsel. Løbske omkostninger kommer som regel af fulde scanninger, manglende partitioner og ubegrænset genbehandling. Behandl omkostning som en måling med ejere, ikke en overraskelse på den månedlige regning.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper | Bedst egnet |
|---|---|---|---|
| ELT (transformér på stedet) | Beholder rå data, billigt lager, kan genbehandles | Stort lagerfodaftryk, styring nødvendig | Cloudanalyse |
| ETL (transformér før indlæsning) | Kontrollerer omkostning, filtrerer følsomme data tidligt | Mister rå data, sværere at genbehandle | Regulerede eller begrænsede indlæsninger |
| Batch | Simpel, testbar, let efterfyldning | Højere latens | Det meste analyse |
| Streaming | Lav latens, realtidsreaktion | Kompleks, dyr, svær at teste | Svindel, driftsalarmering |
| Stjerneskema | Styret, genbrugeligt, selvbetjeningsvenligt | Modelleringsindsats på forhånd | Delt BI |
| Bred tabel | Hurtig til kendte forespørgsler, simpel | Duplikering, mindre fleksibel | Snævert højtydende brug |

Den dominerende afvejning er enkelhed versus latens og fleksibilitet. Batch og ELT med lagdelte stjerneskemaer giver jer et testbart, efterfyldeligt, velforstået system, der betjener de fleste behov overkommeligt. Streaming, realtid og stærkt denormaliserede designs køber hastighed og specifik ydeevne, men til en stejl pris i driftskompleksitet og testvanskelighed. Adoptér kompleksitet kun, hvor et konkret forretningskrav betaler for den, og hold den simple sti som jeres standard.

## Spørgsmål til drøftelse med dit team

1. **Har I bevidst valgt ELT frem for ETL, og beholder I rå, uforanderlige data, så I kan genbehandle, når logik ændres, eller fejl dukker op?** Kapitlets standard er ELT: land rå data billigt, og byg så lagdelte transformationer, fordi det at beholde rå data lader jer genkøre alt, når en regel ændres, eller en fejl dukker op uger senere. At slette rå data afskærer den mulighed og er en almindelig, smertefuld faldgrube. Argumentet for ETL er reelt i regulerede eller begrænsede indlæsninger, hvor privatliv, omkostning eller kontraktvilkår kræver filtrering eller maskering, før data lander. Tag dokumentation med: hvor ofte har I haft brug for at genbehandle historik, og hvad kostede det, da I ikke kunne? For en offentlig eller virksomhedspipeline, der skal kunne spore ethvert tal til kilden, er uforanderlige rå poster også et reviderbarhedskrav, så svaret former både jeres lagerpolitik og jeres juridiske forsvarlighed.

2. **Hvilke af de fire datasundhedssignaler overvåger I faktisk, og hvem bliver pagede, når et går i stykker?** Kapitlet navngiver fire signaler, der er værd at holde øje med: friskhed, volumen, skema og fordeling. Mange teams overvåger ingen af dem og lærer om fejl af en direktør, der stirrer på et forældet dashboard, hvilket er den værst mulige detektor. I virksomheds- og offentlig skala kan en enkelt stille fejl skubbe forkerte data ind i betalinger, rapporter eller offentlig statistik, så omkostningen ved sen detektion måles i tillid og penge, ikke kun omarbejde. Tag jeres reelle gennemsnitlige tid til at opdage og navnet på den, der i øjeblikket finder hændelser først, med. Hvis svaret er "en forbruger", har I brug for alarmering dirigeret til det ejende team plus runbooks og skyldfrie postmortems, der behandler datahændelser præcis som tjenestenedbrud.

3. **Forbruger jeres analytikere modellerede, testede marts, eller dumper I rå tabeller på dem og kalder det selvbetjening?** Kapitlet er direkte: rå tabeller er sjældent egnede til analytikere, og at lægge transformationer i lag i et råt staginglag, et konformt kernelag og forbrugervendte marts lader jer rette logik én gang og give forbrugere stabile grænseflader. Det modstridende træk er hastighed, da modellering med stjerneskemaer eller bevidste brede tabeller koster indsats på forhånd, og det er fristende at springe over. Men at dumpe rå data skubber modelleringsomkostningen over på hver analytiker gentagne gange og producerer divergerende tal og spildte timer. Tag et signal med: hvilken andel af analytikertid går med at omforme rå data, og hvor mange teams har genopbygget de samme joins. Hvis tallet er højt, så invester i et konformt kernelag, så forbrugere afhænger af testede, genbrugelige grænseflader i stedet for at genopfinde dem.

4. **Hvor tjener "realtid" reelt sin omkostning, og hvor er det et uprøvet ønske, der stille fordobler jeres driftsbyrde?** Kapitlets standard er planlagt batch, som er enklere at ræsonnere om, teste og efterfylde, med streaming forbeholdt tilfælde, hvor forretningen reelt har brug for lav latens, såsom svindeldetektion eller operationel alarmering. Det modstridende træk er prestige og vage interessentønsker om "live" data, som lyder billige i et planlægningsmøde og bliver dyre i produktion, fordi streaming trækker rækkefølge, præcis-én-gang-semantik, sent ankommende data og tilstandshåndtering med sig, plus en anden kodebase at holde i trit med batchlogikken. Tag dokumentation med til drøftelsen: for hver streamingpipeline, I kører eller foreslår, navngiv den beslutning, den fodrer, og den latens, den beslutning faktisk tolererer, målt i minutter eller timer frem for tillægsord. For en stor virksomheds- eller offentlig platform så tilføj vagt- og testomkostningen for hver realtidssti, for en streamingpipeline, ingen kan teste eller bemande døgnet rundt, er et pålidelighedsansvar klædt ud som en funktion, og det ærlige svar kollapser ofte et "realtid"-krav tilbage til en times-batch, der betjener den samme beslutning.

5. **Hvilke af jeres pipelines kunne ikke sikkert køres igen i dag, og hvad ville der skulle til for at gøre hver transformation idempotent?** Kapitlet insisterer på idempotente, reproducerbare transformationer, med deterministiske upserts nøglet på forretningsidentifikatorer og partitionsoverskrivningsmønstre, så en genkørsel producerer det samme resultat frem for at duplikere eller korrumpere data. Det modstridende pres er leveringshastighed, da et naivt kun-tilføj-job leveres hurtigere end et designet til at kunne køres igen, og omkostningen ved den genvej forbliver skjult, til en fejl tvinger en delvis genkørsel kl. 2 om natten, og nogen dobbelttæller omsætning. Tag en konkret opgørelse med: list de job, der ville korrumpere data, hvis de blev kørt igen fra et fejlpunkt, og estimér sprængradius af det værste. I virksomheds- og offentlig skala, hvor en enkelt stille fejl kan skubbe forkerte data ind i betalinger, rapporter eller offentlig statistik, er ikke-idempotent behandling ikke blot ubekvem, den underminerer den reviderbarhed, der lader jer genbehandle en periode efter en regelændring og stadig spore hvert tal til kilden, så at finansiere omarbejdet for at gøre genkørsler sikre er et kontrolspørgsmål, ikke blot et ryddelighedsspørgsmål.

6. **Ved I, hvad hver pipeline koster at køre, hvem der ejer det tal, og hvor stor en del af jeres cloudregning der kommer af fulde scanninger og manglende partitioner?** Kapitlet behandler lagerformat, partitionering og beregningsudgift som førsteklasses anliggender med ejere og advarer om, at løbske omkostninger som regel kan spores til fulde scanninger, manglende partitioner og ubegrænset genbehandling. Det modstridende hensyn er, at omkostningsarbejde føles mindre presserende end at levere funktioner, så det udskydes, til den månedlige regning bliver en overraskelse, og økonomien begynder at stille spørgsmål, ingeniørkunsten ikke kan besvare. Tag dokumentation med: udgift pr. pipeline og pr. forespørgsel, andelen af omkostning fra ikke-partitionerede scanninger og antallet af små filer, der bør komprimeres. For en stor organisation, der kører milliarder af poster på tværs af mange kildesystemer, vokser en uejet cloudregning, uden at noget enkelt team føler sig ansvarligt, og i offentlige sammenhænge skal offentlige udgifter begrundes linje for linje, så at tilskrive beregningsomkostning til en navngiven ejer med en sporet måling forvandler en uigennemsigtig udgift til en styret og afslører ofte besparelser store nok til at finansiere den næste platformsinvestering.

## Sektorperspektiv

**Startup.** Hastighed slår arkitektur. Kobl indtag til en administreret connector, byg en håndfuld versionsstyrede transformationer, og kør dem på en let orkestrator, der selv genforsøger og efterfylder, frem for at håndrulle cron-job, der stille går i stykker natten over. Hold hver model idempotent fra den første commit, og tilføj nogle få billige tests for nul-nøgler og rækkeantal, så en dårlig kildeændring fejler i CI i stedet for at dukke op på grundlæggerens mandagsdashboard. Opstil ikke streaming eller en skræddersyet platform: jeres knappeste ressource er ingeniøropmærksomhed.

**Lille virksomhed.** Uden en dedikeret dataingeniør så foretræk at købe en integreret stak frem for at samle en. En administreret ELT-tjeneste plus et cloudvarehus giver jer connectors, planlægning og lager uden et platformsteam til at vedligeholde dem. Ram valget ind som datahygiejne frem for et pipelineprojekt: vid hvilke kildesystemer der fodrer jeres rapporter, behold rå data, så et forkert tal kan spores og genbehandles, og vælg værktøjer, hvis omkostninger er forudsigelige, så en fuld tabelscanning ikke sprænger det månedlige budget.

**Stor virksomhed.** Problemet er ensartethed på tværs af mange teams og milliarder af poster fra mange kildesystemer. Standardisér ELT-mønstret, den lagdelte staging-kerne-mart-model og de fire datasundhedssignaler, så grupper holder op med at genopfinde skrøbelige pipelines. Håndhæv datatests og CI på hver model, tilskriv beregningsomkostning til ejende teams, og kør datahændelser gennem den samme vagt-, runbook- og skyldfri-postmortem-disciplin, I bruger til tjenester, så en stille fejl aldrig når et dashboard uopdaget.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former pipelinen. Land uforanderlige rå poster for reviderbarhed, transformér dem i lagdelte, testede trin, og hold fuld afstamning, så en revisor kan spore ethvert offentliggjort tal tilbage til dets kildedokumenter, ofte et juridisk krav. Idempotent behandling lader jer sikkert genbehandle en indberetning eller rapporteringsperiode, når en regel ændres, og at favorisere åbne formater og portabel transformationskode holder jer fra at blive låst til en enkelt leverandør gennem en flerårig kontrakt.

## Eksempler

**Startup.** Et analysestartup på ti personer havde dyrket et virvar af cron-job, der stille gik i stykker natten over og nogle gange dobbelttællede rækker, når en ingeniør kørte et i hånden igen. Teamet flyttede til en administreret connector til indtag, et transformationsframework til versionsstyrede modeller og en let orkestrator, der selv genforsøger og efterfylder. De gjorde hver model idempotent og tilføjede en håndfuld tests for nul-nøgler og rækkeantal, så en dårlig kildeændring nu fejler i CI i stedet for at dukke op på grundlæggerens mandagsdashboard.

**Stor virksomhed.** En global detailhandler erstattede hundredvis af håndskrevne udtrækscripts med en ELT-stak. Administrerede connectors lander rå kildedata, et transformationsframework bygger testede, versionsstyrede modeller i et lakehouse, og en orkestrator styrer afhængigheder med genforsøg og efterfyldninger. Datatests fanger skemadrift fra kildesystemer, før den når dashboards. Partitioneret kolonneorienteret lager skar forespørgselsomkostninger væsentligt, mens friskheden forbedredes fra daglig til hver time.

**Offentlig sektor.** En skattemyndighed indtager indberetninger og tredjepartsdata gennem en styret pipeline, der lander uforanderlige rå poster for reviderbarhed og så transformerer dem i lagdelte, testede trin. Idempotent behandling lader dem sikkert genbehandle en indberetningsperiode, når en regel ændres. Fuld afstamning lader revisorer spore ethvert beregnet tal tilbage til kildedokumenter, et juridisk krav for offentlig ansvarlighed.

## Business case: motivation, ROI og TCO

ROI af disciplineret datateknik kommer fra pålidelighed, hastighed og omkostningskontrol. Pålidelige pipelines betyder, at beslutninger og rapporter hviler på troværdige data, så I undgår det dyre omarbejde og den omdømmeskade, forkerte tal medfører. Modulære, testede pipelines lader teams levere nye dataprodukter hurtigere og akkumulerer værdien af hver nedstrøms analyse- og ML-investering. At optimere lager og beregning reducerer direkte cloudregningen, ofte med store marginer, når partitionering og forespørgselsmønstre er rettet.

Adoptionsomkostningen omfatter platformsværktøj, ingeniørtid til at bygge testede modulære pipelines og disciplinen at behandle data som software. Vej dette mod omkostningen ved ikke at adoptere: skrøbelige skræddersyede job, kun deres forfatter forstår, stille datakorruption opdaget af ledere, svulmende cloududgifter fra fulde tabelscanninger og analytikere blokeret i ventetid på data. Over for ledelsen så ram datateknik ind som fundamentet, der gør analyse, BI og AI troværdige og overkommelige. Underinvester I her, kapper I afkastet af hvert datainitiativ ovenpå.

## Anti-mønstre og faldgruber

- Pipelines bygget som engangsscripts uden versionsstyring, tests eller gennemgang.
- Ikke-idempotente job, der duplikerer eller korrumperer data, når de køres igen efter fejl.
- At adoptere streaming af prestigehensyn, når batch ville opfylde latenskravet.
- At dumpe rå tabeller på analytikere og kalde det selvbetjening.
- Ingen observerbarhed, så fejl opdages af nedstrøms forbrugere.
- At ignorere partitionering og filstørrelse, til cloudregningen eksploderer.
- At koble indtag, transformation og servering, så intet kan ændres sikkert.
- At slette rå data og gøre det umuligt at genbehandle, når logik ændres.

## Modenhedsmodel

1. Opstart: Ad hoc-scripts og manuelle kørsler uden tests eller overvågning. Fejl opdages af nedstrøms forbrugere, job kan ikke sikkert køres igen, og cloudomkostninger er ustyrede og utilskrevne.
2. Udvikling: Nogle teams har adopteret en orkestrator og lagt grundlæggende transformationer i versionsstyring, men praksis er inkonsistent på tværs af organisationen. Lejlighedsvise tests findes, idempotens er pletvis, og ødelagte pipelines betyder stadig reaktiv brandslukning.
3. Standardisering: ELT med en lagdelt staging-kerne-mart-model, testet og versionsstyret, er den dokumenterede standard anvendt på tværs af teams. Orkestrerede afhængigheder med genforsøg og efterfyldninger, datatests der kører i CI, og fælles konventioner for stjerneskemamodellering og partitionering er håndhævet i hele organisationen frem for overladt til hver gruppe.
4. Styring: Platformen måles og styres. Friskhed, volumen, skema og fordeling overvåges med alarmer dirigeret til ejende teams, og pipeline-SLA'er, gennemsnitlig tid til at opdage, datakvalitetsbeståelsesrater og beregningsomkostning pr. pipeline og pr. forespørgsel følges mod baselines. Tilbagerulnings- og dræbetærskler håndhæves på dokumentation, og omkostning og pålidelighed har navngivne ejere holdt til mål.
5. Orkestrering: Pipelines behandles fuldt ud som software med CI/CD, datakontrakter og automatiseret anomalidetektion, der fanger drift, før forbrugere gør. Batch- og streaminglogik er samlet, hvor latens reelt betaler sig, platformen forbedres løbende og er selvbetjent, og kapacitet, lagerniveauer og omkostning genbalanceres adaptivt, efterhånden som arbejdsbyrder skifter, så nye dataprodukter leveres hurtigt på et stabilt fundament.

## Idéer til drøftelse

- Hvor i jeres stak tjener "realtid" sin omkostning, og hvor er det ønsketænkning?
- Hvilke pipelines kunne ikke sikkert køres igen i dag, og hvad ville der skulle til for at rette det?
- Hvor stor en del af jeres datacloudregning kommer af fulde scanninger og manglende partitioner?
- Forbruger jeres analytikere modellerede marts eller rå tabeller, og hvad koster det dem?
- Hvad er jeres gennemsnitlige tid til at opdage en datahændelse, og hvem finder den først?
- Ville det at samle batch- og streaminglogik reducere jeres vedligeholdelsesbyrde eller tilføje risiko?

## Vigtigste pointer

- Behandl pipelines som software: versionsstyring, tests, gennemgang, CI/CD og observerbarhed.
- Foretræk ELT med lagdelte, testede modeller; behold rå data til genbehandling.
- Vælg batch som standard og streaming kun, hvor latens reelt betaler sig.
- Gør transformationer idempotente, så genkørsler er sikre.
- Modellér data til forbrugere med stjerneskemaer eller bevidste brede tabeller.
- Overvåg friskhed, volumen, skema og fordeling, og behandl datahændelser som nedbrud.
- Optimér lagerformater, partitionering og beregningsomkostning som førsteklasses anliggender.

## Referencer og videre læsning

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
