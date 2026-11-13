# 5.3 Tilgængelighed

## Overblik og motivation

[Tilgængelighed](https://en.wikipedia.org/wiki/Accessibility) (ofte forkortet "a11y") er praksissen at bygge software, som mennesker med handicap kan opfatte, forstå, navigere i og bruge. Det omfatter mennesker, der er blinde eller svagsynede, døve eller hørehæmmede, har motoriske funktionsnedsættelser, har kognitive eller indlæringsmæssige forskelle, og som møder midlertidige eller situationsbestemte begrænsninger såsom en brækket arm, skarpt sollys eller et støjende rum. Omtrent hver femte person har et handicap, og alle har gavn af tilgængeligt design på et tidspunkt. Det er ikke en nichetilpasning. Det er en basislinje for kvalitet.

For store teams skal tilgængelighed bygges ind i systemet, ikke overlades til individuelle gode intentioner. Når mange teams leverer ind i ét produkt, kan en enkelt utilgængelig komponent (et formularfelt uden label, en statusindikator kun i farve, en tastaturfælde i en modal) låse handicappede brugere ude af en hel rejse. At bygge tilgængelighed ind i fælles komponenter, designtokens, testpipelines og definitioner af færdig er den eneste måde at gøre den pålidelig i skala. At eftermontere den bagefter er dyrt og fejlbehæftet. At designe den ind er billigt og varigt.

For det offentlige er tilgængelighed et juridisk krav og en borgerlig forpligtelse, ikke en bonus. Offentlige tjenester skal betjene hvert medlem af offentligheden, og handicappede borgere har ofte ingen alternativ udbyder: hvis den offentlige hjemmeside er utilgængelig, kan de ikke få deres ydelse, licens eller stemme på anden vis. Love og standarder verden over gør tilgængelighed obligatorisk for offentlige organer og i stigende grad også for den private sektor. Dette kapitel behandler tilgængelighed som tre ting på én gang: en juridisk pligt, en etisk pligt og simpelthen godt design.

*Se også:* kapitel 5.2 (UI-design og designsystemer), kapitel 5.6 (frontendudvikling) og kapitel 5.1 (UX-grundlag).

## Grundprincipper

- Tilgængelighed er en basal kvalitetsegenskab, ligesom sikkerhed og ydeevne, ikke en valgfri funktion.
- POUR-principperne: grænseflader skal være Perceivable (mulige at opfatte), Operable (mulige at betjene), Understandable (forståelige) og Robust (robuste).
- [Semantisk HTML](https://en.wikipedia.org/wiki/Semantic_HTML) først; brug [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) kun til at udfylde ægte huller, aldrig som erstatning for native elementer.
- Alt, der kan bruges med mus, skal kunne bruges kun med tastatur.
- Formidl ikke information alene gennem farve, form eller placering.
- Automatiserede værktøjer fanger kun en brøkdel af problemerne; manuel test og test med [hjælpeteknologi](https://en.wikipedia.org/wiki/Assistive_technology) er essentiel.
- Tilgængeligt design er bedre design for alle (["curb-cut-effekten"](https://en.wikipedia.org/wiki/Curb_cut), hvor funktioner bygget til handicappede gavner alle brugere).
- Design og test med handicappede mennesker, ikke blot for dem.

## Anbefalinger

### Design og byg til WCAG, målrettet den aktuelle standard

[Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) er den internationale reference. WCAG 2.1 og 2.2 er organiseret under de fire POUR-principper med testbare succeskriterier på overensstemmelsesniveauerne A, AA og AAA. Sigt efter niveau AA som jeres basislinje; det er det, de fleste love henviser til. WCAG 2.2 tilføjer kriterier for fokussynlighed, målstørrelse og reduktion af kognitiv belastning. WCAG 3.0 er en kommende efterfølger, struktureret anderledes og stadig under udvikling. Hold øje med den, men byg til 2.2 AA i dag. Behandl retningslinjerne som et gulv, ikke et loft: at bestå hvert kriterium garanterer ikke en reelt brugbar oplevelse.

### Brug semantisk HTML og korrekt ARIA

Native HTML-elementer (knapper, links, formularkontroller, overskrifter, lister, landemærker) kommer med indbygget tilgængelighedssemantik, tastaturadfærd og understøttelse af hjælpeteknologi. Brug dem først. Ræk kun ud efter ARIA (Accessible Rich Internet Applications)-roller, -tilstande og -egenskaber til at beskrive tilpassede widgets, som HTML ikke kan udtrykke, og følg ARIA Authoring Practices. Den første regel for ARIA er enkel: brug ikke ARIA, hvis et native element kan gøre det. Forkert ARIA er værre end ingen: den vildleder aktivt [skærmlæsere](https://en.wikipedia.org/wiki/Screen_reader). Giv siden en logisk overskriftsstruktur, meningsfulde labels, alternativ tekst til billeder, undertekster og transskriptioner til medier og et programmatisk link mellem hver label og dens kontrol.

### Garantér betjening med tastatur og hjælpeteknologi

Hvert interaktivt element skal kunne nås og betjenes alene med tastaturet, i en logisk rækkefølge, med en tydeligt synlig fokusindikator. Undgå tastaturfælder. Styr fokus bevidst, når indhold ændrer sig: flyt fokus til en dialog, når den åbner, returnér det, når dialogen lukker, og annoncér dynamiske opdateringer gennem live regions. Test med rigtig hjælpeteknologi, herunder skærmlæsere på desktop og mobil, skærmforstørrelse, stemmestyring og switch-adgang. Og respektér brugerpræferencer som reduceret bevægelse og øget kontrast.

### Test med automatiserede værktøjer, manuel gennemgang og rigtige brugere

Automatiserede tilgængelighedsscannere er værdifulde, og de bør køre i pipelinen ved hver ændring. Men undersøgelser viser konsekvent, at de kun fanger et mindretal af de reelle problemer, omtrent en tredjedel. Resten kræver menneskelig dømmekraft: tastaturgennemgange, skærmlæsertest, kontrasttjek og spørgsmålet om, hvorvidt indholdet faktisk er forståeligt. Vigtigst af alt, inddrag mennesker med handicap i brugbarhedstest. Byg tilgængelighedsacceptkriterier ind i definitionen af færdig, så problemer fanges pr. historie frem for i en revision før lancering.

### Gør tilgængelighed organisatorisk, ikke heroisk

Bag tilgængelighed ind i designsystemet, så komponenter leveres tilgængelige som standard. Tilbyd træning, så designere, ingeniører, indholdsforfattere og produktchefer hver ved, hvad de har ansvaret for. Etablér en tilgængelighedsstandard, en ejer eller et kompetencecenter og en udbedringsproces. Offentliggør en tilgængelighedserklæring og giv brugere en måde at rapportere barrierer på. Og indkøb tilgængeligt: kræv at leverandører og tredjepartskomponenter overholder kravene og leverer dokumentation (såsom en tilgængelighedsoverensstemmelsesrapport).

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Byg tilgængelighed ind fra start | Billigst, varig, bedre for alle | Kræver træning og disciplin på forhånd |
| Eftermontér / udbedr senere | Udskyder indsats, åbner for en hurtig lancering | Langt dyrere, skrøbelig, juridisk eksponering i mellemtiden |
| Kun automatiseret test | Hurtig, billig, fanger regressioner i CI | Misser ~to tredjedele af problemerne; falsk tryghed |
| Manuel test + test med hjælpeteknologi | Fanger reelle brugbarhedsbarrierer | Langsommere, kræver dygtige testere og enheder |
| Test med handicappede brugere | Grundsandhed om den reelle oplevelse | Rekrutteringsindsats og omkostning, skal gøres respektfuldt |

Den centrale afvejning er disciplin på forhånd versus udskudt omkostning. Tilgængelighed bygget ind er billig og forbedrer kvaliteten for alle; tilgængelighed eftermonteret under juridisk pres er dyr, ufuldstændig og stressende. På lang sigt er der ingen reel afvejning mod "hastighed": utilgængelig software virker simpelthen ikke for en femtedel af jeres brugere. Det er en defekt, ikke en besparelse.

## Spørgsmål til drøftelse med dit team

1. **Fejler tilgængelighedsregressioner vores build, som en ødelagt test gør, og hvis ikke, hvorfor?** Automatiserede scannere fanger kun omkring en tredjedel af problemerne, men dem, de fanger (manglende labels, kontrastfejl, kontroller uden label), er billige at fange i CI og dyre at finde i en revision før lancering. At behandle en regression som et buildsvigt er det, der flytter tilgængelighed fra heroisk individuel indsats til en pålidelig systemegenskab, hvilket er det eneste, der virker, når mange teams leverer ind i ét produkt. Beslut, hvilke tjek der er blokerende, hvilke der er vejledende, og hvem der kan tilsidesætte en fejl. Tag jeres nuværende scannerresultater og jeres definition af færdig med til mødet. Hvis tilgængelighedskriterier ikke er skrevet ind i definitionen af færdig pr. historie, bliver de nedprioriteret i det øjeblik, en deadline strammes.

2. **Hvad er vores regel for tilpassede widgets, og hvem gennemgår ARIA'en, før den leveres?** Native HTML-elementer kommer med tastaturadfærd og understøttelse af hjælpeteknologi gratis, og forkert ARIA er værre end ingen, fordi den aktivt vildleder skærmlæsere. Aftal, at semantisk HTML er standarden, og at enhver tilpasset widget (en skræddersyet dropdown, datovælger eller modal) kræver en tastatur- og skærmlæsergennemgang før merge, efter ARIA Authoring Practices. Det betyder mest for de interaktive komponenter, mange teams genbruger, fordi én ødelagt modal med en tastaturfælde kan låse handicappede brugere ude af en hel rejse. Tag en liste over jeres tilpassede widgets med og spørg, hvilke der er testet med en faktisk skærmlæser. Dem, der ikke er, er ansvar, der gemmer sig i delt kode.

3. **Hvad er vores politik over for tilgængelighedsoverlays, og tror nogen på, at de er en reel løsning?** Overlays markedsføres som et script på én linje, der gør et websted overensstemmende, og de er fristende, når juridisk pres ankommer, og en deadline nærmer sig. De leverer ikke ægte overensstemmelse, de kan forværre oplevelsen for brugere af hjælpeteknologi, og for det offentlige efterlader de den underliggende juridiske pligt uopfyldt. Beslut eksplicit, at I vil investere i semantisk markup, tastaturunderstøttelse og test med handicappede mennesker frem for at købe en widget, der dækker over problemet. Tag omkostningen ved et overlayabonnement med og sammenlign den med at bygge tilgængelighed ind i jeres komponenter og pipeline én gang. At ramme dette ind tidligt forebygger en panisk indkøbsbeslutning senere, der bruger penge og ordner intet.

4. **Er handicappede mennesker en del af vores design og test, eller designer vi stadig for en indbildt bruger, vi selv har opfundet?** Automatiserede scannere og selv ekspertrevisioner fortæller jer, om markup er overensstemmende; de fortæller jer ikke, om en blind bruger faktisk kan gennemføre jeres checkout, eller om en person med en kognitiv funktionsnedsættelse kan forstå jeres fejlmeddelelser. At inddrage handicappede deltagere er den eneste kilde til grundsandhed, og det ændrer, hvad I bygger, men det rejser reelle spørgsmål om, hvordan I rekrutterer retfærdigt, hvordan I kompenserer folk for deres tid, og hvordan I undgår at behandle én deltager som talsmand for hvert handicap. Tag jeres nuværende researchpanel, jeres rekrutterings- og betalingspraksis og en ærlig optælling af, hvor mange undersøgelser det seneste år der inkluderede handicappede deltagere, med. For en stor organisation er et tilbagevendende panel med fair kompensation og dækning på tværs af syn, hørelse, motorik og kognitive behov det, der forvandler dette fra en engangsgestus til et pålideligt input; i det offentlige er det at inddrage den offentlighed, I betjener, ofte en del af den juridiske og borgerlige forpligtelse, ikke en valgfri finesse.

5. **Når vi køber eller indlejrer en tredjepartskomponent, kræver vi så dokumentation for tilgængelighed, og hvem tjekker den?** Meget af det, der leveres i et stort produkt, er ikke skrevet internt: en datovælger fra et bibliotek, en betalingswidget i en iframe, en diagrampakke, et helt SaaS-modul. En enkelt utilgængelig indlejret komponent kan fejle en hel rejse, uanset hvor ren jeres egen kode er, og når den først er koblet ind, er det dyrt at erstatte den. Beslut, at tilgængelighed er et indkøbskrav, at leverandører skal levere en tilgængelighedsoverensstemmelsesrapport (et dokument såsom en VPAT, der angiver, hvordan et produkt måler sig mod WCAG), og at nogen teknisk validerer påstanden frem for at arkivere den. Tag en opgørelse over jeres tredjepartskomponenter med og spørg, hvilke der har aktuel, troværdig dokumentation for overensstemmelse. I virksomheds- og offentlige indkøb så skriv WCAG 2.2 AA-overensstemmelse og en ret til udbedring ind i kontrakten, for et løfte givet før underskrift er langt billigere at håndhæve end en barriere opdaget efter go-live.

6. **Hvad er vores mål for overensstemmelsesniveau, hvem ejer det, og hvordan holder vi det aktuelt, efterhånden som standarder flytter sig?** WCAG 2.2 AA er dagens gulv, og de fleste love henviser til det, men 2.2 tilføjede kriterier, mange teams ikke har adopteret, og WCAG 3.0 er på vej med en anden struktur. Uden en navngiven ejer driver standarden: forskellige teams sigter mod forskellige versioner, ingen følger hullet, og overensstemmelse rådner stille mellem revisioner. Beslut den præcise version og det niveau, I bygger til, hvem der har autoritet til at hæve det, og hvordan nye kriterier når designsystemet og definitionen af færdig. Tag jeres nuværende angivne mål, dokumentation for, hvor teams faktisk opfylder det, og en kort køreplan for at adoptere de 2.2-kriterier, I har sprunget over, med. For en stor eller offentlig organisation er en tilgængelighedsejer eller et kompetencecenter, en offentliggjort tilgængelighedserklæring og en dokumenteret plan for den næste standardversion det, der lader jer besvare en tilsynsmyndighed eller en domstol med dokumentation frem for gode intentioner.

## Sektorperspektiv

**Startup.** Hastighed favoriserer jer her, fordi tilgængelighed er billigst, når kodebasen er lille. Tilføj en automatiseret scanner til CI og en tastaturgennemgang til jeres pull request-tjekliste fra første sprint, og støt jer til semantisk HTML, så I får tastatur- og skærmlæserunderstøttelse gratis. Spring overlays og tungt værktøj over; gevinsten er, at når en kundes indkøbsteam beder om en overensstemmelsesrapport midt i et salg, kan I svare på dage i stedet for at skynde jer.

**Lille virksomhed.** Uden en tilgængelighedsspecialist og med et stramt budget så køb tilgængelighed frem for at bygge den: vælg en platform, et tema eller et komponentbibliotek, der allerede overholder kravene og siger det, og foretræk leverandører, der offentliggør en tilgængelighedserklæring. Dæk de grundlæggende ting med høj værdi selv med gratis værktøj, tastatur-kun-tjek, en kontrastkontrol og klare labels på hvert felt, fordi de fanger de fejl, der oftest udelukker kunder. Behandl et forkert eller ubrugeligt automatiseret flow som en tabt kunde, da en lille virksomhed sjældent tilbyder en assisteret kanal at falde tilbage på.

**Stor virksomhed.** I skala er arbejdet at gøre tilgængelighed til en systemegenskab på tværs af mange teams. Lever tilgængelige komponenter som standard i designsystemet, luk porten for regressioner i CI, og opstil en ejer eller et kompetencecenter med en udbedringsproces og træning for designere, ingeniører og indholdsforfattere. Følg overensstemmelse over tid som en måling, skriv WCAG-overensstemmelse ind i indkøb, og styr tredjepartskomponenter som en portefølje, så én indlejret widget ikke stille kan fejle en fælles rejse.

**Offentlig sektor.** Tilgængelighed er et juridisk påbud og en borgerlig pligt, da handicappede borgere ofte ikke har nogen alternativ udbyder til en ydelse, licens eller stemme. Byg til den standard, jeres jurisdiktion henviser til (for eksempel Section 508, EN 301 549 eller European Accessibility Act afbildet til WCAG 2.2 AA), offentliggør en tilgængelighedserklæring med en vej til at rapportere barrierer, og test med den handicappede offentlighed, I betjener. Afvis overlays som erstatning for reel overensstemmelse, og kræv at leverandører leverer troværdig dokumentation og en ret til udbedring i kontrakten.

## Eksempler

**Startup.** Et startup på tre personer, der byggede et rekrutteringsværktøj, tilføjede en tilgængelighedsscanner til deres build og en hurtig tastaturgennemgang til deres pull request-tjekliste fra allerførste sprint og ræsonnerede, at det var billigere at forblive tilgængelig end at rette det senere. Da en mellemstor kundes indkøbsteam bad om en tilgængelighedsoverensstemmelsesrapport under en salgscyklus, brugte startuppet allerede semantisk HTML, havde label på hvert felt og synligt fokus overalt, så de svarede på dage i stedet for at skynde sig. Den parathed vandt en aftale, som en konkurrent tabte på det samme krav.

**Stor virksomhed.** En stor detailhandler stod over for et gruppesøgsmål, fordi blinde kunder ikke kunne gennemføre checkout med en skærmlæser. Ud over forliget og sagsomkostningerne måtte virksomheden udbedre under en domstolsovervåget tidslinje. Bagefter byggede den tilgængelighed ind i sit designsystem og sin CI-pipeline igen, tilføjede skærmlæsertest til definitionen af færdig og uddannede sine teams. Den ombyggede, tilgængelige checkout forbedrede også konverteringen og reducerede supportkontakter for alle: de rettelser, der hjalp skærmlæserbrugere (klare labels, fejlmeddelelser, logisk rækkefølge), hjalp alle brugere.

**Offentlig sektor.** Et offentligt ydelsesagentur var juridisk forpligtet til at opfylde WCAG 2.1 AA for sin onlineansøgning. Tidlig test med blinde og svagsynede brugere, tastatur-kun-brugere og brugere med kognitive handicap afslørede, at en farve-kun-indikator for "obligatorisk felt", en utilgængelig datovælger og uannoncerede valideringsfejl forhindrede folk i at gennemføre. At rette disse gennem semantisk markup, synligt fokus, live region-annonceringer af fejl og hjælp i [almindeligt sprog](https://en.wikipedia.org/wiki/Plain_language) lod handicappede borgere ansøge på egen hånd for første gang. Det reducerede afhængigheden af hjælp i person og sænkede omkostningen ved at betjene, mens det juridiske påbud blev opfyldt.

## Business case: motivation, ROI og TCO

Business casen hviler på markedsrækkevidde, juridisk risiko, omkostning ved at betjene og kvalitet. Handicappede og deres familier kontrollerer betydelig købekraft; at udelukke dem opgiver den. Tilgængelige tjenester reducerer behovet for dyre assisterede kanaler (telefon- og personlig hjælp), hvilket er en direkte driftsbesparelse, især for det offentlige. Og fordi tilgængelighedsforbedringer (klare labels, tastaturunderstøttelse, læseligt indhold, robust markup) hjælper alle, hæver de typisk den samlede gennemførelse og tilfredshed.

Hvad angår TCO er adoptionsomkostningen træning, værktøj og at bygge tilgængelighed ind i komponenter og pipelines, alt sammen beskedent, når I gør det fra starten. Omkostningen ved ikke at adoptere er alvorlig og kommer fra flere retninger: juridisk ansvar (søgsmål, forlig, domstolspåbudt udbedring, regulatoriske sanktioner), den langt højere udgift ved at eftermontere under deadlinepres, omdømmeskade og den løbende omkostning ved at betjene udelukkede brugere gennem dyrere kanaler. Eftermontering koster typisk flere gange, hvad at designe ind ville have gjort.

For at føre sagen over for ledelsen så led med den juridiske forpligtelse, hvor den gælder (den er ikke til forhandling for det offentlige og i stigende grad for den private sektor). Kvantificér derefter den adresserbare population, I udelukker, den assisterede kanalomkostning ved den udelukkelse og "curb-cut"-gevinsterne for alle brugere. Placér tilgængelighed som risikostyring plus kvalitet, ikke velgørenhed.

## Anti-mønstre og faldgruber

- **Tilgængelighed som et afkrydsningsfelt før lancering**: en revision til sidst i stedet for kontinuerlig praksis, hvilket garanterer dyrt omarbejde i sidste øjeblik.
- **"Div-suppe"**: ikke-semantisk markup med klikhåndterere på generiske elementer, usynlig for hjælpeteknologi.
- **ARIA-misbrug**: at skrue ARIA på ødelagt markup, hvilket vildleder skærmlæsere mere, end ren markup ville.
- **Information kun i farve**: status vist alene ved farve, usynlig for farveblinde brugere.
- **Usynligt fokus**: at fjerne fokusmarkeringer af æstetiske grunde og efterlade tastaturbrugere strandet.
- **Tastaturfælder**: modaler og widgets, der fanger eller mister fokus.
- **Selvtilfredshed efter automatiseret scanning**: at bestå en scanner og antage, at produktet er tilgængeligt.
- **Tilgængelighedsoverlays**: tredjeparts "rettelse på én linje"-widgets, der ikke leverer reel overensstemmelse og kan forværre oplevelsen.
- **At udelukke handicappede brugere fra research**: at designe for en indbildt handicappet bruger i stedet for at teste med rigtige.

## Modenhedsmodel

**Niveau 1: Opstart.** Ingen tilgængelighedspraksis. Problemer opdages først, når en bruger klager, eller et søgsmål ankommer, og responsen er reaktiv. Markup er ikke-semantisk og utestet, og ingen ejer problemet.

**Niveau 2: Udvikling.** Bevidsthed findes, og nogle teams handler på den: en automatiseret scanner i et build her, en tastaturgennemgang der, en revision før lancering inden en stor udgivelse. Praksis er grundlæggende og inkonsistent på tværs af teams, tilgængelighed er stadig en tjekliste sent i forløbet, og den nedprioriteres ofte under tidspres.

**Niveau 3: Standardisering.** WCAG 2.2 AA er den dokumenterede standard, håndhævet i hele organisationen. Tilgængelighed er bygget ind i designsystemet, så komponenter leveres tilgængelige som standard, testet automatisk og manuelt og skrevet ind i definitionen af færdig. Teams er uddannet, en ejer eller et kompetencecenter findes, og en udbedringsproces er defineret.

**Niveau 4: Styring.** Tilgængelighed måles og styres med data mod baselines. Organisationen følger overensstemmelsesmålinger over tid (scannerbeståelsesrater, antallet af åbne barrierer efter alvorlighed, skærmlæsertestdækning af kritiske rejser og tid til udbedring), rapporterer dem pr. team på et dashboard og behandler regressioner som buildsvigt frem for vejledende advarsler. Mål sættes mod en baseline, og fremskridt gennemgås, så et team, der skrider, er synligt, før en revision finder det.

**Niveau 5: Orkestrering.** Tilgængelighed forbedres løbende og er integreret på tværs af organisationen. Handicappede mennesker er en del af research og test på tilbagevendende basis, og tilgængelighed er indlejret i indkøb, designtokens og CI. Organisationen tilpasser sig, efterhånden som standarder flytter sig (adopterer nye WCAG-kriterier og forbereder sig på WCAG 3.0), og den påvirker leverandører og partnere, så hele forsyningskæden overholder kravene.

## Idéer til drøftelse

- Hvordan forhindrer I, at tilgængelighed bliver nedprioriteret, når deadlines strammes?
- Hvad er den rette blanding af automatiseret test, manuel test og brugertest for jeres risikoprofil?
- Hvordan bør tilgængelighedsoverensstemmelse skrives ind i leverandørkontrakter og indkøb?
- Hvordan håndterer I hullet mellem WCAG-overensstemmelse og ægte brugbarhed for handicappede?
- Hvordan bør teams forberede sig på WCAG 3.0, mens de bygger til 2.2 i dag?
- Hvordan rekrutterer og kompenserer I retfærdigt og respektfuldt handicappede deltagere til research?

## Vigtigste pointer

- Tilgængelighed er en basal kvalitetsegenskab og, for det offentlige, et juridisk krav.
- Design til WCAG 2.2 AA som et gulv; brug POUR-principperne som en mental model.
- Semantisk HTML først; ARIA kun til at udfylde reelle huller, gjort korrekt.
- Automatiserede værktøjer fanger omkring en tredjedel af problemerne; manuel test og test med hjælpeteknologi er essentiel.
- Test med handicappede mennesker, ikke blot for dem.
- At bygge tilgængelighed ind er billigt og varigt; eftermontering er dyr og skrøbelig.
- Tilgængeligt design er bedre design for alle: curb-cut-effekten er reel.

## Referencer og videre læsning

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
