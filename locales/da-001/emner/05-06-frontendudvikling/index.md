# 5.6 Frontendudvikling

## Overblik og motivation

Frontendudvikling er disciplinen at bygge det klientvendte lag af software: den kode, der kører i browseren eller på enheden og forvandler designs, indhold og data til en fungerende grænseflade. Den spænder over framework- og arkitekturvalg, gengivelsesstrategi, tilstandsstyring, ydeevne og robusthed på tværs af den enorme mangfoldighed af browsere, enheder og netværksforhold i den virkelige verden. Frontenden er der, hvor alt det opstrøms arbejde (UX, design, indhold, tilgængelighed, internationalisering) enten når brugeren med succes eller falder fra hinanden.

For store teams er frontenden unikt udfordrende, fordi den er eksponeret for et miljø, organisationen ikke kontrollerer. Brugeres browsere, enheder, forbindelser og indstillinger varierer vildt, og platformen (nettet) udvikler sig løbende. I skala akkumulerer arkitekturvalg. Et framework valgt i dag begrænser ansættelse, ydeevne og vedligeholdelse i årevis, og tusinder af små beslutninger om bundlestørrelse og gengivelse summerer til den oplevelse, brugerne faktisk får. Fælles standarder, komponentbiblioteker, ydeevnebudgetter og arkitekturmønstre er det, der forhindrer mange uafhængige teams i at producere en langsom, inkonsistent, skrøbelig helhed.

Relevansen for virksomheder og det offentlige er akut. Virksomheder vedligeholder langlivede applikationer, hvor frameworks' levetid og vedligeholdelsesvenlighed betyder mere end nyhed, og hvor mange teams skal interoperere. Det offentlige betjener hele befolkningen, herunder mennesker på gamle enheder, langsomme eller målte forbindelser og hjælpeteknologier. Det gør ydeevne, [progressiv forbedring](https://en.wikipedia.org/wiki/Progressive_enhancement) og robusthed til ikke valgfri finish, men til forskellen mellem en tjeneste, der virker for alle, og en, der udelukker de mindst begunstigede. En offentlig tjeneste, der kun virker på den nyeste telefon med en hurtig forbindelse, svigter sit mandat.

## Grundprincipper

- Frontenden kører i et miljø, du ikke kontrollerer; design til variation og fejl.
- Vælg kedelig, holdbar teknologi til langlivede systemer; optimér for vedligeholdelsesvenlighed og ansættelse.
- Ydeevne er en funktion og for mange brugere en forudsætning for adgang.
- Progressiv forbedring: lever først en fungerende kerneoplevelse, og læg så forbedringer ovenpå.
- Send mindre kode; den hurtigste og mest pålidelige kode er den, du ikke leverer.
- Afstem gengivelsesstrategi med indholdstype og brugerbehov, ikke med mode.
- Robusthed: grænsefladen bør forringes elegant, ikke gå i stykker, når noget går galt.
- Standarder og platformsfunktioner overlever frameworks; læn dig op ad platformen.

## Anbefalinger

### Vælg frameworks efter levetid og pasform, ikke hype

