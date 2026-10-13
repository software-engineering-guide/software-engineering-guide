# 1.10 Teknisk effektivitet og udvikleres produktivitet

## Overblik og motivation

Enhver leder af en stor softwareorganisation stiller før eller siden en variant af det samme spørgsmål: bliver vi bedre til at bygge software, og hvordan ville vi vide det? Dette kapitel handler om at besvare det ærligt. **Teknisk effektivitet** er, hvor godt din organisation omsætter ingeniørindsats til værdifuld, pålidelig software. **Udvikleres produktivitet** er den individuelle og teammæssige side af det: hvor meget nyttigt output en udvikler kan producere, og hvor meget af deres tid og opmærksomhed arbejdsmiljøet giver tilbage frem for at tage fra dem.

Problemerne begynder i det øjeblik, nogen forsøger at reducere dette til ét enkelt tal. Tæl kodelinjer, og folk skriver mere kode. Tæl story points, og estimaterne oppustes. Tæl commits, pull requests eller timer ved skrivebordet, og du belønner bevægelse i stedet for fremskridt. Produktivitet for en vidensarbejder er ikke et stykantal. En udvikler, der sletter ti tusind linjer død kode, eller som bruger en dag på at parre, så en kollega undgår et produktionsnedbrud, har udført fremragende arbejde, som ingen naiv måling fanger. Det ærlige svar på "hvor produktive er vi?" er flerdimensionelt, og det behandler udviklerens oplevelse af arbejdet som et reelt signal frem for et blødt.

Det betyder mere, ikke mindre, når du skalerer. I en virksomhed med dusinvis af teams multipliceres små mængder gnidning (en langsom build, en ustabil testsuite, to dages ventetid på et miljø) på tværs af hundredvis af ingeniører til enorm tabt kapacitet. I det offentlige, hvor der ikke er nogen markedspris på output, er risikoen "output-teater": at måle producerede dokumenter eller lukkede sager, mens offentlig værdi forbliver umålt. Målet med dette kapitel er at hjælpe dig med at måle og forbedre ingeniørorganisationens effektivitet og udviklernes dagligdagsoplevelse uden manipulation, overvågning eller rangordning af folk mod hinanden.

## Grundprincipper

- **Produktivitet er flerdimensionel.** Intet enkelt tal fanger den. Enhver måling, der tilbydes som *den* måling, er forkert.
- **Mål for at fjerne gnidning, ikke for at rangordne folk.** Målingens genstand er systemet, ikke individet.
- **Triangulér.** Kombinér hvordan udviklere siger, arbejdet føles, med hvad systemerne faktisk registrerer.
- **Udviklerens oplevelse er data.** Feedbackløkker, kognitiv belastning og flow kan måles og er værd at forbedre.
- **Antag, at enhver måling vil blive manipuleret.** Design mod Goodharts lov med flere dimensioner og ærlig hensigt.
- **Forbind til resultater, omhyggeligt.** Effektivitet bør kunne føres op til forretningsværdi uden at blive et mål, der korrumperer.

## Anbefalinger

### Afvis fælden med den enkelte måling

