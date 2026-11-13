# 12.3 Skabeloner

Disse skabeloner er kopiér-og-indsæt-klare udgangspunkter. Løft en hvilken som helst skabelon ind i jeres wiki, repository eller ticketsystem, og udfyld pladsholderne i firkantede parenteser. Kursiverede noter og kommentarer i teksten forklarer, hvad der hører hjemme i hvert afsnit; slet dem, når afsnittet er udfyldt. Hold skabeloner lette: en skabelon, der er hurtigere at springe over end at udfylde, bliver ikke brugt. Tilpas overskrifter og afsnit til jeres organisation, men bevar hensigten med hver del.

Nogle få konventioner brugt nedenfor:

- Tekst i `[firkantede parenteser]` er en pladsholder, der skal erstattes.
- Tekst i _kursiv_ eller `<!-- kommentarer -->` er vejledning, der skal slettes.
- Hold det færdige dokument så kort, som det kan være, mens det stadig besvarer sine spørgsmål.

## Architecture Decision Record (ADR)

```markdown
# ADR [NNNN]: [Kort titel på beslutningen]

- Status: [Foreslået | Accepteret | Udfaset | Afløst af ADR-XXXX]
- Dato: [ÅÅÅÅ-MM-DD]
- Beslutningstagere: [navne eller roller]
- Hørt: [navne eller roller]

## Kontekst

<!-- Hvad er det problem, den kraft eller begrænsning, der driver denne
     beslutning? Angiv fakta og krav neutralt. Medtag kun, hvad en
     fremtidig læser har brug for for at forstå, hvorfor en beslutning
     var nødvendig. -->

## Beslutning

<!-- Angiv valget i en eller to klare sætninger: "Vi vil ..." -->

## Overvejede alternativer

<!-- List de realistiske muligheder, I afvejede, og hvorfor hver blev
     eller ikke blev valgt. Mindst to alternativer bør optræde her. -->

- Mulighed A: [resumé]; afvist, fordi [grund].
- Mulighed B: [resumé]; afvist, fordi [grund].
- Valgt mulighed: [resumé]; valgt, fordi [grund].

## Konsekvenser

<!-- Ærlige resultater af beslutningen, både gode og dårlige. -->

- Positivt: [opnåede fordele]
- Negativt: [omkostninger, risici eller begrænsninger, der accepteres]
- Opfølgning: [migreringer, nyt arbejde eller beslutninger, denne udløser]

## Relateret

<!-- Links til tidligere ADR'er, RFC'er, tickets eller dokumenter,
     denne relaterer til. -->
```

## RFC / designdokument

```markdown
# RFC: [Titel]

- Forfatter(e): [navne]
- Status: [Udkast | Under gennemgang | Godkendt | Afvist | Implementeret]
- Gennemgængere: [navne eller roller]
- Oprettet: [ÅÅÅÅ-MM-DD]
- Sidst opdateret: [ÅÅÅÅ-MM-DD]
- Ticket / sporing: [link]

## Resumé

<!-- Ét afsnit: hvad dette foreslår, og hvorfor det betyder noget. En
     læser bør kunne fatte essensen fra dette afsnit alene. -->

## Problem og motivation

<!-- Hvilket problem løser vi? Hvem er berørt? Hvad sker der, hvis vi
     ikke gør noget? Medtag relevant baggrund og begrænsninger. -->

## Mål og ikke-mål

- Mål: [hvordan succes ser ud, målbart hvor det er muligt]
- Ikke-mål: [eksplicit uden for omfanget, for at forhindre omfangsskred]

## Foreslået design

<!-- Dokumentets kerne. Beskriv tilgangen, arkitekturen, datamodellen,
     grænsefladerne og de vigtigste flow. Brug diagrammer, hvor de
     afklarer. Forklar, hvordan det virker, ikke blot hvad det er. -->

## Overvejede alternativer

<!-- Andre tilgange og hvorfor de ikke blev valgt. Viser læseren, at
     designrummet blev udforsket. -->

## Konsekvenser og risici

- Sikkerhed og privatliv: [konsekvenser og afbødninger]
- Ydeevne og skala: [forventet belastning og adfærd]
- Driftsegnethed: [overvågning, fejlformer, udrulning, tilbagerulning]
- Omkostning: [konsekvens for infrastruktur eller licenser]
- Bagudkompatibilitet: [migrering og udfasning]

## Test- og udrulningsplan

<!-- Hvordan ændringen vil blive valideret og udgivet sikkert. -->

## Åbne spørgsmål

<!-- Uafklarede spørgsmål, I vil have gennemgængere til at tage stilling
     til. -->
```

