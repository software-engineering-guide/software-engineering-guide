# 3.3 Distribuerade system

## Översikt och motivation

Ett [distribuerat system](https://en.wikipedia.org/wiki/Distributed_computing) är varje system vars komponenter körs på mer än en maskin och samordnar sig över ett nätverk. I samma stund du korsar en processgräns över ett nätverk ärver du några hårda sanningar som helt enkelt inte finns inuti en enda process. Nätverket är opålitligt och dess latens varierar. Meddelanden kan gå förlorade, dupliceras, fördröjas eller byta ordning. Fjärrkomponenter fallerar på egen hand. Det finns ingen gemensam klocka. De klassiska "[missuppfattningarna om distribuerad databehandling](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)" (nätverket är pålitligt, latensen är noll, bandbredden är oändlig, topologin ändras aldrig) namnger exakt de antaganden som orsakar avbrott. Ditt jobb är att designa för dessa verkligheter från början, i stället för att återupptäcka dem under en incident.

För en stor organisation är distribution inte valfri. Varje system som betjänar nationell eller global skala, förbinder flera avdelningar eller behöver hög tillgänglighet i drift kommer att spänna över många maskiner, datacenter och ofta regioner. Företag kör distribuerade transaktionssystem, händelsepipelines och multiregionsdriftsättningar. Myndigheter kör integrationer mellan myndigheter där varje myndighet äger sina egna system och ingen kontrollerar helheten. Här syns gapet mellan en robust och en skör design som rubrikavbrott, missade bidragsutbetalningar och regulatoriska konsekvenser. Teknikerna i det här kapitlet (konsistensresonemang, [idempotens](https://en.wikipedia.org/wiki/Idempotence), omförsök med fördröjning, [kretsbrytare](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern), [sagor](https://en.wikipedia.org/wiki/Long-running_transaction) och distribuerad observerbarhet) är dina standardförsvar.

Det svåraste med distribuerade system är att fel är partiella och intermittenta. Ett program på en enda maskin fungerar antingen eller kraschar. Ett distribuerat system kan vara halvfungerande: vissa begäranden lyckas, vissa får tidsgränsfel och vissa går i tysthet förlorade, allt på en gång. Det här kapitlet fokuserar på de resonemang och mönster som låter ett stort team bygga system som degraderar graciöst och förblir begripliga under partiellt fel.

## Nyckelprinciper

- **Nätverket är inte pålitligt.** Designa varje fjärrinteraktion utifrån att den kan vara långsam, fallera, duplicera eller byta ordning.
- **Du kan inte få perfekt konsistens och perfekt tillgänglighet i drift under en partition.** Välj medvetet per interaktion (CAP/PACELC), och kom ihåg att latens är en kostnad även när det inte finns någon partition.
- **Gör operationer idempotenta.** Om en operation säkert kan försökas om blir det mesta av distribuerad felhantering hanterbar.
- **Varje fjärranrop behöver en tidsgräns.** Obegränsade väntetider förvandlar ett långsamt beroende till ett systemomfattande avbrott.
- **Föredra eventuell konsistens där verksamheten tillåter, men gör den uttrycklig.** Användare och revisorer måste förstå när de kan se inaktuella data.
- **Isolera fel.** Skott och kretsbrytare hindrar en felande komponent från att kaskadera in i alla.
- **Du kan inte felsöka det du inte kan se.** Distribuerade flöden kräver korrelerad spårning, mått och loggar över varje hopp.
- **"Exakt-en-gång-leverans" är en myt. Exakt-en-gång-*bearbetning* är en teknisk bedrift.** Designa för minst-en-gång med deduplicering.

## Rekommendationer

### Resonera om konsistens med CAP och PACELC

[CAP-satsen](https://en.wikipedia.org/wiki/CAP_theorem) säger att ett system under en nätverkspartition måste välja mellan konsistens (varje läsning ser den senaste skrivningen) och tillgänglighet i drift (varje begäran får ett svar). [PACELC](https://en.wikipedia.org/wiki/PACELC_design_principle) lägger till en andra avvägning: **E**lse (när det inte finns någon partition) byter du ändå **L**atens mot **C**onsistency (konsistens). Stämpla inte detta som en etikett för hela systemet. Besluta det per operation. En banks saldoöverföring behöver stark konsistens och vägrar hellre än riskerar en dubbelutgift. Ett socialt flöde eller en produktvisningsräknare kan acceptera inaktualitet i utbyte mot tillgänglighet och hastighet. Skriv ner vilken konsistensmodell varje dataflöde använder (stark, kausal, läs-dina-skrivningar eller eventuell) så att ingen antar en garanti systemet faktiskt inte ger.

### Bygg idempotens, tidsgränser, omförsök och fördröjning tillsammans

Behandla dessa fyra tekniker som ett paket. Ge varje fjärroperation en **tidsgräns**, så att ett hängt beroende inte kan blockera en tråd för alltid. Vid fel, **försök om**, men bara för operationer som är säkra att upprepa. Säker att upprepa betyder **idempotent**: tilldela varje begäran en unik nyckel och låt mottagaren deduplicera, så att ett omförsökt "debitera kort" inte debiterar två gånger. Sprid dina omförsök med **[exponentiell fördröjning](https://en.wikipedia.org/wiki/Exponential_backoff) och jitter**, så att du undviker en synkroniserad omförsöksstorm som förvandlar ett kort glapp till en självförvållad [överbelastningsattack](https://en.wikipedia.org/wiki/Denial-of-service_attack). Sätt tak på antalet omförsök och den totala tidsbudgeten, eftersom att försöka om för evigt bara flyttar felet. Utan idempotens är omförsök farliga. Utan fördröjning är omförsök destruktiva.

### Lägg till kretsbrytare och skott för att stoppa kaskader

En **kretsbrytare** bevakar anrop till ett beroende och "öppnar", efter en tröskel av fel, för att falla snabbt under en avkylningsperiod i stället för att stapla fler begäranden på en kämpande tjänst, och "halvöppnar" sedan för att testa återhämtning. Det stoppar kaskaden där en långsam nedströmstjänst utmattar varje anropares trådar tills hela systemet stannar. **Skott** partitionerar resurser (trådpooler, anslutningspooler) så att mättnad i ett beroende inte kan äta den kapacitet andra behöver. Para båda med graciös nedgradering: när ett icke kritiskt beroende är otillgängligt, returnera cachade eller standardsvar i stället för att fälla hela begäran.

### Hantera distribuerade transaktioner med sagor, inte tvåfas-commit

Du kan vanligen inte hålla en enda [ACID](https://en.wikipedia.org/wiki/ACID)-transaktion (atomicitet, konsistens, isolering, beständighet) över flera tjänster eller databaser. Distribuerad [tvåfas-commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) är långsam, låser resurser och skär tillgängligheten i drift. Använd i stället **sagamönstret**. Modellera en affärstransaktion som en sekvens av lokala transaktioner, var och en publicerar en händelse som utlöser nästa, med en **kompenserande åtgärd** för varje steg för att ångra det om ett senare steg fallerar. Sagor kommer i två smaker. **Koreografi** låter tjänster reagera på varandras händelser, utan central kontrollant. **Orkestrering** låter en central samordnare driva stegen, vilket är lättare att resonera om och bevaka. Sagor omfamnar eventuell konsistens: systemet passerar genom mellanliggande tillstånd och konvergerar sedan. Designa därför användarupplevelsen och revisionsspåret för att ta hänsyn till tillstånden "pågående" och "kompenserad".

### Behandla exakt-en-gång som minst-en-gång plus deduplicering

[Meddelandeförmedlare](https://en.wikipedia.org/wiki/Message_broker) kan inte verkligen garantera exakt-en-gång-leverans över fel. Vad de och du *kan* åstadkomma är **minst-en-gång-leverans med idempotent bearbetning**, vilket ger exakt-en-gång-*effekter*. Designa konsumenter att hantera dubblettmeddelanden säkert, med idempotensnycklar eller en logg över bearbetade meddelanden. Känn din förmedlares ordnings- och leveransgarantier exakt. För strömmar, använd konsumentgrupper, partitioner och offsethantering medvetet, och gör omkörning säker, så att du kan spela upp en ström igen efter en buggrättelse utan att korrumpera nedströmstillstånd.

### Instrumentera distribuerade flöden från början till slut

Anta observerbarhetens tre pelare, korrelerade över tjänstegränser. Propagera ett **spårnings-/korrelations-ID** genom varje hopp, så att du kan följa en enskild användarbegäran över alla tjänster den rör (distribuerad spårning). Sänd strukturerade **mått** (latenspercentiler, felfrekvenser, mättnad, genomströmning) per tjänst och per beroende. Sänd strukturerade **loggar** som bär korrelations-ID:t. Använd allt detta för att sätta servicenivåmål och för att larma på symptom användare faktiskt känner, som felfrekvens och latens, snarare än bara på enskilda maskiners hälsa. I ett distribuerat system är observerbarhet inte valfria verktyg. Det är det enda sättet att förstå beteende under partiellt fel.

## Avvägningar: för- och nackdelar

| Teknik | Fördelar | Nackdelar / kostnad |
|---|---|---|
| Stark konsistens | Enkel mental modell, inga inaktuella läsningar | Lägre tillgänglighet i drift under partitioner, högre latens, samordningskostnad |
| Eventuell konsistens | Hög tillgänglighet, låg latens, skalbar | Inaktuella läsningar, komplext resonemang, behöver konfliktlösning |
| Omförsök med fördröjning | Rider ut övergående fel automatiskt | Förstärker belastning om det missbrukas. Behöver idempotens och tak |
| Kretsbrytare / skott | Förhindrar kaskadfel, faller snabbt | Tillagd komplexitet, justering av trösklar, risk för förtida utlösning |
| Saga (mot 2PC) | Skalbar, tillgänglig, inga distribuerade lås | Eventuell konsistens, kompensationslogik, svårare att resonera om |

Huvudavvägningen är mellan samordning och oberoende. Varje garanti du vill ha över maskiner (konsistens, ordning, exakt-en-gång) kostar latens, tillgänglighet i drift eller komplexitet. Den kräver att maskiner är överens, och att vara överens över ett opålitligt nätverk är dyrt. Skickligheten är att köpa bara de garantier verksamheten verkligen behöver, operation för operation, och att designa allt annat för graciös nedgradering. Köp för mycket konsistens och dina system blir långsamma och sköra. Köp för lite och du får tyst dataförstörelse som visar sig som ett revisionsmisslyckande månader senare.

## Frågor att diskutera med ditt team

1. **Levereras era motståndskraftsmönster som gemensamma plattformsstandardval, eller uppfinner varje team tidsgränser och omförsök på nytt?** Kapitlet behandlar idempotens, tidsgränser, begränsade omförsök, kretsbrytare och spårning som billigast och mest pålitliga när de byggs en gång in i gemensamma bibliotek och plattformsstandardval. I en stor organisation garanterar det att lämna åt varje team att handrulla dem inkonsekvens: vissa vägar försöker om icke-idempotenta operationer, vissa har ingen tidsgräns, vissa sänder inget korrelations-ID. Ta med belägg genom att granska ett urval av tjänster och räkna hur många som sätter en uttrycklig tidsgräns på varje fjärranrop och propagerar ett spårnings-ID från början till slut. Om det talet är lågt är åtgärden en plattformsinvestering, inte ett utbildningsmemo. Standardval gör också motståndskraft testbar och granskningsbar, vilket tillsynsmyndigheter inom finans och myndigheter alltmer förväntar sig att ni visar.

2. **Komponeras era tidsgränser och omförsöksbudgetar över hela anropskedjan, eller försöker en djup begäran om sig själv in i ett avbrott?** En enda begäran korsar ofta många hopp, och om varje lager oberoende försöker om tre gånger med sin egen tidsgräns multipliceras det innersta felet och den yttre anroparen väntar långt förbi varje mänskligt tolerabel gräns. Sätt en total tidsbudget för den användarvända begäran och dela ned den genom kedjan, så att en inre tjänst vet hur lite tid den har kvar och faller snabbt snarare än försöker om in i en storm. Ta med ert beroendediagram och ett verkligt spår, addera sedan den sämsta kombinationen av tidsgräns och omförsök och jämför den med vad användaren faktiskt kommer att vänta. Exponentiell fördröjning med jitter och ett tak på totala försök hindrar ett kort glapp från att bli en självförvållad överbelastningsattack. Djupa, pratsamma synkrona kedjor är fienden här, så svaret kan driva er mot asynkrona flöden eller färre hopp.

3. **När injicerade ni senast de fel er design påstår sig överleva, och vad gick sönder som ni inte väntat er?** Motståndskraftsmönster är hypoteser tills du får systemet att fallera med avsikt: döda en instans, lägg latens på ett beroende, släpp en andel av meddelandena, leverera en batch två gånger. I ett distribuerat system är de intressanta felen partiella och intermittenta, så en kretsbrytare eller sagakompensation som ser korrekt ut i koden kan ändå bete sig fel under en verklig tidsgräns-som-kanske-slutfördes. Ta med resultaten av en faktisk spelövning eller felinjektionskörning, inte ett designdokument, och notera vilka larm som utlöstes, hur lång tid spårningen tog för att lokalisera felet och om någon omförsöksstorm bildades. I reglerade sektorer är belägg för att ni har testat fel en del av att visa operativ motståndskraft för revisorer. Om ni aldrig har kört en hör det första experimentet hemma i en testmiljö med en snäv sprängradie och en avbrottsbrytare.

4. **Kan det ägande teamet för varje större dataflöde namnge den konsistensmodell det ger, och matchar det valet vad verksamheten faktiskt behöver?** CAP och PACELC tvingar fram ett medvetet val per operation, men i en stor organisation är standardvalet drift: ett flöde som började eventuellt konsistent för en lågriskräknare återanvänds för något som nu godkänner betalningar eller ger åtkomst, och ingen omprövar garantin. De motstridiga hänsynen är verkliga, eftersom stark konsistens kostar tillgänglighet i drift under en partition och latens även när det inte finns någon, medan eventuell konsistens köper hastighet till priset av inaktuella läsningar och konfliktlösning ni måste designa för. Ta med en katalog över era främsta dataflöden, var och en märkt med sin nuvarande modell (stark, kausal, läs-dina-skrivningar eller eventuell) och affärskonsekvensen av en inaktuell eller förlorad läsning, och leta sedan efter missmatchningar där garantin är starkare eller svagare än insatserna motiverar. I företagsfinans och i myndigheters bidrags- eller identitetssystem är en eventuellt konsistent läsning bakom ett auktoritativt beslut den sortens tysta defekt som visar sig som ett revisionsfynd eller ett felaktigt avslag månader senare, så själva granskningen är belägg revisorer kommer att be att få se.

5. **Hur beter sig era affärstransaktioner över flera tjänster halvvägs, och vem är ansvarig för de kompensationer som löser upp dem?** Att ersätta tvåfas-commit med sagor betyder att systemet passerar genom synliga mellanliggande tillstånd, och ett steg kan lyckas medan ett senare steg fallerar och utlöser en kompenserande åtgärd som vänder det. För ett stort team väcker detta svåra ägarskapsfrågor: kedjan godkänn-debitera-kreditera-huvudbok korsar ofta flera team, och en kompensation ett team glömmer att implementera lämnar pengar eller poster permanent inkonsekventa. Väg koreografi, där tjänster reagerar på varandras händelser utan central kontrollant och flödet är svårt att se, mot orkestrering, där en samordnare driver och bevakar stegen till priset av en komponent att köra. Ta med tillståndsdiagrammet för er viktigaste saga, listan över kompenserande åtgärder och deras ägare och belägg för att tillstånden "pågående" och "kompenserad" hanteras både i användarupplevelsen och i revisionsspåret. Inom bank och offentlig ärendehantering förväntar sig tillsynsmyndigheter att ni kan rekonstruera exakt vad som hände med en transaktion som fallerade mitt i, så ett omodellerat mellanliggande tillstånd är en regelefterlevnadslucka, inte bara en bugg.

6. **Överlever era meddelandekonsumenter duplicerad och omordnad leverans, och kan ni bevisa det innan förmedlaren tvingar frågan?** Exakt-en-gång-leverans är en myt, så er verkliga garanti är minst-en-gång, och en konsument som antar att varje meddelande anländer en gång och i ordning kommer att dubbelbearbeta den dag förmedlaren omleverera en batch efter en failover. Över många team växer risken, eftersom en icke-idempotent konsument på en delad ström kan korrumpera nedströmstillstånd andra team är beroende av, och felet är osynligt tills omkörning eller en partition ändrar ordning på händelser. Avvägningen är den tekniska kostnaden för idempotensnycklar, en logg över bearbetade meddelanden och uttrycklig offset- och partitionshantering, mot kostnaden för tyst korruption. Ta med listan över konsumenter på era kritiska strömmar, notera vilka som deduplicerar och vilka som bara hoppas, och ta med resultatet av ett faktiskt omleverans- eller omkörningstest snarare än en försäkran att det borde gå bra. För datautbyte mellan myndigheter och för företagshändelsepipelines är förmågan att spela upp en ström igen säkert efter en buggrättelse, utan att skapa duplicerade ärenden eller debiteringar, både en operativ nödvändighet och något revisorer vill se påvisat.

## Sektorsperspektiv

**Startup.** Med två eller tre rörliga delar och inget plattformsteam, stå emot att bygga distribuerat maskineri du inte kan bemanna. Köp motståndskraft där den bor i det SDK din betalnings- eller meddelandeleverantör redan ger, och lägg din knappa uppmärksamhet på de två mönster som förhindrar oåterkallelig skada: en idempotensnyckel på varje penningflyttande eller kontoändrande anrop, och en tidsgräns med begränsade omförsök så att en opålitlig anslutning aldrig utför samma åtgärd två gånger. Håll antalet nätverkshopp litet, eftersom varje synkront beroende du lägger till är ännu en sak som kan fallera innan du har någon med jour som märker det.

**Småföretag.** Du har sannolikt ingen distribuerade-system-specialist och en snäv budget, så behandla detta som en fråga om köp, inte bygg: föredra hanterade köer, hanterade databaser och plattformar som hanterar omförsök, ordning och deduplicering åt dig snarare än infrastruktur du måste driva. Rama in din risk i klartext, genom att veta vilka operationer som skulle skada en kund om de kördes två gånger eller returnerade inaktuella data, och slå på de idempotens- och minst-en-gång-funktioner dina leverantörer redan erbjuder. Undvik att sy ihop tjänster genom en delad databas för att fejka en transaktion, eftersom det i det tysta återskapar det svåraste distribuerade problemet utan verktygen att hantera det.

**Storföretag.** Kärnproblemet är enhetlighet över många team, så leverera idempotens, tidsgränser, begränsade omförsök, kretsbrytare och korrelerad spårning som gemensamma plattformsstandardval i stället för att låta varje grupp handrulla dem. Standardisera hur konsistensmodeller och leveransgarantier deklareras per flöde, kör felinjektion och spelövningar i regelbunden takt och få totala tidsbudgetar att komponeras över djupa anropskedjor så att en tjänst inte kan försöka om plattformen in i ett avbrott. Hantera motståndskraft som en mätt förmåga med servicenivåmål på användarsynliga symptom, för i din skala kan en enda saknad tidsgräns kaskadera till ett rubrikavbrott.

**Offentlig sektor.** System mellan myndigheter betyder att ingen äger helheten, så designa för gränser ni inte kontrollerar: varaktiga köer med minst-en-gång-leverans, deduplicering på ett stabilt meddelande-ID och korrelations-ID:n som flödar över myndighetsgränser för att ge revisorer ett spår från början till slut. Upphandlings- och transparensregler driver er att dokumentera konsistensmodellen och leveransgarantin för varje integration, och att hålla auktoritativa beslut (identitet, behörighet, bidrag) på starkt konsistenta läsningar snarare än cachade slutpunkter. Behandla belägg för testade fel och rekonstruerbar transaktionshistorik som leverabler, eftersom operativ motståndskraft och ansvarsskyldighet inför allmänheten är avtalsmässiga och lagstadgade skyldigheter, inte interna trevligheter.

## Exempel

**Startup.** En liten fintech-startup har bara två rörliga delar som talar över nätverket: sin app och en tredjepartsbetalningsleverantör. Även i den här storleken låter den varje debiteringsbegäran bära en idempotensnyckel och omsluter anropet i ett omförsök med fördröjning, så att ett tappat svar på en opålitlig anslutning aldrig dubbeldebiterar en kund. Att hoppa över detta känns billigt dag ett, men den första dubbla debiteringen som drabbar en verklig användare kostar en supportbrand, en återbetalning och en bucka i förtroende det unga företaget inte har råd med.

**Storföretag.** En global åktjänstplattform bearbetar resbetalningar genom en saga: godkänn kort, debitera passagerare, kreditera förare, registrera huvudboksposten, var och en en lokal transaktion med en kompenserande återföring. Varje steg bär en idempotensnyckel, så att omförsök efter en nätverkstidsgräns aldrig dubbeldebiterar. Anrop till bedrägeripoängtjänsten sitter bakom en kretsbrytare. När den degraderar under topp öppnar brytaren och resor faller tillbaka på en konservativ poäng i stället för att blockera varje resa. När en kund bestrider en resa låter distribuerad spårning ingenjörer följa den över ett dussin tjänster på sekunder.

**Offentlig sektor.** En nationell identitetstjänst används av många myndigheter för verifiering. Den erbjuder en starkt konsistent läsning för auktoritativa statuskontroller (ni får inte godkänna ett bidrag mot inaktuella identitetsdata), plus en eventuellt konsistent, cachad slutpunkt för högvolyms, icke kritiska uppslag. Datautbyte mellan myndigheter går över en varaktig meddelandekö med minst-en-gång-leverans, och varje myndighets konsument deduplicerar på ett meddelande-ID, så att en omlevererad post inte skapar ett duplicerat ärende. Korrelations-ID:n flödar över myndighetsgränser och ger revisorer ett spår från början till slut av hur en medborgares data rörde sig mellan avdelningar.

## Affärsnytta: motiv, ROI och TCO

Disciplin inom distribuerade system köps billigt och dess frånvaro betalas katastrofalt. Införandekostnaden är ingenjörstid för att bygga in idempotens, tidsgränser, omförsök, kretsbrytare och spårning i gemensamma bibliotek och plattformsstandardval. Det är en måttlig, mest engångsinvestering som sedan gynnar varje team. Kostnaden för att *inte* införa den mäts i stora avbrott: en enda saknad tidsgräns som kaskaderar till ett fullt plattformsavbrott, en icke-idempotent betalningsväg som dubbeldebiterar tusentals kunder eller en sagalös distribuerad transaktion som lämnar data permanent inkonsekventa. Var och en av dessa är en rubrikincident med direkta intäkts-, åtgärds- och anseendekostnader, och i reglerade sektorer, böter.

Rama in ärendet inför ledningen kring tillgänglighet i drift och sprängradie. Motståndskraftsmönster minskar direkt både frekvensen och varaktigheten av allvarliga incidenter, de mått chefer redan följer som drifttid och genomsnittlig återställningstid. Distribuerad observerbarhet är den enskilt största spaken på MTTR: team med korrelerad spårning löser incidenter över tjänster på en bråkdel av tiden. Eftersom dessa förmågor bäst levereras som gemensamma plattformsstandardval är deras marginalkostnad per team låg och deras organisationsomfattande utdelning växer. TCO-argumentet är enkelt: att bygga in motståndskraft från början är en bråkdel av kostnaden för att eftermontera den efter avbrottet som tvingar fram frågan.

## Antimönster och fallgropar

- **Inga tidsgränser.** Ett enda hängt beroende utmattar varje tråd och fäller hela systemet.
- **Att försöka om icke-idempotenta operationer.** Duplicerade biverkningar: dubbla debiteringar, duplicerade poster, dubbla e-postmeddelanden.
- **Omförsöksstormar.** Synkroniserade omförsök utan fördröjning och jitter som förstärker ett litet glapp till ett avbrott.
- **Att anta exakt-en-gång-leverans.** Att bygga konsumenter som går sönder på dubblettmeddelanden förmedlaren så småningom kommer att leverera.
- **Distribuerade transaktioner via delad databas.** Att koppla tjänster genom en databas för att fejka ACID, vilket återskapar en distribuerad monolit.
- **Att ignorera partiellt fel.** Kod som antar att ett fjärranrop antingen lyckas helt eller fallerar helt, utan hantering av "fick tidsgränsfel men slutfördes kanske".
- **Inga korrelations-ID:n.** Att felsöka en incident över tjänster genom att grepa orelaterade loggar på tio maskiner.
- **Pratsamma synkrona anropskedjor.** Djupa synkrona beroendegrafer där ett enda långsamt hopp stoppar hela begäran.

## Mognadsmodell

- **Nivå 1: Initiera.** Fjärranrop behandlas som lokala anrop. Tidsgränser saknas eller är naiva, omförsök saknas eller är hänsynslösa och fel kaskaderar över systemet. Det finns ingen gemensam bild av konsistens eller leverans, och att felsöka en incident över tjänster betyder loggspeleologi maskin för maskin i efterhand.
- **Nivå 2: Utveckla.** Vissa team lägger till tidsgränser och grundläggande omförsök och lite idempotens, men praxis är inkonsekvent från tjänst till tjänst. Loggar är centraliserade men inte korrelerade, så att spåra en begäran över hopp är manuellt. Distribuerade transaktioner hoppas fungera snarare än modelleras, och konsistensgarantier lever i enskilda ingenjörers huvuden.
- **Nivå 3: Standardisera.** Idempotens, begränsade omförsök, fördröjning med jitter, kretsbrytare och skott är standard i hela organisationen via gemensamma bibliotek. Sagor med kompenserande åtgärder hanterar transaktioner över flera tjänster, distribuerad spårning med korrelations-ID:n finns på plats och varje större dataflöde dokumenterar sin konsistensmodell och leveransgaranti. Reglerna är nedskrivna och upprätthålls i hela organisationen snarare än lämnas åt varje team.
- **Nivå 4: Hantera.** Motståndskraft mäts mot utgångslägen, inte bara finns. Du följer felfrekvens, latenspercentiler, mättnad och genomströmning per tjänst och beroende, bevakar omförsöksandelar och kretsbrytares öppenfrekvens och sätter servicenivåmål på användarsynliga symptom. Totala tidsbudgetar verifieras komponeras över anropskedjor, genomsnittlig återställningstid för incidenter över tjänster är ett bevakat mått och resultat från felinjektion och spelövningar matar de tal som grindar varje ändring.
- **Nivå 5: Orkestrera.** Motståndskraft är det kontinuerligt förbättrade plattformsstandardvalet, integrerat i hela organisationen och adaptivt efter förhållanden. Felinjektion körs rutinmässigt i produktion med snäva sprängradier, system degraderar graciöst per konstruktion och konsistens- och leveransval omprövas när belastning och affärsinsatser förskjuts. Måtten från nivå 4 driver automatiska svar och stadig arkitektonisk utveckling, så att den distribuerade egendomen blir mer robust för varje incident i stället för att bara överleva den.

## Idéer för diskussion

1. Vilka av era kritiska operationer är genuint idempotenta i dag, och vilka är det i tysthet inte?
2. Kan ni för varje större dataflöde ange konsistensmodellen och leveransgarantin utantill?
3. Var skulle en kretsbrytare ha förhindrat ert senaste kaskadavbrott?
4. Hur lång tid tar det i dag att spåra en enskild felande begäran över alla tjänster den rör?
5. Vilka av era "distribuerade transaktioner" förlitar sig på tur, och vilka är äkta sagor med kompensationer?
6. Om er meddelandeförmedlare omleverade varje meddelande två gånger i en timme, vad skulle gå sönder?

## Viktigaste punkter

- Anta att nätverket är opålitligt och att fel är partiella. Designa varje fjärrinteraktion för långsamhet, förlust, duplicering och omordning.
- Besluta konsistens mot tillgänglighet i drift per operation med CAP/PACELC. Dokumentera modellen varje flöde ger.
- Idempotens, tidsgränser, begränsade omförsök och fördröjning-med-jitter är ett paket. Anta aldrig omförsök utan de tre andra.
- Kretsbrytare och skott begränsar fel. Sagor med kompensationer ersätter ohanterbara distribuerade transaktioner.
- Behandla leverans som minst-en-gång och gör bearbetning idempotent för att uppnå exakt-en-gång-effekter.
- Korrelerad spårning, mått och loggar är det enda sättet att förstå och driva distribuerade flöden.

## Referenser och vidare läsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew Tanenbaum and Maarten van Steen, *Distributed Systems: Principles and Paradigms*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Sam Newman, *Building Microservices*
- Chris Richardson, *Microservices Patterns* (sagas, transactional messaging)
- Eric Brewer, "CAP Twelve Years Later" and Daniel Abadi on PACELC
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"
- Cindy Sridharan, *Distributed Systems Observability*
- Nassim Nicholas Taleb's notion of antifragility (as applied by resilience-engineering literature)
