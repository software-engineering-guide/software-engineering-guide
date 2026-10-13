# 6.6 AI-infrastruktur og drift

## Overblik og motivation

AI-infrastruktur og drift er disciplinen at provisionere, planlægge og køre de specialiserede beregnings-, lagrings- og servingsystemer, som AI-arbejdsbyrder kræver, omkostningseffektivt, pålideligt og observerbart. Moderne AI er dyr at drive. Træning og serving af store modeller kræver knappe acceleratorer ([GPU'er](https://en.wikipedia.org/wiki/Graphics_processing_unit) og [TPU'er](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), netværk med høj båndbredde, vektorlager i stor skala til hentning (at indeksere data som numeriske vektorer, så lignende elementer hurtigt kan findes) og servinglag justeret til latens og gennemløb. At få denne infrastruktur rigtig er forskellen mellem AI, der skalerer bæredygtigt, og AI, der stille æder et budget, mens den underleverer.

For store teams er kerneproblemerne skala, knaphed og omkostning. Acceleratorer er begrænsede og dyre, så planlægning og udnyttelse betyder enormt meget. Ledige GPU'er er brændte penge, og dårligt batchet inferens multiplicerer omkostningen pr. anmodning. Hentningstunge applikationer har brug for [vektordatabaser](https://en.wikipedia.org/wiki/Vector_database), der forbliver hurtige, efterhånden som de vokser. Generative AI-applikationer har brug for promptversionering, evalueringspipelines og observerbarhed (nogle gange kaldet LLMOps) for at blive drevet sikkert og forbedret over tid. Uden fælles infrastruktur og driftsdisciplin kæmper hvert team de samme kampe, og omkostningerne løber løbsk.

Offentlige og regulerede organisationer tilføjer krav om datasuverænitet, sikkerhed og forudsigelige udgifter. De kan have brug for on-premises eller suveræn cloududrulning, så følsomme data og modeller aldrig forlader kontrollerede grænser. De skal forudsige og begrunde infrastrukturudgifter og opfylde sikkerheds- og tilgængelighedsstandarder. AI-infrastrukturbeslutninger i disse sammenhænge har flerårige konsekvenser, så træf dem med indkøb, sikkerhed og udtrædelse for øje.

## Grundprincipper

- Behandl acceleratorberegning som en knap, dyr ressource, der skal planlægges og udnyttes, ikke hamstres.
- Optimér omkostning pr. nyttig arbejdsenhed, ikke rå kapacitet.
- Dimensionér modeller og hardware til opgaven; den største mulighed er sjældent den mest omkostningseffektive.
- Design serving til latens og gennemløb med batching og caching som førsteklasses teknikker.
- Gør AI-systemer observerbare: følg omkostning, latens, kvalitet og fejl kontinuerligt.
- Versionér og evaluér prompts og modeller med samme stringens som kode.
- Planlæg for portabilitet, og undgå indlåsning i infrastruktur- og servingvalg.

## Anbefalinger

### Planlæg og kontrollér acceleratorberegning

Forudsig efterspørgsel efter træning og inferens hver for sig, da de har forskellig form. Træning er stødvis og kan planlægges; inferens er kontinuerlig og latensfølsom. Brug planlæggere og kvoter til at dele knappe GPU'er og TPU'er på tværs af teams, prioritere arbejdsbyrder og drive udnyttelsen op. Mål udnyttelse, og behandl kronisk ledighed som et problem, der skal rettes. Bland reserveret kapacitet til baselinebelastning med on-demand- eller spotkapacitet til spidsbelastninger for at kontrollere omkostning. Overvej, om billigere eller mindre acceleratorer, eller CPU-inferens til lette modeller, ville række. Vælg mellem cloud, on-premises og hybrid ud fra omkostning i jeres skala, datasuverænitetsbehov og belastningsspidsmønstre, og behold en udtrædelsessti.

### Byg hentningsinfrastruktur: embeddings og vektordatabaser

For hentningsudvidede applikationer så opstil infrastruktur til at generere [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numeriske vektorrepræsentationer, der placerer lignende elementer tæt på hinanden) og gemme dem i en vektordatabase, der understøtter hurtig [tilnærmet nærmeste-nabo-søgning](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (at finde de mest lignende vektorer uden udtømmende at sammenligne hver) i jeres skala. Planlæg for tre ting: omkostning og latens ved embeddinggenerering, indeksfriskhed, når dokumenter ændrer sig, og driftsbyrden ved at holde indekser konsistente. Evaluér, om en dedikeret vektordatabase, en vektorkapabel udvidelse af en eksisterende database eller en administreret tjeneste bedst passer til jeres skala og indlåsningstolerance. Overvåg hentningslatens og recall, fordi hentningskvalitet direkte afgør applikationskvaliteten.

### Optimér modelserving: batching, caching og latens

Serving er, hvor inferensomkostning og brugeroplevelse afgøres. Brug **batching** til at behandle flere anmodninger sammen og hæve acceleratorgennemløbet, og afvej batchstørrelse mod latens. Brug **caching** aggressivt: cache identiske eller semantisk lignende anmodninger, cache embeddings, og udnyt prompt- eller præfikscaching, hvor platformen understøtter det, for at undgå at genberegne delt kontekst. Sæt klare latensmål, og mål halelatens, ikke blot gennemsnit. Dirigér anmodninger til rigtigt dimensionerede modeller: en lille model til de lette tilfælde, en større kun når nødvendigt. Autoskalér serving efter efterspørgsel, og belastningstest før lancering, så I kender jeres kapacitet og omkostningskurve.

### Praktisér LLMOps: promptversionering, evalueringspipelines og observerbarhed

Behandl prompts som versionerede artefakter i versionsstyring, med gennemgang og evnen til at rulle tilbage. Byg evalueringspipelines, der kører offline-testsuiter automatisk, når prompts eller modeller ændres, så I fanger regressioner før udgivelse. Instrumentér produktion omfattende: log input, output, latens, tokenforbrug, omkostning og fejl, med sampling og privatlivsforanstaltninger. Følg kvalitetssignaler og brugerfeedback online. Denne observerbarhed lader jer fange forringelse, kontrollere omkostning, fejlsøge og forbedre systemer sikkert: den operationelle rygrad i generativ AI i produktion.

### Styr omkostning ubarmhjertigt og observerbart

Tilskriv AI-udgifter til teams og anvendelser, så omkostning er synlig og ejet. Sæt budgetter og alarmer, overvåg omkostning pr. anmodning og pr. udfald, og gennemgå de største omkostningsdrivere regelmæssigt. Træk i de løftestænger, I har: modeldimensionering, caching, batching, trimning af prompt og kontekst og valg af den billigste udrulning, der opfylder kravene. AI-omkostninger kan skalere med brug på overraskende måder, så kontinuerlig omkostningsobserverbarhed er essentiel for at undgå ubehagelige overraskelser.

## Afvejninger: fordele og ulemper

| Beslutning | Mulighed A | Mulighed B | Afvejning |
|---|---|---|---|
| Beregningslokation | Cloud | On-premises | Elasticitet og lav omkostning på forhånd versus kontrol, suverænitet og økonomi i stabil drift |
| Kapacitet | Reserveret | On-demand/spot | Forudsigelig omkostning versus fleksibilitet og afbrydelsesrisiko |
| Batchstørrelse | Store batches | Små batches | Gennemløb og omkostning versus latens |
| Modelstørrelse | Stor model | Lille model | Kvalitet versus omkostning og hastighed |
| Vektorlager | Dedikeret database | Udvidelse af eksisterende database | Ydeevne i skala versus enkelhed og færre systemer |
| Caching | Aggressiv | Minimal | Lavere omkostning og latens versus friskhed og kompleksitet |

Den dominerende afvejning er omkostning versus latens og kvalitet. Batching, caching og mindre modeller skærer omkostning, men kan tilføje latens eller reducere kvalitet. Den rette balance afhænger af jeres applikations tolerance. On-premises versus cloud afvejer kontrol og økonomi i stabil drift mod elasticitet og lav forpligtelse, en beslutning kraftigt formet af datasuverænitetsbehov og skala.

## Spørgsmål til drøftelse med dit team

1. **Hvad er vores omkostning pr. nyttigt udfald i dag, og hvilken løftestang ville flytte den mest?** Rå kapacitet og gennemsnit pr. anmodning skjuler det tal, der betyder noget: hvad det koster at levere én reel enhed værdi, og hvordan det skalerer med brug. For et stort team er hullet mellem en optimeret og en ikke-optimeret udrulning ofte flere gange i udgift, så dette spørgsmål forvandler en vag bekymring over regningen til en rangeret liste over rettelser. Tag nuværende omkostningstilskrivning pr. team og anvendelse, tendenser pr. anmodning og pr. udfald og de største omkostningsdrivere med. Drøft løftestængerne i rækkefølge efter gevinst: modeldimensionering, caching (herunder præfiks- og semantisk caching), batching og trimning af prompt eller kontekst. I det offentlige så tilføj presset for at forudsige og begrunde flerårige udgifter. Svaret bør give hver øverste omkostningsdriver en ejer og en løftestang, ikke et skuldertræk.

2. **Hvis vores nuværende inferensudbyder fordoblede sin pris eller gik ned i morgen, hvor hurtigt kunne vi skifte?** Stille indlåsning er let at bygge og smertefuld at undslippe, og servingstakke er, hvor den gemmer sig dybest. For virksomheder og især det offentlige er portabilitet et indkøbs- og kontinuitetskrav, ikke en finesse. Tag jeres arkitektur med: om modeller sidder bag en intern grænseflade, om prompts og evalueringssuiter er portable, og hvor meget udbyderspecifik servingadfærd I afhænger af. Signalet at holde øje med er, om nogen nogensinde har kørt jeres evalueringssuite mod en anden udbyder eller et andet udrulningsmål. Hvis det ville tage måneder at skifte og kræve omskrivning af kerneveje, så behandl det som en designdefekt, der skal adresseres nu, da suveræne og on-premises muligheder kan blive obligatoriske med kort varsel.

3. **Hvad er vores acceleratorudnyttelse lige nu, og hvor meget brænder ledige GPU'er og ikke-batchet inferens af?** Acceleratorer er knappe og dyre, så kronisk ledighed og serving pr. anmodning dræner stille budgetter, der kunne finansiere mere kapacitet. For en stor organisation, der deler GPU'er på tværs af teams, afslører dette spørgsmål, om planlægning, kvoter og prioriteter faktisk holder udnyttelsen høj, eller om hamstret, underudnyttet hardware er normen. Tag reelle udnyttelsestal, jeres batching- og cachingholdning og jeres målinger af halelatens, ikke blot gennemsnit, med, da brugere mærker den langsomme hale. Drøft, om efterspørgsel efter træning og inferens forudsiges hver for sig, givet deres forskellige former, og om en mindre model eller CPU-inferens ville række til lette tilfælde. Svaret bør pege på specifik ledig kapacitet at generobre og specifikke anmodninger at batche eller dirigere til en rigtigt dimensioneret model.

4. **Når en prompt- eller modelændring leveres, hvad forhindrer en stille kvalitets- eller omkostningsregression i at nå brugerne?** En servingstak kan se sund ud på latens og oppetid, mens de svar, den returnerer, stille bliver dårligere, eller en ny prompt fordobler tokenforbruget pr. anmodning. For et stort team, hvor mange grupper redigerer prompts og bytter modeller uafhængigt, er en ugatet ændring en produktionshændelse, der venter på at ske, og sprængradius vokser med hvert team på den fælles platform. Tag jeres evalueringsdækning: hvilke prompts og modeller der har offline-testsuiter, om disse suiter kører automatisk ved hver ændring, hvilke kvalitets- og omkostningstærskler der lukker porten for en udgivelse, og hvor hurtigt I kan rulle tilbage. Drøft, om prompts bor i versionsstyring med gennemgang, eller om nogen stadig kan redigere en live systemprompt i hånden. I virksomheds- og offentlige sammenhænge så bind hver ændring til et revisionsspor og en navngiven godkender, for en tilsynsmyndighed, der spørger "hvem ændrede dette, og hvad testede I", har brug for et svar, der er registreret, ikke husket.

5. **Hvordan afgør vi mellem cloud, on-premises og suveræn udrulning, og har vi prissat den reelle økonomi i stabil drift frem for piloten?** Valget af beregningslokation sætter jeres omkostningskurve, jeres datasuverænitetsholdning og jeres udtrædelsesmuligheder i årevis, men det træffes ofte på en pilots cloudregning, der ikke ligner produktion i skala. For en stor organisation er elastisk cloudkapacitet billig at starte og kan blive den største enkeltpost, når inferens kører kontinuerligt, mens on-premises bytter lav forpligtelse for kontrol og økonomi i stabil drift. Tag forudsagte volumener for træning og inferens, break-even-punktet, hvor reserveret eller ejet hardware slår on-demand, jeres dataresidens- og sikkerhedsbegrænsninger og de belastningsspidsmønstre, der taler for hybrid, med. I offentlige og regulerede sammenhænge så vej krav om suveræn cloud eller on-premises, der kan blive obligatoriske med kort varsel, og bekræft at arkitekturen holder modeller bag en intern grænseflade, så et tvunget skifte ikke omskriver kerneveje.

6. **Ejer vi faktisk vores AI-udgift, og kan hvert team se og stå til ansvar for den omkostning, det driver?** AI-omkostning skalerer med brug på måder, der overrasker folk, og uden tilskrivning lander regningen som ét uigennemsigtigt tal, intet team føler sig ansvarligt for at skrumpe. I en stor organisation er omkostning, ingen ejer, omkostning, ingen optimerer, så spørgsmålet er, om udgift tagges til teams og anvendelser med budgetter, alarmer og tendenser pr. udfald, eller om den først opdages, når økonomien eskalerer. Tag jeres omkostningstilskrivningsmodel, de største drivere pr. team og de løftestænger, hver ejer kontrollerer: dimensionering, caching, batching og trimning af kontekst, med. For virksomheds- og offentlige budgetter så tilføj disciplinen at forudsige og begrunde flerårige infrastrukturudgifter, da et offentligt organ, der ikke kan forklare sin beregningsregning linje for linje, vil have svært ved at forsvare den i gennemgang.

## Sektorperspektiv

**Startup.** Ejer ingen infrastruktur, I kan undgå. Kald en hostet inferens-API, dirigér lette anmodninger til en lille billig model og forbehold en større til svære tilfælde, og cache aggressivt, så gentagne prompts ikke koster noget. Brug en administreret vektordatabase frem for at drive jeres egen, hold prompts i git med et kort evalueringsscript før hver ændring, og log omkostning pr. anmodning, så en løbsk regning viser sig, før den gør ondt. Jeres knappeste ressource er ingeniøropmærksomhed, så køb driftsegnethed og hold det billigt at skifte.

**Lille virksomhed.** Uden et platformsteam så behandl serving, hentning og observerbarhed som ting, I køber inde i værktøjer, I allerede bruger, ikke systemer, I bemander. Foretræk administreret inferens og administreret vektorsøgning med gennemsigtig, forudsigelig prissætning, og sæt et hårdt udgiftsloft og en faktureringsalarm fra dag ét. Ram valget ind som køb versus byg ærligt: at drive GPU'er eller et vektorindeks betaler sig sjældent i jeres volumen, og en lille model bag en hostet API opfylder som regel behovet til en brøkdel af indsatsen.

**Stor virksomhed.** Problemet er en fælles, asfalteret platform på tværs af mange teams: poolede acceleratorer med planlæggere, kvoter og prioriteter for at drive udnyttelsen op, standard batching og caching, dimensioneringsroutere og omkostning tilskrevet hvert team og hver anvendelse. Luk porten for prompt- og modelændringer med automatiserede evalueringssuiter, standardisér grænsefladelaget, så udbydere og udrulningsmål forbliver udskiftelige, og styr omkostning pr. udfald som en førsteklasses måling frem for at lade hver gruppe genopfinde dyr, underudnyttet infrastruktur.

**Offentlig sektor.** Datasuverænitet, sikkerhed og forudsigelige udgifter former hvert valg. Foretræk on-premises eller suveræn cloududrulning, så følsomme data og modeller bliver inden for kontrollerede grænser, planlæg knappe GPU'er på tværs af afdelinger med kvoter, I kan begrunde i indkøb, og forudsig kapacitet for at forsvare flerårige udgifter linje for linje. Versionér og evaluér prompts og modeller med et registreret revisionsspor, hold omfattende observerbarhed over omkostning og kvalitet, og hold modeller bag en intern grænseflade, så et tvunget skifte til en ny udbyder eller en suveræn platform ikke efterlader jer strandet.

## Eksempler

**Startup.** Et lille startup, der kørte en AI-skrivefunktion, holdt sin regning fornuftig uden at eje nogen GPU'er. Det kaldte en hostet inferens-API, dirigerede lette anmodninger til en billigere lille model og gemte den større til svære tilfælde og cachede svar på gentagne prompts. Det gemte sine prompts i git med et kort evalueringsscript, der kørte før hver ændring, brugte en administreret vektordatabase til hentning, så det ikke skulle drive en, og loggede omkostning pr. anmodning, så grundlæggerne kunne se udgiften stige, før den blev en overraskelse.

**Stor virksomhed.** Et mediefirma, der kørte en LLM-funktion med meget trafik, skar inferensomkostninger væsentligt. Det dirigerede lette anmodninger til en lille model og forbeholdt en større model til svære. Det cachede svar på gentagne forespørgsler og aktiverede præfikscaching til sin fælles systemprompt. Det kørte GPU'er gennem en fælles planlægger for at holde udnyttelsen høj, versionerede alle prompts i git med en automatiseret evalueringssuite, der lukkede porten for ændringer, og instrumenterede omkostning pr. anmodning, så hvert produktteam ejede sin udgift.

**Offentlig sektor.** Et nationalt agentur med strenge datasuverænitetsregler udrullede sine AI-systemer on-premises, så følsomme data og modeller aldrig forlod dets kontrollerede miljø. Det planlagde knappe GPU'er på tværs af afdelinger med kvoter og prioriteter, forudsagde kapacitet for at begrunde flerårigt indkøb og byggede en vektorsøgningsplatform til hentning over officielle dokumenter. Prompts og modeller blev versioneret og evalueret før udgivelse. Omfattende observerbarhed fulgte omkostning og kvalitet, og arkitekturen holdt modeller bag en intern grænseflade for at bevare en udtrædelsessti og undgå indlåsning.

## Business case: motivation, ROI og TCO

Motivationen for disciplineret AI-infrastruktur er ligefrem. AI i skala er dyr, og hullet mellem en optimeret og en ikke-optimeret udrulning er ofte flere gange i udgift. ROI kommer fra højere acceleratorudnyttelse, lavere omkostning pr. anmodning gennem batching og caching, rigtigt dimensionerede modeller og at undgå overprovisionering. Observerbarhed og evalueringspipelines betaler sig ved at forebygge dyre hændelser og muliggøre sikker iteration.

TCO spænder over acceleratorberegning (den største linje for mange arbejdsbyrder), vektorlager, servinginfrastruktur, netværk og platforms- og driftspersonalet til at drive det. Vej det mod omkostningen ved ikke at investere: løbske inferensregninger, dårlig latens, der underminerer adoption, og manglende evne til at skalere. For det offentlige så tilføj omkostningen ved at fejle suverænitets- eller sikkerhedskrav. Før sagen over for ledelsen ved at vise tendenser i omkostning pr. udfald og en asfalteret platform, der lader mange teams udrulle AI effektivt, frem for at hver bygger dyr, underudnyttet infrastruktur.

## Anti-mønstre og faldgruber

- **Ledige acceleratorer.** At dedikere knappe GPU'er til teams, der lader dem være underudnyttede.
- **Ingen batching eller caching.** At servere hver anmodning individuelt og genberegne delt kontekst.
- **Største model som standard.** At bruge en dyr model, hvor en lille ville række.
- **Omkostningsblindhed.** Ingen tilskrivning, budgetter eller synlighed af omkostning pr. anmodning, til regningen ankommer.
- **Uversionerede prompts.** At ændre prompts i produktion uden versionering eller evalueringsport.
- **Forsømmelse af halelatens.** At optimere gennemsnitlig latens, mens brugere lider under langsomme haler.
- **Stille indlåsning.** At bygge dybt på én udbyders servingstak uden portabilitet.

## Modenhedsmodel

1. **Opstart.** Ad hoc GPU-tildeling, der reagerer på den, der beder højest, ingen batching eller caching, ingen omkostningssynlighed, til regningen ankommer, prompts redigeret live og uversioneret, minimal overvågning.
2. **Udvikling.** Nogle teams adopterer fælles planlægning, caching og versionsstyrede prompts, men praksis er inkonsistent på tværs af organisationen: én gruppe batcher og evaluerer, mens en anden stadig serverer hver anmodning individuelt og ændrer prompts i hånden.
3. **Standardisering.** En dokumenteret, asfalteret platform er håndhævet i hele organisationen: fælles planlægning med kvoter og prioriteter, standard batching, caching og dimensionering, vektorinfrastruktur til hentning, automatiserede evalueringspipelines, der lukker porten for hver prompt- eller modelændring, og omkostningstilskrivning til teams og anvendelser.
4. **Styring.** Platformen måles og styres mod baselines: acceleratorudnyttelse, omkostning pr. nyttigt udfald, halelatens, hentnings-recall og kvalitetsregressioner pr. ændring følges med alarmer og tærskler, omkostning ejes af hvert team, og go/no-go på en ændring afgøres på dokumentation frem for intuition.
5. **Orkestrering.** Infrastruktur forbedres og tilpasses løbende: routing, batching og skalering justerer sig selv efter live omkostnings- og kvalitetssignaler, kapacitet genbalanceres på tværs af teams og mellem cloud-, on-premises- og suveræne mål, efterhånden som efterspørgsel og begrænsninger skifter, portabilitet øves, og infrastrukturplanlægning er integreret med produkt, sikkerhed og indkøb.

## Idéer til drøftelse

- Hvordan driver I acceleratorudnyttelse op uden at sulte prioriterede arbejdsbyrder?
- Hvor er den rette balance mellem batching og caching for jeres latenskrav?
- Hvornår retfærdiggør on-premises eller suveræn udrulning sin omkostning over cloud?
- Hvordan tilskriver og kontrollerer I AI-udgifter på tværs af mange teams?
- Hvad bør lukke porten for en prompt- eller modelændring fra at nå produktion?
- Hvordan holder I servinginfrastruktur portabel nok til at skifte udbyder?

## Vigtigste pointer

- Acceleratorer er knappe og dyre; planlæg, del og udnyt dem bevidst.
- Batching, caching og modeldimensionering er de primære løftestænger for omkostning og latens.
- Hentningsapplikationer har brug for veldrevet embedding- og vektorsøgningsinfrastruktur.
- LLMOps (promptversionering, evalueringspipelines og observerbarhed) er den operationelle rygrad i generativ AI.
- Styr omkostning observerbart, og bevar portabilitet for at undgå indlåsning.

## Referencer og videre læsning

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
