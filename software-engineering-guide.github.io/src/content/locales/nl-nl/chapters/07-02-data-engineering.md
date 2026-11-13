# 7.2 Data-engineering

## Overzicht en motivatie

[Data-engineering](https://en.wikipedia.org/wiki/Data_engineering) is de discipline van de pijplijnen en platformen bouwen en beheren die data verplaatsen van waar ze wordt geproduceerd naar waar ze waarde creëert. Ze omvat inname uit bronsystemen, transformatie naar schone en gemodelleerde vormen, opslag in kostenefficiënte formaten, orkestratie van de hele stroom en de betrouwbaarheidspraktijken die het geheel betrouwbaar houden. Als datastrategie beslist welke data moet bestaan en wie haar bezit, is data-engineering de leiding en machinerie waardoor ze stroomt.

Voor grote teams is deze discipline fundamenteel. Analytics, [business intelligence](https://en.wikipedia.org/wiki/Business_intelligence), productexperimenten, [machine learning](https://en.wikipedia.org/wiki/Machine_learning) en regelgevende rapportage zitten allemaal stroomafwaarts van datapijplijnen. Wanneer die pijplijnen kwetsbaar, traag of ondoorzichtig zijn, lijdt elke afhankelijke functie. Dashboards tonen verouderde getallen. Modellen trainen op corrupte features. Auditors kunnen niet reconstrueren hoe een cijfer tot stand kwam. Op schaal van onderneming en overheid verwerken pijplijnen miljarden records uit veel bronsystemen, en één stil falen kan foute data in beslissingen, betalingen of publieke statistieken duwen.

Het vakgebied is gegroeid van maatwerkscripts en monolithische [ETL (extract, transform, load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)-tools naar de moderne datastack: modulaire, grotendeels SQL-gedreven componenten voor inname, transformatie, orkestratie en opslag, verbonden door open formaten. Deze modulariteit is zowel een geschenk als een valstrik. Ze laat je de beste tools van elk soort samenstellen, maar zonder engineeringdiscipline levert ze een wildgroei op van ongedocumenteerde, ongeteste jobs. Dit hoofdstuk behandelt de praktijken die pijplijnen idempotent, testbaar, observeerbaar en betaalbaar op schaal houden.

## Kernprincipes

- Pijplijnen zijn software en verdienen versiebeheer, testen, review en CI/CD.
- Geef de voorkeur aan idempotente, reproduceerbare transformaties die veilig opnieuw kunnen draaien.
- Maak datastromen observeerbaar: versheid, volume, schema en kwaliteit worden bewaakt.
- Modelleer data bewust voor haar afnemers in plaats van ruwe tabellen te dumpen.
- Kies batch of streaming op basis van echte latentiebehoeften, niet nieuwigheid.
- Optimaliseer opslagformaat, partitionering en rekenkosten als eersterangs zorgen.
- Scheid inname, transformatie en serving zodat elk onafhankelijk kan evolueren.
- Faal luid en vroeg. Een kapotte pijplijn is veiliger dan stilletjes foute data.

## Aanbevelingen

### Kies bewust tussen ETL en ELT

ETL transformeert data voordat ze in de bestemming wordt geladen. [ELT (extract, load, transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) laadt eerst ruwe data en transformeert haar binnen een krachtig warehouse of lakehouse. Moderne cloudplatformen hebben ELT de standaard gemaakt, omdat opslag goedkoop is en rekenkracht elastisch, en ruwe data houden je laat herverwerken wanneer logica verandert of bugs opduiken. Geef voor analyticswerklasten de voorkeur aan ELT: land ruwe onveranderlijke data en bouw er gelaagde transformaties op. Bewaar transformatie voor het laden voor gevallen waar privacy, kosten of contractuele beperkingen opschoning of filtering eisen voordat de data landt.

### Ontwerp batch- en streamingpijplijnen voor hun latentiebehoeften

De meeste analyticsbehoeften worden goed bediend door geplande batchpijplijnen, die makkelijker te beredeneren, testen en backfillen zijn. Grijp alleen naar streaming wanneer het bedrijf werkelijk data met lage latentie nodig heeft: fraudedetectie, operationele alarmering, realtimepersonalisatie. Streaming voegt echte complexiteit toe rond volgorde, exactly-oncesemantiek, laat aankomende data en toestandsbeheer. Overweeg waar je beide nodig hebt architecturen die batch- en streaminglogica verenigen in plaats van twee uiteenlopende codebases te onderhouden. Wees eerlijk over je latentie-eisen. "Realtime" is vaak een onbezonnen wens die je kosten verdubbelt.

### Orkestreer met expliciete afhankelijkheden

Gebruik een orkestrator om pijplijnen uit te drukken als [gerichte acyclische grafen (DAG's)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) van taken met expliciete afhankelijkheden, herpogingen en planning. Dit geeft je zicht op wat draaide, wat faalde en wat geblokkeerd is, plus het vermogen deterministisch te backfillen en opnieuw te draaien. Baseer afhankelijkheden op beschikbaarheid van data, niet alleen op kloktijd, zodat downstream-jobs op upstream-data wachten in plaats van op een gok af te gaan. Houd orkestratielogica in versiebeheer en behandel DAG-wijzigingen als codewijzigingen.

### Modelleer data voor gebruik

Ruwe tabellen zijn zelden geschikt voor analisten. Pas [dimensionale modellering](https://en.wikipedia.org/wiki/Dimensional_modeling) toe, die feiten en conformerende dimensies ordent in [sterschema's](https://en.wikipedia.org/wiki/Star_schema), waar je bestuurde, herbruikbare self-serviceanalytics nodig hebt. Brede gedenormaliseerde tabellen ("één grote tabel") kunnen beter presteren voor specifieke querypatronen en zijn eenvoudiger voor sommige afnemers, ten koste van duplicatie en flexibiliteit. Laag je transformaties: een ruwe stagelaag, een opgeschoonde en geconformeerde kernlaag en afnemergerichte marts. Deze scheiding laat je logica op één plek repareren en laat afnemers van stabiele interfaces afhangen.

### Maak pijplijnen idempotent en testbaar

Ontwerp transformaties zodat opnieuw draaien hetzelfde resultaat geeft, in plaats van data te dupliceren of te corrumperen, bijvoorbeeld met deterministische upserts op bedrijfsidentifiers en partition-overwritepatronen. Schrijf tests op meerdere niveaus: unittests voor transformatielogica, schematests en datatests die verwachtingen bevestigen zoals uniciteit, niet-lege sleutels, referentiële integriteit en toegestane waardebereiken. Draai deze in CI, zodat een slechte wijziging wordt gevangen voordat ze productiedata bereikt.

### Instrumenteer observeerbaarheid en betrouwbaarheid

Bewaak de vier kernsignalen van datagezondheid: versheid (is het actueel), volume (ligt het aantal rijen in het verwachte bereik), schema (is de structuur onverwacht veranderd) en verdeling (zijn waarden anomaal afgedreven). Alarmeer bij schendingen en leid ze naar het eigenaarsteam. Houd runbooks, bereikbaarheidsdiensten en schuldvrije nabeschouwingen voor dataincidenten, net zoals voor services. Volg herkomst, zodat je wanneer iets breekt de downstream-impact direct kunt zien.

### Optimaliseer opslag en kosten

Gebruik kolomgeoriënteerde open formaten zoals Parquet, of open tabelformaten die schema-evolutie, time travel en efficiënte updates ondersteunen. Partitioneer data op de kolommen waarop je het meest filtert, meestal datum, en vermijd een wildgroei aan kleine bestanden door te comprimeren. Scheid hete en koude data met gelaagde opslag en levenscyclusbeleid. Bewaak rekenuitgaven per pijplijn en per query. Op hol geslagen kosten komen meestal van volledige scans, ontbrekende partities en onbegrensde herverwerking. Behandel kosten als statistiek met eigenaren, niet als verrassing op de maandelijkse rekening.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| ELT (ter plekke transformeren) | Bewaart ruwe data, goedkope opslag, herverwerkbaar | Grote opslagvoetafdruk, governance nodig | Cloudanalytics |
| ETL (transformeren voor laden) | Beheerst kosten, filtert gevoelige data vroeg | Verliest ruwe data, moeilijker te herverwerken | Gereguleerde of beperkte ladingen |
| Batch | Eenvoudig, testbaar, makkelijk backfillen | Hogere latentie | De meeste analytics |
| Streaming | Lage latentie, realtime reactie | Complex, duur, moeilijk te testen | Fraude, operationele alarmering |
| Sterschema | Bestuurd, herbruikbaar, self-servicevriendelijk | Modelleerinspanning vooraf | Gedeelde BI |
| Brede tabel | Snel voor bekende queries, eenvoudig | Duplicatie, minder flexibel | Smal gebruik met hoge prestaties |

De dominante afweging is eenvoud tegenover latentie en flexibiliteit. Batch en ELT met gelaagde sterschema's geven je een testbaar, backfillbaar, goed begrepen systeem dat de meeste behoeften betaalbaar bedient. Streaming, realtime en sterk gedenormaliseerde ontwerpen kopen snelheid en specifieke prestaties, maar tegen een stevige prijs in operationele complexiteit en testmoeilijkheid. Neem complexiteit alleen aan waar een concrete bedrijfseis haar betaalt, en houd het eenvoudige pad je standaard.

## Vragen om met je team te bespreken

1. **Heb je bewust ELT boven ETL gekozen, en bewaar je ruwe onveranderlijke data zodat je kunt herverwerken wanneer logica verandert of bugs opduiken?** De standaard van het hoofdstuk is ELT: land ruwe data goedkoop en bouw er dan gelaagde transformaties op, omdat ruwe data houden je alles laat opnieuw draaien wanneer een regel verandert of een bug weken later opduikt. Ruwe data verwijderen sluit die optie af en is een gangbare, pijnlijke valkuil. Het concurrerende geval voor ETL is echt bij gereguleerde of beperkte ladingen, waar privacy, kosten of contractvoorwaarden filtering of maskering eisen voordat data landt. Neem bewijs mee: hoe vaak moest je geschiedenis herverwerken, en wat kostte het toen je dat niet kon? Voor een overheids- of ondernemingspijplijn die elk cijfer tot de bron moet kunnen herleiden zijn onveranderlijke ruwe records ook een controleerbaarheidseis, dus het antwoord bepaalt zowel je opslagbeleid als je juridische verdedigbaarheid.

2. **Welke van de vier datagezondheidssignalen bewaak je werkelijk, en wie wordt gebeld wanneer er een breekt?** Het hoofdstuk noemt vier signalen die het waard zijn te bewaken: versheid, volume, schema en verdeling. Veel teams bewaken er geen en horen van falen via een bestuurder die naar een verouderd dashboard staart, wat de slechtst mogelijke detector is. Op schaal van onderneming en overheid kan één stil falen foute data in betalingen, rapporten of publieke statistieken duwen, dus de kosten van late detectie worden gemeten in vertrouwen en geld, niet alleen herwerk. Neem je echte gemiddelde detectietijd mee en de naam van wie nu incidenten het eerst vindt. Als het antwoord "een afnemer" is, heb je alarmering nodig naar het eigenaarsteam plus runbooks en schuldvrije nabeschouwingen, dataincidenten precies als service-uitval behandelend.

3. **Consumeren je analisten gemodelleerde, geteste marts, of dump je ruwe tabellen op hen en noem je het self-service?** Het hoofdstuk is direct: ruwe tabellen zijn zelden geschikt voor analisten, en transformaties lagen in een ruwe stagelaag, een geconformeerde kern en afnemergerichte marts laat je logica eenmaal repareren en afnemers stabiele interfaces geven. De concurrerende trek is snelheid, aangezien modelleren met sterschema's of bewuste brede tabellen inspanning vooraf kost en het verleidelijk is het over te slaan. Maar ruwe data dumpen schuift de modelleerkosten herhaaldelijk naar elke analist, wat uiteenlopende getallen en verspilde uren produceert. Neem een signaal mee: welk deel van de analistentijd gaat naar het hervormen van ruwe data, en hoeveel teams hebben dezelfde joins opnieuw gebouwd. Als het getal hoog is, investeer dan in een geconformeerde kernlaag zodat afnemers van geteste, herbruikbare interfaces afhangen in plaats van ze opnieuw uit te vinden.

4. **Waar verdient "realtime" werkelijk zijn kosten, en waar is het een onbezonnen wens die stilletjes je operationele last verdubbelt?** De standaard van het hoofdstuk is geplande batch, die makkelijker te beredeneren, testen en backfillen is, met streaming gereserveerd voor gevallen waar het bedrijf werkelijk lage latentie nodig heeft, zoals fraudedetectie of operationele alarmering. De concurrerende trek is prestige en vage verzoeken van belanghebbenden om "live" data, die in een planningsvergadering goedkoop klinken en in productie duur worden, omdat streaming volgorde, exactly-oncesemantiek, laat aankomende data en toestandsbeheer meesleept, plus een tweede codebasis om synchroon te houden met de batchlogica. Neem bewijs mee naar de discussie: noem voor elke streamingpijplijn die je draait of voorstelt de beslissing die ze voedt en de latentie die die beslissing werkelijk verdraagt, gemeten in minuten of uren in plaats van bijvoeglijke naamwoorden. Voeg voor een groot platform van onderneming of overheid de bereikbaarheids- en testkosten van elk realtimepad toe, want een streamingpijplijn die niemand kan testen of rond de klok kan bemannen is een betrouwbaarheidsverplichting vermomd als functie, en het eerlijke antwoord klapt een "realtime"-eis vaak terug naar een uurlijkse batch die dezelfde beslissing dient.

5. **Welke van je pijplijnen kon vandaag niet veilig opnieuw worden gedraaid, en wat zou er nodig zijn om elke transformatie idempotent te maken?** Het hoofdstuk staat op idempotente, reproduceerbare transformaties, met deterministische upserts op bedrijfsidentifiers en partition-overwritepatronen, zodat een herrun hetzelfde resultaat geeft in plaats van data te dupliceren of te corrumperen. De concurrerende druk is leveringssnelheid, aangezien een naïeve append-only job sneller wordt opgeleverd dan een ontworpen om herdraaibaar te zijn, en de kosten van die sluiproute blijven verborgen tot een falen een gedeeltelijke herrun om 2 uur 's nachts afdwingt en iemand omzet dubbel telt. Neem een concrete inventaris mee: som de jobs op die data zouden corrumperen als ze vanaf een faalpunt opnieuw draaiden en schat de schadezone van de ergste. Op schaal van onderneming en overheid, waar één stil falen foute data in betalingen, rapporten of publieke statistieken kan duwen, is niet-idempotente verwerking niet slechts onhandig, het ondermijnt de controleerbaarheid waarmee je een periode na een regelwijziging kunt herverwerken en toch elk cijfer tot de bron kunt herleiden, dus het herwerk financieren om herruns veilig te maken is een beheersvraag, niet slechts een kwestie van netheid.

6. **Weet je wat elke pijplijn kost om te draaien, wie dat getal bezit en hoeveel van je cloudrekening komt van volledige scans en ontbrekende partities?** Het hoofdstuk behandelt opslagformaat, partitionering en rekenuitgaven als eersterangs zorgen met eigenaren en waarschuwt dat op hol geslagen kosten meestal terug te voeren zijn op volledige scans, ontbrekende partities en onbegrensde herverwerking. De concurrerende overweging is dat kostenwerk minder urgent voelt dan functies opleveren, dus het wordt uitgesteld tot de maandelijkse rekening een verrassing wordt en financiën vragen begint te stellen die engineering niet kan beantwoorden. Neem bewijs mee: uitgaven per pijplijn en per query, het aandeel van de kosten uit ongepartitioneerde scans en het aantal kleine bestanden dat gecomprimeerd moet worden. Voor een grote organisatie die miljarden records over veel bronsystemen draait groeit een eigenaarloze cloudrekening zonder dat enig team zich verantwoordelijk voelt, en bij de overheid moeten publieke uitgaven regel voor regel worden gerechtvaardigd, dus rekenkosten toewijzen aan een benoemde eigenaar met een gevolgde statistiek verandert een ondoorzichtige uitgave in een beheerde en onthult vaak besparingen groot genoeg om de volgende platforminvestering te financieren.

## Sectorperspectief

**Startup.** Snelheid verslaat architectuur. Bedraad inname aan een beheerde connector, bouw een handvol transformaties in versiebeheer en draai ze op een lichtgewicht orkestrator die zelf herprobeert en backfillt, in plaats van met de hand cronjobs te rollen die 's nachts stilletjes breken. Houd elk model vanaf de eerste commit idempotent en voeg een paar goedkope tests toe voor lege sleutels en rijaantallen, zodat een slechte bronwijziging in CI faalt in plaats van op het maandagse dashboard van de oprichter op te duiken. Zet geen streaming of maatwerkplatform op: je schaarse middel is engineeringaandacht.

**Kleinbedrijf.** Zonder aparte data-engineer geef je de voorkeur aan een geïntegreerde stack kopen boven er een samenstellen. Een beheerde ELT-dienst plus een cloudwarehouse geeft je connectoren, planning en opslag zonder platformteam om ze te onderhouden. Formuleer de keuze als datahygiëne in plaats van pijplijnproject: weet welke bronsystemen je rapporten voeden, bewaar ruwe data zodat een fout getal kan worden herleid en herverwerkt en kies tools met voorspelbare kosten zodat een volledige tabelscan het maandbudget niet opblaast.

**Grote onderneming.** Het probleem is consistentie over veel teams en miljarden records uit veel bronsystemen. Standaardiseer het ELT-patroon, het gelaagde stage-kern-martmodel en de vier datagezondheidssignalen zodat groepen ophouden kwetsbare pijplijnen opnieuw uit te vinden. Dwing datatests en CI af op elk model, wijs rekenkosten toe aan eigenaarsteams en laat dataincidenten door dezelfde bereikbaarheids-, runbook- en schuldvrije-nabeschouwingsdiscipline gaan die je voor services gebruikt, zodat een stil falen nooit ongemerkt een dashboard bereikt.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven de pijplijn vorm. Land onveranderlijke ruwe records voor controleerbaarheid, transformeer ze in gelaagde geteste stappen en houd volledige herkomst bij zodat een auditor elk gepubliceerd cijfer kan herleiden tot de brondocumenten, vaak een wettelijke eis. Idempotente verwerking laat je een aangifte of rapportageperiode veilig herverwerken wanneer een regel verandert, en de voorkeur geven aan open formaten en overdraagbare transformatiecode houdt je weg van lock-in bij één leverancier over een meerjarig contract.

## Voorbeelden

**Startup.** Een analytics-startup van tien personen had een kluwen cronjobs laten groeien die 's nachts stilletjes braken en soms rijen dubbel telden wanneer een engineer er met de hand een opnieuw draaide. Het team stapte over op een beheerde connector voor inname, een transformatieframework voor modellen in versiebeheer en een lichtgewicht orkestrator die zelf herprobeert en backfillt. Ze maakten elk model idempotent en voegden een handvol tests toe voor lege sleutels en rijaantallen, zodat een slechte bronwijziging nu in CI faalt in plaats van op het maandagse dashboard van de oprichter op te duiken.

**Grote onderneming.** Een wereldwijde retailer verving honderden met de hand geschreven extractiescripts door een ELT-stack. Beheerde connectoren landen ruwe brondata, een transformatieframework bouwt geteste modellen in versiebeheer in een lakehouse en een orkestrator beheert afhankelijkheden met herpogingen en backfills. Datatests vangen schema-afdrijving uit bronsystemen voordat ze dashboards bereikt. Gepartitioneerde kolomgeoriënteerde opslag verlaagde querykosten aanzienlijk, terwijl de versheid van dagelijks naar uurlijks verbeterde.

**Overheid.** Een belastingdienst neemt aangiften en data van derden in via een bestuurde pijplijn die onveranderlijke ruwe records landt voor controleerbaarheid en ze dan in gelaagde, geteste stappen transformeert. Idempotente verwerking laat hen een aangifteperiode veilig herverwerken wanneer een regel verandert. Volledige herkomst laat auditors elk berekend cijfer herleiden tot brondocumenten, een wettelijke eis voor publieke verantwoording.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van gedisciplineerde data-engineering komt uit betrouwbaarheid, snelheid en kostenbeheersing. Betrouwbare pijplijnen betekenen dat beslissingen en rapporten op betrouwbare data rusten, zodat je het dure herwerk en de reputatieschade van foute getallen vermijdt. Modulaire, geteste pijplijnen laten teams nieuwe dataproducten sneller opleveren, wat de waarde van elke analytics- en ML-investering stroomafwaarts opstapelt. Opslag en rekenkracht optimaliseren verlaagt direct de cloudrekening, vaak met grote marges zodra partitionering en querypatronen zijn gerepareerd.

De adoptiekosten omvatten platformtooling, engineeringtijd om geteste modulaire pijplijnen te bouwen en de discipline om data als software te behandelen. Weeg dit af tegen de kosten van niet adopteren: kwetsbare maatwerkjobs die alleen hun auteur begrijpt, stille datacorruptie ontdekt door bestuurders, oplopende cloudkosten door volledige tabelscans en analisten die op data staan te wachten. Formuleer data-engineering voor het bestuur als het fundament dat analytics, BI en AI betrouwbaar en betaalbaar maakt. Investeer je hier te weinig, dan begrens je het rendement van elk datainitiatief erboven.

## Antipatronen en valkuilen

- Pijplijnen gebouwd als eenmalige scripts zonder versiebeheer, tests of review.
- Niet-idempotente jobs die data dupliceren of corrumperen bij herrun na falen.
- Streaming overnemen voor prestige terwijl batch aan de latentie-eis voldeed.
- Ruwe tabellen op analisten dumpen en het self-service noemen.
- Geen observeerbaarheid, zodat falen door afnemers stroomafwaarts worden ontdekt.
- Partitionering en bestandsgrootte negeren tot de cloudrekening ontploft.
- Inname, transformatie en serving koppelen zodat niets veilig kan veranderen.
- Ruwe data verwijderen, wat herverwerken onmogelijk maakt wanneer logica verandert.

## Volwassenheidsmodel

1. Initiëren: Ad hoc scripts en handmatige runs, zonder tests of bewaking. Falen worden door afnemers stroomafwaarts ontdekt, jobs kunnen niet veilig opnieuw draaien en cloudkosten zijn onbeheerd en niet toegewezen.
2. Ontwikkelen: Sommige teams hebben een orkestrator overgenomen en basistransformaties in versiebeheer gezet, maar de praktijk is inconsistent over de organisatie. Af en toe bestaan tests, idempotentie is onregelmatig en kapotte pijplijnen betekenen nog steeds reactief brandjes blussen.
3. Standaardiseren: ELT met een gelaagd stage-kern-martmodel, getest en in versiebeheer, is de gedocumenteerde standaard toegepast over teams. Georkestreerde afhankelijkheden met herpogingen en backfills, datatests in CI en gedeelde conventies voor sterschemamodellering en partitionering worden organisatiebreed afgedwongen in plaats van aan elke groep overgelaten.
4. Beheersen: Het platform wordt gemeten en beheerst. Versheid, volume, schema en verdeling worden bewaakt met alarmen naar eigenaarsteams, en pijplijn-SLA's, gemiddelde detectietijd, slaagpercentages van datakwaliteit en rekenkosten per pijplijn en per query worden gevolgd tegen uitgangswaarden. Drempels voor terugdraaien en stopzetten worden afgedwongen op bewijs, en kosten en betrouwbaarheid hebben benoemde eigenaren die aan doelen worden gehouden.
5. Orkestreren: Pijplijnen worden volledig als software behandeld met CI/CD, datacontracten en geautomatiseerde anomaliedetectie die afdrijving vangt voordat afnemers dat doen. Batch- en streaminglogica worden verenigd waar latentie werkelijk loont, het platform wordt continu verbeterd en is self-service, en capaciteit, opslaglagen en kosten worden adaptief herbalanceerd naarmate werklasten verschuiven, zodat nieuwe dataproducten snel worden opgeleverd op een stabiel fundament.

## Ideeën voor discussie

- Waar in je stack verdient "realtime" werkelijk zijn kosten, en waar is het wensdenken?
- Welke pijplijnen kunnen vandaag niet veilig opnieuw draaien, en wat zou er nodig zijn om dat te repareren?
- Hoeveel van je clouddatarekening komt van volledige scans en ontbrekende partities?
- Consumeren je analisten gemodelleerde marts of ruwe tabellen, en wat kost ze dat?
- Wat is je gemiddelde detectietijd van een dataincident, en wie vindt het eerst?
- Zou batch- en streaminglogica verenigen je onderhoudslast verminderen of risico toevoegen?

## Belangrijkste inzichten

- Behandel pijplijnen als software: versiebeheer, tests, review, CI/CD en observeerbaarheid.
- Geef de voorkeur aan ELT met gelaagde, geteste modellen. Bewaar ruwe data voor herverwerking.
- Kies standaard batch en streaming alleen waar latentie werkelijk loont.
- Maak transformaties idempotent zodat herruns veilig zijn.
- Modelleer data voor afnemers met sterschema's of bewuste brede tabellen.
- Bewaak versheid, volume, schema en verdeling, en behandel dataincidenten als uitval.
- Optimaliseer opslagformaten, partitionering en rekenkosten als eersterangs zorgen.

## Referenties en verder lezen

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
