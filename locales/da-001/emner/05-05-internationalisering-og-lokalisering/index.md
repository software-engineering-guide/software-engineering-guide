# 5.5 Internationalisering og lokalisering

## Overblik og motivation

[Internationalisering](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) er det ingeniørarbejde, der bygger software, så den kan tilpasses ethvert sprog, enhver region og kultur uden at ændre koden. Lokalisering (l10n) er arbejdet, der følger: faktisk at tilpasse et produkt til et specifikt locale ved at oversætte tekst, formatere datoer og tal, justere layout og tage højde for kulturelle forventninger. De to er forskellige. Internationalisering gøres én gang, i arkitekturen. Lokalisering gøres mange gange, i indholdet. Få arkitekturen rigtig på forhånd, og hver lokalisering er billig. Få den forkert, og hver bliver en smertefuld, fejlbehæftet eftermontering.

For store teams er i18n en grundlæggende arkitekturbeslutning. Den rører hvert lag: datalagring, strenghåndtering, layout og indholdspipelines. Hvis I ikke etablerer den tidligt og håndhæver den gennem fælles biblioteker og lint-regler, hårdkoder teams engelske strenge, sammenkæder oversatte fragmenter og antager latinske skrifttyper. Den gæld skal afvikles, før produktet kan træde ind på noget nyt marked. Et fælles i18n-framework og en lokaliseringsarbejdsgang lader dusinvis af teams levere et produkt på mange sprog uden at hvert enkelt genopfinder rørføringen.

