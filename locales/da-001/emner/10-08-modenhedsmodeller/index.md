# 10.8 Modenhedsmodeller

## Overblik og motivation

En [modenhedsmodel](https://en.wikipedia.org/wiki/Maturity_model) er en struktureret måde at vurdere, hvor kapabel og ensartet jeres praksis er inden for et domæne, og at beskrive en vej til at forbedre den. Den definerer en lille stige af niveauer. I bunden er arbejdet ad hoc og reaktivt. I toppen er det målt, styret og kontinuerligt optimerende. Hvert trin har observerbare kendetegn, I kan tjekke mod.

Modenhedsmodeller forvandler et vagt spørgsmål ("er vi gode til det her?") til et gentageligt svar ("vi er på niveau 2 her, niveau 4 der, og det er, hvad niveau 3 ville kræve"). Denne bog bruger en femniveaumodel i hvert kapitel og konsoliderer dem i kapitel 12.4. Dette kapitel handler om selve disciplinen: hvordan modellerne virker, hvornår de hjælper, og hvordan de vildleder.

Grunden til, at de betyder noget, er enkel. Store organisationer kan ikke forbedre det, de ikke kan se. På tværs af dusinvis af teams varierer kapabilitet enormt og usynligt. Nogle teams har fremragende test og svag sikkerhed; andre har det modsatte. En modenhedsmodel giver jer et fælles ordforråd og en fælles målestok, så huller bliver sammenlignelige, investering kan prioriteres, og fremskridt kan følges over tid frem for blot påstås. Velkendte eksempler omfatter CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), for proces), DORA-modellen ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), softwareleveringspræstation), OWASP SAMM (Software Assurance Maturity Model) og BSIMM (Building Security In Maturity Model) for softwaresikkerhed, TMMi (Test Maturity Model integration, for test), Agile Fluency-modellen og datastyringsmodenhedsmodeller, plus utallige interne scorecards.

For virksomheder og især det offentlige bærer modenhedsmodeller særlig vægt. Offentlig kontraktering har længe brugt CMMI-vurderingsniveauer som leverandørkvalificering, og rammeværker som det amerikanske CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) binder cybersikkerhedsmodenhed direkte til berettigelse til forsvarsarbejde. Det giver modenhedsmodeller reelle tænder. Det skaber også kapitlets centrale risiko: når et niveau bliver en port eller et mål, optimerer folk for vurderingen frem for den underliggende kapabilitet. Brugt godt er modenhedsmodeller et spejl. Brugt dårligt er de teater.

## Grundprincipper

