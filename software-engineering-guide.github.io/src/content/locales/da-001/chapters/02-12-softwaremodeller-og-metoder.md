# 2.12 Softwaremodeller og metoder

## Overblik og motivation

En softwaremodel er en bevidst forenkling af et system, bygget for at besvare et bestemt spørgsmål. En metode er en disciplineret måde at producere software på, herunder de modeller, den bruger undervejs. Sammen udgør de et vidensområde i Software Engineering Body of Knowledge (SWEBOK), fordi de er de mentale værktøjer, du bruger til at ræsonnere om et system før, under og efter, du bygger det. Et UML-klassediagram ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), et [entitet-relationsdiagram](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), en [tilstandsmaskine](https://en.wikipedia.org/wiki/Finite-state_machine), en [formel specifikation](https://en.wikipedia.org/wiki/Formal_specification) og en engangsprototype er alle modeller. [Vandfald](https://en.wikipedia.org/wiki/Waterfall_model), [prototyping](https://en.wikipedia.org/wiki/Software_prototyping), formel udvikling og [agil](https://en.wikipedia.org/wiki/Agile_software_development) er alle metoder.

Hvorfor overhovedet bøvle med modeller? Fordi menneskets arbejdshukommelse er lille, og softwaresystemer er store. Ingen kan holde et system på hundrede tusind linjer i hovedet, så vi tegner billeder og skriver abstraktioner, der viser én facet ad gangen: dataene, kontrolflowet, tilstandene, interaktionerne. En model er aldrig tænkt til at være tro mod koden; den er tænkt til at være egnet til en beslutning. En god model viser præcis, hvad du har brug for for at beslutte noget, og skjuler alt andet.

I store teams er det reelle på spil koordinering og kommunikation. Når hundredvis af ingeniører, arkitekter, analytikere og revisorer arbejder på ét system, er fælles modeller den fælles grund, hvor de forhandler design, krav og risiko. Så tænk på modellering som et værktøj med et job at udføre. Det betaler sig, når en model er billigere end den fejl, den forebygger. Det bliver spild, når du tegner den for sin egen skyld, beholder den længe efter, den er blevet forældet, eller uddyber den ud over den beslutning, den skulle tjene. Modellering hænger tæt sammen med softwarekrav (kapitel 2.8), principper for softwaredesign (kapitel 2.2), arkitektur og dens notationer som C4 og arc42 (kapitel 3.1) og agile arbejdsmetoder (kapitel 10.7).

## Grundprincipper

- Hver model har et formål; hvis du ikke kan navngive den beslutning, en model informerer, så tegn den ikke.
- Abstraktion er modelleringens kerneakt: inkludér det, der betyder noget for formålet, udelad resten.
- Ensartethed betyder noget inden for og på tværs af modeller; modstridende modeller er værre end ingen.
- Modeller er først og fremmest kommunikationsartefakter; deres målgruppe afgør deres notation og detaljeringsgrad.
- Foretræk den letteste model, der besvarer spørgsmålet; uddybning har en bæreomkostning.
- En model er kun så god som dens analyse; en ukontrolleret model er en utestet antagelse.
- Vælg metoden efter problemets usikkerhed, risiko og konsekvens ved fejl.

## Anbefalinger

### Modellér med abstraktion, formål og ensartethed

Begynd hver model med at navngive dens formål og målgruppe. Abstrahér derefter ubarmhjertigt mod det formål: et sekvensdiagram beregnet til at løse en kapløbstilstand bør vise timing og beskeder, ikke hvert felt. Hold dine modeller ensartede med hinanden, så entiteterne i et ERD, klasserne i et klassediagram og navneordene i kravene alle stemmer overens, og ensartede med virkeligheden, hvilket betyder at du opdaterer eller sletter en model, når systemet bevæger sig videre. En forældet model, folk stoler på, er en fare. En forældet model, alle ignorerer, er spild, der stadig koster opmærksomhed.

### Vælg strukturelle eller adfærdsmæssige modeller efter spørgsmålet

Brug strukturelle modeller til at vise, hvad et system består af, og hvordan delene forholder sig: klassediagrammer, komponentdiagrammer og entitet-relationsdiagrammer for datastruktur. Brug adfærdsmæssige modeller til at vise, hvad et system gør over tid: tilstandsmaskiner for objekter med meningsfulde livscyklusser, sekvensdiagrammer for interaktioner på tværs af komponenter og aktivitetsdiagrammer for workflows og forretningsprocesser. Vælg den ene notation, der blotlægger den beslutning, du står over for. De fleste systemer har kun brug for en håndfuld diagramtyper, tegnet selektivt, ikke hele UML-kataloget anvendt på alt.

### Analysér modeller, tegn dem ikke blot

En model tjener sit brød gennem analyse, ikke blot ved at blive tegnet. Tjek en tilstandsmaskine for uopnåelige tilstande, manglende overgange og deadlock. Tjek et ERD for normaliseringsproblemer og forældreløse relationer. Gå et sekvensdiagram igennem mod kravene for at finde manglende fejlstier. Gennemgå dine modeller med de domæneeksperter, der kan spotte, hvad der er galt. Og hvor omkostningen ved fejl er høj, så ræk ud efter værktøjsunderstøttet analyse (modelcheckere, konsistenskontrollører, simulering) frem for at bedømme det med øjet.

### Anvend heuristiske metoder som standard

Det meste software bygges med heuristiske metoder: erfaringsbaserede, iterative tilgange, der bruger modeller uformelt og bedømmer resultater mod forventninger frem for beviser. For de fleste forretnings- og offentlige systemer er det netop rigtigt: krav udvikler sig, og en fejl er som regel genoprettelig. Heuristiske metoder parrer sig naturligt med agil (kapitel 10.7): modellér lige nok til at afstemme teamet, byg derefter og lær.

### Forbehold formelle metoder til kerner med høj konsekvens

[Formelle metoder](https://en.wikipedia.org/wiki/Formal_methods) udtrykker specifikationer i matematik og bruger verifikation, enten bevis eller udtømmende [modelcheck](https://en.wikipedia.org/wiki/Model_checking), til at fastslå egenskaber. De koster reelle færdigheder og tid, og de betaler sig netop, hvor fejl er katastrofal eller uigenkaldelig: sikkerhedskritisk styring, kryptografiske protokoller, afviklingskerner i finansielle systemer og lignende. Anvend dem på den lille kritiske kerne, ikke hele systemet. Og bemærk, at formel specifikation alene, selv uden fuldt bevis, ofte tilføjer værdi blot ved at tvinge dig til at være præcis.

### Brug prototyping til at afvikle usikkerhed

Når krav eller gennemførlighed er uklare, så byg en prototype for at lære, og beslut derefter, med vilje, om den skal udvikles videre eller kasseres. Engangsprototyper udforsker et spørgsmål billigt og slettes derefter. Evolutionære prototyper bliver produktet og skal bygges efter produktionsstandarder. Den klassiske fejl er at lade en engangsprototype glide ind i produktion ved et uheld. Så navngiv prototypens type, før du bygger den.

### Afstem metoden efter risiko, ikke mode

Vælg metoder efter problemets usikkerhed og konsekvensen ved fejl. Høj usikkerhed favoriserer prototyping og agil iteration. Høj konsekvens favoriserer formel analyse og stringent verifikation. Et system med begge har brug for en kritisk formel kerne inde i en ellers agil ramme. Uanset hvad så adoptér ikke en metode blot fordi den er prestigefyldt, eller fordi en leverandør sælger den.

## Afvejninger: fordele og ulemper

| Model eller metode | Anvendt godt | Fejlform |
|---|---|---|
| Strukturelle modeller (UML, ERD) | Fælles billede af dele og data | Diagramvækst; drift fra koden |
| Adfærdsmodeller (tilstand, sekvens, aktivitet) | Blotlægger timing, tilstande og kanttilfælde | Overdetaljerede diagrammer, ingen læser |
| Heuristiske metoder | Hurtige, fleksible, passer til de fleste systemer | Udisciplinerede; skjulte antagelser |
| Formelle metoder | Bevisbare egenskaber for kritiske kerner | Høje omkostninger; misbrugt på hele systemet |
| Prototyping | Billig læring; afvikler risiko tidligt | Engangskode forfremmet til produktion |
| Agile metoder | Tilpasser sig skiftende krav | Springer modellering over, der er nødvendig til svære problemer |

Den tilbagevendende spænding er mellem stringens og hastighed. For lidt modellering sender skjulte antagelser i produktion. For meget modellering brænder indsats af på diagrammer, der aldrig informerer en beslutning, og som rådner i det øjeblik, koden ændrer sig. Der er ingen fast dosis, der løser dette, kun en regel om proportion: invester i en model eller metode i forhold til den usikkerhed, den afklarer, og omkostningen ved at tage beslutningen forkert. En betalingsmotor og et marketing-mikrosite fortjener forskellig behandling.

## Spørgsmål til drøftelse med dit team

1. **Analyserer vi vores modeller, eller tegner vi dem bare og går videre?** En model tjener sit brød gennem analyse, ikke ved at eksistere: en tilstandsmaskine, I aldrig tjekker for uopnåelige tilstande eller manglende overgange, er en utestet antagelse klædt ud som et diagram. I et stort team er det her, reelle fejl gemmer sig, fordi et plausibelt udseende billede stoles på netop, når ingen har gået det igennem mod kravene for at finde den manglende fejlsti eller den forældreløse relation. Tag jeres vigtigste adfærdsmodel med til mødet og prøv at knække den: hvilken overgang er udefineret, hvilken tilstand har ingen udgang, hvilken sekvens har ingen timeout? Hvor omkostningen ved fejl er høj, bør svaret skubbe jer mod værktøjsunderstøttet analyse (modelcheckere, konsistenskontrollører, simulering) frem for at bedømme med øjet, fordi hele grunden til at modellere en kritisk kerne er at finde fejlen på en tavle i stedet for i produktion.

2. **Når to af vores modeller er uenige, hvilken vinder, og hvem lægger mærke til modsigelsen?** Ensartethed betyder noget inden for og på tværs af modeller, og modstridende modeller er værre end ingen, fordi folk handler på begge. På et stort system driver entiteterne i datamodellen, klasserne i designet og navneordene i kravene stille fra hinanden, efterhånden som forskellige teams opdaterer forskellige artefakter, og det første tegn er ofte en produktionsfejl, hvor to komponenter var uenige om, hvad en ting er. Tag et eksempel med: vælg et kernebegreb og tjek, om ERD'et, koden og kravene faktisk er enige om dets form og livscyklus. Hvis de ikke er, så beslut, hvilket artefakt der er autoritativt, og hvem der er ansvarlig for at holde de andre i trit, og vær villige til at slette en model frem for at lade en forældet fortsætte med at lyve for teamet.

3. **Hvilken kerne i vores system taber, hvis den er forkert, reelle penge eller skader nogen, og får den den stringens, den fortjener?** Dette kapitels centrale træk er at afstemme metoden efter risiko: heuristiske og agile metoder til det genoprettelige flertal, formel specifikation og verifikation til den lille kerne med høj konsekvens og billig prototyping til det reelt usikre. Fejlformerne er symmetriske og begge dyre: at anvende formelle metoder på et marketing-mikrosite brænder penge af, og at behandle en afviklingsmotor eller et berettigelsesregelsæt som almindeligt agilt arbejde inviterer den katastrofale, uigenkaldelige fejl. Tag et kort over jeres system med og markér, hvor en fejl er katastrofal versus genoprettelig, og hvor krav er sikre versus ukendte. Svaret bør koncentrere jeres modelleringsinvestering, hvor pengene og tvetydigheden er, og eksplicit holde den tilbage alle andre steder, så en kritisk formel kerne kan sidde inde i en ellers agil ramme uden at nogen af metoderne lækker ind på den andens område.

4. **Hvor meget modellerer vi, før vi skriver kode, og ændrer den dosis sig med den usikkerhed, vi står over for?** Big design up front og slet intet design er begge fejlformer, og den rette dosis ligger imellem, styret af hvor megen usikkerhed en model faktisk afvikler. I et stort team går presset begge veje: en styringsproces kan kræve et fuldt sæt diagrammer før enhver kode og låse beslutninger truffet med mindst information, mens leveringspres kan skubbe et team til at springe den ene tilstandsmaskine over, der ville have fanget et dyrt kanttilfælde. Tag jeres to seneste projekter med og sortér de modeller, I producerede, i dem, der informerede en reel beslutning, og dem, der blev tegnet blot fordi en skabelon bad om dem. I virksomheds- og offentlige programmer, hvor en fasegate eller et godkendelsesudvalg ofte påbyder dokumenter på forhånd, så kom parate til at argumentere for modellering, der følger risiko frem for en fast leveranceliste, så betalingskernen får sin stringens, og det interne rapporteringsværktøj ikke drukner i diagrammer, ingen læser.

5. **Har vi aftalt en fælles notation og et enkelt hjem for vores modeller, eller opfinder hvert team sit eget?** Modeller er først og fremmest kommunikationsartefakter, og deres værdi kollapser, når en tilstandsmaskine tegnet i ét teams værktøj ikke kan læses, findes eller stoles på af det team, der arver den. For hundredvis af ingeniører er de modstridende hensyn reelle: en påbudt notation og et påbudt repositorium køber ensartethed og opdagelighed, men de pålægger også en indlæringsomkostning og kan skubbe folk mod tunge værktøjer, når en fotograferet tavle ville række. Tag eksempler med på, hvor en model faktisk boede (en wiki, et diagramværktøj, et slidedæk, nogens laptop) og spørg, hvem der kunne finde og forstå den seks måneder senere. I virksomheds- og regulerede sammenhænge skærper revisionsvinklen dette: en revisor, der ikke kan finde den aktuelle datamodel eller spore en beslutning tilbage til en dokumenteret tilstandsmaskine, vil behandle systemet som udokumenteret, så aftal en lille fælles notation og et varigt sted, og accepter let optagelse frem for ceremoni overalt, hvor konsekvensen er lav.

6. **Før vi bygger en prototype, beslutter vi så med vilje, om den er engangs eller evolutionær, og holder vi os til det valg?** Den klassiske, dyre fejl er en engangsprototype, der stille glider ind i produktion, fordi den demonstrerede godt, og ingen navngav dens type på forhånd. Spændingen er ægte: engangsprototyper køber den billigst mulige læring og bør slettes, mens evolutionære prototyper bliver produktet og skal bygges efter produktionsstandarder fra første linje, og at forveksle de to enten spilder omarbejde eller sender skrøbelig kode ind i en rolle, den aldrig var konstrueret til. Tag en nylig prototype med og spørg, hvad der blev besluttet, før den blev bygget, hvem der havde autoritet til at forfremme eller kassere den, og om den beslutning overlevede leveringspresset. I offentlige og andre ansvarlige sammenhænge, hvor et borgervendt system bærer forpligtelser om åbenhed og pålidelighed, så behandl utilsigtet forfremmelse som en kontrolfejl: fastlæg prototypens skæbne på forhånd, og gør det at kassere en vellykket engangsprototype til et fejret resultat frem for et spild, der skal undgås.

## Sektorperspektiv

**Startup.** Modellér på en tavle, fotografér den og gå videre. Din knappeste ressource er ingeniørernes opmærksomhed, så ræk ud efter en model kun, når den er billigere end den fejl, den forebygger: en abonnementstilstandsmaskine, før du koder faktureringens kanttilfælde, ikke et fuldt UML-katalog til et produkt, der måske skifter kurs næste måned. Bliv heuristisk og agil, hold formelle metoder helt udenfor, og behandl enhver prototype som engangs, medmindre du bevidst beslutter andet.

**Lille virksomhed.** Du har sandsynligvis ingen, hvis job er formel modellering, så støt dig til de modeller, der allerede er indlejret i de værktøjer og frameworks, du køber, frem for at opstille en modelleringspraksis af din egen. Ram de få modeller, du tegner, ind omkring konkrete beslutninger: en simpel datamodelskitse for at blive enige om, hvilke kundedata du har, et tilstandsdiagram for det ene workflow, der koster dig en kunde, når det går i stykker. Foretræk et købt produkt med en gennemprøvet datamodel frem for at bygge og dokumentere din egen, og hold det, du tegner, let nok til, at én person kan vedligeholde det.

**Stor virksomhed.** Kerneproblemet er koordinering på tværs af mange teams, så fælles modeller bliver den fælles grund: en aftalt datamodel, en ensartet notation og et sted, hvor ERD'et, C4-diagrammerne og tilstandsmaskinerne kan findes og stoles på. Standardisér en lille notation og håndhæv ensartethed, så entiteterne i kravene, designet og databasen ikke driver fra hinanden mellem teams. Forbehold formel specifikation og modelcheck til kerner med høj konsekvens (afvikling, afstemning, adgangskontrol), finansiér den specialistfærdighed, det kræver, og hold et revisionsspor fra hver dokumenteret model tilbage til den beslutning, den retfærdiggjorde.

**Offentlig sektor.** Regler fastsat i lov skal kunne spores til lovtekst, hvilket er der, formel specifikation tjener sin omkostning: specificér berettigelses- eller vurderingslogik præcist, verificér nøgleegenskaber, og lad revisorer spore hvert udfald tilbage til den regel, der producerede det. Indkøb tilføjer sin egen vægt, da dokumenter og modeller ofte er kontraktlige leverancer, så aftal, hvilke modeller der reelt er beslutningsbærende frem for produceret blot for at tilfredsstille en tjekliste. Offentliggør beskrivelser på almindeligt sprog af, hvordan konsekvensrige systemer fungerer, og brug engangsprototyping til at teste borgervendt indtag med rigtige brugere, før I forpligter jer til et produktionsbuild.

## Eksempler

**Startup.** Et lille startup, der bygger et abonnementsfaktureringsprodukt, skitserer abonnementets livscyklus (prøve, aktiv, forfalden, annulleret, genaktiveret) som en tilstandsmaskine på en tavle, før de skriver kode. Da de går diagrammet igennem, bemærker de, at de aldrig definerede, hvad der sker, når en forfalden kontos betaling endelig går igennem, et kanttilfælde, der ville have efterladt reelle kunder i limbo. Den model på fem minutter sparer et produktionsmareridt, og de fotograferer den frem for at vedligeholde et tungt diagramværktøj. Alle andre steder forbliver de agile og modellerer lige nok til at afstemme, fordi en fejl i deres skala er genoprettelig, og formelle metoder ville være ren omkostning.

**Stor virksomhed.** En global bank bygger en ny betalingsplatform. Teamet bruger et entitet-relationsdiagram til at blive enige om den fælles datamodel på tværs af konto-, hovedbogs- og beskedteams og C4-diagrammer (kapitel 3.1) til at vise, hvordan tjenesterne passer sammen. De modellerer transaktionens livscyklus (afventende, clearet, afviklet, tilbageført, bestridt) som en eksplicit tilstandsmaskine, og analysen afslører, at den mangler en overgang for delvise tilbageførsler. Hullet rettes på en tavle frem for i produktion. Sekvensdiagrammer går afviklingsflowet igennem mod kravene (kapitel 2.8) for at afsløre manglende timeout- og genforsøgsstier. Den daglige levering er agil, men kerneafstemningsalgoritmen, hvor en fejl betyder tabte rigtige penge, får en formel specifikation og modelchecks før implementering. Modellering koncentreres, hvor pengene og tvetydigheden er, og holdes let alle andre steder.

**Offentlig sektor.** Et nationalt skatteagentur moderniserer ydelsesvurdering. Fordi berettigelsesregler er fastsat i lov og revideret, skriver teamet en formel specifikation af reglerne som rene transformationer og verificerer nøgleegenskaber, såsom at ingen ansøger er både berettiget og uberettiget, og at hver sag når en afgørelse, så revisorer kan spore udfald tilbage til lovteksten. Ved siden af den formelle kerne bygger teamet en engangsprototype af den borgervendte indtagsformular for at teste med rigtige brugere. De lærer, at en flertrinsguide reducerer fejl, kasserer derefter prototypen og genopbygger indtaget efter produktionsstandarder. Aktivitetsdiagrammer dokumenterer sagsbehandlerens proces fra ende til anden til uddannelse og revision. Reglerne med høj konsekvens får formel stringens; den usikre brugeroplevelse får billig prototyping; ingen af metoderne anvendes, hvor den anden hører hjemme.

## Business case: motivation, ROI og TCO

Afkastet af modellering kommer af at finde fejl tidligere, hvor de er langt billigere at rette. En modsigelse fundet på en tavle koster minutter. Den samme modsigelse fundet i produktion kan koste et nedbrud, et omarbejdsprogram eller, i regulerede domæner, et juridisk ansvar. Modeller sænker også de totale ejeromkostninger ved at tjene som varig kommunikation. Et system, der overlever sine forfattere, det normale i virksomheder og det offentlige, er langt billigere at vedligeholde, når dets datamodel, tilstandsmaskiner og nøgleflows er dokumenteret nøjagtigt.

Omkostningerne er reelle, og du må veje dem. Modeller tager tid at bygge, færdigheder at bygge godt og løbende indsats at holde aktuelle; formelle metoder tilføjer specialistarbejde. Break-even-punktet styres af usikkerhed og konsekvens. Hvor begge er lave, destruerer tung modellering værdi, og agile heuristikker vinder. Hvor enten er høj, betaler målrettet modellering, og for den kritiske kerne formel verifikation, sig tilbage mange gange ved at forebygge den dyre klasse af fejl. For at argumentere over for ledelsen, bind modelleringsinvesteringen til specifikke risici afviklet og til vedligeholdeligheden af langlivede systemer. Og følg, om modeller faktisk bruges, for en ubrugt model er ren omkostning.

## Anti-mønstre og faldgruber

- **Modellering for sin egen skyld:** at producere diagrammer fordi en proces kræver dem, ikke fordi de informerer en beslutning.
- **Forældede modeller, der stoles på som sandhed:** diagrammer, der ikke længere matcher koden, men stadig støttes til.
- **Big design up front:** udtømmende modeller produceret før nogen kode, der låser beslutninger truffet med mindst information.
- **Diagramvækst:** hver UML-type anvendt ensartet, så de få nyttige visninger drukner i støj.
- **Formelle metoder overalt:** at anvende dyr verifikation på kode, hvor konsekvensen ved fejl ikke retfærdiggør det.
- **Utilsigtet forfremmelse af prototype:** en engangsprototype, der stille udgives som produktet.
- **Notation over substans:** at skændes om UML-korrekthed frem for om modellen besvarer spørgsmålet.

## Modenhedsmodel

- **Niveau 1 (Opstart):** Modellering er ad hoc eller fraværende og rent reaktiv; ingen metode er navngivet; modeller, når de overhovedet tegnes, er inkonsistente, uanalyserede og opgivet, så snart mødet slutter.
- **Niveau 2 (Udvikling):** Nogle teams tegner almindelige diagrammer og følger en navngivet metode, men praksis er uens i organisationen: modeller produceres ofte ceremonielt, driver fra koden og analyseres sjældent for fejl.
- **Niveau 3 (Standardisering):** En fælles notation, en dokumenteret metodevalgsguide og konsistensregler er defineret og håndhævet i hele organisationen; modeller vælges efter formål, holdes i trit med systemet, gennemgås for fejl, og metoden afstemmes efter hvert problems risiko.
- **Niveau 4 (Styring):** Modellering måles og styres mod baselines; teams følger, hvor mange fejl analyse fanger før implementering, hvor langt modeller driver fra koden, om hver model faktisk blev konsulteret til en reel beslutning, og det omarbejde og den cyklustid, der spares i forhold til en defineret baseline; metodevalg kalibreres efter målt usikkerhed og konsekvens, og kritiske kerner verificeres formelt mod aftalte dækningsmål.
- **Niveau 5 (Orkestrering):** Modellering og metodevalg forbedres løbende og er integreret med leverings- og risikoplanlægning i hele organisationen; investeringen tilpasser sig, når usikkerhed og konsekvens skifter, modeller holdes rutinemæssigt aktuelle, afvikles eller uddybes på dokumentation, og formelle, heuristiske og prototypemetoder sammensættes, så hver sidder præcis, hvor den betaler sig.

## Idéer til drøftelse

- For jeres seneste projekt, hvilke modeller informerede en reel beslutning, og hvilke blev tegnet blot fordi en proces krævede det?
- Hvor i jeres systemer ville en formel specifikation betale sig selv, og hvor ville den være spild?
- Hvordan beslutter I, om en prototype er engangs eller evolutionær, og håndhæver I den beslutning?
- Hvordan holder I modeller fra at drive ud af trit med koden, eller accepterer I, at nogle bør slettes i stedet?
- Hvad er den rette mængde modellering før kode i jeres sammenhæng, og hvordan ændrer den sig med usikkerhed?
- Hvilken adfærdsmodel (tilstand, sekvens eller aktivitet) ville have fanget jeres seneste produktionshændelse?

## Vigtigste pointer

- En model er en formålsrettet abstraktion; hvis du ikke kan navngive den beslutning, den informerer, så tegn den ikke.
- Afstem strukturelle og adfærdsmæssige modeller efter det specifikke spørgsmål, og hold dem ensartede og aktuelle.
- Analysér modeller; en ukontrolleret model er en utestet antagelse.
- Heuristiske og agile metoder passer til de fleste systemer; forbehold formelle metoder til kerner med høj konsekvens.
- Brug prototyper til at afvikle usikkerhed, og beslut på forhånd, om de er engangs eller evolutionære.
- Invester i modellering i forhold til den usikkerhed, den afklarer, og omkostningen ved at tage beslutningen forkert.

## Referencer og videre læsning

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
