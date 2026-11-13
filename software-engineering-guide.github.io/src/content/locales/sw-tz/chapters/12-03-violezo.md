# 12.3 Violezo

Violezo hivi ni sehemu za kuanzia zilizo tayari kunakiliwa na kubandikwa. Chukua kielezo chochote hadi kwenye wiki yenu, hazina, au mfumo wa tiketi, na ujaze vishikilia nafasi vilivyo kwenye mabano. Maelezo yaliyo kwenye italiki na maoni ya ndani yanaeleza kinachostahili kila sehemu; yafute ukishajaza sehemu. Weka violezo vyepesi: kielezo ambacho ni cha haraka kukiruka kuliko kukikamilisha hakitatumika. Badilisha vichwa na sehemu kulingana na shirika lenu, lakini hifadhi nia ya kila sehemu.

Mikataba michache iliyotumika hapa chini:

- Maandishi yaliyo ndani ya `[mabano ya mraba]` ni kishikilia nafasi cha kubadilisha.
- Maandishi yaliyo ndani ya _italiki_ au `<!-- maoni -->` ni mwongozo wa kufuta.
- Weka hati iliyokamilika fupi kadiri iwezekanavyo huku bado ikijibu maswali yake.

## Kumbukumbu ya uamuzi wa usanifu (ADR)

```markdown
# ADR [NNNN]: [Kichwa kifupi cha uamuzi]

- Hali: [Imependekezwa | Imekubaliwa | Imeachwa | Imebadilishwa na ADR-XXXX]
- Tarehe: [YYYY-MM-DD]
- Waamuzi: [majina au majukumu]
- Walioshauriwa: [majina au majukumu]

## Muktadha

<!-- Tatizo, nguvu, au kikwazo kinachoendesha uamuzi huu ni nini?
     Eleza ukweli na mahitaji bila upendeleo. Jumuisha tu kile
     msomaji wa baadaye anachohitaji kuelewa kwa nini uamuzi
     ulikuwa wa lazima. -->

## Uamuzi

<!-- Eleza chaguo kwa sentensi moja au mbili wazi: "Tutafanya ..." -->

## Mbadala zilizozingatiwa

<!-- Orodhesha chaguo halisi ulizopima na kwa nini kila moja
     ilichaguliwa au haikuchaguliwa. Angalau mbadala mbili
     zinapaswa kuonekana hapa. -->

- Chaguo A: [muhtasari]; limekataliwa kwa sababu [sababu].
- Chaguo B: [muhtasari]; limekataliwa kwa sababu [sababu].
- Chaguo lililochaguliwa: [muhtasari]; limechaguliwa kwa sababu [sababu].

## Matokeo

<!-- Matokeo ya uaminifu ya uamuzi, mazuri na mabaya. -->

- Chanya: [faida zilizopatikana]
- Hasi: [gharama, hatari, au mapungufu yaliyokubaliwa]
- Ufuatiliaji: [uhamishaji, kazi mpya, au maamuzi ambayo hili linachochea]

## Yanayohusiana

<!-- Viungo vya ADR za awali, RFC, tiketi, au hati zinazohusiana. -->
```

## RFC / hati ya usanifu

