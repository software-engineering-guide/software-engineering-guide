# 1.5 Beslutningstagning og styring

## Overblik og motivation

Ethvert softwaresystem er summen af tusindvis af beslutninger: hvilken [database](https://en.wikipedia.org/wiki/Database), hvilken arkitektur, hvilket bibliotek, om man skal bygge eller købe, hvornår man skal påtage sig gæld, og hvornår man skal afdrage den. Styring er, hvordan du træffer disse beslutninger godt og ensartet, involverer de rette mennesker uden at skabe flaskehalse og bevarer begrundelsen, så fremtidige teams ikke er dømt til at lære den forfra. I et lille team sker beslutninger i samtale og lever i fælles hukommelse. I stor skala fordamper den hukommelse. Folk forlader virksomheden, teams omorganiseres, og "hvorfor" bag et kritisk valg går tabt, så efterfølgere enten efterligner det blindt eller river det ud uden at forstå det. God styring er maskineriet, der gør beslutninger synlige, bevidste og varige på tværs af en stor og foranderlig organisation.

Den centrale udfordring for store teams er at afveje autonomi mod sammenhæng. Skub alle beslutninger op til et centralt udvalg, og du får ensartethed, men til prisen af lammende flaskehalse og afmægtiggjorte teams. Skub alle beslutninger ned, og du får hastighed, men til prisen af kaos: uforenelige teknologier, dobbeltarbejde og gentagne fejl. Det modne svar er hverken centralisering eller anarki. Det er en lagdelt model. Teams beslutter det meste lokalt inden for en veludstukket "paved road", mens en let, gennemsigtig proces styrer de reelt tværgående og svære at fortryde valg. Målet er at gøre gode beslutninger til den lette standard og kun bruge knap styringsopmærksomhed, hvor det virkelig betyder noget.

Virksomheder og offentlige organisationer bærer øgede indsatser. De skal tilfredsstille revisorer, tilsynsmyndigheder og kontrolorganer, der kræver dokumenterede, forsvarlige beslutninger. De arbejder på lange tidshorisonter, hvor et dårligt arkitekturvalg eller en uhåndteret bunke [teknisk gæld](https://en.wikipedia.org/wiki/Technical_debt) kan belaste dem i et årti. Og deres indkøbs- og compliance-forpligtelser gør køb-eller-byg-beslutninger særligt vægtige og svære at fortryde. For disse organisationer er disciplineret, veldokumenteret beslutningstagning ikke bureaukrati for dets egen skyld. Det er risikostyring, organisatorisk hukommelse og grundlaget for ansvarlighed.

## Grundprincipper

- Registrér beslutninger og deres begrundelse; en beslutning uden begrundelse er en belastning.
- Skub beslutninger ned til det laveste niveau, der har konteksten, inden for klare rækværk.
- Afstem procesens vægt efter beslutningens vægt og reversibilitet.
- Skeln mellem reversible ("tovejsdør") og irreversible ("envejsdør") beslutninger og styr dem forskelligt.
- Foretræk paved roads og standarder frem for godkendelser fra sag til sag.
- Behandl teknisk gæld som en styret portefølje, ikke en moralsk fejl, der skal skjules.
- Gør styring gennemsigtig; skjult beslutningstagning avler mistillid og omarbejde.

## Anbefalinger

### Indfør Architecture Decision Records og en passende dimensioneret RFC-proces

Et [Architecture Decision Record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) er et kort, uforanderligt dokument, der fastholder én væsentlig beslutning: dens kontekst, de overvejede muligheder, det valg, der blev truffet, og konsekvenserne. Opbevar ADR'er i versionsstyring sammen med koden, så begrundelsen følger systemet. Til beslutninger, der har brug for input, før de træffes, brug en let [RFC](https://en.wikipedia.org/wiki/Request_for_Comments)-proces (request for comments): send et forslag rundt, inviter til kommentarer i en afgrænset periode, beslut derefter og registrér. Hold begge lette. Værdien ligger i tænkningen og den varige optegnelse, ikke i omstændelige skabeloner. Sammen gør ADR'er og RFC'er tavs, glemt begrundelse til en søgbar organisatorisk hukommelse.

### Styr gennem paved roads, ikke portvagter

I stedet for at gennemgå hver beslutning for sig, så invester i en "paved road": et sæt velsignede, velunderstøttede standarder, godkendte sprog, frameworks, udrulningspipelines og mønstre, som teams kan tage i brug med lidt gnidning og masser af støtte. Teams, der bliver på den anlagte vej, har brug for lidt styring, fordi det sikre, regelrette valg også er det lette. Teams med en reel grund til at forlade den kan det, men de påtager sig det ekstra ansvar og en let gennemgang. Denne "golden path"-model skalerer langt bedre end et centralt udvalg, der godkender alt, fordi den flytter styring fra portvagtfunktion sag for sag til veldesignede standarder.

### Brug arkitekturudvalg sparsomt og gennemsigtigt

Et arkitekturudvalg, eller dets ækvivalent, har en legitim rolle for de største, mest tværgående eller mest irreversible beslutninger og til at fastsætte de standarder, der definerer den anlagte vej. Hold dets omfang snævert, dets kriterier offentliggjort og dets proces hurtig og vejledende, ikke en obligatorisk flaskehals for rutinearbejde. Udvalgets opgave er at varetage sammenhæng og dele viden, ikke at godkende hvert valg. Når et udvalg bliver en kø, hvert projekt må vente i, har det slået fejl. Uddelegér offensivt og forbehold central gennemgang til de få beslutninger, der reelt fortjener den.

### Gør køb-versus-byg-versus-adoptér til en bevidst analyse

For enhver væsentlig kapabilitet så vej tre veje: byg den internt, køb et kommercielt produkt eller adoptér en [open source](https://en.wikipedia.org/wiki/Open-source_software)-løsning. Byg, når kapabiliteten er en ægte differentiator og central for din mission. Køb eller adoptér de udifferentierede kapabiliteter, som andre gør bedre. Regn [totale ejeromkostninger](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), ikke kun prisen på forhånd. At købe medfører licens-, integrations- og [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in)-omkostninger. At bygge medfører evig vedligeholdelse og bemanding. At adoptere open source medfører forpligtelser til support og sikkerhedssporing. Registrér beslutningen og dens antagelser som et ADR, så du kan tage den op igen, når omstændighederne ændrer sig.

### Styr teknisk gæld som en portefølje

Teknisk gæld er ikke i sig selv dårlig. Nogle gange er det det rigtige valg at påtage sig den for at udgive tidligere. Det, der er dårligt, er uhåndteret, usynlig, glemt gæld. Før en eksplicit fortegnelse over væsentlig gæld. Notér for hvert punkt den omkostning, det pålægger (den løbende "rente"), og omkostningen ved at rette det. Styr den derefter som en finansiel portefølje. Afdrag højrentegæld, der bremser teamet hver dag. Tolerér lavrentegæld i stabile hjørner. Træf gældsbeslutninger bevidst frem for ved et tilfælde. Afsæt en fast brøkdel af kapaciteten til at afdrage gæld, så den aldrig vokser til en krise.

### Skeln mellem reversible og irreversible beslutninger

Ikke alle beslutninger fortjener lige megen overvejelse. Reversible "tovejsdør"-beslutninger kan nemt fortrydes, så træf dem hurtigt og lokalt, af teamet, med en tilbøjelighed til handling. At spekulere over dem spilder tid og bremser læring. Irreversible eller dyre at fortryde "envejsdør"-beslutninger, en offentlig [API](https://en.wikipedia.org/wiki/API)-kontrakt, en datamodel i stor skala, en flerårig leverandørforpligtelse, fortjener langsom, omhyggelig, senior overvejelse og en registreret begrundelse. At klassificere beslutninger på denne måde er en af de vaner med størst løftestang inden for styring. Den retter knap granskning derhen, hvor den betaler sig, og frigør alt andet.

## Afvejninger: fordele og ulemper

| Styringstilgang | Fordele | Ulemper |
| --- | --- | --- |
| Centralt gennemgangsudvalg for alt | Maksimal ensartethed og tilsyn | Alvorlig flaskehals; afmægtiggør teams; langsom |
| Paved road med lokal autonomi | Skalerer, hurtig, sikker standard, styrker teams | Kræver platformsinvestering på forhånd; noget afdrift fra vejen |
| Fuld teamautonomi, ingen styring | Hurtig, højt ejerskab | Fragmentering, dobbeltarbejde, gentagne fejl |
| ADR'er / RFC'er | Varig hukommelse, bedre beslutninger, gennemsigtighed | Skriveoverhead; ignoreres hvis ikke vedligeholdt |

| Sourcing-valg | Fordele | Ulemper |
| --- | --- | --- |
| Byg | Fuld kontrol, passer præcist, kan differentiere | Evig vedligeholdelses- og bemandingsomkostning |
| Køb | Hurtigt, understøttet, en anden vedligeholder det | Licensomkostning, lock-in, ufuldkommen pasform |
| Adoptér (open source) | Ingen licensafgift, kan inspiceres, fællesskab | Support- og sikkerhedsbyrden falder på dig |

Den samlende afvejning er kontrol versus hastighed og central ensartethed versus lokal autonomi. Hvert styringsvalg ligger på dette spektrum. Den anbefalede holdning, paved roads plus reversibilitetsbaseret delegering, køber bevidst det meste af autonomiens hastighed og bevarer den ensartethed, der betyder noget. Det gør den ved at gøre det afstemte valg til det lette og forbeholde tung proces til den sjældne irreversible beslutning.

## Spørgsmål til drøftelse med dit team

1. **Hvem afgør, om en given beslutning er en envejsdør, og hvordan fanger I fejlklassifikationer i begge retninger?** At klassificere beslutninger efter reversibilitet er en af de vaner med størst løftestang inden for styring, og værdien kollapser, hvis man mærker forkert: behandler du et reversibelt valg som irreversibelt, drukner du det i overvejelser, behandler du et irreversibelt som reversibelt, udgiver du en datamodel eller en offentlig API-kontrakt, du ikke billigt kan fortryde. Den modstridende risiko er, at personen tættest på arbejdet kan være forudindtaget mod hastighed, mens et centralt udvalg kan være forudindtaget mod forsigtighed. Tag konkrete eksempler med til drøftelsen: hvad ville det faktisk koste, i tid og penge, at fortryde hver beslutning, og hvem bærer den omkostning. I virksomheder og offentlige organer gør indkøbsforpligtelser og data i stor skala mange valg til envejsdøre, der så reversible ud på forhånd. Enes om, hvem der klassificerer, og opbyg en vane med en hurtig second opinion på alt nær grænsen, så knap granskning lander, hvor fortrydelse reelt er dyr.

2. **Hvem ejer, finansierer og bemander den anlagte vej, og hvad forhindrer den i at forfalde til en portvagt?** En paved road virker kun, hvis de velsignede standarder er reelt velunderstøttede og lettere end alternativerne, og det kræver vedvarende investering, der er let at underfinansiere. Afvejningen er markant: en underressourceret paved road bliver til mandater uden støtte, hvilket netop er den portvagtfunktion, modellen skulle erstatte, og teams omgår den så. Tag dokumentation for vejens sundhed med: brugsrater, hvor ajourførte de godkendte værktøjer er, hvor hurtigt platformsteamet reagerer, og hvor ofte teams søger om at gå off-road. For store og regulerede organisationer er den anlagte vej også, hvordan det regelrette valg bliver det lette, så dens finansiering er en compliance-investering, ikke bare en bekvemmelighed. Beslut en klar ejer og et fast budget, og mål, om teams vælger vejen, fordi den reelt er den letteste.

3. **Hvor omgår teams jeres styring, og hvad fortæller den skygge-IT jer?** Teams undviger den sanktionerede vej, når den er mere smertefuld end omvejen, så udbredt skygge-IT er mindre et disciplinproblem end en designdom over jeres styring. De modstridende hensyn er reelle: noget undvigelse er hensynsløst, og meget af det er rationel undgåelse af et gennemgangsudvalg, der er blevet en kø på flere uger. Tag dokumentationen med: hvilke godkendelser springes over, hvilke uofficielle værktøjer har stille bredt sig, og hvor lang tid den officielle vej faktisk tager. I virksomheds- og offentlige sammenhænge er indsatsen højere, fordi usanktionerede værktøjer kan bryde revisions-, sikkerheds- og indkøbsforpligtelser med juridisk vægt. Hvis mønstret viser, at folk omgår en flaskehals, er løsningen at gøre den anlagte vej hurtigere og bredere og skrumpe udvalgets omfang til de få tværgående, irreversible beslutninger, ikke at tilføje flere godkendelser.

4. **Hvor stor en del af vores leveringskapacitet går faktisk til at afdrage teknisk gæld, og kan vi navngive de højrente-punkter, den bør ramme først?** Teknisk gæld opfører sig som renters rente, en stille skat på hver fremtidig ændring, og en stor organisation kan bære den i årevis, før nogen bemærker, at systemet er blevet langsomt og skrøbeligt at ændre. Det modstridende pres er barskt: hver time brugt på gæld er en time ikke brugt på features, ledelsen kan se, så afdrag er det første, der skæres, når en deadline strammes. Tag reel dokumentation med til drøftelsen, en skriftlig fortegnelse over væsentlig gæld, et ærligt skøn over den løbende omkostning, hvert punkt pålægger, og omkostningen ved at rette det, og den faktiske andel af den seneste kapacitet, der gik til afdrag versus nyt arbejde. For virksomheder og offentlige organer på tiårige horisonter tvinger uhåndteret gæld til sidst en dyr omskrivning eller et revisionsfund, så behandl en fast afdragsallokering som risikostyring og beslut, hvem der vogter den, når tidsplaner skrider.

5. **Når vi har brug for begrundelsen bag en beslutning truffet for to år siden, kan vi så faktisk finde den, og holder nogen den optegnelse i live?** Hele værdien af et Architecture Decision Record er, at begrundelsen overlever de mennesker, der traf den, og den værdi kollapser, hvis ADR'er skrives én gang, aldrig søges og stille bliver forældede. Spændingen ligger mellem den skrivedisciplin, der skal til for at fange kontekst, muligheder og konsekvenser i beslutningens øjeblik, og det daglige pres for bare at udgive og komme videre. Tag konkrete tests med til drøftelsen: vælg tre vigtige nylige beslutninger og se, om nogen kan finde den registrerede begrundelse på få minutter, og tjek, om erstattede ADR'er er markeret som sådan frem for stille at modsige den nuværende praksis. I virksomheds- og offentlige sammenhænge er den søgbare optegnelse netop det forsvarlige bevis, revisorer og tilsynsorganer kræver, så beslut, hvor ADR'er bor, hvem der gennemgår dem, og hvad der gør en beslutning væsentlig nok til at blive registreret.

6. **Hvornår tog vi sidst en stor køb-versus-byg-beslutning op igen mod dens oprindelige antagelser, og ville vi overhovedet bemærke, når de antagelser udløber?** Sourcing-valg er blandt de dyreste og sværest at fortryde beslutninger, du træffer, og antagelserne bag dem (en leverandørs priser, din egen bemanding, en open source-løsnings modenhed) bliver stille forældede, mens beslutningen står frosset. De modstridende hensyn vejer sunk cost og forstyrrelsen ved at skifte mod den voksende omkostning ved lock-in, en ufuldkommen pasform eller en vedligeholdelsesbyrde, du ikke længere vil have. Tag det oprindelige ADR og dets angivne antagelser med, et aktuelt TCO-skøn for hver vej inklusive licens, integration, bemanding og udgangsomkostning, og ethvert signal, en prisændring eller en nedgradering af support, om at en præmis har forskudt sig. For offentlige og regulerede købere gør indkøbsregler og flerårige kontrakter disse envejsdøre særligt bindende, så aftal på forhånd de udløsere og den kadence, der vil tvinge en bevidst genbeslutning frem for en blind fornyelse.

## Sektorperspektiv

**Startup.** Styr næsten intet og læn dig hårdt op ad hastighed: for reversible tovejsdør-valg så beslut ved skrivebordet og gå videre. Forbehold din ene styringsvane for de få envejsdøre, en kernedatamodel eller en grundlæggende leverandør, og fastholde hver i ét afsnit, så en fremtidig kollega ikke skal forhandle det forfra. Spring gennemgangsudvalg og paved roads helt over, for i din størrelse er de overhead, du ikke har råd til, og hele teamet deler allerede konteksten.

**Lille virksomhed.** Uden en arkitekt i staben så gør køb-versus-byg til dit centrale styringsspørgsmål og besvar det på totale ejeromkostninger frem for præference. Vælg som standard at købe eller adoptere velunderstøttede værktøjer til alt, der ikke er din kerne-differentiator, for evig vedligeholdelse er den omkostning, du har mindst råd til at bære. Hold ét let beslutningslog, så begrundelsen bag dine få væsentlige valg overlever, at en nøgleperson forlader virksomheden.

**Stor virksomhed.** Dit problem er at afveje autonomi mod sammenhæng på tværs af mange teams, så invester i en finansieret paved road og forbehold et snævert, hurtigt arkitekturudvalg til de reelt tværgående og irreversible beslutninger. Standardisér ADR'er, så begrundelse bliver søgbar organisatorisk hukommelse, og styr teknisk gæld og sourcing-valg som porteføljer med faste budgetter. Mål, om teams vælger vejen, fordi den er letteste, og skrump ethvert udvalg, der er forfaldet til en kø.

**Offentlig sektor.** Dokumenterede, forsvarlige beslutninger er ikke valgfrie her: revisorer og tilsynsorganer forventer at se begrundelsen, de vejede muligheder og antagelserne bag hvert væsentligt valg. Kør køb-versus-byg som en registreret TCO-analyse, respektér indkøbsregler, der begrænser sole-source-lock-in, og hold ADR'er som det revisionsparate bevisspor. Tag lange tidshorisonter alvorligt, for en datamodel eller leverandørforpligtelse truffet i dag kan binde organisationen i et årti, så klassificér den som en envejsdør og overvej i overensstemmelse hermed.

## Eksempler

**Startup.** Et startup med fire medarbejdere træffer de fleste beslutninger på minutter over et fælles skrivebord, og for reversible tovejsdør-valg er den hastighed en reel fordel, så de modstår enhver styringsoverhead. Men da de vælger en database og en datamodel, der vil være smertefuld at ændre senere (en envejsdør), holder de pause for at skrive en note på ét afsnit: mulighederne, valget og antagelserne bag. Et år senere, da de rammer skaleringsgrænser, sparer den ene note dem for at forhandle spørgsmålet forfra. De styrer næsten intet og forbeholder deres ene lette vane til de få beslutninger, der reelt er dyre at fortryde.

**Stor virksomhed.** En stor virksomheds platformsteams var lammet af et arkitekturudvalg, der skulle godkende hvert teknologivalg, hvilket skabte køer på flere uger. Virksomheden omstrukturerede styringen omkring en paved road: et kurateret katalog af godkendte, fuldt understøttede sprog, datalagre og pipelines, som teams kunne tage i brug med det samme. ADR'er registrerede enhver beslutning om at afvige, og en hurtig, vejledende gennemgang håndterede kun off-road-valg. Udvalgets omfang skrumpede til standardsætning og de få reelt tværgående beslutninger. Leveringen accelererede kraftigt. Ensartetheden forbedredes faktisk, fordi den lette vej nu var den regelrette. Og ADR-arkivet gav organisationen en søgbar optegnelse over, hvorfor tingene var bygget, som de var.

**Offentlig sektor.** Et ministerium stod over for en stor køb-versus-byg-beslutning om en sagsbehandlingsplatform under strenge indkøbs- og revisionsregler. I stedet for at beslutte efter præference kørte det en dokumenteret TCO-analyse på tværs af tre muligheder: at bygge skræddersyet, at købe et kommercielt produkt og at adoptere en open source-base. Det vejede licens, integration, langsigtet vedligeholdelse, bemanding og lock-in og registrerede beslutningen og dens antagelser som et ADR. År senere, da en leverandørs vilkår ændrede sig, tog ministeriet det ADR op igen, fandt at dets oprindelige antagelser ikke længere holdt, og genbeslutte med fuld viden om den tidligere begrundelse, hvilket undgik en blind og dyr migration. Den registrerede begrundelse var også netop det forsvarlige bevis, revisorerne krævede.

## Business case: motivation, ROI og TCO

Beslutninger er den omkostning inden for software, der har højest løftestang og lavest synlighed. Et enkelt dårligt, irreversibelt arkitektur- eller sourcing-valg kan pålægge år med modstand eller en afhjælpning på ni cifre. At styre det godt, nogle få timers overvejelse og en skriftlig optegnelse, koster næsten intet til sammenligning. Afkastet af ADR'er og reversibilitetsbaseret delegering kommer fra to kilder: at undgå dyre fejl på envejsdør-beslutningerne og at undgå spildt overvejelse og omarbejde på alt andet. Registreret begrundelse skærer også den tilbagevendende omkostning ved at genforhandle afgjorte spørgsmål og ved, at teams reverse-engineerer hensigten bag arvede systemer.

Teknisk gæld gør TCO-argumentet konkret. Uhåndteret gæld opfører sig præcis som renters rente: en voksende skat på hver fremtidig ændring, indtil systemet reelt bliver uvedligeholdeligt og kræver en dyr omskrivning. At styre gæld som en portefølje, med en fast kapacitetsallokering til at afdrage højrente-punkterne, er langt billigere end den endelige krise. God styring er billig at indføre, mest disciplinen at skrive beslutninger ned og investeringen på forhånd i en paved road. At springe den over er dyrt: du betaler i undgåelige omskrivninger, lock-in-overraskelser, revisionssvigt og tabt organisatorisk hukommelse. For at overbevise ledelsen, så fremstil styring på deres sprog: risikoreduktion, undgået omarbejde, hurtigere levering via den anlagte vej og revisionsparat forsvarlighed. Vis, at målet ikke er mere proces, men bedre rettet proces, tung granskning kun hvor fortrydelse er dyr, og gnidningsfri hastighed alle andre steder.

## Anti-mønstre og faldgruber

- Udokumenterede beslutninger: begrundelse tabt i det øjeblik, de mennesker, der traf den, forlader virksomheden.
- Godkendelsesudvalg som flaskehals: et centralt organ, ethvert projekt må stå i kø bag.
- Proces i én størrelse: at tvinge trivielle reversible beslutninger gennem tung gennemgang.
- Analyselammelse: at spekulere over let reversible tovejsdør-beslutninger.
- [Skygge-IT](https://en.wikipedia.org/wiki/Shadow_IT): teams, der helt undviger styring, fordi den sanktionerede vej er for smertefuld.
- Usynlig teknisk gæld: gæld der aldrig er fortegnet, aldrig afdraget og stille vokser.
- Byg-alt- eller køb-alt-reflekser: sourcing efter vane frem for TCO-analyse.
- Styringsteater: dokumenter og udvalg, der findes for syns skyld, men ikke former beslutninger.

## Modenhedsmodel

- Niveau 1 (Opstart): Beslutninger er ad hoc og uregistrerede; styring er enten fraværende eller en generel flaskehals; teknisk gæld er usynlig, og begrundelsen bag valg fordamper, når folk forlader virksomheden.
- Niveau 2 (Udvikling): Nogle beslutninger dokumenteres, og noget gennemgang findes, men praksis er uens på tværs af teams, og processen passer ofte ikke til beslutningens vægt og reversibilitet.
- Niveau 3 (Standardisering): ADR'er, en paved road, reversibilitetsbaseret delegering og en gældsfortegnelse er dokumenteret og håndhævet i hele organisationen, så det regelrette valg er den lette standard, og begrundelse er søgbar.
- Niveau 4 (Styring): Styring måles mod baselines: brug af den anlagte vej, ADR-dækning, beslutningscyklustid, gæld som andel af kapacitet og rater af off-road-undtagelser følges, og beslutninger om at afdrage gæld eller tage sourcing op igen udløses af den dokumentation frem for af kriser.
- Niveau 5 (Orkestrering): Styring tunes løbende og er integreret med levering og risikoplanlægning; granskning rettes præcist mod irreversible beslutninger; gæld og sourcing-valg omfordeles aktivt som porteføljer og genbesluttes på dokumentation, efterhånden som omstændighederne skifter.

## Idéer til drøftelse

- Kan vi for vores vigtigste nylige beslutninger finde den registrerede begrundelse bag dem?
- Hvor er vores styring en flaskehals, og hvor er den fraværende, når der er brug for den?
- Hvilke af vores nuværende beslutninger er envejsdøre, og behandler vi dem som sådan?
- Hvor stor en del af vores kapacitet går til at afdrage teknisk gæld, og er det nok?
- Følger vores teams den anlagte vej, fordi den reelt er den letteste, eller omgår de den?
- Hvornår tog vi sidst en stor køb-versus-byg-beslutning op igen mod dens oprindelige antagelser?

## Vigtigste pointer

- Registrér væsentlige beslutninger og deres begrundelse med ADR'er; gør begrundelse varig.
- Styr gennem paved roads og standarder, ikke portvagtfunktion sag for sag.
- Afstem procesvægt efter beslutningsvægt og reversibilitet; uddelegér tovejsdøre, overvej envejsdøre.
- Analysér køb-versus-byg-versus-adoptér på totale ejeromkostninger, og registrér antagelserne.
- Styr teknisk gæld som en eksplicit portefølje med en fast afdragsallokering.
- Hold styring gennemsigtig og let; ret knap granskning derhen, hvor fortrydelse er dyr.

## Referencer og videre læsning

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
