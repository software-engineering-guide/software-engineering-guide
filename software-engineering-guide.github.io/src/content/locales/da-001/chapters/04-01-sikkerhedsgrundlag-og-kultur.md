# 4.1 Sikkerhedsgrundlag og kultur

## Overblik og motivation

Sikkerhed er ikke en funktion, du skruer på til sidst, og det er ikke jobbet for ét specialiseret team, der sidder adskilt fra udviklingen. I en stor organisation er sikkerhed en egenskab ved, hvordan hele systemet designes, bygges, drives og styres. Når tusinder af ingeniører leverer kode på tværs af hundredvis af tjenester, afgør det svageste led, hvor stor skade en hændelse kan gøre. Én fejlkonfigureret lagerspand, én upatchet afhængighed eller én overprivilegeret tjenestekonto kan blotlægge millioner af poster. Grundlag og kultur er det, der forhindrer det i skala.

For virksomheder er indsatsen økonomisk og omdømmemæssig: brudomkostninger, regulatoriske bøder, tabte kunder og nedtrykte værdiansættelser. For det offentlige rækker den til national sikkerhed, offentlig tillid og kontinuiteten i væsentlige tjenester. Begge sammenhænge deler en hård sandhed: du kan ikke håndhæve sikkerhed alene gennem kontroller og porte. Den skal internaliseres af de mennesker, der udfører arbejdet. En kultur, hvor ingeniører forstår trusler, føler ejerskab og belønnes for at rejse bekymringer, giver langt bedre resultater end en, der læner sig op ad et overbelastet sikkerhedsteam, der spiller målmand.

