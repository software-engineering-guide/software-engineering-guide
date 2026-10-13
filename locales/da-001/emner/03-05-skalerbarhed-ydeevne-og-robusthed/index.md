# 3.5 Skalerbarhed, ydeevne og robusthed

## Overblik og motivation

[Skalerbarhed](https://en.wikipedia.org/wiki/Scalability), ydeevne og robusthed er tre adskilte kvaliteter, og folk blander dem ofte sammen. **Ydeevne** er, hvor hurtigt systemet svarer, og hvor meget arbejde det udfører pr. ressourceenhed. **Skalerbarhed** er, hvor godt det bevarer ydeevne, når belastningen vokser. **Robusthed** er, hvor godt det bliver ved med at virke, eller nedgraderer elegant, når ting fejler. Et system kan være hurtigt, men uskalerbart (fremragende ved lav belastning, kollapser ved høj), skalerbart, men skrøbeligt (håndterer volumen, men falder om, når én komponent fejler), eller robust, men langsomt. En stor organisation har brug for alle tre, designet ind fra begyndelsen, fordi at eftermontere nogen af dem efter lancering er dyrt og forstyrrende.

For virksomheds- og offentlige systemer er konsekvenserne af at tage fejl offentlige og alvorlige. Tænk på en ydelsesportal, der bøjer sig på den første dag af en ny ordning, et skatteindberetningssystem, der får timeout ved fristen, eller en betalingsplatform, der går ned under spidsbelastning i julehandlen. Det er de fejl, der gør overskrifter, udløser undersøgelser og udhuler offentlig tillid. Disse systemer står også over for stærkt toppede, ofte juridisk tidsfastsatte belastninger (indberetningsfrister, tilmeldingsvinduer, lønningsdage) og strenge tilgængeligheds- og genopretningsforpligtelser. Du må planlægge kapacitet til forudsigelige bølger, nedgradere elegant under de uforudsigelige og genoprette inden for definerede tids- og datatabsgrænser efter en katastrofe. Det er ingeniørarbejde med en dimension af offentlig ansvarlighed.

Dette kapitel dækker horisontal versus vertikal skalering, tilstandsløshed og [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) som muliggørere af skala, [belastningsfordeling](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [autoskalering](https://en.wikipedia.org/wiki/Autoscaling) og kapacitetsplanlægning, ydeevneoptimering med eksplicitte budgetter, robusthedsmønstre og [kaosingeniørkunst](https://en.wikipedia.org/wiki/Chaos_engineering) samt [katastrofegenopretning](https://en.wikipedia.org/wiki/Disaster_recovery) på tværs af regioner rammet ind af RTO, RPO og forretningskontinuitet. Det samlende budskab er, at disse kvaliteter er produktet af bevidst design og løbende test, ikke af håb.

*Se også:* kapitel 3.3 (distribuerede systemer), kapitel 9.1 (site reliability engineering) og kapitel 9.2 (observerbarhed og overvågning).

## Grundprincipper

- **Design til udskalering, ikke opskalering.** Vertikal skalering har et loft og et [enkelt fejlpunkt](https://en.wikipedia.org/wiki/Single_point_of_failure); horisontal skalering er, hvordan du når stor, robust skala.
- **Tilstandsløshed er muliggøreren af horisontal skala.** Hvis enhver anmodning kan gå til enhver instans, kan du frit tilføje og fjerne kapacitet.
- **Du kan ikke forbedre det, du ikke måler.** Ydeevnearbejde drives af profilering og belastningstest mod eksplicitte budgetter, aldrig af gætteri.
- **Alt fejler; design til det.** Antag at komponenter vil fejle, og byg, så systemet overlever deres fejl.
- **Elegant nedgradering slår hård fejl.** Et delvist fungerende system, der afgiver ikke-essentielle features, er bedre end et totalt nedbrud.
- **Kapacitet planlægges, bølger absorberes.** Prognosticér forudsigelig belastning; brug autoskalering og margen til resten.
- **Genopretningsmål er forretningsbeslutninger.** RTO og RPO vælges af forretningen mod omkostning og konstrueres derefter til.
- **Test robusthed bevidst.** Du ved ikke, at et system er robust, før du har fået det til at fejle med vilje.

## Anbefalinger

### Foretræk horisontal skalering, og design tilstandsløse tjenester

Vertikal skalering (større maskiner) er enkel og nogle gange det rette første skridt, men den rammer et hårdt loft, bliver uforholdsmæssigt dyr i toppen og efterlader et enkelt fejlpunkt. **Horisontal skalering** (flere maskiner bag en belastningsfordeler) skalerer langt videre og forbedrer tilgængeligheden, fordi tabet af én instans er til at overleve. Forudsætningen er **tilstandsløshed**. Hold ingen klientsession eller anmodningstilstand på instansen; skub den til et fælles lager (database, cache, token). Tilstandsløse tjenester kan tilføjes, fjernes, erstattes og belastningsfordeles frit, hvilket er det, der gør både autoskalering og rullende udrulning mulig. Hvor tilstand må partitioneres, så **shard** efter en nøgle, der fordeler belastningen jævnt og holder relaterede data på samme shard.

### Belastningsfordel, autoskalér og planlæg kapacitet

Sæt en **belastningsfordeler** foran hvert skaleret lag for at fordele trafik og dirigere uden om usunde instanser via sundhedstjek. Konfigurér **autoskalering** til at tilføje kapacitet, når en ledende indikator (CPU, anmodningskødybde, latens) krydser en tærskel, og fjerne den, når belastningen falder. Justér skaleringshastighed og afkølinger, så du hverken halter efter en spids eller svinger. Autoskalering er ikke en erstatning for **kapacitetsplanlægning**. For forudsigelige, forretningskritiske bølger (skattefrister, tilmeldingsperioder, salgsbegivenheder) så prognosticér belastningen, forhåndsprovisionér eller forvarm kapacitet, og belastningstest til det mål på forhånd. Autoskalering alene kan ikke reagere øjeblikkeligt på et trinskift, og koldstart tilføjer latens netop, når du har mindst råd til det. Hold altid margen. At køre ved 100 % efterlader intet rum til at absorbere spidser eller fejl.

### Konstruér ydeevne mod eksplicitte budgetter

Sæt **ydeevnebudgetter** (konkrete mål som p95 API-latens under 200 ms, side interaktiv under 2 sekunder eller omkostning pr. transaktion under en tærskel) og håndhæv dem i test og overvågning, så regressioner får pipelinen til at fejle frem for at nå brugerne. Driv optimering med **måling**. Profilér for at finde den faktiske flaskehals, som sjældent er, hvor du gætter, og belastningstest for at finde, hvor systemet knækker, og hvordan det opfører sig nær den grænse. Fokusér på den kritiske sti og halen (p95/p99), for i stor skala dominerer halelatenser brugeroplevelsen. Optimér den største flaskehals først, mål igen, og stop, når du opfylder budgettet. At overoptimere allerede tilstrækkelig kode er spildt indsats.

### Byg robusthedsmønstre ind, og validér med kaosingeniørkunst

Anvend robusthedsmønstrene fra distribuerede systemer: timeouts, afgrænsede genforsøg med backoff, [circuit breakers](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (der fejler hurtigt, når en afhængighed er usund) og skotter (der isolerer ressourcepuljer, så én fejl ikke kan udtømme resten), plus **elegant nedgradering** (afgiv eller forenkl ikke-essentielle features under stress: slå anbefalinger fra, server cachet indhold, sæt ikke-hastende arbejde i kø) og **belastningsafgivelse** (afvis eller drossel overskydende anmodninger for at beskytte kernen frem for at kollapse helt). Eliminér enkelte fejlpunkter gennem redundans på hvert lag. **Validér** derefter robusthed med kaosingeniørkunst. Injicér fejl bevidst (dræb instanser, tilføj latens, afbryd en afhængighed, fejl en zone) i kontrollerede eksperimenter, begyndende i test og modnes til game days i produktion, for at bevise at systemet opfører sig som designet. Robusthed, der aldrig er testet, er kun en hypotese.

### Planlæg multiregion, katastrofegenopretning og forretningskontinuitet

Beslut genopretningsmålene eksplicit: **RTO** (Recovery Time Objective, hvor længe du kan være nede) og **RPO** (Recovery Point Objective, hvor meget data du kan tåle at miste). Det er forretningsbeslutninger med direkte omkostningskonsekvenser, og de driver arkitekturen. Mulighederne spænder i omkostning og hastighed: backup-og-gendan (billigst, langsomst), pilot light, varm standby og aktiv-aktiv multiregion (dyrest, næsten nul RTO/RPO). Vælg det niveau, hvert systems kritikalitet berettiger. Ikke alt har brug for aktiv-aktiv. Replikér data på tværs af regioner i overensstemmelse med det valgte RPO, automatisér failover, og frem for alt **test failover regelmæssigt**. Utestet katastrofegenopretning fejler pålideligt, når den endelig er nødvendig. Pak det hele ind i en **forretningskontinuitetsplan**, der dækker mennesker, kommunikation og manuelle nødløsninger, ikke kun teknologi.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper |
|---|---|---|
| Vertikal skalering | Enkel, ingen kodeændring, lav indledende indsats | Hårdt loft, dyr i toppen, enkelt fejlpunkt |
| Horisontal skalering | Næsten ubegrænset skala, forbedrer tilgængelighed | Kræver tilstandsløshed, belastningsfordeling, mere drift |
| Autoskalering | Matcher omkostning til efterspørgsel, håndterer variabel belastning | Reagerer med forsinkelse; koldstart; kan svinge hvis fejljusteret |
| Aktiv-aktiv multiregion | Næsten nul RTO/RPO, overlever regionstab | Højeste omkostning og kompleksitet, svær datakonsistens |
| Backup-og-gendan DR | Billigst, simplest | Lang RTO, større datatabsvindue |

Den centrale afvejning er omkostning versus sikkerhed. Hvert trin i skalerbarhedsmargen, ydeevne og genopretningsevne koster penge og kompleksitet, og afkastet er ikke-lineært. At gå fra 99,9 % til 99,99 % tilgængelighed, eller fra en times RTO til sekunder, kan multiplicere omkostningen. Disciplinen er at dimensionere hver investering efter systemets faktiske kritikalitet og forretningens tolerance for nedetid og datatab, frem for refleksivt at konstruere alt til det højeste niveau. Et borgervendt betalingssystem fortjener aktiv-aktiv redundans; et internt rapporteringsværktøj gør ikke.

## Spørgsmål til drøftelse med dit team

1. **Da jeres sidste alvorlige hændelse skete, hvilken af de tre (ydeevne, skalerbarhed, robusthed) fejlede egentlig, og rettede I den rigtige?** Kapitlet adskiller dem bevidst: et system kan være hurtigt, men kollapse under belastning, skalere, men falde om, når en komponent dør, eller overleve fejl, mens det er langsomt. Teams fejldiagnosticerer ofte, tilføjer kapacitet til et robusthedsproblem eller hærder et system, der blot var underprovisioneret til en bølge. Gå de to seneste alvorlige hændelser igennem og navngiv, hvilken kvalitet der gik i stykker, og hvad responsen faktisk forbedrede. Distinktionen ændrer rettelsen: tilstandsløshed og sharding for skala, redundans og circuit breakers for robusthed, profilering og budgetter for ydeevne. At få kategorien rigtig er forskellen mellem at bruge penge på kuren og at bruge dem på et symptom.

2. **Får ydeevneregressioner jeres pipeline til at fejle, eller når de brugerne, før nogen lægger mærke til det?** Et ydeevnebudget (p95-latens, tid til interaktiv side, omkostning pr. transaktion) beskytter kun brugerne, hvis det håndhæves automatisk, så en ændring, der sprænger det, får bygget til at fejle frem for at blive udgivet. I et stort team med mange bidragydere kryber latens ind gennem tusind små commits, og uden en port rådner halen langsomt, til en lancering afslører den. Tag jeres nuværende budgetter med og tjek, om de er koblet ind i CI og overvågning, og om de sigter mod p95 og p99 frem for gennemsnit, fordi halen er, hvad brugerne mærker i stor skala. Hvor intet budget findes, er det første træk at sætte et. Håndhævelse er, hvad der forvandler en god intention til en egenskab, der overlever teamvækst.

3. **Under stress, hvad afgives først, og designede I den rækkefølge, eller vil I opdage den i nedbruddet?** Elegant nedgradering og belastningsafgivelse betyder, at systemet opgiver ikke-essentielt arbejde for at beskytte kernen, men kun hvis I på forhånd har besluttet, hvad der er essentielt. For en borgervendt tjeneste er den rangering ofte en politisk beslutning: at indgive en selvangivelse skal overleve, selv om statusdashboards og historiske opslag går i sort. Hvis ingen har valgt, afgiver systemet, hvad der end fejler først, hvilket kan være netop det, brugerne har mest brug for. List jeres features i prioriteret rækkefølge og bekræft, at arkitekturen kan droppe de lavt prioriterede (cachede svar, deaktiverede anbefalinger, ikke-hastende arbejde sat i kø) uden at tage den kritiske sti med sig. Test det derefter under reel belastning, fordi utestet nedgradering kun er et håb.

4. **For jeres mest kritiske system, hvad er RTO og RPO, hvem valgte faktisk de tal, og hvornår beviste I sidst, at I kan opfylde dem?** Recovery Time Objective (hvor længe I kan være nede) og Recovery Point Objective (hvor meget data I kan tåle at miste) er forretningsbeslutninger med direkte omkostningskonsekvenser, og alligevel opfindes de i et stort team ofte af den, der skrev runbooken, frem for at blive ejet af de mennesker, der er ansvarlige for tjenesten. Det modstridende træk er omkostning mod sikkerhed: at skrumpe RTO fra en time til sekunder eller RPO fra minutter til nul kan multiplicere infrastrukturregningen, så det rette tal er det, forretningen faktisk vil betale for, ikke det mest imponerende. Tag de dokumenterede mål med, datoen for den seneste reelle failover-test og den målte tid og det datatab, testen producerede, fordi et utestet mål er et ønske. I virksomheds- og offentlige sammenhænge kan disse tal være fastsat ved lov, kontrakt eller SLA, så navngiv, hvem der godkender dem, og om den seneste prøve opfyldte forpligtelsen eller stille missede den.

5. **For jeres største forudsigelige bølge, stoler I så på, at autoskalering reagerer i øjeblikket, eller har I prognosticeret belastningen, forhåndsprovisioneret og belastningstestet til det mål?** Autoskalering reagerer med forsinkelse, og koldstart tilføjer latens netop, når I har mindst råd til det, så et kendt trinskift (en indberetningsfrist, et tilmeldingsvindue, en salgsbegivenhed) er præcis det tilfælde, hvor reaktiv skalering fejler, og bevidst kapacitetsplanlægning vinder. Spændingen er omkostning: at forvarme kapacitet til en spids betyder at betale for margen, der står ubrugt det meste af året, og fristelsen er at håbe, autoskalering dækker det gratis. Tag sidste års spidstal, dette års prognose med vækst og resultaterne af en belastningstest kørt til et multiplum af den prognose frem for til dagens gennemsnitlige trafik med. For en offentlig eller virksomhedstjeneste, der står over for en juridisk tidsfastsat bølge, så tilføj konsekvensen af at tage fejl, for en ydelsesportal eller et skattesystem, der bøjer sig på dag ét, bliver til en offentlig undersøgelse, ikke blot en langsom eftermiddag.

6. **Har I nogensinde bevidst fejlet en komponent i produktion, og matcher hvert systems redundansniveau faktisk dets kritikalitet og omkostning?** Robusthed, der aldrig er testet, er en hypotese, og de niveauer, I kan købe, spænder fra billig backup-og-gendan over varm standby til dyr aktiv-aktiv multiregion, så disciplinen er at bruge sikkerhed, hvor den er berettiget, frem for at forgylde alt eller beskytte intet. De modstridende hensyn er sprængradius og budget: kaoseksperimenter skal have rækværk og en afbrydelseskontakt, og aktiv-aktiv til et internt rapporteringsværktøj er spild, mens kun backup til en betalingsplatform er forsømmelse. Tag en opgørelse over jeres enkelte fejlpunkter med, redundansniveauet for hvert kritisk system og dokumentation for den seneste kontrollerede fejlinjektion og hvad den afslørede. I virksomheds- og offentlige porteføljer så afbild hvert niveau til en dokumenteret kritikalitetsvurdering, så en revisor kan se, at pengene følger risikoen, og så ingen skal forsvare udgiften for første gang under nedbruddet.

## Sektorperspektiv

**Startup.** Du kan ikke forudsige, om en lancering bringer halvtreds tilmeldinger eller halvtredstusind, så køb skala frem for at bygge den: kør tilstandsløse tjenester bag en administreret belastningsfordeler og lad platformen autoskalere efter anmodningsrate. Sæt ét beskedent ydeevnebudget og vælg administrerede datalagre, så en spids ikke tvinger en rearkitektur kl. 2 om natten. Spring multiregion-katastrofegenopretning og kaosprogrammer over for nu; hold testede backups og brug din knappe ingeniøropmærksomhed på produktet, ikke på redundans, din trafik endnu ikke berettiger.

**Lille virksomhed.** Uden en pålidelighedsspecialist og med et stramt budget tipper køb-versus-byg-valget hårdt mod køb: en administreret platform eller serverless-stak gør skalering og failover til udbyderens job, og en enkelt velkørt region er som regel nok. Ram robusthed ind som et lille antal konkrete løfter, du kan holde, såsom en natlig backup, du faktisk har gendannet fra én gang, og et realistisk genopretningsvindue, du har kommunikeret til kunderne. Undgå at betale for aktiv-aktiv eller løbende belastningstest, du hverken har trafikken eller personalet til at berettige.

**Stor virksomhed.** Problemet er ensartethed på tværs af mange teams: standardisér ydeevnebudgetter håndhævet i CI, et fælles bibliotek af robusthedsmønstre (timeouts, circuit breakers, skotter) og et dokumenteret redundansniveau for hvert system knyttet til dets kritikalitet. Forbehold aktiv-aktiv multiregion til tier-1-tjenester, kør et kaosingeniørprogram med rækværk og game days i produktion, og behandl kapacitetsplanlægning til kendte bølger som en planlagt disciplin frem for en eftertanke. Styr RTO og RPO centralt, så hvert kritisk system har ejede, testede mål, en revisor kan verificere.

**Offentlig sektor.** Belastning er ofte juridisk tidsfastsat, og tilgængelighedsforpligtelser er lovbestemte, så kapacitetsplanlægning kan ikke støtte sig til, at autoskalering reagerer i øjeblikket: prognosticér fristens bølge, forhåndsprovisionér og belastningstest langt over prognosen. Indkøb bør specificere RTO, RPO og en plan for øvede failovers som kontraktlige krav, ikke leverandørløfter, og bør undgå enkelt-region-indlåsning for kritiske tjenester. Beslut på forhånd, hvilken sti der er juridisk essentiel (at indgive en selvangivelse, at kræve en ydelse), så nedgradering afgiver statusdashboards og opslag først, og vær åbne over for offentligheden om nedbrud og genopretning frem for at håbe, ingen lægger mærke til det.

## Eksempler

**Startup.** Et lille startup, der lancerer på Product Hunt, kan ikke forudsige, om det får halvtreds tilmeldinger eller halvtredstusind, så det holder sine tjenester tilstandsløse bag en administreret belastningsfordeler og lader platformen autoskalere efter anmodningsrate. Det sætter ét beskedent ydeevnebudget (sider svarer på under 300 ms ved 95. percentil) og vælger en administreret database, så en trafikspids ikke tvinger en rearkitektur kl. 2 om natten. Da lanceringsdagens bølge kommer, bliver sitet lidt langsommere frem for at falde om, og teamet bruger dagen på at tale med nye brugere i stedet for at kæmpe mod et nedbrud.

**Stor virksomhed.** Et streamingmedieselskab kører tilstandsløse tjenester på tværs af flere regioner bag global belastningsfordeling og autoskalerer efter anmodningsrate for at følge den daglige primetime-bølge. Ydeevnebudgetter lukker porten for hver udgivelse på p99-starttid. Under et regionsnedbrud skifter trafikken automatisk til sunde regioner, og ikke-essentielle features (personaliseret artwork, opdatering af anbefalinger) nedgraderes først for at beskytte afspilning. Selskabet kører løbende kaoseksperimenter i produktion, afslutter rutinemæssigt instanser og injicerer latens, så reelle fejl er umulige at skelne fra øvelser og ikke forårsager noget kundesynligt nedbrud.

**Offentlig sektor.** En skatteadministration ved, at dens indberetningssystem hvert år står over for en massiv, juridisk fastlagt fristbølge. I stedet for at støtte sig til, at autoskalering reagerer i øjeblikket, prognosticerer den spidsbelastning fra tidligere år, forhåndsprovisionerer kapacitet uger i forvejen og belastningstester til 150 % af prognosen. Arkitekturen er tilstandsløs bag belastningsfordelere med en varm standby-anden region. RTO og RPO er fastsat ved politik (højst 15 minutters nedetid og næsten nul datatab for indgivne selvangivelser), og failover øves kvartalsvis. Under ekstrem belastning afgives ikke-kritiske features (statusdashboards, historiske opslag) først, så indgivelse af selvangivelser, den juridisk essentielle sti, forbliver tilgængelig.

## Business case: motivation, ROI og TCO

Skalerbarhed, ydeevne og robusthed er klassiske tilfælde, hvor omkostningen ved fejl langt overstiger omkostningen ved forebyggelse. Men forebyggelsen er synlig på budgettet, og fejlen er kun potentiel, hvilket er grunden til, at de er kronisk underfinansierede, til den første katastrofe. Indførelsesomkostningen er reel: redundant infrastruktur, multiregion-kapacitet, belastningstest- og kaosværktøj og ingeniørtiden til at bygge tilstandsløshed og robusthedsmønstre. Omkostningen ved *ikke* at investere er et højprofileret nedbrud under spidsbelastning: tabt omsætning pr. minut for handel, missede lovbestemte forpligtelser og offentlig undersøgelse for det offentlige, bøder fra [serviceaftaler](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) og varig omdømmeskade.

Ram sagen ind over for ledelsen med tal, forretningen allerede forstår. Estimér omkostningen ved en times nedetid under spids (tabte transaktioner, bøder, udbedring, omdømme), og sammenlign den derefter med den årlige omkostning ved den redundans og test, der forebygger det. For kritiske systemer er forebyggelsen næsten altid en brøkdel af en enkelt større hændelse. Bind RTO og RPO til eksplicitte penge: hvor megen omsætning eller hvor mange transaktioner pr. times nedetid, og hvor meget datatab der er juridisk eller kommercielt tolerabelt. Fremlæg ydeevne som en omsætnings- og tilfredshedsløftestang, da hurtigere systemer konverterer bedre og koster mindre pr. transaktion, og fremlæg robusthed som en forsikring, hvis præmie er lille i forhold til det dækkede tab. Det stærkeste argument er, at disse kvaliteter er billige at designe ind og ruinerende at eftermontere efter det nedbrud, der tvinger sagen.

## Anti-mønstre og faldgruber

- **Klæbrige sessioner og tilstand i instansen.** At gemme sessionstilstand på serveren, hvilket forhindrer fri horisontal skalering og sikker udskiftning af instanser.
- **Autoskalering som kapacitetsplanlægning.** At antage at autoskalering vil absorbere en kendt trinskift-bølge, den er for langsom til at reagere på.
- **At køre varmt uden margen.** At operere ved næsten 100 % udnyttelse og efterlade intet til at absorbere spidser eller fejl.
- **Optimering uden profilering.** At tune kode, der ikke er flaskehalsen, mens den reelle forbliver urørt.
- **At ignorere halen.** At rapportere gennemsnitlig latens, mens p99-brugere lider; gennemsnit skjuler smerten i stor skala.
- **Utestet katastrofegenopretning.** En DR-plan og backups, der aldrig er øvet, og som vil fejle, når de er nødvendige.
- **Enkelte fejlpunkter.** Én belastningsfordeler, én databaseprimær, én region: en ikke-redundant komponent, der tager alt ned.
- **Kaosingeniørkunst uden rækværk.** At injicere fejl uden sprængradiuskontrol eller afbrydelseskontakt og forårsage det nedbrud, du ville forebygge.

## Modenhedsmodel

- **Niveau 1: Opstart.** Ad hoc og reaktiv. Enkeltinstans eller vertikalt skaleret, med tilstand holdt på serveren. Ingen belastningstest, ingen ydeevnebudgetter og ingen katastrofegenopretning ud over lejlighedsvise backups, ingen har gendannet fra. Ethvert komponentsvigt forårsager et fuldt nedbrud, og skaleringsproblemer opdages i produktion.
- **Niveau 2: Udvikling.** Grundlæggende praksis dukker op, men varierer fra team til team. Nogle tjenester er horisontalt skaleret og tilstandsløse bag en belastningsfordeler, med grundlæggende autoskalering på nogle få af dem. Belastningstest sker før store lanceringer, men ikke rutinemæssigt, og backups findes, mens katastrofegenopretning er dokumenteret, men sjældent øvet. Hvad ét team gør godt, er et andet ikke begyndt på.
- **Niveau 3: Standardisering.** Praksis er dokumenteret og håndhævet i hele organisationen. Kapacitet planlægges til kendte bølger med margen, ydeevnebudgetter håndhæves i CI, så regressioner får bygget til at fejle, og robusthedsmønstre (timeouts, afgrænsede genforsøg, circuit breakers, skotter) plus elegant nedgradering er standarden. RTO og RPO er defineret pr. system, redundansniveauer tildeles efter kritikalitet, og failover i katastrofegenopretning testes efter en fast plan på tværs af teams.
- **Niveau 4: Styring.** Kvaliteterne måles og styres mod baselines. Teams følger p95- og p99-latens, fejlbudgetter og udnyttelse og margen mod prognose og alarmerer på brud frem for at opdage dem ved lancering. Testede failover-tider sammenlignes med mål-RTO og -RPO, nedgraderings- og belastningsafgivelsestærskler valideres med målinger, og go/no-go-beslutninger om udgivelser og kapacitet drives af data. Hvor tal driver fra baselinen, er hullet synligt og ejet frem for skjult bag gennemsnit.
- **Niveau 5: Orkestrering.** Skalerbarhed, ydeevne og robusthed forbedres løbende og er integreret i hele organisationen. Aktiv-aktiv multiregion bruges, hvor kritikalitet berettiger det, kaosingeniørkunst kører løbende inklusive game days i produktion, og kapacitetsprognoser føder direkte ind i planlægning og indkøb. Robusthed valideres løbende, genopretningsmål opfyldes og bevises konsekvent, og arkitekturen tilpasser sig, efterhånden som belastningsmønstre og risikobilledet skifter, bundet ind i forretningskontinuitets- og risikoplanlægning.

## Idéer til drøftelse

1. Hvilke af jeres tjenester holder stadig tilstand på instansen, og hvad forhindrer jer i at gøre dem tilstandsløse?
2. For jeres mest kritiske system, hvad er RTO og RPO, hvem satte dem, og hvornår beviste I sidst, at I kan opfylde dem?
3. Beskytter autoskalering jer faktisk mod jeres største kendte bølge, eller støtter I jer til, at den gør noget, den ikke kan?
4. Hvor er jeres tilbageværende enkelte fejlpunkt, og hvad er planen for at fjerne det?
5. Måler og budgetterer I p99-latens, eller gemmer I jer bag gennemsnit?
6. Har I nogensinde bevidst fejlet en komponent i produktion? Hvis ikke, hvordan ved I, at jeres robusthed virker?

## Vigtigste pointer

- Skeln mellem ydeevne, skalerbarhed og robusthed; et stort system har brug for alle tre, designet ind fra begyndelsen.
- Horisontal skalering og tilstandsløse tjenester er fundamentet for skala, tilgængelighed og sikker udrulning.
- Kombinér autoskalering med reel kapacitetsplanlægning og margen til forudsigelige, forretningskritiske bølger.
- Driv ydeevne med profilering og belastningstest mod eksplicitte budgetter, med fokus på den kritiske sti og halen.
- Byg robusthed med timeouts, circuit breakers, skotter, elegant nedgradering og redundans, og validér den derefter med kaosingeniørkunst.
- Sæt RTO og RPO som forretningsbeslutninger, konstruér DR efter hvert systems kritikalitet, og test failover regelmæssigt.

## Referencer og videre læsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