```markdown
# RFC: [Kichwa]

- Mwandishi/Waandishi: [majina]
- Hali: [Rasimu | Inapitiwa | Imeidhinishwa | Imekataliwa | Imetekelezwa]
- Wapitiaji: [majina au majukumu]
- Imeundwa: [YYYY-MM-DD]
- Imesasishwa mwisho: [YYYY-MM-DD]
- Tiketi / ufuatiliaji: [kiungo]

## Muhtasari

<!-- Aya moja: kinachopendekezwa na kwa nini ni muhimu. Msomaji
     anapaswa kuelewa kiini kutoka sehemu hii peke yake. -->

## Tatizo na msukumo

<!-- Tunatatua tatizo gani? Nani anaathirika? Nini kinatokea
     tusipofanya chochote? Jumuisha usuli na vikwazo vinavyohusika. -->

## Malengo na yasiyo malengo

- Malengo: [mafanikio yanaonekanaje, yanayopimika inapowezekana]
- Yasiyo malengo: [yaliyo nje ya wigo waziwazi, kuzuia wigo kupanuka]

## Muundo unaopendekezwa

<!-- Kiini cha hati. Eleza mbinu, usanifu, muundo wa data,
     kiolesura, na mtiririko muhimu. Tumia michoro pale
     inapofafanua. Eleza jinsi unavyofanya kazi, si kile
     kilicho tu. -->

## Mbadala zilizozingatiwa

<!-- Mbinu nyingine na kwa nini hazikuchaguliwa. Inamwonyesha
     msomaji kwamba nafasi ya usanifu ilichunguzwa. -->

## Athari na hatari

- Usalama na faragha: [athari na hatua za kupunguza]
- Utendaji na ukubwa: [mzigo na tabia inayotarajiwa]
- Uwezo wa kuendesha: [ufuatiliaji, njia za kushindwa, utoaji, kurejesha nyuma]
- Gharama: [athari ya miundombinu au leseni]
- Utangamano wa nyuma: [uhamishaji na kuachwa]

## Mpango wa majaribio na utoaji

<!-- Jinsi badiliko litakavyothibitishwa na kutolewa kwa usalama. -->

## Maswali yaliyo wazi

<!-- Masuala ambayo hayajatatuliwa unayotaka wapitiaji wayapime. -->
```

## Uchambuzi wa baada ya tukio / mapitio ya tukio (bila lawama)

```markdown
# Uchambuzi wa baada ya tukio: [Kichwa cha tukio]

- Kitambulisho cha tukio: [ID]
- Tarehe ya tukio: [YYYY-MM-DD]
- Waandishi: [majina]
- Hali: [Rasimu | Ya mwisho]
- Ukali: [SEV1 | SEV2 | SEV3]

> Mapitio haya ni bila lawama. Tunalenga mifumo na vipengele
> vilivyochangia, si watu binafsi. Lengo ni kujifunza na kuzuia
> kujirudia.

## Muhtasari

<!-- Sentensi mbili au tatu: kilichotokea, athari, na utatuzi,
     zinazosomeka na asiye mtaalamu. -->

## Athari

- Muda: [wakati wa kuanza hadi wakati wa kupona, pamoja na saa za eneo]
- Watumiaji walioathirika: [wigo na idadi]
- Athari kwa biashara: [mapato, SLA, sifa, au nyingine]

## Mfuatano wa matukio

<!-- Mfuatano wenye mihuri ya muda, wa kweli wa matukio. Jumuisha
     ugunduzi, upandishaji, hatua muhimu, na kupona. -->

- [HH:MM] [tukio]
- [HH:MM] [tukio]

## Vipengele vilivyochangia

<!-- Mnyororo wa hali zilizopelekea tukio. Pendelea "vipengele
     vilivyochangia" kuliko chanzo kimoja cha msingi. -->

## Ugunduzi na mwitikio

- Liligunduliwaje? [tahadhari, ripoti ya mteja, n.k.]
- Nini kilisaidia mwitikio?
- Nini kilichelewesha mwitikio?

## Kilichokwenda vizuri

<!-- Tambua hatua zenye ufanisi na kinga zilizofanya kazi. -->

## Vipengee vya hatua

<!-- Mahususi, vyenye wamiliki, na vyenye tarehe. Shughulikia
     kuzuia, ugunduzi, na kupunguza. Vifuatilie kwenye mrundikano
     wa kawaida. -->

| Hatua | Mmiliki | Tarehe ya mwisho | Aina (zuia/gundua/punguza) | Tiketi |
|--------|-------|----------|--------------------------------|--------|
| [hatua] | [jina] | [tarehe] | [aina] | [kiungo] |

## Mafunzo

<!-- Shirika pana linapaswa kuchukua nini. -->
```

## Mfano wa vitisho (unaotegemea STRIDE)