- **Modenhed er et middel, ikke et mål.** Målet er kapabilitet og udfald, ikke et niveautal.
- **Vurdér for at lære, ikke for at score.** Ærlig selvvurdering slår en smigrende vurdering.
- **Højere er ikke altid bedre.** Det rette mål afhænger af risiko, kontekst og omkostning.
- **Mål pr. domæne, ikke ét globalt karakter.** Kapabilitet er ujævn; et enkelt tal skjuler det.
- **Prioritér først de huller med lavest modenhed og højest risiko.**
- **Vogt jer for [Goodharts lov](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Når et niveau først er et mål, holder det op med at måle kapabilitet.
- **Vurdér igen periodisk.** Modenhed driver, efterhånden som mennesker, systemer og trusler ændrer sig.

## Anbefalinger

### Vælg den rette model til domænet

Afstem modellen med den kapabilitet, I vil forbedre, og foretræk etablerede, dokumentationsbaserede modeller frem for opfundne, hvor de findes:

- **Proces og levering:** CMMI (bred procesmodenhed), DORA-kapabilitetsmodellen (leveringspræstation, forankret i forskning, kapitel 11.2).
- **Sikkerhed:** OWASP SAMM og BSIMM (softwaresikkerhedspraksisser), CMMC (forsvarscybersikkerhed).
- **Test og kvalitet:** TMMi.
- **Agil og arbejdsmåder:** Agile Fluency-modellen (kapitel 10.7).
- **Data:** datastyringsmodenhedsmodeller (DMM, DCAM).

Til internt brug er en simpel skala på fire eller fem niveauer anvendt pr. kapabilitet (som denne bog gør) ofte mere handlingsbar end et tungt eksternt rammeværk. Forbehold formelle, vurderede modeller til de steder, hvor de er kontraktligt påkrævede.

### Vurdér ærligt og pr. kapabilitet

Kør vurderinger, der producerer sandhed, ikke komfort. Inddrag de mennesker, der udfører arbejdet. Indsaml dokumentation frem for meninger. Score hver kapabilitet separat, så billedet afspejler virkeligheden: stærk her, svag der. En selvvurdering brugt til at guide forbedring er mere værd end en ekstern vurdering brugt til at optjene et mærke, fordi den første belønner åbenhed og den anden belønner præsentation. Kapitel 12.4 giver en konsolideret selvvurdering på tværs af hvert domæne i denne bog; brug den som et udgangsinstrument.

### Brug modenhed til at prioritere, ikke til at straffe

Outputtet af en vurdering er et prioriteret forbedringsefterslæb, ikke et karakterblad til skyldfordeling. Kombinér modenhed med risiko. En niveau-1-kapabilitet på et lavrisikoområde kan være fin. En niveau-2-kapabilitet på et sikkerheds- eller compliancekritisk område er presserende. Ret investering mod de huller, hvor lav modenhed møder høj risiko, og bind arbejdet til udfald (kapitel 11.1), så forbedring måles på resultater, ikke på at klatre op ad stigen for dens egen skyld.

### Sæt målniveauer bevidst: højere er ikke gratis

Hvert niveau op koster indsats og tilføjer ofte procesvægt. Det rette mål er sjældent "niveau 5 overalt." Det er det niveau, hvor den ekstra kapabilitet stadig retfærdiggør den ekstra omkostning for det domænes risiko. Regulerede og sikkerhedskritiske kapabiliteter kan reelt have brug for de øverste trin, og revision kræver ofte mindst et "defineret" niveau 3. Mange andre er godt tjent med niveau 3 og ville kun ophobe bureaukrati ved at presse videre. Afgør mål pr. kapabilitet, og stop med at klatre, når det risikojusterede afkast gør det.

### Værn mod modenhedsteater

Den ene fejlform, der ødelægger værdien af modenhedsmodeller, er at optimere for scoren. Hold øje med vurderinger, der giver generøse karakterer, dokumentation samlet kun til vurderingen eller "niveau 5"-påstande, som produktionshændelser modsiger. Hold vurderingen bundet til observerbar adfærd og reelle udfald. Roter eller sanity-tjek jeres vurderere eksternt. Behandl en mistænkeligt høj selvscore som en lugt. I det øjeblik niveauet bliver målet, holder modellen op med at fortælle jer sandheden.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| **Formelle vurderede modeller (CMMI, CMMC)** | Sammenlignelige, kontraktligt anerkendte, stringente | Dyre; inviterer til manipulation; kan forstene proces |
| **Lette interne scorecards** | Hurtige, handlingsbare, lav overhead | Mindre sammenlignelige eksternt; lette at skævvride |
| **Dokumentationsbaserede kapabilitetsmodeller (DORA)** | Bundet til reelle udfald; forskningsbaseret | Snævrere omfang; kræver reelle målinger |
| **Enkelt samlet modenhedskarakter** | Enkel at kommunikere | Skjuler ujævn kapabilitet; vildleder |
| **Vurdering pr. kapabilitet** | Nøjagtig, handlingsbar prioritering | Mere indsats; intet enkelt overskriftstal |

Den centrale spænding er **vurdering som spejl versus vurdering som mål**. Den samme model, der hjælper et team med at se sig selv klart, bliver kontraproduktiv i det øjeblik, et niveau knyttes til belønning, berettigelse eller status. Jo mere et niveau betyder, desto mere energi flyder ind i udseendet af modenhed frem for substansen.

## Spørgsmål til drøftelse med dit team

1. **Skal vi holde en åben intern selvvurdering adskilt fra ethvert kontraktligt vurderet niveau, og hvem ejer hver?** Når et CMMC- eller CMMI-niveau lukker omsætning, driver vurderingen og sandheden fra hinanden, fordi energi flyder mod at bestå frem for at forbedre. For en stor virksomhed eller en offentlig leverandør er det hul, hvor risiko gemmer sig: I består revisionen og forbliver eksponerede. Før to bøger med vilje. Behold den formelle vurdering til berettigelse, og behold et ligefremt internt scorecard, ingen belønnes for at puste op. Navngiv en ejer for hver, og behandl enhver afstand mellem dem som et signal at undersøge, ikke at dække over. Tag nylige hændelser, nærved-uheld og forfald efter vurdering med til mødet som dokumentation for, hvilken bog der fortæller sandheden.

2. **For hvert domæne, adopterer vi en etableret dokumentationsbaseret model eller opfinder vi vores eget scorecard, og er det det rette kald?** Etablerede modeller (DORA til levering, SAMM eller BSIMM til sikkerhed, TMMi til test) bærer forskning og ekstern sammenlignelighed, som et hjemmelavet gitter ikke kan matche. En let intern firniveauskala er hurtigere og mere handlingsbar, og den er ofte det bedre valg til intern styring. Fælden er at opfinde et tungt skræddersyet rammeværk, der har al ceremonien fra en formel model og intet af dokumentationsgrundlaget. Afgør pr. domæne: forbehold formelle vurderede modeller til de steder, hvor en kontrakt kræver dem, brug dokumentationsbaserede modeller, hvor de findes og passer, og hold en simpel skala pr. kapabilitet til alt andet. Tag listen over domæner med, markér hvilken model hvert bruger i dag, og udfordr ethvert opfundet scorecard.

3. **Hvem kører vores vurderinger, hvordan ville vi fange generøs karaktergivning, og hvor ofte vurderer vi igen?** En vurdering, der giver karakter til sig selv, smigrer sig selv, og modenhed driver, efterhånden som mennesker, systemer og trusler ændrer sig, så en to år gammel vurdering er ofte fiktion. Roter vurderere eller hent et eksternt sanity-tjek, og behandl en mistænkeligt høj selvscore som en lugt at jage, ikke en sejr at fejre. Sæt en gentagen vurderingskadence bundet til, hvor hurtigt hvert domæne ændrer sig: sikkerhed oftere end, sig, dokumentation. Indsaml dokumentation, og inddrag de mennesker, der udfører arbejdet, frem for at samle meninger fra ledere. Hvis jeres svar er, at ét team scorer sig selv én gang om året uden krydstjek, måler I komfort, ikke kapabilitet.

4. **Hvilket målmodenhedsniveau har hver kapabilitet faktisk brug for, og hvor ville det at presse højere kun købe procesvægt?** Højere er ikke gratis: hvert niveau op koster indsats og tilføjer som regel ceremoni, så et generelt mål om niveau 5 overalt dræner et endeligt forbedringsbudget ind i bureaukrati, nogle domæner aldrig vil betale tilbage. For en stor organisation varierer det rette mål pr. kapabilitet, fordi et lavrisikoområde på niveau 2 kan være helt sikkert, mens et sikkerheds- eller compliancekritisk område på samme niveau er en nødsituation. Tag en risikovurdering pr. kapabilitet, et ærligt estimat af, hvad næste trin koster i indsats og proces, og ethvert revisions- eller kontraktgulv med, da mange revisioner kræver mindst et defineret niveau 3. I virksomheds- og offentlige sammenhænge har nogle regulerede kapabiliteter reelt brug for de øverste trin, mens de fleste er godt tjent med niveau 3, så afgør mål bevidst, kapabilitet for kapabilitet, og stop med at klatre, når det risikojusterede afkast gør det.

5. **Da vi sidst hævede et modenhedsniveau, forbedredes det udfald, det skulle beskytte, faktisk, eller flyttede kun scoren sig?** Et niveau, der stiger, mens hændelser, ledetid eller fejlrater forbliver flade, er Goodharts lov i aktion: når tallet bliver målet, holder det op med at måle kapabilitet. For et stort team glider dette let forbi, fordi en vellykket vurdering føles som fremskridt, selv når produktion fortæller en anden historie. Bind hver kapabilitets niveau til en reel udfaldsmåling, før I investerer, og tag så før-og-efter-dokumentationen med til drøftelsen: hændelser pr. kvartal, ændringsfejlrate, tid til genoprettelse, hvad end kapabiliteten findes for at forbedre. I virksomheds- og offentlige porteføljer, hvor et vurderet niveau lukker berettigelse, er hullet farligt, fordi niveauet kan stige på samlet dokumentation, mens den underliggende praksis stille forfalder, og det første bevis på det er et brud, et udfald eller en dumpet revision.

6. **Kommunikerer vi én overskriftsmodenhedskarakter eller et billede pr. kapabilitet, og bindes niveauer nogensinde til belønning, rangering eller teamstatus?** Et enkelt samlet tal er let at præsentere for ledelsen og skjuler netop den ujævnhed, der betyder noget, fordi stærk levering kan maskere en niveau-1-sikkerhedskapabilitet; et varmekort pr. kapabilitet er mere arbejde, men viser, hvor lav modenhed møder høj risiko. Det sværere spørgsmål er, hvordan scorerne bruges, for i det øjeblik et niveau knyttes til et teams belønning eller rangering, dør ærlig rapportering, og indsats flyder ind i udseendet af modenhed frem for substansen. Tag varmekortet med, og en ærlig redegørelse for hvert sted, hvor et niveau i øjeblikket fodrer en præstationsvurdering, en budgetbeslutning eller et leverandørscorekort. For virksomheder og offentlige leverandører, hvor vurderede niveauer kan lukke omsætning og berettigelse, så vær eksplicitte om, hvilke karakterer der bærer konsekvenser, og hvilke der kun findes for at styre, fordi et modenhedsbillede, folk belønnes for at puste op, holder op med at beskrive virkeligheden.

## Sektorperspektiv

**Startup.** En tung vurderet model er overhead, I ikke har råd til på en kort runway. Kør en time lang selvvurdering på en simpel skala på tværs af en håndfuld kapabiliteter, ret kun det laveste modenhedshul, der blokerer noget konkret (sig, sikkerhedsspørgeskemaet fra jeres første virksomhedskunde), og lad resten være. Vurderingen bør koste en eftermiddag, ikke en konsulent, og dens output er en enkelt næste handling frem for en ensartet høj score, I hverken har brug for eller kan finansiere.

**Lille virksomhed.** Uden en dedikeret vurderer og med et stramt budget så lån en let offentlig model frem for at bestille et skræddersyet rammeværk: en kort leverings- eller sikkerhedstjekliste, I selv kan score. Behandl den som en årlig samtale om, hvor et svagt punkt ville koste jer en kunde, ikke et stående program. Hold den billig og ligefrem, fordi en smigrende score, I betalte en leverandør for at producere, er mindre værd end en ærlig en, I selv lavede på en eftermiddag.

**Stor virksomhed.** Værdien er et fælles scorecard pr. kapabilitet anvendt ensartet på tværs af mange teams, så huller bliver sammenlignelige, og forbedringsbudget flyder derhen, hvor lav modenhed møder høj risiko. Værn hårdt mod modenhedsteater, når niveauer fodrer budget eller status: roter eller sanity-tjek vurderere eksternt, og styr resultaterne som et varmekort, der dirigerer investering i asfalterede veje (kapitel 4.2), frem for en ligatabel, der rangerer teams og dræber ærlig rapportering.

**Offentlig sektor.** Et modenhedsniveau er her ofte en bogstavelig port: CMMC til forsvarsarbejde, en CMMI-vurdering som leverandørkvalificering. Opfyld det påkrævede niveau med ægte kapabilitet, og hold en åben intern selvvurdering adskilt fra den formelle vurdering, så revisionsgulvet aldrig stille bliver loftet. Dokumentér bevismateriale åbent for vurderere, og behandl enhver afstand mellem det certificerede niveau og den reelle praksis som ansvarlig risiko at lukke, ikke papirarbejde at arkivere.

## Eksempler

**Startup.** Et SaaS-startup på ti personer kører en time lang selvvurdering mod en simpel firniveauskala, der dækker levering, test, sikkerhed og vagtberedskab. Det finder levering og test på niveau 3, men sikkerhed fast på niveau 1, hvilket betyder noget, fordi det er ved at underskrive sin første virksomhedskunde med et sikkerhedsspørgeskema. Så grundlæggerne bruger den næste måned på blot at hæve sikkerhed til et forsvarligt niveau 2 og lader resten være i stedet for at jagte en ensartet høj score, de hverken har brug for eller endnu har råd til.

**Stor virksomhed.** En finansiel servicevirksomhed vurderer sine 40 teams med et let scorecard pr. kapabilitet (levering, test, sikkerhed, observerbarhed, vagtberedskab). Varmekortet afslører, at sikkerhedsmodenhed halter mest, hvor den regulatoriske eksponering er højest, så platformsteamet finansierer asfalteret-vej-sikkerhedsværktøj (kapitel 4.2) til de teams først. Fordi vurderingen bruges til at prioritere investering frem for at rangere teams, rapporterer ledere ærligt. Gentagen vurdering et år senere viser reel bevægelse og, afgørende, færre sikkerhedshændelser, ikke blot højere scorer.

**Offentlig sektor.** En forsvarsleverandør skal nå et påkrævet CMMC-niveau for at byde på arbejde, og en systemintegrator har en CMMI-vurdering som kontraktkvalificering. Her er modenhedsniveauet en bogstavelig port til omsætning. Den velkørte version behandler det påkrævede niveau som et gulv for ægte kapabilitet og holder en åben intern selvvurdering adskilt fra den formelle vurdering. Den dårligt kørte version samler dokumentation til vurderingen og lader den reelle praksis forfalde dagen efter, består revisionen og forbliver eksponeret.

## Business case: motivation, ROI og TCO

Afkastet af modenhedsvurdering kommer fra **styret investering**. Forbedringsbudgetter er endelige. Brugt blindt finansierer de det, der er højest. En modenhedsvurdering viser jer, hvor kapabilitet er svagest mod risiko, så det samme forbrug køber mere risikoreduktion og mere udfaldsforbedring. Selve vurderingen er billig, blot dages struktureret, dokumentationsbaseret gennemgang, sat mod omkostningen ved fejlallokerede forbedringsprogrammer eller, værre, et uopdaget kapabilitetshul, der dukker op som et brud, et udfald eller en dumpet revision.

Med hensyn til **samlet ejeromkostning** er disciplinen billig, når I holder den let, og dyr, når den hærder til vurderingsbureaukrati. Den dominerende skjulte omkostning er *modenhedsteater*: indsats brugt på at producere udseendet af modenhed returnerer intet og kan maskere reel risiko, hvilket er negativ ROI. For at fremlægge sagen for ledelsen så ram modenhed ind som en risiko-og-investeringslinse, et varmekort, der forvandler "forbedr alt" til "forbedr disse tre ting først", og budgettér eksplicit mod fristelsen til at jagte niveauer for deres egen skyld. Hvor et niveau er kontraktligt påkrævet (CMMC, CMMI), er ROI direkte: det er prisen for berettigelse, og målet er at opfylde det med ægte kapabilitet frem for kostbar forstillelse.

## Anti-mønstre og faldgruber

- **Niveau som mål:** at jagte et tal i stedet for den kapabilitet, det skal repræsentere.
- **Modenhedsteater:** at samle dokumentation til en vurdering, mens den reelle praksis forfalder.
- **Én global karakter:** en enkelt modenhedsscore, der skjuler farlig ujævnhed.
- **Højere-er-altid-bedre:** at presse hver kapabilitet til niveau 5 uanset risiko eller omkostning.
- **Vurdér én gang, aldrig igen:** en engangsvurdering behandlet som permanent sandhed.
- **At rangere teams for at give skyld:** at bruge modenhed til straf, hvilket dræber ærlig rapportering.
- **Modeldyrkelse:** at følge et tungt rammeværks ceremoni forbi nyttens grænse.
- **At ignorere udfald:** at klatre op ad stigen, mens levering, pålidelighed eller sikkerhed ikke forbedres.

## Modenhedsmodel

- **Niveau 1, Opstart.** Ingen fælles forestilling om modenhed; kapabilitet antages, er ujævn og umålt; enhver vurdering er reaktiv, udløst af en hændelse eller et revisionskrav frem for planlagt.
- **Niveau 2, Udvikling.** Nogle få teams kører ad hoc-vurderinger mod en eller anden skala, men modellen, kadencen og stringensen varierer team for team; resultater bruges inkonsistent, og dokumentationen er tynd, så at score for udseendets skyld er en altid nærværende risiko.
- **Niveau 3, Standardisering.** En enkelt model pr. kapabilitet og vurderingskadence er dokumenteret og anvendt i hele organisationen; vurderinger er dokumentationsbaserede, inddrager de mennesker, der udfører arbejdet, og fodrer et prioriteret forbedringsefterslæb frem for et karakterblad.
- **Niveau 4, Styring.** Modenhed måles og styres med data: hver kapabilitets niveau følges mod en baseline, bindes til en udfaldsmåling (hændelser, ledetid, ændringsfejlrate) og vurderes igen efter en fast kadence, så drift og generøs karaktergivning viser sig som tal frem for meninger, og mål sættes bevidst pr. domæne mod risiko og omkostning.
- **Niveau 5, Orkestrering.** Vurdering er integreret på tværs af organisationen og løbende forbedret: modenhed, risiko og udfald informerer investering som ét adaptivt billede, mål rebalanceres, efterhånden som trusler og kontekst skifter, vurderere roteres eller kontrolleres eksternt som en selvfølge, og praksissen pensionerer aktivt ceremoni, der ikke længere tjener sin omkostning.

## Idéer til drøftelse

1. Hvilke af jeres kapabiliteter antager I er modne uden dokumentation?
2. Hvor falder jeres laveste modenhed sammen med jeres højeste risiko, og er det der, jeres forbedringsbudget går hen?
3. Er noget modenhedsniveau i jeres organisation et mål eller en port? Hvilken adfærd har det produceret?
4. Hvad er det rette målniveau for hver kapabilitet, og hvor ville yderligere klatring blot tilføje bureaukrati?
5. Ville jeres teams rapportere deres modenhed ærligt, eller straffer den måde, I bruger scorer på, åbenhed?
6. Da I sidst "forbedrede modenhed", ændrede udfaldene sig så faktisk?

## Vigtigste pointer

- En modenhedsmodel vurderer kapabilitet mod en stige af niveauer og beskriver en vej til forbedring: et spejl, ikke et trofæ.
- Vælg etablerede, dokumentationsbaserede modeller pr. domæne (CMMI, DORA, SAMM/BSIMM, CMMC); en let skala pr. kapabilitet er ofte mest handlingsbar.
- **Vurdér ærligt, pr. kapabilitet**, og brug resultaterne til at **prioritere efter risiko**, ikke til at rangere eller give skyld.
- **Højere er ikke altid bedre:** sæt målniveauer bevidst mod risiko og omkostning.
- Vogt jer for **modenhedsteater** og **Goodharts lov**: et niveau, der bliver et mål, holder op med at måle kapabilitet.
- Se kapitel 12.4 for denne bogs konsoliderede modenhedsselvvurdering og hvert kapitels egen modenhedssektion.

## Referencer og videre læsning

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
