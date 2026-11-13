# 10.3 Indkøb, open source og licenser

## Overblik og motivation

Næsten ethvert moderne softwaresystem er for det meste samlet af komponenter, en anden har skrevet. [Open source-software](https://en.wikipedia.org/wiki/Open-source_software) udgør fundamentet for operativsystemer, sprog, rammeværker, databaser og cloudinfrastruktur. Den kommer ind i virksomheden på to måder: gennem bevidst [indkøb](https://en.wikipedia.org/wiki/Procurement) og gennem tilfældige `import`-sætninger fra individuelle udviklere. Dette kapitel handler om at gøre det forbrug (og, hvor det passer, bidrag) bevidst. Det betyder en strategi, licenscompliance, en forståelse af forpligtelser og copyleft-risiko og en plan for den uundgåelige [end-of-life](https://en.wikipedia.org/wiki/End-of-life_(product)) for de komponenter, I afhænger af.

For store teams er indsatsen juridisk, driftsmæssig og strategisk på én gang. Juridisk er open source-[licenser](https://en.wikipedia.org/wiki/Software_license) håndhævelige kontrakter med reelle forpligtelser. At få [copyleft](https://en.wikipedia.org/wiki/Copyleft) (licensering der kan kræve, at afledte værker deles på samme vilkår) forkert kan i værste fald tvinge til offentliggørelse af proprietær kildekode eller udløse retssager. Licensovertrædelser kan endda blokere et opkøb eller en børsnotering under [due diligence](https://en.wikipedia.org/wiki/Due_diligence). Driftsmæssigt rådner uforvaltede afhængigheder: komponenter bliver uvedligeholdte, ophober sårbarheder og når end-of-life, mens de stadig er begravet dybt i produktion. Strategisk er open source mere end et omkostningsbesparende input. Det er en måde at undgå [indlåsning](https://en.wikipedia.org/wiki/Vendor_lock-in), tiltrække talent og forme de økosystemer, I afhænger af, fordele I kun indfanger, hvis I engagerer jer med vilje.

Det offentlige har en ekstra dimension. Mange jurisdiktioner har nu eksplicitte politikker, der favoriserer open source, åbne standarder og kodedeling mellem agenturer. Disse udtrykkes ofte som "public money, public code": princippet om, at software finansieret af skatteydere som standard bør være tilgængelig for offentligheden. Så offentlige ingeniører skal navigere både licenscompliance og aktive mandater om at foretrække, offentliggøre og genbruge open source. Dette kapitel sigter mod at gøre det hele håndterbart i skala.

## Grundprincipper

- **Open source er en forsyningskæde, ikke gratis ting.** Behandl forbrugte komponenter med samme stringens som enhver kritisk leverandør.
- **Licenser er forpligtelser, ikke tilladelser til at ignorere.** Hver afhængighed bærer vilkår; kend dem, før I leverer.
- **Copyleft er en designbegrænsning, ikke et tabu.** Copyleft-licenser er brugbare og værdifulde; de kræver blot, at I forstår, hvordan I kombinerer og distribuerer software.
- **Forbrug bevidst, bidrag strategisk.** Afgør, hvad der skal ind, og invester, hvor det tjener jer, i upstreaming frem for at forke.
- **Opgør alt.** I kan ikke overholde, sikre eller opdatere det, I ikke kan se; en SBOM (software bill of materials, en komplet fortegnelse over komponenterne i jeres software) er et minimumskrav.
- **Planlæg for end-of-life fra begyndelsen.** Hver afhængighed bliver en dag uvedligeholdt; kend jeres udgang, før I tvinges ud i en.
- **I det offentlige: som standard åben.** Foretræk [åbne standarder](https://en.wikipedia.org/wiki/Open_standard) og open source, og offentliggør kode betalt af offentlige penge, medmindre der er en specifik grund til ikke at gøre det.

## Anbefalinger

### Sæt en open source-strategi og forbrugspolitik

Offentliggør en klar politik for, hvordan udviklere må bringe open source ind i organisationen: hvilke licenser der er forhåndsgodkendte, hvilke der kræver gennemgang, og hvilke der er forbudte til jeres brugssager. Tilbyd en hurtig, friktionsfri godkendelsessti. En politik langsommere end at kopiere kode bliver simpelthen ignoreret. Skeln mellem kontekster, fordi den samme licens opfører sig forskelligt, når en komponent bruges internt som en tjeneste, indlejres i et distribueret produkt eller linkes ind i en proprietær applikation. Gør den lette sti til den kompatible sti: et kurateret internt repository af efterprøvede komponenter, automatiseret scanning i pipelinen og klar vejledning, udviklere kan følge uden at ringe til en jurist i rutinetilfælde.

### Styr licenscompliance, forpligtelser og copyleft-risiko

Lær licensfamilierne og deres forpligtelser at kende. [Permissive licenser](https://en.wikipedia.org/wiki/Permissive_software_license) (såsom MIT, BSD og Apache 2.0) kræver hovedsageligt kildeangivelse og bevarelse af meddelelser; Apache 2.0 tilføjer en eksplicit patentbevilling. Svag copyleft (såsom [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) og MPL) kræver, at I deler ændringer til de dækkede filer, men lader generelt jer kombinere med proprietær kode. Stærk copyleft (såsom [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) kan kræve, at hele det distribuerede værk tilbydes på samme vilkår. Netværkscopyleft ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) udvider den forpligtelse til software tilbudt over et netværk, ikke blot distribueret som binære filer. De forpligtelser, der betyder mest, afhænger af to ting: om I distribuerer softwaren, og hvor tæt I kombinerer komponenter. Automatisér compliance: scan afhængigheder for licenser, generér og lever de påkrævede kildeangivelses- og meddelelsesfiler, og luk buildet på politik, så en forbudt licens ikke tavst kan komme ind i produktion.

### Etablér et Open Source Program Office (OSPO)

Hvis I forbruger open source i skala, så opret et omdrejningspunkt, et OSPO, der ejer open source-strategi, politik, complianceværktøj, bidragsstyring og fællesskabsrelationer. OSPO'et dæmper kaosset, når hvert team træffer sine egne beslutninger. Det leverer ekspertise, individuelle teams ikke kan vedligeholde. Og det indfanger strategisk værdi: at afgøre, hvilke projekter der skal investeres i, hvornår man skal bidrage upstream, og hvordan man udgiver sine egne open source-projekter godt. Selv et lille OSPO (nogle gange én person plus en tværfaglig arbejdsgruppe) forbedrer dramatisk ensartetheden og reducerer juridisk risiko sammenlignet med fri-for-alle.

### Styr bidrag og, hvor det passer, offentliggørelse

Afgør bevidst, hvornår I skal bidrage tilbage. At upstreame rettelser og funktioner til projekter, I afhænger af, reducerer jeres vedligeholdelsesbyrde, fordi I holder op med at bære private patches. Det bygger også velvilje og indflydelse og styrker komponenter, der er kritiske for jer. Giv udviklere en klar, hurtig proces for godkendte bidrag, inklusive hvordan intellektuel ejendomsret og bidragsyderaftaler håndteres. Når I udgiver jeres egne open source-projekter, så gør det ordentligt: vælg en passende licens, dokumentér styring, og forpligt jer til forvaltning. Et forladt projekt skader jeres omdømme mere end intet projekt.

### Opfyld offentlige open source- og "public money, public code"-mandater

Offentlige teams bør behandle åbenhed som standard. Foretræk åbne standarder for at undgå indlåsning og for at arbejde på tværs af agenturer og leverandører. Offentliggør åbent kildekode udviklet med offentlige midler, medmindre en specifik, dokumenteret undtagelse gælder: for sikkerhedsfølsomme komponenter, tredjeparters rettigheder eller privatlivshensyn. Genbrug, før I bygger: tjek, om et andet agentur allerede har udgivet passende kode. Bag disse forventninger ind i indkøb, så leverandører leverer åben, genbrugelig, veldokumenteret kode, hvor staten beholder passende rettigheder, frem for proprietære sorte bokse, agenturet ikke kan vedligeholde eller dele.

### Styr afhængigheder og end-of-life-software

Hold en levende fortegnelse (SBOM) over hver komponent og dens version, licens og vedligeholdelsesstatus. Hold afhængigheder rimeligt aktuelle. Små, hyppige opdateringer er langt billigere og sikrere end sjældne, gigantiske spring. Hold øje med opstrøms projekter for end-of-life-meddelelser og sikkerhedssupportvinduer, og planlæg migreringer, før supporten ender, ikke efter en sårbarhed tvinger en panik. For kritiske komponenter i risiko for at blive forladt så afgør på forhånd, om I vil finansiere vedligeholderen, bidrage med vedligeholdelse selv, forke eller erstatte. Følg end-of-life for kommerciel og open source-software ens, og hold det at løbe tør for support til samme standard som enhver anden driftsrisiko.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper |
|---|---|---|
| Forbrug open source frit | Hurtig levering; enorm løftestang; ingen licensgebyrer | Licens-, sikkerheds- og vedligeholdelsesforpligtelser, I nu ejer |
| Streng licensgodkendelsesliste | Lav juridisk risiko; forudsigelig | Sinker teams; kan udelukke reelt nyttige komponenter |
| Kun permissive licenser | Minimale forpligtelser; let at kombinere | Opgiver værdifulde copyleft-projekter; mindre gensidighed |
| Acceptér copyleft, hvor det passer | Adgang til stærke økosystemer; fordele ved gensidighed | Kræver omhu i kombination og distribution |
| Bidrag upstream | Mindre byrde med private patches; indflydelse; velvilje | Løbende indsats; IP- og procesoverhead |
| Byg proprietært i stedet | Fuld kontrol; ingen eksterne forpligtelser | Høj omkostning; genopfinder råvarer; I vedligeholder det for evigt |
| Offentlig offentliggørelse som standard | Åbenhed; genbrug; undgår indlåsning | Offentliggørelsesindsats; sikkerhedsgennemgang; vedvarende forvaltning |

Den centrale spænding er mellem udviklerfart og kontrol. Lås alt inde bag tung gennemgang, og udviklere går udenom politikken. Det skaber uforvaltede skyggeafhængigheder, som er værre end en tilladende-men-synlig tilgang. Lad det være helt ukontrolleret, og I ophober juridisk og sikkerhedsmæssig gæld usynligt. Løsningen er automatisering og kuratering: gør den kompatible sti til den hurtigste sti, gennem forhåndsefterprøvede komponenter, pipelinescanning og klare standarder, så I får kontrol uden friktion. Med hensyn til copyleft er afvejningen ikke "risikabel versus sikker", men "forstået versus ikke." Copyleft er fuldt brugbart, når I ved, hvordan I kombinerer og distribuerer.

## Spørgsmål til drøftelse med dit team

1. **Hvad er jeres eksplicitte regel for stærk copyleft og netværkscopyleft på tværs af interne, distribuerede og netværksserverede kontekster?** Copyleft er en designbegrænsning, ikke et tabu, og forpligtelserne afhænger af to ting: om I distribuerer softwaren, og hvor tæt I kombinerer komponenter. GPL i et internt værktøj opfører sig meget anderledes end GPL linket ind i et produkt, I leverer, og AGPL udvider offentliggørelsespligter til software, I blot tilbyder over et netværk, hvilket ændrer jeres byg-versus-adoptér-regnestykke for alt, I kører som en tjeneste. Skriv reglen ned pr. kontekst, så en udvikler uden at ringe til en jurist ved, at (for eksempel) permissiv er forhåndsgodkendt overalt, stærk copyleft er fint internt, men blokeret fra det leverede produkt, og AGPL kræver gennemgang, før den rører en netværkstjeneste. Tag dokumentation med: scan jeres nuværende afhængighedstræ, og find, hvor copyleft-komponenter allerede sidder i forhold til jeres distributionsgrænse. Luk så buildet på den politik, fordi en regel, ingen scanner håndhæver, er en regel, udviklere ved et uheld vil bryde.

2. **Har I brug for et Open Source Program Office, og hvem ejer licenspolitik, scanning og bidragsbeslutninger i dag?** Hvis det ærlige svar er "ingen" eller "hvert team afgør", kører I et fri-for-alle, der ophober juridisk og sikkerhedsmæssig gæld usynligt. Et OSPO, selv én person plus en tværfaglig arbejdsgruppe, dæmper kaosset og indfanger strategisk værdi: hvilke opstrøms projekter der skal investeres i, hvornår man skal bidrage, og hvordan man udgiver sine egne projekter godt. Tag dokumentation med til mødet: kan nogen frembringe den aktuelle godkendte licensliste, SBOM'en og navnet på den person, der ville besvare et copyleft-spørgsmål under due diligence ved et opkøb? Svaret bør tildele klart ejerskab og gøre den kompatible sti til den hurtigste sti, gennem forhåndsefterprøvede komponenter og pipelinescanning, så udviklere får kontrol uden friktion. En politik langsommere end at kopiere kode bliver simpelthen ignoreret.

3. **Hvilke afhængigheder ville gøre mest ondt, hvis de blev forladt i morgen, og hvad er jeres forhåndsafgjorte respons for hver?** Hver afhængighed når end-of-life til sidst, og den dyre version af den begivenhed er at opdage, at en kernekomponent mistede support for måneder siden, først når en sårbarhed tvinger opmærksomhed. For jeres kritiske komponenter i risiko for at blive forladt så afgør på forhånd, om I vil finansiere vedligeholderen, bidrage med vedligeholdelse selv, forke eller erstatte. Tag dokumentation med: fra jeres SBOM så list de komponenter, hvis svigt ville stoppe en omsætnings- eller missionskritisk tjeneste, og notér hvers vedligeholdelsesstatus og sikkerhedssupportvindue. Svaret bør forvandle end-of-life fra en overraskelse til en sporet driftsrisiko med en planlagt migrering, holdt til samme standard som enhver anden risiko. At holde afhængigheder aktuelle i små, hyppige skridt er langt billigere end det sjældne, gigantiske, tvungne spring.

4. **Kan I frembringe en komplet, aktuel SBOM, der når helt ned gennem jeres transitive afhængighedstræ, og hvor hurtigt?** Når en overskriftssårbarhed lander i et udbredt bibliotek, er det første spørgsmål, ledelsen stiller, "er vi eksponeret, og hvor?" Et team, der ikke kan svare inden for timer, er allerede bagud, fordi den reelle risiko som regel gemmer sig flere lag nede i afhængigheder, ingen valgte med vilje. Det modstridende hensyn er omkostning og støj: fuld transitiv fortegnelse på tværs af mange tjenester genererer en stor, skiftende liste, og overalarmering træner folk til at ignorere den, så I må afgøre, hvilken dybde og hvilken alvorlighed der faktisk udløser handling. Tag dokumentation med til drøftelsen: prøv at generere en frisk SBOM for én produktionstjeneste lige nu, tæl hvor mange komponenter der er direkte versus transitive, og mål hvor lang tid det tog. For en virksomheds- eller offentlig organisation så bind det til et konkret hændelsesresponsmål og til enhver regulatorisk pligt til at oplyse berørte komponenter, fordi et mandat om at rapportere eksponering, I ikke kan opregne, er et mandat, I vil bryde.

5. **Hvornår er en kritisk afhængighed værd at finansiere, bidrage til eller forvalte, frem for at behandle den som gratis?** De fleste organisationer forbruger open source, som var det et forsyningsvirksomhed, og bliver så chokerede, når en komponent, der understøtter en omsætningstjeneste, viser sig at være én ulønnet frivillig. At beslutte bevidst at finansiere en vedligeholder, upstreame rettelser eller udgive og forvalte jeres eget projekt forvandler et skrøbeligt gratis input til et varigt, påvirket et, og det forhindrer jeres ingeniører i at bære private patches gennem hver opgradering. Spændingen er, at bidrag og forvaltning koster reel, løbende ingeniørtid og bærer intellektuel ejendomsret og procesoverhead, så I kan ikke gøre det for alt. Tag dokumentation med: fra jeres SBOM så markér den håndfuld komponenter, hvis svigt ville stoppe en missionskritisk tjeneste, og notér hvers antal vedligeholdere, finansiering og hvor mange private patches I allerede bærer mod den. For en stor eller offentlig organisation så vej omdømmeomkostningen ved en forladt open source-udgivelse, I udgav med fanfare, og i det offentlige så behandl vedvarende forvaltning af offentliggjort kode betalt af offentlige penge som en del af leverancen, ikke et valgfrit ekstra.

6. **Leverer jeres indkøb faktisk åben, genbrugelig, veldokumenteret kode med de rettigheder, I har brug for, eller proprietære sorte bokse, I ikke kan vedligeholde eller forlade?** Kontrakter skrevet uden open source-ekspertise afleverer rutinemæssigt kontrol til en leverandør, I vil fortryde: lukkede formater, ingen ret til at offentliggøre eller ændre og afhængigheder, agenturet ikke kan patche, når leverandøren går videre. At få det rigtigt tidligt er langt billigere end at opdage ved fornyelsen, at I ikke kan forlade den. De modstridende hensyn er fart og leverandørvalg: at kræve åbne leverancer og portabilitet kan indsnævre feltet og sinke en tildeling, og nogle reelt nyttige leverandører modsætter sig det. Tag dokumentation med: træk to nylige kontrakter, og tjek, om de specificerer licensvilkår, kildekodeaflevering, dokumentationsstandarder, SBOM-levering og de rettigheder, organisationen beholder. For virksomhedsindkøb så bind det til indlåsning og samlet-ejeromkostningsanalyse; for det offentlige så bind det til åben-som-standard og "public money, public code"-mandater og til den dokumenterede undtagelsesproces, der lader jer lukke kun de sikkerhedsfølsomme dele frem for hele systemet.

## Sektorperspektiv

**Startup.** I samler næsten alt af open source og har ingen jurist, så hold reglen til én side: permissive licenser som MIT og Apache 2.0 er forhåndsgodkendte, stærk copyleft er fint til internt værktøj, men blokeret fra det leverede produkt, og alt mærkeligt får en hurtig gennemgang af en grundlægger. Tilføj en licens- og sårbarhedsscanning til pipelinen, og hold en SBOM fra dag ét, fordi det billigste tidspunkt at få det rigtigt er før en opkøbers due diligence gennemkæmmer jeres afhængighedstræ. Forbyd ikke copyleft af frygt; forstå det, og gå videre.

**Lille virksomhed.** Uden en open source-specialist og med et stramt budget så støt jer til værktøj frem for mandskab: en scanner i buildet og en kort godkendt licensliste gør det meste af det arbejde, et menneske ville. Ram forbrug ind som køb-versus-byg ærligt, da det at genopfinde en velvedligeholdt åben komponent som regel er det dyre valg, men det er også at afhænge af en, I aldrig opgør. Hold en simpel optegnelse over, hvad I bruger og under hvilken licens, så et kundesikkerhedsspørgeskema eller en sårbarhedsalarm ikke bliver en panik.

**Stor virksomhed.** I skala er problemet ensartethed på tværs af mange teams, så rejs et OSPO til at eje politik, automatiseret scanning, kildeangivelsesgenerering og bidragsstyring, og gør den kompatible sti til den hurtigste sti gennem kurerede, forhåndsefterprøvede komponenter. Håndhæv copyleft-regler pr. kontekst i pipelinen, vedligehold SBOM'er på tværs af tjenester, og styr afhængighedsaktualitet og end-of-life som sporet driftsrisiko. Behandl open source som forsyningskædestyring for størstedelen af jeres kodebase, med revisionsklar dokumentation til opkøbs-due-diligence.

**Offentlig sektor.** Åbenhed er ofte påbudt, ikke valgfri, så vælg som standard åbne standarder, og offentliggør kode betalt af offentlige penge, medmindre en dokumenteret undtagelse gælder for sikkerhed, tredjeparters rettigheder eller privatliv. Genbrug, før I bygger, ved at tjekke et tværgående offentligt katalog, og bag åbne, genbrugelige, veldokumenterede leverancer og beholdte rettigheder ind i indkøb, så I modtager vedligeholdelsesvenlig kode frem for proprietære sorte bokse. Hold offentliggjort kode til reel forvaltning, og hold undtagelsesprocessen snæver og åben, så den kun lukker det, den må.

## Eksempler

**Startup.** Et startup på fire personer, der bygger en mobilapp, samler næsten alt af open source og har ingen jurist ansat. I stedet for at forbyde copyleft af frygt skriver grundlæggerne en politik på én side: permissive licenser som MIT og Apache 2.0 er forhåndsgodkendte, stærk copyleft som GPL er fint til internt værktøj, men blokeret fra den leverede app for at undgå offentliggørelsespligter, og alt usædvanligt får en hurtig gennemgang af en grundlægger. De tilføjer en licens- og sårbarhedsscanning til pipelinen, så en forbudt licens ikke kan glide ind i en release, holder en SBOM fra dag ét og upstreamer en lille rettelse til et kritisk bibliotek, så de holder op med at bære en privat patch gennem hver opgradering. At få det rigtigt tidligt skåner dem også for en smertefuld overraskelse, når en opkøbers due diligence til sidst gennemkæmmer afhængighedstræet.

**Stor virksomhed.** En softwareleverandør, der leverer et distribueret produkt, driver et OSPO. OSPO'et vedligeholder en godkendt licensliste, et internt kurateret komponentrepository og automatiseret licens- og sårbarhedsscanning i hver pipeline. Når en udvikler trækker en ny afhængighed ind, tjekker pipelinen dens licens mod politik, genererer de kildeangivelsesmeddelelser, der leveres med produktet, og flagger alt, der kræver gennemgang. Stærk-copyleft-komponenter er tilladt til internt værktøj, men blokeret fra det distribuerede produkt, for at undgå offentliggørelsesforpligtelser. Virksomheden upstreamer rettelser til nogle få kritiske afhængigheder. Det eliminerede et efterslæb af private patches, dens ingeniører plejede at bære gennem hver opgradering.

**Offentlig sektor.** En national digital tjeneste opererer under en "public money, public code"-politik. Nye tjenester bygges på åbne standarder, udvikles åbent på et offentligt kode-repository som standard og genbruges på tværs af agenturer. Dens indkøbsskabeloner kræver, at leverandører leverer åben, veldokumenteret, genbrugelig kode, hvor staten beholder retten til at offentliggøre og ændre. Før start på en ny komponent søger teams i et tværgående katalog efter eksisterende genbrugelig kode. Sikkerhedsfølsomme moduler undtages fra offentliggørelse gennem en dokumenteret proces frem for ved at gøre hele systemet lukket.

## Business case: motivation, ROI og TCO

At styre open source godt er forskellen mellem at indfange dens enorme løftestang og at betale for dens skjulte omkostninger. Open source lader en stor organisation stå på et fundament, den aldrig ville have råd til at bygge. Men den [samlede ejeromkostning](https://en.wikipedia.org/wiki/Total_cost_of_ownership) inkluderer compliance, sikkerhedspatching og eventuel migrering, omkostninger der ankommer, uanset om I planlægger for dem. Bevidst styring konverterer uforudsigelige, dyre kriser til små, jævne, planlagte omkostninger. De kriser omfatter en copyleft-overtrædelse fundet under opkøbs-due-diligence, en nødmigrering væk fra en forladt komponent eller en sårbarhed i en afhængighed, ingen vidste var der.

Adoptionsomkostningen er beskeden ved siden af eksponeringen: et OSPO eller en arbejdsgruppe, scanningsværktøj og disciplinen i at holde en fortegnelse. Omkostningen ved *ikke* at adoptere viser sig som juridisk ansvar, dumpet due diligence, sikkerhedshændelser sporet til upatchede afhængigheder og den akkumulerende udgift ved udskudte opgraderinger, der til sidst tvinger smertefulde big-bang-migreringer. Når I fremlægger sagen for ledelsen, så ram open source-styring ind som forsyningskædestyring for størstedelen af jeres kodebase. Bemærk også den strategiske opside: undgået indlåsning, hurtigere levering, talenttiltrækning og indflydelse over de økosystemer, I afhænger af. I det offentlige så tilføj mandatdimensionen. Åbenhed er ofte påkrævet, ikke valgfri, og at gøre det godt undgår både manglende overholdelse og duplikeret offentligt forbrug.

## Anti-mønstre og faldgruber

- **Kopier-og-indsæt-licensering.** Udviklere trækker komponenter ind uden licenstjek og opdager først forpligtelser ved revision eller opkøb.
- **Ingen fortegnelse.** At være ude af stand til at svare på "hvad bruger vi og under hvilken licens?", når en sårbarhed eller licensspørgsmål bryder ud.
- **Copyleft-panik.** At forbyde al copyleft af frygt frem for forståelse og opgive værdifulde økosystemer.
- **Den forladte open source-udgivelse.** At udgive et projekt med fanfare og så aldrig vedligeholde det, hvilket skader omdømmet.
- **At ignorere transitive afhængigheder.** At efterprøve direkte afhængigheder, mens den reelle risiko gemmer sig flere lag nede.
- **End-of-life-overraskelse.** At opdage, at en kernekomponent mistede support for måneder siden, først når en sårbarhed tvinger opmærksomhed.
- **Politik langsommere end at kopiere.** En complianceproces så tung, at udviklere går udenom den og skaber usynlige skyggeafhængigheder.
- **Offentlige sorte bokse.** At indkøbe proprietære systemer, agenturet ikke kan vedligeholde, dele eller forlade, i strid med åben-som-standard-principper.

## Modenhedsmodel

**Niveau 1: Opstart.** Udviklere tilføjer open source frit uden politik eller fortegnelse. Licenser er uundersøgte, og copyleft-forpligtelser er ukendte. End-of-life opdages ved et tilfælde, som regel når en sårbarhed tvinger opmærksomhed. Ingen ejer open source-strategi.

**Niveau 2: Udvikling.** En basal politik og godkendt licensliste findes, og nogle teams følger dem. Scanning sker, men ofte manuelt, sent eller kun på nogle få projekter. En fortegnelse føres for større systemer, mens transitive afhængigheder forbliver ukortlagte. Bidrag og end-of-life-håndtering er ad hoc og inkonsistent mellem teams.

**Niveau 3: Standardisering.** Et OSPO eller tilsvarende ejer strategi, politik og værktøj i hele organisationen. Licens- og sårbarhedsscanning er automatiseret i hver pipeline, kildeangivelses- og meddelelsesfiler genereres automatisk, og buildet lukkes, så en forbudt licens ikke kan komme ind. SBOM'er vedligeholdes ned gennem det transitive træ, bidrag følger en dokumenteret proces, end-of-life følges med planlagte migreringer, og offentlige teams offentliggør som standard.

**Niveau 4: Styring.** Programmet måles og styres mod baselines. I følger politikscanningsdækning på tværs af tjenester, gennemsnitlig tid til at patche en offentliggjort afhængighedssårbarhed, andelen af komponenter inden for deres sikkerhedssupportvindue, licensovertrædelsesundslippelsesrate, afhængighedsaktualitetsforsinkelse og antallet af private patches båret upstream. Copyleft-placering i forhold til distributionsgrænsen overvåges, og målinger mod mål driver hver go/no-go-beslutning frem for mening.

**Niveau 5: Orkestrering.** Open source er et løbende forbedret strategisk aktiv integreret på tværs af organisationen. Compliance er fuldt automatiseret, og ikke-kompatible komponenter kan ikke nå produktion. I investerer bevidst i kritiske opstrøms projekter, bidrager rutinemæssigt og forvalter jeres egne veldrevne projekter. Afhængighedsaktualitet og end-of-life styres adaptivt, efterhånden som risiko og målinger skifter, og åbenhed bliver en ægte konkurrence- og borgerfordel.

## Idéer til drøftelse

- Hvor går den rette linje mellem en hurtig permissiv standard og den kontrol, der skal til for at undgå juridisk og sikkerhedsmæssig gæld?
- Hvornår bør en organisation finansiere eller vedligeholde en kritisk opstrøms afhængighed frem for at behandle den som gratis?
- Hvordan afgør I, hvilke af jeres egne komponenter der er værd at udgive og forvalte som open source?
- For det offentlige, hvad er en forsvarlig proces til at undtage komponenter fra offentliggørelse som standard uden at udhule princippet?
- Hvor dybt ned i transitive afhængigheder må licens- og sikkerhedsgennemgang realistisk gå?
- Ændrer netværkscopyleft (AGPL) jeres byg-versus-adoptér-regnestykke for software, I tilbyder som en tjeneste?

## Vigtigste pointer

- Open source er størstedelen af de fleste kodebaser og skal styres som en forsyningskæde, ikke behandles som gratis og uden konsekvenser.
- Licenser bærer reelle forpligtelser; forstå familierne permissiv, svag copyleft, stærk copyleft og netværkscopyleft, og hvordan distribution og kombination udløser pligter.
- Gør den kompatible sti til den hurtigste sti gennem kuratering, automatiseret scanning og klare standarder, ellers går udviklere udenom politikken.
- Rejs et OSPO til at eje strategi, compliance, bidrag og forvaltning i skala.
- Oprethold en SBOM, hold afhængigheder aktuelle i små skridt, og planlæg for end-of-life, før det tvinger en krise.
- I det offentlige: vælg som standard åbne standarder, offentliggør kode betalt af offentlige penge, og genbrug, før I bygger.

## Referencer og videre læsning

- Heather Meeker, *Open (Source) for Business* and *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation and TODO Group, *OSPO guides* and *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* and *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* and approved licence list
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy and Code.gov guidance
- UK Government, *Technology Code of Practice* and open-standards principles