```markdown
# Mfano wa vitisho: [Jina la mfumo au kipengele]

- Mwandishi/Waandishi: [majina]
- Tarehe: [YYYY-MM-DD]
- Wapitiaji: [mwasiliani wa usalama, wamiliki]
- Wigo: [kinachojumuishwa na kisichojumuishwa]

## Muhtasari wa mfumo

<!-- Maelezo mafupi ya mfumo, madhumuni yake, na watumiaji wake. -->

## Mali

<!-- Kinachostahili kulindwa: data, siri za uthibitisho, utendaji,
     sifa. Taja unyeti wa kila kimoja. -->

## Mipaka ya uaminifu na mtiririko wa data

<!-- Eleza au chora vijenzi, hifadhi za data, vyombo vya nje, na
     mipaka ambapo uaminifu unabadilika. -->

## Vitisho (STRIDE)

<!-- Kwa kila kipengele, zingatia aina za STRIDE. Rekodi kila
     tishio linaloaminika, hatari yake, na hatua ya kupunguza au
     hatari iliyokubaliwa. -->

| Tishio | Aina ya STRIDE | Kipengele kilichoathirika | Hatari (L/M/H) | Kupunguza | Hali |
|--------|-----------------|------------------|--------------|------------|--------|
| [tishio] | Kujifanya (Spoofing) | [kipengele] | [hatari] | [udhibiti] | [wazi/imepunguzwa/imekubaliwa] |
| [tishio] | Kuchezea (Tampering) | [kipengele] | [hatari] | [udhibiti] | [hali] |
| [tishio] | Kukana (Repudiation) | [kipengele] | [hatari] | [udhibiti] | [hali] |
| [tishio] | Ufichuzi wa taarifa (Information disclosure) | [kipengele] | [hatari] | [udhibiti] | [hali] |
| [tishio] | Kukataa huduma (Denial of service) | [kipengele] | [hatari] | [udhibiti] | [hali] |
| [tishio] | Kupandisha mamlaka (Elevation of privilege) | [kipengele] | [hatari] | [udhibiti] | [hali] |

## Dhana na utegemezi

<!-- Dhana za usalama zinazotegemewa na udhibiti wa nje unaoaminiwa. -->

## Masuala yaliyo wazi na ufuatiliaji

<!-- Vitisho vinavyohitaji kazi zaidi, vinavyofuatiliwa kama tiketi. -->
```

## Mwongozo wa uendeshaji

```markdown
# Mwongozo wa uendeshaji: [Jina la kazi au hali]

- Huduma: [jina la huduma]
- Mmiliki: [timu]
- Ilipitiwa mwisho: [YYYY-MM-DD]
- Tahadhari zinazohusiana: [majina ya tahadhari]

## Madhumuni

<!-- Wakati wa kutumia mwongozo huu na unachokamilisha. -->

## Mahitaji ya awali

<!-- Ufikiaji, zana, na ruhusa zinazohitajika kabla ya kuanza. -->

## Ugunduzi / dalili

<!-- Kile mwendeshaji anachokiona: tahadhari, saini za makosa,
     dashibodi. -->

## Utambuzi

<!-- Ukaguzi hatua kwa hatua wa kuthibitisha tatizo na kupunguza
     sababu. Jumuisha amri kamili, hoja, au viungo vya dashibodi. -->

1. [hatua na matokeo yanayotarajiwa]
2. [hatua na matokeo yanayotarajiwa]

## Utatuzi

<!-- Hatua halisi, zilizopangwa za kurekebisha au kupunguza. Taja
     hatua yoyote yenye hatari au isiyoweza kutenguliwa, na jinsi
     ya kuthibitisha mafanikio. -->

1. [hatua]
2. [thibitisha kupona]

## Kurejesha nyuma

<!-- Jinsi ya kutengua hatua utatuzi ukizidisha mambo. -->

## Upandishaji

<!-- Nani wa kuwasiliana naye na lini kupandisha. Simu ya dharura
     ya pili, timu inayomiliki, na waasiliani wa muuzaji. -->

## Marejeo

<!-- Dashboards, related runbooks, architecture docs. -->
```

## Service README / service catalog entry

