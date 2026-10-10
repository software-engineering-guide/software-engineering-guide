# 12.3 Sjablonen

Deze sjablonen zijn kopieerklare beginpunten. Til elk sjabloon in je wiki, repository of ticketsysteem en vul de placeholders tussen haken in. Cursieve notities en inline commentaar leggen uit wat in elke sectie hoort. Verwijder ze zodra de sectie is ingevuld. Houd sjablonen licht: een sjabloon dat sneller over te slaan is dan in te vullen zal niet worden gebruikt. Pas koppen en secties aan je organisatie aan, maar behoud de bedoeling van elk deel.

Een paar conventies die hieronder worden gebruikt:

- Tekst in `[vierkante haken]` is een placeholder om te vervangen.
- Tekst in _cursief_ of `<!-- commentaar -->` is richtlijn om te verwijderen.
- Houd het voltooide document zo kort als het kan zijn terwijl het zijn vragen nog beantwoordt.

## Architectuurbeslissingsrecord (ADR)

```markdown
# ADR [NNNN]: [Korte titel van de beslissing]

- Status: [Voorgesteld | Geaccepteerd | Verouderd | Vervangen door ADR-XXXX]
- Datum: [JJJJ-MM-DD]
- Beslissers: [namen of rollen]
- Geraadpleegd: [namen of rollen]

## Context

<!-- Wat is het probleem, de kracht of de beperking die deze beslissing
     drijft? Vermeld de feiten en eisen neutraal. Neem alleen op wat een
     toekomstige lezer nodig heeft om te begrijpen waarom een beslissing
     nodig was. -->

## Beslissing

<!-- Vermeld de keuze in een of twee heldere zinnen: "We zullen ..." -->

## Overwogen alternatieven

<!-- Som de realistische opties op die je woog en waarom elk wel of niet
     werd gekozen. Er moeten hier minstens twee alternatieven staan. -->

- Optie A: [samenvatting]; verworpen omdat [reden].
- Optie B: [samenvatting]; verworpen omdat [reden].
- Gekozen optie: [samenvatting]; gekozen omdat [reden].

## Gevolgen

<!-- Eerlijke resultaten van de beslissing, goed en slecht. -->

- Positief: [verkregen voordelen]
- Negatief: [kosten, risico's of beperkingen die worden aanvaard]
- Vervolg: [migraties, nieuw werk of beslissingen die dit triggert]

## Gerelateerd

<!-- Links naar eerdere ADR's, RFC's, tickets of documenten waarmee dit
     samenhangt. -->
```

## RFC / ontwerpdocument

```markdown
# RFC: [Titel]

- Auteur(s): [namen]
- Status: [Concept | In review | Goedgekeurd | Afgewezen | Geïmplementeerd]
- Reviewers: [namen of rollen]
- Aangemaakt: [JJJJ-MM-DD]
- Laatst bijgewerkt: [JJJJ-MM-DD]
- Ticket / tracking: [link]

## Samenvatting

<!-- Eén alinea: wat dit voorstelt en waarom het ertoe doet. Een lezer
     moet de essentie uit alleen deze sectie kunnen halen. -->

## Probleem en motivatie

<!-- Welk probleem lossen we op? Wie wordt geraakt? Wat gebeurt er als we
     niets doen? Neem relevante achtergrond en beperkingen op. -->

## Doelen en niet-doelen

- Doelen: [hoe succes eruitziet, waar mogelijk meetbaar]
- Niet-doelen: [expliciet buiten reikwijdte, om scope creep te voorkomen]

## Voorgesteld ontwerp

<!-- De kern van het document. Beschrijf de aanpak, architectuur,
     datamodel, interfaces en sleutelstromen. Gebruik diagrammen waar ze
     verhelderen. Leg uit hoe het werkt, niet alleen wat het is. -->

## Overwogen alternatieven

<!-- Andere aanpakken en waarom ze niet werden gekozen. Toont de lezer
     dat de ontwerpruimte werd verkend. -->

## Impact en risico's

- Beveiliging en privacy: [gevolgen en maatregelen]
- Prestaties en schaal: [verwachte belasting en gedrag]
- Beheerbaarheid: [bewaking, faalwijzen, uitrol, rollback]
- Kosten: [impact op infrastructuur of licenties]
- Achterwaartse compatibiliteit: [migratie en uitfasering]

## Test- en uitrolplan

<!-- Hoe de wijziging veilig wordt gevalideerd en uitgebracht. -->

## Open vragen

<!-- Onopgeloste kwesties waarover je reviewers wilt laten meewegen. -->
```

