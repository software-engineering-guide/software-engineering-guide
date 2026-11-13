# 2.5 Kodegennemgang og samarbejde

## Overblik og motivation

[Kodegennemgang](https://en.wikipedia.org/wiki/Code_review) er praksissen med at lade en anden end forfatteren undersøge en ændring, før den flettes. Det er en af de aktiviteter med størst løftestang for kvalitet og vidensdeling, en softwareorganisation har, og for store teams er det også en primær mekanisme for koordinering og kultur. Gennemgang fanger fejl, spreder viden om kodebasen, håndhæver standarder og mentorerer ingeniører, men kun når du gør det godt. Gjort dårligt bliver det en flaskehals, en kilde til gnidning eller et gummistempel, der giver falsk tryghed.

For store teams er gennemgang, hvor individuelt arbejde møder kollektivt ejerskab. Det er ofte det vigtigste berøringspunkt mellem ingeniører, der ellers arbejder hver for sig, så dets normer former, hvordan hele organisationen samarbejder. Gennemgang spreder viden, så ingen del af systemet forstås af kun én person, hvilket mindsker [bus-factor](https://en.wikipedia.org/wiki/Bus_factor)-risikoen, faren når viden sidder hos for få mennesker, der plager store, langlivede systemer. Det skaber også et revisionsspor over, hvem der ændrede hvad, og hvem der godkendte det.

I virksomheds- og offentlige sammenhænge bærer gennemgang ofte en compliance-dimension. [Funktionsadskillelse](https://en.wikipedia.org/wiki/Separation_of_duties) (ingen enkelt person kontrollerer en hel følsom ændring), obligatoriske godkendelser og sporbarhed er hyppigt krævede kontroller. En ændring, der rører følsomme systemer, kan kræve gennemgang af bestemte roller, og gennemgangsoptegnelsen bliver revisionsbevis. Din udfordring er at opfylde disse kontroller og samtidig holde gennemgangen hurtig og konstruktiv, i stedet for at gøre den til ceremoni.

## Grundprincipper

- Gennemgå for at forbedre ændringen og dele viden, ikke for at prale.
- Små ændringer får bedre gennemgange, så hold pull requests (PR'er) fokuserede og rimeligt store.
- Gennemgangsventetid er en omkostning for hele teamet. Hurtig behandling holder alle i gang.
- Automatisér det mekaniske (stil, tests, sikkerhedsscanninger), så mennesker gennemgår design og korrekthed.
- Adskil blokerende problemer fra forslag og præferencer, og vær eksplicit om, hvilket der er hvilket.
- Kritisér koden, ikke personen. Feedbacknormer afgør, om gennemgang bygger tillid eller nedbryder den.
- Forfatteren er ansvarlig for at gøre en ændring let at gennemgå.

## Anbefalinger

### Gør pull requests små og velbeskrevne

Hold hver ændring fokuseret på ét logisk anliggende og lille nok til at blive gennemgået omhyggeligt. Store PR'er får overfladiske gennemgange. Giv en klar beskrivelse af, hvad der ændrede sig, hvorfor og hvordan du verificerede det, så gennemgangeren har kontekst. Opdel mekaniske refaktoreringer og adfærdsændringer i separate PR'er, så hver er let at ræsonnere om. En god beskrivelse er forfatterens enkeltstående vigtigste bidrag til gennemgangskvaliteten.

### Fastlæg gennemgangsstandarder og tjeklister

Skriv ud, hvad gennemgangere bør kigge efter: korrekthed, designpasform, testtilstrækkelighed, sikkerhedskonsekvenser, læsbarhed og overholdelse af standarder. En let tjekliste holder gennemgange ensartede og forhindrer vigtige dimensioner i at glide igennem, uden at gøre gennemgangen til afkrydsning. Definér, hvad der kræver gennemgang, hvem der kan godkende, og eventuelle rollebaserede godkendelser, der er nødvendige for følsomme områder.

### Fastlæg og overvåg normer for gennemgangsventetid

Aftal en måltid for behandling, for eksempel at svare inden for en arbejdsdag, og gør gennemgang til en førsteklasses del af dagen frem for noget, der presses ind til sidst. Lange gennemgangskøer standser leveringen og frister ingeniører til overstore, samlede ændringer. Overvåg tid til første gennemgang og tid til flet, og behandl vedvarende ventetid som et procesproblem, der skal rettes, ikke en personlig svaghed.

### Automatisér alt mekanisk

Kør formatering, [linting](https://en.wikipedia.org/wiki/Lint_(software)), tests samt sikkerheds- og afhængighedsscanning i [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), så gennemgangere aldrig bruger opmærksomhed på dem. Spar menneskelig gennemgang til det, maskiner ikke kan bedømme: om designet er rigtigt, om tilgangen passer til systemet, om testene er meningsfulde, og om koden stadig giver mening senere.

### Brug par- og mobprogrammering, hvor de passer

Brug [parprogrammering](https://en.wikipedia.org/wiki/Pair_programming), hvor to ingeniører skriver kode sammen ved én arbejdsstation, til komplekst eller højrisikoarbejde, onboarding og videnoverførsel. Det er løbende gennemgang, og det fjerner ofte behovet for et separat gennemgangstrin. Brug [mobprogrammering](https://en.wikipedia.org/wiki/Mob_programming), hvor hele teamet arbejder på én opgave på én gang, til kritiske designbeslutninger eller til at sprede viden om et besværligt område i teamet. Betragt disse som supplementer til asynkron gennemgang, valgt efter kontekst, ikke erstatninger, der skal påbydes overalt.

### Adoptér automatiseret og AI-assisteret gennemgang med omhu

Brug automatiserede gennemgangsværktøjer og AI-assistenter til at fange almindelige problemer, foreslå forbedringer og lette gennemgangerens byrde, men behandl deres output som input, ikke autoritet. AI-gennemgang er god til overfladeproblemer og ensartethed og dårlig til dyb designdømmekraft og systemkontekst. Hold et menneske ansvarligt for hver godkendelse, især for sikkerhedsfølsomme og compliance-relevante ændringer.

### Fastlæg konstruktive feedbacknormer

Fastlæg normer, der holder feedback specifik, venlig og fokuseret på koden. Opfordr gennemgangere til at stille spørgsmål frem for at give ordrer, til at forklare begrundelsen bag en anmodning og til at rose godt arbejde. Markér blokerende bekymringer og valgfrie forslag tydeligt (for eksempel ved at præfiksere ikke-blokerende noter). Disse normer afgør, om gennemgang styrker teamet eller avler bitterhed.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Asynkron PR-gennemgang | Fleksibel; dokumenteret; skalerer på tværs af tidszoner | Ventetid; mister nuancer; kan føles konfronterende |
| Parprogrammering | Løbende gennemgang; hurtig videnoverførsel; høj kvalitet | To personer på én opgave; trættende; sværere at planlægge |
| Mobprogrammering | Afstemning i hele teamet; spreder dyb viden | Dyr samlet set; ikke til rutinearbejde |
| Obligatorisk flere gennemgangere | Stærk sikkerhed; compliance-venlig | Langsommere; spreder ansvar; kødannelse |
| AI-assisteret gennemgang | Hurtig, utrættelig på almindelige problemer; mindsker byrden | Overser systemkontekst; falsk tillid hvis overtillid |

Den centrale spænding er grundighed versus hastighed. Dybere gennemgang fanger mere, men den sinker leveringen og kan frustrere forfattere. Hurtigere gennemgang bevarer flowet, men risikerer at være overfladisk. Vejen igennem er at afstemme gennemgangsdybden efter ændringens risiko, så trivielle ændringer får en let gennemgang og risikable ændringer en dyb, og at automatisere det mekaniske arbejde væk, så menneskelig indsats koncentreres, hvor det betyder noget.

## Spørgsmål til drøftelse med dit team

1. **Hvad tæller som for stort til én pull request, og opdeler I mekaniske refaktoreringer fra adfærdsændringer?** Dette kapitel siger ligeud, at store PR'er får overfladiske gennemgange, og at forfatteren ejer gennemgangbarheden, og det beder jer adskille refaktoreringer fra adfærdsændringer, så hver er let at ræsonnere om. I et stort team garanterer en kæmpe-PR et gummistempel, som giver falsk tryghed, mens reelle fejl slipper igennem. Tag dokumentationen med: fordelingen af jeres PR-størrelser og hvordan gennemgangsdybden falder, når diffs vokser. Aftal en praktisk størrelsesnorm og en vane med at lande rene refaktoreringer adskilt fra logikændringer, så en gennemganger faktisk kan holde hver ændring i hovedet. Den ene disciplin løfter kvaliteten af hver gennemgang, der følger.

2. **Hvordan skelner I en blokerende indvending fra et valgfrit forslag, og bruges den konvention faktisk?** Kapitlet beder jer adskille blokerende problemer fra præferencer og være eksplicitte om, hvilket der er hvilket, og det peger på at blokere på præference som et ætsende anti-mønster. Uden en fælles konvention læses en gennemgangers stilmening som en påkrævet ændring, hvilket avler bitterhed og sinker leveringen i hele teamet. Tag eksempler fra nylige gennemgange med, hvor en præference standsede en flet, som det konkrete signal. Indfør en let markør, for eksempel et præfiks, der mærker ikke-blokerende noter, så forfattere straks ved, hvad der skal ændres versus hvad der er et forslag. Det holder gennemgangen fokuseret på korrekthed og design frem for smag.

3. **Hvem skal godkende ændringer til sikkerhedsfølsom eller compliance-relevant kode, og hvordan håndhæves den routing?** Dette kapitel beskriver rollebaserede godkendelser, kodeejerskabsregler og funktionsadskillelse, hvor ingen enkelt person kontrollerer en hel følsom ændring, med godkendelsen registreret som revisionsbevis. I virksomheds- og offentlige sammenhænge er disse krævede kontroller, og risikoen er, at de enten bliver sprunget over eller bliver en flaskehals, der fryser leveringen. Tag signalet med: hvilke moduler er følsomme, og dirigerer kodeejerskabsregler i dag disse ændringer til de rette godkendere automatisk. Kod routingen ind i konfigurationen af kodeejerskab og par den med automatiske kontroller og små ændringer, så kontrollen opfyldes uden en menneskelig vagtkø. Beslut dette bevidst frem for at opdage hullet under en revision.

4. **Hvilket gennemgangsventetidsmål har I faktisk aftalt, og måler og håndhæver I det, eller er det kun en ambition?** Kapitlet behandler gennemgangsventetid som en omkostning for hele teamet og beder jer overvåge tid til første gennemgang og tid til flet, og behandle vedvarende forsinkelse som et procesproblem frem for en personlig svaghed. I et stort team beskatter en ejerløs gennemgangskø stille alle: forfattere samler større ændringer for at undgå ventetiden, de ændringer får så overfladiskere gennemgange, og leveringens ledetid driver opad uden en enkelt skyldig. Det modstridende hensyn er, at et hårdt ventetidsmål kan få gennemgangere til at skimme, så hastighed og dybde må afbalanceres frem for at blive byttet blindt. Tag dokumentationen med: jeres nuværende fordeling af tid til første gennemgang, hvordan den varierer efter team og ændringsstørrelse, og hvor gennemgange sidder længst. I virksomheds- og offentlige sammenhænge så bind målet til de flowmålinger, ledelsen allerede følger, fordi en obligatorisk kontrol med flere gennemgangere uden en ventetidsnorm bliver den flaskehals, der fryser leveringen og frister folk til at omgå kontrollen helt.

5. **Til hvilke slags ændringer stoler I på automatiseret og AI-assisteret gennemgang, og hvor skal et menneske forblive ansvarligt?** Kapitlet siger, at I skal behandle AI-gennemgangens output som input, ikke autoritet: stærk på overfladeproblemer og ensartethed, svag på dyb designdømmekraft og systemkontekst, med et menneske ansvarligt for hver godkendelse. Uden en eksplicit grænse driver et stort team ind i overtillid, hvor en grøn bot-kommentar læses som en bestået gennemgang, og reelle design- og sikkerhedsrisici glider igennem under falsk tillid. Det modstridende træk er, at AI-gennemgang reelt letter byrden og utrætteligt fanger almindelige fejl, så at forbyde den spilder løftestang. Tag dokumentationen med: hvor automatiske forslag har fanget reelle problemer, hvor de har produceret støj, og hvilke ændringstyper (sikkerhedsfølsomme, compliance-relevante, arkitektoniske) I aldrig ville lade en maskine godkende alene. Til virksomheds- og offentligt arbejde så navngiv, hvem der bærer ansvaret for en godkendelse, når en AI-assistent var med i løkken, for en revision vil spørge, hvem der gennemgik en ændring, og "værktøjet gjorde" er ikke et svar, en tilsynsmyndighed accepterer.

6. **Hvor bør parprogrammering eller mobbing erstatte asynkron gennemgang, og hvordan bruger I gennemgang til bevidst at mindske bus-factor-risiko?** Kapitlet rammer par- og mobprogrammering ind som løbende gennemgang valgt efter kontekst, og det navngiver gennemgang som mekanismen, der spreder viden, så ingen del af systemet forstås af kun én person. Lades det implicit, koncentreres viden: den samme ekspert gennemgår hver ændring af et delsystem, gennemgangen bliver et gummistempel, fordi ingen andre kan udfordre vedkommende, og bus-factor-risikoen vokser netop, hvor systemet er mest kritisk. Det modstridende hensyn er omkostning, da mobbing bruger hele teamets tid, og parprogrammering binder to ingeniører, så I ikke kan påbyde det overalt. Tag dokumentationen med: hvilke moduler har kun én troværdig gennemganger, hvor går onboarding i stå, og hvor ville et besværligt område have gavn af en live session frem for kommentartråde. I en stor eller offentlig organisation så behandl bevidst videnspredning som risikostyring, for et langlivet system, hvis kritiske dele afhænger af én person, er en operationel og kontinuitetsmæssig forpligtelse, ikke blot en bemandingsulempe.

## Sektorperspektiv

**Startup.** Med tre eller fire ingeniører så hold gennemgangen let: én kollegas godkendelse på en lille pull request, mekaniske kontroller i CI og ingen obligatorisk anden gennemganger, der ville standse en flet. Det reelle mål er mindre compliance end at sikre, at mere end én person forstår hver del af systemet, så par på de risikable dele og behandl det som onboarding. Byg ikke tung routing af kodeejerskab, du snart vokser fra; en fælles norm om små, velbeskrevne ændringer køber det meste af gevinsten til næsten ingen omkostning.

**Lille virksomhed.** Du har næppe en specialist i gennemgangsværktøj, så læn dig op ad det, din hostingplatform (for eksempel en administreret Git-tjeneste) giver dig ud af boksen, frem for at bygge skræddersyet automatisering. Køb linting-, test- og sikkerhedsscanningsintegrationerne i stedet for at vedligeholde dem, så dine få ingeniører bruger deres knappe gennemgangsminutter på design og korrekthed. Hold én simpel regel, hver ændring får ét andet par øjne, og modstå at tilføje proces, du ingen har til at vedligeholde.

**Stor virksomhed.** Udfordringen er ensartethed på tværs af mange teams: fælles standarder, kodeejerskabsregler der dirigerer følsomme ændringer til de rette godkendere, og rollebaserede godkendelser registreret som revisionsbevis. Automatisér de mekaniske kontroller i hele organisationen, så menneskelig gennemgang koncentreres om design, og følg gennemgangsventetid som en flowmåling, så obligatoriske kontroller med flere gennemgangere ikke stille bliver flaskehalse. Afstem gennemgangsdybden efter ændringens risiko med en dokumenteret politik, så trivielle ændringer forbliver hurtige, mens højrisikoændringer får funktionsadskillelse og dybere granskning.

**Offentlig sektor.** Ændringskontrol er ofte obligatorisk: hver produktionsændring gennemgået og godkendt af en anden end forfatteren, med optegnelsen opbevaret som revisionsbevis for at opfylde krav om funktionsadskillelse. Foretræk et gennemsigtigt, sporbart spor over, hvem der forfattede, hvem der godkendte, og hvilke kontroller der bestod, og invester i automatisering og små, hyppige ændringer, så kontrollen ikke fryser leveringen. Hvor gennemgangsværktøj indkøbes, så kræv eksporterbare revisionslogge og undgå indlåsning, da dokumentationen skal overleve enhver enkelt leverandør og kunne bestå offentlig granskning.

## Eksempler

**Startup.** Et startup med fire ingeniører holder hver pull request lille og beder om én kollegas godkendelse før flet, mindre for compliance end for at sikre, at ingen enkelt person er den eneste, der forstår en del af systemet. CI kører formatereren og testene, så menneskerne bruger deres få gennemgangsminutter på design og korrekthed frem for mellemrum. Da teamet rammer en besværlig del af betalingsflowet, parrer to af dem på den i stedet for at bytte asynkrone kommentarer, hvilket tjener som onboarding for den nyeste ansatte.

**Stor virksomhed.** Et stort softwarefirma kræver mindst én godkendende gennemgang på hver ændring, plus en anden godkendelse for ændringer til sikkerhedsfølsomme moduler identificeret ved kodeejerskabsregler. CI håndterer alle stil- og testkontroller, så gennemgangere fokuserer på design og korrekthed. Teamet følger tid til første gennemgang og behandler en stigende median som et signal om at omfordele arbejdsbyrden. Nye ingeniører onboardes gennem parprogrammering, hvilket forkorter deres vej til at bidrage selvstændigt.

**Offentlig sektor.** Et nationalt agentur, der opererer under strenge krav til ændringskontrol, påbyder, at hver produktionsændring gennemgås og godkendes af en anden end forfatteren, med godkendelsen registreret til revision. For at holde kontrollen fra at blive en flaskehals investerer agenturet i automatiske kontroller og små, hyppige ændringer og sætter en norm om svar samme dag. Gennemgangssporet, der dækker hvem der forfattede, hvem der godkendte, og hvilke kontroller der bestod, bliver en del af compliance-dokumentationen for hver udgivelse og opfylder kravene om funktionsadskillelse uden at fryse leveringen.

## Business case: motivation, ROI og TCO

Kodegennemgang betaler sig tilbage i tre valutaer: fejl fanget før produktion, viden spredt i teamet og standarder opretholdt automatisk over tid. At fange en fejl i gennemgang er langt billigere end at fange den i produktion, og vidensdelingsgevinsten mindsker nøgleperson-risikoen, som ellers kan koste en organisation dyrt, når nogen forlader den. Gennemgang er også den kulturelle overførselsmekanisme, der holder et voksende team sammenhængende.

Omkostningen ved gennemgang er ingeniørtid og noget ventetid, begge håndterbare med god praksis. Omkostningen ved *ikke* at gennemgå, eller at gennemgå dårligt, omfatter produktionsfejl, siloopdelt viden, inkonsistent kode og, i regulerede sammenhænge, dumpede revisioner og compliance-fund. For tung gennemgang har sin egen reelle omkostning: lange køer, overstore samlinger, demoraliserede ingeniører. For at argumentere over for ledelsen, forbind gennemgangspraksis til andel fejlslagne ændringer, leveringens ledetid og onboarding-hastighed, og følg gennemgangsventetid som en eksplicit flowmåling.

## Anti-mønstre og faldgruber

- **Gummistemplet:** godkendelser uden reel undersøgelse, som giver falsk tryghed og kun tilfredsstiller kontrollens bogstav.
- **Kæmpe-PR'en:** tusindvis af linjer, der kun kan skimmes, hvilket garanterer overfladisk gennemgang.
- **Gennemgang kun af pedanteri:** fokus på bagateller, mens design og korrekthed overses, ofte fordi mekaniske kontroller ikke er automatiseret.
- **Gennemgang som portvagt:** at bruge gennemgang til at hævde dominans eller blokere andre, hvilket forgifter samarbejdet.
- **Den langsomme kø:** gennemgange, der ligger i dagevis, standser leveringen og tilskynder til samling.
- **Overtillid til AI-gennemgang:** at behandle automatiske forslag som autoritative og droppe menneskelig dømmekraft på risikable ændringer.
- **Blokering på præference:** at præsentere personlige stilmeninger som påkrævede ændringer uden at skelne dem fra reelle fejl.

## Modenhedsmodel

- **Niveau 1, Opstart:** Gennemgang er ad hoc og reaktiv. Den springes ofte over eller udføres inkonsistent, mekaniske problemer dominerer kommentarerne, feedbacknormer er ikke fastlagt, og ethvert godkendelsesspor er tilfældigt frem for bevidst.
- **Niveau 2, Udvikling:** Grundlæggende gennemgangspraksis findes, men varierer fra team til team. Gennemgang er påkrævet nogle steder og langsom eller valgfri andre, automatisering er delvis, og PR-størrelse og kvalitet svinger vidt uden en fælles forventning.
- **Niveau 3, Standardisering:** Standarder er dokumenteret og håndhævet i hele organisationen. Små fokuserede PR'er, automatiseret formatering, linting, tests og sikkerhedsscanning i CI, klare tjeklister, en eksplicit konvention for blokerende versus forslag og kodeejerskabsregler, der dirigerer følsomme ændringer til de rette godkendere.
- **Niveau 4, Styring:** Gennemgang måles og styres mod baselines. Tid til første gennemgang, tid til flet, gennemgangsdybde i forhold til ændringsrisiko, andel undsluppne fejl og andel fejlslagne ændringer følges; vedvarende ventetid behandles som et procesproblem; og data driver, hvor gennemgangerbelastningen skal omfordeles, og hvor kontroller sinker leveringen uden at tilføje sikkerhed.
- **Niveau 5, Orkestrering:** Gennemgang forbedres løbende og er integreret i hele organisationen. Dybden tilpasser sig ændringsrisikoen, parprogrammering, mobbing og AI-assistance bruges bevidst med et menneske ansvarligt, videnspredning og bus-factor-risiko styres med vilje, og gennemgang forbedrer målbart kvalitet, leveringsflow og onboarding.

## Idéer til drøftelse

- Hvad er det rette gennemgangsventetidsmål for dit team, og hvad forhindrer dig i at nå det?
- Hvordan afstemmer I gennemgangsdybde efter ændringsrisiko uden at tilføje bureaukrati?
- Hvor overgår parprogrammering eller mobbing asynkron gennemgang i jeres sammenhæng?
- Hvor meget bør AI-assisteret gennemgang stoles på, og til hvilke slags ændringer?
- Hvordan holder I gennemgangsfeedback konstruktiv, når teamet vokser og bliver mere mangfoldigt?
- Hvordan opfylder I compliance-krav om godkendelse uden at skabe flaskehalse?

## Vigtigste pointer

- Hold pull requests små og velbeskrevne; forfatteren ejer gennemgangbarheden.
- Automatisér det mekaniske, så mennesker gennemgår design, korrekthed og tests.
- Følg og styr gennemgangsventetid som en flowomkostning for hele teamet.
- Afstem gennemgangsdybden efter ændringsrisiko, og skeln blokerende problemer fra præferencer.
- Brug parprogrammering, mobbing og AI-assistance som supplementer efter kontekst, og hold et menneske ansvarligt.

## Referencer og videre læsning

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
