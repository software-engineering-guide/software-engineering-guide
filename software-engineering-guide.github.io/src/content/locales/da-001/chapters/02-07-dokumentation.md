# 2.7 Dokumentation

## Overblik og motivation

[Dokumentation](https://en.wikipedia.org/wiki/Software_documentation) er den skrevne viden, der lader folk bruge, drive og ændre software uden at skulle sammenstykke forståelsen ud fra koden alene. Den kommer i mange genrer: hvordan man kommer i gang, hvordan man udfører en opgave, hvordan et system er struktureret, hvordan man reagerer på en hændelse, hvad en [API](https://en.wikipedia.org/wiki/API) accepterer og returnerer. Hver tjener en forskellig læser med et forskelligt behov. God dokumentation er ikke valgfri. Den er forskellen mellem viden, der skalerer på tværs af en stor organisation, og viden, der bor i nogle få menneskers hoveder.

For store teams er dokumentation dit bedste forsvar mod nøgleperson-risiko (faren når kritisk viden sidder hos kun en eller nogle få) og din hurtigste vej til at onboarde nyankomne. Når hundredvis af ingeniører afhænger af systemer, de ikke selv byggede, og folk kommer, flytter og går hele tiden, kan organisationen kun fungere, hvis viden er skrevet ned og let at finde. Udokumenterede systemer bliver skrøbelige: kun deres forfattere kan sikkert ændre dem, og når de forfattere forlader dem, mister organisationen evnen til at vedligeholde sin egen software. Det er en af de mest almindelige og dyreste fejl i stor skala.

Virksomheds- og offentlige sammenhænge hæver indsatsen yderligere. Systemer lever længe, så din dokumentation skal tjene vedligeholdere år, ja årtier, efter at det oprindelige team er væk. Regulerings- og revisionsregimer kræver ofte bestemte dokumenter som bevis for kontrol: arkitekturoptegnelser, [runbooks](https://en.wikipedia.org/wiki/Runbook) (trin-for-trin drifts- og hændelsesresponsprocedurer) og beslutningslogge. Offentlige systemer, der overdrages mellem leverandører, afhænger helt af dokumentation for at bære viden over kontraktgrænser. Og alligevel er dokumentation berygtet for at rådne, så den reelle udfordring er at holde den nøjagtig, efterhånden som softwaren ændrer sig.

## Grundprincipper

- Skriv til en bestemt læser med et bestemt behov; forskellige dokumentationstyper tjener forskellige formål.
- Hold dokumentation tæt på koden og behandl den som kode (docs-as-code).
- Nøjagtighed slår fuldstændighed; en lille mængde pålidelig dokumentation slår en stor mængde, der er forkert.
- Generér det, der kan genereres; vedligehold ikke i hånden, hvad et værktøj kan producere ud fra sandhedskilden.
- Bekæmp dokumentationsråd aktivt; forældet dokumentation er værre end ingen, fordi den vildleder.
- Gør dokumentation opdagelig; viden, der ikke kan findes, er reelt fraværende.
- Registrér beslutninger og deres begrundelse, ikke kun den nuværende tilstand.

## Anbefalinger

### Adoptér docs-as-code

Hold dokumentation i [versionsstyring](https://en.wikipedia.org/wiki/Version_control) lige ved siden af den kode, den beskriver, skriv den i almindelig tekstmarkup, og gennemgå den gennem den samme pull request-proces. Det holder den versioneret, gennemgåelig og tæt på koden, så du kan opdatere begge sammen. Udgiv den gennem en automatiseret pipeline, så den seneste version altid er tilgængelig. At behandle dokumenter som kode bringer den samme disciplin, der holder kode troværdig: gennemgang, historik og automatisering.

### Strukturér indhold med Diátaxis-rammen

Organisér dokumentation i fire adskilte typer, for at blande dem tjener ingen læser godt: tutorials (læringsorienterede, til nyankomne), how-to-guider (opgaveorienterede, til et bestemt mål), reference (informationsorienteret, præcis og fuldstændig) og forklaring (forståelsesorienteret, hvorfor og konteksten). Hold disse adskilte, og alt bliver lettere at skrive, navigere og vedligeholde, fordi hver side har ét klart job og én klar målgruppe.

### Vedligehold de essentielle driftsdokumenter

Giv hvert repositorium en klar [README](https://en.wikipedia.org/wiki/README) som sin hoveddør: hvad det er, hvordan man bygger og kører det, og hvor man går videre hen. Skriv runbooks til driftsopgaver og hændelsesrespons, så enhver på vagt kan handle, ikke kun eksperterne. Hold arkitekturdokumentation, der forklarer systemets struktur og nøglekomponenter. Og stil onboarding-dokumentation til rådighed, der gør en ny ingeniør produktiv hurtigt. Det er de dokumenter, du savner mest, når de ikke er der.

### Generér API-dokumentation og changelogs fra sandhedskilden

Generér din API-referencedokumentation fra den maskinlæsbare kontrakt eller kodeannotationer, så den ikke kan drive væk fra den faktiske grænseflade. Hold en [changelog](https://en.wikipedia.org/wiki/Changelog), helst genereret fra strukturerede commits eller udgivelsesnoter, så forbrugere kan se, hvad der ændrede sig mellem versioner. At automatisere disse tager den mest råd-udsatte, manuelt vedligeholdte dokumentation af dit bord og holder den troværdig.

### Registrér arkitekturbeslutninger

Fang betydelige arkitektur- og designbeslutninger som lette, daterede optegnelser, der angiver konteksten, beslutningen og dens konsekvenser. Disse beslutningsregistre bevarer den begrundelse, der ellers ville gå tabt, så fremtidige vedligeholdere kan se, hvorfor systemet er, som det er, i stedet for at anfægte det eller gentage gamle fejl. De betaler sig især over de lange levetider for virksomheds- og offentlige systemer.

### Bekæmp dokumentationsråd bevidst

Behandl forældet dokumentation som en fejl. Opdatér dokumenterne som del af den samme ændring, der ændrer adfærd, og gør det til en gennemgangsforventning. Tildel ejerskab, så hvert vigtigt dokument har nogen ansvarlig for det. Gennemgå dokumentation med høj værdi for nøjagtighed fra tid til anden, beskær det forældede, og fjern eller markér tydeligt alt, du ikke længere stoler på. Den dokumentation, der rådner mindst, er levende dokumentation: genereret eller testet mod selve systemet.

### Invester i videnstyring og opdagelighed

Gør dokumentation findbar gennem god søgning, klar navigation og et kendt hjem, så folk kan finde, hvad de har brug for, uden at skulle spørge nogen. Lad den ikke fragmentere på tværs af for mange adskilte wikier og værktøjer. Og fang [tavs viden](https://en.wikipedia.org/wiki/Tacit_knowledge), den uformelle forståelse, der bor i chattråde og folks hoveder, i en varig, findbar form, før den glider væk.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Docs-as-code | Versioneret, gennemgåelig, tæt på koden; lavt råd | Kræver ingeniørdisciplin; mindre venlig over for ikke-tekniske forfattere |
| Wiki / vidensbase | Let at redigere; tilgængelig for alle | Driver fra koden; fragmenterer; rådner stille |
| Genereret dokumentation (API, changelog) | Altid nøjagtig; lav vedligeholdelse | Begrænset til det, kilden udtrykker; kræver værktøj |
| Håndskrevet forklaring | Rig kontekst og begrundelse, maskiner ikke kan producere | Arbejdskrævende; tilbøjelig til at blive forældet |
| Diátaxis-struktur | Klart formål pr. side; lettere at navigere og vedligeholde | Strukturindsats på forhånd; kræver forfatterdisciplin |

Den centrale afvejning er indsats versus nøjagtighed og holdbarhed. Den billigste dokumentation at skrive, en hurtig wikiside, er også den mest udsatte for råd og fragmentering. Den mest holdbare dokumentation, genereret fra kilden eller gennemgået som kode, koster mere disciplin på forhånd, men forbliver troværdig. En god tommelfingerregel: generér, hvad du kan, hold resten tæt på koden og gennemgået som kode, og spar den arbejdskrævende håndskrevne forklaring til den begrundelse, kun mennesker kan give.

## Spørgsmål til drøftelse med dit team

1. **Er jeres dokumenter adskilt efter læserens behov, eller roder tutorials, reference og forklaring sammen på én side?** Dette kapitel anbefaler Diátaxis-opdelingen i tutorials, how-to-guider, reference og forklaring og angiver blanding af typer som et anti-mønster, der ikke tjener nogen læser godt. I stor skala har en nyankommen, der lærer systemet, og en ingeniør på vagt, der leder efter et præcist faktum, brug for forskellige sider, og en enkelt blandet side sinker begge. Tag signalet med: vælg jeres mest besøgte dokumenter og tjek, om hver har ét klart job og én klar målgruppe. Omstrukturér de værste syndere til adskilte typer, så hver side er lettere at skrive, navigere og holde aktuel. Den struktur er det, der gør dokumentation vedligeholdelig, efterhånden som organisationen vokser.

2. **Fanger I betydelige arkitekturbeslutninger med deres begrundelse, eller kun den nuværende tilstand?** Kapitlet anbefaler lette, daterede beslutningsregistre, der angiver kontekst, beslutning og konsekvenser, og bemærker, at de betaler sig mest over de lange levetider for virksomheds- og offentlige systemer. Uden dem kan en vedligeholder år senere ikke se, hvorfor systemet er, som det er, så vedkommende anfægter sunde valg eller gentager gamle fejl. Tag en nylig svær beslutning med, hvis begrundelse nu kun bor i en chattråd eller nogens hukommelse, som det konkrete signal. Adoptér et kort beslutningsregisterformat og gør det at skrive et til en del af enhver betydelig designændring. Begrundelsen er netop den viden, kun mennesker kan give, og som rådner hurtigst, når den ikke er skrevet.

3. **Kan enhver ingeniør på vagt reagere på en hændelse alene ud fra jeres runbooks uden at tilkalde den, der byggede systemet?** Dette kapitel navngiver runbooks som et essentielt driftsdokument, så enhver på vagt kan handle, ikke kun eksperterne, og beskriver et offentligt team, der kun kunne arve et system, fordi runbooks bar viden over en kontraktgrænse. Nøgleperson-risiko er den fejl, dette værner mod: når den ene ekspert er utilgængelig eller væk, forvandler en udokumenteret genopretningsprocedure en rutinehændelse til et nedbrud. Tag dokumentationen med: tag en nylig hændelse og tjek, om runbooken alene ville have løst den. Skriv og test runbooks til de procedurer, folk frygter, og behandl en runbook, der ikke kan stå alene, som en fejl. Det er forskellen mellem en genopretning kl. 2 om natten og en eskalering kl. 2 om natten.

4. **Hvilke af jeres API-referencer og changelogs er genereret fra sandhedskilden, og hvilke er stadig vedligeholdt i hånden og stille driver væk?** Dette kapitel fortæller jer at generere referencedokumentation fra den maskinlæsbare kontrakt eller kodeannotationer, så den ikke kan afvige fra den faktiske grænseflade, og det angiver manuel vedligeholdelse af genererbart indhold som et anti-mønster. For et stort team er en håndskrevet API-dokumentation, der halter efter den reelle grænseflade, værre end ingen: hver forbruger, der stoler på den, skriver en ødelagt integration, og fejlen dukker op langt fra den forældede side, der forårsagede den. Tag det konkrete signal med: tag stikprøver af en håndfuld af jeres mest brugte grænseflader og diff den offentliggjorte reference mod den reelle kontrakt for at se, hvor langt hver er drevet. Hvor I finder drift, så kobl referencen ind i bygget, så den regenereres ved hver ændring, og afvikl den manuelt holdte kopi. I virksomheds- og offentlige sammenhænge, hvor grænseflader forbruges på tværs af teams, leverandører og kontraktgrænser, I aldrig ser, er en autoritativ genereret reference ofte det eneste, der forhindrer integratorer i at bygge mod fiktion.

5. **Hvem ejer hvert dokument med høj værdi, og hvordan ville I i dag lægge mærke til, om et var blevet forældet?** Kapitlet behandler forældet dokumentation som en fejl og advarer om, at ejerløse dokumenter rådner, fordi det at opdatere dem er ingens job, mens forældede dokumenter præsenteret som aktuelle ødelægger tilliden til al jeres dokumentation. I stor skala er faren ikke en enkelt forkert side, men den langsomme erosion af tillid: når læsere først er blevet brændt af forældede instruktioner, holder de op med at stole på hele korpusset og går tilbage til at afbryde folk. Tag et ejerskabskort over jeres mest kritiske dokumenter med og et ærligt svar på, hvordan råd opdages, enten ved gennemgangskadence, generering, tests mod systemet eller ren held. Tildel en navngiven ejer til hvert dokument, der betyder noget, og foretræk levende dokumentation, der er genereret eller testet, så forældelse viser sig mekanisk frem for gennem en flov læser. For virksomheds- og offentlige systemer, der overlever deres oprindelige teams, er ejerløs dokumentation en forpligtelse, en revisor eller en arvende leverandør til sidst vil opkræve jer for.

6. **Hvor opdagelig er jeres dokumentation, og hvor meget kritisk viden bor stadig kun i chattråde og folks hoveder?** Dette kapitel siger, at viden, der ikke kan findes, reelt er fraværende, advarer mod at fragmentere dokumenter på tværs af for mange adskilte wikier og værktøjer og opfordrer jer til at fange tavs viden i varig, findbar form, før den glider væk. I en stor organisation bliver det samme faktum ofte genopdaget, genspurgt og gensvaret hundrede gange, fordi ingen kan finde, hvor det allerede blev skrevet, og hver afgang tager uerstattelig kontekst med ud ad døren. Tag dokumentationen med: tæl, hvor mange separate dokumentationshjem I vedligeholder, prøv at finde tre vigtige fakta alene ved søgning, og notér, hvor de reelle svar viste sig at bo i nogens hukommelse eller en begravet besked. Konsolidér mod et kendt hjem med ægte søgning og klar navigation, og gør det at fange tavs viden til en rutinemæssig del af arbejdet frem for en heroisk redning. I offentlige og stærkt outsourcede sammenhænge, hvor systemer går mellem leverandører og teams ved kontrakt, er opdagelig skrevet viden det eneste, der overlever overdragelsen.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og ingen runway at give af så dokumentér kun, hvad et nedbrud kl. 2 om natten eller en nyansat reelt ville have brug for: en rigtig README pr. tjeneste, én testet runbook for den udrulnings- og genopretningsprocedure, alle frygter, og nogle få daterede noter om de beslutninger, du ellers ville glemme. Generér API-dokumentation fra kontrakten, så du aldrig vedligeholder den i hånden. Modstå at bygge en dokumentationsplatform; en versioneret mappe med markup ved siden af koden er nok, til du mærker reel smerte.

**Lille virksomhed.** Uden en teknisk skribent og med et stramt budget så læn dig op ad den dokumentation, dine værktøjer allerede genererer, og på let docs-as-code frem for et bemandet program. Ram valget ind som køb versus byg: foretræk platforme, der producerer deres egen aktuelle reference og søgbare vidensbase, frem for en wiki, du skal pleje i hånden. Brug din knappe indsats på de to eller tre dokumenter, hvis fravær ville standse virksomheden, og lad en forkert eller manglende side være udløseren til at rette ejerskabet.

**Stor virksomhed.** På tværs af mange teams er problemet ensartethed og opdagelighed: en fælles docs-as-code-pipeline, en fælles struktur som Diátaxis, genererede API-referencer og changelogs og beslutningsregistre anvendt ens overalt, så viden ikke fragmenterer på tværs af dusinvis af wikier. Tildel ejerskab til hvert dokument med høj værdi og mål nøjagtighed, ikke kun tilstedeværelse. Behandl arkitekturoptegnelser, runbooks og beslutningslogge som revisionsbevis, og standardisér, hvordan de produceres, så en kontrolgennemgang finder et dokumenteret, forsvarligt spor frem for panik.

**Offentlig sektor.** Indkøbsregler og offentlig ansvarlighed gør dokumentation til en leverance, ikke en høflighed. Skriv arkitekturdokumentation, runbooks og beslutningsregistre ind i kontrakter som påbudte artefakter, gennemgået for nøjagtighed, så viden overlever et leverandørskifte, og et system kan drives af den, der arver det. Kræv, at enhver autoriseret operatør kan reagere på en hændelse alene ud fra runbooken, og hold beslutningslogge som en gennemsigtig offentlig optegnelse over, hvorfor valg blev truffet. Tynd dokumentation er her ikke en privat ulempe; den bliver til dyr reverse-engineering finansieret af skatteyderne.

## Eksempler

**Startup.** Et startup med fem medarbejdere skriver en rigtig README til hver tjeneste og en kort runbook til den ene udrulnings- og genopretningsprocedure, alle frygter, så et nedbrud kl. 2 om natten ikke afhænger af at vække den ene grundlægger, der kender systemet. De genererer API-dokumentation fra kontrakten i stedet for at skrive den i hånden, og noterer nogle få daterede noter om, hvorfor de valgte deres database og deres tilgang til autentificering. Det forbliver let, men det betyder, at den sjette og syvende ansatte onboarder fra dokumenter frem for ved at afbryde alle.

**Stor virksomhed.** Et stort softwarefirma opbevarer al sin dokumentation i de samme repositorier som sin kode, skrevet i markup og gennemgået i pull requests lige ved siden af de ændringer, de beskriver. API-referencer genereres fra tjenestekontrakter, så de aldrig driver. Changelogs genereres fra strukturerede commits, og arkitekturbeslutningsregistre bevarer begrundelsen bag store valg. Et udgivet dokumentationssite bygges automatisk ved hver flet. Nye ingeniører bliver produktive hurtigt, fordi onboarding-guider og runbooks er aktuelle og findbare, og ingeniører på vagt støtter sig til runbooks i stedet for at tilkalde de oprindelige forfattere.

**Offentlig sektor.** Et nationalt agentur arver et system fra en afgående konsulent og afhænger helt af dokumentation for at bære viden over kontraktgrænsen. Fordi den tidligere leverandør vedligeholdt arkitekturdokumentation, runbooks og beslutningsregistre som påbudte leverancer, kan det nye team drive og ændre systemet uden de oprindelige forfattere. Hvor dokumentationen var tynd, står agenturet over for dyr reverse-engineering. Den erfaring driver en ny politik: dokumentation er en kontraktlig leverance, gennemgået for nøjagtighed frem for behandlet som en eftertanke, og runbooks skal lade enhver autoriseret operatør reagere på hændelser.

## Business case: motivation, ROI og TCO

Dokumentation betaler sig tilbage i kortere onboarding-tid, mindre nøgleperson-risiko, hurtigere hændelsesrespons og en lavere omkostning ved ændring gennem et systems liv. Nye ingeniører, der når produktivitet på dage frem for uger, personale på vagt, der løser hændelser fra en runbook i stedet for at eskalere, vedligeholdere der ændrer et system trygt år efter, det blev bygget: det er store, tilbagevendende besparelser, der akkumuleres på tværs af en stor organisation og et langt systemliv.

Hvad koster dokumentation? Forfatter- og vedligeholdelsesindsats. Hvad koster det *ikke* at dokumentere? Du betaler løbende: i langsom onboarding, gentagne spørgsmål, nøgleperson-flaskehalse, langsommere hændelsesgenopretning og, i yderste konsekvens, systemer ingen sikkert kan ændre, hvilket tvinger dyre omskrivninger eller reverse-engineering. I scenarier med leverandørskifte og revision kan manglende dokumentation bære direkte kontraktlige og compliance-mæssige omkostninger. For at argumentere over for ledelsen, sæt tal på onboarding-tid, hændelsesresponstid og hvor megen kritisk viden der sidder i enkeltes hoveder. Ram derefter docs-as-code og generering ind som måder at få varig dokumentation uden en tilsvarende vedligeholdelsesbyrde. Og understreg, at unøjagtig dokumentation er en forpligtelse, så investeringen må omfatte at holde den aktuel.

## Anti-mønstre og faldgruber

- **Forældet dokumentation præsenteret som aktuel:** vildleder læsere og ødelægger tilliden til al dokumentation.
- **Skriv-én-gang-wikien:** sider oprettet og aldrig opdateret, som stille driver væk fra virkeligheden.
- **Dokumentationsfragmentering:** viden spredt over mange værktøjer og wikier, så intet kan findes.
- **Blanding af dokumentationstyper:** tutorials, reference og forklaring rodet sammen på én side, hvilket ikke tjener nogen læser godt.
- **Manuel vedligeholdelse af genererbart indhold:** manuelt skrevne API-dokumenter, der uundgåeligt afviger fra den faktiske grænseflade.
- **Stammeviden:** kritisk forståelse kun opbevaret i folks hoveder og chathistorik, tabt når de går.
- **Dokumentation som eftertanke:** skrevet til sidst, hvis overhovedet, frem for ved siden af ændringen.
- **Intet ejerskab:** dokumenter uden ansvarlig ejer rådner, fordi det at opdatere dem er ingens job.

## Modenhedsmodel

- **Niveau 1, Opstart.** Dokumentation er spredt, fragmenteret og forældet, og viden bor i folks hoveder. Det, der findes, blev skrevet én gang og aldrig rørt igen, så et nedbrud eller en afgang betyder reverse-engineering af systemet.
- **Niveau 2, Udvikling.** Nøgledokumenter findes, såsom README'er og nogle få runbooks, men de vedligeholdes inkonsistent og er svære at finde. Nogle teams dokumenterer godt og andre næsten slet ikke, og der er ingen fælles forventning til, hvad et repositorium bør bære, eller hvor det bør bo.
- **Niveau 3, Standardisering.** Docs-as-code er normen i hele organisationen: en fælles struktur som Diátaxis, genererede API-referencer og changelogs, beslutningsregistre og en forventning i gennemgang om, at dokumenter ændres sammen med den kode, de beskriver. Hvert dokument med høj værdi har en navngiven ejer, og der er ét kendt hjem med ægte søgning.
- **Niveau 4, Styring.** Dokumentation måles, ikke blot til stede. Du følger dækning af de essentielle dokumenter, dokumentændringsrate mod kodeændringsrate, onboarding-tid, hændelsesløsning alene fra runbooks og friskhed mod en defineret forældelsestærskel, og du gennemgår disse målinger mod baselines. Råd fanges mekanisk gennem generering, tests mod systemet og link- og nøjagtighedskontroller, og forældede sider markeres eller beskæres på dokumentation frem for tilfældighed.
- **Niveau 5, Orkestrering.** Dokumentation forbedres løbende og er integreret i hele organisationen: levende, i vid udstrækning genereret eller testet mod systemet, ejet, opdagelig og adaptiv. Målinger føder tilbage i, hvor I investerer, tavs viden fanges som en rutinemæssig del af arbejdet, og korpusset genbalanceres og beskæres aktivt, efterhånden som systemer, teams og læsere ændrer sig.

## Idéer til drøftelse

- Hvilken dokumentation, hvis den forsvandt i morgen, ville gøre mest ondt på jeres organisation, og findes den i dag og forbliver aktuel?
- Hvordan gør I opdatering af dokumentation til en naturlig del af at ændre kode frem for en separat pligt?
- Hvor kan I erstatte håndskrevet dokumentation med genereret dokumentation knyttet til sandhedskilden?
- Hvordan måler I, om jeres dokumentation er nøjagtig og bliver brugt, ikke blot til stede?
- Hvordan bør AI-assistenter ændre, hvordan I skriver, vedligeholder og søger i dokumentation, og hvor kan de indføre plausibelt, men forkert indhold?
- Hvordan fanger I tavs viden, før de mennesker, der besidder den, forlader jer?

## Vigtigste pointer

- Behandl dokumentation som kode: versioneret, gennemgået, tæt på kilden og udgivet automatisk.
- Strukturér indhold efter læserens behov med tutorials, how-to-guider, reference og forklaring.
- Vedligehold de essentielle med høj værdi: README'er, runbooks, arkitekturdokumenter, onboarding og beslutningsregistre.
- Generér API-dokumentation og changelogs, så de ikke kan drive væk fra sandhedskilden.
- Bekæmp råd med ejerskab, gennemgangsforventninger og beskæring; unøjagtig dokumentation er værre end ingen.

## Referencer og videre læsning

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