```markdown
# [Service name]

- Owner team: [team]
- On-call: [rotation link]
- Tier / criticality: [Tier 1 | 2 | 3]
- Repository: [link]
- Status: [Active | Deprecated]

## What it does

<!-- One paragraph on the service's responsibility and its consumers. -->

## Architecture

<!-- Key components, dependencies (upstream and downstream), and a
     link to the design doc or diagram. -->

## Interfaces

- APIs / endpoints: [link to spec]
- Events published / consumed: [topics]
- Data stores: [databases, caches, buckets]

## Runtime and deployment

- Environments: [dev, staging, prod]
- How to deploy: [pipeline link and process]
- Configuration and feature flags: [where and how]

## Observability

- Dashboards: [links]
- Alerts: [links]
- Logs: [where to find them]
- SLOs: [link]

## Operations

- Runbooks: [links]
- Common tasks: [scaling, restart, backfill]
- Known issues and limitations: [notes]

## Getting started (for new contributors)

<!-- How to build, test, and run locally. -->

## Contacts

- Slack / chat channel: [link]
- Escalation: [path]
```

## SLO / error-budget policy

```markdown
# SLO and error-budget policy: [Service or journey name]

- Owner: [team]
- Effective date: [YYYY-MM-DD]
- Review cadence: [e.g. quarterly]

## Service level indicators (SLIs)

<!-- Define each SLI precisely: the measured quantity, how it is
     measured, and from where (ideally the user's perspective). -->

| SLI | Definition | Data source |
|-----|-----------|-------------|
| Availability | [e.g. successful requests / total requests] | [source] |
| Latency | [e.g. proportion of requests under Xms] | [source] |

## Objectives (SLOs)

| SLI | Target | Measurement window |
|-----|--------|--------------------|
| Availability | [e.g. 99.9%] | [e.g. rolling 28 days] |
| Latency | [e.g. 95% under 300ms] | [rolling 28 days] |

## Error budget

<!-- The allowed unreliability: 100% minus the target, over the
     window. State the budget in concrete terms (e.g. minutes/month). -->

- Budget: [derived allowance]

## Policy when the budget is exhausted

<!-- The agreed consequences. Make them concrete and enforceable. -->

- [e.g. Freeze non-critical feature releases until the budget recovers.]
- [e.g. Prioritize reliability work in the next planning cycle.]
- [e.g. Escalate to engineering leadership if breached two windows running.]

## Policy when the budget is healthy

<!-- What extra risk the team may take, e.g. faster rollouts. -->

## Alerting

<!-- Burn-rate alerts and thresholds tied to this SLO. -->
```

## Risk register entry

```markdown
## Risk: [Short risk title]

- Risk ID: [ID]
- Date raised: [YYYY-MM-DD]
- Owner: [name or role responsible for managing this risk]
- Category: [security | operational | compliance | financial | delivery | vendor]
- Status: [Open | Mitigating | Accepted | Closed]

### Description

<!-- State the risk as: cause -> event -> consequence. What could
     happen, and why it matters. -->

### Assessment

- Likelihood: [Low | Medium | High]
- Impact: [Low | Medium | High]
- Overall rating: [derived from likelihood x impact]

### Current controls

<!-- What already reduces this risk today. -->

### Mitigation plan

<!-- Planned actions to reduce likelihood or impact, with owners and
     dates. If accepting the risk, record who accepted it and why. -->

| Action | Owner | Due date | Status |
|--------|-------|----------|--------|
| [action] | [name] | [date] | [status] |

### Review

- Next review date: [YYYY-MM-DD]
- Decision / notes: [any acceptance sign-off or change]
```

## Project one-pager / product brief

```markdown
# [Project or product name]: one-pager

- Sponsor: [name]
- Lead: [name]
- Date: [YYYY-MM-DD]
- Status: [Idea | Approved | In progress | Shipped]

## Problem

<!-- One paragraph: the customer or business problem, and evidence it
     is real and worth solving. -->

## Audience

<!-- Who has this problem and who benefits from solving it. -->

## Proposed solution

<!-- A short description of what we will build or change. Keep it at
     the level of intent, not implementation detail. -->

## Why now

<!-- The reason to do this now rather than later. -->

## Success metrics

<!-- How we will know it worked. Prefer measurable outcomes. -->

- [metric and target]

## Scope

- In scope: [what we will do]
- Out of scope: [what we will not do]

## Risks and open questions

<!-- Main uncertainties and dependencies. -->

## Rough plan and milestones

<!-- High-level phases and approximate timing. -->

## Cost and resources

<!-- People, time, and budget required. -->
```

## On-call handoff notes

