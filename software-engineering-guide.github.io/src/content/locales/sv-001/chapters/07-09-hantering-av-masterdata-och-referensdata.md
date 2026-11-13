# 7.9 Hantering av masterdata och referensdata

## Översikt och motivation

Fråga fem system hur många kunder organisationen har, och du får fem olika tal. Ett räknar e-postadresser, ett räknar avtal, ett räknar inloggningar och två är oeniga om huruvida "Acme Corp" och "ACME Corporation" är samma företag. [Hantering av masterdata](https://en.wikipedia.org/wiki/Master_data_management) (MDM) är disciplinen att förena de kärnentiteter din verksamhet delar, kund, produkt, leverantör, anställd, plats, till en auktoritativ version alla system kan lita på.

Börja med att sortera din data i tre slag, eftersom de behöver olika behandling. Masterdata beskriver verksamhetens substantiv: de personer, platser och ting som många processer refererar till. Referensdata är det kontrollerade ordförråd processerna använder: valutakoder, landskoder, listor över måttenheter, produktkategorier. Transaktionsdata registrerar verben: en order lagd, en betalning gjord, en leverans skickad. Master- och referensdata har lägre volym än transaktioner men refereras överallt, så ett fel i dem förorenar allt nedströms.

Kostnaden för att göra fel är konkret. När samma kund finns som fyra något olika poster skickar du fyra kataloger, du kan inte se en enda relation värd att behålla och ditt tal för intäkt per kund är i tysthet fel. En [gyllene post](https://en.wikipedia.org/wiki/Single_source_of_truth), den enda pålitliga versionen av en entitet sammansatt från många källor, är det som ersätter de motstridiga kopiorna, så att varje integration slutar lösa samma matchningsproblem på nytt.

För företag som avstämmer system ackumulerade genom årtionden av tillväxt och förvärv är MDM skillnaden mellan en sammanhängande kundbild och en permanent avstämningsskatt. För myndigheter stiger insatserna: en medborgare som förekommer som tre olika personer hos tre myndigheter kan nekas en förmån, beskattas två gånger eller tappas bort mellan avdelningar. Det här kapitlet kompletterar datastrategi och datastyrning (kapitel 7.1), som sätter ägarskap och policy, datamodellering och det semantiska lagret (kapitel 7.7), som definierar vad entiteter betyder, och datakvalitet och observerbarhet (kapitel 7.8), som håller poster rena över tid.

## Nyckelprinciper

- Sortera din data i master-, referens- och transaktionsdata. Var och en behöver olika hantering.
- En gyllene post per verklig entitet, sammansatt medvetet, inte upptäckt av en slump.
- Välj en MDM-arkitekturstil efter dina behov av kontroll och latens, inte efter mode.
- Matchning och överlevnad är affärsregler, så skriv ner dem och låt förvaltare justera dem.
- Referensdata är gemensamt ordförråd. Versionera det och publicera det som ett API.
- Styrning och förvaltning är MDM:s motor. Programvaran är bara verktyget.
- Sprid gyllene poster som händelser så att nedströmssystem hålls synkroniserade, inte inaktuella.
- Mät MDM efter förbättrade beslut och borttagna dubbletter, inte efter inlästa poster.

## Rekommendationer

### Klassificera master-, referens- och transaktionsdata först

Du kan inte hantera det du inte har sorterat, så börja med att klassificera dina datadomäner. Ett användbart test för masterdata är om ett felaktigt värde sprider sig: om en dålig adress krusar in i fakturering, leverans och juridiska meddelanden tittar du på masterdata. Det styr din investering: du bygger en matchningsmotor för kundentiteten, inte för orderrader. Namnge domänerna uttryckligen, rangordna dem efter hur mycket smärta deras duplicering orsakar och börja med den eller de två som svider mest, vanligen kund och produkt eftersom de rör intäkter direkt.

### Välj en MDM-arkitekturstil medvetet

Det finns fyra vanliga arkitekturstilar, och den rätta beror på hur mycket auktoritet du kan centralisera och hur snabbt ändringar måste spridas. Registerstilen lämnar data i källsystemen och bygger bara ett index över matchade identifierare, så den kan svara "dessa fem poster är samma kund" utan att flytta någon data. Den är billig och har låg risk, men skrivskyddad, så den kan inte rätta källorna. Konsolideringsstilen drar in kopior i en central hubb och slår ihop dem till gyllene poster för rapportering, men skickar inte tillbaka rättelser, så källorna förblir stökiga. Samexistensstilen går längre: den synkroniserar rensade värden tillbaka till källsystemen, så att källorna förbättras över tid medan de fortsätter fungera oberoende. Stilen med centraliserad eller transaktionell hubb gör MDM-hubben till själva systemet där sanningen finns, där entiteter skapas och redigeras direkt och varje annat system konsumerar från den. Det ger starkast konsekvens och kontroll, och det är svårast att anta eftersom det ändrar var arbetet sker. Många organisationer går från ett register som bevisar värde mot samexistens när förtroendet växer, och kör mer än en stil över olika domäner.

### Matcha, slå ihop och sätt överlevnadsregler uttryckligen

Hjärtat i MDM är att avgöra när två poster beskriver samma verkliga sak. Detta är [postlänkning](https://en.wikipedia.org/wiki/Record_linkage), sällan så enkelt som en exakt nyckelmatchning eftersom verklig data är full av stavfel, förkortningar och saknade fält. Deterministisk matchning använder exakta regler på valda fält (samma skatte-ID, eller samma e-post plus postnummer). Probabilistisk matchning poängsätter likhet över många fält med hjälp av [approximativ strängmatchning](https://en.wikipedia.org/wiki/Approximate_string_matching) och vikter, så att "Bob Smith, 12 Main St" och "Robert Smith, 12 Main Street" kan bedömas som en sannolik matchning över en tröskel. Att avgöra vilka poster som avser samma entitet kallas identitetsupplösning, och det driver allt från kundbilder till bedrägeriupptäckt.

När poster matchar måste du avgöra vilka värden som överlever in i den gyllene posten. Dessa överlevnadsregler är affärslogik, så gör dem uttryckliga: föredra det senaste värdet för ett telefonnummer, det mest kompletta värdet för en adress, den mest betrodda källan för ett juridiskt namn. Sätt ett tröskelband där matchningar slås ihop automatiskt, ett lägre band där de avvisas automatiskt och ett mellanband där en människa avgör, vilket är där förvaltning bor. Håll varje sammanslagning reversibel och loggad, eftersom en felaktig sammanslagning som fuserar två verkliga kunder är värre än en missad.

### Behandla referensdata som versionerat gemensamt ordförråd

Referensdata är det gemensamma ordförråd dina system talar, och ordförråd som driftar orsakar tyst felanpassning: när ett system använder ISO-landskoden "GB" och ett annat använder "UK" fallerar joins och antal divergerar. Underhåll varje referenslista på ett styrt ställe, publicera den för varje konsument och, avgörande, versionera den. Koder läggs till, avvecklas, delas och slås ihop över tid, och om du skriver över listan på plats bryter du historiska rapporter som var korrekta under de gamla koderna.

Behandla en referensdatamängd som ett API med ett kontrakt. Publicera den med ikraftträdandedatum så att en konsument kan fråga "vilka var de giltiga regionkoderna det här datumet", behåll avvecklade koder i stället för att radera dem och registrera mappningen när en kod ändrar betydelse. Föredra erkända externa standarder där de finns, som ISO:s lands- och valutakoder, eftersom standarder ger dig interoperabilitet gratis och kopplar till disciplinen om öppna standarder i kapitel 3.8.

### Modellera hierarkier och relationer, inte bara platta poster

Masterdata är inte en hög oberoende rader. Det är ett nät av relationer. En kund tillhör ett hushåll och en koncernmoder. En produkt rullar upp i en kategori och ett varumärke. Dessa hierarkier bär verklig affärsbetydelse: rulla upp försäljning efter koncernmoder och bilden ändras helt jämfört med att rulla upp efter enskilt konto. Modellera dessa relationer uttryckligen så att konsumenter traverserar dem konsekvent i stället för att varje team uppfinner sin egen uppsummering.

Se upp för fallet där en entitet behöver flera hierarkier samtidigt. En produkt kan rullas upp på ett sätt för ekonomi och ett annat för sortiment, och båda är legitima, så stöd flera namngivna hierarkier snarare än att tvinga fram ett enda sant träd. Relationer mellan domäner spelar också roll, som vilken leverantör som levererar vilken produkt.

### Koppla gyllene poster till det semantiska lagret och datakvaliteten

De gyllene poster MDM producerar är de pålitliga entiteter som det semantiska lagret i kapitel 7.7 refererar till när det definierar mått: "aktiva kunder" betyder något bara när "kund" är entydig. Mata dina gyllene poster in i det semantiska lagret så att varje mått räknar samma deduplicerade, upplösta entiteter.

MDM och datakvalitet (kapitel 7.8) är två sidor av samma mynt: kvalitetskontroller upptäcker de dubbletter, nollvärden och formatöverträdelser som MDM sedan löser, och MDM:s matchning lyfter fram kvalitetsproblem kontrollerna missade. Kör kontinuerlig kvalitetsövervakning specifikt på din masterdata: dubblettfrekvenser, fördelningar av matchningssäkerhet, fullständighet i nyckelfält och granskningsköns storlek, så att drift visar sig innan konsumenter ser den.

### Sprid gyllene poster genom händelser

En gyllene post som inget nedströmssystem ser hjälper ingen. Det starkaste mönstret är händelsedriven spridning: när en entitet skapas, slås ihop eller rättas publicerar MDM-hubben en ändringshändelse, och prenumererande system uppdaterar sin lokala kopia. Detta bygger på [händelsedriven arkitektur](https://en.wikipedia.org/wiki/Event-driven_architecture) och strömningsmönstren i kapitel 7.2 och håller dussintals system konsekventa utan sköra nattliga batchsynkroniseringar som lämnar alla en dag inaktuella.

Publicera händelserna med tillräckligt sammanhang för att vara användbara: entitetsidentifieraren, vad som ändrades, de nya överlevande värdena och en version så att konsumenter kan ordna uppdateringar och upptäcka sådana de missat. Gör konsumenter idempotenta så att en omspelad händelse inte gör någon skada och erbjud ett API för system som inte kan prenumerera. Principen från dataarkitektur och lagring (kapitel 3.4) gäller: designa för att den gyllene posten ska flöda, eftersom en som ingen konsumerar bara är ett dyrt kalkylblad.

### Tilldela förvaltning och styrning före verktyg

MDM fallerar som ett teknikprojekt och lyckas som ett styrningsprojekt. Den kritiska rollen är [dataförvaltaren](https://en.wikipedia.org/wiki/Data_steward), en person ansvarig för kvaliteten och reglerna i en specifik domän, som löser tvetydiga matchningar, justerar överlevnadsregler och skiljer när två avdelningar är oeniga om vad "leverantör" betyder. Förvaltare är vanligen affärsmänniskor med djup domänkunskap, inte ingenjörer, och de behöver verklig befogenhet och avsatt tid, eftersom deltidsförvaltning utan mandat producerar precis den drift MDM var tänkt att stoppa.

Omge förvaltarna med de styrningsstrukturer från kapitel 7.1: en dataägare ansvarig för varje domän, ett råd för att avgöra tvister mellan domäner och tydliga policyer för vem som får skapa eller slå ihop masterposter. Dokumentera besluten, eftersom reglerna för att matcha en kund är institutionell kunskap som måste överleva personalomsättning. Verktygen tjänar styrningen. Att köpa en MDM-plattform innan du namngivit dina förvaltare är att köpa en motor utan förare.

## Avvägningar: för- och nackdelar

| MDM-stil | Fördelar | Nackdelar |
|---|---|---|
| Register (endast index) | Billig, låg risk, källor orörda | Skrivskyddad. Kan inte rätta källdata |
| Konsolidering (centrala kopior) | Rena poster för analys snabbt | Källor förblir stökiga. Ingen återskrivning |
| Samexistens (synk tillbaka till källor) | Källor förbättras. Balanserad kontroll | Mer integration. Synkkonflikter att hantera |
| Centraliserad / transaktionell hubb | Starkaste konsekvens och kontroll | Högst kostnad. Ändrar var arbetet sker |
| Deterministisk matchning | Förutsägbar, förklarbar, granskningsbar | Missar stavfel, varianter och stökig data |
| Probabilistisk matchning | Fångar verklig variation | Behöver justeras. Falska sammanslagningar om slarvig |

Den centrala spänningen i MDM är kontroll mot störning. De stilar som ger dig den renaste, mest konsekventa datan (samexistens och centraliserade hubbar) är precis de som mest tränger in på hur källsystem och deras ägare arbetar, och det intrånget är där MDM-program stannar av. Den pragmatiska vägen är att förtjäna förtroende med en lågriskstil och röra sig mot starkare kontroll bara där affärsärendet är tydligt. Matchningsavvägningen löper parallellt: deterministiska regler är granskningsbara men sköra, probabilistisk poängsättning är kraftfull men kräver förvaltning och en tolerans för den enstaka felaktiga sammanslagningen. De flesta mogna program blandar båda.

## Frågor att diskutera med ditt team

1. **Vilka masterdatadomäner orsakar oss faktiskt smärta, och har vi rangordnat dem efter kostnad i stället för att ta alla på en gång?** Många MDM-program kollapsar under sin egen ambition, försöker bemästra varje entitet i företaget på en gång och levererar ingenting på två år. Det produktiva draget är att hitta den eller de två domäner där duplicering och konflikt kostar er verkliga pengar eller förtroende, vanligen kund eller produkt, och att kvantifiera den kostnaden: de bortkastade utskicken, avstämningstimmarna, de felaktiga intäktstalen, revisionsanmärkningarna. Ta med konkreta exempel på samma entitet som förekommer på flera sätt över era system och låt den rangordningen tala om var ni ska börja, eftersom en snäv, mätbar vinst bygger den trovärdighet ni behöver för att expandera.

2. **Vem äger varje masterdatadomän, och har våra förvaltare befogenhet och tid att faktiskt göra jobbet?** MDM-verktyg utan bemyndigad förvaltning är en bil utan förare, och det vanligaste felmönstret är att namnge en förvaltare på en bild medan man ger dem inget verkligt mandat och inga avsatta timmar. De som löser tvetydiga matchningar och avgör tvister om "vad räknas som en kund" behöver domänexpertis, beslutsbefogenhet och skyddad tid. Ta med ert organisationsschema och fråga för er främsta domän exakt vem som avgör när två poster är samma person och vem som skiljer när försäljning och ekonomi är oeniga. Om ni inte kan namnge den personen och peka på deras avsatta tid har ni hittat det gap som kommer att sänka programmet.

3. **När vi slår ihop två poster till en gyllene post, kan vi förklara och vända beslutet, och var kommer de överlevande värdena från?** Överlevnadsregler är affärslogik som de flesta team aldrig har skrivit ner, vilket betyder att sammanslagningar sker av en slump av laddningsordning eller verktygsstandarder, och en felaktig sammanslagning som fuserar två verkliga kunder är smärtsam att reda ut. Ta med en verklig sammanslagen post och spåra varje överlevande fält tillbaka till dess källa och regel: varför den här adressen, varför det här namnet, varför det här telefonnumret. Bekräfta att varje sammanslagning är loggad och reversibel och att ett mellanband av osäkra matchningar går till en människa i stället för att slås ihop automatiskt. Om ni inte kan förklara en specifik gyllene post kan era förvaltare inte försvara den inför en revisor eller en felbehandlad kund.

4. **Vilken MDM-arkitekturstil passar varje domän vi planerar att bemästra, och kan vi försvara det valet mot den störning det innebär för källsystemens ägare?** Stilen ni väljer avgör hur mycket ni kan rensa datan och hur mycket ni tränger in på de team som äger källorna, och att välja efter mode eller leverantörspitch snarare än verkligheten kontroll mot störning är hur program stannar halvvägs. Ett register bevisar värde billigt men rättar aldrig en källa. En centraliserad hubb ger starkast konsekvens men flyttar var poster skapas, vilket är en organisatorisk förändring förklädd till en teknisk. Ta med, för varje kandidatdomän, en ärlig läsning av hur mycket befogenhet ni faktiskt har över källägarna, hur färska nedströmskopior måste vara och vad en återskrivning skulle bryta i befintliga arbetsflöden. I företags- och myndighetssammanhang, lägg till migrerings- och förändringshanteringskostnaden för att flytta systemet där sanningen finns, eftersom de team vars dagliga arbete flyttas kommer att motsätta sig en hubb de inte rådfrågades om, och en avstannad samexistensutrullning är dyrare än ett blygsamt register som levereras.

5. **Hur justerar vi matchningströsklarna, och har vi kommit överens om vilken andel falska sammanslagningar och missade matchningar vi kan leva med i varje domän?** Varje probabilistisk matchningsmotor byter falska sammanslagningar (att fusera två verkliga entiteter) mot missade matchningar (att lämna en entitet delad), och balansen är ett affärsbeslut, inte en standard någon lämnade i verktyget. Sätt auto-sammanslagnings- och auto-avvisningsbanden för breda och ni korrumperar gyllene poster tyst. Sätt dem för smala och den mänskliga granskningskön växer fortare än förvaltare kan tömma den. Ta med den nuvarande säkerhetsfördelningen, granskningsköns storlek och ålder och exempel på fel av båda slagen så att rummet kan se den verkliga kostnaden för varje riktning. I en identitetsdomän hos en myndighet, luta hårt mot missade matchningar och mänsklig granskning, eftersom en felaktig sammanslagning kan neka en förmån eller exponera en medborgares data för en annan, och överklagande- och revisionskostnaden för det felet överskuggar kostnaden för en dubblett som en förvaltare löser nästa vecka.

6. **Hur får nedströmssystem veta att en gyllene post ändrats, och hur inaktuellt kan vart och ett vara innan ett beslut går fel?** En perfekt upplöst gyllene post som inget system konsumerar är ett dyrt kalkylblad, och spridningsmekanismen, vare sig ändringshändelser, ett prenumerations-API eller en nattlig batch, sätter i tysthet hur aktuellt varje beroende beslut är. Händelsedriven spridning håller dussintals konsumenter i nära realtid men kräver idempotenta konsumenter och versionerade händelser. En nattlig synk är enklare men lämnar alla en dag inaktuella, vilket kan vara bra för en marknadsföringslista och farligt för en bedrägerikontroll. Ta med listan över konsumerande system, den färskhet var och en faktiskt behöver och hur en konsument som missar en uppdatering i dag återhämtar sig. För en stor eller offentlig organisation, namnge vem som äger kontraktet för dessa händelser och hur en prenumerant upptäcker ett tappat meddelande, eftersom en entitetsändring som i tysthet misslyckas nå en myndighet återskapar just den fragmentering MDM finansierades för att ta bort.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och ingen livslängd att tillgå, köp inte en MDM-plattform. Bemästra den enda entitet som korrumperar dina tal, vanligen kunden duplicerad över självbetjäning och försäljning, med ett matchningsjobb i det datalager du redan kör och en person som granskar osäkra matchningar varje vecka. Håll varje sammanslagning loggad och reversibel så att en dålig regel kostar en eftermiddag, inte en kundrelation, och återkom till tyngre verktyg först när den manuella granskningskön växer ur en enda granskare.

**Småföretag.** Du har ingen dataförvaltare och en snäv budget, så behandla detta som ett köpa-inte-bygga-beslut och lita på standarder du får gratis. Föredra verktyg som redan deduplicerar kontakter och talar ISO:s lands- och valutakoder framför en skräddarsydd hubb du inte kan underhålla och välj den enda domän, typiskt kunder eller produkter, där dubbletter kostar dig verkliga pengar. Tilldela ansvaret till en namngiven ägare även om det är en bråkdel av en persons vecka, eftersom ordförråd som driftar utan att någon bevakar det är det som i tysthet bryter dina rapporter.

**Storföretag.** Över ett dussin ERP- och CRM-system ackumulerade genom förvärv är arbetet portföljstyrning: rangordna domäner efter kostnaden för deras duplicering, sätt upp bemyndigade förvaltare i verksamheten och standardisera överlevnadsregler och versionering av referensdata så att grupper slutar lösa samma matchningsproblem på nytt. Budgetera integrations- och permanent förvaltningskostnad uttryckligen, sprid gyllene poster som versionerade händelser så att källor förbättras över tid och hantera MDM som ett uppmätt program med dubblettfrekvenser och mått för granskningskön snarare än en engångsstädning.

**Offentlig sektor.** Upphandlingsregler, strikt datadelningslagstiftning och offentlig ansvarsskyldighet formar varje val. Nyckla personentiteten på en styrd nationell identifierare, versionera referensdata efter ikraftträdandedatum så att historiska poster förblir korrekta och gör identitetsupplösningen medvetet konservativ: osäkra matchningar går till utbildade förvaltare, aldrig automatiska sammanslagningar, eftersom en felaktig sammanslagning kan neka en förmån eller läcka en medborgares data till en annan. Logga varje matchning för revision och överklagande, kräv dataportabilitet och redovisad matchningslogik från leverantörer och håll hela förmågan inom de interoperabilitetsstandarder den offentliga sektorn redan förbundit sig till.

## Exempel

**Startup.** Ett snabbväxande mjukvaruföretag säljer både genom registrering i självbetjäning och genom ett säljteam, och de två kanalerna skapar samma kund två gånger under något olika företagsnamn. Intäkt per konto ser fel ut och säljteamet fortsätter ringa kallt till befintliga användare. I stället för att köpa en tung plattform börjar de med ett lättviktigt register: ett matchningsjobb i sitt datalager som länkar poster via e-postdomän och normaliserat företagsnamn, med en deltidsförvaltare som granskar de osäkra matchningarna varje vecka. Det kostar lite, rättar rapporteringsfelet och bevisar det värde som motiverar mer investering när de växer.

**Storföretag.** En global tillverkare har vuxit genom förvärv och kör ett dussin ERP- och CRM-system, vart och ett med egna leverantörsposter, så samma leverantör förekommer på femton sätt och företaget kan inte förhandla som en enda köpare eller se sin sanna utgift. Det sätter upp en MDM-hubb i samexistensstil för leverantörs- och produktdomänerna, med deterministisk matchning på skatte- och registreringsidentifierare plus probabilistisk poängsättning på namn och adresser. Namngivna förvaltare inom inköp justerar överlevnadsreglerna och arbetar granskningskön, och gyllene poster publiceras som ändringshändelser som flödar tillbaka in i varje ERP så att rensad data förbättrar källorna. Konsoliderad utgiftssynlighet låser upp bättre avtalsvillkor, och den avstämningsskatt som slukade ekonomi varje kvartal faller kraftigt.

**Offentlig sektor.** En nationell regering vill att myndigheter ska behandla en medborgare som en person i stället för en främling vid varje lucka, samtidigt som strikta rättsliga gränser för datadelning respekteras. Den bygger en centraliserad masterdatahubb för personentiteten, nycklad på en styrd nationell identifierare, med referensdata versionerad efter ikraftträdandedatum så att historiska poster förblir korrekta. Identitetsupplösningen är medvetet konservativ: osäkra matchningar går till utbildade förvaltare i stället för automatiska sammanslagningar, eftersom en felaktig sammanslagning kan neka någon en förmån eller exponera deras data, och varje matchning loggas för revision och överklagande. Utdelningen är färre duplicerade poster, mindre bedrägeri från delade identiteter och en medborgare som inte behöver bevisa vem hen är vid varje dörr, inom de interoperabilitetsstandarder som behandlas i kapitel 3.8.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på MDM kommer av att ta bort en skatt de flesta organisationer betalar utan att namnge den. Duplicerade och motstridiga poster kostar pengar på uppenbara sätt (bortkastad marknadsföring till samma person fem gånger, leveransfel från inaktuella adresser, missade volymrabatter) och på mindre uppenbara sätt (analytiker som avstämmer antal, chefer som beslutar på tal som i tysthet är fel, revisorer som fakturerar timmar för att reda ut vilken post som är den riktiga). En konsoliderad leverantörsbild betalar ofta för hela programmet enbart genom bättre avtalsvillkor.

Den totala ägandekostnaden har tre delar: plattformen eller bygget, integrationen mot källor och konsumenter och, störst över tid, den löpande förvaltningen. Integrationskostnaden är lätt att underskatta, eftersom att koppla ihop ett dussin åldrande källsystem är där MDM-program blöder tidplan och budget, och förvaltningskostnaden är lätt att glömma, eftersom den är en permanent driftkostnad, inte ett engångsbygge. För att driva ärendet inför ledningen, knyt MDM till tal de redan följer: intäktsnoggrannhet, marknadsföringseffektivitet, inköpsbesparingar, revisionskostnad och regulatorisk risk, och börja sedan snävt och låt en uppmätt vinst på en domän med hög smärta finansiera expansionen.

## Antimönster och fallgropar

- **Koka-havet-omfattning:** att bemästra varje domän på en gång, leverera ingenting på åratal och förlora sponsorskap före den första vinsten.
- **Verktyg före styrning:** att köpa en MDM-plattform innan förvaltare och ägare namngivits, så att motorn saknar förare.
- **Deltidsförvaltare utan befogenhet:** att tilldela förvaltning på en bild utan verkligt mandat eller skyddad tid.
- **Tyst överlevnad:** att slå ihop poster efter verktygsstandard eller laddningsordning, utan skrivna regler och utan sätt att förklara en gyllene post.
- **Irreversibla sammanslagningar:** att slå ihop osäkra matchningar automatiskt utan ångra, så att en felaktig fusion av två verkliga entiteter blir permanent skada.
- **Referensdata överskrivet på plats:** att redigera kodlistor utan versionering och bryta varje historisk rapport som var korrekt under de gamla koderna.
- **Gyllene poster ingen konsumerar:** att bygga en skinande hubb som inget nedströmssystem prenumererar på, så att den rena datan aldrig når beslut.
- **Att uppfinna standardkoder på nytt:** att skapa egna lands- eller valutalistor när ISO-standarder finns och förlora interoperabilitet utan anledning.

## Mognadsmodell

- **Nivå 1, Initiera:** Master- och referensdata är ohanterade. Samma entitet finns många gånger utan auktoritativ version, kodlistor divergerar, matchning är manuell och reaktiv och ingen äger problemet, så antal av kärnentiteter är oeniga och ingen kan säga vilket som är rätt.
- **Nivå 2, Utveckla:** Nyckeldomäner är erkända och någon deduplicerar dem, ofta i datalagret för rapportering. Grundläggande deterministisk matchning finns, referenslistor är insamlade och några personer fungerar som informella förvaltare, men praxis varierar team för team, källorna förblir stökiga och regler bor i människors huvuden snarare än på papper.
- **Nivå 3, Standardisera:** MDM är ett styrt program som tillämpas konsekvent över organisationen. Masterdomäner har namngivna ägare och bemyndigade förvaltare, matchnings- och överlevnadsregler är dokumenterade och upprätthållna, gyllene poster produceras och sprids till konsumenter och referensdata är versionerad och publicerad med ikraftträdandedatum som ett API.
- **Nivå 4, Hantera:** Programmet mäts och styrs mot utgångslägen. Dubblettfrekvenser, fördelningar av matchningssäkerhet, andel falska sammanslagningar och missade matchningar, fullständighet i nyckelfält samt granskningsköns storlek och ålder följs som mått. Trösklar justeras mot de talen snarare än på känsla, och MDM-värde (intäktsnoggrannhet, inköpsbesparingar, granskningskostnad) kvantifieras och rapporteras till ägare med fast takt.
- **Nivå 5, Orkestrera:** Gyllene poster flödar som versionerade händelser i nära realtid, matar det semantiska lagret och är betrodda i hela organisationen. Matchning förbättras kontinuerligt mot uppmätta utfall, bemästring sträcker sig till nya domäner som en upprepbar förmåga och MDM är integrerat med styrning och riskplanering så att programmet anpassas när källor, standarder och entitetslandskapet skiftar.

## Idéer för diskussion

1. Om två av era system är oeniga om hur många kunder ni har, vilket är rätt, och hur skulle ni bevisa det?
2. Vilken masterdatadomän skulle leverera den största mätbara vinsten om ni bemästrade den först, och vad är den vinsten värd?
3. Var skulle probabilistisk matchning hjälpa er i dag, och är ni bekväma med den enstaka felaktiga sammanslagning den innebär?
4. Hur versionerar ni er referensdata, och vad går sönder i era historiska rapporter när en kod ändrar betydelse?
5. Vem är den namngivna förvaltaren för er viktigaste entitet, och har hen befogenhet och tid att faktiskt göra jobbet?
6. När en gyllene post ändras, hur får era nedströmssystem veta det, och hur inaktuella kan de vara innan det gör ont?

## Viktigaste punkter

- Sortera din data i master-, referens- och transaktionsdata. Investera matchning och styrning där duplicering kostar mest.
- Producera en gyllene post per verklig entitet, sammansatt av uttryckliga, reversibla, loggade överlevnadsregler.
- Välj en MDM-arkitekturstil (register, konsolidering, samexistens eller centraliserad hubb) efter din aptit för kontroll och störning.
- Behandla referensdata som versionerat gemensamt ordförråd, föredra erkända standarder och skriv aldrig över kodlistor på plats.
- MDM lyckas på styrning och förvaltning, inte verktyg. Sprid gyllene poster som händelser och mät programmet efter förbättrade beslut.

## Referenser och vidare läsning

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