## Postmortem / hændelsesgennemgang (skyldfri)

```markdown
# Postmortem: [Hændelsestitel]

- Hændelses-ID: [ID]
- Hændelsesdato: [ÅÅÅÅ-MM-DD]
- Forfattere: [navne]
- Status: [Udkast | Endelig]
- Alvorlighed: [SEV1 | SEV2 | SEV3]

> Denne gennemgang er skyldfri. Vi fokuserer på systemer og medvirkende
> faktorer, ikke på enkeltpersoner. Målet er at lære og at forhindre
> gentagelse.

## Resumé

<!-- To eller tre sætninger: hvad der skete, påvirkningen og løsningen,
     læsbart for en ikke-ekspert. -->

## Påvirkning

- Varighed: [starttidspunkt til genoprettelsestidspunkt, med tidszone]
- Berørte brugere: [omfang og antal]
- Forretningspåvirkning: [omsætning, SLA, omdømme eller andet]

## Tidslinje

<!-- Tidsstemplet, faktuel rækkefølge af begivenheder. Medtag detektion,
     eskalering, vigtige handlinger og genoprettelse. -->

- [TT:MM] [begivenhed]
- [TT:MM] [begivenhed]

## Medvirkende faktorer

<!-- Kæden af betingelser, der førte til hændelsen. Foretræk
     "medvirkende faktorer" frem for en enkelt rodårsag. -->

## Detektion og respons

- Hvordan blev den opdaget? [alarm, kunderapport osv.]
- Hvad hjalp responsen?
- Hvad forsinkede responsen?

## Hvad gik godt

<!-- Anerkend effektive handlinger og sikkerhedsforanstaltninger, der
     virkede. -->

## Handlingspunkter

<!-- Specifikke, ejede og daterede. Adressér forebyggelse, detektion og
     afbødning. Følg dem i det normale efterslæb. -->

| Handling | Ejer | Forfaldsdato | Type (forebyg/opdag/afbød) | Ticket |
|----------|------|--------------|----------------------------|--------|
| [handling] | [navn] | [dato] | [type] | [link] |

## Erfaringer

<!-- Hvad den bredere organisation bør tage med sig. -->
```

## Trusselsmodel (STRIDE-baseret)

```markdown
# Trusselsmodel: [System- eller funktionsnavn]

- Forfatter(e): [navne]
- Dato: [ÅÅÅÅ-MM-DD]
- Gennemgængere: [sikkerhedskontakt, ejere]
- Omfang: [hvad der er og ikke er dækket]

## Systemoverblik

<!-- Kort beskrivelse af systemet, dets formål og dets brugere. -->

## Aktiver

<!-- Hvad der er værd at beskytte: data, legitimationsoplysninger,
     funktionalitet, omdømme. Notér følsomheden af hver. -->

## Tillidsgrænser og dataflow

<!-- Beskriv eller diagrammér komponenter, datalagre, eksterne
     entiteter og de grænser, hvor tilliden ændrer sig. -->

## Trusler (STRIDE)

<!-- For hvert element, overvej STRIDE-kategorierne. Registrér hver
     troværdig trussel, dens risiko og afbødningen eller den accepterede
     risiko. -->

| Trussel | STRIDE-kategori | Berørt element | Risiko (L/M/H) | Afbødning | Status |
|---------|-----------------|----------------|----------------|-----------|--------|
| [trussel] | Spoofing | [element] | [risiko] | [kontrol] | [åben/afbødet/accepteret] |
| [trussel] | Tampering | [element] | [risiko] | [kontrol] | [status] |
| [trussel] | Repudiation | [element] | [risiko] | [kontrol] | [status] |
| [trussel] | Information disclosure | [element] | [risiko] | [kontrol] | [status] |
| [trussel] | Denial of service | [element] | [risiko] | [kontrol] | [status] |
| [trussel] | Elevation of privilege | [element] | [risiko] | [kontrol] | [status] |

## Antagelser og afhængigheder

<!-- Sikkerhedsantagelser, der støttes på, og eksterne kontroller, der
     stoles på. -->

## Åbne problemer og opfølgning

<!-- Trusler, der kræver mere arbejde, sporet som tickets. -->
```

## Runbook

