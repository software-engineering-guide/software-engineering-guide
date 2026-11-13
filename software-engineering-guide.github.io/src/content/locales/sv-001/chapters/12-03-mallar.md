# 12.3 Mallar

De här mallarna är kopiera-och-klistra-färdiga utgångspunkter. Lyft valfri mall in i er wiki, ert förvar eller ert ärendesystem och fyll i platshållarna inom hakparentes. Kursiverade anteckningar och inbäddade kommentarer förklarar vad som hör hemma i varje avsnitt. Ta bort dem när avsnittet är ifyllt. Håll mallar lätta: en mall som är snabbare att hoppa över än att fylla i kommer inte att användas. Anpassa rubriker och avsnitt efter er organisation, men bevara avsikten med varje del.

Några konventioner som används nedan:

- Text i `[hakparentes]` är en platshållare att ersätta.
- Text i _kursiv_ eller `<!-- kommentarer -->` är vägledning att ta bort.
- Håll det färdiga dokumentet så kort det går och ändå besvarar sina frågor.

## Arkitekturbeslutslogg (ADR)

```markdown
# ADR [NNNN]: [Kort titel på beslutet]

- Status: [Föreslagen | Accepterad | Föråldrad | Ersatt av ADR-XXXX]
- Datum: [ÅÅÅÅ-MM-DD]
- Beslutsfattare: [namn eller roller]
- Konsulterade: [namn eller roller]

## Sammanhang

<!-- Vilket är problemet, kraften eller begränsningen som driver detta
     beslut? Ange fakta och krav neutralt. Ta bara med det en framtida
     läsare behöver för att förstå varför ett beslut var nödvändigt. -->

## Beslut

<!-- Ange valet i en eller två tydliga meningar: "Vi kommer att ..." -->

## Övervägda alternativ

<!-- Lista de realistiska alternativ ni vägde och varför vart och ett
     valdes eller inte. Minst två alternativ bör finnas här. -->

- Alternativ A: [sammanfattning]. Avvisades eftersom [skäl].
- Alternativ B: [sammanfattning]. Avvisades eftersom [skäl].
- Valt alternativ: [sammanfattning]. Valdes eftersom [skäl].

## Konsekvenser

<!-- Beslutets ärliga resultat, både goda och dåliga. -->

- Positivt: [vunna fördelar]
- Negativt: [kostnader, risker eller begränsningar som accepteras]
- Uppföljning: [migreringar, nytt arbete eller beslut detta utlöser]

## Relaterat

<!-- Länkar till tidigare ADR, RFC, ärenden eller dokument detta rör. -->
```

## RFC / designdokument

```markdown
# RFC: [Titel]

- Författare: [namn]
- Status: [Utkast | Under granskning | Godkänd | Avvisad | Implementerad]
- Granskare: [namn eller roller]
- Skapad: [ÅÅÅÅ-MM-DD]
- Senast uppdaterad: [ÅÅÅÅ-MM-DD]
- Ärende / spårning: [länk]

## Sammanfattning

<!-- Ett stycke: vad detta föreslår och varför det spelar roll. En läsare
     bör förstå essensen enbart av det här avsnittet. -->

## Problem och motiv

<!-- Vilket problem löser vi? Vem berörs? Vad händer om vi inte gör
     något? Ta med relevant bakgrund och begränsningar. -->

## Mål och icke-mål

- Mål: [hur framgång ser ut, mätbart där det är möjligt]
- Icke-mål: [uttryckligen utanför omfattningen, för att förhindra omfattningsglidning]

## Föreslagen design

<!-- Dokumentets kärna. Beskriv tillvägagångssätt, arkitektur,
     datamodell, gränssnitt och nyckelflöden. Använd diagram där de
     klargör. Förklara hur det fungerar, inte bara vad det är. -->

## Övervägda alternativ

<!-- Andra tillvägagångssätt och varför de inte valdes. Visar läsaren
     att designrymden utforskats. -->

## Påverkan och risker

- Säkerhet och integritet: [konsekvenser och åtgärder]
- Prestanda och skala: [förväntad last och beteende]
- Driftbarhet: [övervakning, felmoder, utrullning, återställning]
- Kostnad: [påverkan på infrastruktur eller licenser]
- Bakåtkompatibilitet: [migrering och utfasning]

## Test- och utrullningsplan

<!-- Hur ändringen kommer att valideras och släppas säkert. -->

## Öppna frågor

<!-- Olösta frågor ni vill att granskare ska väga in på. -->
```

