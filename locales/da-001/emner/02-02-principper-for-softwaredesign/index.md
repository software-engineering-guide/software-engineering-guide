# 2.2 Principper for softwaredesign

## Overblik og motivation

Principper for softwaredesign er tommelfingerregler for at arrangere kode, så du kan forstå, ændre og udvide den over tid. De omfatter navngivne akronymer ([SOLID](https://en.wikipedia.org/wiki/SOLID) for fem [objektorienterede](https://en.wikipedia.org/wiki/Object-oriented_programming) designprincipper, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) for don't-repeat-yourself, [KISS](https://en.wikipedia.org/wiki/KISS_principle) for keep-it-simple, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) for you-aren't-gonna-need-it), strukturelle begreber ([kobling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [sammenhængskraft](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [adskillelse af ansvarsområder](https://en.wikipedia.org/wiki/Separation_of_concerns)), katalogiserede [designmønstre](https://en.wikipedia.org/wiki/Software_design_pattern), modelleringstilgange på højere niveau som [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (at modellere software i forretningsdomænets sprog) og valget mellem objektorienterede, [funktionelle](https://en.wikipedia.org/wiki/Functional_programming) og [dataorienterede](https://en.wikipedia.org/wiki/Data-oriented_design) stilarter. Intet af dette er love. Det er komprimeret erfaring, og du må anvende det med dømmekraft.

For store teams er værdien af fælles principper koordinering. Når hundredvis af ingeniører arbejder på det samme system, har de brug for et fælles ordforråd til designdiskussioner og et fælles sæt standarder, så uafhængigt skrevne moduler passer sammen. Godt design er det, der lader mange mennesker ændre et system parallelt uden konstante sammenstød. Det er også det, der holder et system ændringsdygtigt et årti senere, den normale levetid for virksomheds- og offentlige systemer, langt ud over deres oprindelige forfatteres ansættelse.

Den afgørende færdighed er ikke at lære principper udenad. Det er at vide, hvornår hver enkelt vildleder dig. Hvert princip har en fejlform: DRY kan producere den forkerte abstraktion, SOLID kan producere unødig indirektion, YAGNI kan sulte en udvidelsesevne, du reelt har brug for. Dette kapitel behandler principper som værktøjer med et anvendelsesområde, og det fremhæver kobling og sammenhængskraft som de dybere egenskaber, som akronymerne forsøger at tjene.

## Grundprincipper

- Styr kobling og sammenhængskraft først; de fleste navngivne principper er indirekte måder at forbedre disse to egenskaber på.
- Optimér for ændring: godt design minimerer omkostningen ved de ændringer, du faktisk får brug for at lave.
- Foretræk det simpleste design, der virker nu, men behold grænser, hvor ændring er sandsynlig.
- Duplikering er billigere end den forkerte abstraktion; vent, til mønstret er klart.
- Gør afhængigheder eksplicitte og peg dem mod stabile ting.
- Modellér domænet i domænets sprog; afstem softwaregrænser med forretningsgrænser.
- Vælg paradigmer efter problemet, ikke ideologi; de fleste store systemer er pragmatisk blandede.

## Anbefalinger

### Brug SOLID som en linse, ikke en tjekliste

Anvend single-responsibility for at holde moduler sammenhængende, dependency-inversion for at pege afhængigheder mod abstraktioner, hvor en grænse reelt findes, og open-closed, hvor udvidelsespunkter er reelle. Fremstil ikke grænseflader, fabrikker og lag blot for at tilfredsstille akronymet, når der kun er én implementering og ingen anden i sigte. Indirektion har en omkostning, og du betaler den ved hver læsning.

### Anvend DRY på viden, ikke på tekst

DRY handler om ikke at duplikere ét autoritativt stykke *viden*. Det handler ikke om at fjerne linjer, der blot ligner hinanden. To stykker kode, der ligner hinanden, men ændres af forskellige grunde, bør forblive adskilte. Foretræk lidt duplikering frem for en for tidlig delt abstraktion, der kobler urelaterede ting. Uddrag abstraktionen, når det rigtige mønster har vist sig to eller tre gange.

### Lad KISS og YAGNI modstå spekulation

Byg til de krav, du har, ikke dem, du forestiller dig. Undgå spekulativ generalitet, såsom konfigurerbare frameworks, plugin-systemer og udvidelsespunkter, ingen har bedt om. Modvægten er, at noget fleksibilitet reelt er billigere at bygge ind tidligt, som en stabil grænseflade eller en ren sømlinje. YAGNI argumenterer mod spekulativ *implementering*, ikke mod gennemtænkte grænser.

### Design eksplicit til lav kobling og høj sammenhængskraft

Lad hvert modul gøre én veldefineret ting (sammenhængskraft), og afhænge af så få andre moduler som muligt, gennem snævre grænseflader (lav kobling). Når du gennemgår et design, så spørg, hvilke ændringer der bølger på tværs af modulgrænser. De bølger er det sande mål for kobling. Adskillelse af ansvarsområder er den samme idé anvendt på lag og tværgående anliggender.

### Brug designmønstre som ordforråd, anvend anti-mønstre som advarsler

Mønstre er nyttige fælles navne for tilbagevendende løsninger. Ræk ud efter ét, når problemet faktisk matcher det. Pålæg ikke mønstre for at se sofistikeret ud, for mønstertung kode er ofte et tegn på overkonstruktion. Lær de almindelige [anti-mønstre](https://en.wikipedia.org/wiki/Anti-pattern) (gudeobjekter, anæmiske modeller hvor de er upassende, big balls of mud, distribuerede monolitter) som diagnostiske betegnelser.

### Adoptér Domain-Driven Design, hvor domænet er komplekst

For systemer med rige forretningsregler så brug DDD's taktiske og strategiske værktøjer: et allestedsnærværende sprog delt med domæneeksperter, afgrænsede kontekster (bounded contexts), der skærer systemet i uafhængigt modellerede stykker, og kontekstkort, der beskriver, hvordan stykkerne forholder sig til hinanden. Afgrænsede kontekster er især værdifulde i virksomhedsskala, fordi de afstemmer teamejerskab med modelgrænser. DDD er overkill til simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)-systemer (create, read, update, delete).

### Vælg paradigmer efter pasform

Brug objektorientering til at indkapsle tilstandsfuld adfærd og modellere domæner. Brug funktionel stil til transformationer, samtidighed og forudsigelighed gennem [uforanderlighed](https://en.wikipedia.org/wiki/Immutable_object). Brug dataorienteret design, hvor ydeevne og cache-adfærd dominerer. Store systemer blander alle tre. Træf valget pr. komponent, og hold grænserne mellem stilarter rene.

## Afvejninger: fordele og ulemper

| Princip / tilgang | Anvendt godt | Fejlform |
|---|---|---|
| SOLID | Klare sømme, hvor ændring sker; testbare enheder | Vækst i grænseflader og lag; indirektion uden gevinst |
| DRY | Én sandhedskilde for reel viden | Forkert abstraktion, der kobler urelateret kode |
| KISS / YAGNI | Slanke, forståelige systemer | Underdesignede sømme; dyre eftermonteringer af nødvendig fleksibilitet |
| Designmønstre | Fælles ordforråd; gennemprøvede strukturer | Mønster-cargo-kult; utilsigtet kompleksitet |
| Domain-Driven Design | Afstemte modeller og teams; tæmmet kompleksitet | Tung ceremoni på simple domæner; forkert placerede kontekstgrænser |
| Funktionel / uforanderlig | Forudsigelighed; sikrere samtidighed | Akavet pasform til iboende tilstandsfulde problemer; ydeevneoverraskelser |

Den tilbagevendende spænding er mellem underdesign og overdesign. Underdesignede systemer samler kobling og bliver stive. Overdesignede systemer drukner i abstraktion, som nogen skal forstå og vedligeholde. Svaret er ikke et fast punkt. Det er en disciplin: udskyd beslutninger, til du har nok information, mens du beholder de sømme, der lader dig skifte mening.

## Spørgsmål til drøftelse med dit team

1. **Hvad er jeres konkrete tærskel for at uddrage en fælles abstraktion, og hvordan forhindrer I, at DRY producerer den forkerte?** Dette kapitel er ligefremt om, at duplikering er billigere end den forkerte abstraktion, og at I bør vente, til mønstret har vist sig to eller tre gange, før I uddrager. I et stort team er faren, at nogen faktoriserer to ens udseende uddrag ind i et fælles modul på tværs af teamgrænser, hvorefter hver fremtidig ændring af den ene kalder bølger ind i den anden. Det signal, I skal bringe, er om dubletterne ændres af samme grund eller blot ligner hinanden lige nu. Aftal en regel om tre, og kræv, at en kandidat til abstraktion faktisk har ændret sig sammen, før I kobler kalderne. Den ene aftale forhindrer en klasse af kobling, der er dyr at løse op, når mange teams afhænger af den.

2. **Hvordan gør I kobling og sammenhængskraft synlige i designgennemgang i stedet for at overlade dem til mavefornemmelse?** Grundprincipperne stiller kobling og sammenhængskraft over ethvert akronym og definerer kobling som de ændringer, der bølger på tværs af modulgrænser. Intuition skalerer ikke på tværs af hundredvis af ingeniører, der hver kun ser deres hjørne af systemet. Tag dokumentation med, en maskine kan producere: afhængighedsgrafer og samændringsdata, der viser, hvilke moduler der bliver ved med at blive redigeret sammen i de samme commits. Tilføj et eksplicit gennemgangsspørgsmål, der spørger, hvilke modulgrænser en ændring tvinger jer til at krydse. Når to moduler altid ændres sammen, er det jeres signal til enten at slå dem sammen eller rette grænsen imellem dem.

3. **Hvor går grænsen i jeres systemer mellem et domæne, der er rigt nok til at retfærdiggøre Domain-Driven Design, og en almindelig CRUD-app, hvor det er overkill?** Kapitlet anbefaler DDD's afgrænsede kontekster netop fordi de afstemmer teamejerskab med modelgrænser, og advarer om, at DDD er overkill til simple create-read-update-delete-systemer og forfalder til ceremoni uden reel modellering. At tage fejl i begge retninger er dyrt: tung DDD på et tyndt domæne begraver en simpel app i ceremoni, mens en vidtstrakt fælles model på tværs af mange teams tvinger konstant koordinering mellem teams. Tag de signaler med, der faktisk afgør det: tætheden af forretningsregler og hvor mange teams, der skal eje stykker uafhængigt. Forbehold det strategiske maskineri til den komplekse kerne, og lad de simple kanter forblive simple. Det holder jer fri af både DDD-teater og big ball of mud.

4. **Hvornår er en abstraktion, grænseflade eller et designmønster den indirektion værd, det tilføjer, og hvem har autoriteten til at kalde et design overkonstrueret?** Dette kapitel er eksplicit om, at indirektion har en omkostning, du betaler ved hver læsning, og at fremstille grænseflader, fabrikker og lag for at tilfredsstille SOLID eller for at se sofistikeret ud er en fejlform. I et stort team går presset den anden vej: gennemgangere vinker ekstra abstraktion igennem, fordi det ser disciplineret ud, og ingen vil være den, der argumenterer for mindre struktur. Det modstridende hensyn er reelt, for nogle sømme fortjener reelt deres plads, og at fjerne dem senere er dyrt. Tag konkret dokumentation med til drøftelsen: hvor mange implementeringer en grænseflade faktisk har i dag, hvor ofte udvidelsespunktet nogensinde har bøjet sig, og hvor mange filer en læser skal åbne for at følge én kodesti. Aftal, at en enkelt implementering uden en anden i sigte som standard er en grund til at flette ind, og navngiv, hvem der kan kalde et design overkonstrueret uden at det læses som en fornærmelse. I virksomheds- og offentlige systemer, der overlever deres forfattere med et årti, er unødig indirektion en skat, hver fremtidig vedligeholder betaler, så behandl "hvad køber denne abstraktion os" som et stående gennemgangsspørgsmål, ikke en personlig udfordring.

5. **Hvordan beslutter I, hvilket paradigme hver komponent bruger, objektorienteret, funktionelt eller dataorienteret, og hvordan holder I grænserne mellem dem rene?** Kapitlet argumenterer for, at store systemer er pragmatisk blandede, og at I bør vælge pr. komponent efter pasform: objektorientering til tilstandsfulde domæner, funktionel stil til transformationer og samtidighed og dataorienteret design, hvor ydeevne og cache-adfærd dominerer. Uden styring bliver paradigmevalget et spørgsmål om, hvem der skrev modulet først, og mutérbar tilstand lækker ind i det, der skulle være rene transformationer, eller en funktionel purisme kæmper mod et iboende tilstandsfuldt problem. Den dokumentation, der er værd at bringe, er, hvor jeres faktiske smerte er: hvilke komponenter er svære at teste på grund af skjult tilstand, hvilke hotte stier er cache-bundne, og hvor tvinger den nuværende stil akavede omveje. Beslut standardparadigmet for hvert lag bevidst og skriv ned, hvor sømmene mellem stilarter falder, så en funktionel kerne og en imperativ kant ikke løber ind i hinanden. For et reguleret eller offentligt system, hvor en beregning skal være reviderbar og reproducerbar for en given periode, er en uforanderlig, funktionel kerne ofte et compliance-krav frem for en smagssag, og den begrænsning bør drive grænsen frem for at følge den.

6. **Hvordan forhindrer I, at disse principper hærder til dogme, og hvor registrerer I begrundelsen bag en designbeslutning, så et fremtidigt team kan genbesøge den?** Hvert princip i dette kapitel har et anvendelsesområde og en fejlform, og hele rammen behandler dem som værktøjer, der skal anvendes med dømmekraft, frem for love, der skal håndhæves. I et stort team bliver et princip stille til en regel: DRY forbyder enhver duplikering, SOLID påbyder en grænseflade pr. klasse, og pragmatiske undtagelser bliver blokeret i gennemgang af folk, der citerer akronymet frem for resultatet. Spændingen er, at en vis ensartethed reelt hjælper hundredvis af ingeniører med at koordinere, så I ikke bare kan erklære ethvert princip valgfrit. Tag eksempler med, hvor det at følge et princip efter bogstaven gav et dårligere design, og tag de beslutningsregistre med, hvis nogen, der forklarer, hvorfor en given grænse eller abstraktion findes. Aftal, at principper er standarder, en ingeniør kan afvige fra med en registreret begrundelse, og fang konsekvensrige designvalg i et kort arkitekturbeslutningsregister, så det næste team arver begrundelsen og ikke blot koden. I virksomheds- og offentlige systemer, hvor de oprindelige forfattere for længst er væk, og revisioner spørger, hvorfor systemet har den form, er det skriftlige spor forskellen mellem et design, fremtidige teams trygt kan ændre, og et de er bange for at røre.

## Sektorperspektiv

**Startup.** Foretræk det simpleste design, der kan leveres, og behold ét velfaktoriseret modul, til et reelt andet anvendelsestilfælde tvinger en søm frem. Din knappeste ressource er ingeniørernes opmærksomhed, så for tidlige grænseflader, lag og spekulative frameworks er ren omkostning. Følg reglen om tre, før du uddrager nogen fælles abstraktion, og lad YAGNI dræbe de udvidelsespunkter, ingen endnu har bedt om.

**Lille virksomhed.** Uden en dedikeret arkitekt og med et stramt budget så læn dig op ad det design, der allerede er bagt ind i de frameworks og biblioteker, du køber, frem for at opfinde dine egne mønstre. Forbehold skræddersyet designindsats til de få regler, der reelt er din forretning, og hold alt andet konventionelt, så en konsulent eller en nyansat kan læse det. Lidt duplikering, du forstår, slår en smart abstraktion, kun dens forfatter kan vedligeholde.

**Stor virksomhed.** Gevinsten ved fælles principper er koordinering på tværs af mange teams: et fælles ordforråd til designgennemgang og afgrænsede kontekster, der afstemmer modelgrænser med teamejerskab, så grupper udvikler sig uafhængigt. Styr kobling og sammenhængskraft eksplicit med afhængigheds- og samændringsdata, og registrér konsekvensrige designbeslutninger, så systemer forbliver ændringsdygtige længe efter, at deres forfattere er gået videre. Værn lige så meget mod den forkerte abstraktion, der kobler teams, som mod den overkonstruktion, der beskatter hver læser.

**Offentlig sektor.** Reviderbarhed og reproducerbarhed dikterer ofte designet. En uforanderlig, funktionel kerne lader dig reproducere en historisk beregning præcist for en given periode, hvilket en sammenfiltret objektgraf med skjult mutérbar tilstand ikke kan garantere. Foretræk eksplicitte offentliggjorte kontrakter frem for fælles tabeller ved kontekstgrænser, og hold designet og dets beslutningsregistre læselige for revisorer og for det team, der arver systemet et årti senere.

## Eksempler

**Startup.** Et startup med tre ingeniører, der bygger sit første produkt, modstår trangen til at opdele hver feature i lag af grænseflader og fabrikker og beholder ét velfaktoriseret modul, til et reelt andet anvendelsestilfælde dukker op. Da den samme logik optræder en tredje gang på tværs af tilmeldings- og faktureringsflowene, uddrager de en lille fælles funktion frem for et spekulativt framework. Det holder kodebasen lille nok til, at enhver af dem kan have den i hovedet, og de få sømme, de trækker, falder, hvor produktet med størst sandsynlighed ændres.

**Stor virksomhed.** En stor forsikringsplatform modellerer police, skader og fakturering som separate afgrænsede kontekster, hver ejet af et dedikeret team med sin egen datamodel og tjenestegrænse. Hvor kontekstene mødes, som når en skade refererer til en police, taler de gennem eksplicitte offentliggjorte kontrakter frem for fælles databasetabeller. Det lader de tre teams udvikle sig uafhængigt, og det allestedsnærværende sprog holder samtaler med forsikringsteknikere og aktuarer præcise. En tidligere version delte én vidtstrakt model, og hver ændring krævede koordinering på tværs af teams.

**Offentlig sektor.** Et nationalt skatteberegningssystem foretrækker bevidst en dataorienteret, funktionel kerne til sin beregningsmotor. Skatteregler udtrykkes som rene transformationer over uforanderlige inputposter, hvilket gør dem reviderbare, testbare og reproducerbare for et givet skatteår. De imperative, tilstandsfulde dele (workflow, notifikationer) holdes ved kanterne. Revisorer kan pege på en bestemt regelversion og reproducere enhver historisk beregning præcist, hvilket er et juridisk krav, som en sammenfiltret objektgraf med skjult mutérbar tilstand ikke kunne garantere.

## Business case: motivation, ROI og TCO

Designkvalitet er en investering i et systems *ændringsdygtighed*, og ændringsdygtighed dominerer de totale ejeromkostninger. Det meste af et systems omkostning falder efter dets første udgivelse, i modifikation og udvidelse. Veldesignede systemer holder omkostningen ved ændring nogenlunde flad over tid. Dårligt designede ser omkostningen ved hver ændring stige, til systemet reelt er umuligt at ændre og må omskrives, det dyreste udfald af alle.

Indførelsesomkostningen er hovedsageligt færdigheder og gennemgangsdisciplin: at undervise i principperne og bruge designtid på forhånd. Omkostningen ved ikke at indføre dem er den langsomme opbygning af [teknisk gæld](https://en.wikipedia.org/wiki/Technical_debt), faldende leveringshastighed, stigende fejlrater og til sidst dyre omskrivninger. For at argumentere over for ledelsen, forbind designdisciplin til leveringsforudsigelighed og til at undgå omskrivningsprogrammer, og følg ledende indikatorer som andel fejlslagne ændringer og tiden til at implementere sammenlignelige features over tid. Vær også opmærksom på den modsatte fejl: at overinvestere i design til usikre fremtider destruerer også værdi. Så argumentet er for *passende* design, kalibreret til hvor sandsynlig og hvor dyr fremtidig ændring er.

## Anti-mønstre og faldgruber

- **Spekulativ generalitet:** at bygge udvidelsesevne til forestillede krav, der aldrig kommer.
- **Den forkerte abstraktion:** at tvinge urelateret kode sammen for at tilfredsstille DRY, hvilket skaber kobling, der er værre end duplikering.
- **Mønster-cargo-kult:** at anvende designmønstre for deres egen skyld og tilføje indirektion uden gevinst.
- **Anæmiske eller gudeobjekter:** modeller uden adfærd, eller objekter der gør alt; begge signalerer fejlplacerede ansvarsområder.
- **Distribueret monolit:** tjenester opdelt fysisk, men stadig tæt koblede, hvilket kombinerer omkostningerne ved begge tilgange.
- **Big ball of mud:** ingen genkendelig struktur; hver ændring risikerer alt.
- **DDD-teater:** at adoptere ordforrådet og mappestrukturen uden den domænemodellering, der giver det værdi.

## Modenhedsmodel

- **Niveau 1, Opstart:** Design er ad hoc og reaktivt; kobling akkumuleres ukontrolleret; principper er ukendte eller påkaldes som slogans, og abstraktioner dukker op eller forsvinder efter individuel vane.
- **Niveau 2, Udvikling:** Teams kender principperne og anvender dem, men uens og ofte dogmatisk; nogle grupper styrer kobling og sammenhængskraft bevidst, mens andre ikke gør, og der er intet fælles ordforråd på tværs af organisationen.
- **Niveau 3, Standardisering:** Et fælles designordforråd, en regel om tre til at uddrage abstraktioner, analyse af kobling og sammenhængskraft og afgrænsede kontekster afstemt med teams er dokumenteret og forventet i hele organisationen, anvendt ensartet i designgennemgang frem for overladt til individuel smag.
- **Niveau 4, Styring:** Designets sundhed måles mod baselines: koblings- og samændringsdata, andel fejlslagne ændringer og tiden til at implementere sammenlignelige features følges over tid, så abstraktioner og grænser tilføjes, beholdes eller fjernes på dokumentation, og overkonstruktion og den forkerte abstraktion fanges af data frem for mening.
- **Niveau 5, Orkestrering:** Designdisciplin er integreret med leverings- og risikoplanlægning i hele organisationen; principper anvendes med nuancer og kendte fejlformer; paradigme- og grænsevalg er bevidste og løbende genbesøgt, og organisationen refaktorerer, genafgrænser og afvikler rutinemæssigt abstraktioner, efterhånden som domænet og dokumentationen skifter.

## Idéer til drøftelse

- Hvordan skelner du mellem en nødvendig søm og spekulativ generalitet, før du har det fremtidige krav?
- Hvornår har DRY ført jeres team til den forkerte abstraktion, og hvordan genkendte I det?
- Hvor bør grænserne for afgrænsede kontekster falde, og hvor tæt bør de spejle organisationsdiagrammet?
- Hvor meget design bør gå forud for kode i jeres sammenhæng, og hvordan registrerer I beslutningerne?
- Hvilke dele af jeres system ville have gavn af en mere funktionel eller dataorienteret stil?
- Hvordan forhindrer I designprincipper i at hærde til dogme, der modstår pragmatiske undtagelser?

## Vigtigste pointer

- Kobling og sammenhængskraft er de egenskaber, der betyder noget; akronymerne er midler til de mål.
- Hvert princip har en fejlform; vid, hvornår hver enkelt vildleder.
- Foretræk lidt duplikering frem for en for tidlig eller forkert abstraktion.
- Brug DDD og afgrænsede kontekster til at afstemme komplekse domæner med teamejerskab.
- Vælg paradigmer efter pasform; store systemer er pragmatisk blandede.
- Design til de ændringer, du faktisk får brug for, og undgå både under- og overdesign.

## Referencer og videre læsning

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
