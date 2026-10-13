# 12.2 Tjeklister

Disse tjeklister er praktiske, brugsklare hurtigreferencer. Kopiér en hvilken som helst tjekliste ind i en pull request-skabelon, en wikiside, en ticket eller en dagsorden til et gennemgangsmøde, og tilpas punkterne til jeres kontekst. Behandl hvert punkt som noget, et menneske kan verificere og besvare med ja eller nej. En tjekliste er en hukommelseshjælp og en fælles standard, ikke en erstatning for dømmekraft; slet punkter, der ikke gælder, og tilføj punkter, jeres domæne kræver.

Vejledning i at bruge dem godt:

- Hold tjeklister korte nok til, at folk faktisk udfylder dem. Hvis en tjekliste rutinemæssigt springes over, er den for lang eller for generisk.
- Automatisér ethvert punkt, en maskine kan verificere (formatering, tests, scanninger), så mennesker bruger opmærksomhed på punkter, der kræver dømmekraft.
- Versionér jeres tjeklister, og gennemgå dem med jævne mellemrum. En tjekliste, der aldrig ændrer sig, bliver sandsynligvis ikke brugt.
- Skeln mellem blokerende og vejledende punkter, når forskellen har betydning for jeres proces.

## Tjekliste til kodegennemgang

Til den gennemgænger, der undersøger en andens ændring.

- [ ] Ændringen gør det, dens beskrivelse og den tilknyttede ticket siger, den gør.
- [ ] Omfanget er fokuseret på ét enkelt logisk anliggende; urelaterede ændringer er skilt ud.
- [ ] Designet passer ind i den eksisterende arkitektur og indfører ikke en kobling, der er lettere at undgå.
- [ ] Grænsetilfælde, fejlstier og fejlformer er håndteret, ikke blot den lykkelige sti.
- [ ] Der findes tests, de er meningsfulde, og de ville fejle, hvis adfærden regredierede.
- [ ] Navngivning, struktur og kommentarer gør koden forståelig for en fremtidig læser.
- [ ] Ingen hemmeligheder, legitimationsoplysninger, tokens eller personoplysninger er committet.
- [ ] Sikkerhedsfølsomt input er valideret, kodet eller parameteriseret på passende vis.
- [ ] Offentlige grænseflader, kontrakter og bagudkompatibilitet er bevaret eller bevidst versioneret.
- [ ] Logning, målinger og fejlrapportering er tilstrækkelige til at drive ændringen i produktion.
- [ ] Dokumentation, runbooks og konfiguration er opdateret, så de svarer til ændringen.
- [ ] Feedback er opdelt i blokerende problemer versus forslag og formuleret om koden.

## Tjekliste til pull request-forfatteren

Til forfatteren, før der anmodes om gennemgang.

- [ ] PR'en er lille og fokuseret nok til at blive gennemgået omhyggeligt i ét stræk.
- [ ] Beskrivelsen angiver, hvad der ændrede sig, hvorfor, og hvordan det blev verificeret.
- [ ] Den tilknyttede ticket, issue eller designdokument giver gennemgængere den nødvendige kontekst.
- [ ] Alle automatiserede tjek består lokalt eller i CI (build, lint, format, tests, scanninger).
- [ ] Ny og ændret adfærd er dækket af tests.
- [ ] Mekaniske refaktoreringer er adskilt fra adfærdsændringer.
- [ ] Selvgennemgangen er fuldført: I har læst jeres egen diff linje for linje.
- [ ] Ingen fejlfindingskode, udkommenterede blokke, hemmeligheder eller løse filer er tilbage.
- [ ] Databasemigreringer, feature flags og konfigurationsændringer er dokumenteret og reversible.
- [ ] Brydende ændringer er påpeget eksplicit med en migreringssti.
- [ ] Skærmbilleder, optagelser eller eksempeloutput er med, hvor de hjælper gennemgangen.
- [ ] De rette gennemgængere og eventuelle påkrævede rollebaserede godkendere er anmodet.

## Definition of Done

Den fælles standard, et arbejdspunkt skal opfylde, før det anses for afsluttet.

