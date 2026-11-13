# 12.1 Ordliste

Denne ordliste definerer termer og akronymer, der bruges i hele guidebogen.
Opslagene er grupperet alfabetisk efter de engelske opslagsord, som er bevaret,
fordi de er de termer, I vil møde i værktøjer, standarder og litteratur. Hvor et
opslag har et almindeligt akronym, vises det i parentes. Definitionerne er med
vilje kortfattede; se det relevante kapitel for en fuldere behandling.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: En autorisationsmodel, der giver adgang på baggrund af evaluerede egenskaber ved brugeren, ressourcen, handlingen og omgivelserne (for eksempel afdeling, sikkerhedsgodkendelse, tidspunkt på dagen) frem for faste roller. Den giver finkornet, politikdrevet kontrol på bekostning af større kompleksitet end RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: Praksissen at designe og bygge software, så mennesker med handicap kan opfatte, forstå, navigere i og interagere med den. Numeronymet "a11y" forkorter de 11 bogstaver mellem "a" og "y".

**ADR (Architecture Decision Record)**: Et kort, versioneret dokument, der fastholder én enkelt væsentlig arkitektonisk eller teknisk beslutning, dens kontekst, de overvejede muligheder og dens konsekvenser. ADR'er skaber en varig, gennemgåelig historik over, hvorfor et system er, som det er.

**Aggregate**: I Domain-Driven Design en klynge af domæneobjekter, der behandles som én enhed ved dataændringer, hvor én entitet fungerer som aggregatroden, der håndhæver invarianter. Aggregater definerer konsistens- og transaktionsgrænser.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: En defineret kontrakt, hvorigennem et stykke software anmoder et andet om tjenester eller data. Veldesignede API'er skjuler implementeringsdetaljer og tilbyder stabile, versionerede grænseflader.

**API-first**: En udviklingstilgang, hvor API-kontrakten designes og aftales før implementeringen, så forbrugere og udbydere kan arbejde parallelt mod en fælles specifikation.

**arc42**: En åben, skabelonbaseret struktur til dokumentation af softwarearkitektur, organiseret i tolv afsnit, der dækker kontekst, begrænsninger, byggeklodser, kørselstid, udrulning og beslutninger.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: En W3C-specifikation, der definerer roller, tilstande og egenskaber, som gør dynamiske og tilpassede webkomponenter forståelige for hjælpeteknologier som skærmlæsere.

**ASR (Architecturally Significant Requirement)**: Et krav, der har en målbar, vidtrækkende effekt på arkitekturen, såsom en begrænsning vedrørende ydeevne, tilgængelighed, sikkerhed eller regulering. ASR'er driver de mest vidtrækkende designbeslutninger.

**ASVS (Application Security Verification Standard)**: En OWASP-standard, der giver en trinopdelt tjekliste over sikkerhedskrav og tests til at designe, bygge og verificere sikre applikationer.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**: Automatisk justering af antallet af kørende beregningsinstanser (eller deres størrelse) som svar på belastning, så kapaciteten følger efterspørgslen uden manuel indgriben. Det supplerer, men erstatter ikke, bevidst kapacitetsplanlægning.

