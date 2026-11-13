# 4.2 Applikationssikkerhed

## Overblik og motivation

Applikationssikkerhed er der, hvor abstrakte trusler møder konkret kode. De fleste brud, der når overskrifterne, kan spores til en fejl i applikationslaget: en injektion, et ødelagt autentificeringsflow, en blotlagt hemmelighed eller en kompromitteret afhængighed. For store teams, der leverer mange tjenester, er det svære ikke at vide, at disse fejl findes. Det er at forebygge dem konsekvent på tværs af en udstrakt kodebase skrevet af tusinder af hænder over mange år.

For virksomheder er applikationssikkerhed et spørgsmål om kundetillid og regulatorisk forpligtelse. En fejl i et loginflow eller en betalingssti kan udløse svindel, bøder og obligatorisk offentliggørelse af brud. Offentlige systemer står over for de samme tekniske risici med data af højere indsats: ydelsesberettigelse, skatteposter, retsplejedata og national infrastruktur. I begge sammenhænge er applikationen hoveddøren, og angribere prøver den konstant og automatisk.

Dette kapitel dækker de praksisser, der holder applikationer modstandsdygtige: at kende og forsvare sig mod de almindelige sårbarhedsklasser, validere input og kode output, få autentificering og autorisation rigtigt, håndtere hemmeligheder og sikre den softwareforsyningskæde, der i stigende grad afgør jeres reelle angrebsflade.

