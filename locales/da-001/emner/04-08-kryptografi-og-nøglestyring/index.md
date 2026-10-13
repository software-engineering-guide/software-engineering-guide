# 4.8 Kryptografi og nøglestyring

## Overblik og motivation

Næsten ethvert system, du bygger, afhænger allerede af [kryptografi](https://en.wikipedia.org/wiki/Cryptography), praksissen at beskytte information med matematiske teknikker, så kun de tiltænkte parter kan læse eller stole på den. Din webtrafik kører over krypterede kanaler, dine adgangskoder er hashede, dine softwareopdateringer er signerede, og dine kundedata ligger krypteret på disk. Den gode nyhed for de fleste ingeniører er, at du ikke bliver bedt om at opfinde noget af det. Det svære er ikke matematikken. Det er at bruge gennemprøvede byggeklodser korrekt og, frem for alt, at styre de nøgler, de byggeklodser afhænger af.

Dette kapitel er skrevet til ingeniører, der ikke er kryptografer, hvilket næsten er os alle. Du har brug for nok forståelse til at træffe sunde valg, til at vide, hvad hvert værktøj garanterer, og til at undgå de fejl, der forvandler stærke algoritmer til falsk tryghed. Kapitel 4.3 (infrastruktur- og cloudsikkerhed) nævner kryptering og nøglestyring i forbifarten; her går vi dybere ind i, hvad der skal krypteres, hvordan, og hvordan man driver nøglens livscyklus, der gør det reelt.

For store virksomheder breder kryptografi sig over tusinder af tjenester, certifikater og nøgler, og et enkelt udløbet certifikat eller en tabt nøgle kan tage et kritisk system ned eller lække et datalager. For det offentlige er kryptografi ofte påbudt, valideret og revideret, med dataklassifikationsregler, der dikterer præcis, hvilke nøgler der beskytter hvilke hemmeligheder, og hvem der må holde dem. I begge sammenhænge er den tilbagevendende fejl den samme: gode algoritmer ødelagt af sjusket nøglestyring.

## Grundprincipper

- **Rul ikke din egen kryptografi.** Brug gennemprøvede, bredt gennemgåede biblioteker og standardalgoritmer. Nye skemaer fejler på måder, kun eksperter fanger.
- **Algoritmer er den lette del; nøgler er den svære del.** Nøglens livscyklus er der, hvor de fleste reelle fejl bor.
- **Kend, hvad hver primitiv garanterer.** Fortrolighed, integritet og ægthed er forskellige egenskaber, der kræver forskellige værktøjer.
- **Krypter under transport og i hvile som standard.** Gør beskyttelse til standarden, ikke et tilvalg.
- **Adskil nøglevaretægt fra dataadgang.** Den, der styrer en nøgle, bør ikke automatisk kunne læse de data, den beskytter.
- **Planlæg for forandring.** Algoritmer svækkes, nøgler lækker, og standarder udvikler sig. Byg til rotation og migrering fra dag ét.
- **Foretræk validerede implementeringer, hvor det betyder noget.** For regulerede og offentlige opgaver vælg moduler med anerkendt validering.

## Anbefalinger

### Rul ikke din egen kryptografi

Dette er den gyldne regel, og den er værd at nævne først. Design aldrig din egen krypteringsalgoritme, opfind aldrig din egen protokol, og implementér aldrig en primitiv i hånden fra en artikel. Fungerende kryptografi ser simpel ud og skjuler subtile fejlformer (timing-sidekanaler, padding-orakler, svag tilfældighed), som kun overlever år af ekspertgennemgang. Brug etablerede biblioteker såsom din platforms standardkryptomodul eller et velanset bibliotek, og brug dem på det højeste abstraktionsniveau, der er tilgængeligt. Ræk ud efter autentificerede krypteringstilstande og "lette" grænseflader, der gør det sikre valg til standarden, frem for selv at samle lavniveaudele.

### Afstem primitiven med den garanti, du har brug for

Forskellige værktøjer giver forskellige garantier, og at forveksle dem er en almindelig og farlig fejl. Lær de tre hovedfamilier.

- **[Symmetrisk nøgle](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)**-kryptografi bruger én delt hemmelig nøgle til både at kryptere og dekryptere. Den er hurtig og beskytter **fortrolighed**, men begge parter skal allerede dele nøglen. AES er det standardiserede arbejdsredskab.
- **[Offentlig nøgle](https://en.wikipedia.org/wiki/Public-key_cryptography)**-kryptografi bruger et matematisk forbundet nøglepar: en offentlig nøgle, enhver kan holde, og en privat nøgle, du holder hemmelig. Den løser nøgledistribution og muliggør **digitale signaturer**, der beviser **ægthed** (hvem der sendte det) og **integritet** (at det ikke blev ændret).
- En **[kryptografisk hashfunktion](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** producerer et fingeraftryk af fast størrelse af data og giver **integritets**kontrol. Hashing er envejs og er ikke kryptering. Til lagring af adgangskoder brug en langsom, saltet adgangskodehashfunktion, aldrig en almindelig hurtig hash (se kapitel 4.2 om applikationssikkerhed).

Den praktiske lektie: kryptering skjuler data, men beviser ikke, hvem der sendte dem, og en hash opdager manipulation, men skjuler intet. De fleste reelle systemer kombinerer dem, hvilket er præcis grunden til, at I bør støtte jer til biblioteker, der bundter dem korrekt.

### Krypter under transport med aktuel TLS

Beskyt hvert netværksspring med [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), protokollen der sikrer data, mens de bevæger sig mellem systemer. Kræv moderne TLS-versioner, deaktivér forældede, vælg stærke krypteringssuiter, og validér certifikater ordentligt frem for at slå tjek fra for at "få det til at virke." Krypter også intern tjeneste-til-tjeneste-trafik, ikke blot den offentlige kant, fordi en zero trust-holdning antager, at det interne netværk er fjendtligt. Automatisér udstedelse og fornyelse af certifikater, så TLS er den ubesværede standard overalt.

### Krypter i hvile med envelope-kryptering

Krypter lagrede data som standard: databaser, objektlager, backups og logs. Standardmønstret er **envelope-kryptering**, hvor en **datakrypteringsnøgle (DEK)** krypterer de egentlige data, og en **nøglekrypteringsnøgle (KEK)** holdt i en nøglestyringstjeneste krypterer DEK'en. Det lader jer rotere hovednøglen uden at omkryptere terabytes af data, og det holder den mægtige rodnøgle inde i en hærdet grænse. Gem kun den indpakkede DEK ved siden af dataene, og hent og pak den ud ved brug.

### Kør nøglens livscyklus bevidst

Nøglens livscyklus er den virkelig svære del af kryptografi og der, hvor de fleste brud og nedbrud har deres oprindelse. Styr hvert trin med vilje:

- **Generering:** opret nøgler fra en stærk tilfældig kilde, med passende styrke.
- **Distribution:** få nøgler til de systemer, der har brug for dem, uden at eksponere dem i kode, konfigurationsfiler eller chat.
- **Rotation:** udskift nøgler efter en plan, og vær i stand til at rotere hurtigt ved mistanke om kompromittering.
- **Tilbagekaldelse:** ugyldiggør en kompromitteret nøgle eller et certifikat hurtigt, og sørg for, at systemer respekterer tilbagekaldelsen.
- **Destruktion:** pensionér sikkert gammelt nøglemateriale, så det ikke kan genskabes.

Brug en **nøglestyringstjeneste (KMS)** til at centralisere dette, og brug et [hardwaresikkerhedsmodul](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), en manipulationssikker enhed, der genererer og vogter nøgler, så de aldrig forlader den i klartekst, til jeres nøgler med højeste assurance. Adskil, hvem der kan styre nøgler, fra hvem der kan læse de beskyttede data, så nøglevaretægt håndhæver adskillelse af opgaver. Dette hænger direkte sammen med dataklassificering og varetægtsregler i kapitel 4.5 (privatliv og databeskyttelse).

### Skeln mellem hemmelighedsstyring og nøglestyring

Disse overlapper, men er ikke det samme. **Nøglestyring** styrer kryptografiske nøgler og deres livscyklus, som regel inde i en KMS eller HSM, der udfører kryptooperationer for dig, så den rå nøgle aldrig forlader. **Hemmelighedsstyring** styrer applikationslegitimationer (databaseadgangskoder, API-tokens, certifikater), som tjenester skal hente og bruge i klartekst, som regel fra en hemmelighedsvault med kortlivet, revideret adgang. Brug en KMS til nøgler, en hemmelighedshåndtering til legitimationer, og indsæt aldrig nogen af dem i kildekode eller miljøfiler indtjekket i versionsstyring.

### Automatisér PKI- og certifikatlivscyklusser

**Public key infrastructure (PKI)** er systemet af certifikatmyndigheder, certifikater og tillidskæder, der binder offentlige nøgler til identiteter. I skala er den dominerende PKI-risiko det overraskende certifikatudløb, der tager en tjeneste ned. Vedligehold en opgørelse over hvert certifikat, overvåg udløb, og automatisér udstedelse og fornyelse, så intet menneske behøver at huske det. Kortlivede certifikater fornyet automatisk er sikrere end langlivede, der plejes i hånden, fordi automatisering fjerner det menneskelige enkelte fejlpunkt. Standardprotokoller her understøtter interoperabilitet på tværs af leverandører (kapitel 3.8 om interoperabilitet og åbne standarder).

### Byg til kryptografisk smidighed og post-kvantemigrering

Algoritmer svækkes over tid, og standarder flytter sig. **Kryptografisk smidighed** betyder at designe systemer, så I kan bytte algoritmer og nøglestørrelser uden en smertefuld omskrivning: abstrahér kryptografi bag en lille grænseflade, versionér jeres krypterede data, så I ved, hvilken algoritme der producerede dem, og hold en kryptoopgørelse over, hvad I bruger hvor. Det betyder noget nu på grund af [post-kvantekryptografi](https://en.wikipedia.org/wiki/Post-quantum_cryptography), den nye familie af algoritmer designet til at modstå fremtidige kvantecomputere. Modstandere kan høste krypterede data i dag for at dekryptere senere, så langlivede hemmeligheder har brug for en migreringsplan. I behøver ikke gå i panik, men I bør kende jeres opgørelse og være klar til at adoptere de standardiserede post-kvantealgoritmer, efterhånden som platforme leverer dem.

### Foretræk validerede implementeringer, hvor det kræves

For regulerede og offentlige systemer er det ikke nok at bruge en stærk algoritme; implementeringen skal være valideret. **FIPS 140** (Federal Information Processing Standard 140) er den amerikanske standard til validering af kryptografiske moduler, og mange kontrakter kræver FIPS-valideret kryptografi. Offentligt arbejde kan også følge national vejledning såsom NSA's Commercial National Security Algorithm (CNSA)-suite for klassificerede systemer. Tjek, hvilket regime der gælder, før I bygger, fordi det er dyrt at eftermontere validerede moduler sent. Dette hænger sammen med compliance-dokumentation og styring (kapitel 4.6).

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Udbyderstyret KMS | Let, integreret, lav driftsbyrde | Udbyderen har varetægten; mindre direkte kontrol |
| Kundestyrede nøgler / HSM | Fuld varetægt, opfylder strenge påbud | Driftsoverhead, risiko for at miste nøgler |
| Automatiserede kortlivede certifikater | Ingen overraskelsesudløb, hurtig tilbagekaldelse | Kræver automatiseringsinvestering på forhånd |
| Langlivede certifikater | Simple, færre bevægelige dele | Menneskestyrede udløb forårsager nedbrud |
| Envelope-kryptering | Billig nøglerotation, beskytter hovednøglen | Flere bevægelige dele at forstå |
| Kryptografisk smidighed fra starten | Billige fremtidige migreringer | Ekstra abstraktion og designindsats nu |
| Tidlig post-kvanteadoption | Beskytter langlivede hemmeligheder | Umodent værktøj, større nøgler, nogen risiko |

Den centrale spænding er kontrol versus driftsbyrde. At holde jeres egne nøgler i en HSM giver maksimal varetægt og opfylder de strengeste påbud, men det kræver ekspertise og skaber en ny katastrofal risiko: mist nøglen, og I mister dataene, uigenkaldeligt. Udbyderstyrede tjenester fjerner den byrde, men placerer varetægten hos udbyderen. Løs det ved at lægge i lag: brug administrerede tjenester med fornuftige standarder til de fleste systemer, og forbehold kundestyrede nøgler og HSM'er til data med højeste klassifikation, hvor den ekstra kontrol er omkostningen og risikoen værd.

## Spørgsmål til drøftelse med dit team

1. **Har I en komplet opgørelse over jeres nøgler, certifikater og de algoritmer, I stoler på?** I kan ikke rotere, migrere eller revidere, hvad I ikke kan se, og de fleste organisationer opdager, at de har langt mere kryptografisk materiale spredt over tjenester, end nogen sporer. En opgørelse er forudsætningen for enhver senere beslutning: certifikatudløbsovervågning, nøglerotation, FIPS-afgrænsning og post-kvanteplanlægning afhænger alle af den. Tag en liste over jeres nuværende certifikater og deres udløbsdatoer med, og spørg, hvem der ejer hvert, og hvad der går i stykker, når det lapser. For en stor ejendom er det ærlige svar som regel, at ingen enkelt kilde til sandheden findes, og at bygge en er det første trin med højest løftestang. Hvis I ikke kan opregne jeres kryptografi i dag, er smidighed og rotation aspirationer, ikke evner.

2. **Kan I rotere eller tilbagekalde en kompromitteret nøgle hurtigt, og har I nogensinde øvet det?** Rotation og tilbagekaldelse er de dele af nøglens livscyklus, der kun betyder noget under pres, og teams opdager rutinemæssigt under en hændelse, at en nøgle er hårdkodet i et dusin steder, eller at tilbagekaldelse ikke faktisk udbredes. Beslut jeres måltid for at rotere en nøgle og tilbagekalde et certifikat, og øv det så, før I har brug for det. Tag historien om jeres seneste legitimationseksponering med og gå igennem, hvad rotation krævede i praksis. For virksomheds- og offentlige systemer kan en uøvet rotation betyde at vælge mellem en langvarig eksponering og et selvforskyldt nedbrud. Hvis rotation aldrig er testet, så antag, at den ikke virker.

3. **Hvor sidder nøglevaretægten, og håndhæver den adskillelse af opgaver?** Den, der kan styre en nøgle, og den, der kan læse de data, den beskytter, bør ikke være den samme person, fordi at slå de beføjelser sammen stille underminerer formålet med kryptering i hvile. Dette valg driver også, om I bruger udbyderstyrede nøgler, kundestyrede nøgler eller HSM'er, hver med forskellig kontrol og forskellig driftsrisiko. Tag jeres nuværende nøglepolitikker med og tjek, om nogen enkelt identitet både kan administrere en nøgle og tilgå klarteksten bagved, hvilket er et almindeligt stille hul. For regulerede og klassificerede data kan varetægtsregler være dikteret af dataklassificering (kapitel 4.5) og af påbud. Hvis varetægt og adgang ikke er adskilt, beskytter jeres kryptering jer mindre, end dashboardet antyder.

4. **Hvordan ville I komme jer, hvis den hovednøgle, der beskytter jeres envelope-kryptering, blev tabt eller ødelagt?** Kundestyrede nøgler og HSM'er giver jer varetægt, men de giver jer en ny katastrofal fejlform: mist nøglekrypteringsnøglen, og hver datakrypteringsnøgle, den pakker ind, bliver permanent ulæselig, sammen med dataene bagved. Vej dette mod den modsatte risiko ved en for bred backup, der stille genskaber netop det varetægtsproblem, I forsøgte at løse. Tag jeres nuværende arrangementer for nøglebackup og escrow med, sprængradius for hver hovednøgle og dokumentation for, at en gendannelse faktisk er blevet udført frem for blot dokumenteret. For virksomheds- og offentlige ejendomme så bind dette til jeres dataklassificeringsregler: de mest følsomme nøgler forbyder ofte tilfældige kopier, så genopretning skal designes bevidst, testes efter en plan og afstemmes med ethvert regulatorisk krav om at bevise, at pensioneret nøglemateriale blev destrueret.

5. **Hvor klare er jeres systemer til en post-kvantemigrering, og hvilke langlivede hemmeligheder ville I migrere først?** Modstandere kan høste krypteret trafik og arkiver i dag og dekryptere dem, når kvantecomputere modnes, så enhver hemmelighed, der skal forblive fortrolig i årevis, er allerede eksponeret for en fremtid, I ikke kan se. Det modstridende pres er, at post-kvanteværktøj stadig er ungt, nøglerne er større, og at flytte for tidligt risikerer at satse på en algoritme, der skifter, før den sætter sig. Tag jeres kryptoopgørelse, en liste over hemmeligheder rangeret efter hvor længe de skal forblive fortrolige og en ærlig vurdering af, om jeres arkitektur kan bytte algoritmer uden en omskrivning, med. For offentligt og reguleret arbejde gør journaler med fortrolighedskrav over flere årtier dette konkret frem for teoretisk, og indkøb kan snart kræve en dokumenteret migreringsplan og understøttelse af de standardiserede post-kvantealgoritmer.

6. **Når regulering kræver valideret kryptografi, ved I så præcis, hvilke moduler der er i omfang, og om de kvalificerer?** At bruge en stærk algoritme er ikke det samme som at bruge en valideret implementering, og teams opdager rutinemæssigt sent, at et bibliotek, en sprogruntime eller en cloudtjeneste ikke er dækket af den FIPS 140-grænse, en kontrakt kræver. Spændingen er, at validerede moduler kan halte efter aktuelle biblioteker i funktioner og hastighed, så at vælge dem begrænser jeres stak på måder, der betyder noget for ingeniørarbejdet. Tag listen over kryptografiske moduler, hver reguleret system faktisk kalder, de valideringscertifikater, der dækker dem, og det specifikke påbud (FIPS 140, CNSA eller en sektorregel), der gælder, med. For virksomheds- og offentlige programmer så beslut dette, før I bygger, fordi det er dyrt, langsomt og ofte tvinger en redesign af netop de komponenter, I troede var færdige, at eftermontere validerede moduler og genautorisere et system bagefter.

## Sektorperspektiv

**Startup.** Støt jer helt til jeres platforms gennemprøvede standarder og brug nul ingeniørtid på tilpasset kryptografi. Slå administreret kryptering i hvile til, terminér TLS med automatisk fornyede certifikater, hash adgangskoder med en standard langsom funktion, og hold hemmeligheder i platformens hemmelighedshåndtering frem for repositoryet. Jeres ene designbeslutning er en tynd grænseflade omkring den håndfuld felter, I krypterer i applikationen, så et fremtidigt skifte væk fra udbyderstyrede nøgler ikke er en omskrivning.

**Lille virksomhed.** I har ingen kryptograf og lille appetit på at drive en HSM, så køb varetægt frem for at bygge den: brug den udbyderstyrede KMS og hemmelighedshåndtering, der følger med jeres cloud- eller SaaS-værktøjer. Ram arbejdet ind som hygiejne, altså ingen nøgler i kode, kryptering slået til overalt som standard og certifikatudløb overvåget, så intet lapser ved overraskelse. Forbehold kundestyrede nøgler til de sjældne data, en kontrakt eller tilsynsmyndighed reelt kræver dem til.

**Stor virksomhed.** Problemet er skala og ensartethed på tværs af tusinder af tjenester, certifikater og nøgler. Kør en centraliseret KMS med envelope-kryptering, automatisér hele certifikatlivscyklussen, så intet udløb plejes i hånden, og vedligehold én kryptoopgørelse, der fodrer rotation, FIPS-afgrænsning og post-kvanteplanlægning. Adskil nøglevaretægt fra dataadgang som en organisationsdækkende kontrol, og gør kryptering til en platformsevne, hvert team arver, frem for en opgave, hvert team genopfinder.

**Offentlig sektor.** Indkøb, validering og revision former hvert valg. Brug FIPS 140-validerede moduler og følg national vejledning såsom CNSA for klassificerede systemer, bind nøglevaretægt til dataklassificering, så de mest følsomme nøgler sidder hos klarerede medarbejdere under streng adskillelse af opgaver, og generér kontinuerlig dokumentation for valideret kryptografi til løbende autorisation. Dokumentér en post-kvantemigreringsplan for journaler, der skal forblive fortrolige i årtier, og kræv at leverandører oplyser, hvilke moduler der er validerede, før I forpligter jer.

## Eksempler

**Startup.** Et lille team, der bygger en sundhedssporingsapp, støtter sig helt til gennemprøvede standarder. De terminerer TLS med automatisk fornyede certifikater, slår kryptering i hvile til på deres administrerede database og objektlager med udbyderens KMS og hasher adgangskoder med en langsom, saltet funktion fra et standardbibliotek. I stedet for selv at skrive kryptografi bruger de et autentificeret krypteringskald på højt niveau til det ene felt, de skal kryptere i applikationen. Hemmeligheder bor i platformens hemmelighedshåndtering, aldrig i repositoryet. Det koster nogle få eftermiddage og fjerner en hel kategori af katastrofale fejl.

**Stor virksomhed.** En global bank kører en centraliseret KMS og en flåde af HSM'er med en kryptoopgørelse, der sporer hver nøgle og hvert certifikat på tværs af tusinder af tjenester. Envelope-kryptering beskytter kundedata, med datanøgler indpakket af hovednøgler, der roterer efter en plan, mens dataene bliver, hvor de er. Certifikatudstedelse og -fornyelse er fuldt automatiseret, efter et offentligt vendt nedbrud lærte dem omkostningen ved et enkelt udløbet certifikat. Nøgleadministratorer er et separat team fra applikationsingeniører, så varetægt håndhæver adskillelse af opgaver, og et lag af kryptografisk smidighed lader dem begynde at pilotere post-kvantealgoritmer til langlivede arkiver.

**Offentlig sektor.** Et nationalt agentur, der håndterer klassificerede journaler, bruger kun FIPS 140-validerede kryptografiske moduler og følger NSA CNSA-vejledning for sine systemer med højeste klassifikation. Nøgler genereres og holdes i HSM'er, der aldrig frigiver nøglemateriale i klartekst, og varetægt er bundet til dataklassificering, så de mest følsomme nøgler sidder hos klarerede medarbejdere under streng adskillelse af opgaver. Certifikater kører på en administreret intern PKI med automatiserede livscyklusser, og kontinuerlig dokumentation for valideret kryptografi fodrer agenturets løbende autorisation. En dokumenteret post-kvantemigreringsplan beskytter journaler, der skal forblive fortrolige i årtier.

## Business case: motivation, ROI og TCO

Kryptografi er endnu et område, hvor en beskeden investering forhindrer katastrofale tab af overskriftskaliber. De totale ejeromkostninger omfatter en KMS eller HSM, værktøj til hemmelighedsstyring og certifikatstyring og ingeniørtiden til at designe livscyklusser og holde en opgørelse aktuel. Disse omkostninger er reelle, men afgrænsede. Omkostningen ved at springe dem over er et brud på ukrypterede data, et nedbrud på flere timer fra et udløbet certifikat eller et uigenkaldeligt datatab fra en fejlhåndteret nøgle, hver med regulatoriske bøder, underretningsomkostninger og varig omdømmeskade.

Det stærkeste ROI kommer fra automatisering og genbrug. Automatiserede certifikatlivscyklusser eliminerer det enkeltstående mest almindelige selvforskyldte nedbrud. Centraliseret nøglestyring med fornuftige standarder betyder, at hver ny tjeneste arver kryptering under transport og i hvile uden indsats pr. team og forvandler kryptografi fra en tilbagevendende skat til en platformsevne. For regulerede og offentlige opgaver sænker validerede moduler og automatiseret dokumentation også omkostningen ved revisioner og autorisation. Når du fører sagen over for ledelsen, så ram den enkelt ind: algoritmerne er gratis og gennemprøvede, risikoen bor i nøglestyring og certifikatdrift, og en lille, automatiseret investering dér forhindrer de dyre fejl.

## Anti-mønstre og faldgruber

- **At rulle din egen kryptografi.** Tilpassede algoritmer eller håndbyggede protokoller, der fejler på subtile, kun-ekspert-måder.
- **Hårdkodede nøgler og hemmeligheder.** Legitimationer indsat i kildekode, konfigurationsfiler eller chat, hvor de lækker og ikke kan roteres.
- **Kryptering uden nøgledisciplin.** At slå kryptering til, men lade nøgleadgang stå vid åben eller aldrig rotere.
- **At forveksle hashing med kryptering.** At behandle en hash som reversibel eller gemme adgangskoder med en hurtig hash i stedet for en langsom, saltet.
- **Certifikatroulette.** Ingen opgørelse, ingen udløbsovervågning og periodiske overraskelsesnedbrud, når et certifikat lapser.
- **Sammenblandet nøglevaretægt og dataadgang.** Én identitet, der både kan styre en nøgle og læse de data, den beskytter.
- **Ingen rotationsplan.** Nøgler, der aldrig er roteret og ikke kan roteres hurtigt under pres.
- **Kryptografi uden smidighed.** Algoritmer koblet så dybt, at det kræver en omskrivning at bytte dem, hvilket blokerer enhver fremtidig migrering.
- **At ignorere valideringspåbud.** At bruge stærke algoritmer i ikke-validerede moduler, hvor FIPS eller lignende validering er påkrævet.

## Modenhedsmodel

- **Niveau 1, Opstart:** Kryptering er inkonsistent og ofte fraværende, anvendt reaktivt, når nogen lægger mærke til et hul. Nøgler og hemmeligheder er hårdkodede eller delt uformelt over chat og konfigurationsfiler. Der er ingen opgørelse, ingen rotation, og certifikater udløber ved overraskelse, og teams skriver lejlighedsvis deres egen kryptografi.
- **Niveau 2, Udvikling:** TLS og kryptering i hvile er slået til for de store systemer, og en KMS eller hemmelighedshåndtering findes, men adoptionen er ujævn og varierer fra team til team. Nogle certifikater overvåges, mens andre ikke gør, rotation er manuel og sjælden, og ingen komplet kryptoopgørelse binder det sammen.
- **Niveau 3, Standardisering:** Kryptering under transport og i hvile er den dokumenterede standard, håndhævet i hele organisationen. Nøgler bor i en KMS med planlagt rotation og envelope-kryptering, nøglevaretægt er adskilt fra dataadgang, certifikatlivscyklusser er automatiserede, en kryptoopgørelse vedligeholdes, og validerede moduler bruges, hvor regulering kræver dem.
- **Niveau 4, Styring:** Kryptoejendommen måles og styres mod baselines. I følger ledetid for certifikatudløb, procentdelen af nøgler roteret efter plan, gennemsnitlig tid til at tilbagekalde en kompromitteret nøgle, detektioner af hemmeligheder i kode pr. periode og opgørelsesdækning, og I gennemgår disse målinger mod mål. Rotation og tilbagekaldelse øves efter en kadence med registrerede tider, og afvigelser udløser korrigerende handling frem for at gå ubemærket hen.
- **Niveau 5, Orkestrering:** Kryptografi er en platformsevne, hver tjeneste arver som standard, og den forbedres løbende og er integreret på tværs af organisationen. Rotation og tilbagekaldelse er hurtige og rutinemæssigt udøvede, HSM'er beskytter nøglerne med højeste assurance, og kryptografisk smidighed plus en aktiv post-kvantemigreringsplan holder ejendommen adaptiv, efterhånden som algoritmer og påbud skifter. Compliance-dokumentation produceres automatisk og fodrer løbende autorisation.

## Idéer til drøftelse

1. Hvilke systemer i jeres ejendom retfærdiggør kundestyrede nøgler eller HSM'er, givet deres driftsomkostning og risiko for katastrofalt tab?
2. Hvordan ville I bygge og vedligeholde én kilde til sandheden for hver nøgle og hvert certifikat, I ejer?
3. Hvad er jeres realistiske tid til at rotere en kompromitteret nøgle i dag, og hvad gør den langsom?
4. Hvor gør jeres arkitektur det svært at bytte en kryptografisk algoritme, og hvordan ville I rette det før en tvungen migrering?
5. Hvilke af jeres langlivede hemmeligheder ville betyde noget, hvis en modstander høstede dem nu og dekrypterede dem år senere?
6. Havner hemmeligheder og nøgler nogensinde i kode, konfiguration eller logs, og hvordan ville I vide det?

## Vigtigste pointer

- **Rul ikke din egen kryptografi.** Brug gennemprøvede biblioteker og standardalgoritmer på det højeste sikre abstraktionsniveau.
- **Algoritmer er lette; nøglestyring er svær.** Nøglens livscyklus (generering, distribution, rotation, tilbagekaldelse, destruktion) er der, hvor reelle fejl bor.
- **Kend jeres garantier:** symmetrisk og offentlig-nøgle-kryptering beskytter fortrolighed, signaturer beviser ægthed og integritet, og hashing opdager manipulation, men er ikke kryptering.
- **Krypter under transport med aktuel TLS og i hvile med envelope-kryptering**, som standard for hvert system.
- **Adskil nøglevaretægt fra dataadgang**, brug en KMS til nøgler og en hemmelighedshåndtering til legitimationer, og hårdkod aldrig nogen af dem.
- **Automatisér certifikatlivscyklusser** for at dræbe nedbruddet ved overraskelsesudløb, og hold en kryptoopgørelse.
- **Byg til kryptografisk smidighed** og start en post-kvantemigreringsplan for langlivede hemmeligheder.
- **Foretræk validerede implementeringer** (FIPS 140 og gældende national vejledning), hvor regulering eller klassificering kræver dem.

## Referencer og videre læsning

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