**[Availability](https://en.wikipedia.org/wiki/Availability)**: Den andel af tiden, et system er i drift og i stand til at betjene forespørgsler, ofte udtrykt i "nier" (for eksempel 99,9 %). Det er et centralt pålidelighedsmål, der er kodificeret i SLO'er og SLA'er.

## B

**Backpressure**: En flowkontrolmekanisme, hvor en komponent under belastning signalerer til producenter opstrøms at sætte farten ned, hvilket forhindrer ubegrænsede køer og kaskadefejl. Den er central for pålidelige streaming- og meddelelsesdrevne systemer.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: En samarbejdsbaseret praksis, der udtrykker krav som konkrete, menneskelæsbare eksempler på adfærd (ofte i Given/When/Then-form), som tjener dobbelt som automatiserede accepttests.

**BFF (Backend for Frontend)**: Et arkitekturmønster, hvor en dedikeret backend-tjeneste bygges til en bestemt frontend eller klienttype og skræddersyer dataformning og aggregering til den klients behov.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: De værktøjer, processer og praksisser, der indsamler, integrerer og analyserer forretningsdata for at understøtte rapportering, dashboards og beslutningstagning.

**Blameless postmortem**: En hændelsesgennemgang, der fokuserer på systemiske årsager og læring frem for individuel skyld, ud fra den præmis, at folk handler fornuftigt med de oplysninger og incitamenter, de havde.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: En releasestrategi, der kører to identiske produktionsmiljøer ("blå" og "grøn"), router trafikken til det ene, mens det andet opdateres, og muliggør næsten øjeblikkelig omskiftning og tilbagerulning.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: En udbredt rangeringsfunktion til fuldtekstsøgning, der scorer, hvor godt et dokument matcher en forespørgsel, ved hjælp af termfrekvens, omvendt dokumentfrekvens og dokumentlængde. Den er standarden for leksikalsk rangering i mange søgemaskiner.

**Bounded context**: I Domain-Driven Design en eksplicit grænse, inden for hvilken en bestemt domænemodel og dens ubiquitous language gælder konsekvent. Den forhindrer, at begreber forveksles på tværs af forskellige dele af et stort system.

**Build cache**: Et lager af tidligere beregnede buildoutput, nøglet efter de inputs, der producerede dem, så uændret arbejde genbruges frem for at blive bygget igen. En delt fjernbuildcache lader et helt team og dets CI genbruge hinandens resultater.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: Det antal personer, der skulle mistes ("blive ramt af en bus", billedligt talt), før et projekt går i stå af mangel på væsentlig viden. En lav bus factor signalerer koncentreret, udokumenteret ekspertise og organisatorisk risiko.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: Den regel, en cache bruger til at afgøre, hvilken post der skal fjernes, når den er fuld, såsom least recently used (LRU) eller least frequently used (LFU). Politikken former trefprocenten og dermed cachens værdi.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**: Problemet med at fjerne eller opdatere cachelagrede data, når den underliggende kilde ændrer sig, så læsere ikke ser forældede værdier. Det er berygtet som et af de sværeste problemer i datalogi.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: En fejlform, hvor mange klienter misser cachen for den samme nøgle på én gang og alle rammer oprindelsen samtidig og overvælder den. Sammenlægning af forespørgsler og forskudt udløb forhindrer det. Kaldes også en thundering herd.

**Canary release**: En udrulningsteknik, der først eksponerer en ny version for en lille delmængde af brugere eller trafik, overvåger for problemer og derefter progressivt udvider udrulningen, hvis målingerne forbliver sunde.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: Et princip, der siger, at et distribueret datalager højst kan garantere to af Consistency, Availability og Partition tolerance samtidig; fordi partitioner er uundgåelige, afvejer designere i praksis konsistens mod tilgængelighed under dem.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**: En let tilgang til at visualisere softwarearkitektur på fire abstraktionsniveauer: System Context, Containers, Components og Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Continuous Delivery holder software i en releasebar tilstand, så den kan udrulles når som helst med en manuel godkendelse; Continuous Deployment udgiver automatisk hver ændring, der består pipelinen.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Et geografisk distribueret netværk af edge-servere, der cacher og leverer indhold tæt på brugerne, skærer latens og aflaster oprindelsesinfrastrukturen.

**Chain-of-thought prompting**: En prompting-teknik, der beder en sprogmodel gennemgå mellemliggende ræsonnementstrin, før den giver et endeligt svar, hvilket forbedrer ydeevnen på flertrinsproblemer på bekostning af længere, langsommere output.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: Praksissen med hyppigt at flette udvikleres ændringer ind i en fælles hovedlinje, hvor hver fletning valideres af et automatiseret build og en testsuite for at opdage integrationsproblemer tidligt.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Den kombinerede pipeline af Continuous Integration og Continuous Delivery/Deployment, der automatiserer bygning, test og udgivelse af software.

**CMMC (Cybersecurity Maturity Model Certification)**: Et program under det amerikanske forsvarsministerium, der certificerer cybersikkerhedsmodenheden hos entreprenører, der håndterer føderale kontraktoplysninger og kontrollerede ikke-klassificerede oplysninger.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Den grad, i hvilken elementerne inde i et modul hører sammen og tjener ét velafgrænset formål. Høj kohæsion, parret med lav kobling, er et kendetegn ved vedligeholdeligt design.

**Context window**: Den maksimale mængde tekst, målt i tokens, som en sprogmodel kan overveje på én gang, omfattende både input og output. Det er et knapt budget, som prompt- og kontekstdesign skal forvalte bevidst.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)**: Iagttagelsen af, at et systems struktur har tendens til at spejle kommunikationsstrukturen i den organisation, der bygger det. Det "omvendte Conway-manøvre" former bevidst teams for at producere en ønsket arkitektur.

**Core Web Vitals**: Et sæt brugercentrerede webydeevnemålinger defineret af Google (såsom Largest Contentful Paint, Interaction to Next Paint og Cumulative Layout Shift), der måler indlæsning, interaktivitet og visuel stabilitet.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)** (forsinkelsesomkostning): Den økonomiske omkostning ved, at noget endnu ikke er færdigt, udtrykt som værdi tabt pr. tidsenhed. At gøre den eksplicit forvandler prioritering fra mening til aritmetik og understøtter sekvenseringsregler som weighted shortest job first.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Graden af indbyrdes afhængighed mellem moduler eller tjenester. Løs kobling begrænser ringvirkningerne af ændringer og er et centralt mål for god arkitektur.

**CQRS (Command Query Responsibility Segregation)**: Et mønster, der adskiller den model, der bruges til at ændre tilstand (kommandoer), fra den model, der bruges til at læse tilstand (forespørgsler), så hver kan optimeres og skaleres uafhængigt.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Et offentligt katalog over offentliggjorte sikkerhedssårbarheder, hver tildelt en unik identifikator, så værktøjer og teams kan referere til samme fejl entydigt.

**CWV**: Se Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Sikkerhedstest, der undersøger en kørende applikation udefra, uden adgang til kildekode, for at finde sårbarheder, der viser sig under kørsel.

