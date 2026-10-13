# 2.14 Projekt- og repositoriestruktur

## Overblik og motivation

Projekt- og repositoriestruktur er den fysiske organisering af en kodebase: de mapper, filer og navngivningskonventioner, der afgør, hvor en given ting bor. Et *repositorium* (ofte forkortet "repo") er den [versionsstyrede](https://en.wikipedia.org/wiki/Version_control) beholder, der rummer et projekts filer og deres historik. Et *projekt*, nogle gange kaldt en *solution*, når det grupperer flere beslægtede komponenter, er den logiske enhed af software, du bygger. Struktur er det kort, du bruger til at finde, forstå og ændre den software.

I et lille team kan én person holde hele layoutet i hovedet. I et stort team, med hundredvis eller tusindvis af ingeniører, hyppige skift mellem teams og konsulenter, der kommer og går, opkræver hvert repositorium, der er organiseret anderledes, en ny kognitiv skat. Når du åbner et ukendt repo, bør du kunne gætte, hvor kildekoden, testene, dokumentationen og udrulningskonfigurationen bor, uden at læse en manual. Når hvert repo besvarer de spørgsmål på samme måde, er mobilitet billig og onboarding hurtig. Når hvert repo er et snefnug, bliver hvert kontekstskift til et lille researchprojekt.

I virksomheds- og offentlige sammenhænge er ensartet struktur også et kontrol- og sikringsanliggende. Revisorer, sikkerhedsgennemgangere og langsigtede vedligeholdere, der ofte arbejder år efter, at de oprindelige forfattere er gået, har brug for pålideligt at finde specifikationsdokumenter, licensfiler, sikkerhedspolitikker og builddefinitioner. Et forudsigeligt layout lader også automatiseret værktøj (scannere, afhængighedsanalysatorer, compliance-kontroller) virke på samme måde på tværs af en hel portefølje af systemer. Så dette kapitel behandler struktur som en konvention, du beslutter én gang og anvender overalt. Det er tæt beslægtet med kodestandarder og stil (kapitel 2.1), versionsstyring og kildekodestyring (kapitel 2.6) og dokumentation (kapitel 2.7).

## Grundprincipper

- Følg *[princippet om mindste overraskelse](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: layoutet bør matche det, en erfaren ingeniør ville forvente, så intet skal læres udenad.
- Ensartethed på tværs af repositorier slår lokal snuhed; en ensartet-nok struktur overalt er mere værd end den perfekte struktur ét sted.
- [README](https://en.wikipedia.org/wiki/README)'en er hoveddøren; en nyankommen bør kunne orientere sig ud fra den alene.
- Gør struktur selvbeskrivende gennem navngivning, så mapper og filer annoncerer deres formål.
- Håndhæv struktur med stilladsering og skabeloner, ikke med viljestyrke og gennemgangskommentarer.
- Adskil ansvarsområder fysisk: kildekode, tests, dokumentation, build og udrulning hører hjemme på adskilte, forudsigelige steder.
- Organisér afhængigheder, så de flyder i én retning, fra stabile kerner mod flygtige kanter.

## Anbefalinger

### Adoptér et ensartet topniveau-layout

Definér et standardsæt af topniveau-mapper, som hvert repositorium bruger, hvor det er relevant, og dokumentér, hvad hver er til for. En almindelig, leverandørneutral konvention omfatter: en kildemappe (ofte `src`) til produktionskode; en testmappe (ofte `test` eller `tests`) til automatiske tests; en `docs`-mappe til dokumentation; en `build`-mappe til builddefinitioner og -output; en `deploy`-mappe til udrulning og *[infrastruktur som kode](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (maskinlæsbare definitioner af servere, netværk og tjenester, dækket i kapitel 8.2); en `scripts`-mappe til automatisering og udviklerværktøj; en `examples`-mappe til kørbare eksempler; og en `spec`- eller `specification`-mappe til krav og designspecifikationer. Ikke hvert repo har brug for hver mappe, men hvor et anliggende findes, bør det bo på det forventede sted med det forventede navn.

### Gør README'en til indgangspunktet

Kræv en README-fil i repositoriets rod som det enkelte, kanoniske udgangspunkt. Den bør angive, hvad projektet er, hvordan man bygger og kører det, hvordan man kører testene, hvor man finder dybere dokumentation, hvem der ejer det, og hvordan man bidrager. README'en er ikke hele dokumentationssættet; den er indekset, der peger på resten (kapitel 2.7). Behandl en manglende eller forældet README som en fejl, fordi det er det første, enhver ny ingeniør, revisor eller integrator vil læse.

### Standardisér editor- og konfigurationsfiler

Check fælles editor- og værktøjskonfiguration ind i repositoriet, så hver bidragyder automatisk får ensartet adfærd. En `.editorconfig`-fil (en enkel, editoruafhængig fil, der definerer regler for mellemrum, indrykning og linjeskift) holder grundlæggende formatering ensartet på tværs af forskellige editorer og operativsystemer. Tilføj en ignoreringsfil til versionsstyringssystemet (så buildoutput og lokale artefakter aldrig committes) sammen med de fælles formatere- og linter-konfigurationer beskrevet i kapitel 2.1. Disse filer gør repositoriets konventioner aktive, ikke blot dokumenterede.

### Definér navngivnings- og mappekonventioner

Aftal konventioner for navngivning af mapper og filer (store og små bogstaver, separatorer, ental versus flertal og påkrævede suffikser som dem, der markerer tests) og anvend dem ensartet. Navne bør afsløre hensigt og matche det domænevokabular, der bruges andre steder i organisationen. Målet er enkelt: en sti bør kommunikere mening, så læsning af et mappe- eller filnavn fortæller dig, hvad der er indeni, uden at åbne det.

### Organisér lag og afhængigheder bevidst

Strukturér kodebasen, så dens arkitektoniske lag vises i mappelayoutet, og så afhængigheder flyder i én fornuftig retning. Politik på højere niveau bør ikke afhænge af detaljer på lavt niveau. Fælles, stabil kode bør sidde, hvor mange moduler kan nå den uden at skabe cyklusser. Når du gør lagdelingen fysisk, afspejlet i mappetræet, er ingeniører mere tilbøjelige til at respektere den, og overtrædelser er lettere at spotte i gennemgang og i automatiske afhængighedskontroller.

### Håndhæv struktur med stilladsering og skabeloner

Stil *[stilladsering](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)* til rådighed, den automatiske generering af et startprojekt, så nye repositorier begynder allerede korrekte. En *skabelon* eller *cookiecutter* (et parameteriseret projektskelet, der genererer et færdigt repositorium ud fra svar på nogle få spørgsmål) koder standardlayoutet, README'en, konfigurationsfilerne og [CI](https://en.wikipedia.org/wiki/Continuous_integration)-opsætningen ét sted. Når ingeniører opretter nye tjenester fra en fælles skabelon, bliver ensartethed standarden i stedet for en aspiration, og forbedringer af skabelonen flyder ud til fremtidige projekter.

### Hold struktur ensartet på tværs af mange repositorier i stor skala

Behandl selve layoutet som en styret standard: vedligeholdt centralt som enhver anden ingeniørstandard (kapitel 1.7) og versioneret som kode (kapitel 2.6). Offentliggør den, stil de skabeloner til rådighed, der implementerer den, og tillad afvigelser kun gennem en dokumenteret undtagelsesproces, så "standarden" bevarer sin betydning. I porteføljeskala kommer næsten al værdien af struktur fra dens ensartethed på tværs af repositorier, så drift er den største risiko at styre.

### Lad struktur informere valget mellem monorepo og multi-repo

Relatér struktur til beslutningen om repositoriegrænser dækket i kapitel 2.6. Et *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (ét repositorium med mange projekter) har brug for en klar intern konvention til at adskille projekter og deres fælles kode, så det enkelte træ forbliver navigerbart. En *multi-repo*-tilgang (mange små repositorier, ét pr. projekt eller tjeneste) har brug for stærk ensartethed på tværs af repoer, så hvert repo føles velkendt, selv om det står alene. Uanset hvad er en dokumenteret, skabelonbaseret struktur det, der holder navigation forudsigelig. Grænsevalget ændrer, hvor du anvender konventionen, ikke om du har brug for en.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper |
|---|---|---|
| Streng standardlayout for hele organisationen | Øjeblikkelig velkendthed; flytbare ingeniører; ensartet værktøj | Lejlighedsvis dårlig pasform til usædvanlige projekter; kræver styring |
| Frihed til layout pr. team | Lokal optimering; høj autonomi | Fragmentering; dyre kontekstskift; inkonsistent værktøj |
| Stilladsering og skabeloner | Korrekte repoer som standard; ændringer udbredes | Vedligeholdelse af skabeloner; risiko for drift fra genererede repoer |
| Dybt, lagdelt mappehierarki | Eksplicit struktur; klare grænser | Navigationsoverhead; lange stier; risiko for overkonstruktion |
| Fladt, lavt layout | Let at skimme; lav ceremoni | Dårlig adskillelse; bryder sammen, efterhånden som projektet vokser |

Den dominerende afvejning er ensartethed versus autonomi. Et enkelt standardlayout fjerner gnidning for de mange ingeniører, der flytter mellem kodebaser, på bekostning af det lejlighedsvise projekt, hvis behov ikke passer pænt i formen. I en stor organisation opvejer den kollektive gevinst ved velkendthed næsten altid det lokale tab. Derfor er den anbefalede holdning en stærk standard plus en dokumenteret undtagelsesvej (kapitel 1.7), frem for enten stiv ensartethed eller uhåndteret frihed. En sekundær afvejning er dybde versus enkelhed: nok struktur til at adskille reelle anliggender, men ikke så meget at navigation bliver til en vandretur gennem tomme mapper.

## Spørgsmål til drøftelse med dit team

1. **Når en ingeniør flytter til et ukendt repo hos os, hvor lang tid går der, før vedkommende kan finde testene, udrulningskonfigurationen og ejeren?** Dette er den navigationsskat, struktur findes for at fjerne, og i porteføljeskala betales den tusindvis af gange om året i små stykker, der lægges sammen til alvorligt tabt ingeniørtid. Pointen med princippet om mindste overraskelse er, at en erfaren ingeniør bør kunne gætte, hvor kildekode, tests, dokumentation og udrulning bor, uden at læse en manual, så den ærlige test er, om det gæt lykkes på tværs af jeres repoer. Tag et reelt tal med til mødet: tag tid på jer selv, når I orienterer jer i to eller tre ukendte interne repositorier, eller træk onboarding-data om, hvor lang tid nyankomne tager om at lave en første ændring. Hvis svaret måles i dages research frem for minutters genkendelse, har I kvantificeret omkostningen ved snefnugrepoer, og det retfærdiggør engangsinvesteringen i et standardlayout, som hvert repo deler.

2. **Vises vores arkitektoniske lag i mappetræet, eller skjuler afhængighedscyklusser sig inde i et fladt layout?** Struktur handler om mere end findbarhed: når du gør lagdeling fysisk, respekterer ingeniører den, og gennemgangere og automatiske afhængighedskontroller kan spotte overtrædelser, mens en flad bunke lader forkert kobling og cyklusser snige sig ind ubemærket, til ændring bliver farlig. På et stort, langlivet system er det, hvad der holder politik på højere niveau fra stille at afhænge af detaljer på lavt niveau, og det er netop den slags erosion, der er billig at forebygge og dyr at løse op. Tag jeres afhængighedsgraf med eller kør en hurtig kontrol: er der cyklusser, og afhænger noget stabilt af noget flygtigt? Svaret bør skubbe jer til at afspejle lag i mapper og tilføje automatiske kontroller af afhængighedsretning, så grænserne er synlige i træet og håndhævet i pipelinen frem for kun at leve i nogens mentale model.

3. **Starter vores nye repositorier korrekt fra en skabelon, eller støtter vi os til en wikiside og gode intentioner?** Struktur håndhævet ved stilladsering er standarden; struktur beskrevet i et dokument driver, fordi virkeligheden følger det, der genererer repoer, ikke det, en side siger, de bør ligne. For en stor eller reguleret organisation er det også et sikringsanliggende: når hvert repo genereres fra en fælles skabelon, finder sikkerhedsscannere, afhængighedsanalysatorer og revisorer licensen, sikkerhedspolitikken, specifikationen og builddefinitionen på samme sted hver gang, på tværs af leverandører og år. Tag dokumentationen med: hvor mange af jeres nylige repoer blev stilladseret fra standardskabelonen versus håndsamlet, og hvor langt er de skabelongenererede siden drevet? Handlingen er at gøre skabelonen til den eneste lette måde at starte et repo på, styre den som en versioneret standard med en dokumenteret undtagelsesvej og opdage drift automatisk, fordi ensartethed er der, hvor næsten al værdien af struktur bor.

4. **Har vi besluttet, om vores standard spænder over et monorepo eller mange separate repositorier, og holder den samme konvention faktisk på begge sider af den grænse?** Valget af repositoriegrænse ændrer, hvor I anvender konventionen, ikke om I har brug for en, og at tage fejl betyder et enkelt gigantisk træ, ingen kan navigere, eller en vækst af repoer, der hver føles fremmed. Et monorepo har brug for en klar intern konvention til at adskille projekter og deres fælles kode, så det ene træ forbliver navigerbart, mens en multi-repo-tilgang har brug for stærk ensartethed på tværs af repoer, så hvert selvstændigt repo stadig føles velkendt. Tag den aktuelle opgørelse med: hvor mange repoer I har, hvordan fælles kode adskilles inde i ethvert monorepo, og en tidsmålt test af, om en ingeniør kan finde et projekt inde i det store træ lige så hurtigt som i et selvstændigt repo. For en stor virksomhed eller et offentligt program, hvor forskellige leverandører leverer separate repositorier, så beslut bevidst, hvilke dele af konventionen der er universelle, og hvilke der er grænsespecifikke, fordi revisorer og platformsværktøj skal virke på samme måde, uanset om koden ankommer som ét træ eller halvtreds.

5. **Hvem ejer vores strukturstandard, og hvad sker der faktisk, når et projekt reelt ikke passer ind?** I porteføljeskala kommer næsten al værdien af struktur fra ensartethed, så de reelle risici er en ejerløs standard, der rådner, og en undtagelsesvej så vag, at hvert team stille opfinder sit eget layout. Spændingen er mellem stiv ensartethed, der passer til intet usædvanligt projekt, og uhåndteret frihed, der fragmenterer alt, og det sunde svar er en stærk standard plus en dokumenteret, reviderbar undtagelsesproces styret af en navngiven ejer og versioneret som kode. Tag dokumentationen med: er der en enkelt ansvarlig ejer, et versioneret standarddokument med en changelog, en log over givne undtagelser og hvorfor, og et antal udokumenterede afvigelser, I kan finde i det fri. I virksomheds- og offentlige sammenhænge er en undtagelse, ingen registrerede, et kontrolhul, så bind hver afvigelse til en skriftlig begrundelse og en gennemgangsdato, og sørg for, at indkøbskontrakter, der påbyder layoutet, også navngiver, hvem der må godkende afvigelser fra det.

6. **Gør vores README og indcheckede konfigurationsfiler vores konventioner aktive, eller er de dekorative?** En README er hoveddøren, og den indcheckede `.editorconfig`, ignoreringsfil og linter-konfiguration er det, der gør konventioner selvhåndhævende, men alligevel er det de første ting, der bliver forældede, og de sidste, nogen lægger mærke til, til en revisor eller en nyankommen ikke kan få projektet til at bygge. Spændingen er mellem en slank README, der forbliver aktuel, og en grundig, der driver, og mellem at stole på, at folk formaterer kode korrekt, og at lade fælles konfiguration håndhæve det automatisk. Tag en stikprøve med: træk fem repoer og tjek, hvor mange README'er der faktisk angiver, hvad projektet er, hvordan man bygger, tester og kører det, og hvem der ejer det, og hvor mange der bærer de fælles konfigurationsfiler frem for at støtte sig til individuelle vaner. For en stor eller reguleret organisation, hvor integratorer, sikkerhedsgennemgangere og langsigtede vedligeholdere læser README'en før noget andet, så behandl en manglende eller forældet hoveddør som en fejl med en ejer, og tjek tilstedeværelsen af konfigurationsfiler automatisk, så overensstemmelse ikke afhænger af velvilje.

## Sektorperspektiv

**Startup.** Hastighed vinder, så aftal ét enkelt, flat-nok layout til dit første repo (src, test, docs, scripts, en udfyldt README, en `.editorconfig` og ignoreringsfiler) og gem det som en let skabelon samme eftermiddag. Generér den anden tjeneste fra den, så begge repoer føles velkendte, og en ny konsulent onboardes på timer frem for at reverse-engineere et snefnug. Modstå dybe hierarkier og tung styring, du ikke har brug for endnu; hele gevinsten her er, at to grundlæggere og en konsulent deler ét kort.

**Lille virksomhed.** Uden en platformsspecialist og med et stramt budget så adoptér det konventionelle layout, dit sprog eller framework allerede antager, frem for at opfinde et, så standardværktøj og enhver nyansat ankommer forhåndstrænet i det. Køb stilladsering (en frameworkgenerator eller en cookiecutter-skabelon) i stedet for at bygge din egen, og brug din knappe indsats på at holde en udfyldt README aktuel. Den README er den billigste forsikring, du har, for den dag, den ene person, der kendte layoutet, flytter videre.

**Stor virksomhed.** På tværs af mange teams og hundredvis af repositorier er målet ensartethed: offentliggør en versioneret strukturstandard, generér hver ny tjeneste fra fælles skabeloner, opdag drift automatisk, og tillad afvigelser kun gennem en dokumenteret undtagelsesproces. Fordi hvert repo ser ens ud, er en ingeniør, der flyttes til et nyt team, produktiv inden for timer, og sikkerheds- og afhængighedsscannere på tværs af porteføljen finder licensen, sikkerhedspolitikken og builddefinitionen på samme sted hver gang. Budgettér skabelonvedligeholdelsen og driftsdetektionen eksplicit, fordi den vedligeholdelse er det, der holder standarden meningsfuld i stor skala.

**Offentlig sektor.** Indkøb, åbenhed og langsigtet ansvarlighed former layoutet, så påbyd en fælles struktur i de leveringsstandarder, der binder hver leverandør. Kræv en `specification`-mappe, der knytter kode til godkendte krav, en licens- og sikkerhedspolitikfil i roden og en `deploy`-mappe med infrastruktur-som-kode-definitionerne, så revisorer finder compliance-artefakter på samme måde i hvert system. Fordi konsulenter fra forskellige leverandører alle følger ét kort, koster vedligeholdelse efter en kontrakts udløb langt mindre, og offentligheden får et forsvarligt, inspicerbart spor fra krav til kørende kode.

## Eksempler

**Startup.** Et startup med tre medarbejdere aftaler et simpelt standardlayout til sit første repo (src, test, docs, scripts, en udfyldt README, en .editorconfig og ignoreringsfiler) og gemmer det som en let skabelon. Da de en måned senere opretter deres anden tjeneste, genererer de den fra den skabelon, så begge repoer allerede føles velkendte, og den nye konsulent onboardes på en eftermiddag. De modstår dybe mappehierarkier, de ikke har brug for endnu, og holder træet fladt nok til at skimme med et blik. Omkostningen var en eftermiddags opsætning, og den sparer dem for den snefnugvækst, der ellers ville gøre hvert fremtidigt repo til et lille researchprojekt.

**Stor virksomhed.** En multinational detailhandler kører hundredvis af tjenester på tværs af flere sprog. Dens platformsteam offentliggør en versioneret standard for repositoriestruktur og et sæt projektskabeloner, der implementerer den. Hver ny tjeneste genereres fra en skabelon, så den ankommer med standardmapperne `src`, `test`, `docs`, `deploy` og `scripts`, en udfyldt README, en `.editorconfig`, ignoreringsfiler og en fungerende CI-pipeline. Fordi hvert repositorium ser ens ud, er en ingeniør, der flyttes til et nyt team, produktiv inden for timer, og sikkerheds- og afhængighedsscannere i hele organisationen kører ensartet, fordi de altid finder filer, hvor de forventer dem.

**Offentlig sektor.** Et nationalt agentur, der moderniserer legacy-systemer, påbyder et fælles repositorielayout som del af sine leveringsstandarder for alle leverandører. Hvert repositorium skal indeholde en `specification`-mappe, der knytter kode til godkendte krav, en dokumenteret README, en licens- og sikkerhedspolitikfil i roden og en `deploy`-mappe med infrastruktur-som-kode-definitionerne (kapitel 8.2). Fordi konsulenter fra forskellige leverandører alle følger den samme struktur, kan agenturets revisorer finde compliance-artefakter på samme måde i hvert system, og langsigtet vedligeholdelse efter en kontrakts udløb koster langt mindre, fordi indkommende vedligeholdere allerede kender kortet.

## Business case: motivation, ROI og TCO

Omkostningen ved at indføre en strukturstandard er mest engangs: at blive enige om layoutet, bygge skabelonerne og dokumentere konventionen. Den tilbagevendende omkostning er lav, koncentreret i at vedligeholde skabelonerne og styre undtagelser. Omkostningen ved *ikke* at have en standard er tilbagevendende og akkumulerende: hver ingeniør, der åbner et ukendt repo, betaler en navigationsskat, hver onboarding kører langsommere, og automatiseret værktøj skal konfigureres pr. repo, fordi intet er, hvor du forventer det. På tværs af en stor organisation multipliceres disse små gnidninger til alvorlige tab af ingeniørtid.

Afkastet viser sig som hurtigere onboarding, billigere mobilitet mellem teams, højere signal fra værktøj på tværs af porteføljen og, i regulerede sammenhænge, lavere revisions- og langsigtede vedligeholdelsesomkostninger, fordi artefakter altid kan findes. De *totale ejeromkostninger* (TCO, den fulde livstidsomkostning ved at bygge, drive og vedligeholde et system) falder mest i langlivede systemer, hvor de vedligeholdere, der drager fordel af forudsigelig struktur, som regel ikke er de forfattere, der skabte den. For at argumentere over for ledelsen, ram struktur ind som en billig standard med stor løftestang, der forbedrer udviklerproduktivitet og revisionsparathed, og sæt et tal på den nuværende omkostning ved inkonsistens ved hjælp af onboarding-data og den indsats, der bruges på at lede efter ting i ukendte repositorier.

## Anti-mønstre og faldgruber

- **Snefnugrepositoriet:** hvert repo organiseret forskelligt, så hvert skal læres forfra.
- **Den manglende eller forældede README:** ingen hoveddør, hvilket tvinger nyankomne til at reverse-engineere, hvordan man bygger og kører projektet.
- **Struktur ved dokument, ikke ved skabelon:** en wikiside beskriver standardlayoutet, men intet genererer eller håndhæver det, så virkeligheden driver væk fra det.
- **Skabelondrift:** repositorier genereret fra en skabelon divergerer over tid, og forbedringer af skabelonen når dem aldrig.
- **Overkonstrueret hierarki:** dybe rede af næsten tomme mapper, der tilføjer ceremoni uden at hjælpe navigation.
- **Blandede ansvarsområder:** kildekode, tests, buildoutput og hemmeligheder rodet sammen uden klar adskillelse.
- **Committede buildoutput og lokale artefakter:** genererede filer checket ind, fordi ignoreringsregler aldrig blev opsat, hvilket forurener historik og diffs.
- **Lagovertrædelser skjult af flad struktur:** ingen fysiske grænser, så afhængighedscyklusser og forkert kobling sniger sig ind ubemærket.

## Modenhedsmodel

- **Niveau 1 (Opstart):** Hvert repositorium organiseres ad hoc af sine forfattere og reagerer på det, øjeblikket kræver; layouts varierer vidt; README'er mangler eller er upålidelige; nyankomne må guides gennem hvert repo i hånden.
- **Niveau 2 (Udvikling):** Grundlæggende konventioner findes uformelt, og mange repoer ligner hinanden; nogle teams har et eget startlayout; men der er ingen autoritativ standard, ingen fælles stilladsering, og strukturen driver mærkbart fra team til team.
- **Niveau 3 (Standardisering):** En dokumenteret, versioneret strukturstandard er håndhævet i hele organisationen; nye repositorier genereres fra fælles skabeloner med et standardlayout, README, konfigurationsfiler og CI; afvigelser går gennem en dokumenteret undtagelsesproces frem for at ske stiltiende.
- **Niveau 4 (Styring):** Overensstemmelse med standarden måles og styres med data: automatiske kontroller rapporterer, hvor stor en andel af repoerne der matcher layoutet, hvor langt skabelongenererede repoer er drevet, README-fuldstændighed og afhængighedsretningsovertrædelser, alt sammen fulgt mod baselines; onboarding- og navigationstider måles; undtagelser logges og gennemgås, og skabelonændringer godkendes på dokumentation frem for mening.
- **Niveau 5 (Orkestrering):** Struktur forbedres løbende og er adaptiv: skabelonforbedringer udbredes automatisk til eksisterende repositorier, strukturstyring er integreret med sikkerheds-, compliance- og platformsværktøj, og standarden udvikler sig bevidst, efterhånden som sprog, arkitekturer og porteføljen skifter, så ensartetheden holdes høj, mens organisationen ændrer sig omkring den.

## Idéer til drøftelse

- Hvilke topniveau-mapper bør være virkelig universelle på tværs af jeres organisation, og hvilke bør være valgfrie?
- Hvordan forhindrer I repositorier genereret fra en skabelon i at drive væk fra den over tid?
- Hvor går grænsen mellem et hjælpsomt, lagdelt hierarki og overkonstrueret mappeceremoni?
- Hvordan bør jeres strukturstandard adskille sig, hvis overhovedet, mellem et monorepo og en multi-repo-tilgang?
- Hvad er den rette undtagelsesproces for et projekt, hvis reelle behov ikke passer til standardlayoutet?
- Hvor stor en del af jeres struktur kan kontrolleres automatisk, og hvad afhænger stadig af menneskelig gennemgang?
- Hvem ejer strukturstandarden og dens skabeloner, og hvordan foreslås og udrulles ændringer?

## Vigtigste pointer

- Organisér hvert repositorium, så enhver ingeniør kan navigere i enhver kodebase efter forventning, efter princippet om mindste overraskelse.
- Adoptér et ensartet topniveau-layout (kildekode, test, docs, build, deploy, scripts, examples, specification) og gør README'en til indgangspunktet.
- Check editor- og værktøjskonfiguration ind (såsom `.editorconfig`), så konventioner er aktive, ikke blot nedskrevne.
- Håndhæv struktur med stilladsering og skabeloner, så nye repositorier er korrekte som standard.
- I stor skala ligger værdien i ensartethed: styr standarden, håndtér drift, og tillad afvigelser kun ved dokumenteret undtagelse.

## Referencer og videre læsning

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
