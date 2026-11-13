# 7.7 Datamodellering og det semantiske lag

## Overblik og motivation

En [datamodel](https://en.wikipedia.org/wiki/Data_model) er en beslutning om, hvad jeres data betyder, truffet før I beslutter, hvor dataene bor. Den navngiver de ting, jeres forretning interesserer sig for, de attributter, der beskriver dem, og relationerne mellem dem. Lagring, indekser, filformater og forespørgselsmotorer kommer alle senere. Rækkefølgen har betydning, fordi dataenes betydning overlever enhver teknologi, I bruger til at rumme dem. Varehuse bliver erstattet, tabelformater ændrer sig, og forespørgselsmotorer kommer og går, men "kunde", "ordre" og "aktiv bruger" skal betyde det samme på tværs af dem alle, i årevis.

For et lille team er modellering ofte implicit. Én ingeniør har hele skemaet i hovedet, og en fælles forståelse af "omsætning" overlever, fordi der kun er tre mennesker til at være uenige. I skalaen hos store udviklerorganisationer, virksomheder og offentlige agenturer kollapser den uformelle tilgang på præcis den måde, der er beskrevet i kapitel 7.1 (datastrategi og datastyring). Dusinvis af teams bygger hundredvis af tabeller, hver med sin egen idé om, hvad en "session" er, eller hvornår en bruger tæller som "aktiv". To dashboards viser to forskellige tal for samme uge, og et ledelsesmøde bliver til en diskussion om, hvis forespørgsel der er rigtig, i stedet for hvad man skal gøre næste gang. Dårlig modellering varsler ikke sig selv. Den viser sig måneder senere som afstemningsarbejde, dumpede revisioner og beslutninger truffet på tal, ingen kan forsvare.

Dette kapitel handler om at gøre det arbejde bevidst. Det dækker konceptuelle, logiske og fysiske modeller; entitet-relationsmodellering; hvornår man normaliserer, og hvornår man denormaliserer; hvordan modellering adskiller sig for transaktionelle versus analytiske arbejdsbyrder; dimensionel modellering med fakta og dimensioner; og det semantiske lag, der rummer den ene styrede definition af hver forretningsmåling. Udbyttet er ikke elegance for elegancens skyld. Det er, at "aktiv bruger" og "omsætning" betyder én ting overalt, så jeres teams kan stole på tallene og bevæge sig hurtigere på grund af det.

*Se også:* kapitel 3.4 (dataarkitektur og lagring), kapitel 7.3 (analyse og business intelligence) og kapitel 11.5 (nøgleindikatorer).

## Grundprincipper

- Afgør, hvad data betyder, før I afgør, hvor de bor.
- Model på tre niveauer: konceptuelt (forretning), logisk (struktur), fysisk (implementering).
- Normalisér for at beskytte korrekthed i transaktionelle systemer; denormalisér bevidst for analytisk hastighed.
- Afstem modellen med arbejdsbyrden: transaktioner og analyse har modsatte behov.
- Hver forretningsmåling har præcis én styret definition, og den bor i det semantiske lag.
- Konformerede dimensioner lader uafhængige teams joine og sammenligne data sikkert.
- Granularitet er en designbeslutning, I træffer med vilje, ikke et tilfælde i en forespørgsel.
- Modeller er levende aktiver: navngiv dem godt, dokumentér dem, og hold dem udviklingsegnede.

## Anbefalinger

### Model på tre niveauer, i rækkefølge

Arbejd fra betydningen og udad. Begynd med en konceptuel model: de entiteter, jeres forretning interesserer sig for, og hvordan de hænger sammen, skrevet i almindeligt sprog, en domæneekspert kan tjekke. "En kunde afgiver mange ordrer; en ordre indeholder mange ordrelinjer; hver ordrelinje henviser til ét produkt." Ingen nøgler, ingen typer, ingen tabeller endnu. Byg så en logisk model, der tilføjer struktur: attributter, primære og fremmednøgler, kardinaliteter og begrænsninger, stadig uafhængigt af en bestemt database. [Entitet-relationsmodellering](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) er standardnotationen her, og et entitet-relationsdiagram er det artefakt, I gennemgår med både ingeniører og forretningsinteressenter. Først derefter producerer I den fysiske model: de faktiske tabeller, kolonner, datatyper, indekser, partitioner og lagerlayout for jeres valgte motor. At springe til fysisk design er den almindeligste modelleringsfejl, fordi det bager nutidens teknologivalg ind i beslutninger, der burde overleve dem.

### Normalisér transaktionelle systemer, denormalisér analytiske med vilje

For systemer, der registrerer transaktioner, så foretræk [databasenormalisering](https://en.wikipedia.org/wiki/Database_normalization). Normalformer fjerner redundans, så hvert faktum lagres én gang, hvilket forhindrer opdateringsanomalier og holder skrivninger korrekte, når mange brugere ændrer data samtidigt. Det er den rette standard for [online transaktionsbehandling](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), hvor korrekthed under samtidige skrivninger betyder mere end hastigheden af en enkelt analytisk forespørgsel. Analytiske systemer har modsatte prioriteter. De er læsetunge, de scanner og aggregerer enorme intervaller, og at joine dusinvis af normaliserede tabeller ved forespørgselstidspunktet er langsomt og svært at ræsonnere om. Der denormaliserer I med vilje og slår beslægtede attributter sammen, så forespørgsler bliver enklere og hurtigere. Disciplinen er at denormalisere bevidst, med en dokumenteret grund, frem for at lade redundans snige sig ind ved et tilfælde. Kapitel 3.4 (dataarkitektur og lagring) dækker de motorer, der får hvert mønster til at yde.

### Brug dimensionel modellering til analyse

Til analytiske arbejdsbyrder så adoptér [dimensionel modellering](https://en.wikipedia.org/wiki/Dimensional_modeling), tilgangen populariseret af Ralph Kimball. I deler verden i fakta og dimensioner. En faktatabel rummer målingerne af en forretningsproces: beløbet på et salg, varigheden af et opkald, den afsendte mængde. Dimensionstabeller rummer den beskrivende kontekst, I filtrerer og grupperer efter: kunden, produktet, butikken, datoen. Arrangér én faktatabel omgivet af dens dimensioner, og I har et [stjerneskema](https://en.wikipedia.org/wiki/Star_schema), som er let for analytikere at forstå og hurtigt for motorer at forespørge. Normalisér de dimensioner ud i undertabeller, og I får et snefnugsskema, som sparer noget lagerplads på bekostning af flere joins og mere kompleksitet; foretræk stjernen, medmindre I har en konkret grund. For meget store, stærkt regulerede miljøer, hvor revisionsbarhed og kildesporing dominerer, modellerer en data vault-tilgang hubs, links og satellitter for at indfange historik og afstamning aggressivt, på bekostning af flere tabeller og en stejlere indlæringskurve. De fleste teams bør begynde med stjerner i Kimball-stil og først række efter data vault, når revisionskravene retfærdiggør det.

### Fastlæg granulariteten, og håndtér skiftende dimensioner eksplicit

Før I tilføjer en eneste kolonne til en faktatabel, så angiv dens granularitet: præcis hvad én række repræsenterer. "Én række pr. ordrelinje." "Én række pr. bruger pr. dag." Granularitet er fundamentet for en korrekt model, fordi hver måling og hver dimension enten passer til den granularitet eller ikke hører hjemme i tabellen. At blande granulariteter er, hvordan I får dobbelttalt omsætning. Afgør så, hvordan dimensioner ændrer sig over tid. En kunde flytter til en ny by; overskriver I den gamle værdi, beholder I fuld historik, eller sporer I kun den nuværende og forrige værdi? Det er de gængse [langsomt skiftende dimension](https://en.wikipedia.org/wiki/Slowly_changing_dimension)-mønstre, og at vælge forkert betyder, at jeres historiske rapporter stille omskriver fortiden. Afgør granularitet og ændringsstrategi på forhånd, skriv dem ind i modellens dokumentation, og hold linjen i gennemgang.

### Byg ét semantisk lag som den enkelte definition af hver måling

Det er den anbefaling, der betaler for hele kapitlet. Et [semantisk lag](https://en.wikipedia.org/wiki/Semantic_layer) sidder mellem jeres fysiske tabeller og hvert værktøj, der forbruger dem, og det rummer den ene styrede definition af hver forretningsmåling. "Aktiv bruger" defineres én gang, som kode, med dens præcise logik: hvilke hændelser der tæller, over hvilket vindue, med udelukkelse af hvilke interne konti. "Omsætning" defineres én gang, inklusive hvordan refusioner, rabatter og valutaomregning håndteres. Hvert dashboard, hver notebook, hver rapport og hvert reverse-ETL-job læser den definition i stedet for at genimplementere den i en skræddersyet forespørgsel. Når definitionen ændres, ændres den ét sted, og hver forbruger opdateres samtidigt. Det er mekanismen, der gør styrede målingsdefinitioner reelle frem for ambitiøse, og det er den direkte implementering af det, kapitel 11.5 (nøgleindikatorer) beder om. Behandl målingsdefinitioner som versioneret kode med ejere, gennemgang og tests, præcis som kapitel 7.1 beder jer behandle data som et produkt.

### Etablér konventioner, navngivning og dokumentation

Ensartethed er en funktion. Adoptér navngivningskonventioner og håndhæv dem: en konvention for tabelnavne, en konvention for nøgler, en standard for datokolonner, en regel for, hvordan I markerer et faktum versus en dimension. Afgør én gang, om I bruger ental eller flertal i entitetsnavne, og bland dem aldrig. Dokumentér hver model, hvor de mennesker, der bruger den, vil lede: betydningen af hver tabel, granulariteten af hvert faktum, definitionen af hver måling og ejeren af hver. God navngivning og dokumentation er, hvad lader en ny analytiker selvbetjene sig i stedet for at afbryde teamet, og det er, hvad lader en revisor spore et tal fra et bestyrelsesdæk tilbage til dets kilde uden en guidet rundvisning.

### Hold modeller udviklingsegnede

Jeres model vil ændre sig, så design for forandring. Tilføj kolonner frem for at omdanne eksisterende. Brug surrogatnøgler, så en ændring i et kildesystems naturlige nøgle ikke forplanter sig gennem jeres varehus. Versionér målingsdefinitioner, og udfas dem med varsel i stedet for tavst at ændre dem under kørende dashboards. Hold transformationer i versionsstyring, testede og gennemgåede, så en ændring af, hvad "aktiv bruger" betyder, er en pull request med en diff og en godkender, ikke en stille redigering i et BI-værktøj. En model, I ikke sikkert kan udvikle, bliver en model, folk går udenom, og skyggedefinitioner er, hvordan den enkelte sandhedskilde dør.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper | Bedst egnet |
|---|---|---|---|
| Normaliseret (3NF) | Korrekte skrivninger, ingen redundans, fleksibel | Langsomme analytiske joins, komplekse forespørgsler | OLTP og operationelle systemer |
| Stjerneskema (Kimball) | Hurtigt, intuitivt, analytikervenligt | Noget redundans, ETL at vedligeholde | Det meste analyse og BI |
| Snefnugsskema | Mindre lagerplads, renere dimensioner | Flere joins, mere kompleksitet | Store, tæt styrede dimensioner |
| Data vault | Fuld historik, revisionsbart, agile indlæsninger | Mange tabeller, stejl indlæringskurve | Stærkt regulerede, revisionstunge |
| Semantisk lag over modeller | Én definition overalt, værktøjsuafhængigt | Opbygning på forhånd, kræver ejerskab | Organisationer med mange teams og værktøjer |

Den centrale spænding er hastigheden af en enkelt forespørgsel mod korrekthed og fleksibilitet på tværs af hele ejendommen. Normalisering beskytter korrekthed og betaler for det i forespørgselskompleksitet; dimensionelle modeller køber forespørgselshastighed og klarhed og betaler for det med ETL og noget styret redundans. Der er ingen universel vinder, hvilket er grunden til, at I afstemmer modellen med arbejdsbyrden frem for at vælge en favorit. Det semantiske lag løser den anden spænding, mellem mange teams og mange værktøjer, ved at gøre målingsdefinitionen uafhængig af hvert enkelt af dem. Fejlen er at behandle disse som ideologiske lejre. En sund organisation kører normaliserede OLTP-systemer, dimensionelle analytiske modeller fodret fra dem og ét semantisk lag ovenpå, hver gør det job, den er god til.

## Spørgsmål til drøftelse med dit team

1. **Når to dashboards viser forskellige tal for samme måling, hvis definition vinder, og hvor bor den definition fysisk?** Dette spørgsmål afslører, om I faktisk har en enkelt sandhedskilde eller blot tror, I har. I de fleste store teams er det ærlige svar, at "aktiv bruger" er omdefineret i et dusin forskellige forespørgsler, og vinderen er den, der skændes højest i mødet. Tag reel dokumentation med: vælg én måling, find hvert sted, den beregnes, og sammenlign logikken linje for linje. I vil næsten sikkert finde tavse uenigheder om vinduer, udelukkelser og grænsetilfælde. Svaret bør drive en beslutning om at bygge et semantisk lag, hvor hver måling defineres én gang, som gennemgået kode, så spørgsmålet holder op med at handle om mennesker og begynder at handle om et versioneret artefakt. Indtil den definition har ét fysisk hjem, er hver afstemning midlertidig.

2. **Hvad er granulariteten af jeres vigtigste faktatabel, og kan alle i rummet angive den på samme måde?** Granularitet er det stille fundament, de fleste modelleringsfejl kan spores tilbage til. Hvis halvdelen af teamet siger "én række pr. ordre" og den anden halvdel "én række pr. ordrelinje", har I en dobbelttællingsfejl, der venter på at dukke op i en omsætningsrapport. Tag den faktiske tabel med og bed hver person beskrive én række i en enkelt sætning. Uenighed her er ikke et kommunikationsproblem at glatte ud; det er en designfejl at rette, før flere målinger hobes oven på den. Svaret bør skrives ind i modellens dokumentation og håndhæves i gennemgang, for når analytikere først bygger forespørgsler på en tvetydig granularitet, spreder tvetydigheden sig hurtigere, end I kan rette den.

3. **Hvordan vil denne model absorbere forandring, og hvad sker der med sidste års rapporter, når en definition skifter?** Hver model møder skiftende kildesystemer, skiftende forretningsregler og skiftende målingsdefinitioner, så det reelle spørgsmål er, om forandring er en kontrolleret pull request eller en tavs redigering, der omskriver historikken. Tag et nyligt eksempel med: en måling, hvis definition ændrede sig, eller en kildenøgle, der blev omdøbt, og spor, hvad der skete med eksisterende dashboards. Hvis en langsomt skiftende dimension blev håndteret ved overskrivning, kan jeres historiske rapporter stille have ændret deres tidligere værdier, hvilket er et alvorligt problem for enhver, der laver tendensanalyse eller regulatorisk rapportering. Svaret bør skubbe jer mod surrogatnøgler, versionerede målingsdefinitioner, eksplicitte ændringsstrategier og transformationer holdt i versionsstyring med gennemgang. En model, ingen sikkert kan ændre, bliver en model, folk opgiver.

4. **Hvilke dimensioner skal betyde det samme på tværs af hvert team, og hvem er ansvarlig for at eje hver enkelt?** Konformerede dimensioner er, hvad lader marketing, økonomi og drift joine deres data og få sammenlignelige svar, men kun når "kunde", "produkt", "region" og "dato" bærer én aftalt definition i stedet for en privat kopi pr. team. Det modstridende træk er autonomi: hvert team vil modellere sin egen verden i sit eget tempo, og at gennemtvinge en fælles dimension sinker dem på kort sigt, mens det betaler sig på tværs af ejendommen. Tag de to eller tre dimensioner, der optræder i flest tværgående rapporter, med, list hver version af hver, der findes i dag, og se, hvor langt deres nøgler og attributter faktisk divergerer. Navngiv en ejer for hver konformeret dimension, for en fælles dimension uden ejer driver tilbage til private kopier inden for et kvartal. I virksomheds- og offentlige sammenhænge, hvor et tal fra én afdeling sammenlignes med et fra en anden offentligt, er en ukonformeret dimension forskellen mellem en ærlig sammenligning og en tilfældig usandhed, så afgør tidligt, hvilke dimensioner der styres centralt, og hvilke der forbliver lokale.

5. **Hvor ligger grænsen mellem jeres normaliserede transaktionelle systemer og jeres denormaliserede analytiske modeller, og er hver denormalisering en bevidst beslutning?** At afstemme modellen med arbejdsbyrden er kernedisciplinen, men grænsen er netop, hvor det udviskes: en analytiker denormaliserer en varehustabel for hastighed, en ingeniør normaliserer en rapporteringstabel af vane, og ingen skrev ned, hvilken side hvert valg hører til. Spændingen er hastigheden af en enkelt forespørgsel mod korrekthed og fleksibilitet på tværs af alt, og fornuftige mennesker lander forskelligt afhængigt af, om de ejer skrivninger eller læsninger. Tag jeres langsomste analytiske forespørgsel og jeres mest omstridte transaktionelle tabel med, og spørg for hver redundant kolonne, om dens redundans blev valgt med en dokumenteret grund eller sneg sig ind ved et tilfælde. Målet er en skrevet regel for, hvornår denormalisering er tilladt, og hvem der godkender, ikke en renhedskonkurrence. For store eller regulerede organisationer afgør denne grænse også, hvor personoplysninger duplikeres, så en udokumenteret denormalisering er både et ydelsesspørgsmål og en datastyringseksponering, nogen til sidst skal forklare for en revisor.

6. **Skal I bygge eller købe det semantiske lag, og hvem er ansvarlig for at holde hver målingsdefinition ajour, når det først findes?** Et semantisk lag leverer kun en enkelt sandhedskilde, når det ejes og vedligeholdes, så valget af værktøj betyder mindre end svaret på, hvem der gennemgår en ændring af, hvad "omsætning" betyder, og hvem der hænger på den, når en definition bliver forældet. De modstridende hensyn er reelle: at bygge giver jer kontrol og passer til jeres stak, men tilføjer en ingeniørbyrde, mens at købe et målingsværktøj er hurtigere, men risikerer indlåsning og et definitionssprog, I ikke fuldt kontrollerer. Tag jeres håndfuld højindsatsmålinger, de værktøjer der forbruger dem i dag, og en ærlig vurdering af, om nogen i øjeblikket ejer de definitioner, eller de blot eksisterer, med. Afgør på forhånd, om definitioner bor som versioneret kode med navngivne ejere og tests, for et semantisk lag, ingen vedligeholder, rådner til de samme spredte definitioner, det skulle erstatte. I virksomheds- og offentlig rapportering, hvor en måling på et offentligt dashboard skal kunne spores til en dokumenteret, gennemgået definition, er det det ejerskab og evnen til at bevise et tals afstamning, der forvandler det semantiske lag fra en bekvemmelighed til en revisionsbar kontrol.

## Sektorperspektiv

**Startup.** Modellering kan vente, men definitioner kan ikke. Med to ingeniører og ingen runway til at bygge et varehus så læg ét lille semantisk lag i jeres transformationsværktøj og definér de to eller tre målinger, jeres bestyrelse faktisk følger, "aktiv bruger" og "omsætning", én gang som testet kode. Spring data vault og omstændelige dimensionelle skemaer over; en tynd stjerne og en håndfuld styrede definitioner køber jer ensartede tal uden at sinke leverancen. Udbyttet er, at bestyrelsesforberedelse holder op med at være en diskussion om, hvis forespørgsel der er rigtig.

**Lille virksomhed.** I har ingen datamodellør og intet budget til en målingsplatform, så støt jer til de definitioner, der er indbygget i de værktøjer, I allerede kører, og skriv de få, der betyder noget, ned i ét fælles dokument, alle læser. Foretræk at købe analyse indlejret i jeres eksisterende software frem for at rejse et varehus, I ikke kan bemande. Hvor I modellerer, så hold det enkelt og navngiv ting ensartet, for den, der vedligeholder det næste år, kan være den, der ikke kan huske, hvorfor "kunde" betød to ting. Ensartethed er billigere end afstemning.

**Stor virksomhed.** Problemet er mange teams og mange værktøjer, der driver ind i private definitioner, så invester i konformerede dimensioner, ét styret semantisk lag og målingsdefinitioner holdt som versioneret kode med ejere og gennemgang. Standardisér navngivning, granularitetserklæringer og strategier for langsomt skiftende dimensioner på tværs af ejendommen, så et tal i ét værktøj matcher det samme tal i et andet. Behandl det semantiske lag som et produkt med en køreplan og et ejende team, og mål, hvor meget afstemningstid det fjerner. Afkastet er betroede tal på tværs af forretningen og revisioner, der sporer rent fra et bestyrelsesdæk tilbage til kilden.

**Offentlig sektor.** Åbenhed og sammenlignelighed på tværs af agenturer former arbejdet: kanoniske referencedata for geografi og demografi, styrede definitioner af kerneindikatorer og offentliggjort metodologi med versionerede udgivelser, så offentligheden kan spore ethvert tal tilbage til en dokumenteret definition. Indkøbsregler kan kræve, at jeres modeller og definitioner forbliver portable og leverandørneutrale, så undgå et semantisk lag låst til ét proprietært værktøj. Hold individuelle agenturer frie til at modellere deres operationelle data, mens de konformerer til fælles dimensioner for alt, der rapporteres nationalt. En offentliggjort indikator, der ikke kan spores til en versioneret definition, er lige så meget en ansvarlighedsfejl som en datafejl.

## Eksempler

**Startup.** Et Series A-selskab havde tre definitioner af "aktiv bruger" boende tre steder: produktanalyseværktøjet, økonomiregnearket og investordækket. Tallene stemte aldrig, og hver bestyrelsesforberedelse blev til en hektisk jagt. To ingeniører indførte et lille semantisk lag i deres transformationsværktøj og definerede "aktiv bruger" og "månedlig tilbagevendende omsætning" én gang som testet kode, med de præcise vinduer og udelukkelser skrevet ned. Hvert dashboard læser nu de definitioner. Diskussionen ved bestyrelsesforberedelsen forsvandt, og onboarding af en ny analytiker gik fra en uge med stammeviden til at læse én dokumenteret model. Det hænger direkte sammen med disciplinen beskrevet i kapitel 7.4 (produktanalyse og eksperimenter), hvor en stabil definition af "aktiv" er, hvad gør eksperimentresultater sammenlignelige.

**Stor virksomhed.** En global detailhandler kørte fem business intelligence-værktøjer på tværs af marketing, økonomi, forsyningskæde, varesortiment og butikker, og hvert havde genopfundet "bruttomargen" en smule forskelligt. De byggede ét semantisk lag oven på et varehus i Kimball-stil med konformerede dimensioner, så "produkt", "butik" og "dato" betød det samme på tværs af hver faktatabel og hvert værktøj. Hver måling blev defineret én gang og forbrugt overalt. Afstemningsmøder, der plejede at æde dage pr. kvartal, forsvandt for det meste, og da økonomi ændrede, hvordan returvarer påvirkede marginen, forplantede ændringen sig til alle fem værktøjer på én gang. De konformerede dimensioner var, hvad lod uafhængige teams joine deres data med tillid i stedet for mistænksomhed.

**Offentlig sektor.** En national regering havde brug for sammenlignelig rapportering på tværs af sundheds-, arbejdsmarkeds- og uddannelsesagenturer, som hver historisk definerede "husstand", "region" og "beskæftigelse" på sin egen måde. Et tværgående organ etablerede fælles referencedata og standarddefinitioner: kanoniske dimensionstabeller for geografi og demografi og styrede definitioner af kerneindikatorer, offentliggjort med metodologi og versionerede udgivelser. Individuelle agenturer modellerer deres egne operationelle data, men konformerer til de fælles dimensioner og definitioner for alt, der rapporteres nationalt. Resultatet er, at et tal fra ét agentur ærligt kan sammenlignes med et andet, og offentligheden kan spore enhver offentliggjort indikator tilbage til en dokumenteret definition, hvilket understøtter de åbenhedsforpligtelser, der dækkes i kapitel 7.1.

## Business case: motivation, ROI og TCO

Afkastet af god modellering og et semantisk lag er mest genvundet tid og undgået fejl. I mange organisationer bruger analytikere størstedelen af deres tid på at finde data, afstemme modstridende tal og genopbygge definitioner, andre allerede har skrevet. En enkelt styret definition af hver måling forvandler det gentagne arbejde til en engangsinvestering. Den fjerner også en hel kategori af dyr fiasko: det forkerte tal i et bestyrelsesdæk, det fejlrapporterede tal, der udløser et revisionsfund, det kvartallange afstemningsprojekt, der kun eksisterer, fordi to teams definerede "omsætning" forskelligt. Når definitionen bor ét gennemgået sted, holder de fiaskoer stort set op med at ske.

Omkostningen er reel og værd at nævne. I investerer på forhånd i konceptuel og logisk modellering, i at bygge og fylde det semantiske lag og i det løbende ejerskab, der holder definitioner ajour. Samlet ejeromkostning (TCO) omfatter værktøjet, modellerings- og analyseingeniørtiden og den styring, der holder modellen fra at drive. Vej det mod omkostningen ved ikke at gøre det, som er større, men skjult: den viser sig som duplikerede pipelines, analytikere som menneskelige afstemningsmotorer og ledere, der træffer selvsikre beslutninger på tal, ingen kan forsvare. Fremlæg sagen for ledelsen på deres vilkår. Én betroet definition af hver måling er, hvad lader dem sammenligne på tværs af forretningen, stole på dashboards og svare tilsyn uden en brandøvelse. Begynd, hvor afstemningssmerten er værst, definér de få målinger én gang, og lad den genvundne tid finansiere resten.

## Anti-mønstre og faldgruber

- At hoppe direkte til fysiske tabeller og bage nutidens teknologi ind i beslutninger, der burde overleve den.
- At definere den samme måling uafhængigt i hvert dashboard, så ikke to tal stemmer.
- At lade granularitet stå uangivet og så opdage dobbelttalte målinger i en omsætningsrapport.
- At denormalisere analytiske tabeller ved et tilfælde i stedet for ved dokumenteret beslutning.
- At normalisere et analytisk varehus, til hver forespørgsel er et tolv-tabellers join, ingen forstår.
- At håndtere langsomt skiftende dimensioner ved overskrivning, så historiske rapporter tavst omskriver fortiden.
- At bruge naturlige nøgler overalt, så en kildesystemnøgleændring forplanter sig gennem hele varehuset.
- At bygge et semantisk lag uden ejer, så definitioner driver og tilliden eroderer.
- At behandle modellen som færdig ved lancering i stedet for et levende aktiv, der skal forblive udviklingsegnet.

## Modenhedsmodel

- **Niveau 1, Opstart:** Modellering er implicit og reaktiv. Tabeller designes fysisk-først af den, der har brug for dem. Målinger omdefineres i hver rapport, og tal er rutinemæssigt i konflikt. Granularitet er udokumenteret, og ingen ejer definitionerne.
- **Niveau 2, Udvikling:** Nogle analytiske tabeller følger et dimensionelt mønster, og nogle få nøglemålinger har skrevne definitioner, men de bor i en wiki og håndhæves ikke. Navngivningskonventioner findes på papiret. Praksis varierer fra team til team, og afstemning er stadig hyppig og manuel.
- **Niveau 3, Standardisering:** Konceptuelle, logiske og fysiske modeller er adskilte og gennemgåede. Et semantisk lag definerer kernemålinger én gang, som versioneret kode med ejere. Konformerede dimensioner lader teams joine sikkert. Granularitet og strategier for langsomt skiftende dimensioner er dokumenteret og håndhævet i gennemgang på tværs af organisationen.
- **Niveau 4, Styring:** Modelejendommen måles mod baselines. I følger dækningen af målingsdefinitioner (andelen af rapporterede målinger betjent af det semantiske lag), antallet af duplikerede eller skyggedefinitioner stadig i brug, afstemningstimer brugt pr. kvartal og raten af granularitets- og afstamningsfejl fanget i gennemgang versus i produktion. Definitionsændringer flyder gennem gennemgåede pull requests med tests, og friskhed, testbestå-rater og drift overvåges på dashboards. Når en måling divergerer, eller en dimension holder op med at konformere, bringer målingen det frem, før et bestyrelsesmøde gør.
- **Niveau 5, Orkestrering:** Hver vigtig måling har én styret definition forbrugt af alle værktøjer og teams, og det semantiske lag er integreret med analyse, eksperimentering og regulatorisk rapportering. Modeller er udviklingsegnede ved design og løbende forfinede; definitioner er betroede i hele organisationen; afstemningsarbejde er stort set forsvundet. Organisationen udfaser, omafgrænser og konformerer rutinemæssigt nye dimensioner, efterhånden som forretningen ændrer sig, og rebalancerer modelejendommen som et adaptivt aktiv.

## Idéer til drøftelse

1. Vælg jeres tre vigtigste målinger. Hvor mange forskellige definitioner af hver findes på tværs af jeres værktøjer i dag, og hvad skulle der til for at samle dem til én?
2. Hvor har en uangivet granularitet forårsaget en reel rapporteringsfejl, og hvor lang tid tog det at opdage?
3. Hvilke af jeres dimensioner bør konformeres på tværs af teams først, og hvem ejer dem?
4. Er jeres målingsdefinitioner i versionsstyring med gennemgang, eller kan de redigeres tavst inde i et BI-værktøj?
5. Hvornår omskrev en langsomt skiftende dimension sidst jeres historik uden at nogen opdagede det, og hvordan ville I fange det næste gang?
6. Hvis I erstattede jeres varehusmotor i morgen, hvor meget af jeres models betydning ville overleve flytningen?

## Vigtigste pointer

- Datamodellering er at afgøre, hvad data betyder, og den betydning overlever enhver lagringsteknologi, I vælger.
- Model på tre niveauer i rækkefølge: konceptuelt, så logisk, så fysisk.
- Normalisér transaktionelle systemer for korrekthed; denormalisér analytiske bevidst for hastighed.
- Brug dimensionel modellering med fakta, dimensioner og en angivet granularitet til analyse.
- Byg ét semantisk lag, så hver forretningsmåling har en enkelt styret definition overalt.
- Konformerede dimensioner lader uafhængige teams joine og sammenligne deres data med tillid.
- Navngiv godt, dokumentér, brug surrogatnøgler, og versionér definitioner, så modellen forbliver udviklingsegnet.

## Referencer og videre læsning

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modelling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
