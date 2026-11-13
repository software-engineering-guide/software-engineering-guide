# 7.8 Datakvalitet och observerbarhet

## Översikt och motivation

[Datakvalitet](https://en.wikipedia.org/wiki/Data_quality) är lämplighet för användning: i vilken grad data tjänar de beslut, produkter och rapporter som beror på den. En datamängd är inte god eller dålig i abstrakt mening. Den är tillräckligt god för ett ändamål, eller så är den inte det. En kundadress som duger för ett marknadsföringsantal kan vara olämplig för ett juridiskt meddelande. Den inramningen spelar roll, eftersom den flyttar samtalet från "är vår data perfekt" (aldrig) till "är vår data lämplig för det vi är på väg att göra med den" (möjligt att besvara, och testbart). De klassiska dimensionerna är noggrannhet, fullständighet, konsekvens, aktualitet, giltighet och unikhet, och de flesta verkliga problem kan föras tillbaka till någon av dem.

Här är den obekväma sanningen för stora team: dålig data är värre än ingen data. När du inte har någon data vet du det och går vidare med lämplig försiktighet. När du har felaktig data som ser rätt ut agerar du på den med falsk tillförsikt. Dålig data korrumperar tyst. Den flödar in i en panel som en chef litar på, in i en [maskininlärnings](https://en.wikipedia.org/wiki/Machine_learning)modell som tränar på den och kodar dess fel och in i beslut som ingen tänker ifrågasätta eftersom talet stod där på skärmen. Skadan är diffus och fördröjd, vilket är precis varför den är dyr. När någon märker det har det felaktiga talet redan citerats i en styrelsepresentation, en regulatorisk inlämning eller en offentlig statistik.

Dataobserverbarhet är disciplinen som fångar detta innan dina konsumenter gör det. Den är den direkta motsvarigheten till programvaruobserverbarhet och telemetri (kapitel 9.2): samma instinkt som säger dig att övervaka svarstid och felfrekvens säger dig att övervaka datans färskhet, volym, schema och fördelning. Det här kapitlet bygger på datastrategi och datastyrning (kapitel 7.1) och datateknik (kapitel 7.2), och det matar datamodellering och det semantiska lagret (kapitel 7.7) och ansvarsfull och pålitlig AI (kapitel 6.5). För företag som avstämmer många källsystem och för myndigheter som publicerar lagstadgad statistik är det att behandla datatillförlitlighet som ett ingenjörsproblem med ägare och servicenivåer skillnaden mellan förtroende och en mycket offentlig rättelse.

## Nyckelprinciper

- Datakvalitet är lämplighet för användning, inte perfektion. Definiera den mot ändamålet.
- Dålig data är värre än ingen data, eftersom den korrumperar beslut tyst.
- Testa data som du testar kod: påståenden, förväntningar och schemakontroller i pipelinen.
- Kontrakt mellan producenter och konsumenter gör förväntningar uttryckliga och möjliga att upprätthålla.
- Observera färskhet, volym, schema och fördelning på samma sätt som du observerar tjänster.
- Ursprung förvandlar "något är fel" till "här är vad som gick sönder och vad det påverkar".
- Behandla dataincidenter som produktionsincidenter, med ägarskap, allvarlighetsgrad och servicenivåer.
- Upptäck problem där de kommer in, inte tre lager nedströms i en panel.

## Rekommendationer

### Definiera kvalitet per dimension och mät den

Vaga kvalitetsmål ger vaga resultat. Bryt ner kvalitet i mätbara dimensioner och fäst konkreta kontroller vid var och en. Noggrannhet frågar om värden speglar verkligheten (stämmer den registrerade intäkten med källreskontran). Fullständighet frågar om förväntade poster och fält finns (saknas några dagar, är obligatoriska kolumner tomma). Konsekvens frågar om samma faktum stämmer överens mellan system (stämmer kundantalet i ekonomi med antalet i datalagret). Aktualitet frågar om data anländer i tid för att vara användbar (är gårdagens data klar före morgonrapporten). Giltighet frågar om värden följer regler och format (är alla valutakoder verkliga, ligger datum inom intervallet). Unikhet frågar om entiteter förekommer en gång (finns det dubblettordrar som blåser upp totalen). Välj de dimensioner som spelar roll för varje datamängd, sätt trösklar och följ dem över tid. Kvalitet du inte mäter är kvalitet du gissar om.

### Testa pipelines med påståenden och förväntningar

Data förtjänar samma teststringens som applikationskod. Använd [datavalidering](https://en.wikipedia.org/wiki/Data_validation) i varje steg: påståendebaserade tester som fäller pipelinen när en invariant bryts och förväntansbaserade tester som deklarerar hur "normalt" ser ut för en tabell och flaggar avvikelser. Hävda att primärnycklar är unika och icke-tomma, att främmande nycklar löses upp, att kategoriska kolumner bara innehåller godkända värden, att numeriska kolumner håller sig inom rimliga intervall och att radantal landar i ett förväntat band. Lägg till schemakontroller som fallerar högljutt när en kolumn läggs till, tas bort, döps om eller byter typ uppströms. Kör dessa kontroller i kontinuerlig integration så att en dålig transformation fångas före sammanslagning, och kör dem igen i produktion mot levande data så att en dålig källa fångas innan den når konsumenter. Målet är att fallera tidigt och högljutt, eftersom en trasig pipeline är säkrare än en tyst felaktig.

### Etablera datakontrakt mellan producenter och konsumenter

De flesta datakvalitetsincidenter börjar uppströms, när ett producerande team ändrar ett schema, en semantisk betydelse eller en värdekonvention utan att veta vem som beror på det. Ett [datakontrakt](https://en.wikipedia.org/wiki/Data_contract) rättar till detta genom att göra gränssnittet uttryckligt: schemat, semantiken hos varje fält, tillåtna värden, färskhetsgarantier och processen för att göra en ändring. Producenten förbinder sig till kontraktet, konsumenten bygger mot det och en brytande ändring kräver versionering och varsel snarare än en tyst överraskning på måndagen. Upprätthåll kontrakt mekaniskt där ni kan, genom att validera inkommande data mot kontraktet vid gränsen och avvisa eller sätta överträdelser i karantän. Kontrakt förvandlar ett implicit, skört beroende till ett uttryckligt, förhandlat. De gör också ägarskap synligt, vilket är halva striden i skala.

### Övervaka de fyra signalerna för dataobserverbarhet

Dataobserverbarhet bevakar fyra signaler, i direkt parallell med hur du bevakar en körande tjänst (kapitel 9.2). Färskhet: är datan så aktuell den ska vara, eller har pipelinen stannat. Volym: ligger radantalet i det förväntade intervallet, eller anlände en tabell halvtom eller dubbelladdad. Schema: har strukturen ändrats oväntat. Fördelning: har själva värdena driftat, så att en kolumn som var 2 procent tom plötsligt är 40 procent tom, eller ett medelvärde har skiftat på ett sätt som signalerar en uppströmsbugg. Instrumentera dessa signaler på dina viktiga tabeller, lär dig deras normala mönster och larma vid brott. Så ersätter du "en chef märkte att panelen såg fel ut" med "det ägande teamet fick larm vid felpunkten". Den sämsta tänkbara detektorn av ett dataproblem är en människa nedströms som litar på talet.

### Lägg till avvikelsedetektering, men justera den mot larmtrötthet

Statiska trösklar fångar de uppenbara felen. För subtilare drift, lägg ovanpå [avvikelsedetektering](https://en.wikipedia.org/wiki/Anomaly_detection) som lär sig varje måtts normala säsongsmönster och flaggar statistiskt ovanliga avvikelser, så att du fångar ett långsamt läckage innan det blir en flod. Var disciplinerad med detta. Bullriga avvikelselarm lär människor att ignorera larm, vilket är värre än inga larm. Börja med dina mest värdefulla tabeller, larma bara på sådant en människa bör agera på, dirigera varje larm till en namngiven ägare och justera skoningslöst. Ett larm ingen agerar på är en bugg i din övervakning, inte en funktion.

### Spåra ursprung för konsekvensanalys och rotorsak

När något går sönder spelar två frågor omedelbart roll: vad orsakade det och vad påverkar det. [Dataursprung](https://en.wikipedia.org/wiki/Data_lineage) besvarar båda genom att kartlägga hur data flödar från källa genom varje transformation till varje nedströms tabell, panel och modell. För rotorsak spårar du en felaktig siffra uppströms till den transformation eller källa som införde den. För konsekvensanalys spårar du framåt för att se varje konsument som berörts av en dålig laddning, så att du kan underrätta dem och sätta skadan i karantän innan den sprider sig. Fånga ursprung automatiskt från dina transformations- och orkestreringsverktyg i stället för att underhålla ett diagram för hand, eftersom ett handritat diagram är fel dagen efter att du ritat det. I företag med många källor, publicera ursprung i en datakatalog så att vilken konsument som helst kan se var ett fält kom ifrån och lita på det i enlighet därmed.

### Behandla dataincidenter som produktionsincidenter

De praxis som håller tjänster pålitliga gäller direkt för data. Ge varje viktig datamängd en ägare. Definiera allvarlighetsnivåer för "dataavbrott", de perioder då data saknas, är felaktig eller sen. Sätt servicenivåer: färskhetsmål, en acceptabel felbudget och en måltid för upptäckt och lösning. Sätt datajourrotationer bakom de mest kritiska pipelines, skriv körböcker och håll skuldfria efterhandsgranskningar efter incidenter så att samma fel inte upprepas. När en betalningstabell är sen eller ett offentligt mått är fel är det en incident, och den förtjänar samma allvar som ett avbrott. Detta är det kulturella skifte som får alla verktyg att löna sig.

### Profilera och stäm av kontinuerligt

Profilering betyder att rutinmässigt undersöka din datas form: värdefördelningar, andel tomma värden, kardinalitet, min och max och formatmönster. Den lyfter fram problem du inte tänkte hävda och talar om hur "normalt" ser ut så att du kan sätta goda förväntningar. Avstämning betyder att kontrollera att oberoende källor stämmer överens: stämmer datalagrets total med källsystemet där sanningen finns, är summan av delarna lika med helheten. Automatisera avstämning mellan kritiska system och larma vid divergens, eftersom ett avstämningsbrott ofta är den tidigaste och tydligaste signalen om att något gick fel uppströms.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar | Bäst passform |
|---|---|---|---|
| Påståendetester (hårt fel) | Stoppar dålig data kallt, tydliga invarianter | Kan blockera pipelines för mindre problem | Kritiska nycklar, referensintegritet |
| Förväntanstester (mjuk flagga) | Fångar drift, mindre skört | Behöver justeras, kan ignoreras | Fördelningar, volymband |
| Datakontrakt | Förhindrar uppströmsöverraskningar, tydligt ägarskap | Samordnings- och styrningsoverhead | Gränser mellan producenter och konsumenter över team |
| Avvikelsedetektering | Fångar subtil, oförutsedd drift | Larmtrötthet, falska positiva | Mycket värdefulla tabeller, säsongsmått |
| Manuella stickprov | Billigt att börja, inga verktyg | Skalar inte, missar tysta fel | Endast mycket tidigt skede |
| Fullständig observerbarhetsplattform | Bred täckning, ursprung, larmning | Kostnad, uppsättning, ännu ett system att driva | Många källor, reglerad rapportering |

Den centrala spänningen är täckning mot brus. Instrumentera ingenting och problem når era konsumenter först, vilket förstör förtroende. Instrumentera allt med hårfina larm och ni dränker ert team i falska positiva tills de stänger av kanalen, vilket också låter problem nå konsumenter. Lös detta genom att rangordna din data efter sprängradie. De tabeller som matar styrelsemått, kundvända produkter, regulatoriska rapporter och maskininlärningsmodeller får full behandling: kontrakt, hårda påståenden, observerbarhet och jourägarskap. Den långa svansen av utforskande tabeller får lättviktig profilering. Spendera din tillförlitlighetsbudget där felaktig data skulle skada mest och var medvetet sparsam överallt annars.

## Frågor att diskutera med ditt team

1. **När dålig data når produktion, vem får veta det först, och hur?** Detta är den mest avslöjande frågan om er datatillförlitlighet, eftersom det ärliga svaret vanligen är "en konsument, av en slump". Om en analytiker, en chef eller en kund är ert detekteringssystem mäts er genomsnittliga tid till upptäckt i dagar och er trovärdighet tar smällen varje gång. Alternativet är instrumentering som larmar det ägande teamet vid felpunkten, innan det felaktiga talet sprider sig. Ta med verkliga tal: hur många av era tio senaste dataincidenter fångades av övervakning mot rapporterades av en människa nedströms, och hur länge låg var och en oupptäckt. Svaret talar om för er om ni har observerbarhet eller bara hopp, och det bör direkt styra var ni först investerar i färskhets-, volym-, schema- och fördelningskontroller.

2. **Vilka datamängder har en ägare, ett kontrakt och en servicenivå, och vilka är föräldralösa?** I skala kan de flesta datakvalitetsfel spåras tillbaka till ett ägarlöst gränssnitt: ett producerande team ändrade något utan att veta vem som berodde på det, eftersom inget kontrakt sade det. Ägarskap är grunden som gör kontrakt, larmvägar och incidentsvar möjliga, och föräldralösa datamängder är där tyst korruption bor. Gå igenom era viktigaste tabeller och fråga för var och en vem som är ansvarig, vad producenten har förbundit sig till och vilken färskhet och noggrannhet konsumenterna är lovade. Ta med ert ursprung: tabellerna med störst sprängradie nedströms är de som mest behöver detta och är ofta de som saknar det. Gapet mellan "viktig" och "ägd" är er prioriteringslista för nästa kvartal.

3. **Vad är den faktiska kostnaden för en datakvalitetsincident för oss, och behandlar vi den därefter?** Team underinvesterar i datakvalitet eftersom kostnaden för dålig data är diffus och fördröjd, så den dyker aldrig upp som en radpost, medan kostnaden för att bygga kvalitetsverktyg är konkret och omedelbar. Ramma om det genom att prissätta en verklig incident från början till slut: det felaktiga beslutet, omarbetet, ingenjörstimmarna som spenderades på att spåra rotorsak utan ursprung, det urholkade förtroendet som får människor att i tysthet bygga sina egna skuggdatamängder och, i reglerade eller publika sammanhang, rättelsemeddelandet och dess anseendeskada. Ta med ett specifikt exempel från senaste året och summera det ärligt. Om ett enda tyst fel i en betalnings- eller offentlig statistikpipeline kunde kosta mer än ett års observerbarhetsverktyg gör affärsärendet sig självt, och samtalet skiftar från om ni ska investera till var.

4. **Har vi rangordnat våra datamängder efter sprängradie, och följer vår övervakningsinvestering faktiskt den rangordningen?** Det centrala felmönstret i skala är att fördela tillförlitlighetsinsatsen jämnt, så att den utforskande tabell ingen litar på får samma uppmärksamhet som den som matar styrelsemått, medan ett hårfint larm på en tabell med lågt värde lär människor stänga av den kanal som också bär det kritiska larmet. Ni kan inte instrumentera allt utan att drunkna i brus, och ni kan inte instrumentera ingenting utan att låta problem nå konsumenter först, så det verkliga beslutet är var den fulla behandlingen (kontrakt, hårda påståenden, observerbarhet och jourägarskap) hamnar och var lättviktig profilering räcker. Ta med en inventering av era tabeller märkta med vad som beror på dem: styrelsemått, kundvända produkter, regulatoriska rapporter och maskininlärningsmodeller, och jämför sedan den rangordningen mot var era kontroller och larm faktiskt sitter i dag. För ett företag som avstämmer många källor eller en myndighet som publicerar lagstadgade siffror hör tabeller med rättslig eller offentlig exponering hemma högst upp på listan, och varje gap mellan "skulle skada mest om fel" och "är mest övervakad" är ett prioriteringsfel att rätta nu.

5. **Vilka maskininlärningsmodeller och analyser fattar beslut på data vi aldrig validerar, och vilka fel kan de i tysthet koda?** En panel visar ett felaktigt tal för en människa som kanske ifrågasätter det, men en modell tränar på felaktiga features och kodar de felen i varje förutsägelse den gör, i en skala och med en ogenomskinlighet som gör skadan långt svårare att upptäcka eller ångra. Det konkurrerande trycket är hastighet: datavetenskapsteam vill röra sig fort på nya features, och att lägga till validering, kontrakt och färskhetsgarantier på varje flöde känns som friktion tills en modell i tysthet försämras för att en uppströmskolumn driftade. Ta med en inventering av era produktionsmodeller och analyser, de datamängder var och en konsumerar och en ärlig markering av vilka av de flödena som har tester, kontrakt och observerbarhet mot vilka som är oskyddade. I ett företags- eller myndighetssammanhang där en modell påverkar kredit-, förmåns- eller tillsynsbeslut blir ovaliderad träningsdata en revisions- och rättviseskuld utöver en kvalitetsrisk, så frågan om vilka flöden som grindar en modellrelease bör ha en ägare och ett dokumenterat svar (kapitel 6.5).

6. **När en kvalitetsbugg dyker upp veckor i efterhand, kan vi faktiskt bearbeta om och stämma av, eller har vi redan kastat det vi skulle behöva?** Många kvalitetsfel är osynliga vid laddningstillfället och blir tydliga först senare, när ett avstämningsbrott eller en misstänkt trend får någon att titta, och då beror förmågan att rätta det rent på val ni gjorde mycket tidigare: om ni behöll oföränderliga råa poster, om oberoende källor kan stämmas av och om ursprung låter er spåra den felaktiga siffran till dess upprinnelse. Spänningen är kostnad och enkelhet mot reproducerbarhet, eftersom att bevara rådata och köra kontinuerlig avstämning mellan system inte är gratis, och det är frestande att radera råa indata när de transformerade tabellerna ser rätt ut. Ta med er policy för lagring och oföränderlighet av rådata, listan över kritiska systempar ni stämmer av automatiskt och ett verkligt exempel på en bugg ni antingen kunde eller inte kunde bearbeta er ur. För en myndighet under en lagstadgad skyldighet att spåra vilket publicerat tal som helst tillbaka till källposter, eller ett företag inför en regulatorisk omräkning, är oföränderlig rådata och automatisk avstämning inte valfri hygien utan mekanismen som gör en rättelse försvarbar.

## Sektorsperspektiv

**Startup.** Hastighet och förtroende spelar större roll än täckning. Lägg en handfull lättviktiga tester i ditt transformationsverktyg (unikhet och icke-tomma på nycklar, godkända värden på de kolumner som bär betydelse, ett radantalsband per källa) och lägg till färskhets- och volymövervakning bara på de få tabeller som matar företagets mått. Dirigera varje larm till en kanal som en ingenjör äger och stå emot att köpa en observerbarhetsplattform innan du har tabellerna eller teamet som motiverar den. Målet är att märka ett felmärkt fält innan det blåser upp ett tal grundarna citerar, inte att instrumentera allt.

**Småföretag.** Utan dataingenjör och med snäv budget, lita på de kvalitetsfunktioner som redan är inbyggda i datalagret, BI-verktyget eller SaaS-plattformarna du betalar för i stället för att sätta upp en separat stack. Fokusera din insats på de handfull tal som faktiskt driver beslut (intäkt, pipeline, lager), kontrollera dem mot en oberoende källa med jämna mellanrum och behandla en leverantörs färskhets- och schemalarm som tillräckligt bra när de finns. Att köpa kvalitet inbäddad i verktyg du redan kör slår att bygga en pipeline du inte har någon att underhålla.

**Storföretag.** Problemet är tillförlitlighet över många team och tusentals tabeller, så standardisera gränssnittet: datakontrakt vid varje producentgräns, en observerbarhetsplattform som bevakar färskhet, volym, schema och fördelning och ursprung publicerat i en katalog för konsekvensanalys. Rangordna datamängder efter sprängradie, sätt avvikelsedetektering och jourägarskap på de värdefulla och kör dataincidenter genom samma allvarlighets- och efterhandsgranskningsprocess som tjänsteavbrott. Servicenivåer på de pipelines som matar regulatoriska rapporter och chefspaneler förvandlar datatillförlitlighet från en ambition till ett uppmätt, styrt åtagande.

**Offentlig sektor.** Lagstadgad noggrannhet och offentlig ansvarsskyldighet sätter ribban: landa oföränderliga råa enkät- och administrativa poster, transformera dem i lagerindelade, testade steg och stäm av mot källtotaler i varje steg. Behåll fullständigt ursprung så att vilken publicerad siffra som helst kan spåras till källposter för revision och grinda varje release bakom validering av giltighet, fullständighet och konsekvens mot tidigare perioder. Upphandling av verktyg bör kräva transparens och dataportabilitet, och en felaktig offentlig statistik måste hanteras som en allvarlig incident, med den tyngd som allmänhetens förtroende för officiella siffror kräver.

## Exempel

**Startup.** Ett företag på tjugo personer driver sin go-to-market på ett datalager matat av produkthändelser och en betalningsleverantör. Tidigt blåste ett felmärkt valutafält i tysthet upp rapporterade intäkter i två veckor innan någon märkte det, vilket skakade teamets förtroende för varje panel. De svarade med en lättviktig uppsättning tester i sitt transformationsverktyg: unikhet och icke-tomma på nycklar, kontroller av godkända värden på valuta- och statuskolumner och ett radantalsband per källa. De lade till grundläggande färskhets- och volymövervakning på de få tabeller som matar företagets mått, dirigerat till en enda Slack-kanal som en ingenjör äger. Det är blygsamt, men det fångar de fel som spelar roll, och grundarna litar på talen igen.

**Storföretag.** En multinationell bank avstämmer kund- och transaktionsdata över dussintals källsystem till ett styrt datalager som matar regulatoriska rapporter, riskmodeller och chefspaneler. Den kör datakontrakt vid varje producentgräns, så en uppströms schemaändring versioneras och förhandlas i stället för att släppas över konsumenter. En observerbarhetsplattform övervakar färskhet, volym, schema och fördelning över tusentals tabeller, med avvikelsedetektering på de värdefulla och ursprung publicerat i en datakatalog för konsekvensanalys. Dataincidenter följer samma allvarlighets- och jourprocess som tjänsteavbrott, med servicenivåer på de pipelines som matar regulatoriska inlämningar. När ett källsystem driftar får det ägande teamet larm och de påverkade nedströmsrapporterna är kända inom minuter, inte upptäckta av en tillsynsmyndighet.

**Offentlig sektor.** En nationell statistikmyndighet publicerar ekonomiska indikatorer som marknader, beslutsfattare och allmänheten behandlar som auktoritativa, så noggrannhet är en lagstadgad skyldighet och varje publicerad siffra måste vara granskningsbar. Dess pipelines landar oföränderliga råa enkät- och administrativa poster och transformerar dem sedan i lagerindelade, testade steg med avstämning mot källtotaler i varje steg. Fullständigt ursprung låter analytiker spåra vilket publicerat tal som helst tillbaka till källposter, vilket är både ett kvalitetsverktyg och ett lagkrav. Före release passerar siffror valideringsgrindar för giltighet, fullständighet och konsekvens mot tidigare perioder, och varje avvikelse utreds och dokumenteras i stället för att publiceras. En felaktig offentlig statistik är en allvarlig incident, så myndigheten behandlar dataavbrott med den tyngd som allmänhetens förtroende kräver.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på datakvalitet och observerbarhet kommer av bevarat förtroende, förkortade incidenter och undvikna dåliga beslut. Pålitlig data är grunden som får varje nedströms investering i analys, business intelligence och AI att faktiskt löna sig, eftersom en modell eller panel bara är så god som datan under den. När kvalitetskontroller fångar en dålig laddning vid gränsen undviker ni den långt större kostnaden av att ett felaktigt tal når ett beslut, en kund eller en inlämning. Ursprung kollapsar rotorsaksutredning från dagars manuell spårning till minuter, vilket är ren återvunnen ingenjörstid. Observerbarhet krymper genomsnittlig tid till upptäckt från "när en konsument klagar" till "när pipelinen fallerar", vilket är där det mesta av förtroendeskadan undviks.

Den totala ägandekostnaden inkluderar verktyg för testning, observerbarhet och katalogisering, plus ingenjörstiden för att instrumentera pipelines och det organisatoriska arbetet att tilldela ägare och skriva kontrakt. Detta är verkligt, men väg det mot kostnaden för att inte göra det: tyst korruption som upptäcks av chefer, maskininlärningsmodeller tränade på dåliga features som kodar fel i skala, analytiker som i tysthet bygger om skuggdatamängder eftersom de inte längre litar på de officiella och, i reglerade eller publika sammanhang, rättelsemeddelanden som skadar trovärdigheten i åratal. Gentemot ledningen, ramma in datakvalitet som en försäkring på varje databaserat beslut organisationen fattar. Premien är måttlig och förutsägbar. Den oförsäkrade förlusten, ett enda uppmärksammat felaktigt tal, är varken det ena eller det andra.

## Antimönster och fallgropar

- Att behandla datakvalitet som ett engångsstädprojekt i stället för en löpande ingenjörspraxis.
- Att upptäcka fel från nedströmskonsumenter i stället för från övervakning vid felpunkten.
- Inget datamängdsägarskap, så ingen är ansvarig när något går sönder och ingen får larm.
- Producenter som ändrar scheman eller semantik utan kontrakt och i tysthet bryter varje konsument.
- Avvikelselarm så bullriga att teamet stänger av kanalen och missar den verkliga incidenten.
- Att mata ovaliderad data direkt in i maskininlärningsmodeller och koda fel i skala (kapitel 6.5).
- Att underhålla ursprung som ett handritat diagram som är fel dagen efter att du ritat det.
- Att jaga perfekt data överallt i stället för kvalitet lämplig för användning på de tabeller som spelar roll.
- Att radera rådata, så att du inte kan bearbeta om eller stämma av när en kvalitetsbugg dyker upp senare.

## Mognadsmodell

- **Nivå 1, Initiera:** Kvalitet är ingens jobb. Problem hittas av konsumenter, vanligen efter att ett felaktigt tal nått en rapport. Inga tester, ingen övervakning, inget ägarskap. Rättelser är manuell brandbekämpning, och samma fel återkommer.
- **Nivå 2, Utveckla:** Vissa team lägger till grundläggande tester på sina kritiska tabeller (nycklar, nollvärden, godkända värden) och lite färskhets- och volymövervakning på de datamängder de bryr sig mest om. Praxisen fungerar där den finns, men täckning och stringens varierar team för team, inget är standardiserat och incidenter hanteras fortfarande reaktivt.
- **Nivå 3, Standardisera:** Kvalitetsdimensioner är definierade med trösklar, och samma förväntningar gäller över team snarare än att bero på vem som byggde en pipeline. Datakontrakt styr viktiga producentgränser, observerbarhet täcker färskhet, volym, schema och fördelning på viktiga tabeller och ursprung stöder konsekvensanalys. Varje viktig datamängd har en namngiven ägare, och dataincidenter följer en dokumenterad allvarlighets- och svarsprocess i hela organisationen.
- **Nivå 4, Hantera:** Kvalitet och tillförlitlighet mäts och styrs mot utgångslägen. Dataavbrott följs med verkliga mått: genomsnittlig tid till upptäckt, genomsnittlig tid till lösning, färskhet och noggrannhet mot överenskomna servicenivåer och felbudgetar en datamängd kan spendera innan den utlöser åtgärd. Frekvens av avstämningsbrott, godkännandefrekvens för tester och andel falska positiva avvikelser trendas över tid, larmning justeras mot dessa tal snarare än på gissning, och beslut att gå eller inte gå på en datarelease fattas på uppmätt kvalitet mot utgångsläget snarare än på hopp.
- **Nivå 5, Orkestrera:** Kvalitet och observerbarhet är genomgripande, automatiska och adaptiva. Avvikelsedetektering fångar subtil drift, kontrakt upprätthålls mekaniskt och ursprung fångas automatiskt och publiceras i en katalog. Data har servicenivåer och jourägarskap som produktionstjänster, avstämning körs kontinuerligt och skuldfria efterhandsgranskningar matar en stadig minskning av dataavbrott. Kvalitet är integrerad med datastyrning, maskininlärning och affärsplanering, och organisationen omdefinierar kontinuerligt trösklar, täckning och ägarskap när datalandskapet skiftar.

## Idéer för diskussion

1. Vilka av era tabeller skulle orsaka mest skada om de var tyst felaktiga i en vecka, och är det de ni övervakar mest?
2. Var hade ett datakontrakt förhindrat er senaste uppströmsorsakade incident, och varför fanns det inget?
3. Hur mycket ingenjörstid tar en typisk rotorsaksutredning i dag, och hur mycket skulle automatiskt ursprung spara?
4. Tränar några av era maskininlärningsmodeller på data ni inte validerar, och vilka fel kan de koda?
5. Är er larmning tillräckligt väl justerad för att människor agerar på varje larm, eller har någon stängt av kanalen?
6. Vilka färskhets- och noggrannhetsservicenivåer skulle era viktigaste konsumenter faktiskt skriva under på, och kunde ni möta dem i dag?

## Viktigaste punkter

- Datakvalitet är lämplighet för användning över noggrannhet, fullständighet, konsekvens, aktualitet, giltighet och unikhet.
- Dålig data är värre än ingen data, eftersom den korrumperar beslut och modeller tyst.
- Testa data som kod: påstående- och förväntanstester plus schemakontroller, i CI och i produktion.
- Använd datakontrakt för att göra producenters och konsumenters förväntningar uttryckliga och möjliga att upprätthålla.
- Observera färskhet, volym, schema och fördelning, parallellt med programvaruobserverbarhet (kapitel 9.2).
- Fånga ursprung för snabb rotorsak och konsekvensanalys och publicera det för konsumenter.
- Behandla dataincidenter som produktionsincidenter, med ägarskap, allvarlighetsgrad och servicenivåer.
- Instrumentera där felaktig data skadar mest. Sikta på kvalitet lämplig för användning, inte perfektion överallt.

## Referenser och vidare läsning

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