*Se også:* kapitel 4.1 (sikkerhedsgrundlag, trusselsmodellering og den sikre udviklingslivscyklus), kapitel 10.3 (open source-forsyningskæde og licensering) og kapitel 10.2 (SBOM'er, risiko og assurance).

## Grundprincipper

- **Stol aldrig på input.** Behandl alle data, der krydser en tillidsgrænse, som fjendtlige, til de er valideret.
- **Sikre standarder.** Den sikre sti bør være den lette sti; usikker adfærd bør kræve bevidst, synlig indsats.
- **Fejl lukket.** Når et sikkerhedstjek ikke kan gennemføres, så nægt adgang frem for at tillade den.
- **Forsvar i dybden i applikationslaget.** Kombinér validering, kodning, parametrisering og frameworkbeskyttelser; stol ikke på én.
- **Mindste privilegium for identiteter og tokens.** Afgræns legitimationer snævert og lad dem udløbe hurtigt.
- **Dine afhængigheder er din kode.** Du er ansvarlig for sikkerheden af alt, du leverer, herunder tredjeparts- og open source-komponenter.
- **Standarder frem for improvisation.** Brug gennemprøvede rammeværker som [OWASP](https://en.wikipedia.org/wiki/OWASP)'s (Open Worldwide Application Security Project) ASVS frem for at opfinde dine egne sikkerhedskontroller.

## Anbefalinger

### Kend og forsvar OWASP Top 10, verificér med ASVS

OWASP Top 10 er branchens basisliste over de mest kritiske risici for webapplikationer: ødelagt adgangskontrol, kryptografiske fejl, injektion, usikkert design, sikkerhedsfejlkonfiguration, sårbare komponenter, autentificeringsfejl, dataintegritetsfejl, logningsfejl og server-side request forgery. Behandl den som påkrævet viden for hver ingeniør, ikke blot en compliance-reference at lægge væk.

Til en stringent, testbar standard så adoptér **OWASP Application Security Verification Standard (ASVS)**. ASVS definerer sikkerhedskrav på tre assurance-niveauer og giver jer konkrete, reviderbare kontroller at designe og teste mod. Vælg det niveau, der passer til hver applikations risiko, og verificér mod det.

### Validér input og kod output

Injektionsfejl forbliver blandt de mest skadelige netop fordi de er så lette at introducere. Forsvar med lagdelte kontroller:

- **Validér input** mod strenge tilladelseslister (forventet type, længde, format, interval). Afvis frem for at rense, hvor I kan.
- **Brug parametriserede forespørgsler** og [prepared statements](https://en.wikipedia.org/wiki/Prepared_statement) til al databaseadgang; byg aldrig SQL ved strengsammenkædning. Brug sikre forespørgselsbyggere og ORM'er (object-relational mappers) korrekt.
- **Kod output** kontekstuelt. HTML, HTML-attributter, JavaScript, URL'er og CSS kræver hver forskellig kodning. Støt dig til frameworkets automatiske escaping og forstå dets grænser.
- **Forebyg [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** med outputkodning plus en stærk Content Security Policy som andet lag.
- **Forebyg kommando- og skabelonindsprøjtning** ved at undgå at kalde skallen med ubetroede data og ved at bruge logikfri eller sandboxede skabeloner.

### Få autentificering og autorisation rigtigt

Autentificering beviser, hvem en bruger er. Autorisation afgør, hvad de må. Begge fejler ofte, så få dem rigtige.

- Foretræk etablerede protokoller: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** til delegeret autorisation og **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** til autentificering. Byg dem ikke fra bunden.
- Håndhæv **[multifaktorautentificering](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, især for privilegeret og administrativ adgang.
- Gem kun adgangskoder som saltede hashes med en moderne, langsom, hukommelsestung algoritme (såsom [Argon2](https://en.wikipedia.org/wiki/Argon2) eller [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Gem eller log aldrig legitimationer i klartekst.
- Håndtér **sessioner** omhyggeligt: generér kryptografisk stærke tokens, sæt secure- og HttpOnly-cookieflag, roter ved privilegieændring og lad inaktive sessioner udløbe.
- Håndhæv **autorisation på serveren for hver anmodning**, og tjek at den autentificerede part ejer eller må tilgå den specifikke ressource. Ødelagt autorisation på objektniveau (at tilgå en anden brugers post ved at ændre et ID) er en af de mest almindelige og alvorlige API-fejl.
- Centralisér autorisationslogik, hvor det er praktisk, så politikken er ensartet og reviderbar.

### Håndtér hemmeligheder og roter nøgler

Hårdkodede hemmeligheder i kildekode er en evig årsag til brud. Byg en disciplineret vane omkring hemmelighedsstyring:

- Gem hemmeligheder i en dedikeret hemmelighedshåndtering eller vault, aldrig i kildekode, konfigurationsfiler eller miljøvariabler indtjekket i versionsstyring.
- Scan commits og repositories automatisk for lækkede hemmeligheder, og bloker merges, der introducerer dem.
- Roter nøgler og legitimationer regelmæssigt og straks ved mistanke om eksponering. Foretræk kortlivede, automatisk udstedte legitimationer frem for langlivede statiske.
- Anvend mindste privilegium på hver hemmelighed: afgræns den til præcis det, den har brug for.
- Krypter hemmeligheder i hvile og under transport, og revidér adgang til dem.

### Sikr softwareforsyningskæden

Moderne applikationer er for det meste samlet af tredjepartskomponenter, hvilket gør forsyningskæden til en primær angrebsflade.

- Vedligehold en **[softwarestykliste](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** for hver applikation, så I ved præcis, hvad I leverer, og kan reagere hurtigt, når en ny sårbarhed lander.
- Scan afhængigheder kontinuerligt (Software Composition Analysis, eller SCA), og udbedr kendt sårbare komponenter prompte.
- Fastlås og verificér afhængighedsversioner; brug låsefiler og betroede registre.
- Adoptér **SLSA** (Supply-chain Levels for Software Artifacts) for at løfte byggeintegritet, og generér **proveniens**-attesteringer, der beskriver, hvordan artefakter blev bygget.
- **Signér artefakter** og verificér signaturer før udrulning, så I kan stole på, at det, der kører, er det, I byggede.
- Sikr selve byggesystemet; en kompromitteret CI-pipeline kan indsprøjte ondsindet kode i hver nedstrøms forbruger.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Køb/adoptér identitetsudbyder (OIDC) | Gennemprøvet, MFA indbygget, mindre kode at sikre | Leverandøravhængighed, integrationsindsats, omkostning |
| Byg tilpasset autentificering | Fuld kontrol, ingen ekstern afhængighed | Ekstremt let at få forkert, høj vedligeholdelse |
| Streng tilladelsesliste-validering | Blokerer hele sårbarhedsklasser | Kan bryde legitime grænsetilfælde, mere arbejde på forhånd |
| Kortlivede legitimationer | Lille brudvindue, automatisk tilbagekaldelse | Kræver robust udstedelsesinfrastruktur |
| Aggressive afhængighedsopdateringer | Færre kendte sårbarheder | Uro, potentielle brydende ændringer, testbyrde |
| SBOM + signering + proveniens | Hurtig hændelsesrespons, verificerbar tillid | Investering i værktøj og proces, kulturændring |

Den tilbagevendende afvejning er stringens på forhånd versus løbende eksponering. At bygge tilpasset autentificering eller springe afhængighedshygiejne over føles hurtigere i dag og koster jer enormt senere. At adoptere gennemprøvede standarder og automatiserede forsyningskædekontroller koster indsats nu, men forvandler en ubegrænset, uforudsigelig risiko til en styret, afgrænset. For store teams betyder automatiseringsmultiplikatoren mest: en kontrol anvendt én gang i en asfalteret skabelon beskytter hver tjeneste, der bruger den.

## Spørgsmål til drøftelse med dit team

1. **Hvilke ASVS-kontroller vil I bage ind i jeres asfalterede framework, så ingeniører får dem gratis?** Den mest virkningsfulde handling for et stort team er at gøre den sikre sti til standard, så en kontrol skrevet én gang i et fælles framework beskytter hver tjeneste, der adopterer det. Beslut, hvilke ASVS-krav (parametriserede forespørgsler, outputkodning, sikre sessionsflag, server-side autorisationstjek) der hører hjemme i skabelonen frem for i hver ingeniørs hukommelse. For virksomheds- og offentlige porteføljer så beslut også, hvilke applikationer der har brug for ASVS niveau 2 versus niveau 3, og bind det til følsomheden af de data, hver rører. Tag en liste over jeres tjenester med og markér, hvilke der allerede arver disse standarder, og hvilke der genimplementerer sikkerhed i hånden, for de håndlavede er, hvor injektion og ødelagt adgangskontrol gemmer sig. Hvis sikre standarder kun bor på en wikiside, bliver de sprunget over under leveringspres, så læg dem i kode.

2. **Hvordan vil I finde og rette ødelagt autorisation på objektniveau på tværs af hver API, ikke kun de nye?** At tilgå en anden brugers post ved at ændre et ID er en af de mest almindelige og alvorlige API-fejl, og den gemmer sig i ældre endepunkter, der er ældre end jeres nuværende standarder. Server-side autorisation på hver anmodning og hvert objekt er reglen, men det svære er at verificere, at den holder på tværs af en udstrakt, årevis gammel kodebase skrevet af mange hænder. Beslut, om I vil centralisere autorisationslogik, tilføje automatiserede tests, der forsøger adgang på tværs af tenants, eller køre målrettet test mod jeres højrisiko-API'er først. Tag jeres opgørelse over endepunkter, der eksponerer objektidentifikatorer, med og rangér dem efter følsomheden af det, de returnerer. Uden en bevidst gennemgang vil I blive ved med at levere denne fejl og opdage den først, når en forsker eller en angriber gør.

3. **Hvad er jeres plan for den næste udbredte afhængighedssårbarhed: hvor hurtigt kan I finde og patche hver berørt tjeneste?** Når en kritisk fejl lander i et populært bibliotek, identificerer de virksomheder med en nøjagtig SBOM berørte tjenester på timer, mens andre bruger uger på at lede, og det hastighedshul afgør, hvor megen skade I tager. Beslut nu, om I producerer en softwarestykliste for hvert artefakt, om afhængighedsscanning kører i hver pipeline, og hvem der ejer nødpatchbeslutningen. For regulerede og offentlige købere er SBOM'er og signeret proveniens i stigende grad en betingelse for at gøre forretning, så denne beredskab beskytter også omsætning. Tag det ærlige resultat af en øvelse med: vælg et bibliotek, I bruger bredt, og tag tid på, hvor lang tid det tager at liste hver tjeneste, der leverer det. Hvis svaret måles i dage, så invester i opgørelse og signering, før den næste hændelse tvinger jer.

4. **Hvordan vil I bevæge jer fra langlivede statiske hemmeligheder til kortlivede, automatisk udstedte legitimationer, og hvilke systemer blokerer det i dag?** Hårdkodede og langlivede hemmeligheder er en evig brudårsag, og rettelsen, kortlivede legitimationer udstedt efter behov, afhænger af udstedelsesinfrastruktur, ældre systemer ofte ikke kan bruge. For et stort team er faren ujævn adoption: en moderne platform roterer nøgler hver time, mens en legacy-tjeneste stadig leverer en statisk databaseadgangskode i en konfigurationsfil. Beslut, hvilke arbejdsbyrder der kan forbruge en hemmelighedshåndtering eller et arbejdsbyrdeidentitetssystem nu, hvilke der har brug for investering først, og hvem der ejer rotationsrunbooken i det øjeblik, en nøgle mistænkes lækket. Tag en opgørelse over hver legitimation i brug med, dens levetid, dens sprængradius, hvis den eksponeres, og om commit-scanning ville fange den før merge. I virksomheds- og offentlige sammenhænge så bind dette til revision: eksaminatorer forventer i stigende grad dokumentation for rotation, afgrænset adgang og adgangslogning for hver hemmelighed, og en statisk legitimation, I ikke kan rotere uden nedetid, er et fund, der venter på at blive skrevet op.

5. **Hvor kører I stadig hjemmelavet eller inkonsistent autentificering, og hvad er planen for at konsolidere på gennemprøvede protokoller?** At bygge autentificering er en af de letteste måder at introducere subtile, udnyttelige fejl på, men alligevel bærer de fleste store ejendomme mindst ét legacy-loginflow, der er ældre end beslutningen om at standardisere på OAuth 2.0 og OIDC. De konkurrerende pres er reelle: at migrere et gammelt flow risikerer at bryde eksisterende brugere og integrationer, mens det at lade det stå holder et højværdimål underforsvaret. Beslut, om I konsoliderer på en enkelt identitetsudbyder, håndhæver MFA ensartet og sætter en frist for at pensionere hvert skræddersyet flow, eller accepterer dokumenterede undtagelser med kompenserende kontroller. Tag et kort over hver autentificeringssti i flåden med, hvilke der håndhæver MFA, hvilke der gemmer adgangskoder med en moderne hukommelsestung hash, og hvilke der er tilpassede. For virksomheds- og offentlige porteføljer så tilføj compliancevinklen: standarder som NIST SP 800-63 sætter konkrete forventninger til identitetsassurance, og et hjemmelavet flow, der ikke kan demonstrere dem, overlever ikke en revision eller en authority-to-operate-gennemgang.

6. **Hvordan verificerer I, at disse kontroller faktisk holder i produktion, og kan I bevise det med dokumentation frem for påstand?** At skrive en sikker standard er ikke det samme som at vide, at hver tjeneste stadig overholder den, og kontroller rådner stille, efterhånden som kode ændrer sig, undtagelser hober sig op, og nye endepunkter udgives. For et stort team er spørgsmålet dækning: hvilke tjenester kører statisk analyse, afhængighedsscanning og dynamisk test eller penetrationstest, og hvordan ved I, at dem, der springer dem over, ikke er jeres højrisikoapplikationer? Beslut, hvilken verifikation der er obligatorisk i pipelinen versus periodisk, hvem der triagerer fundene, og hvilken dokumentation I beholder for at vise, at en kontrol blev testet og bestod på en given dato. Tag jeres nuværende dækningskort, jeres gennemsnitlige tid til udbedring efter alvorlighed og listen over applikationer uden nylig test med. I regulerede og offentlige sammenhænge er denne dokumentation ikke valgfri: revisorer, godkendende embedsmænd og brudundersøgere beder alle om bevis for, at kontroller blev verificeret, og en politik uden testoptegnelser tilfredsstiller dem sjældent.

## Sektorperspektiv

**Startup.** Med to eller tre ingeniører og ingen sikkerhedsspecialist er din løftestang at arve sikkerhed frem for at bygge den: adoptér en administreret OIDC-identitetsudbyder, støt dig til et framework, hvis ORM parametriserer forespørgsler som standard, og hold hemmeligheder i din platforms hemmelighedshåndtering frem for `.env`-filer, et kollega ved et uheld kunne committe. Slå automatiseret afhængighedsscanning til, der åbner patch-pull requests, og behandl det som nok for nu. Byg ikke tilpasset autentificering eller kryptografi, for en enkelt indsprøjtet forespørgsel eller én lækket nøgle kan ende virksomheden, før den har kunder.

**Lille virksomhed.** I har sandsynligvis ingen applikationssikkerhedsspecialist og et stramt budget, så køb kontroller indlejret i de værktøjer og platforme, I allerede betaler for, frem for at bemande en dedikeret funktion. Vælg en hostet identitetsudbyder med MFA inkluderet, en administreret database der styrer jer mod parametriseret adgang og en repositoryvært, der scanner commits for lækkede hemmeligheder ud af boksen. Koncentrér jeres knappe opmærksomhed om OWASP Top 10-grundprincipperne, der forårsager de fleste reelle brud, og foretræk leverandører, der leverer sikre standarder, I ikke tilfældigt kan slå fra.

**Stor virksomhed.** På tværs af mange teams er udfordringen ensartethed: bag ASVS-kontroller ind i asfalterede frameworks, så hver ny tjeneste arver parametriserede forespørgsler, outputkodning, sikre sessioner og server-side autorisation gratis. Kør nøjagtige SBOM'er og afhængighedsscanning på tværs af flåden, så den næste udbredte biblioteksårbarhed er et spørgsmål om timer, ikke uger, og centralisér autorisationspolitik, så adgang på tværs af tenants bliver testbar. Standardisér på én identitetsudbyder med håndhævet MFA, og styr applikationssikkerhed som en styret portefølje med risikoopdelte ASVS-niveauer og revideret dokumentation.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former de kontroller, I skal demonstrere, ikke blot implementere. Verificér borgervendte tjenester mod OWASP ASVS på et niveau afstemt til datafølsomhed, signér hvert udrullet artefakt og attestér dets proveniens efter SLSA for at opfylde forsyningskædepåbud, og udsted kortlivede legitimationer fra en central vault med fuld adgangslogning. Forvent at skulle vise revisorer og godkendende embedsmænd en dokumenteret kæde af kontrol fra kilde til produktion, og afstem identitetsassurance til offentliggjorte standarder som NIST SP 800-63.

## Eksempler

**Startup.** Et SaaS-team på tre ingeniører springer over at bygge sit eget login og adopterer en administreret OIDC-udbyder fra dag ét, hvilket giver MFA og sikre nulstillinger af adgangskoder uden at skrive sikkerhedskritisk kode, de ikke har råd til at få forkert. Det støtter sig til frameworkets ORM, så forespørgsler er parametriserede som standard, holder hemmeligheder i platformens hemmelighedshåndtering frem for i `.env`-filer, en kollega ved et uheld kunne committe, og slår automatiseret afhængighedsscanning til, der åbner en pull request, når et bibliotek skal patches. Intet af dette sinker teamet, og det betyder, at én lækket nøgle eller én indsprøjtet forespørgsel ikke ender virksomheden, før den har kunder.

**Stor virksomhed.** En detailplatform, der betjener titusinder af millioner af shoppere, standardiserer autentificering på OIDC gennem en enkelt identitetsudbyder og håndhæver MFA for medarbejdere og step-up-autentificering for højværdi-kontoændringer. Al databaseadgang går gennem et ORM konfigureret til at parametrisere forespørgsler, og en Content Security Policy bakker outputkodningen op. Efter en vidt omtalt sårbarhed i et populært logningsbibliotek lader virksomhedens SBOM den identificere hver berørt tjeneste inden for timer og patche dem på to dage, mens konkurrenter uden opgørelser brugte uger på at lede.

**Offentlig sektor.** Et føderalt ydelsesagentur bygger borgervendte tjenester verificeret mod OWASP ASVS niveau 2, med niveau 3 for de komponenter, der håndterer de mest følsomme poster. Hemmeligheder bor i en central vault, der udsteder kortlivede legitimationer; commit-scanning blokerer enhver lækket nøgle. Hvert udrullet artefakt er signeret, og dets proveniens er attesteret efter SLSA, hvilket opfylder et føderalt påbud om verificerbare softwareforsyningskæder og giver revisorer en klar kæde af kontrol fra kilde til produktion.

## Business case: motivation, ROI og TCO

Udgifter til applikationssikkerhed køber den mest sandsynlige og dyreste kategori af brud ned. De totale ejeromkostninger omfatter værktøj (scannere, hemmelighedshåndteringer, identitetsudbydere), ingeniørtid til at udbedre fund og den milde gnidning ved sikre standarder. Sæt mod det omkostningen ved at springe det over: injektions- og ødelagt-adgangskontrol-brud eksponerer rutinemæssigt millioner af poster og udløser regulatoriske bøder, obligatorisk underretning, svindeltab, udbedringssprints og omdømmeskade, der undertrykker omsætning i årevis.

ROI er stærkest, når kontroller er automatiserede og genbrugte. En enkelt velkonfigureret identitetsintegration, ét hærdet forespørgselslag i et fælles framework og én pipeline, der blokerer sårbare afhængigheder, beskytter hele flåden til marginal omkostning pr. tjeneste. Forsyningskædekontroller i særdeleshed er gået fra valgfrie til essentielle: en kompromitteret afhængighed kan gøre hver af jeres kunder til et offer, og tilsynsmyndigheder og virksomhedskøbere kræver i stigende grad SBOM'er og signeret proveniens som betingelse for at gøre forretning. Når du fører sagen over for ledelsen, så bind investeringen til specifikke, navngivne risici og til indkøbs- og compliancekrav, der blokerer omsætning, hvis I ikke opfylder dem.

## Anti-mønstre og faldgruber

- **At rulle din egen kryptografi eller autentificering.** Producerer næsten altid subtile, udnyttelige fejl.
- **Validering kun på klientsiden.** Trivielt omgået; serveren må genvalidere alt.
- **Blokeringslistesanering.** At forsøge at fjerne "dårlige" tegn i stedet for at tilladelseslistere gode; angribere finder hullerne.
- **Hemmeligheder i kildekode eller miljøfiler.** Den enkeltstående mest almindelige årsag til legitimationslæk.
- **At ignorere autorisation ved objektadgang.** At antage at en autentificeret bruger må tilgå ethvert objekt, hvis ID de kan gætte.
- **Sæt-og-glem-afhængigheder.** Aldrig at opdatere tredjepartskomponenter, til et brud tvinger det.
- **At behandle Top 10 som målstregen.** Den er et gulv, ikke en omfattende standard; brug ASVS til dybde.
- **Logning af følsomme data.** Adgangskoder, tokens og PII (personligt identificerbare oplysninger) i logs bliver et brud, der venter på at ske.

## Modenhedsmodel

**Niveau 1: Opstart.** Applikationssikkerhed afhænger af individuel udviklerviden og reagerer kun efter hændelser. Ingen standardkontroller. Hemmeligheder sidder i kildekode. Afhængigheder opdateres sjældent. Autentificering er tilpasset og ad hoc, og injektions- eller ødelagt-adgangskontrol-fejl findes ved held frem for ved proces.

**Niveau 2: Udvikling.** Grundlæggende praksis dukker op, men varierer fra team til team. OWASP Top 10-bevidsthed spreder sig, nogle beskyttelser på frameworkniveau er på plads, og en hemmelighedshåndtering findes, men bruges ujævnt. Afhængighedsscanning kører lejlighedsvis. Nye systemer adopterer en standard identitetsudbyder, mens ældre tjenester beholder deres hjemmelavede loginflow urørt.

**Niveau 3: Standardisering.** Kontroller er dokumenteret og håndhævet i hele organisationen. ASVS-baserede krav er sat pr. risikoniveau, parametriserede forespørgsler og outputkodning er normen, og en central identitetsudbyder med MFA er påkrævet. Hemmeligheder styres og scannes automatisk, SBOM'er produceres, og afhængighedsscanning kører i hver pipeline.

**Niveau 4: Styring.** Praksissen måles og styres mod baselines. Scannings- og testdækning, gennemsnitlig tid til udbedring efter alvorlighed, andelen af tjenester, der arver asfalterede standarder, alder på rotation af legitimationer og hemmeligheder og ASVS-overensstemmelse følges alle på dashboards. Undtagelser logges med udløbsdatoer, afvigelse fra baseline udløser handling, og udgivelser lukkes på definerede sikkerhedstærskler frem for på skøn.

**Niveau 5: Orkestrering.** Sikkerhed forbedres løbende og er integreret i hele organisationen. Sikre standarder er bygget ind i asfalterede frameworks, så den sikre sti er automatisk, kortlivede legitimationer bruges overalt, og fuld forsyningskædeassurance med signering og proveniens (SLSA) er standard. Verifikation er kontinuerlig, responsen på nye sårbarheder er hurtig og målt, og hver hændelse føres tilbage i de fælles skabeloner, så en enkelt rettelse hærder hele flåden.

## Idéer til drøftelse

1. Hvor bør autorisationslogik bo for at være både ensartet og vedligeholdelig på tværs af mange tjenester?
2. Hvor aggressivt bør I opdatere afhængigheder, givet afvejningen mellem eksponering og uro?
3. Hvilket ASVS-niveau er passende for hver klasse af applikationer i jeres portefølje?
4. Hvordan eliminerer I langlivede hemmeligheder uden at skabe skrøbelig udstedelsesinfrastruktur?
5. Hvad ville der skulle til for, at jeres organisation producerer og forbruger SBOM'er og proveniens for hvert artefakt?
6. Hvordan forhindrer I, at sikre standarder bliver slået fra under leveringspres?

## Vigtigste pointer

- OWASP Top 10 er essentiel viden; ASVS giver den testbare standard.
- Læg inputvalidering, parametrisering og outputkodning i lag for at slå injektion og XSS.
- Brug gennemprøvede protokoller (OAuth 2.0, OIDC) og håndhæv MFA; byg aldrig autentificering fra bunden.
- Håndhæv autorisation på serveren for hver anmodning og hvert objekt.
- Hold hemmeligheder ude af kildekode, styr dem centralt, og roter til kortlivede legitimationer.
- Forsyningskæden er en primær angrebsflade; brug SBOM'er, SCA, signering og proveniens (SLSA).
- Automatiserede, genbrugelige kontroller beskytter hele flåden til marginal omkostning pr. tjeneste.

## Referencer og videre læsning

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
