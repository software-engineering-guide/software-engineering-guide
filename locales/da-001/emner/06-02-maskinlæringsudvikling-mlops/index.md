# 6.2 Maskinlæringsudvikling (MLOps)

## Overblik og motivation

Maskinlæringsudvikling, som regel kaldet [MLOps](https://en.wikipedia.org/wiki/MLOps), er disciplinen at tage [maskinlæring](https://en.wikipedia.org/wiki/Machine_learning) ud af notebooks og eksperimenter og ind i pålidelige, observerbare, vedligeholdelige produktionssystemer. Traditionel software opfører sig, som dens kode siger, den vil. Et ML-system opfører sig, som dets kode, dets data og dets lærte modelparametre tilsammen siger, det vil. Det gør ML-systemer sværere at teste, sværere at reproducere og tilbøjelige til at fejle stille, efterhånden som verden driver væk fra de data, de blev trænet på. MLOps bringer softwareudviklingens stringens (versionsstyring, test, kontinuerlig levering og overvågning) til denne tredelte virkelighed af kode plus data plus modeller.

For store teams er MLOps det, der adskiller en engangsmodel, der blænder i en demo, fra en flåde af modeller, mange teams kan bygge, udrulle og drive sikkert. Uden fælles platforme og praksisser genopfinder hvert team datapipelines, træningsløkker og udrulning, og I ender med skrøbelige systemer, ingen kan reproducere seks måneder senere. Virksomheder støtter sig til MLOps for at skalere på tværs af dusinvis af modeller, opfylde serviceniveaumål og tilfredsstille revisorer, der spørger, hvordan en given forudsigelse blev produceret.

I det offentlige og i regulerede brancher er MLOps ofte et compliancekrav i forklædning. Reproducerbarhed, afstamning og versionering er det, der lader et agentur besvare et juridisk væsentligt spørgsmål: præcis hvilken model, trænet på hvilke data, med hvilken kode, producerede den afgørelse, der berørte en borger? En moden MLOps-praksis holder det spørgsmål besvarligt år senere, hvilket både er god ingeniørkunst og en juridisk sikkerhedsforanstaltning.

*Se også:* kapitel 8.1 (CI/CD og levering), kapitel 9.2 (observerbarhed og overvågning) og kapitel 6.6 (AI-infrastruktur og drift).

## Grundprincipper

- Behandl data, kode og modeller som fælles versionerede artefakter; at ændre ét ændrer systemets adfærd.
- Automatisér vejen fra data til trænet model til udrulning, så den er gentagelig og reviderbar.
- Gør hver model sporbar til de præcise data, den kode og den konfiguration, der producerede den.
- Evaluér modeller mod repræsentative, tilbageholdte data før udrulning, og bliv ved med at evaluere efter.
- Antag at modeller forringes; overvåg for drift (den gradvise divergens af live data eller input-output-relationer fra det, modellen blev trænet på), datakvalitetsproblemer og ydeevneforfald fra dag ét.
- Foretræk kedelige, reproducerbare pipelines frem for kløgtige, ikke-reproducerbare eksperimenter.
- Adskil anliggenderne eksperimenteringshastighed og produktionspålidelighed, og byg bro imellem dem bevidst.

## Anbefalinger

### Styr hele ML-livscyklussen eksplicit

Definér og instrumentér hvert trin: dataindtag og -validering, [feature engineering](https://en.wikipedia.org/wiki/Feature_engineering), træning, evaluering, udrulning og overvågning. Gør grænserne mellem trin eksplicitte, så hvert kan testes, prøves igen og revideres. Undgå den almindelige fejl, hvor en model trænes i en ad hoc-notebook og kastes over muren til driften. Pak i stedet livscyklussen ind i en orkestreret pipeline, enhver autoriseret ingeniør kan køre fra en ren checkout.

### Brug feature stores, eksperimentsporing og modelregistre

Et **feature store** centraliserer featuredefinitioner, så de samme transformationer kører både i træning og serving. Det eliminerer training-serving skew (uoverensstemmelser mellem, hvordan features beregnes til træning versus til live forudsigelser) og lader teams genbruge features frem for at genberegne dem. **Eksperimentsporing** registrerer hvert træningskørsels parametre, kodeversion, dataversion og målinger, så resultater er sammenlignelige og reproducerbare. Et **modelregister** er systemet af autoritet for trænede modeller og holder versioner, afstamning, evalueringsresultater, godkendelsesstatus og udrulningstrin. Sammen lader disse jer besvare "hvad ændrede sig?", når adfærd skifter, og promovere eller rulle modeller tilbage gennem styrede trin.

### Gør data og modeller reproducerbare og versionerede med afstamning

Versionér jeres datasæt, ikke kun jeres kode. Brug indholdsadresserbart lager eller dataversioneringsværktøjer, så en træningskørsel refererer til et uforanderligt øjebliksbillede. Fastlås kode med git-commits, og fastlås miljøer med låste afhængigheder og containerbilleder. Indfang afstamning fra ende til anden: hvilke rå data fodrede hvilke features, hvilke features og kode producerede hvilken model, og hvor den model er udrullet. Når en hændelse eller revision rammer, forvandler afstamning et retsmedicinsk mareridt til en simpel forespørgsel. Registrér tilfældighed (seeds) og hardware, hvor resultater afhænger af dem.

### Vælg udrulningsmønstre, der passer til arbejdsbyrden

- **Batch**-scoring kører efter en plan over store datasæt; simplest at drive, tolerant over for latens, ideel til rapporter og periodiske beslutninger.
- **Online (realtid)**-serving svarer på individuelle anmodninger inden for stramme latensbudgetter; kræver hentning af features med lav latens og omhyggelig kapacitetsplanlægning.
- **Streaming** scorer hændelser kontinuerligt, efterhånden som de ankommer; passer til svindeldetektion og overvågning, hvor friskhed er kritisk.
- **Edge** kører modeller på enheder eller on-premises hardware af hensyn til latens, privatliv, konnektivitet eller datasuverænitet, almindeligt i offentlige og felt-sammenhænge.

Vælg det simpleste mønster, der opfylder kravet, og design jeres udrulning med skyggeudrulninger, canaries og øjeblikkelig tilbagerulning.

### Overvåg for drift, forringelse og datakvalitet

Instrumentér input og output i produktion. Hold øje med **datadrift** (inputfordelinger der skifter), **[konceptdrift](https://en.wikipedia.org/wiki/Concept_drift)** (relationen mellem input og målet der ændrer sig), **datakvalitets**fejl (nuller, skemaændringer, ødelagte opstrømskilder) og **ydeevneforringelse** målt mod forsinket grundsandhed, hvor I har den. Sæt alarmtærskler, skriv runbooks, og kobl overvågning til jeres gentræningsudløsere. Stille forringelse er den klassiske ML-fejlform, og overvågning er jeres eneste forsvar mod den.

## Afvejninger: fordele og ulemper

| Beslutning | Mulighed A | Mulighed B | Afvejning |
|---|---|---|---|
| Servingmønster | Batch | Online | Enkelhed og omkostning versus friskhed og latens |
| Featureberegning | Feature store | Pipelines pr. model | Ensartethed og genbrug versus opsætningsoverhead |
| Platform | Køb en administreret MLOps-platform | Saml open source-værktøjer | Hastighed og support versus fleksibilitet og indlåsning |
| Gentræning | Planlagt | Udløst af drift | Forudsigelighed versus responsivitet og kompleksitet |
| Reproducerbarhedsstringens | Fuld dataversionering | Let sporing | Revisionsstyrke versus lager og indsats |

Den overordnede afvejning er investering nu versus skrøbelighed senere. Tung reproducerbarheds- og overvågningsinfrastruktur koster indsats på forhånd, men forebygger den langt større omkostning ved uforklarlige fejl, ikke-reproducerbare modeller og eroderet tillid. Administrerede platforme fremskynder teams, men kan skabe indlåsning; open source-stakke giver kontrol til prisen af integrationsarbejde. Store organisationer drager som regel gavn af et fælles platformsteam, der skjuler denne kompleksitet bag asfalterede standarder.

## Spørgsmål til drøftelse med dit team

1. **Hvordan ville vi opdage, at en udrullet model stille er forringet, før en kunde eller borger bliver skadet, og hvem ejer den alarm?** Stille forfald er den klassiske ML-fejlform: koden kører stadig, modellen returnerer stadig selvsikre scores, og kvaliteten glider, efterhånden som verden driver fra træningsdataene. For et stort team, der kører mange modeller, har I brug for dette besvaret pr. model, ikke én gang for flåden, fordi hver har sin egen driftsprofil og sin egen forsinkelse af grundsandhed. Tag jeres nuværende overvågning for datadrift, konceptdrift og datakvalitetsbrud, alarmtærsklerne og den runbook, der siger, hvem der reagerer, med. I regulerede sammenhænge, hvor labels ankommer uger for sent, så drøft proxysignaler, I kan holde øje med i mellemtiden, for at vente på forsinket grundsandhed er at vente på at opdage skade. Hvis ingen enkelt ejer er navngivet for en models driftsalarm, er den model reelt uovervåget.

2. **Hvis en revisor bad os reproducere en specifik forudsigelse fra atten måneder siden, kunne vi så faktisk gøre det fra ende til anden?** Reproducerbarhed er det compliancekrav, der gemmer sig inde i god ingeniørkunst: det lader et agentur besvare præcis hvilken model, trænet på hvilke data, med hvilken kode, producerede en afgørelse, der berørte nogen. Tag et reelt eksempel med og forsøg at spore det: det uforanderlige datasnapshot, git-committen, de låste afhængigheder og containerbilledet, de registrerede seeds og afstamningen fra rå data gennem features til den udrullede model. Signalet er, om noget led i den kæde mangler eller er manuelt. For det offentlige og regulerede brancher så beslut den opbevaringsperiode, loven faktisk kræver, og bekræft at jeres lager holder afstamning besvarlig i hele det vindue, da et hul forvandler en rutineforespørgsel til en retsmedicinsk nødsituation.

3. **Hvad er vores regel for at promovere en model til produktion og rulle den tilbage, og håndhæves den af registret eller kun af tillid?** Ustyret promovering er, hvordan notebookeksperimenter lækker ind i produktion, og hvordan en dårlig model bliver hængende, fordi ingen kan rulle den rent tilbage. For mange teams er forskellen mellem moden og skrøbelig, om modelregistret lukker porten for promovering med obligatorisk godkendelse og evaluering, eller om en ingeniør kan skubbe vægte ud i hånden. Tag jeres nuværende promoveringssti, jeres tilbagerulningsmekanisme og dokumentation for, at skyggeudrulninger eller canaries faktisk kører før fuld trafik, med. Drøft, om gentræning er planlagt eller driftsudløst, og om gentrænede modeller består valideringsporte før udrulning, for gentræning på live data uden validering forstærker drift eller forgiftning. Svaret bør håndhæves i platformen, ikke på en wikiside, folk stoles på at følge.

4. **Bygger vi vores MLOps-platform på open source-værktøjer, køber en administreret eller blander de to, og hvem har vejet indlåsningen?** Dette valg sætter loftet for, hvor hurtigt hver fremtidig model leveres, og hvor meget kontrol I beholder over jeres data og pipelines. En administreret platform får teams hurtigt til produktion og bærer support, men den kan fange jeres featuredefinitioner, afstamningsregistre og modelartefakter i et proprietært format, I ikke let kan forlade; en samlet open source-stak holder jer portable til prisen af reelt integrations- og vedligeholdelsesarbejde. Tag de totale ejeromkostninger for hver vej (licens eller bygning, lager, beregning til gentræning og platformspersonalet til at drive den), en ærlig vurdering af jeres teams kapacitet til at drive infrastruktur og en konkret udtrædelsestest med: kunne I eksportere jeres register, feature store og afstamning og genopbygge andetsteds? I virksomheds- og offentlige sammenhænge så tilføj indkøbsbegrænsninger og datasuverænitetsregler, da en platform, der gemmer træningsdata i en region eller et format, jeres tilsynsmyndighed forbyder, er diskvalificeret, uanset hvor bekvem den er.

5. **Bør vores feature store og modelregister være én centraliseret platform eller føderet pr. team, og hvad koster training-serving skew os i dag?** At centralisere featuredefinitioner eliminerer den skævhed, hvor en feature beregnes på én måde i træning og en anden i serving, hvilket er en stille og dyr kilde til nøjagtighedstab, men en enkelt platform kan blive en flaskehals, der sinker hvert team. At føderere giver teams autonomi, mens det multiplicerer rørføringen og chancerne for, at to teams definerer den samme feature inkonsistent. Tag dokumentation for, hvor skævhed allerede har ramt jer, hvor mange teams der genbruger features versus genopbygger dem, og de asfalterede standarder, et fælles platformsteam kunne tilbyde, med. For en stor organisation så vej styringsfordelen ved ét reviderbart system af autoritet mod leveringsomkostningen ved en central kø, og i regulerede sammenhænge foretræk den centraliserede afstamning, der lader en revisor spore enhver forudsigelse til den præcise featurekode, der producerede den.

6. **Har vi afstemt hver models udrulningsmønster med dens reelle behov for latens, friskhed og suverænitet, eller sat alt til én form som standard?** Batch, online, streaming og edge bærer hver meget forskellig driftsomkostning og kompleksitet, og at vælge det forkerte enten overforbruger på realtidsinfrastruktur, en natlig rapport aldrig havde brug for, eller sulter en svindelscorer for den friskhed, den afhænger af. Beslut pr. arbejdsbyrde, hvilket mønster kravet faktisk retfærdiggør, og modstå at standardisere på den mest komplekse mulighed, fordi den føles moderne. Tag latensbudgettet, volumenet, omkostningen ved et forældet svar og forsinkelsen af grundsandhed for hver model med. I offentlige og felt-sammenhænge så vej edge- og on-premises-udrulning bevidst, fordi datasuverænitetsregler eller intermitterende konnektivitet kan tvinge modeller ud på lokal hardware, og det valg omformer, hvordan I versionerer, overvåger og ruller tilbage hver model, I skubber derhen.

## Sektorperspektiv

**Startup.** Jeres knappeste ressource er ingeniøropmærksomhed, så hold MLOps let og køb det. Spor eksperimenter i et simpelt hostet værktøj, fastlås hver udrullet model til dens træningsdatasnapshot og kode-commit i git, og tilføj ét billigt driftstjek frem for en platform. Spring feature store og skræddersyede pipelines over, til en anden eller tredje model gør genbruget umagen værd; en skrøbelig stak, I ikke kan vedligeholde, vil sænke jer hurtigere end en manglende evne.

**Lille virksomhed.** I har sandsynligvis ingen ML-platformsspecialist og et stramt budget, så behandl MLOps som noget indlejret i de værktøjer, I allerede kører, frem for et system, I bemander. Foretræk en administreret tjeneste, der håndterer versionering, udrulning og overvågning for jer, og ram disciplinen ind som et datahygiejne- og reproducerbarhedsspørgsmål: vid hvilken model og hvilke data der producerede et givet resultat, og behold evnen til at rulle tilbage. Foretræk leverandører, der lader jer eksportere jeres data og modeller, så et senere skifte forbliver muligt.

**Stor virksomhed.** Problemet er skala på tværs af dusinvis af modeller og mange teams: et fælles feature store, eksperimentsporing og et modelregister med styret promovering, så grupper holder op med at genopfinde pipelines. Budgettér et platformsteam, der tilbyder asfalterede standarder, standardisér afstamning og overvågning, så hver model er reviderbar og hver hændelse forklarlig, og styr køb-versus-byg og indlåsning bevidst bag en grænseflade, der holder de underliggende værktøjer udskiftelige. Håndhæv valideringsporte og tilbagerulning i platformen, ikke i konvention.

**Offentlig sektor.** Reproducerbarhed, afstamning og versionering er compliancekrav i forklædning, så behandl dem som førsteklasses fra dag ét. Versionér det præcise datasæt og den kode bag hver udrullet model, opbevar den afstamning i den lovpligtige periode, og vær i stand til at reproducere enhver historisk forudsigelse, der berørte en borger. Hold et menneske til at gennemgå væsentlige afgørelser, vej edge- og on-premises-udrulning, hvor datasuverænitetsregler kræver det, og kræv at enhver leverandørplatform giver fuld portabilitet af jeres data, features og afstamning.

## Eksempler

**Startup.** Et lille analysestartup leverede sin første frafaldsforudsigelsesmodel med én dataforsker og en let opsætning. Det sporede eksperimenter i et simpelt hostet værktøj, fastlåste hver udrullet model til dens træningsdatasnapshot og kode-commit i git og tilføjede et grundlæggende ugentligt job, der sammenlignede seneste input mod træningsfordelingen. Da en datakilde ændrede sit datoformat, og forudsigelser begyndte at drive, fangede det simple tjek det på dage frem for efter et vredt kundeopkald, og teamet kunne reproducere den sidste gode model og rulle tilbage.

**Stor virksomhed.** En detailbank kører dusinvis af kredit- og svindelmodeller. Den standardiserede på et feature store delt på tværs af teams, en eksperimentsporingstjeneste og et modelregister med obligatoriske godkendelsesporte. Hver model i produktion kan spores til dens træningsdatasnapshot og kode-commit. Svindelmodeller udrulles som streaming-scorere; kreditmodeller kører i batch. Et overvågningslag holder øje med inputdrift og alarmerer, når et datakildeskema ændres, hvilket engang fangede et ødelagt opstrømsfeed, før det korrumperede afgørelser.

**Offentlig sektor.** Et offentligt ydelsesagentur bruger en ML-model til at prioritere sagsgennemgange. Fordi disse afgørelser påvirker borgeres adgang til tjenester, versionerer agenturet det præcise datasæt og den kode bag hver udrullet model, opbevarer denne afstamning i den lovpligtige periode og kan reproducere enhver historisk forudsigelse efter behov. Modeller udrulles i batch med et menneske, der gennemgår markerede sager, og en driftsmonitor tvinger en obligatorisk genevaluering, hver gang den indkommende population skifter, så modellen aldrig stille anvendes uden for de betingelser, den blev valideret til.

## Business case: motivation, ROI og TCO

MLOps betaler sig selv ved at forvandle skrøbelige eksperimenter til pålidelige aktiver. ROI kommer fra hurtigere tid til produktion for nye modeller, færre dyre hændelser, mindre duplikeret infrastruktur og evnen til at drive mange modeller med et lille platformsteam. Et fælles feature store og register kan skære leveringstiden pr. model dramatisk, fordi teams holder op med at genopbygge den samme rørføring.

TCO dækker platformsbygning eller -licens, lager til versionerede data og modeller, beregning til gentræning og personalet til at drive det hele. Vej det mod omkostningen ved ikke at adoptere: modeller, I ikke kan reproducere eller revidere, stille fejl der skader kunder eller borgere og regulatoriske fund. I regulerede sammenhænge kan omkostningen ved en uforklarlig model i en revision overgå hele MLOps-investeringen. Før sagen over for ledelsen ved at ramme MLOps ind som risikoreduktion og leveringsacceleration, ikke overhead: en asfalteret vej, hver fremtidig model vil rejse.

## Anti-mønstre og faldgruber

- **Spring fra notebook til produktion.** At udrulle modeller trænet i ustyrede notebooks uden reproducerbarhed.
- **Training-serving skew.** Forskellig featurekode i træning og serving, der forårsager stille nøjagtighedstab.
- **Ingen dataversionering.** At versionere kode, men ikke data, så kørsler ikke kan reproduceres.
- **Udrul og glem.** At levere en model uden overvågning og først opdage forringelse, når brugere klager.
- **Gentræning på autopilot.** Automatisk gentræning på live data uden validering, der forstærker drift eller forgiftning.
- **Engangsinfrastruktur.** Hvert team bygger sin egen pipeline og multiplicerer omkostning og skrøbelighed.
- **At ignorere forsinkede labels.** At antage, at I kan måle nøjagtighed øjeblikkeligt, når grundsandhed ankommer uger senere.

## Modenhedsmodel

1. **Opstart.** Modeller bygget ad hoc i notebooks; manuel udrulning; ingen versionering af data eller modeller; ingen overvågning; at reproducere en tidligere forudsigelse er gætværk.
2. **Udvikling.** Noget eksperimentsporing og et modelregister dukker op, men praksis varierer fra team til team; udrulning er halvautomatiseret; grundlæggende overvågning dækker nogle få modeller; dataversionering er delvis, og afstamning har huller.
3. **Standardisering.** En fælles platform med et feature store, register, reproducerbare pipelines og afstamning fra ende til anden er dokumenteret og håndhævet i hele organisationen; overvågning for drift og datakvalitet kører på tværs af modeller; promovering og tilbagerulning følger en styret sti, hvert team bruger.
4. **Styring.** Flåden måles mod baselines: driftsrater, datakvalitetsbrud, modelnøjagtighed mod forsinket grundsandhed, training-serving skew, tid til produktion og driftsomkostning pr. model følges som målinger; alarmtærskler og valideringsporte håndhæves på dokumentation, og hver models sundhed gennemgås efter en fast kadence med en navngiven ejer.
5. **Orkestrering.** Livscyklussen er fuldt automatiseret, reviderbar og adaptiv; driftsudløst gentræning kører bag valideringsporte; selvbetjente asfalterede veje lader teams levere sikkert; kontinuerlig evaluering knytter modelydeevne til forretningsmålinger, og platformen er integreret med levering, risiko og compliance, så modeller rutinemæssigt pensioneres, erstattes og omafgrænses, efterhånden som data og betingelser skifter.

## Idéer til drøftelse

- Hvordan afvejer I eksperimenteringsfrihed mod produktionsreproducerbarhed?
- Hvad er den rette gentræningsudløser (plan, drift eller ydeevneforfald) for jeres anvendelser?
- Hvor længe skal I opbevare data- og modelafstamning, og hvad driver det krav?
- Bør feature stores og registre være centraliserede platforme eller føderet pr. team?
- Hvordan overvåger I nøjagtighed, når grundsandhedslabels ankommer med lange forsinkelser?
- Hvornår er edge-udrulning den ekstra driftskompleksitet værd?

## Vigtigste pointer

- ML-adfærd kommer af kode plus data plus modeller; versionér og styr alle tre sammen.
- Feature stores, eksperimentsporing og registre er rygraden i reproducerbar ML.
- Afstamning gør modeller reviderbare og hændelser forklarlige: essentielt i regulerede sammenhænge.
- Vælg batch, online, streaming eller edge efter behov for latens, friskhed og suverænitet.
- Modeller forringes; overvågning for drift, datakvalitet og forfald er ikke valgfri.

## Referencer og videre læsning

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
