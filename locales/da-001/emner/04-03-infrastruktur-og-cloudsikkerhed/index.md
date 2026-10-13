# 4.3 Infrastruktur- og cloudsikkerhed

## Overblik og motivation

Applikationer kører på infrastruktur, og i dag er den infrastruktur for det meste cloudbaseret, softwaredefineret og i konstant forandring. En enkelt ingeniør kan nu provisionere en database, åbne en netværkssti eller give en tilladelse med én kommando, i en skala og et tempo, som traditionel ændringskontrol aldrig forudså. Den kraft er netop grunden til, at fejlkonfiguration, ikke eksotiske exploits, er den ledende årsag til cloudbrud. En ved et uheld offentlig lagerspand eller en for bred adgangsrolle kan blotlægge en hel organisations data på sekunder.

For store virksomheder spænder cloudinfrastruktur over flere udbydere, tusinder af konti og en blanding af administrerede tjenester, containere og serverless-funktioner. Angrebsfladen er ikke en statisk perimeter. Den er en levende, udstrakt samling af ressourcer og identiteter. For det offentlige møder den samme kompleksitet strenge autorisationsregimer, dataresidenskrav og klassifikationsgrænser, der former hvert arkitekturvalg. I begge er identitetslaget blevet den nye perimeter: hvem der kan gøre hvad, ved hvilken ressource, under hvilke betingelser.

