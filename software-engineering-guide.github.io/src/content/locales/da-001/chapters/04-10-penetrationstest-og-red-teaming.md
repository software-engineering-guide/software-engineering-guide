# 4.10 Penetrationstest og red teaming

## Overblik og motivation

Du kan bygge hver kontrol, din trusselsmodel kalder på, og stadig ikke vide, om de virker. Dokumentationen siger, at firewallen blokerer den port, kodegennemgangen siger, at input er valideret, politikken siger, at mindste privilegium er håndhævet. Offensiv sikkerhed er, hvordan du finder ud af, om noget af det er sandt, når en motiveret angriber presser på. Dette kapitel handler om bevidst at angribe dine egne systemer, under autorisation, for at finde svaghederne, før en reel modstander gør.

Disciplinen løber langs et spektrum. I den lette ende sidder [sårbarhedsscanning](https://en.wikipedia.org/wiki/Vulnerability_scanner): automatiserede værktøjer, der undersøger for kendte fejl og fejlkonfigurationer. I midten sidder [penetrationstest](https://en.wikipedia.org/wiki/Penetration_test): en dygtig person, der kæder svagheder sammen for at bevise udnyttelighed mod et defineret mål. I den fjerne ende sidder [red teaming](https://en.wikipedia.org/wiki/Red_team): en målrettet kampagne, der emulerer en reel modstander på tværs af mennesker, proces og teknologi, og som tester jeres evne til at opdage og reagere, ikke blot jeres evne til at forebygge. Hver besvarer et forskelligt spørgsmål, og at forveksle dem er den mest almindelige måde, organisationer spilder penge og trøster sig med falsk assurance.

Dette kapitel sidder bevidst adskilt fra sine naboer. Kapitel 4.4 dækker sikkerhedsdrift: den defensive, overvågende side, der holder øje med trusler og reagerer på dem. Dette kapitel er den offensive modpart, der tester, om det forsvar faktisk virker. Kapitel 4.9 dækker den sikre softwareudviklingslivscyklus, hvor sikkerhed er bygget ind i, hvordan kode designes og leveres; offensiv test validerer produktet af den livscyklus udefra. Det bygger også på grundlaget og kulturen i kapitel 4.1 og applikationssikkerhedspraksisserne i kapitel 4.2.

For store virksomheder er offensiv test både et risikoreduktionsværktøj og en regulatorisk forpligtelse. Betalingsbehandlere, banker og sundhedsudbydere står over for eksplicitte krav om at teste. For det offentlige rækker indsatsen til national sikkerhed og offentlig tillid: modstanderne her er velressourcerede nationalstater, og de systemer, de retter sig mod, kører valg, ydelser og kritisk infrastruktur. I begge sammenhænge kommer værdien ikke fra rapporten, men fra det, I retter, og hvor meget hurtigere I lærer at opdage den næste indtrængen.

## Grundprincipper

- Afstem engagementet med spørgsmålet: scanning, pentest og red teaming besvarer forskellige ting.
- Få skriftlig autorisation og klare engagementsregler, før nogen rører et system.
- Fund er værdiløse, indtil de er udbedret og gentestet; spor dem som alt andet arbejde.
- Et red team findes for at gøre blue team bedre, ikke for at vinde.
- Emulér reelle modstandere og deres teknikker, ikke generiske tjeklister.
- Mål detektion og respons, ikke kun antallet af fundne sårbarheder.
- Pas på teater: et engagement afgrænset til at bestå ser imponerende ud og beviser intet.

## Anbefalinger

### Forstå spektret af offensiv sikkerhed

Begynd med at navngive, hvad I køber. Sårbarhedsscanning er bred, automatiseret og billig; kør den kontinuerligt mod jeres ejendom for at fange kendte [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE'er) og fejlkonfigurationer. Den producerer volumen og falske positiver, og den kan ikke fortælle jer, om en fejl reelt er udnyttelig i kontekst. Penetrationstest sætter en dygtig tester mod et defineret mål i et fast vindue og kæder svagheder sammen for at demonstrere reel konsekvens: dette scannerfund, kombineret med den svage tilladelse, giver domæneadministrator. Den besvarer "kan netop denne ting brydes, og hvor slemt."

Red teaming besvarer et større spørgsmål: "hvis en beslutsom modstander rettede sig mod os, ville vi opdage det, og kunne vi stoppe dem." Det er målorienteret (eksfiltrér dette datasæt, nå dette kontrolsystem), dækker hele angrebsfladen, herunder mennesker og fysisk adgang, og køres som regel uden at advare forsvarerne. [Purple teaming](https://en.wikipedia.org/wiki/Red_team#Purple_team) river muren ned: red og blue arbejder sammen i samme rum, angriberen kører en teknik, og forsvareren ser, om deres værktøj fanger den, og justerer detektioner i realtid. Purple teaming leverer ofte mere defensiv forbedring pr. krone end et skjult red team, fordi hver handling bliver et læringsøjeblik.

### Vælg black-, grey- eller white-box bevidst

Hvor meget I fortæller testeren, former, hvad I lærer. Black-box-test giver dem intet andet end et mål og simulerer en ekstern angriber uden intern viden; den er realistisk, men langsom, og testere kan bruge hele budgettet på rekognoscering, som en reel modstander ville bruge måneder på. White-box-test afleverer kildekode, arkitekturdiagrammer og legitimationer og lader testeren gå i dybden og dække mere terræn i den tid, der er til rådighed. Grey-box sidder imellem: noget viden, nogle legitimationer, der efterligner en angriber, der har lavet sit hjemmearbejde, eller en ondsindet insider.

For det meste applikationstest giver grey- eller white-box bedre afkast, fordi I betaler for dybde i analysen, ikke for at testeren genopdager jeres subnetlayout. Forbehold black-box til, når realismen i opdagelsesfasen i sig selv er det, I vil teste, såsom at måle, hvor meget en outsider kan lære af jeres offentlige fodaftryk. Vær eksplicitte om, hvilken I bestiller, da en black-box-rapport, der finder lidt, kan betyde, at I er sikre, eller at testeren løb tør for tid ved perimeteren.

### Afgræns omhyggeligt, og skriv engagementsreglerne

Omfang er, hvor engagementer lykkes eller fejler. Et [engagementsregler](https://en.wikipedia.org/wiki/Rules_of_engagement)-dokument definerer, hvad der er inden for grænserne, og hvad der ikke er, hvilke teknikker der er tilladt, testvinduet, de dækkede systemer og netværk, krav til datahåndtering og nødkontakter på begge sider. Det navngiver de produktionssystemer, der er forbudte eller kræver omhu, sætter en regel for at standse, hvis testeren finder noget aktivt farligt, og definerer, hvad der sker, hvis de falder over reel angriberaktivitet eller reelt følsomme data.

Skriv eskaleringsstier og et "slip-ud-af-fængsel"-brev ned: en autorisation, testeren kan fremvise, hvis sikkerhedspersonale eller politi udfordrer dem midt i engagementet. Aftal på forhånd, hvordan fund gemmes og transmitteres, da en pentestrapport er et kort over, hvordan I kan brydes, og skal beskyttes derefter. Snævert omfang producerer dybe fund på en lille flade; bredt omfang producerer overfladisk dækning af en stor. Vælg med vilje, og lad aldrig omfanget stille udvides midt i et engagement uden gen-autorisation.

### Behandl autorisation som linjen mellem test og kriminalitet

Den ene handling, der adskiller en penetrationstester fra en kriminel, er autorisation. At tilgå systemer, du ikke er autoriseret til at tilgå, er en forbrydelse under love som [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) i USA og tilsvarende andre steder, og gode hensigter er intet forsvar. Autorisation skal komme skriftligt fra en med den faktiske myndighed til at give den, dække præcis de systemer og teknikker, der er i omfang, og være underskrevet, før arbejdet begynder.

Tredjepartssystemer komplicerer dette. Jeres cloududbyder, jeres software-som-en-tjeneste-leverandører og enhver delt infrastruktur kan have deres egne testpolitikker, og I kan ikke autorisere et angreb på aktiver, I ikke ejer. Tjek udbyderregler, anmod om tilladelse, hvor det kræves, og hold test inden for jeres eget tenancy. Social engineering rettet mod medarbejdere rejser etiske og juridiske spørgsmål om samtykke og psykisk skade, som I skal gennemtænke på forhånd. I tvivlstilfælde så inddrag juridisk rådgivning; omkostningen ved en samtale er triviel mod omkostningen ved en hændelse med uautoriseret adgang.

### Vej interne teams mod tredjepartstestere

Et internt red team kender jeres miljø, bygger relationer med forsvarere og kan teste kontinuerligt frem for i årlige byger. Den fortrolighed er også en begrænsning: de deler jeres blinde vinkler og organisatoriske antagelser, og deres uafhængighed kan drages i tvivl, når de rapporterer til samme ledelse som de systemer, de tester. Tredjepartsfirmaer bringer friske øjne, specialiserede færdigheder og den uafhængighed, revisorer og tilsynsmyndigheder ofte kræver, men de kører langsomt op, koster mere pr. engagement og forlader jer, når rapporten er leveret.

De fleste modne programmer bruger begge. Interne teams håndterer kontinuerlig modstanderemulering, detektionsjustering og den dybe miljøviden, der gør purple teaming produktiv. Eksterne firmaer leverer periodisk uafhængig validering, opfylder uafhængighedskravene i standarder som PCI DSS og undersøger de områder, jeres egne folk er holdt op med at se. Uanset hvilken I bruger, så insistér på, at testerne er kvalificerede: certificeringer som OSCP (Offensive Security Certified Professional) og påvist erfaring betyder mere end et poleret salgsdæk.

### Kør bug bounties og koordineret offentliggørelse

Et [bug bounty](https://en.wikipedia.org/wiki/Bug_bounty_program)-program inviterer eksterne forskere til at finde og rapportere sårbarheder til gengæld for anerkendelse og betaling. Det giver jer kontinuerlig, crowdsourcet test på tværs af en række færdigheder, I aldrig kunne ansætte på én gang, og I betaler kun for reelle fund. Det er ikke en erstatning for struktureret pentest, da forskere jagter det, der betaler, og kan ignorere hele kategorier, men det er et kraftfuldt supplement, der afdækker kreative angreb.

Før I kører et betalt bounty, har I brug for en politik for [koordineret sårbarhedsoffentliggørelse](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure): en offentliggjort, let at finde måde for enhver at rapportere et sikkerhedsproblem sikkert, et tilsagn om ikke at forfølge forskere i god tro juridisk, definerede svartidslinjer og en intern proces til at triagere og rette det, der kommer ind. En security.txt-fil og en klar rapporteringsadresse er minimum. Offentlige agenturer påbyder i stigende grad politikker for sårbarhedsoffentliggørelse for offentligt vendte systemer, og at have ingen kanal forhindrer ikke forskere i at finde fejl; det forhindrer dem kun i at fortælle jer det sikkert.

### Brug assumed breach og modstanderemulering

Test kun af perimeteren antager, at angriberen starter udenfor, men reelle brud begynder ofte med en phishet legitimation eller en kompromitteret bærbar, der allerede er inde. En [assumed breach](https://en.wikipedia.org/wiki/Breach_and_attack_simulation)-øvelse starter testeren med et fodfæste, såsom adgang som en almindelig medarbejder, og spørger, hvor langt de kan nå derfra. Det tester jeres interne segmentering, detektion og sprængradiuskontroller direkte frem for at satse alt på en perimeter, der til sidst vil blive krydset. Det er som regel en bedre brug af et red teams tid end at se dem banke på en hærdet kant.

Forankr kampagnen i reel modstanderadfærd ved hjælp af [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), en offentlig vidensbase over de taktikker og teknikker, angribere faktisk bruger, organiseret fra indledende adgang til eksfiltration. Modstanderemulering vælger en trusselsaktør, kendt for at målrette jeres sektor, genskaber deres dokumenterede teknikker og tester, om I opdager og stopper hvert trin. Det er langt mere nyttigt end et generisk angreb, fordi det afbilder jeres forsvar mod de specifikke modstandere, I står over for, og producerer fund, jeres trusselsefterretning kan prioritere.

### Før fund til blue team og detektionsudvikling

Pointen med offensiv er bedre forsvar. Hver red team-handling er en chance for at spørge: genererede vores værktøj et signal, så nogen det, og reagerede de korrekt. Kør engagementer, så hver teknik afbildes til en detektion, I enten har, skal bygge eller skal justere. Det er detektionsudvikling: at omsætte angriberadfærd til pålidelige alarmer, og det er der, red team-værdien akkumulerer. Et fund om, at "vi blev ikke opdaget under sidelæns bevægelse," bør blive til en ny detektionsregel, testet ved at genkøre teknikken.

Tabletop-øvelser udvider dette til beslutningstagning. Saml de personer, der ville reagere på en reel hændelse, og gå et realistisk scenarie igennem på papir: hvem erklærer hændelsen, hvem taler med jura, hvem beslutter at tage et system offline. Tabletops er billige, afslører huller i roller og kommunikation, som tekniske tests overser, og forbereder de mennesker, der betyder mest, når hændelsesstyringen i kapitel 9.3 går live. Par teknisk red teaming med regelmæssige tabletops, så både jeres værktøj og jeres folk bliver udøvet.

### Spor udbedring og gentest

En sårbarhedsrapport, ingen handler på, er et ansvar, da I nu med viden kører en fejl, en revisor kan citere. Før hvert fund ind i jeres normale arbejdssporingssystem med en ejer, en alvorlighed og en forfaldsdato knyttet til risiko. Kritiske fund får nødbehandling; lavere fund slutter sig til backloggen med ærlig prioritet. Den måling, der betyder noget, er tid til udbedring, ikke tid til rapport.

Gentest lukker løkken. Efter en rettelse er leveret, bekræfter testeren (eller et automatiseret tjek), at sårbarheden faktisk er væk, og at rettelsen ikke åbnede et nyt hul. Uden gentest er "udbedret" et håb, ikke et faktum, og mange fund vender tilbage, fordi en rettelse var ufuldstændig, eller en regression genindførte dem. Standarder som PCI DSS kræver denne løkke eksplicit. Byg gentest ind i engagementskontrakten, så det ikke er en glemt eftertanke.

## Afvejninger: fordele og ulemper

| Tilgang | Bedst til | Fordele | Ulemper |
|---|---|---|---|
| Sårbarhedsscanning | Kontinuerlig dækning af kendte fejl | Billig, bred, automatiseret, hyppig | Støjende; kan ikke bevise udnyttelighed |
| Penetrationstest | Bevis for konsekvens på et defineret mål | Dyb, menneskelig indsigt; reelle exploit-kæder | Øjebliksbaseret; snævert afgrænset; dyr |
| Red teaming | Test af detektion og respons | Realistisk; udøver mennesker og proces | Dyr; langsom; kræver et modent blue team |
| Purple teaming | Hurtig forbedring af detektioner | Høj læring pr. krone; samarbejdende | Mindre realistisk; kræver begge teams til rådighed |
| Bug bounty | Løbende crowdsourcet opdagelse | Betal pr. fund; forskellige færdigheder | Ujævn dækning; triagebyrde; kræver proces |

Den centrale spænding er mellem realisme og læringshastighed. Et skjult red team er den mest realistiske test, I kan køre, men dets lektier ankommer langsomt og først efter en hel kampagne, og et umodent blue team lærer lidt af at blive stille besejret. Purple teaming ofrer overraskelse for at maksimere, hvor hurtigt forsvarere forbedres. En anden spænding er bredde versus dybde: scanning dækker alt overfladisk, mens en pentest dækker en skive dybt. Modne programmer lægger disse i lag frem for at vælge én, kører kontinuerlig scanning under periodisk dyb test og lejlighedsvise kampagner med fuldt omfang fra et red team. Det forkerte træk er at købe en enkelt årlig pentest, arkivere rapporten og kalde problemet løst.

## Spørgsmål til drøftelse med dit team

1. **Når vi bestiller offensiv test, er vi klare over, hvilket spørgsmål vi faktisk stiller, og passer engagementet til det?** Mange organisationer køber en "penetrationstest" og modtager en sårbarhedsscanning med en menneskeskrevet opsummering og tror så, at de har testet deres forsvar, når de blot har tjekket for kendte fejl. Andre bestiller et red team, når deres detektionsevne er så umoden, at øvelsen kun beviser, hvad alle allerede vidste. Tag jeres tre seneste engagementsomfang og de resulterende rapporter med, og spørg, om hver besvarede det spørgsmål, I havde brug for besvaret: dækning af kendte sårbarheder, udnyttelighed af et specifikt mål eller evne til at opdage og reagere på en indtrængen. Svaret bør forme en bevidst blanding af scanning, pentest og red eller purple teaming afstemt til jeres modenhed.

2. **Hvad sker der med et fund, efter rapporten lander, og hvordan ville vi bevise, at det blev rettet?** Værdien af offensiv sikkerhed ligger helt i udbedring, men mange programmer måler succes på rapportens størrelse frem for risikoens skrumpning. Spor et reelt fund fra jeres seneste engagement: hvem ejede det, hvordan blev det prioriteret mod funktionsarbejde, hvornår blev det rettet, og bekræftede nogen, at rettelsen faktisk virkede? Hvis I ikke kan fremlægge det spor, genererer jeres test viden, I ikke handler på, hvilket er værre end ikke at vide, for nu er I vidende udsat. Udfaldet af denne drøftelse bør være en sporet udbedringsarbejdsgang med ejere, risikobaserede frister og obligatorisk gentest bygget ind i hver kontrakt.

3. **Gør vores red team vores blue team bedre, eller holder det bare regnskab?** Et red team, der fejrer uopdagede sejre og hamstrer sine teknikker, er underholdende og ubrugeligt. Forholdet bør være samarbejdende under den modstridende overflade: hver teknik, der går uopdaget, bør blive til en ny detektionsregel, hver vellykket sti bør informere segmentering, og de to teams bør debriefe sammen. Spørg jeres forsvarere, hvad de lærte af det seneste red team-engagement, og om nogen konkret detektion eller kontrol ændrede sig som følge heraf. Hvis det ærlige svar er ingenting, betaler I for teater, og I bør skifte mod purple teaming og modstanderemulering eksplicit knyttet til detektionsudvikling.

4. **Har vi før vores næste engagement skriftlig autorisation for hvert aktiv i omfang, herunder dem, vi ikke ejer?** Autorisation er linjen mellem en penetrationstest og en computerkriminalitetshændelse, og i en stor organisation ligger de systemer, en tester vil røre, sjældent inden for en enkelt ejerskabsgrænse: de spænder over cloud-tenancies, software-som-en-tjeneste-platforme, administrerede netværk og delt infrastruktur, en partner eller leverandør kontrollerer. Det modstridende pres er hastighed, fordi det er langsomt og fristende at springe over at jage underskrevet tilladelse og udbyderes testpolitikker, når en deadline truer. Tag udkastet til engagementsregler, aktivopgørelsen med en ejer navngivet mod hvert system, de relevante cloud- og leverandørtestpolitikker og det underskrevne autorisationsbrev, testeren kan fremvise, hvis de udfordres midt i engagementet, med. For virksomheds- og offentligt arbejde er eksponeringen akut: en uautoriseret undersøgelse mod en delt platform kan bryde kontrakter, udløse regulatorisk indberetning eller, for et offentligt agentur, blive en overskrift om, at regeringen angreb systemer, den ikke havde ret til at røre, så juridisk rådgivning bør godkende, før nogen begynder.

5. **Investerer vi i et internt red team, eksterne firmaer eller begge dele, og passer den fordeling til det, vi faktisk har brug for?** Dette er en køb-versus-byg-beslutning med reelle penge og flerårige konsekvenser: et internt team koster lønninger og værktøj og leverer kontinuerlig modstanderemulering og dyb miljøviden, mens eksterne firmaer koster mere pr. engagement, men bringer friske øjne, specialiserede færdigheder og den uafhængighed, revisorer og tilsynsmyndigheder kræver. Spændingen er, at hver dækker den andens blinde vinkel, så at behandle dem som erstatninger frem for supplementer efterlader som regel et hul. Tag jeres nuværende udgift til hver, de certificeringer og den påviste track record hos dem, der udfører arbejdet, engagementskadencen og de uafhængighedskrav, jeres standarder pålægger, med. I en reguleret virksomhed kan PCI DSS og lignende regimer tvinge ekstern uafhængig test uanset hvor godt jeres interne team er; i det offentlige gør indkøbsregler og behovet for at vise en vurdering på armslængde før en authorization to operate ofte en akkrediteret tredjepart obligatorisk, ikke valgfri.

6. **Har vi en sikker kanal, hvor udenforstående forskere kan rapportere sårbarheder, og er vi klar til at håndtere det, der kommer ind?** En stor offentligt vendt organisation bliver allerede undersøgt af forskere, uanset om den inviterer dem eller ej, og det eneste spørgsmål er, om de kan fortælle jer det sikkert eller er tvunget til at publicere eller sælge, hvad de finder. Det modstridende hensyn er parathed: at åbne en politik for koordineret offentliggørelse eller et betalt bug bounty genererer indkommende rapporter og en triagebyrde, og et program, der betaler for fund, det aldrig retter, er værre end intet. Tag jeres nuværende security.txt-fil og rapporteringsadresse, hvis nogen, jeres indtags- og triageproces, de svartidslinjer, I ærligt kan love, og backlogkapaciteten til at udbedre det, der kommer, med. For offentlige agenturer er en politik for sårbarhedsoffentliggørelse på offentlige systemer i stigende grad et direktiv frem for en høflighed, og for virksomheder er et veldrevet bounty både en kilde til kreative fund og dokumentation for modenhed under kundernes due diligence, så beslutningen handler mindre om, hvorvidt I skal have en kanal, end om I er bemandet til at honorere den.

## Sektorperspektiv

**Startup.** I har ikke råd til et internt red team, så læg billig dækning i lag i stedet. Kobl sårbarhedsscanning ind i jeres udrulningspipeline for at fange kendte afhængighedsfejl ved hvert build, offentliggør en security.txt-fil og en simpel politik for koordineret offentliggørelse, så forskere kan nå jer, og bestil en enkelt grey-box-penetrationstest fra et velanset firma før jeres første virksomhedsaftale, og spor hvert fund til en bekræftet rettelse. Hastighed betyder mere end et bredt program: vælg den ene test, der låser op for et salg eller lukker jeres største risiko, og spring resten over, til I vokser.

**Lille virksomhed.** Uden en sikkerhedsspecialist på lønningslisten og med et stramt budget så køb frem for at bygge. Brug en administreret scanningstjeneste og hyr et eksternt pentestfirma på en beskeden kadence i stedet for at opstille nogen intern evne, og sørg for, at jeres kontrakt inkluderer en gentest, så "rettet" er bevist, ikke antaget. Jeres træk med højest værdi og lavest omkostning er en offentliggjort måde, hvorpå enhver kan rapportere en fejl, plus disciplinen til at patche hurtigt, da det meste reelle kompromittering af en virksomhed i jeres størrelse kommer gennem kendte, upatchede svagheder.

**Stor virksomhed.** I skala er udfordringen styring på tværs af mange teams. Kør kontinuerlig scanning under periodiske uafhængige eksterne pentests, der opfylder standarder som PCI DSS, vedligehold et internt red team til kontinuerlig modstanderemulering og purple teaming, og styr udbedring som en sporet portefølje med ejere, risikobaserede frister og obligatorisk gentest. Før hver uopdaget teknik ind i detektionsudvikling, og producér revisionsdokumentationen, dækning, tidslinjer og lukningsrater, som compliance og jeres bestyrelse forventer.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former hele programmet. Vedligehold en politik for sårbarhedsoffentliggørelse på offentligt vendte systemer, som direktiver i stigende grad kræver, brug akkrediterede uafhængige vurderingsfolk til den penetrationstest, der lukker porten for et systems authorization to operate, og model modstanderemulering på de specifikke nationalstatsaktører, jeres efterretningspartnere flager. Behandl autorisation, omfang og datahåndtering med ekstra stringens, fordi systemerne kører valg, ydelser og kritisk infrastruktur, og gør gentest til en forudsætning for at holde ethvert system live.

## Eksempler

**Startup.** Et fintech-startup på tyve personer har ikke råd til et internt red team, så det lægger det i lag, det kan. Automatiseret sårbarhedsscanning kører ved hver udrulning gennem dets pipeline og fanger kendte afhængighedsfejl tidligt. Det offentliggør en security.txt-fil og en simpel politik for koordineret offentliggørelse og åbner så et beskedent bug bounty på en offentlig platform, når produktet stabiliseres, og betaler rigtige forskere for rigtige fejl. Før det underskriver sin første virksomhedskunde, bestiller det en grey-box-penetrationstest af applikationen fra et velanset firma, sporer hvert fund til lukning i sin normale issuetracker og betaler for en gentest for at bekræfte rettelserne. Denne lagdelte tilgang giver troværdig sikkerhedsdækning til en pris, startuppet kan opretholde, og pentestrapporten bliver dokumentation, det kan dele under kundernes due diligence.

**Stor virksomhed.** En multinational detailhandler, der behandler kortbetalinger, skal opfylde PCI DSS, som kræver både intern og ekstern penetrationstest mindst årligt og efter væsentlige ændringer, plus segmenteringstest for at bevise, at kortholdermiljøet er isoleret. Den kører kontinuerlig scanning på tværs af tusinder af aktiver, bestiller uafhængige eksterne pentests for at opfylde standarden og vedligeholder et internt red team, der kører assumed breach-øvelser forankret i MITRE ATT&CK mod trusselsaktører, der er kendt for at målrette detailhandel. Red teamet arbejder tæt sammen med sikkerhedsdriftsfunktionen fra kapitel 4.4: hver uopdaget teknik bliver en detektionsudviklingsticket, og kvartalsvise purple team-sessioner justerer alarmerne. Udbedring spores med risikobaserede frister, og hele programmet producerer den revisionsdokumentation, som compliance i kapitel 4.6 kræver.

**Offentlig sektor.** Et nationalt agentur, der kører borgerydelsessystemer, står over for nationalstatsmodstandere og et offentligt mandat til at beskytte følsomme personoplysninger. Det vedligeholder en politik for sårbarhedsoffentliggørelse på alle offentligt vendte systemer, som regeringsdirektiver i stigende grad kræver, og giver forskere en sikker kanal til at rapportere fejl. Uafhængige tredjepartsvurderingsfolk gennemfører penetrationstests som del af autorisationsprocessen, før noget system går live, og kontinuerlig overvågning inkluderer løbende scanning. Agenturet kører modstanderemulering modelleret på de specifikke trusselsgrupper, dets efterretningspartnere flager, og regelmæssige tabletop-øvelser øver den hændelsesrespons og juridiske koordinering, et reelt brud ville kræve. Fund fodrer et formelt udbedringsprogram med påbudte tidslinjer, og gentest er en forudsætning for at beholde et systems authorization to operate.

## Business case: motivation, ROI og TCO

Afkastet af offensiv sikkerhed er det brud, I ikke led. Et alvorligt databrud koster millioner i direkte respons, regulatoriske bøder, juridisk ansvar, kundefrafald og omdømmeskade, og den enkeltstående dyreste faktor er, hvor længe en indtrængen går uopdaget. Red teaming og purple teaming angriber direkte det tal ved at skrumpe hullet mellem kompromittering og detektion. En penetrationstest, der finder en udnyttelig sti til jeres kundedatabase, rettet før en angriber finder den, betaler hele programmet mange gange tilbage i en enkelt undgået hændelse.

Der er også hårde drivkræfter. PCI DSS påbyder penetrationstest for enhver, der håndterer kortdata. Rammeværker og offentlige autorisationsregimer kræver uafhængig vurdering før og under drift. Virksomhedskunder kræver nylige pentestrapporter som betingelse i kontrakter. I disse tilfælde er test ikke valgfri, og spørgsmålet er blot, om I udtrækker reel sikkerhedsværdi af penge, I alligevel må bruge.

De totale ejeromkostninger omfatter mere end engagementsgebyret. Budgettér værktøjet og personalet til et internt team, hvis I bygger et, triagebyrden ved et bug bounty og frem for alt udbedringsarbejdet, fund genererer, som er der, hvor den reelle udgift lander. Et program, der bestiller test, men underfinansierer rettelser, er det værste fra begge verdener: det betaler for de dårlige nyheder og betaler så igen, når det ignorerede fund udnyttes. For at føre sagen over for ledelsen så bind test til målinger, de følger: gennemsnitlig tid til at opdage, gennemsnitlig tid til at udbedre, lukkede revisionsfund og risikoreduktionen på jeres mest kritiske aktiver.

## Anti-mønstre og faldgruber

- **Scan-og-omdøb:** at sælge en sårbarhedsscanning som en penetrationstest og aflevere et værktøjs output uden menneskelig validering eller kædning af exploits.
- **Rapportér og glem:** at behandle leverancen som målet, arkivere fundene og aldrig spore udbedring eller gentest.
- **Afgræns for at bestå:** at indsnævre engagementet, så de systemer, der mest sandsynligt fejler, belejligt er uden for grænserne, og producere en ren rapport, der intet betyder.
- **Red team som resultattavle:** et modstridende team, der hamstrer teknikker og fejrer sejre i stedet for at gøre forsvarere bedre.
- **At teste et umodent blue team skjult:** at køre et stealth red team, før I har nogen detektionsevne, så øvelsen kun beviser, hvad I allerede vidste.
- **Ingen autorisation eller vagt omfang:** at begynde arbejde uden skriftlig tilladelse eller lade omfanget glide ind i systemer, I ikke ejer, og invitere juridisk katastrofe.
- **Perimeterbesættelse:** kun at teste den eksterne kant, mens assumed breach-virkeligheden ignoreres, at angribere starter indenfor.
- **At ignorere offentliggørelseskanalen:** at have ingen sikker måde for eksterne forskere at rapportere fejl, så de publicerer offentligt eller sælger i stedet.
- **Teatermålinger:** at tælle fundne sårbarheder frem for reduceret risiko, forbedret detektion og forkortet tid til udbedring.

## Modenhedsmodel

- **Niveau 1, Opstart:** Test er lejlighedsvis og reaktiv, ofte en enkelt årlig pentest udført for at sætte flueben, eller udløst først efter en hændelse. Rapporter arkiveres med lidt opfølgning, udbedring er usporet, der er ingen offentliggørelseskanal, og detektion af en reel indtrængen er utestet og sandsynligvis fraværende.
- **Niveau 2, Udvikling:** Sårbarhedsscanning og penetrationstest findes, men er inkonsistente på tværs af teams, hvor nogle grupper scanner kontinuerligt og andre slet ikke. Fund indfanges et sted, selv om ejere og frister er pletvise, gentest er ad hoc, og en koordineret offentliggørelseskanal kan findes for nogle systemer, men ikke hele ejendommen.
- **Niveau 3, Standardisering:** Offensiv test er et dokumenteret program håndhævet i hele organisationen, ikke en begivenhed. Scanning kører kontinuerligt under planlagte penetrationstests bestilt på en defineret kadence og efter større ændringer, engagementsregler og autorisation er standardpraksis, hvert fund spores til lukning med en ejer og en risikobaseret frist, gentest er obligatorisk, og en politik for koordineret offentliggørelse dækker alle offentligt vendte systemer.
- **Niveau 4, Styring:** Programmet måles og styres mod baselines. I følger gennemsnitlig tid til at opdage og gennemsnitlig tid til at udbedre, procentdelen af red team-teknikker, der producerede et signal, detektionsdækning mod de MITRE ATT&CK-teknikker, der er relevante for jeres sektor, rater for gentagelse af fund og offentliggørelsessvartider, og I holder hver måling mod et mål og handler, når den driver. Assumed breach-øvelser og modstanderemulering er rutine, et red team opererer kontinuerligt, fund fodrer detektionsudvikling, og go/no-go-beslutninger hviler på dokumentation frem for mening.
- **Niveau 5, Orkestrering:** Red og purple teaming er integreret på tværs af organisationen og adaptive. Hver teknik afbildes til en testet detektion, modstanderemulering følger de specifikke trusselsaktører, der i øjeblikket målretter jeres sektor, efterhånden som efterretning skifter, og programmet forfiner løbende sit omfang, sine teknikker og sine målinger, efterhånden som det lærer. Offensiv test, sikkerhedsdrift, detektionsudvikling og hændelsesrespons fungerer som én løkke, der målbart skrumper hullet mellem kompromittering og detektion over tid.

## Idéer til drøftelse

1. Hvis en reel angriber fik fodfæste som almindelig medarbejder i dag, hvor langt kunne vedkommende nå, før nogen opdagede det, og hvordan ved I det?
2. Hvilke af jeres seneste engagementer var reelt realistiske, og hvilke var afgrænset, så de sandsynlige fejl belejligt var uden for grænserne?
3. Hvor mange fund fra jeres forrige test er stadig åbne, og hvad siger det om, hvorvidt test eller udbedring er jeres reelle flaskehals?
4. Har eksterne forskere en sikker, åbenlys måde at rapportere en sårbarhed til jer, og hvad sker der, når en rapport ankommer?
5. Hvornår øvede jeres hændelsesresponsfolk sidst et brud på papir, og afslørede tabletoppen huller, jeres tekniske tests overså?
6. Måler I fundne sårbarheder, eller måler I forbedret detektion og reduceret risiko?

## Vigtigste pointer

- Offensiv sikkerhed er et spektrum: scanning finder kendte fejl, pentest beviser udnyttelighed, og red teaming tester detektion og respons. Afstem engagementet med spørgsmålet.
- Skriftlig autorisation og klare engagementsregler er linjen mellem sikkerhedstest og kriminalitet; spring dem aldrig over, især ikke på systemer, I ikke fuldt ejer.
- Værdien ligger i udbedring og gentest, ikke rapporten. Spor hvert fund med en ejer, en risikobaseret frist og en bekræftet rettelse.
- Et red team findes for at gøre blue team bedre. Før fund ind i detektionsudvikling, foretræk purple teaming og assumed breach-øvelser, og forankr kampagner i reelle modstandertekniker via MITRE ATT&CK.
- Mål detektion og respons, ikke kun antal sårbarheder, og pas på engagementer afgrænset til at bestå, som producerer komfort uden sikkerhed.

## Referencer og videre læsning

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
