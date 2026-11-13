# 6.2 Machine-learningengineering (MLOps)

## Overzicht en motivatie

Machine-learningengineering, meestal [MLOps](https://en.wikipedia.org/wiki/MLOps) genoemd, is de discipline van [machine learning](https://en.wikipedia.org/wiki/Machine_learning) uit notebooks en experimenten halen en omzetten in betrouwbare, observeerbare, onderhoudbare productiesystemen. Traditionele software gedraagt zich zoals haar code zegt dat ze zal doen. Een ML-systeem gedraagt zich zoals haar code, haar data en haar geleerde modelparameters samen zeggen dat ze zal doen. Dat maakt ML-systemen moeilijker te testen, moeilijker te reproduceren en gevoelig voor stil falen naarmate de wereld wegdrijft van de data waarop ze zijn getraind. MLOps brengt de rigueur van software-engineering (versiebeheer, testen, continuous delivery en bewaking) in deze drieledige realiteit van code plus data plus modellen.

Voor grote teams is MLOps wat een eenmalig model dat schittert in een demo scheidt van een vloot modellen die veel teams veilig kunnen bouwen, deployen en beheren. Zonder gedeelde platformen en praktijken vindt elk team datapijplijnen, trainingslussen en deployment opnieuw uit, en eindig je met kwetsbare systemen die zes maanden later niemand kan reproduceren. Ondernemingen leunen op MLOps om te schalen over tientallen modellen, service-level objectives te halen en auditors tevreden te stellen die vragen hoe een gegeven voorspelling tot stand kwam.

In de overheid en gereguleerde sectoren is MLOps vaak een verkapte complianceeis. Reproduceerbaarheid, herkomst en versiebeheer laten een instantie een juridisch belangrijke vraag beantwoorden: precies welk model, getraind op welke data, met welke code, produceerde de beslissing die een burger raakte? Een volwassen MLOps-praktijk houdt die vraag jaren later beantwoordbaar, wat zowel goede engineering is als een wettelijke waarborg.

*Zie ook:* hoofdstuk 8.1 (CI/CD en oplevering), hoofdstuk 9.2 (observeerbaarheid en bewaking) en hoofdstuk 6.6 (AI-infrastructuur en -operaties).

## Kernprincipes

- Behandel data, code en modellen als gezamenlijk geversioneerde artefacten. Verandert er één, dan verandert het systeemgedrag.
- Automatiseer het pad van data naar getraind model naar deployment zodat het herhaalbaar en controleerbaar is.
- Maak elk model herleidbaar tot de exacte data, code en configuratie die het produceerden.
- Evalueer modellen tegen representatieve, achtergehouden data vóór deployment, en blijf evalueren erna.
- Neem aan dat modellen degraderen. Bewaak vanaf dag één op drift (het geleidelijk uiteenlopen van live data of invoer-uitvoerrelaties van waarop het model is getraind), dataproblemen en prestatieverval.
- Geef de voorkeur aan saaie, reproduceerbare pijplijnen boven slimme, niet-reproduceerbare experimenten.
- Scheid de zorgen van experimenteersnelheid en productiebetrouwbaarheid, en overbrug ze bewust.

## Aanbevelingen

### Beheer de volledige ML-levenscyclus expliciet

Definieer en instrumenteer elke fase: data-inname en -validatie, [feature engineering](https://en.wikipedia.org/wiki/Feature_engineering), training, evaluatie, deployment en bewaking. Maak de grenzen tussen fasen expliciet zodat elke kan worden getest, herhaald en geaudit. Vermijd het gangbare falen waarbij een model in een ad hoc notebook wordt getraind en over de muur naar operaties wordt gegooid. Wikkel in plaats daarvan de levenscyclus in een georkestreerde pijplijn die elke geautoriseerde engineer vanuit een schone checkout kan draaien.

### Gebruik feature stores, experimenttracking en modelregisters

Een **feature store** centraliseert featuredefinities zodat dezelfde transformaties in zowel training als serving draaien. Dit elimineert training-serving skew (inconsistenties in hoe features worden berekend voor training tegenover voor live voorspellingen) en laat teams features hergebruiken in plaats van ze opnieuw te berekenen. **Experimenttracking** legt van elke trainingsrun de parameters, codeversie, dataversie en statistieken vast, zodat resultaten vergelijkbaar en reproduceerbaar zijn. Een **modelregister** is het systeem van registratie voor getrainde modellen, met versies, herkomst, evaluatieresultaten, goedkeuringsstatus en deploymentfase. Samen laten deze je "wat is er veranderd?" beantwoorden wanneer gedrag verschuift, en modellen door bestuurde fasen promoveren of terugdraaien.

### Maak data en modellen reproduceerbaar en geversioneerd met herkomst

Versioneer je datasets, niet alleen je code. Gebruik content-addressable opslag of dataversietools zodat een trainingsrun naar een onveranderlijke momentopname verwijst. Pin code met git-commits en omgevingen met vergrendelde afhankelijkheden en containerimages. Leg herkomst van begin tot eind vast: welke ruwe data welke features voedde, welke features en code welk model produceerden en waar dat model is gedeployd. Wanneer een incident of audit toeslaat, verandert herkomst een forensische nachtmerrie in een eenvoudige query. Leg willekeur (seeds) en hardware vast waar resultaten ervan afhangen.

### Kies deploymentpatronen die bij de werklast passen

- **Batch**-scoring draait volgens schema over grote datasets. Het eenvoudigst te beheren, latentietolerant, ideaal voor rapporten en periodieke beslissingen.
- **Online (realtime)** serving reageert op individuele verzoeken binnen krappe latentiebudgetten. Vraagt featureretrieval met lage latentie en zorgvuldige capaciteitsplanning.
- **Streaming** scoort gebeurtenissen continu zodra ze binnenkomen. Past bij fraudedetectie en bewaking waar versheid cruciaal is.
- **Edge** draait modellen op apparaten of lokale hardware om redenen van latentie, privacy, connectiviteit of datasoevereiniteit, gangbaar in overheids- en veldomgevingen.

Kies het eenvoudigste patroon dat aan de eis voldoet en ontwerp je uitrol met schaduwdeployments, canaries en directe rollback.

### Bewaak op drift, degradatie en datakwaliteit

Instrumenteer invoer en uitvoer in productie. Let op **datadrift** (invoerverdelingen die verschuiven), **[conceptdrift](https://en.wikipedia.org/wiki/Concept_drift)** (de relatie tussen invoer en doelvariabele die verandert), falen van **datakwaliteit** (nulls, schemawijzigingen, kapotte bronnen stroomopwaarts) en **prestatieverval** gemeten tegen vertraagde ground truth waar je die hebt. Stel alarmdrempels in, schrijf runbooks en bedraad bewaking aan je hertrainingstriggers. Stille degradatie is de klassieke ML-faalwijze, en bewaking is je enige verdediging ertegen.

## Afwegingen: voor- en nadelen

| Beslissing | Optie A | Optie B | Afweging |
|---|---|---|---|
| Servingpatroon | Batch | Online | Eenvoud en kosten tegenover versheid en latentie |
| Featureberekening | Feature store | Pijplijnen per model | Consistentie en hergebruik tegenover opzetoverhead |
| Platform | Een beheerd MLOps-platform kopen | Open-sourcetools samenstellen | Snelheid en ondersteuning tegenover flexibiliteit en lock-in |
| Hertraining | Gepland | Getriggerd door drift | Voorspelbaarheid tegenover responsiviteit en complexiteit |
| Reproduceerbaarheidsrigueur | Volledig dataversiebeheer | Lichtgewicht tracking | Auditkracht tegenover opslag en inspanning |

De overkoepelende afweging is investering nu tegenover kwetsbaarheid later. Zware infrastructuur voor reproduceerbaarheid en bewaking kost vooraf inspanning, maar voorkomt de veel grotere kosten van onverklaarbare falen, niet-reproduceerbare modellen en geërodeerd vertrouwen. Beheerde platformen versnellen teams maar kunnen lock-in creëren. Open-sourcestacks bieden controle tegen de prijs van integratiewerk. Grote organisaties hebben meestal baat bij een gedeeld platformteam dat deze complexiteit verbergt achter standaarden op de gebaande weg.

## Vragen om met je team te bespreken

1. **Hoe zouden we ontdekken dat een gedeployd model stilletjes is gedegradeerd voordat een klant of burger schade lijdt, en wie bezit dat alarm?** Stille verval is de klassieke ML-faalwijze: de code draait nog, het model geeft nog zelfverzekerde scores en de kwaliteit zakt naarmate de wereld van de trainingsdata afdrijft. Voor een groot team dat veel modellen draait moet je dit per model beantwoorden, niet eenmaal voor de vloot, omdat elk zijn eigen driftprofiel en eigen ground-truthvertraging heeft. Neem je huidige monitors voor datadrift, conceptdrift en datakwaliteitsbreuken mee, de alarmdrempels en het runbook dat zegt wie reageert. Bespreek in gereguleerde omgevingen waar labels weken te laat komen proxysignalen die je intussen kunt volgen, want wachten op vertraagde ground truth betekent wachten om schade te ontdekken. Als geen enkele eigenaar is genoemd voor het driftalarm van een model, is dat model in feite onbewaakt.

2. **Als een auditor ons vroeg een specifieke voorspelling van achttien maanden geleden te reproduceren, zouden we dat dan werkelijk van begin tot eind kunnen?** Reproduceerbaarheid is de complianceeis verborgen in goede engineering: ze laat een instantie beantwoorden precies welk model, getraind op welke data, met welke code, een beslissing produceerde die iemand raakte. Neem een echt voorbeeld mee en probeer het te traceren: de onveranderlijke datamomentopname, de git-commit, de vergrendelde afhankelijkheden en het containerimage, de vastgelegde seeds en de herkomst van ruwe data via features naar het gedeployde model. Het signaal is of enige schakel in die keten ontbreekt of handmatig is. Besluit voor overheid en gereguleerde sectoren de bewaartermijn die de wet werkelijk vereist en bevestig dat je opslag de herkomst voor dat hele venster beantwoordbaar houdt, aangezien een gat een routinequery in een forensisch noodgeval verandert.

3. **Wat is onze regel voor een model naar productie promoveren en terugdraaien, en wordt die afgedwongen door het register of alleen door vertrouwen?** Ongecontroleerde promotie is hoe notebookexperimenten in productie lekken en hoe een slecht model blijft hangen omdat niemand het schoon kan terugdraaien. Voor veel teams is het verschil tussen volwassen en kwetsbaar of het modelregister promotie poort met verplichte goedkeuring en evaluatie, of dat een engineer gewichten met de hand kan pushen. Neem je huidige promotiepad mee, je rollbackmechanisme en bewijs dat schaduwdeployments of canaries werkelijk draaien voor het volledige verkeer. Bespreek of hertraining gepland of driftgetriggerd is, en of gehertrainde modellen validatiepoorten passeren vóór deployment, want hertrainen op live data zonder validatie versterkt drift of vergiftiging. Het antwoord moet in het platform worden afgedwongen, niet in een wikipagina die mensen geacht worden te volgen.

4. **Bouwen we ons MLOps-platform op open-sourcetools, kopen we een beheerd platform of mengen we de twee, en wie heeft de lock-in gewogen?** Deze keuze bepaalt het plafond van hoe snel elk toekomstig model wordt opgeleverd en hoeveel controle je houdt over je data en pijplijnen. Een beheerd platform brengt teams snel naar productie en draagt ondersteuning, maar kan je featuredefinities, herkomstregistraties en modelartefacten vangen in een bedrijfseigen formaat dat je moeilijk kunt verlaten. Een samengestelde open-sourcestack houdt je overdraagbaar tegen de prijs van echte integratie- en onderhoudsarbeid. Neem de total cost of ownership voor elk pad mee (licentie of bouw, opslag, rekenkracht voor hertraining en het platformpersoneel om het te beheren), een eerlijke lezing van de capaciteit van je team om infrastructuur te draaien en een concrete exittest: kun je je register, feature store en herkomst exporteren en elders herbouwen? Voeg in omgevingen van onderneming en overheid aanbestedingsbeperkingen en datasoevereiniteitsregels toe, aangezien een platform dat trainingsdata opslaat in een regio of formaat dat je toezichthouder verbiedt is gediskwalificeerd hoe gemakkelijk het ook is.

5. **Moeten onze feature store en ons modelregister één gecentraliseerd platform zijn of gefedereerd per team, en wat kost training-serving skew ons vandaag?** Featuredefinities centraliseren elimineert de skew waarbij een feature in training op de ene manier wordt berekend en in serving op een andere, een stille en dure bron van nauwkeurigheidsverlies, maar één platform kan een knelpunt worden dat elk team vertraagt. Federeren geeft teams autonomie terwijl het de leidingen vermenigvuldigt en de kans dat twee teams dezelfde feature inconsistent definiëren. Neem bewijs mee van waar skew je al heeft gebeten, hoeveel teams features hergebruiken tegenover opnieuw bouwen en de standaarden op de gebaande weg die een gedeeld platformteam kan bieden. Weeg voor een grote organisatie het governancevoordeel van één controleerbaar systeem van registratie af tegen de leveringskosten van een centrale wachtrij, en geef in gereguleerde omgevingen de voorkeur aan de gecentraliseerde herkomst waarmee een auditor elke voorspelling kan herleiden tot de exacte featurecode die haar produceerde.

6. **Hebben we het deploymentpatroon van elk model afgestemd op zijn echte latentie-, versheids- en soevereiniteitsbehoeften, of alles naar één vorm laten standaarden?** Batch, online, streaming en edge dragen elk heel verschillende operationele kosten en complexiteit, en het verkeerde kiezen geeft óf te veel uit aan realtime-infrastructuur die een nachtelijk rapport nooit nodig had óf laat een fraudescorer verhongeren van de versheid waarvan hij afhangt. Besluit per werklast welk patroon de eis werkelijk rechtvaardigt, en weersta standaardiseren op de meest complexe optie omdat die modern voelt. Neem het latentiebudget mee, het volume, de kosten van een verouderd antwoord en de ground-truthvertraging voor elk model. Weeg in overheids- en veldomgevingen edge- en on-premisesdeployment bewust af, omdat datasoevereiniteitsregels of onderbroken connectiviteit modellen op lokale hardware kunnen afdwingen, en die keuze herschikt hoe je elk model dat je daar pusht versioneert, bewaakt en terugdraait.

## Sectorperspectief

**Startup.** Je schaarste middel is engineeringaandacht, dus houd MLOps lichtgewicht en koop het. Volg experimenten in een eenvoudige gehoste tool, pin elk gedeployd model aan zijn trainingsdatamomentopname en codecommit in git en voeg één goedkope driftcontrole toe in plaats van een platform. Sla de feature store en maatwerkpijplijnen over tot een tweede of derde model het hergebruik waard maakt. Een kwetsbare stack die je niet kunt onderhouden laat je sneller zinken dan een ontbrekend vermogen.

**Kleinbedrijf.** Je hebt waarschijnlijk geen ML-platformspecialist en een krap budget, dus behandel MLOps als iets ingebed in de tools die je al draait in plaats van een systeem dat je bemant. Geef de voorkeur aan een beheerde dienst die versiebeheer, deployment en bewaking voor je afhandelt, en formuleer de discipline als vraag over datahygiëne en reproduceerbaarheid: weet welk model en welke data een gegeven resultaat produceerden en houd het vermogen terug te draaien. Geef de voorkeur aan leveranciers die je je data en modellen laten exporteren zodat een latere overstap mogelijk blijft.

**Grote onderneming.** Het probleem is schaal over tientallen modellen en veel teams: een gedeelde feature store, experimenttracking en een modelregister met bestuurde promotie zodat groepen ophouden pijplijnen opnieuw uit te vinden. Begroot een platformteam dat standaarden op de gebaande weg biedt, standaardiseer herkomst en bewaking zodat elk model controleerbaar is en elk incident verklaarbaar en beheer bouwen of kopen en lock-in bewust achter een interface die de onderliggende tools verwisselbaar houdt. Dwing validatiepoorten en rollback af in het platform, niet in conventie.

**Overheid.** Reproduceerbaarheid, herkomst en versiebeheer zijn verkapte complianceeisen, dus behandel ze vanaf dag één als eersterangs. Versioneer de exacte dataset en code achter elk gedeployd model, bewaar die herkomst voor de wettelijk vereiste periode en kun elke historische voorspelling reproduceren die een burger raakte. Houd een mens ingrijpende beslissingen laten beoordelen, weeg edge- en on-premisesdeployment af waar datasoevereiniteitsregels het eisen en eis dat elk leveranciersplatform volledige overdraagbaarheid van je data, features en herkomst verleent.

## Voorbeelden

**Startup.** Een kleine analytics-startup leverde haar eerste verloopvoorspellingsmodel op met één datawetenschapper en een lichtgewicht opzet. Ze volgde experimenten in een eenvoudige gehoste tool, pinde elk gedeployd model aan zijn trainingsdatamomentopname en codecommit in git en voegde een eenvoudige wekelijkse job toe die recente invoer vergeleek met de trainingsverdeling. Toen een databron zijn datumformaat wijzigde en voorspellingen begonnen af te drijven, ving die eenvoudige controle het in dagen in plaats van na een boos klantentelefoontje, en kon het team het laatste goede model reproduceren en terugdraaien.

**Grote onderneming.** Een retailbank draait tientallen krediet- en fraudemodellen. Ze standaardiseerde op een feature store gedeeld over teams, een experimenttrackingdienst en een modelregister met verplichte goedkeuringspoorten. Elk model in productie is herleidbaar tot zijn trainingsdatamomentopname en codecommit. Fraudemodellen deployen als streamingscorers. Kredietmodellen draaien in batch. Een bewakingslaag volgt invoerdrift en alarmeert wanneer het schema van een databron verandert, wat ooit een kapotte feed stroomopwaarts ving voordat die beslissingen corrumpeerde.

**Overheid.** Een publieke uitkeringsinstantie gebruikt een ML-model om dossierbeoordelingen te prioriteren. Omdat die beslissingen de toegang van burgers tot diensten raken, versioneert de instantie de exacte dataset en code achter elk gedeployd model, bewaart deze herkomst voor de wettelijk vereiste periode en kan elke historische voorspelling op verzoek reproduceren. Modellen deployen in batch met een mens die gemarkeerde zaken beoordeelt, en een driftmonitor dwingt een verplichte herevaluatie af wanneer de binnenkomende populatie verschuift, zodat het model nooit stilletjes wordt toegepast buiten de omstandigheden waarvoor het is gevalideerd.

## Zakelijke onderbouwing: motivatie, ROI en TCO

MLOps verdient zichzelf terug door kwetsbare experimenten om te zetten in betrouwbare bezittingen. ROI komt uit snellere time-to-production voor nieuwe modellen, minder kostbare incidenten, minder dubbele infrastructuur en het vermogen veel modellen te beheren met een klein platformteam. Een gedeelde feature store en register kunnen de leveringstijd per model dramatisch verkorten, omdat teams ophouden dezelfde leidingen te herbouwen.

De TCO dekt platformbouw of -licentie, opslag voor geversioneerde data en modellen, rekenkracht voor hertraining en het personeel om alles te beheren. Weeg dat af tegen de kosten van niet adopteren: modellen die je niet kunt reproduceren of auditen, stille falen die klanten of burgers schaden en bevindingen van toezichthouders. In gereguleerde omgevingen kunnen de kosten van een onverklaarbaar model in een audit de hele MLOps-investering overtreffen. Maak de zaak voor het bestuur door MLOps te formuleren als risicovermindering en leveringsversnelling, niet overhead: een gebaande weg die elk toekomstig model zal afleggen.

## Antipatronen en valkuilen

- **Sprongen van notebook naar productie.** Modellen deployen die in ongecontroleerde notebooks zijn getraind zonder reproduceerbaarheid.
- **Training-serving skew.** Andere featurecode in training en serving, wat stil nauwkeurigheid kost.
- **Geen dataversiebeheer.** Code versioneren maar data niet, zodat runs niet kunnen worden gereproduceerd.
- **Deployen en vergeten.** Een model uitleveren zonder bewaking en degradatie pas ontdekken wanneer gebruikers klagen.
- **Hertraining op de automatische piloot.** Automatisch hertrainen op live data zonder validatie, wat drift of vergiftiging versterkt.
- **Eenmalige infrastructuur.** Elk team bouwt zijn eigen pijplijn, wat kosten en kwetsbaarheid vermenigvuldigt.
- **Vertraagde labels negeren.** Aannemen dat je nauwkeurigheid direct kunt meten wanneer ground truth weken later aankomt.

## Volwassenheidsmodel

1. **Initiëren.** Modellen ad hoc gebouwd in notebooks. Handmatige deployment. Geen versiebeheer van data of modellen. Geen bewaking. Een eerdere voorspelling reproduceren is gokken.
2. **Ontwikkelen.** Enige experimenttracking en een modelregister verschijnen, maar praktijken variëren per team. Deployment is half geautomatiseerd. Basisbewaking dekt enkele modellen. Dataversiebeheer is gedeeltelijk en herkomst heeft gaten.
3. **Standaardiseren.** Een gedeeld platform met een feature store, register, reproduceerbare pijplijnen en herkomst van begin tot eind is gedocumenteerd en organisatiebreed afgedwongen. Bewaking voor drift en datakwaliteit draait over modellen. Promotie en rollback volgen een bestuurd pad dat elk team gebruikt.
4. **Beheersen.** De vloot wordt gemeten aan de hand van uitgangswaarden: driftpercentages, datakwaliteitsbreuken, modelnauwkeurigheid tegen vertraagde ground truth, training-serving skew, time-to-production en bedrijfskosten per model worden als statistieken gevolgd. Alarmdrempels en validatiepoorten worden afgedwongen op bewijs, en de gezondheid van elk model wordt volgens een vast ritme beoordeeld met een benoemde eigenaar.
5. **Orkestreren.** De levenscyclus is volledig geautomatiseerd, controleerbaar en adaptief. Driftgetriggerde hertraining draait achter validatiepoorten. Self-service gebaande wegen laten teams veilig opleveren. Continue evaluatie koppelt modelprestaties aan bedrijfsstatistieken, en het platform is geïntegreerd met oplevering, risico en compliance zodat modellen routinematig worden afgeschaft, vervangen en opnieuw afgebakend naarmate data en omstandigheden verschuiven.

## Ideeën voor discussie

- Hoe balanceer je experimenteervrijheid met reproduceerbaarheid in productie?
- Wat is de juiste hertrainingstrigger (schema, drift of prestatieverval) voor jouw gebruiksgevallen?
- Hoe lang moet je data- en modelherkomst bewaren, en wat drijft die eis?
- Moeten feature stores en registers gecentraliseerde platformen zijn of gefedereerd per team?
- Hoe bewaak je nauwkeurigheid wanneer ground-truthlabels met lange vertraging aankomen?
- Wanneer is edgedeployment de extra operationele complexiteit waard?

## Belangrijkste inzichten

- ML-gedrag komt uit code plus data plus modellen. Versioneer en bestuur alle drie samen.
- Feature stores, experimenttracking en registers zijn de ruggengraat van reproduceerbare ML.
- Herkomst maakt modellen controleerbaar en incidenten verklaarbaar: essentieel in gereguleerde omgevingen.
- Kies batch, online, streaming of edge om bij latentie-, versheids- en soevereiniteitsbehoeften te passen.
- Modellen degraderen. Bewaking voor drift, datakwaliteit en verval is niet optioneel.

## Referenties en verder lezen

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
