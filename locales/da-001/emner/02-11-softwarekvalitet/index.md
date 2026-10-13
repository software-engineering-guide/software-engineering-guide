# 2.11 Softwarekvalitet

## Overblik og motivation

[Softwarekvalitet](https://en.wikipedia.org/wiki/Software_quality) er, hvor godt et system opfylder angivne behov og rimelige forventninger. Det betyder mere end, om det virker: det betyder, om systemet er pålideligt, sikkert, vedligeholdeligt, brugbart, ydedygtigt og egnet til sit formål over tid. Kvalitet er bredere end test. Test (kapitel 2.4) er én aktivitet, der afslører fejl. Kvalitet er hele disciplinen at bygge det rigtige godt og at vide, med dokumentation, at du har gjort det. Et system kan bestå hver test og stadig være af lav kvalitet, hvis det er uvedligeholdeligt, utilgængeligt eller dårligt egnet til det, brugerne faktisk har brug for.

I et stort team kan kvalitet ikke bo i ét menneskes hoved eller ét teams vaner. Hundredvis af ingeniører, flere produkter og langlivede systemer har brug for en fælles definition af kvalitet, eksplicitte processer til at sikre den og målinger, der fortæller, om den bliver bedre eller dårligere. Uden det bliver "kvalitet" en vag ambition, der taber hver diskussion til en deadline, og fejl hobes op, til ændring bliver langsom og risikabel.

I virksomheds- og offentlige sammenhænge stiger indsatsen. Regulerede, sikkerhedskritiske og borgervendte systemer skal påvise kvalitet, ikke blot hævde den: dokumenterede processer, sporbar dokumentation og uafhængig verifikation er ofte obligatoriske. Dårlig kvalitet bærer direkte økonomiske, juridiske og omdømmemæssige omkostninger, og i nogle domæner bringer den mennesker i fare. En bevidst kvalitetsdisciplin, bygget af modeller, processer, måling og kultur, er det, der forvandler kvalitet fra et tilfælde til et styret resultat.

## Grundprincipper

- Kvalitet er egnethed til formålet plus overensstemmelse med krav; definér begge eksplicit.
- Kvalitet bygges ind, ikke testes ind; verifikation finder fejl, men forebyggelse undgår dem.
- Skeln mellem [kvalitetssikring](https://en.wikipedia.org/wiki/Quality_assurance) (er vores processer sunde?) og [kvalitetskontrol](https://en.wikipedia.org/wiki/Quality_control) (er dette produkt godt?).
- Verifikation spørger "byggede vi det rigtigt?"; validering spørger "byggede vi det rigtige?"
- Mål kvalitet med et lille sæt meningsfulde målinger; behandl målinger som signaler, ikke mål.
- Omkostningen ved en fejl stiger, jo senere den findes, så flyt kvalitetsaktiviteter tidligere.
- Kvalitet er en egenskab ved hele organisationen og dens kultur, ikke en port til sidst.

## Anbefalinger

### Adoptér en fælles kvalitetsmodel som ISO/IEC 25010

Giv din organisation et fælles ordforråd for kvalitet ved at adoptere en anerkendt produktkvalitetsmodel. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) definerer egenskaber herunder funktionel egnethed, ydeevneeffektivitet, kompatibilitet, brugbarhed, pålidelighed, sikkerhed, vedligeholdelighed og portabilitet. Brug den til at gøre kvalitet konkret: for hvert system så beslut, hvilke egenskaber der betyder mest, og hvad "godt nok" betyder for hver. Disse produktkvalitetsegenskaber er de samme **kvalitetsegenskaber**, der driver arkitekturen (kapitel 3.1). Kvalitet og arkitektur er to synsvinkler på ét anliggende, så lad dem dele én liste over prioriteter frem for to konkurrerende.

### Adskil kvalitetssikring fra kvalitetskontrol

Behandl kvalitetssikring (QA) og kvalitetskontrol (QC) som adskilte, men komplementære aktiviteter. QA er procesorienteret og forebyggende: den forbedrer den måde, arbejdet udføres på, gennem standarder, gennemgange, definitioner af færdig og uddannelse, så fejl er mindre tilbøjelige til at opstå i første omgang. QC er produktorienteret og opdagende: den inspicerer faktiske arbejdsprodukter, såsom test, [kodegennemgang](https://en.wikipedia.org/wiki/Code_review) og revisioner, for at fange fejl, der kom ind. En moden organisation investerer i begge, men læner sig mod QA, fordi det er billigere at forebygge fejl end at finde og rette dem.

### Kør eksplicitte softwarekvalitetsstyringsprocesser

Gør kvalitet til en styret proces, ikke et stille håb. For betydeligt arbejde så skriv en kvalitetsplan, der angiver de ønskede kvalitetsegenskaber, sikrings- og kontrolaktiviteterne, acceptkriterierne og hvem der er ansvarlig. Væv den ind i den praksis, du allerede har: kodegennemgang (kapitel 2.5) som både en kontrol og en måde at dele viden på, teststrategi (kapitel 2.4) som det automatiske sikkerhedsnet og [statisk analyse](https://en.wikipedia.org/wiki/Static_program_analysis) som løbende inspektion. Gennemgå kvalitetsdata regelmæssigt og handl på tendenser i stedet for kun at reagere på hændelser.

### Praktisér verifikation og validering som adskilte discipliner

Verifikation bekræfter, at arbejdsprodukter opfylder deres specifikationer, så de rigtige input til hvert trin giver de rigtige output, gennem gennemgange, statisk analyse og test mod krav. Validering bekræfter, at det færdige system faktisk opfylder brugerbehov og tilsigtet brug, gennem brugertest, accepttest, piloter og feedback fra marken. Du har brug for begge. Et system kan være korrekt mod en mangelfuld specifikation (verificeret, men ikke gyldigt), eller det kan adressere et reelt behov og stadig indeholde fejl (gyldigt, men ikke verificeret). I regulerede miljøer kan uafhængig [verifikation og validering](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) af en part adskilt fra udviklerne være påkrævet.

### Mål kvalitet med meningsfulde målinger

Vælg et lille sæt målinger, der afspejler kvalitetsresultater og deres drivere, og hold øje med dem over tid. Nyttige mål omfatter fejltæthed, andel undsluppne fejl (fejl fundet i produktion versus før udgivelse), middeltid til at opdage og til at rette, andel fejlslagne ændringer, kodesundhedssignaler som kompleksitet og duplikering og valideringssignaler som brugerrapporterede problemer og tilgængelighedsoverensstemmelse. Hold dig fra forfængeligheds- og manipulerbare målinger: en måling, der bliver et mål, holder op med at måle virkeligheden. Par tallene med kvalitative signaler fra gennemgange og brugerfeedback.

### Karakterisér og styr fejl systematisk

Behandl fejl som data, ikke blot som brande at slukke. Klassificér dem efter alvorlighed, type og grundårsag. Følg dem fra opdagelse til løsning. Led efter mønstre, så du kan forebygge gentagelse. Brug teknikker som [grundårsagsanalyse](https://en.wikipedia.org/wiki/Root_cause_analysis) og fejlkategorisering til at skelne enkeltstående fejl fra systemiske svagheder. Før det, du lærer, tilbage i QA, gennem opdaterede standarder, tilføjede tests og forbedrede gennemgange, så den samme klasse af fejl ikke vender tilbage. En fejl rettet uden at forstå dens årsag er en fejl, du har inviteret tilbage.

### Styr kvalitetens omkostning bevidst

Forstå kvalitetsøkonomi gennem de klassiske kategorier: forebyggelsesomkostninger (uddannelse, standarder, godt design, værktøj), vurderingsomkostninger (gennemgange, test, revisioner) og fejlomkostninger (intern omarbejdning før udgivelse samt eksterne fejl fundet af brugere, som koster langt mere). Flyt din investering mod forebyggelse og tidlig vurdering, fordi hver krone der investeres der undgår mange kroner i undgåede fejlomkostninger senere. Gør disse omkostninger synlige, så "vi har ikke tid til kvalitet" ses for det, det er: et valg om at bruge mere på fejl i stedet.

### Byg en kvalitetskultur

Gør kvalitet til alles ansvar, ejet af de teams, der bygger softwaren, frem for overdraget til en nedstrøms QA-afdeling, der inspicerer den til sidst. Ledere bør belønne kvalitetsresultater, gøre det trygt at rapportere fejl og nærved-hændelser og behandle kvalitetsdata som et læringsredskab frem for en pisk. En fejlfri tilgang til fejl bringer problemer frem i lyset tidligt. En bebrejdende tilgang skjuler dem, til de er dyre.

## Afvejninger: fordele og ulemper

| Praksis / valg | Fordele | Ulemper |
|---|---|---|
| Formel kvalitetsmodel (ISO 25010) | Fælles ordforråd; eksplicitte prioriteter | Overhead hvis anvendt dogmatisk |
| Tung kvalitetssikring (forebyggelse) | Færre fejl; lavere samlet omkostning | Investering på forhånd; langsommere at vise gevinst |
| Tung kvalitetskontrol (inspektion) | Fanger fejl, der slipper igennem | Dyr; finder fejl sent |
| Uafhængig V&V | Høj sikkerhed; objektiv | Kostbar; langsommere; kan føles konfronterende |
| Rige kvalitetsmålinger | Synlighed; tidlig advarsel | Risiko for manipulation; måleoverhead |
| Dedikeret QA-team | Fokus og ekspertise | Kan fralægge udviklere ansvar |
| Kvalitet ejet af teams | Ejerskab; hurtig feedback | Kræver disciplin og færdigheder overalt |

Den centrale afvejning er investering versus sikkerhed, formet af timing. Forebyggelse koster penge nu for at undgå større fejlomkostninger senere. Så det økonomisk rette kvalitetsniveau er ikke maksimum; det er det punkt, hvor grænseomkostningen ved mere sikring er lig med den fejlomkostning, den undgår. Det punkt ligger højt for sikkerhedskritiske systemer og lavere for interne værktøjer med lav indsats. Den anden tilbagevendende spænding er ejerskab. Centrale QA-grupper bygger ekspertise, men kan lade udviklere fralægge sig ansvar. Kvalitet ejet af teams bygger ejerskab, men kræver færdigheder og disciplin overalt.

## Spørgsmål til drøftelse med dit team

1. **Når den samme klasse af fejl dukker op to gange, kører vi så grundårsagsanalyse, eller retter vi den bare igen?** En fejl rettet uden at forstå dens årsag er en fejl, I har inviteret tilbage, og i et stort team kan den samme grundårsag dukke op på tværs af mange tjenester, før nogen forbinder prikkerne. At behandle fejl som data (klassificeret efter alvorlighed, type og årsag og derefter gravet i efter mønstre) er det, der adskiller et team, der bliver støt mere pålideligt, fra et, der bliver ved med at have travlt med at rette den samme fejl igen. Tag jeres fejlsporingssystem med til mødet og led efter tilbagevendende signaturer: hvor mange nylige hændelser deler en årsag, I aldrig adresserede systemisk? Svaret bør fodre forebyggelse, så en tilbagevendende årsag driver en opdateret standard, en ny fælles hjælper, en tilføjet test eller en bedre gennemgangstjekliste, for sådan forhindrer en rettelse ét sted hele klassen i at vende tilbage.

2. **Er det trygt i vores team at rapportere en fejl eller en nærved-hændelse, og hvad sker der med den, der rejser en?** Kvalitet er en egenskab ved kulturen, og en fejlfri tilgang bringer problemer frem i lyset tidligt, mens en bebrejdende skjuler dem, til de er dyre, hvilket i et reguleret eller borgervendt system kan betyde et offentligt svigt eller en bøde. Det betyder mest i stor skala, hvor den ingeniør, der er tættest på en risiko, ofte er junior, og incitamentet til at tie er stærkt. Tag ærlige signaler med: bliver nærved-hændelser logget og drøftet, eller forsvinder de? Navngiver efterbehandlinger årsager eller personer? Handlingen er at gøre kvalitetsdata til et læringsredskab frem for en pisk, belønne de mennesker, der bringer problemer frem, og køre fejlfri efterbehandlinger, for I kan ikke forebygge det, jeres team er bange for at rapportere.

3. **Kan validering faktisk standse en udgivelse, og hvem har den autoritet, når en deadline nærmer sig?** Verifikation (byggede vi det rigtigt?) og validering (byggede vi det rigtige?) er adskilte discipliner, og validering har kun tænder, hvis en dumpet tilgængelighedskontrol, en dumpet accepttest eller nedslående brugerresearch reelt kan blokere udgivelse. I virksomheds- og offentlige sammenhænge er dette ofte obligatorisk, nogle gange gennem uafhængig verifikation og validering af en part adskilt fra udviklerne, og "vi udgav det alligevel" er ikke et svar, et tilsynsorgan accepterer. Tag jeres seneste udgivelser med: har et kvalitetssignal nogensinde faktisk standset en, eller viger porten altid for datoen? Hvis validering aldrig har blokeret en udgivelse, er den dekoration, og rettelsen er at skrive acceptkriterier ind i kvalitetsplanen på forhånd, navngive, hvem der ejer go/no-go-beslutningen, og give den beslutning reel autoritet uafhængigt af leveringspresset.

4. **Kender vi faktisk vores omkostning ved dårlig kvalitet, og flytter vi bevidst udgifter fra fejl mod forebyggelse?** Omkostningen ved dårlig kvalitet (COPQ) er de penge, der tabes til intern omarbejdning, produktionshændelser, nødrettelser, supportbelastning, tabte brugere og bøder, og den er næsten altid større end de synlige udgifter til gennemgange og test. I et stort team er fejlomkostningerne spredt over hændelseskanaler, supportkøer og omarbejdning, ingen logger som omarbejdning, så de forbliver usynlige, til nogen lægger dem sammen. Spændingen er, at forebyggelse koster penge nu, i en budgetcyklus, for at undgå fejlomkostninger, der lander senere og på en andens budget, hvilket gør handlen let at udskyde for evigt. Tag reelle tal med: antal hændelser og omkostning, omarbejdstimer, andel undsluppne fejl og den nuværende fordeling af udgifter på forebyggelse, vurdering og fejl, og beslut derefter, om blandingen bør flytte tidligere. For virksomheds- og offentlige systemer, hvor det meste af livstidsomkostningen lander efter første udgivelse, så læg COPQ foran dem, der holder budgettet, for et tal, et tilsynsorgan kan se, er langt sværere at bytte væk end en vag appel til "kvalitet".

5. **Hvilke af vores kvalitetsmålinger er stille blevet til mål, og hvilken adfærd driver de nu?** En måling, der bliver et mål, holder op med at måle virkeligheden: jag en dækningsprocent, og I får tests skrevet for at flytte tallet, ikke tests der fanger fejl. I stor skala er det farligt, fordi et overskriftsdashboard delt på tværs af dusinvis af teams sætter incitamenterne for dem alle, og en manipulerbar måling spreder manipulationen overalt på én gang. Det modstridende hensyn er, at I stadig har brug for måling, så svaret er sjældent "drop målingen", men "par den med et modsignal og læs den sammen med kvalitativ dokumentation fra gennemgange og brugere". Tag jeres nuværende målesæt med og spørg for hver, hvad nogen under pres kunne gøre for at flytte den uden at forbedre kvaliteten, og om I har set det ske. I regulerede og borgervendte sammenhænge så vær særligt på vagt over for overensstemmelsesmålinger, der ser grønne ud, mens den underliggende validering (tilgængelighed, reelle brugerresultater) aldrig blev reelt udøvet, da en revisor til sidst vil teste virkeligheden bag tallet.

6. **Hvem ejer kvalitet her: de teams, der skriver koden, eller en separat gruppe til sidst, og hvad finansierer vi faktisk?** Ejerskab former alt nedstrøms, fordi en nedstrøms QA-silo lader udviklere fralægge sig ansvaret for den kode, de skriver, mens kvalitet ejet af teams bygger ejerskab på bekostning af at kræve færdigheder og disciplin i hvert team. I et stort team er dette ikke enten-eller: det bæredygtige mønster er som regel, at teams ejer kvalitet gennem kodegennemgang og automatiske tests, understøttet af en lille central gruppe, der vedligeholder standarder, kører kvalitetssikring som procesforbedring og coacher, frem for at inspicere kvalitet ind til sidst. Tag et ærligt kort med over, hvor kvalitetsarbejde i øjeblikket foregår, hvem der er ansvarlig, når en fejl slipper ud, og hvor budget og headcount faktisk sidder versus hvor retorikken siger, at kvalitet bor. For virksomheds- og offentlige organisationer så tilføj kravet om uafhængig verifikation og validering: nogle sikringsregimer påbyder en separat part, så beslut bevidst, hvilke kontroller der hører hjemme hos leveringsteamene, og hvilke der må forblive uafhængige for at opfylde revision.

## Sektorperspektiv

**Startup.** Hastighed betyder mere end ceremoni, så navngiv de to eller tre kvalitetsegenskaber, der faktisk beskytter dit produkt, som regel pålidelighed og vedligeholdelighed, og lad finpudsning vente. Ejer kvalitet i hele teamet med kodegennemgang og en beskeden automatisk testsuite frem for at opstille en separat QA-gruppe, du ikke kan bemande. Når den samme klasse af fejl dukker op to gange, så brug tyve minutter på grundårsagen og tilføj én fælles hjælper plus en test, så forebyggelse forbliver billig, og din andel af fejlslagne ændringer forbliver lav, mens du bevæger dig hurtigt.

**Lille virksomhed.** Uden en dedikeret kvalitetsspecialist og med et stramt budget så støt dig til kvalitet, der er bygget ind i de værktøjer og platforme, du køber, frem for en proces, du skal køre. Når du vælger software, så behandl leverandørens kvalitetsdokumentation som en del af købet: sikkerhedsholdning, tilgængelighed, supportens responsivitet og hvor ofte deres udgivelser går i stykker. Følg en håndfuld billige, ærlige signaler (produktionshændelser, kunderapporterede problemer, tid til at rette) i stedet for et omstændeligt målingsprogram, du ingen har til at vedligeholde.

**Stor virksomhed.** Arbejdet er ensartethed på tværs af mange teams: adoptér en fælles kvalitetsmodel som ISO/IEC 25010, adskil kvalitetssikring (proces) fra kvalitetskontrol (produkt), og kør omkostningsgennemgange af kvalitet, der flytter udgifter mod forebyggelse. Hold kvalitet ejet af leveringsteamene, understøttet af en lille central gruppe, der vedligeholder standarder og dashboards for andel undsluppne fejl, andel fejlslagne ændringer og kodesundhedstendenser. Standardisér ordforrådet og portene, så grupper holder op med at genopfinde kvalitetspraksis, mens teams får plads til at opfylde disse barrer på deres egen måde.

**Offentlig sektor.** Indkøb, åbenhed og offentlig ansvarlighed sætter rammen, så skriv kvalitetskrav ind i kontrakter og kræv dokumenteret, sporbar kvalitetsdokumentation frem for påstande. Forvent uafhængig verifikation og validering af en part adskilt fra udviklerne, obligatorisk tilgængelighedsoverensstemmelse og fejloptegnelser med alvorlighed og grundårsag opbevaret som del af revisionssporet. Rapportér tal for omkostning ved dårlig kvalitet (omarbejde, klager, tjenestesvigt) til tilsynsorganer, og giv validering reel autoritet til at blokere en udgivelse, der ville svigte de borgere, som afhænger af den.

## Eksempler

**Startup.** Et startup med fem medarbejdere beslutter, at pålidelighed og vedligeholdelighed er de kvalitetsegenskaber, der betyder noget for dets tidlige produkt, og lader pixelperfekt finpudsning vente. Kvalitet ejes af hele teamet: kodegennemgang og en beskeden automatisk testsuite er kontrollerne, og der er ingen separat QA-gruppe at aflevere fejl til. Da den samme klasse af fejl dukker op to gange, bruger de tyve minutter på et hurtigt blik på grundårsagen og tilføjer én fælles hjælper plus en test, så den holder op med at gentage sig i stedet for at blive rettet i hånden hver gang. Den lille vane med forebyggelse holder deres andel af fejlslagne ændringer lav, mens de stadig bevæger sig hurtigt.

**Stor virksomhed.** Et stort finansielt servicefirma adopterer ISO/IEC 25010 som sit kvalitetsordforråd og registrerer for hvert produkt målniveauer for pålidelighed, sikkerhed og vedligeholdelighed. Teams ejer kvalitet: kodegennemgang og automatiske tests er kontroller i pipelinen, mens en lille central gruppe kører QA ved at vedligeholde standarder og coache. Et kvalitetsdashboard følger andel undsluppne fejl, andel fejlslagne ændringer og kodesundhedstendenser. Fejl klassificeres og grundårsagsanalyseres, og tilbagevendende årsager driver opdateringer af fælles biblioteker og tjeklister. Ledelsen gennemgår omkostningsdata for kvalitet kvartalsvis og har flyttet udgifter mod forebyggelse, hvilket har skåret både produktionshændelser og omkostningen ved at rette dem.

**Offentlig sektor.** Et nationalt agentur, der leverer en borgervendt ydelsesplatform, arbejder under et sikringsregime, der kræver dokumenteret kvalitetsdokumentation. Det kører en formel kvalitetsstyringsproces med en kvalitetsplan pr. udgivelse samt uafhængig verifikation og validering af et team adskilt fra udviklerne. Verifikation kontrollerer hvert arbejdsprodukt mod krav sporet til politik. Validering omfatter test af tilgængelighedsoverensstemmelse og brugerresearch med rigtige borgere, og begge kan blokere en udgivelse. Fejl følges med alvorlighed og grundårsag som del af revisionssporet, og tal for omkostning ved dårlig kvalitet (omarbejde, klager og tjenestesvigt) går til tilsynsorganer for at retfærdiggøre fortsat investering i forebyggelse.

## Business case: motivation, ROI og TCO

Afkastet af kvalitet er lavere totale ejeromkostninger og jævn leveringshastighed. Omkostningen ved kvalitet har to sider. Det gode forbrug, forebyggelse og vurdering, er synligt og kontrollerbart: design, standarder, gennemgange, test og værktøj. Omkostningen ved dårlig kvalitet (COPQ) er større, men ofte skjult: intern omarbejdning, produktionshændelser, nødrettelser, kundesupport, tabte brugere, regulatoriske bøder og omdømmeskade. Undersøgelser, der går tilbage til Crosbys "Quality Is Free", har konsekvent fundet, at den samlede omkostning ved dårlig kvalitet overstiger omkostningen ved at forebygge den langt, og at fejl bliver langt dyrere, jo senere du fanger dem: et problem fundet i design koster en brøkdel af det samme problem fundet i produktion.

For ledelsen er argumentet ikke "brug mere på kvalitet." Det er "brug tidligere for at bruge mindre i alt." Kvantificér COPQ ud fra jeres egne data (antal hændelser og omkostning, omarbejdstimer, andel undsluppne fejl) og vis, hvordan forebyggelse og tidlig vurdering bringer den ned. Forbind kvalitet til forretningsresultater: pålidelighed fastholder kunder, vedligeholdelighed holder fremtidig ændring billig, og sikkerhed og tilgængelighed holder dig ude af juridiske problemer. I langlivede virksomheds- og offentlige systemer, hvor det meste af omkostningen lander efter første udgivelse, dominerer kvalitetens dimensioner vedligeholdelighed og pålidelighed livstidsomkostningen. Det gør tidlig kvalitetsinvestering til en af de beslutninger med størst løftestang, du kan træffe.

## Anti-mønstre og faldgruber

- **Kvalitet som en endelig port:** at inspicere kvalitet ind til sidst i stedet for at bygge den ind, så fejl findes, når de er dyrest.
- **At forveksle test med kvalitet:** at antage, at beståede tests betyder høj kvalitet, og ignorere vedligeholdelighed, brugbarhed og egnethed til formålet.
- **QA som separat silo:** et nedstrøms team, der "ejer kvalitet", og lader udviklere fralægge sig ansvaret for den kode, de skriver.
- **Målingsteater:** at jage dækningsprocenter eller fejlantal som mål, hvilket inviterer til manipulation og skjuler reel kvalitet.
- **Verifikation uden validering:** at bygge specifikationen korrekt uden nogensinde at tjekke, at specifikationen opfylder reelle behov.
- **Ingen grundårsagsanalyse:** at rette fejl enkeltvis uden at adressere den systemiske årsag, så den samme klasse gentager sig.
- **At ignorere omkostningen ved dårlig kvalitet:** at behandle kvalitet som ren omkostning, fordi fejlomkostninger er skjulte og umålte.

## Modenhedsmodel

**Niveau 1 (Opstart).** Kvalitet er udefineret og ad hoc. Den hviler på individuel flid, kontrolleres hovedsageligt ved manuel test til sidst, og fejl håndteres reaktivt, efterhånden som de dukker op. Der er ingen fælles model, ingen målinger og ingen skillelinje mellem sikring og kontrol.

**Niveau 2 (Udvikling).** Grundlæggende praksis dukker op: kodegennemgang, automatiske tests og et fejlsporingssystem. Nogle kvalitetsdata indsamles, men ujævnt, og hvert team gør det på sin egen måde. Kvalitet ses stadig mest som test, forebyggelse er minimal, verifikation sker, og validering er uformel.

**Niveau 3 (Standardisering).** Organisationen adopterer en fælles kvalitetsmodel (såsom ISO/IEC 25010), adskiller QA fra QC og kører kvalitetsstyringsprocesser med kvalitetsplaner og acceptkriterier, dokumenteret og anvendt ensartet på tværs af teams. Verifikation og validering er adskilte og bevidste, og fejl klassificeres og grundårsagsanalyseres efter et aftalt skema.

**Niveau 4 (Styring).** Kvalitet måles og styres mod baselines. Et lille sæt meningsfulde målinger følges over tid (fejltæthed, andel undsluppne fejl, middeltid til at opdage og rette, andel fejlslagne ændringer og kodesundhedssignaler som kompleksitet og duplikering), og omkostningen ved kvalitet kvantificeres på tværs af forebyggelse, vurdering og fejl. Accept- og kvalitetsporte håndhæves på dokumentation frem for mening, tendenser gennemgås efter en fast kadence, og validering kan reelt blokere en udgivelse.

**Niveau 5 (Orkestrering).** Kvalitet er en løbende forbedret, kulturelt ejet disciplin integreret med forretnings- og risikoplanlægning. Forebyggelse er vægtningen, omkostningsdata for kvalitet guider, hvor investering går hen, og grundårsagsfund forhindrer systematisk gentagelse. Teams ejer kvalitet fra ende til anden, målinger føder løbende forbedring, og organisationen tilpasser sin kvalitetspraksis, efterhånden som produkter, risici og regulering skifter. Dette svarer til de højere niveauer i modenhedsmodellerne i kapitel 10.8.

## Idéer til drøftelse

- Hvilke ISO/IEC 25010-kvalitetsegenskaber betyder mest for jeres systemer, og hvad er "godt nok" for hver?
- Hvor ligger jeres organisation i blandingen af udgifter til forebyggelse, vurdering og fejl, og bør den flytte?
- Skelner I verifikation fra validering i praksis, eller slår I begge sammen til "test"?
- Er kvalitet ejet af de teams, der bygger software, eller delegeret til en separat gruppe, og hvad ville ændre sig, hvis I flyttede den?
- Hvad er jeres sande omkostning ved dårlig kvalitet, og kunne I måle den godt nok til at lave business casen?
- Hvilke af jeres kvalitetsmålinger er ægte signaler, og hvilke er blevet til manipulerbare mål?

## Vigtigste pointer

- Kvalitet er bredere end test: det er egnethed til formålet plus overensstemmelse, på tværs af egenskaber som pålidelighed, sikkerhed og vedligeholdelighed.
- Brug en fælles kvalitetsmodel (ISO/IEC 25010), så kvalitetsegenskaber er eksplicitte og afstemt med arkitekturen (kapitel 3.1).
- Adskil kvalitetssikring (forebyg, proces) fra kvalitetskontrol (opdag, produkt), og læn dig mod forebyggelse.
- Praktisér verifikation (byggede det rigtigt) og validering (byggede det rigtige) som adskilte discipliner.
- Mål kvalitet med nogle få meningsfulde målinger, og karakterisér fejl efter alvorlighed og grundårsag for at forebygge gentagelse.
- Styr kvalitetens omkostning: forebyggelse og tidlig vurdering er langt billigere end fejl, især i langlivede systemer.
- Byg en fejlfri kvalitetskultur, hvor teams ejer kvalitet, understøttet af kodegennemgang (kapitel 2.5) og teststrategi (kapitel 2.4).

## Referencer og videre læsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
