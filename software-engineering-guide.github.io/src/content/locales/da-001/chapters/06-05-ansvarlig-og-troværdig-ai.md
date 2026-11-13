# 6.5 Ansvarlig og troværdig AI

## Overblik og motivation

Ansvarlig og troværdig AI er praksissen at bygge og drive AI-systemer, der er retfærdige, gennemsigtige, ansvarlige, sikre og respektfulde over for privatliv. Det betyder også at kunne vise alt dette over for de mennesker, der berøres, og over for tilsynsmyndigheder. Efterhånden som AI tager beslutninger, der former menneskers liv (ansættelse, udlån, ydelsesberettigelse), er spørgsmålet ikke længere blot "virker det?", men "er det rigtigt, og kan vi retfærdiggøre det?" Et system, der er nøjagtigt i gennemsnit, kan stadig være uretfærdigt over for en undergruppe, uforklarligt for den person, det berører, eller usikkert, når det misbruges. I fortjener tillid ved at adressere disse dimensioner bevidst, ikke ved at håbe, at de tager sig af sig selv.

For store teams kan ansvarlig AI ikke være én persons job eller et afkrydsningsfelt til sidst. Væv det ind i, hvordan I designer, evaluerer, udruller og styrer systemer, med klart ejerskab og eskalering. I skala påvirker små bias og huller i tilsyn mange mennesker. Ét højprofileret svigt kan skade jeres omdømme og invitere regulering. Styringsrammeværker findes netop fordi ad hoc-gode intentioner ikke skalerer.

