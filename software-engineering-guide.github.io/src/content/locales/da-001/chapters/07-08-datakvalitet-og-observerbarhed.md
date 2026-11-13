# 7.8 Datakvalitet og observerbarhed

## Overblik og motivation

[Datakvalitet](https://en.wikipedia.org/wiki/Data_quality) er egnethed til brug: i hvilken grad data tjener de beslutninger, produkter og rapporter, der afhænger af dem. Et datasæt er ikke godt eller dårligt i abstrakt forstand. Det er godt nok til et formål, eller det er ikke. En kundeadresse, der er fin til en marketingopgørelse, kan være uegnet til en juridisk meddelelse. Den ramme har betydning, fordi den flytter samtalen fra "er vores data perfekte" (aldrig) til "er vores data egnede til det, vi er ved at bruge dem til" (kan besvares og testes). De klassiske dimensioner er nøjagtighed, fuldstændighed, konsistens, rettidighed, validitet og unikhed, og de fleste reelle problemer kan føres tilbage til en af dem.

Her er den ubehagelige sandhed for store teams: dårlige data er værre end ingen data. Når I ikke har data, ved I det og går frem med passende forsigtighed. Når I har forkerte data, der ser rigtige ud, handler I på dem med falsk selvsikkerhed. Dårlige data korrumperer tavst. De flyder ind i et dashboard, en leder stoler på, ind i en [maskinlæringsmodel](https://en.wikipedia.org/wiki/Machine_learning), der træner på dem og koder deres fejl ind, og ind i beslutninger, ingen tænker på at sætte spørgsmålstegn ved, fordi tallet stod lige der på skærmen. Skaden er diffus og forsinket, hvilket netop er grunden til, at den er dyr. Når nogen opdager det, er det forkerte tal blevet citeret i et bestyrelsesdæk, en regulatorisk indberetning eller en offentlig statistik.

Dataobserverbarhed er den disciplin, der fanger det, før jeres forbrugere gør. Den er den direkte parallel til softwareobserverbarhed og telemetri (kapitel 9.2): den samme instinkt, der får jer til at overvåge forespørgselslatens og fejlrater, får jer til at overvåge datafriskhed, volumen, skema og fordeling. Dette kapitel bygger på datastrategi og datastyring (kapitel 7.1) og datateknik (kapitel 7.2), og det fodrer datamodellering og det semantiske lag (kapitel 7.7) og ansvarlig og troværdig AI (kapitel 6.5). For virksomheder, der afstemmer mange kildesystemer, og for regeringer, der offentliggør lovbestemt statistik, er det at behandle datapålidelighed som et ingeniørproblem med ejere og servicenivåer forskellen mellem tillid og en meget offentlig berigtigelse.

## Grundprincipper

- Datakvalitet er egnethed til brug, ikke perfektion; definér den mod formålet.
- Dårlige data er værre end ingen data, fordi de tavst korrumperer beslutninger.
- Test data, som I tester kode: assertions, forventninger og skematjek i pipelinen.
- Kontrakter mellem producenter og forbrugere gør forventninger eksplicitte og håndhævelige.
- Observér friskhed, volumen, skema og fordeling på samme måde, som I observerer tjenester.
- Afstamning forvandler "noget er galt" til "her er, hvad der gik i stykker, og hvad det berører."
- Behandl datahændelser som produktionshændelser, med ejerskab, alvorlighed og servicenivåer.
- Opdag problemer, hvor de kommer ind, ikke tre lag nedstrøms i et dashboard.

## Anbefalinger

### Definér kvalitet efter dimension, og mål den

Vage kvalitetsmål giver vage resultater. Del kvalitet op i målbare dimensioner, og knyt konkrete tjek til hver. Nøjagtighed spørger, om værdier afspejler virkeligheden (matcher denne registrerede omsætning kildens hovedbog). Fuldstændighed spørger, om forventede poster og felter er til stede (mangler der dage, er krævede kolonner null). Konsistens spørger, om det samme faktum stemmer på tværs af systemer (matcher kundeantallet i økonomi antallet i varehuset). Rettidighed spørger, om data ankommer i tide til at være nyttige (er gårsdagens data klar før morgenrapporten). Validitet spørger, om værdier overholder regler og formater (er alle valutakoder ægte, er datoer inden for intervallet). Unikhed spørger, om entiteter optræder én gang (er der duplikerede ordrer, der puster totalen op). Vælg de dimensioner, der betyder noget for hvert datasæt, sæt tærskler, og følg dem over tid. Kvalitet, I ikke måler, er kvalitet, I gætter på.

### Test pipelines med assertions og forventninger

Data fortjener den samme teststringens som applikationskode. Brug [datavalidering](https://en.wikipedia.org/wiki/Data_validation) på hvert trin: assertionsbaserede tests, der fejler pipelinen, når en invariant brydes, og forventningsbaserede tests, der erklærer, hvordan "normalt" ser ud for en tabel, og flagger afvigelser. Hævd, at primærnøgler er unikke og ikke-null, at fremmednøgler kan opløses, at kategoriske kolonner kun indeholder accepterede værdier, at numeriske kolonner ligger inden for plausible intervaller, og at rækkeantal lander i et forventet bånd. Tilføj skematjek, der fejler højlydt, når en kolonne tilføjes, droppes, omdøbes eller omtypes opstrøms. Kør disse tjek i kontinuerlig integration, så en dårlig transformation fanges før merge, og kør dem igen i produktion mod levende data, så en dårlig kilde fanges, før den når forbrugere. Målet er at fejle tidligt og højlydt, fordi en ødelagt pipeline er sikrere end en tavst forkert.

### Etablér datakontrakter mellem producenter og forbrugere

De fleste datakvalitetshændelser starter opstrøms, når et producerende team ændrer et skema, en semantisk betydning eller en værdikonvention uden at vide, hvem der afhænger af den. En [datakontrakt](https://en.wikipedia.org/wiki/Data_contract) løser det ved at gøre grænsefladen eksplicit: skemaet, semantikken i hvert felt, tilladte værdier, friskhedsgarantier og processen for at lave en ændring. Producenten forpligter sig til kontrakten, forbrugeren bygger mod den, og en brydende ændring kræver versionering og varsel frem for en tavs overraskelse mandag. Håndhæv kontrakter mekanisk, hvor I kan, ved at validere indkommende data mod kontrakten ved grænsen og afvise eller sætte overtrædelser i karantæne. Kontrakter forvandler en implicit, skrøbelig afhængighed til en eksplicit, forhandlet en. De gør også ejerskab synligt, hvilket er halvdelen af kampen i skala.

### Overvåg de fire signaler i dataobserverbarhed

Dataobserverbarhed iagttager fire signaler, i direkte parallel til hvordan I iagttager en kørende tjeneste (kapitel 9.2). Friskhed: er dataene så nylige, som de bør være, eller er pipelinen gået i stå. Volumen: ligger rækkeantallet i det forventede interval, eller ankom en tabel halvtom eller dobbeltindlæst. Skema: er strukturen ændret uventet. Fordeling: er selve værdierne drevet, så en kolonne, der var 2 procent null, pludselig er 40 procent null, eller et gennemsnit har forskudt sig på en måde, der signalerer en opstrøms fejl. Instrumentér disse signaler på jeres vigtige tabeller, lær deres normale mønstre, og alarmér ved brud. Sådan erstatter I "en leder lagde mærke til, at dashboardet så forkert ud" med "det ejende team blev kaldt ud på fejlstedet." Den værst tænkelige detektor af et dataproblem er et menneske nedstrøms, der stoler på tallet.

### Tilføj anomalidetektion, men justér den mod alarmtræthed

Statiske tærskler fanger de åbenlyse fejl. Til subtilere drift så læg [anomalidetektion](https://en.wikipedia.org/wiki/Anomaly_detection) ovenpå, der lærer hver målings normale sæsonmønster og flagger statistisk usædvanlige afvigelser, så I fanger en langsom lækage, før den bliver en oversvømmelse. Vær disciplinerede omkring det. Støjende anomalialarmer træner folk til at ignorere alarmer, hvilket er værre end ingen alarmer. Begynd med jeres mest værdifulde tabeller, alarmér kun på ting, et menneske bør handle på, rut hver alarm til en navngiven ejer, og justér ubarmhjertigt. En alarm, ingen handler på, er en fejl i jeres overvågning, ikke en funktion.

### Spor afstamning til konsekvensanalyse og rodårsag

Når noget går i stykker, betyder to spørgsmål noget med det samme: hvad forårsagede det, og hvad påvirker det. [Dataafstamning](https://en.wikipedia.org/wiki/Data_lineage) besvarer begge ved at kortlægge, hvordan data flyder fra kilden gennem hver transformation til hver nedstrøms tabel, hvert dashboard og hver model. Til rodårsag sporer I et dårligt tal opstrøms til den transformation eller kilde, der indførte det. Til konsekvensanalyse sporer I fremad for at se hver forbruger, en dårlig indlæsning har berørt, så I kan underrette dem og sætte skaden i karantæne, før den spreder sig. Indfang afstamning automatisk fra jeres transformations- og orkestreringsværktøjer frem for at vedligeholde et diagram i hånden, fordi et håndtegnet diagram er forkert dagen efter, I tegner det. I virksomheder med mange kilder så offentliggør afstamning i et datakatalog, så enhver forbruger kan se, hvor et felt kom fra, og stole på det derefter.

### Behandl datahændelser som produktionshændelser

De praksisser, der holder tjenester pålidelige, gælder direkte for data. Giv hvert vigtigt datasæt en ejer. Definér alvorlighedsniveauer for "datanedetid", de perioder hvor data mangler, er forkerte eller sene. Sæt servicenivåer: friskhedsmål, et acceptabelt fejlbudget og en måltid til at opdage og løse. Læg data-vagtrotationer bag de mest kritiske pipelines, skriv runbooks, og kør skyldfrie postmortems efter hændelser, så den samme fejl ikke gentager sig. Når en betalingstabel er forsinket, eller en offentlig måling er forkert, er det en hændelse, og den fortjener samme alvor som et udfald. Det er det kulturelle skifte, der får alt værktøjet til at betale sig.

### Profilér og afstem kontinuerligt

Profilering betyder rutinemæssigt at undersøge formen af jeres data: værdifordelinger, null-rater, kardinalitet, min og max samt formatmønstre. Det bringer problemer frem, I ikke tænkte på at hævde, og det fortæller jer, hvordan "normalt" ser ud, så I kan sætte gode forventninger. Afstemning betyder at tjekke, at uafhængige kilder stemmer overens: matcher varehusets total kildesystemet, summerer delene til helheden. Automatisér afstemning mellem kritiske systemer, og alarmér ved divergens, fordi et afstemningsbrud ofte er det tidligste og tydeligste signal om, at noget opstrøms gik galt.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper | Bedst egnet |
|---|---|---|---|
| Assertionstests (hård fejl) | Stopper dårlige data dødt, klare invarianter | Kan blokere pipelines for mindre problemer | Kritiske nøgler, referentiel integritet |
| Forventningstests (blødt flag) | Fanger drift, mindre skrøbelig | Kræver justering, kan ignoreres | Fordelinger, volumenbånd |
| Datakontrakter | Forebygger opstrøms overraskelser, klart ejerskab | Koordinerings- og styringsoverhead | Producent- eller forbrugergrænser på tværs af teams |
| Anomalidetektion | Fanger subtil, uforudset drift | Alarmtræthed, falske positiver | Tabeller med høj værdi, sæsonmålinger |
| Manuelle stikprøver | Billigt at starte, intet værktøj | Skalerer ikke, overser tavse fejl | Kun meget tidlig fase |
| Fuld observerbarhedsplatform | Bred dækning, afstamning, alarmering | Omkostning, opsætning, endnu et system at køre | Mange kilder, regulatorisk rapportering |

Den centrale spænding er dækning versus støj. Instrumentér intet, og problemer når jeres forbrugere først, hvilket ødelægger tillid. Instrumentér alt med hårtrigger-alarmer, og I drukner teamet i falske positiver, til de slår kanalen fra, hvilket også lader problemer nå forbrugere. Løs det ved at rangere jeres data efter sprængradius. De tabeller, der fodrer bestyrelsesmålinger, kundevendte produkter, regulatoriske rapporter og maskinlæringsmodeller, får den fulde behandling: kontrakter, hårde assertions, observerbarhed og vagtejerskab. Halen af eksplorative tabeller får letvægtsprofilering. Brug jeres pålidelighedsbudget, hvor forkerte data ville gøre mest ondt, og vær bevidst sparsomme alle andre steder.

## Spørgsmål til drøftelse med dit team

1. **Når dårlige data når produktion, hvem finder så først ud af det, og hvordan?** Dette er det mest afslørende enkeltspørgsmål om jeres datapålidelighed, fordi det ærlige svar som regel er "en forbruger, ved et tilfælde." Hvis en analytiker, en leder eller en kunde er jeres detektionssystem, måles jeres gennemsnitlige tid til at opdage i dage, og jeres troværdighed tager skraldet hver gang. Alternativet er instrumentering, der kalder det ejende team ud på fejlstedet, før det dårlige tal forplanter sig. Tag reelle tal med: hvor mange af jeres sidste ti datahændelser blev fanget af overvågning versus meldt af et menneske nedstrøms, og hvor længe sad hver uopdaget. Svaret fortæller jer, om I har observerbarhed eller blot håb, og det bør direkte drive, hvor I først investerer i tjek af friskhed, volumen, skema og fordeling.

2. **Hvilke datasæt har en ejer, en kontrakt og et servicenivå, og hvilke er forældreløse?** I skala kan de fleste datakvalitetsfejl spores tilbage til en uejet grænseflade: et producerende team ændrede noget uden at vide, hvem der afhang af det, fordi ingen kontrakt sagde det. Ejerskab er fundamentet, der gør kontrakter, alarmruter og hændelsesrespons mulige, og forældreløse datasæt er, hvor tavs korruption bor. Gennemgå jeres vigtigste tabeller, og spørg for hver, hvem der er ansvarlig, hvad producenten har forpligtet sig til, og hvilken friskhed og nøjagtighed forbrugerne er lovet. Tag jeres afstamning med: de tabeller med størst nedstrøms sprængradius er dem, der har mest brug for dette, og er ofte dem, der mangler det. Hullet mellem "vigtig" og "ejet" er jeres prioritetsliste for næste kvartal.

3. **Hvad er den faktiske omkostning ved en datakvalitetshændelse for os, og behandler vi den derefter?** Teams underinvesterer i datakvalitet, fordi omkostningen ved dårlige data er diffus og forsinket, så den aldrig viser sig som en linjepost, mens omkostningen ved at bygge kvalitetsværktøj er konkret og umiddelbar. Ram det ind igen ved at prissætte en reel hændelse ende til ende: den forkerte beslutning, omarbejdet, de ingeniørtimer brugt på at spore rodårsag uden afstamning, den eroderede tillid, der får folk til stille at genopbygge deres egne skyggedatasæt, og, i regulerede eller offentligt vendte sammenhænge, berigtigelsesmeddelelsen og dens omdømmeskade. Tag et specifikt eksempel fra det seneste år med, og læg det ærligt sammen. Hvis en enkelt tavs fejl i en betalings- eller offentlig statistikpipeline kunne koste mere end et års observerbarhedsværktøj, argumenterer business casen for sig selv, og samtalen skifter fra, om I skal investere, til hvor.

4. **Har vi rangeret vores datasæt efter sprængradius, og følger vores overvågningsinvestering faktisk den rangering?** Den centrale fejlform i skala er at bruge pålidelighedsindsats jævnt, så den eksplorative tabel, ingen stoler på, får samme opmærksomhed som den, der fodrer bestyrelsesmålinger, mens en hårtrigger-alarm på en tabel med lav værdi træner folk til at slå den kanal fra, der også bærer det kritiske opkald. I kan ikke instrumentere alt uden at drukne i støj, og I kan ikke instrumentere intet uden at lade problemer nå forbrugere først, så den reelle beslutning er, hvor den fulde behandling (kontrakter, hårde assertions, observerbarhed og vagtejerskab) går hen, og hvor letvægtsprofilering er nok. Tag en fortegnelse over jeres tabeller mærket med, hvad der afhænger af dem: bestyrelsesmålinger, kundevendte produkter, regulatoriske rapporter og maskinlæringsmodeller, med, og sammenlign så den rangering med, hvor jeres tjek og alarmer faktisk sidder i dag. For en virksomhed, der afstemmer mange kilder, eller en regering, der offentliggør lovbestemte tal, hører de tabeller med juridisk eller offentlig eksponering øverst på listen, og ethvert hul mellem "ville gøre mest ondt, hvis forkert" og "er mest overvåget" er en prioriteringsfejl at rette nu.

5. **Hvilke maskinlæringsmodeller og analyser beslutter på data, vi aldrig validerer, og hvilke fejl kan de tavst kode ind?** Et dashboard viser et forkert tal for ét menneske, der måske sætter spørgsmålstegn ved det, men en model træner på forkerte features og koder de fejl ind i hver forudsigelse, den laver, i en skala og uigennemsigtighed, der gør skaden langt sværere at få øje på eller omgøre. Det modstridende pres er hastighed: datavidenskabsteams vil bevæge sig hurtigt på nye features, og at tilføje validering, kontrakter og friskhedsgarantier til hver feed føles som friktion, til en model stille forringes, fordi en opstrøms kolonne drev. Tag en fortegnelse over jeres produktionsmodeller og analyser, de datasæt hver forbruger, og en ærlig markering af, hvilke af de feeds der har tests, kontrakter og observerbarhed versus hvilke der er ubeskyttede, med. I en virksomheds- eller offentlig sammenhæng, hvor en model påvirker kredit-, ydelses- eller håndhævelsesbeslutninger, bliver uvaliderede træningsdata en revisions- og retfærdighedsforpligtelse oven i en kvalitetsrisiko, så spørgsmålet om, hvilke feeds der lukker en modeludgivelse, bør have en ejer og et dokumenteret svar (kapitel 6.5).

6. **Når en kvalitetsfejl dukker op uger efter, kan vi så faktisk genbehandle og afstemme, eller har vi allerede kasseret det, vi ville få brug for?** Mange kvalitetsfejl er usynlige ved indlæsning og bliver først tydelige senere, når et afstemningsbrud eller en mistænkelig tendens får nogen til at kigge, og på det tidspunkt afhænger evnen til at rette det rent af valg, I traf meget tidligere: om I beholdt uforanderlige rådata, om uafhængige kilder kan afstemmes, og om afstamning lader jer spore det dårlige tal til dets oprindelse. Spændingen er omkostning og enkelhed mod reproducerbarhed, fordi det ikke er gratis at bevare rådata og køre kontinuerlig afstemning mellem systemer, og det er fristende at slette rå input, når de transformerede tabeller ser rigtige ud. Tag jeres opbevarings- og uforanderlighedspolitik for rådata, listen over kritiske systempar, I afstemmer automatisk, og et reelt eksempel på en fejl, I enten kunne eller ikke kunne genbehandle jer ud af, med. For et offentligt agentur under en lovbestemt forpligtelse til at spore ethvert offentliggjort tal tilbage til kildeposter, eller en virksomhed, der står over for en regulatorisk genfremsættelse, er uforanderlige rådata og automatiseret afstemning ikke valgfri hygiejne, men den mekanisme, der gør en berigtigelse forsvarlig.

## Sektorperspektiv

**Startup.** Hastighed og tillid betyder mere end dækning. Læg en håndfuld letvægtstests i jeres transformationsværktøj (unikhed og ikke-null på nøgler, accepterede værdier på de kolonner, der bærer betydning, et rækkeantalsbånd pr. kilde), og tilføj friskheds- og volumenovervågning kun på de få tabeller, der fodrer virksomhedens målinger. Rut hver alarm til én kanal, som én ingeniør ejer, og modstå at købe en observerbarhedsplatform, før I har tabellerne eller teamet til at retfærdiggøre den. Målet er at opdage et fejlmærket felt, før det puster et tal op, grundlæggerne citerer, ikke at instrumentere alt.

**Lille virksomhed.** Uden en dataingeniør og med et stramt budget så støt jer til de kvalitetsfunktioner, der allerede er bygget ind i det varehus, BI-værktøj eller de SaaS-platforme, I betaler for, frem for at rejse en separat stak. Fokusér jeres indsats på de få tal, der faktisk driver beslutninger (omsætning, pipeline, lager), tjek dem fornuftsmæssigt mod en uafhængig kilde med jævn kadence, og behandl en leverandørs friskheds- og skemaalarmer som gode nok, når de findes. At købe kvalitet indlejret i værktøjer, I allerede kører, slår at bygge en pipeline, I ikke har nogen til at vedligeholde.

**Stor virksomhed.** Problemet er pålidelighed på tværs af mange teams og tusinder af tabeller, så standardisér grænsefladen: datakontrakter ved hver producentgrænse, en observerbarhedsplatform der iagttager friskhed, volumen, skema og fordeling, og afstamning offentliggjort i et katalog til konsekvensanalyse. Rangér datasæt efter sprængradius, læg anomalidetektion og vagtejerskab på dem med høj værdi, og kør datahændelser gennem samme alvorligheds- og postmortemproces som tjenesteudfald. Servicenivåer på de pipelines, der fodrer regulatoriske rapporter og lederdashboards, forvandler datapålidelighed fra en ambition til en målt, styret forpligtelse.

**Offentlig sektor.** Lovbestemt nøjagtighed og offentlig ansvarlighed sætter overliggeren: land uforanderlige rå undersøgelses- og administrative poster, transformér dem i lagdelte, testede trin, og afstem mod kildetotaler ved hvert skridt. Bevar fuld afstamning, så ethvert offentliggjort tal kan spores til kildeposter ved revision, og luk hver udgivelse bag validering af validitet, fuldstændighed og konsistens mod tidligere perioder. Indkøb af værktøj bør kræve åbenhed og dataportabilitet, og en forkert offentlig statistik skal håndteres som en alvorlig hændelse, med den samme tyngde, som offentlig tillid til officielle tal kræver.

## Eksempler

**Startup.** Et firma på tyve personer kører sin go-to-market på et varehus fodret af produkthændelser og en betalingsudbyder. Tidligt fik et fejlmærket valutafelt stille omsætningen til at se oppustet ud i to uger, før nogen lagde mærke til det, hvilket rystede teamets tillid til hvert dashboard. De svarede med et let sæt tests i deres transformationsværktøj: unikhed og ikke-null på nøgler, tjek af accepterede værdier på valuta- og statuskolonner og et rækkeantalsbånd pr. kilde. De tilføjede basal friskheds- og volumenovervågning på de få tabeller, der fodrer virksomhedens målinger, rutet til en enkelt Slack-kanal, én ingeniør ejer. Det er beskedent, men det fanger de fejl, der betyder noget, og grundlæggerne stoler på tallene igen.

**Stor virksomhed.** En multinational bank afstemmer kunde- og transaktionsdata på tværs af dusinvis af kildesystemer ind i et styret varehus, der fodrer regulatoriske rapporter, risikomodeller og lederdashboards. Den kører datakontrakter ved hver producentgrænse, så en opstrøms skemaændring versioneres og forhandles frem for at blive sprunget på forbrugere. En observerbarhedsplatform overvåger friskhed, volumen, skema og fordeling på tværs af tusinder af tabeller, med anomalidetektion på dem med høj værdi og afstamning offentliggjort i et datakatalog til konsekvensanalyse. Datahændelser følger den samme alvorligheds- og vagtproces som tjenesteudfald, med servicenivåer på de pipelines, der fodrer regulatoriske indberetninger. Når et kildesystem driver, bliver det ejende team kaldt ud, og de berørte nedstrøms rapporter er kendt inden for minutter, ikke opdaget af en tilsynsmyndighed.

**Offentlig sektor.** Et nationalt statistikagentur offentliggør økonomiske indikatorer, som markeder, politikere og offentligheden behandler som autoritative, så nøjagtighed er en lovbestemt forpligtelse, og hvert offentliggjort tal skal kunne revideres. Dets pipelines lander uforanderlige rå undersøgelses- og administrative poster og transformerer dem derefter i lagdelte, testede trin med afstemning mod kildetotaler ved hvert skridt. Fuld afstamning lader analytikere spore ethvert offentliggjort tal tilbage til kildeposter, hvilket både er et kvalitetsværktøj og et juridisk krav. Før udgivelse passerer tal valideringsporte for validitet, fuldstændighed og konsistens mod tidligere perioder, og enhver anomali undersøges og dokumenteres frem for at blive offentliggjort. En forkert offentlig statistik er en alvorlig hændelse, så agenturet behandler datanedetid med den tyngde, offentlig tillid kræver.

## Business case: motivation, ROI og TCO

Afkastet af datakvalitet og observerbarhed kommer af bevaret tillid, afkortede hændelser og undgåede dårlige beslutninger. Troværdige data er fundamentet, der får hver nedstrøms investering i analyse, business intelligence og AI til reelt at betale sig, fordi en model eller et dashboard kun er så godt som de data, der ligger under. Når kvalitetstjek fanger en dårlig indlæsning ved grænsen, undgår I den langt større omkostning ved, at et forkert tal når en beslutning, en kunde eller en indberetning. Afstamning kollapser rodårsagsundersøgelse fra dages manuel sporing til minutter, hvilket er ren genvundet ingeniørtid. Observerbarhed skrumper den gennemsnitlige tid til at opdage fra "når en forbruger klager" til "når pipelinen fejler", hvilket er, hvor det meste af tillidsskaden undgås.

Den samlede ejeromkostning omfatter værktøj til test, observerbarhed og katalogisering, plus ingeniørtiden til at instrumentere pipelines og det organisatoriske arbejde med at tildele ejere og skrive kontrakter. Det er reelt, men vej det mod omkostningen ved ikke at gøre det: tavs korruption opdaget af ledere, maskinlæringsmodeller trænet på dårlige features, der koder fejl ind i skala, analytikere der stille genopbygger skyggedatasæt, fordi de ikke længere stoler på de officielle, og, i regulerede eller offentlige sammenhænge, berigtigelsesmeddelelser, der skader troværdigheden i årevis. Over for ledelsen så ram datakvalitet ind som forsikring på hver datadrevet beslutning, organisationen træffer. Præmien er beskeden og forudsigelig. Det uforsikrede tab, et enkelt højprofileret forkert tal, er ingen af delene.

## Anti-mønstre og faldgruber

- At behandle datakvalitet som et engangsoprydningsprojekt i stedet for en løbende ingeniørpraksis.
- At opdage fejl fra forbrugere nedstrøms frem for fra overvågning på fejlstedet.
- Intet datasætejerskab, så ingen er ansvarlig, når noget går i stykker, og ingen bliver kaldt ud.
- Producenter der ændrer skemaer eller semantik uden kontrakt og tavst bryder hver forbruger.
- Anomalialarmer så støjende, at teamet slår kanalen fra og overser den virkelige hændelse.
- At fodre uvaliderede data direkte ind i maskinlæringsmodeller og kode fejl ind i skala (kapitel 6.5).
- At vedligeholde afstamning som et håndtegnet diagram, der er forkert dagen efter, I tegner det.
- At jagte perfekte data overalt i stedet for egnet-til-brug-kvalitet på de tabeller, der betyder noget.
- At slette rådata, så I ikke kan genbehandle eller afstemme, når en kvalitetsfejl dukker op senere.

## Modenhedsmodel

- **Niveau 1, Opstart:** Kvalitet er ingens job. Problemer findes af forbrugere, som regel efter et forkert tal har nået en rapport. Ingen tests, ingen overvågning, intet ejerskab. Rettelser er manuel brandslukning, og de samme fejl gentager sig.
- **Niveau 2, Udvikling:** Nogle teams tilføjer basale tests på deres kritiske tabeller (nøgler, nulls, accepterede værdier) og lidt friskheds- og volumenovervågning på de datasæt, de bekymrer sig mest om. Praksisserne virker, hvor de findes, men dækning og stringens varierer fra team til team, intet er standardiseret, og hændelser håndteres stadig reaktivt.
- **Niveau 3, Standardisering:** Kvalitetsdimensioner er defineret med tærskler, og de samme forventninger gælder på tværs af teams frem for at afhænge af, hvem der byggede en pipeline. Datakontrakter styrer vigtige producentgrænser, observerbarhed dækker friskhed, volumen, skema og fordeling på vigtige tabeller, og afstamning understøtter konsekvensanalyse. Hvert vigtigt datasæt har en navngiven ejer, og datahændelser følger en dokumenteret alvorligheds- og responsproces i hele organisationen.
- **Niveau 4, Styring:** Kvalitet og pålidelighed måles og styres mod baselines. Datanedetid følges med reelle målinger: gennemsnitlig tid til at opdage, gennemsnitlig tid til at løse, friskhed og nøjagtighed mod aftalte servicenivåer og fejlbudgetter, et datasæt kan bruge, før det udløser handling. Afstemningsbrudrater, testbestå-rater og falsk-positiv-rater for anomalier trendes over tid, alarmering justeres mod de tal frem for ved gæt, og go/no-go-beslutninger om en dataudgivelse træffes på målt kvalitet mod baseline frem for på håb.
- **Niveau 5, Orkestrering:** Kvalitet og observerbarhed er gennemgribende, automatiserede og adaptive. Anomalidetektion fanger subtil drift, kontrakter håndhæves mekanisk, og afstamning indfanges automatisk og offentliggøres i et katalog. Data har servicenivåer og vagtejerskab som produktionstjenester, afstemning kører kontinuerligt, og skyldfrie postmortems fodrer en støt reduktion i datanedetid. Kvalitet er integreret med datastyring, maskinlæring og forretningsplanlægning, og organisationen omafgrænser løbende tærskler, dækning og ejerskab, efterhånden som datalandskabet skifter.

## Idéer til drøftelse

1. Hvilke af jeres tabeller ville forårsage mest skade, hvis de var tavst forkerte i en uge, og er det dem, I overvåger mest?
2. Hvor ville en datakontrakt have forebygget jeres seneste opstrøms forårsagede hændelse, og hvorfor var der ikke en?
3. Hvor meget ingeniørtid tager en typisk rodårsagsundersøgelse i dag, og hvor meget ville automatiseret afstamning spare?
4. Træner nogen af jeres maskinlæringsmodeller på data, I ikke validerer, og hvilke fejl kan de kode ind?
5. Er jeres alarmering justeret godt nok til, at folk handler på hver alarm, eller har nogen slået kanalen fra?
6. Hvilke friskheds- og nøjagtighedsservicenivåer ville jeres vigtigste forbrugere faktisk skrive under på, og kunne I opfylde dem i dag?

## Vigtigste pointer

- Datakvalitet er egnethed til brug på tværs af nøjagtighed, fuldstændighed, konsistens, rettidighed, validitet og unikhed.
- Dårlige data er værre end ingen data, fordi de tavst korrumperer beslutninger og modeller.
- Test data som kode: assertions- og forventningstests plus skematjek, i CI og i produktion.
- Brug datakontrakter til at gøre producent- og forbrugerforventninger eksplicitte og håndhævelige.
- Observér friskhed, volumen, skema og fordeling, i parallel til softwareobserverbarhed (kapitel 9.2).
- Indfang afstamning til hurtig rodårsag og konsekvensanalyse, og offentliggør den for forbrugere.
- Behandl datahændelser som produktionshændelser, med ejerskab, alvorlighed og servicenivåer.
- Instrumentér, hvor forkerte data gør mest ondt; sigt efter egnet-til-brug-kvalitet, ikke perfektion overalt.

## Referencer og videre læsning

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