## Efterhandsgranskning / incidentgranskning (skuldfri)

```markdown
# Efterhandsgranskning: [Incidentens titel]

- Incident-ID: [ID]
- Incidentens datum: [ÅÅÅÅ-MM-DD]
- Författare: [namn]
- Status: [Utkast | Slutlig]
- Allvarlighet: [SEV1 | SEV2 | SEV3]

> Den här granskningen är skuldfri. Vi fokuserar på system och bidragande
> faktorer, inte på individer. Målet är att lära och att förhindra
> upprepning.

## Sammanfattning

<!-- Två eller tre meningar: vad som hände, påverkan och lösningen,
     läsbart för en icke-expert. -->

## Påverkan

- Varaktighet: [starttid till återställningstid, med tidszon]
- Berörda användare: [omfattning och antal]
- Affärspåverkan: [intäkt, SLA, anseende eller annat]

## Tidslinje

<!-- Tidsstämplad, faktabaserad sekvens av händelser. Ta med upptäckt,
     eskalering, nyckelåtgärder och återställning. -->

- [TT:MM] [händelse]
- [TT:MM] [händelse]

## Bidragande faktorer

<!-- Kedjan av förhållanden som ledde till incidenten. Föredra
     "bidragande faktorer" framför en enda grundorsak. -->

## Upptäckt och respons

- Hur upptäcktes den? [larm, kundrapport etc.]
- Vad hjälpte responsen?
- Vad fördröjde responsen?

## Vad som gick bra

<!-- Uppmärksamma effektiva åtgärder och skyddsåtgärder som fungerade. -->

## Åtgärdspunkter

<!-- Specifika, ägda och daterade. Adressera förebyggande, upptäckt och
     mildring. Spåra dessa i den vanliga backloggen. -->

| Åtgärd | Ägare | Förfallodatum | Typ (förebygga/upptäcka/mildra) | Ärende |
|--------|-------|---------------|---------------------------------|--------|
| [åtgärd] | [namn] | [datum] | [typ] | [länk] |

## Lärdomar

<!-- Vad den bredare organisationen bör ta med sig. -->
```

## Hotmodell (STRIDE-baserad)

```markdown
# Hotmodell: [System eller funktion]

- Författare: [namn]
- Datum: [ÅÅÅÅ-MM-DD]
- Granskare: [säkerhetskontakt, ägare]
- Omfattning: [vad som täcks och inte täcks]

## Systemöversikt

<!-- Kort beskrivning av systemet, dess syfte och dess användare. -->

## Tillgångar

<!-- Vad som är värt att skydda: data, inloggningsuppgifter,
     funktionalitet, anseende. Notera känsligheten hos varje. -->

## Förtroendegränser och dataflöde

<!-- Beskriv eller rita komponenter, datalager, externa entiteter och
     gränserna där förtroendet ändras. -->

## Hot (STRIDE)

<!-- För varje element, beakta STRIDE-kategorierna. Registrera varje
     trovärdigt hot, dess risk och åtgärden eller den accepterade risken. -->

| Hot | STRIDE-kategori | Berört element | Risk (L/M/H) | Åtgärd | Status |
|-----|-----------------|----------------|--------------|--------|--------|
| [hot] | Förfalskning av identitet (Spoofing) | [element] | [risk] | [kontroll] | [öppen/mildrad/accepterad] |
| [hot] | Manipulering (Tampering) | [element] | [risk] | [kontroll] | [status] |
| [hot] | Förnekande (Repudiation) | [element] | [risk] | [kontroll] | [status] |
| [hot] | Informationsläckage (Information disclosure) | [element] | [risk] | [kontroll] | [status] |
| [hot] | Överbelastning (Denial of service) | [element] | [risk] | [kontroll] | [status] |
| [hot] | Behörighetseskalering (Elevation of privilege) | [element] | [risk] | [kontroll] | [status] |

## Antaganden och beroenden

<!-- Säkerhetsantaganden som förlitas på och externa kontroller som litas på. -->

## Öppna frågor och uppföljning

<!-- Hot som behöver mer arbete, spårade som ärenden. -->
```

## Körbok