```markdown
# Runbook: [Opgave- eller scenarienavn]

- Tjeneste: [tjenestenavn]
- Ejer: [team]
- Sidst gennemgået: [ÅÅÅÅ-MM-DD]
- Relaterede alarmer: [alarmnavne]

## Formål

<!-- Hvornår denne runbook bruges, og hvad den opnår. -->

## Forudsætninger

<!-- Adgang, værktøjer og tilladelser, der er nødvendige, før man
     begynder. -->

## Detektion / symptomer

<!-- Hvad operatøren observerer: alarmer, fejlsignaturer, dashboards. -->

## Diagnose

<!-- Trin-for-trin-tjek for at bekræfte problemet og indsnævre årsagen.
     Medtag de præcise kommandoer, forespørgsler eller dashboardlinks. -->

1. [trin og forventet resultat]
2. [trin og forventet resultat]

## Løsning

<!-- Konkrete, ordnede trin til at rette eller afbøde. Notér ethvert
     trin, der er risikabelt eller uigenkaldeligt, og hvordan succes
     verificeres. -->

1. [trin]
2. [verificér genoprettelse]

## Tilbagerulning

<!-- Hvordan handlingerne fortrydes, hvis løsningen gør tingene værre. -->

## Eskalering

<!-- Hvem der skal kontaktes, og hvornår der skal eskaleres. Sekundær
     vagt, ejende team og leverandørkontakter. -->

## Referencer

<!-- Dashboards, relaterede runbooks, arkitekturdokumenter. -->
```

## Service-README / servicekatalogindgang

```markdown
# [Servicenavn]

- Ejende team: [team]
- Vagt: [link til rotation]
- Niveau / kritikalitet: [Niveau 1 | 2 | 3]
- Repository: [link]
- Status: [Aktiv | Udfaset]

## Hvad den gør

<!-- Ét afsnit om tjenestens ansvar og dens forbrugere. -->

## Arkitektur

<!-- Nøglekomponenter, afhængigheder (opstrøms og nedstrøms) og et link
     til designdokumentet eller diagrammet. -->

## Grænseflader

- API'er / endepunkter: [link til specifikation]
- Hændelser udgivet / forbrugt: [emner]
- Datalagre: [databaser, caches, buckets]

## Kørselstid og udrulning

- Miljøer: [dev, staging, prod]
- Sådan udrulles: [pipelinelink og proces]
- Konfiguration og feature flags: [hvor og hvordan]

## Observerbarhed

- Dashboards: [links]
- Alarmer: [links]
- Logs: [hvor de findes]
- SLO'er: [link]

## Drift

- Runbooks: [links]
- Almindelige opgaver: [skalering, genstart, efterfyldning]
- Kendte problemer og begrænsninger: [noter]

## Kom i gang (for nye bidragydere)

<!-- Hvordan man bygger, tester og kører lokalt. -->

## Kontakter

- Slack / chatkanal: [link]
- Eskalering: [sti]
```

## SLO- / fejlbudgetpolitik

```markdown
# SLO- og fejlbudgetpolitik: [Tjeneste- eller rejsenavn]

- Ejer: [team]
- Ikrafttrædelsesdato: [ÅÅÅÅ-MM-DD]
- Gennemgangskadence: [f.eks. kvartalsvis]

## Serviceindikatorer (SLI'er)

<!-- Definér hver SLI præcist: den målte størrelse, hvordan den måles,
     og hvorfra (ideelt fra brugerens perspektiv). -->

| SLI | Definition | Datakilde |
|-----|-----------|-----------|
| Tilgængelighed | [f.eks. vellykkede forespørgsler / samlede forespørgsler] | [kilde] |
| Latens | [f.eks. andel af forespørgsler under X ms] | [kilde] |

## Mål (SLO'er)

| SLI | Mål | Måleperiode |
|-----|-----|-------------|
| Tilgængelighed | [f.eks. 99,9 %] | [f.eks. rullende 28 dage] |
| Latens | [f.eks. 95 % under 300 ms] | [rullende 28 dage] |

## Fejlbudget

<!-- Den tilladte upålidelighed: 100 % minus målet, over perioden.
     Angiv budgettet i konkrete termer (f.eks. minutter/måned). -->

- Budget: [udledt tilladelse]

## Politik, når budgettet er opbrugt

<!-- De aftalte konsekvenser. Gør dem konkrete og håndhævbare. -->

- [f.eks. Frys ikke-kritiske funktionsreleases, til budgettet genoprettes.]
- [f.eks. Prioritér pålidelighedsarbejde i den næste planlægningscyklus.]
- [f.eks. Eskalér til ingeniørledelsen, hvis brudt to perioder i træk.]

## Politik, når budgettet er sundt

<!-- Hvilken ekstra risiko teamet må tage, f.eks. hurtigere udrulninger. -->

## Alarmering

<!-- Alarmer på forbrændingsrate og tærskler knyttet til denne SLO. -->
```

