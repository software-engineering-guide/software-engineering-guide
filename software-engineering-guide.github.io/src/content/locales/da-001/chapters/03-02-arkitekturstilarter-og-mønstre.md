# 3.2 Arkitekturstilarter og mønstre

## Overblik og motivation

En arkitekturstil er en bred, genbrugelig form til at organisere et system: hvordan det opdeles, hvordan delene kommunikerer, og hvor grænserne falder. At vælge en er blandt de mest konsekvensrige (og mest misforståede) beslutninger, en stor organisation træffer. Alt for ofte følger valget moden ("alle laver [mikrotjenester](https://en.wikipedia.org/wiki/Microservices)") i stedet for de reelle begrænsninger hos teamet, domænet og driftsvirkeligheden. Du ender med et af to rod: et distribueret system, organisationen ikke kan drive, eller en sammenfiltret [monolit](https://en.wikipedia.org/wiki/Monolithic_application), ingen kan ændre sikkert. Ingen af delene er stilens skyld. Begge kommer af at matche stilen forkert til situationen.

For store udviklerteams betyder stilarter mest på grund af [Conways lov](https://en.wikipedia.org/wiki/Conway%27s_law): et systems struktur har tendens til at spejle kommunikationsstrukturen i den organisation, der bygger det. Så en arkitekturstil er også en organisatorisk designbeslutning. At dele et system op i tjenester er reelt en beslutning om at dele teams, ejerskab og vagtansvar. Virksomheder med hundredvis af ingeniører kan have råd til (og har ofte brug for) finkornede tjenester med uafhængig udrulning, fordi den uafhængighed er, hvordan mange teams leverer uden at blokere hinanden. Tving det samme mønster på et enkelt lille team, og det arver hele driftsskatten uden nogen af de organisatoriske fordele.

Offentlige og virksomhedsmæssige sammenhænge lægger flere begrænsninger oven på: lange systemlevetider, streng ændringskontrol, indkøbscyklusser, integration med forankrede registersystemer og reviderbarhed. Disse favoriserer stilarter, der holder grænser eksplicitte og afhængigheder lette at inspicere. Dette kapitel gennemgår de store stilarter: monolit til mikrotjenester, [hændelsesdrevne arkitekturer](https://en.wikipedia.org/wiki/Event-driven_architecture) med [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) og event sourcing, [service mesh](https://en.wikipedia.org/wiki/Service_mesh)- og gateway-mønstre, [serverless](https://en.wikipedia.org/wiki/Serverless_computing) og de interne discipliner i [hexagonal](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) og ren arkitektur. Vigtigere endnu hjælper det dig med at se, hvornår hver passer.

*Se også:* kapitel 2.2 (principper for softwaredesign, herunder [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)), kapitel 3.1 (grundlæggende arkitektur) og kapitel 3.3 (distribuerede systemer).

## Grundprincipper

- **Stil følger kræfter, ikke mode.** Vælg ud fra teamstørrelse, domænekompleksitet, belastning og driftsmodenhed, aldrig fordi en teknologi er populær.
- **Kobling er den reelle fjende, ikke antallet af udrulningsenheder.** En velmodulariseret monolit slår en distribueret big ball of mud.
- **Distribution er en omkostning, du betaler for uafhængighed.** Del kun, når værdien af uafhængig udrulning, skalering eller fejlisolation overstiger omkostningen ved netværkskald, delvis fejl og datakonsistens på tværs af tjenester.
- **Grænser bør følge forretningsdomænet.** Afstem tjenester og moduler med afgrænsede kontekster (hver en selvstændig domænemodel med sin egen eksplicitte grænse), ikke med tekniske lag.
- **Design det indre godt uanset det ydre.** Hexagonal/ren lagdeling holder forretningslogik uafhængig af frameworks og infrastruktur i enhver stil.
- **Conways lov er uundgåelig, så brug den.** Design teamgrænser og arkitektur sammen.
- **Begynd simplere, end du tror, du har brug for.** Du kan uddrage tjenester fra en god modulær monolit; at af-distribuere et for tidligt mikrotjenesterod er langt sværere.

## Anbefalinger

### Vælg en modulær monolit som standard; del med dokumentation

Begynd de fleste systemer som en enkelt udrulningsenhed med stærke interne modulgrænser: klare grænseflader, ingen indgriben i et andet moduls data og håndhævede afhængighedsregler. Du får simple transaktioner, let refaktorering og én ting at udrulle og observere. Del først et modul ud i sin egen tjeneste, når du har en konkret grund: en del, der skal skalere for sig selv, et team, der har brug for at udrulle på sin egen kadence, et fejldomæne, du skal isolere, eller et teknologikrav, der adskiller sig fra resten. Når du deler, så del langs afgrænsede konteksters linjer, så hver tjeneste ejer sine data og eksponerer en stabil kontrakt.

### Vid, hvornår mikrotjenester tjener deres brød

Mikrotjenester giver dig uafhængig udrulning, uafhængig skalering, fejlisolation og frihed til at blande teknologier. Til gengæld kræver de moden CI/CD (continuous integration og continuous delivery), automatiseret infrastruktur, distribueret sporing, tjenesteopdagelse og en vagtkultur. Spørg dig selv ærligt: kan din organisation drive dusinvis af uafhængigt udrullede tjenester i produktion pålideligt? Hvis platformen og driftsmodenheden ikke er der, multiplicerer mikrotjenester blot dine fejlformer uden at levere deres fordele. Mange organisationer klarer sig bedst med en håndfuld grovkornede tjenester afstemt med de store domæner frem for en sværm af små.

### Brug hændelsesdrevet arkitektur, hvor afkobling og asynkroni betaler sig

Hændelsesdrevet arkitektur lader producenter udsende fakta uden at vide, hvem der forbruger dem. Det køber dig løs kobling, en buffer for belastningsspidser og en let måde at tilføje nye forbrugere på. Brug det, hvor workflows er naturligt asynkrone og reaktive. **CQRS** (Command Query Responsibility Segregation) adskiller skrivemodellen fra en eller flere læsemodeller, hvilket hjælper, når læse- og skrivebelastning eller -former adskiller sig kraftigt. **Event sourcing** gemmer tilstand som en kun-tilføjelses-log af hændelser frem for som nuværende tilstand, hvilket giver dig et perfekt revisionsspor og tidsrejse. Det er stærkt for finans og det offentlige, hvor "hvordan nåede vi til denne værdi?" er et juridisk spørgsmål, men det tilføjer reel kompleksitet i versionering af hændelser, genopbygning af projektioner og ræsonnement om eventual consistency. Ræk ud efter disse med vilje, ikke som standard.

### Anvend gateway-, BFF- og mesh-mønstre til at styre mange tjenester

En **API-gateway** giver eksterne klienter et enkelt indgangspunkt og håndterer autentificering, hastighedsbegrænsning, routing og [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)-terminering (Transport Layer Security). En **Backend-for-Frontend (BFF)** giver hver klienttype (web, mobil, partner-API) sit eget skræddersyede aggregeringslag, så du undgår en oppustet én-størrelse-passer-alle-API. Et **service mesh** flytter tværgående anliggender (gensidig TLS, genforsøg, timeouts, trafikflytning og telemetri) ind i et sidecar-infrastrukturlag, så applikationsteams ikke skal genimplementere dem. Tilføj et mesh først, når antallet af tjenester gør det uhåndterligt at håndtere disse anliggender pr. tjeneste. For nogle få tjenester er et mesh mere driftsvægt, end det er værd.

### Vej serverless ærligt

Function-as-a-service og administrerede serverless-platforme tager serverstyring af dit bord, skalerer til nul og afregner pr. brug, hvilket er fremragende til spidsbelastede, hændelsesdrevne eller lavbaseline-arbejdsbyrder og til små teams. Afvejningerne er reelle: koldstartslatens, grænser for eksekveringstid og ressourcer, sværere lokal test, mulig leverandørindlåsning og omkostning, der kan overstige provisioneret infrastruktur ved vedvarende højt volumen. Brug serverless, hvor dets økonomi og driftsenkelhed klart vinder. Tving ikke stabile kernesystemer med højt gennemløb ind i det af begejstring.

### Hold forretningslogikken ren inde i hver tjeneste

Uanset den ydre stil så hold det indre rent med **hexagonal (ports og adaptere)** eller **ren arkitektur**: forretningsregler i midten, afhængige kun af abstraktioner; frameworks, databaser og beskedudveksling ved kanterne som udskiftelige adaptere. Det holder din værdifulde domænelogik testbar uden infrastruktur og portabel på tværs af teknologiskift: en afgørende fordel for langlivede offentlige og virksomhedssystemer, der vil overleve flere generationer af frameworks.

## Afvejninger: fordele og ulemper

| Stil | Bedst når | Fordele | Ulemper |
|---|---|---|---|
| Modulær monolit | De fleste systemer, især tidligt | Simpel drift, lette transaktioner og refaktorering | Enkelt udrulningsenhed; skalerer som én; risiko for erosion |
| Mikrotjenester | Mange teams, høj skala, moden platform | Uafhængig udrulning/skalering, fejlisolation | Distribueret kompleksitet, datakonsistens, høje driftsomkostninger |
| Hændelsesdrevet / CQRS / event sourcing | Asynkrone workflows, revisionsbehov, divergerende læsning/skrivning | Løs kobling, reviderbarhed, skalerbare læsninger | Eventual consistency, hændelsesversionering, sværere fejlsøgning |
| Serverless | Spidsbelastet eller lav baseline, hændelsesdrevet arbejde | Ingen serverstyring, skalering til nul, betaling pr. brug | Koldstart, grænser, indlåsning, omkostning ved høj stabil belastning |

Det tilbagevendende tema: du køber fleksibilitet og uafhængighed med drifts- og kognitiv kompleksitet. Distribuerede og hændelsesdrevne stilarter opgiver enkelheden i en enkelt kaldestak og en enkelt transaktion til gengæld for evnen til at skalere, udrulle og fejle uafhængigt. Den handel betaler sig i stor skala og med en moden platform. Uden en er den ruinerende. De interne discipliner (hexagonal/ren) er næsten altid umagen værd, fordi de koster lidt og holder dine muligheder åbne for at skifte stil senere.

## Spørgsmål til drøftelse med dit team

1. **Før I deler den næste tjeneste, deler I så også det team, der ejer den, og hvem har autoriteten til at gøre det?** Conways lov betyder, at en tjenestegrænse reelt er en teamgrænse, så en deling, organisationsdiagrammet ikke bakker op om, producerer en distribueret monolit: to udrulningsenheder, ét udgivelsestog, delt vagt. I en stor virksomhed sidder autoriteten til at omforme teams som regel over ingeniørarbejdet, hos rapporteringslinjer, økonomi og HR, hvilket er grunden til, at arkitektur og organisationsdesign skal besluttes sammen. Tag dokumentation med til drøftelsen: har den foreslåede tjeneste et team, der kan eje den fra ende til anden, bemande sin egen vagt og udrulle på sin egen kadence? Hvis svaret er nej, så finansiér enten teamet eller behold kapaciteten som et modul i monolitten. At dele kode uden at dele ejerskab køber alle omkostninger ved distribution og intet af uafhængigheden.

2. **Kan I udrulle hver af jeres tjenester uafhængigt i dag, eller udgives de i hemmelighed i lockstep?** Den distribuerede monolit er det værste udfald i dette kapitel: I betaler for netværkskald, delvis fejl og datakonsistens på tværs af tjenester og kan alligevel ikke udgive én uden de andre. Kendetegnene er en fælles database, et fælles bibliotek der tvinger koordinerede opgraderinger og integrationstests, der skal køre hele landskabet sammen. For et stort team begrænser det stille gennemløbet, fordi hvert team står i kø bag én udgivelse, selv om diagrammet viser uafhængighed. Tag en nylig ændring og tæl, hvor mange tjenester der måtte udrulles sammen for at gøre den sikker; hvis det tal er større end én for en ændring, der rørte en enkelt kapacitet, er jeres grænser forkerte. Rettelsen er som regel at give hver tjeneste sine egne data og en stabil, versioneret kontrakt, ikke at tilføje flere tjenester.

3. **Hvilke af jeres eksisterende tjenesteopdelinger har holdt op med at betale sig, og ville I konsolidere dem tilbage?** Kapitlets mest avancerede vane er at behandle stilbeslutninger som reversible: uddrag, når en driver dukker op, og flet igen, når driveren forsvinder. De fleste organisationer deler kun, så nanotjenester og snakkesalige entitetstjenester akkumuleres, til orkestrerings- og netværksoverhead dværger det arbejde, hver tjeneste udfører. Led efter tjenester, der altid udrulles sammen, som eksisterer på grund af en databasetabel frem for en forretningskapacitet, eller hvis netværksspring nu dominerer en anmodnings latens. I virksomheds- og offentlige landskaber, hvor headcount og budgetter granskes, er det at folde to tynde tjenester tilbage i én grovkornet tjeneste et legitimt, omkostningsbesparende træk, ikke en indrømmelse af fiasko. Sæt genkonsolidering på bordet lige så åbent som uddragning, og beslut begge med den samme dokumentation.

4. **Understøtter jeres platform og vagtmodenhed faktisk den stil, I foreslår, og kan I navngive de specifikke huller, før I forpligter jer?** Mikrotjenester, meshes og hændelsesdrevne rygrader leverer kun deres fordele oven på moden CI/CD, distribueret sporing, tjenesteopdagelse og en vagtkultur, der kan ræsonnere om delvis fejl. En stor organisation har tendens til at beslutte målstilen i et arkitekturforum og opdage den manglende platform senere, når dusinvis af tjenester allerede er i produktion, og hver hændelse tager timer at diagnosticere. Vej tiltrækningen ved uafhængig udrulning og skalering mod det nøgterne spørgsmål om, hvem der driver det kl. 3 om natten: den samme deling, der frigør teams til at levere parallelt, multiplicerer også de fejlformer, hvert team skal forstå. Tag en ærlig opgørelse med til drøftelsen: nuværende udrulningsfrekvens, middeltid til genopretning, om I har sporing på tværs af tjenestegrænser, og hvor mange tjenester et enkelt team realistisk kan drive. I virksomheds- og offentlige sammenhænge så tilføj indkøbs- og ansættelsesledetiderne for de platformsevner, I mangler, fordi en stil, der antager et mesh og et platformsteam, I ikke har finansieret, er en plan for at køre et uholdbart landskab.

5. **For hvilke dele af domænet er et fuldt event-sourcet revisionsspor et juridisk krav frem for en bekvemmelighed, og hvem har autoriteten til at beslutte?** Event sourcing og CQRS køber jer en perfekt, rekonstruerbar historik og læsemodeller, der skalerer for sig selv, men de koster jer hændelsesversionering, projektionsgenopbygninger og ræsonnement om eventual consistency i systemets hele liv. Anvendt på et domæne, der aldrig havde brug for revisionssporet, er den kompleksitet ren skat; tilbageholdt fra et domæne, hvor "hvordan nåede vi frem til denne værdi?" er et juridisk spørgsmål, er dens fravær et compliance-svigt. De modstridende hensyn er reviderbarhed og forespørgselsskalerbarhed på den ene side og fejlsøgningsvanskelighed og udviklernes kognitive belastning på den anden, så beslutningen hører hjemme hos folk, der forstår både den regulatoriske forpligtelse og driftsbyrden, ikke hos den, der er mest begejstret for mønstret. Tag de specifikke juridiske eller kontraktlige krav til opbevaring og rekonstruktion med, det forventede hændelsesvolumen og et ærligt skøn over versionerings- og projektionsarbejdet. I finans, skat og det offentlige, hvor det at rekonstruere en beslutning år senere kan være en lovbestemt pligt, så navngiv den ansvarlige ejer, der godkender, at en given afgrænset kontekst kræver, eller ikke kræver, en uforanderlig hændelseslog.

6. **Hvordan forhindrer I, at den modulære monolit eroderes, så senere uddragning forbliver billig, og hvad vil håndhæve grænserne?** Hele argumentet for at begynde med en modulær monolit hviler på løftet om, at rene interne grænser gør senere tjenesteuddragning overkommelig, men de grænser forfalder stille, i det øjeblik en deadline frister ét modul til at gribe ind i et andets data. For et stort team med mange bidragydere vil gode intentioner og kodegennemgang alene ikke holde linjen; uden en håndhævende mekanisme bliver monolitten stille den big ball of mud, stilen skulle undgå. Vej gnidningen ved håndhævede afhængighedsregler og modulgrænseflader mod omkostningen ved at opdage, år senere, at ingen grænse er reel, og at hver uddragning betyder at løse delt tilstand op. Tag dokumentation med: håndhæves modulgrænser af byggeværktøj, statisk analyse eller pakkestruktur, eller er de blot dokumenterede konventioner, de sidste seks fletninger ignorerede? I langlivede virksomheds- og offentlige systemer, der skal overleve streng ændringskontrol og flere frameworkgenerationer, så behandl grænsehåndhævelse som en reviderbar kontrol, så muligheden for at distribuere senere er en, I faktisk har bevaret, frem for en I antager, I stadig har.

## Sektorperspektiv

**Startup.** Vælg en enkelt modulær monolit som standard og modstå trækket mod mikrotjenester, fordi din knappeste ressource er ingeniørernes opmærksomhed, og en sværm af tjenester er en driftsskat, du ikke har råd til før produkt-markedstilpasning. Hold rene modulgrænser, så du kan uddrage senere, og ræk ud efter serverless, hvor skalering til nul og betaling pr. brug passer til din spidsbelastede, lave baseline. Del præcis én ting, kun når en konkret driver dukker op, såsom en spidsbelastet notifikationssender, og aldrig tidligere.

**Lille virksomhed.** Uden et platformsteam og med et stramt budget så foretræk en monolit eller en håndfuld grovkornede tjenester på en administreret platform, og køb hostet infrastruktur frem for selv at bygge meshes, sporing og tjenesteopdagelse. Vej serverless og administrerede databaser som en måde at undgå at drive servere overhovedet, og vær på vagt over for et distribueret design, hvis driftsbyrde du ingen har til at bære. Den rette arkitektur er den, en eller to personer faktisk kan udrulle, observere og genoprette.

**Stor virksomhed.** Det reelle problem er mange teams og Conways lov: afstem grovkornede tjenester med afgrænsede kontekster og teamejerskab, og invester bevidst i den platform (CI/CD, sporing, mesh og tjenesteopdagelse), der gør distribution sikker. Standardisér gateway-, BFF- og intern ren arkitektur-mønstre, så grupper holder op med at genopfinde dem, og styr uddragning og genkonsolidering som dokumentationsbaserede porteføljebeslutninger frem for lokal præference. Budgettér driftsomkostningen ved hver deling eksplicit, fordi den distribuerede-monolit-fejl i jeres skala er dyr og langsom at løse op.

**Offentlig sektor.** Lange systemlevetider, streng ændringskontrol, indkøbscyklusser og reviderbarhed former valget: foretræk stilarter med eksplicitte, inspicerbare grænser og varige kontrakter, der overlever leverandører og frameworkgenerationer. Event sourcing tjener sin kompleksitet, hvor rekonstruktion af en borgervendt beslutning er en lovbestemt pligt, så brug det bevidst til kernehovedbøger og hold ren arkitektur inde i hver tjeneste for at isolere regler, der ændres med hvert budget. Behandl portabilitet og udgang fra proprietære serverless- eller leverandørplatforme som indkøbskrav, ikke eftertanker.

## Eksempler

**Startup.** Et startup med fire medarbejdere, der bygger et planlægningsprodukt, føler pres for at begynde med mikrotjenester, fordi en konkurrent blogede om dem, men modstår. De udgiver en enkelt modulær monolit med klare interne grænser (planlægning, fakturering, notifikationer) som separate moduler i én udrulningsenhed, så én ingeniør kan køre det hele lokalt, og en udgivelse er ét tryk. Efterhånden som produktet finder fodfæste, trækkes kun notifikationssenderen, som breder ud til e-mail og SMS under spidsbelastning, ud i sin egen tjeneste. De arver intet af driftsskatten fra et dusin tjenester, mens de stadig leder efter produkt-markedstilpasning.

**Stor virksomhed.** En stor e-handelsvirksomhed begynder som en modulær monolit. Efterhånden som trafikken vokser, og teams formeres, trækker den de domæner med højest belastning og mest uafhængig udvikling (katalog, kurv, checkout og søgning) ud i separate tjenester, hver med egne data. Checkout udsender hændelser, som lager, opfyldelse og analyse forbruger gennem en hændelsesrygrad, så nye forbrugere (svindeldetektion, loyalitet) kan tilknytte sig uden at røre checkout. En API-gateway håndterer autentificering og hastighedsbegrænsning, og en BFF skræddersyer nyttelaster til mobil. De resterende domæner med lavere trafik bliver i monolitten, hvilket undgår unødvendig fragmentering.

**Offentlig sektor.** En skattemyndighed bygger en vurderingsplatform på event sourcing til kernehovedbogen, fordi hver ændring af en skatteyders forpligtelse skal kunne rekonstrueres og være juridisk reviderbar i årevis. Kommandoer (indgiv selvangivelse, anvend betaling, udsted justering) producerer uforanderlige hændelser, og læsemodeller projicerer nuværende saldi til sagsbehandlere og borgere. CQRS lader den offentlige forespørgselsside skalere for sig selv til spidsbelastning i indberetningssæsonen uden at sætte skriveisiden i fare. Indeni følger hver tjeneste ren arkitektur, så vurderingsreglerne, der ændres med hvert budget, forbliver isoleret fra persistens- og beskedteknologien.

## Business case: motivation, ROI og TCO

Pengene på spil i et stilvalg er enorme, fordi beslutningen er dyr at gøre om. Adoptér mikrotjenester for tidligt, og du oppuster de totale ejeromkostninger gennem platformsopbygning, duplikeret infrastruktur, distribueret fejlsøgning og en tungere driftsbyrde: omkostninger, der bliver hos dig i systemets liv. Nægt at dele en reelt overbelastet monolit, og du begrænser leveringsgennemløbet: teams står i kø bag en fælles udgivelse, og hver ændring sætter hele systemet i fare. ROI-samtalen handler reelt om at matche driftsudgifter til organisatorisk behov.

Argumentér over for ledelsen i termer af gennemløb og risiko, ikke teknologi. Uafhængig udrulning betyder flere teams, der leverer parallelt, og kortere ledetider: målbar forretningshastighed. Fejlisolation betyder færre samlede nedbrud og en mindre sprængradius: målbar tilgængelighed og omdømmebeskyttelse. Men vær lige så ærlige om den platformsinvestering, hver stil kræver: et mesh, sporing og CI/CD-modenhed er forudsætninger, ikke valgfrit tilbehør, og deres omkostning hører hjemme i TCO. For mange organisationer er den billigste vej en velmoduleret monolit nu, med rene interne grænser, der gør senere uddragning billig. Det køber dig muligheden for at distribuere, uden at du betaler for den, før du har brug for den.

## Anti-mønstre og faldgruber

- **Distribueret monolit.** Tjenester, der skal udrulles sammen og deler en database: alle omkostningerne ved distribution, ingen af uafhængigheden.
- **Nanotjenester.** Tjenester så finkornede, at orkestrerings- og netværksoverhead dværger det arbejde, de udfører.
- **Mikrotjenester uden en platform.** At dele, før du har CI/CD, sporing og vagtmodenhed; fejlformer multipliceres.
- **Entitetstjenester.** At dele efter databasetabel ("Brugertjeneste," "Ordretjeneste") i stedet for efter forretningskapacitet, hvilket tvinger snakkesalige kald på tværs af tjenester for hver operation.
- **Event sourcing overalt.** At anvende det på domæner, der ikke har brug for et revisionsspor, og betale kompleksitetsskatten uden gevinst.
- **Gateway som monolit.** At lægge forretningslogik i API-gatewayen og genskabe et centralt flaskehalspunkt.
- **Frameworkkoblet kerne.** Forretningslogik viklet ind i web- eller ORM-frameworket (object-relational mapping), hvilket gør både test og teknologiskift smertefulde.

## Modenhedsmodel

- **Niveau 1: Opstart.** Stilen vælges efter mode eller ved et tilfælde. I har én sammenfiltret monolit eller et utilsigtet distribueret rod, grænser følger tekniske lag eller historie frem for domænet, og delinger sker reaktivt, når noget går i stykker.
- **Niveau 2: Udvikling.** Nogle teams trækker bevidste modulgrænser inde i monolitten eller opstiller nogle få grovkornede tjenester, og nogle tværgående anliggender håndteres ensartet. Praksis er uens: én gruppe afstemmer tjenester med afgrænsede kontekster, mens en anden stadig deler efter databasetabel, og uddragning forbliver ad hoc.
- **Niveau 3: Standardisering.** En dokumenteret tilgang er håndhævet i hele organisationen: tjenester afstemmes med afgrænsede kontekster og ejer deres data, gateway- og BFF-mønstre bruges, hvor det er passende, intern ren eller hexagonal lagdeling er standarden, og hver deling kræver en angivet driver. Modulgrænser håndhæves af værktøj, ikke kun konvention.
- **Niveau 4: Styring.** Stilbeslutninger måles og styres mod baselines. I følger udrulningsfrekvens og ledetid pr. tjeneste, middeltid til genopretning, hvor mange tjenester der skal udrulles sammen for en typisk ændring og netværksspringslatens, og I sammenligner hver deling omkostning mod den uafhængighed, den skulle købe. Dokumentation, ikke præference, driver, om en grænse overlever, og drift mod en distribueret monolit fanges af målinger frem for af et nedbrud.
- **Niveau 5: Orkestrering.** Arkitektur er integreret med organisationsdesign og tilpasses løbende. En moden platform (CI/CD, sporing og mesh, hvor det er berettiget) gør både distribution og genkonsolidering billig, teams uddrager rutinemæssigt, når en driver dukker op, og folder tjenester tilbage, når en forsvinder, og stilvalg genbalanceres, efterhånden som teamtopologi, belastning og risikobilledet skifter på tværs af hele landskabet.

## Idéer til drøftelse

1. Hvor i jeres system er en monolit faktisk en styrke, og hvor er den en reel flaskehals?
2. Hvilken konkret driver ville berettige at uddrage jeres næste tjeneste, og kan I navngive den, før I bygger den?
3. Har jeres organisation den driftsmodenhed, mikrotjenester kræver? Hvad mangler?
4. For hvilke dele af jeres domæne er et fuldt event-sourcet revisionsspor en juridisk eller forretningsmæssig nødvendighed versus en finesse?
5. Hvor godt spejler jeres nuværende tjenestegrænser jeres teamgrænser, og hjælper eller skader den afstemning?
6. Hvis I skulle skifte jeres webframework eller database næste år, hvor meget af jeres forretningslogik ville I skulle omskrive?

## Vigtigste pointer

- Vælg arkitekturstil ud fra reelle kræfter (teamstørrelse, domæne, belastning, driftsmodenhed), ikke ud fra mode.
- En modulær monolit er den rette standard for de fleste systemer; uddrag kun tjenester med en konkret driver og langs afgrænsede konteksters linjer.
- Mikrotjenester bytter drifts- og kognitiv kompleksitet for uafhængig udrulning, skalering og fejlisolation; de kræver en moden platform.
- Hændelsesdrevet, CQRS og event sourcing tilbyder afkobling og reviderbarhed på bekostning af eventual consistency og versioneringskompleksitet; adoptér bevidst.
- Gateways, BFF'er og meshes tæmmer landskaber med mange tjenester, men tilføjer vægt; indfør dem, når skalaen kræver det, ikke før.
- Anvend hexagonal/ren arkitektur inde i hver tjeneste for at holde værdifuld forretningslogik testbar og holdbar på tværs af teknologiskift.

## Referencer og videre læsning

- Sam Newman, *Building Microservices* and *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (and articles on CQRS and Event Sourcing)
- Matthew Skelton and Manuel Pais, *Team Topologies*