```markdown
# On-call handoff: [YYYY-MM-DD]

- Outgoing: [name]
- Incoming: [name]
- Service(s): [names]

## Overall status

<!-- One line: quiet, noisy, or ongoing issue. -->

## Open incidents

<!-- Any active or recently resolved incidents the next responder
     must know about, with links. -->

- [incident, status, and what remains]

## Ongoing or planned changes

<!-- Deploys, migrations, maintenance windows, or experiments in
     flight that could cause alerts. -->

## Noisy or flaky alerts

<!-- Alerts that fired and their real meaning, so the next person is
     not misled. Note any temporary silences and their expiry. -->

## Watch items

<!-- Metrics or systems trending in a concerning direction. -->

## Pending follow-ups

<!-- Tasks handed to the next shift, with links to tickets. -->

## Notes

<!-- Anything else useful: access quirks, vendor issues, context. -->
```

## Change request (for regulated change control)

```markdown
# Change request: [Change title]

- Change ID: [ID]
- Requester: [name]
- Date submitted: [YYYY-MM-DD]
- Type: [Standard | Normal | Emergency]
- Priority: [Low | Medium | High]
- Status: [Submitted | Approved | Rejected | Implemented | Closed]

## Description of change

<!-- What is changing and why. Reference the ticket or requirement. -->

## Systems and components affected

<!-- Services, data, environments, and users impacted. -->

## Justification and business impact

<!-- The reason for the change and the impact of not doing it. -->

## Risk assessment

- Risk level: [Low | Medium | High]
- Potential impact if the change fails: [description]
- Impact on security, privacy, or compliance: [description]

## Implementation plan

<!-- Ordered steps, responsible parties, and timing. -->

## Test and validation plan

<!-- How success will be verified before and after the change. -->

## Backout / rollback plan

<!-- How to reverse the change if it fails, and the recovery time. -->

## Schedule

- Proposed window: [start and end, with timezone]
- Expected downtime: [duration or none]

## Approvals

| Role | Name | Decision | Date |
|------|------|----------|------|
| Change owner | [name] | [approve/reject] | [date] |
| Technical reviewer | [name] | [approve/reject] | [date] |
| Change advisory board | [name] | [approve/reject] | [date] |

## Post-implementation review

<!-- Outcome, issues encountered, and whether backout was needed. -->
```

## Data Protection Impact Assessment (DPIA) outline

```markdown
# Data Protection Impact Assessment: [Processing activity name]

- Assessor: [name]
- Date: [YYYY-MM-DD]
- Reviewers: [DPO / privacy contact]
- Status: [Draft | Reviewed | Approved]

## 1. Description of the processing

<!-- What personal data is processed, how, by whom, and for what
     purpose. Include data flows from collection to deletion. -->

- Data subjects: [who the data is about]
- Data categories: [types of personal data, note any special categories]
- Purposes: [why the data is processed]
- Recipients and processors: [who receives or handles the data]
- Retention period: [how long data is kept and deletion method]
- International transfers: [destinations and transfer mechanism]

## 2. Necessity and proportionality

<!-- Is the processing necessary for the purpose? Is it the least
     intrusive option? What is the lawful basis or authority? -->

- Lawful basis / authority: [basis for each purpose]
- Data minimization: [why each field is necessary]
- Accuracy and retention justification: [notes]
- How data subject rights are supported: [access, deletion, etc.]

## 3. Consultation

<!-- Stakeholders, and where relevant data subjects, consulted. -->

## 4. Risks to individuals

<!-- Identify privacy risks and rate each. -->

| Risk to individuals | Likelihood | Severity | Overall |
|---------------------|-----------|----------|---------|
| [e.g. unauthorized access to sensitive data] | [L/M/H] | [L/M/H] | [rating] |

## 5. Measures to reduce risk

<!-- For each risk, the mitigation and residual risk after it. -->

| Risk | Measure | Residual risk | Accepted by |
|------|---------|---------------|-------------|
| [risk] | [control] | [L/M/H] | [name] |

## 6. Outcome and sign-off

- Residual risk acceptable: [Yes | No]
- Measures approved by: [name, role]
- Consultation with supervisory authority required: [Yes | No]
- Review date: [YYYY-MM-DD]
```