**Data-ink ratio**: Et princip fra Edward Tufte, der siger, at et diagram bør bruge det meste af sit blæk på selve dataene og lidt på pynt, og fjerne gitterlinjer, rammer og chartjunk, der ikke informerer.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: En decentraliseret dataarkitektur og driftsmodel, der behandler data som et produkt ejet af domæneteams, understøttet af selvbetjent platformsinfrastruktur og fødereret styring.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)** (datavisualisering): Praksissen at kode data i visuel form (position, længde, farve og lignende), så mønstre, sammenligninger og trends bliver synlige, og beslutninger bliver bedre informeret.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: En tilgang til softwaredesign, der centrerer modellen om forretningsdomænet ved hjælp af et fælles ubiquitous language, bounded contexts og byggeklodser som entiteter, værdiobjekter og aggregater.

**Design tokens**: Navngivne, platformsuafhængige værdier (farver, afstand, typografi og lignende), der koder designbeslutninger, så de kan deles konsekvent på tværs af et designsystem og flere produkter.

**DevEx / DevX (Developer Experience)**: Den overordnede kvalitet af en udviklers daglige samspil med værktøjer, platforme og processer, omfattende friktion, feedbackhastighed og kognitiv belastning.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: En kultur og et sæt praksisser, der forener softwareudvikling og drift for at forkorte leveringscyklusser, øge udrulningsfrekvensen og forbedre pålideligheden gennem automatisering og fælles ejerskab.

**DORA (DevOps Research and Assessment)**: Et forskningsprogram og dets fire udbredte leveringsmålinger (udrulningsfrekvens, ledetid for ændringer, ændringsfejlrate og tid til genoprettelse af tjenesten), der bruges til at benchmarke softwareleveringspræstation.

**DPIA (Data Protection Impact Assessment)**: En struktureret konsekvensanalyse, krævet under GDPR for højrisikobehandling, der identificerer og afbøder privatlivsrisici, før et projekt går videre.

**Drift (configuration)**: Den gradvise afvigelse af et systems faktiske tilstand fra dets erklærede eller tilsigtede tilstand, almindeligvis forårsaget af manuelle ændringer; Infrastructure as Code og GitOps sigter mod at opdage og rette det.

**Drift (model)**: I maskinlæring forringelsen af modelpræstation over tid, efterhånden som inputdataenes statistiske egenskaber (datadrift) eller det modellerede forhold (konceptdrift) ændrer sig.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: Strategien, procedurerne og infrastrukturen til at genoprette tjeneste og data efter en større forstyrrende begivenhed, typisk styret af RTO- og RPO-mål.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Et designprincip, der siger, at hver viden bør have én enkelt, autoritativ repræsentation, hvilket reducerer duplikering og risikoen for inkonsistente opdateringer.

## E

**East-west traffic**: Netværkstrafik mellem tjenester inde i et system eller datacenter, i modsætning til nord-syd-trafik mellem systemet og eksterne klienter. Et service mesh styrer typisk øst-vest-trafik.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**: At køre beregning og lagring tæt på, hvor data produceres eller forbruges, frem for på et centralt sted, for at skære latens og båndbredde. Content delivery networks er en tidlig, udbredt form.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: Et systems evne til automatisk at erhverve og frigive ressourcer som svar på skiftende efterspørgsel, så kapaciteten følger belastningen tæt.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Et dataintegrationsmønster, der først indlæser rådata i et målslager og transformerer dem dér, og udnytter skalaen i moderne lagre og lakehouses.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: En repræsentation af tekst, billeder eller andre data som en tæt numerisk vektor, placeret så ens poster ligger tæt sammen. Embeddings driver semantisk søgning og vektorsøgning samt retrieval-augmented generation.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Den europæiske standard, der specificerer tilgængelighedskrav til IKT-produkter og -tjenester, refereret af offentlige indkøb i hele EU og afstemt med WCAG.

**Error budget** (fejlbudget): Den tilladte mængde upålidelighed, en SLO tillader over en periode; når det er opbrugt, prioriterer teams pålidelighedsarbejde over nye funktioner. Det forener spændingen mellem velocity og stabilitet.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Et dataintegrationsmønster, der udtrækker data fra kilder, transformerer dem til en målform og indlæser dem i en destination som et lager.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Den Europæiske Unions forordning, der klassificerer AI-systemer efter risiko og pålægger forpligtelser i overensstemmelse hermed, forbyder visse anvendelser og regulerer højrisikosystemer kraftigt.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**: En konsistensmodel i distribuerede systemer, hvor replikaer midlertidigt kan afvige, men konvergerer til samme tilstand, når opdateringer holder op med at udbrede sig.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: En mekanisme til at aktivere eller deaktivere funktionalitet under kørsel uden genudrulning, brugt til gradvis udrulning, eksperimentering og operationel kontrol.

**Feature store**: Et centraliseret system til at definere, lagre og levere kuraterede maskinlæringsfeatures konsistent til både træning og inferens, hvilket reducerer duplikering og afvigelse mellem træning og serving.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Et amerikansk regeringsprogram, der standardiserer sikkerhedsvurdering, autorisation og kontinuerlig overvågning af cloudtjenester brugt af føderale agenturer.

**Few-shot prompting**: At give en sprogmodel en håndfuld udarbejdede eksempler i prompten for at demonstrere den ønskede opgave og outputformat, i modsætning til zero-shot prompting, som giver instruktioner uden eksempler.

**FinOps**: En disciplin og kulturel praksis, der bringer økonomisk ansvarlighed til variable cloududgifter og giver ingeniør-, økonomi- og forretningsteams fælles ejerskab af omkostning og værdi.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Amerikansk lovgivning, der kræver, at føderale agenturer implementerer, dokumenterer og overvåger informationssikkerhedsprogrammer, i vid udstrækning operationaliseret gennem NIST-vejledning.

