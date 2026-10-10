# 12.6 Invoeringsroutekaart

Deze bijlage is een praktische gids om de praktijken in dit boek *stapsgewijs* uit te
rollen. De belangrijkste instructie in het hele handboek, herhaald in elk hoofdstuk, is
**voer stapsgewijs in, geen big bang**. Een transformatie die alles tegelijk probeert te
veranderen, verandert niets duurzaam: ze put goodwill uit, overweldigt teams en stort in
bij de eerste crisis. Een transformatie die begint bij echte pijn, een zichtbare winst
levert en van daaruit samengestelde groei opbouwt, kan in een paar jaar een organisatie van
duizenden mensen in beweging brengen.

Deze routekaart geeft je principes voor invoering, een op volwassenheid gebaseerde volgorde
voor de eerste 90 dagen tot twee jaar en meer, een prioriteringskader met een uitgewerkt
voorbeeld, snelle winst per domein, speciale richtlijnen voor onderneming en overheid,
manieren om succes te meten en de faalwijzen die je moet vermijden.

## Principes van invoering

Deze principes gelden ongeacht je omvang, sector of beginvolwassenheid.

- **Begin bij pijn, niet bij een kader.** Zoek wat het meest pijn doet, of dat nu trage
  releases, frequente uitval, mislukte audits of verloop is, en los dat eerst op. Pijn
  creëert de vraag en de politieke dekking die een mandaat van bovenaf nooit kan geven.
  Niemand verzet zich tegen verlichting.
- **Gebaande wegen boven mandaten.** Maak de aanbevolen manier de *makkelijkste* manier.
  Een gouden pad dat sneller, veiliger en beter gedocumenteerd is, wint adoptie op eigen
  verdienste. Een beleid dat trager is dan de omweg, wordt omzeild. Investeer in de gebaande
  weg voordat je het zandpad afschaft.
- **Meet uitkomsten, geen activiteit.** Volg of de verandering de oplevering, betrouwbaarheid,
  beveiligingshouding of gebruikersuitkomsten heeft verbeterd, niet hoeveel teams een training
  volgden of een vakje aanvinkten. Instrumenteer voordat je verandert zodat je het effect kunt
  bewijzen.
- **Verwerf directiesponsoring en behoud die.** Duurzame verandering vraagt een
  verantwoordelijke bestuurder die financiering beschermt, blokkades wegneemt en standhoudt
  wanneer de transformatie ongemakkelijk wordt. Sponsoring is geen lanceringsevenement maar
  een doorlopende relatie die je met resultaten telkens opnieuw moet verdienen.
- **Vrijwilligers vóór dienstplichtigen.** Begin met teams die willen veranderen. Hun succes
  wordt het referentieverhaal dat de terughoudende meerderheid meetrekt. De weerstand eerst
  dwingen levert kwaadwillige naleving en waarschuwende verhalen op.
- **Maak het omkeerbaar waar het kan.** Geef de voorkeur aan veranderingen die je kunt
  uitproberen, meten en terugdraaien. Omkeerbare "tweewegdeur"-beslissingen mogen snel gaan.
  Bewaar zwaar proces voor het werkelijk onomkeerbare.
- **Toon winst vroeg en vaak.** Lever binnen weken iets zichtbaars, niet binnen kwartalen.
  Momentum is een hulpbron. Besteed de eerste winst om de volgende te financieren.
- **Ontmoet teams waar ze staan.** Eén volwassenheidslat die voor iedereen gelijk geldt is
  oneerlijk en ontmoedigend. Bepaal de volgorde naar de gereedheid en pijn van elk team.

## Volgorde op basis van volwassenheid

De horizonnen hieronder zijn cumulatief: elk bouwt voort op het vorige. Data zijn richtlijnen,
geen deadlines. Een grote of zwaar gereguleerde organisatie kan elke fase langer laten duren.
Het patroon (*stabiliseren, dan standaardiseren, dan opschalen, dan volhouden*) geldt
ongeacht het tempo.

### Eerste 90 dagen: stabiliseren en bewijzen

Doel: een basislijn vaststellen, een of twee vlaggenschipproblemen kiezen en met een
bereidwillig team een geloofwaardige eerste winst leveren.

- [ ] Benoem een verantwoordelijke directiesponsor en een kleine leidende coalitie.
- [ ] Leg de vier DORA-statistieken vast als basislijn (deployfrequentie, doorlooptijd,
      wijzigingsfaalpercentage, hersteltijd), ook als de getallen ruw zijn.