Vælg frontendteknologi ud fra problemet, teamet, vedligeholdelseshorisonten og ansættelsesmarkedet, ikke ud fra hvad der trender. For langlivede virksomheds- og offentlige systemer foretræk modne, velunderstøttede teknologier med store talentpuljer, stabile udgivelsespraksisser og klare opgraderingsstier. Vej de samlede omkostninger ved framework-uro: omskrivninger er dyre og risikable. Foretræk tilgange, der læner sig op ad [webstandarder](https://en.wikipedia.org/wiki/Web_standards), så jeres investering overlever framework-udskiftning, og isolér frameworkspecifik kode bag grænser, så applikationen ikke er gidsel for ét biblioteks livscyklus.

### Afstem gengivelsesstrategi med behovet

De vigtigste gengivelsesstrategier passer hver til forskelligt indhold. Server-side rendering (SSR) producerer hurtig første visning og god SEO ([søgemaskineoptimering](https://en.wikipedia.org/wiki/Search_engine_optimization)) og virker uden klient-JavaScript, hvilket passer til indholdstunge og offentligt vendte sider. [Statisk site-generering](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) præ-gengiver ved byggetidspunktet for maksimal hastighed og cachebarhed, ideelt til indhold, der sjældent ændres. Client-side rendering (CSR) passer til meget interaktive app-lignende oplevelser bag autentificering. Streaming og progressiv hydrering sender og aktiverer siden trinvis, så brugere ser og bruger indhold hurtigere. Mange store systemer blander disse pr. rute frem for at vælge én globalt. Styr tilstand bevidst: hold servertilstand, URL-tilstand og lokal UI-tilstand adskilt, og undgå at overcentralisere alt i ét tungt globalt lager.

### Behandl ydeevne som en budgetteret, målt disciplin

Adoptér ydeevnebudgetter (eksplicitte grænser for bundlestørrelse, antal anmodninger og nøglemålinger) og håndhæv dem i CI, så regressioner fejler buildet. Følg Core Web Vitals (indlæsning, interaktivitet og visuel stabilitet) med realbrugermonitorering fra faktiske enheder og netværk, ikke blot laboratorietests på hurtige maskiner. Reducér JavaScript aggressivt: kodedel og [lazy-load](https://en.wikipedia.org/wiki/Lazy_loading), så brugere kun henter det, en given visning har brug for, udskyd ikke-kritisk arbejde, og foretræk platformsmuligheder frem for tunge biblioteker. Optimér billeder og skrifttyper, cache effektivt, og mål på repræsentative lavtydende enheder og langsomme forbindelser.

### Byg med progressiv forbedring og robusthed

Start fra en baseline, der virker med semantisk HTML og minimal eller ingen JavaScript, og forbedr så for kapable klienter. Det sikrer, at kerneopgaven forbliver mulig, når scripts ikke indlæses, en enhed er gammel, eller et netværk er ustabilt, en almindelig virkelighed frem for et grænsetilfælde. Håndtér fejl elegant: vis nyttige tilstande for indlæsning, tom, fejl og offline frem for blanke skærme eller uendelige spinnere. For tjenester, folk er afhængige af, overvej offline-first-teknikker, så appen forbliver brugbar gennem intermitterende forbindelse og synkroniserer, når forbindelsen vender tilbage.

### Sikr kompatibilitet på tværs af browsere, enheder og hjælpeteknologi

Test på tværs af de browsere, enheder og hjælpeteknologier, jeres brugere faktisk har, informeret af reel analyse frem for teamets egne maskiner. Brug progressiv forbedring og funktionsdetektion frem for at antage, at de nyeste platformsfunktioner er tilgængelige overalt. Byg [responsivt](https://en.wikipedia.org/wiki/Responsive_web_design) (se kapitlet om designsystemer), så én kodebase betjener telefoner til desktops. Integrér tilgængelighed og internationalisering i frontendarkitekturen fra start, ikke som senere gennemgange.

### Styr frontenden som fælles infrastruktur

Lever fælles komponentbiblioteker, linting, formatering og byggeværktøj, så teams er ensartede og produktive. Etablér arkitekturretningslinjer (hvordan man strukturerer applikationer, styrer tilstand og deler bundles) og ydeevnebudgetter håndhævet i CI. For meget store frontender kan I overveje modulære eller micro-frontend-arkitekturer, der lader teams udrulle uafhængigt, men vej den ekstra kompleksitet og ydeevneomkostning omhyggeligt, da de ikke er gratis.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Populært modent framework | Stor talentpulje, stabilt, understøttet | Kan bære arvet vægt; langsommere at adoptere de nyeste funktioner |
| Nyeste framework | Moderne funktioner, ydeevnegevinster | Risiko for uro, lille talentpulje, usikker levetid |
| SSR / SSG | Hurtig første visning, SEO, virker uden JS | Server- eller byggekompleksitet, caching-udfordringer |
| CSR (SPA) | Rig interaktivitet, app-lignende følelse | Langsom første indlæsning, JS-afhængig, SEO- og robusthedsomkostning |
| Tung klient-JavaScript | Rige funktioner | Dårlig ydeevne på lavtydende enheder, skrøbelig |
| Progressiv forbedring | Robust, inkluderende, virker overalt | Mere designindsats for at definere en fungerende baseline |
| Micro-frontends | Uafhængige team-udrulninger, skala | Kompleksitet, duplikerede afhængigheder, ydeevneoverhead |

Den tilbagevendende afvejning er rigdom og udviklerbekvemmelighed versus rækkevidde, ydeevne og robusthed. Tunge klientsidetilgange er behagelige at bygge og demonstrere på hurtige maskiner, men de udelukker brugere på svage enheder og netværk. For virksomheds- og især offentlige målgrupper skal balancen vippes mod ydeevne, progressiv forbedring og holdbarhed, fordi omkostningen ved at udelukke brugere er høj og ofte ikke til forhandling.

## Spørgsmål til drøftelse med dit team

1. **Hvordan isolerer vi frameworkspecifik kode, så applikationen ikke er gidsel for ét biblioteks livscyklus?** For langlivede virksomheds- og offentlige systemer er framework-uro den største undgåelige udgift: en omskrivning er dyr og risikabel, og dagens trendende bibliotek begrænser ansættelse og vedligeholdelse i årevis. At læne sig op ad webstandarder og placere frameworkspecifik kode bag klare grænser betyder, at jeres forretningslogik og jeres indhold overlever den næste framework-udskiftning. Beslut, hvor disse sømme er, og om en ny ingeniør kunne skelne platformskode fra frameworkkode. Tag et estimat af, hvad jeres seneste framework-migrering kostede, eller hvad den kommende vil koste, med. Hvis jeres kernelogik er svejset til ét biblioteks API'er, så prissæt den kobling, før I forsvarer framework-valget.

2. **Afstemmer vi gengivelsesstrategi pr. rute, eller tvinger vi én strategi på hele produktet?** Server-side rendering giver hurtig første visning og virker uden klient-JavaScript for offentligt indhold, statisk generering maksimerer hastigheden for sider, der sjældent ændres, og klientgengivelse passer til interaktive app-lignende flader bag login. At tvinge én globalt enten sinker offentlige sider med tung JavaScript eller overkonstruerer en simpel indholdsside. Dette er et rækkeviddespørgsmål for det offentlige, hvor en tjeneste, der kun virker, når en stor bundle er indlæst, udelukker brugere på gamle enheder og langsomme forbindelser. Tag jeres nøgleruter med og mærk hver med den strategi, den faktisk bruger i dag. Hvis en offentligt vendt side har brug for JavaScript for at vise sit indhold, så beslut, om det er et bevidst valg eller et uheld.

3. **Hvor disciplineret er vores tilstandsstyring, og overcentraliserer vi alt i ét tungt globalt lager?** At holde servertilstand, URL-tilstand og lokal UI-tilstand adskilt forebygger den kobling og de gengivelsesstorme, der gør store frontender langsomme og skrøbelige, men den fristende standard er at dumpe alt i ét globalt lager. Det akkumulerer i skala, hvor mange teams, der rører ét fælles lager, skaber skjulte afhængigheder og uforudsigelig ydeevne. Aftal, hvor hver slags tilstand hører hjemme, og hvad der ikke hører hjemme i det globale lager. Tag en komponent, der gengives oftere end den bør, med og spor hvorfor. Hvis svaret er et oppustet centralt lager, så beslut grænserne, før koblingen hærder.

4. **Hvad er vores ydeevnebudgetter, fejler de buildet i CI, og måles de på de enheder, vores brugere faktisk har?** Et budget, ingen håndhæver, er et ønske, og et budget målt kun på teamets hurtige bærbare beskriver en bruger, der ikke findes. For en stor organisation er budgetter den ene mekanisme, der holder bundlestørrelse og Core Web Vitals i skak, når dusinvis af teams tilføjer funktioner til en fælles flade, fordi ingen enkelt gennemgår kan fange hver regression med øjet. Det modstridende pres er leveringshastighed: et hårdt buildsvigt over få kilobytes føles obstruktivt, til man prissætter det frafald, det forebygger. Tag jeres nuværende budgetter, realbrugermonitoreringsdata fra lavtydende enheder og langsomme forbindelser og listen over udgivelser, hvor en regression slap igennem, med. I det offentlige, hvor mandatet er at betjene hele befolkningen, herunder folk på gamle telefoner og målte data, så bind budgettet til den langsomste tiendedel af jeres brugere frem for medianen, og gør CI-porten ufravigelig.

5. **Hvilke af vores tjenester skal blive ved med at virke uden klient-JavaScript, og har vi faktisk testet den sti?** Progressiv forbedring er let at påstå og let stille at bryde, fordi den forbedrede sti er den, udviklere bruger hver dag, mens baselinen rådner utestet. At beslutte dette bevidst betyder noget i skala, da mange teams, der leverer til én platform, hver antager, at scripts altid indlæses, medmindre en fælles standard siger andet, og en enkelt hård afhængighed kan bryde kerneopgaven for enhver, hvis bundle fejler. Afvejningen er reel: en fungerende baseline uden JavaScript koster designindsats og begrænser, hvordan I bygger interaktivitet. Tag jeres kritiske brugerrejser, en test der indlæser hver med scripts deaktiveret eller fejlet, og dokumentation for, hvor ofte scripts reelt ikke indlæses i felten, med. For en offentlig tjeneste er en ydelses- eller skatteformular, der kollapser, når ét script får timeout, ikke en forringet oplevelse, det er en borger, der ikke kan opfylde en juridisk forpligtelse, så behandl baselinen som et compliancekrav, ikke en finesse.

6. **Hvornår betaler micro-frontends reelt for deres kompleksitet, og hvem afgør det, før et team rækker ud efter en?** Uafhængige team-udrulninger er attraktive, men micro-frontends bærer kompleksitet fra distribuerede systemer, duplikerede afhængigheder og en ydeevneskat, brugerne betaler i langsommere indlæsninger. Uden et fælles beslutningspunkt adopterer ambitiøse teams dem for organisatorisk bekvemmelighed længe før skalaen retfærdiggør omkostningen, og hele produktet arver overheaden. Det modstridende hensyn er autonomi: teams, der leverer på én fælles kodebase, kan blokere hinanden, og i ægte skala er den kobling sit eget dyre problem. Tag antallet af teams, der rører fladen, den udrulningskonflikt, I faktisk oplever i dag, og et målt estimat af den nyttelastduplikering, en opdeling ville introducere, med. For virksomheds- og offentlige platforme, hvor arkitekturbeslutninger binder mange teams i årevis og skal overleve revision og overdragelse, så kræv en eksplicit, dokumenteret tærskel og en ejer, der godkender skiftet, frem for at lade hvert team beslutte isoleret.

## Sektorperspektiv

**Startup.** Hastighed og rækkevidde betyder begge noget, når hver tilmelding tæller, så modstå den tunge single-page-app til offentlige sider. Server-gengiv jeres marketing- og tilmeldingsflow, så de indlæses hurtigt på de mellemklassetelefoner og den pletvise data, jeres tidlige kunder bruger, og forbehold klientsideinteraktivitet til appen bag login. Sæt ét simpelt bundlestørrelsesbudget i CI, så en skødesløs afhængighed ikke stille kan oppuste siden, og støt jer til webstandarder for at holde en lille kodebase vedligeholdelsesvenlig, efterhånden som I ansætter.

**Lille virksomhed.** Uden en dedikeret frontendspecialist og med et stramt budget så foretræk et velunderstøttet mainstream-framework eller en hostet sitebygger frem for noget skræddersyet, så I ansætter fra en stor talentpulje og køber vedligeholdelse frem for at bemande den. Ram valget ind som holdbarhed: den billigste mulighed er den, I ikke tvinges til at omskrive om to år. Insistér på hurtige, mobilvenlige sider og tilgængelig markup ud af boksen, da en langsom eller ødelagt checkout koster jer kunder, I ikke har råd til at miste.

**Stor virksomhed.** Problemet er ensartethed på tværs af mange teams: et fælles komponentbibliotek, aftalte arkitekturmønstre, linting og byggeværktøj og ydeevnebudgetter håndhævet i CI, så intet team stille kan forringe helheden. Vælg frameworks efter levetid og ansættelse frem for nyhed, isolér frameworkspecifik kode bag grænser for at overleve den næste migrering, og afstem gengivelsesstrategi pr. flade. Styr frontenden som fælles infrastruktur med realbrugermonitorering, styring og en reviderbar optegnelse over, hvorfor hvert arkitekturvalg blev truffet.

**Offentlig sektor.** I betjener hele befolkningen, herunder mennesker på gamle enheder, langsomme eller målte forbindelser og hjælpeteknologier, så progressiv forbedring og ydeevne er forpligtelser, ikke finish. Gør en fungerende baseline uden JavaScript til en hård regel for borgervendte tjenester, budgettér sider til de langsomste brugere frem for medianen, og hold kerneopgaven mulig at gennemføre, når et script fejler. Indkøb og åbenhed gælder: foretræk holdbar, standardsøgende teknologi, der undgår leverandørindlåsning, dokumentér tilgængeligheds- og ydeevnekrav i kontrakter, og vær i stand til at vise, at tjenesten virker for den mindst begunstigede bruger, ikke blot demoenheden.

## Eksempler

**Startup.** Et seed-stadie-startup var fristet til at bygge sit marketingsite og tilmeldingsflow som en tung single-page-app, men deres målkunder var shoppere, ofte på mellemklassetelefoner over pletvis mobildata. De to grundlæggere server-gengav i stedet de offentlige sider, så de indlæstes hurtigt og virkede, før nogen JavaScript kørte, og forbeholdt klientsideinteraktivitet til appen bag login. De satte et simpelt bundlestørrelsesbudget i CI, så en skødesløs afhængighed ikke stille kunne oppuste siden. Den slanke, hurtige første indlæsning forbedrede målbart tilmeldingerne, og at læne sig op ad webstandarder holdt deres lille kodebase let at vedligeholde, efterhånden som de ansatte.

**Stor virksomhed.** En finansiel servicevirksomhed moderniserede en omfattende række interne og kundeapplikationer ved at standardisere på et modent framework, et fælles komponentbibliotek og håndhævede ydeevnebudgetter i CI. Gengivelsesstrategi blev valgt pr. flade: server-gengivne, cachebare sider til offentlig marketing og indhold og en klient-gengivet applikation bag login til interaktive dashboards. Bundlebudgetter og realbrugermonitorering fangede regressioner før udgivelse, holdt indlæsningstider hurtige på tværs af virksomhedens mange teams og reducerede den framework-uro, der tidligere havde tvunget dyre omskrivninger.

**Offentlig sektor.** Et nationalt digitalt serviceteam byggede borgervendte tjenester med progressiv forbedring som en hård regel: hver tjeneste virker med semantisk HTML og server-gengivelse først, og JavaScript forbedrer kun. Det garanterer, at tjenesten fungerer på gamle telefoner, langsomme landlige forbindelser og hjælpeteknologier, populationer en regering ikke kan udelukke. Ydeevnebudgetter holder sider lette og hurtige på lavtydende enheder, og elegant forringelse betyder, at et fejlet script aldrig blokerer nogen i at fuldføre en ydelsesansøgning. Resultatet er en tjeneste, der er hurtig, robust, tilgængelig og brugbar for hele befolkningen.

## Business case: motivation, ROI og TCO

Frontendvalg driver omsætning, rækkevidde og omkostning. Ydeevne er direkte knyttet til konvertering, engagement og opgavegennemførelse. Hurtigere oplevelser overgår målbart langsommere, og for brugere på svage enheder er ydeevne skellet mellem at bruge tjenesten og at opgive den. Progressiv forbedring og understøttelse på tværs af enheder udvider den adresserbare målgruppe, hvilket for det offentlige er et mandat og for virksomheder er markedsandel. Sunde framework- og arkitekturvalg reducerer hyppigheden og omkostningen ved omskrivninger, den største undgåelige udgift i frontendudvikling.

Hvad angår TCO er adoptionsomkostninger disciplinen med ydeevnebudgetter og test, indsatsen ved progressiv forbedring og investeringen i fælles værktøj og komponentbiblioteker. Omkostningen ved ikke at adoptere betales i langsomme oplevelser, der mister brugere og omsætning, udelukkelse af brugere på lavtydende enheder og hjælpeteknologi (med juridisk eksponering i det offentlige), skrøbelige applikationer, der går i stykker i felten, og dyr framework-uro og omskrivninger drevet af at jage trends. Frontendproblemer viser sig som diffust frafald og supportbelastning frem for en enkelt budgetpost, så det er let at underinvestere.

For at føre sagen over for ledelsen så bind Core Web Vitals og indlæsningstider til konverterings- og gennemførelsestragte, kvantificér de brugere, tunge klientsidetilgange udelukker, og prissæt omkostningen ved tidligere eller kommende omskrivninger mod stabiliteten i en holdbar, standardsøgende arkitektur. Ram ydeevnebudgetter og progressiv forbedring ind som risikoreduktion og rækkeviddeudvidelse.

## Anti-mønstre og faldgruber

- **Framework-jagt**: at omskrive på det nyeste bibliotek og pådrage sig uro uden brugergevinst.
- **Kun-JavaScript-oplevelser**: intet virker, før en stor bundle er indlæst og kører, hvilket udelukker mange brugere.
- **Kun test på hurtige enheder**: teamets flagskibsbærbare skjuler den reelle brugeroplevelse.
- **At ignorere bundlestørrelse**: ubegrænset afhængighedsvækst, til sider er langsomme overalt.
- **Intet ydeevnebudget**: regressioner akkumulerer stille udgivelse for udgivelse.
- **Blank-skærm-fejl**: ingen indlæsnings-, tom-, fejl- eller offline-tilstande; en fejlet anmodning bryder siden.
- **Overcentraliseret global tilstand**: alt i ét lager, hvilket skaber kobling og gengivelsesstorme.
- **For tidlige micro-frontends**: kompleksitet fra distribuerede systemer og duplikerede nyttelaster uden skala til at retfærdiggøre dem.
- **At forsømme tilgængelighed og i18n i arkitekturen**: at skrue dem på senere til høj pris.

## Modenhedsmodel

**Niveau 1: Opstart.** Ad hoc frontend bygget pr. team uden fælles standarder. Tung klientsidekode, ingen ydeevnebudgetter, kun testet på teamets egne enheder. Framework-valg truffet efter præference eller hype, og et fejlet script kan efterlade brugere stirrende på en blank skærm.

**Niveau 2: Udvikling.** Nogle teams adopterer fælles værktøj og et komponentbibliotek, men praksis er inkonsistent på tværs af organisationen. Ydeevne måles lejlighedsvis frem for at blive budgetteret eller håndhævet. Gengivelsesstrategi er ofte ensartet uanset indholdstype, og test på tværs af enheder er begrænset og manuel.

**Niveau 3: Standardisering.** Framework og arkitektur vælges bevidst for levetid, og valgene er dokumenteret og håndhævet i hele organisationen. Gengivelsesstrategi afstemmes pr. flade, progressiv forbedring og elegant forringelse er standarden, og fælles komponentbiblioteker, linting og byggeværktøj gælder for hvert team. Tværbrowser-, tilgængeligheds- og internationaliseringsunderstøttelse er bygget ind frem for skruet på.

**Niveau 4: Styring.** Frontenden måles og styres med data. Ydeevnebudgetter håndhæves i CI, så regressioner fejler buildet, og Core Web Vitals følges med realbrugermonitorering fra faktiske lavtydende enheder og langsomme forbindelser mod eksplicitte baselines. Bundlestørrelse, dækning af fejl- og offline-tilstande og andelen af brugere, der betjenes på de langsomste forbindelser, rapporteres og gennemgås, så beslutninger hviler på dokumentation frem for mening.

**Niveau 5: Orkestrering.** Ydeevne, robusthed og rækkevidde forbedres løbende og er knyttet til forretningsudfald i hele organisationen. Frontenden læner sig op ad webstandarder for holdbarhed, isolerer framework-afhængigheder, så migreringer er billige, og udvikler arkitekturen adaptivt, efterhånden som enheder, platformen og realbrugerdata skifter. Hele befolkningen og alle enheder er førsteklasses, og frontendpraksis er integreret med design, tilgængelighed og produktplanlægning frem for behandlet som et separat anliggende.

## Idéer til drøftelse

- Hvordan afgør I, hvornår en framework-migrering er sin omkostning og risiko værd?
- Hvilke Core Web Vitals og bundlebudgetter bør være hårde, buildfejlende tærskler?
- Hvor er progressiv forbedring essentiel, og hvor er en klientsideapp acceptabel?
- Hvordan holder I frontendarkitekturen ensartet på tværs af mange autonome teams?
- Hvornår betaler micro-frontends reelt for deres kompleksitet?
- Hvordan bør test på rigtige enheder og langsomme netværk bygges ind i pipelinen?

## Vigtigste pointer

- Frontenden kører i et miljø, du ikke kontrollerer: design til variation og fejl.
- Vælg holdbar, velunderstøttet teknologi til langlivede systemer; læn dig op ad webstandarder.
- Afstem gengivelsesstrategi (SSR, SSG, CSR, streaming) med indhold og behov, ofte blandet pr. rute.
- Behandl ydeevne som en budgetteret, målt disciplin håndhævet i CI med realbrugerdata.
- Byg med progressiv forbedring, så kerneoplevelsen virker overalt.
- Lever mindre JavaScript; kodedel, lazy-load og foretræk platformsmuligheder.
- Især for det offentlige er ydeevne og robusthed forudsætninger for retfærdig adgang.

## Referencer og videre læsning

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
