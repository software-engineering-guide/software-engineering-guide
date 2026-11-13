# 8.7 Buildsystemer og artefaktstyring

## Overblik og motivation

Buildet er, hvor jeres kildekode bliver til noget, I kan levere. Hver pipeline i kapitel 8.1 starter her: før I kan teste, scanne, udrulle eller promovere noget, skal et buildsystem forvandle et træ af kildefiler til et konkret artefakt, en kompileret binær, en pakke, et containerimage eller en pakke af statiske aktiver. Hvis det første trin er langsomt, ustabilt eller ureproducerbart, arver hvert trin efter det skaden. Et build, der producerer forskelligt output på to maskiner, underminerer hver test, I kører, og hver godkendelse, I indsamler, fordi det, I efterprøvede, ikke beviseligt er det, I leverer.

Dette kapitel handler om det første trin og dets output: det buildsystem, der konstruerer artefakter, og den artefaktstyring, der lagrer, versionerer, sikrer og promoverer dem. Det er bevidst snævrere end kapitel 8.1, som dækker hele pipelinen for kontinuerlig integration og kontinuerlig levering (CI/CD). Her er emnet selve buildet og de artefakter, det udsender. Det supplerer kapitel 2.10 om softwarekonfigurationsstyring, som styrer, hvordan I sporer og kontrollerer inputtene, og kapitel 2.18 om afhængigheds- og forsyningskædestyring, som styrer den tredjepartskode, I trækker ind. Buildet er, hvor disse input mødes: jeres kilde, jeres afhængigheder og jeres konfiguration konvergerer alle til ét uforanderligt output.

For store teams er indsatsen konkret. Når hundredvis af ingeniører venter på build på flere minutter mange gange om dagen, overstiger den samlede tabte tid næsten enhver anden ingeniøromkostning. Når artefakter er foranderlige, usporede eller genbygget pr. miljø, mister I evnen til med sikkerhed at sige, hvad der kører i produktion. I virksomheds- og offentlige sammenhænge er den sporbarhed ikke valgfri. Revisorer og sikkerhedsansvarlige har brug for dokumentation for, at binæren i produktion kom fra gennemgået kilde, bygget af et betroet system, med en registreret forvaringskæde. En disciplineret build- og artefaktpraksis forvandler den dokumentation til et biprodukt af normalt arbejde frem for en panik før hver revision.

## Grundprincipper

- Buildet er det første trin i levering: behandl dets hastighed og korrekthed som produktionsanliggender.
- Sigt mod reproducerbare og, hvor det er muligt, hermetiske builds: samme input, samme output, hver gang.
- Byg et artefakt én gang, og promovér så netop det artefakt på tværs af miljøer.
- Gør artefakter uforanderlige og indholdsadresserede, og versionér dem meningsfuldt.
- Gem artefakter i et administreret repository med opbevaring, adgangskontrol og proveniens.
- Cache aggressivt, men behandl cachen som en sikkerhedsgrænse, ikke blot et hastighedstrick.
- Indfang proveniens, signaturer og en materialefortegnelse ved buildtidspunktet, ikke bagefter.

## Anbefalinger

### Behandl buildet som det første trin i levering

Jeres buildsystem er produktionsinfrastruktur, og I bør finansiere og vedligeholde det derefter. Den hurtige, korrekte konstruktion af et artefakt er det fundament, CI/CD (kapitel 8.1) hviler på. Når teams behandler buildet som en eftertanke, en bunke shellscripts ingen ejer, betaler de for det i ustabile pipelines, mystiske "det virker på min maskine"-fejl og langsom feedback, der eroderer hele det ingeniørflow, der er beskrevet i del 11. Giv buildet en ejer, en definition holdt i versionsstyring sammen med koden (kapitel 2.14 om projekt- og repositoriestruktur) og den samme gennemgangsdisciplin som ethvert andet kritisk system.

### Gør builds reproducerbare og, hvor I kan, hermetiske

