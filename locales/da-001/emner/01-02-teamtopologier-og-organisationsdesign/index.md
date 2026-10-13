# 1.2 Teamtopologier og organisationsdesign

## Overblik og motivation

Hvordan du deler mennesker op i teams, afgør, hvilken software du kan bygge, og hvor hurtigt du kan bygge den. Det er ikke en metafor. Det er en næsten mekanisk konsekvens kendt som [Conways lov](https://en.wikipedia.org/wiki/Conway%27s_law): organisationer designer systemer, der spejler deres egne kommunikationsstrukturer. Hvis tre teams bygger en [compiler](https://en.wikipedia.org/wiki/Compiler), får du en compiler med tre gennemløb. Hvis din betalingslogik er delt mellem et frontendteam, et backendteam og et databaseteam, kræver hver ændring af betalinger koordinering mellem tre parter. I en lille organisation kan det håndteres. I en stor bliver organisationsdiagrammets form den dominerende begrænsning for din teknik, din arkitektur, din leveringshastighed og din kvalitet. Derfor er design af teamstruktur en førsteklasses ingeniøropgave, ikke en HR-eftertanke.

Teamtopologier giver dig et bevidst ordforråd til dette design. I stedet for at lade strukturen vokse tilfældigt gennem omorganiseringer og headcount vælger modne organisationer teamtyper og samspilsformer med vilje og tager dem op til revision, efterhånden som systemet og forretningen udvikler sig. Målet er at holde hvert teams [kognitive belastning](https://en.wikipedia.org/wiki/Cognitive_load) lav, altså den samlede mængde et team skal holde i hovedet for at være effektivt, så teams kan eje deres domæne fra ende til anden og levere en jævn strøm af værdi uden konstant at vente på andre.

For virksomheder og offentlige organisationer er denne disciplin afgørende. Store organisationer breder sig naturligt ud i dybe hierarkier, delte tjenester med lange køer og overdragelseskæder, der gør en ændring på to dage til et projekt på to måneder. Den offentlige sektor tilføjer udbudsgrænser, konsulentteams og påbudte [funktionsadskillelser](https://en.wikipedia.org/wiki/Separation_of_duties), der fragmenterer ejerskabet yderligere. Eksplicit topologidesign er, hvordan disse organisationer vinder flowet tilbage: tilpas teams til værdistrømme, byg platforme, der mindsker kognitiv belastning, og vælg samspilsmønstre, der gør afhængigheder synlige og tilsigtede frem for skjulte og konstante.

## Grundprincipper

- Conways lov er uundgåelig; design teams, så de svarer til den softwareudvikling, du ønsker (den "omvendte manøvre").
- Optimér for teamets kognitive belastning, ikke for størst mulig udnyttelse af enkeltpersoner.
- Foretræk stream-aligned teams, der ejer en skive af værdien fra ende til anden.
- Platforme findes for at mindske stream-aligned teams' kognitive belastning, ikke for at stå som portvagter.
- Gør teamsamspil eksplicit og få: samarbejde, X-as-a-service eller facilitering.
- Minimér afhængigheder; hver overdragelse på tværs af teams er en kø og en risiko.
- Teamstruktur er et levende design, der må udvikle sig, når systemet og forretningen ændrer sig.

## Anbefalinger

### Brug de fire grundlæggende teamtyper

Teamtopologier definerer fire teamtyper, der dækker de fleste behov. Stream-aligned teams er standarden: hvert ejer et kontinuerligt arbejdsflow for et bestemt produkt, en tjeneste eller en brugerrejse fra ende til anden. Platformsteams leverer interne produkter (compute, udrulning, datapipelines, identitet), som stream-aligned teams bruger som selvbetjening, hvilket mindsker deres kognitive belastning. Enabling teams er specialister (test, sikkerhed, observerbarhed), der coacher stream-aligned teams til at opbygge en kapabilitet og derefter trækker sig. Complicated-subsystem-teams ejer komponenter, der kræver dyb specialistviden (en prisberegningsmotor, en [videocodec](https://en.wikipedia.org/wiki/Video_codec), et kryptografisk modul), hvor det ikke giver mening, at hvert team besidder den viden. De fleste af dine teams bør være stream-aligned; de tre andre typer findes for at støtte dem.

### Anvend den omvendte Conway-manøvre

Da software spejler din organisations struktur, så form dine teams, så de frembringer den software, du ønsker. Vil du have løst koblede tjenester med klare grænser? Opret løst koblede teams med klare ejerskabsgrænser. Vil du have en betalingskapabilitet, der udkommer på sit eget tidsskema? Dan et betalingsteam, der ejer den fra front til bund. Bekæmp ikke Conways lov med heroisk koordinering. Tegn teamgrænserne om, så den arkitektur, du ønsker, bliver den lette vej.

### Styr kognitiv belastning eksplicit

Et team kan kun mestre så meget. Kognitiv belastning omfatter domænets kompleksitet, teknologierne, driftsbyrden og bredden af interessenter. Når et team ejer for mange indbyrdes urelaterede tjenester, kollapser både kvalitet og hastighed. Afgræns derfor hvert teams ansvar til et domæne, det reelt kan mestre, og brug platforme og enabling teams til at tage udifferentieret kompleksitet af dets tallerken. Hold teams på cirka fem til ni personer: små nok til at kommunikere let og, så at sige, til at blive mættet af et par pizzaer.

### Vælg samspilsformer bevidst

Begræns teamsamspil til tre former. Samarbejde er tæt arbejde med høj båndbredde mellem to teams i en afgrænset periode; det er stærkt til opdagelse, men dyrt, så hold det midlertidigt. X-as-a-service er et rent leverandør/forbruger-forhold med en veldefineret grænseflade, ideelt til platformsforbrug i stor skala. Facilitering er, at ét team hjælper et andet med at lære, hvilket er det, enabling teams gør. Navngiv formen for hvert vigtigt forhold på tværs af teams, og læs langvarigt samarbejde mellem de samme to teams som et tegn på, at deres grænse ligger det forkerte sted.

### Vælg en driftsmodel for tværgående funktioner

Sikkerhed, data, design og lignende discipliner kan organiseres på tre måder: centraliseret (ét team ejer det for alle), føderet (specialister indlejret på deltid og koordineret gennem et guild) eller indlejret (en dedikeret specialist i hvert stream-aligned team). Centraliseret giver dig ensartethed og dybde, men bliver en flaskehals. Indlejret giver hastighed og kontekst, men risikerer inkonsistens og dobbeltarbejde. Føderet (ofte en hub-and-spoke- eller [praksisfællesskab](https://en.wikipedia.org/wiki/Community_of_practice)-model) ligger midt imellem. Vælg pr. funktion og pr. skala. De fleste store organisationer ender på føderet for disse discipliner, med en lille central kerne, der fastsætter standarder.

### Invester i inner-source

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) bringer samarbejdsmønstrene fra [open source](https://en.wikipedia.org/wiki/Open-source_software) ind i organisationen: delte interne repositories, offentliggjorte retningslinjer for bidrag, [kodegennemgang](https://en.wikipedia.org/wiki/Code_review) på tværs af teamgrænser og klare maintainere. Når et team har brug for en ændring i et andet teams komponent, kan det selv bidrage med ændringen i stedet for at oprette en sag og vente i kø. Det letter afhængigheder på tværs af teams uden at opløse ejerskab, og det spreder viden og standarder naturligt over en stor ingeniørbestand.

## Afvejninger: fordele og ulemper

| Model for tværgående funktioner | Fordele | Ulemper |
| --- | --- | --- |
| Centraliseret (ét team for alle) | Ensartethed, dyb ekspertise, klare standarder | Flaskehals, køer, tab af produktkontekst |
| Føderet (hub-and-spoke, guilds) | Balancerer ensartethed og hastighed; deler viden | Kræver koordinationsdisciplin; ansvar kan blive udvisket |
| Indlejret (specialist pr. team) | Hurtig, kontekstrig, stærkt ejerskab | Dobbeltarbejde, inkonsistens, svær at bemande i stor skala |

| Teamtype | Bedst til | Risiko hvis overbrugt |
| --- | --- | --- |
| Stream-aligned | Det meste produkt- og servicelevering | Ingen; det bør dominere |
| Platform | Mindske fælles kognitiv belastning | Bliver en portvagt i elfenbenstårnet |
| Enabling | Midlertidig spredning af en kapabilitet | Bliver en permanent afhængighed |
| Complicated-subsystem | Reelt dybe specialistdomæner | Bruges som undskyldning for at hamstre almindeligt arbejde |

Den tilbagevendende afvejning er autonomi versus ensartethed. Fuldt autonome teams bevæger sig hurtigt, men de driver fra hinanden i standarder, værktøjer og sikkerhedsholdning. Fuldt centraliseret kontrol holder tingene ensartede, men kvæler flowet. Godt topologidesign finder sømmen: autonomi til stream-aligned levering plus tynde centrale standarder og paved-road-platforme (velunderstøttede standardværktøjer, der gør det regelrette valg til det lette) til de ting, der reelt må være ensartede.

## Spørgsmål til drøftelse med dit team

1. **Hvilke konkrete signaler vil fortælle dig, at et teams kognitive belastning er for høj, før kvaliteten kollapser?** "Afgræns hvert team til et domæne, det kan mestre" er let at sige og svært at handle på uden dokumentation, fordi kognitiv belastning er usynlig, indtil levering og pålidelighed forringes. Hold øje med målbare symptomer: antallet af urelaterede tjenester eller repositories, et team ejer, hvor lang tid onboarding tager, hvor mange domæner en enkelt ingeniør skal skifte kontekst mellem på en uge, og stigende hændelsesrater i hjørnerne af et teams ansvarsområde. For en stor organisation betyder det noget, fordi overbelastede teams stille bliver flaskehalse, som intet omorganiseringsdiagram forudsiger. Tag tallene med til drøftelsen, plus teamets egen fornemmelse af, hvad de kan og ikke kan holde i hovedet. Hvis signalerne siger overbelastet, er svaret at aflaste udifferentieret arbejde til en platform eller et enabling team, ikke at forlange mere heltemod.

2. **Er en omorganisering reelt værd at forstyrrelsen her, eller fodrer du en omorganiseringsafhængighed?** At tegne grænser om for at anvende den omvendte Conway-manøvre er stærkt, og hver omorganisering ødelægger også den stabilitet, teams har brug for for at falde til, og nulstiller hårdt tjent domæneviden. De modstridende hensyn er den løbende koordinationsafgift ved den nuværende struktur versus engangsomkostningen og moralstødet ved at ændre den. I virksomheder og offentlige organer gør udbudsgrænser, konsulentteams og påbudte funktionsadskillelser omorganiseringer langsommere og dyrere, så barren bør ligge højere. Tag dokumentation for afhængighedsdrevet forsinkelse med: hvor mange initiativer er blokeret af ventetid på et andet team, og hvor længe. Omorganisér, når ventetiden er strukturel og stor, og modstå omrokeringer, når smerten er midlertidig eller ville være billigere at løse med inner-source-bidrag og klarere grænseflader.

3. **For sikkerhed, data og design: hvilken begivenhed får dig til at skifte mellem indlejret, føderet og centraliseret?** Kapitlets anbefaling er at vælge pr. funktion og pr. skala, og den sværere disciplin er at bestemme på forhånd, hvilken vækst eller risiko der får dig til at genoverveje valget. En model, der passer til halvtreds ingeniører, kan blive en flaskehals eller en ensartethedskatastrofe ved femhundrede, og især virksomheder og offentlige organer må navngive de standarder, en lille central kerne altid vil holde. Tag de nuværende ventetider og ensartethedshuller for hver funktion med: et centralt sikkerhedsteam med ugelange gennemgangskøer er et signal om at føderere, mens indlejrede specialister, der producerer uforenelige datamodeller, er et signal om at tilføje en central standardkerne. Beslut udløseren nu, for eksempel en køgrænse eller et revisionsfund, så ændringen bliver en planlagt udvikling frem for en krisereaktion. Svaret afgør, hvor du investerer i paved roads og ambassadører versus en central hub.

4. **Hvordan vil du vide, om dit platformsteam reelt mindsker kognitiv belastning eller stille bliver en portvagt?** En platform findes for at gøre det regelrette, pålidelige valg til det lette via selvbetjening, og det samme team kan glide over i at påbyde værktøjer, håndgennemgå hver anmodning og tilføje den gnidning, det skulle fjerne. For en stor organisation afgør denne forskel, om platformsinvesteringen betaler sig eller bliver en central flaskehals, som alle stream-aligned teams står i kø bag. De modstridende hensyn er ensartethed og kontrol på den ene side mod forbrugerens autonomi og flow på den anden. Tag dokumentation med, som en forbruger ville genkende: hvor lang tid det tager et stream-aligned team at selvbetjene et nyt miljø eller en ny pipeline uden at oprette en sag, forholdet mellem selvbetjeningshandlinger og menneskeformidlede, og platformsbrug målt som teams, der vælger den, frem for teams, der er tvunget på den. I virksomheder og offentlige organer bør du insistere på, at platformen genererer revisions- og compliancebeviser automatisk frem for gennem manuelle porte, for en platform, der opfylder regler om funktionsadskillelse ved at indsætte en menneskelig gennemgang, har genskabt den flaskehals, den blev finansieret til at opløse.

5. **Hvilke af dine forhold på tværs af teams har sat sig som permanent samarbejde, og hvad ville konvertere hvert af dem til en ren servicegrænseflade eller en omtegnet grænse?** Samarbejdsformen er tænkt som intens og midlertidig, og en makkerskabsrelation, der aldrig slutter, er som regel et tegn på, at ejerskabet ligger det forkerte sted, eller at grænsefladen mellem to teams aldrig blev gjort eksplicit. Det betyder noget i stor skala, fordi unavngivet, vedvarende samarbejde er der, hvor koordinationsomkostninger gemmer sig: det optræder ikke på noget organisationsdiagram, men beskatter hver ændring, de to teams rører ved. De modstridende hensyn er opdagelsesværdien ved at blive tæt på versus det flow, du vinder ved at gøre forholdet til en X-as-a-service-kontrakt med en defineret grænseflade, eller ved at flette ansvaret ind i ét team. Tag listen over teampar, der har samarbejdet kontinuerligt i mere end et kvartal, de ændringer, der de seneste måneder krævede begge teams, og om en stabil grænseflade mellem dem kunne skrives ned. I virksomheds- og offentlige sammenhænge, hvor konsulentgrænser og udbudsdele kan fryse en overdragelse i årevis, så navngiv, hvilke forhold du kan konvertere med en grænseflade og inner-source-bidrag, og hvilke der er kontraktligt faste og må styres som eksplicitte afhængigheder.

6. **Når et enabling team hjælper et andet team med at opbygge en kapabilitet, hvordan vil du vide, at det er lykkedes, og at det kan trække sig i stedet for at blive en permanent afhængighed?** Enabling teams er tænkt til at coache et stream-aligned team til at mestre test, sikkerhed eller observerbarhed og derefter gå videre, og uden en eksplicit afslutningsbetingelse hærder coachingforholdet til en stående tjeneste, som det stream-aligned team aldrig reelt optager. For en stor organisation er det forskellen mellem at sprede en kapabilitet over snesevis af teams og at skabe en ny fælles flaskehals, der skalerer dårligere hvert år. De modstridende hensyn er den dybde og ensartethed, et specialistteam giver, mod den autonomi og det ende-til-ende-ejerskab, du forsøger at bygge ind i stream-aligned teams. Tag dokumentation for kapabilitetsoverførsel med: om modtagerteamet nu klarer arbejdet uden enabling teamet til stede, hvor mange teams en fast enabling gruppe er forpligtet til ad gangen, og hvor længe hvert forløb har kørt ud over den tilsigtede overdragelse. I virksomheder og offentlige organer, hvor en knap specialistkompetence kan sidde bag ét centralt team eller én kontrakt, så beslut på forhånd, hvordan du finansierer kapabilitetsoverførsel og ambassadører, så ekspertise diffunderer ind i leveringsteams i stedet for at forblive låst bag en kø, som alle revisioner og udgivelser må vente på.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og lidt runway er den rette topologi ét stream-aligned team, der ejer hele produktet, og disciplinen er at nægte at skabe siloer, før du har brug for dem. Modstå at ansætte en enlig "DevOps"- eller "QA"-person, der bliver en port; fold disse kompetencer ind i det ene team som en indlejret kapabilitet. Lad Conways lov arbejde for dig ved at holde organisationen flad, så arkitekturen forbliver lige så enkel og foranderlig som teamet.

**Lille virksomhed.** Du vil ikke bemande et dedikeret platforms- eller enabling team, så køb platformen: brug administrerede cloudtjenester, hostede pipelines og færdige sikkerhedsværktøjer til at tage udifferentieret kognitiv belastning af dit ene eller to teams. Betragt tværgående emner som sikkerhed og data som ting, du konfigurerer og bruger, frem for en funktion du bygger. Forbehold eventuelt skræddersyet ejerskab til det ene komplicerede delsystem, der reelt differentierer dig, og lad leverandører bære resten.

**Stor virksomhed.** I stor skala er problemet koordinationsomkostninger på tværs af mange teams, så gør topologi til et eksplicit, styret design: en fælles taksonomi over de fire teamtyper, navngivne samspilsformer, en paved-road-platform og inner-source til at aflaste køer på tværs af teams. Følg afhængighedsdrevet forsinkelse og teams' kognitive belastning som porteføljemål, og kør omorganiseringer som bevidste udviklinger med en høj barre frem for en årlig refleks. En tynd central kerne holder de standarder, der skal være ensartede, mens stream-aligned teams beholder autonomi over leveringen.

**Offentlig sektor.** Indkøbsregler, konsulentgrænser og påbudte funktionsadskillelser fragmenterer ejerskab, så design topologien til at opfylde disse begrænsninger gennem værktøjer og klare grænseflader frem for menneskelige overdragelser. Foretræk føderede modeller med en lille standardkerne og en platform, der genererer revisions- og compliancebeviser automatisk, så funktionsadskillelse håndhæves af pipelines frem for gennemgangskøer. Dokumentér teamgrænser, samspilsformer og driftsmodellen åbent, så strukturen er gennemsigtig for revisorer, tilsynsorganer og den offentlighed, der finansierer den.

## Eksempler

**Startup.** Et startup med ti medarbejdere har ét stream-aligned team, der ejer hele produktet fra ende til anden, hvilket er helt rigtigt i den skala: ingen overdragelser, ingen koordinationsafgift, alle deler samme kontekst. Problemerne begynder, da de ansætter en dedikeret "DevOps-person" og en separat "QA-person" og ved et uheld genskaber funktionelle siloer, så hver udgivelse nu venter på to personer. De retter kursen ved at behandle de ansættelser som en indlejret platforms- og testkapabilitet inde i det ene team frem for porte, arbejdet skal igennem. I denne størrelse er den billigste topologi den, der holder alle i ét flow.

**Stor virksomhed.** En stor detailkædes checkout var langsom at ændre, fordi frontend-, backend- og opfyldelseslogik var spredt over tre funktionelt organiserede teams, hvilket tvang hver ændring gennem tre backlogs. Ved at anvende den omvendte Conway-manøvre omorganiserede de i stream-aligned teams omkring kunderejser ("browse", "kurv og checkout", "efter køb"), hvert med ejerskab over sin skive fra front til bund, bakket op af et platformsteam, der leverede udrulning og observerbarhed som en tjeneste. Checkout-ændringer, der før tog et kvartal, begyndte at udkomme på dage, fordi den koordinering, der før spændte over teams, nu skete inden for ét.

**Offentlig sektor.** En offentlig skattemyndighed kørte et centralt sikkerhedsteam, der gennemgik hver udgivelse, hvilket skabte en kø på flere uger, der forsinkede kritiske rettelser. De skiftede til en føderet model: en lille central sikkerhedsfunktion fastsatte standarder og leverede en "paved road" af forhåndsgodkendte, automatisk scannede pipelines, mens sikkerhedsambassadører indlejret på deltid i hvert leveringsteam tog de daglige beslutninger. Platformen genererede compliancebeviser automatisk. Påbudte krav om funktionsadskillelse blev stadig opfyldt, men gennem værktøjer og klare grænseflader frem for en menneskelig flaskehals, hvilket skar udgivelsesledetiden dramatisk og samtidig forbedrede revisionsparatheden.

## Business case: motivation, ROI og TCO

Du betaler for dårligt teamdesign i koordinationsoverhead, og det overhead vokser hurtigere end lineært med antallet af teams, der skal synkronisere for en typisk ændring. Hver overdragelse er en kø med ventetid, en kontekstoverførsel, der mister information, og en ny chance for at misforstå. Når en rutineændring kræver, at tre teams afstemmer deres køreplaner, er den reelle omkostning ikke summen af deres arbejde; det er den langt større omkostning ved planlægning, ventetid og omarbejde. Tegn grænserne om, så de fleste ændringer ligger inden for ét teams ejerskab, og det overhead forsvinder simpelthen.

Indførelsesomkostningen er reel. Omorganiseringer er forstyrrende, og at bygge platforme og inner-source-praksis kræver investering på forhånd, før gevinsten kommer. Men omkostningen ved ikke at indføre dem akkumulerer. Organisationer, der lader strukturen vokse tilfældigt, hober overdragelseskæder, delte flaskehalsteams med kvartalslange køer og arkitekturer fossiliseret af organisationsdiagrammet op. For at argumentere over for ledelsen, mål afhængighedsdrevet forsinkelse: hvor mange aktive initiativer er blokeret af ventetid på et andet team, og hvor længe. Platforms- og topologiinvesteringer betaler sig som regel ved at gøre ventetid til flow, hvilket viser sig som kortere ledetider og højere gennemløb uden at tilføje headcount.

## Anti-mønstre og faldgruber

- At ignorere Conways lov: at designe en arkitektur, organisationsstrukturen ikke kan levere.
- Funktionelle siloer: separate frontend-, backend-, QA- og driftsteams, der skal koordinere ved enhver ændring.
- Flaskehals i delte tjenester: et centralt team, alle projekter skal stå i kø bag.
- Platform som portvagt: et platformsteam, der påbyder frem for at tjene og tilføjer gnidning i stedet for at fjerne den.
- Kognitiv overbelastning: teams, der ejer vildtvoksende, urelaterede systemer, de ikke kan mestre.
- Permanent "samarbejde": to teams evigt sammenfiltret, hvilket tyder på en fejlplaceret grænse.
- Omorganiseringsafhængighed: konstant omrokering, der ødelægger den stabilitet, teams har brug for for at falde til.

## Modenhedsmodel

- **Niveau 1, Opstart.** Teams dannes tilfældigt, efter headcount eller arvet hierarki; ingen navngiver teamtyper eller samspilsformer; funktionelle siloer og flaskehalse i delte tjenester er overalt, og afhængigheder er skjult, indtil de blokerer en udgivelse.
- **Niveau 2, Udvikling.** Nogle stream-aligned teams findes, og en første platforms- eller inner-source-indsats dukker op, men mønstret anvendes ujævnt: nogle få teams ejer deres skive fra ende til anden, mens andre stadig står i kø bag centrale funktioner, og kognitiv belastning drøftes anekdotisk frem for at blive styret.
- **Niveau 3, Standardisering.** De fire teamtyper og de tre samspilsformer er dokumenteret og bruges bevidst i hele organisationen; platforme og inner-source aflaster afhængigheder på tværs af teams; en driftsmodel for sikkerhed, data og design er valgt og nedskrevet, og nye teams dannes efter disse standarder frem for ved improvisation.
- **Niveau 4, Styring.** Topologien måles og styres mod baselines: teams følger kognitiv belastning, afhængighedsdrevet forsinkelse (initiativer blokeret af ventetid på et andet team, og hvor længe), platformes selvbetjeningsandel og brug, samspilsformers varighed og leveringsflowmål som ledetid og ændringsfrekvens. Tærskler udløser handling, for eksempel en køstørrelse, der tvinger en funktion til at føderere, eller et vedvarende samarbejde, der flager en fejlplaceret grænse, så beslutninger hviler på dokumentation frem for mening.
- **Niveau 5, Orkestrering.** Teamdesign forbedres løbende og er integreret med arkitektur, produkt og risikoplanlægning; organisationen omformer grænser, efterhånden som systemet og forretningen udvikler sig, afslutter enabling-forløb, når kapabiliteten er overført, og omfordeler platformsinvestering, når kognitiv belastning skifter, så hurtigt flow er en adaptiv, stående egenskab frem for en engangsomorganisering.

## Idéer til drøftelse

- For en typisk ændring: hvor mange teams skal koordinere, og hvorfor?
- Hvilke af vores teams bærer for stor kognitiv belastning, og hvad kunne en platform aflaste?
- Hvor kæmper vi mod Conways lov i stedet for at tegne grænserne om?
- Tjener vores platformsteams stream-aligned teams, eller står de som portvagter?
- Bør sikkerhed, data og design være centraliseret, føderet eller indlejret hos os lige nu?
- Hvilke "midlertidige" samarbejder er stille blevet til permanente afhængigheder?

## Vigtigste pointer

- Organisationsstrukturen afgør arkitektur og leveringshastighed; design den bevidst.
- Brug de fire teamtyper, med stream-aligned som standard og de øvrige i støtterolle.
- Anvend den omvendte Conway-manøvre for at gøre den ønskede arkitektur til den lette vej.
- Styr kognitiv belastning; afgræns hvert team til et domæne, det kan mestre.
- Begræns og navngiv samspilsformer mellem teams; behandl vedvarende afhængigheder som grænsefejl.
- Vælg centraliserede, føderede eller indlejrede modeller for tværgående funktioner efter skala, og brug InnerSource til at aflaste køer.

## Referencer og videre læsning

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