## Nabeschouwing / incidentreview (schuldvrij)

```markdown
# Nabeschouwing: [Incidenttitel]

- Incident-ID: [ID]
- Datum van het incident: [JJJJ-MM-DD]
- Auteurs: [namen]
- Status: [Concept | Definitief]
- Ernst: [SEV1 | SEV2 | SEV3]

> Deze review is schuldvrij. We richten ons op systemen en bijdragende
> factoren, niet op individuen. Het doel is te leren en herhaling te
> voorkomen.

## Samenvatting

<!-- Twee of drie zinnen: wat er gebeurde, de impact en de oplossing,
     leesbaar voor een niet-expert. -->

## Impact

- Duur: [begintijd tot hersteltijd, met tijdzone]
- Getroffen gebruikers: [reikwijdte en aantal]
- Bedrijfsimpact: [omzet, SLA, reputatie of anders]

## Tijdlijn

<!-- Feitelijke volgorde van gebeurtenissen met tijdstempels. Neem
     detectie, escalatie, sleutelacties en herstel op. -->

- [UU:MM] [gebeurtenis]
- [UU:MM] [gebeurtenis]

## Bijdragende factoren

<!-- De keten van omstandigheden die tot het incident leidde. Geef de
     voorkeur aan "bijdragende factoren" boven een enkele grondoorzaak. -->

## Detectie en respons

- Hoe werd het gedetecteerd? [alarm, klantmelding, enz.]
- Wat hielp de respons?
- Wat vertraagde de respons?

## Wat goed ging

<!-- Erken effectieve acties en waarborgen die werkten. -->

## Actiepunten

<!-- Specifiek, bezeten en gedateerd. Behandel preventie, detectie en
     beperking. Volg deze in de normale achterstand. -->

| Actie | Eigenaar | Vervaldatum | Type (voorkomen/detecteren/beperken) | Ticket |
|-------|----------|-------------|--------------------------------------|--------|
| [actie] | [naam] | [datum] | [type] | [link] |

## Geleerde lessen

<!-- Wat de bredere organisatie hieruit moet meenemen. -->
```

## Dreigingsmodel (op STRIDE gebaseerd)

```markdown
# Dreigingsmodel: [Naam van systeem of functie]

- Auteur(s): [namen]
- Datum: [JJJJ-MM-DD]
- Reviewers: [beveiligingscontact, eigenaren]
- Reikwijdte: [wat wel en niet wordt gedekt]

## Systeemoverzicht

<!-- Korte beschrijving van het systeem, haar doel en haar gebruikers. -->

## Bezittingen

<!-- Wat het beschermen waard is: data, inloggegevens, functionaliteit,
     reputatie. Noteer de gevoeligheid van elk. -->

## Vertrouwensgrenzen en datastroom

<!-- Beschrijf of diagrammeer componenten, datastores, externe entiteiten
     en de grenzen waar vertrouwen verandert. -->

## Dreigingen (STRIDE)

<!-- Overweeg voor elk element de STRIDE-categorieën. Leg elke
     geloofwaardige dreiging vast, haar risico en de maatregel of het
     geaccepteerde risico. -->

| Dreiging | STRIDE-categorie | Getroffen element | Risico (L/M/H) | Maatregel | Status |
|----------|------------------|-------------------|----------------|-----------|--------|
| [dreiging] | Spoofing | [element] | [risico] | [maatregel] | [open/beperkt/geaccepteerd] |
| [dreiging] | Tampering | [element] | [risico] | [maatregel] | [status] |
| [dreiging] | Repudiation | [element] | [risico] | [maatregel] | [status] |
| [dreiging] | Information disclosure | [element] | [risico] | [maatregel] | [status] |
| [dreiging] | Denial of service | [element] | [risico] | [maatregel] | [status] |
| [dreiging] | Elevation of privilege | [element] | [risico] | [maatregel] | [status] |

## Aannames en afhankelijkheden

<!-- Beveiligingsaannames waarop wordt geleund en externe maatregelen
     die worden vertrouwd. -->

## Open kwesties en vervolg

<!-- Dreigingen die verder werk vragen, gevolgd als tickets. -->
```

## Runbook