```markdown
# Körbok: [Uppgift eller scenario]

- Tjänst: [tjänstens namn]
- Ägare: [team]
- Senast granskad: [ÅÅÅÅ-MM-DD]
- Relaterade larm: [larmnamn]

## Syfte

<!-- När den här körboken används och vad den åstadkommer. -->

## Förutsättningar

<!-- Åtkomst, verktyg och behörigheter som behövs innan start. -->

## Upptäckt / symtom

<!-- Vad operatören observerar: larm, felsignaturer, paneler. -->

## Diagnos

<!-- Steg-för-steg-kontroller för att bekräfta problemet och snäva in
     orsaken. Ta med de exakta kommandona, frågorna eller panellänkarna. -->

1. [steg och förväntat resultat]
2. [steg och förväntat resultat]

## Åtgärd

<!-- Konkreta, ordnade steg för att rätta eller mildra. Notera varje steg
     som är riskabelt eller oåterkalleligt och hur framgång verifieras. -->

1. [steg]
2. [verifiera återhämtning]

## Återställning

<!-- Hur åtgärderna görs ogjorda om lösningen gör saken värre. -->

## Eskalering

<!-- Vem som ska kontaktas och när man ska eskalera. Sekundär jour,
     ägande team och leverantörskontakter. -->

## Referenser

<!-- Paneler, relaterade körböcker, arkitekturdokument. -->
```

## Tjänstens README / tjänstekatalogpost

```markdown
# [Tjänstens namn]

- Ägande team: [team]
- Jour: [länk till rotation]
- Nivå / kritikalitet: [Nivå 1 | 2 | 3]
- Förvar: [länk]
- Status: [Aktiv | Föråldrad]

## Vad den gör

<!-- Ett stycke om tjänstens ansvar och dess konsumenter. -->

## Arkitektur

<!-- Nyckelkomponenter, beroenden (uppströms och nedströms) och en länk
     till designdokumentet eller diagrammet. -->

## Gränssnitt

- API:er / ändpunkter: [länk till specifikation]
- Händelser som publiceras / konsumeras: [ämnen]
- Datalager: [databaser, cacher, hinkar]

## Körtid och driftsättning

- Miljöer: [utveckling, staging, produktion]
- Hur man driftsätter: [flödeslänk och process]
- Konfiguration och funktionsflaggor: [var och hur]

## Observerbarhet

- Paneler: [länkar]
- Larm: [länkar]
- Loggar: [var man hittar dem]
- SLO:er: [länk]

## Drift

- Körböcker: [länkar]
- Vanliga uppgifter: [skalning, omstart, efterfyllnad]
- Kända problem och begränsningar: [anteckningar]

## Kom igång (för nya bidragsgivare)

<!-- Hur man bygger, testar och kör lokalt. -->

## Kontakter

- Slack / chattkanal: [länk]
- Eskalering: [väg]
```

## SLO- / felbudgetpolicy

```markdown
# SLO- och felbudgetpolicy: [Tjänst eller resa]

- Ägare: [team]
- Ikraftträdandedatum: [ÅÅÅÅ-MM-DD]
- Granskningstakt: [t.ex. kvartalsvis]

## Servicenivåindikatorer (SLI)

<!-- Definiera varje SLI exakt: den uppmätta storheten, hur den mäts och
     varifrån (helst ur användarens perspektiv). -->

| SLI | Definition | Datakälla |
|-----|-----------|-----------|
| Tillgänglighet | [t.ex. lyckade förfrågningar / totala förfrågningar] | [källa] |
| Latens | [t.ex. andel förfrågningar under X ms] | [källa] |

## Mål (SLO)

| SLI | Mål | Mätfönster |
|-----|-----|-----------|
| Tillgänglighet | [t.ex. 99,9 %] | [t.ex. rullande 28 dagar] |
| Latens | [t.ex. 95 % under 300 ms] | [rullande 28 dagar] |

## Felbudget

<!-- Den tillåtna otillförlitligheten: 100 % minus målet, över fönstret.
     Ange budgeten i konkreta termer (t.ex. minuter/månad). -->

- Budget: [härledd tillåtelse]

## Policy när budgeten är förbrukad

<!-- De överenskomna konsekvenserna. Gör dem konkreta och verkställbara. -->

- [t.ex. Frys icke-kritiska funktionsreleaser tills budgeten återhämtat sig.]
- [t.ex. Prioritera tillförlitlighetsarbete i nästa planeringscykel.]
- [t.ex. Eskalera till teknikledningen om budgeten överskrids två fönster i rad.]

## Policy när budgeten är frisk

<!-- Vilken extra risk teamet får ta, t.ex. snabbare utrullningar. -->

## Larm

<!-- Förbränningstaktslarm och trösklar knutna till denna SLO. -->
```