- [ ] Acceptkriterierne i ticketten er alle opfyldt og kan demonstreres.
- [ ] Koden er peer-gennemgået og godkendt af de påkrævede gennemgængere.
- [ ] Automatiserede tests er skrevet, består og er flettet sammen med ændringen.
- [ ] Koden er flettet ind i hovedlinjen og udrulles rent gennem pipelinen.
- [ ] Ingen kendte defekter af den aftalte alvorlighedstærskel er stadig åbne.
- [ ] Dokumentation, hjælpetekst og runbooks er opdateret.
- [ ] Observerbarhed er på plads: relevante logs, målinger og alarmer findes.
- [ ] Sikkerheds- og privatlivskonsekvenser er overvejet og adresseret.
- [ ] Tilgængelighedskrav til ændringen er opfyldt, hvor den er brugervendt.
- [ ] Feature flags er konfigureret, og udrulningsplanen er aftalt.
- [ ] Produktejeren eller interessenten har accepteret udfaldet.
- [ ] Opfølgende arbejde er fanget som sporede tickets, ikke efterladt implicit.

## Produktionslancering / go-live-parathed

Før en væsentlig ændring eller en ny tjeneste leveres til produktion.

- [ ] Udrulningsplanen er dokumenteret, inklusive trinvise eller canary-trin og succeskriterier.
- [ ] Tilbagerulningsplanen er dokumenteret, testet og kan udføres hurtigt.
- [ ] Kapacitets- og belastningstest viser, at systemet opfylder forventet og maksimal efterspørgsel.
- [ ] Overvågning, dashboards og alarmer er live og valideret før lancering.
- [ ] Vagtdækning er planlagt, og de ansvarlige kender systemet.
- [ ] Runbooks findes for de mest sandsynlige fejl- og driftsscenarier.
- [ ] Afhængigheder, integrationer og tredjeparter er bekræftet klar, og rategrænser er forstået.
- [ ] Sikkerhedsgennemgang og påkrævede godkendelser er fuldført.
- [ ] Datamigrering, hvis nogen, er testet ende-til-ende med en verificeret tilbagetrækning.
- [ ] Feature flags tillader at deaktivere ændringen uden en genudrulning.
- [ ] Juridiske, privatlivs- og compliancegodkendelser er indhentet, hvor det kræves.
- [ ] Kommunikationsplanen dækker interessenter, support og kunder.
- [ ] En go/no-go-beslutning træffes af navngivne ejere mod eksplicitte kriterier.

## Sikkerhedsgennemgang / tjekliste til trusselsmodel

Til vurdering af sikkerhedstilstanden for en ændring eller et system.

- [ ] Tillidsgrænser og dataflow er identificeret og dokumenteret.
- [ ] Autentificering håndhæves på hvert indgangspunkt, der kræver det.
- [ ] Autorisationstjek håndhæver least privilege for hver handling og ressource.
- [ ] Alt eksternt input valideres, og output kodes til sit mål.
- [ ] Hemmeligheder lagres i et administreret hvælv, aldrig i kode eller konfiguration, og kan roteres.
- [ ] Data er krypteret under transport og i hvile, som klassifikationen kræver.
- [ ] Afhængigheder scannes for kendte sårbarheder og holdes opdaterede.
- [ ] Risici for injektion, deserialisering og SSRF er afbødet for utroværdigt input.
- [ ] Sikkerhedsrelevante hændelser logges uden at registrere følsomme data.
- [ ] Rategrænser, kvoter og misbrugsbeskyttelse vogter eksponerede endepunkter.
- [ ] Fejlmeddelelser lækker ikke stakspor, interne forhold eller følsomme detaljer.
- [ ] Trusler identificeret via STRIDE eller lignende er registreret med afbødninger eller accepteret risiko.
- [ ] Sikkerhedstest (SAST, DAST eller penetrationstest) er planlagt eller fuldført.

## Tjekliste til privatliv og databeskyttelse (DPIA-stil)

Til behandling, der involverer personlige eller følsomme data.

- [ ] De indsamlede personoplysninger er opgjort, klassificeret og minimeret til det nødvendige.
- [ ] Det lovlige grundlag eller den hjemmel, der gælder for hvert behandlingsformål, er dokumenteret.
- [ ] Formålsbegrænsning håndhæves: data bruges kun til de angivne formål.
- [ ] Opbevaringsperioder er defineret, og sletning eller anonymisering er automatiseret.
- [ ] Registreredes rettigheder (indsigt, berigtigelse, sletning, dataportabilitet) kan opfyldes.
- [ ] Samtykke, hvor der støttes sig til det, er frit, specifikt og kan trækkes tilbage.
- [ ] Tredjeparter og databehandlere er bundet af tilstrækkelige databeskyttelsesvilkår.
- [ ] Overførsler på tværs af grænser har et passende juridisk overførselsgrundlag.
- [ ] Adgang til personoplysninger er begrænset, logget og gennemgået.
- [ ] Privatlivsrisici for enkeltpersoner er vurderet og afbødet eller eskaleret.
- [ ] Processer til opdagelse og anmeldelse af databrud er defineret.
- [ ] Valg om privatliv gennem design og som standard er dokumenteret for funktionen.
- [ ] Databeskyttelsesrådgiveren eller privatlivsgennemgængeren har godkendt, hvor det kræves.