```markdown
# Runbook: [Naam van taak of scenario]

- Service: [servicenaam]
- Eigenaar: [team]
- Laatst beoordeeld: [JJJJ-MM-DD]
- Gerelateerde alarmen: [alarmnamen]

## Doel

<!-- Wanneer dit runbook te gebruiken en wat het bereikt. -->

## Voorwaarden

<!-- Toegang, tools en rechten die nodig zijn voor je begint. -->

## Detectie / symptomen

<!-- Wat de beheerder waarneemt: alarmen, foutsignaturen, dashboards. -->

## Diagnose

<!-- Stap-voor-stapcontroles om het probleem te bevestigen en de oorzaak
     te versmallen. Neem de exacte commando's, queries of
     dashboardlinks op. -->

1. [stap en verwacht resultaat]
2. [stap en verwacht resultaat]

## Oplossing

<!-- Concrete, geordende stappen om te repareren of te beperken. Noteer
     elke stap die riskant of onomkeerbaar is, en hoe je succes
     verifieert. -->

1. [stap]
2. [verifieer herstel]

## Rollback

<!-- Hoe je de acties ongedaan maakt als de oplossing het erger maakt. -->

## Escalatie

<!-- Wie te contacteren en wanneer te escaleren. Secundaire
     bereikbaarheid, eigenaarsteam en leverancierscontacten. -->

## Referenties

<!-- Dashboards, gerelateerde runbooks, architectuurdocumenten. -->
```

## Service-README / servicecatalogusvermelding

```markdown
# [Servicenaam]

- Eigenaarsteam: [team]
- Bereikbaarheid: [roosterlink]
- Laag / kritiekheid: [Laag 1 | 2 | 3]
- Repository: [link]
- Status: [Actief | Verouderd]

## Wat het doet

<!-- Eén alinea over de verantwoordelijkheid van de service en haar
     afnemers. -->

## Architectuur

<!-- Sleutelcomponenten, afhankelijkheden (upstream en downstream) en een
     link naar het ontwerpdocument of diagram. -->

## Interfaces

- API's / eindpunten: [link naar spec]
- Gepubliceerde / geconsumeerde gebeurtenissen: [topics]
- Datastores: [databases, caches, buckets]

## Runtime en deployment

- Omgevingen: [dev, staging, prod]
- Hoe te deployen: [pijplijnlink en proces]
- Configuratie en feature flags: [waar en hoe]

## Observeerbaarheid

- Dashboards: [links]
- Alarmen: [links]
- Logs: [waar te vinden]
- SLO's: [link]

## Beheer

- Runbooks: [links]
- Gangbare taken: [schalen, herstarten, backfill]
- Bekende problemen en beperkingen: [notities]

## Aan de slag (voor nieuwe bijdragers)

<!-- Hoe lokaal te bouwen, testen en draaien. -->

## Contacten

- Slack-/chatkanaal: [link]
- Escalatie: [pad]
```

## SLO- / foutbudgetbeleid

```markdown
# SLO- en foutbudgetbeleid: [Naam van service of reis]

- Eigenaar: [team]
- Ingangsdatum: [JJJJ-MM-DD]
- Beoordelingsritme: [bijv. per kwartaal]

## Service level indicators (SLI's)

<!-- Definieer elke SLI precies: de gemeten grootheid, hoe ze wordt
     gemeten en vanwaar (bij voorkeur vanuit het perspectief van de
     gebruiker). -->

| SLI | Definitie | Databron |
|-----|-----------|----------|
| Beschikbaarheid | [bijv. geslaagde verzoeken / totaal verzoeken] | [bron] |
| Latentie | [bijv. deel van verzoeken onder X ms] | [bron] |

## Doelstellingen (SLO's)

| SLI | Doel | Meetvenster |
|-----|------|-------------|
| Beschikbaarheid | [bijv. 99,9%] | [bijv. voortschrijdend 28 dagen] |
| Latentie | [bijv. 95% onder 300 ms] | [voortschrijdend 28 dagen] |

## Foutbudget

<!-- De toegestane onbetrouwbaarheid: 100% minus het doel, over het
     venster. Vermeld het budget in concrete termen (bijv.
     minuten/maand). -->

- Budget: [afgeleide toelage]

## Beleid wanneer het budget is uitgeput

<!-- De afgesproken gevolgen. Maak ze concreet en afdwingbaar. -->

- [bijv. Bevries niet-kritieke functiereleases tot het budget herstelt.]
- [bijv. Prioriteer betrouwbaarheidswerk in de volgende planningscyclus.]
- [bijv. Escaleer naar engineeringleiderschap als twee vensters op rij worden geschonden.]

## Beleid wanneer het budget gezond is

<!-- Welk extra risico het team mag nemen, bijv. snellere uitrol. -->

## Alarmering

<!-- Alarmen op verbrandingssnelheid en drempels gekoppeld aan deze SLO. -->
```

