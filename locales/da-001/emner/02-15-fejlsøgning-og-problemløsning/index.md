# 2.15 Fejlsøgning og problemløsning

## Overblik og motivation

Fejlsøgning er det disciplinerede arbejde med at finde ud af, hvorfor et system gør noget, det ikke bør, og problemløsning (troubleshooting) er den samme færdighed rettet mod et kørende produktionssystem under tidspres. Begge er den [videnskabelige metode](https://en.wikipedia.org/wiki/Scientific_method) anvendt på fejl: du observerer en overraskende adfærd, danner en hypotese om dens årsag, designer et eksperiment, der ville bekræfte eller afkræfte den, og lader dokumentationen, ikke din mavefornemmelse, fortælle dig, hvad der skal ændres. Gjort på denne måde er fejlsøgning en lærbar, undervisbar ingeniørfærdighed. Gjort som folklore bliver det overtro: at ændre tilfældige linjer, genstarte servere og håbe.

For et stort team er forskellen dyr. En enkelt svær fejl kan trække ingeniører ind på tværs af flere tjenester, æde vagttimer og standse en udgivelse. Når hver person fejlsøger på instinkt, akkumuleres den indsats ikke, fordi ingen kan reproducere eller forklare, hvad andre prøvede. Når teamet deler en metode (reproducér først, isolér ved søgning, fang fejlen i en fejlende test, ret derefter), bliver den samme indsats til en gentagelig proces og en voksende regressionssuite. Fejlsøgning hænger tæt sammen med teststrategi (kapitel 2.4), med softwarekvalitet (kapitel 2.11) og med de konstruktionsvaner (kapitel 2.9), der gør kode diagnosticerbar fra begyndelsen.

I virksomheds- og offentlige sammenhænge stiger indsatsen. Virksomhedsfejl krydser tjeneste- og teamgrænser, så den person, der ser symptomet, sjældent er den, der ejer årsagen. Offentlige systemer tilføjer begrænsninger, de fleste ingeniører aldrig møder: luftgappede eller begrænsede miljøer, hvor du ikke kan tilslutte en debugger til produktion, reproducerbare builds, der skal diagnosticeres ud fra artefakter, og revisionsspor, der skal registrere, hvad du ændrede og hvorfor. I alle tre er målet det samme: at erstatte gætteri med dokumentation.

## Grundprincipper

- **Reproducér, før du teoretiserer.** En fejl, du ikke kan udløse efter behov, er et rygte, ikke en defekt.
- **Fejlsøgning er hypotesetest.** Angiv, hvad du tror, og design så det billigste eksperiment, der kunne bevise, at du tager fejl.
- **Læs fejlen og stakssporet først.** Systemet fortæller som regel, hvor det gik i stykker, før du ændrer en linje.
- **Søg i problemrummet, skan det ikke.** Halvér den mistænkte region hvert trin i stedet for at læse oppefra og ned.
- **Reducér til det minimale.** Skær tilfældet ned, til kun den essentielle udløser er tilbage.
- **Én ændring ad gangen.** Haglskudsredigeringer ødelægger den dokumentation, der ville have fortalt dig, hvilken ændring der betød noget.
- **Fang fejlen i en fejlende test, før du retter den.** Rettelsen er først bevist, når den test bliver grøn og forbliver grøn.
- **Find grundårsagen, ikke det nærmeste symptom.** En lap, der skjuler symptomet, lader fejlen vende tilbage.

## Anbefalinger

### Reproducér fejlen pålideligt, før du ændrer noget

Dit første job er en pålidelig reproduktion: et sæt trin eller et automatiseret tilfælde, der udløser fejlen efter behov. Uden den kan du ikke skelne en reel rettelse fra en tilfældighed, fordi symptomet kan komme og gå af grunde, du aldrig kontrollerede. Fastlæg input, miljø, versioner og timing. Hvis fejlen er intermitterende, så led efter den skjulte variabel, der får den til at dukke op (en bestemt datapost, en urgrænse, en samtidig anmodning), til reproduktionen er pålidelig. En pålidelig reproduktion er det enkeltstående mest værdifulde artefakt i fejlsøgning, fordi alt efter den bliver målbart.

### Læs fejlen, logs og stakssporet, før du rører ved kode

Før du danner en eneste teori, så læs, hvad systemet allerede har fortalt dig. [Stakssporet](https://en.wikipedia.org/wiki/Stack_trace) (optegnelsen over kaldekæden i det øjeblik, fejlen opstod) navngiver som regel filen, linjen og sekvensen, der fejlede. Undtagelsesbeskeden, loglinjerne omkring den og værdierne i scope indsnævrer søgningen, før du har ændret noget. Ingeniører spilder timer på at teoretisere om årsager, som stakssporet udelukkede på første linje. Behandl fejloutputtet som det første vidne, læs det omhyggeligt og fuldstændigt, og beslut først derefter, hvad der skal undersøges.

### Isolér ved binær søgning i problemrummet

Skan ikke koden oppefra og ned. Søg i den. Brug [binær søgning](https://en.wikipedia.org/wiki/Binary_search_algorithm): find et punkt, hvor tilstanden stadig er god, og et punkt, hvor den allerede er dårlig, tjek derefter midtpunktet, og gentag og halvér den mistænkte region hver gang. Det forvandler en søgning i tusind linjer til ti spørgsmål. Når regressionen opstod over en række commits, anvend så den samme idé på historikken med bisektion: `git bisect` går gennem commit-området, og du markerer hver revision som god eller dårlig, til den navngiver den præcise ændring, der indførte fejlen. Automatisér god-eller-dårlig-testen, og bisektionen kører af sig selv.

### Reducér til et minimalt reproducerbart eksempel

Når du kan udløse fejlen, så skrump den. Et [minimalt reproducerbart eksempel](https://en.wikipedia.org/wiki/Minimal_reproducible_example) er det mindste input og den korteste kodesti, der stadig fejler: fjern data, features og trin, til enhver yderligere fjernelse får fejlen til at forsvinde. Reduktion er ikke beskæftigelsesterapi; hvert element, du eliminerer, er en årsag, du har udelukket, så det minimale tilfælde peger ofte lige på fejlen. Når inputtet er stort eller struktureret, så automatisér skrumpningen med [delta-fejlsøgning](https://en.wikipedia.org/wiki/Delta_debugging), en algoritme, der systematisk fjerner stykker af et fejlende input for at finde den minimale fejlende delmængde. En lille, selvstændig reproduktion er også den bedst mulige fejlrapport at give til et andet team.

### Instrumentér med logs, brug derefter en interaktiv debugger

Afstem værktøjet efter fejlen. Logning og målrettet instrumentering er bedst, når du har brug for at se adfærd over tid, på tværs af processer eller i et miljø, du ikke kan pause. En interaktiv debugger, der lader dig sætte breakpoints, træde linje for linje og inspicere live tilstand, er bedst, når du kan køre koden lokalt og har brug for at se en enkelt eksekvering tæt på. Tilføj instrumentering som et bevidst eksperiment knyttet til en hypotese, ikke som spredte print-udsagn, og fjern den eller forfrem den til permanent struktureret logning, når fejlen er løst. I produktion så støt dig til observerbarhedsdrevet fejlsøgning: begivenheder med høj kardinalitet og distribueret sporing (kapitel 9.2) lader dig følge én anmodning på tværs af mange tjenester, hvilket ofte er den eneste måde at fejlsøge et distribueret system, du ikke kan tilslutte en debugger til.

### Skriv en fejlende test, der fanger fejlen, før du retter den

Før du skriver rettelsen, så skriv en test, der fejler på grund af fejlen. Det gør tre ting på én gang: det beviser, at du faktisk forstår årsagen, det definerer præcis, hvad "rettet" betyder, og det bliver et permanent værn. Lav så rettelsen og se testen blive grøn. Den test slutter sig nu til din suite som et [regressionstest](https://en.wikipedia.org/wiki/Regression_testing)-værn, så den samme fejl ikke kan vende tilbage ubemærket. Den praksis knytter fejlsøgning direkte til din teststrategi (kapitel 2.4): hver svær fejl, du løser, efterlader suiten stærkere, end du fandt den, og en ustabil test får samme behandling (reproducér ikke-determinismen, og værn derefter mod den) frem for en genforsøgsannotation.

### Find grundårsagen, og hold analysen fejlfri

At rette symptomet er ikke at rette fejlen. Spor fejlen tilbage til dens sande oprindelse, og spørg hvorfor i hvert lag, til du når en årsag, du kan fjerne frem for at maskere. For fejl, der nåede produktion, så kør en fejlfri grundårsagsanalyse som del af hændelsesstyring (kapitel 9.3): fokusér på de system- og procesforhold, der lod fejlen blive udgivet og overleve, aldrig på den enkelte, der skrev linjen. Bebrejdelse driver information under jorden, og fejlsøgning kører på information. Resultatet er både en rettelse og en ændring i, hvordan den klasse af fejl fanges tidligere næste gang.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Logning og instrumentering | Virker i produktion og distribuerede systemer; fanger adfærd over tid | Støj, omkostning og logvækst; kan forstyrre timingfejl |
| Interaktiv debugger | Præcis, live inspektion af tilstand; hurtig til lokale fejl | Ubrugelig i begrænset eller luftgappet produktion; kan skjule samtidighedsfejl |
| Reproducér-først-disciplin | Forvandler gætteri til måling; muliggør en fejlende test | Langsom på forhånd; nogle fejl er reelt svære at udløse |
| Binær søgning og bisektion | Hurtig isolation, selv i ukendt kode | Kræver en pålidelig god-eller-dårlig-test; svært når fejl interagerer |
| Delta-fejlsøgningsreduktion | Skrumper store input automatisk til udløseren | Opsætningsomkostning; antager at fejlen er deterministisk |
| Ret symptomet nu | Genopretter service hurtigt under pres | Lader grundårsagen vende tilbage; opbygger gæld |

Den centrale spænding er hastighed versus sikkerhed. Under en produktionshændelse kan du have brug for at stoppe blødningen først (en tilbagerulning eller en symptomlap) for at genoprette service, og det er legitimt. Fejlen er at stoppe der. Løs spændingen ved at adskille de to jobs: afbød hurtigt for at beskytte brugerne, reproducér derefter, find grundårsagen, og tilføj regressionsværnet, før du betragter fejlen som lukket. En symptomrettelse uden opfølgning er en fejl, du har aftalt at møde igen.

## Spørgsmål til drøftelse med dit team

1. **Når nogen rammer en svær fejl, hvad er det første, vedkommende gør, og er det at reproducere eller at gætte?** Det ærlige svar afslører, om jeres team har en fælles metode eller et rum fuld af privat folklore. Bed folk fortælle højt om deres seneste vanskelige fejl: fik de en pålidelig reproduktion først, eller begyndte de at ændre kode og genstarte ting? Et team, der reproducerer først, kan give en fejl videre mellem folk, fordi reproduktionen rejser med; et team, der gætter, kan ikke, fordi hvert forsøg er ugentageligt. Det betyder mere, efterhånden som teamet vokser, da den person, der ser et symptom, i stigende grad ikke er den, der kan rette det. Hvis standarden er at gætte, så aftal reproducér-først som en norm og gør en ren reproduktion til adgangsprisen til en fejlsag.

2. **Vender de fejl, vi retter, tilbage, og ville vi vide det, hvis de gjorde?** En fejl, der vender tilbage, er en fejl, hvis grundårsag aldrig blev fjernet, og hvis rettelse aldrig blev vogtet af en test. Træk sidste kvartals hændelser og genåbnede sager og tæl, hvor mange der var gentagelser eller nære fætre til tidligere fejl. Hver gentagelse er dokumentation for, at teamet lappede et symptom, sprang den fejlende test over eller stoppede grundårsagsanalysen for tidligt. Rettelsen er en regel: ingen fejl lukkes, før en test, der fejler på den gamle adfærd, består på den nye og slutter sig til suiten. Tag en nylig tilbagevendende fejl med og spørg, hvilket værn der ville have fanget den, for det værn er det, I manglede.

3. **Kan vi overhovedet fejlsøge vores produktionssystemer, givet hvordan vi må røre dem?** I virksomheds- og især offentlige miljøer kan I ofte ikke tilslutte en debugger, ikke reproducere med rigtige data og ikke ændre et kørende system uden et revisionsspor. Hvis jeres eneste fejlsøgningsteknik er en lokal interaktiv debugger, er I blinde netop, hvor de sværeste fejl bor. Spørg, hvilken dokumentation en produktionsfejl faktisk efterlader: strukturerede logs, distribuerede spor (kapitel 9.2), kernedumps eller reproducerbare buildartefakter. Beslut nu, hvad I skal fange som standard, så en fremtidig hændelse kan diagnosticeres, fordi I ikke kan tilføje instrumentering til en fejl, der allerede er sket. I regulerede sammenhænge så bekræft, at det samme spor også opfylder jeres revisionsforpligtelser.

4. **Når en produktionshændelse tvinger os til at stoppe blødningen hurtigt, hvordan sikrer vi så, at grundårsagen stadig bliver fundet bagefter?** Under en hændelse er en tilbagerulning eller en symptomlap det rette første træk for at beskytte brugerne, men faren er, at sagen lukkes i det øjeblik, servicen vender tilbage, og den underliggende fejl aldrig diagnosticeres. For et stort team er det her, gæld akkumuleres usynligt, fordi den samme klasse af fejl dukker op igen på en anden tjeneste og med en anden vagthavende ingeniør måneder senere. Tag jeres sidste par alvorlighedsgrad-ét-hændelser med og tjek hver: fulgte en reproduktion, en grundårsagsanalyse og et regressionsværn efter afbødningen, eller sluttede historien ved "service genoprettet"? Aftal en eksplicit regel om, at en afbødet hændelse forbliver åben, til grundårsagen er forstået og vogtet, og navngiv, hvem der ejer den opfølgning. I virksomheds- og offentlige sammenhænge så bind dette til jeres hændelsesstyringsproces (kapitel 9.3), så efterbehandlingen er et påkrævet, reviderbart trin frem for en høflighed, der glider, når den næste brand starter.

5. **Hvor meget af en fejl kan vi faktisk rekonstruere bagefter, og hvem besluttede, hvad vi fanger som standard?** I kan ikke tilslutte instrumentering til en fejl, der allerede er sket, så diagnosticerbarheden af enhver hændelse er fastlagt på forhånd af de logs, spor, målinger og dumps, I valgte at udsende. Det modstridende hensyn er omkostning og støj: begivenheder med høj kardinalitet og fuld sporing er ikke gratis, og overlogning begraver signalet, mens den oppuster lager og, i regulerede sammenhænge, jeres eksponering for dataopbevaring. Tag en reel nylig hændelse med og spørg, hvilken dokumentation den efterlod, og arbejd så baglæns til, hvad I ønsker, I havde fanget, og hvad det ville koste at beholde. Beslut bevidst, hvilke signaler der er slået til som standard versus samplede eller tilvalg, og registrér den beslutning, så det er en politik, ikke et tilfælde. For et virksomheds- eller offentligt system så tilføj, hvem der er ansvarlig for det observerbarhedsbudget, og om det fangede spor også opfylder forpligtelser om revision, privatliv og dataresidens.

6. **Behandler vi fejlsøgning som en undervist, målbar færdighed, eller optager nye ingeniører den ved osmose?** Fejlsøgning er lærbar, men de fleste teams underviser aldrig eksplicit i den, så juniorer arver den folklore, der sidder nærmest, og reproducér-først-metoden spredes ujævnt eller slet ikke. Spændingen er, at bevidst undervisning (parprogrammering på svære fejl, skrive fund efter hændelser ned, følge målinger) koster seniortid, som altid føles nødvendig andre steder. Tag to tal med til drøftelsen: jeres gentagelsesrate for fejl og jeres tid til diagnose, for hvis I ikke kan måle dem, kan I ikke se, om jeres metode forbedres eller forfalder. Overvej, om onboarding inkluderer en reel fejlsøgningsøvelse, og om grundårsagsfund faktisk fodrer tidligere opdagelse. I en stor eller offentlig organisation bliver en dokumenteret, målt fejlsøgningspraksis også dokumentation for ingeniørstringens, som revisorer, tilsynsmyndigheder og tilsynsorganer i stigende grad forventer at se.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og ingen slack er dit mål at gøre fejl billige at reproducere og umulige at glemme, ikke at bygge tung proces. Støt dig til `git bisect`, en hurtig lokal reproduktion og én fejlende test pr. rettet fejl, for den vane koster minutter og stopper dig i at betale igen for den samme fejl, mens du forsøger at udgive. Spring formelle efterbehandlinger over, men spring aldrig regressionstesten over: det er det ene artefakt, der er småt nok til altid at have råd til og værdifuldt nok til altid at beholde.

**Lille virksomhed.** Du har sandsynligvis ingen dedikeret pålideligheds- eller observerbarhedsspecialist og et stramt værktøjsbudget, så foretræk det, din stak allerede giver: læselige stakspor, strukturerede logs og den sporing, der er indbygget i de frameworks og hostede tjenester, du har købt. Når du evaluerer en ny platform, så vej, hvor diagnosticerbare den gør fejl, fordi et billigt værktøj, der skjuler, hvad der gik galt, koster dig langt mere i gættetid, end licensen sparede. Reproducér-først og én-ændring-ad-gangen er gratis discipliner, der betaler sig hurtigst, når ingen har timer at give af.

**Stor virksomhed.** Dine svære fejl krydser tjeneste- og teamgrænser, så den person, der ser symptomet, sjældent ejer årsagen, og en fælles metode betyder mere end enhver enkelts færdighed. Standardisér reproducér-først, binær søgeisolation, en fejlende test før rettelsen og fejlfri efterbehandlinger på tværs af teams, og invester i distribueret sporing (kapitel 9.2), så én anmodning kan følges på tværs af tjenester. Styr fejlsøgning som en målt evne: følg gentagelsesrate for fejl og tid til diagnose, og før grundårsagsfund tilbage i tidligere opdagelse, så den samme klasse af fejl ikke turnerer rundt på dit tjenestekort.

**Offentlig sektor.** Indkøbsregler, begrænsede miljøer og offentlig ansvarlighed former, hvordan du overhovedet må fejlsøge. Du kan ofte ikke tilslutte en debugger til produktion eller kopiere borgerdata til en bærbar, så design til diagnose ud fra det tilladte: reproducerbare builds, syntetiske poster i en isoleret enklave og strukturerede logs og spor fanget som standard. Registrér hvert diagnostisk trin og hver ændring i revisionssporet, og kræv, at leverandører eksponerer nok telemetri og buildreproducerbarhed til, at du kan undersøge fejl uafhængigt frem for at afhænge af leverandørens ord.

## Eksempler

**Startup.** Et team på fire ingeniører bliver ved med at se checkout fejle for en brøkdel af brugerne, men aldrig i test. I stedet for at gætte fanger en ingeniør en pålidelig reproduktion ved at afspille den præcise fejlende anmodningsnyttelast og læser så det stakspor, de havde ignoreret, som peger på et datoparsningskald. En hurtig `git bisect` på tværs af ugens commits navngiver den ændring, der skiftede et datobibliotek. De skriver en fejlende test med det anstødelige tidsstempel, retter parseren, ser testen blive grøn og beholder den i suiten. Hele undersøgelsen tager en eftermiddag, fordi de reproducerede, før de teoretiserede, og fejlen vender aldrig tilbage.

**Stor virksomhed.** En betalingsplatform ser intermitterende timeouts, som intet enkelt team kan forklare, fordi symptomet viser sig i checkout, men årsagen bor tre tjenester væk. Vagthavende ingeniører bruger distribueret sporing (kapitel 9.2) til at følge én fejlende anmodning på tværs af tjenestegrænser og finder et nedstrøms kald, der lejlighedsvis deadlocker under samtidig belastning, en klassisk [kapløbstilstand](https://en.wikipedia.org/wiki/Race_condition), hvor resultatet afhænger af uheldig timing mellem tråde. De reproducerer den med en belastningstest, fanger den i en fejlende integrationstest, retter låsningen og kører en fejlfri efterbehandling (kapitel 9.3), der tilføjer et sporingsspan og en alarm, så den næste forekomst fanges på minutter, ikke dage.

**Offentlig sektor.** Et ydelsesagentur kører sit sagssystem i et luftgappet miljø, hvor ingeniører ikke kan tilslutte en debugger til produktion og ikke kan kopiere borgerdata til deres bærbare. En beregningsfejl dukker op i afstemning. Teamet fejlsøger ud fra det, miljøet tillader: strukturerede logs, et reproducerbart build, de kan stille op i en isoleret testenklave, og syntetiske poster, der genskaber det fejlende tilfælde. Hvert diagnostisk trin registreres i revisionssporet, rettelsen leveres med en fejlende-så-bestående test som dokumentation, og grundårsagsanalysen fodrer en ny kontrol før udgivelse. Fordi reproduktionen brugte syntetiske data, forlod ingen borgerpost nogensinde grænsen.

## Business case: motivation, ROI og TCO

Afkastet af disciplineret fejlsøgning måles i ingeniørtimer, der ikke bruges på at gætte, og i fejl, der ikke gentager sig. En udiagnosticeret intermitterende fejl kan æde dage af seniortid og gentagne eskaleringer på vagt; en reproducér-først-metode forvandler det til en afgrænset, uddelegerbar opgave, og vanen med den fejlende test stopper den samme fejl i at fakturere dig igen næste kvartal. På tværs af en stor organisation er den akkumulerende effekt af aldrig at betale igen for den samme fejl betydelig, og den forbedrer direkte andelen af fejlslagne ændringer og middeltiden til genopretning, som ledelsen allerede følger.

De totale ejeromkostninger er mest uddannelse og værktøj, og de er beskedne. I har brug for fælles konventioner (reproducér først, én ændring ad gangen, en fejlende test før rettelsen), debuggere og sporing, der allerede er almindelige i værktøjskæden, og den observerbarhedsinvestering, der er beskrevet i kapitel 9.2. Den større, skjulte omkostning er alternativet: en kultur af overtro, hvor ingeniører anvender haglskudsændringer, symptomer lappes og vender tilbage, og vagtbelastningen vokser uden grænse. Alene at reducere manuelt slid på vagt retfærdiggør ofte investeringen, og argumentet over for ledelsen er enklest formuleret som færre gentagne hændelser og hurtigere genopretning for en engangsomkostning i vaner og instrumentering.

## Anti-mønstre og faldgruber

- **Haglskudsfejlsøgning:** at ændre mange ting på én gang, så selv en rettelse ikke lærer dig noget om årsagen.
- **Rettelse uden reproduktion:** at erklære sejr over en fejl, du aldrig kunne udløse efter behov.
- **At ignorere fejloutputtet:** at teoretisere om årsager, som stakssporet allerede udelukkede.
- **Symptomlapning:** at gøre symptomet tavst, mens grundårsagen overlever og vender tilbage.
- **Print-udsagnsvækst:** spredt fejlsøgningsoutput efterladt i koden, der tilføjer støj i stedet for et eksperiment knyttet til en hypotese.
- **At springe regressionstesten over:** at rette fejlen, men ikke efterlade noget værn, så den stille kan komme tilbage.
- **At genforsøge ustabile tests:** at skjule ikke-determinisme med genforsøg i stedet for at fejlsøge den underliggende kapløbstilstand eller [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), en fejl der ændrer sig eller forsvinder i det øjeblik, du forsøger at observere den.
- **Bebrejdelsesdrevne efterbehandlinger:** at straffe forfatteren, hvilket driver den information under jorden, fejlsøgning afhænger af.

## Modenhedsmodel

- **Niveau 1, Opstart:** Fejlsøgning er individuel folklore og reaktion. Ingeniører gætter, anvender haglskudsændringer og genstarter ting. Fejl rettes ved symptomet, reproduktioner er sjældne, og de samme fejl gentager sig. Produktion er knap nok diagnosticerbar, og ingen kan give en fejl videre til nogen, fordi intet forsøg er gentageligt.
- **Niveau 2, Udvikling:** Nogle ingeniører reproducerer pålideligt, læser stakspor og bruger debuggere, men praksis er inkonsistent og varierer fra person til person og team til team. Logning findes, men er støjende og ustruktureret. Rettelser leveres nogle gange med en fejlende test, ofte ikke, og grundårsagsanalyse sker kun, når nogen insisterer.
- **Niveau 3, Standardisering:** Reproducér-først, binær søgeisolation, én ændring ad gangen og en fejlende test før rettelsen er dokumenterede teamnormer håndhævet i hele organisationen. Bisektion og delta-fejlsøgningsreduktion er almindelig praksis. Produktion har struktureret logning og sporing (kapitel 9.2), og fejlfri efterbehandlinger (kapitel 9.3) er standardresponsen på hver undsluppen fejl.
- **Niveau 4, Styring:** Fejlsøgningspraksis måles og styres mod baselines. Gentagelsesrate for fejl, tid til diagnose, antal genåbnede sager og andelen af rettelser leveret med en regressionstest følges pr. team og gennemgås efter en kadence. Reproduktion og færdig grundårsagsanalyse behandles som porte frem for gode intentioner, og tendenser mod baselinen driver, hvor I investerer i værktøj, uddannelse og observerbarhed.
- **Niveau 5, Orkestrering:** Fejlsøgning er en undervist færdighed integreret med kvalitet (kapitel 2.11) og hændelsesstyring (kapitel 9.3), og hele løkken tilpasser sig løbende. Observerbarhed er designet ind, så de fleste produktionsfejl kan diagnosticeres uden en debugger, hver løst fejl styrker regressionssuiten, og grundårsagsfund fodrer tidligere opdagelse, så klasser af fejl forebygges frem for at blive diagnosticeret igen. Organisationen omfordeler indsats, efterhånden som dens systemer og fejlformer udvikler sig, og gentagelsesraten for fejl bliver ved med at falde.

## Idéer til drøftelse

1. Hvor stor en andel af jeres seneste fejl blev reproduceret pålideligt, før nogen ændrede kode, og hvad siger den andel om jeres metode?
2. Når en regression dukker op, rækker jeres team ud efter bisektion, eller læser det kode i hånden, til nogen spotter den?
3. Hvor diagnosticerbart er jeres produktionssystem i dag, og hvad ville I give for at have fanget om en fejl, der allerede er sket?
4. Leveres jeres rettelser konsekvent med en fejlende-så-bestående test, og hvis ikke, hvor bryder den disciplin sammen?
5. Hvordan håndterer I ustabile tests: fejlsøger I ikke-determinismen, eller dækker I over den med genforsøg?
6. Undervises fejlsøgning bevidst til nye ingeniører, eller overlades de til at optage folklore ved osmose?

## Vigtigste pointer

- Fejlsøgning er hypotesetest: reproducér pålideligt, læs fejlen og stakssporet, og isolér derefter ved binær søgning og bisektion frem for at skanne.
- Reducér fejlen til et minimalt reproducerbart eksempel, med delta-fejlsøgning til store input, fordi hvert fjernet element er en udelukket årsag.
- Afstem værktøjet efter fejlen: instrumentering og sporing til produktion og distribuerede systemer (kapitel 9.2), interaktive debuggere til lokal undersøgelse.
- Skriv en fejlende test, der fanger fejlen, før du retter den, så rettelsen er bevist og fejlen vogtet for altid (kapitel 2.4).
- Find og fjern grundårsagen, kør fejlfri efterbehandlinger (kapitel 9.3), og behandl fejlsøgning som en lærbar færdighed, ikke folklore.
- Ændr én ting ad gangen; haglskudsændringer og symptomlapper ødelægger dokumentation og inviterer fejlen tilbage.

## Referencer og videre læsning

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller and Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (the delta debugging algorithm)
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (chapter on debugging)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (the chapters on debugging and assertions)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (the debugging chapter)
- John Regehr, "Reducers Are Fuzzers" and related writing on test-case reduction
- Charity Majors, Liz Fong-Jones, and George Miranda, *Observability Engineering* (debugging production with high-cardinality telemetry and tracing)
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (blameless postmortems and production debugging)