Relevansen for virksomheder og det offentlige er direkte. Multinationale virksomheder skal betjene kunder og medarbejdere på tværs af lande, sprog og regulatoriske regimer. Det offentlige skal betjene sprogligt forskelligartede befolkninger. Mange lande er officielt flersprogede, og mange er juridisk forpligtede til at levere tjenester på flere sprog, herunder skrifttyper, der skrives [fra højre mod venstre](https://en.wikipedia.org/wiki/Bidirectional_text), og oprindelige eller minoritetssprog. For offentlige tjenester er sprogadgang et lighedsspørgsmål og et juridisk spørgsmål: en borger, der ikke kan læse det eneste tilgængelige sprog, er reelt nægtet tjenesten.

## Grundprincipper

- Internationalisér arkitekturen én gang; lokalisér indholdet mange gange.
- Hårdkod aldrig brugervendt tekst; eksternalisér alle strenge til styrede ressourcer.
- Brug [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) overalt; antag, at tekst kan være i enhver skrifttype.
- Sammenkæd aldrig oversatte fragmenter; grammatik og ordstilling er forskellig fra sprog til sprog.
- Planlæg for tekstudvidelse, skrifttyper fra højre mod venstre og komplekse regler for flertal og køn.
- Formatér datoer, tal, valutaer og navne efter locale, ikke kode.
- Adskil oversætbart indhold fra kode, så oversættere aldrig rører kildekode.
- Lokalisering er kulturel, ikke kun sproglig: farver, billeder og eksempler betyder noget.

## Anbefalinger

### Byg en sund internationaliseringsarkitektur

Gem og behandl al tekst som Unicode (UTF-8) fra ende til anden (database, API'er og UI), så enhver skrifttype kan repræsenteres. Eksternalisér hver brugervendt streng til ressourcefiler eller et beskedkatalog nøglet efter identifikator, aldrig indlejret i kode eller markup. Repræsentér et locale som sprog plus region (og skrifttype, hvor det er nødvendigt), så I kan skelne for eksempel ét sprogs varianter på tværs af lande. Hold formateringslogik i et veltestet internationaliseringsbibliotek frem for at håndrulle formatering af dato, tal og valuta. Gem data i neutrale, utvetydige former (UTC-tidsstempler, ISO-lande- og valutakoder, grundenheder) og formatér kun i præsentationslaget.

### Håndtér sprogkompleksitet korrekt

Antag ikke tekstlængde; giv rigelig plads, fordi oversættelser ofte løber meget længere end engelsk, og design layouts, der omflyder frem for at afkorte eller overlappe. Understøt tovejs (højre-mod-venstre) skrifttyper ved at bruge logiske frem for fysiske layoutegenskaber og spejle grænsefladen, hvor det er passende. Brug locales regler for flertal gennem jeres i18n-bibliotek (sprog har alt fra én til seks flertalsformer) i stedet for naiv ental/flertal-logik. Håndtér køn og grammatisk kongruens, hvor sproget kræver det. Byg aldrig sætninger ved sammenkædning; brug fulde, parametriserede beskedskabeloner, så oversættere styrer ordstillingen.

### Etablér en lokaliseringsarbejdsgang og oversættelsesstyring

Behandl lokalisering som en kontinuerlig pipeline, ikke en batch før lancering. Udtræk strenge automatisk, skub dem til et [oversættelsesstyringssystem](https://en.wikipedia.org/wiki/Translation_management_system), og træk færdige oversættelser tilbage, helst integreret med CI, så nye strenge flages, og lokaliserede versioner forbliver synkroniserede. Giv oversættere kontekst: skærmbilleder, beskrivelser, tegngrænser og en ordliste og stilguide pr. sprog for at holde terminologi og tone ensartet. Brug [oversættelseshukommelse](https://en.wikipedia.org/wiki/Translation_memory) til at genbruge tidligere arbejde og skære omkostning. Beslut bevidst, hvor [maskinoversættelse](https://en.wikipedia.org/wiki/Machine_translation) er acceptabel (lavrisiko indhold i højt volumen), og hvor menneskelig oversættelse og gennemgang kræves (juridisk, medicinsk, sikkerhed, brandkritisk). [Pseudolokalisér](https://en.wikipedia.org/wiki/Pseudolocalization) tidligt og erstat strenge med forlængede, accentuerede pladsholdere for at fange hårdkodede strenge, afkortning og kodningsfejl, før den rigtige oversættelse begynder.

### Lokalisér formater, kultur og indhold, ikke kun ord

Formatér datoer, tidspunkter, tal, valutaer, adresser, telefonnumre og navne pr. locale og respektér lokale konventioner (datorækkefølge, decimal- og grupperingsseparatorer, valutaplacering, navnerækkefølge). Tilpas billeder, ikoner, farver, eksempler og metaforer til lokal kulturel betydning, da symboler og farver bærer forskellige konnotationer på tværs af kulturer. Tag højde for lokale juridiske og regulatoriske indholdsforskelle. Skeln mellem global ensartethed (brand, kernefunktionalitet) og regional tilpasning (indhold, eksempler, compliance), og beslut eksplicit, hvilke elementer der er faste, og hvilke der bøjer sig.

### Styr i18n som fælles infrastruktur

Lever et fælles i18n-bibliotek, lint-regler for strengeksternalisering og en standardmekanisme til locale-opløsning, så teams ikke ved et uheld kan hårdkode tekst. Etablér ejerskab af lokaliseringspipelinen og ordlisterne. Test i flere locales i CI, herunder et højre-mod-venstre-locale og et langtekst-pseudolocale, så regressioner fanges automatisk.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Internationalisér fra dag ét | Billig markedsindtræden senere, ingen eftermontering | Omkostning på forhånd, selv før et andet locale er nødvendigt |
| Eftermontér i18n senere | Udskyd omkostning, hvis globalt behov er usikkert | Meget dyrt og risikabelt at afvikle hårdkodede antagelser |
| Menneskelig oversættelse | Høj kvalitet, kulturelt nøjagtig | Langsommere og dyrere |
| Maskinoversættelse | Hurtig, billig, skalerer til enormt volumen | Risiko for kvalitet og nøjagtighed; uegnet til højindsatsindhold |
| Kontinuerlig lokaliseringspipeline | Locales forbliver synkroniserede, ingen travlhed før lancering | Investering i værktøj og proces |
| Dyb kulturel tilpasning pr. region | Bedre lokal pasform og tillid | Flere indholdsvarianter at bygge og vedligeholde |

Den afgørende afvejning er, hvornår man investerer i internationalisering. At eftermontere i18n i et produkt fuldt af hårdkodet, sammenkædet, latin-antagende kode er en af de dyrere former for teknisk gæld at afvikle. For enhver organisation med plausible internationale eller flersprogede ambitioner, hvilket omfatter i det væsentlige alle store virksomheder og flersprogede regeringer, er det langt billigere at internationalisere arkitekturen tidligt end at eftermontere, selv om gevinsten er udskudt.

## Spørgsmål til drøftelse med dit team

1. **Håndhæver vi strengeksternalisering med lint-regler, og kører pseudolokalisering i CI før nogen rigtig oversættelse?** Den gæld, der gør internationalisering dyr (hårdkodede engelske strenge, sammenkædede sætningsfragmenter, antagelser om latinsk skrift), akkumulerer stille, medmindre værktøj stopper den ved commit. Lint-regler, der flager hårdkodet brugertekst, plus et langtekst-accentueret pseudolocale kørt i CI fanger afkortning, overlap og kodningsfejl, mens de er billige at rette. Det er det, der lader dusinvis af teams levere ét produkt på mange sprog uden at hvert genopfinder rørføringen eller afvikler antagelser under en deadline senere. Tag en søgning efter hårdkodede strenge med og spørg, om noget team ved et uheld kunne levere en i dag. Hvis intet i pipelinen ville fange det, er det hullet, der skal lukkes først.

2. **Hvor gemmer vi kanoniske data, og er formatering begrænset til præsentationslaget?** At gemme tidsstempler som UTC, lande og valutaer som ISO-koder og beløb i grundenheder betyder, at ethvert locale kan formatere dem korrekt ved kanten, mens formateringslogik bagt ind i datalaget producerer fejl, der er smertefulde at afvikle. Aftal, at datoer, tal, valutaer, adresser og navne kun formateres ved præsentation, gennem et veltestet bibliotek frem for håndrullet kode. Det betyder noget for multinationale virksomheder og flersprogede regeringer, hvor en borger skal se korrekt datorækkefølge, decimalseparatorer og navnerækkefølge i sin egen konvention. Tag et eksempel på en værdi, jeres system gemmer allerede formateret, med og spor, hvad der går i stykker, når et nyt locale har brug for det anderledes. Hvis data og præsentation er viklet sammen, så beslut, hvordan I trævler dem ud, før I tilføjer locales.

3. **Hvor præcis er maskinoversættelse acceptabel, og hvordan holdes vores lokaliseringspipeline kontinuerlig frem for batch?** Maskinoversættelse er hurtig og billig til lavrisiko indhold i højt volumen, men uegnet til juridisk, medicinsk, sikkerheds- eller brandkritisk tekst, hvor en fejloversættelse forårsager reel skade, så grænsen skal være en eksplicit politik, ikke et gæt pr. team. Lige så sikrer det at behandle lokalisering som en batch før lancering en oversættelsestravlhed, mens automatisk udtræk af strenge og synkronisering gennem et oversættelsesstyringssystem holder hvert locale aktuelt. Beslut, hvem der ejer pipelinen, ordlisterne og den menneskelige gennemgangsport for strenge med høj indsats. Tag en nylig udgivelse med og spørg, hvor lang tid dens nye strenge tog om at dukke op på hvert sprog. Hvis locales driver ud af synkronisering mellem udgivelser, er jeres pipeline batch i forklædning.

4. **Tester vi automatisk et højre-mod-venstre-locale og et langtekst-pseudolocale, eller antager vi stille latinsk skrift og layouts i engelsk længde?** Tovejsunderstøttelse (højre mod venstre) og tekstudvidelse er de antagelser, der går mest synligt i stykker på et nyt marked: spejlede grænseflader, der aldrig blev spejlet, og knapper, der afkortes, når tysk eller finsk løber fyrre procent længere end engelsk. Det modstridende træk er hastighed, da det koster indsats at bygge på logiske frem for fysiske layoutegenskaber og koble et accentueret pseudolocale ind i kontinuerlig integration (CI), før nogen rigtig kunde har brug for det. Tag et skærmbillede af jeres travleste skærme gengivet i et højre-mod-venstre-locale og i et forlænget pseudolocale med og tæl overlappene, afklippede labels og hængende pile. For en multinational virksomhed eller en regering, der juridisk skal betjene et højre-mod-venstre- eller minoritetssprog, er et layout, der ikke kan spejle, ikke en kosmetisk defekt, det er et marked eller en lovbestemt forpligtelse, I ikke kan opfylde uden en ombygning.

5. **Hvilke dele af produktet er globalt faste, og hvilke bøjer sig efter region, og hvem har autoritet til at afgøre det?** Lokalisering er kulturel, ikke blot sproglig, så farver, billeder, eksempler, tiltaleformer og endda hvilke funktioner der tilbydes kan være forskellige fra marked til marked, men hver regional variant, I tillader, er endnu et artefakt at bygge, oversætte, gennemgå og vedligeholde for evigt. Spændingen er mellem lokal pasform, der bygger tillid og konvertering, og ensartethed, der holder brandet sammenhængende og vedligeholdelsesbyrden afgrænset. Tag en konkret liste over, hvad et foreslået nyt locale ville ændre ud over oversatte strenge, med og prissæt den løbende vedligeholdelse af hver variant, ikke blot dens første bygning. I en stor virksomhed har denne beslutning brug for en navngiven ejer, så regionale teams ikke kan forke produktet ad hoc, og i det offentlige skal den respektere juridiske og tilgængelighedsmæssige indholdsregler, der varierer efter jurisdiktion og ikke er valgfri.

6. **Hvilke locales forpligter vi os reelt til, hvordan holder vi terminologien ensartet på tværs af dem, og hvilken dokumentation driver den liste?** At tilføje et sprog er let at love og dyrt at opretholde, fordi hvert kræver en ordliste, en stilguide, menneskelig gennemgang af strenge med høj indsats og korrekt håndtering af flertal og køn, som naiv ental-eller-flertal-logik får forkert på de fleste sprog. De konkurrerende hensyn er rækkevidde mod omkostning: et marked eller en befolkning, der betjenes dårligt, kan være værre end en, der slet ikke betjenes. Tag befolkningen eller omsætningen bag hvert kandidatlocale, den dækning af flertalsregler og formatering, jeres bibliotek giver for det, og hvem der ejer dets ordliste, med. For en multinational virksomhed er drivkraften det adresserbare marked og supportomkostningen pr. sprog, mens den for det offentlige er den juridiske sprogadgangsforpligtelse og lighed, kvantificeret ved antallet af indbyggere, der kun kan handle på det sprog.

## Sektorperspektiv

**Startup.** Træf de billige arkitekturvalg på dag ét og stop så: UTF-8 fra ende til anden, hver brugervendt streng i et beskedkatalog og datoer, tal og valutaer formateret gennem et locale-bevidst bibliotek. De koster næsten intet, mens I leverer på ét sprog, og sparer en omskrivning, når jeres første store kunde vil have et andet. Opstil ikke en oversættelsespipeline eller understøt locales, ingen betaler for endnu; hold døren åben, ikke hele huset møbleret.

**Lille virksomhed.** Uden en internationaliseringsspecialist og med et stramt budget så støt jer til de i18n-funktioner, der allerede findes i jeres framework, og en hostet oversættelsesstyringstjeneste frem for selv at bygge pipelines. Brug maskinoversættelse til lavrisiko indhold i højt volumen, og betal kun for menneskelig oversættelse, hvor en fejl ville koste jer en kunde eller bryde en regel, såsom juridisk, sikkerheds- eller faktureringstekst. Forpligt jer kun til et locale, når et specifikt marked klart retfærdiggør den løbende oversættelses- og gennemgangsomkostning.

**Stor virksomhed.** Problemet er styring på tværs af mange teams: et fælles i18n-bibliotek, lint-regler, der afviser hårdkodede strenge, en kontinuerlig lokaliseringspipeline med oversættelseshukommelse og ordlister pr. sprog og multi-locale CI, der inkluderer et højre-mod-venstre- og et langtekst-pseudolocale. Kør lokalisering som fælles infrastruktur med en klar ejer, så grupper holder op med at genopfinde rørføringen eller drive ud af synkronisering. Mål sprogdækning, lokaliseringskvalitet og tid til at lancere et nyt locale, og styr locale-porteføljen mod de tal frem for at lancere markeder ad hoc.

**Offentlig sektor.** Sprogadgang er ofte en juridisk forpligtelse, der dækker officielle sprog, højre-mod-venstre-skrifttyper og oprindelige eller minoritetssprog, så åbenhed og lighed former hvert valg. Byg et fælles i18n-framework og en oversættelsesarbejdsgang på tværs af agenturer, kræv menneskelig gennemgang for juridisk og sikkerhedsmæssig terminologi, og offentliggør ordlister, så termer forbliver ensartede mellem tjenester. Indkøb bør kræve locale-, højre-mod-venstre- og tilgængelighedsunderstøttelse i kontrakter, og den befolkning, der betjenes på hvert sprog, er den måling, der retfærdiggør udgiften over for offentligheden.

## Eksempler

**Startup.** Et lille startup, der kun leverede på engelsk, traf alligevel nogle få billige arkitekturvalg på dag ét: UTF-8 overalt, hver brugervendt streng trukket ind i et beskedkatalog i stedet for hårdkodet og datoer og valutaer formateret gennem et locale-bevidst bibliotek. Det kostede dem næsten intet, mens de havde ét sprog. Et år senere, da deres største prospekt bad om en fransk og en tysk version, var det at tilføje disse locales mest en oversættelsesøvelse overdraget til en freelanceoversætter, ikke en omskrivning, og de lukkede aftalen på uger i stedet for at udskyde den et kvartal med ingeniørarbejde.

**Stor virksomhed.** Et globalt e-handelsfirma internationaliserede sin platform tidligt: UTF-8 hele vejen, eksternaliserede strenge, et locale-bevidst formateringsbibliotek og en kontinuerlig lokaliseringspipeline med oversættelseshukommelse og ordlister pr. sprog. At gå ind på et nyt marked blev stort set en indholdsøvelse (oversæt, gennemgå, justér billeder) frem for et ingeniørprojekt og lod virksomheden lancere i nye locales på uger. Højre-mod-venstre-understøttelse bygget på logiske layoutegenskaber betød, at arabiske og hebraiske markeder krævede lidt nyt UI-arbejde.

**Offentlig sektor.** En national regering, juridisk forpligtet til at levere tjenester på flere officielle sprog, herunder en højre-mod-venstre-skrifttype og minoritetssprog, byggede et fælles i18n-framework og en oversættelsesarbejdsgang brugt på tværs af agenturer. Pseudolokalisering i CI fangede hårdkodede strenge og afkortning før lancering; en fælles ordliste holdt juridisk terminologi ensartet på tværs af tjenester og sprog. Borgere kan gennemføre skatte-, sundheds- og ydelsestransaktioner på deres eget sprog med korrekt dato-, tal- og navneformatering, hvilket opfylder sprogadgangslovgivning og forbedrer lighed for talere af ikke-flertalssprog.

## Business case: motivation, ROI og TCO

ROI af internationalisering er markedsadgang og hastighed. Et veludbygget internationaliseret produkt kan træde ind i nye lande og sprogmarkeder hurtigt og billigt og forvandle hvert nyt locale til yderligere omsætning eller borgerrækkevidde frem for et større projekt. Lokaliseringskvalitet driver konvertering, tillid og supportomkostning på hvert marked: brugere handler mere og kontakter support mindre, når produktet taler deres sprog korrekt og respekterer deres konventioner.

Hvad angår TCO er adoptionsomkostningen det ingeniørarbejde på forhånd, der skal til for at internationalisere, plus løbende oversættelses- og pipelineomkostninger. Omkostningen ved ikke at adoptere er den dyre eftermontering: at afvikle hårdkodede strenge, sammenkædning, kodningsfejl og layoutantagelser på tværs af en hel kodebase, ofte på en deadline drevet af et markeds- eller juridisk krav. Dårlig lokalisering bærer også skjulte omkostninger: tabte salg på markeder, der betjenes dårligt, supportbyrde fra forvirrende formater og juridisk eller omdømmemæssig skade fra fejloversat indhold med høj indsats. Kontinuerlig lokalisering undgår dyre oversættelsesjag før lancering.

For at føre sagen over for ledelsen så ram internationalisering ind som en option på fremtidige markeder. Det er en beskeden investering på forhånd, der dramatisk sænker omkostningen og tiden ved hver fremtidig markedsindtræden. For det offentlige er drivkraften den juridiske sprogadgangsforpligtelse og lighed, kvantificeret ved den befolkning, der betjenes på hvert sprog.

## Anti-mønstre og faldgruber

- **Hårdkodede strenge**: brugertekst bagt ind i kode, hvilket tvinger kodeændringer pr. locale.
- **Strengsammenkædning**: at bygge sætninger af fragmenter, hvilket bryder grammatik og ordstilling.
- **Ikke-Unicode-antagelser**: kodningsfejl, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (forvansket tekst fra uens tegnkodninger) og manglende evne til at repræsentere skrifttyper.
- **At antage engelsk tekstlængde**: layouts, der afkortes eller overlapper, når de oversættes.
- **At ignorere højre-mod-venstre**: at bruge fysisk venstre/højre-layout, der ikke kan spejle.
- **Naiv flertalshåndtering**: ental/flertal-logik, der er forkert på de fleste sprog.
- **Locale-blind formatering**: hårdkodede dato-, tal- og valutaformater.
- **Oversættelse uden kontekst**: oversættere, der gætter på betydning og producerer fejl.
- **Batch-lokalisering i sidste øjeblik**: en travlhed før lancering i stedet for en kontinuerlig pipeline.
- **Kulturel døvhed**: billeder, farver eller eksempler, der støder eller forvirrer lokalt.

## Modenhedsmodel

**Niveau 1: Opstart.** Ét sprog, hårdkodede strenge, ikke-Unicode-antagelser og tekst bygget ved sammenkædning. Internationalisering er reaktiv: ethvert nyt locale betyder at ændre kode, og kodnings- og layoutfejl findes ved et tilfælde i produktion.

**Niveau 2: Udvikling.** Nogle strenge er eksternaliserede, og Unicode bruges nogle steder, men praksis er inkonsistent på tværs af teams. Lokalisering er en manuel batchindsats før lancering, og formatering, håndtering af flertal og højre-mod-venstre-understøttelse håndteres forskelligt (eller slet ikke) fra team til team.

**Niveau 3: Standardisering.** En fælles i18n-arkitektur og et locale-bevidst formateringsbibliotek er den dokumenterede, håndhævede standard i hele organisationen. Strengeksternalisering kontrolleres af lint-regler, et oversættelsesstyringssystem og en kontinuerlig pipeline er på plads med ordlister og oversættelseshukommelse, og pseudolokalisering plus multi-locale-test (herunder et højre-mod-venstre- og et langtekst-locale) kører i CI.

**Niveau 4: Styring.** Lokaliseringsprogrammet måles og styres mod baselines. Teams følger sprogdækning, lokaliseringskvalitet og defektrater, synkroniseringsforsinkelse fra commit til oversat udgivelse, afkortnings- og højre-mod-venstre-gengivelsesdefekter fanget pr. udgivelse, oversættelsesomkostning pr. locale og tid til at lancere et nyt locale, og disse målinger lukker porten for udgivelser og driver, hvor man investerer i menneskelig gennemgang versus maskinoversættelse.

**Niveau 5: Orkestrering.** Internationalisering og lokalisering forbedres løbende og er integreret på tværs af organisationen. Lokalisering er kontinuerlig, maskin- og menneskelig oversættelse vælges bevidst pr. indholdsklasse, og kulturel tilpasning er systematisk. Organisationen tilføjer, pensionerer og omafgrænser locales som svar på markeds- og lighedsdokumentation, og nye locales lanceres hurtigt i høj kvalitet uden eftermontering.

## Idéer til drøftelse

- Hvor tidligt bør et produkt internationalisere, hvis international efterspørgsel er usikker?
- Hvor er maskinoversættelse acceptabel, og hvor skal mennesker gennemgå?
- Hvordan holder I terminologien ensartet på tværs af mange sprog og teams?
- Hvor megen regional kulturel tilpasning er den ekstra variantvedligeholdelse værd?
- Hvordan bør højre-mod-venstre- og minoritetssprogsunderstøttelse prioriteres og testes?
- Hvordan giver I oversættere nok kontekst uden at sinke pipelinen?

## Vigtigste pointer

- Internationalisér arkitekturen én gang; lokalisér indhold mange gange.
- Brug Unicode overalt, eksternalisér alle strenge, og sammenkæd aldrig oversættelser.
- Planlæg for tekstudvidelse, højre-mod-venstre-skrifttyper og locale-specifikke regler for flertal og formatering.
- Kør en kontinuerlig lokaliseringspipeline med oversættelseshukommelse, ordlister og kontekst.
- Pseudolokalisér tidligt i CI for at fange i18n-fejl før den rigtige oversættelse.
- Lokalisering er kulturel, ikke blot sproglig.
- Tidlig internationalisering er langt billigere end eftermontering; for det offentlige er det et juridisk lighedskrav.

## Referencer og videre læsning

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
