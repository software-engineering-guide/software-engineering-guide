# 2.9 Softwarekonstruktion

## Overblik og motivation

[Softwarekonstruktion](https://en.wikipedia.org/wiki/Software_construction) er der, hvor design bliver til kørende kode. Det er det detaljerede arbejde med kodning, verifikation, [enhedstest](https://en.wikipedia.org/wiki/Unit_testing), [integrationstest](https://en.wikipedia.org/wiki/Integration_testing) og [fejlsøgning](https://en.wikipedia.org/wiki/Debugging). Guiden [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) behandler konstruktion som et eget vidensområde, og med god grund: det er her, det meste af dit daglige arbejde foregår. De valg, du træffer linje for linje (hvordan du indeholder kompleksitet, hvordan du håndterer fejl, hvor læseligt du efterlader tingene), afgør, om et system kan forstås, ændres og stoles på i årevis fremover.

I et stort team er konstruktion en gruppeindsats, ikke en solo. Hundredvis af ingeniører skriver ind i en fælles kodebase, der vil overleve enhver enkelts tid i teamet. Så barren er ikke "virker det på min maskine i dag." Den er "kan en fremmed ændre dette sikkert om fem år." Konstruktion forbinder opad til krav (kapitel 2.8) og design (kapitel 2.2), som fortæller dig, hvad der skal bygges, og dets form. Den forbinder sidelæns til kodestandarder (kapitel 2.1), test (kapitel 2.4) og kodegennemgang (kapitel 2.5), som former, hvordan arbejdet udtrykkes, verificeres og inspiceres. God konstruktion forvandler et sundt design til et vedligeholdeligt aktiv. Dårlig konstruktion forvandler selv et godt design til en belastning.

I virksomheds- og offentlige sammenhænge bærer konstruktion ekstra vægt. Disse systemer er langlivede, stærkt regulerede og ofte sikkerheds- eller borgerkritiske. [Defensiv kodning](https://en.wikipedia.org/wiki/Defensive_programming), disciplineret fejlhåndtering og kode, der er åbenlyst korrekt, er ikke finesser her; de er krav til sikkerhed, revision og kontinuitet over årtier og personaleudskiftning. Målet er kode, der kommunikerer sin hensigt, modstår fejl og kan verificeres. Kode, der blot kører, er ikke nok.

## Grundprincipper

- Minimér kompleksitet frem for alt; den primære fjende af konstruktion i stor skala er kode, ingen fuldt ud kan forstå.
- Forudse ændring; konstruér, så sandsynlige fremtidige modifikationer er lokaliserede og billige.
- Konstruér til verifikation; skriv kode, hvis korrekthed er let at kontrollere ved test, gennemgang og ræsonnement.
- Genbrug bevidst; byg på betroede eksisterende komponenter frem for at genopfinde, men undgå kobling til de forkerte abstraktioner.
- Følg standarder; ensartethed på tværs af en kodebase mindsker den kognitive omkostning ved hver fremtidig ændring.
- Håndtér fejl og ugyldige tilstande eksplicit; gør fejlformer synlige frem for tavse.
- Hold kode læselig; konstruktion er kommunikation med fremtidige vedligeholdere først og med compileren dernæst.

## Anbefalinger

### Minimér kompleksitet som den primære disciplin

Gør det at reducere kompleksitet, både essentiel og tilfældig, til dit centrale mål. Skriv små funktioner og moduler med ét formål. Foretræk klare navne frem for kloge tricks. Hold indlejring lav og kontrolflow lineært. Lokalisér beslutninger, så forståelsen af ét stykke kode ikke tvinger dig til at holde hele systemet i hovedet. Kompleksitet er det, der gør store kodebaser langsomme at ændre og farlige at røre, så vej hvert valg efter, om det tilføjer kompleksitet eller fjerner den. Anvend designprincipperne i kapitel 2.2 også i lille skala: høj sammenhængskraft, lav kobling og klar [adskillelse af ansvarsområder](https://en.wikipedia.org/wiki/Separation_of_concerns) betyder lige så meget i en enkelt funktion som i en arkitektur.

### Konstruér til ændring og til verifikation

Tænk fremad til de ændringer, der med størst sandsynlighed kommer (nye forretningsregler, nye integrationer, ny regulering) og isolér dem bag stabile grænseflader, så ændring forbliver lokal. Skriv samtidig kode, der er let at verificere: [rene funktioner](https://en.wikipedia.org/wiki/Pure_function) (samme input giver altid samme output, uden bivirkninger), hvor du kan, minimal skjult tilstand og eksplicitte afhængigheder, så tests kan udskifte dem. Kode, der er svær at teste, er som regel kode, der er svær at forstå og ændre. Testbarhed (kapitel 2.4) er et designsignal, ikke blot en QA-bekymring.

### Genbrug bevidst og standardisér

Ræk ud efter velvedligeholdte, betroede biblioteker og interne komponenter, før du omskriver grundlæggende logik, og brug dem gennem klare grænseflader (kapitel 2.3). Byg genbrugelige komponenter kun når et ægte andet anvendelsestilfælde findes, fordi at generalisere for tidligt i sig selv er en form for kompleksitet. Anvend din organisations kodestandarder og stil (kapitel 2.1) ensartet, helst håndhævet af automatiske formatere og [linters](https://en.wikipedia.org/wiki/Lint_(software)), så hele kodebasen læses, som om én omhyggelig forfatter havde skrevet den.

### Praktisér defensiv programmering med omtanke

Validér input ved tillidsgrænser (eksterne anmodninger, fil- og netværks-I/O, brugerinput) og behandl alle data, der krydser disse grænser, som fjendtlige, indtil det modsatte er bevist. Inde i et veltestet modul skal du dog ikke kvæle hver linje i redundante kontroller, der skjuler logikken og undertrykker reelle fejl. Reglen er enkel: forsvar ved grænserne, stol på dem indenfor. Brug [assertions](https://en.wikipedia.org/wiki/Assertion_(software_development)) til at dokumentere og håndhæve invarianter, der aldrig bør være falske i et korrekt program. Brug [undtagelser](https://en.wikipedia.org/wiki/Exception_handling) og fejlhåndtering til tilstande, der legitimt kan opstå ved runtime. Hold de to adskilte: assertions vogter programmørens antagelser, fejlhåndtering styrer forventet fejl.

### Håndtér fejl eksplicit og fejl sikkert

For hver fejl så beslut bevidst, hvad der skal gøres: genoprette, prøve igen, propagere eller fejle hurtigt. Slug aldrig stiltiende en undtagelse og ignorer aldrig en returneret fejl; en undertrykt fejl vender tilbage som en mystisk defekt senere. Behold kontekst i dine fejlbeskeder og logs, så fejl kan diagnosticeres. I sikkerheds- og borgerkritiske systemer så fejl ind i en sikker, kendt tilstand frem for at fortsætte i en korrumperet. Giv fejlstien lige så meget omtanke som den lykkelige sti, for i produktion er fejlstien, hvor tillid vindes eller tabes.

### Byg kvalitet ind under konstruktion

Kvalitet bygges ind, ikke inspiceres ind bagefter. Skriv enhedstests sammen med koden, kør [statisk analyse](https://en.wikipedia.org/wiki/Static_program_analysis) og linters løbende, og hold funktioner små nok til at ræsonnere om. Brug selvforklarende navne og struktur, så dine kommentarer kan forklare hvorfor, ikke hvad. [Refaktorér](https://en.wikipedia.org/wiki/Code_refactoring) undervejs for at holde koden beboelig. Kodegennemgang (kapitel 2.5) er det menneskelige bagstop, men det meste af kvaliteten skal være der, før gennemgangen overhovedet begynder.

### Vælg og standardisér konstruktionsværktøjer

Standardisér værktøjskæden (compilere, byggesystemer, formatere, linters, statiske analysatorer, debuggere, afhængighedsstyring og IDE-konfigurationer), så hver ingeniør arbejder i et ensartet, reproducerbart miljø. Kobl disse værktøjer ind i pipelinen, så kvalitetskontroller ikke er valgfrie. Indfør AI-assisterede kodeværktøjer bevidst, og behandl deres output som et udkast, der skal bestå de samme standarder, gennemgang og tests som enhver anden kode.

## Afvejninger: fordele og ulemper

| Praksis | Fordele | Ulemper |
|---|---|---|
| Aggressiv minimering af kompleksitet | Læselig, ændringsdygtig, lav fejlrate | Kan føles langsom; risikerer overabstraktion hvis misbrugt |
| Omfattende defensive kontroller | Fanger dårlige tilstande tidligt, robuste grænser | Roder logikken til; kan maskere reelle fejl hvis overdrevet |
| Assertions til invarianter | Dokumenterer og håndhæver antagelser | Slået fra i nogle produktionsbuilds; ikke fejlhåndtering |
| Kraftig genbrug af biblioteker | Mindre kode at eje; hurtigere levering | Afhængighedsrisiko, kobling, eksponering i forsyningskæden |
| Strenge standarder og linting | Ensartet, gnidningsfri kodebase | Opsætning på forhånd; kan føles stiv for enkeltpersoner |
| Konstruktion til testbarhed | Verificerbar, ændringsdygtig kode | Kan tilføje indirektion, nogle ser som ceremoni |

Den centrale afvejning i konstruktion er kortsigtet hastighed versus langsigtet ændringsdygtighed. At skære hjørner (springe fejlhåndtering over, tolerere kompleksitet, ignorere standarder) føles hurtigere i øjeblikket, og det er næsten altid dyrere over systemets liv. Den modsatte fejl er overkonstruktion: for megen defensivitet, spekulativ abstraktion og generalitet, ingen har brug for. Dygtig konstruktion bor i midten: så simpel som muligt, så defensiv som grænserne kræver og ikke mere.

## Spørgsmål til drøftelse med dit team

1. **Hvad er vores fælles, konkrete definition af "for kompleks," og hvor håndhæver vi den før flet?** "Minimér kompleksitet" er konstruktionens centrale disciplin, men som slogan taber den hver diskussion til en deadline. I et stort team, hvor hundredvis af mennesker skriver ind i én kodebase, må kompleksitet være målbar, så aftal signaler, I faktisk vil handle på: funktionslængde, indlejringsdybde, cyklomatisk kompleksitet og antallet af ting, en læser skal holde i hovedet for at forstå én ændring. Tag jeres værste synder med til mødet og spørg, om jeres nuværende gennemgang ville have fanget den. Svaret bør blive til en pipelineport eller et gennemgangstjeklistepunkt, for en tærskel håndhævet af et værktøj er mere værd end et princip håndhævet af viljestyrke, og det sparer jeres næste ansatte for den langsomme ophobning af kode, ingen sikkert kan røre.

2. **Opfører vores fejlstier sig i produktion, som vi designede dem, og hvornår brugte vi sidst en med vilje?** Konstruktionsrådet siger, at I skal give fejlstien lige så meget omtanke som den lykkelige sti, og alligevel er fejlstien som regel den mindst testede kode, I ejer, og i et borgerkritisk eller sikkerhedskritisk system er det her, tillid vindes eller tabes. En undertrykt undtagelse eller en ignoreret returkode bliver en mystisk defekt uger senere, og "fejl ind i en sikker tilstand" er et løfte, I ikke kan holde, hvis I aldrig har set det ske. Tag jeres hændelseshistorik med: hvor mange tidligere nedbrud kunne spores tilbage til en slugt fejl eller en utestet genopretningssti? Handlingen er at teste fejl bevidst (injicér det afviste kort, timeouten, det misdannede input) og at kræve, at hver fejl enten håndteres, logges med kontekst eller propageres, aldrig stiltiende droppes.

3. **Hvilke dele af vores kodebase er svære at teste, og hvad fortæller den vanskelighed os om designet?** Kode, der modstår test, er næsten altid kode, der skjuler tilstand, kobler til de forkerte afhængigheder eller gør for meget, så testbarhed er et designsignal, ikke en QA-eftertanke. På et langlivet virksomhedssystem betyder det noget, fordi de moduler, der er smertefulde at teste i dag, er dem, en fremmed vil være bange for at ændre om fem år. Tag den klasse eller tjeneste med, jeres team frygter at skrive tests for, og spørg hvorfor: er tilstanden skjult, er afhængighederne umulige at udskifte, gør funktionen tre jobs? Svaret bør drive refaktorering mod rene funktioner, eksplicitte afhængigheder og små enheder med ét formål, for at gøre koden verificerbar er det samme arbejde som at gøre den forståelig og billig at ændre.

4. **Hvornår genbruger vi et eksternt bibliotek versus bygger kapaciteten selv, og hvem ejer den risiko i forsyningskæden, vi tager på os?** At række ud efter et betroet bibliotek er hurtigere end at genopfinde grundlæggende logik, men hver afhængighed, I tilføjer, er kode, I ikke kontrollerer, ikke let kan revidere og skal patche den dag, den kompromitteres. I et stort team er faren, at hundrede ingeniører hver trækker deres egne transitive afhængigheder ind, til ingen kan sige, hvad kodebasen faktisk kører. Tag jeres afhængighedsopgørelse med og stil tre konkrete spørgsmål: hvor mange biblioteker er ikke vedligeholdt, hvor mange bærer kendte sårbarheder, og hvor mange omslutter logik, der er enkel nok til at eje selv. Det modstridende hensyn er reelt, fordi at skrive jeres egen kryptografi eller datohåndtering næsten altid er værre end et gennemprøvet bibliotek, så målet er en bevidst genbrugspolitik frem for generel afvisning. I virksomheds- og offentlige sammenhænge så tilføj indkøbs- og licensvinklen, da en ikke-gennemgået afhængighed kan bære en licens, der er uforenelig med jeres forpligtelser, eller en proveniens, ingen revisor vil acceptere.

5. **Hvordan holder vi AI-genereret kode til de samme konstruktionsstandarder som menneskeskrevet kode, og kan vi skelne de to, når det betyder noget?** AI-kodeassistenter producerer plausible udkast hurtigt, og fristelsen er at behandle deres output som færdigt, fordi det kompilerer og ser idiomatisk ud. Kapitlets regel er, at genereret kode består den samme gennemgang, de samme tests og standarder som alt andet, og et stort team må gøre den regel operationel frem for aspirationel. Tag eksempler på AI-assisterede ændringer med, der nyligt blev udgivet, og spørg, om hver bar tests, bestod statisk analyse og blev reelt forstået af det menneske, der indsendte den, eller blev vinket igennem på tillid. Det modstridende pres er hastighed, fordi disse assistenter er reelt produktive, og at sinke hvert forslag til et snegletempo kaster gevinsten væk. I regulerede og offentlige sammenhænge så tilføj proveniens- og ansvarlighedsvinklen, fordi I måske skal attestere, hvem der er ansvarlig for en kodelinje, og om et genereret fragment bærer et licens- eller ophavsretsspørgsmål, I ikke kan besvare.

6. **Er vores konstruktionsværktøjskæde faktisk standardiseret og håndhævet i pipelinen, eller arbejder enkeltpersoner stadig i uforenelige opsætninger?** En fælles værktøjskæde af formatere, linter, statisk analysator, byggesystem og afhængighedsstyring lader en ingeniør bevæge sig trygt på tværs af ukendte tjenester, fordi koden læses som én stemme, og kontrollerne er identiske overalt. Når den driver, genopfinder hvert team sin egen konfiguration, gennemgangstid bruges på at skændes om stil, og fejl, som ét teams analysator ville have fanget, slipper igennem hos et andet. Tag listen med over repositorier, der ikke kører standardkontrollerne på hver commit, og spørg hvorfor hvert valgte at fravælge det. Spændingen er, at en enkelt påbudt opsætning kan føles stiv for teams med reelt forskellige behov, så beslut, hvor ensartethed er gnidningen værd, og hvor en dokumenteret undtagelse er fin. For en stor virksomhed eller et offentligt organ så bind dette til reproducerbarhed og revision, fordi et build, I ikke kan reproducere bit for bit fra en kontrolleret værktøjskæde, er et, I ikke kan forsvare over for en vurderer år senere.

## Sektorperspektiv

**Startup.** Hastighed vinder, så sæt en fælles formatere og linter på plads på dag ét, validér input ved din ene eksterne grænse, og hold den interne kode ren frem for defensiv på hver linje. Spring spekulativ abstraktion og tung proces over: med to eller tre ingeniører har hele teamet kodebasen i hovedet, og den reelle risiko er kompleksitet, der overlever den fælles hukommelse. Støt dig til betroede biblioteker til alt grundlæggende, så du skriver så lidt kode, som du kan eje godt.

**Lille virksomhed.** Uden en dedikeret byggeingeniør og med et stramt budget så foretræk konventioner, dine eksisterende værktøjer håndhæver gratis: en formatere og linter, der følger med sproget, fornuftige standarder og et lille sæt regler, alle kan huske. Køb eller adoptér velvedligeholdte biblioteker frem for at bygge infrastruktur, du ikke kan bemande til at vedligeholde. Brug din begrænsede disciplin på de to ting, der gør mest ondt, når de forsømmes: at validere input ved grænsen og aldrig stiltiende at sluge en fejl.

**Stor virksomhed.** Med hundredvis af ingeniører, der skriver ind i fælles kode, er prioriteten ensartethed og håndhævelse: en standardværktøjskæde koblet ind i pipelinen, porte for statisk analyse og regler for grænsevalidering anvendt overalt, så folk bevæger sig trygt mellem tjenester. Styr afhængigheds- og forsyningskæderisiko som en styret proces frem for improvisation pr. team, og brug assertions til at kode domæneinvarianter, der skal holde på tværs af hvert team. Behandl konstruktionsstandarder som det substrat, der holder en kodebase beboelig gennem årtier og personaleudskiftning.

**Offentlig sektor.** Langlivede, borgerkritiske systemer gør disciplineret konstruktion til et spørgsmål om sikkerhed og ansvarlighed. Isolér flygtige regler som lovgivning bag stabile grænseflader, så ændring forbliver lokal og sporbar til krav, fejl ind i sikre kendte tilstande frem for at fortsætte i en korrumperet, og lever hvert modul med tests, der fungerer som revisionsbevis. Indkøbs- og åbenhedsforpligtelser betyder, at jeres værktøjskæde, afhængigheder og fejlhåndtering må være dokumenteret godt nok til, at en embedsmand, der ankommer år senere, eller en ekstern revisor, kan verificere, at koden er korrekt.

## Eksempler

**Startup.** Et startup med tre ingeniører sætter en fælles formatere og linter op på dag ét og kører dem på hver commit, så kodebasen læses som én stemme, selv når de tilføjer konsulenter. De validerer input ved deres API-grænse og behandler alt udefra som fjendtligt, men holder den interne logik ren frem for at kvæle den i redundante kontroller. Da en betalings-webhook begynder at fejle, er rettelsen hurtig, fordi ingen undtagelse nogensinde blev stiltiende slugt, og fejlbeskeden bærer nok kontekst til at pege direkte på årsagen. Hele opsætningen tog en eftermiddag og sparede dem for den langsomme ophobning af kompleksitet, der ville have gjort deres næste ansattes første uge elendig.

**Stor virksomhed.** Et globalt betalingsfirma håndhæver en fælles værktøjskæde på tværs af hundredvis af ingeniører: automatisk formatering og linting på hver commit, porte for statisk analyse i pipelinen og en regel om, at alle eksterne input valideres ved tjenestegrænser. Domænelogik bruger assertions til at håndhæve invarianter som "en hovedbogspost balancerer altid," mens runtime-tilstande som et afvist kort håndteres som eksplicitte, loggede udfald. Fordi standarderne er ensartede, og fejl aldrig stiltiende slugs, bevæger ingeniører sig trygt på tværs af ukendte tjenester, og produktionshændelser kan diagnosticeres direkte fra logs.

**Offentlig sektor.** Et nationalt skatteagentur bygger et langlivet vurderingssystem, der forventes at køre i årtier under skiftende lovgivning. Konstruktionen isolerer hver skatteregel bag en stabil grænseflade, så årlige lovændringer forbliver lokale og sporbare til krav (kapitel 2.8). Defensiv validering vogter hvert borgervendt input. Fejlstier fejler ind i en sikker tilstand, der aldrig stiltiende udsteder en forkert vurdering. Hvert modul leveres med enhedstests som revisionsbevis. Fordi konstruktionen er standardiseret og veldokumenteret, kan nye embedsfolk sikkert vedligeholde kode skrevet af forgængere, der for længst er gået.

## Business case: motivation, ROI og TCO

Afkastet af disciplineret konstruktion er den varige evne til at ændre software billigt og sikkert, og det er der, det meste af et systems totale ejeromkostninger afgøres. Undersøgelser af softwareøkonomi viser konsekvent, at det meste af et systems livstidsomkostning er vedligeholdelse, og vedligeholdelsesomkostningen domineres af, hvor forståelig og ændringsdygtig koden er. At minimere kompleksitet, håndtere fejl eksplicit og følge standarder sænker direkte omkostningen ved hver fremtidig ændring og hver produktionshændelse.

Omkostningen ved at indføre det er beskeden og mest på forhånd: fastlæg standarderne, kobl linters og analysatorer på, og byg vanen med at skrive verificerbar, defensiv kode. Omkostningen ved forsømmelse akkumuleres derimod. Kompleksitet ophobes til kode, der er langsom at ændre og risikabel at røre. Stille fejl bliver til dyre produktionshændelser. Inkonsistent stil multiplicerer indsatsen ved hver gennemgang og hver onboarding. For at argumentere over for ledelsen, forbind konstruktionskvalitet til andel fejlslagne ændringer, middeltid til genopretning, andel undsluppne fejl og onboarding-tid, som alle forbedres direkte af konstruktionsdisciplin.

## Anti-mønstre og faldgruber

- **Kompleksitetsvækst:** at ophobe kloge, dybt indlejrede eller sprawlende kode, til ingen forstår den.
- **At sluge fejl stiltiende:** tomme catch-blokke og ignorerede returkoder, der forvandler fejl til fremtidige mysterier.
- **Overdreven defensiv programmering:** redundante kontroller overalt, der begraver logikken og maskerer reelle fejl.
- **At forveksle assertions med fejlhåndtering:** at bruge assertions til runtime-tilstande, eller undtagelser til programmørinvarianter.
- **Kopier-og-indsæt-konstruktion:** at duplikere logik i stedet for at genbruge, så rettelser skal laves mange steder.
- **Spekulativ generalitet:** at bygge abstraktioner og konfigurerbarhed til behov, der aldrig kommer.
- **At ignorere standarder:** hver ingeniør koder på sin egen måde, hvilket multiplicerer kognitiv belastning i hele kodebasen.
- **Utestet konstruktion:** at skrive kode uden tilhørende tests og udskyde verifikation til en fase, der aldrig kommer.

## Modenhedsmodel

- **Niveau 1 (Opstart):** Konstruktion er ad hoc og reaktiv; kompleksitet og fejlhåndtering varierer fra person til person; få standarder findes, og stille fejl er almindelige.
- **Niveau 2 (Udvikling):** Kodestandarder, formatere og linters findes, og grundlæggende fejlhåndtering og enhedstest forventes, men praksis er inkonsistent, og hvert team anvender den forskelligt.
- **Niveau 3 (Standardisering):** Minimering af kompleksitet, grænsevalidering, eksplicit fejlhåndtering og testbarhed er dokumenteret og håndhævet i hele organisationen, i pipelinen og i gennemgang, så hele kodebasen læses, som om én omhyggelig forfatter havde skrevet den.
- **Niveau 4 (Styring):** Konstruktionskvalitet måles mod baselines; teamet følger cyklomatisk kompleksitet, andel undsluppne fejl, andel fejlslagne ændringer, testdækning af fejlstier og fund fra kodegennemgang og handler på tendenserne frem for på mening.
- **Niveau 5 (Orkestrering):** Konstruktion forbedres løbende og er integreret i hele organisationen; defensive mønstre, standarder og målinger føder tilbage i refaktorering og værktøj; AI-assisterede værktøjer kører under de samme kvalitetsporte, og praksis tilpasser sig, efterhånden som sprog, regulering og risici ændrer sig.

## Idéer til drøftelse

- Hvor ophobes tilfældig kompleksitet mest i jeres kodebase, og hvilke konstruktionsvaner skaber den?
- Hvad er dit teams faktiske regel for, hvor input valideres, og hvor der stoles på dem?
- Skelner dine ingeniører mellem assertions og fejlhåndtering, og er den skelnen ensartet?
- Hvor meget af jeres kvalitet bygges ind under konstruktion versus fanges senere i gennemgang eller test?
- Hvordan beslutter I, hvornår I skal genbruge et bibliotek versus bygge, givet risikoen i forsyningskæden?
- Hvordan bør AI-genereret kode holdes til de samme konstruktionsstandarder som menneskeskrevet kode?

## Vigtigste pointer

- Konstruktion er, hvor design bliver til vedligeholdelig kode; at minimere kompleksitet er dens centrale disciplin.
- Konstruér til ændring og til verifikation: testbar, ændringsdygtig kode er forståelig kode.
- Forsvar ved tillidsgrænser, stol på dem indenfor, og slug aldrig fejl stiltiende.
- Brug assertions til invarianter og fejlhåndtering til forventede runtime-tilstande; forveksl dem ikke.
- Standardisér værktøjer og stil, genbrug bevidst, og byg kvalitet ind frem for at inspicere den bagefter.

## Referencer og videre læsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
