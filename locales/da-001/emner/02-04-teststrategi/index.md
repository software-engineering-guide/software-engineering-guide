# 2.4 Teststrategi

## Overblik og motivation

En [test](https://en.wikipedia.org/wiki/Software_testing)strategi er det bevidste sæt af valg om, hvad der skal testes, på hvilket niveau, hvor automatisk og med hvilken tillid, så dit team kan ændre kode hurtigt uden at ødelægge den. Tests er det, der lader en stor organisation udrulle ofte og sikkert. De koder forventet adfærd, fanger regressioner og giver ingeniører tilliden til at [refaktorere](https://en.wikipedia.org/wiki/Code_refactoring). Uden en sammenhængende strategi har test tendens til at gå én af to dårlige veje: fraværende (frygtdrevet, langsom udvikling) eller oppustet (tusindvis af langsomme, ustabile tests, ingen stoler på).

For et stort team betyder strategien mere end nogen enkelt test. Hundredvis af ingeniører, der arbejder i en fælles kodebase, har brug for et hurtigt, pålideligt sikkerhedsnet. Uden et er hver ændring risikabel, og hver udgivelse bliver en manuel prøvelse. Tests fungerer også som eksekverbar dokumentation af tilsigtet adfærd, hvilket er uvurderligt, når de oprindelige forfattere er gået videre. Strategien afgør, om din testsuite er et aktiv, der fremskynder leveringen, eller en belastning, der trækker den ned.

I virksomheds- og offentlige sammenhænge bærer test ekstra vægt. Regulering kan kræve dokumenteret testdækning og dokumentation. Sikkerhedskritiske og borgervendte systemer kræver høj sikkerhed. Tilgængeligheds- og sikkerhedstest kan være juridisk påkrævet. Så strategien må afbalancere hastighed, tillid, omkostning og compliance, og den må behandle dækning som et signal, ikke et mål, der skal manipuleres.

## Grundprincipper

- Test for at få tillid til at ændre, ikke for at ramme et tal.
- Foretræk hurtige, pålidelige, isolerede tests. Langsomme eller ustabile tests udhuler den tillid, der gør en suite nyttig.
- Skub tests ned til det laveste niveau, der giver reel tillid, og gem langsomme, brede tests til ægte integrationsrisiko.
- En ustabil test er en ødelagt test. Behandl ustabilitet som en førsteklasses fejl.
- Dækning er et signal, ikke et mål. Høj dækning af triviel kode beviser lidt.
- Test adfærd og kontrakter, ikke implementeringsdetaljer, så dine tests overlever refaktorering.
- Gør ikke-funktionel test (tilgængelighed, ydeevne, sikkerhed) til en del af strategien, ikke en eftertanke.

## Anbefalinger

### Brug testpyramiden som standard, og kend kritikken af den

Vælg som standard mange hurtige [enhedstests](https://en.wikipedia.org/wiki/Unit_testing), færre [integrationstests](https://en.wikipedia.org/wiki/Integration_testing) og et lille antal end-to-end-tests, fordi omkostning og skrøbelighed stiger, når omfanget vokser. Kend også kritikken: formen bør følge din arkitektur, ikke dogmet. Et tjenestetungt system kan have brug for et større integrationslag ("testing trophy"), og det reelle mål er tillid pr. enhed omkostning og hastighed, ikke en bestemt silhuet. Uanset hvad du gør, så undgå den omvendte pyramide af for det meste langsomme end-to-end-tests.

### Adoptér TDD, BDD og specifikationsdrevet udvikling, hvor de hjælper

Brug [testdrevet udvikling](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) til at drive design og garantere testbarhed, især for kompleks logik. Det er lige så meget en designdisciplin som en testdisciplin. Brug [adfærdsdrevet udvikling](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) til at udtrykke tests i domænesprog, du deler med interessenter, hvilket er værdifuldt til acceptkriterier i regulerede eller kravtunge miljøer. Specifikationsdrevet udvikling går et skridt videre: den behandler en eksekverbar specifikation (den aftalte adfærd, udtrykt som eksempler) som den enkelte sandhedskilde, der både styrer implementeringen og verificerer den. Det kommer til sin ret, hvor krav skal kunne spores til acceptdokumentation, som i offentlige og regulerede programmer. Beslægtet med alle tre er **[shift-left-test](https://en.wikipedia.org/wiki/Shift-left_testing)**: at flytte verifikation så tidligt som muligt i livscyklussen, skrive tests ved siden af eller før koden og køre dem løbende, så du fanger fejl, når de er billigst at rette, frem for i sene testfaser eller i produktion. Intet af dette er påbudt overalt. Anvend dem, hvor de tilføjer klarhed.

### Brug avancerede teknikker til kode med høj værdi

Brug egenskabsbaseret test (property-based testing) til at kontrollere invarianter på tværs af mange genererede input og fange kanttilfælde, eksempelbaserede tests overser. Brug [fuzz-test](https://en.wikipedia.org/wiki/Fuzzing) på parsere og grænser for ubetroet input for at finde nedbrud og sikkerhedsfejl. Brug [mutationstest](https://en.wikipedia.org/wiki/Mutation_testing) til at måle, om dine tests faktisk opdager injicerede fejl, et langt bedre kvalitetssignal end rå dækning. Brug snapshot-test med omtanke til serialiseret output, og vær opmærksom på fælden at godkende snapshots blindt igen.

### Styr testdata, og brug syntetiske data

Gør tests deterministiske med kontrollerede, isolerede testdata, og undgå fælles mutérbare fixtures, der kobler tests sammen. Generér [syntetiske data](https://en.wikipedia.org/wiki/Synthetic_data), der spejler produktionens egenskaber uden at eksponere reelle personoplysninger, hvilket er afgørende, hvor privatlivsregler forbyder brug af produktionsdata i testmiljøer. Stil fabrikker eller buildere til rådighed, så hver test kan konstruere præcis de data, den har brug for.

### Behandl ustabile tests som fejl

Opdag ustabilitet automatisk, flyt ustabile tests ud af den blokerende sti, og ret eller slet dem inden for en frist. En suite, der fejler tilfældigt, træner ingeniører til at ignorere fejl, hvilket ødelægger hele dens værdi. Følg ustabilitetsrater og gør pålidelighed til en eksplicit kvalitetsmåling for selve testsuiten.

### Brug dækning som signal, og tilføj ikke-funktionel test

Mål dækning for at finde utestede områder, men gør den ikke til et hårdt mål, der inviterer til manipulation med tests uden assertions. Supplér den med mutationstest for dybde. Byg tilgængelighedstest (automatiske kontroller plus manuelle revisioner), ydeevnetest (belastnings- og latensbaselines med regressionsdetektion) og sikkerhedstest (afhængighedsscanning, [statisk analyse](https://en.wikipedia.org/wiki/Static_program_analysis) og dynamisk test) ind i pipelinen.

## Afvejninger: fordele og ulemper

| Testtype / praksis | Fordele | Ulemper |
|---|---|---|
| Enhedstests | Hurtige, præcise, billige, stabile | Overser integrations- og systemniveaufejl |
| Integrationstests | Fanger grænseflade- og forbindelsesfejl | Langsommere; mere opsætning; mere skrøbelige |
| End-to-end-tests | Højeste tillid til reel adfærd | Langsomme, ustabile, dyre at vedligeholde |
| TDD | Bedre design, garanteret testbarhed | Indlæringskurve; føles langsomt i starten |
| Egenskabsbaseret test | Finder kanttilfælde, koder invarianter | Kræver at man tænker i egenskaber; sværere at skrive |
| Mutationstest | Sandt mål for testeffektivitet | Beregningstung; langsom at køre |
| Højt dækningsmål | Afslører utestet kode | Kan manipuleres; kan incitamentere tests uden værdi |

Den centrale afvejning er tillid versus hastighed og omkostning. Bredere tests giver mere tillid, men kører langsommere og går oftere i stykker. Snævrere tests er hurtige og stabile, men overser fejl på systemniveau. Den rette blanding maksimerer tillid pr. sekund feedback og pr. times vedligeholdelse. Og overtest er en reel fejlform: en oppustet suite af redundante, langsomme, skrøbelige tests kan koste mere end de fejl, den forebygger.

## Spørgsmål til drøftelse med dit team

1. **Hvilke ikke-funktionelle tests, tilgængelighed, ydeevne og sikkerhed, skal blokere en udgivelse, og hvilke skal kun rapportere?** Dette kapitel argumenterer for, at ikke-funktionel test hører hjemme i strategien frem for som en eftertanke, og bemærker, at tilgængelighed kan være juridisk påkrævet, og at sikkerhedstest kan være en del af dokumentation for driftsgodkendelse. For et stort eller borgervendt system bremser en blokerende port leveringen, men en tilgængeligheds- eller sikkerhedsfejl fundet i produktion bærer udbedrings-, omdømme- og juridiske omkostninger, der overstiger testen langt. Tag de signaler med, der afgør det: jeres regulatoriske eksponering, om systemet er borgervendt, og hvor ofte disse fejl i dag slipper ud i produktion. Gør de juridisk påkrævede kontroller blokerende, og lad lavrisikokontroller rapportere med en tendens, så porten afspejler reel risiko frem for dogme. Svaret fastlægger direkte, hvad der kan og ikke kan flettes.

2. **Sætter I en hård dækningsprocent som port, og hvis ja, hvad forhindrer ingeniører i at manipulere den med tests uden assertions?** Kapitlet er fast på, at dækning er et signal, ikke et mål, at høj dækning af triviel kode beviser lidt, og at et hårdt mål inviterer til manipulation. Et enkelt tal pålagt hele en stor organisation producerer pålideligt tests, der eksekverer kode uden at hævde noget, hvilket hæver målingen og sænker den reelle tillid. Tag et bedre signal med til drøftelsen: en mutationstestscore på jeres mest værdifulde moduler, der måler, om tests faktisk opdager injicerede fejl. Brug dækning til at finde utestede områder og mutationstest til dybde, og modstå at gøre nogen af dem til et mål, ledelsen følger isoleret. Beslut, hvor tallet reelt hjælper, og hvor det blot inviterer til teater.

3. **Hvad er jeres politik, når testsuiten bliver for langsom til, at ingeniører vil vente på den?** Den centrale afvejning i dette kapitel er tillid versus hastighed og omkostning, og det navngiver overtest som en reel fejlform, hvor en oppustet, redundant, langsom suite koster mere end de fejl, den forebygger. I et stort team er suitens køretid en fælles skat, betalt ved hver ændring, og en suite, folk lærer at omgå, mister al sin værdi. Tag dokumentationen med: CI's vægurstid, de langsomste tests og hvor meget redundant end-to-end-dækning der duplikerer billigere enhedstests. Skub tests ned til det laveste niveau, der giver reel tillid, parallelisér, og slet redundante langsomme tests inden for en frist. At optimere tillid pr. sekund feedback, ikke rå testantal, er målet.

4. **Når en test bliver ustabil, hvem ejer den, hvor hurtigt skal den rettes eller slettes, og hvad håndhæver den frist?** Dette kapitel behandler en ustabil test som en ødelagt test, en førsteklasses fejl, fordi en suite, der fejler tilfældigt, træner et stort team til at ignorere røde builds og stille ødelægger det sikkerhedsnet, alle afhænger af. Det modstridende pres er reelt: at sætte en ustabil test i karantæne fjerner en blokering for leveringen i dag, men risikerer at maskere en ægte intermitterende fejl, mens at blokere på den standser hundredvis af ingeniører over en fejl, der kan være ren støj. Tag den dokumentation med, der afgør det: jeres nuværende ustabilitetsrate, hvor længe tests sidder i karantæne, før nogen rører dem, og hvor mange tests i karantæne viste sig at skjule en reel fejl. Tildel en ejer til hver test i karantæne, sæt en hård frist for at rette eller slette, og følg pålidelighed som en eksplicit måling for selve suiten. I virksomheds- og offentlige sammenhænge, hvor et grønt build er en del af udgivelsesdokumentationen, er en uhåndteret karantænebunke også en revisionsforpligtelse, fordi I udgiver på et signal, I privat har aftalt ikke at stole på.

5. **Må I bruge produktionsdata i testmiljøer, og hvis ikke, hvordan genererer I syntetiske data, der er trofaste nok til at fange reelle fejl?** Kapitlet er direkte på, at privatlivsregler ofte forbyder reelle personoplysninger i test, og at syntetiske data må spejle produktionens egenskaber, ellers giver jeres tests falsk tillid. For en stor organisation er spændingen mellem troværdighed og compliance: produktionsdata fanger de rodede kanttilfælde, syntetiske data overser, men hver kopi af dem multiplicerer jeres eksponering og jeres forpligtelser. Tag detaljerne med: hvilke datasæt bærer personlige eller regulerede data, hvad jeres regler for privatliv og dataresidens faktisk kræver, og hvor godt jeres nuværende fixtures gengiver de fordelinger og kanttilfælde, der ses i produktion. Standardisér fabrikker eller buildere, så hver test konstruerer præcis de data, den har brug for, og invester i syntetisk generering, der matcher reelle demografiske og volumenfordelinger. I offentlige og regulerede programmer er det at bruge borgerdata i et testmiljø ikke en genvej, det er et rapporteringspligtigt brud, så datastrategien må være afklaret, før det første miljø stilles op.

6. **Hvor bør TDD, BDD eller specifikationsdrevet udvikling forventes frem for at være valgfri, og hvem beslutter?** Dette kapitel præsenterer disse som discipliner, der skal anvendes, hvor de tilføjer klarhed, ikke påbud for hver kodelinje, men et stort team har gavn af en fælles standard, så praksis ikke fragmenterer team for team. Afvejningen er mellem design- og sporbarhedsfordelene (eksekverbare specifikationer, politikeksperter kan gennemgå, tests der overlever refaktorering) og den reelle indlæringskurve og langsommelighed i starten, der får et generelt påbud til at slå tilbage. Tag dokumentation med til at afgrænse det: hvilke moduler bærer kompleks logik eller høje andele af fejlslagne ændringer, hvor skal acceptkriterier kunne spores til krav, og hvordan teams, der allerede praktiserer dette, rapporterer om hastighed og fejlrater. Forbehold forventningen til kompleks logik og kravtunge områder, og lad simplere kode vælge selv. I regulerede og offentlige programmer, hvor software skal kunne spores til den lov, den implementerer, er specifikationsdrevet udvikling med eksekverbar acceptdokumentation mindre en præference end en vej til jeres driftsgodkendelse, så navngiv eksplicit, hvor det er påkrævet.

## Sektorperspektiv

**Startup.** Et lille team kan ikke bemande QA, så lad suiten tjene sit brød: hurtige enhedstests på hver commit plus et par end-to-end-tests over den ene sti, der betaler regningerne, og intet, du ikke vil vedligeholde. Spring dækningsmål over og test den logik, du er mest bange for at ødelægge, så du kan udgive flere gange om dagen uden en manuel regressionsrunde. Ret en ustabil test samme dag, for på dette trin er en suite, teamet lærer at ignorere, værre end ingen suite.

**Lille virksomhed.** Uden en dedikeret testingeniør og med et stramt budget så læn dig op ad den test, der er indbygget i de frameworks og værktøjer, du allerede kører, frem for en skræddersyet harness, du ikke kan støtte. Prioritér de få kontroller, der beskytter omsætning og kundetillid, og brug hostet CI, så du ikke selv vedligeholder byggeinfrastruktur. Foretræk at købe tilgængeligheds- og sikkerhedsscanning som en tjeneste frem for at bygge den, da en enkelt overset fejl kan koste mere end et års værktøj.

**Stor virksomhed.** På tværs af mange teams er strategiproblemet ensartethed: en fælles pyramidestandard, automatisk karantæne af ustabile tests og ikke-funktionelle porte, der betyder det samme overalt, så et grønt build er troværdigt, uanset hvem der producerede det. Budgettér suitens køretid som en fælles skat og parallelisér aggressivt, for CI's vægurstid betales ved hver ændring af hver ingeniør. Styr dækning og mutationsscorer som porteføljesignaler med klart ejerskab, ikke tal, ledelsen følger isoleret.

**Offentlig sektor.** Indkøb og tilsyn gør test til dokumentation, ikke blot ingeniørhygiejne. Udtryk berettigelses- og politikregler som eksekverbare specifikationer gennemgået af domæneeksperter, så du kan spore softwaren til den lov, den implementerer, og gør tilgængeligheds- og sikkerhedstest blokerende, fordi de er juridisk påkrævede og del af dokumentationen for driftsgodkendelse. Brug syntetiske data genereret til at matche reelle fordelinger, da borgerdata i et testmiljø er et rapporteringspligtigt brud, og hold testartefakterne reviderbare, så en ekstern gennemgang kan bekræfte præcis, hvad der blev verificeret.

## Eksempler

**Startup.** Et startup med fem medarbejdere har ikke råd til et QA-team, så det støtter sig til en hurtig enhedstestsuite, der kører på hver commit, plus et par end-to-end-tests, der dækker stien fra tilmelding til checkout, som betaler regningerne. Grundlæggerne springer udtømmende dækning over og tester i stedet den logik, de er mest bange for at ødelægge, hvilket lader dem udgive flere gange om dagen uden en manuel regressionsrunde. Da en ustabil test begynder at fejle tilfældigt, retter de den samme dag, for en suite, teamet lærer at ignorere, er værre end ingen suite på det trin, hvor tillid er alt.

**Stor virksomhed.** En stor e-handelsplatform vedligeholder tusindvis af hurtige enhedstests, der kører på hver commit på minutter, et fokuseret sæt integrationstests omkring betalings- og lagergrænser og en lille suite af end-to-end-tests for de kritiske checkout-forløb. Ustabile end-to-end-tests sættes automatisk i karantæne og tildeles til reparation. Fordi ingeniørerne stoler på suiten, udruller de mange gange om dagen, trygge ved at et rødt build betyder et reelt problem.

**Offentlig sektor.** Et nationalt ydelsessystem under regulatorisk tilsyn bruger BDD til at udtrykke berettigelsesregler som eksekverbare specifikationer gennemgået af politikeksperter, hvilket giver sporbar dokumentation for, at softwaren implementerer loven. Det bruger syntetiske data genereret til at matche reelle demografiske fordelinger, fordi privatlivsregler forbyder borgerdata i testmiljøer. Tilgængelighedstest er obligatorisk og blokerer udgivelse, da tjenesten skal kunne bruges af alle borgere. Og sikkerhedstest er en del af dokumentationen for driftsgodkendelse (ATO), den formelle godkendelse til at køre systemet i produktion.

## Business case: motivation, ROI og TCO

Afkastet af test er evnen til at ændre software hurtigt og sikkert, hvilket er fundamentet for vedvarende leveringshastighed. En pålidelig automatiseret suite erstatter langsom, dyr manuel [regressionstest](https://en.wikipedia.org/wiki/Regression_testing) og fanger fejl, når de er billigst at rette, før udgivelsen frem for i produktion. I et reguleret eller borgervendt system overstiger omkostningen ved en produktionsfejl (udbedring, omdømme og potentiel juridisk eksponering) langt omkostningen ved de tests, der ville have fanget den.

Indførelsesomkostningen er reel: du skriver og vedligeholder tests og bygger [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI)-infrastruktur. Men omkostningen ved ikke at teste er højere og akkumuleres: frygtdrevet udvikling, der sinker til et snegletempo, hyppige regressioner og manuelle udgivelsesprocesser, der ikke kan skalere. Der er også en omkostning ved overtest, så argumentet er for en veldesignet strategi, ikke det maksimale antal tests. For at argumentere over for ledelsen, forbind suiten til udrulningsfrekvens, andel fejlslagne ændringer og middeltid til genopretning, og kvantificér den manuelle testindsats, den erstatter, og de produktionshændelser, den forebygger.

## Anti-mønstre og faldgruber

- **Flødeis-kræmmerhus-test:** for det meste langsomme end-to-end-tests oven på en tynd enhedsbase; langsom, ustabil, dyr.
- **Dækning som mål:** at jage en procent med tests uden assertions eller trivielle tests, der ikke beviser noget.
- **Test af implementeringsdetaljer:** tests koblet til det indre, der går i stykker ved hver refaktorering og modvirker ændring.
- **Tolereret ustabilitet:** tilfældige fejl, der træner teamet til at ignorere røde builds.
- **Fælles mutérbare testdata:** tests, der forstyrrer hinanden og fejler uforudsigeligt.
- **Brug af produktionsdata i test:** et brud på privatliv og compliance, der venter på at ske.
- **Ikke-funktionel test sprunget over:** tilgængelighed, ydeevne og sikkerhed opdaget først i produktion.
- **Den upålidelige suite:** så upålidelig, at ingeniører rutinemæssigt kører den igen eller omgår den, hvilket ophæver dens formål.

## Modenhedsmodel

- **Niveau 1, Opstart:** Test er manuel og reaktiv; automatiseret dækning er minimal; regressioner er hyppige og fanges sent, ofte af brugere frem for suiten.
- **Niveau 2, Udvikling:** Automatiserede enheds- og nogle integrationstests findes, men suiten er langsom eller ustabil, tilliden er lav, og praksis varierer vidt fra team til team.
- **Niveau 3, Standardisering:** En afbalanceret, hurtig, pålidelig suite lukker hver ændring; en dokumenteret pyramidestandard, en politik for ustabile tests og ikke-funktionel test (tilgængelighed, ydeevne, sikkerhed) håndhæves ensartet på tværs af teams.
- **Niveau 4, Styring:** Suitens sundhed måles og styres mod baselines; ustabilitetsrate, CI's vægurstid, mutationsscore på moduler med høj værdi og andel undsluppne fejl følges og gennemgås; dækning er ét signal blandt flere, og porte udløses på dokumentation frem for mening.
- **Niveau 5, Orkestrering:** Avancerede teknikker (egenskabsbaseret, mutations- og fuzz-test) rettes mod kode med høj værdi; test er integreret med leveringsmålinger som udrulningsfrekvens, andel fejlslagne ændringer og middeltid til genopretning; organisationen omformer løbende suiten efter sin arkitektur og risiko, afvikler redundante tests og investerer, hvor dokumentation viser, at fejl stadig slipper ud.

## Idéer til drøftelse

- Hvilken form har jeres testfordeling faktisk, og matcher den jeres arkitektur og risiko?
- Hvordan afgør I, hvornår et stykke kode berettiger egenskabsbaseret eller mutationstest frem for eksempeltests?
- Hvad er jeres politik for ustabile tests, og bliver den faktisk håndhævet?
- Hvordan genererer I realistiske syntetiske data uden at lække følsomme oplysninger?
- Hvor hjælper dækning jer reelt, og hvor er den blevet manipuleret?
- Hvordan bør AI-genererede tests gennemgås, så de tilføjer tillid frem for støj?

## Vigtigste pointer

- Test for at få tillid til at ændre; optimér tillid pr. enhed hastighed og omkostning.
- Brug pyramiden som standard, men form testen efter din arkitektur.
- Behandl ustabile tests som fejl og dækning som et signal, ikke et mål.
- Anvend avancerede teknikker, hvor værdien retfærdiggør omkostningen.
- Medtag tilgængeligheds-, ydeevne- og sikkerhedstest i strategien, og brug syntetiske data til at beskytte privatlivet.

## Referencer og videre læsning

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles on the Test Pyramid and test-related patterns