## Tjekliste til tilgængelighed (WCAG)

Til brugervendte grænseflader, afstemt med WCAG-principperne.

- [ ] Alt indhold kan nås og betjenes alene med tastaturet.
- [ ] Fokusrækkefølgen er logisk, og en synlig fokusindikator er til stede.
- [ ] Tekstfarvekontrast opfylder målforholdet (typisk 4,5:1 for brødtekst).
- [ ] Billeder og ikke-tekstligt indhold har meningsfuld alternativ tekst.
- [ ] Formularfelter har tilknyttede labels og klare fejlmeddelelser.
- [ ] Overskrifter, landemærker og struktur er markeret semantisk.
- [ ] Interaktive komponenter eksponerer korrekt navn, rolle og tilstand til hjælpeteknologi.
- [ ] Indhold omflyder og forbliver brugbart ved 200 % zoom og på små skærme.
- [ ] Tidsgrænser kan justeres, og bevægelse eller automatisk afspillet indhold kan sættes på pause.
- [ ] Farve er ikke det eneste middel til at formidle information.
- [ ] Medier har undertekster og, hvor det er nødvendigt, transskriptioner eller lydbeskrivelse.
- [ ] Grænsefladen er testet med en skærmlæser og automatiseret tilgængelighedsværktøj.

## Tjekliste til API-designgennemgang

Før et API udgives eller ændres.

- [ ] Navngivning af ressourcer og operationer er konsekvent og forudsigelig.
- [ ] Kontrakten er specificeret i et maskinlæsbart skema (for eksempel OpenAPI).
- [ ] Versioneringsstrategien er defineret, og bagudkompatibilitet er bevaret eller styret.
- [ ] Paginering, filtrering og sortering følger ensartede konventioner.
- [ ] Fejlsvar bruger ensartet struktur, koder og handlingsbare meddelelser.
- [ ] Autentificering og autorisation er specificeret for hver operation.
- [ ] Inputvalidering og størrelsesgrænser er defineret og håndhævet.
- [ ] Idempotens er defineret for operationer, hvor genforsøg forventes.
- [ ] Rategrænser, kvoter og drosling er dokumenteret.
- [ ] Timeouts, genforsøg og fejlsemantik er klare for klienterne.
- [ ] Eksponering af følsomme data i svar er minimeret og begrundet.
- [ ] Dokumentationen indeholder eksempler for hver operation og fejlsituation.
- [ ] Udfasningspolitik og nedlukningstidslinjer er defineret.

## Tjekliste til gennemgang af arkitekturbeslutning (ADR)

Til gennemgang af et foreslået arkitekturbeslutningsregister.

- [ ] Konteksten og det problem, der løses, er angivet klart.
- [ ] Beslutningen er angivet entydigt som et enkelt valg.
- [ ] Mindst to realistiske alternativer blev overvejet og sammenlignet.
- [ ] Konsekvenser, både positive og negative, er dokumenteret.
- [ ] Ikke-funktionelle konsekvenser (ydeevne, sikkerhed, omkostning, driftsegnethed) er adresseret.
- [ ] Beslutningen stemmer overens med eksisterende principper og tidligere ADR'er eller afløser dem eksplicit.
- [ ] Berørte teams og interessenter blev hørt.
- [ ] Reversibilitet og omkostning ved ændring er vurderet.
- [ ] Antagelser og begrænsninger er gjort eksplicitte.
- [ ] Statussen (foreslået, accepteret, afløst) er sat og dateret.
- [ ] Beslutningen kan findes og er linket fra relevante systemer.
- [ ] Eventuelle opfølgende handlinger eller migreringer er fanget som sporet arbejde.

## Tjekliste til hændelsesrespons

Under en aktiv produktionshændelse.