**Flow efficiency** (flowevne): Den andel af den samlede ledetid, et arbejdspunkt bruger på at blive aktivt arbejdet på frem for at vente, beregnet som værdiskabende tid divideret med samlet ledetid. De fleste systemer er overraskende lave, ofte under 15 procent.

**Four-eyes principle**: En kontrol, der kræver, at en væsentlig handling gennemgås eller godkendes af mindst to personer, hvilket reducerer risikoen for fejl eller misbrug.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: En automatiseret testteknik, der fodrer et program med misdannede, tilfældige eller uventede input for at afdække nedbrud, sikkerhedsfejl og defekter i grænsetilfælde.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Den Europæiske Unions forordning om behandling af personoplysninger, der giver enkeltpersoner rettigheder og pålægger dataansvarlige og databehandlere forpligtelser, med betydelige sanktioner for manglende overholdelse.

**GitOps**: En driftsmodel, der bruger Git som den enkelte kilde til sandhed for deklarativ infrastruktur og applikationer, hvor automatisering kontinuerligt afstemmer det levende system til den committede tilstand.

**Golden path / paved road** (asfalteret vej): En velunderstøttet, meningstung standardmåde at bygge og levere software på inden for en organisation, designet til at gøre det sikre, compliante og pålidelige valg til det letteste.

**Golden record**: I master data management den enkelte, afstemte, autoritative version af en forretningsentitet (såsom en kunde), samlet fra flere kildesystemer gennem matchnings- og overlevelsesregler.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)**: En tilgang til typesystemer, der lader statisk og dynamisk typning sameksistere i én kodebase, så typer kan tilføjes trinvis til et dynamisk typet program. Typehints og valgfrie typecheckere er almindelige eksempler.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Et forespørgselssprog og en runtime til API'er, der lader klienter anmode om præcis de data, de har brug for, i ét enkelt kald, ved hjælp af et stærkt typet skema.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Et højtydende, kontraktførst remote procedure call-rammeværk, der bruger HTTP/2 og typisk Protocol Buffers til effektiv kommunikation mellem tjenester.

## H

**Hermetic build**: Et build, der kun afhænger af eksplicit deklarerede input og er isoleret fra værtsmiljøet, så det producerer det samme output overalt. Hermetiskhed er fundamentet for reproducerbare builds og pålidelig caching.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: En manipulationssikret hardwareenhed, der genererer, lagrer og bruger kryptografiske nøgler og giver stærkere nøglebeskyttelse end rene softwaretilgange.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Amerikansk lovgivning, der blandt andet fastsætter krav til beskyttelse af beskyttede sundhedsoplysninger (PHI) og styrer deres brug og videregivelse.

**Horizontal scaling**: At øge kapaciteten ved at tilføje flere instanser eller noder ("scale out") frem for at gøre en enkelt node mere kraftfuld. Det understøtter de fleste storskala, robuste arkitekturer.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Praksissen at definere og provisionere infrastruktur gennem maskinlæsbar, versionsstyret konfiguration frem for manuelle processer, hvilket muliggør gentagelighed og gennemgang.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: Rammeværket af politikker og teknologier, der sikrer, at de rette identiteter har den rette adgang til de rette ressourcer på de rette tidspunkter.

**IDP / IdP**: "IDP" betegner almindeligvis en Internal Developer Platform, det selvbetjente værktøjslag, der abstraherer infrastruktur for produktteams; "IdP" betegner en Identity Provider, en tjeneste der autentificerer brugere og udsteder påstande. Konteksten afgør, hvilken af de to der menes.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**: En egenskab, hvor en operation udført flere gange har samme effekt som udført én gang, afgørende for sikre genforsøg i distribuerede systemer og API'er.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: At designe og bygge software, så den kan tilpasses forskellige sprog, regioner og kulturelle konventioner uden ingeniørmæssige ændringer. Numeronymet forkorter de 18 bogstaver mellem "i" og "n".

**Immutable artefact**: Et buildoutput, der, når det først er produceret og versioneret, aldrig ændres; enhver ændring giver en ny version. Uforanderlighed gør releases reproducerbare og lader jer bygge én gang og promovere det samme artefakt på tværs af miljøer.

**InnerSource**: Anvendelsen af open source-udviklingspraksisser (gennemsigtighed, fælles repositories og bidrag på tværs af teams) inde i en enkelt organisation.

**IaC drift**: Se Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)**: En søgemaskines kerne-datastruktur, der kortlægger hver term til listen over dokumenter, der indeholder den, så forespørgsler kan besvares uden at gennemsøge hvert dokument.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: En international standard, der specificerer krav til et informationssikkerhedsledelsessystem (ISMS) og giver et certificerbart rammeværk til at styre informationssikkerhedsrisiko.

**ISO/IEC 42001**: En international standard, der specificerer krav til et AI-ledelsessystem og giver organisationer et certificerbart rammeværk til ansvarlig styring af udvikling og brug af AI.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Et kompakt, signeret (og eventuelt krypteret) tokenformat, der bruges til at overføre påstande mellem parter, almindeligvis til autentificering og autorisation i web- og API-systemer.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: En lean arbejdsgangsmetode, der visualiserer arbejde på en tavle, begrænser igangværende arbejde og styrer flow for at forbedre gennemløb og forudsigelighed.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Et designprincip, der foretrækker den simpleste løsning, der opfylder behovet, med den begrundelse, at unødvendig kompleksitet øger omkostning og risiko.

