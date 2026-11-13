# 2.19 Refaktorering og teknisk gæld

## Overblik og motivation

[Refaktorering](https://en.wikipedia.org/wiki/Code_refactoring) er at ændre kodens indre struktur uden at ændre, hvad den gør udadtil. Du omdøber en variabel, deler en lang funktion, uddrager en klasse, kollapser en sammenfiltring af betingelser til noget, en læser kan følge, og programmet opfører sig præcis som før. Den sidste del er hele disciplinen. Refaktorering bevarer adfærd per definition, og i det øjeblik du også ændrer adfærd, refaktorerer du ikke længere, du gør to risikable ting på én gang og skjuler hver bag den anden. Dette kapitel behandler dem som adskilte handlinger med vilje, fordi forvekslingen mellem dem er, hvor det meste refaktorering går galt.

I et stort team betyder dette mere end for en enkelt udvikler, fordi den kode, du rydder op i, er kode, hundredvis af andre læser, afhænger af og er bange for at røre. Refaktorering er, hvordan en fælles kodebase forbliver beboelig gennem år og personaleudskiftning. Det hænger direkte sammen med softwarekonstruktion (kapitel 2.9), hvor den daglige kodningskvalitet fastsættes, og med teststrategi (kapitel 2.4), som er det sikkerhedsnet, der overhovedet gør refaktorering sikker. Det hænger også sammen med det sværere spørgsmål om [teknisk gæld](https://en.wikipedia.org/wiki/Technical_debt): de akkumulerede omkostninger ved genveje, aldrende designs og udskudt oprydning, der gør hver fremtidig ændring langsommere. Refaktorering er den vigtigste måde, du betaler den gæld ned, så de to emner hører hjemme i ét kapitel.

I virksomheds- og offentlige sammenhænge stiger indsatsen. Disse systemer er langlivede, ofte årtier gamle, og står hyppigt under revisions- og ændringskontrolregimer, der behandler enhver kodeændring som en styret begivenhed. Du kan ikke blot omskrive et borgerydelsessystem over en lang weekend; du moderniserer det i små, reversible, dokumentationsbaserede skridt, hvilket netop er, hvad disciplineret refaktorering giver dig. At koordinere det arbejde på tværs af mange teams og langlivede systemer (kapitel 10.4) er en af de definerende udfordringer i ingeniørarbejde i stor skala, og at gøre det forkert er, hvordan organisationer ender frosne, ude af stand til at ændre software, de ikke længere forstår.

## Grundprincipper

- Refaktorering bevarer adfærd; hvis du ændrer, hvad koden gør, er det en separat ændring, udført separat.
- En pålidelig testsuite er forudsætningen for sikker refaktorering, ikke et valgfrit tilbehør.
- Arbejd i små, navngivne, reversible skridt, og hold koden fungerende efter hvert.
- Gør teknisk gæld synlig og sporet, og finansiér derefter nedbetaling som jævn kapacitet frem for heltemod.
- Refaktorér den kode, du allerede ændrer, hvor oprydningen tjener sit brød.
- Ikke al gæld er værd at betale; stabil, sjældent rørt eller snart pensioneret kode kan lades i fred.
- Mål intern kvalitet for at informere dømmekraft, aldrig som et mål, der skal manipuleres.

## Anbefalinger

### Hold refaktorering og adfærdsændring strengt adskilt

Beslut, før du begynder, hvilken af dem du gør, og lad aldrig de to flyde sammen i en enkelt commit. Når du refaktorerer, skal de tests, der bestod før, bestå efter, uændrede, fordi den observerbare adfærd ikke er flyttet. Når du ændrer adfærd, så gør det som sin egen commit med sine egne tests. Grunden er praktisk: hvis en blandet ændring bryder noget, kan du ikke se, om din omstrukturering indførte fejlen, eller din adfærdsændring gjorde, og i kodegennemgang (kapitel 2.5) kan en gennemganger ikke ræsonnere rent om nogen af halvdelene. Den vane, der virker, er topersonhat-reglen fra Martin Fowler: du bærer altid enten refaktoreringshatten eller featurehatten, du ved hvilken, og du skifter bevidst. Separate commits gør også [versionsstyringshistorikken](https://en.wikipedia.org/wiki/Version_control) læselig, så en ingeniør, der bisekterer en fejl, trygt kan springe de rene refaktoreringscommits over.

### Etablér et pålideligt sikkerhedsnet, før du omstrukturerer

Refaktorering uden tests er blot redigering og håb. Før du omstrukturerer noget af betydning, har du brug for en suite, du stoler på til at fange en adfærdsændring, hvis du forårsager en, hvilket er kerneargumentet i teststrategi (kapitel 2.4). For kode, der allerede har god dækning, så kør testene, refaktorér i små skridt, og kør dem igen efter hvert skridt. For legacy-kode uden tests er det ærlige træk at skrive [karakteriseringstests](https://en.wikipedia.org/wiki/Characterization_test) først. En karakteriseringstest hævder ikke, hvad koden bør gøre; den fanger, hvad koden faktisk gør lige nu, herunder dens særheder, så enhver ændring i adfærd viser sig som en fejlende test. Michael Feathers populariserede denne tilgang netop til den situation, store organisationer lever i: kode der virker, betyder noget og ikke har nogen tests. Når den nuværende adfærd er fastnaglet, kan du refaktorere nedenunder sikkert, og først derefter ændre adfærd ovenpå.

### Lær at genkende kodelugte, og anvend små navngivne refaktoreringer

En [kodelugt](https://en.wikipedia.org/wiki/Code_smell) er et overfladetegn på, at noget nedenunder måske har brug for opmærksomhed: en funktion, der er vokset for lang, en klasse, der ved for meget, duplikeret logik, en lang parameterliste, navne der lyver om, hvad de gør. En lugt er et vink, ikke en dom, så du undersøger frem for at adlyde den blindt. Svaret er en lille, navngivet refaktorering fra Fowlers katalog: Extract Function, Rename Variable, Move Method, Replace Conditional with Polymorphism og dusinvis flere. Værdien af at bruge navngivne træk er, at hvert er lille, forstået, mekanisk sikkert og ofte understøttet direkte af din IDE. Du sammensætter store forbedringer af mange små pålidelige skridt og holder koden grøn hele vejen, frem for at tage ét stort spring, du ikke kan verificere.

### Foretræk opportunistisk refaktorering, og forbehold kampagner til reelt strukturelt behov

Det meste refaktorering bør være opportunistisk, foldet ind i det arbejde, du allerede udfører. Spejderreglen fanger det: efterlad koden lidt renere, end du fandt den. Når du rører en fil for at tilføje en feature eller rette en fejl, forstår du allerede det hjørne, og små oprydninger der akkumuleres over tid uden at kræve nogens tilladelse eller et separat budget. Planlagte refaktoreringskampagner, hvor et team standser featurearbejde for at omstrukturere et stort område, er nogle gange nødvendige, men de er dyre, svære at planlægge mod produktpres og risikable, hvis området er dårligt testet. Forbehold kampagner til strukturelle problemer, som opportunistisk oprydning ikke kan nå, og fremfør sagen med dokumentation om den ændringsomkostning, du betaler. Foretræk den jævne dryppen af små oprydninger; den er mere varig end den lejlighedsvise heroiske omskrivning.

### Brug strangler fig-mønstret til store strukturelle ændringer

Når et helt delsystem skal erstattes, så forsøg ikke en big-bang-omskrivning, der løber i et år og flettes til sidst; sådan dør moderniseringsprojekter. Brug [strangler fig-mønstret](https://en.wikipedia.org/wiki/Strangler_fig_pattern), opkaldt af Martin Fowler efter vinstokken, der vokser rundt om et træ og gradvist erstatter det. Du sætter en facade foran det gamle system, dirigerer én skive funktionalitet ad gangen til ny kode bag den facade, verificerer det i produktion og gentager, til det gamle system er fuldt omgivet og kan fjernes. Hver skive er lille, udgivelig og reversibel, så risikoen forbliver afgrænset, og værdi ankommer løbende. En tæt fætter, branch by abstraction, gør det samme inde i en enkelt kodebase: du indfører et abstraktionslag over det, du vil erstatte, bygger den nye implementering bag det, mens begge sameksisterer, skifter forbrugerne gradvist over og sletter den gamle implementering, når intet længere afhænger af den. Begge lader et [legacy-system](https://en.wikipedia.org/wiki/Legacy_system) udvikle sig, mens det forbliver i live, hvilket er den eneste slags modernisering, de fleste store organisationer faktisk har råd til.

### Behandl teknisk gæld som en portefølje, og gør den synlig

Gældsmetaforen, opfundet af Ward Cunningham, adskiller to ting: hovedstolen (den rodede kode eller genvej selv) og renten (den ekstra indsats, hver fremtidig ændring betaler på grund af den). Ikke al gæld er lige. Fowlers kvadrant sorterer den langs to akser: bevidst versus utilsigtet og klog versus skødesløs. Klog-bevidst gæld ("vi udgiver nu og rydder op næste sprint, og vi kender omkostningen") er en legitim forretningsbeslutning. Skødesløs-utilsigtet gæld ("hvad er et designmønster?") er blot skade. Ledelsesopgaven, som hænger sammen med beslutningstagning og styring (kapitel 1.5) og dets behandling af gæld som en portefølje, er at gøre gælden synlig, så der kan ræsonneres om den: følg betydelige poster, hvor arbejdet bor, mærk koden, og registrér den rente, du betaler, så nedbetaling konkurrerer om kapacitet på dokumentation frem for på, hvem der klager højest. Gæld, du ikke kan se, kan du ikke styre.

### Finansiér nedbetaling som jævn kapacitet, ikke heltemod

Fejlformen er at behandle oprydning som noget, du vil gøre "når tingene falder til ro," hvilket er aldrig. Det varige mønster er en fast, beskyttet kapacitet til nedbetaling: en eksplicit skive af hver cyklus, eller en stående aftale om, at oprydning følger med featurearbejde i samme område. Det, der ikke virker, er det periodiske heroiske sprint, hvor nogen brænder en weekend af for at rette alt, fordi det er uholdbart, ugennemgået og som regel ophæver sig selv. Jævn kapacitet holder rentebetalinger nede og undgår den opgangs-og-nedgangs-cyklus, hvor gæld akkumuleres, til en krise tvinger en dyr omskrivning. Dette er lige så meget en ledelsesforpligtelse som en ingeniørpraksis, og det hører hjemme i, hvordan du planlægger softwarevedligeholdelse (kapitel 3.7) gennem et systems liv.

### Mål intern kvalitet, men lad ikke målingen blive målet

Du kan måle intern kvalitet med signaler som [cyklomatisk kompleksitet](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (et antal uafhængige stier gennem en funktion), duplikering, testdækning, andel fejlslagne ændringer og hvor lang tid ændringer tager i de områder, du mistænker. Disse tal er nyttige til at spotte, hvor gæld koncentreres, og til at følge en tendens over tid. Faren er Goodharts lov: når en måling bliver et mål, holder den op med at måle noget reelt. Påbyd et dækningstal, og du får tests, der ikke hævder noget; beløn lave kompleksitetsscorer, og du får logik smurt ud over flere funktioner for at undgå målingen. Brug målinger til at starte samtaler og lokalisere hotspots, og bind aldrig en kvalitetsmåling til en port, folk er motiverede til at manipulere.

### Vid, hvornår du ikke skal refaktorere

Refaktorering er en investering, og nogen kode vil aldrig betale sig tilbage. Hvis et modul er stabilt, sjældent rørt og forstået godt nok til at blive ændret de sjældne gange, du må, er det at rydde op indsats brugt på rente, du ikke betalte. Hvis kode er sat til pensionering, er refaktorering af den polering af noget, du er ved at smide ud. Disciplinen er at bruge dit oprydningsbudget, hvor ændring er hyppig og smertefuld, hvilket er, hvor reduktion af renten faktisk akkumuleres, og at lade de stille hjørner være.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
| --- | --- | --- |
| Opportunistisk refaktorering (spejderreglen) | Billig, løbende, intet separat budget, akkumuleres over tid | Ujævn dækning; varme filer forbedres, mens kolde rådner |
| Planlagt refaktoreringskampagne | Retter strukturelle problemer, oprydning ikke kan nå | Dyr; konkurrerer med features; risikabel uden gode tests |
| Strangler fig / branch by abstraction | Inkrementel, reversibel, holder systemet i live, afgrænser risiko | Langsommere end en omskrivning på papiret; kræver disciplin at færdiggøre |
| Big-bang-omskrivning | Blankt ark; ingen legacy-begrænsninger | Høj fejlrate; lang tid til værdi; adfærdshuller |
| Bevidst klog gæld | Leverer værdi nu; eksplicit, planlagt tilbagebetaling | Bliver skødesløs, hvis tilbagebetalingen aldrig planlægges |
| Målingsstyret kvalitet | Objektiv, synlig, fanger drift tidligt | Inviterer til manipulation; straffer nuancer; kan forringe reel kvalitet |

Den centrale spænding er hastighed nu versus ændringsdygtighed senere, og den er reel. At udgive en genvej kan være det rette kald, når deadlinen er ægte, og gælden er klog og sporet. Fejlen er at lade som om gælden er gratis eller lade den akkumulere usynligt, til systemet er for dyrt at ændre. Løs det ved at gøre afvejningen eksplicit hver gang: navngiv gælden, estimér renten, beslut bevidst, og registrér beslutningen, så nedbetaling kan planlægges frem for glemmes. Et team, der låner bevidst og betaler jævnt, forbliver hurtigt i årevis; et team, der låner blindt, går i stå.

## Spørgsmål til drøftelse med dit team

1. **Hvordan forhindrer vi refaktorering og adfærdsændring i at flyde ind i samme commit, og håndhæver vores gennemgang det faktisk?** Dette er kapitlets grundlæggende disciplin, og den, der oftest brydes under deadlinepres, fordi det føles effektivt at "rydde op, mens jeg er her" og udgive det hele sammen. Omkostningen lander senere: når en blandet commit bryder produktion, kan ingen se, om omstruktureringen eller featuren forårsagede det, og en bisektion gennem jeres historik holder op med at være pålidelig. Tag en håndfuld nylige pull requests med og tjek ærligt, hvor mange der blandede de to hatte. Det modstridende hensyn er gnidning, da det at opdele arbejde i separate commits er lidt mere indsats på forhånd. Svaret bør forme jeres commitkonventioner og jeres gennemgangstjekliste.

2. **Hvor er vores tekniske gæld, hvor meget rente betaler vi på den, og hvem beslutter, hvad der betales ned?** De fleste teams kan ikke besvare dette, hvilket er det egentlige problem, fordi gæld, I ikke kan se, styres af den, der klager højest, frem for af hvor omkostningen reelt er. At gøre den synlig betyder at følge betydelige poster, mærke koden og indsamle dokumentation om, hvilke områder der gør ændringer langsomme og fejlbehæftede. Det modstridende træk er, at hver time brugt på nedbetaling er en time, der ikke bruges på features, så beslutningen må være en porteføljebeslutning truffet med ledelsen, i forbindelse med hvordan I styrer ingeniørarbejde (kapitel 1.5). Tag jeres data om andel fejlslagne ændringer og jeres liste over filerne, alle frygter at røre, med. Svaret bør blive til en beskyttet, jævn nedbetalingskapacitet, ikke en vag intention om at rydde op, når tingene falder til ro.

3. **Hvilke dele af vores kodebase bør vi bevidst ikke refaktorere, og hvordan ville vi vide det?** At refaktorere alt er lige så meget en fejl som at refaktorere intet, fordi indsats brugt på at rydde stabil, sjældent rørt eller snart pensioneret kode er rente betalt på et lån, I ikke skyldte. Dømmekraften er reel: et modul kan se grimt ud og stadig være det forkerte sted at investere, hvis ingen nogensinde ændrer det. Tag jeres ændringsfrekvensdata med sammen med jeres kompleksitetssignaler, fordi skæringspunktet mellem høj omsætning og høj kompleksitet er, hvor oprydning akkumuleres, mens kode med lav omsætning som regel bedst lades i fred. Den modstridende risiko er, at "vi lader den være" bliver en undskyldning for aldrig at røre noget svært. Svaret bør give jer en eksplicit kortliste over hotspots, der er værd at investere i, og tilladelse til at ignorere de stille hjørner.

4. **Stoler vi nok på vores testsuite til at refaktorere den kode, vi mest har brug for at ændre, og hvor ville vi skulle skrive karakteriseringstests først?** Et sikkerhedsnet, I ikke kan stole på, forvandler refaktorering til redigering og håb, og i et stort team er den mest skræmmende kode som regel den mindst testede, hvilket netop er, hvor oprydning ville betale sig mest. Tag dækningsdata og data om andel fejlslagne ændringer for jeres hotspots med, og vær ærlige om, hvilke kritiske moduler der ikke ville give jer nogen advarsel, hvis en omstrukturering ændrede adfærd. Det modstridende hensyn er, at at skrive karakteriseringstests til legacy-kode er langsomt, uglamourøst arbejde, der ikke leverer nogen feature, så det er let at udskyde for evigt. I virksomheds- og offentlige systemer under revision og ændringskontrol er de fastnaglede tests også dokumentationen for, at en ændring bevarede adfærd, så at finansiere dem er både en sikkerheds- og en compliance-foranstaltning på én gang; svaret bør navngive, hvilke områder der får en testharness, før nogen rører dem.

5. **Når et delsystem reelt skal erstattes, hvordan vælger vi mellem en inkrementel strangler fig-tilgang og en omskrivning, og hvem har autoritet til at sige nej til omskrivningen?** Big-bang-omskrivningen er den mest forførende og mest fejlbehæftede mulighed på bordet, fordi et blankt ark altid ser billigere ud på papiret end at leve med de gamle begrænsninger. For en stor organisation holder den inkrementelle vej (en facade, én skive ad gangen, verificeret i produktion) systemet i live og afgrænser risikoen, men den er langsommere, kræver disciplin at færdiggøre og konkurrerer med appetitten på en frisk start. Tag delsystemets ændringsfrekvenskort med, et ærligt skøn over, hvor lang tid en omskrivning ville løbe, før den leverede værdi, og de adfærdshuller, en parallel omskrivning skulle lukke. I offentlige og regulerede sammenhænge er en omskrivning over flere år, der flettes til sidst, sjældent overlevelig under revision, så svaret bør som standard være strangler fig eller branch by abstraction og behandle enhver omskrivning som en undtagelse, der skal argumenteres for med dokumentation.

6. **Hvordan bruger vi interne kvalitetsmålinger til at finde, hvor gæld koncentreres, uden at lade et tal blive et mål, folk manipulerer?** Målinger som kompleksitet, duplikering, dækning og andel fejlslagne ændringer er den eneste måde, en stor organisation kan se på tværs af kode, ingen enkelt person læser, men i det øjeblik en bindes til en port eller en præstationssamtale, tager Goodharts lov over, og tallet holder op med at måle noget reelt. Tag eksempler med på, hvor en måling allerede driver adfærd, og spørg, om den starter samtaler eller stille belønner tests, der ikke hævder noget, og logik smurt ud over funktioner for at undgå en tærskel. Det modstridende træk er, at ledelsen vil have et simpelt dashboardtal, og "brug dømmekraft" er sværere at sælge end en grøn bjælke. I virksomheds- og offentlige sammenhænge, hvor målinger føder styringsrapportering, så vær eksplicit om, at kvalitetssignaler informerer investering og lokaliserer hotspots, men aldrig lukker porten for enkeltpersoner; svaret bør trække en fast linje mellem at måle for at lære og at måle for at dømme.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og ingen runway at give af så refaktorér kun opportunistisk: bær én hat pr. commit, så historikken forbliver bisekterbar, og hold en kort ærlig liste over de genveje, du tog med vilje. Lancér ikke oprydningskampagner og pudsér ikke stabile moduler; brug din knappe opmærksomhed på den ene fil, alle frygter, og skriv kun karakteriseringstests, hvor en ændring faktisk skræmmer dig. Bevidst, synlig gæld er fin på dette trin; skødesløs usynlig gæld er det, der slår dig ihjel.

**Lille virksomhed.** Uden en dedikeret platforms- eller værktøjsspecialist og med et stramt budget så støt dig til det, din IDE og dit sprogs økosystem giver dig gratis: automatisk omdøbning og uddragstræk, en linter og et grundlæggende dækningssignal. Behandl det meste gæld som noget, du styrer i løbet af det almindelige arbejde, frem for noget du hyrer en konsulent til at rette, og foretræk at købe velvedligeholdte biblioteker frem for at bygge og så skulle refaktorere dine egne. Forbehold den sjældne betalte indsats til det ene system, hvis langsomhed direkte koster dig kunder.

**Stor virksomhed.** På tværs af mange teams er problemet porteføljestyring: et fælles gældsregister, ensartet mærkning af hotspots efter ændringsfrekvens og kompleksitet og en beskyttet skive af hvert teams kapacitet til nedbetaling, så oprydning holder op med at tabe til features som standard. Standardisér topersonhat-disciplinen og karakteriseringstestpraksis, så enhver ingeniør, der skifter mellem teams, finder de samme regler, og brug strangler fig og branch by abstraction til strukturel ændring koordineret på tværs af grupper. Hold kvalitetsmålinger informative, så de lokaliserer gæld uden at blive manipuleret i præstationssamtaler.

**Offentlig sektor.** Langlivede systemer under streng revision og ændringskontrol gør disciplineret refaktorering til et compliance-aktiv, ikke kun et ingeniøraktiv: at holde omstrukturering strengt adskilt fra adfærdsændring lader revisorer se præcis, hvilke commits der ændrede adfærd, og hvilke der blot ryddede op. Indkøbs- og åbenhedsregler favoriserer små, reversible, dokumentationsbaserede skridt frem for big-bang-omskrivninger, så vælg som standard strangler fig med karakteriseringstests, der dokumenterer at adfærd er bevaret. Gør gældsregisteret og dets nedbetalingsplan til en del af systemets vedligeholdelsesoptegnelse, så tilsynsorganer får den sporbarhed, de kræver.

## Eksempler

**Startup.** Et startup med seks medarbejdere udgiver hurtigt og ved, at det optager gæld, så det gør to billige ting godt. Hver pull request bærer én hat: refaktoreringscommits er adskilt fra featurecommits, hvilket holder deres historik bisekterbar selv ved høj hastighed. Og de holder en kort, ærlig liste over de genveje, de tog med vilje, med en enlinjes note om den rente, hver koster. Da et betalingsmodul bliver den fil, alle frygter, gør den liste plus deres historik over fejlslagne ændringer sagen for at bruge to dage på at uddrage en renere grænse. De skriver karakteriseringstests for at fastnagle den nuværende adfærd, refaktorerer nedenunder med IDE'ens omdøbnings- og uddragstræk og rører aldrig de stabile moduler, ingen ændrer. Den gæld, de bærer, er bevidst og synlig, så den bliver aldrig den skødesløse slags.

**Stor virksomhed.** Et globalt logistikfirma kører et femten år gammelt ordresystem, som mange teams ændrer hver uge. I stedet for en omskrivning adopterer de strangler fig-mønstret: en facade sidder foran monolitten, og én afgrænset kapacitet ad gangen omdirigeres til nye tjenester bag den, verificeret i produktion, før den næste skive begynder. At koordinere dette på tværs af teams og et langlivet system (kapitel 10.4) er det svære, så de vedligeholder et fælles gældsregister, mærker hotspots efter ændringsfrekvens og kompleksitet og reserverer en fast skive af hvert teams kapacitet til nedbetaling. Interne kvalitetsmålinger informerer om, hvor man skal kigge, men lukker aldrig porten for nogens præstationssamtale, hvilket holder tallene ærlige. I løbet af to år skrumper monolitten støt, og ingen enkelt ændring risikerer nogensinde hele systemet.

**Offentlig sektor.** Et nationalt skatteagentur skal modernisere en årtier gammel vurderingsplatform under streng revision og ændringskontrol, hvor hver kodeændring er en styret, dokumentationsbaseret begivenhed. En big-bang-omskrivning er umulig, så de bruger branch by abstraction: et abstraktionslag indføres over den gamle beregningsmotor, en ny implementering bygges bag det, og forbrugere migreres én skatteregel ad gangen, hver migrering dokumenteret som en lille, reversibel ændring med karakteriseringstests, der beviser at adfærd er uændret. Fordi refaktorering holdes strengt adskilt fra enhver lovgivningsmæssig adfærdsændring, kan revisorer se præcis, hvilke commits der ændrede adfærd, og hvilke der blot omstrukturerede. Gældsregisteret og dets nedbetalingsplan bliver en del af systemets vedligeholdelsesoptegnelse (kapitel 3.7), hvilket giver tilsynsorganer den sporbarhed, de kræver.

## Business case: motivation, ROI og TCO

Afkastet af refaktorering og gældsnedbetaling er den vedvarende evne til at ændre software billigt, og for de fleste systemer er størstedelen af livstidsomkostningen vedligeholdelse, så det er her, de totale ejeromkostninger i vid udstrækning afgøres. Renten på teknisk gæld betales i den valuta, ledelsen allerede følger: langsommere levering, højere andel fejlslagne ændringer, længere tid til at komme sig efter hændelser og ingeniører, der undgår den mest skræmmende kode. Når du gør gæld synlig og finansierer nedbetaling jævnt, sænker du omkostningen ved hver fremtidig ændring i de områder, der betyder mest, og undgår opgangs-og-nedgangs-mønstret, hvor forsømt gæld tvinger en dyr nødomskrivning.

Omkostningen ved at indføre det er beskeden og mest kulturel: etablér topersonhat-disciplinen, byg sikkerhedsnettet, hvor du har brug for at refaktorere, hold et gældsregister og beskyt en jævn skive kapacitet til nedbetaling. Omkostningen ved forsømmelse akkumuleres stille. Rente løber på hver ændring, til hastigheden kollapser, og organisationen finder sig frosset, ude af stand til sikkert at ændre et system, den ikke længere forstår, hvilket er det dyreste udfald af alle. For at argumentere over for ledelsen, forbind gæld direkte til de leveringsmålinger, de allerede bekymrer sig om, og ram nedbetaling ind som en porteføljebeslutning med en målbar gevinst, ikke som ingeniører, der beder om tid til at rydde op.

## Anti-mønstre og faldgruber

- **At blande refaktorering med adfærdsændring:** én commit gør begge, så et brud ikke kan tilskrives, og historikken bliver upålidelig.
- **Refaktorering uden et sikkerhedsnet:** at omstrukturere utestet kode og håbe, hvilket er redigering på tro.
- **Big-bang-omskrivningen:** at erstatte et fungerende system på én gang, et mønster med høj fejlrate og lang tid til værdi.
- **Refaktorering som en heroisk weekend:** ugennemgået, uholdbar oprydning, der ophæver sig selv, i stedet for jævn kapacitet.
- **Usynlig gæld:** genveje ingen følger, så nedbetaling drives af klagevolumen frem for faktisk omkostning.
- **Manipulation af kvalitetsmålinger:** at ramme et dækningsmål eller kompleksitetsmål, mens den reelle kvalitet falder, fordi målingen blev målet.
- **Refaktorering af den forkerte kode:** at polere stabile eller snart pensionerede moduler, mens de sande hotspots bliver ved med at koste dig.
- **Evig refaktorering:** endeløs omstrukturering, der aldrig leverer værdi, spejlbilledet af aldrig at rydde op.

## Modenhedsmodel

- **Niveau 1, Opstart:** Refaktorering er ad hoc og reaktiv, ofte blandet med adfærdsændring i samme commit. Der er intet pålideligt sikkerhedsnet, teknisk gæld er usynlig og sporløs, og oprydning sker kun i lejlighedsvise heroiske udbrud eller slet ikke.
- **Niveau 2, Udvikling:** Nogle teams adskiller refaktorering fra adfærdsændring og støtter sig til tests, hvor de findes, og navngivne refaktoreringer og karakteriseringstests dukker op i lommer. Praksis er inkonsistent på tværs af teams, gæld drøftes og logges nogle gange, og nedbetaling konkurrerer ad hoc mod features og taber som regel.
- **Niveau 3, Standardisering:** Topersonhat-disciplinen, karakteriseringstests til legacy-kode og små navngivne refaktoreringer er dokumenteret og forventet i hele organisationen. Gæld spores i et fælles register, der adskiller hovedstol fra rente, og en beskyttet kapacitet til nedbetaling planlægges hver cyklus og håndhæves i gennemgang.
- **Niveau 4, Styring:** Gæld og oprydning måles og styres med data mod baselines. Du følger ændringsfrekvens og kompleksitet for at lokalisere hotspots, holder øje med andel fejlslagne ændringer og ændringsledetid i refaktorerede områder og registrerer den rente, hver betydelig post koster, så nedbetalingsbeslutninger hviler på dokumentation, og afvikl-eller-invester-kald træffes på tendenser frem for klagevolumen. Kvalitetssignaler informerer investering uden at være bundet til porte, folk kan manipulere.
- **Niveau 5, Orkestrering:** Gæld styres som en løbende genbalanceret portefølje integreret med produkt- og vedligeholdelsesplanlægning i hele organisationen. Strukturel ændring bruger rutinemæssigt strangler fig og branch by abstraction koordineret på tværs af teams, nedbetaling er løbende og afstemt efter, hvor ændring er hyppig og smertefuld, og praksis tilpasser sig, efterhånden som systemet og dets risikobillede skifter, så langlivet kode forbliver ændringsdygtig gennem årtier.

## Idéer til drøftelse

1. Hvad er jeres teams faktiske, håndhævede regel for at holde refaktorering adskilt fra adfærdsændring, og hvor bryder den sammen under deadlinepres?
2. Hvordan beslutter I, med dokumentation, hvilken kode der fortjener oprydning, og hvilken der bedst lades i fred?
3. Hvor ville karakteriseringstests lade jer sikkert refaktorere et legacy-område, I i øjeblikket undgår?
4. For jeres næste større modernisering, hvordan ville en strangler fig-tilgang se ud, og hvilken facade eller abstraktion ville I indføre først?
5. Hvem ejer registret over teknisk gæld, og hvordan vinder nedbetaling faktisk kapacitet mod featurearbejde?

## Vigtigste pointer

- Refaktorering bevarer adfærd; hold den strengt adskilt fra adfærdsændring, i separate commits.
- En pålidelig testsuite er forudsætningen for sikker refaktorering, og karakteriseringstests giver legacy-kode en.
- Arbejd i små, navngivne, reversible skridt, foretræk opportunistisk oprydning, og brug strangler fig eller branch by abstraction til stor strukturel ændring.
- Gør teknisk gæld synlig, adskil hovedstol fra rente, og finansiér nedbetaling som jævn kapacitet frem for heltemod.
- Mål intern kvalitet for at guide dømmekraft, aldrig som et mål at manipulere, og refaktorér ikke kode, der er stabil eller sat til pensionering.

## Referencer og videre læsning

- Martin Fowler, *Refactoring: Improving the Design of Existing Code*, second edition
- Michael Feathers, *Working Effectively with Legacy Code*
- Ward Cunningham, *The WyCash Portfolio Management System* (OOPSLA 1992 experience report, origin of the debt metaphor)
- Martin Fowler, "TechnicalDebtQuadrant" and "StranglerFigApplication" (martinfowler.com)
- Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
