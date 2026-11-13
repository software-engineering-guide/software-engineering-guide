# 10.4 Vedligeholdelse af store og langlivede systemer

## Overblik og motivation

Det meste skriveri om softwareudvikling handler om at bygge nye ting. Men det meste af verdens vigtige software er gammelt, stort og stadig i drift: skattesystemer, ydelsesudbetalinger, flyvekontrol, kernebankvirksomhed, industriel styring og infrastrukturen i dagligdagen. Disse systemer kører rutinemæssigt i ti, tyve eller tredive år. Det er langt længere end ansættelsestiden for nogen af dem, der byggede dem, og ofte længere end de virksomheder og sprog, der frembragte dem. At vedligeholde sådanne systemer betyder at holde dem pålidelige, sikre, forståede og i stand til at ændre sig, på tværs af årtier og generationer af medarbejdere. Det er en af de sværeste og mindst glamourøse discipliner i faget, og en hvor store virksomheder og regeringer bærer den tungeste byrde.

Hvorfor betyder det mere for store organisationer? Forpligtelsens kontinuitet. Et startup kan omskrive eller opgive sin software. En national regering kan ikke holde op med at udbetale pensioner, mens den refaktorerer. Virksomheder og agenturer ejer systemer, hvis svigt har konsekvenser målt i levebrød, sikkerhed eller offentlig tillid. Og de ejer mange af dem på én gang, bemandet af folk, der kommer og går over årtier. De centrale trusler er ikke eksotiske. De er den langsomme erosion af de mennesker, der forstår systemet ([bus-faktor](https://en.wikipedia.org/wiki/Bus_factor), hvor få mennesker der skal forlade, før viden om et system går tabt), ophobningen af udokumenteret viden i nogle få hoveder, teknologistakkens forfald mod [end of life](https://en.wikipedia.org/wiki/End-of-life_(product)) og den lammelse, der sætter ind, når et system bliver for kritisk at røre og for dårligt forstået til at ændre sikkert.

Dette kapitel handler om forvaltning: det bevidste, uglamourøse arbejde at hjælpe et system med at overleve sine forfattere elegant. Det dækker ejerskabskontinuitet og bus-faktor-afbødning, planlagt [udfasning](https://en.wikipedia.org/wiki/Deprecation) og nedlukning, videnoverdragelse, de særlige udfordringer ved årtier lange systemer og den konstante balancegang mellem at innovere og at bevare den stabilitet, borgere og kunder afhænger af.

## Grundprincipper

- **Hvert kritisk system har altid brug for en ejer.** Ejerskab er en løbende tildeling, ikke en erindring om, hvem der skrev det.
- **Viden, der bor i ét hoved, er en risiko, ikke et aktiv.** Institutionalisér forståelse, før personen forlader jer.
- **Kedeligt er en funktion.** For langlivede kritiske systemer slår stabilitet og forudsigelighed ofte nyhed.
- **Planlæg afslutningen i begyndelsen.** Hvert system bliver pensioneret eller erstattet; design og dokumentér til den dag.
- **Forandring er, hvordan I forbliver sikre.** Et system, der er for skræmmende at røre, fejler allerede; evnen til at ændre er en overlevelsesegenskab.
- **Kontinuitet overlever enkeltpersoner.** Design teams, dokumentation og processer, så ingen enkelt afgang er en krise.
- **Tillid er det reelle produkt.** For borger- og kundevendte systemer er pålidelighed og retfærdighed vedligeholdt over tid missionen.

## Anbefalinger

### Etablér forvaltning og ejerskabskontinuitet

Tildel eksplicit, aktuelt ejerskab til hvert system, der betyder noget. Eje på teamniveau, ikke individniveau, så ejerskab overlever afgange. Vedligehold et [servicekatalog](https://en.wikipedia.org/wiki/Service_catalog), der for hvert system registrerer, hvem der ejer det, hvad det gør, hvad det afhænger af, og hvor kritisk det er. Gennemgå ejerskab regelmæssigt, og lad aldrig et system blive forældreløst. Et ejerløst kritisk system er en nødsituation, der venter på at ske. Når teams omorganiserer, så overfør ejerskab bevidst, med en overdragelse, ikke ved antagelse. For de mest kritiske langlivede systemer så sørg for, at ejerskab ikke kun inkluderer drift, men evnen til at forstå og ændre systemet, så forvaltning ikke forfalder til blot barnepigearbejde.

### Afbød bus-faktor og nøgleperson-risiko

Mål og reducér aktivt koncentrationen af viden. Hvis kun én person kan udrulle, fejlfinde eller ændre et system, er det et [enkeltstående fejlpunkt](https://en.wikipedia.org/wiki/Single_point_of_failure) lige så reelt som enhver hardware. Reducér det gennem parprogrammering og rotation, obligatorisk kodegennemgang, delt vagtberedskab og en bevidst regel om, at ingen kritisk opgave har præcis én kompetent person. Krydsuddan, så mindst to (helst tre) personer kan udføre hver væsentlig funktion. Behandl en nøglepersons afgang som en forudsigelig begivenhed, I forbereder jer på kontinuerligt, ikke et chok, I absorberer. Dokumentation hjælper. Men arbejdsviden spredt over et team gennem faktisk praksis er langt mere varig end dokumenter, ingen har udøvet.

### Institutionalisér videnoverdragelse

Indfang den viden, der ellers ville forlade jer sammen med folk. Fokusér først på den viden, der er svær at rekonstruere: hvorfor beslutninger blev truffet, hvilke alternativer der blev afvist og hvorfor, hvor de skarpe kanter og de kritiske hacks er, som resten af systemet stille afhænger af, og hvordan systemet opfører sig under belastning. Brug arkitekturbeslutningsregistre til at bevare ræsonnementet bag valg, ikke kun valgene. Hold [runbooks](https://en.wikipedia.org/wiki/Runbook) og driftsdokumentation tæt på systemet, og udøv dem regelmæssigt, så de forbliver sande. Byg onboardingstier, der får nye forvaltere til reel kompetence. Behandl afgange som videnoverdragelsesbegivenheder med reel overdragelsestid. Husk, at [tavs viden](https://en.wikipedia.org/wiki/Tacit_knowledge), fornemmelsen for et system, overføres hovedsageligt ved at gøre noget sammen med en, der har den, så lad afgående og ankommende forvaltere overlappe, hvor I kan.

### Styr udfasning, nedlukning og end-of-life

Planlæg afslutninger bevidst. Når I beslutter at pensionere eller erstatte et system, så behandl nedlukningen som et projekt i sig selv: identificér hver forbruger og afhængighed, giv en migreringssti og en realistisk tidslinje, kommunikér klart og gentagne gange, og støt forbrugere gennem overgangen. Undgå fælden at køre det gamle og nye system parallelt for evigt, fordi ingen vil gøre det hårde arbejde med at slukke det gamle. Tildel eksplicit ansvarlighed for at fuldføre nedtagningen. Bevar data, optegnelser og evnen til at besvare spørgsmål om det pensionerede system længe efter, det holder op med at køre, især hvor lovpligtige opbevaringsregler gælder. En nedlukning udført dårligt efterlader zombiesystemer, der er uvedligeholdte, men stadig afhængige: det værste af alle verdener.

### Vedligehold systemer gennem årtier

For systemer, der skal køre i tyve eller tredive år, så planlæg at overleve alt: det oprindelige team, leverandørerne, sprogøkosystemet og hardwaren. Foretræk [åbne standarder](https://en.wikipedia.org/wiki/Open_standard) og dokumenterede grænseflader frem for proprietære sorte bokse, så fremtidige vedligeholdere har en chance. Modularisér, så dele kan erstattes én ad gangen frem for gennem en alt-eller-intet-[omskrivning](https://en.wikipedia.org/wiki/Rewrite_(programming)), der er for risikabel at forsøge. Hold systemet kontinuerligt vedligeholdt. Et system holdt aktuelt i små skridt forbliver bæredygtigt. Et system frosset "fordi det virker" bliver stille uvedligeholdeligt, efterhånden som dets stak ældes ud af support. Hold også færdighederne til at drive det: for reelt gammel teknologi så træn bevidst efterfølgere frem for at håbe, at den sidste ekspert aldrig går på pension.

### Afbalancér innovation med stabilitet og tillid

Skeln mellem de dele af jeres ejendom, hvor nyhed skaber værdi, og de dele, hvor stabilitet er værdien. Kernesystemer, borgere og kunder afhænger af dagligt, belønner som regel pålidelighed, bagudkompatibilitet og forsigtig ændring frem for spændende omskrivninger. Invester innovation i kanten (nye kanaler, nye funktioner, nye grænseflader), mens I holder den varige kerne stabil og velforstået. Ændr kernen, ja, men i små, reversible, velafprøvede trin frem for heroiske spring. Målet er et system, der både er pålideligt og i stand til at udvikle sig: aldrig så frosset, at det [rådner](https://en.wikipedia.org/wiki/Software_rot), aldrig så omrørt, at det bliver upålideligt.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Behold og vedligehold det gamle system | Bevarer institutionel viden; lav forstyrrelse; gennemprøvet pålidelighed | Aldrende stak; knappe færdigheder; voksende risiko hvis uvedligeholdt |
| Big-bang-omskrivning | Frisk stak; afviser ophobet skrammel | Meget høj fejlrate; mister hårdt tilkæmpet grænsetilfældeviden |
| Trinvis modernisering | Kontinuerlig risikoreduktion; forbliver i drift | Langsom; kræver vedvarende finansiering og disciplin |
| Dokumentationstung overdragelse | Eksplicit, søgbar optegnelse | Forfalder hvis uvedligeholdt; misser tavs viden |
| Menneskebaseret overdragelse (parprogrammering/rotation) | Varig arbejdsviden; robuste teams | Koster nuværende produktivitet; kræver bevidst planlægning |
| Frys den kritiske kerne | Maksimal stabilitet på kort sigt | Stakken ældes til uvedligeholdelighed; bliver for skræmmende at røre |

Den definerende afvejning er stabilitet versus udvikling, og de naive løsninger fejler begge. Frys et kritisk system for at beskytte det, og I garanterer, at det til sidst bliver uvedligeholdeligt og usikkert. Omskriv det i sin helhed for at modernisere, og I inviterer den høje fejlrate, big-bang-erstatninger er berygtede for, og I kasserer årtiers indkodet grænsetilfældeviden, ingen husker er der. Den varige vej er kontinuerlig, trinvis forandring: hold systemet i live og i bevægelse i små skridt, så det aldrig ældes ud af support og aldrig behøver et skræmmende spring. Videnoverdragelse er en lignende afvejning, mellem dokumenters lethed og levet erfarings varighed. Svaret er begge dele: levet, teamholdt viden som rygraden og dokumenter som referencen.

## Spørgsmål til drøftelse med dit team

1. **Hvilke af jeres kritiske systemer har lige nu ingen aktuel, navngiven teamejer?** Ejerskab er en løbende tildeling, ikke en erindring om, hvem der skrev koden, og et ejerløst kritisk system er en nødsituation, der venter på at ske, bemærket først når det går i stykker. Gennemgå jeres servicekatalog (eller byg et), og tjek, at hvert system registrerer, hvem der ejer det, hvad det afhænger af, og hvor kritisk det er. Tag dokumentation med: vælg tre vigtige systemer, og prøv at navngive det ansvarlige team og sidste gang, ejerskab blev gennemgået. Hvor et system er forældreløst, eller hvor en omorganisering stille tabte det, så tildel ejerskab bevidst med en reel overdragelse frem for ved antagelse. Sørg for, at ejerskab inkluderer evnen til at forstå og ændre systemet, så forvaltning ikke forfalder til blot barnepigearbejde.

2. **Når I erstatter et system, hvem er ansvarlig for faktisk at slukke det gamle?** Den evige parallelkørsel er en almindelig og kostbar fejl: gamle og nye systemer kører side om side på ubestemt tid, fordi ingen ejer nedlukningen, hvilket efterlader jer med at vedligeholde to systemer og få sikkerheden fra ingen af dem. Behandl hver nedlukning som et styret projekt med navngiven ansvarlighed for at fuldføre nedtagningen, en kortlagt liste over forbrugere, en migreringssti og en realistisk tidslinje. Tag dokumentation med: hvor mange "midlertidige" parallelkørsler eller halvt pensionerede systemer trækker stadig vedligeholdelse i jeres ejendom i dag? Bevar data og optegnelser for at opfylde lovpligtige opbevaringsregler længe efter, systemet holder op med at køre, men lad ikke opbevaring blive en undskyldning for aldrig at blive færdig. En nedlukning udført dårligt efterlader zombiesystemer, der er uvedligeholdte, men stadig afhængige, det værste af alle verdener.

3. **Hvilke færdigheder til jeres langlivede systemer vil arbejdsmarkedet holde op med at levere, og hvad er jeres successionsplan?** Systemer, der kører i tyve eller tredive år, overlever deres sprogøkosystemer, deres leverandører og karriererne hos de mennesker, der forstår den gamle stak, og markedet vil ikke pålideligt aflevere erstatninger. Reducér bus-faktor bevidst, så ingen kritisk funktion har præcis én kompetent person, og krydsuddan, så mindst to, helst tre, personer kan udføre hver væsentlig opgave. Tag dokumentation med: for hvert aldrende kritisk system så tæl hvor mange mennesker der sikkert kan ændre det, og hvor tæt de mest vidende er på pension. Svaret bør drive bevidst træning af efterfølgere og reel overlapning mellem afgående og ankommende forvaltere, fordi tavs viden (fornemmelsen for et system) overføres hovedsageligt ved at gøre noget sammen med en, der har den. Dokumenter er referencen; levet, teamholdt viden er rygraden.

4. **Hvornår ændrede I sidst jeres mest kritiske langlivede system, og tør nogen stadig?** Et system, ingen har rørt i et år, er ikke stabilt, det driver mod "for skræmmende at røre"-fælden, hvor enhver ændring frygtes, og stakken derfor stille ældes ud af support. For en stor organisation har det betydning, fordi lammelse akkumulerer: jo længere frysningen, desto mere viden forsvinder, og desto mere risikabel bliver den eventuelle uundgåelige ændring. Tag dokumentation med: for hvert kritisk system datoen for den sidste bevidste ændring, størrelsen på den mindste ændring, nogen i dag ville forsøge, og om en rutinemæssig afhængigheds- eller sikkerhedspatch kunne leveres i denne uge uden heltemod. Det modstridende hensyn er reelt, fordi forandring også indfører risiko, så målet er ikke omrøring, men en jævn kadence af små, reversible, velafprøvede skridt. I virksomheds- og offentlige ejendomme, hvor en frosset kerne kan sidde under en borgertjeneste i et årti, så behandl "vi ændrer den aldrig" som et rødt flag frem for en betryggelse, og finansiér den kontinuerlige vedligeholdelse, der holder muligheden for at ændre i live.

5. **Hvor stor en del af jeres ejendom kører på en teknologi, der er ved eller nær end of life, og hvem følger det ur?** Aldrende runtimes, ustøttede databaser og rammeværker uden vedligeholdelse er den langsomme fejlform, der bliver til en pludselig krise den dag, en sikkerhedspatch holder op med at ankomme. For et stort team er faren, at ingen ejer horisonten: individuelle teams patcher det, der går i stykker, men ingen vedligeholder et porteføljebillede af, hvilke stakke der mister leverandørsupport og hvornår. Tag dokumentation med: en fortegnelse over hvert kritisk systems kerneteknologier, deres offentliggjorte end-of-life- eller end-of-support-datoer og det nuværende hul mellem det, I kører, og det, der stadig støttes. Spændingen er mellem omkostningen ved kontinuerlig opgradering og risikoen ved udskydelse, og udskydelse vinder som regel, til den katastrofalt taber. I virksomheds- og offentlige sammenhænge, hvor indkøbs- og akkrediteringscyklusser kan tage et år eller mere, ligger en end-of-life-dato, der ser fjern ud, ofte allerede inden for jeres ledetid, så successions- og opgraderingsarbejdet må begynde længe før uret løber ud.

6. **Hvor i jeres ejendom er stabilitet værdien og nyhed et ansvar, og hvordan holder I den grænse ærlig?** Ikke alle systemer belønner den samme behandling: kernesystemer borgere og kunder afhænger af dagligt belønner som regel pålidelighed og forsigtig ændring, mens kanterne belønner eksperimentering, og at forveksle de to spilder penge eller inviterer til udfald. For en stor organisation er risikoen, at ambition og karriereincitamenter skubber spændende omskrivninger ind i netop den varige kerne, der bør forblive kedelig. Tag dokumentation med: et kort over jeres ejendom, der markerer, hvor pålidelighed er missionen, og hvor nyhed skaber værdi, plus nylige ændringer, der krydsede den linje i begge retninger, og hvad de kostede. Det modstridende hensyn er, at selv en stabil kerne stadig skal udvikle sig, så "stabil" kan ikke blive en undskyldning for at fryse. I virksomheds- og offentlige sammenhænge så bind den grænse til eksplicitte kritikalitetsniveauer og en navngiven autoritet, der kan nedlægge veto mod en risikabel omskrivning af et system, offentligheden ikke har råd til at se fejle, så dømmekraften ikke driver med, hvem der er højest dette kvartal.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og lidt runway er jeres vedligeholdelsesrisiko koncentreret i en eller to personer, der skrev de systemer, I ikke har råd til at miste, såsom fakturering eller autentificering. Brug næsten intet på proces, men gør de billige, højværdi ting nu: par en anden person gennem hvert kritisk system, skriv et arkitekturbeslutningsregister på én side til de overraskende dele, og hold en runbook, I faktisk bruger. Modstå trangen til at omskrive noget, blot fordi det er gammelt, for i jeres størrelse kan en fejlslagen omskrivning af et kernesystem afslutte virksomheden.

**Lille virksomhed.** I har intet dedikeret vedligeholdelsesteam og et stramt budget, så foretræk at købe og hoste frem for at bygge noget, I selv skulle vedligeholde. Foretræk leverandører og åbne standarder, der lader jer forlade dem, og hold en enkel optegnelse over, hvilket eksternt system der kører hvilken kritisk funktion, og hvem man ringer til, når det går i stykker. Hvor I ejer skræddersyet kode, så sørg for, at mindst to personer (eller en betroet konsulent plus en medarbejder) forstår den, så en enkelt afgang eller en udløbet supportkontrakt ikke efterlader jer strandet.

**Stor virksomhed.** Jeres udfordring er porteføljeskala: mange langlivede systemer, mange teams og medarbejdere, der roterer over årtier. Standardisér ejerskab på teamniveau i et servicekatalog, mål bus-faktor på tværs af ejendommen, og finansiér kontinuerlig trinvis modernisering frem for at satse på big-bang-omskrivninger. Styr end-of-life-horisonter centralt, så ingen kritisk stak stille ældes ud af support, og kør hver nedlukning som et revideret projekt med navngiven ansvarlighed for at fuldføre nedtagningen.

**Offentlig sektor.** Forpligtelsens kontinuitet er absolut: I kan ikke holde op med at udbetale ydelser eller køre flyvekontrol, mens I refaktorerer, og fejl er offentlige og konsekvensfulde. Indkøbsregler skubber jer mod åbne standarder, dataportabilitet og dokumenterede grænseflader, så fremtidige vedligeholdere og fremtidige leverandører har en chance. Finansiér bevidst successionstræning for de ældre teknologier, arbejdsmarkedet ikke længere leverer, bevar optegnelser over pensionerede systemer for at opfylde lovpligtig opbevaring, og behandl vedvarende pålidelighed af borgertjenester som den ansvarlige mission frem for overhead.

## Eksempler

**Startup.** Et startup på fem personer har allerede et system, det ikke har råd til at miste: faktureringstjenesten, en grundlægger skrev den første måned, og som nu kører hver kundeopkrævning. Kun den grundlægger forstår den, så teamet behandler bus-faktoren som en reel risiko frem for et kompliment. De par en anden ingeniør gennem en hel faktureringscyklus, skriver et kort arkitekturbeslutningsregister, der forklarer, hvorfor den mærkelige genforsøgslogik findes, og holder en runbook ved siden af koden, som de faktisk udøver under en hændelse. De modstår at omskrive den, blot fordi den er gammel og uglamourøs, og forbedrer den i stedet i små reversible skridt, så den tjeneste, der holder virksomheden i live, forstås af mere end ét hoved.

**Stor virksomhed.** Et stort forsikringsselskab kører et policeadministrationssystem, første gang skrevet for årtier siden og stadig centralt for dets forretning. I stedet for at forsøge en risikabel total omskrivning modulariserede det systemet bag veldefinerede grænseflader og erstatter nu én komponent ad gangen, hver ændring lille og reversibel. Hver kritisk funktion har mindst tre personer, der kan udføre den. Vagtberedskab er delt. Arkitekturbeslutningsregistre indfanger, hvorfor systemet fungerer, som det gør. Et kurateret internt kursus bringer nye ingeniører til kompetence på den [ældre](https://en.wikipedia.org/wiki/Legacy_system) stak, og afgående eksperter overlapper med efterfølgere, så tavs viden overføres ved at gøre.

**Offentlig sektor.** Et nationalt socialsikringsagentur driver ydelsesudbetalingssystemer, der har kørt i over tredive år og ikke kan stoppe. Det registrerer eksplicit teamejerskab i et servicekatalog. Det finansierer kontinuerlig vedligeholdelse frem for at fryse systemerne. Det træner bevidst efterfølgere i de ældre teknologier, fordi arbejdsmarkedet ikke vil levere dem. Når det pensionerer et forældet delsystem, kører det nedlukningen som et styret projekt: kortlægger hver forbruger, giver migreringsstøtte, bevarer optegnelser for at opfylde lovpligtige opbevaringsregler og tildeler ansvarlighed for faktisk at fuldføre nedtagningen, så intet zombiesystem hænger ved.

## Business case: motivation, ROI og TCO

Afkastet af at vedligeholde langlivede systemer kommer af at undgå de to katastrofale fejlformer, der dominerer deres [samlede ejeromkostning](https://en.wikipedia.org/wiki/Total_cost_of_ownership). Den første er den pludselige krise: en nøgleperson forlader jer, en ustøttet komponent bliver brudt, eller et forældreløst system fejler uden nogen, der forstår det. Den anden er det fejlslagne megaprojekt: en forhastet total omskrivning, der overskrider, underleverer eller kollapser. Begge er enormt dyre, og begge kan stort set forebygges ved jævn forvaltning. Omkostningen ved en enkelt undgået omskrivningsfiasko, eller et enkelt undgået forlænget udfald af en kritisk borgertjeneste, overstiger som regel års vedvarende vedligeholdelsesinvestering.

Adoptionsomkostningen er løbende og uglamourøs: at finansiere vedligeholdelse, der ikke producerer nye funktioner, at betale for krydsuddannelses- og dokumentationstid, der reducerer kortsigtet output, og at investere i trinvis modernisering, der aldrig kommer i overskrifterne. Omkostningen ved *ikke* at adoptere er udskudt og større: stigende risiko, efterhånden som stakken ældes, svulmende nøgleperson-eksponering og til sidst en tvungen, højrisiko, højomkostningserstatning under nødforhold. Når I fremlægger sagen for ledelsen, så ram vedligeholdelse om fra "omkostningscenter" til "risikostyring for systemer, organisationen ikke har råd til at miste." Præsentér samlet ejeromkostning over hele det flerårige liv (inklusive vedligeholdelsen og den eventuelle nedtagning) frem for kun bygningen. Og fremhæv dette: for borger- og kundevendte systemer er vedvarende pålidelighed ikke overhead. Det er den tillid, der er det egentlige produkt.

## Anti-mønstre og faldgruber

- **Den heroiske vedligeholder.** Én uerstattelig person, der forstår systemet; deres afgang er en eksistentiel begivenhed.
- **Frys og glem.** At erklære et kritisk system "færdigt", stoppe vedligeholdelse og se dets stak ældes til uvedligeholdelighed.
- **Den dødsdømte omskrivning.** At satse organisationen på en total erstatning, der kasserer indkodet viden og som regel overskrider eller fejler.
- **Forældreløse systemer.** Kritisk software uden nuværende ejer, bemærket først når den går i stykker.
- **Dokumentationsteater.** Bind af dokumenter, der er forældede, uudøvede og betroet af ingen.
- **Den evige parallelkørsel.** Gamle og nye systemer, der kører side om side på ubestemt tid, fordi ingen er ansvarlig for nedlukningen.
- **Tab af tavs viden.** At lade eksperter forlade jer uden overlapning, så fornemmelsen for systemet fordamper.
- **For skræmmende at røre.** Et system så dårligt forstået, at enhver ændring frygtes, hvilket garanterer, at det forfalder.

## Modenhedsmodel

**Niveau 1: Opstart.** Vedligeholdelse er ad hoc og reaktiv. Systemer afhænger af individuelle helte, ejerskab huskes frem for tildeles, og viden bor udokumenteret i nogle få hoveder. Gamle systemer fryses, til de går i stykker, aldrende stakke driver mod end of life ubemærket, og pensioneringer annonceres, men fuldføres aldrig.

**Niveau 2: Udvikling.** Basale praksisser dukker op, men varierer team for team. Ejerskab er skrevet ned for de mest åbenlyse større systemer, nogle runbooks og noget dokumentation findes, og nogle få kritiske funktioner har en anden kompetent person. Vedligeholdelse er finansieret, men reaktiv, krydsuddannelse sker, når nogen husker det, og der er ingen fælles måde at gøre noget af det på på tværs af organisationen.

**Niveau 3: Standardisering.** Forvaltningspraksisser er dokumenteret og håndhævet i hele organisationen. Ejerskab på teamniveau registreres i et servicekatalog og overlever omorganiseringer. Bus-faktor-afbødning gennem rotation og krydsuddannelse er en stående regel, arkitekturbeslutningsregistre og udøvede runbooks forventes, modernisering er trinvis ved politik, og hver nedlukning kører som et styret projekt med navngiven ansvarlighed for at fuldføre nedtagningen.

**Niveau 4: Styring.** Vedligeholdelse måles og styres med data mod baselines. I følger bus-faktor pr. kritisk system, antallet af personer, der sikkert kan ændre hvert, alderen på hver kerneteknologi mod dens end-of-life-dato, andelen af ejendommen under kontinuerlig versus udskudt vedligeholdelse og antallet af gået-i-stå parallelkørsler og halvfærdige nedtagninger. Disse målinger bærer tærskler, der udløser handling: et system, der falder under bus-faktor-gulvet eller krydser en end-of-support-horisont, får finansieret afhjælpning, og forvaltningssundhed rapporteres til ledelsen sammen med levering.

**Niveau 5: Orkestrering.** Forvaltning forbedres løbende og er integreret på tværs af organisationen. Intet kritisk system er et enkeltstående menneskeligt fejlpunkt, videnoverdragelse inklusive tavs viden gennem overlapning er rutine, og systemer udvikler sig i små reversible skridt, så ingen ældes ud af support. Ejerskab, end-of-life-sporing, succession og nedlukningsplanlægning er vævet ind i portefølje- og risikoplanlægning, ejendommen rebalanceres, efterhånden som teknologier og forpligtelser skifter, og flerårige systemer vedligeholdes, mens tilliden hos de mennesker, der afhænger af dem, bevares.

## Idéer til drøftelse

- Hvordan måler I bus-faktor meningsfuldt, og hvilket mål er det rette for forskellige kritikalitetsniveauer?
- Hvornår er trinvis modernisering reelt umulig, så en omskrivning er den mindre risiko?
- Hvordan finansierer og belønner I vedligeholdelsesarbejde, så forvaltning er en respekteret karrierevej, ikke en blindgyde?
- Hvad er den rette måde at bevare tavs viden på, når den sidste ekspert er ved at gå på pension, og ingen overlapning er mulig?
- Hvor længe bør I bevare evnen til at besvare spørgsmål om et pensioneret system, og hvem betaler for det?
- Hvor i jeres ejendom er stabilitet værdien og nyhed et ansvar, og hvordan holder I den dømmekraft ærlig over tid?

## Vigtigste pointer

- Det meste vigtige software er gammelt og langlivet; at vedligeholde det på tværs af årtier og medarbejdergenerationer er en førsteklasses disciplin.
- Hvert kritisk system har brug for aktuelt ejerskab på teamniveau; forældreløse kritiske systemer er latente nødsituationer.
- Reducér bus-faktor bevidst (ingen kritisk opgave bør have præcis én kompetent person), og overfør tavs viden gennem overlapning, ikke blot dokumenter.
- Hold langlivede systemer kontinuerligt og trinvis vedligeholdt; at fryse dem og at satse på total omskrivning er begge fejlformer.
- Planlæg afslutninger som styrede projekter med ansvarlig fuldførelse, og bevar data og optegnelser for at opfylde forpligtelser.
- For borger- og kundevendte systemer er vedvarende pålidelighed og retfærdighed missionen, og vedligeholdelse er risikostyring for det, I ikke har råd til at miste.

## Referencer og videre læsning

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce and Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* and writings on the Strangler Fig pattern
- Betsy Beyer et al., *Site Reliability Engineering* and *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, reports on federal legacy IT modernisation