## Risikoregisterindgang

```markdown
## Risiko: [Kort risikotitel]

- Risiko-ID: [ID]
- Dato rejst: [ÅÅÅÅ-MM-DD]
- Ejer: [navn eller rolle ansvarlig for at styre denne risiko]
- Kategori: [sikkerhed | drift | compliance | økonomi | levering | leverandør]
- Status: [Åben | Afbødes | Accepteret | Lukket]

### Beskrivelse

<!-- Angiv risikoen som: årsag -> hændelse -> konsekvens. Hvad der kunne
     ske, og hvorfor det betyder noget. -->

### Vurdering

- Sandsynlighed: [Lav | Middel | Høj]
- Konsekvens: [Lav | Middel | Høj]
- Samlet vurdering: [udledt af sandsynlighed x konsekvens]

### Nuværende kontroller

<!-- Hvad der allerede reducerer denne risiko i dag. -->

### Afbødningsplan

<!-- Planlagte handlinger til at reducere sandsynlighed eller
     konsekvens, med ejere og datoer. Hvis risikoen accepteres, så
     registrér hvem der accepterede den og hvorfor. -->

| Handling | Ejer | Forfaldsdato | Status |
|----------|------|--------------|--------|
| [handling] | [navn] | [dato] | [status] |

### Gennemgang

- Næste gennemgangsdato: [ÅÅÅÅ-MM-DD]
- Beslutning / noter: [enhver godkendelse af accept eller ændring]
```

## Projekt-one-pager / produktbrief

```markdown
# [Projekt- eller produktnavn]: one-pager

- Sponsor: [navn]
- Leder: [navn]
- Dato: [ÅÅÅÅ-MM-DD]
- Status: [Idé | Godkendt | I gang | Leveret]

## Problem

<!-- Ét afsnit: kunde- eller forretningsproblemet og dokumentation for,
     at det er reelt og værd at løse. -->

## Målgruppe

<!-- Hvem har dette problem, og hvem drager fordel af at løse det. -->

## Foreslået løsning

<!-- En kort beskrivelse af, hvad vi vil bygge eller ændre. Hold det på
     niveau med hensigt, ikke implementeringsdetaljer. -->

## Hvorfor nu

<!-- Grunden til at gøre dette nu frem for senere. -->

## Succesmålinger

<!-- Hvordan vi ved, at det virkede. Foretræk målbare udfald. -->

- [måling og mål]

## Omfang

- Inden for omfanget: [hvad vi vil gøre]
- Uden for omfanget: [hvad vi ikke vil gøre]

## Risici og åbne spørgsmål

<!-- Hovedusikkerheder og afhængigheder. -->

## Grov plan og milepæle

<!-- Højniveaufaser og omtrentlig timing. -->

## Omkostning og ressourcer

<!-- Mennesker, tid og budget, der kræves. -->
```

## Vagtoverdragelsesnoter

```markdown
# Vagtoverdragelse: [ÅÅÅÅ-MM-DD]

- Afgående: [navn]
- Kommende: [navn]
- Tjeneste(r): [navne]

## Overordnet status

<!-- Én linje: stille, støjende eller igangværende problem. -->

## Åbne hændelser

<!-- Alle aktive eller nyligt løste hændelser, den næste ansvarlige
     skal kende til, med links. -->

- [hændelse, status og hvad der er tilbage]

## Igangværende eller planlagte ændringer

<!-- Udrulninger, migreringer, vedligeholdelsesvinduer eller
     eksperimenter undervejs, der kan forårsage alarmer. -->

## Støjende eller ustabile alarmer

<!-- Alarmer, der udløstes, og deres reelle betydning, så den næste
     ikke bliver vildledt. Notér midlertidige dæmpninger og deres
     udløb. -->

## Observationspunkter

<!-- Målinger eller systemer, der trender i en bekymrende retning. -->

## Afventende opfølgninger

<!-- Opgaver overdraget til næste vagthold, med links til tickets. -->

## Noter

<!-- Alt andet nyttigt: adgangsbesynderligheder, leverandørproblemer,
     kontekst. -->
```

## Ændringsanmodning (til reguleret ændringskontrol)

