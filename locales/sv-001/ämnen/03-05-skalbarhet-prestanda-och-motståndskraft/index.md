# 3.5 Skalbarhet, prestanda och motståndskraft

## Översikt och motivation

[Skalbarhet](https://en.wikipedia.org/wiki/Scalability), prestanda och motståndskraft är tre skilda kvaliteter, och människor suddar ofta ihop dem. **Prestanda** är hur snabbt systemet svarar och hur mycket arbete det gör per resursenhet. **Skalbarhet** är hur väl det behåller prestanda när belastningen växer. **Motståndskraft** är hur väl det fortsätter fungera, eller degraderar graciöst, när saker fallerar. Ett system kan vara snabbt men oskalbart (utmärkt vid låg belastning, kollapsar vid hög), skalbart men skört (hanterar volym men faller när en komponent fallerar) eller motståndskraftigt men långsamt. En stor organisation behöver alla tre, utformade in från början, eftersom att eftermontera någon av dem efter lansering är dyrt och störande.

För företags- och myndighetssystem är konsekvenserna av att få dessa fel offentliga och allvarliga. Tänk på en bidragsportal som viker sig första dagen av ett nytt program, ett skatteingivningssystem som får tidsgränsfel vid deadline eller en betalningsplattform som går ner under köptoppen. Det är de misslyckanden som blir rubriker, utlöser utredningar och urholkar allmänhetens förtroende. Dessa system möter också starkt toppade, ofta lagstadgat tidssatta belastningar (ingivningsdeadlines, anmälningsfönster, löningsdagar) och stränga krav på tillgänglighet i drift och återställning. Du måste planera kapacitet för förutsägbara toppar, degradera graciöst under de oförutsägbara och återhämta dig inom definierade gränser för tid och dataförlust efter en katastrof. Det är teknik med en dimension av offentlig ansvarsskyldighet.

Det här kapitlet behandlar horisontell mot vertikal skalning, tillståndslöshet och [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) som möjliggörare av skala, [lastbalansering](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [autoskalning](https://en.wikipedia.org/wiki/Autoscaling) och kapacitetsplanering, prestandateknik med uttryckliga budgetar, motståndskraftsmönster och [kaosteknik](https://en.wikipedia.org/wiki/Chaos_engineering) samt multiregion-[katastrofåterställning](https://en.wikipedia.org/wiki/Disaster_recovery) inramad av RTO, RPO och verksamhetskontinuitet. Det enande budskapet är att dessa kvaliteter är produkten av medveten design och kontinuerlig testning, inte av hopp.

*Se även:* kapitel 3.3 (distribuerade system), kapitel 9.1 (driftsäkerhetsteknik) och kapitel 9.2 (observerbarhet och övervakning).

## Nyckelprinciper

- **Designa för utskalning, inte uppskalning.** Vertikal skalning har ett tak och en [enskild felpunkt](https://en.wikipedia.org/wiki/Single_point_of_failure). Horisontell skalning är hur du når stor, motståndskraftig skala.
- **Tillståndslöshet är möjliggöraren av horisontell skala.** Om varje begäran kan gå till vilken instans som helst kan du fritt lägga till och ta bort kapacitet.
- **Du kan inte förbättra det du inte mäter.** Prestandaarbete drivs av profilering och belastningstestning mot uttryckliga budgetar, aldrig av gissningar.
- **Allt fallerar. Designa för det.** Anta att komponenter kommer att fallera och bygg så att systemet överlever deras fel.
- **Graciös nedgradering slår hårt fel.** Ett delvis fungerande system som fäller icke väsentliga funktioner är bättre än ett totalt avbrott.
- **Kapacitet planeras, toppar absorberas.** Prognostisera förutsägbar belastning. Använd autoskalning och utrymme för resten.
- **Återställningsmål är affärsbeslut.** RTO och RPO väljs av verksamheten mot kostnad och konstrueras sedan mot.
- **Testa motståndskraft medvetet.** Du vet inte att ett system är motståndskraftigt förrän du har fått det att fallera med avsikt.

## Rekommendationer

### Föredra horisontell skalning och designa tillståndslösa tjänster

Vertikal skalning (större maskiner) är enkel och ibland rätt första steg, men den slår i ett hårt tak, blir oproportionerligt dyr i toppen och lämnar en enskild felpunkt. **Horisontell skalning** (fler maskiner bakom en lastbalanserare) skalar långt längre och förbättrar tillgängligheten i drift, eftersom att förlora en instans är överlevbart. Förutsättningen är **tillståndslöshet**. Håll ingen klientsession eller begäranstillstånd på instansen. Skjut det till ett delat lager (databas, cache, token). Tillståndslösa tjänster kan läggas till, tas bort, ersättas och lastbalanseras fritt, vilket är det som gör både autoskalning och rullande driftsättning möjliga. Där tillstånd måste partitioneras, **shard**a efter en nyckel som fördelar belastningen jämnt och håller relaterade data på samma shard.

### Lastbalansera, autoskala och planera kapacitet

Sätt en **lastbalanserare** framför varje skalad nivå för att fördela trafik och dirigera runt ohälsosamma instanser via hälsokontroller. Konfigurera **autoskalning** att lägga till kapacitet när en ledande indikator (CPU, begäranskölängd, latens) passerar en tröskel och ta bort den när belastningen faller. Justera skalningshastighet och avkylning så att du varken släpar efter en topp eller fladdrar. Autoskalning är inte en ersättning för **kapacitetsplanering**. För förutsägbara, affärskritiska toppar (skattedeadlines, anmälningsperioder, försäljningshändelser), prognostisera belastningen, förprovisionera eller förvärm kapacitet och belastningstesta mot det målet i förväg. Autoskalning ensam kan inte reagera omedelbart på en stegändring, och kallstarter lägger till latens exakt när du minst har råd med det. Behåll alltid utrymme. Att köra på 100 % lämnar inget rum för att absorbera toppar eller fel.

### Konstruera prestanda mot uttryckliga budgetar

Sätt **prestandabudgetar** (konkreta mål som p95-API-latens under 200 ms, sidan interaktiv under 2 sekunder eller kostnad per transaktion under en tröskel) och upprätthåll dem i testning och övervakning så att regressioner fäller pipelinen snarare än når användare. Driv optimering med **mätning**. Profilera för att hitta den faktiska flaskhalsen, som sällan är där du gissar, och belastningstesta för att hitta var systemet går sönder och hur det beter sig nära den gränsen. Fokusera på den kritiska vägen och svansen (p95/p99), eftersom svanslatenser dominerar användarupplevelsen i skala. Optimera den största flaskhalsen först, mät om och sluta när du möter budgeten. Att överoptimera redan tillräcklig kod är bortkastad insats.

### Bygg in motståndskraftsmönster och validera med kaosteknik

Tillämpa motståndskraftsmönstren från distribuerade system: tidsgränser, begränsade omförsök med fördröjning, [kretsbrytare](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (som faller snabbt när ett beroende är ohälsosamt) och skott (som isolerar resurspooler så att ett fel inte kan utmatta resten), plus **graciös nedgradering** (fäll eller förenkla icke väsentliga funktioner under stress: stäng av rekommendationer, servera cachat innehåll, köa icke brådskande arbete) och **lastfällning** (avvisa eller strypa överskottsbegäranden för att skydda kärnan snarare än att kollapsa helt). Eliminera enskilda felpunkter genom redundans på varje nivå. **Validera** sedan motståndskraften med kaosteknik. Injicera medvetet fel (döda instanser, lägg till latens, kapa ett beroende, fäll en zon) i kontrollerade experiment, börja i test och mogna till produktionsspelövningar, för att bevisa att systemet beter sig som designat. Motståndskraft som aldrig testats är bara en hypotes.

### Planera multiregion, katastrofåterställning och verksamhetskontinuitet

Besluta återställningsmålen uttryckligen: **RTO** (Recovery Time Objective, hur länge du kan vara nere) och **RPO** (Recovery Point Objective, hur mycket data du har råd att förlora). Dessa är affärsbeslut med direkta kostnadskonsekvenser, och de driver arkitekturen. Alternativen varierar i kostnad och hastighet: säkerhetskopiera-och-återställ (billigast, långsammast), pilotlampa, varm reserv och aktiv-aktiv multiregion (dyrast, nästan noll RTO/RPO). Välj den nivå varje systems kritikalitet motiverar. Inte allt behöver aktiv-aktiv. Replikera data över regioner i linje med vald RPO, automatisera failover och, framför allt, **testa failover regelbundet**. Otestad katastrofåterställning fallerar pålitligt när den äntligen behövs. Linda in allt detta i en **verksamhetskontinuitetsplan** som täcker människor, kommunikation och manuella reservlösningar, inte bara teknik.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar |
|---|---|---|
| Vertikal skalning | Enkel, ingen kodändring, låg initial insats | Hårt tak, kostsam i toppen, enskild felpunkt |
| Horisontell skalning | Nästan obegränsad skala, förbättrar tillgängligheten i drift | Kräver tillståndslöshet, lastbalansering, mer drift |
| Autoskalning | Matchar kostnad mot efterfrågan, hanterar varierande belastning | Reagerar med fördröjning. Kallstarter. Kan fladdra om fel justerad |
| Aktiv-aktiv multiregion | Nästan noll RTO/RPO, överlever regionförlust | Högsta kostnad och komplexitet, svår datakonsistens |
| DR med säkerhetskopiera-och-återställ | Billigast, enklast | Lång RTO, större dataförlustfönster |

Den centrala avvägningen är kostnad mot försäkran. Varje ökning av skalbarhetsutrymme, prestanda och återställningsförmåga kostar pengar och komplexitet, och avkastningen är icke-linjär. Att gå från 99,9 % till 99,99 % tillgänglighet i drift, eller från en timmes RTO till sekunder, kan multiplicera kostnaden. Disciplinen är att dimensionera varje investering efter systemets faktiska kritikalitet och verksamhetens tolerans för driftstopp och dataförlust, snarare än att reflexmässigt konstruera allt till högsta nivån. Ett medborgarvänt betalningssystem förtjänar aktiv-aktiv redundans. Ett internt rapporteringsverktyg gör det inte.

## Frågor att diskutera med ditt team

1. **När er senaste allvarliga incident hände, vilken av de tre (prestanda, skalbarhet, motståndskraft) fallerade faktiskt, och åtgärdade ni rätt en?** Kapitlet skiljer dem åt medvetet: ett system kan vara snabbt men kollapsa under belastning, skala men falla när en komponent dör eller överleva fel samtidigt som det är långsamt. Team feldiagnostiserar ofta, lägger till kapacitet till ett motståndskraftsproblem eller härdar ett system som helt enkelt var underdimensionerat för en topp. Gå igenom de två senaste allvarliga incidenterna och namnge vilken kvalitet som gick sönder och vad svaret faktiskt förbättrade. Skillnaden ändrar åtgärden: tillståndslöshet och sharding för skala, redundans och kretsbrytare för motståndskraft, profilering och budgetar för prestanda. Att få kategorin rätt är skillnaden mellan att spendera på botemedlet och att spendera på ett symptom.

2. **Fäller prestandaregressioner er pipeline, eller når de användare innan någon märker det?** En prestandabudget (p95-latens, sidan-interaktiv-tid, kostnad per transaktion) skyddar bara användare om den upprätthålls automatiskt, så att en ändring som spräcker den fäller bygget snarare än levereras. I ett stort team med många bidragsgivare kryper latens in genom tusen små commits, och utan en grind ruttnar svansen långsamt tills en lansering blottlägger den. Ta med era nuvarande budgetar och kontrollera om de är inkopplade i CI och övervakning, och om de siktar på p95 och p99 snarare än medelvärden, eftersom svansen är vad användare känner i skala. Där ingen budget finns är att sätta en det första draget. Upprätthållande är vad som förvandlar en god avsikt till en egenskap som överlever teamtillväxt.

3. **Vad fälls först under stress, och designade ni den ordningen eller kommer ni att upptäcka den i avbrottet?** Graciös nedgradering och lastfällning betyder att systemet ger upp icke väsentligt arbete för att skydda kärnan, men bara om ni i förväg har beslutat vad som är väsentligt. För en medborgarvänd tjänst är den rangordningen ofta ett policybeslut: att lämna in en skattedeklaration måste överleva även om statuspaneler och historiska uppslag går mörka. Om ingen har valt fäller systemet vad som än fallerar först, vilket kan vara precis det användare behöver mest. Lista era funktioner i prioritetsordning och bekräfta att arkitekturen kan släppa de lågprioriterade (cachade svar, avstängda rekommendationer, köat icke brådskande arbete) utan att ta den kritiska vägen med sig. Testa det sedan under verklig belastning, för otestad nedgradering är bara ett hopp.

4. **Vilka är RTO och RPO för ert mest kritiska system, vem valde faktiskt de talen och när bevisade ni senast att ni kan möta dem?** Recovery Time Objective (hur länge ni kan vara nere) och Recovery Point Objective (hur mycket data ni har råd att förlora) är affärsbeslut med direkta kostnadskonsekvenser, men i ett stort team uppfinns de ofta av den som skrev körboken snarare än ägs av de människor som är ansvariga för tjänsten. Det motstridiga draget är kostnad mot försäkran: att krympa RTO från en timme till sekunder eller RPO från minuter till noll kan multiplicera infrastrukturräkningen, så rätt tal är det verksamheten faktiskt kommer att betala för, inte det mest imponerande. Ta med de dokumenterade målen, datumet för det senaste verkliga failovertestet och den uppmätta tid och dataförlust det testet gav, för ett otestat mål är en önskan. I företags- och myndighetsmiljöer kan dessa tal vara satta av lag, avtal eller SLA, så namnge vem som godkänner dem och om den senaste repetitionen uppfyllde skyldigheten eller i det tysta missade den.

5. **För er största förutsägbara topp, litar ni på att autoskalning reagerar i stunden, eller har ni prognostiserat belastningen, förprovisionerat och belastningstestat mot det målet?** Autoskalning reagerar med fördröjning och kallstarter lägger till latens exakt när ni minst har råd med det, så en känd stegändring (en ingivningsdeadline, ett anmälningsfönster, en försäljningshändelse) är precis fallet där reaktiv skalning fallerar och medveten kapacitetsplanering vinner. Spänningen är kostnad: att förvärma kapacitet för en topp betyder att betala för utrymme som ligger oanvänt det mesta av året, och frestelsen är att hoppas att autoskalning täcker det gratis. Ta med förra årets toppsiffror, i år prognos med tillväxt och resultaten av ett belastningstest körd till en multipel av den prognosen snarare än till dagens genomsnittliga trafik. För en myndighets- eller företagstjänst som står inför en lagstadgat tidssatt topp, lägg till konsekvensen av att få det fel, eftersom en bidragsportal eller ett skattesystem som viker sig första dagen blir en offentlig utredning, inte bara en långsam eftermiddag.

6. **Har ni någonsin medvetet fällt en komponent i produktion, och matchar varje systems redundansnivå faktiskt dess kritikalitet och dess kostnad?** Motståndskraft som aldrig testats är en hypotes, och nivåerna ni kan köpa varierar från billig säkerhetskopiera-och-återställ genom varm reserv till dyr aktiv-aktiv multiregion, så disciplinen är att spendera försäkran där den är motiverad snarare än att guldplätera allt eller skydda ingenting. De motstridiga hänsynen är sprängradie och budget: kaosexperiment måste ha skyddsräcken och en avbrottsbrytare, och aktiv-aktiv för ett internt rapporteringsverktyg är slöseri medan enbart säkerhetskopiering för en betalningsplattform är vårdslöshet. Ta med en inventering av era enskilda felpunkter, redundansnivån för varje kritiskt system och belägg för den senaste kontrollerade felinjektionen och vad den avslöjade. I företags- och myndighetsportföljer, kartlägg varje nivå mot ett dokumenterat kritikalitetsbetyg så att en revisor kan se att pengarna följer risken, och så att ingen behöver försvara utgiften för första gången under avbrottet.

## Sektorsperspektiv

**Startup.** Du kan inte förutsäga om en lansering ger femtio registreringar eller femtio tusen, så köp skala snarare än bygg den: kör tillståndslösa tjänster bakom en hanterad lastbalanserare och låt plattformen autoskala på begäransfrekvens. Sätt en måttlig prestandabudget och välj hanterade datalager så att en topp inte tvingar fram en omarkitektur klockan två på natten. Hoppa över multiregion-katastrofåterställning och kaosprogram för nu. Behåll testade säkerhetskopior och lägg din knappa utvecklingsuppmärksamhet på produkten, inte på redundans din trafik ännu inte motiverar.

**Småföretag.** Utan tillförlitlighetsspecialist och med snäv budget lutar köp-mot-bygg-valet hårt mot köp: en hanterad plattform eller serverlös stack gör skalning och failover till leverantörens jobb, och en enda väl driven region räcker vanligen. Rama in motståndskraft som ett litet antal konkreta löften du kan hålla, som en nattlig säkerhetskopia du faktiskt har återställt från en gång och ett realistiskt återställningsfönster du har kommunicerat till kunder. Undvik att betala för aktiv-aktiv eller kontinuerlig belastningstestning du varken har trafiken eller personalen att motivera.

**Storföretag.** Problemet är enhetlighet över många team: standardisera prestandabudgetar upprätthållna i CI, ett gemensamt bibliotek av motståndskraftsmönster (tidsgränser, kretsbrytare, skott) och en dokumenterad redundansnivå för varje system knuten till dess kritikalitet. Reservera aktiv-aktiv multiregion för nivå-ett-tjänster, kör ett kaosteknikprogram med skyddsräcken och produktionsspelövningar och behandla kapacitetsplanering för kända toppar som en schemalagd disciplin snarare än en eftertanke. Styr RTO och RPO centralt så att varje kritiskt system har ägda, testade mål en revisor kan verifiera.

**Offentlig sektor.** Belastningen är ofta lagstadgat tidssatt och tillgänglighetsskyldigheter är lagstadgade, så kapacitetsplanering kan inte förlita sig på att autoskalning reagerar i stunden: prognostisera deadlinetoppen, förprovisionera och belastningstesta långt över prognosen. Upphandling bör specificera RTO, RPO och ett schema för repeterade failovers som avtalsmässiga krav, inte leverantörslöften, och bör undvika enregioninlåsning för kritiska tjänster. Besluta i förväg vilken väg som är rättsligt väsentlig (att lämna in en deklaration, att ansöka om ett bidrag) så att nedgradering fäller statuspaneler och uppslag först, och var transparent mot allmänheten om avbrott och återställning snarare än hoppas att ingen märker det.

## Exempel

**Startup.** En liten startup som lanseras på Product Hunt kan inte förutsäga om den får femtio registreringar eller femtio tusen, så den håller sina tjänster tillståndslösa bakom en hanterad lastbalanserare och låter plattformen autoskala på begäransfrekvens. Den sätter en måttlig prestandabudget (sidor svarar under 300 ms vid den 95:e percentilen) och väljer en hanterad databas så att en trafiktopp inte tvingar fram en omarkitektur klockan två på natten. När lanseringsdagens topp väl anländer blir sajten lite långsammare snarare än faller, och teamet lägger dagen på att prata med nya användare i stället för att slåss mot ett avbrott.

**Storföretag.** Ett streamingmediaföretag kör tillståndslösa tjänster över flera regioner bakom global lastbalansering och autoskalar på begäransfrekvens för att följa den dagliga primetime-vågen. Prestandabudgetar grindar varje release på p99-startlatens. Vid ett regionalt fel skiftar trafiken automatiskt till friska regioner, och icke väsentliga funktioner (personliga omslagsbilder, uppdatering av rekommendationer) degraderar först för att skydda uppspelningen. Företaget kör kontinuerliga kaosexperiment i produktion, avslutar rutinmässigt instanser och injicerar latens, så att verkliga fel inte går att skilja från övningar och inte orsakar något kundsynligt avbrott.

**Offentlig sektor.** En skattemyndighet vet att dess ingivningssystem möter en massiv, lagstadgat fast deadlinetopp varje år. I stället för att förlita sig på att autoskalning reagerar i stunden prognostiserar den toppbelastningen utifrån tidigare år, förprovisionerar kapacitet veckor i förväg och belastningstestar till 150 % av prognosen. Arkitekturen är tillståndslös bakom lastbalanserare med en varm reservregion. RTO och RPO sätts av policy (högst 15 minuters driftstopp och nästan noll dataförlust för inlämnade deklarationer), och failover repeteras kvartalsvis. Under extrem belastning fälls icke kritiska funktioner (statuspaneler, historiska uppslag) först så att deklarationsinlämning, den rättsligt väsentliga vägen, förblir tillgänglig.

## Affärsnytta: motiv, ROI och TCO

Skalbarhet, prestanda och motståndskraft är klassiska fall där kostnaden för misslyckande vida överstiger kostnaden för förebyggande. Men förebyggandet syns i budgeten och misslyckandet är bara potentiellt, vilket är därför de kroniskt underfinansieras tills den första katastrofen. Införandekostnaden är verklig: redundant infrastruktur, multiregionkapacitet, belastningstest- och kaosverktyg och ingenjörstiden att bygga tillståndslöshet och motståndskraftsmönster. Kostnaden för att *inte* investera är ett uppmärksammat avbrott under toppefterfrågan: förlorade intäkter per minut för handel, missade lagstadgade skyldigheter och offentlig utredning för myndigheter, viten enligt [servicenivåavtal](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) och bestående anseendeskada.

Rama in ärendet inför ledningen med tal verksamheten redan förstår. Uppskatta kostnaden för en timmes driftstopp under topp (förlorade transaktioner, viten, åtgärd, anseende) och jämför den med årskostnaden för den redundans och testning som förhindrar det. För kritiska system är förebyggandet nästan alltid en bråkdel av en enda större incident. Knyt RTO och RPO till uttryckliga pengar: hur mycket intäkt eller hur många transaktioner per timme av driftstopp, och hur mycket dataförlust som är rättsligt eller kommersiellt tolerabel. Presentera prestanda som en intäkts- och nöjdhetsspak, eftersom snabbare system konverterar bättre och kostar mindre per transaktion, och presentera motståndskraft som en försäkring vars premie är liten i förhållande till den täckta förlusten. Det starkaste argumentet är att dessa kvaliteter är billiga att designa in och förödande att eftermontera efter avbrottet som tvingar fram frågan.

## Antimönster och fallgropar

- **Klistriga sessioner och tillstånd i instansen.** Att lagra sessionstillstånd på servern, vilket förhindrar fri horisontell skalning och säker ersättning av instanser.
- **Autoskalning som kapacitetsplanering.** Att anta att autoskalning kommer att absorbera en känd stegändringstopp den är för långsam att reagera på.
- **Att köra varm utan utrymme.** Att drifta nära 100 % utnyttjande och lämna inget att absorbera toppar eller fel.
- **Att optimera utan att profilera.** Att justera kod som inte är flaskhalsen medan den verkliga förblir orörd.
- **Att ignorera svansen.** Att rapportera medellatens medan p99-användare lider. Medelvärden döljer smärtan i skala.
- **Otestad katastrofåterställning.** En DR-plan och säkerhetskopior som aldrig övats och som kommer att fallera när de behövs.
- **Enskilda felpunkter.** En lastbalanserare, en databasprimär, en region: en oredundant komponent som tar ner allt.
- **Kaosteknik utan skyddsräcken.** Att injicera fel utan kontroll över sprängradien eller en avbrottsbrytare, vilket orsakar just det avbrott du ville förhindra.

## Mognadsmodell

- **Nivå 1: Initiera.** Ad hoc och reaktivt. Enkelinstans eller vertikalt skalat, med tillstånd hållet på servern. Ingen belastningstestning, inga prestandabudgetar och ingen katastrofåterställning utöver enstaka säkerhetskopior ingen har återställt från. Varje komponentfel orsakar ett fullt avbrott, och skalningsproblem upptäcks i produktion.
- **Nivå 2: Utveckla.** Grundläggande praxis dyker upp men varierar med team. Vissa tjänster är horisontellt skalade och tillståndslösa bakom en lastbalanserare, med grundläggande autoskalning på några. Belastningstestning sker före stora lanseringar men inte rutinmässigt, och säkerhetskopior finns medan katastrofåterställning är dokumenterad men sällan övad. Vad ett team gör väl har ett annat inte börjat med.
- **Nivå 3: Standardisera.** Praxis är dokumenterad och upprätthålls i hela organisationen. Kapacitet planeras för kända toppar med utrymme, prestandabudgetar upprätthålls i CI så att regressioner fäller bygget, och motståndskraftsmönster (tidsgränser, begränsade omförsök, kretsbrytare, skott) plus graciös nedgradering är standardvalet. RTO och RPO definieras per system, redundansnivåer tilldelas efter kritikalitet och failover för katastrofåterställning testas regelbundet i alla team.
- **Nivå 4: Hantera.** Kvaliteterna mäts och styrs mot utgångslägen. Team följer p95- och p99-latens, felbudgetar samt utnyttjande och utrymme mot prognos, och larmar på brott snarare än att upptäcka dem vid lansering. Testade failovertider jämförs med mål-RTO och RPO, trösklar för nedgradering och lastfällning valideras med mått och beslut att gå eller inte gå vidare om releaser och kapacitet drivs av data. Där tal driver från utgångsläget är gapet synligt och ägt snarare än gömt bakom medelvärden.
- **Nivå 5: Orkestrera.** Skalbarhet, prestanda och motståndskraft förbättras kontinuerligt och är integrerade i hela organisationen. Aktiv-aktiv multiregion används varhelst kritikalitet motiverar det, kaosteknik körs kontinuerligt inklusive produktionsspelövningar och kapacitetsprognostisering matar direkt planering och upphandling. Motståndskraft valideras löpande, återställningsmål möts och bevisas konsekvent och arkitekturen anpassas när belastningsmönster och riskbilden förskjuts, knuten till verksamhetskontinuitets- och riskplanering.

## Idéer för diskussion

1. Vilka av era tjänster håller fortfarande tillstånd på instansen, och vad hindrar er från att göra dem tillståndslösa?
2. Vilka är RTO och RPO för ert mest kritiska system, vem satte dem och när bevisade ni senast att ni kan möta dem?
3. Skyddar autoskalning er faktiskt mot er största kända topp, eller förlitar ni er på att den gör något den inte kan?
4. Var är er återstående enskilda felpunkt, och vad är planen att ta bort den?
5. Mäter och budgeterar ni p99-latens, eller gömmer ni er bakom medelvärden?
6. Har ni någonsin medvetet fällt en komponent i produktion? Om inte, hur vet ni att er motståndskraft fungerar?

## Viktigaste punkter

- Skilj prestanda, skalbarhet och motståndskraft åt. Ett stort system behöver alla tre, utformade in från början.
- Horisontell skalning och tillståndslösa tjänster är grunden för skala, tillgänglighet i drift och säker driftsättning.
- Kombinera autoskalning med verklig kapacitetsplanering och utrymme för förutsägbara, affärskritiska toppar.
- Driv prestanda med profilering och belastningstestning mot uttryckliga budgetar, med fokus på den kritiska vägen och svansen.
- Bygg motståndskraft med tidsgränser, kretsbrytare, skott, graciös nedgradering och redundans, och validera den sedan med kaosteknik.
- Sätt RTO och RPO som affärsbeslut, konstruera DR i linje med varje systems kritikalitet och testa failover regelbundet.

## Referenser och vidare läsning

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
