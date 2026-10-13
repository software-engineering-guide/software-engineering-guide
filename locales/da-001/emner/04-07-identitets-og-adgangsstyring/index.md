# 4.7 Identitets- og adgangsstyring

## Overblik og motivation

Hver anmodning, der rammer dine systemer, bærer en implicit påstand: *jeg har lov til at gøre dette*. Identitets- og adgangsstyring (IAM) er disciplinen at afgøre, om den påstand er sand. Den besvarer to separate spørgsmål, som folk konstant blander sammen. [Autentificering](https://en.wikipedia.org/wiki/Authentication) beviser, hvem du er. [Autorisation](https://en.wikipedia.org/wiki/Authorization) afgør, hvad du må, når du har bevist det. Hold de to idéer adskilt i hovedet, og halvdelen af forvirringen på dette felt forsvinder.

For store teams er identitet stille blevet den vigtigste kontrol, du ejer. Kapitel 4.3 gør pointen, at identitet er den nye perimeter, og kapitel 4.1 bygger zero trust oven på den: når du holder op med at stole på netværket, er det eneste, der er tilbage at stole på, en verificeret identitet og en eksplicit politik. Det skifte betyder, at et svagt flow til nulstilling af adgangskoder eller en glemt tjenestekonto ikke længere er en lille fejl. Det er hoveddøren. De fleste reelle brud er ikke kløgtige exploits af hukommelsessikkerhedsfejl; de er stjålne legitimationer, for brede tilladelser og konti, der burde have været lukket måneder tidligere.

Indsatsen stiger i virksomheds- og offentlige sammenhænge. En global virksomhed jonglerer dusinvis af overlappende kataloger, tusinder af nye og afgående medarbejdere om måneden og partnere, der skal have afgrænset adgang til en skive af jeres systemer. Et offentligt agentur lægger smartcard-legitimationer, påbudte identitetsassurance-niveauer og revisorer oven på, som skriftligt vil spørge, præcis hvem der kunne røre en given post på en given dag. Dette kapitel er holdningspræget om, hvordan man bygger et identitetslag, der besvarer disse spørgsmål godt uden at standse jeres folk.

## Grundprincipper

- **Autentificering og autorisation er forskellige problemer.** At bevise identitet og at give tilladelse kræver separate designs og separate gennemgange.
- **Én identitet, mange systemer.** Konsolidér til en enkelt kilde til sandheden pr. identitetspopulation; katalogvildtvækst er en sikkerhedsfejl.
- **Mindste privilegium som standard.** Start fra nul adgang og tilføj bevidst, for både mennesker og maskiner.
- **Hver legitimation er midlertidig.** Foretræk kortlivede, automatisk udstedte legitimationer frem for langlivede hemmeligheder.
- **Deprovisionering er lige så vigtig som provisionering.** Adgang, der overlever sit behov, er ren risiko.
- **Phishing-resistent slår mindeværdigt.** Bevæg autentificering mod passkeys og hardwarebackede faktorer.
- **Maskiner er også identiteter.** Arbejdsbyrder, pipelines og tjenester har brug for administreret identitet, ikke delte statiske nøgler.
- **Adgang er en livscyklus, ikke en begivenhed.** Giv, gennemgå og tilbagekald efter en plan, og bevis at du gjorde det.

## Anbefalinger

### Adskil autentificering fra autorisation, og centralisér begge

Autentificér gennem én identitetsudbyder (IdP), et system der verificerer identitet og udsteder tokens, andre systemer stoler på. Lad derefter hver applikation træffe sine egne autorisationsbeslutninger ud fra den identitet og de attributter, det token bærer. Denne deling lader jer styrke autentificeringen én gang, for alle, mens finkornet tilladelseslogik holdes tæt på de data, den beskytter. Adoptér [single sign-on](https://en.wikipedia.org/wiki/Single_sign-on) (SSO), hvor én autentificering giver adgang til mange applikationer, så jeres folk har ét stærkt login i stedet for fyrre svage. Føderation udvider den samme tillid på tværs af organisatoriske grænser og lader en partners identiteter tilgå jeres systemer uden at I styrer deres adgangskoder.

### Brug de moderne protokoller til det, hver faktisk er til

Tre standarder gør det meste af arbejdet, og hver har et job. **OpenID Connect (OIDC)** er et identitetslag bygget på [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0; brug det til at besvare *hvem er denne bruger* for web- og mobilindlogning. **OAuth 2.0** er et autorisationsrammeværk for delegeret adgang; brug det til at lade en applikation kalde en API på en brugers vegne uden nogensinde at se deres adgangskode (kapitel 2.3). **Security Assertion Markup Language (SAML)** er den ældre XML-baserede føderationsstandard; den forbliver arbejdshesten for virksomheds-SSO ind i etablerede forretningsapplikationer. En almindelig fejl er at række ud efter OAuth for at gøre autentificering direkte. OAuth giver adgang til ressourcer; OIDC sidder oven på det for at etablere identitet. Vælg OIDC til ny brugervendt indlogning, behold SAML, hvor jeres virksomhedskatalog kræver det, og opfind ikke dit eget tokenformat.

### Gør autentificering phishing-resistent

Adgangskoder alene er uforsvarlige i skala. Kræv multifaktorautentificering (MFA), som kombinerer noget du ved, noget du har og noget du er, for hver menneskelig konto uden undtagelse. Gå så videre end de svage faktorer: engangskoder over SMS kan phishes og SIM-swappes. Den stærke destination er [passkeys](https://en.wikipedia.org/wiki/Passkey) og den underliggende WebAuthn-standard (en browser-API til offentlig-nøgle-autentificering), der binder et login til en hardwareholdt privat nøgle og til det rigtige websteds oprindelse, så en falsk side ikke kan høste noget, der er værd at stjæle. Passkeys er også adgangskodefrie, hvilket jeres brugere vil takke jer for. Behandl kontogenopretning og nulstilling af adgangskoder som en del af autentificeringsfladen, fordi en angriber, der ikke kan slå jeres MFA, i stedet blot vil angribe nulstillingsflowet.

### Styr joiner-mover-leaver-livscyklussen, og deprovisionér hurtigt

Identitet er en livscyklus. En **joiner** har brug for den rette adgang på dag ét. En **mover**, der skifter rolle, har brug for ny adgang og, afgørende, for at den gamle adgang fjernes, ellers akkumulerer vedkommende langsomt nøglerne til hele bygningen. En **leaver** skal miste al adgang prompte, helst inden for minutter efter sin sidste dag, på tværs af hvert system. Lad dette udgå fra en autoritativ kilde, som regel HR-systemet, så en statusændring der automatisk provisionerer og deprovisionerer nedstrøms. Automatisér det. Manuelle offboardingtjeklister overser altid noget, og den konto, de overser, er den, der dukker op i hændelsesrapporten.

### Vælg en autorisationsmodel og udtryk den som policy-as-code

Giv tilladelser med [rollebaseret adgangskontrol](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), hvor I tildeler tilladelser til jobfunktionsroller og tildeler folk til roller, fordi den er simpel at ræsonnere om og let at revidere. Ræk ud efter [attributbaseret adgangskontrol](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC), hvor I har brug for kontekstbevidste beslutninger baseret på attributter som afdeling, dataklassificering, placering eller tidspunkt på dagen. De fleste modne organisationer kører en hybrid: RBAC til de grove tildelinger, ABAC til de fine betingelser. Uanset hvad I vælger, så udtryk autorisation som **policy-as-code**: regler skrevet i en versionsstyret, testbar, gennemgåelig form frem for klikket ind i en konsol. Policy-as-code gør adgangsbeslutninger reviderbare, diffbare og ensartede på tværs af miljøer, og det lader jer teste en tilladelsesændring, før den udgives.

### Håndhæv mindste privilegium med just-in-time-adgang og PAM

Anvend [princippet om mindste privilegium](https://en.wikipedia.org/wiki/Principle_of_least_privilege): hver identitet får den mindste adgang, den har brug for, og ikke mere. Stående privilegium er fjenden, fordi en tilladelse givet permanent er en tilladelse, der er tilgængelig for enhver angriber, som lander på den konto til enhver tid. Foretræk **just-in-time (JIT)-adgang**, hvor en person anmoder om forhøjede rettigheder for et afgrænset vindue, får dem efter godkendelse og mister dem automatisk, når vinduet lukker. For jeres farligste konti så adoptér **privileged access management (PAM)**: et system, der vaulter administrative legitimationer, formidler og optager privilegerede sessioner og udsteder forhøjelse efter behov. Målet er nul stående administratoradgang, så selv en fuldt kompromitteret bærbar intet varigt udbytter.

### Giv maskiner og arbejdsbyrder ægte identitet

Mennesker er kun halvdelen af jeres identiteter. Tjenester, pipelines, containere og funktioner autentificerer alle over for noget, og alt for ofte gør de det med en langlivet hemmelighed indsat i en konfigurationsfil. Erstat statiske nøgler med administreret **arbejdsbyrdeidentitet**: kortlivede legitimationer udstedt automatisk til en arbejdsbyrde baseret på, hvor den kører, og hvad den er. Brug gensidig TLS (mTLS), hvor begge sider af en forbindelse præsenterer certifikater, til tjeneste-til-tjeneste-autentificering. Hold eventuelle resterende hemmeligheder i en dedikeret hemmelighedshåndtering med rotation, aldrig i kildekode eller billeder (kapitel 4.2). Kortlivede, automatisk roterede arbejdsbyrdelegitimationer fjerner den enkeltstående mest almindelige årsag til lækager af cloudlegitimationer.

### Gør identitet til kontrolplanet, og gennemgå adgang kontinuerligt

I en zero trust-arkitektur (kapitel 4.1) er identitet der, hvor politik afgøres og håndhæves, så invester der i overensstemmelse hermed. Luk derefter løkken med **adgangsgennemgange**, også kaldet rekertificering: efter en plan bekræfter ejeren af hvert system, at hver person og maskine med adgang stadig har brug for den, og tilbagekalder det, de ikke kan begrunde. Før hver autentificerings- og autorisationshændelse ind i et revisionsspor, der besvarer *hvem der tilgik hvad, hvornår og under hvilken politik* (kapitel 4.6). Adgangsgennemgange er, hvordan I bekæmper privilegiekrybning, den langsomme akkumulering af tilladelser, hvor ingen enkelt tildeling nogensinde så urimelig ud, men som tilsammen gør en konto langt for mægtig.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Centraliseret IdP med SSO | Ét stærkt login, ensartet politik, let revision | Enkelt fejlpunkt; et nedbrud låser alle ude |
| RBAC | Simpel, reviderbar, velkendt | Rolleeksplosion; grov til kontekstfølsomme behov |
| ABAC | Finkornet, kontekstbevidst, skalerer med attributter | Sværere at designe, teste og ræsonnere om |
| Passkeys / WebAuthn | Phishing-resistent, adgangskodefri, stærk | Genopretnings- og enhedstabsflow kræver omhyggeligt design |
| Just-in-time-adgang | Nær nul stående privilegium | Gnidning; kræver hurtige, pålidelige godkendelsesstier |
| Føderation med partnere | Ingen ekstern adgangskodestyring; afgrænset tillid | Tilliden afhænger af partnerens egen hygiejne |
| Langlivede tjenestenøgler | Trivielt let at sætte op | Lækagetilbøjelige; den største årsag til legitimationsbrud |

Den centrale spænding er sikkerhed versus gnidning. Hver kontrol, der skrumper angrebsfladen (MFA på alt, JIT-forhøjelse, korte legitimationslevetider), tilføjer også et trin til nogens dag, og folk går uden om kontroller, der gør for ondt. Løs det ved at gøre den sikre sti til den lette sti: SSO, så stærk autentificering er ét tryk, passkeys, så der ikke er nogen adgangskode at skrive, og automatiseret provisionering, så den rette adgang simpelthen dukker op. Brug jeres gnidningsbudget, hvor sprængradius er størst, på privilegeret og produktionsadgang, og hold hverdagsadgang næsten gnidningsfri.

## Spørgsmål til drøftelse med dit team

1. **Hvor hurtigt kan I faktisk tilbagekalde al adgang for en, der forlader jer i dag, og hvordan ved I, at det virkede?** Deprovisioneringshastighed er et direkte mål for jeres identitetsmodenhed, fordi en afgående medarbejder, hvis adgang bliver hængende, er en ikke-overvåget konto med reelle tilladelser. I en stor organisation med dusinvis af ikke-forbundne systemer er det ærlige svar ofte "vi er ikke sikre," og hullet er som regel de applikationer, der aldrig blev koblet til den centrale identitetsudbyder. Tag en reel nylig afgang med og spor hvert system, vedkommende kunne røre, og tjek tidsstempler for, hvornår hver adgang faktisk sluttede. Beslut et mål, såsom fuld tilbagekaldelse inden for en time efter HR-statusændringen, og instrumentér det, så I kan bevise det frem for at håbe. Hvis noget system hviler på, at nogen husker et manuelt trin, er det den konto, et fremtidigt brud vil bruge.

2. **Hvor har I stadig stående privilegeret adgang og langlivede statiske legitimationer, og hvad ville der skulle til for at eliminere dem?** Stående administratorrettigheder og permanente tjenestenøgler er de to aktiver, angribere mest vil have, fordi de er varige og mægtige. Lav en opgørelse over hvert menneske med altid-tændt produktions- eller administrativ adgang og hver tjeneste, der autentificerer med en statisk nøgle, og spørg så ærligt, hvilke af dem der kunne flyttes til just-in-time-forhøjelse eller kortlivet arbejdsbyrdeidentitet. Det modstridende hensyn er driftsfrygt: teams beholder stående adgang, fordi nød-øjeblikke føles sikrere med den, så I skal gøre nødforhøjelse hurtig og pålidelig, før I tager de stående rettigheder væk. Tag listen med til drøftelsen og rangér poster efter sprængradius, med produktions- og administrativ adgang først. Den ønskede slutstat er nul stående administratoradgang og ingen statisk nøgle, der overlever en enkelt udrulning.

3. **Har I én autoritativ identitet pr. person og pr. arbejdsbyrde, eller flere, og hvad koster vildtvæksten jer?** Katalogvildtvækst, hvor det samme menneske eksisterer som fem konti på tværs af fem systemer med drivende attributter, er der, hvor deprovisioneringshuller og forældreløs adgang fødes. At konsolidere til en enkelt kilde til sandheden pr. identitetspopulation er en af de investeringer med højest løftestang, et stort team kan foretage, fordi enhver nedstrøms kontrol afhænger af at vide, at to poster er den samme person. Tag en opgørelse over jeres identitetslagre med og kortlæg, hvilke der er autoritative, og hvilke der er bekvemme kopier, ingen styrer. Afvejningen er, at konsolidering er en stor, uglamourøs migrering, der konkurrerer med funktionsarbejde om opmærksomhed. Beslut, om den løbende omkostning ved vildtvækst, i revisionssmerte og brudrisiko, retfærdiggør at finansiere den migrering nu frem for efter den næste hændelse.

4. **Er jeres stærkeste autentificeringsfaktorer reelt phishing-resistente, og hvad forhindrer jer i at pensionere adgangskoder for altid?** Den faktor, en angriber ikke kan phishe, er den, der gør en ende på legitimationstyveri som jeres dominerende brudsti, og passkeys bundet til WebAuthn er den eneste bredt udrulbare mulighed, der klarer den barre. I en stor organisation er det ærlige billede som regel blandet: passkeys for nogle, engangskoder over SMS for andre og en lang hale af legacy-applikationer, der stadig accepterer en adgangskode alene. Det modstridende hensyn er reelt, fordi passkeys flytter det svære problem til genopretning og enhedstab, og et klodset genopretningsflow bliver det nye bløde mål, en angriber blot skifter til. Tag dækningstallene efter faktortype, listen over applikationer, der stadig falder tilbage til en adgangskode, og en designet kontogenopretningssti med, I ville stole på mod et beslutsomt socialt ingeniørforsøg. I virksomheds- og offentlige sammenhænge så bind målet til ethvert påbudt assurance-niveau, da et højassurance-system, der stadig tillader en phishbar faktor, har et compliancehul såvel som et sikkerhedshul.

5. **Hvordan afgør I, hvilken adgang hver identitet får, og kan I diffe, teste og bevise den beslutning, før den udgives?** Hullet mellem "nogen klikkede tilladelser ind i en konsol" og "en gennemgået, versionsstyret politik" er forskellen mellem en adgangsmodel, I kan revidere, og en, I kun kan undskylde for. For et stort team er presset at lade hver applikation vokse sine egne skræddersyede regler, hvilket stille producerer rolleeksplosion på RBAC-siden og utestbare betingelser på ABAC-siden, til ingen kan sige, hvad en given tildeling egentlig tillader. Det modstridende hensyn er leveringshastighed, fordi udtryk af autorisation som policy-as-code tilføjer et gennemgangstrin, et konsolklik ikke gør, og teams under deadline harmes over gnidningen, til den første dumpede revision eller for brede tildeling fører sagen for dem. Tag en reel tilladelsesændring med og spor, hvordan den ville blive foreslået, testet, gennemgået og rullet tilbage, plus en optælling af, hvor mange roller I har, og hvor mange ingen kan forklare. I virksomheds- og offentlige sammenhænge vil en revisor bede jer vise præcis, hvem der kunne tilgå en post og under hvilken regel på en given dag, og kun en diffbar, testbar politik besvarer det uden panik.

6. **Hvornår tilbagekaldte en adgangsgennemgang sidst noget reelt, og hvem er ansvarlig, når privilegiekrybning går uafkontrolleret?** Adgangsgennemgange er kontrollen, der bekæmper den langsomme akkumulering af tilladelser, hvor ingen enkelt tildeling nogensinde så urimelig ud, og en gennemgang, der aldrig tilbagekalder noget, er gennemgangsteater, der producerer papirarbejde i stedet for sikkerhed. I en stor organisation er fejlformen gummistemplet: systemejere rekertificerer hundredvis af poster i ét ryk og godkender dem alle, fordi reelt at vurdere hver er kedeligt, og incitamentet til at holde adgang flydende er stærkere end incitamentet til at skære. Det modstridende hensyn er, at meningsfulde gennemgange koster ejertid og lejlighedsvis bryder nogens arbejdsgang, når adgang, de stille var afhængige af, forsvinder, så I skal gøre gennemgangen målrettet og risikodrevet frem for en udifferentieret liste. Tag tilbagekaldelsesraten fra jeres seneste cyklus, det gennemsnitlige antal rettigheder pr. person og dokumentation for, hvem der ejer hvert systems rekertificering. I virksomheds- og offentlige sammenhænge så navngiv den ansvarlige embedsmand for hver gennemgang og den kadence, vedkommende holdes til, for privilegiekrybning, ingen er ansvarlig for at fange, er netop den tilstand, revisorer og angribere begge udnytter.

## Sektorperspektiv

**Startup.** Køb identitet, byg den ikke. En enkelt hostet identitetsudbyder med SSO, påkrævede passkeys og offboarding med ét klik giver en håndfuld ingeniører en holdning i virksomhedsklasse for et gebyr pr. sæde. Støt dig til udbyderens indbyggede arbejdsbyrdeidentitet, så der ikke er en eneste langlivet cloudnøgle i din pipeline, og brug OIDC og OAuth 2.0 ud af boksen frem for at opfinde tokenhåndtering, du ikke har råd til at vedligeholde.

**Lille virksomhed.** Uden en identitetsspecialist på lønningslisten så foretræk den SSO og MFA, der allerede er bundtet i de værktøjer, du betaler for, og slå dem til frem for at shoppe efter en separat platform. Behandl joiner-mover-leaver-problemet som en kort skriftlig tjekliste knyttet til den, der ejer ansættelser, og foretræk passkeys, fordi de fjerner byrden på helpdesken for nulstilling af adgangskoder, som du ikke kan undvære nogen til at håndtere. Undgå delte logins, da de er den billige vane, der senere gør tilskrivning og tilbagekaldelse umulig.

**Stor virksomhed.** Arbejdet er konsolidering og styring på tværs af mange kataloger og teams: én autoritativ identitetsudbyder drevet af HR-systemet, automatiserede joiner-mover-leaver-flow, RBAC til jobfunktioner med ABAC til kontekst og privileged access management med sessionsoptagelse. Udtryk autorisation som policy-as-code, så ændringer er diffbare og testbare, kør planlagte adgangsgennemgange, der faktisk tilbagekalder, og standardisér grænsefladen, så applikationer kobles til central identitet i stedet for hver at vokse sit eget login.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed driver designet. Bind autentificering til hardwarelegitimationer såsom PIV- eller CAC-smartcards, sæt identitetsassurance-niveauer efter NIST SP 800-63, så systemer med højere risiko kræver faktorer med højere assurance, og hold uforanderlige revisionslogs, der besvarer præcis, hvem der tilgik hvad og hvornår. Offentliggør håndteringen af borgervendt identitet i almindeligt sprog, hold kunde- og medarbejderidentitetsstakke adskilt, og sørg for, at hver privilegeret handling på et følsomt system formidles og optages for de revisorer, der vil spørge.

## Eksempler

**Startup.** Et startup på tyve personer kan ikke bemande et identitetsteam, så det køber et. Hver medarbejder logger ind gennem en enkelt hostet identitetsudbyder med SSO ind i e-mail, kodehosting, cloudkonsol og den interne app, og passkeys er påkrævede, så der ikke er adgangskoder at phishe. Offboarding er ét klik: at deaktivere personen i identitetsudbyderen skærer adgang overalt på én gang. Til deres eget produkt bruger de OIDC til brugerindlogning og OAuth 2.0 til at lade integrationer kalde deres API med afgrænsede tokens. Autentificering fra tjeneste til cloud bruger udbyderens indbyggede arbejdsbyrdeidentitet, så der ikke er en eneste langlivet cloudnøgle nogen steder i deres pipeline. Det koster et beskedent gebyr pr. sæde og køber dem en identitetsholdning stærkere, end mange virksomheder kører.

**Stor virksomhed.** En multinational bank har brugt et årti på at akkumulere fire kataloger og hundredvis af applikationer, nogle føderet med SAML, nogle med deres egne lokale logins. Den finansierer et konsolideringsprogram: én autoritativ identitetsudbyder, drevet af HR-systemet, med automatiserede joiner-mover-leaver-flow, der provisionerer ved ansættelse og tilbagekalder inden for minutter efter opsigelse. RBAC dækker standardjobfunktioner, mens ABAC håndhæver dataresidens- og klareringsregler for adgang på tværs af grænser. Administratorer holder ingen stående produktionsadgang; de anmoder om just-in-time-forhøjelse gennem et privileged access management-system, der optager hver session. Kvartalsvise adgangsgennemgange tvinger systemejere til at rekertificere eller tilbagekalde, og hver beslutning udtrykkes som policy-as-code, så revisorer kan diffe præcis, hvad der ændrede sig, og hvornår.

**Offentlig sektor.** Et føderalt agentur udsteder personal identity verification (PIV)-smartcards, og det militære ækvivalent, common access card (CAC), til sin arbejdsstyrke, så autentificering er bundet til en hardwarelegitimation frem for en adgangskode. Dets identitetsprogram følger den føderale tilgang til identitet, legitimation og adgangsstyring (FICAM) og sætter identitetsassurance-niveauer efter National Institute of Standards and Technology-retningslinjen NIST SP 800-63, så systemer med højere risiko kræver legitimationer med højere assurance. Borgervendte tjenester bruger en separat kundeidentitetsstak på et lavere assurance-niveau med stærk MFA. Adgangsgennemgange og uforanderlige revisionslogs fodrer direkte ind i agenturets dokumentation for kontinuerlig autorisation (kapitel 4.6), og hver privilegeret handling på et klassificeret system formidles og optages.

## Business case: motivation, ROI og TCO

Afkastet af identitetsinvestering kommer af at flytte jeres dominerende brudvektor ud af farezonen. Stjålne legitimationer og overtilladte konti driver en stor andel af reelle hændelser, og hver bærer en tung hale: hændelsesrespons, regulatoriske bøder, underretning om brud og varig omdømmeskade. Phishing-resistent MFA alene eliminerer den mest almindelige indtrængningssti, og automatiseret deprovisionering lukker hullet med forældreløse konti, der forvandler en rutineafgang til en eksponering. Disse er blandt de billigste risikoreduktioner pr. brugt krone.

De totale ejeromkostninger er reelle, men afgrænsede. De omfatter licensering af identitetsudbyder, en privileged access management- og hemmelighedsplatform, ingeniørarbejdet til at koble hver applikation til central identitet og den løbende indsats i adgangsgennemgange. Den større omkostning er organisatorisk: at konsolidere kataloger og eftermontere SSO på legacy-applikationer er langsomt, uglamourøst arbejde, der konkurrerer med funktioner. Vej det mod alternativet. Fragmenteret identitet bruger de samme penge for evigt i form af manuel offboarding, revisionspaniker og helpdesk-nulstillinger af adgangskoder, plus den eventuelle omkostning ved det brud, fragmenteringen gør sandsynligt. Når du fører sagen over for ledelsen, så ram identitet ind som kontrolplanet for zero trust: konsolidering og automatisering er en engangsinvestering, der sænker både brudrisiko og den tilbagevendende omkostning ved revisioner, offboarding og adgangssupport.

## Anti-mønstre og faldgruber

- **Forældreløse konti.** Adgang, der overlever personen eller formålet, især ikke-overvågede tjenestekonti og glemte konsulenter.
- **Stående admin overalt.** Altid-tændt privilegeret adgang i stedet for just-in-time-forhøjelse, hvilket giver enhver kompromitteret administratorkonto varig magt.
- **Langlivede statiske nøgler.** Tjenestelegitimationer indsat i konfiguration eller CI, der aldrig udløber og til sidst lækker.
- **Katalogvildtvækst.** Det samme menneske som mange ustyrede konti, så ingen ændring nogensinde fuldt udbredes.
- **Delte konti.** Legitimationer brugt af flere personer, der ødelægger tilskrivning og gør tilbagekaldelse umulig.
- **SMS som din stærke faktor.** At behandle phishbare, SIM-swapbare engangskoder som tilstrækkelig MFA.
- **Rolleeksplosion.** Så mange snævre RBAC-roller, at modellen bliver ureviderbar, og ingen ved, hvad en rolle giver.
- **Deprovisionering som manuel tjekliste.** Menneskelige offboardingtrin, der uundgåeligt overser den ene konto, der betyder noget.
- **OAuth brugt til autentificering.** At behandle et adgangstoken som bevis for identitet i stedet for at bruge OIDC.
- **Gennemgangsteater.** Adgangsrekertificeringer gummistemplet uden at nogen reelt vurderer behovet.

## Modenhedsmodel

- **Niveau 1, Opstart:** Hver applikation har sit eget login. Adgangskoder uden ensartet MFA. Provisionering og offboarding er manuel, reaktiv og langsom; forældreløse konti akkumulerer. Tjenestelegitimationer er langlivede statiske nøgler. Ingen adgangsgennemgange; tilladelser gives og genbesøges aldrig.
- **Niveau 2, Udvikling:** SSO dækker de store applikationer gennem en central identitetsudbyder, men dækningen er ujævn på tværs af teams. MFA er påkrævet for det meste menneskelig adgang. Grundlæggende RBAC findes. Joiner-mover-leaver er delvist automatiseret fra HR-systemet. Nogle privilegerede konti er vaultede. Adgangsgennemgange sker lejlighedsvis og inkonsistent.
- **Niveau 3, Standardisering:** En konsolideret identitetsudbyder er autoritativ for arbejdsstyrken, med automatiseret provisionering og prompte deprovisionering håndhævet i hele organisationen. Phishing-resistent MFA er standard og dokumenteret. RBAC plus ABAC er udtrykt som policy-as-code. Privileged access management med sessionsoptagelse er på plads. Arbejdsbyrdeidentitet erstatter de fleste statiske nøgler. Planlagte adgangsgennemgange er håndhævet og revideret mod en skriftlig politik, hvert team følger.
- **Niveau 4, Styring:** Identitetsprogrammet måles mod baselines og styres med data. I følger deprovisioneringstid fra HR-statusændring til fuld tilbagekaldelse, MFA- og passkey-dækning efter population, antallet af konti med stående privilegeret adgang, antallet af langlivede statiske nøgler stadig i brug, antal forældreløse konti og tilbagekaldelsesrater i adgangsgennemgange. Målinger bærer mål, såsom fuld tilbagekaldelse inden for en time og nul nye stående admin-tildelinger, og brud på en tærskel udløser undersøgelse frem for et skuldertræk. Autorisationsændringer testes i pipelinen, og hver go eller no-go på en adgangstildeling drives af dokumentation, ikke vane.
- **Niveau 5, Orkestrering:** Identitet er det løbende forbedrede kontrolplan for zero trust, integreret med sikkerhed, risiko og joiner-mover-leaver-planlægning på tværs af organisationen. Passkeys er standard, og adgangskoder er ved at blive pensioneret. Nul stående privilegium opnås gennem just-in-time-forhøjelse, og alle arbejdsbyrder bruger kortlivede, automatisk roterede legitimationer og mTLS. Autorisation er fuldt policy-as-code. Adgangsgennemgange er kontinuerlige og risikodrevne, deprovisionering er næsten øjeblikkelig, og hver beslutning producerer revisionsdokumentation automatisk. Modellen tilpasser sig, efterhånden som risikosignaler skifter, og strammer eller løsner adgang dynamisk frem for efter en fast kadence.

## Idéer til drøftelse

1. Hvad ville der skulle til for at nå nul stående administratoradgang, og hvilken break-glass-sti ville gøre det sikkert?
2. Hvor er ABAC sin kompleksitet værd i jeres miljø versus at blive ved almindelig RBAC?
3. Hvor aggressivt bør I pensionere adgangskoder til fordel for passkeys, og hvilket genopretningsflow erstatter dem?
4. Hvilke applikationer er stadig uden for jeres centrale identitetsudbyder, og hvad holder dem der?
5. Hvordan giver I partnere og kunder afgrænset adgang uden at arve deres sikkerhedshygiejne?
6. Hvilken enkelt måling fanger bedst jeres deprovisioneringshastighed, og måler I den i dag?

## Vigtigste pointer

- Autentificering beviser, hvem du er; autorisation afgør, hvad du må. Design og gennemgå dem separat.
- Konsolidér til én autoritativ identitetsudbyder med SSO; katalogvildtvækst er en sikkerhedsdefekt, ikke en bekvemmelighed.
- Automatisér joiner-mover-leaver-livscyklussen, og gør deprovisionering hurtig og bevislig.
- Brug OIDC til brugerindlogning, OAuth 2.0 til delegeret API-adgang og SAML, hvor virksomhedskataloget har brug for det; brug ikke OAuth som autentificering.
- Bevæg autentificering mod phishing-resistente passkeys og WebAuthn; kræv MFA overalt og behandl svage faktorer som en nødløsning.
- Håndhæv mindste privilegium med just-in-time-adgang og privileged access management; sigt mod nul stående administratorrettigheder.
- Giv maskiner ægte identitet med kortlivede arbejdsbyrdelegitimationer og mTLS; eliminér langlivede statiske nøgler.
- Gør identitet til kontrolplanet for zero trust (kapitel 4.1), og luk løkken med kontinuerlige adgangsgennemgange og revisionsdokumentation (kapitel 4.6).

## Referencer og videre læsning

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (identity assurance, authentication, and federation levels)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, Access Control (AC) and Identification and Authentication (IA) families
- The OAuth 2.0 Authorisation Framework, IETF RFC 6749, and the OAuth 2.0 Security Best Current Practice
- OpenID Connect Core 1.0 specification, OpenID Foundation
- Security Assertion Markup Language (SAML) 2.0 specification, OASIS
- Web Authentication (WebAuthn) Level 2, W3C Recommendation, and FIDO2 / FIDO Alliance passkey specifications
- Federal Identity, Credential, and Access Management (FICAM) architecture and playbooks, U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Open Policy Agent (OPA) documentation, Cloud Native Computing Foundation (policy-as-code for authorisation)
