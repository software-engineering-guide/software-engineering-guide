# 3.1 Grundlæggende arkitektur

## Overblik og motivation

[Softwarearkitektur](https://en.wikipedia.org/wiki/Software_architecture) er det sæt betydelige designbeslutninger, der er dyre at ændre: strukturen af de store komponenter, relationerne mellem dem og de egenskaber, hele systemet skal udvise. Tænk på den som den fælles mentale model, der lader mange mennesker bygge ét sammenhængende produkt. I et lille team kan arkitektur bo i nogle få hoveder og udvikle sig undervejs. I en stor organisation (hundredvis af ingeniører, dusinvis af teams, flere produkter, år af køreplan) bliver arkitektur det, der holder alle koordinerede. Når den er klar, bevæger teams sig uafhængigt uden at støde sammen. Når den er vag, bliver hver afhængighed på tværs af teams en forhandling, og hver hændelse et arkæologiprojekt.

For virksomheder og det offentlige betyder grundlagene endnu mere, fordi systemerne er langlivede, stærkt regulerede og delt på tværs af afdelinger. Et skattesystem, en ydelsesplatform, en national sundhedsjournal eller en banks kernehovedbog vil overleve karrieren hos dem, der byggede den. De beslutninger, du træffer i dag om kobling, dataejerskab og [kvalitetsegenskaber](https://en.wikipedia.org/wiki/List_of_system_quality_attributes), begrænser, hvad der er muligt i et årti eller mere. Tilsynsmyndigheder og revisorer forventer i stigende grad dokumenteret, forsvarlig arkitektur: dokumentation for, at pålidelighed, sikkerhed, privatliv og tilgængelighed var designet ind, ikke skruet på. At få grundlagene rigtige er ikke akademisk. Det er forskellen mellem en platform, der tilpasser sig nye påbud, og en, der må genopbygges fra bunden.

Dette kapitel dækker de varige grundlag, der overlever teknologimoder: kvalitetsegenskaber ("-iliteterne"), arkitektonisk signifikante krav, fitness functions og evolutionær arkitektur, let dokumentation med [C4](https://en.wikipedia.org/wiki/C4_model) og arc42 samt struktureret afvejningsanalyse. Det er de værktøjer, der lader et stort team ræsonnere om arkitektur med vilje frem for ved et tilfælde.

## Grundprincipper

- **Arkitektur handler om afvejninger, ikke rigtige svar.** Hver betydelig beslutning bytter én kvalitet for en anden; opgaven er at træffe disse valg bevidst og gennemsigtigt.
- **Kvalitetsegenskaber er krav.** Ydeevne, tilgængelighed, sikkerhed og vedligeholdelighed skal specificeres med samme stringens som features, ellers ofres de under deadlinepres.
- **Ikke hvert krav er arkitektonisk signifikant.** Fokusér knap designopmærksomhed på de krav, der former struktur, er svære at ændre eller bærer høj risiko.
- **Arkitektur skal kunne udvikle sig.** Stort design på forhånd fejler, fordi viden er lavest i begyndelsen; design inkrementelt og beskyt nøgleegenskaber med automatiske kontroller.
- **Dokumentér beslutninger, ikke kun diagrammer.** Begrundelsen bag et valg (og de afviste muligheder) er mere værd end et billede af resultatet.
- **Gør arkitekturen læselig for dem, der ikke skabte den.** Nyansatte, revisorer og fremtidige vedligeholdere skal kunne rekonstruere hensigten.
- **Udskyd de beslutninger, du kan; træf dem, du må.** Hold muligheder åbne, hvor ændring er billig; forpligt dig tidligt kun, hvor sen forpligtelse er dyr.

## Anbefalinger

### Specificér kvalitetsegenskaber som målbare scenarier

Vage mål som "systemet bør være hurtigt" eller "højt tilgængeligt" kan ikke testes eller håndhæves. Skriv i stedet hver kvalitetsegenskab som et konkret scenarie med en stimulus, en kontekst og et målbart svar: "Når samtidige brugere ved spidsbelastning når 50.000, afsluttes 95 % af søgeanmodninger inden for 300 ms." Dæk de egenskaber, der betyder noget for dit domæne: tilgængelighed, ydeevne, skalerbarhed, sikkerhed, vedligeholdelighed, observerbarhed, handicaptilgængelighed, portabilitet og omkostningseffektivitet. Rangér dem højt, for du kan ikke maksimere dem alle på én gang. Et system tunet til maksimal konsistens vil ikke også være maksimalt tilgængeligt.

### Identificér arkitektonisk signifikante krav (ASR'er)

Afsæt tid til at adskille ASR'er fra almindelige krav. Et krav er arkitektonisk signifikant, hvis det rører mange komponenter, er dyrt at opfylde, pålægger en streng begrænsning eller er teknisk risikabelt. Regulatoriske påbud (dataresidens, opbevaring, reviderbarhed), scenarier med høj belastning, integration med legacy-registersystemer og hårde sikkerhedsgrænser er som regel ASR'er. Hold en kort, levende liste over dem, og spor større designbeslutninger tilbage til den liste, så gennemgangere kan se, hvorfor arkitekturen ser ud, som den gør.

### Adoptér evolutionær arkitektur og fitness functions

Behandl arkitektur som noget, der ændrer sig skridt for skridt i styrede retninger, ikke som en fast tegning. En **fitness function** er en automatisk, objektiv test af, at en bestemt arkitektonisk egenskab holder: en kontrol ved byggetid af, at intet modul importerer fra et forbudt lag, en ydeevnetest der lader pipelinen fejle, hvis p99-latens regredierer, en sikkerhedsscanning der blokerer kendt sårbare afhængigheder, en test der bekræfter, at ingen tjeneste holder en direkte forbindelse til en anden tjenestes database. Fitness functions forvandler arkitektonisk hensigt til rækværk, der håndhæves løbende: den eneste måde at holde den hensigt i live på tværs af et stort, skiftende team.

### Dokumentér med C4 og arc42

Brug **C4-modellen** til at beskrive struktur i fire zoomniveauer (System Context, Containers, Components og Code), så hver målgruppe læser det niveau, der passer, og intet enkelt diagram skal sige det hele. Brug **arc42** som skabelon til den omgivende fortælling: mål, begrænsninger, kontekst, løsningsstrategi, byggeklodser, runtime-scenarier, udrulning, tværgående anliggender, beslutninger og risici. Registrér enkelte beslutninger som korte **[arkitekturbeslutningsregistre (ADR'er)](https://en.wikipedia.org/wiki/Architectural_decision)**: kontekst, beslutning, status og konsekvenser, én fil pr. beslutning, versioneret sammen med koden. Hvis du kun adopterer én dokumentationsvane, så gør det ADR'er: de betaler sig mere end noget andet for store teams.

### Kør struktureret afvejningsanalyse, og driv design efter risiko

For højrisikosystemer så brug en metode som **[Architecture Tradeoff Analysis Method (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** til at veje kandidatarkitekturer mod prioriterede scenarier for kvalitetsegenskaber. Den bringer følsomhedspunkter (hvor en beslutning stærkt påvirker én egenskab) og afvejningspunkter (hvor den påvirker flere) frem. For en lettere berøring så adoptér **risikodrevet design**: brug designindsats i forhold til risiko. Lavrisiko, velforståede dele har brug for lidt ceremoni. Nye, højkonsekvente eller uigenkaldelige beslutninger fortjener prototyper, spikes og formel gennemgang.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Tung arkitektur på forhånd | Koordinationsklarhed; færre sene overraskelser i programmer med fast omfang | Beslutninger truffet når viden er lavest; langsom; skrøbelig over for ændring |
| Fremvoksende / evolutionær arkitektur | Tilpasser sig læring; mindre spild; understøtter hurtig levering | Risiko for drift uden fitness functions; kræver stærk ingeniørdisciplin |
| Formel ATAM-lignende evaluering | Stringent, reviderbar, bringer skjulte konflikter frem | Tids- og ekspertisekrævende; overkill til små ændringer |
| Lette ADR'er + C4 | Billige, læselige, inkrementelle, skalerer til mange teams | Kun så gode som disciplinen til at holde dem aktuelle |

Den centrale spænding er mellem sikkerhed og tilpasningsevne. Offentlige programmer til fast pris og sikkerhedskritiske systemer læner sig mod mere stringens på forhånd og formel evaluering, fordi omkostningen ved sen ændring eller fejl er enorm. Hurtigt bevægende produktorganisationer læner sig mod evolutionære tilgange bevogtet af automatisering. De fleste store organisationer har brug for begge: tungere styring af de uigenkaldelige, højkonsekvente beslutninger og tværgående anliggender og lettere, fremvoksende design alle andre steder. Begge ekstremer fejler på hver sin måde: overarkitektur spilder år og leverer intet, mens underarkitektur producerer en sammenfiltring, der ikke kan skalere eller revideres.

## Spørgsmål til drøftelse med dit team

1. **Når to af jeres kvalitetsegenskaber kolliderer under belastning, hvilken vinder, og har I skrevet den prioriteringsrækkefølge ned?** Hver arkitektur tvinger afvejninger: maksimal konsistens underminerer tilgængelighed, stram sikkerhed tilføjer latens, aggressiv caching kæmper mod reviderbarhed. I et stort team er faren, at forskellige hold stille antager forskellige prioriteter, så ét optimerer for gennemløb, mens et andet vogter streng konsistens, og konflikten kun dukker op under en hændelse. I virksomheds- og offentlige sammenhænge vil en tilsynsmyndighed spørge, hvilken egenskab I beskyttede og hvorfor, så rangeringen må være eksplicit og forsvarlig frem for folklore. Tag jeres kvalitetsscenarier med og rangér dem højt mod hinanden, par for par, til rækkefølgen er utvetydig. Kod derefter vinderen ind som en fitness function, så prioriteten holder under deadlinepres i stedet for at eroderes.

2. **Hvilke af jeres seneste beslutninger var envejsdøre, og fik de mere granskning end tovejsdørene?** Risikodrevet design siger, at I skal bruge designindsats i forhold til, hvor svær en beslutning er at gøre om, men de fleste teams gennemgår hver ændring med nogenlunde samme ceremoni. Det spilder opmærksomhed på billige, reversible valg, mens uigenkaldelige (en datamodel bagt ind i en juridisk post, en offentlig API-kontrakt, et centralt datalager) glider igennem med for lidt udfordring. Træk sidste kvartals betydelige beslutninger og sortér dem efter reversibilitet, og spørg så, om de uigenkaldelige fik prototyper, spikes eller formel gennemgang. I langlivede virksomheds- og offentlige systemer akkumuleres omkostningen ved en forkert envejsdør i et årti, så den ekstra stringens betaler sig mange gange. Afstem vægten af jeres proces efter beslutningens reversibilitet, ikke efter diffens størrelse.

3. **Til jeres næste højrisiko, svært reversible beslutning, hvem skal være i rummet, og mod hvilke scenarier vil I score mulighederne?** En struktureret afvejningsgennemgang i ATAM-stil tjener sin omkostning, når en beslutning er uigenkaldelig og rører flere kvalitetsegenskaber på én gang, og dens kraft kommer fra de tilstedeværende: levering, sikkerhed, drift og de politik- eller forretningsejere, der mærker konsekvenserne. Udelad én af de stemmer, og I opdager konflikten efter bygningen, som et cachingvalg stille kan bryde et krav om reviderbarhed. Tag de prioriterede kvalitetsscenarier med som scoringsskema, og led efter følsomhedspunkter, hvor en mulighed svinger en enkelt egenskab hårdt, og afvejningspunkter, hvor den flytter flere. Det output, I vil have, er en kort ADR, der registrerer de muligheder, I afviste, og hvorfor, så begrundelsen overlever de mennesker, der traf den. Hvis ingen kommende beslutning synes at berettige dette, er det i sig selv værd at tjekke, for et stort program uden uigenkaldelige beslutninger forude kigger som regel ikke langt nok frem.

4. **Hvis en nyansat eller en ekstern revisor kun havde jeres skrevne arkitektur, kunne vedkommende så rekonstruere, hvorfor systemet har den form, det har, og hvornår testede I det sidst?** Arkitektur, der bor i nogle få seniore hoveder, er et enkelt fejlpunkt: når de mennesker går videre, forsvinder begrundelsen bag hver svært reversibel beslutning med dem, og det næste team lærer den igen gennem hændelser. For en stor organisation er arkitekturens læselighed (C4-diagrammer, der matcher virkeligheden, en arc42-fortælling, ADR'er der registrerer afviste muligheder) det, der lader dusinvis af teams ræsonnere om det samme system uden et møde. Tag en nylig ADR og et aktuelt diagram med, aflever dem til nogen, der ikke byggede komponenten, og se, hvor langt vedkommende kommer, før de må spørge et menneske. I virksomheds- og offentlige sammenhænge vil en revisor gøre netop den øvelse, og dokumentation, der beskriver sidste års system, er værre end ingen, fordi den vildleder netop de mennesker, der skal certificere det. Behandl den skrevne optegnelses friskhed som en målbar egenskab, og sæt en fitness function eller en gennemgangskadence bag at holde den sand.

5. **Hvilke af jeres arkitektoniske egenskaber er i dag beskyttet af en automatisk fitness function, og hvilke afhænger stadig af, at alle husker reglen?** Hensigt, der kun bor på en wikiside eller i en gennemgangers hukommelse, eroderes i det øjeblik, en deadline ankommer, fordi lagdelingsreglen, grænsen om ingen fælles database og latensbudgettet er netop det, teams skærer under pres. I en stor, hurtigt skiftende kodebase er den eneste hensigt, der overlever, den hensigt, et build håndhæver, så hullet mellem de egenskaber, I påstår, og dem, I faktisk kontrollerer, er jeres reelle arkitektoniske risiko. List jeres betydelige egenskaber, markér hver som håndhævet, manuelt gennemgået eller ubeskyttet, og tag de sidste tre gange med, hvor en gennemgang fangede drift, som en fitness function kunne have fanget tidligere. I regulerede og offentlige systemer betyder dette dobbelt, fordi en tilsynsmyndighed vil spørge ikke om I havde til hensigt dataresidens eller reviderbarhed, men hvordan I beviser, at det holdt løbende, og en grøn pipeline er et langt stærkere svar end et politikdokument. Prioritér at automatisere de egenskaber, hvis svigt både er sandsynligt og dyrt, og accepter, at nogle forbliver manuelle.

6. **Når I afgør, om et krav er arkitektonisk signifikant, hvem træffer det kald, og hvordan holder I ASR-listen fra at blive enten alt eller intet?** Værdien af at navngive arkitektonisk signifikante krav kommer af selektivitet: behandl hvert krav som signifikant, og design går i stå, behandl ingen som signifikante, og de strukturelle, risikable, svært ændrelige slipper igennem ubeskyttet. I et stort team er fristelsen at lade hvert hold afgøre lokalt, hvilket producerer inkonsistente barrer og overraskelser på tværs af teams, når én gruppes "mindre" valg begrænser en andens struktur. Tag jeres nuværende ASR-liste med, de kriterier I brugte (rører mange komponenter, dyrt at opfylde, streng begrænsning, teknisk risikabelt) og nogle få grænsetilfælde at teste grænsen højt på. For virksomheder og det offentlige er regulatoriske påbud som dataresidens, opbevaring og reviderbarhed næsten altid signifikante og ufravigelige, så navngiv, hvem der ejer listen, hvordan den gennemgås, og hvordan en beslutning om at tilføje eller droppe en ASR registreres, for en ASR, ingen styrer, er et krav, ingen vil forsvare under granskning.

## Sektorperspektiv

**Startup.** Hold ceremonien nær nul og optegnelsen nær fuldstændig. Spring formelle ATAM-workshops og tunge skabeloner over, men skriv stadig et dusin korte ADR'er til de valg, der ville være smertefulde at rulle tilbage (datalager, monolit versus tjenester, autentificeringsudbyder), og fastlås de to eller tre kvalitetsscenarier, dine tidligste kunder faktisk mærker. Din knappe ressource er ingeniørernes opmærksomhed, så beskyt kun de egenskaber, hvis svigt ville sænke dig, såsom tenantisolation, og lad alt andet forblive fremvoksende og billigt at ændre.

**Lille virksomhed.** Uden en dedikeret arkitekt og med et stramt budget så støt dig til de grundlag, der koster næsten intet: navngiv din håndfuld kvalitetsegenskaber som konkrete tal, skriv ADR'er til alt, du ville have svært ved at gøre om, og lad din valgte platform eller leverandør bære de tunge strukturelle beslutninger. Foretræk at købe en veltilsluttet stak frem for at bygge skræddersyet infrastruktur, og behandl leverandørens dokumenterede arkitektur som en begrænsning, du arver, frem for en du skal forfatte fra bunden.

**Stor virksomhed.** Udfordringen er sammenhæng på tværs af mange teams og års køreplan, så invester i fælles maskineri: et arkitekturgilde, et fælles sæt kvalitetsscenarier, ADR'er opbevaret ved siden af koden og fitness functions i CI, der håndhæver grænser, ingen enkelt gennemganger kunne overvåge i stor skala. Brug struktureret afvejningsanalyse til de uigenkaldelige, tværgående beslutninger, behold C4-diagrammer som det fælles kort i designgennemgange, og styr ASR-listen centralt, så grupper holder op med at træffe lokalt fornuftige valg, der kolliderer globalt.

**Offentlig sektor.** Langlivede, regulerede systemer gør dokumenteret, forsvarlig arkitektur til et indkøbs- og ansvarlighedskrav, ikke en finesse. Behandl dataresidens, opbevaring, reviderbarhed og handicaptilgængelighed som arkitektonisk signifikante krav skrevet ind i en arc42-beskrivelse, revisorer kan læse direkte, og kør lette afvejningsworkshops, der inkluderer politik- og sikkerhedsansvarlige, så konflikter (såsom caching versus reviderbarhed) dukker op på papiret før kode. Hold begrundelsessporet fuldstændigt nok til, at en ansvarlig embedsmand kan vise rettidig omhu, og foretræk arkitekturer med klare udgangsmuligheder frem for dem, der låser et offentligt organ til en enkelt leverandør i et årti.

## Eksempler

**Startup.** Et SaaS-team på seks personer i seed-fasen holder sin arkitektur i et fælles dokument frem for en formel proces, men skriver stadig de beslutninger ned, der ville være smertefulde at gøre om. De registrerer omkring et dusin ADR'er (hvorfor Postgres frem for et dokumentlager, hvorfor en modulær monolit frem for tjenester, hvorfor de valgte deres autentificeringsudbyder) og fastlåser to kvalitetsscenarier, der faktisk betyder noget for tidlige kunder: "en tilmelding gennemføres på under to sekunder" og "ingen kunde kan nogensinde læse en anden tenants data." Da de ansætter deres syvende og ottende ingeniør, lader disse noter de nyankomne levere i deres første uge i stedet for at afbryde alle for at spørge, hvorfor tingene er, som de er.

**Stor virksomhed.** En multinational bank konsoliderer tolv regionale betalingssystemer, så den opretter et lille arkitekturgilde. Gildet definerer otte kvalitetsscenarier (herunder "behandl 10.000 transaktioner i sekundet uden tabte transaktioner" og "genopret en region på 15 minutter"), fanger omkring fyrre ADR'er og håndhæver fitness functions i CI ([continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)): ingen tjeneste må skrive til et andet domænes database, alle kald mellem tjenester skal spores, og enhver afhængighed med en kritisk [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Common Vulnerabilities and Exposures) får bygget til at fejle. C4-kontekst- og containerdiagrammerne bliver det fælles kort i hver designgennemgang, og uenigheder om integration på tværs af teams falder kraftigt.

**Offentlig sektor.** Et nationalt agentur moderniserer en ydelsesplatform, og loven kræver, at det garanterer dataresidens, syv års reviderbarhed og tilgængelighedsoverensstemmelse. Dets arkitekter behandler disse som ASR'er og skriver dem ind i en arc42-beskrivelse, som revisorer gennemgår direkte. De kører en let ATAM-workshop med leveringsteams, sikkerhed og politikansvarlige for at sammenligne to kandidatarkitekturer, og opdager, at det foretrukne designs cachingstrategi er i konflikt med kravet om reviderbarhed. At fange den afvejning på papiret, før en linje kode, sparer måneders omarbejde og giver den ansvarlige minister dokumenteret bevis for rettidig omhu.

## Business case: motivation, ROI og TCO

Afkastet af arkitekturgrundlag er mest undgået omkostning, hvilket gør det let at underfinansiere og dyrt at springe over. Omkostningen ved at indføre dem er beskeden: nogle få erfarne arkitekters tid, nogle workshops, en dokumentationsskabelon og noget CI-investering i fitness functions, som regel en lille éncifret procent af et programs budget. Omkostningen ved *ikke* at indføre dem ankommer senere og til en præmie: omarbejde, når en ikke-specificeret kvalitetsegenskab svigter i produktion, nød-replatforming, når en udokumenteret kobling blokerer en påbudt ændring, langvarige hændelser, fordi ingen forstår systemet, og dumpede revisioner, der standser levering eller udløser bøder.

For ledelsen så ram sagen ind omkring optionalitet og risiko. Gode arkitekturgrundlag sænker omkostningen ved fremtidig ændring (en direkte løftestang på leveringshastighed og totale ejeromkostninger over et årti langt systemliv), reducerer hvor ofte og hvor længe alvorlige hændelser varer og producerer det dokumentationsspor, tilsynsmyndigheder og revisorer nu kræver. ADR-vanen alene betaler sig tilbage første gang, et nyt ledelsesteam spørger "hvorfor byggede vi det sådan?" og får et svar på minutter i stedet for en retsmedicinsk undersøgelse. Sæt tal på, hvor I kan: vej omkostningen ved én større undgået rearkitektur, eller én undgået dumpet revision, mod den lille løbende omkostning ved praksisserne.

## Anti-mønstre og faldgruber

- **Elfenbenstårnsarkitektur.** Arkitekter, der producerer diagrammer, men aldrig rører kode eller taler med leveringsteams; deres designs ignoreres eller kan ikke bygges.
- **Kvalitetsegenskaber som tillægsord.** "Skalerbar, sikker, pålidelig" uden tal, uden scenarier og derfor uden måde at verificere eller afveje på.
- **Stort design på forhånd.** At forpligte sig til hver detalje før den første kodelinje og låse beslutninger, når forståelsen er svagest.
- **Dokumentation, der lyver.** Diagrammer, der beskriver sidste års system; værre end ingen, fordi de vildleder.
- **CV-drevet design.** At vælge teknologier for at bygge karrierer frem for at opfylde ASR'er.
- **Forgyldning.** At konstruere til skala, fleksibilitet eller generalitet, kravene aldrig bad om, hvilket tilføjer omkostning og kompleksitet permanent.
- **Intet arkitektonisk rækværk.** At stole på gode intentioner i stedet for fitness functions for at bevare struktur på tværs af et stort team.

## Modenhedsmodel

- **Niveau 1: Opstart.** Arkitektur er implicit og bor i enkeltpersoners hoveder. Ingen dokumenterede kvalitetsegenskaber, ingen ADR'er, ingen fælles diagrammer. Struktur opdages under hændelser, og hver afhængighed på tværs af teams genforhandles fra bunden.
- **Niveau 2: Udvikling.** Nogle teams skriver de beslutninger ned, der ville gøre ondt at gøre om, og skitserer nøglediagrammer, men praksis er inkonsistent: ét hold fører ADR'er, mens et andet ikke fører nogen, kvalitetsegenskaber navngives som tillægsord frem for målbare scenarier, og dokumentation driver forældet mellem projekter.
- **Niveau 3: Standardisering.** Kvalitetsscenarier og arkitektonisk signifikante krav er specificeret og prioriteret efter en dokumenteret standard for hele organisationen. ADR'er er rutine og opbevares ved siden af koden, C4- og arc42-dokumentation vedligeholdes efter en fælles skabelon, og strukturerede afvejningsgennemgange er påkrævet for betydelige beslutninger i alle teams.
- **Niveau 4: Styring.** Arkitekturen måles mod baselines frem for blot at blive hævdet. Fitness functions i CI rapporterer om egenskaber som p99-latens, lagdelingsovertrædelser, usporede kald og sårbare afhængigheder; ADR-dækning og dokumentationsfriskhed følges som målinger; afvejningsgennemgange scorer muligheder mod de prioriterede scenarier; og drift mod aftalte baselines udløser en defineret respons frem for en overraskelse. Revisorer kan støtte sig til målt dokumentation frem for fortælling alene.
- **Niveau 5: Orkestrering.** Arkitekturen udvikler sig løbende og adaptivt i hele organisationen. Data fra fitness functions og hændelser føder tilbage i, hvilke egenskaber der betyder noget, og hvor designindsatsen går hen; ASR-lister, kvalitetsprioriteter og rækværk genafgrænses, efterhånden som påbud og risiko skifter; og praksis er integreret med leverings-, sikkerheds- og risikoplanlægning, så platformen tilpasser sig nye krav i stedet for at blive genopbygget fra bunden.

## Idéer til drøftelse

1. Hvilke tre kvalitetsegenskaber er reelt ufravigelige for jeres mest kritiske system, og kan I angive hver som et målbart scenarie i dag?
2. Hvordan afgør I, hvornår en beslutning er "arkitektonisk signifikant" nok til at berettige en ADR frem for blot at gøre det?
3. Hvor ville fitness functions fange drift, som jeres nuværende kodegennemgang overser?
4. Overarkitekterer eller underarkitekterer jeres organisation, og hvilken dokumentation fortæller jer hvad?
5. Hvem er ansvarlig for arkitektur i en team-af-teams-struktur, og hvordan undgår I både elfenbenstårne og total anarki?
6. Hvordan ville en ekstern revisor rekonstruere hensigten med jeres arkitektur ud fra det, der er skrevet ned i dag?

## Vigtigste pointer

- Arkitektur er det sæt beslutninger, der er dyre at gøre om; træf disse afvejninger bevidst og registrér dem.
- Specificér kvalitetsegenskaber som målbare scenarier og identificér de arkitektonisk signifikante krav, der former struktur.
- Design inkrementelt og beskyt centrale arkitektoniske egenskaber med automatiske fitness functions.
- Dokumentér let, men sandfærdigt, med C4-diagrammer, en arc42-fortælling og ADR'er pr. beslutning opbevaret ved siden af koden.
- Afstem stringens efter risiko: tung analyse til uigenkaldelige, højkonsekvente beslutninger; let proces alle andre steder.
- Business casen er undgået omarbejde, kortere hændelser, hurtigere fremtidig ændring og revisionsparat dokumentation.

## Referencer og videre læsning

- Len Bass, Paul Clements, and Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (and the C4 model)
- Mark Richards and Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (the ADR pattern)
- Gernot Starke and Peter Hruschka, *arc42* documentation template
- Paul Clements et al., *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