Dette kapitel dækker, hvordan man sikrer det fundament: [identitets- og adgangsstyring](https://en.wikipedia.org/wiki/Identity_management) (IAM), [netværkssegmentering](https://en.wikipedia.org/wiki/Network_segmentation), [kryptering](https://en.wikipedia.org/wiki/Encryption) og [nøglestyring](https://en.wikipedia.org/wiki/Key_management), sikkerheden af containere og [serverless](https://en.wikipedia.org/wiki/Serverless_computing)-arbejdsbyrder og den kontinuerlige holdningsstyring, der holder en hurtigt bevægende cloudejendom fra at drive ind i fare.

## Grundprincipper

- **Identitet er perimeteren.** Adgangsbeslutninger afhænger af stærk identitet og finkornet autorisation, ikke netværksplacering.
- **Mindste privilegium, altid.** Hver identitet, menneskelig eller maskine, får de mindste nødvendige tilladelser og ikke mere.
- **Segmentér for at indgrænse.** Opdel netværk og arbejdsbyrder, så en kompromittering ét sted ikke frit kan sprede sig.
- **Krypter overalt.** Beskyt data under transport og i hvile som standard, med velstyrede nøgler.
- **Uforanderlig og deklarativ.** Definér infrastruktur som kode (IaC), udrul uforanderligt, og behandl drift som en defekt.
- **Kontinuerlig verifikation.** Sikkerhedsholdning er ikke en engangsrevision; scan og håndhæv kontinuerligt.
- **Sikker standardkonfiguration.** Standardtilstanden for enhver ressource bør være låst ned, ikke åben.

## Anbefalinger

### Design identitets- og adgangsstyring bevidst

IAM er den vigtigste del af cloudsikkerhed og den hyppigst fejlstyrede.

- Brug **[rollebaseret adgangskontrol](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** til at give tilladelser efter jobfunktion og **[attributbaseret adgangskontrol](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)**, hvor der er brug for finere, kontekstbevidste beslutninger (baseret på tags, miljø, dataklassificering eller tid).
- Eliminér langlivede statiske legitimationer til fordel for kortlivede, automatisk udstedte tokens og føderation af arbejdsbyrdeidentitet.
- Håndhæv [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (multifaktorautentificering) for al menneskelig adgang, og kræv stærk autentificering for privilegerede handlinger.
- Anvend mindste privilegium stringent: start fra nul og tilføj tilladelser bevidst. Gennemgå og beskær regelmæssigt ubrugte tilladelser; adgang har tendens til at akkumulere.
- Adskil opgaver, så ingen enkelt identitet både kan foretage og godkende følsomme ændringer.
- Brug dedikerede konti eller projekter til at skabe hårde grænser mellem miljøer (produktion, staging, udvikling) og mellem forretningsenheder.

### Segmentér netværk og mikrosegmentér arbejdsbyrder

Flade netværk lader angribere bevæge sig sideværts, når de først er inde. Opdel og indgræns.

- Segmentér på netværksniveau i lag og zoner, og tillad kun den trafik, hvert lag legitimt har brug for.
- Anvend **mikrosegmentering**, så individuelle arbejdsbyrder kun kommunikerer med de specifikke peers, de kræver, håndhævet af identitetsbevidst politik frem for brede subnetregler.
- Afvis øst-vest-trafik som standard; kræv eksplicitte tilladelsesregler.
- Placér følsomme datalagre i private subnet uden direkte internetadgang, kun nået gennem kontrollerede stier.
- Brug privat konnektivitet til administrerede tjenester i stedet for at route over det offentlige internet, hvor det er muligt.

### Krypter data og styr nøgler ordentligt

Kryptering er kun nogensinde så stærk som nøglestyringen bag den.

- Krypter **under transport** med aktuel [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) overalt, herunder intern tjeneste-til-tjeneste-trafik.
- Krypter **i hvile** som standard for alt lager, alle databaser og backups.
- Styr nøgler med en **nøglestyringstjeneste (KMS)**, og brug et **[hardwaresikkerhedsmodul](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** til nøgler med højeste assurance og til regulatoriske krav.
- Roter nøgler efter en plan, og understøt hurtig rotation ved mistanke om kompromittering.
- Kontrollér og revidér, hvem der kan bruge og styre nøgler, adskilt fra hvem der kan tilgå dataene, så nøglevaretægt håndhæver adskillelse af opgaver.
- Overvej kundestyrede nøgler, hvor regulering eller kontraktlig tillid kræver, at organisationen holder nøglerne frem for udbyderen.

### Sikr containere, Kubernetes og serverless

Hver beregningsmodel bringer sine egne risici.

- **Containere:** byg fra minimale, betroede basisbilleder; scan billeder for sårbarheder før udrulning; kør som ikke-root; gør filsystemer skrivebeskyttede, hvor det er muligt; og bag aldrig hemmeligheder ind i billeder.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** slå RBAC til og afgræns tjenestekonti snævert; anvend netværkspolitikker til mikrosegmentering; brug admission controllers og politikmotorer til at håndhæve standarder; begræns privilegerede containere; isolér følsomme arbejdsbyrder; og hold kontrolplanet og noderne patchet.
- **Serverless:** anvend mindste privilegium på hver funktions eksekveringsrolle (en almindelig kilde til overtilladelse); validér alle hændelsesinput; styr hemmeligheder gennem platformens hemmelighedslager; og overvåg for unormale kaldemønstre.

Uanset modellen så hold runtimen patchet og billederne friske. En container er kun så sikker som softwaren indeni.

### Styr cloudsikkerhedsholdning kontinuerligt

Skyen ændrer sig langt for hurtigt til, at periodiske manuelle revisioner kan følge med.

- Adoptér værktøj til **Cloud Security Posture Management (CSPM)** for kontinuerligt at opdage fejlkonfigurationer, offentlig eksponering og politikovertrædelser på tværs af konti.
- Definér sikkerhedspolitik som kode og håndhæv den på udrulningstidspunktet, så dårlige konfigurationer blokeres, før de lander.
- Foretræk forebyggelse (rækværk, der stopper fejlkonfiguration) frem for detektion (alarmer bagefter), og kombinér begge.
- Vedligehold en nøjagtig opgørelse over ressourcer og identiteter; du kan ikke sikre, hvad du ikke kan se.
- Følg og udbedr drift mellem erklæret infrastruktur-som-kode og den faktiske kørende tilstand.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| RBAC | Simpel, forståelig, let at revidere | Grov, rolleeksplosion i skala |
| ABAC | Finkornet, kontekstbevidst, skalerer med tags | Kompleks at designe og ræsonnere om |
| Udbyderstyrede nøgler (KMS) | Let, integreret, lav driftsbyrde | Udbyderen har varetægten; mindre kontrol |
| Kundestyrede nøgler/HSM | Fuld kontrol, opfylder strenge påbud | Driftsoverhead, risiko for at miste nøgler |
| Forebyggende rækværk | Stopper fejlkonfiguration, før den sker | Kan blokere legitimt arbejde, kræver justering |
| Kun detektiv CSPM | Fleksibel, ikke-blokerende | Skade kan ske før detektion |
| Mikrosegmentering | Stærk indgrænsning af sidelæns bevægelse | Driftskompleksitet, politikvildtvækst |

Den dominerende afvejning er kontrol versus driftsbyrde. Strammere kontroller (kundestyrede nøgler, streng mikrosegmentering, ABAC) reducerer risiko, men de kræver ekspertise og vedligeholdelse, som små teams har svært ved at opretholde. Det rette niveau afhænger af, hvor følsomme dataene er, og hvilke reguleringer der gælder. En pragmatisk tilgang lægger stærke sikre standarder for alle og forbeholder så ekstra stringens til de højeste risikosystemer, og den foretrækker automatiserede rækværk, der gør det sikre valg til standarden frem for en manuel disciplin.

## Spørgsmål til drøftelse med dit team

1. **Hvor vil I trække hårde konto- eller projektgrænser, og hvad hører hjemme inden for hver?** Dedikerede konti og projekter skaber den stærkeste indgrænsning, skyen tilbyder, så en kompromittering i udvikling ikke kan nå produktion, og én forretningsenhed ikke kan røre en andens data. Beslut jeres grænseskema, før jeres ejendom vokser til tusinder af konti, fordi det er langsomt og risikabelt at eftermontere isolation på en flad struktur. For virksomheds- og offentligt arbejde afbildes disse grænser også pænt til miljøadskillelse, dataklassificering og de sprængradiusgrænser, revisorer forventer at se. Tag et nuværende diagram over, hvilke arbejdsbyrder der deler en konto i dag, og markér, hvor en enkelt for bred rolle spænder over produktion og ikke-produktion. Hvis følsomme data sidder i samme konto som eksperimentelle arbejdsbyrder, er det grænsen, der skal rettes først.

2. **Hvad er jeres standard for, hvem der kan styre nøgler versus hvem der kan tilgå de krypterede data?** Kryptering er kun så stærk som nøglestyring, og at adskille nøglevaretægt fra dataadgang gør jeres KMS til et håndhævelsespunkt for adskillelse af opgaver. Beslut, hvem der må oprette, rotere og bruge nøgler, og sørg for, at det sæt ikke overlapper med de personer, der kan læse de data, nøglerne beskytter. For regulerede og offentlige systemer driver det ofte valget mellem udbyderstyrede nøgler og kundestyrede nøgler eller HSM'er, som bærer mere kontrol og mere driftsrisiko for at miste nøgler. Tag jeres nuværende nøglepolitikker med og tjek, om nogen enkelt identitet både kan styre en nøgle og læse dataene bagved, for det er et almindeligt stille hul. Hvis varetægt og adgang ikke er adskilt, beskytter kryptering i hvile jer mindre, end dashboardet antyder.

3. **Hvordan vil I gøre sikre standarder uundgåelige i jeres landing zone frem for blot anbefalede?** Fejlkonfiguration, ikke eksotiske exploits, er den ledende årsag til cloudbrud, og rettelsen er forebyggende rækværk, der blokerer en offentlig database eller en ukrypteret spand, før den lander, ikke alarmer bagefter. Beslut, hvilke politikker I vil håndhæve på udrulningstidspunktet (ingen offentligt lager, kryptering slået til som standard, obligatoriske tags), og hvilke I kun vil detektere og rapportere. For et stort team betyder det at kode disse ind i landing zones og infrastruktur-som-kode-skabeloner, at hver ny konto arver beskyttelse uden indsats pr. team, hvilket forvandler sikkerhed fra en tilbagevendende skat til en engangsinvestering. Tag jeres seneste måneds fejlkonfigurationsfund med og spørg, hvilke et forebyggende rækværk ville have stoppet direkte. Hvis jeres holdningsstyring kun er detektiv, kan skade ske, før nogen ser alarmen, så flyt de højeste konsekvenstjek til forebyggelse.

4. **Hvordan eliminerer I langlivede statiske legitimationer uden at bryde den automatisering, der stille afhænger af dem?** Indlejrede adgangsnøgler, der aldrig udløber, er blandt de mest almindelige årsager til cloudbrud, fordi en enkelt lækket nøgle i et script, en log eller et repository giver en angriber varig adgang. Det modstridende træk er driftsmæssigt: legacy CI-job, cron-opgaver og tredjepartsintegrationer antager ofte, at en statisk nøgle findes, og at omlægge dem til kortlivede tokens eller føderation af arbejdsbyrdeidentitet tager ingeniørtid, ingen har planlagt. For et stort team forhindrer en fælles migreringssti (udsted tokens automatisk, sæt en udløbsstandard og alarmér på enhver ny langlivet nøgle), at hver gruppe opfinder sit eget svagere svar. Tag en opgørelse over hver statisk legitimation i brug med, dens alder, dens sprængradius og om det system, den fodrer, kan acceptere føderet identitet i dag. I virksomheds- og offentlige sammenhænge så bind fristen til revisions- og autorisationscyklusser, fordi en legitimation, der overlever den person, der oprettede den, er præcis det fund, der standser en kontinuerlig autorisation.

5. **Når en ressource er fejlkonfigureret, eller en nøgle er kompromitteret, hvor hurtigt kan I opdage, indgrænse og udbedre det, og har I målt det?** En offentlig spand eller en for bred rolle er kun så farlig som det vindue, den står åben, så gennemsnitlig tid til at opdage og udbedre er det tal, der faktisk afgrænser jeres eksponering. Spændingen er mellem forebyggende rækværk, der stopper fejlen på udrulningstidspunktet, og detektiv holdningsstyring, der fanger det, der slipper igennem, og I har brug for ærlige tal for begge frem for en betryggende antagelse om, at rækværk dækker alt. Tag jeres sidste kvartals fejlkonfigurations- og driftsfund med tidsstempler, medianen af tid fra introduktion til udbedring og øvelsesoptegnelsen for en nøglekompromitterings rotation. For virksomheds- og offentlige ejendomme, der spænder over tusinder af konti, så aftal, hvem der ejer udbedring af et fund, ingen teams åbenlyst ejer, for en alarm uden en ansvarlig responder er en alarm, der ældes til en hændelse.

6. **Hvordan holder I sikkerhedsholdningen konsistent på tværs af flere skyer, konti og teams uden at sinke alle til et crawl?** Multicloud- og multikontoejendomme fragmenterer hurtigt: hver udbyder har sin egen IAM-model, sine egne standarder og sit eget holdningsværktøj, så en politik håndhævet ét sted stille lapser et andet. Afvejningen er mellem central kontrol, der garanterer konsistens, og lokal autonomi, der lader teams bevæge sig hurtigt, og at læne sig for langt i begge retninger enten flaskehalser leveringen eller lader standarder drive. Tag jeres nuværende dækningskort med: hvilke konti der arver landing zone-rækværk, hvilke der er ustyrede, og hvor den samme kontrol er udtrykt på tre forskellige måder på tværs af udbydere. For en stor eller offentlig organisation så tilføj revisionsvinklen, fordi revisorer forventer én forsvarlig standard anvendt overalt, og en kontrol, der findes i jeres primære sky, men ikke den sekundære, er et hul, en målrettet angriber eller vurderingsmand vil finde først.

## Sektorperspektiv

**Startup.** Hastighed og overlevelse vinder, så støt jer helt til sikre standarder, der følger gratis med: kryptering i hvile slået til, lager privat medmindre et menneske åbner det, MFA på rodkontoen og udbyderens indbyggede arbejdsbyrdeidentitet i stedet for indsatte adgangsnøgler. Opstil ikke en CSPM-platform eller håndrul mikrosegmentering, I ikke kan vedligeholde; et enkelt rækværk, der blokerer en database åbnet mod internettet, køber det meste af beskyttelsen for en eftermiddags arbejde. Hold alt i infrastruktur-som-kode fra starten, så hærdning skalerer med jer frem for at blive en senere omskrivning.

**Lille virksomhed.** Uden en dedikeret sikkerhedsingeniør og med et stramt budget så foretræk administrerede tjenester, hvis standarder allerede er hærdede, og hvis nøglestyring er håndteret for jer, frem for at bygge jeres egen KMS-disciplin. Behandl cloudsikkerhed som et spørgsmål om konfigurationshygiejne: vid hvilke spande og databaser der findes, hold dem private, kræv MFA, og slå udbyderens indbyggede holdningstjek til, som kommer uden ekstra omkostning. Når I køber værktøj, så foretræk dem, der flager offentlig eksponering og ukrypteret lager ud af boksen, fordi de to fejl forårsager de fleste undgåelige brud.

**Stor virksomhed.** Det reelle problem er ensartethed på tværs af tusinder af konti og mange teams, så arbejdet er platformsarbejde: landing zones, der provisionerer hver konto hærdet, rækværk håndhævet som policy-as-code og CSPM, der scanner kontinuerligt for drift. Standardisér IAM-modellen, nøglevaretægtsreglerne og segmenteringsbaselinen, så grupper holder op med at genopfinde svagere versioner, og mål holdningen på tværs af ejendommen frem for at stole på hvert teams ord. Budgettér den løbende ingeniørindsats til at holde politikker aktuelle, efterhånden som udbydere tilføjer tjenester, og ejendommen vokser.

**Offentlig sektor.** Indkøbsregler, dataresidenskrav og autorisationsregimer former hvert valg, så sikkerhedskontroller fungerer også som revisionsdokumentation. Foretræk FIPS-valideret nøglestyring med varetægt adskilt fra dataadgang, isolerede regioner, der holder data inden for nationale grænser, og signerede, scannede containerbilleder med streng admission control. Offentliggør de sikkerhedsforanstaltninger, I kan, fodr kontinuerlig holdningsstyring direkte ind i løbende autorisation, og kræv at leverandører oplyser deres konfigurationsstandarder og understøtter de segmenterings- og nøglevaretægtskontroller, jeres klassifikationsgrænser kræver.

## Eksempler

**Startup.** Et lille startup kører alt i én cloudkonto og kan ikke bemande et platformsteam, så det støtter sig til standarder, der leveres sikre: kryptering i hvile slået til som standard, lagerspande private medmindre et menneske eksplicit åbner dem, og MFA påkrævet på rodkontoen. I stedet for langlivede adgangsnøgler indsat i CI bruger det udbyderens indbyggede arbejdsbyrdeidentitet, så pipelinen automatisk får kortlivede legitimationer. Et enkelt gratis rækværk, der flager enhver database åbnet mod internettet, redder dem fra den mest almindelige og dyreste cloudfejl, til en pris af én eftermiddags opsætning.

**Stor virksomhed.** Et mediefirma, der kører tusinder af konti på tværs af to cloududbydere, håndhæver et landing zone-mønster: hver konto provisioneres fra en skabelon med kryptering i hvile slået til som standard, ingen offentlig adgang til lager, obligatoriske tags og en baseline af rækværkspolitikker. CSPM scanner kontinuerligt for drift, og føderation af arbejdsbyrdeidentitet har elimineret langlivede nøgler for CI-systemer. Da en udvikler ved et uheld forsøger at åbne en database mod internettet, blokerer en forebyggende politik ændringen og opretter automatisk en ticket.

**Offentlig sektor.** Et forsvarsnært agentur opererer i en isoleret cloudregion med dataresidens håndhævet af politik, så ingen data forlader nationale grænser. De mest følsomme nøgler bor i FIPS-validerede (Federal Information Processing Standards) HSM'er, med nøglevaretægt adskilt fra dataadgang for at håndhæve adskillelse af opgaver. Kubernetes-clustere bruger strenge netværkspolitikker og admission controls; hvert containerbillede scannes og signeres, før det må køre. Kontinuerlig holdningsstyring fodrer direkte ind i agenturets løbende autorisationsdokumentation.

## Business case: motivation, ROI og TCO

Cloudinfrastruktursikkerhed er der, hvor en lille investering afværger katastrofale tab af overskriftskaliber. De totale ejeromkostninger omfatter CSPM-værktøj, nøglestyringstjenester, ingeniørtiden til at designe IAM og segmentering efter mindste privilegium og den løbende indsats for at holde politikker aktuelle. Disse omkostninger er reelle, men beskedne. Omkostningen ved at springe dem over er én fejlkonfigureret ressource, der blotlægger en hel kundedatabase, sammen med de regulatoriske bøder, underretningsomkostninger og varig brandskade, der følger. Cloudfejlkonfigurationsbrud er blandt de mest almindelige og mest forebyggelige hændelser i branchen.

Automatisering og genbrug forstærker ROI. Kod sikre standarder ind i landing zones og infrastruktur-som-kode-skabeloner, og hver ny konto og arbejdsbyrde arver beskyttelse uden indsats pr. team, hvilket forvandler sikkerhed fra en tilbagevendende manuel skat til en engangsplatformsinvestering. For offentlige og regulerede virksomheder sænker stærk holdningsstyring også omkostningen ved revisioner og kontinuerlig autorisation ved at producere dokumentation automatisk. Når du fører sagen over for ledelsen, så understreg, at identitets- og konfigurationslaget nu er den primære brudvektor, at fejlkonfiguration er forebyggelig, og at rækværk skærer både risikoen og gnidningen ved manuel gennemgang.

## Anti-mønstre og faldgruber

- **Wildcard-tilladelser.** At give brede `*`-adgange "for at få tingene til at virke" og aldrig stramme dem.
- **Langlivede statiske nøgler.** Adgangsnøgler indlejret i scripts og CI, der aldrig udløber og til sidst lækker.
- **Flade netværk.** Ingen segmentering, så én kompromitteret vært når alt.
- **Offentlig ved uheld.** Lager og databaser eksponeret mod internettet gennem standard- eller skødesløse indstillinger.
- **Kryptering uden nøgledisciplin.** At slå kryptering til, men lade nøgleadgang stå vid åben eller aldrig rotere.
- **Hemmeligheder bagt ind i billeder.** Legitimationer indlejret i containerbilleder, der spredes overalt, billedet kører.
- **Overtilladte serverless-roller.** Funktioner givet langt mere, end de behøver, fordi afgrænsning blev sprunget over.
- **Kun-revision-holdning.** At detektere fejlkonfigurationer bagefter i stedet for at forebygge dem på udrulningstidspunktet.
- **At ignorere drift.** At lade det kørende miljø afvige fra infrastruktur-som-kode, til ingen kender den reelle tilstand.

## Modenhedsmodel

**Niveau 1: Opstart.** Manuel provisionering drevet af den, der har brug for en ressource. Brede wildcard-tilladelser og langlivede statiske nøgler. Flade netværk uden segmentering. Kryptering anvendt inkonsistent, hvis overhovedet. Ingen holdningsstyring; fejlkonfigurationer viser sig først, når en hændelse tvinger spørgsmålet.

**Niveau 2: Udvikling.** Nogle IAM-roller og MFA dukker op, og kryptering i hvile er slået til for de store lagre, men praksis varierer fra team til team. Grundlæggende netværkslag findes uden afvisning som standard. Konfigurationsgennemgange sker periodisk og i hånden. Infrastruktur er delvist defineret som kode, så hærdning afhænger af, hvilken gruppe der provisionerede kontoen.

**Niveau 3: Standardisering.** RBAC og ABAC efter mindste privilegium med kortlivede legitimationer er dokumenteret og håndhævet i hele organisationen. Segmentering bruger afvisning som standard for øst-vest. Kryptering under transport og i hvile er slået til som standard, med nøgler i KMS efter en rotationsplan og varetægt adskilt fra dataadgang. Container- og Kubernetes-hærdning er en standard, og CSPM kører mod definerede politikker anvendt ensartet på tværs af hver konto.

**Niveau 4: Styring.** Holdningen måles, ikke antages. I følger navngivne målinger mod baselines og mål: andelen af identiteter inden for deres baseline for mindste privilegium, gennemsnitlig tid til at opdage og udbedre fejlkonfigurationer og drift, rækværks- og CSPM-dækning på tværs af konti, overholdelse af nøglerotation og antallet af overlevende langlivede legitimationer. Fund triageres efter sprængradius, udbedring har en ejer og et serviceniveaumål, og tendensdata for disse tal driver, hvor den næste hærdningsindsats går hen.

**Niveau 5: Orkestrering.** Sikre standarder er bagt ind i landing zones og infrastruktur-som-kode, så hver ressource fødes hærdet, og kontrollerne tilpasser sig, efterhånden som ejendommen og trusselsbilledet skifter. Mikrosegmentering bruger identitetsbevidst politik; kundestyrede nøgler og HSM'er beskytter systemerne med højeste assurance med varetægtsadskillelse. Forebyggende rækværk blokerer fejlkonfiguration på udrulningstidspunktet, drift opdages og udbedres automatisk, og holdningsdokumentation fodrer kontinuerlig autorisation automatisk. Sikkerhed er integreret med levering og risikoplanlægning, og organisationen pensionerer og omafgrænser rutinemæssigt kontroller, efterhånden som udbydere, tjenester og reguleringer ændrer sig.

## Idéer til drøftelse

1. Hvor er ABAC sin kompleksitet værd versus at holde sig til RBAC i jeres miljø?
2. Hvordan eliminerer I langlivede legitimationer uden at bryde legacy-automatisering?
3. Hvad er den rette fordeling mellem forebyggende rækværk og detektiv holdningsstyring?
4. Hvilke systemer retfærdiggør kundestyrede nøgler eller HSM'er, givet deres driftsomkostning?
5. Hvordan forhindrer I, at tilladelser efter mindste privilegium stille akkumulerer tilbage til overprivilegium?
6. Hvordan bør multicloudkompleksitet ændre jeres tilgang til ensartet holdning og politik?

## Vigtigste pointer

- Identitet er den nye perimeter; invester i IAM efter mindste privilegium med kortlivede legitimationer.
- Segmentér netværk og mikrosegmentér arbejdsbyrder for at indgrænse kompromittering.
- Krypter under transport og i hvile som standard, og styr nøgler med KMS/HSM og adskillelse af varetægt.
- Hærd containere, Kubernetes og serverless; hold runtimes og billeder patchet.
- Foretræk forebyggende rækværk frem for detektion bagefter, og styr holdningen kontinuerligt.
- Bag sikre standarder ind i landing zones og infrastruktur-som-kode, så beskyttelse skalerer automatisk.
- Fejlkonfiguration, ikke eksotiske exploits, er den ledende årsag til cloudbrud, og den er forebyggelig.

## Referencer og videre læsning

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