## Risicoregistervermelding

```markdown
## Risico: [Korte risicotitel]

- Risico-ID: [ID]
- Datum aangekaart: [JJJJ-MM-DD]
- Eigenaar: [naam of rol verantwoordelijk voor het beheren van dit risico]
- Categorie: [beveiliging | operationeel | compliance | financieel | oplevering | leverancier]
- Status: [Open | Beperken | Geaccepteerd | Gesloten]

### Beschrijving

<!-- Vermeld het risico als: oorzaak -> gebeurtenis -> gevolg. Wat er
     kan gebeuren en waarom het ertoe doet. -->

### Beoordeling

- Waarschijnlijkheid: [Laag | Middel | Hoog]
- Impact: [Laag | Middel | Hoog]
- Totaalbeoordeling: [afgeleid van waarschijnlijkheid x impact]

### Huidige maatregelen

<!-- Wat dit risico vandaag al vermindert. -->

### Beperkingsplan

<!-- Geplande acties om waarschijnlijkheid of impact te verminderen, met
     eigenaren en data. Leg bij het accepteren van het risico vast wie
     het accepteerde en waarom. -->

| Actie | Eigenaar | Vervaldatum | Status |
|-------|----------|-------------|--------|
| [actie] | [naam] | [datum] | [status] |

### Review

- Volgende reviewdatum: [JJJJ-MM-DD]
- Beslissing / notities: [enige acceptatieaftekening of wijziging]
```

## Projectoverzicht op één pagina / productbrief

```markdown
# [Project- of productnaam]: overzicht op één pagina

- Sponsor: [naam]
- Leider: [naam]
- Datum: [JJJJ-MM-DD]
- Status: [Idee | Goedgekeurd | In uitvoering | Uitgeleverd]

## Probleem

<!-- Eén alinea: het klant- of bedrijfsprobleem, en bewijs dat het echt
     is en het oplossen waard. -->

## Doelgroep

<!-- Wie dit probleem heeft en wie baat heeft bij het oplossen ervan. -->

## Voorgestelde oplossing

<!-- Een korte beschrijving van wat we gaan bouwen of veranderen. Houd
     het op het niveau van intentie, niet implementatiedetail. -->

## Waarom nu

<!-- De reden om dit nu te doen in plaats van later. -->

## Succesmaten

<!-- Hoe we weten dat het werkte. Geef de voorkeur aan meetbare
     uitkomsten. -->

- [statistiek en doel]

## Reikwijdte

- Binnen reikwijdte: [wat we gaan doen]
- Buiten reikwijdte: [wat we niet gaan doen]

## Risico's en open vragen

<!-- Belangrijkste onzekerheden en afhankelijkheden. -->

## Ruw plan en mijlpalen

<!-- Fasen op hoog niveau en ongeveer timing. -->

## Kosten en middelen

<!-- Benodigde mensen, tijd en budget. -->
```

## Overdrachtsnotities bereikbaarheid

```markdown
# Overdracht bereikbaarheid: [JJJJ-MM-DD]

- Vertrekkend: [naam]
- Aankomend: [naam]
- Service(s): [namen]

## Algemene status

<!-- Eén regel: rustig, rumoerig of lopend probleem. -->

## Open incidenten

<!-- Alle actieve of recent opgeloste incidenten die de volgende
     responder moet kennen, met links. -->

- [incident, status en wat er resteert]

## Lopende of geplande wijzigingen

<!-- Deploys, migraties, onderhoudsvensters of experimenten onderweg die
     alarmen kunnen veroorzaken. -->

## Lawaaierige of onbetrouwbare alarmen

<!-- Alarmen die afgingen en hun werkelijke betekenis, zodat de volgende
     persoon niet wordt misleid. Noteer tijdelijke onderdrukkingen en hun
     vervaldatum. -->

## Aandachtspunten

<!-- Statistieken of systemen die in een zorgwekkende richting trenden. -->

## Openstaande vervolgacties

<!-- Taken overgedragen aan de volgende dienst, met links naar tickets. -->

## Notities

<!-- Al het andere nuttige: toegangsquirks, leveranciersproblemen,
     context. -->
```

## Wijzigingsverzoek (voor gereguleerd wijzigingsbeheer)