- [ ] Erklær hændelsen, og udpeg en enkelt hændelsesleder.
- [ ] Vurdér og kommunikér alvorlighed, omfang og kundepåvirkning.
- [ ] Åbn en dedikeret kommunikationskanal og en hændelsesregistrering.
- [ ] Tildel klare roller: leder, kommunikationsansvarlig og driftsansvarlig.
- [ ] Prioritér afbødning og genoprettelse af tjenesten over rodårsagsanalyse.
- [ ] Giv regelmæssige statusopdateringer til interessenter efter en fast kadence.
- [ ] Fang en tidslinje over begivenheder, handlinger og beslutninger, mens de sker.
- [ ] Eskalér til yderligere ansvarlige eller leverandører, når det er nødvendigt.
- [ ] Underret jura, sikkerhed og compliance, hvis data eller regulering er involveret.
- [ ] Verificér rettelsen, og bekræft, at systemet er fuldt genoprettet.
- [ ] Luk hændelsen formelt, og kommunikér løsningen.
- [ ] Planlæg den skyldfrie postmortem, før folk spredes.

## Tjekliste til postmortem

Til den retrospektive gennemgang efter en hændelse.

- [ ] Gennemgangen er skyldfri og fokuserer på systemer og medvirkende faktorer.
- [ ] En faktuel, tidsstemplet tidslinje over hændelsen er dokumenteret.
- [ ] Kunde- og forretningspåvirkning er kvantificeret (varighed, omfang, omkostning).
- [ ] Detektion er analyseret: hvordan og hvornår problemet blev opdaget.
- [ ] Respons er analyseret: hvad der hjalp, og hvad der forsinkede genoprettelsen.
- [ ] Medvirkende årsager er identificeret, ikke blot én enkelt rodårsag.
- [ ] Hvad der gik godt, er registreret, såvel som hvad der gik galt.
- [ ] Handlingspunkter er specifikke, tildelt ejere og har forfaldsdatoer.
- [ ] Handlingspunkter adresserer forebyggelse, detektion og afbødning.
- [ ] Opfølgende punkter følges til afslutning i det normale efterslæb.
- [ ] Postmortemen deles bredt, så andre kan lære af den.
- [ ] Systemiske mønstre på tværs af hændelser gennemgås med jævne mellemrum.

## Tjekliste til vagtparathed

Før nogen tager et vagthold.

- [ ] Den ansvarlige har adgang til alle systemer, dashboards og værktøjer, de har brug for.
- [ ] Alarmering når den ansvarlige pålideligt og er testet.
- [ ] Eskaleringsstier og sekundære vagtkontakter er kendt og aktuelle.
- [ ] Runbooks findes for de mest almindelige og mest alvorlige alarmer.
- [ ] Den ansvarlige har gennemført onboarding eller skygning for disse systemer.
- [ ] Nylige ændringer, igangværende hændelser og kendte problemer er overdraget.
- [ ] Alarmtærskler er tunet til at minimere støj og falske paging.
- [ ] Den ansvarlige ved, hvordan man erklærer en hændelse og når lederen.
- [ ] Adgang til produktion er mulig fra den ansvarliges arbejdsmiljø.
- [ ] Kommunikationskanaler og interessentkontakter er dokumenteret.
- [ ] Vagtskemaet er offentliggjort, og dækningen har ingen huller.
- [ ] Kompensation, forventninger og arbejdsbyrdegrænser for vagt er klare.

## Tjekliste til SLO-definition

Når et servicemål (SLO) defineres.

