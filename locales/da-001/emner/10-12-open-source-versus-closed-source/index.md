# 10.12 Open source versus closed source

## Overblik og motivation

Næsten ethvert moderne system er en blanding af software, I skrev, software, I købte, og software, I tog gratis. To af de tre kommer med et grundlæggende valg: er softwaren **open source** eller **closed source**? **[Open source-software](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** distribueres under en licens, der giver alle ret til at bruge, studere, ændre og videredistribuere kildekoden, de menneskelæselige instruktioner, der definerer programmet. **Closed source-software**, også kaldet **[proprietær software](https://en.wikipedia.org/wiki/Proprietary_software)**, distribueres som et færdigt produkt, hvis kildekode leverandøren holder privat. I får ret til at køre det under en licens, men ikke til at inspicere eller ændre, hvordan det virker. En mellemkategori, **[source-available-software](https://en.wikipedia.org/wiki/Source-available_software)**, offentliggør kilden til læsning, men begrænser brug, ændring eller videredistribution. Den er *synlig*, men ikke *åben* efter standarddefinitionen.

To præciseringer betyder noget, før I sammenligner dem. For det første er "gratis" flertydigt. Fællesskabet skelner mellem **gratis-som-i-frihed** (friheden til at ændre og dele, nogle gange skrevet "libre") og **gratis-som-i-pris** (nul omkostning, "gratis"). Open source handler om frihed, ikke nødvendigvis pris. For det andet deler open source-licenser sig i to familier. **[Permissive licenser](https://en.wikipedia.org/wiki/Permissive_software_license)** (såsom [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD og Apache 2.0) lader jer gøre næsten alt, inklusive at indlejre koden i et lukket produkt. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft)-licenser** (såsom [GNU General Public Licence](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) kræver, at afledte værker, I distribuerer, også udgives under de samme åbne vilkår, en gensidighedsregel som kritikere nogle gange kalder "viral" og tilhængere "del-på-samme-vilkår."

Dette kapitel ser på valget fra to sider. Som **forbruger** afgør I, om I skal adoptere en open source- eller proprietær komponent. Som **producent** afgør I, om I skal open source software, I byggede. For store virksomheder og især det offentlige bærer begge beslutninger vægt langt ud over licensfilen. De berører indkøb (kapitel 10.3), digital suverænitet (kapitel 10.11), forsyningskædesikkerhed (kapitel 4.2), interoperabilitet (kapitel 3.8) og byg-eller-køb-regnestykket (kapitel 6.1).

## Grundprincipper

- **Licensen, ikke prisen, definerer "åben."** Læs licensen; gratis og open source er forskellige påstande.
- **Ingen af modellerne er iboende mere sikre.** Begge kan være fremragende eller forsømmelige; praksisserne omkring koden betyder mere end dens åbenhed.
- **Åbenhed er en afhængighedsreducerende løftestang.** Adgang til kilden er den ultimative beskyttelse mod [leverandørindlåsning](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **I ejer altid driftsbyrden.** Gratis at erhverve er aldrig gratis at køre; [samlet ejeromkostning](https://en.wikipedia.org/wiki/Total_cost_of_ownership) fortæller den sande historie.
- **Differentiatorer forbliver lukkede; råvarer kan åbnes.** Open source det, der ikke adskiller jer; vogt det, der gør.
- **Copyleft har konsekvenser.** Forstå gensidighedsforpligtelser, før I indlejrer copyleft-kode i et produkt, I distribuerer.
- **Et levende fællesskab er et aktiv; et forladt repository er et ansvar.** Bedøm projektet, ikke blot licensen.

## Anbefalinger

### Vurdér en komponent på projektet, ikke blot licensen

Før I adopterer nogen afhængighed, open source eller proprietær, så vurdér dens sundhed: releasekadence, antal og mangfoldighed af vedligeholdere, responsivitet over for sikkerhedsrapporter og adoptionsbredde. Et bibliotek med én vedligeholder og en lille proprietær leverandør bærer den samme **bus-faktor-risiko** (faren for, at et projekt kollapser, hvis en eller nogle få nøglepersoner forlader det). Foretræk komponenter med en bred bidragyderbase eller en finansielt sund leverandør, og registrér vurderingen som en del af due diligence (kapitel 10.2, 4.2).

### Læs og følg licenser som en førsteklasses forpligtelse

Hold en fortegnelse over hver komponent og dens licens, og håndhæv en politik om, hvilke licensfamilier der er acceptable til hvilke formål. Det afgørende skel er copyleft. **Permissiv** kode (MIT, Apache 2.0) kan generelt indlejres frit i lukkede produkter. **Stærk copyleft** (GPL) kan forpligte jer til at udgive jeres eget distribuerede afledte værk under de samme vilkår. Brug automatiseret **softwarekompositionsanalyse (SCA)**, værktøjer der scanner jeres afhængigheder for at identificere komponenter, licenser og kendte sårbarheder, og generér en **software bill of materials (SBOM)**, en formel liste over hver komponent i et produkt (kapitel 10.3, 4.2).

### Bedøm sikkerhed efter praksis, ikke efter åbenhed

Antag ikke, at open source er sikkert på grund af **"mange øjne"-argumentet** ([Linus' lov](https://en.wikipedia.org/wiki/Linus%27s_law): "med nok øjne er alle fejl overfladiske"). Og antag ikke, at proprietær kode er sikker gennem **[sikkerhed-gennem-uklarhed](https://en.wikipedia.org/wiki/Security_through_obscurity)** (den fejlbehæftede tro på, at skjult kilde skjuler fejl). Mange øjne hjælper kun, hvis kvalificerede folk faktisk kigger, og mange udbredt brugte projekter er tyndt vedligeholdte. Begge modeller bærer **forsyningskæderisiko**: open source gennem kompromitterede eller forladte afhængigheder, proprietær gennem uigennemsigtig kode og opdateringskanaler, I ikke kan inspicere. Fastlås versioner, verificér proveniens, scan kontinuerligt og overvåg advisories uanset model (kapitel 4.2).

### Design til udtrædelse og interoperabilitet

Foretræk komponenter, der taler åbne standarder og portable dataformater, så I kan erstatte dem senere (kapitel 3.8, 10.11). Med open source får I den ultimative udtrædelse: hvis et projekt går i stå, kan I **[forke](https://en.wikipedia.org/wiki/Fork_(software_development))** det (oprette og vedligeholde jeres egen kopi). Med proprietær software så forhandl beskyttelser på forhånd: dataeksport i åbne formater, dokumenterede API'er og **[kildekodedepot](https://en.wikipedia.org/wiki/Source_code_escrow)** (en juridisk ordning, hvor leverandøren deponerer kilden hos en tredjepart, frigivet til jer, hvis leverandøren fejler). Design, så ingen enkelt komponent, af nogen art, kan holde jeres system som gidsel.

### Vej samlet ejeromkostning, ikke listepris

Sammenlign muligheder på **samlet ejeromkostning (TCO)**, den fulde livsomkostning inklusive erhvervelse, integration, drift, support, træning, opgraderinger og eventuel erstatning, frem for licensgebyrer alene. Open source bytter ofte licensomkostning for højere drifts- og bemandingsomkostning. Proprietær software bytter ofte forudsigelige abonnementsgebyrer for indlåsning og mindre kontrol. Medregn omkostningen ved selve modellen: selvunderstøttende open source kræver intern færdighed, mens proprietær software kræver leverandørstyringskapacitet.

### Som producent: open source det, der ikke differentierer jer

Klassificér jeres egen software i, hvad der giver konkurrence- eller missionsfordel, og hvad der er udifferentieret rørlægning. Hold differentiatorerne proprietære. Overvej at open source den almindelige infrastruktur, hvor et fællesskab kan dele vedligeholdelse og forbedring. For det offentlige så vej **"public money, public code"** (princippet om, at software finansieret af skatteydere som standard bør være offentligt tilgængelig) som en driver for åbenhed, genbrug og suverænitet (kapitel 10.5, 10.11). Vælg licensen bevidst: permissiv for at maksimere adoption, copyleft for at holde økosystemet åbent.

## Afvejninger: fordele og ulemper

| Dimension | Open source | Closed / proprietær |
|---|---|---|
| **Erhvervelsesomkostning** | Normalt nul at erhverve | Licens- eller abonnementsgebyr |
| **Samlet ejeromkostning** | Omkostning skifter til drift og personale | Mere forudsigelig, men indlåsningspræmie |
| **Kontrol & tilpasning** | Fuld: I kan læse og ændre kilden | Begrænset til det, leverandøren eksponerer |
| **Support & ansvarlighed** | Fællesskab eller betalt tredjepart; ingen enkelt at holde ansvarlig | Kontraktlig support og en klar ansvarlig part |
| **Sikkerhedsholdning** | Revisionsbar; "mange øjne" hvis reelt vedligeholdt | Leverandørstyret; uigennemsigtig; uklarhed er ikke beskyttelse |
| **Levetid / forladelse** | Kan forkes hvis vedligeholdt; kan stadig visne | Afhænger af leverandørens levedygtighed og køreplan |
| **Leverandørindlåsning** | Lav: kilde og åbne formater muliggør udtrædelse | Høj, medmindre afbødet af standarder og depot |
| **Økosystem** | Åbent fællesskab og interoperabilitet | Kurateret, integreret, nogle gange indhegnet |

Den tilbagevendende spænding er **kontrol versus bekvemmelighed og ansvarlighed**. Open source maksimerer kontrol, revisionsbarhed og frihed fra indlåsning, men beder jer selv levere kapabilitet, integration og support. Proprietær software leverer et understøttet, integreret, ansvarligt produkt med en kontrakt at håndhæve, men giver afkald på kontrol og inviterer til indlåsning. Løsningen er sjældent alt-eller-intet. De fleste modne ejendomme blander open source-fundamenter med proprietære systemer, hvor support, ansvarlighed eller specialiseret kapabilitet retfærdiggør afvejningen.

## Spørgsmål til drøftelse med dit team

1. **Håndhæver vi en licenspolitik med automatiseret SCA og SBOM'er i pipelinen, især for at fange stærk copyleft, før den leveres?** At indlejre et GPL-bibliotek i et distribueret proprietært produkt kan forpligte jer til at udgive jeres egen kilde, og den overraskelse dukker som regel op sent, når den er dyr at rulle tilbage. Hold en fortegnelse over hver komponent og dens licens, håndhæv hvilke licensfamilier der er acceptable til hvilke formål, og kør softwarekompositionsanalyse automatisk, så pipelinen blokerer overtrædelser frem for, at en jurist fanger dem ved leveringstidspunktet. Generér en SBOM som en selvfølge. For en stor eller offentlig ejendom er det også forsyningskædehygiejne og ofte et indkøbskrav. Tag jeres nuværende licensfortegnelse med, eller det faktum, at I ikke har en, og afgør, hvem der ejer politikken.

2. **Når vi adopterer en afhængighed, vurderer vi så projektsundhed og bus-faktor som due diligence?** Et bibliotek med én vedligeholder og en lille proprietær leverandør bærer den samme risiko: projektet kollapser, hvis en eller nogle få nøglepersoner forlader det. Før I adopterer noget, så vurdér releasekadence, antal og mangfoldighed af vedligeholdere, responsivitet over for sikkerhedsrapporter og adoptionsbredde, og registrér vurderingen. Ingen af modellerne er sikrere som standard; "mange øjne" hjælper kun, hvis kvalificerede folk faktisk kigger, og mange udbredt brugte projekter er tyndt vedligeholdte. Tag de tre eller fire afhængigheder, jeres produkt mest støtter sig til, med, og spørg for hver, hvor mange mennesker der skulle gå væk, før det blev jeres problem. Hvis I ikke kan svare, er det den vurdering, I skylder jer selv.

3. **Når vi køber proprietært, sikrer vi så udtrædelsesbeskyttelser på forhånd?** Proprietær software tilbyder ansvarlighed og bekvemmelighed til gengæld for kontrol, og den skjulte omkostning er indlåsning: skifteomkostninger, der lader en leverandør hæve priser eller forringe service med lille klagemulighed. Forhandl beskyttelserne før I underskriver, mens I stadig har indflydelse: dataeksport i åbne formater, dokumenterede API'er og kildekodedepot, der frigiver kilden, hvis leverandøren fejler. Med open source er jeres udtrædelse evnen til at forke; med proprietær skal I skrive udtrædelsen ind i kontrakten. Tag jeres mest kritiske proprietære systemer med, og spørg, hvad der faktisk sker, hvis leverandøren fordobler prisen eller går konkurs. Hvis svaret er "vi sidder fast", så ret kontrakten ved fornyelsen.

4. **For den software, vi selv bygger, hvordan afgør vi, hvad der skal open sources og hvad der skal holdes lukket, og hvem har autoriteten til at træffe det kald?** Få det forkert i den ene retning, og I giver netop den kode væk, der differentierer jer; få det forkert i den anden, og I hamstrer almindelig rørlægning, hvis vedligeholdelse et fællesskab gerne ville dele. De modstridende pres er reelle: ingeniører vil have rekrutterings- og omdømmefordelen ved et offentligt repository, mens produkt og jura bekymrer sig om at give rivaler en fordel eller blotlægge en sikkerhedsfølsom heuristik. Tag en ærlig klassificering af jeres systemer i missionsdifferentierende versus udifferentieret infrastruktur med, og navngiv den person eller det udvalg, der godkender en udgivelse, fordi en ad hoc-beslutning truffet af den, der pushede repositoryet, er, hvordan kronjuvelerne lækker. For en stor virksomhed er spørgsmålet porteføljestrategi, og for det offentlige støder det sammen med "public money, public code", princippet om at skatteyderfinansieret software bør være offentlig som standard, så afgør på forhånd, hvilke undtagelser (national sikkerhed, svindelopdagelse, personoplysninger) der retfærdiggør at holde kode lukket.

5. **Fanger vores byg-eller-køb-sammenligninger den fulde samlede ejeromkostning, eller behandler vi stadig et nul-licensgebyr som en nul-omkostning?** Den almindeligste økonomiske fejl med open source er at læse "gratis at erhverve" som "gratis at køre" og så opdage, at integration, drift, sikkerhedsrespons og betalt support overstiger enhver licens, I undgik. Spændingen er, at et proprietært abonnement ser dyrt ud på fakturaen, mens det skjuler en indlåsningspræmie, og en åben komponent ser gratis ud på fakturaen, mens den flytter omkostning over på jeres eget personale. Tag en lige-for-lige TCO-model for to eller tre reelle beslutninger med: erhvervelse, integration, drift, support, træning, opgraderinger, sikkerhedsrespons og eventuel erstatning, prissat over hele livet frem for det første år. I en virksomheds- eller offentlig ejendom så tilføj omkostningen ved selve driftsmodellen, da selvunderstøttende open source kræver intern færdighed, I skal rekruttere og fastholde, og behandl en sammenligning, der udelader de linjer, som dokumentation for en mangel, ikke som analyse.

6. **Bedømmer vi en komponents sikkerhed efter dens praksisser, eller støtter vi os til åbenhedsmærkaten, hvad enten det er "mange øjne" eller den lukkede kodes hemmeligholdelse?** Begge standarder er fælder: "mange øjne" beskytter jer kun, når kvalificerede folk faktisk gennemgår koden, og mange udbredt brugte åbne projekter kører på én udmattet vedligeholder, mens closed source, der afhænger af, at angribere ikke ser den, er sikkerhed gennem uklarhed, ikke en kontrol. Debatten har betydning, fordi den ændrer, hvor I bruger knap sikkerhedsindsats, og det ærlige svar er, at begge modeller bærer forsyningskæderisiko, open source gennem kompromitterede eller forladte afhængigheder og proprietær gennem uigennemsigtige opdateringskanaler, I ikke kan inspicere. Tag dokumentation for jeres mest kritiske komponenter med: hvem der faktisk gennemgår dem, hvor hurtigt advisories patches, om versioner er fastlåste og proveniens verificeret, og om I genererer en SBOM. For en stor eller offentlig ejendom så bind det til indkøbs- og kontinuerlige scanningsforpligtelser, fordi en tilsynsmyndighed vil spørge, hvad I inspicerede, ikke om kilden var offentlig.

## Sektorperspektiv

**Startup.** Med lidt runway bygger I på open source-fundamenter, fordi I ikke har råd til licensgebyrer, og I vil have friheden til at forke, hvis et projekt går i stå. Kør en kompositionsanalyse-scanning, før I leverer, så et stærk-copyleft-bibliotek ikke stille forpligter jer til at offentliggøre jeres egen kilde, og hold jeres ene reelle differentiator strengt lukket. Open source et lille, ikke-kritisk værktøj, hvis det hjælper rekruttering, men bemand ikke en vedligeholdelsesbyrde, I ikke kan bære.

**Lille virksomhed.** Uden intern juridisk eller platformsspecialist så behandl licensen som en risiko, I ikke må misforstå, frem for et emne, I kan mestre. Foretræk understøttede proprietære værktøjer eller kommercielle open source-distributioner, hvor en leverandør ejer patches og ansvarlighed, fordi selvunderstøttelse af en stak, I ikke kan drive, er en falsk økonomi. Når I adopterer en gratis komponent, så tjek, at dens licens tillader jeres brug, og at projektet faktisk vedligeholdes, ikke forladt.

**Stor virksomhed.** I skala er problemet ensartethed på tværs af mange teams: en skriftlig licenspolitik, automatiseret softwarekompositionsanalyse og SBOM-generering i hver pipeline og TCO-baserede byg-eller-køb-beslutninger frem for pr.-team-vane. Styr open source og proprietær software som én portefølje, standardisér udtrædelsesbeskyttelser som åbne formater og kildekodedepot i indkøb, og følg sundheden af kritiske afhængigheder, så et enkelt forladt projekt ikke bliver en hændelse. Styr også producentsiden med en klar regel om, hvad organisationen open sourcer versus holder lukket.

**Offentlig sektor.** Indkøbsregler, åbenhedspligter og offentlig ansvarlighed former hvert valg. Vej "public money, public code", princippet om, at skatteyderfinansieret software som standard bør være offentlig, for at fremme genbrug på tværs af agenturer og digital suverænitet, mens I skærer snævre undtagelser for sikkerhedsfølsom eller personoplysningskode. Kræv, at enhver proprietær leverandør leverer dataeksport i åbne formater og kildekodedepot, så en leverandørfiasko ikke kan efterlade en offentlig tjeneste strandet, og offentliggør den ikke-følsomme kilde, så borgere kan revidere de regler, der styrer dem.

## Eksempler

**Startup.** Et startup med tre grundlæggere bygger hele sit produkt på open source-fundamenter (Linux, en open source-database, et webframework), fordi det ikke har råd til licensgebyrer og vil have friheden til at forke, hvis et projekt går i stå. Før levering kører en grundlægger en kompositionsanalyse-scanning og fanger et stærk-copyleft-bibliotek, der ville have tvunget dem til at offentliggøre deres proprietære matchingalgoritme, så de bytter det ud med et permissivt licenseret ækvivalent. De holder den algoritme, deres eneste differentiator, strengt lukket og open sourcer kun et lille internt logningsværktøj for at bygge velvilje og tiltrække ingeniører.

**Stor virksomhed.** Et stort forsikringsselskab kører sin kerneplatform på open source-fundamenter: Linux, en udbredt open source-database og en containerorkestrator. Men det køber en proprietær aktuarmodelleringspakke, fordi leverandørens domæneekspertise, regulatoriske certificeringer og supportkontrakt er gebyret værd, og der ikke findes noget sammenligneligt åbent alternativ. Det betaler et abonnement for **kommerciel open source** (leverandørunderstøttede distributioner af de åbne komponenter) for at få ansvarlighed og patches på rørlægningen, mens det holder den prissætningsalgoritme, der differentierer det, strengt proprietær og internt. TCO-analyse (kapitel 10.10) driver hvert valg frem for ideologi.

**Offentlig sektor.** En national skattemyndighed, under en "public money, public code"-politik, bygger en ny ydelsesberettigelsestjeneste på open source-komponenter og åbne standarder (kapitel 3.8), så andre agenturer kan genbruge den, og borgere kan revidere reglerne. Den offentliggør den ikke-følsomme kode i et offentligt repository og beholder kun svindelopdagelsesheuristikker lukkede af sikkerhedsgrunde. Det reducerer leverandørindlåsning og fremmer digital suverænitet (kapitel 10.11). Indkøbsregler (kapitel 10.3) kræver, at enhver proprietær komponent leverer dataeksport i åbne formater og kildekodedepot for at garantere kontinuitet, hvis leverandøren fejler.

## Business case: motivation, ROI og TCO

Open sources økonomiske appel, manglen på licensgebyr, er den mindst pålidelige del af sagen, fordi erhvervelse er en lille brøkdel af TCO. De varige afkast er strategiske: frihed fra indlåsning (evnen til at skifte eller droppe en leverandør uden at re-arkitekturere), revisionsbarhed for sikkerhed og compliance, hurtigere adoption, fordi ingeniører kan prøve før forpligtelse, og delt vedligeholdelse af almindelig kode på tværs af en hel branche. De modsvarende omkostninger er reelle. I skal levere integration, drift, sikkerhedsrespons og ofte betalt support, og et dårligt valgt uvedligeholdt projekt kan koste mere i hændelser, end nogen licens ville have.

Proprietær softwares business case er ansvarlighed og bekvemmelighed: en enkelt leverandør ansvarlig for produktet, en supportkontrakt, I kan håndhæve, integrerede funktioner og forudsigelig budgettering. Dens skjulte omkostning er indlåsning, de skifteomkostninger, der lader en leverandør hæve priser eller forringe service med lille klagemulighed, plus afhængighed af leverandørens solvens og køreplan. Almindelige **forretningsmodeller** udvisker linjen: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (en åben base med proprietære betalte tilføjelser), **dobbelt licensering** (den samme kode tilbudt under både en copyleft- og en betalt kommerciel licens), **[software som en tjeneste](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (softwaren kører som en hostet tjeneste, I lejer, hvor kilden kan være irrelevant, fordi I aldrig besidder den binære) og **support-/abonnements**-modeller, der sælger service omkring ellers fri kode.

For en producent kan ROI af **at open source jeres egen ikke-differentierende software** være betydeligt. Eksterne bidragydere reducerer jeres vedligeholdelsesbelastning. Projektet bliver et rekrutterings- og omdømmeaktiv. Ekstern adoption gør jeres standard til den de facto. For det offentlige leverer det åbenhed og genbrug på tværs af den offentlige sektor. Den strategiske regel er enkel: open source råvaren for at dele dens omkostning og dyrke et økosystem, og hold differentiatoren lukket for at beskytte den fordel, der finansierer alt det andet.

## Anti-mønstre og faldgruber

- **"Gratis betyder gratis":** at behandle nul erhvervelsesomkostning som nul TCO og så underfinansiere drift og support.
- **Licensblindhed:** at indlejre stærk-copyleft-kode i et distribueret proprietært produkt og udløse forpligtelser, I aldrig planlagde.
- **Tro på "mange øjne":** at antage, at et åbent projekt revideres, når det har én overbelastet vedligeholder og ingen sikkerhedsgennemgang.
- **Sikkerhed-gennem-uklarhed:** at tro, at closed source er sikker, blot fordi angribere ikke kan læse den.
- **Ideologisk absolutisme:** at påbyde "alt åbent" eller "alt proprietært" i stedet for at vælge pr. komponent efter fortjeneste og TCO.
- **At ignorere proveniens:** at trække afhængigheder uden SBOM, versionsfastlåsning eller forsyningskædeverifikation (kapitel 4.2).
- **At open source kronjuvelerne:** at udgive netop den kode, der differentierer jer, og give jeres fordel væk.
- **Fork-og-glem:** at forke et forladt projekt uden kapaciteten til faktisk at vedligeholde forken.

## Modenhedsmodel

**Niveau 1 (Opstart).** Open source- og proprietære komponenter kommer ind i ejendommen ad hoc. Licenser er ulæste, der er ingen fortegnelse eller SBOM, og valget mellem modeller træffes efter vane eller pris alene. Forladelses- og licensrisiko dukker først op, når noget går i stykker, og hvert team reagerer for sig selv.

**Niveau 2 (Udvikling).** Nogle teams begynder på grundlæggende praksisser: en komponent- og licensfortegnelse, et groft billede af acceptable licenser og lejlighedsvis softwarekompositionsanalyse. Byg-eller-køb- og åben-eller-lukket-beslutninger skrives ned, men disciplinen er pletvis og inkonsistent fra team til team, så en copyleft- eller bus-faktor-overraskelse stadig kan slippe igennem, hvor vanen ikke har taget fat.

**Niveau 3 (Standardisering).** Et dokumenteret rammeværk styrer både forbrug og produktion i hele organisationen. Komponenter vælges efter TCO og projektsundhed, licenser håndhæves automatisk i pipelinen, så overtrædelser blokerer et build, SBOM'er genereres som en selvfølge, og en eksplicit politik angiver, hvad organisationen open sourcer versus holder lukket. Udtrædelsesbeskyttelser som åbne formater og kildekodedepot er standard i indkøb, og hvert team følger de samme regler frem for sine egne.

**Niveau 4 (Styring).** Programmet måles og styres mod baselines. Organisationen følger målinger som SBOM-dækning på tværs af produkter, andelen af afhængigheder der overtræder politik, gennemsnitlig tid til at patche en offentliggjort afhængighedssårbarhed, bus-faktor- og sundhedsscorer for kritiske projekter og realiseret TCO mod det estimat, der retfærdiggjorde hvert valg. Tærskler udløser handling: en komponent, hvis vedligeholdelse går i stå, eller hvis patchlatens driver forbi målet, flagges til erstatning på dokumentation, og åben-eller-lukket- og byg-eller-køb-beslutninger gennemgås mod tallene frem for forsvares af vane.

**Niveau 5 (Orkestrering).** Open source-strategi er en bevidst forretningskapabilitet, integreret på tværs af organisationen og løbende forbedret. Organisationen bidrager til og forvalter nogle gange de projekter, den afhænger af, open sourcer sin ikke-differentierende software som en selvfølge og fodrer afhængighedssundheds- og TCO-data tilbage i indkøbs-, sikkerheds- og produktplanlægning. Den rebalancerer rutinemæssigt sin portefølje af åben og proprietær software og tilpasser sig skift i omkostning, risiko, suverænitet og strategisk fordel, før de tvinger en krise.

## Idéer til drøftelse

- Hvor i jeres ejendom ville tabet af en enkelt leverandør eller vedligeholder være eksistentielt, og hvad er jeres udtrædelsesplan?
- Hvilke af jeres egne systemer er råvarer, I kunne open source, og hvilke er ægte differentiatorer at beskytte?
- Behandler jeres organisation "mange øjne" som en reel sikkerhedskontrol eller en uundersøgt antagelse?
- For offentlige læsere: hvad ville en "public money, public code"-standard ændre i jeres næste indkøb?
- Hvor godt fanger jeres TCO-sammenligninger de drifts- og supportomkostninger, open source flytter over på jer?

## Vigtigste pointer

- **Åben versus lukket defineres af licensen**, ikke af prisen; kend forskellen mellem gratis-som-i-frihed og gratis-som-i-pris og mellem permissiv og copyleft.
- **Ingen af modellerne er iboende mere sikre eller billigere.** Bedøm projektets praksisser og dets fulde TCO, ikke åbenhedsmærkaten.
- **Åbenhed er den stærkeste modgift mod indlåsning** og leverer revisionsbarhed, portabilitet og evnen til at forke; proprietær software tilbyder ansvarlighed og bekvemmelighed til gengæld for kontrol.
- **Afgør pr. komponent efter fortjeneste**, og bland modeller bevidst frem for efter ideologi.
- **Som producent: open source råvaren, og hold differentiatoren lukket**, og i det offentlige så vej "public money, public code" for åbenhed, genbrug og suverænitet.

## Referencer og videre læsning

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