Et [reproducerbart build](https://en.wikipedia.org/wiki/Reproducible_builds) producerer bit-for-bit identisk output fra den samme kilde, så enhver uafhængigt kan genbygge og verificere, at et artefakt matcher dets kilde. Det er den egenskab, der lader jer stole på, at en binær ikke blev manipuleret mellem commit og udrulning. At nå dertil betyder at eliminere kilder til ikke-determinisme: indlejrede tidsstempler, absolutte filstier, tilfældighed i byggerækkefølge og netværkshentninger, hvis resultater driver over tid.

Et hermetisk build går videre ved at deklarere hvert input på forhånd og køre i et isoleret miljø, der ikke kan nå netværket eller værtens omgivende tilstand. Intet kommer ind i buildet undtagen det, I deklarerede: fastlåste værktøjskædeversioner, fastlåste afhængigheder, eksplicitte kildefiler. Hermeticitet er, hvad gør reproducerbarhed pålidelig frem for heldig. Fuld hermeticitet har en reel omkostning i værktøj og disciplin, så behandl den som en retning frem for en binær. Selv delvis fremgang, at fastlåse jeres compilerversion, at vendore eller låse afhængigheder, at fjerne tidsstempler, køber jer det meste af tilliden for en brøkdel af indsatsen.

### Opløs afhængigheder deterministisk med lockfiler

Hvert build trækker tredjepartskode ind, og hvordan I opløser den, afgør, om jeres build er deterministisk. En [lockfil](https://en.wikipedia.org/wiki/Lock_file) registrerer den præcise opløste version og kryptografiske hash af hver direkte og transitiv afhængighed, så et build måneder herfra opløses til præcis den samme graf. Commit lockfilen, behandl ændringer i den som gennemgåelige begivenheder, og verificér hashes ved hver hentning, så en muteret opstrøms pakke ikke kan slippe ind uset. Det er buildtidsansigtet af forsyningskædedisciplinen i kapitel 2.18. Uden en lockfil fortæller "det byggede i går" jer intet om, hvad det vil bygge i dag, fordi et flydende versionsinterval tavst kan trække en ny release, eller en angriber kan udgive en ondsindet.

### Brug inkrementelle builds og caching, lokalt og eksternt

Ingen bør genbygge det, der ikke har ændret sig. Inkrementelle builds sporer, hvilke input der fodrer hvilke output, og genbygger kun de dele, en ændring berører. En buildcache lagrer outputtene fra tidligere arbejde nøglet på en hash af deres input, så et uændret mål hentes frem for genberegnes. En lokal cache fremskynder én udviklers løkke; en ekstern eller distribueret buildcache deler resultater på tværs af hele teamet og CI-flåden, så den første, der bygger et givent input, betaler omkostningen, og alle andre får et cache-hit. I et stort monorepo er det forskellen mellem et ti-minutters build og et ti-sekunders.

Udbyttet er udviklerfeedbackhastighed, som er en af de investeringer med højest løftestang, I kan foretage. Hurtig, korrekt feedback holder ingeniører i flow og forkorter løkken mellem at skrive kode og at vide, om den virker. Vogt dog omhyggeligt cachens korrekthed: en cachenøgle, der udelader et reelt input (en miljøvariabel, en værktøjsversion), producerer forældede resultater, som er vanvittige at fejlfinde. Cachen er kun så troværdig som fuldstændigheden af dens inputhashing.

### Vælg buildværktøj, der matcher jeres skala

Buildværktøjer sidder på et spektrum. I den lette ende modellerer [Make](https://en.wikipedia.org/wiki/Make_(software)) og sprognative værktøjer en simpel afhængighedsgraf og rækker til en enkelt tjeneste eller et lille repo. I midten tilføjer økosystemværktøjer som Gradle og Maven til Java-verdenen eller standardværktøjskæderne til Go, Rust og JavaScript afhængighedsopløsning og konventioner. I den tunge ende modellerer grafbaserede systemer som [Bazel](https://en.wikipedia.org/wiki/Bazel_(software)) og lignende monorepo-buildværktøjer hele buildet som en finkornet, hermetisk [rettet acyklisk graf](https://en.wikipedia.org/wiki/Directed_acyclic_graph) af mål, hvilket muliggør præcis inkrementalitet, ekstern caching og ekstern eksekvering på tværs af en stor kodebase.

Tungere værktøj betaler sig, når I har mange indbyrdes afhængige projekter, et stort monorepo (kapitel 2.14) eller buildtider, der kvæler jeres teams. Det koster reel investering: en stejlere indlæringskurve, migreringsindsats og et dedikeret team til at vedligeholde builddefinitionerne. Adoptér ikke Bazel-klasse værktøj, fordi det er på mode. Adoptér det, når jeres buildgraf er stor nok til, at finkornet caching og parallelisme genvinder mere ingeniørtid, end værktøjet koster at køre. For de fleste små og mellemstore systemer er et godt økosystemværktøj med en ekstern cache det sweet spot.

### Gem artefakter i et administreret repository

Når I har bygget et artefakt, har det brug for et hjem. Et [artefaktrepository](https://en.wikipedia.org/wiki/Software_repository) (også kaldet et register) lagrer jeres pakker, containerimages og binære filer med versionering, adgangskontrol og metadata. Det er modstykket til jeres kilderepository: kilde ind, artefakter ud, begge styret. Et godt repository giver jer ét betroet sted at udgive og hente interne artefakter, proxier og cacher eksterne, så I ikke rækker ud til det offentlige internet ved hvert build, og registrerer, hvem der udgav hvad og hvornår. Containerimages har deres egne registerkonventioner, og andre pakketyper har deres, men disciplinen er den samme: intet kører i produktion, som ikke kom fra et administreret, adgangskontrolleret lager.

### Versionér artefakter, og gør dem uforanderlige og indholdsadresserede

Giv hvert artefakt en meningsfuld version. [Semantisk versionering](https://en.wikipedia.org/wiki/Software_versioning) (major.minor.patch) kommunikerer en ændrings karakter til forbrugere: et major-spring signalerer en brydende ændring, et minor tilføjer kompatible funktioner, en patch retter fejl. Ved siden af den menneskelæselige version så identificér hvert artefakt ved en kryptografisk hash af dets indhold, så det er indholdsadresseret. En indholdsadresse, ofte kaldet et digest, er et fingeraftryk, der ændrer sig, hvis en enkelt byte ændrer sig, hvilket lader jer henvise til et præcist artefakt utvetydigt og opdage enhver manipulation.

Gør udgivne artefakter uforanderlige: når en version er udgivet, ændrer den sig aldrig. At genudgive andre bytes under samme version er en forsyningskædefare og et fejlfindingsmareridt, fordi to personer kan holde "version 1.4.2" og have forskellig software. Foranderlige tags som "latest" er bekvemme for mennesker, men skal for alt, der betyder noget, altid opløses til et specifikt uforanderligt digest, som I registrerer. Udrul efter digest, ikke efter flydende tag, så det, I testede, beviseligt er det, I kører.

### Byg én gang, promovér overalt

Byg et artefakt én gang, og flyt så det samme artefakt gennem jeres miljøer: udvikling, staging, produktion. Denne "byg én gang, promovér overalt"-regel er den vigtigste enkeltartefaktstyringspraksis. Hvis I genbygger pr. miljø, har I kastet jeres garanti væk for, at det testede artefakt er det udrullede, fordi hver genbygning kan trække en anden afhængighed eller køre på en let anderledes maskine. Promovering er en metadataoperation: I markerer et allerede bygget, allerede testet digest som godkendt til næste miljø, og I konfigurerer det til det miljø gennem eksternaliseret konfiguration (kapitel 2.10) frem for ved at genbygge. Det holder binæren konstant og konfigurationen variabel, hvilket netop er den adskillelse, I vil have for både pålidelighed og revisionsbarhed.

### Indfang proveniens, signér artefakter, og generér en SBOM

Ved buildtidspunktet så registrér, hvor artefaktet kom fra, og bevis, at det ikke er ændret. Proveniens er en signeret erklæring om, hvordan et artefakt blev bygget: hvilken kildecommit, hvilken builder, hvilke input. At signere et artefakt lader forbrugere verificere ægthed og integritet, før de kører det, og at verificere signaturer ved udrulning lukker løkken. En [software bill of materials](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM), en komplet fortegnelse over komponenterne og afhængighederne inde i et artefakt, lader jer svare på "er vi berørt?" inden for minutter, når en ny sårbarhed offentliggøres, frem for at bruge dage på at rode gennem buildlogs.

Rammeværker som SLSA (Supply-chain Levels for Software Artifacts) giver jer en graderet model for buildtidsintegritet: højere niveauer kræver hermetiske, isolerede builds og uforfalskelig proveniens. Generér alt dette i buildet, hvor informationen er autoritativ og billig at indsamle, ikke rekonstrueret bagefter, når det er dyrt og upålideligt. Dette arbejde tjener direkte den sikre softwareudviklingslivscyklus i kapitel 4.9 og forsyningskædehensynene i kapitel 2.18.

### Sikr cachen, og styr opbevaring og omkostning

En delt buildcache er en delt tillidsgrænse. Hvis en angriber kan skrive en forgiftet post, kører hver forbruger, der henter den, kompromitteret kode, og hastighedsfordelen bliver en angrebsflade. Beskyt cachen med autentificering, afgræns skriveadgang snævert (ofte kun betroet CI, aldrig udvikleres bærbare), og sørg for, at cachenøgler hasher hvert reelt input, så en forgiftet eller forældet post ikke kan udgive sig for en legitim. Behandl cacheforgiftning som en reel trusselsmodel, især for eksterne caches delt på tværs af teams.

Artefakter akkumulerer også omkostning. Containerimages og buildoutput er store, og et ubegrænset register vokser, til lagerregninger og langsomme opslag tvinger sagen. Definér opbevaringspolitikker: behold hvert produktionspromoveret artefakt og alt, der refereres af et kørende system, lad gamle udviklings- og pull request-builds udløbe automatisk, og registrér, hvad I slettede. Målet er et lager, der beholder det, I har brug for til reproducerbarhed og revision, mens det smider støjen, til en omkostning, I bevidst vælger, frem for en der overrasker jer.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Tungt grafbuildværktøj (Bazel-klasse) | Finkornet inkrementalitet, ekstern cache og eksekvering, skalerer til enorme monorepos | Stejl indlæringskurve, migreringsomkostning, kræver et dedikeret buildteam |
| Let buildværktøj (Make, native) | Enkelt, lav overhead, hurtigt at adoptere | Dårlig inkrementalitet og caching i skala, svag hermeticitet |
| Ekstern/distribueret buildcache | Delte resultater, dramatiske speedups på tværs af flåden | Cacheforgiftningsflade, korrekthed afhænger af komplet inputhashing |
| Fuldt hermetiske builds | Pålidelig reproducerbarhed, stærk proveniens | Reel værktøjs- og disciplinomkostning, sværere lokale arbejdsgange |
| Byg én gang, promovér overalt | Testet artefakt er lig leveret artefakt, rent revisionsspor | Kræver eksternaliseret konfiguration og disciplineret promovering |
| Uforanderlige, indholdsadresserede artefakter | Manipulationssikre, utvetydige referencer | Mindre bekvemt end flydende tags, mere lager at styre |
| Lang artefaktopbevaring | Fuld reproducerbarhed og revisionshistorik | Lageromkostning, langsommere opslag uden oprydningspolitik |

Den tilbagevendende spænding er mellem hastighed og tillid. Caching, delte buildfarme og flydende tags gør alle builds hurtigere og mere bekvemme, og hver enkelt svækker, brugt skødesløst, jeres evne til at sige præcis, hvad I byggede, og bevise, at det ikke blev manipuleret. Løs det ved at gøre den troværdige vej til den hurtige vej. En komplet inputhash gør cachen både hurtig og korrekt. At udrulle efter digest er lige så hurtigt som efter tag og langt sikrere. At generere en SBOM i buildet koster sekunder og sparer dage. I behøver sjældent vælge hastighed frem for integritet, hvis I designer integriteten ind i den hurtige vej fra begyndelsen.

## Spørgsmål til drøftelse med dit team

1. **Kan vi genbygge sidste kvartals produktionsartefakt i dag og få de samme bytes, og hvis ikke, hvad mangler?** Det er den skarpeste test af jeres builddisciplin, fordi reproducerbarhed afhænger af fastlåste værktøjskæder, låste afhængigheder og eliminerede ikke-determinismer, der alle virker sammen. Vælg et specifikt artefakt, der blev leveret for nogle måneder siden, og forsøg faktisk at genbygge det fra den registrerede kildecommit. Det, I lærer af forsøget, er mere værd end noget politikdokument: måske flød et afhængighedsinterval, måske blev compilerversionen aldrig fastlåst, måske er et tidsstempel bagt ind. De huller, I finder, er jeres reproducerbarhedsefterslæb, og at lukke dem er, hvad lader jer stole på, at det, I reviderede, er det, I kører, hvilket betyder enormt meget i regulerede og offentlige sammenhænge, hvor den forvaringskæde er et juridisk krav.

2. **Bygger vi hvert artefakt én gang og promoverer det, eller genbygger vi pr. miljø, og hvordan ville vi bevise hvilket?** Mange teams tror, at de promoverer et enkelt artefakt, men opdager, når de ser nærmere efter, at staging og produktion hver udløser et nyt build med subtilt forskellige input. Spor én reel release fra commit til produktion, og bekræft, om det nøjagtig samme digest flyttede gennem hvert miljø, eller om nye bytes blev produceret undervejs. Hvis I finder genbygninger, har I fundet et sted, hvor jeres testgarantier er svagere, end I troede, fordi det testede artefakt og det udrullede artefakt ikke beviseligt er identiske. Rettelsen, at eksternalisere konfiguration, så binæren forbliver konstant, mens indstillinger varierer, betaler sig i både pålidelighed og en langt renere revisionshistorie.

3. **Hvis en kritisk sårbarhed blev annonceret i et almindeligt bibliotek i morgen, hvor hurtigt kunne vi så liste hvert artefakt, der indeholder det?** Dette spørgsmål tester, om jeres buildtidsproveniens og SBOM-praksis er reel eller ambitiøs. Når en udbredt komponent viser sig at være udnyttelig, er de organisationer, der kommer sig på timer, dem, der genererer en materialefortegnelse ved buildtidspunktet og gemmer den med hvert artefakt; dem, der kommer sig på uger, er dem, der søger gennem buildlogs og interviewer ingeniører. Gennemgå scenariet konkret med et bibliotek, I faktisk afhænger af, og mål, hvor lang tid svaret ville tage i dag. Hullet mellem den tid og "minutter" er et direkte mål for jeres forsyningskædeeksponering, og det forbinder sig direkte med arbejdet med den sikre udviklingslivscyklus i kapitel 4.9.

4. **Hvor meget ingeniørtid koster vores builds hver dag, og hvad er business casen for at gøre dem hurtigere?** Buildlatens er en skat betalt ved hver ændring af hver ingeniør, og i skalaen hos et stort team er det samlede let at undervurdere, fordi ingen enkelt ventetid føles dyr. At aftale at måle den forvandler en vag klage til et tal, I kan veje mod omkostningen ved en ekstern cache, bedre inkrementalitet eller tungere buildværktøj. Tag jeres mediane og værste-tilfælde lokale og CI-buildtider, antallet af builds om dagen og et ærligt estimat af, hvor ofte et langsomt build skubber nogen ud af flow og ind i et kontekstskifte, med. Det modstridende hensyn er, at hurtigere builds ikke er gratis: en ekstern cache og distribueret eksekvering tilføjer infrastruktur at køre og sikre, og tungere værktøj tilføjer et vedligeholdelsesteam. For en virksomheds- eller offentlig organisation så tæl gennemløbs- og moralomkostningen ved langsom feedback på tværs af mange teams med, som som regel overstiger infrastrukturregningen og netop er den ramme, ledelsen allerede finansierer.

5. **Hvem kan skrive til vores delte buildcache, og hvad forhindrer en forgiftet post i at nå produktion?** En delt cache bytter en hastighedsgevinst for en ny tillidsgrænse, og den samme mekanisme, der lader én ingeniørs resultat betjene hele flåden, lader én korrumperet eller ondsindet post kompromittere alle, der henter den. For et stort team er sprængradius hele organisationen, så dette fortjener en bevidst beslutning frem for hvad et værktøjs standarder tilfældigvis er. Tag listen over, hvem og hvad der har skriveadgang til hver cache, om skrivninger er afgrænset til betroet CI frem for udvikleres bærbare, og om jeres cachenøgler hasher hvert reelt input, så en forældet eller forgiftet post ikke kan udgive sig for legitim, med. Spændingen er, at de strammeste kontroller sinker den bekvemme vej, hvor udviklere skubber cacheposter fra deres egne maskiner. I virksomheds- og offentlige sammenhænge så behandl cacheforgiftning som en eksplicit trussel i jeres forsyningskædemodel, og kræv den samme adgangskontrol, logning og gennemgang, I anvender på ethvert andet produktionssystem, der kan injicere kode i en release.

6. **Hvornår retfærdiggør vores buildgraf tungere værktøj, og hvordan vil vi vide, at vi har krydset den grænse?** Valget mellem et let økosystemværktøj og et grafbaseret system som Bazel er en af de dyrere og sværere at omgøre beslutninger på dette område, fordi migrering af en stor kodebase til finkornede builddefinitioner koster måneder og et dedikeret team. At afgøre tærsklen på forhånd forhindrer jer i enten at adoptere kompleksitet, I ikke har brug for, fordi det er på mode, eller at klamre jer til et let værktøj længe efter, at jeres buildtider kvæler hvert team. Tag størrelsen og den indbyrdes afhængighed af jeres buildgraf, nuværende build- og cache-hit-målinger og et realistisk estimat af migrerings- og løbende vedligeholdelsesomkostning mod den ingeniørtid, værktøjet ville genvinde, med. Det modstridende træk er, at tungt værktøj leverer præcis inkrementalitet og ekstern eksekvering, intet andet matcher i skala, men kun hvis jeres graf er reelt stor nok til at betale det tilbage. For en stor virksomhed eller et stort agentur så vej også, om værktøjets hermeticitets- og proveniensgarantier hjælper med at opfylde revisions- og forsyningskædekrav, hvilket kan flytte regnestykket ud over rå hastighed.

## Sektorperspektiv

**Startup.** Med et lille team og ingen runway til buildinfrastruktur så hold det let: brug sprognative buildværktøjer, adoptér lockfiler fra dag ét, og udrul containerimages efter digest frem for "latest"-tagget, da de vaner koster næsten intet og sparer jer for en hel klasse af "det virker på min maskine"-smerte senere. Modstå tunge grafbuildværktøjer; jeres knappeste ressource er ingeniøropmærksomhed. En ekstern buildcache er den ene opgradering, der er værd at række efter, når builds begynder at krybe forbi et par minutter.

**Lille virksomhed.** Uden en dedikeret buildingeniør så støt jer til administrerede tjenester frem for at køre jeres egen artefaktinfrastruktur: et hostet register og jeres CI-udbyders indbyggede cache giver versionering, opbevaring og adgangskontrol uden et platformsteam. Ram valget ind som køb frem for byg, sæt en automatisk udløbspolitik, så lageromkostninger forbliver forudsigelige, og sørg for, at det grundlæggende er på plads, låste afhængigheder og uforanderlige, digestfastlåste udrulninger, fordi de beskytter jer, selv når ingen iagttager pipelinen på fuld tid.

**Stor virksomhed.** På tværs af mange teams er problemet ensartethed: en fælles, ejet buildplatform, et fælles artefaktrepository og håndhævede standarder for lockfiler, signering, SBOM'er og byg-én-gang-promovér, så ingen gruppe genopfinder en upålidelig pipeline. Invester i en ekstern cache og, hvor buildgrafen retfærdiggør det, grafbaseret værktøj, og behandl cachen som en styret tillidsgrænse med afgrænset skriveadgang og revisionslogning. Styr artefakter som en kontrolleret ejendom med opbevaringspolitikker og proveniens, så enhver produktionskomponent kan spores tilbage til gennemgået kilde efter behov.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed gør buildtidsintegritet til et compliancekrav, ikke en finesse. Afstem pipelinen med et graderet rammeværk som SLSA, kør builds i isolerede, netværksbegrænsede miljøer fra fastlåste værktøjskæder, og proxy tredjepartsafhængigheder gennem et internt repository, der scanner og godkender dem før brug. Gem signerede SBOM'er og proveniens uforanderligt i de år, arkivlovgivningen kræver, udrul kun signerede, digestidentificerede artefakter, og vær klar til at attestere over for revisorer og offentligheden, at softwaren i produktion er præcis det, der blev gennemgået og godkendt.

## Eksempler

**Startup.** Et startup på femten personer, der kører et lille monorepo, starter med sprognative buildværktøjer og hurtig feedback, hvilket er det rette kald i deres skala. Efterhånden som de vokser, kryber buildtider forbi fem minutter, og ingeniører begynder at skifte kontekst, mens de venter. I stedet for at hoppe til et tungt grafbuildværktøj tilføjer de en ekstern buildcache delt mellem udviklermaskiner og CI, som skærer de fleste builds til sekunder, fordi uændrede mål hentes, ikke genbygges. De adopterer lockfiler for hvert sprog, udruller containerimages efter digest i stedet for "latest"-tagget og slår automatisk udløb til for pull request-imagebuilds, så deres registerregning forbliver flad. Hele indsatsen tager et par uger og køber timers ingeniørtid tilbage hver dag.

**Stor virksomhed.** Et globalt finansielt servicefirma kører et stort monorepo på tværs af hundredvis af ingeniører og adopterer et grafbaseret buildsystem med ekstern caching og ekstern eksekvering, fordi finkornet inkrementalitet i deres skala genvinder langt mere ingeniørtid, end buildteamet koster. Hvert artefakt bygges hermetisk i et isoleret miljø, signeres og udgives til et administreret register med en SBOM og signeret proveniens vedhæftet. Udrulninger sker efter indholdsdigest, og en politikmotor nægter at køre ethvert image, hvis signatur ikke verificeres. Artefakter promoveres, aldrig genbygges, fra staging til produktion, så den binære, der bestod test, beviseligt er den, der betjener kunder. Når revisorer beder om at spore en produktionskomponent tilbage til gennemgået kilde, er forvaringskæden en forespørgsel, ikke en efterforskning.

**Offentlig sektor.** En national skattemyndighed, der moderniserer sine systemer, behandler forsyningskædeintegritet ved buildtidspunktet som et compliancekrav og afstemmer sin pipeline med et graderet rammeværk som SLSA. Builds kører i isolerede, netværksbegrænsede miljøer fra fastlåste værktøjskæder og låste afhængigheder, så outputtet er reproducerbart og uafhængigt verificerbart. Hvert artefakt bærer en signeret SBOM og proveniens, gemt uforanderligt i årevis for at opfylde arkivlovgivningen. Tredjepartsafhængigheder proxies gennem et internt repository, der scanner og godkender dem, før noget build kan bruge dem, hvilket holder uefterprøvet kode helt ude af netværket. Fordi myndigheden kun udruller signerede, promoverede artefakter identificeret ved digest, kan den attestere over for tilsynsmyndigheder og offentligheden, at softwaren, der behandler borgernes selvangivelser, er præcis det, der blev gennemgået og godkendt.

## Business case: motivation, ROI og TCO

Afkastet af build- og artefaktdisciplin viser sig først som genvundet ingeniørtid. Langsomme builds beskatter hver ingeniør ved hver ændring, og omkostningen akkumulerer på tværs af en stor organisation: at barbere minutter af et build, der kører tusinder af gange om dagen, genvinder personår årligt og, sværere at kvantificere men lige så reelt, holder ingeniører i flow i stedet for at skifte kontekst. En ekstern cache og god inkrementalitet betaler ofte sig selv inden for uger. Reproducerbare, promovér-én-gang-artefakter reducerer en hel klasse af "det virkede i staging"-hændelser og sænker ændringsfejlraten og gennemsnitlig genoprettelsestid, de leveringsmålinger, ledere allerede følger.

Det større, mindre synlige afkast er risikoreduktion. Signerede artefakter, SBOM'er og proveniens forvandler en forsyningskædehændelse fra en flerugers nødsituation til et afgrænset, timelangt svar, og de forvandler revisioner fra en brandøvelse til en forespørgsel. I regulerede og offentlige sammenhænge er den sporbarhed en forudsætning for overhovedet at operere, så investeringen er ikke valgfri, men strukturel. Den samlede ejeromkostning løber den anden vej, når I forsømmer dette: foranderlige artefakter og ureproducerbare builds ophobes til en ejendom, ingen fuldt kan gøre rede for, lager vokser ubegrænset uden opbevaringspolitik, og hver revision og hver hændelse koster mere, end den burde. For at fremlægge sagen for ledelsen så forbind buildhastighed med ingeniørgennemløb og artefaktintegritet med revisionsomkostning og bruddeksponering, som de begge allerede finansierer.

## Anti-mønstre og faldgruber

- **Genbyg pr. miljø:** at producere friske bytes til staging og produktion og kassere garantien for, at det testede artefakt er det udrullede.
- **Udrulning efter flydende tag:** at køre "latest" eller et foranderligt tag i stedet for et uforanderligt digest, så det, der kører, er uforudsigeligt og usporbart.
- **Ingen lockfil:** flydende versionsintervaller, der lader et build tavst trække forskellige eller ondsindede afhængigheder over tid.
- **Ufuldstændige cachenøgler:** at udelade et reelt input fra cachenøglen og producere forældede resultater, der spilder dages fejlfinding.
- **Usikret delt cache:** at lade upålidelige skribenter forgifte en ekstern cache, så forbrugere henter og kører kompromitterede output.
- **Ikke-deterministiske builds:** indlejrede tidsstempler, absolutte stier og ufastlåste værktøjer, der får output til at variere og besejrer verifikation.
- **For tidlig adoption af tungt værktøj:** at tage Bazel-klasse kompleksitet på, før buildgrafen er stor nok til at retfærdiggøre det.
- **SBOM og proveniens som eftertanke:** at rekonstruere forsyningskædemetadata efter buildet, når det er dyrt og upålideligt, i stedet for at generere dem i buildet.
- **Ubegrænset opbevaring:** aldrig at lade gamle artefakter udløbe, til lageromkostning og langsomme opslag tvinger en panisk oprydning.

## Modenhedsmodel

- **Niveau 1, Opstart:** Builds er ad hoc scripts, ingen ejer, ofte kørt fra udviklermaskiner. Output er ikke-deterministisk, afhængigheder flyder uden lockfiler, artefakter genbygges pr. miljø og udrulles efter foranderligt tag, og der er ingen fælles cache, ingen signering og ingen materialefortegnelse.
- **Niveau 2, Udvikling:** Nogle teams har flyttet builds ind i CI fra en indtjekket definition og adopteret lockfiler, men praksis er inkonsistent på tværs af organisationen. Artefakter lander måske i et administreret repository med basal versionering, og en lokal eller simpel ekstern cache fremskynder almindelige builds, men genbygninger pr. miljø sker stadig, og proveniens er pletvis.
- **Niveau 3, Standardisering:** Reproducerbare, stort set hermetiske builds er dokumenteret og håndhævet i hele organisationen, med fastlåste værktøjskæder og en fælles ekstern cache, hvis nøgler hasher alle reelle input. Artefakter er uforanderlige, indholdsadresserede, semantisk versionerede, bygget én gang og promoveret overalt, signerede og leveret med en SBOM. Cacheadgang er kontrolleret, og opbevaringspolitikker anvendes ensartet på tværs af teams.
- **Niveau 4, Styring:** Buildejendommen måles og styres mod baselines. Buildtider, cache-hit-rater, udviklerfeedbacktid og lageromkostning følges med eksplicitte mål, regressioner udløser handling, og signatur- og proveniensverifikation håndhæves ved udrulning, så et fejlet tjek blokerer release. Forsyningskædeintegritet ved buildtidspunktet vurderes mod et graderet rammeværk som SLSA, og tallene driver, hvor I investerer næste gang.
- **Niveau 5, Orkestrering:** Build-, cache-, artefakt- og forsyningskædepraksis forbedres løbende og er integreret på tværs af organisationen. Værktøj, opbevaring og sikkerhedsholdning tilpasser sig, efterhånden som I lærer af hændelser og revisioner, ekstern eksekvering og caching justeres, efterhånden som kodebasen udvikler sig, og buildtidsintegritet er vævet ind i den bredere sikre udviklingslivscyklus frem for boltet på bagefter.

## Idéer til drøftelse

1. Hvad er jeres nuværende mediane og værste-tilfælde lokale buildtid, og hvad ville en ekstern cache gøre ved hver?
2. Hvilke af jeres artefakter udrulles efter foranderligt tag i dag, og hvad skulle der til for at udrulle hvert efter digest?
3. Hvor retfærdiggør jeres buildgraf tungere værktøj, og hvor ville det værktøj koste mere, end det sparer?
4. Hvem kan skrive til jeres delte buildcache, og hvad forhindrer en forgiftet post i at nå produktion?
5. Kan I producere en signeret SBOM for det sidste, I leverede, og hvis ikke, hvad er det mindste skridt derhen?
6. Hvad er jeres opbevaringspolitik for buildartefakter, og hvad koster lager jer i dag versus hvad det burde?

## Vigtigste pointer

- Buildet er det første trin i levering: finansiér dets hastighed og korrekthed som produktionsanliggender, fordi alt nedstrøms arver dets fejl.
- Gør builds reproducerbare og, hvor det er muligt, hermetiske, med fastlåste værktøjskæder og lockfiler, så det artefakt, I reviderer, beviseligt er det, I leverer.
- Cache og byg inkrementelt, lokalt og eksternt, men hash hvert reelt input og sikr cachen, fordi en delt cache er en delt tillidsgrænse.
- Byg hvert artefakt én gang, gør det uforanderligt og indholdsadresseret, versionér det meningsfuldt, og promovér netop det artefakt på tværs af miljøer.
- Generér proveniens, signaturer og en SBOM ved buildtidspunktet, og gem artefakter med opbevaring og adgangskontrol, så forsyningskædeintegritet og revisionsparathed bliver et biprodukt af normalt arbejde.

## Referencer og videre læsning

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google: Lessons Learned from Programming Over Time*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Peter Smith, *Software Build Systems: Principles and Experience*
- The Open Source Security Foundation, *SLSA: Supply-chain Levels for Software Artifacts* (specification)
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