```markdown
# Wijzigingsverzoek: [Titel van wijziging]

- Wijzigings-ID: [ID]
- Aanvrager: [naam]
- Datum ingediend: [JJJJ-MM-DD]
- Type: [Standaard | Normaal | Nood]
- Prioriteit: [Laag | Middel | Hoog]
- Status: [Ingediend | Goedgekeurd | Afgewezen | Geïmplementeerd | Gesloten]

## Beschrijving van de wijziging

<!-- Wat er verandert en waarom. Verwijs naar het ticket of de eis. -->

## Getroffen systemen en componenten

<!-- Services, data, omgevingen en gebruikers die worden geraakt. -->

## Rechtvaardiging en bedrijfsimpact

<!-- De reden voor de wijziging en de impact van het niet doen. -->

## Risicobeoordeling

- Risiconiveau: [Laag | Middel | Hoog]
- Mogelijke impact als de wijziging faalt: [beschrijving]
- Impact op beveiliging, privacy of compliance: [beschrijving]

## Implementatieplan

<!-- Geordende stappen, verantwoordelijke partijen en timing. -->

## Test- en validatieplan

<!-- Hoe succes vóór en na de wijziging wordt geverifieerd. -->

## Terugtrek- / rollbackplan

<!-- Hoe de wijziging wordt teruggedraaid als ze faalt, en de
     hersteltijd. -->

## Planning

- Voorgesteld venster: [begin en eind, met tijdzone]
- Verwachte downtime: [duur of geen]

## Goedkeuringen

| Rol | Naam | Beslissing | Datum |
|-----|------|------------|-------|
| Wijzigingseigenaar | [naam] | [goedkeuren/afwijzen] | [datum] |
| Technisch reviewer | [naam] | [goedkeuren/afwijzen] | [datum] |
| Wijzigingsadviesraad | [naam] | [goedkeuren/afwijzen] | [datum] |

## Review na implementatie

<!-- Uitkomst, ondervonden problemen en of terugtrekken nodig was. -->
```

## Schets voor gegevensbeschermingseffectbeoordeling (DPIA)

```markdown
# Gegevensbeschermingseffectbeoordeling: [Naam van verwerkingsactiviteit]

- Beoordelaar: [naam]
- Datum: [JJJJ-MM-DD]
- Reviewers: [FG / privacycontact]
- Status: [Concept | Beoordeeld | Goedgekeurd]

## 1. Beschrijving van de verwerking

<!-- Welke persoonsgegevens worden verwerkt, hoe, door wie en met welk
     doel. Neem datastromen van verzameling tot verwijdering op. -->

- Betrokkenen: [over wie de data gaat]
- Datacategorieën: [soorten persoonsgegevens, noteer bijzondere categorieën]
- Doelen: [waarom de data wordt verwerkt]
- Ontvangers en verwerkers: [wie de data ontvangt of afhandelt]
- Bewaartermijn: [hoe lang data wordt bewaard en verwijdermethode]
- Internationale doorgiften: [bestemmingen en overdrachtsmechanisme]

## 2. Noodzaak en evenredigheid

<!-- Is de verwerking noodzakelijk voor het doel? Is het de minst
     ingrijpende optie? Wat is de rechtsgrond of bevoegdheid? -->

- Rechtsgrond / bevoegdheid: [grondslag per doel]
- Dataminimalisatie: [waarom elk veld noodzakelijk is]
- Nauwkeurigheid en onderbouwing van bewaring: [notities]
- Hoe rechten van betrokkenen worden ondersteund: [inzage, verwijdering, enz.]

## 3. Raadpleging

<!-- Geraadpleegde belanghebbenden en, waar relevant, betrokkenen. -->

## 4. Risico's voor individuen

<!-- Identificeer privacyrisico's en beoordeel elk. -->

| Risico voor individuen | Waarschijnlijkheid | Ernst | Totaal |
|------------------------|--------------------|-------|--------|
| [bijv. ongeautoriseerde toegang tot gevoelige data] | [L/M/H] | [L/M/H] | [beoordeling] |

## 5. Maatregelen om risico te verminderen

<!-- Voor elk risico de beperking en het restrisico daarna. -->

| Risico | Maatregel | Restrisico | Geaccepteerd door |
|--------|-----------|------------|-------------------|
| [risico] | [maatregel] | [L/M/H] | [naam] |

## 6. Uitkomst en aftekening

- Restrisico aanvaardbaar: [Ja | Nee]
- Maatregelen goedgekeurd door: [naam, rol]
- Raadpleging van toezichthoudende autoriteit vereist: [Ja | Nee]
- Reviewdatum: [JJJJ-MM-DD]
```