## Riskregisterpost

```markdown
## Risk: [Kort risktitel]

- Risk-ID: [ID]
- Datum väckt: [ÅÅÅÅ-MM-DD]
- Ägare: [namn eller roll ansvarig för att hantera risken]
- Kategori: [säkerhet | operativ | efterlevnad | ekonomisk | leverans | leverantör]
- Status: [Öppen | Mildras | Accepterad | Stängd]

### Beskrivning

<!-- Ange risken som: orsak -> händelse -> konsekvens. Vad som kan
     hända och varför det spelar roll. -->

### Bedömning

- Sannolikhet: [Låg | Medel | Hög]
- Påverkan: [Låg | Medel | Hög]
- Sammantaget betyg: [härlett ur sannolikhet x påverkan]

### Nuvarande kontroller

<!-- Vad som redan minskar den här risken i dag. -->

### Åtgärdsplan

<!-- Planerade åtgärder för att minska sannolikhet eller påverkan, med
     ägare och datum. Om risken accepteras, registrera vem som accepterade
     den och varför. -->

| Åtgärd | Ägare | Förfallodatum | Status |
|--------|-------|---------------|--------|
| [åtgärd] | [namn] | [datum] | [status] |

### Granskning

- Nästa granskningsdatum: [ÅÅÅÅ-MM-DD]
- Beslut / anteckningar: [eventuellt godkännande eller ändring]
```

## Projektets enkelsidare / produktunderlag

```markdown
# [Projekt- eller produktnamn]: enkelsidare

- Sponsor: [namn]
- Ledare: [namn]
- Datum: [ÅÅÅÅ-MM-DD]
- Status: [Idé | Godkänd | Pågår | Levererad]

## Problem

<!-- Ett stycke: kund- eller affärsproblemet och belägg för att det är
     verkligt och värt att lösa. -->

## Målgrupp

<!-- Vem som har det här problemet och vem som drar nytta av att lösa det. -->

## Föreslagen lösning

<!-- En kort beskrivning av vad vi ska bygga eller ändra. Håll det på
     avsiktsnivå, inte implementationsdetaljer. -->

## Varför nu

<!-- Skälet att göra detta nu snarare än senare. -->

## Framgångsmått

<!-- Hur vi vet att det fungerade. Föredra mätbara utfall. -->

- [mått och mål]

## Omfattning

- Inom omfattningen: [vad vi ska göra]
- Utanför omfattningen: [vad vi inte ska göra]

## Risker och öppna frågor

<!-- Huvudsakliga osäkerheter och beroenden. -->

## Grov plan och milstolpar

<!-- Övergripande faser och ungefärlig tidsplan. -->

## Kostnad och resurser

<!-- Människor, tid och budget som krävs. -->
```

## Jouröverlämningsanteckningar

```markdown
# Jouröverlämning: [ÅÅÅÅ-MM-DD]

- Avgående: [namn]
- Inkommande: [namn]
- Tjänst(er): [namn]

## Övergripande status

<!-- En rad: lugnt, bullrigt eller pågående problem. -->

## Öppna incidenter

<!-- Alla aktiva eller nyligen lösta incidenter nästa respondent måste
     känna till, med länkar. -->

- [incident, status och vad som återstår]

## Pågående eller planerade ändringar

<!-- Driftsättningar, migreringar, underhållsfönster eller experiment
     under arbete som kan orsaka larm. -->

## Bullriga eller opålitliga larm

<!-- Larm som utlöstes och deras verkliga betydelse, så att nästa person
     inte vilseleds. Notera tillfälliga tystningar och när de upphör. -->

## Bevakningsposter

<!-- Mått eller system som trendar i oroande riktning. -->

## Väntande uppföljningar

<!-- Uppgifter överlämnade till nästa pass, med länkar till ärenden. -->

## Anteckningar

<!-- Allt annat användbart: åtkomstkonstigheter, leverantörsproblem, sammanhang. -->
```

## Ändringsbegäran (för reglerad ändringskontroll)