**KMS (Key Management Service)**: Et system til at oprette, lagre, rotere og kontrollere adgang til kryptografiske nøgler, ofte understøttet af hardware security modules.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: Et kvantificerbart mål, der bruges til at følge fremskridt mod et specifikt forretnings- eller driftsmål.

## L

**Lakehouse**: En dataarkitektur, der kombinerer det billige, fleksible lager i en data lake med styrings-, transaktions- og ydeevnefunktionerne i et datavarehus.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)** (ledetid): Den forløbne tid fra en ændring anmodes (eller committes) til den er leveret i produktion; en central DORA-leveringsmåling.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Et sikkerhedsprincip, der giver hver bruger, proces eller hvert system kun den minimale adgang, der kræves for at udføre dets funktion, og begrænser skaden fra kompromittering eller fejl.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)** (Littles lov): Et resultat fra køteori, der siger, at det gennemsnitlige antal poster i et stabilt system er lig den gennemsnitlige ankomstrate gange den gennemsnitlige tid, hver post bruger i systemet. Den forbinder igangværende arbejde, gennemløb og ledetid.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: En maskinlæringsmodel trænet på meget store tekstkorpora til at forudsige og generere sprog, i stand til opgaver som opsummering, oversættelse og kodegenerering.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)**: At tilpasse internationaliseret software til en bestemt lokalitet, inklusive oversættelse, formatering og kulturelle konventioner. Numeronymet forkorter de 10 bogstaver mellem "l" og "n".

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: Disciplinen og værktøjerne til at skabe og vedligeholde et enkelt, autoritativt, konsistent billede af centrale forretningsentiteter (såsom kunder eller produkter) på tværs af systemer.

**MITRE ATT&CK**: En kurateret, offentlig vidensbase over reelle modstandertaktikker og -teknikker, udbredt til at planlægge red team-øvelser, vejlede detektionsudvikling og beskrive trusler i et fælles ordforråd.

**Mean Time to Recovery (MTTR)**: Den gennemsnitlige tid, det tager at genoprette tjenesten efter en fejl; en almindelig pålideligheds- og hændelsesstyringsmåling.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: En praksis, hvor et helt team arbejder sammen på den samme opgave ved den samme computer og skiftes til at skrive, for at dele viden og træffe beslutninger kollektivt.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: Det sæt praksisser, der pålideligt og effektivt udruller, overvåger og vedligeholder maskinlæringsmodeller i produktion og udvider DevOps-principper til ML-livscyklussen.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Et enkelt versionsstyringsrepository, der rummer koden for mange projekter eller hele organisationen, og muliggør fælles værktøj og atomare ændringer på tværs af projekter på bekostning af specialiseret skaleringsværktøj.

**mTLS (mutual TLS)**: En konfiguration af Transport Layer Security, hvor begge parter fremviser og verificerer certifikater, så hver autentificerer den anden. Det er en standard for trafik mellem tjenester i et service mesh og zero trust-netværk. Se også [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**: En teknik, der bevidst indfører små fejl ("mutanter") i kode for at tjekke, om testsuiten opdager dem, og måler suitens reelle effektivitet.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: En rangeringskvalitetsmåling, der belønner at placere højt relevante resultater nær toppen af en resultatliste, normaliseret så scorer kan sammenlignes på tværs af forespørgsler. Den er en fast bestanddel af evaluering af søgerelevans.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Et amerikansk føderalt agentur, hvis Special Publications og rammeværker er vidt refererede standarder for cybersikkerhed, privatliv og AI.

**NIST AI RMF (AI Risk Management Framework)**: Et frivilligt NIST-rammeværk til at identificere, vurdere og styre risici forbundet med AI-systemer gennem hele deres livscyklus, organiseret omkring funktionerne Govern, Map, Measure og Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Et NIST-katalog over sikkerheds- og privatlivskontroller til føderale informationssystemer, udbredt som baseline langt ud over det offentlige.

**NIST SP 800-171**: En NIST-publikation, der specificerer krav til beskyttelse af kontrollerede ikke-klassificerede oplysninger (CUI) i ikke-føderale systemer, central for forsvarsentreprenørers compliance.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Et krav, der beskriver, hvordan et system skal opføre sig (dets egenskaber som ydeevne, sikkerhed, pålidelighed eller brugervenlighed) frem for hvilke funktioner det udfører.

**North-south traffic**: Netværkstrafik mellem et system og dets eksterne klienter (ind og ud af datacentret eller klyngen), i modsætning til øst-vest-trafik mellem interne tjenester. En API-gateway styrer typisk nord-syd-trafik.

## O

**Observability** (observerbarhed): Den grad, i hvilken et systems indre tilstand kan udledes af dets eksterne output, typisk opnået gennem telemetri: målinger, logs og traces.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Et målsætningsrammeværk, der parrer et kvalitativt mål med nogle få målbare nøgleresultater for at afstemme og fokusere en organisation.

**OpenTelemetry (OTel)**: En leverandørneutral, åben standard og værktøjssæt til at generere, indsamle og eksportere telemetridata (traces, målinger og logs) fra software.

**OPA (Open Policy Agent)**: En open source-politikmotor til generelle formål, der evaluerer politikker (skrevet i sproget Rego) for at håndhæve autorisations- og konfigurationsregler på tværs af stakken og muliggør policy as code.

**OSPO (Open Source Program Office)**: En organisatorisk funktion, der koordinerer open source-strategi, styring, compliance og fællesskabsengagement og styrer både forbrug og bidrag.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Et nonprofit-fællesskab, der producerer udbredte, frit tilgængelige applikationssikkerhedsressourcer, herunder OWASP Top Ten og ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: En udvidelse af CAP-teoremet, der siger, at hvis der er en Partition, afvejer et system Availability mod Consistency, Else (i normal drift) afvejer det Latency mod Consistency.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: En sikkerhedsstandard vedligeholdt af betalingskortbranchen, der specificerer krav til organisationer, der lagrer, behandler eller transmitterer kortindehaverdata.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)**: Et autoriseret, simuleret angreb på et system udført af dygtige testere for at finde og demonstrere udnyttelige sårbarheder, før rigtige angribere gør det, leveret som prioriterede, handlingsbare fund.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Oplysninger, der kan identificere en bestemt person, enten alene eller kombineret med andre data; deres håndtering er styret af privatlivslove og intern politik.

