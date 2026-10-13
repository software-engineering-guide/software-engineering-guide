# 7.6 Realtids- og streamingdata

## Overblik og motivation

Det meste af det, I ved om datapipelines, forudsætter, at dataene holder stille. I indsamler en dags poster, kører et job natten over og læser resultaterne om morgenen. Realtids- og streamingdata vender den antagelse på hovedet. I stedet for at behandle en færdig bunke data behandler I en endeløs strøm af hændelser, efterhånden som de ankommer, og I producerer svar løbende. Det er forskellen mellem [batchbehandling](https://en.wikipedia.org/wiki/Batch_processing), som arbejder på et afgrænset, komplet datasæt, og [strømbehandling](https://en.wikipedia.org/wiki/Stream_processing), som arbejder på en uafgrænset, aldrig færdig strøm.

For store teams dukker streaming op i det øjeblik, latens begynder at have betydning for forretningen. En svindelbeslutning, der ankommer en time for sent, er værdiløs. Et personaliseringssignal, der lander i morgen, personaliserer intet. Et operationelt dashboard, der halter et skift bagefter virkeligheden, vildleder de mennesker, der ser på det. Kapitel 7.2 (datateknik) argumenterer for, at I som standard skal vælge batch og kun række ud efter streaming, hvor latens reelt betaler sig, og dette kapitel tager jer resten af vejen: hvornår realtid tjener sin omkostning, og hvordan I bygger det uden at sætte ild til jeres driftsbudget. Streaming ligger tæt på de hændelsesdrevne beskedmønstre i kapitel 3.12 (hændelsesdrevet arkitektur og beskedhåndtering), lagringsvalgene i kapitel 3.4 (dataarkitektur og lagring) og telemetripraksisserne i kapitel 9.2 (observerbarhed og telemetri).

Virksomheds- og offentlige sammenhænge hæver indsatsen. En bank scorer transaktioner for svindel i den tid, det tager en kortlæser at blinke. En transportmyndighed følger køretøjer og forudsiger ankomster for millioner af passagerer. En ydelsesmyndighed holder øje med anomalier i krav, mens den fører en revisionsbar optegnelse over hver beslutning. I dem alle kommer værdien af at handle på data, mens de stadig er friske, og risikoen kommer af at handle på data, der er forkerte, ufuldstændige eller umulige at rekonstruere senere. Dette kapitel har holdninger til begge dele.

## Grundprincipper

- Ræk kun efter streaming, når latens har en klar forretningsværdi; batch er billigere og enklere.
- Skeln mellem afgrænsede (endelige) og uafgrænsede (endeløse) data, og design derefter.
- Behandl hændelsestid, ikke ankomsttid, som sandhedskilden, og planlæg for forsinkede data og data i forkert rækkefølge.
- Vinduer og vandmærker er, hvordan I får endelige svar fra uendelige strømme.
- Foretræk effektivt-én-gang-resultater gennem idempotente sinks frem for skrøbelige exactly-once-løfter.
- Tilstandsfuld behandling kræver checkpointing, så den kan genoprette sig uden at miste eller dobbelttælle.
- Design for modtryk og genbehandling fra dag ét, ikke som en eftertanke.
- Hold streaminglogik observerbar og revisionsbar; en tavs strøm er værre end et fejlet batchjob.

## Anbefalinger

### Begrund realtid, før I bygger det

Den vigtigste streamingbeslutning er, om I overhovedet skal streame. Realtid fordobler groft sagt jeres operationelle kompleksitet og omkostning, fordi I bytter et job, der kører og stopper, ud med et system, der skal være sundt hvert sekund. Før I forpligter jer, så navngiv den beslutning, friske data muliggør, og omkostningen ved, at beslutningen ankommer for sent. Svindelscoring, operationel alarmering og live personalisering klarer som regel overliggeren. Et dashboard, et menneske ser på to gange om dagen, gør det næsten aldrig, uanset hvor tilfredsstillende "realtid" lyder i et planlægningsmøde. Skriv latenskravet ned som et tal, i sekunder eller minutter, og tjek det mod virkeligheden. Meget af det, folk kalder realtid, bliver godt betjent af mikrobatches, der kører hvert par minutter til en brøkdel af omkostningen.

### Design omkring hændelsestid, ikke behandlingstid

Den enkeltstående sværeste idé i streaming er, at hændelser sker på ét tidspunkt og bliver behandlet på et andet. Hændelsestid er, hvornår tingen faktisk skete, for eksempel da en passager tappede et kort. Behandlingstid er, hvornår jeres system fik taget fat i den. De driver konstant fra hinanden: en telefon mister signal i en tunnel og uploader tre minutters tap på én gang, et netværkshik omarrangerer beskeder, en partition halter. Hvis I beregner på behandlingstid, vakler jeres tal med jeres infrastruktur frem for at afspejle verden. Dette problem med forsinkede data og data i forkert rækkefølge er disciplinens kerne, og det hænger direkte sammen med hændelsesmodelleringen i [hændelsesdrevet arkitektur](https://en.wikipedia.org/wiki/Event-driven_architecture). Stempl hver hændelse med dens hændelsestid ved kilden, før det tidsstempel med gennem hele pipelinen, og beregn jeres resultater mod det.

### Brug vinduer og vandmærker til at få endelige svar

En uafgrænset strøm slutter aldrig, så "tæl hændelserne" har intet svar, før I afgrænser den. Vinduer gør den afgrænsning. Tumbling-vinduer hakker tid i faste, ikke-overlappende spande, for eksempel hvert minut. Glidende vinduer overlapper, så et fem-minutters vindue, der rykker frem hvert minut, giver jer et jævnt glidende tal. Sessionsvinduer grupperer byger af aktivitet adskilt af huller af inaktivitet, hvilket passer godt til brugersessioner. Når I har vinduer, skal I afgøre, hvornår et vindue er færdigt, fordi forsinkede data stadig kan ankomme. Et vandmærke er systemets estimat af, at det sandsynligvis har set alle hændelser op til en given hændelsestid. Når vandmærket passerer et vindues slutning, udsender I resultatet. Justér, hvor længe I venter: hold vinduer åbne længere, og I tolererer mere forsinkelse på bekostning af latens og hukommelse, luk dem hurtigere, og I risikerer at tabe eftersnakkere. Afgør eksplicit, hvad der sker med data, der ankommer, efter et vindue er lukket, om I dropper dem, logger dem eller udsender en korrektion.

### Gør sinks idempotente, og foretræk effektivt-én-gang

Leveringsgarantier lyder enkle og er det ikke. At-least-once-levering betyder, at hver hændelse behandles, men nogle kan blive behandlet mere end én gang efter et genforsøg, så tal kan blæses op. Exactly-once lyder ideelt, men er dyrt og, taget bogstaveligt på tværs af vilkårlige eksterne systemer, ofte umuligt. Det praktiske mål er effektivt-én-gang: det observerbare resultat er, som om hver hændelse blev behandlet én gang, selv hvis maskineriet forsøgte igen nedenunder. I kommer dertil ved at gøre jeres [idempotente](https://en.wikipedia.org/wiki/Idempotence) sinks sikre at skrive til gentagne gange, med deterministiske nøgler og upserts, så en genafspillet hændelse overskriver frem for at duplikere. Kombinér at-least-once-levering med idempotente skrivninger, og I får korrekte resultater uden at betale for tung transaktionel koordinering overalt. Forbehold ægte exactly-once-maskineri til de snævre steder, der reelt har brug for det.

### Checkpoint tilstandsfuld behandling, så den kan genoprette sig

Mange nyttige streamingberegninger er tilstandsfulde: løbende tællinger, joins på tværs af strømme, deduplikering, svindelmodeller der husker nylig adfærd. Den tilstand ligger i hukommelsen og ville forsvinde, når en proces genstarter. Checkpointing tager med jævne mellemrum et øjebliksbillede af tilstanden og strømpositionen sammen, så systemet efter et nedbrud genoptager fra et konsistent punkt frem for at afspille alt igen eller miste sin hukommelse. Dimensionér jeres tilstand bevidst, fordi uafgrænset tilstand er en almindelig måde at køre et streamingjob tør for hukommelse i produktion. Brug udløb og time-to-live på tilstand, I ikke længere har brug for, og overvåg tilstandsstørrelse som en førsteklasses måling. Genoprettelsestid efter en fejl er et reelt servicenivåhensyn, så test den, før jeres brugere gør det.

### Stream fra operationelle databaser med change data capture

I vil ofte reagere på ændringer i en database, der aldrig blev designet til at udsende hændelser. [Change data capture](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) løser det ved at læse databasens transaktionslog og forvandle hver insert, update og delete til en strøm af ændringshændelser. Det er langt bedre end at polle tabellen på en timer, hvilket er langsomt, overser mellemliggende tilstande og hamrer på kilden. CDC lader jer holde et søgeindeks, en cache, et analyselager eller en nedstrøms tjeneste kontinuerligt synkroniseret med et kildesystem, og det gør det uden indgribende ændringer i applikationen. Behandl ændringsstrømmen som et førsteklasses dataprodukt: versionér dens skema, dokumentér dens betydning, og hold øje med dens lag, fordi alt nedstrøms arver det lag.

### Foretræk en streaming-først-arkitektur frem for at vedligeholde to kodebaser

Den klassiske [Lambda-arkitektur](https://en.wikipedia.org/wiki/Lambda_architecture) kører et batchlag for nøjagtig, komplet historik ved siden af et hastighedslag for friske, tilnærmede resultater og fletter dem så sammen. Den virker, men den får jer til at skrive og vedligeholde den samme forretningslogik to gange, i to systemer, og afstemme forskellene for evigt. Kappa-arkitekturen kollapser dette: hold en varig, genafspillelig log af hændelser, og kør al behandling som strømbehandling, og genbehandl historik ved at afspille loggen igen, når logikken ændres. Branchen er drevet mod denne streaming-først-form, fordi en enkelt kodebase er dramatisk billigere at vedligeholde og ræsonnere om. Hvis I kan udtrykke jeres batchbehov som genafspilninger over en bevaret hændelseslog, undgår I helt to-kodebaser-skatten. Brug logbaserede brokere, der bevarer historik, så genbehandling er et spørgsmål om at spole tilbage, ikke om at genopbygge.

### Eksponér strømme som SQL, materialiserede views og realtids-OLAP

Ikke alle, der har brug for streaming, bør skulle skrive lavniveau strømbehandlingskode. Streaming-SQL lader analytikere og ingeniører udtrykke vinduer, joins og aggregeringer i et sprog, de allerede kender, og det holder resultaterne løbende ajour som materialiserede views. Til lavlatens analytiske forespørgsler over friske data indtager et realtids-[OLAP](https://en.wikipedia.org/wiki/Online_analytical_processing)-lager (online analytical processing) strømmen og besvarer slice-and-dice-forespørgsler på millisekunder, hvilket er det, der driver et reelt levende operationelt dashboard. Par disse med produktanalysepraksisserne i kapitel 7.4 (produktanalyse og eksperimenter), når målet er hurtig feedback på funktioner og eksperimenter. Vælg disse højniveauværktøjer, hvor de passer, og gem håndskrevne strømbehandlere til logik, de ikke kan udtrykke.

### Planlæg for modtryk og genbehandling fra begyndelsen

En strøm kan ankomme hurtigere, end I kan behandle den. Modtryk er mekanismen, der lader en langsom forbruger signalere opstrøms om at sænke tempoet frem for at falde om eller tabe data tavst. Sørg for, at hvert trin i jeres pipeline respekterer det, og overvåg forbrugerlag som en overskriftsmåling, fordi voksende lag er den tidligste advarsel om, at I taber kapløbet. Genbehandling er den anden evne, folk ønsker, de havde bygget ind. Når I finder en fejl eller ændrer en regel, vil I afspille historik igen gennem den rettede logik. Det er kun muligt, hvis jeres hændelseslog bevarer nok historik, og jeres sinks er idempotente nok til at absorbere genafspilningen. Design begge ind fra dag ét; at eftermontere dem under hændelsespres er elendigt.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper | Bedst egnet |
| --- | --- | --- | --- |
| Batch | Enkelt, billigt, let at teste og efterfylde | Høj latens, forældet mellem kørsler | Rapportering, det meste analyse |
| Mikrobatch (minutter) | Næsten realtid, langt enklere end streaming | Ikke helt øjeblikkelig | "Realtids"-dashboards |
| Ægte streaming (under et sekund) | Øjeblikkelig reaktion, løbende resultater | Kompleks, dyr, svær at teste | Svindel, alarmering, live personalisering |
| At-least-once + idempotent sink | Korrekte resultater, overkommeligt, robust | Kræver disciplineret nøgledesign | De fleste streamingpipelines |
| Exactly-once-maskineri | Stærk garanti ende til ende | Dyrt, begrænset på tværs af systemer | Snævre højindsatsstier |
| Lambda (batch + hastighed) | Nøjagtig historik plus frisk visning | To kodebaser at vedligeholde | Ældre migreringer |
| Kappa (streaming-først) | Én kodebase, genafspillelig | Kræver bevaret, varig log | Nye streamingplatforme |

Den centrale spænding er latens mod kompleksitet. Hvert skridt mod realtid koster jer i driftsbyrde, testvanskelighed og penge, og afkastet er ikke lineært: at gå fra dagligt til hvert par minutter er billigt og ofte nok, mens det er ved overgangen fra minutter til under et sekund, at udgiften koncentreres. Løs spændingen ved at prissætte beslutningen, ikke teknologien. Spørg, hvilken handling friskheden muliggør, og hvad forsinkelse koster, og køb så kun så meget latensreduktion, som den handling retfærdiggør. Når I har brug for streaming, så læn jer op ad at-least-once-levering med idempotente sinks og en streaming-først-log, fordi den kombination giver jer korrekthed og genafspillelighed uden de tungeste garantier.

## Spørgsmål til drøftelse med dit team

1. **Hvilken beslutning muliggør realtidsdata reelt for os, og hvad koster det, når dataene ankommer et minut for sent i stedet for øjeblikkeligt?** Det er det spørgsmål, der bør lukke hvert streamingprojekt, fordi streaming groft sagt fordobler jeres operationelle omkostning og kompleksitet sammenlignet med batch. Et stort team kan brænde kvartaler af på at bygge en realtidsplatform, der betjener dashboards, et menneske tjekker to gange om dagen, hvilket er penge sat i brand. Tag den konkrete handling, dataene driver, med, hvad enten det er at blokere en svigagtig transaktion, at kalde en operatør eller at ændre, hvad en bruger ser, og sæt et tal på omkostningen ved latens for hver. Hvis det ærlige svar er, at en fem-minutters mikrobatch ville dække behovet, er det et fund, der er værd at fejre, ikke skjule. Svaret bør direkte ændre, om I bygger ægte streaming, nøjes med mikrobatches eller bliver i batch.

2. **Hvordan håndterer vi forsinkede hændelser og hændelser i forkert rækkefølge, og hvad sker der med data, der ankommer, efter et vindue er lukket?** Forsinkede data og data i forkert rækkefølge er den svære del af streaming, og teams, der springer dette spørgsmål over, opdager det i produktion, når deres tal nægter at stemme. De modstridende pres er latens og korrekthed: hold vinduer åbne længere for at fange eftersnakkere, og I forsinker hvert resultat og bruger mere hukommelse, luk dem hurtigere, og I dropper tavst rigtige data. Tag dokumentation for, hvor sent jeres data faktisk ankommer, målt som forskellen mellem hændelsestid og behandlingstid på tværs af jeres kilder, med, da en mobilkilde i tunneler opfører sig ganske anderledes end en serverside-hændelse. Afgør eksplicit, om forsinkede data droppes, logges eller udløser en korrektion, og sørg for, at alle nedstrøms ved hvilket. I en offentlig sammenhæng, hvor tal skal kunne forsvares, kan tavs droppen af forsinkede hændelser være et complianceproblem, så politikken skal være bevidst og dokumenteret.

3. **Er vores sinks idempotente nok til, at vi sikkert kan afspille historik igen, og bevarer vores hændelseslog nok til, at genafspilning er mulig?** Genbehandling er den evne, teams oftest ønsker, de havde bygget ind, og oftest ikke gjorde, og den afhænger af to ting, der virker sammen: idempotente sinks, der absorberer genafspillede hændelser uden at duplikere, og en varig log, der bevarer nok historik til at afspille fra. Uden begge betyder det at rette en logikfejl, at I ikke rent kan genberegne den berørte periode, og at I sidder fast med at lappe tal i hånden under pres. Tag jeres nuværende opbevaringsvindue og en konkret test med: vælg en reel fejl fra sidste kvartal, og spørg, om I kunne have afspillet den rettede logik over de berørte data. Trækket imod dette er omkostning, da det kræver lagerplads og disciplin på forhånd at bevare historik og designe idempotente skrivninger. Men alternativet dukker op på det værst tænkelige tidspunkt, under en hændelse, så svaret former, hvor meget I investerer i genafspillelighed, før I får brug for den.

4. **Når et streamingjob styrter ned, hvor hurtigt skal det genoprette sig, hvor meget tilstand må det holde, og har vi faktisk målt en genoprettelse under produktionsbelastning?** Et batchjob, der dør, kan køres igen i morgen, men en altid-tændt strøm, der dør, er et igangværende udfald, og tilstandsfulde jobs, der holder løbende tællinger, joins eller svindelmodeller, kan miste minutters hukommelse eller tage lang tid om at genindlæse tilstand efter en genstart. For et stort team er det her, en uglamourøs detalje stille sætter jeres reelle tilgængelighed: uafgrænset tilstand vokser, til et job løber tør for hukommelse, og en langsom checkpoint-gendannelse forvandler et ti-sekunders hik til et ti-minutters. De modstridende pres er friskhed mod sikkerhed, fordi hyppigere checkpoints forkorter genoprettelse, men tilføjer overhead, og generøs tilstandsbevaring forbedrer nøjagtighed, men risikerer hukommelsesudmattelse. Tag et konkret genoprettelsestidsmål, jeres nuværende tilstandsstørrelse og dens vækstkurve, jeres checkpoint-interval og resultaterne af en reel failover-øvelse med frem for et håbefuldt estimat. I virksomheds- og offentlige sammenhænge, hvor strømmen understøtter svindelscoring eller en offentlig sikkerhedsfeed, er en utestet genoprettelsesvej en driftsrisiko, I har accepteret uden at måle, så behandl øvelsen som et krav, ikke et rart-at-have.

5. **Kører vi én streaming-først-kodebase eller et separat batchlag og hastighedslag, og hvad koster det os reelt at holde de to afstemt?** Lambda-mønstret med et batchlag til nøjagtig historik plus et hastighedslag til friske resultater tvinger jer til at skrive den samme forretningslogik to gange, i to systemer, og afstemme deres svar for evigt, hvorimod en streaming-først-form (Kappa) holder en varig, genafspillelig log og kører al behandling som strømbehandling. For en stor organisation er den duplikerede logik, hvor drift og omstridte tal yngler, fordi en regel ændres i det ene lag og ikke i det andet, og ingeniører bruger reel tid på at forklare, hvorfor de to er uenige. Trækket mod at beholde begge er inerti og trygheden ved et gennemprøvet batchlag, så vej det ærligt mod vedligeholdelsesskatten. Tag listen over beregninger, I i dag kører begge steder, de hændelser, der skyldtes de to lags uenighed, og en vurdering af, om jeres hændelseslog bevarer nok historik til at udtrykke batchbehov som genafspilninger, med. I offentlige og reviderede virksomhedssammenhænge er to lag, der kan rapportere forskellige tal for samme periode, i sig selv en complianceforpligtelse, da I skal kunne sige, hvilket tal der er autoritativt og hvorfor.

6. **Hvem driver dette altid-tændte system, når det går i stykker klokken tre om natten, og har vi budgetteret den vagtbelastning og de specialistfærdigheder, det kræver, eller antager vi batchformet bemanding?** Streaming flytter omkostning fra bygning til drift: systemet skal være sundt hvert sekund, hvilket betyder reel vagtdækning, ingeniører flydende i hændelsestid, vandmærker, tilstand og leveringssemantik, og test, der er sværere end for et job, der kører og stopper. Teams godkender rutinemæssigt en streamingplatform på grund af dens kapaciteter og finansierer aldrig de mennesker, der holder den i live, så platformen forfalder, og tilliden eroderer. Afvejningen er omfang mod bæredygtighed: hver yderligere realtidspipeline er endnu en ting, der kan kalde nogen ud, så spørgsmålet er, om den latens, den køber, retfærdiggør en permanent driftsforpligtelse. Tag en ærlig fortegnelse over, hvem der ejer hver strøm i produktion, jeres nuværende vagtrotation og dens luft, og hvor hændelsestidsekspertisen faktisk sidder, hvad enten det er en ansættelse, en partner eller en administreret tjeneste, med. For et offentligt organ eller en stor virksomhed så tilføj indkøbs- og ansættelsesledetider og enhver administreret tjenestemulighed, for en realtidsplatform, der afhænger af knap talent, I ikke kan rekruttere eller fastholde, er en plan om at drive et udfaldstruet system underbemandet.

## Sektorperspektiv

**Startup.** Streaming er sjældent jeres første træk, og at rejse en tung platform kan sænke et lille team. Vælg det ene signal, der berører jeres kerneværdi, læg hændelser på en enkelt bevaret logbaseret broker, og kør en let processor med nøglede, idempotente sinks, så et at-least-once-genforsøg aldrig dobbelttæller. Behold nogle dages historik, så I kan afspille igen gennem rettet logik, og foretræk en administreret streamingtjeneste frem for selv at drive en klynge, fordi jeres knappeste ressource er ingeniøropmærksomhed.

**Lille virksomhed.** I har sandsynligvis ingen streamingspecialist og ingen lyst til at drive altid-tændt infrastruktur, så behandl realtid som noget, I køber inde i værktøjer, I allerede bruger, frem for et system, I bemander. Ram behovet ind som et latensspørgsmål med et tal på, og i de fleste tilfælde vil en mikrobatch, der opdaterer hvert par minutter, opfylde det til en brøkdel af omkostning og risiko. Vælg leverandører, hvis realtidsfunktioner er åbne om lag og lette at falde tilbage fra, og forbehold skræddersyet streaming til de sjældne tilfælde, hvor friske data direkte driver omsætning eller sikkerhed.

**Stor virksomhed.** Problemet er ensartethed og omkostning på tværs af mange teams: en fælles logbaseret platform, en standard hændelsestids- og forsinkededatapolitik og idempotente sinks, så grupper holder op med at genopfinde skrøbelige pipelines. Budgettér den altid-tændte drift og vagtbyrden eksplicit, standardisér på en streaming-først-log, så I undgår en duplikeret batchkodebase, og styr strømme som styrede dataprodukter med ejere, skemaversionering og overvåget lag frem for en spredning af skræddersyede jobs. Følg latens, genoprettelsestid og omkostning pr. strøm som porteføljemålinger.

**Offentlig sektor.** Revisionsbarhed og offentlig ansvarlighed former hvert valg. Bevar hver behandlet hændelse i en varig log, så tal rapporteret til tilsynsorganer, passagertal, ydelsesanomalier, svindelbeslutninger, kan rekonstrueres præcist, og gør forsinkededatapolitikken eksplicit og dokumenteret frem for tavst at droppe hændelser. Indkøb bør kræve dataportabilitet og åbenhed om en administreret tjenestes leverings- og opbevaringsgarantier, og enhver genfremsættelse efter en regelændring bør være en forsvarlig genafspilning gennem rettet logik, ikke et manuelt plaster, ingen kan spore.

## Eksempler

**Startup.** En forbrugerapp vil vise brugere en levende aktivitetsfeed og flagge mistænkelige logins, mens de sker. Teamet modstår at rejse en tung streamingplatform. De lægger hændelser på en enkelt bevaret logbaseret broker, kører en let strømprocessor til login-risikologikken og fodrer et realtids-OLAP-lager, der driver aktivitetsfeeden. Hver sink er nøglet og idempotent, så et at-least-once-genforsøg aldrig dobbelttæller. Da de senere finder en fejl i risikoreglen, afspiller de blot loggen igen gennem den rettede logik natten over, fordi de beholdt en uges historik og aldrig behøvede en anden batchkodebase.

**Stor virksomhed.** En detailbank scorer hver korttransaktion for svindel inden for godkendelsesvinduet og joiner den levende transaktionsstrøm mod en tilstandsfuld model af nylig kontoadfærd. Checkpointing lader scoringstjenesten genoprette sig efter en nodefejl på sekunder uden at miste sin hukommelse om de seneste minutter. Separat streamer change data capture opdateringer fra kernebankdatabasen ind i et søgeindeks og en personaliseringstjeneste og holder begge friske uden polling. Operationelle dashboards læser fra et realtids-OLAP-lager, så risiko- og driftsteams ser forretningen, mens den bevæger sig, og hele pipelinen udsender den lag- og gennemløbstelemetri, der er beskrevet i kapitel 9.2.

**Offentlig sektor.** En storbys transportmyndighed indtager køretøjspositioner og billettap for at forudsige ankomster og overvåge trængsel i realtid, hvilket fodrer både offentlige apps og et driftscenter. Fordi passagerer i tunneler uploader tap i forsinkede byger, beregner teamet passagertal på hændelsestid med vandmærker justeret til den observerede forsinkelse og logger enhver hændelse, der ankommer efter dens vindue er lukket, frem for at droppe den tavst. Hver behandlet hændelse bevares i en revisionsbar log, så passagertal rapporteret til tilsynsorganer kan rekonstrueres præcist. Når en takstregel ændres, afspiller de den berørte periode igen gennem den rettede logik og producerer en forsvarlig genfremsættelse.

## Business case: motivation, ROI og TCO

Afkastet af realtidsdata kommer af at handle, mens handling stadig betyder noget. Svindel fanget under godkendelse forebygger et tab, som et natligt batch kun ville rapportere. Personalisering, der reagerer inden for en session, løfter konvertering på en måde, som morgendagens anbefaling ikke kan. Operationel overvågning, der afspejler nuet, lader jer gribe ind, før et lille problem bliver et udfald eller en offentlig hændelse. I hvert tilfælde er værdien deltaet mellem at handle nu og at handle senere, og det delta er, hvad I bør kvantificere, når I laver sagen.

Den samlede ejeromkostning er højere end batch, og ærlighed om det beskytter jeres troværdighed. I betaler for altid-tændt infrastruktur, for ingeniører der forstår hændelsestid, vandmærker, tilstand og leveringssemantik, og for den sværere test- og vagtbyrde i et system, der skal være sundt kontinuerligt frem for at køre og stoppe. En streaming-først-arkitektur på en bevaret log sænker de løbende omkostninger ved at spare jer for en duplikeret batchkodebase, og at vælge at-least-once med idempotente sinks undgår udgiften til ende-til-ende exactly-once-maskineri. Den dyreste fejl er at bygge realtid, hvor mikrobatch eller batch ville række, så det stærkeste omkostningsargument er ofte en beslutning om ikke at streame. Ram pitchen til ledelsen ind omkring specifikke latensfølsomme beslutninger og deres målbare udbytte, og vær lige så klare om, hvor det at blive i batch sparer penge uden tab af værdi.

## Anti-mønstre og faldgruber

- At bygge streaming for prestige, når en mikrobatch hvert par minutter ville dække behovet.
- At beregne på behandlingstid, så jeres tal vakler med jeres infrastruktur i stedet for verden.
- At ignorere forsinkede data og data i forkert rækkefølge, til afstemning fejler i produktion.
- At jagte bogstaveligt exactly-once overalt i stedet for at-least-once med idempotente sinks.
- Uafgrænset tilstand uden udløb, der stille vokser, til et job løber tør for hukommelse.
- Ingen checkpointing, så en genstart mister tilstand eller tvinger en fuld genafspilning.
- At polle operationelle databaser på en timer i stedet for at bruge change data capture.
- At vedligeholde et Lambda-batchlag og hastighedslag med duplikeret, driftende logik.
- Et opbevaringsvindue for kort til at afspille historik igen, når I finder en fejl.
- Strømme uden lag-, gennemløbs- eller friskhedsmålinger, der fejler tavst.

## Modenhedsmodel

- **Niveau 1, Opstart:** Alt er batch, eller nogle få håndbyggede streamingjobs kører reaktivt uden overvågning. Tal beregnes på behandlingstid, forsinkede data ignoreres, og en genstart mister tilstand. Ingen kan afspille historik igen for at rette en fejl, og problemer opdages, når nedstrøms tal nægter at stemme.
- **Niveau 2, Udvikling:** Nogle teams kører centrale streamingpipelines på en logbaseret broker med checkpointing, og de skelner hændelsestid fra behandlingstid og bruger basale vinduer. Praksis er inkonsistent fra team til team: levering er at-least-once, men ikke alle sinks er idempotente, håndtering af forsinkede data er improviseret, og lag overvåges uformelt frem for at blive alarmeret på.
- **Niveau 3, Standardisering:** Hændelsestid, vandmærker og en eksplicit forsinkededatapolitik er dokumenteret og anvendt på tværs af organisationen. Sinks er idempotente for effektivt-én-gang-resultater, tilstand har udløb, og change data capture fodrer nedstrøms systemer efter konvention. En bevaret log understøtter genafspilning, og lag, gennemløb og friskhed overvåges med alarmer som en organisationsstandard frem for en vane pr. team.
- **Niveau 4, Styring:** Streamingejendommen måles og styres mod baselines. Hver pipeline bærer servicenivåmål for ende-til-ende latens, forbrugerlag, genoprettelsestid, hændelsestidsskævhed, rate af forsinkede hændelser, tilstandsstørrelse og omkostning pr. million hændelser, alle fulgt mod aftalte mål og alarmerende ved regression. Genoprettelse øves og tidsmåles frem for antages, modtrykshøjde og tilstandsvækst overvåges som kapacitetssignaler, og en ny strøm skal klare disse målinger, før den går i produktion.
- **Niveau 5, Orkestrering:** En streaming-først-arkitektur betjener både friske og historiske behov fra én genafspillelig log, og streaming-SQL, materialiserede views og realtids-OLAP gør friske data bredt tilgængelige. Genbehandling er rutine og testet, platformen autoskalerer og rebalancerer mod målt belastning og omkostning, og strømme pensioneres, omafgrænses eller erstattes på dokumentation. Streaming er integreret med forretnings- og risikoplanlægning, og hver strøm er observerbar og revisionsbar ende til ende, efterhånden som belastnings- og omkostningsbilledet skifter.

## Idéer til drøftelse

1. Hvor i jeres stak tjener "realtid" reelt sin omkostning, og hvor er det et uprøvet ønske?
2. Hvor stort er hullet mellem hændelsestid og behandlingstid på tværs af jeres kilder, og måler I det?
3. Kunne I kollapse en Lambda-opsætning med batch og hastighed til en enkelt streaming-først-kodebase, og hvad ville blokere det?
4. Hvilke af jeres sinks er reelt idempotente, og kunne I i dag sikkert afspille sidste kvartals data igen gennem rettet logik?
5. Hvad er jeres politik for data, der ankommer, efter et vindue er lukket, og ved alle nedstrøms den?
6. Hvordan ville change data capture ændre måden, I holder søgning, caches og analyse synkroniseret på?

## Vigtigste pointer

- Ræk kun efter streaming, når en latensfølsom beslutning betaler for det; batch og mikrobatch er billigere standarder.
- Beregn på hændelsestid, og behandl forsinkede data og data i forkert rækkefølge som kerneproblemet, håndteret med vinduer og vandmærker.
- Foretræk at-least-once-levering med idempotente sinks for effektivt-én-gang-resultater frem for bogstaveligt exactly-once overalt.
- Checkpoint tilstandsfuld behandling, afgræns jeres tilstand, og overvåg forbrugerlag som en overskriftsmåling.
- Brug change data capture til at streame fra operationelle databaser i stedet for at polle.
- Foretræk en streaming-først-arkitektur på en bevaret, genafspillelig log frem for at vedligeholde to kodebaser.
- Eksponér strømme gennem streaming-SQL, materialiserede views og realtids-OLAP, og hold hver strøm observerbar og revisionsbar.

## Referencer og videre læsning

- Tyler Akidau, Slava Chernyak, and Reuven Lax, "Streaming Systems."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Jay Kreps, "Questioning the Lambda Architecture" (O'Reilly Radar).
- Fabian Hueske and Vasiliki Kalavri, "Stream Processing with Apache Flink."
- Ben Stopford, "Designing Event-Driven Systems."
- Tyler Akidau and colleagues, "The Dataflow Model" (VLDB paper on windowing and watermarks).