```markdown
# Ändringsbegäran: [Ändringens titel]

- Ändrings-ID: [ID]
- Begärare: [namn]
- Inskickad: [ÅÅÅÅ-MM-DD]
- Typ: [Standard | Normal | Akut]
- Prioritet: [Låg | Medel | Hög]
- Status: [Inskickad | Godkänd | Avvisad | Genomförd | Stängd]

## Beskrivning av ändringen

<!-- Vad som ändras och varför. Hänvisa till ärendet eller kravet. -->

## Berörda system och komponenter

<!-- Tjänster, data, miljöer och användare som påverkas. -->

## Motivering och affärspåverkan

<!-- Skälet till ändringen och konsekvensen av att inte göra den. -->

## Riskbedömning

- Risknivå: [Låg | Medel | Hög]
- Potentiell påverkan om ändringen misslyckas: [beskrivning]
- Påverkan på säkerhet, integritet eller efterlevnad: [beskrivning]

## Genomförandeplan

<!-- Ordnade steg, ansvariga parter och tidsplan. -->

## Test- och valideringsplan

<!-- Hur framgång verifieras före och efter ändringen. -->

## Reträtt- / återställningsplan

<!-- Hur ändringen backas om den misslyckas, och återställningstiden. -->

## Schema

- Föreslaget fönster: [start och slut, med tidszon]
- Förväntat driftstopp: [varaktighet eller inget]

## Godkännanden

| Roll | Namn | Beslut | Datum |
|------|------|--------|-------|
| Ändringsägare | [namn] | [godkänn/avvisa] | [datum] |
| Teknisk granskare | [namn] | [godkänn/avvisa] | [datum] |
| Ändringsrådgivande nämnd | [namn] | [godkänn/avvisa] | [datum] |

## Granskning efter genomförande

<!-- Utfall, problem som uppstod och om reträtt behövdes. -->
```

## Konsekvensbedömning avseende dataskydd (DPIA), disposition

```markdown
# Konsekvensbedömning avseende dataskydd: [Behandlingsaktivitet]

- Bedömare: [namn]
- Datum: [ÅÅÅÅ-MM-DD]
- Granskare: [dataskyddsombud / integritetskontakt]
- Status: [Utkast | Granskad | Godkänd]

## 1. Beskrivning av behandlingen

<!-- Vilka personuppgifter som behandlas, hur, av vem och för vilket
     ändamål. Ta med dataflöden från insamling till radering. -->

- Registrerade: [vem uppgifterna handlar om]
- Datakategorier: [typer av personuppgifter, notera särskilda kategorier]
- Ändamål: [varför uppgifterna behandlas]
- Mottagare och biträden: [vem som tar emot eller hanterar uppgifterna]
- Lagringsperiod: [hur länge uppgifterna sparas och raderingsmetod]
- Internationella överföringar: [destinationer och överföringsmekanism]

## 2. Nödvändighet och proportionalitet

<!-- Är behandlingen nödvändig för ändamålet? Är den det minst
     ingripande alternativet? Vilken är den rättsliga grunden eller
     befogenheten? -->

- Rättslig grund / befogenhet: [grund för varje ändamål]
- Uppgiftsminimering: [varför varje fält är nödvändigt]
- Motivering av riktighet och lagring: [anteckningar]
- Hur registrerades rättigheter stöds: [tillgång, radering etc.]

## 3. Samråd

<!-- Intressenter och, där det är relevant, registrerade som hörts. -->

## 4. Risker för individer

<!-- Identifiera integritetsrisker och betygsätt var och en. -->

| Risk för individer | Sannolikhet | Allvarlighetsgrad | Sammantaget |
|--------------------|------------|-------------------|-------------|
| [t.ex. obehörig åtkomst till känsliga uppgifter] | [L/M/H] | [L/M/H] | [betyg] |

## 5. Åtgärder för att minska risken

<!-- För varje risk, åtgärden och kvarstående risk efter den. -->

| Risk | Åtgärd | Kvarstående risk | Accepterad av |
|------|--------|------------------|---------------|
| [risk] | [kontroll] | [L/M/H] | [namn] |

## 6. Utfall och godkännande

- Kvarstående risk godtagbar: [Ja | Nej]
- Åtgärder godkända av: [namn, roll]
- Samråd med tillsynsmyndighet krävs: [Ja | Nej]
- Granskningsdatum: [ÅÅÅÅ-MM-DD]
```
