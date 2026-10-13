# 10.5 Etik, ansvarlighed og almenvellet

## Overblik og motivation

Software er ikke længere et neutralt værktøj, der sidder bag menneskelige beslutninger. Den *er* i stigende grad beslutningen. Den afgør, hvem der får et lån, hvilket cv en rekrutterer ser, hvor lang tid en ydelsessag tager, om et svindelflag fryser en konto, og hvilken information der når millioner af mennesker. Når software træffer eller former beslutninger, der påvirker menneskers rettigheder, penge, sikkerhed og værdighed, påtager de ingeniører og organisationer, der bygger den, sig ansvar ud over korrekthed og ydeevne. Dette kapitel handler om de ansvar: [professionel etik](https://en.wikipedia.org/wiki/Professional_ethics), ansvarlighed for, hvad systemer gør, [tilgængelighed](https://en.wikipedia.org/wiki/Web_accessibility) og lighed som forpligtelser frem for funktioner, algoritmisk åbenhed, [bæredygtighed](https://en.wikipedia.org/wiki/Sustainability) og pligten til at betjene mennesker med retfærdighed og værdighed.

For store organisationer hæver skala og magt indsatsen. Et virksomheds- eller offentligt system påvirker ikke én person. Det påvirker millioner. Et enkelt designvalg (et skævt træningssæt, en utilgængelig formular, et uigennemsigtigt automatiseret afslag) gentages på tværs af hver eneste af dem. Regeringer bærer en forhøjet pligt, fordi deres systemer ikke er valgfrie. En borger kan ikke vælge en konkurrent til sin skattemyndighed eller sit ydelsesagentur. Statens monopol på visse tjenester betyder, at et dårligt bygget system kan nægte folk rettigheder, de ikke har nogen anden måde at udøve på. Med den rækkevidde følger en tilsvarende pligt til at være retfærdig, åben og ansvarlig.

Etik i software behandles ofte som et blødt emne, boltet på til sidst eller overladt til en juridisk complianceliste. Dette kapitel argumenterer for det modsatte. Etiske overvejelser er ingeniørkrav. Ansvarlighed skal designes ind, ikke påstås bagefter. Og at betjene mennesker med værdighed er både en moralsk pligt og, over tid, fundamentet for den tillid, store organisationer afhænger af.

## Grundprincipper

- **Software træffer beslutninger, så dens skabere bærer ansvar.** I er ansvarlige for, hvad jeres system gør ved mennesker, ikke blot for, om det opfylder specifikationen.
- **Tilgængelighed og lighed er forpligtelser, ikke forbedringer.** At udelukke folk er en fejl og ofte et juridisk og moralsk svigt.
- **Afgørende automatiserede beslutninger kræver ansvarlighed.** Folk, der berøres af en automatiseret beslutning, fortjener forklaring, klagemulighed og menneskelig gennemgang.
- **Åbenhed er standarden, hemmeligholdelse undtagelsen.** Især i den offentlige sektor har folk ret til at forstå, hvordan beslutninger om dem træffes.
- **Retfærdighed skal undersøges, ikke antages.** Systemer arver og forstærker bias i deres data og design, medmindre I bevidst tjekker.
- **Værdighed er et designkrav.** Behandl hver bruger, inklusive de sårbare og ikke-typiske, som et menneske, der fortjener respekt.
- **Bæredygtighed og social påvirkning tæller.** Softwares energi, ressourcer og samfundsmæssige effekter er en del af dens sande omkostning.

## Anbefalinger

### Adoptér og lev professionel etik

Forankr organisationen i en anerkendt adfærdskodeks, og gør den reel frem for dekorativ. Ingeniører bør forstå, at de har forpligtelser over for offentligheden, ikke blot over for deres arbejdsgiver. "Jeg fulgte bare specifikationen" er ikke et forsvar, når et system skader mennesker. Skab ægte kanaler til at rejse etiske betænkeligheder: en måde at sige "vi bør ikke bygge dette, eller ikke bygge det på denne måde", der ikke kræver karrierebrydende mod. Giv teams ordforrådet og ret til at veje konsekvenser. Bak det op med ledelse, der behandler etiske indvendinger som værdifuldt signal, ikke hindring. Etiktræning hjælper kun, hvis organisationen synligt handler på det, den lærer.

### Behandl tilgængelighed og lighed som forpligtelser

Byg til hele spektret af menneskelig evne og omstændighed fra begyndelsen. At eftermontere tilgængelighed er langt dyrere og som regel dårligere. Følg etablerede tilgængelighedsstandarder (såsom [WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines), Web Content Accessibility Guidelines), og opfyld i mange jurisdiktioner juridiske krav, der påbyder dem for offentlige tjenester. Test med [hjælpeteknologier](https://en.wikipedia.org/wiki/Assistive_technology) og, frem for alt, med rigtige brugere med handicap. Udvid lighed ud over handicap til hele den befolkning, I betjener: folk med lav båndbredde, på gamle enheder, med begrænset [digital kompetence](https://en.wikipedia.org/wiki/Digital_literacy), på minoritetssprog og i vanskelige livsomstændigheder. For tjenester, folk ikke kan fravælge (især offentlige tjenester), er det at designe kun til den selvsikre, forbundne, typiske bruger et svigt i at betjene, ikke en rimelig standard.

### Byg algoritmisk ansvarlighed og offentlig åbenhed

For ethvert system, der træffer eller væsentligt former afgørende beslutninger om mennesker, så design ansvarlighed ind. Hold mennesker meningsfuldt [i løkken](https://en.wikipedia.org/wiki/Human-in-the-loop) for højindsatsbeslutninger frem for blindt at henholde sig til automatiseret output. Vær i stand til at forklare, i vendinger en berørt person kan forstå, hvorfor en beslutning blev truffet. Giv en reel vej til at udfordre den og nå et menneske. Test systemer for [bias](https://en.wikipedia.org/wiki/Algorithmic_bias) og [forskellig virkning](https://en.wikipedia.org/wiki/Disparate_impact) på tværs af beskyttede og sårbare grupper, før og under udrulning, og overvåg for drift over tid. I den offentlige sektor så offentliggør, hvordan algoritmiske systemer virker (deres formål, data og logik på et passende niveau) gennem mekanismer som algoritmeregistre, så borgere og tilsynsorganer kan granske dem. Dokumentér tilsigtet brug og kendte begrænsninger, så systemer ikke anvendes, hvor de ikke bør.

### Design til retfærdighed, værdighed og klagemulighed

Undersøg jeres systemer for de måder, de kan behandle mennesker uretfærdigt eller uden værdighed. Gransk træningsdata og regler for indlejret bias. Husk, at et system optimeret rent for effektivitet kan være grusomt: et svindelfilter justeret til at minimere falske negativer kan fryse tusinder af uskyldiges konti, hver et rigtigt menneske i nød. Design til fejltilfældene fra den berørte persons synspunkt. Hvad sker der, når systemet tager fejl? Hvor let kan de få et menneske, en forklaring og en afhjælpning? Håndtér [personoplysninger](https://en.wikipedia.org/wiki/Personal_data) med respekt og tilbageholdenhed: indsaml kun det nødvendige, og vær ærlige om brugen. Behandl fejl, forsinkelse og afslag ikke som grænsetilfælde, men som de øjeblikke, hvor værdigheden er mest i fare.

### Tag højde for bæredygtighed og socialt ansvar

Anerkend, at software har fysiske og sociale omkostninger. Datacentre, træningskørsler og ineffektive systemer forbruger reel energi. Effektivitet er en miljømæssig dyd såvel som en finansiel. Overvej de bredere effekter af det, I bygger (på arbejde, på den offentlige debat, på sårbare grupper), og vær villige til at afslå eller omforme arbejde, hvis skader overstiger dets fordele. For store organisationer, hvis systemer former samfundet i skala, er socialt ansvar ikke filantropi ved siden af forretningen. Det er en del af at bygge ansvarligt og i stigende grad et spørgsmål om regulering og offentlig forventning.

## Afvejninger: fordele og ulemper

| Spænding | Den ene side | Den anden side |
|---|---|---|
| Automatisering vs. menneskelig dømmekraft | Skala, ensartethed, fart, lavere omkostning | Ansvarlighed, nuance, barmhjertighed, klagemulighed |
| Åbenhed vs. beskyttelse | Offentlig granskning, tillid, tilsyn | Risiko for manipulation, sikkerhed, datas privatliv |
| Tilgængelighedsinvestering vs. fart | Betjener alle; juridisk og moralsk compliance | Langsommere indledende levering; mere designindsats |
| Effektivitet vs. retfærdighed | Optimerede udfald; lavere omkostning | Risiko for grusomhed mod enkeltpersoner i halerne |
| Datarig personalisering vs. privatliv | Bedre service; skræddersyet oplevelse | Overvågningsrisiko; bekymringer om værdighed og samtykke |
| Innovationsfart vs. forsigtighed | Hurtigere værdi; konkurrencefordel | Uundersøgte skader udrullet i skala |

Den sværeste afvejning er skala versus individuel retfærdighed. Automatisering leverer ensartethed og effektivitet på tværs af millioner. Men dens fejl leveres også i skala, og et system optimeret for aggregatet kan være stille brutalt over for enkeltpersonerne i dets haler. Svaret er ikke at opgive automatisering. Det er at designe til det individuelle fejltilfælde: hold mennesker i løkken, hvor indsatsen er høj, garantér forklaring og klagemulighed, og mål systemets effekt på de dårligst betjente, ikke blot gennemsnittet. Åbenhed bærer også en reel spænding, fordi fuld åbenhed kan muliggøre manipulation og blotlægge private data. Men i offentlige tjenester læner svaret sig stærkt mod offentliggørelse som standard, hvor kun det, der reelt skal beskyttes, undtages, frem for at behandle uigennemsigtighed som den sikre standard.

## Spørgsmål til drøftelse med dit team

1. **Hvilke af jeres systemer træffer eller former væsentligt afgørende beslutninger om mennesker, og tilbyder hvert af dem i dag forklaring, menneskelig gennemgang og klagemulighed?** Software er i stigende grad beslutningen: hvem der får et lån, hvilket cv der ses, om en konto fryses, hvor lang tid en sag tager. For hvert sådant system fortjener en berørt person en forklaring, de kan forstå, en reel vej til at udfordre den og et menneske, der kan gribe ind, og i virksomheds- eller offentlig skala gentages en enkelt designfejl på tværs af millioner. Tag dokumentation med: opgør jeres afgørende automatiserede beslutninger, og tjek for hver, om en forkert behandlet person faktisk kan nå et menneske og få en begrundelse i almindeligt sprog. Hvor svaret er nej, er det en fejl at rette, ikke en funktion at tilføje senere. For tjenester, folk ikke kan fravælge, især offentlige tjenester, er det en forpligtelse frem for en finesse.

2. **Behandler I tilgængelighed som et lanceringsblokerende krav testet med rigtige handicappede brugere, og hvem svigter I i øjeblikket?** Tilgængelighed og lighed er forpligtelser, og at udelukke folk er en fejl, ofte et juridisk og moralsk svigt, og alligevel er eftermontering af tilgængelighed pålideligt langsommere, dyrere og dårligere end at designe den ind fra den første skærm. Følg WCAG, og gå ud over automatiserede tjek for at teste med hjælpeteknologier og rigtige brugere med handicap, plus folk med lav båndbredde, gamle enheder, minoritetssprog og begrænset digital kompetence. Tag dokumentation med: kør jeres vigtigste flow med en skærmlæser og på en droslet forbindelse, og se, hvor det går i stykker. Svaret bør afgøre, om tilgængelighed er en port, der blokerer release, eller et efterslædspunkt, der aldrig stiger, og for tjenester, folk ikke kan fravælge, er kun porten forsvarlig. At designe kun til den selvsikre, forbundne, typiske bruger er et svigt i at betjene.

3. **Hvad er jeres stående proces for at teste afgørende systemer for bias og forskellig virkning, før og under udrulning?** Systemer arver og forstærker bias i deres data og design, medmindre I bevidst tjekker, og at antage retfærdighed, fordi ingen havde til hensigt uretfærdighed, er bias ved forsømmelse. Et svindelfilter justeret rent til at minimere falske negativer kan fryse tusinder af uskyldiges konti, hver et rigtigt menneske i nød, så effektivitet optimeret uden hensyn til retfærdighed kan være stille grusom. Tag dokumentation med: for hver model, der påvirker mennesker, vis testen for forskellig virkning på tværs af beskyttede og sårbare grupper, de dokumenterede data og kendte begrænsninger og den driftsovervågning, der gentester, efterhånden som befolkningen ændrer sig. Svaret bør gøre biastest rutinemæssig og kontinuerlig frem for et engangsafkrydsningsfelt før lancering, og det bør ændre jeres optimeringsmål til at veje skade på enkeltpersoner, ikke blot aggregeret nøjagtighed. Design til fejltilfældet fra den berørte persons synspunkt.

4. **Når en ingeniør mener, at I ikke bør bygge noget, eller ikke bygge det på denne måde, hvad sker der så faktisk med den indvending?** Etik bliver først reel, når "vi bør ikke levere dette" er en sætning, nogen kan sige uden at afslutte deres karriere, og i skala er den person, der er tættest på en skade, ofte den mest juniore i rummet. Det modstridende pres er levering: en rejst indvending sinker en køreplan, og ledere under deadline kan behandle den som hindring frem for værdifuldt signal. Tag dokumentation med: navngiv den præcise kanal, en ingeniør ville bruge, tæl hvor mange betænkeligheder der blev rejst i det seneste år, og spor, hvad der ændrede sig som følge, fordi en kanal, der aldrig har stoppet eller omformet arbejde, er dekorativ. For en virksomheds- eller offentlig organisation så bind kanalen til en navngiven ejer og en dokumenteret gennemgang, da en indvending, ingen er forpligtet til at høre, er en, ingen vil risikere at rejse, og skaden så dukker op først som en offentlig skandale.

5. **Kender I den miljømæssige og sociale omkostning ved det, I kører, og ville I omforme eller afslå arbejde, hvis skader overstiger dets fordele?** Software har fysiske og sociale omkostninger: datacentre, træningskørsler og ineffektive systemer forbruger reel energi, og andenordens effekter på arbejde, offentlig debat og sårbare grupper er en del af et systems sande omkostning. Spændingen er, at at måle og skære disse omkostninger konkurrerer med funktionsfart, og at afslå skadeligt arbejde opgiver omsætning, som nogen er ansvarlig for. Tag dokumentation med: energi- eller beregningsaftrykket af jeres største systemer, en ærlig læsning af, hvem der bærer de nedstrøms effekter, og mindst ét konkret tilfælde, hvor I omformede eller afviste arbejde på disse grunde. I virksomheds- eller offentlig skala, hvor jeres systemer former samfundet, så behandl dette som en del af at bygge ansvarligt og i stigende grad et spørgsmål om regulering og offentlig forventning, ikke filantropi boltet på siden af forretningen.

6. **Hvor meget kan en udenforstående faktisk lære om, hvordan jeres afgørende systemer beslutter, og er offentliggørelse jeres standard eller jeres undtagelse?** Åbenhed er, hvor offentlig tillid optjenes eller tabes, fordi folk har ret til at forstå, hvordan beslutninger om dem træffes, og i den offentlige sektor er den ret ofte loven. Det reelle modtryk er, at fuld åbenhed kan muliggøre manipulation og blotlægge private data, så det reelle spørgsmål er, hvor linjen skal trækkes, ikke om der overhovedet skal offentliggøres. Tag dokumentation med: for hvert væsentligt system vis, hvad I offentliggør (formål, data og logik på et passende niveau), hvad I tilbageholder og den specifikke grund, og om en beskrivelse i almindeligt sprog står ved siden af enhver teknisk. For et offentligt organ så vej en mekanisme som et algoritmeregister mod de snævre, forsvarlige undtagelser, og tjek, at jeres offentliggørelser reelt forklarer frem for teknisk at informere, mens de intet fortæller en berørt person.

## Sektorperspektiv

**Startup.** Med en håndfuld mennesker og lidt runway kan I ikke bemande et etikudvalg, så bag de billige, højløftestangs vaner ind i selve produktet: en begrundelse i almindeligt sprog på hvert automatiseret afslag, en ét-kliks vej til at nå et menneske og tilgængelige formularer fra den første skærm, fordi eftermontering senere er langsommere og dårligere. Vælg det ene sted, hvor jeres software træffer en væsentlig beslutning om en person, og få forklaring og klagemulighed rigtig der, før I skalerer skaden. At behandle retfærdighed og værdighed som lanceringskrav, ikke senere finpudsning, koster lidt nu og undgår et omdømme, I ikke har råd til at miste tidligt.

**Lille virksomhed.** I har sandsynligvis ingen tilgængeligheds- eller retfærdighedsspecialist og et stramt budget, så støt jer til den etik, der er bygget ind i værktøjer, I køber: vælg leverandører, der opfylder WCAG, dokumenterer, hvordan deres automatiserede funktioner beslutter, og lader jer holde et menneske i løkken. Ram jeres egen pligt ind som et datahygiejne- og værdighedsspørgsmål, at vide hvilke personoplysninger I har, kun indsamle det nødvendige og sikre, at et forkert automatiseret svar ikke efterlader en kunde uden en vej til at nå jer. Bed leverandører vise deres tilgængeligheds- og biasholdning, før I underskriver, frem for at opdage hullet efter en klage.

**Stor virksomhed.** I skala er problemet styring på tværs af mange teams: en fælles standard for, hvad der tæller som en væsentlig beslutning, ensartede tilgængeligheds- og biastestporte og et revisionsspor, der beviser, at forklaring, menneskelig gennemgang og klagemulighed findes, hvor de skal. Rejs en etisk gennemgang, der blokerer release, frem for en træning, der ikke ændrer noget, budgettér tilgængeligheds- og forskellig-virkning-arbejdet eksplicit, og overvåg udrullede modeller for drift, så retfærdighed er kontinuerlig frem for et engangsafkrydsningsfelt. Behandl en enkelt designfejl som gentaget på tværs af millioner, for i jeres rækkevidde er den det.

**Offentlig sektor.** Indkøbsregler, åbenhedspligter og offentlig ansvarlighed former hvert valg, og borgere kan ikke fravælge jeres tjeneste ved at gå til en konkurrent. Offentliggør, hvordan afgørende systemer virker, gennem en mekanisme som et algoritmeregister, kræv ved kontrakt, at leverandører oplyser datapraksis og kendte begrænsninger, og byg hver offentlig tjeneste til tilgængelighedsstandarder testet med handicappede brugere, forbindelser med lav båndbredde og minoritetssprogstalende. Garantér en ret til menneskelig gennemgang og en forklaring i almindeligt sprog på hver væsentlig automatiseret beslutning, og hold endelige afgørelser, der skal hvile hos en ansvarlig embedsmand, helt uden for fuld automatisering.

## Eksempler

**Startup.** Et fintech-startup på tre personer, der bygger en automatiseret långivningsfunktion, beslutter, at retfærdighed og værdighed er krav, ikke senere finpudsning. Før lancering tester de modellen for forskellig virkning på tværs af de grupper, de kan måle, skriver de data ned, den bruger, og hvor den ikke bør stoles på, og sikrer, at hver afvist ansøger får en begrundelse i almindeligt sprog og en ét-kliks vej til at nå en menneskelig grundlægger. De bygger tilmeldingsflowet til tilgængelighedsstandarder fra den første skærm, fordi eftermontering senere ville være langsommere og dårligere, og de tilføjer en hurtig tilsidesættelseskanal, så en fejlagtigt frosset konto kan åbnes på minutter frem for at efterlade et rigtigt menneske strandet.

**Stor virksomhed.** En bank, der udruller automatiseret kreditvurdering, behandler retfærdighed som et ingeniørkrav. Før lancering tester den modellen for forskellig virkning på tværs af beskyttede grupper, dokumenterer dataene og deres begrænsninger og bygger en forklaringsfacilitet, så hver afvist ansøger får en forståelig begrundelse og en klar vej til menneskelig gennemgang. En overvågningsproces holder øje med drift og gentester for bias, efterhånden som befolkningen ændrer sig. Da svindelopdagelsessystemet begyndte at fryse mange legitime konti, tilføjede banken en hurtig menneskelig gennemgangskanal og ændrede sit optimeringsmål til at veje kundeskade. Den behandlede de fejlagtigt flagede kunders nød som en reel omkostning, ikke en acceptabel statistik.

**Offentlig sektor.** En kommune offentliggør et algoritmeregister. Det opregner de automatiserede systemer, kommunen bruger i offentlige tjenester, og beskriver hvert systems formål, de data det støtter sig til og hvordan beslutninger kan anfægtes. Kommunens digitale tjenester er bygget til tilgængelighedsstandarder og testet med handicappede brugere, forbindelser med lav båndbredde og minoritetssprogstalende, efter princippet om, at en tjeneste, folk ikke kan fravælge, skal virke for alle. Hver væsentlig automatiseret beslutning bærer en ret til menneskelig gennemgang og en forklaring i almindeligt sprog, så borgere beholder både værdighed og klagemulighed, når statens software afgør noget om deres liv.

## Business case: motivation, ROI og TCO

Business casen for etik og ansvarlighed hviler på tillid, risiko og rækkevidde. Tillid er det varige aktiv. Organisationer, hvis systemer behandler mennesker retfærdigt og åbent, optjener den tillid, der gør folk villige til at bruge dem, og offentlige institutioner afhænger især af legitimitet, som et enkelt højprofileret uretfærdigt system kan knuse. Risiko er den nære driver. Skæve, utilgængelige eller uigennemsigtige systemer bærer i stigende grad regulatoriske bøder, retssager og omdømmeskade, der kan overstige omkostningen ved at bygge ansvarligt. Rækkevidde forstærker begge. I virksomheds- eller offentlig skala gentages en enkelt etisk fejl på tværs af millioner og bliver en overskrift.

Adoptionsomkostningen er reel. Tilgængelighedsarbejde, biastest, forklarings- og klagemekanismer, menneskelig gennemgang i løkken og designtiden til at overveje konsekvenser tilføjer alt sammen indsats, især tidligt. Omkostningen ved *ikke* at adoptere er større og i stigende grad ikke-valgfri: diskriminationsansvar, udelukkelse af store dele af den befolkning, I er forpligtet til at betjene, udgiften til at eftermontere tilgængelighed og ansvarlighed efter lancering og erosionen af tillid, der, når den først er tabt, er dyr og langsom at genopbygge. Når I fremlægger sagen for ledelsen, så ram etik ind som risikostyring og tillidsopbygning, ikke altruisme. Bemærk det stramnende regulatoriske miljø omkring [algoritmisk ansvarlighed](https://en.wikipedia.org/wiki/Algorithmic_accountability) og tilgængelighed. Fremhæv samlet ejeromkostning: at bygge ansvarligt fra begyndelsen er langt billigere end at afhjælpe et system, der allerede har skadet mennesker i skala. For offentlige institutioner så tilføj det mest enkle argument: at betjene borgere retfærdigt er missionen, ikke en begrænsning på den.

## Anti-mønstre og faldgruber

- **Etik som afkrydsningsfelt.** En engangsgennemgang eller -træning, der ikke ændrer noget ved, hvordan systemer faktisk bygges.
- **Eftermontering af tilgængelighed.** At behandle tilgængelighed som et sent tillæg og producere dårligere og dyrere resultater end at designe den ind.
- **Den uansvarlige algoritme.** Afgørende automatiserede beslutninger uden forklaring, uden menneskelig gennemgang og uden vej til at udfordre.
- **Optimering til grusomhed.** At justere rent for aggregeret effektivitet, til systemet stille brutaliserer de mennesker i dets haler.
- **Bias ved forsømmelse.** At antage, at et system er retfærdigt, fordi ingen havde til hensigt uretfærdighed, uden nogensinde at teste for det.
- **"Computeren siger nej."** Frontlinjemedarbejdere og brugere uden mulighed for at tilsidesætte eller sætte spørgsmålstegn ved en automatiseret beslutning, de kan se er forkert.
- **At designe til den selvsikre bruger.** At bygge til den typiske, forbundne, læsekyndige bruger og udelukke alle andre, uforsvarligt for tjenester, folk ikke kan fravælge.
- **Åbenhedsteater.** At offentliggøre uigennemtrængelige oplysninger, der teknisk informerer, men reelt intet forklarer.

## Modenhedsmodel

**Niveau 1: Opstart.** Etik er uadresseret eller rent reaktiv efter en skandale. Tilgængelighed ignoreres eller er minimal. Automatiserede beslutninger er uigennemsigtige, uden forklaring og uden klagemulighed. Bias testes aldrig, og bæredygtighed og social påvirkning overvejes ikke.

**Niveau 2: Udvikling.** En adfærdskodeks findes, og nogle tilgængelighedsstandarder følges, ofte sent. Højprofilerede automatiserede beslutninger får noget menneskeligt tilsyn, men de fleste gør ikke. Bias tjekkes lejlighedsvist, betænkeligheder kan rejses gennem en svag proces, og praksis varierer vidt fra team til team.

**Niveau 3: Standardisering.** Etisk gennemgang er en dokumenteret del af udviklingsprocessen og håndhævet på tværs af organisationen. Tilgængelighed er designet ind og testet med rigtige brugere. Afgørende automatiserede beslutninger bærer som standard forklaring, menneskelig gennemgang og klagemulighed. Biastest og driftsovervågning er rutine, offentlige systemer offentliggør, hvordan de virker, og bæredygtighed måles efter en fælles standard.

**Niveau 4: Styring.** Organisationen måler og styrer sin etiske holdning med data mod baselines: tilgængelighedsoverholdelsesscorer, målinger af forskellig virkning fulgt på tværs af beskyttede grupper over tid, klageraten og tid-til-menneske for anfægtede beslutninger, andelen af afgørende systemer med offentliggjort dokumentation og energi- eller beregningsaftrykket af større systemer. Målinger lukker releases, tærskelbrud udløser undersøgelse, og ledere gennemgår tallene efter en fast kadence frem for at antage, at praksisserne følges.

**Niveau 5: Orkestrering.** Ansvar er indlejret i, hvordan organisationen bygger og tilpasser sig. Tilgængelighed og lighed er ufravigelige standarder verificeret for hele den betjente befolkning, algoritmisk ansvarlighed (åbenhed, retfærdighedstest, klagemulighed, menneskeligt tilsyn) er standard og kontinuerligt overvåget, og etiske betænkeligheder værdsættes som signal, der omformer eller stopper arbejde. Organisationen behandler tillid, retfærdighed og værdighed som kernen i sin mission, integrerer etik med produkt-, risiko- og indkøbsbeslutninger og omafgrænser eller pensionerer systemer, efterhånden som forventninger og dokumentation udvikler sig.

## Idéer til drøftelse

- Hvor går linjen mellem beslutninger, der må automatiseres fuldt, og dem, der skal beholde et menneske meningsfuldt i løkken?
- Hvor megen algoritmisk åbenhed er nok, og hvordan offentliggør I meningsfuldt uden at muliggøre manipulation eller bryde privatlivet?
- Hvem er ansvarlig, når et automatiseret system skader nogen: ingeniøren, lederen, organisationen eller leverandøren?
- Hvordan gør I det reelt sikkert at rejse en etisk indvending frem for karrierebegrænsende?
- Hvilke forpligtelser har en organisation over for brugere, den ikke designede til, og hvor langt skal lighed række?
- Hvordan bør beregningens miljøomkostning indgå i arkitektur- og produktbeslutninger?

## Vigtigste pointer

- Når software træffer afgørende beslutninger om mennesker, er dens skabere ansvarlige for, hvad den gør, ikke blot for, om den opfylder specifikationen.
- Tilgængelighed og lighed er forpligtelser og fejl, når de mangler, ikke valgfrie forbedringer, især for tjenester, folk ikke kan fravælge.
- Afgørende automatiserede beslutninger kræver forklaring, menneskelig gennemgang, klagemulighed og løbende biastest; design ansvarlighed ind frem for at påstå den bagefter.
- Effektivitet optimeret uden hensyn til retfærdighed kan være stille grusom; design til det individuelle fejltilfælde, ikke blot aggregatet.
- I den offentlige sektor bør åbenhed om, hvordan algoritmiske systemer virker, være standarden, med hemmeligholdelse som den snævre undtagelse.
- Business casen er tillid og risiko: at bygge ansvarligt fra begyndelsen er langt billigere end at afhjælpe skade i skala, og for offentlige institutioner er retfærdighed missionen.

## Referencer og videre læsning

- ACM/IEEE-CS, *Software Engineering Code of Ethics and Professional Practice*
- ACM, *Code of Ethics and Professional Conduct*
- Cathy O'Neil, *Weapons of Maths Destruction*
- Virginia Eubanks, *Automating Inequality*
- Safiya Umoja Noble, *Algorithms of Oppression*
- Ruha Benjamin, *Race After Technology*
- Batya Friedman and David G. Hendry, *Value Sensitive Design*
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG)*
- NIST, *AI Risk Management Framework*
- OECD, *Principles on Artificial Intelligence*
- European Union, *General Data Protection Regulation (GDPR)* and the *AI Act*
- UK Government, *Data Ethics Framework* and the *Algorithmic Transparency Recording Standard*