Dette kapitel fremlægger de mentale modeller og kulturelle praksisser, der understøtter hvert andet sikkerhedskapitel i denne guide. Det dækker at gøre sikkerhed til alles opgave, [trusselsmodellering](https://en.wikipedia.org/wiki/Threat_model), den sikre udviklingslivscyklus, grundlæggende arkitekturprincipper som [forsvar i dybden](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) og [zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) og hvordan man prioriterer sikkerhedsarbejde efter reel risiko frem for frygt eller mode.

*Se også:* kapitel 4.2 (applikationssikkerhed), kapitel 4.3 (infrastruktur- og cloudsikkerhed), kapitel 4.4 (sikkerhedsdrift) og kapitel 4.6 (compliance og styring) bygger på dette grundlag.

## Grundprincipper

- **Sikkerhed er alles opgave.** Hver ingeniør, produktchef og driftsansvarlig ejer sikkerheden af det, de bygger. Sikkerhedsteamet muliggør, rådgiver og reviderer; det gør ikke og kan ikke gøre arbejdet alene.
- **Antag brud.** Design, som om angribere allerede er inde. Minimér, hvad en kompromitteret komponent kan nå.
- **Forsvar i dybden.** Ingen enkelt kontrol er tilstrækkelig. Læg uafhængige kontroller i lag, så svigt af én ikke betyder svigt af alle.
- **[Mindste privilegium](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Giv den mindste adgang, der er nødvendig, i den korteste tid, og træk den automatisk tilbage, når den ikke længere er nødvendig.
- **Skift til venstre.** Find og ret problemer så tidligt som muligt, når de er billigst at udbedre.
- **Risikobaseret prioritering.** Brug kræfterne, hvor kombinationen af sandsynlighed og konsekvens er højest, vejledt af CIA-triaden (fortrolighed, integritet og tilgængelighed), ikke på det, der var i nyhederne denne uge.
- **Skyldfri læring.** Behandl sikkerhedshændelser og næsten-uheld som læringsmuligheder, ikke anledninger til straf.

## Anbefalinger

### Etablér et program for sikkerhedsambassadører

Indlejr en udpeget sikkerhedsambassadør i hvert udviklingsteam. Ambassadører er ikke fuldtids-sikkerhedsspecialister. De er ingeniører med ekstra træning og en direkte linje til det centrale sikkerhedsteam. De gennemgår designs, triagerer fund, besvarer kollegaers spørgsmål og bærer sikkerhedskontekst ind i planlægningen. Det skalerer sikkerhedsekspertise på tværs af organisationen uden at ansætte en specialist til hvert team, og det bygger tillid, fordi rådet kommer fra en kollega, der faktisk kender kodebasen.

Giv ambassadører reel støtte: et fast forum til at dele det, de lærer, budget til træning og konferencer, anerkendelse i præstationssamtaler og tid taget ud af deres leveringsforpligtelser. Et ambassadørprogram, der kun findes på papiret, producerer ingenting.

### Praktisér trusselsmodellering rutinemæssigt

Trusselsmodellering er den disciplinerede vane at spørge "hvad kan gå galt?", før du bygger. Gør det for nye tjenester, større funktioner og enhver ændring af tillidsgrænser. Hold det let nok til, at det faktisk sker ofte.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** er en praktisk tjekliste afbildet til sikkerhedsegenskaber: Spoofing (autentificering), Tampering (integritet), Repudiation (uafviselighed), Information disclosure (fortrolighed), Denial of service (tilgængelighed) og Elevation of privilege (autorisation). Gå hvert dataflow igennem og spørg, hvordan hver kategori gælder.
- **PASTA** (Process for Attack Simulation and Threat Analysis) er en tungere, risikocentreret metode i syv trin, der knytter tekniske trusler til forretningsmæssig konsekvens; brug den til højværdisystemer.
- **[Angrebstræer](https://en.wikipedia.org/wiki/Attack_tree)** nedbryder et mål ("stjæl kundedata") til de forgrenede trin, en angriber ville tage, og hjælper dig med at finde og beskære stier.

Hold trusselsmodeller som levende dokumenter ved siden af koden, og genbesøg dem, hver gang arkitekturen ændrer sig.

### Byg en sikker softwareudviklingslivscyklus

Væv sikkerhed ind i hver fase frem for at behandle den som en afsluttende port:

- **Krav:** indfang sikkerheds- og privatlivskrav sammen med de funktionelle.
- **Design:** trusselsmodellér og gennemgå tillidsgrænser.
- **Implementering:** håndhæv standarder for sikker kodning, kodegennemgang og scanning efter hemmeligheder før commit.
- **Test:** kør [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (statisk applikationssikkerhedstest), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dynamisk applikationssikkerhedstest) og afhængighedsscanning i pipelinen (se kapitel 4.4).
- **Udgivelse:** verificér proveniens, signér artefakter og tjek konfiguration.
- **Drift:** overvåg, patch og reagér.

Pointen med at skifte til venstre er ikke at stable alt arbejdet tidligere og overvælde ingeniører. Det er at fange de typer fejl, der er langt billigere at rette tidligt.

### Adoptér zero trust-arkitekturprincipper

Traditionel perimetersikkerhed antager, at alt inde i netværket er pålideligt. Den antagelse fejler i det øjeblik, en angriber får fodfæste. Zero trust erstatter implicit netværkstillid med eksplicit, kontinuerlig verifikation: autentificér og autorisér hver anmodning baseret på identitet, enhedens tilstand og kontekst, uanset hvor den kommer fra på netværket. Kombinér stærk identitet, autorisation efter mindste privilegium, mikrosegmentering og [kryptering](https://en.wikipedia.org/wiki/Encryption) overalt. Zero trust er en rejse, ikke et produkt, så tilgå det ét skridt ad gangen.

### Prioritér efter risiko med CIA-triaden

Ram hvert aktiv og hver kontrol ind omkring **fortrolighed**, **integritet** og **tilgængelighed**. Ikke alle data har brug for samme beskyttelse: en offentlig marketingside og en database med sundhedsjournaler har vildt forskellige behov for fortrolighed. Klassificér jeres aktiver, estimér sandsynlighed og konsekvens af kompromittering, og ret knappe sikkerhedsressourcer mod kombinationerne med højest risiko. Skriv jeres risikobeslutninger ned, så andre kan gennemgå og forsvare dem senere.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Centralt sikkerhedsteam ejer al sikkerhed | Dyb ekspertise, ensartede standarder | Flaskehals, ingeniører mister engagement, skalerer ikke |
| Distribueret sikkerhed (ambassadører) | Skalerer, bygger ejerskab, hurtigere feedback | Kræver investering, ujævne færdigheder, kræver koordinering |
| Tung trusselsmodellering på forhånd af alt | Grundig, fanger designfejl | Sinker leveringen, kan blive afkrydsning |
| Let, risikorettet trusselsmodellering | Hurtig, fokuseret på det vigtige | Kan misse trusler i "lavrisiko"-systemer |
| Strenge porte, der blokerer udgivelser | Håndhæver compliance | Gnidning, tilskynder til omveje |

Den centrale spænding er mellem hastighed og assurance. Læn dig for langt mod porte og central kontrol, og du skaber gnidning, ingeniører går uden om, hvilket avler skygge-IT og harme. Læn dig for langt mod autonomi uden støtte, og du får inkonsistent, urevideret sikkerhed. Det bæredygtige svar er en stærk kultur med muliggørende rækværk: automatiseret, hvor du kan, menneskeligt, hvor dømmekraft er påkrævet, og altid forklaret frem for blot pålagt.

## Spørgsmål til drøftelse med dit team

1. **Hvilke af jeres systemer fortjener tung trusselsmodellering, og hvem afgør niveauet?** I en stor ejendom kan I ikke køre en PASTA-analyse i syv trin på hver tjeneste, så I har brug for en eksplicit regel for, hvornår en STRIDE-gennemgang på 30 minutter er nok, og hvornår et højværdisystem fortjener dyb, forretningskonsekvensdrevet modellering. Forankr beslutningen i jeres CIA-klassificering: systemer med regulerede journaler, betalingsflows eller autentificeringslogik sidder øverst, og en offentlig marketingside gør ikke. I virksomheds- og offentligt arbejde vil en revisor bede jer forsvare, hvorfor et givet system blev modelleret, som det blev, så skriv niveaukriterierne ned og navngiv den ejer, der anvender dem. Tag jeres nuværende aktivklassificering og en liste over tjenester uden trusselsmodel med til mødet, for hullet mellem dem er jeres reelle risiko. Kan I ikke blive enige om barren, falder I tilbage til at modellere alt let eller intet dybt, og begge dele svigter jer.

2. **Når en sikkerhedsambassadør og en leveringsfrist støder sammen, hvem kan så faktisk standse udgivelsen?** Et ambassadørprogram ændrer kun udfald, hvis ambassadøren bærer reel autoritet, ikke blot ekstra træning og gode intentioner. Beslut på forhånd, om en ambassadør kan blokere en udgivelse, om de eskalerer til det centrale AppSec-team, og hvilken alvorlighed af et fund der retfærdiggør at standse leveringen versus blot at spore det. Det betyder mest under pres, når en produktchef vil frafalde en designfejl ugen før lancering, hvilket netop er, når uadresserede fejl er dyrest at rette. Tag et nyligt eksempel med, hvor en sikkerhedsbekymring mødte en frist, og spor hvem der besluttede, og hvordan, for den historie afslører jeres sande eskaleringssti. Hvis det ærlige svar er, at levering altid vinder, er jeres ambassadører dekorative, og I bør rette incitamentet, før I tilføjer flere af dem.

3. **Hvad ændrer "antag brud" konkret i jeres næste designgennemgang?** Princippet er let at nikke til og svært at operationalisere, så fastgør det til specifikke tilsagn: hvilke tillidsgrænser I vil stramme, hvor I vil tilføje mikrosegmentering, og hvordan I vil skrumpe det, en enkelt kompromitteret tjenestekonto kan nå. For et stort team er gevinsten reduktion af sprængradius, så en angriber, der lander i én tjeneste, ikke kan svinge videre til datalageret bagved. I virksomheds- og offentlige sammenhænge former det også jeres beslutninger om mindste privilegium og kortlivede legitimationer, som er billige at designe ind og smertefulde at eftermontere. Tag ét reelt tjenestediagram med og spørg, hvad en angriber gør, når de ejer weblaget, og forpligt jer så til to indgrænsningsændringer dette kvartal. Vag enighed om, at brud sker, er værdiløs, medmindre den flytter en tilladelse, en netværksregel eller en legitimations levetid.

4. **Hvordan ved I, at jeres sikkerhedskultur faktisk forbedres, og hvilken måling ville I forsvare over for bestyrelsen?** Gennemførelsesrater for træning og antal sager er lette at indsamle og næsten ubrugelige, fordi de måler aktivitet frem for risikoreduktion, og en stor organisation drukner i dem. Vælg udfaldsmålinger, I faktisk ville satse et budget på: medianen af tid til at udbedre fund med høj alvorlighed, andelen af tjenester med en aktuel trusselsmodel, den brøkdel af hændelser, der fanges før produktion, og raten af selvrapporterede næsten-uheld, som bør stige, efterhånden som tilliden vokser, frem for at falde. Det modstridende hensyn er, at enhver god måling kan spilles, så par hver med en modmåling og gennemgå tendensen frem for øjebliksbilledet. Tag jeres nuværende dashboard med og spørg, hvilke tal der ville ændre sig, hvis sikkerheden reelt blev værre; dem, der ikke ville, er dekoration. I virksomheds- og offentlige sammenhænge vil en tilsynsmyndighed eller et revisionsudvalg bede om dokumentation for, at kontroller virker, så vælg målinger, I kan forsvare under granskning, frem for dem, der blot ser grønne ud.

5. **Hvad sker der egentlig næste gang en ingeniør rapporterer en fejl, og er jeres proces skyldfri i praksis eller kun på slidet?** Skyldfri læring er det princip, der oftest bekendes og sjældnest leves, fordi den første alvorlige hændelse tester, om ledelsen virkelig mener det. Beslut på forhånd, hvordan I adskiller ansvar for at rette et problem fra straf for at have forårsaget det, og hvem der leder gennemgangen efter hændelsen, så den forbliver om ødelagte systemer frem for navngivne personer. Spændingen er reel: interessenter vil have nogen holdt ansvarlig, men at straffe rapportøren garanterer, at den næste fejl forbliver skjult, til den bliver et brud. Tag jeres to seneste hændelsesgennemgange med og tjek, om de skyldte en person eller en kontrol, og om ingeniøren, der slog alarm, blev takket eller stille sat uden for. For offentlige og regulerede virksomheder hæver obligatoriske regler om offentliggørelse af brud indsatsen yderligere, fordi en kultur, der skjuler fejl, også vil misse de indberetningsfrister, der bærer juridiske sanktioner.

6. **Hvem ejer gnidningen i jeres shift-left-værktøj, og køber I det, bygger det eller drukner i det?** Automatiseret statisk og dynamisk analyse, afhængighedsscanning og scanning efter hemmeligheder er rygraden i en sikker udviklingslivscyklus, men en pipeline, der oversvømmer ingeniører med falske positiver, lærer dem at ignorere sikkerhedsoutput, hvilket er værre end ingen scanning. Beslut, hvem der justerer værktøjerne, hvem der triagerer fundene, og om I køber en integreret platform eller samler open source-scannere, I derefter selv skal vedligeholde. De konkurrerende hensyn er dækning versus støj og kontrol versus omkostning: en billig scanner, der råber ulv, brænder den tillid, et ambassadørprogram brugte år på at bygge. Tag jeres nuværende rate af falske positiver, den gennemsnitlige tid ingeniører venter på et blokerende tjek, og listen over teams, der stille har deaktiveret en port. I store virksomheder og det offentlige så tilføj indkøbs- og værktøjsvildtvækstvinklen, fordi ti teams, der hver køber deres egen scanner, producerer inkonsistent dækning, ingen revisor kan afstemme.

## Sektorperspektiv

**Startup.** Uden sikkerhedsteam og med lidt runway er kultur din eneste overkommelige kontrol. Gør en trusselsmodellering på 30 minutter ved et whiteboard til vane før enhver funktion, der rører autentificering eller betalinger, slå mindste privilegium og MFA til overalt, fordi de ikke koster noget, og hold en skyldfri kanal, hvor enhver kan flage en bekymring. Spring tung proces og tunge værktøjer over; de stiftende ingeniører kan ikke vedligeholde dem, og den disciplin, du bygger nu, er det, der lader virksomhedskøbere stole på dig senere.

**Lille virksomhed.** I har ingen dedikeret sikkerhedsspecialist og et stramt budget, så støt jer til sikre standarder i de værktøjer, I allerede køber, frem for at opstille jeres egen pipeline. Foretræk administrerede platforme, der håndhæver MFA, patching og mindste privilegium for jer, og behandl sikkerhed som et datahygiejnespørgsmål: vid hvilke følsomme data I holder, og hvem der kan nå dem. Når I skal vælge byg versus køb, så køb, for en administreret kontrol, I holder opdateret, slår en skræddersyet, I lader rådne.

**Stor virksomhed.** I skalaen af hundredvis af tjenester og tusinder af ingeniører er udfordringen ensartethed og styring på tværs af mange teams. Kør et program for sikkerhedsambassadører, standardisér trusselsmodelleringsniveauer knyttet til CIA-klassificering, og lever asfalterede skabeloner og automatiserede pipelinetjek, så hvert team arver gode standarder. Følg udbedrings- og dækningsmålinger mod baselines, og hold et revisionsspor, der viser, hvorfor hvert system blev modelleret og kontrolleret, som det blev.

**Offentlig sektor.** Indkøbsregler, åbenhedsforpligtelser og offentlig ansvarlighed former hvert valg. Zero trust-principper og kortlivede legitimationer er ofte påbudt af politik, og I skal kunne vise en revisor en dokumenteret, risikobaseret begrundelse for, hvor hærdningsbudgettet gik hen. Prioritér først de systemer, der holder de mest følsomme borgerposter, offentliggør sikkerhedsforanstaltningerne, hvor offentligheden har ret til at vide, og kræv at leverandører oplyser begrænsninger frem for at acceptere uigennemsigtige sorte bokse.

## Eksempler

**Startup.** Et startup på ti personer har intet sikkerhedsteam og intet budget til et, så de to stiftende ingeniører gør trusselsmodellering til en vane på 30 minutter ved et whiteboard før enhver funktion, der rører autentificering eller betalinger, hvor de spørger, hvad der kan gå galt, og hvem der ville ønske, at det skete. De adopterer nogle få grundlæggende vaner, der ikke koster noget: mindste privilegium på hver cloudrolle, MFA på hver konto og en skyldfri kanal, hvor enhver kan rejse en bekymring uden frygt for skyld. Da de senere rejser en runde, og virksomhedskøbere spørger, hvordan de håndterer sikkerhed, lader den tidlige kultur dem svare ærligt i stedet for at skynde sig at opfinde en.

**Stor virksomhed.** En global bank med 6.000 ingeniører kører et program for sikkerhedsambassadører med én uddannet ambassadør pr. squad. Ambassadører deltager i et månedligt laug, gennemfører kvartalsvis træning og leder trusselsmodellering for hver ny tjeneste med STRIDE. Det centrale AppSec-team vedligeholder asfalterede skabeloner og automatiserede pipelinetjek. Over to år faldt medianen af tid til at udbedre fund med høj alvorlighed fra 45 dage til 9, og trusselsmodellering i designfasen fangede en autorisationsfejl i en betalings-API, før den nåede produktion, hvilket undgik en sandsynlig indberetningspligtig hændelse.

**Offentlig sektor.** En national skatteadministration, der moderniserer legacy-systemer, adopterer zero trust-principper påbudt af politik. Hvert internt tjenestekald autentificeres med kortlivede legitimationer og autoriseres pr. anmodning; netværkssegmenter giver ikke længere tillid. Administrationen trusselsmodellerer hver borgervendt tjeneste mod angrebstræer med rod i "eksfiltrér skatteyderposter" og "ændr en indberetning." Risikobaseret prioritering, afstemt til CIA-konsekvensniveauer, fokuserer hærdningsbudgettet på de systemer, der holder de mest følsomme poster, først.

## Business case: motivation, ROI og TCO

Omkostningen ved at bygge en sikkerhedskultur er reel: ambassadørtid, træning, værktøj og den beskedne belastning ved at lave trusselsmodellering og gennemgange. Men den omkostning er lille ved siden af omkostningen ved ikke at gøre det. Et gennemsnitligt større databrud løber op i millioner, når du tæller undersøgelse, underretning, udbedring, regulatoriske bøder, juridisk eksponering og tabt forretning. Offentlige brud tilføjer missionsforstyrrelse og erosion af offentlig tillid, som ingen faktura fanger fuldt ud.

Afkastet af sikkerhedsinvestering kommer fra tre steder: **undgåede hændelser** (bruddet, der aldrig sker), **reduceret udbedringsomkostning** (fejl rettet på designtidspunktet koster en brøkdel af dem rettet i produktion) og **hurtigere levering** (asfalterede veje og automatiserede tjek lader teams levere med tillid i stedet for at vente på manuel gennemgang). Når du fører sagen over for ledelsen, så ram sikkerhed ind som risikostyring med en pris, ikke som et abstrakt gode. Vis det forventede tab (sandsynlighed gange konsekvens) for de øverste risici, omkostningen ved at reducere dem og den risiko, der stadig består. Ledere finansierer risikoreduktion, de kan måle.

## Anti-mønstre og faldgruber

- **Sikkerhedsteater.** Kontroller, der ser imponerende ud, men ikke reducerer nogen reel risiko, adopteret for at tilfredsstille en revision frem for for at beskytte noget.
- **Sikkerhedsteamet som en port til sidst.** At opdage designfejl ugen før lancering, når de er dyrest at rette og mest sandsynlige at blive frafaldet.
- **Skyldskultur.** At straffe ingeniøren, der rapporterer en fejl, garanterer, at den næste fejl forbliver skjult.
- **Afkrydsningstrusselsmodellering.** At udfylde en skabelon, ingen læser, og producere dokumenter adskilt fra den reelle arkitektur.
- **Kontroller i én størrelse til alle.** At anvende den samme tunge proces på en offentlig hjemmeside og et betalingssystem, hvilket spilder kræfter og avler harme.
- **Frygtdreven prioritering.** At jage den sårbarhed, der trender i nyhederne, frem for det, der faktisk truer jeres aktiver.
- **Ambassadører kun af navn.** At udpege ambassadører uden at give dem tid, træning eller autoritet.

## Modenhedsmodel

**Niveau 1: Opstart.** Sikkerhed er reaktiv og centraliseret. Gennemgange sker sent, hvis overhovedet, og der er ingen trusselsmodellering. Hændelser driver ad hoc-rettelser. Ingeniører ser sikkerhed som en andens problem, og der findes ingen fælles standard.

**Niveau 2: Udvikling.** Et sikkerhedsteam findes og definerer standarder, men praksis er inkonsistent på tværs af teams. Nogen trusselsmodellering sker på større projekter og ingen på andre. Grundlæggende træning er tilgængelig. Sikkerhed opfattes stadig som en port, og shift-left er aspirationel frem for reel.

**Niveau 3: Standardisering.** Sikkerhedsambassadører er indlejret i hvert team. Trusselsmodellering er rutine for nye tjenester, opdelt i niveauer efter CIA-klassificering, og den sikre udviklingslivscyklus er dokumenteret og håndhævet i hele organisationen. Risikobaseret prioritering vejleder arbejdet, standarder for sikker kodning og pipelinetjek er den asfalterede standardvej, og skyldfrie gennemgange efter hændelser er normen.

**Niveau 4: Styring.** Sikkerhedsudfald måles og styres mod baselines. Organisationen følger medianen af tid til at udbedre fund med høj alvorlighed, dækning af trusselsmodeller, andelen af hændelser fanget før produktion og rater for rapportering af næsten-uheld, nedbrudt pr. team. Ambassadørers autoritet til at standse en udgivelse er defineret og faktisk udøvet. Risikobeslutninger kvantificeres som sandsynlighed gange konsekvens, registreres og gennemgås efter en fast kadence, så kontrolhuller viser sig som data frem for som overraskelser.

**Niveau 5: Orkestrering.** Sikkerhed er reelt alles opgave og integreret med levering, risiko og forretningsplanlægning. Trusselsmodellering og sikkert design er vanemæssigt og let, og zero trust-principper er stort set realiseret. Målinger driver løbende forbedring, organisationen lærer af næsten-uheld på tværs af teams, og kontroller tilpasser sig automatisk, efterhånden som trusselsbilledet og arkitekturen ændrer sig.

## Idéer til drøftelse

1. Hvordan måler I, om en sikkerhedskultur faktisk forbedres, ud over at tælle gennemførte træninger?
2. Hvor går den rette grænse mellem det, sikkerhedsambassadører håndterer, og det, det centrale team ejer?
3. Hvordan holder I trusselsmodellering værdifuld uden at lade den blive en bureaukratisk afkrydsning?
4. Er en fuld zero trust-arkitektur realistisk for jeres legacy-ejendom, og hvis ikke, hvad er den pragmatiske delmængde?
5. Hvordan bør sikkerhedsarbejde prioriteres mod funktionslevering, når begge konkurrerer om de samme ingeniører?
6. Hvilke incitamenter ændrer faktisk ingeniørers adfærd i retning af sikkerhedsejerskab?

## Vigtigste pointer

- Sikkerhed er en kulturel egenskab ved store organisationer, ikke en opgave uddelegeret til ét team.
- Sikkerhedsambassadører skalerer ekspertise og ejerskab på tværs af udviklingen.
- Trusselsmodellering (STRIDE, PASTA, angrebstræer) afdækker designfejl tidligt og billigt.
- En sikker SDLC og shift-left-tankegang fanger fejl, når de koster mindst.
- Forsvar i dybden, mindste privilegium og zero trust er de grundlæggende arkitekturprincipper.
- CIA-triaden og risikobaseret prioritering retter knappe kræfter derhen, hvor det betyder mest.
- Omkostningen ved at bygge sikkerhedskultur er langt mindre end omkostningen ved de brud, den forebygger.

## Referencer og videre læsning

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modelling* and *Security Champions* guidance