**Platform engineering**: Disciplinen at bygge og drive interne selvbetjente platforme og golden paths, der reducerer kognitiv belastning og accelererer produktteams.

**POUR**: De fire vejledende principper i Web Content Accessibility Guidelines: indhold skal være Perceivable, Operable, Understandable og Robust.

**Production readiness review**: Et struktureret tjek, kørt før en tjeneste går live eller overtager vagtejerskab, der bekræfter, at den opfylder standarder for observerbarhed, pålidelighed, sikkerhed, runbooks og driftsstøtte.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**: Praksissen at designe og forfine de instruktioner, den kontekst og de eksempler, en sprogmodel får, for at opnå pålideligt output af høj kvalitet, behandlet som en versioneret, testet ingeniørdisciplin frem for forsøg og fejl.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Et angreb, hvor udformet input får en sprogmodel til at ignorere sine tilsigtede instruktioner og følge angriberens i stedet, AI-æraens modstykke til injektionsfejl. Det er en central sikkerhedsrisiko for LLM-applikationer.

**Property-based testing**: En testteknik, der tjekker, at angivne egenskaber holder på tværs af mange automatisk genererede input, frem for kun at støtte sig til håndvalgte eksempler.

**Pull request (PR) / merge request (MR)**: Et foreslået sæt ændringer indsendt til gennemgang og diskussion, før det flettes ind i en fælles gren, den primære enhed for kodegennemgang i de fleste arbejdsgange.

**Purple team**: En samarbejdsøvelse, hvor offensive (røde) og defensive (blå) sikkerhedsteams arbejder sammen i realtid, så angreb og de detektioner, der skal fange dem, tunes mod hinanden.

## Q

**Quality gate** (kvalitetsport): Et automatiseret kontrolpunkt i en pipeline, der skal bestås (for eksempel opfyldelse af dækning, sikkerhed eller ydeevnetærskler), før en ændring kan gå videre.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: I distribuerede systemer det mindste antal noder, der skal være enige, for at en operation (såsom en læsning eller skrivning) anses for vellykket, brugt til at bevare konsistens trods fejl.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: En ansvarsfordelingsmodel, der mærker hver deltager i en opgave eller beslutning som Responsible, Accountable, Consulted eller Informed.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: En teknik, der forankrer en sprogmodels output ved først at hente relevante dokumenter eller data og levere dem som kontekst, hvilket forbedrer nøjagtigheden og reducerer hallucination.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: En autorisationsmodel, der tildeler rettigheder til roller og roller til brugere og forenkler administration ved at styre adgang på rolleniveau.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: En gruppe, der efterligner en realistisk modstander, ofte mod en hel organisation og uden varsel til forsvarerne, for at teste detektion og respons frem for blot at opregne sårbarheder. Modsat et blåt (defensivt) team.

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)**: Kontrollerede, langsomt skiftende kodelister og klassifikationer brugt til at kategorisere andre data, såsom landekoder, valutaer og statusværdier. At styre det som et fælles, versioneret ordforråd holder systemer konsistente.