Offentlige og regulerede organisationer står over for bindende forpligtelser. Fremvoksende lovgivning såsom [EU's AI-forordning](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act) pålægger krav graderet efter risiko. Standarder som NIST AI Risk Management Framework og ISO/IEC 42001 giver jer strukturerede måder at opfylde dem på. Offentlige organer skal undgå ulovlig diskrimination, tilbyde veje til at anfægte automatiserede afgørelser og være åbne om, hvordan AI bruges i udøvelsen af offentlig myndighed. Ansvarlig AI i disse sammenhænge er både en etisk pligt og en juridisk nødvendighed.

*Se også:* kapitel 6.1 (AI-strategi og parathed), kapitel 10.5 (etik, ansvarlighed og offentlig interesse) og kapitel 4.5 (privatliv og databeskyttelse).

## Grundprincipper

- Retfærdighed er et designmål, der skal måles og styres, ikke antages.
- Mennesker berørt af AI-afgørelser fortjener forklaring og en vej til at anfægte dem.
- Ansvarlighed hviler hos mennesker og organisationen, aldrig hos modellen.
- Privatliv og sikkerhed skal udvikles ind, herunder beskyttelse mod misbrug.
- Styring bør følge anerkendte rammeværker, så den er forsvarlig og reviderbar.
- Menneskeligt tilsyn skal være meningsfuldt, med reel autoritet til at tilsidesætte og standse.
- Overvej de bredere omkostninger ved AI, herunder dens miljøaftryk.

## Anbefalinger

### Opdag og afbød bias og uretfærdighed

Definér, hvad retfærdighed betyder i jeres sammenhæng. Der findes flere, nogle gange modstridende, matematiske definitioner, og den rette afhænger af beslutningen og loven. Test modeller for forskellig ydeevne på tværs af beskyttede og sårbare grupper med repræsentative data. Gør det før udrulning, og bliv ved efter, fordi [bias](https://en.wikipedia.org/wiki/Algorithmic_bias) kan opstå, når populationer skifter. Afbød gennem bedre data, omvægtning, begrænsninger eller ved at ændre, hvordan systemet bruges, og dokumentér de afvejninger, I accepterede. At fjerne en beskyttet attribut fjerner ikke bias, da proxyer består. Behandl retfærdighed som en løbende måle- og styringsdisciplin, ikke en engangsgodkendelse.

### Giv forklarlighed, fortolkelighed og gennemsigtighed

Afstem forklaringens niveau med indsatsen og målgruppen. For væsentlige afgørelser så giv berørte mennesker en klar begrundelse i almindeligt sprog, de kan forstå og handle på. Til intern styring så bevar nok teknisk [fortolkelighed](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) til at fejlsøge og forsvare systemet. Foretræk iboende fortolkelige modeller, hvor indsatsen er høj, og fortolkelighed er opnåelig. Hvor komplekse modeller er nødvendige, så brug forklaringsteknikker og vær ærlige om deres grænser. Vær åbne om, hvornår AI overhovedet bruges, især i interaktioner med offentligheden.

### Styr med anerkendte rammeværker

Adoptér en struktureret styringstilgang frem for at opfinde en. **NIST AI Risk Management Framework** organiserer arbejdet omkring at styre, kortlægge, måle og håndtere AI-risiko. **EU's AI-forordning** klassificerer systemer efter risiko og pålægger forpligtelser i overensstemmelse hermed, med strenge krav til højrisikoanvendelser. **ISO/IEC 42001** definerer et AI-ledelsessystem, der kan revideres og certificeres. Kortlæg jeres systemer til disse rammeværker. Vedligehold dokumentation såsom model- og datakort (standardiserede opsummeringer af en models eller et datasæts formål, ydeevne og begrænsninger). Kør risikovurderinger før udrulning, og hold en opgørelse over AI-systemer med deres risikoniveauer og ejere. God styring tildeler klare roller, beslutningsrettigheder og eskaleringsstier.

### Sørg for menneskeligt tilsyn, ansvarlighed og klageadgang

Hold et menneske meningsfuldt i kontrol over væsentlige afgørelser, med ægte autoritet og de oplysninger, der skal til for at tilsidesætte systemet, ikke et gummistempel. Tildel klar ansvarlighed: navngiv en ejer, der kan stilles til ansvar for hvert systems adfærd. Giv mennesker berørt af automatiserede afgørelser en ret til forklaring og en farbar proces til at klage til et menneske, der kan ændre udfaldet. Log afgørelser og grundlaget for dem, så I kan håndtere klager og revisioner retfærdigt og prompte.

### Beskyt privatliv og sikkerhed, og mod misbrug

Minimér de personoplysninger, I indsamler og bruger, etablér et retsgrundlag, og anvend privatlivsteknikker, der passer til den involverede følsomhed. [Red team](https://en.wikipedia.org/wiki/Red_team) systemer før og efter udrulning for at finde måder, de kan manipuleres, jailbreakes eller misbruges til at forårsage skade, og ret det, I finder. Byg sikkerhedsforanstaltninger mod at generere skadeligt indhold, lække følsomme data eller muliggøre misbrug. Planlæg for hændelser: overvågning, respons og offentliggørelse. Overvej [dual-use](https://en.wikipedia.org/wiki/Dual-use_technology) (den samme kapacitet, der tjener både gavnlige og skadelige formål) og efterfølgende misbrug, ikke blot tilsigtet brug.

### Regn med miljøomkostningen

Træning og serving af store modeller forbruger betydelig energi og vand. Mål og rapportér aftrykket af større AI-arbejdsbyrder. Foretræk effektive modeller og hardware, hvor de opfylder behovet. Dimensionér modeller til opgaven frem for som standard at vælge den største, og indregn miljøomkostning i arkitektur- og indkøbsbeslutninger.

## Afvejninger: fordele og ulemper

| Spænding | Den ene side | Den anden side |
|---|---|---|
| Nøjagtighed vs retfærdighed | Højeste gennemsnitlige nøjagtighed | Retfærdige udfald på tværs af grupper |
| Ydeevne vs fortolkelighed | Komplekse, kraftfulde modeller | Forklarlige, forsvarlige modeller |
| Automatisering vs tilsyn | Effektivitet og skala | Menneskelig kontrol og ansvarlighed |
| Datanytte vs privatliv | Rigere modeller af flere data | Dataminimering og beskyttelse |
| Kapacitet vs sikkerhed | Bred, åben funktionalitet | Afgrænset, bevogtet adfærd |
| Hastighed vs styring | Hurtig udrulning | Grundig gennemgang og dokumentation |

Der er sjældent en gratis frokost. At forbedre retfærdighed kan koste noget nøjagtighed. Fortolkelighed kan koste noget ydeevne. Styring koster tid. Den ansvarlige vej er at træffe disse afvejninger bevidst, dokumentere dem og vælge til fordel for berørte mennesker og forsvarlighed, når indsatsen er høj. At ramme styring ind som en bremse på innovation er en falsk dikotomi. Ustyret AI-risiko er selv en trussel mod vedvarende innovation.

## Spørgsmål til drøftelse med dit team

1. **Hvilke af vores udrullede AI-systemer ville EU's AI-forordning klassificere som højrisiko, og opfylder vi de forpligtelser i dag?** Risikograderet lov er nu bindende, ikke hypotetisk, og et system, der afgør ansættelse, udlån eller ydelsesberettigelse, kan bære strenge krav, I måske allerede overtræder. For en stor organisation tvinger dette spørgsmål en ærlig opgørelse frem i stedet for en bekvem antagelse om, at styring er "håndteret." Tag jeres liste over AI-systemer med deres risikoniveauer og ejere med, afbildet mod EU's AI-forordning, NIST AI Risk Management Framework og ISO/IEC 42001, hvor relevant. Signalet at holde øje med er ethvert væsentligt system uden risikoklassificering, uden konsekvensvurdering og uden model- eller datakort. For offentlige organer, der udøver offentlig myndighed, er manglende forpligtelser ikke et backlogpunkt, det er juridisk eksponering, og svaret bør udløse de vurderinger og den dokumentation, disse systemer kræver.

2. **Når en af vores modeller afviser nogen, kan den person så få en begrundelse i almindeligt sprog og nå et menneske, der faktisk kan omgøre udfaldet?** En ret til forklaring og en farbar klageadgang er, hvad der adskiller ansvarlig AI fra en sort boks, der skader folk uden mulighed for oprejsning. Retfærdighed målt i gennemsnit kan stadig svigte et individ, og fortolkelighed valgt efter udrulning er som regel teater. Tag en specifik udrullet afgørelse med og spor den: begrundelsen, den berørte person modtager, klagekanalen og om det menneske i den anden ende har ægte autoritet og det loggede grundlag til at tilsidesætte. I offentlige og regulerede sammenhænge er en klagesti ofte et juridisk krav, ikke en høflighed. Hvis begrundelsen er uforståelig, eller klagen fører til et gummistempel, er det hullet, der skal rettes før næste udgivelse.

3. **Hvem er den ene navngivne person, der er ansvarlig, når en model forårsager skade, og har vedkommende reel autoritet til at standse den?** Ansvarlighed hviler hos mennesker og organisationen, aldrig hos modellen, men det princip er tomt, til et navn er knyttet til hvert system, og den person faktisk kan trække stikket. For et stort team betyder diffust ejerskab, at når et retfærdighedssvigt eller en jailbreak dukker op, antager alle, at en anden holder øje. Tag jeres ejerskabskort, jeres eskaleringsstier og dokumentation for, at tilsynet er meningsfuldt, med: får den navngivne ejer oplysningerne og magten til at tilsidesætte eller standse systemet, eller kun til at nikke? Drøft, hvordan I red teamer for misbrug, I endnu ikke har forestillet jer, da test kun af tilsigtet brug misser de fejl, der kommer i overskrifterne. Svaret bør ikke efterlade noget væsentligt system uden en ansvarlig ejer, der kan stoppe det.

4. **For hver væsentlig model, hvilken retfærdighedsdefinition valgte vi, hvem godkendte den, og holder vores undergruppemålinger faktisk i produktion?** Retfærdighed har flere matematiske definitioner, der er i konflikt med hinanden, så en model, der opfylder lige falske positive rater, kan overtræde lige udfald, og at vælge en definition er en værdidom, der ikke bør overlades til den, der skrev træningsløkken. For et stort team skjuler en uprøvet standard valget inde i koden og får hver nedstrøms gruppe til at arve en beslutning, ingen debatterede. Tag den retfærdighedsmåling, I optimerede, de beskyttede og sårbare grupper, I testede på tværs af, de repræsentative data, I brugte, og den drift, I har set siden lancering, med, da fjernelse af en beskyttet attribut efterlader proxyer, der holder bias i live. I virksomheds- og offentlige sammenhænge så navngiv den person, der har autoritet til at acceptere en retfærdighedsafvejning, og registrér det, for en tilsynsmyndighed eller en ombudsmand vil spørge, hvem der besluttede, at netop denne definition af retfærdig var den rette for folk nægtet et lån, en ydelse eller et job. Hvis ingen undergruppemålinger overvåges efter udrulning, så behandl modellen som umålt frem for retfærdig.

5. **Hvor lidt personoplysninger kan hvert system køre på, og har vi red teamet det for det misbrug og dual-use, vi helst ikke tænker på?** Privatliv og sikkerhed skal udvikles ind, og den billigste måde at reducere både brudrisiko og misbrugsflade på er at indsamle og opbevare mindre data i første omgang, men alligevel hamstrer teams rutinemæssigt input "for en sikkerheds skyld, hvis de skulle hjælpe senere." For en stor organisation er hvert ekstra felt et retsgrundlagsspørgsmål, en opbevaringsforpligtelse og en større præmie for en angriber eller en jailbreak. Tag dataopgørelsen og retsgrundlaget for hvert system, resultaterne af red teaming for manipulation, læk og skadelig generering og en ærlig liste over dual-use-kapaciteter, hvor den samme funktion, der hjælper en legitim bruger, også hjælper nogen, der handler i ond tro, med. I regulerede og offentlige sammenhænge så bind dette til jeres hændelsesplan: overvågning, respons og offentliggørelse, for et offentligt organ, der lækker følsomme data eller leverer et jailbreakbart system, står over for lovpligtige forpligtelser, ikke kun forlegenhed. Hvis red teaming kun nogensinde udøvede den tilsigtede sti, har I testet demoen, ikke systemet.

6. **Måler og ejer vi miljøaftrykket af vores større AI-arbejdsbyrder, eller er "brug den største model" en uprissat standard?** Træning og serving af store modeller forbruger reel energi og vand, og at vælge den største model som standard til opgaver, en mindre ville håndtere, forvandler en ingeniørgenvej til en tilbagevendende omkostning, organisationen aldrig ser på et dashboard. For et stort team, der kører mange arbejdsbyrder, akkumulerer små ineffektiviteter pr. kald til et aftryk, der bliver et indkøbs- og rapporteringsansvar, efterhånden som forventninger til offentliggørelse strammes. Tag det målte aftryk af jeres tungeste arbejdsbyrder, en sammenligning af modelstørrelser mod den nøjagtighed, opgaven faktisk har brug for, og de hardware- og servingvalg, I kunne dimensionere, med. I virksomheds- og offentlige sammenhænge så bind dette til bæredygtighedstilsagn og indkøbskriterier, da offentlige organer i stigende grad skal rapportere miljøpåvirkning og begrunde udgifter, og et umålt aftryk er et tal, I en dag vil blive bedt om at fremlægge og ikke kan. Beslut, om miljøomkostning er et formelt input til modelvalg, eller indrøm, at det i dag ikke er.

## Sektorperspektiv

**Startup.** I kan ikke bemande et styringsudvalg, så gør den lette version, der stadig tæller. Vælg fortolkelige modeller, hvor beslutningen er væsentlig, skriv et modelkort på én side, test for forskellige udfald på tværs af de grupper, I kan måle, og log afgørelser, så I kan genbesøge retfærdighed, når I vokser. Giv enhver negativ afgørelse en begrundelse i almindeligt sprog og en vej til et menneske. At springe dette over er ikke hastighed, det er et ansvar, I ikke har råd til, hvis en enkelt uretfærdig afgørelse når pressen eller en tilsynsmyndighed.

**Lille virksomhed.** Uden en dedikeret specialist så behandl ansvarlig AI som et købsspørgsmål: foretræk leverandører, der dokumenterer retfærdighedstest, blotlægger model- og datakort og lader jer oplyse kunder, når AI er i brug. Vid hvilke personoplysninger jeres værktøjer indsamler, og om I har et retsgrundlag for at bruge dem. Hvor et forkert automatiseret svar kunne skade en kunde, så hold et menneske i løkken frem for at stole på et værktøj, I ikke kan inspicere eller forklare.

**Stor virksomhed.** Opgaven er styring i skala på tværs af mange teams: kortlæg hvert system til NIST AI Risk Management Framework, EU's AI-forordning og ISO/IEC 42001, hold en opgørelse med risikoniveauer og navngivne ejere, og kræv retfærdigheds-, sikkerheds- og privatlivstest før og efter lancering. Standardisér model- og datakort, red teaming og klageprocesser, så grupper holder op med at genopfinde dem. Budgettér styrings-, tilsyns- og fortolkelighedsomkostningerne eksplicit, og behandl ustyret AI-risiko som en trussel mod retten til at drive virksomhed.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former hvert valg. Offentliggør en gennemsigtighedserklæring i almindeligt sprog, kør en konsekvensvurdering før udrulning, og hold meningsfuld menneskelig beslutningstagning for enhver handling, der berører en borger, med en farbar klagesti. Kræv at leverandører oplyser modelbegrænsninger og giver dataportabilitet, undgå ulovlig diskrimination, navngiv en ansvarlig embedsmand for hvert system, og rapportér miljøaftrykket af større arbejdsbyrder.

## Eksempler

**Startup.** Et lille udlånsstartup, der byggede en tidlig kreditscoringsfunktion, kunne ikke bemande et styringsudvalg, så det gjorde den lette version, der stadig betød noget. To grundlæggere godkendte modellen sammen, testede den for forskellige udfald på tværs af de grupper, de kunne måle, og skrev et kort modelkort på én side, der dækkede dens data, grænser og kendte risici. De valgte en simplere, mere fortolkelig model, så de kunne give enhver afvist ansøger en begrundelse i almindeligt sprog og en vej til menneskelig gennemgang, og de loggede afgørelser, så de kunne genbesøge retfærdighed, efterhånden som de voksede.

**Stor virksomhed.** En bank, der udrullede en kreditmodel, etablerede et AI-styringsudvalg, kortlagde modellen til en højrisikokategori og krævede retfærdighedstest på tværs af demografiske grupper før og efter lancering. Den dokumenterede modellen i et modelkort. Den gav afviste ansøgere en begrundelse i almindeligt sprog og en klage til en menneskelig kreditvurderer, og den red teamede systemet for manipulation. Den valgte en lidt mindre nøjagtig, men mere fortolkelig model, fordi den skulle forklare og forsvare hver afgørelse over for tilsynsmyndigheder.

**Offentlig sektor.** Et offentligt agentur, der brugte AI til at hjælpe med at allokere inspektionsressourcer, afstemte sit program til NIST AI RMF og de relevante bestemmelser i gældende AI-lov. Det offentliggjorde en gennemsigtighedserklæring, der beskrev, hvordan systemet virkede, og dets sikkerhedsforanstaltninger. Det gennemførte en konsekvensvurdering før udrulning, holdt meningsfuld menneskelig beslutningstagning for enhver handling, der berørte en borger, og tilbød en klageproces. Retfærdighed blev overvåget kontinuerligt, arbejdsbyrdens miljøomkostning blev rapporteret, og en ansvarlig embedsmand blev navngivet som ansvarlig for systemet.

## Business case: motivation, ROI og TCO

Ansvarlig AI beskytter værdi lige så meget, som den skaber den. ROI er stort set undgået omkostning: færre diskriminationskrav, regulatoriske bøder og omdømmekatastrofer; smidigere revisioner; og større bruger- og offentlig tillid, som driver adoption. Troværdige systemer er også mere robuste, fordi den disciplin, der producerer retfærdighed og sikkerhed, også producerer bedre ingeniørarbejde.

TCO omfatter styringspersonale, retfærdigheds- og sikkerhedstest, dokumentation, red teaming, tilsynsprocesser og den ydeevne, der nogle gange ofres for fortolkelighed eller retfærdighed. Vej det mod omkostningen ved ikke at investere: juridisk ansvar, tvungne nedlukninger, tabt offentlig tillid og den langt højere omkostning ved at eftermontere styring efter et svigt. I regulerede sammenhænge er investering i ansvarlig AI i stigende grad ikke til forhandling. Før sagen over for ledelsen ved at ramme den ind som risikostyring og ret til at drive virksomhed: forudsætningen for overhovedet at udrulle AI i skala.

## Anti-mønstre og faldgruber

- **Retfærdighed ved udeladelse.** At antage, at en model er retfærdig, fordi den ignorerer beskyttede attributter.
- **Forklarlighedsteater.** At producere forklaringer, der ikke faktisk afspejler, hvordan afgørelser træffes.
- **Gummistempeltilsyn.** Nominel menneskelig gennemgang uden reel autoritet eller oplysninger til at tilsidesætte.
- **Styring som eftertanke.** At skrue dokumentation og gennemgang på efter design og udrulning.
- **Ingen klagesti.** At efterlade berørte mennesker uden mulighed for at anfægte en automatiseret afgørelse.
- **At ignorere misbrug.** At teste kun tilsigtet brug og misse jailbreaks og misbrug.
- **Blindhed over for aftrykket.** At vælge den største model som standard uden hensyn til miljøomkostning.

## Modenhedsmodel

1. **Opstart.** Ingen retfærdighedstest, forklaringer eller styring; ansvar er udefineret; bias, misbrug og privatlivsproblemer dukker først op efter skade, og der er ingen opgørelse over AI-systemer eller deres risici.
2. **Udvikling.** Noget biastest, modelkort og red teaming sker på individuelle systemer, men praksis er inkonsistent på tværs af teams; tilsyn er ad hoc; rammeværker som NIST AI Risk Management Framework og EU's AI-forordning er kendt, men kun delvist adopteret.
3. **Standardisering.** Styring er dokumenteret og håndhævet i hele organisationen: systemer er kortlagt til anerkendte rammeværker og ISO/IEC 42001, hvert har et risikoniveau og en navngiven ejer, og retfærdigheds-, sikkerheds- og privatlivstest, model- og datakort, klagestier og red teaming for højrisikosystemer er påkrævede frem for valgfrie.
4. **Styring.** Programmet måles og styres med data: undergruppemålinger for retfærdighed, sikkerheds- og jailbreakfund, klagevolumener og omgørelsesrater, tilsidesættelsesrater og arbejdsbyrdeaftryk følges mod baselines og tærskler; drift og forskellige udfald udløser defineret handling; go/no-go-beslutninger hviler på dokumentation frem for forsikring.
5. **Orkestrering.** Ansvarlig AI forbedres løbende og er integreret på tværs af organisationen: overvågning af retfærdighed, sikkerhed og misbrug kører i produktion, styring er bygget ind i levering, miljøomkostning er et formelt input til modelvalg, og organisationen tilpasser sine kontroller, efterhånden som lov, risiko og kapacitet skifter, med ansvar ejet af alle frem for et enkelt team.

## Idéer til drøftelse

- Hvilken retfærdighedsdefinition gælder for en given afgørelse, og hvem afgør det?
- Hvor megen nøjagtighed eller ydeevne er det acceptabelt at bytte for retfærdighed eller fortolkelighed?
- Hvad gør menneskeligt tilsyn meningsfuldt frem for et gummistempel?
- Hvordan bør klager over automatiserede afgørelser designes, så de er retfærdige og rettidige?
- Hvordan red teamer I for misbrug, I endnu ikke har forestillet jer?
- Bør miljøomkostning påvirke modelvalg, og hvordan ville I veje den?

## Vigtigste pointer

- Troværdig AI er retfærdig, forklarlig, ansvarlig, sikker og privatlivsrespekterende, ved design.
- Retfærdighed og sikkerhed er kontinuerlige måle- og styringsdiscipliner, ikke engangstjek.
- Afstem styring til NIST AI RMF, EU's AI-forordning og ISO/IEC 42001 for at være forsvarlig og reviderbar.
- Hold meningsfuldt menneskeligt tilsyn, klar ansvarlighed og en reel ret til at klage.
- Udvikl for privatliv og mod misbrug, og regn med miljøomkostningen.

## Referencer og videre læsning

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh, and Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
