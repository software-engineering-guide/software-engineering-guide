# 8.1 CI/CD en oplevering

## Overzicht en motivatie

[Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) en [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) zijn het bindweefsel tussen code schrijven en haar veilig voor gebruikers brengen. Continuous integration betekent dat elke wijziging vaak in een gedeelde hoofdlijn wordt samengevoegd en dan automatisch wordt gebouwd en getest, zodat integratieproblemen binnen minuten opduiken in plaats van aan het eind van een lange releasecyclus. Continuous delivery betekent dat elke wijziging die de pijplijn passeert inzetbaar blijft, zodat uitbrengen naar productie een bedrijfsbeslissing wordt in plaats van een engineeringhaast. [Continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) gaat een stap verder en brengt elke slagende wijziging automatisch uit, zonder menselijke poort.

Voor grote teams doen deze onderscheiden er enorm toe. Wanneer honderden engineers committen aan overlappende systemen, groeien de kosten van handmatige integratie en handmatig testen niet-lineair. Een gedeelde, geautomatiseerde pijplijn is de enige praktische manier om veel bijdragers snelle, betrouwbare feedback te geven en te voorkomen dat de wijziging van het ene team stilletjes die van een ander breekt. De pijplijn wordt de enige bron van waarheid over of de software gezond is, en dwingt een consistentie af die geen hoeveelheid documentatie of goede bedoelingen op schaal kan garanderen.

Contexten van onderneming en overheid voegen nog een dimensie toe: controleerbaarheid en wijzigingsbeheer. Toezichthouders, beveiligingsfunctionarissen en auditors hebben bewijs nodig dat wijzigingen zijn beoordeeld, getest en goedgekeurd, en dat het artefact dat in productie draait precies degene is die is gebouwd en gecontroleerd. Een goed ontworpen CI/CD-pijplijn verandert deze complianceverplichtingen van papierlast in een automatisch bijproduct van de normale engineeringworkflow. Goed gedaan wordt oplevering tegelijk sneller en veiliger, wat de uitkomst is die voor leiderschap het meest telt.

