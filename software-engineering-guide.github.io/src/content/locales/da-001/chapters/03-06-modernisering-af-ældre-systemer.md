# 3.6 Modernisering af ældre systemer

## Overblik og motivation

[Ældre systemer (legacy)](https://en.wikipedia.org/wiki/Legacy_system) er de systemer, der driver verden. De centrale bankhovedbøger, skatte- og ydelsesmotorer, flytrafik- og forsvarssystemer, forsikringspolicestyring og offentlige registre, samfund afhænger af, er hyppigt årtier gamle. Mange er skrevet i [COBOL](https://en.wikipedia.org/wiki/COBOL) (Common Business-Oriented Language) eller andre ældre teknologier, og de behandler stadig størstedelen af de kritiske transaktioner. "Legacy" er ikke en fornærmelse. Det betyder, at systemet er værdifuldt nok til at have overlevet, kritisk nok til at et svigt er katastrofalt, og gammelt nok til at det er svært at ændre sikkert. Modernisering af ældre systemer er disciplinen at forbedre, migrere eller erstatte disse systemer uden at bryde de essentielle tjenester, de leverer.

Dette er uforholdsmæssigt meget et virksomheds- og offentligt problem, og det er der, de største og mest offentlige it-fiaskoer sker. En enorm andel af større transaktioner verden over rører stadig [mainframe](https://en.wikipedia.org/wiki/Mainframe_computer)-systemer. En stor del af produktionskoden i store institutioner er i ældre sprog vedligeholdt af en aldrende, skrumpende pulje af specialister. Det offentlige bærer den tungeste byrde: lovbestemte forpligtelser kodet gennem årtier, indkøbs- og budgetcyklusser, der overlever administrationer, og borgerservices, der ikke kan afbrydes. Den dominerende risiko er ikke, at disse systemer er gamle, da mange kører fremragende. Det er, at viden til at vedligeholde dem er på vej på pension, platformene bliver stadig dyrere og mere begrænsede, og fristelsen til at "bare omskrive det" fører til nogle af de dyreste fiaskoer i feltets historie.

Dette kapitel dækker de inkrementelle moderniseringsmønstre, der faktisk virker (strangler fig og branch-by-abstraction), hvordan man vurderer og prioriterer legacy-risiko, forvaltningen af mainframe- og COBOL-landskaber, disciplinen [datamigrering](https://en.wikipedia.org/wiki/Data_migration) og dobbeltkørsel, og frem for alt hvordan man modstår fristelsen til den store omskrivning. Den centrale overbevisning er, at vellykket modernisering næsten altid er inkrementel, dokumentationsdrevet og løbende leverer værdi. Den er aldrig et flerårigt big bang.

## Grundprincipper

- **Legacy betyder værdifuldt og fundamentalt, ikke blot gammelt.** Respektér, hvad systemet gør, før du rører det; det koder årtiers hårdt tilkæmpede forretningsregler.
- **Inkrementelt slår big-bang, næsten altid.** Erstat stykke for stykke bag en stabil grænseflade; lever værdi løbende og hold risikoen lille.
- **Den store omskrivning er standardfejlformen.** Fulde omskrivninger overskrider rutinemæssigt, underleverer og aflyses; behandl trangen med dyb mistænksomhed.
- **Du kan ikke modernisere det, du ikke forstår.** [Reverse-engineer](https://en.wikipedia.org/wiki/Reverse_engineering) og dokumentér adfærd (herunder udokumenterede regler), før du erstatter den.
- **Datamigrering er, hvor projekter dør.** Dataene er ældre, snavsede og mere sammenfiltrede, end nogen forventer; planlæg for det som en førsteklasses indsats.
- **Kør gammelt og nyt parallelt for at opbygge tillid.** Dobbeltkørsel og sammenligning fanger uoverensstemmelser før omstilling.
- **Prioritér efter risiko og værdi, ikke efter alder.** Moderniser det mest risikable og værdifulde først, ikke det, der blot er ældst.
- **Hold lyset tændt, mens du skifter motoren.** Tjenesten skal blive ved med at køre hele vejen; der er ingen acceptabel nedetid for kritiske borger- eller finansielle systemer.

## Anbefalinger

### Moderniser inkrementelt med strangler fig-mønstret

**Strangler fig** (opkaldt efter vinstokken, der vokser rundt om et træ og gradvist erstatter det) er arbejdshesten i sikker modernisering. Placér et routinglag (en API-gateway, facade eller proxy) foran legacy-systemet. Byg derefter, kapacitet for kapacitet, erstatningen i et moderne system og omdirigér den skive af trafik til det, mens resten bliver på legacy-systemet. Over tid vokser det nye system, og det gamle skrumper, til det kan pensioneres. Det leverer værdi løbende, holder hver ændring lille og reversibel, undgår en risikabel omstilling og lader dig standse eller omprioritere på ethvert tidspunkt. Det er det modsatte af big bang. Legacy-systemet bliver ved med at køre og tjene sit brød, mens du erstatter det rundt om det.

### Brug branch-by-abstraction til interne sømme

Hvor du skal erstatte en komponent, mange dele af systemet afhænger af, så brug **branch-by-abstraction**. Indfør et abstraktionslag (en grænseflade) over den eksisterende implementering, migrér kaldere til at afhænge af abstraktionen, byg den nye implementering bag den samme abstraktion, skift over (ofte bag et [feature flag](https://en.wikipedia.org/wiki/Feature_toggle), gradvist), og fjern til sidst den gamle implementering. Det lader en stor komponent blive erstattet inkrementelt på udviklingens hovedlinje uden en langlivet gren og holder systemet udgivelsesklart hele vejen. Det parrer sig naturligt med strangler fig: facaden håndterer eksterne sømme, branch-by-abstraction håndterer interne.

### Vurdér og prioritér legacy-risiko bevidst

Før du moderniserer, så byg en klarsynet opgørelse og risikovurdering af landskabet. For hvert system så score det på forretningskritikalitet, teknisk risiko (forældelse, ikke-understøttede platforme, sikkerhedseksponering), ændringsfrekvens og, afgørende, **videnrisiko** (hvor mange der stadig kan vedligeholde det, og hvor tæt de er på pension). Afbild systemer på et risiko-versus-værdi-gitter. Prioritér at modernisere det, der både er højrisiko og højværdi. Overvej at lade stabile, lavfrekvente, velforståede systemer være i fred, selv om de er gamle, fordi et fungerende system, ingen har brug for at ændre, ikke er en nødsituation. Denne vurdering forvandler "alt er gammelt og skræmmende" til en forsvarlig, sekventeret køreplan.

### Forvalt mainframe- og COBOL-landskabet, erstat det ikke blot

Ikke hvert mainframe- eller COBOL-system bør, eller kan sikkert, erstattes snart. Den kortsigtede prioritet er ofte **forvaltning**: fang viden, før den går på pension. Dokumentér de forretningsregler, koden koder (meget af det udokumenteret og uerstatteligt), invester i automatiserede tests, der fastnagler den nuværende adfærd, så fremtidig ændring er sikker, rekruttér og krydsuddan vedligeholdere, og modernisér de omgivende leveringspraksisser (kildekodestyring, [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), automatiseret test), selv mens kernen bliver på plads. Hvor du moderniserer, så foretræk at eksponere legacy-evner gennem moderne API'er (indkapsling) som et første skridt. Behandl automatiseret oversættelse fra COBOL til moderne sprog med forsigtighed, fordi den producerer kode, der kører, men ofte trofast gengiver uforståelig logik. Den knappeste ressource er forståelse, ikke beregning.

### Behandl datamigrering og dobbeltkørsel som projektets kerne

Den sværeste og mest risikable del af de fleste moderniseringsindsatser er **dataene**. De er voluminøse, af dårlig og inkonsistent kvalitet og fulde af udokumenteret mening akkumuleret gennem årtier. Profilér og rens dem, afbild gamle til nye skemaer eksplicit, og byg gentagelig, automatiseret migrering med fuld afstemning (antal, tjeksummer, forretningstotaler), så du kan bevise, at intet gik tabt eller blev ændret. Afrisikér omstilling med **dobbeltkørsel** (parallelkørsel): driv det gamle og det nye system side om side på de samme input og sammenlign output, til det nye system matcher det gamle til din tillidstærskel. Først da skift over, og behold evnen til at rulle tilbage. For virkelig kritiske systemer så migrér og skift over i skiver frem for alt på én gang.

### Styr fristelsen til den store omskrivning

Instinktet til at smide det rodede gamle system væk og bygge et rent nyt fra bunden er stærkt, og det er næsten altid forkert for store, kritiske systemer. Fulde omskrivninger undervurderer den værdi, der er skjult i den "grimme" kode (kanttilfælde, regulatoriske regler, fejlkompatibel adfærd, reelle brugere afhænger af), tager langt længere end projekteret, leverer ingen værdi før til sidst og aflyses hyppigt efter enorme udgifter. Vælg inkrementel modernisering som standard. Forbehold omskrivninger til tilfælde, hvor platformen reelt er uholdbar, og inkrementelle veje er udtømt. Selv da så dekomponér omskrivningen i uafhængigt leverbare stykker via strangler-mønstret frem for en enkelt big-bang-udgivelse. Når ledelsen presser på for en total omskrivning, så insistér på spørgsmålet: hvilken værdi leveres de første tre måneder, og hvad sker der, hvis programmet stoppes halvvejs?

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Strangler fig (inkrementel) | Løbende værdi, lav risiko, reversibel, holder tjenesten kørende | Længere samlet tidslinje, skal køre to systemer parallelt, integrationsoverhead |
| Big-bang-omskrivning | Blankt ark, ingen legacy-begrænsninger i den nye kode | Meget høj fejlrate, ingen værdi før til sidst, enorm omkostning, forretningsregler tabt |
| Indkapsl (omslut med API'er) | Hurtig, lav risiko, moderniserer adgang uden at røre kernen | Kernen forbliver legacy; udskyder, løser ikke, den underliggende risiko |
| Lad være som det er (forvalt) | Ingen projektrisiko; billigst på kort sigt | Videns- og platformsrisiko bliver ved med at akkumulere; til sidst tvungen handling |

Den grundlæggende afvejning er transformationshastighed versus risiko for fejl, og modernisering af ældre systemer er det domæne, hvor den handel er mest skæv. Den "hurtige, rene" big-bang-omskrivning er en luftspejling, der gentagne gange producerer det langsomste og dyreste udfald af alle: et aflyst program og et stadig ikke-moderniseret system. Inkrementelle tilgange føles langsommere og kræver at køre to systemer parallelt, men de leverer værdi hele vejen, holder risikoen lille og reversibel og er den empirisk pålidelige vej. Det ægte dømmekraftsspørgsmål er mellem at forvalte et stabilt legacy-system lidt længere og at begynde inkrementel erstatning nu. Lad risikotrajektorien drive det kald, især videnrisiko, frem for ubehag ved gammel teknologi.

## Spørgsmål til drøftelse med dit team

1. **Har I et sted at placere et routinglag foran jeres legacy-system, og hvis ikke, hvad ville der skulle til for at skabe et?** Strangler fig afhænger af en søm: en API-gateway, facade eller proxy, hvorigennem I kan omdirigere én kapacitet ad gangen til en ny implementering. Mange gamle systemer har ingen sådan søm, så det første moderniseringstrin er ofte blot at bygge opfangningspunktet, og det arbejde er let at undervurdere. Tag den aktuelle integrationsoversigt med og spørg, hvor trafik kunne opfanges pr. kapacitet uden en big-bang-omstilling. Hvis der intet sted er, kan branch-by-abstraction på en intern søm være startskuddet i stedet. Uden et routinglag har I ingen inkrementel vej, hvilket netop er, hvordan organisationer skubbes tilbage mod den omskrivning, der som regel fejler.

2. **Har I faktisk afbildet jeres landskab på et risiko-versus-værdi-gitter, eller drives jeres køreplan af, hvilket system der føles ældst?** Kapitlet insisterer på, at I moderniserer det, der er højrisiko og højværdi, først, og bevidst lader stabile, lavfrekvente, velforståede systemer være i fred, selv når de er ældgamle. Uden et eksplicit gitter flyder opmærksomheden til den højeste klage eller den mindst moderne teknologi, og ægte tidsindstillede bomber (et kritisk system med to vedligeholdere nær pension) venter. Score hvert system på forretningskritikalitet, teknisk risiko, ændringsfrekvens og videnrisiko, og sekventér derefter fra øverste højre hjørne. Tag det gitter med til mødet som det fælles kort. Videnrisiko fortjener den tungeste vægt, fordi det er det ene input, der kun bliver værre og ikke kan købes tilbage, når folk først er gået.

3. **Når I skifter over, hvordan beviser I så, at ikke en eneste post gik tabt eller blev ændret, og hvem godkender den dokumentation?** Datamigrering er, hvor disse projekter dør, og tillid kommer fra afstemning: rækkeantal, tjeksummer og forretningskontroltotaler, der matcher mellem gammelt og nyt, plus dobbeltkørsel, der sammenligner output på de samme input, til de er enige til en høj tærskel. For et ydelses- eller hovedbogssystem er en uoverensstemmelse en borger underbetalt eller en øre tabt, så dokumentationen må tilfredsstille en revisor, ikke blot en ingeniør. Beslut nu, hvilke totaler I vil afstemme, hvilken tillidstærskel der udløser omstilling, og hvor længe I vil køre gammelt og nyt parallelt. Hold tilbagerulning tilgængelig hele vejen, og skift over i skiver frem for alt på én gang. De uoverensstemmelser, I finder under dobbeltkørsel, er som regel udokumenterede legacy-regler, I må bevare, så behandl hver som en opdagelse, ikke blot en fejl.

4. **Hvilke af jeres legacy-systemer forvalter I versus erstatter aktivt, og hvem besluttede, hvilket der er hvilket?** Kapitlet trækker en bevidst linje mellem systemer, der er værd at stabilisere på stedet (dokumentere regler, tilføje karakteriseringstests, krydsuddanne vedligeholdere), og systemer, der er værd at erstatte inkrementelt, og de to kræver meget forskellig finansiering og bemanding. For en stor organisation er faren drift: et system mærket "forvalt for nu" bliver stille "forvalt for evigt", til den sidste vedligeholder går på pension, og valget træffes for jer under krise. De modstridende hensyn er forvaltningsomkostning og platformsforældelse på den ene side mod risikoen og forstyrrelsen ved erstatning på den anden, og videnrisiko bør tippe balancen, fordi den kun forværres. Tag risiko-versus-værdi-gitteret med, vedligeholderantal og pensionshorisont for hvert system og en eksplicit ejer af forvalt-eller-erstat-beslutningen. I virksomheds- og offentlige landskaber så navngiv en gennemgangskadence og en ansvarlig embedsmand for hvert system, fordi en klassifikation, ingen genbesøger, er en beslutning, ingen træffer.

5. **Når ledelsen beder om en fuld omskrivning, hvad er jeres faste svar, og kan I vise, hvad en inkrementel vej leverer de første tre måneder?** Big-bang-omskrivningen er standardfejlformen, men den bliver ved med at blive finansieret, fordi et blankt ark er let at sælge og en strangler fig ikke er. Et stort team har brug for et indøvet svar, så argumentet vindes på dokumentation frem for på, hvem der er mest senior i rummet. Spændingen er ægte: nogle platforme er reelt uholdbare, og en omskrivning er berettiget, så svaret kan ikke være en generel afvisning: det må veje, om inkrementelle sømme stadig findes, mod den sande omkostning ved at holde den gamle platform i live. Tag den værdi med, et første inkrementelt skridt ville levere, den historiske fejlrate for sammenlignelige omskrivninger og en dekomponering af enhver foreslået omskrivning i uafhængigt leverbare stykker. I det offentlige, hvor et aflyst flerårigt program brænder offentlige penge af i fuld offentlighed, så insistér på, at enhver omskrivning leverer værdi tidligt og overlever at blive stoppet halvvejs uden totalt tab.

6. **Hvordan fanger I de forretningsregler, der er låst i jeres ældste kode, før de mennesker, der forstår dem, er væk?** Meget af værdien i et legacy-system er udokumenteret adfærd, som årtiers kanttilfælde, reguleringer og fejlkompatible rettelser har akkumuleret, og den bor i en skrumpende pulje af pensionerende specialister frem for i nogen skreven optegnelse. For en stor organisation er dette den ene risiko, der ikke kan købes tilbage, når folk først er gået, så den fortjener finansiering forud for det mere synlige platformsarbejde. Det modstridende træk er, at vidensfangst (dokumentation, karakteriseringstests, reverse engineering, krydsuddannelse) føles som overhead, der ikke leverer noget, hvilket netop er grunden til, at den udskydes. Tag en opgørelse med over, hvem der holder kritisk viden, hvor tæt de er på at forlade jer, og hvilken testdækning der fastnagler nuværende adfærd i dag. I regulerede og offentlige sammenhænge så behandl de lovbestemte regler kodet i gammel kode som et compliance-aktiv: at miste dem stille er ikke en teknisk gæld, det er en juridisk eksponering.

## Sektorperspektiv

**Startup.** Dit legacy er din egen hastigt skrevne MVP, ikke en mainframe: en prototype, der nu bærer omsætning, og som alle er bange for at røre. Omskriv den ikke. Omslut det mest skræmmende modul bag en ren grænseflade, tilføj karakteriseringstests for at fastnagle dets adfærd, og udskær funktionalitet inkrementelt, så hver lille udgivelse leverer værdi og skrumper risikoen. Du har ingen runway til en genopbygning fra bunden, så optionalitet betyder mere end elegance.

**Lille virksomhed.** Du har intet moderniseringsteam og et stramt budget, så det praktiske træk er som regel at holde et fungerende system fungerende: fang, hvad den ene person, der forstår det, ved, få det i kildekodestyring med nogle få automatiske tests, og støt dig til en leverandør eller et pakket produkt frem for en skræddersyet genopbygning. Ram beslutningen ind som køb versus byg, og foretræk at købe, når kapaciteten er en standardvare. Brug din begrænsede indsats på det ene system, hvis svigt ville standse virksomheden, ikke på det, der blot ser ældst ud.

**Stor virksomhed.** Problemet er porteføljeskala: dusinvis af systemer, mange teams og videnrisiko på tværs af landskabet. Kør en fælles risiko-versus-værdi-vurdering, standardisér på inkrementelle mønstre (strangler fig og branch-by-abstraction), og behandl datamigrering og dobbeltkørsel som førsteklasses discipliner med afstemning, alle stoler på. Styr modernisering som en løbende portefølje mod risikotrajektorie frem for en spredning af heroiske projekter, og budgettér forvaltning og vidensfangst eksplicit, så intet kritisk system afhænger af en enkelt pensionerende vedligeholder.

**Offentlig sektor.** Lovbestemte forpligtelser kodet gennem årtier, indkøbsregler og borgerservices, der ikke kan afbrydes, gør big-bang-erstatning særligt farlig. Foretræk inkrementel strangler fig-migrering med omstilling skive for skive, bevis gennem afstemning og lang parallelkørsel at ikke en eneste borgerpost gik tabt eller blev fejlberegnet, og hold tilbagerulning tilgængelig hele vejen. Indkøb bør kræve dataportabilitet og offentliggørelse af forretningsregler frem for uigennemsigtig oversættelse, og ethvert flerårigt program skal levere reviderbar værdi tidligt og overleve offentlig granskning, hvis det stoppes undervejs.

## Eksempler

**Startup.** Et tre år gammelt startups oprindelige MVP er blevet sin egen slags legacy: en hastigt skrevet prototype, der nu håndterer reel omsætning, og som alle er bange for at røre. I stedet for en omskrivning omslutter teamet det værste modul bag en ren grænseflade, tilføjer karakteriseringstests for at fastnagle dets nuværende adfærd og flytter funktionalitet ud af det stykke for stykke over nogle måneder. Hver lille udgivelse leverer værdi og skrumper den skræmmende del, så startuppet får et vedligeholdeligt system uden at satse virksomheden på en genopbygning fra bunden, det ikke har råd til.

**Stor virksomhed.** Et stort forsikringsselskab kører policeadministration på et mainframe COBOL-system, der er pålideligt, men dyrt at ændre og vedligeholdt af en håndfuld ingeniører tæt på pension. I stedet for en omskrivning omslutter selskabet mainframen med moderne API'er og anvender strangler fig: nye tilbuds-og-køb- og selvbetjeningsevner bygges på en moderne platform og dirigeres gennem en facade, mens kernepolicerne bliver på mainframen. Parallelt dokumenterer teamet forretningsreglerne og tilføjer [karakteriseringstests](https://en.wikipedia.org/wiki/Characterization_test) omkring COBOL'en. Over flere år flytter kapacitet efter kapacitet af mainframen, hver udgivelse leverer værdi, til den resterende kerne kan pensioneres på selskabets egne vilkår frem for under krise.

**Offentlig sektor.** En social sikringsmyndighed skal modernisere et årtier gammelt ydelsesberegningssystem, der betaler millioner af borgere og ikke kan afbrydes eller betale forkert. Den afviser en big-bang-erstatning efter at have studeret sammenlignelige fejlslagne programmer. I stedet profilerer og renser den dataene, bygger automatiseret migrering med fuld afstemning mod kontroltotaler og kører den nye ydelsesmotor parallelt med den gamle i mange måneder, fodrer begge med de samme krav og sammenligner hver beregning, og undersøger hver uoverensstemmelse (der ofte afslører udokumenterede legacy-regler, som må bevares). Først når det nye system matcher det gamle til en meget høj tillid, skifter den over ydelsestype for ydelsestype og bevarer tilbagerulning hele vejen. Strangler-facaden lader borgere se én sammenhængende tjeneste gennem overgangen.

## Business case: motivation, ROI og TCO

Modernisering af ældre systemer har en usædvanlig business case, fordi den største omkostning ofte er omkostningen ved *passivitet*, og den største risiko er selve moderniseringsprojektet. De voksende omkostninger ved ikke at modernisere er konkrete: stigende vedligeholdelse og licensering på forældede platforme, en stadig knappere og dyrere specialistarbejdsstyrke, manglende evne til hurtigt at møde nye regulatoriske eller servicekrav og voksende eksponering for et katastrofalt svigt, uden at nogen er tilbage, der forstår systemet. Over for det er omkostningen ved modernisering høj, og udført som et big bang bærer den en reelt høj sandsynlighed for fiasko. Det er netop derfor, den inkrementelle tilgang betyder noget for ROI: den omsætter ét stort væddemål til en række små, der hver returnerer værdi og kan stoppes.

Argumentér over for ledelsen ved at omramme valget. Spørgsmålet er ikke "modernisere eller ej." Det er "modernisere inkrementelt nu, eller betale eskalerende forvaltningsomkostninger og stå over for en tvungen, højere-risiko modernisering senere under krise." Kvantificér status quo's TCO (platforms- og licensomkostninger, præmien for knappe færdigheder, den risikovægtede omkostning ved et uopretteligt nedbrud) og sammenlign den med et trinvist program, der reducerer risiko og omkostning med hvert trin, mens tjenesten holdes kørende. Afgørende, insistér på at ethvert foreslået omskrivningsprogram struktureres til at levere værdi tidligt og ofte. Et program, der ikke leverer noget i tre år og kan aflyses med totalt tab, er ikke en investering; det er et gamble. Det stærkeste ROI-argument for strangler-tilgangen er optionalitet: værdi leveres løbende, og organisationen kan justere kursen på ethvert tidspunkt.

## Anti-mønstre og faldgruber

- **Den store omskrivning.** Flerårig, alt-eller-intet-erstatning, der ikke leverer værdi før til sidst og hyppigt aflyses til stor omkostning.
- **Omskrivning uden forståelse.** At erstatte kode, hvis forretningsregler aldrig blev dokumenteret, og stille droppe kanttilfælde, reelle brugere og love afhænger af.
- **At undervurdere dataene.** At behandle datamigrering som en eftertanke, når det er projektets sværeste og mest risikable del.
- **At springe dobbeltkørsel over.** At skifte til det nye system uden parallel sammenligning og opdage uoverensstemmelser først efter de rammer rigtige mennesker.
- **Automatiseret oversættelse som løsning.** At maskinoversætte COBOL til et moderne sprog og tro, at jobbet er gjort, hvilket producerer uforståelig kode, der gengiver den gamle logik ordret.
- **Modernisering efter alder, ikke risiko.** At bruge indsats på gamle, men stabile systemer, mens højrisiko-, højfrekvente systemer venter.
- **At miste viden.** At lade de sidste vedligeholdere gå på pension uden at fange forretningsreglerne og tilføje karakteriseringstests.
- **Ingen tilbagerulning.** At skifte over uden vej tilbage, når det nye system opfører sig forkert under reel belastning og reelle data.

## Modenhedsmodel

- **Niveau 1: Opstart.** Legacy-systemer frygtes og fryses; ændring undgås. Ingen opgørelse eller risikovurdering findes. Modernisering, når den overhovedet forsøges, er en ad hoc alt-eller-intet-omskrivning drevet af frustration. Viden bor i nogle få pensionerende hoveder, intet skrevet ned.
- **Niveau 2: Udvikling.** Nogle teams har en opgørelse og en grov fornemmelse af risiko, og nogle få legacy-systemer er omsluttet med API'er til adgang. Inkrementelle mønstre er kendt, men anvendes uens, og tænkningen driver stadig mod big-bang-omskrivninger. Datamigrering forsøges, men undervurderes, og praksis varierer vidt fra team til team.
- **Niveau 3: Standardisering.** Systemer prioriteres efter risiko og værdi efter en dokumenteret metode for hele organisationen. Inkrementelle mønstre (strangler fig, branch-by-abstraction) er den håndhævede standard, og hver modernisering følger en standardhåndbog. Datamigrering er en planlagt, afstemt indsats med dobbeltkørsel før omstilling, og vidensfangst og karakteriseringstests er påkrævet praksis frem for valgfri.
- **Niveau 4: Styring.** Modernisering måles og styres med data. Landskabet bærer baselines: vedligeholderantal og pensionshorisont pr. system, dækning af karakteriseringstests, bestå-rater for migreringsafstemning, antal uoverensstemmelser i dobbeltkørsel og leveret værdi pr. trin, alt sammen fulgt mod mål. Forvalt-eller-erstat-beslutninger og go/no-go-kald for omstilling træffes på denne dokumentation, og et system, der driver forbi sin videnrisikotærskel, udløser handling frem for at vente på en krise.
- **Niveau 5: Orkestrering.** Modernisering er løbende, integreret med forretnings- og risikoplanlægning og adaptiv. Porteføljen genbalanceres mod risikotrajektorie (især videnrisiko), når den skifter, inkrementel erstatning er rutine og lavdramatisk, hvert trin leverer værdi og er reversibelt, og organisationen styrer tempoet bevidst. Lektioner fra hver migrering føder tilbage i den fælles håndbog, så hele landskabet forbedres over tid.

## Idéer til drøftelse

1. For jeres mest kritiske legacy-system, hvor mange mennesker kan stadig vedligeholde det, og hvor tæt er de på at forlade jer?
2. Hvor fristes I af en big-bang-omskrivning, og hvilken værdi kunne en inkrementel tilgang levere de første tre måneder i stedet?
3. Hvor godt er forretningsreglerne i jeres ældste systemer dokumenteret, og hvad sker der med dem, hvis koden erstattes?
4. Har I profileret de data, I ville skulle migrere, og ved I, hvor snavsede og sammenfiltrede de reelt er?
5. Hvilke gamle-men-stabile systemer bruger I moderniseringsenergi på, som I sikkert kunne lade være i fred?
6. Kunne I køre jeres nye system parallelt med det gamle og bevise, at de er enige, før I skifter over?

## Vigtigste pointer

- Legacy betyder værdifuldt og fundamentalt; respektér og forstå et system, før du ændrer det.
- Moderniser inkrementelt med strangler fig og branch-by-abstraction, lever værdi løbende og hold hver ændring lille og reversibel.
- Behandl den store omskrivning som standardfejlformen; forbehold den til reelt uholdbare platforme, og dekomponér den selv da.
- Prioritér efter risiko og værdi (især videnrisiko), ikke efter alder; nogle gamle systemer forvaltes bedst, ikke erstattes.
- Datamigrering og dobbeltkørsel er indsatsens hjerte; profilér, afstem, kør parallelt og behold tilbagerulning.
- Den stærkeste business case er optionalitet: inkrementel modernisering omsætter ét stort, risikabelt væddemål til mange små, værdireturnerende.

## Referencer og videre læsning

- Michael Feathers, *Working Effectively with Legacy Code*
- Martin Fowler, "StranglerFigApplication" and "BranchByAbstraction"
- Sam Newman, *Monolith to Microservices*
- Nicholas Carr / industry studies on mainframe and COBOL dependency (context on the scale of legacy estates)
- Robert Annett, *Working with Legacy Systems*
- Eric Evans, *Domain-Driven Design* (anti-corruption layer)
- Gregor Hohpe, *Enterprise Integration Patterns* and *The Software Architect Elevator*
- Standish Group *CHAOS Report* (evidence on large project and rewrite failure rates)