- [ ] Voer een lichte beoordeling uit tegen de volwassenheidsmodellen in hoofdstuk 12.4 om de
      grootste hiaten te vinden.
- [ ] Kies een of twee pilotteams die zich *aanmelden* en echte pijn hebben.
- [ ] Los één zichtbaar probleem van begin tot eind op (bijv. automatiseer de deployment van
      één team, of voeg SLO's toe aan één kritieke service).
- [ ] Richt een gedeeld beslissingsrecord (ADR's) in en een plek om resultaten te publiceren.
- [ ] Spreek af hoe je succes gaat meten *voordat* je iets verandert.

### Na 6 maanden: het winnende patroon standaardiseren

Doel: het succes van de pilot omzetten in een herhaalbaar, gedocumenteerd patroon en het
aanbieden als gebaande weg aan de volgende groep teams.

- [ ] Publiceer het gouden pad van de pilot als herbruikbare sjablonen, pijplijnen en
      documentatie.
- [ ] Richt een platform- of ondersteunend team op (desnoods een virtueel) dat de gebaande weg
      bezit en ondersteunt.
- [ ] Rol het patroon uit naar drie tot vijf teams meer, geprioriteerd naar impact en
      gereedheid.
- [ ] Voer geautomatiseerde kwaliteits- en beveiligingspoorten (linting, tests, SAST/SCA) in
      de gedeelde pijplijn in als standaard, niet als extra.
- [ ] Begin met een schuldvrije incidentreview en publiceer nabeschouwingen intern.
- [ ] Zet een lichte governancedialoog op (architectuurreview, rentmeesterschap van de gebaande
      weg) die deblokkeert in plaats van poortwachter te spelen.

### Na 12 maanden: opschalen over de organisatie

Doel: de gebaande weg de standaard maken voor het meeste nieuwe werk en beginnen met het
uitfaseren van de slechtste legacypraktijken.

- [ ] Vergroot het mandaat van het platformteam. Publiceer een servicecatalogus en
      scorekaarten.
- [ ] Stel organisatiebrede basislijnen vast: SLO's voor laag-1-services, beveiligingsmaatregelen
      in elke pijplijn, toegankelijkheidscontroles in frontendbuilds.
- [ ] Volg adoptiepercentages per team en maak de data zichtbaar.
- [ ] Begin met bewuste legacymodernisering op de systemen met het hoogste risico via
      strangler-fig- en branch-by-abstractionpatronen.
- [ ] Verweef meting met planning: teams beoordelen hun DORA- en betrouwbaarheidstrends in het
      normale bedrijfsritme.
- [ ] Investeer in toerusting (interne training, mentoring, praktijkgemeenschappen) zodat
      vermogen zich sneller verspreidt dan mandaten.

### Na 2+ jaar: volhouden en continu verbeteren

Doel: de praktijken zijn "hoe wij werken", geen programma, en de organisatie verbetert ze
zonder centrale duw.

- [ ] Beëindig het transformatieprogramma als benoemd initiatief. Bed het werk in normale
      governance en platformoperaties in.
- [ ] Behandel de gebaande weg als een product met een eigen roadmap, gebruikers en
      tevredenheidsstatistieken (enquêtes over ontwikkelaarservaring).
- [ ] Beheer technische schuld en modernisering als een doorlopend portfolio, niet als een
      eenmalige inspanning.
- [ ] Voer periodiek nieuwe volwassenheidsbeoordelingen uit en leg standaarden hoger naarmate
      de ondergrens stijgt.
- [ ] Bescherm tegen terugval: houd sponsoring, blijf meten en ververs praktijken naarmate
      technologie en dreigingen evolueren.

## Een prioriteringskader

Je hebt altijd meer verbeteringen dan capaciteit om ze te doen. Prioriteer met een eenvoudig,
verdedigbaar model in plaats van de luidste stem in de kamer.

Score elk kandidaat-initiatief op drie dimensies:

- **Impact (1–5):** Hoeveel verbetert dit een echte uitkomst (leveringssnelheid,
  betrouwbaarheid, beveiliging, kosten of gebruikerswaarde), en voor hoeveel teams of
  gebruikers?
- **Inspanning (1–5):** Hoeveel werk, coördinatie en verstoring kost het om te leveren?
  (Hoger = meer inspanning.)
- **Risicogewicht (0,5–2,0):** Een vermenigvuldiger voor urgentie en blootstelling.
  Beveiligings-, compliance- en veiligheidskwesties krijgen een hoger gewicht, prettige extra's
  een lager.

Een bruikbare rangschikkingsscore is:

```
Prioriteit = (Impact × Risicogewicht) ÷ Inspanning
```

Rangschik naar aflopende prioriteit. Zet de bovenste items in volgorde, maar houd altijd
minstens één snelle "quick win" met lage inspanning gaande om momentum vast te houden, en
herzie de scores elk kwartaal naarmate omstandigheden veranderen.

### Uitgewerkt voorbeeld

| Initiatief | Impact | Inspanning | Risicogewicht | Prioriteit | Volgorde |
|---|---|---|---|---|---|
| Automatiseer deployment voor de service met de hoogste omzet | 5 | 2 | 1,5 | 3,75 | Nu |
| Voeg SLO's en alarmering toe aan laag-1-services | 4 | 2 | 1,5 | 3,00 | Nu |
| Voer SAST/SCA in de gedeelde pijplijn in | 4 | 2 | 2,0 | 4,00 | Nu |
| Rol een designsysteem uit naar alle frontends | 4 | 5 | 1,0 | 0,80 | Later |
| Migreer mainframebatch naar de cloud | 5 | 5 | 1,5 | 1,50 | In fasen |
| Standaardiseer ADR's over teams | 3 | 1 | 1,0 | 3,00 | Nu (quick win) |
| Neem organisatiebreed een nieuwe programmeertaal aan | 2 | 5 | 0,5 | 0,20 | Uitstellen |

In dit voorbeeld staat het werk aan de beveiligingspijplijn bovenaan vanwege het hoge
risicogewicht en de bescheiden inspanning, terwijl de organisatiebrede taalwijziging ondanks
het enthousiasme onderaan belandt, omdat haar impact laag is en haar inspanning en verstoring
hoog zijn. Het kader maakt die afweging expliciet en bespreekbaar, en dat is haar echte
waarde.

## Snelle winst per domein

Elk deel van het boek heeft een goedkope eerste stap met een sterk signaal. Begin hier.

| Deel | Quick win om mee te "beginnen" |
|---|---|
| **Fundamenten (cultuur, teams, proces)** | Voer lichte ADR's in en houd één schuldvrije retrospective. Maak beslissingen en leren zichtbaar. |
| **Programmeervak** | Zet een automatische formatter en linter in CI aan als afgedwongen standaard, zodat stijl geen reviewonderwerp meer is. |
| **Architectuur** | Schrijf een beslissing van één pagina en een C4-contextdiagram voor je belangrijkste systeem. |
| **Beveiliging** | Voeg scannen van afhankelijkheden (SCA) en van geheimen toe aan de pijplijn. Schakel ze eerst in voor één kritieke repository. |
| **UX / ontwerp** | Houd drie goedkope usabilitytests op je drukste stroom. Los het grootste probleem op dat je ziet. |
| **AI / ML** | Schrijf een probleemkadering van één pagina en een datagereedheidscontrole voordat je enig modelwerk doet. Definieer hoe je succes evalueert. |
| **Data / analytics** | Definieer één afgesproken "noordster"-statistiek en één betrouwbaar dashboard. Schaf een tegenstrijdig dashboard af. |
| **DevOps / platform** | Breng één team naar een volledig geautomatiseerde build-test-deploypijplijn en documenteer die als sjabloon. |
| **Beheer / betrouwbaarheid** | Definieer SLI's en één SLO voor je meest kritieke gebruikersreis. Alarmeer op symptomen, niet op oorzaken. |
| **Onderneming / overheid** | Breng je huidige maatregelen in kaart tegen één kader (NIST CSF, ISO 27001 of SOC 2) en automatiseer het bewijs voor één maatregel. |

## Speciale richtlijnen voor onderneming

Grote gevestigde organisaties dragen schaal, veel teams, diepe legacy en zware overhead van
wijzigingsbeheer. Pas de routekaart daarop aan.

- **Federeer, centraliseer niet alles.** Eén centraal team kan geen honderden productteams
  bedienen. Gebruik een platformteam voor gebaande wegen en ondersteunende teams om te
  coachen, terwijl productteams eigenaar blijven. (Zie Team Topologies.)
- **Respecteer de wet van Conway.** Je architectuur zal je organogram weerspiegelen. Als je
  ontkoppelde services wilt, heb je ontkoppelde, bekrachtigde teams nodig. Reorganiseer
  bewust in plaats van tegen de draad in te gaan.
- **Behandel legacy als portfolio.** Je kunt niet alles moderniseren. Rangschik legacysystemen
  naar risico en bedrijfswaarde en pas strangler-fig-migratie toe op de weinige die ertoe
  doen. Bevries of beëindig de rest bewust.
- **Verandermanagement is echt werk.** Op schaal zijn communicatie, training en afstemming van
  prikkels geen overhead: ze zijn de transformatie. Begroot expliciet voor toerusting,
  praktijkgemeenschappen en interne evangelisatie.
- **Pas op voor de mandaatreflex.** Grote organisaties vallen terug op beleidsmemo's. Weersta.
  Een mandaat zonder gebaande weg levert vinkjes op. Een gebaande weg zonder mandaat levert
  echte adoptie op.
- **Stem prikkels en financiering af.** Verschuif van projectfinanciering naar duurzame
  productteams zodat verbeteringen de einddatum van een project overleven. Beloon uitkomsten,
  geen output.

## Speciale richtlijnen voor overheid

Organisaties in de publieke sector voegen inkoopcycli, compliancepoorten, aannemersbeheer,
meerjarige financiering en transparantieverplichtingen toe. Dit zijn ontwerpinvoer, geen
excuses.

- **Ontwerp vanaf dag één voor de ATO.** Poorten voor authorisation to operate en continue
  bewaking (volgens NIST RMF / 800-37) kunnen de doorlooptijd domineren. Bouw
  beveiligingsmaatregelen en bewijsverzameling vroeg in de pijplijn zodat compliance continu
  is, geen late, blokkerende haastklus.
- **Koop stapsgewijs in.** Meerjarige big-bang-aanbestedingen institutionaliseren het
  big-bangfalen waartegen dit boek waarschuwt. Geef de voorkeur aan modulaire contractering,
  kleinere gunningen en op uitkomsten gebaseerde opdrachtomschrijvingen die iteratie toelaten.
- **Beheer leveranciers en integrators als onderdeel van het team.** Veel
  overheidsengineering wordt door aannemers geleverd. Schrijf gebaande wegen, kwaliteitspoorten
  en transparantie-eisen in contracten en zorg dat kennis en code naar de overheid
  overgaan om afhankelijkheid en bus-factorrisico te vermijden.
- **Plan rond financieringscycli.** Meerjarige en jaarlijkse begrotingen beperken waaraan je je
  kunt verbinden. Orden werk zodat elke gefinancierde stap op zichzelf waarde levert en je niet
  halverwege de transformatie laat steken als financiering verschuift.
- **Toegankelijkheid en gewone taal zijn wettelijke verplichtingen.** Section 508, de ADA, WCAG
  en mandaten voor gewone taal zijn eisen, geen verbeteringen. Bak toegankelijkheidscontroles
  in pijplijnen en contentreview in de workflow.
- **Transparantie is een functie.** Woo (Wet open overheid), open-sourcemandaten ("publiek geld, publieke
  code") en gepubliceerde dienststandaarden betekenen dat je werk onderhevig is aan publieke
  toetsing. Ontwerp ervoor: heldere records, open waar gepast en eerlijke gepubliceerde
  prestatiedata.
- **Volg bewezen patronen uit de publieke sector.** De U.S. Digital Services Playbook, de
  GOV.UK Service Standard en USWDS bevatten zwaar bevochten lessen. Neem ze over in plaats van
  opnieuw uit te vinden.

## Het succes van invoering meten

Meet zowel *voorlopende* indicatoren (vroege signalen dat de verandering aanslaat) als
*achterlopende* indicatoren (de uitkomsten waar het uiteindelijk om gaat). Let op de trend,
niet op één meting, en laat een statistiek nooit een doel worden dat wordt bespeeld.

| Type | Indicator | Wat het je vertelt |
|---|---|---|
| Voorlopend | Aantal teams op de gebaande weg | Hoe snel de adoptie zich verspreidt |
| Voorlopend | Dekking van pijplijnpoorten (tests, SAST, toegankelijkheid) | Hoe ingebed kwaliteit/beveiliging zijn geraakt |
| Voorlopend | Scores van enquêtes over ontwikkelaarservaring | Of de gebaande weg werkelijk helpt |
| Voorlopend | Percentage beslissingen vastgelegd als ADR's | Of de schrijf-/leercultuur echt is |
| Achterlopend | Deployfrequentie (DORA) | Leveringsdoorvoer |
| Achterlopend | Doorlooptijd van wijzigingen (DORA) | Snelheid van commit tot productie |
| Achterlopend | Wijzigingsfaalpercentage (DORA) | Kwaliteit van het leveringsproces |
| Achterlopend | Tijd tot herstel van de dienst (DORA) | Operationele weerbaarheid |
| Achterlopend | Trend in incidentfrequentie en ernst | Betrouwbaarheidsverbetering in de tijd |
| Achterlopend | Auditbevindingen / maatregelfalen | Compliancehouding |
| Achterlopend | Behoud en verloop | Of de cultuur verbetert |

De vier DORA-statistieken zijn de meest gevalideerde uitkomstmaten voor oplevering over
sectoren heen. Behandel verbetering op alle vier samen als het kopsignaal en bescherm je
ertegen dat je de een verbetert ten koste van de ander.

## Veelvoorkomende faalwijzen en hoe je ze vermijdt

| Faalwijze | Hoe het eruitziet | Hoe je het vermijdt |
|---|---|---|
| **Big-bang-uitrol** | Alles voor iedereen tegelijk veranderen. Het programma stort in onder zijn eigen gewicht. | Orden naar pijn en gereedheid. Pilot, bewijs, schaal dan op. |
| **Mandaat zonder gebaande weg** | Beleid eist de nieuwe manier, maar de nieuwe manier is trager. Teams voldoen op papier en omzeilen het. | Bouw eerst het makkelijkere, betere pad. Verdien adoptie op verdienste. |
| **Een kader kopiëren zonder begrip** | SAFe, het Spotify-model of de structuur van een andere organisatie kopiëren zonder hun context. | Begin bij je eigen pijn en principes. Pas aan, verplant niet. |
| **Activiteit meten, geen uitkomsten** | Voltooide trainingen en afgevinkte vakjes vieren terwijl oplevering en betrouwbaarheid niet bewegen. | Instrumenteer uitkomsten (DORA, incidenten, gebruikerswaarde) vanaf het begin. |
| **Tool-eerst-transformatie** | Een platform kopen en verwachten dat cultuur volgt. | Begin met praktijken en gebaande wegen. Tools dienen die, niet andersom. |
| **Sponsoring verliezen** | De directiekampioen vertrekt of haakt af. Het programma stagneert. | Institutionaliseer de verandering in normale governance. Bouw een coalitie, geen single point of failure. |
| **Ijdele statistieken en bespelen** | Dekkings- of velocitygetallen stijgen terwijl kwaliteit daalt. | Gebruik statistieken als signalen met balancerende metingen, nooit als enige doelen. |
| **De oceaan koken op legacy** | Alles proberen te moderniseren en niets opleveren. | Rangschik naar risico en waarde. Wurg de kritieke paar, bevries de rest. |
| **Transformatiemoeheid** | Eindeloze verandering zonder zichtbare opbrengst. Teams haken af. | Lever vroege winst. Bescherm een houdbaar tempo. Laat het programma eindigen en gewoon werk worden. |
| **Het organogram negeren** | Nieuwe architectuur vecht tegen de bestaande teamstructuur. | Pas de omgekeerde Conway-manoeuvre toe: vorm teams naar de architectuur die je wilt. |

## De kortst mogelijke versie

Als je niets anders onthoudt uit deze bijlage:

1. Zoek de grootste pijn en los die op met een bereidwillig team.
2. Maak van die oplossing een gebaande weg die werkelijk makkelijker is dan de oude manier.
3. Meet de uitkomst, toon de winst en gebruik die om de volgende stap te financieren.
4. Herhaal en verbreed de kring tot de gebaande weg gewoon is hoe je werkt.
5. Behoud sponsoring, blijf meten en doe nooit een big bang.

Zie **hoofdstuk 12.4** voor de volwassenheidsmodellen die de beoordelingen verankeren, en
**hoofdstuk 12.2** voor de checklists voor lancering, review en audit die elke stap
operationaliseren.
