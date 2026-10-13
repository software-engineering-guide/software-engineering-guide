# 3.4 Dataarkitektur og lagring

## Overblik og motivation

Data overlever kode. Applikationer omskrives hvert par år, men de data, de styrer (kundeposter, finansielle hovedbøger, ydelseshistorik, sundhedsjournaler), består i årtier. Det er ofte organisationens mest værdifulde og mest regulerede aktiv. Dataarkitektur er disciplinen at beslutte, hvordan data modelleres, hvor de gemmes, hvordan de holdes konsistente, hvordan de udvikler sig, og hvordan de serveres hurtigt nok i stor skala. For en stor organisation er disse beslutninger fundamentale. Dit valg af lagringsmotorer og datamodeller begrænser, hvad virksomheden kan gøre, hvor hurtigt den kan bevæge sig, og hvad det koster, i systemets hele levetid.

Indsatsen er højest i virksomheder og det offentlige på grund af skala, levetid og regulering. En banks transaktionslager må aldrig miste eller dobbelttælle en øre. Et offentligt register skal opbevare poster i lovbestemte perioder og bevise deres integritet over for revisorer. Et sundhedssystem skal håndhæve finkornet adgang og residensregler. Samtidig betjener disse organisationer enorme læse- og skrivevolumener og har ikke råd til, at hver forespørgsel rammer en enkelt [relationel database](https://en.wikipedia.org/wiki/Relational_database). Så dataarkitektur må forene korrekthed og holdbarhed med ydeevne og skala, og gøre det, mens skemaet bliver ved med at ændre sig for at møde nye påbud.

Dette kapitel dækker de store lagringsparadigmer og hvornår man bruger hvert, disciplinen [polyglot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence), datamodellering og det ofte undervurderede problem med skemaudvikling og migrering, [caching](https://en.wikipedia.org/wiki/Cache_(computing)) og [CDN'er](https://en.wikipedia.org/wiki/Content_delivery_network) (content delivery networks) med det berygtede svære problem med invalidering, og hvordan transaktioner, låsning og samtidighed opfører sig, når du presser dem til skala. Den røde tråd er enkel: der findes ingen universel database. Der er afvejninger, og god dataarkitektur betyder at vælge dem bevidst, én arbejdsbyrde ad gangen.

## Grundprincipper

- **Modellér data efter adgangsmønstrene, ikke omvendt.** Design lagring omkring, hvordan data vil blive læst og skrevet, ikke omkring en abstrakt "korrekt" model.
- **Der er ingen database, der hersker over dem alle.** Forskellige arbejdsbyrder vil have forskellige motorer; polyglot persistence er normalt i stor skala.
- **Korrekthed først for registersystemer.** For autoritative data er holdbarhed og konsistens ufravigelige; optimér ydeevne omkring dem, ikke igennem dem.
- **Skemaet vil ændre sig, så planlæg for det.** Migreringer er en førsteklasses, løbende ingeniøraktivitet, ikke en engangsopgave.
- **Eje dine data bag en tjenestegrænse.** Hver afgrænset kontekst (en selvstændig domænemodel med sin egen eksplicitte grænse) ejer sine data; at dele en database kobler teams og ødelægger autonomi.
- **Caching er et korrekthedsproblem forklædt som en ydeevnegevinst.** Hver cache indfører forældelse og invalideringsrisiko; behandl den bevidst.
- **Denormalisering er en afvejning, ikke en synd.** At duplikere data for læseydeevne er legitimt, hvis du ejer konsistenskonsekvenserne.
- **Konsistens og skala bytter.** Jo stærkere den transaktionelle garanti, desto sværere er den at distribuere; køb kun det, arbejdsbyrden har brug for.

## Anbefalinger

### Vælg lagringsparadigmet ud fra arbejdsbyrden

Match hver arbejdsbyrde til den model, der passer. **Relationelle** databaser giver stærk konsistens, joins og modne transaktioner; de er standarden for registersystemer og alt med komplekse integritetsregler. **[Dokument](https://en.wikipedia.org/wiki/Document-oriented_database)**lagre passer til hierarkiske, skemafleksible data læst som en enhed (en hel ordre, en hel profil). **[Nøgle-værdi](https://en.wikipedia.org/wiki/Key-value_database)**lagre giver ekstrem hastighed til simple opslag (sessioner, feature flags, caches). **[Graf](https://en.wikipedia.org/wiki/Graph_database)**databaser udmærker sig, hvor relationer er forespørgslen (svindelringe, organisationsdiagrammer, rettigheder, forsyningskæder). **[Kolonne](https://en.wikipedia.org/wiki/Column-oriented_DBMS)**lagre driver analytiske forespørgsler, der skanner få kolonner over milliarder af rækker (datavarehuse, rapportering). **[Tidsserie](https://en.wikipedia.org/wiki/Time_series_database)**databaser optimerer til tilføjelsestunge, tidsstemplede data (målinger, telemetri, [tingenes internet](https://en.wikipedia.org/wiki/Internet_of_things) (IoT)-sensorer, markedsdata). Modstå at tvinge én motor til at gøre hvert job. At bruge en relationel database som kø, eller et dokumentlager som hovedbog, inviterer til smerte.

### Adoptér polyglot persistence bevidst

Store systemer bruger legitimt flere lagre: et relationelt registersystem, et søgeindeks, en cache, et analysevarehus og måske en graf- eller tidsseriemotor. Dette er **polyglot persistence**, og det er det rette mønster, når arbejdsbyrder reelt adskiller sig. Omkostningen er operationel, fordi du nu har flere motorer at drive, sikre, tage backup af og bemande. Styr den omkostning ved at behandle hvert lager som ejet af en tjeneste, standardisere driftsværktøj og holde antallet af teknologier til dem, der fortjener deres plads. Vær på vagt over for at adoptere en ny database til hvert mindre behov. Hver er en permanent driftsforpligtelse.

### Modellér data, og behandl skemaudvikling som løbende

Invester i datamodellering på forhånd for registersystemer. Normalisér for at beskytte integritet, og denormalisér derefter selektivt til dokumenterede læsehotspots. Uanset modellen **udvikler skemaet sig for evigt**, så gør migreringer sikre og rutinemæssige. Brug versionerede, automatiserede, kun-fremad-migreringsscripts checket ind i versionsstyring og anvendt gennem udrulningspipelinen. Til ændringer uden nedetid på store tabeller så brug **expand-contract (parallel change)**-mønstret: tilføj den nye kolonne eller tabel, backfill og dobbeltskriv, migrér læsere, og fjern så den gamle form. Aldrig en enkelt brydende alter. Gør skemaændringer bagudkompatible på tværs af udrulninger, så gammel og ny kode kører på samme tid. I event-sourcede eller beskedbaserede systemer så versionér dine hændelses- og beskedskemaer eksplicit og understøt upcasting af gamle hændelser (at transformere dem til det nuværende skema ved læsning).

### Design caching og invalidering med åbne øjne

Caching og CDN'er er de ydeevneværktøjer med størst løftestang. Et CDN serverer statisk og cachebart indhold fra kanten nær brugerne, og applikationscaches skåner databasen for gentagne læsninger. Men det svære er invalidering: at vide, hvornår cachede data er forældede. Vælg en strategi pr. tilfælde. Brug tidsbaseret udløb (TTL), hvor lidt forældelse er acceptabel og simplest. Brug eksplicit invalidering eller write-through, hvor friskhed betyder noget. Brug cache-aside, hvor applikationen styrer udfyldningen. Sæt TTL'er bevidst, værn mod **cache-stampeder** (mange klienter, der genopbygger den samme udløbne post på én gang) med låsning eller anmodningssammenlægning, og forebyg **thundering herds** på kolde caches. Cache aldrig data, hvis forældelse kunne forårsage en korrekthedsfejl eller et compliance-svigt (rettigheder, saldi, samtykke), uden en eksplicit, testet invalideringssti. Behandl cachenøgler, TTL'er og invalidering som designede artefakter, ikke tilfældig konfiguration.

### Styr transaktioner, låsning og samtidighed for skala

Forstå isolationsniveauer og vælg det svageste, der stadig er korrekt for hver transaktion, fordi højere isolation koster samtidighed. Foretræk **[optimistisk samtidighed](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)** (versionstjek ved skrivning) til arbejdsbyrder med lav konkurrence og tung læsning, og ræk kun ud efter pessimistisk låsning under reel varm konkurrence, og hold låse korte og konsekvent ordnede for at undgå deadlocks. Efterhånden som du skalerer, bliver en enkelt skrivbar database flaskehalsen. Indfør læsereplikaer til læseskalering (accepter replikeringsforsinkelse), og **[shard](https://en.wikipedia.org/wiki/Shard_(database_architecture))/partitionér** efter en nøgle, der spreder belastningen jævnt og holder relaterede data sammen for at undgå transaktioner på tværs af shards. Husk, at sharding bytter nem join på tværs af shards og [ACID](https://en.wikipedia.org/wiki/ACID)-transaktioner (Atomicity, Consistency, Isolation, Durability) over flere shards væk, hvilket ofte er grunden til, at sagaer og denormalisering dukker op. Skub disse teknikker ind kun efterhånden som arbejdsbyrden kræver det. For tidlig sharding tilføjer permanent kompleksitet.

## Afvejninger: fordele og ulemper

| Lagertype | Bedst til | Styrker | Svagheder |
|---|---|---|---|
| Relationel | Registersystemer, komplekse integritetsregler | ACID, joins, modent værktøj | Sværere at skalere skrivninger horisontalt |
| Dokument | Aggregatlæsninger, fleksibelt skema | Hurtig læsning/skrivning af hele objekter, fleksibel | Svage joins/transaktioner på tværs af dokumenter |
| Nøgle-værdi | Sessioner, caches, simple opslag | Ekstrem hastighed og skala | Ingen forespørgsler ud over nøglen |
| Graf | Relationstunge forespørgsler | Hurtige gennemløb, udtryksfuld | Nichedriftsfærdigheder, skaleringsgrænser |
| Kolonne | Analyse, rapportering | Hurtige aggregerede skanninger, komprimering | Dårlig til rækkeniveau-transaktionelle skrivninger |
| Tidsserie | Målinger, telemetri, IoT | Effektiv tilføjelse og tidsforespørgsler | Snævert formål |

Den dominerende afvejning er konsistens og rig forespørgsel versus horisontal skalerbarhed og hastighed. Relationelle systemer giver de stærkeste garantier og de mest fleksible forespørgsler, men er sværest at skalere skrivninger på tværs af mange maskiner. [NoSQL](https://en.wikipedia.org/wiki/NoSQL)-familier (ikke-relationelle) slækker på joins, transaktioner eller skema for at vinde skala og hastighed. Caching bytter friskhed for latens. Sharding bytter transaktioner på tværs af partitioner for skrivegennemløb. Intet af dette er universelt rigtigt. Kunsten er at placere hver arbejdsbyrde på det punkt af kurven, dens korrekthed og ydeevnebehov faktisk kræver.

## Spørgsmål til drøftelse med dit team

1. **Kan alle for hvert kritisk datasæt navngive det ene registersystem, eller bliver caches og projektioner stille behandlet som sandhed?** Data overlever kode, og de mest skadelige datahændelser kommer af drift: en cache, et søgeindeks eller en læseprojektion forveksles med autoritativ og afviger stille fra den reelle kilde. I et stort team sker det, når ejerskab er uklart, og flere tjenester skriver overlappende kopier, så ingen kan sige, hvilken værdi der er korrekt under en hændelse. Tag et kort over jeres vigtige data med og, for hvert, det enkelte lager, der er autoritativt, plus de afledte kopier, der skal kunne genopbygges fra det. I finans og det offentlige er det at kunne bevise, hvilken post der er den juridiske kilde, og rekonstruere resten, ofte et regulatorisk krav, ikke en bekvemmelighed. Alt, I ikke kan genopbygge fra registersystemet, er selv et registersystem, uanset om I mente det.

2. **Hvad koster hver databasemotor i jeres landskab faktisk at drive, sikre og tage backup af, og fortjener hver stadig sin plads?** Polyglot persistence er rigtigt, når arbejdsbyrder reelt adskiller sig, men hver motor er en permanent driftsforpligtelse: patching, backups, overvågning, sikkerhedsgennemgang og personale, der kender den kl. 3 om natten. En stor organisation kan drive ind i en zoologisk have af lagre adopteret til én feature hver, og den marginale tilføjer omkostning for evigt, mens den betjener en arbejdsbyrde, et lager, I allerede kører, kunne håndtere. List hver motor, den arbejdsbyrde, der retfærdiggør den, og hvem der er på vagt for den, og markér derefter enhver adopteret til et behov, et primært lager nu kunne møde. Ny databaseadoption bør klare en høj barre, fordi at fjerne en senere betyder endnu en migrering. At standardisere driftsværktøj på tværs af de lagre, I beholder, er, hvordan I holder omkostningen nede uden at tvinge én motor til at gøre hvert job.

3. **Hvor kan en bruger læse en forældet værdi fra en replika lige efter sin egen skrivning, og bryder det et løfte, I gav vedkommende?** Læsereplikaer skalerer læsninger, men halter efter primæren, så en bruger, der opdaterer en profil og straks genindlæser, kan se den gamle værdi, hvilket læses som en fejl eller, for en saldo eller et samtykkeflag, et compliance-svigt. Beslut pr. flow, om læs-dine-skrivninger betyder noget, og dirigér de læsninger til primæren eller brug en sessionskonsistensmekanisme. Tag listen over flows serveret fra replikaer med, og markér hvilke en bruger handler på umiddelbart efter at have skrevet. For saldi, rettigheder og samtykke så behandl forældede læsninger som korrekthedssvigt, ikke kosmetiske. Pointen er at købe den konsistens, hver arbejdsbyrde faktisk har brug for, og at gøre den forældelse, I accepterer, eksplicit frem for tilfældig.

4. **Kan I ændre skemaet for jeres største, travleste tabel i dag uden nedetid, og hvem har faktisk øvet expand-contract-trinene?** Skemaet udvikler sig for evigt, og den fejl, der gør mest ondt, er en big-bang-alter, der låser en kæmpe tabel, fryser tjenesten og ikke kan rulles rent tilbage. I et stort team multipliceres risikoen, fordi flere tjenester læser den samme form, så en brydende ændring kræver, at gammel og ny kode kører side om side på tværs af en trindelt udrulning. Det modstridende træk er hastighed: en enkelt alter er hurtig at skrive, mens expand-contract (tilføj den nye form, backfill, dobbeltskriv, migrér læsere, drop den gamle form) er flere trin og mere tålmodighed. Tag jeres største tabel med, et ærligt skøn over, hvor længe en naiv alter ville låse den, og en specifik migrering, nogen har kørt fra ende til anden i en prøve frem for i teorien. I virksomheds- og offentlige systemer, der kører kontinuerligt og bærer lovbestemte tilgængelighedsmål, er nedetid for en migrering et brud, så expand-contract-disciplinen er prisen for overhovedet at få lov til at ændre skemaet.

5. **Hvilke cachede eller replikerede værdier ville, hvis serveret forældede, forårsage et compliance- eller sikkerhedssvigt frem for et kosmetisk, og er hver af de invalideringsstier testet?** Caching er et korrekthedsproblem i et ydeevnekostume: faren er ikke langsomhed, men at servere en rettighed, saldo, samtykkeflag eller adgangsbeslutning, efter den ændrede sig. For en stor organisation er faren diffus, fordi caches og kantlag akkumuleres på tværs af teams, og ingen enkelt person kan liste, hvad der er cachet hvor, eller hvornår det ryddes. Spændingen er reel: aggressiv caching og lange TTL'er køber latens og beskytter databasen, mens streng friskhed koster begge. Tag en opgørelse over cachede og CDN-serverede data med, markeret for hvilke poster der bærer en compliance- eller sikkerhedskonsekvens, plus dokumentation for, at invalideringsstien for hver af dem er blevet brugt i praksis frem for blot konfigureret. I regulerede og offentlige sammenhænge er en forældet samtykke- eller berettigelsesværdi et reviderbart svigt, så de poster har brug for en eksplicit, testet invalideringssti, ellers bør de slet ikke caches.

6. **Hvad er jeres opbevarings-, arkiverings- og dataresidensstrategi for hvert autoritativt lager, og kan I bevise det over for en revisor?** Data overlever kode og ofte det team, der skrev den, så ubegrænset vækst og vage residensregler bliver stille det problem, ingen ejer, til en tabel er uhåndterlig, eller en post sidder i den forkerte jurisdiktion. En stor organisation spænder over mange lagre og regioner, og de modstridende hensyn er omkostning (varmt lager er dyrt, så arkivér og lagdel), ydeevne (oppustede tabeller sinker alt) og juridisk pligt (lovbestemte opbevaringsgulve og residensloft, der kan være i konflikt). Tag pr. autoritativt datasæt opbevaringsperioden, hvor dataene fysisk bor, arkiverings- og sletningsmekanismen og navnet på den ansvarlige med. For virksomheds- og især offentlige systemer er opbevaring og residens som regel juridiske påbud med revisions- og suverænitetskrav, så at kunne bevise, hvor hver post bor, hvor længe den opbevares, og hvornår den destrueres, er en licens til at operere, ikke en finesse.

## Sektorperspektiv

**Startup.** Kør én database og modstå zoologisk have. Et enkelt administreret relationelt lager giver dig transaktioner, én ting at tage backup af og ét sted at ræsonnere om konsistens, hvilket netop er, hvad et team på tre kan holde i hovedet. Tilføj en cache, en læsereplika eller et søgeindeks først, når en specifik langsom forespørgsel eller reelt læsevolumen tvinger det, så kompleksitet ankommer med en betalende grund. Hold migreringer versionerede fra dag ét, fordi at eftermontere migreringsdisciplin på et live produkt er langt sværere end at starte med den.

**Lille virksomhed.** Du har ingen databasespecialist og ingen tid til at drive flere motorer, så foretræk et administreret lager og lad din platformsudbyder håndtere backups, patching og replikering. Behandl lagervalg som en købsbeslutning: vælg den kedelige, veltilsluttede motor, dine værktøjer allerede integrerer med, frem for den hurtigste på en benchmark. Sæt en simpel opbevarings- og backuppolitik, du faktisk kan verificere, og cache aldrig noget bundet til penge eller tilladelser uden en klar måde at rydde det på, fordi en forældet pris eller rettighed koster dig en kunde.

**Stor virksomhed.** Kerneudfordringen er polyglot persistence på tværs af mange teams: et relationelt registersystem plus søgning, cache, varehus og måske graf- eller tidsseriemotorer, hver ejet af en tjeneste frem for delt. Standardisér driftsværktøj, backup og overvågning på tværs af de lagre, du beholder, hold adoption af nye motorer til en høj barre, og gør expand-contract-migreringer og eksplicit cacheinvalidering til standarden. Styr landskabet som en portefølje med klart dataejerskab, så ingen motor overlever den arbejdsbyrde, der retfærdiggjorde den, og intet team er koblet gennem en fælles database.

**Offentlig sektor.** Dataresidens, lovbestemt opbevaring og påviselig integritet former hvert valg. Provisionér hvert lager i suveræne regioner, konfigurér CDN'er til kun at cache ikke-personlige data, og hold en uforanderlig revisionshistorik for poster, der skal kunne rekonstrueres for tilsynsmyndigheder. Migreringer påbudt af ny lovgivning skal anvendes bagudkompatibelt gennem pipelinen, så tjenesten forbliver tilgængelig gennem lovgivningsmæssige frister, og registersystemet skal kunne identificeres, så du kan bevise, hvilken værdi der er den juridiske kilde, og genopbygge hver afledt kopi fra det.

## Eksempler

**Startup.** Et seed-stage startup kører alt på en enkelt administreret PostgreSQL-instans og modstår trangen til at tilføje en separat søgemotor, cache og varehus, før det har brug for dem. Én database betyder én ting at tage backup af, ét sted at ræsonnere om konsistens og transaktioner, der bare virker, hvilket betyder noget, når hele teamet er tre ingeniører. De tilføjer en Redis-cache og en læsereplika først, når en specifik langsom forespørgsel og reelt læsevolumen retfærdiggør det, så kompleksitet ankommer med en betalende grund frem for forud for en.

**Stor virksomhed.** En detailbank holder sin autoritative hovedbog i en stærkt konsistent relationel database: hver postering er en ordentlig ACID-transaktion, shardet efter kontointerval til skrivningsskala. Rundt om den sidder et polyglot landskab: et søgeindeks til kundeopslag, en Redis-cache (write-through, kort TTL) til kontooversigter i mobilappen, et kolonnevarehus til regulatorisk og analytisk rapportering og en grafdatabase til svindeldetektion i transaktionsnetværk. Skemaændringer til hovedbogen bruger expand-contract med dobbeltskrivninger, så det døgnåbne system aldrig tager nedetid for en migrering.

**Offentlig sektor.** Et nationalt køretøjsregister gemmer autoritative poster i et relationelt registersystem med lovbestemt opbevaring og fuld revisionshistorik. Offentlige "tjek et køretøj"-opslag serveres fra en læsereplika og en kantcache med kort TTL, fordi lidt forældede offentlige data er acceptable, og læsevolumen dværger skrivninger. Lov om dataresidens kræver, at alle poster forbliver i landet, så hvert lager provisioneres i suveræne regioner, og CDN'et er konfigureret til kun at cache ikke-personlige data. Migreringer til at tilføje nye felter påbudt af transportpolitik anvendes bagudkompatibelt gennem pipelinen, så tjenesten forbliver tilgængelig under lovgivningsmæssige frister.

## Business case: motivation, ROI og TCO

Dataarkitekturbeslutninger har blandt de længste og største omkostningshaler i software, fordi data og deres skema er det sværeste at ændre, når først systemer og integrationer afhænger af dem. Indførelsesomkostningen ved god praksis (bevidst lagervalg, disciplinerede migreringer, designet caching og passende sharding) er mest senioringeniørtid og noget ekstra driftsværktøj. Omkostningen ved *ikke* at indføre den viser sig som en enkelt overbelastet database, der kvæler hele virksomheden, nød-replatforming, når det forkerte lager opdages for sent, forlængede nedbrud fra en fejlslagen migrering og, mest skadeligt, datakorruption eller et compliance-brud fra en fejlinvalideret cache eller en tabt transaktion.

Argumentér over for ledelsen i termer af skalerbarhedsmargen, hændelsesrisiko og regulatorisk eksponering. De rette lagringsvalg er det, der lader virksomheden vokse læse- og skrivevolumen uden en omskrivning. Disciplinerede migreringer er det, der lader skemaet holde trit med nye påbud uden nedetid. Korrekt caching er det, der leverer hurtige brugeroplevelser uden stille forældelsesfejl. Kvantificér TCO over systemets liv. En enkelt veludvalgt dataarkitektur undgår den tilbagevendende omkostning ved at arbejde sig omkring en dårlig, og én forebygget datakorruptionshændelse overstiger typisk hele omkostningen ved at gøre det godt. I regulerede sektorer er evnen til at bevise dataintegritet og residens ikke et omkostningscenter, men en licens til at operere.

## Anti-mønstre og faldgruber

- **Fælles database på tværs af tjenester.** Flere tjenester, der læser og skriver ét skema, kobler teams og gør hver ændring til en koordinationskrise.
- **Én database til alt.** At tvinge analyse, køer, søgning og transaktioner ind på en enkelt relationel motor, til den kollapser.
- **Big-bang-migreringer.** Enkelte brydende skemaændringer, der kræver nedetid og ikke kan rulles sikkert tilbage.
- **Caching uden invalideringsstrategi.** Forældede data serveret på ubestemt tid, eller korrekthedsfejl, fordi ingen ejer, hvornår cachen ryddes.
- **For tidlig sharding.** At distribuere data, før belastningen kræver det, og permanent miste joins og transaktioner uden gevinst.
- **At ignorere replikeringsforsinkelse.** At læse sin egen skrivning fra en forsinket replika og få forældede data, hvilket bryder brugerforventninger.
- **Ubegrænset datavækst.** Ingen arkiverings- eller opbevaringsstrategi, så tabeller vokser, til ydeevne og omkostning bliver uholdbare.
- **At gemme afledte data som sandhed.** At behandle en cache, et indeks eller en projektion som registersystemet og så opdage, at det er drevet.

## Modenhedsmodel

- **Niveau 1: Opstart.** Én database bruges til alle formål. Skemaændringer er manuelle og ad hoc, uden migreringsdisciplin. Caching er tilfældig, og invalidering er en eftertanke. Ydeevneproblemer løses reaktivt ved at købe en større maskine, og ingen kan pålideligt navngive registersystemet for et givet datasæt.
- **Niveau 2: Udvikling.** Nogle lagringsvalg er bevidste, og en cache eller et varehus er dukket op, men praksis varierer fra team til team. Migreringer er versionerede, men kræver nogle gange nedetid, og expand-contract bruges af den, der tilfældigvis kender det. Flere tjenester deler stadig en database, og cachingstrategier adskiller sig fra team til team.
- **Niveau 3: Standardisering.** Polyglot persistence er matchet til arbejdsbyrder, hvert lager ejet af en tjeneste og aldrig delt. Automatiserede, bagudkompatible expand-contract-migreringer uden nedetid er den dokumenterede, håndhævede standard i hele organisationen. Cachingstrategier, TTL'er og invalideringsstier er eksplicitte designartefakter, og det enkelte registersystem for hvert datasæt er dokumenteret, med afledte kopier der kan genopbygges fra det.
- **Niveau 4: Styring.** Datalandskabet måles og styres mod baselines. I følger migreringsvarighed og tilbagerulningsrate, replikeringsforsinkelse mod krav om læs-dine-skrivninger, cache-hitrate og forældelseshændelser, driftsomkostning pr. lager og forespørgselslatens ved målpercentiler og handler derefter på tallene. Opbevaring og residens revideres mod lovbestemte krav, korrektheden af afledte data verificeres løbende, og hver motor skal retfærdiggøre sin omkostning mod den arbejdsbyrde, den betjener.
- **Niveau 5: Orkestrering.** Dataarkitektur forbedres løbende og er integreret med kapacitets-, omkostnings- og risikoplanlægning i hele organisationen. Sharding-, caching- og konsistensvalg genbalanceres pr. arbejdsbyrde, efterhånden som adgangsmønstre og omkostning skifter, og lagre, der ikke længere fortjener deres plads, afvikles gennem planlagte migreringer. Skemaudvikling, arkivering og residens er fuldt automatiserede og adaptive, så landskabet omformer sig til nye påbud og belastning uden nød-replatforming.

## Idéer til drøftelse

1. Hvilke af jeres nuværende lagre udfører et job, de ikke var designet til, og hvad ville den rette motor være?
2. Kan I foretage en skemaændring på jeres største tabel i dag uden nedetid? Hvis ikke, hvorfor ikke?
3. Hvor cacher jeres system data, hvis forældelse kunne forårsage et compliance- eller korrekthedssvigt?
4. Hvilke tjenester deler en database, og hvad ville der skulle til for at give hver sin egen?
5. Hvor er en enkelt skrivbar database jeres skaleringsloft, og er læsereplikering eller sharding det rette næste skridt?
6. Hvad er jeres opbevarings- og arkiveringsstrategi, og hvem er ansvarlig for den?

## Vigtigste pointer

- Data overlever kode; lagrings- og modelleringsbeslutninger begrænser virksomheden i systemets hele liv.
- Match hver arbejdsbyrde til det lagringsparadigme, der passer til dens adgangsmønster; forvent polyglot persistence i stor skala.
- Giv hver tjeneste ejerskab af sine data; kobl aldrig teams gennem en fælles database.
- Behandl skemaudvikling som løbende og brug bagudkompatible expand-contract-migreringer uden nedetid.
- Caching er et korrekthedsproblem: design TTL'er, invalidering og stampede-beskyttelse bevidst, og cache aldrig compliance-kritiske data uden en testet invalideringssti.
- Køb kun de konsistens- og transaktionsgarantier, hver arbejdsbyrde har brug for; sharding og replikering bytter transaktioner på tværs af partitioner for skala.

## Referencer og videre læsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Pramod Sadalage and Martin Fowler, *NoSQL Distilled*
- Pramod Sadalage and Scott Ambler, *Refactoring Databases: Evolutionary Database Design*
- C. J. Date, *An Introduction to Database Systems*
- Joe Celko, *SQL for Smarties*
- Vlad Mihalcea, *High-Performance Java Persistence* (transactions, isolation, concurrency)
- Eric Evans, *Domain-Driven Design* (bounded contexts and data ownership)
- Werner Vogels, "Eventually Consistent"