*Zie ook:* hoofdstuk 8.4 (platform engineering en developer experience), hoofdstuk 8.5 (test- en procesautomatisering) en hoofdstuk 7.4 (productanalytics en experimenteren) voor de praktijken van [feature flags](https://en.wikipedia.org/wiki/Feature_toggle) (runtimeschakelaars die functionaliteit aan gebruikers blootstellen zonder opnieuw te deployen) en experimenteren die progressieve oplevering (een wijziging geleidelijk uitbrengen terwijl haar gezondheidsstatistieken automatisch worden bewaakt) mogelijk maakt.

## Kernprincipes

- Integreer kleine wijzigingen vaak. Langlevende branches zijn de vijand van continuous integration.
- Bouw het artefact eenmaal en promoveer het identieke artefact door elke omgeving.
- Maak de pijplijn de gezaghebbende poort: als ze groen is, is de wijziging inzetbaar. Als ze rood is, stopt het werk tot het is gerepareerd.
- Optimaliseer meedogenloos voor snelle feedback zodat ontwikkelaars in flow blijven en defecten worden gevangen terwijl de context vers is.
- Automatiseer alles wat herhaald wordt, inclusief tests, beveiligingsscans, provisioning en deployment.
- Behandel pijplijndefinities als geversioneerde code onder review, niet als klikbare consoleconfiguratie.
- Ontwerp voor veilige, omkeerbare releases zodat elke deployment snel ongedaan kan worden gemaakt.
- Scheid deployment (de code installeren) van release (haar aan gebruikers blootstellen) met feature flags.

## Aanbevelingen

### Ontwerp de pijplijn als reeks kwaliteitspoorten

Structureer de pijplijn in fasen die van goedkoop en snel naar duur en grondig vorderen: eerst compileren en unittests, dan integratietests, beveiligings- en licentiescans en ten slotte deployment naar staging en productie. Elke fase is een poort die een wijziging moet passeren. Orden de poorten zodat de snelste, meest waarschijnlijk falende controles eerst draaien, wat ontwikkelaars de feedback in de kortst mogelijke tijd geeft. Houd de feedbacklus van de commitfase waar mogelijk onder tien minuten. Daarboven wisselen ontwikkelaars van context en daalt de productiviteit.

### Bouw eenmaal, promoveer overal

Produceer in de buildfase één onveranderlijk artefact en promoveer precies dat artefact door test, staging en productie. Bouw nooit per omgeving opnieuw, want een herbouw kan stilletjes verschillen introduceren. Configuratie die per omgeving varieert moet bij deployment worden geïnjecteerd, niet in aparte builds gebakken. Deze praktijk laat je een auditor ook met zekerheid vertellen dat het binaire bestand in productie het bestand is dat elke poort passeerde.

### Maak de pijplijn het afdwingpunt voor beleid

Codeer vereiste controles (goedkeuring van codereview, drempels voor testdekking, resultaten van beveiligingsscans, ondertekende commits) direct in de pijplijn en branchbeschermingsregels. Handmatig beleid dat in een wiki leeft wordt onder deadlinedruk routinematig omzeild. Beleid gecodeerd in de pijplijn wordt uniform en automatisch op elke wijziging toegepast.

### Houd de hoofdlijn altijd uitbrengbaar

Gebruik trunk-based development, dat alle werk in één gedeelde branch integreert met weinig of geen langlevende branches, of gebruik kortlevende featurebranches, en leun op feature flags om onvoltooid werk te verbergen in plaats van langlevende branches. Dit houdt mergeconflicten klein en de hoofdlijn altijd inzetbaar, wat de voorwaarde is voor echte continuous delivery.

### Kies deploymentstrategieën bewust

Stem de deploymentstrategie af op het risico en de schadezone van de service:

- **Rolling**-deployments vervangen instanties geleidelijk en zijn een verstandige standaard voor stateless services.
- **[Blue-green](https://en.wikipedia.org/wiki/Blue-green_deployment)** houdt twee identieke omgevingen aan en schakelt verkeer in één keer om, wat een direct rollbackpad geeft.
- **Canary**-releases sturen een klein percentage verkeer naar de nieuwe versie, bewaken gezondheidsstatistieken en breiden alleen uit als de signalen goed zijn.
- **Feature flags** koppelen release los van deployment, zodat je functionaliteit voor specifieke gebruikers of cohorten kunt inschakelen zonder opnieuw te deployen.

### Neem progressieve oplevering aan met geautomatiseerde rollback

Progressieve oplevering combineert canary-releases met geautomatiseerde analyse van statistieken als foutpercentage, latentie en verzadiging. Definieer objectieve gezondheidscriteria vooraf en laat het systeem dan automatisch promoveren of terugdraaien op basis van die signalen. Geautomatiseerde rollback neemt de menselijke aarzeling weg die een klein incident in een groot verandert.

### Bied releasemanagement en wijzigingsbeheer voor gereguleerde omgevingen

Houd in gereguleerde omgevingen een lichtgewicht maar echte wijzigingsregistratie bij. Leg automatisch vast wie elke wijziging goedkeurde, welke tests draaiden en welk artefact werd gedeployd. Gebruik wijzigingsadviesprocessen voor werkelijk risicovolle wijzigingen, maar reserveer ze voor die gevallen. Elke routinewijziging door een wekelijkse raad leiden vernietigt de waarde van automatisering. Mik in plaats daarvan op standaard, vooraf goedgekeurde wijzigingstypen die zonder ceremonie door de pijplijn stromen.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| Continuous delivery (handmatige releasepoort) | Het bedrijf beheert de timing. Sterk voor gereguleerde releasevensters | Vraagt discipline om de hoofdlijn inzetbaar te houden | Ondernemingen met wijzigingsvensters |
| Continuous deployment (volledig automatisch) | Snelste feedback. Kleinste batches | Vraagt volwassen tests en observeerbaarheid | Teams met veel vertrouwen en hoge frequentie |
| Blue-green | Directe rollback. Eenvoudig mentaal model | Verdubbelt omgevingskosten tijdens de omschakeling | Kritieke services die snel terugdraaien nodig hebben |
| Canary + progressieve oplevering | Beperkt schadezone. Datagedreven | Complex te bouwen. Vraagt goede statistieken | Grootschalige gebruikersgerichte systemen |
| Feature flags | Koppelt deploy los van release | Flagschuld als niet opgeruimd | Teams die onvoltooid werk veilig opleveren |

De centrale afweging is snelheid tegenover controle, maar dat is vaak een valse keuze. Volwassen automatisering levert beide: releases zijn sneller omdat ze kleiner zijn, en veiliger omdat elke is geverifieerd en omkeerbaar. De echte kosten zijn de investering vooraf in testdekking, observeerbaarheid en pijplijnengineering, plus de doorlopende discipline om ze gezond te houden. Organisaties die op die investering beknibbelen krijgen de snelheid zonder de veiligheid, wat erger is dan een traag handmatig proces.

## Vragen om met je team te bespreken

1. **Wat is je doel voor feedbacktijd in de commitfase, en wat wordt weggesneden wanneer de suite tien minuten ontgroeit?** Een trage commitfase doodt continuous integration stilletjes, omdat ontwikkelaars ophouden op groen te wachten en wijzigingen gaan bundelen. Besluit het getal nu (dit hoofdstuk pleit voor onder tien minuten) en besluit het mechanisme om het te houden: parallelle workers, een strikte testpiramide en trage integratiecontroles naar een latere fase verplaatsen. Op ondernemingsschaal is dit een platformbeslissing, aangezien honderden engineers dezelfde pijplijn delen en elke toegevoegde minuut zich vermenigvuldigt over elke commit. Neem echte data mee naar de vergadering: huidige p50 en p95 van pijplijnduur, de traagste tien tests en hoe vaak mensen herstarten in plaats van wachten. Als je het doel niet kunt noemen en met cijfers verdedigen, drijft je pijplijn af naar een batchproces in CI-kostuum.

2. **Welke deploymentstrategie gebruikt elke service, en wie is verantwoordelijk voor die keuze?** Rolling, blue-green en canary zijn niet uitwisselbaar: ze ruilen kosten, rollbacksnelheid en complexiteit verschillend, en de juiste keuze hangt af van de schadezone van de service. Blue-green koopt directe rollback tegen de prijs van een verdubbelde omgeving tijdens de omschakeling, wat het waard is voor een betalingssysteem en verspillend voor een intern dashboard. Canary beperkt blootstelling maar vraagt goede gezondheidsstatistieken en meer pijplijnengineering. Voor een groot of gereguleerd landschap levert het aan de gewoonte van elk team overlaten inconsistentie op die tijdens een incident aan het licht komt, dus spreek standaarden per servicelaag af en leg de beslissing vast. Neem je servicecatalogus mee en tag elke service met haar strategie, haar rollbackpad en de persoon die die keuze bezit.

3. **Hoe bewijs je dat het artefact in productie precies degene is die elke poort passeerde?** Bouw eenmaal en promoveer het identieke artefact is het hele spel voor controleerbaarheid, en het breekt zodra iemand per omgeving herbouwt of een draaiende machine patcht. In omgevingen van onderneming en overheid zal een auditor je vragen een draaiend binair bestand terug te traceren naar zijn commit, zijn review en zijn goedkeuringen, en je wilt dat dat antwoord seconden kost, geen week. Besluit hoe je het afdwingt: onveranderlijke artefacten, ondertekende images, handtekeningverificatie bij deployment en configuratie die bij deployment wordt geïnjecteerd in plaats van in aparte builds gebakken. Neem de huidige gaten mee naar de tafel, zoals elke fase die herbouwt, elk handmatig hotfixpad en elke plek waar config het artefact forkt. Het antwoord bepaalt of je complianceonderbouwing een bijproduct van de pijplijn is of een handmatige haast vóór elke audit.

4. **Wanneer de hoofdlijn rood gaat, wat stopt er dan werkelijk, en hoe ga je om met onbetrouwbare tests?** Een pijplijn is alleen een gezaghebbende poort als een rode build werk werkelijk stopt, toch tolereren veel organisaties stilletjes een kapotte hoofdlijn en een achterstand aan onregelmatige falen, wat ontwikkelaars traint te herstarten tot groen en bovenop falen op te leveren. Voor een groot team stapelt dit verval zich op, omdat de genegeerde flake van het ene team het excuus van iedereen wordt de poort te omzeilen, en vertrouwen in de pijplijn veel goedkoper te behouden is dan te herbouwen. Weeg de concurrerende trekken: een strikte stop-de-lijnregel beschermt kwaliteit maar kan honderden engineers blokkeren op één slechte commit, terwijl een soepel beleid doorvoer behoudt en de poort erodeert. Neem bewijs mee naar de discussie: je huidige rode tijd van de hoofdlijn, het aantal in quarantaine geplaatste of onbetrouwbare tests, het herstartpercentage en hoe vaak wijzigingen mergen over een falende controle. Noem in omgevingen van onderneming en overheid wie flaketriage bezit en wie het gezag heeft merges te bevriezen, want een poort waarvoor niemand verantwoordelijk is voor het afdwingen is er een waarvan auditors zullen vinden dat ze routinematig is overschreven.

5. **Wat is je levenscyclus voor feature flags, en wie moet ze afschaffen?** Flags zijn wat je deployment van release laat scheiden en onvoltooid werk laat verbergen, maar elke flag is een tak in je code die zichzelf nooit opruimt, en onbeheerde flags stapelen zich op tot voorwaardelijke complexiteit die niemand durft aan te raken. In een groot landschap is deze schuld gevaarlijk, omdat een verouderde flag stilletjes een beveiligingsreparatie kan poorten of ongeteste codepaden naar productie kan schakelen, en de maker er vaak is weggegaan. Balanceer de spanning: flags kochten je veilige, incrementele oplevering, dus het doel is niet minder flags maar een gedisciplineerde levenscyclus met een eigenaar, een verwachting van verloop en tooling die verouderde naar boven brengt. Neem de huidige inventaris mee naar de vergadering: hoeveel flags zijn live, hoe oud is de oudste, welke hebben geen eigenaar en of een langlevende flag nu als permanente configuratie functioneert die elders hoort. Voeg voor gereguleerde omgevingen toe wie een flag in productie mag wijzigen en of die wijziging met dezelfde rigueur wordt gelogd als een deployment, aangezien een flagomschakeling een release is ook als de pijplijn nooit draait.

6. **Waar ligt de grens tussen continuous delivery met een menselijke poort en volledige continuous deployment, en wie stelt de rollbackdrempels?** Continuous delivery houdt een persoon in controle over de releasetiming, wat past bij wettelijke wijzigingsvensters en systemen met hoge schadezone, terwijl continuous deployment elke slagende wijziging automatisch uitbrengt en volwassen tests, observeerbaarheid en geautomatiseerde rollback vraagt om veilig te zijn. Voor een grote of gereguleerde organisatie is het antwoord zelden uniform: je marketingsite kan continu deployen terwijl je betalingskern een gedocumenteerde menselijke poort houdt, en die lijn per servicelaag trekken voorkomt zowel onnodige wrijving als roekeloze automatisering. De concurrerende overwegingen zijn snelheid en batchgrootte tegenover controle en controleerbaarheid, plus de engineeringkosten van de gezondheidsstatistieken die geautomatiseerde rollback vereist. Neem het bewijs mee: wijzigingsfaalpercentage per service, gemiddelde hersteltijd, huidige releasefrequentie en de objectieve signalen (foutpercentage, latentie, verzadiging) die je zou vertrouwen om zonder mens te promoveren of terug te draaien. Koppel in overheids- en ondernemingsomgevingen elke laag aan wie de rollbackdrempels bezit en wie elke stap van een gepoorte release naar volledige automatisering goedkeurt, zodat de beslissing bewust is in plaats van afdrijft.

## Sectorperspectief

**Startup.** Leun vanaf dag één op beheerde CI/CD: een gehoste runner, één pijplijn, één onveranderlijk image en automatische deploy naar staging bij merge. Bouw geen pijplijninfrastructuur die je dan moet onderhouden. Feature flags laten twee of drie engineers veilig half afgemaakt werk mergen en meerdere keren per dag opleveren, en een productiedeploy met één klik plus een snelle flag-uit is alle wijzigingsbeheer dat je nodig hebt tot schaal meer afdwingt.

**Kleinbedrijf.** Zonder aparte platform- of releaseengineer geef je de voorkeur aan de pijplijn die je bronhost je geeft (ingebouwde Actions of equivalent) en haar standaarddeploymentstrategie boven alles op maat. Formuleer de keuze tussen kopen en bouwen eerlijk: een beheerde pijplijn en een hostingplatform met ingebouwde rollback kosten minder dan de engineeruren die een maatwerkopzet verbruikt. Houd de essentie, namelijk eenmaal bouwen, hetzelfde artefact promoveren en een makkelijke revert, en sla de progressieve-opleveringsmachinerie over tot volume haar rechtvaardigt.

**Grote onderneming.** Het kernprobleem is consistentie over veel teams: standaardiseer een gedeeld pijplijnsjabloon dat review, scanning, ondertekende onveranderlijke artefacten en deploymentstrategieën per laag afdwingt, zodat kwaliteit niet per team varieert. Behandel pijplijndefinities als beoordeelde code, leg wijzigingsbeheerbewijs automatisch vast en beheer feature flags en rollbackdrempels als bestuurde bezittingen in plaats van de privégewoonte van elk team. De opbrengst is snellere oplevering en auditbewijs geproduceerd als bijproduct in plaats van een kwartaalhaast.

**Overheid.** Aanbestedingsregels, wettelijke wijzigingsvensters en publieke verantwoording geven de pijplijn vorm. Geef voor ingrijpende systemen de voorkeur aan continuous delivery met een gedocumenteerde menselijke releasepoort boven volledige automatisering, classificeer routinewerk als vooraf goedgekeurde standaardwijzigingen en houd een direct rollbackpad (blue-green of geautomatiseerde canary) voor services waar burgers tijdens smalle jaarlijkse vensters van afhangen. Zorg dat de pijplijn vastlegt wie elke wijziging goedkeurde, welke tests draaiden en welk artefact werd gedeployd, zodat transparantie- en auditverplichtingen door de normale workflow worden voldaan in plaats van door handmatig papierwerk.

## Voorbeelden

**Startup.** Een SaaS-startup van vier personen zet één GitHub Actions-pijplijn op die unittests draait, één Docker-image bouwt en datzelfde image automatisch naar staging deployt bij elke merge naar main. Een productiedeploy is één klik, en de oprichters leunen op feature flags zodat ze half afgemaakt werk achter een flag kunnen mergen in plaats van een branch weken in leven te houden. Wanneer een slechte release doorglipt, zetten ze de flag in seconden uit en repareren ze rustig, wat hun piepkleine team meerdere keren per dag laat opleveren zonder aparte ops-persoon.

**Grote onderneming.** Een wereldwijde bank consolideert tientallen teamspecifieke Jenkinsjobs in een gestandaardiseerd pijplijnsjabloon dat elk productteam erft. Het sjabloon dwingt statische analyse, afhankelijkheidsscanning en een ondertekend, onveranderlijk artefact af en deployt via canary met geautomatiseerde rollback gekoppeld aan drempels voor foutpercentage en latentie. Omdat hetzelfde artefact van test naar productie wordt gepromoveerd en elke poort wordt gelogd, kunnen de auditors van de bank elk productiebinair in seconden terugtraceren naar zijn commit, review en goedkeuring, wat een kwartaaloefening in handmatig bewijs verzamelen vervangt.

**Overheid.** Een nationale belastingdienst die een aangiftesysteem moderniseert neemt continuous delivery aan met een expliciete menselijke releasepoort, zodat ze wettelijke wijzigingsvensters tijdens het aangifteseizoen kan respecteren. Routinewijzigingen worden geclassificeerd als vooraf goedgekeurde standaardwijzigingen die automatisch naar staging stromen. Productierelease vereist één gedocumenteerde goedkeuring die de pijplijn vastlegt. Blue-green-deployment geeft de dienst een direct rollbackpad als een defect productie bereikt, wat cruciaal is wanneer miljoenen burgers tijdens een smal jaarlijks venster van de dienst afhangen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van CI/CD-investering toont zich als kortere doorlooptijd voor wijzigingen, lager wijzigingsfaalpercentage en snellere herstel wanneer incidenten optreden: de statistieken die onderzoek consistent koppelt aan zowel leveringsprestaties als organisatorische uitkomsten. Snellere, kleinere releases snijden de coördinatieoverhead weg die op schaal engineeringcapaciteit opslokt, en geautomatiseerde verificatie snijdt het dure, moraalondermijnende werk van productiedefecten blussen weg.

De total cost of ownership weegt adoptiekosten af tegen de kosten van niet adopteren. Adoptiekosten omvatten pijplijnen bouwen en onderhouden, testdekking laten groeien en investeren in observeerbaarheid en platformpersoneel. De kosten van niet adopteren zijn groter maar minder zichtbaar: trage handmatige releases, integratiepijn, productie-incidenten die reputatie schaden en, in gereguleerde omgevingen, mislukte audits en herstel. Voor leiderschap wordt het argument het best geformuleerd als risicovermindering en capaciteit. Automatisering zet schaarse tijd van senior engineers om van repetitief releasesleurwerk in productwerk, terwijl uitval zeldzamer en korter wordt.

## Antipatronen en valkuilen

- **Sneeuwvlokpijplijnen.** Elk team bouwt met de hand een unieke pijplijn, zodat verbeteringen en reparaties niet gedeeld kunnen worden en kwaliteit wild varieert.
- **Herbouw per omgeving.** Voor elke fase herbouwen breekt de garantie "eenmaal bouwen" en laat subtiele verschillen productie bereiken.
- **Genegeerde rode builds.** Een aanhoudend kapotte hoofdlijn tolereren vernietigt vertrouwen in de pijplijn en normaliseert opleveren bovenop falen.
- **Onbehandelde onbetrouwbare tests.** Onregelmatige falen trainen ontwikkelaars te herstarten tot groen, wat het doel van de poort tenietdoet.
- **Goedkeuringstheater.** Een wijzigingsadviesraad die alles afstempelt voegt vertraging toe zonder veiligheid toe te voegen.
- **Flagschuld.** Feature flags die nooit worden verwijderd stapelen zich op tot onbeheersbare voorwaardelijke complexiteit.
- **Deploy gelijk release.** Beide koppelen betekent dat elke gebruikersgerichte wijziging een riskante herdeployment vereist.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Builds en deployments zijn grotendeels handmatig, ad hoc en reactief. Integratie gebeurt laat, releases zijn zeldzaam en stressvol, rollback betekent een oude versie met de hand opnieuw deployen en er is geen gedeeld begrip van een pijplijnpoort.

**Niveau 2: Ontwikkelen.** Geautomatiseerde builds en unittests draaien bij elke commit, maar praktijken verschillen per team. Deployments zijn gescript maar nog handmatig getriggerd en gesuperviseerd, sommige omgevingen zijn consistent en artefacten kunnen nog per fase worden herbouwd. Waar een pijplijn bestaat is ze vaak een sneeuwvlok die niet gedeeld kan worden.

**Niveau 3: Standaardiseren.** Een gedocumenteerd, gestandaardiseerd pijplijnsjabloon wordt over teams afgedwongen. Het promoveert één onveranderlijk artefact door alle omgevingen, past geautomatiseerde kwaliteits- en beveiligingspoorten toe, codeert vereiste controles zoals reviewgoedkeuring en scanresultaten en legt wijzigingsregistraties automatisch vast. Deploymentstrategieën als canary of blue-green worden bewust per servicelaag gekozen.

**Niveau 4: Beheersen.** Oplevering wordt gemeten en beheerst aan de hand van uitgangswaarden. De organisatie volgt doorlooptijd voor wijzigingen, deploymentfrequentie, wijzigingsfaalpercentage en gemiddelde hersteltijd, samen met p50 en p95 van pijplijnduur, percentages onbetrouwbare tests en herstarts en leeftijd van feature flags. Rollbackdrempels worden gesteld uit waargenomen data over foutpercentage, latentie en verzadiging, poorten worden afgedwongen op bewijs in plaats van gewoonte en elke statistiek heeft een eigenaar die handelt wanneer ze van het doel afdrijft.

**Niveau 5: Orkestreren.** Oplevering wordt continu verbeterd en over de organisatie geïntegreerd. Progressieve oplevering met geautomatiseerde, statistiekgedreven rollback is de norm, release is losgekoppeld van deployment via goed bestuurde flags en complianceonderbouwing wordt automatisch geproduceerd als bijproduct. De pijplijn past zich aan naarmate het landschap verandert, en leveringsstatistieken voeden bedrijfs- en risicoplanning zodat investering naar de verbeteringen met de hoogste hefboom stroomt.

## Ideeën voor discussie

- Waar ligt de juiste grens tussen continuous delivery met een menselijke poort en volledige continuous deployment voor je meest kritieke systemen?
- Hoe houd je een verplicht wijzigingsbeheerproces betekenisvol zonder het in afstempeltheater te laten verworden?
- Welke objectieve gezondheidsstatistieken moeten geautomatiseerde rollback besturen, en wie bezit hun drempels?
- Hoe moeten platformteams gestandaardiseerde pijplijnsjablonen afwegen tegen de legitieme behoeften van teams met ongebruikelijke eisen?
- Wat is je beleid en tooling om feature flags af te schaffen voordat ze schuld worden?
- Hoe meet je of snellere oplevering werkelijk bedrijfsuitkomsten verbetert in plaats van alleen meer uit te leveren?

## Belangrijkste inzichten

- CI, CD en continuous deployment zijn verschillend. Kies het automatiseringsniveau dat bij je risicotolerantie en volwassenheid past.
- Bouw het artefact eenmaal en promoveer het identieke artefact door elke omgeving.
- Ontwerp de pijplijn als geordende kwaliteitspoorten geoptimaliseerd voor snelle feedback en behandel haar als gezaghebbende uitleverbeslissing.
- Kies deploymentstrategieën bewust, en neem progressieve oplevering met geautomatiseerde rollback aan om de schadezone te beperken.
- Koppel release los van deployment met feature flags en beheer flagschuld.
- Leg in gereguleerde omgevingen wijzigingsbeheerbewijs automatisch vast in plaats van met handmatig papierwerk.

## Referenties en verder lezen

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