**Rego**: Det deklarative politiksprog, Open Policy Agent bruger til at udtrykke regler for autorisations- og konfigurationsbeslutninger.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: En arkitekturstil for netværksapplikationer, der bruger tilstandsløse operationer over HTTP på adresserbare ressourcer, værdsat for enkelhed og bredt værktøj.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**: En server, der sidder foran en eller flere backend-tjenester og videresender klientforespørgsler til dem, og almindeligvis tilbyder TLS-terminering, belastningsfordeling, caching og et enkelt indgangspunkt.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Et skriftligt forslag, cirkuleret til feedback før en væsentlig teknisk beslutning eller ændring, der fremmer gennemsigtighed og fælles ejerskab. (Termen betegner også internetstandarddokumentserien.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: Et mål for den værdi, der opnås ved en investering, i forhold til dens omkostning, brugt til at retfærdiggøre og prioritere ingeniør- og teknologibeslutninger.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: Software-"robotter", der automatiserer gentagne, regelbaserede opgaver ved at interagere med eksisterende brugerflader og systemer, som en person ville.

**RPO (Recovery Point Objective)**: Den maksimalt acceptable mængde datatab målt i tid (for eksempel "op til fem minutter"), som definerer, hvor hyppigt data skal beskyttes.

**RTO (Recovery Time Objective)**: Den maksimalt acceptable varighed for at genoprette en tjeneste efter en forstyrrelse, der vejleder design af og investering i katastrofegenopretning.

## S

**Saga**: Et mønster til at styre datakonsistens på tværs af tjenester i en distribueret transaktion ved at sekvensere lokale transaktioner og udstede kompenserende handlinger, når et trin fejler.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Et rammeværk til at anvende agile og lean praksisser på tværs af store virksomheder og koordinere mange teams; værdsat for struktur og kritiseret for potentiel tyngde.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Sikkerhedstest, der analyserer kildekode, bytekode eller binære filer uden at udføre dem for at finde sårbarheder tidligt i udviklingen.

**SBOM (Software Bill of Materials)**: En formel, maskinlæsbar fortegnelse over komponenterne og afhængighederne i et stykke software, brugt til at styre forsyningskæde- og sårbarhedsrisiko.

**SCA (Software Composition Analysis)**: Værktøj, der identificerer open source- og tredjepartskomponenter i en kodebase og flagger kendte sårbarheder og licensrisici.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Et agilt rammeværk, der organiserer arbejde i iterationer af fast længde (sprints) med definerede roller, begivenheder og artefakter for at levere værditilvækst.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: En amerikansk lov, der kræver, at føderale agenturer gør deres elektroniske og informationsteknologi tilgængelig for mennesker med handicap, i praksis afstemt med WCAG.

**Semantic search**: Søgning, der matcher på mening frem for eksakte nøgleord, typisk ved at sammenligne embeddings af forespørgslen og dokumenterne. Den kombineres ofte med leksikalsk søgning i en hybrid tilgang.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Et dedikeret infrastrukturlag, normalt implementeret med sidecar-proxyer, der håndterer kommunikationsproblemer mellem tjenester såsom mutual TLS, genforsøg, timeouts, trafikskift og observerbarhed og holder dem ude af applikationskoden.

**Sidecar**: En hjælpeproces eller -container udrullet ved siden af en hovedapplikationsinstans for at levere understøttende kapabiliteter (såsom en service mesh-proxy) uden at ændre selve applikationen.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Et system, der aggregerer og korrelerer sikkerhedslogs og hændelser på tværs af et miljø for at muliggøre detektion, alarmering og efterforskning.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: En formel forpligtelse mellem en tjenesteudbyder og dens kunder, der specificerer forventede serviceniveauer og konsekvenserne af at misse dem.

**SLI (Service Level Indicator)**: Et kvantitativt mål for et aspekt af servicekvalitet, såsom forespørgselslatens eller fejlrate, der fodrer SLO'er.

**SLO (Service Level Objective)**: En målværdi eller et interval for en SLI, der definerer det ønskede pålidelighedsniveau og danner grundlag for fejlbudgetter.

**SLSA (Supply-chain Levels for Software Artifacts)**: Et rammeværk af trinvise sikkerhedskrav til at forbedre integriteten og oprindelsen af softwareartefakter gennem bygge- og releaseprocessen.

**SOAR (Security Orchestration, Automation, and Response)**: Værktøjer og praksisser, der automatiserer og koordinerer sikkerhedsdrift, såsom triage- og responsplaybooks, for at forbedre fart og ensartethed.

**SOC 2 (System and Organisation Controls 2)**: Et revisionsrammeværk og en rapport, baseret på AICPA's Trust Services Criteria, der vurderer en serviceorganisations kontroller for sikkerhed, tilgængelighed, behandlingsintegritet, fortrolighed og privatliv.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Fem objektorienterede designprincipper (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation og Dependency Inversion), der fremmer vedligeholdelig, fleksibel kode.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Amerikansk lovgivning, der fastsætter krav til finansiel rapportering og interne kontroller i børsnoterede virksomheder, med konsekvenser for de it-systemer, der understøtter finansielle data.

**SPACE**: Et rammeværk til at måle udviklerproduktivitet på tværs af fem dimensioner: Satisfaction and well-being, Performance, Activity, Communication and collaboration og Efficiency and flow, der advarer mod enkeltmålinger.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: En disciplin, der anvender softwareudviklingstilgange på drift og bruger SLO'er, fejlbudgetter og automatisering til at drive pålidelige systemer i skala.

**SSDF (Secure Software Development Framework)**: NIST's rammeværk (SP 800-218) af højniveau sikre udviklingspraksisser, der spænder over at forberede organisationen, beskytte software, producere velsikret software og reagere på sårbarheder.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)**: At undersøge kildekode, bytekode eller binære filer uden at udføre dem for at finde defekter, stilbrud og sikkerhedsfejl, typisk gennem linters, typecheckere og dedikerede analysatorer koblet ind i editoren og pipelinen.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: En trusselsmodelleringstaksonomi, der kategoriserer trusler som Spoofing, Tampering, Repudiation, Information disclosure, Denial of service og Elevation of privilege.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (samlet ejeromkostning): Den fulde livstidsomkostning for et system eller en beslutning, inklusive anskaffelse, drift, vedligeholdelse og eventuel udfasning, ikke blot den oprindelige pris.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: En praksis, hvor man skriver en fejlende automatiseret test før den kode, der får den til at bestå, og så refaktorerer, i korte gentagne cyklusser for at drive design og sikre dækning.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)** (teknisk gæld): Den underforståede fremtidige omkostning ved at vælge en hurtig løsning nu frem for en bedre, der ville tage længere tid, og som skal styres bevidst frem for at blive ophobet ubevidst.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Et klassisk vægtningsskema, der scorer en terms betydning for et dokument efter, hvor ofte den optræder dér, modregnet hvor almindelig den er i hele korpuset. Det ligger til grund for meget leksikalsk søgerangering.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)** (begrænsningsteori): En ledelsestilgang, der hævder, at et systems gennemløb til enhver tid begrænses af en enkelt flaskehals, så forbedringsindsats bør fokusere på den begrænsning, til den flytter sig andetsteds.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)** (trusselsmodellering): En struktureret praksis til at identificere, opregne og prioritere potentielle trusler mod et system, så forsvar kan designes ind tidligt.

**Toil**: I SRE manuelt, gentaget, automatiserbart driftsarbejde, der skalerer lineært med en tjeneste og ikke giver varig værdi; at reducere det frigør kapacitet til ingeniørarbejde.

**Trunk-based development**: En kildekontrolpraksis, hvor udviklere hyppigt integrerer små ændringer i en enkelt fælles gren og minimerer langlivede grene og flettesmerter.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)**: En sprogfunktion, der automatisk udleder typerne af udtryk og giver meget af statisk typnings sikkerhed uden at kræve, at hver type skrives ud i hånden.

