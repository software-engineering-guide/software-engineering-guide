# 3.15 Caching og indholdslevering

## Overblik og motivation

En [cache](https://en.wikipedia.org/wiki/Cache_(computing)) er en kopi af data, opbevaret et sted, der er hurtigere eller tættere på end originalen, så du kan besvare en anmodning uden at gøre det fulde, dyre arbejde igen. Næsten ethvert system, der føles hurtigt, er hurtigt på grund af caching. Databaseforespørgslen, der ville tage 40 millisekunder, returnerer på under én, når dens resultat allerede ligger i hukommelsen. Billedet, der ville krydse et hav, serveres fra en maskine i samme by. Caching er den teknik med størst løftestang for ydeevne, du har, og den er også den, der mest sandsynligt giver dig en subtil, vanvittig fejl.

Dette kapitel går i dybden med cachingstrategi. Kapitel 3.4 (dataarkitektur og lagring) introducerer caches og content delivery networks som ét lagringsanliggende blandt mange, og kapitel 3.13 (netværk og konnektivitet) dækker den netværkssti, de kører på. Her får du beslutningerne: hvor en cache skal placeres, hvordan den skal nøgles, hvornår den skal invalideres, hvordan den skal beskyttes under belastning, og hvordan du ræsonnerer om den forældelse, du bytter for hastighed. Caching rører ved ydeevneteknik (kapitel 2.16), skalerbarhed og robusthed (kapitel 3.5), de delvise fejl i distribuerede systemer (kapitel 3.3) og, fordi en forgiftet cache kan servere et angreb til tusinder af brugere, applikationssikkerhed (kapitel 4.2).

Motivationen koger ned til tre løftestænger. Caching skærer latens, så brugerne venter mindre. Den skærer belastning, så din oprindelsesserver betjener mere trafik på den samme hardware. Og den skærer omkostning, fordi en anmodning besvaret ved kanten aldrig rører din database, din beregning eller din egress-regning. For store teams er en fælles cachingstrategi forskellen mellem en platform, der skalerer forudsigeligt, og en, hvor hver tjeneste genopfinder invalidering og får den forkert. I virksomheds- og offentlige systemer, hvor trafikken spidser ved indberetningsfrister og lanceringsdage, er en veldesignet cache ofte det, der står mellem en fungerende portal og en offentlig fiasko.

## Grundprincipper

- Cache for at skære latens, belastning og omkostning, og vid hvilken af dem du køber.
- Placér caches på det rette lag i hierarkiet, tættest på hvor de hjælper mest.
- Behandl invalidering som den svære del; design nøgler og levetider, før du cacher.
- Beskyt cachen under belastning med sammenlægning, jitter og forsvar mod stampede.
- Vælg et skrivemønster bevidst: konsistens og hastighed trækker mod hinanden.
- Mål hitrate, forældelse og oprindelsesbelastning; en ikke-målt cache er et ansvar.
- Behandl cachet indhold som en angrebsflade; en forgiftet cache serverer alle.

## Anbefalinger

### Forstå cachehierarkiet

Caching er ikke én ting ét sted. Det er et hierarki af kopier, hver tættere på brugeren end den forrige, og du designer på tværs af det hele. Nærmest brugeren er klientcachen: browserens HTTP-cache, en mobilapps lokale lager, en cache i processens hukommelse. Dernæst er [content delivery network](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN), en flåde af servere fordelt rundt i verden, der holder kopier af dit indhold ved netværkets kant, nær brugerne. Bag det sidder reverse proxy- eller gateway-cachen, en delt cache foran dine servere. Så applikationscachen: et hurtigt nøgle-værdi-lager såsom et in-memory data grid, der holder beregnede resultater, sessioner og gengivne fragmenter. Til sidst databasens egen forespørgsels- og bufferlager, der holder varme sider i hukommelsen, så disken rammes sjældnere.

Hvert lag tjener et særskilt job: klientcachen eliminerer anmodningen helt, CDN'et absorberer global læsetrafik, reverse proxyen skærmer din oprindelsesserver mod gentaget identisk arbejde, applikationscachen sparer genberegning, og databasecachen holder lageret responsivt. En anmodning, der misser hvert lag og når databasen, er den langsomste, dyreste sti, du har, så hierarkiets pointe er at besvare så langt oppe og ude, som du sikkert kan. Design det som et system, for et cachet fragment i applikationslaget og en forældet CDN-kopi over det kan være uenige på måder, der forvirrer brugerne.

### Behandl invalidering som det svære problem

Der er en gammel joke om, at de to sværeste problemer i datalogi er at navngive ting, [cacheinvalidering](https://en.wikipedia.org/wiki/Cache_invalidation) og off-by-one-fejl. Jokken holder, fordi invalidering reelt er svær: en cache er en kopi, og i det øjeblik originalen ændres, er hver kopi en potentiel løgn. Du har tre brede strategier. Tidsbaseret udløb med en time to live (TTL), den varighed en post forbliver gyldig, før den anses for forældet, er den simpleste: du accepterer afgrænset forældelse og lader poster ældes ud. Eksplicit invalidering rydder eller opdaterer poster, når de underliggende data ændres, hvilket er præcist, men kræver, at du kender hvert sted, en kopi bor. Hændelsesdrevet invalidering abonnerer caches på ændringshændelser, så de opdaterer sig selv, hvilket skalerer bedre på tværs af mange caches, men tilføjer en beskedafhængighed.

De fleste reelle systemer blander disse: korte TTL'er til data, der ændres ofte og tåler sekunders forældelse, længere TTL'er plus eksplicit rydning til data, der ændres sjældent, men skal være korrekte, når de gør, og versionerede cachenøgler til indhold, der er uforanderligt, når det er udgivet. Tricket med versionerede nøgler er værd at tage til sig: i stedet for at invalidere ændrer du nøglen. Et stylesheet serveret som `app.v187.css` behøver aldrig rydning, fordi en ny version er en ny nøgle, og den gamle simpelthen holder op med at blive efterspurgt. Hver gang du kan forvandle et invalideringsproblem til et navngivningsproblem, så gør det.

### Design cachenøgler og TTL'er med vilje

En cache er kun så god som sin nøgle. [Cachenøglen](https://en.wikipedia.org/wiki/Cache_(computing)) er den identifikator, en værdi gemmes og slås op under, og at få den forkert forårsager to modsatte fejl. For grov, og du serverer én brugers data til en anden: en personaliseret side cachet under en URL, der ignorerer brugeridentiteten, er et datalæk. For fin, og din hitrate kollapser, fordi ingen to anmodninger deler en nøgle. Beslut bevidst, hvad der hører til i nøglen: ressourceidentiteten plus alt, der legitimt varierer svaret (sprog, valuta, enhedsklasse) og intet, der ikke gør. Normalisér nøgler, så trivielle forskelle som rækkefølgen af forespørgselsparametre ikke fragmenterer cachen.

TTL'er fortjener samme omtanke. En TTL er et løfte om den maksimale forældelse, du vil servere, så sæt den ud fra datas reelle tolerance, ikke et rundt tal, nogen gættede: en aktiekurs tåler sekunder, et produktkatalog minutter, en udgivet forskrift timer eller en versioneret nøgle og slet intet udløb. Tilføj en lille tilfældig spredning, kaldet jitter, så en batch af poster skrevet sammen ikke alle udløber i samme øjeblik og stormer oprindelsesserveren. Skriv disse valg ned, for en TTL uden begrundelse er et tal, den næste ingeniør vil være bange for at ændre.

### Beskyt mod stampedes, og læg anmodninger sammen

Når en populær cachet post udløber, misser hver anmodning, der ville have den, på én gang og styrter mod oprindelsesserveren sammen. Dette er [cache-stampeden](https://en.wikipedia.org/wiki/Cache_stampede), også kaldet thundering herd, og den kan vælte netop den database, cachen beskyttede. Byg forsvaret én gang og genbrug det overalt. Anmodningssammenlægning (single-flight) lader kun den første anmodning om en manglende nøgle genberegne værdien, mens de andre venter på dens resultat, så tusind samtidige misses forårsager ét oprindelseskald. Sandsynlighedsbaseret tidlig genberegning opdaterer en varm post tilfældigt lidt før dens udløb, så én baggrundsanmodning fornyer den, før mængden ser en miss. En stale-while-revalidate-politik serverer den lidt forældede kopi straks og opdaterer den asynkront, så brugerne aldrig venter på en miss.

Disse mønstre betyder mest netop, når du har mest brug for cachen, under spidsbelastning, så valider dem i realistisk skala: et forsvar, der virker med ti brugere, kan stadig fejle ved ti tusind. Par dem med robusthedsmønstrene fra kapitel 3.5, især timeouts og circuit breakers, så cachelaget skærmer oprindelsesserveren frem for at stable oven på, når den reelt er langsom. Målet er en cache, der opfører sig bedst under pres, ikke en, der forstærker en spids til et nedbrud.

### Vælg et skrivemønster bevidst

Hvordan du håndterer skrivninger afgør, hvor frisk din cache forbliver, og hvor meget du risikerer ved fejl. Der er fire almindelige mønstre. I [cache-aside](https://en.wikipedia.org/wiki/Cache_(computing)) (lazy loading) tjekker applikationen cachen, og ved en miss læser den oprindelsen, udfylder cachen og returnerer værdien; skrivninger går til oprindelsen og invaliderer posten. Det er standarden med god grund: simpelt, og cachen holder kun det, der efterspørges. I write-through går hver skrivning til cache og oprindelse sammen, så cachen altid er aktuel, til prisen af skrivelatens og caching af data, der måske aldrig læses. I write-back (write-behind) rammer skrivninger cachen først og flushes til oprindelsen asynkront, hvilket gør skrivninger hurtige, men risikerer tab, hvis cachen dør før flush. I write-around går skrivninger direkte til oprindelsen og springer cachen over, hvilket undgår uro fra skrivetunge data, der sjældent læses, til prisen af en garanteret første-læsnings-miss.

Vælg pr. arbejdsbyrde, ikke én gang for hele systemet. Et læsetungt katalog passer til cache-aside eller write-through. En skrivetung log- eller målingsstrøm passer til write-around, så cachen ikke forstyrres af data, ingen genlæser. Write-back passer til skrivninger med højt gennemløb, hvor en lille, forstået risiko for tab er acceptabel, og holdbarhed håndteres andetsteds. Angiv mønstret for hver cache eksplicit, for en læser, der antager cache-aside, når koden gør write-back, vil fejlbedømme både friskhed og fejladfærd.

### Afstem udsmidningspolitik med dit adgangsmønster

En cache har en fast størrelse, så når den fyldes, må noget gå. Udsmidningspolitikken afgør hvad. [Least recently used](https://en.wikipedia.org/wiki/Cache_replacement_policies) (LRU) smider den post ud, der har været urørt længst, i væddemål om at nylig brug forudsiger fremtidig brug, og den er en fornuftig standard. Least frequently used (LFU) smider posten med færrest hits ud, hvilket passer til stabile varme sæt, hvor få elementer er evigt populære, men kan klamre sig til poster, der engang var varme og aldrig tilpasser sig. Varianter som segmenteret LRU og adaptive politikker blander nylighed og hyppighed; først-ind-først-ud og simpelt tidsbaseret udløb er billigere, men mere sløve.

Afstem politikken med, hvordan dine data tilgås: LFU eller en frekvensbevidst politik til et lille varmt sæt, der sjældent skifter, LRU hvor popularitet flytter sig over tid som med nyheder eller trendende indhold. Uanset hvad du vælger, så dimensionér cachen, så det varme sæt passer, for en cache for lille til at holde arbejdssættet thrasher og smider poster ud lige før, de skal bruges igen. Følg udsmidningsraten som en førsteklasses måling, da en pludselig stigning som regel betyder, at cachen er underdimensioneret, eller at en nøgleeksplosion fragmenterer den.

### Brug HTTP-cachingsemantik korrekt

Nettet har en moden, standardiseret cachingmodel indbygget i [HTTP](https://en.wikipedia.org/wiki/HTTP), og at bruge den godt giver dig klient- og CDN-caching gratis. `Cache-Control`-headeren er kontrolfladen: `max-age` sætter friskhedslevetiden, `public` og `private` siger, om delte caches må gemme svaret, `no-store` forbyder caching, og `stale-while-revalidate` tillader at servere en forældet kopi, mens den opdateres. Validering lader en cache tjekke friskhed billigt uden at hente indholdet igen. Et [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) (entitetstag) er en uigennemsigtig versionsidentifikator, serveren vedhæfter et svar; klienten sender den tilbage i en `If-None-Match`-header, og serveren svarer `304 Not Modified` uden indhold, hvis intet er ændret. `Last-Modified` med `If-Modified-Since` gør det samme med tidsstempler.

Den praktiske disciplin er at være eksplicit. Sæt `Cache-Control` på hvert svar frem for at lade caches gætte med heuristikker. Markér private svar pr. bruger `private` eller `no-store`, så en delt proxy aldrig gemmer dem, en almindelig og farlig fejl. Brug versionerede URL'er med lang max-age og `immutable`-direktivet til statiske aktiver, og validering med ETags til indhold, der ændres uforudsigeligt. At få disse headers rigtige forvandler hele klient- og CDN-laget til en korrekt, standardbaseret cache, du ikke behøvede at bygge.

### Skub arbejde til kanten med CDN'er og edge computing

Et CDN startede som en måde at cache statiske filer nær brugerne på, og det gør det stadig fremragende: billeder, scripts, video og downloads serveret fra en kantlokation få millisekunder væk i stedet for en fjern oprindelsesserver. Moderne CDN'er går videre. De cacher dynamisk og personaliseret indhold med finkornede nøgler, terminerer TLS ved kanten, absorberer trafikspidser og distribuerede denial-of-service-angreb og kører i stigende grad din kode. [Edge computing](https://en.wikipedia.org/wiki/Edge_computing) udfører logik ved selve kantlokationerne, så du kan personalisere et svar, tjekke autorisation eller samle et sidefragment uden en rundtur til en central region.

Støt dig til dette for de læsninger, der dominerer de fleste systemer. Læg statiske aktiver bag CDN'et med langlivede versionerede URL'er, cache API-svar ved kanten, hvor friskhed tillader det (nøglet omhyggeligt, så personalisering ikke lækker), og brug edge compute til latenskritisk, let logik tæt på brugerne. Afvejningen er rækkevidde versus kontrol: kanten er hurtig og tæt på, men langt fra dine data og sværere at fejlsøge, så hold alt, der kræver stærk konsistens eller frisk autoritativ tilstand, i oprindelsen, og lad kanten håndtere den enorme, cachebare læsetrafik.

### Behandl cachen som en angrebsflade

En cache serverer det samme gemte svar til mange brugere, hvilket gør den til et mål. [Cacheforgiftning](https://en.wikipedia.org/wiki/Cache_poisoning) er et angreb, hvor en anmodning udformes, så cachen gemmer et skadeligt eller angriberstyret svar og derefter serverer det til alle, der følger efter. Det udnytter som regel et unøglet input: en header, applikationen reflekterer ind i svaret, men cachen ignorerer, når den bygger nøglen. Det beslægtede web cache deception-angreb narrer en cache til at gemme et offers private svar under en offentlig URL. Begge er fejl i nøgling og i tillid til input, dækket bredere i kapitel 4.2.

Forsvar bevidst. Inkludér i cachenøglen hvert input, der kan ændre svaret, og nægt at reflektere unøglede headers ind i cachede indhold. Lad aldrig en delt cache gemme autentificerede svar pr. bruger under en delt nøgle. Normalisér og validér anmodningsstier og parametre før caching. Sæt `Vary` korrekt, så caches partitionerer svar efter de headers, der faktisk betyder noget, såsom indholdskodning eller sprog. Fordi en enkelt forgiftet post skader hver nedstrøms bruger, så behandl cachekonfiguration som sikkerhedsfølsom kode og gennemgå den som sådan.

### Gør cacheadfærd observerbar

Du kan ikke styre en cache, du ikke kan se. Den overordnede måling er hitraten: andelen af anmodninger, der serveres fra cachen frem for oprindelsen. En hitrate, der stille falder fra 95 til 70 procent, kan multiplicere oprindelsesbelastningen adskillige gange og gå forud for et nedbrud, og du fanger det kun tidligt, hvis du holder øje. Instrumentér hvert lag separat, da en sund CDN-hitrate kan skjule en kollapsende hitrate i applikationscachen nedenunder. Dette er cachingens ansigt af observerbarhedspraksisserne i kapitel 9.2.

Følg mere end hits: udsmidningsrate og hukommelsespres for at fange underdimensionering, latens ved hvert lag for at bekræfte, at cachen faktisk er hurtigere, oprindelsesanmodningsrate for at se, hvor meget belastning cachen absorberer, og forældelse (hvor gamle serverede poster er) for at bekræfte, at I overholder jeres friskhedsløfter. Alarmér på de forhold, der forudsiger problemer, især en faldende hitrate eller en stigende udsmidningsrate, så I hører om en forringet cache fra et dashboard frem for fra brugerne. En observeret cache er et aktiv, I kan justere; en ikke-observeret er en skjult afhængighed, der venter på at overraske jer.

## Afvejninger: fordele og ulemper

Caching køber hastighed og skala med valutaen friskhed og kompleksitet. Hver cache er et væddemål om, at forældet-men-hurtigt slår frisk-men-langsomt for netop disse data, og kunsten er at placere væddemålet bevidst frem for som standard. Tabellen nedenfor opsummerer de vigtigste valg.

| Valg | Fordele | Ulemper |
|---|---|---|
| Cache-aside | Simpelt; cacher kun det, der læses | Første læsning misser altid; risiko for kortvarig forældelse efter skrivninger |
| Write-through | Cachen altid aktuel ved skrivning | Langsommere skrivninger; cacher data, der måske aldrig læses |
| Write-back | Meget hurtige skrivninger; absorberer byger | Risiko for datatab, hvis cachen fejler før flush |
| Write-around | Undgår uro i cachen fra skrivetunge data | Garanteret miss ved første læsning |
| Kort TTL | Afgrænset, lille forældelse | Lavere hitrate; mere oprindelsesbelastning |
| Lang TTL / versionerede nøgler | Høj hitrate; lav oprindelsesbelastning | Forældelse medmindre invalideret; kræver disciplinerede nøgler |
| CDN og edge | Global lav latens; absorberer spidser | Langt fra data; sværere at fejlsøge og invalidere |
| LRU-udsmidning | Tilpasser sig skiftende popularitet | Kan smide et stabilt varmt sæt ud under scanningstung belastning |
| LFU-udsmidning | Beskytter et stabilt varmt sæt | Langsom til at tilpasse sig; klamrer sig til tidligere varme poster |

Den tilbagevendende spænding er konsistens versus ydeevne. En cache med lang TTL og høj hitrate er hurtig og billig og kan servere forældede data; en cache med kort TTL og aggressiv invalidering er frisk og korrekt og arbejder oprindelsen hårdere. Der er intet universelt rigtigt svar, kun et rigtigt svar pr. stykke data, bestemt af dets reelle tolerance for forældelse. Den anden spænding er enkelhed versus rækkevidde: en applikationscache er tæt på dine data og let at ræsonnere om, mens kanten er langt væk, hurtig og sværere at invalidere. Løs begge ved at klassificere dine data efter friskhedsbehov og læsevolumen og så placere og konfigurere hver klasse med vilje.

## Spørgsmål til drøftelse med dit team

1. **Hvad er den reelle forældelsestolerance for hver slags data, vi cacher, og har vi sat TTL'er og invalidering ud fra den tolerance frem for ud fra vane?** De fleste teams cacher med en TTL, nogen valgte én gang og aldrig genbesøgte, så nogle data serveres mere forældede, end forretningen kan acceptere, mens andre data udløber så aggressivt, at cachen næsten ikke hjælper. Tag jeres ti øverste cachede ressourcer med, og spørg for hver dem, der ejer disse data, hvor forældede de sikkert må være: sekunder, minutter, timer eller aldrig efter udgivelse. I vil som regel finde, at svarene varierer vidt, og at jeres nuværende TTL'er ikke svarer til dem. Det udfald, I vil have, er en kort friskhedsklassificering, hver klasse afbildet til en tilgang (kort TTL, lang TTL plus rydning eller versionerede uforanderlige nøgler), så cachingbeslutninger følger af datas semantik i stedet for gætværk.

2. **Hvis vores mest populære cachepost udløb lige nu under spidsbelastning, hvad ville der ske med oprindelsen?** Dette spørgsmål afslører, om I har reel beskyttelse mod stampede eller kun håb. Mange systemer kører fint, indtil en varm nøgle udløber under en trafikspids, og hver anmodning styrter mod databasen på én gang og forvandler cachen fra et skjold til en udløser. Gå stien konkret igennem for jeres travleste endepunkt: er der anmodningssammenlægning, så kun én miss når oprindelsen, er der jitter, så poster ikke udløber i takt, er der en stale-while-revalidate-politik, så brugerne aldrig venter på en genopfyldning? Tag belastningstestdokumentation med, ikke intuition, for et stampedeforsvar, der holder ved ti brugere, kan stadig kollapse ved ti tusind. Hvis I ikke kan svare med sikkerhed, har I netop fundet jeres næste robusthedsinvestering.

3. **Er vi sikre på, at ingen delt cache nogensinde gemmer én brugers private data under en nøgle, en anden bruger kan ramme?** Dette er den cachingfejl, der bliver til en sikkerhedshændelse og en overskrift. Det sker, når et personaliseret eller autentificeret svar caches under en nøgle, der udelader brugeridentiteten, eller når en `Cache-Control`-header, der skulle holde et svar privat, mangler, så en delt proxy eller CDN gemmer det og serverer det til den næste person. Gennemgå, hvilke svar der kan caches på delte lag, bekræft at hvert svar pr. bruger er markeret `private` eller `no-store`, og bekræft at hver cachenøgle inkluderer hvert input, der ændrer svaret. Behandl dette som sikkerhedsgennemgang, fordi sprængradien er hver nedstrøms bruger, og bind det til praksisserne i kapitel 4.2.

4. **Hvilket skrivemønster bruger hver af vores caches faktisk, og valgte nogen det med vilje?** Cache-aside, write-through, write-back og write-around giver modsatte løfter om friskhed og om, hvad I mister, når cachen fejler, men i de fleste kodebaser er mønstret det, den første forfatter tilfældigvis kopierede. For et stort team betyder det noget, fordi én tjeneste, der antager cache-aside-friskhed, mens en anden stille kører write-back, kan producere data, der ser korrupte ud, men blot er forældede, og vagthavende ingeniør spilder timer på at jage et spøgelse. Tag en opgørelse pr. cache med: skrivemønstret, den friskhed det garanterer, og hvad der sker med uflushede skrivninger, hvis processen dør. Hvor en cache bruger write-back, så tag holdbarhedshistorien med, der understøtter den. I virksomheds- og offentlige systemer, der håndterer finans- eller registerdata, er en write-back-cache uden bagvedliggende garanti et revisionsfund, der venter på at ske, så drøftelsen bør ende med, at hver caches mønster er navngivet, begrundet og skrevet ned.

5. **Når vi udruller eller ændrer data, invaliderer hvert relevant cachelag da korrekt, eller stoler vi på, at nogen husker at rydde?** Invalidering er den svære del, og fejlformen er stille: en rettet værdi, der forbliver forkert i timer, fordi ét lag i hierarkiet, et CDN, en reverse proxy eller en applikationscache, aldrig fik beskeden. En stor organisation multiplicerer denne risiko, fordi en enkelt logisk ændring kan skulle udbredes på tværs af mange caches i mange regioner ejet af forskellige teams. Tag et konkret spor af én nylig dataændring med, og følg den gennem hvert cachelag og spørg ved hvert: hvad udløste invalidering her, og hvor lang tid tog det? Foretræk designs, der forvandler invalidering til navngivning (versionerede nøgler) eller til hændelser (en ændring udgiver en rydning), frem for manuelle runbooks. I offentlige systemer, hvor et forkert udgivet tal, en skattesats eller et ydelsesbeløb, kan have juridisk vægt, er et invalideringshul ikke en gene, men en compliance-eksponering, så udfaldet bør være en kortlagt invalideringssti for hver klasse af cachede data.

6. **Behandler vi caching som fælles platformsinfrastruktur, eller genopfinder hvert team nøgler, invalidering og stampedebeskyttelse på egen hånd?** Caching gjort godt er et lille sæt svære problemer løst én gang: normaliserede nøgler, hændelsesdrevet invalidering, anmodningssammenlægning, korrekt HTTP-semantik og observerbarhed pr. lag. Når hvert team improviserer disse, betaler en stor organisation for de samme fejl gentagne gange, og en forgiftningsfejl eller et privatdatalæk rettet i én tjeneste består stille i ti andre. Tag et ærligt kort over, hvem der ejer cachingkonventioner i dag, og hvor megen duplikeret cachingkode der findes på tværs af tjenester. Det modstridende hensyn er autonomi: teams modstår et påbudt fælles bibliotek, så vej en asfalteret standardvej, der er let at adoptere, mod en hård standard, der håndhæves. For en virksomheds- eller offentlig platformsgruppe er en fælles, veltestet cachingevne også den billigste måde at få sikkerheds- og revisionskrav til at holde ensartet, så drøftelsen bør afgøre, hvad der bliver fælles infrastruktur, og hvem der finansierer det.

## Sektorperspektiv

**Startup.** Caching er din billigste vej til at overleve en trafikspids, du endnu ikke har råd til at skalere for, så brug den lille tid, du har, på nogle få placeringer med høj løftestang: et CDN med versionerede URL'er til statiske aktiver og et enkelt cache-aside-lag med korte TTL'er og jitter foran din varmeste forespørgsel. Støt dig til administrerede CDN- og cachetjenester frem for at køre dine egne, og tilføj anmodningssammenlægning tidligt, for en stampede på lanceringsdagen mod en lille database er den fejl, der mest sandsynligt får en god dag til at ende dårligt. Spring omfattende invalideringsskemaer over, til du har data, der fortæller dig, at de betyder noget.

**Lille virksomhed.** Uden en cachingspecialist og med et stramt budget så foretræk at købe caching, du får gratis i værktøjer, du allerede kører: et CDN medfølgende dit hosting, HTTP `Cache-Control`-headers på dit webframeworks svar og din databases indbyggede forespørgselscache. Køb-versus-byg-kaldet favoriserer næsten altid køb her, da en fejlnøglet cache, der lækker én kundes data til en anden, koster langt mere end den administrerede tjeneste, du undgik. Få de to billige gevinster rigtige, korrekte HTTP-headers og aldrig at cache autentificerede sider på delte lag, og lad de eksotiske mønstre være.

**Stor virksomhed.** I skala på tværs af mange teams skifter risikoen fra enhver enkelt cache til inkonsistens mellem dem: divergerende nøgleskemaer, ujævn invalidering og privatdatalæk, der optræder i én tjeneste og ikke en anden. Lever caching som fælles platformsinfrastruktur med asfalterede standardveje for nøgler, invalidering, stampedebeskyttelse og observerbarhed pr. lag, så hitrate, udsmidning og forældelse er synlige ét sted og styret ensartet. Gør cachekonfiguration gennemgåelig som sikkerhedsfølsom kode, og behandl invalidering på tværs af regioner som et førsteklasses designproblem frem for en runbook pr. team.

**Offentlig sektor.** Indkøbs- og åbenhedsbegrænsninger former, hvad I kan cache, og hvordan I beviser, at det er sikkert. Cache offentligt indhold aggressivt, vejledninger, formularer og satstabeller bag et CDN med lange TTL'er, så en spids ved indberetningsfristen absorberes langt fra oprindelsen, og dokumentér konfigurationen til revision. Autentificerede sider, der viser en borgers egne poster, må aldrig røre en delt cache, og den regel bør være verificerbar, ikke blot påstået. Hvor et CDN eller en cachingtjeneste indkøbes fra en leverandør, så kræv at kontrakten eksponerer de kontroller, I har brug for (nøgling, rydning og logning), og undgå indlåsning, der ville fange offentlige data bag proprietære cacheformater.

## Eksempler

**Startup.** En lille forbrugerapp kører sit produktkatalog gennem et cache-aside-lag bakket af et in-memory-lager med en TTL på 60 sekunder og jitter, så poster ikke udløber sammen. Statiske aktiver går til et CDN med versionerede filnavne og en max-age på et år, så en udrulning, der ændrer et stylesheet, serverer en ny URL og aldrig behøver en rydning. Da en lancering i en populær podcast sender en trafikspids, betyder single-flight-sammenlægning, at de tusindvis af samtidige forsidemiss forårsager én databaselæsning, ikke tusinder. Grundlæggerne bruger næsten intet på caching, men håndterer en spids, der ville have smeltet deres lille database, fordi de placerede nogle få velvalgte caches med vilje.

**Stor virksomhed.** En global detailhandler betjener millioner af kunder gennem en lagdelt cache: et CDN til billeder og cachebare API-svar, en delt reverse proxy-cache i hver region og en applikationscache til beregnede pris- og lagerfragmenter. Cachenøgler er normaliserede og inkluderer valuta, sprog og enhedsklasse, så personalisering aldrig lækker, og hitrater forbliver høje. Produktdata bruger korte TTL'er med hændelsesdrevet invalidering, så en prisændring udgiver til en beskedbus, der rydder de berørte nøgler på tværs af regioner inden for sekunder. Hvert lag rapporterer hitrate, udsmidningsrate og forældelse til observerbarhedsplatformen fra kapitel 9.2, og en alarm på en faldende hitrate fangede engang en underdimensioneret cache, før den blev et nedbrud i checkout.

**Offentlig sektor.** En national skatteadministration kører en indberetningsportal, der er stille det meste af året og overvældet nær fristen. Teamet cacher aggressivt, hvor det er sikkert, og aldrig hvor det ikke er. Offentligt indhold (vejledningssider, formularer, satstabeller) serveres fra et CDN med lange TTL'er og versionerede URL'er og absorberer læsebølgen på fristdagen langt fra oprindelsen. Autentificerede sider, der viser en borgers egen indberetning, er markeret `no-store` og rører aldrig en delt cache, så ingen skatteyder nogensinde serveres en andens data. Cachekonfigurationen gennemgås som sikkerhedsfølsom kode mod praksisserne i kapitel 4.2, og stampedebeskyttelse belastningstestes i fristskala måneder i forvejen, så portalen, der plejede at bukke på årets travleste dag, nu holder.

## Business case: motivation, ROI og TCO

Afkastet af caching er usædvanligt direkte og let at kvantificere. En cache, der hæver hitraten fra 80 til 95 procent, skærer oprindelsestrafikken med tre fjerdedele, hvilket kan betyde at udskyde en databaseopgradering, køre færre applikationsservere eller overleve en trafikspids, der ellers ville have krævet nødskalering. Latensforbedringer omsættes til omsætning i handel og til tilfredshed og gennemførelsesrater i offentlige tjenester, hvor forskning længe har koblet hurtigere sider til højere konvertering og lavere frafald. Egress- og beregningsomkostninger falder, fordi en anmodning serveret fra kanten aldrig betaler for oprindelsesbåndbredde eller -behandling. For læsetunge systemer, som de fleste systemer er, er caching ofte den billigste ydeevne, du kan købe.

Vej de totale ejeromkostninger ærligt. De direkte omkostninger er beskedne: CDN- og cacheinfrastruktur er billig i forhold til den oprindelseskapacitet, de sparer. Den reelle omkostning er ingeniørdisciplin, fordi en cache, der er forkert, er værre end ingen cache. Forældelsesfejl, invalideringsfejl og sårbarheder for cacheforgiftning bærer alle reel omkostning, og de vokser, når caching improviseres pr. team i stedet for at leveres som en fælles, veltestet evne. Det stærkeste business case finansierer en lille mængde fælles cachinginfrastruktur og konvention (standardnøgler, invalidering, stampedebeskyttelse og observerbarhed), så hvert team får gevinsten uden at gentage fejlene. Rammet ind for ledelsen forbinder caching sig til målinger, de allerede følger: infrastrukturomkostning, sidelatens, konverterings- og gennemførelsesrater og hændelsesfrekvens under spidsbelastninger.

## Anti-mønstre og faldgruber

- **Caching uden invalidering:** en lang TTL uden mulighed for at rydde, så en rettet værdi forbliver forkert i timer.
- **Nøgler for grove:** caching af personaliserede svar under en delt nøgle, der lækker én brugers data til en anden.
- **Nøgler for fine:** flygtige input i nøglen, så ingen to anmodninger nogensinde matcher, og hitraten kollapser.
- **Ingen stampedebeskyttelse:** en varm nøgle udløber under belastning, og hver anmodning styrter mod oprindelsen på én gang.
- **Synkroniseret udløb:** en batch af poster skrevet sammen udløber i samme øjeblik uden jitter og forårsager en periodisk thundering herd.
- **Caching af private data på delte lag:** manglende `Cache-Control: private` eller `no-store`, så en proxy eller et CDN gemmer autentificerede svar.
- **Ignorering af unøglede input:** at reflektere en header ind i svaret, men udelade den fra nøglen, hvilket åbner døren for cacheforgiftning.
- **Underdimensioneret cache:** en cache for lille til at holde arbejdssættet thrasher og smider poster ud lige før, de skal bruges.
- **Ikke-målt cache:** ingen hitrate- eller udsmidningsmåling, så en forringet cache er usynlig, til den bliver et nedbrud.
- **Write-back uden holdbarhed:** hurtige skrivninger, der forsvinder, når cachen dør før flush, uden bagvedliggende garanti.

## Modenhedsmodel

- **Niveau 1, Opstart:** Caching er ad hoc og pr. udvikler, tilføjet reaktivt, når noget føles langsomt. TTL'er er gættede, nøgler er inkonsistente, invalidering er manuel eller fraværende, og forældede data og mystiske fejl er almindelige. Ingen følger hitrate, og en trafikspids, som en cache burde have absorberet, forårsager i stedet et nedbrud.
- **Niveau 2, Udvikling:** Teams cacher på de oplagte steder og bruger et CDN til statiske aktiver. Grundlæggende TTL'er og cache-aside dukker op, men konventioner varierer fra tjeneste til tjeneste, invalidering er inkonsistent, stampedebeskyttelse mangler, regler for privat versus delt caching er uformelle, og observerbarhed er begrænset til lejlighedsvise stikprøver.
- **Niveau 3, Standardisering:** En cachingstrategi er dokumenteret og håndhævet i hele organisationen. Cachenøgler er normaliserede, TTL'er følger en fælles friskhedsklassificering, invalidering er hændelsesdrevet, hvor det betyder noget, stampedebeskyttelse og korrekt HTTP-semantik er standard, private data caches aldrig på delte lag, og hvert lag rapporterer hitrate og udsmidning til en fælles observerbarhedspipeline.
- **Niveau 4, Styring:** Caching måles og styres mod baselines. Hvert lag har mål for hitrate, forældelsesbudgetter og udsmidningstærskler, og dashboards alarmerer, når en hitrate falder, eller en udsmidningsrate stiger forbi sin baseline. Stampedeforsvar belastningstestes i spidsskala, reduktion af oprindelsesbelastning kvantificeres pr. cache, TTL'er og udsmidningspolitikker justeres ud fra målte adgangsmønstre, og cachekonfiguration gennemgås som sikkerhedsfølsom kode før udgivelse.
- **Niveau 5, Orkestrering:** Caching forbedres løbende og er integreret i hele organisationen. Placering, nøgler og TTL'er tilpasser sig skiftende trafik, edge compute bruges, hvor det tjener sit brød, kapacitetsplanlægning og omkostningsmodeller trækker på cachemålinger, og erfaringer fra ét teams hændelser fodrer fælles konventioner. Organisationen behandler caching som en designet, målt, adaptiv evne frem for en samling lokale hacks.

## Idéer til drøftelse

1. Hvilken enkelt cache i jeres system ville, hvis den blev kold lige nu, mest bringe jeres oprindelse i fare, og hvad beskytter den?
2. Kan I for hvert lag i jeres cachehierarki nævne dets nuværende hitrate udenad, og hvis ikke, hvad fortæller det jer?
3. Hvor har I forvandlet et invalideringsproblem til et navngivningsproblem med versionerede nøgler, og hvor kunne I stadig gøre det?
4. Hvilke af jeres skrivestier bruger cache-aside, write-through, write-back eller write-around, og blev hver valgt med vilje?
5. Hvis en angriber kontrollerede én anmodningsheader, kunne vedkommende så forgifte et cachet svar, jeres brugere deler?
6. Hvordan ville I vide, inden for minutter, at jeres hitrate stille var faldet med tyve point?

## Vigtigste pointer

- Caching skærer latens, belastning og omkostning, og cachehierarkiet (klient, CDN og edge, reverse proxy, applikation, database) lader jer besvare så langt oppe og ude, som I sikkert kan.
- Invalidering er den svære del; design cachenøgler og TTL'er bevidst, og forvandl invalideringsproblemer til navngivningsproblemer med versionerede nøgler, hvor I kan.
- Beskyt cachen under belastning med anmodningssammenlægning, jitter og stale-while-revalidate, fordi en cache er mest nødvendig netop, når en stampede kan bryde den.
- Vælg skrivemønstre og udsmidningspolitikker pr. arbejdsbyrde, og brug HTTP-cachingsemantik (`Cache-Control`, ETags, validering) eksplicit frem for at lade caches gætte.
- Behandl cachet indhold som en angrebsflade, og mål hitrate, udsmidning og forældelse, fordi en ikke-observeret eller fejlnøglet cache er et skjult ansvar, ikke et aktiv.

## Referencer og videre læsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew S. Tanenbaum and Herbert Bos, *Modern Operating Systems*
- John L. Hennessy and David A. Patterson, *Computer Architecture: A Quantitative Approach*
- Roy T. Fielding and Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Caching," RFC 7234, IETF
- Mark Nottingham, "Caching Tutorial for Web Authors and Webmasters"
- James Kettle, "Practical Web Cache Poisoning," PortSwigger Research
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