```markdown
# Ændringsanmodning: [Ændringstitel]

- Ændrings-ID: [ID]
- Anmoder: [navn]
- Dato indsendt: [ÅÅÅÅ-MM-DD]
- Type: [Standard | Normal | Nød]
- Prioritet: [Lav | Middel | Høj]
- Status: [Indsendt | Godkendt | Afvist | Implementeret | Lukket]

## Beskrivelse af ændringen

<!-- Hvad der ændrer sig, og hvorfor. Referér til ticketten eller
     kravet. -->

## Berørte systemer og komponenter

<!-- Tjenester, data, miljøer og brugere, der påvirkes. -->

## Begrundelse og forretningspåvirkning

<!-- Grunden til ændringen og konsekvensen af ikke at gøre den. -->

## Risikovurdering

- Risikoniveau: [Lav | Middel | Høj]
- Mulig konsekvens, hvis ændringen fejler: [beskrivelse]
- Konsekvens for sikkerhed, privatliv eller compliance: [beskrivelse]

## Implementeringsplan

<!-- Ordnede trin, ansvarlige parter og timing. -->

## Test- og valideringsplan

<!-- Hvordan succes verificeres før og efter ændringen. -->

## Tilbagetrækning / tilbagerulningsplan

<!-- Hvordan ændringen omgøres, hvis den fejler, og genoprettelsestiden. -->

## Tidsplan

- Foreslået vindue: [start og slut, med tidszone]
- Forventet nedetid: [varighed eller ingen]

## Godkendelser

| Rolle | Navn | Beslutning | Dato |
|-------|------|------------|------|
| Ændringsejer | [navn] | [godkend/afvis] | [dato] |
| Teknisk gennemgænger | [navn] | [godkend/afvis] | [dato] |
| Ændringsrådgivende udvalg | [navn] | [godkend/afvis] | [dato] |

## Gennemgang efter implementering

<!-- Udfald, mødte problemer, og om tilbagetrækning var nødvendig. -->
```

## Skitse til konsekvensanalyse vedrørende databeskyttelse (DPIA)

```markdown
# Konsekvensanalyse vedrørende databeskyttelse: [Navn på behandlingsaktivitet]

- Vurderer: [navn]
- Dato: [ÅÅÅÅ-MM-DD]
- Gennemgængere: [DPO / privatlivskontakt]
- Status: [Udkast | Gennemgået | Godkendt]

## 1. Beskrivelse af behandlingen

<!-- Hvilke personoplysninger der behandles, hvordan, af hvem og til
     hvilket formål. Medtag dataflow fra indsamling til sletning. -->

- Registrerede: [hvem dataene handler om]
- Datakategorier: [typer af personoplysninger, notér særlige kategorier]
- Formål: [hvorfor dataene behandles]
- Modtagere og databehandlere: [hvem der modtager eller håndterer dataene]
- Opbevaringsperiode: [hvor længe data opbevares og sletningsmetode]
- Internationale overførsler: [destinationer og overførselsgrundlag]

## 2. Nødvendighed og proportionalitet

<!-- Er behandlingen nødvendig for formålet? Er det den mindst
     indgribende mulighed? Hvad er det lovlige grundlag eller
     hjemlen? -->

- Lovligt grundlag / hjemmel: [grundlag for hvert formål]
- Dataminimering: [hvorfor hvert felt er nødvendigt]
- Begrundelse for nøjagtighed og opbevaring: [noter]
- Hvordan registreredes rettigheder understøttes: [indsigt, sletning osv.]

## 3. Høring

<!-- Interessenter og, hvor relevant, registrerede, der er hørt. -->

## 4. Risici for enkeltpersoner

<!-- Identificér privatlivsrisici, og vurdér hver. -->

| Risiko for enkeltpersoner | Sandsynlighed | Alvorlighed | Samlet |
|---------------------------|---------------|-------------|--------|
| [f.eks. uautoriseret adgang til følsomme data] | [L/M/H] | [L/M/H] | [vurdering] |

## 5. Foranstaltninger til at reducere risiko

<!-- For hver risiko, afbødningen og restrisikoen efter den. -->

| Risiko | Foranstaltning | Restrisiko | Accepteret af |
|--------|----------------|------------|---------------|
| [risiko] | [kontrol] | [L/M/H] | [navn] |

## 6. Udfald og godkendelse

- Restrisiko acceptabel: [Ja | Nej]
- Foranstaltninger godkendt af: [navn, rolle]
- Høring af tilsynsmyndigheden påkrævet: [Ja | Nej]
- Gennemgangsdato: [ÅÅÅÅ-MM-DD]
```