**[Type system](https://en.wikipedia.org/wiki/Type_system)**: Det sæt regler, et sprog bruger til at tildele og kontrollere typer, som fanger hele klasser af fejl, før programmet kører, og dokumenterer hensigt. Typesystemer spænder fra dynamiske til statiske og fra svage til stærke.

## U

**Ubiquitous language**: I Domain-Driven Design et fælles, præcist ordforråd, der bruges konsekvent af udviklere og domæneeksperter og afspejles direkte i koden og modellerne.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Test udført af slutbrugere eller deres repræsentanter for at bekræfte, at et system opfylder forretningsbehov, før det accepteres til release.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: User Experience er den overordnede kvalitet af en persons samspil med et produkt; User Interface er den specifikke visuelle og interaktive overflade, hvorigennem samspillet foregår.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**: I Domain-Driven Design et uforanderligt objekt, der udelukkende er defineret ved sine egenskaber frem for en særskilt identitet, såsom et pengebeløb eller et datointerval.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)** (værdistrømskortlægning): En teknik til at tegne hvert trin fra idé til leveret værdi og skelne værdiskabende tid fra ventetid, så flaskehalse, overdragelser og omarbejdsløkker bliver synlige og kan forbedres.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)**: Et datalager optimeret til at indeksere og søge i højdimensionelle embeddingvektorer efter lighed, en almindelig rygrad i semantisk søgning og retrieval-augmented generation.

**Vertical scaling**: At øge kapaciteten ved at gøre en enkelt node mere kraftfuld ("scale up"), hvilket er enkelt, men i sidste ende begrænset af den største tilgængelige maskine.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Et værktøj, såsom Git, der registrerer ændringer i filer over tid, så historikken kan gennemgås, grene kan vedligeholdes og arbejde kan koordineres.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Automatiseret inspektion af systemer, containere eller kode mod databaser over kendte svagheder og fejlkonfigurationer. Det er bredt og billigt og supplerer dybden i manuel penetrationstest.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Et W3C-sæt internationalt anerkendte retningslinjer, organiseret omkring POUR-principperne og konformitetsniveauerne A, AA og AAA, for at gøre webindhold tilgængeligt.

**Wardley map**: En visuel strategiteknik, der placerer kapabiliteter efter deres værdi for brugerne og deres evolutionære modenhed, for at informere bygge/købe- og investeringsbeslutninger.

**Work in progress (WIP) limit**: Et loft over, hvor mange poster der må være i et givent trin af en arbejdsgang ad gangen, en central Kanban-praksis, der forbedrer flow ved at blotlægge flaskehalse og dæmpe overheadet ved for meget parallelt arbejde.

**WSJF (Weighted Shortest Job First)**: En prioriteringsmetode, der sekvenserer arbejde ved at dividere dets forsinkelsesomkostning med dets estimerede varighed, så de korteste, mest tidsfølsomme poster med højest værdi gøres først.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: En websårbarhed, hvor en angriber injicerer ondsindede scripts, der udføres i andre brugeres browsere og potentielt stjæler data eller kaprer sessioner.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Et princip, der fraråder at bygge funktionalitet på spekulation, med den begrundelse, at forventede behov ofte ikke materialiserer sig og tilføjer omkostning og kompleksitet.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: En sikkerhedsmodel, der ikke antager nogen implicit tillid baseret på netværksplacering og kontinuerligt verificerer hver adgangsanmodning mod identitet, enhed og kontekst, efter devisen "stol aldrig, verificér altid."