- [ ] Den brugerrejse eller kapabilitet, SLO'en beskytter, er klart identificeret.
- [ ] Serviceindikatorer (SLI'er) er defineret som klare, målbare størrelser.
- [ ] SLI'er måles fra brugerens perspektiv, hvor det er muligt.
- [ ] Målet er sat til et niveau, brugerne faktisk har brug for, ikke 100 %.
- [ ] Måleperioden (for eksempel rullende 28 dage) er specificeret.
- [ ] Fejlbudgettet udledt af målet er beregnet og forstået.
- [ ] En politik definerer, hvad der sker, når fejlbudgettet er opbrugt.
- [ ] Datakilderne til SLI'erne er pålidelige og instrumenterede.
- [ ] Alarmering er knyttet til forbrændingsrate, ikke blot tærskelbrud.
- [ ] Ejere og interessenter er enige om, at SLO'en er realistisk og meningsfuld.
- [ ] SLO'en er dokumenteret og synlig på et dashboard.
- [ ] Der findes en plan for at gennemgå og revidere SLO'er, efterhånden som tjenesten udvikler sig.

## Tjekliste til CI/CD-pipeline

Til en kontinuerlig integrations- og leveringspipeline.

- [ ] Hver commit udløser et automatiseret build- og testløb.
- [ ] Pipelinen fejler hurtigt og rapporterer resultater klart til forfattere.
- [ ] Linting, formatering og statisk analyse kører automatisk.
- [ ] Enheds-, integrations- og relevante ende-til-ende-tests kører i pipelinen.
- [ ] Sikkerheds- og afhængighedsscanning kører ved hvert build.
- [ ] Buildartefakter er versionerede, uforanderlige og lagret i et register.
- [ ] Hemmeligheder injiceres sikkert og udskrives aldrig i logs.
- [ ] Udrulninger er automatiserede og gentagelige på tværs af miljøer.
- [ ] Udrulningsstrategien (canary, blue-green, rullende) er defineret og anvendt.
- [ ] Tilbagerulning er automatiseret eller en enkelt dokumenteret handling.
- [ ] Pipelinetilladelser følger least privilege og er revisionsbare.
- [ ] Pipelinekonfigurationen er lagret i versionsstyring som kode.
- [ ] Buildoprindelse og en software bill of materials produceres, hvor det kræves.

## Tjekliste til gennemgang af infrastruktur som kode

Til gennemgang af infrastruktur defineret som kode.

- [ ] Ændringer er udtrykt udelukkende i kode og anvendt gennem pipelinen.
- [ ] Et plan- eller tørkørselsoutput gennemgås før anvendelse.
- [ ] Tilstand lagres sikkert med låsning for at forhindre samtidige ændringer.
- [ ] Ressourcer følger konventioner for navngivning, mærkning og ejerskab.
- [ ] IAM-roller og -politikker med least privilege bruges, uden jokertegn, hvor det kan undgås.
- [ ] Netværkseksponering er minimeret; ingen utilsigtet offentlig adgang.
- [ ] Hemmeligheder og følsomme værdier refereres fra et hvælv, ikke hardkodet.
- [ ] Kryptering er aktiveret for lager, databaser og transport.
- [ ] Ændringer er idempotente og sikre at anvende igen.
- [ ] Sprængradius er forstået; destruktive ændringer er påpeget.
- [ ] Omkostningsvirkningen af ændringen er overvejet.
- [ ] Moduler er genbrugelige, versionerede og testede.
- [ ] Afdriftsdetektion er på plads for at fange ændringer uden om pipelinen.

## Tjekliste til release af AI/ML-model

Før en maskinlæringsmodel udgives til produktion.

- [ ] Modellens tilsigtede brug, omfang og begrænsninger er dokumenteret.
- [ ] Oprindelse, licensering og samtykke for trænings- og evalueringsdata er verificeret.
- [ ] Data og model er versionerede og reproducerbare.
- [ ] Ydeevne er evalueret på repræsentative, tilbageholdte testdata.
- [ ] Retfærdighed og bias er vurderet på tværs af relevante undergrupper.
- [ ] Modellen er evalueret mod den eksisterende eller en baseline.
- [ ] Fejlformer, grænsetilfælde og adfærd uden for fordelingen er forstået.
- [ ] Risici for sikkerhed, misbrug og skadeligt output er vurderet og afbødet.
- [ ] Overvågning af drift, datakvalitet og præstationsforringelse er på plads.
- [ ] En tilbagerulning eller fallback til en tidligere model eller regelbaseret sti findes.
- [ ] Menneskeligt tilsyn eller klagemulighed er sørget for ved afgørende beslutninger.
- [ ] Privatlivsgennemgang dækker træningsdata og inferensinput og -output.
- [ ] Et modelkort eller tilsvarende dokumentation er offentliggjort til interessenter.

## Tjekliste til datapipelinekvalitet

Til en datapipeline, der fodrer analyse eller produkter.

- [ ] Kildedataskemaer valideres, og skemaændringer opdages.
- [ ] Indlæsning håndterer sene, duplikerede og uordnede poster korrekt.
- [ ] Datakvalitetstjek (fuldstændighed, unikhed, intervaller) kører automatisk.
- [ ] Fejlede poster sættes i karantæne og vises, ikke droppes stille.
- [ ] Transformationer er testet med repræsentative input og input i grænsetilfælde.
- [ ] Pipelinen er idempotent og sikker at køre igen efter fejl.
- [ ] Friskhed og latens af output overvåges mod forventninger.
- [ ] Afstamning er dokumenteret, så forbrugere ved, hvor data kommer fra.
- [ ] Personlige og følsomme data er klassificeret, maskeret eller begrænset på passende vis.
- [ ] Efterfyldning og genbehandling er understøttet og dokumenteret.
- [ ] Alarmering underretter ejere om fejl og kvalitetsbrud.
- [ ] Opbevarings- og sletningspolitikker håndhæves på lagrede data.
- [ ] Downstream-forbrugere og SLA'er er dokumenteret.

## Tjekliste til open source-optag og licensgennemgang

Før en open source-komponent tages i brug.

- [ ] Komponentens licens er identificeret og står på den godkendte liste.
- [ ] Licensforpligtelser (tilskrivning, copyleft, meddelelser) er forstået og opfyldt.
- [ ] Licenskompatibilitet med jeres distributionsmodel er bekræftet.
- [ ] Projektet vedligeholdes aktivt og har et sundt fællesskab.
- [ ] Kendte sårbarheder er tjekket, og versionen er aktuel.
- [ ] Afhængigheden og dens transitive afhængigheder er opgjort.
- [ ] Sikkerhedstilstand og tidligere hændelseshistorik er gennemgået.
- [ ] Komponenten opfylder et reelt behov uden væsentlig duplikering.
- [ ] Udtrædelsesomkostning og udskiftelighed af komponenten er overvejet.
- [ ] Komponenten er registreret i software bill of materials.
- [ ] En navngiven ejer er ansvarlig for at følge opdateringer og sikkerhedsadvarsler.
- [ ] Politikker for bidrag tilbage og interne forks følges, hvis den er modificeret.

## Tjekliste til leverandør-/tredjepartsrisiko

Før en ekstern leverandør eller tjeneste onboardes.

- [ ] Forretningsbehovet og de data, leverandøren vil få adgang til, er klart defineret.
- [ ] Leverandørens sikkerhedstilstand er vurderet (certificeringer, revisioner, spørgeskema).
- [ ] Databehandlingsvilkår, ejerskab og sletning ved udtræden er kontraktligt klare.
- [ ] Leverandørens underdatabehandlere og datalokationer er oplyst og acceptable.
- [ ] Overholdelse af relevante reguleringer er verificeret.
- [ ] Oppetid, support og SLA-forpligtelser er dokumenteret.
- [ ] Forpligtelser og tidsfrister for anmeldelse af brud står i kontrakten.
- [ ] Adgang er afgrænset til least privilege og kan tilbagekaldes.
- [ ] Forretningskontinuitet og konsekvensen af leverandørsvigt er vurderet.
- [ ] En plan for udtræden og datamigrering findes for at undgå indlåsning.
- [ ] Omkostninger, fornyelsesvilkår og prisændringsklausuler er forstået.
- [ ] Leverandøren er tilføjet til risikoregistret med en gennemgangsdato.

## Tjekliste til offentlig compliance (ATO / FedRAMP-stil)

Til systemer, der kræver formel tilladelse til drift.

- [ ] Systemgrænsen og dataflowene er defineret og diagrammeret.
- [ ] Data er kategoriseret efter konsekvensniveau og følsomhed.
- [ ] Den gældende kontrolbaseline er valgt og tilpasset.
- [ ] En systemsikkerhedsplan dokumenterer, hvordan hver kontrol er implementeret.
- [ ] Kontroller er implementeret, dokumenteret og kortlagt til planen.
- [ ] Kontinuerlig overvågning og sårbarhedsscanning er i drift.
- [ ] En handlings- og milepælsplan følger åbne fund til afhjælpning.
- [ ] Adgangskontrol, revisionslogning og identitetsstyring opfylder kravene.
- [ ] Kryptering bruger godkendte algoritmer og validerede moduler.
- [ ] En hændelsesresponsplan er dokumenteret og testet.
- [ ] En beredskabs- og katastrofegenopretningsplan er dokumenteret og testet.
- [ ] En uafhængig vurdering eller revision af kontrollerne er gennemført.
- [ ] Den autoriserende embedsperson har den risikovurdering, der skal til for at give tilladelsen.
- [ ] Udløsere for gentilladelse og kadencen for løbende tilladelse er defineret.
