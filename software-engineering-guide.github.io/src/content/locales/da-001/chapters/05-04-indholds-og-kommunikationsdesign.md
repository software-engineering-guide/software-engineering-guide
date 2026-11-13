# 5.4 Indholds- og kommunikationsdesign

## Overblik og motivation

Indholds- og kommunikationsdesign er arbejdet med at forme de ord, beskeder og oplysninger, et produkt bruger til at hjælpe folk med at handle. Det dækker [indholdsstrategi](https://en.wikipedia.org/wiki/Content_strategy) (hvilket indhold der bør findes, til hvem og hvorfor), UX-skrivning og microcopy (labels, knapper, hints og fejlmeddelelser inde i en grænseflade) og den kommunikation, der når brugerne gennem e-mail, notifikationer og andre kanaler. Ord er grænseflade. For det meste software er indholdet produktoplevelsen langt mere, end det visuelle er.

For store teams er indhold et koordinerings- og tillidsproblem. Når mange teams skriver uafhængigt, driver terminologien fra hinanden, tonen svinger fra venlig til bureaukratisk fra skærm til skærm, og det samme begreb får tre forskellige navne. Brugerne mister tråden, og de mister tilliden. En fælles indholdsstrategi løser det. En stemme-og-tone-guide, et kontrolleret ordforråd og genbrugelige mønstre for fejl og tomme tilstande gør for ord, hvad et designsystem gør for pixels: de lader uafhængige teams producere en sammenhængende, troværdig helhed.

I virksomheder og det offentlige er klart indhold ofte et juridisk og etisk krav, ikke et spørgsmål om stil. Love om [almindeligt sprog](https://en.wikipedia.org/wiki/Plain_language) kræver, at offentlig kommunikation kan forstås af de mennesker, der skal handle på den. Dårligt formuleret indhold i en ydelsesformular, en medicinsk instruktion eller en sikkerhedsadvarsel kan gøre reel skade: en overskredet frist, en forkert dosis, et svindeloffer. Og i en tid med manipulerende ["dark patterns"](https://en.wikipedia.org/wiki/Dark_pattern) (grænsefladedesign, der snyder eller presser folk til valg imod deres egen interesse) er det, hvordan et produkt præsenterer valg, et spørgsmål om tillid, sikkerhed og i stigende grad regulering.

## Grundprincipper

- Ord er UI; indhold er en kernedel af oplevelsen, ikke fyld tilføjet senere.
- Skriv til læserens mål og kontekst, i almindeligt sprog, i det øjeblik de har brug for det.
- Klarhed frem for kløgt; en forvirret bruger bliver ikke glædet af en vittig fejlmeddelelse.
- Ensartet terminologi og tone sænker den kognitive belastning og bygger tillid.
- Gode standarder og hjælpsomme tomme tilstande leder folk mod succes.
- Ærlighed ved design: snyd, pres eller skam aldrig brugere til valg.
- Indhold bør være struktureret og genbrugeligt, ikke hårdkodet og duplikeret.
- Design kommunikation for hele rejsen på tværs af kanaler, og respektér opmærksomhed.

## Anbefalinger

### Etablér en indholdsstrategi og en stemme

Begynd med at afgøre, hvem indholdet er til, hvilke jobs det hjælper dem med at få gjort, og hvordan det skal lyde. Skriv en stemme-og-tone-guide med konkrete eksempler og en terminologiordliste ([kontrolleret ordforråd](https://en.wikipedia.org/wiki/Controlled_vocabulary)), så den samme ting altid kaldes det samme. Lad tonen følge konteksten: beroligende i en fejl, rolig i en sikkerhedsadvarsel, festlig i en succes. Stemmen forbliver konstant; tonen bøjer sig. Behandl indhold som et styret aktiv med ejere, gennemgang og en livscyklus, ikke som tekst tastet ind i et felt i sidste øjeblik.

### Skriv microcopy, der hjælper folk med at handle

Giv knapper navn efter den handling, de udfører ("Indsend ansøgning," ikke "OK"). Skriv hints og hjælpetekst, der afværger fejl, før de sker. Sæt de vigtige ord forrest, så folk, der skimmer skærmen, stadig får pointen. Brug andenpersonsformen og aktiv form. Hold sætninger korte og specifikke. Hvert stykke microcopy bør reducere usikkerhed om, hvad der vil ske, og hvad man skal gøre næste gang.

### Gør almindeligt sprog til standarden, og opfyld juridiske krav

Skriv på et [læseniveau](https://en.wikipedia.org/wiki/Readability), der passer til hele jeres målgruppe, ikke forfatterne. Foretræk almindelige ord, korte sætninger og konkrete instruktioner; udvid jargon og akronymer ved første brug, eller undgå dem. I den offentlige sektor er almindeligt sprog ofte krævet ved lov og politik: følg de gældende standarder for almindeligt sprog, og test forståelse med rigtige brugere, herunder mennesker med lavere læsefærdigheder og ikke-modersmålstalende. Almindeligt sprog er ikke at "gøre det dummere." Ekspertlæsere foretrækker også klar, effektiv tekst.

### Design fejlmeddelelser, tomme tilstande og standarder bevidst

En fejlmeddelelse bør sige, hvad der gik galt, hvorfor og hvordan det rettes, i almindeligt sprog, uden bebrejdelse og uden koder, brugeren ikke kan handle på. Bevar brugerens input, og placér beskeden lige der, hvor problemet er. Tomme tilstande er en onboarding-mulighed: forklar, hvad der hører hjemme her, og hvordan man tilføjer det, i stedet for at vise et blankt tomrum. Vælg hjælpsomme, sikre standarder, så de fleste brugere lykkes uden at ændre noget, og gør standarden til den mulighed, der tjener brugerens interesse, ikke blot virksomhedens.

### Design for tillid og sikkerhed; undgå dark patterns

Præsentér valg ærligt og symmetrisk: at afmelde bør være lige så let som at tilmelde, og at afslå bør være lige så fremtrædende som at acceptere. Brug ikke confirmshaming ("Nej tak, jeg bryder mig ikke om at spare penge"), forhåndsafkrydset samtykke, skjulte omkostninger, falsk hast eller roach-motel-flows, der er lette at komme ind i og svære at forlade. Ud over etikken er mange af disse mønstre nu ulovlige under forbrugerbeskyttelses- og privatlivslovgivning. Vær særligt omhyggelig med kommunikation om sikkerhed, privatliv og penge, for det er der, manipulation gør mest skade, og hvor svindlere efterligner legitime beskeder.

### Design kommunikation på tværs af kanaler sammenhængende

E-mail, pushnotifikationer, SMS og beskeder i appen er en del af én rejse. Koordinér dem, så brugere ikke spammes eller modsiges på tværs af kanaler. Respektér opmærksomhed: underret kun, når det er rettidigt og nyttigt, lad brugere styre frekvens og kanal, og gør hver besked tilgængelig og enkel. Sørg for, at transaktionel kommunikation (kvitteringer, alarmer, frister) er pålidelig, klar og svær at forveksle med [phishing](https://en.wikipedia.org/wiki/Phishing): ensartet afsenderidentitet og formatering hjælper brugere med at stole på ægte beskeder.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Centraliseret indholdsstrategi | Ensartethed, tillid, genbrug | Overhead, kan sinke teams, hvis den bliver en flaskehals |
| Almindeligt sprog overalt | Forståelse, inklusion, juridisk compliance | Indsats at omskrive; specialister kan modsætte sig at miste jargon |
| Legende, brandet stemme | Personlighed, mindeværdighed | Kan misse i fejl, højindsatssituationer eller forskellige målgrupper |
| Stærke standarder | De fleste brugere lykkes uden anstrengelse | Risiko for nudging; skal sættes i brugerens interesse |
| Rig kommunikation på tværs af kanaler | Rettidig, engagerende | Bliver let støj; byrde med privatliv og samtykke |

Den centrale spænding er mellem brandpersonlighed og klarhed og mellem engagement og respekt for opmærksomhed. Konteksten løser den. Lad stemmen tilføje varme, hvor indsatsen er lav, og prioritér almindelig, rolig klarhed, hvor indsatsen er høj (fejl, penge, sikkerhed, juridisk). Ved standarder og beskeder er den etiske linje enkel: tjener designet brugerens ægte interesse, eller udnytter det deres uopmærksomhed?

## Spørgsmål til drøftelse med dit team

1. **Er fejlmeddelelser, tomme tilstande og standarder fælles mønstre i vores designsystem, eller genopfundet på hver skærm?** Det er de øjeblikke med højest løftestang i hele oplevelsen: en god fejl siger, hvad der gik galt, hvorfor og hvordan det rettes, uden bebrejdelse eller en kode, man ikke kan handle på, og en god tom tilstand lærer folk, hvad der hører hjemme der, i stedet for at vise et tomrum. Når hvert team skriver dem fra bunden, får I "Error 500" ét sted og en hjælpsom besked et andet, og brugerne mister tilliden. Beslut, om disse mønstre bor i designsystemet sammen med komponenterne, med aftalte strukturer og eksempeltekst. Tag tre rigtige fejlmeddelelser og tre tomme tilstande fra jeres produkt med og læs dem højt. Hvis nogen bebrejder brugeren eller ikke tilbyder en vej til genopretning, har I fundet jeres første backlogpunkt.

2. **Er vores indhold struktureret og genbrugeligt, eller hårdkodet og duplikeret på tværs af skærme?** Tekst tastet direkte ind i en komponent kan ikke opdateres ensartet, kan ikke gennemgås og kan ikke lokaliseres uden en kodeændring, hvilket stille blokerer hvert fremtidigt marked og hver ordlydsrettelse. Det bliver akut i skala, hvor det samme begreb får tre navne, fordi der ikke er nogen ordliste og ingen enkelt kilde. Beslut, hvordan indhold gemmes, hvem der ejer det kontrollerede ordforråd, og hvordan en ordlydsændring udbredes uden en udrulning pr. skærm. Tag et eksempel på et begreb, jeres produkt staver eller navngiver inkonsistent, med og spor, hvor mange steder I skulle redigere. Hvis svaret er "søg og erstat i hånden," er jeres indhold fanget i koden.

3. **Hvornår træder indholdsdesignere ind i arbejdsgangen, og hvem har autoritet til at blokere et manipulerende flow?** Hvis indhold er en eftertanke (lorem ipsum til lancering, så hvad der nu passer i feltet), får de ord, der bærer det meste af oplevelsen, mindst omtanke, og dark patterns smutter ind under vækstpres, fordi ingen ejer ærligheden. Aftal, at indhold er et designinput fra start, med en stemme-og-tone-guide og gennemgang i arbejdsgangen, og navngiv, hvem der kan stoppe et confirmshaming- eller forhåndsafkrydset-samtykke-flow, før det leveres. Dette er nu et juridisk spørgsmål såvel som et etisk, fordi forbrugerbeskyttelses- og privatlivslovgivning i stigende grad forbyder disse mønstre. Tag et nyligt flow med og spørg, om det at afslå er lige så let og lige så fremtrædende som at acceptere. Hvis det ikke er, så beslut i dag, hvem der er ansvarlig for at rette det.

4. **Hvilket læseniveau skriver vi faktisk til, og hvordan ved vi, at rigtige brugere forstår vores indhold med højest indsats?** Almindeligt sprog er let at påstå og svært at bevise: forfattere skriver på deres eget forståelsesniveau, og de læsere, der mest har brug for klarhed, folk med lavere læsefærdigheder og ikke-modersmålstalende, er mindst repræsenteret i rummet. For en stor organisation akkumulerer indsatsen, fordi ét forvirrende ydelsesbrev eller én sikkerhedsadvarsel kopieres til millioner af modtagere, før nogen måler, om den lander. Beslut et mål for læseniveau for hele jeres målgruppe, udvid eller forbyd jargon ved første brug, og forpligt jer til forståelsestest med rigtige mennesker frem for at stole på en læsbarhedsscore alene. Tag jeres tre kommunikationer med mest trafik og dokumentationen for, at nogen uden for forfatterteamet kan handle korrekt på dem, med. I virksomheds- og offentlige sammenhænge så tilføj den gældende lov eller politik om almindeligt sprog og vær ærlige om, hvilke dokumenter der ville dumpe en revision i dag.

5. **Hvem styrer, hvordan, hvornår og hvor ofte vi sender beskeder til brugere på tværs af e-mail, push, SMS og i appen, så hele rejsen forbliver sammenhængende?** Når hvert team ejer sin egen kanal, bliver brugere spammet, modsagt og til sidst trænet til at ignorere eller afmelde alt, også de transaktionelle beskeder, der faktisk betyder noget. At koordinere rejsen betyder at aftale frekvensgrænser, give brugere reel kontrol over kanal og samtykke og holde en ensartet afsenderidentitet, så ægte beskeder er svære at forveksle med phishing, der efterligner dem. Tag en log over hver besked, en enkelt bruger kunne modtage i en travl uge, med og tæl dubletterne, modsigelserne og dem, der kunne forveksles med svindel. Det modstridende træk er engagementspres, da vækstteams altid vil have endnu et berøringspunkt, og respekt for opmærksomhed ikke har nogen umiddelbar måling. I virksomheds- og offentlige sammenhænge så tilføj de samtykke- og privatlivsforpligtelser, der gør uopfordret kommunikation til juridisk eksponering, og navngiv, hvem der kan nedlægge veto mod en kampagne, der misbruger kanalen.

6. **Hvordan måler vi, om vores indhold virker, og hvor viger brandstemmen helt for almindelig klarhed?** Indhold, der aldrig måles, driver på smag, og den højeste stemme vinder ordlyden frem for brugeren. Bind indhold til reelle signaler, supportticketkategorier, gennemførelses- og konverteringstragte, fejl- og klagerater og afmeldings- og klagerater, så en omskrivning bedømmes på udfald i stedet for præference. Aftal samtidig, hvor stemmen må vige: en vittig fejl, en spøgefuld pengebesked eller en legende sikkerhedsadvarsel eroderer tillid netop, når indsatsen er højest. Tag et flow med høj trafik, den måling det flytter, og en foreslået linje for, hvor personlighed hjælper, og hvor rolig klarhed er obligatorisk, med. For en stor eller offentlig organisation så navngiv, hvem der ejer den linje, og hvordan en bevist forbedring udbredes på tværs af teams, frem for at vinde én skærm og miste resten.

## Sektorperspektiv

**Startup.** Uden skribent og med to ingeniører så behandl indhold som en grundlæggeropgave, ikke en ansættelse. Brug en dag på de ord med højest løftestang: giv knapper navn efter deres handling, forvandl det tomme dashboard til en førstegangstutorial, og få fejl til at sige, hvad der skal rettes. Skriv en stemmeguide på én side, så tonen forbliver almindelig, når I vokser, og spring ordlisten og indholdsplatformen over, til inkonsistens faktisk gør ondt.

**Lille virksomhed.** Uden en indholdsdesigner og med et stramt budget så støt jer til de konventioner for almindeligt sprog og microcopy, der er indbygget i de værktøjer, I allerede bruger, og køb skabeloner til transaktionelle e-mails frem for at skabe dem fra bunden. Prioritér de få skærme, der mister kunder, en tom tilstand, en checkoutfejl, et opsigelsesflow, og hold det at afslå lige så let som at acceptere, så I holder jer fri af dark pattern-lovgivning. Kør en gratis læsbarhedskontrol over alt kundevendt, før det leveres.

**Stor virksomhed.** Problemet er sammenhæng på tværs af mange teams: en fælles stemme-og-tone-guide, et kontrolleret ordforråd, så ét begreb beholder ét navn, og mønstre for fejl, tomme tilstande og standarder, der bor i designsystemet ved siden af komponenterne. Gem indhold i versionsstyring, struktureret og lokaliserbart frem for hårdkodet, giv det ejere og gennemgang, og koordinér kommunikation på tværs af kanaler, så brugere ikke spammes eller modsiges. Styr ærlighed centralt, så intet team leverer confirmshaming eller forhåndsafkrydset samtykke under vækstpres.

**Offentlig sektor.** Almindeligt sprog er ofte en juridisk pligt, ikke en præference, så følg de gældende standarder og test forståelse med rigtige modtagere, herunder mennesker med lavere læsefærdigheder og ikke-modersmålstalende. Led hver meddelelse med handlingen og fristen, fjern jargonen, og få hver kommunikation til klart at identificere sin afsender, så folk ikke forveksler den med svindel. Hold valg ærlige og symmetriske, offentliggør de indholdsstandarder, I holder jer til, og giv folk en enkel vej til at anfægte en afgørelse, de ikke forstår.

## Eksempler

**Startup.** Et lille startup uden skribenter bemærkede, at de fleste prøvebrugere tilmeldte sig, så et tomt dashboard og aldrig kom tilbage. En grundlægger brugte en dag på at omskrive microcopyen: den tomme tilstand forklarede nu, hvad man skulle tilføje, og tilbød et eksempelprojekt med ét klik, knapper fik navn efter deres handling i stedet for at sige "OK," og fejlmeddelelser sagde, hvad der gik galt, og hvordan det rettes. Aktiveringen steg mærkbart ugen efter, og den samme grundlægger skrev en stemmeguide på én side, så hele teamet ville holde tonen almindelig og ensartet, efterhånden som de voksede.

**Stor virksomhed.** Et SaaS-firma omskrev sin onboarding, sine fejlmeddelelser og sine tomme tilstande omkring klar, handlingsorienteret microcopy og en dokumenteret stemmeguide. Supporttickets for "hvordan gør jeg..."-spørgsmål faldt, aktiveringen blev bedre, fordi tomme tilstande nu lærte brugere, hvad de skulle gøre, og konverteringen fra prøve til betalende steg. Virksomheden fjernede også et confirmshaming-opsigelsesflow, efter det skadede tilliden og vakte kritik, og erstattede det med en ligefrem, symmetrisk opsigelsessti, som, modsat intuitionen, forbedrede omdømmet og genvundne kunder.

**Offentlig sektor.** Et agentur omskrev et brev om ydelsesberettigelse, som modtagere rutinemæssigt misforstod, hvilket forårsagede overskredne aftaler og uberettiget ydelsestab. Ved at anvende standarder for almindeligt sprog ledte teamet med den krævede handling og fristen, fjernede juridisk jargon og testede forståelse med rigtige modtagere, herunder ikke-modersmålstalende. Forståelsen steg kraftigt, og raten af overskredne frister faldt, hvilket reducerede klager og sagsbehandling. Fordi brevet nu klart identificerede sig selv og sin afsender, var modtagere også mindre tilbøjelige til at forveksle det med svindel.

## Business case: motivation, ROI og TCO

Indholdskvalitet driver målbare udfald: højere opgavegennemførelse og konvertering, lavere supportvolumen, færre fejl og klager og større tillid og fastholdelse. Klar microcopy og hjælpsomme standarder reducerer antallet af folk, der går i stå og kontakter support eller opgiver. Kommunikation i almindeligt sprog reducerer nedstrøms omkostning: færre forvirrede opkald, færre fejl at rette, færre klager i offentlige sammenhænge. Troværdigt, ikke-manipulerende design beskytter omdømmet og reducerer juridisk eksponering, efterhånden som regulering af dark patterns strammes.

Hvad angår TCO er adoptionsomkostningen beskeden: indholdsdesignere eller uddannede skribenter, en stemmeguide og ordliste og gennemgang i arbejdsgangen. Omkostningen ved ikke at adoptere er diffus og stor: support- og callcenterbelastning, opgivne transaktioner, fejlrettelse, klager, regulatoriske sanktioner for manipulerende mønstre eller ikke-overensstemmende kommunikation og eroderet tillid. Disse omkostninger lander i support og drift frem for produktbudgettet, så ledelsen har tendens til at undervægte dem.

For at føre sagen så bind indholdsarbejde til supportticketkategorier, gennemførelses- og konverteringstragte, fejl- og klagerater og afmeldings- eller klagerater. En lille omskrivning af et flow med høj trafik eller en kommunikation med højt volumen producerer som regel en klar, tilskrivelig forbedring, og det er det, der retfærdiggør at skalere praksissen.

## Anti-mønstre og faldgruber

- **Indhold som en eftertanke**: lorem ipsum til lancering, så hvad der nu passer i feltet.
- **Jargon og internt sprog**: at skrive fra organisationens perspektiv, ikke brugerens.
- **Bebrejdende, uhjælpsomme fejl**: "Error 500" eller "Ugyldigt input" uden vej til genopretning.
- **Blanke tomme tilstande**: et tomrum, hvor vejledning burde være.
- **Dark patterns**: confirmshaming, forhåndsafkrydset samtykke, skjulte omkostninger, roach motels, falsk hast.
- **Inkonsistent terminologi**: tre navne for ét begreb på tværs af produktet.
- **Notifikationsspam**: overbeskeder, der træner brugere til at ignorere eller afmelde.
- **Utestet læsbarhed**: at antage, at indhold er klart, uden at teste med rigtige brugere.
- **Hårdkodet, duplikeret tekst**: umulig at opdatere eller lokalisere ensartet.

## Modenhedsmodel

**Niveau 1: Opstart.** Ingen indholdspraksis. Ord skrives ad hoc af den, der bygger skærmen, reagerende på det, feltet har brug for i øjeblikket. Terminologi og tone er inkonsistente, fejl bebrejder brugeren eller viser koder, man ikke kan handle på, og tomme tilstande er et blankt tomrum.

**Niveau 2: Udvikling.** En stilguide eller nogle stemmenoter kan findes, og nogle få teams har samlet vaner op i almindeligt sprog. Indhold er stadig en aktivitet sent i forløbet og pr. team med lidt genbrug og lidt test, så kvalitet og ensartethed varierer vidt fra den ene squad til den næste.

**Niveau 3: Standardisering.** En indholdsstrategi, en stemme-og-tone-guide og et kontrolleret ordforråd er dokumenteret og brugt på tværs af teams. Almindeligt sprog er standarden og, hvor det kræves, overensstemmende; fejl, tomme tilstande og standarder følger fælles mønstre; indhold er struktureret, gennemgået og genbrugeligt frem for hårdkodet pr. skærm.

**Niveau 4: Styring.** Indhold måles mod udfald med data. Læsbarheds- og forståelsestestresultater, supportticketkategorier, gennemførelses- og konverteringstragte, fejl- og klagerater og afmeldings- og klagerater følges mod baselines, og hver indholdsændring bedømmes på, om den flytter disse tal. Dark patterns revideres mod en dokumenteret politik, og beskedfrekvens på tværs af kanaler overvåges mod aftalte grænser.

**Niveau 5: Orkestrering.** Indhold forbedres løbende og er integreret på tværs af organisationen. Mønstre bor i designsystemet, lokaliseret og tilgængeligt som standard; det kontrollerede ordforråd holder ét navn pr. begreb overalt; kommunikation på tværs af kanaler er koordineret og brugerstyret; og praksissen tilpasser sig, efterhånden som regulering, målgruppe og kanaler skifter, og pensionerer og omskriver indhold på dokumentation frem for mening.

## Idéer til drøftelse

- Hvor bør brandstemmen helt vige for almindelig klarhed, og hvem afgør linjen?
- Hvordan håndhæver I en politik uden dark patterns, når vækstteams er presset på målinger?
- Hvordan holder I terminologien ensartet på tværs af mange teams uden at flaskehalse dem?
- Hvilket læseniveau er det rette for en tjeneste brugt af hele befolkningen?
- Hvordan bør notifikationsfrekvens og kanalkontrol styres på tværs af organisationen?
- Hvordan gør I ægte kommunikation skelnelig fra phishing, der efterligner den?

## Vigtigste pointer

- Indhold er kerne-UI; design ord med samme stringens som visuelt.
- Almindeligt sprog forbedrer forståelsen for alle og er ofte juridisk påkrævet.
- Fejl, tomme tilstande og standarder er øjeblikke med høj løftestang: design dem til at hjælpe.
- Undgå dark patterns: præsentér valg ærligt og symmetrisk; de er i stigende grad ulovlige.
- Ensartet terminologi og tone bygger tillid og sænker den kognitive belastning.
- Koordinér kommunikation på tværs af kanaler og respektér brugerens opmærksomhed og kontrol.
- Indholdskvalitet viser sig direkte i supportvolumen, gennemførelse, fejl og tillid.

## Referencer og videre læsning

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson and Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton and Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (dark patterns research)
- U.S. Federal Plain Language Guidelines and PlainLanguage.gov
- UK Government Digital Service, content design and style guidance
- Nielsen Norman Group, articles on error messages, microcopy, and readability