Den første disciplin er at nægte at udpege ét tal som produktivitet. Kodelinjer, antal commits, story points-[velocity](https://en.wikipedia.org/wiki/Velocity_(software_development)) og loggede timer deler alle en fatal fejl: de måler aktivitet, ikke værdi, og aktivitet er trivielt at oppuste. Det er [Goodharts lov](https://en.wikipedia.org/wiki/Goodhart%27s_law) i aktion, princippet om at når en måling bliver et mål, holder den op med at være en god måling. Velocity blev opfundet som et teams eget prognoseredskab; i det øjeblik en leder sammenligner ét teams points med et andets, omskalerer teams stille deres estimater, og tallet bliver meningsløst. Når nogen kræver en enkelt produktivitets-KPI, så behandl det som en anmodning, du må omforme, ikke opfylde. Tilbyd i stedet et lille balanceret sæt, og forklar, hvorfor ét tal ville vildlede dem.

### Brug SPACE til at strukturere, hvad du måler

**SPACE-rammen** giver dig de fem dimensioner, der er værd at holde sammen: **S**atisfaction (tilfredshed) og trivsel, **P**erformance (præstation), **A**ctivity (aktivitet), **C**ommunication (kommunikation) og samarbejde samt **E**fficiency (effektivitet) og flow. Pointen med SPACE er, at du bør vælge mindst nogle få dimensioner, aldrig kun én, og aldrig alle fra samme kategori. Aktivitetsmål (commits, udrulninger) er forførende, fordi de er lette at indsamle, men alene forvrider de. Par dem med et tilfredshedssignal og et præstationssignal, så ingen enkelt dimension kan manipuleres uden at de andre afslører det. Et team, der udruller mere, mens tilfredsheden styrtdykker og andelen af fejlslagne ændringer stiger, er ikke mere produktivt, og et balanceret sæt viser dig det med det samme.

### Behandl udvikleroplevelse som feedbackløkker, kognitiv belastning og flow

**Udvikleroplevelse (DevEx)** er, hvordan det føles at udføre ingeniørarbejde her, og den er mere konkret, end den lyder. Den hviler på tre ting, du kan måle og forbedre. **Feedbackløkker** er, hvor længe en udvikler venter på at lære, om noget virkede: lokal buildtid, testsuitens varighed, gennemløbstid for kodegennemgang, udrulningstid. Langsomme løkker tvinger kontekstskift og tomgangsventen. **[Kognitiv belastning](https://en.wikipedia.org/wiki/Cognitive_load)**, den samlede mentale indsats en opgave kræver, vokser, når en udvikler må jonglere med for mange værktøjer, udokumenterede systemer og sammenfiltrede afhængigheder for at lave en simpel ændring. **[Flow](https://en.wikipedia.org/wiki/Flow_(psychology))** er den tilstand af fokuseret, produktiv fordybelse, som fragmenterede kalendere og konstante afbrydelser ødelægger. Når du forkorter en feedbackløkke, fjerner et begreb en udvikler skulle holde i hovedet eller beskytter en blok fokustid, har du forbedret produktiviteten på en måde, ingen aktivitetstælling ville registrere. Det er samme DevEx-bekymring, som platformsudvikling tjener gennem paved roads og selvbetjening (kapitel 8.4).

### Triangulér opfattelser med systemmålinger

Ingen enkelt datakilde er pålidelig alene, så kombinér to slags. **Opfattelsesdata** kommer fra udviklerne selv gennem en **udvikleroplevelsesundersøgelse**: et regelmæssigt, for det meste anonymt spørgeskema, der spørger, hvor trygge de føler sig ved at levere, hvor de mister tid, og hvad der frustrerer dem. **Systemdata** kommer fra dine værktøjer: pipelinetider, gennemgangsventetid, hændelsesfrekvens. Hver korrigerer den anden. Undersøgelser fanger smerte, instrumenter overser, såsom en demoraliserende vagtrotation eller en frygtet legacy-tjeneste. Systemmålinger fanger problemer, folk har normaliseret og holdt op med at rapportere. Når en undersøgelse siger, at builds er pinefulde, og dine pipelinedata bekræfter en median-build på femten minutter, har du en prioriteret, forsvarlig investering. Kør undersøgelsen med en stabil kadence, hold den kort, og luk altid løkken ved at vise, hvad der ændrede sig på grund af den.

### Brug DORA som et leveringssignal, ikke en rangliste

De fire **[DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA)**-målinger (udrulningsfrekvens, ledetid for ændringer, andel fejlslagne ændringer og tid til at genoprette service) er en stærk, forskningsbaseret aflæsning af din leveringsevne, som parrer hastighed med stabilitet, så ingen af delene ofres for den anden. Kapitel 11.5 ejer dybden i disse, og kapitel 11.2 dækker den leveringspipeline, de måler; brug dem der. Her handler vejledningen om, hvordan du holder dem. Behandl DORA som et sundhedssignal på teamniveau, der viser, om dit leveringssystem forbedres, ikke som en resultattavle til at rangordne teams eller individer. I det øjeblik DORA-tal dukker op i nogens præstationssamtale, begynder teams at opdele udrulninger for at pumpe frekvensen og skjule hændelser for at beskytte deres fejlrate, og signalet dør.

### Mål systemet, overvåg aldrig individet

Dette er den linje, du ikke må krydse. Aggregér målinger til team- og organisationsniveau, og brug dem til at finde og fjerne gnidning. Byg ikke dashboards, der rangordner udviklere efter commits, timer eller "produktivitetsscorer", og lad ikke individuel telemetri føde løn eller forfremmelse. Overvågning ødelægger den psykologiske tryghed og tillid, effektiv ingeniørkunst afhænger af, og lærer folk at optimere målingen i stedet for arbejdet. Individuel vækst og vurdering hører til de særskilte, menneskelige mekanismer med karrierestiger og lederens samtaler (kapitel 1.3). Effektivitetsmåling spørger "hvad bremser vores teams?" Den spørger aldrig "hvem er vores langsomste ingeniør?"

### Angrib manuelt slid og gnidning direkte

Når du kan se, hvor tid lækker, så brug den tilbage. Meget af det, der begrænser effektiviteten, er **toil** (manuelt slid), det manuelle, gentagne, automatiserbare arbejde, der vokser med væksten og ikke leverer varig værdi (kapitel 9.1). Langsomme gennemgange er også gnidning, så at strømline kodegennemgang (kapitel 2.5) med mindre ændringer og klare forventninger forkorter en central feedbackløkke. Paved roads og selvbetjeningsplatforme (kapitel 8.4) fjerner hele kategorier af ventetid og kognitiv belastning på én gang. Budgettér også mod [teknisk gæld](https://en.wikipedia.org/wiki/Technical_debt), de akkumulerede omkostninger ved tidligere genveje, der beskatter hver fremtidig ændring, for en kodebase, ingen sikkert kan ændre, er det dybeste produktivitetssluk af dem alle.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
| --- | --- | --- |
| Enkelt produktivitetsmåling (LOC, velocity, commits) | Billig, let, ét tal til ledere | Manipuleres med det samme; måler aktivitet ikke værdi; nedbryder tillid |
| SPACE-lignende balanceret sæt | Modstår manipulation; afspejler virkeligheden | Mere arbejde at indsamle; sværere at opsummere i ét tal |
| DevEx-undersøgelse (opfattelse) | Fanger følt smerte, instrumenter overser | Subjektiv; kræver tillid og opfølgning for at forblive ærlig |
| Systemmålinger (DORA, pipelinetider) | Objektive, løbende, svære at forfalske samlet | Blinde for moral og kontekst; farlige, hvis de anvendes på individer |
| Triangulering af begge | Hver kilde korrigerer den anden; robust | Kræver investering i værktøjer og undersøgelsesdisciplin |

Den centrale spænding er stringens versus ærlighed. Et enkelt tal er let at rapportere og let at korrumpere; et rigt, flerdimensionelt billede er ærligt, men sværere at formidle til en travl direktør. Løs det ved at vælge et lille balanceret sæt (nogle få SPACE-dimensioner plus en undersøgelse plus DORA som en leveringsaflæsning), rapportere tendenser frem for øjebliksbilleder og være eksplicit om, at tallene findes for at forbedre systemet, ikke for at score folk. Når ledelsen vil have "ét diagram", så giv dem en tendens for nogle få komplementære signaler, og modstå fristelsen til at kollapse dem til en falsk sammensat måling.

## Spørgsmål til drøftelse med dit team

1. **Hvis en leder i morgen krævede et enkelt produktivitetstal, hvad ville I give vedkommende?** Spørgsmålet afslører, om jeres organisation forstår fælden. Det ærlige svar er, at intet enkelt tal er sikkert, og at jeres opgave er at omforme anmodningen til et lille balanceret sæt, der modstår manipulation. Tag de målinger med, I allerede rapporterer, og spørg for hver: "hvordan ville et klogt, kynisk team oppuste dette uden at gøre bedre arbejde?" Hvis svaret er let, er målingen farlig i det øjeblik, den bliver et mål. Drøft, hvad I i stedet ville tilbyde, og hvordan I ville forklare ledelsen, hvorfor ét tal ville få dem til at optimere det forkerte. Kvaliteten af den samtale forudsiger, om måling vil hjælpe jer eller korrumpere jer.

2. **Hvad er jeres langsomste feedbackløkke, og hvad koster den jer hver dag?** Feedbackløkker er, hvor produktivitet stille lækker: en build på femten minutter, to dages ventetid på gennemgang, en ustabil testsuite, der undergraver tilliden til hvert grønt flueben. Tag reelle tal med fra en udvikleroplevelsesundersøgelse og fra jeres pipelineinstrumenter, og se, om den oplevede smerte og den målte latens stemmer overens. Anslå den daglige omkostning ved at gange ventetiden med, hvor mange udviklere der rammes, og hvor ofte, og argumentet for investering fremstår som regel af sig selv. Beslut, hvilken løkke der skal forkortes først, og hvem der ejer rettelsen. Et team, der ikke kan nævne sin langsomste løkke, er endnu ikke begyndt at måle det, der betyder mest.

3. **Hvor risikerer jeres måling at føles som overvågning, og hvordan forhindrer I det?** Forskellen mellem at måle systemet og at overvåge folk er forskellen mellem tillid og frygt, og den er let at krydse uden at lægge mærke til det. Gå hvert dashboard og hver rapport igennem og spørg, om nogen af dem kunne rangordne et individ eller føde en præstationssamtale. Beslut eksplicit, hvad der forbliver aggregeret, hvad der forbliver anonymt, og hvad der er forbudt, og sig det åbent til de teams, der måles. I virksomheds- og offentlige sammenhænge, hvor tilsyn og revisionspres er stærkt, er fristelsen til at bore ned til individer konstant, så værnet må være et angivet princip, ikke et håb. Hvis udviklere tror, at tallene bruges imod dem, vil de optimere tallene, og sandheden forsvinder.

4. **Da vi sidst spurgte udviklere, hvordan arbejdet føles, hvad ændrede sig på grund af det, og fandt de nogensinde ud af det?** En undersøgelse, der ikke producerer synlig handling, lærer udviklere at holde op med at svare ærligt, så den anden tavse undersøgelse trækker færre og fadere svar end den første, og det instrument, I stoler på, forfalder netop, som I skalerer det. For en stor organisation akkumuleres spildet: hundredvis af mennesker bruger tid på at rapportere gnidning, en rapport cirkulerer, og intet leveres. Tag den seneste undersøgelses tre vigtigste fund med, det konkrete arbejde hvert udløste, og hvordan I kommunikerede resultatet tilbage til dem, der rejste det. Vej det modstridende træk mellem at handle på den højeste klage og at handle på den mest udbredte, for de er ofte forskellige problemer. I virksomheds- og offentlige sammenhænge, hvor undersøgelsestræthed og høringsoverbelastning allerede er høj, så behandl at lukke løkken som en styringsforpligtelse: navngiv, hvem der ejer svaret, offentliggør hvad der ændrede sig, og accepter, at en ubesvaret undersøgelse er værre end ingen.

5. **Hvordan ville vi sammenligne teams uden at bygge en rangliste, der straffer ærlighed?** Ledere af store organisationer vil naturligt gerne vide, hvilke teams der trives, og hvilke der sidder fast, men at rangordne teams efter rå velocity, udrulningsfrekvens eller DORA-tal ignorerer, at et betalingsteam under tung regulering og et greenfield-prototypeteam lever i forskellige verdener. Det modstridende hensyn er reelt: I har brug for at spotte teams i vanskeligheder og sprede det, der virker, men i det øjeblik sammenligning bliver en resultattavle, omskalerer teams estimater, skjuler hændelser og opdeler udrulninger for at beskytte deres placering. Tag konkrete eksempler med på, hvordan teamkontekster er forskellige i jeres organisation, sammen med et forslag om at sammenligne hvert team med sin egen udvikling over tid frem for med naboerne. I virksomheds- og offentlige sammenhænge, hvor revisions- og tilsynspres trykker hårdt mod rangordning på tværs af teams, så aftal på forhånd, hvad der må sammenlignes, hvad der kun nogensinde læses som en tendens pr. team, og hvem der har beføjelse til at afvise en uretfærdig sammenligning.

6. **Hvordan forbinder vi effektivitet til reelle resultater uden at gøre en leveringsmåling til et korrumperende mål?** Effektivitet, der aldrig kan føres op til værdi, ligner navlepilleri for ledelsen, men i det øjeblik et leveringssignal som ledetid eller udrulningsfrekvens bliver målet i en præstationssamtale, optimerer teams tallet og opgiver det resultat, det skulle være proxy for. For en stor organisation er spændingen akut, fordi direktører vil have en ren linje fra ingeniørindsats til forretningsresultater, mens den ærlige linje er rodet og forsinket. Tag jeres nuværende resultatmål med, de leveringssignaler I ville knytte dem til, og en eksplicit redegørelse for, hvordan hvert kunne manipuleres, hvis det blev et mål. Vej trækket mellem en simpel historie, ledelsen kan genfortælle, og et sandfærdigt billede, der modstår forvridning. I det offentlige eller en ikke-markedsbaseret intern platform, hvor der ingen omsætning er at forankre værdi i, så vær klar til at definere resultater som servicepålidelighed, gennemløbstid på rettelser og samfundsnytte frem for rå aktivitet, og til at forsvare det valg over for tilsynsorganer, der måske foretrækker lettere at tælle artefakter.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og lidt runway så spring dashboards helt over og mål de to ting, der bevæger sig hurtigst: en udvikleroplevelsesundersøgelse på ti spørgsmål og grundlæggende pipelinetider. Din største produktivitetsrisiko er en langsom eller ustabil testsuite og konstant kontekstskift, så find den værste feedbackløkke, forkort den, og gå videre. Opsæt ikke et målingsprogram, du ingen har til at køre, for én ærlig samtale om, hvor dagen lækker, slår ethvert værktøj, du så skulle vedligeholde.

**Lille virksomhed.** Uden målingsspecialist og med et stramt budget så læn dig op ad det, dine eksisterende værktøjer allerede registrerer: buildtider, gennemgangsventetid og hændelsestællinger fra de systemer, du allerede betaler for. Køb et let undersøgelsesværktøj frem for at bygge et, og modstå leverandørens tilbud om et individuelt produktivitetsdashboard, som vil koste dig tillid, du ikke har råd til at miste. Ramm hele indsatsen ind som at fjerne gnidning for et lille team, der ikke har råd til at spilde nogens dag.

**Stor virksomhed.** På tværs af dusinvis af teams er gevinsten genvundet kapacitet i stor skala, og faren er et centralt dashboard, der stille glider over i at rangordne folk. Standardisér et balanceret program (en kvartalsvis DevEx-undersøgelse, nogle få SPACE-dimensioner og DORA læst som en leveringstendens pr. team) og styr det, så individuel telemetri aldrig indsamles. Sammenlign hvert team med sin egen udvikling, begrund platforminvestering (kapitel 8.4) mod den gnidning, dataene afslører, og giv én ansvarlig ejer beføjelsen til at afvise enhver måling, der ville blive en rangliste.

**Offentlig sektor.** Uden markedspris på output og med stærkt tilsynspres er trækket mod output-teater (at tælle dokumenter og lukkede sager) konstant, og trækket mod at overvåge navngivne individer under revision er endnu stærkere. Mål i stedet resultater og leveringsevne: hvor hurtigt en tjeneste kan levere en rettelse, hvor pålidelig den er, og hvordan medarbejdere og konsulenter oplever arbejdet gennem en anonym undersøgelse. Mål embedsfolk og konsulenter på samme systemniveau, offentliggør hvad målingen er til for, og vær klar til at argumentere over for en lovgivende forsamling, at en leveringstendens pr. team er en mere ærlig aflæsning af offentlig værdi end nogen individuel score.

## Eksempler

**Startup.** Et startup med tyve medarbejdere bemærker, at leveringen er blevet langsommere, selv om alle har travlt. I stedet for at installere et produktivitetsdashboard kører ingeniørlederen en DevEx-undersøgelse på ti spørgsmål og trækker grundlæggende pipelinetider. Undersøgelsen og dataene er enige: testsuiten tager toogtyve minutter og fejler tilfældigt, så folk samler ændringer og skifter kontekst, mens de venter. Teamet bruger to uger på at rette ustabile tests og parallelisere suiten, så den falder til fire minutter. Udrulningsfrekvensen stiger af sig selv, tilfredsheden springer i næste undersøgelse, og ingen blev nogensinde rangordnet eller scoret for at få det til at ske.

**Stor virksomhed.** En bank med fyrre ingeniørteams vil retfærdiggøre fortsat investering i sin interne platform. Platformsgruppen indfører et balanceret målingsprogram: en kvartalsvis DevEx-undersøgelse på tværs af alle teams, SPACE-lignende signaler og DORA-målinger læst på teamniveau som en leveringssundhedstendens (kapitel 11.5). Afgørende er, at de benchmarker teams retfærdigt ved at sammenligne hvert team med sin egen udvikling over tid, ikke med hinanden, fordi teamkontekster er vidt forskellige. Dataene viser, at teams på paved roads (kapitel 8.4) onboarder nye ingeniører på dage frem for uger og rapporterer langt lavere kognitiv belastning. Den dokumentation, rammet ind som genvundet kapacitet på tværs af hundredvis af udviklere, finansierer platformen i endnu et år. Individuel telemetri indsamles bevidst aldrig.

**Offentlig sektor.** Et føderalt digitaltjenesteagentur skal vise en lovgivende forsamling, at dets ingeniørudgifter leverer værdi, i en sammenhæng uden markedspris på output. Det afviser output-teater (at tælle dokumenter eller lukkede sager) og måler i stedet resultater og leveringsevne: hvor hurtigt tjenester kan levere en rettelse, hvor pålidelige de er, og hvordan arbejdsstyrken og dens konsulenter oplever arbejdet gennem en anonym undersøgelse. DORA-lignende leveringssignaler viser, om modernisering faktisk forbedrer gennemløb og stabilitet, knyttet tilbage til offentlige resultater frem for rå aktivitet (kapitel 11.5). Fordi måling aldrig rangordner individer, og fordi konsulenter og fastansatte måles på samme systemniveau, undgår agenturet de overvågnings- og moralproblemer, der sænker sådanne indsatser, og giver tilsynsorganer en ærlig aflæsning af værdi.

## Business case: motivation, ROI og TCO

Afkastet af at måle og forbedre effektivitet er genvundet kapacitet, og i stor skala er tallene store. Små gnidninger multipliceres på tværs af en stor organisation: en build på ti minutter, som hundrede ingeniører rammer flere gange om dagen, er tusindvis af ingeniørtimer om året brugt på at vente. Forkort løkken, og du har tilføjet meningsfuld kapacitet uden at ansætte nogen. Det dominerende ROI her er det samme som i platformsudvikling (kapitel 8.4): dyr ingeniørtid omdirigeret fra ventetid og toil mod værdifuldt arbejde.

De totale ejeromkostninger er beskedne, men reelle. Du betaler for undersøgelsesværktøj og disciplinen til at køre det, for instrumentering af pipelines og for ledelsesopmærksomhed til at læse tendenser og handle på dem. Den større risiko for ROI er at gøre måling dårligt. En enkelt manipuleret måling eller et overvågningsprogram kan give negativt afkast: måneders indsats brugt på at optimere et tal, mens reelle resultater stagnerer, plus den korrosion af tillid, der gør hver fremtidig ændring sværere. Omkostningen ved slet ikke at måle er diffus og enorm: gnidning og toil akkumuleres usynligt, seniore ingeniører brænder ud på undgåeligt spild, og ledelsen kan ikke se, om investeringer hjælper. Argumentér over for ledelsen som løftestang og ærlighed: et lille, betroet, balanceret målingsprogram, der finder ud af, hvor en stor arbejdsstyrke mister tid, og betaler sig selv mange gange hjem i det øjeblik, du handler på det første fund.

## Anti-mønstre og faldgruber

- **Den enkelte produktivitetsmåling.** Ethvert enkelt tal (LOC, velocity, commits, timer) manipuleres den dag, det bliver et mål.
- **Rangordning af individer.** Ranglister og individuelle "produktivitetsscorer" ødelægger tillid og lærer folk at optimere målingen.
- **Måling som overvågning.** Finkornet individuel telemetri, der føder samtaler, nedbryder den psykologiske tryghed, effektivt arbejde har brug for.
- **Undersøgelser uden opfølgning.** At spørge udviklere, hvordan arbejdet føles, og så ikke ændre noget, lærer dem at holde op med at svare ærligt.
- **Sammenligning af teams' rå tal.** Teamkontekster er forskellige; velocity- eller DORA-sammenligninger på tværs af teams straffer ærlighed og belønner manipulation.
- **Output-teater.** At tælle producerede artefakter (dokumenter, sager, leverede features), mens reelle resultater forbliver umålt, almindeligt hvor der ikke er markedspris.
- **DORA i en præstationssamtale.** I det øjeblik leveringsmålinger scorer folk, skjuler teams hændelser og opdeler udrulninger, og signalet dør.

## Modenhedsmodel

- **Niveau 1, Opstart:** Produktivitet bedømmes ved mavefornemmelse eller en enkelt manipulerbar måling som kodelinjer, velocity eller timer. Måling er ad hoc og reaktiv, gnidning er usynlig, klager er anekdotiske, og ingen kan sige, om organisationen bliver bedre.
- **Niveau 2, Udvikling:** Nogle teams indfører grundlæggende praksis: nogle få målinger, ofte aktivitetstællinger, og den lejlighedsvise udvikleroplevelsesundersøgelse. Praksis er uens fra team til team, data indsamles, men sjældent handles der på dem, rå sammenligninger på tværs af teams sniger sig ind, og intet fælles princip beskytter individer mod rangordning.
- **Niveau 3, Standardisering:** Et balanceret målingsprogram er dokumenteret og anvendt i hele organisationen, med SPACE-lignende dimensioner, en regelmæssig DevEx-undersøgelse og DORA som leveringssignal (kapitel 11.5). Målinger aggregeres til teams efter politik, individer rangordnes aldrig, og fund driver konkret arbejde for at forkorte feedbackløkker og skære toil (kapitel 9.1).
- **Niveau 4, Styring:** Programmet måles og styres mod baselines. Feedbackløkketider, undersøgelsesscorer og DORA-tendenser bærer aftalte mål og følges over tid; hvert team sammenlignes med sin egen udvikling frem for med naboerne; platforms- og toil-reducerende investeringer begrundes med før-og-efter-data om genvundet kapacitet; og en regression i ethvert signal udløser gennemgang frem for at passere ubemærket.
- **Niveau 5, Orkestrering:** Måling er betroet, rutinemæssig og adaptiv. Opfattelses- og systemdata trianguleres, tendenser føder løbende forbedring, gnidning og kognitiv belastning jages og fjernes aktivt, selve målesættet revideres, når organisationen ændrer sig, og effektivitet integreres med forretnings- og samfundsresultater, uden at nogen måling får lov at blive et korrumperende mål.

## Idéer til drøftelse

1. Hvilke af jeres nuværende målinger kunne et kynisk team oppuste uden at gøre bedre arbejde, og hvad ville I erstatte dem med?
2. Hvis I kunne forkorte netop én feedbackløkke i hele organisationen, hvilken ville give mest genvundet kapacitet?
3. Hvordan ville I benchmarke mange teams retfærdigt, når deres kontekster er forskellige, uden at skabe en rangliste, der straffer ærlighed?
4. Hvor går grænsen mellem at måle systemet og at overvåge individet, og hvem i jeres organisation har beføjelse til at håndhæve den?
5. I en sammenhæng uden markedspris på output, såsom det offentlige eller en intern platform, hvordan måler I reel værdi frem for aktivitet?
6. Hvad ville I vise en udvikler for at bevise, at dette kvartals undersøgelse ændrede noget?

## Vigtigste pointer

- Produktivitet for ingeniører er flerdimensionel. Afvis ethvert enkelt tal (kodelinjer, velocity, commits, timer) som *den* måling, for Goodharts lov garanterer, at det vil blive manipuleret.
- Brug **SPACE-rammen** (tilfredshed og trivsel, præstation, aktivitet, kommunikation og samarbejde, effektivitet og flow) til at holde flere dimensioner sammen, så ingen enkelt dimension kan manipuleres alene.
- **Udvikleroplevelse** handler om feedbackløkker, kognitiv belastning og flow. At forkorte løkker og fjerne belastning er reel produktivitet, som aktivitetstællinger aldrig viser.
- **Triangulér** opfattelsesdata fra en DevEx-undersøgelse med systemdata fra dine værktøjer; hver korrigerer den anden.
- Behandl **DORA**-målinger som et leveringssignal på teamniveau, ikke en rangliste; deres dybde bor i kapitel 11.5 og pipelinen i kapitel 11.2.
- Mål **systemet**, aldrig individet. Aggregér til teams, hold vurdering i de særskilte menneskelige kanaler fra kapitel 1.3, og lad aldrig måling blive overvågning.
- Brug genvundet tid på at skære toil (kapitel 9.1), fremskynde kodegennemgang (kapitel 2.5) og anlægge paved roads (kapitel 8.4). Forbind effektivitet til forretningsresultater uden at lade nogen måling blive et korrumperende mål.

## Referencer og videre læsning

- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler, "The SPACE of Developer Productivity" (*ACM Queue*, 2021): the multidimensional framework.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren, and Michaela Greiler, "DevEx: What Actually Drives Productivity" (*ACM Queue*, 2023): feedback loops, cognitive load, and flow.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (the DORA metrics and their research basis).
- DORA, *Accelerate State of DevOps Report* (annual): the ongoing research programme behind the four metrics.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (toil and its elimination).
- Matthew Skelton and Manuel Pais, *Team Topologies* (cognitive load as a first-class design concern).
- Mihaly Csikszentmihalyi, *Flow: The Psychology of Optimal Experience* (the origin of flow state).
- Tom DeMarco and Timothy Lister, *Peopleware: Productive Projects and Teams* (focus, interruption, and the human side of productivity).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law; see also Marilyn Strathern's widely quoted formulation.
- U.S. Government Accountability Office (GAO) guidance on performance measurement: measuring value in non-market public-sector settings.
